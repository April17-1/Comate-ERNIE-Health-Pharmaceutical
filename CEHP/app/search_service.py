# app/search_service.py

import jieba
from collections import Counter
from typing import List, Tuple
from .db import get_collection
import json


# 根据药品名称取详细信息
def search_name_detail(drug_name: str) -> List[str]:
    collection = get_collection()
    res = collection.find({"药品名称": drug_name}).limit(1)
    first_document = res.next()

    # 拷贝一份，去掉 _id，避免 ObjectId 序列化问题
    doc_copy = dict(first_document)
    doc_copy.pop("_id", None)

    # 转成格式化 JSON 字符串，前端弹窗直接展示
    detail_json = json.dumps(doc_copy, ensure_ascii=False, indent=2)

    ldata = [
        doc_copy.get("药品名称", "---"),
        doc_copy.get("处方类型", "---"),
        doc_copy.get("用法用量", "---"),
        doc_copy.get("适应症", "---"),
        doc_copy.get("副作用", "尚不明确。"),
        doc_copy.get("禁忌", "---"),
        doc_copy.get("储藏方法", "尚未说明。"),
        detail_json,                 # ✅ 新增：完整 JSON 字符串
    ]
    return ldata



def jieba_cut(string: str) -> List[str]:
    seg_list = jieba.cut(string, cut_all=False)
    return [word.strip() for word in seg_list if word.strip()]


def merge_and_count_elements(lst: List[str]) -> Tuple[List[str], List[int]]:
    counter = Counter(lst)
    merged_list = []
    merged_count = []
    for element, count in counter.items():
        merged_list.append(element)
        merged_count.append(count)
    return merged_list, merged_count


def jieba_search(word_list: List[str]) -> Tuple[List[str], List[int]]:
    collection = get_collection()

    # 按第一个分词做正则查询
    query = {
        "药品名称": {
            "$regex": f".*{word_list[0]}.*",
            "$options": "i"
        }
    }
    results = collection.find(query, {"药品名称": 1, "_id": 0})
    results_list = list({r["药品名称"] for r in results})



    # 结果太多时，用后续分词再过滤
    if len(results_list) > 100 and len(word_list) > 1:
        for word in word_list:
            new_list = [name for name in results_list if word.lower() in name.lower()]
            if not new_list:
                break
            results_list = new_list


    print(f"搜索结果：{results_list},共计：{len(results_list)}")

    return merge_and_count_elements(results_list)


def levenshtein_distance(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,
                    dp[i][j - 1] + 1,
                    dp[i - 1][j - 1] + 1
                )
    return dp[m][n]


def find_common_ordered_subset(a: str, b: str):
    common_subset = ""
    i = 0
    for char_a in a:
        for char_b in b[i:]:
            if char_a == char_b:
                common_subset += char_a
                i = b.index(char_b) + 1
                break
    if len(common_subset) >= 2:
        return len(common_subset)
    else:
        return False


def sort_lists(list1, list2, list3):
    combined = zip(list3, list1, list2)
    sorted_combined = sorted(combined)
    sorted_list3, sorted_list1, sorted_list2 = zip(*sorted_combined)
    return list(sorted_list1), list(sorted_list2), list(sorted_list3)


def perform_search(query: str) -> List[list]:
    word_list = jieba_cut(query)
    result1, result2 = jieba_search(word_list)
    result3 = []

    # 构建 query 的“抽象字符串”
    querydict = {}
    for i, w in enumerate(word_list):
        querydict[w] = chr(i + 65)
    querystr = "".join(querydict[w] for w in word_list)

    # 为每个候选药品构建抽象字符串并计算距离
    for name in result1:
        tokens = jieba_cut(name)

        count = len(word_list)
        resultdict = {}
        for t in tokens:
            if t in querydict:
                resultdict[t] = querydict[t]
            else:
                resultdict[t] = chr(count + 65)
                count += 1
        resultstr = "".join(resultdict[t] for t in tokens)

        common_len = find_common_ordered_subset(querystr, resultstr)
        if common_len:
            score = abs(len(resultstr) - len(querystr)) - common_len
        else:
            score = levenshtein_distance(querystr, resultstr)
        result3.append(score)

    if not result1:
        # 没有搜索到结果
        return [
            ['无匹配项', '--', '--', '其他', '个人开发者', '无匹配项', '无匹配项']
        ]

    # 按相似度排序
    sorted_list1, sorted_list2, sorted_list3 = sort_lists(result1, result2, result3)
    # # 取前10个结果
    # run = min(len(sorted_list3), 10)
    # 取所有结果
    run = len(sorted_list3)

    
    search_all = []
    for i in range(run):
        detail = search_name_detail(sorted_list1[i])
        search_all.append(detail)

    return search_all

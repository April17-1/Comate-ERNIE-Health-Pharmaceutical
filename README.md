#### 核心技术支持：Comate、ERNIE 4.5 模型系列开源

# Comate-ERNIE-Health-Pharmaceutical

这是一个医药信息检索 + AI健康咨询的综合性 Web 应用，核心价值在于：  

✅ 降低用户获取药品信息的门槛 

✅ 提供智能化的健康知识服务 

✅ 通过模糊匹配技术提升搜索体验 

✅ 结合 AI 大模型实现智能问答 

项目采用经典的 MVC 架构，代码结构清晰，功能模块划分合理，具有良好的扩展性。



# 快速部署：

## 1.环境准备

### Python

Python环境可以参考文件

envinfo\environment_info.txt

envinfo\requirements.txt

envinfo\conda_packages.txt

但项目所需python版本、库等并不严格，**完全可以自行配置**



### MongoDB

MongoDB基本信息参考下面文件

envinfo\MongoDB_info.txt

项目适配性较好，**同样建议自行配置环境**



### PaddlePaddle/ERNIE-4.5-21B-A3B-Paddle

**🎯** 需在aistudio.baidu.com中自行部署，**也可以选择其他模型**
部署过程参考下面项目文档

https://github.com/PaddlePaddle/FastDeploy/blob/develop/docs/zh/supported_models.md

部署目的是获得大模型API来支持智能助手医药知识问答。



## 2.参数修改

在部署ERNIE-4.5-21B-A3B-Paddle之后，会得到AI Studio 访问令牌


将访问令牌信息填入info.yaml文件中



## 3.程序运行

直接运行run.py

出现如下信息即项目部署成功，可以通过URL访问系统

 * Serving Flask app 'app'
 * Debug mode: off
   WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://10.8.12.103:5000
   Press CTRL+C to quit


# 视频介绍

部署与介绍视频链接：https://live.csdn.net/v/502421?spm=1001.2014.3001.5501


# Comate赋能

## 项目分析

最新版的Comate推出了一个不错的功能，即项目整体分析，这是当前很多大模型面对结构复杂项目分析的瓶颈，但是Comate已经将其应用到代码实现中，效果还不错...

![image-20251125160927202](G:/BLOG/source/_posts/picture/image-20251125160927202.png)

![image-20251125155539037](G:/BLOG/source/_posts/picture/image-20251125155539037.png)



## 核心功能

这里对项目的核心功能进行梳理总结，向用户快速总结项目的核心功能...

![image-20251125155629823](G:/BLOG/source/_posts/picture/image-20251125155629823.png)



## 整体架构

Comate这个板块的分析结果包括技术栈、架构层次、核心模块职责、这些功能可以..

![image-20251125155833200](G:/BLOG/source/_posts/picture/image-20251125155833200.png)

![image-20251125155928131](G:/BLOG/source/_posts/picture/image-20251125155928131.png)



## 数据分析

这个板块的内容Comate分析了数据的实体信息，中间件数据的格式及信息，可以帮助开发者..

![image-20251125155947140](G:/BLOG/source/_posts/picture/image-20251125155947140.png)



## 业务流程

Comate对项目流程与逻辑关联把握能力很强，可以依据代码从各个角度切分，进行流程分析，

**关键算法**：

1. **jieba分词**：将查询词拆分为语义单元
2. **正则匹配**：MongoDB `$regex` 查询
3. 相似度计算：
   - 优先使用"有序公共子集"匹配
   - 回退到Levenshtein距离算法
4. **排序策略**：相似度分数从低到高（越小越相似）

![image-20251125160527765](G:/BLOG/source/_posts/picture/image-20251125160527765.png)



![image-20251125160637925](G:/BLOG/source/_posts/picture/image-20251125160637925.png)



![image-20251125160652142](G:/BLOG/source/_posts/picture/image-20251125160652142.png)



## 开发辅助功能

在开发功能API函数过程中，Comate在脚本中嵌入代码解释、函数注释、调优建议等功能，帮助开发者更好地生成优质代码，更加轻松地理解优质代码，对代码进行快速测试优化...



![image-20251125161354292](G:/BLOG/source/_posts/picture/image-20251125161354292.png)










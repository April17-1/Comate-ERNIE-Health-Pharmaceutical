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

## 一、项目整体解析能力

最新版本的 Comate 引入了“**项目整体分析（Project Overview Analysis）**”能力，这项能力正在突破传统大模型处理复杂结构化软件项目的瓶颈。它能够在无需人工标注的前提下，对大型代码工程进行自动化解析、抽象与总结，并形成可直接用于理解、沟通与文档化的项目画像。

Comate 会自动识别项目的目录结构、技术栈、模块职责、流程逻辑及关键依赖关系，生成高质量的结构化分析结果，为开发者提供一次性鸟瞰整个系统的入口，让项目理解不再依赖资深开发者的口述经验。

这种能力在真实工程中已经展现出不错的效果，尤其适用于接手陌生项目、团队交接、文档缺失或系统重构等场景。

<img width="756" height="629" alt="image-20251125160927202" src="https://github.com/user-attachments/assets/e8842b46-17bf-4bfe-9ffa-710c6104f565" />


<img width="1920" height="1040" alt="image-20251125155539037" src="https://github.com/user-attachments/assets/e17040b4-596a-475f-8936-805afdf4f075" />




## 二、核心功能总结

Comate 会对给定项目进行“要点压缩”，自动梳理系统的核心职责与关键功能模块。这种总结不会停留在表面描述，而是深度解析代码逻辑，用简练语言提取业务主干结构，让用户在数秒内洞悉项目的核心价值。

通过该能力，开发者可以迅速构建对项目的心智模型，包括：

- 项目提供的主要业务能力
- 模块间的调用路径与协作方式
- 各功能的输入输出数据结构
- 整体业务范围与边界

这种“高维度简化”极大降低了理解成本，提高了研发效率。

<img width="1920" height="1040" alt="image-20251125155629823" src="https://github.com/user-attachments/assets/5b2a2b24-0a51-46db-a086-8a841da48454" />




## 三、系统整体架构分析

Comate 的架构理解能力涵盖以下内容：

**技术栈识别**
 自动识别语言栈、框架、依赖库、数据源、基础设施等，建立项目生态全貌。

**架构层级划分**
 推断系统的分层结构（如控制层、服务层、数据层、基础设施层）并指出各层作用。

**核心模块职责**
 分析模块之间的依赖关系、边界划分、调用链路和功能定位。

**跨组件交互模式**
 识别消息队列、缓存、数据库、RPC 调用等交互方式。

这些分析帮助开发者快速定位项目的可演化空间与架构瓶颈，为技术决策提供参考。

<img width="1920" height="1040" alt="image-20251125155833200" src="https://github.com/user-attachments/assets/cba58605-fd02-428a-a0be-bf18c6fa33d1" />


<img width="1920" height="1040" alt="image-20251125155928131" src="https://github.com/user-attachments/assets/64518c32-9f94-4435-8785-842377fbc06e" />




## 四、数据结构与数据链路解析

在数据分析板块中，Comate 会识别：

- 实体对象及其属性
- 数据库表/文档结构
- 中间件消息格式
- 各模块数据输入输出链路

这种数据级解析能力让开发者不仅能看到代码“长什么样”，还能理解数据在系统中的“流动方式”。尤其在调试、重构和跨模块协作时，这类信息极具价值。

<img width="1920" height="1040" alt="image-20251125155947140" src="https://github.com/user-attachments/assets/47c0d744-4a5c-4b3d-8b37-6b2742d4e469" />




## 五、业务流程与关键算法解析

Comate 对项目流程的把握具有精细粒度的深度。它会基于调用关系、逻辑链路、接口输入输出等要素，在代码层面重建系统的业务流程。

这使得流程图和逻辑分析不再依赖人工，还能显著减少逻辑遗漏。

在关键算法识别方面，Comate 能自动抽取项目中使用的主要算法。例如文档中涉及的检索算法路径：

**关键算法**：

1. **jieba分词**：将查询词拆分为语义单元
2. **正则匹配**：MongoDB `$regex` 查询
3. 相似度计算：
   - 优先使用"有序公共子集"匹配
   - 回退到Levenshtein距离算法
4. **排序策略**：相似度分数从低到高（越小越相似）

这种分析方式能让开发者迅速理解代码的“意图”而不是只看到实现细节。

<img width="728" height="720" alt="image-20251125160527765" src="https://github.com/user-attachments/assets/55e22ac5-c218-4bf3-9576-cd4033d913a8" />




<img width="725" height="659" alt="image-20251125160637925" src="https://github.com/user-attachments/assets/850de3cb-82f1-4f06-be64-f0688acdecd8" />




<img width="735" height="484" alt="image-20251125160652142" src="https://github.com/user-attachments/assets/afbda9a5-74a5-40ce-9ff1-5aeeb40dbfed" />




## 六、开发辅助能力

在实际开发场景中，Comate 不仅能阅读代码，还能成为“深度理解型助手”。它可以在脚本中嵌入：

- 代码解释
- 函数注释自动生成
- 性能瓶颈提示
- 优化建议
- 边界条件补齐
- 逻辑风险点检测
- 单元测试自动构造

这种能力让开发者在写代码时就能即时得到“高质量审阅”，形成从撰写到调优的闭环，极大提升开发质量与研发效率。

<img width="1920" height="1040" alt="image-20251125161354292" src="https://github.com/user-attachments/assets/de3cccf0-6520-46cb-be71-317bf2095d37" />



















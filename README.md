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

解压压缩包

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




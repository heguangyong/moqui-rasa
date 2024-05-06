# rasa-moqui

## Rasa 版本和项目依赖
python环境准备   安装python3.10 

```
python3 --version
``` 
```
pip3 --version
```
```
brew update
```
```
brew install python
```
更新pip   

```
pip3 install -U pip
```
代码均在 Rasa 3.6.X 版本中完成。

安装并初始化rasa
``` 
pip3 install rasa
```
查看版本
```
rasa --version
```
rasa环境启动失败，更新  
```
pip install --upgrade rasa
```
初始化项目
```
rasa init
```

完成项目代码的依赖安装。

## 安装依赖

```bash
pip install MicroTokenizer
```

这一步骤是可选的，因为在上一步骤中，已经安装了相关的依赖。

## 自定义组件

自定义组件位于 `rasa_custom_tokenizer/tokenizer.py`

## 激活虚拟环境
```shell
source ./venv/bin/activate
```
## 训练 Rasa 模型

```shell
rasa train
```

## 使用 API 密钥启动 Rasa 动作服务器

```shell
SENIVERSE_KEY=SzmZu0tiBVGGaPB0N rasa run actions
```

`SzmZu0tiBVGGaPB0N` 是我们可以从 [https://www.seniverse.com/](https://www.seniverse.com/) 获取的 API 密钥.

对于 Windows 用户，可以使用直接修改代码的方式，快速更改 API
密钥。具体操作如下：

1. 打开 `service/weather.py` 文件，定位到第 9 行，也就是：
   `KEY = os.getenv("SENIVERSE_KEY", "")  # API key` 这一行
2. 将其中的 `""` 替换成 API 密钥。代码修改效果如下：
   `KEY = os.getenv("SENIVERSE_KEY", "ThisIsYourKey")  # API key`

## 启动 Rasa 服务器

```bash
rasa run --cors "*"
```

## 启动网页客户端

```bash
python -m http.server
```

  

## 使用 API 密钥启动 Rasa 动作服务器
确认moqui API可用  
用户列表：api_url = 'https://d.upservce.com/rest/s1/moqui/users'  
单个用户：api_url = 'https://d.upservce.com/rest/s1/moqui/users/{userId}'



## 有用链接

你可以在[Rasa指南](https://rasa.com/docs/rasa/command-line-interface)中找到更多有关Rasa语法的信息。

你可以阅读[Chatbots with Rasa](https://medium.com/codex/introduction-to-chatbots-with-rasa-python-463d9df058e9#id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6ImUxYjkzYzY0MDE0NGI4NGJkMDViZjI5NmQ2NzI2MmI2YmM2MWE0ODciLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiIyMTYyOTYwMzU4MzQtazFrNnFlMDYwczJ0cDJhMmphbTRsamRjbXMwMHN0dGcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiIyMTYyOTYwMzU4MzQtazFrNnFlMDYwczJ0cDJhMmphbTRsamRjbXMwMHN0dGcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMDM1MjI2OTAwNzc5ODYxMzQ2MTQiLCJlbWFpbCI6ImhlZ3Vhbmd5b25nQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYmYiOjE3MTQyMzE2MzEsIm5hbWUiOiJHdWFuZ3lvbmcgSGUiLCJnaXZlbl9uYW1lIjoiR3Vhbmd5b25nIiwiZmFtaWx5X25hbWUiOiJIZSIsImlhdCI6MTcxNDIzMTkzMSwiZXhwIjoxNzE0MjM1NTMxLCJqdGkiOiI1YjFmYmEzZWEwYTZlNzMzMGIxNTViNGFkMDdkNWUwZmEwMzZlYTY5In0.k0ONP-3Uzo1Edys3Qa3AReAaQyBXz26Ry3xUG9vhUNUCxFfafDO8_fvA-MvUQesiRbXdCCIdNbec4flJnlvoyesmtZ7kDhFifbLYOP9HSq9fhjCLHXmVjXyLkuq7hHqLBw1GE92hcI3sMNWws4K5lJrS8zHDRlWpQ5ypGxR-AoYgkygdk8pL8vMk1Ar8IN50Hvi9I94j5dwRFakix9Ib_igGFltDoPBwwCLTMAXBWOTsgvCQDsgvtVPVEP0Q-Ucp3kamiRfSsgdfkW8ip_uQy25Roht5RaAL0adJAErEchsZ4cIGLg6doL683ASUOwrVqyBinVnK0ynOfDwnAfXEtw)
对Rasa关键知识点有个基本认识。

## 本地测试安装ngrok




 	
	
	
	
	
 
	
	
	
	

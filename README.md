# rasa-moqui
作为一个专业rasa顾问，请从rasa3.6的基础环境开始，项目名称为rasa-moqui 使用rasa的form功能查询rasa的用户列表；

### Installing Rasa Open Source  
python environment setup 安装python3.10   
```
python3 --version
pip3 --version
brew update
brew install python
```  
初始化环境  激活环境 
```
python3.10 -m venv ./venv
source ./venv/bin/activate
```  
更新pip   install rasa    init rasa  
安装rasa依赖环境  运行rasa环境
```
pip3 install -U pip
pip3 install rasa
rasa init
rasa train
rasa shell
rasa test
```

确认moqui API可用  
用户列表：api_url = 'https://d.upservce.com/rest/s1/moqui/users'
单个用户：api_url = 'https://d.upservce.com/rest/s1/moqui/users/{userId}'



本地测试安装ngrok




### Command Line Interface
The command line interface (CLI) gives you easy-to-remember commands for common tasks. This page describes the behavior of the commands and the parameters you can pass to them.

#### Cheat Sheet

| Command                |  Effect |
|------------------------|---|
| rasa init              |  Creates a new project with example training data, actions, and config files. |
| rasa train             |  Trains a model using your NLU data and stories, saves trained model in ./models. |
| rasa interactive       |  Starts an interactive learning session to create new training data by chatting to your assistant. |
| rasa shell             |  Loads your trained model and lets you talk to your assistant on the command line. |
| rasa run               | Starts a server with your trained model.  |
| rasa run actions       |  Starts an action server using the Rasa SDK. |
| rasa visualize         |  Generates a visual representation of your stories. |
| rasa test              |  Tests a trained Rasa model on any files starting with test_. |
| rasa test e2e          |  Runs end-to-end testing fully integrated with the action server that serves as acceptance testing. |
| rasa data split nlu    |Performs a 80/20 split of your NLU training data.|
| rasa data split stories | Do the same as rasa data split nlu, but for your stories data.  |
| rasa data convert      | Converts training data between different formats.  |
| rasa data migrate      | Migrates 2.0 domain to 3.0 format.  |
| rasa data validate     |  Checks the domain, NLU and conversation data for inconsistencies. |
| rasa export	Exports    |  conversations from a tracker store to an event broker. |
| rasa evaluate markers | Extracts markers from an existing tracker store.  |
|  rasa marker upload     | Upload marker configurations to Analytics Data Pipeline  |
|  rasa license    |  Display licensing information. |
|  rasa -h    | Shows all available commands.  |

## 有用链接

你可以在[Rasa指南](https://rasa.com/docs/rasa/command-line-interface)中找到更多有关Rasa语法的信息。


# [Chapter 09] Rasa 的工作原理与扩展性

## Rasa 版本和项目依赖

本书所用代码均在 Rasa 3.0.X 版本中完成。
读者可以使用：

```shell
pip install --no-deps -r ../full_requirements.txt
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
source .venv/bin/activate
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

尝试输入一些查询，例如“上海今天的天气如何”并查看响应。

演示效果如下所示：

![](media/demo.png)

玩得开心！

 	
	
	
	
	
 
	
	
	
	

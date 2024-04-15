# rasa-moqui
此为Rasa适配Moqui交互模块，可适配到多端，web、telegram、rocket.chat等场景使用
### Installing Rasa Open Source
更新pip  
```pip3 install -U pip```  
install rasa  
```pip3 install rasa```   
init rasa  
```rasa init```  



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

 	
	
	
	
	
 
	
	
	
	

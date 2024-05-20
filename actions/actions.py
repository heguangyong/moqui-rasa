# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

import requests
from requests.exceptions import HTTPError

class ActionShowUserInfo(Action):
    """
    every class has just 2 methods: name & run
    """

    def name(self) -> Text:
        """Returns the name of action

        Returns:
            Text: the text we will register in `domain.py`
        """
        return "action_find_userinfo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # we can get values from slots by `tracker` object
        target_userinfo = tracker.get_slot('target_userinfo')

        api_url = "https://d.upservce.com/rest/s1/moqui/users"
        auth_token = 'Basic a2FybWE6QWJjZEAxMjM0'
        headers = {
            'Authorization': auth_token,
            'accept': 'application/json'
        }

        try:
            res = requests.get(f'{api_url}/{target_userinfo}', headers=headers)
            res = res.json()

            if res:
                output = (f"User info is {res} "
                          # 这是硬编码的用户账户对应的自动屏幕链接
                          f"https://d.upservce.com/qapps/tools/Entity/DataEdit/EntityDetail?selectedEntity=moqui.security.UserAccount")
            else:
                output = "Please type in this structure: ID， for example:100000。"
        except HTTPError as e:
            output = f"发生HTTP错误: {str(e)}"
        except Exception as e:
            output = f"发生错误: {str(e)}"
        dispatcher.utter_message(text=output)
        return []

class ActionAskForCredentials(Action):
    def name(self) -> Text:
        return "action_ask_for_credentials"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="请输入您的用户名和密码。")
        return []

class ActionValidateLogin(Action):
    def name(self) -> Text:
        return "action_validate_login"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        username = tracker.get_slot('username')
        password = tracker.get_slot('password')

        api_url = "https://d.upservce.com/rest/s1/moqui/login"
        auth_token = 'Basic a2FybWE6QWJjZEAxMjM0'
        headers = {
            'Authorization': auth_token,
            'Content-Type': 'application/json'
        }
        payload = {
            'username': username,
            'password': password
        }

        try:
            res = requests.post(api_url, json=payload, headers=headers)
            res.raise_for_status()
            res_json = res.json()

            if res_json.get('loginSuccess'):
                user_role = res_json.get('userRole')
                return [SlotSet("user_role", user_role), SlotSet("login_success", True)]
            else:
                dispatcher.utter_message(text="登录失败，请检查您的用户名和密码。")
                return [SlotSet("login_success", False)]
        except HTTPError as e:
            dispatcher.utter_message(text=f"发生HTTP错误: {str(e)}")
            return [SlotSet("login_success", False)]
        except Exception as e:
            dispatcher.utter_message(text=f"发生错误: {str(e)}")
            return [SlotSet("login_success", False)]

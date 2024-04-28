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

BASE_URL = "http://worldtimeapi.org/api/timezone/"


class ActionShowTimeZone(Action):
    """
    every class has just 2 methods: name & run
    """

    def name(self) -> Text:
        """Returns the name of action

        Returns:
            Text: the text we will register in `domain.py`
        """
        return "action_find_timezone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # we can get values from slots by `tracker` object
        target_timezone = tracker.get_slot('target_timezone')
        try:
            res = requests.get(BASE_URL + target_timezone)
            res = res.json()

            if res['utc_offset']:
                output = f"Time zone is {res['utc_offset']}"
            else:
                output = "Please type in this structure: Area/Region"
        except:
            output = 'Ops! There are too many requests on the time zone API. Please try a few moments later...'
        dispatcher.utter_message(text=output)
        return []


class ActionQueryUser(Action):
    def name(self) -> Text:
        return "action_query_user"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict]:
        user_id = tracker.get_slot("user_id")

        if not user_id:
            dispatcher.utter_message("请输入用户ID或用户名。")
            return self._clear_slot_values()

        api_url = 'https://d.upservce.com/rest/s1/moqui/users'
        auth_token = 'Basic a2FybWE6QWJjZEAxMjM0'
        headers = {
            'Authorization': auth_token,
            'accept': 'application/json'
        }

        try:
            response = requests.get(f'{api_url}/{user_id}', headers=headers)
            response.raise_for_status()
            user_json = response.json()

            if user_json:
                self._utter_user_details(dispatcher, user_json)
                return self._set_slot_values(tracker, user_json)
            else:
                dispatcher.utter_message("未找到用户信息。")
                return self._clear_slot_values()

        except HTTPError as e:
            dispatcher.utter_message(f"发生HTTP错误: {str(e)}")
        except Exception as e:
            dispatcher.utter_message(f"发生错误: {str(e)}")

        return []

    def _utter_user_details(self, dispatcher: CollectingDispatcher, user_json: Dict) -> None:
        dispatcher.utter_message(
            template="utter_user_details",
            user_id=user_json.get('userId', ''),
            username=user_json.get('username', ''),
            full_name=user_json.get('userFullName', ''),
            email=user_json.get('emailAddress', '')
        )

    def _set_slot_values(self, tracker: Tracker, user_json: Dict) -> List[Dict]:
        slots_to_set = {
            "user_id": user_json.get('userId', ''),
            "username": user_json.get('username', ''),
            "full_name": user_json.get('userFullName', ''),
            "email": user_json.get('emailAddress', '')
        }

        # Check if slots are already set
        current_slot_values = {slot: tracker.get_slot(slot) for slot in slots_to_set.keys()}

        if current_slot_values != slots_to_set:
            return [SlotSet(slot, value) for slot, value in slots_to_set.items()]
        else:
            return []

    def _clear_slot_values(self) -> List[Dict]:
        return [SlotSet(slot, None) for slot in ["user_id", "username", "full_name", "email"]]

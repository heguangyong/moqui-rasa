from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

from service.normalization import text_to_date
from service.weather import get_text_weather_date
import requests
from requests.exceptions import HTTPError


class WeatherFormAction(Action):
    def name(self) -> Text:
        return "action_weather_form_submit"

    def run(
            self, dispatch: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict]:
        city = tracker.get_slot("address")
        date_text = tracker.get_slot("date-time")

        date_object = text_to_date(date_text)

        if not date_object:  # parse date_time failed
            msg = "暂不支持查询 {} 的天气".format([city, date_text])
            dispatch.utter_message(msg)
        else:
            dispatch.utter_message(templete="utter_working_on_it")
            try:
                weather_data = get_text_weather_date(city, date_object, date_text)
            except Exception as e:
                exec_msg = str(e)
                dispatch.utter_message(exec_msg)
            else:
                dispatch.utter_message(weather_data)

        return []


class QueryUserAction(Action):
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

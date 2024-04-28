from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import requests
BASE_URL = "http://worldtimeapi.org/api/timezone/"
class ActionShowTimeZone(Action):
    """
    every class has just 2 methods:name & run
    """
    def name(self) -> Text:
        """Return the name of action

        Returns:
            Text: the text we will register in 'domain.py'
        """
        return "action_find_timezone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # we can get values from slots by 'tracker' object
        action_find_timezone = tracker.get_slot('action_find_timezone')
        res = requests.get(BASE_URL+action_find_timezone)
        res = res.json()
        if res['utc_offset']:
            output = f"Time zone is {res['utc_offset']}"
        else:
            output = "Please type in this structure: /Area/Region"
        dispatcher.utter_message(text=output)
        return []

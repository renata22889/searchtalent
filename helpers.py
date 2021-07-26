import os
import requests
import json
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps

def lookup(city, facility, area_of_expertise):
    """Look up quote for symbol."""

    # Contact API
    try:
        # set parameters
        params = [
            ("city", city ),
            ("facility", facility),
            ("area_of_expertise", area_of_expertise),
        ]

        # access data
        url = f"https://recruit-staging.searchtalent.de/medical/get_doctors"
        response = requests.get(url, params)
        data = response.content
        json_data = json.loads(data)
        return json_data["doctors"]

        # response.raise_for_status()
    except requests.RequestException:
        return None



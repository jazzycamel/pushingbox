import requests
import xml.etree.ElementTree as ET
import logging

class PushingBox(object):
    """A very simple Python client for the PushingBox Notification service API."""

    def __init__(self):
        self._endpoint="http://api.pushingbox.com/pushingbox"

    @property
    def endpoint(self):
        """Set the endpoint (URL) for the PushingBox service. Defaults
        to: http://api.pushingbox.com/pushingbox"""
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        self._endpoint=endpoint

    def push(self, device, **kwargs):
        """Push a notification to a device where 'device' is a DeviceID
        for a Scenario created on the PushingBox dashboard.

        Extra URL/scenario arguments are passed as keyword arguments to this
        function, for example, if the Scenario was as follows:

        The $room$ temperature is $temperature$ degrees

        Then the user would call:

        >>> PushingBox().push('<DeviceID>', room='kitchen', temperature='23')
        """
        params=dict(devid=device)
        params.update(kwargs)

        request=requests.get(self._endpoint, params=params)
        if request.status_code==200:
            logging.getLogger(__name__).info("Successfully pushed notification")
            return True

        logging.getLogger(__name__).error(
            "Failed to push notification: HTTP Status Code {0}".format(
                request.status_code))

        responseXML=ET.fromstring(request.text)
        if responseXML.tag.lower() in ('error',):
            logging.getLogger(__name__).error(
                "Failed to push notification: {0}".format(responseXML.text))
        
        return False

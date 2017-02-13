# pushingbox [![Build Status](https://travis-ci.org/jazzycamel/pushingbox.svg?branch=master)](https://travis-ci.org/jazzycamel/pushingbox)
A very simple Python client for the [PushingBox](https://www.pushingbox.com/index.php) Notification service API.

## Installation
Simply install using pip as follows:

`pip install PushingBox`

or clone this repo and run the following:

`python setup.py install`

You will need to install the [requests](http://python-requests.org) module (`pip install -r requirements.txt`).

## Usage
This is extremely simple. First create a 'Scenario' via the [PushingBox dashboard](https://www.pushingbox.com/scenarios.php). This will generate a DeviceID for your scenario, for example: `v0123456789ABCDE`. To use this scenario with this python library is as easy as the following:

```
>>> from PushingBox import PushingBox
>>> pbox=PushingBox()
>>> pbox.push('v0123456789ABCDE')
```

If your Scenario contains variables, as per the following example from the [PushingBox API page](https://www.pushingbox.com/api.php):

`The $room$ temperature is $temperature$ degrees`

then you can pass these variables as keyword arguments to the `push()` method as follows:

`>>> pbox.push('v0123456789ABCDE', room='kitchen', temperature='23')`

Its as simple as that.

# Source: https://docs.edgeimpulse.com/tutorials/tools/apis/studio/customize-the-eon-tuner.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Customize the EON Tuner

<a href="https://colab.research.google.com/github/edgeimpulse/notebooks/blob/main/notebooks/customize-the-EON-Tuner.ipynb" target="_blank">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Google Colab" noZoom />
</a>

The EON Tuner is Edge Impulse's AutoML (automated machine learning) tool to help you find and select the best embedded machine learning model for your application within the constraints of your target device.

This notebook will show you how to configure and run the EON Tuner programmatically using the [Edge Impulse API](/apis/studio)!

## 1. Setup

This section will set up your environment and API credentials so that you can start making calls to the [Edge Impulse API](/apis/studio) from this notebook. Run this block only once per runtime session, or every time you:

* Open the notebook on your browser or IDE to start working on it, or
* restart the runtime, or
* change the project you are working on

[API documentation](/apis)

### 1.1 Update your `PROJECT_ID`

You will need to enter the correct `PROJECT_ID` for the project you want to work with, in the code in section 1.3 below. The project ID can be obtained from your Edge Impulse Project's Dashboard under the **Project Info** section.

### 1.2 Obtain your API Key

The block below will prompt you for your project's API Key. You can obtain this key from your Project's Dashboard, by selecting the **Keys** tab from the top navigation bar.

### 1.3 Run the setup block

Run the block below and enter your API key when prompted. Then continue to the next section.

```python  theme={"system"}
import getpass
import requests
import json
import pytz
from datetime import datetime
import time
import sys

PROJECT_ID = 94424  #👈🏼 Update as necessary!

URL_STUDIO = "https://studio.edgeimpulse.com/v1/api/"
URL_PROJECT = URL_STUDIO + str(PROJECT_ID)
KEY = getpass.getpass('Enter your API key: ')
API_HEADERS = {
    "Accept": "application/json",
    "x-api-key": KEY  #👈🏼 Update as necessary!
}


def get_eon_info(project, response_key):
    response = requests.get(URL_STUDIO + str(project) + "/optimize/state",
                            headers=API_HEADERS)
    if response.ok:
        return json.loads(response.text)[response_key]

response = requests.get(URL_PROJECT, headers=API_HEADERS)
if response.ok:
    data = json.loads(response.text)
    print(json.dumps(data, indent=2))
else:
    print("\n⛔️ An Error Ocurred, do you have the correct project ID?")
```

## 2. Customization

You can use the code in section 2.2 below to programmatically update the configuration of the EON Tuner.

### 2.1 Enable advanced EON Tuner mode (optional)

In basic mode (the default) you will be able to modify the `datasetCategory`, `targetLatency` and `targetDevice`. For additional control, ask your User Success or Solutions Engineer to enable the EON Tuner advanced mode for you.

### 2.2 Update the EON Tuner configuration

```python  theme={"system"}
if "running" == get_eon_info(PROJECT_ID, "status")["status"]:
    print(
        "EON Tuner job is running, run section 2.4 to track the job's progress."
    )
else:
    payload = {
        "datasetCategory": # Select one of:
            # "speech_keyword"
            # "speech_continuous"
            # "audio_event"
            # "audio_continuous"
            # "transfer_learning"
            # "motion_event"
            # "motion_continuous"
            # "audio_syntiant"
            "audio_continuous",
        "targetLatency": 500,  # Latency in ms
        "targetDevice": {
            "name":  # Select one of:
            # cortex-m4f-80mhz
            # cortex-m7-216mhz
            # st-iot-discovery-kit
            # arduino-nano-33-ble
            # nordic-nrf52840-dk
            # nordic-nrf5340-dk
            # nordic-nrf9160-dk
            # silabs-thunderboard-sense-2
            # silabs-xg24
            # synaptics-ka10000
            # himax-we-i
            # wio-terminal
            # sony-spresense
            # ti-launchxl
            # portenta-h7
            # mbp-16-2020
            # raspberry-pi-4
            # raspberry-pi-rp2040
            # jetson-nano
            "jetson-nano",
            "ram": 262144,  # Memory in bytes
            "rom": 1048576  # Memory in bytes
        },
        "trainingCycles": 10,  # Default 100
        "tuningMaxTrials": 3,  # Default 30
        "tuningWorkers": 9,  # Default 3
        "minMACCS": 100,  # Default 0
        "maxMACCS": 1750,  # Default 1750000
        "tuningAlgorithm": # Select one of:
        # "random"
        # "hyperband"
        # "bayesian"
        "random"
    }
    response = requests.post(URL_PROJECT + "/optimize/config",
                            headers=API_HEADERS,
                            json=payload)
    if response.ok:
        # Show me the new configuration
        response = requests.get(URL_PROJECT + "/optimize/state", headers=API_HEADERS)
        if response.ok:
            print("EON Tuner configuration updated successfully!")
            print(json.dumps(get_eon_info(PROJECT_ID, "config"), indent=2))
```

### 2.3 Start the EON Tuner

Run the cell below to start spinning up EON Tuner optimization jobs. If your project is already running an EON Tuner optimization, go instead to section 2.4 to track the job's progress.

```python  theme={"system"}
if "running" == get_eon_info(PROJECT_ID, "status")["status"]:
    print(
        "EON Tuner job is running, run section 2.4 to track the job's progress."
    )
else:
    response = requests.post(URL_PROJECT + "/jobs/optimize", headers=API_HEADERS)
    if response.ok:
        data = json.loads(response.text)
        print("EON Tuner job %s started successfully!" % data["id"])
        # print(json.dumps(data, indent=2))
```

### 2.4 Track the EON Tuner optimization progress

Run the cell below to track the progress of your EON Tuner job. You can safely stop and restart the cell at any time since this will not affect the running EON Tuner jobs.

```python  theme={"system"}
finished = False
job_id = get_eon_info(PROJECT_ID, "activeTunerJobId")

while not finished:
    response = requests.get(URL_PROJECT + "/jobs/" + str(job_id) + "/status", headers=API_HEADERS)
    if response.ok:
        job_status = json.loads(response.text)
        if "finishedSuccessful" in job_status["job"].keys():
            print("\nJob completed")
            finished = True
        else:
            response = requests.get(URL_PROJECT + "/optimize/state", headers=API_HEADERS)
            if response.ok:
                status = json.loads(response.text)["status"]
                started = datetime.fromisoformat(job_status["job"]["started"].replace("Z", "+00:00"))
                for iter in range(30):
                    now = datetime.now(pytz.utc)
                    diff = now - started
                    sys.stdout.write("\r[%s] " % diff) # Back to the beginning
                    for x in range(status["numCompletedTrials"]):
                        sys.stdout.write("█")
                    for x in range(status["numRunningTrials"]):
                        sys.stdout.write("▒")
                    for x in range(status["numPendingTrials"]):
                        sys.stdout.write(" ")
                    total = status["numCompletedTrials"] + status[
                        "numRunningTrials"] + status["numPendingTrials"]
                    sys.stdout.write(" %d/%d" % (status["numCompletedTrials"], total))
                    time.sleep(1)

```

### 2.5 Get the EON Tuner optimization results

Use the cell below to retrieve the EON Tuner optimization results and save them to the `trials` variable.

```python  theme={"system"}
trials = get_eon_info(PROJECT_ID, "trials")
print(trials[0].keys())
```


Built with [Mintlify](https://mintlify.com).
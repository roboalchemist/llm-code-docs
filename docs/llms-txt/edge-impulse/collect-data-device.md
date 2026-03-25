# Source: https://docs.edgeimpulse.com/tutorials/tools/apis/studio/collect-data-device.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Collect data from a device

<a href="https://colab.research.google.com/github/edgeimpulse/notebooks/blob/main/notebooks/collect-data-from-board.ipynb" target="_blank">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Google Colab" noZoom />
</a>

## 1. Obtain an API key from your project

Your project API key can be used to enable programmatic access to Edge Impulse. You can create and/or obtain a key from your project's Dashboard, under the `Keys` tab. API keys are long strings, and start with `ei_`:

<Frame caption="Project API Key">
  <img src="https://raw.githubusercontent.com/edgeimpulse/notebooks/main/.assets/images/project-key.png" />
</Frame>

## 2. Connect your development kit to your project

Open a terminal and run the Edge Impulse daemon. The daemon is the service that connects your hardware with any Edge Impulse project:

```shell  theme={"system"}
edge-impulse-daemon --api-key <your project API key>
```

## 3. Obtain your project's ID

Copy your project's ID from the project's Dashboard under the `Project Info` section:

<Frame caption="Project API Key">
  <img src="https://raw.githubusercontent.com/edgeimpulse/notebooks/main/.assets/images/project-id.png" />
</Frame>

## 4. Setup API Connection

Replace the `PROJECT_ID` below with the ID of your project you selected and enter your API key when prompted:

```python  theme={"system"}
import requests
import getpass
import json

URL_STUDIO = "https://studio.edgeimpulse.com/v1/api/"
PROJECT_ID = int(input('Enter your Project ID: '))
AUTH_KEY = getpass.getpass('Enter your API key: ')


def check_response(response, debug=False):
    if not response.ok:
        raise RuntimeError("⛔️ Error\n%s" % response.text)
    else:
        if debug:
            print(response)
        return response


def do_get(url, auth, debug=False):
    if debug:
        print(url)
    response = requests.get(url,
                            headers={
                                "Accept": "application/json",
                                "x-api-key": auth
                            })
    return check_response(response, debug)


def parse_response(response, key=""):
    parsed = json.loads(response.text)
    if not parsed["success"]:
        raise RuntimeError(parsed["error"])
    if key == "":
        return json.loads(response.text)
    return json.loads(response.text)[key]


def get_project(project_id, project_auth, debug=False):
    response = do_get(URL_STUDIO + str(project_id), project_auth)
    return parse_response(response, "project")


print("Project %s is accessible" % get_project(PROJECT_ID, AUTH_KEY)["name"])
```

## 5. Get the ID of the connected device

```python  theme={"system"}
# https://studio.edgeimpulse.com/v1/api/{projectId}/devices

def get_devices(project_id, project_auth, debug=False):
    response = do_get(URL_STUDIO + str(project_id) + "/devices", project_auth)
    return parse_response(response, "devices")


device_id = ""
for device in get_devices(PROJECT_ID, AUTH_KEY):
    # if device["remote_mgmt_connected"] and device["supportsSnapshotStreaming"]:
    if device["remote_mgmt_connected"]:
        device_id = device["deviceId"]
        print("Found %s (type %s, id: %s)" %
              (device["name"], device["deviceType"], device_id))
        break
if device_id == "":
    print(
        "Could not find a connected device that supports snapshot streaming!")
```

## 6. Trigger data sampling

```python  theme={"system"}
# https://studio.edgeimpulse.com/v1/api/{projectId}/device/{deviceId}/start-sampling

SAMPLE_CATEGORY = "testing"
SAMPLE_LENGTH_MS = 20000
SAMPLE_LABEL = "squat"

def do_post(url, payload, auth, debug=False):
    if debug:
        print(url)
    response = requests.post(url,
                             headers={
                                 "Accept": "application/json",
                                 "x-api-key": auth
                             },
                             json=payload)
    return check_response(response, debug)


def collect_sample(project_id, device_id, project_auth, debug=False):
    payload = {
        "category": SAMPLE_CATEGORY,
        # "Microphone", "Inertial", "Environmental" or "Inertial + Environmental"
        "sensor": "Inertial",
        # The inverse of frequency in Hz
        "intervalMs": 10,
        "label": SAMPLE_LABEL,
        "lengthMs": SAMPLE_LENGTH_MS
    }
    response = do_post(
        URL_STUDIO + str(project_id) + "/device/" + str(device_id) +
        "/start-sampling", payload, project_auth, debug)
    return parse_response(response, "id")


print("Sample request returned", collect_sample(PROJECT_ID, device_id, AUTH_KEY))
```


Built with [Mintlify](https://mintlify.com).
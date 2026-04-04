# Source: https://docs.port.io/build-your-software-catalog/custom-integration/api/ci-cd/gitlab-pipelines.md

# Gitlab CI Pipelines

Using Gitlab CI Pipelines, you can easily create/update and query entities in Port.

<br />

<br />

![Github Illustration](/assets/images/gitlab-pipelines-illustration-4b516fdb48ad47b4da483e8cb0a8f71d.png)

## ð¡ Common Gitlab CI Pipelines usage[â](#-common-gitlab-ci-pipelines-usage "Direct link to ð¡ Common Gitlab CI Pipelines usage")

Port's API allows for easy integration between Port and your Gitlab CI Pipeline jobs, for example:

* Report the status of a running **CI job**;
* Update the software catalog about a new **build version** for a **microservice**;
* Get existing **entities**.

## Setup[â](#setup "Direct link to Setup")

To interact with Port using Gitlab CI Pipeline, you will first need to [define your Port credentials](https://docs.gitlab.com/ee/ci/variables/index.html#define-a-cicd-variable-in-the-ui) as variables for your pipeline. Then, pass the defined variables to your ci pipeline script, for example, `Python`:

```
image: python:3.9

variables:
  PORT_CLIENT_ID: $PORT_CLIENT_ID # The variable name for your Port clientId
  PORT_CLIENT_SECRET: $PORT_CLIENT_SECRET # The variable name for your Port clientSecret

report_to_port:
  stage: build
  script:
    - python main.py
```

Make sure you have an existing [Blueprint](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/.md) in your Port installation to create/update entities.

## Working with Port's API[â](#working-with-ports-api "Direct link to Working with Port's API")

Here is an example snippet showing how to integrate a job that uses Port's API with your existing Gitlab CI pipelines using Python:

Add the following task to your Gitlab pipeline:

Gitlab pipeline YAML

```
image: python:3.9

variables:
  PORT_CLIENT_ID: $PORT_CLIENT_ID
  PORT_CLIENT_SECRET: $PORT_CLIENT_SECRET

stages:
  - build

report_to_port:
  stage: build
  before_script:
    - python -m pip install --upgrade pip
    - pip install -r requirements.txt
  script:
    - python main.py
```

<br />

note

In the following example, we use Python modules which need to be installed. You can use the following `requirements.txt`:

port\_requirements.txt

```
requests>=2.28.2
```

* Create/Update
* Get

Create the following Python script in your repository to create or update Port entities as part of your pipeline:

```
import os
import requests
import json

# These are the credentials passed by the variables of your pipeline to your tasks and in to your env
CLIENT_ID = os.environ['PORT_CLIENT_ID']
CLIENT_SECRET = os.environ['PORT_CLIENT_SECRET']
API_URL = 'https://api.port.io/v1'

credentials = {
    'clientId': CLIENT_ID,
    'clientSecret': CLIENT_SECRET
}
token_response = requests.post(f"{API_URL}/auth/access_token", json=credentials)
# use this access token + header for all http requests to Port
access_token = token_response.json()['accessToken']

headers = {
    'Authorization': f'Bearer {access_token}'
}

entity_json = {
        "identifier": "example-entity",
        "properties": {
          "myStringProp": "My value",
          "myNumberProp": 1,
          "myBooleanProp": true,
          "myArrayProp": ["myVal1", "myVal2"],
          "myObjectProp": {"myKey": "myVal", "myExtraKey": "myExtraVal"}
      }
}

# request url : {API_URL}/blueprints/<blueprint_id>/entities
create_response = requests.post(f'{API_URL}/blueprints/test-blueprint/entities?upsert=true', json=entity_json, headers=headers)
print(json.dumps(get_response.json(), indent=4))
```

Create the following Python script in your repository to get Port entities as part of your pipeline:

```
import os
import requests
import json

# These are the credentials passed by the variables of your pipeline to your tasks and in to your env
CLIENT_ID = os.environ['PORT_CLIENT_ID']
CLIENT_SECRET = os.environ['PORT_CLIENT_SECRET']
API_URL = 'https://api.port.io/v1'

credentials = {
    'clientId': CLIENT_ID,
    'clientSecret': CLIENT_SECRET
}

token_response = requests.post(f'{API_URL}/auth/access_token', json=credentials)
# use this access token + header for all http requests to Port
access_token = token_response.json()['accessToken']
headers = {
  'Authorization': f'Bearer {access_token}'
}

# request url : {API_URL}/blueprints/<blueprint_id>/entities/<entity_id>
get_response = requests.get(f"{API_URL}/blueprints/test-blueprint/entities/test-entity", headers=headers)
print(json.dumps(get_response.json(), indent=4))
```

Selecting a Port API URL by account region

The `port_region`, `port.baseUrl`, `portBaseUrl`, `port_base_url` and `OCEAN__PORT__BASE_URL` parameters select which Port API instance to use:

* **EU** ([app.port.io](https://app.port.io)) â `https://api.port.io`
* **US** ([app.us.port.io](https://app.us.port.io)) â `https://api.us.port.io`

## Examples[â](#examples "Direct link to Examples")

Refer to the [examples](/build-your-software-catalog/custom-integration/api/ci-cd/gitlab-pipelines/examples.md) page for practical examples of working with Port using Gitlab CI Pipelines.

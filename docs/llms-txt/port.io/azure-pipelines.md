# Source: https://docs.port.io/build-your-software-catalog/custom-integration/api/ci-cd/azure-pipelines.md

# Azure Pipelines

Using Azure Pipelines, you can easily create/update and query entities in Port.

<br />

<br />

![Github Illustration](/assets/images/azure-pipelines-illustration-27b43edbd8daf04f7bcf197a3c6bad54.png)

## ð¡ Common Azure Pipelines usage[â](#-common-azure-pipelines-usage "Direct link to ð¡ Common Azure Pipelines usage")

Port's API allows for easy integration between Port and your Azure Pipeline jobs, for example:

* Report the status of a running **CI job**;
* Update the software catalog about a new **build version** for a **microservice**;
* Get existing **entities**.

## Setup[â](#setup "Direct link to Setup")

To interact with Port using Azure Pipelines, you will first need to [define your Port credentials](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/set-secret-variables?view=azure-devops\&tabs=yaml%2Cbash#secret-variable-in-the-ui) as variables for your pipeline. Then, pass the defined variables to your pipeline script, for example, `Python`:

```
- task: PythonScript@0
  env:
    PORT_CLIENT_ID: $(PORT_CLIENT_ID) # The variable name for your Port clientId
    PORT_CLIENT_SECRET: $(PORT_CLIENT_SECRET) # The variable name for your Port clientSecret
  inputs:
    scriptSource: "filePath"
    scriptPath: "main.py"
```

Make sure you have an existing [Blueprint](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/.md) in your Port installation to create/update entities.

## Working with Port's API[â](#working-with-ports-api "Direct link to Working with Port's API")

Here is an example snippet showing how to integrate a job that uses Port's API with your existing Azure pipelines using Python:

Add the following task to your Azure pipeline:

Azure pipeline YAML

```
- script: |
    pip install -r port_requirements.txt
- task: PythonScript@0
  env:
    PORT_CLIENT_ID: $(PORT_CLIENT_ID)
    PORT_CLIENT_SECRET: $(PORT_CLIENT_SECRET)
  inputs:
    scriptSource: "filePath"
    scriptPath: "port.py"
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

credentials = {
    'clientId': CLIENT_ID,
    'clientSecret': CLIENT_SECRET
}
token_response = requests.post(f"{API_URL}/auth/access_token", json=credentials)
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

credentials = {
    'clientId': CLIENT_ID,
    'clientSecret': CLIENT_SECRET
}
token_response = requests.post(f"{API_URL}/auth/access_token", json=credentials)
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

Refer to the [examples](/build-your-software-catalog/custom-integration/api/ci-cd/azure-pipelines/examples.md) page for practical examples of working with Port using Azure Pipelines.

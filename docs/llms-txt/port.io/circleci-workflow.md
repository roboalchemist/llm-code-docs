# Source: https://docs.port.io/build-your-software-catalog/custom-integration/api/ci-cd/circleci-workflow.md

# CircleCI workflows

Using CircleCI workflows, you can easily create/update and query entities in Port.

<br />

<br />

![Github Illustration](/assets/images/circleci-illustration-08476391e6968de3afaf256b27f6ab8c.png)

## ð¡ Common CircleCI workflow usage[â](#-common-circleci-workflow-usage "Direct link to ð¡ Common CircleCI workflow usage")

Port's API allows for easy integration between Port and your CircleCI workflows, for example:

* Report the status of a running **CI job**;
* Update the software catalog about a new **build version** for a **microservice**;
* Get existing **entities**.

## Setup[â](#setup "Direct link to Setup")

To interact with Port using Circle CI, you will first need to set up a [CircleCI context](https://circleci.com/docs/contexts/) in order to save your Port credentials, and pass the context to the relevant workflow.

```
workflows:
  deploy-service:
    jobs:
      - report-to-port:
          context:
            # the CircleCI context name of the credentials
            - port
```

Make sure you have an existing [Blueprint](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/.md) in your Port installation to create/update entities.

## Working with Port's API[â](#working-with-ports-api "Direct link to Working with Port's API")

Here is an example snippet showing how to integrate a job that uses Port's API with your existing CircleCI pipelines using Python:

Add the following job and workflow to your CircleCI pipeline:

CircleCI Pipeline YAML

```
  jobs:
  # ... other jobs
    report-to-port:
      docker:
        - image: cimg/python:3.11
      environment:
        API_URL: https://api.port.io
      steps:
        - checkout
        - run: pip install -r port_requirements.txt
        - run: python get_port_entity.py

workflows:
  # ... other workflows
  deploy-production-service:
    jobs:
      # ... other jobs
      - report-to-port:
        context:
          - port
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

# These are the credentials passed by the 'port' context to your environment variables
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

# These are the credentials passed by the 'port' context to your environment variables
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

Refer to the [examples](/build-your-software-catalog/custom-integration/api/ci-cd/circleci-workflow/examples.md) page for practical examples of working with Port using CircleCI.

# Source: https://docs.port.io/build-your-software-catalog/custom-integration/webhook/examples/codecov.md

# Codecov

In this example you are going to create a webhook integration between [Codecov](https://docs.codecov.com/docs/quick-start) and Port. The integration will facilitate the ingestion of coverage entities into Port.

## Port configuration[â](#port-configuration "Direct link to Port configuration")

Create the following blueprint definitions:

Codecov coverage blueprint

Create in Port

```
{
    "identifier": "codecov_coverage",
    "title": "Codecov Coverage",
    "icon": "Git",
    "schema": {
      "properties": {
        "repository": {
          "title": "Repository",
          "type": "string",
          "format": "url"
        },
        "coverage": {
          "title": "Test Coverage",
          "type": "string"
        },
        "service": {
          "title": "Service",
          "type": "string"
        },
        "author": {
          "title": "Author",
          "type": "string"
        },
        "createdAt": {
          "title": "Created At",
          "type": "string",
          "format": "date-time"
        },
        "files": {
          "title": "Tracked Files",
          "type": "string",
          "description": "Number of files tracked"
        },
        "lines": {
          "title": "Tracked Lines",
          "description": "Number of lines tracked",
          "type": "string"
        },
        "branch": {
          "title": "Branch",
          "type": "string"
        },
        "report": {
          "title": "Full Report Data",
          "type": "object",
          "description": "Detailed information about the codecov report"
        }
      },
      "required": []
    },
    "mirrorProperties": {},
    "calculationProperties": {},
    "aggregationProperties": {},
    "relations": {}
}
```

Create the following webhook configuration [using Port's UI](/build-your-software-catalog/custom-integration/webhook/.md?operation=ui#configuring-webhook-endpoints):

Codecov webhook configuration

1. **Basic details** tab - fill the following details:

   1. Title : `Codecov Mapper`;
   2. Identifier : `codecov_mapper`;
   3. Description : `A webhook configuration to map Codecov coverage to Port`;
   4. Icon : `Git`;

2. **Integration configuration** tab - fill the following JQ mapping:

   ```
   [
       {
         "blueprint": "codecov_coverage",
         "filter": "true",
         "entity": {
           "identifier": ".body.repo.name | tostring",
           "title": ".body.repo.name | tostring",
           "properties": {
             "repository": ".body.repo.url",
             "coverage": ".body.head.totals.coverage",
             "service": ".body.owner.service",
             "author": ".body.head.author.name",
             "createdAt": ".body.head.timestamp | (strptime(\"%Y-%m-%dT%H:%M:%S\") | strftime(\"%Y-%m-%dT%H:%M:%SZ\"))",
             "files": ".body.head.totals.files",
             "lines": ".body.head.totals.lines",
             "branch": ".body.head.branch",
             "report": ".body.head.totals"
           }
         }
       }
   ]
   ```

   Webhook URL

   Take note of, and copy the Webhook URL that is provided in this tab

3. Click **Save** at the bottom of the page.

## Create a webhook in Codecov[â](#create-a-webhook-in-codecov "Direct link to Create a webhook in Codecov")

1. From your Codecov account, open **Settings**;

2. Click on the **Global YAML** tab at the left sidebar menu;

3. In the YAML editor, add the following Codecov configuration to notify Port anytime an event occurs in your code repositories:

   ```
   coverage:
   notify:
       webhook:
       default:
           only_pulls: false
           url: YOUR_PORT_WEBHOOK
   ```

   Webhook URL replacement

   Remember to replace `YOUR_PORT_WEBOOK` with the value of the `URL` you received after creating the webhook configuration in Port.

   notification service customization

   For more information on customizing the notification service, follow this [guide](https://docs.codecov.com/docs/notifications#standard-notification-fields)

4. Click **Save changes** to save the webhook configuration.

For more information on customizing the notification service, follow [this documentation](https://docs.codecov.com/docs/notifications#standard-notification-fields)

All set! When any changes occur in your Codecov account, a webhook event will be triggered to the URL provided by Port. Port will then parse the events based on the mapping and subsequently update the catalog entities.

## Import historical Codecov coverage[â](#import-historical-codecov-coverage "Direct link to Import historical Codecov coverage")

In this example you are going to use the provided Python script to fetch coverage data from Codecov REST API and ingest it to Port.

### Prerequisites[â](#prerequisites "Direct link to Prerequisites")

This example utilizes the same [blueprint and webhook](#port-configuration) definition from the previous section.

In addition, provide the following environment variables:

* `PORT_CLIENT_ID` - Your Port client id
* `PORT_CLIENT_SECRET` - Your Port client secret
* `CODECOV_TOKEN` - Codecov API access token
* `CODECOV_SERVICE_PROVIDER` - Git hosting service provider. Accepts values such as `github`, `github_enterprise`, `bitbucket`, `bitbucket_server`, `gitlab` and `gitlab_enterprise`
* `CODECOV_SERVICE_PROVIDER_ACCOUNT_NAME` - Username from the Git service provider

Credentials

Find your Port credentials using this [guide](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)

Find your Codecov API token using this [guide](https://docs.codecov.com/reference/overview)

Use the following Python script to ingest historical Codecov coverage into port:

Codecov Python script

```
## Import the needed libraries
import requests
from decouple import config
from loguru import logger
from typing import Any

# Get environment variables using the config object or os.environ["KEY"]
# These are the credentials passed by the variables of your pipeline to your tasks and in to your env

PORT_CLIENT_ID = config("PORT_CLIENT_ID")
PORT_CLIENT_SECRET = config("PORT_CLIENT_SECRET")
CODECOV_TOKEN = config("CODECOV_TOKEN")
CODECOV_SERVICE_PROVIDER = config("CODECOV_SERVICE_PROVIDER")
CODECOV_SERVICE_PROVIDER_ACCOUNT_NAME = config("CODECOV_SERVICE_PROVIDER_ACCOUNT_NAME")
CODECOV_API_URL = "https://api.codecov.io/api/v2"
PORT_API_URL = "https://api.port.io/v1"

ALLOWED_SERVICE_PROVIDERS = {
    "github",
    "github_enterprise",
    "bitbucket",
    "bitbucket_server",
    "gitlab",
    "gitlab_enterprise",
}

if CODECOV_SERVICE_PROVIDER not in ALLOWED_SERVICE_PROVIDERS:
    raise ValueError(
        f"Invalid CODECOV_SERVICE_PROVIDER: {CODECOV_SERVICE_PROVIDER}. Allowed values are {', '.join(ALLOWED_SERVICE_PROVIDERS)}"
    )

## Get Port Access Token
credentials = {"clientId": PORT_CLIENT_ID, "clientSecret": PORT_CLIENT_SECRET}
token_response = requests.post(f"{PORT_API_URL}/auth/access_token", json=credentials)
access_token = token_response.json()["accessToken"]

# You can now use the value in access_token when making further requests
port_headers = {"Authorization": f"Bearer {access_token}"}


def add_entity_to_port(blueprint_id: str, entity_object: dict[str, Any]):
    response = requests.post(
        f"{PORT_API_URL}/blueprints/{blueprint_id}/entities?upsert=true&merge=true",
        json=entity_object,
        headers=port_headers,
    )
    logger.info(response.json())


def get_paginated_resource(path: str, query_params: dict[str, Any] = {}):
    logger.info(
        f"Requesting paginated data for path: {path} and params: {query_params}"
    )

    url = f"{CODECOV_API_URL}/{path}"

    while url:
        try:
            response = requests.get(url=url, params=query_params)
            response.raise_for_status()
            page_json = response.json()
            batch_data = page_json["results"]
            yield batch_data

            url = page_json.get("next")

        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP error with info: {e}")
            raise

    logger.info(f"Successfully fetched paginated data for {path}")


def process_repository_entities(repository_data: list[dict[str, Any]]):
    blueprint_id = "codecov_coverage"
    for repo in repository_data:
        report: dict[str, Any] = repo.get("totals", {})
        entity = {
            "identifier": repo["name"],
            "title": repo["name"],
            "properties": {
                "repository": f"https://app.codecov.io/{repo['author']['service']}/{repo['author']['username']}/{repo['name']}",
                "coverage": report.get("coverage") if report else None,
                "service": repo["author"]["service"],
                "author": repo["author"]["name"],
                "createdAt": repo["updatestamp"],
                "files": report.get("files") if report else None,
                "lines": report.get("lines") if report else None,
                "report": report,
                "branch": repo["branch"],
            },
            "relations": {},
        }
        add_entity_to_port(blueprint_id=blueprint_id, entity_object=entity)


if __name__ == "__main__":
    logger.debug("Starting Codecov app")
    repository_path = (
        f"{CODECOV_SERVICE_PROVIDER}/{CODECOV_SERVICE_PROVIDER_ACCOUNT_NAME}/repos"
    )
    for repositories_batch in get_paginated_resource(path=repository_path):
        logger.debug(
            f"Received Codecov repositories batch with size {len(repositories_batch)}"
        )
        process_repository_entities(repository_data=repositories_batch)

    logger.debug("Finished Codecov app")
```

### Running the python script[â](#running-the-python-script "Direct link to Running the python script")

To ingest coverage data from your Codecov account to Port, run the following commands:

```
export PORT_CLIENT_ID=<ENTER CLIENT ID>
export PORT_CLIENT_SECRET=<ENTER CLIENT SECRET>
export CODECOV_TOKEN=<ENTER CODECOV TOKEN>
export CODECOV_SERVICE_PROVIDER=<ENTER CODECOV SERVICE PROVIDER>
export CODECOV_SERVICE_PROVIDER_ACCOUNT_NAME=<ENTER CODECOV SERVICE PROVIDER ACCOUNT NAME>

git clone https://github.com/port-labs/example-codecov-test-coverage.git

cd example-codecov-test-coverage

pip install -r ./requirements.txt

python app.py
```

Python script information

Find more information about the python script [here](https://github.com/port-labs/example-codecov-test-coverage)

Done! you are now able to import historical coverage from Codecov into Port. Port will parse the objects according to the mapping and update the catalog entities accordingly.

## Let's Test It[â](#lets-test-it "Direct link to Let's Test It")

This section includes a sample response data from Codecov. In addition, it includes the entity created from the resync event based on the Ocean configuration provided in the previous section.

### Payload[â](#payload "Direct link to Payload")

Here is an example of the payload structure from Codecov:

**Coverage response data (Click to expand)**

```
{
  "body": {
    "repo": {
      "url": "https://app.codecov.io/gh/slanks/codecov-example",
      "service_id": "742056150",
      "name": "codecov-example",
      "private": false
    },
    "head": {
      "author": {
        "username": "slanks",
        "service_id": "15999660",
        "email": "slanks@email.com",
        "service": "github",
        "name": "PagesCoffy"
      },
      "url": "https://app.codecov.io/gh/slanks/codecov-example/commit/a7794fc92007d3a1b99066c8f6ec66a393bf3520",
      "timestamp": "2024-02-02T14:21:35",
      "totals": {
        "files": 3,
        "lines": 36,
        "hits": 35,
        "misses": 1,
        "partials": 0,
        "coverage": "97.22222",
        "branches": 0,
        "methods": 0,
        "messages": 0,
        "sessions": 2,
        "complexity": 0,
        "complexity_total": 0,
        "diff": [0, 0, 0, 0, 0, null, 0, 0, 0, 0, null, null, 0]
      },
      "commitid": "a7794fc92007d3a1b99066c8f6ec66a393bf3520",
      "service_url": "https://github.com/slanks/codecov-example/commit/a7794fc92007d3a1b99066c8f6ec66a393bf3520",
      "branch": "slanks-patch-11",
      "message": "Update sonarqube.yml"
    },
    "base": {
      "author": {
        "username": "slanks",
        "service_id": "15999660",
        "email": "slanks@email.com",
        "service": "github",
        "name": "PagesCoffy"
      },
      "url": "https://app.codecov.io/gh/slanks/codecov-example/commit/ce38c96963e6c7100f668503da2ce4e7500de739",
      "timestamp": "2024-02-02T14:17:51",
      "totals": {
        "files": 3,
        "lines": 36,
        "hits": 35,
        "misses": 1,
        "partials": 0,
        "coverage": "97.22222",
        "branches": 0,
        "methods": 0,
        "messages": 0,
        "sessions": 2,
        "complexity": 0,
        "complexity_total": 0,
        "diff": [0, 0, 0, 0, 0, null, 0, 0, 0, 0, null, null, 0]
      },
      "commitid": "ce38c96963e6c7100f668503da2ce4e7500de739",
      "service_url": "https://github.com/slanks/codecov-example/commit/ce38c96963e6c7100f668503da2ce4e7500de739",
      "branch": "slanks-patch-10",
      "message": "Update sonarqube.yml"
    },
    "compare": {
      "url": "https://app.codecov.io/gh/slanks/codecov-example/pull/11",
      "message": "no change",
      "coverage": "0.00",
      "notation": ""
    },
    "owner": {
      "username": "slanks",
      "service_id": "15999660",
      "service": "github"
    },
    "pull": {
      "head": {
        "commit": "a7794fc92007d3a1b99066c8f6ec66a393bf3520",
        "branch": "master"
      },
      "number": "11",
      "base": {
        "commit": "ce38c96963e6c7100f668503da2ce4e7500de739",
        "branch": "master"
      },
      "open": true,
      "id": 11,
      "merged": false
    }
  }
}
```

### Mapping Result[â](#mapping-result "Direct link to Mapping Result")

The combination of the sample payload and the Ocean configuration generates the following Port entity:

**Coverage entity in Port (Click to expand)**

```
{
  "identifier": "codecov-example",
  "title": "codecov-example",
  "blueprint": "codecov_coverage",
  "properties": {
    "repository": "https://app.codecov.io/gh/slanks/codecov-example",
    "coverage": "97.22222",
    "service": "github",
    "author": "PagesCoffy",
    "createdAt": "2024-02-02T14:21:35Z",
    "files": 3,
    "lines": 36,
    "branch": "slanks-patch-11",
    "report": {
      "files": 3,
      "lines": 36,
      "hits": 35,
      "misses": 1,
      "partials": 0,
      "coverage": "97.22222",
      "branches": 0,
      "methods": 0,
      "messages": 0,
      "sessions": 2,
      "complexity": 0,
      "complexity_total": 0,
      "diff": [0, 0, 0, 0, 0, null, 0, 0, 0, 0, null, null, 0]
    }
  },
  "relations": {},
  "filter": true
}
```

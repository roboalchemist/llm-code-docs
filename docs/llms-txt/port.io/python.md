# Source: https://docs.port.io/build-your-software-catalog/custom-integration/webhook/examples/packages/python.md

# Python

In this example you are going to create a `package` blueprint that ingests all third party dependencies and libraries in your `requirements.txt` file using a combination of Port's [API](/build-your-software-catalog/custom-integration/api/.md) and [webhook functionality](/build-your-software-catalog/custom-integration/webhook/.md). You will then relate this blueprint to a `service` blueprint, allowing you to map all the packages used by a service.

To ingest the packages to Port, a script that sends information about packages according to the webhook configuration is used.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

Create the following blueprint definition and webhook configuration:

Service blueprint

Create in Port

```
{
  "identifier": "service",
  "title": "Service",
  "icon": "Service",
  "schema": {
    "properties": {
      "description": {
        "title": "Description",
        "type": "string"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "relations": {}
}
```

Package blueprint

Create in Port

```
{
  "identifier": "packages",
  "description": "This blueprint represents a software package file in our catalog",
  "title": "Package",
  "icon": "Package",
  "schema": {
    "properties": {
      "version": {
        "type": "string",
        "title": "Depedency Version"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "relations": {
    "service": {
      "title": "Service",
      "target": "service",
      "required": false,
      "many": true
    }
  }
}
```

Package webhook configuration

```
{
  "identifier": "packagesMapper",
  "title": "Package Mapper",
  "description": "A webhook configuration to map packages and dependencies from a file",
  "icon": "Package",
  "mappings": [
    {
      "blueprint": "packages",
      "itemsToParse": ".body.dependencies",
      "entity": {
        "identifier": ".item.id",
        "title": ".item.name",
        "properties": {
          "version": ".item.version"
        },
        "relations": {
          "service": ".body.service"
        }
      }
    }
  ],
  "enabled": true,
  "security": {}
}
```

## Working with Port's API and Bash script[â](#working-with-ports-api-and-bash-script "Direct link to Working with Port's API and Bash script")

Here is an example snippet showing how to integrate Port's API and Webhook with your existing pipelines using Python and Bash:

* Python
* Bash

Create the following Python script in your repository to create or update Port entities as part of your pipeline:

Python script example

```
import requests
import json

# Get environment variables using the config object or os.environ["KEY"]
WEBHOOK_URL = os.environ['WEBHOOK_URL'] ## the value of the URL you receive after creating the Port webhook
SERVICE_ID = os.environ['SERVICE_ID'] ## The identifier of your service in Port
PATH_TO_REQUIREMENTS_TXT_FILE = os.environ['PATH_TO_REQUIREMENTS_TXT_FILE']


def add_entity_to_port(entity_object):
    """A function to create the passed entity in Port using the webhook URL

    Params
    --------------
    entity_object: dict
        The entity to add in your Port catalog

    Returns
    --------------
    response: dict
        The response object after calling the webhook
    """
    headers = {"Content-Type": "application/json"}
    response = requests.post(WEBHOOK_URL, json=entity_object, headers=headers)
    return response.json()

def convert_requirements_txt(requirements_txt_path):
    """This function takes a requirements.txt file path, converts all the dependencies into a
    JSON array using three keys (name, version, and id). It then sends this data to Port

    Params
    --------------
    requirements_txt_path: str
        The path to the requirements.txt file relative to the project's root folder

    Returns
    --------------
    response: dict
        The response object after calling the webhook"""
    with open(requirements_txt_path, 'r') as file:
        requirements = file.readlines()

    dependencies = []
    for index, requirement in enumerate(requirements, start=1):
        requirement = requirement.strip()
        if requirement:
            name, version = requirement.split("==")
            pkg_id = f"pkg-{index}"
            dependencies.append({
                'name': name,
                'version': version,
                'id': pkg_id
            })

    converted_data = {
        "service": SERVICE_ID,
        'dependencies': dependencies
    }

    return converted_data

entity_object = convert_requirements_txt(PATH_TO_REQUIREMENTS_TXT_FILE)
webhook_response = add_entity_to_port(entity_object)
print(webhook_response)
```

Create the following Bash script in your repository to create or update Port entities as part of your pipeline:

Bash script example

```
#!/bin/sh

# Get environment variables
WEBHOOK_URL="$WEBHOOK_URL"
SERVICE_ID="$SERVICE_ID"
PATH_TO_REQUIREMENTS_TXT_FILE="$PATH_TO_REQUIREMENTS_TXT_FILE"

add_entity_to_port() {
    local entity_object="$1"
    local headers="Accept: application/json"
    local response=$(curl -X POST -H "$headers" -H "Content-Type: application/json" -d "$entity_object" "$WEBHOOK_URL")
    echo "$response"
}

# This function takes a requirements.txt file path, converts all the dependencies into a
# JSON array using three keys (name, version, and id). It then sends this data to Port

#!/bin/sh

convert_requirements_txt() {
    requirements_txt_path="$1"

    # Initialize variables
    index=1
    dependencies=""

    # Read the requirements.txt file line by line
    while IFS= read -r line || [ -n "$line" ]; do
        # Trim leading and trailing whitespace
        line=$(echo "$line" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')

        # Skip empty lines or lines starting with #
        if [ -z "$line" ] || [ "$(printf %.1s "$line")" = "#" ]; then
            continue
        fi

        # Extract the name and version using awk
        name=$(echo "$line" | awk -F'==' '{print $1}')
        version=$(echo "$line" | awk -F'==' '{print $2}')

        # Generate the ID with the format "pkg-<ID>"
        pkg_id="pkg-$index"

        # Add the dependency to the JSON array
        dependencies="$dependencies{\"name\":\"$name\",\"version\":\"$version\",\"id\":\"$pkg_id\"},"

        # Increment the index
        index=$((index + 1))
    done < "$requirements_txt_path"

    # Remove the trailing comma from the dependencies string
    dependencies=$(echo "$dependencies" | sed 's/,$//')

    # Generate the final JSON object and send it to Port
    local entity_object="{\"service\":\"$SERVICE_ID\",\"dependencies\":[${dependencies}]}"

    local webhook_response=$(add_entity_to_port "$entity_object")
    echo "$webhook_response"

}
# Example usage

converted_data=$(convert_requirements_txt "$PATH_TO_REQUIREMENTS_TXT_FILE")
echo "$converted_data"
```

For an example showing how to integrate the above scripts with your existing Gitlab CI pipelines, visit:

* [Requirements.txt example](https://github.com/port-labs/requirements-file-webhook-example)

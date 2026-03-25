# Source: https://docs.port.io/build-your-software-catalog/custom-integration/webhook/examples/packages/go.md

# Golang

In this example you are going to create a `package` blueprint that ingests Go modules, versions and dependencies using a combination of Port's [API](/build-your-software-catalog/custom-integration/api/.md) and [webhook functionality](/build-your-software-catalog/custom-integration/webhook/.md). You will then relate this blueprint to a `service` blueprint, allowing you to map all the packages used by a service.

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
  "identifier": "package",
  "description": "This blueprint represents a Go dependency",
  "title": "Go Package",
  "icon": "Go",
  "schema": {
    "properties": {
      "packageUrl": {
        "icon": "DefaultProperty",
        "title": "Package URL",
        "description": "The URL of the dependency package",
        "type": "string",
        "format": "url"
      },
      "version": {
        "type": "string",
        "title": "Version",
        "description": "The version of the dependency"
      },
      "indirect": {
        "type": "boolean",
        "title": "Indirect Dependency",
        "description": "Whether the dependency is indirect"
      },
      "packageName": {
        "type": "string",
        "title": "Package Name",
        "description": "The name of the dependency package"
      }
    },
    "required": ["packageName", "packageUrl", "version"]
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
  "identifier": "goDependencyMapper",
  "title": "Go Dependency Mapper",
  "description": "A webhook configuration to map packages and dependencies from a file",
  "icon": "Go",
  "mappings": [
    {
      "blueprint": "package",
      "entity": {
        "identifier": ".body.package_name",
        "title": ".body.package_url",
        "properties": {
          "packageName": ".body.package_name",
          "packageUrl": ".body.package_url",
          "version": ".body.version",
          "indirect": ".body.indirect"
        }
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

Create the following Bash script in your repository to create or update Port entities as part of your pipeline:

Go Bash script

```
#!/bin/bash

# Get environment variables
WEBHOOK_URL="$WEBHOOK_URL"
SERVICE_ID="$SERVICE_ID"

set -e
# Create or clear the output file
echo "[]" > output.json

# Extract require lines from go.mod excluding the first and the last lines
mapfile -t requires < <(sed -n '/require (/,/)/p' go.mod | tail -n +2 | head -n -1)

# Parse each require line into a package JSON
for require in "${requires[@]}"; do
    # Ignore if line is 'require (' or ')'
    if [[ "$require" == "require (" ]] || [[ "$require" == ")" ]]; then
        continue
    fi

    # Split line into an array
    IFS=' ' read -r -a parts <<< "$require"

    # Assign array items to variables
    package_url="${parts[0]}"
    version="${parts[1]}"
    indirect=false

    # Check if line is indirect
    if [[ "${parts[2]}" == "//" && "${parts[3]}" == "indirect" ]]; then
        indirect=true
    fi

    # Extract the package name from the URL
    package_name=$(basename "$package_url")

    # Prepend 'https://' to package URL if not already there and remove any white spaces
    package_url=$(echo "$package_url" | tr -d '[:space:]')
    if [[ "$package_url" != http* ]]; then
        package_url="https://$package_url"
    fi

    # Create the package JSON
    package_json=$(jq -n \
        --arg pn "$package_name" \
        --arg id "$package_name" \
        --arg pu "$package_url" \
        --arg v "$version" \
        --argjson i "$indirect" \
        '{
            identifier: $id,
            packageName: $pn,
            packageUrl: $pu,
            version: $v,
            indirect: $i,
            service: $SERVICE_ID
        }')

    # Add the package JSON to the output file
    jq --argjson p "$package_json" '. += [$p]' output.json > temp.json && mv temp.json output.json

    # Send the package JSON to the webhook
    curl --location '$WEBHOOK_URL' \
        --header 'Content-Type: application/json' \
        --data "$package_json"
done
```

note

* The script utilizes the `mapfile` command, which is a built-in command in the Bash shell, to read lines from the `go.mod` file and store them in an array. Please note that this command may not be available in all shells by default. If you are using a different shell such as Dash or Zsh, you may need to switch to Bash or modify the script to achieve a similar functionality.

* The script relies on the `jq` command for manipulating JSON data. It is used to create JSON objects based on the package details extracted from the `go.mod` file and append these objects to an output JSON file. It is important to note that `jq` is a powerful JSON processor for the command-line, but it is not typically included in many systems by default. You may need to install it separately to use it.

Create the following Python script in your repository to create or update Port entities as part of your pipeline:

Go Python script

```
# Dependencies to install:
# pip install requests
# pip install tldextract

import json
import requests
import os
from urllib.parse import urlparse

output_filename = "output.json"
webhook_url = os.environ.get('WEBHOOK_URL')
SERVICE_ID = os.environ.get('SERVICE_ID')

# Prepare the headers for the requests
headers = {'Content-Type': 'application/json'}

# Initialize the output file
with open(output_filename, 'w') as f:
    json.dump([], f)

# Read the go.mod file
with open('go.mod', 'r') as f:
    lines = f.readlines()

# Find all require blocks
require_blocks = []
start = -1
for i, line in enumerate(lines):
    if line.strip() == 'require (':
        start = i
    elif line.strip() == ')' and start != -1:
        require_blocks.append(lines[start + 1:i])
        start = -1

# Process each require block
for requires in require_blocks:
    for require in requires:
        parts = require.split()  # Split the line into parts

        package_url = parts[0]
        version = parts[1]
        indirect = len(parts) > 3 and parts[2] == "//" and parts[3] == "indirect"  # Check if the package is indirect

        # Parse the package name from the URL
        package_name = os.path.basename(urlparse(package_url).path)

        # Ensure package_url is in URL format
        if not package_url.startswith('http://') and not package_url.startswith('https://'):
            package_url = 'https://' + package_url

        # Prepare the package dictionary
        package_dict = {
            "identifier": package_name,
            "package_name": package_name,
            "package_url": package_url,
            "version": version,
            "indirect": indirect,
            "service" SERVICE_ID
        }

        # Append to the output file
        with open(output_filename, 'r+') as f:
            data = json.load(f)
            data.append(package_dict)
            f.seek(0)
            json.dump(data, f, indent=4)

        # Send data to the webhook
        response = requests.post(webhook_url, headers=headers, data=json.dumps(package_dict))
        print(response.status_code)
```

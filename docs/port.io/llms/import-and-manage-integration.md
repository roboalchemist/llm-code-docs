# Source: https://docs.port.io/guides/all/import-and-manage-integration.md

# Manage integration mapping using Terraform

This guide demonstrates how to use the Import State feature of Terraform to manage your Port integration's mapping with Terraform.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* Complete the [onboarding process](/getting-started/overview.md).
* Install the [integration](/build-your-software-catalog/sync-data-to-catalog/.md#available-plug--play-integrations) whose mapping you want to manage.

Installation Id

Take note of the installation ID of your integration when installing it - you'll need this ID to import and manage the integration with Terraform.

## Getting started[â](#getting-started "Direct link to Getting started")

In order to interact with the API you will need an **API token**.

To get an **API token** you need to:

1. Find your Port API credentials.
2. Make an API request to generate a valid token.

### Find your Port API credentials[â](#find-your-port-api-credentials "Direct link to Find your Port API credentials")

Get your Port credentials

To get your Port credentials, go to your [Port application](https://app.getport.io), click on the `...` button in the top right corner, and select `Credentials`. Here you can view and copy your `CLIENT_ID` and `CLIENT_SECRET`:

![](/img/software-catalog/credentials-modal.png)

### Download your integration configuration into a file[â](#download-your-integration-configuration-into-a-file "Direct link to Download your integration configuration into a file")

Here are some code examples showing how to download the integration configuration in various programming languages:

* cURL
* Python
* Javascript

```
#/usr/bin/env bash

# Dependencies to install:
# For apt:
# $ sudo apt-get install jq
# For yum:
# $ sudo yum install jq

INSTALLATION_ID="YOUR_INSTALLATION_ID"
CLIENT_ID="YOUR_CLIENT_ID"
CLIENT_SECRET="YOUR_CLIENT_SECRET"

ACCESS_TOKEN=$(curl -s --location -X POST 'https://api.port.io/v1/auth/access_token' \
--header 'Content-Type: application/json' \
--data-raw """{
    \"clientId\": \"${CLIENT_ID}\",
    \"clientSecret\": \"${CLIENT_SECRET}\"
}""" | jq -r '.accessToken')

curl -s -X GET \
  "https://api.port.io/v1/integration/${INSTALLATION_ID}?byField=installationId" \
  -H 'accept: */*' \
  -H "Authorization: Bearer ${ACCESS_TOKEN}" \
  | jq '.integration.config' > ./${INSTALLATION_ID}.json
```

```
# Dependencies to install:
# $ python -m pip install requests

import json
import requests

CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
INSTALLATION_ID = 'YOUR_INSTALLATION_ID'

API_URL = 'https://api.port.io/v1'

credentials = {'clientId': CLIENT_ID, 'clientSecret': CLIENT_SECRET}

token_response = requests.post(f'{API_URL}/auth/access_token', json=credentials)

access_token = token_response.json()['accessToken']

headers = {
    'Authorization': f'Bearer {access_token}'
}

integration_response = requests.get(
    f'{API_URL}/integration/{INSTALLATION_ID}?byField=installationId',
    headers=headers)

with open(f'{INSTALLATION_ID}.json', 'w') as file:
    file.write(json.dumps(integration_response.json()['integration']['config']))
```

```
// Dependencies to install:
// $ npm install axios --save


const fs = require('node:fs/promises');
const axios = require("axios").default;

const CLIENT_ID = "YOUR_CLIENT_ID";
const CLIENT_SECRET = "YOUR_CLIENT_SECRET";
const INSTALLATION_ID = "YOUR_INSTALLATION_ID";

const API_URL = "https://api.port.io/v1";

(async () => {
  const response = await axios.post(`${API_URL}/auth/access_token`, {
    clientId: CLIENT_ID,
    clientSecret: CLIENT_SECRET,
  });

  const accessToken = response.data.accessToken;
  const config = {
      headers: {
          Authorization: `Bearer ${accessToken}`,
      }
  };

  const integrationResponse = await axios.get(
      `${API_URL}/integration/${INSTALLATION_ID}?byField=installationId`, 
      config)

  await fs.writeFile(
    `./${INSTALLATION_ID}.json`, 
    JSON.stringify(integrationResponse.data.integration.config)
  )
})();
```

Selecting a Port API URL by account region

The `port_region`, `port.baseUrl`, `portBaseUrl`, `port_base_url` and `OCEAN__PORT__BASE_URL` parameters select which Port API instance to use:

* **EU** ([app.port.io](https://app.port.io)) â `https://api.port.io`
* **US** ([app.us.port.io](https://app.us.port.io)) â `https://api.us.port.io`

Here is the complete `main.tf` file:

`main.tf` dependency

Notice that the `main.tf` file references the downloaded file generated in the previous command

See the `file("${path.module}/...")` function

Complete Terraform definition file

```
terraform {
  required_providers {
    port = {
      source  = "port-labs/port-labs"
      version = "~> 2.0.3"
    }
  }

  provider "port" {
  client_id = "YOUR_CLIENT_ID"     # or set the environment variable PORT_CLIENT_ID
  secret    = "YOUR_CLIENT_SECRET" # or set the environment variable PORT_CLIENT_SECRET
  base_url  = "https://api.port.io"
}

resource "port_integration" "tf_{my-installation-id}" {
  installation_id       = "{my-installation-id}"
  installation_app_type = "{my-installation-type}"
  title                 = "{my-installation-title}"
  version               = ""
  # The reason for the jsonencode|jsondecode is
  # to preserve the exact syntax as terraform expects,
  # this resolves conflicts in the state caused by indents
  config                = jsonencode(jsondecode(file("${path.module}/{my-installation-id}.json")))
}
```

Selecting a Port API URL by account region

The `port_region`, `port.baseUrl`, `portBaseUrl`, `port_base_url` and `OCEAN__PORT__BASE_URL` parameters select which Port API instance to use:

* **EU** ([app.port.io](https://app.port.io)) â `https://api.port.io`
* **US** ([app.us.port.io](https://app.us.port.io)) â `https://api.us.port.io`

Let's break down the definition file and understand the different parts:

## Module imports[â](#module-imports "Direct link to Module imports")

This part includes importing and setting up the required Terraform providers and modules:

```
terraform {
  required_providers {
    port = {
      source  = "port-labs/port-labs"
      version = "~> 2.0.3"
    }
  }
}

provider "port" {
  client_id = "YOUR_CLIENT_ID"     # or set the environment variable PORT_CLIENT_ID
  secret    = "YOUR_CLIENT_SECRET" # or set the environment variable PORT_CLIENT_SECRET
  base_url  = "https://api.port.io"
}
```

Selecting a Port API URL by account region

The `port_region`, `port.baseUrl`, `portBaseUrl`, `port_base_url` and `OCEAN__PORT__BASE_URL` parameters select which Port API instance to use:

* **EU** ([app.port.io](https://app.port.io)) â `https://api.port.io`
* **US** ([app.us.port.io](https://app.us.port.io)) â `https://api.us.port.io`

## Port Terraform Provider Integration Resource[â](#port-terraform-provider-integration-resource "Direct link to Port Terraform Provider Integration Resource")

This part includes declaring the Port integration and pointing the downloaded json file as the source of the integration configuration

```
resource "port_integration" "tf_{my-installation-id}" {
  installation_id       = "{my-installation-id}"
  installation_app_type = "{my-installation-type}"
  title                 = "{my-installation-title}"
  version               = ""
  # The reason for the jsonencode|jsondecode is
  # to preserve the exact syntax as terraform expects,
  # this resolves conflicts in the state caused by indents
  config                = jsonencode(jsondecode(file("${path.module}/{my-installation-id}.json")))
}
```

Terraform JSON formatting

Since Terraform is very explicit when writing and reading the state, we use `jsonencode` and `jsondecode` on the raw JSON file to make sure we do not have a conflict simply by having a bit different formatting than the Terraform JSON formatting.

To use this example yourself, simply replace the placeholders for `installation_id`, `client_id` and `secret` and then run the following commands to setup terraform, import the state and verifying that everything was imported:

```
# install modules and create an initial state
terraform init
# import state from the Port API
terraform import port_integration.tf_{my-installation-id} {my-installation-id}
# To view Terraform's planned changes based on your .tf definition file:
terraform plan
```

## Result[â](#result "Direct link to Result")

After running `terraform plan` you should see that there are not changes from the imported state.

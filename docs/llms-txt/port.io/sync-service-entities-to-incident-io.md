# Source: https://docs.port.io/guides/all/sync-service-entities-to-incident-io.md

# Sync Port Services to incident.io

This guide demonstrates how to sync service entities from Port into incident.io's catalog, ensuring better visibility and context for your services during incident management.

You can use either of these methods:

* **catalog-importer** (recommended): incident.io's official CLI tool, designed to run as part of CI/CD or on a cronjob. It syncs structured data from Port (and other sources) into the incident.io catalog.
* **Custom GitHub workflow**: A GitHub Actions workflow that fetches entities from Port and pushes them to incident.io via their API.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* Complete the [onboarding process](/getting-started/overview.md).
* An [incident.io](https://app.incident.io/) account with **admin access** to create API keys.
* A `Service` blueprint in Port to represent the service entities you want to sync to incident.io. You should already have one installed during the [onboarding process](/getting-started/overview.md).
* For the custom GitHub workflow: A GitHub repository and [Port's GitHub app](https://github.com/apps/getport-io) installed.

Admin access required

You need admin access to your incident.io organization to create API keys. If you don't have admin access, contact your incident.io administrator to create the API key for you.

## Setup[â](#setup "Direct link to Setup")

* Catalog Importer
* Custom GitHub workflow

The [catalog-importer](https://github.com/incident-io/catalog-importer) is incident.io's official tool for syncing catalog data. It is designed to run as part of CI/CD or on a cronjob and supports multiple data sources, including Port.

### Install catalog-importer

**macOS (Homebrew):**

```
brew tap incident-io/homebrew-taps
brew install catalog-importer
```

**Other platforms:**

Install from the [releases page](https://github.com/incident-io/catalog-importer/releases) or run:

```
go install -v github.com/incident-io/catalog-importer/v2/cmd/catalog-importer@latest
```

### Set up API keys

Create an [incident.io API key](https://app.incident.io/settings/api-keys) with permissions to view and manage catalog types and entries. Set:

```
export INCIDENT_API_KEY="your-incident-io-api-key"
```

For Port, use your [Port credentials](/build-your-software-catalog/custom-integration/api/.md#get-api-token):

```
export PORT_CLIENT_ID="your-port-client-id"
export PORT_CLIENT_SECRET="your-port-client-secret"
```

Selecting a Port API URL by account region

The `port_region`, `port.baseUrl`, `portBaseUrl`, `port_base_url` and `OCEAN__PORT__BASE_URL` parameters select which Port API instance to use:

* **EU** ([app.port.io](https://app.port.io)) â `https://api.port.io`
* **US** ([app.us.port.io](https://app.us.port.io)) â `https://api.us.port.io`

### Create the fetch script

Create `fetch-from-port.sh` to fetch entities from Port and output JSON for the catalog-importer:

```
#!/bin/bash
set -e

PORT_BASE_URL="${PORT_BASE_URL:-https://api.port.io}"
BLUEPRINT_ID="${BLUEPRINT_ID:-service}"

TOKEN=$(curl -s -X POST "${PORT_BASE_URL}/v1/auth/access_token" \
  -H "Content-Type: application/json" \
  -d "{\"clientId\": \"$PORT_CLIENT_ID\", \"clientSecret\": \"$PORT_CLIENT_SECRET\"}" \
  | jq -r '.accessToken')

curl -s -X GET "${PORT_BASE_URL}/v1/blueprints/${BLUEPRINT_ID}/entities" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  | jq '[.entities[] | {
      external_id: .identifier,
      name: .title,
      url: .properties.url // "",
      readme: .properties.readme // "",
      language: .properties.language // "",
      lifecycle: .properties.lifecycle // "",
      type: .properties.type // ""
    }]'
```

### Create the importer config

Create `importer.jsonnet`. The catalog-importer creates the catalog type automatically on first sync.

Blueprint schema matching

Ensure the attribute IDs in the config (`url`, `readme`, etc.) match the property names in your Port Service blueprint.

```
{
  sync_id: 'port-services',

  pipelines: [
    {
      sources: [
        {
          exec: {
            command: ['bash', 'fetch-from-port.sh'],
          },
        },
      ],
      outputs: [
        {
          name: 'Port Services',
          description: 'Services entities synced from Port',
          type_name: 'Custom["PortServices"]',
          categories: ['service'],
          source: {
            external_id: '$.external_id',
            name: '$.name',
          },
          attributes: [
            { id: 'url', name: 'URL', type: 'String', source: '$.url' },
            { id: 'readme', name: 'Readme', type: 'Text', source: '$.readme' },
            { id: 'language', name: 'Language', type: 'String', source: '$.language' },
            { id: 'lifecycle', name: 'Lifecycle', type: 'String', source: '$.lifecycle' },
            { id: 'type', name: 'Type', type: 'String', source: '$.type' },
          ],
        },
      ],
    },
  ],
}
```

For full configuration options, see the [catalog-importer config reference](https://github.com/incident-io/catalog-importer/blob/master/config/reference.jsonnet).

### Validate and sync

```
catalog-importer validate --config=importer.jsonnet
catalog-importer sync --config=importer.jsonnet --dry-run
catalog-importer sync --config=importer.jsonnet
```

### Run in CI/CD

You can run the catalog-importer in GitHub Actions using the [Docker image](https://hub.docker.com/r/incidentio/catalog-importer/tags):

```
name: Sync Port to incident.io

on:
  schedule:
    - cron: "0 */2 * * *"
  workflow_dispatch:

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Sync catalog
        run: |
          docker run --rm \
            -v ${{ github.workspace }}/incident-io:/config \
            -w /config \
            -e INCIDENT_API_KEY=${{ secrets.INCIDENT_API_KEY }} \
            -e PORT_CLIENT_ID=${{ secrets.PORT_CLIENT_ID }} \
            -e PORT_CLIENT_SECRET=${{ secrets.PORT_CLIENT_SECRET }} \
            incidentio/catalog-importer:latest \
            sync --config importer.jsonnet
```

Store your config and `fetch-from-port.sh` in an `incident-io` directory in your repo. For Port's EU region, add `-e PORT_BASE_URL=https://api.eu.getport.io` to the `docker run` command.

For more details, see the [catalog-importer documentation](https://github.com/incident-io/catalog-importer/tree/master/docs).

This method uses a GitHub Actions workflow that fetches entities from Port and pushes them to incident.io via their API.

### Set up required secrets and permissions

In your GitHub repository, [add these secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository):

* `PORT_CLIENT_ID` - Port client ID [learn more](/build-your-software-catalog/custom-integration/api/.md#get-api-token).
* `PORT_CLIENT_SECRET` - Port client secret [learn more](/build-your-software-catalog/custom-integration/api/.md#get-api-token).
* `INCIDENT_IO_API_KEY` - [API key](https://app.incident.io/settings/api-keys) with permissions to manage catalog types and view catalog entries.
* `INCIDENT_IO_CATALOG_TYPE_ID` - Incident.io catalog type ID from [Create a catalog type in incident.io](#create-a-catalog-type-in-incident-io).

### Create a catalog type in incident.io

To sync your Port services into incident.io, you first need to create a catalog type in incident.io. Follow the steps below:

1. Log in to your [incident.io](https://app.incident.io/) account.

2. Click **Catalog** on the left navigation bar.

3. Click **add a custom type**.

4. Fill in the following details:

   * **Name**: a suitable name such as `Port Services`

   * **Description**: Provide a description for the catalog type

   * Under **Categories**, select `Services` from the list

   * Under **Attributes**, add the following columns to reflect the properties of your Port `Service` blueprint:

     <!-- -->

     * `url`: Select `string` as the data type
     * `readme`: Select `rich text` as the data type
     * `language`: Select `string` as the data type
     * `lifecycle`: Select `string` as the data type
     * `type`: Select `string` as the data type

5. **Save the changes** by clicking the **Save** button.

6. Once successful, click on the newly created type and take note of the ID from the browser's URL. For example, the ID might be something like `01J5RB95K5NNDE1CRQ7ZQ24YH5` for this browser URL (<https://app.incident.io/organization/catalog/01J5RB95K5NNDE1CRQ7ZQ24YH5>).

7. Create a GitHub secret (`INCIDENT_IO_CATALOG_TYPE_ID`) in the repository with the value of this ID.

### Create GitHub workflow

* Create a GitHub repository (or use an existing one).
* Create a `.github` directory and `workflows` subdirectory.

Inside the `.github/workflows` directory create a file called `sync-port-services-to-incident-io.yml` with the following content:

**GitHub workflow configuration (click to expand)**

Blueprint Schema Matching

Make sure the property names in your Port Service blueprint match the attribute names in your incident.io catalog type. The workflow maps these properties:

* `url` â `url` attribute
* `readme` â `readme` attribute
* `language` â `language` attribute
* `lifecycle` â `lifecycle` attribute
* `type` â `type` attribute

If you have different property names, update the mapping in step 4 of the workflow.

```
name: Sync Data to incident.io
on:
  schedule:
    - cron: "0 */2 * * *" # every two hours. Adjust this value
  workflow_dispatch: # allows manual triggering

jobs:
  sync-data:
    runs-on: ubuntu-latest
    steps:
      - name: Check out the repository
        uses: actions/checkout@v4
        
      - name: Get Port Access Token
        id: get_token
        run: |
          access_token=$(curl --location --request POST 'https://api.port.io/v1/auth/access_token' \
          --header 'Content-Type: application/json' \
          --data-raw '{
              "clientId": "${{ secrets.PORT_CLIENT_ID }}",
              "clientSecret": "${{ secrets.PORT_CLIENT_SECRET }}"
          }' | jq '.accessToken' | sed 's/"//g')
          echo "access_token=$access_token" >> $GITHUB_ENV

      - name: Get Service Entities from Port
        id: get_entities
        run: |
          response=$(curl -X GET "https://api.port.io/v1/blueprints/service/entities" \
              -H "Authorization: Bearer ${{ env.access_token }}" \
              -H "Content-Type: application/json")
          
          # Check if response is empty or if an error occurred
          if [ -z "$response" ]; then
            echo "No response received from Port API."
            exit 1
          else
            echo "Port Service Entities Response:"
            echo "$response"
          fi
          
          # Save response to file and environment variable
          echo "$response" > response.json

      - name: Get incident.io Schema
        id: get_schema
        run: |
          schema_response=$(curl --location --request GET 'https://api.incident.io/v2/catalog_types/${{ secrets.INCIDENT_IO_CATALOG_TYPE_ID }}' \
          -H "Authorization: Bearer ${{ secrets.INCIDENT_IO_API_KEY }}" \
          -H "Content-Type: application/json")
          echo "$schema_response" > schema.json
          
      - name: Map and Send Data to incident.io
        run: |
          schema=$(jq '.catalog_type.schema.attributes' schema.json)

          # Extract IDs of incident.io catalog attributes
          # IMPORTANT: Make sure these attribute names match your incident.io catalog type
          url_id=$(echo "$schema" | jq -r '.[] | select(.name == "url") | .id')
          readme_id=$(echo "$schema" | jq -r '.[] | select(.name == "readme") | .id')
          language_id=$(echo "$schema" | jq -r '.[] | select(.name == "language") | .id')
          lifecycle_id=$(echo "$schema" | jq -r '.[] | select(.name == "lifecycle") | .id')
          type_id=$(echo "$schema" | jq -r '.[] | select(.name == "type") | .id')

          # Read entities as a JSON array, and use `jq` to iterate correctly
          entities=$(jq -c '.entities[]' response.json)

          echo "$entities" | while IFS= read -r entity; do

            name=$(echo "$entity" | jq -r '.title // empty')
            if [ -z "$name" ]; then
              echo "Error: 'name' field is required but is empty. Skipping this entity."
              continue
            fi

            data=$(jq -n \
              --arg url_id "$url_id" \
              --arg url "$(echo "$entity" | jq -r '.properties.url // empty')" \
              --arg readme_id "$readme_id" \
              --arg readme "$(echo "$entity" | jq -r '.properties.readme // empty')" \
              --arg language_id "$language_id" \
              --arg language "$(echo "$entity" | jq -r '.properties.language // empty')" \
              --arg lifecycle_id "$lifecycle_id" \
              --arg lifecycle "$(echo "$entity" | jq -r '.properties.lifecycle // empty')" \
              --arg type_id "$type_id" \
              --arg type "$(echo "$entity" | jq -r '.properties.type // empty')" \
              --arg external_id "$(echo "$entity" | jq -r '.identifier')" \
              --arg name "$name" \
              --arg catalog_type_id "${{ secrets.INCIDENT_IO_CATALOG_TYPE_ID }}" \
              '{
                "aliases": [],
                "attribute_values": {
                  ($url_id): {"value": {"literal": $url}},
                  ($readme_id): {"value": {"literal": $readme}},
                  ($language_id): {"value": {"literal": $language}},
                  ($lifecycle_id): {"value": {"literal": $lifecycle}},
                  ($type_id): {"value": {"literal": $type}}
                },
                "catalog_type_id": $catalog_type_id,
                "external_id": $external_id,
                "name": $name
              }')

            echo "Sending data to API for entity $name"

            response=$(curl -i -X POST "https://api.incident.io/v2/catalog_entries" \
              -H "Authorization: Bearer ${{ secrets.INCIDENT_IO_API_KEY }}" \
              -H "Content-Type: application/json" \
              -d "$data")

            echo "Incident.io API response for entity $name:"
            echo "$response"
            
            # Check if the response indicates success
            if echo "$response" | grep -q "201\|200"; then
              echo "â Successfully synced entity $name to incident.io"
            else
              echo "â Failed to sync entity $name to incident.io"
              echo "Response: $response"
            fi
          done
```

Selecting a Port API URL by account region

The `port_region`, `port.baseUrl`, `portBaseUrl`, `port_base_url` and `OCEAN__PORT__BASE_URL` parameters select which Port API instance to use:

* **EU** ([app.port.io](https://app.port.io)) â `https://api.port.io`
* **US** ([app.us.port.io](https://app.us.port.io)) â `https://api.us.port.io`

### Let's test it!

1. **Manual Testing**: Go to your GitHub repository's **Actions** tab and manually trigger the `Sync Data to incident.io` workflow to test it immediately.

2. **Check the logs**: Review the workflow logs to ensure all entities are being synced successfully.

3. **Verify in incident.io**:

   * Log in to your incident.io account.

   * Navigate to the **Catalog** section in the left navigation bar.

   * Search for the `Port Services` catalog type or any custom name you provided.

   * You should now see the synced service entities from Port listed under this catalog type.

     ![](/img/guides/IncidentioServiceCatalog.png)

Once the GitHub workflow runs (either manually or on schedule), the service entities from Port will be automatically synced into your incident.io catalog, giving you improved visibility and context for managing incidents.

## Limitations[â](#limitations "Direct link to Limitations")

Note that incident.io can currently ingest up to **50,000 catalog items**. Keep this limit in mind when scaling your service catalog.

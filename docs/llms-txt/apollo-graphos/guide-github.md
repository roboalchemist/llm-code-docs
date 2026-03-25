# Source: https://www.apollographql.com/docs/graphos/platform/schema-management/delivery/publishing/guide-github.md

# Schema publishing with GitHub Actions

This guide walks you through how to set up schema publishing in your CI/CD pipeline using [GitHub Actions](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflows).

## Pre-requisites

* A graph set up in GraphOS with its graph reference value (`APOLLO_GRAPH_REF`)
* Your GraphOS organization ID
* A GitHub repository for a subgraph you want to publish
* [Rover CLI](https://www.apollographql.com/docs/rover/getting-started/) installed

## 1. Set up a GitHub Actions workflow

Create a workflow file called `publish-subgraph.yml` in the `.github/workflows` directory of your repository.

```yaml title=publish-subgraph.yml
name: Publish Subgraph Schema

on:
  push:
    branches: [main]

jobs:
  publish-subgraph:
    runs-on: ubuntu-latest
    env:
      APOLLO_KEY: ${{ secrets.MY_APOLLO_SUBGRAPH_KEY }}
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Publish subgraph schema
        run: |
          npx rover subgraph publish <APOLLO_GRAPH_REF> \
            --name <SUBGRAPH_NAME> \
            --schema <PATH/TO/SUBGRAPH/SCHEMA.GRAPHQL> \
            --routing-url <SUBGRAPH_ROUTING_URL>
```

Replace the values in `<>` with your own values.

You'll set up the `MY_APOLLO_SUBGRAPH_KEY` secret later.

## 2. Obtain a subgraph API key

Use subgraph API keys to publish updates to subgraph schemas within CI/CD pipelines.

To create a subgraph API key, first you'll need to create a subgraph configuration file with the details of the subgraph you want to publish.

```yaml title=subgraph-config.yaml
subgraphs:
  - name: <YOUR_SUBGRAPH_NAME>
    routingUrl: <YOUR_SUBGRAPH_ROUTING_URL>
```

Then, run the following Rover command, replacing `<YOUR_ORGANIZATION_ID>` with your own value and `<YOUR_KEY_NAME>` with your desired key name.

```shell
rover api-key create <YOUR_ORGANIZATION_ID> subgraph <YOUR_KEY_NAME> --subgraph-config subgraph-config.yaml
```

>

You can also use the `createKey` mutation from the [Platform API](https://www.apollographql.com/docs/graphos/platform/platform-api).

Open up the [Explorer for the Platform API](https://studio.apollographql.com/public/apollo-platform/home?variant=main) and paste the following mutation in the **Operations** tab:

```graphql
mutation Mutation($organizationId: ID!, $name: String!, $type: GraphOsKeyType!, $resources: ApiKeyResourceInput) {  
  organization(id: $organizationId) {    
    createKey(name: $name, type: $type, resources: $resources) {      
      keyName      
      id      
      token    
    }
  }
}
```

Include a request payload in the **Variables** panel with the following properties, filling in your own values:

```graphql title=Request payload
{
  "name": <YOUR_SUBGRAPH_API_KEY_NAME>,
  "type": "SUBGRAPH",
  "organizationId": <YOUR_ORGANIZATION_ID>,
  "resources": {
    "subgraphs": [
      {
        "graphId": <YOUR_GRAPH_ID>,
        "subgraphName": <YOUR_SUBGRAPH_ID>,
        "variantName": <YOUR_VARIANT_NAME>
      }
    ]
  }
}
```

Run the request. You'll receive a response payload that looks something like this:

```graphql title=Response payload
{
  "data": {
    "organization": {
      "createKey": {
        "keyName": "YOUR_SUBGRAPH_API_KEY_NAME",
        "id": "6ca72032-535a-4bba-b816-fa8d88823863",
        "token": "ak_v2_RkZFMjE4ODYtMzk5Qy00QkMzLUExRDYtMDRBMjE5NTdFNTdF_MUU3M0MxQ0MtMjY5OS00QjhBLTk4MjYtQzVFMUJFRjFBQUZB"
     }
    }
  }
}
```

Copy the `token` value.

## 3. Store your subgraph API key

1. In GitHub, go to your repository's **Settings → Secrets and variables → Actions**.
2. Click **New repository secret**.
3. Give it a name that matches your workflow's environment variable. In this example, you named it `MY_APOLLO_SUBGRAPH_KEY`.
4. Paste the `token` value into the secret value field.
5. Click **Add secret**.
6. Verify that your new secret appears in the **Repository Secrets** list.

## 4. Run your workflow

Make a change in your subgraph schema and push it to your repository's `main` branch. This triggers the **Publish Subgraph Schema**  workflow.

Watch the workflow run in the **Actions** tab and publish the subgraph schema to your graph in GraphOS.

## Conclusion

You've now set up schema publishing in your CI/CD pipeline using GitHub Actions. The process for other CI/CD systems is similar: create a workflow file, obtain a subgraph API key, store the key in your secret manager, and run the workflow.

# Source: https://docs.port.io/build-your-software-catalog/custom-integration/api/ci-cd/jenkins-deployment.md

# Jenkins Deployment

Available Ocean integration

Port provides an [Ocean integration](/build-your-software-catalog/sync-data-to-catalog/cicd/jenkins/.md) for Jenkins, which allows you to automatically sync your Jenkins resources with Port and provides more configuration options. This is the **recommended** way to integrate Port with Jenkins.<br /><!-- -->If you would still prefer to use Port's API, follow this page.

Using Jenkins build, you can easily create/update and query entities in Port.

<br />

<br />

![Github Illustration](/assets/images/jenkins-pipeline-illustration-3a299aa823a294cbe653f3a0091b8738.png)

## ð¡ Common Jenkins build usage[â](#-common-jenkins-build-usage "Direct link to ð¡ Common Jenkins build usage")

Port's API allows for easy integration between Port and your Jenkins builds, for example:

* Report the status of a running **CI job**;
* Update the software catalog about a new **build version** for a **microservice**;
* Get existing **entities**.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. This example makes use of the following Jenkins plugins:

* [Plain Credentials](https://plugins.jenkins.io/credentials-binding/) (>=143.v1b\_df8b\_d3b\_e48)
* [HTTP Request](https://plugins.jenkins.io/http_request/) (>=1.16)

2. The following methods are used in the example, and these signatures need to be approved:

```
new groovy.json.JsonSlurperClassic
method groovy.json.JsonSlurperClassic parseText java.lang.String
```

3. Add your `PORT_CLIENT_ID` and `PORT_CLIENT_SECRET` as [Jenkins Credentials](https://www.jenkins.io/doc/book/using/using-credentials/) to use them in your CI pipelines.

4. Make sure you have an existing [Blueprint](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/.md) in your Port installation to create/update entities.

## Set up[â](#set-up "Direct link to Set up")

tip

All Port API routes used in this guide can be found in Port's [API documentation](/api-reference/port-api.md).

To interact with Port inside your Jenkins builds, follow these steps:

### Fetching your API token[â](#fetching-your-api-token "Direct link to Fetching your API token")

The following snippet shows you how to pass your `PORT_CLIENT_ID` and `PORT_CLIENT_SECRET` credentials to your build using `withCredentials`, which utilizes the Plain Credentials plugin to bind credentials to variables.

The snippet provided also includes saving Port's API URL as an environment variable for use in future stages and makes a request to Port's API using the credentials to get an access token:

Get API token

```
pipeline {
  agent any
  environment {
    API_URL = "https://api.port.io"
  }
...
    withCredentials([
        string(credentialsId: 'port-client-id', variable: 'PORT_CLIENT_ID'),
        string(credentialsId: 'port-client-secret', variable: 'PORT_CLIENT_SECRET')
        ]){
            // Token request body
            auth_body = """
                {
                    "clientId": "${PORT_CLIENT_ID}",
                    "clientSecret": "${PORT_CLIENT_SECRET}"
                }
                """

            // Make a request to fetch Port API's token
            token_response = httpRequest contentType: 'APPLICATION_JSON',
                httpMode: "POST",
                requestBody: auth_body,
                url: "${API_URL}/v1/auth/access_token"

            // Parse the response to get the accessToken
            def slurped_response = new JsonSlurperClassic().parseText(token_response.content)
            def token = slurped_response.accessToken // Use this token for authentication with Port
            ...
        }
```

### Working with Port's API[â](#working-with-ports-api "Direct link to Working with Port's API")

Add the following code to your Jenkins build, to either create/update an entity, or get an existing one:

* Create/Update
* Get

```
import groovy.json.JsonSlurperClassic
...
    auth_body = """
        {
            "clientId": "${PORT_CLIENT_ID}",
            "clientSecret": "${PORT_CLIENT_SECRET}"
        }
        """
    token_response = httpRequest contentType: 'APPLICATION_JSON',
        httpMode: "POST",
        requestBody: auth_body,
        url: "${API_URL}/v1/auth/access_token"
    def slurped_response = new JsonSlurperClassic().parseText(token_response.content)
    def token = slurped_response.accessToken // Port's access token

    entity_body = """
        {
            "identifier": "example-entity",
            "properties": {
              "myStringProp": "My value",
              "myNumberProp": 1,
              "myBooleanProp": true,
              "myArrayProp": ["myVal1", "myVal2"],
              "myObjectProp": {"myKey": "myVal", "myExtraKey": "myExtraVal"}
            }
        }
    """
    // request url : {API_URL}/blueprints/<blueprint_name>/entities/<entity_name>
    response = httpRequest contentType: "APPLICATION_JSON", httpMode: "POST",
            url: "${API_URL}/v1/blueprints/blueprint/entities?upsert=true&merge=true",
            requestBody: entity_body,
            customHeaders: [
                [name: "Authorization", value: "Bearer ${token}"],
            ]
    println(response.content)
```

```
import groovy.json.JsonSlurperClassic
...
    auth_body = """
        {
            "clientId": "${PORT_CLIENT_ID}",
            "clientSecret": "${PORT_CLIENT_SECRET}"
        }
        """
    token_response = httpRequest contentType: 'APPLICATION_JSON',
        httpMode: "POST",
        requestBody: auth_body,
        url: "${API_URL}/v1/auth/access_token"
    def slurped_response = new JsonSlurperClassic().parseText(token_response.content)
    def token = slurped_response.accessToken // Port's access token

    response = httpRequest contentType: 'APPLICATION_JSON', httpMode: "GET",
            url: "${API_URL}/v1/blueprints/blueprint/entities/entity-example",
            customHeaders: [
                [name: "Authorization", value: "Bearer ${token}"],
            ]
    println(response.content)
```

Selecting a Port API URL by account region

The `port_region`, `port.baseUrl`, `portBaseUrl`, `port_base_url` and `OCEAN__PORT__BASE_URL` parameters select which Port API instance to use:

* **EU** ([app.port.io](https://app.port.io)) â `https://api.port.io`
* **US** ([app.us.port.io](https://app.us.port.io)) â `https://api.us.port.io`

## Examples[â](#examples "Direct link to Examples")

Refer to the [examples](/build-your-software-catalog/custom-integration/api/ci-cd/jenkins-deployment/examples.md) page for practical examples for using Port with Jenkins.

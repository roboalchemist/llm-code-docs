# Source: https://docs.upsun.com/add-services/headless-chrome.md

# Headless Chrome


Headless Chrome is a headless browser that can be configured on projects like any other service on Upsun.

You can interact with the `chrome-headless` service container using Puppeteer, a Node.js library that provides an API to control Chrome over the DevTools Protocol.

Puppeteer can be used to generate PDFs and screenshots of web pages, automate form submission, and test your project's UI. You can find out more information about using Puppeteer on [GitHub](https://github.com/GoogleChrome/puppeteer) or in their [documentation](https://pptr.dev/).

## Supported versions

You can select the major version. But the latest compatible minor version is applied automatically and can’t be overridden.

Patch versions are applied periodically for bug fixes and the like. When you deploy your app, you always get the latest available patches.

   - 120

## Deprecated versions

The following versions are still available in your projects,
but they're at their end of life and are no longer receiving security updates from upstream.

   - 113

   - 95

   - 91

   - 86

   - 84

   - 83

   - 81

   - 80

   - 73

To ensure your project remains stable in the future,
switch to a [supported version](#supported-versions).

## Relationship reference

For each service [defined via a relationship](#usage-example) to your application,
Upsun automatically generates corresponding environment variables within your application container,
in the ``$_`` format.

Here is example information available through the [service environment variables](https://docs.upsun.com/development/variables.md#service-environment-variables) themselves,
or through the [``PLATFORM_RELATIONSHIPS`` environment variable](https://docs.upsun.com/development/variables/use-variables.md#use-provided-variables).

For some advanced use cases, you can use the [PLATFORM_RELATIONSHIPS](https://docs.upsun.com/development/variables/use-variables.md#use-provided-variables).
The structure of the ``PLATFORM_RELATIONSHIPS`` environment variable can be obtained by running ``upsun relationships`` in your terminal:

```json {}
{
  "service": "chrome-headless",
  "ip": "123.456.78.90",
  "hostname": "azertyuiopqsdfghjklm.chrome-headless.service._.eu-1.platformsh.site",
  "cluster": "azertyuiop-main-7rqtwti",
  "host": "chrome-headless.internal",
  "rel": "http",
  "scheme": "http",
  "type": "chrome-headless:120",
  "port": 9222
}
```

Here is an example of how to gather [PLATFORM_RELATIONSHIPS](https://docs.upsun.com/development/variables/use-variables.md#use-provided-variables) information in a [.environment](https://docs.upsun.com/development/variables/set-variables.md#use-env-files):

    .environment

```bash {}
# Decode the built-in credentials object variable.
export RELATIONSHIPS_JSON="$(echo "$PLATFORM_RELATIONSHIPS" | base64 --decode)"

# Set environment variables for individual credentials.
export APP_HEADLESSCHROME_HOST=="$(echo "$RELATIONSHIPS_JSON" | jq -r '.chrome-headless[0].host')"
```

## Requirements

Puppeteer requires at least Node.js version 6.4.0, while using the async and await examples below requires Node 7.6.0 or greater.

If your app container uses a language other than Node.js, upgrade the Node.js version before using Puppeteer.
See how to [manage your Node.js version](https://docs.upsun.com../languages/nodejs/node-version.md).

## Usage example

### 1. Configure the service

To define the service, use the `chrome-headless` type:

```yaml  {location=".upsun/config.yaml"}
services:
  # The name of the service container. Must be unique within a project.
  <SERVICE_NAME>:
    type: chrome-headless:<VERSION>
```

Note that changing the name of the service replaces it with a brand new service and all existing data is lost. Back up your data before changing the service.

### 2. Define the relationship

To define the relationship, use the following configuration:

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  <APP_NAME>:
    # Relationships enable access from this app to a given service.
    # The example below shows simplified configuration leveraging a default service
    # (identified from the relationship name) and a default endpoint.
    # See the Application reference for all options for defining relationships and endpoints.
    relationships:
      <SERVICE_NAME>:
```

You can define ``<SERVICE_NAME>`` as you like, so long as it’s unique between all defined services
and matches in both the application and services configuration.
The example above leverages [default endpoint](https://docs.upsun.com/create-apps/image-properties/relationships.md) configuration for relationships.
That is, it uses default endpoints behind the scenes, providing a [relationship](https://docs.upsun.com/create-apps/image-properties/relationships.md)
(the network address a service is accessible from) that is identical to the name of that service.
Depending on your needs, instead of default endpoint configuration,
you can use [explicit endpoint configuration](https://docs.upsun.com/create-apps/image-properties/relationships.md).
With the above definition, the application container now has [access to the service](#use-in-app) via the relationship ``<SERVICE_NAME>`` and its corresponding [service environment variables](https://docs.upsun.com/development/variables.md#service-environment-variables).

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  <APP_NAME>:
    # Relationships enable access from this app to a given service.
    # The example below shows configuration with an explicitly set service name and endpoint.
    # See the Application reference for all options for defining relationships and endpoints.
    relationships:
      <RELATIONSHIP_NAME>:
        service: <SERVICE_NAME>
        endpoint: http
```

You can define ``<SERVICE_NAME>`` and ``<RELATIONSHIP_NAME>`` as you like, so long as it’s unique between all defined services and relationships
and matches in both the application and services configuration.
The example above leverages [explicit endpoint](https://docs.upsun.com/create-apps/image-properties/relationships.md) configuration for relationships.
Depending on your needs, instead of explicit endpoint configuration,
you can use [default endpoint configuration](https://docs.upsun.com/create-apps/image-properties/relationships.md).
With the above definition, the application container now has [access to the service](#use-in-app) via the relationship ``<RELATIONSHIP_NAME>`` and its corresponding [service environment variables](https://docs.upsun.com/development/variables.md#service-environment-variables).

### Example configuration

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # Relationships enable access from this app to a given service.
    # The example below shows simplified configuration leveraging a default service
    # (identified from the relationship name) and a default endpoint.
    # See the Application reference for all options for defining relationships and endpoints.
    relationships:
      chrome-headless:
services:
  # The name of the service container. Must be unique within a project.
  chrome-headless:
    type: chrome-headless:120
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # Relationships enable access from this app to a given service.
    # The example below shows configuration with an explicitly set service name and endpoint.
    # See the Application reference for all options for defining relationships and endpoints.
    relationships:
      chrome-headless:
        service: chrome-headless
        endpoint: http
services:
  # The name of the service container. Must be unique within a project.
  chrome-headless:
    type: chrome-headless:120
```

### Use in app

After configuration, include [Puppeteer](https://www.npmjs.com/package/puppeteer) as a dependency:

```bash {}
pnpm add puppeteer
```

```bash {}
yarn add puppeteer
```

Configuration for a project looks similar to the following:

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "myapp"
      type: "nodejs:24"

      [...]

      # Relationships enable access from this app to a given service.
      # The example below shows simplified configuration leveraging a default service
      # (identified from the relationship name) and a default endpoint.
      # See the Application reference for all options for defining relationships and endpoints.
      relationships:
        chrome-headless:
services:
  # The name of the service container. Must be unique within a project.
  chrome-headless:
    type: chrome-headless:120
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "myapp"
      type: "nodejs:24"

      [...]

      # Relationships enable access from this app to a given service.
      # The example below shows configuration with an explicitly set service name and endpoint.
      # See the Application reference for all options for defining relationships and endpoints.
      relationships:
        chrome-headless:
          service: chrome-headless
          endpoint: http
services:
  # The name of the service container. Must be unique within a project.
  chrome-headless:
    type: chrome-headless:120
```

This configuration defines a single application (`myapp`), whose source code exists in the `<PROJECT_ROOT>/myapp` directory. 
`myapp` has access to the `chrome-headless` service, via a relationship whose name is [identical to the service name](#2-define-the-relationship)
(as per [default endpoint](https://docs.upsun.com/create-apps/image-properties/relationships.md) configuration for relationships).

From this, `myapp` can retrieve access credentials to the service through the [relationship environment variable](https://docs.upsun.com/add-services/elasticsearch.md#relationship-reference).

```bash  {location="myapp/.environment"}
# Set environment variables for individual credentials,
# For more information, please visit https://docs.upsun.com/development/variables.html#service-environment-variables.
export CHROME_IP="${CHROME_HEADLESS_IP}"
export CHROME_PORT="${CHROME_HEADLESS_PORT}"

# Combine into a single base URL to be used within app.
export CHROME_BASEURL="http://${CHROME_IP}:${CHROME_PORT}"
```

The above file — `.environment` in the `myapp` directory — is automatically sourced by Upsun into the runtime environment, so that the variable `CHROME_BASEURL` can be used within the application to connect to the service.

Note that `CHROME_BASEURL` and all Upsun [service environment variables](https://docs.upsun.com/development/variables.md#service-environment-variables) like `CHROME_HEADLESS_HOST`, are environment-dependent. Unlike the build produced for a given commit, they can't be reused across environments and only allow your app to connect to a single service instance on a single environment.

A file very similar to this is generated automatically for your when using the `upsun ify` command to [migrate a codebase to Upsun](https://docs.upsun.com/get-started.md).

Puppeteer allows your application to [create screenshots](https://pptr.dev/#?product=Puppeteer&version=v13.0.1&show=api-pagescreenshotoptions), [emulate a mobile device](https://pptr.dev/#?product=Puppeteer&version=v13.0.1&show=api-pageemulateoptions), [generate PDFs](https://pptr.dev/#?product=Puppeteer&version=v13.0.1&show=api-pagepdfoptions), and much more.


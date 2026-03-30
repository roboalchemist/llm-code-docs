# Source: https://docs.nimbleway.io/management-tools/nimble-admin-api.md

# Nimble Admin API

### Overview

Having control and visibility over your account, requests and usage is a crucial part of modern IP infrastructure. We’ve created the Nimble Admin API to let you do just that. The API gives you access to advanced pipeline management tools, as well as detailed statistics starting from the account level, all the way down to a single request. A UI dashboard is in development and expected to be available in the coming weeks.

The Admin API is accessible at this address:

***<https://api.nimbleway.com/api/v1/>***

We’ve also added a sandbox environment (based on Swagger), where you can experiment with all Admin API features:

&#x20;[***https://api.nimbleway.com/swagger/index.html***](https://api.nimbleway.com/swagger/index.html#/)

![https://api.nimbleway.com/swagger/index.html](https://www.nimbleway.com/wp-content/uploads/2022/09/Nimble-Admin-API-Swagger.png)

### Statistics

Usage reports are available at the account level and on the pipeline level. This allows you to get a bird’s eye view of your activity, and a deep dive into a single pipeline.

Get a daily activity summary to see the overall trend, or pinpoint a single event with a detailed report of your pipeline’s last requests.

### Managing Pipelines

It’s simple to create and configure multiple pipelines for your account, each with its own settings, to fit different use cases. A pipeline configuration is composed of three main elements:

1. **Authentication** – Each pipeline is created with a unique name, while a password is generated automatically, by the API. In case you wish to use IP authentication, add an IP *allow list* rule to your pipeline.
2. **Targeting and session control** – A pipeline can be set to target a default geolocation. This is particularly useful when using an allow listed IP, as the target location cannot be included in the connection string.
3. **Budget control and access permission** – These options will be added in the future to allow control over a pipeline’s daily spending and permission for accessing its statistics and configuration.

###

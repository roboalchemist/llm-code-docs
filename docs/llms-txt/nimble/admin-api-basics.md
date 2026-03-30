# Source: https://docs.nimbleway.io/management-tools/nimble-admin-api/admin-api-basics.md

# Admin API basics

### Authentication

Nimble’s Admin API uses bearer authentication. A token must be generated before beginning a session and is valid for 72 hours. The first credentials for generating a token will be provided by your account manager.

{% hint style="info" %}
The username and password for accessing the Admin API are different than the credentials used for sending proxy requests, as the Admin API credentials must be well-secured and not passed on public traffic.
{% endhint %}

### Creating a new pipeline

To create a new pipeline, use the *<mark style="color:red;background-color:yellow;">/accounts/projects/</mark>* endpoint. Provide a name for the new pipeline and the API will generate a password automatically. Here is an example pipeline configuration:

![](https://www.nimbleway.com/wp-content/uploads/2022/09/Admin-API-New-Pipeline.png)

### Setting a pipeline’s country and state

In order to use residential proxies from a selected location; country or state (US only), use the *<mark style="color:red;background-color:yellow;">/account/projects/{pipelineName}</mark>* endpoint.

For country codes, we use [ISO 3166 alpha-2 Country Codes](https://www.iban.com/country-codes) (use <mark style="color:red;background-color:yellow;">ALL</mark> to randomly select a country).

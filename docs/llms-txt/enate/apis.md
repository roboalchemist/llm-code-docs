# Source: https://docs.enate.net/enate-help/integrations/enate-integrations/apis.md

# APIs

## Intro to Enate APIs

Enate has an API that allows other systems to start, track and interact with work in Enate. Enate APIs communicate via HTTPS Get/Post calls using the JSON data format.

Enate also supports Webhooks, which you can subscribe to so your system is updated on Enate activity in real-time. Check out the Webhooks section for more information:

{% content-ref url="webhooks" %}
[webhooks](https://docs.enate.net/enate-help/integrations/enate-integrations/webhooks)
{% endcontent-ref %}

## Using Application Credentials to access Enate

Enate allows you to create Application Credentials to support multiple concurrent integrations into Enate via APIs. This approach has replaced the need to use standard Enate user accounts for authorized access to the system, which only supported one concurrent access. The Application Credentials records created in User Management section of Builder can be used to generate 'Bearer Tokens' which can be appended in the header of each API to grant access to Enate. Different permission levels can be granted to each Application Credential by selecting from a number of available 'Roles' when creating the Application Credential.

For more information on this, check out the Application Credentials page in the Builder section:

{% content-ref url="../../builder/builder-2021.1/user-management/application-credentials" %}
[application-credentials](https://docs.enate.net/enate-help/builder/builder-2021.1/user-management/application-credentials)
{% endcontent-ref %}

## Swagger - Enate's Interactive API Documentation

If you've got access to an existing Enate environment, you'll be able to access interactive API documentation for Enate’s APIs using your Swagger link, which will be a unique URL specific to your instance available. See the below examples:

**Operational API: <https://yourplatform/operational/swagger>**

**Configuration API: <https://yourplatform/configuration/swagger>**

More general information on Swagger can be found [here](https://swagger.io/docs/specification/v3_0/about/).

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MXl_fwaVHI33OtXs2yx%2F-MXlcVYbs_aqVocOqjGg%2FUsing-Swagger.gif?alt=media\&token=85fb95d6-f0ed-423e-8c92-a3e406ab6e5a)

## Sample Integration Patterns Using Enate's API's

{% content-ref url="api-sample-webform-front-end-to-post-tickets" %}
[api-sample-webform-front-end-to-post-tickets](https://docs.enate.net/enate-help/integrations/enate-integrations/api-sample-webform-front-end-to-post-tickets)
{% endcontent-ref %}

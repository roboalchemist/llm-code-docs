# Source: https://docs.sonarsource.com/sonarqube-community-build/extension-guide/web-api.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/extension-guide/web-api.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/extension-guide/web-api.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/extension-guide/web-api.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/extension-guide/web-api.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/extension-guide/web-api.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/extension-guide/web-api.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/extension-guide/web-api.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/extension-guide/web-api.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/extension-guide/web-api.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/extension-guide/web-api.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/extension-guide/web-api.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/extension-guide/web-api.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/extension-guide/web-api.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/extension-guide/web-api.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/extension-guide/web-api.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/extension-guide/web-api.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/extension-guide/web-api.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/extension-guide/web-api.md

# Source: https://docs.sonarsource.com/sonarqube-server/extension-guide/web-api.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/web-api.md

# Web API

SonarQube Cloud provides a web API to access its functionalities from applications.

The web services composing the web API are documented within SonarQube Cloud, through the URL <https://sonarcloud.io/web_api>. You can also access the web API documentation from the top bar in Cloud by selecting the help button:

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-5baa9328aac01cb9e14b4c4b07b08d37d6857c61%2F4ab33ab815065784a8ddf26188ff179c272eff89.png?alt=media" alt="You can find the Web API under the help menu in the upper right-hand corner of your SonarQube Cloud UI." width="152"><figcaption></figcaption></figure></div>

### Authenticating to the Web API <a href="#authenticate-to-api" id="authenticate-to-api"></a>

Administrative web services are secured and require the user to have specific permissions.

To authenticate to the Web API, we recommend that you use the [bearer authentication scheme](https://swagger.io/docs/specification/v3_0/authentication/bearer-authentication/). With this scheme, a SonarQube Cloud token is used:

* The token is generated in SonarQube Cloud UI. See [managing-tokens](https://docs.sonarsource.com/sonarqube-cloud/managing-your-account/managing-tokens "mention").
* The token is provided through the `Authorization: Bearer <myToken>` header. See [#sample-api-request](#sample-api-request "mention") below.

### Sending an API request <a href="#send-api-request" id="send-api-request"></a>

To make a request, you need to find the HTTP method and the right path for the operation that you want to use.

{% hint style="warning" %}
It’s highly recommended to use form data parameters when making POST requests to the Web API. If you use URI query parameters instead then these parameters won’t be securely passed to the endpoint.
{% endhint %}

#### Content-Type header

Unless the Sonar Web API endpoint specifications list a specific `Content-Type` value, your request should use the following `Content-Type` header:

`Content-Type: application/x-www-form-urlencoded`

This is the default `Content-Type` value set by most tools and libraries, such as `curl` and Python’s `requests` module, but you should check their documentation for proper usage.

#### Sample API request <a href="#sample-api-request" id="sample-api-request"></a>

If, for example, you want to use the Web API to extract measures, you can make a "GET MEASURES" call to the SonarQube Cloud [`/api/measures`](https://sonarcloud.io/web_api/api/measures?deprecated=false) endpoint in order to extract measures of a given metric for a given project. For this example, a possible request and response are shown below.

<details>

<summary>Sample request</summary>

```bash
curl --request GET \
  --url 'https://sonarcloud.io/api/measures/component?metricKeys=ncloc%2Ccode_smells%2Ccomplexity&component=my_project_key' \
  --header 'Authorization: Bearer my_token' 
```

</details>

<details>

<summary>Sample response</summary>

```bash
{
   "component": {
      "id": "id",
      "key": "my_project_key",
      "name": "my_project_name",
      "qualifier": "TRK",
      "measures": [
         {
            "metric": "complexity",
            "value": "4214"
         },
         {
            "metric": "code_smells",
            "value": "8595",
            "bestValue": false
         },
         {
            "metric": "ncloc",
            "value": "51667"
         }
      ]
   }
}
```

</details>

### Taking into account the API rate limiting <a href="#api-rate-limiting" id="api-rate-limiting"></a>

Some of SonarQube Cloud’s APIs are rate-limited in order to ensure that we can continue to deliver the service smoothly and with optimum performance. In most cases, you should take this into account when automating tasks and processes by using the SonarQube Cloud Web API.

Your API calls will fail with a 429 status code when the rate limit has been reached. If this happens, wait a few minutes before retrying the operation.

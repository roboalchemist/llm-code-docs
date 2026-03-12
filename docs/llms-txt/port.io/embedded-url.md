# Source: https://docs.port.io/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/embedded-url.md

# Embedded URL

The `embedded URL` property is used to embed and display a webpage within an [entity]() in Port.<br /><!-- -->Using this property will automatically create an additional tab in each [entity page](/customize-pages-dashboards-and-plugins/page/entity-page.md), displaying the embedded content.

In the following example, we see the `Shipping` entity page, which is an instance on the `Domain` blueprint.<br /><!-- -->The blueprint has an `embedded URL` property named `Architecture`, which is automatically displayed in a dedicated tab:

![](/img/software-catalog/blueprint/embeddedUrlExample.png)

## URL type[â](#url-type "Direct link to URL type")

Port supports the following URL types:

* **Public link** - A link to a public webpage, which does not require authentication.
* **Private link** - A link to a webpage that is protected by SSO authentication. To use this type, you'll need to provide the required parameters, see the [authentication](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/embedded-url/authentication.md) section for more information and examples.

## ð¡ Common embedded URL usage[â](#-common-embedded-url-usage "Direct link to ð¡ Common embedded URL usage")

* Display a service's architecture
* Display & track a service's Datadog dashboard
* Display charts and diagrams from external tools

## Schema definition[â](#schema-definition "Direct link to Schema definition")

* API
* Terraform

```
{
  "myEmbeddedUrl": {
    "title": "My Embedded URL",
    "type": "string",
    "format": "url",
    "spec": "embedded-url",
    "description": "embedded-url Prop",
    // specAuthentication is needed only when using a protected/private URL
    "specAuthentication": {
        "authorizationUrl": "https://app.com",
        "tokenUrl": "https://app.com",
        "clientId": "1234",
        "authorizationScope": [
          "api://xxxx-xxxx-xxxx-xxxx-xxxx/user.read"
        ]
      }

  }
}
```

```
resource "port_blueprint" "myBlueprint" {
  # ...blueprint properties
  properties {
    identifier = "myEmbeddedUrl"
    title      = "My Embedded URL"
    required   = false
    type       = "string"
    format     = "url"
    spec       = "embedded-url"
  }
}
```

## Examples[â](#examples "Direct link to Examples")

### Datadog dashboard[â](#datadog-dashboard "Direct link to Datadog dashboard")

In this example we are embedding a [Datadog](https://docs.datadoghq.com/dashboards/sharing/) dashboard in order to get application metrics directly inside Port.

Add the `embedded-URL` property to a Blueprint:

Blueprint property definition

```
{
  "datadog": {
    "title": "Datadog",
    "type": "string",
    "format": "url",
    "spec": "embedded-url"
  }
}
```

Create or edit an Entity of the Blueprint you added the `Datadog` property to, and specify the URL to the Datadog dashboard:

![Datadog Entity edit example](data:image/png;base64,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2NvtKw899JAfuQ5ZffXVK/wiDOfdlZ9//tnTt0G4ZhLc+3vuuWfFXlxYDVPmVvUczCe2vqxstdVWXVItc+sSoMWL+++/33H473//21RMIzcV0zw2FbZeoBVWWKFiWs16QVrye+KJJ7we9p6jluL1RmD73p6X7eWXX26Y3SKLLFI544wzGoarleYPP/xQWW655Ty/m266qWE6EeDAAw+szDLLLF1+3If8jAhGsJrH2267zcPOOeecld///vd+fsEFF9QMj0czfe+oo46qrLzyynXTadaT8lAfyshxmmmm8Tm+LL6RJg9DuEZS7MuHHXaYx6UtwZR8nnrqqUbJNOXfyljaVIItBOq1Zdn444+fJplkkjTvvPOmbbfdNo0wwgjp9ttvr7JGAyGdddZZ6eSTT0533XVXsjqkL774Ip1yyinJBjL34/t0SFlY9xjkd+655/oqJT4NEH6sCu+444502mmnJbuRPP3ws8nDV3n4XX755envf/+7s/nw11EI9CcEYnsRDVeZ4M7qEu0XGjHOidMu4QO1F154YZdHuMvc2pU/K+ai5rvMrV35l6XLSv6GG24o85JbDQRs4Z7GHnvsZBNwjRCtO9dK86KLLnINUasp7r///j5/MIfEb7HFFku/+93v0nDDDdcwuX322Sf94Q9/SEaAXYNqC5a01157uVazYeReCICmi/KcdNJJ6cknn0xo0maccca07777/iL3b775JlF+hHZrRdjpYv4/9dRTfbfMCFeaZ5550hFHHNFKMn0ybK8Rr7z2ww47bDImn9544w13ttWLA4w6F2BRXzIRjDjiiNXBkq0Q3jZbKywJoeKFvKHq58a89NJLq9lCrP7yl794J5l77rkTg/7xxx9f/WzANddc48TLGLyrTCFgUb5qIjoRAv0EgbDh4rjmmmt6qTmfaKKJ/BduHOM84nS3ip9++qnbiy266KJp880393uNtDAzsJWsJ7v00ksn03aXuhHg6quv9kGd44orrphWWWUVXyj9+OOPHp8/tgh22223RD6bbrppF/LCGHDFFVdUw3LCh3HffPPNlG+nFt1MS5HOP//8ZFoBT3fjjTf2xVmXhAoXbANRDtI1bZrnkwfhPUGnn356Wn755T3M9ttvn9555x0PwgLz4IMPTq+++qrX8/rrr3f3enEIYDsIPo6tttpqaYkllvBFokfM/pjsGNvA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)

Now go to the specific entity page of your Entity and the Datadog dashboard will be visible in a dedicated tab:

![Datadog dashboard example](/assets/images/datadog-c2f969d502d2aa1e80668f1584755b1d.png)

### New Relic Chart[â](#new-relic-chart "Direct link to New Relic Chart")

In this example we are embedding a CPU usage [New Relic Chart](https://one.eu.newrelic.com/) to get infrastructure metrics directly inside Port.

Add the `embedded-URL` property to a Blueprint:

Blueprint property definition

```
{
  "cpuUsage": {
    "type": "string",
    "title": "CPU usage",
    "spec": "embedded-url",
    "format": "url"
  }
}
```

Go to new relic and extract the chart URL of a specific chart

![New Relic get embed URL](/assets/images/GetEmbedUrlNewRelic-e5eb1f6949302d2a9cb5d3cbb2351092.png)

Create or edit an Entity of the Blueprint you added the `cpuUsage` property to, and specify the URL to the CPU Usage chart:

![New Relic Entity edit example](/assets/images/editEntityNewRelic-e9eee5a55f5ca8517248ceb75c8e100f.png)

Now go to the specific entity page of your Entity and the CPU Usage chart will be visible in a dedicated tab:

![New Relic dashboard example](/assets/images/new-relic-84de49a9e2ea2ff834011c6b87f28cef.png)

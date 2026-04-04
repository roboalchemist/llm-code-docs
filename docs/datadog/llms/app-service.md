# Source: https://docs.datadoghq.com/security/application_security/setup/azure/app-service.md

---
title: Enabling AAP for Azure App Services
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > App and API Protection > Enabling App and API
  Protection > Enabling AAP for Azure App Services
---

# Enabling AAP for Azure App Services

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Compatibility{% #compatibility %}

Only *web applications* are supported. Azure Functions are not supported.

**Note**: Threat Protection through Remote Configuration is not supported. Use [Workflows](https://docs.datadoghq.com/security/default_rules/security-scan-detected/) to block IPs in your [WAF](https://docs.datadoghq.com/serverless/libraries_integrations/plugin/).

| Type   | OS             | Threat Detection |
| ------ | -------------- | ---------------- |
| Java   | Windows, Linux | yes              |
| .NET   | Windows, Linux | yes              |
| Node   | Linux          | yes              |
| Python | Linux          | yes              |
| Ruby   | Linux          | yes              |
| PHP    | Linux          |

## Setup{% #setup %}

### Set application settings{% #set-application-settings %}

To enable AAP on your application, begin by adding the following key-value pairs under **Application Settings** in your Azure configuration settings.

{% image
   source="https://datadog-docs.imgix.net/images/serverless/azure_app_service/application-settings.11370e675fea49d1906ce20ad41d8ec8.jpg?auto=format"
   alt="Azure App Service Configuration: the Application Settings, under the Configuration section of Settings in the Azure UI. Three settings are listed: DD_API_KEY, DD_SERVICE, and DD_START_APP." /%}

- `DD_API_KEY` is your Datadog API key.
- `DD_CUSTOM_METRICS_ENABLED` (optional) enables custom metrics.
- `DD_SITE` is the Datadog site [parameter](https://docs.datadoghq.com/serverless/distributed_tracing/). Your site is . This value defaults to `datadoghq.com`.
- `DD_SERVICE` is the service name used for this program. Defaults to the name field value in `package.json`.
- `DD_START_APP` is the command used to start your application. For example, `node ./bin/www` (unnecessary for applications running in Tomcat).
- `DD_APPSEC_ENABLED` value should be 1 in order to enable App and API Protection

### Identifying your startup command{% #identifying-your-startup-command %}

Linux Azure App Service Web Apps built using the code deployment option on built-in runtimes depend on a startup command that varies by language. The default values are outlined in [Azure's documentation](https://learn.microsoft.com/en-us/troubleshoot/azure/app-service/faqs-app-service-linux#what-are-the-expected-values-for-the-startup-file-section-when-i-configure-the-runtime-stack-). Examples are included below.

Set these values in the `DD_START_APP` environment variable. Examples below are for an application named `datadog-demo`, where relevant.

| Runtime   | `DD_START_APP` Example Value                                                               | Description                                                                                                                                                                                                    |
| --------- | ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Node.js   | `node ./bin/www`                                                                           | Runs the [Node PM2 configuration file](https://learn.microsoft.com/en-us/azure/app-service/configure-language-nodejs?pivots=platform-linux#configure-nodejs-server), or your script file.                      |
| .NET Core | `dotnet datadog-demo.dll`                                                                  | Runs a `.dll` file that uses your Web App name by default.**Note**: The `.dll` file name in the command should match the file name of your `.dll` file. In certain cases, this might not match your Web App.   |
| PHP       | `cp /home/site/wwwroot/default /etc/nginx/sites-available/default && service nginx reload` | Copies script to correct location and starts application.                                                                                                                                                      |
| Python    | `gunicorn --bind=0.0.0.0 --timeout 600 quickstartproject.wsgi`                             | Custom [startup script](https://learn.microsoft.com/en-us/azure/app-service/configure-language-php?pivots=platform-linux#customize-start-up). This example shows a Gunicorn command for starting a Django app. |
| Java      | `java -jar /home/site/wwwroot/datadog-demo.jar`                                            | The command to start your app. This is not required for applications running in Tomcat.                                                                                                                        |

**Note**: The application restarts when new settings are saved.

### Set General Settings{% #set-general-settings %}

{% tab title="Node, .NET, PHP, Python" %}
Go to **General settings** and add the following to the **Startup Command** field:

```
curl -s https://raw.githubusercontent.com/DataDog/datadog-aas-linux/v1.14.0/datadog_wrapper | bash
```

{% image
   source="https://datadog-docs.imgix.net/images/serverless/azure_app_service/startup-command-1.7655beacbd7a4e4282eaf0aebb660ab6.jpeg?auto=format"
   alt="Azure App Service Configuration: the Stack settings, under the Configuration section of Settings in the Azure UI. Underneath the stack, major version, and minor version fields is a 'Startup Command' field that is populated by the above curl command." /%}

{% /tab %}

{% tab title="Java" %}
Download the [`datadog_wrapper`](https://github.com/DataDog/datadog-aas-linux/releases) file from the releases and upload it to your application with the Azure CLI command:

```
  az webapp deploy --resource-group <group-name> --name <app-name> --src-path <path-to-datadog-wrapper> --type=startup
```

{% /tab %}

## Testing threat detection{% #testing-threat-detection %}

To see App and API Protection threat detection in action, send known attack patterns to your application. For example, send a request with the user agent header set to `dd-test-scanner-log` to trigger a [security scanner attack](https://docs.datadoghq.com/security/default_rules/security-scan-detected/) attempt:

```sh
curl -A 'dd-test-scanner-log' https://your-function-url/existing-route
```

A few minutes after you enable your application and exercise it, **threat information appears in the [Application Signals Explorer](https://app.datadoghq.com/security/appsec)**.

## Further reading{% #further-reading %}

- [How App and API Protection Works](https://docs.datadoghq.com/security/application_security/how-it-works/)
- [OOTB App and API Protection Rules](https://docs.datadoghq.com/security/default_rules/?category=cat-application-security)
- [Troubleshooting App and API Protection](https://docs.datadoghq.com/security/application_security/troubleshooting)
- [App and API Protection](https://docs.datadoghq.com/security/application_security/threats/)
- [Datadog Security extends compliance and threat protection capabilities for Google Cloud](https://www.datadoghq.com/blog/datadog-security-google-cloud/)

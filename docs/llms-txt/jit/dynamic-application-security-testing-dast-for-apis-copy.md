# Source: https://docs.jit.io/docs/dynamic-application-security-testing-dast-for-apis-copy.md

# Configuring Vulnerability Scans for APIs

# Activate API scanning with Jit DAST

Complete the following steps to begin configuring DAST for API scanning:

1. Select **ASPM → Security Plans** from the left menu, scroll to **Dynamic Application Security Testing** and locate **Scan your API for vulnerabilities**.

![](https://files.readme.io/c7e5053-image.png)

2. Select **Activate**.
3. Click **Add new application** to begin configuring DAST scanning for your API.

***

# Configure API scanning with Jit DAST

* Step 1: Setting the target and authentication
* Step 2: Setting the scanning triggers
* Step 3: Configure notifications (recommended)

## Step 1:  Setting the target and authentication

### Setting the target

![](https://files.readme.io/6a0ad6c-image.png)

| Field                                     | Description                                                                                                                                                                            |
| :---------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Application Name                          | Name of the application that is scanned.                                                                                                                                               |
| Open API (Swagger) file URL / Upload File | The URL where the OpenAPI file is hosted. The Swagger file has to be valid OpenAPI format ([validate here](https://editor.swagger.io/)) and **must not include** Non-ASCII characters. |
| (Optional) Exclude URLs                   | URLs that are not scanned. For example, Logout. We recommend excluding Logout so that Jit scanning remains continually connected.                                                      |
| API Domain                                | The base URL where the API is hosted, serving as the entry point for making API requests.                                                                                              |
| Enable Authentication                     | We recommend enabling this option for enhanced security scanning. See **Enabling authentication** below.                                                                               |

### Enabling Authentication (recommended)

> Enabling authentication requires some specialized configuration, which is why we ask that you meet with us for a free onboarding session if you want to enable authentication. Schedule your onboarding session [here](https://www.jit.io/book-a-demo).

Check **Enable authentication**. There are four types of authentication:

| Authentication Type       | Fields                         | Description                                                                                                                                                                                                                                               |
| :------------------------ | :----------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Form-based authentication | Login URL                      | Login URL for authentication.                                                                                                                                                                                                                             |
|                           | Username                       | Username to be authenticated.                                                                                                                                                                                                                             |
|                           | Password                       | Password to be authenticated.                                                                                                                                                                                                                             |
|                           | Enable Selectors Configuration | Check to enable enhanced authentication using the username and password selectors that are derived from the source of  the Login's web page. When unchecked, Jit searches for common selectors. See **Configuring authentication using selectors** below. |
| Local storage             | Local Storage Item Key         | The specific identifier used in the Web Storage API for storing and retrieving data in the web browser's local storage.                                                                                                                                   |
|                           | Local Storage Item Value       | The actual information that is stored and retrieved using a specific key.                                                                                                                                                                                 |
| Custom cookie             | Cookie name                    | Name of the cookie used for authentication.                                                                                                                                                                                                               |
|                           | Cookie value                   | Value of the cookie used for authentication.                                                                                                                                                                                                              |
| Bearer token header       | Value                          | The value of the bearer token header consisting of the word Bearer followed by a space and then the actual token.                                                                                                                                         |

1. Check **Enable Selectors Configuration**.\
   ![](https://files.readme.io/ef04a05-image.png)
2. To complete the **Username Field Selector** and  **Password Field Selector** fields, go to your **application's website** and open the **Developer Tools** and then use the **Inspect Element** to find the matching selectors for the **Username** and **Password**.\
   For example:\
   ![](https://files.readme.io/2d16dfd-image.png)\
   ![](https://files.readme.io/8c8b21f-image.png)
3. Copy the **text** into the **Username Field Selector** and  **Password Field Selector** fields.

## Step 2: Setting the scanning trigger

![](https://files.readme.io/7120873-image.png)

| Field                                | Description                                                                                                                                                                                                                                                                                         |
| :----------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Scan Daily                           | ZAP scans your application daily.                                                                                                                                                                                                                                                                   |
| Scan on deployment (only for GitHub) | Jit scans your application when a deployment event is detected in your GitHub account.                                                                                                                                                                                                              |
| Environment name (only for GitHub)   | The environment defined in the deployment YAML on GitHub actions. Jit needs an exact match between the environment name defined in Jit and in GitHub Actions to trigger a scan. [See Deployment-based Scanning](https://dash.readme.com/project/jitsecurity/v4.5.0/docs/deployment-based-scanning). |

## Step 3: Configure notifications

Integrate with Slack to stay notified of new scan results. See configuration instructions [here](https://docs.jit.io/v5.0/docs/integrating-with-slack).

![](https://files.readme.io/eb1b49a-image.png)

Click **Activate**. Jit creates a header based on your configurations and shares the authentication information with ZAP.  The header is integrated by ZAP and used to authenticate the API. Jit then generates security findings, which are documented in the [Backlog page](https://docs.jit.io/v5.0/docs/jit-backlog).

> 🔒 Whitelisting Jit DAST scanners
>
> To perform API scans, Zap requires access to your APIs. If your APIs are secured with a whitelist, please ensure the following IP addresses are included:
>
> For Jit - 🇺🇸 US site (<https://platform.jit.io>)
>
> * 3.220.250.224/32
> * 52.45.232.22/32
>
> For Jit - 🇪🇺 Europe site (<https://platform.eu.jit.io>)
>
> * 18.198.245.94/32
> * 18.157.204.182/32
>
> Adding these IP addresses to your whitelist will enable Zap to conduct its scans without interruption.
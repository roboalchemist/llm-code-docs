# Source: https://tyk.io/docs/tyk-cloud/initial-portal-config.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure Developer Portal in Tyk Cloud

> Learn how to set up and configure the Developer Portal in Tyk Cloud Control Plane deployments.

After deploying your Control Plane, you need to perform some initial configuration for the Developer Portal to prevent seeing any `Page Not Found` errors when trying to access the portal. You need to set up a Home page from the Control Plane Dashboard.

Watch our video on configuring your Tyk Cloud Developer Portal.

<iframe width="560" height="315" src="https://www.youtube.com/embed/8_SPUake84w" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

1. From the Control Plane Dashboard, select **Pages** from the **Portal Management** menu
2. Click **Add Page**

<img src="https://mintcdn.com/tyk/GWakR0LnkXjsKcah/img/getting-started/create-account-portal-pages.png?fit=max&auto=format&n=GWakR0LnkXjsKcah&q=85&s=f75cb823562a40474b693395eacc59dc" alt="Add Portal Page" width="2838" height="1558" data-path="img/getting-started/create-account-portal-pages.png" />

3. In the Settings, give your page a name and slug. Below we've called it Home
4. Select **Check to make this page the Home page**
5. Select **Default Home page template** from the Page type drop-down list
6. You can leave the Registered Fields sections for now

<img src="https://mintcdn.com/tyk/GWakR0LnkXjsKcah/img/getting-started/portal-home-page-settings.png?fit=max&auto=format&n=GWakR0LnkXjsKcah&q=85&s=9bbd2b18a5aef2e35276d40a9b945cc4" alt="Portal Home page settings" width="2454" height="1356" data-path="img/getting-started/portal-home-page-settings.png" />

7. Click **Save**.

You should now be able to access your Portal from **Open Your Portal** from the **Your Developer Portal** menu.

<img src="https://mintcdn.com/tyk/GWakR0LnkXjsKcah/img/getting-started/portal_menu.png?fit=max&auto=format&n=GWakR0LnkXjsKcah&q=85&s=a1469de2c678e958da9e7b9cbaf23a89" alt="Portal Menu" width="2000" height="1432" data-path="img/getting-started/portal_menu.png" />

#### Further Portal Configuration

Our Developer Portal is completely customizable. See [Portal Customization](/tyk-developer-portal/customise) for more details.


Built with [Mintlify](https://mintlify.com).
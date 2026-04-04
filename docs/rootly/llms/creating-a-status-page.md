# Source: https://docs.rootly.com/configuration/creating-a-status-page.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating A Status Page

> Set up and customize public status pages to communicate service health and incident updates to your customers and stakeholders.

Creating a status page only takes about a minute. Before you do so, we recommend you have at least one [service](https://docs.rootly.com/configuration/services) configured in Rootly that you can display on your status page. You can do this by visiting **Configuration > Services** or if you have the [PagerDuty integration](/integrations/pagerduty/pagerduty) configured, you can easily import services directly from PagerDuty then add them to your status page.

To create a new status page:

1. In the Rootly navigation bar, click on **Configuration**, then **Status Pages**.
2. Next, click **Add New Status Page**.
3. Give your status page a name and description. These are internal to Rootly, and will not be used on the actual Status Page.

# **Customize your Status Page**

Once you've created your status page, you're able to customize the look and feel of the page to tailor the contents to your end users.

## **Setup**

Under setup, you're able to make changes to the name and description of your status page. Remember: these are internal only so should be descriptive for other Rootly admins to know what the status page is.

Here, you can also determine if the page will be private or publicly available. Learn more about public and private status pages [here](https://docs.rootly.com/configuration/public-and-private-status-pages).

In the Advanced Settings, you can also customize the domain name of the status page. By default, Rootly will assign each Status Page a URL in the following format:

`rootly.com/teams/[your-org-name]/status-pages/[status-page-name]/[public/private]`

Configure your own custom domain by following: [Custom Domain Names for Status Pages](/configuration/custom-domain-names-for-status-pages). Note: for custom external domain names, you may need to talk with the team at your organization to have them help you configure a custom domain name and associated DNS. 

<img src="https://mintcdn.com/rootly/7ojKISea6oiQMk0o/images/status-pages/status-page-setup-tab.webp?fit=max&auto=format&n=7ojKISea6oiQMk0o&q=85&s=9a97051442f495a6c183c560e2d62d39" alt="Setup Status Page" width="3400" height="1936" data-path="images/status-pages/status-page-setup-tab.webp" />

## **Customize**

Customize the default content and look-and-feel of your status page in the Customize tab. As you make changes to the settings in this tab, the right-hand preview of your status page will reflect your latest updates.

<img src="https://mintcdn.com/rootly/7ojKISea6oiQMk0o/images/status-pages/status-page-customize-tab.webp?fit=max&auto=format&n=7ojKISea6oiQMk0o&q=85&s=f5b1597158260a04433082e2e3da66a5" alt="Customize Status Page" width="3400" height="1940" data-path="images/status-pages/status-page-customize-tab.webp" />

## **Components**

Use the Components section to add Services to your status page. You're able to add any Rootly Service, as well as any third party service your organization uses.

Anytime a selected Service is involved in an incident, it will be reflected on the status page under the 'System Status' section.

**Note**: You'll be able to add third party services to your status page after you've created the status page.

<img src="https://mintcdn.com/rootly/7ojKISea6oiQMk0o/images/status-pages/status-page-components-tab.webp?fit=max&auto=format&n=7ojKISea6oiQMk0o&q=85&s=85c126f29336f89ba745ef2cf736790f" alt="Status Page Component" width="3410" height="1940" data-path="images/status-pages/status-page-components-tab.webp" />

## **Templates**

Standardize the incident updates your teams share with Status Templates. When a commander publishes an incident update to a status page, they'll be able to use the templates defined in this section to help write their update.

<img src="https://mintcdn.com/rootly/7ojKISea6oiQMk0o/images/status-pages/status-page-templates-tab.webp?fit=max&auto=format&n=7ojKISea6oiQMk0o&q=85&s=312db4902de1e850c6a392046504b470" alt="Templates Status Pag" width="3410" height="1940" data-path="images/status-pages/status-page-templates-tab.webp" />


Built with [Mintlify](https://mintlify.com).
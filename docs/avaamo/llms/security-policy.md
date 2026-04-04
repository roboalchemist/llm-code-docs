# Source: https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/security-policy.md

# Security policy

You can configure a list of domains in the **Security policy** page from where the resources are allowed to be loaded in the Avaamo platform. This feature is useful in agent development when you are using resources such as fonts, assets, and web pages (web view) from an external source that is not whitelisted in the Avaamo Platform.

{% hint style="info" %}
**Notes**:&#x20;

* The domains listed on the **Security policy** page ensures that the resources are accessible from your Avaamo dashboard.&#x20;
* When you deploy the agent in other channels, say on another website, then it is upto the security policies of the parent website to handle the accessibility of such resources.
* This option is available only for users with the **Settings** role.&#x20;
* Contact your administrator to learn about the whitelisted IPs for your dashboard.
  {% endhint %}

Consider that you wish to include a font from an external source in the custom CSS of your web channel that is not whitelisted in the Avaamo Platform. When you test the agent using Simulator, you can view the error that the font is not loaded.

**To add security policy**:

* Click your user initials at the top right corner. Click **Settings.**
* Navigate to the **Security policy** in the left navigation menu.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FfT5aC5noMbkEjpocL2tk%2FScreenshot%2031-01-2025%20at%2015.50.png?alt=media\&token=70e4e0e7-d4cd-4c8d-97d5-d60d3e1de797)

* **First field**: List of domains, separated by spaces from where the resources are allowed to be loaded in the Avaamo platform.
* **Second field**: List of script-src domains, separated by spaces from where the resources are allowed to be loaded in the Avaamo platform for webview HTML.
* Click **Update.**
* You can now test the same agent and the font from the domain gets loaded as specified in the Security policy.

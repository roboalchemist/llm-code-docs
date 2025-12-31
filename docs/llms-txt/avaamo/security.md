# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/security.md

# Security

In the **Security** section, you can secure your agent with different authentication mechanisms as per your requirements.&#x20;

{% hint style="info" %}
**Before configuring security details in the web channel**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can deploy the agent to a channel after creating and building an agent. See [Create agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills), for more information.
* If you wish to edit an agent, then:
  * In the **Avaamo Platform UI**, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/how-to/manage-agents/other-common-actions#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editing the agent.
    {% endhint %}

In the **Security** section, you can specify the following details:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FEvB1SlLU3tJkem5KRLkk%2FScreenshot%2006-05-2025%20at%2014.52%20copy.png?alt=media\&token=eb9fbaf2-cd56-4a82-9e5e-a43208923cd4)

<table><thead><tr><th>Parameters</th><th width="374.83822821376987">Description</th><th align="center">Default</th></tr></thead><tbody><tr><td>Is agent publicly accessible on any website?</td><td><p>Use this option if you wish to make the agent publicly accessible on any website. </p><p></p><p>Toggle the slider to enable and disable as required. </p></td><td align="center">Disabled</td></tr><tr><td>Use custom user authentication</td><td><p>Use this if you wish to enable custom authentication for your agents deployed on web and mobile channels using JavaScript code. </p><p></p><p>Toggle the slider to enable and disable as required. </p><p></p><p>See <a href="../../../define-settings#user-authentication-handler">User authentication handle</a>r, for more information.</p></td><td align="center">Disabled</td></tr><tr><td>Cookie expires in (hours)</td><td>Use this configuration option to set the expiry time for cookies in your browser by specifying the duration (in hours) for which the cookies remain active. See <a href="#cookie-expires-in-hours">Cookie expires in (hours)</a>, for more information.</td><td align="center">Must specify a value in the range of 1-8760 hours.</td></tr><tr><td>Allowed domains</td><td><p>Specify a space-separated list of domains where the agent is accessible. Use this if the agent is not publicly accessible.<br></p><p>While adding the URL, If a URL has both a domain and a subdomain, include both. If it only has a domain, mention just the domain name.</p><p></p><p>Examples: </p><p><code>https://www.google.com</code> → <strong><code>www.google.com</code></strong> </p><p><code>https://example.com</code> → <strong><code>example.com</code></strong></p></td><td align="center">NA</td></tr><tr><td>JWT secret key</td><td><p>The key that must be used to encode user information when a JWT token is passed in the web channel URL. </p><p></p><p>Click the <strong>Copy</strong> icon at the end of the textbox to copy the JWT secret key.</p><p></p><p>See <a href="authentication-using-jwt">Authentication using JWT</a>, for more information.</p></td><td align="center">NA</td></tr></tbody></table>

### Cookie expires in (hours)

The cookie configuration option allows you to configure the expiry time for cookies in your browser by setting a specific duration (in hours) for which the cookies remain active. This functionality ensures that user sessions can be automatically terminated after inactivity, providing better control over session management.

**Key features:**

* You can set the number of hours for cookie expiration. The user's session expires once the specified time has passed, and the agent stops responding due to inactivity.
* You can not keep this field empty and must specify a value in the range of 1-8760 hours.

For example, if you set `Cookie expires in (hours)` for one hour. After one hour of inactivity, the agent stops responding and displays the error message: "`Please check your network connection`". You need to restart the conversation from the beginning by refreshing the agent.

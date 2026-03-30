# Source: https://help.aikido.dev/zen-firewall/zen-features/blocking-users-with-zen-firewall.md

# Blocking Users with Zen Firewall

Zen Firewall by Aikido provides a way to identify and block users who are unwanted or trigger attacks, enhancing your app's security by preventing malicious activity.

> **Important**: User blocking operates independently of the global "[Blocking/Detection Mode](https://help.aikido.dev/zen-firewall/zen-features/blocking-vs-detection-mode-in-zen-firewall)" setting. When you enable user blocks, they will always be enforced, even if Zen is in Detection Mode.

### Use Cases <a href="#use-cases" id="use-cases"></a>

* 🔍 **Monitoring active users:** Track user activity to identify and respond to potential threats.
* 🛡️ **Block Malicious Users**: Prevent access from users who have triggered security events

### How to identify and block users <a href="#how-to-identify-and-block-users" id="how-to-identify-and-block-users"></a>

**Step 1:** Identify current users using the `setUser` function found in our agents.

* [Nodejs](https://github.com/AikidoSec/firewall-node/blob/main/docs/user.md)
* [PHP](https://github.com/AikidoSec/firewall-php/blob/main/docs/user.md)
* [Python](https://github.com/AikidoSec/firewall-python/blob/main/docs/user.md)
* [Java](https://github.com/AikidoSec/firewall-java/blob/main/docs/user.md)
* [Dotnet](https://github.com/AikidoSec/firewall-dotnet/tree/main?tab=readme-ov-file#installation)

Once set, Aikido will display all active users in the dashboard.

![User management dashboard showing user status and last activity for a demo app.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FtWGHINuPaAH1SXHyE2I5%2FScreenshot%202025-10-30%20at%2011.59.35.png?alt=media\&token=8817291d-590c-4b63-bf6e-cb18c6647e8c)

**Step 2:** Identify which user to block and open the Action menu by clicking the triple dots.

![User management table showing "Active" status with a menu option to block a user.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FTOhgXJzUjRknCcJhw7HY%2FScreenshot%202025-10-30%20at%2011.59.44.png?alt=media\&token=62362390-6ff1-4acc-a030-ade2f80572e5)

{% hint style="info" %}
Note that user blocking is not immediate; it takes up to a minute for the block to take effect.
{% endhint %}

## Privacy & GDPR <a href="#privacy--gdpr" id="privacy--gdpr"></a>

Passing the user's name is optional, but it can help you identify the user in the dashboard. You will be required to list Aikido Security as a subprocessor if you choose to share personal identifiable information (PII).

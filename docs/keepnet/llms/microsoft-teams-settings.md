# Source: https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/microsoft-teams-settings.md

# Microsoft Teams Settings

Microsoft Teams integration allows you to send training notifications directly inside Teams, where your employees already collaborate every day. Instead of relying only on SMS or email, you can reach users in a familiar workspace without leaving their daily workflow. This makes training invitations harder to miss and easier to act on. Messages arrive from a dedicated bot that you can name, keeping communication clear and professional.

## Prerequisites

* Microsoft 365 tenant with Microsoft Teams enabled.
* Tenant admin/global admin permission to grant consent during setup.
* Keepnet platform access.

## Step 1: Enable the integration

On **Company > Company Settings > Microsoft Teams Settings** you will see two access cards. Enable them in order:

### Access 1: **Connect to Teams**

Links your Microsoft Teams tenant to Keepnet.

1. Click **Enable Access**.
2. Sign in with a Microsoft global admin account.
3. Review and **Accept** the permissions consent.
4. You’ll return to Keepnet and see **Access Enabled**.

### Access 2: **Training Delivery**

Allows Keepnet to send training notifications to Teams.

1. Click **Enable Access** on the second card.
2. Sign in with a Microsoft global admin account.
3. Review and **Accept** the permissions consent.
4. You’ll return to Keepnet and see **Access Enabled**.
5. When both cards show **Access Enabled**, setup is complete and you can send trainings via Teams.

> Status banner: When both accesses are enabled you’ll see **Access complete. You can now send trainings via Teams**.

### Step 2: Managing Setup Policies in Microsoft Teams

Please follow the steps below to allow the '**Keepnet Security Awareness'** app within your Microsoft Teams.

1. Log in to your [Microsoft Teams admin](https://admin.teams.microsoft.com/) center.
2. In the sidebar on the left side, click **Teams** **apps** to expand a drop-down menu.
3. Click **Setup** **policies** from the drop-down menu.
4. On the **App** **setup** **policies** page, you will need to click the name of the policy your team is under. If your team is under the default global policy, click **Global (Org-wide default)**. If your team is under a custom policy, click that custom policy’s name.
5. In the following **Global (Org-wide default)** or custom policy page, click **Add apps** under the **Installed** **Apps** field . A new sidebar will open on the right side of the screen.
6. Use the search bar in the sidebar on the right side of the screen to search for the **'Keepnet Security Awareness'** app. **Select** the app and click **Add**.
7. Click **Save** to apply the changes.
8. The **Keepnet Security Awareness** app will now show under **Installed Apps** or **Teams Apps > Manage Apps** page.
9. Open the **Keepnet** app, then go to **Users and Groups** and make sure **Keepnet Security Awareness** is set to **Available to everyone (org-wide default)**.

{% hint style="warning" %}
After installing the Keepnet Security Awareness app, **please allow up to 12 hours** for changes to take effect in the Microsoft admin center.

If the app takes longer than 12 hours to deploy, it could be due to a conflicting policy. For help with resolving conflicting custom policies in the Microsoft Admin Centre, please reach out to [Keepnet support](https://doc.keepnetlabs.com/resources/keepnet-support-help-desk).
{% endhint %}

{% hint style="success" %}
Once the Keepnet Security Awareness App is added to your Microsoft Admin Centre and waited a few hours or 12 hours, you can test it by entering your business email address and clicking the 'SEND TEST MESSAGE' button on the Company > Company Settings > Microsoft Teams Settings page.
{% endhint %}

## Additional Settings

The following settings can be customised and used within the **Company > Company Settings > Microsoft Teams Settings** page.

### Customize Bot Name

Choose the display name that users will see as the sender in Teams.

1. In **Bot Name**, enter a clear name (e.g., **Keepnet Training Delivery Bot**).
2. Click **Update** to save.

{% hint style="warning" %}
The bot name is not allowed to be updated at the moment, but it will be available to change in the future.
{% endhint %}

### Update Integration Version

If Keepnet releases an integration update for Microsoft Teams, you may see an **Update Integration Version** button. Click it to apply the latest improvements.

### Disable or Revoke Access

* If you need to remove Keepnet’s permissions from your Microsoft Teams tenant for some reason, click the **Disable** **Access** button.
* You can re-enable it later by repeating **Enable the integration**.

## How to Launch Training via Microsoft Teams

You can learn how to launch training content through Microsoft Teams integration by going to the document [here](https://doc.keepnetlabs.com/next-generation-product/awareness-educator/training-library#how-to-launch-training-through-microsoft-teams).

## Troubleshooting

### **1. I don’t see the Microsoft consent page.**

Use a Microsoft tenant/global admin account and try again in a private browser window.

### **2. Access 1 enabled but Access 2 fails.**

Ensure the same admin completes both steps and that Teams is enabled for the tenant. If the issue persists, please take a screenshot of the error and share it with the [support team](https://doc.keepnetlabs.com/resources/keepnet-support-help-desk).

### **3. Messages aren’t arriving in Teams.**

* Confirm both accesses show **Access Enabled**.
* Verify the Bot Name is saved.
* Check the campaign’s audience actually has Teams licenses and can receive chat messages.
* Check the '**Activity**' menu on your Microsoft Teams app to confirm if you see the training enrollment.

If this case persists, contact the [support team](https://doc.keepnetlabs.com/resources/keepnet-support-help-desk) for further assistance.

## FAQ

### **Q: Who can enable the integration?**

A: A Microsoft tenant/global admin and access to the Keepnet platform.

### **Q: Does this replace Email or SMS delivery?**

A: No. It adds Microsoft Teams as an additional training-delivery channel.

### **Q: Can I limit which users receive Teams messages?**

A: Yes. You control the target groups when launching or scheduling a training. Please create target groups for your employees, and launch the training to those groups via Microsoft Teams.

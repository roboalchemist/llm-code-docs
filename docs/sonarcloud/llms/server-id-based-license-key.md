# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/license-administration/server-id-based-license-key.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/license-administration/server-id-based-license-key.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/license-administration/server-id-based-license-key.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/license-administration/server-id-based-license-key.md

# Server ID based license key

To run SonarQube Server, you need a license that corresponds to the plan you had purchased, including SonarQube Server edition, Lines of Code (LOC), staging licenses, commercial support and additional features such as Advanced Security. See [Plans and Pricing](https://www.sonarsource.com/plans-and-pricing/sonarqube/) for more information about the different editions and features.

[Contact sales](https://www.sonarsource.com/plans-and-pricing/contact-sales/) to request the license key or email us at <contact@sonarsource.com>.

After your purchase is confirmed, you will receive a license key. If the license key follows this format: XXXX-XXXX-XXXX-XXXX, see [online-license-management](https://docs.sonarsource.com/sonarqube-server/instance-administration/license-administration/online-license-management "mention"). Otherwise, continue reading this page.

### Permissions

To manage your licenses and additional features in SonarQube Server you must have the Administer System permission.

To apply the permission to users or groups go to **Administration** > **Security** > **Global Permissions** and select the **Administer System** check box.

### Activating your license

After your purchase is confirmed, you will have to request the license key based on your server ID.

<figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/wQoiOb6YqbBol3nwIPe1/license-activation-serverID.png" alt="System info page to copy server ID information"><figcaption></figcaption></figure>

To get your license key based on the server ID:

1. Go to **Administration** > **System**
2. Click **Copy ID information**. You will need the server ID when requesting the license.
3. Email us at <contact@sonarsource.com> to request the license key, provide the info you just copied.

{% hint style="info" %}
The server ID is specific to the current database. Make sure to configure an external database for long-term use prior to requesting your license with this server ID.
{% endhint %}

To activate your SonarQube Server license:

<figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/ELrat2PninJHlJrUij3l/license-activation-online.png" alt="Set up a license modal where you enter your license key"><figcaption></figcaption></figure>

1. Go to **Administration** > **Configuration** > **License Manager**
2. Click **Add license** button to open a modal.
3. Enter your license key in the modal and accept the terms and conditions.
4. Click **Set license** to confirm.

### License invalidation scenarios

Certain actions will change your server ID and invalidate your license. The following are some of the most common cases:

* Moving, upgrading, or changing your database server to another host, available with a different IP or DNS name.
* Changing the existing database server IP or DNS name.
* Changing the database/schema name on the database server.
* Restoring the database content from another SonarQube Server instance (except for production/staging synchronization).
* Reinstalling SonarQube Server on an empty database.
* Using DBCopy or MySQL Migrator to copy your old database into a new one.

If you plan on going through one of these scenarios and you have commercial support, open a support ticket beforehand to confirm the plan of action or to explore alternatives.

When your license is invalidated due to a change of server ID, you can extend it using `api/editions/activate_grace_period` api endpoint to benefit from a grace period of seven days. After this period, the license will remain invalid. Note that you can only do this once and the procedure requires the Administer System permission.

**Curl example:**

```hurl
curl -X POST -u <sqUserToken>: <sqServerBaseUrl>/api/editions/activate_grace_period
```

Replace `<sqUserToken>` and `<sqServerBaseUrl>` with information relevant to your use case.

### SonarQube Server license page

Once your activation has been completed you will see the following information on the SonarQube license page.

<figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/lztqrLYlXnCA7h5cbLwl/license-page-serverid.png" alt="The license administration page for SonarQube Server"><figcaption></figcaption></figure>

1. Click **Set a new license** and enter a new license key to replace your current license. Click on the dropdown menu and select **Unset license** to remove it.
2. **License information**:
   * **Edition**: This is based on the plan you had purchased (Developer, Enterprise or Data Center).
   * **Type**: Type of license, the options are production, test or evaluation.
   * **Expiration date**: Displays when the license expires.
   * **Support included**: Indicates whether commercial support is included in your license.
   * **Activation method**: Displays whether the license was activated online, offline or is based on server ID.
   * **Server ID** of your instance.
3. **License usage**:
   * **Lines of code** (LOC): Shows the number of LOC currently analyzed out of the total allowed by your license.
   * **Notification threshold**: Shows the LOC threshold that triggers email notification. A reminder is sent two months and again one month before your license expires. Click the **Edit notification threshold** to change it. For more information, see [lines-of-code](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/monitoring/lines-of-code "mention") for more information.
4. **Additional features**: Lists all the extra features your organization has purchased, such as [advanced-security](https://docs.sonarsource.com/sonarqube-server/advanced-security "mention"). It shows the feature’s name, availability and enablement.

### Unsetting a license

To remove the license from the system click on the dropdown menu next to the **Set a new license** button and select **Unset license** to remove it.

### Staging licenses

Staging licenses are available in Enterprise and Data Center editions, or with editions with commercial support. Your contract may include one or more staging licenses. You can use these licenses for non-production instances to test new features, for update purposes, new integrations, etc.

The process of activating staging licenses is the same as for production. However, you should consider the following:

#### Setting up staging instance and database

1. Create a staging database and copy the production database into it.
2. Connect your SonarQube Server staging instance to the staging database.
3. Start SonarQube Server and retrieve the generated server ID.
4. Request your staging license key for this server ID.
5. Activate the license on the license administration page.

#### Synchronizing your staging database

To synchronize your staging database with your production database:

1. Empty the staging database and copy the production database into it.
2. Start SonarQube Server.
3. The server ID will be the same as generated the first time, so you can reuse the same license key.

### License key isn't working

If your license key isn't working, send an email to <contact@sonarsource.com> that includes the following information:

1. Server ID found under **Administration** > **System**.
2. SonarQube Server version found under **Administration** > **System**.
3. Clarify what current license, production or staging, and server ID it is replacing.
4. Confirm the status of the existing license.

A new license key will be issued within one business day once we receive an email with the required information.

### Related pages

* [lines-of-code](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/monitoring/lines-of-code "mention")
* [Plans and Pricing](https://www.sonarsource.com/plans-and-pricing/sonarqube/)

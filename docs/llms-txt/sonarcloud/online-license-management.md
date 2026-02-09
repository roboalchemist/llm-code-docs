# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/license-administration/online-license-management.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/license-administration/online-license-management.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/license-administration/online-license-management.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/license-administration/online-license-management.md

# Online license management

To run SonarQube Server, you need a license that corresponds to the plan you purchased, including the SonarQube Server edition, Lines of Code (LOC), staging licenses, commercial support, and additional features such as Advanced Security. See [Plans and Pricing](https://www.sonarsource.com/plans-and-pricing/sonarqube/) for more information about the different editions and features.

[Contact sales](https://www.sonarsource.com/plans-and-pricing/enterprise/) to request the license key or email us at <contact@sonarsource.com>.

After your purchase is confirmed, you will receive a license key. If the license key follows this format XXXX-XXXX-XXXX-XXXX, continue reading this page. Otherwise, see [server-id-based-license-key](https://docs.sonarsource.com/sonarqube-server/instance-administration/license-administration/server-id-based-license-key "mention").

### Permissions

To manage your licenses and additional features in SonarQube Server you must have the **Administer System** permission.

To apply the permission to users or groups go to **Administration** > **Security** > **Global Permissions** and select the **Administer System** check box.

### Activating your license

To activate your SonarQube Server license:

<figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/ELrat2PninJHlJrUij3l/license-activation-online.png" alt="Set up license modal"><figcaption></figcaption></figure>

1. Go to **Administration** > **Configuration** > **License Manager**.
2. Click **Add license** button to open a modal.
3. Enter your license key in the modal and accept the terms and conditions.
4. Click **Set license** to confirm.

An internet connection is required to activate your license. Your instance should be allowed to reach the following resources: `https://api.prod.sonarsource.licensespring.com`

#### Activating your license offline

If your SonarQube Server instance is offline and cannot reach the online resource listed in the previous section after you enter the license key, you will have to choose the **Activate offline** option.

<figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/yZeYHkyfOfRIvAKwr47Q/license-offline.png" alt="Activate the license offline"><figcaption></figcaption></figure>

Then follow these steps:

<figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/vt8PAXb4kx5n6dpj7y2V/license-activation-offline.png" alt="Offline license activations steps"><figcaption></figcaption></figure>

1. Click **Download .req file**, to download the request file to your computer. You will need this file in the next step.
2. Upload this .req request file to the activation page that opens in a new tab. The license activation URL is `https://offlinelicense.sonarsource.com` and it will automatically trigger the download of a .lic license file to your computer.&#x20;
3. Click **Upload .lic file** and locate the .lic file to upload it into your SonarQube Server instance to complete the activation.

### SonarQube Server license page

Once your activation has been completed you will see the following information on the SonarQube license page.

<figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/ckPZEEtC8A1022ReVfVM/license-page-new.png" alt="SonarQube Server license page"><figcaption></figcaption></figure>

1. Click **Set a new license** and enter a new license key to replace your current license. Click on the dropdown menu and select **Unset license** to remove it. See [#unsetting-a-license](#unsetting-a-license "mention") for more information.
2. Click **Refresh license** to fetch all the up-to-date information about the license from the license server. This is required if the license was changed by Sonar to update, for example, the maximum LOC. To refresh the offline activated license you can use **Set a new license** with the same license key.
3. &#x20;**License information**:
   * **Edition**: This is based on the plan you had purchased (Developer, Enterprise or Data Center).
   * **Type**: Type of license, the options are production, test and evaluation.
   * **Start date**: Displays the license start date.
   * **Expiration date**: Shows when the license expires.
   * **Support included**: Indicates whether commercial support is included in your license.
   * **Activation method**: Displays whether the license was activated online, offline or is based on server ID.
   * **License key** currently used.
4. **License usage**:
   * **Lines of code** (LOC): Shows the number of LOC currently analyzed out of the total allowed by your license.
   * **Notification threshold**: Shows the LOC threshold that triggers email notification. A reminder is sent two months and again one month before your license expires. Click the **Edit notification threshold** to change it. See [#checking-your-lines-of-code-consumption](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/monitoring/lines-of-code#checking-your-lines-of-code-consumption "mention") for more information.
5. **Additional features**: Lists all the extra features your organization has purchased. It shows the feature’s name, start and expiration dates, availability and enablement.

### Changing server ID

To move your license to an instance with another server ID you have to unset it on the current instance. See [#unsetting-a-license](#unsetting-a-license "mention") for more information.

{% hint style="info" %}
If the license was not unset and it’s no longer possible to do so, for example, due to an incident, contact us at <contact@sonarsource.com> and we will adjust the activation count on the license server for you so you can use the same license on another instance of SonarQube Server. In case you require zero downtime, use the [#break-glass-license](#break-glass-license "mention").
{% endhint %}

#### License invalidation scenarios

Certain actions will change your server ID and invalidate your license activation. The following are some of the most common cases:

* Moving, upgrading, or changing your database server to another host, available with a different IP or DNS name.
* Changing the existing database server IP or DNS name.
* Changing the database/schema name on the database server.
* Restoring the database content from another SonarQube Server instance (except for production/staging synchronization).
* Reinstalling SonarQube Server on an empty database.
* Using DBCopy or MySQL Migrator to copy your old database into a new one.

If you plan on going through one of these scenarios and you have commercial support, open a [support ticket](https://help.sonarsource.com/) beforehand to confirm the plan of action or to explore alternatives.

### Unsetting a license

The operation of unsetting a license is necessary in several situations:

* When reusing the license on a different instance with another server ID.
* When changing the server ID of the current instance.
* When applying a different license to the current instance.&#x20;

#### Unsetting a license activated online

To unset a license activated online click on the dropdown menu next to **Set a new license** button and select **Unset license** to remove it. Unsetting a license removes it both locally and from the license server and allows you to use it again on another instance or to set a different license on the current instance. Using **Set a new license** button will first unset the current license and then activate a new one.

#### Unsetting license activated offline

If you activated your license offline, unsetting the license in SonarQube UI will not remove it from the license server because your SonarQube Server is not connected to it. The license will only be removed locally, and the license server will still consider it activated.

To fully unset the license from the license server, follow these instructions:

1. **Retrieve the .req file**: Use the `POST /api/v2/entitlements/offline-deactivation` endpoint (requires the Administer System permission).
2. **Unset on the license server**: Go to[ https://offlinelicense.sonarsource.com/](https://offlinelicense.sonarsource.com/) and upload the `.req` file retrieved in the previous step.

This process unsets the license on the license server, allowing you to activate it again on an instance with a different server ID.

You can still rely on the **Unset license** or **Set a new license** functionality in SonarQube UI if you need to set another license on the same instance, for example, after a renewal.

### Break glass license

{% hint style="info" %}
Before performing maintenance on your SonarQube Server deployment that could result in a server ID change (see [#changing-server-id](#changing-server-id "mention")), it is highly recommended to first unset the current license. See [#unsetting-a-license](#unsetting-a-license "mention") for more details.
{% endhint %}

You are entitled to a break glass license available in the License user portal along with the production license. The break glass license should be used if the main production license can’t be activated. It expires in 7 days after the day of activation. The process for activating a break-glass license is the same as for a production license.

To reactivate your main production license, reach out to us at <contact@sonarsource.com>.

### Staging license

A staging license is available in Enterprise and Data Center editions, or in editions with commercial support. Your staging license may include one or more activations, which you can use for non-production instances to test new features, for update purposes, new integrations, and other purposes. The process of activating staging licenses is the same as for production.

### License user portal

As soon as a license is created, your organization will receive an email with access to the License user portal, where you can see all available licenses.

#### Logging into the License user portal

Sonar License user portal is available at <http://license.sonarsource.com/>.&#x20;

* Access to the license user portal requires your email address to be registered by Sonar as a license manager for your organization.
* It is recommended to log in using one of the available Single Sign-On (SSO) authentication providers.
* If this is your first time logging in and you are using an email address instead of an SSO provider, you must first **Sign up** to create an account.

<div align="left"><figure><img src="https://583449977-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FLWhbesChsC4Yd1BbhHhS%2Fuploads%2F4L1cAvYhg6YpFHNlhTdR%2Flicense-user-portal-login.png?alt=media&#x26;token=86815c3c-d6de-4298-a134-a9d3237deda7" alt="" width="375"><figcaption></figcaption></figure></div>

* Your existing[ Help Center](https://help.sonarsource.com/) account credentials are also valid for accessing the License user portal.

#### Checking the license status

<figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/09soxecFBG0bG6UTdAbU/license-user-portal.png" alt="Checking the status of your license"><figcaption></figcaption></figure>

To retrieve the license’s status:

* Click on **Licenses** in the left-side navigation to see a list of all licenses for your organization.&#x20;
* Select a license and navigate to the **Devices** tab.

The **Devices** tab contains a list of SonarQube Server instances. The **Status** column shows the status of the license on that instance, **Active** or **Inactive**. Note that the **Hardware ID** column shows the server ID of your SonarQube Server.

<figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/dz35oy569cqvO45q3WQH/license-user-portal-activation-status.png" alt="Viewing the license&#x27;s status"><figcaption></figcaption></figure>

### License key isn't working

If your license key isn't working, send an email to <contact@sonarsource.com> that includes the following information:

1. Server ID found under **Administration** > **System.**
2. SonarQube Server version found under **Administration** > **System**.
3. Clarify which existing license (production or staging) and server ID it is replacing.
4. Confirm the status of the existing license.

We will fix the problem with the license or issue a new one within one business day once we receive an email with the required information at <contact@sonarsource.com>.

### Related pages

* [](https://docs.sonarsource.com/sonarqube-server/instance-administration/license-administration "mention"): server ID based activation method
* [#checking-your-lines-of-code-consumption](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/monitoring/lines-of-code#checking-your-lines-of-code-consumption "mention")
* [Plans and pricing](https://www.sonarsource.com/plans-and-pricing/sonarqube/)

# Source: https://docs.axonius.com/docs/system-warnings.md

# System Warnings

The system displays banners with warnings about events that can seriously impact your use of the Axonius System. These banners are displayed to administrators and are removed after the required action is taken.

The following banners  could appear:

## Scheduled Activities

**Banner**
*This system is not running scheduled activities. Data may not be up-to-date. Click for Details*

**Explanation:**
An admin has temporarily turned off scheduled activities for this system.\
Contact your admin for more details.
This banner is shown when all system activities are disabled. Typically this is done when an instance is being moved from Customer-hosted (on-premises / private cloud) to Axonius-hosted (SaaS). To enable or disable this setting, you must be an administrator user in Axonius. This is set from System Settings `>` Lifecycle `>` Advanced Lifecycle settings, see [Configuring Advanced Lifecycle Settings](/docs/configuring-advanced-lifecycle-settings).

## Connectivity Issues

**Banner**
*There are/is X Compute Node/s that is/are not reporting. This can lead to data issues. Please check the Manage Nodes tab for more information*.

**Explanation:**

There is a problem of connectivity with one of your Compute Node. This happens when the Compute Node is not reporting back. Open the **Manage Nodes** page from the side menu.  Identify the Compute Node that is not reporting (the last seen should be not recent) and perform a restart of the Compute Node using SSH or the underlying virtualization from the  Compute Node.

Note that when this happens cleanup does not occur on the Axonius Instance.
Not relevant for  **Axonius-hosted (SaaS)** deployments

## Low Disk Space

**Banner**
*There is 1  Compute Node with low disk space. This can lead to data issues. Please check the Manage Nodes tab for more information*.

**Explanation:**

This message is displayed when there is a  low disk percentage, that is, if there is less than 50GB left. Extend the disk space or reduce historical snapshot retention to save less data.
Not relevant for  **Axonius-hosted (SaaS)** deployments

## Fetch Issues

**Banner**
*The system detected an issue in the fetch assets phase. This can lead to data issues. Please check the activity logs for more information. Click for Details*.

**Explanation:**

This message is displayed when the 'Fetch Phase' of the system Lifecycle runs for over 48 hours. Contact Axonius support for further maintenance.

## Certificate Issues

**Banner**
*Your Axonius SSL Certificate will expire in X days.  Click for Details*.

**Explanation:**

Your Axonius self signed certificate is about to expire. Create and upload a new SSL certificate. Refer to [Managing Certificate Settings](/docs/certificate-settings).

## Gateway Issues

**Banner**
*The following Gateways have expired: G-1, G-2. Please rotate each Gateway's certificate and reconnect to the agent.  Click for Details*.

**Explanation:**

This message is displayed when the certificate for a Gateway has expired. You need to rotate the gateway keys and redownload and run the gateway script again. Refer to [Rotating the Gateway Certificate](/docs/manage-tunnels#rotating-the-gateway-certificate).

**Banner**
*The following Gateway's IDs are about to expire: G-1, G-2. The earliest expiration date is in x days. Please rotate each Gateway's certificate and reconnect to the agent. Click for Details*.

**Explanation:**

This message is displayed when the certificate for one or more Gatways is about to expire. The system tells you how soon the earliest gateway will expire. You need to rotate the gateway keys for each of these gateways and redownload and run the gateway script again. Refer to [Rotating the Gateway Certificate](/docs/manage-tunnels#rotating-the-gateway-certificate).

**Banner**

*One or more gateways are running an outdated agent version. Latest version is x.x.x.*

**Explanation:**

This message is displayed on the Gateways page when the version of the latest gateway agent for the current Axonius instance is higher than the running gateway agent. A new gateway version is available, and it is recommended to upgrade each gateway to match the Axonius instance version. This banner is displayed until all gateways are upgraded. See [Managing Gateways](https://docs.axonius.com/axonius-help-docs/docs/manage-gateways).

**Banner**

*This gateway agent is out of date. Current: X.X.X, Latest: X.X.X*

**Explanation:**

This message is displayed in the gateway details drawer when the version of the gateway agent installed is not the same as the version as the Axonius instance. See [Managing Gateways](https://docs.axonius.com/axonius-help-docs/docs/manage-gateways).

**Banner**

*Version information for this gateway isn't available, could be caused by an older agent version. It is recommended to upgrade this gateway.*

**Explanation:**

This message is displayed in the gateway details drawer when the version of the gateway agent is unknown. It is recommended to upgrade the gateway to the same version as the Axonius instance. See [Managing Gateways](https://docs.axonius.com/axonius-help-docs/docs/manage-gateways).
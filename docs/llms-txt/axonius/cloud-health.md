# Source: https://docs.axonius.com/docs/cloud-health.md

# CloudHealth

CloudHealth is a cloud management platform to analyze and manage cloud cost, usage, security, and governance.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **CloudHealth Domain** *(required, default: `https://chapi.cloudhealthtech.com`)* - The hostname of the Cloud Health server.
2. **API Key** *(required)* - The API Key generated through the CloudHealth web interface. To generate an API key, see [Generate an API Key](/docs/cloud-health#how-to-generate-an-api-key).
3. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

<Image alt="CloudHealth" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CloudHealth.png" />

<Callout icon="📘" theme="info">
  Note

  To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).
</Callout>

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch AWS accounts** - Select whether all connections for this adapter will fetch  AWS accounts.
2. **Fetch AWS Classic Load Balancers**    - Select  whether all connections for this adapter will fetch  AWS Classic Load Balancers.
3. **Fetch AWS Application Load Balancers**  - Select whether all connections for this adapter will fetch AWS Application Load Balancers.
4. **Fetch AWS Network Load Balancers**    - Select  whether all connections for this adapter will fetch AWS Network Load Balancers.
5. **Fetch AWS RDS instances**  - Select  whether all connections for this adapter will fetch AWS RDS instances.
6. **Fetch AWS S3 buckets**   - Select  whether all connections for this adapter will fetch AWS S3 buckets.
7. **Fetch AWS VPCs**  - Select  whether all connections for this adapter will fetch AWS VPCs.
8. **Fetch AWS NAT gateways**   -  Select  whether all connections for this adapter will fetch AWS NAT gateways.
9. **Fetch Azure VMs**   - Select whether all connections for this adapter will fetch  Azure VMs.
10. **Fetch Azure IP addresses**  - Select  whether all connections for this adapter will fetch  Azure IP addresses.
11. **Fetch Azure virtual networks** - Select  whether all connections for this adapter will fetch  Azure virtual networks.
12. **Fetch Azure network interfaces**   - Select  whether all connections for this adapter will fetch  Azure network interfaces.
13. **Fetch Azure Subscription and ID**  - Select this option to  fetch Azure Subscription and ID information.
14. **Fetch GCP computer instances**  - Select whether all connections for this adapter will fetch  GCP computer instances.
15. **List AWS Account tags as adapter tags** - Select to consider the AWS Account tags as adapter tags.
16. **Fetch offline assets** - Select whether to fetch offline assets.
17. **Fetch GCP project information** - If selected, will fetch the Google project ID and name for GCP assets.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the Adapter Configuration tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Cloud Health API](https://apidocs.cloudhealthtech.com/#documentation_getting-your-api-key).

## Generate an API Key

1. Click **My Profile** in your user settings.
   ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(345\).png)

2. In your profile settings, scroll to the API Key section and click **Get API Key**. Then click **Save Profile Changes**.
   ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(346\).png)

## Create a Read-only User for Axonius

When a dedicated user is required, you need to create the Axonius user role and Axonius user.

### Creating the Axonius User Role

**To create the Axonius User role**

1. In the left menu bar, navigate to **Setup `>` Admin `>` Roles**.
2. Copy the Standard User profile and fill-in the following fields:
   * Name - "Axonius User"
   * Description - "Standard User with Generate API Key privileges"
3. Select the checkbox next to:
   * **All Privileges `>` Setup `>` Generate API Key Profile**.
4. Save the profile.

### Creating an Axonius User

An Axonius user is a Standard User (read only user) that has the capability to also  generate an API key.

**To create an Axonius user**

1. From the left menu bar, navigate to **Setup `>` Admin `>` Users**.
2. From the right corner of the page, click **INVITE USER** and fill-in the following fields:

* Full Name - Axonius User
* Email Address
* Role - Axonius User
* Organization

3. Click **Invite User**.
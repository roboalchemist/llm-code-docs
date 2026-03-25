# Source: https://docs.axonius.com/docs/google-cloud-platform-gcp.md

# Google Cloud Platform (GCP)

Google Cloud Platform (GCP) is a suite of cloud computing services. Alongside a set of management tools, it provides a series of modular cloud services including computing, data storage, data analytics and machine learning.

## Types of Assets Fetched

This adapter fetches the following types of assets, some may need to be selected as advanced options:

* Devices, Users, Software, SaaS Applications, Compute Services, Application Services, Networks, Load Balancers, Databases, Object Storage, Accounts/Tenants, Serverless Functions, Disks, Compute Images, Network/Firewall Rules, Application Resources

**Related Enforcement Actions**:

* [GSuite - Add Users](/docs/gsuite-add-users)
* [GSuite - Remove Users](/docs/gsuite-remove-users)
* [GSuite - Add Users to Group](/docs/gsuite-add-users-to-group)
* [GCP - Add or Remove Tags to/from Assets](/docs/gce-compute-add-tags)

## Parameters

1. **JSON Key pair for the service account** *(required)* - A JSON-document containing service-account credentials to GCP. For details, see [Connect Axonius to Google Cloud Platform](/docs/google-cloud-platform-gcp#connect-axonius-to-google-cloud-platform).

2. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the GCP APIs.

3. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

5. **Projects Include Filter (GCP Format)** *(optional)* - Filter by projects accessible by the active account, as per the [Gcloud Topic Filters](https://cloud.google.com/sdk/gcloud/reference/topic/filters#Operator-Terms).

6. **Exclude App Scripts Projects** - Select this option to exclude App Script projects from the projects data fetched by this adapter.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="GCP_Connection" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/GCP_Connection.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Email domain include list** *(optional)* - Enter a comma-separated list of email domains to include in the fetch. If left empty, all connections for this adapter will fetch all users unless the **Email domain exclude list** is populated.
2. **Email domain exclude list** *(optional)* - Enter a comma-separated list of email domains to exclude from the fetch when the **Email domain include list** is empty.
3. **Fetch Google Cloud Clusters** - Select this option to fetch Cluster devices and display them in the **Devices** page.
4. **Fetch Google Cloud SQL database instances** - Fetch all Google Cloud SQL instances.
   * If enabled, all connections for this adapter will fetch Google Cloud SQL database instances.
   * If disabled, all connections for this adapter will not fetch Google Cloud SQL database instances.

<Callout icon="📘" theme="info">
  Note

  Fetching Google Cloud SQL database instances also requires the following:

  1. [Enabling the Cloud SQL Admin API](#1enablecloudapis)
  2. [Cloud SQL Viewer role](#2createaserviceaccountandgrantpermissionstothatserviceaccount)
</Callout>

3. **Fetch Google Cloud Routers** - Select to fetch Google Cloud routers.
4. **Fetch Google Instance Groups** - Select to fetch Google Instance Groups as Compute Services.
5. **Fetch Google Cloud VPCs** - Select whether to fetch VPCs from Google Cloud as assets.
6. **Fetch Subnets as assets** - Split subnets of a VPC network into individual assets.
7. **Fetch Google Cloud Storage buckets** Select to fetch all Google Cloud Storage buckets.
   * If enabled (default), all connections for this adapter will fetch the GCP Storage buckets.
   * If disabled, all connections for this adapter will not fetch the GCP Storage buckets.

<Callout icon="📘" theme="info">
  Note

  Fetch all Google Cloud Storage buckets also requires the following:

  1. [Google Cloud Storage JSON API](https://docs.cloud.google.com/storage/docs/json_api)
  2. Storage Object Viewer role
</Callout>

4. **Fetch Google Cloud Compute Images (Images, Snapshots and Templates)** - Select whether to fetch all Google Cloud Compute Disk Images, Snapshots and Templates.
5. **Fetch Object metadata in Google Cloud Storage buckets (0: disabled, max supported: 1000)** *(optional, default: 0)* - Fetch Object metadata in GCP Storage buckets that includes: name, size, and links to objects within each bucket.
   * If supplied, all connections for this adapter will fetch 1000 objects or the specified number, the smallest of the two.
   * If not supplied, all connections for this adapter will not fetch Object metadata in GCP Storage buckets.

<Callout icon="📘" theme="info">
  Note

  Fetch object metadata in GCP Storage buckets also requires the following:

  1. [Google Cloud Storage JSON API](https://docs.cloud.google.com/storage/docs/json_api)
  2. Storage Object Viewer role
</Callout>

5. **Fetch IAM permissions for users** - Fetch IAM permissions and associate those to the users roles. This includes permissions for build-in roles as well as Subscription-level and Project-level custom defined roles.
   * If enabled (default), all connections for this adapter will fetch IAM permissions and will associate those to the users roles. These permissions will be represented as the **Role Details** complex field. This must be enabled to use the Axonius - Send Email to Assets action to send emails to GCE account administrators.
   * If disabled, all connections for this adapter will not fetch IAM permissions.

<Callout icon="📘" theme="info">
  Note

  Fetch IAM permissions and associate those to the users roles requires the following:

  * Role Viewer
</Callout>

13. **Only Fetch SCC Assets with associated SCC Findings** - Select this option to only fetch SCC assets that have findings.
14. **Fetch organizational tags** - Select this option to enrich VM instances with organizational tags or project tags associated with them.
15. **Fetch users** *(optional, default: true)* - Unselect this option to exclude user data from the fetch.
16. **Security Command Center (SCC) Organizations** *(optional)* - Specify a comma-separated list of organization IDs.
    * If supplied, all connections for this adapter will fetch Security Command Center device assets and their associated vulnerabilities from the specified list of organization IDs.
    * If not supplied, all connections for this adapter will not fetch any Security Command Center device assets.

<Callout icon="📘" theme="info">
  Note

  Fetch Security Command Center device assets and their associated vulnerabilities requires the following organization-level roles to each of the specified organizations:

  1. [ Security Center Findings Viewer role](#2createaserviceaccountandgrantpermissionstothatserviceaccount)
  2. [ Security Center Assets Viewer role](#2createaserviceaccountandgrantpermissionstothatserviceaccount)

  Alternatively, Security Center Admin is required.
</Callout>

17. **Fetch SCC findings from the last X days (0: disabled, max supported: 90)** *(optional, default: 90)* - Specify the number of days SCC findings data is to be fetched.
    * If supplied, all connections for this adapter will fetch SCC findings data gathered in the last number of days as specified.
    * If not supplied, all connections for this adapter will fetch SCC findings data gathered in the last 90 days.

18. **Custom filter expression for SCC findings** *(optional)* - Specify an [expression](https://cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.assets/list#query-parameters) that defines the filter to apply across assets fetched from SCC.
    * If supplied, all connections for this adapter will apply the specified filter when fetching SCC assets.
    * If not supplied, all connections for this adapter will not apply any filter when fetching SCC assets.

19. **Number of parallel connections** *(required, default: 20)* - Specify the number of connections to be opened to control the performance of the data fetch.

20. **Fetch only compute devices that are turned on** - Select this option to not fetch compute devices that are turned on.

21. **List of tags to parse as fields** *(optional, default: empty)* - Specify a comma-separated list of tag keys to be parsed as device or user  fields. Each tag is a key-value pair that is part of the **Adapter Tags** complex field.
    * If supplied, all connections for this adapter will parse any of the listed tags that are associated with the fetched device or user as:
      * Values of the **Adapter Tags** field.
      * Designated field with the name of the tag key and the value of the tag value.
    * If not supplied, all connections for this adapter will only parse all tags as values of the **Adapter Tags** field.

22. **Fetch Google Cloud Serverless Functions** - Select this option to fetch Serverless Functions from the 'Cloud Functions' service using the [Method: projects.locations.functions.list API](https://cloud.google.com/functions/docs/reference/rest/v2/projects.locations.functions/list).To fetch  Google Cloud Serverless Functions the following permissions need to be granted:
    1. OAuth scope: `https://www.googleapis.com/auth/cloud-platform`
    2. IAM permission on the specified resource parent: `cloudfunctions.functions.list`

23. **Fetch Google Cloud APIs** - Select this option to fetch APIs from Apigee. To enable this, the following IAM permission on the specified resource parent is required: `apigee.proxies.list`

24. **Fetch Google Cloud Run Services** - Select this option to fetch Cloud Run Services and parse them as Compute Services.

25. **Fetch Google Cloud Projects** - Select this option to fetch Google Cloud Projects and parse them as Account/Tenants.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Connect Axonius to Google Cloud Platform

To connect Axonius to Google Cloud Platform you need to:

1. Enable cloud APIs
2. Create a service account and grant permissions to that service account

## 1. Enable Cloud APIs

1. Navigate to the [Google Cloud Console](https://console.cloud.google.com/) and select the project that you want Axonius to connect to.

2. Navigate to **APIs & Services `>`  Dashboard**.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(460\).png)

3. Axonius requires the following APIs to be enabled:

| Enabled API Name                         | Required / Optional | Used for                                                                                                                                                                                                                                         |
| ---------------------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Compute Engine API                       | Required            | The adapter to fetch assets data from Google Cloud Platform.                                                                                                                                                                                     |
| Cloud Resource Manager API               | Required            | The adapter to fetch assets data from Google Cloud Platform.                                                                                                                                                                                     |
| Container Artifact API                   | Required            | `https://container.googleapis.com`                                                                                                                                                                                                               |
| Identity and Access Management (IAM) API | Required            | `https://iam.googleapis.com`                                                                                                                                                                                                                     |
| Security Command Center API              | Required            | `https://securitycenter.googleapis.com`                                                                                                                                                                                                          |
| Google Cloud Storage JSON API            | Optional            | **[Adapter advanced settings:](#advanced-settings)**  **Fetch Google Cloud Storage buckets** - Fetch all Google Cloud Storage buckets. **Fetch Object metadata in Google Cloud Storage buckets** - Fetch Object metadata in GCP Storage buckets. |
| Cloud SQL Admin API                      | Optional            | **[Adapter advanced settings:](#advanced-settings)**     **Fetch Google Cloud SQL database instances** - Fetch all Google Cloud SQL instances.                                                                                                   |

For example, in the screenshot below you can see that since the **Cloud Resource Manager API** doesn't appear in the list, it isn't enabled and needs to be enabled.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(461\).png)

To enable an API, click **Enable APIs and Services** at the top of the page.

4. Search for the API you want to enable and select it. For example: **Cloud Resource Manager API**
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(462\).png)

5. Click **Enable**.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(463\).png)

## 2. Create a Service Account and Grant Permissions to that Service Account

1. Navigate to the [Google Cloud Console](https://console.cloud.google.com/) and select the project that you want Axonius to connect to.

2. Select **IAM & admin** `>`  **Service accounts**.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(115\).png) 

3. Click **Create a Service Account**.

<Image alt="GCPService1.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/GCPService1(1).png" />

4. Provide a name and description for the service account, then click **Create**. If you already clicked **Done**, skip to Step 8.

<Image alt="GCPService2.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/GCPService2(1).png" />

5. In the **Grant this service account access to a project** section, give the service account the roles listed below, as well as the "Security Reviewer" role.

| Role Name                | Required / Optional | Used for                                                                                                                                                                                                                                            |
| ------------------------ | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compute Viewer           | Required            | Grants read-only access to Axonius to fetch assets.                                                                                                                                                                                                 |
| Kubernetes Engine Viewer | Required            | Grants read-only access to Axonius to fetch assets.                                                                                                                                                                                                 |
| Storage Object Viewer    | Optional            | **[Adapter advanced settings:](#advanced-settings)** • **Fetch Google Cloud Storage buckets** - Fetch all Google Cloud Storage buckets.•  **Fetch Object metadata in Google Cloud Storage buckets** - Fetch Object metadata in GCP Storage buckets. |
| Cloud SQL Viewer         | Optional            | **[Adapter advanced settings:](#advanced-settings)**  •  **Fetch Google Cloud SQL database instances** - Fetch all Google Cloud SQL instances.                                                                                                      |
| IAM: Role Viewer         | Optional            | **[Adapter advanced settings:](#advanced-settings)**•  **Fetch IAM permissions for users** - Fetch IAM permissions and associate those to the users roles.                                                                                          |
| Security Reviewer        | Required            | Provides permissions to list all resources and allow policies on them.                                                                                                                                                                              |

<Image alt="GCPService3.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/GCPService3.png" />

6. Skip the **Grant users access to this service account** step.
7. Click **Done**.
8. To modify, or review the permissions granted to this service account in any project or at the organization level, go to IAM, find the service account you've created and click **Edit Permissions**.

<Image alt="GCPService4.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/GCPService4.png" />

<Image alt="GCPService5.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/GCPService5.png" />

<Image alt="GCPSErvice6.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/GCPSErvice6.png" />

9. In the Service Account just created, go to **Keys**

10. Click **Add key** and then **Create**.
    ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(118\).png)

11. Your JSON key is subsequently downloaded. Finish creating the account and go back to the Service Accounts page. Copy the email address of the new service account.

12. In the top part of the page, select the organization resource, and go to **IAM & Admin - IAM**.
    1. Click **Add** and use the service account email to add the new service account as a new member of the organization.
    2. Click **+ Add Another role** to add the following roles to added member:

| Role Name                                                                                                           | Required / Optional | Used for                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------- | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compute Viewer                                                                                                      | Required            | Grants read-only access to Axonius to fetch assets.                                                                                                                                                                                                                                                                    |
| Kubernetes Engine Viewer                                                                                            | Required            | Grants read-only access to Axonius to fetch assets.                                                                                                                                                                                                                                                                    |
| Storage Object Viewer                                                                                               | Optional            | **[Adapter advanced settings:](#advanced-settings)** •  **Fetch Google Cloud Storage buckets** - Fetch all Google Cloud Storage buckets. •  **Fetch Object metadata in Google Cloud Storage buckets** - Fetch Object metadata in GCP Storage buckets.                                                                  |
| Cloud SQL Viewer                                                                                                    | Optional            | **[Adapter advanced settings:](#advanced-settings)**  • **Fetch Google Cloud SQL database instances** - Fetch all Google Cloud SQL instances.                                                                                                                                                                          |
| IAM: Role Viewer                                                                                                    | Optional            | **[Adapter advanced settings:](#advanced-settings)**• **Fetch IAM permissions for users** - Fetch IAM permissions and associate those to the users roles.                                                                                                                                                              |
| • Security Center Findings Viewer role• Security Center Assets Viewer role(Or alternatively, Security Center Admin) | Optional            | **[Adapter advanced settings:](#advanced-settings)**• **Security Command Center organizations** - Fetch Security Command Center device assets and their associated vulnerabilities from a specified list of organizations (NOTE: Those organization-level roles are required for each of the specified organizations.) |

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1233).png" />

<Callout icon="📘" theme="info">
  Note

  Additional permissions are required for GCP Enforcement Actions.
</Callout>

12. Click **Save**.
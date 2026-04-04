# Source: https://docs.aporia.com/data-sources/mssql.md

# Microsoft SQL Server

This guide describes how to connect Aporia to an MSSQL data source in order to monitor your ML Model in production.&#x20;

We will assume that your model inputs, outputs and optionally delayed actuals can be queried with SQL. This data source may also be used to connect to your model's training set to be used as a baseline for model monitoring.

### Access MSSQL using user/password authentication

In order to provide access to MSSQL, create a read-only user for Aporia in MSSQL.

Please use the SQL snippet below to create the user for Aporia. Before using the snippet, you will need to populate the following:

* `<user_name>`: The name of the user you want to create
* `<password>`: Strong password to be used by the user

```sql
CREATE USER <user_name> WITH PASSWORD '<password>';
ALTER ROLE db_datareader ADD MEMBER <user_name>;
```

### Access MSSQL using Azure AD authentication

{% hint style="info" %}
This authentication method is currently supported for databricks deployments only. Need it for other deployment type? Let us know!
{% endhint %}

#### Step 1: Create a new application for Aporia access in your Azure Active Directory

1. Go the Azure Active Directory portal and login
2. Click on **+ Add** and choose **App registration**<br>

   <figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FAh7RKoG9XRtKec5XV4T4%2Fimage.png?alt=media&#x26;token=288b32c5-8309-4741-a1c8-4e9a48d25566" alt=""><figcaption></figcaption></figure>
3. Insert a display name for the Aporia app and click on **Register**
4. Create a new secret for the newly created application

   <figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FYJRd5VigU6M7ckRSBqO0%2Fimage.png?alt=media&#x26;token=64c714fd-ddc3-4d19-9ad1-ed3146933d70" alt=""><figcaption><p>Click on "Add a certificate or secret"</p></figcaption></figure>

   <figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FACRydCfWIRuu5yVtTyhE%2Fimage.png?alt=media&#x26;token=9b3e2c2e-ab68-4619-89c3-6e0cb29db799" alt=""><figcaption><p>Click on "+ New client secret"</p></figcaption></figure>

   <figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FVCtiBTfku2K7LEud3knm%2Fimage.png?alt=media&#x26;token=759a6cdf-35ae-4b69-9e23-739ebb338177" alt=""><figcaption><p>Save the newly created secret for later</p></figcaption></figure>

#### Step 2: Create corresponding secrets in your databricks account

In order to enable authentication using Azure AD, create the following secrets in the same databricks account where Aporia is deployed:

* `aporia-client-secret` - The application secret value you created in the previous step
* `aporia-client-id` - Client ID of the application created in the previous step
* `aporia-tenant-id` - Tenant ID of the application created in the previous step

<figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FfYHhJYgiOAme9WzOD4A8%2Fimage.png?alt=media&#x26;token=4f4f0c7b-c458-4aff-af47-3ed72c31ffbd" alt=""><figcaption><p>Client ID &#x26; Tenant ID can be found in the application page</p></figcaption></figure>

#### Step 3: Create a read-only user for MSSQL access

In order to provide access to MSSQL, create a read-only user for Aporia in MSSQL.

Please use the SQL snippet below to create the user for Aporia. Before using the snippet, you will need to populate the following:

* `<application_name>`: The name of the application you have created in the previous step

```sql
CREATE USER <application_name> FROM EXTERNAL PROVIDER;
ALTER ROLE db_datareader ADD MEMBER <application_name>;
```

{% hint style="info" %}
Make sure that the Aporia data plane IP can access your Microsoft SQL Server
{% endhint %}

### Create a MSSQL data source in Aporia

1. Go to [Aporia platform](https://platform.aporia.com/) and login to your account.
2. Go to **Integrations** page and click on the **Data Connectors** tab
3. Scroll to **Connect New Data Source** section
4. Click **Connect** on the MSSQL card and follow the instructions
   1. Note that the provided URL should be in the following format `jdbc:mssqlsql://<SERVER_HOSTNAME>`.

Bravo! :clap: now you can use the data source you've created across all your models in Aporia.

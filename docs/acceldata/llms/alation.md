# Source: https://docs.acceldata.io/documentation/alation.md

# Alation

Integrate your Alation data catalog with the ADOC platform to display data reliability scores directly in Alation. This integration lets you monitor data quality without switching tools, saving time and reducing errors for data-driven decisions.

## Prerequisites

Ensure the following requirements are met before you connect Alation as a data source:

- You need a working Alation instance with a valid URL (e.g., `https://your-alation-instance.com`). This is your Alation catalog’s web address.
- Your account must have Catalog Admin permissions to manage data assets in Alation. Refer [Access, Roles, Permissions](https://docs.alation.com/en/latest/welcome/CatalogBasics/AccessRolesPermissions.html).
- Alation’s REST API must be enabled in your instance:
- Ensure the Alation user has REST API access permissions. Use a valid username and password..
- Generate a Client ID and Secret under your Alation Service Account. Enable **read access** to the **catalog** and **lineage** scopes.
For more information, [How to Authenticate into Alation APIs](https://developer.alation.com/dev/docs/authentication-into-alation-apis).
- The data assets you want to monitor must be cataloged in Alation and registered in ADOC. This ensures ADOC’s policy scores and metadata display correctly in Alation.

## Add Alation as a Data Source in ADOC

Follow these steps to set up Alation as a data source in ADOC.

### Step 1: Start Setup

1. Select **Register** from the left main menu.
2. Select **Add Data Source**.
3. Select **Alation** from the list of data sources.
4. On the **Basic Details** page:
    1. Enter a unique name for this data source.
    2. Optionally, add a brief description to clarify its purpose.

5. Select **Next** to proceed.

### Step 2: Add Connection Details

| Field | Description | 
| ---- | ---- | 
| Base URL | Enter your Alation URL (e.g., [https://alation.yourdomain.com](https://alation.yourdomain.com)). | 
| Username / Password | Enter your Alation login credentials. | 
| OAuth settings (Optional) | If using OAuth, provide the Client ID, Secret, and token duration (in seconds). | 


1. Select **Test Connection**. If successful, you’ll see “Connected.” If the connection fails, check for common issues such as:
    - Incorrect or expired API token. Refer to the [Alation ](https://developer.alation.com/dev/docs/authentication-into-alation-apis#regenerate-an-api-access-token-via-the-ui)documentation to regenerate an API token.
    - Invalid Alation API URL
    - Invalid credential format

2. Select **Next** to proceed.

### Step 3:  Setup Observability

Customize how ADOC’s data reliability features appear in Alation.

1. **Enable Trust Flag**: Display the asset’s status in Alation:
    - **Green**: Endorsed
    - **Yellow**: Warning
    - **Red**: Deprecated

2. **Allow Acceldata to deprecate assets**: Permit ADOC to mark assets as deprecated in Alation. If disabled, deprecated assets will appear with a warning instead.
3. **Set thresholds**: Define score thresholds that trigger warning or deprecated flags.
4. **Enable Acceldata Data Reliability Summary on Alation Overview**: Display ADOC’s overall and policy-level scores in the asset’s Overview tab in Alation. Users can select a link to view the asset in ADOC.
5. **Enable Acceldata Policies in Alation Health**: Display policy names, scores, and execution logs in Alation’s Health tab.
6. **Map data sources:**
    - Select the Alation data source from the list.
    - Match it with the corresponding data source in ADOC.

7. Click **Submit**.

---

## What's Next

Once integrated, ADOC’s policy executions will automatically update the following in Alation for each mapped asset:

- **Quality Scores**: Reflect the asset’s data reliability.
- **Asset Health**: Show the asset’s status (e.g., endorsed, warning, deprecated).
- **Policy Executions**: Log details of ADOC’s data quality checks.
- **Direct Link to ADOC**: Access the asset’s details in ADOC with one click.

These updates appear in Alation’s interface, streamlining data monitoring and improving team collaboration.

### Optional: Add ADOC Summary Field in Alation

To display ADOC’s Data Reliability Summary in Alation’s interface:

1. In Alation, navigate to the **Custom Template** tab.
2. Select your asset type (e.g., table, schema).
3. Find and select **A** **Acceldata Data Quality Summary**.
4. Select **Insert** to add the field.
5. The summary will appear in the **Overview** tab of each asset.

If policy logging is enabled, detailed policy execution logs will appear in the **Health** tab.

For more details, refer to the steps in [Alation Help Center](https://docs.alationdata.com/en/latest/steward/TemplatesAndCustomFields/CatalogTemplates.html#finding-templates-in-the-catalog).
# Source: https://docs.acceldata.io/documentation/azure-data-factory.md

# Azure Data Factory

Azure Data Factory (ADF) serves as Azure's cloud-based ETL (Extract, Transform, Load) service, designed to facilitate scalable and serverless data integration and transformation. It provides a user-friendly interface devoid of coding requirements, ensuring straightforward configuration, along with comprehensive monitoring and management capabilities within a single interface.

In addition to supporting ADF's computational capabilities, ADOC now supports its integration for Data Reliability. This interface allows ADOC to take advantage of ADF's data cleansing and standardization functionalities, inputting standardized and cleansed files directly into ADOC for further data quality analysis.

## Configuring Permissions for Azure Data Factory Integration

To set up an Azure Data Factory (ADF) data source on the ADOC platform, you need to grant certain permissions. These permissions allow us to read ADF metadata such as pipelines, activities, and other components. You can authenticate using one of two methods:

- **Azure Service Principal**
- **Azure Managed Identity**

The following steps will guide you through granting the necessary permissions using either method.

### Granting Permissions at the Azure Subscription Level

You can provide access to a Service Principal or Managed Identity in several ways:

1. **Through Azure Managed Identities**
2. **Through Azure Subscriptions**
3. **Through Azure Data Factory**

Azure Managed Identities
**1. Navigate to Azure Managed Identities:**

1.1. Go to the **Azure Portal** and select your **Managed Identity**.

1.2. Click on **Azure Role Assignments**.

**2. Select the Scope:**

2.1. Choose the scope for the role assignment:

- **Azure Subscription**
- **Azure Resource Group** within a subscription

**3. Add a Role Assignment:**

3.1. Click on **Add Role Assignment**.

3.2. Select the **Reader** role for ADF integration.

3.3. Choose the appropriate scope (Subscription or Resource Group).

Using Azure Subscriptions
**1. Navigate to Azure Subscriptions:**

- In the **Azure Portal**, select your **Subscription**.

**2. Access Control:**

- Click on Access Control (IAM).

**3. Add a Role Assignment:**

3.1. Click on **Add** and select **Add Role Assignment**.

3.2. Choose the **Reader** role.

3.3. Select the members (Service Principals or Managed Identities) you wish to assign the role to.

3.4. Review and save the role assignment.

Using Azure Data Factory
**1. Navigate to Your ADF Instance:**

- In the **Azure Portal**, select your **Azure Data Factory** instance.

**2. Access Control:**

- Click on **Access Control (IAM).**

**3. Add a Role Assignment:**

3.1. Click on **Add** and choose **Add Role Assignment**.

3.2. Select the **Reader** role.

3.3. Choose the members (Service Principals or Managed Identities) to assign the role to.

3.4. Save the role assignment.



---

## Data Plane Setup for Managed Identity (MSI)

If you are using Azure Managed Identities to authenticate with Azure services like ADF, Azure Data Lake Storage, or Azure SQL, you must take these extra steps to set up the data plane.

### Step 1: Map Managed Identity to Kubernetes Service account.

**1. Navigate to Federated Credentials:**

- In your **Managed Identity** settings, select **Federated Credentials**.

**2. Add Credentials**

- Click on **Add Credentials**.
- For each Kubernetes Service account listed below, create a new credentials:
    - `analysis-service`
    - `analysis-standalone-service`
    - `spark-scheduler`
    - `sparkoperator`
    - `torch-monitors`

### Step 2: Annotate Kubernetes Service Accounts

For each of the service accounts mentioned:

**1. Add Annotation:**

- Include the following annotation with the client ID of your Managed Identity:

```yaml
azure.workload.identity/client-id: <client id of the managed identity>
```



### Step 3:  Label Deployments in Kubernetes

In the deployment YAML files for each of the service, add the following label, under both the `metadata` and `template` sections:

```yaml
azure.workload.identity/use: "true"
```



**Service to Update:**

- `analysis-service`
- `analysis-standalone-service`
- `spark-scheduler`
- `sparkoperator`
- `torch-monitors`

By completing these steps, you'll enable your data plane to use Azure Managed Identities when connecting to Azure Data Factory and other Azure resources.

> Ensure you have the necessary administrative privileges to perform these actions. If you encounter any issues, consult your Azure administrator or refer to the official Azure documentation for more detailed guidance.

---

## Configuring an Azure Data Factory Data Source in ADOC

### Step 1: Start Setup

1. **Access Data Sources**: In the ADOC platform, click on **Register** from the left navigation menu to open the data sources window.
2. **Add a New Data Source**: Click the **Add Data Source** button.
3. **Select Azure Data Factory**: Choose **Azure Data Factory** from the list of available data source types.

![](https://uploads.developerhub.io/prod/Yoq2/hsxi889k0x0wrkw6lwpierephgckh9zsfg9ccdfu4afk6cnn1tc2bjpfyzm4ktkd.png)

### Step 2: Enter Data Source Details

1. **Provide Basic Information**:
    - **Name**: Enter a meaningful name for your data source.
    - **Description**: Optionally, add a description for future reference.

2. **Enable Observability Options**:
    - **Compute Observability**: Toggle this on if you want to monitor compute resources.
    - **Data Reliability**: Toggle this on to enable pipeline observability.
        - **Data Plane Selection**: If Data Reliability is enabled, select the appropriate **Data Plane**.

3. **Proceed to Connection Details**:
    - Click **Next** to move to the connection details page.

### Step 3: Add Connection Details

You can authenticate using one of two methods:

#### Option 1: Service Principal

1. **Select Authentication Method**:
    - Choose **Service Principal**.

2. **Enter Credentials**:
    - **Tenant ID**: Input your Azure Active Directory tenant ID.
    - **Client ID**: Enter the application (client) ID of your Service Principal.
    - **Client Secret**: Provide the client secret value.
    - **Subscription ID**: Input the Azure subscription ID where your Data Factories are located.

#### Option 2: Azure Managed Identity (MSI)

1. **Select Authentication Method**:
    - Choose **Managed Identities**.

2. **Enter Subscription ID**:
    - **Subscription ID**: Provide the Azure subscription ID where your Data Factories are located.

### Step 4: Test the Connection

1. **Initiate Connection Test**:
    - Click **Test Connection** to verify that the provided credentials can access your Azure Data Factory.

2. **Review Results**:
    - If the test is successful, proceed to the next step.
    - If the test fails, double-check your credentials and ensure the correct permissions are in place.

### Step 5: Setup Observability

Following a successful connection test, you get directed to the data source configuration page.

1. **Set Up Observability Preferences**:
    - **Compute Observability**:
        - **Polling Frequency**: Determine how frequently ADOC should retrieve compute data.

    - **Data Reliability / Pipeline Observability**:
        - **Select Resource Groups**: Select the relevant resource groups from the dropdown.
        - **Select Data Factories**: Select the specific Data Factories you want to monitor.
        - **Crawler Scheduling**: Configure if needed.
        - **Schema Drift Monitoring**: Enable and set up if applicable.

2. **Review and Confirm Settings**:
    - Ensure all selections align with your monitoring needs.

### Step 6: Finalize the Integration

1. **Save the Data Source**: Click **Submit** or **Save** to complete the integration process.
2. **Data Fetching Schedule**: Data will be fetched or crawled according to the configured schedule, typically every 24 hours.

---

## Pipeline Observability Features

Once your ADF data source is registered, you gain access to enhanced pipeline observability features:

1. **Automatic Detection**:
    - **Pipelines and Runs**: All pipelines, their runs, and associated metadata are automatically detected. All pipeline capabilities within ADOC are applicable to ADF pipelines.

2. **Enhanced Filtering Options**:
    - **Source Type Filter**: On the **Pipeline Listing** page, you can filter pipelines based on the ETL orchestrator (e.g., ADF, other sources).
    - **Data Factory Filter**:
        - For ADF sources, you can filter pipelines by **Data Factory** or specific **ADF Data Sources**.
        - This helps in narrowing down the pipelines for better analysis and monitoring.

![](https://uploads.developerhub.io/prod/Yoq2/mmfkh7g2e0ugvbwbr0sqtxmri16mr5uxzcjkjs4fhwj7ybg1q2pvfjiok4x4u7n6.png)

Also see, [Pipeline](/documentation/pipeline-home#filters).

---

## Role(s) Required to Fetch ADF (Cost + Operations) Data in Azure

You can assign roles in three ways to make ADF integration work.

| Role Assignment Method | Descriptions | 
| ---- | ---- | 
| Assign **Reader** role at resource group level | Provides read access to all the resources (including cost) present in that resource group. | 
| Assign **Cost Management Reader** and **Data Factory Contributor** roles at resource group level | Provides read access to cost data of all the resources and read access to all the data factories present in the resource group. | 
| Assign **Cost Management Reader** role at resource group level and **Reader** role at data factory level | Provides read access to cost data of all the resources in the resource group and read access to the Data Factory. | 


For more information, see the [Microsoft Azure](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/custom-overview) documentation.
# Source: https://infisical.com/docs/integrations/app-connections/gcp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# GCP Connection

> Learn how to configure a GCP Connection for Infisical.

Infisical supports [service account impersonation](https://cloud.google.com/iam/docs/service-account-impersonation) to connect with your GCP projects.

<Accordion title="Self-Hosted Instance">
  Using the GCP integration on a self-hosted instance of Infisical requires configuring a service account on GCP and
  configuring your instance to use it.

  <Steps>
    <Step title="Enable the IAM Service Account Credentials API">
      Enable the IAM Service Account Credentials API for the project containing the service account that will be impersonated. You can do this from the Google Cloud Console or via the command line.

            <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/gcp/service-account-credentials-api.png" alt="Service Account API" />

      To enable via command line, run the following command, replacing `projectId` with your GCP project ID:

      ```bash  theme={"dark"}
      gcloud services enable iamcredentials.googleapis.com --project=projectId
      ```

      Verify the API is enabled by running:

      ```bash  theme={"dark"}
      gcloud services list --enabled --project=projectId | grep iamcredentials
      ```
    </Step>

    <Step title="Navigate to IAM & Admin > Service Accounts in Google Cloud Console">
            <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/gcp/service-account-overview.png" alt="Service Account IAM Page" />
    </Step>

    <Step title="Create a Service Account">
      Create a new service account that will be used to impersonate other GCP service accounts for your app connections.
      <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/gcp/create-instance-service-account.png" alt="Create Service Account Page" />

      Press "DONE" after creating the service account.
    </Step>

    <Step title="Generate Service Account Key">
      Download the JSON key file for your service account. This will be used to authenticate your instance with GCP.
      <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/gcp/create-service-account-credential.png" alt="Service Account Credential Page" />
    </Step>

    <Step title="Configure Your Instance">
      1. Copy the entire contents of the downloaded JSON key file.
      2. Set it as a string value for the `INF_APP_CONNECTION_GCP_SERVICE_ACCOUNT_CREDENTIAL` environment variable.
      3. Restart your Infisical instance to apply the changes.
      4. You can now use GCP integration with service account impersonation.
    </Step>
  </Steps>
</Accordion>

## Configure Service Account for Infisical

<Steps>
  <Step title="Navigate to IAM & Admin > Service Accounts in Google Cloud Console">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/gcp/service-account-overview.png" alt="Service Account Page" />
  </Step>

  <Step title="Create Service Account">
    Create a new service account with an ID that follows this requirement:

    Your service account ID must end with the first two sections of your Infisical organization ID.

    Example:

    * Infisical organization ID: `df92581a-0fe9-42b5-b526-0a1e88ec8085`
    * Required service account ID suffix: `df92581a-0fe9`

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/gcp/create-service-account.png" alt="Create Service Account" />
  </Step>

  <Step title="Configure Service Account Permissions">
    <Tabs>
      <Tab title="Secret Sync">
        Add the required permissions for secret syncs:
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/gcp/service-account-secret-sync-permission.png" alt="Assign Service Account Permission" />
      </Tab>
    </Tabs>

    After configuring the appropriate roles, press "DONE".
  </Step>

  <Step title="Enable Service Account Impersonation">
    To enable service account impersonation, you'll need to grant the **Service Account Token Creator** role to the Infisical instance's service account. This configuration allows Infisical to securely impersonate the new service account.

    * Navigate to the IAM & Admin > Service Accounts section in your Google Cloud Console
    * Select the newly created service account
    * Click on the "PERMISSIONS" tab
    * Click "Grant Access" to add a new principal

    If you're using Infisical Cloud US, use the following service account: [infisical-us@infisical-us.iam.gserviceaccount.com](mailto:infisical-us@infisical-us.iam.gserviceaccount.com)

    If you're using Infisical Cloud EU, use the following service account: [infisical-eu@infisical-eu.iam.gserviceaccount.com](mailto:infisical-eu@infisical-eu.iam.gserviceaccount.com)

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/gcp/service-account-grant-access.png" alt="Service Account Page" />
  </Step>
</Steps>

## Setup GCP Connection in Infisical

<Steps>
  <Step title="Navigate to App Connections">
    Navigate to the **Integrations** tab in the desired project, then select **App Connections**. <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/general/add-connection.png" alt="App Connections
    Tab" />
  </Step>

  <Step title="Add Connection">
    Select the **GCP Connection** option from the connection options modal.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/gcp/select-gcp-connection.png" alt="Select GCP
    Connection" />
  </Step>

  <Step title="Authorize Connection">
    Select the **Service Account Impersonation** method and click **Connect to
    GCP**. <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/gcp/create-gcp-impersonation-method.png" alt="Connect via GCP
    impersonation" />
  </Step>

  <Step title="Connection Created">
    Your **GCP Connection** is now available for use. <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/gcp/gcp-app-impersonation-connection.png" alt="Impersonation GCP
    Connection" />
  </Step>
</Steps>

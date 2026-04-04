# Source: https://infisical.com/docs/documentation/platform/kms-configuration/gcp-kms.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# GCP Key Management Service

> Learn how to manage encryption using GCP KMS

To enhance the security of your Infisical projects, you can now encrypt your secrets using an external Key Management Service (KMS).
When external KMS is configured for your project, all encryption and decryption operations will be handled by the chosen KMS.
This guide will walk you through the steps needed to configure external KMS support with Google Cloud KMS.

## Prerequisites

Before you begin, you'll first need to set up a GCP Service Account, add a KMS key and set the required permissions.

<Steps>
  <Step title="Create a GCP Service Account">
    1. Navigate to the [Create Service Account](https://console.cloud.google.com/iam-admin/serviceaccounts/create) page in your GCP Console.
       <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/kms/gcp/service-account-form.png" alt="GCP Service Account Creation" />

    2. Give the service account a suitable **name** and **description**. Then click **Create and Continue**.

    3. Under **Grant this service account access to project**, click **Select a role** and select the
       **Cloud KMS Viewer** and **Cloud KMS CryptoKey Encrypter/Decrypter**\* roles, then click **Continue**.
       <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/kms/gcp/service-account-permissions.png" alt="GCP Service Account Permissions" />

    4. You can skip the **Grant users access to this service account** options.

    5. Click Done.

    6. You should see the service account in the list of service accounts. Click it to view the service account details.

    7. Select the **Keys** tab, click **Add Key**, select **Create new key**, select **JSON** as the key type, then click **Create**.

    8. You will be prompted to download a JSON file that we will need later on.

    <Info>
      Remember to keep the JSON file in a secure location. It will be used to authenticate your GCP service account.

      Once you have successfully set up GCP KMS with Infisical, you should permanently delete the JSON file.
    </Info>
  </Step>

  <Step title="Add a GCP KMS Key">
    1. Navigate to the [KMS](https://console.cloud.google.com/security/kms) page in your GCP Console.

    <Info>
      If you have not used GCP KMS before, you will be redirected to the **Cloud Key Management Service (KMS) API** page.

      Click **Enable** to enable the KMS API, then continue the steps below.

      It may take a few minutes for the API to be enabled and KMS section of the Cloud Console to become viewable.
    </Info>

    2. In the KMS section, click **Create Key Ring**.
       <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/kms/gcp/keyring-create.png" alt="GCP Create Key Ring" />

    3. Give the key ring a **Name** and select a **Region**, then click **Create**.

    <Info>
      We don't currently support multi-region key rings.
    </Info>

    4. On the "Create Key" page, give the key a **Name** and set the **Protection Level** based on your requirements (or use default *Software*), then click **Continue**.

    5. Under **Key Material**, select **Generated Key**, then click **Continue**.

    6. Under **Purpose**, select **Symmetric encrypt/decrypt**, then click **Continue**.

    7. For **Key Rotation Period**, select **Never (manual rotation)**, then click **Continue** followed by **Create**.

    8. You should see the key in the list of keys. We're now ready to set it up in Infisical.
  </Step>
</Steps>

## Setup GCP KMS in the Organization Settings

Next, you will need to follow the steps listed below to add GCP KMS for your organization.

<Steps>
  <Step title="Navigate to the organization settings and select the 'Encryption' tab.">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/kms/encryption-org-settings.png" alt="Open encryption org settings" />
  </Step>

  <Step title="Click on the 'Add' button">
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/kms/encryption-org-settings-add.png" alt="Add encryption org settings" />
    Click the 'Add' button to begin adding a new external KMS.
  </Step>

  <Step title="Select 'GCP KMS'">
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/kms/encryption-modal-provider-select.png" alt="Select Encryption Provider" />
    Choose 'GCP KMS' from the list of encryption providers.
  </Step>

  <Step title="Provide the inputs for GCP KMS">
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/kms/gcp/gcp-add-modal-filled.png" alt="GCP Create KMS Modal" />
    Selecting GCP as the provider will require you input the following fields.

    <ParamField path="Alias" type="string" required>
      Name for referencing the GCP KMS key within the organization.
    </ParamField>

    <ParamField path="Description" type="string">
      Short description of the GCP KMS key.
    </ParamField>

    <ParamField path="GCP Region" type="dropdown" required>
      The GCP region where the GCP KMS key ring is located.
    </ParamField>

    <ParamField path="Service Account Credential JSON" type="file" required>
      Upload the JSON file you downloaded earlier when creating the GCP service account.
    </ParamField>

    <ParamField path="GCP Key Name" type="dropdown" required>
      This field will be populated with the list of GCP KMS keys in the selected region. Select the key you created earlier.
    </ParamField>
  </Step>

  <Step title="Click Save">
    Save your configuration to apply the settings.
  </Step>
</Steps>

You now have a GCP KMS Key configured at the organization level. You can assign these GCP KMS keys to existing Infisical projects by visiting the 'Project Settings' page.

## Assign GCP KMS Key to an Existing Project

To assign the GCP KMS key you added to your organization, follow the steps below.

<Steps>
  <Step title="Open Project Settings and select to the Encryption Tab">
        <img
          src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/kms/gcp/project-settings.png"
          alt="Open encryption project
    settings"
        />
  </Step>

  <Step title="Under the Key Management section, select your newly added GCP KMS key from the dropdown">
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/kms/gcp/select-gcp-kms-in-project.png" alt="Select encryption project
    settings" />
    Choose the GCP KMS key you configured earlier.
  </Step>

  <Step title="Click Save">
    Once you have selected the KMS of choice, click save.
  </Step>
</Steps>

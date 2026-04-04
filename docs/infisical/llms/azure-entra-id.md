# Source: https://infisical.com/docs/documentation/platform/dynamic-secrets/azure-entra-id.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Azure Entra Id

> Learn how to dynamically generate Azure Entra Id user credentials.

The Infisical Azure Entra Id dynamic secret allows you to generate Azure Entra Id credentials on demand based on configured role.

## Prerequisites

<Steps>
  <Step>
    Login to [Microsoft Entra ID](https://entra.microsoft.com/)
  </Step>

  <Step>
    Go to Overview, Copy and store `Tenant Id`
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-ad-tenant-id.png" alt="Copy Tenant Id" />
  </Step>

  <Step>
    Go to Applications > App registrations. Click on New Registration.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-ad-new-registration.png" alt="Copy Tenant Id" />
  </Step>

  <Step>
    Enter an application name. Click Register.
  </Step>

  <Step>
    Copy and store `Application Id`.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-ad-copy-app-id.png" alt="Copy Application Id" />
  </Step>

  <Step>
    Go to Clients and Secrets. Click on New Client Secret.
  </Step>

  <Step>
    Enter a description, select expiry and click Add.
  </Step>

  <Step>
    Copy and store `Client Secret` value.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-ad-add-client-secret.png" alt="Copy client Secret" />
  </Step>

  <Step>
    Go to API Permissions. Click on Add a permission.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-ad-add-permission.png" alt="Click add a permission" />
  </Step>

  <Step>
    Click on Microsoft Graph.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-ad-select-graph.png" alt="Click Microsoft Graph" />
  </Step>

  <Step>
    Click on Application Permissions. Search and select `User.ReadWrite.All` and click Add permissions.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-ad-select-perms.png" alt="Add User.Read.All" />
  </Step>

  <Step>
    Click on Grant admin consent for app. Click yes to confirm.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-ad-admin-consent.png" alt="Grant admin consent" />
  </Step>

  <Step>
    Go to Dashboard. Click on show more.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-ad-show-more.png" alt="Show more" />
  </Step>

  <Step>
    Click on Roles & admins. Search for User Administrator and click on it.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-ad-user-admin.png" alt="User Administrator" />
  </Step>

  <Step>
    Click on Add assignments. Search for the application name you created and select it. Click on Add.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-ad-add-assignments.png" alt="Add assignments" />
  </Step>
</Steps>

## Set up Dynamic Secrets with Azure Entra ID

<Steps>
  <Step title="Open Secret Overview Dashboard">
    Open the Secret Overview dashboard and select the environment in which you would like to add a dynamic secret.
  </Step>

  <Step title="Click on the 'Add Dynamic Secret' button">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/add-dynamic-secret-button.png" alt="Add Dynamic Secret Button" />
  </Step>

  <Step title="Select 'Azure Entra ID'">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-ad-modal.png" alt="Dynamic Secret Modal" />
  </Step>

  <Step title="Provide the inputs for dynamic secret parameters">
    <ParamField path="Secret Prefix" type="string" required>
      Prefix for the secrets to be created
    </ParamField>

    <ParamField path="Default TTL" type="string" required>
      Default time-to-live for a generated secret (it is possible to modify this value after a secret is generated)
    </ParamField>

    <ParamField path="Max TTL" type="string" required>
      Maximum time-to-live for a generated secret.
    </ParamField>

    <ParamField path="Tenant ID" type="string" required>
      The Tenant ID of your Azure Entra ID account.
    </ParamField>

    <ParamField path="Application ID" type="string" required>
      The Application ID of the application you created in Azure Entra ID.
    </ParamField>

    <ParamField path="Client Secret" type="string" required>
      The Client Secret of the application you created in Azure Entra ID.
    </ParamField>

    <ParamField path="Users" type="selection" required>
      Multi select list of users to generate secrets for.
    </ParamField>
  </Step>

  <Step title="Click `Submit`">
    After submitting the form, you will see a dynamic secret for each user created in the dashboard.
  </Step>

  <Step title="Generate dynamic secrets">
    Once you've successfully configured the dynamic secret, you're ready to generate on-demand credentials.
    To do this, simply click on the 'Generate' button which appears when hovering over the dynamic secret item.
    Alternatively, you can initiate the creation of a new lease by selecting 'New Lease' from the dynamic secret lease list section.

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-generate.png" alt="Dynamic Secret" />
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-lease-empty.png" alt="Dynamic Secret" />

    When generating these secrets, it's important to specify a Time-to-Live (TTL) duration. This will dictate how long the credentials are valid for.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/provision-lease.png" alt="Provision Lease" />

    <Tip>
      Ensure that the TTL for the lease falls within the maximum TTL defined when configuring the dynamic secret.
    </Tip>

    Once you click the `Submit` button, a new secret lease will be generated and the credentials from it will be shown to you.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-ad-lease.png" alt="Provision Lease" />
  </Step>
</Steps>

## Audit or Revoke Leases

Once you have created one or more leases, you will be able to access them by clicking on the respective dynamic secret item on the dashboard.
This will allow you to see the expiration time of the lease or delete a lease before its set time to live.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/lease-data.png" alt="Provision Lease" />

## Renew Leases

To extend the life of the generated dynamic secret leases past its initial time to live, simply click on the **Renew** button as illustrated below.
<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-lease-renew.png" alt="Provision Lease" />

<Warning>
  Lease renewals cannot exceed the maximum TTL set when configuring the dynamic secret
</Warning>

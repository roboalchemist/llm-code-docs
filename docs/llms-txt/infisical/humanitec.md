# Source: https://infisical.com/docs/integrations/secret-syncs/humanitec.md

# Source: https://infisical.com/docs/integrations/app-connections/humanitec.md

# Source: https://infisical.com/docs/integrations/secret-syncs/humanitec.md

# Source: https://infisical.com/docs/integrations/app-connections/humanitec.md

# Source: https://infisical.com/docs/integrations/secret-syncs/humanitec.md

# Source: https://infisical.com/docs/integrations/app-connections/humanitec.md

# Source: https://infisical.com/docs/integrations/secret-syncs/humanitec.md

# Source: https://infisical.com/docs/integrations/app-connections/humanitec.md

# Humanitec Connection

> Learn how to configure a Humanitec Connection for Infisical.

Infisical supports connecting to Humanitec using a service user.

## Setup Humanitec Connection in Infisical

<Steps>
  <Step title="Move to Service Users on Humanitec">
    Navigate to the Humanitec **Service Users** tab.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/humanitec/humanitec-service-users.png" alt="Humanitec Service Users Tab" />
  </Step>

  <Step title="Create a Service User">
    Create a new service user. Take into account that the role set here will affect the permissions of the API Token so be sure to set it so the Service User has access permissions to the App you want to integrate to Infisical.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/humanitec/humanitec-create-new-user.png" alt="Humanitec Create New Service User" />
  </Step>

  <Step title="Add API Token for the Service User">
    Add a new API token for the service user.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/humanitec/humanitec-add-api-token.png" alt="Humanitec Add API Token" />
  </Step>

  <Step title="Create the API Token for the Service User">
    Create the API token for the service user.
    This token's permission will be limited to the **Service User** role.

    <Note>
      If you configure an expiry date for your API token you will need to manually rotate to a new token prior to expiration to avoid integration downtime.
    </Note>

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/humanitec/humanitec-create-api-token.png" alt="Humanitec Create API Token" />
  </Step>

  <Step title="Copy the API Token">
    A modal with the API token will be displayed. Save the token in a secure location for later use in the following steps.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/humanitec/humanitec-copy-api-token.png" alt="Humanitec Copy API Token" />
  </Step>

  <Step title="Service User has been successfully created">
    After following the previous steps the Service User has been successfully created, and now should be visible on the Service Users tab.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/humanitec/humanitec-service-account-filled.png" alt="Humanitec Service User Created" />
  </Step>

  <Step title="Add Service User to Application">
    Move to the **Applications** tab and add the Service User to the Application you want to sync with Infisical.
    Clicking on the App Title will open the App details page.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/humanitec/humanitec-applications-tab.png" alt="Humanitec Applications Tab" />
  </Step>

  <Step title="Add new member to this Application">
    Move to the **People** tab and add a new member to this Application. The recently created User Service should be visible on the dropdown shown.
    Make sure to assign at least Developer role as Write permissions are required.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/humanitec/humanitec-add-user.png" alt="Humanitec Add User to Application" />
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/humanitec/humanitec-add-user-options.png" alt="Humanitec Add User Options" />
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/humanitec/humanitec-add-user-role.png" alt="Humanitec Add User Role" />
  </Step>

  <Step title="Connection Created">
    Your **Humanitec Connection** is now available for use.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/humanitec/humanitec-user-added.png" alt="Humanitec Connection Created" />
  </Step>

  <Step title="Navigate to App Connections">
    Navigate to the **App Connections** page in the desired project.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/general/add-connection.png" alt="App Connections Tab" />
  </Step>

  <Step title="Add Connection">
    Select the **Humanitec Connection** option from the connection options modal.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/humanitec/humanitec-app-connection-option.png" alt="Select Humanitec Connection" />
  </Step>

  <Step title="Fill the Humanitec Connection Modal">
    Fill the Humanitec Connection modal, here you will need to provide the User Service API Token generated in the previous step.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/humanitec/humanitec-app-connection-modal.png" alt="Humanitec Connection Modal" />
  </Step>

  <Step title="Connection Created">
    Your **Humanitec Connection** is now available for use.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/humanitec/humanitec-app-connection-created.png" alt="Humanitec Connection Created" />
  </Step>
</Steps>

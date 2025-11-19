# Source: https://infisical.com/docs/integrations/cicd/rundeck.md

# Rundeck

> How to sync secrets from Infisical to Rundeck

Prerequisites:

* Set up and add envars to [Infisical Cloud](https://app.infisical.com)

<Steps>
  <Step title="Authorize Infisical for Rundeck">
    Obtain a User API Token in the Profile settings of Rundeck

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/rundeck/integrations-rundeck-token.png" alt="integrations rundeck token" />

    Navigate to your project's integrations tab in Infisical.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations.png" alt="integrations" />

    Press on the Rundeck tile and input your Rundeck instance Base URL and User API token to grant Infisical access to manage Rundeck keys

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/rundeck/integrations-rundeck-auth.png" alt="integrations rundeck authorization" />
  </Step>

  <Step title="Start integration">
    Select which Infisical environment secrets you want to sync to a Rundeck Key Storage Path and press create integration to start syncing secrets to Rundeck.

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/rundeck/integrations-rundeck-create.png" alt="create integration rundeck" />
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/rundeck/integrations-rundeck.png" alt="integrations rundeck" />
  </Step>
</Steps>

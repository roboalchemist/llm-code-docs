# Source: https://infisical.com/docs/integrations/cloud/hasura-cloud.md

# Hasura Cloud

> How to sync secrets from Infisical to Hasura Cloud

Prerequisites:

* Set up and add envars to [Infisical Cloud](https://app.infisical.com)

<Steps>
  <Step title="Authorize Infisical for Hasura Cloud">
    Obtain a Hasura Cloud Access Token in My Account > Access Tokens

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/hasura-cloud/integrations-hasura-cloud-tokens.png" alt="integrations hasura cloud tokens" />

    Navigate to your project's integrations tab in Infisical.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations.png" alt="integrations" />

    Press on the Hasura Cloud tile and input your Hasura Cloud access token to grant Infisical access to your Hasura Cloud account.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/hasura-cloud/integrations-hasura-cloud-auth.png" alt="integrations hasura cloud authorization" />
  </Step>

  <Step title="Start integration">
    Select which Infisical environment secrets you want to sync to which Hasura Cloud project and press create integration to start syncing secrets to Hasura Cloud.

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/hasura-cloud/integrations-hasura-cloud-create.png" alt="integrations hasura cloud" />
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/hasura-cloud/integrations-hasura-cloud.png" alt="integrations hasura cloud" />
  </Step>
</Steps>

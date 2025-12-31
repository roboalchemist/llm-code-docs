# Source: https://infisical.com/docs/integrations/cloud/qovery.md

# Qovery

> How to sync secrets from Infisical to Qovery

Prerequisites:

* Set up and add envars to [Infisical Cloud](https://app.infisical.com)

<Steps>
  <Step title="Authorize Infisical for Qovery">
    Obtain a Qovery API Token in Settings > API Token.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/qovery/integrations-qovery-token.png" alt="integrations qovery api token" />

    Navigate to your project's integrations tab in Infisical.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations.png" alt="integrations" />

    Press on the Qovery tile and input your Qovery API Token to grant Infisical access to your Qovery account.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/qovery/integrations-qovery-auth.png" alt="integrations qovery authorization" />
  </Step>

  <Step title="Start integration">
    Select which Infisical environment secrets you want to sync to Qovery and press create integration to start syncing secrets.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/qovery/integrations-qovery-create-1.png" alt="integrations qovery create" />

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/qovery/integrations-qovery-create-2.png" alt="integrations qovery create" />

    <Note>
      Infisical supports syncing secrets to various Qovery scopes including applications, jobs, or containers.
    </Note>

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/qovery/integrations-qovery.png" alt="integrations qovery settings" />
  </Step>
</Steps>

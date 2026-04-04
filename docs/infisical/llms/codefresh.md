# Source: https://infisical.com/docs/integrations/cicd/codefresh.md

# Codefresh

> How to sync secrets from Infisical to Codefresh

Prerequisites:

* Set up and add envars to [Infisical Cloud](https://app.infisical.com)

<Steps>
  <Step title="Authorize Infisical for Codefresh">
    Obtain an API key in User Settings > API Keys

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/codefresh/integrations-codefresh-dashboard.png" alt="integrations codefresh dashboard" />
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/codefresh/integrations-codefresh-token.png" alt="integrations codefresh token" />

    Navigate to your project's integrations tab in Infisical.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations.png" alt="integrations" />

    Press on the Codefresh tile and input your Codefresh API key to grant Infisical access to your Codefresh account.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/codefresh/integrations-codefresh-auth.png" alt="integrations codefresh authorization" />
  </Step>

  <Step title="Start integration">
    Select which Infisical environment secrets you want to sync to which Codefresh service and press create integration to start syncing secrets to Codefresh.

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/codefresh/integrations-codefresh-create.png" alt="create integration codefresh" />
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/codefresh/integrations-codefresh.png" alt="integrations codefresh" />
  </Step>
</Steps>

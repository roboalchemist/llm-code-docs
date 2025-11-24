# Source: https://infisical.com/docs/integrations/cicd/travisci.md

# Travis CI

> How to sync secrets from Infisical to Travis CI

Prerequisites:

* Set up and add envars to [Infisical Cloud](https://app.infisical.com)

<Steps>
  <Step title="Authorize Infisical for Travis CI">
    Obtain your API token in User Settings > API authentication > Token

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/travis-ci/integrations-travisci-token.png" alt="integrations travis ci token" />

    Navigate to your project's integrations tab in Infisical.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations.png" alt="integrations" />

    Press on the Travis CI tile and input your Travis CI API token to grant Infisical access to your Travis CI account.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/travis-ci/integrations-travisci-auth.png" alt="integrations travis ci authorization" />
  </Step>

  <Step title="Start integration">
    Select which Infisical environment secrets you want to sync to which Travis CI repository and press create integration to start syncing secrets to Travis CI.

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/travis-ci/integrations-travisci-create.png" alt="create integration travis ci" />
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/travis-ci/integrations-travisci.png" alt="integrations travis ci" />
  </Step>
</Steps>

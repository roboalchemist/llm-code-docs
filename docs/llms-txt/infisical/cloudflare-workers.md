# Source: https://infisical.com/docs/integrations/secret-syncs/cloudflare-workers.md

# Source: https://infisical.com/docs/integrations/cloud/cloudflare-workers.md

# Source: https://infisical.com/docs/integrations/secret-syncs/cloudflare-workers.md

# Source: https://infisical.com/docs/integrations/cloud/cloudflare-workers.md

# Cloudflare Workers

> How to sync secrets from Infisical to Cloudflare Workers

Prerequisites:

* Set up and add envars to [Infisical Cloud](https://app.infisical.com)

<Steps>
  <Step title="Authorize Infisical for Cloudflare Workers">
    Obtain a Cloudflare [API token](https://dash.cloudflare.com/profile/api-tokens) and [Account ID](https://developers.cloudflare.com/fundamentals/get-started/basic-tasks/find-account-and-zone-ids/):

    Create a new [API token](https://dash.cloudflare.com/profile/api-tokens) in My Profile > API Tokens

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/cloudflare/integrations-cloudflare-credentials-1.png" alt="integrations cloudflare credentials 1" />
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/cloudflare/integrations-cloudflare-credentials-2.png" alt="integrations cloudflare credentials 2" />
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/cloudflare/integrations-cloudflare-workers-permission.png" alt="integrations cloudflare credentials 3" />

    Copy your [Account ID](https://developers.cloudflare.com/fundamentals/get-started/basic-tasks/find-account-and-zone-ids/) from Account > Workers & Pages > Overview

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/cloudflare/integrations-cloudflare-credentials-4.png" alt="integrations cloudflare credentials 4" />

    Navigate to your project's integrations tab in Infisical.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations.png" alt="integrations" />

    Press on the Cloudflare Workers tile and input your Cloudflare API token and account ID to grant Infisical access to your Cloudflare Workers.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/cloudflare/integration-cloudflare-workers-connect.png" alt="integrations cloudflare authorization" />
  </Step>

  <Step title="Start integration">
    Select which Infisical environment secrets you want to sync to Cloudflare Workers and press create integration to start syncing secrets.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/cloudflare/integration-cloudflare-workers-create.png" alt="integrations cloudflare" />
  </Step>
</Steps>

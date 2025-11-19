# Source: https://infisical.com/docs/integrations/cloud/cloud-66.md

# Cloud 66

> How to sync secrets from Infisical to Cloud 66

Prerequisites:

* Set up and add envars to [Infisical Cloud](https://app.infisical.com)

## Navigate to your project's integrations tab

<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations.png" alt="integrations" />

## Enter your Cloud 66 Access Token

In Cloud 66 Dashboard, click on the top right icon > Account Settings > Access Token
<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/cloud-66/integrations-cloud-66-dashboard.png" alt="integrations cloud 66 dashboard" />
<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/cloud-66/integrations-cloud-66-access-token.png" alt="integrations cloud 66 access token" />

Create new Personal Access Token.
<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/cloud-66/integrations-cloud-66-pat.png" alt="integrations cloud 66 personal access token" />

Name it **infisical** and check **Public** and **Admin**. Then click "Create Token"
<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/cloud-66/integrations-cloud-66-pat-setup.png" alt="integrations cloud 66 personal access token setup" />

Copy and save your token.
<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/cloud-66/integrations-cloud-66-copy-pat.png" alt="integrations cloud 66 copy API token" />

### Go to Infisical Integration Page

Click on the Cloud 66 tile and enter your API token to grant Infisical access to your Cloud 66 account.
<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/cloud-66/integrations-cloud-66-infisical-dashboard.png" alt="integrations cloud 66 tile in infisical dashboard" />

Enter your Cloud 66 Personal Access Token here. Then click "Connect to Cloud 66".
<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/cloud-66/integrations-cloud-66-paste-pat.png" alt="integrations cloud 66 tile in infisical dashboard" />

## Start integration

Select which Infisical environment secrets you want to sync to which Cloud 66 stacks and press create integration to start syncing secrets to Cloud 66.
<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/cloud-66/integrations-cloud-66-create.png" alt="integrations laravel forge" />

<Warning>
  Any existing environment variables in Cloud 66 will be deleted when you start syncing. Make sure to add all the secrets into the Infisical dashboard first before doing any integrations.
</Warning>

Done!
<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/cloud-66/integrations-cloud-66-done.png" alt="integrations laravel forge" />

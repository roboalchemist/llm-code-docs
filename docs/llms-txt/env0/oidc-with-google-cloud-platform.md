# Source: https://docs.envzero.com/guides/integrations/oidc-integrations/oidc-with-google-cloud-platform.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# OIDC for GCP

> Connect env zero to GCP using OIDC with Workload Identity Federation for temporary credentials

This guide is to help you connect to GCP with OIDC, instead of using static credentials.

## Overview

This guide will show you how to create a GCP Workload Identity Federation Provider, and attach it to a Service Account to generate temporary credentials by accepting env zero's OIDC token. Refer to [env zero's OIDC configuration](/guides/integrations/oidc-integrations).

## Workload Identity Federation Pool and Provider

1. Login to your GCP account and select the relevant project.
2. In the left-hand side menu select `IAM & Admin`
3. Go to `Workload Identity Federation` page
4. Click on the `Create Pool` button
5. Enter a name and description, make sure the `Enabled Pool` is selected and click on the `Continue` button.

<Frame caption="Identity Pool">
  <img src="https://mintcdn.com/envzero-b61043c8/t0QBBK-2O7wlTUvX/images/guides/integrations/oidc-integrations/identity_pool.png?fit=max&auto=format&n=t0QBBK-2O7wlTUvX&q=85&s=c9d96652714c84cd088abd57250fbfbb" alt="Google Cloud Identity Pool configuration interface showing OIDC provider setup" width="1284" height="1218" data-path="images/guides/integrations/oidc-integrations/identity_pool.png" />
</Frame>

1. In `Select a provider` selection choose OIDC, add a Provider name, enter a Proivder ID
2. In the `Issuer (URL)` section enter `https://login.app.env0.com/`
3. In the `Audiences` Select `Allowed audiences` and enter `https://prod.env0.com` and click on the continue button.

<Frame caption="Identity Provider">
  <img src="https://mintcdn.com/envzero-b61043c8/t0QBBK-2O7wlTUvX/images/guides/integrations/oidc-integrations/identity_provider.png?fit=max&auto=format&n=t0QBBK-2O7wlTUvX&q=85&s=b4bc77f2dd2f0f43f940072c4a4af2fa" alt="Google Cloud Identity Provider configuration showing OIDC settings and audience configuration" width="591" height="873" data-path="images/guides/integrations/oidc-integrations/identity_provider.png" />
</Frame>

1. In the `Configure provider attributes` under the `OIDC 1` enter `assertion.sub`
2. Click on the `Save` button

<Frame caption="Attribute Mapping">
  <img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/oidc-integrations/attribute_mapping.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=54d4f96257601119e43f8ab9f5159a3f" alt="Google Cloud attribute mapping configuration showing OIDC assertion mapping settings" width="1208" height="622" data-path="images/guides/integrations/oidc-integrations/attribute_mapping.png" />
</Frame>

<Info>
  **Adding Custom Claims**

  If you like to add more Custom Claims, for example, I would like to add the organization id claim I would click on the `Add Mapping` button and add `attribute.org_id` in the Google text box, and in the OIDC I would add `assertion.organizationId`, and repeat step 14 with the organization id.

  Read more about Custom Claims [here](/guides/integrations/oidc-integrations/#format-of-the-openid-connect-id-token)
</Info>

1. Follow [this guide](/guides/integrations/oidc-integrations/oidc-retrieving-your-subject-identifier) to get you `sub` value
2. In the Identity pool you've just created click on the `Grant Access` button
3. In the `Service account` select the relevant service account you would like to associate the identity pool with. Make sure this service account has the relevant access to what your code needs in order to create those resources
4. Select the `Only identities matching the filter` radio button and in the `Attribute name` select `subject` and in the `Attribure value` enter the value of your `sub` you got from the previous steps, and click on the `Save` button

<Frame caption="Grant Access to Service Account">
  <img src="https://mintcdn.com/envzero-b61043c8/t0QBBK-2O7wlTUvX/images/guides/integrations/oidc-integrations/grant_access_to_service_account.png?fit=max&auto=format&n=t0QBBK-2O7wlTUvX&q=85&s=a1f10a9c8da10e530fb302a0f2bf3498" alt="Grant Access to Service Account" width="1200" height="1158" data-path="images/guides/integrations/oidc-integrations/grant_access_to_service_account.png" />
</Frame>

1. In the `Configure your application` modal select the env zero provider you have created, insert `env0-oidc-token.txt` as a filename in `OIDC ID token path` text box , and in the `Format type` select `text` and click on the `Download Config` button
2. This will download a JSON configuration file that we will need during your deployment in env zero, and doesn't contain any sensitive data on it:

```json  theme={null}
{
  "type": "external_account",
  "audience": "//iam.googleapis.com/projects/XXXXXXXXXXXX/locations/global/workloadIdentityPools/env0-identity-pool/providers/env0oidc",
  "subject_token_type": "urn:ietf:params:oauth:token-type:jwt",
  "token_url": "https://sts.googleapis.com/v1/token",
  "service_account_impersonation_url": "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/env0-49@env0project.iam.gserviceaccount.com:generateAccessToken",
  "credential_source": {
    "file": "env0-oidc-token.txt",
    "format": {
      "type": "text"
    }
  }
}
```

## Configure env0 OIDC Credential

Go to the organization's credentials page and create a new deployment credential. Select `GCP OIDC` type and enter the following fields:

* `JSON configuration file content` - The content of the JSON configuration file from the previous step

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/oidc-integrations/44f3dab-image.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=caaea0fe7120d4dbaa12651537d36bcd" alt="Interface screenshot showing configuration options" width="1126" height="1448" data-path="images/guides/integrations/oidc-integrations/44f3dab-image.png" />
</Frame>

We will create a new file named `env0_credential_configuration.json` in the deployment pod that will contain the configuration file content. To be able to use OIDC with GCP you will need to read that configuration file in your code. For example, using terraform, it will look like this:

```hcl  theme={null}
provider "google" {
    credentials = file("env0_credential_configuration.json")
    project = "env0project"
    region = "us-central1"
    zone = "us-central1-c"
}
```

<Info>
  **Credential File Placement**

  The file will be placed in the environment's template path. The value is exposed by the [ENV0\_TEMPLATE\_PATH](/guides/admin-guide/custom-flows/#:~:text=deployed%20Template%20ID-,ENV0_TEMPLATE_PATH,-The%20deployed%20template) variable.

  If no specific template path is set, the file will be placed in the directory defined by the variable: [ENV0\_ROOT\_DIR](/guides/admin-guide/custom-flows/#exposed-env0-system-environment-variables:~:text=in%20the%20Environment-,ENV0_ROOT_DIR,-The%20root%20repository).
</Info>

Built with [Mintlify](https://mintlify.com).

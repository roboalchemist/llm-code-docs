# Source: https://docs.envzero.com/guides/integrations/oidc-integrations/oidc-with-aws.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# OIDC for AWS

> Connect env zero to AWS using OIDC with an Identity Provider and IAM role for temporary credentials

This guide is to help you connect to AWS with OIDC, instead of using a static API Key and Secret.

## Overview

This guide will show you how to create an AWS Identity Provider and IAM role to go along with it, and configure env zero to utilize OIDC. This will allow you to authenticate to AWS and get temporary credentials by accepting env zero's OIDC token. Refer to [env zero's OIDC configuration](/guides/integrations/oidc-integrations) for more information

## AWS Identity Provider and IAM Role

To be able to authenticate with OIDC, we will need to create an Identity Provider in your AWS account and attach an IAM role to it. We will follow [this guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html) by AWS.

### Create an Identity Provider

1. Login to your desired AWS account and go to Identity and Access Management (IAM)
2. In the left side menu under Access management, click on Identity Providers
3. Click on Add provider
4. Choose the OpenID Connect option
5. For Provider URL, enter [https://login.app.env0.com/](https://login.app.env0.com/) and click Get thumbprint
6. Under Audience, enter `hoMiq9PdkRh9LUvVpH4wIErWg50VSG1b`
7. Add tags if you wish, then click Add provider to create the identity provider

<Frame caption="Add an Identity Provide">
  <img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/oidc-integrations/add_an_identity_provide.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=04bf720f5b9f108dfb7a525f58107b80" alt="Add an Identity Provide" width="1660" height="729" data-path="images/guides/integrations/oidc-integrations/add_an_identity_provide.png" />
</Frame>

### Assign an IAM Role

1. Go to the Identity Provider you created in the previous step
2. In the Audiences section, select `hoMiq9PdkRh9LUvVpH4wIErWg50VSG1b` then click on the Actions button and select Assign role
3. Select the Create a new role option which will open the Create role wizard
4. Select the Web Identity option. Under Identity provider select `login.app.env0.com/:aud` and under Audience select `hoMiq9PdkRh9LUvVpH4wIErWg50VSG1b` then click Next: Permissions
5. In the permissions phase, select the permissions you would like this role to have. Remember, these permissions will be used to deploy your IaC so make sure they match the permissions your code needs.
6. Add tags if you wish
7. In the Review phase, give the role a name and a description, then click Create role

<Frame caption="Add Role">
  <img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/oidc-integrations/add_role.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=cb26bb549b4e3512138981d7ead7e76d" alt="AWS IAM role creation interface showing role name and description fields" width="1911" height="761" data-path="images/guides/integrations/oidc-integrations/add_role.png" />
</Frame>

### Add a `sub` Claim

1. Retrieve your organization `sub` identifier using [this guide](/guides/integrations/oidc-integrations/oidc-retrieving-your-subject-identifier)
2. Go to the AWS IAM role you created in the previous step
3. In the Trust Relationships tab, click Edit Trust Policy
4. Under the Action section, add the following:
   1. `sts:AssumeRoleWithWebIdentity`
   2. `sts:TagSession`
5. UnderCondition, go to the StringEquals section of the Policy JSON add `"login.app.env0.com/:sub": "{your_organization_sub}"` – Make sure you substitute `{your_organization_sub}`with the sub value you retrieved in the first step. It should be something like `"login.app.env0.com/:sub": "auth0|632b8219674bde0224a96141"`
6. Now click Update policy

```json Trust Policy theme={null}
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Federated": "arn:aws:iam::XXXXXXXXXXXX:oidc-provider/login.app.env0.com/"
            },
            "Action": [
                "sts:AssumeRoleWithWebIdentity",
                "sts:TagSession"
            ],
            "Condition": {
                "StringEquals": {
                    "login.app.env0.com/:aud": "hoMiq9PdkRh9LUvVpH4wIErWg50VSG1b",
                    "login.app.env0.com/:sub": "auth0|632b8219674bde0224a96141"
                }
            }
        }
    ]
}
```

<Image src="/images/guides/integrations/oidc-integrations/a8247b8a49c1e70c4192f536925bf3a50c3e65c3241e20e78b73ccd1a8d193b6-image.png" />

<Info>
  **Self-Hosted Agent Users**

  For EKS users, you will also need to add `"Action": "sts:AssumeRoleWithWebIdentity"` to either your node role or service account role where your agent is running.
</Info>

### Custom Claims with AWS Session Tags (Optional)

AWS OIDC identity providers support only a few out-of-the-box claims, which is a limitation when you want to control who inside env zero can access this AWS role. You can read more about [available claims for AWS here](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif).

AWS lets you pass [Session tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html) inside the JWT token, allowing you to have more control and define the right access level.

1. `organizationId` - The env zero Organization ID
2. `projectId` - The env zero Project ID
3. `templateId` - The env zero Template ID
4. `environmentId` - The env zero Environment ID
5. `deployerEmail` - The email address of the user who created this deployment

<Warning>
  AWS Session Tags Limitation

  As session tags have a length limitation, we will only add specific claims. These will undoubtedly give you the desired access control for your AWS role.

  You can read more about [AWS session tags limitation here](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html#id_session-tags_operations).
</Warning>

In order to configure the AWS session tags, you need to edit the role you created in the previous steps:

1. Go to the AWS IAM Role you created in the previous step
2. In the Trust Relationships tab, click Edit Trust Policy
3. Under Condition, select StringEquals for Policy JSON and add the designated claim as `aws:RequestTag/{custom_claim}`. If you would like to make sure that only a specific project ID has access to this AWS role, add the following: `"aws:RequestTag/projectId": ["1a433171-217e-4f58-9b4e-308d4d77902f"]`- This is applicable to all custom claims mentioned above. See the full example in the image below.
4. Click Update policy

```json Trust Policy theme={null}
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Federated": "arn:aws:iam::XXXXXXXXXXXX:oidc-provider/login.app.env0.com/"
            },
            "Action": [
                "sts:AssumeRoleWithWebIdentity",
                "sts:TagSession"
            ],
            "Condition": {
                "StringEquals": {
                    "login.app.env0.com/:aud": "hoMiq9PdkRh9LUvVpH4wIErWg50VSG1b",
                    "login.app.env0.com/:sub": "auth0|632b8219674bde0224a96141",
                    "aws:RequestTag/projectId": [
                      "1a433171-217e-4f58-9b4e-308d4d77902f"
                    ]
                }
            }
        }
    ]
}
```

<Frame caption="Trust Relationships With Custom Claims">
  <img src="https://mintcdn.com/envzero-b61043c8/t0QBBK-2O7wlTUvX/images/guides/integrations/oidc-integrations/trust_relationships_with_custom_claims.png?fit=max&auto=format&n=t0QBBK-2O7wlTUvX&q=85&s=8e4597ce2cdec621622a604e343ab96d" alt="Trust Relationships With Custom Claims" width="1191" height="874" data-path="images/guides/integrations/oidc-integrations/trust_relationships_with_custom_claims.png" />
</Frame>

## Configure env0 OIDC Credential

Go to the organization's credentials page and create a new deployment credential. Select AWS OIDC type and enter the following fields:

* `Role ARN` - The ARN of the role that was  previously created
* `Duration` - **Configure to 1 hour for OIDC.** Determines how long the token will  be valid. The token is generated when deployment starts, not when the credential is being created.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/oidc-integrations/9150fff-image.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=a08d8988ea3db951006d3aa9c29f0964" alt="AWS OIDC deployment credential configuration form showing Role ARN and Duration fields" width="1126" height="1302" data-path="images/guides/integrations/oidc-integrations/9150fff-image.png" />
</Frame>

<Warning>
  Troubleshooting

  **Not authorized to perform sts:AssumeRoleWithWebIdentity**

* Make sure your AssumeRole durations match the env zero credential and your maximum session in the role. Otherwise, try setting your duration to 1 hour.
</Warning>

### Override Role ARN - Deploying to a Different AWS Account

If you would like to authenticate to a different AWS account within a specific environment you can override the Role ARN configuration by using an environment variable. To do so, you will need to add an environment variable named `ENV0_AWS_ROLE_ARN`and set the value to the role you created in your AWS account you would like to authenticate to.

<Frame caption="Override Role ARN">
  <img src="https://mintcdn.com/envzero-b61043c8/t0QBBK-2O7wlTUvX/images/guides/integrations/oidc-integrations/override_role_arn.png?fit=max&auto=format&n=t0QBBK-2O7wlTUvX&q=85&s=7ed8380570f6f05f1b8756c456613f1e" alt="Environment variable override interface showing Role ARN configuration" width="1413" height="342" data-path="images/guides/integrations/oidc-integrations/override_role_arn.png" />
</Frame>

Built with [Mintlify](https://mintlify.com).

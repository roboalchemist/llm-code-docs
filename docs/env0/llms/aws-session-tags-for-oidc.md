# Source: https://docs.envzero.com/changelogs/2023/06/aws-session-tags-for-oidc.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🥸 AWS Session Tags for OIDC

> OpenID Connect (OIDC) allows clients to verify the identity of a user or an application based on the authentication performed by an Authorization Server. This will enable you to securely interact with 3rd party applications like your cloud provider. As env0 supports OIDC and have special claims to have full control of your authentication process, there was some limitation to using this method with AWS. However, now we are integrating with AWS with additional claims so you would be able to make sure each deployment has specific access to your AWS account.

With OpenID Connect (OIDC), clients can authenticate users or applications through an Authorization Server, ensuring secure interaction with third-party apps such as cloud providers. Though env0 supports OIDC and has special claims for authentication control, there were some limitations in using it with AWS. We have now integrated AWS with additional claims, allowing you to grant deployment-specific access to your AWS account.

## ✨ AWS Session Tags ✨

The OIDC token, with each env0 deployment, included [additional claims](/guides/integrations/oidc-integrations#format-of-the-openid-connect-id-token) like the organization id, project id, and deployer email, to give you more control over who can access your cloud account and with which role.

However, with AWS you couldn't use the custom claims in your JWT token as other vendors allow. Instead, AWS supports session tags. Using your (AWS IAM Role) trust policy, you can verify those tags, and add rules on top of them as you please.

Now, we added new claims to the JWT token that includes a new claim called `https://aws.amazon.com/tags` which will include a `principal_tags` section with the following claims:

1. `organizationId` - The env0 Organization ID
2. `projectId` - The env0 Project ID
3. `templateId` - The env0 Template ID
4. `environmentId` - The env0 Environment ID
5. `deployerEmail` - The email address of the user who created this deployment

You can read more about how to [set it up with env0 here](/guides/integrations/oidc-integrations/oidc-with-aws) and more about [AWS Session tags here](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html)

> ❗️ Breaking Change
>
> This introduces a breaking change!  You will need to add the `sts:TagSession` permission to the role for any existing AWS Role authenticating with OIDC, whether you're using session tags or not. This feature will be released on the **19th of June**.

## Related Content

[OIDC Integration](/guides/integrations/oidc-integrations)

[OIDC With AWS](/guides/integrations/oidc-integrations/oidc-with-aws)

[OIDC With AWS With Custom Claims](/guides/integrations/oidc-integrations/oidc-with-aws#custom-claims-with-aws-session-tags-optional)

[AWS Session Tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html)

Built with [Mintlify](https://mintlify.com).

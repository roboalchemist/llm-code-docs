# Source: https://docs.datafold.com/datafold-deployment/dedicated-cloud/aws.md

# Datafold VPC Deployment on AWS

> Learn how to deploy Datafold in a Virtual Private Cloud (VPC) on AWS.

<Note>
  **INFO**

  VPC deployments are an Enterprise feature. Please email [sales@datafold.com](mailto:sales@datafold.com) to enable your account.
</Note>

## Create a Domain Name (optional)

You can either choose to use your domain (for example, `datafold.domain.tld`) or to use a Datafold managed domain (for example, `yourcompany.dedicated.datafold.com`).

### Customer Managed Domain Name

Create a DNS A-record for the domain where Datafold will be hosted. For the DNS record, there are two options:

* **Public-facing:** When the domain is publicly available, we will provide an SSL certificate for the endpoint.
* **Internal:** It is also possible to have Datafold disconnected from the internet. This would require an internal DNS (for example, AWS Route 53) record that points to the Datafold instance. It is possible to provide your own certificate for setting up the SSL connection.

Once the deployment is complete, you will point that A-record to the IP address of the Datafold service.

## Give Datafold Access to AWS

For setting up Datafold, it is required to set up a separate account within your organization where we can deploy Datafold. We're following the [best practices of AWS to allow third-party access](https://docs.aws.amazon.com/IAM/latest/UserGuide/id%5Froles%5Fcommon-scenarios%5Fthird-party.html).

### Create a separate AWS account for Datafold

First, create a new account for Datafold. Go to **My Organization** to add an account:

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_landing-329bb3e7015c52b1b3a9d4872ff71d66.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=ecb7e602c3b08de265dacb1df1eac10e" data-og-width="1593" width="1593" data-og-height="878" height="878" data-path="images/onprem_aws_landing-329bb3e7015c52b1b3a9d4872ff71d66.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_landing-329bb3e7015c52b1b3a9d4872ff71d66.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=1d1dd34b489ca092788995df5ba5a6a5 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_landing-329bb3e7015c52b1b3a9d4872ff71d66.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=c631068d953452483122091b2ff8aa42 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_landing-329bb3e7015c52b1b3a9d4872ff71d66.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=d7abac8ab1dc7620a03a5ba1f59d0a03 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_landing-329bb3e7015c52b1b3a9d4872ff71d66.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=5004316cbd8cacc25d30522a4e869640 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_landing-329bb3e7015c52b1b3a9d4872ff71d66.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=2cd359c13851e11163c35f3e3492af1b 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_landing-329bb3e7015c52b1b3a9d4872ff71d66.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=8ad47cba5e59c951e16413618733c07d 2500w" />
</Frame>

Click **Add an AWS Account**:

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_add_account-e8f6d7c449b5763c1962b0df7322ecf0.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=549b03369b95e7623fe57e5dc532b957" data-og-width="1593" width="1593" data-og-height="878" height="878" data-path="images/onprem_aws_add_account-e8f6d7c449b5763c1962b0df7322ecf0.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_add_account-e8f6d7c449b5763c1962b0df7322ecf0.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=3add6311c17236abacca7c817aafe03a 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_add_account-e8f6d7c449b5763c1962b0df7322ecf0.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=97e5fa312b986eecde33780f82eb2f1f 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_add_account-e8f6d7c449b5763c1962b0df7322ecf0.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=29998282119a491d95edee409fc00ff7 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_add_account-e8f6d7c449b5763c1962b0df7322ecf0.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=bccdcc52d6c5d7ee423188ff4ab8c88a 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_add_account-e8f6d7c449b5763c1962b0df7322ecf0.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=63bff3ac6c8e33920fd9568c8130dab0 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_add_account-e8f6d7c449b5763c1962b0df7322ecf0.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=d54a5a18bb61f457c16a44bd0ac0201d 2500w" />
</Frame>

You can name this account anything that helps identify it clearly. In our examples, we name it **Datafold**. Make sure that the email address of the owner isn't used by another account.

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_account-41993b39bb1c092bd085a1727f5537e9.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=e0b959106f88d7ede59ded7fb7997a54" data-og-width="1593" width="1593" data-og-height="1136" height="1136" data-path="images/onprem_aws_account-41993b39bb1c092bd085a1727f5537e9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_account-41993b39bb1c092bd085a1727f5537e9.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=7bd72307ea05f4bcdd77d35826744103 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_account-41993b39bb1c092bd085a1727f5537e9.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=966d93f01380181036384e4a1e7e8ee0 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_account-41993b39bb1c092bd085a1727f5537e9.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=eaab173b708c779b307e492ccb756219 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_account-41993b39bb1c092bd085a1727f5537e9.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=932ad5b38472837e76e6a747fb645dc3 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_account-41993b39bb1c092bd085a1727f5537e9.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=5c53c5787dc6dd9c6aadc9bfe15144fd 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_account-41993b39bb1c092bd085a1727f5537e9.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=055e3adc3b951f5eba043280543f7886 2500w" />
</Frame>

When you click the **Create AWS Account** button, you'll be returned back the organization screen, and see the notification that the new account is being created. After refresh a few minutes later, the account should appear in the organizations list.

### Grant Third-Party access to Datafold

To make sure that deployment runs as expected, your Datafold Support Engineer may need access to the Datafold-specific AWS account that you created. The access can be revoked after the deployment if needed.

To grant access, log into the account created in the previous step. You can switch to the newly created account using the [Switch Role page](https://signin.aws.amazon.com/switchrole):

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_aws_switch_role-f8ff2e8a925e444830b7db4afd41a14d.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=43de213f0410fc802ed38ef6f6f44ded" data-og-width="1593" width="1593" data-og-height="872" height="872" data-path="images/onprem_aws_switch_role-f8ff2e8a925e444830b7db4afd41a14d.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_aws_switch_role-f8ff2e8a925e444830b7db4afd41a14d.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=47b26c7efda81871101e132b5972f853 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_aws_switch_role-f8ff2e8a925e444830b7db4afd41a14d.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=94d86401db3b4ab1303a0c956d06287d 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_aws_switch_role-f8ff2e8a925e444830b7db4afd41a14d.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=7d058ff7c3af83e9ebfec6fe3da143e6 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_aws_switch_role-f8ff2e8a925e444830b7db4afd41a14d.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=51afba04ebc6c906b68db9a2eac01cbd 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_aws_switch_role-f8ff2e8a925e444830b7db4afd41a14d.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=502d5ec9a4535a063dae99adb31bdddf 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_aws_switch_role-f8ff2e8a925e444830b7db4afd41a14d.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=18413ef3f774045bb57cffa4eff6fd6a 2500w" />
</Frame>

By default, the role name is **OrganizationAccountAccessRole**.

Click **Switch Role** to log in to the Datafold account.

## Grant Access to Datafold

Next, we need to allow Datafold to access the account. We do this by allowing the Datafold AWS account to access your AWS workspace. Go to the [IAM page](https://console.aws.amazon.com/iam/home) or type **IAM** in the search bar:

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_iam-dc7c1aa1e6e33ef4c37d46f0092c5268.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=8132e03e72c2f723790206113dbf13b2" data-og-width="1484" width="1484" data-og-height="854" height="854" data-path="images/onprem_aws_iam-dc7c1aa1e6e33ef4c37d46f0092c5268.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_iam-dc7c1aa1e6e33ef4c37d46f0092c5268.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=0224906492782f6b4ad2190c1cf22f16 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_iam-dc7c1aa1e6e33ef4c37d46f0092c5268.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=0f49a249de61c0cbc37db5652e026c26 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_iam-dc7c1aa1e6e33ef4c37d46f0092c5268.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=e58a1a6015f9e70bff52be81c7a2f963 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_iam-dc7c1aa1e6e33ef4c37d46f0092c5268.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=77c44b7423dbf73e4131a4cad605a091 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_iam-dc7c1aa1e6e33ef4c37d46f0092c5268.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=854526199c25a4b4835a88e11619c60b 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_iam-dc7c1aa1e6e33ef4c37d46f0092c5268.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=132fa23b5cb5c06a71f789b1266fe412 2500w" />
</Frame>

Go to the Roles page, and click the **Create Role** button:

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_create_role-82ea0f25999413532214cae7b4cf1c89.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=8417176c60c7b467090588b20b216222" data-og-width="1484" width="1484" data-og-height="854" height="854" data-path="images/onprem_aws_create_role-82ea0f25999413532214cae7b4cf1c89.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_create_role-82ea0f25999413532214cae7b4cf1c89.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=f67e6f63b968dbab9b24a2f601e8d2a0 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_create_role-82ea0f25999413532214cae7b4cf1c89.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=d8032e0c8fbfeb25cf3b08f2953e7e48 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_create_role-82ea0f25999413532214cae7b4cf1c89.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=99edbba40c4799d4455b03b0557ee4e3 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_create_role-82ea0f25999413532214cae7b4cf1c89.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=136f812410de0edc50bff12a05cc161b 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_create_role-82ea0f25999413532214cae7b4cf1c89.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=0f77d10a11640acf8e5b7cd201e05b43 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_create_role-82ea0f25999413532214cae7b4cf1c89.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=199490033f59d5e2b308109502255523 2500w" />
</Frame>

Select **Another AWS Account**, and use account ID `710753145501`, which is Datafold's account ID. Select **Require MFA** and click **Next: Permissions**.

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_role_config-11a94bf4eb4fb1921544b0824d65d223.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=6f71fb94b0427e11f18738e9c9639bb5" data-og-width="1484" width="1484" data-og-height="854" height="854" data-path="images/onprem_aws_role_config-11a94bf4eb4fb1921544b0824d65d223.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_role_config-11a94bf4eb4fb1921544b0824d65d223.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=95c2292924300065c552da526a647474 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_role_config-11a94bf4eb4fb1921544b0824d65d223.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=87c379d8fe9f02b9b24d971008f0c114 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_role_config-11a94bf4eb4fb1921544b0824d65d223.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=93d44d5470c9d7541bd7c13bd51443b4 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_role_config-11a94bf4eb4fb1921544b0824d65d223.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=cbfdd71748f7512c10b5d6f9b6b97181 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_role_config-11a94bf4eb4fb1921544b0824d65d223.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=be4801b775469da2befae6b399dcc242 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/onprem_aws_role_config-11a94bf4eb4fb1921544b0824d65d223.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=ec36f881a225bffc97015169773425db 2500w" />
</Frame>

On the Permissions page, attach the **AdministratorAccess** permissions for Datafold to have control over the resources within the account, or see [Minimal IAM Permissions](#minimal-iam-permissions).

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_aws_role_permissions-72630b3366b32c6e1a4986c52f98f439.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=8da938f9d77fffe2fbb7b419fd52e14e" data-og-width="1484" width="1484" data-og-height="933" height="933" data-path="images/onprem_aws_role_permissions-72630b3366b32c6e1a4986c52f98f439.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_aws_role_permissions-72630b3366b32c6e1a4986c52f98f439.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=d8cc13e9f3674b5e74ec2ad2d05adfb8 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_aws_role_permissions-72630b3366b32c6e1a4986c52f98f439.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=f15b9f9974e816105d6aebf313ab6aed 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_aws_role_permissions-72630b3366b32c6e1a4986c52f98f439.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=fd552639c1f531f8dc46a597f451eaa4 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_aws_role_permissions-72630b3366b32c6e1a4986c52f98f439.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=99b1cfafe1afd6b54b93489f42f00670 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_aws_role_permissions-72630b3366b32c6e1a4986c52f98f439.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=0b2ec43ba66d36dc09a8a48f23920a95 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/onprem_aws_role_permissions-72630b3366b32c6e1a4986c52f98f439.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=9406b62f38814e4fe7861fccf33e1af1 2500w" />
</Frame>

Next, you can set **Tags**; however, they are not a requirement.

Finally, give the role a name of your choice. Be careful not to duplicate the account name. If you named the account in an earlier step `Datafold`, you may want to name the role `Datafold-role`.

Click **Create Role** to complete this step.

Now that the role is created, you should be routed back to a list of roles in your organization.

Click on your newly created role to get a sharable link for the account and store this in your password manager. When setting up your deployment with a support engineer, Datafold will use this link to gain access to the account.

After validating the deployment with your support engineer, and making sure that everything works as it should, we will let you know when it's clear to revoke the credentials.

### Minimal IAM Permissions

Because we work in a Account dedicated to Datafold, there is no direct access to your resources unless explicitly configured (e.g., VPC Peering). The following IAM policy are required to update and maintain the infrastructure.

```JSON  theme={null}
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "acm:AddTagsToCertificate",
                "acm:DeleteCertificate",
                "acm:DescribeCertificate",
                "acm:GetCertificate",
                "acm:ListCertificates",
                "acm:ListTagsForCertificate",
                "acm:RemoveTagsFromCertificate",
                "acm:RequestCertificate",
                "acm:UpdateCertificateOptions",
                "apigateway:DELETE",
                "apigateway:GET",
                "apigateway:PATCH",
                "apigateway:POST",
                "apigateway:PUT",
                "apigateway:UpdateRestApiPolicy",
                "autoscaling:*",
                "ec2:*",
                "eks:*",
                "elasticloadbalancing:*",
                "iam:GetPolicy",
                "iam:GetPolicyVersion",
                "iam:GetOpenIDConnectProvider",
                "iam:GetRole",
                "iam:GetRolePolicy",
                "iam:GetUserPolicy",
                "iam:GetUser",
                "iam:ListAccessKeys",
                "iam:ListAttachedRolePolicies",
                "iam:ListGroupsForUser",
                "iam:ListInstanceProfilesForRole",
                "iam:ListPolicies",
                "iam:ListPolicyVersions",
                "iam:ListRolePolicies",
                "iam:PassRole",
                "iam:TagOpenIDConnectProvider",
                "iam:TagPolicy",
                "iam:TagRole",
                "iam:TagUser",
                "kms:CreateAlias",
                "kms:CreateGrant",
                "kms:CreateKey",
                "kms:Decrypt",
                "kms:DeleteAlias",
                "kms:DescribeKey",
                "kms:DisableKey",
                "kms:EnableKeyRotation",
                "kms:GenerateDataKey",
                "kms:GetKeyPolicy",
                "kms:GetKeyRotationStatus",
                "kms:ListAliases",
                "kms:ListResourceTags",
                "kms:PutKeyPolicy",
                "kms:RevokeGrant",
                "kms:ScheduleKeyDeletion",
                "kms:TagResource",
                "logs:CreateLogGroup",
                "logs:DeleteLogGroup",
                "logs:DescribeLogGroups",
                "logs:ListTagsLogGroup",
                "logs:ListTagsForResource",
                "logs:PutRetentionPolicy",
                "logs:TagResource",
                "rds:*",
                "ssm:GetParameter",
                "secretsmanager:CreateSecret",
                "secretsmanager:DeleteSecret",
                "secretsmanager:DescribeSecret",
                "secretsmanager:GetResourcePolicy",
                "secretsmanager:PutSecretValue",
                "secretsmanager:TagResource",
                "s3:*"
            ],
            "Resource": "*"
        }
    ]
}
```

Some policies we need from time to time. For example, when we do the first deployment. Since those are IAM-related, we will ask for temporary permissions when required.

```JSON  theme={null}
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "iam:AttachRolePolicy",
                "iam:CreateAccessKey",
                "iam:CreateOpenIDConnectProvider",
                "iam:CreatePolicy",
                "iam:CreateRole",
                "iam:CreateUser",
                "iam:DeleteAccessKey",
                "iam:DeleteOpenIDConnectProvider",
                "iam:DeletePolicy",
                "iam:DeleteRole",
                "iam:DeleteRolePolicy",
                "iam:DeleteUser",
                "iam:DeleteUserPolicy",
                "iam:DetachRolePolicy",
                "iam:PutRolePolicy",
                "iam:PutUserPolicy"
            ],
            "Resource": "*"
        }
    ]
}
```

It is easier to allow `PowerUserAccess` and then selectively add iam permissions given above.
PowerUserAccess has explicit denies for `account:*`, `organization:*` and `iam:*.`

# Datafold AWS infrastructure details

This document provides detailed information about the AWS infrastructure components deployed by the Datafold Terraform module, explaining the architectural decisions and operational considerations for each component.

## EBS volumes

The Datafold application requires 3 volumes for persistent storage, each deployed as encrypted Elastic Block Store (EBS) volumes in the primary availability zone. This also means that pods cannot be deployed outside the availability zone of these volumes, because the nodes wouldn't be able to attach them.

**ClickHouse data volume** serves as the analytical database storage for Datafold. ClickHouse is a columnar database that excels at analytical queries. The default 40GB allocation usually provides sufficient space for typical deployments, but it can be scaled up based on data volume requirements. The GP3 volume type with 3000 IOPS ensures consistent performance for analytical workloads.

**ClickHouse Logs Volume** stores ClickHouse's internal logs and temporary data. The separate logs volume prevents log data from consuming IOPS and I/O performance from actual data storage.

**Redis Data Volume** provides persistent storage for Redis, which handles task distribution and distributed locks in the Datafold application. Redis is memory-first but benefits from persistence for data durability across restarts. The 50GB default size accommodates typical caching needs while remaining cost-effective.

All EBS volumes are encrypted using AWS KMS, managed by AWS, ensuring data security at rest. The volumes are deployed in the first availability zone to minimize latency and simplify backup strategies.

## Load balancer

The load balancer serves as the primary entry point for all external traffic to the Datafold application. The module offers 2 deployment strategies, each with different operational characteristics and trade-offs.

**External Load Balancer Deployment** (the default approach) creates an AWS Application Load Balancer through Terraform. This approach provides centralized control over load balancer configuration and integrates well with existing AWS infrastructure. The load balancer automatically handles SSL termination, health checks, and traffic distribution across Kubernetes pods. This method is ideal for organizations that prefer infrastructure-as-code management and want consistent load balancer configurations across environments.

**Kubernetes-Managed Load Balancer** deployment sets `deploy_lb = false` and relies on the AWS Load Balancer Controller running within the EKS cluster. This approach leverages Kubernetes-native load balancer management, allowing for dynamic scaling and easier integration with Kubernetes ingress resources. The controller automatically provisions and manages load balancers based on Kubernetes service definitions, which can be more flexible for applications that need to scale load balancer resources dynamically.

Both load balancers apply the currently recommended and strictest ELB security policies: `ELBSecurityPolicy-TLS13-1-2-Res-2021-06` and security settings.

The choice between these approaches often depends on operational preferences and existing infrastructure patterns. External deployment provides more predictable resource management, while Kubernetes-managed deployment offers greater flexibility for dynamic workloads.

**Security** A security group shared between the load balancer and the EKS nodes allows traffic to reach only the EKS nodes and nothing else. The load balancer allows traffic to land directly into the EKS private subnet.

**Certificate** The certificate can be pre-created by the customer and then attached, or a cloud-managed certificate can be created on the fly.
The application will not function without HTTPS, so a certificate is mandatory. After the certificate is created either manually or through this repository, it must be validated by the DNS administrator by adding a CNAME record. This puts the certificate in "Issued" state. The certificate cannot be found when it's still provisioning.

## EKS cluster

The Elastic Kubernetes Service (EKS) cluster forms the compute foundation for the Datafold application, providing a managed Kubernetes environment optimized for AWS infrastructure.

**Network Architecture** The entire cluster is deployed into private subnets. This means the data plane is not reachable from the Internet except through the load balancer. A NAT gateway allows the cluster to reach the internet (egress traffic) for downloading pod images, optionally sending Datadog logs and metrics, and retrieving the version to apply to the cluster from our portal. The control plane is accessible via a private endpoint using a PrivateLink setup from, for example, a VPN VPC elsewhere. This is a private+public endpoint, so the control plane can also be made accessible through the Internet, but then the appropriate CIDR restrictions should be put in place.

For a typical dedicated cloud deployment of Datafold, only around 100 IPs are needed. This assumes 3 r7a.2xlarge instances where one node runs ClickHouse+Redis, another node runs the application, and a third node may be put in place when version rollovers occur. This means a subnet of size /24 (253 IPs) should be sufficient to run this application.

By default, the repository creates a VPC and subnets, but by specifying the VPC ID of an already existing VPC, the cluster and load balancer
get deployed into existing network infrastructure. This is important for some customers where they deploy a different architecture without NAT gateways, firewall options that check egress, and other DLP controls.

**Add-ons**

The cluster includes essential add-ons like CoreDNS for service discovery, the VPC CNI for networking, and the EBS CSI driver for persistent volume management. These components are automatically updated and maintained by AWS, reducing operational overhead.

The AWS load balancer controller and metrics-server are deployed separately via Helm charts in the application deployment, not through this Terraform infrastructure. The Load Balancer Controller manages at least the AWS target group that enables ingress for the Datafold application. Optionally, it may also manage the entire external load balancer.

**Node Management** supports up to three managed node groups, allowing for workload-specific resource allocation. Each node group can be configured with different instance types, enabling cost optimization and performance tuning for different application components. The cluster autoscaler automatically adjusts node count based on resource demands, ensuring efficient resource utilization while maintaining application availability. One typical way to deploy is to let the application pods go on a wider range of nodes, and set up tolerations and labels on the second node group, which are then selected by both Redis and ClickHouse. This is because Redis and ClickHouse have restrictions on the zone they must be present in because of their volumes, and ClickHouse is a bit more CPU intensive. This method optimizes CPU performance for the Datafold application.

**Security Features** include IAM Roles for Service Accounts (IRSA), which provide fine-grained IAM permissions to Kubernetes pods without requiring AWS credentials in container images. This approach enhances security by following the principle of least privilege and integrates seamlessly with AWS security services.

## IAM Roles and Permissions

The IAM architecture follows the principle of least privilege, providing specific permissions only where needed. Service accounts in Kubernetes are mapped to IAM roles using IRSA, enabling secure access to AWS services without embedding credentials in application code.

**EBS CSI Controller Role** enables the Kubernetes cluster to manage EBS volumes dynamically. This role allows pods to request persistent storage that's automatically provisioned and attached to the appropriate nodes or attach static volumes. The permissions are scoped to only the EBS operations needed for volume lifecycle management.

**Load Balancer Controller Role** provides the permissions necessary for Kubernetes to manage AWS load balancers. This includes creating target groups, registering and deregistering targets, and managing load balancer listeners. The controller can automatically provision load balancers based on Kubernetes service definitions, enabling seamless integration between Kubernetes and AWS networking.

**Cluster Autoscaler Role** allows the cluster to automatically scale node groups based on resource demands. This role can describe and modify Auto Scaling groups, enabling the cluster to add or remove nodes as needed. The autoscaler considers pod resource requests and node capacity when making scaling decisions.

**Datafold Roles** Datafold has roles per pod pre-defined which can have their permissions assigned when they need them. At the moment, we have two specific roles in use. One is for the ClickHouse pod to be able to make backups and store them on S3. The other is for the use of the Bedrock service for our AI offering.

These roles are automatically created and configured when the cluster is deployed, ensuring that the necessary permissions are in place for the cluster to function properly. The use of IRSA means that these permissions are automatically rotated and managed by AWS, reducing security risks associated with long-lived credentials.

## RDS database

The PostgreSQL Relational Database Service (RDS) instance serves as the primary relational database for the Datafold application, storing user data, configuration, and application state.

**Storage Configuration** starts with a 20GB initial allocation that can automatically scale up to 100GB based on usage patterns. This auto-scaling feature prevents storage-related outages while avoiding over-provisioning. For typical deployments, storage usage remains under 200GB, though some high-volume deployments may approach 400GB. The GP3 storage type provides consistent performance with configurable IOPS and throughput.

**High Availability** is intentionally disabled by default, meaning the database runs in a single availability zone. This configuration reduces costs and complexity while still providing excellent reliability. The database includes automated backups with 14-day retention, ensuring data can be recovered in case of failures. For organizations requiring higher availability, multi-AZ deployment can be enabled, though this significantly increases costs.

**Security and Encryption** always encrypts data at rest using AWS KMS. A dedicated KMS key is created for the database, providing better security isolation and audit capabilities compared to using the default AWS RDS key. The database is deployed in private subnets with security groups that restrict access to only the EKS cluster, ensuring network-level security.

The database configuration prioritizes operational simplicity and cost-effectiveness while maintaining the security and reliability required for production workloads. The combination of automated backups, encryption, and network isolation provides a robust foundation for the application's data storage needs.

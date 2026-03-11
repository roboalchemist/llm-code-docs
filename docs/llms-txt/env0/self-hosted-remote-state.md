# Source: https://docs.envzero.com/guides/admin-guide/remote-backend/self-hosted-remote-state.md

# Source: https://docs.envzero.com/changelogs/2023/11/self-hosted-remote-state.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🤳🏡 Self Hosted Remote State

> When orchestrating your infrastructure with Terraform, accessing the state of a remote backend environment securely is a common need. There are instances where safeguarding this sensitive information in house or in a specific region is needed.
Now with our Self-Hosted Remote State you have the power to take control of your environment's state storing it on your chosen bucket and configurations.

## 🔐 Setting Up Your Remote State 🔐

In order to start storing your state in your account all you need to do is deploy our [remote-state-bucket](https://github.com/env0/remote-state-bucket-module) module to create the necessary resources for env0 to be able to access the stored state object.
Once the module is deployed please contact our support team with the module outputs we will configure your organization to use your configured newly configured remote state bucket for your env0 remote state environments.

When orchestrating your infrastructure with Terraform, accessing the state of a remote backend environment securely is a common need. There are instances where safeguarding this sensitive information in house or in a specific region is needed.

Now with our Self-Hosted Remote State you have the power to take control of your environment's state storing it on your chosen bucket and configurations.

## 🔐 Setting Up Your Remote State 🔐

In order to start storing your state in your account all you need to do is deploy our [remote-state-bucket](https://github.com/env0/remote-state-bucket-module) module to create the necessary resources for env0 to be able to access the stored state object.

Once the module is deployed please contact our support team with the module outputs we will configure your organization to use your configured newly configured remote state bucket for your env0 remote state environments.

## 📝 Recommended Blog Reads

* [Self Hosted Remote State](/guides/admin-guide/remote-backend/self-hosted-remote-state) - more details in our docs
* [Manage Terraform Remote State with a Remote Backend](https://www.env0.com/blog/terraform-remote-state-using-a-remote-backend)

Built with [Mintlify](https://mintlify.com).

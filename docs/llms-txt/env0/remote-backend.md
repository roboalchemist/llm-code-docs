# Source: https://docs.envzero.com/changelogs/2022/10/remote-backend.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🔙✋ Remote Backend

> Terraform offers several state storage options, of which env0 supports Remote Backend, which has some great benefits such as: No underlying infrastructure setup and management, Security, State consistency & Local runs. Using env zero's Remote Backend has additional advantages: Not Terraform Backend configuration when running inside env0...

Terraform uses persisted state data to keep track of the resources it manages. Most non-trivial Terraform configurations use a [backend](https://www.terraform.io/language/settings/backends/configuration) to store the state remotely. This lets multiple people access the state data and work together on that collection of infrastructure resources.

Terraform offers several state storage options, of which env zero supports [Remote Backend](https://www.terraform.io/language/settings/backends/remote), which has some great benefits such as:

* **No underlying infrastructure setup and management** - env zero takes care of the setup as opposed to other approaches, where you need to do all the setup and management yourself (for example, [S3 Backend](https://www.terraform.io/language/settings/backends/s3) requires you to create an S3 Bucket and an optional DynamoDB Table for locking beforehand)
* **Security** - env zero stores the state securely for you and assures only you can access it
* **State consistency** - Remote Backends assure that users won't overwrite each other's state with a locking mechanism and that they receive the most recent state on every Terraform operation
* **Local runs** - By providing the Remote Backend configuration and a successful [login](/guides/admin-guide/remote-backend/login), users can run Terraform operations locally while still working on a shared state.

Using env zero's Remote Backend has additional advantages:

* **No Terraform Backend configuration when running inside env zero** - you don't have to provide any type of configuration; you just deploy your code as is, and env zero will automatically configure it to use the Remote Backend
* **States UI** - view the current version of your state as well as all of the previous versions
* **Correlation of Deployment to State** - easily figure out which deployment is responsible for a specific change to your state (Coming soon)

After successfully deploying an environment with a remote backend, you would have access to the **"States"** tab in the environment page, in which you could view all state versions of a specific environment & downloading them.

## ✨ Use Remote Backend In Your Environments ✨

You can configure your Environment to use Remote Backend by following this [simple guide](/guides/admin-guide/remote-backend#use-remote-backend-in-a-new-environment)

## Suggested Blog Content

[Terraform Modules Guide](https://www.env0.com/blog/terraform-modules)

[Terraform Plan Examples](https://www.env0.com/blog/terraform-plan)

[Managing Terraform Variable Hierarchy](https://www.env0.com/blog/managing-terraform-variable-hierarchy)

[Manage Terraform Remote State with a Remote Backend](https://www.env0.com/blog/terraform-remote-state-using-a-remote-backend)

Built with [Mintlify](https://mintlify.com).

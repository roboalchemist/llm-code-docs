# Source: https://docs.envzero.com/changelogs/2022/06/managing-pulumi-version.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🔢 Managing Pulumi Version

> Managing software versions of your Infrastructure as code framework is one of the basic aspects when managing your deployment and code. Now you can specify the exact Pulumi CLI version you want your IaC to run with and avoid version incompatibility issues and have full control over what versions update and backward compatibilities issues.

Managing software versions of your Infrastructure as code framework is one of the basic aspects when managing your deployment and code. Now you can specify the exact Pulumi CLI version you want your IaC to run with and avoid version incompatibility issues and have full control over what versions update and backward compatibilities issues.

### ✨ Setting Pulumi Version ✨

The version defined for Pulumi templates until recently defaulted to being the latest stable Pulumi CLI build,\
Now you can choose exactly what version you want your CLI to run with.
You can define your version by:

* Defining the environment variable `ENV0_PULUMI_VERSION`
* Choosing your version in our template wizard

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/4i75qYgyhlssLgkA/images/changelogs/2022/06/pulumi_version.png?fit=max&auto=format&n=4i75qYgyhlssLgkA&q=85&s=2977f73a0e6d982f2e17c200575855c4" alt="Pulumi version management interface showing version selection and configuration options" width="2708" height="1536" data-path="images/changelogs/2022/06/pulumi_version.png" />
</Frame>

You can read more about defining an IaC version for you templates [here](/guides/admin-guide/templates)

Built with [Mintlify](https://mintlify.com).

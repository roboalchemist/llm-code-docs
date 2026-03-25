# Source: https://docs.envzero.com/guides/admin-guide/environment-discovery.md

# Source: https://docs.envzero.com/changelogs/2024/02/environment-discovery.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🔎 Environment Discovery

> Automatically create, plan, deploy and destroy Environments in env zero by simply creating pull requests within a preconfigured directory structure

Managing your IaC through env zero provides many advantages, but manual environment creation and deployment can be tedious and error-prone at scale.\
env zero now seamlessly syncs your Git folder structure with projects and environments. Manage and maintain the structure your team thrives on without breaking a sweat.

# ✨ Introducing: Environment Discovery ✨

With **Environment Discovery** you can create, plan, deploy and destroy env zero environments automatically, just by managing your Pull Requests on your favorite Git provider.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/hr9e779VSnIZk8JC/images/changelogs/2024/02/8011246-image.png?fit=max&auto=format&n=hr9e779VSnIZk8JC&q=85&s=54abbc3ec2eaa7174914bda0e30596f9" alt="Feature demonstration screenshot showing new functionality" width="1300" height="576" data-path="images/changelogs/2024/02/8011246-image.png" />
</Frame>

## Here's How

1. Configure an **Environment Discovery** under Project Settings.
2. Open a **Pull Request** with the infrastructure you'd like to deploy, under the directory structure you configured.
3. In env zero, the environment will be created but won't be deployed. instead, you'll see a **PR Plan** for the code you pushed.
4. **Review and Merge** the changes you pushed.
5. The environment will be deployed in env zero.

Want to learn more? visit [our docs](/guides/admin-guide/environment-discovery)

Built with [Mintlify](https://mintlify.com).

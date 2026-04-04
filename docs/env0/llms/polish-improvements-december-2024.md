# Source: https://docs.envzero.com/changelogs/2024/12/polish-improvements-december-2024.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# ✨ Polish & Improvements - December 2024

This month, we’ve rolled out several updates and improvements to enhance workflows, address common challenges, and bring new capabilities based on user feedback. Here’s a quick look at what’s new.

## Improved Self-Hosted VCS Management

With the latest update to managing self-hosted VCS, we’ve introduced two key improvements:

#### Support for Multiple VCS Agents

Manage multiple VCS Agents (Proxies) within the same organization. This enhancement allows routing requests to different servers, providing greater flexibility for distributed systems and workload-specific setups.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/BZYthPtvpSdQtcKJ/images/changelogs/2024/12/41417cde12a3868dcf1c3dcef88b2a24b3535921b86ed60aa62a37cbc456d697-image.png?fit=max&auto=format&n=BZYthPtvpSdQtcKJ&q=85&s=234a6b6beb44ad4cd4f2395f59c1b8c7" alt="Feature demonstration screenshot showing new functionality" width="701" height="176" data-path="images/changelogs/2024/12/41417cde12a3868dcf1c3dcef88b2a24b3535921b86ed60aa62a37cbc456d697-image.png" />
</Frame>

#### Centralized Configuration in the UI

Use the Agents tab in Organization Settings to configure a self-hosted VCS connection once, assign a VCS agent key, and reuse it across templates and environments. This streamlines management and eliminates redundant configurations.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/BZYthPtvpSdQtcKJ/images/changelogs/2024/12/bbd94d272c39891f68173e8591ed17c99ea203383fce2a6cf0dd7db555d647af-image.png?fit=max&auto=format&n=BZYthPtvpSdQtcKJ&q=85&s=01ea5d981d71c8f82ffb0f631ddb08d9" alt="Feature demonstration screenshot showing new functionality" width="2330" height="474" data-path="images/changelogs/2024/12/bbd94d272c39891f68173e8591ed17c99ea203383fce2a6cf0dd7db555d647af-image.png" />
</Frame>

When creating a new template or VCS environment, the repository URL selection is now available as a dropdown list instead of a free-text field, allowing you to select a repository defined in the VCS Connections list, or add a new one.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/BZYthPtvpSdQtcKJ/images/changelogs/2024/12/4559d27b6570dcaffbe106ad096621a809a402b731357fa4d31acb0a2f553b35-image.png?fit=max&auto=format&n=BZYthPtvpSdQtcKJ&q=85&s=090e4bdb949f5e7360d5d8e55f8b9030" alt="Feature demonstration screenshot showing new functionality" width="707" height="273" data-path="images/changelogs/2024/12/4559d27b6570dcaffbe106ad096621a809a402b731357fa4d31acb0a2f553b35-image.png" />
</Frame>

These updates make it easier to scale and manage VCS connections efficiently.\
For more information, visit the updated [Documentation on Managing Self-Hosted VCS](/guides/admin-guide/templates/self-hosted-vcs).ֿ

## Vault Authentication via Certificates

We've added support for Vault authentication via certificates in env zero's [Secrets](/guides/admin-guide/variables#secrets) in Self-Hosted Agent. This enhancement ensures secure, seamless access to Vault-managed secrets, leveraging certificate-based authentication for improved security and easier integration with your existing PKI infrastructure. [Learn more](/guides/admin-guide/self-hosted-kubernetes-agent#customoptional-configuration)

## GitLab Personal & Group Access Token Support

We now support GitLab integration using [Personal](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html) or [Group](https://docs.gitlab.com/ee/user/group/settings/group_access_tokens.html) Access Tokens, making permission management more flexible and efficient.

When setting up a new Environment or Template, you'll see GitLab Access Token as an authentication option alongside OAuth.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/BZYthPtvpSdQtcKJ/images/changelogs/2024/12/9e33eb926ecb4a1cd878230a75261500985bdcd037b2b25a0287094a4f2f7dbb-image.png?fit=max&auto=format&n=BZYthPtvpSdQtcKJ&q=85&s=32734693f5b64205994f50aa98738eca" alt="Feature demonstration screenshot showing new functionality" width="992" height="668" data-path="images/changelogs/2024/12/9e33eb926ecb4a1cd878230a75261500985bdcd037b2b25a0287094a4f2f7dbb-image.png" />
</Frame>

[Learn more](/guides/admin-guide/templates/gitlab-integration)

## Cost Estimation for Terragrunt Run-All

You can now set up cost estimation for Terragrunt run-all executions. env zero uses Infracost to perform cost evaluation on each of the generated plans and combine them together. [Learn more](/guides/policies-governance/cost-estimation)

## Filter Deployments by User and Status

You can now filter deployments by status or by user that started the deployment.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/BZYthPtvpSdQtcKJ/images/changelogs/2024/12/2ffec0b92af664a842b216087a134b60478d2836ff52952fffbb611984e9c447-265a3e02fed2196dc77b07dfe81789cd06210b863d7f0d1df0617cffb8ae59fe-image_1.png?fit=max&auto=format&n=BZYthPtvpSdQtcKJ&q=85&s=02095ea6f0f3d3929cd3c673123db13a" width="1403" height="560" data-path="images/changelogs/2024/12/2ffec0b92af664a842b216087a134b60478d2836ff52952fffbb611984e9c447-265a3e02fed2196dc77b07dfe81789cd06210b863d7f0d1df0617cffb8ae59fe-image_1.png" />
</Frame>

<br />

## Filter Environments from the Summary Chart

Clicking any part of the Environments donut chart in the Summary Dashboard will now filter the Environment table below according to the selected Environment Status, making it easier to drill down into relevant data.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/hr9e779VSnIZk8JC/images/changelogs/2024/12/125107003237caee9441a35b02a555b9897a1d1f3c4f3c77e0148d6b84b35cd4-image.png?fit=max&auto=format&n=hr9e779VSnIZk8JC&q=85&s=283d13cc198af15655fdc789e4200843" alt="Feature demonstration screenshot showing new functionality" width="1400" height="761" data-path="images/changelogs/2024/12/125107003237caee9441a35b02a555b9897a1d1f3c4f3c77e0148d6b84b35cd4-image.png" />
</Frame>

<br />

## Global Search by Environment ID

Our Global Search (CMD/CTRL + K) now supports searching by Environment ID, making it easier to immediately navigate to a specific environment you’d like to take a look at.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/BZYthPtvpSdQtcKJ/images/changelogs/2024/12/713b6e9d3ffa5c18dbcaa72945878db61343f617ffd6ebe65f152d5964e6dbcf-image.png?fit=max&auto=format&n=BZYthPtvpSdQtcKJ&q=85&s=675ba95484ecc0d5ef08a2f08b5faf0d" alt="Feature demonstration screenshot showing new functionality" width="609" height="127" data-path="images/changelogs/2024/12/713b6e9d3ffa5c18dbcaa72945878db61343f617ffd6ebe65f152d5964e6dbcf-image.png" />
</Frame>

Built with [Mintlify](https://mintlify.com).

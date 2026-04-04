# Source: https://docs.envzero.com/guides/admin-guide/custom-flows/project-level-custom-flow.md

# Source: https://docs.envzero.com/changelogs/2022/12/project-level-custom-flow.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🎚️ Project Level Custom Flow

> Tired of copying the same custom-flow files in different environments? Project-level custom flow comes into play! It will allow you to configure one custom flow for all environments within a project by pointing to a different custom-flow yaml/yml file. This file can be in a separate repository, thus making sure all of your deployments will run that specific code and separate the IaC code from the policies and general deployment script you would like to run.

Project-level Custom Flows enable you to move a custom flow out of the main repository. Now you can configure a single custom flow file for all environments within a project by pointing to a different custom-flow yaml file. Because this custom flow file can be located in a separate repository, it is possible to separate the actual infrastructure code from your deployment policies and scripts that you would like to run on every deployment.

### ✨ Enabling Project Level Custom Flow ✨

This new setting is available in **Project Policies** section.

Here is an example of defining a common OPA policy within a project:

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/4i75qYgyhlssLgkA/images/changelogs/2022/12/5d13e05-image.png?fit=max&auto=format&n=4i75qYgyhlssLgkA&q=85&s=1fb04906ff519d516c36d9283c6e40b9" alt="Feature demonstration screenshot showing new functionality" style={{ width: '400px' }} width="1237" height="1137" data-path="images/changelogs/2022/12/5d13e05-image.png" />
</Frame>

After enabling, any environment deployment within the project will use this custom flow file.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/4i75qYgyhlssLgkA/images/changelogs/2022/12/bd0c9a1-image.png?fit=max&auto=format&n=4i75qYgyhlssLgkA&q=85&s=598aa04adcf6c308e8cb8e1493749929" alt="Feature demonstration screenshot showing new functionality" style={{ width: '400px' }} width="847" height="543" data-path="images/changelogs/2022/12/bd0c9a1-image.png" />
</Frame>

Learn more about `Project-level custom flow` in our [documentation](/guides/admin-guide/custom-flows/project-level-custom-flow)🎚️.

Built with [Mintlify](https://mintlify.com).

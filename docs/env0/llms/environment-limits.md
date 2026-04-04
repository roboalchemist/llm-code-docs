# Source: https://docs.envzero.com/guides/policies-governance/environment-limits.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Set Environment Limits

> Restrict the number of active environments per user or per project in env zero

## Control Number of Environments

env zero allows you to restrict the number of active environments in each project. You can limit both the number of environments allowed per user, and the total amount of environments in the project. By default projects have no restrictions on the number of environments allowed.

You must be a Project Admin for the project you would like to create this restriction for. Simply go to "Project Settings", and select the "Policies" tab. There you can set a restriction on the number of active environments allowed.

<Frame caption="Project Settings - Policies - Environment Limits">
  <img src="https://mintcdn.com/envzero-b61043c8/t0QBBK-2O7wlTUvX/images/guides/policies-governance/project_settings_environment_limits_configuration.png?fit=max&auto=format&n=t0QBBK-2O7wlTUvX&q=85&s=c07ce2336ae9c18d3b17ad68984c4962" alt="Project settings environment limits configuration" width="2230" height="1880" data-path="images/guides/policies-governance/project_settings_environment_limits_configuration.png" />
</Frame>

### Control Number of Environments Allowed per User

<Note>
  Note

  This restriction does not affect users that have Project Admin or Organization Admin privileges.
</Note>

When a user tries to deploy an environment, and this deployment will cause the user to exceed the allowed number of active environments for the user in the project, the user will get the following error:

<img src="https://mintcdn.com/envzero-b61043c8/t0QBBK-2O7wlTUvX/images/guides/policies-governance/384c060-screen_shot_2021-10-20_at_10.png?fit=max&auto=format&n=t0QBBK-2O7wlTUvX&q=85&s=e899b9c3f8d2369f4b004ad22c1c81c9" alt="" width="2960" height="1160" data-path="images/guides/policies-governance/384c060-screen_shot_2021-10-20_at_10.png" />

### Control Number of Environments Allowed in Entire Project

When a user tries to deploy an environment, and the project already exceeds the allowed number of active environments in the project, the user will get the following error:

<img src="https://mintcdn.com/envzero-b61043c8/t0QBBK-2O7wlTUvX/images/guides/policies-governance/4940abf-screen_shot_2021-10-20_at_10.png?fit=max&auto=format&n=t0QBBK-2O7wlTUvX&q=85&s=68c4580c4f00b0fbc57bc041ed4502b6" alt="" width="2960" height="1160" data-path="images/guides/policies-governance/4940abf-screen_shot_2021-10-20_at_10.png" />

Built with [Mintlify](https://mintlify.com).

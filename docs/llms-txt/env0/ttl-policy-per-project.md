# Source: https://docs.envzero.com/changelogs/2022/06/ttl-policy-per-project.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# ⌛️ TTL Policy Per Project

> env0 lets you create a managed self-service inside your organization, empower your developers and RnD teams to spin up, update and destroy an environment with one click, and easily track environment status or deployment history. To manage those environments and make sure no resources wasted, env0 lets you create TTL policies. The Organization administrator can limit the environment's time-to-live, but often, the same settings don't fit the needs of different projects in the organization. Now we allow overriding organization TTL policy on a project basis.

env0 lets you create a managed self-service inside your organization, empower your developers and R\&D teams to spin up, update and destroy an environment with one click, and easily track environment status or deployment history. To manage those environments and make sure no resources wasted, env0 lets you create [TTL policies](/guides/policies-governance/policy-ttl). The Organization administrator can limit the environment's time-to-live, but often, the same settings don't fit the needs of different projects in the organization. Now we allow overriding organization TTL policy on a project basis.

### ✨ TTL Policy Settings ✨

When users create or redeploy an environment, they can set the environment's time-to-live. TTL Policies define the default and maximum time-to-live values for the environment either at the organization level or at the project level.

### Organization Level Policy

Administrators can set the policies at the Organization level under the Policies tabs.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/4i75qYgyhlssLgkA/images/changelogs/2022/06/organization_settings_-_policies_-_ttl.png?fit=max&auto=format&n=4i75qYgyhlssLgkA&q=85&s=53212fcb4d6adc7c732ce8b517449a3d" alt="Organization Settings - Policies - TTL" width="2230" height="1090" data-path="images/changelogs/2022/06/organization_settings_-_policies_-_ttl.png" />
</Frame>

### Project Level

Project Admins can find the new settings in Project Settings > Policies tab

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/4i75qYgyhlssLgkA/images/changelogs/2022/06/project_settings_-_policies_-_ttl.png?fit=max&auto=format&n=4i75qYgyhlssLgkA&q=85&s=1901942dab3d7065f275624ef755aa7f" alt="Project Settings - Policies - TTL" width="2230" height="1880" data-path="images/changelogs/2022/06/project_settings_-_policies_-_ttl.png" />
</Frame>

The defaults are to use the settings from the Organization policy, but you can override it for each project.
You can read more about TTL policies [here](/guides/policies-governance/policy-ttl).

Built with [Mintlify](https://mintlify.com).

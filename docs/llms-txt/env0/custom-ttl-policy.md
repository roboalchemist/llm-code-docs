# Source: https://docs.envzero.com/changelogs/2023/02/custom-ttl-policy.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# ⌚ Custom TTL Policy

> env0 lets you create a managed self-service inside your organization, empower your developers and RnD teams to spin up, update and destroy an environment with one click, and easily track environment status or deployment history. To manage those environments and ensure no wasted resources are left behind, env0 lets you create custom TTL policies in the Organization or Project policies to ensure that.

One potential side affect of empowering development teams with self-service access to cloud resources is that systems and services may be left running, and unused for long periods. This is wasteful, and potentially dangerous. env0 has already had the ability to define a Time-To-Live (TTL) for an environment, but you can now set custom TTL policies per project to ensure that no resources are left behind.

## ✨ Setting Custom TTL Policies ✨

Many customers wanted to be able to set the Max and Default TTL policies to a custom value of their choice and not to be limited (pun intended) to the predefined set of durations.\
We added the ability to choose any TTL duration you want (Months, Weeks, Days, Hours). Those policies can be set at the Organization level or inside a specific Project.

<div style={{ textAlign: 'center' }}>
  <img src="https://mintcdn.com/envzero-b61043c8/U9rcMIDzc38oPcXx/images/changelogs/2023/02/organization_settings_new_ttls.png?fit=max&auto=format&n=U9rcMIDzc38oPcXx&q=85&s=a014d52b16835dceb8189bdb17233ce0" alt="Organization settings new TTLs" width="3012" height="1222" data-path="images/changelogs/2023/02/organization_settings_new_ttls.png" />

  <div>Organization settings new TTLs</div>
</div>

<div style={{ textAlign: 'center' }}>
  <img src="https://mintcdn.com/envzero-b61043c8/U9rcMIDzc38oPcXx/images/changelogs/2023/02/project_settings_new_ttls.png?fit=max&auto=format&n=U9rcMIDzc38oPcXx&q=85&s=171e15393f39ee45445faff76e8f96da" alt="Project settings new TTLs" width="2908" height="1954" data-path="images/changelogs/2023/02/project_settings_new_ttls.png" />

  <div>Project settings new TTLs</div>
</div>

Built with [Mintlify](https://mintlify.com).

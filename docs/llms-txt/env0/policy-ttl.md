# Source: https://docs.envzero.com/guides/policies-governance/policy-ttl.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure Policy TTL

> Set default and maximum time-to-live values for environments at organization or project level in env zero

When users create or redeploy an environment, they can set the environment's *time-to-live*. TTL Policies define the default and maximum *time-to-live* values for the environment.\
Those TTL limits do not apply to admins.\
*Administrators* can set the policies at Organization or Project level.

<Info>
  **The Maximum TTL limit is relative to the **creation** time of the environment and not to the time of any deployment.**
</Info>

<Frame caption="TTL policies on the Organization level">
  <img src="https://mintcdn.com/envzero-b61043c8/t0QBBK-2O7wlTUvX/images/guides/policies-governance/organization_level_ttl_policies_configuration.png?fit=max&auto=format&n=t0QBBK-2O7wlTUvX&q=85&s=410b07675517460a64e5d210a2e2610c" alt="Organization level TTL policies configuration" width="3012" height="1222" data-path="images/guides/policies-governance/organization_level_ttl_policies_configuration.png" />
</Frame>

On the Project level, you can choose to use the organization's settings or override them.

<Frame caption="TTL policies on the Project level">
  <img src="https://mintcdn.com/envzero-b61043c8/t0QBBK-2O7wlTUvX/images/guides/policies-governance/project_level_ttl_policies_configuration.png?fit=max&auto=format&n=t0QBBK-2O7wlTUvX&q=85&s=35fdf454240bbcf2856486d065477235" alt="Project level TTL policies configuration" width="2908" height="1954" data-path="images/guides/policies-governance/project_level_ttl_policies_configuration.png" />
</Frame>

<Info>
  **An infinite time-to-live means the environment will never be destroyed automatically. This is useful for static environments like staging or production, but is not recommended for development environments.**
</Info>

### Update Environment TTL

To update a specific environment's time-to-live definition, go to that environment's page, and in the info card, click on the pen icon near the Time Left label to update the TTL.

<img src="https://mintcdn.com/envzero-b61043c8/t0QBBK-2O7wlTUvX/images/guides/policies-governance/48a9cab-screenshot_2023-06-04_at_17.png?fit=max&auto=format&n=t0QBBK-2O7wlTUvX&q=85&s=50d25890a8c7c5a8d19a16e33dc7211a" alt="" width="1356" height="297" data-path="images/guides/policies-governance/48a9cab-screenshot_2023-06-04_at_17.png" />

<Info>
  **Notifications**

  Alert emails are automatically sent to the environment creator 3 times before the actual destroy command is triggered:

* 2 Days
* 2 Hours
* 30 Minutes
</Info>

Built with [Mintlify](https://mintlify.com).

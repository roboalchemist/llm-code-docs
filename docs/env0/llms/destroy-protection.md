# Source: https://docs.envzero.com/guides/policies-governance/destroy-protection.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Enable Destroy Protection

> Prevent accidental destruction of environments by enabling destroy protection per project in env zero

Enabling "Destroy protection" will prevent destruction of environments. The policy is configured per Project.

<img src="https://mintcdn.com/envzero-b61043c8/t0QBBK-2O7wlTUvX/images/guides/policies-governance/31c3f00-protected.png?fit=max&auto=format&n=t0QBBK-2O7wlTUvX&q=85&s=454313311415778d12c6133af81afd02" alt="" width="1708" height="666" data-path="images/guides/policies-governance/31c3f00-protected.png" />

The following features will be restricted:

* The Destroy button and Time Left indication in the Environment screen will be disabled.
* The TTL panel in Create/Redeploy Environment screen will be hidden.
* Scheduled Destroy will be disabled.

<Warning>
  TTL & Scheduled Destroy Reset

  For environments that existed before enabling destroy protection, TTL & Scheduled Destroy configurations will be deleted.
</Warning>

To enable "Destroy Protection", mark *Prevent destroy of environments in this project*. This can be found in each Project's Settings page, under the Policies tab.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/t0QBBK-2O7wlTUvX/images/guides/policies-governance/destroy_protection_policy_configuration.png?fit=max&auto=format&n=t0QBBK-2O7wlTUvX&q=85&s=aae6301489a941e5470d8aa9e037d781" alt="Destroy protection policy configuration" width="1514" height="676" data-path="images/guides/policies-governance/destroy_protection_policy_configuration.png" />
</Frame>

Built with [Mintlify](https://mintlify.com).

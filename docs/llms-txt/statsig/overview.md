# Source: https://docs.statsig.com/webanalytics/overview.md

# Source: https://docs.statsig.com/session-replay/overview.md

# Source: https://docs.statsig.com/segments/overview.md

# Source: https://docs.statsig.com/release-pipeline/overview.md

# Source: https://docs.statsig.com/product-analytics/overview.md

# Source: https://docs.statsig.com/integrations/mcp/overview.md

# Source: https://docs.statsig.com/integrations/data-imports/overview.md

# Source: https://docs.statsig.com/infra-analytics/overview.md

# Source: https://docs.statsig.com/http-api/overview.md

# Source: https://docs.statsig.com/feature-flags/overview.md

# Source: https://docs.statsig.com/experiments/overview.md

# Source: https://docs.statsig.com/dynamic-config/overview.md

# Source: https://docs.statsig.com/control-panel/overview.md

# Source: https://docs.statsig.com/autotune/overview.md

# Source: https://docs.statsig.com/ai-evals/overview.md

# Source: https://docs.statsig.com/access-management/sso/overview.md

# Source: https://docs.statsig.com/access-management/scim/overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SCIM User Provisioning

## Introduction

SCIM (System for Cross-domain Identity Management) is a standardized protocol that simplifies the automation of user provisioning and management across multiple platforms.
By integrating SCIM with your preferred Identity Provider (IdP), such as Okta,
you can securely and efficiently manage user creation, updates, and de-provisioning within Statsig.
We currently only offer an Okta SCIM integration.

## How To Obtain SCIM Auth Key

<Note>
  You must be a Statsig Organization Admin in order to enable SCIM.
  The SCIM key includes the `scim` prefix.
</Note>

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/WSul5JjdT4kF2k8h/images/okta_scim_steps/scim-access.png?fit=max&auto=format&n=WSul5JjdT4kF2k8h&q=85&s=54e1c43d1476b55ba6d577bde9bbc95f" alt="Statsig organization settings showing SCIM key management panel" width="1466" height="480" data-path="images/okta_scim_steps/scim-access.png" />
</Frame>

1. Navigate to Organization Access Management:
   Go to [Settings > Organization > Organization Info > Access Management](https://console.statsig.com/settings?tab=organization).
2. Generate a Key:
   If SCIM is not yet enabled, generate a new authentication key.
3. Deactivate the Key:
   To disable the key, select Deactivate.
4. Regenerate the Key:
   If you suspect the key has been compromised, you can regenerate a new one to replace it.

## Current SCIM Offering

### Okta

* **Push Users.** Assigning users to the Statsig application in Okta automatically adds the users as members of your organization in Statsig. Unassigning users deactivates them and wipes all roles/permissions.
* **Import Users.** Users in Statsig can be imported into Okta and either matched to existing Okta users, or created as new Okta users.
* **Import Groups.** Import project/team roles as groups in Okta. Note that imported groups cannot be modified in Okta.
* **Push Groups.** Groups can be pushed to Statsig to update user project/team roles.

[Okta Setup Guide](/access-management/scim/okta_scim_setup)


Built with [Mintlify](https://mintlify.com).
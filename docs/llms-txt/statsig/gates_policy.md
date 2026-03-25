# Source: https://docs.statsig.com/access-management/org-admin/gates_policy.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Feature Gates Policy

<Info>
  Organization level Feature Gate Policies are an Enterprise only feature.
</Info>

## Overview

Feature Gates Policy grants organization admins the ability to:

**Configure the Custom Fields leveraged in Feature Gate targeting:** With this setting, admins can pre-define allowed Custom Fields by ID type, add a description to provide more context on the Custom Field to end users, and pre-define the allowed values. Defining allowed values is optional.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/SnkiaVI10G4C2tMJ/images/access-management/org-admin/gates_policy/394b586d-22aa-45e9-96be-10ba2270c010.png?fit=max&auto=format&n=SnkiaVI10G4C2tMJ&q=85&s=3d6a9df12959268511afb52fb3945c21" alt="Organization gate policy page showing allowed custom fields per ID type" width="599" height="594" data-path="images/access-management/org-admin/gates_policy/394b586d-22aa-45e9-96be-10ba2270c010.png" />
</Frame>

**Configure allowed Targeting Criteria for Feature Gates:** With this setting, admins can select which targeting criteria will surface as options during gate creation for end users. These allowed targeting criteria are defined at the ID type as well, enabling you to, for example, create one set of targeting criteria for logged-in (UserID) vs. logged-out (stableID) feature rollouts.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/SnkiaVI10G4C2tMJ/images/access-management/org-admin/gates_policy/e94ca308-49e3-422f-ad42-3647dc910773.png?fit=max&auto=format&n=SnkiaVI10G4C2tMJ&q=85&s=2326e5ecaa8a5663617c122ad395f1e2" alt="Allowed targeting criteria configuration for feature gates by ID type" width="599" height="679" data-path="images/access-management/org-admin/gates_policy/e94ca308-49e3-422f-ad42-3647dc910773.png" />
</Frame>

**Require Templates for Gate or Dynamic Config Creation:** Enables admins to enforce that all gate or dynamic config creations are from a template. Restrictions on who can create/ edit templates (as well as which templates are allowed per-team) can be managed under **People** -> **Teams** and **Roles**

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/SnkiaVI10G4C2tMJ/images/access-management/org-admin/gates_policy/db0a74d4-a92a-4ae8-a82c-8b8cd409b251.png?fit=max&auto=format&n=SnkiaVI10G4C2tMJ&q=85&s=ede7fdfd40157fba5d24280ddba6a49e" alt="Requirement toggle enforcing templates for new gates or configs" width="1153" height="69" data-path="images/access-management/org-admin/gates_policy/db0a74d4-a92a-4ae8-a82c-8b8cd409b251.png" />
</Frame>

## Where can these be configured?

Organization Gate Policy can be managed in settings by visiting Product Configuration → Feature Management → [Organization tab](https://console.statsig.com/settings/feature_management?tab=org). Only organization admins have the ability to modify these settings.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/4jrx_wdABEVo0Z-t/images/organization_policies/gates_policy_3.png?fit=max&auto=format&n=4jrx_wdABEVo0Z-t&q=85&s=cc057e3c1b43d3e3fbf2a713fdfcb806" alt="Product Configuration settings highlighting Feature Management organization policies" width="3306" height="1290" data-path="images/organization_policies/gates_policy_3.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).
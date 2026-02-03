# Source: https://docs.crewai.com/en/enterprise/features/rbac.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.crewai.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Role-Based Access Control (RBAC)

> Control access to crews, tools, and data with roles, scopes, and granular permissions.

## Overview

RBAC in CrewAI AMP enables secure, scalable access management through a combination of organization‑level roles and automation‑level visibility controls.

<Frame>
  <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/users_and_roles.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=31b2661025e9813f32938f9d583228b5" alt="RBAC overview in CrewAI AMP" data-og-width="1365" width="1365" data-og-height="1044" height="1044" data-path="images/enterprise/users_and_roles.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/users_and_roles.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c3863373e71e9e7190b4e68024e82ad6 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/users_and_roles.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=e9bfbec405004555d4a862a97e29945e 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/users_and_roles.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=8b3c5a5d5a1ba5417537c6ae6cae8f1c 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/users_and_roles.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=50ba9cfdd73790c67ed3a7cce74d4f39 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/users_and_roles.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=aed9da1d5c9044e026f1674463f9adc2 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/users_and_roles.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=64a041f4e9ee05456c86d7259cef7e61 2500w" />
</Frame>

## Users and Roles

Each member in your CrewAI workspace is assigned a role, which determines their access across various features.

You can:

* Use predefined roles (Owner, Member)
* Create custom roles tailored to specific permissions
* Assign roles at any time through the settings panel

You can configure users and roles in Settings → Roles.

<Steps>
  <Step title="Open Roles settings">
    Go to <b>Settings → Roles</b> in CrewAI AMP.
  </Step>

  <Step title="Choose a role type">
    Use a predefined role (<b>Owner</b>, <b>Member</b>) or click{" "}
    <b>Create role</b> to define a custom one.
  </Step>

  <Step title="Assign to members">
    Select users and assign the role. You can change this anytime.
  </Step>
</Steps>

### Configuration summary

| Area                  | Where to configure                 | Options                                 |
| :-------------------- | :--------------------------------- | :-------------------------------------- |
| Users & Roles         | Settings → Roles                   | Predefined: Owner, Member; Custom roles |
| Automation visibility | Automation → Settings → Visibility | Private; Whitelist users/roles          |

## Automation‑level Access Control

In addition to organization‑wide roles, CrewAI Automations support fine‑grained visibility settings that let you restrict access to specific automations by user or role.

This is useful for:

* Keeping sensitive or experimental automations private
* Managing visibility across large teams or external collaborators
* Testing automations in isolated contexts

Deployments can be configured as private, meaning only whitelisted users and roles will be able to:

* View the deployment
* Run it or interact with its API
* Access its logs, metrics, and settings

The organization owner always has access, regardless of visibility settings.

You can configure automation‑level access control in Automation → Settings → Visibility tab.

<Steps>
  <Step title="Open Visibility tab">
    Navigate to <b>Automation → Settings → Visibility</b>.
  </Step>

  <Step title="Set visibility">
    Choose <b>Private</b> to restrict access. The organization owner always
    retains access.
  </Step>

  <Step title="Whitelist access">
    Add specific users and roles allowed to view, run, and access
    logs/metrics/settings.
  </Step>

  <Step title="Save and verify">
    Save changes, then confirm that non‑whitelisted users cannot view or run the
    automation.
  </Step>
</Steps>

### Private visibility: access outcomes

| Action                       | Owner | Whitelisted user/role | Not whitelisted |
| :--------------------------- | :---- | :-------------------- | :-------------- |
| View automation              | ✓     | ✓                     | ✗               |
| Run automation/API           | ✓     | ✓                     | ✗               |
| Access logs/metrics/settings | ✓     | ✓                     | ✗               |

<Tip>
  The organization owner always has access. In private mode, only whitelisted
  users and roles can view, run, and access logs/metrics/settings.
</Tip>

<Frame>
  <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/visibility.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=48e3dd12b9d55da6f7adc82ea80be56d" alt="Automation Visibility settings in CrewAI AMP" data-og-width="2028" width="2028" data-og-height="1498" height="1498" data-path="images/enterprise/visibility.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/visibility.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=382d272d44871f509846140dc972592e 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/visibility.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=6d6ba4cf2fcc360c7ce05266f5cc27e9 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/visibility.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b9fff488a36423a05ccb3f8e592ffd07 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/visibility.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=00471ecc85192b53abbcd64416e2b624 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/visibility.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=9008ee6b24abd22593938021d2093174 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/visibility.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=27fde319cbc6fae3e4c1e0a9044c264f 2500w" />
</Frame>

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with RBAC questions.
</Card>

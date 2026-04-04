# Source: https://help.aikido.dev/bug-bounty/setting-up-a-bug-bounty-program.md

# Setting Up a Bug Bounty Program

## Prerequisites

Before creating a Bug Bounty program, ensure you meet the following requirements:

* You need the **Can Manage Pentests** permission. See [setting-roles-and-permissions](https://help.aikido.dev/getting-started/automated-user-management/setting-roles-and-permissions "mention") for details on managing user access.
* The Bug Bounty feature must be enabled for your workspace. It is in **closed beta** right now, you can request access through intercom.

## Set up Bug bounty

{% stepper %}
{% step %}

### Create a Program

Navigate to **Bug Bounty** in the left navigation.

Click **Add Program** and enter a program name.
{% endstep %}

{% step %}

### Define the Scope

Define the target URL(s) for the program. This is what the AI agents will test against when a report is submitted.

{% hint style="warning" %}
**Use a test environment:** Bug Bounty assessments involve active testing against your application. To avoid impacting production users, point the scope at a staging or QA environment.
{% endhint %}
{% endstep %}

{% step %}

### Allowed Domains

Specify which domains are in scope and which are allowed to reach but not actively tested. Any domain not explicitly listed is blocked.

* **In scope:** Domains that will be actively tested by the AI agents.
* **Allowed to reach:** Domains the agents can interact with (e.g., authentication providers) but will not attack.
* **Blocked:** Everything else is blocked by default for safety.
  {% endstep %}

{% step %}

### Add Test Users

Configure test user credentials so the AI agents can authenticate when testing your application. You provide plain-English login instructions, no complex scripts required.

* **Define roles:** Create credential sets for different user types (e.g., `Admin`, `Standard User`). This allows the agents to test authorization logic across roles.
* **Write instructions:** Describe the login flow in plain English. For example:

```
Navigate to /login.
Enter email 'test@example.com' and password 'securepass'.
Click Sign In."
```

* **Multiple roles:** You can configure multiple roles to test privilege escalation and cross-role access.

For advanced authentication scenarios (2FA, magic links, OAuth), see [setting-up-authenticated-testing](https://help.aikido.dev/pentests/setting-up-authenticated-testing "mention").
{% endstep %}

{% step %}

### Code & Documentation

Optionally link repositories and upload OpenAPI specs or documentation to enable white-box analysis. Providing source code also unlocks the possibility to **automatically create fixes** for found vulnerabilities.
{% endstep %}

{% step %}

### Safety Measures

Configure request rate limits and allowed scanning hours to minimize the impact on your environment.

For more on safety controls, see [safety-measures](https://help.aikido.dev/pentests/safety-measures "mention").
{% endstep %}

{% step %}

### Summary

Review all your configuration choices and save the program. Once saved, the program is ready to receive reports.
{% endstep %}
{% endstepper %}

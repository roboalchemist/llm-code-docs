# Source: https://docs.socket.dev/docs/alert-purpose-definitions.md

# Alert Purpose Definitions

To maintain clarity and avoid redundant or conflicting signals, the following three labels serve distinct, non-overlapping communication roles in the alerting lifecycle:

| **Signal**   | **Purpose**                                                                                                                        | **Audience**                                   | **Based On**                                                          | **Customizable?**                            |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | --------------------------------------------------------------------- | -------------------------------------------- |
| **Severity** | Communicates how inherently dangerous an alert is, regardless of where it appears. This is Socket’s global risk signal.            | All users (Org Admins, Devs, Security)         | Public knowledge: CVSS, exploitability, malware, Socket threat models | ❌ No — set by Socket only                    |
| **Priority** | Reflects how relevant the threat is in the context of reachability, settings, code usage, environment, and policies.               | Security teams within the organization         | Severity + org-specific signals (e.g., reachability, config, triage)  | ❌ No —  organization-scoped                  |
| **Action**   | Communicates what developers should do. A workflow signal from Security to Engineering teams to guide urgency and effort required. | Developer teams (via PRs, tickets, dashboards) | Security team judgment, playbooks, policies                           | ✅ Yes — assigned by the org or security team |

<br />

**Severity**: A standardized signal from Socket that reflects the inherent risk of an alert across all organizations. It indicates how likely the alert could be exploited as a real threat. This rating is independent of any specific codebase, reachability, or organizational context. Severity is a global, objective assessment that does not change across environments.

**Priority**: A risk signal customized for each organization. It builds on Severity by including factors like reachability, usage, environment, policies, and triage input. Priority reflects how urgent or relevant the alert is for a specific organization. You can think of this as an organization’s internal version of Severity.

**Action**: A signal from Security teams to Developer teams that guides how much effort should be spent on fixing an alert. This is typically used during code reviews or pull requests. It reflects internal priorities and helps developers understand what needs attention and when.

No Overlap: Each label answers a different question.

* Severity: “How bad is this universally?”
* Priority: “How bad is this for us?”
* Action: “What should we do now?”

Customizability Boundaries:

* Severity and Priority are not customizable.
* Action is useful for customization and policy tuning.

Use in Practice:

* Security teams rely on Priority to triage at scale and automate actions.
* Developers rely on Action to know what’s expected of them without parsing complex risk context.
* Socket uses Severity to power risk analytics, threat detection, and dashboards at a consistent level across orgs.
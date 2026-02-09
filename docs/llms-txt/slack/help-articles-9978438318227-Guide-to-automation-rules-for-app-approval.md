# Guide to automation rules for app approval

When setting up [automated app approvals](https://slack.com/help/articles/9487088123411-Configure-automations-for-app-approval) for your organization, it's important to proceed with care and ensure that your rules meet any unique [security requirements](https://slack.com/help/articles/360001670528-Security-recommendations-for-approving-apps) established by your team. Read on for an overview of the components that make up rules and how to apply them.

**Note:** We recommend testing these features in a separate testing environment before implementing them in production. For additional support, you can [contact us](https://slack.com/help/requests/new) at any time.

## How it works

App installation requests can be automatically approved, restricted, dismissed, or flagged for human review based on conditions that your rules will look out for. Rules can be comprised of several rule components, which will be evaluated in the order that you determine. If the requested app meets the requirements of the rule, your predetermined resolution will be automatically applied.

## Terms to know

### Rule component

Components are what a rule looks out for to determine an automated outcome.

| Available components |
| --- |
| Scopes | Previous resolution | App distribution | App IDs |

### Conditions

Conditional statements modify how the component and comparison interact.

| Available conditions |
| --- |
| Is | Is not |

### Comparisons

Comparisons are the state of the rule component. Each component has its own set of available comparisons.

| Available comparisons |
| --- |
| Includes | Is empty | Approved | Restricted | Unresolved |
| Internal app | Slack Marketplace approved | Specific app ID |

### Resolutions

Resolutions determine how you'd like to action a requested app that contains all the elements of a rule.

| Available resolutions |
| --- |
| Restrict | Approve | Cancel | Review |

### Rules

The available components, conditions and comparisons are constructed into a conditional statement with a resolution, known as a rule:

| If any or all Component + Condition + Comparison then Resolution = Restrict Approve Cancel Review |
| --- |
| Scope Requested |
| Scopes Requested refers to all the scopes present in any requested app. |
| **Comparison** | **Rating list** |
| Includes any of those in | Low risk list |
| Includes only those in | Medium risk list |
| Is empty | High risk list |
| Is not empty | Unrated list |
| **Condition** | **Comparison** |
| Is | Approved |
| Is | Restricted |
| Is | Unresolved |
| Previous resolution is |
| Previous resolution is not |

| Previous resolution is approved, restrict |
| --- |
| **Condition** | **Comparison** |
| Is | Approved |
| Is | Restricted |
| Is | Unresolved |
| **Condition** | **Comparison** |
| Is not | Approved |
| Is not | Restricted |
| Is not | Unresolved |
| "If previous resolution is approved, approve" |

| App distribution is |
| --- |
| App distribution is internal |
| App distribution is Slack Marketplace approved |
| **Condition** | **Comparison** |
| Is | An internal app |
| Is | Slack Marketplace approved |
| **Condition** | **Comparison** |
| Is not | An internal app |
| Is not | Slack Marketplace approved |
| "If app requested is an internal app, send for review" |

| App ID is |
| --- |
| App ID is a specific app ID |
| **Condition** | **Comparison** |
| Is | A specific app ID |
| "If app ID is [any app ID], cancel" |

## Resolutions

When a requested app meets all the conditions of a rule, it will be resolved based on the set resolution and the requestor will be notified.

- **Restrict**: App cannot be installed and cannot be requested again unless the scopes change.
- **Approve**: App will be installed.
- **Cancel**: Dismiss the request without making a decision. A new request can be made anytime.
- **Review**: App will be sent to a human for review and approval.

**Who can use this feature?**

- **Workspace/Org Owners**, **Workspace/Org Admins** and **members** with [permission to manage apps](https://slack.com/help/articles/222386767-Manage-app-approval-for-your-workspace#choose-how-app-requests-work)
- Available on [**all plans**](https://slack.com/pricing)

**Awesome!**

Thanks so much for your feedback!

If you’d like a member of our support team to respond to you, please send a note to [feedback@slack.com](mailto:feedback@slack.com).

**Got it!**

If you’d like a member of our support team to respond to you, please send a note to [feedback@slack.com](mailto:feedback@slack.com).

**Was this article helpful?**
- Yes, thanks!
- Not really

**Sorry about that! What did you find most unhelpful?**
- This article didn’t answer my questions or solve my problem
- I found this article confusing or difficult to read
- I don’t like how the feature works
- Other

**Submit article feedback**

If you’d like a member of our support team to respond to you, please send a note to [feedback@slack.com](mailto:feedback@slack.com).
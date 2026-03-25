# Source: https://docs.axonius.com/docs/justification-types.md

# Justification Types

Learn about [Justifications](/docs/justifications) here.

This table lists all the justification types.

| Type                         | Description                                                                                                                                | Is Justified Value |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |
| Day 1                        | What the platform had noticed the moment the Identities was enabled. This doesn’t change the justification, only serves as an observation. | Null               |
| In-app Assignment            | In the latest fetch, the adapter detected that the entitlement was assigned internally within the connected application.                   | No                 |
| In-app Revocation            | In the latest fetch, the adapter detected that the entitlement was removed internally within the connected application.                    | No                 |
| Certified                    | An approver approved the entitlement as part of an Access Review campaign.                                                                 | Yes                |
| Uncertified                  | An approver rejected the entitlement as part of an Access Review campaign.                                                                 | No                 |
| Uncertified with Revocation  | An approver rejected the entitlement as part of an Access Review campaign, and asked that it would be immediately revoked.                 | No                 |
| Access Request               | An approver approved the entitlement as part of an Access Request ticket.                                                                  | Yes                |
| Admin Console Assignment     | The entitlement was manually granted by the admin of the platform from the UI.                                                             | Yes                |
| Admin Console Revocation     | The entitlement was manually removed by the admin of the platform from the UI.                                                             | No                 |
| Justified by Admin Console   | The entitlement was manually justified by the admin of the platform from the UI.                                                           | Yes                |
| Disapproval by Admin Console | The entitlement was manually rejected by the admin of the platform from the UI.                                                            | No                 |
| Automation Assignment        | The entitlement was automatically assigned by an EC/Workflow.                                                                              | Yes                |
| Automation Revocation        | The entitlement was automatically removed by an EC/Workflow.                                                                               | No                 |
| Disapproval by Automation    | The entitlement was automatically rejected by an EC/Workflow.                                                                              | No                 |
| Justified by Automation      | The entitlement was automatically approved by an EC/Workflow.                                                                              | Yes                |
| Rule Assignment              | The entitlement was granted by a rule (either internal or external).                                                                       | Yes                |
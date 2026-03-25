# Source: https://docs.axonius.com/docs/risk-score-settings.md

# Risk Score Overview

The **Axonius Risk Score** page offers a robust solution to assess threat levels and prioritize remediation efforts. Use this page to create multiple Risk Scores for different assets and scenarios, and to manage and edit them as needed.

The Risk Score calculation process takes into account risk, business impact, and exploitability considerations, and incorporates custom conditions and data normalization rules to allow for an accurate, transparent calculation process.

A key capability of the Risk Score module it is calculating Risk Score **across assets and Security Findings**, namely, to calculate the Risk Score of a specific vulnerability in the context of a specific asset. For example, you can compare the risk level of specific CVEs on a laptop with the risk level of the same CVEs on a desktop or a mobile device.

From the **Security Findings** page, click **Risk Score** to navigate to the Risk Score settings page.

<Image alt="RiskScoreButton" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-AWVB27XP.png" />

## Required Permissions

To create, edit and run Risk Scores, and edit Risk Score settings, the following [Enforcement Center Permissions](https://docs.axonius.com/docs/permissions-list#enforcement-center) are required:

| Permission                      | UI Page             | UI component                                                                    | Behavior (when permission is disabled)                |
| :------------------------------ | :------------------ | :------------------------------------------------------------------------------ | :---------------------------------------------------- |
| View Enforcement Center         | Risk Score          | Page                                                                            | Cannot access page                                    |
| Add Enforcement Center          | Risk Score          | **Add Asset** button on the left side panel                                     | Can change risk score details but cannot save         |
| Add Enforcement Center          | Risk Score          | **Quick Add (+)** button next to an asset item on the left side panel           | Can change risk score details but cannot save         |
| Add Enforcement Center          | Risk Score          | Create a new Risk Score                                                         | Can change risk score details but cannot save         |
| Add & Run Enforcement Center    | Risk Score          | **Save and Run** button                                                         | Can change risk score details but cannot save and run |
| Edit Enforcement Center         | Risk Score          | Edit a Risk Score                                                               | Can change risk score details but cannot save         |
| Edit & Run - Enforcement Center | Risk Score          | **Save and Run** button                                                         | Can change risk score details but cannot save         |
| Delete Enforcement Center       | Risk Score          | **Delete Risk Score** option in the **Risk Score Menu** of each Risk Score item | Can change risk score details but cannot save         |
| Edit - Enforcement Center       | Risk Score Settings | **Save** button at the bottom right                                             | Can change risk score details but cannot save         |

The following pages walk you through the Risk Score configuration process:

[Creating a Risk Score](/docs/creating-a-risk-score)

[Viewing Risk Score Results](/docs/viewing-risk-score-results)

[Previewing the Risk Score](https://docs.axonius.com/axonius-help-docs/docs/previewing-the-risk-score)

[Editing Enforcement Actions in a Risk Score](/docs/editing-enforcement-actions-in-a-risk-score)
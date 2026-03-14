# Source: https://doc.keepnetlabs.com/api-reference/reseller/reports.md

# Source: https://doc.keepnetlabs.com/next-generation-product/platform/reports.md

# Reports

This page offers a brief overview of the **Reports** menu, located on the left side of the platform. The **Reports** menu provides advanced reports related to the platform's products, which you can access from the links listed in the **Shortcuts** section below.

Additionally, this page includes important information on the metrics used in these reports, explaining how they are calculated and displayed. For a deeper understanding of these calculations, please refer to the "[Understanding Risk Scores](#understanding-risk-scores)" section.

## Shortcuts

* [How to create advanced high-level reports](https://doc.keepnetlabs.com/next-generation-product/platform/reports/advanced-reports)
* [How to create custom executive reports](https://doc.keepnetlabs.com/next-generation-product/platform/reports/executive-reports)
* [How to schedule reports](https://doc.keepnetlabs.com/next-generation-product/platform/reports/scheduled-reports)
* [How to view the gamification report](https://doc.keepnetlabs.com/next-generation-product/platform/reports/gamification-report)

## Test data is excluded from reports

**Mark as Test** (or **Marked As Test**) campaign and training report data is **not included** in platform reports. Specifically:

* **Simulation campaigns** (Phishing, Smishing, Quishing, Vishing, Callback): If a campaign is marked as "Mark as Test" when created or edited, its statistics are not used in dashboard widgets, Advanced Reports, Executive Reports, or risk score / KPI calculations.
* **Training reports (Awareness Educator):** If "Mark as Test" is selected when creating an enrollment, that training report's statistics are not included in platform reports or metrics.

Use test campaigns only for trial or demo purposes; they do not affect real KPI or reporting numbers.

## Understanding Risk Scores

This document explains the purpose and calculations of **Phishing Risk Scores** and **Human** **Cyber Risk Scores**. It details metrics used in phishing simulations (email phishing, smishing, quishing, vishing, and callback phishing) to evaluate user responses and assess training effectiveness.

Additionally, it outlines how these risk scores are calculated to identify and quantify risky behaviors during phishing simulations.

Please find the two types of risk score methods and their calculations below:

### Phishing Simulation Metrics Overview

This table categorizes and describes the key metrics used to evaluate user responses in different phishing simulation types. It serves as a comprehensive guide for understanding how individuals interact with various simulated phishing attacks, including email phishing, smishing, quishing, vishing, and callback phishing.

Each metric is linked to specific actions taken by users during these simulations, providing critical data for assessing the effectiveness of phishing awareness training programs.

| Simulation Type                               | Metric                | Description                                                                                                               |
| --------------------------------------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| <p><strong>Email Phishing</strong><br></p>    | Clicked Link          | Clicked the link in simulated phishing email.                                                                             |
| <p><br></p>                                   | Opened Attachment     | Opened the suspicious attached file in phishing email.                                                                    |
| <p><br></p>                                   | Submitted Data        | Submitted sensitive data on phishing landing page.                                                                        |
| <p><br></p>                                   | Submit MFA Code       | Submitted one-time code for Multi-Factor Authentication (MFA) on phishing landing page.                                   |
| <p><br></p>                                   | Phishing Reports      | Reported simulated phishing emails.                                                                                       |
| **Smishing**                                  | Clicked Link          | Clicked the link in simulated phishing SMS.                                                                               |
| <p><br></p>                                   | Submitted Data        | Submitted sensitive data on phishing landing page via SMS link.                                                           |
| <p><br><strong>Quishing</strong></p>          | Scanned QR Link       | Scanned a QR code that led to a phishing site.                                                                            |
| <p><br></p>                                   | Submitted Data        | Submitted sensitive data on phishing landing page.                                                                        |
| **Vishing**                                   | Answered Call         | Answered a call in a vishing attempt, engaging with the caller.                                                           |
| <p><br></p>                                   | Shared Sensitive Data | Disclosed sensitive information during a vishing call.                                                                    |
| <p><strong>Callback Phishing</strong><br></p> | Called Back           | Returned a call to a number provided in a phishing email as part of a callback phishing simulation.                       |
| <p><br></p>                                   | Entered Digits        | <p>Entered personal identification numbers or sensitive information in response to a callback request.</p><p><br><br></p> |

### How the Phishing Risk Score Is Calculated?

Keepnet calculates the Phishing Risk Score for a campaign based on identified risky behaviors.

Here are some of the risky behaviors that we detect during phishing simulations and use in the calculation for phishing risk scores.

<table><thead><tr><th width="278">Risk Behaviors</th><th>Low</th><th>Medium</th><th>High</th></tr></thead><tbody><tr><td>Click Phishing URL</td><td><br></td><td>x</td><td><br></td></tr><tr><td>MFA Code Sharing</td><td><br></td><td><br></td><td>x</td></tr><tr><td>Data Submit on Phishing Page</td><td><br></td><td><br></td><td>x</td></tr><tr><td>Open Attachment</td><td><br></td><td><br></td><td>x</td></tr><tr><td>Answer Voice Phishing Call</td><td>x</td><td><br></td><td><br></td></tr><tr><td>Share Sensitive Data on Voice Phishing Calls</td><td><br></td><td><br></td><td>x</td></tr><tr><td>Give unauthorized access to the system on the phone</td><td><br></td><td><br></td><td>x<br></td></tr><tr><td>Scan QR Code Phishing</td><td><br></td><td>x</td><td><br></td></tr><tr><td>Reply to phishing SMS</td><td><br></td><td>x</td><td><br></td></tr></tbody></table>

Suppose 100 individuals receive QR phishing emails, and 45 of them scan the QR code in the phishing email, this indicates that 45% of the employees engaged in a risky action. If 10 of those 45 individuals proceed to data submit on phishing page, the Phishing Risk Score Percentage for that campaign would rise to 55%.

Here's a step-by-step explanation for calculating the Phishing Risk Score Percentage:

1. **Total Target Users:** 100 employees receive a phishing email with a QR code to test their response to potential phishing threats.
2. **Initial Response:** 45 of these 100 employees scan the QR code, indicating a 45% initial failure rate due to this risky behavior.
3. **Further Risky Action:** Of those who scanned, 10 also submit data on the phishing page, demonstrating higher risk engagement.
4. **Final Risk Score Calculation:** Adding the submissions increases the Phishing Risk Score to 55%. This metric illustrates the percentage of at-risk employees, aiding in targeted cybersecurity training and enhancements.

{% hint style="info" %}
QR code phishing is used here as just one example; similar formulas can be applied to SMS, voice, callback, and email phishing simulations.
{% endhint %}

The following criteria are not included in calculating the phishing risk score:

{% hint style="info" %}

* Phishing activities belonging to IPs excluded from the campaign report or defined as a Sandbox activity will not be included in the calculation.
* Companies in the "test" group will not be included in the calculations.
* Campaigns marked as "Mark as Test" will not be included in these calculations.
* The users who opened the simulation email.
  {% endhint %}

### How is the Human Cyber Risk Score Calculated?

The Human Cyber Risk Score measures the percentage of users who exhibit risky behaviors during a phishing simulation.

Unlike the Phishing Risk Score, which counts each specific risky action, the Human Cyber Risk Score only identifies whether any risky behavior occurred, not how many times it happened. This score simply reflects the proportion of users who demonstrated at least one risky action.

The user shows at least one of the following risky behaviors:

<table><thead><tr><th width="282">Risk Behaviors</th><th>Low</th><th width="103">Medium</th><th>High</th></tr></thead><tbody><tr><td>Click Phishing URL</td><td><br></td><td>x</td><td><br></td></tr><tr><td>MFA Code Sharing</td><td><br></td><td><br></td><td>x</td></tr><tr><td>Data Submit on Phishing Page</td><td><br></td><td><br></td><td>x</td></tr><tr><td>Open Attachment</td><td><br></td><td><br></td><td>x</td></tr><tr><td>Answer Voice Phishing Call</td><td>x</td><td><br></td><td><br></td></tr><tr><td>Share Sensitive Data on Voice Phishing Calls</td><td><br></td><td><br></td><td>x</td></tr><tr><td>Give unauthorized access to the system on the phone</td><td><br></td><td><br></td><td>x</td></tr><tr><td>Scan QR Code Phishing</td><td><br></td><td>x</td><td><br></td></tr><tr><td>Reply to phishing SMS</td><td><br></td><td>x</td><td><br></td></tr></tbody></table>

This percentage is calculated by dividing the number of simulations where the user showed risky behavior by the total number of phishing simulations they received.

For instance, if a user displays risky behavior in one of three simulations, their Human Cyber Risk Score Percentage is 33%.

<table><thead><tr><th>Target User</th><th width="98">QR Phishing</th><th>Voice Phishing</th><th>SMS Phishing</th><th width="118">Human Cyber Risk Score Formula</th><th>Human Cyber Risk Score (%)</th></tr></thead><tbody><tr><td>Alex</td><td>No</td><td>No</td><td>Yes</td><td>(1 / 3) * 100</td><td>33%</td></tr><tr><td>Bob</td><td>Yes</td><td>Yes</td><td>No</td><td>(2 / 3) * 100</td><td>67%</td></tr></tbody></table>

This table demonstrates whether each individual displayed risky behavior in each type of phishing campaign and calculates their overall Human Cyber Risk Score.

A higher Human Cyber Risk Score suggests that the individual is more susceptible to falling for social engineering attacks.

{% hint style="success" %}
Reported phishing is a secure behavior that is not counted as a risky behavior.
{% endhint %}

### How is the Phishing Susceptibility Calculated?

Phishing susceptibility measures the percentage of users who engage in risky behaviors when engaged in simulated phishing tests. This metric helps organizations identify individuals more susceptible to social engineering tactics.

Unlike the traditional phishing risk score, which tracks the frequency of risky actions, phishing susceptibility determines whether a user has exhibited at least one risky behavior during a phishing simulation, regardless of how often it occurred.

#### Identifying Risky Behaviors

Phishing susceptibility is determined based on specific actions that indicate potential vulnerability to phishing threats. If a user performs at least one of the following risky behaviors, they are considered susceptible:

<table><thead><tr><th width="282">Risk Behaviors</th><th>Low</th><th width="103">Medium</th><th>High</th></tr></thead><tbody><tr><td>Click Phishing URL</td><td><br></td><td>x</td><td><br></td></tr><tr><td>MFA Code Sharing</td><td><br></td><td><br></td><td>x</td></tr><tr><td>Data Submit on Phishing Page</td><td><br></td><td><br></td><td>x</td></tr><tr><td>Open Attachment</td><td><br></td><td><br></td><td>x</td></tr><tr><td>Answer Voice Phishing Call</td><td>x</td><td><br></td><td><br></td></tr><tr><td>Share Sensitive Data on Voice Phishing Calls</td><td><br></td><td><br></td><td>x</td></tr><tr><td>Give unauthorized access to the system on the phone</td><td><br></td><td><br></td><td>x</td></tr><tr><td>Scan QR Code Phishing</td><td><br></td><td>x</td><td><br></td></tr><tr><td>Reply to phishing SMS</td><td><br></td><td>x</td><td><br></td></tr></tbody></table>

#### Calculation of Phishing Susceptibility

Phishing susceptibility is calculated by dividing the number of phishing simulations where the user displayed risky behavior by the total number of phishing tests they received.

For example, if a user engages in risky behavior during one out of three phishing attempts, their phishing susceptibility percentage is calculated as follows:

<table><thead><tr><th>Target User</th><th width="98">QR Phishing</th><th>Voice Phishing</th><th>SMS Phishing</th><th width="118">Formula</th><th>Phishing Susceptibility (%)</th></tr></thead><tbody><tr><td>Simon</td><td>No</td><td>No</td><td>Yes</td><td>(1 / 3) * 100</td><td>33%</td></tr><tr><td>Josh</td><td>Yes</td><td>Yes</td><td>No</td><td>(2 / 3) * 100</td><td>67%</td></tr></tbody></table>

The table above showcases whether each user fell for various phishing tactics and calculates their overall susceptibility.

## FAQ

### Q: How long does Keepnet retain and display reports on the platform?

A: As long as the customer maintains an active subscription with Keepnet, all reporting data is retained and accessible. Reports display data from the beginning of the customer's usage without any time limitations.

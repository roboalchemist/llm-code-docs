# Run a successful proof-of-value (POV) trial with Semgrep

Source: https://semgrep.dev/docs/run-a-successful-pov

- [](/docs/)- [What&#x27;s Semgrep](/docs/faq/overview)- Support &amp; resources- Run a successful trial with Semgrep**On this page- [Semgrep AppSec Platform](/docs/tags/semgrep-app-sec-platform)- [Support](/docs/tags/support)Run a successful proof-of-value (POV) trial with Semgrep
Start a POVTo start a proof-of-value (POV), contact Sales at [** sales@semgrep.com](mailto:sales@semgrep.com).

Run a POV to learn more about Semgrep solutions and receive support that is specific to your infrastructure and business needs. During a POV, you receive dedicated sales, engineering, and support resources to ensure that every Semgrep feature that supports your infrastructure is implemented quickly and reliably.

## POV requirements[​](#pov-requirements)
To run a successful POV, the Semgrep team needs your organization&#x27;s decisions regarding these factors:

- **The team involved in running the POV**

Who among your organization will be evaluating Semgrep? Semgrep creates accounts for everyone on the team who is involved in the POV.

- **The method to scan the repositories used in the POV**

**Recommended: Semgrep Managed Scans (SMS)**

This is the fastest way to deploy Semgrep to the repositories you want to scan. It requires access to your code, which can be limited to only certain repositories.

- **CI/CD**

This method relies on a CI configuration file, such as a GitHub Actions workflow file. A CI/CD job must be created for each repository you want to scan.

- **The technical resources**

You must decide on and communicate the repositories you want Semgrep to scan for the POV.
- You must decide on and communicate to Semgrep your account management, infra, and tech needs.

Benefits of Semgrep Managed ScansSMS is the **fastest** and **most scalable** deployment method, since it enables you to add repositories for scanning without the need for CI integrations. However, SMS requires access to your code.

## Summary[​](#summary)
The following table includes a short summary of the POV process.

StepActivitiesBoth parties agree to run a POV- Verify that your technical stack is supported by Semgrep.- Begin gathering necessary permissions from your organization for **technical resources** to run the POV.Pre-POV kickoff call and preparation- Both parties establish success criteria and alignment of the POV goals through a **kickoff call**.- Semgrep prepares for the POV by creating a dedicated Slack channel and other necessary accounts.Formal POV period- Semgrep deployment rollout.- Detection and remediation of findings.- Analysis of Semgrep ROI.Optional POV activities- A roadmap call with the Semgrep product team.- A rule-writing session where you can learn how to write custom Semgrep rules.POV conclusionSemgrep sets up a wrap-up call that discusses Semgrep&#x27;s performance and your feedback about Semgrep.
## General steps[​](#general-steps)
Running a POV involves the following steps:

- POV agreement between both parties
- Pre-POV or kickoff period
- Formal POV period
- POV conclusion

You can also participate in optional activities:

- Roadmap call
- Rule-writing session

Refer to the following sections for details.

### Both parties agree to run a POV[​](#both-parties-agree-to-run-a-pov)

- From your end (the buyer), a need has been identified and a budget has been allocated.
- From Semgrep&#x27;s end, the team has verified, with your help, that your technical stack is supported by Semgrep. This includes:

Programming languages
- Source code managers
- Account management
- Other factors

- **Optional**: If you&#x27;d like a **technical deep dive** of Semgrep from a sales engineer, you can request one through your account executive.
- Semgrep recommends that **the buyer (you) start gathering and gaining approvals** from your organization for resources needed to run the POV, such as repository access.

### Pre-POV stage[​](#pre-pov-stage)
#### Kickoff call[​](#kickoff-call)

- During the pre-POV kickoff call, both parties set **success criteria**.
- You and your organization can define the success criteria, or Semgrep can assist you in creating them.
- The pre-POV kickoff call ensures that all stakeholders are aligned for the goals of the POV.
- It also ensures that the technical requirements for both parties are clearly communicated.

#### Preparation for POV[​](#preparation-for-pov)
In preparation for the POV, Semgrep performs the following tasks:

- Sets up **one (1) trial license** for your organization.
- Sets up a **dedicated Slack channel** where you can reach out to the team during the POV.
- Creates an account in Semgrep AppSec Platform for your organization.
- Connects your source code manager, such as GitHub or Bitbucket, to Semgrep.
- Sets up SSO if you require it.
- For on-premise environments, Semgrep sets up the Network Broker to facilitate secure access between Semgrep and your private network.

### Formal POV period[​](#formal-pov-period)
This is a **two-week** period in which Semgrep assists you in deployment, scanning, triage, reporting, and all other related functions for a successful security program.

It is broken into three smaller phases.

#### Semgrep deployment rollout[​](#semgrep-deployment-rollout)
In this phase, the Semgrep team assists you in completing the following tasks:

- Add repositories for scanning through SMS or through a CI/CD job
- View findings in Semgrep AppSec Platform for scanned repositories within the POV&#x27;s scope
- Enable Assistant, ensuring that it&#x27;s analyzing full scan findings
- Prepare to set up pull request or merge request comments (PR or MR comments) and involve developers in Semgrep

#### Detection and remediation of findings[​](#detection-and-remediation-of-findings)
In this phase, the Semgrep team assists you in completing the following tasks:

- Review the quality of findings with out-of-the-box rules
- Show how Semgrep **filters out noise** with:

Assistant Memories and triage for Semgrep Code
- Direct and transitive reachability for Semgrep Supply Chain
- Secrets validation for Semgrep Secrets

- Improve developer experience through contextual, actionable vulnerability information:

Inline PR comments or MR comments
- Tailored remediation guidance in PR comments or MR comments
- Breaking changes and upgrade guidance for Supply Chain findings

- Integrate Jira for ticket creation and Slack for notifications if these are part of the success criteria

#### Semgrep return-on-investment[​](#semgrep-return-on-investment)
In the final phase, the Semgrep team provides you with data on the return on investment that Semgrep provides, compared to your existing security program.

Some metrics include:

- The number of developers in your company and the cost per developer per hour
- Number of hours **reduced** per developer, per year in triage time, research and fix time by having Semgrep Assistant provide autofix and triage recommendations
- Number of hours reduced in triage time per developer by having the ability to detect if secrets are valid or invalid
- Reduction in review time with Semgrep Supply Chain reachability analysis

### Optional POV activities[​](#optional-pov-activities)
Feel free to request the following:

- **Roadmap call**. You can request a call with the Product team to learn about Semgrep&#x27;s upcoming features and approaches.
- **Rule-writing session**. Learn how to write Semgrep rules to customize Semgrep for your organization&#x27;s unique code standards.

### POV conclusion[​](#pov-conclusion)
When the POV ends, Semgrep sets up a wrap-up call that discusses the following:

- Semgrep&#x27;s performance measured against the evaluation criteria
- Your feedback about Semgrep

## Trial license duration[​](#trial-license-duration)
The trial license duration lasts for 30 days.

## Appendix: common questions and evaluation criteria[​](#appendix-common-questions-and-evaluation-criteria)
Click to view a sample of common questions you and your team may ask to identify specific needs and criteria to evaluate Semgrep.

- **Feature set**

What features and language support do you need?
- How easy is it to set up a Semgrep POV environment?

- **Deployment**

Does Semgrep support your unique infrastructure or network needs?
- Does Semgrep support your SCM and CI provider? Can you easily deploy Semgrep through SMS?

- **Integrations and notifications**

Do the Semgrep integrations support your workflows for that tool? For example, does Semgrep support your custom fields in Jira?
- Are your custom workflows supported by the Semgrep API?

- **Findings and reports**

What percent of findings are true positives? How does this compare with previous tools?
- Is Semgrep Assistant (AI) able to reduce false positives?
- Does the dashboard assist you in tracking secure guardrails?

- **Security**

Can Semgrep handle your sensitive data securely?
- Can Semgrep successfully block PRs based on the criteria you need to set?

- **Support and documentation**

How easy is it to work with the Semgrep support team? Do they respond within the timeframe provided to you?
- Does the documentation provide you with a clear explanation of the product and features? Was it easy for you to find answers?

Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

Tags:**- [Semgrep AppSec Platform](/docs/tags/semgrep-app-sec-platform)- [Support](/docs/tags/support)[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/run-a-successful-pov.md)Last updated on **Nov 25, 2025**
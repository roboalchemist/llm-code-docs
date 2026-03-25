# Glow Documentation

Source: https://glow-docs.xrpl-commons.org/llms-full.txt

---

# Introduction

You are reading documentation for the Glow retroactive funding program.

## What is the Glow program?

Glow is an experimental funding program designed and run by XRPL Commons which aims to reward participants in the XRPL ecosystem retroactively.

This project builds on previous work by XRPL Commons and Kudos to identify ways to reward open-source software developers contributing to the XRPL ecosystem by identifying contributors algorithmically.

This project also builds on extensive consultation with community members and Ripple to design a funding program that complements existing funding offerings in the community, such as the Grants and Accelerator programs.

The program aims to initially reward work done [retroactively](https://glow-docs.xrpl-commons.org/program-information/core-principles/frequency), specifically meaningful contributions which have been made in the last six months.

This is an experimental program and documentation is subject to change while we fine tune it.

## How does it work?

The Glow program is run via a dedicated web application built with Nuxt.js, which has the following key features:

* Allows [Scouts](https://glow-docs.xrpl-commons.org/program-information/core-principles/glossary#scouts) to search for or create projects and contributors, then [nominate](https://glow-docs.xrpl-commons.org/program-information/core-principles/glossary#nominations) them for their valuable contributions to [eligible projects](https://glow-docs.xrpl-commons.org/project-eligibility)
* Provides a [voting](https://glow-docs.xrpl-commons.org/program-information/core-principles/glossary#votes) mechanism for XRPL wallet holders to connect wallets like Xaman or GemWallet or Crossmark, verify ownership, and cast votes on nominations
* Enables [Judges](https://glow-docs.xrpl-commons.org/program-information/core-principles/glossary#judges) to review nominations, assess eligibility criteria, and assign appropriate reward[ sizes](https://glow-docs.xrpl-commons.org/program-information/core-principles/shirt-size) (Small, Medium, or Large)
* Notifies contributors of their nominations and guides them through the application process
* Manages contributor applications including terms acceptance, eligibility verification, and XRPL wallet connection
* Facilitates KYC verification when required, for instance before any disbursement
* Handles disbursement through [Kudos](https://glow-docs.xrpl-commons.org/program-information/core-principles/glossary#kudos) integration, sending funds directly to verified XRPL wallets

## Transparency & Openness

The Glow program provides an open operating process through public documentation of all the workflows involved in the funding program. The platform is designed with transparency as a core principle, with clear roles and permissions for Scouts, Voters, Judges, and Contributors.

The platform tracks all nominations, votes, assessments, and grant decisions to ensure a transparent and auditable funds attribution process for all parties involved.

Please refer to the [key processes](https://glow-docs.xrpl-commons.org/program-information/key-processes) section for detailed information on specific workflows, and the [technical documentation](https://glow-docs.xrpl-commons.org/technical-resources) section for implementation details.

## Who can apply?

Contributors don't apply directly for funding but are nominated by Scouts. When nominated, contributors receive an email notification inviting them to complete an application on the Glow platform.

The application process includes:

1. Account creation or login
2. Terms acceptance
3. Eligibility verification
4. Wallet connection
5. Application form submission
6. KYC verification (if required)

Check out the [eligibility criteria](https://glow-docs.xrpl-commons.org/program-information/core-principles/eligibility) for detailed information on who can receive funding through the program.

## Platform Status (April 2025)

* **Current Cohort**: Cohort #1
* **Application Status**: Open for nominations
* **Shirt Sizes**: Small (\~50 XRP), Medium (\~750 XRP), Large (\~3000 XRP)
* **Supported Wallets**: Xaman (formerly XUMM), GemWallet, Crossmark

## Additional Resources

* [**Project Eligibility**](https://glow-docs.xrpl-commons.org/project-eligibility): Detailed criteria for eligible projects
* [**Technical Documentation**](https://glow-docs.xrpl-commons.org/technical-resources/platform-architecture): Platform architecture and implementation details
* [**User Guides**](https://glow-docs.xrpl-commons.org/user-guides/contributor-guide): Role-specific guides for platform participants


# Project Eligibility

Guidelines for determining what projects are eligible for funding through the Glow program.

## Overview

To qualify for funding through the Glow program, a project must align with the program's goal of supporting core protocol development and tools within the XRP Ledger (XRPL) ecosystem. Projects must be freely available to the community and demonstrate clear value to the broader XRPL ecosystem.

## Project Categories

The Glow platform recognizes contributions across multiple categories as implemented in the nomination process. When creating a nomination, Scouts can select from the following project categories:

### 1. Solving Technical Debt

Projects aimed at improving the maintainability and reliability of the XRPL codebase by addressing technical debt are eligible. This includes:

* Removing unused or redundant code
* Simplifying complex code structures for better readability and performance
* Writing unit, integration, and end-to-end tests to ensure code robustness
* Providing tools for code analysis, debugging, or optimization

### 2. Improving the Core Protocol

Contributions that enhance the underlying protocol of XRPL itself are eligible for funding. This can involve:

* Optimizing consensus algorithms for speed or efficiency
* Implementing security improvements or fixing protocol vulnerabilities
* Adding new features to the XRPL core that improve scalability, stability, or performance

### 3. Improving Existing Standards

Eligible projects may also focus on enhancing current XRPL-related standards, such as:

* Refining existing standards (e.g., transaction formats, account structures)
* Improving security, interoperability, or performance of established standards

### 4. Creating New Standards

Participating in the creation of new standards for the XRPL community is also fundable. This includes:

* Drafting and proposing new standards
* Collaborating with the community to define best practices

### 5. Improving Documentation or Creating Example Code

Educational and community-building contributions are essential for expanding XRPL adoption and understanding. Eligible projects include:

* Enhancing existing documentation to make it more accurate, comprehensive, or easier to follow
* Creating detailed tutorials, guides, or walkthroughs on XRPL functionalities
* Developing example code to help developers understand best practices or new features

### 6. Creating Community Tools

Tools that provide value to the wider XRPL community are considered fundable. Some examples are:

* Blockchain explorers that provide transparency and accessibility to data on the ledger
* Wallets or tools for managing XRP and other assets on the XRPL
* Analytical tools that provide insights into transaction patterns, account activity, or ledger performance

### 7. Supporting Infrastructure

Contributions to infrastructure that supports the XRPL ecosystem:

* Node deployment and scaling solutions
* Developer environments and testing frameworks
* Monitoring and alerting systems for XRPL networks
* Interoperability solutions with other blockchains

## Nomination Process

When submitting a nomination in the Glow platform, Scouts must:

1. Identify one or more existing projects in the platform or create new project entries
2. Provide a detailed description of the specific contribution being nominated
3. Select the appropriate project category that best describes the contribution
4. Explain how the contribution provides value to the XRPL ecosystem

## Evaluation Criteria

Judges evaluate project eligibility based on several factors:

* **Alignment with XRPL Ecosystem**: The project must contribute directly to the XRPL ecosystem
* **Open Access**: The contributions must be freely available to the community
* **Quality**: Code, documentation, or other contributions must demonstrate high quality
* **Impact**: The contribution must demonstrate meaningful impact or utility
* **Recency**: Contributions should have been made within the last 6 months
* **Unpaid Work**: The contribution should not have been previously funded or eligible for the Glow program.


# Key Processes

This section details the core workflows and processes involved in the Glow retroactive funding program. Each document explains a specific stage of the funding cycle from the perspective of both the platform and its users.

## Program Workflows

* [**Nominations**](https://glow-docs.xrpl-commons.org/program-information/key-processes/nominations)**:** How Scouts identify and nominate contributors for their work on eligible projects.
* [**Community Voting**](https://glow-docs.xrpl-commons.org/program-information/key-processes/community-voting)**:** The process for XRPL wallet holders to connect their wallets, verify ownership, and vote on nominations.
* [**Judging**](https://glow-docs.xrpl-commons.org/program-information/key-processes/judging)**:** How Judges evaluate nominations based on eligibility criteria, community votes, and contribution impact to assign shirt sizes.
* [**Recipient Application**](https://glow-docs.xrpl-commons.org/program-information/key-processes/recipient-application)**:** The steps contributors take after being nominated, including accepting terms, verifying eligibility, and connecting wallets.
* [**Disbursement**](https://glow-docs.xrpl-commons.org/program-information/key-processes/disbursement)**:** The process for distributing approved grants to contributors via their connected XRPL wallets, including KYC verification and payment processing.

***

For questions about any process, contact <info@xrpl-commons.org>.


# Nominations

Scouts nominate XRPL ecosystem contributors

## Scouts

Scouts are remarkable community members with an important online presence who regularly interact with the XRPL community.

Initially, Scouts were selected from active participants, including social media thought leaders, developer relations, and recipients of past XRPL Grants, XRPL Accelerator, and Aquarium programs.

Scouts can elect other Scouts, helping to grow the network of community advocates who identify valuable contributions to the XRPL ecosystem.

## How Nominations Work

Scouts log in to the Glow Platform and follow a guided two-step process to nominate contributors:

1. **Select or create project and contributor** - Scouts first select (or create) the project and contributor they wish to nominate
2. **Submit nomination details** - Scouts then provide detailed information about the contribution

### Project Management

#### Searching Projects

Scouts can search for existing projects on the platform. If the project doesn't exist, they can create a new one.

#### Adding New Projects

When adding a project, Scouts must provide:

* **Project name** (required): A unique name for the project
* **Project description** (required): A succinct summary of the project's main goals
* **GitHub repository** (required): The official project repository
* **X (Twitter) handle** (optional): The project's official X/Twitter account
* **Website URL** (optional): The project's website

### Contributor Management

#### Searching Contributors

Scouts can search for existing contributors on the platform by name. If the contributor doesn't exist, they can create a new profile.

#### Adding New Contributors

When adding a contributor, Scouts must provide:

* **First name** (required)
* **Last name** (required)
* **Email address** (required)
* **GitHub username** (required)
* **X/Twitter handle** (optional)
* **Contributor Since** (required): The date when the contributor started working on XRPL projects
* **Contributor Until** (optional): End date, if applicable

### Making a Nomination

#### Eligibility Screening

Before submitting a nomination, Scouts must verify:

* **Is the nominee over 18?** (required)
* **Is the nominee or any project team members located in a restricted region?** (Syria, Iran, Cuba, North Korea, or specific regions of Ukraine)
* **Is the nominee or any project team members on any Sanctions List?**
* **Is the nominee an employee at Ripple or an affiliated organization?** (XRPL Commons, XRP Ledger Foundation, etc.)

Contributors who fail any of these eligibility criteria cannot be nominated for funding.

#### Nomination Details

For eligible contributors, Scouts must provide:

* **Project category** (required): Select one or more categories that describe the contribution:
  * Solving Technical Debt
  * Improving the Core Protocol
  * Improving Existing Standards
  * Creating New Standards
  * Improving Documentation or Creating Example Code
  * Creating Community Tools
  * Others
* **Achievement description** (required): A detailed description of the specific contribution (max 2000 characters)

### Post-Nomination Process

1. **Community Voting**: Once nominated, the contribution becomes visible on the community voting platform
2. **Judge Review**: Judges will assess the nomination based on specific criteria including:
   * Verification the contributor is over 18
   * Confirmation they have genuinely contributed to the project
   * Verification the work was done recently
   * Confirmation the work was unpaid
   * Assignment of appropriate grant size
3. **Contributor Application**: Nominees receive an email invitation to apply for the grant
4. **Disbursement**: Approved nominees receive their grant after completing all required steps

### Nomination Management

Scouts can view all their submitted nominations for the current cohort, including:

* Contributor name
* Project name
* Contribution description
* Nomination date
* Current vote count

***

For questions about nominations, contact <info@xrpl-commons.org>.


# Community Voting

XRPL wallet holders can cast votes and support their favorite nominees.

## How It Works

Any XRPL account holder can participate in the program by voting for nominated contributors.

### Vote Activation

XRPL wallet holders must first connect their wallet to the platform using supported wallets. To cast votes, a wallet holder must prove ownership by signing a minimal one-drop transaction. This registration process enables the wallet holder to vote on all nominations for current and future cohorts.

Each wallet can cast only one vote per nomination.

### Types of Votes

Three types of votes can be cast:

* **Upvote (Yay):** +1, indicating support for the nomination
* **Downvote (Nay):** -1, indicating opposition to the nomination
* **Remove vote (Null):** Removes a previously cast vote

Users can change their vote at any time by clicking the voting buttons. The total community votes are tallied and displayed for each nomination, helping to inform the judges' evaluations.

## Impact of Voting

Community votes are used to evaluate nominated projects. For more details, see the [Judging section](https://glow-docs.xrpl-commons.org/program-information/key-processes/judging).

***

For questions about voting, contact <info@xrpl-commons.org>.


# Judging

Judges attribute shirt sizes to nominations.

Judges review nominations and community voting, assigning shirt sizes (small, medium, or large) to contributors based on the impact and eligibility of their work.

## Who Are the Judges?

Judges are experienced program administrators, initially selected from the XRPL Commons team. Over time, judges may be sourced from the pool of Scouts, with limits on consecutive cohort participation to ensure fairness and diversity.

## Size Determination

Before evaluating a nomination, Judges verify the [eligibility criteria](https://glow-docs.xrpl-commons.org/program-information/core-principles/eligibility) for each nominee by answering specific questions:

1. Is the contributor over 18? (Yes/No)
2. Has the nominee contributed to core infrastructure? (Yes/No)
3. Is the work recent (within 6 months)? (Yes/No)
4. Is it unpaid work? (Yes/No)

Each nomination in the active cohort is reviewed by at least three Judges.

Based on their assessment, Judges assign a shirt size:

* **Small:** Minor contributions or fixes
* **Medium:** Substantial improvements or features
* **Large:** Major contributions with significant impact
* **Decline:** Contributions that do not meet eligibility criteria

The size determination considers:

* The number of Scout nominations
* Community votes
* Contribution impact and quality
* GitHub activity and metrics

See [Shirt Size](https://glow-docs.xrpl-commons.org/program-information/core-principles/shirt-size) for more information on size determination criteria.

## Final Assessment

After individual assessments are submitted, the platform compiles all evaluations and presents them to Judges for a final review and consensus.

***

For questions about judging, contact <info@xrpl-commons.org>.


# Recipient Application

Nominees are notified to fill out a recipient application

Nominees must explicitly apply for the grant program. After a nomination, they are notified via email and instructed to apply through the Glow platform.

## Applying for the Glow Grant

Once nominated, contributors receive an email notification and are invited to apply through the Glow platform.

### Application Steps

The application process consists of several required steps, completed in sequence:

1. **Account Creation:** Create an account or log in with existing credentials.
2. **Terms and Documentation:** Review and accept the [Terms of Service](https://glow-docs.xrpl-commons.org/documents/terms-of-service) and [Code of Conduct](https://glow-docs.xrpl-commons.org/documents/code-of-conduct).
3. **Eligibility Confirmation:** Complete a questionnaire covering:
   * Age verification (must be 18+)
   * Location check (not in sanctioned regions)
   * Sanctions list verification
   * Employment status (not employed by Ripple or affiliated organizations)
   * Status check (not currently a Scout or Judge)
   * Funding verification (work was not previously funded)
4. **Wallet Registration:** Connect an XRPL wallet using supported providers (Xaman, GemWallet, etc.).
5. **Application Information:** Submit additional details:
   * Previous XRPL grants participation (Yes/No)
   * Previous XRPL accelerator participation (Yes/No)
   * Website (optional)
   * GitHub profile (optional)
   * X/Twitter account (optional)
   * Additional relevant information (optional)

After submitting the application, the information is reviewed by administrators before final grant approval and disbursement.

***

For questions about the recipient application process, contact <info@xrpl-commons.org>.


# Disbursement

How approved grants are disbursed to contributors

## Grant Disbursement Process

Once a contributor has been approved for funding through the judging process, the platform manages the disbursement of funds through the following steps:

### 1. Eligibility Verification

Before any funds can be disbursed, the system verifies that:

* The contributor has completed their application
* The nomination has been approved by judges
* Required KYC verification has been completed (if applicable)
* The contributor has connected a valid XRPL wallet

### 2. Shirt Size Determination

The final shirt size is determined based on:

* Judge assessments (Small, Medium, or Large grant designation)
* Multiple judge reviews to ensure fair assessment
* The most frequent assessment is typically used as the final determination

### 3. Payment Processing

The platform integrates with the Kudos system for payment processing:

* A Kudos pool is created for each cohort of approved nominations
* Each nomination is processed with its determined shirt size
* Contributors receive their grants directly to their registered XRPL wallet address
* The platform records transaction details for transparency and audit purposes

### 4. Notification

When disbursement is complete:

* Contributors receive an email notification about their grant payment
* The platform provides a record of the transaction for reference

***

For questions about disbursement, contact <info@xrpl-commons.org>.


# Core Principles

This section outlines the fundamental values and guidelines that shape the Glow program. These principles ensure fairness, transparency, and impact throughout the grant process. For details on each principle, see the documents below:

* [Eligibility](https://glow-docs.xrpl-commons.org/program-information/core-principles/eligibility)
* [Frequency](https://glow-docs.xrpl-commons.org/program-information/core-principles/frequency)
* [Shirt Size](https://glow-docs.xrpl-commons.org/program-information/core-principles/shirt-size)
* [Transparency](https://glow-docs.xrpl-commons.org/program-information/core-principles/transparency)
* [Glossary](https://glow-docs.xrpl-commons.org/program-information/core-principles/glossary)


# Glossary

These are terms frequently used throughout this documentation

#### **Cohorts**

Grants are compiled on a rolling basis but allocated in groups or cohorts. Each cohort is a collection of nominations over a given period, usually starting where the previous cohort ended and ending when the next cohort starts.

#### **Contributors**

Individuals who have made significant contributions to projects. Contributors should not have otherwise received funding for the task for which they are being nominated.

#### **Glow**

A retroactive funding program. Only past contributions are rewarded, ensuring the work has already been done and the community has received value.

#### **Judges**

Seasoned program administrators who review all data about a nomination and attribute a shirt size. Initially, judges are members of the XRPL Commons team, but over time, they will be sourced from existing Scouts for a maximum tenure of 6 cohorts in a row and never more than six cohorts a year. Typically, 3 Judges evaluate each project, and the combination of evaluations creates the final grants list.

#### **Kudos**

[Kudos](https://github.com/LoremLabs/kudos) is a service developed by Lorem Labs. Kudos is a new way for rewarding creation while keeping the best parts of the "free Internet". Kudos creates an *attribution economy* where end users record those who help them, and then later optionally fund their accounts with a monthly fee which will be proportionally distributed to all kudos attributions they generate for that month. Kudos is used under the hood by the Glow platform to reward XRPL econsystem contributors.&#x20;

#### **Nominations**

Once per cohort, Scouts can nominate contributors for the next grant wave. This enables community voting for this specific contribution and project. Several Scouts can nominate the same project, increasing the chance of a higher shirt size. The more Scouts nominate a project, the higher the nomination will be on the Judges' list.

#### **Projects**

Any product, tool, documentation, or other initiative provided to the XRPL ecosystem for free. These can be core open-source projects such as xrpld, explorers, wallets, standards proposals, or any resource made available to the community at no cost.

#### **Retroactive**

Glow is a retroactive funding program. Only past contributions are rewarded, ensuring the work has already been done and the community has received value.

#### **Scouts**

Remarkable individuals in the community who are typically visible and known, and have a chance to see many projects in their day-to-day. Scouts are entrusted with nominating meaningful contributions, making them part of a given cohort. Every Scout can occasionally elect other Scouts. You can view Scouts for a given cohort on the public Scouts page of the corresponding cohort.

#### **Votes**

XRPL wallet holders cast votes on nominations through the Glow platform. To vote, users must connect their wallet using supported providers like Xaman (formerly XUMM) or GemWallet or Crossmark, then register by signing a minimal 1 drop transaction to verify wallet ownership. This registration enables voting on all nominations in current and future cohorts.

A single wallet can cast one vote per nomination, which can be changed at any time. Three voting actions are available: upvote (+1), downvote (-1), or remove vote (0). The platform tracks and displays the total community score for each nomination, which helps inform judges' evaluations. Nominations with higher vote counts are typically prioritized during the review process.


# Reward Size

Like T-shirts, rewards come in three sizes, depending on the level of contribution: small, medium, and large.

## Overview

The Glow platform uses a standardized system for determining reward sizes. Judges evaluate each nomination against specific criteria and assign one of three reward sizes based on the contribution's impact, complexity, and effort.

## Grant Categories

### Small

Designed to acknowledge initial contributors or modest contributions. This grant expresses appreciation for participation and encourages further involvement. Typically awarded for bug fixes, minor improvements, or first-time contributions to the XRPL ecosystem.

### Medium

Intended to reward more significant contributions. This grant provides a substantial reward to support those making a notable impact within the XRPL ecosystem. Awarded for feature implementations, significant improvements, or ongoing maintenance of important projects.

### Large

Reserved for full-time contributors. This grant aims to support and incentivize sustained work on projects that advance the XRPL ecosystem. Awarded for major contributions that demonstrate exceptional impact, innovation, or technical excellence.

## Determination Process

Grant sizes are determined through a structured assessment process:

1. **Eligibility Check:** Judges first verify that the contribution meets the [eligibility criteria](https://glow-docs.xrpl-commons.org/program-information/core-principles/eligibility).
2. **Quality Assessment:** Each judge evaluates the contribution's technical quality, complexity, and impact.
3. **Community Impact:** Judges consider community votes and multiple Scout nominations.
4. **Consensus:** Multiple judges (typically three) review each nomination independently.
5. **Final Decision:** The most common assessment among judges determines the final shirt size.

| Size   | Description                                                                                                                                     | Grant Amount (XRP) |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| Small  | To reward initial contributions, encourage further engagement, or say thank you.                                                                | 50                 |
| Medium | To reward recurring contributions, and/or contributions that have a significant impact on the XRPL ecosystem.                                   | 750                |
| Large  | To reward large contributions that likely took full-time commitment and achieved excellence in a noteworthy contribution to the XRPL ecosystem. | 3,000              |


# Eligibility

These criteria determine who can receive a grant from the Glow Program

## Individual Contributors

The Glow funding program rewards individual contributors only. Companies and institutions are not eligible.

* Contributors must be over the age of 18.
* Contributors must not be located in restricted regions (Syria, Iran, Cuba, North Korea, or the Crimea, Donetsk, or Luhansk regions of Ukraine).
* Contributors must not be on any sanctions list or act on behalf of sanctioned individuals.
* Contributors must not be employees of Ripple, the Interledger Foundation, XRPL Commons, XRP Ledger Foundation, or any Ripple-affiliated organization.
* Contributors should not serve as Scouts or Judges in the cohort for which they are nominated.
* Nominations can only apply to contributions made in the last 6 months.
* The work must be unpaid (not already funded through other channels).
* Only one grant per individual can be allocated per cohort, but contributors can be nominated multiple times.
* Contributors must connect an XRPL wallet to receive funds.
* Some shirt sizes may require KYC verification before disbursement.

## Infrastructure and Core Protocol

Priority is given to projects that enhance the core infrastructure or protocol.

## Eligible Projects

Eligible projects include any product, tool, documentation, or other initiative provided to the XRPL ecosystem for free. These can be core open-source projects such as xrpld, explorers, wallets, or standards proposals, or any resource made available to the community at no cost.


# Frequency

Glow is meant to be a recurring funding program to support developer journeys over the medium term.

The goal of Glow is to reward both new and ongoing participation in the XRPL ecosystem. To achieve this, the Glow program disburses funds on a regular cadence, aiming for a half-yearly schedule.

## Eligibility Considerations

Glow is a retroactive funding program, designed to reward projects where value has already been at least partly realized and demonstrated.

Contributions are eligible for funding for up to 6 months from the time the contribution was made.

## Why is the Program Recurring?

The goal is to give contributors a clear path to make increasingly significant contributions to the XRPL ecosystem. Grant sizes are intended as stepping stones, starting from small and gradually increasing as the nominee gathers support and makes more impactful contributions.


# Transparency

The Glow project is open and transparent by default

## Cohort Transparency

For each cohort, the identities of Scouts and Judges are public.

Additionally, all nominations and their final assessments are made public.

To preserve the independence of Scouts and Judges, the specific actions taken by each individual are not disclosed. Only aggregate results are released.


# Frequently Asked Questions

Frequently Asked Questions about the Glow program

This comprehensive FAQ section addresses common questions about the Glow program, covering all aspects from eligibility to disbursement.

## General Questions

### What is the Glow program?

Glow is an experimental funding program designed and run by XRPL Commons which aims to reward participants in the XRPL ecosystem retroactively. It recognizes and rewards valuable contributions to the XRPL ecosystem that have already been completed and have demonstrated value.

### Why is it called "retroactive" funding?

Glow is retroactive because it rewards work that has already been completed, rather than funding future work. This ensures that the community has already received value from the contribution before funding is provided.

### How is Glow different from other funding programs?

Unlike traditional grants or accelerator programs that fund future work, Glow specifically rewards past contributions. It complements existing funding offerings in the XRPL ecosystem by focusing on recognizing work that has already provided value to the community.

### What types of projects are eligible for Glow funding?

Eligible projects include any product, tool, documentation, or other initiative provided to the XRPL ecosystem for free. These can be core open-source projects like xrpld, explorers, wallets, standards proposals, or generally anything made available to the community at no cost.

### How often are grants distributed?

Glow aims to distribute grants on a half-yearly basis. Grants are compiled and allocated in groups called cohorts. Each cohort represents nominations over a specific period.

## Roles & Participation

### What are the different roles in the Glow program?

There are four primary roles:

1. **Scouts**: Community members who identify and nominate potential contributors
2. **Community Voters**: XRPL wallet holders who can vote on nominations
3. **Judges**: Individuals who evaluate nominations and determine grant sizes
4. **Recipients**: Contributors who receive grants after being nominated and approved

### How do I become a Scout?

Scouts are remarkable individuals in the community who are typically visible and known and have a chance to see many projects in the course of their day-to-day. Existing Scouts occasionally have the power to elect new Scouts. You can view current Scouts on the public Scouts page for each cohort.

### How do I become a Judge?

Initially, Judges are members of the XRPL Commons team. Over time, they will be sourced from existing Scouts for a maximum tenure of 6 cohorts in a row and never more than six cohorts a year. There are typically 7 judges: 3 from XRPL Commons and 4 from the Community, elected for 6-month terms.

### Can I apply for a grant directly?

No. Grant recipients don't apply directly for funding but must be nominated by Scouts. If you believe your contribution deserves recognition, reach out to a Scout from the current cohort to discuss your specific contribution.

## Eligibility

### Who is eligible to receive Glow grants?

Glow grants are only for individual contributors, not companies or institutions. To be eligible:

* You must be over 18 years old
* You should not be a Judge in the cohort where you're a nominee
* Your contribution must have been made within the last 6 months
* You can receive only one grant per cohort
* Your contribution must be to an eligible project

### Can I receive a grant if I work for Ripple?

No. Current employees or contractors of Ripple or partnered organizations are not eligible for Glow grants.

### Can Scouts or Judges receive grants?

While Scouts can potentially receive grants, Judges cannot receive grants in cohorts where they serve as Judges. Individuals currently serving as Scouts or Judges for the Glow program should declare this status during the application process.

### Are projects that received other funding eligible?

Projects that were completed as part of paid work engagements or were otherwise funded by another program generally aren't eligible for Glow grants, as Glow aims to reward unpaid contributions.

### Can I be nominated for multiple contributions?

Yes, a contributor can be nominated multiple times by different Scouts, which may increase the chance of receiving a higher grant size. However, you can only receive one grant per cohort.

## Nomination Process

### How does the nomination process work?

Scouts connect to the Glow Platform and add projects and contributors if they don't exist yet. For each nomination, Scouts provide details about the contribution and when it was completed. Once nominated, community voting is enabled for that contribution.

### What information do Scouts need to provide when nominating?

For projects: name, description, GitHub repo, X handle, and website URL.\
For contributors: first name, last name, email, GitHub, X handle, role, active dates, and status.\
For nominations: description of the contribution and the date it was completed.

### Can I nominate myself?

No, you cannot nominate yourself. Nominations must come from designated Scouts.

## Voting

### How does voting work?

XRPL wallet holders can vote on nominated projects. To participate, wallet holders must first prove their wallet is active by signing a minimal one-drop transaction. Once verified, they can cast votes on all nominations in current and future cohorts.

### What types of votes can be cast?

Three types of votes can be cast: yay (counts as +1), nay (counts as -1), or null (counts as 0). A single wallet can cast only one vote per nomination per cohort.

### How do votes affect the grant decision?

Votes help inform the Judges' evaluation process. Projects with more community support (more positive votes) are prioritized for review.

## Grant Sizes

### What are the different grant sizes?

Glow grants come in three sizes, often referred to as "shirt sizes":

1. **Small (50 XRP)**: For initial contributions, to encourage further engagement, or to say thank you.
2. **Medium (750 XRP)**: For recurring contributions and/or those with significant impact on the XRPL ecosystem.
3. **Large (3,000 XRP)**: For extensive contributions that likely required full-time commitment and achieved excellence in a noteworthy way.

### How is the grant size determined?

Judges determine grant sizes based on the number of Scout nominations, community votes, GitHub activity, and the overall impact of the contribution. Each nomination is typically evaluated by at least 3 Judges, and the combined assessment determines the final grant size.

## Application Process

### What happens after I'm nominated?

If you're nominated, you'll receive an email notification inviting you to apply for a Glow grant through the Glow platform. You'll need to complete several forms to proceed with your application.

### What forms do I need to complete?

Recipients need to complete:

1. Terms and conditions acceptance
2. Code of conduct acceptance
3. Self-eligibility declaration
4. Application form completion

### Do I need to complete all forms for every nomination?

For your first nomination, you need to complete all forms. For subsequent nominations, only validation of the application form is required.

## KYC and Disbursement

### What is KYC and why is it required?

KYC stands for "Know Your Customer" and is a standard process to verify the identity of grant recipients. KYC, along with KYT (Know Your Transaction) and KYW (Know Your Wallet) checks, are required to ensure compliance with regulatory requirements.

### Who conducts the KYC process?

Kudos conducts the KYC verification process for all Glow grant recipients.

### How are grants disbursed?

Grants are paid exclusively in XRP tokens. Once your KYC is validated, funds are disbursed to your specified XRPL wallet address.

### What happens if I don't pass KYC?

If you don't pass the KYC verification process, you won't be able to receive the grant, and the funds will be reallocated to the next Glow wave.

### How long does disbursement take?

Full disbursement occurs upon successful KYC validation. The specific timeline may vary, but the goal is to process disbursements efficiently.

## Technical Issues and Support

### What if I encounter issues with the Glow platform?

For technical issues with the platform, please reach out to the support team via the contact information provided on the Glow website.

### How do I connect my XRPL wallet to the platform?

The platform provides a "Connect Wallet" option that guides you through the process of connecting your XRPL wallet for voting or receiving grants.

### What if I made an error in my wallet address?

It's crucial to double-check your wallet address when providing it. As stated in the terms, the recipient is fully responsible for any errors in the wallet address, and payments sent to incorrect addresses due to user error will still be considered complete.

## Transparency and Governance

### What information about the program is public?

For each cohort, the identities of Scouts and Judges are public, as are all nominations and their final assessment. To preserve the independence of Scouts and Judges, the specific actions they took are not disclosed - only aggregate results are released.

### How is the program governed?

The Glow program is designed and run by XRPL Commons. The governance structure includes designated Scouts and Judges who operate according to established principles of transparency and fairness.

### Can I provide feedback on the program?

Yes, feedback on the Glow program is welcomed and can help improve future cohorts. Please reach out through the official channels provided on the Glow website.


# Code of Conduct

## Introduction

The Glow program is committed to providing an inclusive, welcoming, and harassment-free experience for all participants, regardless of background, identity, or experience level. This Code of Conduct outlines our expectations for all community members—including contributors, scouts, judges, voters, and administrators.

By participating in the Glow program, you agree to abide by this Code of Conduct in all interactions, both online and offline, related to the program.

## Our Standards

Examples of behavior that contribute to a positive environment include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy toward other community members

Examples of unacceptable behavior include:

* The use of sexualized language or imagery
* Trolling, insulting, or derogatory comments; personal or political attacks
* Public or private harassment
* Publishing others' private information without explicit permission
* Any other conduct that could reasonably be considered inappropriate in a professional setting

## Responsibilities

### Scouts

* Nominate contributors based on merit, not personal relationships
* Provide accurate and honest descriptions of contributions
* Respect the privacy and preferences of those they nominate
* Disclose any potential conflicts of interest

### Judges

* Evaluate nominations objectively using consistent criteria
* Recuse themselves from assessing nominations where conflicts of interest exist
* Maintain confidentiality regarding deliberations and sensitive information
* Provide constructive feedback when requested

### All Participants

* Report any violations of this Code of Conduct to the Glow support team
* Cooperate with investigations into reported incidents

## Reporting and Enforcement

Violations of this Code of Conduct may result in warnings, removal from the program, or other actions as deemed appropriate by the Glow administrators.

To report a violation or concern, please contact <info@xrpl-commons.org>.

***

Thank you for helping to make the Glow community welcoming and respectful for everyone.


# Terms of Service

## Introduction

These Terms of Service ("Terms") govern your use of the Glow platform ("Platform"), operated by XRPL Commons ("we," "us," or "our"). By accessing or using the Platform, you agree to be bound by these Terms. If you do not agree with any part of the Terms, you may not access the Platform.

## Definitions

* **User:** Any individual accessing or using the Platform, including Scouts, Judges, Contributors, and Voters.
* **Contributor:** An individual nominated for their contribution to the XRPL ecosystem.
* **Scout:** An individual authorized to nominate contributors for grants.
* **Judge:** An individual authorized to evaluate nominations and determine grant allocations.
* **Voter:** An XRPL wallet holder who participates in the community voting process.
* **Grant:** A financial award in XRP tokens provided to eligible contributors.

## User Registration and Accounts

### Account Creation

To access certain features of the Platform, you must create an account. When creating an account, you agree to:

1. Provide accurate, current, and complete information
2. Maintain and update your information as needed
3. Keep your password secure and confidential
4. Accept responsibility for all activities that occur under your account
5. Notify us immediately of any unauthorized use of your account

### Wallet Connection

For voting and grant disbursement, you must connect an XRPL wallet to the Platform. By connecting your wallet, you:

1. Certify that you are the legitimate owner of the wallet
2. Agree to sign transactions necessary for verification and grant reception
3. Accept responsibility for maintaining the security of your wallet

## Platform Rules and User Conduct

### General Conduct

All users of the Platform agree to:

* Act respectfully and professionally in all interactions
* Comply with all applicable laws and regulations
* Not engage in fraudulent, abusive, or harmful behavior
* Follow the [Code of Conduct](https://glow-docs.xrpl-commons.org/documents/code-of-conduct)

## Termination

We reserve the right to suspend or terminate your access to the Platform at our discretion, including for violations of these Terms or the Code of Conduct.

## Changes to Terms

We may update these Terms from time to time. Continued use of the Platform after changes constitutes acceptance of the new Terms.

## Contact

For questions about these Terms, contact <info@xrpl-commons.org>.


# Platform Architecture

Technical overview of the Glow platform architecture and components

## Overview

The Glow platform is a modern web application built with Nuxt.js (Vue 3) to facilitate the retroactive funding process for XRPL ecosystem contributors. The platform connects Scouts, Contributors, Judges, Voters, and Admins in a streamlined workflow.

## Tech Stack

* **Frontend Framework:** [Nuxt.js](https://nuxt.com/) (Vue 3)
* **UI Components:** [@nuxt/ui](https://ui.nuxt.com/)
* **Styling:** Tailwind CSS
* **Server-Side:** Nuxt server middleware
* **Database:** MongoDB
* **Authentication:** Custom auth module with session-based authentication
* **XRPL Integration:** Wallet connectivity for voting and wallet registration

## Core Modules

### 1. Auth Module

Manages user sessions and role-based access control:

* Role management: Admin, Scout, Judge, Contributor, Voter
* Session persistence
* Route protection based on user roles
* Password management

### 2. Wallet Connectivity

Facilitates voting and wallet registration:

* XRP Ledger wallet integration
* Transaction signing
* Wallet address verification
* Support for multiple wallet providers (Xaman, GemWallet, Crossmark, etc.)

### 3. API Services

* RESTful endpoints for all platform operations
* Secure data access and validation
* Integration with external services (XRPL, KYC, etc.)

***

For technical questions or support, contact <info@xrpl-commons.org>.


# Application Workflow

Technical overview of the Glow application workflow

The Glow platform implements a structured workflow for retroactive funding of contributions to the XRPL ecosystem. This document provides a technical overview of the process from nomination to disbursement.

## Cohort Creation

A cohort represents a time-bounded collection of nominations processed together.

### Technical Implementation

Cohorts are managed through the `Cohort` model with key fields:

* `name`: Cohort identifier (e.g., "Cohort 1")
* `startDate`: When the cohort begins accepting nominations
* `endDate`: When the cohort closes (null for active cohorts)
* `status`: Current state of the cohort

Only one cohort can be active at a time. When a Scout creates a nomination, it is automatically associated with the currently active cohort (where `endDate` is null and `startDate` is in the past).

The admin interface allows administrators to:

* Create new cohorts
* Set start dates
* Close cohorts by setting end dates
* View all nominations within a cohort

## Nomination Process

### Step 1: Scout Authentication

Scouts authenticate using their credentials through the authentication module. Role-based access control ensures only Scouts can create nominations.

### Step 2: Project and Contributor Selection

#### Nomination Workflow

1. **Scout Authentication**
   * Scout logs in to the Glow platform
   * System verifies scout role permissions
2. **Project Management**
   * Scout searches for existing projects
   * **If project exists:**
     * Scout selects the existing project
   * **If project doesn't exist:**
     * Scout creates a new project with required details:
       * Project name
       * Description
       * GitHub repository
       * X handle
       * Website URL
3. **Contributor Management**
   * Scout searches for the contributor
   * **If contributor exists:**
     * Scout selects the existing contributor
   * **If contributor doesn't exist:**
     * Scout creates a new contributor record with:
       * First and last name
       * Email address
       * GitHub username
       * X handle
       * Role (creator, maintainer, contributor, editor)
       * Active dates
       * Status
4. **Nomination Creation**
   * Scout provides contribution details:
     * Description of contribution
     * Date of contribution
   * System creates nomination linking:
     * Selected contributor
     * Selected project(s)
     * Current cohort
     * Scout information

#### Workflow Diagram

```
Scout Login
    │
    ▼
Search Projects
    │
    ├─────────────┐
    │             │
    ▼             ▼
Project Exists?   Project Doesn't Exist
    │             │
    │             ▼
    │         Create Project
    │             │
    │             │
    ▼             │
Select Project    │
    │             │
    └──────┬──────┘
           │
           ▼
Search Contributors
           │
           ├─────────────┐
           │             │
           ▼             ▼
Contributor Exists?  Contributor Missing
           │             │
           │             ▼
           │      Create Contributor
           │             │
           ▼             │
   Select Contributor    │
           │             │
           └──────┬──────┘
                  │
                  ▼
          Create Nomination
```

> Note: The diagram above is a simplified representation of the workflow. In actual implementation, the system uses API endpoints for these operations.

The platform provides search functionality with API endpoints:

* `/api/projects/search` - Find existing projects
* `/api/contributors/search` - Find existing contributors

When creating new records:

* New projects are added through `/api/projects`
* New contributors are added through `/api/contributors`

### Step 3: Nomination Details

When submitting a nomination, the scout provides:

* Contribution description
* Contribution date
* Project category

The system automatically records:

* Cohort ID (active cohort)
* Nominator ID (scout)
* Timestamp

### Technical Implementation

Nominations are stored in the `Nomination` model with relationships to:

* `contributorId`: Reference to the Contributor being nominated
* `projectsIds`: References to Projects involved
* `cohortId`: Reference to the current Cohort
* `nominatorId`: Reference to the Scout making the nomination

## Voting Process

### Step 1: Wallet Connection

Voters authenticate by connecting their XRPL wallet. This integration occurs through:

1. Wallet provider selection (Xaman, GemWallet, Crossmark, etc.)
2. Connection via the corresponding wallet provider API
3. Address verification

### Step 2: Wallet Verification

To prevent spam, voters must prove wallet ownership by signing a small transaction (1 drop) to a designated verification address. This registration is stored in the `Voter` model.

### Step 3: Casting Votes

Voters browse nominations through public pages and can cast three types of votes:

* Yay (+1)
* Nay (-1)
* Null (0)

The voting system enforces one vote per nomination per wallet.

### Technical Implementation

Votes are stored in the `Vote` model with:

* `voterId`: Reference to the Voter
* `nominationId`: Reference to the Nomination
* `vote`: The vote value
* `timestamp`: When the vote was cast

API endpoints for voting:

* `GET /api/nominations/list` - View nominations
* `POST /api/votes` - Cast votes
* `PUT /api/votes/:id` - Update votes

## Judging Process

### Step 1: Judge Review

Judges review nominations with access to:

* Contribution details
* Project information
* Contributor information
* Community voting metrics

### Step 2: Assessment Creation

Judges evaluate nominations against eligibility and quality criteria:

1. Is the contributor over 18?
2. Has the nominee contributed to core infrastructure?
3. Is the contribution recent work (within 6 months)?
4. Is it unpaid work?

### Step 3: Reward Size Assignment

Based on their assessment, judges assign a shirt size:

* Decline (0)
* Small (1)
* Medium (2)
* Large (3)

Multiple judges assess each nomination, typically a minimum of three.

### Step 4: Final Approval

Once all nominations in a cohort have been assessed, judges conduct a final review and approve the distribution.

### Technical Implementation

Judge assessments are stored in the `JudgeAssessment` model:

* `nominationId`: Reference to the Nomination
* `userId`: Reference to the Judge
* `status`: 'approved' or 'declined'
* `criteria`: Object containing evaluation criteria results
* `comment`: Optional judge feedback
* `rejectionReason`: Required if status is 'declined'

Key judge-related API endpoints:

* `GET /api/nominations/metrics` - View nomination metrics
* `POST /api/judgeAssessments` - Create assessments
* `PUT /api/judgeAssessments/:id` - Update assessments
* `POST /api/nominations/actions/approve` - Approve final distributions

## Contributor Application Process

### Step 1: Notification

Contributors receive email notifications about their nominations.

### Step 2: Account Creation

If contributors don't have an account, the system facilitates account creation with the 'contributor' role.

### Step 3: Eligibility Verification

Contributors must complete an eligibility questionnaire covering:

* Age verification (18+)
* Sanctioned region check
* Affiliation checks (e.g., not a Ripple employee)
* Conflict of interest checks (not a scout or judge)

### Step 4: Terms Acceptance

Contributors must accept:

* Terms of Service
* Code of Conduct

### Step 5: Wallet Registration

Contributors register their XRPL wallet to receive funds.

### Step 6: Application Submission

Contributors complete their application with additional project details:

* Previous XRPL grants or accelerator participation
* Website, GitHub, and social media links
* Additional project information

### Step 7: KYC Verification

Contributors may need to complete KYC verification through the integrated verification service.

### Technical Implementation

The contributor journey is managed through:

* `Contributor` model with verification fields
* `KycVerification` model for KYC status
* API endpoints for:
  * Getting contributor status
  * Updating eligibility
  * Accepting terms
  * Registering wallet
  * Submitting application details

## Disbursement Process

### Step 1: Verification Check

The system verifies all requirements are met:

* Nomination approved by judges
* Contributor completed application
* KYC verification (if required)
* Valid XRPL wallet connected

### Step 2: Payment Processing

Payments are processed through XRPL transactions to the contributor's registered wallet.

### Step 3: Transaction Recording

All disbursements are recorded for transparency and audit purposes.

## Integration Points

The workflow integrates with several external systems:

### Email Service

* Used for notifications to contributors
* Account verification
* Status updates

### XRPL Network

* Wallet connectivity
* Transaction signing
* Payment disbursements

### KYC Provider

* Identity verification
* Compliance checks

## Security Measures

The workflow includes multiple security controls:

* Role-based access control
* Wallet signature verification
* Multi-judge approval requirements
* KYC verification
* Transaction validation


# User Roles & Permissions

Detailed explanation of user roles and permissions in the Glow platform

The Glow platform uses a robust role-based access control system with five distinct user roles. Each role has specific permissions and responsibilities within the platform ecosystem.

## Admin Role

Administrators have full system access and management capabilities.

### Permissions

* Create, edit, and delete users of all roles
* Manage cohorts (create, update, close)
* Access all platform data and metrics
* Configure system settings
* View audit logs
* Manage projects and contributors

### Responsibilities

* System oversight and maintenance
* User management and support
* Monitoring program integrity
* Managing cohort lifecycle
* Overseeing the grant disbursement process

## Scout Role

Scouts identify and nominate valuable contributions to the XRPL ecosystem.

### Permissions

* Create and manage nominations
* Create and edit project records
* Create and edit contributor profiles
* View nomination status and voting metrics
* Access personal profile settings

### Responsibilities

* Identify impactful projects and contributors
* Submit high-quality nominations
* Ensure nomination data accuracy
* Follow the [Glow Code of Conduct](https://glow-docs.xrpl-commons.org/documents/code-of-conduct)

### Nomination Process

1. Search for or create project records
2. Search for or create contributor profiles
3. Create a nomination with detailed contribution description
4. Monitor nomination status through voting and judging phases

## Judge Role

Judges evaluate nominations and determine grant allocations.

### Permissions

* Review all nominations in assigned cohorts
* Access voting statistics and community feedback
* Create and edit assessments for nominations
* Rate contributions according to defined criteria
* Approve final distributions

### Responsibilities

* Evaluating eligibility of nominations
* Reviewing contribution quality and impact
* Assigning appropriate shirt sizes (Small, Medium, Large)
* Providing feedback on contributions
* Participating in final assessment meetings
* Approving cohort distributions

### Assessment Criteria

Judges evaluate nominations based on:

* Eligibility (18+, not in sanctioned regions, etc.)
* Contribution to core infrastructure
* Recency of work (within 6 months)
* Whether work was unpaid
* Community votes and support
* Overall impact on the XRPL ecosystem

## Contributor Role

Contributors are developers who have been nominated for their valuable contributions to XRPL projects.

### Permissions

* Complete eligibility verification
* Submit grant applications
* Connect XRPL wallet for payments
* View application status
* Access personal profile settings

### Responsibilities

* Confirming eligibility status
* Accepting terms of service and code of conduct
* Providing accurate application information
* Connecting valid XRPL wallet for disbursements
* Completing KYC verification when required

### Application Process

1. Review and accept terms of service
2. Review and accept code of conduct
3. Complete eligibility questionnaire
4. Register wallet for fund reception
5. Submit application with additional project details
6. Complete KYC verification

## Voter Role

XRPL wallet holders who participate in the community voting process.

### Permissions

* Connect XRPL wallet to the platform
* Cast votes on nominations
* View public nomination details and metrics
* Monitor voting impact

### Responsibilities

* Evaluating nominations objectively
* Providing community input on contribution value
* Supporting deserving projects through votes

### Voting Process

1. Connect XRPL wallet to the platform
2. Verify wallet ownership through a small transaction
3. Browse and review nominations
4. Cast votes (yay, nay, or null) on nominations
5. Monitor voting impact on nomination prioritization

## Role Interactions

The Glow platform facilitates seamless interaction between these roles:

1. **Scouts** identify worthy contributions and create nominations
2. **Voters** provide community input through voting
3. **Judges** evaluate nominations and determine shirt sizes
4. **Contributors** complete applications and receive grants
5. **Admins** oversee the entire process and manage platform operations

Each role plays a vital part in ensuring that valuable contributions to the XRPL ecosystem are properly recognized and rewarded.


# Scout Guide

A comprehensive guide for scouts on using the Glow platform

This guide provides detailed instructions for Scouts on how to nominate valuable contributions to the XRPL ecosystem through the Glow platform.

## Introduction

As a Scout, you play a vital role in the Glow program by identifying and nominating impactful contributions to the XRPL ecosystem. Your nominations help direct funding to developers, encouraging ongoing development and innovation.

## Getting Started

### Accessing Your Account

1. **Log In:** Access the Glow platform at [glow.xrpl-commons.org](https://glow.xrpl-commons.org/login) using your credentials.
2. **Scout Dashboard:** After logging in, you'll be directed to your Scout dashboard.

### Understanding Your Role

As a Scout, you can:

* Create and manage nominations
* Add new projects and contributors to the system
* Monitor the status of your nominations
* View voting and assessment results

## The Nomination Process

### Step 1: Finding or Creating a Project

Before submitting a nomination, identify the project:

1. Navigate to the "Nominations" section and click "Add Nomination."
2. Search for the project by name.
3. If the project exists, select it from the search results.
4. If the project doesn't exist, click "New Project" and provide:
   * Project name (required)
   * Project description (required)
   * GitHub repository URL (required)
   * X/Twitter handle (optional)
   * Website URL (optional)

### Step 2: Adding a Contributor

If the contributor is not already in the system, add them by providing:

* First name (required)
* Last name (required)
* Email address (required)
* GitHub username (required)
* X/Twitter handle (optional)
* XRPL wallet address (optional)

### Step 3: Submitting a Nomination

1. Select the project and contributor.
2. Provide a detailed description of the contribution and its impact.
3. Confirm eligibility (age, location, employment, etc.).
4. Submit the nomination for review.

## Monitoring Nominations

* Track the status of your nominations from your dashboard.
* View community voting and judge assessments as they become available.

***

For questions or support, contact <info@xrpl-commons.org>.


# Judge Guide

A comprehensive guide for judges on evaluating nominations in the Glow platform

This guide provides detailed instructions for Judges on how to evaluate nominations and determine grant allocations in the Glow platform.

## Introduction

As a Judge in the Glow program, you play a critical role in determining which contributions receive funding and at what level. Your assessments directly impact fund distribution and the recognition of valuable work in the XRPL ecosystem.

## Getting Started

### Accessing Your Account

1. **Log In:** Access the Glow platform at [glow.xrpl-commons.org](https://glow.xrpl-commons.org/login) using your credentials.
2. **Judge Dashboard:** After logging in, you'll be directed to your Judge dashboard where you can see your current tasks.

### Understanding Your Role

As a Judge, you are responsible for:

* Reviewing nominated contributions
* Assessing their eligibility and impact
* Assigning appropriate shirt sizes
* Approving final distributions

## The Evaluation Process

### Step 1: Reviewing Nominations

1. Navigate to the "Evaluations" section from your dashboard.
2. You'll see a list of nominations requiring assessment, typically showing:
   * Contributor name
   * Project name
   * Brief description
   * Vote count
   * Assessment status

### Step 2: Assessing Eligibility and Impact

* Review the details of each nomination, including the contribution description, project information, and community votes.
* Verify eligibility (age, location, employment, recency, and funding status).
* Consider the impact and quality of the contribution.

### Step 3: Assigning Shirt Size

* Choose the appropriate shirt size (Small, Medium, Large, or Decline) based on your assessment and the [shirt size criteria](https://glow-docs.xrpl-commons.org/program-information/core-principles/shirt-size).
* Submit your evaluation for each nomination.

### Step 4: Final Review and Approval

* After all Judges have submitted their assessments, review the compiled results.
* Approve the final distribution list for the cohort.

***

For questions or support, contact <info@xrpl-commons.org>.


# Contributor Guide

A comprehensive guide for contributors in the Glow platform

This guide walks you through the process of completing your application as a contributor who has been nominated for a Glow grant.

## Introduction

Congratulations on being nominated for a Glow grant! This nomination recognizes your valuable contributions to the XRPL ecosystem. To proceed with your application and potentially receive funding, you'll need to complete several steps outlined in this guide.

## Getting Started

### Accessing Your Account

1. **Check Your Email:** You will receive an email notification when you've been nominated.
2. **Create or Access Your Account:**
   * If you're new to Glow, the email will contain instructions to set up your account.
   * If you already have an account, simply log in at [glow.xrpl-commons.org](https://glow.xrpl-commons.org/login).

### Your Dashboard

After logging in, you'll be directed to the contributor dashboard where you can see your nomination(s) and the application steps you need to complete.

## Application Steps

You must complete these steps in sequence to be eligible for funding:

### 1. Review and Accept Terms of Service

* Navigate to the "Terms of Service" section.
* Read the document carefully.
* Check the acceptance box at the bottom.
* Click "Accept Terms" to proceed.

### 2. Review and Accept Code of Conduct

* Navigate to the "Code of Conduct" section.
* Read the document and agree to abide by the community standards.
* Check the acceptance box and click "Accept Code of Conduct."

### 3. Complete Eligibility Questionnaire

* Answer questions about your age, location, employment, and funding status.
* Confirm you meet all eligibility requirements.

### 4. Connect Your XRPL Wallet

* Use a supported provider (Xaman, GemWallet, Crossmark, etc.) to connect your wallet.
* Follow the on-screen instructions to verify ownership.

### 5. Submit Additional Information

* Provide details about previous XRPL grants or accelerator participation (if any).
* Optionally, add your website, GitHub profile, or X/Twitter account.
* Add any other relevant information to support your application.

After completing all steps, your application will be reviewed by administrators. If approved, you will receive your grant directly to your registered XRPL wallet.

***

For questions or support, contact <info@xrpl-commons.org>.


# Program Documents

This directory contains the official documents and legal agreements for the Glow platform. These documents define the formal policies, procedures, and agreements that govern the operation of the Glow program and the relationships between all participants.

## Available Documents

### [Code of Conduct](https://glow-docs.xrpl-commons.org/documents/code-of-conduct)

Outlines the expectations for all participants in the Glow community—including contributors, scouts, judges, and voters. Adherence to this code is required for participation in the program.

### [Terms of Service](https://glow-docs.xrpl-commons.org/documents/terms-of-service)

The legal agreement between users and the Glow platform. It governs platform usage, account creation, wallet connections, and general program participation.

### [Self-Eligibility Criteria](https://glow-docs.xrpl-commons.org/legal-documents/documents/self-eligibility-criteria)

A detailed questionnaire and checklist that contributors must complete to confirm their eligibility for the Glow program. This includes age verification, geographic restrictions, sanctions compliance, and more.

### [Nominee Application Form](https://glow-docs.xrpl-commons.org/legal-documents/documents/nominee-application-form)

The formal grant agreement that successful nominees must complete to receive funding. It includes legal details about the grant amount, payment process, obligations, and conditions.

## Document Completion Process

As part of the application workflow, contributors must review and accept these documents at various stages:

1. The **Terms of Service** and **Code of Conduct** must be accepted during initial account creation.
2. The **Self-Eligibility Criteria** must be completed during the application process.
3. The **Nominee Application Form** is completed by approved nominees before grant disbursement.

All acceptances and submissions are recorded in the platform database for compliance and audit purposes.

***

For questions or support regarding these documents, please contact the Glow support team at <info@xrpl-commons.org>.


# Self-Eligibility Criteria

## Overview

Before receiving funding through the Glow program, all nominated contributors must confirm their eligibility by answering a series of questions designed to ensure compliance with program requirements and regulations.

## Eligibility Checklist

As part of the application process, contributors must verify the following criteria:

### Age Verification

* You are at least 18 years of age.
* The Glow program is not available to minors.

### Geographic Restrictions

* You are not located in, and are not a resident or national of:
  * Syria
  * Iran
  * Cuba
  * North Korea
  * The Crimea, Donetsk People's Republic, or Luhansk People's Republic regions of Ukraine

### Sanctions Compliance

* You are not on any sanctions list.
* You are not acting on behalf of or for the benefit of any person on a sanctions list.
* You are not the target of any sanctions laws.

### Affiliation Verification

* You are not an employee at:
  * Ripple
  * Interledger Foundation
  * XRPL Commons
  * XRP Ledger Foundation
  * Any other Ripple-affiliated or partnered organization

### Role Conflict Check

* You are not a Scout or Judge in the cohort for which you are nominated.

### Contribution Recency

* The contribution was made within the last 6 months.

### Funding Status

* The work was not already funded through other channels.

***

**Note:** Falsifying eligibility information may result in disqualification from the program.

For questions about eligibility, contact <info@xrpl-commons.org>.


# Nominee Application Form

## Overview

This document contains the official retroactive grant agreement that contributors must complete after being nominated and verified through the Glow platform. The agreement is presented to contributors only after they have:

1. Received a nomination from a Scout
2. Created an account on the platform
3. Completed the eligibility verification process
4. Connected their XRPL wallet

The application form collects the necessary legal information to process the grant payment and establishes the contractual relationship between the contributor and XRPL Commons. This includes personal details, wallet address verification, and acceptance of the grant terms.

## Application Process Integration

Within the Glow platform, this agreement is presented as a digital form with built-in validation. Contributors can:

* Review all terms before accepting
* Provide required personal information
* Verify their connected XRPL wallet address
* Digitally sign the agreement

Once submitted, the application is reviewed by administrators before final grant approval and disbursement.

***

## Retroactive Grant Agreement

**Between:**

XRPL Commons, a French association (*loi de 1901*), headquartered at 15, rue Alasseur, 75015 Paris, registered under number 923 128 151, represented by Mr. David BCHIRI, duly authorized for the purposes hereof (email: <david@xrpl-commons.org>),

*hereinafter referred to as the “Association”*

**And:**

*The grantee, as identified in the digital application form.*

***

*The remainder of this agreement is completed and signed digitally within the Glow platform. For questions, contact* [*info@xrpl-commons.org*](mailto:info@xrpl-commons.org)*.*


# Communication

All official communication material and copy for the Glow platform

This directory contains official communication materials and copy used in the Glow platform. These resources ensure consistent messaging and branding across all touchpoints with users.

## Communication Categories

### User Notifications

The Glow platform sends various notifications to users based on their roles and actions:

* **Scout notifications**: Updates on nomination status and reminders
* **Contributor notifications**: Nomination alerts, application requirements, and grant status updates
* **Judge notifications**: Review requests, cohort assignments, and approval requirements
* **Voter notifications**: Registration confirmations and voting impact updates

### Email Templates

Standard email templates used throughout the platform workflow:

* Nomination notifications to contributors
* Application completion reminders
* Eligibility verification requests
* Wallet connection instructions
* KYC verification requests (when applicable)
* Grant approval notifications
* Payment confirmations

### Website Content

The [website.md](https://glow-docs.xrpl-commons.org/legal-documents/documents/communication/website) file contains official copy for key website sections, ensuring consistent messaging about the program's purpose, processes, and benefits.

## Usage Guidelines

When communicating about the Glow platform:

1. Maintain a professional, inclusive tone
2. Use consistent terminology as defined in the [glossary](https://glow-docs.xrpl-commons.org/program-information/core-principles/glossary)
3. Clearly explain technical concepts when necessary
4. Provide specific next steps for users when applicable
5. Include relevant links to documentation for additional information


# Website Content

This is the copy for the landing page

\[Verification and Disbursement\
When nominated, contributors receive an email notification inviting them to complete their application on the Glow platform. The streamlined process includes:

1. **Eligibility Verification**: Answer questions confirming age (18+), location (not in restricted regions), sanctions compliance, and funding status
2. **Wallet Connection**: Connect your XRPL wallet securely to receive funds directly
3. **Application Submission**: Provide additional information about your contribution and background
4. **KYC Verification**: Complete KYC checks through our integrated verification system (required for certain shirt sizes)

Grants are disbursed through the Kudos system directly to your connected XRPL wallet once all verification steps are completed. The platform provides real-time status updates throughout the process.g page]\(<https://glow.xrpl-commons.org>)

## Welcome to Glow

Fostering a thriving XRPL developer community through rewards and recognition

### For the Aspiring Developer

Join a project, contribute valuable feedback, or correct a community repository. Your efforts are recognized and rewarded with a small grant of 400 XRP, setting you on a path of growth and community engagement.

### For the Dedicated Contributor

Glow encourages ongoing contributions to XRPL ecosystem projects. As you consistently innovate and collaborate, your contributions are recognized with medium grants of 4,000 XRP, building a reputation that attracts further opportunities.

### For the Core Maintainer

Take on a leadership role, implementing major features or maintaining critical infrastructure for XRPL projects. Your extensive experience and dedication are rewarded with a large grant of 14,000 XRP, recognizing your significant impact on the ecosystem.

### Long-term Vision

Glow aims to create a consolidated database of projects to inspire ongoing developer contributions, fostering a sustainable and innovative development ecosystem.

### Sourcing

Respected community members serve as Scouts, identifying and nominating valuable contributors to XRPL projects. Scouts include developer relations professionals, past grant recipients, and active ecosystem participants.

### Community-Driven Evaluation

XRPL wallet holders participate in the evaluation process by connecting wallets and casting votes on nominations. Each vote can be an upvote (+1) or downvote (-1), with the ability to change your vote at any time. Your participation helps identify the most impactful contributions and directly influences the judge assessment process.

### Transparent Assessment

Experienced judges review all nominations, considering community votes, contribution quality, and project impact to determine appropriate shirt sizes. The entire process is documented and transparent.

### Get Involved

#### For Contributors

Have you made valuable contributions to XRPL projects? Connect with a Scout to be considered for nomination in the next cohort.

#### For Voters

Connect your XRPL wallet to register as a voter and help recognize the most impactful contributors to the ecosystem.

#### For Scouts

Experienced community members can apply to become Scouts and help identify deserving contributors.

### Cohort Timeline

Each funding cohort follows a structured timeline:

* **Nomination Period**: Scouts identify and nominate contributors
* **Voting Period**: Community members cast votes on nominations
* **Assessment Period**: Judges evaluate nominations and determine shirt sizes
* **Distribution Period**: Approved grants are disbursed to contributors

[Apply Now](https://glow.xrpl-commons.org/login) | [Learn More](https://glow.xrpl-commons.org/about)

Continuous sourcing ensures each Glow wave follows the previous without interruption.

Projects are sourced both manually (via scouts and the community) and algorithmically (through GitHub pools, Kudos, social networks, etc.).

A contributor can be nominated multiple times by different scouts.

### Community Input

All sourced projects are visible on a dedicated website, allowing community members to support their favorites. Each wallet can support a project only once, and project prioritization is based on collected data and community engagement.

### Final Judging

\~7 Judges, distinct from the Scouts, oversee the final project evaluations.

3 judges from XRPL Commons and 4 from the Community, elected for 6-month terms based on a list proposed by Commons.

Judges review nominations continuously, with a minimum of 3 judges per project. They tier selected projects (S / M / L) based on community support, scout nominations, and GitHub activity.

Final meeting to review nominees and finalize award allocations.

### KYC and Disbursement

Phased disbursement ensures deliverability of projects.

Kudos conducts KYC to verify recipients.

Recipients are invited to apply: “You’ve been nominated to apply for a Glow Grant.”

Full disbursement occurs upon KYC validation, with undisbursed funds reallocated to the next Glow wave.

\
\\



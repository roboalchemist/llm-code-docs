# Source: https://glow-docs.xrpl-commons.org/readme.md

# Introduction

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

# Source: https://docs.snowflake.com/en/collaboration/guidelines-reqs-for-listing-apps.md

# Guidelines and requirements for listing Apps on Snowflake Marketplace

## Overview

These guidelines define the enforced standards for publishing applications—both Snowflake Native Apps and Connected Apps—on Snowflake Marketplace.

## Native Applications

### Publish on Snowflake Marketplace

When your application package is ready to be published on the Snowflake Marketplace, you must submit it to Snowflake for review and approval.

> **Note:**
>
> The approval process required to publish an app on the Snowflake Marketplace is in addition to the [automated security scan](../developer-guide/native-apps/security-overview.md) that is run when the DISTRIBUTION property of an
> application package is set to EXTERNAL. See [Snowflake Native App listing approval flow](provider-listings-workflows.md) for details.

Before creating a listing, verify that you understand the enforced requirements and ensure that your application package follows each requirement. If an application package does not follow these requirements, your submission may be rejected.

If you receive a rejection notification for the application package you submitted, make the recommended changes and resubmit your application package for approval.

### Standards for Snowflake Native Apps on Snowflake Marketplace

The Snowflake Native App functional review process ensures the quality of apps published on Snowflake Marketplace. To provide clarity into what is evaluated during this process, the following standards apply to all Snowflake Native Apps distributed through Snowflake Marketplace.

**Immediate utility**

The app functionality must be provided within the consumer account and the app must be operational once installed.

**Standalone**

Apps must deliver product experience on Snowflake and facilitate external requirements through Snowflake functionality.

**Data-centric**

Apps should be based on data-centric use cases that leverage data stored in Snowflake.

**Transparent, simple, and secure**

Apps must use Snowflake features to disclose the app’s resource and access requirements and simplify the configuration process for the consumer.

### Enforced standards

Snowflake uses the following requirements to determine if a Snowflake Native App meets the standards for publication on Snowflake Marketplace. These requirements are verified when you submit a listing with an attached application package to Snowflake Marketplace.

1. Immediate utility

   1. Apps must not be shell apps that advertise functionality. Apps must deliver the advertised functionality.
   2. Apps must include a clear framework and instruction for utilizing app functionality.
   3. Apps should not crash, freeze, or otherwise function abnormally.
   4. Apps must list all required credentials and providers must share required credentials with Snowflake at submission for testing.
   5. If apps are not immediately actionable, they must document the expected workflow for a consumer, allowing consumers to fully install and configure the app.
2. Standalone

   1. Apps must not be pass-through. For example, they must not redirect consumers to an external service to enable the app’s core
      functionality.
   2. App interfaces must be accessible after installation directly from Snowflake.
   3. Apps cannot use the Snowflake Marketplace as a distribution platform for cross-selling external applications or services.
   4. Apps that access external services and leverage user authentication should comply with the following standards:

      1. Apps may ask consumers to create a service user in their Snowflake account only to enable access to an external service.

         > 1. Acceptable authentication methods are Programmatic Access Tokens (PAT), OAuth, or key pair. The service user must be granted only the minimum permissions necessary for the app to function.
      2. Apps that require user authentication should never require the consumer to do the following for authentication:

         > 1. Input consumer’s Snowflake username and password.
         > 2. Create a private / public key and share the private key.
3. Data-centric

   1. Apps must leverage Snowflake data in one of the following ways:

      1. Share data from the app provider’s account.
      2. Use datasets from the Snowflake Marketplace.
      3. Access data in the consumer account.
4. Transparent and simple

   1. All account-level privileges and references that the app requires must be listed in the application package manifest file.
   2. All resource requirements for the Snowflake Native App must be listed in the [marketplace.yml](../developer-guide/native-apps/marketplace-file.md) file of the app. The app must create these resources as part of installation and setup.
   3. All account-level privileges and references listed in the application package manifest file must be requested from the consumer through Snowsight or the Python Permission SDK.
   4. Apps must provide a readme file. Apps that do not include a Streamlit or custom user interface must include the following information in the readme file:

      1. A description of what the app does.
      2. The steps the consumer must perform to configure the app after it is installed.
      3. The stored procedures and user-defined functions the app uses.
      4. The privileges the app requires.
      5. Example SQL commands that show consumers how to use the app.
   5. All required SQL commands must be delivered using Snowflake and formatted as code blocks.
   6. If the app provides sample data, you must include procedures on how to use the sample data.
   7. If an application package contains a Streamlit app but does not contain a readme file, you must configure a default [Streamlit
      app](../developer-guide/native-apps/adding-streamlit.md).

### Best practices when publishing a Snowflake Native App

In addition to the requirements for submitting an application package to Snowflake Marketplace, Snowflake also recommends the following best practices when publishing a Snowflake Native App:

* Ensure that all required files are uploaded to the named stage for the version of the app you are submitting, including:

  * The manifest file.
  * The setup script.
  * The README file.
  * Any external stored procedures or user-defined functions required by the application package.
  * Any Streamlit files required by the application package.
  * Any external source code, including Python, Java, etc.
* Ensure that the version of the app you are developing passes the [automated security scan](../developer-guide/native-apps/security-overview.md).
* Test the new version of your application package by creating the application object locally by using the [CREATE APPLICATION](../sql-reference/sql/create-application.md) command.

  * Do not add a new version to your application package or set the DISTRIBUTION property to EXTERNAL while you are developing and testing
    an app. These actions trigger the [automated security scan](../developer-guide/native-apps/security-overview.md). Instead, create the
    application object using [files on a named stage](../developer-guide/native-apps/installing-testing-application.md).
  * If your app includes a Streamlit app, test the application in Snowsight to ensure the Streamlit app works as expected.
  * Verify that interactions between the Streamlit app and Snowflake Worksheets are seamless and that the consumer does not have to navigate excessively between the two.
* Review all parts of a listing before submitting it for approval.
* Ensure that there are no typos or other textual errors in the listing, readme file, and Streamlit app.

### Recommendations for trial listings

* When an app trial listing expires, Snowflake automatically suspends the app to avoid consumers incurring extra compute costs to the consumer. Snowflake only suspends the objects owned by the app that are currently active. Snowflake does not modify the status of objects that are already suspended.
* When a trial listing is converted to a full or paid listing, Snowflake attempts to re-enable the app by resuming tasks, containers, and compute pools. Snowflake only resumes services and compute pools that have the `auto_resume` property set to false.

### Recommendations for apps with containers

* Compute pools should be set to automatically suspend in combination with Snowpark Container Services jobs to avoid idle compute nodes.
* For higher availability during upgrades and to reduce cold start latency, Snowflake recommends that you set the `MIN_NODES` parameter greater than 1.
* If connections across different services are required in the same app, use the DNS name of the service instead of configuring an external access integration.

### Recommendations for event sharing

* Providers should configure an app to emit log messages and trace events that conform to
  [supported event definitions](../developer-guide/native-apps/ui-consumer-enable-logging.md) to ensure that consumers understand what information is collected.
* Mandatory event definitions should be limited to the log messages and trace events required by the app. Excessive or unnecessary mandatory event definitions should be avoided.
* Adding new mandatory event definitions in a version upgrade must require the consumer re-enable event definitions for the app.
* Use the Python Permission SDK to allow consumers to share optional events.

## Connected Apps

Snowflake allows SaaS providers to list their Connected Apps on Snowflake Marketplace. Connected Apps are integrated SaaS applications that securely connect to a Snowflake customer’s account to read or ingest specified data as part of their workflow. Connected Apps enable consumers to interact with their Snowflake data directly through an external UI.

### Requirements to publish a Connected App on Snowflake Marketplace

* **Partner network tier:** Providers must be a member of the [Snowflake Partner Network (SPN)](https://www.snowflake.com/en/why-snowflake/partners/) and hold a **Select**, **Premier**, or **Elite** tier designation.
* **CSID requirement:** Each Connected App must use a Connection String Identifier (CSID) to enable full telemetry and usage tracking. Providers are encouraged to consolidate to a single CSID per application; however, multiple CSIDs are also supported where necessary. The CSID(s) must be initially submitted through SPN and will subsequently be required in your listing submission and verified during the review process.
* **Security transparency:** Providers must complete a short **Security & Data Handling Attestation** as part of the listing process.
* **Listing type:** All connected app listings must leverage a public, paid listing and fulfill deals using standard or private offers.

### Ongoing standards for Connected Apps on Snowflake Marketplace

1. **Ecosystem contribution:** Connected Apps should meaningfully contribute to the **Snowflake Data Cloud ecosystem**, helping drive data collaboration, consumption, or workload adoption.
2. **Active partnership:** Providers must be **active contributors** to the Snowflake ecosystem. To remain listed on the Marketplace, providers must maintain their standing within the Partner Network at the Select tier or above, and their application must continue to benefit the ecosystem. Snowflake may remove a listing if the provider is no longer contributing to the ecosystem (per Snowflake’s discretion) or no longer meets partner eligibility standards.

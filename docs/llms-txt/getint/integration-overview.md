# Source: https://docs.getint.io/guides/quickstart/integration-overview.md

# Integration Overview

An integration connects **two applications** and defines how items are synced between them. Each integration has its own configuration, mappings, filters, and execution rules. This page explains how integrations are structured and how they work behind the scenes.

### **Integration Sections**

Each integration contains several configuration areas:

#### **Applications Icons**

Displays the two applications connected by this integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FHsVrUruq7upLIXIAuFKl%2FDisplaying%20the%20two%20icons%20that%20are%20part%20of%20the%20integration.png?alt=media&#x26;token=7909ee78-d677-4596-be5d-0c585459f30a" alt=""><figcaption></figcaption></figure>

It is also possible to change the connection and use a Query or JQL for advanced filtering by clicking the icons. See the documentation:[Filtering Items for Integration in Getint](https://docs.getint.io/getintio-platform/workflows/filtering-items-for-integration-in-getint) and [How to Use JQL Filters for Jira Integrations](https://docs.getint.io/getintio-platform/workflows/how-to-use-jql-filters-for-jira-integrations).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FfzCZgfCzamwLDCmzatYQ%2FChanging%20the%20connector%20or%20using%20a%20JQL%20query.png?alt=media&#x26;token=0648942e-86e2-4455-94c6-2a291b375875" alt=""><figcaption></figcaption></figure>

#### **More**

Here, you can access and control the integration interval between runs (Onpremise and Data Center deployments), the trigger behavior, ownership, and other execution rules. You can also disable the integration and export it.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FfqSEvhxuokr3HnQC7Ta7%2FMore%20options%20in%20Getint.png?alt=media&#x26;token=44a22645-8c2c-473c-9dca-062f4f2409ed" alt=""><figcaption></figcaption></figure>

Under this section, you will also find **Advanced Configuration.** It includes scripting options and advanced logic for cases that require customization. You can discover more about [Advanced Scripting](https://docs.getint.io/getintio-platform/advanced-scripting) or [contact us](https://getintio.atlassian.net/servicedesk/customer/portals) for help.

#### **Items Filtering**

Allows you to filter which items should be synced.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FF8v32YDCmAh4HxmGXGB3%2FOpening%20the%20UI%20filters.png?alt=media&#x26;token=b90f9d2f-a48d-4a38-8059-5a77d774d203" alt=""><figcaption></figcaption></figure>

You can include or exclude items based on fields, conditions, or specific values. For more details on how to use the filters, check our documentation: [Filtering Items for Integration in Getint](https://docs.getint.io/getintio-platform/workflows/filtering-items-for-integration-in-getint).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FXGz6mWhYvtwMwuis6f8z%2FFiltering%20options%20in%20Getint.png?alt=media&#x26;token=4490cf3b-6a6d-4b7e-ab36-fe577fe13026" alt=""><figcaption></figcaption></figure>

#### **Integration Name**

If a name is not provided, Getint will give it a generic name with the creation date when selecting "Create." The name can be changed at any time.

Here you can also see the status, integration owner, the date of creation, and the access it was given.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMPMrPd4WiRcG653ScXcB%2FIntegration%20name%20and%20creation%20data.png?alt=media&#x26;token=e01e0723-fb00-4df9-9b54-08c2f1b24f46" alt=""><figcaption></figcaption></figure>

#### **Type Mapping**

Defines how item types from one application translate into work item types in the other.

Within Type Mapping, you can:

* **Map work item types** between both applications.
* **Copy configuration** to reuse the same mapping settings.
* **Disable** a mapping without removing it.
* **Access to edit** the field mappings.
* **Delete** a mapping.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FjE7H7xAjgb70Jyown27d%2FType%20mapping%20and%20copy%20configuration.png?alt=media&#x26;token=86f81005-f49b-4f90-9f21-d6e38fc9a0b4" alt=""><figcaption></figcaption></figure>

#### **Migration Configuration**

Used when migrating existing or legacy items between applications. See more about migration options and configurations on our guides: [Migration Guides](https://docs.getint.io/guides/migration).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FcEQsr250w5cg8JYrUdIW%2FMigrate%20data%20with%20Getint.png?alt=media&#x26;token=c7ca46b5-6646-420c-8a59-dbcf03dbbe9a" alt=""><figcaption></figcaption></figure>

## **Structure of an Integration**

Integrations are built around **Type Mappings**.

A type mapping tells Getint how to translate a Work Item type from one system when it’s created or updated in the other.

**Example**

Jira might use (not limited to):

* Task
* Bug
* Story

Azure might use (not limited to):

* Task
* User Story
* Issue

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FbUYdXuGwIidUjNrOcBxg%2FMapping%20issue%20types.png?alt=media&#x26;token=df2c3fa6-8e7a-4641-bb97-6e909a3b9daa" alt=""><figcaption></figcaption></figure>

If you want an *Issue* in Azure to create a *Bug* in Jira, you simply map **Issue → Bug**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fp8Usj8r6v9tCf5VhzFvC%2Fmapping%20task%20to%20bug.png?alt=media&#x26;token=6e261e48-0aa7-43fa-b5a2-0934242c2ca0" alt=""><figcaption></figcaption></figure>

Work items that are **not** included in any mapping will **not** be synced.

Here, you can also use the [**Quick Build**](https://docs.getint.io/getintio-platform/quick-build) to facilitate the mapping of work items and fields, map [dependencies](https://docs.getint.io/guides/integration-synchronization/jira-azure-devops-integration/syncing-dependencies-between-jira-and-azure-devops-using-getint), and [manage the fields](https://docs.getint.io/guides/integration-synchronization/how-to-map-fields).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9Mfdaj8e1Sr6ChwEqmRF%2FChecking%20features%20that%20complement%20the%20issue%20types.png?alt=media&#x26;token=185dd910-3ff6-43dd-8668-ba5c583c165d" alt=""><figcaption></figcaption></figure>

### **Mapping Multiple Types Into One**

You can map several item types on one side into a single type on the other.

Example:

* Jira *Bug*, *Task*, and *Story* → *Azure Issue*

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FtBy0XPfmQra09JAW3tuE%2Fmapping%20multiple%20types%20into%20one.png?alt=media&#x26;token=ccc552f9-9bb9-47df-9d82-ed1198f1a5ea" alt=""><figcaption></figcaption></figure>

When Azure needs to create the corresponding Issue, Getint uses the **first matching work item type** from the top of your mapping list.

## **How Integrations Run**

Integrations run automatically based on the interval defined in **Settings** (For Cloud users, the minimum interval is 180 seconds).

Here’s how the execution works:

1. Getint checks the integration run interval in Settings.
2. When the scheduled time is reached, the integration starts.
3. For each connected application, Getint looks for all changes since the **last run**.
4. Only items that match your Type Mappings, Filtering Rules, and Sync Logic are processed.
5. Each execution is logged and can be viewed in **Reporting → Runs**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FNZuXmkcaaRUYJ94xml2w%2FChecking%20the%20Reporting.png?alt=media&#x26;token=ac55db77-e7f7-4b32-bb45-ea219d4e3b93" alt=""><figcaption></figcaption></figure>

This provides a clear record of what happened, when it occurred, and which items were synced.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fxm6U4lVvjDE0UC8vMeAn%2FChecking%20the%20sync%20history%20in%20Reporting.png?alt=media&#x26;token=5268c61a-b0ca-49b5-ad4b-b3cb75fe2970" alt=""><figcaption></figcaption></figure>

### **Need Help?**

If you have questions while setting up your integration, or if something doesn’t behave the way you expect, feel free to reach out. Our support team is happy to help you troubleshoot, review your configuration, or point you in the right direction. Contact us directly through our [help page](https://getintio.atlassian.net/servicedesk/customer/portals).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

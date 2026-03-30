# Source: https://docs.aws.amazon.com/appstudio/latest/userguide/llms.txt

# AWS App Studio User Guide

- [What is AWS App Studio?](https://docs.aws.amazon.com/appstudio/latest/userguide/welcome.html)
- [Concepts](https://docs.aws.amazon.com/appstudio/latest/userguide/concepts.html)
- [How App Studio works](https://docs.aws.amazon.com/appstudio/latest/userguide/how-it-works.html)
- [Supported browsers](https://docs.aws.amazon.com/appstudio/latest/userguide/supported-browsers.html)
- [Quotas](https://docs.aws.amazon.com/appstudio/latest/userguide/quotas.html)
- [Document history](https://docs.aws.amazon.com/appstudio/latest/userguide/doc-history.html)

## [Setting up and signing in to App Studio](https://docs.aws.amazon.com/appstudio/latest/userguide/setting-up.html)

- [Creating and setting up an App Studio instance for the first time](https://docs.aws.amazon.com/appstudio/latest/userguide/setting-up-first-time-admin.html)
- [Accepting an invitation to join App Studio](https://docs.aws.amazon.com/appstudio/latest/userguide/setting-up-signing-in.html): Access to App Studio is managed by IAM Identity Center.


## [Getting started](https://docs.aws.amazon.com/appstudio/latest/userguide/getting-started.html)

- [Tutorial: Generate an app using AI](https://docs.aws.amazon.com/appstudio/latest/userguide/getting-started-tutorial-ai.html): Learn about App Studio by following a step-by-step tutorial to generate an app using AI.
- [Tutorial: Start building from an empty app](https://docs.aws.amazon.com/appstudio/latest/userguide/getting-started-tutorial-empty.html): Learn about App Studio by following a step-by-step tutorial to build an app from scratch.


## [Administrator documentation](https://docs.aws.amazon.com/appstudio/latest/userguide/administrator-documentation.html)

- [Managing user access with groups and roles](https://docs.aws.amazon.com/appstudio/latest/userguide/managing-access-and-roles.html): Learn how to manage access to App Studio with groups and roles.

### [Connect to other services with connectors](https://docs.aws.amazon.com/appstudio/latest/userguide/connectors.html)

Learn how to connect App Studio to other services to access their resources and APIs from App Studio apps.

### [Connect to AWS services](https://docs.aws.amazon.com/appstudio/latest/userguide/add-connector-services.html)

- [Connect to Amazon Redshift](https://docs.aws.amazon.com/appstudio/latest/userguide/connectors-redshift.html): Learn how to connect App Studio to Amazon Redshift to use Amazon Redshift resources in App Studio apps.
- [Connect to Amazon DynamoDB](https://docs.aws.amazon.com/appstudio/latest/userguide/connectors-dynamodb.html): Learn how to connect App Studio to Amazon DynamoDB to use DynamoDB resources in apps.
- [Connect to AWS Lambda](https://docs.aws.amazon.com/appstudio/latest/userguide/connectors-lambda.html): Learn how to connect App Studio to AWS Lambda to use Lambda resources in App Studio apps.
- [Connect to Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/appstudio/latest/userguide/connectors-s3.html): Learn how to connect App Studio to Amazon S3 to use Amazon S3 resources in App Studio apps.
- [Connect to Amazon Aurora](https://docs.aws.amazon.com/appstudio/latest/userguide/connectors-aurora.html): Learn how to connect to Amazon Aurora for use in App Studio apps.
- [Connect to Amazon Bedrock](https://docs.aws.amazon.com/appstudio/latest/userguide/connectors-bedrock.html): Learn how to connect App Studio to Amazon Bedrock to use Amazon Bedrock in App Studio apps.
- [Connect to Amazon Simple Email Service](https://docs.aws.amazon.com/appstudio/latest/userguide/connectors-ses.html): Learn how to connect App Studio to Amazon Simple Email Service to use it to send email notifications from your app.
- [Connect to other AWS services](https://docs.aws.amazon.com/appstudio/latest/userguide/connectors-aws.html): Use the Other AWS services connector how to connect App Studio to AWS services and use them in apps.
- [Use encrypted data sources with CMKs](https://docs.aws.amazon.com/appstudio/latest/userguide/encrypted-data-cmk.html): This topic contains information about setting up and connecting App Studio to data sources that are encrypted using a AWS KMS Customer Managed Key (CMK).

### [Connect to third-party services](https://docs.aws.amazon.com/appstudio/latest/userguide/add-connector-third-party.html)

- [Connect to third-party services and APIs (generic)](https://docs.aws.amazon.com/appstudio/latest/userguide/connectors-api.html): Learn how to connect App Studio apps to third-party services and their APIs with the API Connector.
- [Connect to services with OpenAPI](https://docs.aws.amazon.com/appstudio/latest/userguide/connectors-openapi.html): Learn how to connect App Studio to third-party services with OpenAPI for use in App Studio apps.
- [Connect to Salesforce](https://docs.aws.amazon.com/appstudio/latest/userguide/connectors-salesforce.html): Learn how to connect App Studio to Salesforce for use in App Studio apps.
- [Viewing, editing, and deleting connectors](https://docs.aws.amazon.com/appstudio/latest/userguide/viewing-deleting-connectors.html)
- [Deleting an App Studio instance](https://docs.aws.amazon.com/appstudio/latest/userguide/instance-delete.html): Discover how to delete your App Studio instance.


## [Builder documentation](https://docs.aws.amazon.com/appstudio/latest/userguide/builder-documentation.html)

### [Tutorials](https://docs.aws.amazon.com/appstudio/latest/userguide/tutorials.html)

Explore tutorials that walk through creating various App Studio apps.

- [Build a text summarizer app with Amazon Bedrock](https://docs.aws.amazon.com/appstudio/latest/userguide/tutorial-conversational-bedrock.html): Learn about App Studio by following a step-by-step tutorial to build an app from scratch.
- [Interacting with Amazon S3](https://docs.aws.amazon.com/appstudio/latest/userguide/automations-s3.html): Follow this tutorial to learn how to the basics about managing and showing Amazon S3 objects in your App Studio app.
- [Invoking Lambda functions](https://docs.aws.amazon.com/appstudio/latest/userguide/tutorial-lambda.html): Follow this tutorial to learn how to the basics about invoking Lambda functions in your App Studio app.
- [Building your app with generative AI](https://docs.aws.amazon.com/appstudio/latest/userguide/generative-ai.html): Learn about the generative AI features of App Studio and how to use them.

### [Creating, editing, and deleting applications](https://docs.aws.amazon.com/appstudio/latest/userguide/applications-create-edit-delete.html)

Learn how to create, edit, and delete App Studio applications.

- [Creating an application](https://docs.aws.amazon.com/appstudio/latest/userguide/applications-create.html): Use the following procedure to create an application in App Studio.
- [Importing applications](https://docs.aws.amazon.com/appstudio/latest/userguide/applications-import.html): You can import a copy of an exported application to your App Studio instance.
- [Duplicating applications](https://docs.aws.amazon.com/appstudio/latest/userguide/applications-duplicate.html): Application owners and co-owners can duplicate their apps to create an exact copy of the app.
- [Editing or building an application](https://docs.aws.amazon.com/appstudio/latest/userguide/applications-edit.html): Use the following procedure to edit an application in App Studio.
- [Edit a previously published app version](https://docs.aws.amazon.com/appstudio/latest/userguide/applications-edit-previously-published-version.html): Use the following procedure to edit a previously published version of your App Studio application.
- [Renaming an application](https://docs.aws.amazon.com/appstudio/latest/userguide/applications-rename.html): Use the following procedure to rename an application in App Studio.
- [Deleting an application](https://docs.aws.amazon.com/appstudio/latest/userguide/applications-delete.html): Use the following procedure to delete an application in App Studio.

### [Previewing, publishing, and sharing applications](https://docs.aws.amazon.com/appstudio/latest/userguide/applications-preview-publish-share.html)

Learn how to create app-specific roles and configure page visibility based on roles in App Studio.

- [Previewing applications](https://docs.aws.amazon.com/appstudio/latest/userguide/applications-preview.html): You can preview applications in App Studio to see how they will appear to users and also test its functionality by using it and checking logs in a debug panel.
- [Publishing applications](https://docs.aws.amazon.com/appstudio/latest/userguide/applications-publish.html): When you've finished creating and configuring your application the next step is to publish it to test data transfers or share it with end users.
- [Sharing published applications](https://docs.aws.amazon.com/appstudio/latest/userguide/application-share.html): When you publish an application that has not been published yet, it is not available for users until it is shared.
- [Rolling back to a previously published version](https://docs.aws.amazon.com/appstudio/latest/userguide/application-rollback-version.html): Use the following procedure to roll back the Production environment of your App Studio app to a previously published version.
- [Exporting applications](https://docs.aws.amazon.com/appstudio/latest/userguide/applications-export.html): You can export a snapshot of your application to share it with other App Studio instances.

### [Pages and components: Build your app's user interface](https://docs.aws.amazon.com/appstudio/latest/userguide/pages-components-ux.html)

Learn about building the UX of an App Studio app with pages and components.

### [Managing pages](https://docs.aws.amazon.com/appstudio/latest/userguide/pages.html)

Learn how to create, edit, and delete pages to build the UX of an App Studio app.

- [Creating a page](https://docs.aws.amazon.com/appstudio/latest/userguide/pages-create.html): Use the following procedure to create a page in an application in App Studio.
- [Duplicating a page](https://docs.aws.amazon.com/appstudio/latest/userguide/pages-duplicate.html): Use the following procedure to duplicate a page in an application in App Studio.
- [Viewing and editing page properties](https://docs.aws.amazon.com/appstudio/latest/userguide/pages-edit.html): Use the following procedure to edit a page in an application in App Studio.
- [Deleting a page](https://docs.aws.amazon.com/appstudio/latest/userguide/pages-delete.html): Use the following procedure to delete a page from an application in App Studio.

### [Managing components](https://docs.aws.amazon.com/appstudio/latest/userguide/adding-editing-deleting-components.html)

Use the following procedures to add, edit, and delete components in or from pages in the App Studio application studio to craft the desired user interface for your application.

- [Adding components to a page](https://docs.aws.amazon.com/appstudio/latest/userguide/adding-components.html): Use the following procedure to add a component to a page in App Studio.
- [Duplicating components](https://docs.aws.amazon.com/appstudio/latest/userguide/duplicating-components.html): Use the following procedure to duplicate a component in an App Studio app.
- [Viewing and editing component properties](https://docs.aws.amazon.com/appstudio/latest/userguide/editing-component-properties.html)
- [Deleting components](https://docs.aws.amazon.com/appstudio/latest/userguide/deleting-components.html)
- [Configuring role-based visibility of pages](https://docs.aws.amazon.com/appstudio/latest/userguide/app-level-roles.html): Learn how to create app-specific roles and configure page visibility based on roles.
- [Ordering and organizing pages in the app navigation](https://docs.aws.amazon.com/appstudio/latest/userguide/pages-order.html): Learn how to order or organize pages in App Studio.
- [Change colors in your app with app themes](https://docs.aws.amazon.com/appstudio/latest/userguide/app-theme.html): Learn how to change the color of certain parts of your App Studio app using app themes.
- [Components reference](https://docs.aws.amazon.com/appstudio/latest/userguide/components-reference.html): Learn how to configure components and their properties in an App Studio app.

### [Automations and actions: Define your app's business logic](https://docs.aws.amazon.com/appstudio/latest/userguide/automations.html)

Learn how configure your App Studio app's business logic and functionality with automations.

- [Automations concepts](https://docs.aws.amazon.com/appstudio/latest/userguide/automations-concepts.html): Learn important concepts and terms to know when defining and configuring your app's functionality with automations in App Studio.
- [Creating, editing, and deleting automations](https://docs.aws.amazon.com/appstudio/latest/userguide/automations-create-edit-delete.html)
- [Adding, editing, and deleting automation actions](https://docs.aws.amazon.com/appstudio/latest/userguide/automations-actions-add-edit-delete.html): Learn how to add, edit, or delete actions in automations for an App Studio app.
- [Automation actions reference](https://docs.aws.amazon.com/appstudio/latest/userguide/automations-actions-reference.html): Learn how to configure actions and their properties in App Studio automations.

### [Entities and data actions: Configure your app's data model](https://docs.aws.amazon.com/appstudio/latest/userguide/data.html)

Learn how to define your App Studio app's data model with entities.

- [Best practices when designing data models](https://docs.aws.amazon.com/appstudio/latest/userguide/data-model-best-practices.html): Learn best practices for designing and defining your App Studio data models.
- [Creating an entity](https://docs.aws.amazon.com/appstudio/latest/userguide/data-entities-create.html): There are four methods for creating an entity in an App Studio app.

### [Configuring an entity](https://docs.aws.amazon.com/appstudio/latest/userguide/data-entities-edit.html)

Use the following topics to configure an entity in an App Studio application.

- [Editing the entity name](https://docs.aws.amazon.com/appstudio/latest/userguide/data-entities-edit-name.html)
- [Adding, editing, or deleting entity fields](https://docs.aws.amazon.com/appstudio/latest/userguide/data-entities-edit-fields.html)
- [Creating, editing, or deleting data actions](https://docs.aws.amazon.com/appstudio/latest/userguide/data-entities-edit-data-actions.html): Data actions are used in applications to run actions on an entity's data, such as fetching all records, or fetching a record by ID.
- [Adding or deleting sample data](https://docs.aws.amazon.com/appstudio/latest/userguide/data-entities-edit-sample-data.html): You can add sample data to entities in an App Studio application.
- [Add or edit connected data source and map fields](https://docs.aws.amazon.com/appstudio/latest/userguide/data-entities-edit-connection.html)
- [Deleting an entity](https://docs.aws.amazon.com/appstudio/latest/userguide/data-entities-delete.html): Use the following procedure to delete an entity from an App Studio application.
- [Managed data entities](https://docs.aws.amazon.com/appstudio/latest/userguide/managed-data-entities.html): Learn about using managed data entities connected to DynamoDB tables in an App Studio app.

### [Page and automation parameters](https://docs.aws.amazon.com/appstudio/latest/userguide/paramters.html)

Learn how to pass dynamic values between components, pages, and automations using parameters in an App Studio app.

- [Page parameters](https://docs.aws.amazon.com/appstudio/latest/userguide/parameters-page.html): Page parameters are a way to send information between pages and are often used when navigating from one page to another within an App Studio app to maintain context or pass data.
- [Automation parameters](https://docs.aws.amazon.com/appstudio/latest/userguide/parameters-automation.html): Automation parameters are a powerful feature in App Studio that can be used to create flexible and reusable automations by passing dynamic values from various sources, such as the UI, other automations, or data actions.
- [Using JavaScript to write expressions](https://docs.aws.amazon.com/appstudio/latest/userguide/expressions.html): Learn how to use JavaScript to write expressions in App Studio apps.
- [Data dependencies and timing considerations](https://docs.aws.amazon.com/appstudio/latest/userguide/data-dependencies-timing-considerations.html): When building complex applications in App Studio, it's crucial to understand and manage data dependencies between different data components, such as forms, detail views, and automation-powered components.
- [Building an app with multiple users](https://docs.aws.amazon.com/appstudio/latest/userguide/builder-collaboration.html): Multiple users can work on a single App Studio app, however only one user can edit an app at one time.
- [Updating your app's content security settings](https://docs.aws.amazon.com/appstudio/latest/userguide/app-content-security-settings-csp.html): Every application in App Studio has content security settings that can be used to restrict external media or resources such as images, iFrames, and PDFs from being loaded, or only permitted from specified domains or URLs (including Amazon S3 buckets).


## [Troubleshooting and debugging](https://docs.aws.amazon.com/appstudio/latest/userguide/troubleshooting-and-debugging.html)

- [Setup, permissions, and onboarding](https://docs.aws.amazon.com/appstudio/latest/userguide/troubleshooting-permissions-onboarding.html): This topic includes information about troubleshooting common issues when setting up or onboarding to App Studio, and managing permissions.

### [Troubleshooting and debugging apps](https://docs.aws.amazon.com/appstudio/latest/userguide/troubleshooting-debugging-apps.html)

The following topics include information for troubleshooting and debugging App Studio apps.

- [The AI builder assistant](https://docs.aws.amazon.com/appstudio/latest/userguide/troubleshooting-ai-builder-assistant.html): This topic contains troubleshooting guidance for common issues when using the AI builder assistant.
- [In the app studio](https://docs.aws.amazon.com/appstudio/latest/userguide/troubleshooting-building.html): This topic contains troubleshooting and debugging guidance for issues when building applications.
- [Previewing apps](https://docs.aws.amazon.com/appstudio/latest/userguide/troubleshooting-preview.html): This topic contains information about troubleshooting issues when trying to preview apps.
- [In the Testing environment](https://docs.aws.amazon.com/appstudio/latest/userguide/troubleshooting-testing.html): This topic contains information about troubleshooting apps published to the Testing environment.
- [Using logs in CloudWatch](https://docs.aws.amazon.com/appstudio/latest/userguide/troubleshooting-cloudwatch.html): Amazon CloudWatch Logs monitors your AWS resources and the applications you run on AWS in real time.
- [Connectors](https://docs.aws.amazon.com/appstudio/latest/userguide/troubleshooting-connectors.html): This topic contains troubleshooting guidance for common connector issues.
- [Publishing and sharing apps](https://docs.aws.amazon.com/appstudio/latest/userguide/troubleshooting-publishing-sharing.html): This topic contains troubleshooting guidance for common issues when publishing or sharing App Studio applications.


## [Security](https://docs.aws.amazon.com/appstudio/latest/userguide/security.html)

- [Security considerations and mitigations](https://docs.aws.amazon.com/appstudio/latest/userguide/security-considerations-and-mitigations.html)
- [Data protection](https://docs.aws.amazon.com/appstudio/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in App Studio.

### [App Studio and Identity and Access Management](https://docs.aws.amazon.com/appstudio/latest/userguide/security-iam.html)

How to authenticate requests and manage access your App Studio resources.

- [AWS managed policies](https://docs.aws.amazon.com/appstudio/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for App Studio and recent changes to those policies.
- [Service-linked roles](https://docs.aws.amazon.com/appstudio/latest/userguide/appstudio-service-linked-roles.html): Learn about service-linked roles for App Studio.
- [Identity-based policy examples](https://docs.aws.amazon.com/appstudio/latest/userguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify App Studio resources.
- [Compliance validation](https://docs.aws.amazon.com/appstudio/latest/userguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/appstudio/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific App Studio features for data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/appstudio/latest/userguide/infrastructure-security.html): Learn how AWS App Studio isolates service traffic.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/appstudio/latest/userguide/vulnerability-analysis-and-management.html): Learn about configuration and vulnerability analysis in AWS App Studio.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/appstudio/latest/userguide/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.
- [Cross-Region data transfer](https://docs.aws.amazon.com/appstudio/latest/userguide/cross-region-data-transfer.html): Learn about cross-Region data transfer in AWS App Studio, including the features that use it, and how to opt out.

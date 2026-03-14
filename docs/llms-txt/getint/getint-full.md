# Getint Documentation

Source: https://docs.getint.io/llms-full.txt

---

# Welcome to the Getint Documentation Hub

Greetings and a warm welcome to the official documentation page of Getint.io – where every ticket indeed finds its rightful place.

**About Getint:** Getint emerges as a state-of-the-art platform designed to seamlessly integrate and synchronize a wide array of tools including Jira, ServiceNow, Salesforce, Monday.com, ClickUp, Asana, Trello, GitHub, GitLab, Wrike, Zendesk, Azure DevOps, Airtable, Hubspot, Freshdesk, Freshservice with more integrations on the horizon. Whether it's connecting one app to another or orchestrating multi-app integrations, Getint facilitates diverse connectivity scenarios like:

* Single Jira to ServiceNow, or multiple ServiceNows
* Jira to Jira
* Jira to Asana, and simultaneously to GitLab, and beyond.

**Our Foundation:** Founded in 2019 by a team rich in integration expertise, Getint.io was born out of a desire to revolutionize the integration landscape. With extensive experience in the Atlassian Ecosystem and beyond, we observed a gap in the market for modern, agile, and efficiently designed integration solutions. Our journey is driven by three core observations:

* **Innovation Over Legacy**: Confronted with outdated solutions suffering from legacy code issues, we committed to developing a fresh, agile, and high-performing platform leveraging our profound industry experience.
* **Fair Pricing Model**: We challenge the status quo with a pricing structure that ensures the best value for money. This commitment is exemplified by our offer of free migration for users of platforms like ConnectAll, Workato, Unito, Backbone, Exalate, and TFS4JIRA.
* **Focus on Admins and Customization**: While appreciating solutions that prioritize business user-friendliness, our vision was to create a tool that empowers admins with extensive customization options, detailed reporting, and comprehensive logs for deep insights into integration activities. Available as both SaaS and on-premise, Getint is versatile to meet the diverse needs of businesses and legal departments alike.
* **Exceptional Customer Service**: At Getint, customer service is not just a department; it's at the heart of everything we do. We pride ourselves on offering personalized support directly from our team, ensuring that every interaction is meaningful and genuinely focused on solving your challenges.

**Embark on Your Integration Journey with Confidence:** With Getint, embark on a journey of seamless integration and data synchronization crafted to support the most intricate workflows and business requirements. Explore our documentation to get started, discover best practices, and unlock the full potential of your tools with Getint.

Welcome aboard, where your integration success is our mission.

Read more:

* [Case studies](https://www.getint.io/case-studies)
* [Blog posts](https://www.getint.io/blog)
* [Atlassian Marketplace](https://marketplace.atlassian.com/vendors/1218845/getint-integrations-jira-azure-devops-servicenow-salesforce-asana-monday-com-clickup-and-others)

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# About Getint / Concepts

### How Getint Helps Your Team

Getint is a platform that connects two or more systems and keeps data aligned between them. It can move information once during a migration or keep it synchronized continuously through an integration.

The platform is designed for enterprise environments, but it stays simple enough for administrators and project teams to configure without writing code.

### Key Concepts You Should Know

#### Integration

An integration keeps data synchronized between two systems. Changes made in one tool appear in the other based on your mapping and sync rules.

#### Migration

A migration moves data from one system to another. It is typically used during tool consolidation or platform changes.

#### Connection

A connection links Getint to an external system. Each connection includes authentication details and configuration settings.

#### Mapping

A mapping defines how fields, statuses, comments, attachments, and other elements relate between the two systems.

#### Run Cycle

A run cycle is the process where Getint checks for changes and updates the connected systems.

#### Conflict Resolution

If both systems change the same item, Getint will apply the latest changes.

### Migration and Integration at a Glance

A simple comparison helps clarify the difference.

| Concept     | Purpose                | When to Use It                                 |
| ----------- | ---------------------- | ---------------------------------------------- |
| Migration   | Move data once         | Tool consolidation, platform changes           |
| Integration | Sync data continuously | Cross‑team collaboration, multi‑tool workflows |

{% hint style="success" %}
For a deeper explanation, see the dedicated page on [Migration and Integration](https://docs.getint.io/getting-started-with-the-platform/about-getint-concepts/migration-vs-integration).
{% endhint %}

Understanding these core concepts will help you plan your first project and get the most out of the platform. If you need guidance or want help reviewing your setup, you can contact our support team for assistance.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# How Getint Works (How it Syncs the Data)

Getint offers a uniquely flexible and efficient approach to integration, designed to meet diverse business needs. Here's how our platform operates.

## Set Up Getint for the First Time

1. Connect to Applications: Users begin by connecting Getint to the desired apps (e.g., Jira, ServiceNow, Asana, Azure DevOps). This requires Service Accounts, preferably with admin permissions.
2. Establishing Connection: To connect, provide the instance URL and credentials of the Service Account (including instance URL, username, password/token).
3. Mapping Types and Fields: The next step involves type mapping (e.g., Task in Jira to Task in Azure DevOps) and field mapping (e.g., Summary in Jira to Title in ServiceNow), including options for comments and attachments integration.
4. Status Mapping: Finally, map the statuses between the systems to ensure accurate status reflection across platforms.

### Platform Operations

#### Deployment Flexibility

* Jira Native Application: Getint seamlessly integrates with Jira, requiring no additional installations for other apps you're integrating with Jira.
* Getint SaaS: For those preferring a cloud-based solution, Getint offers a Software as a Service (SaaS) model.
* Getint OnPremise: Ideal for businesses prioritizing data security, this option works entirely behind the firewall, ensuring maximum data protection.

#### Straightforward Pricing

* We believe in simplicity and transparency. Our pricing is based on the number of connections established (e.g., one Jira instance to one Azure DevOps instance).
* No hidden fees for the number of projects, tasks, rules, templates, or similar metrics.

#### REST API Utilization

* Getint.io leverages REST API to communicate with applications like Jira, ServiceNow, etc.
* Through REST API, we efficiently fetch data that needs to be synchronized between different platforms.

#### Synchronization Logic

Every specified interval, Getint performs the following steps for each integration:

* Data Fetching: Send REST API requests to both apps (A and B) to fetch relevant data for synchronization.
* Sync Check & Update:
  * For each item returned from both apps, we first check if it has been synced in previous runs.
  * If it has a counterpart, we determine which item was modified later. The more recent one is used as the trigger to update its counterpart.
  * If an item has no counterpart, a new item is created in the corresponding app.

This systematic approach ensures that data across your integrated platforms remains up-to-date and consistent, streamlining workflows and enhancing productivity.

Getint.io stands as a robust and user-friendly solution for your integration needs, blending adaptability, security, and efficiency in one powerful package.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# How Integrations are Executed by Getint

## Integration Execution: The Basics

In Getint, each integration runs sequentially, meaning one integration execution must finish before the next one can start. This concept is crucial to understand as it directly impacts the frequency of integration runs.

For instance, Jira Cloud users can only set a run interval of a minimum of 3 minutes, and Data Center customers have run intervals of a minimum of 60-120 seconds (mostly 120 seconds). However, On-Premise users can have run intervals of >= 0 seconds.

When users set an interval for integration (such as every 15 seconds), it’s important to understand that this doesn’t guarantee the integration will occur exactly every 15 seconds. The actual frequency of execution depends on various factors, including the total number of integrations and the duration each integration requires to complete.

### The Impact of Multiple Integrations

If a user has a large number of integrations, it can significantly impact the sync time of changes. For instance, if an item is set to be synced by an integration that is 10th in a queue, and each preceding integration takes 15 minutes (due to the large amount of data they sync), the user may experience a 2-3 hour delay between the change and its propagation.

In a scenario where there are 50 integrations, a 60-second interval won’t be effective because each integration needs to be completed before the next one can start. Therefore, the interval time does not always dictate the frequency of integration runs.

### Boost your Performance with Getint On-Premise

For customers seeking improved performance and parallel integration execution, Getint’s On-Premise solution stands out as a robust choice. This solution allows customers to run multiple threads and assign integrations to them, thereby significantly enhancing performance. Also, On-Premise operates entirely behind your firewall, providing a secure environment aligned with your company requirements.

The benefits of using our On-Premise solution include, but aren’t excluded to:

* Modifying run intervals to your system needs
* Supports multithreading and multi-tenancy
* Saving your data is configurable, which differs from Cloud users who can only retain their data for a maximum of 1 month
* Freedom to perform your own server maintenance and software updates

### Optimizing Integration Settings

To optimize the performance of Getint, users should consider the number of integrations they have and the interval they set for each integration. If there are more than a certain number of integrations, users might need to adjust the intervals to ensure efficient data syncing.

Understanding these nuances can help users make the most of Getint’s powerful integration capabilities and ensure smooth and timely data syncing across platforms. Remember, the key is to find the right balance between the number of integrations and the intervals set for each one.

{% hint style="info" %}
If you have any questions or need assistance with your integration, don’t hesitate to contact our [Support Center.](https://getint.io/help-center)
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Migration vs Integration

Getint offers two fundamental functionalities: data migration and continuous sync. Understanding the difference between these two is key to optimizing your use of the platform.

{% hint style="warning" %}
Migration is a premium feature that is limited during the trial version. For detailed pricing information based on the volume of tasks, visit [Getint Pricing](https://www.getint.io/pricing) and click on **Migration.**
{% endhint %}

### Data Migration

#### Definition and Use Case <a href="#definition-and-use-case" id="definition-and-use-case"></a>

Data migration in Getint refers to the process of moving historical data—the information that existed before you started using Getint. This is crucial when transitioning from one tool to another, ensuring that all records are preserved. Typical use cases involve migrating data from one platform to another, such as:

* Jira to Azure DevOps
* Asana to Jira
* ClickUp to Monday.com

#### Project Nature <a href="#project-nature" id="project-nature"></a>

Migration projects are generally one-time operations designed to move a large volume of data within a limited timeframe. This process ensures that historical data is seamlessly transferred to the new system, maintaining the continuity of your workflows.

### Continuous Sync <a href="#data-integration" id="data-integration"></a>

#### Definition and Use Case <a href="#definition-and-use-case.1" id="definition-and-use-case.1"></a>

Data integration connects newly created or recently updated items—tasks, service requests, bugs, etc.—in real-time or near real-time. This ongoing process begins the moment you start using Getint, keeping your systems synchronized as new data is generated.

#### Project Nature <a href="#project-nature.1" id="project-nature.1"></a>

Integrations are typically long-term, ongoing projects. They involve syncing smaller batches of data regularly, often daily. Integration is essential for maintaining continuous data flow between different platforms as updates and new items are created.

### Combining Migration and Integration <a href="#combining-migration-and-integration" id="combining-migration-and-integration"></a>

Some projects require both: initially migrating historical items and then continuously syncing new updates or creations. This approach ensures a comprehensive transition to a new system, followed by consistent and up-to-date synchronization moving forward.

### Pricing Models <a href="#pricing-models" id="pricing-models"></a>

* **Migrations:** The cost is based on the **volume of tasks** to be migrated.
* **Integrations:** For integrations involving Jira, pricing is based on the number of Jira users, and billed via the [**Atlassian Marketplace**](https://marketplace.atlassian.com/vendors/1218845/getint-integrations-jira-azure-devops-servicenow-salesforce-asana-monday-clickup-gitlab-and-others). Non-Jira integrations are billed through us directly, and they are available in three different plans:
  * **Unlimited $1,800/year - Supported Tools:** ClickUp, Monday, Asana, GitLab, GitHub, Wrike, Hubspot, Zendesk.
  * **Professional $4,800/year - Supported Tools:** ServiceNow, Salesforce, Azure DevOps.
  * **Enterprise - Custom Pricing:** An unlimited number of tools are supported.

### Setup Process <a href="#setup-process" id="setup-process"></a>

The setup for both migration and integration is nearly identical in Getint. For migrations, additional steps include enabling the migration feature, specifying the direction (source and target systems), and defining the time range for the issues to be migrated.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Onboarding

Welcome to the Onboarding page of Getint – your comprehensive guide to getting started and making the most out of our platform.

### **Navigating the Getint Onboarding Experience**

Embarking on your journey with Getint is an exciting step towards enhancing your team's collaboration and workflow efficiency. Our onboarding process is designed to help you swiftly familiarize yourself with Getint’s capabilities, reducing the time and effort required for internal training.

### **What is Getint's Customer Onboarding?**

Getint's customer onboarding is a specialized service aimed at providing a smooth introduction to our platform. This service is tailored to meet the needs of various customer tiers, based on their specific plans. During onboarding, you'll be paired with a dedicated Customer Success Manager who will guide you through the nuances of Getint, from basic functionalities to more complex customization and workflow consultations.

The scope of your onboarding will depend on several factors, including your selected plan, the applications you're integrating, and the overall breadth of your integration project.<br>

### **Key Topics in Getint Onboarding Sessions**

Once you subscribe to Getint, keep an eye on your email for an onboarding invitation. This invite will allow you to schedule a session at a convenient time. If you're struggling to find a suitable slot, don’t hesitate to contact us directly – we're committed to accommodating clients across different time zones.

Onboarding sessions are conducted via platforms like Google Meet or Zoom, facilitating an interactive experience with screen-sharing capabilities.

Your session will be tailored to your specific requirements, covering topics essential for maximizing your use of Getint. A typical onboarding agenda includes:

* Understanding and aligning with your business goals.
* Deep diving into your existing workflow.
* Offering advice on workflow development, especially if you're in the initial stages.
* Providing insights on customizing your flows optimally.
* Introducing you to Getint's latest features and functionalities.

### **Preparing for Your Onboarding**

To get the most out of your onboarding session, here are a few preparatory steps:

* Ensure all relevant tools are connected on the Getint integrations page. Some tools, like Jira, may require additional setup steps prior to integration.
* Set up a few test projects and synchronize them. This exercise will help you formulate specific questions and understand how Getint aligns with your actual workflow.

The Getint onboarding experience is more than just a tutorial – it's a customized journey that equips you and your team with the knowledge and skills to make the most of what Getint has to offer. We look forward to assisting you in streamlining your workflows and achieving your business objectives with Getint.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# One-directional / Bi-directional Integration

### Understanding Integration Types with Getint <a href="#understanding-integration-types-with-getint" id="understanding-integration-types-with-getint"></a>

In Getint, we offer two primary types of data synchronization between integrated tools: one-directional and bi-directional integration. Understanding these concepts is key to effectively managing data and maintaining smooth synchronization between your workflows.

### One-Directional Integration <a href="#one-directional-integration" id="one-directional-integration"></a>

In a one-directional integration, data flows in a single direction from a source system to a target system. This means any changes made in the source system will be reflected in the target system, but not vice versa. For example, updates in a Jira project can be automatically reflected in a connected ServiceNow instance, but changes in ServiceNow won’t impact the Jira project. This type of integration is useful for scenarios where data consistency is needed from one primary system to another without reciprocal updates.

### Bi-Directional Integration <a href="#bi-directional-integration" id="bi-directional-integration"></a>

Bi-directional integration allows data to flow in both directions – from the source to the target and from the target back to the source. In this setup, changes made in either system are synchronized with the other. For example, updates made in a Jira project and a connected Azure DevOps project are reflected in each other. This approach is ideal for environments where ongoing collaboration and real-time data parity between systems are crucial.

### Flexibility with Getint <a href="#flexibility-with-getint" id="flexibility-with-getint"></a>

A unique feature of Getint is the ability for users to easily switch between one-directional and bi-directional integration at the field level. This means you can customize how each field (such as summary, priority, labels, or custom fields) is synchronized between systems. For instance, you might choose bi-directional synchronization for the “priority” field but one-directional for the “summary” field. This level of control allows users to tailor the integration to their specific workflow and data management needs, ensuring optimal efficiency and data integrity.

### Conclusion <a href="#conclusion" id="conclusion"></a>

Getint’s flexible integration approach empowers users to configure their data synchronization precisely as needed, whether it be one-directional or bi-directional, or even mixed within the same integration setup. This provides a highly customizable and efficient data integration solution.

Our amazing team at Getint is always here to support you throughout your integration journey. We specialize in providing the best possible customer experience. If you have any questions about this integration or need help with the setup process, feel free to open a ticket with us at our [Help Center](https://getint.io/help-center) or [Schedule a Demo](https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# What are Runs?

In the Getint platform, a "Run" is a critical operation in the synchronization process between connected tools. Here’s an extended explanation, including the recording and logging of each Run.

### Initiating Synchronization

A Run occurs when Getint sends API requests to connected collaboration tools. These requests aim to gather data on all newly created items and their respective fields, as well as any recent updates, as defined in the integration setup.

### How Run Intervals Affect Your Integration

Integrations execute sequentially, meaning each one must finish before the next can begin. This sequence is essential for understanding how often integrations can run.

For example, Jira Cloud users can set a minimum run interval of 3 minutes, while Data Center customers have a range between 60 to 120 seconds (primarily 120 seconds). However, On-Premise users can set run intervals starting from 0 seconds.

When setting an interval for integration (like every 15 seconds), remember that this doesn't guarantee the integration will occur exactly at that interval. The actual frequency depends on various factors, such as the total number of integrations and the time each one takes to complete.

### Detection and Integration of Changes

Getint actively searches for new items or changes in existing items during a Run. Detected changes are then integrated, ensuring data across the tools remains synchronized and current.

### Handling Concurrent Changes

Getint effectively merges data when changes occur simultaneously in the same field across integrated tools. This merging mechanism is crucial for preserving all updates and preventing data loss.

### Recording and Logging of Runs

Every Run is meticulously recorded and logged within Getint. This means that users have the ability to review and analyze the actions taken during each Run.

The logs provide valuable insights into the outcomes of each synchronization process. They are an essential tool for users to easily identify and understand any errors or discrepancies that may occur.

### Ensuring Data Integrity and Continuity

Regular Runs are essential for maintaining data integrity and continuity across different platforms. They ensure that all integrated systems reflect the latest and most accurate data.

In summary, a Run in Getint is not only a process of querying and integrating data but also involves a comprehensive recording and logging mechanism. This feature allows users to monitor, analyze, and troubleshoot the synchronization process, ensuring transparency and control over data integration across their collaboration tools.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# What is a Connection?

### What is a Connection?

In the context of Getint, a "Connection" is a crucial element that forms the basis of our integration process. It refers to the established link between Getint and a specific collaboration software tool, such as Jira, Azure DevOps, ServiceNow, Asana, among others. Here's a detailed breakdown of what a Connection entails and how it's set up:<br>

#### Authentication and Accessibility

* A Connection is successfully established when Getint is authenticated and can access a given collaboration software tool.
* This authentication is the bridge that enables seamless communication and data exchange between Getint and the external tool.

#### Establishing a Connection

* To create this link, you need the instance URL of the tool you want to connect with. The instance URL is the web address where the application is hosted or can be accessed.
* Additionally, a service account user is required. This involves the email/login associated with the account and either a password or a token for authentication.
* The service account should ideally have the necessary permissions to perform the intended actions within the tool (like creating, updating, and managing tasks or issues).

#### Functioning as the Service Account User

* Once connected successfully, Getint operates as this service account user.
* All actions performed by Getint, such as creating or updating tasks and issues, will be executed under this user's identity.
* This approach ensures that all changes and activities carried out by Getint are properly logged and traceable within the collaboration tool.

In summary, a Connection in Getint is the authenticated and functional link between Getint and an external collaboration tool, enabled through specific access credentials. This connection is fundamental to the integration process, allowing Getint to perform a range of actions as an authorized user of the external tool.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Starting the Free Trial and Accessing the Getint App

Installing and integrating applications within your Jira tool is a seamless process, provided you have the right access and permissions. This document outlines user-friendly steps for both Jira Server/Data Center and Jira Cloud, ensuring a smooth experience for all users.

### **Starting the Free Trial and Accessing the Getint App** <a href="#starting-the-free-trial-and-accessing-the-getint-app" id="starting-the-free-trial-and-accessing-the-getint-app"></a>

#### **Jira Cloud Integration**

#### **Admin User**

Access your Atlassian using the admin account, as these steps require admin access to the Jira Cloud. Navigate to the Atlassian marketplace.

* Navigate to the Atlassian Marketplace and select "Explore More Apps."
* Search for the Getint app, select "Try it Free," and let it install.
* Go to "Manage Apps" and, if the trial hasn't started, click "Start Trial."
* When the trial begins, click the "Apps" tab again and choose the Getint app you want to use.
* Once the trial begins, choose the Getint app under the "Apps" tab to initiate integration.
* Users will be routed to the Getint app and prompted to begin their integration. To get started, select integration or migration. (Click here to learn how to begin the integration.)

{% embed url="<https://youtu.be/GzmQYVt9U04>" %}

**Non-Admin Users**

Non-admin users should request app authorization from administrators

* Select the "Apps" tab, "Explore More Apps," and search for the Getint app.
* Request installation, and administrators will see the request under "Apps > View App Requests."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fo5fGNzzZ1ZNdtYuK9UL5%2FRequest%20installation%20from%20your%20Jira%20admin.png?alt=media&#x26;token=0295d43f-eb2a-4045-ab51-972d4af7021d" alt=""><figcaption></figcaption></figure>

* After approval, administrators configure the app. Users will not be able to access or view the application.

#### **Jira Server/Data Center**

To follow these instructions, you will need administrator access to the Jira server or data center.

* Go to "Settings" under your avatar, and select "Atlassian Marketplace."
* Search for the Getint app, choose "Free Trial," and accept the installation.
* Generate the license and follow the steps that will appear. Apply the license, go to "Manage Apps," and start the trial if not already initiated.
* After trial or purchase, access the app by selecting Admin in the left menu.
* You will be transferred to the Getint app and prompted to start their integration. To get started, choose integration or migration. (Click here to learn how to begin the integration.)

{% embed url="<https://youtu.be/Zx8LPlSk5Rg?si=dLe4xQOgMwJd2922>" %}

{% hint style="info" %}
Admin access to the Jira Server/ Data Center is necessary to administer the apps and enable downloads.
{% endhint %}

### **User Access feature** <a href="#user-access-feature" id="user-access-feature"></a>

We are excited to introduce the User Management Feature, enhancing flexibility and enabling non-admin users to create and manage integrations starting from version 1.52.

*Jira Admin can handle integrations, logs, and data. They can view it and authorize access to it. The system administrator can also troubleshoot all user-created integrations in the user's management views and download logs to submit to support if necessary.*

To enable the User Management Feature option, carefully follow the instructions below:

#### **Jira Cloud**

* In your Jira Cloud instance, log in as an administrator.
* Go to Settings and select "User Management, on the right side, select "Groups." Create a group (e.g., getint-jira-azure), select "View details," and add members.
* To access the application, the user will now see the app under the tab Apps and should click on it. They should select the app, and the Getint app will open. The option to create a new integration will prompt, giving the option to create a new integration if it is the first time accessing the app.

{% embed url="<https://youtu.be/voGnW9j1oRo>" %}

*Groups created must adhere to the Getint-xx format, such as:*

* getint-jira-jira
* getint-jira-azure
* getint-jira-wrike
* getint-jira-servicenow
* getint-jira-monday
* getint-jira-notion
* getint-jira-airtable
* getint-jira-trello
* getint-jira-hubspot
* getint-jira-gitlab
* getint-jira-freshdesk
* getint-jira-zendesk
* getint-jira-clickup
* getint-jira-asana

{% hint style="warning" %}
**Important:** This naming convention is required for the integration to work correctly.\
For example, if you're connecting **Jira** with **Monday**, the group name must be:\
\&#xNAN;**`getint-jira-monday`**
{% endhint %}

{% embed url="<https://youtu.be/BDDVf2mM1Xo>" %}

#### **Jira Server/Data Center (DC)**

* Enter your Jira Server or Data Center instance and log in as an administrator.
* Navigate to Settings, click the gear in the upper right corner of the screen, then select "User Management." Select "Groups" and create a new group (as Jira Cloud, the format should adhere to *Getint-xx*: getint-jira-azure or Getint-integrations). Please utilize the same format for the groups mentioned above.
* Select "Add," and the newly created group will appear in the group list. Choose "Edit members" and add the username, or choose it from your user list. Select "Add selected users,".

{% embed url="<https://youtu.be/DNERhFm-8jg>" %}

{% hint style="info" %}
*Access to apps can be given to Project Admin or non-admin users*
{% endhint %}

**Accessing the app:**

**Non-administrative users**

* After being granted access, users will be able to manage the integration, create a new one, and view logs and data.
* To see the application's contents, a non-admin user must get the URL to access the Getint app for now.

**Project Admin User**

* If the user is a project administrator, they will be able to locate the app in the project settings.
* On the project page, select "Project Settings". On the menu that appears, the Getint app will now appear.
* The Getint app will launch, and creating and maintaining the integrations will be possible.

{% embed url="<https://youtu.be/EXlV1TNW-Nc>" %}

{% hint style="info" %}
**For all the Non-Jira Admin roles:**

* Other users' integrations are visible but cannot be managed or saved.
* Logs for these integrations are securely encrypted to protect data privacy and cannot be viewed.
  {% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FmNmcgv7EiaNxX2LTkq5D%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=e3bc4f73-2bed-47ae-a7fa-139dd809c092" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Selecting the Correct App per License

When installing an app from the [**Atlassian Marketplace**](https://marketplace.atlassian.com/vendors/1218845/getint-integrations-jira-azure-devops-servicenow-salesforce-asana-monday-clickup-gitlab-and-others), you may encounter issues if the installation is not performed using the correct app, especially when initiating the appropriate trial or license. Following the steps below will ensure a smooth installation and help avoid common errors such as licensing mismatches or failed installations.

{% hint style="warning" %}
If the correct app is not installed, you will encounter an **Invalid Jira license** error, which prevents any work items from being synchronized.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F7mQpQDzyWm4GkxfrUWbW%2FInstalling%20the%20correct%20app.png?alt=media&#x26;token=e2d4198d-4e4e-4994-92ae-753c07f19813" alt=""><figcaption><p>On the left, you can see that different apps are available depending on the connectors you want to integrate</p></figcaption></figure>

### Troubleshooting the Invalid Jira License Error <a href="#troubleshooting-the-invalid-jira-license-error" id="troubleshooting-the-invalid-jira-license-error"></a>

After you create an integration, if the runs begin to fail, you'll see this message in the run logs. During this period, the integration will not sync any work items.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fvanv2XduX0uIu4f6hxqk%2FInvalid%20jira%20license%20error.png?alt=media&#x26;token=dbaabe25-bb47-4fa8-a568-3938e00dc5e5" alt=""><figcaption></figcaption></figure>

A warning icon will also appear beneath the license column to indicate an issue with your license.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FzgIV0gotkQZmPU5qYtQj%2FWarning%20icon%20below%20the%20License%20column.png?alt=media&#x26;token=ef4c30b6-de73-449b-927d-3cc1fa045d6e" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
We’re using the Jira Airtable app as an example to build a ServiceNow integration and intentionally force a failure, but this message will appear in any app if you’re using the wrong connector or if your license has expired.
{% endhint %}

To resolve this issue, first assess what integration you would like to build:

1. If you are integrating with **Jira**, first verify if you have an active trial for your integration:

* **Jira Cloud**: Go to the **Subscriptions** section in your billing console and check if your subscription is active.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fpa6uKuJWqnzYLbUgpe4a%2FCheck%20your%20subscription%20in%20the%20billing%20console.png?alt=media&#x26;token=7127bc7e-19a2-424c-b214-c8c60433695e" alt=""><figcaption></figcaption></figure>

* **Jira DC**: Go to the **Manage apps** section and locate the Getint app. Click on it to view more information, where all app details will be available.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FzKcWxMCwfK51PsHlPdBZ%2FWhere%20to%20check%20Jira%20DC%20license.png?alt=media&#x26;token=41eb3c5d-9e7d-41a7-adb0-7fbdc9610445" alt=""><figcaption></figcaption></figure>

1. If your trial is active, go to the **Apps** section and select the appropriate app for your integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Ffyop1YiBMlweNH3KcIIZ%2FSelecting%20the%20correct%20app%20depending%20on%20the%20tools%20you%20want%20to%20integrate.png?alt=media&#x26;token=63c10925-b537-48a3-b489-d698610f683c" alt=""><figcaption></figcaption></figure>

1. If you don’t have an active trial, go to the Atlassian Marketplace and search for **Getint**. All our apps will be listed there. Select the app you need for your integration (in this example, we’ll use ServiceNow).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMnR4mv4Nt0mAbN8QeYAI%2FSearching%20for%20the%20ServiceNow%20integration%20app%20in%20the%20marketplace.png?alt=media&#x26;token=76027433-bbb0-4175-9f39-223867b66129" alt=""><figcaption></figcaption></figure>

1. Activate the trial if you still don’t have it:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FlaJZolvf6mCDUYEyuzAo%2FActivate%20trial%20for%20ServiceNow%20app.png?alt=media&#x26;token=c4201b04-99fb-420b-b9f8-ec0fcfabd7af" alt=""><figcaption></figcaption></figure>

1. Go back to your **Apps**, and launch the Getint app.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F8dshuVFVwoBbamDsWUkM%2FLaunching%20the%20ServiceNow%20app.png?alt=media&#x26;token=3a162979-63be-47f2-9583-9a245a329753" alt=""><figcaption></figcaption></figure>

1. You should now be able to build your integrations as needed.

{% hint style="warning" %}
Note: If you are using our app to integrate (e.g., Jira-ServiceNow) and would now like to scale to integrate ServiceNow with DevOps, we can generate a new license key that will enable this within the Jira app.

This additional license key must be purchased separately. For more information, please contact our [Support Center](https://getint.io/help-center).
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FmNmcgv7EiaNxX2LTkq5D%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=e3bc4f73-2bed-47ae-a7fa-139dd809c092" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# How to Request a Trial Extension for Getint

If your trial is ending and you need extra time to fully evaluate Getint's capabilities, you can request a trial extension. The process depends on how you’re using Getint (Cloud vs. Server/Data Center) and where your instance is hosted.

### Extending Your Free Trial <a href="#extending-your-free-trial" id="extending-your-free-trial"></a>

#### **For Jira Cloud Users** <a href="#for-jira-cloud-users" id="for-jira-cloud-users"></a>

1. **Contact Getint Support:**

Start by reaching out to our support team through the in‑app chat or at our [Help Center](https://getint.io/help-center).

* Please include your **company name**, **contact email**, the **reason for the extension request**, and the additional time required.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FKciDmA88I4Wepmktdf2U%2FAsking%20for%20a%20trial%20extension.png?alt=media&#x26;token=7f68853d-e115-4f32-851f-ae31d1af378d" alt=""><figcaption></figcaption></figure>

* After evaluation, we’ll confirm the extension request and provide a screenshot or message you’ll need for Atlassian.

<br>

1. **Create a Ticket with Atlassian:**

* Go to the [Atlassian Support](https://support.atlassian.com/) portal, and click **Contact us**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FALsZ3aE7LXsdfEvBJoBY%2FContacting%20Atlassian.png?alt=media&#x26;token=9a8f02cb-6235-4915-b509-f9921dcd3f77" alt=""><figcaption></figcaption></figure>

* Under the drop-down, select **Billing, payments, and pricing**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FrKNSJZiNbZskYEYNUyBt%2FOpening%20a%20ticket%20with%20Atlassian.png?alt=media&#x26;token=673db6ad-dd63-484c-adfb-c92542547eae" alt=""><figcaption></figcaption></figure>

* You'll be redirected to a separate page to submit your ticket. Once there, select **Product Trials**, then choose **Extend product trials**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9tZytXwAJkTi8wbkXI5q%2FGo%20to%20product%20trials%20to%20extend%20your%20license.png?alt=media&#x26;token=88d529e3-424b-4d94-a00f-a430834f476d" alt=""><figcaption></figcaption></figure>

* Specify that you are requesting an extension for a **third-party app** (Getint), and attach the screenshot from Getint Support confirming the approval request.

1. **Wait for Atlassian's Approval:**

* Atlassian will review the request and notify you once the extension is applied.

#### For Jira Server/Data Center Users <a href="#for-jira-server-data-center-users" id="for-jira-server-data-center-users"></a>

If you are using Getint on **Jira Server or Data Center**, you can **generate one or more extended trial licenses** directly from the Atlassian Marketplace.

1. Go to **Manage apps** in Jira Administration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FbrlYu7hPFUwkbP4FbPtf%2FManage%20apps%20in%20Data%20Center.png?alt=media&#x26;token=78a57c29-08d4-47e3-bbd1-eba879d34802" alt=""><figcaption></figcaption></figure>

1. Find the **Getint app**, remove the current license key, and click **Update**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FLg16aqCc85DnYqHCBq4l%2FFinding%20the%20Getint%20DC%20app.png?alt=media&#x26;token=a996ffa4-8ea0-4521-801d-20605d0b5f5c" alt=""><figcaption></figcaption></figure>

1. Click the **Free Trial** button to begin a new trial request.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMpkvOl3Dbwe49uzDSGFn%2FGetting%20a%20free%20trial%20for%20the%20DC%20app.png?alt=media&#x26;token=f1eca77e-de92-41e3-bf14-680ff09c4d4e" alt=""><figcaption></figcaption></figure>

1. On the next screen, mark the checkboxes and click **Generate License**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FIwexcKi0Bp2455QFwntj%2FNew%20Trial%20License%20for%20DC.png?alt=media&#x26;token=263d3c7c-cc75-46a4-b8bd-ee9b7f488695" alt=""><figcaption></figcaption></figure>

1. Apply the license in Jira and enjoy another trial period (each extension adds 30 more days).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FhmIdeYa0Zr6Cve83mq47%2FCopy%20your%20license%20and%20extend%20your%20trial.png?alt=media&#x26;token=674e38a4-a55c-4506-8103-9f23904fcd72" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Data Center licenses can usually be extended multiple times (up to 5 total extensions).
{% endhint %}

#### For Non-Jira App Users <a href="#for-non-jira-app-users" id="for-non-jira-app-users"></a>

**Direct Extension Request:**

* Using the trial version of [app.getint.io](http://app.getint.io/) or the On‑premise deployment? No problem. Contact us to request a trial extension. Our team will walk you through the steps to extend your trial so you have plenty of time to continue testing.

If you require additional assistance, don't hesitate to get in touch with our support team.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FmNmcgv7EiaNxX2LTkq5D%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=e3bc4f73-2bed-47ae-a7fa-139dd809c092" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Jira Access and User Management

Integrating applications within Jira Server/Data Center and Jira Cloud environments requires careful consideration of access permissions and system configurations. This comprehensive guide provides step-by-step instructions tailored for both environments, ensuring a seamless integration process with Getint.

### Starting the Free Trial and Accessing the Getint App <a href="#starting-the-free-trial-and-accessing-the-getint-app" id="starting-the-free-trial-and-accessing-the-getint-app"></a>

#### **Jira Cloud Integration:** <a href="#jira-cloud-integration" id="jira-cloud-integration"></a>

**Admin User:**

1. **Access Atlassian Marketplace:**
   * Log in to your Atlassian account using admin credentials.
   * Navigate to the Atlassian Marketplace and select "Explore More Apps."
2. **Search and Install Getint:**
   * Search for the Getint app, select "Try it Free," and install it.
   * Go to "Manage Apps" and, if the trial hasn't started, click "Start Trial."
   * When the trial begins, select the Getint app under the "Apps" tab to initiate integration.
3. **Start the Integration:**
   * Users will be routed to the Getint app and prompted to begin their integration. Choose "Integration" or "Migration" to get started. [(Click here to learn how to begin the integration.)](https://docs.getint.io/guides/quickstart)

{% embed url="<https://youtu.be/GzmQYVt9U04>" %}

**Non-Admin Users:**

1. **Request App Authorization:**
   * Request app authorization from administrators.
   * Select the "Apps" tab, "Explore More Apps," and search for the Getint app.
   * Request installation and administrators will see the request under "Apps > View App Requests."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FpFug3GMkPKkBLgUAAUW3%2FRequest%20installation%20from%20your%20Jira%20admin.png?alt=media&#x26;token=10bdfee0-358a-4d32-bf6d-835cabbcbb97" alt=""><figcaption></figcaption></figure>

1. **Post-Approval:**

* After approval, administrators configure the app. Users will not be able to access or view the application until it is configured.

#### **Jira Server/Data Center Integration:** <a href="#jira-server-data-center-integration" id="jira-server-data-center-integration"></a>

**Admin User:**

1. **Access Atlassian Marketplace:**
   * Log in as an administrator, go to "Settings" under your avatar, then select "Atlassian Marketplace."
2. **Search and Install Getint:**
   * Search for the Getint app, choose "Free Trial," and accept the installation.
   * Generate the license and follow the steps that appear. Apply the license, go to "Manage Apps," and start the trial if not already initiated.
3. **Start the Integration:**
   * After trial or purchase, access the app by selecting admin in the left menu.
   * You will be transferred to the Getint app and prompted to start their integration. Choose "Integration" or "Migration" to get started.

{% embed url="<https://youtu.be/Zx8LPlSk5Rg>" %}

{% hint style="info" %}
**Note:** Admin access to the Jira Server/Data Center is necessary to administer the apps and enable downloads.
{% endhint %}

#### Verifying your trial license <a href="#verifying-your-trial-license" id="verifying-your-trial-license"></a>

1. Ensure that the steps generate a valid license. Go to Marketplace > Manage Apps and check the generated license. For Jira Server/DC and Cloud apps, these steps are applicable. For On-premise installation, the license will appear under Settings > License.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FOr3GudUE6HS0pjUAJKz7%2FChecking%20your%20license%20in%20Cloud%20apps.png?alt=media&#x26;token=0d3db4d9-1b81-4658-a8f2-06b12c2e86b4" alt=""><figcaption></figcaption></figure>

### User Access Feature <a href="#user-access-feature" id="user-access-feature"></a>

We are excited to introduce the User Management Feature, enhancing flexibility and enabling non-admin users to create and manage integrations starting from version 1.52.

#### **On-premise:** <a href="#on-premise" id="on-premise"></a>

1. **Switch the workspace:**

* Select the "Account" icon on the bottom left side and switch to Getint Administration
* Then select "Users" and tap on "Create User."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FYepxxq6j57NEaJGei3kS%2Fimage-20240617-125527.png?alt=media&#x26;token=bc3d9017-3b2c-42bc-bda1-38f484a5133f" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F6C7g6IzRFoWUx2IUN7IO%2Fimage-20240617-125725.png?alt=media&#x26;token=a34c292d-2096-4a21-be33-4ebde94cabd7" alt=""><figcaption></figcaption></figure>

* On the screen that appears, create a user with the desired credentials.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FbOwD0QTvbs1CiSecnKxq%2Fimage-20240617-130159%20(1).png?alt=media&#x26;token=0344c2c2-50b8-4e21-b954-0fe5c22f1512" alt=""><figcaption></figcaption></figure>

* The user will be created, and now you need to assign the Workspace that they have access to. Select the three dots on the right and click “Edit”. Assign the workspace, select “add access,” and enable the user.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FhJ0MbalgabXeSTXDYDCV%2Fimage-20240618-082411.png?alt=media&#x26;token=11b446e4-6fdb-415b-82b5-26211d3d58dc" alt=""><figcaption></figcaption></figure>

**Jira Cloud:**

1. **Enable User Management:**
   * Log in as an administrator in your Jira Cloud instance.
   * Go to Settings, select "User Management," then "Groups."
   * Create a group (e.g., getint-jira-azure), select "View details," and add members.
2. **Accessing the App:**
   * Users will now see the app under the "Apps" tab and should click on it.
   * The Getint app will open, prompting users to create a new integration if it is their first time accessing the app.

{% embed url="<https://youtu.be/BDDVf2mM1Xo>" %}

**Groups Naming Requirements**

To ensure smooth integration and avoid any confusion, all groups must follow this naming convention: **getint-jira-xxx**.

**Mandatory Format:**

* getint-jira-jira
* getint-jira-azure
* getint-jira-wrike
* getint-jira-servicenow
* getint-jira-monday
* getint-jira-notion
* getint-jira-airtable
* getint-jira-trello
* getint-jira-hubspot
* getint-jira-gitlab
* getint-jira-freshdesk
* getint-jira-zendesk
* getint-jira-clickup
* getint-jira-asana

{% hint style="warning" %}
**Important Note:** This naming convention is a must for proper integration. For example, if your integration is between Jira and Monday, ensure the group name follows this format: **getint-jira-monday**.
{% endhint %}

**Jira Server/Data Center (DC):**

1. **Enable User Management:**
   * Enter your Jira Server or Data Center instance and log in as an administrator.
   * Navigate to Settings, click the gear in the upper right corner of the screen, then select "User Management."
   * Select "Groups" and create a new group (e.g., getint-jira-azure).
2. **Add Members:**
   * Select "Add," and the newly created group will appear in the group list.
   * Choose "Edit members" and add the username, or select it from your user list. Select "Add selected users."

{% embed url="<https://youtu.be/DNERhFm-8jg>" %}

**Groups Naming Requirements**

Same as the steps for Jira Cloud, Jira Data Center Groups must follow this naming convention: **getint-jira-xxx**.

**Mandatory Format:**

* getint-jira-jira
* getint-jira-azure
* getint-jira-wrike
* getint-jira-servicenow
* getint-jira-monday
* getint-jira-notion
* getint-jira-airtable
* getint-jira-trello
* getint-jira-hubspot
* getint-jira-gitlab
* getint-jira-freshdesk
* getint-jira-zendesk
* getint-jira-clickup
* getint-jira-asana

{% hint style="warning" %}
**Important Note:** This naming convention is a must for proper integration. For example, if your integration is between Jira and ServiceNow, ensure the group name follows this format: **getint-jira-servicenow**.
{% endhint %}

**Accessing the App:**

**Non-administrative Users:**

* After being granted access, users can manage the integration, create a new one, and view logs and data.
* To see the application's contents, a non-admin user must get the URL to access the Getint app for now.

**Project Admin User:**

* If the user is a project administrator, they can locate the app in the project settings.
* On the project page, select "Project Settings." On the menu that appears, the Getint app will now appear.
* The Getint app will launch, allowing for creating and maintaining integrations.

**For all Non-Jira Admin Roles:**

* Other users' integrations are visible but cannot be managed or saved.
* Logs for these integrations are securely encrypted to protect data privacy and cannot be viewed.

This comprehensive guide ensures administrators and non-admin users can effectively navigate and utilize the Getint app within Jira Server/Data Center and Jira Cloud environments, promoting a smooth integration process. For further assistance, please get in touch with our support team at our [Help Center](https://getint.io/help-center).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FmNmcgv7EiaNxX2LTkq5D%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=e3bc4f73-2bed-47ae-a7fa-139dd809c092" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Deployment Options

Getint is engineered to cater to a diverse range of customer needs, including those with their own infrastructure (on-premise/data center), those preferring cloud-based services (SaaS), and organizations with stringent security requirements. Recognizing security as a pivotal concern for our customers and ourselves, we offer the option of on-premise deployment on the customer's own servers. This flexibility sets us apart in the market, offering tailored deployment options to meet specific needs.

**Deployment Choices:**

* **Jira Cloud - Cloud Hosted by Getint**: Our cloud-hosted solution provides a dedicated platform instance on Getint servers, with a separate database for each instance. This model is the standard for Jira Cloud applications. Jira Cloud customers looking for alternative deployment options can reach out to us at <support@getint.io> for personalized solutions.
* **Data Center – Native Application (Jira-Specific)**:&#x20;

  For organizations already running Jira Data Center, Getint offers a native application deployment. Unlike the standalone platform, this version is installed via the Atlassian Marketplace and resides within your existing Jira infrastructure.

  * **Host (Server) Maintenance**: Managed by the customer as part of their Jira Data Center maintenance.
  * **Architecture**: The app runs as a native plugin. For multi-node Jira clusters, Getint uses a cluster lock mechanism to ensure that synchronization tasks are executed on only one node at a time, preventing data duplication or conflicts.
  * **Data Residency**: All configuration details, logs, and synced item information are stored within your Jira instance's database and `JIRA_HOME` directory. This ensures that no data ever leaves your internal network.
  * **Security**: Operates entirely behind your firewall. Since it is a native app, it inherits the security protocols and user permissions already established in your Jira Data Center environment.
* **On-Premise - Hosted by the Customer**: To accommodate organizations with critical data security needs, such as those in the fintech and health tech sectors, we offer an On-Premise deployment option. This allows for the Getint platform to be installed on customer-owned servers, mirroring the functionality of our SaaS/Cloud model. Once installed and licensed, the platform operates independently of Getint servers, connecting only to authenticated applications set up by the client. All data, logs, passwords, and configurations are securely managed on the client's servers. This model is standard for Jira Server/Data Center applications, ensuring data security and autonomy.

**Why Choose Getint?**

Our commitment to security, coupled with the versatility of our deployment models, underscores our dedication to providing solutions that not only meet but exceed our clients' expectations. Whether you prioritize the control and security of on-premise hosting or the convenience and scalability of cloud services, Getint accommodates your specific requirements, ensuring that your data is handled with the utmost care and respect.

For more information on our deployment options or to discuss the best solution for your organization, please get in touch with us at our [Help Center](https://getint.io/help-center).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

<br>

# Getint for Jira Cloud

## Getint for Jira Cloud: Deployment & Architecture Guide

### Overview

Getint for Jira Cloud operates as a SaaS (Software as a Service) application. Unlike legacy Jira Server plugins that ran natively within the Java Virtual Machine (JVM) of the host server, the Cloud version functions as an external service that interacts with your Jira instance via secure web protocols.

This deployment model ensures that the integration platform runs independently of your Jira infrastructure, preventing performance impact on your primary project management environment.

### Technical Architecture

The integration relies on a distributed architecture comprising two main components: the Atlassian Connect App and the Getint Platform.

#### The Interface (Iframe-Based Loading)

When a user accesses Getint via the Jira Apps menu, the following process occurs:

* **Request Initiation**: Jira Cloud sends a request to Getint servers to load the application interface.
* **Iframe Execution**: The Getint administration panel loads within a secure iframe inside the Jira UI. This panel is hosted externally on Getint's infrastructure.
* **User Functionality**: From this panel, administrators configure integrations, map fields, and view synchronization reports.

#### Data Synchronization (REST API)

Actual data processing and synchronization occur via the Jira Cloud REST API:

* **External Execution**: The sync engine runs on Getint’s servers, not within Jira.
* **API Requests**: Getint sends authenticated HTTP requests to Jira to read issue data, write updates, upload attachments, or post comments.
* **Storage**: Configuration data (mappings, settings) and synchronization logs are stored on the Getint infrastructure.

### Deployment & Configuration

#### Installation (Direct via Atlassian Marketplace)

In 2025, the standard installation flow starts directly at the external marketplace rather than searching from within the Jira instance.

1. Navigate to [marketplace.atlassian.com](https://marketplace.atlassian.com) in your browser.
2. Search for **Getint** and select the application from the search results.
3. Click the **Try it free** button in the top right corner.
4. If prompted, log in with your Atlassian credentials.
5. Select the Jira Cloud site where you want to install the app from the dropdown menu.
6. Click **Start free trial** to confirm. The app will be installed on your selected instance, and you will be redirected to the success page.

#### User Group Setup

For Jira instances with restrictive permissions, you must follow a specific group naming convention.

* Required Format: `getint-jira-[target-tool]`
* Examples:
  * `getint-jira-azure` (for Jira to Azure DevOps)
  * `getint-jira-servicenow` (for Jira to ServiceNow)

#### Authentication Requirements

Because the application runs externally, it requires explicit authorization to access your Jira data. Getint uses API Token authentication rather than user passwords, adhering to Atlassian's security standards.

Required Credentials:

* User Email: The email address of the Jira account used for the integration (we recommend a dedicated service account).
* API Token: An Atlassian API Token generated from [id.atlassian.com](https://id.atlassian.com/manage-profile/security/api-tokens).

*Note: The Jira account used for the connection must have the necessary permissions (Browse Projects, Create Issues, Edit Issues) for all projects you intend to synchronize.*

### Security & Data Residency

* Infrastructure: The Getint platform is hosted on AWS (Amazon Web Services).
* Data Handling: While configuration and logs are stored on Getint servers to facilitate the service, the application connects directly to your Jira instance to process ticket data.
* Compliance: The application operates under the Atlassian Cloud Fortified program standards.

### Comparison: Cloud vs. Data Center

| **Deployment** | **Jira Cloud (SaaS)**  | **Jira Data Center (Native)** |
| -------------- | ---------------------- | ----------------------------- |
| Hosting        | Hosted by Getint (AWS) | Hosted on Customer Server     |
| Connectivity   | REST API (HTTP)        | Native Java API               |
| Maintenance    | Managed by Getint      | Managed by Customer           |
| Updates        | Automatic              | Manual Update Required        |

### Deployment Best Practices

* **Dedicated Integration User**: We recommend creating a "Service User" in Jira Cloud for the integration. This ensures that sync activities are not tied to a specific employee's account and provides a clear audit trail in the issue history (e.g., "Updated by Getint Sync").
* **Filter Early**: Use Getint's JQL-based filtering to only sync the tickets you need. This reduces unwanted syncs and optimizes performance.
* **Log Retention**: Customize your log retention settings in the Getint dashboard to align with your organization’s internal data privacy policies.

*For organizations with restricted cloud access, Getint also offers an On-Premise deployment option that can be installed on private servers behind your firewall.*

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FjrKGRyToPPdWu8WzVABo%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=29e3b121-8c4c-4ea7-b9c2-9c66a3308838" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Getint for Jira Data Center

## Getint for Jira Data Center & Server: Architecture & Deployment Guide

### Overview

Getint for Jira Data Center and Server is a native application built using the Atlassian Plugins SDK (P2 framework). Unlike the Cloud version, which is a SaaS service, the Data Center version resides entirely within your infrastructure. This deployment type is designed for high-availability environments and organizations with strict data residency requirements.

### 1. Technical Architecture

The application runs as a native plugin within the Jira Java Virtual Machine (JVM).

* **Clustered Environments**: For Jira Data Center instances with multiple nodes, Getint uses a cluster lock mechanism. This ensures that synchronization tasks are executed on only one node at a time, preventing data conflicts or duplicate syncs.
* **Scheduling**: The app initiates a background scheduled job to handle data integration. While users define the sync interval in the settings, the actual execution is managed by the Jira internal scheduler.
* **Internal Communication**: The app communicates with Jira via the Jira Java API and the Internal REST API.

### 2. Data Storage & Security

This deployment model is "Firewall-Friendly" and does not require outbound access to external Getint servers.

* **Local Storage**: All configuration details, mapping logic, and synchronization metadata are stored within your own Jira Database (in dedicated Getint tables).
* **File Storage**: Synchronization logs and temporary files are stored in the `JIRA_HOME/log/getint` directory (or the root `JIRA_HOME` If no log folder exists.)
* **Zero External Connectivity**: When deployed in a standalone on-premise capacity, the platform operates independently of `getint.io` servers. No ticket data ever leaves your internal network.

{% hint style="info" %}
We know Data Center admins have to be careful about storage bloat. If you ever decide to uninstall the app, feel free to clear out any leftover Getint database tables and log files. It’s completely safe to delete them, and it’s actually a great way to keep your instance optimized and clutter-free.
{% endhint %}

### 3. Installation & Licensing

Following the 2025 standard, installation is managed directly via the Atlassian Marketplace.

1. Navigate to the [Atlassian Marketplace](https://marketplace.atlassian.com).
2. Search for Getint and select the version compatible with Data Center.
3. Click Get it now or Try it free.
4. Log in to your Jira instance as a System Administrator.
5. Navigate to Administration (Gear Icon) > Manage Apps.
6. Upload the `.jar` or `.obr` file if you downloaded it manually, or confirm the installation from the Marketplace prompt.
7. License Verification: Access the license settings within the Getint menu to apply your Marketplace license key.

### 4. User Access & Permissions

To manage integrations, users must be granted specific access through Jira Groups.

* Admin Access: System Administrators see the "Getint" menu by default.
* Delegated Access: To allow non-admin users to manage specific integrations, create a group following the naming convention: `getint-jira-[target-tool]` (e.g., `getint-jira-azure-devops`).
* Service Account: We recommend using a dedicated "Service User" to establish the connection. This provides a clear audit trail in issue histories (e.g., "Updated by Getint Integration").

### 5. Key Comparison: Data Center vs. Cloud

| **Feature**     | **Data Center (Native)**     | **Jira Cloud (SaaS)** |
| --------------- | ---------------------------- | --------------------- |
| Hosting         | Customer Infrastructure      | Getint (AWS)          |
| Data Storage    | Local Database & JIRA\_HOME  | Getint Infrastructure |
| Cluster Support | Native Cluster Lock          | Multi-tenant SaaS     |
| Maintenance     | Managed by Customer          | Managed by Getint     |
| External Access | Not Required (Firewall safe) | Required (SaaS model) |

For organizations ready to begin their integration, you can initiate a 30-day free trial directly through the **Atlassian Marketplace** to evaluate the platform in your sandbox or production environment. If your deployment involves complex high-availability configurations or specific security requirements, you can schedule a technical consultation with a Getint specialist. For more information, feel free to contact us at our [Help Center](https://getint.io/help-center).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FjrKGRyToPPdWu8WzVABo%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=29e3b121-8c4c-4ea7-b9c2-9c66a3308838" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Getint Jira Server / Jira Data Center App (native)

**Introduction to Getint.io Native Apps for Jira Server and Jira Data Center**

In December 2022, we proudly launched our first "native" applications for Jira Server and Jira Data Center. Developed using the Atlassian Plugins SDK, these apps integrate seamlessly within your Jira environment, alongside other applications. They are designed to facilitate comprehensive integration and synchronization between Jira and various collaboration software tools such as ServiceNow, Azure DevOps, Asana, Monday.com, GitLab, and more.

## Installation Guide

1. Log in with Administrator credentials and navigate to the **'Manage Apps'** section in your Jira instance.

![](https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FC5GlNTqq8PQDWOGQkbvZ%2FScreenshot%202022-12-18%20at%2013.35.48.png?alt=media\&token=28797e01-fed3-4faf-9720-eb31b682d5e8)

1. Search for our integration apps, selecting the one that suits your needs (e.g., Azure DevOps Jira integration), and initiate the Free Trial.

![](https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FGLzmKVo5I5mm7hXCPyaB%2FScreenshot%202022-12-18%20at%2013.36.49.png?alt=media\&token=022593c7-6499-416f-850b-78dc3ea1cff9)

1. After installation, access 'Manage Apps' from the left sidebar to ensure a valid license is active for the newly installed app.\
   \
   ![](https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FKdxXAG4ijA3sKo3bXJlu%2FScreenshot%202023-02-16%20at%2009.38.04.png?alt=media\&token=95d8de57-771c-4438-9ee3-e0ce6bf5d28e)<br>
2. Post-installation, a Getint section will appear on the left vertical menu. Clicking on this link will direct you to the app’s dedicated page, where you can begin creating your integrations.

![](https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FvRM8yOlMabsaINADLXPi%2FScreenshot%202022-12-18%20at%2021.11.37.png?alt=media\&token=1f518a99-3486-4f5a-8022-2368be7d6af8)

You will be navigated to a dedicated page of the app.&#x20;

You can start building your integrations!&#x20;

## Starting the synchronisation

Immediately after installation, the app initiates a scheduled job responsible for executing integrations and performing data cleanups.

**Jira Data Center Consideration:** For instances running on more than one node, a cluster lock ensures Getint operates on a single node at a time.

## App Data and Database

Getint stores configuration details and synced item information within the database. It also generates detailed log files for each sync, aiding in error analysis and support. The app creates several tables for storing data, including configurations, syncs, runs, and error logs.

**Database**

Getint creates the following tables to store configuration details and data related to synchronization processes:

* getint\_connections
* getint\_integrations
* getint\_runs
* getint\_syncs
* getint\_steps
* getint\_artifacts
* getint\_per\_artifacts
* getint\_syncs\_errors
* getint\_tenant\_info

**Log files**

Logs capture valuable details on the actions undertaken to synchronize specific items. The directory for these logs is located at:

* If the JIRA\_HOME directory includes a log directory, a 'getint' directory will be created within it.
* If the JIRA\_HOME directory lacks a log directory, the 'getint' directory will be directly created within the JIRA\_HOME directory.

**Clean up**

Each integration run is meticulously recorded in the database and accompanied by a log file. With numerous integrations potentially executing hundreds of times daily, this can lead to an accumulation of extensive files and database records. Getint.io offers a solution to manage this data efficiently by allowing users to specify a retention period for these records.

To set a data retention limit, follow these three steps:

1. Navigate to the Settings page via the main menu.
2. Enter the desired maximum number of days for data retention.
3. Confirm your settings by clicking 'Save'.

![](https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fx1BBOZFNr1Fv1znz2zcM%2FScreenshot%202022-12-18%20at%2021.13.55.png?alt=media\&token=b0ddecb2-6703-4ee6-b461-57585137d858)

After defining the retention period, a scheduled cleanup task will automatically run every 8 hours to remove outdated data, ensuring your system remains efficient and clutter-free. Please note, the initiation of the first cleanup might be delayed following the setup.

## Differences in features&#x20;

The native apps for Jira Server/Data Center currently do not support a few features that are available in other versions. These include:

* Bulk Resynchronization
* Advanced Scripting Capabilities
* Preview of Background Job Status
* Notifications

**Integration Interval Configuration**

The integration interval for Server/Data Center apps, as specified in the settings, represents the intended frequency for integration executions. However, the actual scheduling of these integration jobs is managed by Jira's internal logic, which determines when the jobs are permitted to run. Consequently, the practical interval between integration runs may exceed the predefined settings.

![](https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FOawnU17huSjZOrPAccqy%2FScreenshot%202023-04-03%20at%2022.39.10.png?alt=media\&token=c0c486da-eeca-4b73-ad3e-3e928f40489c)

## Testing Recommendations

It's best practice to conduct testing in a development or local environment rather than directly in a production setting. To facilitate this, you have the option to download Jira and install it on a temporary machine or your personal computer. Alternatively, a dockerized version of Jira is available at <https://hub.docker.com/r/atlassian/jira-software>. For licensing during setup, Timebomb licenses can be utilized, accessible at <https://developer.atlassian.com/platform/marketplace/timebomb-licenses-for-testing-server-apps>, simplifying the entire setup process.

## Uninstall

Upon uninstallation, Getint will halt all scheduled jobs, stopping further synchronizations. However, log files generated during the app's operation will remain intact.

This guide aims to streamline the installation, operation, and management of Getint native apps within your Jira Server or Data Center environment, ensuring a smooth integration process with other collaboration tools.

###

# Getint for Jira Data Center / Jira Server - Architecture

Jira Server / DC apps are basically installed on the target Jira Server / DC and loaded up within a Jira system, which makes them accessible for the Jira end users. Those Jira Server / DC apps are written mainly in Java with support of Atlassian plugins framework.

Because, as stated on Architecture page, getint.io is a standalone, separate platform, there is still a need to have an instance of getint.io platform installed somewhere. It can be either hosted still by getint.io or installed (as on-premise) on customers owned Linux/Windows servers.

Below diagram, shows simplified architecture of how getint.io cooperates with Jira Server, when getint.io is installed as **On-Premise** software.

![](https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MR6Z9V8zLATPQPOGSDf%2F-MSvBbkykpjkiLXBC9CU%2F-MSvEWSSpsI4x-94BCnt%2FJira_Server_DC_Architecture_OnPremise.png?alt=media\&token=a912db17-dee1-4887-83d2-589e3fd13214)

Components overview

* Getint.io Jira App - its a one of our apps available on Atlassian Marketplace. When its clicked from *Mange Apps* menu, Jira Server / DC will try to load up (Request 1) an iframe with a source from the getint.io platform. \
  Except administration panel (UI), Jira app  is used also for License verification purposes.
* Request 1 - it's a request sent by Jira Cloud in order to load up content within an iframe. That iframe will contain an administration panel of the app where all integrations can be managed as well as whole reporting and other system informations can be accessed. When request is successfully authenticated, UI is loaded up
* All the configurations and reporting data is stored **on the owned by customers servers**&#x20;
* Request 2 - getint.io platform to perform data integration is using standard Jira REST Api. Because all of the requests to Jira REST Api must be authenticated, during integration setup user is asked to provide user credentials (username and password)

{% hint style="info" %}
As can be noticed on the above diagram, with a on-premise deployment mode, getint.io platform and Jira apps are not trying to connect with any servers, including getint.io servers. **That means it is possible to work totally behind firewall.**
{% endhint %}

# Getint On-Premise

To meet the data security requirements of different organizations (like fintech, and health tech companies with very sensitive data), we offer the On-Premise deployment version.&#x20;

This is practically the same version as the one created in the SaaS/Cloud model, but possible to be installed directly on customers' servers.

{% hint style="info" %}
The On-Premise version of getint.io allows you to be the **owner and administrator** of the processed data during the integration/synchronization.

With that deployment mode, you can have Getint working **fully behind the firewall**. No requests will be performed, except for the apps you are integrating with.
{% endhint %}

## Comparison

| Feature                                                   | On-Premise                | SaaS (Cloud)               | Data Center                |
| --------------------------------------------------------- | ------------------------- | -------------------------- | -------------------------- |
| Integration run interval                                  | >= 0s                     | min 180 seg (3 mins)       | min 120 seg (2 mins)       |
| Multithreading                                            | Supported                 | -                          | Unsupported                |
| Multi-tenancy                                             | Supported                 | One customer - One tenant  | Unsupported                |
| Software update                                           | Performed by the Customer | Applied by Getint          | Performed by the Customer  |
| Host (Server) maintenance                                 | Customer                  | Getint.io                  | Customer                   |
| Data retention                                            | Configurable              | Fixed. Max 1 month         | Configurable               |
| Health monitoring                                         | Customer responsibility   | Handled by Getint          | Customer responsibility    |
| <p>Max number of items<br>to sync per integration run</p> | Unlimited                 | Connector based (max 1000) | Connector based (max 1000) |
| <p>Max number of items<br>to sync per migration run</p>   | Unlimited                 | 10000                      | 10000                      |

If you have further questions about our pricing, please visit [Getint.io](https://www.getint.io/) or contact us at our [Support Centre](https://getint.io/help-center). Our integration experts are always happy to help.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Architecture

Getint.io platform is designed to work as a clustered system with multiple tenants under each cluster. So its possible to create multiple clusters and point forward incoming requests to specific cluster basing on their e.g. subdomains (like <https://cluster1.getint.io.company.com>).

**With such approach, its possible to**

* run multiple clusters integrating different apps / software of organisation
* separate and perform integrations of particular partners on dedicated clusters
* within a cluster, setup integrations on separate tenants (e.g. put more resource intensive or business critical integrations on separate tenants)
* have getint.io platform running **Fully Behind Firewall**

{% hint style="info" %}
On-Premise version of getint.io allows you to be the **owner and administrator** of the processed data during the integration / synchronization.

With that deployment mode, you can have getint.io working **Fully Behind Firewall**. No requests, except to the apps you are integrating will be performed.&#x20;
{% endhint %}

Below you can find cluster high level architecture diagram

![](https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MR6Z9V8zLATPQPOGSDf%2F-MSvBbkykpjkiLXBC9CU%2F-MSvE5wFtOei_jda7rtW%2FOnPremise_Cluster%20\(2\).png?alt=media\&token=da22bd9b-7c35-4b76-805d-6bd75eb7a4e5)

Overview

* **Incoming HTTP Requests** is containing information about a cluster and tenant to which it wants to reach. That info can be attached to requests under different technics but for not only subdomain approach is supported. So each tenant within each cluster is having different subdomain e.g. tenant1.getint.mycompany.com
* **Load balancer** is directing the request to the proper cluster
* **Spring Web Application** is the main heart of the cluster. It is receiving incoming requests, authenticates them, extract info about tenant and performs business logics to return a data
* **React UI** is a chosen framework for building modern UI. Its packaged and included within Spring Web Application and server when user visits administration panel
* **Tenant N Thread** as said before, clusters supports *multi-tenancy*. For every tenant separate integration thread is created which is responsible for performing data synchronization according to configured integrations by tenant users
* **PostgreSQL** is a RDBMS of our default choice. Years of experience with that db system make us sure its the best choice we could as a heart of a platform data storage. One of the biggest advantages we found was different supported ways of data replication and most importantly, possibility to store non-relations data
* **Tenant Schema** is created for each tenant within a database to which that cluster is connected. Each tenant has the access **only** to its schema.&#x20;

# Installation

For those looking for enhanced performance, superior workflow management, efficient operations, and robust data security, On-Premise emerges as an exceptional solution. You’re in control of your data during any changes or updates, and it all happens within your custom server. This ensures that there are no other requests, except for the applications you are integrating. Thus, On-Premise offers a compelling blend of power and privacy.

### How to Install On-Premise <a href="#how-to-install-on-premise" id="how-to-install-on-premise"></a>

This detailed guide will cover all the necessary steps to install [getint.io](http://getint.io/) in your dedicated network.

#### Installation requirements <a href="#installation-requirements" id="installation-requirements"></a>

* Ubuntu / Debian / Redhat / Windows server / Docker - Server requirements
* **Root user** access
* Your Getint binary and License files. If you do not have them, please get in touch with us at [**support@getint.io**](mailto:support@getint.io)

#### Server requirements <a href="#server-requirements" id="server-requirements"></a>

| Minimum   | Recommended |
| --------- | ----------- |
| 2GB Ram   | 4GB Ram     |
| 1 vCPU    | 2 vCPU      |
| 60 GB HDD | 60 GB SSD   |

#### Installation steps <a href="#installation-steps" id="installation-steps"></a>

1. **Open your terminal and sign in to the machine as a root user.**
   * Use the SSH command and replace `youripaddress` with the hostname or IP address of the server:

| ssh root\@youripaddress |
| ----------------------- |

1. **Enter your password:**
   * You’ll be prompted to enter your password for the specified username
2. **Download Getint files:**
   * Getint will provide these. Use the command `wget` + the link to the files to download the installation package
   * Use the command `ls -al` to see the files in the current directory, and ensure the zip files are located there
3. **Extract the files**
   * Use the `unzip` command to extract Getint files in the directory. For instance, it should be like this: `unzip getint-1.58.zip`
   * Run `apt install unzip` to download an unzip tool if you don’t have one
4. **Switch to the Getint directory**
   * After the installation, switch the directory to the new Getint folder by running `cd getint`
   * Now enter `cd synchronizer` to open the Getint installation folder
5. **Make sure you have the necessary tools to run Getint**
   * Install Java if it isn’t available on your machine. Enter the command `apt install default-jre` and press **Y** then **Enter** when prompted. Press **ctrl + c** to return to the directory.
   * Make sure Java is now installed with the command `java --version`

{% hint style="warning" %}
Please note that we support Java versions 8 through 17.
{% endhint %}

1. **Running Getint**

* Use the command `./manager.sh start` to launch Getint. Press **ctrl + c** to close the logs and return to the directory
* Check if Getint is up and running in the background by using the command `ps -aux | grep getint`

1. **Accessing Getint**

* These are the credentials you can use to log into Getint via your browser:
  * Username: admin
  * Password: admin
* Open the browser and type the URL which is the machine’s IP address. Alternatively, if you have any domain name assigned to the machine on which Getint is installed, you can type that domain name
* Other commands you can use to manage your instance:
  * `./manager.sh stop` stops the integration, so you won’t be able to access it until you start it again
  * `./manager.sh restart` restarts the integration in case you have made some changes to the directory

Getint will start on port 80 by default. If port 80 is already in use, change it with the command `vim getint.env`

After switching ports, use the command `cat getint.env` to see the current port in use.

#### Video tutorial <a href="#video-tutorial" id="video-tutorial"></a>

Here’s a video tutorial that demonstrates how to install the On-Premise version.

{% embed url="<https://www.loom.com/share/8f018d0128fc45178d5b27346cba707a?sid=fd9f751c-6a9e-423f-bb11-b343c1293cbe>" %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FvfdnR8QBDNRNmvHoH6lW%2FGetint%20White%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=72cfc2d7-2f26-47ec-9eb6-1bdeacaf470f" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>

### **Docker - Docker-compose installation** <a href="#docker-docker-compose-installation" id="docker-docker-compose-installation"></a>

The initial steps are similar to installing Getint on your dedicated machine, but they have remarkable differences in how the app is installed and fully executed. Ultimately, it will depend on your server requirements.

As Docker is a separate tool, please ensure it is installed on your machine before running Getint. Otherwise, Getint won’t start, and your terminal will pop up an error.

1. **Open your terminal and sign in to the machine as a root user.**
   * Use the SSH command and replace `youripaddress` with the hostname or IP address of the server:

| ssh root\@youripaddress |
| ----------------------- |

1. **Enter your password:**
   * You’ll be prompted to enter your password for the specified username
2. **Download Getint files:**
   * Getint will provide these. Use the command `wget` + the link to the files to download the installation package
   * Use the command `ls -al` to see the files in the current directory, and ensure the zip files are located there
3. **Extract the files**
   * Run `apt install unzip` to download an unzip tool if you don’t have one
   * Use the `unzip` command to extract Getint files in the directory. For instance, it should be like this: `unzip getint-1.58.zip`
4. **Switch to the Getint directory**
   * After the installation, switch the directory to the new Getint folder by running `cd getint`
   * Now enter `cd synchronizer` to open the Getint installation folder
   * Use the command `cd docker`, and then `cd scripts`
5. **Installing docker if it isn't installed on your machine**
   * The installation path will depend on the tool you’re using. For example, we’re using Ubuntu 20, and the installation package is available here: [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/). However, if you’re using a different distribution, click on **Docker Engine**, then click on **Install**, and locate your distribution under this page. After the installation, use the command `docker version` to ensure the tool is installed

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FjGAYIVZuO28CfzCOpSWY%2F912ba1c97c369e7ccb5bee2071a62ca3.png?alt=media&#x26;token=f54729ab-db24-420a-bd66-3d980a98dc5b" alt=""><figcaption></figcaption></figure>

1. **Installing docker-compose on your machine**
   * It is also necessary to have docker-compose as our installation will consist of the PostgreSQL database, Nginx, and the Getint app. After the installation, use the command `docker-compose version` to ensure the tool is installed
   * Docker-compose standalone is available here: [Install Compose standalone](https://docs.docker.com/compose/install/standalone/)
2. **Running Getint**
   * While in the scripts folder, enter the command `sh start.sh` to launch Getint
   * Ensure Getint is running in the background by using the command `docker container ls`
3. **Accessing Getint**
   * These are the credentials you can use to log into Getint via your browser:
     * Username: admin
     * Password: admin
   * Open the browser and type the URL which is the machine’s IP address. Alternatively, if you have any domain name assigned to the machine on which Getint is installed, you can type that domain name
   * Other commands you can use to manage your instance:
     * `sh stop.sh`
     * `sh restart.sh`

Getint will start on port 80 by default. If port 80 is already in use, change it with the command `vim ../docker-compose.yaml`

After switching ports, use the command `docker container ls` to see the current port in use.

#### **Video tutorial** <a href="#video-tutorial.1" id="video-tutorial.1"></a>

Here’s a video tutorial on how to Install Getint in a docker.

{% embed url="<https://www.loom.com/share/4beb603104b245cbbaacef013032ac7d?sid=cc553c61-a37d-4839-b2be-329ab722ff2f}>" %}

{% hint style="info" %}
Our amazing team at Getint is always here to support you throughout your integration journey. We specialize in providing the best possible customer experience. If you have any questions about the setup process, please open a ticket with us at our [Help Center](https://getint.io/help-center) or [Schedule a Demo](https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team).
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# How to Install Getint On-Premise in Windows Server

This guide provides a step-by-step process for setting up PostgreSQL, Java, and Getint on Windows Server. It covers the installation and configuration of PostgreSQL, downloading and preparing the trial version of our app, and running the application. With these instructions, you can smoothly set up and integrate Getint into your workflow.

{% hint style="warning" %}
This guide is only intended for Getint version v1.70 and above. Please ensure your Getint version is updated to this version before proceeding.
{% endhint %}

### Installing Getint in Windows Server <a href="#installing-getint-in-windows-server" id="installing-getint-in-windows-server"></a>

#### 1. Install PostgreSQL

* Follow all the steps located on the **PostgreSQL** website [here.](https://www.postgresql.org/docs/current/installation.html) All the software packages situated on this website are essential to PostgreSQL's correct function, which would equal the proper installation of Getint.

#### 2. Install JAVA JDK

* Download and install from Oracle's official site: [Java JDK.](https://www.oracle.com/java/technologies/downloads/?er=221886)

{% hint style="info" %}
At Getint, we support Java versions 8 through 17.
{% endhint %}

#### 3. Download and Unzip Getint

* Download the **Getint .zip package** from the provided source.
* Unzip the **downloaded file** to a location of your choice on the Windows Server. For example, you can unzip it to C:\Users\Administrator\Downloads\getint-1.68.
* The [Getint](http://getint.io) team will provide the URL to download the trial version. Please visit our [support portal](https://getint.io/help-center) and open a ticket if you need to download the latest version of Getint for your Windows Server.

#### 4. Open Command Prompt and Navigate to the Synchronizer Folder

* Open a terminal (Command Prompt) on the Windows Server.
* Navigate to the unzipped folder by using the cd command. For example:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FJkg8YCckPMaCfcgNR5gy%2Fcmd%20synchronizer%20file.png?alt=media&#x26;token=07ce24e4-da39-4d4d-9559-7aae4dd118ab" alt=""><figcaption></figcaption></figure>

#### 5. Start Getint

* **Execute** the `call manager.bat start` command to start Getint:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FBMpsuIpHU1cC4cpSboNv%2Fmanager.bat%20start%20command%20to%20initiate%20Getint.png?alt=media&#x26;token=6c44021b-6e7d-43c8-98c8-39d4c060c1b3" alt=""><figcaption></figcaption></figure>

* Getint will start on **port 80** by default.

* **To change the port**, open the manager.bat file and modify the port number by changing the line set PORT=80 to, for example, set PORT=8080. Then, **restart Getint** if it's already running.

* **To change the database** (you may use our database during the trial period), you can modify the datasource variables also defined in the manager.bat:

  ```

  set SPRING_DATASOURCE_USER=sa
  set SPRING_DATASOURCE_PASSWORD=
  set SPRING_DATASOURCE_DRIVER=org.h2.Driver
  set SPRING_DATASOURCE_URL=jdbc:h2:~/getintio-db;DB_CLOSE_DELAY=-1;INIT=CREATE SCHEMA IF NOT EXISTS public
  ```

* For example, to connect to the Postgres database, you can provide the following values:

  ```
  set SPRING_DATASOURCE_USER=postgres
  set SPRING_DATASOURCE_PASSWORD=postgres
  set SPRING_DATASOURCE_URL=jdbc:postgresql://localhost:5432/getint
  set SPRING_DATASOURCE_DRIVER=org.postgresql.Driver
  ```

{% hint style="info" %}
Running the .bat file in this manner will execute its commands in the foreground. This means the process will continue to run as long as the console remains open. Closing the console will stop the process, causing the [Getint.io](http://getint.io) .jar file to stop running. You must set the .bat file as a Windows Service to ensure it runs permanently.
{% endhint %}

#### 6. Open Your Browser and Access Getint

* **Open a web browser** on the same machine where Getint is running. Open your browser and type the URL, which is your machine's IP address. Alternatively, if you have a domain name assigned to the machine on which **Getint** is installed, you can type that domain name. If you have used a port other than 80, remember to include it in the address (i.e., the URL would be `http://10.0.0.32:8089`).
* **Type the machine's URL:**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FcrTkiNhR9UATL0Uz4Nvl%2FURL%20for%20Getint%20Initialization.png?alt=media&#x26;token=8220bf07-8c58-40fb-b6c6-c772c74402bc" alt=""><figcaption></figcaption></figure>

* Replace PORT with the port number configured in the `getint.env` file (default is 80).
* **The Getint UI should load.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FskvtAidJbWEcO1zbFSbf%2FGetint%20UI.png?alt=media&#x26;token=22b5d621-b57a-4f0b-82e3-2c3ffafbb0ac" alt=""><figcaption></figcaption></figure>

#### 7. Log In

* Use the following default credentials to sign in:
  * Username: admin
  * Password: admin

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FvFH4ZVAPdAMNoSCliAvc%2Fcredentials%20for%20getint%20usage.png?alt=media&#x26;token=c20e468f-d941-4491-b13c-0e2024e20e92" alt=""><figcaption></figcaption></figure>

#### 8. Running Getint in the Background Using the Task Scheduler

To allow Getint to launch on startup, you can create a **Basic task** and add it to the **Task Scheduler** as shown below.

* Open the Task Scheduler, and click **Create Basic Task.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F22wUgNUHMUnfbQsT2znP%2FOpening%20the%20Task%20Scheduler.png?alt=media&#x26;token=f3c402e2-dbd6-4192-9444-d8dcb6f7d527" alt=""><figcaption></figcaption></figure>

* Name your task to identify it easily if you need to make changes later.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FnXL6XzChw9X1P9y0R5AR%2FName%20your%20task.png?alt=media&#x26;token=e75a7927-4523-45ea-bd92-f612d57620db" alt=""><figcaption></figcaption></figure>

* Select the trigger for your task, also known as when you want the task to start. Select **when the computer starts,** so the run.bat file launches during each startup.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FJR6NMjJXsWCpmjYcTep0%2FSelect%20the%20trigger.png?alt=media&#x26;token=42e97f07-5a7a-44df-89d5-c396db43f2db" alt=""><figcaption></figcaption></figure>

* Select **start a program.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FIIaFk06dhSN9LwzI0nYc%2FStarting%20a%20Program.png?alt=media&#x26;token=9e2891ee-cde7-48e4-922b-64a0b9a74dec" alt=""><figcaption></figcaption></figure>

* Use the Getint path to configure the task.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F2NAe86c6vAflpn2Ymcox%2FUse%20Getint%20path%20to%20set%20the%20task.png?alt=media&#x26;token=85d90014-3f72-491a-bcbf-ae1cf76cce72" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If you need any further help or if you are experiencing issues with your installation, feel free to open a support ticket at our [Support Portal.](https://getint.io/help-center)
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# On-Premise/Standalone Guide

### Changing Getint license

* Navigate to SYSTEM
* Click on LICENSE tab
* Click EDIT button
* Paste received license from support team
* Click SUBMIT button

New license should be applied and already used by GetInt

### Running GetInt on different HTTP port / HTTPS

GetInt application is Java web application that as all other web apps, can be run on different HTTP ports. HTTP port 80 is a default port.&#x20;

**How to change port?**

You can simply change it in getint.env file, value for PORT variable, e.g. change it to 8080 port.

```
PORT=8080
```

After a change restart of application will be needed.

**Setting up HTTPS with SSL certificate**

At the moment, easiest way of doing this is to use some proxy server like NGINX which will handle SSL certificates and proxy traffic to GetInt application.

For NGINX, here is a configuration file that when included into NGINX main configuration, will listen at 443 port and for traffic to \<DOMAIN>. It is loading SSL cert and key. Such traffic will be internally proxied to GetInt application running on \<PORT> port.

\<DOMAIN> and \<PORT> is sth that you have to specify according to your GetInt deployment. \<DOMAIN> is domain name which you open when you want to access GetInt and \<PORT> is a port defined in getint.env file.

```
server { 
    listen 443; 
    server_name <DOMAIN>; 
    ssl_certificate     /opt/getint/certs/fullchain.pem;
    ssl_certificate_key /opt/getint/certs/privkey.pem;
    ssl on; 
    ssl_session_cache  builtin:1000  shared:SSL:10m;
    ssl_protocols  TLSv1 TLSv1.1 TLSv1.2;
    ssl_ciphers HIGH:!aNULL:!eNULL:!EXPORT:!CAMELLIA:!DES:!MD5:!PSK:!RC4;
    ssl_prefer_server_ciphers on; 
    
    location / { 
        proxy_pass http://localhost:<PORT>; 
        proxy_set_header        Host $host; 
        proxy_set_header        X-Real-IP $remote_addr; 
        proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for; 
        proxy_set_header        X-Forwarded-Proto $scheme;
        proxy_read_timeout  90; 
        proxy_redirect http://127.0.0.1:<PORT> $host;
    } 
}
```

### Updating version

At the moment updates are handled manually.&#x20;

There is experimental feature for performing updates in almost fully automatic way but its not yet ready to use in production.&#x20;

**Manual way**

* Download and unpack new version of GetInt
* From unpacked directory, copy getint.jar file from synchronizer/libs dir and copy to \<CURRENT\_INSTALLATION>/synchronizer/libs directory
* Restart application

{% embed url="<https://www.youtube.com/watch?v=uCHNWq1jdiU>" %}

# Updating On-Premise

### How to update Getint On-Premise deployed on Linux <a href="#how-to-update-getint-on-premise-deployed-on-linux" id="how-to-update-getint-on-premise-deployed-on-linux"></a>

1. **Open your terminal and sign in to the machine as a root user.**
   * Use the SSH command and replace `youripaddress` with the hostname or IP address of the server:

| ssh root\@youripaddress |
| ----------------------- |

1. **Enter your password:**
   * You’ll be prompted to enter your password for the specified username
2. **Open your Getint folder**
   * Enter`cd getint` to switch to the Getint directory
   * Now enter `cd synchronizer` to open the Getint installation folder
3. **Download Getint files:**
   * Getint will provide these. Use the command `wget` + the link to the files to download the installation package. For example, `wget <URL_FROM_GETINT_TEAM>`
   * Use the command `ls -al` to see the files in the current directory, and ensure the zip files are located there
4. **Updating Getint**
   * Run the command `./upgrade.sh` + the zip file. For example, the full command should be `./upgrade.sh getint-1.62.zip`
   * Wait for the files to install and use **ctrl + c** to close the logs and return to the directory
   * Alternatively, if you didn’t download the installation package, you can use this command to upgrade your version directly without downloading Getint files separately `./upgrade.sh` + the link to the files.
5. **Access Getint and ensure the version was updated**
   * These are the credentials you can use to log into Getint via your browser in case you didn’t change them when installing Getint for the first time:
     * Username: admin
     * Password: admin
   * Open the browser and type the URL which is the machine’s IP address. Alternatively, if you have any domain name assigned to the machine on which Getint is installed, you can type that domain name
   * Within Getint, look for the **“?”** icon in the bottom left corner of your screen, and click on it. This will show your current software version. Please verify that your version was upgraded successfully

{% hint style="info" %}
Please test your integration to confirm that it is working without errors. Additionally, if you previously experienced any issues with Getint, check whether they have been resolved after the update. If not, please reach out to our support team at <support@getint.io>, and we’ll assist you accordingly.
{% endhint %}

#### Video tutorial <a href="#video-tutorial" id="video-tutorial"></a>

{% embed url="<https://www.loom.com/share/7805f1a26c924f8ea5d4df7e8df6021d?sid=65ea022c-6b61-4b74-bfb3-4d72d7496300>" %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Cluster High Availability

Availability, in the other words uptime of any software can be implemented in several different ways. It's up to company decisions, policies and best practices which process should be implemented.

## Monitoring

## Availability&#x20;

Getint.io Cluster application is a combination of different components, mainly Java Application, PostgreSQL database, NGINX balancer. All being built with different frameworks and running independently from each other. All can run on a one or multiple machines, it all depends on a deployment architecture you select.&#x20;

All of above, can become a point of failure, but after all, business directly depends on a Cluster application and this is what we will focus in first place to monitor and ensure highest possible uptime.

We decided to prepare for you a short guide taking you step by step on how to setup basic and efficient low level monitoring over a Cluster application processes with **Monit** and how to start them up in case of failure.

**Install Monit**

```
sudo apt-get update && sudo apt-get upgrade
sudo apt install monit
sudo monit
```

**Configure**

```
sudo systemctl status monit
# you should see info saying monit is running

sudo vim /etc/monit/monitrc
# - change interval to 60 seconds:
# - uncomment set httpd lines if you want to access monit web ui
```

/etc/monit/monitrc file would look like this

```
  set daemon 60            # check services at 2-minute intervals
  with start delay 240    # optional: delay the first check by 4-minutes (by

  set log /var/log/monit.log

  set idfile /var/lib/monit/id
  set statefile /var/lib/monit/state

  set eventqueue
      basedir /var/lib/monit/events # set the base directory where events will be stored
      slots 100                     # optionally limit the queue size

 set httpd port 2812 and
     use address <YOUR_IP_ADDRESS>  # only accept connection from localhost
     allow localhost        # allow localhost to connect to the server and
     allow admin:monit      # require user 'admin' with password 'monit'

   include /etc/monit/conf.d/*
   include /etc/monit/conf-enabled/*
```

Reload Monit

```
sudo systemctl restart monit
sudo systemctl enable monit
```

..

# How to Enable Multi-Threading in Getint

### Enabling Multi-Threading in Getint

Getint supports a multi-threading configuration, allowing integrations to run in parallel. In an **on-premise deployment**, multiple threads can be assigned per tenant based on a predefined setting.

#### Configuring Multi-Threading for On-Premise Deployments

To enable multi-threading, define a **custom property** specifying the number of threads allocated to each tenant. Follow these steps:

1. Navigate to **Custom Properties** (<https://docs.getint.io/getintio-platform/settings/how-to-override-getint-behavior-using-custom-properties> ).
2. Add a property named SYNC\_THREADS\_NUMBER and set its value to a number greater than 1 (e.g., 3 to create three threads).
3. Restart the Getint service for changes to take effect:

   ```
   ./manager.sh restart 
   ```

#### Verifying Multi-Threading Setup

After restarting, go to **Reporting → Sync Jobs** in the Getint UI. The configured number of integration threads should be visible. For example, if SYNC\_THREADS\_NUMBER=3, the UI should display **Thread #0, Thread #1, and Thread #2**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FTENrLBQWpIweJfSDgfVu%2FChecking%20multi-threading%20for%20Onpremise.png?alt=media&#x26;token=f11264b8-166e-4847-b593-c36faec73f78" alt=""><figcaption></figcaption></figure>

#### Assigning Integrations to Threads

By default, all integrations run on **Thread #0**. To distribute integrations across multiple threads:

1. Open the integration details page.
2. Navigate to **Settings**.
3. Specify the **Thread ID** to execute that integration.

For example, if **3 threads** were created, valid Thread IDs are: 0, 1, 2.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F6GQMbbRhI5x2tZZIolV7%2FAssigning%20threads%20to%20Integrations.png?alt=media&#x26;token=d66d481a-9ac8-41f6-bb80-47adc4d3c7c1" alt=""><figcaption></figcaption></figure>

#### Managing Thread Reductions

If the number of threads is reduced in the future, integrations assigned to non-existing threads must be manually reassigned. For example:

* If **Thread #4** was previously assigned to an integration but the number of threads is reduced to **3**, then **Thread #4 no longer exists**.
* In such cases, update the integration’s settings to use a valid Thread ID (0, 1, or 2).

#### Conclusion

Setting up multi-threading in your on-premise Getint environment can help improve performance and keep integrations running more efficiently. By adjusting a few settings and defining the number of threads, you can allow multiple jobs to run in parallel and support each tenant's setup.

Just remember to keep an eye on thread assignments if you ever decide to change the number of threads. If integrations are still linked to old thread IDs that no longer exist, they’ll need to be updated to make sure everything keeps running smoothly.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Preparing for the Integration

### **Setting Up Service Accounts**

Before initiating an integration with Getint, one critical step is to prepare and set up Service Accounts in the systems you plan to integrate. Service Accounts act as the bridge through which Getint accesses and synchronizes data between different platforms. Here’s a guide on how to effectively prepare these accounts:

#### Choose the Right Account Type

* Opt for dedicated Service Accounts rather than personal user accounts. Service Accounts are designed to facilitate automated processes and integrations, ensuring uninterrupted service and more controlled access.
* Comments are added as the user you chose to create the connection. Therefore, we recommend using a dedicated Service Account for this purpose. While there is no technical possibility of adding comments as the original authors, you can still map the assignees. However, issues, incidents, and tasks will be created, and comments will be attributed to the user who established the connection.

{% hint style="info" %}
Example of a comment that was synced with Getint: **`[Author: Radek, Created on: 2024-08-12T12:53:21.711+0000] [Origin: DEMO-346, Comment ID: 26888].`**

Although comments are still attributed to the integration account, the footer includes additional details such as the original author, creation date, the task that triggered the comment, and the comment ID. It’s an industry standard to add comments as one, the default user, but Getint adds the information about the original commenter and the original date of the comment in the footer, which is not an industry standard.
{% endhint %}

### How to Create a Jira Service Account <a href="#how-to-create-a-jira-service-account" id="how-to-create-a-jira-service-account"></a>

Atlassian now provides native Service Accounts that are ideal for integrations like Getint. These accounts do not consume a standard user license and are purpose-built for API interactions.

#### Why use a Service Account? <a href="#why-use-a-service-account" id="why-use-a-service-account"></a>

* **Security**: Avoid sharing personal login credentials.
* **Continuity**: Integrations won't break when individual passwords change or when users are deactivated.
* **Audit Trails**: Easily distinguish between actions performed by company users and those performed by Getint.
* **Permission Control**: Only grant the specific access required for the integration.

#### Creating a Service Account

To begin, you need to define the account within your Atlassian Organization.

1. Log in to **admin.atlassian.com**.
2. Select your **Organization** from the list.
3. Navigate to **Directory** > **Service accounts**.
4. Click **Create service account**.
5. Enter a **Name** (for example, `Getint-Sync-Bot`) and an optional **Description**.
6. Select the **user** role for the service account in Jira.
7. Click **Create**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FAmNLl2yF4CsedMe7NFGq%2FUser%20role%20for%20service%20account.png?alt=media&#x26;token=adb708e3-6082-445c-ba91-1da6e7a84ca8" alt=""><figcaption></figcaption></figure>

#### Generate Authentication Credentials

Service accounts cannot log in via a browser UI. You must use an **API Token** with classic or granular scopes.

{% hint style="warning" %}
**OAuth 2.0** isn't supported yet.
{% endhint %}

**Creating an API Token**

1. Go to **Directory** > **Service accounts** and select your account.
2. Click **More actions** (•••) > **Create credentials**.
3. Select **API token** and click **Next**.
4. **Name your token**: Use something descriptive like `Production-Sync-Token`.
5. **Set Scopes**: To know the necessary permissions to connect with Getint, please click [here](https://docs.getint.io/guides/quickstart/connection#forge-apps-onpremise-scoped-tokens).
6. **Set Expiration**: Choose a duration (1–365 days) that aligns with your security policy.
7. **Copy & Save**: Copy the token immediately. You will not be able to see it again.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FTt9HVz6RnfoVitvH1F76%2FAPI%20token%20for%20the%20service%20account.png?alt=media&#x26;token=1984213d-9ed2-4d78-8baa-a35f708b323e" alt=""><figcaption></figcaption></figure>

Your service account is now ready for use with Getint.

#### Document and Maintain

* Keep a record of the Service Accounts you've created for integration purposes. Document their purpose, associated systems, and any relevant details.
* Regularly review and maintain these accounts. Update credentials periodically and ensure they’re in line with your organization's security policies.

#### Test the Accounts

* Before finalizing the integration setup, test the Service Accounts to ensure they have the appropriate level of access and can perform all intended functions successfully.

If you're setting up a service account to synchronize Jira with tools like Azure DevOps, ServiceNow, Asana, and so on, check out our [Integration Guides](https://docs.getint.io/guides/integration-synchronization) or reach out to our [Getint support team](https://getint.io/help-center).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# One-to-One, One-to-Many, and Many-to-Many integration

Getint's integration configurations, ranging from one-to-one to many-to-many, are designed to cater to a wide array of synchronization needs.

### One-to-One Integration

* Involves connecting one instance of a tool (like Jira) with one instance of another tool (like Azure DevOps).
* Pricing: This is covered under a single license of Getint, which includes one instance to one instance integration.
* Ideal for direct, straightforward synchronization between two systems.

### One-to-Many Integration

* This setup connects a single instance of a tool with multiple instances of different tools.
* Pricing: Each additional connection (beyond the first instance-to-instance link) requires an additional Getint license.
* Suitable for scenarios where a central system (like Jira) integrates with various platforms (e.g., Azure DevOps, Asana, GitLab).

### Many-to-Many Integration

* Involves multiple independent integrations between various tools or different instances of the same tool.
* Pricing: Each pair of instances (e.g., one ServiceNow instance to one Jira instance) in a many-to-many setup requires its own Getint license.
* Perfect for complex organizational structures needing interconnected systems across various departments or teams.

### Pricing Model and Licenses

* Getint’s pricing model is straightforward: each license covers one instance-to-instance connection.
* For more intricate setups like one-to-many or many-to-many integrations, each additional connection necessitates an extra license.
* This model ensures that organizations only pay for what they need, allowing for scalability and flexibility in their integration solutions.<br>

By understanding these configurations and the associated pricing model, organizations can plan their integrations with Getint effectively, ensuring they choose the most cost-effective and suitable setup for their specific needs. Whether it's simple direct integrations or complex networks of systems, Getint provides a tailored solution for seamless data synchronization.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Simplifying Workflow Sync with Getint: Jira

Integrating project management workflows, particularly in environments involving Jira among other systems, requires careful consideration of status and transition mappings to maintain consistency across platforms. The process of aligning these elements can become complex, underscoring the need for a well-considered strategy. Such mappings often employ a one-to-one approach, where statuses like "To Do" and "In Progress" are directly correlated across systems, ensuring a streamlined workflow. Nevertheless, certain integration scenarios demand a more flexible one-to-many mapping strategy, where a single status in the source system corresponds to multiple statuses in the target system, adapting to the varied requirements of different workflows.

### Status Mapping with Getint

Within Getint, status mappings are designed to be versatile, supporting both one-to-one and one-to-many approaches for integrating Jira with various systems. This adaptability ensures that whether you're aligning Jira instances or integrating Jira with other project management tools, the process remains seamless. Getint provides visual representations of these mappings, delivering a clear and concise overview of your integrated workflows, thus making it a universal solution for managing complex workflow integrations involving Jira.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fe1IpPr3nyOV3Ik2uZSXf%2Fimage-20240105-082023.png?alt=media&#x26;token=b8a7a997-dd16-4cf6-8bea-1e062d53d35e" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Note: Getint makes it easy to map statuses for both one-to-one and one-to-many scenarios. However, if your integration requirements are more complex and involve detailed transition setups, additional customization may be necessary. Our extensive documentation and dedicated [support](mailto:support@getint.io) team are available to assist you in optimizing your workflow transitions.
{% endhint %}

The correct synchronization of a real workflow with restrictions can feel like a puzzle. We want transitions to flow freely, but even with the right transitions, weird warnings might pop up in the logs.

### Understanding the Integration Challenge of Synchronizing Transitions Between Restricted Workflows

While status mappings define the overall relationship, the true challenge lies in synchronizing transitions between restricted workflows. From a technical perspective, transitions cannot always be perfectly mirrored due to inherent limitations in how workflows are configured in Jira. Each status change is governed by strict validation rules to ensure the workflow path is followed correctly. During synchronization, disparities in transition rules between systems can lead to errors that hinder the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fwaznoj4Wt5l7jKQbFBil%2FScreen%2BShot%2B2020-04-14%2Bat%2B11.22.04%2BAM.png?alt=media&#x26;token=0b09fb7a-b6c5-4c09-b356-9a7894170c13" alt=""><figcaption><p>Image from Atlassian Support</p></figcaption></figure>

### Addressing Workflow Restrictions in Status Transitions

While status mappings define the primary relationships, synchronizing transitions within restricted workflows can present challenges. Jira workflows often enforce strict transition rules and validation processes, meaning transitions cannot always be perfectly mirrored across systems. Discrepancies in transition rules may lead to errors during synchronization, which can impact integration stability.

{% hint style="danger" %}
If your Jira workflow restricts necessary transitions, you may encounter an error like this: `[WARN ] 2024-10-25T06:16:32.401Z - [a673999b6-30-177094-1] Change to status [name='Test'] was not possible. It looks like the workflow does not contain the required transition to that status.`

If this occurs, please review and adjust your Jira transition settings or contact our support team for further assistance.
{% endhint %}

#### **Strategies for Effective Workflow Integration:**

1. **Mirror Workflow Structure:** Replicating the original workflow structure, including identical status names and paths, ensures workflow consistency across integrations involving Jira, whether it's Jira to Jira, Jira to ServiceNow, or other project management tools. This replication minimizes the likelihood of errors due to discrepancies in workflow configuration, ensuring smooth and reliable synchronization across all platforms.
2. **Master Account Permissions:** Initiate synchronization from an account with Master Admin privileges. This approach ensures the synchronization process has the necessary permissions to adjust workflows appropriately.
3. **Enable All-to-All Transitions:** Provide the flexibility to change the workflow as needed by adopting a workflow model that allows transitions from one state to another.

### Enhancing Workflow Flexibility with User-Specific Permissions <a href="#enhancing-workflow-flexibility-with-user-specific-permissions" id="enhancing-workflow-flexibility-with-user-specific-permissions"></a>

An important flexibility aspect comes into play when managing user permissions within a workflow. It's feasible to design a workflow that appears less restricted for certain users while maintaining restrictions for others. This approach caters to the need for both synchronization flexibility and control.

**Steps to Customize Workflows with User-Specific Permissions:**

1. **Access Workflow Management in Jira:**
   * Select the gear icon next to your profile picture on the top right corner of the screen.
   * Select "Issues" to configure the workflows.
   * Go to Workflows, then modify or make a copy of your workflow that you would like to change.
2. **Add New Status and Transition:**
   * Add a new status and create a transition that allows moving from any status. You can name it “Rest user transition” and connect it to the restricted status.
   * Save the changes.
3. **Configure Conditions:**
   * Select “Conditions” and add a condition such as “User is in Any Group.”
   * Add the groups that are allowed to change these statuses.
4. **Publish and Test:**
   * Publish the draft and test the workflow to ensure the new permissions work as expected.

{% embed url="<https://www.youtube.com/watch?v=bfCghlkLwls>" %}

### Assessing Project Needs and Customizing Workflows

1. **Review Project Requirements:**
   * Identify key stages and transitions needed for the task or issue lifecycle.
2. **Create or Edit Workflows:**
   * Add a new workflow or edit an existing one to customize statuses and transitions.
3. **Define Statuses and Transition Rules:**
   * Configure statuses like "To Do," "In Progress," and "Completed," and specify transitions for each status.
4. **Implement Transition Screens:**
   * Attach screens to transitions to gather necessary information during status changes.
5. **Testing and Feedback:**
   * Test the new workflow extensively and collect feedback to refine the setup.
6. **Make Transitions Exclusive:**
   * Tailor-specific transitions to be accessible only by certain users or groups.

### Conclusion <a href="#conclusion" id="conclusion"></a>

Integrating Jira workflows with Getint improves operations and strengthens collaboration. By applying status mappings, adjusting workflows to user permissions, and following a systematic approach of planning, testing, and refinement, teams can align project practices with their needs. These strategies help organizations overcome workflow synchronization challenges, leading to better outcomes and a more adaptive project environment.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Understanding the Difference Between Platforms you Integrate

Integrating different tools using Getint involves navigating various technical nuances. Understanding these subtleties ensures effective data synchronization and functionality across systems.

### Field Naming Variations

* Different tools often use different terminologies for similar fields. It’s crucial to identify these variations and establish a mapping (e.g., Jira's "Summary" to Azure DevOps, "Description").

### Tool-Specific Fields and Custom Field Creation

* Some fields are unique to specific tools (e.g., "Assignment Group" in ServiceNow, "Area Path" in Azure DevOps).
* Technical Note: To integrate these unique fields, you may need to create corresponding custom fields in the other system to store this data. This ensures that all relevant information is captured and synced accurately.

### Inline Image Support Inconsistencies

* Different tools have varying capabilities for embedding images within items. This should be considered when setting up integrations to ensure compatibility.

### Out-of-the-Box vs. Custom Fields

* Tools like Jira offer numerous pre-defined fields, while others, like Monday.com, may start with fewer and require customizations for additional fields.

### Mandatory Fields Variance

* The presence and enforcement of mandatory fields differ across systems, affecting how data is entered and synchronized.

### Item Type Diversity

* The range of item types varies significantly among tools, influencing how data is categorized and managed during integration.

### Hierarchy and Structure Complexity

* The level of hierarchical complexity in tools can vary, impacting how sub-items are managed and synchronized.

### API Documentation and Usability

* The quality and detail of API documentation can greatly affect the ease of the integration setup and customization.

### Read-Only Field Integration

* Some fields in certain tools are read-only and can be integrated in only one direction.
* Technical Note: To enable bi-directional integration for such fields, a corresponding writable custom field may need to be created in the other system. This allows for two-way data flow while respecting the read-only nature of the original field.

### Custom Field Support

* The extent and flexibility of custom field support can vary, affecting how specific data points are handled during integration.

### Integration Limitations and Custom Solutions

* Each tool has its unique limitations regarding integration. Identifying these early can help in determining the need for workarounds or custom development.

### Workflow Mechanisms and Compatibility

* The complexity and nature of workflow configurations differ across tools, which should be considered for maintaining process integrity during integration.

In summary, technical preparation and a deep understanding of each tool’s capabilities and limitations are key to a successful integration process with Getint. Custom field creation, proper mapping, and accommodating read-only fields are just some of the technical strategies that can be employed to ensure seamless integration across diverse systems.

### Integration of Collaboration Tools: Detailed Technical Perspective

Integrating various collaboration tools using Getint requires a deep understanding of each platform's unique features and limitations. Here's an expert-level breakdown focusing on common collaboration tools and their differences:

#### Jira and Azure DevOps

* Jira's "Epic Link" correlates to Azure DevOps' "Parent Work Item."
* 'Sprint' in Jira aligns with 'Iteration Path' in Azure DevOps.

#### ServiceNow and Salesforce

* ServiceNow's "Assignment Group" can be mapped to a custom field in Salesforce, as Salesforce doesn't have a direct equivalent.
* "Incident State" in ServiceNow differs from "Case Status" in Salesforce in terms of the lifecycle of a ticket.

#### Asana and ClickUp

* Asana's "Sections" are similar to ClickUp's "Lists" within projects.
* 'Tags' in Asana can be equated to 'Labels' in ClickUp for categorization.

#### Monday.com and GitLab

* Monday.com's "Pulse" is conceptually similar to GitLab's "Issue."
* Custom status columns in Monday.com need to be mapped to GitLab's "Issue Status."

#### GitHub and Wrike

* GitHub's "Issues" can be mapped to "Tasks" in Wrike.
* "Milestones" in GitHub have a different implementation compared to Wrike's "Folders/Projects."

#### HubSpot and Trello

* HubSpot's "Deals" can be somewhat paralleled to Trello's "Cards" in a sales pipeline board.
* "Contact" in Hubspot versus "Member" in Trello reflects the CRM versus project management focus.

#### Zendesk and Jira Service Management

* "Ticket" in Zendesk corresponds to "Issue" in Jira Service Management.
* Zendesk's "Views" for ticket organization are different from Jira Service Management's "Queues."

#### Read-Only and Custom Fields

* Tools like Jira and Azure DevOps allow extensive custom fields, which might need to be created in other systems like Monday.com or Trello for a complete sync.
* For read-only fields in systems like Salesforce (e.g., "Created Date"), corresponding writable fields may be necessary in the integrated tool to facilitate bi-directional data flow.

In each case, understanding the specific functionalities and limitations of these tools is crucial. This knowledge informs the creation of custom fields and the mapping process to ensure accurate data synchronization. It's also important to consider the hierarchical structures, workflow mechanisms, and API capabilities of each tool for a successful integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Connectors

# Airtable

## Getint: Simplifying Airtable Integration and Data Synchronization <a href="#getint-simplifying-airtable-integration-and-data-synchronization" id="getint-simplifying-airtable-integration-and-data-synchronization"></a>

Getint facilitates seamless integration between multiple platforms, enabling synchronization across tools like Airtable, Jira, Asana, and Azure DevOps. It supports both SaaS and On-Premise deployment, offering adaptability to suit diverse business requirements.

### Key Topics Covered: <a href="#key-topics-covered" id="key-topics-covered"></a>

* [Installing and Configuring the Application](#installing-and-configuring-getint-for-airtable)
* [Supported Airtable Fields](#supported-airtable-fields)
* [Key Considerations](#key-considerations)
* [Contacting Support - Case Studies](#contacting-our-support-team)

By synchronizing data across instances and platforms, Getint empowers users to efficiently track and manage tasks while integrating Airtable with other project management tools.

### Installing and Configuring Getint for Airtable <a href="#installing-and-configuring-getint-for-airtable" id="installing-and-configuring-getint-for-airtable"></a>

Getint simplifies connecting and migrating data between systems. Below are the steps to get started:

**Step 1: Access Getint**

* **Want to integrate Jira with Airtable?** Just download the app from the Atlassian Marketplace. It’s quick and easy! You can find it here: [Airtable Integration for Jira.](https://marketplace.atlassian.com/apps/1231789/airtable-integration-for-jira-airtable-connector?hosting=cloud\&tab=overview)
* Other tools: Select between [Getint On-Premise or SaaS options.](https://app.getint.io/app/auth/sign-up)

**Step 2: Set Up a Connection with Airtable**

* Ensure you have the correct access permissions. Here you will find all the steps to generate an access token in Airtable: [Generating an Airtable Token.](https://docs.getint.io/guides/quickstart/connection#airtable)
* Choose Airtable as the app, create a new connection, and enter your Airtable access token.

**Step 3: Connect to Another Tool**

* Choose the platform you want to integrate with Airtable, such as Jira.

**Step 4: Map Types and Fields**

* Match Airtable issue types, such as Tasks, with their equivalents in the other tool.
* Leverage the Quick Build feature for automatic mapping, or adjust mappings manually to fit your needs.

If you need help with setup or run into any challenges, our support team is always here to assist.

For additional guidance on using Getint with Airtable, refer to:

* [Quickstart Guides](https://docs.getint.io/guides/quickstart)
* [Jira Airtable Integration Guide](https://docs.getint.io/guides/integration-synchronization/jira-airtable-integration)
* [Migration Guides](https://docs.getint.io/guides/migration)

### Supported Airtable Fields <a href="#supported-airtable-fields" id="supported-airtable-fields"></a>

Getint allows you to map fields between different platforms, and here's a list of our currently supported:

{% hint style="info" %}

#### **How Field Mappings Work:** <a href="#how-field-mappings-work" id="how-field-mappings-work"></a>

**One-Way Mapping:**

* When you update fields in one of the synced apps, those changes will appear in the other app. However, updates made in the other app won’t affect the first app because the fields are read-only.

**Two-Way Mapping:**

* Updates to synced fields will be reflected in both apps. If you modify a field in one app, the change will automatically sync to the other app as well.

**Tip:**

While technically it's not possible to directly modify read-only fields, we offer a solution to achieve bidirectional integration or migrate these fields using custom fields. Setting up this solution requires specific steps, but it is indeed possible. You can find more detailed information in this [article.](https://docs.getint.io/getting-started-with-the-platform/prepare-for-integration/understanding-the-difference-between-platforms-you-integrate)
{% endhint %}

| **Airtable Field**                                                                                         | **One Way**                                                                                                                                                                          | **Both Ways**                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Attachments                                                                                                | <img src="https://pf-emoji-service--cdn.us-east-1.prod.public.atl-paas.net/standard/ef8b0642-7523-4e13-9fd3-01b65648acf6/64x64/2716.png" alt="multiplication sign" data-size="line"> | <img src="https://pf-emoji-service--cdn.us-east-1.prod.public.atl-paas.net/standard/ef8b0642-7523-4e13-9fd3-01b65648acf6/64x64/2716.png" alt="multiplication sign" data-size="line"> |
| Comments                                                                                                   | ✔️                                                                                                                                                                                   | ✔️                                                                                                                                                                                   |
| <p>Custom Fields</p><p><strong>Long Text - Rich Text Field -Single Line Text - Single Select</strong> </p> | ✔️                                                                                                                                                                                   | ✔️                                                                                                                                                                                   |
| ID                                                                                                         | ✔️                                                                                                                                                                                   |                                                                                                                                                                                      |
| Item Type                                                                                                  | ✔️                                                                                                                                                                                   |                                                                                                                                                                                      |
| Last modified time                                                                                         | ✔️                                                                                                                                                                                   | ✔️                                                                                                                                                                                   |
| Name                                                                                                       | ✔️                                                                                                                                                                                   | ✔️                                                                                                                                                                                   |
| Notes                                                                                                      | ✔️                                                                                                                                                                                   | ✔️                                                                                                                                                                                   |
| Record API URL                                                                                             | ✔️                                                                                                                                                                                   |                                                                                                                                                                                      |
| Status                                                                                                     | ✔️                                                                                                                                                                                   | ✔️                                                                                                                                                                                   |
| URL                                                                                                        | ✔️                                                                                                                                                                                   |                                                                                                                                                                                      |

{% hint style="danger" %}
**Important Note:** While we make every effort to ensure the accuracy of this list, please be aware that supported fields may differ in the original product.
{% endhint %}

### Key Considerations <a href="#key-considerations" id="key-considerations"></a>

At Getint, we are committed to continuously updating our supported features, fields, and compatible apps. However, please keep the following key points in mind:

* **Attachments** aren't supported.
* **Change History**: Getint cannot integrate the history of changes.
* **Comments**: Comments added by Getint will appear under the user account you choose during connection setup. Consider creating a dedicated Service Account for integration to maintain consistency. The original author’s name will appear in the comment footer, but the comment will be assigned to the connecting account. Also, comments and attachments transferred from Airtable to Jira will be set to public or private (they will be public by default). You can configure Jira to mark all comments from Airtable as private automatically. However, enabling both public and private visibility options is impossible.
* **Rich text** formatting is supported for text fields.

### Contacting Our Support Team <a href="#contacting-our-support-team" id="contacting-our-support-team"></a>

Our dedicated Support Team is here to assist with your integration and migration needs. Whether you have questions or seek deeper insights into our solution, you’re welcome to schedule a [demo call](https://www.getint.io/schedule-demo-call) with us.

#### Case Studies <a href="#case-studies" id="case-studies"></a>

Discover how Getint enhances tool integration for businesses of all sizes. Our [Case Studies](https://www.getint.io/case-studies) highlight real-world solutions designed to empower teams and organizations.

{% hint style="info" %}
**Looking for a solution we don’t currently support?** Reach out to our [support team](https://getint.io/help-center); we’d be happy to help you explore a customized solution tailored to your needs.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>

# Asana

## Getint: Simplifying Asana Integration and Data Synchronization <a href="#getint-simplifying-asana-integration-and-data-synchronization" id="getint-simplifying-asana-integration-and-data-synchronization"></a>

Getint is expertly designed to integrate and synchronize an extensive range of tools. It accommodates a variety of connectivity scenarios, such as Asana - Jira, Asana - Asana, Asana - Monday, Asana - Azure DevOps, and more. With its availability as both a Software-as-a-Service (SaaS) and On-Premise solution, Getint offers the versatility to meet the unique requirements of various businesses.

### Key Topics Covered: <a href="#key-topics-covered" id="key-topics-covered"></a>

* [How to Set Up the App](#what-does-this-article-cover)
* [Supported Fields in Asana](#setting-up-getint-for-asana)
* [Limitations and Considerations to Make](#limitations-to-be-considered)
* [Contacting Our Support Team - Case Studies](#contacting-our-support-team)

Getint enables seamless data synchronization within the same platform, different platforms/different instances. It supports Asana across different projects. This allows users to efficiently track and manage Asana tasks and subtasks in diverse environments as well as integrate Asana with other platforms.

### Setting Up Getint for Asana <a href="#setting-up-getint-for-asana" id="setting-up-getint-for-asana"></a>

Getint simplifies data integration and migration. With easy setup steps, you can connect your systems, such as Asana, map types (i.e. Task - Task), and fields (i.e. Assignee - Assignee). Whether you're looking to sync data continuously or perform a one-time migration, Getint has got you covered. Our dedicated support team is always ready to assist you with any challenges you may encounter during setup or operation.

For more detailed guides on how to set up your Asana integration, please make sure to check the following:

* [Starting with Getint - Quickstart Guides](https://docs.getint.io/guides/quickstart)
* [Integration Guides](https://docs.getint.io/guides/integration-synchronization)
* [Migration Guides](https://docs.getint.io/guides/migration)
* [Understanding Getint - Workflows](https://docs.getint.io/getintio-platform/workflows)

Here's a simplified version of how to integrate Asana with other tools (you can find a detailed overview [**here**](https://docs.getint.io/guides/integration-synchronization/jira-asana-integration)):

1. **Access Getint:**
   * If you’re using Jira, go to "Apps," "Find new apps," and get the app from the Atlassian Marketplace.
   * If you want to integrate Asana with any other, non-Jira application, opt for the [Getint On-Premise or Getint SaaS](https://app.getint.io/).
2. **Token Generation for Asana:** Visit your Asana Settings. Go to the "Apps" section and launch the developer console. Now, click "Create new token" in the developer console under "Personal access token." This will serve as the password to create your connection.
3. **Establish a Connection with Asana:** Ensure you're logged in as a user with the correct permissions. Click "Select App" and choose Asana. Select "Create New" to establish a new connection with your Asana instance. Name your connection, and add the URL of your Asana instance (without "/" at the end). Provide the login credentials.
4. **Choose and Connect the Second App:** Choose and connect another tool you'd like to integrate with Asana—either another Asana instance, DevOps, Jira, or any other tool that we support.
5. **Map Types and Fields:** Link Asana types (Task, Subtasks) to synchronize with other tools. You can use the "Quick Build" feature, which allows you to map available fields automatically, or you can set them manually.

Getint's support team is committed to ensuring a smooth and efficient integration experience customized to your unique needs. If you encounter any challenges during setup or require assistance with missing functionalities, our dedicated support team is readily available to provide guidance and help.

### Supported Fields in Asana <a href="#supported-fields-in-asana" id="supported-fields-in-asana"></a>

Getint allows you to map fields between different platforms, and here's a list of our currently supported:

{% hint style="info" %}

### **How Field Mappings Work:**

**One-Way Mapping:**

* When you update fields in one of the synced apps, those changes will appear in the other app. However, updates made in the other app won’t affect the first app because the fields are read-only.

**Two-Way Mapping:**

* Updates to synced fields will be reflected in both apps. If you modify a field in one app, the change will automatically sync to the other app as well.

**Tip:**

While technically it's not possible to directly modify read-only fields, we offer a solution to achieve bidirectional integration or migrate these fields using custom fields. Setting up this solution requires specific steps, but it is indeed possible. You can find more detailed information in this [article.](https://docs.getint.io/getting-started-with-the-platform/prepare-for-integration/understanding-the-difference-between-platforms-you-integrate)
{% endhint %}

| **Asana Field**                                                                                 | **One Way** | **Both Ways** |
| ----------------------------------------------------------------------------------------------- | ----------- | ------------- |
| Assignee                                                                                        | ✔️          | ✔️            |
| Attachments                                                                                     | ✔️          | ✔️            |
| Created                                                                                         | ✔️          |               |
| Comments                                                                                        | ✔️          | ✔️            |
| Completed                                                                                       | ✔️          | ✔️            |
| <p>Custom fields</p><p><strong>Single-select - Date - Text - Number - Formula - ID</strong></p> | ✔️          | ✔️            |
| Description (Notes)                                                                             | ✔️          | ✔️            |
| Estimated time                                                                                  | ✔️          | ✔️            |
| ID                                                                                              | ✔️          |               |
| Priority                                                                                        | ✔️          | ✔️            |
| Reporter                                                                                        | ✔️          | ✔️            |
| Section                                                                                         | ✔️          | ✔️            |
| Start date                                                                                      | ✔️          | ✔️            |
| Status                                                                                          | ✔️          | ✔️            |
| Subtasks                                                                                        | ✔️          | ✔️            |
| Tags                                                                                            | ✔️          | ✔️            |
| Title (Name)                                                                                    | ✔️          | ✔️            |
| URL                                                                                             | ✔️          |               |

{% hint style="danger" %}
**Important Note:**\
We strive to maintain the accuracy of this list, but please be aware that supported fields may vary in the original product.
{% endhint %}

### Limitations to be Considered

At Getint, we’re constantly updating our supported features, fields, and compatible apps. However, there are a few limitations you should be aware of:

* When a new issue is created in Asana by Getint, it will always be one type of issue, whether that's a Task or a Subtask. You can set the default item type using a rule or manually change it in Asana after it's created.
* Comments will be added as the user you choose to create the connection. Therefore, it is advised to create a dedicated Service Account to build your integration. The original author will appear in the comment footer; however, it will still be assigned to the account that established the connection.
* The history of changes can't be integrated.

### Contacting Our Support Team

Our Support Team at Getint is eager to assist with your integration and migration needs and answer any other questions you may have. If you're seeking assistance or a deeper understanding of our solution, we invite you to schedule a demo call [here](https://www.getint.io/schedule-demo-call).

#### Case Studies

Large and small businesses have experienced the benefits of using Getint for their data integration needs. This has provided them with various solutions tailored to their teams and organizations. We invite you to explore some of our [Case Studies](https://www.getint.io/case-studies), which are true accounts of how Getint continually enhances and improves the tool integration process.

{% hint style="info" %}
**Are you looking for a specific solution that we don’t currently support?** Please get in touch with our [support team](https://getint.io/help-center), and we can assist you in developing a customized solution for your particular case.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>

# Azure DevOps

## Getint: Simplifying Azure DevOps Integration and Data Synchronization <a href="#getint-simplifying-azure-devops-integration-and-data-synchronization" id="getint-simplifying-azure-devops-integration-and-data-synchronization"></a>

Getint is expertly designed to integrate and synchronize an extensive range of tools. It accommodates a variety of connectivity scenarios, such as Azure DevOps - Jira, Azure DevOps - Asana, Azure DevOps - Monday, Azure DevOps - ServiceNow, and more. With its availability as both a Software-as-a-Service (SaaS) and On-Premise solution, Getint offers the versatility to meet the unique requirements of various businesses.

### What Does this Article Cover? <a href="#what-does-this-article-cover" id="what-does-this-article-cover"></a>

* [How to Set Up the App](#setting-up-getint-for-azure-devops)
* [Supported Fields in Azure DevOps](#supported-fields-in-azure-devops)
* [Limitations and Considerations to Make](#limitations-to-be-considered)
* [Contacting our Support Team - Case Studies](#contacting-our-support-team)

**Getint** facilitates smooth data synchronization across various platforms and instances. It specifically supports **Azure,** allowing users to monitor and manage tasks in diverse environments effectively. Additionally, it enables seamless integration with other platforms.

### Setting Up Getint for Azure DevOps <a href="#setting-up-getint-for-azure-devops" id="setting-up-getint-for-azure-devops"></a>

Getint simplifies data integration and migration. With easy setup steps, you can connect your systems, such as Azure DevOps, map types (i.e. Epic - Epic), and fields (i.e. Assignee - Assigned to). Whether you're looking to sync data continuously or perform a one-time migration, Getint has got you covered. Our dedicated support team is always ready to assist you with any challenges you may encounter during setup or operation.

For more detailed guides on how to set up your Azure integration, please make sure to check the following:

* [Starting with Getint - Quickstart Guides](https://docs.getint.io/guides/quickstart)
* [Integration Guides](https://docs.getint.io/guides/integration-synchronization)
* [Migration Guides](https://docs.getint.io/guides/migration)
* [Understanding Getint - Workflows](https://docs.getint.io/getintio-platform/workflows)

Here's a simplified version of how to integrate Azure with other tools (you can find a detailed overview [**here**](https://docs.getint.io/guides/integration-synchronization/jira-azure-devops-integration)):

1. **Access Getint:** If you’re using Jira, navigate to the "Apps" section, search for new apps, and acquire the app from the [Atlassian Marketplace](https://marketplace.atlassian.com/apps/1223931/azure-devops-integration-for-jira-azure-devops-connector?hosting=cloud\&tab=overview). Alternatively, if you need to integrate Azure DevOps with a non-Jira application, consider choosing either [Getint On-Premise or Getint SaaS](https://www.getint.io/contact).
2. **Token Generation for Azure DevOps:** Click on your user profile icon, navigate to the "Personal access tokens" section, and click "New token." Provide a name for the token, select the relevant organization, set an expiration, and choose "Full Access" in the scopes. This token will serve as your password to connect with Getint.
3. **Establish a Connection with Azure DevOps:** Ensure you're logged in as a user with the correct permissions. Click "Select App" and choose "Azure DevOps." Select "Create New" to establish a new connection with your Azure DevOps instance. Name your connection, and add the URL of your Azure instance. Provide the login credentials.
4. **Choose and Connect the Second App:** You can select and link an additional tool to integrate with Azure DevOps. Options include another Azure instance, ServiceNow, Jira, or any other supported tool.
5. **Map Types and Fields:** Link "Azure types" (Epics, Tasks, Issues) to synchronize with other tools. You can use the "Quick Build" feature, which allows you to map available fields automatically, or you can set them manually.

Getint's support team is committed to ensuring a smooth and efficient integration experience customized to your unique needs. If you encounter any challenges during setup or require assistance with missing functionalities, our dedicated support team can provide guidance and assistance.

### Supported Fields in Azure DevOps <a href="#supported-fields-in-azure-devops" id="supported-fields-in-azure-devops"></a>

Getint allows you to map fields between different platforms, and here's a list of our currently supported:

{% hint style="info" %}

#### **How Field Mappings Work:** <a href="#how-field-mappings-work" id="how-field-mappings-work"></a>

**One-Way Mapping:**

* When you update fields in one of the synced apps, those changes will appear in the other app. However, updates made in the other app won’t affect the first app because the fields are read-only.

**Two-Way Mapping:**

* Updates to synced fields will be reflected in both apps. If you modify a field in one app, the change will automatically sync to the other app as well.

**Tip:**

While technically it's not possible to directly modify read-only fields, we offer a solution to achieve bidirectional integration or migrate these fields using custom fields. Setting up this solution requires specific steps, but it is indeed possible. You can find more detailed information in this [article.](https://docs.getint.io/getting-started-with-the-platform/prepare-for-integration/understanding-the-difference-between-platforms-you-integrate)
{% endhint %}

| **Azure DevOps Field**                                                                                                                       | **One Way** | **Both Ways** |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------- |
| Activated By                                                                                                                                 | ✔️          | ✔️            |
| Activated Date                                                                                                                               | ✔️          | ✔️            |
| Activity                                                                                                                                     | ✔️          | ✔️            |
| Area ID                                                                                                                                      | ✔️          | ✔️            |
| Area Path                                                                                                                                    | ✔️          | ✔️            |
| Assigned To (Assignees)                                                                                                                      | ✔️          | ✔️            |
| Changed By                                                                                                                                   | ✔️          | ✔️            |
| Closed By                                                                                                                                    | ✔️          | ✔️            |
| Closed Date                                                                                                                                  | ✔️          | ✔️            |
| Created By                                                                                                                                   | ✔️          | ✔️            |
| Completed Work                                                                                                                               | ✔️          | ✔️            |
| <p>Custom fields</p><p><strong>Date - Decimal - Identity - Integer - Picklist - Picklist integer - Text (Single/Multiple lines)</strong></p> | ✔️          | ✔️            |
| Description (System.Description)                                                                                                             | ✔️          | ✔️            |
| ID                                                                                                                                           | ✔️          |               |
| Iteration ID                                                                                                                                 | ✔️          | ✔️            |
| Iteration Path                                                                                                                               | ✔️          | ✔️            |
| Priority                                                                                                                                     | ✔️          | ✔️            |
| Reason                                                                                                                                       | ✔️          | ✔️            |
| Remaining Work                                                                                                                               | ✔️          | ✔️            |
| Resolved By                                                                                                                                  | ✔️          | ✔️            |
| Resolved Date                                                                                                                                | ✔️          | ✔️            |
| Stack Rank                                                                                                                                   | ✔️          | ✔️            |
| State                                                                                                                                        | ✔️          | ✔️            |
| State Change Date                                                                                                                            | ✔️          | ✔️            |
| Status                                                                                                                                       | ✔️          | ✔️            |
| Story Points                                                                                                                                 | ✔️          | ✔️            |
| Tags                                                                                                                                         | ✔️          | ✔️            |
| Target Date                                                                                                                                  | ✔️          | ✔️            |
| Team Project                                                                                                                                 | ✔️          | ✔️            |
| Title                                                                                                                                        | ✔️          | ✔️            |
| URL                                                                                                                                          | ✔️          |               |
| Work Item Type                                                                                                                               | ✔️          | ✔️            |

{% hint style="danger" %}
**Important Note:**\
We strive to maintain the accuracy of this list, but please be aware that supported fields may vary in the original product.
{% endhint %}

### Supported Item Types for Azure DevOps Integration

| Code Review Request | Code Review Response |
| ------------------- | -------------------- |
| Epic                | Feedback Request     |
| Issue               | Feedback Response    |
| Shared Parameter    | Task                 |

### Limitations to be Considered

At Getint, we continuously update our supported features, fields, and compatible apps. However, there are a few important limitations to keep in mind:

* When Getint creates a new issue in Azure DevOps, it will always be one specific type of issue: an Epic, an Issue, a Test Plan, or a Task (to name a few). You can set the default item type with Getint or manually change it in Azure after it's created.
* Comments added to the issue will appear under the user account you choose to create the connection. To ensure seamless integration, creating a dedicated Service Account is recommended to build your integration. Although the original author’s name will appear in the comment footer, the comment will still be associated with the account that established the connection.
* Unfortunately, integrating the history of changes is not possible.

### Contacting Our Support Team

Our Support Team at Getint is eager to assist with your integration and migration needs and answer any other questions you may have. If you're seeking assistance or a deeper understanding of our solution, we invite you to schedule a demo call [here](https://www.getint.io/schedule-demo-call).

#### Case Studies

Large and small businesses have experienced the benefits of using Getint for their data integration needs. This has provided them with various solutions tailored to their teams and organizations. We invite you to explore some of our [Case Studies](https://www.getint.io/case-studies), which are true accounts of how Getint continually enhances and improves the tool integration process.

{% hint style="info" %}
**Are you looking for a specific solution that we don’t currently support?** Please get in touch with our [support team](https://getint.io/help-center), and we can assist you in developing a customized solution for your particular case.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>

# ClickUp

## Getint: Simplifying ClickUp Integration and Data Synchronization

Getint connects and synchronizes multiple tools, enabling seamless integrations between platforms such as ClickUp, Jira, Asana, and Azure DevOps. Available as both a Cloud and an on-premise solution, Getint offers the flexibility to meet diverse business requirements.

### Key Topics Covered

* [Setting Up the App](#how-to-set-up-getint-for-clickup)
* [Supported Fields in ClickUp](#supported-fields-for-clickup-integration)
* [Limitations and Considerations](#limitations-and-considerations)
* [Contacting Support](#contacting-our-support-team)

Getint synchronizes data across platforms or instances, including ClickUp, allowing users to monitor and manage tasks and activities across projects while integrating ClickUp with other tools.

### How to Set Up Getint for ClickUp

Getint makes it easy to connect systems and synchronize or migrate data between them. Follow the steps below to get started with ClickUp.

**Step 1: Access Getint**

* **For Jira users**: If you plan to integrate Jira with ClickUp, download the Getint app from the [Atlassian Marketplace](https://marketplace.atlassian.com/apps/1231636/clickup-integration-for-jira-2-way-clickup-connector?hosting=cloud\&tab=overview).
* **For other tools**: Choose between Getint's **SaaS** or **On-Premise** deployment options, depending on your requirements.

**Step 2: Set Up a Connection with ClickUp**

* Ensure you have the necessary [access permissions](https://docs.getint.io/guides/quickstart/connection#clickup) in ClickUp.
* Select **ClickUp** as the application.
* Create a new connection and enter your ClickUp credentials.

**Step 3: Connect to Another Tool**

* Choose the platform you want to integrate with ClickUp, such as **Jira**, **Asana**, or **Azure DevOps**.

**Step 4: Map Types and Fields**

* Match ClickUp entities (for example, tasks, custom fields, or statuses) with their corresponding entities in the other tool.
* Use the **Quick Build** feature for automatic mapping, or manually customize mappings to fit your workflow.

Our support team is always available to help with setup or operational questions.

For additional guidance on using Getint with ClickUp, refer to:

* [Quickstart Guides](https://docs.getint.io/guides/quickstart)
* [Jira ClickUp Integration Guide](https://docs.getint.io/guides/integration-synchronization/jira-clickup-integration)
* [Migration Guides](https://docs.getint.io/guides/migration)

### Supported Fields for ClickUp Integration

Getint enables field mapping between ClickUp and other platforms. Below is an overview of the currently supported field-mapping options and their functionality.

{% hint style="info" %}

#### **How Field Mappings Work:**

**One-Way Mapping:**

* When you update fields in one of the synced apps, those changes will appear in the other app. However, updates made in the other app won’t affect the first app because the fields are read-only.

**Two-Way Mapping:**

* Updates to synced fields will be reflected in both apps. If you modify a field in one app, the change will automatically sync to the other app as well.

**Tip:**

While technically it's not possible to directly modify read-only fields, we offer a solution to achieve bidirectional integration or migrate these fields using custom fields. Setting up this solution requires specific steps, but it is indeed possible. For more detailed information, please refer to this [article.](https://docs.getint.io/getting-started-with-the-platform/prepare-for-integration/understanding-the-difference-between-platforms-you-integrate)
{% endhint %}

| **ClickUp Field**                                                                      | **One Way** | **Both Ways** |
| -------------------------------------------------------------------------------------- | ----------- | ------------- |
| Assignee                                                                               | ✔️          | ✔️            |
| Comments & Attachments                                                                 | ✔️          | ✔️            |
| <p>Custom Fields</p><p><strong>Dropdown - Labels - Number - People - Text</strong></p> | ✔️          | ✔️            |
| Description                                                                            | ✔️          | ✔️            |
| Id                                                                                     | ✔️          |               |
| Item Type                                                                              | ✔️          |               |
| Status                                                                                 | ✔️          | ✔️            |
| Tags                                                                                   | ✔️          |               |
| Title                                                                                  | ✔️          | ✔️            |
| URL                                                                                    | ✔️          |               |

{% hint style="warning" %}
**Important Note:**\
We strive to maintain the accuracy of this list, but please be aware that supported fields may vary in the original product.
{% endhint %}

### Limitations and Considerations

At Getint, we continuously update our supported features, fields, and compatible apps. However, there are a few important points to consider:

* **Attachments**: Inline images aren’t supported for the Description field.
* **Change History**: Unfortunately, Getint cannot integrate the history of changes.
* **Comments**: Comments added by Getint will appear under the user account you choose during connection setup. Consider creating a dedicated Service Account for integration to maintain consistency. The original author’s name will appear in the comment footer, but the comment will be assigned to the connecting account.
* **Issue Types**: Currently, the integration supports ClickUp tasks as the only issue type.
* **Item Hierarchy**: Sub-items are not currently supported in Jira–ClickUp synchronization.
* **Multi-project Support**: Many-to-many project synchronization between Jira and ClickUp is not supported.
* **Synchronization Scope**: In ClickUp, you can specify a Space and Folder, but not an individual List, which means all lists in a folder are synced.
* **Text Formatting Errors**: Formatting is not fully preserved during synchronization; bullet points may not convert correctly in Jira, and embedded links can be removed.

### Contacting Our Support Team

Our dedicated Support Team is ready to assist with your integration and migration needs. If you have questions or need deeper insights into our solution, feel free to schedule a [demo call](https://www.getint.io/schedule-demo-call) with us.

#### Case Studies

Explore real-world examples of how Getint enhances tool integration for businesses of all sizes. Our [Case Studies](https://www.getint.io/case-studies) showcase tailored solutions that empower teams and organizations.

{% hint style="info" %}
**Are you looking for a specific solution that we don’t currently support?** Please get in touch with our [support team](https://getint.io/help-center), and we can assist you in developing a customized solution for your particular case.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>

# Freshdesk

## Getint: Streamlining Freshdesk Integration and Data Synchronization <a href="#getint-streamlining-freshdesk-integration-and-data-synchronization" id="getint-streamlining-freshdesk-integration-and-data-synchronization"></a>

Getint revolutionizes the integration and synchronization of various tools, including Freshdesk. It supports diverse connectivity scenarios such as Freshdesk-Jira, Freshdesk-Asana, Freshdesk-Monday, Freshdesk-Azure DevOps, and more. Whether you need a SaaS or On-premise solution, Getint offers the flexibility to meet the unique needs of different businesses.

### The Article Covers the Following Topics: <a href="#the-article-covers-the-following-topics" id="the-article-covers-the-following-topics"></a>

* [How to Set Up the App](#setting-up-getint-for-freshdesk)
* [Supported Fields for Freshdesk Integrations](#supported-fields-for-freshdesk-integrations)
* [Limitations and Considerations to Keep in Mind](#limitations-to-keep-in-mind)
* [Case Studies and Contacting Our Support Team](#case-studies-and-support-contact)

Getint ensures seamless data synchronization across platforms and instances, specifically supporting Freshdesk. Users can efficiently monitor and manage tasks in diverse environments while integrating seamlessly with other platforms.

### Setting Up Getint for Freshdesk <a href="#setting-up-getint-for-freshdesk" id="setting-up-getint-for-freshdesk"></a>

Getint simplifies data integration and migration. Follow these straightforward steps to connect your systems, such as Freshdesk, map types (i.e., Task - Incident), and fields (i.e., Description - Description). Whether you’re syncing data or performing a continuous one-time migration, Getint has you covered. Our dedicated support team is ready to assist you with any setup or operational challenges.

For more detailed guides on setting up your Freshdesk integration, refer to the following resources:

* [Starting with Getint - Quickstart Guides](https://docs.getint.io/guides/quickstart)
* [Integration Guides](https://docs.getint.io/guides/integration-synchronization)
* [Migration Guides](https://docs.getint.io/guides/migration)
* [Understanding Getint - Workflows](https://docs.getint.io/getintio-platform/workflows)

#### Simplified Freshdesk Integration Process <a href="#simplified-freshdesk-integration-process" id="simplified-freshdesk-integration-process"></a>

Here's a simplified version of how to integrate Freshdesk with other tools (you can find a detailed overview [**here**](https://docs.getint.io/guides/integration-synchronization/jira-freshdesk)):

1. **Access Getint:** If you’re using Jira, navigate to the **Apps** section, search for new apps, and acquire the app from the [Atlassian Marketplace.](https://marketplace.atlassian.com/apps/1227929/freshdesk-freshservice-jira-works-behind-the-firewall?hosting=cloud\&tab=overview) Alternatively, if you need to integrate Freshdesk with a non-Jira application, consider choosing either [Getint On-Premise or Getint SaaS.](https://www.getint.io/contact)
2. **Token Generation for Freshdesk:** Log in to your Freshdesk account, click on your profile picture in the top right corner, and select **Profile Settings.** In the sidebar on the right, locate the **View API key** button, click on it to access the API key, and complete the captcha verification when prompted. Copy the provided API key and paste it to authenticate your Getint integration.
3. **How to Establish a Connection with Freshdesk:** Ensure you’re logged in as a user with the correct permissions. Click **Select App** and choose **Freshdesk.** Select **Create New** to establish a new connection with your Freshdesk instance. Name your connection and add the **URL** of your Freshdesk instance. Provide your login credentials to connect with Getint.
4. **Choose and Connect the Second App:** Select and link another tool to integrate with Freshdesk—options include another Freshdesk instance, ServiceNow, Jira, or any other supported tool.
5. **Mapping Types and Fields:** Link **Freshdesk types** (Incidents) to synchronize with other tools. You can use the **Quick Build** feature, which allows you to map available fields automatically or set them manually.

Getint’s support team is committed to ensuring a smooth and efficient integration experience tailored to your unique needs. If you encounter any challenges during setup or require assistance with missing functionalities, our dedicated support team is here to help.

### Supported Fields for Freshdesk Integrations <a href="#supported-fields-for-freshdesk-integrations" id="supported-fields-for-freshdesk-integrations"></a>

Getint allows you to map fields between different platforms, and here's a list of our currently supported fields for Freshdesk integrations:

{% hint style="info" %}

#### **How Field Mappings Work:** <a href="#how-field-mappings-work" id="how-field-mappings-work"></a>

**One-Way Mapping:**

* When you update fields in one of the synchronized apps, those changes will appear in the other app. However, updates made in the other app won’t impact the first app because the fields are read-only.

**Two-Way Mapping:**

* Updates to synchronized fields will be reflected in both apps. If you modify a field in one app, the change will automatically sync to the other app as well.

**Tip:** While it’s technically not possible to directly modify read-only fields, we provide a solution for achieving bidirectional integration or migrating these fields using custom fields. Setting up this solution requires specific steps, but it is indeed feasible. You can find more detailed information in this [article.](https://docs.getint.io/getting-started-with-the-platform/prepare-for-integration/understanding-the-difference-between-platforms-you-integrate)
{% endhint %}

| **Freshdesk Field**                                                                              | **One Way** | **Both Ways** |
| ------------------------------------------------------------------------------------------------ | ----------- | ------------- |
| Agent                                                                                            | ✔️          | ✔️            |
| Comments & Attachments                                                                           | ✔️          | ✔️            |
| <p>Custom fields</p><p><strong>Date - Dependent field - Dropdown - Single line text</strong></p> | ✔️          | ✔️            |
| Description                                                                                      | ✔️          | ✔️            |
| Group                                                                                            | ✔️          | ✔️            |
| Id                                                                                               | ✔️          |               |
| Priority                                                                                         | ✔️          | ✔️            |
| Requester                                                                                        | ✔️          | ✔️            |
| Status                                                                                           | ✔️          | ✔️            |
| Source                                                                                           | ✔️          | ✔️            |
| Subject                                                                                          | ✔️          | ✔️            |
| Type                                                                                             | ✔️          | ✔️            |
| URL                                                                                              | ✔️          |               |

{% hint style="warning" %}
**Important Note:**\
We strive to maintain the accuracy of this list, but please be aware that supported fields may vary in the original product.
{% endhint %}

### Limitations to Keep in Mind

At Getint, we continuously update our supported features, fields, and compatible apps. However, there are a few important limitations to keep in mind:

* To ensure your integration functions correctly, you must map the following mandatory fields: Requester, Status (mapped with a fixed value “Open” for newly created tickets), and Priority. For detailed instructions on mapping these fields with platforms like Jira, please refer to the guide available [here.](https://docs.getint.io/guides/integration-synchronization/jira-freshdesk#field-mapping)
* Comments added to the issue will display under the user account you select when creating the connection. For a seamless integration, we recommend creating a dedicated Service Account. Although the original author’s name will appear in the comment footer, the comment will still be linked to the account that established the connection.
* Unfortunately, integrating the history of changes is not possible due to the technical limitations of Jira / Freshdesk APIs.

### Case Studies and Support Contact

Our Support Team at Getint is eager to assist with your integration and migration needs and answer any other questions you may have. If you're seeking assistance or a deeper understanding of our solution, we invite you to schedule a demo call [here](https://www.getint.io/schedule-demo-call).

#### Case Studies

Large and small businesses have experienced the benefits of using Getint for data integration. This has provided them with various solutions tailored to their teams and organizations. We invite you to explore some of our [Case Studies](https://www.getint.io/case-studies), which are true accounts of how Getint continually enhances and improves the tool integration process.

{% hint style="info" %}
**Are you looking for a specific solution that we don’t currently support?** Please get in touch with our [support team](https://getint.io/help-center), and we can assist you in developing a customized solution for your particular case.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>

# Freshservice

## Getint: Connecting Freshservice and Synchronizing Data Across Platforms <a href="#getint-connecting-freshservice-and-synchronizing-data-across-platforms" id="getint-connecting-freshservice-and-synchronizing-data-across-platforms"></a>

Getint makes it easier to connect Freshservice with other tools and keep data aligned. It supports a wide range of setups, including Freshservice-Jira, Freshservice-Asana, Freshservice-Monday, Freshservice-Azure DevOps, and more. Whether you’re using a SaaS or On-Premise version, Getint offers flexible options to support different business needs.

### What’s Inside: <a href="#whats-inside" id="whats-inside"></a>

* [How to Set Up the App](#setting-up-getint-with-freshservice)
* [Supported Fields for Freshservice Connections](#supported-fields-for-freshservice-integrations)
* [Key Limitations and Setup Notes](#things-to-keep-in-mind)
* [Case Studies and How to Reach Support](#case-studies-and-support)

Getint helps teams keep data consistent across platforms and environments. With support for Freshservice, users can track and manage work across systems without losing visibility or control.

### Setting Up Getint with Freshservice <a href="#setting-up-getint-with-freshservice" id="setting-up-getint-with-freshservice"></a>

Connecting Freshservice to other tools through Getint is straightforward. You can sync data or run a one-time migration. The process includes mapping issue types (e.g., Task → Incident) and fields (e.g., Description → Description). If you need help during setup, our support team is available to guide you.

#### Helpful Resources: <a href="#helpful-resources" id="helpful-resources"></a>

* [Quickstart Guides](https://docs.getint.io/guides/quickstart)
* [Integration Instructions](https://docs.getint.io/guides/integration-synchronization/jira-freshservice-integration)
* [Migration Steps](https://docs.getint.io/guides/migration)
* [Workflow Overview](https://docs.getint.io/getintio-platform/workflows)

#### Freshservice Integration: Step-by-Step <a href="#freshservice-integration-step-by-step" id="freshservice-integration-step-by-step"></a>

Here’s a quick look at how to connect Freshservice with other platforms:

1. **Access Getint**: If you're using Jira, go to the Apps section and install Getint from the [Atlassian Marketplace](https://marketplace.atlassian.com/apps/1227929/freshservice-freshdesk-integration-for-jira-2-way-work-sync?hosting=cloud\&tab=overview). For other platforms, choose either Getint SaaS or On-Premise, depending on your setup.
2. **Generate Your Freshservice API Token**: Log in to [Freshservice](https://docs.getint.io/guides/quickstart/connection#freshservice), click your profile icon in the top-right corner, and go to Profile Settings. On the right sidebar, click "View API Key," complete the captcha, and copy the key. You'll use this to connect Freshservice to Getint.
3. **Create the Connection**: Make sure you’re logged in with the right permissions. In Getint, click "Select App" and choose Freshservice. Then click "Create New" to start a new connection. Add your Freshservice URL, enter your credentials, and save the connection.
4. **Link a Second Tool**: Choose another platform to connect with Freshservice—this could be another Freshservice instance, Jira, ServiceNow, or any other supported tool.
5. **Map Types and Fields**: Use Getint's Quick Build feature to automatically map Freshservice fields, or configure them manually. You can link incident types and sync fields like status, priority, and description.

If you run into any issues or need help with setup, our support team is ready to assist.

### Supported Fields for Freshservice Integrations <a href="#supported-fields-for-freshservice-integrations" id="supported-fields-for-freshservice-integrations"></a>

Getint lets you map fields between Freshservice and other platforms. Here’s how it works:

#### Field Mapping Options: <a href="#field-mapping-options" id="field-mapping-options"></a>

* **One-Way Mapping**: Changes made in one app appear in the other, but not the reverse.
* **Two-Way Mapping**: Updates are reflected in both apps automatically.

{% hint style="info" %}
Tip: Read-only fields can’t be edited directly, but Getint offers a way to sync or migrate them using custom fields. Setup steps are available in our guides.
{% endhint %}

| **Freshservice Field**                                                         | **One Way** | **Both Ways** |
| ------------------------------------------------------------------------------ | ----------- | ------------- |
| Assigned to                                                                    | ✔️          | ✔️            |
| Category                                                                       | ✔️          | ✔️            |
| Comments & Attachments                                                         | ✔️          | ✔️            |
| <p>Custom fields</p><p><strong>Date - Dropdown - Single line text</strong></p> | ✔️          | ✔️            |
| Department                                                                     | ✔️          | ✔️            |
| Description                                                                    | ✔️          | ✔️            |
| Group                                                                          | ✔️          | ✔️            |
| Id                                                                             | ✔️          |               |
| Item                                                                           | ✔️          | ✔️            |
| Priority                                                                       | ✔️          | ✔️            |
| Requester                                                                      | ✔️          | ✔️            |
| Status                                                                         | ✔️          | ✔️            |
| Source                                                                         | ✔️          | ✔️            |
| Status                                                                         | ✔️          | ✔️            |
| Subject                                                                        | ✔️          | ✔️            |
| Sub-category                                                                   | ✔️          | ✔️            |
| Time Tracking - Original Estimate                                              | ✔️          | ✔️            |
| Time tracking date field                                                       | ✔️          | ✔️            |
| Type                                                                           | ✔️          | ✔️            |
| URL                                                                            | ✔️          |               |

{% hint style="warning" %}
**Important Note:**\
We strive to maintain the accuracy of this list, but please be aware that supported fields may vary in the original product.
{% endhint %}

### Things to Keep in Mind

While Getint supports many features, here are a few important notes:

* **Required Fields**: You must map Requester, Status (set to "Open" for new tickets), and Priority for the integration to work properly. More information about field mappings [here](https://docs.getint.io/guides/integration-synchronization/jira-freshservice-integration#id-7.-field-mapping).
* **Comment Attribution**: Comments will appear under the account selected during setup. For best results, we recommend using a dedicated Service Account. The original author's name will still show in the comment footer.
* **Change History**: Syncing historical changes isn't supported due to API limitations in Jira and Freshservice.

### Case Studies and Support

Our team is here to help you get started, troubleshoot issues, and answer any questions. If you're seeking assistance or a deeper understanding of our solution, we invite you to schedule a demo call [here](https://www.getint.io/schedule-demo-call).

#### Real-World Examples

Companies of all sizes use Getint to connect their tools and manage data more effectively. Check out our [Case Studies](https://www.getint.io/case-studies) to see how others have used Getint in different environments.

{% hint style="info" %}
**Need something specific that's not currently supported?**

Please contact our [support team](https://getint.io/help-center), and we will assist you in developing a customized solution to your specific needs.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>

# GitHub

## Getint: Simplifying GitHub Integration and Data Synchronization <a href="#getint-simplifying-github-integration-and-data-synchronization" id="getint-simplifying-github-integration-and-data-synchronization"></a>

Getint facilitates seamless integration between multiple platforms, enabling synchronization across tools like GitHub, Jira, Asana, and Azure DevOps. It supports both SaaS and On-Premise deployment, offering adaptability to suit diverse business requirements.

### Key Topics Covered: <a href="#key-topics-covered" id="key-topics-covered"></a>

* [Installing and Configuring the Application](#installing-and-configuring-getint-for-github)
* [Supported GitHub Fields](#supported-github-fields)
* [Key Considerations](#key-considerations)
* [Contacting Support - Case Studies](#contacting-our-support-team)

By synchronizing data across instances and platforms, Getint empowers users to efficiently track and manage tasks while integrating GitHub with other project management tools.

### Installing and Configuring Getint for GitHub <a href="#installing-and-configuring-getint-for-github" id="installing-and-configuring-getint-for-github"></a>

Getint simplifies connecting and migrating data between systems. Below are the steps to get started:

**Step 1: Access Getint**

* **Want to integrate Jira with GitHub?** Just download the app from the Atlassian Marketplace. It's quick and easy! You can find it here: [GitHub Integration for Jira.](https://marketplace.atlassian.com/apps/1223933/github-integration-for-jira-github-connector?hosting=cloud\&tab=overview)
* Other tools: Select between [Getint On-Premise or SaaS options.](https://app.getint.io/app/auth/sign-up)

**Step 2: Set Up a Connection with GitHub**

* Ensure you have the correct access permissions. Here you will find all the steps to generate an access token in GitHub: [Generating a GitHub Token.](https://docs.getint.io/guides/quickstart/connection#github)
* Choose GitHub as the app, create a new connection, and enter your GitHub access token.

**Step 3: Connect to Another Tool**

* Choose the platform you want to integrate with GitHub, such as Jira.

**Step 4: Map Types and Fields**

* Match GitHub issue types, such as Tasks, with their equivalents in the other tool.
* Leverage the Quick Build feature for automatic mapping, or adjust mappings manually to fit your needs.

If you need help with setup or run into any challenges, our support team is always here to assist.

For additional guidance on using Getint with GitHub, refer to:

* [Quickstart Guides](https://docs.getint.io/guides/quickstart)
* [Jira GitHub Integration Guide](https://docs.getint.io/guides/integration-synchronization/jira-github-integration)
* [Migration Guides](https://docs.getint.io/guides/migration)

### Setting Up a Git Repository Integration <a href="#setting-up-a-git-repository-integration" id="setting-up-a-git-repository-integration"></a>

#### **Configuration Steps**

1. **Create a Git Connector Integration**: Navigate to the Getint dashboard and select Git Connector. Choose GitHub as your app.
2. **Authenticate with GitHub**: Generate an [access token](https://docs.getint.io/guides/quickstart/connection#github). Grant access to the repositories you want to sync.
3. **Set up OAuth for Jira**: Unlike Continuous Syncs or data Migrations, Git integrations need OAuth setup directly within your Jira environment. Follow the steps outlined in our guide: [Connection | Jira OAuth.](https://docs.getint.io/guides/quickstart/connection#jira-cloud-oauth)
4. **Select Repositories**: Choose one or more GitHub repositories to link with Getint. You can sync issues, pull requests, and commits.
5. **Test & Activate**: Run a test sync to verify everything works as expected. Once confirmed, activate the integration.
6. **Sync Your Branches**: Use the correct prefixes outlined in our [Git Integration](https://docs.getint.io/guides/integration-synchronization/git-integrations/git-connector-github#id-5.-test-the-integration-and-sync-your-branches) article to sync the branches, commits, and pull requests.

{% hint style="info" %}
All the installation steps to connect your Git Repository with Jira are located in our dedicated article: [Git Connector - GitHub](https://docs.getint.io/guides/integration-synchronization/git-integrations/git-connector-github).
{% endhint %}

### Supported GitHub Fields <a href="#supported-github-fields" id="supported-github-fields"></a>

Getint allows you to map fields between different platforms, and here's a list of our currently supported:

{% hint style="info" %}

#### **How Field Mappings Work:** <a href="#how-field-mappings-work" id="how-field-mappings-work"></a>

**One-Way Mapping:**

* When you update fields in one of the synced apps, those changes will appear in the other app. However, updates made in the other app won’t affect the first app because the fields are read-only.

**Two-Way Mapping:**

* Updates to synced fields will be reflected in both apps. If you modify a field in one app, the change will automatically sync to the other app as well.

**Tip:**

While technically it's not possible to directly modify read-only fields, we offer a solution to achieve bidirectional integration or migrate these fields using custom fields. Setting up this solution requires specific steps, but it is indeed possible. You can find more detailed information in this [article.](https://docs.getint.io/getting-started-with-the-platform/prepare-for-integration/understanding-the-difference-between-platforms-you-integrate)
{% endhint %}

| **GitHub Field** | **One Way**                                                                                                                                                                          | **Both Ways**                                                                                                                                                                        |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Assignee         | ✔️                                                                                                                                                                                   | ✔️                                                                                                                                                                                   |
| Author           | ✔️                                                                                                                                                                                   |                                                                                                                                                                                      |
| Comments         | ✔️                                                                                                                                                                                   | ✔️                                                                                                                                                                                   |
| Description      | ✔️                                                                                                                                                                                   | ✔️                                                                                                                                                                                   |
| ID               | ✔️                                                                                                                                                                                   |                                                                                                                                                                                      |
| Labels           | <img src="https://pf-emoji-service--cdn.us-east-1.prod.public.atl-paas.net/standard/ef8b0642-7523-4e13-9fd3-01b65648acf6/64x64/2716.png" alt="multiplication sign" data-size="line"> | <img src="https://pf-emoji-service--cdn.us-east-1.prod.public.atl-paas.net/standard/ef8b0642-7523-4e13-9fd3-01b65648acf6/64x64/2716.png" alt="multiplication sign" data-size="line"> |
| Title            | ✔️                                                                                                                                                                                   | ✔️                                                                                                                                                                                   |

{% hint style="warning" %}
**Important Note:** While we make every effort to ensure the accuracy of this list, please be aware that supported fields may differ in the original product.
{% endhint %}

### Key Considerations

At Getint, we are committed to continuously updating our supported features, fields, and compatible apps. However, please keep the following key points in mind:

* **Attachments**: You can sync attachments from GitHub to Jira by providing S3 credentials.
* **Change History**: Getint cannot integrate the history of changes.
* **Comments**: Comments added by Getint will appear under the user account you choose during connection setup. Consider creating a dedicated Service Account for integration to maintain consistency. The original author’s name will appear in the comment footer, but the comment will be assigned to the connecting account. Also, comments and attachments transferred from GitHub to Jira will be set to public or private (they will be public by default). You can configure Jira to mark all comments from GitHub as private automatically. However, enabling both public and private visibility options is impossible.
* **Custom fields**: Currently, there's no support for custom fields.
* **Inline** **images** aren't supported.
* **Labels** aren't supported.

### Contacting Our Support Team

Our dedicated Support Team is here to assist with your integration and migration needs. Whether you have questions or seek deeper insights into our solution, you’re welcome to schedule a [demo call](https://www.getint.io/schedule-demo-call) with us.

#### Case Studies

Discover how Getint enhances tool integration for businesses of all sizes. Our [Case Studies](https://www.getint.io/case-studies) highlight real-world solutions designed to empower teams and organizations.

{% hint style="info" %}
**Looking for a solution we don’t currently support?** Reach out to our [support team](https://getint.io/help-center); we’d be happy to help you explore a customized solution tailored to your needs.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>

# GitLab

## Getint: Simplifying GitLab Integration and Data Synchronization <a href="#getint-simplifying-gitlab-integration-and-data-synchronization" id="getint-simplifying-gitlab-integration-and-data-synchronization"></a>

**Getint** is designed to connect and synchronize various tools, supporting integrations such as GitLab with Jira, Asana, or Azure DevOps. It offers both SaaS and On-Premise solutions, providing flexibility for different business needs.

### Key Topics Covered: <a href="#key-topics-covered" id="key-topics-covered"></a>

* [Setting Up the App](#how-to-set-up-getint-for-gitlab)
* [Supported Fields in GitLab](#supported-fields-for-gitlab-integration)
* [Supported Item Types](#supported-fields-for-gitlab-integration)
* [Limitations and Considerations](#limitations-and-considerations)
* [Contacting Support - Case Studies](#contacting-our-support-team)

Getint helps synchronize data across platforms or instances, including GitLab. It enables users to monitor and manage tasks or activities across projects and integrate GitLab with other tools.

### How to Set Up Getint for GitLab <a href="#how-to-set-up-getint-for-gitlab" id="how-to-set-up-getint-for-gitlab"></a>

Getint simplifies connecting and migrating data between systems. Below are the steps to get started:

**Step 1: Access Getint**

* **Want to integrate Jira with GitLab?** Just download the app from the Atlassian Marketplace. It's quick and easy! You can find it here: [GitLab Integration for Jira.](https://marketplace.atlassian.com/apps/1223999/gitlab-integration-for-jira-gitlab-connector-2-way-sync?hosting=cloud\&tab=overview)
* Other tools: Select between Getint On-Premise or SaaS options.

**Step 2: Set Up a Connection with GitLab**

* Ensure you have the correct access permissions. Here you will find all the steps to generate an access token in GitLab: [Generating a GitLab Token.](https://docs.getint.io/guides/quickstart/connection#gitlab)
* Choose GitLab as the app, create a new connection, and enter your GitLab access token.

**Step 3: Connect to Another Tool**

* Choose the platform you want to integrate with GitLab, such as Jira.

**Step 4: Map Types and Fields**

* Match GitLab issue types, such as Incidents, with their equivalents in the other tool.
* Leverage the Quick Build feature for automatic mapping, or adjust mappings manually to fit your needs.

If you need help with setup or run into any challenges, our support team is always here to assist.

For additional guidance on using Getint with GitLab, refer to:

* [Quickstart Guides](https://docs.getint.io/guides/quickstart)
* [Jira GitLab Integration Guide](https://docs.getint.io/guides/integration-synchronization/jira-gitlab)
* [Migration Guides](https://docs.getint.io/guides/migration)

### Supported Fields for GitLab Integration <a href="#supported-fields-for-gitlab-integration" id="supported-fields-for-gitlab-integration"></a>

Getint allows you to map fields between different platforms, and here's a list of our currently supported:

{% hint style="info" %}

#### **How Field Mappings Work:** <a href="#how-field-mappings-work" id="how-field-mappings-work"></a>

**One-Way Mapping:**

* When you update fields in one of the synced apps, those changes will appear in the other app. However, updates made in the other app won’t affect the first app because the fields are read-only.

**Two-Way Mapping:**

* Updates to synced fields will be reflected in both apps. If you modify a field in one app, the change will automatically sync to the other app as well.

**Tip:**

While technically it's not possible to directly modify read-only fields, we offer a solution to achieve bidirectional integration or migrate these fields using custom fields. Setting up this solution requires specific steps, but it is indeed possible. You can find more detailed information in this [article.](https://docs.getint.io/getting-started-with-the-platform/prepare-for-integration/understanding-the-difference-between-platforms-you-integrate)
{% endhint %}

| **GitLab Field**  | **One Way** | **Both Ways** |
| ----------------- | ----------- | ------------- |
| Assignee          | ✔️          | ✔️            |
| Attachments       | ✔️          |               |
| Author Name       | ✔️          |               |
| Closed At         | ✔️          |               |
| Comments          | ✔️          | ✔️            |
| Confidential      | ✔️          |               |
| Created At        | ✔️          |               |
| Discussion Locked | ✔️          |               |
| Due date          | ✔️          | ✔️️           |
| Epic Id           | ✔️          |               |
| Epic Name         | ✔️          |               |
| ID                | ✔️          |               |
| Labels            | ✔️          | ✔️            |
| Milestone Name    | ✔️          |               |
| Reporter          | ✔️          |               |
| Status            | ✔️          | ✔️            |
| Time Estimate     | ✔️          |               |
| Time Spent        | ✔️          |               |
| Title             | ✔️          |               |
| Updated At        | ✔️          |               |
| URL               | ✔️          |               |
| Weight            | ✔️          |               |

{% hint style="warning" %}
**Important Note:** While we make every effort to ensure the accuracy of this list, please be aware that supported fields may differ in the original product.
{% endhint %}

### Limitations and Considerations <a href="#limitations-and-considerations" id="limitations-and-considerations"></a>

At Getint, we are committed to continuously updating our supported features, fields, and compatible apps. However, please keep the following key points in mind:

* **Attachments**: You can sync attachments from GitLab to Jira with a cookie header. These attachments will always sync one way from GitLab to the counterpart tool. More information about this option here: [Attachments Sync in GitLab Integration.](https://docs.getint.io/guides/integration-synchronization/jira-gitlab/attachments-sync-in-gitlab-integration)
* **Change History**: Getint cannot integrate the history of changes.
* **Comments**: Comments added by Getint will appear under the user account you choose during connection setup. Consider creating a dedicated Service Account for integration to maintain consistency. The original author’s name will appear in the comment footer, but the comment will be assigned to the connecting account. Also, comments and attachments transferred from GitLab to Jira will be set to public or private (they will be public by default). You can configure Jira to mark all comments from GitLab as private automatically. However, enabling both public and private visibility options is impossible.
* **Custom fields**: Currently, GitLab has no support for custom fields.
* **Inline** **images** aren’t supported.
* **Issue Types**: When Getint creates a new issue in GitLab, it will always be one specific type (i.e., Issue, or Incident). You can set the default item type using a rule or manually adjust it in GitLab after creation.

### Contacting Our Support Team <a href="#contacting-our-support-team" id="contacting-our-support-team"></a>

Our dedicated Support Team is here to assist with your integration and migration needs. Whether you have questions or seek deeper insights into our solution, you’re welcome to schedule a [demo call](https://www.getint.io/schedule-demo-call) with us.

#### Case Studies <a href="#case-studies" id="case-studies"></a>

Discover how Getint enhances tool integration for businesses of all sizes. Our [Case Studies](https://www.getint.io/case-studies) highlight real-world solutions designed to empower teams and organizations.

{% hint style="info" %}
**Looking for a solution we don’t currently support?** Reach out to our [support team](https://getint.io/help-center)—we’d be happy to help you explore a customized solution tailored to your needs.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>

# HubSpot

## Getint: Simplifying HubSpot Integration and Data Synchronization

**Getint** is designed to connect and synchronize various tools, supporting integrations such as HubSpot with Jira, Asana, or Azure DevOps. We offer SaaS and On-Premise solutions, providing flexibility for different business needs.

### Key Topics Covered

* [Setting Up the App](#how-to-set-up-getint-for-hubspot)
* [Supported Fields in HubSpot](#supported-fields-for-hubspot-integration)
* [Supported Item Types](#supported-item-types-for-hubspot-integration)
* [Limitations and Considerations](#limitations-and-considerations)
* [Contacting Support - Case Studies](#contacting-our-support-team)

Getint helps synchronize data across platforms or instances, including HubSpot. It enables users to monitor and manage tasks or activities across projects and integrate HubSpot with other tools.

### How to Set Up Getint for HubSpot

Getint simplifies connecting and migrating data between systems. Below are the steps to get started:

**Step 1: Access Getint**

* For Jira users: If you want to integrate Jira with HubSpot, download the app from the [Atlassian Marketplace](https://marketplace.atlassian.com/apps/1231637/hubspot-integration-for-jira-bi-directional-issue-sync?hosting=cloud\&tab=overview).
* For other tools: Select between Getint On-Premise or SaaS options.

**Step 2: Set Up a Connection with HubSpot**

* Ensure you have the correct [access permissions](https://docs.getint.io/guides/quickstart/connection#hubspot).
* Choose HubSpot as the app, create a new connection, and enter your HubSpot credentials.

**Step 3: Connect to Another Tool**

* Pick the platform you want to integrate with HubSpot, such as Jira.

**Step 4: Map Types and Fields**

* Match HubSpot categories like Contacts or Deals with their counterparts in the other tool.
* Use the "Quick Build" feature for automatic mapping or customize mappings manually if needed.

Our support team is always available to assist with any setup or operational challenges.

For additional guidance on using Getint with HubSpot, refer to:

* [Quickstart Guides](https://docs.getint.io/guides/quickstart)
* [Jira HubSpot Integration Guide](https://docs.getint.io/guides/integration-synchronization/jira-hubspot-integration)
* [Migration Guides](https://docs.getint.io/guides/migration)

### Supported Fields for HubSpot Integration

Getint allows you to map fields between different platforms, and here's a list of our currently supported:

{% hint style="info" %}

#### **How Field Mappings Work:**

**One-Way Mapping:**

* When you update fields in one of the synced apps, those changes will appear in the other app. However, updates made in the other app won’t affect the first app because the fields are read-only.

**Two-Way Mapping:**

* Updates to synced fields will be reflected in both apps. If you modify a field in one app, the change will automatically sync to the other app as well.

**Tip:**

While technically it's not possible to directly modify read-only fields, we offer a solution to achieve bidirectional integration or migrate these fields using custom fields. Setting up this solution requires specific steps, but it is indeed possible. You can find more detailed information in this [article.](https://docs.getint.io/getting-started-with-the-platform/prepare-for-integration/understanding-the-difference-between-platforms-you-integrate)
{% endhint %}

| **HubSpot Field**                                               | **One Way** | **Both Ways** |
| --------------------------------------------------------------- | ----------- | ------------- |
| All associated contact companies                                | ✔️          |               |
| All associated contact emails                                   | ✔️          |               |
| All associated contact first names                              | ✔️          |               |
| All associated contact last names                               | ✔️          |               |
| All associated contact mobile phones                            | ✔️          |               |
| All associated contact phones                                   | ✔️          |               |
| All conversation mentions                                       | ✔️          |               |
| All Owner IDs                                                   | ✔️          |               |
| All Team IDs                                                    | ✔️          |               |
| All teams                                                       | ✔️          |               |
| Amount                                                          | ✔️          | ✔️            |
| Amount in company currency                                      | ✔️          |               |
| Annual contract value                                           | ✔️          |               |
| Annual recurring revenue                                        | ✔️          |               |
| Applied SLA                                                     | ✔️          | ✔️            |
| Assigned Teams                                                  | ✔️          |               |
| Assigned To (Assignees)                                         | ✔️          | ✔️            |
| Assignment Method                                               | ✔️          | ✔️            |
| Associated Shared Deal Product Interests                        | ✔️          |               |
| Associated Shared Deal Type                                     | ✔️          |               |
| Attributed reporting team                                       | ✔️          | ✔️            |
| Auto-generated from thread id                                   | ✔️          |               |
| Average ticket sentiment                                        | ✔️          |               |
| Average ticket sentiment score                                  | ✔️          |               |
| Business units                                                  | ✔️          | ✔️            |
| Campaign of last booking in meetings tool                       | ✔️          |               |
| Category                                                        | ✔️          |               |
| Close date                                                      | ✔️          | ✔️            |
| Closed Deal Amount                                              | ✔️          |               |
| Closed deal amount in home currency                             | ✔️          |               |
| Closed Deal Close Date                                          | ✔️          |               |
| Closed Deal Create Date                                         | ✔️          |               |
| Closed Deal Lost Reason                                         | ✔️          | ✔️            |
| Closed won count                                                | ✔️          |               |
| Closed Won Date (Internal)                                      | ✔️          |               |
| Closed Won Reason                                               | ✔️          | ✔️            |
| Companies                                                       | ✔️          | ✔️            |
| Comments & Attachments                                          | ✔️          | ✔️            |
| Contacts                                                        | ✔️          | ✔️            |
| Conversation NPS score                                          | ✔️          |               |
| Conversations originating thread id                             | ✔️          |               |
| Copied at                                                       | ✔️          |               |
| Copied by user                                                  | ✔️          |               |
| Copied ticket                                                   | ✔️          |               |
| Copied ticket source                                            | ✔️          |               |
| Create Date                                                     | ✔️          | ✔️            |
| Created by                                                      | ✔️          | ✔️            |
| Created by user ID                                              | ✔️          |               |
| Cumulative time in                                              | ✔️          |               |
| Currency                                                        | ✔️          | ✔️            |
| Custom fields                                                   | ✔️          | ✔️            |
| Custom inbox ID                                                 | ✔️          | ✔️            |
| Customer Agent ticket status                                    | ✔️          |               |
| Date entered                                                    | ✔️          |               |
| Date entered current stage                                      | ✔️          |               |
| Date exited                                                     | ✔️          |               |
| Date of last engagement                                         | ✔️          |               |
| Date of last meeting booked in meetings tool                    | ✔️          |               |
| Days to close                                                   | ✔️          |               |
| Days to close (without rounding)                                | ✔️          |               |
| Draft UserIDs                                                   | ✔️          |               |
| Deal amount calculation preference                              | ✔️          | ✔️            |
| Deal Collaborator                                               | ✔️          | ✔️            |
| Deal Description                                                | ✔️          | ✔️            |
| Deal Name                                                       | ✔️          | ✔️            |
| Deal owner                                                      | ✔️          | ✔️            |
| Deal probability                                                | ✔️          | ✔️            |
| Deal Score                                                      | ✔️          |               |
| Deal Split Users                                                | ✔️          |               |
| Deal Stage                                                      | ✔️          | ✔️            |
| Deal stage probability shadow                                   | ✔️          |               |
| Deal Tags                                                       | ✔️          |               |
| Deal Type                                                       | ✔️          | ✔️            |
| Email Subject                                                   | ✔️          |               |
| External object ids                                             | ✔️          |               |
| Exchange rate                                                   | ✔️          | ✔️            |
| File upload                                                     | ✔️          | ✔️            |
| First agent email response date                                 | ✔️          |               |
| First agent response date                                       | ✔️          |               |
| First message sentiment                                         | ✔️          |               |
| First message sentiment score                                   | ✔️          |               |
| Forecast amount                                                 | ✔️          |               |
| Forcast category                                                | ✔️          | ✔️            |
| Forecast probability                                            | ✔️          | ✔️            |
| Form                                                            | ✔️          |               |
| Form submission conversion ID                                   | ✔️          |               |
| Global Term Line Item Discount Percentage                       | ✔️          | ✔️            |
| Global Term Line Item Recurring Frequency                       | ✔️          | ✔️            |
| Global Term Line Item Recurring Billing Period                  | ✔️          | ✔️            |
| Global Term Line Item Recurring Billing Start                   | ✔️          |               |
| Help Desk onboarding ticket                                     | ✔️          |               |
| Helpdesk Sort Timestamp                                         | ✔️          |               |
| HubSpot Campaign                                                | ✔️          | ✔️            |
| HubSpot Create Date                                             | ✔️          | ✔️            |
| HubSpot Sales Lead                                              | ✔️          |               |
| HubSpot Shared Deal MRR                                         | ✔️          |               |
| HubSpot Shared Deal MRR Currency Code                           | ✔️          |               |
| HubSpot Team                                                    | ✔️          |               |
| ID                                                              | ✔️          |               |
| Inbox ID                                                        | ✔️          |               |
| Is Closed (numeric)                                             | ✔️          |               |
| Is Open (numeric)                                               | ✔️          |               |
| Item Type                                                       | ✔️          |               |
| Language                                                        | ✔️          | ✔️            |
| Last Activity Date                                              | ✔️          |               |
| Last Activity Date (Ticket Note)                                | ✔️          |               |
| Last Contacted                                                  | ✔️          |               |
| Last CES                                                        | ✔️          |               |
| Last customer reply date                                        | ✔️          |               |
| Last email activity                                             | ✔️          |               |
| Last email date                                                 | ✔️          |               |
| Last email ID                                                   | ✔️          |               |
| Last email type                                                 | ✔️          |               |
| Last Modified Date                                              | ✔️          |               |
| Last Response Date                                              | ✔️          |               |
| Latest Approval Status                                          | ✔️          |               |
| Latest Approval Status ID                                       | ✔️          |               |
| Latest Meeting Activity                                         | ✔️          |               |
| Latest message                                                  | ✔️          |               |
| Latest time in                                                  | ✔️          |               |
| Latest Traffic Source                                           | ✔️          |               |
| Likelihood to close by the close date                           | ✔️          |               |
| Medium of last booking in meetings tool                         | ✔️          |               |
| Merged Deal IDs                                                 | ✔️          |               |
| Merged Ticket IDs                                               | ✔️          |               |
| mentioned\_note\_user\_IDs                                      | ✔️          |               |
| mentions\_user\_IDs                                             | ✔️          |               |
| Microsoft Teams message ID for this ticket.                     | ✔️          |               |
| Monthly recurring revenue                                       | ✔️          |               |
| Most relevant SLA status                                        | ✔️          | ✔️            |
| Most Relevant SLA Type                                          | ✔️          | ✔️            |
| Next Pipeline Impact                                            | ✔️          | ✔️            |
| Next Activity Date                                              | ✔️          |               |
| Next Activity Type                                              | ✔️          |               |
| Next Meeting ID                                                 | ✔️          |               |
| Next Meeting Name                                               | ✔️          |               |
| Next Meeting Start Time                                         | ✔️          |               |
| Next step                                                       | ✔️          | ✔️            |
| Next Step Updated At                                            | ✔️          |               |
| Number of Active Deal Registrations                             | ✔️          |               |
| Number of Associated Contacts                                   | ✔️          |               |
| Number of Associated Line Items                                 | ✔️          |               |
| Number of Deal Splits                                           | ✔️          |               |
| Number of Sales Activities                                      | ✔️          |               |
| Number of target accounts                                       | ✔️          |               |
| Number of times contacted                                       | ✔️          |               |
| Object Type                                                     | ✔️          |               |
| Open deal create date                                           | ✔️          |               |
| Original Traffic Source                                         | ✔️          | ✔️            |
| Original Traffic Source Drill-Down 1                            | ✔️          |               |
| Original Traffic Source Drill-Down 2                            | ✔️          |               |
| Owner assigned date                                             | ✔️          |               |
| Owning Teams                                                    | ✔️          | ✔️            |
| Pinned Engagement ID                                            | ✔️          | ✔️            |
| Pipeline                                                        | ✔️          | ✔️            |
| Primary Company ID                                              | ✔️          |               |
| Primary Company Name                                            |             |               |
| Priority                                                        | ✔️          | ✔️            |
| Recent Sales Email Replied Date                                 | ✔️          |               |
| Record creation source                                          | ✔️          |               |
| Record creation source ID                                       | ✔️          |               |
| Record creation source user ID                                  | ✔️          |               |
| Record ID                                                       | ✔️          |               |
| Record source                                                   | ✔️          |               |
| Record source detail 1                                          | ✔️          |               |
| Record source detail 2                                          | ✔️          |               |
| Record source detail 3                                          | ✔️          |               |
| Shared teams                                                    | ✔️          | ✔️            |
| Shared users                                                    | ✔️          |               |
| Source Object ID                                                | ✔️          |               |
| Source of last booking in meetings tool                         | ✔️          |               |
| Status transition                                               | ✔️          | ✔️            |
| Task Type                                                       | ✔️          | ✔️            |
| Tasks completed                                                 | ✔️          |               |
| Task Title                                                      | ✔️          | ✔️            |
| The predicted deal amount                                       | ✔️          |               |
| <p>The predicted deal amount in your company's currency<br></p> | ✔️          |               |
| Time in                                                         | ✔️          |               |
| Time to                                                         | ✔️          |               |
| Total contract value                                            | ✔️          |               |
| Unique creation Key                                             | ✔️          |               |
| Updated by user ID                                              | ✔️          |               |
| URL                                                             | ✔️          |               |
| User IDs of all notification followers                          | ✔️          |               |
| User IDs of all notification unfollowers                        | ✔️          |               |
| User IDs of all owners                                          | ✔️          |               |
| Users Interaction                                               | ✔️          |               |
| Weighted amount                                                 | ✔️          |               |
| Weighted amount in company currency                             | ✔️          |               |

{% hint style="warning" %}
**Important Note:**\
We strive to maintain the accuracy of this list, but please be aware that supported fields may vary in the original product.
{% endhint %}

### Supported Item Types for HubSpot Integration

| Company   |
| --------- |
| Contact   |
| Deal      |
| Line Item |
| Quote     |
| Task      |
| Ticket    |

### Limitations and Considerations

At Getint, we continuously update our supported features, fields, and compatible apps. However, there are a few important points to consider:

* **Issue Types:** When Getint creates a new issue in HubSpot, it will always be one specific type (i.e., Task, Deal, or Ticket). You can set the default item type using a rule or manually adjust it in HubSpot after creation.
* **Comments:** Comments added by Getint will appear under the user account you choose during connection setup. Consider creating a dedicated Service Account for integration to maintain consistency. The original author’s name will appear in the comment footer, but the comment will be assigned to the connecting account.

Comments and attachments transferred from HubSpot to Jira will be set to either public or private. You can configure Jira to mark all comments from HubSpot as private automatically. However, it is impossible to enable both public and private visibility options simultaneously.

* **Change History:** Unfortunately, Getint cannot integrate the history of changes.
* **Inline** **images** aren't supported for the Description field.

### Contacting Our Support Team

Our dedicated Support Team is ready to assist with your integration and migration needs. If you have questions or need deeper insights into our solution, feel free to schedule a [demo call](https://www.getint.io/schedule-demo-call) with us.

#### Case Studies

Explore real-world examples of how Getint enhances tool integration for businesses of all sizes. Our [Case Studies](https://www.getint.io/case-studies) showcase tailored solutions that empower teams and organizations.

{% hint style="info" %}
**Are you looking for a specific solution that we don’t currently support?** Please get in touch with our [support team](https://getint.io/help-center), and we can assist you in developing a customized solution for your particular case.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>

# Jira

## Getint: Simplifying Jira Integration and Data Synchronization <a href="#title-text" id="title-text"></a>

Getint is expertly designed to integrate and synchronize an extensive range of tools. It accommodates a variety of connectivity scenarios, such as Jira - Jira, Jira - Azure DevOps, Jira - Asana, Jira - ServiceNow, and more. With its availability as both a Software-as-a-Service (SaaS) and On-Premise solution, Getint offers the versatility to meet the unique requirements of various businesses.

### What does this article cover? <a href="#what-does-this-article-cover" id="what-does-this-article-cover"></a>

* [How to Set Up the App](#setting-up-getint-for-jira)
* [Supported Fields in Jira](#supported-fields-in-jira)
* [Limitations and Considerations to Make](#limitations-to-be-considered)
* [Contacting Our Support Team - Case Studies](#contacting-our-support-team)

Getint enables seamless data synchronization within the same platform or different platforms/different instances. It supports Jira and Jira Service Management of all types (Cloud, Server, Data Center), and across different projects. Allowing users to efficiently track and manage Jira tickets, tasks, bugs, and epics in diverse Jira environments, as well as integrating Jira with other platforms.

### Setting up Getint for Jira <a href="#setting-up-getint-for-jira" id="setting-up-getint-for-jira"></a>

Getint simplifies data integration and migration. With easy setup steps, you can connect your systems, such as Jira, map types (i.e., Task - Task), and fields (i.e., Priority - Priority). Whether you're looking to sync data continuously or perform a one-time migration, Getint has got you covered. Our dedicated support team is always ready to assist you with any challenges you may encounter during setup or operation.

For more detailed guides on how to set up your Jira integration, please make sure to check the following:

* [Starting with Getint - Quickstart Guides](https://docs.getint.io/guides/quickstart)
* [Integration Guides](https://docs.getint.io/guides/integration-synchronization)
* [Migration Guides](https://docs.getint.io/guides/migration)
* [Understanding Getint - Workflows](https://docs.getint.io/getintio-platform/workflows)

Here's a simplified version of how to integrate Jira with other tools (you can find a detailed overview [**here**](https://docs.getint.io/guides/integration-synchronization/jira-jira-integration)):

1. **Access the Getint App in Jira:** The app is available for download in the Atlassian Marketplace. After the installation, navigate to Jira, go to "Apps," and select "the Getint app." Select "Create Integration" then "Continuous Sync" or "Migration" based on your requirements.
2. **Token Generation for Jira Cloud:** Visit Atlassian Account Settings. Go to Security, navigate to the API Token section, and generate a token. This token serves as the password for the Jira Cloud.
3. **Establish a Connection with Jira:** Ensure you're logged in as a user with the correct permissions. Click "Select App" and choose Jira. Select "Create New" to establish a new connection with your Jira instance. Name your connection, and add the URL of your Jira instance (without "/" at the end). Provide the login credentials.
4. **Choose and Connect the Second App:** Choose and connect another tool you'd like to integrate with your Jira—either another Jira instance, DevOps, ServiceNow, Salesforce, or any other tool that we support.
5. **Map Types and Fields:** Link Jira types (Task, Bug, Epic, Story) to synchronize with other tools. You can use the "Quick Build" feature, which allows you to map available fields automatically, or you can set them manually.

Getint's support team is committed to ensuring a smooth and efficient integration experience customized to your unique needs. If you encounter any challenges during setup or require assistance with missing functionalities, our dedicated support team is readily available to provide guidance and help.

### Supported Fields in Jira <a href="#supported-fields-in-jira" id="supported-fields-in-jira"></a>

Getint allows you to map fields between different platforms, and here's a list of our currently supported:

{% hint style="info" %}

#### **How Field Mappings Work:** <a href="#how-field-mappings-work" id="how-field-mappings-work"></a>

**One-Way Mapping:**

* When you update fields in one of the synced apps, those changes will appear in the other app. However, updates made in the other app won’t affect the first app because the fields are read-only.

**Two-Way Mapping:**

* Updates to synced fields will be reflected in both apps. If you modify a field in one app, the change will automatically sync to the other app as well.

**Tip:**

While technically it's not possible to directly modify read-only fields, we offer a solution to achieve bidirectional integration or migrate these fields using custom fields. Setting up this solution requires specific steps, but it is indeed possible. You can find more detailed information in this [article.](https://docs.getint.io/getting-started-with-the-platform/prepare-for-integration/understanding-the-difference-between-platforms-you-integrate)
{% endhint %}

<table data-header-hidden><thead><tr><th width="249"></th><th></th><th></th></tr></thead><tbody><tr><td><strong>Jira Field</strong></td><td><strong>One Way</strong></td><td><strong>Both Ways</strong></td></tr><tr><td>Assignee</td><td>✔️</td><td>✔️</td></tr><tr><td>Attachments</td><td>✔️</td><td>✔️</td></tr><tr><td>Created</td><td>✔️</td><td> </td></tr><tr><td>Comments</td><td>✔️</td><td>✔️</td></tr><tr><td><p>Custom fields</p><p><strong>Short text - Paragraph - Date - Number - Time Stamp - Labels - Dropdown - Checkbox - People - Dependent dropdown - URL</strong></p></td><td>✔️</td><td>✔️</td></tr><tr><td>Description</td><td>✔️</td><td>✔️</td></tr><tr><td>Design</td><td>✔️</td><td>✔️</td></tr><tr><td>Due date</td><td>✔️</td><td>✔️</td></tr><tr><td>Flagged</td><td>✔️</td><td>✔️</td></tr><tr><td>ID</td><td>✔️</td><td> </td></tr><tr><td>Issue color</td><td>✔️</td><td>✔️</td></tr><tr><td>Issue key</td><td>✔️</td><td> </td></tr><tr><td>Issue type name</td><td>✔️</td><td> </td></tr><tr><td>Labels</td><td>✔️</td><td>✔️</td></tr><tr><td>Linked issues</td><td>✔️</td><td>✔️</td></tr><tr><td>Priority</td><td>✔️</td><td>✔️</td></tr><tr><td>Project key</td><td>✔️</td><td> </td></tr><tr><td>Project name</td><td>✔️</td><td> </td></tr><tr><td>Reporter</td><td>✔️</td><td>✔️</td></tr><tr><td>Reporter display name</td><td>✔️</td><td> </td></tr><tr><td>Reporter email</td><td>✔️</td><td> </td></tr><tr><td>Request type</td><td>✔️</td><td>✔️</td></tr><tr><td>Resolution</td><td>✔️</td><td> </td></tr><tr><td>Resolved</td><td>✔️</td><td>✔️</td></tr><tr><td>Satisfaction</td><td>✔️</td><td></td></tr><tr><td>Sprint</td><td>✔️</td><td> </td></tr><tr><td>Start date</td><td>✔️</td><td>✔️</td></tr><tr><td>Status</td><td>✔️</td><td>✔️</td></tr><tr><td>Story point estimate</td><td>✔️</td><td>✔️</td></tr><tr><td>Story points</td><td>✔️</td><td>✔️</td></tr><tr><td>Subtasks</td><td>✔️</td><td>✔️</td></tr><tr><td>Time tracking - Original estimate</td><td>✔️</td><td>✔️</td></tr><tr><td>Time tracking - Remaining estimate</td><td>✔️</td><td> </td></tr><tr><td>Time tracking - Time spent</td><td>✔️</td><td> </td></tr><tr><td>Title (Summary)</td><td>✔️</td><td>✔️</td></tr><tr><td>Updated</td><td>✔️</td><td> </td></tr><tr><td>URL</td><td>✔️</td><td> </td></tr></tbody></table>

{% hint style="danger" %}
**Important Note:**\
We strive to maintain the accuracy of this list, but please be aware that supported fields may vary in the original product.
{% endhint %}

### Limitations to be Considered <a href="#limitations-to-be-considered" id="limitations-to-be-considered"></a>

At Getint, we're constantly updating our supported features, fields, and compatible apps. However, there are a few limitations you should be aware of:

* When a new issue is created in Jira by Getint, it will always be one type of issue, whether that's a Task, an Epic, a Feature, or a Bug. You can set the default item type using a rule or manually change it in Jira after it's created.
* Comments will be added as the user you choose to create the connection. Therefore, it is advised to create a dedicated Service Account to build your integration. The original author will appear in the comment footer; however, it will still be assigned to the account that established the connection.
* The history of changes can't be integrated.

### Contacting Our Support Team <a href="#contacting-our-support-team" id="contacting-our-support-team"></a>

Our Support Team at Getint is eager to assist with your integration and migration needs and answer any other questions you may have. If you're seeking assistance or a deeper understanding of our solution, we invite you to schedule a call [here](https://www.getint.io/schedule-demo-call).

#### Case Studies <a href="#case-studies" id="case-studies"></a>

Large and small businesses have experienced the benefits of using Getint for their data integration needs. This has provided them with various solutions tailored to their teams and organizations. We invite you to explore some of our [Case Studies](https://www.getint.io/case-studies), which are true accounts of how Getint continually enhances and improves the tool integration process.

{% hint style="info" %}
**Are you looking for a specific solution that we don’t currently support?** Please get in touch with our [support team](https://getint.io/help-center), and we can assist you in developing a customized solution for your particular case.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>

# Monday.com

## Getint: Simplifying Monday.com Integration and Data Synchronization <a href="#getint-simplifying-monday.com-integration-and-data-synchronization" id="getint-simplifying-monday.com-integration-and-data-synchronization"></a>

Getint, a powerful integration solution, seamlessly connects and synchronizes various tools. It supports multiple connectivity scenarios, including Jira - Monday.com, Monday.com - Azure DevOps, Monday.com - Asana, and more. Whether you choose Software-as-a-Service (SaaS) or On-Premise deployment, Getint provides the flexibility to meet the distinct needs of different businesses.

### What does this article cover? <a href="#what-does-this-article-cover" id="what-does-this-article-cover"></a>

* [How to Set Up the App](#setting-up-getint-for-monday.com)
* [Supported Fields in Monday.com](#supported-fields-in-monday.com)
* [Limitations and Considerations to Make](#limitations-to-be-considered)
* [Contacting Our Support Team - Case Studies](#contacting-our-support-team)

**Getint** facilitates smooth data synchronization across various platforms and instances. It supports **Monday.com,** allowing users to monitor and manage tasks in diverse environments effectively. Additionally, it enables seamless integration with other platforms.

### Setting up Getint for Monday.com <a href="#setting-up-getint-for-monday.com" id="setting-up-getint-for-monday.com"></a>

Getint simplifies data integration and migration. You can connect your systems with easy setup steps, such as Monday.com, map types (i.e., Task - Item), and fields (i.e., Assignee - Responsable). Whether you're looking to sync data continuously or perform a one-time migration, Getint has got you covered. Our dedicated support team is always ready to assist you with any challenges you may encounter during setup or operation.

For more detailed guides on how to configure your Monday.com integration, please make sure to check the following:

* [Starting with Getint - Quickstart Guides](https://docs.getint.io/guides/quickstart)
* [Integration Guides](https://docs.getint.io/guides/integration-synchronization)
* [Migration Guides](https://docs.getint.io/guides/migration)
* [Understanding Getint - Workflows](https://docs.getint.io/getintio-platform/workflows)

Here's a simplified version of how to integrate Monday.com with other tools (you can find a detailed overview [**here**](https://docs.getint.io/guides/integration-synchronization/jira-monday.com-integration)):

1. **Access Getint:** Navigate through the [Atlassian Marketplace](https://marketplace.atlassian.com/apps/1225780/monday-com-integration-for-jira-monday-com-connector?hosting=cloud\&tab=overview) or go to your "Apps" section in Jira, and search for the "Getint Monday.com integration app." Alternatively, if you need to integrate Monday.com with a non-Jira application, consider choosing either [Getint On-Premise or Getint SaaS.](https://app.getint.io/)
2. **Token Generation for Monday.com:** There are two options to see your API token:
   1. **Admin Tab:**
      * Log in to your "Monday.com" account.
      * Click your "avatar/profile picture" in the top right corner.
      * Go to **Administration** > **Connections** > **API.**
      * Copy your personal token.
   2. **Developer Tab:**
      * Log in to your "Monday.com" account.
      * Click your profile picture in the top right corner.
      * Visit "Developers" to open the Developer Center.
      * Click **My Access Tokens** > **Show.**
      * Copy your personal token.
3. **Establish a Connection with Monday.com:** Ensure you're logged in as a user with the correct permissions. Click "Select App" and choose "Monday.com." Select "Create New" to establish a new connection with your Monday.com instance. Name your connection, and add the URL of your Monday.com instance. Provide the login credentials.
4. **Choose and Connect the Second App:** You can select and link an additional tool to integrate with Monday.com. Options include another Monday.com instance, ServiceNow, Jira, or any other supported tool.
5. **Map Types and Fields:** Link "Monday.com types" (Items, SubItems) to synchronize with other tools. You can use the "Quick Build" feature, which allows you to map available fields automatically, or you can set them manually.

Getint's support team is dedicated to delivering a seamless and efficient integration experience tailored to your specific requirements. Should you encounter any setup challenges or need assistance with missing features, our committed support team is ready to provide guidance and help.

### Supported Fields in Monday.com <a href="#supported-fields-in-monday.com" id="supported-fields-in-monday.com"></a>

Getint allows you to map fields between different platforms, and here's a list of our currently supported:

{% hint style="info" %}

#### **Field Mappings Explained:** <a href="#field-mappings-explained" id="field-mappings-explained"></a>

**One-Way Mapping:**

* When you update fields in one of the synchronized apps, those changes will appear in the other app.
* However, updates made in the other app won’t affect the first app because the fields are read-only.

**Two-Way Mapping:**

* Updates to synced fields will be reflected in both apps.
* If you modify a field in one app, the change will automatically sync to the other app as well.

**Tip:** While it’s technically not possible to directly modify read-only fields, we offer a solution for achieving bidirectional integration or migrating these fields using custom fields. Setting up this solution requires specific steps, but it is indeed possible. You can find more detailed information in this [article.](https://docs.getint.io/getting-started-with-the-platform/prepare-for-integration/understanding-the-difference-between-platforms-you-integrate)
{% endhint %}

| **Monday.com Field**                                                                                                            | **One Way** | **Both Ways** |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------- |
| Comments & Attachments                                                                                                          | ✔️          | ✔️            |
| <p>Custom fields</p><p><strong>Dropdown - Label - People - Priority - Status - Text - Timeline Start Date/End Date</strong></p> | ✔️          | ✔️            |
| Date                                                                                                                            | ✔️          | ✔️            |
| Group                                                                                                                           | ✔️          | ✔️            |
| ID                                                                                                                              | ✔️          |               |
| Person                                                                                                                          | ✔️          | ✔️            |
| Status                                                                                                                          | ✔️          | ✔️            |
| Title (Name)                                                                                                                    | ✔️          | ✔️            |
| URL                                                                                                                             | ✔️          |               |

{% hint style="danger" %}
**Important Note:**\
We strive to maintain the accuracy of this list, but please be aware that supported fields may vary in the original product.
{% endhint %}

### Limitations to be Considered

At Getint, we continuously update our supported features, fields, and compatible apps. However, there are a few important limitations to keep in mind:

* When you add comments to an issue, they will be displayed under the user account you select to establish the connection. For smooth integration, it’s advisable to create a dedicated Service Account specifically for building your integration. Although the original author’s name will be visible in the comment footer, the comment itself will remain associated with the account that set up the connection.
* Unfortunately, incorporating the history of changes is not feasible at this time.
* Attachments need to be uploaded from the **Files** column in your Monday.com project, not from the **Files** section within the tasks. Otherwise, your attachments will not trigger syncs to the other app you integrate.
* Updates to existing comments will not trigger syncs. Subcomments do not trigger syncs as well.

### Contacting Our Support Team

Our Support Team at Getint is eager to assist with your integration and migration needs and answer any other questions you may have. If you're seeking assistance or a deeper understanding of our solution, we invite you to schedule a demo call [here](https://www.getint.io/schedule-demo-call).

#### Case Studies

Large and small businesses have experienced the benefits of using Getint for their data integration needs. This has provided them with various solutions tailored to their teams and organizations. We invite you to explore some of our [Case Studies](https://www.getint.io/case-studies), which are true accounts of how Getint continually enhances and improves the tool integration process.

{% hint style="info" %}
**Are you looking for a specific solution that we don’t currently support?** Please get in touch with our [support team](https://getint.io/help-center), and we can assist you in developing a customized solution for your particular case.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>

# Notion

## Getint: Simplifying Notion Integration and Data Synchronization

Getint simplifies the integration and synchronization of a wide range of tools. It supports various connectivity scenarios, including Notion - Jira, Notion - Asana, Notion - Monday, Notion - Azure DevOps, and more. Whether you need a software-as-a-service (SaaS) or an On-premise solution, Getint offers the flexibility to meet the unique requirements of different businesses.

### The article covers the following topics

* [How to Setup the App](#setting-up-getint-for-notion)
* [Supported Fields in Notion](#supported-fields-in-notion)
* [Limitations and Considerations to Keep in Mind](#limitations-to-keep-in-mind)
* [Case Studies and Contacting Our Support Team](#contacting-our-support-team-and-case-studies)

Getint ensures seamless data synchronization across platforms and instances, with specific support for Notion. Users can effectively monitor and manage tasks in diverse environments while seamlessly integrating with other platforms.

### Setting Up Getint for Notion

Getint simplifies data integration and migration. Follow these straightforward steps to connect your systems, such as Notion, map types (i.e., Task - Task), and fields (i.e., Description - Summary). Whether you’re syncing data or performing a continuous one-time migration, Getint has you covered. Our dedicated support team is ready to assist you with any setup or operational challenges.

For more detailed guides on setting up your Notion integration, refer to the following resources:

* [Starting with Getint - Quickstart Guides](https://docs.getint.io/guides/quickstart)
* [Integration Guides](https://docs.getint.io/guides/integration-synchronization)
* [Migration Guides](https://docs.getint.io/guides/migration)
* [Understanding Getint - Workflows](https://docs.getint.io/getintio-platform/workflows)

Here's a simplified version of how to integrate Notion with other tools (you can find a detailed overview [**here**](https://docs.getint.io/guides/integration-synchronization/jira-notion-integration)):

1. **Access Getint:** If you’re using Jira, navigate to the "Apps" section, search for new apps, and acquire the app from the [Atlassian Marketplace.](https://marketplace.atlassian.com/apps/1231784/notion-integration-for-jira?tab=overview\&hosting=cloud) Alternatively, if you need to integrate Notion with a non-Jira application, consider choosing either [Getint On-Premise or Getint SaaS.](https://www.getint.io/contact)
2. **Token Generation for Notion:**
   * Open the "Notion" app.
   * Click on the "three dots" located in the top right corner.
   * Select "Add a Connection."
   * Navigate to "Manage Connections" and choose "Develop or Manage integrations."
   * Click on "New Integration."
   * Provide a name for your integration, grant the necessary permissions, and copy the "API token." This will be your password to create a connection.
3. **How to Establish a Connection with Notion:** Ensure you’re logged in as a user with the correct permissions. Click "Select App" and choose "Notion." Select "Create New" to establish a new connection with your Notion instance. Name your connection and add the "URL" of your Notion instance. Provide your login credentials to connect with Getint.
4. **Choose and Connect the Second App:** Select and link another tool to integrate with Notion—options include another Notion instance, ServiceNow, Jira, or any other supported tool.
5. **Mapping Types and Fields:** Link Notion types (Tasks) to synchronize with other tools. You can use the "Quick Build" feature, which allows you to map available fields automatically or set them manually.

Getint's support team is committed to ensuring a smooth and efficient integration experience customized to your unique needs. If you encounter any challenges during setup or require assistance with missing functionalities, our dedicated support team can provide guidance and assistance.

### Supported Fields in Notion

Getint allows you to map fields between different platforms, and here's a list of our currently supported:

{% hint style="info" %}

#### **How Field Mappings Work:**

**One-Way Mapping:**

* When you update fields in one of the synchronized apps, those changes will appear in the other app. However, updates made in the other app won’t impact the first app because the fields are read-only.

**Two-Way Mapping:**

* Updates to synchronized fields will be reflected in both apps. If you modify a field in one app, the change will automatically sync to the other app as well.

**Tip:** While it’s technically not possible to directly modify read-only fields, we provide a solution for achieving bidirectional integration or migrating these fields using custom fields. Setting up this solution requires specific steps, but it is indeed feasible. You can find more detailed information in this [article.](https://docs.getint.io/getting-started-with-the-platform/prepare-for-integration/understanding-the-difference-between-platforms-you-integrate)
{% endhint %}

| **Notion Field**                                                                                                     | **One Way** | **Both Ways** |
| -------------------------------------------------------------------------------------------------------------------- | ----------- | ------------- |
| Comments & Attachments                                                                                               | ✔️          | ✔️            |
| <p>Custom fields</p><p><strong>Checkbox - Date - Description - Estimates - Select - Status - Text - URL</strong></p> | ✔️          | ✔️            |
| Database Id                                                                                                          | ✔️          | ✔️            |
| Due (End Date)                                                                                                       | ✔️          | ✔️            |
| Due (Start Date)                                                                                                     | ✔️          | ✔️            |
| Item Type                                                                                                            | ✔️          |               |
| Priority                                                                                                             | ✔️          | ✔️            |
| Reason                                                                                                               | ✔️          | ✔️            |
| Status                                                                                                               | ✔️          | ✔️            |
| Summary                                                                                                              | ✔️          | ✔️            |
| Task name                                                                                                            | ✔️          | ✔️            |
| URL                                                                                                                  | ✔️          |               |

{% hint style="warning" %}
**Important Note:**\
We strive to maintain the accuracy of this list, but please be aware that supported fields may vary in the original product.
{% endhint %}

### Limitations to Keep in Mind

At Getint, we continuously update our supported features, fields, and compatible apps. However, there are a few important limitations to keep in mind:

* At the time of publishing this article, we currently only support mapping Tasks for Notion, and Assignees are not supported.
* Comments added to the issue will display under the user account you select when creating the connection. For a seamless integration, we recommend creating a dedicated Service Account. Although the original author’s name will appear in the comment footer, the comment will still be linked to the account that established the connection.
* Unfortunately, integrating the history of changes is not possible due to the technical limitations of Jira / Notion APIs.

### Contacting Our Support Team & Case Studies

Our Support Team at Getint is eager to assist with your integration and migration needs and answer any other questions you may have. If you're seeking assistance or a deeper understanding of our solution, we invite you to schedule a demo call [here](https://www.getint.io/schedule-demo-call).

#### Case Studies

Large and small businesses have experienced the benefits of using Getint for their data integration needs. This has provided them with various solutions tailored to their teams and organizations. We invite you to explore some of our [Case Studies](https://www.getint.io/case-studies), which are true accounts of how Getint continually enhances and improves the tool integration process.

{% hint style="info" %}
**Are you looking for a specific solution that we don’t currently support?** Please get in touch with our [support team](https://getint.io/help-center), and we can assist you in developing a customized solution for your particular case.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>

# Salesforce

## Getint: Simplifying Salesforce Integration and Data Synchronization <a href="#getint-simplifying-salesforce-integration-and-data-synchronization" id="getint-simplifying-salesforce-integration-and-data-synchronization"></a>

Getint, a powerful integration solution, seamlessly connects and synchronizes various tools. It supports various connectivity scenarios, including Salesforce - Jira, Salesforce - Azure DevOps, and more. Whether you require Software-as-a-Service (SaaS) or On-Premise deployment, Getint provides the flexibility to meet the distinct needs of different businesses and companies.

### What does this article cover? <a href="#what-does-this-article-cover" id="what-does-this-article-cover"></a>

* [How to Set Up the App](#setting-up-getint-for-salesforce)
* [Supported Fields in Salesforce](#supported-fields-in-salesforce)
* [Limitations and Considerations to Make](#limitations-to-be-considered)
* [Contacting Our Support Team - Case Studies](#contacting-our-support-team)

**Getint** facilitates smooth data synchronization across various platforms and instances. It supports Salesforce, allowing users to monitor and manage tasks in diverse environments effectively. Additionally, it enables seamless integration with other platforms.

### Setting Up Getint for Salesforce <a href="#setting-up-getint-for-salesforce" id="setting-up-getint-for-salesforce"></a>

Getint simplifies data integration and migration. You can connect your systems with easy setup steps, such as Salesforce, map types (i.e., Task - Case), and fields (i.e., Priority - Priority). Whether you're looking to sync data continuously or perform a one-time migration, Getint has got you covered. Our dedicated support team is always ready to assist you with any challenges you may encounter during setup or operation.

For more detailed guides on how to set up your Salesforce integration, please make sure to check the following:

* [Starting with Getint - Quickstart Guides](https://docs.getint.io/guides/quickstart)
* [Integration Guides](https://docs.getint.io/guides/integration-synchronization)
* [Migration Guides](https://docs.getint.io/guides/migration)
* [Understanding Getint - Workflows](https://docs.getint.io/getintio-platform/workflows)

Here's a simplified version of how to integrate Salesforce with other tools (you can find a detailed overview [**here**](https://docs.getint.io/guides/integration-synchronization/jira-salesforce-integration)):

1. **Access Getint:** Navigate through the [Atlassian Marketplace](https://marketplace.atlassian.com/apps/1231635/connector-for-salesforce-jira-salesforce-integration?hosting=cloud\&tab=overview), go to your "Apps" section in Jira, and search for the "Getint Salesforce integration" app. Alternatively, if you need to integrate Salesforce with a non-Jira application, consider choosing either [Getint On-Premise or Getint SaaS.](https://app.getint.io/)
2. **Token Generation for Salesforce:** To connect with Salesforce, users must grant an "API token" to Getint via the "OAuth authentication" method within our app.
3. **Establishing a Connection with Salesforce:**
   * Ensure you're logged in as a user with the correct permissions. Click "Select App" and choose "Salesforce."
   * Select "Create New" to establish a new connection with your Salesforce instance. Name your connection, and add the URL of your Salesforce instance.
   * Provide the login credentials. Click the "Authorize Getint" button.
   * You’ll be redirected to the Salesforce login page. Once authorized, a confirmation message will prompt you to click "Add" to create the connection. Click "Add."
   * Select the newly created connection and press "Connect."
4. **Choose and Connect the Second App:** You can select and link an additional tool to integrate with Salesforce. Options include another Salesforce instance, ServiceNow, Jira, or other supported tools.
5. **Map Types and Fields:** Link Salesforce types (Account, Case, and Contact) to synchronize with other tools. You can use the Quick Build feature, which allows you to map available fields automatically, or you can set them manually.

Getint’s support team is dedicated to delivering a seamless and efficient integration experience customized to your specific requirements. Should you encounter any inconveniences or need assistance with missing features, our committed support team is ready to provide guidance and help.

### Supported Fields in Salesforce <a href="#supported-fields-in-salesforce" id="supported-fields-in-salesforce"></a>

Getint allows you to map fields between different platforms, and here's a list of our currently supported:

{% hint style="info" %}

#### **How Field Mappings Work:** <a href="#how-field-mappings-work" id="how-field-mappings-work"></a>

**One-Way Mapping:**

* When you update fields in one of the synced apps, those changes will appear in the other app. However, updates made in the other app won’t affect the first app because the fields are read-only.

**Two-Way Mapping:**

* Updates to synced fields will be reflected in both apps. If you modify a field in one app, the change will automatically sync to the other app as well.

**Tip:** While technically it's not possible to directly modify read-only fields, we offer a solution to achieve bidirectional integration or migrate these fields using custom fields. Setting up this solution requires specific steps, but it is indeed possible. You can find more detailed information in this [article.](https://docs.getint.io/getting-started-with-the-platform/prepare-for-integration/understanding-the-difference-between-platforms-you-integrate)
{% endhint %}

| **Salesforce Field**                                                                             | **One Way** | **Both Ways** |
| ------------------------------------------------------------------------------------------------ | ----------- | ------------- |
| Case Number                                                                                      | ✔️          |               |
| Case Origin                                                                                      | ✔️          | ✔️            |
| Case Reason                                                                                      | ✔️          | ✔️            |
| Case Type                                                                                        | ✔️          | ✔️            |
| Company                                                                                          | ✔️          | ✔️            |
| <p>Custom fields</p><p><strong>Date/Time - Email - Number - Phone - Picklist - Text</strong></p> | ✔️          | ✔️            |
| Engineering Req Number                                                                           | ✔️          | ✔️            |
| Free Text                                                                                        | ✔️          | ✔️            |
| ID                                                                                               | ✔️          |               |
| Internal Comments                                                                                | ✔️          | ✔️            |
| Item Type                                                                                        | ✔️          |               |
| Name                                                                                             | ✔️          | ✔️            |
| Object Type                                                                                      | ✔️          |               |
| Phone                                                                                            | ✔️          | ✔️            |
| Potenial Liability                                                                               | ✔️          | ✔️            |
| Priority                                                                                         | ✔️          | ✔️            |
| Product                                                                                          | ✔️          | ✔️            |
| Single select                                                                                    | ✔️          | ✔️            |
| SLA Violation                                                                                    | ✔️          | ✔️            |
| Status                                                                                           | ✔️          | ✔️            |
| Subject                                                                                          | ✔️          | ✔️            |
| URL                                                                                              | ✔️          |               |

{% hint style="danger" %}
**Important Note:**\
We strive to maintain the accuracy of this list, but please be aware that supported fields may vary in the original product.
{% endhint %}

### Limitations to be Considered

At Getint, we continuously update our supported features, fields, and compatible apps. However, there are a few important limitations to keep in mind:

* When you add comments to an issue, they will be displayed under the user account you select to establish the connection. For smooth integration, it’s advisable to create a dedicated Service Account specifically for building your integration. Although the original author’s name will be visible in the comment footer, the comment itself will remain associated with the account that set up the connection.
* Unfortunately, incorporating the history of changes is not feasible at this time.

### Contacting Our Support Team

Our Support Team at Getint is eager to assist with your integration and migration needs and answer any other questions you may have. If you're seeking assistance or a deeper understanding of our solution, we invite you to schedule a demo call [here](https://www.getint.io/schedule-demo-call).

#### Case Studies

Large and small businesses have experienced the benefits of using Getint for their data integration needs. This has provided them with various solutions tailored to their teams and organizations. We invite you to explore some of our [Case Studies](https://www.getint.io/case-studies), which are true accounts of how Getint continually enhances and improves the tool integration process.

{% hint style="info" %}
**Are you looking for a specific solution that we don’t currently support?** Please get in touch with our [support team](https://getintio.atlassian.net/servicedesk/customer/portals), and we can assist you in developing a customized solution for your particular case.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>

# ServiceNow

## Getint: Simplifying ServiceNow Integration and Data Synchronization <a href="#getint-simplifying-servicenow-integration-and-data-synchronization" id="getint-simplifying-servicenow-integration-and-data-synchronization"></a>

Getint is expertly designed to seamlessly integrate and synchronize a wide range of tools. It supports various connectivity scenarios, including ServiceNow - Jira, ServiceNow - Asana, ServiceNow - Azure DevOps, and ServiceNow - Zendesk. Whether you choose the Software-as-a-Service (SaaS) or On-Premise solution, Getint offers the flexibility to meet diverse business requirements.

### Key Points Covered in the Article: <a href="#key-points-covered-in-the-article" id="key-points-covered-in-the-article"></a>

* [Setting Up the App](#how-to-setup-getint-for-servicenow)
* [Supported Fields in ServiceNow](#supported-fields-for-servicenow-integration)
* [Limitations and Considerations](#limitations-and-considerations)
* [Contacting Our Support Team - Case studies](#contacting-our-support-team)

Getint enables seamless data synchronization within the same platform, different platforms/different instances. It supports ServiceNow across different projects. This allows users to efficiently track and manage ServiceNow tasks/incidents in diverse environments as well as integrate ServiceNow with other platforms.

### How to Set Up Getint for ServiceNow <a href="#how-to-setup-getint-for-servicenow" id="how-to-setup-getint-for-servicenow"></a>

Getint simplifies data integration and migration. With easy setup steps, you can connect your systems, such as ServiceNow, map types (i.e., Task - Incident), and fields (i.e., Assignee - Assigned to). Whether you're looking to sync data continuously or perform a one-time migration, Getint has got you covered. Our dedicated support team is always ready to assist you with any challenges you may encounter during setup or operation.

For more detailed guides on how to set up your ServiceNow integration, please make sure to check the following:

* [Starting with Getint - Quickstart Guides](https://docs.getint.io/guides/quickstart)
* [Integration Guides](https://docs.getint.io/guides/integration-synchronization)
* [Migration Guides](https://docs.getint.io/guides/migration)
* [Understanding Getint - Workflows](https://docs.getint.io/getintio-platform/workflows)

Here's a simplified version of how to integrate ServiceNow with other tools (you can find a detailed overview [**here**](https://docs.getint.io/guides/integration-synchronization/jira-servicenow-integration)):

1. **Accessing Getint:**
   * If you're using Jira, find the app in the [Atlassian Marketplace](https://marketplace.atlassian.com/apps/1223935/servicenow-integration-for-jira-servicenow-connector?hosting=cloud\&tab=overview).
   * For non-Jira applications, choose between [Getint On-Premise or Getint SaaS](https://app.getint.io/).
2. **Establish a Connection with ServiceNow:**
   * Log in with the correct permissions.
   * Select ServiceNow as the app, create a new connection, and provide the instance URL and login credentials.
3. **Choose and Connect the Second App:**
   * Choose another tool (i.e., DevOps, Jira) to integrate with ServiceNow.
4. **Map Types and Fields:**
   * Link ServiceNow types (e.g., Incidents, Tasks) to synchronize with other tools.
   * Use the "Quick Build" feature or set mappings manually.

Getint's support team ensures a smooth integration experience customized to your needs. If you encounter challenges or need assistance, we're here to help!

### Supported Fields for ServiceNow Integration <a href="#supported-fields-for-servicenow-integration" id="supported-fields-for-servicenow-integration"></a>

Getint allows you to map fields between different platforms, and here's a list of our currently supported:

{% hint style="info" %}

#### **How Field Mappings Work:** <a href="#how-field-mappings-work" id="how-field-mappings-work"></a>

**One-Way Mapping:**

* When you update fields in one of the synced apps, those changes will appear in the other app. However, updates made in the other app won’t affect the first app because the fields are read-only.

**Two-Way Mapping:**

* Updates to synced fields will be reflected in both apps. If you modify a field in one app, the change will automatically sync to the other app as well.

**Tip:**

While technically it's not possible to directly modify read-only fields, we offer a solution to achieve bidirectional integration or migrate these fields using custom fields. Setting up this solution requires specific steps, but it is indeed possible. You can find more detailed information in this [article.](https://docs.getint.io/getting-started-with-the-platform/prepare-for-integration/understanding-the-difference-between-platforms-you-integrate)
{% endhint %}

| **ServiceNow Field**                                                                                      | **One Way** | **Both Ways** |
| --------------------------------------------------------------------------------------------------------- | ----------- | ------------- |
| Actual end                                                                                                | ✔️          | ✔️            |
| Actual start                                                                                              | ✔️          | ✔️            |
| Approval                                                                                                  | ✔️          | ✔️            |
| Approval set                                                                                              | ✔️          | ✔️            |
| Assigned to (Assignees)                                                                                   | ✔️          | ✔️            |
| Assignment group                                                                                          | ✔️          | ✔️            |
| Attachments                                                                                               | ✔️          | ✔️            |
| Business impact                                                                                           | ✔️          | ✔️            |
| Business resolve time                                                                                     | ✔️          |               |
| Caller                                                                                                    | ✔️          | ✔️            |
| Category                                                                                                  | ✔️          | ✔️            |
| Child Incidents                                                                                           | ✔️          | ✔️            |
| Close code                                                                                                | ✔️          | ✔️            |
| Close notes                                                                                               | ✔️          | ✔️            |
| Closed                                                                                                    | ✔️          | ✔️            |
| Closed by                                                                                                 | ✔️          | ✔️            |
| Configuration item                                                                                        | ✔️          | ✔️            |
| Contact type                                                                                              | ✔️          | ✔️            |
| Correlation display                                                                                       | ✔️          | ✔️            |
| Correlation ID                                                                                            | ✔️          | ✔️            |
| Created                                                                                                   | ✔️          |               |
| Created by                                                                                                | ✔️          | ✔️            |
| Comments                                                                                                  | ✔️          | ✔️            |
| <p>Custom fields</p><p><strong>Date - Dropdown fields - Text fields - Reference fields - URL</strong></p> | ✔️          | ✔️            |
| Description                                                                                               | ✔️          | ✔️            |
| Due date                                                                                                  | ✔️          | ✔️            |
| Effective number                                                                                          | ✔️          |               |
| Escalation                                                                                                | ✔️          |               |
| Expected start                                                                                            | ✔️          | ✔️            |
| Follow up                                                                                                 | ✔️          | ✔️            |
| Id                                                                                                        | ✔️          |               |
| Impact                                                                                                    | ✔️          | ✔️            |
| Incident state                                                                                            | ✔️          | ✔️            |
| Last reopened at                                                                                          | ✔️          |               |
| Last reopened by                                                                                          | ✔️          |               |
| Location                                                                                                  | ✔️          | ✔️            |
| Notify                                                                                                    | ✔️          | ✔️            |
| Number                                                                                                    | ✔️          | ✔️            |
| On hold reason                                                                                            | ✔️          | ✔️            |
| Opened                                                                                                    | ✔️          | ✔️            |
| Opened by                                                                                                 | ✔️          | ✔️            |
| Order                                                                                                     | ✔️          | ✔️            |
| Priority                                                                                                  | ✔️          | ✔️            |
| Probable cause                                                                                            | ✔️          | ✔️            |
| Reassignment count                                                                                        | ✔️          | ✔️            |
| Reopen count                                                                                              | ✔️          | ✔️            |
| Resolve time                                                                                              | ✔️          |               |
| Resolved                                                                                                  | ✔️          | ✔️            |
| Resolved by                                                                                               | ✔️          | ✔️            |
| Service                                                                                                   | ✔️          | ✔️            |
| Severity                                                                                                  | ✔️          | ✔️            |
| Short description                                                                                         | ✔️          | ✔️            |
| State (Status)                                                                                            | ✔️          | ✔️            |
| Subcategory                                                                                               | ✔️          | ✔️            |
| Subtasks                                                                                                  | ✔️          | ✔️            |
| Task type                                                                                                 | ✔️          | ✔️            |
| Transfer reason                                                                                           | ✔️          |               |
| Updated                                                                                                   | ✔️          |               |
| Updated by                                                                                                | ✔️          | ✔️            |
| Updates                                                                                                   | ✔️          | ✔️            |
| Upon approval                                                                                             | ✔️          | ✔️            |
| Upon reject                                                                                               | ✔️          | ✔️            |
| Urgency                                                                                                   | ✔️          | ✔️            |
| URL                                                                                                       | ✔️          |               |

{% hint style="danger" %}
**Important Note:**\
We strive to maintain the accuracy of this list, but please be aware that supported fields may vary in the original product.
{% endhint %}

### Limitations and Considerations

At Getint, we continuously update our supported features, fields, and compatible apps. However, there are a few important points to consider:

* **Issue Types:** When Getint creates a new issue in ServiceNow, it will always be one specific type (e.g., Task or Incident). You can set the default item type using a rule or manually adjust it in ServiceNow after creation.
* **Comments:** Comments added by Getint will appear under the user account you choose during connection setup. Consider creating a dedicated Service Account for integration to maintain consistency. The original author's name will appear in the comment footer, but the comment will be assigned to the connecting account.
* **Change History:** Unfortunately, Getint cannot integrate the history of changes.
* **Private Tasks:** While Getint allows the creation of private tasks in ServiceNow, setting them up on boards is not supported.

### Contacting Our Support Team

Our dedicated Support Team is ready to assist with your integration and migration needs. If you have questions or need deeper insights into our solution, feel free to schedule a [demo call](https://www.getint.io/schedule-demo-call) with us.

#### Case Studies

Explore real-world examples of how Getint enhances tool integration for businesses of all sizes. Our [Case Studies](https://www.getint.io/case-studies) showcase tailored solutions that empower teams and organizations.

{% hint style="info" %}
**Are you looking for a specific solution that we don’t currently support?** Please get in touch with our [support team](https://getint.io/help-center), and we can assist you in developing a customized solution for your particular case.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>

# Trello

## Getint: Simplifying Trello Integration and Data Synchronization <a href="#getint-simplifying-trello-integration-and-data-synchronization" id="getint-simplifying-trello-integration-and-data-synchronization"></a>

Getint connects and synchronizes multiple tools, allowing teams to create seamless integrations between platforms such as Trello, Jira, Asana, and Azure DevOps. Available as both a Cloud and an on-premise solution, Getint provides the flexibility to support a wide range of business needs and deployment preferences.

### Key Topics Covered: <a href="#key-topics-covered" id="key-topics-covered"></a>

* [App Setup](#app-setup)
* [Supported Trello Fields](#supported-trello-fields)
* [Limitations and Important Notes](#limitations-and-important-notes)
* [Contacting Our Support Team](#contacting-our-support-team)

Getint enables data synchronization across platforms and instances, including Trello. This allows users to track, manage, and update tasks across multiple projects while keeping Trello aligned with other tools in their ecosystem.

### App Setup <a href="#app-setup" id="app-setup"></a>

Getint simplifies the process of connecting systems and synchronizing or migrating data between them. Follow the steps below to start integrating Trello with your preferred tools.

**Step 1: Access Getint**

* **For Jira users:** If you are integrating Jira with Trello, install the Getint app directly from the [Atlassian Marketplace](https://marketplace.atlassian.com/apps/1231790/integration-for-jira-and-trello-2-way-integration?hosting=cloud\&tab=overview).
* **For other platforms:** Select either the browser version ([app.getint.io](http://app.getint.io/)) or On-Premise version of Getint based on your organizational requirements.

**Step 2: Set Up a Connection with Trello**

* Ensure you have the necessary [access permissions](https://docs.getint.io/guides/quickstart/connection#trello) in Trello.
* Select **Trello** as the application.
* Create a new connection and enter your Trello credentials.

**Step 3: Connect to Another Tool**

* Choose the platform you want to integrate with Trello, such as **Jira** or **Azure DevOps**.

**Step 4: Map Types and Fields**

* Match Trello types and fields with their corresponding entities in the other tool.
* Use the **Quick Build** option for automatic mapping, or define mappings manually to better align with your workflows.

Our support team is always available to help with setup or operational questions.

For additional guidance on using Getint with Trello, refer to:

* [Quickstart Guides](https://docs.getint.io/guides/quickstart)
* [Jira Trello Integration Guide](https://docs.getint.io/guides/integration-synchronization/jira-trello-integration)
* [Migration Guides](https://docs.getint.io/guides/migration)

### Supported Trello Fields <a href="#supported-trello-fields" id="supported-trello-fields"></a>

Getint enables field mapping between Trello and other platforms. Below is an overview of the currently supported field-mapping options and their functionality.

{% hint style="info" %}

#### **How Field Mappings Work:** <a href="#how-field-mappings-work" id="how-field-mappings-work"></a>

**One-Way Mapping:**

* When you update fields in one of the synced apps, those changes will appear in the other app. However, updates made in the other app won’t affect the first app because the fields are read-only.

**Two-Way Mapping:**

* Updates to synced fields will be reflected in both apps. If you modify a field in one app, the change will automatically sync to the other app as well.

**Tip:**

While technically it's not possible to directly modify read-only fields, we offer a solution to achieve bidirectional integration or migrate these fields using custom fields. Setting up this solution requires specific steps, but it is indeed possible. For more detailed information, please refer to this [article.](https://docs.getint.io/getting-started-with-the-platform/prepare-for-integration/understanding-the-difference-between-platforms-you-integrate)
{% endhint %}

| **Trello Field** | **One Way**                                                                                                                                                                          | **Both Ways**                                                                                                                                                                        |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Attachments      | <img src="https://pf-emoji-service--cdn.us-east-1.prod.public.atl-paas.net/standard/ef8b0642-7523-4e13-9fd3-01b65648acf6/64x64/2716.png" alt="multiplication sign" data-size="line"> | <img src="https://pf-emoji-service--cdn.us-east-1.prod.public.atl-paas.net/standard/ef8b0642-7523-4e13-9fd3-01b65648acf6/64x64/2716.png" alt="multiplication sign" data-size="line"> |
| Comments         | ✔️                                                                                                                                                                                   | ✔️                                                                                                                                                                                   |
| Custom Fields    | <img src="https://pf-emoji-service--cdn.us-east-1.prod.public.atl-paas.net/standard/ef8b0642-7523-4e13-9fd3-01b65648acf6/64x64/2716.png" alt="multiplication sign" data-size="line"> | <img src="https://pf-emoji-service--cdn.us-east-1.prod.public.atl-paas.net/standard/ef8b0642-7523-4e13-9fd3-01b65648acf6/64x64/2716.png" alt="multiplication sign" data-size="line"> |
| Description      | ✔️                                                                                                                                                                                   | ✔️                                                                                                                                                                                   |
| Id               | ✔️                                                                                                                                                                                   |                                                                                                                                                                                      |
| Item Type        | ✔️                                                                                                                                                                                   |                                                                                                                                                                                      |
| List             | ✔️                                                                                                                                                                                   | ✔️                                                                                                                                                                                   |
| Status           | ✔️                                                                                                                                                                                   | ✔️                                                                                                                                                                                   |
| Title            | ✔️                                                                                                                                                                                   | ✔️                                                                                                                                                                                   |
| URL              | ✔️                                                                                                                                                                                   |                                                                                                                                                                                      |

{% hint style="warning" %}
**Important Note:**\
We strive to maintain the accuracy of this list, but please be aware that supported fields may vary in the original product.
{% endhint %}

### Limitations and Important Notes <a href="#limitations-and-important-notes" id="limitations-and-important-notes"></a>

At Getint, we continuously update our supported features, fields, and compatible apps. However, there are a few important points to consider:

* **Attachments**: Syncing attachments isn’t supported.
* **Change History**: Unfortunately, Getint cannot integrate the history of changes.
* **Comments**: Comments added by Getint will appear under the user account you choose during connection setup. Consider creating a dedicated Service Account for integration to maintain consistency. The original author’s name will appear in the comment footer, but the comment will be assigned to the connecting account.
* **Custom Fields**: Aren’t supported for this integration.
* **Issue Types**: Currently, the integration supports Trello Cards as the only issue type.
* **Multi-project support**: Many-to-many project synchronization between Jira and Trello is not supported.
* **Text Formatting Errors**: Formatting is not fully preserved during synchronization; bullet points may not convert correctly in Jira.

### Contacting Our Support Team <a href="#contacting-our-support-team" id="contacting-our-support-team"></a>

Our dedicated Support Team is ready to assist with your integration and migration needs. If you have questions or need deeper insights into our solution, feel free to schedule a [demo call](https://www.getint.io/schedule-demo-call) with us.

#### Case Studies <a href="#case-studies" id="case-studies"></a>

Explore real-world examples of how Getint enhances tool integration for businesses of all sizes. Our [Case Studies](https://www.getint.io/case-studies) showcase tailored solutions that empower teams and organizations.

{% hint style="info" %}
**Are you looking for a specific solution that we don’t currently support?** Please get in touch with our [support team](https://getint.io/help-center), and we can assist you in developing a customized solution for your particular case.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>

# Wrike

## Getint: Simplifying Wrike Integration and Data Synchronization <a href="#getint-simplifying-wrike-integration-and-data-synchronization" id="getint-simplifying-wrike-integration-and-data-synchronization"></a>

Getint connects and synchronizes multiple tools, allowing teams to create seamless integrations between platforms such as Wrike, Jira, Asana, and Azure DevOps. Available as both a Cloud and an on-premise solution, Getint provides the flexibility to support a wide range of business needs and deployment preferences.

### Key Topics Covered: <a href="#key-topics-covered" id="key-topics-covered"></a>

* [App Setup](#app-setup)
* [Supported Wrike Fields](#supported-wrike-fields)
* [Limitations and Important Notes](#limitations-and-important-notes)
* [Support Resources and Case Studies](#contacting-our-support-team)

Getint enables data synchronization across platforms and instances, including Wrike. This allows users to track, manage, and update tasks across multiple projects while keeping Wrike aligned with other tools in their ecosystem.

### App Setup <a href="#app-setup" id="app-setup"></a>

Getint simplifies the process of connecting systems and synchronizing or migrating data between them. Follow the steps below to start integrating Wrike with your preferred tools.

**Step 1: Access Getint**

* **For Jira users:** If you are integrating Jira with Wrike, install the Getint app directly from the [Atlassian Marketplace](https://marketplace.atlassian.com/apps/1223936/wrike-integration-for-jira-wrike-connector?hosting=cloud\&tab=overview).
* **For other platforms:** Select either the browser version ([app.getint.io](http://app.getint.io/)) or On-Premise version of Getint based on your organizational requirements.

**Step 2: Set Up a Connection with Wrike**

* Ensure you have the necessary [access permissions](https://docs.getint.io/guides/quickstart/connection#wrike) in Wrike.
* Select **Wrike** as the application.
* Create a new connection and enter your Wrike credentials.

**Step 3: Connect to Another Tool**

* Choose the platform you want to integrate with Wrike, such as **Jira** or **Azure DevOps**.

**Step 4: Map Types and Fields**

* Match Wrike types and fields with their corresponding entities in the other tool.
* Use the **Quick Build** option for automatic mapping, or define mappings manually to better align with your workflows.

Our support team is always available to help with setup or operational questions.

For additional guidance on using Getint with Wrike, refer to:

* [Quickstart Guides](https://docs.getint.io/guides/quickstart)
* [Jira Wrike Integration Guide](https://docs.getint.io/guides/integration-synchronization/jira-wrike-integration)
* [Migration Guides](https://docs.getint.io/guides/migration)

### Supported Wrike Fields <a href="#supported-wrike-fields" id="supported-wrike-fields"></a>

Getint enables field mapping between Wrike and other platforms. Below is an overview of the currently supported field-mapping options and their functionality.

{% hint style="info" %}

#### **How Field Mappings Work:** <a href="#how-field-mappings-work" id="how-field-mappings-work"></a>

**One-Way Mapping:**

* When you update fields in one of the synced apps, those changes will appear in the other app. However, updates made in the other app won’t affect the first app because the fields are read-only.

**Two-Way Mapping:**

* Updates to synced fields will be reflected in both apps. If you modify a field in one app, the change will automatically sync to the other app as well.

**Tip:**

While technically it's not possible to directly modify read-only fields, we offer a solution to achieve bidirectional integration or migrate these fields using custom fields. Setting up this solution requires specific steps, but it is indeed possible. For more detailed information, please refer to this [article.](https://docs.getint.io/getting-started-with-the-platform/prepare-for-integration/understanding-the-difference-between-platforms-you-integrate)
{% endhint %}

| **Wrike Field**                                                          | **One Way** | **Both Ways** |
| ------------------------------------------------------------------------ | ----------- | ------------- |
| Assignee                                                                 | ✔️          | ✔️            |
| Comments & Attachments                                                   | ✔️          | ✔️            |
| Custom Fields                   **Date - Number - Single Select - Text** | ✔️          | ✔️            |
| Description                                                              | ✔️          | ✔️            |
| Due Date                                                                 | ✔️          | ✔️            |
| Id                                                                       | ✔️          |               |
| Is Milestone                                                             | ✔️          |               |
| Start Date                                                               | ✔️          | ✔️            |
| Status                                                                   | ✔️          | ✔️            |
| Title                                                                    | ✔️          | ✔️            |
| URL                                                                      | ✔️          |               |

{% hint style="warning" %}
**Important Note:**\
We strive to maintain the accuracy of this list, but please be aware that supported fields may vary in the original product.
{% endhint %}

### Limitations and Important Notes <a href="#limitations-and-important-notes" id="limitations-and-important-notes"></a>

At Getint, we continuously update our supported features, fields, and compatible apps. However, there are a few important points to consider:

* **Change History**: Unfortunately, Getint cannot integrate the history of changes.
* **Comments**: Comments added by Getint will appear under the user account you choose during connection setup. Consider creating a dedicated Service Account for integration to maintain consistency. The original author’s name will appear in the comment footer, but the comment will be assigned to the connecting account.
* **Multi-project support**: Many-to-many project synchronization between Jira and Wrike is not supported.
* **Sub-tasks**: Currently, syncing sub-tasks is not supported.
* **Text Formatting Errors**: Formatting is not fully preserved during synchronization. For example, bullet points may not convert correctly in Jira.

### Contacting Our Support Team <a href="#contacting-our-support-team" id="contacting-our-support-team"></a>

Our dedicated Support Team is ready to assist with your integration and migration needs. If you have questions or need deeper insights into our solution, feel free to schedule a [demo call](https://www.getint.io/schedule-demo-call) with us.

#### Case Studies <a href="#case-studies" id="case-studies"></a>

Explore real-world examples of how Getint enhances tool integration for businesses of all sizes. Our [Case Studies](https://www.getint.io/case-studies) showcase tailored solutions that empower teams and organizations.

{% hint style="info" %}
**Are you looking for a specific solution that we don’t currently support?** Please get in touch with our [support team](https://getint.io/help-center), and we can assist you in developing a customized solution for your particular case.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>

# Zendesk

## Getint: Simplifying Zendesk Integration and Data Synchronization <a href="#getint-simplifying-zendesk-integration-and-data-synchronization" id="getint-simplifying-zendesk-integration-and-data-synchronization"></a>

**Getint** connects and synchronizes various tools, enabling integrations between Zendesk and platforms like Jira, Asana, or Azure DevOps. It offers both SaaS and On-Premise solutions, allowing businesses to choose the deployment option that best fits their needs.

### Key Topics Covered: <a href="#key-topics-covered" id="key-topics-covered"></a>

* [Setting Up the App](#how-to-set-up-getint-for-zendesk)
* [Supported Fields in Zendesk](#supported-fields-for-zendesk-integration)
* [Limitations and Considerations](#limitations-and-considerations)
* [Contacting Support - Case Studies](#contacting-our-support-team)

Getint synchronizes data across platforms and instances, including Zendesk. It allows users to track and manage tasks or activities across projects while connecting Zendesk with other tools for improved coordination.

### How to Set Up Getint for Zendesk <a href="#how-to-set-up-getint-for-zendesk" id="how-to-set-up-getint-for-zendesk"></a>

Getint simplifies connecting and migrating data between systems. Below are the steps to get started:

**Step 1: Access Getint**

* For Jira users: If you want to integrate Jira with Zendesk, download the app from the Atlassian Marketplace [here](https://marketplace.atlassian.com/apps/1223934/zendesk-integration-for-jira-2-way-zendesk-connector?hosting=cloud\&tab=overview).
* For other tools: Select between Getint On-Premise or SaaS options.

**Step 2: Set Up a Connection with Zendesk**

* Ensure you have the correct [access permissions](https://docs.getint.io/guides/quickstart/connection#zendesk).
* Choose Zendesk as the app, create a new connection, and enter your Zendesk credentials.

**Step 3: Connect to Another Tool**

* Pick the platform you want to integrate with Zendesk, such as Jira.

**Step 4: Map Types and Fields**

* Match Zendesk categories with their counterparts in the other tool.
* Use the **Quick Build** feature for automatic mapping or customize mappings manually if needed.

Our support team is always available to assist with any setup or operational challenges.

For additional guidance on using Getint with Zendesk, refer to:

* [Quickstart Guides](https://docs.getint.io/guides/quickstart)
* [Jira Zendesk Integration Guide](https://docs.getint.io/guides/integration-synchronization/jira-zendesk-integration)
* [Migration Guides](https://docs.getint.io/guides/migration)

### Supported Fields for Zendesk Integration <a href="#supported-fields-for-zendesk-integration" id="supported-fields-for-zendesk-integration"></a>

Getint allows you to map fields between different platforms, and here's a list of our currently supported:

{% hint style="info" %}

#### **How Field Mappings Work:** <a href="#how-field-mappings-work" id="how-field-mappings-work"></a>

**One-Way Mapping:**

* When you update fields in one of the synced apps, those changes will appear in the other app. However, updates made in the other app won’t affect the first app because the fields are read-only.

**Two-Way Mapping:**

* Updates to synced fields will be reflected in both apps. If you modify a field in one app, the change will automatically sync to the other app as well.

**Tip:**

While technically it's not possible to directly modify read-only fields, we offer a solution to achieve bidirectional integration or migrate these fields using custom fields. Setting up this solution requires additional steps, but it is indeed possible. You can find more detailed information in this [article.](https://docs.getint.io/getting-started-with-the-platform/prepare-for-integration/understanding-the-difference-between-platforms-you-integrate)
{% endhint %}

| **Zendesk Field**                                                                 | **One Way** | **Both Ways** |
| --------------------------------------------------------------------------------- | ----------- | ------------- |
| Assignee                                                                          | ✔️          | ✔️            |
| Brand                                                                             | ✔️          | ✔️            |
| Comments & Attachments                                                            | ✔️          | ✔️            |
| <p>Custom Fields:</p><p><strong>Date - Dropdown - Multi-Line - Text</strong> </p> | ✔️          | ✔️            |
| Description                                                                       | ✔️          | ✔️            |
| Group                                                                             | ✔️          | ✔️            |
| ID                                                                                | ✔️          |               |
| IS Side Conversation                                                              | ✔️          |               |
| Priority                                                                          | ✔️          | ✔️            |
| Recipient                                                                         | ✔️          | ✔️            |
| Requester email (on-create only)                                                  | ✔️          |               |
| Requester name (on-create only)                                                   | ✔️          |               |
| Status                                                                            | ✔️          | ✔️            |
| Tags (Labels)                                                                     | ✔️          |               |
| Ticket form                                                                       | ✔️          | ✔️            |
| Ticket form ID                                                                    | ✔️          | ✔️            |
| Title (Subject)                                                                   | ✔️          | ✔️            |
| Topic                                                                             | ✔️          | ✔️            |
| Type                                                                              | ✔️          | ✔️            |
| URL                                                                               | ✔️          |               |

{% hint style="warning" %}
**Important Note:**\
We strive to maintain the accuracy of this list, but please be aware that supported fields may vary in the original product.
{% endhint %}

### Limitations and Considerations <a href="#limitations-and-considerations" id="limitations-and-considerations"></a>

At Getint, we continuously update our supported features, fields, and compatible apps. However, there are a few important points to consider:

* **Issue Types**: When Getint creates a new issue in Zendesk, it will always be one specific type (Ticket).
* **Comments**: Comments added by Getint will appear under the user account you choose during connection setup. Consider creating a dedicated Service Account for integration to maintain consistency. The original author's name will appear in the comment footer, but the comment will be assigned to the connecting account.

Comments and attachments transferred from Zendesk to Jira can be set to either public, private, or skipped completely. You can configure your integration to enable both public and private visibility options simultaneously.

* **Change History**: Unfortunately, Getint cannot integrate the history of changes.
* **Inline** **Images** aren’t supported for the Description field.
* **On-create Only Fields**: These fields will only trigger when a new ticket is created in Zendesk. This means that if you add this field to your integration later or if you update an existing issue in Jira, it won’t be possible to retrieve the information from these fields.
* **Ticket Synchronization**: Keep in mind that when you start a new integration, all existing tickets in Zendesk will begin syncing with the connected tool, one by one. If you disable your previous integration and set up a new one, the syncing process will restart automatically, which may result in duplicate tickets.

### Contacting Our Support Team <a href="#contacting-our-support-team" id="contacting-our-support-team"></a>

Our dedicated Support Team is ready to assist with your integration and migration needs. If you have questions or need deeper insights into our solution, feel free to schedule a [demo call](https://www.getint.io/schedule-demo-call) with us.

#### Case Studies <a href="#case-studies" id="case-studies"></a>

Explore real-world examples of how Getint enhances tool integration for businesses of all sizes. Our [Case Studies](https://www.getint.io/case-studies) showcase tailored solutions that empower teams and organizations.

{% hint style="info" %}
**Are you looking for a specific solution that we don’t currently support?** Please get in touch with our [support team](https://getint.io/help-center), and we can assist you in developing a customized solution for your particular case.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>

# Quickstart

Streamline your workflow with Getint's easy-to-use integration platform. Connect your tools in minutes. Scale from basic tasks to advanced features effortlessly. Start with our free trial

Welcome to Getint, where simplicity meets power! Our goal is to make your first integration not just possible but enjoyable in minutes, whether you're handling straightforward tasks or diving into complex cases. Forget the hassle of installing multiple apps or choosing between an intuitive UI and complex scripting. Getint combines the best of both worlds: a single, user-friendly UI for all your integration needs, with the power of scripting at your fingertips for those unique challenges. To start your free trial, follow the instructions provided in the [Getint documentation](https://docs.getint.io/getting-started-with-the-platform/starting-the-free-trial-and-accessing-the-getint-app).

Feel free to explore the platform and experience the benefits of Getint!

### **Why Choose Getint?**

* **One UI to Rule Them All**: Manage all your connectors from a single interface. No separate installations, no toggling between modes—just seamless integration.
* **Flexibility and Power**: Start with the basics, then effortlessly scale to more advanced features like custom fields, sync directions, filtering, and handling comments, all tailored to your needs.
* **Simplified Setup**: From your very first task integration to syncing attachments and status mapping, see immediate results and scale your setup as needed.

Before diving in, prepare for your integration journey by reviewing our [preparation guide](https://docs.getint.io/getting-started-with-the-platform/prepare-for-integration) and claiming your free trial instance, available via the Atlassian Marketplace or directly through Getint SaaS or Getint OnPremise options.

### Iteration 1: Establishing a Basic Integration MVP

#### Step-by-Step Setup

1. **Initiate Your Integration**:
   * Click "**Create Integration"**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FgTUZUxhtbdXnPrQiPUIZ%2Ffirst%20workflow%20screen%20qucikstart.png?alt=media&#x26;token=99d60ac9-8ff3-4b80-9996-00236e7cca14" alt=""><figcaption></figcaption></figure>

* Choose **Continuous sync** and learn about integration vs. migration [here](https://chat.openai.com/c/8fae8437-be08-44b9-b71b-1d51c3815ddd).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FVTGfwx9DEp63YZNwY0bZ%2Fquickstart%20contin%20sync.png?alt=media&#x26;token=9e8211b6-348b-4004-a7e8-4d9779f18134" alt=""><figcaption></figcaption></figure>

1. **Connect Your First Application (Example: Jira)**:

* Select **Connect App**, choose Jira, and click **Create New Connection**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FWPMt3DlF235dF97eTu84%2Fquickstart_1app_1.png?alt=media&#x26;token=3f279819-0315-449e-9325-9d72580c76e8" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FIrUUbzFInakzSJPpQVgE%2Fquickstart_select_Jira.png?alt=media&#x26;token=309cf168-942e-414b-ade5-a9b1a3d8f483" alt=""><figcaption></figcaption></figure>

* Enter the URL of your Jira instance (e.g., `https://demogetintio.atlassian.net/`).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FPTkpvltDTANDHuQdxGP4%2Fquickstart%20instance%20url.png?alt=media&#x26;token=ed635a2d-a3ab-4551-b0b0-3c6a92d45142" alt=""><figcaption></figcaption></figure>

* Name your connection, Provide the email and Personal Access Token for the admin service account.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fhp0j8imS22rByW00vZNg%2Fquickstart%20connect%20app.png?alt=media&#x26;token=58fc25f8-3e8c-40f2-9ea0-b547a78bf7b1" alt=""><figcaption></figcaption></figure>

* Select your newly created connection, choose a test project, and click **Connect.**

1. **Repeat for the Second Application (Example: Azure DevOps)**: Follow the steps above to establish a connection with your second application.
2. **Type Mapping**: Map a Task in Jira to a Task in Azure DevOps. Provide a name for your integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FBUhiXctRPVFPBNXDpXIK%2Ftype_mapping_quickstart.png?alt=media&#x26;token=30af9c16-e2b1-466a-9b67-9aeee74112d8" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMyC0pFb0pW9P1sv7Jer5%2Fqucik%20start%20task%20task.png?alt=media&#x26;token=a1fa97b1-134a-486b-8bfb-61d81ad972a9" alt=""><figcaption></figcaption></figure>

1. **Finalize**: Click **Create**. Your integration is now live!

**Test Your Integration**: Create a task in Jira with a title and description. It should appear in Azure DevOps (or an app of your choice) shortly.

### Iteration 2: Enhancing Integration with Fields, Statuses, and Comments

1. **Refine Your Integration**: Return to **Workflows**, select your integration, and access the previously created Type Mapping.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Flxh79r1zlKWUAKLjt8Mc%2Fqucik_start_task_task_to_field.png?alt=media&#x26;token=f50e4da9-ac89-4a6f-ab53-cc89e8196a3e" alt=""><figcaption></figcaption></figure>

1. **Field Mapping**:&#x20;
   * Map fields between apps, e.g., Jira's **Assignee** to Azure DevOps's **Assigned to**. Adjust mappings for dropdown fields as necessary.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FbrMzX4fHOWqtI789zInj%2FField%20mapping%201.png?alt=media&#x26;token=de5e323b-b3ee-4570-b829-23cc6c11d128" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FnIFQxOVEynTA13hGG1um%2FField%20mapping%202.png?alt=media&#x26;token=4fdec8c6-1e24-4197-b66d-2f09220f5b1c" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FJjp03B2IG9V32VdXneUH%2FField%20mapping%203.png?alt=media&#x26;token=9a0ceb2d-639b-4d3e-94cf-256067cd7a3e" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Frgf3EZ8Md7k1CmLHN9Wp%2FField%20mapping%204.png?alt=media&#x26;token=4d65dd9f-5765-4c0c-9ae2-fa2dd23cd90f" alt=""><figcaption></figcaption></figure>

1. **Status Mapping**: Customize your status mappings to fit your workflow.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FoaaG8xmffobnFvZPbIl8%2Fquickstart%20statuses%201.png?alt=media&#x26;token=d0ad0f91-2578-4891-b393-5a632cff9251" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F6m2gbfA49aAXSs1IKXDe%2Fquickstart%20statuses%202.png?alt=media&#x26;token=f92a7687-10a3-436e-bc08-dfa00e050dea" alt=""><figcaption></figcaption></figure>

1. **Comments and Attachments**: Enable attachment sync and apply your settings.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Ft19fGWTAwkizKgAZbwBQ%2Fqucistart_attachments.png?alt=media&#x26;token=db6030ca-ca41-4b66-8f71-845ae18e293d" alt=""><figcaption></figcaption></figure>

1. **Save Your Progress**: Don’t forget to save your integration changes.

**Test Enhancements**: Update your test task with comments, attachments, assignees, and status changes to see the reflection in both systems.

### Iteration 3: Monitoring Your Integration

1. **Access Reporting**: Upon opening the first tab, you'll be presented with a comprehensive table listing all **Performed Syncs** along with their respective statuses. This provides a quick snapshot of your integration activity.
2. **Detailed Sync Analysis**:

* **Sync ID**: For a deeper dive into a specific sync, click on its **ID** (e.g., #139010). This action opens a detailed view of the sync, offering insights into its execution.
* **Trigger Source**: By selecting **Triggered by** (e.g., AM-3235), you can review the task that initiated the sync. A clickable URL facilitates direct access to the triggering task, enabling easy review and analysis.
* **Sync Outcome**: Clicking on **Synced with** (e.g., AM-3235) reveals the task resulting from the sync, complete with a direct URL for quick access. This feature allows you to evaluate the sync's effectiveness and outcome clarity.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FczlaRRHZMyaEqgqZL4zn%2Fquickstart_reporting.png?alt=media&#x26;token=f9fee898-ed51-4ce9-9507-066e34f5fae3" alt=""><figcaption></figcaption></figure>

1. **Troubleshoot**: The **Mode** section is your go-to for assessing the sync's success. A successful sync indicates everything is functioning as expected. Conversely, should you encounter any issues, this section will guide you to identify errors. Should an error be detected, revisit step 1 for troubleshooting. To facilitate resolution, copy the error details and submit a support ticket for assistance.

### Always Here to Help

Encounter a snag? Reach out at any stage of your integration journey. Click the chat icon, schedule a [free onboarding demo call](https://www.getint.io/schedule-demo-call), or [open a support ticket.](https://getintio.atlassian.net/servicedesk/) We're here to ensure your integration success with Getint.

<br>

# Access Tokens & Requirements

Connecting various applications within your organization is pivotal for fostering seamless collaboration and optimizing workflow efficiency. Getint offers a user-friendly platform made to simplify the integration process between diverse applications like Jira, ServiceNow, Azure DevOps, and Asana. This comprehensive guide will walk you through each step to establish robust connections effortlessly, ensuring smooth operations and enhanced productivity across your organization. Let's dive in!

### User Account Requirements <a href="#user-account-requirements" id="user-account-requirements"></a>

To initiate the integration process, you'll need user accounts in both systems you plan to integrate. We highly recommend using a dedicated service account with administrative privileges. This ensures all integration functions can execute smoothly, enabling Getint to perform a wide range of actions effectively. While administrative access is preferred, the essential requirement is that the user account possesses the necessary permissions to create, update, and manage projects, types, and fields within the applications.

### Role of the Service Account <a href="#role-of-the-service-account" id="role-of-the-service-account"></a>

The Service Account plays a pivotal role in facilitating integration operations. Here's what it entails:

* Getint operates under the Service Account to execute various actions, including task creation and updates across integrated platforms.
* Comments generated by Getint will be attributed to the Service Account, with clear indications of the original author in the comment footer. This practice fosters transparency and preserves context in communication threads

### Providing Connection Details <a href="#providing-connection-details" id="providing-connection-details"></a>

To kickstart the integration process, specific details are required:

* **URL of the Instance**: This refers to the web address where your application, such as Jira or ServiceNow, is hosted.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F32NKKqWecWXG4amAFpCX%2FConnection%20URL.png?alt=media&#x26;token=710da9b3-e547-446c-af15-fc0690421050" alt=""><figcaption></figcaption></figure>

* **Username**: Enter the username associated with the Service Account in the application.
* **Password/Token**: Depending on the application, you may need to provide either a password or an API token for authentication.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F56PZ8ze17LQV5ZUxxMYc%2FProvide%20the%20details%20of%20your%20connection.png?alt=media&#x26;token=fea4c0f7-de00-4704-b0fb-744accbea608" alt=""><figcaption></figcaption></figure>

By providing these details, Getint seamlessly connects your applications, mediating between two entities that would otherwise operate independently. It ensures smooth communication and data exchange, enabling your team to collaborate effectively across platforms and enhance productivity.

*Now, let's connect with each application, generating its tokens:*

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F867JS2ZcWq8soMHClJmv%2FGetint%20White%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=56f3eb60-1357-4889-af99-bf49ba50a3c1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Jumpstart your Getint experience! Schedule a demo with one of our Integration Experts now!</a></p></figcaption></figure>

### **Jira** <a href="#jira" id="jira"></a>

Jira offers integration options for Cloud, Server, and Data Center. Depending on your choice, the method for generating a Personal Access Token varies.

#### **Jira Cloud - API Token (Unscoped)**

It is required to use a Personal Access Token for integration:

* Log in to your Atlassian account and visit Atlassian Account Settings.
* Go to Security and select "Personal API Token."
* Click on "Create API token" and provide a label for your token to identify it.
* Click "Create" to generate the token.
* Copy the token and ensure it is stored securely in a safe location.

This API token will work as the authentication mechanism for connecting Jira Cloud with Getint, enabling seamless integration and data synchronization between the two platforms.

{% embed url="<https://youtu.be/K5jRfZVKLOo>" %}

#### **Forge Apps/Onpremise - Scoped Tokens**

While standard API tokens grant the full permissions of the associated user, **Scoped Tokens** allow you to limit what an application can see and do.

{% hint style="warning" %}
Scoped tokens are currently only available for **Forge apps** and **Jira On-Premise (self-hosted)** environments. They are **not** available for standard Jira Cloud service accounts or Jira Data Center deployments.
{% endhint %}

* Go to your profile, then **Account settings** > **Security** > **Create and manage API tokens**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F2sXbXlnd8pIYcHGaIySS%2FCreating%20an%20scoped%20API%20token.png?alt=media&#x26;token=d876b2b1-0479-4814-8de2-f348b1068877" alt=""><figcaption></figcaption></figure>

* Click **Create API token with scopes**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fas5kyHE3MTnyT3FSooi0%2FCreate%20API%20token%20with%20scopes.png?alt=media&#x26;token=8dbe5314-3e49-4e30-a587-9c45f456e429" alt=""><figcaption></figcaption></figure>

* Set the token name and expiry date. Then, select Jira as the app and choose the relevant scopes.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FWtR8EhKfM4UL0svK91no%2FSelecting%20the%20API%20token%20scopes.png?alt=media&#x26;token=3fd6ffed-e2d2-4739-9777-356c9c60f9b0" alt=""><figcaption></figcaption></figure>

* Next, depending on your company's security requirements, you can select either classic or granular scopes. The necessary permissions for each of them go as follows:

1. **Classic Scopes:**

   * **Manage**

   `manage:jira-configuration`

   `manage:jira-data-provider`

   `manage:jira-project`

   `manage:jira-webhook`

   * **Read**

   `read:account`

   `read:jira-user`

   `read:me`

   `read:jira-work`

   * **Write**

   `write:jira-work`

   `write:servicedesk-request`
2. **Granular Scopes:**
   * **Read**

     `read:issue:jira`

     `read:issue-meta:jira`

     `read:issue.transition:jira`

     `read:comment:jira`

     `read:attachment:jira`

     `read:issue.property:jira`

     `read:issue-link-type:jira`

     `read:project:jira`

     `read:project-version:jira`

     `read:field:jira`

     `read:user:jira`

     `read:board-scope:jira-software`

     `read:sprint:jira-software`

     `read:servicedesk:jira-service-management`

     `read:jira-work`

     `read:jira-user`
   * **Write**

     `write:issue:jira`

     `write:comment:jira`

     `write:attachment:jira`

     `write:issue.property:jira`

     `write:issue-link:jira`

     `write:project-version:jira`

     `write:board-scope:jira-software`

     `write:sprint:jira-software`

     `write:jira-work`
   * **Delete**

     `delete:comment:jira`

     `delete:attachment:jira`

     `delete:issue-link:jira`
   * **Manage**

     `read:servicedesk:jira-service-management`

     `manage:jira-configuration`

     `manage:jira-project`

     `manage:jira-data-provider`

* After generating your access token, copy it and store it safely.

#### **Jira Cloud - OAuth**

To add another layer of security and to meet certain tools' requirements (i.e., GitHub, GitLab, Azure DevOps), you can set up a connection with Jira OAuth. You will need your OAuth credentials as well as your Email and Personal Access Token.

* Go to **https\://(yourinstancename).atlassian.net/secure/admin/oauth-credentials.** Click "OAuth credentials" and then "Create credentials."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FeDLyiOYFSjqj3CxraM6S%2FCreate%20OAuth%20credentials.png?alt=media&#x26;token=49bd8f15-70b2-44c6-9795-f1fab25c8d25" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Ensure you have admin permissions in your Jira instance; otherwise, you won't be able to generate an OAuth token.
{% endhint %}

* Establish the parameters for your OAuth. You can find more information regarding each permission [here.](https://support.atlassian.com/jira-software-cloud/docs/allow-oauth-access/)
* When setting up OAuth credentials for integrations, the server base URL doesn't impact the validity of the credentials (client ID and secret key). This means that you can use any URL, such as a [getint.io](http://getint.io/), to generate your client ID and secret key.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FaKeMT2hqrwd8TYfV1Oml%2FOAuth%20credentials%20options.png?alt=media&#x26;token=2412e9aa-97e2-47bb-9350-f05207df3d0d" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
It is important to note that **Development information** must be selected.
{% endhint %}

* Your newly created credentials will appear in the corresponding screen as shown below.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fgy1ChmxQugNnyiPbn3G4%2FAfter%20OAuth%20creation%20screen.png?alt=media&#x26;token=da97ecf3-45cc-4031-8f7d-2a73e59d69ef" alt=""><figcaption></figcaption></figure>

* To establish the connection, use your OAuth credentials along with your email and personal access token. You can create the personal access token by following the instructions provided at the beginning of this connector or clicking [here](https://docs.getint.io/guides/quickstart/connection#jira-cloud-oauth).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FzclqFnlDwnY0cdP8XbLA%2FCreate%20the%20connection%20with%20the%20newly%20created%20credentials.png?alt=media&#x26;token=e1a91060-c4b2-4861-b992-da6e890d9bb1" alt=""><figcaption><p>Here is an example of the correct way to enter all credentials</p></figcaption></figure>

With these credentials, you'll be able to successfully connect your Jira instance to another tool. This opens up new opportunities for your integration journey, enabling smooth integration and data synchronization between the two platforms.

#### **Connecting Jira Data Center/Server**

Unlike the cloud, the data center will not require a token but can work with an email and a password. If Chosen to use the Token, leave the "email" option blank in the Getint platform:

* Log in to your Jira Data Center instance.
* Click on the Avatar on the top right of the screen.
* Select "Profile" and then "Personal Access Tokens."
* Click on "Create Token," provide a name for your Token, and select if this Token will expire and when.
* Copy the token and ensure it is stored securely in a safe location.

{% embed url="<https://youtu.be/5bpdLeFn-Qo>" %}

#### **Jira Service Management**

Jira also has the Jira Service Management option for service tasks and projects. This can also be integrated and will use a Personal Token as a Password:

* Log in to your Jira instance.
* Click on the Avatar on the top right of the screen.
* Select "Profile" and then "Personal Access Tokens."
* Click on "Create Token," provide a name for your Token, and select if this Token will expire and when.
* Copy the token and ensure it is stored securely in a safe location.

Connect as you would for a Jira Cloud, Server, or Data Center, depending on your type of access.

{% hint style="info" %}
The permission level of personal access tokens in the Data Center is set to the level of access you currently have.
{% endhint %}

### **Asana**

Generating an Asana Token:

* Log in to your Asana account.
* Click on your profile picture and go to "My Profile Settings."
* Select the "Apps" tab, and under "App Integrations," click "Manage Developer Apps."
* Click "+ New Access Token," provide a description, and create the token.
* Copy and securely store the token.

{% embed url="<https://youtu.be/5Ml9hdha57U>" %}

### **Airtable**

To ensure seamless synchronization with Airtable, it's crucial to incorporate a "Last Modified Time" column within the table designated for synchronization with other applications. Follow these steps to set it up if it's not already visible:

* Click on the "+" button on the table's right side.
* Select "Last Modified Time" from the options provided.
* Enter "Last Modified Time" in the name field.
* Click on the "Create Field" button to finalize the setup.

Then, let's create the Access Token:

* Click on your profile icon and navigate to the "Account" section.
* Choose the "Developer Hub" subsection, then select "Personal Access Tokens."
* Press the "Create New Token" button.
* Name your token and select the appropriate scopes.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FZMv6kuu8uTrYA1T7651r%2FAirtable%20token.png?alt=media&#x26;token=af2f1a4d-d1d1-4120-aa7d-7067d86db901" alt=""><figcaption></figcaption></figure>

* Specify which team the token would give access to.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FRfVzjyNTdP5EmzWjEFcY%2FAirtable%20personal%20access%20token.png?alt=media&#x26;token=36ff759d-a6bf-4322-a387-2fb326b05e7f" alt=""><figcaption></figcaption></figure>

* Press create and ensure to store it securely in a safe location.

{% embed url="<https://youtu.be/t2VVnNq0EZI>" %}

### **Azure DevOps**

If you want to integrate Azure DevOps (ADO) with your Server or Cloud, you must provide a token with the necessary permissions. Follow the steps below to generate a token:

* Log in to your Azure DevOps organization.
* Open User Settings from the profile menu.
* Select Personal Access Tokens from the left sidebar.
* Click "New Token" and enter a name for the token.
* Set the expiration for the token and select the appropriate scopes:
  * Work Items - Read & Write
  * Project and Team - Read & Write
  * Graph - Read (graph permission is necessary to ensure accurate user data retrieval)
  * Code - Read (if you're syncing repositories with the Git Connector)
* Click Create, then copy and securely store the generated token. This token will authenticate and authorize Getint to access your Azure DevOps organization.
* When configuring the Azure DevOps connection details in Getint, provide the generated token as the password.

{% embed url="<https://www.loom.com/share/de71aa8b806340039b5931b0c9c4c74d>" %}

### **ClickUp**

To connect with the ClickUp app user must provide a personal API token in the API TOKEN field. Every ClickUp user, whether a team member or guest, has the power to create their token with ease. Here's how you can do it:

* Log in to ClickUp.
* If you're using ClickUp 2.0, simply click on your avatar at the lower-left corner and select "Apps." For ClickUp 3.0 users, click on your avatar in the upper-right corner, then choose "Settings" and scroll down to click on "Apps" in the sidebar.
* Look for the "API Token" section, and with just a click on "Generate," your token is created.
* Now, feel free to copy and paste your unique API token wherever you need it for seamless integration and authentication.

{% embed url="<https://youtu.be/fT0Rd_ikXsU>" %}

### **Freshdesk**

Ensure seamless synchronization of your Freshdesk tickets, calls, and other crucial details with these simple steps:

* Log in to your Freshdesk account.
* Click on your profile picture located in the top right corner and select "Profile Settings."
* In the sidebar on the right, locate the "View API key" button. Click on it to access the API key and complete the captcha verification when prompted.
* Copy the API key provided.
* Paste this API key to authenticate your Getint integration.

Remember, if needed, you can reset the API Key to deauthorize an app from connecting to your helpdesk. However, note that doing so will also disconnect all other apps using this key. You'll need to provide the new key to these apps to resume their usage.

{% hint style="warning" %}
While customers have the flexibility to customize their Freshdesk instance URL, Getint will only establish the connection if the primary (original) URL is properly entered.

For example, the customer's current URL could be <https://support.getint.io>; however, their original URL was <https://help-getint.io>.
{% endhint %}

{% embed url="<https://youtu.be/AXpUq3NEhqE>" %}

### **Freshservice**

Connect to Freshservice:

* Log in to your Freshservice account, click on your profile picture in the top right corner, and select "Profile Settings."
* On the new page, click on "Your API Key" and select the check button to access the API key.
* Complete the captcha verification when prompted, and copy the API Key for integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FKUd6nFTiaoE09vxaGSAU%2FFreshservice%20token.jpg?alt=media&#x26;token=f18207fb-910b-42a9-bb89-ebdc82ad3985" alt=""><figcaption></figcaption></figure>

### **GitLab**

**Generating a GitLab Token:**

GitLab offers a comprehensive platform for version control, collaboration, and continuous integration. You can generate a Personal Access Token to enable integration with other applications:

* Log in to your GitLab account.
* Go to "User Settings" and select "Access Tokens."
* Choose a name, an expiration date, and the desired scopes for the token.
* Click "Create personal access token," then copy and securely store the token.

{% embed url="<https://youtu.be/JqOHsYnVX6M>" %}

### **GitHub**

Like other platforms, you can generate a Personal Access Token in GitHub to facilitate integration with external tools and platforms. However, the app is now offering a beta version that can also be used:

#### **Generating a GitHub Token (Classic):**

* Log in to your GitHub account.
* Go to "Settings," then "Developer settings."
* Select "Personal access tokens" and select "Generate new token." In the dropdown menu, select "Generate new Token (Classic)."
* On the screen that will appear, provide a name for your Token, select the scopes like the example below, and save:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FK78gFKNla20AQzITYwdf%2FGenerating%20a%20GitHub%20Token%20(classic).png?alt=media&#x26;token=4ff0fa4b-765e-406e-b7b0-bb1c273fe631" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FIzQGzQ3LsuOAJp7yfkS8%2FGenerating%20a%20GitHub%20Token%20(classic)%20-%20Rest%20of%20the%20permissions.png?alt=media&#x26;token=d0d555b2-e762-4c5d-8519-4a8392ed143b" alt=""><figcaption></figcaption></figure>

* Copy and securely store the token.

#### **Video Tutorial for Token (Classic)**

{% embed url="<https://www.loom.com/share/dfb4847898e6458283287e88d3d04d52?sid=fcd5ea49-be06-46fc-985b-b5baa00b15eb>" %}

#### **Generating a Fine-Grained Token:**

* Log in to your GitHub account.
* Go to "Settings," then "Developer settings."
* Select "Personal Access Tokens," then go to "Fine-grained personal access Tokens."
* Click on Generate New Token. Choose a name for your Token, set the expiration date and repository access, and provide the necessary access permissions in the dropdown list.

#### **Video Tutorial for Fine-Grained Token**

{% embed url="<https://www.loom.com/share/aa25716c7ac44b2594c46f462a3f2500?sid=14b4c1f7-6d1c-4a65-b657-7cc0750b05cb>" %}

### **HubSpot**

To connect with the HubSpot app, the user must provide an API token from a Private App. Only API Tokens are supported at the moment. To create a Private App:

* Log in to your HubSpot account, and click on your initials in the top right corner.
* Select "Profile and Preferences" and then navigate to Integrations > Private Apps.
* Click "Create a Private App."
* On the Basic Info tab, provide a name for your App and then select Scopes:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FePCVrmp8zx3Epbbki8sA%2FGetint%20Sync.png?alt=media&#x26;token=4c34b981-03eb-46b4-a08c-f987caa8f2a9" alt=""><figcaption></figcaption></figure>

* After you're done configuring your app, click "Create app" on the top right.

{% embed url="<https://youtu.be/EsXLv5VsyOg>" %}

### **Monday.com**

Generating a Monday.com Token:

* Log in to Monday.com, click on your initials in the top right corner, and navigate to Administration.
* On the next screen, select "API" and regenerate the token.
* Copy the Personal Access token, then continue your integration setup following the guide provided for [Jira Monday.com integration](https://docs.getint.io/guides/integration-synchronization/jira-monday-integration).

{% embed url="<https://www.loom.com/share/da2bbdaa0f0049609567868de98753e1?sid=505e3306-9363-41aa-88a7-99778700e173>" %}

### **Notion**

Integrating Notion with Getint allows you to synchronize your project management tasks seamlessly across platforms. Below is a detailed guide on how to connect Getint with Notion:

* In the Notion app, click on the three dots in the top right corner, then select "Connection to" and navigate to "Manage Connections." Choose "Develop or Manage integrations."
* Select "New Integration," provide a name for your integration, and grant the necessary permissions.
* Copy the generated API token, close the window, return to the Notion dashboard, and click on the three dots again.
* Scroll down to add a connection, select the name of the connection that you have already created, and agree to the pop-up that appears. Continue your integration setup following the guide provided for [Jira Notion integration](https://docs.getint.io/guides/integration-synchronization/jira-notion-integration)

{% hint style="info" %}
It might be necessary to refresh your browser to see the new connection in the list.
{% endhint %}

{% embed url="<https://youtu.be/EpbjAtGoEQE>" %}

### **Salesforce**

To connect with Salesforce, users must grant permissions to Getint via the OAuth authentication method. These credentials are securely stored in a dedicated Getint database and are used exclusively by that user. Follow the steps below to create a new connection between Getint and your Salesforce instance:

1. Sign in to your Salesforce account, then click the "Cog" icon in the upper-right corner of the screen. From there, select "Setup" to access your user settings.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FchMQZxU2imQtC71PTuhn%2Fa6c9112bffc8242333cbcb242573c2f6.png?alt=media&#x26;token=9796f9bf-75e5-4f3f-8553-1a5ad8ba8942" alt=""><figcaption></figcaption></figure>

1. Navigate to "Platform Tools," then select "Apps." From there, go to "External Client Apps" and open the "External Client App Manager."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FkMTgXBtjiwoA9MNg7DJT%2FExternal%20Client%20App%20Manager.png?alt=media&#x26;token=7b09ab4a-e82f-4b5a-badf-c94c4762f3f5" alt=""><figcaption></figcaption></figure>

1. Select "New External Client App" to create a new application.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FOyZLjcBeLP9SWNcfGs80%2FNew%20External%20Client%20App.png?alt=media&#x26;token=520c5714-b60e-4119-b23d-eb99bc0d54bc" alt=""><figcaption></figcaption></figure>

1. Enter a unique name, your email address, and the API name.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FsDLojbocuKUMO6OZqijl%2FExternal%20Client%20App%20Manager%20Setup.png?alt=media&#x26;token=dfb9525c-882e-4338-a10c-d61d30fb1b47" alt=""><figcaption></figcaption></figure>

1. **Enable OAuth**:
   * Turn on "OAuth" by scrolling down and enabling it.
   * Enter the **Callback URL**: `https://login.salesforce.com/services/oauth2/callback`.
   * Choose the required "OAuth Scope: Manage user data via APIs (API)."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FI85U9OjfcVAAGOfI0UuB%2FEnabling%20API%20Settings.png?alt=media&#x26;token=5590ba5b-5581-4549-b621-aa963d9bd84a" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Salesforce mandates the use of HTTPS for the Callback URL to ensure secure communication.
{% endhint %}

1. Scroll down to the "Flow Enablement" section and activate the "Client Credentials Flow." After that, turn off all other options in the "Security" section.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FvUPHXsxVYX2EH2QYmurf%2FEnable%20Client%20Credentials%20Flow.png?alt=media&#x26;token=b072a14a-a81f-4860-a67b-08cbb7e4b101" alt=""><figcaption></figcaption></figure>

1. **Create the External Client App**:
   * Click "Create" at the bottom of the page.
   * Once the app is created, go back to edit its settings. You should see the new client listed.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FlGZxon9zRTWIwfwuITzH%2FNew%20client%20created%20(1).png?alt=media&#x26;token=056f78bd-ce9c-42bd-9d76-e57ebff3a17d" alt=""><figcaption></figcaption></figure>

1. **Edit Settings for the new Client**:
   * Select "Edit" to access the settings.
   * Open the section for "OAuth Policies."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FIqvo3Na3RMQHFpEkZJC8%2FNew%20client%20created.png?alt=media&#x26;token=4712917e-5b34-437b-bb79-cca997dcf1c5" alt=""><figcaption></figcaption></figure>

1. Enable "Client Credentials Flow" and enter the username found under "Personal Information" in your profile. Click "Save" at the bottom of the page to apply your changes.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fb03ppB2fZCtf9huCVhnN%2FOAuth%20Flows%20and%20External%20Client%20app%20Enhancements.png?alt=media&#x26;token=b8b2e41f-ae3e-4e14-b85b-eb193b328fb3" alt=""><figcaption></figcaption></figure>

1. **Generate** `client_id` **and** `client_secret`**:**
    * Go to the "Settings" tab from the "Policies" tab.
    * Select "Consumer Key and Secret" to proceed.
    * You’ll be redirected to a verification screen.
    * Copy the "Consumer Key" (client\_id) and "Consumer Secret" (client\_secret) for future use.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FEuJc4jgls9nAO4wUFyOx%2Fgenerating%20ID%20and%20Secret.png?alt=media&#x26;token=397cd405-475b-4889-8e12-4d9bc0e4cc4e" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FAkuqHtW9dPOxOhuSXSy6%2FClient%20ID%20and%20Secret.png?alt=media&#x26;token=6ed14864-b0fe-4373-8319-b1a751b15c89" alt=""><figcaption><p>Using these credentials, you're ready to establish a connection with Salesforce in Getint.</p></figcaption></figure>

1. **Create a Salesforce Connection in Getint**:
    * Choose "Salesforce" and click "Create a Connection."
    * Enter your Salesforce Instance URL in the "URL" field and click "Next."
    * Give the connection a name and input the "client\_id" and "client\_secret."
    * Add the connection, then select it to complete the setup.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMqy14CoUOm09U74YGxOk%2FCreating%20a%20connection%20with%20Salesforce.png?alt=media&#x26;token=55e9c9d8-4a81-417e-a856-65a80f555f82" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Make sure to use the correct URLs to connect to your instance:

* `https://YOUR_INSTANCE_NAME.develop.lightning.force.com`
* `https://YOUR_INSTANCE_NAME.develop.my.salesforce.com`

Salesforce has several editions, including Enterprise, Unlimited, Performance, Developer, Group, Essentials, and Professional. The API is automatically enabled in Enterprise, Unlimited, Performance, and Developer editions. For Group, Essentials, and Professional editions, the API is not enabled by default.

If you run into issues or can't find the API option, reach out to the Help and Training Community or contact our support team through the [support portal.](https://getint.io/help-center)
{% endhint %}

### **ServiceNow**

Integration involves providing connection details like instance URLs and credentials or API tokens to enable seamless communication with other applications. The ServiceNow will require the creation of a special user, as shown in [Creating a ServiceNow User for Getint Integration](https://docs.getint.io/guides/integration-synchronization/jira-servicenow-integration/creating-a-servicenow-user-for-getint-integration).

**Set Up ServiceNow Connection**

* Click CONNECT APP, and then click ServiceNow.
* Input the URL of your ServiceNow instance you want to connect to, and click "Next."
* In the next screen, provide the name for the connection, username, and password for the ServiceNow account.
* Click "Add" to set up the connection.

{% embed url="<https://youtu.be/Iythq-HdHsI>" %}

{% hint style="warning" %}
You will get an "insufficient permissions" or "user cannot be authenticated" error if you haven't created the ServiceNow user.
{% endhint %}

### **Trello**

Trello is part of the Atlassian environment. Being linked to your Atlassian, the user creating the connection must have access to the project and admin permissions to enable the connection.

* In the Getint app, select "Trello" and "Create a new connection."
* Name your connections, select "Authorize GetInt," review the permissions, and accept.
* Select the project that you want to sync and select "Connect."
* Choose the connection you just created and press connect. Continue your integration setup following the guide provided for [Jira Trello](https://docs.getint.io/getting-started-with-the-platform/integration-synchronization/jira-trello-integration) integration.

{% embed url="<https://youtu.be/esiUOXBizsU>" %}

### **Wrike**

Generating a Wrike Token:

* Log in to your Wrike account.
* Click on your initials on the top right of the page, select "Apps & Integrations," then go to "API."
* On the API tab, add a name for your Token in the "App Name" field and click "Create New."
* Scroll down to the bottom of the page and under "Permanent Access Token," select "Create Token."
* Add your Wrike password and click on "Obtain token." Then select "Copy Token."

{% embed url="<https://youtu.be/HgyRhch-rgM>" %}

### **Zendesk**

Connecting with Zendesk requires creating the API access, which can be controlled in the Admin Center.

* Access your Zendesk instance with Admin credentials. Select the four-square icon and choose "Admin Center."
* Navigate to "Apps and integrations" and select "Zendesk API."
* Enable "Token Access" by toggling the switch on the right, then clicking "Add API Token."
* Create a name for your token, copy it, and select "Save."
* Follow the complete guide on integrating [Jira with Zendesk](https://docs.getint.io/getting-started-with-the-platform/integration-synchronization/jira-zendesk-integration) to continue setting up your integration.

{% embed url="<https://youtu.be/Unnp9UrFCAw>" %}

{% hint style="info" %}
If you have any questions or need assistance, please do not hesitate to contact us at our [Help Center](https://getint.io/help-center) or [Schedule a Demo](https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team).
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

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

# Integration Guides

# Git Repository integration

With the integration of Git, repository management becomes highly practical and efficient. We currently support integration with Azure DevOps, GitLab, and GitHub. Whether you're merging branches, tracking changes, or rolling back to previous versions, you can track all these changes seamlessly within your Jira instance. This integration allows you to easily track **repositories**, **branches**, **commits**, and **pull requests**.

Our Git integration app for Jira is available at the following link: [Git Connector for Jira.](https://marketplace.atlassian.com/apps/1236406/git-connector-for-jira-azure-devops-github-gitlab?hosting=cloud\&tab=overview)

{% hint style="warning" %}
While it is possible to create a Git integration using other integration apps, it is mandatory to have the Git Connector app installed.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F16CHi6P2piPZwusJr8af%2FGetint%20White%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=703e3f94-c326-4b4e-a684-baaf294c1bdd" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

### How to Build a Git Integration <a href="#how-to-build-a-git-integration" id="how-to-build-a-git-integration"></a>

#### 1. Launch the Getint App: <a href="#id-1.-launch-the-getint-app" id="id-1.-launch-the-getint-app"></a>

* Navigate to **Apps**, launch the app **Git Connector for Jira**, go to **Integrations**, click **Create Integration**, and select **Sync GIT Repository**.
* If you’re using Getint On-Premise, simply launch the app, click **Create Integration**, and select **GIT**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FDC3rn331vJYbArTMksN6%2FGIT%20REPOSITORY%20OPTION.png?alt=media&#x26;token=13e3f588-1880-4da0-acec-034f2b42cd4e" alt=""><figcaption></figcaption></figure>

#### 2. Create a Connection for the App Containing the Git Repository: <a href="#id-2.-create-a-connection-for-the-app-containing-the-git-repository" id="id-2.-create-a-connection-for-the-app-containing-the-git-repository"></a>

* Select the app you want to integrate by clicking the **Connect App** button.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fcaqysp7JfGO8CwRb4jR5%2FSelect%20the%20app%20you%20want%20to%20integrate.png?alt=media&#x26;token=6cba9594-f34d-4031-8cd7-ce2f11718fc8" alt=""><figcaption></figcaption></figure>

* Create a connection or select an existing one.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FTzsC9ZxCUT8GR19kP8k6%2FCreate%20New%20Connection%20or%20Select%20an%20existing%20connection.png?alt=media&#x26;token=b4a3c649-eaff-4a73-a002-57f1db94a9aa" alt=""><figcaption></figcaption></figure>

* Follow the next steps depending on the app you selected. We’re taking GitLab as an example, but the process is the same for the rest of the connectors.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FyPsJDKMX12njsLT91lf5%2FNaming%20your%20connection%20and%20adding%20access%20token.png?alt=media&#x26;token=4b7b51ec-a0f1-4e54-b0ce-7f2f03717c28" alt=""><figcaption></figcaption></figure>

* Once you've added your details, you'll find your new connection in the dropdown list of available connections. Please select it and click **Connect** to complete the process.

{% hint style="info" %}
For detailed instructions on creating a connection and generating an access token, please refer to our comprehensive guide: [Connections | Tokens and Requirements](https://docs.getint.io/guides/quickstart/connection).
{% endhint %}

#### 3. Establish a Connection with Jira: <a href="#id-3.-establish-a-connection-with-jira" id="id-3.-establish-a-connection-with-jira"></a>

* Make sure you are logged in with admin rights, then click on **Connect App** and select **Jira**. Choose **Create New** to establish a fresh connection with your Jira instance and enter the URL of your Jira instance.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FViEmoRAVjRwNaM4c9uxV%2FAdd%20the%20URL%20of%20your%20Jira%20instance.png?alt=media&#x26;token=0c2fb255-2c54-4bcd-8d17-388e502d99a7" alt=""><figcaption></figcaption></figure>

* Unlike **Continuous Syncs** or **Migrations**, GIT integrations require users to set up OAuth in their Jira instance. Please ensure you have admin permissions; otherwise, you will not be able to set up the OAuth credentials. Then, follow our guide to configure a Jira OAuth at the following: [Connection | Jira OAuth.](https://docs.getint.io/guides/quickstart/connection#jira-cloud-oauth)
* Enter the necessary details to establish the connection.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fk4fwjhgAACAHG2j3KhyJ%2FCreating%20a%20connection%20with%20Jira%20for%20a%20GIT%20integration.png?alt=media&#x26;token=dfaf9b91-4170-429a-884e-4c775a27eb4d" alt=""><figcaption></figcaption></figure>

* Once you've added your details, you'll find your new connection in the dropdown list of available connections. Please select it and click **Connect** to complete the process.

#### 4. Building Your Integration: <a href="#id-4.-building-your-integration" id="id-4.-building-your-integration"></a>

* By default, the Git repositories will sync with all projects in your Jira instance. However, unchecking this option allows you to select one or multiple projects where you want this information to be available.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fcrp2zQWC4JhlGxHx7hxV%2Fjira%20git%20connector.png?alt=media&#x26;token=799b7b94-e002-445b-a5ae-9f14b3c64337" alt=""><figcaption></figcaption></figure>

* For example, you can select specific projects based on your company’s needs. Next, choose the Git repositories you want to sync. Finally, name your integration and click **Create** at the top right corner of the screen to save it.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FeD7VNdkrMmWb2cjsz95N%2FSelect%20the%20Git%20Repositories%20and%20Jira%20projects.png?alt=media&#x26;token=59923863-c07b-46f3-992a-db2efa062421" alt=""><figcaption></figcaption></figure>

* Once you've created your integration, it will be easily accessible in the **Integrations** section within Workflows, and it is marked with a code icon.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fy05P9ZUj2IfTsCL4Expx%2FGit%20Repositories.png?alt=media&#x26;token=3144ac2c-3963-4289-afd6-376280050299" alt=""><figcaption></figcaption></figure>

* If you did not install the Git Connector app as instructed at the beginning of the article, you will encounter an error like the one shown below:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fl14thAOIsUVU9ucwK4Nr%2FSync%20error%20due%20to%20missing%20Git%20connector.png?alt=media&#x26;token=9d566c5c-567a-4c1e-8ed7-a06deb5c98f5" alt=""><figcaption></figcaption></figure>

#### 5. Test the Integration and Sync Your Branches <a href="#id-5.-test-the-integration-and-sync-your-branches" id="id-5.-test-the-integration-and-sync-your-branches"></a>

* To start syncing branches, ensure that you use the ID of the Jira task as a prefix for the branch names. For branch names, only underscores or dashes can be used instead of spaces. For example **ED-23-resolve-support-ticket-9843-migrate**.
* For example, if you’re syncing an item with the Jira ID **ED-23**, your branch should be named **ED-23 + branch name**, as shown below:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FXVyMeraVnPrUOLQ8FcYd%2Fnaming%20new%20branches.png?alt=media&#x26;token=c61d5086-b52d-4c5d-acf9-2464e3e97350" alt=""><figcaption><p>Example of proper branch naming for synchronization. Using GitHub as an example, the same principle applies to the other connectors.</p></figcaption></figure>

* If the correct naming prefix is not used to sync your items, an error like the one below will occur:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FdRqi0bfxOuT4KJikt6vN%2FGit%20sync%20error.png?alt=media&#x26;token=4a8ffa76-97c9-4ad0-9a55-724924060cb0" alt=""><figcaption></figcaption></figure>

* The Git repository details of your Jira items will be available in the Development field. Refresh the page if you don’t see any changes to the Development field.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FyZjqactZD1plsWifSHPp%2FChecking%20how%20changes%20are%20being%20integrated%20to%20Jira.png?alt=media&#x26;token=30df93ba-ee71-467f-baa5-12a8dc792489" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Depending on your Project template, the Development field may not be visible. In such cases, you must either add the field by modifying the issue layout or switch to a different template.
{% endhint %}

* By clicking on this field, you can easily access all the information that is being collected from the repositories.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fgx4778nNEoaJzUXAViCm%2FDevelopment%20field%20for%20git%20integration.png?alt=media&#x26;token=ce1a88c4-ecd4-4055-8f28-61eec798f166" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Getint enables the synchronization of Repositories, Branches, Commits, and Pull Requests. However, please note that changes cannot be submitted from Jira to the Git repository. The synchronization of repository information is one-way from the Git connector.
{% endhint %}

### Conclusion <a href="#conclusion" id="conclusion"></a>

With this comprehensive guide, you can seamlessly integrate Git with Jira and take full advantage of efficient repository management. If you require any assistance or have further questions, don't hesitate to contact us [here](https://getint.io/help-center).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Git Connector - Azure DevOps

With the integration of Git, repository management becomes highly practical and efficient. We currently support integration with Azure DevOps. Whether you're merging branches, tracking changes, or rolling back to previous versions, you can track all these changes seamlessly within your Jira instance. This integration lets you easily track **repositories**, **branches**, **commits**, and **pull requests**.

Our Git integration app for Jira is available at the following link: [Git Connector for Jira.](https://marketplace.atlassian.com/apps/1236406/git-connector-for-jira-azure-devops-github-gitlab?hosting=cloud\&tab=overview)

{% hint style="warning" %}
While it is possible to create a Git integration using the Azure DevOps integration app, it is mandatory to have the Git Connector app installed.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F3wmXPrAwlaQk7K4jQcMo%2FGetint%20White%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=412364ac-394b-4c84-bf60-e26925e07dcb" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

### How to Build a Git Integration for Azure DevOps <a href="#how-to-build-a-git-integration-for-azure-devops" id="how-to-build-a-git-integration-for-azure-devops"></a>

#### 1. Launch the Getint App: <a href="#id-1.-launch-the-getint-app" id="id-1.-launch-the-getint-app"></a>

* Navigate to **Apps**, launch the app **Git Connector for Jira**, go to **Integrations**, click **Create Integration**, and select **Sync GIT Repository**.
* If you’re using Getint On-Premise, simply launch the app, click **Create Integration**, and select **GIT**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FLz79THZQV0fEbkSnlZUx%2FGIT%20REPOSITORY%20OPTION.png?alt=media&#x26;token=920487b3-4c18-45be-9a0d-2b9126678b13" alt=""><figcaption></figcaption></figure>

#### 2. Create a Connection with Azure DevOps: <a href="#id-2.-create-a-connection-with-azure-devops" id="id-2.-create-a-connection-with-azure-devops"></a>

* Click the **Connect App** button, and select **Azure DevOps**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Ft6NEa2kCl4SoaSucmULK%2FSelect%20the%20app%20you%20want%20to%20integrate%20-%20DevOps.png?alt=media&#x26;token=6f03f2ad-f0da-4990-806a-5da260cd7f96" alt=""><figcaption></figcaption></figure>

* Create a connection or select an existing one.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FIMzxE2qfiB0LUgEZA2Ye%2FCreate%20New%20Connection%20or%20Select%20an%20existing%20connection.png?alt=media&#x26;token=ea5be1c6-94ae-4ea0-9de6-1721d3c33d05" alt=""><figcaption></figcaption></figure>

* Tap on **Create a new connection** if you don’t have an existing one.
* Enter your instance URL, and click on **Connect**.
* Name the connection, input your email, and paste the token generated (create the personal access token following the instructions in this guide: [Connections](https://docs.getint.io/guides/quickstart/connection#azure-devops)). Then click **Add**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FGNsemYijaZscjjUX16Tv%2FCreating%20a%20connection%20with%20Azure%20DevOps.png?alt=media&#x26;token=c0296d9d-13b4-4014-9585-357c166f981d" alt=""><figcaption></figcaption></figure>

* Once you've added your details, you'll find your new connection in the dropdown list of available connections. Please select it and click **Connect** to complete the process.

{% hint style="warning" %}
For Git Azure DevOps integrations, it is important to set the scope **Code** to **Read**. Otherwise, you’ll get the following error:

*Unfortunately, your integration failed to save due to the following reason: Forbidden.*
{% endhint %}

#### 3. Establish a Connection with Jira: <a href="#id-3.-establish-a-connection-with-jira" id="id-3.-establish-a-connection-with-jira"></a>

* Ensure that you are logged in with administrative rights, then click on **Connect App** and select **Jira**. Click on **Create New** to set up a new connection with your Jira instance and enter the URL of your Jira instance.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FqvVDf27e4wRmzgdIy6BL%2FAdd%20the%20URL%20of%20your%20Jira%20instance.png?alt=media&#x26;token=80cc6191-f359-4979-bec6-d9621aa00a8c" alt=""><figcaption></figcaption></figure>

* Unlike **Continuous Syncs** or **Migrations**, GIT integrations require users to set up OAuth in your Jira instance. Please ensure you have admin permissions; otherwise, you will not be able to set up the OAuth credentials. Then, follow our guide to configure a Jira OAuth at the following: [Connection | Jira OAuth.](https://docs.getint.io/guides/quickstart/connection#jira-cloud-oauth)
* Enter the necessary details to establish the connection.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9E20Mude7KWSaIM0KOvu%2FCreating%20a%20connection%20with%20Jira%20for%20a%20GIT%20integration.png?alt=media&#x26;token=3ec045f0-eb62-4e83-983d-45f576901960" alt=""><figcaption></figcaption></figure>

* After entering your details, your new connection will appear in the dropdown list of available connections. Please select it and click **Connect** to finalize the setup.

#### 4. Building Your Integration: <a href="#id-4.-building-your-integration" id="id-4.-building-your-integration"></a>

* By default, the Git repositories will synchronize with all projects in your Jira instance. However, if you uncheck this option, you can choose one or multiple projects where you want this information to be accessible.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FitkgLgg1BZkgx1qB4iiv%2FGit%20integration%20-%20Azure%20DevOps.png?alt=media&#x26;token=7c718d82-e968-4a2e-b018-79c9e429c2b3" alt=""><figcaption></figcaption></figure>

* For instance, you can choose specific projects according to your company's requirements. Then, select the Git repositories you wish to synchronize. Lastly, give your integration a name and click **Create** at the top right corner of the screen to save it.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FpWQXyuvuywJdPvLD5nQP%2FAzure%20DevOps%20Git%20integration.png?alt=media&#x26;token=5dba6db7-432d-4709-8347-e547fe4f1602" alt=""><figcaption></figcaption></figure>

* After creating your integration, it will be readily available in the Integrations section within Workflows, identified by a code icon.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FOMdLDE1ZYF6xe8PjFGEw%2FChecking%20Azure%20DevOps%20integration%20from%20Workflows%20section.png?alt=media&#x26;token=4836d789-5481-4155-97ef-863b38ce8b40" alt=""><figcaption></figcaption></figure>

* If you did not install the Git Connector app as instructed at the beginning of the article, you will encounter an error like the one shown below:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F6Pg0OECp7YyPZQOVys6W%2FSync%20error%20due%20to%20missing%20Git%20connector.png?alt=media&#x26;token=41050743-9eae-4562-ac5d-684c63216261" alt=""><figcaption></figcaption></figure>

#### 5. Test the Integration and Sync Your Branches <a href="#id-5.-test-the-integration-and-sync-your-branches" id="id-5.-test-the-integration-and-sync-your-branches"></a>

* To start syncing branches, use the Jira task ID as a prefix for the branch, commit, and pull request names. For branch names, only underscores or dashes can be used instead of spaces. For example **ED-32\_Energy\_Dot**.
* For instance, if you are syncing an item with the Jira ID **ED-32**, your branch should be named **ED-32** followed by the branch name, as shown below:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F0dJWjqdDvgQu0Vx2gewY%2FAzure%20DevOps%20-%20Creating%20branches.png?alt=media&#x26;token=9e740c87-8ada-46ae-954c-e3499117f7d1" alt=""><figcaption><p>Example of proper branch naming for synchronization.</p></figcaption></figure>

* If you fail to use the correct naming prefix to sync your items, you will encounter an error similar to the one shown below:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FziOt6DvRWjjyeQCvpDxE%2FGit%20sync%20error.png?alt=media&#x26;token=79304c6b-eece-4851-8d78-867bdbdcb569" alt=""><figcaption></figcaption></figure>

* The Git repository details of your Jira items will be available in the Development field. Refresh the page if you don’t see any changes to the Development field.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FIpjysDbkpfwNfGR9UliW%2FDevelopment%20field%20for%20Azure%20DevOps%20Git%20integration.png?alt=media&#x26;token=676e44c7-b9c8-4318-9a6a-f0de6acc61f0" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Depending on your Project template, the Development field may not be visible. In such cases, you must either add the field by modifying the issue layout or switch to a different template.
{% endhint %}

* Clicking on this field allows you to effortlessly access all the information being fetched from the repositories.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F0TOuFjFYbBoICqOmZiRi%2FInside%20the%20Development%20field.png?alt=media&#x26;token=ebe8c9fe-baf3-4968-8dba-80b39fecf907" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Getint enables the synchronization of Repositories, Branches, Commits, and Pull Requests. However, please note that changes cannot be submitted from Jira to the Git repository. The synchronization of repository information is one-way from Azure DevOps.
{% endhint %}

### Conclusion <a href="#conclusion" id="conclusion"></a>

By following this detailed guide, you can effortlessly integrate Azure DevOps repositories with Jira and fully leverage efficient repository management. Should you need any assistance or have additional questions, please feel free to contact us here.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Git Connector - GitHub

Effortlessly sync your GitHub repositories with Jira using our in-depth guide. This comprehensive resource helps your team track changes, manage issues, and collaborate effectively.

We guide you through every step, from setting up the integration to configuring OAuth credentials and ensuring smooth data synchronization. As of now, we support syncing repositories, branches, commits, and pull requests. Discover how to link your GitHub repositories to Jira projects, enabling you to monitor branches, commits, and pull requests directly within Jira. This guide will show you how to combine the strengths of GitHub and Jira to optimize your workflow, boost visibility, and enhance productivity.

Access our Git integration app for Jira through this link: [Git Connector.](https://marketplace.atlassian.com/apps/1236406/git-connector-for-jira-azure-devops-github-gitlab?hosting=cloud\&tab=overview)

{% hint style="warning" %}
The Git Connector app is not required if you're using the GitHub integration app.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F6TmPdBT0Gk3Tg0aM9rT8%2FGetint%20White%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=29bc1de5-0133-41a6-bdaa-08db20302cf5" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a><br></p></figcaption></figure>

### How to Build a Git Integration for GitHub <a href="#how-to-build-a-git-integration-for-github" id="how-to-build-a-git-integration-for-github"></a>

#### 1. Launch the Getint App: <a href="#id-1.-launch-the-getint-app" id="id-1.-launch-the-getint-app"></a>

* Go to **Apps**, open the Git Connector for Jira app, navigate to **Integrations**, click **Create Integration**, and choose **Sync GIT Repository**.
* If you’re using Getint On-Premise, simply open the app, click **Create Integration**, and choose **Sync GIT Repository**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F7kXR3sPFRHv0EgaEYbFX%2FGIT%20REPOSITORY%20OPTION.png?alt=media&#x26;token=369c2764-ffd7-4f43-9971-6727fdf110c4" alt=""><figcaption></figcaption></figure>

#### 2. Create a Connection with GitHub: <a href="#id-2.-create-a-connection-with-github" id="id-2.-create-a-connection-with-github"></a>

* Click the **Connect App** button, and select **GitHub**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FHTrUIwMDRpI3WLm5gk2R%2FSelecting%20GitHub%20for%20Git%20integration.png?alt=media&#x26;token=3afeefe7-6e22-40c4-aa68-2db5f10e77a1" alt=""><figcaption></figcaption></figure>

* Create a connection or select an existing one.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FS6EWuoFdc9CENGKzDf4P%2FCreate%20New%20Connection%20or%20Select%20an%20existing%20connection.png?alt=media&#x26;token=5cccedb7-3891-4806-8b9b-185c5e50891b" alt=""><figcaption></figcaption></figure>

* Tap on **Create a new connection** if you don’t have an existing one.
* Name the connection, and paste the token generated (create the personal access token following the instructions in this guide: [Connections](https://docs.getint.io/guides/quickstart/connection#github)). Then click **Add**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FtJqoAGaaUb7fTUsXYKnS%2FConnection%20to%20GitHub.png?alt=media&#x26;token=def5f2fc-f23d-484e-a3dc-8ad13dd71dd2" alt=""><figcaption></figcaption></figure>

* Once you've added your details, you'll find your new connection in the dropdown list of available connections. Please select it and click **Connect** to complete the process.

#### 3. Establish a Connection with Jira: <a href="#id-3.-establish-a-connection-with-jira" id="id-3.-establish-a-connection-with-jira"></a>

* Ensure that you are logged in with administrative rights, then click on **Connect App** and select **Jira**. Click on **Create New** to set up a new connection with your Jira instance and enter the URL of your Jira instance.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9jAABZyaQOrnhZdKPvg2%2FAdd%20the%20URL%20of%20your%20Jira%20instance.png?alt=media&#x26;token=331b1ea3-145b-4d6e-b91f-20e1d86aacb6" alt=""><figcaption></figcaption></figure>

* Unlike **Continuous Syncs** or **Migrations**, GIT integrations require users to set up OAuth in your Jira instance. Please ensure you have admin permissions; otherwise, you will not be able to set up the OAuth credentials. Then, follow our guide to configure a Jira OAuth at the following: [Connection | Jira OAuth.](https://docs.getint.io/guides/quickstart/connection#jira-cloud-oauth)
* Enter the necessary details to establish the connection.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F6qeU2BobwaYJooJftR99%2FCreating%20a%20connection%20with%20Jira%20for%20a%20GIT%20integration.png?alt=media&#x26;token=98df4b79-20f0-48b0-b71f-2b636c5cda53" alt=""><figcaption></figcaption></figure>

* After entering your details, your new connection will appear in the dropdown list of available connections. Please select it and click **Connect** to finalize the setup.

#### 4. Building Your Integration: <a href="#id-4.-building-your-integration" id="id-4.-building-your-integration"></a>

* By default, the Git repositories will automatically synchronize with all projects in your Jira instance. However, if you disable this option, you can specify one or multiple projects where this information should be available.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FTsST25NjptxPg2mGdJ4i%2FGitHub%20git%20repository%20integration.png?alt=media&#x26;token=4082aa1b-436a-4d92-91cc-55b65b28b39c" alt=""><figcaption></figcaption></figure>

* For example, you can pick particular projects based on your company's needs. Next, identify the Git repositories you want to sync. Finally, name your integration and click **Create** in the top right corner of the screen to save it.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FSBTdluLaUsYkvGnRTquo%2FGitHub%20connector.png?alt=media&#x26;token=48d29b71-2daa-4bd8-afa6-5952b89cc345" alt=""><figcaption></figcaption></figure>

* After creating your integration, it will be readily available in the Integrations section within Workflows, identified by a code icon.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FFJgdgT9pakrhoAsbjczB%2FCHecking%20the%20github%20integration.png?alt=media&#x26;token=6c12bbff-c115-4b3f-9f98-d7f6e83b4fb1" alt=""><figcaption></figcaption></figure>

* If you did not install the Git Connector app as instructed at the beginning of the article, you will encounter an error like the one shown below:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F8rWKCs35Bk6GLAN5o008%2FSync%20error%20due%20to%20missing%20Git%20connector.png?alt=media&#x26;token=acd8eae6-45b3-4a12-b8ba-269e314c314f" alt=""><figcaption></figcaption></figure>

#### 5. Test the Integration and Sync Your Branches <a href="#id-5.-test-the-integration-and-sync-your-branches" id="id-5.-test-the-integration-and-sync-your-branches"></a>

* To start syncing items, use the Jira task ID as a prefix for the branch, commit, and pull request names. For branch names, only underscores or dashes can be used instead of spaces. For example **ED-34**\_**New\_branch**.
* For instance, if you are syncing an item with the Jira ID **ED-34**, your branch should be named **ED-34** followed by the branch name, as shown below:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F8QR8BFVIt2DOGvl3MGcl%2FCreating%20a%20branch%20in%20GitHub.png?alt=media&#x26;token=5c9fe8d0-614d-4f24-9eac-9900b3355127" alt=""><figcaption></figcaption></figure>

* If you fail to use the correct naming prefix for branches and commits, you will encounter an error similar to the one shown below:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FGGSQ6NbcFDxwFj9639Nj%2FGit%20sync%20error.png?alt=media&#x26;token=383290ba-70a0-4968-aaf7-e1d7d438d649" alt=""><figcaption></figcaption></figure>

* The Git repository details of your Jira items will be available in the Development field. Refresh the page if you don’t see any changes to the Development field.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Foe9mmberMQWAoMD7fL9T%2FDevelopment%20field%20for%20GitHub%20integration.png?alt=media&#x26;token=cea5c9f5-cd85-42ba-b0be-8d3a60dee929" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Depending on your Project template, the Development field may not be visible. In such cases, you must either add the field by modifying the issue layout or switch to a different template.
{% endhint %}

* Clicking on this field allows you to effortlessly access all the information being fetched from the repositories.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FEjdZmK9zUjJWnS2Z4YS6%2FInside%20the%20development%20field%20-%20Github.png?alt=media&#x26;token=119fb1e6-7ed9-4bda-8362-aa102f553b55" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Getint enables the synchronization of Repositories, Branches, Commits, and Pull Requests. However, please note that changes cannot be submitted from Jira to the Git repository. The synchronization of repository information is one-way from GitHub.
{% endhint %}

### Conclusion <a href="#conclusion" id="conclusion"></a>

With this comprehensive guide at your disposal, you can seamlessly integrate GitHub repositories with Jira and unlock the full potential of efficient repository management. If you need any help or have any questions along the way, don't hesitate to reach out to us here.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Git Connector - GitLab

This article provides a comprehensive guide on how to sync GitLab repositories with Jira, allowing teams to track changes, manage issues, and collaborate more effectively.

We cover everything from setting up the integration to configuring OAuth credentials and ensuring smooth data synchronization. Learn how to link your GitLab repositories to Jira projects, enabling you to monitor branches, commits, and pull requests directly within Jira. By following this guide, you can leverage the combined power of GitLab and Jira to streamline your workflow, enhance visibility, and improve productivity.

You can access our Git integration app for Jira using the following link: [Git Connector.](https://marketplace.atlassian.com/apps/1236406/git-connector-for-jira-azure-devops-github-gitlab?hosting=cloud\&tab=overview)

{% hint style="warning" %}
The Git Connector app is not required if you're using the GitLab integration app.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FjLPlqGF8Q02otsQFuMdd%2FGetint%20White%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=f4dc12ae-55ac-4d9d-82dd-f1acdd231e01" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a><br></p></figcaption></figure>

### How to Build a Git Integration for GitLab <a href="#how-to-build-a-git-integration-for-gitlab" id="how-to-build-a-git-integration-for-gitlab"></a>

#### 1. Launch the Getint App: <a href="#id-1.-launch-the-getint-app" id="id-1.-launch-the-getint-app"></a>

* Go to **Apps**, open the Git Connector for Jira app, navigate to **Integrations**, click **Create Integration**, and choose **GIT**.
* If you’re using Getint On-Premise, simply open the app, click **Create Integration**, and choose **Sync GIT Repository**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FIMX1Zagem19zcQcdmnmI%2FGIT%20REPOSITORY%20OPTION.png?alt=media&#x26;token=59787ee9-ad10-479e-beee-43c8ed77f008" alt=""><figcaption></figcaption></figure>

#### 2. Create a Connection with GitLab: <a href="#id-2.-create-a-connection-with-gitlab" id="id-2.-create-a-connection-with-gitlab"></a>

* Click the **Connect App** button, and select **GitLab**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FPx1OLCtYbT1beMx2rZuU%2FSelecting%20GitLab%20for%20Git%20Integration.png?alt=media&#x26;token=fee233b9-5040-48b8-bad7-c52d0260cb40" alt=""><figcaption></figcaption></figure>

* Create a connection or select an existing one.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fq5ko2hye5X091CfboWub%2FCreate%20New%20Connection%20or%20Select%20an%20existing%20connection.png?alt=media&#x26;token=1c0c2cdb-dbbb-46c6-84e5-4ea58876166a" alt=""><figcaption></figcaption></figure>

* Tap on **Create a new connection** if you don’t have an existing one.
* Enter your instance URL, and click on **Connect**. Do NOT provide a URL if you are using GitLab Cloud.
* Name the connection, and paste the token generated (create the personal access token following the instructions in this guide: [Connections](https://docs.getint.io/guides/quickstart/connection#gitlab)). Then click **Add**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FpiXSYswfv2pfzLgiCvNL%2FNaming%20your%20connection%20and%20adding%20access%20token.png?alt=media&#x26;token=6c023c8d-f767-4b23-a6a2-a11a99f1be8b" alt=""><figcaption></figcaption></figure>

* Once you've added your details, you'll find your new connection in the dropdown list of available connections. Please select it and click **Connect** to complete the process.

#### 3. Establish a Connection with Jira: <a href="#id-3.-establish-a-connection-with-jira" id="id-3.-establish-a-connection-with-jira"></a>

* Ensure that you are logged in with administrative rights, then click on **Connect App** and select **Jira**. Click on **Create New** to set up a new connection with your Jira instance and enter the URL of your Jira instance.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F95QXAP4ctPtxiVWVk9dU%2FAdd%20the%20URL%20of%20your%20Jira%20instance.png?alt=media&#x26;token=020e7e6b-d584-498c-bda9-f8a2031d36fa" alt=""><figcaption></figcaption></figure>

* Unlike **Continuous Syncs** or **Migrations**, GIT integrations require users to set up OAuth in your Jira instance. Please ensure you have admin permissions; otherwise, you will not be able to set up the OAuth credentials. Then, follow our guide to configure a Jira OAuth at the following: [Connection | Jira OAuth.](https://docs.getint.io/guides/quickstart/connection#jira-cloud-oauth)
* Enter the necessary details to establish the connection.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F4obVTbpw36olFtf5ymeF%2FCreating%20a%20connection%20with%20Jira%20for%20a%20GIT%20integration.png?alt=media&#x26;token=aaff0167-0bb8-4c58-a7d7-a8a29124b5a0" alt=""><figcaption></figcaption></figure>

* After entering your details, your new connection will appear in the dropdown list of available connections. Please select it and click **Connect** to finalize the setup.

#### 4. Building Your Integration: <a href="#id-4.-building-your-integration" id="id-4.-building-your-integration"></a>

* By default, the Git repositories will automatically synchronize with all projects in your Jira instance. However, if you disable this option, you can specify one or multiple projects where this information should be available.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FCJ4eMp5NuhwJXHvj0IVS%2FGitlab%20git%20repository%20integration.png?alt=media&#x26;token=e12c1e7d-41de-42c9-aaaa-85f0c785b328" alt=""><figcaption></figcaption></figure>

* For example, you can pick particular projects based on your company's needs. Next, identify the Git repositories you want to sync. Finally, name your integration and click **Create** in the top right corner of the screen to save it.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FN2yEQWPz3n1o7TrMcsgH%2FSelecting%20different%20Jira%20Projects%20for%20Git%20Integration.png?alt=media&#x26;token=f37bc00a-2190-453e-936b-bf9b047f1cc9" alt=""><figcaption></figcaption></figure>

* After creating your integration, it will be readily available in the Integrations section within Workflows, identified by a code icon.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FrcGeRf1yMfNmFtEOZXr6%2FWhere%20to%20find%20the%20GIT%20integrations.png?alt=media&#x26;token=4363123a-ed21-4f57-8563-300fe9d18aff" alt=""><figcaption></figcaption></figure>

* If you did not install the Git Connector app as instructed at the beginning of the article, you will encounter an error like the one shown below:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FFlVRS1y9icaE4XL8wRYb%2FSync%20error%20due%20to%20missing%20Git%20connector.png?alt=media&#x26;token=7054f8bd-cd0e-4b86-b29b-efbeab5c2ee3" alt=""><figcaption></figcaption></figure>

#### 5. Test the Integration and Sync Your Branches <a href="#id-5.-test-the-integration-and-sync-your-branches" id="id-5.-test-the-integration-and-sync-your-branches"></a>

* To start syncing branches, use the Jira task ID as a prefix for the branch, commit, and pull request names. For branch names, only underscores or dashes can be used instead of spaces. For example **ED-33**\_**feature\_user\_authentication**.
* For instance, if you are syncing an item with the Jira ID **ED-33**, your branch should be named **ED-33** followed by the branch name, as shown below:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FU2ZOqlZ52EPEwhYQpXqG%2FGitLab%20repository%20integration.png?alt=media&#x26;token=0882d758-0e87-4652-8941-16bc791e2b09" alt=""><figcaption></figcaption></figure>

* If you fail to use the correct naming prefix for branches and commits, you will encounter an error similar to the one shown below:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F3IKnhL7xiBYLFci3xbkk%2FGit%20sync%20error.png?alt=media&#x26;token=a3e94d63-4c74-4a8f-ab12-a4de3d7c82fb" alt=""><figcaption></figcaption></figure>

* The GitLab repository details of your Jira items will be available in the Development field. Refresh the page if you don’t see any changes to this field.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FDXqZ6SM0Ns1pkmHVCOEn%2FDevelopment%20field%20for%20gitlab%20integration.png?alt=media&#x26;token=4b6b3cad-7381-4911-97f6-2c90985823d8" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Depending on your Project template, the Development field may not be visible. In such cases, you must either add the field by modifying the issue layout or switch to a different template.
{% endhint %}

* Clicking on this field allows you to effortlessly access all the information fetched from the GitLab Repository.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FrFzEFQjm9HpdfdWMl7A7%2FInside%20the%20Development%20field%20in%20Jira.png?alt=media&#x26;token=335edbdd-8243-42ab-aa4a-688c62d958c1" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Getint enables the synchronization of Repositories, Branches, Commits, and Pull Requests. However, please note that changes cannot be submitted from Jira to the Git repository. The synchronization of repository information is one-way from GitLab.
{% endhint %}

### Conclusion <a href="#conclusion" id="conclusion"></a>

With this comprehensive guide at your disposal, you can seamlessly integrate GitLab repositories with Jira and unlock the full potential of efficient repository management. If you need any help or have any questions along the way, don't hesitate to reach out to us here.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Azure DevOps Asana integration

Managing projects across multiple platforms can be difficult, especially when teams rely on different tools for tasks and development. The Asana–Azure DevOps integration with Getint connects these systems, enabling real-time synchronization of tasks, statuses, and project data for a unified workflow. Built for simplicity and flexibility, it lets teams collaborate effectively without disrupting existing processes. This guide offers a step-by-step approach to setting up the integration, helping you improve coordination and enhance project management.

***

### Setting Up Your Asana-Azure DevOps Integration: Step-by-Step Guide <a href="#setting-up-your-asana-azure-devops-integration-step-by-step-guide" id="setting-up-your-asana-azure-devops-integration-step-by-step-guide"></a>

#### **1. Access the Getint App:** <a href="#id-0.-access-the-getint-app" id="id-0.-access-the-getint-app"></a>

* Navigate to Getint and sign in.
* Select "Create Integration" then "Continuous Sync" or "Migration" based on your requirements.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FsBEY8rF6KIh9H4ePEd37%2FCreating%20an%20integration.png?alt=media&#x26;token=0fd82721-d3e3-4a0d-b6b1-f8b1414481ec" alt=""><figcaption></figcaption></figure>

#### 2. Connect to Asana <a href="#id-2.-connect-to-asana" id="id-2.-connect-to-asana"></a>

* Select an existing Asana connection, or create a new connection if this is your first time. Follow the guide [here](https://docs.getint.io/guides/quickstart/connection#asana)on how to create the Asana Token.
* Click "Select App" and choose Asana. Choose "Create New" to establish a new connection.
* Name your connection, use the token generated, then select "Add."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F4wFLjbCda6qQYTOpp1xK%2FCreate%20a%20connection%20with%20Asana.png?alt=media&#x26;token=0161653a-2387-459c-be41-8c837fd35584" alt=""><figcaption></figcaption></figure>

* Once the connection is established, choose the workspace and project you want to connect to from the dropdown menu.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FWtoIFZicT3MwE3Bk8dQ7%2FSelect%20the%20project%20from%20the%20dropdown%20menu.png?alt=media&#x26;token=7e162960-1137-4ad8-9169-92adcb559fd0" alt=""><figcaption></figcaption></figure>

#### 3. Connect to Azure DevOps <a href="#id-3.-connect-to-azure-devops" id="id-3.-connect-to-azure-devops"></a>

* Log in to the Azure DevOps app as an admin. Follow the steps in our "[Connections](https://docs.getint.io/guides/quickstart/connection#azure-devops)" guide to generate the token.
* Select "Azure DevOps" as the connection application, then choose "Create a new connection." Enter the URL for the connection and click "Next."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FqZSWGuVhqdbgb4Kue9DF%2FConnect%20to%20Azure%20DevOps.png?alt=media&#x26;token=cafcba14-268c-40c6-aaa1-9b9b5d1a5a4d" alt=""><figcaption></figcaption></figure>

* Provide a name for the connection, enter your email, and paste the token generated in the previous steps. Click "Add" to complete.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FozqsQv1CS8Weut4werqF%2FEnter%20your%20credentials.png?alt=media&#x26;token=b032ef5f-24c6-4d89-a45c-dd84d8f44200" alt=""><figcaption></figcaption></figure>

* Once the connection is established, select the Azure DevOps project you want to synchronize from the dropdown menu and click connect.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FnWsJOhHerCbIXw6bK4Cv%2FClick%20connection%20to%20establish%20the%20connection%20with%20Getint.png?alt=media&#x26;token=4f8535e5-7140-4f9a-a676-7539eaf7267a" alt=""><figcaption></figcaption></figure>

#### 4. Configure Type Mapping <a href="#id-4.-configure-type-mapping" id="id-4.-configure-type-mapping"></a>

Consider using the "Quick Build" beta feature for automated type and field mapping, which can streamline the setup process.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FhnOzfFIMpFRMtcAi69N9%2FUse%20quickbuild%20for%20auto%20type%20mapping.png?alt=media&#x26;token=f02113ce-0dce-43a0-8259-cc8ada28fd80" alt=""><figcaption></figcaption></figure>

* Map task types you wish to sync between Asana and Azure DevOps. This could include:
  * Asana *Tasks* → Azure DevOps *User Stories*.
  * Asana *Sub-Tasks* → Azure DevOps *Tasks*.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fb3VsJhsskhriDhp5VWgP%2FAdapting%20your%20type%20mappings.png?alt=media&#x26;token=e83f4f60-425b-4216-bdbf-6559fb46a638" alt=""><figcaption></figcaption></figure>

This flexibility allows you to adapt the integration to your team's workflow needs.

#### 5. Field Mapping <a href="#id-5.-field-mapping" id="id-5.-field-mapping"></a>

Review or manually map the fields you'd like to integrate and sync, such as title, description, assignees, custom fields, and more.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FnQqgbxatRqpOhyQNEx6Y%2FField%20mapping%20Azure%20Asana.png?alt=media&#x26;token=5facdae2-7dcf-4a63-9368-4d1eabfd81c0" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If you don’t see a field you need, please reach out to our [support team](https://getint.io/help-center) for assistance! We’re constantly working to enhance your experience.
{% endhint %}

#### 6. Name and Finalize the Integration <a href="#id-6.-name-and-finalize-the-integration" id="id-6.-name-and-finalize-the-integration"></a>

Assign a name to your integration and click "Create" to initiate it.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Ft4v0K1IgZMqMGQBoRgF8%2FName%20and%20finalize%20the%20integration.png?alt=media&#x26;token=74a76a26-54a7-4ad7-af77-14f262002ae5" alt=""><figcaption></figcaption></figure>

### Advanced Configuration Options <a href="#advanced-configuration-options" id="advanced-configuration-options"></a>

#### 7. Configure Statuses Sync <a href="#id-7.-configure-statuses-sync" id="id-7.-configure-statuses-sync"></a>

Enable status synchronization to match the progress stages between Asana and Azure DevOps:

* Go to the "Statuses" tab, enable sync, and define mappings:
  * Asana *Done* → Azure DevOps *Closed/Resolved*.
  * Asana *In Progress* → Azure DevOps *Active*, etc.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FKfndRfowQMJSM345ff71%2FStatus%20mapping%20configuration.png?alt=media&#x26;token=97b83f82-abf6-40c6-8540-dd055c05d2c3" alt=""><figcaption></figcaption></figure>

#### 8. Sync Comments and Attachments <a href="#id-8.-sync-comments-and-attachments" id="id-8.-sync-comments-and-attachments"></a>

To synchronize comments and attachments, navigate to the "Comments & Attachments" tab, enable the setting, and configure options to tailor the integration to your team's workflow needs.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FuLjKBnMNA62ONWobHjeH%2FSync%20comments%20%26%20attachments.png?alt=media&#x26;token=d098f689-5336-4b33-bcc7-f4eb06da12a8" alt=""><figcaption></figcaption></figure>

#### 9. Assignee Mapping <a href="#id-9.-assignee-mapping" id="id-9.-assignee-mapping"></a>

Map and match assignees according to your desired configuration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F0tUkdzK43HtjZrgqlBhY%2FMapping%20assignees.png?alt=media&#x26;token=e3752c76-5f26-482f-8432-21ff49022c6e" alt=""><figcaption></figcaption></figure>

#### 10. Filtering: <a href="#id-10.-filtering" id="id-10.-filtering"></a>

It is possible to filter the synchronization to have it customized for your needs and requirements.

**UI Filtering Option:**

* Click on the filtering icon next to the app icon in your integration. This filter will apply to that side of the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FGgHBfpjoy4NYOV0p2IuZ%2FUI%20filtering%20configuration.png?alt=media&#x26;token=c508c4f1-3d5b-4709-95fb-8bab07075a0a" alt=""><figcaption></figcaption></figure>

* Choose whether the filter applies to *"All," "New,"* or *"Synced"* items:
  * **New items:** The filter will only apply to new items, while already-synced items continue to sync and update.
  * **Synced items**: The filter will apply only to items that have already been synced, updating them based on the filter criteria.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F0JLD17YhpHOtbC86kEnS%2FSetup%20your%20filters.png?alt=media&#x26;token=fedf202d-ca07-4157-a5d6-07de8253ca18" alt=""><figcaption></figcaption></figure>

* Select your options and enter values for the filter. As needed, you can apply multiple filter options for each field. Once your filters are set, click "Apply" and "Save" the integration.

### Need Assistance? <a href="#need-assistance" id="need-assistance"></a>

Leverage the Asana-Azure DevOps integration by Getint to optimize your task management and project workflows. For further assistance or to request support, please visit our [Help Center](https://getint.io/help-center).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Jira Airtable integration

**Introduction**

The Jira–Airtable integration with Getint provides a practical solution for project and data management. It combines Jira’s structured task tracking with Airtable’s flexible database features, creating a single interface that supports efficiency and collaboration. This guide explains how to set up the integration step by step, helping teams improve productivity, maintain data accuracy, and achieve real‑time synchronization aligned with business needs.

### Step-by-Step Setup Guide <a href="#step-by-step-setup-guide" id="step-by-step-setup-guide"></a>

**1. Launch Getint within Jira**

* Navigate to "Apps" and select "Airtable integration for Jira."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FKmva55Sdg26TS9rqSHen%2Fimage-20240626-144813.png?alt=media&#x26;token=29d9fba4-4814-44a7-8f82-e91f538f41bb" alt=""><figcaption></figcaption></figure>

**2. Create Integration**

* Click "Continuous Sync" or "Migration."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FvBdztsn0Y6eU6q8qdVe7%2Fimage-20240619-115231%20(1).png?alt=media&#x26;token=623d4c18-950a-4492-970e-111fe7fb1e5e" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
**Note:** The "Continuous Sync" functionality ensures consistent data integration, which is Getint's standard operation mode. For transferring pre-existing data, consider the "Migration" feature available as a premium option. For more details, contact our support team.
{% endhint %}

**3. Token Generation (Password for Jira Cloud)**

* For Jira Cloud, generate a Jira token. This token will act as your password:
  * Go to Atlassian Account Settings.
  * Navigate to Security and generate an API token, then use this token as the password for Jira integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FVYN4z7XPyRqTKAPOUqFD%2FCreating%20API%20token.png?alt=media&#x26;token=028cb340-303b-49c8-b828-5b9affa50892" alt=""><figcaption></figcaption></figure>

**4. Choose the Apps and Establish Connections**

* Ensure you are logged in as a user with admin rights, click on "Select App" and choose Jira.
* Select "Create New" to establish a new connection with your Jira instance and add the URL of your Jira instance (omit the trailing "/ ").
* Enter the login credentials of the admin user.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FCjhtyzJGdkbyM45qdwgq%2Fimage-20240620-165801%20(1).png?alt=media&#x26;token=31a83bbb-7c3c-402b-8a17-6bbdaa8aa0ad" alt=""><figcaption></figcaption></figure>

**5. Select the Jira Project**

* Once the connection is established, choose the Jira project you want to connect to from the dropdown menu.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FjfVXiWf993wn6D81YD11%2Fimage-20240620-170315%20(1).png?alt=media&#x26;token=dd022d94-7285-449f-9f03-6cc1d1ba9ff0" alt=""><figcaption></figcaption></figure>

**6. Generate Airtable Token**

* Go to Airtable, ensure that you have created the "Last Modified Time" column, then create the Access Token. Follow the steps [here](https://docs.getint.io/guides/quickstart/connection#airtable) for the token with the correct scope.

**7. Connect to Airtable**

* If no connection is established yet, create a new one.
* Use the Airtable token generated as a password. Then select the space and table.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FfQLYQXjlJa46f2QhJmHM%2Fimage-20240628-114059.png?alt=media&#x26;token=6a62e53e-1197-4aab-80e6-8d846156eb39" alt=""><figcaption></figcaption></figure>

**8. Type Mapping**

* Map Jira issue types such as Task, Bug, Epic, and Story to Task in Airtable.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FpaJXNahmmbbZtoXSjoMh%2Fimage-20240628-114750.png?alt=media&#x26;token=bca52421-c3f8-4ab0-981c-cf17d0648273" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Please note that at the moment, we only support the "Task" issue type for this integration.
{% endhint %}

**9. Field Mapping**

* Designate specific fields for synchronization and map them accordingly.
* If you need fields that are not appearing for your integration, including labels or custom fields, contact us at <https://getint.io/help-center>. We continually improve our product based on user feedback and value your insights.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FEMICceNkxy8Al4Jk3x6C%2Fimage-20240628-114709.png?alt=media&#x26;token=5373b805-4bf2-49bc-84b5-216ad411f509" alt=""><figcaption></figcaption></figure>

**10. Finalize Integration**

* Name your project and click "Create" to finalize the integration setup.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fc5YXwfyo82bT8HNuSwpY%2FUntitled%20design%20(11).jpg?alt=media&#x26;token=97ce5844-4ea5-4ff3-ac33-179b47696cdf" alt=""><figcaption></figcaption></figure>

**11. Filtering:**

It is possible to filter the synchronization to have it customized for your needs and requirements.

**UI Filtering Option:**

* Click on the filtering icon near the app icon in your integration. This will apply to that side of the integration.
* Select if the filtering applies to All, New, and Synced items.
* Note that if the option *"New items"* is selected, the filtering will apply only to the new items, and the already synced items will continue to sync and update. If the option *"Synced items"* is selected, only the already synced items will be updated based on that filter.
* Choose the options and add the value for the filter. It is possible to filter more than one option for each field.
* Select "Apply" once you have created the filters and "Save" the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FWEpjf30CfNioo4TCHbQj%2Fimage-20240710-095555.png?alt=media&#x26;token=071da8b3-df1f-4ebe-8701-56b926b86e91" alt=""><figcaption></figcaption></figure>

**12. Test the Integration**

To ensure everything is working correctly, create tasks and go to the reporting section to verify that all syncs are functioning as expected. If you encounter any issues, please contact our support team for assistance.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F6q0zqpHCMoqgo7af5Ldm%2Fimage-20240710-095044.png?alt=media&#x26;token=5c5e5f9e-b2d7-4b23-8c7c-88dc6df9bd3f" alt=""><figcaption></figcaption></figure>

Leverage the Jira-Airtable integration by Getint to optimize your project management and data processes. For further assistance or feedback, contact us at our [Help Center](https://getintio.atlassian.net/servicedesk/customer/portals).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Jira Asana integration

The Jira Asana integration provided by Getint allows users to seamlessly sync their project data between the two platforms.

Integrate Jira with Asana using Getint to enhance workflows with other teams, facilitate effective communication among teams, companies, and customers, or efficiently migrate to Jira while maintaining your previous backlog.

Asana and Jira are vital tools for companies, offering distinct advantages in project management and collaboration. Asana's user-friendly interface and flexible task management complement Jira's robust issue-tracking and development capabilities. Integrating both platforms through Getint streamlines communication, synchronizing tasks and timelines in real time. This synergy enhances productivity, fosters collaboration, and ensures alignment across teams and departments, driving success in today's competitive landscape. With Getint, you can integrate Asana to your Jira Cloud, Jira Data Center, or On-Premise seamlessly and synchronize tasks across your workspace with efficiency.

To set up two-way Jira Asana Integration, follow the video tutorial below:

{% embed url="<https://youtu.be/PBKYO99Enls>" %}

### Prepare your workspaces, and check the fields you would like to integrate to the counterpart

Different projects have different requirements, with this in mind you may like to track and integrate specific information for your project.

Asana has a multitude of custom field types that can be added to your board, make sure to have your board configured beforehand with all the custom fields you would like to integrate so that when creating the integration, you can visualize them for mapping and map them according to their counterpart in Jira.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FaBWn6VQNSrwt54HibJi3%2Fimage.png?alt=media&#x26;token=a011646c-c811-4ec5-b862-bb449ddc7688" alt=""><figcaption><p>Custom field types creation screen from Asana</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FH84fVATjoIyUiMBMM3ro%2Fimage.png?alt=media&#x26;token=b5e5fb56-5bf1-4af3-b411-fe7227f7c77c" alt=""><figcaption><p>Custom field types added to an Asana’s board</p></figcaption></figure>

### **Create the integration and add the connections** <a href="#create-the-integration-and-add-the-connections" id="create-the-integration-and-add-the-connections"></a>

**Access the Getint App in Jira.**

1. Here we are going to select the Jira - Asana Integration app for this integration, then create the connection for Jira with Jira’s API token and create the connection for Asana with Asana’s Access token. Remember to give a name to your integration, then create it.

{% embed url="<https://www.loom.com/share/4942cde250484e999d3af6200564275b?sid=7e5e29f6-fc6a-47ef-8fe8-11b2c77ad1e0>" %}

1. Navigate to Jira, go to “Apps”, and select the “Jira - Asana Integration app” (If you still don’t have the trial for this application, please check it at the Atlassian Marketplace on the [Asana Jira integration by Getint \[2-way sync + migration\] | Atlassian Marketplace](https://marketplace.atlassian.com/apps/1223932/asana-jira-integration-by-getint-2-way-sync-migration?hosting=cloud\&tab=overview)\
   ![](https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMhJiFCNXNmGvxWtcrhYp%2Fimage.png?alt=media\&token=47cda971-646c-4cf9-85e9-e20e88bd69ab)
2. Select “Create Integration” then “Continuous Sync” or "Migration" based on your requirements.<br>

   <figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FUI8Mr1JOPzNcfspi8BDj%2Fimage.png?alt=media&#x26;token=5b8f86e7-56f1-4537-93bf-8d01c57af6fa" alt=""><figcaption></figcaption></figure>

**Create the tokens for each workspace, and create the connections right after**

To ensure the integration functions properly, grant access to both environments using their respective access tokens.

You can learn how to create the access token on **Jira** with the below, but you can also follow this article: <https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/>

{% embed url="<https://www.loom.com/share/a6bcc913aef240f59ccb278e010f584e?sid=abe94819-52a8-455d-8a72-3b10da384d5c>" %}

In the video below you can learn how to create an access token for **Asana,** you can also read the instructions in the Asana article: [Personal access token](https://developers.asana.com/docs/personal-access-token)

{% embed url="<https://www.loom.com/share/3f4f209accd846eca989aedeb76357f6?sid=3d0080b8-0b11-4eb1-b6c9-cfde98f570dd>" %}

### **Add mapping fields and configure them** <a href="#add-mapping-fields-and-configure-them" id="add-mapping-fields-and-configure-them"></a>

Create a task ↔︎ task, and subtask ↔︎ subtask task type mapping, add your desired fields and define the sync direction (unidirectional or bi-directional) with the arrows. and configure your task status synchronization.\
Save your integration at the end:

{% embed url="<https://www.loom.com/share/f16575ca0ced489f9ccab8c600ef69c1?sid=52d5a050-f04e-418b-83f6-cb735abcd9c7>" %}

For Asana, we selected “Section” as a reflection to Jira tasks statuses, then applied the change, left the screen and re-entered it for the statuses to be displayed.\
**Note that the options at the left are form Jira, and the options from the right are from Asana.**

Click on the “Start with mapping types” button, and the “Map Your Types for a Seamless Integration” tab should pop up:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FHMd9P4EYrDw1wfqwheCf%2Fimage.png?alt=media&#x26;token=4747176f-20d0-4f56-bcc9-6c1c83f30955" alt=""><figcaption></figcaption></figure>

Map task to task, and you can add another mapping type with subtask to subtask:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FeikrNmdb8iybyKaGjyrb%2Fimage.png?alt=media&#x26;token=0017639b-2f98-41c0-b4bb-2f0efbb124d4" alt=""><figcaption></figcaption></figure>

Click on the newly created type mapping to enter the field configuration, then start mapping your fields:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FBHg4Zbs6ejv9sosNJ2Rn%2Fimage.png?alt=media&#x26;token=80d46e5c-c2d3-4695-8213-b324d689103f" alt=""><figcaption></figcaption></figure>

Use the dropdown menus to map your fields, for example, Assignee to Assignee, Priority to Priority, Title to Title, and so on, click on the arrows in the middle to define the synchronization flow (updates only unidirectionally from left to right, from right to left, or bidirectional)

**Click the “Apply” blue button at the right bottom to save the changes made.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fr649gGrpEw0nYgFnVS1H%2Fimage.png?alt=media&#x26;token=fde0b203-e204-49e7-9331-ef021c733fc8" alt=""><figcaption></figcaption></figure>

Map the statuses, use the dropdowns to map them according to your organization parameters, and click Apply to save the changes made

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FbsoTkbOgeFT6AqqExgm0%2Fimage.png?alt=media&#x26;token=ae9583f5-2df4-42fb-9c95-d7f60d97fbd6" alt=""><figcaption></figcaption></figure>

Name your integration, then create it

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fqxr2TrlxlSRi0cGwql67%2Fimage.png?alt=media&#x26;token=3f325f81-22c4-44e3-ae6b-4b571463ab9b" alt=""><figcaption></figcaption></figure>

### **Create a test ticket on both sides to check if it’s working** <a href="#create-a-test-ticket-on-both-sides-to-check-if-its-working" id="create-a-test-ticket-on-both-sides-to-check-if-its-working"></a>

**Create a ticket or tasks on each side to test the integration**:\
\
Add a comment or attachment, and change the task status on one side to ensure the corresponding fields are captured correctly on the other:

{% embed url="<https://www.loom.com/share/32fcee4152c04efc9ef2720026e85545?sid=06f3a4cd-25e6-493f-be4a-261ac7ec6751>" %}

The integration has been successfully set up, the tasks are synchronizing through both workspaces and assigning correctly the data from the fields mapped.

{% hint style="info" %}
In case you bump into an error while trying to integrate your software, please raise a ticket at our support channel: <https://getintio.atlassian.net/servicedesk/customer/portals>\
(You can also email us at <support@getint.io>).
{% endhint %}

# Jira - Asana: Subtasks Synchronization

Making sure your tasks and subtasks play well between Jira and Asana is vital for smooth teamwork. This step-by-step guide will walk you through the process, making it easy to map, configure, and sync tasks and subtasks seamlessly.

### **Mapping Tasks and Subtasks:**

1. **Task and Subtask Mapping:**
   * Ensure tasks and subtasks are appropriately mapped between Jira and Asana. Match their counterparts in both tools for effective synchronization.
2. **Enable the Synchronization:**
   * Click on the subtasks mapping, navigate to the hierarchy section, and select "Synchronize Subtasks relationship."
   * Enable the synchronization for the Subtasks relationships.
   * Configure subtask relationships in the dropdown menu. Decide if they should sync with their counterpart or get linked to a specific parent task by providing its ID.
   * Click "Apply" and "Save" to apply the changes to the integration.

{% embed url="<https://youtu.be/WOX4mTKXhus>" %}

1. **Initiating Sync for Subtasks:**
   * By configuring the settings, any new subtasks will be automatically synchronized with their parent tasks on Jira and Asana.
2. **Handling Existing Items:**
   * If the subtasks were created before this synchronization, it will be necessary to perform a migration to ensure that the older subtasks are migrated. Follow the necessary migration steps to create the relevant link.

**Conclusion:** Synchronizing tasks and subtasks in the Jira<>Asana integration improves collaboration and ensures consistent project management. By mapping, configuring relationships, and enabling synchronization, you create a seamless workflow between the two platforms.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

&#x20;

# Jira Azure DevOps integration

Integrating Jira (Software/Service Management) and Azure DevOps (Cloud/OnPremise) is essential for optimizing workflows. Getint's integration bridges the gap between tracking project milestones in Jira and managing development tasks in Azure DevOps. Whether you're using Jira Cloud, Data Center/Server, or On-Premise, this guide will help you set up an efficient information flow between these platforms. Enhance your productivity and collaboration across teams of all sizes by following this guide.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FASVDQPea4wMrFSisW9nM%2FAzure%20DevOps%20Jira%20Integration%20App.png?alt=media&#x26;token=448b36f1-9fc0-4f40-ac5d-c0e831c7bcfc" alt=""><figcaption><p><a href="https://marketplace.atlassian.com/apps/1223931/azure-devops-integration-for-jira-azure-devops-connector?hosting=cloud&#x26;tab=overview">Check out our Azure DevOps integration app on the Atlassian Marketplace</a></p></figcaption></figure>

#### Step-by-Step Setup Guide

**1. Access the Getint App in Jira**

Navigate to Jira, go to "Apps," and select "Jira - Azure DevOps Integration."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FUb7y0bNix6nUKR2PPVx4%2Finstalling%20jira%20azure%20app.png?alt=media&#x26;token=6aa644a9-703e-4972-9d3b-e0d743e11a64" alt=""><figcaption></figcaption></figure>

**2. Create Integration**

* Choose "Continuous Sync" for ongoing data synchronization or "Migration" if you need to transfer existing data.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FauPLTmwoTx7ZzZdV3qG6%2FSelecting%20Continuos%20Sync%20or%20Migration.png?alt=media&#x26;token=cfb3998d-5690-48a5-9d70-6e2f4c361e74" alt=""><figcaption></figcaption></figure>

**3. Token Generation (Password for Jira Cloud)**

For Jira Cloud, generate a Jira token. This token will act as your password:

* Go to Atlassian Account Settings.
* Navigate to Security and generate an API token, then use this token as the password for Jira integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FkN1AECBGj6ezWCzEeJgt%2Fimage-20240812-171049.png?alt=media&#x26;token=d5eb3df0-41a2-4ba6-932a-365dfb742763" alt=""><figcaption></figcaption></figure>

**4. Choose the Apps and Establish Connections**

* Ensure you are logged in as a user with admin rights, click "Select App" and choose Jira.
* Select "Create New" to establish a new connection with your Jira instance and add the URL of your Jira instance.
* Enter the login credentials of the admin user.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fck3TsUWGgXbjMlm3Rq1R%2Fimage-20240715-151822%20(1).png?alt=media&#x26;token=4199e5bf-966e-401f-99ca-12c089753b75" alt=""><figcaption></figcaption></figure>

**5. Select the Jira Project**

* Once the connection is established, choose the Jira project you want to connect to from the dropdown menu.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FaLzTCzZZK2bSl5F1Zn17%2Fimage-20240620-170315%20(2)%20(1).png?alt=media&#x26;token=4628072c-0fa4-4410-9feb-b5a5fefa2855" alt=""><figcaption></figcaption></figure>

**6. Connect to Azure DevOps**

* Select the Azure DevOps app and tap on "Create a new connection." Use the Personal token created following the instructions in the guide: [Connections](https://docs.getint.io/guides/quickstart/connection#azure-devops).
* Tap on "Connect."
* Name the connection, input your email, and paste the token generated. Then click "Add."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FRZktv7TnQ801tyYaJH2X%2Fimage-20240812-171756.png?alt=media&#x26;token=a4e80115-8f3e-4900-af99-4bfde8dff19f" alt=""><figcaption></figcaption></figure>

* Select the Azure DevOps connection and choose the database you want to synchronize.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FXLeRynMnAO0OIaj3oO7A%2Fimage-20240812-171610.png?alt=media&#x26;token=7d851352-ce4a-40fc-9feb-43e3680f7e51" alt=""><figcaption></figcaption></figure>

**7. Map Types**

* Map the Jira issue types you want to sync with Azure DevOps tasks, such as mapping an Azure DevOps task to a Jira issue or a Jira bug.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FBqjeeVDE6niPRQu1a1y4%2Fimage-20240812-172213.png?alt=media&#x26;token=02c3fa3e-3900-4f48-bc0a-12e4417ea69c" alt=""><figcaption></figcaption></figure>

* Consider using the "Quick Build" beta feature for automated type and field mapping, which can streamline the setup process. Quick Build is currently in the beta stage; if you have feedback or questions about it, please contact our [support.](https://getintio.atlassian.net/servicedesk/customer/portals)

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F0wB95VbhZiq6LTFyyByM%2FUntitled%20design%20(25).jpg?alt=media&#x26;token=1808f599-ff84-4c6c-a720-b7a1966aea6e" alt=""><figcaption></figcaption></figure>

**8. Field Mapping**

Review or manually map which fields to integrate and sync within supported mapped types, make any necessary modifications, and hit apply.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FlNNfeI3P5IWZ7ucyPi2i%2FUntitled%20design%20(24).jpg?alt=media&#x26;token=fb626577-0347-4a8c-8377-24ad17f7e785" alt=""><figcaption></figcaption></figure>

#### Advanced Settings <a href="#advanced-settings" id="advanced-settings"></a>

**9. Comments**

If needed, enable the integration and synchronization of comments.

* Filter the comments with the criteria that suit you. Make them private/public or use the preferred attributes, such as created date or author.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FEm9fPbbacf4s4DTVK7rQ%2FCaptura%20de%20tela%202024-08-12%20143828.png?alt=media&#x26;token=7ba85ffc-4580-42cb-8a00-e80ccd2ce155" alt=""><figcaption></figcaption></figure>

**10. Statuses Mapping**

Enable status mapping, then map the statuses as desired.

* Specify the Azure DevOps field that will keep the status data from Jira, ensuring fields in Azure DevOps mirror your Jira setup (e.g., Done - Closed, Open - Active).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FAsN0MViXkpbc9UTvk1mA%2Fimage-20240812-174143.png?alt=media&#x26;token=176df56f-eba5-4642-b227-c0ba1b930441" alt=""><figcaption></figcaption></figure>

#### **Finalize Integration**

**11. Name the Integration and Click "Create"**

* Name your integration and click "Create" to finalize the setup.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FkREPm5UYV7kAcY78UPmj%2FUntitled%20design%20(26).jpg?alt=media&#x26;token=05ebe7e1-a328-40c8-8622-62779b9f489a" alt=""><figcaption></figcaption></figure>

**12. Filtering**

It is possible to filter the synchronization to have it customized for your needs and requirements.

**UI Filtering Option:**

* Click on the filtering icon near the app icon in your integration. This will apply to that side of the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F0QFYm1XlWIqLz6XWo3Oj%2FUntitled%20design%20(27).jpg?alt=media&#x26;token=da0c4f07-cbd0-485b-a063-e8c464f09cc1" alt=""><figcaption></figcaption></figure>

* Select if the filtering applies to All, New, and Synced items.
* Note that if the option "New items" is selected, the filtering will apply only to the new items, and the already synced items will continue to sync and update. If the option "Synced items" is selected, only the already synced items will be updated based on that filter.
* Choose the options and add the value for the filter. It is possible to filter more than one option for each field.
* Select Apply once you have created the filters and "Save" the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F7o3MGnkJ4plqvEbR36Xi%2FUntitled%20design%20(28).jpg?alt=media&#x26;token=a62bf43b-3860-4058-95fc-af881818be4f" alt=""><figcaption></figcaption></figure>

**13. Test the Integration**

To ensure everything is working correctly, create tasks and go to the reporting section to verify that all syncs are functioning as expected. If you encounter any issues, please contact our [support team](https://getintio.atlassian.net/servicedesk/customer/portals) for assistance.

#### Conclusion <a href="#conclusion" id="conclusion"></a>

Leverage the Jira-Azure DevOps integration by Getint to optimize your project management and development processes. This seamless integration enhances collaboration and productivity, ensuring that all tasks and milestones are accurately tracked and managed across platforms. Please contact our [Support Team](https://getint.io/help-center) or [Schedule a Demo](https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team), if you require further assistance.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# How to Setup a Connection with Azure DevOps On-Premise

Connecting your On-Premise infrastructure with Azure can significantly enhance your organization’s capabilities by leveraging cloud resources while maintaining control over your local environment. With this detailed article, you can establish a connection between your Azure DevOps On-Premise infrastructure and any of our supported tools.

### Requirements and Recommendations <a href="#requirements-and-recommendations" id="requirements-and-recommendations"></a>

Before you begin, ensure you have the following:

* Administrative access to your Azure on-premise environment and the other app you’re integrating.
* Necessary permissions to create and manage projects, types, and fields within the applications.
* Service accounts with the required privileges for integration. It is not recommended to use personal accounts to build your integration. Additionally, it is important to note that comments are added as the user you chose to create the connection. The original author will still appear in the comment footer, but it will be attributed to the user who established the connection.

### Establishing the Connection <a href="#establishing-the-connection" id="establishing-the-connection"></a>

1. Launch Getint and look for the **Azure DevOps** in the apps selection.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FdbIaiz12h2aQFXNje2hM%2FSelecting%20Azure%20DevOps%20as%20the%20tool%20for%20connection.png?alt=media&#x26;token=fcdadf81-4c24-4ea0-bd3b-9c376658d420" alt=""><figcaption></figcaption></figure>

1. Click **Create New Connection.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FRzRUDblWqVgV4R0Vc6Mz%2FCreate%20connection.png?alt=media&#x26;token=48c76d46-65ae-49d4-98d4-df4d4cf1457b" alt=""><figcaption></figcaption></figure>

1. Add the **URL** of your server/deployment. Please ensure you use only the main **URL** without any additional information, such as project destinations, and so on.
   * These are examples of how URLs should be entered:
     * `https://mytfs.internal.com`
     * `http://1.32.312.32`
     * `https://devops.local:8080/tfs`
     * `http://10.0.0.1:8080/tfs`
   * Please avoid entering URLs this way:
     * `https://devops.local:8080/tfs/Collection/Project`
     * `http://10.0.0.1:8080/tfs/tfs/DefaultCollection/Project`
     * `http://1.32.312.32/DefaultCollection/Project`
     * `https://mytfs.internal.com/SomeCollection/`

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FtNsL51yURFldS9jCyTOR%2FURL%20for%20connection.png?alt=media&#x26;token=ee6a2941-4fbb-4d9d-9112-445fba3dde17" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
If the URLs are not entered correctly, the tool will display an error message, and the connection will not be established.
{% endhint %}

1. Enter the connection details such as the **Connection Name, Collection Name, Username, Password / Personal Access Token**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FccqQr6usvwRG6n2op6m9%2FConnection%20to%20Azure.png?alt=media&#x26;token=62b89b45-1927-464a-8db6-bc7a665ca303" alt=""><figcaption></figcaption></figure>

1. You can create your **Personal Access Token** by going to the **Security** settings in your Azure Server.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FqQHJ23zcVnx2LJ78FOx8%2FPersonal%20Access%20Token%20creation.png?alt=media&#x26;token=5295b308-c730-4660-95d1-317a7d664311" alt=""><figcaption></figcaption></figure>

1. Navigate to **Personal access tokens** and click on **+** **New Token.** Then, name your token and authorize it for **Full access.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F0f9Yj3S5RErZ2jBv098C%2FGuide%20to%20personal%20access%20token%20setting.png?alt=media&#x26;token=48d63a77-a3cf-4a6e-a1e0-2d38e043c991" alt=""><figcaption></figcaption></figure>

1. Return to the connection screen and paste your new token in the appropriate field. Finally, click **Add** at the bottom right to save this connection.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FXUG2FvIlMluyR06PcVzy%2FEnter%20the%20connection%20details.png?alt=media&#x26;token=9ba331ec-cd95-4ff0-a69a-85b09d459c9c" alt=""><figcaption></figcaption></figure>

1. Your new connection will be available in the **Select Connection** dropdown list when integrating with Azure DevOps.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FjJtPXH0Hzjh44JTLcdqB%2FAzure%20DevOps%20On-Premise%20(1).png?alt=media&#x26;token=594d7d36-38c6-4807-bc71-2dc759dd9482" alt=""><figcaption></figcaption></figure>

1. After selecting the connection, you will be prompted to choose the project you will be syncing. Now click **Connect,** and you’ll be ready to start syncing tasks/issues.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F15XI4jFUrRhg4V5zxlbE%2FSelecting%20the%20newly%20created%20connection%20(1).png?alt=media&#x26;token=29370274-9afe-4e8d-808d-0c01e3fd05f7" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If you experience any issues establishing a connection or have any doubts, feel free to contact our support team [here.](https://getint.io/help-center)
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Jira - Azure DevOps: Epics and Subtasks Synchronization

Integrating Jira with Azure DevOps can significantly improve team collaboration and workflows. One of the key aspects of this integration is syncing Epics and Subtasks between the two platforms. This article will guide you through the process of setting up and maintaining subtask synchronization using a third-party tool called Getint.

### How to Map Epics and Subtasks

#### 1. Mapping Epics and Subtasks

* Ensure that Epics and Tasks are mapped accordingly between Jira and Azure DevOps. Match the counterpart items on both sides of the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fdu5Wa1K93MlG6Yq2BOvE%2FEpics%20and%20Subtasks%20synchronization.png?alt=media&#x26;token=402fe976-3e1c-4e1a-9978-0d46d176cb67" alt=""><figcaption><p>Example of the correct order for hierarchy levels.</p></figcaption></figure>

{% hint style="warning" %}
When mapping Epics from Jira, don't forget to also map the **Epic Name** (if available). Otherwise, the epics will fail to create.
{% endhint %}

#### 2. Enable the Epic and Subtask Links

* Open the Task - Task type mapping. Then, click on the **Hierarchy** tab, and check the box to enable the **Epic relationship**. Afterward, display the dropdown option and select the corresponding parent link for both sides.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FXguLyUTlNiWxRBX3EFYa%2FEnabling%20epic%20relantionship%20in%20Jira%20Azure%20DevOps%20integration.png?alt=media&#x26;token=8167ebcf-b4cb-4167-b703-021182428680" alt=""><figcaption></figcaption></figure>

* For Subtasks, access the relevant type mapping. Next, activate the **Synchronize Subtasks relationship**. Finally, open the dropdown menu and choose the **Parent Link** option. Determine whether the subtasks should synchronize with their counterpart or be linked to a specific parent task by providing the task's ID.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FqntZzr8XaABWBdu2ctWA%2FEnabling%20subtasks%20relantionship%20Jira%20Azure%20Integration.png?alt=media&#x26;token=4f109c68-7dde-48b8-ac8d-cfcd3ecedbc0" alt=""><figcaption></figcaption></figure>

* After enabling this feature, any new Epics and Subtasks will be automatically synchronized with their parent/child task on Jira and Azure DevOps.

{% embed url="<https://www.loom.com/share/7df417d3d42042cba54f7115ae042005?sid=65b9aa78-e9cf-4ac7-9560-b6b088c17eae>" %}

* Click **Apply** to submit the changes and save your integration.

#### 3. Considerations to Take

* **Respect hierarchy levels:** Use Quickbuild to automatically align type mappings and create links. For manual integration, order issues correctly to prevent sync errors: **Epics** first, **Stories/Tasks/Bugs** second, and **Subtasks** last.
* **For existing projects:** Move or bulk-move issues in order, starting with Epics, followed by Tasks and Subtasks. This ensures proper sync with existing parents on the other side.

{% hint style="warning" %}
Do not modify the **Hierarchy** options within Epics, as this will break the integration. Only enable relationships for Stories/Tasks/Bugs and Subtasks.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Syncing Dependencies between Jira and Azure DevOps using Getint

1. **Understanding Work Items Links in Azure DevOps:**
   * Azure DevOps offers "Related Work" options for linking tasks, featuring system-defined, process-defined, or user-defined link types. To learn more about how to create a Work link in DevOps, see the guides: [Link work items to objects](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/add-link?view=azure-devops) and [Reference guide for link types](https://learn.microsoft.com/en-us/azure/devops/boards/queries/link-type-reference?view=azure-devops\&source=recommendations).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FEc967yDSN0rlTZpQ5d87%2Fimage.png?alt=media&#x26;token=9d9582d0-55e3-4b0e-974d-9d61e83b45e5" alt=""><figcaption></figcaption></figure>

1. **Syncing Jira-DevOps Dependencies with Getint:**
   * Open the integration tab, and choose the integration.
   * Navigate to Dependencies to configure settings.
   * Align Jira dependencies with their Azure DevOps-related work items links.
   * Click "Apply" and then "Save" to implement changes. The next sync will seamlessly integrate the new dependencies.
   * Getint will then update tasks with the corresponding Work link based on matched fields, applying to new and migrated items. Ensure non-migrated tasks have the necessary link field.

{% embed url="<https://youtu.be/vspK_h3gnDU>" %}

**Important Reminder:**

{% hint style="info" %}
When mapping fields, do not select the "Linked Issues" option in dropdowns. Use the Dependency box for creating dependencies between platforms.

Links will be established only if both items, intended to be linked within the app, have already been synchronized by Getint; otherwise, they will be skipped
{% endhint %}

# Jira ClickUp integration

Integrating Jira with ClickUp using Getint allows teams to manage projects seamlessly across platforms, combining Jira’s robust issue tracking with ClickUp’s dynamic task management. This powerful integration supports both Jira Cloud and Jira Server, enabling real-time data synchronization between Jira issues and ClickUp tasks. Whether you need a one-way or two-way sync, this step-by-step guide ensures you can set up the integration quickly and effortlessly, improving productivity and collaboration across your teams with **enterprise-grade, no-code solutions**.

### **Why Choose Getint for Atlassian Native Integrations?** <a href="#why-choose-getint-for-atlassian-native-integrations" id="why-choose-getint-for-atlassian-native-integrations"></a>

Getint specializes in **secure, SOC 2 Type 2 certified integrations** for enterprise environments, ensuring that data synchronization across platforms like **Jira, Azure, ClickUp, Confluence, and Trello** remains efficient and secure. With **no-code integrations for Jira**, Getint makes it easy for teams to connect platforms without extensive technical knowledge, offering solutions that integrate natively with Atlassian tools.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FDFiMQ5y6jPSGhzwEFQTb%2FGetint%20White%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=f02690b6-d42f-4b2d-ad72-da0b788c6e31" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

### **Step-by-Step Guide to Integrating Jira with ClickUp** <a href="#step-by-step-guide-to-integrating-jira-with-clickup" id="step-by-step-guide-to-integrating-jira-with-clickup"></a>

Here’s how to set up **Jira-ClickUp integration** using **Getint’s real-time sync** solution:

#### **1. Access the Getint App in Jira**

* Navigate to Jira, go to **Apps**, and select **ClickUp Integration for Jira** to start the integration process.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FIzIKcKYk7d5V3OuBFgN5%2FLaunching%20Getint%20Jira%20Clickup%20app%20integration.png?alt=media&#x26;token=1eb11411-c325-44b7-abe7-fa32d89141e1" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Pro tip**: Ensure you’re logged in as an admin user to avoid permission issues during setup.
{% endhint %}

#### **2. Create a New Integration**

* Click **Create Integration** for ongoing sync or **Migration** to transfer existing data.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FBqUsLQI0qqerbaqjn7dy%2FInitiating%20app.png?alt=media&#x26;token=9d227f6a-fab9-4ec1-8e67-179eac97d0da" alt=""><figcaption></figcaption></figure>

#### **3. Token Generation (Password for Jira Cloud)**

* For Jira Cloud, generate a Jira token. This token will act as your password:
  * Go to Atlassian Account Settings.
  * Navigate to Security and generate an API token, then use this token as the password for Jira integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FbmHNJBVnrEaDJIMNvWbB%2FAPI%20Token.png?alt=media&#x26;token=64428dc4-e407-456e-a625-9d00787b2ae8" alt=""><figcaption></figcaption></figure>

#### **4. Choose the Apps and Establish Connections**

* Ensure you are logged in as a user with admin rights, click on "Select App" and choose Jira.
* Select "Create New" to establish a new connection with your Jira instance and add the URL of your Jira instance (omit the trailing "/").
* Enter the login credentials of the admin user.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FoVSRYR0eneTbFvJGYViI%2FChose%20the%20app%20and%20established%20connections.png?alt=media&#x26;token=f802e601-2b01-43d0-a39a-04a80ea021ec" alt=""><figcaption></figcaption></figure>

#### **5. Select the Jira Project**

* Once the connection is established, a dropdown menu will appear. Choose the **Jira project** you want to sync with ClickUp.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FLPVPuuq5ciJiuplvjd6A%2FSelecting%20Jira%20project.png?alt=media&#x26;token=b1dd1ceb-d928-46ec-b812-fd30e435436c" alt=""><figcaption></figcaption></figure>

#### **6. Generate ClickUp API Token**

* Follow our guide to generate the [**ClickUp API Token**](https://docs.getint.io/guides/quickstart/connection#clickup) and create the connection.
* Then select the connection, and choose the space and folder you wish to sync.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F1aF5KC8QCUce45bse0Qb%2FChose%20the%20app%20and%20established%20connections.png?alt=media&#x26;token=3a001f7b-2036-4b45-a0e5-c3b67797f9a7" alt=""><figcaption></figcaption></figure>

#### **7. Map Issue Types and fields**

Consider using the **Quick Build beta feature** for automated type and field mapping to simplify the setup.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9pIK91w86sNcMfSFSkg1%2FUsing%20Quick%20Build.jpg?alt=media&#x26;token=54353b32-c9a5-4e12-9fa1-34d021adc43d" alt=""><figcaption></figcaption></figure>

* Define how Jira issue types will sync with ClickUp task types.
  * Example: map a **Jira Task** to a **ClickUp Task** or a **Jira Bug** to a **ClickUp Task**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F4OcEeDGgW6uWXJRpN3rH%2FDefine%20issue%20types.png?alt=media&#x26;token=b9ca50d1-b73d-4073-ba03-d0c78f084864" alt=""><figcaption></figcaption></figure>

* Manually map or modify fields like **Title**, **Description**, **Assignee**, and **Custom Fields** between Jira and ClickUp.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FT859ESZMW8STGdRvH5lm%2FModify%20issues%20manually.png?alt=media&#x26;token=1207dd27-a0a4-4ee0-ba3e-4f495fb4a265" alt=""><figcaption></figcaption></figure>

#### **8. Status Mapping**

* Consider using the "Quick Build" beta feature for automated type and field mapping, which can streamline the setup process
* Enable and configure **Status Mapping** between Jira and ClickUp.
  * Map Jira statuses (e.g., **To Do**, **In Progress**, **Done**) to their corresponding ClickUp statuses for consistency.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FxAejkaQLUnyM3N5TyVBJ%2Fimage-20240918-134034.png?alt=media&#x26;token=b9d9a16e-e484-4823-af50-799faa862173" alt=""><figcaption></figcaption></figure>

#### **9. Sync Comments and Attachments**

* If needed, enable the synchronization of comments and attachments. Customize comment syncing, such as making them private or public or providing the parameters that fit your synchronization. Then apply and save the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FGvGu8JbPsctfiEFypJXm%2FSynchronizating%20too%20many%20songs%2C%20right%2B.jpg?alt=media&#x26;token=f53c0ea3-6ba7-4c9d-8b98-bb9c68b9bebf" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FQU8sw7JbkJ5FGvlHrA60%2F%C3%B6ptions%20for%20synchronization.jpg?alt=media&#x26;token=302afa52-2e5b-4dc4-aa5a-17a146fa36d1" alt=""><figcaption></figcaption></figure>

#### **10. UI Filtering Option:**

* Click on the filtering icon near the app icon in your integration. This will apply to that side of the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FCpxSpYZoBpLRLimjk1pT%2FGithub%20pendiente.png?alt=media&#x26;token=e89ba532-e405-4e1c-9f32-ff84768d771e" alt=""><figcaption></figcaption></figure>

* Select if the filtering applies to All, New, and Synced items.
* Note that if the option “*New items”* is selected, the filtering will apply only to the new items, and the already synced items will continue to sync and update. If the option “*Synced items”* is selected, only the already synced items will be updated based on that filter.
* Choose the options and add the value for the filter. It is possible to filter more than one option for each field.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FvpWZgeo8gmaPs844ZZKF%2FClickup%20user.jpg?alt=media&#x26;token=bc977f0c-75a8-4f9c-8ebc-359edfb90159" alt=""><figcaption></figcaption></figure>

Once you create the filters, Name the integration and Save it.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FLEJwpDI8b22K7wczWaq5%2FUntitled%20design%20(4)%20(1).jpg?alt=media&#x26;token=e5bbcb67-9f58-4787-8a5a-4f65181c899d" alt=""><figcaption></figcaption></figure>

#### **11. Test the Integration**

* Create sample tasks in both Jira and ClickUp to ensure the integration works as expected.
* Check the **reporting section** to confirm the sync is successful. If issues arise, visit our [**Help Center**](https://getint.io/help-center) for assistance.

#### **Advanced Settings for Your Atlassian Integration**

For users looking for advanced integration features, Getint allows for custom configurations, such as syncing **comments, attachments**, and **custom fields** between Jira and ClickUp. You can also tailor **workflow automation** to your team’s needs, ensuring that your data flows exactly how you need it to.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FdyysprFdJEELfEZqwFPB%2FGetint%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=3b653e81-cace-400d-9405-0bb554b122f0" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues to build your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>

# Jira Freshdesk integration

In the ever-evolving landscape of project management and customer support, the seamless integration between Jira and Freshdesk stands out as a game-changer.

In the ever-evolving landscape of project management and customer support, the seamless integration between Jira and Freshdesk stands out as a game-changer. Facilitated by Getint, this powerful connection bridges the divide between tracking project milestones and delivering exceptional customer service. By enabling a dynamic flow of information between Jira and Freshdesk, businesses can now manage their projects and customer queries from a single, unified interface. This guide simplifies the setup process and unlocks a world of efficiency and collaboration for teams of all sizes. Embrace the future of work with the Jira-Freshdesk integration and transform your project management experience.

**Optimize Your Team's Productivity with Getint 's Jira-Freshdesk Integration**

### &#x20;**Access the Getint App in Jira**

* Navigate to Jira, go to "Apps," and select "Jira - Freshdesk integration"

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FpYJVr120PJGxzgWk14Qh%2Fimage.png?alt=media&#x26;token=5cf2440a-aa43-4fe4-b8dd-2d70830591b1" alt=""><figcaption></figcaption></figure>

* Choose "Continuous Sync" or "Migration" based on your integration needs.<br>

  <figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fi2otPII3wowoLtKOuxdp%2Fimage.png?alt=media&#x26;token=d26f2713-7900-4b4e-bdeb-dadcdcfb383c" alt=""><figcaption></figcaption></figure>

### **Establish a** **Connection with Jira** <a href="#id-2.-establish-a-connection-with-jira" id="id-2.-establish-a-connection-with-jira"></a>

* Ensure you're logged in as a user with the correct permissions
* Click "Select App" and choose Jira.
  * **Token Generation for Jira Cloud:**
    * Visit your Atlassian Account Settings and go to the Security section.
    * Generate an API token in the API Token section. This token will authenticate your Jira Cloud.

{% embed url="<https://youtu.be/XKt7uOtFngk>" %}

* Select "Create New" to connect with your Jira instance.
* Name your connection, and add the URL of your Jira instance (without "/" at the end).
* Provide the login credentials.

{% embed url="<https://youtu.be/FiMSX3J4v2Q>" %}

#### **Choose the Jira Project** <a href="#id-3.-choose-the-jira-project" id="id-3.-choose-the-jira-project"></a>

* With a successful connection, a dropdown menu will appear.
* Select the Jira project you want to integrate.&#x20;

{% embed url="<https://youtu.be/z-fG4bEyl_o>" %}

### **Connect to Freshdesk** <a href="#id-4.-connect-to-freshdesk" id="id-4.-connect-to-freshdesk"></a>

* Log in to your Freshdesk account, click on your profile picture in the top right corner, and select 'Profile Settings.'
* In the sidebar on the right, click on the 'View API key' button to access the API key.
* Complete the captcha verification when prompted.

{% embed url="<https://youtu.be/odlS2evq4p4>" %}

{% hint style="info" %}
You can reset the API Key to stop an app from connecting to your helpdesk if you need to. Keep in mind that doing so will also disconnect other apps that use the same key.
{% endhint %}

**Configure** [**Getint**](http://getint.io/) **for Freshdesk**

* Open the Getint app and select "Freshdesk" as the connection app.
* Enter your Freshdesk instance URL and click "Next".
* Name the connection and provide your login credentials, using the token captured as the password.
* Choose an existing connection or create a new one and select “Connect”

### **Map Types**

* Synchronize Jira issue types such as Task, Bug, Epic, and Story with their Freshdesk counterparts.
* Clearly define which fields should be integrated or synchronized during this process.

{% embed url="<https://youtu.be/Oaii88uCfyI>" %}

### **Field Mapping**

Proper field mapping ensures data integrity across both platforms. Below are essential fields that require mapping:

* For the Freshdesk connection to work, it is necessary to map some key fields:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FYR4VqjuPHUzjQ9yXkIAn%2Fimage.png?alt=media&#x26;token=3e180257-e52d-4208-8c62-6bf1428330fd" alt=""><figcaption></figcaption></figure>

**Reporter/Requester Mapping**

* Link the 'Reporter' field in Jira to the 'Requester' field in Freshdesk.
* Ensure that requesters on both platforms are mapped to allow Getint to match them appropriately.
  * In case a fixed value, like an email, is supposed to be defined for this field, the configuration can be done like this:

{% embed url="<https://youtu.be/LJHIho1pQVo>" %}

#### **Status Field**

* Freshdesk mandates status mapping for the integration to function. A default value needs to be set for the ticket creation only, pointing towards the Freshdesk side, avoiding this option being picked up again when the issues are updated:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FYN6dmkFAadsRCgoCR7jY%2Fimage.png?alt=media&#x26;token=f38a35fb-8c6a-4b46-b7cd-3edcb1bff8d7" alt=""><figcaption></figcaption></figure>

**Priority Field**

* Mapping the priority field is a necessity for the integration's operation within Freshdesk.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FTKNpA81kI1TNoXcBHOrH%2Fimage.png?alt=media&#x26;token=c206ed82-c2b0-403b-a15a-42a4cfe3d60b" alt=""><figcaption></figcaption></figure>

* After all fields and types have been configured, give your integration a distinctive name and save the settings.
* Consider using the "Quick Build" beta feature for automated type and field mapping, which can streamline the setup process.

{% embed url="<https://youtu.be/1BF4mOmzbzU>" %}

{% hint style="info" %}
Quick build is currently in the beta stage, if you have feedback or questions about it, please get in touch with our support at <support@geint.io>
{% endhint %}

### **Filtering** <a href="#id-8.-filtering" id="id-8.-filtering"></a>

It is possible to filter the synchronization to have them customized for your needs and requirements.

#### **UI Filtering Option**

* Click on the filtering icon near the app icon in your integration. This will apply to that side of the integration.
* Select if the filtering applies to All, New, and Synced items.
* Note that if the option “*New items”* is selected, the filtering will apply only to the new items, and the already synced items will continue to sync and update. If the option “*Synced items”* is selected, only the already synced items will be updated based on that filter.
* Choose the options and add the value for the filter. It is possible to filter more than one option for each field.
* Select Apply once you created the filters and Save the integration.

{% embed url="<https://youtu.be/qDj5KmG0w7U>" %}

#### **JQL Filtering**

* Select the app that will receive the filter.
* Under the field Custom JQL, it is possible to provide a JQL, which will be the filter for your sync and appended to the one generated when searching for issues in Jira (e.g., status in ('In Progress')).
* Save the integration.

{% embed url="<https://youtu.be/oNjFSqRRUSA>" %}

#### Duplicate Setup and Select Different Projects <a href="#id-9.-duplicate-setup-and-select-different-projects" id="id-9.-duplicate-setup-and-select-different-projects"></a>

* Go to Workflows.
* Click the 3 dots on the right side and select "duplicate."
* A side panel will appear. Select a new name for the integration (by default, the integration will be called “copy of” if the same projects are established).
* On the dropdown menu, select the projects you would like to integrate.
* For each side, select Connect. Then Duplicate.
* Save the new integration.&#x20;

{% embed url="<https://youtu.be/6su7bE9VZyc>" %}

Leverage the Jira-Freshdesk integration by Getint to optimize your project management and customer service processes. For further assistance or feedback, contact <support@getint.io>.

# Jira Freshservice integration

Integrating Jira with Freshservice via the Getint platform transforms how organizations handle project management and customer service in today's interconnected business environment. This essential link creates a streamlined interface that aligns project tracking with IT service management, significantly enhancing operational efficiency and team communication. Our guide offers a clear, straightforward setup process, allowing companies of all sizes to boost collaboration and elevate their service delivery capabilities. Harness the power of the Jira-Freshservice integration with Getint, and move towards a more efficient and effective framework for managing projects and support services.

### **Optimize Your Team's Productivity with Getint 's Jira-Freshservice Integration**

#### &#x20;**0. Access the** [**Getint**](http://getint.io/) **App in Jira:**

* Navigate to Jira, go to "Apps," and select "Jira - Freshdesk integration"

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F5hTfLvMtTE0UKWCw62oP%2Fimage-20240404-113459.png?alt=media&#x26;token=d8240af9-c9fe-4153-8dd7-568e84e732ef" alt=""><figcaption></figcaption></figure>

* Choose "Continuous Sync" or "Migration" based on your integration needs.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F2Z9X8IKZDi7VCj5f83w2%2Fimage-20240109-123756.png?alt=media&#x26;token=db32b39b-c73a-460c-ab4f-7fa0f0ce4838" alt=""><figcaption></figcaption></figure>

#### **1. Token Generation for Jira Cloud:** <a href="#id-1.-token-generation-for-jira-cloud" id="id-1.-token-generation-for-jira-cloud"></a>

* Visit your Atlassian Account Settings and go to the Security section.
* Generate an API token in the API Token section. This token will authenticate your Jira Cloud.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FCYziHUpTlaIl4TtquGld%2FUntitled%20design-20240514-103351.jpg?alt=media&#x26;token=95575920-8c25-40c1-8696-91e6d6d7ec1d" alt=""><figcaption></figcaption></figure>

#### **2. Establish a** **Connection with Jira:** <a href="#id-2.-establish-a-connection-with-jira" id="id-2.-establish-a-connection-with-jira"></a>

* Ensure you're logged in as a user with the correct permissions
* Click "Select App" and choose Jira.
* Select "Create New" to connect with your Jira instance.
* Name your connection, and add the URL of your Jira instance (without "/" at the end).
* Provide the login credentials.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FuXZjNY9ijf1XiVx7eb5X%2FScreenshot%202024-05-14%20074340.png?alt=media&#x26;token=fba8cf20-246f-4005-ad74-c6325af579ed" alt=""><figcaption></figcaption></figure>

#### **3. Choose the Jira Project:** <a href="#id-3.-choose-the-jira-project" id="id-3.-choose-the-jira-project"></a>

* With a successful connection, a dropdown menu will appear.
* Select the Jira project you want to integrate.&#x20;

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F8nH8zo9lx0ZgaMBmg3Sj%2FScreenshot%20from%20May%2014%2C%202024%2C%207_39%20AM.png?alt=media&#x26;token=744ff639-2203-48ee-97fd-4a8d3c184784" alt=""><figcaption></figcaption></figure>

#### **4. Connect to Freshservice:** <a href="#id-4.-connect-to-freshservice" id="id-4.-connect-to-freshservice"></a>

* Log in to your Freshservice account, click on your profile picture in the top right corner, and select “profile settings”
* On the new page, on the right, click on 'Your API Key' and select the check button to access the API key:
* Complete the captcha verification when prompted, and copy the API Key.

{% hint style="info" %}
You can reset the API Key to stop an app from connecting to your helpdesk if you need to. Remember that doing so will also disconnect other apps that use the same key.
{% endhint %}

#### **5. Configure** [**Getint**](http://getint.io/) **for Freshservice:**

* Open the Getint app and select "Freshservice" as the connection app.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FXOuBNoTC3SED6ffBqywU%2FUntitled%20design%20(2).jpg?alt=media&#x26;token=a29f4c8f-6418-4fe1-ae6c-08bdb2ae332c" alt=""><figcaption></figcaption></figure>

* Enter your Freshservice instance URL and click "Next".
* Name the connection and provide your login credentials, using the token captured as the password.
* Choose an existing connection or create a new one and select “Connect”

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FLc8njeCyUxaXK8vPm7pD%2FScreenshot%202024-05-14%20080419.png?alt=media&#x26;token=87b8b6a6-0902-4701-98aa-afd666baf229" alt=""><figcaption></figcaption></figure>

#### **6. Map Types:**

**Quick Build:**

* Consider using the "Quick Build" beta feature for automated type and field mapping. Quick Build automatically performs the mappings based on the most common configurations used by our customers, making it an ideal initial setup for a Minimum Viable Product (MVP). This feature simplifies the setup process by pre-configuring types, fields, and values, allowing you to quickly get started with a functional integration. Once the initial setup is complete, you can review and adjust the mappings to better suit your specific needs and requirements.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FaCwU8IXeUFL9kZSLlkbr%2Fe9281c80-3b60-4eda-91be-a0b476809f2a.jfif?alt=media&#x26;token=e851f182-5358-4199-b56f-aa85a3e552fd" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Quick build is currently in the beta stage, if you have feedback or questions about it, please get in touch with our support at <support@geint.io>
{% endhint %}

**Manual Setup:**

* Select to synchronize Jira issue types such as Task, Bug, Epic, and Story with their Freshservice counterparts.
* Define which fields should be integrated or synchronized during this process.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Ffzfu5EqZaYcKji8MGPxG%2Fimage-20240514-114435.png?alt=media&#x26;token=a3f569bc-51be-418f-a8f9-f2303693300e" alt=""><figcaption></figcaption></figure>

#### **7. Field Mapping:**

Proper field mapping ensures data integrity across both platforms. Below are essential fields that require mapping:

* For the Freshservice connection to work, it is necessary to map some key fields:

1. **Reporter/Requester Mapping**:
   * Link the "Reporter" field in Jira to the "Requester" field in Freshservice.
   * Ensure that requesters on both platforms are mapped to allow Getint to match them appropriately.
     * In case a fixed value, like an email, is supposed to be defined for this field, the configuration can be done like this:
2. **Status Field**:
   * Freshservice mandates status mapping for the integration to function. A default value needs to be set for the ticket creation only, pointing towards the Freshservice side, avoiding this option being picked up again when the issues are updated:
3. **Priority Field**:
   * Mapping the priority field is necessary for the integration's operation within Freshservice.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FIIVQQjgTlkTjuDK2zcIV%2FUntitled%20design%20(4).jpg?alt=media&#x26;token=e02a456e-c15d-4db2-8056-25000412b613" alt=""><figcaption></figcaption></figure>

* After all fields and types have been configured, give your integration a distinctive name and save the settings.
* Consider using the "Quick Build" beta feature for automated type and field mapping, which can streamline the setup process.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FoDwgJ7sfZloIauZJeYdg%2FUntitled%20design%20(3).jpg?alt=media&#x26;token=c3df1527-88d6-4073-b658-ebe64687f054" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Quick build is currently in the beta stage, if you have feedback or questions about it, please get in touch with our support at <support@geint.io>
{% endhint %}

#### **8. Filtering:** <a href="#id-8.-filtering" id="id-8.-filtering"></a>

It is possible to filter the synchronization to have them customized for your needs and requirements.

**UI Filtering Option:**

* Click on the filtering icon near the app icon in your integration. This will apply to that side of the integration.
* Select if the filtering applies to All, New, and Synced items.
* Note that if the option “New items” is selected, the filtering will apply only to the new items, and the already synced items will continue to sync and update. If the option “Synced items” is selected, only the already synced items will be updated based on that filter.
* Choose the options and add the value for the filter. It is possible to filter more than one option for each field.
* Select Apply once you have created the filters and Save the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FKfCUK4qqsEhjMJiytxo9%2FUntitled%20design%20(5).jpg?alt=media&#x26;token=f8cbedab-ae09-4acf-a420-3e784afb86d2" alt=""><figcaption></figcaption></figure>

**JQL Filtering:**

* Select the app that will receive the filter.
* Under the field Custom JQL, it is possible to provide a JQL, which will be the filter for your sync and appended to the one generated when searching for issues in Jira (e.g., status in ('In Progress')).
* Save the integration.

#### &#x20;9. Duplicate Setup and Select Different Projects: <a href="#id-9.-duplicate-setup-and-select-different-projects" id="id-9.-duplicate-setup-and-select-different-projects"></a>

* Go to Workflows.
* Click the 3 dots on the right side and select "duplicate."
* A side panel will appear. Select a new name for the integration (by default, the integration will be called “copy of” if the same projects are established).
* On the dropdown menu, select the projects you would like to integrate.
* For each side, select Connect. Then Duplicate.
* Save the new integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FI9E62kiAff0YYQim4X1H%2FUntitled%20design%20(6).jpg?alt=media&#x26;token=df6dbac9-bbde-4879-a952-53cc26c3e3f6" alt=""><figcaption></figcaption></figure>

Leverage the Jira-Freshservice integration by Getint to optimize your customer service processes. For further assistance or feedback, contact <support@getint.io>

# Jira GitHub integration

Integrating Jira with GitHub using Getint connects your project tracking and code management through two-way synchronization. Whether you’re logging issues in Jira or handling code in GitHub, this setup keeps both teams aligned and informed.

This step-by-step guide shows you how to configure the integration using Personal Access Tokens for authentication.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FSYEVjXgxno7iiLBoXU2c%2FGitHub%20Integration%20for%20Jira.png?alt=media&#x26;token=c3dc8b64-9e26-486f-8002-38268c43a32b" alt=""><figcaption><p><a href="https://marketplace.atlassian.com/apps/1223933/github-integration-for-jira-github-connector?hosting=cloud&#x26;tab=overview">Check out our GitHub integration app on the Atlassian Marketplace</a></p></figcaption></figure>

***

### GitHub-Jira Licensing Model <a href="#github-jira-licensing-model" id="github-jira-licensing-model"></a>

The GitHub-Jira licensing model with Getint is designed to accommodate different integration needs. Here’s an overview:

#### Standard Licensing <a href="#standard-licensing" id="standard-licensing"></a>

* A Getint license is only required on Jira, allowing seamless data synchronization between GitHub and Jira.

  This makes setup simpler and faster, without the need for additional configurations in GitHub.

#### Flexible License <a href="#flexible-license" id="flexible-license"></a>

* For managed services companies or organizations looking to integrate four or more instances (regardless of whether they are the same or different tools), Getint offers a **Flexible License.** This custom license covers a specific number of connections (i.e., up to 10 instances) without restrictions on the tools involved. You can also swap the integrated tools while the license remains active, offering unparalleled flexibility.

For more details on licensing, visit our [**Pricing Page**](https://docs.getint.io/billing-and-services/licensing).

#### Requirements to Build Your Integration: <a href="#requirements-to-build-your-integration" id="requirements-to-build-your-integration"></a>

* The **Getint app** must be installed in Jira.
* Comments are attributed to the user who created the connection. Therefore, we recommend using dedicated Service Accounts for both instances.
* Jira instances must have a dedicated user and an associated API token with permissions to read, write, view, and modify the project.
* **Personal Access Tokens** are required for Jira and GitHub authentication. You can find the steps to generate the access token for your connectors here: [Connection Guide](https://docs.getint.io/guides/quickstart/connection#github).

### Setting Up Your GitHub-Jira Integration <a href="#setting-up-your-github-jira-integration" id="setting-up-your-github-jira-integration"></a>

**1. Access the Getint App in Jira**

* Navigate to **Apps** and select **Jira - GitHub Integration**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FKtiTHpWuah3KFrxNxcqv%2FJira%20GitHub%20app.png?alt=media&#x26;token=b16944e5-5dc1-48aa-bfb8-2267322bd683" alt=""><figcaption></figcaption></figure>

**2. Create Integration**

* Click **Create integration** or **Migration**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FTKrsyipUrJ5JuTpaDYSL%2FChoosing%20Continuos%20sync%20or%20Migration.png?alt=media&#x26;token=76875dc4-c6e6-4855-9718-1ce6ff853122" alt=""><figcaption></figcaption></figure>

**3. Token Generation (Password for Jira Cloud)**

* For Jira Cloud, generate a Jira token. This token will act as your password:
  * Go to Atlassian Account Settings.
  * Navigate to Security and generate an API token, then use this token as the password for Jira integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FeRhhFwwP7bFhYfywv20q%2FToken%20Generation%20for%20GitHub.png?alt=media&#x26;token=c2f93a38-19f7-4118-86cd-46ef5f5cd20d" alt=""><figcaption></figcaption></figure>

**4. Generate a GitHub Personal Access Token**

* Log in to your GitHub account.
* Select your Avatar in the top right corner. Navigate to Settings > Developer Settings > Personal access tokens.
* Generate a new Token (Classic) or Fine-grained token.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FcZI6Kl1yE9gGhWGjUlUQ%2FGitHub%20Personal%20Access%20Token.png?alt=media&#x26;token=c9908b7d-8019-4bcb-8725-77abf6e5da9e" alt=""><figcaption></figcaption></figure>

* Provide a name for your token, select the expiration date, and set the required scopes (permissions). For a detailed description of how to create the token, please follow this [guide](https://docs.getint.io/guides/quickstart/connection#github).
* Click **Generate Token** and make sure to securely store your token, as it will only be visible once.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FvjqQ1HxHe8NlMCtPpUc5%2FGenerate%20token%20button.png?alt=media&#x26;token=032f4686-7770-48fe-afff-da4182f051cc" alt=""><figcaption></figcaption></figure>

**5. Connect to Jira**

* In Getint, enter your Jira instance URL, username, and the API token.
* Use the Personal Access Token for Jira Cloud.
* Follow our [Quickstart Guide](https://docs.getint.io/guides/quickstart/connection#jira) for more details on how to create the connection.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FTM4mxWp0iygKg9Ey0ZZa%2FCreate%20a%20connection.png?alt=media&#x26;token=d615fc24-d004-49e2-80f2-1600738e4acf" alt=""><figcaption></figcaption></figure>

* Select the Jira project you wish to integrate with GitHub.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FVIKxUlQfvPzPm23omA33%2FConfigure%20the%20connection.png?alt=media&#x26;token=f9da4ee8-b416-4334-9fe8-df33f9b0c7c7" alt=""><figcaption></figcaption></figure>

**6. Enter GitHub Token in Getint**

* Once you have generated a Personal Access Token in your GitHub instance, you will now have the option to connect the tool with Getint.
* Paste the GitHub Personal Access Token into the API token field.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FbeokfRzBNHUTiJKlq2V8%2FGitHub%20entering%20API%20token.png?alt=media&#x26;token=a06eb84b-1780-4ab3-b8b7-f443792b1f51" alt=""><figcaption></figcaption></figure>

* Select the GitHub repository or the Project you want to sync with Jira.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FuYkG6xcvanrQL6ebtPce%2FConnection%20to%20GitHub.png?alt=media&#x26;token=18b06aee-f09a-406c-93d0-dadfb6fe1b12" alt=""><figcaption></figcaption></figure>

* Click Save to establish the connection.

**7. Issue Type Mapping**

* Map the Jira issue types you want to sync with GitHub tasks, such as mapping a GitHub Task to a Jira task or a Jira bug to a GitHub task.
* Consider using the **Quick Build** beta feature for automated type and field mapping, which can streamline the setup process.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F7QJTEaNHF8ET6nsnfId4%2FJira%20GitHub%20integration%20main%20screen.png?alt=media&#x26;token=851237ad-c4e0-417f-bade-dd2259d11a9d" alt=""><figcaption></figcaption></figure>

#### 8. Field Mapping <a href="#id-7.-field-mapping" id="id-7.-field-mapping"></a>

* Review or manually map fields within mapped types, including title, description, and assignees.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FLB3W6KC6VK4eCUe11jZu%2FField%20Mapping.png?alt=media&#x26;token=12a1abbe-3bac-4d8e-a365-8c18f5ef192b" alt=""><figcaption></figcaption></figure>

**9. Assignee Mapping**

* Use the assignee mapping option to match Jira assignees to GitHub collaborators, enabling precise synchronization of task ownership. For more details, visit our doc: [Assignees (users) mapping](https://docs.getint.io/getintio-platform/workflows/assignees-users-mapping).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9u3PwXpgnKsl8PwKvwn0%2FAsignee%20Mapping.png?alt=media&#x26;token=88059e10-c0bf-4231-ad5f-c4528dd4fa87" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
When syncing **projects**, make sure your repository is linked to the target project. If it isn’t, assignees won’t appear in the mapping dropdown.
{% endhint %}

#### 10. Status Mapping

* Map status fields to align between Jira and GitHub. For example, **To do** in Jira could be mapped to **Opened** in GitHub.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FmdPpFvoAlrK2lMAfQ5Pj%2FStatus%20Mapping.png?alt=media&#x26;token=86bd30ee-b5f1-4ef9-a076-48c62bae1fb3" alt=""><figcaption></figcaption></figure>

#### 11. Comments <a href="#id-10.-comments" id="id-10.-comments"></a>

* When enabling comment synchronization, you can filter by criteria such as created date, author, or visibility (public/private).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FbWUDWHZTBZuydDO5ZWrv%2FComments.png?alt=media&#x26;token=1f257003-8e9a-439f-a5fa-48cc3ce2496b" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
**Attachment Limitation**: Attachments are currently limited to one-way syncing and are only supported from Jira to GitHub. Attachments in GitHub will not sync to Jira
{% endhint %}

**12. Filtering:**

* It is possible to filter the synchronization to have it customized for your needs and requirements. Please see the doc [Items Filtering](https://docs.getint.io/getintio-platform/workflows/items-filtering) for more details.

**UI Filtering Option:**

* Click on the filtering icon near the app icon in your integration. This will apply to that side of the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F0hJ9uxMKjOazAFXe8yHk%2FFiltering.png?alt=media&#x26;token=916e2e03-a017-4db0-9d18-8dc644776e40" alt=""><figcaption></figcaption></figure>

* Select if the filtering applies to All, New, and Synced items.
* Note that if the option **New items** is selected, the filtering will apply only to the new items, and the already synced items will continue to sync and update. If the option **Synced items** is selected, only the already synced items will be updated based on that filter.
* Choose the options and add the value for the filter. It is possible to filter more than one option for each field.
* Select **Apply** once you have created the filters and **Save** the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F2OYcFAuHtmED9CyXmJDN%2FUI%20Filtering.png?alt=media&#x26;token=f0899ace-21e6-4d9a-a638-076fc8ba16cf" alt=""><figcaption></figcaption></figure>

**13. Test the Integration**

* Create test issues or tasks in Jira or GitHub and observe how they synchronize.
* Ensure that the data between the two platforms is correctly synced.
* Monitor the integration status and the logs in Getint to verify that everything functions as expected.

***

### Conclusion <a href="#conclusion" id="conclusion"></a>

By following this guide, you can successfully integrate **Jira** and **GitHub** using Getint. This setup enables smooth synchronization of issues, tasks, and workflows between development and project management tools, helping teams collaborate more effectively and bridging the gap between developers and project managers.

For further assistance, please contact us at the [Support Center](https://getint.io/help-center) or [Schedule a Demo](https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FquqlmoKO6zqGHsjk6DTL%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=de8e62c8-2dd6-4ee8-8d8d-c133b8b954b4" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>

# Jira GitLab integration

### **Introduction**

Integrating Jira with GitLab enables seamless synchronization between project management and version control, enhancing collaboration and workflow efficiency. Follow this comprehensive guide to set up a two-way integration between Jira and GitLab quickly and easily.

### Step-by-Step Setup Guide <a href="#step-by-step-setup-guide" id="step-by-step-setup-guide"></a>

#### **0. Access the Getint App in Jira**

* Navigate to "Apps" and select “Jira - GitLab Integration”

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fk4lt3ZVafvd38ZWsu72X%2Fimage-20240617-154412.png?alt=media&#x26;token=7d1b0094-0a2b-4ee9-aeba-c963ccfa7a16" alt=""><figcaption></figcaption></figure>

#### **1. Create Integration**

* Click "Create integration” or “Migration”

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FJebLOxMpqGdg4Ml4R4U4%2Fimage-20240619-115231.png?alt=media&#x26;token=040467a0-212f-46a1-84d8-b731d80d3575" alt=""><figcaption></figcaption></figure>

#### **2. Token Generation (Password for Jira Cloud)**

* For Jira Cloud, generate a Jira token. This token will act as your password:
  * Go to Atlassian Account Settings.
  * Navigate to Security and generate an API token, then use this token as the password for Jira integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FAjTYyEg7wJ0rOH9rn06Y%2FScreenshot%202024-06-19%20085658.png?alt=media&#x26;token=5b480230-999b-489b-94a0-7814884fb944" alt=""><figcaption></figcaption></figure>

#### **3. Choose the Apps and Establish Connections**

* Ensure you are logged in as a user with admin rights, click on "Select App" and choose Jira.
* Select "Create New" to establish a new connection with your Jira instance and add the URL of your Jira instance (omit the trailing "/").
* Enter the login credentials of the admin user.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FjP3Zl01xPNTvzaasBNCG%2Fimage-20240620-165801.png?alt=media&#x26;token=71153fff-310f-4239-88b1-c2ae62827052" alt=""><figcaption></figcaption></figure>

#### **4. Select the Jira Project**

* Once the connection is established, choose the Jira project you want to connect to from the dropdown menu.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FloMoKloeDsLHZVf6CKeU%2Fimage-20240620-170315.png?alt=media&#x26;token=78f729d4-4905-4cd4-abec-39335d2b22bf" alt=""><figcaption></figcaption></figure>

#### **5. Generate GitLab Token**

* Go to the GitLab developer console and generate a token. This token will serve as the password for the integration. Follow the steps [here](https://docs.getint.io/guides/quickstart/connection#gitlab) for the token with the correct permissions.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FtLKPmpuDjisXuwSTZ4LJ%2FGetint%20White%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=9714219f-de96-40b9-9041-7d7f17cb8e3d" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

#### **6. Connect to GitLab**

* If no connection is established yet, create a new one.
* Use the GitLab token generated as a password.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FUY4eFKXWqewsRxwmS58g%2Fimage-20240620-171013.png?alt=media&#x26;token=4f0b1155-a521-4852-84a2-25c8011e33a3" alt=""><figcaption></figcaption></figure>

#### **7. Select the Connection and Project**

* Select the established GitLab connection and choose the project you want to integrate with.

#### **8. Type Mapping**

* Map the Jira issue types you want to sync with GitLab issues, such as mapping a GitLab issue to a Jira task or a Jira bug to a GitLab issue.
* Consider using the "Quick Build" beta feature for automated type and field mapping, which can streamline the setup process.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FJNK7Uf5to7oNvXBYFqBb%2Fimage-20240621-101521.png?alt=media&#x26;token=61d252c2-1f2b-42a7-b19e-e27544a37614" alt=""><figcaption></figcaption></figure>

#### **9. Field Mapping**

* Review or manually map which fields to integrate and sync within the mapped types, including title, description, assignees, custom fields, and more.

#### **10. Assignee Mapping**

* Map and match assignees according to your desired configuration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FlNhgQ78GwibAqwZ1JQJk%2Fimage-20240620-171902.png?alt=media&#x26;token=ff68dd4b-9f8e-44f4-a6b6-131e2a4ce89d" alt=""><figcaption></figcaption></figure>

#### **11. Comments**

* If needed, enable the integration and synchronization of comments.
* Filter the comments with the criteria that suit you. Make them private/public or use the preferred attributes such as created date or author.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FYrl9lfjW3wXBIeDU4vt4%2Fimage-20240621-102606.png?alt=media&#x26;token=61aa9388-80c9-4ae4-b060-701494ba92df" alt=""><figcaption></figcaption></figure>

#### **12. Finalize Integration**

* Name your project and click "Create" to finalize the integration setup.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMbNyYKcJ2eJ6Uy63USCO%2Fimage-20240621-102709.png?alt=media&#x26;token=4870a7ae-2972-49dc-9ea7-7fb48b2b6956" alt=""><figcaption></figcaption></figure>

#### **13. Filtering:**

It is possible to filter the synchronization to have them customized for your needs and requirements.

**UI Filtering Option:**

* Click on the filtering icon near the app icon in your integration. This will apply to that side of the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F3bYZlY7VvCQe8BQB1zkX%2Fimage-20240621-102751.png?alt=media&#x26;token=3dd7f8a0-3175-4f62-ad5a-dd653a4c109f" alt=""><figcaption></figcaption></figure>

* Select if the filtering applies to All, New, and Synced items.
* Note that if the option “*New items”* is selected, the filtering will apply only to the new items, and the already synced items will continue to sync and update. If the option “*Synced items”* is selected, only the already synced items will be updated based on that filter.
* Choose the options and add the value for the filter. It is possible to filter more than one option for each field.
* Select Apply once you created the filters and Save the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FjKfXYFdXfIbBThJjorZ4%2Fimage-20240621-102849.png?alt=media&#x26;token=8010f270-b7ab-4938-a6f8-f94011f041d2" alt=""><figcaption></figcaption></figure>

### Conclusion <a href="#conclusion" id="conclusion"></a>

Following these steps, you can effectively integrate Jira with GitLab, ensuring smooth synchronization of tasks, issues, and workflows between the two platforms. This setup enhances collaboration and streamlines project management processes.

For further assistance, please contact us at the [Support Center](https://getint.io/help-center) or [Schedule a Demo](https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FCQdON7rk1lCKReSQtp9W%2FGetint%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=e240ec28-3056-42c7-968c-c66de763b0d5" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>

# Attachments Sync in GitLab Integration

As of now, there’s a limitation to syncing attachments from GitLab. It doesn’t support attachments natively, but it is possible to sync them with a workaround by providing a cookie header.

### How to sync attachments <a href="#how-to-sync-attachments" id="how-to-sync-attachments"></a>

1. Please open your type mappings in your Jira Gitlab integration and go to the **Comments & Attachments** tab. Enable **Synchronize attachments:**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FTbP65Hl6wgOkZuPrhKhD%2F01e799325071a6493e9cf4555d7671f2%20(1).png?alt=media&#x26;token=478c466f-4802-4a4d-8ae2-59f066f0c02c" alt=""><figcaption></figcaption></figure>

1. Get the **Cookie header** from your GitLab account. Use the developer's tool (F12 on Windows) within your GitLab’s groups page and go to **Network** > **Groups** > Click on **Headers** and scroll down to **Cookie**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Frlx18fnugpG1uezmyBX5%2F65e501727ccb3c3cf44c6c24119aee27%20(1).png?alt=media&#x26;token=e9237911-2d9f-4ed7-abbd-c02738169908" alt=""><figcaption></figcaption></figure>

1. Copy the information and paste it into the **GitLab Cookie Header** field in Getint. Click **Apply,** to submit the changes and save your integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FQHD2reVbQ81Ohf1kHytN%2F1cbc24fe9b3e6f2df72ee82a896e5a6a%20(1).png?alt=media&#x26;token=ed698052-6fae-495a-a119-b6c6d4e141ef" alt=""><figcaption></figcaption></figure>

1. Make sure to test the attachments after enabling the feature.

{% hint style="warning" %}
Currently, attachments are only supported one way from GitLab to the other app in the integration. Also, no API is available to download and upload attachments through a Gitlab integration. As a result, this alternative remains the only option for downloading attachments from synced comments as long as they come from GitLab.
{% endhint %}

# Jira HubSpot integration

In today's fast-paced business environment, integrating your project management tools with customer relationship management platforms is essential for maintaining seamless operations and maximizing efficiency. Getint's Jira-Hubspot integration brings together the robust issue-tracking capabilities of Jira with the dynamic CRM functionalities of Hubspot, ensuring a continuous flow of information and enhanced collaboration across your teams. Whether you're looking to set up a two-way or a one-way integration, this comprehensive guide will help you establish a streamlined connection, boosting productivity and facilitating superior project management.

### Step-by-Step Setup Guide <a href="#step-by-step-setup-guide" id="step-by-step-setup-guide"></a>

#### **1. Access the Getint App in Jira**

Navigate to "Apps" and select "Hubspot Integration for Jira"

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fcp5p3qIfViyQ9m4A0TOD%2Fimage-20240715-150006.png?alt=media&#x26;token=3fa786ac-d84d-4c9b-8a23-f32ed079e9cc" alt=""><figcaption></figcaption></figure>

#### **2. Create Integration**

Click "Create integration" for ongoing sync or "Migration" to transfer existing data: [Migration Guide](https://docs.getint.io/guides/migration).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F0RATyPkExYUKG6XXqR5h%2Fimage-20240715-150119.png?alt=media&#x26;token=ef99b370-2b18-48b7-b2e2-97ae28ff1aa4" alt=""><figcaption></figcaption></figure>

#### **3. Token Generation (Password for Jira Cloud)**

For Jira Cloud, generate a Jira token. This token will act as your password:

* Go to Atlassian Account Settings.
* Navigate to Security and generate an API token, then use this token as the password for Jira integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fdey3IkQg3fWUG0rcMdpI%2Ff8193fbb-47b9-4cde-951d-924dc076abf4.png?alt=media&#x26;token=f7aab8d5-8244-4a7d-a763-722f50af3882" alt=""><figcaption></figcaption></figure>

#### **4. Choose the Apps and Establish Connections**

* Ensure you are logged in as a user with admin rights, click "Select App" and choose Jira.
* Select "Create New" to establish a new connection with your Jira instance and add the URL of your Jira instance (omit the trailing "/").
* Enter the login credentials of the admin user.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FvsH3IQXotbjlDAVnPzBD%2Fimage-20240715-151822.png?alt=media&#x26;token=eb22713c-f3b3-46b3-b541-6b62a273955d" alt=""><figcaption></figcaption></figure>

#### **5. Select the Jira Project**

* Once the connection is established, choose the Jira project you want to connect to from the dropdown menu.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FR4qXw1mhnjBlraSm7nzS%2Fimage-20240620-170315%20(2).png?alt=media&#x26;token=9643bad6-2677-4687-9773-dbcdd9971ebc" alt=""><figcaption></figcaption></figure>

#### **6. Connect to Hubspot**

* Select the Hubspot app and tap on "Create a new connection" Use the Personal token created following the instructions in the guide: [Connections](https://docs.getint.io/guides/quickstart/connection#hubspot)
* Tap on "Connect"

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FhxVhwLkrkxmxLGGIsGbW%2Fimage-20240715-170006.png?alt=media&#x26;token=3d9d65ac-32eb-4854-9df0-0a9c3bc10629" alt=""><figcaption></figcaption></figure>

#### **7. Type Mapping**

Map the Jira issue types you want to sync with Hubspot tasks, such as mapping a Hubspot task to a Jira issue or a Jira bug.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FaBmgEircnMjbgKxPCvZA%2FScreenshot%20from%20July%2015%2C%202024%2C%202_02%20PM3.png?alt=media&#x26;token=6a07cc71-971b-465a-bdd8-2702e2a7c608" alt=""><figcaption></figcaption></figure>

Consider using the "Quick Build" beta feature for automated type and field mapping, which can facilitate the setup process.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FR1p8EfdfeV8OgJ8jFQk2%2FUntitled%20design%20(15).jpg?alt=media&#x26;token=dbb86e56-2c19-4ca1-a328-ffe250554479" alt=""><figcaption></figcaption></figure>

#### **8. Field Mapping**

Review or manually map which fields to integrate and sync within supported mapped types, make any necessary modifications, and hit apply

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F7tBSpT20NC8HeqRQ9IoQ%2FScreenshot%20from%20July%2015%2C%202024%2C%202_01%20PM2.png?alt=media&#x26;token=9920d8fe-8b2a-438c-8a40-2729d0859daf" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
To keep your tickets syncing correctly, you MUST map the "Ticket Status" field to a fixed value called "New," just like in the picture above. This lets Jira send new and updated tickets over to HubSpot without any issues. If you don’t do this, you’ll run into a sync error when Jira tries to share data with HubSpot.

The Quick Build feature will add this field mapping by default, but you can also add it manually by selecting Add Field Mapping > HubSpot > Ticket Status > Fixed Value and entering the status for newly created tickets. For most customers, this value is "New," but you can use your status, such as "Open" or "To Do." In these cases, simply enter the corresponding value. For example, map the "Ticket Status" field to the fixed value "To Do."
{% endhint %}

Getint now supports the Satisfaction field in Jira, enabling seamless synchronization and integration of satisfaction ratings across platforms. This new feature ensures that customer feedback and satisfaction metrics are consistently tracked and managed within your Jira projects. This enhancement reflects Getint’s dedication to offering comprehensive and adaptable integration solutions that cater to evolving user needs.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FEzSd5P5UixJjgDNLj8xR%2FAdded%20support%20for%20the%20Satisfaction%20field%20in%20JSM.png?alt=media&#x26;token=93d9af51-52d1-4b74-b3e2-0ff689dd851b" alt=""><figcaption><p>An example of how the Satisfaction field is located in Jira Service Management</p></figcaption></figure>

The Satisfaction field, located in Jira Service Management, can be utilized to track customer feedback in your Jira-HubSpot integration, enhancing your ability to monitor and improve customer satisfaction.

{% hint style="info" %}
If you need custom development or are trying to sync a field that isn't supported, please reach out to our [Service Center](https://getint.io/help-center) or [Schedule a Demo Call](https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team).
{% endhint %}

### Advanced Settings

#### **9. Comments**

If needed, enable the integration and synchronization of comments.

* Filter the comments with criteria that suit you. Make them private/public or use the preferred attributes such as created date or author.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMT0Oc5nlORciom2L5Xrv%2Fimage-20240715-171122.png?alt=media&#x26;token=15216bda-14b6-448f-aa58-dc6dd2bd38d1" alt=""><figcaption></figcaption></figure>

#### **10. Statuses Mapping**

Enable status mapping, then map the statuses as desired.

* Specify the Hubspot field that will keep the status data from Jira, ensuring fields in Hubspot mirror your Jira setup (e.g., To do - To do, Done - Done).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FsZHxtIF6OPs5T94pkO8J%2Fimage-20240715-171606.png?alt=media&#x26;token=b754240c-40b9-4ea6-a576-c476e36da756" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
**Note:** In HubSpot, each mapped type has a different status field. For example, a Deal maps to Stage, while a Ticket maps to Ticket Status. Identify the correct field for the mapped type to ensure the status transition syncs properly.
{% endhint %}

### Finalize Integration

#### **11. Name the Integration and Click "Create"**

Name your integration and click "Create" to finalize the setup.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FUtlQZJyUPDsnALAFvQvB%2FUntitled%20design%20(16).jpg?alt=media&#x26;token=0fbbeb60-3810-4f33-b3fe-d7bd53fa460a" alt=""><figcaption></figcaption></figure>

#### **12. Filtering**

It is possible to filter the synchronization to have them customized for your needs and requirements.

**UI Filtering Option:**

* Click on the filtering icon near the app icon in your integration. This will apply to that side of the integration.
* Select if the filtering applies to All, New, and Synced items.
* Note that if the option "New items" is selected, the filtering will apply only to the new items, and the already synced items will continue to sync and update. If the option "Synced items" is selected, only the already synced items will be updated based on that filter.
* Choose the options and add the value for the filter. It is possible to filter more than one option for each field.
* Select Apply once you created the filters and "Save" the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fj33hBBJYnNxJdE34Qsu4%2Fimage-20240715-172050.png?alt=media&#x26;token=b0bc8f18-c5e1-4d1d-8517-3b883073ce80" alt=""><figcaption></figcaption></figure>

#### **13. Test the Integration**

To ensure everything is working correctly, create tasks and go to the reporting section to verify that all syncs are functioning as expected. If you encounter any issues, please contact our support team for assistance.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FVUbYKO22D4G6Io0Bt5XF%2Fimage-20240710-094940.png?alt=media&#x26;token=4e9bb60e-eae8-4159-a740-9884295928cf" alt=""><figcaption></figcaption></figure>

### Conclusion

Following these steps, you can effectively integrate Jira with Hubspot, ensuring smooth synchronization of tasks, issues, and workflows between the two platforms. This setup enhances collaboration and project management processes.

For further assistance contact our support at our [Support Center](https://getint.io/help-center).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FxYEVeDT7MBYDFKg2E56t%2FGetint%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=8db51c7a-b35c-415a-a93c-e2bfb73fb16b" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Jira Jira integration

Integrating Jira with Jira through Getint provides users with a robust solution to streamline project management and collaboration workflows. This powerful integration enables seamless data synchronization across different projects within the same platform, allowing users to efficiently track and manage Jira tickets, tasks, bugs, and epics in diverse Jira environments. For example, a company developing various products such as mobile phones, computers, and smartwatches can benefit from this integration. While each development team operates within its designated Jira environment, Getint facilitates collaboration across projects by enabling integration and filtering of relevant projects, ensuring teams can work together effectively while maintaining appropriate access restrictions.

{% hint style="info" %}
While some steps may vary depending on your current deployment, we support syncing items from Jira Software (Cloud and Service Management), and Jira Data Center.
{% endhint %}

### Jira Jira Licensing Model: <a href="#jira-jira-licensing-model" id="jira-jira-licensing-model"></a>

The Jira Jira licensing model with Getint is designed to accommodate various integration scenarios. Here's a breakdown:

* **Standard Dual Licensing:** This model requires the Getint license to be installed on both Jira instances involved in the integration. This ensures that each instance is properly licensed and can communicate seamlessly.
* **Remote License:** For situations where installing the Getint app on both Jira instances is not feasible (e.g., when integrating with a partner company that doesn't want to install any additional apps), Getint offers a **Remote License** for a fixed fee. This provides a flexible solution for such cases.
* **Flexible License:** For managed services companies or organizations looking to integrate four or more instances (regardless of whether they are the same or different tools), Getint offers a **Flexible License.** This custom license covers a specific number of connections (i.e., up to 10 instances) without restrictions on the tools involved. You can also swap the integrated tools while the license remains active, offering unparalleled flexibility.

For more information about our licensing options, please read [more.](https://docs.getint.io/billing-and-services/licensing)

### Requirements to Build Your Integration: <a href="#requirements-to-build-your-integration" id="requirements-to-build-your-integration"></a>

* The Jira Jira Getint app must be installed on both instances unless you’re opting for a **Remote License** (app installed on a single instance only)**.**
* Both Jira instances should include a dedicated user and an associated API token. These users must have permission to read, write, view, and modify the project.
* Comments are added as the user you chose to create the connection. Therefore, we recommend using dedicated Service Accounts for both instances as comments will be attributed to the user who established the connection.
* Personal Access Tokens to establish the connections. More information about creating API tokens here: [<img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Ficon%2FPRq8D5IBseUvQPEVFVwD%2FGitbook%20getint%20sygnet%20logo.png?alt=media&#x26;token=3353768c-d008-46f7-bc2d-fd71b5d48f14" alt="" data-size="line">Connection](https://docs.getint.io/guides/quickstart/connection#jira).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FJlxO4cRlrnMNKihzj5J7%2FGetint%20White%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=39917e2c-268a-456e-ac81-bc1e9c44b149" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

### Setting up your Jira integration <a href="#setting-up-your-jira-integration" id="setting-up-your-jira-integration"></a>

#### **1. Access the** [**Getint**](https://marketplace.atlassian.com/apps/1223930/issue-sync-integration-for-jira-getint-issue-sync?hosting=cloud\&tab=overview) **App in Jira:**

* Navigate to Jira, go to **Apps**, and select the Getint app (Jira - Jira integration in this case).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FUN0eSqTxVkL47IMsdIeo%2FJira%20jira%20integration%20app.png?alt=media&#x26;token=19eca1f6-9386-4125-b63e-789adba8a461" alt=""><figcaption></figcaption></figure>

* Select **Create Integration** then **Continuous Sync** or **Migration** based on your requirements.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FVNDkkoLk6Xu14yj5iCl7%2FContinuous%20Sync%20or%20Migration.png?alt=media&#x26;token=003d7bef-af3e-4c65-8b63-4938a1485211" alt=""><figcaption></figcaption></figure>

#### **2. Token Generation for Jira:**

#### **Jira Cloud**

* Sign in to your Atlassian account and navigate to the Account Settings.
* Head to the Security section and select **Personal API Token**.
* Click on **Create API token** and provide a label to identify your token easily.
* Hit **Create** to generate the token.
* Copy the token and store it securely in a safe location.

{% embed url="<https://youtu.be/K5jRfZVKLOo>" %}

#### **Jira Data Center**

Unlike Jira Cloud, the Data Center does not require a token and can be accessed using an email and password. If you choose to use a token, leave the **email** option blank on the Getint platform:

1. Log in to your Jira Data Center instance.
2. Click on the Avatar at the top right of the screen.
3. Select **Profile** and then **Personal Access Tokens**.
4. Click on **Create Token**, provide a name for your token, and specify whether the token will expire and when.
5. Copy the token and store it in a safe location.

{% embed url="<https://youtu.be/5bpdLeFn-Qo>" %}

#### **3. Establish a Connection with Jira:**

* Ensure you're logged in as a user with the correct permissions.
* Click **Select App** and choose Jira.
* Select **Create New** to connect with your Jira instance.
* Name your connection, and add the URL of your Jira instance.
* Provide the login credentials.

{% embed url="<https://www.loom.com/share/50ef974c586a49d7b5537bba8106e341?sid=14829839-3999-4a47-921f-b845ea84eac3>" %}

#### **4. Choose and Connect the Second Jira Project:**

* Repeat the process on the other side. Since you are connecting Jira with Jira, repeat the steps.

{% embed url="<https://www.loom.com/share/56ae6bc216d84dccb7a4537f5b2e3cfe?sid=2b0e23d8-ecfb-4c57-a83f-e2b814f900be>" %}

#### **5. Type Mapping:**

* **Quick Build (Beta):** Utilize the Quick Build feature to automatically map fields and types between your applications. This feature simplifies the process.
* **Manual Mapping:** For greater control, manually map the types yourself. This approach lets you tailor the mapping to meet your specific needs. Click **+ Add type mapping** to add Jira types (Task, Bug, Epic, Story) by yourself.
* After configuring your type and field mappings, name and save your integration settings.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fvgv4Ed3JBr6oB9BfWv62%2FQuick%20build%20type%20mapping%20for%20jira%20jira%20integration.png?alt=media&#x26;token=9fc73fd2-4982-4c71-9024-47c9d6d429af" alt=""><figcaption></figcaption></figure>

#### **6. Field Mapping:**

* Review or manually assign the fields to integrate and synchronize within the mapped types, such as title, description, assignees, custom fields, and more.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FFKyYI8y877XWNlRJcVZz%2FJira%20Jira%20field%20mapping.png?alt=media&#x26;token=76754361-8922-4f71-bae0-a8d1f30ca9ca" alt=""><figcaption><p>Example of automatic field mappings with <strong>Quick Build</strong> where you can also add fields manually while using this feature.</p></figcaption></figure>

#### **7. Assignees Mapping:**

* Map assignees according to your organization’s requirements.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FvtpH9DI5um49ZRhuF1rJ%2FAssignees%20in%20Jira%20Jira.png?alt=media&#x26;token=6f9446d9-8b5f-4b97-85bf-c560a4c9e470" alt=""><figcaption></figcaption></figure>

#### **8. How to Manage Comments & Attachments:**

* Review the **Comments & Attachments** tab. These features are enabled by default, but you can adjust them as needed to suit your organization's requirements.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FDnRnJDn3JNloxrt4sR49%2FComments%20%26%20attachment%20sync%20in%20Jira%20Jira%20integration.png?alt=media&#x26;token=084ea820-d684-484a-a7dc-466bde27caf6" alt=""><figcaption></figcaption></figure>

* For Jira Jira integrations, you have the option to further customize comment creation under **Customize comments creation**. This allows you to specify whether comments should be Public, Private, or omitted entirely, providing flexibility to meet your needs.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FCdRqKu8I1O6nirMLgsc1%2FComments%20configuration%20for%20Jira%20Jira%20integrations.png?alt=media&#x26;token=201777d7-fe32-46c8-b041-1e5d06c08e3e" alt=""><figcaption></figcaption></figure>

* You can also modify the sync direction for comments and attachments: **Both ways,** **only to Jira A (left),** or **only to Jira B (right).**

{% hint style="info" %}
You can disable comments and attachments entirely if they are not needed or are restricted in your organization.
{% endhint %}

#### **9. Mapping Statuses**

* Make sure you’re using the correct fields that represent the statuses for each Jira instance.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FmrLnMOwMmMMik0nvWHmz%2FStatus%20for%20Jira%20Jira.png?alt=media&#x26;token=538474c2-8a7d-460b-915d-83a6efb03092" alt=""><figcaption></figcaption></figure>

#### **10. How to Enable Filters:**

It is possible to filter the synchronization to have them customized for your needs and requirements.

#### **UI Filtering**

* After finalizing your integration, you may also add filters to each Jira instance. Select the filter icon adjacent to the app icon within your integration. This action will affect the corresponding side of the integration.
* **Define Filter Rules:**
  * **ALL items filters:** Rules will be verified for every item before synchronization.
  * **NEW items filters:** Rules will be verified only for newly created items that have not yet been synced.
  * **SYNCED items filters:** Rules will be verified for items that were already synced in the past.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fjd5tQYSLDYOmJh7ymHb0%2FJira%20items%20filtering.png?alt=media&#x26;token=98c88e10-4434-4210-a574-a80f911b96dc" alt=""><figcaption><p>For more information about this feature, please visit <a href="https://docs.getint.io/getintio-platform/workflows/items-filtering">Items Filtering.</a></p></figcaption></figure>

#### **JQL Filtering:**&#x20;

* Select the side that will receive the filter.
* Under the field Custom JQL, it is possible to provide a JQL, which will be the filter for your sync and appended to the one generated when searching for issues in Jira (i.e., status in ("In Progress")).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FTuiyjbQeBvITKrW1WXft%2FJira%20JQL.png?alt=media&#x26;token=75b8d907-c0cb-49d6-bfe7-5c6b3c21a39d" alt=""><figcaption></figcaption></figure>

#### **11. Duplicating Your Setup and Selecting Different Projects:**

* Go to Workflows.
* Click the 3 dots on the right side and select **Duplicate**.
* A side panel will appear. Select a new name for the integration (by default, the integration will be called **copy of** if the same projects are established).
* On the dropdown menu, select the projects that you would like to integrate.
* For each side, select **Connect**. Then **Duplicate**.
* Save the new integration.

{% embed url="<https://www.loom.com/share/8e0f7b01d465470498af29b0d3224f23?sid=0746ccf2-4f87-4fcc-90fd-facba4f2befe>" %}

{% hint style="warning" %}
This setup applies to both Jira Software and Jira Service Management, enabling integration of tasks, bugs, and epics, as well as incidents, service requests, and IT help types specific to Jira Service Management.
{% endhint %}

#### **12. Final Steps:**

* Complete the integration setup by naming your project and clicking **SAVE** in the top right corner.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F4DKF862kjSI2O3yK3tsu%2FJira%20Jira%20main%20screen.png?alt=media&#x26;token=0fc09650-7cf6-4813-bcaf-1e7f6180aec6" alt=""><figcaption></figcaption></figure>

At Getint, we're dedicated to providing exceptional support throughout your integration journey. Our team is committed to delivering the best customer experience. For any questions about this integration or assistance with the setup process, don't hesitate to open a ticket at our [Help Center](https://getint.io/help-center) or [Schedule a Demo](https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team). We're here to help!

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Getint Instance URL

The **Getint instance URL** is a unique identifier for a Getint installation. It is used to establish secure connections between Jira instances, validate licenses, and expose important instance metadata. This article explains what the Getint instance URL is, where to find it, and how it’s used in cross-instance configurations.

### What Is the Getint Instance URL? <a href="#what-is-the-getint-instance-url" id="what-is-the-getint-instance-url"></a>

The Getint instance URL uniquely represents a Getint instance running within a Jira environment. It allows Getint to:

* Identify another Getint instance on the “other side” of a connection.
* Validate licensing without querying Jira directly.
* Exchange instance-level metadata, such as version and data residency.

From now on, the Getint instance URL is the **single source of truth** for instance identification and license checks.

### Obtain Your Getint Instance URL <a href="#obtain-your-getint-instance-url" id="obtain-your-getint-instance-url"></a>

Each Jira instance running Getint has its own Getint instance URL.

To find it:

1. Open the **Getint app** in your Jira instance.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F6GI0XTsRJyg2VfloyI1J%2FOpening%20Getint.png?alt=media&#x26;token=aafe6cc9-49d5-4486-b19e-f2d83909e365" alt=""><figcaption></figcaption></figure>

1. Navigate to **Settings**, and open the **General** tab. Your **Getint instance URL** is displayed there.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FB9jS0exj1LMfnVGCzQWD%2FGetint%20Instance%20URL.png?alt=media&#x26;token=428a1786-eeec-41ca-9eaf-4f4d952aea46" alt=""><figcaption></figcaption></figure>

This URL is generated automatically and is specific to that Getint installation.

### Adding the Getint Instance URL to the Connection <a href="#adding-the-getint-instance-url-to-the-connection" id="adding-the-getint-instance-url-to-the-connection"></a>

When setting up a connection between two Jira instances, you must retrieve the URL from the **counterpart** (the Jira instance you are connecting to).

{% hint style="info" %}
You do not need to provide the Getint instance URL in the connection that is running the integration.

The only exception is when a single Getint instance connects to two different Jira instances, for example, one on the left and another on the right. In this scenario, each connected Jira instance must have its corresponding Getint instance URL specified in the connection configuration.
{% endhint %}

1. Go to the connection configuration (**Workflows > Connections**), locate the Jira connection you want to update, and click the **3-dot button** below “Actions.”

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FtB86uz1J6OCbni5yH37I%2FLocate%20the%20second%20jira%20connection.png?alt=media&#x26;token=7e3ef1fa-9069-436c-b485-cabe938accd6" alt=""><figcaption></figcaption></figure>

1. Click on **Edit** to modify the connection.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FY3MjDZy2Zs0Ch95DZ6mb%2FOpening%20the%20actions%20for%20the%20connections%20tab.png?alt=media&#x26;token=4ddecb48-b9ec-4747-86c0-40bb0ef6d0d6" alt=""><figcaption></figcaption></figure>

1. Specify the **Getint instance URL of the partner** (Getint instance on the other side), and hit the **Update** button.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F0uKavt3xNoEXBgSYiC8m%2FEntering%20the%20second%20Jira%20instance%20URL.png?alt=media&#x26;token=27ca6f84-1585-4466-a27e-4bcf172f03d8" alt=""><figcaption></figcaption></figure>

1. Now test your integration. This time, you shouldn’t experience any Jira licensing errors.

Once updated, the two Getint connections are linked, allowing for secure and accurate cross-instance communication.

### Licensing Behavior Using the Getint Instance URL <a href="#licensing-behavior-using-the-getint-instance-url" id="licensing-behavior-using-the-getint-instance-url"></a>

With Forge, licensing is now handled at the Getint level rather than through Jira directly.

* If **Jira 2 is licensed**, license validation is performed by querying the **Getint instance** identified by the provided instance URL.
* Getint no longer asks Jira whether a license exists.
* Instead, Getint asks the **other Getint instance**: “Is there an explicit license associated with this instance URL?”

### Summary <a href="#summary" id="summary"></a>

* Every Getint installation has a unique **Getint instance URL**.
* The instance URL is available in the **Getint app** > **Settings** > **General**.
* No need to specify an ID for your local Jira instance (the Jira that is running the integration), regardless of whether it is configured as the left or the right side of the connection. Just focus on grabbing the Getint URL for the counterpart instance.
* License validation is now performed via Getint using the instance URL, not Jira.
* Additional metadata, such as version and data residency, is tied to the instance URL.

Using the Getint instance URL ensures clear identification, accurate license validation, and a scalable foundation for cross-instance integrations.

### Need Assistance? <a href="#need-assistance" id="need-assistance"></a>

If you encounter any issues retrieving your Getint instance URL, configuring the connection, or validating licensing, please contact our [**Support Team**](https://getint.io/help-center) for assistance.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Jira Jira licensing

Jira Jira Licensing Model Explained

**Overview of Our Licensing Model**

Our standard licensing approach is tailored to the number of connections or instances you're integrating. Simplified, this means you only need a single app installed on Jira to facilitate integration (e.g., connecting 1x Jira instance to 1x Azure DevOps requires just the Jira app).

**Special Considerations for Jira-Jira Integrations**

However, integrating Jira with another Jira (both Software and Service Management) instance necessitates a different model. Why the exception? Previously, our model did not differentiate between the sizes of the companies being integrated. This often led to scenarios where large enterprises were linked with smaller ones, paying only for the smaller instance's license but requiring enterprise-level support and generating data volumes typical of larger organizations. This discrepancy meant the costs incurred by us were not adequately covered by the licensing fees.

To address this, the basic requirement for Jira-Jira integrations is to have a valid license (app installed) on each Jira instance being connected by Getint. The integration can be managed from a single user interface on one of the Jira instances, with the app installation serving primarily for licensing purposes.

**Remote License Option**

We understand there might be situations where installing an app on both Jira instances is not feasible, such as when integrating with a partner company unwilling to install any Jira apps on their end. For these cases, we offer a "Remote License" for a fixed fee, providing a flexible solution to this challenge. For more details, please contact <https://getint.io/help-center>.&#x20;

**Flexible License for Managed Services and Multi-Instance Integrations**

For managed services companies or any organization looking to integrate four or more instances (regardless of whether they are the same or different tools), we introduce our "Flexible License." This custom license fee covers a specific number of connections (e.g., up to 10 instances), without restrictions on the tools involved. You are also free to swap the integrated tools while the license remains active, offering unparalleled flexibility to adapt to changing needs.

For inquiries about our "Remote License" or "Flexible License" options, or for further clarification on our Jira licensing model, please reach out to us. We're here to ensure your integration process is smooth, compliant, and optimized for your specific business requirements.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Time Tracking in Getint – One-Way Synchronization

In Getint, time-tracking synchronization is available, but there are some important distinctions to keep in mind. While the **Original Estimate** can be mapped both ways between systems, the **Remaining Estimate** and **Time Spent** are limited to one-way synchronization. These fields must be mapped to a text field in the target system. In this guide, we will explain how time-tracking synchronization works, and the best way to configure your mappings to ensure accurate and effective data flow.

### Understanding Time Tracking Fields <a href="#understanding-time-tracking-fields" id="understanding-time-tracking-fields"></a>

#### **1. Original Estimate:**

This field represents the initial estimate of time required to complete a task or issue.

* **Two-Way Synchronization**: You can map the **Original Estimate** field in both directions, meaning it can be updated and synced from either system.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fi7nkWtKC56cOkYe86G2r%2FTime%20tracking%20synchronization.png?alt=media&#x26;token=0b14f5c6-ad1e-4f48-8169-b7e9440428a6" alt=""><figcaption></figcaption></figure>

#### **2. Remaining Estimate:**

This field represents the amount of time left to complete the task or issue.

* **One-Way Synchronization**: The **Remaining Estimate** can only be synced in one direction. It needs to be mapped to a text field in the target system. You will see a "read-only" indicator when configuring the mapping, meaning that changes made in the target system will not sync back.

#### **3. Time Spent:**

This field tracks the actual time that has been spent working on a task or issue.

* **One-Way Synchronization**:

Similar to the **Remaining Estimate**, the **Time Spent** field can only be synchronized in one direction and must be mapped to a text field. It cannot be updated from the target system and only serves as a reference.

{% hint style="warning" %}
Note: The mapping of these fields is disabled by default to map both ways.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FOqWTAyOH4RiiANbJL1e2%2FMapping%20these%20fields%20is%20disabled%20by%20default.png?alt=media&#x26;token=d2652203-0000-4a00-8a59-f20aba3bd682" alt=""><figcaption></figcaption></figure>

### Configuring Time Tracking in Getint <a href="#configuring-time-tracking-in-getint" id="configuring-time-tracking-in-getint"></a>

To set up time tracking synchronization, follow these steps:

* **Original Estimate Mapping (Two-Way)**:
  * When mapping the **Original Estimate**, you can choose to sync the field in both directions. This is useful if both systems need to keep track of the initial time estimates for tasks.
  * Select the **Original Estimate** field in both systems during the field mapping process. Ensure that it is mapped as a two-way sync to allow updates from either side.
* **Remaining Estimate & Time Spent Mapping (One-Way)**:
  * For the **Remaining Estimate** and **Time Spent**, select these fields in the source system.
  * In the target system, map these fields to text fields. Since these fields are one-way sync only, you will see a "read-only" label when configuring the mappings, indicating that they can only be updated in the source system.
  * Any updates made in the source system will be reflected as text in the target system.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FXwrJ5UIvwH4NpDZS5eIe%2FConfiguring%20Time%20Tracking%20with%20Getint.png?alt=media&#x26;token=9aa77519-a159-4275-abfc-eebfa610edd6" alt=""><figcaption></figcaption></figure>

### Key Considerations <a href="#key-considerations" id="key-considerations"></a>

* **Text Field Mapping**: Since **Remaining Estimate** and **Time Spent** are mapped to text fields in the target system, their values will not be interactable or updateable in the target system. They serve as a static reference point for the time-tracking data.
* **Read-Only Fields**: These fields are marked as "read-only" during the field mapping process, meaning that changes can only be made from the source system and not in the target system.
* **Consistency**: It's crucial to ensure that your team is aware of the one-way synchronization for the **Remaining Estimate** and **Time Spent** fields. All updates to these fields must be made in the source system to maintain accurate and consistent data across integrations.

### Conclusion <a href="#conclusion" id="conclusion"></a>

Time tracking in Getint provides valuable synchronization options but with some limitations. While the **Original Estimate** can be synchronized both ways, the **Remaining Estimate** and **Time Spent** fields are limited to one-way synchronization and must be mapped to text fields in the target system.

For more detailed guidance or assistance with configuring your time-tracking integration, visit our [Help Center](https://getint.io/help-center).

# Jira Monday.com integration

Integrating Jira with Monday.com using Getint significantly enhances workflows, communication, and migration efficiency. Monday’s user-friendly interface and customizable workflows perfectly complement Jira’s robust issue-tracking capabilities. This integration streamlines tasks, updates, and timelines, thereby maximizing productivity.

With Getint, you can seamlessly integrate your Monday.com boards with Jira Cloud, Jira Data Center, or On-Premise, ensuring efficient synchronization of tasks across your workspace.

### Optimize your workspaces <a href="#optimize-your-workspaces" id="optimize-your-workspaces"></a>

Different projects have different requirements, with this in mind, you may like to track and integrate specific information for your project.

#### How to integrate custom fields for Monday.com integrations <a href="#how-to-integrate-custom-fields-for-monday.com-integrations" id="how-to-integrate-custom-fields-for-monday.com-integrations"></a>

Monday.com has a multitude of custom field types that can be added to your board, make sure to have your board configured beforehand with all the custom fields you would like to integrate so that when creating the integration, you can visualize them for mapping and map them according to their counterpart in Jira.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FAFIwfdw4XKMARc9QLFOA%2FMonday.com%20custom%20fields.png?alt=media&#x26;token=a67c4908-1737-4c7b-ae7f-4c4797802178" alt=""><figcaption><p>Available custom fields in a Monday workspace</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FCweZ6JoSfJD9NAQyvz3o%2FAvailable%20custom%20fields%20in%20Monday%20(1).png?alt=media&#x26;token=211884f2-a283-4f9a-b3d3-f22459dc36f0" alt=""><figcaption><p>Monday board with multiple custom field types added</p></figcaption></figure>

{% hint style="info" %}
Please, note that some custom field types may not be supported by us at the moment.\
In case you need a custom development for your product or project, please get in touch with our [support team](https://getint.io/help-center) for pricing.
{% endhint %}

### Create the integration | Add the connections <a href="#create-the-integration-or-add-the-connections" id="create-the-integration-or-add-the-connections"></a>

#### Access the Getint App in Jira <a href="#access-the-getint-app-in-jira" id="access-the-getint-app-in-jira"></a>

Here we will select the Jira - Monday.com Integration app for this integration, then create the connection for Jira with Jira’s API token and create the connection for Monday.com with Monday’s Personal API Token. Remember to give a name to your integration, then build it.

{% embed url="<https://www.loom.com/share/0e7f6f456796480e9336b09eaabd6f54?sid=aad5c2ff-31ca-4be2-ac39-550dde5cb99d>" %}

\
Navigate to Jira, go to **Apps,** and select the **Jira - Monday.com Integration app**.[<img src="https://marketplace.atlassian.com/s/images/favicon.ico" alt="" data-size="line">Monday.com Jira Integration \[2-way sync + migration\] | Atlassian Marketplace](https://marketplace.atlassian.com/apps/1225780/monday-com-jira-integration-2-way-sync-migration?hosting=cloud\&tab=overview)

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F7lXexX2QfUCfTVvmbgUW%2FJira%20Monday%20Integration.png?alt=media&#x26;token=16a99be7-2bfe-4c0b-8503-a0c0b9862e5b" alt=""><figcaption></figcaption></figure>

* Go to **Workflows,** then **Integrations,** select **Create Integration,** and then **Continuous Sync** or **Migration** based on your requirements.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FDD98e4uQUfBVJfbt9rHb%2FIntegration%20setup%20(2).png?alt=media&#x26;token=cdf5284b-e1b7-4cca-8006-28b5606e6fab" alt=""><figcaption></figcaption></figure>

#### Create the tokens for each workspace <a href="#create-the-tokens-for-each-workspace" id="create-the-tokens-for-each-workspace"></a>

For the integration to work properly, you must grant access to both environments through their respective access tokens.

* You can learn how to create the access token on **Jira** with the below, but you can also follow this article: [<img src="https://wac-cdn.atlassian.com/assets/img/favicons/atlassian/favicon.png" alt="" data-size="line">Manage API tokens for your Atlassian account | Atlassian Support](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/)

{% embed url="<https://www.loom.com/share/5f3b465c73f64fdfb09ceb579e8678fe?sid=4bd29d58-523e-463b-a4a9-2876643a6a31>" %}

* In the video below you can learn how to create an access token for **Monday,** you can also read the instructions in the Monday article: [![](https://files.readme.io/cfbc181-small-favicon-monday5-192.png)Authentication](https://developer.monday.com/api-reference/docs/authentication#accessing-api-tokens)

{% embed url="<https://www.loom.com/share/da2bbdaa0f0049609567868de98753e1?sid=db1e50fe-4f40-4b1c-809c-bffd05b3c3db>" %}

#### Mapping fields <a href="#mapping-fields" id="mapping-fields"></a>

Users can now build an entire integration, with multiple item types and fields mapped, with just a few clicks using our **Quick Build** feature.

**Use the quick build in your integration editor to create your integration from scratch:**

{% embed url="<https://www.loom.com/share/f23c366411a84183a8dcc75015e28ffc?sid=09e4ebb0-d48a-47c4-9359-60d6e1c878b9>" %}

* In your integration editor screen, click **Quick Build.** Next, click **Build,** and wait for the tool to load the item types and their fields.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FiIW2AUYQcJMbwPTHFGUK%2FJira%20Monday%20integration%20quickbuild%20(1).png?alt=media&#x26;token=ea35f41b-142b-4ff7-9988-06f14419cb22" alt=""><figcaption></figcaption></figure>

* Once the app loads the item types and their fields, take your time to check if the item types brought are the desired ones, also all fields brought up are configurable through this screen so you can go through each of them and set them as you desire.
* When you decide that everything is set as you expect, click **Apply.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FS9WKvEpCJn7J3T7dS0W4%2FQuickbuild%20options%20(1).png?alt=media&#x26;token=013511f5-cb2b-483d-aab1-e5b3a3e20a5c" alt=""><figcaption></figcaption></figure>

* If undesirable item types were brought, you can simply delete them through the integration editor. Either create your integration or save it right after.

#### Manually add and configure item types/fields

* Click on the **Add type mapping** button, and the **Map Your Types for a Seamless Integration** tab should pop up:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FxaGsQEL5J64ehoiCl0nP%2Fcreate%20integration%20(1).png?alt=media&#x26;token=b3707e73-0bf2-4417-b9b0-4e84fdda56d1" alt=""><figcaption></figcaption></figure>

* Create a task ↔︎ task, and subtask ↔︎ subtask task type mapping, add your desired fields, and define the sync direction (unidirectional or bi-directional) with the arrows. and configure your task status synchronization. Save your integration at the end:

{% embed url="<https://www.loom.com/share/d4b2a6ac3e8d43a1bc643542fceb6667?sid=2a79fda4-930e-4420-89e4-6b5052d3f35d>" %}

* Use the **Add Mapping Field** button to map different fields of your workspaces to integrate them, the menu at the top can be used to navigate the type mapping configuration screen to edit different settings of your mapping, such as **Status** and **Comments & Attachments.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F2HKgpuZXbahub2S49ltK%2Fadd%20field%20mappings%20(1).png?alt=media&#x26;token=9db15b98-3a8b-45b1-a3d2-9c8d4552e8e0" alt=""><figcaption></figcaption></figure>

* For **Comments & Attachments** in a Monday.com integration, please ensure to enable the attachments as they’re disabled by default. Also, attachments need to be uploaded from the **Files** column in your Monday board, otherwise, they will fail to sync.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FFbY2ezsh6yjDSJXARcTu%2FExample%20attachments%20in%20Monday.com%20(1).png?alt=media&#x26;token=b049e723-1032-4c6e-9102-5520f24185a9" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Always upload attachments from the **FILES** column rather than the **Item/Task** menu to ensure file synchronization with the other app.
{% endhint %}

* Use the step-by-step configurator to add new mappings of different fields from your item types, click on the arrows in the middle to define the synchronization flow (updates only unidirectionally from left to right, from right to left, or bidirectional). At last, click the **Apply** blue button at the right bottom corner to save the changes made.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fl7Jr3cra2jnFI7hU9CCG%2FSync%20direction%20(1).png?alt=media&#x26;token=4a18c55d-34fc-4c47-8eb6-850c426b2e63" alt=""><figcaption></figcaption></figure>

* Map the statuses, use the dropdowns to map them according to your organization parameters, and click Apply to save the changes made.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FTmSPpCi2exPGXDIzdb8K%2FItem%20statuses%20(1).png?alt=media&#x26;token=74499f2e-a623-49a4-b79b-1c03f00d177c" alt=""><figcaption></figcaption></figure>

* Name your integration, then save the changes to create it.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FPnhLKwTad1OvwXvILh55%2FFinishing%20the%20steps%20(1).png?alt=media&#x26;token=04e6a69a-1386-47d7-aea0-758c0a8e1c85" alt=""><figcaption></figcaption></figure>

###

### Create a ticket on both sides to test the integration

Add a comment or attachment and change the task status to ensure the counterpart is capturing the mapped fields correctly:

{% embed url="<https://www.loom.com/share/146ea35ca30b44caad040ceebcc41896?sid=c4221468-de8f-46eb-9dca-bd25a7f372f0>" %}

{% hint style="warning" %}
Please be aware that replies to comments (also known as subcomments) are not supported by Getint, and they will not trigger synchronization. If an update is added before a sync is triggered, and a reply is subsequently added to the update, the tool will bring the subcomment to the other side. However, due to a technical limitation from Monday, we cannot guarantee that this will work consistently, to manage expectations.
{% endhint %}

At Getint, we take feedback and customer inquiries seriously. Therefore, if you bump into an error while trying to integrate your software, or if you have any custom requirements, please raise a ticket at our support channel [here.](https://getint.io/help-center)

# Synchronizing Attachments in a Monday.com Integration

Our tool allows users to migrate and synchronize attachments from Monday tasks to other management software we support. However, please note that inline images are not currently supported for synchronization.

### Key Points and Considerations

* **File Size Limit:** Monday enforces a 500MB file size limit for task attachments. Be mindful of this limitation when dealing with large files.
* **Inline Images:** We currently do not support inline images. Please note that they won’t be properly synchronized.
* **Enabling the Feature:** Attachments are disabled by default. They need to be activated manually within your integration settings.
* **Attachments Limitation:** Uploading attachments from the **Files** section within the tasks is not supported. Attachments need to be uploaded from the **Files** column in your Monday.com board.

### How to Sync Attachments

1. Navigate to the **Comments & Attachments** section in the mapping configuration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FQrp8CbILMsi1hHkWofHf%2Fa34213f4177462df29ea7dad21d2f5c6%20(1).png?alt=media&#x26;token=e2c904c4-1970-4a59-b14a-70d3b4491b51" alt=""><figcaption></figcaption></figure>

1. Scroll down to **Synchronize attachments** and enable the option.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fh9b5RJCvyw8z4fhn7OGu%2Fd911384ed3bc3c5ad3d26144c1d4f7ed%20(1).png?alt=media&#x26;token=75eacc76-0380-4c37-a2de-f3e1e281758f" alt=""><figcaption></figcaption></figure>

1. Go to your **Monday.com** workspace and upload attachments from the **FILES** column in your **Monday.com board.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FJ8T51cY4WjQazE4aIwar%2F995b3b95f73710e20e90b5e47dc98ad9%20(1).png?alt=media&#x26;token=f5e4521e-6be0-47ae-950b-d5087710c542" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Always upload attachments from the **FILES** column rather than the **Item/Task** menu to ensure file synchronization with the other app.
{% endhint %}

1. Choose the synchronization direction for your attachments. Options include **Both ways** (bi-directional sync), **Only to app A** (left)**,** and **Only to app B** (right) for unidirectional sync.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FtXA0rXE7wWv1s9lWXpUB%2F89c8394ecae512c8332629137caae364%20(1).png?alt=media&#x26;token=23ff5d7d-5d06-4e07-8352-8792e589b8f2" alt=""><figcaption></figcaption></figure>

1. Click **Apply** at the bottom right to submit your changes. Then, **Save** your integration.

{% hint style="info" %}
If you’re experiencing difficulties syncing attachments or have any other questions, please contact us at our [Support Center.](https://getint.io/help-center)
{% endhint %}

# How to Insert Monday.com Items into Specific Groups Using Getint

Groups on Monday provide a way to organize tasks, projects, and workflows efficiently. When integrating with Jira, Asana, Azure DevOps, or other tools through Getint, users may need to automatically assign items to specific groups instead of having them placed in a default category.

This guide explains how to configure custom field mapping to ensure that items land in the correct group during synchronization.

### Why Assign Items to Specific Groups <a href="#why-assign-items-to-specific-groups" id="why-assign-items-to-specific-groups"></a>

By default, new tasks synced into Monday may not be placed in the intended group, requiring manual adjustments. Using custom field mapping, teams can ensure items are categorized correctly without additional effort.

#### Benefits <a href="#benefits" id="benefits"></a>

* Improves organization by ensuring items are placed in the right group automatically.
* Reduces the need to manually move tasks after sync.

#### **Step 1: Create a Custom Field in the Source Tool** <a href="#step-1-create-a-custom-field-in-the-source-tool" id="step-1-create-a-custom-field-in-the-source-tool"></a>

To enable group assignment, a custom field must be created in the source tool. This field will determine where each item is placed on Monday.

Since the process varies by platform, refer to the official instructions for creating custom fields. For this guide, we will use Jira - Monday integration:

* [**How to Create a Custom Field in Supported Software**](https://getintio.atlassian.net/wiki/spaces/Support/pages/898170881/How+to+Insert+Monday.com+Items+into+Specific+Groups+Using+Getint) (full guide).
* **Jira** - follow the steps on [Create a Custom Field](https://support.atlassian.com/jira-cloud-administration/docs/create-a-custom-field/) and add the field to the issue types:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FUb2lOFcqaKZkIh3HldpV%2FCreating%20groups%20in%20Jira.png?alt=media&#x26;token=5968a2c6-ae26-4948-8956-4eb5e91dcb61" alt=""><figcaption></figcaption></figure>

When setting up the field:

* Use a **Dropdown (Single Select) or Picklist** to match group values.
* Ensure that all issue types contain the new field.

#### **Step 2: Map the Custom Field to Monday.com** **Groups in Getint** <a href="#step-2-map-the-custom-field-to-monday.com-groups-in-getint" id="step-2-map-the-custom-field-to-monday.com-groups-in-getint"></a>

Once the custom field is set up, configure Getint to recognize and use it for group assignment.

* Open **Getint** and navigate to the integration.
* Select **Type Mapping** then add **Field Mapping** and locate the custom field created in Step 1. Map this field to the **Group** field in Monday.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FvCcxc9MmPTivqMS6xWmf%2FMapping%20the%20Groups.png?alt=media&#x26;token=763ab96f-8246-4f05-b167-4a7cfb7e403b" alt=""><figcaption></figcaption></figure>

* Click on the cog icon to match the groups.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FuPiSUQDUK0zH1h9GxUUy%2FMapping%20the%20available%20options%20in%20the%20groups.png?alt=media&#x26;token=2e310605-243d-4181-9816-51dbb2793790" alt=""><figcaption></figcaption></figure>

* Define the synchronization direction:
  * **Unidirectional (Source to Monday)** – Items are assigned a group based on the source tool but will not update if moved manually
  * **Bidirectional (Sync Both Ways)** – Group changes will reflect in both systems
* Click **Save** to apply the mapping

{% hint style="warning" %}
The Group field **must be** mapped to a dedicated custom field instead of a status field, as statuses function separately in synchronization.
{% endhint %}

#### **Step 3: Test the Integration** <a href="#step-3-test-the-integration" id="step-3-test-the-integration"></a>

Once the setup is complete, verify that it functions correctly by testing with new items.

* Create a task in the source tool and set the **Group Assignment** field to a specific group.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FQwdKDVo5EYfUm3Fm89jA%2FGroup%20assignment%20from%20Jira.png?alt=media&#x26;token=f020dbb7-b0ac-47dd-97ed-7f7b3345a99c" alt=""><figcaption></figcaption></figure>

* Wait for the sync to happen and check that the item appears in the correct group.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FfVfpsJtwv98IQXXo8rhb%2FChecking%20Syncs%20with%20Monday%20Groups.png?alt=media&#x26;token=7aebe415-65e8-4db9-b090-fee2e6c34a17" alt=""><figcaption><p>Ticket assigned to the Group selected</p></figcaption></figure>

If items are not assigned as expected, review:

* The values entered in the custom field
* Field mapping settings in Getint
* Sync logs for potential mapping errors

### Conclusion <a href="#conclusion" id="conclusion"></a>

By mapping a custom field in the source tool to the **Group field**, users can ensure that items are automatically placed in the correct category, eliminating manual adjustments and improving workflow efficiency.

For further assistance, check the [**Getint Help Center**](https://getint.io/help-center) or contact support.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FLilxKjQzV1V0fHEgCW7L%2FGetint%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=78a1f8e4-f61d-4357-a8a6-5fa09126b06a" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues to build your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>

# Jira Notion integration

Getint's Jira-Notion integration enables users to sync project data between the two platforms. Once set up, users can view and manage Jira tickets, tasks, bugs, and epics directly within Notion, providing a unified workspace for project tracking and team collaboration. Initially, the integration supports syncing only the title and description fields between Jira and Notion items, with plans to map additional fields like assignees, statuses, labels, and custom fields in future updates.

As a relatively new integration, full feature parity between Jira and Notion may not yet be available. However, Getint is committed to ongoing development and values user feedback to prioritize and expand integration capabilities. If certain functionalities are missing or challenges arise during setup, users are encouraged to reach out. The guide below offers a 3-minute setup process for a functional MVP integration, with Getint's dedicated team available for personalized onboarding, expert support, custom script assistance for complex scenarios, and bespoke development solutions.

{% embed url="<https://youtu.be/ZNZPsiZNzps>" %}

#### **1. Access the** [**Getint**](http://getint.io/) **App in Jira:** <a href="#id-0.-access-the-getint-app-in-jira" id="id-0.-access-the-getint-app-in-jira"></a>

* Navigate to Jira, go to "Apps," and select "the Getint app."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FFPDFjQAZcRht2DpWeCsE%2FNotion%20integration%20app%20for%20Jira.png?alt=media&#x26;token=f867ab55-ee7e-4e07-b8f3-44f144b6fa53" alt=""><figcaption></figcaption></figure>

* Select "Create Integration" then "Continuous Sync" or "Migration" based on your requirements.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FxPQuHRml69V0fkrvIo4P%2FSelecting%20Continuos%20Sync%20or%20Migration.png?alt=media&#x26;token=516a4fc0-d24a-4642-9699-ce6f852b9dd6" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fa1Z99b8khISGbcsrb4qr%2FGetint%20White%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=526d7a99-8a15-4fda-b829-7263c748214b" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>

#### **2. Token Generation for Jira Cloud:** <a href="#id-1.-token-generation-for-jira-cloud" id="id-1.-token-generation-for-jira-cloud"></a>

* Visit Atlassian Account Settings.

{% embed url="<https://www.loom.com/share/21ed10cc0c7c4b34893f04497ca04ddd?sid=773e4e8d-98ee-4820-8aa9-2e561500474f>" %}

* Go to Security
* Navigate to the API Token section and generate a token. This token serves as the password for Jira Cloud.

{% embed url="<https://www.loom.com/share/f8246071639a484193fb5ee247e07a9b?sid=a5718d6a-1033-4cf7-9df2-002998207c36>" %}

#### **3. Establish a** **Connection with Jira:**  <a href="#id-2.-establish-a-connection-with-jira" id="id-2.-establish-a-connection-with-jira"></a>

* Ensure you're logged in as a user with the correct permissions
* Click "Select App" and choose Jira.
* Select "Create New" to establish a new connection with your Jira instance.
* Name your connection, and add the URL of your Jira instance (without "/" at the end).
* Provide the login credentials.

{% embed url="<https://youtu.be/xOg076frYw4>" %}

**4. Choose the Jira Project:**

* With a successful connection, a dropdown menu will appear.
* Select the Jira project you want to integrate.

{% embed url="<https://youtu.be/aiknGfYdbD8>" %}

**5. Connect to Notion:**

* In the Notion app, click on the three dots in the top right corner.
* Select "Add a Connection," then navigate to "Manage Connections" and choose "Develop or Manage integrations."

{% embed url="<https://youtu.be/IXr52732ppM>" %}

* Select "New Integration."
* Provide a name for your integration, grant necessary permissions, and copy the API token.

{% embed url="<https://youtu.be/yliJs_muuJQ>" %}

* Close the window, return to the Notion dashboard, and click on the three dots again.
* Scroll down to add a connection and select the name of the connection that you have already created.

{% embed url="<https://youtu.be/XL5xE3xe0Ps>" %}

{% hint style="info" %}
It might be necessary to refresh your browser to see the new connection in the list.
{% endhint %}

#### **6. Configure** [**Getint**](http://getint.io/) **for Notion:** <a href="#id-5.-configure-getint-for-notion" id="id-5.-configure-getint-for-notion"></a>

* In the [Getint](http://getint.io/) app, choose "Notion" as the connection app.
* Select "Create a new connection," name it, and provide the API Token.
* Select the connection you want to integrate.
* Choose the Notion database to synchronize.

{% embed url="<https://youtu.be/XKd0gczYqNU>" %}

#### **7. Map Types:** <a href="#id-6.-map-types" id="id-6.-map-types"></a>

* Link Jira types (Task, Bug, Epic, Story) to synchronize in Notion.
* Specify the fields for integration or synchronization.

{% embed url="<https://youtu.be/Dn5ZclInIcY>" %}

{% hint style="info" %}
Please note that the current version of Getint for Notion only supports the "Title" and "Description" fields. For syncing other fields like assignees, statuses, labels, or custom fields, please contact us directly at <https://getint.io/help-center>.
{% endhint %}

#### **8. Field Mapping:** <a href="#id-7.-field-mapping" id="id-7.-field-mapping"></a>

* Map key fields such as title/summary and description
* After configuring, name and save your integration settings.

{% embed url="<https://youtu.be/BMJJtQk3YW0>" %}

{% hint style="warning" %}
The "Description" field in Notion supports a maximum of 2000 characters. To avoid sync errors and blank description fields when transferring text from Jira to Notion, ensure your content does not exceed this limit. Keeping descriptions concise and within the character count helps maintain data integrity and prevents synchronization issues.
{% endhint %}

#### **9. Filtering:** <a href="#id-8.-filtering" id="id-8.-filtering"></a>

It is possible to filter the synchronization to have them customized for your needs and requirements.

**UI Filtering Option:**&#x20;

* Click on the filtering icon near the app icon in your integration. This will apply to that side of the integration.
* Select if the filtering will apply to All items, New items, and Synced items.
* Note that if the option "*New items"* is selected, the filtering will apply only to the new items, and the already synced items will continue to sync and update. If the option "*Synced items"* is selected, only the already synced items will be updated based on that filter.
* Choose the options and add the value for the filter. It is possible to filter more than one option for each field.
* Select Apply once you created the filters and Save the integration.

{% embed url="<https://youtu.be/Hp7q8IQwFng>" %}

**JQL Filtering:**&#x20;

* Select the app that will receive the filter.
* Under the field Custom JQL, it is possible to provide a JQL, which will be the filter for your sync and appended to the one generated when searching for issues in Jira (e.g., status in ('In Progress')).
* Save the integration.

{% embed url="<https://youtu.be/1uy9T0hKl7o>" %}

#### **10. Duplicate Setup and Select Different Projects:** <a href="#id-9.-duplicate-setup-and-select-different-projects" id="id-9.-duplicate-setup-and-select-different-projects"></a>

* Go to Workflows.
* Click on the 3 dots on the right side and select "duplicate."
* A side panel will appear. Select a new name for the integration (by default, the integration will be called “copy of” if the same projects are established).
* On the dropdown menu, select the projects that you would like to integrate.
* For each side, select Connect. Then Duplicate.
* Save the new integration.

{% embed url="<https://youtu.be/ut7MxxAQ8Vk>" %}

{% hint style="info" %}
If you require further assistance with your integration or if you have any questions about Getint, feel free to open a ticket at our [Support Center](https://getint.io/help-center) or [Schedule a Demo](https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team).
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F4q6IDb8EZjgAx52jlppF%2FGetint%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=faae9475-d471-4886-adbe-386a97632e80" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Jira Salesforce integration

Integrating Salesforce with Jira using Getint improves team collaboration. Real-time data sync allows the management of customer requests, tasks, bugs, and projects without manual input. This integration supports Salesforce Lightning, Classic, and various Jira deployments, including Cloud, Data Center, and Service Management.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F2qEXNxGFHbXeqES3p4dE%2FSalesforce%20Integration%20for%20Jira.png?alt=media&#x26;token=794f5956-471a-46f2-9fba-aa37fd7ea671" alt=""><figcaption><p>Check out our Salesforce integration app on the Atlassian Marketplace</p></figcaption></figure>

### **Salesforce-Jira Licensing Model** <a href="#salesforce-jira-licensing-model" id="salesforce-jira-licensing-model"></a>

The **Salesforce-Jira licensing model** with Getint is designed to accommodate different integration needs. Here’s an overview:

#### **Standard Licensing** <a href="#standard-licensing" id="standard-licensing"></a>

* A Getint license is only required on Jira, allowing seamless data synchronization between Salesforce and Jira.
* This makes setup simpler and faster, without the need for additional configurations in Salesforce.

#### **Flexible License** <a href="#flexible-license" id="flexible-license"></a>

* For managed services companies or organizations looking to integrate four or more instances (regardless of whether they are the same or different tools), Getint offers a **Flexible License.** This custom license covers a specific number of connections (i.e., up to 10 instances) without restrictions on the tools involved. You can also swap the integrated tools while the license remains active, offering unparalleled flexibility.

For more details on licensing, visit our [**Pricing Page**](https://docs.getint.io/billing-and-services/licensing)**.**

### **Requirements to Build Your Integration** <a href="#requirements-to-build-your-integration" id="requirements-to-build-your-integration"></a>

* The **Getint app** must be installed in Jira.

#### **Salesforce API Requirements** <a href="#salesforce-api-requirements" id="salesforce-api-requirements"></a>

Salesforce requires API access for integration. API access is enabled by default in the following editions:

* Enterprise Edition
* Unlimited Edition
* Performance Edition
* Developer Edition

API access is **NOT enabled** by default in:

* Group Edition
* Essentials Edition
* Professional Edition

{% hint style="info" %}
If using a Salesforce edition without API access enabled, please contact Salesforce support or refer to the Salesforce Help & Training Community.
{% endhint %}

#### **Authentication and Access Requirements** <a href="#authentication-and-access-requirements" id="authentication-and-access-requirements"></a>

* OAuth authentication is required to establish a secure connection between Salesforce and Jira.
* Comments are attributed to the user who created the connection. Therefore, we recommend using dedicated Service Accounts for both instances.
* Jira instances must have a dedicated user and an associated API token with permissions to read, write, view, and modify the project.
* **Personal Access Tokens** are required for Jira authentication. Learn more here: [Connection Guide](https://docs.getint.io/guides/quickstart/connection#salesforce).

### **Setting Up Your Salesforce-Jira Integration** <a href="#setting-up-your-salesforce-jira-integration" id="setting-up-your-salesforce-jira-integration"></a>

#### **1. Access the** [**Getint**](https://marketplace.atlassian.com/apps/1223930/issue-sync-integration-for-jira-getint-issue-sync?hosting=cloud\&tab=overview) **App in Jira:**

* Navigate to Jira, go to Apps, and select the Getint app (Salesforce integration for Jira in this case).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FyK2OhTeupywShD8810yD%2FSelecting%20the%20Jira%20Salesforce%20app.png?alt=media&#x26;token=73aefd46-0f0e-486e-b9f0-21d2b92a37bb" alt=""><figcaption></figcaption></figure>

#### **2. Create Integration**

Click **Create Integration** and select either:

* **Continuous Sync** for ongoing synchronization.
* **Migration** for a one-time data transfer.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FEFVi5oJIlDxyWWYIprla%2FSelecting%20Continuos%20Sync%20or%20Migration.png?alt=media&#x26;token=45b25f45-0a77-40f7-aa82-dba35b27ca82" alt=""><figcaption></figcaption></figure>

#### **3. Generate a Jira API Token**

* Log in to your Atlassian account and navigate to **Account Settings > Security**.
* Generate an API token.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FhfzIIgY8fiL0vtQiPEZ1%2FCreating%20an%20API%20token%20for%20Jira%20Salesforce.png?alt=media&#x26;token=c2960bad-ec80-4ab7-b768-f8af8abb58e9" alt=""><figcaption></figcaption></figure>

* Copy and securely store the token, as it will be used as the password for Jira Cloud.

For detailed steps, refer to our guide [Connection](https://docs.getint.io/guides/quickstart/connection#jira).

#### **4. Create a connection to Jira and Salesforce and authorize Getint**

**Jira Connection:**

* Select the **Jira** app. Then enter your Jira instance **URL**, username, and Access token generated.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F49m2fgJzZ7xSnTXFZAPW%2FConnection%20with%20Jira.png?alt=media&#x26;token=cc87470e-980a-4eeb-813e-b9404ed82f92" alt=""><figcaption></figcaption></figure>

* Select the Jira project you want to synchronize and select **Connect**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FfyI3T747GlRa9j6riDDo%2Festablishing%20a%20connection%20with%20Jira.png?alt=media&#x26;token=cdd19a39-3c27-435e-b3a5-0223cb84a0fe" alt=""><figcaption></figcaption></figure>

#### **Salesforce Connection:**

* Select **Salesforce** and click **Create a Connection**.
* Enter your Salesforce instance URL in the **URL** field and click **Next**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FFZ4r8qYmAVmFyfXWdi4C%2FEstablishing%20a%20connection%20with%20Salesforce.png?alt=media&#x26;token=830a89fa-6026-4060-8c47-855e85e73159" alt=""><figcaption></figcaption></figure>

* Assign a name to the connection and enter the **client\_id** and **client\_secret** credentials.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F0yfhjmL41mlSI3JDlqEJ%2FCreating%20a%20connection%20with%20Salesforce.png?alt=media&#x26;token=952855e4-2592-4892-819b-0fe85e914619" alt=""><figcaption></figcaption></figure>

* **Add** the connection and select it.

{% hint style="info" %}
For detailed steps on how to configure your **Salesforce credentials**, please refer to our guide [Connection](https://docs.getint.io/guides/integration-synchronization/jira-salesforce-integration/salesforce-oauth-authentication).
{% endhint %}

#### **6. Configure Type Mapping**

* **Quick Build (Beta):** Use the Quick Build feature to automatically map fields and types between applications, simplifying the process.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FVu1lj4Q4F4kapIbW3ni6%2FUsing%20quickbuild%20for%20a%20Jira%20Salesforce%20integration.png?alt=media&#x26;token=17c3e67b-cc1a-4b0b-b0fa-0b528dfe0405" alt=""><figcaption></figcaption></figure>

* **Manual Mapping:** For greater control, manually map the types yourself. This approach lets you tailor the mapping to meet your specific needs. Click **+ Add type mapping** to add the types (Case, Task, Bug, Epic, Story) by yourself.
  * **Story ↔ Case**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fq0FgOjEMiUyPYimZE0oY%2FAdding%20a%20manual%20mapping%20Jira%20Salesforce.png?alt=media&#x26;token=94ca3ce7-981b-4f0e-972d-b024413e44d0" alt=""><figcaption></figcaption></figure>

#### **7. Configure Field Mapping**

* Select the fields to synchronize, such as **Title**, **Description**, **Assignees**, and **Custom** fields.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX0ANoBXjkRTzv4sK5fQR%2Ffield%20mappings%20in%20Salesforce%20integration.png?alt=media&#x26;token=d44a911b-ee24-4fa4-8662-7f522f9af176" alt=""><figcaption></figcaption></figure>

* Ensure synchronization flow is defined for each field, using the arrows and selecting **Apply**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FV5XTfLWJqWB0Pict3skP%2FChoosing%20the%20sync%20direction.png?alt=media&#x26;token=8e30bcdf-fd73-46df-acb6-4ef193245b37" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Some custom field types may not be supported. Please check our [Connectors Salesforce page](https://docs.getint.io/getting-started-with-the-platform/apps-connectors/salesforce) for a list of supported fields. If a field is missing or you need custom development, visit our [Help Center](https://getint.io/help-center).
{% endhint %}

#### **8. Configure Status Mapping**

Ensure you are using the correct fields for each instance's status.

* Navigate to the **Status Mapping** tab.
* Use the dropdown menu to map Salesforce statuses to their Jira equivalents (e.g., **Open ↔ To Do**).
* **Apply** the status mappings.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FxXZX352z8tmmZtuajaxc%2Ftype%20mapping%20configuration.png?alt=media&#x26;token=9a1e34ee-8ddd-4a29-bb0f-d3889dfb1504" alt=""><figcaption></figcaption></figure>

#### **9. How to Manage Comments & Attachments:**

* Review the **Comments & Attachments** tab. These features are enabled by default but can be adjusted to meet your organization's needs.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FWfddpamcXLWps9wrnxQT%2Fcomments%20%26%20attachments%20jira%20salesforce.png?alt=media&#x26;token=121d799f-8630-4693-93f2-7cde99dcd8ad" alt=""><figcaption></figcaption></figure>

* You can adjust the sync direction for comments and attachments to be bidirectional, **unidirectional to Jira**, or **unidirectional to Salesforce**. Also, you can completely disable comments and attachments if they are unnecessary or restricted in your organization.

{% hint style="warning" %}
Comments and attachments do not automatically sync from Salesforce to Jira. To ensure they appear in Jira, update either the Salesforce ticket or the Jira ticket, depending on whether bidirectional sync is enabled.
{% endhint %}

#### **10. Filtering Option**

Customize synchronization by applying filters:

* After completing your integration, add filters to each app by clicking the filter icon next to its app icon. This will affect the corresponding side of the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FM5N89dkWN1egx0Ct3OnT%2FUI%20filters%20Jira%20Salesforce.png?alt=media&#x26;token=32d48849-6a50-44d3-8802-03928fed52f3" alt=""><figcaption></figcaption></figure>

* Choose the filter scope:
  * **ALL items filter:** Rules will be verified for every item before synchronization.
  * **NEW items filter:** Rules will be verified only for newly created items that have not yet been synced.
  * **SYNCED items filter:** Rules will be verified for items that were already synced in the past.

Add values for the filters and click **Apply**. For more details on how to use the filter, refer to our [Filtering Guide](https://docs.getint.io/getintio-platform/workflows/items-filtering).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F7tJBiZKGYu4x6lEAPlQz%2FFiltering%20options%20Jira%20Salesforce.png?alt=media&#x26;token=2d9bf42a-e42a-4060-b716-ff83b77a411b" alt=""><figcaption></figcaption></figure>

#### **JQL Filtering (For Jira Side Only)**

* In addition to the Item Filtering options mentioned above, Jira apps also support JQL (Jira Query Language) Filtering, allowing you to refine and customize which items are included in the sync.
* Under the field Custom JQL, it is possible to provide a JQL, which will be the filter for your sync and appended to the one generated when searching for issues in Jira (i.e., status in (“In Progress”)).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FkG3TMZ2rZuszUvtrtdpp%2FJQL%20filtering%20options.png?alt=media&#x26;token=22c7eff4-d46d-4021-88d4-a846acbb32bd" alt=""><figcaption></figcaption></figure>

* Name your integration and click on **Create** to save the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMBxugNOPFUg5jQXtOTT7%2FSaving%20the%20integration.png?alt=media&#x26;token=76d19028-f188-43ba-a707-5394cb4d72ec" alt=""><figcaption></figcaption></figure>

#### **11. Test the Integration**

* Create a test case in Salesforce and a test task in Jira.
* Verify synchronization by performing actions like adding comments, attachments, or changing statuses.
* Check logs in Getint to ensure the integration is working as expected.

{% embed url="<https://www.loom.com/share/31c28c0ceade49319dfd3868c628188b?sid=12551b4c-3a64-4957-94fd-5f8b39c8f5f7>" %}

#### **12. Duplicating Your Setup and Selecting Different Projects:**

* Navigate to Workflows.
* Click the three dots on the right and choose Duplicate.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F7foFv7QPO0Zgc0AKm4vz%2FDuplicating%20your%20integration.png?alt=media&#x26;token=4973c435-dc92-4d94-b256-9b4837f7f4be" alt=""><figcaption></figcaption></figure>

* A side panel will appear. Enter a new name for the integration, which defaults to "copy" if the same projects are used.
* In the dropdown menu, choose the projects to integrate.
* For each side, click Connect, then Duplicate.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FWM4ZCQ02wrIB7yvaGWRW%2FCopying%20the%20Jira%20Salesforce%20integration.png?alt=media&#x26;token=ab554067-a169-4502-9350-90bff27ae515" alt=""><figcaption></figcaption></figure>

* Save the new integration.

### **Conclusion** <a href="#conclusion" id="conclusion"></a>

At Getint, we're dedicated to providing exceptional support throughout your integration journey. Our team is committed to delivering the best customer experience. For any questions about this integration or assistance with the setup process, don't hesitate to open a ticket at our [Help Center](https://getint.io/help-center) or [Schedule a Demo](https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team). We're here to help!

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Salesforce OAuth Authentication

Starting version 1.78, Salesforce customers must configure OAuth authentication, deprecating our previous connection method. To do this, start by creating the necessary credentials in Salesforce. These credentials will connect your Salesforce instance and Getint, facilitating smooth and efficient data synchronization.

### How to Set Up OAuth Authentication in Salesforce <a href="#how-to-set-up-oauth-authentication-in-salesforce" id="how-to-set-up-oauth-authentication-in-salesforce"></a>

1. Log in to your Salesforce instance, click the **Cog icon** in the top right corner of your screen, and click on **Setup** to open your user settings.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FVQqhPKV4BmH8BgZxNpAt%2Fa6c9112bffc8242333cbcb242573c2f6.png?alt=media&#x26;token=aadf95ad-d071-4117-9a98-20236e2c809f" alt=""><figcaption></figcaption></figure>

1. Go to **Platform Tools** > **Apps** > **External Client Apps** > **External Client App Manager.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FkMTgXBtjiwoA9MNg7DJT%2FExternal%20Client%20App%20Manager.png?alt=media&#x26;token=7b09ab4a-e82f-4b5a-badf-c94c4762f3f5" alt=""><figcaption></figcaption></figure>

1. Click **New External Client App.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FOyZLjcBeLP9SWNcfGs80%2FNew%20External%20Client%20App.png?alt=media&#x26;token=520c5714-b60e-4119-b23d-eb99bc0d54bc" alt=""><figcaption></figcaption></figure>

1. Provide a **custom name**, **your email**, and the **API name.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FsDLojbocuKUMO6OZqijl%2FExternal%20Client%20App%20Manager%20Setup.png?alt=media&#x26;token=dfb9525c-882e-4338-a10c-d61d30fb1b47" alt=""><figcaption></figcaption></figure>

1. **Enable OAuth**:
   * Scroll down and enable **OAuth.**
   * Provide the **Callback URL:** `https://login.salesforce.com/services/oauth2/callback`.
   * Select the **OAuth Scope:** The only one required is *Manage user data via APIs (API).*

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FI85U9OjfcVAAGOfI0UuB%2FEnabling%20API%20Settings.png?alt=media&#x26;token=5590ba5b-5581-4549-b621-aa963d9bd84a" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Salesforce requires the Callback URL to use HTTPS for security purposes.
{% endhint %}

1. Scroll down to the section **Flow Enablement** and enable **Client Credentials Flow**. Then, disable the rest of the options in the **Security** section.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FvUPHXsxVYX2EH2QYmurf%2FEnable%20Client%20Credentials%20Flow.png?alt=media&#x26;token=b072a14a-a81f-4860-a67b-08cbb7e4b101" alt=""><figcaption></figcaption></figure>

1. **Create the External Client App**:
   * Click **Create** at the bottom of the screen.
   * After creation, navigate back to edit settings. The new Client should’ve been created.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FlGZxon9zRTWIwfwuITzH%2FNew%20client%20created%20(1).png?alt=media&#x26;token=056f78bd-ce9c-42bd-9d76-e57ebff3a17d" alt=""><figcaption></figcaption></figure>

1. **Edit Settings for the new Client**:
   * Click **Edit**, and display the **OAuth Policies**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FIqvo3Na3RMQHFpEkZJC8%2FNew%20client%20created.png?alt=media&#x26;token=4712917e-5b34-437b-bb79-cca997dcf1c5" alt=""><figcaption></figcaption></figure>

1. Enable **Client Credentials Flow** and provide the username found under **Personal Information** in your profile. Then, click **Save** to submit your changes.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fb03ppB2fZCtf9huCVhnN%2FOAuth%20Flows%20and%20External%20Client%20app%20Enhancements.png?alt=media&#x26;token=b8b2e41f-ae3e-4e14-b85b-eb193b328fb3" alt=""><figcaption></figcaption></figure>

1. **Generate** `client_id` **and** `client_secret`**:**
    * Switch from the **Policies** tab to the **Settings** tab.
    * Click **Consumer Key and Secret**.
    * It will redirect you to the verification screen.
    * Copy the **Consumer Key (**`client_id`**)** and **Consumer Secret (**`client_secret`**)**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FEuJc4jgls9nAO4wUFyOx%2Fgenerating%20ID%20and%20Secret.png?alt=media&#x26;token=397cd405-475b-4889-8e12-4d9bc0e4cc4e" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FAkuqHtW9dPOxOhuSXSy6%2FClient%20ID%20and%20Secret.png?alt=media&#x26;token=6ed14864-b0fe-4373-8319-b1a751b15c89" alt=""><figcaption><p>With these credentials, you can create a connection with Salesforce in Getint.</p></figcaption></figure>

1. **Create a Salesforce Connection in Getint**:
    * Select **Salesforce** and click **Create a Connection.**
    * Enter your **Salesforce Instance URL** in the URL field and click **Next.**
    * Name the connection and provide the **client\_id** and **client\_secret.**
    * Add and select the connection to finalize the process.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMqy14CoUOm09U74YGxOk%2FCreating%20a%20connection%20with%20Salesforce.png?alt=media&#x26;token=55e9c9d8-4a81-417e-a856-65a80f555f82" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Ensure to use the correct URLs to connect to your instance:

* <https://YOUR\\_INSTANCE\\_NAME.develop.lightning.force.com>
* <https://YOUR\\_INSTANCE\\_NAME.develop.my.salesforce.com>
  {% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FU4wZvYTDfP4G94OnTsEe%2FGetint%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=09b1ea50-e0e3-47c0-bdc3-97ad8c38ef6e" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues to build your integration? Schedule a free consultation with our Integration Experts now!</a><br></p></figcaption></figure>

# Jira ServiceNow integration

Easily integrate Jira and Jira Service Management with ServiceNow for enhanced workflow efficiency. You can ensure data consistency by bridging the gap between IT teams (using ServiceNow) and software development teams (relying on Jira). The integration provides a unified workspace where users can manage Jira incidents, problems, changes, and service requests within ServiceNow, and vice versa. Set up the Jira-ServiceNow integration using the application available in the Atlassian Marketplace (for cloud customers), the Data Center apps, or the On-Premise version of Getint. This bi-directional integration allows you to send ServiceNow incident events to Jira Service Management and vice versa. Enjoy cross-functional collaboration, streamlined processes, and a cohesive view of your tickets across platforms.

### Requirements to build your integration: <a href="#requirements-to-build-your-integration" id="requirements-to-build-your-integration"></a>

* A Jira instance with a dedicated user, and an API token for that user.
* A ServiceNow instance with a dedicated user. For testing purposes, you can create a developer instance here:[<img src="https://developer.servicenow.com/favicon.ico" alt="" data-size="line">ServiceNow Developers](https://developer.servicenow.com/dev.do)

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FxPB2B3r5PhVg3ItlD8qS%2FJira%20Snow%20developer%20instance.png?alt=media&#x26;token=0481d2b1-54b9-4a0f-bc1c-bf00df3bbe64" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
For a detailed guide on how to create a ServiceNow user, please visit the following link: [How to create a ServiceNow user.](https://docs.getint.io/guides/integration-synchronization/jira-servicenow-integration/creating-a-servicenow-user-for-getint-integration)
{% endhint %}

* For Jira **Cloud customers,** download the corresponding app from the Atlassian Marketplace, and launch it. Please note that we support both Jira Software and Jira Service Management.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FtlJcuf7AEnbuDyYe8lEE%2FJira%20Snow%20developer%20instance.png?alt=media&#x26;token=830c6e40-d4b9-4b90-9fd8-d2dfa80ec403" alt=""><figcaption></figcaption></figure>

* For Jira **Data Center,** please click your profile icon at the top right corner of your Jira instance, click **Atlassian Marketplace,** and use the option **Find new apps** to search for our **Jira ServiceNow integration app by Getint** (similar to the apps found below).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FSgpVKMXdpz03ISXtpRVX%2FDownloading%20the%20Snow%20app%20from%20the%20Atlassian%20marketplace.png?alt=media&#x26;token=7d911c5d-052e-4840-a84e-39833d1d2457" alt=""><figcaption></figcaption></figure>

### Setting up your ServiceNow integration <a href="#setting-up-your-servicenow-integration" id="setting-up-your-servicenow-integration"></a>

#### **1. Accessing Getint:**

* Launch the app, and click **Create integration** or **Migration.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F883r3IPFXuCiKBuWdWOG%2FBuilding%20an%20integration.png?alt=media&#x26;token=67ab614f-ef65-4fe7-bd44-d0b474e048ee" alt=""><figcaption></figcaption></figure>

#### **2. Token generation for Jira Cloud:**

* For **Jira Cloud,** generate a Jira token. This token will act as your password.
* Go to **Atlassian Account Settings.**
* Navigate to **Security** and generate an API token, then use this token as the password for Jira integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FP69SIlFBn8plq08HvUIW%2FCreating%20API%20token.png?alt=media&#x26;token=1e792058-668b-420d-aa08-c63d1b730aef" alt=""><figcaption></figcaption></figure>

#### **3. Establishing a Connection with Jira:**

* Ensure you’re logged in as a user with admin rights, click on **Connect App,** and select Jira. Choose **Create New** to set up a fresh connection with your Jira instance and input the URL of your Jira instance.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FV9C3x2mgvJYSJiArz0np%2FCreating%20a%20connection.png?alt=media&#x26;token=e4b6d266-b59f-4e97-9c88-1b4049ab0026" alt=""><figcaption></figcaption></figure>

* After establishing the connection, select the **Jira project** you want to connect to from the dropdown menu.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F4moYvRxpyVvijr8xDp3u%2FName%20your%20connection.png?alt=media&#x26;token=9da2f3c5-3ed5-40b6-b050-3fee414dc9af" alt=""><figcaption></figcaption></figure>

#### **4. Establishing a Connection with ServiceNow:**

* Connect to **ServiceNow.** If no connection is established yet, create a new one.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FzY9rsJh8WpaMBnK6ZOin%2FEstablishing%20connection%20with%20Snow.png?alt=media&#x26;token=6dadcf71-048e-45e0-9ccc-a43320c2287b" alt=""><figcaption><p>You can find your credentials within the settings in your <strong>ServiceNow</strong> instance.</p></figcaption></figure>

{% hint style="info" %}
It is crucial to grant specific access permissions to your ServiceNow user; otherwise, the connection will fail. You can find the full list of required permissions [here.](https://docs.getint.io/guides/integration-synchronization/jira-servicenow-integration/creating-a-servicenow-user-for-getint-integration)
{% endhint %}

#### **5. Type mapping:**

* **Quick Build (Beta):** You can use the Quick Build feature to automatically map fields and types between your apps. It’s a convenient way to make the process easier.
* **Manual Mapping:** If you prefer more control, you can manually map the types yourself. This allows you to customize the mapping based on your specific requirements.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FI2NhvHzOZUnXtt1ta4mW%2FUsing%20Quick%20build.png?alt=media&#x26;token=ffb84f96-aca7-4d2d-873a-15edc5a0f610" alt=""><figcaption></figcaption></figure>

* **Mapping ServiceNow Projects:** Projects in ServiceNow are part of the [Strategic Portfolio Management](https://www.servicenow.com/docs/bundle/vancouver-it-business-management/page/product/project-management/concept/c_ProjectApplicationOverview.html) (SPM) module. This module must be installed so that project mappings appear as an option in the dropdown list when pairing your type mappings. You can find more information about this module [here.](https://www.servicenow.com/docs/bundle/vancouver-it-business-management/page/product/project-management/concept/c_ProjectApplicationOverview.html)

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FN6By0OLuQUQbNpfvlM4b%2FProject%20type%20mapping%20for%20ServiceNow.png?alt=media&#x26;token=312fc436-e213-4662-9d6c-05911f8322c0" alt=""><figcaption><p>Project mapping in Jira ServiceNow integration</p></figcaption></figure>

* After enabling this module, you can start syncing ServiceNow projects from your **Project workspace.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FLsL177WgZnvAm9Y6ocsH%2FServiceNow%20project%20workspace.png?alt=media&#x26;token=24c343f0-1b7f-4e47-b81f-28f4999531e9" alt=""><figcaption></figcaption></figure>

* These will sync just like any other ServiceNow table, such as incidents, change requests, and more. Consequently, any new project from ServiceNow can be seamlessly transferred as a new task in Jira.

#### **6. Field mapping:**

* Review or manually map which fields to integrate and sync within the mapped types, including title, description, assignees, custom fields, and more.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FqvGhGmzPWxEE8KCoSWGP%2FField%20mappings.png?alt=media&#x26;token=d0b18993-80cd-491d-98e8-cfd5e4f3206a" alt=""><figcaption><p>Example of automatic field mappings with <strong>Quick Build</strong> where you can also add fields manually while using <strong>Quick Build.</strong></p></figcaption></figure>

#### **7. Assignees:**

* Map **Assignees** according to your user pairing requirements.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F1kJFuLpmBOUoGCNljb4Q%2FAssignees.png?alt=media&#x26;token=e8ba8667-648f-4168-8f0f-457b15cae87b" alt=""><figcaption><p><strong>Assignees</strong> in Jira (left). <strong>Assigned to</strong> in ServiceNow (right)</p></figcaption></figure>

#### **8. How to Manage Comments & Attachments:**

* Check the **Comments & Attachments** tab. These are activated by default, but you’re free to modify them depending on your organization’s needs.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F8BfwAoqxdtjJeCSfkqeI%2FComments%20%26%20attachments%20sync%20(1).png?alt=media&#x26;token=5cb295fc-7433-4d21-be30-ff4d8d478ec0" alt=""><figcaption></figcaption></figure>

* For ServiceNow integrations, there’s an option to further customize how comments are created under **Customize comments creation.** It can be incredibly helpful to make specific comments that either go Public or Private or **be skipped completely.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F2GRWwL02S0XDabziBvC8%2FServiceNow%20Comments%20and%20Attachments%20Customization%20(1).png?alt=media&#x26;token=5b333fcf-21ce-4539-85a9-21898e8b16ea" alt=""><figcaption></figcaption></figure>

* You can also choose the sync direction for attachments: **both ways,** **only to App A (left),** or **only to App B (right).** This feature adds an extra layer of customization to meet your organizational needs.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9oIFLum46yiunQjQBtfV%2FSynchronizing%20attachments.png?alt=media&#x26;token=7bf4d0d7-257f-4aeb-adbd-7b66ae057f51" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
You can disable comments and attachments entirely if they are not needed or are restricted in your organization.
{% endhint %}

#### **9. How to Map Statuses:**

* Map **Statuses.** Ensure you’re using the correct fields that represent the statuses for each app.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FxqdpiwpJxjUVQ9HEpW6L%2FMapping%20statuses.png?alt=media&#x26;token=d9421809-c87f-4b75-9a6f-06c6d1933da4" alt=""><figcaption></figcaption></figure>

#### **10. Finishing your Integration**

* Name your project and click **Create** at the top right corner to finish the integration setup.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FfHJYlwdle2DMjzmxKedU%2FFinishing%20your%20integration.png?alt=media&#x26;token=e0e87faa-90da-4587-ab46-53067bd170d7" alt=""><figcaption></figcaption></figure>

#### **11. UI Filtering**

* After finalizing your integration, you may also add filters to each app. Select the filter icon adjacent to the app icon within your integration. This action will affect the corresponding side of the integration.
* **Define Filter Rules**:
  * **ALL items filters**: Rules will be verified for every item before synchronization.
  * **NEW items filters**: Rules will be verified only for newly created items that have not yet been synced.
  * **SYNCED items filters**: Rules will be verified for items that were already synced in the past.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9bmB9mrXlZnRbBNIbBcL%2FItems%20filtering.png?alt=media&#x26;token=46a7aab0-09c3-49cc-923e-ee13c93112c1" alt=""><figcaption><p>For more information about this feature, please visit <a href="https://docs.getint.io/getintio-platform/workflows/items-filtering">Items Filtering.</a></p></figcaption></figure>

* You can also use custom queries to synchronize tickets only when the Assignment Group is set to a specific value. For example:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FkWUUNXiTeE7CB3GvDi8G%2FCustom%20query%20for%20SNOW%20groups.png?alt=media&#x26;token=b98c3036-6aa9-4d8f-8c58-bfc575359ee6" alt=""><figcaption><p>A custom query to sync ServiceNow tickets by the Assignment Group ID</p></figcaption></figure>

#### **12. Case Scenario for Items Filtering:**

* For example, If you want to integrate **Jira Project A** with ServiceNow Incidents that belong to **Assignment Group A,** use the filter items feature. In Getint, you can configure the connection by mapping the types and fields between ServiceNow and Jira, ensuring that fields like **Assignee** and **Assignment Group** are correctly synchronized.
* On a separate integration, you can set up (or duplicate the existing integration) to integrate **Jira Project B** with ServiceNow Incidents that belong to **Assignment Group B.** Here, different filtering will be needed. You can define filter rules in Getint to control which items are synchronized, specifying criteria such as status or priority to ensure only relevant items are synced. This helps manage data efficiently and avoids unnecessary clutter. Remember to save the integration once the filters are applied to ensure they are active.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FjeQHAfpEIT9mwpPlvjn4%2FFiltering%20items%20by%20assignment%20groups.png?alt=media&#x26;token=bc630a57-cec2-41ab-a420-eded3eea8e80" alt=""><figcaption><p>Filtering items by Assignment Group</p></figcaption></figure>

#### **13. Test your integration:**

* Ensure you aren’t experiencing any errors and that your integration is running smoothly. Create test scenarios to validate the functionality of your setup.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FQdZBNclmbe5HGkyHXVFv%2FServiceNow%20incident.png?alt=media&#x26;token=c380cfae-d5d9-4f76-a71f-ed14af519906" alt=""><figcaption><p>ServiceNow ticket created for testing purposes</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Ffdcp5Jssc6u3C18YbGpX%2FNew%20Jira%20ticket%20created%20from%20SNOW%20integration.png?alt=media&#x26;token=eb6dd91a-efa8-4ca8-9aba-57b32c6ea6a3" alt=""><figcaption><p>A new Jira ticket was created on the other end as a result of the integration</p></figcaption></figure>

### Conclusion <a href="#conclusion" id="conclusion"></a>

By following these steps, you can easily integrate Jira with ServiceNow, ensuring efficient synchronization of tasks, issues, and workflows across both platforms. This configuration promotes collaboration and streamlines project management processes. Please contact our [Support Team](https://getint.io/help-center) or [Schedule a Demo](https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team), if you require further assistance.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Creating a ServiceNow User for Getint Integration

In general scenarios, Admin access is not provided to a ServiceNow instance. The best practice/recommendation is to create a dedicated user (with several different access controls) to connect a ServiceNow instance to Getint and sync the data.

### How to Create a ServiceNow User <a href="#how-to-create-a-servicenow-user" id="how-to-create-a-servicenow-user"></a>

#### **1. User Creation:** <a href="#id-1.-user-creation" id="id-1.-user-creation"></a>

* Log in to ServiceNow, click **All** at the top left corner, and navigate to the **Users** (under User Administration) section.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FJNoYfNVWX1B0d7Tp7ZUt%2FServiceNow%20Developer%20Instance.png?alt=media&#x26;token=f7fc9f83-5998-432b-8861-32956f3f5d80" alt=""><figcaption></figcaption></figure>

* Click on **New** to create a new user, and enter all relevant user details.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FEkxDtQAojLSPVEHoVvO7%2FCreating%20a%20ServiceNow%20user.png?alt=media&#x26;token=45791963-98e7-49d4-83d6-40a7d0b9e3c9" alt=""><figcaption></figcaption></figure>

* Enter the User details, and click **Submit** to create the user.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FjCcgh8MUWUpVl9RfkOTD%2FName%20your%20user%20and%20submit%20it.png?alt=media&#x26;token=988370e5-e99e-432f-9cb6-f9e2458d3448" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Ensure that you untick **Password needs reset** when creating a new user. If you skip this step, the system will block the connection and display an error stating that you lack sufficient permissions. This message is misleading, as the issue isn’t related to permissions, but simply that the password is set to reset.
{% endhint %}

* After creating the user, you can now generate a password. Do so by clicking **Set Password** in the right corner of the screen. Save the password, and now you can use the full credentials to create a connection with Getint.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMx64Idxe8ExBvSOBoUjV%2FSetting%20up%20a%20password.png?alt=media&#x26;token=f6f7ab84-3679-4ef3-a630-9283129bcb79" alt=""><figcaption></figcaption></figure>

#### **2. Create a Role:** <a href="#id-2.-create-a-role" id="id-2.-create-a-role"></a>

* Navigate to **System Security** > **Users and Groups** > **Roles.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FHQCsYtcAEnnL47vyYI7s%2F82779d882a8ec1955b1c3feb980817f8%20(1).png?alt=media&#x26;token=5ffbf046-56df-43f8-9721-95d55ab83110" alt=""><figcaption></figcaption></figure>

* Click on **New** and enter relevant details for the new role.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Ft9ekcUQFBgMmVmdB8Tt8%2F0a524ce617cface009af137cdc1f88c0%20(1).png?alt=media&#x26;token=799238dd-d212-45a1-b109-e2ac0a3b0f93" alt=""><figcaption></figcaption></figure>

* Click **Submit** to create the role.

#### **3. Elevate System Admin to Security Admin:** <a href="#id-3.-elevate-system-admin-to-security-admin" id="id-3.-elevate-system-admin-to-security-admin"></a>

* Click on your profile image and select **Elevate Role.** In the pop-up, choose **security\_admin** and click **Update.** This step elevates the **System Admin** to **Security Admin** and will allow you to modify the **ACL** settings.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FnpurKaVQ5j2cfS1sOdV3%2F3cbd2f8bd07344f83f0556c919121622%20(1).png?alt=media&#x26;token=5dbb5eb5-cfad-4c5a-a550-cd0d4088bc5a" alt=""><figcaption></figcaption></figure>

#### 4. Required ACLs for Getint Integration

As we are tailoring access for our users, some base ACLs are required so that the connection with the ServiceNow instance works properly, allowing users to create, edit, and read their fields.

Here is a list of the needed ACLs, as well as their respective purpose in this process:

* **Dictionary Entry \[sys\_dictionary]**\
  This is the ServiceNow Data Dictionary, which defines the structure and attributes of every field on every table.\
  The Getint user needs read access to this table to introspect the schema of the records being synchronized. By reading this table, Getint identifies a field's type (e.g., reference, string) and its properties (e.g., maximum length, required status). This information is crucial for accurately translating and mapping data types between ServiceNow and other software.
* **Field Class \[sys\_glide*****\_*****object]**\
  This table stores definitions for the fundamental data types (e.g., string, integer, reference) used by fields across the instance.

  The dedicated user requires read access to this table because it is closely related to sys\_dictionary. It provides the low-level, technical classification of the field types. This access helps Getint's logic correctly interpret and handle the data being pulled or pushed, ensuring that all synchronized fields adhere to their native ServiceNow data constraints.
* **Choice \[sys\_choice]**\
  This table contains all the predefined drop-down options (choices) for choice fields in the system, such as Incident State or Priority values.

  The Getint user must have read access to retrieve both the internal value (the numerical/system value) and the display label (the user-friendly name) for these choices. This is essential for the core integration function of status and value mapping, ensuring that a status correctly corresponds to the appropriate, valid choice value in ServiceNow.
* **Journal Entry \[sys\_journal\_field]**\
  This table is where Journal-type field entries are stored, specifically, records like Additional comments and Work notes from synchronized tickets.

  The dedicated user requires read and create/write access to this table to manage bi-directional communication. This access allows Getint to extract comments from a ServiceNow record to sync to the integrated software, and conversely, to write comments back into the correct ServiceNow journal field, maintaining a full communication history.

#### 5. Granting User Access: Create Permission Records in ServiceNow

* Go to **System Security** > **Access Control (ACL).** Now, in the **ACL**, create **six new records** as follows:

**Record 1:**

* Click **New** to create a new record.
* Select **Read** from the **Operation** dropdown.
* In the **Name** field, select **Dictionary Entry \[sys\_dictionary]** in the first dropdown and **\*** in the second dropdown.
* Provide a **Description.**
* In the **Requires Role** section, add the role created in **Step 2** above.
* Click **Submit** at the top right corner, and **Continue** to create the new ACL record.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FSr1If8WIDWKiapmX7tOE%2Fa2ce5cb001b4863e64efcaf97a15ca92%20(1).png?alt=media&#x26;token=e4ab8ba7-20ec-49be-8f10-10968d7ab2d6" alt=""><figcaption></figcaption></figure>

**Record 2:**

* Repeat the steps as **Record 1,** but this time select **None** in the second dropdown instead of the **\* (asterisk).**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FVpXOCtJdpY2sTvo2CtL2%2F3ec142a61b16bda4734f6bf41b378436%20(1).png?alt=media&#x26;token=1a0e6b27-f0ba-47bd-a4e6-f4fb7fffafeb" alt=""><figcaption></figcaption></figure>

**Record 3:**

* Repeat the previous steps, but in the **Name** field, choose **Field class \[sys\_glide*****\_*****object]** in the first dropdown and **\*** in the second dropdown.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FiDR8pcyfYMhxVayudaeC%2Fb833a4169923482038ca2173f14065d0%20(1).png?alt=media&#x26;token=30ac4e3b-d617-4a78-bfc6-da1f23199474" alt=""><figcaption></figcaption></figure>

**Record 4:**

* Repeat the previous steps, but in the **Name** field, choose **Choice \[sys\_choice]** in the first dropdown and **\*** in the second dropdown.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fxa5dXkCd7W4o9sRDY8mm%2F0265b1df0503d18b78dcb86ef65ff561%20(1).png?alt=media&#x26;token=20787949-f5e3-4486-bbc6-386480155dec" alt=""><figcaption></figcaption></figure>

**Record 5:**

* Repeat the previous steps, but in the **Name** field, choose **Field class \[sys\_glide*****\_*****object]** in the first dropdown and **None** in the second dropdown.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fw68TScwvjkjicPiYAgRJ%2F433d73b97a2b9a532f77673f4de2e335%20(1).png?alt=media&#x26;token=6fecc870-c555-49fd-9fa2-4012f370e604" alt=""><figcaption></figcaption></figure>

**Record 6:**

* Repeat the previous steps, but in the **Name** field, choose **Journal Entry \[sys\_journal\_field]** and **None** in the second dropdown.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FECqA6YFJYTFYniI2CXE9%2F4ae64ae1bdc9f5e58d85347ba492d6ce.png?alt=media&#x26;token=c37f5e74-2c8b-448a-a471-042873133ce5" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Do not forget to add the **getint role** in the **Requires role** section for all six records.
{% endhint %}

#### **6. Configure User Permissions:** <a href="#id-4.-configure-user-permissions" id="id-4.-configure-user-permissions"></a>

* Go to **Users Administration** > **Users.**
* Search for the user created in **Step 1.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FFYEkZJrtoJf3EINUMeCj%2F13732d07421f4c47cacf87f6d6b928b9%20(1).png?alt=media&#x26;token=d4511f78-c821-445e-ac12-a101576bf72c" alt=""><figcaption></figcaption></figure>

* Click on the user ID and navigate to the **Entitled Custom Tables** section.
* In the **Roles** tab, click **Edit.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F2kfgUBj3uVbODjOqbYPF%2Ff92234b9c098f8319e4fe4c2030bdfa1%20(1).png?alt=media&#x26;token=d92b7e43-7e17-4d08-b0e6-788145becd08" alt=""><figcaption></figcaption></figure>

* In the **Collections** section:
  * Search for **itil** and move it to the **Roles list.**
  * Also, search for the role created in **Step 2** and add it to the **Roles list.**
* Click **Save** and then **Update** to finalize the changes for the user.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FzF8hXfkotOln5fSXChs5%2Fcc28d7fb4a0878eb6d68c2058dae5007%20(1).png?alt=media&#x26;token=7a055e10-f9a2-46fa-8972-9fcd5fe955d4" alt=""><figcaption></figcaption></figure>

With these steps, all permissions are now configured for this ServiceNow user, allowing to establish a connection between Getint and ServiceNow.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# ServiceNow OAuth Authentication

To set up OAuth authentication, begin by creating credentials in the Application Registry. Once set up, these credentials allow you to connect a ServiceNow instance to Getint, enabling seamless data synchronization.

### Creating Application Registry for OAuth Authentication <a href="#creating-application-registry-for-oauth-athentication" id="creating-application-registry-for-oauth-athentication"></a>

#### 1. Find Application Registry in All tab

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FmxNbrvZHnObLcGNajXs4%2FCreator%20studio%20main%20screen.png?alt=media&#x26;token=79f28c1d-9acf-4608-90e4-f0851b74e8a2" alt=""><figcaption></figcaption></figure>

#### 2. Create a New Application Registry <a href="#id-2.-create-new-application-registry" id="id-2.-create-new-application-registry"></a>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FCYl42wUpdSXMGqaQnADJ%2FCreate%20a%20new%20application%20registry.png?alt=media&#x26;token=2b1107c9-613a-40bd-a207-1bb8bc8a5da0" alt=""><figcaption></figcaption></figure>

#### 3. Click Create an OAuth API endpoint for external clients <a href="#id-3.-click-create-an-oauth-api-endpoint-for-external-clients" id="id-3.-click-create-an-oauth-api-endpoint-for-external-clients"></a>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FVM9cQQe99UExoJnQa6aO%2FAPI%20endpoint.png?alt=media&#x26;token=bbc289ed-337a-4de8-9a8b-29790a382341" alt=""><figcaption></figcaption></figure>

#### 4. Fill in the Name input and Submit <a href="#id-4.-fill-the-name-input-and-submit" id="id-4.-fill-the-name-input-and-submit"></a>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FIcn8QYvfP3thqEkAUHt7%2Ffilling%20in%20name%20input.png?alt=media&#x26;token=2cc8c551-47d1-4cec-af83-4811df6e9422" alt=""><figcaption></figcaption></figure>

#### 5. Enter the newly created Application Registry <a href="#id-5.-enter-newly-created-application-registry" id="id-5.-enter-newly-created-application-registry"></a>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FQjmbND50aVZe2Gpn4lZq%2FEnter%20application%20registry.png?alt=media&#x26;token=6207fffc-7632-45a6-ab19-86b009ad1f77" alt=""><figcaption></figcaption></figure>

#### 6. Click the padlock to show the Client Secret <a href="#id-6.-click-padlock-to-show-client-secret" id="id-6.-click-padlock-to-show-client-secret"></a>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F98GJmJcfWGon4IeQsp4e%2FClient%20secret.png?alt=media&#x26;token=5d2cc427-edf4-496e-ab48-4e66dd951300" alt=""><figcaption><p>Generated client ID and client secret can be now used during connection setup in Getint.</p></figcaption></figure>

### **Generating Access & Refresh tokens manually via POSTMAN** <a href="#generating-access-and-refresh-tokens-manually-via-postman" id="generating-access-and-refresh-tokens-manually-via-postman"></a>

#### 1. Create POST request: <a href="#id-1.-create-post-request" id="id-1.-create-post-request"></a>

* Set **URL** to https\://**instance**.service-now\.co&#x6D;**/oauth\_token.do**
* Select **x-www-form-urlencoded** in the **Body** tab and add the following properties:
  * **client\_id** - client\_id from Application Registry
  * **client\_secret** - client\_secret from Application Registry
  * **username** - ServiceNow User name
  * **password** - ServiceNow User password
  * **grant\_type** - must be named **password**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FaIYyxIaP17ONvu7nBWwX%2FPostman%20configuration.png?alt=media&#x26;token=08dbd0b2-9b03-415d-81ef-6c5faca80d08" alt=""><figcaption></figcaption></figure>

#### 2. You will get the following response <a href="#id-2.-you-will-get-the-following-response" id="id-2.-you-will-get-the-following-response"></a>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FrjzeLJXrAoLZyaLzpSmv%2FPostman%20response.png?alt=media&#x26;token=29cf7f45-d286-4fe9-b442-911644b3d62b" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
At Getint we take feedback seriously. Our company aims to bring solutions to many different use cases. Therefore, we highly advise you to contact our [Support Team](https://getint.io/help-center) or [Schedule a Demo](https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team), if you require further assistance.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Troubleshooting ServiceNow Access and Synchronization Issues

### Use Case

When integrating with ServiceNow, you may choose to restrict your dedicated user’s access to specific tables to enforce boundaries. However, overly strict limitations can lead to insufficient permissions, preventing Getint from retrieving data correctly and disrupting synchronization.

Out-of-the-box (OOB) modules installed via the Application Manager may require specific ACLs to be assigned to the dedicated user's role to access necessary tables and ensure proper syncing.

This guide walks you through how to grant the required permissions or troubleshoot common access issues that may appear during setup.

### Assign OOB Roles for Easier Setup

Base OOB roles can be assigned to your dedicated user to grant read, write, and create access to the **Incident**, **Problem**, and **Change** tables.

If you’re encountering access errors when syncing these work items and prefer not to assign the more extensive **ITIL** role, consider using OOB roles customized to your needs.

#### Understanding Roles in ServiceNow

Roles in ServiceNow can inherit other roles, which helps with permission management. You can view these associations by navigating to:

**System Security** > **Users and Groups** > **Roles**

Locate a specific role and click to see inherited roles in the **Contains Roles** tab.

Additionally, roles can include specific ACLs to grant change permissions and access to various tables.

### Role Access Breakdown

#### Incident

* **sn\_incident\_read** Grants read access to Incident records.
* **sn\_incident\_write** Enables creation and editing of Incident records.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FdG1osNSJGgfe9z1ZYINE%2FRole%20SN%20Incident%20Read.png?alt=media&#x26;token=a84984be-42cf-4664-959a-8f171fb99bc1" alt=""><figcaption><p>sn_incident_read role</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FQZCU26wpSPbA9Kv1H9xl%2FSN%20Incident%20Write%20ServiceNow.png?alt=media&#x26;token=84ca24d0-228d-4c60-ba51-431e0b2bd2ba" alt=""><figcaption><p>sn_incident_write role</p></figcaption></figure>

#### Change

* **sn\_change\_read** Provides read access to Change records.
* **sn\_change\_write** Allows creation and modification of Change records.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FsBI4499sccBcEdNtAwKE%2FSN%20Change%20Read%20ServiceNow.png?alt=media&#x26;token=34a8787d-2afc-42ee-a750-978e491fb182" alt=""><figcaption><p>sn_change_read role</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FLUZjENnCQdQKFuACqNEP%2FSN%20Change%20Write%20ServiceNOW.png?alt=media&#x26;token=5db1fec6-b93b-41e5-b4be-7f03391d0552" alt=""><figcaption><p>sn_change_write role</p></figcaption></figure>

#### Problem

* **sn\_problem\_read** Enables reading of Problem records.
* **sn\_problem\_write** Supports creating and editing of Problem records.

Each role displays inherited permissions in the **Contains Roles** tab at the bottom.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FbetaceNpEjkuGs2U49Ri%2FSN%20Problem%20Read.png?alt=media&#x26;token=4d4f5330-8b28-4679-a472-5d122fef81bf" alt=""><figcaption><p>sn_problem_read role</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FrvyOY6KaHnB3cORocivx%2FSN%20Problem%20Write%20ServiceNow.png?alt=media&#x26;token=7cc9bcc5-0c5f-4925-82a0-0e2f24d63452" alt=""><figcaption><p>sn_problem_write role</p></figcaption></figure>

### Removing Unwanted ACLs from OOB Roles

If you're concerned about assigning OOB roles that may include excessive permissions, you can query ACLs and trim them to fit your integration scope.

#### Steps to Query ACLs

1. In the **Application Navigator**, type `sys_security_acl_role_list.do` and press **Enter**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fdz3yRL7ADNHYZM0zmLNR%2FSys%20Security%20role.png?alt=media&#x26;token=7f54ddc2-07d5-46de-aba0-093065b37a87" alt=""><figcaption></figcaption></figure>

1. It will lead you to a page that lists all ACLs within your ServiceNow workspace. You can then filter the ACLs by role.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fj5n6epvskNOOYkvquMkr%2FACL%20Roles.png?alt=media&#x26;token=0ba3de90-c0cf-4319-b541-f637ab66ae5b" alt=""><figcaption></figcaption></figure>

1. Running the filter with conditions **ROLE - IS - \[yourRoleName]** will output all ACLs associated with the specified role. You can then customize all ACLs assigned to the specified role (you can also add tags to each ACL, so you can track their operation type, as you won’t be able to see it through this screen).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FdDFOK3q3uFWdoEeJZegh%2Fimage-20250705-000707.png?alt=media&#x26;token=3e04f673-d81c-4aac-8fbf-b24e1fc56946" alt=""><figcaption></figcaption></figure>

### Adding ACLs for Vendor and Scoped Applications

For integrations involving modules like **Customer Service Management (CSM)** or **Project Portfolio Management (PPM)**, dedicated users must have ACLs aligned with corresponding work item tables.

For example, syncing the **Project** work item from **PPM** requires read, write, and create ACLs for the **Project** table. Without these, syncing will fail even if mappings exist in Getint.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FjjfPFyL58siajBOlPKm5%2FProject%20portfolio%20management.png?alt=media&#x26;token=d43c6cf9-2944-41e9-b8c3-aae0d27f766a" alt=""><figcaption><p>View of the Project Portfolio Management, through the Application Manager.</p></figcaption></figure>

#### Example Error

```
{"message":"Insufficient rights to query records","detail":"Field(s) present in the query do not have permission to be read"}
```

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FZywdFyBv6yV5Q0jyYSkO%2FError%20with%20missing%20permissions.png?alt=media&#x26;token=6dc8cf7a-86b5-410d-b61a-bbce17d2f725" alt=""><figcaption><p>Dedicated user doesn’t have read ACL for the Project table.</p></figcaption></figure>

After installing a vendor application, you must create ACLs corresponding to the table and work item that you’d like to synchronize. Make sure to assign the ACLs to the dedicated user’s role:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMy7Xy85yOG2BK1a3CfEJ%2Fimage-20250705-032322.png?alt=media&#x26;token=e3d5464a-742f-4a55-8f1d-7fac0d0aa3c0" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
In this case, we installed Project Portfolio Management. Searching for **Project** in the name dropdown of the ACL creation screen fetches the right table for the work item Project that we are looking to sync.
{% endhint %}

After assigning the **Read** ACL for the Project table to the dedicated user's role, Getint successfully retrieved items from the Project table. However, because the **Create** ACL was still missing, the integration was unable to generate new Project work items in ServiceNow.

To ensure smooth data synchronization, confirm that the dedicated user's role includes all required ACLs. These typically include **Read**, **Write**, and **Create** permissions for the relevant tables.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FYIfYmAIU2SZovJxAamX6%2Fimage-20250705-032709%20(1).png?alt=media&#x26;token=f1f2d112-d864-40b8-9509-0842ce9ec220" alt=""><figcaption><p>Ensure to add Read, Write, and Create ACLs to the dedicated user’s role for the integration to run smoothly.</p></figcaption></figure>

#### Working with Scoped Applications

* Scoped applications like **CSM** operate in isolated environments. You cannot use the `.*` ACL operator unless you change the **global scope**. This ACL operator is required for Getint to synchronize data, and without the ACLs with this operator you might experience access issues.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FVt00ddfF9lwk6cYTNixr%2Fimage-20250705-033327.png?alt=media&#x26;token=34389ce2-63a3-4415-9fe1-4563c2206eab" alt=""><figcaption><p>.* ACL is missing from the dropdown, as we are not in the scope of the application.</p></figcaption></figure>

* To change your current scope, click the **Application Scope** icon, and then click on the first option:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FrGJVFfX7SpMHRcGa44VE%2Fimage-20250705-035437.png?alt=media&#x26;token=99e48636-1bb4-431e-b31f-9f6af8615e74" alt=""><figcaption></figcaption></figure>

* Filter the application by name, then click it. When the application is selected, your ServiceNow tab should refresh, and the global scope will change the one selected:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FfVBjPJWW6Ty5prfug599%2FCustomer%20Service%20Scope%20ServiceNOW.png?alt=media&#x26;token=3aafbac2-56d2-4bc8-8af6-eff3e272862f" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FykO0njJRSiQ0MjzJK6oq%2FApplication%20scope.png?alt=media&#x26;token=f2901c71-ec36-40d0-b2bf-b54ce340d014" alt=""><figcaption><p>You can confirm that you are within the scope of the application by hovering your mouse over the application scope icon.</p></figcaption></figure>

* You should now be able to create ACLs of the scoped application’s tables with the .\* operator:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FJfbY2e4hriotaQ5hMeJx%2Fimage-20250705-040522.png?alt=media&#x26;token=754c1004-f232-4283-bbda-10e30767f05a" alt=""><figcaption><p>The <strong>.*</strong> operator for ACL can now be selected, as we are within the application’s scope.</p></figcaption></figure>

### Debugging Field-Level ACLs

You can debug individual work item fields to uncover their ACLs, identify missing permissions, and assign only those needed for syncing. This lets you control which fields Getint can access while excluding any restricted data.

#### How to Debug Fields

1. Type **Debug Security** in the navigator,  and select **Debug Security Rules** under System Security.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FkCjMdoq0Vl1TBeXkLdLj%2Fimage-20250706-021722.png?alt=media&#x26;token=912813d1-f08d-482d-be04-287ce637f1c7" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Avoid impersonating before opening the Debug application. Doing so will prevent access, even if the user has the **script\_debugger** role. Instead, open the Debug application first and impersonate after the debug window is active.
{% endhint %}

1. The Debug application window will appear. Impersonate the user, minimize the window, and navigate to the work item you want to debug.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F6hHwDuUsmM3olEl6HmJl%2Fimage-20250706-022644.png?alt=media&#x26;token=29fea761-21cd-40b9-b6a0-948230c2f17b" alt=""><figcaption><p>Debug application window.</p></figcaption></figure>

1. When debugging is active, a small **Bug** <img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FNXvTrtIrW8H0TfXCR6d8%2Fimage.png?alt=media&#x26;token=fe642c8b-eba8-4cc7-b908-2416ce4de9e7" alt="" data-size="line"> icon appears beside fields governed by ACL rules. Clicking it reveals the applicable ACLs and their evaluation results.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FSw5le2sY72jCjAcJQxDO%2FDebug%20icon%20next%20to%20fields.png?alt=media&#x26;token=81415305-6f83-4f53-96fb-fd8342da26af" alt=""><figcaption></figcaption></figure>

1. The fields appear greyed out, indicating the dedicated user lacks Write permissions, even though they have access to the Incidents application and table.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FqNpp0d0fZJwzH9CfvLdr%2FFields%20with%20ACL%20rules.png?alt=media&#x26;token=a5c23f10-cd37-48ce-bfd6-a2792becd00b" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
A **True** result for a Read ACL means the dedicated user has a role with Read access to the field.

A **False** result for a Write ACL means the user lacks Write permission for the field.
{% endhint %}

1. Granting Write ACL for the Urgency field to the dedicated user’s role enables editing of that field.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F0CtDTLgmeq0KnoT9GLyH%2Fimage-20250706-024345.png?alt=media&#x26;token=02f4364a-d5e6-419f-8988-2b1f10a7d349" alt=""><figcaption><p>Write ACL for the Incident's Urgency field has been added to the <strong>getint_integration</strong> role assigned to the dedicated user.</p></figcaption></figure>

1. The field is no longer greyed out, and its values are now editable.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fq645bJxKDkcEBeXQqlrv%2Fimage-20250706-024528.png?alt=media&#x26;token=a26ae33a-73cc-4665-a8c8-ed1e2bbe3649" alt=""><figcaption><p>Getint can now sync the Urgency field, while leaving the data of other unwanted fields out of access.</p></figcaption></figure>

### Fields Not Visible Due to Business Rule <a href="#fields-not-visible-due-to-business-rule" id="fields-not-visible-due-to-business-rule"></a>

When reducing the access of the dedicated user, or when limiting its ACLs/roles, you may notice some fields missing from the work item:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FwqCw2UWXacQvfmHCYdD2%2FMissing%20fields%20in%20ServiceNow%20Incident.png?alt=media&#x26;token=633a0607-1804-441c-b3b8-c93f9eee19dc" alt=""><figcaption><p>Fields such as Assignee and Assignment Group are missing from the view.</p></figcaption></figure>

If the dedicated user doesn't have **ITIL** or **snc\_incident\_read** roles, trying to switch the view from Self-Service to Default to display those missing fields will always switch it back to Self-Service.\
\
This happens due to a Business Rule in place. You can add the dedicated user role to the list of roles allowed to switch the view to default with the following process:

* Type **Business Rules** in the application navigator, and select the option under **System Definition**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FlNWoI5MeJlTpL9tm8SfC%2FBusiness%20Rules.png?alt=media&#x26;token=d9a9c248-13f6-4df0-acad-1bff4aed6b3c" alt=""><figcaption></figcaption></figure>

* Type **incident** in the search bar, and click on the **Incident Functions** option:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fy8fGYHQ9d4zHWdoLixDq%2FLooking%20for%20incidents.png?alt=media&#x26;token=5ebba8d0-66f2-4105-831e-cf68626b2c29" alt=""><figcaption></figcaption></figure>

* Switch to the Advanced tab, and copy this text (from the first space until the penultimate parenthesis):

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FAXognwbe4AbXMqneGA3b%2FSwitch%20to%20the%20Advanced%20tab.png?alt=media&#x26;token=9d575dd4-6c07-4040-ba7d-850232b2eead" alt=""><figcaption></figcaption></figure>

* Paste the text right after the penultimate parenthesis, and change the "sn\_incident\_read“ role for the role you have created for your dedicated user (in my case, it’s getint\_integration):

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FeTM9dXDf4pRas84HJ8iQ%2FLook%20for%20the%20incident%20read%20role.png?alt=media&#x26;token=b61d7ee9-d348-4cb9-9e21-e790832b8ad5" alt=""><figcaption></figcaption></figure>

* Now the dedicated user should be able to switch views to Default, without it switching back to Self-Service, allowing you to visualize the fields from the work item properly while logged in through the dedicated user (or while impersonating it):

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FJpfpv5YicXRd19CPraYC%2Fdefault%20view%20for%20the%20dedicated%20user.png?alt=media&#x26;token=1cb5fcc7-34cf-4e85-864e-596be21ee6bc" alt=""><figcaption><p>Default View can now be selected, and the fields previously not visible are now displayed.</p></figcaption></figure>

### Summary

Use these steps to control what Getint can access and sync from ServiceNow.

* For a straightforward setup, assign OOB roles.
* To limit permissions, query ACLs, remove excess, and customize the role.
* Vendor applications like PPM or scoped apps like CSM require targeted ACLs. Make sure to switch scopes and add `. *` ACLs as needed.
* Debug field-level permissions to ensure the user can read and write the intended fields.

If you need any further help or if you are experiencing issues with your installation, feel free to open a support ticket at our [Support Portal.](https://getint.io/help-center)

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Creating a Custom Field in ServiceNow

Creating custom fields in ServiceNow enables better data organization and adapts the platform to meet specific business requirements. This opens a new way to map data fields across various platforms, ensuring seamless data flow and synchronization.

### How to Create Custom Fields in ServiceNow <a href="#how-to-create-custom-fields-in-servicenow" id="how-to-create-custom-fields-in-servicenow"></a>

Here’s a step-by-step guide to creating custom fields in ServiceNow:

#### 1. Select the Appropriate Table: <a href="#id-1.-select-the-appropriate-table" id="id-1.-select-the-appropriate-table"></a>

* Choose the table where the new custom field will be created. ServiceNow organizes its data in tables, such as Incidents, Change, or Task, and each table can have customized fields.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FDn7EBsvxjOn86pM8NqFC%2FServiceNow%20Incident%20Task.png?alt=media&#x26;token=47870e5c-3fb4-4704-9d0b-738abcb21c8e" alt=""><figcaption></figcaption></figure>

#### 2. Access the Form Layout to Create a Custom Field: <a href="#id-2.-access-the-form-layout-to-create-a-custom-field" id="id-2.-access-the-form-layout-to-create-a-custom-field"></a>

* Click the three horizontal bars (as shown below) and select **Configure > Form Layout**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FEAktKbQWMVNAiJ6fiCpc%2FConfiguring%20Form%20Layouts%20to%20Create%20Custom%20fields.png?alt=media&#x26;token=9d1bf23e-16c7-4e12-85bf-b515e5b4b9b4" alt=""><figcaption></figcaption></figure>

* In the **Create new field** section, provide the necessary details:
  * **Name**: Enter the name of the field.
  * **Type**: Select the field type.
  * **Field Length**: Specify the length of the field.
  * **View Name**: Choose the view for displaying the field (Default view is recommended).
  * **Section**: Determine which section the field will be displayed in.
  * Click **Add** to create the field.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FGCpCTHNPcjRvjGME0TTf%2FExample%20of%20a%20custom%20field%20being%20created.png?alt=media&#x26;token=93989af6-b782-4255-a165-ba10bccf298d" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
As of the publication date of this article, Getint supports the following field types: Date, Dropdown, Text, Reference, and URL.
{% endhint %}

#### 3. Place the Field <a href="#id-3.-place-the-field" id="id-3.-place-the-field"></a>

* Use the ServiceNow **slushbucket** (the term slushbucket refers to a user interface component used to transfer items between two lists) to place the new field in the desired position on the form.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FxNKOUeUQijEjcrhWJLvv%2FCreating%20a%20custom%20field.png?alt=media&#x26;token=786f3fad-cb58-42ee-9b07-ee40b980a232" alt=""><figcaption><p>Think of it as a method for sorting and organizing data within forms and catalog items</p></figcaption></figure>

* Click **Save** to finalize your changes.

#### 4. Test Your Custom Field <a href="#id-4.-test-your-custom-field" id="id-4.-test-your-custom-field"></a>

* Ensure the new field appears correctly on the form and functions as intended.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FrMzvXGnjiPB1j6otD3Fb%2FCustom%20field%20being%20created.png?alt=media&#x26;token=081fa150-dde5-45f5-8060-bdd7047f8586" alt=""><figcaption></figcaption></figure>

* It is important to also test the field in your ServiceNow integration to validate it is working as expected. The new field should be available from the dropdown list of field mapping.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FgTnqDgjEB5Rb4ze3HfbF%2FCustom%20field%20being%20recognized%20by%20Getint.png?alt=media&#x26;token=5878bc3d-f530-4cd7-a82d-fd64a50f8046" alt=""><figcaption><p>The newly created custom field appears when searching for ServiceNow fields</p></figcaption></figure>

When integrating ServiceNow with other tools using Getint, mapping custom fields is essential to maintain consistent data synchronization. Getint facilitates field mapping by allowing users to connect different platforms' fields, which may vary in naming conventions and types. If fields unique to ServiceNow (like Assignment Group) need to be mapped to other platforms, creating corresponding custom fields in those platforms can ensure a smooth integration experience.

These steps help customize the ServiceNow environment to fit specific use cases, enhance data management, and improve workflow automation. For more information about our tool or if need assistance with your integration, please contact our [Help Center](https://getint.io/help-center).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# How to Restrict "Incident" Data to Specific 3rd Party Companies

### Who is this tutorial for? <a href="#who-is-this-tutorial-for" id="who-is-this-tutorial-for"></a>

This tutorial is for users integrating multiple 3rd parties (e.g., multiple companies using Jira) with ServiceNow, and you want to ensure that each company only sees their relevant data.

### Use Case <a href="#use-case" id="use-case"></a>

The examples here are based on the **Incident** type in ServiceNow. However, you can apply the same logic to other types like Change Request, Requested Item, Incident Task, etc.

If your ServiceNow instance is integrated with multiple 3rd party companies using Jira, this setup ensures that each company only sees the data associated with their **Assignment Group** in the Getint integration.

{% hint style="info" %}
**Important**: When creating an Incident in ServiceNow, always specify the **Assignment Group** field.
{% endhint %}

### How does it work? <a href="#how-does-it-work" id="how-does-it-work"></a>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FjJjlquR4lhcfwyW2tQKd%2FJira%20ServiceNow%20integration%20main%20screen.png?alt=media&#x26;token=0b42e6da-0389-4f2b-a852-4212b2505a04" alt=""><figcaption><p>Example integration Incident ↔︎ Bug</p></figcaption></figure>

* **Incident 1** created in ServiceNow with **Assignment Group: company1** will result in Getint creating a Bug in **company1's Jira**.
* **Incident 2** created in ServiceNow with **Assignment Group: company2** will result in Getint creating a Bug in **company2's Jira**.
* **Incident 3** created in ServiceNow **without an Assignment Group** will not create any Bug in Jira, even if the integration is enabled.

When a **Bug is created in Jira** by company1 or company2:

* Getint automatically creates a corresponding Incident in ServiceNow with the appropriate **Assignment Group** matching the company (e.g., company1 or company2).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9bzsxpRaXDnpFA9Qc1Px%2FGetint%20White%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=bb914c97-78ab-4a91-89b4-2e42a5dc06a2" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

#### Quick Steps

* **Create an Assignment Group** in ServiceNow (e.g., **company1**).
* **Create a user** with the username **company1** and assign the roles: **getint**, **sn\_incident\_read**, **sn\_incident\_write**.
* **Add Business Rules** for incidents (and other relevant types) to restrict access (Insert, Update, Read) based on the Assignment Group and username.
* **Add Business Rules** to ensure that each company only uses its own Assignment Group.

#### Step 1: Create an Assignment Group in ServiceNow

To ensure that each company only has access to its own Incidents and data, first create an **Assignment Group** in ServiceNow.

* Go to **User Administration > Groups**.
* Create a new Assignment Group.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FBNvBP38gozNuUy9y71A6%2FCreating%20an%20Assignment%20Group.png?alt=media&#x26;token=309dbc77-6a28-4360-b5a8-5c8dfad32a1f" alt=""><figcaption><p>Create a new <strong>Assignment Group</strong></p></figcaption></figure>

* Name the group (e.g., **company1**).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FbppaBRxeiYzELMaw2iEZ%2FCreate%20the%20Assignment%20Group.png?alt=media&#x26;token=33814dcf-48ee-4cee-b834-e187d645e55f" alt=""><figcaption><p>Create an <strong>Assignment Group</strong> with name company1</p></figcaption></figure>

#### Step 2: Create a ServiceNow User for Each Company

For tutorial purposes, the **Assignment Group name** should match the **username** for the integration user. Of course, it is possible to use any assignment group but, in such case, scripts defined below will have to be adjusted.

* Go to **User Administration > Users** and create a new user (e.g., **company1**).
* Set the **User ID** to **company1**.
* Set the password for the user.
* Assign the roles: **getint**, **sn\_incident\_read**, **sn\_incident\_write**. If the **getint** role doesn’t exist, create it as described earlier.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FWBYjXaOpoa7l5xyHOi7Z%2FCreate%20a%20ServiceNow%20User.png?alt=media&#x26;token=33918100-bec0-460c-ada8-289fa5e74a5e" alt=""><figcaption><p>Create new user</p></figcaption></figure>

{% hint style="info" %}
**Important note:**

[In this tutorial,](https://docs.getint.io/guides/integration-synchronization/jira-servicenow-integration/creating-a-servicenow-user-for-getint-integration)we created the **getint\_integration** user (and it applies for most cases where you have a single ServiceNow and single Jira to integrate), but we need to create another user (for each company) and assign roles: **getint**, **sn\_incident\_read**, **sn\_incident\_write**)
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FUDwm3qmF7d13xf4T9bSp%2FUser%20records.png?alt=media&#x26;token=6c2e8c9a-8983-46cc-982b-945acf030c04" alt=""><figcaption><p>User ID is the most important (company1)</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FC3DqBTRr2bhBbYrgZpZE%2FAfter%20creating%20an%20user%2C%20edit%20the%20user%20password..png?alt=media&#x26;token=cb6366f9-847f-4c80-b835-a5a52a3b1973" alt=""><figcaption><p>After creating a user. Edit the user password.</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FGBl1SOnC7oDu9NUP0h02%2FGenerate%20the%20password..png?alt=media&#x26;token=2fba2ce9-da3b-425c-9180-35e05b783d0c" alt=""><figcaption><p>Generate and then copy the password</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F3CA6WaROlRHhhC61k463%2FUncheck%20and%20click%20Update.png?alt=media&#x26;token=0ed11200-77b3-483b-b650-d6607bbf5f38" alt=""><figcaption><p>Uncheck and click Update.</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FlKnQ7ZSxwNXDaotg3IFI%2FAssign%20roles%20to%20the%20user.png?alt=media&#x26;token=f4e8be9a-3d28-471a-aef1-32de8d38b183" alt=""><figcaption><p>Assign Roles to the user</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FhRrdhiTxlKGFFzhfFlH6%2FUser%20Role%20-%20Edit%20Users.png?alt=media&#x26;token=58d87015-b416-4f36-82b8-8a1678249548" alt=""><figcaption><p>Assign <strong>getint</strong>, <strong>sn_incident_read</strong>, <strong>sn_incident_write</strong>. If you don't see role <strong>getint</strong> then create it as described <a href="https://docs.getint.io/guides/integration-synchronization/jira-servicenow-integration/creating-a-servicenow-user-for-getint-integration"><strong>here</strong></a>.</p></figcaption></figure>

#### Step 3: Add a Business Rule to Restrict Access to Incidents by Assignment Group and Username

You need to create Business Rules to ensure that data visibility is restricted by **Assignment Group** and **username**.

**Requirements:**

* The Assignment Group (e.g., **company1**) is created.
* The user with the matching username (e.g., **company1**) and with the roles assigned: (**getint**, **sn\_incident\_read**, **sn\_incident\_write**

{% hint style="info" %}
**Important:** The username and Assignment Group must be identical (case-sensitive).
{% endhint %}

**Steps:**

* Go to **Administration > Business Rule**.
* And follow the steps shown in the pictures below:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FvmGz4DzaO1ZzZk67wzrm%2FAdding%20a%20business%20rule.png?alt=media&#x26;token=9d9b2705-9cbe-46c2-88b0-a2b68dd08e74" alt=""><figcaption><p>Create a new Business Rule</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FW8vbKCdp348ZaCxeE1xm%2FBusiness%20rule%20configuration.png?alt=media&#x26;token=e3764bdd-2fff-4f9a-abda-f7ff8644c356" alt=""><figcaption><p>Everything should be set as in the picture above</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fj5Q7g1TDXxrKgL9ZBO1e%2FAdding%20the%20business%20rule%20script.png?alt=media&#x26;token=f2970db5-6496-4197-8304-46fbdfeb98a9" alt=""><figcaption><p>Go to Advanced tab and paste script shown below.</p></figcaption></figure>

* Create a new Business Rule with the following script:

```
(function executeRule(current, previous) {
    var userName = gs.getUserName();  // Get the current user's username

 // Bypass restriction for admin users
    if (gs.hasRole('admin')) {
        gs.info("Admin user, bypassing group restriction.");
        return; // Allow admins to proceed
    }

    // Handle querying incidents where assignment group matches the username
    if (!current.isNewRecord()) {  // Only add this condition for non-insert actions
        current.addQuery('assignment_group.name', userName);  // Compare assignment group's name with the username
        gs.info("Querying incidents where assignment group matches username: " + userName);
    }

    // Handle inserts - set the assignment group based on the username
    if (current.isNewRecord()) {  // If this is an insert operation
        var userGr = new GlideRecord('sys_user_group');
        userGr.addQuery('name', userName);  // Find the group by username
        userGr.query();
        
        if (userGr.next()) {
            current.assignment_group = userGr.sys_id;  // Set the assignment group to the group found
            gs.info("Set assignment group to: " + userGr.name + " for user: " + userName);
        } else {
            gs.error("No matching assignment group found for username: " + userName);
        }
    }

    // Handle updates - restrict changes if assignment_group doesn't match the username
    if (!current.isNewRecord() && current.assignment_group.changes()) {  // If it's an update and assignment_group has changed
        var newAssignmentGroup = current.assignment_group.getDisplayValue().toLowerCase();
        
        // Check if the new assignment group matches the current user's group
        if (newAssignmentGroup !== userName.toLowerCase()) {
            gs.addErrorMessage("You cannot change the assignment group to one that does not match your username.");
            gs.error("Update blocked: Attempt to change assignment group to: " + newAssignmentGroup + " by user: " + userName);
            current.setAbortAction(true);  // Prevent the update from completing
        }
    }
})(current, previous);
```

This script ensures that users only see Incidents assigned to their group, and it sets the **Assignment Group** automatically for new records.

#### Step 4: (Optional) Add Business Rule to Hide Other Assignment Groups

This step is **optional** and only serves to hide other Assignment Groups, ensuring that 3rd parties will only see their own Assignment Group (which matches their username) in the integration configuration.

{% hint style="info" %}
**Important**: Even if a 3rd party company attempts to use an Assignment Group other than their own, Getint will ignore it and still enforce the use of the username as the Assignment Group.
{% endhint %}

**Purpose:**

This Business Rule ensures that each company only sees its own Assignment Group and hides others. This is useful for preventing 3rd parties from seeing Assignment Groups that do not belong to them.

**Steps:**

* Go to **Administration > Business Rule**.
* Create a new Business Rule following the steps shown in the images below.
* Set the fields as shown in the image.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FPYYRTHwbfXlR1p3mOOu3%2FChecking%20assignment%20groups%20in%20getint%20integration.png?alt=media&#x26;token=d4b3c746-fd0d-4d9c-a682-09b81701347b" alt=""><figcaption><p>You can also hide all groups and leave group created specifically for 3rd party (ex. “company1”)</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FBfhYaAZ5vonuTQwtRGLG%2FNew%20Business%20Rule.png?alt=media&#x26;token=7106406c-575f-4638-a4c2-e424ff30a088" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fkev7RLBvOumXpvZi6mWk%2FBusiness%20rule%20setup.png?alt=media&#x26;token=5c0cb54f-6e35-47d3-9f79-e6612cde6bc0" alt=""><figcaption><p>Everything should be set as in the picture above</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FPSWorAInvkxsnDeuWFEP%2FBusiness%20rule%20script%20for%20SNOW%20integration.png?alt=media&#x26;token=e2711d9f-dc48-4794-8c8d-633b9809be18" alt=""><figcaption><p>Go to Advanced tab and paste script shown below</p></figcaption></figure>

* Script: In the Advanced tab, paste the following script to restrict the visibility of Assignment Groups based on the current user's username:

```
(function executeRule(current, previous /*null when async*/) {
    // Get the current user's username
    var userName = gs.getUserName();
    // Bypass restriction for admin users
    if (gs.hasRole('admin')) {
        gs.info("Admin user, bypassing group restriction.");
        return; // Allow admins to proceed
    }
    // Get the group name of the current group being queried or interacted with
    var groupName = current.name.getDisplayValue();
    // Log values for debugging (optional)
    gs.info("User: " + userName + " | Group: " + groupName);
 // Restrict the query to return only groups where the group name matches the username
    current.addQuery('name', userName);
})(current, previous);
```

This rule ensures that only the group matching the username will be visible to each company during the integration process.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FPzdBwHnoDwTXtyDvQelC%2FChecking%20Assignment%20Group%20in%20Getint.png?alt=media&#x26;token=4e5fca5e-c59b-40e6-bc8c-d391dce38247" alt=""><figcaption><p>Example for user "allegro." Only one Assignment Group is visible because username is allegro.</p></figcaption></figure>

#### Step 5: Add Business Rule to Restrict Access to Comments from Incidents

**Steps:**

* Go to **Administration > Business Rule**.
* And follow steps shown on the pictures below:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FdQCHllEEQsIZ9nlYFf9q%2FAdd%20Business%20Rule%20to%20Restrict%20Access%20to%20Comments%20from%20Incidents.png?alt=media&#x26;token=3e53c704-bb07-4507-9600-b255bbedc7a0" alt=""><figcaption><p>Make sure to select sys_journal_field table</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FsXhZtQS9gMtXd2OOAEor%2FAdvance%20tab%20for%20the%20business%20rule.png?alt=media&#x26;token=298c7280-0d74-41c1-b0eb-c785e325345b" alt=""><figcaption><p>Go to Advanced tab and paste script shown below</p></figcaption></figure>

* Create a new Business Rule with the following script

```
(function executeRule(current, previous /*null when async*/) {
 var username = gs.getUserName();

    // Filter records where the 'name' field is 'incident'
    current.addQuery('sys_class_name', 'incident'); // Ensure we are working with incidents only

    // Create a new GlideRecord for incidents
    var gr = new GlideRecord('incident');
    gr.addQuery('sys_class_name', 'incident'); // Ensure we are filtering incidents
    gr.query();

    var incidentSysIds = [];
    while (gr.next()) {
        var assignmentGroupId = gr.getValue('assignment_group'); // Get the sys_id of the assignment group
        var groupRecord = new GlideRecord('sys_user_group');
        if (groupRecord.get(assignmentGroupId)) { // Fetch group record
            var groupName = groupRecord.getValue('name'); // Get the group name
            if (groupName === username) {
                incidentSysIds.push(gr.getValue('sys_id')); // Add the incident's sys_id if it matches
            }
        }
    }

    // Now add the query to 'current' to return only the incidents with the collected sys_ids
    if (incidentSysIds.length > 0) {
        current.addQuery('element_id', 'IN', incidentSysIds); // Filter current to only include these sys_ids
    } else {
        current.addQuery('element_id', 'IN', ['-1']); // No matching incidents, return an empty set
    }

})(current, previous);
```

#### Step 6: Add Two Business Rules to Restrict Access to Attachments from Incidents

**Steps:**

* Go to **Administration > Business Rule**.
* And follow steps shown on the pictures below:

In the first step you will restrict access to the **sys\_attachment** table, and in the second step you will restrict access to the **sys\_attachment\_doc** table (which holds the data for each attachment).

* Restrict access to **sys\_attachment** table

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FiXYhQWQwe4m9xNTXwr9Y%2Fsys%20attachment%20table.png?alt=media&#x26;token=4e889fed-6872-4e45-92cc-732a9c5b5dba" alt=""><figcaption><p>Make sure to select sys_attachment table</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMuijH3N1aL5pdLw0UJpl%2FBusiness%20rule%20for%20step%206.png?alt=media&#x26;token=7acdb3b7-a7b8-47de-905b-75acb6ada7f2" alt=""><figcaption><p>Go to Advanced tab and paste script shown below:</p></figcaption></figure>

* Create a new Business Rule with the following script

```
(function executeRule(current, previous /*null when async*/) {
    var username = gs.getUserName();

    // Filter attachments that are linked to incidents
    current.addQuery('table_name', 'incident'); // Filter only attachments related to incidents

    // Create a new GlideRecord to query incidents
    var gr = new GlideRecord('incident');
    gr.addQuery('sys_class_name', 'incident'); // Ensure we are filtering incidents
    gr.query();

    var incidentSysIds = [];
    while (gr.next()) {
        var assignmentGroupId = gr.getValue('assignment_group'); // Get the sys_id of the assignment group
        var groupRecord = new GlideRecord('sys_user_group');
        if (groupRecord.get(assignmentGroupId)) { // Fetch group record
            var groupName = groupRecord.getValue('name'); // Get the group name
            if (groupName === username) { // Compare assignment group with the username
                incidentSysIds.push(gr.getValue('sys_id')); // Add the incident's sys_id if it matches
            }
        }
    }

    // Now add the query to 'current' to return only the attachments linked to the incidents with the matching assignment group
    if (incidentSysIds.length > 0) {
        gs.error("Matching incident sys_ids: " + incidentSysIds.join(", "));
        current.addQuery('table_sys_id', 'IN', incidentSysIds); // Filter current to only include attachments linked to these incidents
    } else {
        gs.error("No matching incidents found for user: " + username);
        current.addQuery('table_sys_id', 'IN', ['-1']); // No matching incidents, return an empty set
    }

})(current, previous);
```

* Restrict access to **sys\_attachment\_doc** table

**Steps:**

* Go to **Administration > Business Rule**.
* And follow steps shown on the pictures below:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FNQttSMtRPn3411FO9gyH%2Fsys%20attachment%20doc.png?alt=media&#x26;token=68d7bc75-72e1-4a4a-ba4f-6c4a5facd0d8" alt=""><figcaption><p>Make sure to select sys_attachment_doc table</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fw1UOOXGMD2qocpUGKgBz%2FBusiness%20rule%20script%20for%20SNOW%20step%206.png?alt=media&#x26;token=e41fd0be-4efd-42ad-bfed-94daa0f270d4" alt=""><figcaption><p>Go to Advanced tab and paste script shown below:</p></figcaption></figure>

* Create a new Business Rule with the following script
*

```
(function executeRule(current, previous /*null when async*/) {
    var username = gs.getUserName();

    // Create a new GlideRecord for attachments related to incidents
    var attachmentGR = new GlideRecord('sys_attachment');
    attachmentGR.addQuery('table_name', 'incident'); // Filter for attachments related to incidents
    attachmentGR.query();

    var attachmentSysIds = [];
    while (attachmentGR.next()) {
        var incidentId = attachmentGR.getValue('table_sys_id'); // Get the sys_id of the related incident
        
        // Query the incident to get the assignment group
        var incidentGR = new GlideRecord('incident');
        if (incidentGR.get(incidentId)) {
            var assignmentGroupId = incidentGR.getValue('assignment_group'); // Get assignment group id
            var groupRecord = new GlideRecord('sys_user_group');
            if (groupRecord.get(assignmentGroupId)) { // Fetch group record
                var groupName = groupRecord.getValue('name'); // Get the group name
                if (groupName === username) {
                    attachmentSysIds.push(attachmentGR.getValue('sys_id')); // Add the attachment sys_id if it matches
                }
            }
        }
    }

    // Now add the query to 'current' to return only the documents linked to the attachments with the collected sys_ids
    if (attachmentSysIds.length > 0) {
        gs.error("Matching attachment sys_ids for user: " + username + " - " + attachmentSysIds.join(", "));
        current.addQuery('sys_attachment', 'IN', attachmentSysIds); // Filter current to only include attachment docs linked to these attachments
    } else {
        gs.error("No matching attachments found for user: " + username);
        current.addQuery('sys_attachment', 'IN', ['-1']); // No matching attachments, return an empty set
    }

})(current, previous);
```

### Summary

We have now restricted data access for each company to the Incidents associated with their Assignment Group. You can apply similar logic to other tables, such as Change Request, to restrict full access.

If you need any further help or if you are experiencing issues with your integration, feel free to open a support ticket at our [Support Portal.](https://getint.io/help-center)

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# How to Restrict Access to Specific Tables for Integration

### Use Case

If you want to restrict full access to specific tables in ServiceNow for certain companies during integration, you can do this by adding Business Rules. This allows you to specify which tables you don't want to provide access to.

For example, if you only want to integrate **Incidents** and not **Change Requests**, you can restrict access to the **ChangeRequest** table.

**Scenario:**

Integrating **ChangeRequest** (ServiceNow) ↔︎ **Story** (Jira)

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F89VjCIC2qnPTQ6ylF4UY%2FSample%20integration%20ChangeRequest%20(ServiceNow)%20%E2%86%94%EF%B8%8E%20Story%20(Jira).png?alt=media&#x26;token=795bdd75-187f-4992-938e-c29c50664614" alt=""><figcaption><p>Sample integration ChangeRequest (ServiceNow) ↔︎ Story (Jira)</p></figcaption></figure>

If you restrict access to the **ChangeRequest** table, attempting to create a Story in Jira will result in an error when trying to create a ChangeRequest in ServiceNow. This error will appear in the Getint integration logs.

### How to Deny Access to the ChangeRequest Table

* Go to **Administration > Business Rule**.
* Follow the steps shown in the images below to create a new Business Rule.
* Configure the fields as shown.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FgQUwb9bzErjDdpGYzXuM%2FCreating%20a%20new%20business%20rule.png?alt=media&#x26;token=98818c48-552c-4ca5-9755-f67eb6c12dc6" alt=""><figcaption><p>Create a new Business Rule</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F85nyiaXZWW6BfFi7xeBk%2FBusiness%20Rule%20configuration%20for%20SNOW%20getint%20integration.png?alt=media&#x26;token=f13134e0-8285-498a-9e9e-d34144ad28c6" alt=""><figcaption><p>Everything should be set as in the picture above</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fpq5zipQLXyYG4vy4JimR%2FRestrict%20Change%20Request.png?alt=media&#x26;token=b226bb33-5047-42e3-8e24-4a9dc3b4fc0e" alt=""><figcaption><p>Go to the Advanced tab and paste the script shown below</p></figcaption></figure>

* In the **Advanced** tab, paste the following script to block access to the **ChangeRequest** table:

```
(function executeRule(current, previous) {
 // Bypass restriction for admin users
    if (gs.hasRole('admin')) {
        return; // Allow admins to proceed
    }
    // Abort any operation on the change_request table
    current.setAbortAction(true); // Prevent any operation from completing
    // Apply a query that results in no records being returned
    current.addQuery('number', "00000000000"); // An invalid query to ensure no records are returned
})(current, previous);
```

This script will prevent any operation (Insert, Update, Query, or Delete) from happening on the **ChangeRequest** table by aborting the action and returning no records.

### How to Restrict Access to Other Tables

To restrict access to other tables, simply repeat the steps described above for the **ChangeRequest** table.

The only change required is to select a different table in the **Table** field. You can restrict access to various tables such as:

* **Requested Item**
* **Incident**
* **Incident Task**
* **Problem**
* Other tables like **sys\_dictionary** or **journal\_field\_type** which we may have allowed access to in previous ACLs.

### Summary

By following this approach, you can ensure that companies only access the tables necessary for their integration and block unwanted access to other tables.

If you need any further help or if you are experiencing issues with your installation, feel free to open a support ticket at our [Support Portal.](https://getint.io/help-center)

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# REST API requests list

Below, you can find a list of endpoints that <http://getint.io> will call during integration configuration and data synchronization.

### During integration configuration <a href="#during-integration-configuration" id="during-integration-configuration"></a>

[/api/now/table/sys\_db\_object?sysparm\_query=sys\_name%3DTask](https://dev57744.service-now.com/api/now/table/sys_db_object?sysparm_query=sys_name%3DTask) - finding task table details.

[/api/now/table/sys\_db\_object?sysparm\_query=super\_class%3De3f033c4c923101091f9f06464832716](https://dev57744.service-now.com/api/now/table/sys_db_object?sysparm_query=super_class%3De3f033c4c923101091f9f06464832716) - finding tables extending task.

[/now/table/sys\_db\_object/fa257b04c927101091f9f06464832798](https://dev57744.service-now.com/api/now/table/sys_db_object/fa257b04c927101091f9f06464832798) - table meta data.

[/now/table/sys\_db\_object/e3f033c4c923101091f9f06464832716](https://dev57744.service-now.com/api/now/table/sys_db_object/e3f033c4c923101091f9f06464832716) - table meta data.

[/api/now/v2/table/sys\_choice?name=task\&element=assignment\_group](https://dev57744.service-now.com/api/now/v2/table/sys_choice?name=task\&element=assignment_group) - fetching e.g. groups for assignment group field.

[/api/now/v2/table/sys\_user\_group?sysparm\_fields=sys\_id,name](https://dev57744.service-now.com/api/now/v2/table/sys_user_group?sysparm_fields=sys_id,name) - fetching user groups.

[/api/now/v2/table/sys\_user?sysparm\_fields=sys\_id,name](https://dev57744.service-now.com/api/now/v2/table/sys_user?sysparm_fields=sys_id,name) - fetching users who can be assigned.

[/api/now/v2/table/sys\_choice?name=incident\&element=state](https://dev57744.service-now.com/api/now/v2/table/sys_choice?name=incident\&element=state) - fetching options for state field.

[/api/now/table/sys\_dictionary?sysparm\_query=name=incident](https://dev57744.service-now.com/api/now/table/sys_dictionary?sysparm_query=name=incident) - fetching fields from incident table.

[/api/now/table/sys\_dictionary?sysparm\_query=name=task](https://dev57744.service-now.com/api/now/table/sys_dictionary?sysparm_query=name=task) - fetching fields for task table.

### During synchronization <a href="#during-synchronization" id="during-synchronization"></a>

[/api/now/v2/table/incident?sysparm\_fields=sys\_id,sys\_updated\_on\&sysparm\_limit=50\&sysparm\_offset=0\&sysparm\_query=%5Esys\_updated\_on%3E%3D2021-03-24+14%3A15%3A03null](https://dev57744.service-now.com/api/now/v2/table/incident?sysparm_fields=sys_id,sys_updated_on\&sysparm_limit=50\&sysparm_offset=0\&sysparm_query=%5Esys_updated_on%3E%3D2021-03-24+14%3A15%3A03null) - fetching incidents.

[/api/now/v2/table/incident](https://dev57744.service-now.com/api/now/v2/table/incident) - creating incidents.

[/api/now/v2/table/incident?sysparm\_query=sys\_id%3D680e615edb83a010a1db5385ca9619e3](https://dev57744.service-now.com/api/now/v2/table/incident?sysparm_query=sys_id%3D680e615edb83a010a1db5385ca9619e3) - fetching incident by sys id.

[/api/now/v2/table/incident/680e615edb83a010a1db5385ca9619e3](https://dev57744.service-now.com/api/now/v2/table/incident/680e615edb83a010a1db5385ca9619e3) - update incident fields, write comments.

[/api/now/v2/table/sys\_journal\_field?sysparm\_limit=100\&element\_id=680e615edb83a010a1db5385ca9619e3](https://dev57744.service-now.com/api/now/v2/table/sys_journal_field?sysparm_limit=100\&element_id=680e615edb83a010a1db5385ca9619e3) - fetching comments for incident.

[/api/now/attachment](https://dev57744.service-now.com/api/now/attachment) - fetching attachments by sys id.

[/api/now/attachment/upload](https://dev57744.service-now.com/api/now/attachment/upload) - upload attachments.

At Getint, we take feedback and customer inquiries seriously. Therefore, if you experience any errors while trying to integrate your app, or if you have any custom requirements, please raise a ticket at our support channel [here.](https://getint.io/help-center)

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FyO43KDfREuL9Vo6QaCZh%2F19.png?alt=media&#x26;token=32c85bb9-310a-4a64-9a0e-f0d7d5170924" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Jira Trello integration

Integrating Jira with Trello via Getint revolutionizes project management by combining detailed tracking with visual task management. This seamless integration works for Jira Cloud, Jira Data Center, Jira Software, and Jira Service Management. Our step-by-step guide will help you quickly set up the Jira-Trello connection, enhancing productivity and collaboration for your team. Transform your project management experience today.

### Step-by-Step Setup Guide <a href="#step-by-step-setup-guide" id="step-by-step-setup-guide"></a>

#### **0. Access the Getint App in Jira**

* Navigate to "Apps" and select "Integration for Jira - Trello."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fb8HeKpXorqEcVSc5s7LV%2Fimage-20240628-150153.png?alt=media&#x26;token=e638f224-2746-4069-80d7-eac35a62d415" alt=""><figcaption></figcaption></figure>

#### **1. Create Integration**

* Click "Create integration" for ongoing sync or "Migration" to transfer existing data: [Migration Guide.](https://docs.getint.io/guides/migration)

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FtBYpcOXKgHt6d5b558wJ%2Fimage-20240619-115231%20(2).png?alt=media&#x26;token=84eb0cf9-9909-455b-9e16-4bc331c0ea05" alt=""><figcaption></figcaption></figure>

#### **2. Token Generation (Password for Jira Cloud)**

* For Jira Cloud, generate a Jira token. This token will act as your password:
  * Go to Atlassian Account Settings.
  * Navigate to Security and generate an API token, then use this token as the password for Jira integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FtsxTENzoWRPEVY3WDjbt%2Fimage-20240628-150712.png?alt=media&#x26;token=41cdecd5-ac26-4971-abec-85a486f3ab51" alt=""><figcaption></figcaption></figure>

#### **3. Choose the Apps and Establish Connections**

* Ensure you are logged in as a user with admin rights, click "Select App" and choose Jira.
* Select "Create New" to establish a new connection with your Jira instance and add the URL of your Jira instance (omit the trailing "/").
* Enter the login credentials of the admin user.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FoB22bIX8YzzkEwTDtur7%2Fimage-20240620-165801%20(2).png?alt=media&#x26;token=fc8461e7-3b8c-4ed9-9ccb-7f87d4c73e8d" alt=""><figcaption></figcaption></figure>

#### **4. Select the Jira Project**

* Once the connection is established, choose the Jira project you want to connect to from the dropdown menu.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FQIUXlyHnEeL0LZuxnIFo%2Fimage-20240620-170315%20(3).png?alt=media&#x26;token=8db3c53d-de39-4687-b6fa-0dbcfef92612" alt=""><figcaption></figcaption></figure>

#### **5. Connect to Trello**

* Select the Trello app authorize the app and allow Getint to connect with your Trello board on the popup screen that will appear.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FZ8tsKzdLtb9box44SYto%2Fimage-20240628-151651.png?alt=media&#x26;token=f086d1ce-dd9d-41a3-978d-9ad10e2ae91f" alt=""><figcaption></figcaption></figure>

* Select "Add" to start the integration.
* Choose the board that you want to integrate.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FdGuzIupcLB7iiBiMhgpv%2Fimage-20240628-152006.png?alt=media&#x26;token=b0e24687-5b77-4ec7-a3aa-116d2b994972" alt=""><figcaption></figcaption></figure>

#### **6. Type Mapping**

* Map the Jira issue types you want to sync with Trello Cards, such as mapping a Trello card to a Jira task or a Jira bug.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FaKFs3HHIn2naqAPODVC0%2Fimage-20240628-200542.png?alt=media&#x26;token=a7e47a61-6d7c-4588-9104-8967af4c5bf2" alt=""><figcaption></figcaption></figure>

* Consider using the "Quick Build" beta feature for automated type and field mapping, which can facilitate the setup process.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FRrUFpyclvfntt3kAm1Oj%2FUntitled%20design%20(12)%20(2).jpg?alt=media&#x26;token=70f3f1ba-52e3-4570-a879-3edc1e42e6f6" alt=""><figcaption></figcaption></figure>

#### **7. Field Mapping**

* Review or manually map which fields to integrate and sync within supported mapped types.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F2EDKhoqr6HXJmwQtE27D%2Fimage-20240628-201703.png?alt=media&#x26;token=b70c7ed4-dfea-4923-8e19-80503a0ac9db" alt=""><figcaption></figcaption></figure>

#### **8. Comments**

* If needed, enable the integration and synchronization of comments.
* Filter the comments with the criteria that suit you. Make them private/public or use the preferred attributes such as created date or author.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F1iIB9YbnTX2bs8jS6czM%2Fimage-20240628-201754.png?alt=media&#x26;token=e77e4c77-0d9c-4417-b803-bf3db4ee85e5" alt=""><figcaption></figcaption></figure>

#### **9. Finalize Integration**

* Name your project and click "Create" to finalize the integration setup.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F56Y8FFSMAjHWydrHFPaH%2FUntitled%20design%20(13).jpg?alt=media&#x26;token=5b1b8ce1-4062-40f4-b9eb-780e00584e92" alt=""><figcaption></figcaption></figure>

#### **10. Filtering:**

It is possible to filter the synchronization to have them customized for your needs and requirements.

**UI Filtering Option:**

* Click on the filtering icon near the app icon in your integration. This will apply to that side of the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FwtcY0sfIs69CBal8dKQZ%2FScreenshot%20from%20June%2028%2C%202024%2C%205_21%20PM.png?alt=media&#x26;token=0e244782-f898-45d8-b22c-c6d287b0ea9d" alt=""><figcaption></figcaption></figure>

* Select if the filtering applies to All, New, and Synced items.
* Note that if the option “*New items”* is selected, the filtering will apply only to the new items, and the already synced items will continue to sync and update. If the option “*Synced items”* is selected, only the already synced items will be updated based on that filter.
* Choose the options and add the value for the filter. It is possible to filter more than one option for each field.
* Select Apply once you created the filters and “Save” the integration.

#### **11. Test the integration**

To ensure everything is working correctly, create tasks and go to the reporting section to verify that all syncs are functioning as expected. If you encounter any issues, don't hesitate to contact our support team for assistance.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FzsaMrqpYC0H8d39VdpaG%2Fimage-20240710-094940%20(1).png?alt=media&#x26;token=72049f3a-18a5-4c64-89f2-ac3c7603cae8" alt=""><figcaption></figcaption></figure>

### Conclusion

Following these steps, you can effectively integrate Jira with Trello, ensuring smooth synchronization of tasks, issues, and workflows between the two platforms. This setup enhances collaboration and project management processes.

For further assistance contact our support at <https://getint.io/help-center>.

# Jira Wrike integration

Managing tasks and projects across Jira and Wrike can be challenging without a unified system. Getint simplifies this process by enabling seamless two-way synchronization between the two platforms. This integration ensures that both teams stay aligned, whether you're handling development in Jira or managing tasks in Wrike. With features like field mapping, status synchronization, and customizable workflows, you can streamline collaboration, enhance efficiency, and tailor the integration to meet your unique business needs.

This guide will walk you through the setup process, ensuring a smooth and efficient integration experience.

### **Step-by-Step Setup Guide** <a href="#step-by-step-setup-guide" id="step-by-step-setup-guide"></a>

#### **1. Access the Getint App in Jira** <a href="#id-1.-access-the-getint-app-in-jira" id="id-1.-access-the-getint-app-in-jira"></a>

Navigate to **Apps** and select **Jira-Wrike Integration.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FdSHRWruRuz1G5Pbb1Ydn%2FJira%20Wrike%20Integration%20App.png?alt=media&#x26;token=b7bbeb91-a1e3-4688-866f-d84ef2b1e461" alt=""><figcaption></figcaption></figure>

#### **2. Create Integration** <a href="#id-2.-create-integration" id="id-2.-create-integration"></a>

Click **Create Integration** and choose between **Continuous Sync** or **Migration** based on your requirements.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F0LhTTdNgsUH4vh95s8Yy%2FContinuous%20Sync%20or%20Migration.png?alt=media&#x26;token=460f20d9-0c04-4034-ac65-2a4ef0c0623e" alt=""><figcaption></figcaption></figure>

#### **3. Generate a Jira API Token** <a href="#id-3.-generate-a-jira-api-token" id="id-3.-generate-a-jira-api-token"></a>

For Jira Cloud:

* Log in to your Atlassian account and navigate to **Account Settings > Security**.
* Generate an API token, which will act as your password for integration.
* Copy and securely store the token.

For detailed instructions, refer to guide [**Connection**](https://docs.getint.io/guides/quickstart/connection).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FhsPN7FHhoLb3eYAOKcuN%2FJira%20API%20Token.png?alt=media&#x26;token=e52d779d-c0ad-4149-8102-0988dfef1d9b" alt=""><figcaption></figcaption></figure>

#### **4. Generate a Wrike Permanent Access Token** <a href="#id-4.-generate-a-wrike-permanent-access-token" id="id-4.-generate-a-wrike-permanent-access-token"></a>

1. Log in to your Wrike account.
2. Verify your Wrike account if the API settings are unavailable.
3. Go to **Account Settings > Apps & Integrations > API Access**.
4. Generate an Access Token and securely store it.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FXYqCZltZXm0Ek8AKilAQ%2FWrike%20access%20token.png?alt=media&#x26;token=2295fb7d-b7f6-4bad-a74c-a60d01c6bd03" alt=""><figcaption></figcaption></figure>

For detailed instructions, refer to our [Connection](https://docs.getint.io/guides/quickstart/connection) guide.

#### **5. Connect to Jira and Wrike** <a href="#id-5.-connect-to-jira-and-wrike" id="id-5.-connect-to-jira-and-wrike"></a>

**Jira Connection:**

* Enter your Jira instance URL, username, and API token in Getint.
* Select the Jira project you want to synchronize.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FsiWQrwcbl76Kt8ctoMEu%2FJira%20Wrike%20Connection.png?alt=media&#x26;token=869e2a9a-629c-4d6f-8b81-9745a31376a2" alt=""><figcaption></figcaption></figure>

**Wrike Connection:**

* Use the Permanent Access Token to connect Wrike to Getint.
* Select the Wrike workspace and Folder you wish to sync with Jira.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F13QTj2iocFtrDk42dlWB%2FWrike%20connection.png?alt=media&#x26;token=6c5877fd-eb64-4dd2-a98d-bd7aa7eb7019" alt=""><figcaption></figcaption></figure>

* Click **Save** to establish the connection.

#### **6. Type Mapping** <a href="#id-6.-type-mapping" id="id-6.-type-mapping"></a>

Map the types of items you want to synchronize between Jira and Wrike.

* **Tasks ↔ Tasks**
* **Subtasks ↔ Subtasks**

Use the **Type Mapping** screen in Getint to configure the mappings according to your workflow needs.

Consider using the **Quick Build** beta feature for automated type and field mapping to streamline the setup process.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FVmoFoUONXEjvI3g9TrFE%2FJira%20Wrike%20type%20mapping.png?alt=media&#x26;token=149b16fb-8c38-4cce-9826-c8f5a35c17dc" alt=""><figcaption></figcaption></figure>

#### **7. Field Mapping** <a href="#id-7.-field-mapping" id="id-7.-field-mapping"></a>

* Select the fields to synchronize, such as **Title**, **Description**, **Assignees**, and **Custom** fields.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F4AUxgFbSRofGluLsCE2Z%2FField%20mapping%20Jira%20Wrike.png?alt=media&#x26;token=1c5642bf-232a-441c-87d7-100413761ae9" alt=""><figcaption></figcaption></figure>

* Use the arrows to define the synchronization direction:
  * **Unidirectional:** Sync changes from one platform to another.
  * **Bidirectional:** Sync updates in both directions.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FkwsEYv0GOxsOhOLRQnwH%2FSynchronization%20direction%20in%20a%20Jira%20Wrike%20integration.png?alt=media&#x26;token=3d1bc7cc-1c4d-46e4-9a4a-471c91c957cf" alt=""><figcaption></figcaption></figure>

* Click **Apply** to save your field mappings.

#### **8. Status Mapping** <a href="#id-8.-status-mapping" id="id-8.-status-mapping"></a>

1. Create tasks in Wrike for each status you wish to synchronize.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FpwTIhhYxmsVQNyB1fDiB%2FStatus%20mapping%20for%20a%20Jira%20Wrike%20integration.png?alt=media&#x26;token=d3449143-2eb5-4635-a28c-afecbb357b6f" alt=""><figcaption></figcaption></figure>

1. In Getint, go to the **Status Mapping** tab.
2. As Wrike does not provide the API, it is necessary to select **Add Option Manually** for its side.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FOD6aK47GE4JV1U8sJrDG%2Fadding%20option%20manually.png?alt=media&#x26;token=04477a34-2b83-4f9e-a70f-b70c1a45173f" alt=""><figcaption></figcaption></figure>

1. Copy the Wrike task status ID and paste it into Getint.
2. Assign a name to the status and map it to its Jira counterpart.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9kKzFb3jGRsJJek9c8jS%2FAssign%20a%20name%20to%20the%20status.png?alt=media&#x26;token=640a611a-d34a-4c21-9cf9-3f1bbdf9d3b5" alt=""><figcaption></figcaption></figure>

1. Repeat for all statuses and then **Apply**.

{% hint style="info" %}
**Tip:** Add and map statuses one at a time to avoid resetting the dropdown menu.
{% endhint %}

#### **9. Filtering Options** <a href="#id-9.-filtering-options" id="id-9.-filtering-options"></a>

Customize synchronization by applying filters:

1. Click the **Filtering** icon near the app icon in your integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FseqdR7Akcs0KVEMUNtv0%2FFiltering%20options%20for%20Jira%20Wrike%20integration.png?alt=media&#x26;token=513ab821-5359-4de0-bff5-644b7fddfb64" alt=""><figcaption></figcaption></figure>

1. Choose the filter scope:

* **All**: Apply the filter to all items.
* **New**: Apply the filter to newly created items only.
* **Synced**: Apply the filter to already synchronized items.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FjPxOQtpKi4TXS593mSKk%2FChoose%20the%20filter%20scope.png?alt=media&#x26;token=34c705f0-5572-479f-84b6-362a499c9be5" alt=""><figcaption></figcaption></figure>

1. Add values for the filters and click **Apply**.
2. Name and click on **Create** to save the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FINkVbHu7QZb1mx2toSYa%2FSaving%20your%20integration.png?alt=media&#x26;token=929240f5-b366-4902-b39c-17fc75960673" alt=""><figcaption></figcaption></figure>

For more details, refer to our [Filtering Guide](https://docs.getint.io/getintio-platform/workflows/items-filtering).

#### **10. Test the Integration** <a href="#id-10.-test-the-integration" id="id-10.-test-the-integration"></a>

1. Create test tasks in both Jira and Wrike.
2. Verify synchronization by adding comments, attachments, or updating task statuses.
3. Check logs in Getint to ensure proper synchronization.

{% embed url="<https://www.loom.com/share/a67d469bd38f40b79092430a53595a60?sid=f435dd99-b3d1-4ab5-b1ac-246aaa5fd709>" %}

### **Conclusion** <a href="#conclusion" id="conclusion"></a>

By following this guide, you can successfully integrate Jira and Wrike using Getint. This setup allows you to synchronize tasks, statuses, and workflows, fostering seamless collaboration between teams.

For further assistance, visit our [Help Center](https://getint.io/help-center) or schedule a demo to explore the full potential of Getint.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FmLeA5dSF46PtimhtWwRE%2FGetint%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=4a7609ca-78d2-4f00-acd0-74d4a58bacaf" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Jira Zendesk integration

In the ever-evolving world of project management and customer support, the integration between Jira and Zendesk facilitated by Getint is a true game-changer. This powerful connection bridges the gap between tracking project milestones and delivering exceptional customer service. By enabling a seamless flow of information between Jira and Zendesk, businesses can now manage projects and customer queries from a single, unified interface. This guide not only simplifies the setup process but also unlocks a world of efficiency and collaboration for teams of all sizes. Embrace the future of work with the Jira-Zendesk integration and revolutionize your project management experience.

**Optimize Your Team's Productivity with Getint 's Jira-Zendesk Integration**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F7QX86ZcIqIPnKN2syttO%2Fimage.png?alt=media&#x26;token=c9892a32-846c-4c36-9249-382ab42714de" alt=""><figcaption></figcaption></figure>

### **Access the** [**Getint**](http://getint.io/) **App in Jira:** <a href="#id-0.-access-the-getint-app-in-jira" id="id-0.-access-the-getint-app-in-jira"></a>

Navigate to Jira, go to "Apps," and select "Jira Zendesk integration"

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FDQZhsLc1XhhWHNIn4Z45%2Fimage.png?alt=media&#x26;token=567b072d-df61-43e6-afe9-a29e840a7a8c" alt=""><figcaption></figcaption></figure>

Choose between "Continuous Sync" or "Migration" based on your integration needs.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FwEh44mzYpKVSF4HCunjX%2Fimage.png?alt=media&#x26;token=79f92da2-4a75-448e-a898-1b6b6189879d" alt=""><figcaption></figcaption></figure>

#### **1. Token Generation for Jira Cloud:** <a href="#id-1.-token-generation-for-jira-cloud" id="id-1.-token-generation-for-jira-cloud"></a>

* Visit your Atlassian Account Settings and go to the Security section.
* Generate an API token in the API Token section. This token will authenticate your Jira Cloud.

{% embed url="<https://youtu.be/ERTZMVmWcCs>" %}

### **Establish a** **Connection with Jira:** <a href="#id-2.-establish-a-connection-with-jira" id="id-2.-establish-a-connection-with-jira"></a>

* Ensure you're logged in as a user with the correct permissions
* Click "Select App" and choose Jira.
* Select "Create New" to connect with your Jira instance.
* Name your connection, and add the URL of your Jira instance (without "/" at the end).
* Provide the login credentials.

#### **Choose the Jira Project:** <a href="#id-3.-choose-the-jira-project" id="id-3.-choose-the-jira-project"></a>

* With a successful connection, a dropdown menu will appear.
* Select the Jira project you want to integrate.&#x20;

{% embed url="<https://youtu.be/FiMSX3J4v2Q>" %}

### **Connect to Zendesk:** <a href="#id-4.-connect-to-zendesk" id="id-4.-connect-to-zendesk"></a>

* Access your Zendesk instance with Admin credentials. Select the four squares icon and choose ‘Admin Center’.
* Log in to Zendesk as an Admin. Select the four squares icon and go to ‘Admin Center' then navigate to ‘Apps and integrations’ -> 'Zendesk API'.
* Enable ‘Token Access’ and create an API token for the integration.

{% embed url="<https://youtu.be/Unnp9UrFCAw>" %}

#### **Configure** [**Getint**](http://getint.io/) **for Zendesk:**

* Open the Getint app and select "Zendesk" as the connection app.
* Enter your Zendesk instance URL and click "Next".
* Name the connection and provide your login credentials, using the token captured as the password.
* Choose an existing connection or create a new one.
* On the next page, select your organization and click "Connect".

{% embed url="<https://youtu.be/Aje-HxH4bEA>" %}

### &#x20;**Map Types:**

* Link Jira types (Task, Bug, Epic, Story) to synchronize in Zendesk.
* Specify the fields for integration or synchronization.

### &#x20;**Field Mapping:**

* Map key fields such as title/summary and description
* After configuring, name and save your integration settings.

{% embed url="<https://youtu.be/5GiMTj6khP4>" %}

Try the beta feature "auto-build" for automatic field mapping.

{% embed url="<https://youtu.be/w-xDO-IsMew>" %}

{% hint style="info" %}
Auto-build is currently in beta stage, if you have a feedback or have questions about it, please contact our support at <support@geint.io>
{% endhint %}

### **Filtering:** <a href="#id-8.-filtering" id="id-8.-filtering"></a>

It is possible to filter the synchronization to have them customized for your needs and requirements.

**UI Filtering Option:**

* Click on the filtering icon near the app icon in your integration. This will apply to that side of the integration.
* Select if the filtering applies to All, New, and Synced items.
* Note that if the option “*New items”* is selected, the filtering will apply only to the new items, and the already synced items will continue to sync and update. If the option “*Synced items”* is selected, only the already synced items will be updated based on that filter.
* Choose the options and add the value for the filter. It is possible to filter more than one option for each field.
* Select Apply once you created the filters and Save the integration.

{% embed url="<https://youtu.be/yhkjBnRR8x4>" %}

**JQL Filtering:**

* Select the app that will receive the filter.
* Under the field Custom JQL, it is possible to provide a JQL, which will be the filter for your sync and appended to the one generated when searching for issues in Jira (e.g., status in ('In Progress')).
* Save the integration.&#x20;

{% embed url="<https://youtu.be/jXKPNzunoPk>" %}

**Duplicate Setup and Select Different Projects:**

* Go to Workflows.
* Click the 3 dots on the right side and select "duplicate."
* A side panel will appear. Select a new name for the integration (by default, the integration will be called “copy of” if the same projects are established).
* On the dropdown menu, select the projects you would like to integrate.
* For each side, select Connect. Then Duplicate.
* Save the new integration.

{% embed url="<https://youtu.be/lHW9IbvrFtQ>" %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FiwAmwiuWcOM1s8joTmD9%2Fimage.png?alt=media&#x26;token=115af02b-d2a7-45fa-9590-2824b5b93fb7" alt=""><figcaption></figcaption></figure>

Leverage the Jira-Zendesk integration by Getint to optimize your project management and customer service processes. For further assistance or feedback, contact [getint.io/help-center](https://getint.io/help-center).

# How to Manually Provide Zendesk Organization ID and Name

When integrating with Zendesk, companies that do not own the Zendesk instance but have been provided credentials for an Agent user by the Zendesk instance owner may need to manually input the organization details during integration setup. This guide explains how to retrieve and provide the Zendesk organization ID and Name manually.

#### **Manually Providing Zendesk Organization Details** <a href="#manually-providing-zendesk-organization-details" id="manually-providing-zendesk-organization-details"></a>

1. In Getint, set up the Connection by following our [guide](https://docs.getint.io/guides/quickstart/connection#zendesk). On the integration setup screen, select the connection then click the **PROVIDE MANUALLY** button to access the organization details form.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FJBy33mJz4Gez3cLmq3Sn%2FEstablishing%20a%20connection%20with%20Zendesk.png?alt=media&#x26;token=cd63c59b-29f7-48d8-bc01-a868e464ffa6" alt=""><figcaption></figcaption></figure>

1. Enter the **Organization ID** and **Organization Name** fields with the details provided by the Zendesk instance owner then select **Connect**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FEm0Z498qYtMyFe0VZAft%2FConnection%20with%20Zendesk.png?alt=media&#x26;token=1a97b0aa-5c46-4b70-b2e9-812541429003" alt=""><figcaption></figcaption></figure>

1. Continue to set up the integration and **Save**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FUDpdxv44nODCJendyM94%2FCreating%20a%20ZD%20integration.png?alt=media&#x26;token=2f2e3c69-5b27-4d2e-9279-f9543029c1cc" alt=""><figcaption></figcaption></figure>

#### **How to Obtain Zendesk Organization ID and Name** <a href="#how-to-obtain-zendesk-organization-id-and-name" id="how-to-obtain-zendesk-organization-id-and-name"></a>

The Zendesk instance owner must retrieve the organization ID and Name and provide it to you. Here’s how they can locate this information:

1. **Log in to Zendesk as an Administrator**:
   * The instance owner must sign in with an administrator account.
2. **Access the Organization Information**:
   * Navigate to the following URL, replacing `<ZENDESK_INSTANCE_SUBDOMAIN>` with the Zendesk subdomain:

     `https://<ZENDESK_INSTANCE_SUBDOMAIN>.zendesk.com/api/v2/organizations.json`
3. **Find the Required Details in the API Response**:
   * The response will include a JSON object with the organization details.
   * Look for the `"id"` and `"name"` properties. For example:

     `{`\
     `"organizations": [`\
     `{`\
     `"url": "https://getintaugust.zendesk.com/api/v2/organizations/1900023220573.json",`\
     `"id": 1900023220573,`\
     `"name": "demogetint",`\
     `"shared_tickets": false,`\
     `"shared_comments": false,`\
     `"external_id": null,`\
     `"created_at": "2021-08-27T11:29:24Z",`\
     `"updated_at": "2021-08-27T11:29:24Z",`\
     `"domain_names": [],`\
     `"details": null,`\
     `"notes": null,`\
     `"group_id": null,`\
     `"tags": [],`\
     `"organization_fields": {}`\
     `}`\
     `],`\
     `"next_page": null,`\
     `"previous_page": null,`\
     `"count": 1`\
     `}`
4. **Extract the Details**:
   * **ID**: `1900023220573`
   * **Name**: `demogetint`

The instance owner should share these details with the company setting up the integration.

***

By following these steps, you can ensure the manual provision of Zendesk organization details is accurate, enabling a seamless integration setup.

If you encounter any issues or require further assistance, please contact our [Support Team](https://getint.io/help-center).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FXjjsbK8xBZHLL005BsbD%2FGetint%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=fb9ae7ba-3e7e-49b3-9e3d-b63377861f81" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Migration Guides

The Migration feature in Getint allows users to efficiently transfer data between applications, ensuring seamless transitions while maintaining data integrity. Whether you're switching from one platform to another or need to migrate specific items as part of a larger workflow, Getint provides a structured and flexible migration process.

In this guide, you'll learn how the migration feature works, how to test it during the trial period, and key considerations for a smooth data migration experience.

{% hint style="info" %}
Looking for step-by-step migration instructions? Choose a specific migration tutorial from the left menu.
{% endhint %}

### **How Migration Works in Getint**

#### **Key Features of the Getint Migration Tool** <a href="#key-features-of-the-getint-migration-tool" id="key-features-of-the-getint-migration-tool"></a>

* **Trial Limitations**: The migration feature has limitations during the trial period but can still be tested (details below).
* **Full Access on Request**: To unlock full migration capabilities, users must request access and purchase the feature.
* **Advanced Migration Options**:
  * **Time-Range Selection**: Migrate items created or updated within a specific period.
  * **Directional Migration**: Choose the source and target applications for migration.
  * **Handling Existing Items**: Select whether to:
    * **Skip** previously synchronized items.
    * **Recreate** existing items.
    * **Update** existing counterparts in the target app.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F5Dm9amrqvWUHJQQkiu3i%2FMigration%20options%20to%20select%20from.png?alt=media&#x26;token=636836b7-048f-42aa-abf0-ff610cc96ae9" alt=""><figcaption></figcaption></figure>

### **Migration Mode vs. Standard Integration** <a href="#migration-mode-vs.-standard-integration" id="migration-mode-vs.-standard-integration"></a>

* When the migration feature is enabled, the next integration run operates in **Migration Mode**, ensuring smooth data transfer.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FA14GLIuoI0XxUrA1CJxD%2FIdentifying%20the%20migration%20on%20the%20latest%20runs.png?alt=media&#x26;token=73e17abe-2997-42b8-bf58-72b2a39b808d" alt=""><figcaption></figcaption></figure>

* **Type Mapping and Field Mapping**: Migration follows the same type and field mapping configurations as a regular integration run.

#### **Optimized Performance and Reliability** <a href="#optimized-performance-and-reliability" id="optimized-performance-and-reliability"></a>

* Migration operations can be resource-intensive and time-consuming.
* To ensure a smooth experience, Getint runs migrations in a dedicated environment, keeping live integrations unaffected.

### **How to Test the Migration Feature During Trial** <a href="#how-to-test-the-migration-feature-during-trial" id="how-to-test-the-migration-feature-during-trial"></a>

During the trial period, **the migration feature is limited**, but testing is available under the following conditions:

* Users have access to 20 migration test runs.
* Each test run can migrate up to 5 items.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9izH9zqRZ2PlwWqavlGb%2FEnabling%20the%20migration%20feature.png?alt=media&#x26;token=162b669d-6024-438f-bc1c-bbd86df72b6b" alt=""><figcaption></figcaption></figure>

This allows businesses to evaluate migration functionality before purchasing full access.

{% hint style="info" %}
Need help testing migration? Visit our [Support Portal](https://getint.io/help-center) for assistance.
{% endhint %}

### **Why Getint Migration is Better Than Standard CSV Import/Export** <a href="#why-getint-migration-is-better-than-standard-csv-import-export" id="why-getint-migration-is-better-than-standard-csv-import-export"></a>

Unlike traditional CSV export-import methods, Getint offers a much more efficient, accurate, and automated migration process:

**✅ Real-Time Synchronization –** Unlike CSV imports, which require manual updates, Getint keeps your data continuously in sync.\
\&#xNAN;**✅ Preserves Issue History & Relationships –** Getint migrates full data structures, including attachments, comments, and custom fields. CSV imports often fail to retain relationships.\
\&#xNAN;**✅ Error Prevention & Smart Mapping –** Getint ensures precise field mapping and prevents data mismatches, reducing errors compared to manual CSV handling.\
\&#xNAN;**✅ No Manual Intervention Required –** CSV imports require manual exports, format corrections, and imports, while Getint automates the entire process seamlessly.\
\&#xNAN;**✅ Works with Complex Workflows –** Supports advanced migration rules, such as filtering, transformation, and incremental updates, which CSV lacks.

For an in-depth Jira migration process, refer to our [Master Jira Migration with Getint – Your Ultimate Guide](https://getintio.atlassian.net/wiki/spaces/Support/pages/854884356/Migration+Guides).

### **Pricing for the Migration Feature** <a href="#pricing-for-the-migration-feature" id="pricing-for-the-migration-feature"></a>

Getint’s migration pricing is based on the volume of issues, tasks, or incidents you need to migrate, ensuring flexibility and scalability for businesses of all sizes. Unlike our regular licensing model, migration pricing is not based on Jira users or an annual fee. Instead, it is structured as a 3-month migration license (with a sync license included), allowing enough time for thorough planning, execution, and validation of the migration process.

#### **Pricing Tiers** <a href="#pricing-tiers" id="pricing-tiers"></a>

* **Up to 2,000 issues/tasks/incidents** → **$1,500**
* **Up to 20,000 issues/tasks/incidents** → **$3,000**
* **Custom Pricing** → Contact our team for a tailored quote on migrations exceeding **20,000 items**, including large-scale migrations of up to **1 million tasks**.

View our [pricing page](https://www.getint.io/pricing) for more details or reach out to our [Support Team](https://getint.io/help-center) for assistance.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Migrating Data with Getint

Migrating data between project management tools is a critical step in ensuring seamless transitions during tool changes, company mergers, or acquisitions. Whether you are moving from Azure DevOps, ServiceNow, Asana, or Monday to Jira, or the other way around, consolidating multiple Jira instances, or onboarding Company B’s project data into Company A’s system, Getint’s Migration Feature ensures a smooth and structured transfer of historical issues, tasks, bugs, and more.

Unlike traditional CSV export/import, Getint’s migration offers granular control, automation, and real-time monitoring, eliminating manual errors and data inconsistencies.

### Migration Licensing <a href="#migration-licensing" id="migration-licensing"></a>

Migration is a **premium feature** and is **billed separately** from continuous integration. This ensures an advanced migration experience with **enhanced customization, support, and additional features**.

Before starting your migration, review our [**Migration Pricing Guide**](https://www.getint.io/pricing) for detailed licensing options. If you have any questions, reach out to our [Support.](https://getint.io/help-center)

### **Preparing Your Environment Before Migration** <a href="#preparing-your-environment-before-migration" id="preparing-your-environment-before-migration"></a>

To ensure a smooth migration, consider the following:

* Ensure Matching Fields Exist: If your source system includes fields that do not exist in the destination system, you must create them beforehand. This ensures that 1:1 field mapping can be applied where necessary.
* Handling Fields That Cannot Be Mapped: If some fields cannot be mapped directly, you can still migrate their values. Create a custom text field on the destination tool and map the original field to it, enabling the **Use label from the other side** option. This will transfer the field's value as plain text without requiring a matching field type.
* For advanced use cases, it is also possible to migrate values from multiple source fields into a single text field using a merging option or, if necessary, a custom script. This can be useful when a 1:1 mapping is not required or feasible. For more information on how to merge fields, follow our guide [here](https://docs.getint.io/guides/integration-synchronization/how-to-map-fields#concatenating-fields).

For more tips, refer to [Master Jira Migration with Getint - Your Ultimate Guide](https://www.getint.io/blog/mastering-jira-migration-a-comprehensive-guide-with-getint).

### Setting Up Your Migration <a href="#setting-up-your-migration" id="setting-up-your-migration"></a>

#### A. Connecting for the First Time and Migrating <a href="#id-1.-connecting-for-the-first-time-and-migrating" id="id-1.-connecting-for-the-first-time-and-migrating"></a>

#### **Create a Connection to Migrate**

1. Open the **Getint App** and select **Create an Integration**.
2. In the pop-up window, choose **Migration** as the integration type.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FL7X0l57FnovAV0TtdUs9%2FData%20migration%20with%20Getint.png?alt=media&#x26;token=29922ab6-dc33-4a67-b5ef-b5b43313c01d" alt=""><figcaption></figcaption></figure>

#### **Set Up the Integration**

1. Select the apps involved in the migration. We recommend checking our documentation to review how to create the integrations: [Integration Guides](https://docs.getint.io/getting-started-with-the-platform/starting-the-free-trial-and-accessing-the-getint-app/jira-access-and-user-management#jira-server-data-center-dc).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FNT9CJ09UqvoKRoYDWfbx%2FSelect%20the%20app%20for%20migration.png?alt=media&#x26;token=cd517892-6586-42e6-82b1-374668cdcce7" alt=""><figcaption></figcaption></figure>

1. Map issue types, according to your needs, between the two systems.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F98B5n6cAsIk7U80dGIgS%2FMap%20issues%20accordingly.png?alt=media&#x26;token=b22def04-3ec3-41b9-83f0-d651dcabb519" alt=""><figcaption></figcaption></figure>

1. Ensure that the fields are mapped correctly. Follow our guides for each app integration to ensure proper mapping.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FLiAZLweJSh1PgFFjBK4k%2FEnsure%20all%20fields%20are%20mapped%20properly.png?alt=media&#x26;token=892e2d4a-3427-4ccc-a5bc-76509462a29e" alt=""><figcaption></figcaption></figure>

1. Name the integration and save the configuration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FsaHUsbCehafDs7fFNVvp%2FName%20and%20save%20your%20integration.png?alt=media&#x26;token=f9cff86c-cc35-4e1f-a338-6659faff8b99" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
The migration will be created but disabled by default; its status will change once the settings are properly configured.
{% endhint %}

#### **Configure Migration Settings**

With the integration properly configured, it is now time to set up the migration. Go to the **Migrate Data tab** and click **Enable the Migration on the next run.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fauud2ke31GjiS3xup9Ht%2FMigration%20configuration%20with%20Getint.png?alt=media&#x26;token=86d7c983-a6d2-4338-9dd5-ebbfb0a78cd2" alt=""><figcaption></figcaption></figure>

1. **Select Migration Direction**: Define if the items from the app on the left will be migrated to the right or from the app on the right to the left.ft

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FcyK4Plcy5aNvcudQ6BiJ%2FSelect%20a%20side%20to%20move%20the%20items.png?alt=media&#x26;token=6327ce4c-742a-41eb-a759-73321a6c36a6" alt=""><figcaption></figcaption></figure>

1. **Decide on what to do with the items already migrated**: Define whether items will be **recreated, updated, or skipped** if they already exist in the target system.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fv8h5pe5ccXPVy3DOqSyg%2FDecide%20on%20what%20to%20do%20with%20items%20that%20were%20already%20migrated.png?alt=media&#x26;token=2d251855-ab68-4747-b7e5-1430f73b5423" alt=""><figcaption></figcaption></figure>

1. **Field Resynchronization (Optional)**: If you’ve **previously migrated data** and want to update specific fields (e.g., **Assignee, Status, Description**), specify them here. To resync all fields, enter **\_*****ALL*****\_** or leave the field blank.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FAQrUqiFslCRyFKzZs6ph%2Ffields%20that%20should%20be%20resynced.png?alt=media&#x26;token=7aa0f48b-d0c6-4b42-aece-780fe67f680f" alt=""><figcaption><p>To ensure the integration continues after migration, disable the option to interrupt it.</p></figcaption></figure>

1. **Selective Migration (Optional)**:

* Provide specific **item IDs** for migration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMdKdbBp8tIUG4OEfQaJi%2Fitems%20that%20should%20be%20migrated%20Asana.png?alt=media&#x26;token=b96755b0-b214-4c23-9065-1f3d73d4127d" alt=""><figcaption></figcaption></figure>

* Use **JQL filtering** for more refined data selection. JQL filters can be accessed by clicking the app logo in the integration. You can find more details on filtering in our guide: [Filtering Items for Integration in Getint](https://docs.getint.io/getintio-platform/workflows/filtering-items-for-integration-in-getint).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fh48S5GVEUEaYcrMvDYUC%2FJQL%20filtering.png?alt=media&#x26;token=4691ca4d-9c75-43c1-ad3e-53aa8384a8a3" alt=""><figcaption></figcaption></figure>

1. **Set a Time Range:** To filter which items should be migrated, select the creation date or the last updated date in UTC.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FbncxRpypbPb6LV2tbVWR%2FSet%20a%20time%20range.png?alt=media&#x26;token=63b95222-4746-4c37-bfa6-7aa6235b11e5" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Note that if the items were not updated or created within the selected time range, Getint will not migrate them.
{% endhint %}

1. **Start the Migration**: Click **Schedule Migration** to begin the process. Migration time depends on the volume of data.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FqAymezpjyYU0UPQby4jh%2FSchedule%20the%20migration.png?alt=media&#x26;token=15169e0a-a9dd-40bd-9144-a534b7e32636" alt=""><figcaption></figcaption></figure>

1. Getint will be in migration mode. Monitor progress in **sync logs** to ensure a smooth transfer.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMj8uTwaQ9vDeo8BcISgS%2Fmigration%20mode.png?alt=media&#x26;token=59519a8b-2fcc-4519-9118-2208a543edb4" alt=""><figcaption></figcaption></figure>

1. **Enable Continuous Sync (Optional)**

If you want **newly created issues** to continue syncing after migration:

Disable the option to stop the sync after the migration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FYIxPnwxCEd1mwPGWqmgF%2FDisable%20the%20option%20to%20stop%20the%20sync%20after%20the%20migration.png?alt=media&#x26;token=c757b393-be0b-4c49-860d-bcc27d64aa36" alt=""><figcaption></figcaption></figure>

Or change the settings after the Migration:

* Go to your integration, click **More >Settings> Enable**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FIFWdzHryiznGdMevQEe6%2FEnable%20the%20integration%20after%20the%20migration%20run.png?alt=media&#x26;token=1a351c8c-6900-41ef-8b5c-a578391a8e31" alt=""><figcaption></figcaption></figure>

By default, the integration is disabled after migration to **prevent unintended updates**.

#### B. Migrating on an Existing Integration <a href="#id-2.-migrating-on-an-existing-integration" id="id-2.-migrating-on-an-existing-integration"></a>

If you already have a **continuous sync in place** but need to **migrate older items**, follow these steps:

1. Open the **Getint App** and navigate to your **existing integration**.
2. Select **Migrate Data** from the left-hand menu.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FRAwxPkpql31LIXlUIdF2%2Fmigrate%20data%20on%20an%20existing%20integration.png?alt=media&#x26;token=bde7f12e-d881-4505-af03-119f6a5ba63e" alt=""><figcaption></figcaption></figure>

1. Configure the migration settings as described in the previous section.
2. **Enable migration** for the next sync run.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FGdarvEUk36LRBVgdPiel%2Fenable%20migration%20on%20the%20next%20sync%20run.png?alt=media&#x26;token=deb1af3c-b5fb-4346-a64d-7301a04dd1a6" alt=""><figcaption></figcaption></figure>

1. **Monitor progress** on the latest runs and logs.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMFVM2b9jUyyFtrNHlMYA%2Fmonitor%20progress.png?alt=media&#x26;token=b4e367c4-d2c5-4bce-9ec6-665c53b1a26f" alt=""><figcaption></figcaption></figure>

### Getint Migration vs. Traditional CSV Import <a href="#getint-migration-vs.-traditional-csv-import" id="getint-migration-vs.-traditional-csv-import"></a>

Many companies use CSV exports/imports for migration, but Getint’s Migration Feature provides several advantages:

#### **1. Advanced Field Mapping** <a href="#id-1.-advanced-field-mapping" id="id-1.-advanced-field-mapping"></a>

* Getint allows users to manually map issue types and fields, ensuring precise data transfer.
* Traditional CSV imports require rigid predefined templates, making data structuring complex.

#### **2. Granular Field Resynchronization** <a href="#id-2.-granular-field-resynchronization" id="id-2.-granular-field-resynchronization"></a>

* With Getint, specific fields can be resynced on demand, preventing unnecessary updates.
* CSV imports lack flexibility—you must re-import everything or risk data loss.

#### **3. Selective Data Migration** <a href="#id-3.-selective-data-migration" id="id-3.-selective-data-migration"></a>

* Getint lets you filter specific items by ID or JQL queries to migrate only what’s necessary.
* CSV methods require manual filtering and do not offer dynamic selection.

#### **4. Real-Time Monitoring & Automation** <a href="#id-4.-real-time-monitoring-and-automation" id="id-4.-real-time-monitoring-and-automation"></a>

* Getint provides live tracking of migration progress with sync logs.
* Traditional CSV methods lack real-time updates—errors may go unnoticed until post-import verification.

#### **5. Seamless Integration with Existing Workflows** <a href="#id-5.-seamless-integration-with-existing-workflows" id="id-5.-seamless-integration-with-existing-workflows"></a>

* Getint migration works alongside existing integrations, allowing continuous sync post-migration.
* CSV imports often overwrite or duplicate data, requiring additional cleanup.

By choosing Getint’s Migration Feature, your organization benefits from precision, automation, and full control over the migration process.

### Need Assistance? <a href="#need-assistance" id="need-assistance"></a>

For **additional support**, visit our [**Help Center**](https://getint.io/help-center).

**Considering migration?** [**Schedule a Demo**](https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team) with our team to explore how Getint can support your transition.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Getint Migration Guide – Best Practices & Preparation

When moving from Server or Data Center to **Jira Cloud** (or between tools with Getint integrations), planning is everything. From what we saw at NEXP and from our own experience with migrations, here's what our customers need to know and do.

{% hint style="warning" %}
Your migration license includes a 3-month sync license, giving you time to test the tool, understand how it works, and prepare your setup. There's no need to migrate data immediately. Use this period to validate your configuration and plan a gradual, well-structured migration. Skipping this step can lead to issues that are easily avoided with proper preparation.
{% endhint %}

#### 1. What Customers Must Know Upfront

* **Migrations take time**: Even small setups require weeks of planning and testing; larger ones may take months.
* **Costs go beyond licenses**: Budget for app replacements, support, and potential consulting hours.
* **Not all apps migrate smoothly**: Some on-premise apps don't exist on Cloud or behave differently — we’ll help you map alternatives.
* **Integrations are critical**: If you rely on Salesforce, GitHub, ServiceNow, or others, these must be accounted for from day one.
* **User adoption is as important as data migration**: A technically successful migration can fail if users aren’t prepared.

#### 2. How to Plan with Getint

**Step 1 – Define your goals**

* Why migrate? Cost savings, Atlassian support deadlines, scalability, better collaboration?
* Be clear on priorities so the migration plan matches your business needs.

**Step 2 – Audit Your Current Setup**

* Review projects, workflows, custom fields, and automations.
* List all apps in use and mark which are critical vs. "nice-to-have."
* Map all external systems that connect to Jira.

**Step 3 – Budget & Timeline**

* Plan for phased migration (waves).
* Include costs for apps that need replacements.
* Expect extra time for clean-up and user training.

**Step 4 – Communication Plan**

* Identify your internal champions.
* Create a channel for migration updates and questions.
* Let users know what changes to expect and when.

#### 3. Best Practices During Migration

* **Start small**: Run a pilot migration with one project/team before moving everything.
* **Clean before you move**: Archive unused projects and standardize workflows to simplify the transition.
* **Test more than once**: Run dry migrations to validate data accuracy and permissions.
* **Have a rollback plan**: Always know how you’ll recover if something fails.
* **Document everything**: Track what’s moved, what's pending, and any issues found.
* **Use the sync license to test the tool**: A sync license is included with your migration and remains active for 3 months. We recommend using this time to thoroughly test the tool, get familiar with its features, and ensure everything is working as expected before running your full migration. Starting the migration without a solid understanding of how Getint works can lead to avoidable issues down the line.

#### 4. What Not to Do

* Don’t underestimate app compatibility — this is the #1 issue in every migration.
* Don’t leave communication for the last minute. Silence creates frustration.
* Don’t try to "lift and shift" everything at once.
* Don’t rely only on IT — involve business teams who know the workflows.
* Don’t ignore integrations — migrations fail if critical connections aren’t mapped and tested.

#### 5. Preparing Your Team

* **Training**: Run short workshops on Jira Cloud differences before go-live.
* **Support Presence**: Have a clear escalation path with Getint and your own IT team.
* **Onboarding aids**: Provide quick guides, FAQs, or even AI assistants like Rovo to help with "how do I…" questions.
* **Post-migration check-ins**: Schedule follow-ups after each wave to collect feedback and fix issues.

#### 6. Time & Cost Expectations

* **Timeline**:
  * Small teams: 4–6 weeks with preparation + testing.
  * Medium setups: 2–3 months.
  * Large/complex (multiple tools + apps): 6+ months.
* **Costs**:
  * Jira Cloud licenses.
  * App replacements or upgrades.
  * Migration support hours (internal + Getint consultants if needed).
  * Training and change management.

#### 7. How Getint Supports You

* **Assessment**: We help audit your setup, identify risks, and recommend alternatives.
* **Phased approach**: We plan waves with you, not a risky all-in-one move.
* **Integrations expertise**: We ensure Salesforce, GitHub, ServiceNow, Azure DevOps, etc., continue to work seamlessly.
* **Hands-on support**: Our team is available during and after migration, not just for issues but to guide best practices.
* **Post-migration optimization**: We check integrations, workflows, and performance once you're live.

#### 8. Quick Checklist

✅ Define goals & align leadership.\
✅ Audit apps, workflows, and integrations.\
✅ Budget for more than licenses.\
✅ Plan phased migration waves.\
✅ Run test migrations & validate data.\
✅ Prepare a rollback plan.\
✅ Train and support users before go-live.\
✅ Monitor and optimize post-migration.

If you have questions about pricing or need help with the migration process, please submit a ticket through our [support portal](https://getint.io/help-center). We're happy to assist.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FXgzsQIevLcrguBFkqAcf%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=b82ea5a3-fb20-4d0d-9ff2-1806698c9cf1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Jira to Jira migration

Migrating Epics, tasks, and issues from Jira to Jira can be a significant move for a team or organization.

Getint specializes in handling complex data migrations, ensuring that all relevant data/fields—including Epics, tasks, and issue item types—are accurately transferred from Jira to Jira. We address the data and the relationships and hierarchies between different elements.

Our emphasis on data accuracy and integrity is often a standout feature, ensuring that no important information is lost or corrupted during the migration process.

Discover our comprehensive guide to mastering Jira migrations with Getint. To learn more about how our tool works and how you can maximize its potential, visit [Mastering Jira Migration: A Comprehensive Guide with Getint.](https://www.getint.io/blog/mastering-jira-migration-a-comprehensive-guide-with-getint)

{% hint style="info" %}
This guide is intended to support users of Jira Software, Jira Service Management, and Jira Data Center.
{% endhint %}

### **Requirements for migrating historical data** <a href="#requirements-for-migrating-historical-data" id="requirements-for-migrating-historical-data"></a>

For migrating historical items, you must have a migration license with us as an integration license won’t suffice in this case.

The migration licenses offer different features depending on the scale of your migration. To learn more about and purchase our migration license, please visit our pricing page <https://www.getint.io/pricing> and select the "Migration" tab for more details.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FuZOZBdZuG8mWtxKiqMUT%2FPrices%20for%20data%20migration.png?alt=media&#x26;token=a4cb8326-84aa-4aa0-9b63-0b38e92ae91a" alt=""><figcaption><p>If you have further questions regarding the migration license details, or if you are ready to proceed with your purchase, you can quickly reach out to us via our chat icon, located in the lower right corner of the page.</p></figcaption></figure>

{% hint style="info" %}
Before buying a license, you can use our trial application to preview the migration process. The trial allows up to 20 migration runs, each with a maximum of 5 historical items. After reaching the 20 migration runs threshold, further migrations require a license.

To access our app and install the trial version, please go to
{% endhint %}

### **How to set up your migration** <a href="#how-to-set-up-your-migration" id="how-to-set-up-your-migration"></a>

**1.** For setup integration between Jira and Jira, you can check the steps to build this integration here:[<img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Ficon%2FPRq8D5IBseUvQPEVFVwD%2FGitbook%20getint%20sygnet%20logo.png?alt=media&#x26;token=3353768c-d008-46f7-bc2d-fd71b5d48f14" alt="" data-size="line">Jira Jira integration | Getint: Where every ticket finds it's place.](https://docs.getint.io/guides/integration-synchronization/jira-jira-integration)

{% hint style="warning" %}
When you set up the integration, new items created in either of the Jira instances will sync across both platforms. To avoid issues with live environments, you can disable the integration right after setup, schedule migration with the integration off, or pause work in both systems during the migration.
{% endhint %}

**2.** With your integration set, click on the "Migrate Data" button, located in the left side menu:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FAWIsciXqseUz4SgaZzID%2FGo%20to%20Migrate%20data%20in%20the%20integration%20editor.png?alt=media&#x26;token=165d0d23-f3c3-484c-9c9c-205ac0ea2235" alt=""><figcaption></figcaption></figure>

If you are using the app's trial version or have a limited integration license, you'll see a warning indicating that you have a restricted number of Migration Runs available. Each Migration Run is capped at migrating a maximum of 5 items. If you’d like to learn more about the different licensing models and pricing, please visit [<img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Ficon%2FPRq8D5IBseUvQPEVFVwD%2FGitbook%20getint%20sygnet%20logo.png?alt=media&#x26;token=3353768c-d008-46f7-bc2d-fd71b5d48f14" alt="" data-size="line">Licensing and payments | Getint: Where every ticket finds it's place.](https://docs.getint.io/billing-and-services/licensing)

Check the "Enable Migration on Next run" box to continue.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FJ9pkwDckr3EpVU66iQRr%2FEnable%20migration%20on%20the%20next%20run.png?alt=media&#x26;token=01cd14ec-71cb-4ee1-8b74-64e089b465c2" alt=""><figcaption></figcaption></figure>

**3**. On this screen, you can customize your migration by choosing the direction (Right to Left or Left to Right), determining the handling of previously migrated items (replace, update, or skip), and specifying any fields you want to resync to capture updated data post-migration.

Configure your migration preferences, then either enter the specific item IDs you wish to migrate or leave the field blank to instead add a date range at the bottom to include items created within that period. The tool will migrate all items that fall within the specified date range, so please make sure that in case you want to migrate specific items by their IDs, to fill a date range that covers the date of creation of these items.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FW0SU7nx22oC2mifIUkcq%2FMigration%20configuration.png?alt=media&#x26;token=e6554eff-2f88-4f26-9959-6187ce82893e" alt=""><figcaption></figcaption></figure>

**4**. With the migration set per your preference, click "Schedule Migration" at the bottom. The tool should migrate the items based on the specifications on the next synchronization run.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F6KWTTSBUafSGoNeC1Mbo%2FJira%20Jira%20Scheduling%20migration.png?alt=media&#x26;token=216fc84c-9ded-404d-9759-c5be9d8d0ef2" alt=""><figcaption></figcaption></figure>

**5.** After scheduling a migration, you can observe the results of your migration through the reporting section or the "latest runs" from the left menu.

Your items should have been successfully migrated, you can check the receiving end to verify the integrity of the migrated data (note that migration runs are displayed as "MIGRATION," under the "Mode" column)

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMe4NNw7FiRBAGVZG86j8%2FChecking%20migration%20on%20latest%20runs.png?alt=media&#x26;token=20469597-2e83-4ed9-a57d-31b63047e28f" alt=""><figcaption></figcaption></figure>

### **Jira Service Management - Jira Software migration**

When it comes to Jira Jira migrations, the most common scenario is syncing Jira Software with Jira Service Management or vice-versa. With Getint, this is achievable by simply connecting the corresponding projects to both Jira instances. For more information on how to connect Jira instances, please refer to this [guide](https://docs.getint.io/guides/quickstart/connection#jira).

Below you can see an example of how tasks will be migrated from one side to the other.

#### **Project 1 - Jira Software**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FRmFNW5ixytLkmNqxy8Zd%2FJira%20Software%20Tasks.png?alt=media&#x26;token=6de72060-9dd2-47c8-b986-7ea3bdef787f" alt=""><figcaption><p>Existing tasks in a Jira Software project</p></figcaption></figure>

#### **Project 2 - Jira Service Management**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FZz2wrlsbNCSXjDMFH8Fs%2FMigratin%20tasks%20from%20Jira%20Software%20to%20Jira%20Service%20Management.png?alt=media&#x26;token=3205877a-c5e3-4511-82c5-39b07bb91bf1" alt=""><figcaption><p>Note how tasks were recreated in this Jira Service Management project</p></figcaption></figure>

### **Migrating based on Date Range**

To migrate data based on creation dates, use our calendar to select the relevant dates for your tasks. Getint will then recognize the specified timeframe and fetch only the tasks from that period.

{% embed url="<https://www.loom.com/share/79edd7b69a6b4f5cac5a9ab0a4056cd6?sid=813dcc76-0277-42b0-8175-2c1fc1d97139>" %}

### **Migrating based on item's IDs**

To migrate data based on item IDs, simply copy the relevant IDs to sync only the specified tasks. Getint will then identify these IDs and retrieve the associated tasks.

{% embed url="<https://www.loom.com/share/7c6122a6e5a647f0b0c7528b0b658455?sid=23396daa-f5a6-41e5-ac53-91970830def4>" %}

### **Migrating based on Filters**

To migrate data based on the filters you applied to the integration, use the relevant filters to sync only the specified tasks. Getint will then recognize these filters and retrieve the associated tasks.

{% embed url="<https://www.loom.com/share/448fbda5211844ff8428f232bfe5a897?sid=8fc8d84c-f891-44a3-8b60-932495e47082>" %}

{% hint style="info" %}
If you experience any issues while performing the process above, please raise a ticket through our [support portal.](https://getint.io/help-center)
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Jira to Asana Migration

Migrating tasks and projects from Asana to Jira is an important process when transitioning between project management platforms. Whether you're unifying workflows, scaling operations, or consolidating tools across departments, Getint’s Migration Feature ensures a structured and accurate transfer of historical data.

Unlike standard integrations that sync only newly created or updated items, the migration feature enables a one-time, bulk transfer of existing data while preserving essential details such as custom fields, status, relationships, and item types.

This guide walks you through the steps to configure and execute a migration from Asana to Jira using Getint.

### Requirements for Migrating Historical Data <a href="#requirements-for-migrating-historical-data" id="requirements-for-migrating-historical-data"></a>

#### Migration License <a href="#migration-license" id="migration-license"></a>

Migrating historical data requires a migration license, as integration licenses alone do not support this functionality. Migration licenses are billed separately.

To purchase a license, visit our [Pricing Page](https://www.getint.io/pricing) and select the "Migration" tab. You can also contact our team via the [Help Center](https://getint.io/help-center) for assistance.

Before purchasing, we encourage you to test the process using our trial version, which allows:

* Up to 20 migration runs
* A maximum of 5 items per run

To begin your trial, visit: [Getint for Asana and Jira on Atlassian Marketplace](https://marketplace.atlassian.com/apps/1223932/asana-integration-for-jira-2-way-sync-and-data-migration?hosting=cloud\&tab=overview)

For best practices and advanced tips, see: [Master Jira Migration with Getint](https://www.getint.io/blog/mastering-jira-migration-a-comprehensive-guide-with-getint)

### Preparing Your Environment Before Migration <a href="#preparing-your-environment-before-migration" id="preparing-your-environment-before-migration"></a>

#### Handling Fields That Cannot Be Mapped <a href="#handling-fields-that-cannot-be-mapped" id="handling-fields-that-cannot-be-mapped"></a>

Before starting the migration, ensure that all required custom fields exist on both Asana and Jira. If a field does not exist on one side, you must create it before attempting to map it.

Need help? Refer to: [How to Create Custom Fields](https://docs.getint.io/guides/integration-synchronization/how-to-create-a-custom-field-in-all-supported-software#hardbreak-asana).

#### Migrating Values Without 1:1 Mapping <a href="#migrating-values-without-1-1-mapping" id="migrating-values-without-1-1-mapping"></a>

If a field in Asana doesn’t have a direct counterpart in Jira, you can use the **Use label from the other side** option to inject its value into a custom text field.

**Steps:**

* Create a custom Text field in Asana.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FjV3EFDOyvvjTKSlxjRPX%2Fimage-20250512-123626.png?alt=media&#x26;token=c4745cca-0dc8-4b6f-808f-e936df3fc380" alt=""><figcaption></figcaption></figure>

* In the Getint field mapping screen, map the source Asana field to the Jira text field.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FHyU4ZnAYjT1mzZjWv6zA%2Fimage-20250512-123903.png?alt=media&#x26;token=5ee09a3d-c1cb-4610-bcef-22bbcbdd2d1b" alt=""><figcaption></figcaption></figure>

* Enable **Use label from the other side** to insert the original value.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F0MZYv42b7ypYLJmtPjnX%2Fimage-20250512-123959.png?alt=media&#x26;token=b3d1bf63-d2b2-4c9e-aab1-a325ad66d660" alt=""><figcaption></figcaption></figure>

This approach will insert the label/value of the original field into the destination field. Especially helpful for migrating the Assignees. You probably don’t want to recreate the accounts of people no longer in the company in Jira. This way, no mapping is required; we will inject the value into a text field.

You can also migrate values from **multiple source fields into one** text field. You can read more about how to set up this option [here](https://docs.getint.io/guides/integration-synchronization/how-to-map-fields#concatenating-fields).

For more tips, refer to [Master Jira Migration with Getint - Your Ultimate Guide](https://www.getint.io/blog/mastering-jira-migration-a-comprehensive-guide-with-getint).

### How to Set Up Your Asana to Jira Migration <a href="#how-to-set-up-your-asana-to-jira-migration" id="how-to-set-up-your-asana-to-jira-migration"></a>

#### 1. Set Up an Asana to Jira Integration <a href="#id-1.-set-up-an-asana-to-jira-integration" id="id-1.-set-up-an-asana-to-jira-integration"></a>

Before migrating, you must set up a working integration between Jira and Asana. Follow our full [Jira-Asana Integration Guide](https://docs.getint.io/guides/integration-synchronization/jira-asana-integration) to configure your connection properly.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FSvy95z9Kvshil5z0p8mM%2Fimage-20250512-124531.png?alt=media&#x26;token=0224910d-eba6-476c-abd8-0668b5da5478" alt=""><figcaption></figcaption></figure>

To avoid live data conflicts, we recommend either disabling the integration after setup or scheduling the migration outside of active working hours.

#### 2. Access the Migration Feature <a href="#id-2.-access-the-migration-feature" id="id-2.-access-the-migration-feature"></a>

Once your integration is set:

* Click **Migrate Data** from the left-side menu.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FdrtpInX8JzdfzQX0V0lm%2Fimage-20250512-125316.png?alt=media&#x26;token=5e2f9ecd-9cf6-439c-b772-91f500e5d21e" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
If you're on a trial version, a warning will appear regarding your migration limits (5 items per run, 20 runs).
{% endhint %}

* Check the **Enable Migration on the Next Run** box to proceed.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FgadajEQ4kTU24NjEcZ9E%2Fimage-20250512-125558.png?alt=media&#x26;token=acb0d343-8551-4d9e-bb79-96a34fd92330" alt=""><figcaption></figcaption></figure>

#### 3. Configure Migration Settings <a href="#id-3.-configure-migration-settings" id="id-3.-configure-migration-settings"></a>

* **Migration Direction:** Choose whether data flows from Asana to Jira or vice versa.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FZaqQt83Ese1D2djmuzlQ%2Fimage-20250512-125705.png?alt=media&#x26;token=e6c4edc7-79ef-44c3-8b25-e06474986abf" alt=""><figcaption></figcaption></figure>

* **Handling Previously Migrated Items:** Choose how to handle items that were already migrated:
  * **Replace** (overwrite existing items).
  * **Update** (sync only new changes).
  * **Skip** (ignore already migrated items).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FdRNDAuISjwsO7seO1AMz%2Fimage-20250512-125821.png?alt=media&#x26;token=25d81f7b-5429-4c0b-ae7b-87aebdb4c03f" alt=""><figcaption></figcaption></figure>

* **Selective Resync (Optional)**: If a previous migration was incomplete, choose specific fields to **resync**, such as **Assignee, Status, and Description**.
  * To resync **all fields**, enter ***ALL**.*

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FPPNPalCKtrdlhqNF2EQU%2Fimage-20250512-130254.png?alt=media&#x26;token=20265acc-6a3a-497c-80ef-e04472dd2e5b" alt=""><figcaption></figcaption></figure>

* **Selective Item Migration (Optional)**:
  * Enter specific **item IDs** to migrate **only selected tasks**.
  * Use **JQL filtering** for refined selection.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FSsDfVm3pzYRUCCRqkbEU%2Fimage-20250512-140152.png?alt=media&#x26;token=cb91ba8a-0acd-4b17-a6b9-b3b580fd3d0c" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
**Important:** Ensure that your **JQL filter or item IDs align with the creation/updating date range** to avoid missing items during migration.
{% endhint %}

* **Time Range Filtering:**
  * Select a **creation date range** in the **UTC timezone**.
  * Only issues created or updated **within the selected period** will be migrated.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FLZfYYu3i2xtfj3AbmeBF%2Fimage-20250512-140320.png?alt=media&#x26;token=3d628d54-3843-46bf-bef1-d7bb9b778e27" alt=""><figcaption></figcaption></figure>

#### 4. Schedule and Run the Migration <a href="#id-4.-schedule-and-run-the-migration" id="id-4.-schedule-and-run-the-migration"></a>

* Click **Schedule Migration** to queue the process.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fz2H6pQvQ6vEFueqHMnqA%2Fimage-20250512-140451.png?alt=media&#x26;token=935d2c4f-9efe-4510-b684-adbb75dbf51c" alt=""><figcaption></figcaption></figure>

* The system will begin migration during the next synchronization run.
* Monitor progress in the **Reporting section** or the **Latest Runs tab**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9I93s40uthydlKArWKxH%2Fimage-20250512-140605.png?alt=media&#x26;token=5a4f893c-c72d-47c0-9f3b-8732cf08e89f" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Migration runs appear under the **Mode** column as **MIGRATION** instead of **SYNC**.
{% endhint %}

#### 5. Enable Continuous Sync After Migration (Optional) <a href="#id-5.-enable-continuous-sync-after-migration-optional" id="id-5.-enable-continuous-sync-after-migration-optional"></a>

If you want to keep the items in sync after migration:

* Open the **Integration Settings**.
* Click **More > Enable Continuous Sync**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Frb861nQrkzpw6C0jtivW%2Fimage-20250512-140811.png?alt=media&#x26;token=7ce59181-861f-4dcf-bba0-a8e8f42f3040" alt=""><figcaption></figcaption></figure>

Alternatively, you can uncheck the disable box when setting up the migration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F67jPVRSm3xwinnGkbzyn%2Fimage-20250512-140848.png?alt=media&#x26;token=bd21e263-3330-4c61-b048-a0be5f4a54c4" alt=""><figcaption></figcaption></figure>

This ensures that **newly created** tasks, issues, and updates flow **between Jira and Zendesk** moving forward.

### Why Choose Getint Migration Over CSV Import? <a href="#why-choose-getint-migration-over-csv-import" id="why-choose-getint-migration-over-csv-import"></a>

Traditional CSV methods can result in data loss, manual fixes, and inconsistencies. Getint Migration offers key advantages:

#### 1. Smart Field Mapping <a href="#id-1.-smart-field-mapping" id="id-1.-smart-field-mapping"></a>

* ✔ Allows precise manual field mapping for accuracy
* ❌ CSV imports require manual rework after upload

#### 2. Selective Migration <a href="#id-2.-selective-migration" id="id-2.-selective-migration"></a>

* ✔ JQL filtering, item ID targeting, and date-based migrations
* ❌ CSV imports require entire bulk imports

#### 3. Real-Time Monitoring <a href="#id-3.-real-time-monitoring" id="id-3.-real-time-monitoring"></a>

* ✔ Live sync logs, error reports, and migration tracking
* ❌ CSV imports offer no live visibility

#### 4. Seamless Transition <a href="#id-4.-seamless-transition" id="id-4.-seamless-transition"></a>

* ✔ Integrated post-migration syncing
* ❌ CSV requires additional manual alignment

### Need Help? <a href="#need-help" id="need-help"></a>

If you need further assistance with your Jira to Asana migration, please open a ticket at our [Help Center.](https://getint.io/help-center)

Considering migration? [**Schedule a Demo**](https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team) with our **experts** to explore how **Getint** can optimize your **Jira to Asana** migration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# Jira to Azure DevOps Migration

Migrating Epics, tasks, and work items from Jira to Azure DevOps is a critical step for organizations consolidating platforms or transitioning development and support workflows. With Getint, this migration process becomes straightforward, accurate, and reliable.

Getint ensures that all essential data, including issue types, custom fields, and relationships, are transferred while preserving the integrity and hierarchy of your records. Whether you're moving an entire backlog or selectively migrating specific items, this guide walks you through the process step-by-step.

### Requirements for Migrating Historical Data <a href="#requirements-for-migrating-historical-data" id="requirements-for-migrating-historical-data"></a>

#### Migration License <a href="#migration-license" id="migration-license"></a>

Migrating historical data requires a migration license, as integration licenses alone do not support this functionality. Migration licenses are billed separately.

To purchase a license, visit our [Pricing Page](https://www.getint.io/pricing) and select the "Migration" tab. You can also contact our team via the [Help Center](https://getint.io/help-center) for assistance.

Before purchasing, we encourage you to test the process using our trial version, which allows:

* Up to 20 migration runs
* A maximum of 5 items per run

To begin your trial, visit: [Azure DevOps Integration for Jira (Azure DevOps Connector)](https://marketplace.atlassian.com/apps/1223931/azure-devops-integration-for-jira-azure-devops-connector?hosting=cloud\&tab=overview)

For best practices and advanced tips, see: [Master Jira Migration with Getint](https://www.getint.io/blog/mastering-jira-migration-a-comprehensive-guide-with-getint).

### Preparing Your Environment Before Migration <a href="#preparing-your-environment-before-migration" id="preparing-your-environment-before-migration"></a>

#### Handling Fields That Cannot Be Mapped <a href="#handling-fields-that-cannot-be-mapped" id="handling-fields-that-cannot-be-mapped"></a>

Before starting your migration, ensure that custom fields used in Azure DevOps also exist in Jira. If the destination field is missing, it must be created manually to enable proper mapping.

For steps to create fields in both tools, refer to: [How to Create Custom Fields](https://docs.getint.io/guides/integration-synchronization/how-to-create-a-custom-field-in-all-supported-software#hardbreak-azure-devops).

#### Migrating Values Without 1:1 Mapping <a href="#migrating-values-without-1-1-mapping" id="migrating-values-without-1-1-mapping"></a>

If a field in Azure DevOps doesn’t have a direct counterpart in Jira or you want to avoid the 1:1 mapping, you can use the **Use label from the other side** option to inject its value into a custom text field.

**Steps:**

* Create a text custom field in Azure DevOps.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FpzDvf5Rf2blw7Hj9MVOU%2FCreate%20a%20custom%20field%20in%20Azure%20DevOps.png?alt=media&#x26;token=62d2bbf7-82d9-4e62-bb59-bcda4f56bc09" alt=""><figcaption></figcaption></figure>

* In the Getint field mapping screen, map the source Azure DevOps field to the Jira text field.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F4Tp7DUr0rnDfwNQyvX9a%2Fmapping%20the%20custom%20field%20in%20Azure.png?alt=media&#x26;token=ff76e065-671a-4881-ac76-d689367ae95d" alt=""><figcaption></figcaption></figure>

* Enable **Use label from the other side** to insert the original value.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FIuUUNbxAP8Jpm7QCUMsC%2Fuse%20label%20from%20other%20side%20Jira%20Azure.png?alt=media&#x26;token=28b12597-6f67-42ae-9143-e8cf40ec985e" alt=""><figcaption></figcaption></figure>

This approach will insert the label/value of the original field into the destination field. Especially helpful for migrating the Assignees. You probably don’t want to recreate the accounts of people no longer in the company in Jira. This way, no mapping is required; we will inject the value into a text field.

You can also migrate values from **multiple source fields into one** text field. You can read more about how to set up this option [here](https://docs.getint.io/guides/integration-synchronization/how-to-map-fields#concatenating-fields).

For more tips, refer to: [Master Jira Migration with Getint - Your Ultimate Guide](https://www.getint.io/blog/mastering-jira-migration-a-comprehensive-guide-with-getint).

### Setting Up Your Azure DevOps to Jira Migration <a href="#setting-up-your-azure-devops-to-jira-migration" id="setting-up-your-azure-devops-to-jira-migration"></a>

#### 1. Set Up the Integration <a href="#id-1.-set-up-the-integration" id="id-1.-set-up-the-integration"></a>

Before migrating, you must set up a working integration between Jira and Azure DevOps. Follow our full integration guide, [Jira Azure DevOps Integration Guide](https://docs.getint.io/guides/integration-synchronization/jira-azure-devops-integration), to configure your connection properly.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FmHL3ePjZNb7xfL7lpFsv%2FJira%20Azure%20Migration.png?alt=media&#x26;token=d9d95ed8-63c5-4b33-96bd-679f72d77640" alt=""><figcaption></figcaption></figure>

After setup, we recommend disabling the integration or pausing activity in both tools during migration to avoid sync conflicts.

#### 2. Access the Migration Feature <a href="#id-2.-access-the-migration-feature" id="id-2.-access-the-migration-feature"></a>

Once your integration is set:

* Click **Migrate Data** from the left-side menu.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FN4qV2A2sfVgfJKoNFgs6%2FJira%20Azure%20Migration%20Setup.png?alt=media&#x26;token=08a22f37-e623-4520-b13d-7e8aa4210ddb" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
If you're on a trial version, a warning will appear regarding your migration limits (5 items per run, 20 runs).
{% endhint %}

* Enable **Migration on Next Run** to proceed.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FtnIaYWS8PNOX2dxaXQIL%2FEnable%20migration%20in%20the%20next%20run%20Azure.png?alt=media&#x26;token=ce7c8159-b43a-4df4-9db6-fdac9857fb0b" alt=""><figcaption></figcaption></figure>

#### 3. Configure Migration Settings <a href="#id-3.-configure-migration-settings" id="id-3.-configure-migration-settings"></a>

* **Migration Direction:** Choose whether data flows from Azure DevOps to Jira or vice versa.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F2T5dRDuJdOHvJ8AvUfAY%2Fconfigure%20migration%20settings.png?alt=media&#x26;token=7593f941-076f-4bf5-9292-3376715c0563" alt=""><figcaption></figcaption></figure>

* **Handling Previously Migrated Items:** Choose how to handle items that were already migrated:
  * **Replace** (overwrite existing items).
  * **Update** (sync only new changes).
  * **Skip** (ignore already migrated items).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FxR15fCl6XSwuhZFtnj1U%2Fhandling%20previously%20migrated%20items.png?alt=media&#x26;token=9fd1d89f-c909-4f70-9c35-febfbdd42795" alt=""><figcaption></figcaption></figure>

* **Selective Resync (Optional)**: If a previous migration was incomplete, choose specific fields to **resync**, such as **Assignee, Status, and Description**.
  * To resync **all fields**, enter ***ALL**.*

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FYNcO6muware6HZM7JZza%2Fimage-20250523-130947.png?alt=media&#x26;token=82f08bf0-0f24-4987-8766-9bc13846b73a" alt=""><figcaption></figcaption></figure>

* **Selective Item Migration (Optional)**:
  * Enter specific **item IDs** to migrate **only selected tasks**.
  * Use **JQL filtering** for refined selection.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FoLrap4iw5XORIS36RJyH%2Fimage-20250523-131103.png?alt=media&#x26;token=33ceb6e0-b674-4318-9c3b-447ab412c357" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
**Important:** Ensure that your **JQL filter or item IDs align with the creation/updating date range** to avoid missing items during migration. Learn more: [Filtering Items for Integration](https://docs.getint.io/getintio-platform/workflows/filtering-items-for-integration-in-getint).
{% endhint %}

* **Time Range Filtering:**
  * Select a **creation date range** in the **UTC timezone**.
  * Only issues created or updated **within the selected period** will be migrated.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMGZrMQO1xaLGJhgQwB8i%2Fimage-20250523-131322.png?alt=media&#x26;token=e5a678b6-5cff-4015-8f57-0606e01125b5" alt=""><figcaption></figcaption></figure>

#### 4. Schedule and Run the Migration <a href="#id-4.-schedule-and-run-the-migration" id="id-4.-schedule-and-run-the-migration"></a>

When your settings are complete, click **Schedule Migration** at the bottom of the screen.

* Click **Schedule Migration** to queue the process.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FDbwJaUrzp1IceajTLkvN%2Fimage-20250523-131558.png?alt=media&#x26;token=e101f590-8137-475a-925b-8e02872b8f98" alt=""><figcaption></figcaption></figure>

* The system will begin migration during the next synchronization run.
* Monitor progress in the **Reporting section** or the **Latest Runs tab**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FLMTmoSTXztlRkJrQHFM4%2Fimage-20250523-131516.png?alt=media&#x26;token=b78ef2c3-c451-4f2f-a31a-14f23488fa73" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Migration runs appear under the **Mode** column as **MIGRATION** instead of **SYNC**.
{% endhint %}

#### **5. Enable Continuous Sync After Migration (Optional)** <a href="#id-5.-enable-continuous-sync-after-migration-optional" id="id-5.-enable-continuous-sync-after-migration-optional"></a>

If you want to keep the items in sync after migration:

* Open the **Integration Settings**.
* Click **More > Enable Continuous Sync**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FVAtUH8FJ12qL34ca3sOk%2Fimage-20250523-131839.png?alt=media&#x26;token=bf53a187-b090-42f1-8ece-a18c952ae3ed" alt=""><figcaption></figcaption></figure>

You can also uncheck the box below when you are setting up the migration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FGSvfgOEKyKwlYxDPNg1t%2Fimage-20250523-131757.png?alt=media&#x26;token=7cea7425-52d7-4ef5-8cda-14206b62f7e0" alt=""><figcaption></figcaption></figure>

This ensures that **newly created** tasks, issues, and updates flow **between Jira and Azure DevOps** moving forward.

### **Why Choose Getint Migration Over CSV Import?** <a href="#why-choose-getint-migration-over-csv-import" id="why-choose-getint-migration-over-csv-import"></a>

Traditional CSV imports require manual data manipulation and lack automation, often leading to data loss and inconsistency. Getint eliminates these issues by providing:

#### **1. Smart Field Mapping** <a href="#id-1.-smart-field-mapping" id="id-1.-smart-field-mapping"></a>

✔ Getint enables precise **manual field mapping**, ensuring correct **data alignment**\
❌ CSV imports require **manual restructuring** after import

#### **2. Selective Migration** <a href="#id-2.-selective-migration" id="id-2.-selective-migration"></a>

✔ Getint supports **JQL filtering, item ID selection, and date-based migration**\
❌ CSV imports transfer **all data**, requiring **manual clean-up**

#### **3. Real-Time Monitoring** <a href="#id-3.-real-time-monitoring" id="id-3.-real-time-monitoring"></a>

✔ Getint provides **sync logs, error tracking, and live migration updates**\
❌ CSV imports offer **no real-time feedback**

#### **4. Seamless Integration** <a href="#id-4.-seamless-integration" id="id-4.-seamless-integration"></a>

✔ Getint **automatically syncs** data post-migration\
❌ CSV imports require **additional steps** to align projects and workflows

### **Need Help?** <a href="#need-help" id="need-help"></a>

For additional **assistance or troubleshooting**, visit our [**Help Center**](https://getint.io/help-center).

Considering migration? [**Schedule a Demo**](https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team) with our **experts** to explore how **Getint** can optimize your **Jira to Azure DevOps** migration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

# GitLab to Jira migration

Sometimes all you need is to migrate from one tool/project to the other. Getint.io provides an answer to this. Request migration feature if you need it.

The Migration feature lets you migrate the data between GitLab and Jira (both directions).

This feature is available on request - write to us at <getint@getint.io>.

Read more about the special pricing offer for migrations [here](https://www.getint.io/pricing).

### How to set it up

To enable migration, you need to build the workflow first [(learn how to build the workflow)](https://docs.getint.io/getintio-platform/workflows).\
Based on your settings (where you decide what types and fields to migrate if you want to include attachments, custom fields, and so on), the getint.io platform will execute the migration. \
Then, enable the migration feature, as shown in the video below.

{% embed url="<https://youtu.be/o9XDRRXSGeY>" %}

---

[Next Page](/llms-full.txt/1)

# Source: https://docs.getint.io/getting-started-with-the-platform/about-getint-concepts/how-getint-works-how-it-syncs-the-data.md

# How Getint Works (How it Syncs the Data)

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

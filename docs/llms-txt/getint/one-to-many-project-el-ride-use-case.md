# Source: https://docs.getint.io/getintio-platform/workflows/integrating-one-project-with-many-streamlining-synchronization-across-multiple-projects./one-to-many-project-el-ride-use-case.md

# One to Many Project - El Ride Use Case

In today's intricate business environment, precise task integration is a cornerstone for efficient operations. Getint offers customized solutions, empowering organizations to synchronize tasks precisely according to project requisites and team preferences. This guide provides an in-depth overview of configuring integrations effectively within the distinctive ecosystem of various tools. The company needs to keep different teams, using different tools, in sync and wants to be able to have a helicopter view of what’s happening across different teams and tools for the management.

&#x20;                                                <img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fvlbjjr1GYYLnofGg0VnD%2F35ea3527-3322-4532-bb4f-2eaa7c66dfef-removebg-preview.png?alt=media&#x26;token=762ed90d-acd7-470b-9317-7ca726f6b95d" alt="" data-size="original">

### Use Case: Bike Company Utilizing Jira as the Central Hub <a href="#use-case-bike-company-utilizing-jira-as-the-central-hub" id="use-case-bike-company-utilizing-jira-as-the-central-hub"></a>

Imagine a biking company, El Ride, that uses Jira Software as their main tool, the central hub. This company has two types of integration needs: internal and external.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fx87bhu1HriTA3CMd1V52%2Fimage-20240517-144322.png?alt=media&#x26;token=42820645-bea4-4bce-a89e-4c0c43bf2550" alt=""><figcaption></figcaption></figure>

### Internal Integration <a href="#internal-integration" id="internal-integration"></a>

1. **Management Overview**
   * **Tool**: Jira Software
   * **Purpose**: Provides management with a general overview of everything happening within the company. Dashboards are built and monitored based on this data. Please see our [guide](https://docs.getint.io/guides/integration-synchronization/jira-jira-integration) to creating a connection
2. **Development Team**
   * **Tool**: Azure DevOps
   * **Purpose**: Developers working on the online store use Azure DevOps. This tool is integrated with Jira to track all development progress centrally. Please see our [guide](https://docs.getint.io/guides/integration-synchronization/jira-azure-devops-integration) to creating a connection
3. **Service Team**
   * **Tool**: ServiceNow
   * **Purpose**: Handles customer service requests and issues. ServiceNow is integrated with Jira for centralized issue management and tracking, and with DevOps to address incidents that require IT Development team support. Please see our [guide](https://docs.getint.io/guides/integration-synchronization/jira-servicenow-integration) to creating a connection
4. **Marketing Team**
   * **Tool**: Asana
   * **Purpose**: Manages marketing projects and tasks. Asana is integrated with Jira to sync marketing projects and ensure alignment with other teams and DevOps to address tasks requiring IT Development team support and with Salesforce to work on the sales materials and lead campaigns. Please see our [guide](https://docs.getint.io/guides/integration-synchronization/jira-asana-integration) to creating a connection
5. **Sales Team**
   * **Tool**: Salesforce
   * **Purpose**: Manages sales activities and customer relationships. Salesforce integrates with Jira to sync sales projects and data and Asana to work with the Marketing team. Please see our [guide](https://docs.getint.io/guides/integration-synchronization/jira-salesforce-integration) to creating a connection
6. **Cross-Functional Integrations**
   * **Salesforce and Asana**: Connected to facilitate collaboration between the marketing and sales teams on sales materials.
   * **Asana and Azure DevOps**: Integrated to allow for seamless web changes and updates, ensuring marketing projects reflect the latest developments. Please see our [guide](https://docs.getint.io/guides/integration-synchronization/azure-devops-asana-integration) to creating a connection

### External Integration <a href="#external-integration" id="external-integration"></a>

1. **Service Team Integration**
   * **ServiceNow and Jira Service Management**: The external service team connects their Jira Service Management with ServiceNow, which the first-level support team uses. This integration allows first-level customer support requests via telephone to be escalated to more expert levels within the bike company's ServiceNow system.
2. **Design Company Integration**
   * **External Design Team's Jira**: The main Jira instance is connected to the Jira Software used by an external design company. Designs provided by this company need management approval within the bike company's Jira.

### Configuring Complex Syncs <a href="#configuring-complex-syncs" id="configuring-complex-syncs"></a>

Companies like El Ride sometimes require syncing one project or instance in one app to several projects in another. This setup is complex for various reasons, including:

* **Avoiding Duplicates**: To prevent duplication of tasks and ensure data integrity across platforms.
* **Multiple Integrations**: Many integrations must be created to facilitate syncing between multiple projects.
* **Performance Concerns**: Executing integrations one by one can impact performance and efficiency.
* **Security:** The integration must be set up considering security to ensure proper access control and prevent unauthorized viewing.

### 1. Getting Connected <a href="#id-1.-getting-connected" id="id-1.-getting-connected"></a>

Our first step involves creating service accounts and linking the apps, and our Guides [Prepare for Integration](https://docs.getint.io/getting-started-with-the-platform/preparing-for-the-integration) and [Connection](https://docs.getint.io/guides/quickstart/connection) will help in this first step. Followed by linking projects and defining filters. Since Jira plays a central role in the company's workflow, we will utilize it as the primary hub for integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FXZeQJpH2XrNAeGvk0WQo%2FScreenshot%202024-06-03%20194247.png?alt=media&#x26;token=bec3e439-ccd3-45ba-9b7f-5c01e4a7b718" alt=""><figcaption></figcaption></figure>

To kick things off, we'll connect [Jira Software with Asana](https://docs.getint.io/guides/integration-synchronization/jira-asana-integration). This integration allows seamless task exchange between the Marketing and Development teams, ensuring campaign coordination and project alignment.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FENuRTQIPr44JCVUfmbcq%2FScreenshot%202024-06-03%20194347.png?alt=media&#x26;token=4aa50e65-b98f-4009-8e54-595d3fade60c" alt=""><figcaption></figcaption></figure>

### 2. Set Up Filters for Precision <a href="#id-2.-set-up-filters-for-precision" id="id-2.-set-up-filters-for-precision"></a>

With Jira serving as the central hub, we'll tailor filters for the Asana connection based on specific project requirements. For instance, tasks tagged for Q2 will be selectively synced to maintain focus and clarity.

**To achieve this:**

1. Access the filter settings adjacent to the Asana app icon.
2. Apply filters based on criteria such as project quarters, ensuring only relevant tasks are transferred.
3. Save the integration with an identifier for easy management.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FldBHrsrWTnXV9OAPWQXg%2FUntitled%20design%20(7).jpg?alt=media&#x26;token=b81a4b5f-5b3a-494c-a479-f3d04d6dcefb" alt=""><figcaption></figcaption></figure>

### When is Filtering Needed? <a href="#when-is-filtering-needed" id="when-is-filtering-needed"></a>

Filtering is crucial in various scenarios to ensure efficient and relevant data synchronization across multiple platforms. Here are some specific use cases:

1. **Project-Specific Syncing**: When tasks from a particular project must be synced to specific projects in another tool. For example, marketing tasks tagged for a specific campaign should sync only to the relevant project in Jira.
2. **Role-Based Access**: Filtering helps ensure that only the relevant information is accessible to different organizational roles. For instance, sensitive sales data should sync only to Salesforce and not be visible in Asana.
3. **Data Overload Prevention**: To prevent overwhelming team members with irrelevant tasks. For instance, syncing only high-priority tasks from ServiceNow to Jira to avoid cluttering the dashboard with low-priority issues.
4. **Time-Based Filtering**: Syncing tasks based on timelines or deadlines. For example, tasks tagged for Q2 in Asana should sync to the Q2 project in Jira.
5. **Custom Workflows**: When specific workflows require tailored syncing criteria. For example, development tasks that need approval before syncing to production can be filtered to ensure that only approved tasks are transferred.

### 3. Name and Save the Integration <a href="#id-3.-name-and-save-the-integration" id="id-3.-name-and-save-the-integration"></a>

Assigning distinct names to integrations facilitates efficient management and quick identification of associated projects or applications. Additionally, grouping integrations can further streamline the process for enhanced organization.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fmxi4disNAvM1RSGdGW1x%2FUntitled%20design%20(8).jpg?alt=media&#x26;token=e9b86326-1725-4d16-9aad-9b2e7ec29b1c" alt=""><figcaption></figcaption></figure>

### 4. Setting Up New Integrations for Multiple Projects <a href="#id-4.-setting-up-new-integrations-for-multiple-projects" id="id-4.-setting-up-new-integrations-for-multiple-projects"></a>

Once Asana's hooked up for Marketing, it's time to bring in the rest of the team – like ServiceNow for customer support. Since it's a different app, you must start fresh with a new integration. However, if you want to use other projects within the same application like Asana, it's as easy as hitting duplicate.

**Steps to Set Up New Integrations:**

1. Head to the workflows section and find your existing integrations.
2. Tap the option to create a new integration for the new tool.
3. Configure the settings and criteria specific to the new tool.
4. Make Jira your central hub for task management and customize filters for each integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FdYBCyFoDfIWvZBIQn76T%2FEl%20ride%201.png?alt=media&#x26;token=d0c551db-455a-44a2-9049-724583e9e4d7" alt=""><figcaption></figcaption></figure>

### 5. Repeat the Process for Other Platforms <a href="#id-5.-repeat-the-process-for-other-platforms" id="id-5.-repeat-the-process-for-other-platforms"></a>

Repeat the integration process for additional applications like Salesforce for Sales or Azure DevOps for development. Each integration is customized to align with the specific needs of the respective teams:

**Steps to Repeat:**

1. Use the filter icon to start sorting through issues for each app.
2. Set up the right operators and criteria for each platform – think Lead in Salesforce, for example.
3. Name each integration with something catchy, so you always know who's who.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FzHoFMMRe1RhWMlsvNFul%2FEl%20ride%202.jpg?alt=media&#x26;token=51edea51-3862-453f-885c-fb5b6e5d576a" alt=""><figcaption></figcaption></figure>

### 6. Using the Filtering with JQL for Jira <a href="#id-6.-using-the-filtering-with-jql-for-jira" id="id-6.-using-the-filtering-with-jql-for-jira"></a>

For advanced filtering, Getint offers the option to use JQL filters, providing greater flexibility in defining criteria for task synchronization across projects and platforms. This feature enables precise control over the flow of information, enhancing overall efficiency and workflow management:

**Steps for JQL Filtering:**

1. Select the application icon.
2. Below the integration details, a field for the JQL filter will be available.
3. Write the JQL details defining the criteria that the application should follow.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F5hcVXgFDK8aaT8SyDxmv%2FEl%20ride%203.jpg?alt=media&#x26;token=1e880b32-74f8-4447-bb49-9b27cab59f52" alt=""><figcaption></figcaption></figure>

### Pros and Cons of this type of connection: <a href="#pros-and-cons-of-this-type-of-connection" id="pros-and-cons-of-this-type-of-connection"></a>

**Pros:**

* **Centralized Management**: Syncing one project across multiple applications allows centralized task and data management.
* **Efficiency**: Streamlined workflows save time and reduce the likelihood of errors.
* **Visibility**: All stakeholders can access relevant information, promoting transparency and collaboration.

**Cons:**

* **Overwhelming Data**: Large volumes of synced data may overwhelm projects, leading to cluttered interfaces.
* **Lack of Granularity**: The one-size-fits-all approach may not adequately address varying project priorities or requirements.
* **Complexity**: Managing synchronization settings for multiple projects can be complex and require careful planning.

### Getint Best Practices <a href="#getint-best-practices" id="getint-best-practices"></a>

* **Selective Syncing**: Users can choose which data elements or tasks are synced to each project, offering flexibility and control.
* **Custom Mapping**: Customize mapping settings for each project to align with specific requirements.
* **Integration Filters**: Incorporate filters to define criteria for data synchronization, filtering out irrelevant information.
* **Project Mapping**: Map one project or instance from the originating application to multiple projects in the receiving application for accurate data distribution.

Getint's advanced filtering capabilities empower organizations to streamline task integration effectively. With features like selective syncing, integration filters, and project mapping, Getint ensures precise data transfer across platforms. By leveraging these solutions, organizations can overcome the complexities of task integration and achieve seamless collaboration between teams and projects.

### Use Case Example <a href="#use-case-example" id="use-case-example"></a>

Integrating a single project with multiple others demands meticulous planning to avoid synchronization hiccups. With Getint, "El Ride" ensures precise task synchronization across various projects and platforms by implementing accurate filters and assigning unique names to integrations. Following these steps, specific tasks from Asana are efficiently integrated into Jira, ensuring seamless project management across platforms.

By following these guidelines, organizations can achieve efficient and streamlined project synchronization, ensuring all teams are aligned and working harmoniously.

{% hint style="info" %}
For complicated cases like this, we can offer customized licensing for you. Please reach out to <https://getint.io/help-center> and we will assist you with this.
{% endhint %}

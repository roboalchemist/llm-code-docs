# Set up and manage Agentforce in Slack

Agentforce makes it possible for an organization to build custom agents that handle specific aspects of their work. When you deploy Agentforce in Slack, your team can collaborate with agents right where they’re already getting work done.

## How it works

- [Build and customize agents](#build-and-customize-agents) in Salesforce, then [add them to Slack](#add-agents-to-slack) to make them available to your members.
- Once they’ve been added to Slack, members can [find and message agents](https://slack.com/help/articles/36218786859667-Use-Agentforce-in-Slack/) they have access to in the **Agentforce** tab or [message them in channels](https://slack.com/help/articles/36218786859667-Use-Agentforce-in-Slack#chat-with-an-agent-in-a-channel).

**Learn more about Agentforce:** [Visit our launch guide](https://slack.com/resources/collections/launching-agentforce-in-slack) or [contact your Slack Account Executive](https://slack.com/ai-agents/contact-sales).

## Build an agent in Salesforce

Use the guidance below to get started with [creating an agent](https://help.salesforce.com/s/articleView?id=ai.agent_setup_create.htm&type=5) using Agentforce Builder in Salesforce:

- Create an agent using [pre-made templates](https://help.salesforce.com/s/articleView?id=ai.agent_employee_agent_setup.htm&type=5) for Slack.
- Customize your agent with [topics](https://help.salesforce.com/s/articleView?id=ai.copilot_topics.htm&type=5) and [actions](https://help.salesforce.com/s/articleView?id=ai.copilot_actions.htm&type=5) to define its scope and expertise.
- Add the **General Slack Actions** topic to your agent to choose from a set of [Slack actions](https://help.salesforce.com/s/articleView?id=ai.copilot_actions_ref.htm&type=5) like [creating a canvas](https://help.salesforce.com/s/articleView?id=ai.copilot_actions_ref_slack_create_canvas.htm&type=5) (not available on the [free version of Slack](https://slack.com/help/articles/27204752526611-Feature-limitations-on-the-free-version-of-Slack)), [performing a search](https://help.salesforce.com/s/articleView?id=ai.copilot_actions_ref_slack_search.htm&type=5), and more.

**Note:** You can only build agents for Slack using the Agentforce [Employee Agent type](https://help.salesforce.com/s/articleView?id=ai.agent_setup_explore_types.htm&type=5).

### Agent templates for Slack

Agent templates allow you to quickly create an agent to handle common tasks. When [creating an agent from a template](https://help.salesforce.com/s/articleView?id=ai.agent_employee_agent_setup.htm&type=5), search for **Slack** to view the available templates. There are three agent templates available for Slack:

- **Customer Insights Agent**  
  Uses Salesforce data to summarize customer information, find subject matter experts in Slack, and generate customer briefs.
- **Employee Help Agent**  
  Resolves internal issues by answering frequently asked questions using internal resources and conversations in Slack.
- **Onboarding Agent**  
  Helps onboard new team members by creating onboarding canvases and answering frequently asked questions from custom knowledge bases.

## Connect Salesforce and Slack

To set up Agentforce in Slack, connect your Salesforce organization to Slack. You’ll need help from an [admin in Salesforce](https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.basics_understanding_administrator.htm&type=5) to complete this process.

### Step 1: Connect a Salesforce org to Slack

1. Follow the steps in our [Connect Salesforce and Slack](https://slack.com/help/articles/30754346665747-Connect-Salesforce-and-Slack) guide.
2. Once your Salesforce org is connected, you’ll need to manually map users if they haven’t already been granted access to Salesforce in Slack.

### Step 2: Install the Slack connected app

1. From Salesforce, select **Setup**.
2. In the Quick Find box, search for and select **Connected Apps OAuth Usage**.
3. Scroll down to **Slack**, then select **Install** on the right.
4. Click **Install** to finish.

**Note:** People in Slack that don’t have a Salesforce account will need a provisional Salesforce license to access Agentforce in Slack. Reach out to your Salesforce Account Executive to learn more.

### Step 3: Map accounts

Connect your members’ Salesforce and Slack accounts. When you manually map members in Slack, they’ll be prompted to sign in to Salesforce to connect their accounts.

#### Pro and Business+ plans

1. From your desktop, click **Admin** in the sidebar.
2. Select **Workspace settings** from the menu, then click **Salesforce**.
3. Click the **Users** tab.
4. Select **Add individually** and search for the member you’d like to add. To add members in bulk, click **Add by CSV** and follow the prompts.

#### Enterprise plans

1. From **Home**, click your organization name in the sidebar.  
   ![Image 1](https://a.slack-edge.com/8e8e4/helpcenter/img/workspace-picker@2x.jpg)
2. Hover over **Tools & settings**, then click **Organization settings**.
3. Click **Salesforce**, then select **Salesforce organizations**.
4. Click the **Users** tab.
5. Select **Add individually** and search for the member you’d like to add. To add members in bulk, click **Add by CSV** and follow the prompts.

**Tip:** Members with the [Salesforce admin system role](https://slack.com/help/articles/360018112273-Types-of-roles-in-Slack#system-roles) in Slack can connect Salesforce orgs and map accounts.

## Add an agent to Slack

Now that Salesforce and Slack are connected, you’re ready to add agents. Keep in mind that member access for Employee Agents is [assigned automatically based on permissions in Salesforce](https://help.salesforce.com/s/articleView?id=ai.agent_manage_aea_access.htm&type=5). If you're installing an [Agentforce Service Agent](https://help.salesforce.com/s/articleView?id=service.service_agent_overview.htm&type=5), be sure to [assign member access](#assign-member-access) when installation is complete.

### Step 1: Create an agent connection

First, establish a connection to Slack for your agent in Salesforce:

1. Sign in to Salesforce, then select **Setup**.
2. In the **Quick Find** box, search for and select **Agents**.
3. Select an agent.
4. Click the **Connections** tab.
5. Click **Add**.
6. Below **Connection**, select **API** from the drop-down menu.
7. Enter a unique **Integration Name**.
8. Below **Connected App**, select **Slack**.
9. Click **Save**.

### Step 2: Install an agent

Once you’ve established a connection for your agent, add it to Slack.

#### Pro and Business+ plans

1. From your desktop, click **Admin** in the sidebar.
2. Select **Manage Agentforce** from the menu.
3. Next to the agent you'd like to add, click **Review agent**.
4. Review the permissions the agent will have in Slack, then click **Install Agent**.

#### Enterprise plans

First, install and grant the agent access at the org level. Then, you can add the agent to specific workspaces in your org.

1. From **Home**, click your **organization name** in the sidebar.  
   ![Image 2](https://a.slack-edge.com/8e8e4/helpcenter/img/workspace-picker@2x.jpg)
2. Hover over **Tools & settings**, then click **Organization settings**.
3. Click **Salesforce**, then select **Agentforce**.
4. Next to the agent you’d like to add, click **Review Agent**.
5. Review the permissions the agent will have in Slack, then click **Install Agent**.
6. Check the box next to the workspace(s) the agent should be available in.
7. Click **Add to Workspaces**.

## Manage Agentforce agents in Slack

You can manage agents in Slack by editing their profile, assigning member access, and uninstalling them.

### Edit an agent’s profile

Owners, admins, Agent Builders, and assigned Agent Managers can edit an agent’s profile right in Slack. To change the profile picture, adjust suggested prompts, or assign additional agent managers, follow the steps below:

1. From your desktop, click **Agentforce** in the sidebar. If you don’t see **Agentforce**, click **More** to find it.
2. Click **Managed by you**.
3. Next to an agent, click the **three dots icon**, then select **View Agent Profile**.
4. Click **Edit**.
5. Edit the profile fields you’d like to change, then click **Save**.

### Assign access to a Service Agent

By default, no one can use [Agentforce Service Agents](https://help.salesforce.com/s/articleView?id=service.service_agent_overview.htm&type=5) in Slack until they’re assigned access by an owner or admin.

#### Pro and Business+ plans

1. From your desktop, click **Admin** in the sidebar.
2. Select **Manage Agentforce** from the menu.
3. Click **Installed agents** at the top of the page.
4. Next to an agent, click **Manage Agent**.
5. Next to **Who can use this agent?**, click **Edit**.
6. Choose who can access the agent, then click **Save**.

#### Enterprise plans

1. From **Home**, click your **organization name** in the sidebar.  
   ![Image 3](https://a.slack-edge.com/8e8e4/helpcenter/img/workspace-picker@2x.jpg)
2. Hover over **Tools & settings**, then click **Organization settings**.
3. Click **Salesforce**, then select **Agentforce**.
4. Next to the agent you’d like to add, click **Review Agent**.
5. Review the permissions the agent will have in Slack, then click **Install Agent**.
6. Check the box next to the workspace(s) you’d like to remove the agent from and click **Next**.
7. Check the box next to **I’m ready to remove this agent**, then select **Remove agent**.

### Remove or uninstall an agent

On the Pro and Business+ plans, you can uninstall an agent. On Enterprise plans, you can remove an agent from specific workspaces, or uninstall it from your organization.

#### Pro and Business+ plans

1. From your desktop, click **Admin** in the sidebar.
2. Select **Manage Agentforce** from the menu.
3. Click **Installed agents** at the top of the page.
4. Next to an agent, click **Manage Agent**.
5. Click **Manage** in the top-right corner, then select **Remove [agent name]**.

### Remove an agent from a workspace

1. From **Home**, click your **organization name** in the sidebar.  
   ![Image 4](https://a.slack-edge.com/8e8e4/helpcenter/img/workspace-picker@2x.jpg)
2. Hover over **Tools & settings**, then click **Organization settings**.
3. Click **Salesforce**, then select **Agentforce**.
4. Click **Installed agents** at the top of the page, then click **Manage agent** next to the agent you'd like to remove.
5. Select **Manage** in the top right, then click **Remove from a workspace**.
6. Check the box next to the workspace(s) you’d like to remove the agent from and click **Next**.
7. Check the box next to **I’m ready to remove this agent**, then select **Remove agent**.

### Uninstall an agent from your org

1. From **Home**, click your **organization name** in the sidebar.  
   ![Image 5](https://a.slack-edge.com/8e8e4/helpcenter/img/workspace-picker@2x.jpg)
2. Hover over **Tools & settings**, then click **Organization settings**.
3. Click **Salesforce**, then select **Agentforce**.
4. Click **Installed agents** at the top of the page, then click **Manage agent** next to the agent you'd like to uninstall.
5. Select **Manage** in the top right, then click **Uninstall from your organization**.
6. Check the box next to **I’m ready to remove this agent**, then click **Remove agent**.

**Who can use this feature?**

- **Workspace Owners** / **Admins** (Free, Pro, and Business+ plans)  
  **Org Owners** / **Admins** (Enterprise plans)
- Available on [**all Slack plans**](https://slack.com/pricing) with a Salesforce [Agentforce](https://www.salesforce.com/agentforce/) license
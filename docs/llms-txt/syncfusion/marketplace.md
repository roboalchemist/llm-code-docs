# Source: https://docs.syncfusion.com/code-studio/reference/configure-properties/mcp/marketplace.md

# MCP Marketplace Documentation

## Overview
The **MCP Marketplace** is a centralized platform for server management, helping users discover, install, and connect the right servers for their needs through an easy-to-use interface. It showcases a variety of available MCP servers. Users can explore server options and configure them for use by simply clicking the **Install** button, which initiates an automated setup process to integrate the server with the Code Studio extension.



## Steps to Install an MCP Server from Marketplace
- Click the **Syncfusion Code Studio** icon on the top right side  to open the Syncfusion Code Studio chat window.

  <img src="../../reference-images/marketplace1.png" alt="marketplace" >

- Navigate to **Configure Chat** by clicking the gear icon.

  <img src="../../reference-images/marketplace2.png" alt="marketplace" >

- Select **MCP Servers** from the drop-down menu.

  <img src="../../reference-images/marketplace3.png" alt="marketplace" >

- After selecting MCP Servers, it navigates to the Marketplace tab:

   - You can find predefined MCP servers such as **Azure DevOps, Figma, MongoDB, Playwright, Postgres,etc**.
   - Choose and install any of them.
   
   <img src="../../reference-images/marketplace4.png" alt="marketplace" >

- Click the **Install** button to install the MCP server.

   <img src="../../reference-images/marketplace5.png" alt="marketplace" >

- After installation, the MCP tools appear in the **Tools** section:

  - Select **Configure Tools**.

   <img src="../../reference-images/marketplace6.png" alt="marketplace" >

  - Verify the tools added in the dropdown list.

   <img src="../../reference-images/marketplace7.png" alt="marketplace" >

- Open the Marketplace and select **Installed** to check the servers youâve added.

   <img src="../../reference-images/mcpfilter2.png" alt="marketplace" >



## Filter Support in Marketplace
- The Marketplace allows you to apply filters to quickly narrow down and find the servers you need:

   
   - By selecting **Available**, it will show the MCP servers currently available.

    <img src="../../reference-images/mcpfilter3.png" alt="marketplace" >

   - By selecting **Installed**, it will narrow down to show only the installed servers.

    <img src="../../reference-images/mcpfilter2.png" alt="marketplace" >

   

  

   - By sorting by **Name**, it will list servers alphabetically.

   - By sorting by **Newest**, it will show the most recently added MCP servers.

    <img src="../../reference-images/mcpfilter6.png" alt="marketplace" >

   - By filtering **Categories**, you can easily narrow down to specific categories (e.g., Database, Cloud Platform), and it will display all available servers in those categories.

    <img src="../../reference-images/mcpfilter7.png" alt="marketplace" >

   - Using the **Search** option, you can quickly find the desired MCP server.

    <img src="../../reference-images/mcpfilter4.png" alt="marketplace" >




## Example Usage of GitHub MCP Server

### Step 1: Installation of GitHub MCP Server
- Open the Marketplace tab.
- There you can find GitHub and click install 

  <img src="../../reference-images/github1.png" alt="marketplace" >

### Step 2: Provide Access Token
- After clicking Install, you will be prompted to enter a **GitHub Personal Access Token**.
- Enter a valid access token generated from your GitHub account.
- After entering the access token, click Continue to complete the installation successfully
- Help Link for creating a access token : [Personal Access Tokens](https://github.com/settings/tokens).

  <img src="../../reference-images/github2.png" alt="marketplace" >

### Step 3: Select the Installed Tool
- Identify the GitHub MCP server from **Configure Tool**.
- Select the tools you need from the GitHub MCP server and add them.

  <img src="../../reference-images/github3.png" alt="marketplace" >

### Step 4: Formulate Your Prompt
- Decide what action you want the tool to perform.
- Write the prompt in the chat panel.
  Example : 

  <img src="../../reference-images/github4.png" alt="marketplace" >

### Step 5: Execute the Command
- Hit **Enter** to run the command.
- The MCP system parses your request and prepares execution.

### Step 6: Allow or Skip Permissions
- The system may ask you to allow or skip execution (for security reasons).

    <img src="../../reference-images/github5.png" alt="marketplace" >

- If you choose **Allow**, the tool proceeds.
- If you choose **Skip**, the action is canceled.

### Step 7: Confirm Branch Availability
- Once allowed, the tool executes the action.
- After that check the **Branches section** in your GitHub repository.
- Ensure the newly created branch (e.g., `exception-handling`) appears in the list.




## Uninstalling an MCP Server
- Go to the **Marketplace** tab.
- Select the **Installed** filter to view all installed MCP servers.
- Choose the MCP server you want to uninstall.
- Click **Uninstall** to remove the selected server.

  <img src="../../reference-images/uninstallmcp.png" alt="marketplace" >


## Best Practices
- **Clear Service Boundaries**: Keep each MCP server focused on a single responsibility.responsibility (e.g., database, browser automation, API gateway) to simplify scaling and maintenance.
- **Strong Security Controls**: Enforce authentication, authorization, and encrypted communication. Apply the principle of least privilege and maintain audit logs.
- **Resilience & Reliability**: Implement health checks, retries, and circuit breakers. Design for graceful degradation so services remain usable under stress.
- **Observability & Monitoring**: Provide metrics, structured logs, and tracing. Use tools like Prometheus/Grafana for visibility into performance and failures.
- **Developer Friendly Documentation**: Offer clear onboarding guides, versioned APIs, and examples. Good documentation accelerates adoption and reduces support overhead.


## Note
If you want to add a new MCP server, you can request it by creating a support ticket using the link provided below. This ensures your request is tracked, reviewed, and considered for inclusion.

**Link:** [Create Ticket](https://codestudio.syncfusion.com/agent/tickets/create)

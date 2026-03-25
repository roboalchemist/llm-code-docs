# Source: https://docs.xano.com/xano-features/workspace-settings/audit-logs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Audit Logs

> Audit Logs provide clear and searchable logging of all workspace changes

<Check>
  **Limited Availability**

  This feature is still in development and not widely available. If you have any questions, please reach out to your Xano representative for more information.
</Check>

<Info>
  **Quick Summary**

  Audit Logs provide detailed and searchable information about any changes or activity inside of a Xano workspace.
</Info>

## What's included in Audit Logs?

<Tabs>
  <Tab title="Workspace">
    ### Workspace

    * **Create Workspace** - Create new workspaces
    * **Update Workspace** - Modify workspace settings
    * **Reset Workspace** - Reset workspace to default state
    * **Read Workspace** - View workspace information
    * **Delete Workspace** - Remove workspaces

    ### Data Sources

    * **Create Data Source** - Set up new data connections
    * **Update Data Source** - Modify data source settings
    * **Delete Data Source** - Remove data sources

    ### Branch Management

    * **Create Branch** - Set up new development branches
    * **Update Branch** - Modify branch settings
    * **Delete Branch** - Remove branches
    * **Merge Branch** - Combine branches
    * **Set Live Branch** - Designate the active production branch
  </Tab>

  <Tab title="Environment Variables">
    * **Read Environment Variable** - View environment variable details
    * **Create Environment Variable** - Create new environment variable
    * **Update Environment Variable** - Modify environment variable
    * **Delete Environment Variable** - Remove environment variabl
  </Tab>

  <Tab title="Tenants">
    * **Read Tenant Environment Variable** - View tenant environment variables
    * **Create Tenant Environment Variable** - Create tenant environment variable
    * **Update Tenant Environment Variable** - Modify tenant environment variable
    * **Delete Tenant Environment Variable** - Remove tenant environment variable
    * **Create Tenant** - Set up new tenants
    * **Update Tenant** - Modify tenant settings
    * **Delete Tenant** - Remove tenants
    * **Read Tenant License** - View tenant licensing information
    * **Update Tenant License** - Modify tenant licenses
    * **Impersonate Tenant** - Act on behalf of a tenant

    ### Backup & Restore

    * **Create Tenant Backup** - Generate tenant backups
    * **Restore Tenant Backup** - Restore from tenant backups

    ### Release Management

    * **Create Release** - Generate new releases
    * **Update Release** - Modify release information
  </Tab>

  <Tab title="Database">
    ### Table Activity

    * **Create Table** - Set up new database tables
    * **Update Table** - Modify table structure and settings
    * **Delete Table** - Remove tables
    * **Restore Table** - Recover deleted tables
    * **Truncate Table** - Clear all data from tables
  </Tab>

  <Tab title="Function Stacks">
    ### API Groups

    * **Create API Group** - Set up new API endpoint groups
    * **Update API Group** - Modify API group settings
    * **Delete API Group** - Remove API groups
    * **Restore API Group** - Recover deleted API groups

    ### APIs

    * **Create Query** - Build new API
    * **Update Query** - Modify existing API
    * **Delete Query** - Remove API
    * **Restore Query** - Restored a previous version
    * **Run Query** - Execute database queries

    ### Functions

    * **Create Function** - Build new custom functions
    * **Update Function** - Modify existing functions
    * **Delete Function** - Remove functions
    * **Restore Function** - Restored a previous version

    ### Add-ons

    * **Create Add-on** - Install new add-ons
    * **Update Add-on** - Modify add-on settings
    * **Delete Add-on** - Remove add-ons
    * **Restore Add-on** - Restored a previous version
    * **Run Add-on** - Execute add-on functionality

    ### Tasks

    * **Create Task** - Set up new automated tasks
    * **Update Task** - Modify task settings
    * **Delete Task** - Remove tasks
    * **Restore Task** - Restored a previous version
    * **Run Task** - Execute tasks
  </Tab>
</Tabs>

## Audit Log Retention

Depending on your plan, you'll be able to retain different amounts of audit logs.

* Free/Build: `24h`
* Launch, Starter, Starter+ : `7 days`
* Scale, Pro, Pro +: `28 days`
* Enterprise/Custom: `Unlimited`

## Accessing and Using Audit Logs

<Danger>
  Please note that if your instance has [RBAC (Role-based Access Control)](/enterprise/enterprise-features/rbac-role-based-access-control) enabled, any users that you want to be able to view the logs need to have the **Workspace Logs** permission applied.
</Danger>

<Steps>
  <Step title="From the workspace dashboard, click the three dots in the top-right corner, and choose Audit Logs" />

  <Step title="Viewing Audit Logs">
    From the main view, you'll be presented with a list of all available logs.

    <Frame caption>
            <img src="https://mintcdn.com/xano-997cb9ee/tjSJ_pOzk8E0WRhF/images/c320879d-image.jpeg?fit=max&auto=format&n=tjSJ_pOzk8E0WRhF&q=85&s=62c7482204c62fe941f27af0dcdf2fa6" alt="" width="1587" height="858" data-path="images/c320879d-image.jpeg" />
    </Frame>

    Click on a log to view more details about that event.

    <Frame caption>
            <img src="https://mintcdn.com/xano-997cb9ee/o7zunZFYmjx8RZ8N/images/f4a55ef3-image.jpeg?fit=max&auto=format&n=o7zunZFYmjx8RZ8N&q=85&s=f45ac23249c94a859ea1f6800dca58ae" alt="" width="445" height="880" data-path="images/f4a55ef3-image.jpeg" />
    </Frame>

    On some event types, you'll have a Go To button to quickly navigate to where the change took place. The JSON playload can be useful for your own external data collection.
  </Step>

  <Step title="Searching and Filtering Audit Logs">
    You can search your Audit Logs from the search panel above the list.

    <Frame caption="Please note that the search only looks at the summary title of each event currently.">
            <img src="https://mintcdn.com/xano-997cb9ee/dyVYERTquSXdpw_-/images/a06404eb-image.jpeg?fit=max&auto=format&n=dyVYERTquSXdpw_-&q=85&s=6069043f9e8ea851b220a1e83d0e32a6" alt="" width="779" height="161" data-path="images/a06404eb-image.jpeg" />
    </Frame>

    You can also use the filters to quickly narrow down specific event types, users, and labels.

    <Frame caption>
            <img src="https://mintcdn.com/xano-997cb9ee/Qia2QBMIuWWrGb-s/images/1ce6299e-image.jpeg?fit=max&auto=format&n=Qia2QBMIuWWrGb-s&q=85&s=580fda53a60258415eb1b313e069822a" alt="" width="1599" height="317" data-path="images/1ce6299e-image.jpeg" />
    </Frame>
  </Step>

  <Step title="Exporting Audit Logs">
    #### Exporting to CSV

    From the top-right corner of your screen, click the three dots and choose Export CSV to export the current batch of logs as a CSV.

    #### Using the Metadata API

    There are two new endpoints available via the [Metadata API](/xano-features/metadata-api) to retrieve Audit Logs.
  </Step>
</Steps>


Built with [Mintlify](https://mintlify.com).
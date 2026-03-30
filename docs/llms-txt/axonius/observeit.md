# Source: https://docs.axonius.com/docs/observeit.md

# ObserveIT

ObserveIT provides insider threat security solutions, including employee monitoring, user activity monitoring, behavioral analytics, policy enforcement, and digital forensics.

## Adapter Parameters

* **MSSQL Server** *(required)* - The DNS / IP Address of the Microsoft SQL Server your ObserveIT instance is using.
  * To use a specific named instance, the value supplied should be in the following format: `{server_host}\{instance_name}`.
  * If no instance is supplied, the default instance will be used.
* **Port** *(optional, default: 1433)* - The port used for the connection.
* **Database** *(required)* - The name of the database inside the SQL Server (Usually starts with "CM\_").
* **User Name** *(required)* - A user name with read-only permissions .

  **Important Notes:**

  * The best practice is to create a dedicated SQL local user for Axonius usage. For details, see [Creating a Local Read-Only User  for Microsoft SQL Server](/docs/microsoft-sql-server-mssql#creating-a-local-readonly-user-for-microsoft-sql-server).
  * If you are using a domain user, specify the domain and the user name in the following format: domain\username.
* **Password** *(required)*  - The user's password. The password must not include ";".

<Image alt="OberverIt.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OberverIt.png" />

<Callout icon="📘" theme="info">
  NOTE

  For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).
</Callout>

## Advanced Settings

Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)

To configure the ObserveIT adapter advanced settings, open the **ObserveIT adapter** page, click **Advanced Settings**, and then click the **ObserveIT Configuration** tab:

* **SQL pagination** *(required, default: 1000)* - Set the number of results per page received for a given SQL query, to gain better control of the performance of all connections  for this adapter.

<Image alt="ObservitAdvanced.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ObservitAdvanced.png" />

<Callout icon="📘" theme="info">
  NOTE

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Required Ports

Axonius must be able to communicate with the MSSQL Server via the following ports:

* Microsoft SQL Server discovery port - 1433.
* The specific port for the supplied named instance, if relevant.

## Troubleshooting

* **"Login failed"** - If you are using a domain user, in the **User Name** field, specify the domain and the user name in the following format: domain\username.
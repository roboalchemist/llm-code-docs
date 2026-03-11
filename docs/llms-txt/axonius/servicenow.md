# Source: https://docs.axonius.com/docs/servicenow.md

# ServiceNow

## Overview

ServiceNow provides service management software as a service, including IT services management (ITSM), IT operations management (ITOM), and IT business management (ITBM).

An accurate Configuration Management Database (CMDB) is crucial for your ITSM program. It can often be a single source of truth for tracking and managing IT assets. Axonius collects data across multiple adapters to perform [CMDB Reconciliation and Remediation](https://docs.axonius.com/docs/cmdb-reconciliation-and-remediation).

## Types of Assets Fetched

### Cyber & Software Assets

![](https://files.readme.io/ec086cdf823db1e0ed64d98c6c85dcd48fda2e0e85f020a1c48e19102d693c7e-devices.svg) Devices ![](https://files.readme.io/3df2652b3ae372a16f17272613c0d7ca2c6495ed1eee7d209569c3860086ebd1-users.svg) Users ![](https://files.readme.io/57dbff8b10b5f9f86bcc56a3f99fe2401d3e839b4166bb9e8c1430462cf58782-software.svg) Software ![](https://files.readme.io/d8d2f675f38d58a0a1d0b0baa0d69dfcdcd2e69200f9a1d13f1f6788ee674d43-roles.svg) Roles ![](https://files.readme.io/085e5879d236e9ffb784ca783b50d7ce35047123bbd547ddde8bd16a82d5eedb-groups.svg) Groups ![](https://files.readme.io/d38e68c628a60c64dadc91a1458fc13c66e13b8886b123573020763dbdae1585-tickets.svg) Tickets ![](https://files.readme.io/66e2d736ae845c1f84043eca01fd81bda00e2ea2e120bedc93ae071ae0c4317e-compute-services.svg) Compute Services ![](https://files.readme.io/219406200e3133a9561d54e5f093d867bdc2a00d6bf3e408a3691f3b8a45a9db-load-balancers.svg) Load Balancers

![](https://files.readme.io/f3f37e2a830914a3bd5ab4db997c68d477c314a10bcc8a1f78f3dd1a621d66af-databases.svg) Databases ![](https://files.readme.io/63eb85f5476bc64303dfcc01aeed2fe673d328b629ea31e45e8f105a097856d8-containers.svg) Containers ![](https://files.readme.io/08fa18d5d10eb337cc3c8f3187c48d283a41ec7dc6e82f3e2a78b82b274009b0-object-storage.svg) Object Storage ![](https://files.readme.io/634d21eaf6e9f69a19cd0f00cba1bc8d45f48efd6b450685f11540af9e6efe3d-permissions.svg) Permissions ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Accounts_Tenants.svg) Accounts & Tenants

***

### SaaS Applications

![](https://files.readme.io/fae714433d9de3b43b58268c16387d253796a3ac579d759f510ac28c7884cfaf-application-settings.svg) Application Settings ![](https://files.readme.io/ddc84fe94b76c954e09a97dfd0c2df7ba93c475fefd5b6033a85afb18f5d4916-business-applications.svg) Business Applications ![](https://files.readme.io/af9b907315a9eb55dcc363582312b1c2239d2ed2d902bbc259172c78f3d19220-saas-applications.svg) SaaS Applications

***

<br />

<Callout icon="📘" theme="info">
  ➡️ Use this adapter (**ServiceNow**) to fetch updates to tickets that were created by Axonius Enforcement Actions, provided these tickets have not been deleted from Axonius.

  ➡️ Use the [**ServiceNow Tickets Fetch** adapter](/docs/servicenow-tickets-fetch), to fetch all tickets from:

  * The incidents table
  * Any additional tables
</Callout>

<br />

## Data Retrieved from ServiceNow

Data retrieved from ServiceNow is highly customizable, as each deployment can vary greatly. By default, Axonius connects to the following tables and their child tables.

<Columns layout="auto">
  <Column>
    * cmdb\_ci\_computer
    * cmdb\_ci\_vm
    * cmdb\_ci\_vm\_instance
    * cmdb\_ci\_printer
    * cmdb\_ci\_netgear
    * u\_cmdb\_ci\_computer\_atm
  </Column>

  <Column>
    * cmdb\_ci\_comm
    * cmdb\_ci\_cluster
    * cmdb\_ci\_cluster\_vip
    * cmdb\_ci\_facility\_hardware
    * cmdb\_ci\_msd
    * sys\_user
  </Column>
</Columns>

You can add or remove tables using the adapter [Advanced Configuration settings](https://docs.axonius.com/axonius-help-docs/docs/servicenow-advanced-settings).

## Before You Begin

### Authentication Methods

You can connect the adapter using either of the following authentication methods:

* **Username/Password** (Cyber & Software Assets only)
* **OAuth with Client ID/Secret** (Cyber & Software Assets, SaaS Applications, Identities, Enforcement Actions)

### Required Permissions

The following roles and or permissions are required:

<Tabs>
  <Tab title="Cyber & Software Assets">
    <Columns layout="auto">
      <Column>
        Roles:

        * itil
        * rest\_api\_explorer
        * web\_service\_admin
      </Column>

      <Column>
        Permissions:

        **read** permission to the sys\_audit\_delete table
      </Column>
    </Columns>
  </Tab>

  <Tab title="SaaS Applications">
    <Columns layout="auto">
      <Column>
        Roles:

        * snc\_read\_only
      </Column>

      <Column>
        Permissions:

        **read** permission in the following tables:

        * syslog\_transaction
        * sysevent\_script\_action
        * sys\_email\_filter
        * sys\_dictionary
        * sys\_properties
        * password\_policy
        * v\_plugins
        * sys\_user
      </Column>
    </Columns>
  </Tab>

  <Tab title="Enforcement Actions">
    Permissions:

    * ITIL Admin
  </Tab>
</Tabs>

***

### APIs

Axonius uses the following APIs:

* [Table API](https://developer.servicenow.com/dev.do#!/reference/api/utah/rest/c_TableAPI)
* [IRE API](https://docs.servicenow.com/bundle/vancouver-api-reference/page/integrate/inbound-rest/concept/c_IdentifyReconcileAPI.html), if the  'Use IdentifyReconcile Discovery Source to create computer' setting is configured

## Additional ServiceNow Pages

[Deploying the ServiceNow Adapter](https://docs.axonius.com/axonius-help-docs/docs/deploying-the-servicenow-adapter)

[ServiceNow Advanced Settings](/docs/servicenow-advanced-settings)

[Custom Asset Schema](/docs/servicenow-adv-settings-custom-asset-schema)

[Showing JSON Fields in Basic View](/docs/servicenow-showing-adv-settings-json-fields-in-basic-view)

[Configuring Delta Fetch in ServiceNow](/docs/configuring-delta-fetch-in-servicenow)

<br />

## Related Enforcement Actions

Refer to the ServiceNow [Related Enforcement Actions](https://docs.axonius.com/axonius-help-docs/docs/servicenow-enforcement-actions).

<br />
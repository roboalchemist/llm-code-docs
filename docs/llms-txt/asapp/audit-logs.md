# Source: https://docs.asapp.com/getting-started/setup/audit-logs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Audit Logs

> Learn how to view, search, and export audit logs to track changes in AI Console.

All activities in AI Console are saved as events and are viewable in audit logs. These logs provide a detailed record of configuration changes made in AI-Console for AI Services and ASAPP Messaging.

The system saves these records indefinitely, providing administrators with a comprehensive historical view of changes made to ASAPP services, including when they were made and by whom.

Administrators of your ASAPP organization can access audit logs.

Audit logs allow you to:

* See the most recent changes made to every resource.
* Investigate a particular historical change associated with a deployment.
* Review activity for a given user or product over the course of weeks or months.

To access Audit Logs:

1. Navigate to the AI-Console home page
2. Select Admin

<Frame>
  <img src="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4c72fddf-e958-b9d7-08a1-94132217ed81.png?fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=c27c4128f00e04788214d2a00a299fe7" alt="View of the audit logs landing page." data-og-width="1600" width="1600" data-og-height="966" height="966" data-path="image/uuid-4c72fddf-e958-b9d7-08a1-94132217ed81.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4c72fddf-e958-b9d7-08a1-94132217ed81.png?w=280&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=f48c7626d4ff7ff376acbd6016417fed 280w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4c72fddf-e958-b9d7-08a1-94132217ed81.png?w=560&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=c8bd35218b4d6dea5853b3ca70a8272a 560w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4c72fddf-e958-b9d7-08a1-94132217ed81.png?w=840&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=f09a537ff1873602a99e932acecb6305 840w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4c72fddf-e958-b9d7-08a1-94132217ed81.png?w=1100&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=dd1a48f61582f30ed13028f739de943b 1100w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4c72fddf-e958-b9d7-08a1-94132217ed81.png?w=1650&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=b67a1a19d36437838f52b0f44c8131c6 1650w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4c72fddf-e958-b9d7-08a1-94132217ed81.png?w=2500&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=cd22bf994859e11fa62307b17b16a4d2 2500w" />
</Frame>

The following list displays the resources being tracked:

* **General**
  * Links
  * Custom entities
* **Virtual Agent**
  * Flows
  * Intent routing
* **AI Compose**
  * Global responses

## Audit Logs Entries

For each audit log record, the system records the following fields:

| Field         | Description                                                                       |
| :------------ | :-------------------------------------------------------------------------------- |
| Resource type | Type of resource modified.                                                        |
| Resource name | Name of the resource modified.                                                    |
| Event type    | Type of event. Supported fields are create, deploy, undeploy, update, and delete. |
| Environment   | Environment where you deployed the resource. Only applicable for deploy events.   |
| User          | Name of user who caused the event.                                                |
| Timestamp     | Time and date the event occurred, in UTC format.                                  |
| Unique ID     | (Optional) Unique identifier for the resource.                                    |

## Searching Audit Logs

Administrators can use the search bar to look for a specific resource name, or user.

To search your audit logs, navigate to the search bar on the top-right corner of the screen.

<Note>
  The search functionality searches for exact matches with either the resource name, or the user that made the change.
</Note>

Additionally, you can filter the results of the audit logs by using the filter dropdown menus.

You can filter by the following fields:

* Resource type
* Event type
* User
* Date

<Tip>
  You can additionally click on the "timestamp" column to re-order the results by ascending or descending dates:

  <Frame>
    <img src="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0beb7055-4087-4d8b-da5e-d11b5a3c7b54.png?fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=2544a123c11d7e95b16ebf5ad8ad63c4" alt="Timestamp column highlighted on the Audit Logs main view." data-og-width="1391" width="1391" data-og-height="169" height="169" data-path="image/uuid-0beb7055-4087-4d8b-da5e-d11b5a3c7b54.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0beb7055-4087-4d8b-da5e-d11b5a3c7b54.png?w=280&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=d887d369d6ecce50bc9d3abf86d5a6ea 280w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0beb7055-4087-4d8b-da5e-d11b5a3c7b54.png?w=560&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=f490d2655e8eca6bc9b7c437c9c8ef7b 560w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0beb7055-4087-4d8b-da5e-d11b5a3c7b54.png?w=840&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=1bda4608c56659ee3ac9386d3bb12b08 840w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0beb7055-4087-4d8b-da5e-d11b5a3c7b54.png?w=1100&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=40833e9eead4d015a79e4ba47274cf0c 1100w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0beb7055-4087-4d8b-da5e-d11b5a3c7b54.png?w=1650&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=d359385ab415a17343a09ea939959a50 1650w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0beb7055-4087-4d8b-da5e-d11b5a3c7b54.png?w=2500&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=58492946c562c7414a3be973bbefc9ae 2500w" />
  </Frame>
</Tip>

## Exporting Audit Logs

Administrators can download the audit logs as a CSV file to store and review later. If you export the audit logs as a .csv file after filtering them using the search bar or filters, the downloaded file will also be filtered.

To download the audit logs as a .csv file:

1. Navigate to the Audit Logs section in AI Console.
2. Click on the download button, next to the search bar.

The system will record data in audit logs from the time the feature is enabled. The system will not display historical activity retroactively.

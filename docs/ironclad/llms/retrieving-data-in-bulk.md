# Source: https://clickwrap-developer.ironcladapp.com/docs/retrieving-data-in-bulk.md

# Retrieving Activity Data in Bulk

Today, there are a few available options for retrieving bulk Activity of data from the Ironclad Clickwrap platform outside of our web application. While reviewing these options, please keep in mind that we encourage you to limit your use of these routes to what is absolutely necessary. If you have more sophisticated or complex needs, please reach out to our support team for additional information on other methods that may be available.

## REST API - Tasks Route

Our REST API provides a `/tasks` route that allows you to programmatically trigger the initiation of generating a CSV export of Activity data.

**How**\
When using the `/tasks/export/activity` route, you are able to export activity data to a CSV asynchronously and retrieve the link(s) to the exported CSV by checking the status of the export with an ID generated upon creating the Task.

For example, your overall flow would look something like this:

<Image title="tasks-flow.jpeg" alt={484} src="https://files.readme.io/47e0898-tasks-flow.jpeg">
  Tasks Process Overview
</Image>

When the export has completed successfully, you’ll see a property links that contains links to the CSV(s) available for download.

### Starting the Export

Below, we’ll cover some key concepts when using this route—which we highly recommend reading through to ensure the exports are successful.

**Filtering**\
When generating the export, you may want to limit the amount of data that is returned. To do this, you can supply a filter parameter that can limit the scope of the query on Activity data. Utilizing this is highly recommended in high-volume environments.

Example: `https://api.pactsafe.com/v1.1/tasks/export/activity?filter=created_time>=2020-10-10 and event_type==agreed`

The above API call when generating the export will only look for Activities that occurred after the specified date and are only agreed events.

**Specifying Fields**\
Additionally, when generating the export, you may want to specify the columns data that gets returned in the CSV. Doing this requires adding a fields parameter with the field names you want to return. The fields `id`, `signer_id`, `created_time` should always be included in your call. If I wanted to specify additional fields like the IP Address, Page Title of the acceptance and a custom data field that I’ve previously used named VIP, my fields parameter and value would look like this: `fields=id,signer_id,created_time,connection_data.remote_address,connection_data.page_title,custom_data.vip`

This will result in the CSV having column headers that appear like the following:

<Table align={["left","left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        id
      </th>

      <th>
        signer\_id
      </th>

      <th>
        created\_time
      </th>

      <th>
        connection\_data.remote\_address
      </th>

      <th>
        connection\_data.page\_title
      </th>

      <th>
        custom\_data.vip
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        5f88980b5944913d477c6dce
      </td>

      <td>
        123
      </td>

      <td>
        2020-10-15T18:42:19.689Z
      </td>

      <td>
        1.1.1.1
      </td>

      <td>
        My Page
      </td>

      <td>
        TRUE
      </td>
    </tr>
  </tbody>
</Table>

Note: not sure which fields are available or used on your site? Make the following call to retrieve the list by doing a GET on `https://api.pactsafe.com/v1.1/sites/:id/exportFields`

**Full POST Example**

```http
https://api.pactsafe.com/v1.1/tasks/export/activity?filter=created_time>=2020-10-10 and event_type==agreed&fields=id,signer_id,created_time,connection_data.remote_address,connection_data.page_title,custom_data.vip&no_count=true&lean=true
```

[View API Reference documentation](https://developer.pactsafe.com/reference/tasks?showHidden=ccd8f#export-activity-to-csv) for more information.

**Example Response**

```json
{
    "data": {
        "status": "pending",
        "source": "api",
        "retry_count": 0,
        "active": true,
        "job_name": "GenerateExportCSV",
        "created_by": 9785,
        "account": 2785,
        "site": 5193,
        "data": {
            "exportName": "action",
            "exportType": "Action",
            "sendTo": "example@example.com"
        }
        "id": "5f88abf5f4689d7295cf1134"
    }
}
```

### Retrieving Job Data and CSV

With the POST response, you’ll need to use the id property and use it to retrieve the status by doing a GET on the following: `https://api.pactsafe.com/v1.1/tasks/export/:id` which tells you the current status of the job and if it has successfully finished, it will provide the link(s) to the CSV (can contain multiple links depending on volume).

[View API Reference documentation](https://developer.pactsafe.com/reference/tasks?showHidden=ccd8f#retrieve-status-on-activity-to-csv) for more information.

> 📘 Automatic Deletion
>
> Please note that these CSVs are automatically deleted after 30 days.

## REST API - Activity Route

Additionally, with our REST API, you can retrieve a “list” of Activity of Signers within Ironclad Clickwrap using the /activity route. This is the easiest way to get data from the Ironclad Clickwrap platform but we also *strongly* recommended working with your Ironclad Clickwrap Customer Success Manager on ensuring the best query is made when using this route.

**How**\
When using the /activity route, you can grab the data and utilize a couple of parameters that help reduce and filter data. For example, you can make the following API call to retrieve Agreed Activity events that were created after or equal to the specified date:\
`https://api.pactsafe.com/v1.1/activity?filter=event_type==agreed and created_time>=2020-10-14&no_count=true&lean=true`

Additionally, a no\_count parameter that is equal to true and a lean parameter equal to true is used to reduce overhead and overall payload size.
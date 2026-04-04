# Source: https://docs.xano.com/xano-features/metadata-api/request-history.md

# Source: https://docs.xano.com/maintenance-monitoring-and-logging/request-history.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Request History

## API Request History

From the dashboard, easily view the high-level statistics of the API request history from your entire Workspace. You can toggle between your database and top API requests to see which of your API endpoints are being hit the most. To the right, visualize your API request history with a graph displaying the statistics of the past 24 hours. Select 'View Request Details' to see a detailed view and history of each API call made in your Workspace.

You can expand each individual call to review detailed information including inputs, response and request headers, and the output. You can even drill-down on a per-user basis to see the activity of each user in your application. Furthermore, you can view failed API calls here in order to help debug what went wrong. Finally, you can use these details to understand Webhook payloads to make it easier to build API endpoints that receive Webhooks.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/Qia2QBMIuWWrGb-s/images/211b85b8-image.jpeg?fit=max&auto=format&n=Qia2QBMIuWWrGb-s&q=85&s=6f0ba10a165f0df28d4e44aeec686da8" width="800" height="511" data-path="images/211b85b8-image.jpeg" />
</Frame>

You can also choose whether to see the request history for the specific branch you have active, or all branches, and download your request history as a CSV. If you would like to access your request history via API, you can do so using our [Metadata API](/xano-features/metadata-api).

The Request History panel allows you to filter by the following metrics:

* **Time** - when the request was received

* **Duration** - how long the request took

* **Status** - if there was a standard code returned, filter by that status

* **Input / Output Size** - how much data was sent to or sent from the request

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/Qia2QBMIuWWrGb-s/images/1f4f6775-image.jpeg?fit=max&auto=format&n=Qia2QBMIuWWrGb-s&q=85&s=083731879dfb4ac632c9b34fbb674ebe" width="666" height="1202" data-path="images/1f4f6775-image.jpeg" />
</Frame>

API and Custom Function request history panels will also show the average runtime of all of your requests, giving you quick visibility into the state of your application.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/dC3SQWgPCF_-1qn6/images/26e7c8a1-image.jpeg?fit=max&auto=format&n=dC3SQWgPCF_-1qn6&q=85&s=3a2345135eaee449154f2c2c5fedfc66" width="394" height="340" data-path="images/26e7c8a1-image.jpeg" />
</Frame>

It doesn't stop at the entire Workspace level. From each API group, you can see the detailed history of the entire group. And from each API endpoint, you can see the history of the individual endpoint.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/pz6e9Ndbn8i3u8Zz/images/6a261296-image.jpeg?fit=max&auto=format&n=pz6e9Ndbn8i3u8Zz&q=85&s=8ddda00553775e0bf9fd65bdcc7d6c7b" width="800" height="513" data-path="images/6a261296-image.jpeg" />
</Frame>

## Activate Debugger from Request History

When viewing request history **from a specific API endpoint** (not the dashboard-level view), you can click **Activate Debugger** on any request entry. This will re-execute the request and open the [debugger](/testing-debugging/testing-and-debugging-function-stacks#using-the-debugger), allowing you to step through the entire execution one step at a time.

This is especially useful for investigating issues reported in production, as you can quickly replay the exact request that caused a problem and inspect each step of the function stack.

<Warning>
  Activating the debugger will **re-execute the request against live data**. Depending on the logic in your endpoint, this could have unintended side effects such as creating duplicate records, sending emails, processing payments, or modifying data. Use caution before activating the debugger on requests that perform write operations or trigger external services.
</Warning>

<Info>
  This feature is only available when viewing request history from a specific API endpoint. It is not available from the dashboard-level request history view.
</Info>

## Function Request History

[Custom Functions](/the-function-stack/functions/custom-functions) are similar to API endpoints in Xano, in the sense that they have the same No-Code API builder UI. However, custom functions can only be called by other internal function stacks in Xano whether that's an API, other function, or background task.

Functions also have a request history for any time a function is part of a live API request.

First, open the request history of a function from the top right menu icon.

<Frame caption="Open request history for a function">
  <img src="https://mintcdn.com/xano-997cb9ee/dC3SQWgPCF_-1qn6/images/2be7f7f2-image.jpeg?fit=max&auto=format&n=dC3SQWgPCF_-1qn6&q=85&s=7648d74ba492f513857d25c1c64be72e" width="706" height="541" data-path="images/2be7f7f2-image.jpeg" />
</Frame>

Once opened, you can see all the requests from the past 24 hours.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/dyVYERTquSXdpw_-/images/9d3dd39f-image.jpeg?fit=max&auto=format&n=dyVYERTquSXdpw_-&q=85&s=0e4587d2fdbdaedf388b3126d547a0ed" width="402" height="826" data-path="images/9d3dd39f-image.jpeg" />
</Frame>

At the top, you can filter the requests by the time they occurred up until and by the duration of the how long the function took to run.

<Info>
  The duration filter can be useful for identifying potential performance issues.
</Info>

You can click on any of the requests to see the specific details of the inputs, output (response), and the function stack run time information.

<Frame caption="Granular information on the function request.">
  <img src="https://mintcdn.com/xano-997cb9ee/dyVYERTquSXdpw_-/images/9ae54071-image.jpeg?fit=max&auto=format&n=dyVYERTquSXdpw_-&q=85&s=76a48b31463e8d5cb96f74867db0c8a7" width="399" height="775" data-path="images/9ae54071-image.jpeg" />
</Frame>

### Task History

Task history behaves a little differently than APIs and functions. Tasks maintain a history over 7 days instead of 24 hours. Tasks also do not deliver responses, so no response data will be recorded, but you will still be able to review the statement log, execution status, and the timing details.

### Middleware History

Middleware history will behave the same as API and function history.

### Triggers History

Request history for triggers behaves most similar to a task, as there is no output returned with a trigger. You can, however, review the inputs (new, old, action, datasource) and the timing details for each step.

## Managing Request History

## Branch Defaults

> These are default settings related to what is logged in your [Request History](/maintenance-monitoring-and-logging/request-history)

In your workspace settings, you can manage the request history for your entire workspace in the Branch Defaults panel.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/dyVYERTquSXdpw_-/images/9c38d0ca-image.jpeg?fit=max&auto=format&n=dyVYERTquSXdpw_-&q=85&s=b636196c618692d996a05b0ae63260c6" width="831" height="848" data-path="images/9c38d0ca-image.jpeg" />
</Frame>

From this panel, we can define the request history defaults for each object type (query, function, task, middleware, trigger) that maintains history.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/dC3SQWgPCF_-1qn6/images/2a57b449-image.jpeg?fit=max&auto=format&n=dC3SQWgPCF_-1qn6&q=85&s=8d412eb62a28858ea471805170fa5715" width="397" height="596" data-path="images/2a57b449-image.jpeg" />
</Frame>

* **Enable / Disable** - Performs the selected action on the object type

* **Function Statement Limit** - The number of statements to record for each object type. You can choose between:

  * No statements

  * 100 statements

  * 1,000 statements

  * 10,000 statements

  * Store all statements

<Warning>
  Please note that request history utilizes your Database (SSD) storage. It is important to consider this when determining how many statements can be stored, or if they need to be stored at all.
</Warning>

#### Inheriting Settings

In each individual API, function, task, middleware, or trigger's settings, you can also control the request history for that object specifically.

By default, these will be set to **inherit**, which means it will obey the branch defaults. Otherwise, you can adjust this for specific objects as necessary.

## Clearing Request History

From your Instance settings, you have the option to manually clear your request history at any time.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/o7zunZFYmjx8RZ8N/images/f81a8291-image.jpeg?fit=max&auto=format&n=o7zunZFYmjx8RZ8N&q=85&s=8847d2fe11b0db9ea5468706888f2243" width="2304" height="1192" data-path="images/f81a8291-image.jpeg" />
</Frame>

From this panel, we have two options: **database storage** and **cache storage**.

### Database Storage for Request History

This is the actual database table that contains all of your request history, and counts against your available database storage in your instance. You can click on this option to delete one portion or all of your request history at any time.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/_oKnuVg5Nf4VhJM4/images/489aca5c-image.jpeg?fit=max&auto=format&n=_oKnuVg5Nf4VhJM4&q=85&s=64fa9a0f5b4dfd3d102e9d13029a273c" width="665" height="869" data-path="images/489aca5c-image.jpeg" />
</Frame>

Use the **Force** option to halt any running processes to ensure the data can be cleared -- please note however that this may result in a little bit of downtime as the server halts running processes.

### Cache Storage for Request History

As requests are logged, they are not immediately saved to the database. For a short period of time, they are held in a cache, and dumped into the database at fast, regular intervals. In some cases, such as during excessive traffic spikes, you may find that clearing the request cache before the items are added to the database can help the recovery process.

Please note that when items are cleared from the cache, they will not be logged in the history database.


Built with [Mintlify](https://mintlify.com).
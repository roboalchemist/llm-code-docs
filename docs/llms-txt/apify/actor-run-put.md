# Source: https://docs.apify.com/api/v2/actor-run-put.md

# Update run


```
PUT 
https://api.apify.com/v2/actor-runs/:runId
```


This endpoint can be used to update both the run's status message and to configure its general resource access level.

**Status message:**

You can set a single status message on your run that will be displayed in the Apify Console UI. During an Actor run, you will typically do this in order to inform users of your Actor about the Actor's progress.

The request body must contain `runId` and `statusMessage` properties. The `isStatusMessageTerminal` property is optional and it indicates if the status message is the very last one. In the absence of a status message, the platform will try to substitute sensible defaults.

**General resource access:**

You can also update the run's general resource access setting, which determines who can view the run and its related data.

Allowed values:

* `FOLLOW_USER_SETTING` - The run inherits the general access setting from the account level.
* `ANYONE_WITH_ID_CAN_READ` - The run can be viewed anonymously by anyone who has its ID.
* `RESTRICTED` - Only users with explicit access to the resource can access the run.

When a run is accessible anonymously, all of the run's default storages and logs also become accessible anonymously.

## Request

## Responses

* 200
* 400

**Response Headers**



Bad request - invalid input parameters or request body.

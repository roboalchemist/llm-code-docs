# Source: https://docs.getint.io/getintio-platform/workflows/type-mapping.md

# Type Mapping

Type mapping maps items types between applications which almost in all cases operates on different items types. Thanks to type mapping you define what type of item should be created from another item type from another application. Item types are e.g. Bugs, Stories, Incidents, Service Requests.&#x20;

Every Type Mapping can be configured separately from other types mappings. This gives a flexibility when it comes to cover differences / corner cases for separate types. E.g. fields are pretty often different for each type, types has also different workflows (status transitions).

For every Type Mapping you can configure

* Fields
* Status transition
* Comments&#x20;
* Attachments
* Hierarchy

## Status transition

Status transition for type mapping can be configured on a **STATUS** tab. To make sure that status can be synced please map available statuses options between both apps (each app can use different statuses and thats why Getint requires mapped options to know what status to set when syncing item to the other app.

Once you map status options together they will appear on a list like below CANCELLED - DONE options are mapped together. You can click **trash** icon to delte a mapping or **cog** icon to configure transition fields.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FUB77X1YYyBTBflDtKJgm%2FScreenshot%202023-07-04%20at%2010.39.17.png?alt=media&#x26;token=9674622f-0ad3-4340-a3b1-4b1a08d29874" alt=""><figcaption></figcaption></figure>

### Transition fields

Some apps like Jira, ServiceNow and Azure DevOps requires transition fields to be set up. Transition fields are the fields which are provided when the status is being changed from A to B.&#x20;

For example, for Jira Resolution is mostly a transition field, so if Jira issue is moved from IN PROGRESS to DONE it still requires the resolution to be provided, which can be Fixed, Duplicate, Won't Do etc.&#x20;

In similar way it works for ServiceNow. ServiceNow in default requires Close Code and Close Notes to be provided when Ticket is moved to Closed or Resolved state.

**How to find out that transition fields are missing?**

If you see in run logs error message stating that there were some fields missing, like below, it can indicate that there was an error during status transition

```
Invalid response status code received (expected: 200 but got 403). Response: {"error":{"message":"Operation Failed","detail":"Data Policy Exception: \n\tThe following fields are mandatory: Resolution code, Close notes"},"status":"failure"}
```

**How to set Transition Fields?**

Please have a look at the short video below showing how to set Transition Fields when the&#x20;

![](https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MR6Z9V8zLATPQPOGSDf%2F-MeiEVVowlznM0m6_2m8%2F-MeiGlbw7qaomnoiRyWY%2Ftransition_fields.gif?alt=media\&token=4a878f4f-9f7b-4b32-a6f2-95b0189dd0a5)

{% file src="<https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MR6Z9V8zLATPQPOGSDf%2F-MeiEVVowlznM0m6_2m8%2F-MeiGdYY0GH5Xct-3ntS%2Ftransition_fields.mov?alt=media&token=bc7bd527-3ed3-4709-a0eb-468c2764d784>" %}

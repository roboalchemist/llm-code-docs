# Source: https://www.uptrends.com/support/kb/api/changelog/

Title: API changelog | Uptrends

URL Source: https://www.uptrends.com/support/kb/api/changelog/

Markdown Content:
Uptrends API will be improved and extended over time. We’ll be adding new endpoints and methods for new functionalities.

When adding a new functionality, our goal is always to stay backward-compatible. However, sometimes change is inevitable and a new version of the API may not be compatible with what you’ve coded and used so far. You should check the API changelog regularly to stay on top of all changes and to act on those changes when necessary.

If you are looking for the documentation of the API, please check out the articles in the [Uptrends API](https://www.uptrends.com/support/kb/api/api-overview/) category.

Also, if you are interested in the changes to the Uptrends app, check out the [general changelog](https://www.uptrends.com/changelog/).

March 2026
----------

### Manage RUM websites efficiently with the API

RUM websites can now be fully managed through the API. The `/RUM` endpoint has been extended to support creating, updating, and deleting RUM website configurations, in addition to retrieving them. For more information, refer to the [Uptrends API v4 RUM documentation](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/RUM).

September 2025
--------------

### Introducing the MonitorCheck endpoint for Postman API monitors

The `/MonitorCheck/{monitorCheckId}/PostmanAPI` endpoint has been added to provide detailed monitoring information for individual Postman API monitor checks. This returns key results, such as HTTP status code, assertion outcomes, total execution time, response components, and other information for each API step.

For more information, refer to the [Uptrends API v4 MonitorCheck documentation](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/MonitorCheck/MonitorCheck).

### Monitor API update: Support for predefined variables in Postman API monitors

The `/Monitor` endpoint now also returns the `PredefinedVariables` field for Postman API monitors. This field contains all the user-defined and collection variables associated with the monitor.

```
"PredefinedVariables": [
    {
      "Key": "baseUrl",
      "Value": "{{prodEnvironment}}"
    },
    {
      "Key": "testEnvironment",
      "Value": "https://test-galactic.resorts.com/"
    },
    {
      "Key": "prodEnvironment",
      "Value": "https://https://prod-galactic.resorts.com/"
    },
    {
      "Key": "secretkey",
      "Value": "{{@VaultItem.70454a43-ef64-4f6a-aee0-3779654f1a31.Password}}"
    }
  ]
```

For more information, refer to the [Postman API variables](https://www.uptrends.com/support/kb/synthetic-monitoring/api-monitoring/postman-monitoring/postman-api-monitoring-variables/) knowledge base article and the [Uptrends API v4 Monitor documentation](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/Monitor).

### Monitor API update: Support for the latest Edge and Chrome user agents

The `/Monitor` endpoint now supports `ChromeLatest` and `EdgeLatest` as user agent values for the latest Chrome and Edge versions. You can also use these values with the `/POST`, `/PUT`, and `/PATCH` methods.

August 2025
-----------

### Monitor API update: Deprecated fields

As of 27 August 2025, certain fields in the `/Monitor` endpoint were deprecated. To define error conditions and maintain compatibility with the Uptrends API, use the `Monitor.ErrorConditions` command.

May 2025
--------

### Upcoming breaking change: Deprecating API fields

As part of our ongoing efforts to optimize the Uptrends API, specific fields in the following [Monitor](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/Monitor) endpoints will be deprecated, effective **27 August 2025**:

*   `GET` and `POST``/Monitor`
*   `GET`, `PUT`, and `PATCH``/Monitor/{monitorGuid}`
*   `GET` and `POST``/Monitor/MonitorGroup/{monitorGroupGuid}`

The following deprecated fields will now be treated as [Error condition types](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-overview/) under the `ErrorConditions` array. Related fields will be merged into a single entry, replacing their previous usage as individual fields:

| Deprecated fields | Replacement fields |
| --- | --- |
| `AlertOnLoadTimeLimit1`, `LoadTimeLimit1` | [LoadTimeLimit1](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings/) |
| `AlertOnLoadTimeLimit2`, `LoadTimeLimit2` | [LoadTimeLimit2](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings/) |
| `AlertOnMaximumBytes`, `MaximumBytes` | [TotalMaxBytes](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources/#check-the-sum-of-all-resources-together-full-page-check) |
| `AlertOnMinimumBytes`, `MinimumBytes` | [TotalMinBytes](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources/#check-the-sum-of-all-resources-together-full-page-check) |
| `AlertOnMaximumSize`, `ElementMaximumSize` | [PageElementMaxSizeWithPercentage](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources/#check-each-resource-individually-full-page-check) |
| `AlertOnPercentageFail`, `FailedObjectPercentage` | [PageElementFailedWithPercentage](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources/#check-each-resource-individually-full-page-check) |
| `ExpectedHttpStatusCode`, `ExpectedHttpStatusCodeSpecified` | [HttpStatus](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-page-availability/) |

Below is an example of the updated API response. It is recommended that you adjust your API calls to use the `ErrorConditions` array. This aligns with the latest API structure and ensures correct API functionality.

```
{
  ...
  "ErrorConditions": [
    {
      "ErrorConditionType": "LoadTimeLimit1",
      "Value": "2500",
      "Effect": "Indicate"
    },
    {
      "ErrorConditionType": "LoadTimeLimit2",
      "Value": "5000",
      "Effect": "Error"
    },
    {
      "ErrorConditionType": "TotalMaxBytes",
      "Value": "5000000"
    },
    {
      "ErrorConditionType": "TotalMinBytes",
      "Value": "5000"
    },
    {
      "ErrorConditionType": "PageElementMaxSizeWithPercentage",
      "Value": "200000",
      "Percentage": "10"
    },
    {
      "ErrorConditionType": "PageElementFailedWithPercentage",
      "Percentage": "10"
    },
    { "ErrorConditionType": "HttpStatus",       
      "Value": "200"     
    }
  ],
 ...
}
```

### Private Checkpoint Health Update

The `GET /PrivateCheckpointHealth` endpoint now returns the `Warnings` field, which contains all warning information associated with the server’s checkpoint. To know more, refer to the [Uptrends API v4 Private location Checkpoint health documentation](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/PrivateLocation/PrivateLocation_GetSpecifiedPrivateCheckpointHealth).

April 2025
----------

### Introducing the Private locations API​

A new set of API endpoints has been added to help you manage your Private locations configuration, including health and checkpoint information. To know more, refer to the [Uptrends API v4 Private locations documentation](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json).

March 2025
----------

### Monitor Group API Update

The `/MonitorGroup` endpoint now returns the number of credits used per [monitor type](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-types/):

*   `UsedBasicMonitorQuota` — returns the number of credits used for [Uptime or Basic monitors](https://www.uptrends.com/support/kb/synthetic-monitoring/uptime-monitoring/uptime-monitoring-overview/).
*   `UsedBrowserMonitorQuota` — returns the number of credits used for [Browser or Full-Page Check (FPC) monitors](https://www.uptrends.com/support/kb/synthetic-monitoring/browser-monitoring/browser-monitoring-overview/).
*   `UsedTransactionMonitorQuota` — returns the number of credits used for [Transaction monitors](https://www.uptrends.com/support/kb/synthetic-monitoring/transactions/transactions-overview/).
*   `UsedApiMonitorQuota` — returns the number of credits used for [Multi-step API (MSA)](https://www.uptrends.com/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview/) and [Postman](https://www.uptrends.com/support/kb/synthetic-monitoring/api-monitoring/postman-monitoring/postman-api-monitoring/) monitors.

Previously, the MonitorGroup API only returned the total number of credits available to the group for each monitor category. Now, it also returns the number of credits in use in the group for each monitor category.

February 2025
-------------

### Cursor Parameter Value Update

The API Cursor parameter is a string value that works as a pointer to traverse data from the API response.

Cursors have now been updated to a longer string format to ensure safer data handling. All newly created cursors will now follow the new format, and the old formatted cursors will still continue to work until 1 April 2025. After that period, old cursors will no longer be available for use. It is recommended to generate new cursor values to keep them updated and working as expected.

Note that the Cursor parameter is available in the [Monitor Check API](https://www.uptrends.com/support/kb/api/monitorcheck-api/) and Alert API endpoints.

January 2025
------------

### Monitor API Update

The `/Monitor` endpoint now returns the `LastModifiedDate`, which contains the date and time the monitor was last updated. Previously, only the `CreatedDate` could be retrieved from the Monitor API.

November 2024
-------------

### VaultItem Update

The `POST/v4/VaultItem`, `PUT/v4/VaultItem/{vaultItemGuid}`, and `PATCH/v4/VaultItem/{vaultItemGuid}` now accept the `SecretEncodingMethod` field when updating or creating the [One-time password configuration](https://www.uptrends.com/support/kb/account/vault/#one-time-password) vault item. This new field accepts _Hex_ or _Base32_ as string values. The _Base32_ format is the default encoding method if the `SecretEncodingMethod` field is not specified.

September 2024
--------------

### VaultItem Update

The `GET /v4/VaultItem` now returns an additional data item, `VaultItemUsedBy`, which returns details about which items or monitors are using each vault item.

August 2024
-----------

### Checkpoint API

The API endpoint `/Checkpoint/Server/{serverId}` now also returns private location servers.

### VaultItem Update

The `GET /v4/VaultItem` endpoint is now able to return the same extent of details for each vault item, similar to how details are returned for a single item in a `GET /v4/VaultItem/{GUID}`.

June 2024
---------

### Breaking change: the /Register API for SSO-only operators

The Uptrends API requires [registration](https://www.uptrends.com/support/kb/api/authentication-v4/) before it can be used. Operators can create a set of API-specific credentials, based on their regular Uptrends credentials. There are two ways to register a set of API credentials:

*   Operators can make use of the regular Uptrends interface, and add an API user through the API management tab in their operator settings.
*   Alternatively, operators can register for credentials in the API itself, via a request `POST /Register` by supplying their regular Uptrends credentials.

As of this update, operators who can only [log in using Single sign-on (SSO)](https://www.uptrends.com/support/kb/account/settings/single-sign-on-overview/) can no longer attempt to make use of this second option for registering API credentials, since they do not have ‘regular’ Uptrends credentials to use.

In such cases, we recommend making a separate operator account, and using that to register for API credentials.

October 2023
------------

### Breaking change: page load metrics for browser-based monitoring

**Note:** the following is a **breaking change** to the _MonitorCheck_ API. The change will go live on **Wednesday, November 8th**.

The Uptrends [MonitorCheck API](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/MonitorCheck) can be used to retrieve detailed information about individual monitor checks. For browser-based monitoring, the [waterfall chart](https://www.uptrends.com/support/kb/synthetic-monitoring/monitoring-results/waterfall-chart/) can be retrieved via the `GET /MonitorCheck/{monitorCheckId}/Waterfall` call, which returns all the waterfall metrics, including [Core Web Vitals](https://www.uptrends.com/support/kb/synthetic-monitoring/monitoring-results/core-web-vitals/) and [W3C navigation timings](https://www.uptrends.com/support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings/), if they are present in the check result.

Currently, the MonitorCheck API returns Core Web Vitals and W3C navigation timings in two separate JSON objects: `PageLoadMetrics` and `W3CNavigationTiming`. Going forward, these separate objects will be combined into a single array, `PageLoadMetricsCollection` as follows:

```
"Attributes": {
    "PageLoadMetricsCollection": [
      {
        "CumulativeLayoutShift": 0.029,
        "FirstContentfulPaint": 2914,
        "LargestContentfulPaint": 3014,
        "TotalBlockingTime": 819,
        "TimeToInteractive": 12516,
        "TimeToFirstByte": 2068,
        "SendStart": 2059,
        "LoadEventEnd": 6721,
        "DomInteractive": 2652,
        "DomComplete": 6719
      }
    ],
    ...
  }
```

### Specifying variables in alert definitions via the API

When configuring [alerting](https://www.uptrends.com/support/kb/alerting/) through a [custom integration](https://www.uptrends.com/support/kb/alerting/integrations/custom-integrations/) in Uptrends, operators can use the UI to specify certain required variables [in the escalation level of the alert definition](https://www.uptrends.com/support/kb/alerting/integrations/custom-integrations/building-the-right-message-content/#specifying-variables-per-escalation-level), instead of in the integration options. This allows users to use a single integration for various scenarios, such as sending alerts for different sets of monitors to different teams, but with the same message content.

When the option to specify variables in the escalation level is selected in the integration settings, the variables must instead be configured when the integration is set to be used in the settings of the alert definition. To do this, an extra text field appears in the integration selection list in the alert definition settings.

Until now, this option was unavailable when configuring alert definitions through the API. We’ve added a new option to the `/AlertDefinition/{alertDefinitionGuid}/EscalationLevel/{escalationLevelId}/Integration` request (where you configure which integrations are tied to each escalation level in the alert definition). The new property will be:

```
{
    ...
    "VariableValues": {
        "ApiUrl": "https://api.escalationlevel-specific-url.com/alerts"
    },
    ...
}
```

This property is the equivalent of this option in the application UI:

![Image 1: Configuring integration variable in alert definition](https://www.uptrends.com/img/content/scr-api-cl-conf-variables-in-escalation-level.min.png)

September 2023
--------------

### Change in checkpoint’s IPv6 addresses

Previously, when using the checkpoint API to retrieve checkpoint information, the checkpoint’s IPv4 addresses were displayed as a simple list in an array, while the IPv6 addresses (if applicable) were a list of objects. For example, the Amsterdam checkpoint IP addresses were previously listed as follows:

```
"Ipv4Addresses": [
        "178.217.84.4",
        "188.241.149.95",
        "66.212.22.2",
        "185.145.63.225",
        "5.182.210.227",
        "5.182.210.168"
    ],
    "IpV6Addresses": [
        {
            "IpAddress": "2a01:5cc0:1:2::4"
        },
        {
            "IpAddress": "2607:fcd0:cd40:1400::2"
        }
    ],
```

Uptrends has resolved this inconsistency now, and returns the IPv6 addresses in the same way:

```
"IpV6Addresses": [
        "2a01:5cc0:1:2::4",
        "2607:fcd0:cd40:1400::2",
    ],
```

Be aware that if you’ve automated the retrieval of checkpoint IP addresses, e.g. for whitelisting purposes, this may be a **breaking change**.

January 2023
------------

Version 3 of the API has reached its end of life as of January 2023, and has been disabled. You can still find [its documentation](https://www.uptrends.com/support/kb/api/api-overview/) in our knowledge base, but it will no longer work. If you have existing scripts or procedures in place that are still making use of version 3, these will fail, and we recommend you switch to version 4 as quickly as possible. See our [upgrade guide](https://www.uptrends.com/support/kb/api/api-overview/) for more information on switching from API version 3 to version 4.

**Update May 2023:** The documentation for version 3 of our API has been removed, and is no longer accessible.

December 2022
-------------

### Monitor creation date info through the API

The [/Monitor endpoint](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/Monitor) can be used to retrieve definitions of the monitors in your account (via _GET /Monitor/{monitorGuid}_), among other things. The response will now also include a `CreatedDate`, indicating when the monitor was created.

November 2022
-------------

### Small changes to /Register endpoint

As you may have read [in our regular changelog](https://www.uptrends.com/changelog/), this release we’ve added the option to [‘Create and revoke Uptrends API credentials via UI’](https://www.uptrends.com/changelog/#2022-11-manage-uptrends-api-credentials-via-ui). In order to align the Uptrends API v4 with the user interface, we have added 2 new options to the /Register endpoint:

*   It’s now possible to specify an optional description when registering a new API account by using the `description` field.
*   It’s now possible to create an API account for another operator when the calling operator has sufficient rights by using the `operatorGuid` field.

September 2022
--------------

### Upcoming change: timestamps in the API response

Currently, timestamps that are part of the response for any [API v4](https://www.uptrends.com/support/kb/api/api-overview/) call are being converted to JSON in one of two ways:

*   Millisecond count is equal to 0: _2022-09-21T13:08:47_
*   Millisecond count is not equal to 0: _2022-09-21T13:08:47**.682**_

This inconsistency can lead to problems when the data containing these timestamps is automatically parsed and handled. Because of this, we’re making a change: the millisecond count will no longer be shown for any timestamps included in the API response. Going forward, all timestamps will have the format _2022-09-21T13:08:47_.

June 2022
---------

### Upcoming checkpoint IP addresses

The Uptrends API can be used to retrieve checkpoint IP addresses, for automated whitelisting. Previously, responses to such requests to our [checkpoint API](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/Checkpoint) were typically an up-to-date list of current checkpoint IP addresses. However, Uptrends' checkpoint network is always in motion. New checkpoints are added, existing checkpoints are removed or relocated, or IP addresses are changed. That could mean that the list of IP addresses you were using to whitelist might fall behind until the next synchronization, leading to unnecessary errors.

We’re now registering upcoming checkpoint IP addresses and including them in the API response. That way your whitelist will be up to date ahead of time.

### Relationships in statistics API

Responses from the [Statistics API](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/Statistics) (which can be used to retrieve statistical data for your monitors or monitor groups) will now include some additional metadata about the response. The new `Relationships` array already exists for other API endpoints, and contains additional information about the request like a link to the Monitor or MonitorGroup API request to retrieve additional information about the monitor (group) itself.

```
"Relationships": [
            {
                "Id": "4c3a9529-7934-4978-9c36-c377b232g7hb",
                "Type": "Monitor",
                "Links": {
                    "Self": "/Monitor/4c3a9529-7934-4978-9c36-c377b232g7hb"
                }
            }  
        ]
```

May 2022
--------

### Fix for start/end parameters in statistics API

Our API supports retrieving statistical monitor data, with the [Statistics API](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/Statistics/Statistics_GetMonitorStatistics). You can specify either a preset period for which to retrieve the data (with available values such as `Last24Hours`), or set a custom period using start and end URL parameters. For example, `GET /Statistics/Monitor/{monitorGuid}?Start=2022-04-08&End=2022-04-09` retrieves statistical data for a single monitor, for the specified period.

There was an issue where the minute indicator in the start and end timestamps wasn’t being mapped correctly, which could have led to incomplete (or even empty) results in the API response. This issue has been resolved.

February 2022
-------------

### Update to status API

The [Status API](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/Status/Status_GetMonitorStatus) retrieves status information for a specific monitor, based on the most recent monitor check. This endpoint can be used for information regarding the current monitor status. We’ve expanded the response to now also include a value for `TotalTime` - information about the [total time metric](https://www.uptrends.com/support/kb/dashboards-and-reporting/dashboards/explanation-total-time-metrics/) for the most recent monitor check.

January 2022
------------

### Returning the correct monitor data

When a non-Administrator operator with [the **View data** permission](https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-settings/monitor-permissions/) on a certain monitor retrieved that monitor definition through the API (via `GET /Monitor/{monitorGuid}`), the response did not include all relevant data. That was incorrect, since the same data was already available through the UI but not the API, and has been rectified. Now, when these operators retrieve a monitor, the response will include values for _MonitorGuid_, _Name_, _MonitorType_, _MonitorMode_, _IsActive_, and _GenerateAlert_.

August 2021
-----------

### Announcement: deprecation of version 3 of our API

The [Uptrends API](https://www.uptrends.com/support/kb/api/api-overview/) currently supports two versions side-by-side. Version 3 is the older legacy version of our API, and version 4 is the currently recommended version. With a much more complete set of features, version 4 has been the focus of our development for some time. As such, we’ve decided to deprecate version 3 of our API, and it will be retired and become unavailable by **December 2022**.

For customers currently still making active use of version 3 of our API, it should be noted that it will still be supported up until that time. However, we do recommend switching over to making use of version 4 as soon as possible. To assist you in this, we’ve written an [API v3 to v4 upgrade guide](https://www.uptrends.com/support/kb/api/api-overview/), which will cover the key differences between the two API versions and how to bridge them in your scripts and software.

July 2021
---------

The Uptrends API allows you to manage [permissions for operators and operator groups](https://www.uptrends.com/support/kb/account/users/operators/permissions/), assigning roles such as **Administrator**, **Financial operator**, or allowing **Infra access**. The [OperatorGroup API](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/OperatorGroup) contains several options for retrieving, adding or deleting such permissions.

We have changed the way in which the permissions are specified for operator groups in the API, which could affect any automated creation, removal, or retrieval of information about operator group permissions you may have set up. Currently, retrieving information about permissions works by requesting:

`GET /OperatorGroup/{operatorGroupGuid}/Authorization`

which returns a response along the following lines (depending on which permissions have been set up for that particular operator group):

```
[
      {
        "AuthorizationId": "{authIdGuid1}",
        "AuthorizationType": "FinancialOperator",
        "OperatorGroupGuid": "{operatorGroupGuid}"
    },
    {
        "AuthorizationId": "{authIdGuid2}",
        "AuthorizationType": "AllowInfra",
        "OperatorGroupGuid": "{operatorGroupGuid}"
    },
    ...
]
```

Going forward, that same request will have its response simplified, simply listing the permissions granted and no other information. The response will no longer contain an `operatorGroupGuid` or `AuthorizationId` (the latter will disappear completely, meaning permissions will no longer have an individual GUID assigned to them). It will look like this:

```
{
    "FinancialOperator",
    "AllowInfra",
    ...
}
```

Adding a new operator group permission currently works by sending a POST request to:

`/OperatorGroup/{operatorGroupGuid}/Authorization` with a request body specifying an “AuthorizationType”. The currently available values for AuthorizationType for operator groups is available in the [Uptrends API Swagger UI](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/), under **Models** (at the bottom), and then **OperatorGroupAuthorizationType**.

Going forward, new permissions can be added to an operator group by sending a POST request to:

`/OperatorGroup/{operatorGroupGuid}/Authorization/{authorizationType}` without including a request body.

Deleting a permission from an operator group is currently done by sending a DELETE request to `/OperatorGroup/{operatorGroupGuid}/Authorization/{authorizationGuid}` - but as noted above, “authorizationGuid” will disappear entirely as an entity and can no longer be used. Instead, you can delete permissions by referring to them directly by name in the request URL: `/OperatorGroup/{operatorGroupGuid}/Authorization/{authorizationType}`

February 2021
-------------

### Breaking change: sensitive values in multi-step API monitors

Our [multi-step API monitor type](https://www.uptrends.com/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview/) allows you to execute multiple consecutive HTTP requests, where each new request uses one or more pieces of data retrieved from a previous request to perform its task. Often, one of the steps will involve submitting credentials to gain access to a particular resource. In the past, these credentials would be added as predefined variables to the monitor definition, and then marked as _Sensitive_.

To improve the security of how we handle such credentials, we’re going to be moving away from that setup. Instead, the credentials will be placed in the [vault](https://www.uptrends.com/support/kb/account/vault/). With that change, the option to mark predefined variables as sensitive in multi-step API monitors becomes obsolete, and we will be removing it.

This will affect the way in which you can create or interact with multi-step API monitors through our API. Currently, the monitor definition for this monitor type will contain an array “PredefinedVariables”, where each of the individual variables has a true/false boolean “Sensitive”. In the near future, this boolean will be removed from the definition. If you wish to create or update an existing multi-step API monitor in your account through the Uptrends API, this field must no longer be included.

### Change: renamed routing

For Uptrends APIv4 we have an inconsistent way of naming routes. In most cases singular is used, but plural on a few occasions. The route now contains only singular parts, e.g. `/MonitorGroup/{monitorGroupGuid}/Member` instead of `/MonitorGroup/{monitorGroupGuid}/Members`.

We still support the old routes for backwards compatibility.

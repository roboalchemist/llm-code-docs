# Source: https://virustotal.readme.io/docs/quota-consumption.md

# Understanding Consumption

<style>
.tbd {
  background-color: lightgray;
}
table {
  width: 100%;
  padding: 5px 2px 11px 4px;
  font-size: 12px;
  vertical-align: top;
}
table td:first-child {
  max-width: 133px;
}
table td:nth-child(2) {
  max-width: 183px;
  text-align: center;
}
table td:nth-child(3) {
  max-width: 220px;
  text-align: center;
}
table td:nth-child(4) {
  max-width: 100px;
  text-align: center;
}
table td:nth-child(5) {
  max-width: 100px;
  text-align: center;
}
table td:nth-child(6) {
  max-width: 100px;
  text-align: center;
}
</style>

Here you can find how we measure consumption depending on each one of our services.

> ⚠️
>
> Group quota is shared between all group members. This means that for premium services, each individual user consumption is subtracted from the group quota. Therefore, it will be reflected in both the user and their group consumptions.

Summary table:

|                                 |                                        |                                  |              |               |                    |
| ------------------------------- | -------------------------------------- | -------------------------------- | ------------ | ------------- | ------------------ |
| **SERVICE / QUOTA CONSUMPTION** | **Searches / Downloads**               | **API requests**                 | **Livehunt** | **Retrohunt** | **Private Graphs** |
| [VTAPI](#vtapi)                 | When VTI available but not Premium API | X                                |              |               |                    |
| [VTI](#vti)                     | X                                      |                                  |              |               |                    |
| [Livehunt](#livehunt)           |                                        | If using Livehunt API endpoints  | X            |               |                    |
| [Retrohunt](#retrohunt)         |                                        | If using Retrohunt API endpoints |              | X             |                    |
| [Graph](#vtgraph)               |                                        | When loading public graphs       |              |               | X                  |

# VTAPI

*\*Minute, daily and monthly limitations. E.g. requests/day*

![Quota consumption API details](https://storage.googleapis.com/vtdocresources/guides/account-management/quotaconsumption_api_20231113.png)

## API v2

***

*\***API version 3 is now the default and encouraged way to programmatically interact with VirusTotal.** While older API endpoints are still available and will not be deprecated, we encourage you to migrate your workloads to this new version.*

Usually one API call consumes **one request** from your quota. However, there are some **exceptions**:

* **Multihash searches:** You can make a request to /vtapi/v2/file/report, that admits a list of hashes as a parameter. This way you will save time, but it will count as one request per hash in the list.
* **Information about file uploads:** Our /vtapi/v2/file/submissions endpoint lets you obtain information about uploads for one or more files. It will count as one request per each submission returned for each one of the files. This means that if file1.txt has been uploaded to VT 4 times and file2.txt has been uploaded to VT 6 times, you will consume 10 requests from your group quota.
* **New file uploads:** If you upload a new file to VirusTotal via /file/scan it won't consume from your quota. This means that you can freely upload **new files not found in VirusTotal** without consuming from your API quota. Notice that after uploading those files you usually would want to check the file analysis via /file/report, and doing this does consume from your quota.

[Link to our APIv2 documentation](/v2.0/reference/getting-started)

## API v3

***

Usually one API call consumes **one request** from your quota. However, there are some **exceptions**:

* **Enterprise searches (only for users with VTI and without VTAPI):** If you have Intelligence quota and you don't have premium API, the requests to VTI premium endpoints ("VT Enterprise Endpoints" section) are taken from your VTI quota. If you have VTAPI, these searches will consume quota from your API limits, as usual
* **Checking consumption and quota details:** For example using /users/{id}/overall\_quotas and /users/{id}/api\_usage endpoints for checking your API quotas and usage. No quota consumption.
* \*\*Feeds:\*\*No quota consumption for feeds endpoints. This includes file downloads using links provided by feeds endpoints.
* \*\*Invalid analysis requests:\*\*Analysis are retrieved via "/api/v3/analyses/{id}". Quota is not consumed for this endpoint if the {id} is invalid.
* **File uploading**: If a user uploads a new file that is not in VirusTotal, then no API quota will be consumed. Further calls to retrieve this file's data (`GET /files/{sha256}`) or its analyses (`GET /files/analyses/{id}`) won't consume quota either. Note that re-scanning the file (`POST /files/{sha256}/analyse`) will consume quota as any other API call.

[Link to our APIv3 documentation](https://virustotal.readme.io/reference/overview)

# VTI

*\*Monthly limitation. E.g. downloads/month*

![Quota consumption VTI details](https://storage.googleapis.com/vtdocresources/guides/account-management/quotaconsumption_vti_20231113.png)

VTI Quota can be consumed in 2 ways:

1. Via **website** (multihash search or not). A direct search, pivoting to another search or if you use pagination. This consumes only 1 search from Intelligence.
2. Via **APIv3**. If you don't have premium VTAPI but you have premium VTI it consumes 1 search/request from Intelligence. If you use the cursor to iterate over the results, it also consumes 1 req/request.

> ⚠️
>
> If you use VT Enterprise via API with our VT Enterprise endpoints, quota will be consumed from Premium API (if purchased) or from VT Enterprise (if no API purchased)

# VTHunting

*\*Monthly limitation. E.g. rules/month*

![Quota consumption VTHunting details](https://storage.googleapis.com/vtdocresources/guides/account-management/quotaconsumption_vthunting_20231113.png)

## Livehunt

***

Each YARA **rule** you create consumes **1 rule** from your quota, except for inactive rulesets. This means that if you have 3 rules in 1 active ruleset, you consume 3 YARA rules.

## Retrohunt

***

Each retrohunt **job** you create consumes **1 job** from your quota, no exceptions. This means that it doesn't matter if your job was successful or not or whether it had matches or not.

# VTGraph

*\*Monthly limitation. Private graphs/month*

![Quota consumption Graph details](https://storage.googleapis.com/vtdocresources/guides/account-management/quotaconsumption_graph_20231113.png)

## Private

***

VTGraph service only consumes from graph quota when creating **private graphs**.

If you create a private graph, it will consume 1 graph from your quota. No other consumption will be applied.

## Public

***

However, if you create a **public** graph, it will consume from your **API** **quota** as per the requests to the API that have been necessary in order to load all items in the graph. The more items you try to load, the more requests to API and therefore the more API quota consumption.
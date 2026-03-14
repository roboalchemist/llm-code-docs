# Source: https://docs.airbyte.com/integrations/sources/track-pms.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-track-pms/latest/icon.svg)

# Track PMS

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [4.3.1](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-track-pms)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-track-pms)(last updated 3 months ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `aa0373c1-a7a6-48ff-8277-e5fe6cecff75`

An Airbyte source for the Track Property Management System (PMS)<br /><!-- -->Enterprise-class property management solutions for vacation rental companies

Website: <https://tnsinc.com/><br /><!-- -->API Docs: <https://developer.trackhs.com><br /><!-- -->Authentication Docs: <https://developer.trackhs.com/docs/authentication#authentication>

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

To use this connector, you need API credentials from your Track PMS account. Contact your Track PMS administrator or Track support to obtain your API key and secret. For more information, see the [Track authentication documentation](https://developer.trackhs.com/docs/authentication#authentication).

## Configuration[​](#configuration "Direct link to Configuration")

| Input             | Type     | Description                                                                                                                                             | Default Value |
| ----------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `customer_domain` | `string` | Your Track PMS domain. Enter the domain only, without `https://` or trailing paths. For example: `api.trackhs.com` or your customer-specific subdomain. |               |
| `api_key`         | `string` | Your Track API key, used as the username for authentication.                                                                                            |               |
| `api_secret`      | `string` | Your Track API secret, used as the password for authentication.                                                                                         |               |

The connector uses HTTP Basic authentication, sending `api_key` as the username and `api_secret` as the password. If authentication fails, verify that you have provided both values correctly.

## Sync behavior[​](#sync-behavior "Direct link to Sync behavior")

The connector handles Track's API rate limit of 10,000 requests per 5 minutes. When the rate limit is reached, the connector waits approximately 5 minutes before retrying.

## Streams[​](#streams "Direct link to Streams")

| Stream Name                          | Primary Key               | Pagination         | Supports Full Sync | Supports Incremental | API Docs                                                                                    |
| ------------------------------------ | ------------------------- | ------------------ | ------------------ | -------------------- | ------------------------------------------------------------------------------------------- |
| accounting\_accounts                 | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getledgeraccounts)                           |
| accounting\_bills                    | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getbillscollection)                          |
| accounting\_charges                  | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getaccountingchargescollection)              |
| accounting\_deposits                 | id                        | DefaultPaginator   | ✅                 | ❌                   | Undocumented                                                                                |
| accounting\_deposits\_payments       | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getdepositpayments)                          |
| accounting\_items                    | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getitemscollection)                          |
| accounting\_transactions             | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getowneridtransactionscollection)            |
| booking\_fees                        | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getbookingfees)                              |
| charges                              | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getchargescollection)                        |
| companies                            | id                        | DefaultPaginator   | ✅                 | ✅                   | [Link](https://developer.trackhs.com/reference/getcompanies)                                |
| contacts                             | id                        | DefaultPaginator   | ✅                 | ✅                   | [Link](https://developer.trackhs.com/reference/getcontacts)                                 |
| contacts\_companies                  | contactId.companyId       | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getcontactcompanies)                         |
| contacts\_pii\_redacted              | id                        | DefaultPaginator   | ✅                 | ✅                   | [Link](https://developer.trackhs.com/reference/getcontacts)                                 |
| contracts                            | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getownercontractcollection)                  |
| crm\_company\_attachment             | company\_id.id            | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getcompanyattachments)                       |
| crm\_tasks                           | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/gettasks)                                    |
| custom\_fields                       | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getcustomfields)                             |
| date\_groups                         | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getdategroupcollection)                      |
| documents                            | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getalldocuments)                             |
| folios                               | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getfolioscollection)                         |
| folios\_logs                         | folio\_id.id              | DefaultPaginator   | ✅                 | ❌                   | Undocumented                                                                                |
| folios\_rules                        | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getfoliorulescollection)                     |
| folios\_transactions                 | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getfolioidtransactionscollection)            |
| fractionals                          | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/get-pms-fractionals)                         |
| fractionals\_inventory               | fraction\_id.id           | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/get-pms-fractionals-fractionalid-invetories) |
| fractionals\_owners                  | fraction\_id.id           | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/get-pms-fractionals-owners)                  |
| groups                               | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getgroupscollection)                         |
| groups\_blocks                       | group\_id.id              | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getgroupblockmappingcollection)              |
| groups\_breakdown                    | group\_id                 | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getgroupbreakdown)                           |
| groups\_tags                         | group\_id.id              | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getgrouptagmappingcollection)                |
| housekeeping\_clean\_types           | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getcleantypes)                               |
| housekeeping\_task\_list             | id                        | DefaultPaginator   | ✅                 | ❌                   | Undocumented                                                                                |
| housekeeping\_work\_orders           | id                        | DefaultPaginator   | ✅                 | ✅                   | [Link](https://developer.trackhs.com/reference/getworkorders)                               |
| lodging\_types                       | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getlodgingtypescollection)                   |
| maintenance\_problems                | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getmaintenanceproblemscollection)            |
| maintenance\_work\_orders            | id                        | DefaultPaginator   | ✅                 | ✅                   | [Link](https://developer.trackhs.com/reference/getmaintworkorders)                          |
| nodes                                | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getnodes)                                    |
| nodes\_types                         | id                        | DefaultPaginator   | ✅                 | ❌                   | Undocumented                                                                                |
| owners                               | id                        | DefaultPaginator   | ✅                 | ✅                   | [Link](https://developer.trackhs.com/reference/getownercollection)                          |
| owners\_contracts                    | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getownercontractcollection)                  |
| owners\_pii\_redacted                | id                        | DefaultPaginator   | ✅                 | ✅                   | [Link](https://developer.trackhs.com/reference/getownercollection)                          |
| owners\_statements                   | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/get-pms-statements)                          |
| owners\_statements\_transactions     | statement\_id.id          | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getstatementtransactionscollection)          |
| owners\_units                        | ownerId.id                | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getownerunitscollection)                     |
| promo\_codes                         | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getpromocodesv2)                             |
| quotes                               | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getquotescollectionv2)                       |
| rate\_types                          | id                        | DefaultPaginator   | ✅                 | ❌                   | Undocumented                                                                                |
| reservations                         | id                        | Elastic Search PIT | ✅                 | ✅                   | [Link](https://developer.trackhs.com/reference/getreservations)                             |
| reservations\_cancellation\_policies | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getcancellationpolicies)                     |
| reservations\_cancellation\_reasons  | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getcancellationreasons)                      |
| reservations\_discount\_reasons      | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getdiscountreasons)                          |
| reservations\_guarantee\_policies    | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/get-pms-reservations-policies-guaranties)    |
| reservations\_types                  | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getreservationtypes)                         |
| reservations\_v2                     | id                        | Elastic Search PIT | ✅                 | ✅                   | [Link](https://developer.trackhs.com/reference/getreservations-1)                           |
| reviews                              | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getreviewscollection)                        |
| roles                                | id                        | DefaultPaginator   | ✅                 | ❌                   | Undocumented                                                                                |
| suspend\_code\_reasons               | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getsuspendcodereasons)                       |
| tags                                 | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/gettagscollection)                           |
| tax\_districts                       | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/gettaxdistrictscollection)                   |
| tax\_policies                        | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/gettaxpolicycollection)                      |
| taxes                                | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/gettaxcollection)                            |
| travel\_insurance\_products          | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/gettravelinsuranceproducts)                  |
| units                                | id                        | DefaultPaginator   | ✅                 | ✅                   | [Link](https://developer.trackhs.com/reference/getchannelunits)                             |
| units\_amenities                     | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getunitamenities)                            |
| units\_amenity\_groups               | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getunitamenitygroups)                        |
| units\_bed\_types                    | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getbedtypescollection)                       |
| units\_blocks                        | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getunitblockscollection)                     |
| units\_channel                       | unit\_id.id               | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getunitchannelunitcollection)                |
| units\_daily\_pricing\_v2            | unit\_id.rateTypeId       | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getv2unitdailypricing)                       |
| units\_daily\_pricing\_parent        | id                        | DefaultPaginator   | ✅                 | ✅                   | [Link](https://developer.trackhs.com/reference/getchannelunits)                             |
| units\_taxes                         | unit\_id.id               | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getunitchanneltaxcollection)                 |
| units\_taxes\_parent                 | id                        | DefaultPaginator   | ✅                 | ✅                   | [Link](https://developer.trackhs.com/reference/getchannelunits)                             |
| units\_types                         | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getunittypes-2)                              |
| units\_types\_daily\_pricing\_v2     | unit\_type\_id.rateTypeId | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getv2unittypedailypricing)                   |
| units\_types\_daily\_pricing\_parent | id                        | DefaultPaginator   | ✅                 | ❌                   | [Link](https://developer.trackhs.com/reference/getunittypes-2)                              |
| users                                | id                        | DefaultPaginator   | ✅                 | ❌                   | Undocumented                                                                                |
| users\_pii\_redacted                 | id                        | DefaultPaginator   | ✅                 | ❌                   | Undocumented                                                                                |

## Reference[​](#reference "Direct link to Reference")

### Config fields reference

Field

Type

Property name

API Key

required

string

api\_key

Customer Domain

required

string

customer\_domain

API Secret

string

api\_secret

## Changelog[​](#changelog "Direct link to Changelog")

Expand to review

| Version | Date       | Subject                                                                                                       |
| ------- | ---------- | ------------------------------------------------------------------------------------------------------------- |
| 4.3.1   | 2025-11-30 | Fix travel insurance products record selector path                                                            |
| 4.3.0   | 2025-09-30 | Improve 404 err handling for units pricing, drop unneeded parent streams, rename units pricing parent streams |
| 4.2.0   | 2025-07-20 | Improved reservations & reservations\_v2 scroll index handling; add folios\_transactions stream               |
| 4.1.0   | 2025-06-30 | Fix error handler, add scroll parameter for reservations endpoints, add booking fees endpoint, schema updates |
| 4.0.0   | 2025-03-30 | Prune units schema; fix docs; update error handler; diable connector auto schema determination                |
| 3.0.0   | 2025-02-26 | Drop redundant streams & omit unneeded sensitive fields from accounting\_\* streams                           |
| 2.0.0   | 2025-02-13 | Rename and alphabetize folio\_id stream                                                                       |
| 1.0.0   | 2025-01-16 | Fix housekeeping\_work\_orders incremental field; add reservations endpoint                                   |
| 0.1.0   | 2025-01-16 | Move kebab case streams to snake case; alphabetize streams                                                    |
| 0.0.1   | 2024-10-18 | Initial release by [@blakeflei](https://github.com/blakeflei) via Connector Builder                           |

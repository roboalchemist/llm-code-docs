# Source: https://docs.datadoghq.com/api/latest/rate-limits

## [Rate Limits](https://docs.datadoghq.com/api/latest/rate-limits/#rate-limits)
Many API endpoints are rate limited. Once you exceed a certain number of requests in a specific period, Datadog returns an error.
If you are rate limited, you can see a 429 in the response code. You can either wait the designated time by the `X-RateLimit-Period` before making calls again, or switch to making calls at a frequency slightly longer than the `X-RateLimit-Limit` or `X-RateLimit-Period`.
Rate limits can be increased from the defaults by [contacting the Datadog support team](https://docs.datadoghq.com/help/).
Regarding the API rate limit policy:
  * Datadog **does not rate limit** on data point/metric submission (see [metrics section](https://docs.datadoghq.com/api/v1/metrics/) for more info on how the metric submission rate is handled). Limits encounter is dependent on the quantity of [custom metrics](https://docs.datadoghq.com/metrics/custom_metrics/) based on your agreement.
  * The API for sending logs is not rate limited.
  * The rate limit for event submission is `250,000` events per minute per organization.
  * The rate limits for endpoints vary and are included in the headers detailed below. These can be extended on demand.


The list above is not comprehensive of all rate limits on Datadog APIs. If you are experiencing rate limiting, reach out to [support](https://www.datadoghq.com/support/) for more information about the APIs you're using and their limits.
Rate Limit Headers | Description  
---|---  
`X-RateLimit-Limit` | number of requests allowed in a time period.  
`X-RateLimit-Period` | length of time in seconds for resets (calendar aligned).  
`X-RateLimit-Remaining` | number of allowed requests left in the current time period.  
`X-RateLimit-Reset` | time in seconds until next reset.  
`X-RateLimit-Name` | name of the rate limit for increase requests.  
### [Datadog API usage metrics](https://docs.datadoghq.com/api/latest/rate-limits/#datadog-api-usage-metrics)
All Datadog APIs have a usage limit for a given period of time. APIs can have unique, distinct rate limit buckets or be grouped together into a single bucket depending on the resource(s) being used. For example, the monitor status API has a rate limit that allows a human or automation script to query only so many times per minute. The endpoint rejects excess requests with a 429 response code and a hint to back off until a reset period has expired. API usage metrics allow Datadog users to self-service and audit API rate limit consumption for API endpoints (excluding metrics, logs, and event submission endpoints). These metrics provide a picture of allowed and blocked requests, and are provided with the following dimensions and available tags:
[Datadog API Rate Limit Usage Dashboard](https://app.datadoghq.com/dash/integration/31668/datadog-api-rate-limit-usage)
[Datadog API Rate Limit Usage Dashboard](https://app.datadoghq.eu/dash/integration/1386/datadog-api-rate-limit-usage)
[Datadog API Rate Limit Usage Dashboard](https://us3.datadoghq.com/dash/integration/2248/datadog-api-rate-limit-usage)
[Datadog API Rate Limit Usage Dashboard](https://us5.datadoghq.com/dash/integration/1421/datadog-api-rate-limit-usage)
[Datadog API Rate Limit Usage Dashboard](https://ap1.datadoghq.com/dash/integration/2698/datadog-api-rate-limit-usage)
[Datadog API Rate Limit Usage Dashboard](https://app.ddog-gov.com/dash/integration/1330/datadog-api-rate-limit-usage)
#### [Available metrics](https://docs.datadoghq.com/api/latest/rate-limits/#available-metrics)
Dimension | Usage metric | Description | Available Tags  
---|---|---|---  
**Org** | `datadog.apis.usage.per_org` | The organization-wide rate limit of the number of API requests made to a specific endpoint | 
  * `app_key_id`
  * `child_org` (on parent only)
  * `limit_count`
  * `limit_name`
  * `limit_period`
  * `rate_limit_status`
  * `user_uuid`

  
`datadog.apis.usage.per_org_ratio` | Ratio of API requests by available dimensions to total number of requests (`limit_count`) allowed. | 
  * `app_key_id`
  * `child_org` (on parent only)
  * `limit_count`
  * `limit_name`
  * `limit_period`
  * `rate_limit_status`
  * `user_uuid`

  
**User (UUID)** | `datadog.apis.usage.per_user` | Number of API requests made for a specific API endpoint that is rate limited per unique user. | 
  * `app_key_id`
  * `child_org` (on parent only)
  * `limit_count`
  * `limit_name`
  * `limit_period`
  * `rate_limit_status`
  * `user_uuid`

  
`datadog.apis.usage.per_user_ratio` | Ratio of API requests by available dimensions to total number of requests (`limit_count`) allowed. | 
  * `app_key_id`  

  * `child_org` (on parent only)
  * `limit_count`  

  * `limit_name`  

  * `limit_period`  

  * `rate_limit_status`  

  * `user_uuid`

  
**API Key** | `datadog.apis.usage.per_api_key` | Number of API requests made for a specific API endpoint that is rate limited per unique API Key used | 
  * `app_key_id`
  * `child_org` (on parent only)
  * `limit_count`
  * `limit_name`
  * `limit_period`
  * `rate_limit_status`
  * `user_uuid`

  
`datadog.apis.usage.per_api_key_ratio` | Ratio of API requests by available dimensions to total number of requests (`limit_count`) allowed. | 
  * `app_key_id`
  * `child_org` (on parent only)
  * `limit_count`
  * `limit_name`
  * `limit_period`
  * `rate_limit_status`
  * `user_uuid`

  
#### [Tag key](https://docs.datadoghq.com/api/latest/rate-limits/#tag-key)
Tag name | Description  
---|---  
`app_key_id` | Application Key ID used by API client. This can be `N/A` for web or mobile users and open endpoints.  
`child_org` | Name of child org, if viewing from the parent org. Otherwise, set to `N/A`. This only applies within the same datacenter.  
`limit_count` | Number of requests available to each rate limit name during a request period.  
`limit_name` | Name of rate limit. Different endpoints can share the same name.  
`limit_period` | Time in seconds for each rate limit name before the consumption count is reset.  
`rate_limit_status` |  `passed`: Request was not blocked.  
`blocked`: Request was blocked due to rate limits breached.  
`user_uuid` | UUID of user for API consumption.  
#### [Rollup in widgets](https://docs.datadoghq.com/api/latest/rate-limits/#rollup-in-widgets)
Metric visualizations should generally be rolled up to the minute using sum(60s) to aggregate the total number of requests per minute.
Ratio metrics are already normalized to the corresponding `limit_period`.
##### [Example use cases](https://docs.datadoghq.com/api/latest/rate-limits/#example-use-cases) 

Requests by rate limit name
    Graph the sum of `datadog.apis.usage.per_org`, `datadog.apis.usage.per_user`, and `datadog.apis.usage.per_api_key` by `limit_name`  
  
**Example:** `default_zero(sum:datadog.apis.usage.per_org{*} by {limit_name}) + default_zero(sum:datadog.apis.usage.per_user{*} by {limit_name}) + default_zero(sum:datadog.apis.usage.per_api_key{*} by {limit_name})` 

Blocked by rate limit name
    Graph the sum of `datadog.apis.usage.per_org`, `datadog.apis.usage.per_user`, and `datadog.apis.usage.per_api_key` by `limit_name` with `rate_limit_status:blocked`  
  
**Example:** `default_zero(sum:datadog.apis.usage.per_org{rate_limit_status:blocked} by {limit_name}) + default_zero(sum:datadog.apis.usage.per_user{rate_limit_status:blocked} by {limit_name}) + default_zero(sum:datadog.apis.usage.per_api_key{rate_limit_status:blocked} by {limit_name})` 

Blocked endpoint by user
    Graph the sum of `datadog.apis.usage.per_org`, `datadog.apis.usage.per_user`, and `datadog.apis.usage.per_api_key` by `user_uuid` with `rate_limit_status:blocked` and `limit_name:example`  
  
**Example:** `default_zero(sum:datadog.apis.usage.per_org{rate_limit_status:blocked,limit_name:example} by {user_uuid}) + default_zero(sum:datadog.apis.usage.per_user{rate_limit_status:blocked,limit_name:example} by {user_uuid}) + default_zero(sum:datadog.apis.usage.per_api_key{rate_limit_status:blocked,limit_name:example} by {user_uuid})` 

Blocked endpoint by app key ID
    Graph the sum of `datadog.apis.usage.per_org`, `datadog.apis.usage.per_user`, and `datadog.apis.usage.per_api_key` by `app_key_id` with `rate_limit_status:blocked` and `limit_name:example`  
  
**Example:** `default_zero(sum:datadog.apis.usage.per_org{rate_limit_status:blocked,limit_name:example} by {app_key_id}) + default_zero(sum:datadog.apis.usage.per_user{rate_limit_status:blocked,limit_name:example} by {app_key_id}) + default_zero(sum:datadog.apis.usage.per_api_key{rate_limit_status:blocked,limit_name:example} by {app_key_id})` 

Ratio of Rate Limits Used by Rate Limit Name
    Graph the sum of `datadog.apis.usage.per_org_ratio`, `datadog.apis.usage.per_user_ratio`, and `datadog.apis.usage.per_api_key_ratio` by `limit_name`  
  
**Example:** `default_zero(max:datadog.apis.usage.per_org_ratio{*} by {limit_name}) + default_zero(max:datadog.apis.usage.per_user_ratio{*} by {limit_name}) + default_zero(max:datadog.apis.usage.per_api_key_ratio{*} by {limit_name})`
### [Increase your rate limit](https://docs.datadoghq.com/api/latest/rate-limits/#increase-your-rate-limit)
You can request increased rate limits by creating a Support ticket with the below details under **Help** > **New Support Ticket**. Upon receiving a rate limit increase, our Support Engineering team reviews the request on a case-by-case basis and, if needed, works with internal engineering resources to confirm the viability of the rate limit increase request.
```
Title:
    Request to increase rate limit on endpoint: X

Details:
    We would like to request a rate limit increase for API endpoint: X
    Example use cases/queries:
        Example API call as cURL or as URL with example payload

    Motivation for increasing rate limit:
        Example - Our organization uses this endpoint to right size a container before we deploy. This deployment takes place every X hours or up to Y times per day.

    Desired target rate limit:
        Tip - Having a specific limit increase or percentage increase in mind helps Support Engineering expedite the request to internal Engineering teams for review.

```

After Datadog Support reviews and approves the use case, they can apply the rate limit increase behind the scenes. Note that there is a maximum to how much a rate limit can be increased due to the SaaS nature of Datadog. Datadog Support reserves the right to reject rate limit increases based on use cases and Engineering recommendations.
### [Audit logs](https://docs.datadoghq.com/api/latest/rate-limits/#audit-logs)
API limit and usage metrics provide insight into usage patterns and blocked requests. If you need additional details, Audit Trail offers more granular visibility into API activity.
With Audit Trail, you can view data such as:
  * **IP address & geolocation** – Identify where API requests originated.
  * **Actor type** – Distinguish between service accounts and user accounts.
  * **API vs. app key authentication** – See whether requests were made through an API key or directly by a user.
  * **Correlated events** – View other events occurring at the same time, such as configuration changes or security-related actions.


Audit Trail can help teams troubleshoot rate limit issues by providing more context on API consumption and blocked requests. It also enables tracking of API usage across an organization for security and compliance purposes.
For more detailed visibility into API activity, consider using **[Audit Trail](https://docs.datadoghq.com/account_management/audit_trail/events/)**.
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=c4b73423-79f3-48fa-8b79-0a4fb5109cd5&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=6e44f413-c311-4cec-a4ec-3eb7d6110c99&pt=Rate%20Limits&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Frate-limits%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=c4b73423-79f3-48fa-8b79-0a4fb5109cd5&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=6e44f413-c311-4cec-a4ec-3eb7d6110c99&pt=Rate%20Limits&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Frate-limits%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=b2d1b930-bab7-40b4-bd98-05f040289cbe&bo=2&sid=e9375cd0f0bd11f08bcff787fa0fba6f&vid=e9375d80f0bd11f0b5075ff6ae9d9677&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Rate%20Limits&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Frate-limits%2F&r=&lt=881&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=741832)

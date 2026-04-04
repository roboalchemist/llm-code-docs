# Source: https://developers.statuscake.com/api/

Title: StatusCake API | StatusCake Developers Portal

URL Source: https://developers.statuscake.com/api/

Markdown Content:
Skip to main content
We are looking to improve our docs, please fill this survey
Guides
References
Dashboard
Search
K
Authentication
Ratelimiting
Errors
Handling Input Parameters
FEATURES
heartbeat
pagespeed
ssl
uptime
ALERTING
contact groups
maintenance windows
MONITORING LOCATIONS
locations
StatusCake API (1.2.0)

Download OpenAPI specification:Download

Support: support@statuscake.com
URL: https://www.statuscake.com
License: Apache-2.0
Terms of Service

StatusCake API endpoints to manage monitoring resources.

Authentication

Documentation on API authentication can be found here.

Ratelimiting

Documentation on API ratelimiting can be found here.

Errors

Documentation on error handling can be found here.

Handling Input Parameters

Documentation on input parameters, including how to pass arrays to API endpoints can be found here.

heartbeat

The Heartbeat API provides methods to operate on heartbeat resources, effectively allowing checks to be read and listed.

Get all heartbeat checks

Returns a list of heartbeat checks for an account.

QUERY PARAMETERS
status	
string
Enum: "down" "up"

Heartbeat check status


page	
integer <int32> >= 1
Default: 1

Page of results


limit	
integer <int32> [ 1 .. 100 ]
Default: 25

The number of heartbeat checks to return per page


tags	
string

Comma separated list of tags assocaited with a check


matchany	
boolean
Default: false

Include heartbeat checks in response that match any specified tag or all tags. This parameter does not take a value. The absence of this paratemer equates to false whilst the presence of thie paramerter equates to true.


nouptime	
boolean
Default: false

Do not calculate uptime percentages for results. This parameter does not take a value. The absence of this paratemer equates to false whilst the presence of thie paramerter equates to true.

Responses
200 

OK

RESPONSE SCHEMA: application/json
data
required
	
Array of objects (HeartbeatTestOverview)

List of heartbeat checks


metadata
required
	
object (Pagination)
default 

Unexpected Error

GET
/heartbeat
Request samples
cURLGo
Copy
curl https://api.statuscake.com/v1/heartbeat \
  -H "Authorization: Bearer ${API_TOKEN}"

Response samples
200default
Content type
application/json
Copy
Expand allCollapse all
{
"data": 
[
{}
],
"metadata": 
{
"page": 1,
"per_page": 25,
"page_count": 10,
"total_count": 230
}
}
Create a heartbeat check

Creates a heartbeat check with the given parameters.

REQUEST BODY SCHEMA: application/x-www-form-urlencoded
name
required
	
string

Name of the check


period
required
	
integer <int32> [ 30 .. 172800 ]
Default: 1800

Number of seconds since the last ping before the check is considered down


contact_groups	
Array of strings

List of contact group IDs


host	
string

Name of the hosting provider


paused	
boolean
Default: false

Whether the check should be run


tags	
Array of strings

List of tags

Responses
201 

Created

default 

Unexpected Error

POST
/heartbeat
Request samples
cURLGo
Copy
curl -X POST https://api.statuscake.com/v1/heartbeat \
  -H "Authorization: Bearer ${API_TOKEN}" \
  -d "name=Example%20Heartbeat&period=1800"

Response samples
201default
Content type
application/json
Copy
Expand allCollapse all
{
"data": 
{
"new_id": "123"
}
}
Retrieve a heartbeat check

Returns a heartbeat check with the given id.

PATH PARAMETERS
test_id
required
	
string

Heartbeat check ID

Responses
200 

OK

RESPONSE SCHEMA: application/json
data
required
	
object (HeartbeatTest)


id
required
	
string

Heartbeat check ID


name
required
	
string

Name of the check


url
required
	
string <uri>

URL of the check


period
required
	
integer <int32> [ 30 .. 172800 ]

Number of seconds since the last ping before the check is considered down


contact_groups
required
	
Array of strings

List of contact group IDs


host	
string

Name of the hosting provider


last_tested_at	
string <date-time>

When the check was last run (RFC3339 format)


paused
required
	
boolean

Whether the check should be run


status
required
	
string (HeartbeatTestStatus)
Enum: "down" "up"

The returned status of a heartbeat check


tags
required
	
Array of strings

List of tags


uptime
required
	
number <float> >= 0

Uptime percentage for a check

default 

Unexpected Error

GET
/heartbeat/{test_id}
Request samples
cURLGo
Copy
curl https://api.statuscake.com/v1/heartbeat/123 \
  -H "Authorization: Bearer ${API_TOKEN}"

Response samples
200default
Content type
application/json
Copy
Expand allCollapse all
{
"data": 
{
"id": "123",
"name": "example Heartbeat check",
"url": "https://push.statuscake.com/?PK=61e7ca9c88f06d0&TestID=123&time=0",
"period": 1800,
"contact_groups": 
[],
"last_tested_at": "2013-01-20T14:38:18+00:00",
"paused": false,
"status": "up",
"tags": 
[],
"uptime": 99.9
}
}
Update a heartbeat check

Updates a heartbeat check with the given parameters.

PATH PARAMETERS
test_id
required
	
string

Heartbeat check ID

REQUEST BODY SCHEMA: application/x-www-form-urlencoded
name	
string

Name of the check


period	
integer <int32> [ 30 .. 172800 ]

Number of seconds since the last ping before the check is considered down


contact_groups	
Array of strings

List of contact group IDs


host	
string

Name of the hosting provider


paused	
boolean

Whether the check should be run


tags	
Array of strings

List of tags

Responses
204 

No Content

default 

Unexpected Error

PUT
/heartbeat/{test_id}
Request samples
cURLGo
Copy
curl -X PUT https://api.statuscake.com/v1/heartbeat/123 \
  -H "Authorization: Bearer ${API_TOKEN}" \
  -d "name=Example%20Heartbeat&period=1800"

Response samples
default
Content type
application/json
Copy
Expand allCollapse all
{
"message": "Something went wrong",
"errors": 
{
"field_name": 
[]
}
}
Delete a heartbeat check

Deletes a heartbeat check with the given id.

PATH PARAMETERS
test_id
required
	
string

Heartbeat check ID

Responses
204 

No Content

default 

Unexpected Error

DELETE
/heartbeat/{test_id}
Request samples
cURLGo
Copy
curl -X DELETE https://api.statuscake.com/v1/heartbeat/123 \
  -H "Authorization: Bearer ${API_TOKEN}"

Response samples
default
Content type
application/json
Copy
Expand allCollapse all
{
"message": "Something went wrong",
"errors": 
{
"field_name": 
[]
}
}
pagespeed

The Pagespeed API provides methods to operate on pagespeed resources, effectively allowing checks to be created, read, updated, and deleted. In addition the history of a specific pagespeed check can be returned for a given period.

Get all pagespeed checks

Returns a list of pagespeed checks for an account.

QUERY PARAMETERS
page	
integer <int32> >= 1
Default: 1

Page of results


limit	
integer <int32> [ 1 .. 100 ]
Default: 25

The number of pagespeed checks to return per page

Responses
200 

OK

RESPONSE SCHEMA: application/json
data
required
	
Array of objects (PagespeedTest)

List of pagespeed checks


metadata
required
	
object (Pagination)
default 

Unexpected Error

GET
/pagespeed
Request samples
cURLGo
Copy
curl https://api.statuscake.com/v1/pagespeed \
  -H "Authorization: Bearer ${API_TOKEN}"

Response samples
200default
Content type
application/json
Copy
Expand allCollapse all
{
"data": 
[
{}
],
"metadata": 
{
"page": 1,
"per_page": 25,
"page_count": 10,
"total_count": 230
}
}
Create a pagespeed check

Creates a pagespeed check with the given parameters.

REQUEST BODY SCHEMA: application/x-www-form-urlencoded
name
required
	
string

Name of the check


website_url
required
	
string <uri>

URL, FQDN, or IP address of the website under test


check_rate
required
	
integer (PagespeedTestCheckRate)
Enum: 60 300 600 900 1800 3600 86400

Number of seconds between checks


alert_bigger	
integer <int32> >= 0
Default: 0

An alert will be sent if the size of the page is larger than this value (kb). A value of 0 prevents alerts being sent.


alert_slower	
integer <int64> >= 0
Default: 0

An alert will be sent if the load time of the page exceeds this value (ms). A value of 0 prevents alerts being sent


alert_smaller	
integer <int32> >= 0
Default: 0

An alert will be sent if the size of the page is smaller than this value (kb). A value of 0 prevents alerts being sent


contact_groups	
Array of strings

List of contact group IDs


paused	
boolean
Default: false

Whether the check should be run


region
required
	
string (PagespeedTestRegion)
Enum: "AU" "CA" "DE" "FR" "IN" "JP" "NL" "SG" "UK" "US" "USW"

Region on which to run checks

Responses
201 

Created

default 

Unexpected Error

POST
/pagespeed
Request samples
cURLGo
Copy
curl -X POST https://api.statuscake.com/v1/pagespeed \
  -H "Authorization: Bearer ${API_TOKEN}" \
  -d "name=Example&website_url=https://www.example.com&region=UK&check_rate=10"

Response samples
201default
Content type
application/json
Copy
Expand allCollapse all
{
"data": 
{
"new_id": "123"
}
}
Retrieve a pagespeed check

Returns a pagespeed check with the given id.

PATH PARAMETERS
test_id
required
	
string

Pagespeed check ID

Responses
200 

OK

RESPONSE SCHEMA: application/json
data
required
	
object (PagespeedTest)


id
required
	
string

Pagespeed check ID


name
required
	
string

Name of the check


website_url
required
	
string <uri>

URL, FQDN, or IP address of the website under test


check_rate
required
	
integer (PagespeedTestCheckRate)
Enum: 60 300 600 900 1800 3600 86400

Number of seconds between checks


alert_bigger
required
	
integer <int32> >= 0

An alert will be sent if the size of the page is larger than this value (kb). A value of 0 prevents alerts being sent.


alert_slower
required
	
integer <int64> >= 0

An alert will be sent if the load time of the page exceeds this value (ms). A value of 0 prevents alerts being sent


alert_smaller
required
	
integer <int32> >= 0

An alert will be sent if the size of the page is smaller than this value (kb). A value of 0 prevents alerts being sent


contact_groups
required
	
Array of strings

List of contact group IDs


latest_stats	
object (PagespeedTestStats)

location
required
	
string

Assigned monitoring location on which checks will be run


paused
required
	
boolean

Whether the check should be run

default 

Unexpected Error

GET
/pagespeed/{test_id}
Request samples
cURLGo
Copy
curl https://api.statuscake.com/v1/pagespeed/123 \
  -H "Authorization: Bearer ${API_TOKEN}"

Response samples
200default
Content type
application/json
Copy
Expand allCollapse all
{
"data": 
{
"id": "123",
"name": "Example",
"website_url": "https://www.example.com",
"check_rate": 1800,
"alert_bigger": 0,
"alert_slower": 0,
"alert_smaller": 0,
"contact_groups": 
[],
"latest_stats": 
{},
"location": "PAGESPD-UK5",
"paused": false
}
}
Update a pagespeed check

Updates a pagespeed check with the given parameters.

PATH PARAMETERS
test_id
required
	
string

Pagespeed check ID

REQUEST BODY SCHEMA: application/x-www-form-urlencoded
name	
string

Name of the check


website_url	
string <uri>

URL, FQDN, or IP address of the website under test


check_rate	
integer (PagespeedTestCheckRate)
Enum: 60 300 600 900 1800 3600 86400

Number of seconds between checks


alert_bigger	
integer <int32> >= 0

An alert will be sent if the size of the page is larger than this value (kb). A value of 0 prevents alerts being sent.


alert_slower	
integer <int64> >= 0

An alert will be sent if the load time of the page exceeds this value (ms). A value of 0 prevents alerts being sent


alert_smaller	
integer <int32> >= 0

An alert will be sent if the size of the page is smaller than this value (kb). A value of 0 prevents alerts being sent


contact_groups	
Array of strings

List of contact group IDs


paused	
boolean

Whether the check should be run


region	
string (PagespeedTestRegion)
Enum: "AU" "CA" "DE" "FR" "IN" "JP" "NL" "SG" "UK" "US" "USW"

Region on which to run checks

Responses
204 

No Content

default 

Unexpected Error

PUT
/pagespeed/{test_id}
Request samples
cURLGo
Copy
curl -X PUT https://api.statuscake.com/v1/pagespeed/123 \
  -H "Authorization: Bearer ${API_TOKEN}" \
  -d "name=Example&region=UK&check_rate=10"

Response samples
default
Content type
application/json
Copy
Expand allCollapse all
{
"message": "Something went wrong",
"errors": 
{
"field_name": 
[]
}
}
Delete a pagespeed check

Deletes a pagespeed check with the given id.

PATH PARAMETERS
test_id
required
	
string

Pagespeed check ID

Responses
204 

No Content

default 

Unexpected Error

DELETE
/pagespeed/{test_id}
Request samples
cURLGo
Copy
curl -X DELETE https://api.statuscake.com/v1/pagespeed/123 \
  -H "Authorization: Bearer ${API_TOKEN}"

Response samples
default
Content type
application/json
Copy
Expand allCollapse all
{
"message": "Something went wrong",
"errors": 
{
"field_name": 
[]
}
}
Get all pagespeed check history

Returns a list of pagespeed check history results for a given id, detailing the runs performed on the StatusCake testing infrastruture.

The returned results are a paginated series. Alongside the response data is a links object referencing the current response document, self, and the next page in the series, next.

Aggregated data over the specified duration is returned in the root level metadata field.

PATH PARAMETERS
test_id
required
	
string

Pagespeed check ID

QUERY PARAMETERS
limit	
integer <int32> [ 1 .. 100 ]
Default: 25

The number of results to return from the series


before	
integer <int64> >= 0

Only results created before this UNIX timestamp will be returned


after	
integer <int64> >= 0

Only results created after this UNIX timestamp will be returned

Responses
200 

OK

RESPONSE SCHEMA: application/json
data
required
	
Array of objects (PagespeedTestHistoryResult)

List of pagespeed check history results


links
required
	
object (Links)

metadata	
object (Metadata)
default 

Unexpected Error

GET
/pagespeed/{test_id}/history
Request samples
cURLGo
Copy
curl https://api.statuscake.com/v1/pagespeed/123/history \
  -H "Authorization: Bearer ${API_TOKEN}"

Response samples
200default
Content type
application/json
Copy
Expand allCollapse all
{
"data": 
[
{}
],
"links": 
{
"self": "https://api.statuscake.com/v1/pagespeed/1/history?before=1509796803",
"next": "https://api.statuscake/com/v1/pagespeed/1/history?before=1509796703"
},
"metadata": 
{
"aggregates": 
{}
}
}
ssl

The SSL API provides methods to operate on SSL resources, effectively allowing checks to be created, read, updated, and deleted.

Get all SSL checks

Returns a list of SSL checks for an account.

QUERY PARAMETERS
page	
integer <int32> >= 1
Default: 1

Page of results


limit	
integer <int32> [ 1 .. 100 ]
Default: 25

The number of SSL checks to return per page

Responses
200 

OK

RESPONSE SCHEMA: application/json
data
required
	
Array of objects (SSLTest)

List of SSL checks


metadata
required
	
object (Pagination)
default 

Unexpected Error

GET
/ssl
Request samples
cURLGo
Copy
curl https://api.statuscake.com/v1/ssl \
  -H "Authorization: Bearer ${API_TOKEN}"

Response samples
200default
Content type
application/json
Copy
Expand allCollapse all
{
"data": 
[
{}
],
"metadata": 
{
"page": 1,
"per_page": 25,
"page_count": 10,
"total_count": 230
}
}
Create an SSL check

Creates an SSL check with the given parameters.

REQUEST BODY SCHEMA: application/x-www-form-urlencoded
website_url
required
	
string <uri>

URL of the server under test. Must begin with https://


check_rate
required
	
integer (SSLTestCheckRate)
Enum: 300 600 1800 3600 86400 2073600

Number of seconds between checks


alert_at
required
	
Array of integers <int32> [ items <int32 > ]

List representing when alerts should be sent (days). Must be exactly 3 numerical values


alert_broken	
boolean
Default: false

Whether to enable alerts when SSL certificate issues are found


alert_expiry	
boolean
Default: false

Whether to enable alerts when the SSL certificate is to expire


alert_mixed	
boolean
Default: false

Whether to enable alerts when mixed content is found


alert_reminder	
boolean
Default: false

Whether to enable alert reminders


contact_groups	
Array of strings

List of contact group IDs


follow_redirects	
boolean
Default: false

Whether to follow redirects when testing. Disabled by default


hostname	
string

Hostname of the server under test


paused	
boolean
Default: false

Whether the check should be run


user_agent	
string

Custom user agent string set when testing

Responses
201 

Created

default 

Unexpected Error

POST
/ssl
Request samples
cURLGo
Copy
curl -X POST https://api.statuscake.com/v1/ssl \
  -H "Authorization: Bearer ${API_TOKEN}" \
  -d "website_url=https://www.example.com&check_rate=1800&alert_at[]=1&alert_at[]=2&alert_at[]=3&alert_reminder=true&alert_expiry=true&alert_broken=true&alert_mixed=true"

Response samples
201default
Content type
application/json
Copy
Expand allCollapse all
{
"data": 
{
"new_id": "123"
}
}
Retrieve an SSL check

Returns an SSL check with the given id.

PATH PARAMETERS
test_id
required
	
string

SSL check ID

Responses
200 

OK

RESPONSE SCHEMA: application/json
data
required
	
object (SSLTest)


id
required
	
string

SSL check ID


website_url
required
	
string <uri>

URL of the server under test


check_rate
required
	
integer (SSLTestCheckRate)
Enum: 300 600 1800 3600 86400 2073600

Number of seconds between checks


alert_at
required
	
Array of integers <int32> [ items <int32 > ]

List representing when alerts should be sent (days).


alert_broken
required
	
boolean

Whether to enable alerts when SSL certificate issues are found


alert_expiry
required
	
boolean

Whether to enable alerts when the SSL certificate is to expire


alert_mixed
required
	
boolean

Whether to enable alerts when mixed content is found


alert_reminder
required
	
boolean

Whether to enable alert reminders


certificate_score	
integer <int32> [ 0 .. 100 ]

SSL certificate score (%)


certificate_status	
string

SSL certificate status


cipher	
string

SSL/TLS cipher suite belonging to the SSL certificate


cipher_score	
integer <int32> [ 0 .. 100 ]

SSL certificate cipher strength (%)


contact_groups
required
	
Array of strings

List of contact group IDs


issuer_common_name	
string

Issuer of the SSL certificate


flags	
object (SSLTestFlags)

follow_redirects
required
	
boolean

Whether to follow redirects when testing. Disabled by default


hostname	
string

Hostname of the server under test


last_reminder	
integer <int32> >= 0

The last reminder to have been sent (days)


mixed_content
required
	
Array of objects (SSLTestMixedContent)

List of mixed content resources


paused
required
	
boolean

Whether the check should be run


updated_at	
string <date-time>

When the SSL certificate was last updated (RFC3339 format)


user_agent	
string

Custom user agent string set when testing


valid_from	
string <date-time>

SSL certificate validity start (RFC3339 format)


valid_until	
string <date-time>

SSL certificate validity end (RFC3339 format)

default 

Unexpected Error

GET
/ssl/{test_id}
Request samples
cURLGo
Copy
curl https://api.statuscake.com/v1/ssl/123 \
  -H "Authorization: Bearer ${API_TOKEN}"

Response samples
200default
Content type
application/json
Copy
Expand allCollapse all
{
"data": 
{
"id": "123",
"website_url": "https://www.example.com",
"check_rate": 1800,
"alert_at": 
[],
"alert_broken": true,
"alert_expiry": true,
"alert_mixed": true,
"alert_reminder": true,
"certificate_score": 55,
"certificate_status": "CERT_OK",
"cipher": "TLS_RSA_WITH_AES_128_GCM_SHA256",
"cipher_score": 70,
"contact_groups": 
[],
"issuer_common_name": "Let's Encrypt Authority X3",
"flags": 
{},
"follow_redirects": true,
"hostname": "svc.example.com",
"last_reminder": 0,
"mixed_content": 
[],
"paused": false,
"updated_at": "2017-10-24T09:02:25+00:00",
"user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.51 mycustomstring",
"valid_from": "2017-10-10T14:06:00+00:00",
"valid_until": "2017-12-29T00:00:00+00:00"
}
}
Update an SSL check

Updates an SSL check with the given parameters.

PATH PARAMETERS
test_id
required
	
string

SSL check ID

REQUEST BODY SCHEMA: application/x-www-form-urlencoded
website_url	
string <uri>

URL of the server under test. Must begin with https://


check_rate	
integer (SSLTestCheckRate)
Enum: 300 600 1800 3600 86400 2073600

Number of seconds between checks


alert_at	
Array of integers <int32> [ items <int32 > ]

List representing when alerts should be sent (days). Must be exactly 3 numerical values


alert_broken	
boolean

Whether to enable alerts when SSL certificate issues are found


alert_expiry	
boolean

Whether to enable alerts when the SSL certificate is to expire


alert_mixed	
boolean

Whether to enable alerts when mixed content is found


alert_reminder	
boolean

Whether to enable alert reminders


contact_groups	
Array of strings

List of contact group IDs


follow_redirects	
boolean

Whether to follow redirects when testing. Disabled by default


hostname	
string

Hostname of the server under test


paused	
boolean

Whether the check should be run


user_agent	
string

Custom user agent string set when testing

Responses
204 

No Content

default 

Unexpected Error

PUT
/ssl/{test_id}
Request samples
cURLGo
Copy
curl -X PUT https://api.statuscake.com/v1/ssl/123 \
  -H "Authorization: Bearer ${API_TOKEN}" \
  -d "check_rate=1800&alert_at[]=1&alert_at[]=2&alert_at[]=3&alert_reminder=true&alert_expiry=true&alert_broken=true&alert_mixed=true"

Response samples
default
Content type
application/json
Copy
Expand allCollapse all
{
"message": "Something went wrong",
"errors": 
{
"field_name": 
[]
}
}
Delete an SSL check

Deletes an SSL check with the given id.

PATH PARAMETERS
test_id
required
	
string

Pagespeed check ID

Responses
204 

No Content

default 

Unexpected Error

DELETE
/ssl/{test_id}
Request samples
cURLGo
Copy
curl -X DELETE https://api.statuscake.com/v1/ssl/123 \
  -H "Authorization: Bearer ${API_TOKEN}"

Response samples
default
Content type
application/json
Copy
Expand allCollapse all
{
"message": "Something went wrong",
"errors": 
{
"field_name": 
[]
}
}
uptime

The Uptime API provides methods to operate on uptime resources, effectively allowing checks to be created, read, updated, and deleted. In addition the Uptime API is able to return a history of uptime status for a given period; and return a history of alerts since a given date.

Get all uptime checks

Returns a list of uptime checks for an account.

QUERY PARAMETERS
status	
string
Enum: "down" "up"

Uptime check status


page	
integer <int32> >= 1
Default: 1

Page of results


limit	
integer <int32> [ 1 .. 100 ]
Default: 25

The number of uptime checks to return per page


tags	
string

Comma separated list of tags assocaited with a check


matchany	
boolean
Default: false

Include uptime checks in response that match any specified tag or all tags. This parameter does not take a value. The absence of this paratemer equates to false whilst the presence of thie paramerter equates to true.


nouptime	
boolean
Default: false

Do not calculate uptime percentages for results. This parameter does not take a value. The absence of this paratemer equates to false whilst the presence of thie paramerter equates to true.

Responses
200 

OK

RESPONSE SCHEMA: application/json
data
required
	
Array of objects (UptimeTestOverview)

List of uptime checks


metadata
required
	
object (Pagination)
default 

Unexpected Error

GET
/uptime
Request samples
cURLGo
Copy
curl https://api.statuscake.com/v1/uptime \
  -H "Authorization: Bearer ${API_TOKEN}"

Response samples
200default
Content type
application/json
Copy
Expand allCollapse all
{
"data": 
[
{}
],
"metadata": 
{
"page": 1,
"per_page": 25,
"page_count": 10,
"total_count": 230
}
}
Create an uptime check

Creates an uptime check with the given parameters.

REQUEST BODY SCHEMA: application/x-www-form-urlencoded
name
required
	
string

Name of the check


test_type
required
	
string (UptimeTestType)
Enum: "DNS" "HEAD" "HTTP" "PING" "SMTP" "SSH" "TCP"

Uptime check type


website_url
required
	
string <uri>

URL or IP address of the server under test


check_rate
required
	
integer (UptimeTestCheckRate)
Enum: 0 30 60 300 900 1800 3600 86400

Number of seconds between checks


basic_username	
string

Basic authentication username


basic_password	
string

Basic authentication password


confirmation	
integer <int32> [ 0 .. 3 ]
Default: 2

Number of confirmation servers to confirm downtime before an alert is triggered


contact_groups	
Array of strings

List of contact group IDs


custom_header	
string

JSON object. Represents headers to be sent when making requests


do_not_find	
boolean
Default: false

Whether to consider the check as down if the content is present within the response


dns_ips	
Array of strings

List of IP addresses to compare against returned DNS records


dns_server	
string

FQDN or IP address of the nameserver to query


enable_ssl_alert	
boolean
Default: false

Whether to send an alert if the SSL certificate is soon to expire


final_endpoint	
string

Specify where the redirect chain should end


find_string	
string

String to look for within the response. Considered down if not found


follow_redirects	
boolean
Default: false

Whether to follow redirects when testing. Disabled by default


host	
string

Name of the hosting provider


include_header	
boolean
Default: false

Include header content in string match search


paused	
boolean
Default: false

Whether the check should be run


port	
integer <int32> >= 0

Destination port for TCP checks


post_body	
string

JSON object. Payload submitted with the request. Setting this updates the check to use the HTTP POST verb


post_raw	
string

Raw HTTP POST string to send to the server


regions	
Array of strings

List of regions on which to run checks. The values required for this parameter can be retrieved from the GET /v1/uptime-locations endpoint.


status_codes_csv	
string

Comma separated list of status codes that trigger an alert


tags	
Array of strings

List of tags


timeout	
integer <int32> [ 5 .. 75 ]
Default: 15

The number of seconds to wait to receive the first byte


trigger_rate	
integer <int32> [ 0 .. 60 ]
Default: 0

The number of minutes to wait before sending an alert


use_jar	
boolean
Default: false

Whether to enable cookie storage


user_agent	
string

Custom user agent string set when testing

Responses
201 

Created

default 

Unexpected Error

POST
/uptime
Request samples
cURLGo
Copy
curl -X POST https://api.statuscake.com/v1/uptime \
  -H "Authorization: Bearer ${API_TOKEN}" \
  -d "name=Example%20HTTP&test_type=HTTP&website_url=https://www.example.com&check_rate=1800&regions[]=london&regions[]=paris"

Response samples
201default
Content type
application/json
Copy
Expand allCollapse all
{
"data": 
{
"new_id": "123"
}
}
Retrieve an uptime check

Returns an uptime check with the given id.

PATH PARAMETERS
test_id
required
	
string

Uptime check ID

Responses
200 

OK

RESPONSE SCHEMA: application/json
data
required
	
object (UptimeTest)


id
required
	
string

Uptime check ID


name
required
	
string

Name of the check


test_type
required
	
string (UptimeTestType)
Enum: "DNS" "HEAD" "HTTP" "PING" "SMTP" "SSH" "TCP"

Uptime check type


website_url
required
	
string <uri>

URL, FQDN, or IP address of the server under test


check_rate
required
	
integer (UptimeTestCheckRate)
Enum: 0 30 60 300 900 1800 3600 86400

Number of seconds between checks


confirmation
required
	
integer <int32> [ 0 .. 3 ]

Number of confirmation servers to confirm downtime before an alert is triggered


contact_groups
required
	
Array of strings

List of contact group IDs


custom_header	
string

JSON object. Represents headers to be sent when making requests


dns_ips
required
	
Array of strings

List of IP addresses to compare against returned DNS records


dns_server	
string

FQDN or IP address of the nameserver to query


do_not_find
required
	
boolean

Whether to consider the check as down if the content is present within the response


enable_ssl_alert
required
	
boolean

Whether to send an alert if the SSL certificate is soon to expire


final_endpoint	
string

Specify where the redirect chain should end


find_string	
string

String to look for within the response. Considered down if not found


follow_redirects
required
	
boolean

Whether to follow redirects when testing. Disabled by default


include_header
required
	
boolean

Include header content in string match search


host	
string

Name of the hosting provider


last_tested_at	
string <date-time>

When the check was last run (RFC3339 format)


next_location	
string

The server location the check will run next


paused
required
	
boolean

Whether the check should be run


port	
integer <int32> >= 0

Destination port for TCP checks


post_body	
string

JSON object. Payload submitted with the request. Setting this updates the check to use the HTTP POST verb


post_raw	
string

Raw HTTP POST string to send to the server


processing
required
	
boolean

Whether the check is currently being processed


processing_on	
string

The server location the check is currently being run


processing_state	
string (UptimeTestProcessingState)
Enum: "complete" "pretest" "retest" "up_retest"

Uptime check proccessing state


servers
required
	
Array of objects (MonitoringLocation)

List of assigned monitoring locations on which to run checks


status
required
	
string (UptimeTestStatus)
Enum: "down" "up"

The returned status of an uptime check


status_codes
required
	
Array of strings

List of status codes that trigger an alert


tags
required
	
Array of strings

List of tags


timeout
required
	
integer <int32> [ 5 .. 75 ]

The number of seconds to wait to receive the first byte


trigger_rate
required
	
integer <int32> [ 0 .. 60 ]

The number of minutes to wait before sending an alert


uptime
required
	
number <float> >= 0

Uptime percentage for a check


use_jar
required
	
boolean

Whether to enable cookie storage


user_agent	
string

Custom user agent string set when testing

default 

Unexpected Error

GET
/uptime/{test_id}
Request samples
cURLGo
Copy
curl https://api.statuscake.com/v1/uptime/123 \
  -H "Authorization: Bearer ${API_TOKEN}"

Response samples
200default
Content type
application/json
Copy
Expand allCollapse all
{
"data": 
{
"id": "123",
"name": "example HTTP check",
"test_type": "HTTP",
"website_url": "https://www.example.com",
"check_rate": 1800,
"confirmation": 3,
"contact_groups": 
[],
"dns_ips": [ ],
"do_not_find": false,
"enable_ssl_alert": true,
"follow_redirects": false,
"host": "AWS",
"include_header": false,
"last_tested_at": "2013-01-20T14:38:18+00:00",
"next_location": "UK",
"paused": false,
"processing": true,
"processing_on": "UKCON2",
"processing_state": "pretest",
"servers": 
[],
"status": "up",
"status_codes": 
[],
"tags": 
[],
"timeout": 15,
"trigger_rate": 0,
"uptime": 99.9,
"use_jar": true
}
}
Update an uptime check

Updates an uptime check with the given parameters.

PATH PARAMETERS
test_id
required
	
string

Uptime check ID

REQUEST BODY SCHEMA: application/x-www-form-urlencoded
name	
string

Name of the check


website_url	
string <uri>

URL or IP address of the server under test


check_rate	
integer (UptimeTestCheckRate)
Enum: 0 30 60 300 900 1800 3600 86400

Number of seconds between checks


basic_username	
string

Basic authentication username


basic_password	
string

Basic authentication password


confirmation	
integer <int32> [ 0 .. 3 ]

Number of confirmation servers to confirm downtime before an alert is triggered


contact_groups	
Array of strings

List of contact group IDs


custom_header	
string

JSON object. Represents headers to be sent when making requests


do_not_find	
boolean

Whether to consider the check as down if the content is present within the response


dns_ips	
Array of strings

List of IP addresses to compare against returned DNS records


dns_server	
string

FQDN or IP address of the nameserver to query


enable_ssl_alert	
boolean

Whether to send an alert if the SSL certificate is soon to expire


final_endpoint	
string

Specify where the redirect chain should end


find_string	
string

String to look for within the response. Considered down if not found


follow_redirects	
boolean

Whether to follow redirects when testing. Disabled by default


host	
string

Name of the hosting provider


include_header	
boolean

Include header content in string match search


paused	
boolean

Whether the check should be run


port	
integer <int32> >= 0

Destination port for TCP checks


post_body	
string

JSON object. Payload submitted with the request. Setting this updates the check to use the HTTP POST verb


post_raw	
string

Raw HTTP POST string to send to the server


regions	
Array of strings

List of regions on which to run checks. The values required for this parameter can be retrieved from the GET /v1/uptime-locations endpoint.


status_codes_csv	
string

Comma separated list of status codes that trigger an alert


tags	
Array of strings

List of tags


timeout	
integer <int32> [ 5 .. 75 ]

The number of seconds to wait to receive the first byte


trigger_rate	
integer <int32> [ 0 .. 60 ]

The number of minutes to wait before sending an alert


use_jar	
boolean

Whether to enable cookie storage


user_agent	
string

Custom user agent string set when testing

Responses
204 

No Content

default 

Unexpected Error

PUT
/uptime/{test_id}
Request samples
cURLGo
Copy
curl -X PUT https://api.statuscake.com/v1/uptime/123 \
  -H "Authorization: Bearer ${API_TOKEN}" \
  -d "name=Example%20HTTP&check_rate=1800&regions[]=london&regions[]=paris"

Response samples
default
Content type
application/json
Copy
Expand allCollapse all
{
"message": "Something went wrong",
"errors": 
{
"field_name": 
[]
}
}
Delete an uptime check

Deletes an uptime check with the given id.

PATH PARAMETERS
test_id
required
	
string

Uptime check ID

Responses
204 

No Content

default 

Unexpected Error

DELETE
/uptime/{test_id}
Request samples
cURLGo
Copy
curl -X DELETE https://api.statuscake.com/v1/uptime/123 \
  -H "Authorization: Bearer ${API_TOKEN}"

Response samples
default
Content type
application/json
Copy
Expand allCollapse all
{
"message": "Something went wrong",
"errors": 
{
"field_name": 
[]
}
}
Get all uptime check history

Returns a list of uptime check history results for a given id, detailing the runs performed on the StatusCake testing infrastruture.

The returned results are a paginated series. Alongside the response data is a links object referencing the current response document, self, and the next page in the series, next.

PATH PARAMETERS
test_id
required
	
string

Uptime check ID

QUERY PARAMETERS
limit	
integer <int32> [ 1 .. 100 ]
Default: 25

The number of results to return per page


before	
integer <int64> >= 0

Only results created before this UNIX timestamp will be returned


after	
integer <int64> >= 0

Only results created after this UNIX timestamp will be returned

Responses
200 

OK

RESPONSE SCHEMA: application/json
data
required
	
Array of objects (UptimeTestHistoryResult)

List of uptime check history results


links
required
	
object (Links)

metadata	
object (Metadata)
default 

Unexpected Error

GET
/uptime/{test_id}/history
Request samples
cURLGo
Copy
curl https://api.statuscake.com/v1/uptime/123/history \
  -H "Authorization: Bearer ${API_TOKEN}"

Response samples
200default
Content type
application/json
Copy
Expand allCollapse all
{
"data": 
[
{}
],
"links": 
{
"self": "https://api.statuscake.com/v1/uptime/1/history?before=1509796803",
"next": "https://api.statuscake.com/v1/uptime/1/history?before=1509796703"
}
}
Get all uptime check periods

Returns a list of uptime check periods for a given id, detailing the creation time of the period, when it ended and the duration.

The returned results are a paginated series. Alongside the response data is a links object referencing the current response document, self, and the next page in the series, next.

PATH PARAMETERS
test_id
required
	
string

Uptime check ID

QUERY PARAMETERS
limit	
integer <int32> [ 1 .. 100 ]
Default: 25

The number of uptime check periods to return per page


before	
integer <int64> >= 0

Only check periods created before this UNIX timestamp will be returned


after	
integer <int64> >= 0

Only check periods created after this UNIX timestamp will be returned

Responses
200 

OK

RESPONSE SCHEMA: application/json
data
required
	
Array of objects (UptimeTestPeriod)

List of uptime check periods


links
required
	
object (Links)

metadata	
object (Metadata)
default 

Unexpected Error

GET
/uptime/{test_id}/periods
Request samples
cURLGo
Copy
curl https://api.statuscake.com/v1/uptime/123/periods \
  -H "Authorization: Bearer ${API_TOKEN}"

Response samples
200default
Content type
application/json
Copy
Expand allCollapse all
{
"data": 
[
{}
],
"links": 
{
"self": "https://api.statuscake.com/v1/uptime/1/periods?before=1361803461",
"next": "https://api.statuscake.com/v1/uptime/1/periods?before=1361803361"
}
}
Get all uptime check alerts

Returns a list of uptime check alerts for a given id.

The returned results are a paginated series. Alongside the response data is a links object referencing the current response document, self, and the next page in the series, next.

PATH PARAMETERS
test_id
required
	
string

Uptime check ID

QUERY PARAMETERS
limit	
integer <int32> [ 1 .. 100 ]
Default: 25

The number of uptime alerts to return per page


before	
integer <int64> >= 0

Only alerts triggered before this UNIX timestamp will be returned


after	
integer <int64> >= 0

Only alerts triggered after this UNIX timestamp will be returned

Responses
200 

OK

RESPONSE SCHEMA: application/json
data
required
	
Array of objects (UptimeTestAlert)

List of uptime check alerts


links
required
	
object (Links)

metadata	
object (Metadata)
default 

Unexpected Error

GET
/uptime/{test_id}/alerts
Request samples
cURLGo
Copy
curl https://api.statuscake.com/v1/uptime/123/alerts \
  -H "Authorization: Bearer ${API_TOKEN}"

Response samples
200default
Content type
application/json
Copy
Expand allCollapse all
{
"data": 
[
{}
],
"links": 
{
"self": "https://api.statuscake.com/v1/uptime/1/alerts?before=1361803461",
"next": "https://api.statuscake.com/v1/uptime/1/alerts?before=1361803361"
}
}
contact groups

The Contact Groups API provides methods to configure how StatusCake alerts are forwarded to the people that need to see them.

Get all contact groups

Returns a list of contact groups for an account.

QUERY PARAMETERS
page	
integer <int32> >= 1
Default: 1

Page of results


limit	
integer <int32> [ 1 .. 100 ]
Default: 25

The number of contact groups to return per page

Responses
200 

OK

RESPONSE SCHEMA: application/json
data
required
	
Array of objects (ContactGroup)

List of contact groups


metadata
required
	
object (Pagination)
default 

Unexpected Error

GET
/contact-groups
Request samples
cURLGo
Copy
curl https://api.statuscake.com/v1/contact-groups \
  -H "Authorization: Bearer ${API_TOKEN}"

Response samples
200default
Content type
application/json
Copy
Expand allCollapse all
{
"data": 
[
{}
],
"metadata": 
{
"page": 1,
"per_page": 25,
"page_count": 10,
"total_count": 230
}
}
Create a contact group

Creates a contact group with the given parameters.

REQUEST BODY SCHEMA: application/x-www-form-urlencoded
name
required
	
string

Name of the contact group


email_addresses	
Array of strings

List of email addresses


integrations	
Array of strings

List of integration IDs


mobile_numbers	
Array of strings

List of international format mobile phone numbers


ping_url	
string <uri>

URL or IP address of an endpoint to push uptime events. Currently this only supports HTTP GET endpoints

Responses
201 

Created

default 

Unexpected Error

POST
/contact-groups
Request samples
cURLGo
Copy
curl -X POST https://api.statuscake.com/v1/contact-groups \
  -H "Authorization: Bearer ${API_TOKEN}" \
  -d "name=Operations%20Team&email_addresses[]=johnsmith@example.com&email_addresses[]=janesmith@example.com"

Response samples
201default
Content type
application/json
Copy
Expand allCollapse all
{
"data": 
{
"new_id": "123"
}
}
Retrieve a contact group

Returns a contact group with the given id.

PATH PARAMETERS
group_id
required
	
string

Contact group ID

Responses
200 

OK

RESPONSE SCHEMA: application/json
data
required
	
object (ContactGroup)


id
required
	
string

Contact group ID


name
required
	
string

Name of the contact group


email_addresses
required
	
Array of strings

List of email addresses


integrations
required
	
Array of strings

List of configured integration IDs


mobile_numbers
required
	
Array of strings

List of international format mobile phone numbers


ping_url	
string <uri>

URL or IP address of an endpoint to push uptime events. Currently this only supports HTTP GET endpoints

default 

Unexpected Error

GET
/contact-groups/{group_id}
Request samples
cURLGo
Copy
curl https://api.statuscake.com/v1/contact-groups/123 \
  -H "Authorization: Bearer ${API_TOKEN}"

Response samples
200default
Content type
application/json
Copy
Expand allCollapse all
{
"data": 
{
"id": "123",
"name": "Operations Team",
"email_addresses": 
[],
"integrations": 
[],
"mobile_numbers": 
[],
"ping_url": "https://www.example.com/notifications"
}
}
Update a contact group

Updates a contact group with the given parameters.

PATH PARAMETERS
group_id
required
	
string

Contact group ID

REQUEST BODY SCHEMA: application/x-www-form-urlencoded
name	
string

Name of the contact group


email_addresses	
Array of strings

List of email addresses


integrations	
Array of strings

List of integration IDs


mobile_numbers	
Array of strings

List of international format mobile phone numbers


ping_url	
string <uri>

URL or IP address of an endpoint to push uptime events. Currently this only supports HTTP GET endpoints

Responses
204 

No Content

default 

Unexpected Error

PUT
/contact-groups/{group_id}
Request samples
cURLGo
Copy
curl -X PUT https://api.statuscake.com/v1/contact-groups/123 \
  -H "Authorization: Bearer ${API_TOKEN}" \
  -d "name=Operations%20Team&email_addresses[]johnsmith@example.com&email_addresses[]=janesmith@example.com"

Response samples
default
Content type
application/json
Copy
Expand allCollapse all
{
"message": "Something went wrong",
"errors": 
{
"field_name": 
[]
}
}
Delete a contact group

Deletes a contact group with the given id.

PATH PARAMETERS
group_id
required
	
string

Contact group ID

Responses
204 

No Content

default 

Unexpected Error

DELETE
/contact-groups/{group_id}
Request samples
cURLGo
Copy
curl -X DELETE https://api.statuscake.com/v1/contact-groups/123 \
  -H "Authorization: Bearer ${API_TOKEN}"

Response samples
default
Content type
application/json
Copy
Expand allCollapse all
{
"message": "Something went wrong",
"errors": 
{
"field_name": 
[]
}
}
maintenance windows

The Maintenance Windows API provides methods to pause alerts from being sent for scheduled maintenance periods.

NOTE: the API endpoints concerned with maintenance windows will only work with accounts registed to use the newer version of maintenance windows. This version of maintenance windows is incompatible with the original version and all existing windows will require migrating to be further used. Presently a tool to automate the migration of maintenance windows is under development.

Get all maintenance windows

Returns a list of maintenance windows for an account.

QUERY PARAMETERS
page	
integer <int32> >= 1
Default: 1

Page of results


limit	
integer <int32> [ 1 .. 100 ]
Default: 25

The number of maintenance windows to return per page


state	
string
Enum: "active" "paused" "pending"

Maintenance window state

Responses
200 

OK

RESPONSE SCHEMA: application/json
data
required
	
Array of objects (MaintenanceWindow)

List of maintenance windows


metadata
required
	
object (Pagination)
default 

Unexpected Error

GET
/maintenance-windows
Request samples
cURLGo
Copy
curl https://api.statuscake.com/v1/maintenance-windows \
  -H "Authorization: Bearer ${API_TOKEN}"

Response samples
200default
Content type
application/json
Copy
Expand allCollapse all
{
"data": 
[
{}
],
"metadata": 
{
"page": 1,
"per_page": 25,
"page_count": 10,
"total_count": 230
}
}
Create a maintenance window

Creates a maintenance window with the given parameters.

REQUEST BODY SCHEMA: application/x-www-form-urlencoded
name
required
	
string

Name of the maintenance window


end_at
required
	
string <date-time>

End of the maintenance window (RFC3339 format)


repeat_interval	
string (MaintenanceWindowRepeatInterval)
Enum: "never" "1d" "1w" "2w" "1m"

How often the maintenance window should occur


start_at
required
	
string <date-time>

Start of the maintenance window (RFC3339 format)


tags	
Array of strings

List of tags used to include matching uptime checks in this maintenance window. At least one of tests and tags must be present in the request


tests	
Array of strings

List of uptime check IDs explicitly included in this maintenance window. At least one of tests and tags must be present in the request


timezone
required
	
string

Standard timezone associated with this maintenance window

Responses
201 

Created

default 

Unexpected Error

POST
/maintenance-windows
Request samples
cURLGo
Copy
curl -X POST https://api.statuscake.com/v1/maintenance-windows \
  -H "Authorization: Bearer ${API_TOKEN}" \
  -d "name=Weekends&start_at=2021-12-06T01:30:00Z&end_at=2021-07-11T06:00:00Z&repeat_interval=1w&tags[]=production&timezone=UTC"

Response samples
201default
Content type
application/json
Copy
Expand allCollapse all
{
"data": 
{
"new_id": "123"
}
}
Retrieve a maintenance window

Returns a maintenance window with the given id.

PATH PARAMETERS
window_id
required
	
string

Maintenance window ID

Responses
200 

OK

RESPONSE SCHEMA: application/json
data
required
	
object (MaintenanceWindow)


id
required
	
string

Maintenance window ID


name
required
	
string

Name of the maintenance window


end_at
required
	
string <date-time>

End of the maintenance window (RFC3339 format)


repeat_interval
required
	
string (MaintenanceWindowRepeatInterval)
Enum: "never" "1d" "1w" "2w" "1m"

How often the maintenance window should occur


start_at
required
	
string <date-time>

Start of the maintenance window (RFC3339 format)


state
required
	
string (MaintenanceWindowState)
Enum: "active" "paused" "pending"

Maintenance window state


tags
required
	
Array of strings

List of tags used to include matching uptime checks in this maintenance window


tests
required
	
Array of strings

List of uptime check IDs explicitly included in this maintenance window


timezone
required
	
string

Standard timezone associated with this maintenance window

default 

Unexpected Error

GET
/maintenance-windows/{window_id}
Request samples
cURLGo
Copy
curl https://api.statuscake.com/v1/maintenance-windows/123 \
  -H "Authorization: Bearer ${API_TOKEN}"

Response samples
200default
Content type
application/json
Copy
Expand allCollapse all
{
"data": 
{
"id": "123",
"name": "Weekends",
"end_at": "2020-10-25T23:59:59+00:00",
"repeat_interval": "1w",
"start_at": "2020-10-24T00:00:00+00:00",
"state": "active",
"tags": 
[],
"tests": 
[],
"timezone": "UTC"
}
}
Update a maintenance window

Updates a maintenance window with the given parameters.

PATH PARAMETERS
window_id
required
	
string

Maintenance window ID

REQUEST BODY SCHEMA: application/x-www-form-urlencoded
name	
string

Name of the maintenance window


end_at	
string <date-time>

End of the maintenance window (RFC3339 format)


repeat_interval	
string (MaintenanceWindowRepeatInterval)
Enum: "never" "1d" "1w" "2w" "1m"

How often the maintenance window should occur


start_at	
string <date-time>

Start of the maintenance window (RFC3339 format)


tags	
Array of strings

List of tags used to include matching uptime checks in this maintenance window


tests	
Array of strings

List of uptime check IDs explicitly included in this maintenance window


timezone	
string

Standard timezone associated with this maintenance window

Responses
204 

No Content

default 

Unexpected Error

PUT
/maintenance-windows/{window_id}
Request samples
cURLGo
Copy
curl -X PUT https://api.statuscake.com/v1/maintenance-windows/123 \
  -H "Authorization: Bearer ${API_TOKEN}" \
  -d "name=Weekends&start_at=2021-12-06T01:30:00Z&end_at=2021-07-11T06:00:00Z&repeat_interval=1w&tags[]=production&timezone=UTC"

Response samples
default
Content type
application/json
Copy
Expand allCollapse all
{
"message": "Something went wrong",
"errors": 
{
"field_name": 
[]
}
}
Delete a maintenance window

Deletes a maintenance window with the given id.

PATH PARAMETERS
window_id
required
	
string

Maintenance window ID

Responses
204 

No Content

default 

Unexpected Error

DELETE
/maintenance-windows/{window_id}
Request samples
cURLGo
Copy
curl -X DELETE https://api.statuscake.com/v1/maintenance-windows/123 \
  -H "Authorization: Bearer ${API_TOKEN}"

Response samples
default
Content type
application/json
Copy
Expand allCollapse all
{
"message": "Something went wrong",
"errors": 
{
"field_name": 
[]
}
}
locations

The Locations API returns details of our testing infrastructure. This may be used to gather information regarding IP addresses that may need to be allowed through firewalls for checks to be succesful.

Get all uptime monitoring locations

Returns a list of locations detailing server information for uptime monitoring servers. This information can be used to create further checks using the API.

QUERY PARAMETERS
region_code	
string

Server region code

Responses
200 

OK

RESPONSE SCHEMA: application/json
data
required
	
Array of objects (MonitoringLocation)

List of monitoring locations



Array 
description
required
	
string

Server description


ipv4	
string <ipv4>

Server IPv4 address


ipv6	
string <ipv6>

Server IPv6 address


region
required
	
string

Server region


region_code
required
	
string

Server region code


status
required
	
string (MonitoringLocationStatus)
Enum: "down" "up"

Server status

default 

Unexpected Error

GET
/uptime-locations
Request samples
cURLGo
Copy
curl https://api.statuscake.com/v1/uptime-locations \
  -H "Authorization: Bearer ${API_TOKEN}"

Response samples
200default
Content type
application/json
Copy
Expand allCollapse all
{
"data": 
[
{}
]
}
Get all pagespeed monitoring locations

Returns a list of locations detailing server information for pagespeed monitoring servers. This information can be used to create further checks using the API.

QUERY PARAMETERS
location	
string

Alpha-2 ISO 3166-1 country code

Responses
200 

OK

RESPONSE SCHEMA: application/json
data
required
	
Array of objects (MonitoringLocation)

List of monitoring locations



Array 
description
required
	
string

Server description


ipv4	
string <ipv4>

Server IPv4 address


ipv6	
string <ipv6>

Server IPv6 address


region
required
	
string

Server region


region_code
required
	
string

Server region code


status
required
	
string (MonitoringLocationStatus)
Enum: "down" "up"

Server status

default 

Unexpected Error

GET
/pagespeed-locations
Request samples
cURLGo
Copy
curl https://api.statuscake.com/v1/pagespeed-locations \
  -H "Authorization: Bearer ${API_TOKEN}"

Response samples
200default
Content type
application/json
Copy
Expand allCollapse all
{
"data": 
[
{}
]
}
Documentation
Guides
Community
GitHub
Stack Overflow
LinkedIn
Twitter
More
Blog
Careers
Copyright © 2026 StatusCake. Built with Docusaurus and Redocly.

# Source: https://docs.trackjs.com/data-api/errors/

Title: Errors API

URL Source: https://docs.trackjs.com/data-api/errors/

Markdown Content:
This endpoint returns a list of individual errors, sorted by date descending.

[URI](https://docs.trackjs.com/data-api/errors/#uri "Permalink Here")
---------------------------------------------------------------------

GET https://api.trackjs.com/{CUSTOMER_ID}/v1/errors
The following querystring parameters are accepted:

### [application](https://docs.trackjs.com/data-api/errors/#application "Permalink Here")

String

Optional

Filter the results to only the Application key provided.

* * *

### [endDate](https://docs.trackjs.com/data-api/errors/#enddate "Permalink Here")

ISO 8601 String

Optional

Filter the results to only return errors before this date. Time precision is within 1 second.

* * *

### [startDate](https://docs.trackjs.com/data-api/errors/#startdate "Permalink Here")

ISO 8601 String

Optional

Filter the results to only return errors after this date. Time precision is within 1 second.

* * *

### [page](https://docs.trackjs.com/data-api/errors/#page "Permalink Here")

Number

Optional

The page of data you want returned. By default, the first page of data is returned. See [Paging](https://docs.trackjs.com/data-api/#paging).

* * *

### [size](https://docs.trackjs.com/data-api/errors/#size "Permalink Here")

Number 1-1000

Optional

The size of the page of data you want returned. See [Paging](https://docs.trackjs.com/data-api/#paging).

* * *

### [query](https://docs.trackjs.com/data-api/errors/#query "Permalink Here")

String

Optional

Filter the results to errors that match the supplied query term. The query searches errors in the same way as the [TrackJS Dashboard Search](https://my.trackjs.com/search). Many fields are searched including Error Message, URLs, Metadata and User IDs.

* * *

### [includeStack](https://docs.trackjs.com/data-api/errors/#includestack "Permalink Here")

Boolean

Optional

Whether to return a `stackTrace` with the Error response. The value is unprocessed except for splitting on newlines `\n`. These can be very large, so they are not included by default.

[Response](https://docs.trackjs.com/data-api/errors/#response "Permalink Here")
-------------------------------------------------------------------------------

{ "data": [{ "message": "test", "timestamp": "2014-09-24T23:53:08+00:00", "url": "https://my.trackjs.com/", "id": "5d893bd8c50346fe9b97af36af530f2d", "browserName": "Firefox", "browserVersion": "32.0", "entry": "direct", "line": 40, "column": 213, "file": "awesome.js", "userId": "", "sessionId": "", "status": "Investigating", "trackJsUrl": "https://my.trackjs.com/details/5d893bd8c50346fe9b97af36af530f2d", "stackTrace": [ "ReferenceError: data is not defined", " at HTMLDocument (https://my.trackjs.com/daily?date=2016-07-23:387:41)", " at c (https://my.trackjs.com/js/lib/jquery/jquery-1.10.2.min.js:4:26036)", " at Object.fireWith [as resolveWith] (https://my.trackjs.com/js/lib/jquery/jquery-1.10.2.min.js:4:26840)", " at Function.ready (https://my.trackjs.com/js/lib/jquery/jquery-1.10.2.min.js:4:3305)", " at HTMLDocument.q (https://my.trackjs.com/js/lib/jquery/jquery-1.10.2.min.js:4:717)" ], "metadata": [{ "key": "subscription", "value": "Professional" }] }], "metadata": { "startDate": "2014-09-11T00:00:00Z", "endDate": "2014-09-12T00:00:00Z", "totalCount": 193, "page": 1, "size": 3, "hasMore": true, "trackJsUrl": "https://my.trackjs.com/recent" }}
[Example](https://docs.trackjs.com/data-api/errors/#example "Permalink Here")
-----------------------------------------------------------------------------

curl -H "Authorization: {API_KEY}" "https://api.trackjs.com/{CUSTOMER_ID}/v1/errors?startDate=2018-11-20&endDate=2018-11-27&includeStack=true"
[Search Example](https://docs.trackjs.com/data-api/errors/#search-example "Permalink Here")
-------------------------------------------------------------------------------------------

It is often useful to filter the errors returned by more than date range. The `query` parameter allows you to limit results to those that contain the supplied string. The query string is used to perform the same search done in the [TrackJS Dashboard Search](https://my.trackjs.com/search). You can search against many fields including Error Message, URLs, Metadata and User IDs.

curl -H "Authorization: {API_KEY}" "https://api.trackjs.com/{CUSTOMER_ID}/v1/errors?query=Cannot%20read%20property"

* * *

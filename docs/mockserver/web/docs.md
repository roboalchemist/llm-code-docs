Getting Started Mocking

MockServer

* [What is MockServer](/#what-is-mockserver)
* [Why use MockServer](/#why-use-mockserver)

* [Running MockServer](/mock_server/running_mock_server.html)
* [MockServer Clients](/mock_server/mockserver_clients.html)
* [MockServer UI](/mock_server/mockserver_ui.html)
* [Clearing & Resetting](/mock_server/clearing_and_resetting.html)
* [Logging & Debugging](/mock_server/debugging_issues.html)
* [Scalability & Latency](/mock_server/performance.html)
* [HTTPS & TLS](/mock_server/HTTPS_TLS.html)
* [API Security](/mock_server/control_plane_authorisation.html)
* [CORS Support](/mock_server/CORS_support.html)
* [Configuration](/mock_server/configuration_properties.html)
* [REST API Reference](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi)
* [Example Code](https://github.com/mock-server/mockserver/tree/master/mockserver-examples)

Mocking

* [Getting Started](/mock_server/getting_started.html)
* [Creating Expectations](/mock_server/creating_expectations.html)
* [Using OpenAPI](/mock_server/using_openapi.html)
* [Response Templates](/mock_server/response_templates.html)
* [Verifying Requests](/mock_server/verification.html)
* [Expectation Initializers](/mock_server/initializing_expectations.html)
* [Persisting Expectations](/mock_server/persisting_expectations.html)
* [Running Tests In Parallel](/mock_server/running_tests_in_parallel.html)

Proxying

* [Getting Started](/proxy/getting_started.html)
* [Configuring Clients](/proxy/configuring_sut.html)
* [Record & Replay](/proxy/record_and_replay.html)
* [Verifying Requests](/proxy/verification.html)
* [Isolate Single Service](/mock_server/isolating_single_service.html)

Where

* [Downloads](/where/downloads.html)
* [Community](/where/slack.html)
* [Source Control](/where/github.html)
* [Backlog & Issues](/where/trello.html)
* [npm](/where/npm.html)
* [Maven](/where/maven_central.html)
* [Docker](/where/docker.html)
* [Helm & Kubernetes](/where/kubernetes.html)
* [Swagger Hub](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi)

Getting Started Mocking
=======================

![Note: this page is a high level overview of each topic, more detail is available for each topic on a linked page.](../images/more_detail_available_message.png)

The typical sequence for using MockServer is as follows:

0. [Start MockServer](#start_mockserver)
1. [Setup Expectations](#setup_expectations)
2. Run Your Test Scenarios
3. [Verify Requests](#verify_requests)

![Mocking service dependencies with MockServer](../images/system_under_test_with_mockserver_cropped.png)

For example code see the [code examples folder](https://github.com/mock-server/mockserver/tree/master/mockserver-examples) in the git repository.

1. Start MockServer

-------------------

MockServer is flexible and support numerous usage patterns.

### MockServer can be run

* programmatically via a [**Java API**](/mock_server/running_mock_server.html#client_api) in an @Before or @After method
* using a [**JUnit 4 @Rule**](/mock_server/running_mock_server.html#junit_rule) via a @Rule annotated field in a JUnit 4 test
* using a [**JUnit 5 Test Extension**](/mock_server/running_mock_server.html#junit_test_extension) via a @ExtendWith annotated JUnit 5 class
* using a [**Spring Test Execution Listener**](/mock_server/running_mock_server.html#spring_test_exec_listener) via a @MockServerTest annotated test class
* as a [**Docker container**](/mock_server/running_mock_server.html#docker_container) in any Docker enabled environment
* via a [**Helm chart**](/mock_server/running_mock_server.html#helm_chart) in any Kubernetes environment
* from the [**command line**](/mock_server/running_mock_server.html#running_from_command_line) as a stand-alone process in a test environment
* via a [**Maven Plugin**](/mock_server/running_mock_server.html#maven_plugin) as part of a Maven build cycle
* as a [**Node.js (npm) module**](/mock_server/running_mock_server.html#mockserver_node) from any Node.js code
* as a [**Grunt plugin**](/mock_server/running_mock_server.html#mockserver_node) as part of a Grunt build cycle
* as a [**deployable WAR**](/mock_server/running_mock_server.html#deployable_war) to an existing application server

To simplify configuration all versions (except the deployable WAR) use a single port to support the control plane and data plane in HTTP, HTTPS or SOCKS.

### MockServer is available in the following formats

* [java dependency](https://search.maven.org/artifact/org.mock-server/mockserver-netty/5.14.0/shaded)
* [Docker container](https://hub.docker.com/r/mockserver/mockserver)
* [Helm chart](#helm_chart) for Kubernetes
* [executable jar](https://search.maven.org/remotecontent?filepath=org/mock-server/mockserver-netty/5.14.0/mockserver-netty-5.14.0-shaded.jar)
* [Homebrew package](#running_from_command_line_using_homebrew)
* [maven plugin](#maven_plugin)
* [npm plugin](https://www.npmjs.org/package/mockserver-node)
* [Grunt plugin](https://www.npmjs.org/package/mockserver-node)
* [deployable WAR](https://search.maven.org/remotecontent?filepath=org/mock-server/mockserver-war/5.14.0/mockserver-war-5.14.0.war) that runs on JEE web servers

It is also possible to [build and run MockServer directly from source code](/mock_server/running_mock_server.html#build-and-run-from-source)

### MockServer UI

MockServer has a [UI](/mock_server/mockserver_ui.html) that can be used to view the internal state within MockServer, including:

* **[logs](#ui_logs_section)**
* **[active expectations](#ui_active_expectations_section)**
* **[requests received](#ui_requests_received_section)**
* **[proxied requests](#ui_proxied_requests_section)**

1. Setup Expectations

---------------------

**Java Code Example**

***Please Note:** There are over 100 more detailed code examples in Java, JavaScript and the REST API below.*

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withMethod("POST")
            .withPath("/login")
            .withBody("{username: 'foo', password: 'bar'}")
    )
    .respond(
        response()
            .withStatusCode(302)
            .withCookie(
                "sessionId", "2By8LOhBmaW5nZXJwcmludCIlMDAzMW"
            )
            .withHeader(
                "Location", "https://www.mock-server.com"
            )
    );
```

**JavaScript Code Example**

***Please Note:** There are over 100 more detailed code examples in Java, JavaScript and the REST API below.*

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "method": "POST",
        "path": "/login",
        "body": {
            "username": "foo",
            "password": "bar"
        }
    },
    "httpResponse": {
        "statusCode": 302,
        "headers": {
            "Location": [
                "https://www.mock-server.com"
            ]
        },
        "cookies": {
            "sessionId": "2By8LOhBmaW5nZXJwcmludCIlMDAzMW"
        }
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

To use the Java client add the **org.mock-server:mockserver-client-java-no-dependencies:5.14.0** dependency.

For more details about the different dependency versions see the page on [Maven Central](/where/maven_central.html#mockserver_client_java)

for example in maven:

```
<dependency>
 <groupId>org.mock-server</groupId>
 <artifactId>mockserver-client-java-no-dependencies</artifactId>
 <version>RELEASE</version>
</dependency>
```

A **request matcher expectation** may contain:

* **[request matcher](#request_matchers)** - used to match which requests this expectation should be applied to
* **[action](#actions)** - what action to take, actions include **response**, **forward**, **callback** and **error**
* **[times](#button_match_request_by_path_exactly_twice)** *(optional)* - how many times the action should be taken
* **[timeToLive](#button_match_request_by_path_exactly_once_in_the_next_60_seconds)** *(optional)* - how long the expectation should stay active
* **[priority](#button_match_request_by_priority)** *(optional)* - matching is ordered by priority (highest first) then creation (earliest first)
* **[id](#button_match_request_update_by_id)** *(optional)* - used for updating an existing expectation (i.e. when the id matches)

**[open api expectations](/mock_server/using_openapi.html#generate_expectation_from_openapi)** are also supported using an [**OpenAPI
v3**](https://swagger.io/docs/specification/basic-structure/) specifications to generate **request matcher expectations** for each operation, see the section on **[open api
expectations](/mock_server/using_openapi.html#generate_expectation_from_openapi)** for details.

#### Matching Order

MockServer will match (or play) active expectations in the exact order they are added (if their priority is identical). For example, if an expectation A is added with Times.exactly(3)
then expectation B is added with Times.exactly(2) with the same request matcher they will be applied in the following order A, A, A, B, B. Priority can be used to alter the order that expectations are matched; matching is ordered by
priority (highest first) then creation (earliest first).

Priority can be used to configure a [default expectation or response](#button_match_request_by_negative_priority) by specifying a negative value for priority and a very lax request matcher; the lax request matcher ensures the
default expectation is always matched, but the low priority ensure it is matched last after all other expectations.

#### Updating Expectations

If an expectation is added and the **id** field matches an existing expectation the existing expectation will be updated (i.e. replaced). A UUID will be used assigned to each expectation if no value for **id**
is specified.

### Request Matchers

The are two types of **request matcher**:

* **[request properties matcher](#request_properties_matchers)** - that match requests using HTTP properties such as **method**, **path** or **body**
* **[open api request matcher](#request_openapi_matchers)** - that match requests using an [**OpenAPI**](https://swagger.io/docs/specification/about/) definition

A **request properties matcher** matches requests using one or more of the following properties:

* **method** - [property matcher](#request_property_matchers)
* **path** - [property matcher](#request_property_matchers)
* **path parameters** - [key to multiple values matcher](#request_key_to_multivalue_matchers)
* **query string parameters** - [key to multiple values matcher](#request_key_to_multivalue_matchers)
* **headers** - [key to multiple values matcher](#request_key_to_multivalue_matchers)
* **cookies** - [key to single value matcher](#request_key_to_value_matchers)
* **body** - [body matchers](#request_body_matchers)
* **secure** - boolean value, true for HTTPS

Matching for **properties** can be done using:

* **string value**
  * **use for:** method, path, path parameter keys, path parameters values, query parameter keys, query parameters values, header keys, header values, cookie keys, cookie values or bodies
  * **examples:** [method](#button_match_request_by_query_parameter_name_regex), [path](#button_match_request_by_path), [path parameters](#button_match_request_by_path_and_path_parameters), [query parameters](#button_match_request_by_cookies_and_query_parameters), [headers](#button_match_request_by_headers), [cookies](#button_match_request_by_cookies_and_query_parameters)
* **regex value**
  * **use for:** method, path, path parameter keys, path parameters values, query parameter keys, query parameters values, header keys, header values, cookie keys, cookie values or bodies
  * **examples:** [method](#button_match_request_by_method_regex), [path](#button_match_request_by_regex_path), [path parameters](#button_match_request_by_path_parameter_regex_value), [query parameters](#button_match_request_by_query_parameter_name_regex), [headers](#button_match_request_by_header_name_regex)
  * for syntax see [Java regex syntax](https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html)
* **json schema**
  * **use for:** method, path, path parameters values, query parameters values, header values, cookie values or bodies
  * **not supported for:** path parameter keys, query parameter keys, header keys or cookie keys
  * **examples:** [path parameters](#button_match_request_by_path_parameter_json_schema_value), [query parameters](#button_match_request_by_query_parameter_value_json_schema), [headers](#button_match_request_by_header_value_json_schema) , [cookies](#button_match_request_by_cookies_value_json_schema)
  * for syntax see [JSON Schema documentation](https://json-schema.org)
* **optional value**
  * **use for:** method, path, path parameters values, query parameter keys, query parameters values, header keys, header values, cookie keys, cookie values or bodies
  * **not supported for:** path parameter keys or values, query parameter values, header values or cookie values
  * **examples:** [query parameters](#button_match_request_by_optional_query_parameter), [headers](#button_match_request_by_optional_header), [cookies](#button_match_request_by_optional_cookies)
* **negated value**
  * **use for:** method, path, path parameter keys, path parameters values, query parameter keys, query parameters values, header keys, header values, cookie keys, cookie values or bodies
  * **examples:** [method](#button_match_request_by_not_matching_method), [path](#button_match_request_by_not_matching_path), [headers](#button_match_request_by_not_matching_header_value)

Matching for **key to multiple values** supports multiple values for each key for headers, query parameters and path parameters

* Keys support all [property matcher](#request_property_matchers) except json schema
* Values support all [property matcher](#request_property_matchers) except optional values
* Matching supports two modes:
  * **[sub set](#button_match_request_by_query_parameter_by_sub_set)** (default) - matches if the request property contains a matching sub set (considering optional keys), therefore there is **at least one matching value** for each
    non-optional key or optional key if present
  * **[matching key](#button_match_request_by_header_by_matching_key)** - matches if the request property contains only matching values (considering optional keys), therefore **all values must match** for each non-optional key or optional
    key if present

Matching for **key to single value** supports a single value for each key for cookies

* Keys support all [property matcher](#request_property_matchers) except json schema
* Values support all [property matcher](#request_property_matchers) except optional values

Matching for **bodies** can be done using:

* **[plain text](#button_match_request_by_body_in_utf16)** (i.e. exact match)
* **[regular expression](#button_match_request_by_regex_body)** - see [Java regex syntax](https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html)
* **[JSON](#button_match_request_by_body_with_json_exactly)** - supports:
  * **matchType** to control which fields get matched:
    * **[STRICT](#button_match_request_by_body_with_json_exactly)** matches all fields, order of arrays and no additional fields allowed
    * **[ONLY\_MATCHING\_FIELDS](#button_match_request_by_body_with_json_ignoring_extra_fields)** only matches fields provided in the request matcher
  * **[JSONUnit placeholders](#button_match_request_by_body_with_json_placeholders)** to allow fields or values to be ignored or matched by type for example:
    * **${json-unit.ignore-element}** ignore a field
    * **${json-unit.any-boolean}** match a field as any booleansee [JSONUnit documentation](https://github.com/lukas-krecan/JsonUnit) for full details
* **[JSON Schema](#button_match_request_by_body_with_json_schema)** - see [JSON Schema documentation](https://json-schema.org/)
* **[JsonPath](#button_match_request_by_body_with_json_path)** - matches if at least one value is returned by the expression, see [JsonPath documentation](https://github.com/json-path/JsonPath)
* **[XML](#button_match_request_by_body_with_xml)** - supports:
  * **[XMLUnit placeholders](#button_match_request_by_body_with_xml_placeholders)** to allow fields or elements to be ignored or matched by type for example:
    * **${xmlunit.ignore}** ignore an element
    * **${xmlunit.isNumber}** match an element or attribute as a numbersee [XMLUnit documentation](https://github.com/xmlunit/user-guide/wiki/Placeholders) for full details
* **[XML Schema](#button_match_request_by_body_with_xml_schema)** - see [XML Schema documentation](https://www.w3.org/standards/xml/schema.html)
* **[XPath](#button_match_request_by_body_with_xpath)** - matches if at least one value returned by expression, see [XPath specification](https://www.w3.org/TR/2017/REC-xpath-31-20170321/)
* **[form fields](#button_match_request_by_form_submission_body)** (i.e. body parameters)
* **[binary](#button_match_request_by_binary_body)**
* **[negated matcher](#button_match_request_by_not_matching_body_with_xpath)**

**Request Properties Matcher Code Examples**

The following code examples show how to match against different elements of a request using different matchers. For more examples see the [code examples folder](https://github.com/mock-server/mockserver/tree/master/mockserver-examples) in the git repository.

For brevity static imports have not been included in the Java code examples so please add the following static imports if copying this code

```
import static org.mockserver.model.HttpRequest.request;
import static org.mockserver.model.HttpResponse.response;
```

match requests using priority

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path"),
        Times.once(),
        TimeToLive.exactly(TimeUnit.SECONDS, 60L),
        10
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some/path"
    },
    "httpResponse": {
        "body": "some_response_body"
    },
    "times": {
        "remainingTimes": 1,
        "unlimited": false
    },
    "timeToLive": {
        "timeUnit": "SECONDS",
        "timeToLive": 60,
        "unlimited": false
    },
    "priority" : 10
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
  "httpRequest" : {
    "path" : "/some/path"
  },
  "httpResponse" : {
    "body" : "some_response_body"
  },
  "times" : {
    "remainingTimes" : 1,
    "unlimited" : false
  },
  "timeToLive" : {
    "timeUnit" : "SECONDS",
    "timeToLive" : 60,
    "unlimited" : false
  },
  "priority" : 10
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

match requests using default expectation

A negative priority can be used to specify a default expectation or response.

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request(),
        Times.once(),
        TimeToLive.exactly(TimeUnit.SECONDS, 60L),
        -10
    )
    .respond(
        response()
            .withBody("some_default_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {},
    "httpResponse": {
        "body": "some_default_response_body"
    },
    "times": {
        "remainingTimes": 1,
        "unlimited": false
    },
    "timeToLive": {
        "timeUnit": "SECONDS",
        "timeToLive": 60,
        "unlimited": false
    },
    "priority" : -10
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
  "httpRequest" : {},
  "httpResponse" : {
    "body" : "some_default_response_body"
  },
  "times" : {
    "remainingTimes" : 1,
    "unlimited" : false
  },
  "timeToLive" : {
    "timeUnit" : "SECONDS",
    "timeToLive" : 60,
    "unlimited" : false
  },
  "priority" : -10
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

match request by path

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some/path"
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
  "httpRequest" : {
    "path" : "/some/path"
  },
  "httpResponse" : {
    "body" : "some_response_body"
  }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

match request by path exactly twice

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path"),
        Times.exactly(2)
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some/path"
    },
    "httpResponse": {
        "body": "some_response_body"
    },
    "times": {
        "remainingTimes": 2
    },
    "timeToLive": {
        "unlimited": true
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
  "httpRequest" : {
    "path" : "/some/path"
  },
  "httpResponse" : {
    "body" : "some_response_body"
  },
  "times" : {
    "remainingTimes" : 2,
    "unlimited" : false
  },
  "timeToLive" : {
    "unlimited" : true
  }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

match request by path exactly once in the next 60 seconds

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path"),
        Times.once(),
        TimeToLive.exactly(TimeUnit.SECONDS, 60L)
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some/path"
    },
    "httpResponse": {
        "body": "some_response_body"
    },
    "times": {
        "remainingTimes": 1,
        "unlimited": false
    },
    "timeToLive": {
        "timeUnit": "SECONDS",
        "timeToLive": 60,
        "unlimited": false
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
  "httpRequest" : {
    "path" : "/some/path"
  },
  "httpResponse" : {
    "body" : "some_response_body"
  },
  "times" : {
    "remainingTimes" : 1,
    "unlimited" : false
  },
  "timeToLive" : {
    "timeUnit" : "SECONDS",
    "timeToLive" : 60,
    "unlimited" : false
  }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

match request by regex path

For details of the full regex syntax supported please see [the JDK documentation](https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html).

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            // matches any requests those path starts with "/some"
            .withPath("/some.*")
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
// matches any requests those path starts with "/some"
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some.*"
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
  "httpRequest" : {
    "path" : "/some.*"
  },
  "httpResponse" : {
    "body" : "some_response_body"
  }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

match request by not matching path

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            // matches any requests those path does NOT start with "/some"
            .withPath(not("/some.*"))
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
// matches any requests those path does NOT start with "/some"
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "!/some.*"
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
  "httpRequest" : {
    "path" : "!/some.*"
  },
  "httpResponse" : {
    "body" : "some_response_body"
  }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

match request by path parameter and query parameter

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
            .withPathParameters(
                param("cartId", "055CA455-1DF7-45BB-8535-4F83E7266092")
            )
            .withQueryStringParameters(
                param("type", "[A-Z0-9\\-]+")
            )
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
    "path": "/some/path/{cartId}",
        "pathParameters": {
            "cartId": ["055CA455-1DF7-45BB-8535-4F83E7266092"]
        },
        "queryStringParameters": {
            "type": ["[A-Z0-9\\-]+"]
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
    "path": "/some/path/{cartId}",
        "pathParameters": {
            "cartId": ["055CA455-1DF7-45BB-8535-4F83E7266092"]
        },
        "queryStringParameters": {
            "type": ["[A-Z0-9\\-]+"]
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

match request by path parameter regex value

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path/{cartId}")
            .withPathParameters(
                param("cartId", "[A-Z0-9\\-]+")
            )
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some/path/{cartId}",
        "pathParameters": {
            "cartId": ["[A-Z0-9\\-]+"]
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "path": "/some/path/{cartId}",
        "pathParameters": {
            "cartId": ["[A-Z0-9\\-]+"]
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

match request by path parameter with json schema value

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path/{cartId}/{maxItemCount}")
            .withPathParameters(
                schemaParam("cartId", "{\"type\": \"string\", \"pattern\": \"^[A-Z0-9\\-]+$\"}"),
                param(string("maxItemCount"), schemaString("{ \"type\": \"integer\" }"))
            )
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some/path/{cartId}/{maxItemCount}",
        "pathParameters": {
            "cartId": [{
                "schema": {
                    "type": "string",
                    "pattern": "^[A-Z0-9-]+$"
                }
            }],
            "maxItemCount": [{
                "schema": {
                    "type": "integer"
                }
            }]
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "path": "/some/path/{cartId}/{maxItemCount}",
        "pathParameters": {
            "cartId": [{
                "schema": {
                    "type": "string",
                    "pattern": "^[A-Z0-9-]+$"
                }
            }],
            "maxItemCount": [{
                "schema": {
                    "type": "integer"
                }
            }]
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

match request by method regex

For details of the full regex syntax supported please see [the JDK documentation](https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html).

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            // matches any requests that does NOT have a "GET" method
            .withMethod(not("P.*{2,3}"))
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "method": "P.*{2,3}"
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
  "httpRequest" : {
    "method" : "P.*{2,3}"
  },
  "httpResponse" : {
    "body" : "some_response_body"
  }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

match request by not matching method

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            // matches any requests that does NOT have a "GET" method
            .withMethod(not("GET"))
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
// matches any requests that does NOT have a "GET" method
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "method": "!GET"
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
  "httpRequest" : {
    "method" : "!GET"
  },
  "httpResponse" : {
    "body" : "some_response_body"
  }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

match request by query parameter with name regex

For details of the full regex syntax supported please see [the JDK documentation](https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html).

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
            .withQueryStringParameters(
                param("[A-z]{0,10}", "055CA455-1DF7-45BB-8535-4F83E7266092")
            )
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some/path",
        "queryStringParameters": {
            "[A-z]{0,10}": ["055CA455-1DF7-45BB-8535-4F83E7266092"]
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "path": "/some/path",
        "queryStringParameters": {
            "[A-z]{0,10}": ["055CA455-1DF7-45BB-8535-4F83E7266092"]
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

match request by query parameter with regex value

For details of the full regex syntax supported please see [the JDK documentation](https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html).

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
            .withQueryStringParameters(
                param("cartId", "[A-Z0-9\\-]+")
            )
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some/path",
        "queryStringParameters": {
            "cartId": ["[A-Z0-9\\-]+"]
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "path": "/some/path",
        "queryStringParameters": {
            "cartId": ["[A-Z0-9\\-]+"]
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

match request by query parameter with json schema value

Java

This example shows the two ways a JSON Schema can be specified to match a query parameter value, either using the **schemaParam** static builder for parameters or the **schemaString** for static builder
strings.

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
            .withQueryStringParameters(
                schemaParam("cartId", "{\"type\": \"string\", \"pattern\": \"^[A-Z0-9\\-]+$\"}"),
                param(string("maxItemCount"), schemaString("{ \"type\": \"integer\" }"))
            )
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some/path",
        "queryStringParameters": {
            "cartId": [{
                "schema": {
                    "type": "string",
                    "pattern": "^[A-Z0-9-]+$"
                }
            }],
            "maxItemCount": [{
                "schema": {
                    "type": "integer"
                }
            }]
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "path": "/some/path",
        "queryStringParameters": {
            "cartId": [{
                "schema": {
                    "type": "string",
                    "pattern": "^[A-Z0-9-]+$"
                }
            }],
            "maxItemCount": [{
                "schema": {
                    "type": "integer"
                }
            }]
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

match request by optional query parameter

Java

This example shows the two ways to specify an optional query parameter value, either using the **optionalParam** static builder for parameters or the **optionalString** for static builder strings.

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
            .withQueryStringParameters(
                optionalParam("cartId", "[A-Z0-9\\-]+"),
                param(optionalString("maxItemCount"), schemaString("{ \"type\": \"integer\" }")),
                schemaParam(optionalString("userId"), "{ \"type\": \"string\", \"format\": \"uuid\" }")
            )
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some/path",
        "queryStringParameters": {
            "?cartId": ["[A-Z0-9\\-]+"],
            "?maxItemCount": [{
                "schema": {
                    "type": "integer"
                }
            }],
            "?userId": [{
                "schema": {
                    "type": "string",
                    "format": "uuid"
                }
            }]
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "path": "/some/path",
        "queryStringParameters": {
            "?cartId": ["[A-Z0-9\\-]+"],
            "?maxItemCount": [{
                "schema": {
                    "type": "integer"
                }
            }],
            "?userId": [{
                "schema": {
                    "type": "string",
                    "format": "uuid"
                }
            }]
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

match request by query parameter as sub set

Matching by keys to multiple-values by **SUB\_SET** is the default mode this ensures at least one value with the same key matches, but **MATCHING\_KEY** is also supported which ensures all values with the same
key match.

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
            .withQueryStringParameters(new Parameters(
                schemaParam("multiValuedParameter", "{\"type\": \"string\", \"pattern\": \"^[A-Z0-9\\-]+$\"}"),
                param(string("maxItemCount"), schemaString("{ \"type\": \"integer\" }"))
            ).withKeyMatchStyle(KeyMatchStyle.SUB_SET))
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

Matching by **SUB\_SET** is the default mode so nothing needs to be specified for this key match style.

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest" : {
        "path" : "/some/path",
        "queryStringParameters" : {
            "multiValuedParameter" : [ {
                "schema" : {
                    "type" : "string",
                    "pattern" : "^[A-Z0-9-]+$"
                }
            } ],
            "maxItemCount" : [ {
                "schema" : {
                    "type" : "integer"
                }
            } ]
        }
    },
    "httpResponse" : {
        "body" : "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

Matching by **SUB\_SET** is the default mode so nothing needs to be specified for this key match style.

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest" : {
        "path" : "/some/path",
        "queryStringParameters" : {
            "multiValuedParameter" : [ {
                "schema" : {
                    "type" : "string",
                    "pattern" : "^[A-Z0-9-]+$"
                }
            } ],
            "maxItemCount" : [ {
                "schema" : {
                    "type" : "integer"
                }
            } ]
        }
    },
    "httpResponse" : {
        "body" : "some_response_body"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

match request by query parameter as matching key

Matching by keys to multiple-values by **SUB\_SET** is the default mode this ensures at least one value with the same key matches, but **MATCHING\_KEY** is also supported which ensures all values with the same
key match.

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
            .withQueryStringParameters(new Parameters(
                schemaParam("multiValuedParameter", "{\"type\": \"string\", \"pattern\": \"^[A-Z0-9\\-]+$\"}"),
                param(string("maxItemCount"), schemaString("{ \"type\": \"integer\" }"))
            ).withKeyMatchStyle(KeyMatchStyle.MATCHING_KEY))
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest" : {
        "path" : "/some/path",
        "queryStringParameters" : {
            "keyMatchStyle" : "MATCHING_KEY",
            "multiValuedParameter" : [ {
                "schema" : {
                    "type" : "string",
                    "pattern" : "^[A-Z0-9-]+$"
                }
            } ],
            "maxItemCount" : [ {
                "schema" : {
                    "type" : "integer"
                }
            } ]
        }
    },
    "httpResponse" : {
        "body" : "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest" : {
        "path" : "/some/path",
        "queryStringParameters" : {
            "keyMatchStyle" : "MATCHING_KEY",
            "multiValuedParameter" : [ {
                "schema" : {
                    "type" : "string",
                    "pattern" : "^[A-Z0-9-]+$"
                }
            } ],
            "maxItemCount" : [ {
                "schema" : {
                    "type" : "integer"
                }
            } ]
        }
    },
    "httpResponse" : {
        "body" : "some_response_body"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

match request by headers

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withMethod("GET")
            .withPath("/some/path")
            .withHeaders(
                header("Accept", "application/json"),
                header("Accept-Encoding", "gzip, deflate, br")
            )
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "method": "GET",
        "path": "/some/path",
        "headers": {
            "Accept": ["application/json"],
            "Accept-Encoding": ["gzip, deflate, br"]
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
  "httpRequest" : {
    "method" : "GET",
    "path" : "/some/path",
    "headers" : {
      "Accept" : [ "application/json" ],
      "Accept-Encoding" : [ "gzip, deflate, br" ]
    }
  },
  "httpResponse" : {
    "body" : "some_response_body"
  }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

match request by header name regex

For details of the full regex syntax supported please see [the JDK documentation](https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html).

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
            .withHeader(
                header("Accept.*")
            )
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some/path",
        "headers": {
            // matches requests that have any header starting with the name Accept
            "Accept.*": [ "" ]
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
// matches requests that have any header starting with the name Accept
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "path": "/some/path",
        "headers": {
            "Accept.*": [ "" ]
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

match request by header name and regex value

For details of the full regex syntax supported please see [the JDK documentation](https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html).

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
            .withHeader(
                header("Accept.*", ".*gzip.*")
            )
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some/path",
        "headers": {
            // matches requests that have a header with a name starting with Accept and a value containing gzip
            "Accept.*": [".*gzip.*"]
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
// matches requests that have a header with a name starting with Accept and a value containing gzip
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "path": "/some/path",
        "headers": {
            "Accept.*": [".*gzip.*"]
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

match request by not matching header value

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
            .withHeaders(
                // matches requests that have an Accept header without the value "application/json"
                header(string("Accept"), not("application/json")),
                // matches requests that have an Accept-Encoding without the substring "gzip"
                header(string("Accept-Encoding"), not(".*gzip.*"))
            )
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some/path",
        "headers": {
            // matches requests that have an Accept header without the value "application/json"
            "Accept": ["!application/json"],
            // matches requests that have an Accept-Encoding without the substring "gzip"
            "Accept-Encoding": ["!.*gzip.*"]
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
  "httpRequest" : {
    "path" : "/some/path",
    "headers" : {
      "Accept" : [ "!application/json" ],
      "Accept-Encoding" : [ "!.*gzip.*" ]
    }
  },
  "httpResponse" : {
    "body" : "some_response_body"
  }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

match request by not matching headers

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
            .withHeaders(
                // matches requests that do not have either an Accept or an Accept-Encoding header
                header(not("Accept")),
                header(not("Accept-Encoding"))
            )
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some/path",
        "headers": {
            // matches requests that do not have either an Accept or an Accept-Encoding header
            "!Accept": [".*"],
            "!Accept-Encoding": [".*"]
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
  "httpRequest" : {
    "path" : "/some/path",
    "headers" : {
      "!Accept" : [ ".*" ],
      "!Accept-Encoding" : [ ".*" ]
    }
  },
  "httpResponse" : {
    "body" : "some_response_body"
  }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

match request by header with json schema value

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
            .withHeader(
                schemaHeader("Accept.*", "{\"type\": \"string\", \"pattern\": \"^.*gzip.*$\"}")
            )
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some/path",
        "headers": {
            "Accept.*": [{
                "schema": {
                    "type": "string",
                    "pattern": "^.*gzip.*$"
                }
            }]
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "path": "/some/path",
        "headers": {
            "Accept.*": [{
                "schema": {
                    "type": "string",
                    "pattern": "^.*gzip.*$"
                }
            }]
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

match request by either one header or another header using optional header

This example shows how to match by either one value (in this case a header) or another value or both.

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
            .withHeaders(
                header("headerOne|headerTwo", ".*"),
                optionalHeader("headerOne", "headerOneValue"),
                optionalHeader("headerTwo", "headerTwoValue")
            )
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some/path",
        "headers": {
            "headerOne|headerTwo": [".*"],
            "?headerOne": ["headerOneValue"],
            "?headerTwo": ["headerTwoValue"]
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "path": "/some/path",
        "headers": {
            "headerOne|headerTwo": [".*"],
            "?headerOne": ["headerOneValue"],
            "?headerTwo": ["headerTwoValue"]
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

match request by header as matching key

Matching by keys to multiple-values by **SUB\_SET** is the default mode this ensures at least one value with the same key matches, but **MATCHING\_KEY** is also supported which ensures all values with the same
key match.

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
            .withHeaders(new Headers(
                header("multiValuedHeader", "value.*"),
                header("headerTwo", "headerTwoValue")
            ).withKeyMatchStyle(KeyMatchStyle.MATCHING_KEY))
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest" : {
        "path" : "/some/path",
        "headers" : {
            "keyMatchStyle" : "MATCHING_KEY",
            "multiValuedHeader" : [ "value.*" ],
            "headerTwo" : [ "headerTwoValue" ]
        }
    },
    "httpResponse" : {
        "body" : "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest" : {
        "path" : "/some/path",
        "headers" : {
            "keyMatchStyle" : "MATCHING_KEY",
            "multiValuedHeader" : [ "value.*" ],
            "headerTwo" : [ "headerTwoValue" ]
        }
    },
    "httpResponse" : {
        "body" : "some_response_body"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

match request by cookie and query parameter

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withMethod("GET")
            .withPath("/view/cart")
            .withCookies(
                cookie("session", "4930456C-C718-476F-971F-CB8E047AB349")
            )
            .withQueryStringParameters(
                param("cartId", "055CA455-1DF7-45BB-8535-4F83E7266092")
            )
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "method": "GET",
        "path": "/view/cart",
        "queryStringParameters": {
            "cartId": ["055CA455-1DF7-45BB-8535-4F83E7266092"]
        },
        "cookies": {
            "session": "4930456C-C718-476F-971F-CB8E047AB349"
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
  "httpRequest" : {
    "method" : "GET",
    "path" : "/view/cart",
    "queryStringParameters" : {
      "cartId" : [ "055CA455-1DF7-45BB-8535-4F83E7266092" ]
    },
    "cookies" : {
      "session" : "4930456C-C718-476F-971F-CB8E047AB349"
    }
  },
  "httpResponse" : {
    "body" : "some_response_body"
  }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

match request by cookie and query parameter with json schema values

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withMethod("GET")
            .withPath("/view/cart")
            .withQueryStringParameters(
                schemaParam("cartId", "{ \"type\": \"string\", \"format\": \"uuid\" }")
            )
            .withCookies(
                schemaCookie("session", "{ \"type\": \"string\", \"format\": \"uuid\" }")
            )
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "method": "GET",
        "path": "/view/cart",
        "queryStringParameters": {
            "cartId": [{
                "schema": {
                    "type": "string",
                    "format": "uuid"
                }
            }]
        },
        "cookies": {
            "session": {
                "schema": {
                    "type": "string",
                    "format": "uuid"
                }
            }
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
  "httpRequest" : {
    "method" : "GET",
    "path" : "/view/cart",
    "queryStringParameters" : {
      "cartId" : [ "055CA455-1DF7-45BB-8535-4F83E7266092" ]
    },
    "cookies" : {
      "session" : "4930456C-C718-476F-971F-CB8E047AB349"
    }
  },
  "httpResponse" : {
    "body" : "some_response_body"
  }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

match request by optional cookie

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/view/cart")
            .withCookies(
                optionalCookie("session", schemaString("{ \"type\": \"string\", \"format\": \"uuid\" }"))
            )
            .withQueryStringParameters(
                schemaParam("cartId", "{ \"type\": \"string\", \"format\": \"uuid\" }")
            )
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/view/cart",
        "queryStringParameters": {
            "cartId": [{
                "schema": {
                    "type": "string",
                    "format": "uuid"
                }
            }]
        },
        "cookies": {
            "?session": {
                "schema": {
                    "type": "string",
                    "format": "uuid"
                }
            }
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "path": "/view/cart",
        "queryStringParameters": {
            "cartId": [{
                "schema": {
                    "type": "string",
                    "format": "uuid"
                }
            }]
        },
        "cookies": {
            "?session": {
                "schema": {
                    "type": "string",
                    "format": "uuid"
                }
            }
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

match request by body sub-string

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withBody(subString("some_string"))
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "body": {
            "type": "STRING",
            "string": "some_string",
            "subString": true
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
  "httpRequest" : {
    "body" : {
      "type": "STRING",
      "string": "some_string",
      "subString": true
    }
  },
  "httpResponse" : {
    "body" : "some_response_body"
  }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

match request by body in utf16

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withBody(exact("æè¯´ä¸­å½è¯", Charsets.UTF_16))
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "body": {
            "type": "STRING",
            "string": "æè¯´ä¸­å½è¯",
            "contentType": "text/plain; charset=utf-16"
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
  "httpRequest" : {
    "body" : {
      "type" : "STRING",
      "string" : "æè¯´ä¸­å½è¯",
      "contentType" : "text/plain; charset=utf-16"
    }
  },
  "httpResponse" : {
    "body" : "some_response_body"
  }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

match request by regex body

For details of the full regex syntax supported please see [the JDK documentation](https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html).

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withBody(regex("starts_with_.*"))
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "body": {
            "type": "REGEX",
            "regex": "starts_with_.*"
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
  "httpRequest": {
    "body": {
      "type": "REGEX",
      "regex": "starts_with_.*"
    }
  },
  "httpResponse" : {
    "body" : "some_response_body"
  }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

match request by form submission body

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withMethod("POST")
            .withHeaders(
                header("Content-Type", "application/x-www-form-urlencoded")
            )
            .withBody(
                params(
                    param("email", "joe.blogs@gmail.com"),
                    param("password", "secure_Password123")
                )
            )
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "method": "POST",
        "headers": {
            "Content-Type": ["application/x-www-form-urlencoded"]
        },
        "body": {
            "type": "PARAMETERS",
            "parameters": {
                "email": ["joe.blogs@gmail.com"],
                "password": ["secure_Password123"]
            }
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
  "httpRequest" : {
    "method" : "POST",
    "headers" : {
      "Content-Type" : [ "application/x-www-form-urlencoded" ]
    },
    "body" : {
      "type" : "PARAMETERS",
      "parameters" : {
        "email" : [ "joe.blogs@gmail.com" ],
        "password" : [ "secure_Password123" ]
      }
    }
  },
  "httpResponse" : {
    "body" : "some_response_body"
  }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

match request by body with xpath

Matches if at least one value is returned by the JsonPath expression

For a quick summary the XPath syntax please see [w3schools](https://www.w3schools.com/xml/xpath_syntax.asp), for details of the full XPath syntax please see [www.w3.org](https://www.w3.org/TR/1999/REC-xpath-19991116/#path-abbrev)

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            // matches any request with an XML body that contains
            // one or more elements that match the XPath expression
            .withBody(
                xpath("/bookstore/book[price>30]/price")
            )
    )
    .respond(
        response()
            .withBody("some_response_body")
    );

// matches a request with the following body:
/*
<?xml version="1.0" encoding="ISO-8859-1"?>
<bookstore>
  <book category="COOKING">
    <title lang="en">Everyday Italian</title>
    <author>Giada De Laurentiis</author>
    <year>2005</year>
    <price>30.00</price>
  </book>
  <book category="CHILDREN">
    <title lang="en">Harry Potter</title>
    <author>J K. Rowling</author>
    <year>2005</year>
    <price>29.99</price>
  </book>
  <book category="WEB">
    <title lang="en">Learning XML</title>
    <author>Erik T. Ray</author>
    <year>2003</year>
    <price>31.95</price>
  </book>
</bookstore>
 */
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "body": {
            // matches any request with an XML body that contains
            // one or more elements that match the XPath expression
            "type": "XPATH",
            "xpath": "/bookstore/book[price>30]/price"
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
});

// matches a request with the following body:
/*
<?xml version="1.0" encoding="ISO-8859-1"?>
<bookstore>
  <book category="COOKING">
    <title lang="en">Everyday Italian</title>
    <author>Giada De Laurentiis</author>
    <year>2005</year>
    <price>30.00</price>
  </book>
  <book category="CHILDREN">
    <title lang="en">Harry Potter</title>
    <author>J K. Rowling</author>
    <year>2005</year>
    <price>29.99</price>
  </book>
  <book category="WEB">
    <title lang="en">Learning XML</title>
    <author>Erik T. Ray</author>
    <year>2003</year>
    <price>31.95</price>
  </book>
</bookstore>
 */
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
  "httpRequest" : {
    "body" : {
      "type" : "XPATH",
      "xpath" : "/bookstore/book[price>30]/price"
    }
  },
  "httpResponse" : {
    "body" : "some_response_body"
  }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

match request by not matching body with xpath

Matches if at least one value is returned by the JsonPath expression

For a quick summary the XPath syntax please see [w3schools](https://www.w3schools.com/xml/xpath_syntax.asp), for details of the full XPath syntax please see [www.w3.org](https://www.w3.org/TR/1999/REC-xpath-19991116/#path-abbrev)

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withBody(
                // matches any request with an XML body that does NOT
                // contain one or more elements that match the XPath expression
                not(xpath("/bookstore/book[price>30]/price"))
            )
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "body": {
            // matches any request with an XML body that does NOT
            // contain one or more elements that match the XPath expression
            "not": true,
            "type": "XPATH",
            "xpath": "/bookstore/book[price>30]/price"
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
  "httpRequest" : {
    "body" : {
      "not" : true,
      "type" : "XPATH",
      "xpath" : "/bookstore/book[price>30]/price"
    }
  },
  "httpResponse" : {
    "body" : "some_response_body"
  }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

match request by body with xml

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withBody(
                xml("<bookstore>" + System.lineSeparator() +
                    "   <book nationality=\"ITALIAN\" category=\"COOKING\">" + System.lineSeparator() +
                    "       <title lang=\"en\">Everyday Italian</title>" + System.lineSeparator() +
                    "       <author>Giada De Laurentiis</author>" + System.lineSeparator() +
                    "       <year>2005</year>" + System.lineSeparator() +
                    "       <price>30.00</price>" + System.lineSeparator() +
                    "   </book>" + System.lineSeparator() +
                    "</bookstore>")
            )
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "body": {
            "type": "XML",
            "xml":  "<bookstore>\n" +
                    "   <book nationality=\"ITALIAN\" category=\"COOKING\">\n" +
                    "       <title lang=\"en\">Everyday Italian</title>\n" +
                    "       <author>Giada De Laurentiis</author>\n" +
                    "       <year>2005</year>\n" +
                    "       <price>30.00</price>\n" +
                    "   </book>\n" +
                    "</bookstore>"
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
  "httpRequest" : {
    "body" : {
      "type" : "XML",
      "xml" : "<bookstore> <book nationality=\"ITALIAN\" category=\"COOKING\"><title lang=\"en\">Everyday Italian</title><author>Giada De Laurentiis</author><year>2005</year><price>30.00</price></book> </bookstore>"
    }
  },
  "httpResponse" : {
    "body" : "some_response_body"
  }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

match request by body with xml using placeholders

See [XMLUnit documentation](https://github.com/xmlunit/user-guide/wiki/Placeholders) for full details of supported placeholders.

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withBody(
                xml("<bookstore>" + System.lineSeparator() +
                    "   <book nationality=\"ITALIAN\" category=\"COOKING\">" + System.lineSeparator() +
                    "       <title lang=\"en\">Everyday Italian</title>" + System.lineSeparator() +
                    "       <author>${xmlunit.ignore}</author>" + System.lineSeparator() +
                    "       <year>${xmlunit.isNumber}</year>" + System.lineSeparator() +
                    "       <price>30.00</price>" + System.lineSeparator() +
                    "   </book>" + System.lineSeparator() +
                    "</bookstore>")
            )
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest" : {
        "body" : {
            "type" : "XML",
            "xml" : "<bookstore>\n" +
                "   <book nationality=\"ITALIAN\" category=\"COOKING\">\n" +
                "       <title lang=\"en\">Everyday Italian</title>\n" +
                "       <author>${xmlunit.ignore}</author>\n" +
                "       <year>${xmlunit.isNumber}</year>\n" +
                "       <price>30.00</price>\n" +
                "   </book>\n" +
                "</bookstore>"
        }
    },
    "httpResponse" : {
        "body" : "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest" : {
        "body" : {
            "type" : "XML",
            "xml" : "<bookstore>\n   <book nationality=\"ITALIAN\" category=\"COOKING\">\n       <title lang=\"en\">Everyday Italian</title>\n       <author>${xmlunit.ignore}</author>\n       <year>${xmlunit.isNumber}</year>\n       <price>30.00</price>\n   </book>\n</bookstore>"
        }
    },
    "httpResponse" : {
        "body" : "some_response_body"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

match request by body with xml schema

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withBody(
                xmlSchema("<?xml version=\"1.0\" encoding=\"UTF-8\"?>" + System.lineSeparator() +
                    "<xs:schema xmlns:xs=\"http://www.w3.org/2001/XMLSchema\" elementFormDefault=\"qualified\" attributeFormDefault=\"unqualified\">" + System.lineSeparator() +
                    "    <!-- XML Schema Generated from XML Document on Wed Jun 28 2017 21:52:45 GMT+0100 (BST) -->" + System.lineSeparator() +
                    "    <!-- with XmlGrid.net Free Online Service http://xmlgrid.net -->" + System.lineSeparator() +
                    "    <xs:element name=\"notes\">" + System.lineSeparator() +
                    "        <xs:complexType>" + System.lineSeparator() +
                    "            <xs:sequence>" + System.lineSeparator() +
                    "                <xs:element name=\"note\" maxOccurs=\"unbounded\">" + System.lineSeparator() +
                    "                    <xs:complexType>" + System.lineSeparator() +
                    "                        <xs:sequence>" + System.lineSeparator() +
                    "                            <xs:element name=\"to\" minOccurs=\"1\" maxOccurs=\"1\" type=\"xs:string\"></xs:element>" + System.lineSeparator() +
                    "                            <xs:element name=\"from\" minOccurs=\"1\" maxOccurs=\"1\" type=\"xs:string\"></xs:element>" + System.lineSeparator() +
                    "                            <xs:element name=\"heading\" minOccurs=\"1\" maxOccurs=\"1\" type=\"xs:string\"></xs:element>" + System.lineSeparator() +
                    "                            <xs:element name=\"body\" minOccurs=\"1\" maxOccurs=\"1\" type=\"xs:string\"></xs:element>" + System.lineSeparator() +
                    "                        </xs:sequence>" + System.lineSeparator() +
                    "                    </xs:complexType>" + System.lineSeparator() +
                    "                </xs:element>" + System.lineSeparator() +
                    "            </xs:sequence>" + System.lineSeparator() +
                    "        </xs:complexType>" + System.lineSeparator() +
                    "    </xs:element>" + System.lineSeparator() +
                    "</xs:schema>")
            )
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "body": {
            "type": "XML_SCHEMA",
            "xmlSchema": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<xs:schema xmlns:xs=\"http://www.w3.org/2001/XMLSchema\" elementFormDefault=\"qualified\" attributeFormDefault=\"unqualified\">\n" +
            "    <!-- XML Schema Generated from XML Document on Wed Jun 28 2017 21:52:45 GMT+0100 (BST) -->\n" +
            "    <!-- with XmlGrid.net Free Online Service http://xmlgrid.net -->\n" +
            "    <xs:element name=\"notes\">\n" +
            "        <xs:complexType>\n" +
            "            <xs:sequence>\n" +
            "                <xs:element name=\"note\" maxOccurs=\"unbounded\">\n" +
            "                    <xs:complexType>\n" +
            "                        <xs:sequence>\n" +
            "                            <xs:element name=\"to\" minOccurs=\"1\" maxOccurs=\"1\" type=\"xs:string\"></xs:element>\n" +
            "                            <xs:element name=\"from\" minOccurs=\"1\" maxOccurs=\"1\" type=\"xs:string\"></xs:element>\n" +
            "                            <xs:element name=\"heading\" minOccurs=\"1\" maxOccurs=\"1\" type=\"xs:string\"></xs:element>\n" +
            "                            <xs:element name=\"body\" minOccurs=\"1\" maxOccurs=\"1\" type=\"xs:string\"></xs:element>\n" +
            "                        </xs:sequence>\n" +
            "                    </xs:complexType>\n" +
            "                </xs:element>\n" +
            "            </xs:sequence>\n" +
            "        </xs:complexType>\n" +
            "    </xs:element>\n</xs:schema>"
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
  "httpRequest" : {
    "body" : {
      "type" : "XML_SCHEMA",
      "xmlSchema" : "<?xml version=\"1.0\" encoding=\"UTF-8\"?> <xs:schema xmlns:xs=\"http://www.w3.org/2001/XMLSchema\" elementFormDefault=\"qualified\" attributeFormDefault=\"unqualified\"> <xs:element name=\"notes\"> <xs:complexType> <xs:sequence> <xs:element name=\"note\" maxOccurs=\"unbounded\"> <xs:complexType> <xs:sequence> <xs:element name=\"to\" minOccurs=\"1\" maxOccurs=\"1\" type=\"xs:string\"></xs:element> <xs:element name=\"from\" minOccurs=\"1\" maxOccurs=\"1\" type=\"xs:string\"></xs:element> <xs:element name=\"heading\" minOccurs=\"1\" maxOccurs=\"1\" type=\"xs:string\"></xs:element> <xs:element name=\"body\" minOccurs=\"1\" maxOccurs=\"1\" type=\"xs:string\"></xs:element> </xs:sequence> </xs:complexType> </xs:element> </xs:sequence> </xs:complexType> </xs:element> </xs:schema>"
    }
  },
  "httpResponse" : {
    "body" : "some_response_body"
  }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

match request by body with xml schema by classpath

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withBody(
                xmlSchemaFromResource("org/mockserver/examples/mockserver/testXmlSchema.xsd")
            )
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

match request by body with json exactly

JSON body matcher supports two mode **STRICT** which matches all fields, order of arrays and no additional fields allowed, and **ONLY\_MATCHING\_FIELDS** which only matches fields provided in the request
matcher.

When matching JSON arrays the number of elements in the array must always match, however if **ONLY\_MATCHING\_FIELDS** mode is specified only the fields in the each array element in the matcher will be matched against each
corresponding object in the array.

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withBody(
                json("{" + System.lineSeparator() +
                        "    \"id\": 1," + System.lineSeparator() +
                        "    \"name\": \"A green door\"," + System.lineSeparator() +
                        "    \"price\": 12.50," + System.lineSeparator() +
                        "    \"tags\": [\"home\", \"green\"]" + System.lineSeparator() +
                        "}",
                    MatchType.STRICT
                )
            )
    )
    .respond(
        response()
            .withStatusCode(HttpStatusCode.ACCEPTED_202.code())
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "body": {
            "type": "JSON",
            "json": {
                "id": 1,
                "name": "A green door",
                "price": 12.50,
                "tags": ["home", "green"]
            },
            "matchType": "STRICT"
        }
    },
    "httpResponse": {
        "statusCode": 202,
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "body": {
            "type": "JSON",
            "json": {
                "id": 1,
                "name": "A green door",
                "price": 12.50,
                "tags": ["home", "green"]
            },
            "matchType": "STRICT"
        }
    },
    "httpResponse": {
        "statusCode": 202,
        "body": "some_response_body"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

match request by body with json ignoring extra fields

JSON body matcher supports two mode **STRICT** which matches all fields, order of arrays and no additional fields allowed, and **ONLY\_MATCHING\_FIELDS** which only matches fields provided in the request
matcher.

When matching JSON arrays the number of elements in the array must always match, however if **ONLY\_MATCHING\_FIELDS** mode is specified only the fields in the each array element in the matcher will be matched against each
corresponding object in the array.

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withBody(
                json("{" + System.lineSeparator() +
                        "    \"id\": 1," + System.lineSeparator() +
                        "    \"name\": \"A green door\"," + System.lineSeparator() +
                        "    \"price\": 12.50," + System.lineSeparator() +
                        "    \"tags\": [\"home\", \"green\"]" + System.lineSeparator() +
                        "}",
                    MatchType.ONLY_MATCHING_FIELDS
                )
            )
    )
    .respond(
        response()
            .withStatusCode(HttpStatusCode.ACCEPTED_202.code())
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "body": {
            "id": 1,
            "name": "A green door",
            "price": 12.50,
            "tags": ["home", "green"]
        }
    },
    "httpResponse": {
        "statusCode": 202,
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "body": {
            "id": 1,
            "name": "A green door",
            "price": 12.50,
            "tags": ["home", "green"]
        }
    },
    "httpResponse": {
        "statusCode": 202,
        "body": "some_response_body"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

match request by body with json ignoring extra fields in array objects

JSON body matcher supports two mode **STRICT** which matches all fields, order of arrays and no additional fields allowed, and **ONLY\_MATCHING\_FIELDS** which only matches fields provided in the request
matcher.

When matching JSON arrays the number of elements in the array must always match, however if **ONLY\_MATCHING\_FIELDS** mode is specified only the fields in the each array element in the matcher will be matched against each
corresponding object in the array.

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withBody(
                json(
                    "{\"context\": [{\"source\": \"DECISION_REQUEST\"},{\"source\": \"DECISION_REQUEST\"},{\"source\": \"DECISION_REQUEST\"}]}",
                    MatchType.ONLY_MATCHING_FIELDS
                )
            )
    )
    .respond(
        response()
            .withStatusCode(HttpStatusCode.ACCEPTED_202.code())
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "method": "POST",
        "path": "/json",
        "body": {
            "type": "JSON",
            "json": {
                "context": [
                    {
                        "source": "DECISION_REQUEST"
                    },
                    {
                        "source": "DECISION_REQUEST"
                    },
                    {
                        "source": "DECISION_REQUEST"
                    }
                ]
            },
            "matchType": "ONLY_MATCHING_FIELDS"
        }
    },
    "httpResponse": {
        "statusCode": 200,
        "body": "some response"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "method": "POST",
        "path": "/json",
        "body": {
            "type": "JSON",
            "json": {
                "context": [
                    {
                        "source": "DECISION_REQUEST"
                    },
                    {
                        "source": "DECISION_REQUEST"
                    },
                    {
                        "source": "DECISION_REQUEST"
                    }
                ]
            },
            "matchType": "ONLY_MATCHING_FIELDS"
        }
    },
    "httpResponse": {
        "statusCode": 200,
        "body": "some response"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

match request by body with json using placeholders

See [JSONUnit documentation](https://github.com/lukas-krecan/JsonUnit) for full details of supported placeholders.

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withBody(
                json("{" + System.lineSeparator() +
                        "    \"id\": 1," + System.lineSeparator() +
                        "    \"name\": \"A green door\"," + System.lineSeparator() +
                        "    \"price\": \"${json-unit.ignore-element}\"," + System.lineSeparator() +
                        "    \"enabled\": \"${json-unit.any-boolean}\"," + System.lineSeparator() +
                        "    \"tags\": [\"home\", \"green\"]" + System.lineSeparator() +
                        "}",
                    MatchType.ONLY_MATCHING_FIELDS
                )
            )
    )
    .respond(
        response()
            .withStatusCode(HttpStatusCode.ACCEPTED_202.code())
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest" : {
        "body" : {
            "type" : "JSON",
            "json" : {
                "id" : 1,
                "name" : "A green door",
                "price" : "${json-unit.ignore-element}",
                "enabled" : "${json-unit.any-boolean}",
                "tags" : [ "home", "green" ]
            }
        }
    },
    "httpResponse" : {
        "statusCode" : 202,
        "body" : "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest" : {
        "body" : {
            "type" : "JSON",
            "json" : {
                "id" : 1,
                "name" : "A green door",
                "price" : "${json-unit.ignore-element}",
                "enabled" : "${json-unit.any-boolean}",
                "tags" : [ "home", "green" ]
            }
        }
    },
    "httpResponse" : {
        "statusCode" : 202,
        "body" : "some_response_body"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

match request by body with json schema

For details of the full json schema supported please see [json-schema.org](https://json-schema.org/).

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withBody(
                jsonSchema("{" + System.lineSeparator() +
                    "    \"$schema\": \"https://json-schema.org/draft-04/schema#\"," + System.lineSeparator() +
                    "    \"title\": \"Product\"," + System.lineSeparator() +
                    "    \"description\": \"A product from Acme catalog\"," + System.lineSeparator() +
                    "    \"type\": \"object\"," + System.lineSeparator() +
                    "    \"properties\": {" + System.lineSeparator() +
                    "        \"id\": {" + System.lineSeparator() +
                    "            \"description\": \"The unique identifier for a product\"," + System.lineSeparator() +
                    "            \"type\": \"integer\"" + System.lineSeparator() +
                    "        }," + System.lineSeparator() +
                    "        \"name\": {" + System.lineSeparator() +
                    "            \"description\": \"Name of the product\"," + System.lineSeparator() +
                    "            \"type\": \"string\"" + System.lineSeparator() +
                    "        }," + System.lineSeparator() +
                    "        \"price\": {" + System.lineSeparator() +
                    "            \"type\": \"number\"," + System.lineSeparator() +
                    "            \"minimum\": 0," + System.lineSeparator() +
                    "            \"exclusiveMinimum\": true" + System.lineSeparator() +
                    "        }," + System.lineSeparator() +
                    "        \"tags\": {" + System.lineSeparator() +
                    "            \"type\": \"array\"," + System.lineSeparator() +
                    "            \"items\": {" + System.lineSeparator() +
                    "                \"type\": \"string\"" + System.lineSeparator() +
                    "            }," + System.lineSeparator() +
                    "            \"minItems\": 1," + System.lineSeparator() +
                    "            \"uniqueItems\": true" + System.lineSeparator() +
                    "        }" + System.lineSeparator() +
                    "    }," + System.lineSeparator() +
                    "    \"required\": [\"id\", \"name\", \"price\"]" + System.lineSeparator() +
                    "}"))
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "body": {
            "type": "JSON_SCHEMA",
            "jsonSchema": {
                "$schema": "https://json-schema.org/draft-04/schema#",
                "title": "Product",
                "description": "A product from Acme catalog",
                "type": "object",
                "properties": {
                    "id": {
                        "description": "The unique identifier for a product",
                        "type": "integer"
                    },
                    "name": {
                        "description": "Name of the product",
                        "type": "string"
                    },
                    "price": {
                        "type": "number",
                        "minimum": 0,
                        "exclusiveMinimum": true
                    },
                    "tags": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        },
                        "minItems": 1,
                        "uniqueItems": true
                    }
                },
                "required": [
                    "id",
                    "name",
                    "price"
                ]
            }
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "body": {
            "type": "JSON_SCHEMA",
            "jsonSchema": {
                "$schema": "https://json-schema.org/draft-04/schema#",
                "title": "Product",
                "description": "A product from Acme catalog",
                "type": "object",
                "properties": {
                    "id": {
                        "description": "The unique identifier for a product",
                        "type": "integer"
                    },
                    "name": {
                        "description": "Name of the product",
                        "type": "string"
                    },
                    "price": {
                        "type": "number",
                        "minimum": 0,
                        "exclusiveMinimum": true
                    },
                    "tags": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        },
                        "minItems": 1,
                        "uniqueItems": true
                    }
                },
                "required": [
                    "id",
                    "name",
                    "price"
                ]
            }
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

match request by body with jsonpath

Matches if at least one value is returned by the JsonPath expression. For details of the full JsonPath supported please see [github.com/json-path/JsonPath](https://github.com/json-path/JsonPath).

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withBody(
                // matches any request with an JSON body that contain
                // one or more fields that match the JsonPath expression
                jsonPath("$.store.book[?(@.price < 10)]")
            )
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "body": {
            // matches any request with an JSON body that contain
            // one or more fields that match the JsonPath expression
            "type": "JSON_PATH",
            "jsonPath": "$.store.book[?(@.price < 10)]"
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
  "httpRequest" : {
    "body" : {
      "type": "JSON_PATH",
      "jsonPath": "$.store.book[?(@.price < 10)]"
    }
  },
  "httpResponse" : {
    "body" : "some_response_body"
  }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

match request by not matching body with JsonPath

Matches if at least one value is returned by the JsonPath expression. For details of the full JsonPath supported please see [github.com/json-path/JsonPath](https://github.com/json-path/JsonPath).

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withBody(
                // matches any request with an JSON body that does NOT contain
                // one or more fields that match the JsonPath expression
                not(jsonPath("$.store.book[?(@.price < 10)]"))
            )
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "body": {
            // matches any request with an JSON body that does NOT contain
            // one or more fields that match the JsonPath expression
            "not": true,
            "type": "JSON_PATH",
            "jsonPath": "$.store.book[?(@.price < 10)]"
        }
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
  "httpRequest" : {
    "body" : {
      "not": true,
      "type": "JSON_PATH",
      "jsonPath": "$.store.book[?(@.price < 10)]"
    }
  },
  "httpResponse" : {
    "body" : "some_response_body"
  }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

match request with binary PNG body

Java

```
byte[] pngBytes = IOUtils.toByteArray(getClass().getClassLoader().getResourceAsStream("org/mockserver/examples/mockserver/test.png"));
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withMethod("POST")
            .withHeaders(
                header("content-type", "image/png"),
                header("content-disposition", "form-data; name=\"test.png\"; filename=\"test.png\"")
            )
            .withBody(binary(pngBytes))
    )
    .respond(
        response()
            .withBody("png_saved_response")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "method": "POST"
        "headers": {
            "content-type": ["image/png"],
            "content-disposition": ["form-data; name=\"test.png\"; filename=\"test.png\""]
        },
        "body": {
            "type": "BINARY",
            "base64Bytes": "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"
        }
    },
    "httpResponse" : {
        "body" : "png_saved_response"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "method": "POST"
        "headers": {
            "content-type": ["image/png"],
            "content-disposition": ["form-data; name=\"test.png\"; filename=\"test.png\""]
        },
        "body": {
            "type": "BINARY",
            "base64Bytes": "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"
        }
    },
    "httpResponse" : {
        "body" : "png_saved_response"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

update expectation by id

Java

```
new MockServerClient("localhost", 1080)
    .upsert(
        new Expectation(
            request().withPath("/some/path"),
            Times.once(),
            TimeToLive.exactly(TimeUnit.SECONDS, 60L),
            100
        )
        .withId("some_unique_id")
        .thenRespond(response().withBody("some_response_body"))
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "id": "some_unique_id",
    "httpRequest": {
        "path": "/some/path"
    },
    "httpResponse": {
        "body": "some_response_body"
    },
    "times": {
        "remainingTimes": 1,
        "unlimited": false
    },
    "timeToLive": {
        "timeUnit": "SECONDS",
        "timeToLive": 60,
        "unlimited": false
    },
    "priority" : 100
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
  "id": "some_unique_id",
  "httpRequest" : {
    "path" : "/some/path"
  },
  "httpResponse" : {
    "body" : "some_response_body"
  },
  "times" : {
    "remainingTimes" : 1,
    "unlimited" : false
  },
  "timeToLive" : {
    "timeUnit" : "SECONDS",
    "timeToLive" : 60,
    "unlimited" : false
  },
  "priority" : 100
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

An **open api request matcher** can contain any of the following fields:

* **specUrlOrPayload** - mandatory value containing an [**OpenAPI v3**](https://swagger.io/docs/specification/basic-structure/) specifications in either JSON or YAML format as an:
  * **[HTTP/HTTPS URL](#button_match_by_openapi_url)**
  * **[File URL](#button_match_by_openapi_filepath)**
  * **[classpath location](#button_match_by_openapi_classpath)** (without the classpath: scheme)
  * **[inline JSON object](#button_match_by_inline_openapi_json)**
  * **[inline escaped YAML string](#button_match_by_inline_openapi_yaml)**
* **operationId** - optional value that specifies which [operation](#button_match_by_openapi_url_and_operation) to match against, if [empty or null](#button_match_by_openapi_url) all operations are
  matched against

MockServer creates a set of **[request properties matchers](#request_properties_matchers)** for each **open api request matcher**, to ensures control-plane logic such as [clearing expectations](/mock_server/clearing_and_resetting.html) or [retrieving expectations](/mock_server/debugging_issues.html) work consistently between the two types of request matchers, this can be viewed in
the [MockServer UI](/mock_server/mockserver_ui.html) [active expectations](/mock_server/mockserver_ui.html#active_expectations) section.

**OpenAPI Request Matcher Code Examples**

The following code examples show how to match request using an Open API specification. For more examples see the [code examples folder](https://github.com/mock-server/mockserver/tree/master/mockserver-examples) in the git repository.

For brevity static imports have not been included in the Java code examples so please add the following static imports if copying this code

```
import static org.mockserver.model.HttpRequest.request;
import static org.mockserver.model.HttpResponse.response;
```

match request by openapi loaded by http url

Java

```
new MockServerClient("localhost", 1080)
    .when(
        openAPI(
            "https://raw.githubusercontent.com/mock-server/mockserver/master/mockserver-integration-testing/src/main/resources/org/mockserver/openapi/openapi_petstore_example.json"
        )
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "specUrlOrPayload": "https://raw.githubusercontent.com/mock-server/mockserver/master/mockserver-integration-testing/src/main/resources/org/mockserver/openapi/openapi_petstore_example.json"
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "specUrlOrPayload": "https://raw.githubusercontent.com/mock-server/mockserver/master/mockserver-integration-testing/src/main/resources/org/mockserver/openapi/openapi_petstore_example.json"
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

match request by openapi operation

Java

```
new MockServerClient("localhost", 1080)
    .when(
        openAPI(
            "https://raw.githubusercontent.com/mock-server/mockserver/master/mockserver-integration-testing/src/main/resources/org/mockserver/openapi/openapi_petstore_example.json",
            "showPetById"
        )
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "specUrlOrPayload": "https://raw.githubusercontent.com/mock-server/mockserver/master/mockserver-integration-testing/src/main/resources/org/mockserver/openapi/openapi_petstore_example.json",
        "operationId": "showPetById"
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "specUrlOrPayload": "https://raw.githubusercontent.com/mock-server/mockserver/master/mockserver-integration-testing/src/main/resources/org/mockserver/openapi/openapi_petstore_example.json",
        "operationId": "showPetById"
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

match request by openapi loaded by file url

Java

```
new MockServerClient("localhost", 1080)
    .when(
        openAPI(
            "file:/Users/jamesbloom/git/mockserver/mockserver/mockserver-core/target/test-classes/org/mockserver/openapi/openapi_petstore_example.json"
        )
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "specUrlOrPayload": "file:/Users/jamesbloom/git/mockserver/mockserver/mockserver-core/target/test-classes/org/mockserver/openapi/openapi_petstore_example.json"
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "specUrlOrPayload": "file:/Users/jamesbloom/git/mockserver/mockserver/mockserver-core/target/test-classes/org/mockserver/openapi/openapi_petstore_example.json"
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

match request by openapi loaded by classpath location

Java

```
new MockServerClient("localhost", 1080)
    .when(
        openAPI(
            "org/mockserver/openapi/openapi_petstore_example.json"
        )
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "specUrlOrPayload": "org/mockserver/openapi/openapi_petstore_example.json"
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "specUrlOrPayload": "org/mockserver/openapi/openapi_petstore_example.json"
    },
    "httpResponse": {
        "body": "some_response_body"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

match request by openapi loaded by json string literal

Java

```
new MockServerClient("localhost", 1080)
    .when(
        new OpenAPIDefinition()
            .withSpecUrlOrPayload(
                FileReader.readFileFromClassPathOrPath("/Users/jamesbloom/git/mockserver/mockserver/mockserver-core/target/test-classes/org/mockserver/openapi/openapi_petstore_example.json")
            )
            .withOperationId("listPets")
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var fs = require('fs');
try {
    var mockServerClient = require('mockserver-client').mockServerClient;
    mockServerClient("localhost", 1080).mockAnyResponse({
        "httpRequest": {
            "specUrlOrPayload": fs.readFileSync("/Users/jamesbloom/git/mockserver/mockserver/mockserver-core/target/test-classes/org/mockserver/openapi/openapi_petstore_example.json", "utf8"),
            "operationId": "showPetById"
        },
        "httpResponse": {
            "body": "some_response_body"
        }
    }).then(
        function () {
            console.log("expectation created");
        },
        function (error) {
            console.log(error);
        }
    );
} catch(e) {
    console.log('Error:', e.stack);
}
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API using cat

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d "{
    \"httpRequest\": {
        \"specUrlOrPayload\": `cat /Users/jamesbloom/git/mockserver/mockserver/mockserver-core/target/test-classes/org/mockserver/openapi/openapi_petstore_example.json`
    },
    \"httpResponse\": {
        \"body\": \"some_response_body\"
    }
}"
```

REST API inline json

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest" : {
      "specUrlOrPayload" : {
        "openapi" : "3.0.0",
        "info" : {
          "version" : "1.0.0",
          "title" : "Swagger Petstore",
          "license" : {
            "name" : "MIT"
          }
        },
        "servers" : [ {
          "url" : "http://petstore.swagger.io/v1"
        } ],
        "paths" : {
          "/pets" : {
            "get" : {
              "summary" : "List all pets",
              "operationId" : "listPets",
              "tags" : [ "pets" ],
              "parameters" : [ {
                "name" : "limit",
                "in" : "query",
                "description" : "How many items to return at one time (max 100)",
                "required" : false,
                "schema" : {
                  "type" : "integer",
                  "format" : "int32"
                }
              } ],
              "responses" : {
                "200" : {
                  "description" : "A paged array of pets",
                  "headers" : {
                    "x-next" : {
                      "description" : "A link to the next page of responses",
                      "schema" : {
                        "type" : "string"
                      }
                    }
                  },
                  "content" : {
                    "application/json" : {
                      "schema" : {
                        "$ref" : "#/components/schemas/Pets"
                      }
                    }
                  }
                },
                "500" : {
                  "description" : "unexpected error",
                  "content" : {
                    "application/json" : {
                      "schema" : {
                        "$ref" : "#/components/schemas/Error"
                      }
                    }
                  }
                },
                "default" : {
                  "description" : "unexpected error",
                  "content" : {
                    "application/json" : {
                      "schema" : {
                        "$ref" : "#/components/schemas/Error"
                      }
                    }
                  }
                }
              }
            },
            "post" : {
              "summary" : "Create a pet",
              "operationId" : "createPets",
              "tags" : [ "pets" ],
              "requestBody" : {
                "description" : "a pet",
                "required" : true,
                "content" : {
                  "application/json" : {
                    "schema" : {
                      "$ref" : "#/components/schemas/Pet"
                    }
                  },
                  "*/*" : {
                    "schema" : {
                      "$ref" : "#/components/schemas/Pet"
                    }
                  }
                }
              },
              "responses" : {
                "201" : {
                  "description" : "Null response"
                },
                "400" : {
                  "description" : "unexpected error",
                  "content" : {
                    "application/json" : {
                      "schema" : {
                        "$ref" : "#/components/schemas/Error"
                      }
                    }
                  }
                },
                "500" : {
                  "description" : "unexpected error",
                  "content" : {
                    "application/json" : {
                      "schema" : {
                        "$ref" : "#/components/schemas/Error"
                      }
                    }
                  }
                },
                "default" : {
                  "description" : "unexpected error",
                  "content" : {
                    "application/json" : {
                      "schema" : {
                        "$ref" : "#/components/schemas/Error"
                      }
                    }
                  }
                }
              }
            }
          },
          "/pets/{petId}" : {
            "get" : {
              "summary" : "Info for a specific pet",
              "operationId" : "showPetById",
              "tags" : [ "pets" ],
              "parameters" : [ {
                "name" : "petId",
                "in" : "path",
                "required" : true,
                "description" : "The id of the pet to retrieve",
                "schema" : {
                  "type" : "string"
                }
              }, {
                "in" : "header",
                "name" : "X-Request-ID",
                "schema" : {
                  "type" : "string",
                  "format" : "uuid"
                },
                "required" : true
              } ],
              "responses" : {
                "200" : {
                  "description" : "Expected response to a valid request",
                  "content" : {
                    "application/json" : {
                      "schema" : {
                        "$ref" : "#/components/schemas/Pet"
                      }
                    }
                  }
                },
                "400" : {
                  "description" : "unexpected error",
                  "content" : {
                    "application/json" : {
                      "schema" : {
                        "$ref" : "#/components/schemas/Error"
                      }
                    }
                  }
                },
                "500" : {
                  "description" : "unexpected error",
                  "content" : {
                    "application/json" : {
                      "schema" : {
                        "$ref" : "#/components/schemas/Error"
                      }
                    }
                  }
                },
                "default" : {
                  "description" : "unexpected error",
                  "content" : {
                    "application/json" : {
                      "schema" : {
                        "$ref" : "#/components/schemas/Error"
                      }
                    }
                  }
                }
              }
            }
          },
          "/some/path" : {
            "get" : {
              "summary" : "Additional request with extra matchers",
              "operationId" : "somePath",
              "tags" : [ "pets" ],
              "parameters" : [ {
                "name" : "limit",
                "in" : "query",
                "description" : "How many items to return at one time (max 100)",
                "required" : false,
                "schema" : {
                  "type" : "integer",
                  "format" : "int32"
                }
              }, {
                "in" : "header",
                "name" : "X-Request-ID",
                "schema" : {
                  "type" : "string",
                  "format" : "uuid"
                },
                "required" : true
              } ],
              "responses" : {
                "200" : {
                  "description" : "Expected response to a valid request",
                  "content" : {
                    "application/json" : {
                      "schema" : {
                        "$ref" : "#/components/schemas/Pet"
                      }
                    }
                  }
                },
                "default" : {
                  "description" : "unexpected error",
                  "content" : {
                    "application/json" : {
                      "schema" : {
                        "$ref" : "#/components/schemas/Error"
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "components" : {
          "schemas" : {
            "Pet" : {
              "type" : "object",
              "required" : [ "id", "name" ],
              "properties" : {
                "id" : {
                  "type" : "integer",
                  "format" : "int64"
                },
                "name" : {
                  "type" : "string"
                },
                "tag" : {
                  "type" : "string"
                }
              }
            },
            "Pets" : {
              "type" : "array",
              "items" : {
                "$ref" : "#/components/schemas/Pet"
              }
            },
            "Error" : {
              "type" : "object",
              "required" : [ "code", "message" ],
              "properties" : {
                "code" : {
                  "type" : "integer",
                  "format" : "int32"
                },
                "message" : {
                  "type" : "string"
                }
              }
            }
          }
        }
      },
      "operationId" : "listPets"
    },
    "httpResponse" : {
      "body" : "some_response_body"
    }
  }'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

match request by openapi loaded by yaml string literal

Java

```
new MockServerClient("localhost", 1080)
    .when(
        new OpenAPIDefinition()
            .withSpecUrlOrPayload(
                "\nopenapi: 3.0.0\ninfo:\n  version: 1.0.0\n  title: Swagger Petstore\n  license:\n    name: MIT\nservers:\n  - url: http://petstore.swagger.io/v1\npaths:\n  /pets:\n    get:\n      summary: List all pets\n      operationId: listPets\n      tags:\n        - pets\n      parameters:\n        - name: limit\n          in: query\n          description: How many items to return at one time (max 100)\n          required: false\n          schema:\n            type: integer\n            format: int32\n      responses:\n        '200':\n          description: A paged array of pets\n          headers:\n            x-next:\n              description: A link to the next page of responses\n              schema:\n                type: string\n              examples:\n                two:\n                  value: \"/pets?query=752cd724e0d7&page=2\"\n                end:\n                  value: \"\"\n          content:\n            application/json:\n              schema:\n                $ref: '#/components/schemas/Pets'\n        '500':\n          description: unexpected error\n          headers:\n            x-code:\n              description: The error code\n              schema:\n                type: integer\n                format: int32\n                example: 90\n          content:\n            application/json:\n              schema:\n                $ref: '#/components/schemas/Error'\n        default:\n          description: unexpected error\n          content:\n            application/json:\n              schema:\n                $ref: '#/components/schemas/Error'\n    post:\n      summary: Create a pet\n      operationId: createPets\n      tags:\n        - pets\n      requestBody:\n        description: a pet\n        required: true\n        content:\n          application/json:\n            schema:\n              $ref: '#/components/schemas/Pet'\n          '*/*':\n            schema:\n              $ref: '#/components/schemas/Pet'\n      responses:\n        '201':\n          description: Null response\n        '400':\n          description: unexpected error\n          content:\n            application/json:\n              schema:\n                $ref: '#/components/schemas/Error'\n        '500':\n          description: unexpected error\n          content:\n            application/json:\n              schema:\n                $ref: '#/components/schemas/Error'\n        default:\n          description: unexpected error\n          content:\n            application/json:\n              schema:\n                $ref: '#/components/schemas/Error'\n  /pets/{petId}:\n    get:\n      summary: Info for a specific pet\n      operationId: showPetById\n      tags:\n        - pets\n      parameters:\n        - name: petId\n          in: path\n          required: true\n          description: The id of the pet to retrieve\n          schema:\n            type: string\n        - in: header\n          name: X-Request-ID\n          schema:\n            type: string\n            format: uuid\n          required: true\n      responses:\n        '200':\n          description: Expected response to a valid request\n          content:\n            application/json:\n              schema:\n                $ref: '#/components/schemas/Pet'\n              examples:\n                Crumble:\n                  value:\n                    id: 2\n                    name: Crumble\n                    tag: dog\n                Boots:\n                  value:\n                    id: 3\n                    name: Boots\n                    tag: cat\n        '500':\n          description: unexpected error\n          content:\n            application/json:\n              schema:\n                $ref: '#/components/schemas/Error'\n        default:\n          description: unexpected error\n          content:\n            application/json:\n              schema:\n                $ref: '#/components/schemas/Error'\ncomponents:\n  schemas:\n    Pet:\n      type: object\n      required:\n        - id\n        - name\n      properties:\n        id:\n          type: integer\n          format: int64\n        name:\n          type: string\n        tag:\n          type: string\n      example:\n        id: 1\n        name: Scruffles\n        tag: dog\n    Pets:\n      type: array\n      items:\n        $ref: '#/components/schemas/Pet'\n    Error:\n      type: object\n      required:\n        - code\n        - message\n      properties:\n        code:\n          type: integer\n          format: int32\n        message:\n          type: string\n",
      "operationId" : "listPets"
    },
    "times" : {
      "unlimited" : true
    },
    "timeToLive" : {
      "unlimited" : true
    },
    "httpResponse" : {
      "body" : "some_response_body"
    }
  }'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

match request by openapi operation exactly twice

Java

```
new MockServerClient("localhost", 1080)
    .when(
        new OpenAPIDefinition()
            .withSpecUrlOrPayload(
               FileReader.readFileFromClassPathOrPath("/Users/jamesbloom/git/mockserver/mockserver/mockserver-core/target/test-classes/org/mockserver/openapi/openapi_petstore_example.json")
            )
            .withOperationId("listPets"),
        Times.exactly(2)
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest":{
        "specUrlOrPayload": "https://raw.githubusercontent.com/mock-server/mockserver/master/mockserver-integration-testing/src/main/resources/org/mockserver/openapi/openapi_petstore_example.json",
        "operationId": "showPetById"
    },
    "httpResponse":{
        "statusCode": 200,
        "body": "some_body"
    },
    "times": {
        "remainingTimes": 2
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest":{
        "specUrlOrPayload": "https://raw.githubusercontent.com/mock-server/mockserver/master/mockserver-integration-testing/src/main/resources/org/mockserver/openapi/openapi_petstore_example.json",
        "operationId": "showPetById"
    },
    "httpResponse":{
        "statusCode": 200,
        "body": "some_body"
    },
    "times": {
        "remainingTimes": 2
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

update expectation by id

Java

```
new MockServerClient("localhost", 1080)
    .upsert(
        new Expectation(
            openAPI(
               "org/mockserver/openapi/openapi_petstore_example.json",
               "showPetById"
            ),
            Times.once(),
            TimeToLive.exactly(TimeUnit.SECONDS, 60L),
            100
        )
        .withId("630a6e5b-9d61-4668-a18f-a0d3df558583")
        .thenRespond(response().withBody("some_response_body"))
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "id": "630a6e5b-9d61-4668-a18f-a0d3df558583",
    "priority": 0,
    "httpRequest":{
        "specUrlOrPayload": "https://raw.githubusercontent.com/mock-server/mockserver/master/mockserver-integration-testing/src/main/resources/org/mockserver/openapi/openapi_petstore_example.json",
        "operationId": "showPetById"
    },
    "httpResponse":{
        "statusCode": 200,
        "body": "some_response_body"
    },
    "times":{
        "unlimited": true
    },
    "timeToLive":{
        "unlimited": true
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "id": "630a6e5b-9d61-4668-a18f-a0d3df558583",
    "priority": 0,
    "httpRequest":{
        "specUrlOrPayload": "https://raw.githubusercontent.com/mock-server/mockserver/master/mockserver-integration-testing/src/main/resources/org/mockserver/openapi/openapi_petstore_example.json",
        "operationId": "showPetById"
    },
    "httpResponse":{
        "statusCode": 200,
        "body": "some_response_body"
    },
    "times":{
        "unlimited": true
    },
    "timeToLive":{
        "unlimited": true
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

### Actions

Actions can be one of the following types:

* **[response](#response_action)** - returns a response defined by using
  * a **[literal](#button_response_literal_body_only)**
  * a **[javascript template](#button_javascript_templated_response)**
  * a **[velocity template](#button_javascript_velocity_templated_response)**
  * a **[class callback](#button_response_class_callback)** (must be present in classpath)
  * a **[method / closure callback](#button_response_method_or_closure_callback)** (via WebSocket)
* **[forward](#forward_action)** - forwards modified requests and returns modified response by using
  * the **[exact request and response received](#button_forward_exactly)**
  * an **[static overridden request and / or response](#button_forward_overridden)**
  * a **[dynamically modified request and / or response](#button_forward_overridden_and_modified_req)**
  * a **[javascript template (request only)](#button_javascript_templated_forward)**
  * a **[velocity template (request only)](#button_javascript_velocity_templated_forward)**
  * a **[class callback for request and / or response](#button_forward_class_callback)** (must be present in classpath)
  * a **[method / closure callback for request and / or response](#button_forward_method_or_closure_callback)** (via WebSocket)
* **[error](#error_action)** - returns an invalid response as a sequence of bytes or closes the connection

If no action is present for a request because no [request matcher](#request_matchers) was matched then:

* if MockServer is being used as a proxy the request is proxied to its destination un-modified
* if the request host header does not match the hostname or IP the request automatically proxied to the host header

A **response action** can be:

* either a [response literal](#button_response_literal_body_only) containing any of the following:

  * **[status code](#button_response_literal_status_code_and_reason_phrase)**
  * **[reason phrase](#button_response_literal_status_code_and_reason_phrase)**
  * **[body](#button_response_literal_binary_PNG_body)**
  * **[headers](#button_response_literal_with_header)**
  * **[cookies](#button_response_literal_with_cookie)**
  * **[delay](#button_response_literal_with_10_second_delay)**
  * **[connectionOptions](#button_response_literal_with_connection_options_to_suppress_headers)** that can be used to [suppress
    headers](#button_response_literal_with_connection_options_to_suppress_headers), [override headers](#button_response_literal_with_connection_options_to_override_headers) or [close the socket connection](#button_response_literal_with_connection_options_to_close_socket)
* or a **templated** response using **[javascript](#button_javascript_templated_response)** or **[velocity](#button_javascript_velocity_templated_response)** with a
  **[delay](#button_javascript_templated_response_with_delay)**
* or a **callback** used to dynamically generate a response based on the request:

  * as a **server side callback** implemented as a [java class](#button_response_class_callback) that has a default constructor, implements org.mockserver.mock.action.ExpectationResponseCallback
    and is available on the classpath
  * as a **client side callback** implemented as a [closure](#button_response_method_or_closure_callback) using the java or javascript clients

**Response Action Code Examples**

The following code examples show how to create different response actions.

literal response with body only

Java

```
new MockServerClient("localhost", 1080)
    // this request matcher matches every request
    .when(
        request()
    )
    .respond(
        response()
            .withBody("some_response_body")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    // if no request matcher is specified then every request matched
    "httpResponse": {
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
# if no request matcher is specified then every request matched
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpResponse": {
        "body": "some_response_body"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

literal response with UTF16 body

Java

```
new MockServerClient("localhost", 1080)
    // this request matcher matches every request
    .when(
        request()
    )
    .respond(
        response()
            .withHeader(
                CONTENT_TYPE.toString(),
                MediaType.create("text", "plain").withCharset(Charsets.UTF_16).toString()
            )
            .withBody("æè¯´ä¸­å½è¯".getBytes(Charsets.UTF_16))
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    // if no request matcher is specified then every request matched
    "httpResponse": {
        "headers": {
            "content-type": ["text/plain; charset=utf-16"]
        },
        "body": {
            "type": "BINARY",
            "base64Bytes": "/v9iEYv0Ti1W/Yvd"
        }
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
# if no request matcher is specified then every request matched
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpResponse": {
        "headers": {
            "content-type": ["text/plain; charset=utf-16"]
        },
        "body": {
            "type": "BINARY",
            "base64Bytes": "/v9iEYv0Ti1W/Yvd"
        }
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

json response with UTF8 body

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withMethod("GET")
            .withPath("/farsi_body")
    )
    .respond(
        response()
            .withBody(json("Ø³ÙØ§Ù", MediaType.APPLICATION_JSON_UTF_8))
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "method": "GET",
        "path": "/simple"
    },
    "httpResponse": {
        "body": {
            "type": "STRING",
            "string": "Ø³ÙØ§Ù",
            "contentType": "text/plain; charset=utf-8"
         }
    },
    "times": {
        "unlimited": true
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT http://localhost:1080/mockserver/expectation -H "Content-Type: application/json; charset=utf-8" --data '{
    "httpRequest": {
        "method": "GET",
        "path": "/simple"
    },
    "httpResponse": {
        "body": {
            "type": "STRING",
            "string": "Ø³ÙØ§Ù",
            "contentType": "text/plain; charset=utf-8"
         }
    },
    "times": {
        "unlimited": true
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

json response with header

Java

```
new MockServerClient("localhost", 1080)
    // this request matcher matches every request
    .when(
        request()
    )
    .respond(
        response()
            .withBody("some_response_body")
            .withHeader("Content-Type", "plain/text")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    // if no request matcher is specified then every request matched
    "httpResponse": {
        "headers": {
            "Content-Type": ["plain/text"]
        },
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT http://localhost:1080/mockserver/expectation -H "Content-Type: application/json; charset=utf-8" --data '{
    "httpResponse": {
        "headers": {
            "Content-Type": ["plain/text"]
        },
        "body": "some_response_body"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

json response with cookie

Java

```
new MockServerClient("localhost", 1080)
    // this request matcher matches every request
    .when(
        request()
    )
    .respond(
        response()
            .withBody("some_response_body")
            .withHeader("Content-Type", "plain/text")
            .withCookie("Session", "97d43b1e-fe03-4855-926a-f448eddac32f")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    // if no request matcher is specified then every request matched
    "httpResponse": {
        "headers": {
            "Content-Type": ["plain/text"]
        },
        "cookies": {
            "Session": "97d43b1e-fe03-4855-926a-f448eddac32f"
        },
        "body": "some_response_body"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT http://localhost:1080/mockserver/expectation -H "Content-Type: application/json; charset=utf-8" --data '{
    "httpResponse": {
        "headers": {
            "Content-Type": ["plain/text"]
        },
        "cookies": {
            "Session": "97d43b1e-fe03-4855-926a-f448eddac32f"
        },
        "body": "some_response_body"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

literal response with status code and reason phrase

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withMethod("POST")
            .withPath("/some/path")
    )
    .respond(
        response()
            .withStatusCode(418)
            .withReasonPhrase("I'm a teapot")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "method": "POST",
        "path": "/some/path"
    },
    "httpResponse": {
        "statusCode": 418,
        "reasonPhrase": "I'm a teapot"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "method": "POST",
        "path": "/some/path"
    },
    "httpResponse": {
        "statusCode": 418,
        "reasonPhrase": "I'm a teapot"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

literal response with binary PNG body

Java

```
byte[] pngBytes = IOUtils.toByteArray(getClass().getClassLoader().getResourceAsStream("org/mockserver/examples/mockserver/test.png"));
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/ws/rest/user/[0-9]+/icon/[0-9]+\\.png")
    )
    .respond(
        response()
            .withStatusCode(HttpStatusCode.OK_200.code())
            .withHeaders(
                header(CONTENT_TYPE.toString(), MediaType.PNG.toString()),
                header(CONTENT_DISPOSITION.toString(), "form-data; name=\"test.png\"; filename=\"test.png\"")
            )
            .withBody(binary(pngBytes))
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/ws/rest/user/[0-9]+/icon/[0-9]+\\.png"
    },
    "httpResponse": {
        "statusCode": 200,
        "headers": {
            "content-type": ["image/png"],
            "content-disposition": ["form-data; name=\"test.png\"; filename=\"test.png\""]
        },
        "body": {
            "type": "BINARY",
            "base64Bytes": "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"
        }
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "path": "/ws/rest/user/[0-9]+/icon/[0-9]+\\.png"
    },
    "httpResponse": {
        "statusCode": 200,
        "headers": {
            "content-type": ["image/png"],
            "content-disposition": ["form-data; name=\"test.png\"; filename=\"test.png\""]
        },
        "body": {
            "type": "BINARY",
            "base64Bytes": "iVBORw0KGgoAAAANSUhEUgAAAqwAAAApCAIAAAB/QuwlAAAK+GlDQ1BJQ0MgUHJvZmlsZQAASA2tl3dcU8kWx+fe9EYLICAl9CZIr9JrAAXpYCMkgYQSYgoCVpTFFVwLKiKgrugiiIJrAWQtiAULoljAvkEWFXVdLIiKypvAEvfzPm//e5PP3Pne35w598zcmXzOBYBGZQmFWagKANkCiSg6xJ+RmJTMIDwGWKAF8EAf2LHYYqFfVFQE+NfyoRcg8s5bNnJf/2r2vztUOVwxGwAkCnancsTsbMjHYH3PFookAGDqoG68RCKUcxdkdREMELJMzumT/F7OqROMJU7YxEYHAIDVBYBIZbFE6QBQLaDOyGWnQz/UUMh2Ag5fADkPsjebx+JAboU8Izs7R85/QLZI/Yef9H8wi5Wq8MlipSt4ci5wJHxwIF8szGLlT9z8Py/ZWVK4XhPFEF6pPFFoNGwT4ZpVZ+aEK1iQOidySufDGU0xTxoaN8VscQBcy8mxHFZg+BRLM+P8ppglgvS3DV/CjJ1iUU60wr8ga458f0zEwOMyFcwVB8VM6Wn8YOYUF/BiE6Y4lx8/Z4rFmTGKGAp4AQpdJI1WxJwmClbMMVsMR/79XDbr+7MkvFj5O56Ih8MNDJpiriBOEY9Q4q/wI8ya2N8T9tysEIUuzo1RjJWIYhV6BitMvl8n7IWSKMWagEDAB2IgBFmABfIBAyyB9xLAg5QGcoAIsAEXcOBdNAgB/rDNhioHagxgAYLgaCasDKjlQk0Ef/yJXksJNw/uWwACcoT5In46T8LwgyeNy2AK2LYzGA529k4wGHhu5TYAvLs7cR4RTeJ3bYcDAEFVcI9wvmtujwA4CM+AWu93zaQTANooAKffsaWi3El/WHmDA2SgDNSBNvxPMIbR2gAH4AI8gS+MOwxEgliQBBbC+fHgnERw3stAISgGpWAT2AYqwW6wF9SBQ+AIaAEnwVlwEVwFN8Ad8ADIwCB4CYbBBzCGIAgBoSF0RBsxQEwRa8QBcUO8kSAkAolGkpAUJB0RIFJkGbIGKUXKkEpkD1KP/IqcQM4il5Ee5B7Sjwwhb5HPKAalouqoHmqGzkTdUD80HI1FF6Dp6GK0AC1CN6AVaA16EG1Gz6JX0TuoDH2JjmAAhoLRxBhibDBumABMJCYZk4YRYVZgSjDlmBpMI6YN04m5hZFhXmE+YfFYOpaBtcF6YkOxcVg2djF2BXY9thJbh23GnsfewvZjh7HfcDScLs4a54Fj4hJx6bgluGJcOa4Wdxx3AXcHN4j7gMfjNfHmeFd8KD4Jn4Ffil+P34lvwrfje/AD+BECgaBNsCZ4ESIJLIKEUEzYQThIOEO4SRgkfCRSiAZEB2IwMZkoIK4mlhMPEE8TbxKfEcdIKiRTkgcpksQh5ZM2kvaR2kjXSYOkMbIq2ZzsRY4lZ5ALyRXkRvIF8kPyOwqFYkRxp8yl8CmrKBWUw5RLlH7KJ6oa1YoaQJ1PlVI3UPdT26n3qO9oNJoZzZeWTJPQNtDqaedoj2kflehKtkpMJY7SSqUqpWalm0qvlUnKpsp+yguVC5TLlY8qX1d+pUJSMVMJUGGprFCpUjmh0qcyokpXtVeNVM1WXa96QPWy6nM1gpqZWpAaR61Iba/aObUBOoZuTA+gs+lr6PvoF+iD6nh1c3WmeoZ6qfoh9W71YQ01DSeNeI08jSqNUxoyTYymmSZTM0tzo+YRzV7Nz9P0pvlN405bN61x2s1po1rTtXy1uFolWk1ad7Q+azO0g7QztTdrt2g/0sHqWOnM1Vmis0vngs6r6erTPaezp5dMPzL9vi6qa6UbrbtUd69ul+6Inr5eiJ5Qb4feOb1X+pr6vvoZ+lv1T+sPGdANvA34BlsNzhi8YGgw/BhZjArGecawoa5hqKHUcI9ht+GYkblRnNFqoyajR8ZkYzfjNOOtxh3GwyYGJrNNlpk0mNw3JZm6mfJMt5t2mo6amZslmK01azF7bq5lzjQvMG8wf2hBs/CxWGxRY3HbEm/pZplpudPyhhVq5WzFs6qyum6NWrtY8613WvfMwM1wnyGYUTOjz4Zq42eTa9Ng02+raRthu9q2xfb1TJOZyTM3z+yc+c3O2S7Lbp/dA3s1+zD71fZt9m8drBzYDlUOtx1pjsGOKx1bHd84WTtxnXY53XWmO892Xuvc4fzVxdVF5NLoMuRq4priWu3a56buFuW23u2SO87d332l+0n3Tx4uHhKPIx5/edp4Znoe8Hw+y3wWd9a+WQNeRl4srz1eMm+Gd4r3z94yH0Mflk+NzxNfY1+Ob63vMz9Lvwy/g36v/e38Rf7H/UcDPAKWB7QHYgJDAksCu4PUguKCKoMeBxsFpwc3BA+HOIcsDWkPxYWGh24O7WPqMdnMeuZwmGvY8rDz4dTwmPDK8CcRVhGiiLbZ6Oyw2VtmP5xjOkcwpyUSRDIjt0Q+ijKPWhz121z83Ki5VXOfRttHL4vujKHHLIo5EPMh1j92Y+yDOIs4aVxHvHL8/Pj6+NGEwISyBFnizMTliVeTdJL4Sa3JhOT45NrkkXlB87bNG5zvPL94fu8C8wV5Cy4v1FmYtfDUIuVFrEVHU3ApCSkHUr6wIlk1rJFUZmp16jA7gL2d/ZLjy9nKGeJ6ccu4z9K80srSnqd7pW9JH+L58Mp5r/gB/Er+m4zQjN0Zo5mRmfszx7MSspqyidkp2ScEaoJMwfkc/Zy8nB6htbBYKFvssXjb4mFRuKhWjIgXiFsl6jBB6pJaSH+Q9ud651blflwSv+RonmqeIK8r3yp/Xf6zguCCX5Zil7KXdiwzXFa4rH+53/I9K5AVqSs6VhqvLFo5uCpkVV0huTCz8Npqu9Vlq9+vSVjTVqRXtKpo4IeQHxqKlYpFxX1rPdfu/hH7I//H7nWO63as+1bCKblSaldaXvplPXv9lZ/sf6r4aXxD2obujS4bd23CbxJs6t3ss7muTLWsoGxgy+wtzVsZW0u2vt+2aNvlcqfy3dvJ26XbZRURFa07THZs2vGlkld5p8q/qqlat3pd9ehOzs6bu3x3Ne7W2126+/PP/J/v7gnZ01xjVlO+F783d+/TffH7On9x+6W+Vqe2tPbrfsF+WV103fl61/r6A7oHNjagDdKGoYPzD944FHiotdGmcU+TZlPpYXBYevjFrym/9h4JP9Jx1O1o4zHTY9XH6cdLmpHm/ObhFl6LrDWptedE2ImONs+247/Z/rb/pOHJqlMapzaeJp8uOj1+puDMSLuw/dXZ9LMDHYs6HpxLPHf7/Nzz3RfCL1y6GHzxXKdf55lLXpdOXva4fOKK25WWqy5Xm7ucu45fc752vNulu/m66/XWG+432npm9Zy+6XPz7K3AWxdvM29fvTPnTk9vXO/dvvl9srucu8/vZd17cz/3/tiDVQ9xD0seqTwqf6z7uOZ3y9+bZC6yU/2B/V1PYp48GGAPvPxD/MeXwaKntKflzwye1T93eH5yKHjoxot5LwZfCl+OvSr+U/XP6tcWr4/95ftX13Di8OAb0Zvxt+vfab/b/97pfcdI1MjjD9kfxkZLPmp/rPvk9qnzc8LnZ2NLvhC+VHy1/Nr2Lfzbw/Hs8XEhS8SayAUw8IqmpQHwdj/ME5IAoN8AgKw0mVdPWCCT3wKQkb+rXP4vnsy95R0whwCNsIn0BcC5HYCjsDWFLQ3WKMixvgB1dFRUMFnEaY4wn4EFobTA1KR8fPwdzCcJlgB87RsfH2sZH/9aC78R7gPQ/mEyn5cbqxwEwLfQwc454tropVVy5Z/lPzaRFDnqunSQAAABnGlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNS40LjAiPgogICA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICAgICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgICAgICAgICB4bWxuczpleGlmPSJodHRwOi8vbnMuYWRvYmUuY29tL2V4aWYvMS4wLyI+CiAgICAgICAgIDxleGlmOlBpeGVsWERpbWVuc2lvbj42ODQ8L2V4aWY6UGl4ZWxYRGltZW5zaW9uPgogICAgICAgICA8ZXhpZjpQaXhlbFlEaW1lbnNpb24+NDE8L2V4aWY6UGl4ZWxZRGltZW5zaW9uPgogICAgICA8L3JkZjpEZXNjcmlwdGlvbj4KICAgPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4Kl/XR7QAAIpRJREFUeAHtfQ9YVNW69/Y4KChDgqKmGRl6JZMR8cN/ZQV0vqNZzWTW8djQjU6H8aknlXOPdbDsJlRe7JSiHR3/NZRgIqiMf0LNgQT/gFxABxUo0CECFBRsBprRGQ7fu9bae8+eYWbDIHnvp2s9PDNrr/W+73rXb71rrXevvd+hX2dnJ0MTRYAiQBGgCFAEKAL3HgK/u/e6THtMEaAIUAQoAhQBigBCgDoB1A4oAhQBigBFgCJwjyJAnYB7dOBptykCFAGKAEWAIkCdAGoDFAGKAEWAIkARuEcRoE7APTrwtNsUAYoARYAiQBGgTgC1AYoARYAiQBGgCNyjCFAn4B4deNptigBFgCJAEaAIUCeA2gBFgCJAEaAIUATuUQSoE3CPDjztNkWAIkARoAhQBKgTQG2AIkARoAhQBCgC9ygC1Am4RweedpsiQBGgCFAEKAISCgFFgCLwGyBgM9VVG41WhvHyChgx/H7/36AJKpIiQBH4/xUBS2tzi5mRDg+U/k9vwuInAabUmH5iSbHZZClHJFGbTS7HwlKuglogc1nrrrB3XO6kuSm32Swmk8VNpQfFYnIsdfFjN0x9+XibB/L6gFRMpe7E3w6vULa4HIdacRMSCu0+bypS+W2fAn/RFxttzuQ3ijJQld/2mNTbGnhLuRaEqNwKab9wQBsdsPv5aYeVjx1WTjvwTND2FxafPdvgrA+97msETOWbYb2J2Vze14Kd5d2xhpwbFlxX7kSL6+bSVkHZHc1W7cqYOnbDl2W3NZnuqMb/WxqzlabG+wQMHz16+KaSboavcmc8jLJqZyXoLsz3YVfEnQCG6X73tiISPzcqWa0/Qs3lm13WYzf0pLh3XKIiu1bqNy708/PZXNp9D7vyCkvE5Nhu1gJpnc2z7gul9yovplJ3Am+HVyhbXI5jragJCYX2IN/xKyEqrtBVOJFfP5XBemNtN52qPLy0omWv6WaHKzbrpT27lK9ca2GYgOgRC5cHKRYhR9+wsyQ2pOBUsysOWtbHCJhuwgHMnUh3rCGXnfn1Glpcf7lDfXWhgvkaWjxNVpfzwAU9LWIRsOgTY9dBXhYZFzLMRxwWq+kaEFy9htY1YV6cy6Na8ZMI6WvZnUqGIUSl6xVTl2ojUwpzl0y3t2EplcKF0V7gkJOGa1uaLIy3Z4ehveNyaLj7i0F+SHE4rO2eVJRCTI7vuK/PKE2MzxBRCX1eKaZSd43dDq9Qtrgcp1oxExIK7UG+P0dzQ3PYpAzFY0yKTNXfbGMrfTmi3n6jGeHL8G0JxFjOJcfC5ZC3v1O8Pp0leC/p7McLS7KLf/j0m/B9SwYLqGm2bxG43cncY23uWEMiGoW/qW36k8Xb37PFVUSgp1Vhb/zp4Pxb0gBq0R4i5z0IrUuR6pJclfgG7KHcXpJ3dxLAeQAg3msg0tyPcWX/oxlD6f74GMVkSP0mr0gtYE+IbA1HtqrVu4vZS0tD1vr4KEQEKSopNdf1bXjvuBACtsrcnaAGbiJKoVqxs6DGxV24rWFnUvzHX+uBYfHSvySlFhAaS0Pp+hUxUZOjIMXEr8mtFNy3udTcjRykCEm21mMZp3fnXELdt11L+3i/em/VhROF8S9ve3qmev7LGWl5VzlS9G1pMKhXps+fuW3+3G2Llx85XuXgWzWW/feK2K/mz/0qJnb/t2UNxXuPp3xRJlARS3KjUjOMjiIKjpX69ZusiEk6LOwar4Eb3j6GxU0rjDsTwuqJ6cDr75RpSarCwLPFzScrzztRoEvT2QMHY6LxE4QpGaqki1UOiN4o3qONmYJqo6fsSfi0us6lwVqqvkw6mLD44LrDVsZ6Cx9FBM/lPABoQxIYtvQ9p9lubSwtWBWTHh2d/kI0SK7i27U1FK1afPjLghuXcpFi0apj7/9Vm5B0uVlgyDdKj0FzyQfacYd6LOqv9a6eSzUUZakUk7FpTAazL6jl++h+NtkaUleoVmzOra3MTVIpYL7AfI7fzM16rJXTR0NpVjzMLUj9JkfFJOXW8K0AoaV0/3o0a0GQQrVmZy7f14aCVJVqRW5lTW5qEtuMIj63ll1OUBOW2p1JKsSnUMSv33+uWeyMx9ZauXMNzAOkBnCsWL+zspVFtQ8baijCOtfU5m6Gta6fKrUcQ+G2j6QXWWtUAA2an1Exa3YWCdBxy9hcckS9Vl1cbwHl41WqpNQi3BD7UbpzjUoVn1VOTpvdChGykLwISk7EzRUVOzadKWm6BeV1eScSV+pOnTfs/jhj/kz10zO3xa88ccnB3m6dPahbDEvf3G2w9KXsusiPMhJra83+bG/My1/BX+IXZVVVVV9+duTbMocFkG/dnS01FGxWxcTvF5gWKTlcwxmMpdYtziJV7u0TVHKnjLsqS20ubD5pUJ23cfmKNWDM3avN95zLmMqzYMRXbGZ3LlxsK0pNQiNeKbAdjr6b784eJ71aCbLkKSUOHOYSVNolRSbqrEBnLImEqsiUFsRTnywjdLLISFSMklKDqxxE9pKrs7MEa4jE2htglmkNjtI7O816OSLiUqTa2NnZUqLhrmWsmgyTmEN43WjuSo5DW6bLLzy0PnzOsVYoNV1WQp7926Scw+ZVWy4TltbSAr42mqNMPtJMaiu/2cPV8kIgs/WMidRzn65UqkhfxnYtUi7n+pagreZ4uG9XvH0PS9dWxE2om6HhlGe/jYVK6bYw1cnt8dvCpLs2FvLVjRkqKMlem5IdJt2mVJtxRWMGIkN/CsWuKJwJk+YcYpH5GbPg2qhUQhYWdqHB2mkuycJC2pAQo/7DKCwkSl8DdmQ8qcBy4tZcqqm/xTff2Wkzm2+Z0ZyA1FamYdsNC+MkS787io3NVLKLbYvo88S3z6FMVkYF4YVP0pdtS7NAvieioi45WUtnpz49jrONSM40ZDn1SE+x2WQscZhB/MxJyGF7yOuKM/W6RL4VbuYz6hIy9Vs0nAoMP/NkiQYsqCTFZTuROaTarOcsm9MAfzuvUUSZFn6lEqw/zLLqvm7ISedItGCK9REsiAcgkhsEGYukGCNpKKWkxViSgvsdV8Gjb60gMjOrwdLFhDgOFJps3HruAiUn4rINqbAobSpF84DkyRoV/dJWbrFKO8Ou72073uIWrhmb2NoZh34iCpt+SuBWPI4REb/wjx+dWoRLEVviAeG5HEpEcBapEkVPRBl3VdxgsRabXNLioCRWXVgi3Hb5vLk6nVh6CVnIgMusJwOHR5wHoEcZpkdUmIjXwIGFX8GVKRUtSKPqnGSkH9n4Sa0c7bJGvZqUN2F+a1MhUVpHroVCe8fV2UKcDHVhPRFWnYOXHrkGWu+SrIV4fUnOx8TWarKaLNPkY2JzoYYUKCvM4po7ynFqxnxZBcb90vdo7TVzTsBrBaTH59l9fev3cG29QqZBwleVeKG+eeYrsuunVQKoTReIW7BqD9LW2vLTupfIjEot67KsQ71D11p0ZNlNzCF7m7WE9Qnk+S78L0fe3wgWJw3FTUhUBye8wcqIE1Bbk4+30hXXWIqWfLQ3R12oLLQ7Aa26NLzdfneURaaW9QkUP4LX1qQj2/OBfRVIhrWpeGkYbMZp4FiwToDG1mku+zsq3BamrATnAKfWo4ncBg/lYVlLV5zM2H+p0mB3CKzVB3C7B3bk4ylsvrSD+CLKRrgmwrHMsjMVrU3G1u+xQEUK9jmgjSbcF2l+mbHTQ1FEQ/tnk45s/Msy2T6mx6ECeOQHu4HYbOKHTJ6sb0KdqMhMsM96ewMkZ0zHUz05n536hcRZT9BBdXUmnmiyZfkGNPNgWViGdVJqkEpkzQHJiVo9asaoT8C1KYXIdvMTsWnLEkrqodJarSN7YZcbFSCF/hTidUmpxh4O4FxNuNV61G4fNsSLUiZmVhjqjeZu+sj3AivS2VSiwV2UFxq7YSQNgRMAO2OiABZ7Z/HCK44wgkaQxFESEKLs+S1psFUTJ4Dk4XJ70S+ojtvXoz+6AFc1e/BqNmPPyVo0jNamHxNmoBVM9RVa0E5+hJ2GGdrzaDWzVR44DFXwp9xwGa4dk5gtCQBhmYQlIjiLVImiJ6KMSBUs4IXIt41MIaYoVJLoLSwheeLXCvItKdj2E7ntkx24SLWLRd0Rwa5X3T8OQHO7+yTTfb4kxN8bCIOfnoumfF7uZadjCSs+qcsrPl3eYLHBEen0jQa9TqcbxdjExHvAJZn5rlqdWaKaPooI9PG/D2WMLl9LlAzCTze8B6NnHKaKY+vgS6759LXZ+Cmy9/TXPtWggUo7/qOJEdPBQQ4wiCT86Gz49g2PB2KiRxfKkxbAsxVzxc/tbZWVR6AwYkriqxPwA+sBEa/K4yOgqOVktaUqp6yVYfwXPL5iPuqaxH/M0n9GB2Ehrj4cVKrUavLgDZTE/JVzgjGxJHzRag0aIW3ZZZDqlBx4fzNYHFrhNHBtQt3owDE7frf3fzBiwjQo21B1AVlhR92JHwwMMynm4eD7eGu7clADp4SShYee/j2LzIMvfzIJcekaDa31RzRAKVHsflYRAkVgr//nPxJhaCQ3yRk8nAMW5iXMKzlcwwS8EZW3Y8L97Hn/kN+vfFGTPnoaGjyGqblxfEPF6ldyF4Z+PeWFsxcQ4JaqY+gh0KT1c5Wz0YRhvMcq10yaBBntJcFJ5tQ9mrCIkCGB0iHTFUOg0qC5hOMdOuoKUV+YtyeGST0VBWzCVH5IA4/E4KZz7QK2j4tWJIHV+1mgjz2ZTbKcre+EBqJOhCj+BIwuZr2gvfKykoZWBPl01caSfJ1OPsrGmI6loZmnTvt0dhCaebAsfJqBzuTSsgv59UOWoFv5fChqRhr66pvIdnOLLjOW8i0fINPW7v8kfBRUSoKjlhD3Fwi6Jp9hM1NS1IWfq0aRgZL4DPdDVDetvEUAFH3QENt0XKZm5YKQoFFSb9E+8r3ISSQvsASGK5MTAEtpu+lGT8DBzY1SxCNYtu8qwp2xFexCd4oJi+dIe4YwqzPD9AQlnrhrJmKV4vVpGFbfMYnHZ8LbCq0nGm8wlu931QPxW1vlsx5EwygJHJeYOgUyxQcvtVnqvt5mhqfNSRnzHkVrX/8Jz/5hwxs+kBNJrmxJhBxmHWctXXFuPssaUteqng2BiDIuqyQ+XvjJ+sDbCA70n/cm8p4/yDguHPFly+YA5p4mpyeVnrLz9POC+cZtrl9XlU6MhBOqLUyaXIYeiMiVy+a+tPDlZ6L8RVXwhEs6e9GiAVnwTsDac3p9nh498idJtAWEoeHUCUSpjV2gyCYs6EqLsrBG9EwHPBY8s7tMxOhxeJPH9f2DYN5ntZz87+bZzM+opLgs9uUanvViMcresnbYsPv0nDzY3pHAh5+N0P0TE/D0XTJIJeLARE1+UFDrPTVayaSlXfnZyITzwyaoR9k7A4sQNNcmJD40Tkpzl20djHfwordLzmz48WDxrEejrny3G6qGvRjpzRj5JjvQo0xmaKgDMg/Mlp8/o21vMDK41jd4NCeTYcY890fykNJSigpbdtYexpXjZA+gXdqehoQ9N2fzcx0QgtpguFpZUndUW3tcB75FiXJJ4OkdTBE2tvNLsmKwhWG+Nvy+Qod9Q5IHsJsVOAmhkxQRJ+C9Ql11qDKE9GXI2wuHMky9p6LsOuIctivZvwn6GPR8dmcnoep+NslemRrISZQ8MFfOThmuiP+Whs+NY9K2pC2dm7YUdm35sgWKhYvkUbBkWMpLMQaLlQtyxnL0Rlwk8N0XzA3l6pgREeBdpeFLvM5Evjk7iK9kJkfOhYlrvxbkvINnx84bsFMdv7rk3GVtnn11END0SUNEnjx8AjtbLQbRPpLVcsbYAH5yS+Z8kt35Cdq3MnoADmkudN4rMiZNv25fxeo5oYz+y3XQP+WCp4J6iDCPQU9Q4om7ZqaF8wbBSIaPGAdLWuUVw7XmcrxS/fMvaXljOCaTEeVMHex8DBkf8aD9RVuZfDyzzeUQubclTrCbbxGcS5HXyfRiCMSUcWvzbvTztDg4en4ksy5vS5r+HwvCvSoy0YjLF0YKJkOPJfbRSYA8yG7D7tr2Dt1sbdJpkpX4uZc2bd1i+YwAr6iCZncMuLznXJbK+H5+M15avC4tLW/oUGVcQkpKAhKBHVPRNhgrFwoJhmnkklyplEfKhw2SwCrcG81dN9nhUIxX4cED+1u54xC4BWs3WcnfxKcCJob4BQxi54Z0yAABr6McQYXLbMjYAIdy3K6PL5xDiKU7CAsYsGsT6kYHd+pbGOnUF8Hdsu06eN3W/EM6rKYRIbAm2qz8WktYA4IckcF7v2Qwi0zAwyPdtYDKA/ARwpklR7JrCJm1sejUpvVF35bC8PT3lg55OHTCM689vW7fq/uzse+nvVTZ2sGwr0vB8mdrM5I/32ly34eifXx47do4i0CCH14YA5839hy3MM0VqC/Bj+B9sReiiJ7Cz9BgV33syWwaex+6rWOTZCCX6/odsmhzk16XvEwpgzq9dt0HsTPGBUStKYD7v0EstdE+8fzQzJNPHspjMXywvR2JF9eOZBDmxaZsb5KrtZewuZqseL9xMxZ/sE6rvT5UrkxITkH3246pTxpiRdrDFEX7KBk0DBgiHx1p7yKvkygjT0UygY/hs4AteRdNrcWHwERkCbHhSKYnQuDkqgcoObUsvIQ7FsElyUu8JP25+3qYzezi1i71i3jKb+KkwRJJfzQDpQM5GizA7g0L5OGse1viKXnDYRjeHERwFqnqDj0RZUSqeEUdM67UdqRwuPKPeBO996E9dLbVdC4nDbJxyqn4HNuBrAcXgoZ7QH07JJaG8lOVv4YsfGfHa+9oLK21F4u2J85drc37bG/5bJXd03dqoudcpotH0cFiZKI+Yzk5omQa9i+FOw/Y2LtLQ+9HtyFwGJj7SRRP21pTev4aEzJO2nMdeF63Gf6IE1Nca4JzMCYsNHBoPYye0V8ZvTdpIs97o8Zw8TozPti7/jvkLlcb2phJ3FLR1pjXzTEAK8Z6EzV54pRBFcqDbCk/gWzmviEO845lEHzdOVgEjTplxXVwIna49JVNfJI5c3zb6S98rrcwzLSYILhfh9NoLnXcRJtxY5GBedSOTGMRuvkaeJ8PqW06V8fM4m5uGnMPvrOB+cPfn0UPccADeFuh+7j/t+/teW/D1VVxVY/pJgQyHS1nK7a8zzDLJz4TDiPKJ68xTwRPY86dQQWDRyJjkyiyX/lPu7G1XyptvM6MCJYK9347+4T/C75KrWH3uW+ZetSX5ePv76UoXiZkiG2cKqtjZnN9bMiNf3M9o0hIlBX1ejYJm8B5U3lR8Y1BIe+s3fHOWk1rQ23Rge1zF6/Oe3dL+ZsfYgKZ7lhuFKcCHCGXFpxnRk3iAbzpEhTzL1eBGR47Wpbg55BI0tXLP2CBXT/YM/nETH3CglCy6h2O376a0QtJ+6IhoTyclxCH0k0fzT9cBqq83DrLEvxcBS5sBeuXf5brk7Dp3zG/G0ZcJ/iQzotNZNI+yM464GfOgvL4V2ehWvHWBfw42yOUnJkcru1384zp1yaoihgZ5EsKvT7f/8aT9lFuP3viZ+b+B3wtjXVAVtzSiqJu2VR98mcu6/Tt3paWzCakFvQrHsR2bPXnuPE1/+IW57Xz3FZ1MwQiyoQx59zY/JLZ/HIj7JtrtYUUznnvaGUys+XdrL3aMT6HoTL59ejebed9dBLgrJ+La8PRldHRM97dVQ51Em//4PA5r8IBIkrkoAZnu3x4wIVvESIjn2I9AMa0f/uXSJ7fQJEb3oFeaCMcPfkx+NSv1tiPJZoLYsdNfWLG1NNNtp7oQOSg5sRTpX7j0WuExFJTloIehjEBg353vwwdSremldl/Tqa56u2nD7z9xwPFTR0jHkVT58jb+RfYe0hL9qpjF4kU959EpTGTpgJJ2uIv+F9FMpXvTUY+gHz6WH933HcGlp6AJj407vTH5ZKHX14JmatfbQAfavQCeBbgkPwnhsP1jQ3//IlFlbFc2HsB7dPRDzzk7z8ZraFtWWlcWJ2t6uuPr57Xtd/irGnUg4Ph9wCe+dsjk4Cw+MRf0Q8IegfPwk8GPj26qUBo1u0XtFXYA5D6+QwJRcZmy9ZU82dgzQUHX3zqeNxTBoeoKaDi06hJsTBZis+/txz6ErTo90SJXoniZTJjpqA+arfvKGd9U1vu9o/gTvnyTS8ICIYqT2eTXbQwZzGsnBH9hOzdcuSBSfxHBc9R4RcI4K6wMwg9I2T0mm+KeI6CNbFTn3hi6hp7CV/lkJGOnCqDAu2OvWhJQclSvm7lapLt8uklRftC5FPRrAdgqtmvRieoTPdG6FlDXVqWiPZR+vAs9IaXvRe2hmP/uRQG4aKXb7BH4ATOUijBnVj9Siz0S5Y8LwTbu3jrzsreBkpY1NYVuXVgoCjd+nb9qVr4HjxQIhn2+DzIWb/JqEY1OJ36LOvPMUf/vLaG8R0aOhKKaj/fhZwBSG1VhX/7zEjyzp8itgTzDd/3p+86TVRoLU2bi4cYCRHBedi/9XIIRJQxubd54bpAuieitnP/Ha79Zz4Ps0e/LjZ2dR7DLHtxKlrPTbXlBQUFlQ3slHZgcHfR9V1BdyWCVxMFJCRYCL+Gypay4UPo7VYI9kP7PK61GjKJDvIEdU6OVp2IX0RmmHQUxOKYesVlrkgn8pWJ6nR46IAWCJIiU7R6PnaGb4mEYcgi5QmafIj6ykSLEaRI4E5Xk3eQ0TtTwCiuuaMcXjzOOEYHoEgB/Jew4XTGFi0bB/i3UqzbzX1sCM3W5C322uj3z+HalnX4ZVqICVz1j8MJbGgASEt1DhHEzTqq1MRFZspTMrVaDXmPmLwB7qitC97fBhYIP8OhGSz4guFmFRKakOjQdOmA8SQKEVTUkqAJsx7FAqA/BRsdR969V5AQwaZcNixQkb9vv35HIgkHQO//o0QCChBv/g7Nd3EkCkBKQgRR6IFCTV7Xt/20n40jwLGFbPweIlDmb9ec3LjmQByJIZRui0vHtm4uW0q0ivpue3rx9hWEPfXDHBs0y4YIcgpjVdAHF60AAZCNdmvulSheZif7jjFM0RSNJpGbMxAi2M1s6jpknUb8Ii2e9Xb5JGflJpdSnZmjzVTHkUC4uEzoh7maXRZkcYnpmekJrA4yLQ4CFL4mTWSRICPysnRTfiI7aZelZKancOq7jA4wp8MOCUmmhPmdnEAuUEFkXIq+xdp3DbGBBsIwRfE+thSmID1gDBJSNGp2ejLLcqC/4oxdddaRgAc4GE6v4AdBXAhPhjPdoORI7Do6IHzOnow9p1e9xMYB7qtFRm2uLiZLX/Rbh1Dta6R20yFc25R7iNS+8JZ23Uf2WOgXXEQHiNoSCUCDMV2WrE4hUSYIWBxAAeEhbnEWqRJFT0QZkSqAA2+L3Jv8ZlG1hduuME/Ggo1rgC4ns+HQJThsQMZdOg2Zy0sPQgQrcDyvUq13EGTGQa5CJ8BMQlTjUEyPQy0Ep7GTFo0MTolau7HaxfaOCwLP1OxOjmVHgq/BhRkndw2caCpUs0rIyM8YNGU6PiSUJ2RyXGKad5Fj7weEBQpDBIkToOSmB9j9C28VcJFlwPXLvvdR3C3/p3y/GP3AAEnWloz3UUAO/tuU8JEW/QLBjMMNXL3w21klY4XQJ4Jex6XoYHBcJmfezt8AFtjRhOA7DDdWSmhCqEBEB6dOGAvj0LbNOgGdnZX/hTbg1L/vR0sRJC66j+2+qSKX291JXF/2Rp09ls9sOInDArmQP0XxGRxQSnwLpYbH8Ocd6EcI+O258WgKCT7kGKEq7MDGHPCKudRU9qFCUCvd9WEWGwForsCOi+pnXjrLYyYxirvW2n/8ANf0QhSnBXybDWrWGyezQZ7ORtiKzqauQ8Y6AXjWC8STrLWpJJGc+rFTDna85AoOjhZ9pmOlPFPPzrwK/DMG6hKOlIs0VmrYVahCK1xSIhPw7s7XChWxNuU7rA7L1DptMlEnsbClDxsiooTbMKgh0keoNehS7PcsyBtIN3CjL8LI6cytUjCY7I2Qc/SviBAhRJAXR8mJ2EWI4IxU/jdO4I5le4Fdt9byYsEPpaAbmH3lXNBrZ2dD0WkVe5+zPvqlPaveQkGDybl2dr5pUVuycqHdeGDBq0pE3h5vPyI4i1SJoCeijEgVrEJILSUfuy6mttCchHkCCPeDAQz/8wB6HPrlcgrwGDpl+sE1mQl36NPSXHmxDv2omtegseNJUGEPWu4xl6W51nDd7OXlNxyCc9ATEktzg0ki9fd3GY1hMbWaGR+pj7eEfZhiAvYrRq9BfkMDRgTyTxqJgiI6dJHDdslSt/iR7OII2fHdT/paDIsfOVAcMeXk7sdNP11tMXcMCggYwz0G5CFoa75We9Us8fEJCPAL9B/AyTFeqPjF54ERDwcybW3/kvh6ezN1MWOzL4bIjuc8yT9I44WgTBeVmmsrrxitViszdOz4IKeuOXC64O1jWEhzXTR00sLpUkwHJ1IPL011lfDv/jqszOCHxg8d4vTQgGlvrG03M/19Bg25P1DwwLPbNizXq35sN6OzvwF+I4c8OMq7y/M6sNXrTcb+Pn6DA0ZIu7TbbQNCgtsUBc/p4R+aSXwGjR4VKFTTs9kkVMhVHiyw7jqa+oOGjg0JcnoUZaqtrIcjYD+/oSNGdZkVrqTxZTZTQ7XhOqwnIx4KFrdrsOzaGoPZ6uU3dPioQPR4AP6Tm8km8Q8UD1Fim/KkIV47YUa0j/CaFLzuIZEMChjd5f/KiTIKWxDL91xIT1G6sDX91U9a/rL39cVTBpN8/GGVMshyqbbNKhkwOmiYr9CYkG6WuqoWNMpS38BRfvxMa66pqzf7hEwaxrRB8PjvfH0HVG1NX8RJdtknEVsCowVL8vHxGz7K1bCK4CxSBafs7u1TRBmRKqd+daO2EzV3aanc6fPIK/ALxC25KqcZxZF0/33HnYDuVbpLKGyWW621F1RzTtSGyHQ5Tw5hnQCZbveT+LGxB91sK9M9OR/eARj+dekfH0VD3b57+TfJWWZm3uNFX0xxnmgeCKakFAGKAEWgFwh0WNraC1L2/X2bUegEkLyH4izqmVu3XmGeWK1Yu3AM8N44X7jgueJWhll5XKV4kLsR8lDoXU8O/wQXfmZj119Gx6Yx8JNBKwUv1nrad7qDeIpYT+nPb/v6z5+h9/4gWAyhbGPa4RMGzvPkOyX8jyMvZlxpejV8A8QNtn/fgt64YXw+XyGj4+c5nJSDIkARuD0E2i4vCs3BqxAzwIsckPVmZcNKeMs/Cd76ek1+QvbUFL+IEGvx92jZDHoj+lnqAbgfJf0W+dSl8D4gpMQ/34YHAPz9P/zwQySHpr5G4Nem5gvXrI9ETfxHyuMjwJ39180mQ2PgrPHR0xxOXHvWrM9jC4NH9G+t/clUfd78y0ivCEXIB5uenzWKe1O9Z1IoFUWAIkAR6AME/mWpvVDf+dB9yg/m/ft0dLLZdv264eqAxxSPBN/nyUMzrIp07PhnZvVvvXa95nx7g8HmHxEQ8x9PJakm0EMAkZH6ta7q+2teMx5//auchEektxXlRx8HiOBMqygCFAGKAEWAInA3I3BbHsTdDAztG0WAIkARoAhQBO52BKgTcLePMO0fRYAiQBGgCFAE3CBAnQA3wNBiigBFgCJAEaAI3O0IUCfgbh9h2j+KAEWAIkARoAi4QYA6AW6AocUUAYoARYAiQBG42xGgTsDdPsK0fxQBigBFgCJAEXCDAHUC3ABDiykCFAGKAEWAInC3I0CdgLt9hGn/KAIUAYoARYAi4AYB6gS4AYYWUwQoAhQBigBF4G5HgDoBd/sI0/5RBCgCFAGKAEXADQL/D4BaqFLDMQVOAAAAAElFTkSuQmCC"
        }
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

literal response with 10 second delay

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
    )
    .respond(
        response()
            .withBody("some_response_body")
            .withDelay(TimeUnit.SECONDS, 10)
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some/path"
    },
    "httpResponse": {
        "body": "some_response_body",
        "delay": {
            "timeUnit": "SECONDS",
            "value": 10
        }
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "path": "/some/path"
    },
    "httpResponse": {
        "body": "some_response_body",
        "delay": {
            "timeUnit": "SECONDS",
            "value": 10
        }
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

respond differently for the same request

Java

```
MockServerClient mockServerClient = new MockServerClient("localhost", 1080);

// respond once with 200, then respond twice with 204, then
// respond with 404 as no remaining active expectations
mockServerClient
    .when(
        request()
            .withPath("/some/path"),
        Times.exactly(1)
    )
    .respond(
        response()
            .withStatusCode(200)
    );

mockServerClient
    .when(
        request()
            .withPath("/some/path"),
        Times.exactly(2)
    )
    .respond(
        response()
            .withStatusCode(204)
    );
```

JavaScript

```
var client = require('mockserver-client').mockServerClient("localhost", 1080);

// respond once with 200, then respond twice with 204, then
// respond with 404 as no remaining active expectations
client.mockAnyResponse({
    "httpRequest": {
        "path": "/some/path"
    },
    "httpResponse": {
        "statusCode": 200
    },
    "times": {
        "remainingTimes": 1,
        "unlimited": false
    }
}).then(
    function () {
        console.log("first expectation created");

        client.mockAnyResponse({
            "httpRequest": {
                "path": "/some/path"
            },
            "httpResponse": {
                "statusCode": 204
            },
            "times": {
                "remainingTimes": 2,
                "unlimited": false
            }
        }).then(
            function () {
                console.log("second expectation created");
            },
            function (error) {
                console.log(error);
            }
        );
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
# respond once with 200, then respond twice with 204, then
# respond with 404 as no remaining active expectations

curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "path": "/some/path"
    },
    "httpResponse": {
        "statusCode": 200
    },
    "times": {
        "remainingTimes": 1,
        "unlimited": false
    }
}'

curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "path": "/some/path"
    },
    "httpResponse": {
        "statusCode": 204
    },
    "times": {
        "remainingTimes": 2,
        "unlimited": false
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

literal response with connection options to suppress headers

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
    )
    .respond(
        response()
            .withBody("some_response_body")
            .withConnectionOptions(
                connectionOptions()
                    .withSuppressConnectionHeader(true)
                    .withSuppressContentLengthHeader(true)
            )
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest" : {
        "path" : "/some/path"
    },
    "httpResponse" : {
        "body" : "some_response_body",
        "connectionOptions" : {
            "suppressContentLengthHeader" : true,
            "suppressConnectionHeader" : true
        }
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest" : {
        "path" : "/some/path"
    },
    "httpResponse" : {
        "body" : "some_response_body",
        "connectionOptions" : {
            "suppressContentLengthHeader" : true,
            "suppressConnectionHeader" : true
        }
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

literal response with connection options to override headers

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
    )
    .respond(
        response()
            .withBody("some_response_body")
            .withConnectionOptions(
                connectionOptions()
                    .withKeepAliveOverride(false)
                    .withContentLengthHeaderOverride(10)
            )
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest" : {
        "path" : "/some/path"
    },
    "httpResponse" : {
        "body" : "some_response_body",
        "connectionOptions" : {
            "contentLengthHeaderOverride" : 10,
            "keepAliveOverride" : false
        }
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest" : {
        "path" : "/some/path"
    },
    "httpResponse" : {
        "body" : "some_response_body",
        "connectionOptions" : {
            "contentLengthHeaderOverride" : 10,
            "keepAliveOverride" : false
        }
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

literal response with connection options to close socket

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
    )
    .respond(
        response()
            .withBody("some_response_body")
            .withConnectionOptions(
                connectionOptions()
                    .withCloseSocket(true)
            )
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest" : {
        "path" : "/some/path"
    },
    "httpResponse" : {
        "body" : "some_response_body",
        "connectionOptions" : {
            "closeSocket" : true
        }
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest" : {
        "path" : "/some/path"
    },
    "httpResponse" : {
        "body" : "some_response_body",
        "connectionOptions" : {
            "closeSocket" : true
        }
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

literal response with connection options to close socket after a delay

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
    )
    .respond(
        response()
            .withBody("some_response_body")
            .withConnectionOptions(
                connectionOptions()
                    .withCloseSocket(true)
                    .withCloseSocketDelay(new Delay(MILLISECONDS, 500))
            )
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest" : {
        "path" : "/some/path"
    },
    "httpResponse" : {
        "body" : "some_response_body",
        "connectionOptions" : {
            "closeSocket" : true,
            "closeSocketDelay" : {
                "timeUnit" : "MILLISECONDS",
                "value" : 500
            }
        }
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest" : {
        "path" : "/some/path"
    },
    "httpResponse" : {
        "body" : "some_response_body",
        "connectionOptions" : {
            "closeSocket" : true,
            "closeSocketDelay" : {
                "timeUnit" : "MILLISECONDS",
                "value" : 500
            }
        }
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

javascript templated response

Java

```
// $!request.headers['Session-Id'] returns an array of values because headers and queryStringParameters have multiple values
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
    )
    .respond(
        template(
            HttpTemplate.TemplateType.JAVASCRIPT,
            "return {\n" +
                "     'statusCode': 200,\n" +
                "     'cookies': {\n" +
                "          'session' : request.headers['Session-Id'][0]\n" +
                "     },\n" +
                "     'headers': {\n" +
                "          'Date' : Date()\n" +
                "     },\n" +
                "     'body': JSON.stringify(\n" +
                "               {\n" +
                "                    method: request.method,\n" +
                "                    path: request.path,\n" +
                "                    body: request.body\n" +
                "               }\n" +
                "          )\n" +
                "};"
        )
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
// $!request.headers['Session-Id'] returns an array of values because headers and queryStringParameters have multiple values
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some/path"
    },
    "httpResponseTemplate": {
        "template": "return { statusCode: 200, cookies: { session: request.headers[\"Session-Id\"] && request.headers[\"Session-Id\"][0] }, headers: { Date: [ Date() ] }, body: JSON.stringify({method: request.method, path: request.path, body: request.body}) };",
        "templateType": "JAVASCRIPT"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "path": "/some/path"
    },
    "httpResponseTemplate": {
        "template": "return { statusCode: 200, cookies: { session: request.headers[\"Session-Id\"] && request.headers[\"Session-Id\"][0] }, headers: { Date: [ Date() ] }, body: JSON.stringify({method: request.method, path: request.path, body: request.body}) };",
        "templateType": "JAVASCRIPT"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

javascript templated response reading request body

To simplify handling different types of bodies, JavaScript and Velocity templates, have access to both an object `request.body` field and a string `request.bodyAsString` field which can be used as shown in the examples below.

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
    )
    .respond(
        template(
            HttpTemplate.TemplateType.JAVASCRIPT,
            "return { statusCode: 200, headers: { Date: [ Date() ] }, body: JSON.stringify({is_active: JSON.parse(request.bodyAsString).is_active, id: \"1234\", name: \"taras\"}) };"
        )
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some/path"
    },
    "httpResponseTemplate": {
        "template": "return { statusCode: 200, headers: { Date: [ Date() ] }, body: JSON.stringify({is_active: JSON.parse(request.bodyAsString).is_active, id: \"1234\", name: \"taras\"}) };",
        "templateType": "JAVASCRIPT"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "path": "/some/path"
    },
    "httpResponseTemplate": {
        "template": "return { statusCode: 200, headers: { Date: [ Date() ] }, body: JSON.stringify({is_active: JSON.parse(request.bodyAsString).is_active, id: \"1234\", name: \"taras\"}) };",
        "templateType": "JAVASCRIPT"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

javascript templated response with delay

Java

```
String template = "" +
    "if (request.method === 'POST' && request.path === '/somePath') {\n" +
    "    return {\n" +
    "        'statusCode': 200,\n" +
    "        'body': JSON.stringify({name: 'value'})\n" +
    "    };\n" +
    "} else {\n" +
    "    return {\n" +
    "        'statusCode': 406,\n" +
    "        'body': request.body\n" +
    "    };\n" +
    "}";

new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
    )
    .respond(
        template(HttpTemplate.TemplateType.JAVASCRIPT)
            .withTemplate(template)
            .withDelay(TimeUnit.MINUTES, 2)
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {"path": "/some/path"},
    "httpResponseTemplate": {
        "template": "if (request.method === \"POST\" && request.path === \"/some/path\") { return { statusCode: 200, body: JSON.stringify({name: \"value\"}) }; } else { return { statusCode: 406, body: request.body }; }",
        "templateType": "JAVASCRIPT",
        "delay": {"timeUnit": "MINUTES", "value": 2}
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {"path": "/some/path"},
    "httpResponseTemplate": {
        "template": "if (request.method === \"POST\" && request.path === \"/some/path\") { return { statusCode: 200, body: JSON.stringify({name: \"value\"}) }; } else { return { statusCode: 406, body: request.body }; }",
        "templateType": "JAVASCRIPT",
        "delay": {"timeUnit": "MINUTES", "value": 2}
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

velocity templated response

Java

```
// $!request.headers['Session-Id'] and $!request.headers['User-Agent'] both returns an
// array of values because headers and queryStringParameters have multiple values
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
    )
    .respond(
        template(
            HttpTemplate.TemplateType.VELOCITY,
            "{\n" +
                "     \"statusCode\": 200,\n" +
                "     \"cookies\": { \n" +
                "          \"session\": \"$!request.headers['Session-Id'][0]\"\n" +
                "     },\n" +
                "     \"headers\": {\n" +
                "          \"Client-User-Agent\": [ \"$!request.headers['User-Agent'][0]\" ]\n" +
                "     },\n" +
                "     \"body\": $!request.body\n" +
                "}"
        )
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
// $!request.headers['Session-Id'] and $!request.headers['User-Agent'] both returns an
// array of values because headers and queryStringParameters have multiple values
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some/path"
    },
    "httpResponseTemplate": {
        "template": "{ \"statusCode\": 200, \"cookies\": { \"session\": \"$!request.headers[\"Session-Id\"][0]\" }, \"headers\": { \"Client-User-Agent\": [ \"$!request.headers[\"User-Agent\"][0]\" ] }, \"body\": \"$!request.body\" }",
        "templateType": "VELOCITY"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "path": "/some/path"
    },
    "httpResponseTemplate": {
        "template": "{ \"statusCode\": 200, \"cookies\": { \"session\": \"$!request.headers[\"Session-Id\"][0]\" }, \"headers\": { \"Client-User-Agent\": [ \"$!request.headers[\"User-Agent\"][0]\" ] }, \"body\": \"$!request.body\" }",
        "templateType": "VELOCITY"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

class callback

Java

```
public class CallbackActionExamples {

    public void responseClassCallback() {
        new ClientAndServer(1080)
            .when(
                request()
                    .withPath("/some.*")
            )
            .respond(
                callback()
                    .withCallbackClass(TestExpectationResponseCallback.class)
            );
    }

    public static class TestExpectationResponseCallback implements ExpectationResponseCallback {

        @Override
        public HttpResponse handle(HttpRequest httpRequest) {
            if (httpRequest.getPath().getValue().endsWith("/path")) {
                return response()
                    .withStatusCode(HttpStatusCode.ACCEPTED_202.code())
                    .withHeaders(
                        header("x-callback", "test_callback_header"),
                        header("Content-Length", "a_callback_response".getBytes(UTF_8).length),
                        header("Connection", "keep-alive")
                    )
                    .withBody("a_callback_response");
            } else {
                return notFoundResponse();
            }
        }
    }

}
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some.*"
    },
    "httpResponseClassCallback": {
        "callbackClass": "org.mockserver.examples.mockserver.CallbackActionExamples$TestExpectationResponseCallback"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest" : {
        "path" : "/some.*"
    },
    "httpResponseClassCallback" : {
        "callbackClass" : "org.mockserver.examples.mockserver.CallbackActionExamples$TestExpectationResponseCallback"
    }
}'
```

To use a class callback MockServer must be able to **load the class from the classpath**.

The callback class must:

* implement
  * **org.mockserver.mock.action.ExpectationResponseCallback** to dynamically override the **response**
* have a zero argument constructor
* be available in the classpath of the MockServer

If MockServer is started using the the [JUnit 4 @Rule](/mock_server/running_mock_server.html#junit_rule), the [JUnit 5 Test Extension](/mock_server/running_mock_server.html#junit_test_extension), [ClientAndServer](/mock_server/running_mock_server.html#client_api) or directly using org.mockserver.netty.MockServer then any class present in the main or test classpaths will be visible to MockServer.

If MockServer is started using the [maven plugin](/mock_server/running_mock_server.html#maven_plugin) only the non-forked goals (such as runAndWait and start) will be able to load classes from the main and test classpaths. It is possible to use classes from a separate maven dependency, however, this dependency must be specified in the plugin configuration dependencies section. Any dependency added to the plugin configuration dependencies section will then be visible to MockServer run using both forked and non-forked goals.

The following configuration shows how to use classes from a separate maven dependency in callback actions.

```
 <plugin>
     <groupId>org.mock-server</groupId>
     <artifactId>mockserver-maven-plugin</artifactId>
     <version>5.14.0</version>
     <configuration>
        <serverPort>1080</serverPort>
        <logLevel>DEBUG</logLevel>
        <pipeLogToConsole>true</pipeLogToConsole>
     </configuration>
     <executions>
         <execution>
             <id>pre-integration-test</id>
             <phase>pre-integration-test</phase>
             <goals>
                 <goal>runForked</goal>
             </goals>
         </execution>
         <execution>
             <id>post-integration-test</id>
             <phase>post-integration-test</phase>
             <goals>
                 <goal>stopForked</goal>
             </goals>
         </execution>
     </executions>
     <dependencies>
         <dependency>
             <groupId>com.my-domain</groupId>
             <artifactId>my-callback-dependency</artifactId>
             <version>1.0.0</version>
         </dependency>
     </dependencies>
 </plugin>
```

If MockServer is started using the [command line](/mock_server/running_mock_server.html#running_from_command_line) then the callback classes must be added to the JVM using the classpath command line switch (**cp** or **classpath**). The **classpath** switch is ignored by the JVM if the
**jar** switch is used. So to run the MockServer from the command line directly (with mockserver-netty-5.14.0-shaded.jar) you must specify the **org.mockserver.cli.Main** main class specifically and not use the **jar** switch as follows.

```
java -Dfile.encoding=UTF-8 -cp mockserver-netty-5.14.0-shaded.jar:my-callback-dependency.jar org.mockserver.cli.Main -serverPort 1080
```

method / closure callback

Java 7

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
    )
    .respond(
        new ExpectationResponseCallback() {
            @Override
            public HttpResponse handle(HttpRequest httpRequest) {
                if (httpRequest.getMethod().getValue().equals("POST")) {
                    return response()
                        .withStatusCode(ACCEPTED_202.code())
                        .withHeaders(
                            header("x-object-callback", "test_object_callback_header")
                        )
                        .withBody("an_object_callback_response");
                } else {
                    return notFoundResponse();
                }
            }
        }
    );
```

Java 8+

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
    )
    .respond(
        request -> {
            if (request.getMethod().getValue().equals("POST")) {
                return response()
                    .withStatusCode(ACCEPTED_202.code())
                    .withHeaders(
                        header("x-object-callback", "test_object_callback_header")
                    )
                    .withBody("an_object_callback_response");
            } else {
                return notFoundResponse();
            }
        }
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
var callback = function (request) {
    if (request.method === 'POST') {
        return {
            'statusCode': 201,
            'header': {
                "x-object-callback": ["test_object_callback_header"]
            },
            'body': "an_object_callback_response"
        };
    } else {
        return {
            'statusCode': 404
        };
    }
};
mockServerClient("localhost", 1080)
    .mockWithCallback(
        {
            'path': '/some/path'
        },
        callback
    )
    .then(
        function () {
            console.log("expectation created");
        },
        function (error) {
            console.log(error);
        }
    );
```

When using org.mockserver.client.MockServerClient each method / closure callback has a separate web socket client. To ensure the number of total threads does not grow too large for large numbers of method / closure callback expectations the default event loop thread pool for the web socket client is kept fairly low. However, if an extremely large load is matched against a single method / closure callback expectation the event loop thread pool may not be large enough for its web socket client.

The number of threads for the event loop thread pool for each web socket client (i.e. for each expectation with a method / closure callback) [can be configured and is described in the configuration section](/mock_server/configuration_properties.html#button_configuration_web_socket_event_loop_thread_count).

create expectation within method / closure callback

Java 7

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
    )
    .respond(
        new ExpectationResponseCallback() {
            @Override
            public HttpResponse handle(HttpRequest httpRequest) throws Exception {
                if (httpRequest.getMethod().getValue().equals("POST")) {
                    mockServerClient
                        .when(
                            request()
                                .withPath("/some/otherPath")
                        )
                        .respond(
                            response()
                                .withBody(httpRequest.getBodyAsString())
                        );
                    return response()
                        .withStatusCode(ACCEPTED_202.code())
                        .withBody("request processed");
                } else {
                    return notFoundResponse();
                }
            }
        }
    );
```

Java 8+

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
    )
    .respond(
        httpRequest -> {
            if (httpRequest.getMethod().getValue().equals("POST")) {
                mockServerClient
                    .when(
                        request()
                            .withPath("/some/otherPath")
                    )
                    .respond(
                        response()
                            .withBody(httpRequest.getBodyAsString())
                    );
                return response()
                    .withStatusCode(ACCEPTED_202.code())
                    .withBody("request processed");
            } else {
                return notFoundResponse();
            }
        }
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
var callback = function (request) {
    if (request.method === 'POST') {
        mockServerClient("localhost", 1080)
            .mockAnyResponse({
                "httpRequest": {
                    "path": "/some/otherPath"
                },
                "httpResponse": {
                    "body": request.body.string
                }
            })
            .then(
                function () {
                    console.log("chained expectation created");
                },
                function (error) {
                    console.log(error);
                }
            );
        return {
            'statusCode': 202,
            'body': "request processed"
        };
    } else {
        return {
            'statusCode': 404
        };
    }
};
mockServerClient("localhost", 1080)
    .mockWithCallback(
        {
            'path': '/some/path'
        },
        callback
    )
    .then(
        function () {
            console.log("expectation created");
        },
        function (error) {
            console.log(error);
        }
    );
```

When using org.mockserver.client.MockServerClient each method / closure callback has a separate web socket client. To ensure the number of total threads does not grow too large for large numbers of method / closure callback expectations the default event loop thread pool for the web socket client is kept fairly low. However, if an extremely large load is matched against a single method / closure callback expectation the event loop thread pool may not be large enough for its web socket client.

The number of threads for the event loop thread pool for each web socket client (i.e. for each expectation with a method / closure callback) [can be configured and is described in the configuration section](/mock_server/configuration_properties.html#button_configuration_web_socket_event_loop_thread_count).

A **forward action** can be:

* either an [exact forwarder](#button_forward_exactly), that forwards requests exactly as it receives them, containing the following:

  * **host**
  * **port**
  * **[scheme](#button_forward_exactly_in_https)**
* or an [overridden request](#button_forward_overridden) (or overridden response), with a **[delay](#button_forward_overridden_with_delay)**, that allows any part of a forwarded request or
  response to be replaced or certain fields (path, headers, cookies or query parameters) to be modified
* or a templated forwarder using **[javascript](#button_javascript_templated_forward)** or **[velocity](#button_javascript_velocity_templated_forward)**, with a **[delay](#button_javascript_templated_forward_with_delay)**, that allows requests to be modified or completely re-written before they are forwarded
* or a **callback** used to dynamically generate the request to forward based on the request received by MockServer:

  * as a **server side callback** implemented as a [java class](#button_forward_class_callback) that has a default constructor, implements org.mockserver.mock.action.ExpectationForwardCallback
    or org.mockserver.mock.action.ExpectationForwardAndResponseCallback and is available on the classpath
  * as a **client side callback** implemented as a [closure](#button_forward_method_or_closure_callback) using the java or javascript clients

**Forward Action Code Examples**

The following code examples show how to create different forward actions.

forward exact request

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
    )
    .forward(
        forward()
            .withHost("mock-server.com")
            .withPort(80)
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some/path"
    },
    "httpForward": {
        "host": "mock-server.com",
        "port": 80,
        "scheme": "HTTP"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "path": "/some/path"
    },
    "httpForward": {
        "host": "mock-server.com",
        "port": 80,
        "scheme": "HTTP"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

forward exact request in HTTPS

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
    )
    .forward(
        forward()
            .withHost("mock-server.com")
            .withPort(443)
            .withScheme(HttpForward.Scheme.HTTPS)
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some/path"
    },
    "httpForward": {
        "host": "mock-server.com",
        "port": 443,
        "scheme": "HTTPS"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "path": "/some/path"
    },
    "httpForward": {
        "host": "mock-server.com",
        "port": 443,
        "scheme": "HTTPS"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

forward overridden request

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
    )
    .forward(
        forwardOverriddenRequest(
            request()
                .withPath("/some/other/path")
                .withHeader("Host", "target.host.com")
        )
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some/path"
    },
    "httpOverrideForwardedRequest": {
        "httpRequest": {
            "path": "/some/other/path",
            "headers": {
                "Host": ["target.host.com"]
            }
        }
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "path": "/some/path"
    },
    "httpOverrideForwardedRequest": {
        "httpRequest": {
            "path": "/some/other/path",
            "headers": {
                "Host": ["target.host.com"]
            }
        }
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

forward overridden request and response

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
    )
    .forward(
        forwardOverriddenRequest(
            request()
                .withPath("/some/other/path")
                .withHeader("Host", "target.host.com"),
            response()
                .withBody("some_overridden_body")
        )
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some/path"
    },
    "httpOverrideForwardedRequest": {
        "httpRequest": {
            "path": "/some/other/path",
            "headers": {
                "Host": ["target.host.com"]
            }
        },
        "httpResponse": {
            "body": "some_overridden_body"
        }
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "path": "/some/path"
    },
    "httpOverrideForwardedRequest": {
        "httpRequest": {
            "path": "/some/other/path",
            "headers": {
                "Host": ["target.host.com"]
            }
        },
        "httpResponse": {
            "body": "some_overridden_body"
        }
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

forward overridden and modified request

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
    )
    .forward(
        forwardOverriddenRequest(
            request()
                // this replaces the entire set of headers
                .withHeader("Host", "target.host.com")
                .withBody("some_overridden_body"),
            requestModifier()
                .withPath("^/(.+)/(.+)$", "/prefix/$1/infix/$2/postfix")
                .withQueryStringParameters(
                    queryParametersModifier()
                        .add(
                            param("parameterToAddOne", "addedValue"),
                            param("parameterToAddTwo", "addedValue")
                        )
                        .replace(
                            param("overrideParameterToReplace", "replacedValue"),
                            param("requestParameterToReplace", "replacedValue"),
                            param("extraParameterToReplace", "shouldBeIgnore")
                        )
                        .remove(
                            "overrideParameterToRemove",
                            "requestParameterToRemove"
                        )

                )
                // this modifies the set of headers
                .withHeaders(
                    headersModifier()
                        .add(
                            header("headerToAddOne", "addedValue"),
                            header("headerToAddTwo", "addedValue")
                        )
                        .replace(
                            header("overrideHeaderToReplace", "replacedValue"),
                            header("requestHeaderToReplace", "replacedValue"),
                            header("extraHeaderToReplace", "shouldBeIgnore")
                        )
                        .remove(
                            "overrideHeaderToRemove",
                            "requestHeaderToRemove"
                        )

                )
                .withCookies(
                    cookiesModifier()
                        .add(
                            cookie("cookieToAddOne", "addedValue"),
                            cookie("cookieToAddTwo", "addedValue")
                        )
                        .replace(
                            cookie("overrideCookieToReplace", "replacedValue"),
                            cookie("requestCookieToReplace", "replacedValue"),
                            cookie("extraCookieToReplace", "shouldBeIgnore")
                        )
                        .remove(
                            "overrideCookieToRemove",
                            "requestCookieToRemove"
                        )

                )
        )
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some/path"
    },
    "httpOverrideForwardedRequest": {
        "requestOverride": {
            "headers": {
                "Host": [
                    "target.host.com"
                ]
            },
            "body": "some_overridden_body"
        },
        "requestModifier": {
            "cookies": {
                "add": {
                    "cookieToAddOne": "addedValue",
                    "cookieToAddTwo": "addedValue"
                },
                "remove": [
                    "overrideCookieToRemove",
                    "requestCookieToRemove"
                ],
                "replace": {
                    "overrideCookieToReplace": "replacedValue",
                    "requestCookieToReplace": "replacedValue",
                    "extraCookieToReplace": "shouldBeIgnore"
                }
            },
            "headers": {
                "add": {
                    "headerToAddTwo": [
                        "addedValue"
                    ],
                    "headerToAddOne": [
                        "addedValue"
                    ]
                },
                "remove": [
                    "overrideHeaderToRemove",
                    "requestHeaderToRemove"
                ],
                "replace": {
                    "requestHeaderToReplace": [
                        "replacedValue"
                    ],
                    "overrideHeaderToReplace": [
                        "replacedValue"
                    ],
                    "extraHeaderToReplace": [
                        "shouldBeIgnore"
                    ]
                }
            },
            "path": {
                "regex": "^/(.+)/(.+)$",
                "substitution": "/prefix/$1/infix/$2/postfix"
            },
            "queryStringParameters": {
                "add": {
                    "parameterToAddTwo": [
                        "addedValue"
                    ],
                    "parameterToAddOne": [
                        "addedValue"
                    ]
                },
                "remove": [
                    "overrideParameterToRemove",
                    "requestParameterToRemove"
                ],
                "replace": {
                    "requestParameterToReplace": [
                        "replacedValue"
                    ],
                    "overrideParameterToReplace": [
                        "replacedValue"
                    ],
                    "extraParameterToReplace": [
                        "shouldBeIgnore"
                    ]
                }
            }
        }
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "path": "/some/path"
    },
    "httpOverrideForwardedRequest": {
        "requestOverride": {
            "headers": {
                "Host": [
                    "target.host.com"
                ]
            },
            "body": "some_overridden_body"
        },
        "requestModifier": {
            "cookies": {
                "add": {
                    "cookieToAddOne": "addedValue",
                    "cookieToAddTwo": "addedValue"
                },
                "remove": [
                    "overrideCookieToRemove",
                    "requestCookieToRemove"
                ],
                "replace": {
                    "overrideCookieToReplace": "replacedValue",
                    "requestCookieToReplace": "replacedValue",
                    "extraCookieToReplace": "shouldBeIgnore"
                }
            },
            "headers": {
                "add": {
                    "headerToAddTwo": [
                        "addedValue"
                    ],
                    "headerToAddOne": [
                        "addedValue"
                    ]
                },
                "remove": [
                    "overrideHeaderToRemove",
                    "requestHeaderToRemove"
                ],
                "replace": {
                    "requestHeaderToReplace": [
                        "replacedValue"
                    ],
                    "overrideHeaderToReplace": [
                        "replacedValue"
                    ],
                    "extraHeaderToReplace": [
                        "shouldBeIgnore"
                    ]
                }
            },
            "path": {
                "regex": "^/(.+)/(.+)$",
                "substitution": "/prefix/$1/infix/$2/postfix"
            },
            "queryStringParameters": {
                "add": {
                    "parameterToAddTwo": [
                        "addedValue"
                    ],
                    "parameterToAddOne": [
                        "addedValue"
                    ]
                },
                "remove": [
                    "overrideParameterToRemove",
                    "requestParameterToRemove"
                ],
                "replace": {
                    "requestParameterToReplace": [
                        "replacedValue"
                    ],
                    "overrideParameterToReplace": [
                        "replacedValue"
                    ],
                    "extraParameterToReplace": [
                        "shouldBeIgnore"
                    ]
                }
            }
        }
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

forward overridden and modified request and response

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
    )
    .forward(
        forwardOverriddenRequest()
            .withRequestOverride(
                request()
                    // this replaces the entire set of headers
                    .withHeader("Host", "target.host.com")
                    .withBody("some_overridden_body")
            )
            .withRequestModifier(
                requestModifier()
                    .withPath("^/(.+)/(.+)$", "/prefix/$1/infix/$2/postfix")
                    .withQueryStringParameters(
                        queryParametersModifier()
                            .add(
                                param("parameterToAddOne", "addedValue"),
                                param("parameterToAddTwo", "addedValue")
                            )
                            .replace(
                                param("overrideParameterToReplace", "replacedValue"),
                                param("requestParameterToReplace", "replacedValue"),
                                param("extraParameterToReplace", "shouldBeIgnore")
                            )
                            .remove(
                                "overrideParameterToRemove",
                                "requestParameterToRemove"
                            )

                    )
                    // this modifies the set of headers
                    .withHeaders(
                        headersModifier()
                            .add(
                                header("headerToAddOne", "addedValue"),
                                header("headerToAddTwo", "addedValue")
                            )
                            .replace(
                                header("overrideHeaderToReplace", "replacedValue"),
                                header("requestHeaderToReplace", "replacedValue"),
                                header("extraHeaderToReplace", "shouldBeIgnore")
                            )
                            .remove(
                                "overrideHeaderToRemove",
                                "requestHeaderToRemove"
                            )

                    )
                    .withCookies(
                        cookiesModifier()
                            .add(
                                cookie("cookieToAddOne", "addedValue"),
                                cookie("cookieToAddTwo", "addedValue")
                            )
                            .replace(
                                cookie("overrideCookieToReplace", "replacedValue"),
                                cookie("requestCookieToReplace", "replacedValue"),
                                cookie("extraCookieToReplace", "shouldBeIgnore")
                            )
                            .remove(
                                "overrideCookieToRemove",
                                "requestCookieToRemove"
                            )

                    )
            )
            .withResponseOverride(
                response()
                    .withBody("some_overridden_body")
            )
            .withResponseModifier(
                responseModifier()
                    .withHeaders(
                        headersModifier()
                            .add(
                                header("headerToAddOne", "addedValue"),
                                header("headerToAddTwo", "addedValue")
                            )
                            .replace(
                                header("overrideHeaderToReplace", "replacedValue"),
                                header("requestHeaderToReplace", "replacedValue"),
                                header("extraHeaderToReplace", "shouldBeIgnore")
                            )
                            .remove(
                                "overrideHeaderToRemove",
                                "requestHeaderToRemove"
                            )

                    )
                    .withCookies(
                        cookiesModifier()
                            .add(
                                cookie("cookieToAddOne", "addedValue"),
                                cookie("cookieToAddTwo", "addedValue")
                            )
                            .replace(
                                cookie("overrideCookieToReplace", "replacedValue"),
                                cookie("requestCookieToReplace", "replacedValue"),
                                cookie("extraCookieToReplace", "shouldBeIgnore")
                            )
                            .remove(
                                "overrideCookieToRemove",
                                "requestCookieToRemove"
                            )

                    )
            )
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some/path"
    },
    "httpOverrideForwardedRequest": {
        "requestOverride": {
            "headers": {
                "Host": [
                    "target.host.com"
                ]
            },
            "body": "some_overridden_body"
        },
        "requestModifier": {
            "cookies": {
                "add": {
                    "cookieToAddOne": "addedValue",
                    "cookieToAddTwo": "addedValue"
                },
                "remove": [
                    "overrideCookieToRemove",
                    "requestCookieToRemove"
                ],
                "replace": {
                    "overrideCookieToReplace": "replacedValue",
                    "requestCookieToReplace": "replacedValue",
                    "extraCookieToReplace": "shouldBeIgnore"
                }
            },
            "headers": {
                "add": {
                    "headerToAddTwo": [
                        "addedValue"
                    ],
                    "headerToAddOne": [
                        "addedValue"
                    ]
                },
                "remove": [
                    "overrideHeaderToRemove",
                    "requestHeaderToRemove"
                ],
                "replace": {
                    "requestHeaderToReplace": [
                        "replacedValue"
                    ],
                    "overrideHeaderToReplace": [
                        "replacedValue"
                    ],
                    "extraHeaderToReplace": [
                        "shouldBeIgnore"
                    ]
                }
            },
            "path": {
                "regex": "^/(.+)/(.+)$",
                "substitution": "/prefix/$1/infix/$2/postfix"
            },
            "queryStringParameters": {
                "add": {
                    "parameterToAddTwo": [
                        "addedValue"
                    ],
                    "parameterToAddOne": [
                        "addedValue"
                    ]
                },
                "remove": [
                    "overrideParameterToRemove",
                    "requestParameterToRemove"
                ],
                "replace": {
                    "requestParameterToReplace": [
                        "replacedValue"
                    ],
                    "overrideParameterToReplace": [
                        "replacedValue"
                    ],
                    "extraParameterToReplace": [
                        "shouldBeIgnore"
                    ]
                }
            }
        },
        "responseOverride": {
            "body": "some_overridden_body"
        },
        "responseModifier": {
            "cookies": {
                "add": {
                    "cookieToAddOne": "addedValue",
                    "cookieToAddTwo": "addedValue"
                },
                "remove": [
                    "overrideCookieToRemove",
                    "requestCookieToRemove"
                ],
                "replace": {
                    "overrideCookieToReplace": "replacedValue",
                    "requestCookieToReplace": "replacedValue",
                    "extraCookieToReplace": "shouldBeIgnore"
                }
            },
            "headers": {
                "add": {
                    "headerToAddTwo": [
                        "addedValue"
                    ],
                    "headerToAddOne": [
                        "addedValue"
                    ]
                },
                "remove": [
                    "overrideHeaderToRemove",
                    "requestHeaderToRemove"
                ],
                "replace": {
                    "requestHeaderToReplace": [
                        "replacedValue"
                    ],
                    "overrideHeaderToReplace": [
                        "replacedValue"
                    ],
                    "extraHeaderToReplace": [
                        "shouldBeIgnore"
                    ]
                }
            }
        }
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "path": "/some/path"
    },
    "httpOverrideForwardedRequest": {
        "requestOverride": {
            "headers": {
                "Host": [
                    "target.host.com"
                ]
            },
            "body": "some_overridden_body"
        },
        "requestModifier": {
            "cookies": {
                "add": {
                    "cookieToAddOne": "addedValue",
                    "cookieToAddTwo": "addedValue"
                },
                "remove": [
                    "overrideCookieToRemove",
                    "requestCookieToRemove"
                ],
                "replace": {
                    "overrideCookieToReplace": "replacedValue",
                    "requestCookieToReplace": "replacedValue",
                    "extraCookieToReplace": "shouldBeIgnore"
                }
            },
            "headers": {
                "add": {
                    "headerToAddTwo": [
                        "addedValue"
                    ],
                    "headerToAddOne": [
                        "addedValue"
                    ]
                },
                "remove": [
                    "overrideHeaderToRemove",
                    "requestHeaderToRemove"
                ],
                "replace": {
                    "requestHeaderToReplace": [
                        "replacedValue"
                    ],
                    "overrideHeaderToReplace": [
                        "replacedValue"
                    ],
                    "extraHeaderToReplace": [
                        "shouldBeIgnore"
                    ]
                }
            },
            "path": {
                "regex": "^/(.+)/(.+)$",
                "substitution": "/prefix/$1/infix/$2/postfix"
            },
            "queryStringParameters": {
                "add": {
                    "parameterToAddTwo": [
                        "addedValue"
                    ],
                    "parameterToAddOne": [
                        "addedValue"
                    ]
                },
                "remove": [
                    "overrideParameterToRemove",
                    "requestParameterToRemove"
                ],
                "replace": {
                    "requestParameterToReplace": [
                        "replacedValue"
                    ],
                    "overrideParameterToReplace": [
                        "replacedValue"
                    ],
                    "extraParameterToReplace": [
                        "shouldBeIgnore"
                    ]
                }
            }
        },
        "responseOverride": {
            "body": "some_overridden_body"
        },
        "responseModifier": {
            "cookies": {
                "add": {
                    "cookieToAddOne": "addedValue",
                    "cookieToAddTwo": "addedValue"
                },
                "remove": [
                    "overrideCookieToRemove",
                    "requestCookieToRemove"
                ],
                "replace": {
                    "overrideCookieToReplace": "replacedValue",
                    "requestCookieToReplace": "replacedValue",
                    "extraCookieToReplace": "shouldBeIgnore"
                }
            },
            "headers": {
                "add": {
                    "headerToAddTwo": [
                        "addedValue"
                    ],
                    "headerToAddOne": [
                        "addedValue"
                    ]
                },
                "remove": [
                    "overrideHeaderToRemove",
                    "requestHeaderToRemove"
                ],
                "replace": {
                    "requestHeaderToReplace": [
                        "replacedValue"
                    ],
                    "overrideHeaderToReplace": [
                        "replacedValue"
                    ],
                    "extraHeaderToReplace": [
                        "shouldBeIgnore"
                    ]
                }
            }
        }
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

forward overridden request and change host and port

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
    )
    .forward(
        forwardOverriddenRequest(
            request()
                .withPath("/some/other/path")
                .withHeader("Host", "any.host.com")
                .withSocketAddress("target.host.com", 1234, SocketAddress.Scheme.HTTPS)
        )
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some/path"
    },
    "httpOverrideForwardedRequest": {
        "httpRequest": {
            "path": "/some/other/path",
            "headers": {
                "Host": ["any.host.com"]
            },
            "socketAddress": {
                "host": "target.host.com",
                "port": 1234,
                "scheme": "HTTPS"
            }
        }
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "path": "/some/path"
    },
    "httpOverrideForwardedRequest": {
        "httpRequest": {
            "path": "/some/other/path",
            "headers": {
                "Host": ["any.host.com"]
            },
            "socketAddress": {
                "host": "target.host.com",
                "port": 1234,
                "scheme": "HTTPS"
            }
        }
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

forward overridden request with delay

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
    )
    .forward(
        forwardOverriddenRequest(
            request()
                .withHeader("Host", "target.host.com")
                .withBody("some_overridden_body")
        ).withDelay(SECONDS, 10)
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some/path"
    },
    "httpOverrideForwardedRequest": {
        "httpRequest": {
            "path": "/some/other/path",
            "body": "some_overridden_body",
            "headers": {
                "Host": ["target.host.com"]
            }
        },
        "delay": {
            "timeUnit": "SECONDS",
            "value": 10
        }
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "path": "/some/path"
    },
    "httpOverrideForwardedRequest": {
        "httpRequest": {
            "path": "/some/other/path",
            "body": "some_overridden_body",
            "headers": {
                "Host": ["target.host.com"]
            }
        },
        "delay": {
            "timeUnit": "SECONDS",
            "value": 10
        }
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

javascript templated forward

Java

```
// request.queryStringParameters['userId'] returns an array of values because headers and queryStringParameters have multiple values
String template = "return {\n" +
    "    'path' : \"/somePath\",\n" +
    "    'queryStringParameters' : {\n" +
    "        'userId' : request.queryStringParameters && request.queryStringParameters['userId']\n" +
    "    },\n" +
    "    'headers' : {\n" +
    "        'Host' : [ \"localhost:1081\" ]\n" +
    "    },\n" +
    "    'body': JSON.stringify({'name': 'value'})\n" +
    "};";

new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
    )
    .forward(
        template(
            HttpTemplate.TemplateType.JAVASCRIPT,
            template
        )
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
// request.queryStringParameters['userId'] returns an array of values because headers and queryStringParameters have multiple values
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some/path"
    },
    "httpForwardTemplate": {
        "template": "return {\n" +
        "    'path' : \"/somePath\",\n" +
        "    'queryStringParameters' : {\n" +
        "        'userId' : request.queryStringParameters && request.queryStringParameters['userId']\n" +
        "    },\n" +
        "    'headers' : {\n" +
        "        'Host' : [ \"localhost:1081\" ]\n" +
        "    },\n" +
        "    'body': JSON.stringify({'name': 'value'})\n" +
        "};",
        "templateType": "JAVASCRIPT"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "path": "/some/path"
    },
    "httpForwardTemplate": {
        "template": "return {\n" +
        "    'path' : \"/somePath\",\n" +
        "    'queryStringParameters' : {\n" +
        "        'userId' : request.queryStringParameters && request.queryStringParameters['userId']\n" +
        "    },\n" +
        "    'headers' : {\n" +
        "        'Host' : [ \"localhost:1081\" ]\n" +
        "    },\n" +
        "    'body': JSON.stringify({'name': 'value'})\n" +
        "};",
        "templateType": "JAVASCRIPT"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

javascript templated forward stripping path prefix

Java

```
String template = "return {" + System.getProperty("line.separator") +
    "    'path' : request.path.substring(request.path.indexOf('/somePrefix')+'/somePrefix'.length,request.path.length)," + System.getProperty("line.separator") +
    "    'headers' : {" + System.getProperty("line.separator") +
    "        'Host' : [ \"localhost:1081\" ]" + System.getProperty("line.separator") +
    "    }," + System.getProperty("line.separator") +
    "};";

new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/somePrefix*")
    )
    .forward(
        template(
            HttpTemplate.TemplateType.JAVASCRIPT,
            template
        )
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/somePrefix*"
    },
    "httpForwardTemplate": {
        "template": "return {\n" +
        "    'path' : request.path.substring(request.path.indexOf('/somePrefix')+'/somePrefix'.length,request.path.length),\n" +
        "    'headers' : {\n" +
        "        'Host' : [ \"localhost:1081\" ]\n" +
        "    }
        "};",
        "templateType": "JAVASCRIPT"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "path": "/somePrefix*"
    },
    "httpForwardTemplate": {
        "template": "return {\n" +
        "    'path' : request.path.substring(request.path.indexOf('/somePrefix')+'/somePrefix'.length,request.path.length),\n" +
        "    'headers' : {\n" +
        "        'Host' : [ \"localhost:1081\" ]\n" +
        "    }\n" +
        "};",
        "templateType": "JAVASCRIPT"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

javascript templated forward with delay

Java

```
// request.cookies['SessionId'] returns a single value because cookies only contain a single value
String template = "return {\n" +
    "    'path' : \"/somePath\",\n" +
    "    'cookies' : {\n" +
    "        'SessionId' : request.cookies && request.cookies['SessionId']\n" +
    "    },\n" +
    "    'headers' : {\n" +
    "        'Host' : [ \"localhost:1081\" ]\n" +
    "    },\n" +
    "    'keepAlive' : true,\n" +
    "    'secure' : true,\n" +
    "    'body' : \"some_body\"\n" +
    "};";

new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
    )
    .forward(
        template(HttpTemplate.TemplateType.JAVASCRIPT)
            .withTemplate(template)
            .withDelay(TimeUnit.SECONDS, 20)
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
// request.cookies['SessionId'] returns a single value because cookies only contain a single value
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some/path"
    },
    "httpForwardTemplate": {
        "template": "return {\n" +
        "    'path' : \"/somePath\",\n" +
        "    'cookies' : {\n" +
        "        'SessionId' : request.cookies && request.cookies['SessionId']\n" +
        "    },\n" +
        "    'headers' : {\n" +
        "        'Host' : [ \"localhost:1081\" ]\n" +
        "    },\n" +
        "    'keepAlive' : true,\n" +
        "    'secure' : true,\n" +
        "    'body' : \"some_body\"\n" +
        "};",
        "templateType": "JAVASCRIPT",
        "delay": {"timeUnit": "SECONDS", "value": 20}
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "path": "/some/path"
    },
    "httpForwardTemplate": {
        "template": "return {\n" +
        "    'path' : \"/somePath\",\n" +
        "    'cookies' : {\n" +
        "        'SessionId' : request.cookies && request.cookies['SessionId']\n" +
        "    },\n" +
        "    'headers' : {\n" +
        "        'Host' : [ \"localhost:1081\" ]\n" +
        "    },\n" +
        "    'keepAlive' : true,\n" +
        "    'secure' : true,\n" +
        "    'body' : \"some_body\"\n" +
        "};",
        "templateType": "JAVASCRIPT",
        "delay": {"timeUnit": "SECONDS", "value": 20}
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

velocity templated forward

Java

```
// $!request.queryStringParameters['userId'] returns an array of values because headers and queryStringParameters have multiple values
String template = "{\n" +
    "    'path' : \"/somePath\",\n" +
    "    'queryStringParameters' : {\n" +
    "        'userId' : [ \"$!request.queryStringParameters['userId'][0]\" ]\n" +
    "    },\n" +
    "    'cookies' : {\n" +
    "        'SessionId' : \"$!request.cookies['SessionId']\"\n" +
    "    },\n" +
    "    'headers' : {\n" +
    "        'Host' : [ \"localhost:1081\" ]\n" +
    "    },\n" +
    "    'body': \"{'name': 'value'}\"\n" +
    "}";

new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
    )
    .forward(
        template(
            HttpTemplate.TemplateType.VELOCITY,
            template
        )
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
// $!request.queryStringParameters['userId'] returns an array of values because headers and queryStringParameters have multiple values
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some/path"
    },
    "httpForwardTemplate": {
        "template": "{\n" +
        "    'path' : \"/somePath\",\n" +
        "    'queryStringParameters' : {\n" +
        "        'userId' : [ \"$!request.queryStringParameters['userId'][0]\" ]\n" +
        "    },\n" +
        "    'cookies' : {\n" +
        "        'SessionId' : \"$!request.cookies['SessionId']\"\n" +
        "    },\n" +
        "    'headers' : {\n" +
        "        'Host' : [ \"localhost:1081\" ]\n" +
        "    },\n" +
        "    'body': \"{'name': 'value'}\"\n" +
        "}",
        "templateType": "VELOCITY"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "path": "/some/path"
    },
    "httpForwardTemplate": {
        "template": "{\n" +
        "    'path' : \"/somePath\",\n" +
        "    'queryStringParameters' : {\n" +
        "        'userId' : [ \"$!request.queryStringParameters['userId'][0]\" ]\n" +
        "    },\n" +
        "    'cookies' : {\n" +
        "        'SessionId' : \"$!request.cookies['SessionId']\"\n" +
        "    },\n" +
        "    'headers' : {\n" +
        "        'Host' : [ \"localhost:1081\" ]\n" +
        "    },\n" +
        "    'body': \"{'name': 'value'}\"\n" +
        "}",
        "templateType": "VELOCITY"
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.9.x#/expectation/put_expectation) for full JSON specification

class callback to override request & response

Java

```
public class CallbackActionExamples {

    public void forwardClassCallback() {
        new ClientAndServer(1080)
            .when(
                request()
                    .withPath("/some.*")
            )
            .forward(
                callback()
                    .withCallbackClass(TestExpectationForwardCallback.class)
            );
    }

    public static class TestExpectationForwardCallback implements ExpectationForwardCallback {

        @Override
        public HttpRequest handle(HttpRequest httpRequest) {
            return request()
                .withPath(httpRequest.getPath())
                .withMethod("POST")
                .withHeaders(
                    header("x-callback", "test_callback_header"),
                    header("Content-Length", "a_callback_request".getBytes(UTF_8).length),
                    header("Connection", "keep-alive")
                )
                .withBody("a_callback_request");
        }
    }

}
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some.*"
    },
    "httpForwardClassCallback": {
        "callbackClass": "org.mockserver.examples.mockserver.CallbackActionExamples$TestExpectationForwardCallback"
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest" : {
        "path" : "/some.*"
    },
    "httpForwardClassCallback" : {
        "callbackClass" : "org.mockserver.examples.mockserver.CallbackActionExamples$TestExpectationForwardCallback"
    }
}'
```

To use a class callback MockServer must be able to **load the class from the classpath**.

The callback class must:

* implement
  * **org.mockserver.mock.action.ExpectationForwardCallback** to dynamically override the **request** or
  * **org.mockserver.mock.action.ExpectationForwardAndResponseCallback** to dynamically override the **request** and the **response**
* have a zero argument constructor
* be available in the classpath of the MockServer

If MockServer is started using the [JUnit 4 @Rule](/mock_server/running_mock_server.html#junit_rule), the [JUnit 5 Test Extension](/mock_server/running_mock_server.html#junit_test_extension), [ClientAndServer](/mock_server/running_mock_server.html#client_api) or directly using org.mockserver.netty.MockServer then any class present in the main or test classpaths will be visible to MockServer.

If MockServer is started using the [maven plugin](/mock_server/running_mock_server.html#maven_plugin) only the non-forked goals (such as runAndWait and start) will be able to load classes from the main and test classpaths. It is possible to use classes from a separate maven dependency, however, this dependency must be specified in the plugin configuration dependencies section. Any dependency added to the plugin configuration dependencies section will then be visible to MockServer run using both forked and non-forked goals.

The following configuration shows how to use classes from a separate maven dependency in callback actions.

```
 <plugin>
     <groupId>org.mock-server</groupId>
     <artifactId>mockserver-maven-plugin</artifactId>
     <version>5.14.0</version>
     <configuration>
        <serverPort>1080</serverPort>
        <logLevel>DEBUG</logLevel>
        <pipeLogToConsole>true</pipeLogToConsole>
     </configuration>
     <executions>
         <execution>
             <id>pre-integration-test</id>
             <phase>pre-integration-test</phase>
             <goals>
                 <goal>runForked</goal>
             </goals>
         </execution>
         <execution>
             <id>post-integration-test</id>
             <phase>post-integration-test</phase>
             <goals>
                 <goal>stopForked</goal>
             </goals>
         </execution>
     </executions>
     <dependencies>
         <dependency>
             <groupId>com.my-domain</groupId>
             <artifactId>my-callback-dependency</artifactId>
             <version>1.0.0</version>
         </dependency>
     </dependencies>
 </plugin>
```

If MockServer is started using the [command line](/mock_server/running_mock_server.html#running_from_command_line) then the callback classes must be added to the JVM using the classpath command line switch (**cp** or **classpath**). The **classpath** switch is ignored by the JVM if the
**jar** switch is used. So to run the MockServer from the command line directly (with mockserver-netty-5.14.0-shaded.jar) you must specify the **org.mockserver.cli.Main** main class specifically and not use the **jar** switch as follows.

```
java -Dfile.encoding=UTF-8 -cp mockserver-netty-5.14.0-shaded.jar:my-callback-dependency.jar org.mockserver.cli.Main -serverPort 1080
```

method / closure callback to override request

Java 7

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
    )
    .forward(
        new ExpectationForwardCallback() {
            @Override
            public HttpRequest handle(HttpRequest httpRequest) {
                return request()
                    .withPath(httpRequest.getPath())
                    .withMethod("POST")
                    .withHeaders(
                        header("x-callback", "test_callback_header"),
                        header("Content-Length", "a_callback_request".getBytes(UTF_8).length),
                        header("Connection", "keep-alive")
                    )
                    .withBody("a_callback_request");
            }
        }
    );
```

Java 8+

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
    )
    .forward(
        httpRequest -> request()
                    .withPath(httpRequest.getPath())
                    .withMethod("POST")
                    .withHeaders(
                        header("x-callback", "test_callback_header"),
                        header("Content-Length", "a_callback_request".getBytes(UTF_8).length),
                        header("Connection", "keep-alive")
                    )
                    .withBody("a_callback_request")
    );
```

When using org.mockserver.client.MockServerClient each method / closure callback has a separate web socket client. To ensure the number of total threads does not grow too large for large numbers of method / closure callback expectations the default event loop thread pool for the web socket client is kept fairly low. However, if an extremely large load is matched against a single method / closure callback expectation the event loop thread pool may not be large enough for its web socket client.

The number of threads for the event loop thread pool for each web socket client (i.e. for each expectation with a method / closure callback) [can be configured and is described in the configuration section](/mock_server/configuration_properties.html#button_configuration_web_socket_event_loop_thread_count).

method / closure callback to override request & response

Java 7

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
    )
    .forward(
        new ExpectationForwardCallback() {
            @Override
            public HttpRequest handle(HttpRequest httpRequest) throws Exception {
                return request()
                    .withPath(httpRequest.getPath())
                    .withMethod("POST")
                    .withHeaders(
                        header("x-callback", "test_callback_header"),
                        header("Content-Length", "a_callback_request".getBytes(UTF_8).length),
                        header("Connection", "keep-alive")
                    )
                    .withBody("a_callback_request");
            }
        },
        new ExpectationForwardAndResponseCallback() {
            @Override
            public HttpResponse handle(HttpRequest httpRequest, HttpResponse httpResponse) throws Exception {
                return httpResponse
                    .withHeader("x-response-test", "x-response-test")
                    .removeHeader(CONTENT_LENGTH.toString())
                    .withBody("some_overridden_response_body");
            }
        }
    );
```

Java 8+

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
    )
    .forward(
        httpRequest ->
            request()
                .withPath(httpRequest.getPath())
                .withMethod("POST")
                .withHeaders(
                    header("x-callback", "test_callback_header"),
                    header("Content-Length", "a_callback_request".getBytes(UTF_8).length),
                    header("Connection", "keep-alive")
                )
                .withBody("a_callback_request"),
        (httpRequest, httpResponse) ->
            httpResponse
                .withHeader("x-response-test", "x-response-test")
                .removeHeader(CONTENT_LENGTH.toString())
                .withBody("some_overridden_response_body")
    );
```

When using org.mockserver.client.MockServerClient each method / closure callback has a separate web socket client. To ensure the number of total threads does not grow too large for large numbers of method / closure callback expectations the default event loop thread pool for the web socket client is kept fairly low. However, if an extremely large load is matched against a single method / closure callback expectation the event loop thread pool may not be large enough for its web socket client.

The number of threads for the event loop thread pool for each web socket client (i.e. for each expectation with a method / closure callback) [can be configured and is described in the configuration section](/mock_server/configuration_properties.html#button_configuration_web_socket_event_loop_thread_count).

An **error action** can return an invalid response as a [sequence of bytes](#button_random_bytes_error) or [drop the connection](#button_drop_connection_error)

**Error Action Code Examples**

The following code examples show how to create different error actions.

random bytes error

Java

```
// generate random bytes
byte[] randomByteArray = new byte[25];
new Random().nextBytes(randomByteArray);

new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
    )
    .error(
        error()
            .withDropConnection(true)
            .withResponseBytes(randomByteArray)
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "path": "/some/path"
    },
    "httpError": {
        "dropConnection": true,
        "responseBytes": "eQqmdjEEoaXnCvcK6lOAIZeU+Pn+womxmg=="
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest": {
        "path": "/some/path"
    },
    "httpError": {
        "dropConnection": true,
        "responseBytes": "eQqmdjEEoaXnCvcK6lOAIZeU+Pn+womxmg=="
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

drop connection error

Java

```
new MockServerClient("localhost", 1080)
    .when(
        request()
            .withPath("/some/path")
    )
    .error(
        error()
            .withDropConnection(true)
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest" : {
        "path" : "/some/path"
    },
    "httpError" : {
        "dropConnection" : true
    }
}).then(
    function () {
        console.log("expectation created");
    },
    function (error) {
        console.log(error);
    }
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
    "httpRequest" : {
        "path" : "/some/path"
    },
    "httpError" : {
        "dropConnection" : true
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/expectation/put_expectation) for full JSON specification

1. Verify Requests

------------------

MockServer supports verification of requests is has received, including both proxied requests and requests that have matched an expectation.

Verification can be specified as follows:

* a [**request matcher**](/mock_server/getting_started.html#request_matchers) and a condition indicating the number of times the request should be matched
* a sequence of [**request matchers**](/mock_server/getting_started.html#request_matchers) that is matched in order

### Verifying Repeating Requests

Verify that a request has been received by MockServer a specific number of times using a **Verification**

**Verify Repeating Requests Code Examples**

verify requests received at least twice

Java

```
new MockServerClient("localhost", 1080)
    .verify(
        request()
            .withPath("/some/path"),
        VerificationTimes.atLeast(2)
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080)
  .verify(
    {
      'path': '/some/path'
    }, 2)
  .then(
    function () {
      console.log("request found exactly 2 times");
    },
    function (error) {
      console.log(error);
    }
  );
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/verify/put_verify) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/verify" -d '{
    "httpRequest": {
        "path": "/simple"
    },
    "times": {
        "atLeast": 2
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/verify/put_verify) for full JSON specification

verify requests received at most twice

Java

```
new MockServerClient("localhost", 1080)
.verify(
    request()
        .withPath("/some/path"),
    VerificationTimes.atMost(2)
);
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080)
.verify(
{
  'path': '/some/path'
}, 0, 2)
.then(
function () {
  console.log("request found exactly 2 times");
},
function (error) {
  console.log(error);
}
);
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/verify/put_verify) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/verify" -d '{
    "httpRequest": {
        "path": "/simple"
    },
    "times": {
        "atMost": 2
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/verify/put_verify) for full JSON specification

verify requests received exactly twice

Java

```
new MockServerClient("localhost", 1080)
    .verify(
        request()
            .withPath("/some/path"),
        VerificationTimes.exactly(2)
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080)
  .verify(
    {
      'path': '/some/path'
    }, 2, 2)
  .then(
    function () {
      console.log("request found exactly 1 times");
    },
    function (error) {
      console.log(error);
    }
  );
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/verify/put_verify) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/verify" -d '{
    "httpRequest": {
        "path": "/simple"
    },
    "times": {
        "atLeast": 2,
        "atMost": 2
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/verify/put_verify) for full JSON specification

verify requests received at least twice by openapi

Java

```
new MockServerClient("localhost", 1080)
    .verify(
        openAPI(
            "https://raw.githubusercontent.com/mock-server/mockserver/master/mockserver-integration-testing/src/main/resources/org/mockserver/openapi/openapi_petstore_example.json"
        ),
        VerificationTimes.atLeast(2)
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080)
    .verify(
        {
            'specUrlOrPayload': 'https://raw.githubusercontent.com/mock-server/mockserver/master/mockserver-integration-testing/src/main/resources/org/mockserver/openapi/openapi_petstore_example.json'
        }, 2)
    .then(
        function () {
            console.log("request found exactly 2 times");
        },
        function (error) {
            console.log(error);
        }
    );
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/verify/put_verify) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/verify" -d '{
    "httpRequest": {
        "specUrlOrPayload": "https://raw.githubusercontent.com/mock-server/mockserver/master/mockserver-integration-testing/src/main/resources/org/mockserver/openapi/openapi_petstore_example.json"
    },
    "times": {
        "atLeast": 2
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/verify/put_verify) for full JSON specification

verify requests received at exactly once by openapi and operation

Java

```
new MockServerClient("localhost", 1080)
    .verify(
        openAPI(
            "org/mockserver/openapi/openapi_petstore_example.json",
            "showPetById"
        ),
        VerificationTimes.once()
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080)
    .verify(
        {
            'specUrlOrPayload': 'org/mockserver/openapi/openapi_petstore_example.json',
            'operationId': 'showPetById'
        }, 1, 1)
    .then(
        function () {
            console.log("request found exactly 2 times");
        },
        function (error) {
            console.log(error);
        }
    );
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/verify/put_verify) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/verify" -d '{
    "httpRequest": {
        "specUrlOrPayload": "org/mockserver/openapi/openapi_petstore_example.json",
        "operationId": "showPetById"
    },
    "times": {
        "atLeast": 1,
        "atMost": 1
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/verify/put_verify) for full JSON specification

verify requests received at exactly once by expectation id

Java

```
new MockServerClient("localhost", 1080)
    .verify(
        "31e4ca35-66c6-4645-afeb-6e66c4ca0559",
        VerificationTimes.once()
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080)
    .verifyById(
        {
            'id': '31e4ca35-66c6-4645-afeb-6e66c4ca0559'
        }, 1, 1)
    .then(
        function () {
            console.log("request found exactly 2 times");
        },
        function (error) {
            console.log(error);
        }
    );
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/verify/put_verify) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/verify" -d '{
            "id": "31e4ca35-66c6-4645-afeb-6e66c4ca0559"
        }'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/verify/put_verify) for full JSON specification

verify requests never received

Java

```
new MockServerClient("localhost", 1080)
    .verify(
        request()
            .withPath("/some/path"),
        VerificationTimes.exactly(0)
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080)
  .verify(
    {
      'path': '/some/path'
    }, 0, true)
  .then(
    function () {
      console.log("request found zero times");
    },
    function (error) {
      console.log(error);
    }
  );
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/verify/put_verify) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/verify" -d '{
    "httpRequest": {
        "path": "/simple"
    },
    "times": {
        "atMost": 0
    }
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/verify/put_verify) for full JSON specification

### Verifying Request Sequences

Verify that a sequence of requests has been received by MockServer in the specified order using a **VerificationSequence**

The each request in the sequence will be verified to have been received at least once, in the exact order specified.

**Verify Request Sequences Code Examples**

verify request sequence received

Java

```
new MockServerClient("localhost", 1080)
    .verify(
        request()
            .withPath("/some/path/one"),
        request()
            .withPath("/some/path/two"),
        request()
            .withPath("/some/path/three")
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080)
  .verifySequence(
    {
      'path': '/some/path/one'
    },
    {
      'path': '/some/path/two'
    },
    {
      'path': '/some/path/three'
    }
  )
  .then(
    function () {
      console.log("request sequence found in the order specified");
    },
    function (error) {
      console.log(error);
    }
  );
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/verify/put_verifySequence) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/verifySequence" -d '{
   "httpRequests":[
      {
         "path":"/some/path/one"
      },
      {
         "path":"/some/path/two"
      },
      {
         "path":"/some/path/three"
      }
   ]
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/verify/put_verifySequence) for full JSON specification

verify request sequence received using openapi

Java

```
new MockServerClient("localhost", 1080)
    .verify(
        request()
            .withPath("/status"),
        openAPI(
            "org/mockserver/openapi/openapi_petstore_example.json",
            "listPets"
        ),
        openAPI(
            "org/mockserver/openapi/openapi_petstore_example.json",
            "showPetById"
        )
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080)
    .verifySequence(
        {
            'path': '/status'
        },
        {
            'specUrlOrPayload': 'org/mockserver/openapi/openapi_petstore_example.json',
            'operationId': 'listPets'
        },
        {
            'specUrlOrPayload': 'org/mockserver/openapi/openapi_petstore_example.json',
            'operationId': 'showPetById'
        }
    )
    .then(
        function () {
            console.log("request sequence found in the order specified");
        },
        function (error) {
            console.log(error);
        }
    );
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/verify/put_verifySequence) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/verifySequence" -d '{
   "httpRequests":[
      {
         "path": "/status"
      },
      {
         "specUrlOrPayload": "org/mockserver/openapi/openapi_petstore_example.json",
         "operationId": "listPets"
      },
      {
         "specUrlOrPayload": "org/mockserver/openapi/openapi_petstore_example.json",
         "operationId": "showPetById"
      }
   ]
}'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/verify/put_verifySequence) for full JSON specification

verify request sequence received using expectation ids

Java

```
new MockServerClient("localhost", 1080)
    .verify(
        "31e4ca35-66c6-4645-afeb-6e66c4ca0559",
        "66c6ca35-ca35-66f5-8feb-5e6ac7ca0559",
        "ca3531e4-23c8-ff45-88f5-4ca0c7ca0559"
    );
```

JavaScript

```
var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080)
    .verifySequenceById(
        {
            'id': '31e4ca35-66c6-4645-afeb-6e66c4ca0559'
        },
        {
            'id': '66c6ca35-ca35-66f5-8feb-5e6ac7ca0559'
        },
        {
            'id': 'ca3531e4-23c8-ff45-88f5-4ca0c7ca0559'
        }
    )
    .then(
        function () {
            console.log("request sequence found in the order specified");
        },
        function (error) {
            console.log(error);
        }
    );
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/verify/put_verifySequence) for full JSON specification

REST API

```
curl -v -X PUT "http://localhost:1080/mockserver/verifySequence" -d '{
            "id": "31e4ca35-66c6-4645-afeb-6e66c4ca0559"
        },
        {
            "id": "66c6ca35-ca35-66f5-8feb-5e6ac7ca0559"
        },
        {
            "id": "ca3531e4-23c8-ff45-88f5-4ca0c7ca0559"
        }'
```

See [REST API](https://app.swaggerhub.com/apis/jamesdbloom/mock-server-openapi/5.14.x#/verify/put_verifySequence) for full JSON specification

© MockServer 2022
[James D Bloom](https://plus.google.com/110954472544793839756?rel=author)

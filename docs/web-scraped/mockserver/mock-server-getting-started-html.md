# Source: https://www.mock-server.com/mock_server/getting_started.html

Title: MockServer

URL Source: https://www.mock-server.com/mock_server/getting_started.html

Markdown Content:
MOCKSERVER
What is MockServer
Why use MockServer
Running MockServer
MockServer Clients
MockServer UI
Clearing & Resetting
Logging & Debugging
Scalability & Latency
HTTPS & TLS
API Security
CORS Support
Configuration
REST API Reference
Example Code
MOCKING
Getting Started
Creating Expectations
Using OpenAPI
Response Templates
Verifying Requests
Expectation Initializers
Persisting Expectations
Running Tests In Parallel
PROXYING
Getting Started
Configuring Clients
Record & Replay
Verifying Requests
Isolate Single Service
WHERE
Downloads
Community
Source Control
Backlog & Issues
npm
Maven
Docker
Helm & Kubernetes
Swagger Hub
Getting Started Mocking

The typical sequence for using MockServer is as follows:

Start MockServer
Setup Expectations
Run Your Test Scenarios
Verify Requests

For example code see the code examples folder in the git repository.

 
0. Start MockServer

MockServer is flexible and support numerous usage patterns.

MockServer can be run:
programmatically via a Java API in an @Before or @After method
using a JUnit 4 @Rule via a @Rule annotated field in a JUnit 4 test
using a JUnit 5 Test Extension via a @ExtendWith annotated JUnit 5 class
using a Spring Test Execution Listener via a @MockServerTest annotated test class
as a Docker container in any Docker enabled environment
via a Helm chart in any Kubernetes environment
from the command line as a stand-alone process in a test environment
via a Maven Plugin as part of a Maven build cycle
as a Node.js (npm) module from any Node.js code
as a Grunt plugin as part of a Grunt build cycle
as a deployable WAR to an existing application server

To simplify configuration all versions (except the deployable WAR) use a single port to support the control plane and data plane in HTTP, HTTPS or SOCKS.

MockServer is available in the following formats:
java dependency
Docker container
Helm chart for Kubernetes
executable jar
Homebrew package
maven plugin
npm plugin
Grunt plugin
deployable WAR that runs on JEE web servers

It is also possible to build and run MockServer directly from source code

MockServer UI:

MockServer has a UI that can be used to view the internal state within MockServer, including:

logs
active expectations
requests received
proxied requests
 
1. Setup Expectations
Java Code Example JavaScript Code Example

To use the Java client add the org.mock-server:mockserver-client-java-no-dependencies:5.14.0 dependency.

For more details about the different dependency versions see the page on Maven Central

for example in maven:

<dependency>
	<groupId>org.mock-server</groupId>
	<artifactId>mockserver-client-java-no-dependencies</artifactId>
	<version>RELEASE</version>
</dependency>

A request matcher expectation may contain:

request matcher - used to match which requests this expectation should be applied to
action - what action to take, actions include response, forward, callback and error
times (optional) - how many times the action should be taken
timeToLive (optional) - how long the expectation should stay active
priority (optional) - matching is ordered by priority (highest first) then creation (earliest first)
id (optional) - used for updating an existing expectation (i.e. when the id matches)

open api expectations are also supported using an OpenAPI v3 specifications to generate request matcher expectations for each operation, see the section on open api expectations for details.

 
Matching Order

MockServer will match (or play) active expectations in the exact order they are added (if their priority is identical). For example, if an expectation A is added with Times.exactly(3) then expectation B is added with Times.exactly(2) with the same request matcher they will be applied in the following order A, A, A, B, B. Priority can be used to alter the order that expectations are matched; matching is ordered by priority (highest first) then creation (earliest first).

Priority can be used to configure a default expectation or response by specifying a negative value for priority and a very lax request matcher; the lax request matcher ensures the default expectation is always matched, but the low priority ensure it is matched last after all other expectations.

 
Updating Expectations

If an expectation is added and the id field matches an existing expectation the existing expectation will be updated (i.e. replaced). A UUID will be used assigned to each expectation if no value for id is specified.

 
Request Matchers

The are two types of request matcher:

request properties matcher - that match requests using HTTP properties such as method, path or body
open api request matcher - that match requests using an OpenAPI definition
 

A request properties matcher matches requests using one or more of the following properties:

method - property matcher
path - property matcher
path parameters - key to multiple values matcher
query string parameters - key to multiple values matcher
headers - key to multiple values matcher
cookies - key to single value matcher
body - body matchers
secure - boolean value, true for HTTPS
 

Matching for properties can be done using:

string value
use for: method, path, path parameter keys, path parameters values, query parameter keys, query parameters values, header keys, header values, cookie keys, cookie values or bodies
examples: method, path, path parameters, query parameters, headers, cookies
regex value
use for: method, path, path parameter keys, path parameters values, query parameter keys, query parameters values, header keys, header values, cookie keys, cookie values or bodies
examples: method, path, path parameters, query parameters, headers
for syntax see Java regex syntax
json schema
use for: method, path, path parameters values, query parameters values, header values, cookie values or bodies
not supported for: path parameter keys, query parameter keys, header keys or cookie keys
examples: path parameters, query parameters, headers , cookies
for syntax see JSON Schema documentation
optional value
use for: method, path, path parameters values, query parameter keys, query parameters values, header keys, header values, cookie keys, cookie values or bodies
not supported for: path parameter keys or values, query parameter values, header values or cookie values
examples: query parameters, headers, cookies
negated value
use for: method, path, path parameter keys, path parameters values, query parameter keys, query parameters values, header keys, header values, cookie keys, cookie values or bodies
examples: method, path, headers
 

Matching for key to multiple values supports multiple values for each key for headers, query parameters and path parameters

Keys support all property matcher except json schema
Values support all property matcher except optional values
Matching supports two modes:
sub set (default) - matches if the request property contains a matching sub set (considering optional keys), therefore there is at least one matching value for each non-optional key or optional key if present
matching key - matches if the request property contains only matching values (considering optional keys), therefore all values must match for each non-optional key or optional key if present
 

Matching for key to single value supports a single value for each key for cookies

Keys support all property matcher except json schema
Values support all property matcher except optional values
 

Matching for bodies can be done using:

plain text (i.e. exact match)
regular expression - see Java regex syntax
JSON - supports:
matchType to control which fields get matched:
STRICT matches all fields, order of arrays and no additional fields allowed
ONLY_MATCHING_FIELDS only matches fields provided in the request matcher
JSONUnit placeholders to allow fields or values to be ignored or matched by type for example:
${json-unit.ignore-element} ignore a field
${json-unit.any-boolean} match a field as any boolean
see JSONUnit documentation for full details
JSON Schema - see JSON Schema documentation
JsonPath - matches if at least one value is returned by the expression, see JsonPath documentation
XML - supports:
XMLUnit placeholders to allow fields or elements to be ignored or matched by type for example:
${xmlunit.ignore} ignore an element
${xmlunit.isNumber} match an element or attribute as a number
see XMLUnit documentation for full details
XML Schema - see XML Schema documentation
XPath - matches if at least one value returned by expression, see XPath specification
form fields (i.e. body parameters)
binary
negated matcher
Request Properties Matcher Code Examples
 

An open api request matcher can contain any of the following fields:

specUrlOrPayload - mandatory value containing an OpenAPI v3 specifications in either JSON or YAML format as an:
HTTP/HTTPS URL
File URL
classpath location (without the classpath: scheme)
inline JSON object
inline escaped YAML string
operationId - optional value that specifies which operation to match against, if empty or null all operations are matched against

MockServer creates a set of request properties matchers for each open api request matcher, to ensures control-plane logic such as clearing expectations or retrieving expectations work consistently between the two types of request matchers, this can be viewed in the MockServer UI active expectations section.

OpenAPI Request Matcher Code Examples
 
Actions

Actions can be one of the following types:

response - returns a response defined by using
a literal
a javascript template
a velocity template
a class callback (must be present in classpath)
a method / closure callback (via WebSocket)
forward - forwards modified requests and returns modified response by using
the exact request and response received
an static overridden request and / or response
a dynamically modified request and / or response
a javascript template (request only)
a velocity template (request only)
a class callback for request and / or response (must be present in classpath)
a method / closure callback for request and / or response (via WebSocket)
error - returns an invalid response as a sequence of bytes or closes the connection

If no action is present for a request because no request matcher was matched then:

if MockServer is being used as a proxy the request is proxied to its destination un-modified
if the request host header does not match the hostname or IP the request automatically proxied to the host header
 

A response action can be:

either a response literal containing any of the following:

status code
reason phrase
body
headers
cookies
delay
connectionOptions that can be used to suppress headers, override headers or close the socket connection

or a templated response using javascript or velocity with a delay

or a callback used to dynamically generate a response based on the request:

as a server side callback implemented as a java class that has a default constructor, implements org.mockserver.mock.action.ExpectationResponseCallback and is available on the classpath

as a client side callback implemented as a closure using the java or javascript clients

Response Action Code Examples
 

A forward action can be:

either an exact forwarder, that forwards requests exactly as it receives them, containing the following:

host
port
scheme

or an overridden request (or overridden response), with a delay, that allows any part of a forwarded request or response to be replaced or certain fields (path, headers, cookies or query parameters) to be modified

or a templated forwarder using javascript or velocity, with a delay, that allows requests to be modified or completely re-written before they are forwarded

or a callback used to dynamically generate the request to forward based on the request received by MockServer:

as a server side callback implemented as a java class that has a default constructor, implements org.mockserver.mock.action.ExpectationForwardCallback or org.mockserver.mock.action.ExpectationForwardAndResponseCallback and is available on the classpath

as a client side callback implemented as a closure using the java or javascript clients

Forward Action Code Examples
 

An error action can return an invalid response as a sequence of bytes or drop the connection

Error Action Code Examples
 
3. Verify Requests

MockServer supports verification of requests is has received, including both proxied requests and requests that have matched an expectation.

Verification can be specified as follows:

a request matcher and a condition indicating the number of times the request should be matched
a sequence of request matchers that is matched in order
Verifying Repeating Requests

Verify that a request has been received by MockServer a specific number of times using a Verification

Verify Repeating Requests Code Examples
Verifying Request Sequences

Verify that a sequence of requests has been received by MockServer in the specified order using a VerificationSequence

The each request in the sequence will be verified to have been received at least once, in the exact order specified.

Verify Request Sequences Code Examples
© MockServer 2022
James D Bloom

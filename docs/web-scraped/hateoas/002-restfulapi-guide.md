# Source: https://restfulapi.net/hateoas/

How to Build HATEOAS Driven REST APIs
Skip to content
REST API Tutorial
Menu
Menu
REST
JSON
HATEOAS Driven REST APIs
HATEOAS (Hypermedia as the Engine of Application State) is a constraint of the REST application architecture which uses hypertext in API response.
Written by: Lokesh Gupta
Last Updated:
November 4, 2023
1. What is HATEOAS
HATEOAS (Hypermedia as the Engine of Application State)
is a constraint of the REST application architecture. HATEOAS keeps the REST style architecture unique from most other network application architectures.
The term “
hypermedia
” refers to any content that contains links to other forms of media such as images, movies, and text.
REST architectural style
lets us use the hypermedia links in the API response contents. It allows the client to dynamically navigate to the appropriate resources by traversing the hypermedia links.
Navigating hypermedia links is conceptually the same as browsing through web pages by clicking the relevant hyperlinks to achieve a final goal.
For example, the given below JSON response may be from an API like
HTTP GET http://api.domain.com/management/departments/10
{
"departmentId": 10,
"departmentName": "Administration",
"locationId": 1700,
"managerId": 200,
"links": [
{
"href": "10/employees",
"rel": "employees",
"type" : "GET"
}
]
}
In the preceding example, the response returned by the server contains hypermedia links to employee resources
10/employees
which can be traversed by the client to read employees belonging to the department.
The advantage of the above approach is that hypermedia links returned from the server drive the application&#8217;s state and not the other way around.
JSON does not have any universally accepted format for representing links between two resources. We may choose to send in the response body or decide to send links in HTTP response headers.
HTTP/1.1 200 OK
...
Link: &lt;10/employees&gt;; rel="employees"
Both are good solutions.
2. How to Implement HATEOAS
In the real world, when we visit a website &#8211; we hit its homepage. The homepage presents some snapshots and links to other sections of websites. We click on the links and get more information and related links relevant to the context.
Like a human’s interaction with a website, a
REST client hits an initial API URI and uses the server-provided links to access the resources it needs and discover available actions dynamically
.
The client need not have prior knowledge of the service or the different steps involved in a workflow. Additionally, the
clients no longer have to hardcode the URI structures for various resources
. HATEOAS allows the server to make URI changes as the API evolves without breaking the clients.
Above API interaction is possible using HATEOAS only.
Each REST framework provides its way of creating the HATEOAS links using framework capabilities. For example, in
Spring Boot HATEOAS tutorial
, links are part of resource model classes that are transferred as the resource state to the client.
3. HATEOAS References
The following are the two popular formats for specifying JSON REST API hypermedia links:
3.1. RFC 5988 (web linking)
RFC 5988
puts forward a framework for building links that define the relationships between resources on the web. Each link in RFC 5988 contains the following properties:
Target URI
: Each link should contain a target
Internationalized Resource Identifiers
(IRIs). This is represented by the
href
attribute.
Link relation type
: The link relation type describes how the current context (source) is related to the target resource. This is represented by the
rel
attribute.
Attributes for target IRI
: The attributes for a link included
hreflang
,
media
,
title
, and
type
, and any extension link parameters.
3.2. JSON Hypermedia API Language (HAL)
JSON HAL
is a promising proposal that sets the conventions for expressing hypermedia controls, such as links, with JSON or XML. It is in the draft stage at this time.
The two associated MIME types are
media type: application/hal+xml
media type: application/hal+json
Each link in HAL may contain the following properties:
Target URI
: It indicates the target resource URI. This is represented by the
href
attribute.
Link relation
: The link relation type describes how the current context is related to the target resource. This is represented by the
rel
attribute.
Type
: This indicates the expected resource media type. This is represented by the
type
attribute.
There is no right or wrong in choosing a hypermedia link format for our application. We should pick up a format that meets most of our use case requirements and stick to it.
Comments
Subscribe
Notify of
new follow-up comments
new replies to my comments
Label
{}
[+]
Name*
Email*
Website
Label
{}
[+]
Name*
Email*
Website
36
Comments
Most Voted
Newest
Oldest
Inline Feedbacks
View all comments
Load More Comments
Learn REST
What is REST?
REST Constraints
Naming REST Resources
Guides
Caching
Compression
Content Negotiation
HATEOAS
Idempotence
Security Essentials
Versioning
Statelessness
Pagination, Sorting and Filtering
Rate Limits
Best Practices
Tech &#8211; How To
Design REST APIs
Design API for Long-Running Tasks
REST APIs with JAX-RS
FAQs
PUT vs POST
N+1 Problem
&#8216;q&#8217; Parameter
Resources
What is an API?
SOAP vs REST
HTTP Methods
Richardson Maturity Model
HTTP Response Codes
200 (OK)
201 (Created)
202 (Accepted)
204 (No Content)
301 (Moved Permanently)
About Lokesh Gupta
A fun-loving family man, passionate about computers and problem-solving, with over 15 years of experience in Java and related technologies.
An avid Sci-Fi movie enthusiast and a fan of Christopher Nolan and Quentin Tarantino.
Follow on Twitter
Previous
Caching REST API Response
Next
REST Resource Representation Compression
References
The dissertation by Roy Thomas Fielding
Uniform Resource Identifier (URI, URL, URN) [RFC 3986]
Internet MediaTypes
Web Application Description Language (WADL)
Meta Links
About
Contact Us
Privacy Policy
Blogs
How To Do In Java
Copyright © 2023 •
Sitemap
Insert
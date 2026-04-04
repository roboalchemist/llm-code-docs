# Source: https://docs.spring.io/spring-hateoas/docs/current/reference/html/

Spring HATEOAS - Reference Documentation
Spring HATEOAS - Reference Documentation
Oliver Gierke
Greg Turnquist
Jay Bryant
version 1.2.1,
2020-11-10
Table of Contents
1. Preface
1.1. Migrating to Spring HATEOAS 1.0
1.1.1. The changes
Representation models
1.1.2. The migration script
1.1.3. Migrating from 1.0 M3 to 1.0 RC1
2. Fundamentals
2.1. Links
2.2. URI templates
2.3. Link relations
2.3.1. IANA link relations
2.4.  Representation models
2.4.1. Item resource representation model
2.4.2. Collection resource representation model
3. Server-side support
3.1.   Building links in Spring MVC
3.1.1. Building links that point to methods
3.2. Building links in Spring WebFlux
3.3. Affordances
3.3.1. Building affordances manually
3.4. Forwarded header handling
3.5.  Using the EntityLinks interface
3.5.1. EntityLinks based on Spring MVC controllers
3.5.2. EntityLinks API in detail
TypedEntityLinks
3.5.3. EntityLinks as SPI
3.6.  Representation model assembler
3.7. Representation Model Processors
3.8.  Using the
LinkRelationProvider
API
4. Media types
4.1. HAL – Hypertext Application Language
4.1.1. Building HAL representation models
4.1.2. Configuring link rendering
4.1.3. Link title internationalization
4.1.4.  Using the
CurieProvider
API
4.2. HAL-FORMS
4.2.1. Defining HAL-FORMS metadata
4.2.2. Internationalization of form attributes
Template titles
Property prompts
4.3. HTTP Problem Details
4.4. Collection+JSON
4.5. UBER - Uniform Basis for Exchanging Representations
4.6. ALPS - Application-Level Profile Semantics
4.7. Community-based media types
4.7.1. JSON:API
4.7.2. Siren
4.8. Registering a custom media type
4.8.1. Custom media type configuration
4.8.2. Recommendations
5. Configuration
5.1. Using
@EnableHypermediaSupport
5.1.1. Explicitly enabling support for dedicated web stacks
6. Client-side Support
6.1. Traverson
6.1.1.
EntityModel&lt;T&gt;
vs.
CollectionModel&lt;T&gt;
6.2. Using
LinkDiscoverer
Instances
6.3. Configuring WebClient instances
6.4. Configuring
WebTestClient
Instances
6.5. Configuring RestTemplate instances
This project provides some APIs to ease creating REST representations that follow the
HATEOAS
principle when working with Spring and especially Spring MVC. The core problem it tries to address is link creation and representation assembly.
&#169; 2012-2020 The original authors.
Copies of this document may be made for your own use and for distribution to others, provided that you do not charge any fee for such copies and further provided that each copy contains this Copyright Notice, whether distributed in print or electronically.
1. Preface
1.1. Migrating to Spring HATEOAS 1.0
For 1.0 we took the chance to re-evaluate some of the design and package structure choices we had made for the 0.x branch.
There had been an incredible amount of feedback on it and the major version bump seemed to be the most natural place to refactor those.
1.1.1. The changes
The biggest changes in package structure were driven by the introduction of a hypermedia type registration API to support additional media types in Spring HATEOAS.
This lead to the clear separation of client and server APIs (packages named respectively) as well as media type implementations in the package
mediatype
.
The easiest way to get your code base upgraded to the new API is by using the
migration script
.
Before we jump to that, here are the changes at a quick glance.
Representation models
The
ResourceSupport
/
Resource
/
Resources
/
PagedResources
group of classes never really felt appropriately named.
After all, these types do not actually manifest resources but rather representation models that can be enriched with hypermedia information and affordances.
Here&#8217;s how new names map to the old ones:
ResourceSupport
is now
RepresentationModel
Resource
is now
EntityModel
Resources
is now
CollectionModel
PagedResources
is now
PagedModel
Consequently,
ResourceAssembler
has been renamed to
RepresentationModelAssembler
and its methods
toResource(…)
and
toResources(…)
have been renamed to
toModel(…)
and
toCollectionModel(…)
respectively.
Also the name changes have been reflected in the classes contained in
TypeReferences
.
RepresentationModel.getLinks()
now exposes a
Links
instance (over a
List&lt;Link&gt;
) as that exposes additional API to concatenate and merge different
Links
instances using various strategies.
Also it has been turned into a self-bound generic type to allow the methods that add links to the instance return the instance itself.
The
LinkDiscoverer
API has been moved to the
client
package.
The
LinkBuilder
and
EntityLinks
APIs have been moved to the
server
package.
ControllerLinkBuilder
has been moved into
server.mvc
and deprecated to be replaced by
WebMvcLinkBuilder
.
RelProvider
has been renamed to
LinkRelationProvider
and returns
LinkRelation
instances instead of
String
s.
VndError
has been moved to the
mediatype.vnderror
package.
1.1.2. The migration script
You can find
a script
to run from your application root that will update all import statements and static method references to Spring HATEOAS types that moved in our source code repository.
Simply download that, run it from your project root.
By default it will inspect all Java source files and replace the legacy Spring HATEOAS type references with the new ones.
Example 1. Sample application of the migration script
$ ./migrate-to-1.0.sh
Migrating Spring HATEOAS references to 1.0 for files : *.java
Adapting ./src/main/java/…
…
Done!
Note that the script will not necessarily be able to entirely fix all changes, but it should cover the most important refactorings.
Now verify the changes made to the files in your favorite Git client and commit as appropriate.
In case you find method or type references unmigrated, please open a ticket in out issue tracker.
1.1.3. Migrating from 1.0 M3 to 1.0 RC1
Link.andAffordance(…)
taking Affordance details have been moved to
Affordances
. To manually build up
Affordance
instances now use
Affordances.of(link).afford(…)
. Also note the new
AffordanceBuilder
type exposed from
Affordances
for fluent usage. See
Affordances
for details.
AffordanceModelFactory.getAffordanceModel(…)
now receives
InputPayloadMetadata
and
PayloadMetadata
instances instead of
ResolvableType
s to allow non-type-based implementations. Custom media type implementations have to be adapted to that accordingly.
HAL Forms now does not render property attributes if their value adheres to what&#8217;s defined as default in the spec. I.e. if previously
required
was explicitly set to
false
, we now just omit the entry for
required
.
We also now only force them to be non-required for templates that use
PATCH
as the HTTP method.
2. Fundamentals
This section covers the basics of Spring HATEOAS and its fundamental domain abstractions.
2.1. Links
The fundamental idea of hypermedia is to enrich the representation of a resource with hypermedia elements.
The simplest form of that are links.
They indicate a client that it can navigate to a certain resource.
The semantics of a related resource are defined in a so-called link relation.
You might have seen this in the header of an HTML file already:
Example 2. A link in an HTML document
&lt;link href="theme.css" rel="stylesheet" type="text/css" /&gt;
As you can see the link points to a resource
theme.css
and indicates that it is a style sheet.
Links often carry additional information, like the media type that the resource pointed to will return.
However, the fundamental building blocks of a link are its reference and relation.
Spring HATEOAS lets you work with links through its immutable
Link
value type.
Its constructor takes both a hypertext reference and a link relation, the latter being defaulted to the IANA link relation
self
.
Read more on the latter in
Link relations
.
Example 3. Using links
Link link = Link.of("/something");
assertThat(link.getHref()).isEqualTo("/something");
assertThat(link.getRel()).isEqualTo(IanaLinkRelations.SELF);
link = Link.of("/something", "my-rel");
assertThat(link.getHref()).isEqualTo("/something");
assertThat(link.getRel()).isEqualTo(LinkRelation.of("my-rel"));
Link
exposes other attributes as defined in
RFC-8288
.
You can set them by calling the corresponding wither method on a
Link
instance.
Find more information on how to create links pointing to Spring MVC and Spring WebFlux controllers in
Building links in Spring MVC
and
Building links in Spring WebFlux
.
2.2. URI templates
For a Spring HATEOAS
Link
, the hypertext reference can not only be a URI, but also a URI template according to
RFC-6570
.
A URI template contains so-called template variables and allows expansion of these parameters.
This allows clients to turn parameterized templates into URIs without having to know about the structure of the final URI, it only needs to know about the names of the variables.
Example 4. Using links with templated URIs
Link link = Link.of("/{segment}/something{?parameter}");
assertThat(link.isTemplated()).isTrue();
(1)
assertThat(link.getVariableNames()).contains("segment", "parameter");
(2)
Map&lt;String, Object&gt; values = new HashMap&lt;&gt;();
values.put("segment", "path");
values.put("parameter", 42);
assertThat(link.expand(values).getHref())
(3)
.isEqualTo("/path/something?parameter=42");
1
The
Link
instance indicates that is templated, i.e. it contains a URI template.
2
It exposes the parameters contained in the template.
3
It allows expansion of the parameters.
URI templates can be constructed manually and template variables added later on.
Example 5. Working with URI templates
UriTemplate template = UriTemplate.of("/{segment}/something")
.with(new TemplateVariable("parameter", VariableType.REQUEST_PARAM);
assertThat(template.toString()).isEqualTo("/{segment}/something{?parameter}");
2.3. Link relations
To indicate the relationship of the target resource to the current one so-called link relations are used.
Spring HATEOAS provides a
LinkRelation
type to easily create
String
-based instances of it.
2.3.1. IANA link relations
The Internet Assigned Numbers Authority contains a set of
predefined link relations
.
They can be referred to via
IanaLinkRelations
.
Example 6. Using IANA link relations
Link link = Link.of("/some-resource"), IanaLinkRelations.NEXT);
assertThat(link.getRel()).isEqualTo(LinkRelation.of("next"));
assertThat(IanaLinkRelation.isIanaRel(link.getRel())).isTrue();
2.4.
Representation models
To easily create hypermedia enriched representations, Spring HATEOAS provides a set of classes with
RepresentationModel
at their root.
It&#8217;s basically a container for a collection of
Link
s and has convenient methods to add those to the model.
The models can later be rendered into various media type formats that will define how the hypermedia elements look in the representation.
For more information on this, have a look at
Media types
.
Example 7. The
RepresentationModel
class hierarchy
The default way to work with a
RepresentationModel
is to create a subclass of it to contain all the properties the representation is supposed to contain, create instances of that class, populate the properties and enrich it with links.
Example 8. A sample representation model type
class PersonModel extends RepresentationModel&lt;PersonModel&gt; {
String firstname, lastname;
}
The generic self-typing is necessary to let
RepresentationModel.add(…)
return instances of itself.
The model type can now be used like this:
Example 9. Using the person representation model
PersonModel model = new PersonModel();
model.firstname = "Dave";
model.lastname = "Matthews";
model.add(Link.of("https://myhost/people/42"));
If you returned such an instance from a Spring MVC or WebFlux controller and the client sent an
Accept
header set to
application/hal+json
, the response would look as follows:
Example 10. The HAL representation generated for the person representation model
{
"_links" : {
"self" : {
"href" : "https://myhost/people/42"
}
},
"firstname" : "Dave",
"lastname" : "Matthews"
}
2.4.1. Item resource representation model
For a resource that&#8217;s backed by a singular object or concept, a convenience
EntityModel
type exists.
Instead of creating a custom model type for each concept, you can just reuse an already existing type and wrap instances of it into the
EntityModel
.
Example 11. Using
EntityModel
to wrap existing objects
Person person = new Person("Dave", "Matthews");
EntityModel&lt;Person&gt; model = EntityModel.of(person);
2.4.2. Collection resource representation model
For resources that are conceptually collections, a
CollectionModel
is available.
Its elements can either be simple objects or
RepresentationModel
instances in turn.
Example 12. Using
CollectionModel
to wrap a collection of existing objects
Collection&lt;Person&gt; people = Collections.singleton(new Person("Dave", "Matthews"));
CollectionModel&lt;Person&gt; model = CollectionModel.of(people);
3. Server-side support
3.1.
Building links in Spring MVC
Now we have the domain vocabulary in place, but the main challenge remains: how to create the actual URIs to be wrapped into
Link
instances in a less fragile way. Right now, we would have to duplicate URI strings all over the place. Doing so is brittle and unmaintainable.
Assume you have your Spring MVC controllers implemented as follows:
@Controller
class PersonController {
@GetMapping("/people")
HttpEntity&lt;PersonModel&gt; showAll() { … }
@GetMapping(value = "/{person}", method = RequestMethod.GET)
HttpEntity&lt;PersonModel&gt; show(@PathVariable Long person) { … }
}
We see two conventions here. The first is a collection resource that is exposed through
@GetMapping
annotation of the controller method, with individual elements of that collection exposed as direct sub resources. The collection resource might be exposed at a simple URI (as just shown) or more complex ones (such as
/people/{id}/addresses
). Suppose you would like to link to the collection resource of all people. Following the approach from above would cause two problems:
To create an absolute URI, you would need to look up the protocol, hostname, port, servlet base, and other values. This is cumbersome and requires ugly manual string concatenation code.
You probably do not want to concatenate the
/people
on top of your base URI, because you would then have to maintain the information in multiple places. If you change the mapping, you then have to change all the clients pointing to it.
Spring HATEOAS now provides a
WebMvcLinkBuilder
that lets you create links by pointing to controller classes.
The following example shows how to do so:
import static org.sfw.hateoas.server.mvc.WebMvcLinkBuilder.*;
Link link = linkTo(PersonController.class).withRel("people");
assertThat(link.getRel()).isEqualTo(LinkRelation.of("people"));
assertThat(link.getHref()).endsWith("/people");
The
WebMvcLinkBuilder
uses Spring&#8217;s
ServletUriComponentsBuilder
under the hood to obtain the basic URI information from the current request. Assuming your application runs at
localhost:8080/your-app
, this is exactly the URI on top of which you are constructing additional parts. The builder now inspects the given controller class for its root mapping and thus ends up with
localhost:8080/your-app/people
. You can also build more nested links as well.
The following example shows how to do so:
Person person = new Person(1L, "Dave", "Matthews");
//                 /person                 /     1
Link link = linkTo(PersonController.class).slash(person.getId()).withSelfRel();
assertThat(link.getRel(), is(IanaLinkRelation.SELF.value()));
assertThat(link.getHref(), endsWith("/people/1"));
The builder also allows creating URI instances to build up (for example, response header values):
HttpHeaders headers = new HttpHeaders();
headers.setLocation(linkTo(PersonController.class).slash(person).toUri());
return new ResponseEntity&lt;PersonModel&gt;(headers, HttpStatus.CREATED);
3.1.1. Building links that point to methods
You can even build links that point to methods or create dummy controller method invocations.
The first approach is to hand a
Method
instance to the
WebMvcLinkBuilder
.
The following example shows how to do so:
Method method = PersonController.class.getMethod("show", Long.class);
Link link = linkTo(method, 2L).withSelfRel();
assertThat(link.getHref()).endsWith("/people/2"));
This is still a bit dissatisfying, as we have to first get a
Method
instance, which throws an exception and is generally quite cumbersome. At least we do not repeat the mapping. An even better approach is to have a dummy method invocation of the target method on a controller proxy, which we can create by using the
methodOn(…)
helper.
The following example shows how to do so:
Link link = linkTo(methodOn(PersonController.class).show(2L)).withSelfRel();
assertThat(link.getHref()).endsWith("/people/2");
methodOn(…)
creates a proxy of the controller class that records the method invocation and exposes it in a proxy created for the return type of the method. This allows the fluent expression of the method for which we want to obtain the mapping. However, there are a few constraints on the methods that can be obtained by using this technique:
The return type has to be capable of proxying, as we need to expose the method invocation on it.
The parameters handed into the methods are generally neglected (except the ones referred to through
@PathVariable
, because they make up the URI).
3.2. Building links in Spring WebFlux
TODO
3.3. Affordances
The affordances of the environment are what it offers …​ what it provides or furnishes, either for good or ill. The verb 'to afford' is found in the dictionary, but the noun 'affordance' is not. I have made it up.
&#8212; James J. Gibson
The Ecological Approach to Visual Perception (page 126)
REST-based resources provide not just data but controls.
The last ingredient to form a flexible service are detailed
affordances
on how to use the various controls.
Because affordances are associated with links, Spring HATEOAS provides an API to attach as many related methods as needed to a link.
Just as you can create links by pointing to Spring MVC controller methods (see
Building links in Spring MVC
for details) you &#8230;&#8203;
The following code shows how to take a
self
link and associate two more affordances:
Example 13. Connecting affordances to
GET /employees/{id}
@GetMapping("/employees/{id}")
public EntityModel&lt;Employee&gt; findOne(@PathVariable Integer id) {
Class&lt;EmployeeController&gt; controllerClass = EmployeeController.class;
// Start the affordance with the "self" link, i.e. this method.
Link findOneLink = linkTo(methodOn(controllerClass).findOne(id)).withSelfRel();
(1)
// Return the affordance + a link back to the entire collection resource.
return EntityModel.of(EMPLOYEES.get(id), //
findOneLink //
.andAffordance(afford(methodOn(controllerClass).updateEmployee(null, id)))
(2)
.andAffordance(afford(methodOn(controllerClass).partiallyUpdateEmployee(null, id))));
(3)
}
1
Create the
self
link.
2
Associate the
updateEmployee
method with the
self
link.
3
Associate the
partiallyUpdateEmployee
method with the
self
link.
Using
.andAffordance(afford(&#8230;&#8203;))
, you can use the controller&#8217;s methods to connect a
PUT
and a
PATCH
operation to a
GET
operation.
Imagine that the related methods
afforded
above look like this:
Example 14.
updateEmpoyee
method that responds to
PUT /employees/{id}
@PutMapping("/employees/{id}")
public ResponseEntity&lt;?&gt; updateEmployee( //
@RequestBody EntityModel&lt;Employee&gt; employee, @PathVariable Integer id)
Example 15.
partiallyUpdateEmployee
method that responds to
PATCH /employees/{id}
@PatchMapping("/employees/{id}")
public ResponseEntity&lt;?&gt; partiallyUpdateEmployee( //
@RequestBody EntityModel&lt;Employee&gt; employee, @PathVariable Integer id)
Pointing to those methods using the
afford(…)
methods will cause Spring HATEOAS to analyze the request body and response types and capture metadata to allow different media type implementations to use that information to translate that into descriptions of the input and outputs.
3.3.1. Building affordances manually
While the primary way to register affordances for a link, it might be necessary to build some of them manually.
This can be achieved by using the
Affordances
API:
Example 16. Using the
Affordances
API to manually register affordances
var methodInvocation = methodOn(EmployeeController.class).all();
var link = Affordances.of(linkTo(methodInvocation).withSelfRel())
(1)
.afford(HttpMethod.POST)
(2)
.withInputAndOutput(Employee.class) //
.withName("createEmployee") //
.andAfford(HttpMethod.GET)
(3)
.withOutput(Employee.class) //
.addParameters(//
QueryParameter.optional("name"), //
QueryParameter.optional("role")) //
.withName("search") //
.toLink();
1
You start by creating an instance of
Affordances
from a
Link
instance creating the context for describing the affordances.
2
Each affordance starts with the HTTP method it&#8217;s supposed to support. We then register a type as payload description and name the affordance explicitly. The latter can be omitted and a default name will be derived from the HTTP method and input type name. This effectively creates the same affordance as the pointer to
EmployeeController.newEmployee(…)
created.
3
The next affordance is built to reflect what&#8217;s happening for the pointer to
EmployeeController.search(…)
. Here we define
Employee
to be the model for the response created and explicitly register
QueryParameter
s.
Affordances are backed by media type specific affordance models that translate the general affordance metadata into specific representations.
Please make sure to check the section on affordances in the
Media types
section to find more details about how to control the exposure of that metadata.
3.4. Forwarded header handling
RFC-7239 forwarding headers
are most commonly used when your application is behind a proxy, behind a load balancer, or in the cloud.
The node that actually receives the web request is part of the infrastructure, and
forwards
the request to your application.
Your application may be running on
localhost:8080
, but to the outside world you&#8217;re expected to be at
reallycoolsite.com
(and on the web&#8217;s standard port 80).
By having the proxy include extra headers (which many already do), Spring HATEOAS can generate links properly as it uses Spring Framework functionality to obtain the base URI of the original request.
Anything that can change the root URI based on external inputs must be properly guarded.
That&#8217;s why, by default, forwarded header handling is
disabled
.
You MUST enable it to be operational.
If you are deploying to the cloud or into a configuration where you control the proxies and load balancers, then you&#8217;ll certainly want to use this feature.
To enable forwarded header handling you need to register Spring&#8217;s
ForwardedHeaderFilter
for Spring MVC (details
here
) or
ForwardedHeaderTransformer
for Spring WebFlux (details
here
) in your application.
In a Spring Boot application those components can be simply declared as Spring beans as described
here
.
Example 17. Registering a
ForwardedHeaderFilter
@Bean
ForwardedHeaderFilter forwardedHeaderFilter() {
return new ForwardedHeaderFilter();
}
This will create a servlet filter that processes all the
X-Forwarded-…
headers.
And it will register it properly with the servlet handlers.
For a Spring WebFlux application, the reactive counterpart is
ForwardedHeaderTransformer
:
Example 18. Registering a
ForwardedHeaderTransformer
@Bean
ForwardedHeaderTransformer forwardedHeaderTransformer() {
return new ForwardedHeaderTransformer();
}
This will create a function that transforms reactive web requests, processing
X-Forwarded-…
headers.
And it will register it properly with WebFlux.
With configuration as shown above in place, a request passing
X-Forwarded-…
headers will see those reflected in the links generated:
Example 19. A request using
X-Forwarded-…
headers
curl -v localhost:8080/employees \
-H 'X-Forwarded-Proto: https' \
-H 'X-Forwarded-Host: example.com' \
-H 'X-Forwarded-Port: 9001'
Example 20. The corresponding response with the links generated to consider those headers
{
"_embedded": {
"employees": [
{
"id": 1,
"name": "Bilbo Baggins",
"role": "burglar",
"_links": {
"self": {
"href": "https://example.com:9001/employees/1"
},
"employees": {
"href": "https://example.com:9001/employees"
}
}
}
]
},
"_links": {
"self": {
"href": "https://example.com:9001/employees"
},
"root": {
"href": "https://example.com:9001"
}
}
}
3.5.
Using the EntityLinks interface
EntityLinks
and its various implementations are NOT currently provided out-of-the-box for Spring WebFlux applications.
The contract defined in the
EntityLinks
SPI was originally aimed at Spring Web MVC and doesn&#8217;t consider Reactor types.
Developing a comparable contract that supports reactive programming is still in progress.
So far, we have created links by pointing to the web framework implementations (that is, the Spring MVC controllers) and inspected the mapping.
In many cases, these classes essentially read and write representations backed by a model class.
The
EntityLinks
interface now exposes an API to look up a
Link
or
LinkBuilder
based on the model types.
The methods essentially return links that point either to the collection resource (such as
/people
) or to an item resource (such as
/people/1
).
The following example shows how to use
EntityLinks
:
EntityLinks links = …;
LinkBuilder builder = links.linkFor(Customer.class);
Link link = links.linkToItemResource(Customer.class, 1L);
EntityLinks
is available via dependency injection by activating
@EnableHypermediaSupport
in your Spring MVC configuration.
This will cause a variety of default implementations of
EntityLinks
being registered.
The most fundamental one is
ControllerEntityLinks
that inspects SpringMVC controller classes.
If you want to register your own implementation of
EntityLinks
, check out
this section
.
3.5.1. EntityLinks based on Spring MVC controllers
Activating entity links functionality causes all the Spring MVC controllers available in the current
ApplicationContext
to be inspected for the
@ExposesResourceFor(…)
annotation.
The annotation exposes which model type the controller manages.
Beyond that, we assume that you adhere to the following URI mapping setup and conventions:
A type level
@ExposesResourceFor(…)
declaring which entity type the controller exposes collection and item resources for.
A class level base mapping that represents the collection resource.
An additional method level mapping that extends the mapping to append an identifier as additional path segment.
The following example shows an implementation of an
EntityLinks
-capable controller:
@Controller
@ExposesResourceFor(Order.class)
(1)
@RequestMapping("/orders")
(2)
class OrderController {
@GetMapping
(3)
ResponseEntity orders(…) { … }
@GetMapping("{id}")
(4)
ResponseEntity order(@PathVariable("id") … ) { … }
}
1
The controller indicates it&#8217;s exposing collection and item resources for the entity
Order
.
2
Its collection resource is exposed under
/orders
3
That collection resource can handle
GET
requests. Add more methods for other HTTP methods at your convenience.
4
An additional controller method to handle a subordinate resource taking a path variable to expose an item resource, i.e. a single
Order
.
With this in place, when you enable
EntityLinks
@EnableHypermediaSupport
in your Spring MVC configuration, you can create links to the controller as follows:
@Controller
class PaymentController {
private final EntityLinks entityLinks;
PaymentController(EntityLinks entityLinks) {
(1)
this.entityLinks = entityLinks;
}
@PutMapping(…)
ResponseEntity payment(@PathVariable Long orderId) {
Link link = entityLinks.linkToItemResource(Order.class, orderId);
(2)
…
}
}
1
Inject
EntityLinks
made available by
@EnableHypermediaSupport
in your configuration.
2
Use the APIs to build links by using the entity types instead of controller classes.
As you can see, you can refer to resources managing
Order
instances without referring to
OrderController
explicitly.
3.5.2. EntityLinks API in detail
Fundamentally,
EntityLinks
allows to build
LinkBuilder
s and
Link
instances to collection and item resources of an entity type.
Methods starting with
linkFor…
will produce
LinkBuilder
instances for you to extend and augment with additional path segments, parameters, etc.
Methods starting with
linkTo
produce fully prepared
Link
instances.
While for collection resources providing an entity type is sufficient, links to item resources will need an identifier provided.
This usually looks like this:
Example 21. Obtaining a link to an item resource
entityLinks.linkToItemResource(order, order.getId());
If you find yourself repeating those method calls the identifier extraction step can be pulled out into a reusable
Function
to be reused throughout different invocations:
Function&lt;Order, Object&gt; idExtractor = Order::getId;
(1)
entityLinks.linkToItemResource(order, idExtractor);
(2)
1
The identifier extraction is externalized so that it can be held in a field or constant.
2
The link lookup using the extractor.
TypedEntityLinks
As controller implementations are often grouped around entity types, you&#8217;ll very often find yourself using the same extractor function (see
EntityLinks API in detail
for details) all over the controller class.
We can centralize the identifier extraction logic even more by obtaining a
TypedEntityLinks
instance providing the extractor once, so that the actual lookups don&#8217;t have to deal with the extraction anymore at all.
Example 22. Using TypedEntityLinks
class OrderController {
private final TypedEntityLinks&lt;Order&gt; links;
OrderController(EntityLinks entityLinks) {
(1)
this.links = entityLinks.forType(Order::getId);
(2)
}
@GetMapping
ResponseEntity&lt;Order&gt; someMethod(…) {
Order order = … // lookup order
Link link = links.linkToItemResource(order);
(3)
}
}
1
Inject an
EntityLinks
instance.
2
Indicate you&#8217;re going to look up
Order
instances with a certain identifier extractor function.
3
Look up item resource links based on a sole
Order
instance.
3.5.3. EntityLinks as SPI
The
EntityLinks
instance created by
@EnableHypermediaSupport
is of type
DelegatingEntityLinks
which will in turn pick up all other
EntityLinks
implementations available as beans in the
ApplicationContext
.
It&#8217;s registered as primary bean so that it&#8217;s always the sole injection candidate when you inject
EntityLinks
in general.
ControllerEntityLinks
is the default implementation that will be included in the setup, but users are free to implement and register their own implementations.
Making those available to the
EntityLinks
instance available for injection is a matter of registering your implementation as Spring bean.
Example 23. Declaring a custom EntityLinks implementation
@Configuration
class CustomEntityLinksConfiguration {
@Bean
MyEntityLinks myEntityLinks(…) {
return new MyEntityLinks(…);
}
}
An example for the extensibility of this mechanism is Spring Data REST&#8217;s
RepositoryEntityLinks
, which uses the repository mapping information to create links pointing to resources backed by Spring Data repositories.
At the same time, it even exposes additional lookup methods for other types of resources.
If you want to make use of these, simply inject
RepositoryEntityLinks
explicitly.
3.6.
Representation model assembler
As the mapping from an entity to a representation model must be used in multiple places, it makes sense to create a dedicated class responsible for doing so. The conversion contains very custom steps but also a few boilerplate steps:
Instantiation of the model class
Adding a link with a
rel
of
self
pointing to the resource that gets rendered.
Spring HATEOAS now provides a
RepresentationModelAssemblerSupport
base class that helps reduce the amount of code you need to write.
The following example shows how to use it:
class PersonModelAssembler extends RepresentationModelAssemblerSupport&lt;Person, PersonModel&gt; {
public PersonModelAssembler() {
super(PersonController.class, PersonModel.class);
}
@Override
public PersonModel toModel(Person person) {
PersonModel resource = createResource(person);
// … do further mapping
return resource;
}
}
createResource(&#8230;&#8203;)
is code you write to instantiate a
PersonModel
object given a
Person
object. It should only focus on setting attributes, not populating
Links
.
Setting the class up as we did in the preceding example gives you the following benefits:
There are a handful of
createModelWithId(…)
methods that let you create an instance of the resource and have a
Link
with a rel of
self
added to it. The href of that link is determined by the configured controller&#8217;s request mapping plus the ID of the entity (for example,
/people/1
).
The resource type gets instantiated by reflection and expects a no-arg constructor. If you want to use a dedicated constructor or avoid the reflection performance overhead, you can override
instantiateModel(…)
.
You can then use the assembler to either assemble a
RepresentationModel
or a
CollectionModel
.
The following example creates a
CollectionModel
of
PersonModel
instances:
Person person = new Person(…);
Iterable&lt;Person&gt; people = Collections.singletonList(person);
PersonModelAssembler assembler = new PersonModelAssembler();
PersonModel model = assembler.toModel(person);
CollectionModel&lt;PersonModel&gt; model = assembler.toCollectionModel(people);
3.7. Representation Model Processors
Sometimes you need to tweak and adjust hypermedia representations after they have been
assembled
.
A perfect example is when you have a controller that deals with order fulfillment, but you need to add links related to making payments.
Imagine having your ordering system producing this type of hypermedia:
{
"orderId" : "42",
"state" : "AWAITING_PAYMENT",
"_links" : {
"self" : {
"href" : "http://localhost/orders/999"
}
}
}
You wish to add a link so the client can make payment, but don&#8217;t want to mix details about your
PaymentController
into
the
OrderController
.
Instead of polluting the details of your ordering system, you can write a
RepresentationModelProcessor
like this:
public class PaymentProcessor implements RepresentationModelProcessor&lt;EntityModel&lt;Order&gt;&gt; {
(1)
@Override
public EntityModel&lt;Order&gt; process(EntityModel&lt;Order&gt; model) {
model.add(
(2)
Link.of("/payments/{orderId}").withRel(LinkRelation.of("payments")) //
.expand(model.getContent().getOrderId()));
return model;
(3)
}
}
1
This processor will only be applied to
EntityModel&lt;Order&gt;
objects.
2
Manipulate the existing
EntityModel
object by adding an unconditional link.
3
Return the
EntityModel
so it can be serialized into the requested media type.
Register the processor with your application:
@Configuration
public class PaymentProcessingApp {
@Bean
PaymentProcessor paymentProcessor() {
return new PaymentProcessor();
}
}
Now when you issue a hypermedia respresentation of an
Order
, the client receives this:
{
"orderId" : "42",
"state" : "AWAITING_PAYMENT",
"_links" : {
"self" : {
"href" : "http://localhost/orders/999"
},
"payments" : {
(1)
"href" : "/payments/42"
(2)
}
}
}
1
You see the
LinkRelation.of("payments")
plugged in as this link&#8217;s relation.
2
The URI was provided by the processor.
This example is quite simple, but you can easily:
Use
WebMvcLinkBuilder
or
WebFluxLinkBuilder
to construct a dynamic link to your
PaymentController
.
Inject any services needed to conditionally add other links (e.g.
cancel
,
amend
) that are driven by state.
Leverage cross cutting services like Spring Security to add, remove, or revise links based upon the current user&#8217;s context.
Also, in this example, the
PaymentProcessor
alters the provided
EntityModel&lt;Order&gt;
. You also have the power to
replace
it with another object. Just be advised the API requires the return type to equal the input type.
3.8.
Using the
LinkRelationProvider
API
When building links, you usually need to determine the relation type to be used for the link. In most cases, the relation type is directly associated with a (domain) type. We encapsulate the detailed algorithm to look up the relation types behind a
LinkRelationProvider
API that lets you determine the relation types for single and collection resources. The algorithm for looking up the relation type follows:
If the type is annotated with
@Relation
, we use the values configured in the annotation.
If not, we default to the uncapitalized simple class name plus an appended
List
for the collection
rel
.
If the
EVO inflector
JAR is in the classpath, we use the plural of the single resource
rel
provided by the pluralizing algorithm.
@Controller
classes annotated with
@ExposesResourceFor
(see
Using the EntityLinks interface
for details) transparently look up the relation types for the type configured in the annotation, so that you can use
LinkRelationProvider.getItemResourceRelFor(MyController.class)
and get the relation type of the domain type exposed.
A
LinkRelationProvider
is automatically exposed as a Spring bean when you use
@EnableHypermediaSupport
. You can plug in custom providers by implementing the interface and exposing them as Spring beans in turn.
4. Media types
4.1. HAL – Hypertext Application Language
JSON Hypertext Application Language
or HAL is one of the simplest
and most widely adopted hypermedia media types adopted when not discussing specific web stacks.
It was the first spec-based media type adopted by Spring HATEOAS.
4.1.1. Building HAL representation models
As of Spring HATEOAS 1.1, we ship a dedicated
HalModelBuilder
that allows to create
RepresentationModel
instances through a HAL-idiomatic API.
These are its fundamental assumptions:
A HAL representation can be backed by an arbitrary object (an entity) that builds up the domain fields contained in the representation.
The representation can be enriched by a variety of embedded documents, which can be either arbitrary objects or HAL representations themselves (i.e. containing nested embeddeds and links).
Certain HAL specific patterns (e.g. previews) can be directly used in the API so that the code setting up the representation reads like you&#8217;d describe a HAL representation following those idioms.
Here&#8217;s an example of the API used:
// An order
var order = new Order(…);
(1)
// The customer who placed the order
var customer = customer.findById(order.getCustomerId());
var customerLink = Link.of("/orders/{id}/customer")
(2)
.expand(order.getId())
.withRel("customer");
var additional = …
var model = HalModelBuilder.halModel(order)
.preview(new CustomerSummary(customer))
(3)
.forLink(customerLink)
(4)
.embed(additional)
(5)
.link(Link.of(…, IanaLinkRelations.SELF));
.build();
1
We set up some domain type. In this case, an order that has a relationship to the customer that placed it.
2
We prepare a link pointing to a resource that will expose customer details
3
We start building a preview by providing the payload that&#8217;s supposed to be rendered inside the
_embeddable
clause.
4
We conclude that preview by providing the target link. It transparently gets added to the
_links
object and its link relation is used as the key for the object provided in the previous step.
5
Other objects can be added to show up under
_embedded
.
The key under which they&#8217;re listed is derived from the objects relation settings. They&#8217;re customizable via
@Relation
or a dedicated
LinkRelationProvider
(see
Using the
LinkRelationProvider
API
for details).
{
"_links" : {
"self" : { "href" : "…" },
(1)
"customer" : { "href" : "/orders/4711/customer" }
(2)
},
"_embedded" : {
"customer" : { … },
(3)
"additional" : { … }
(4)
}
}
1
The
self
link as explicitly provided.
2
The
customer
link transparently added through
….preview(…).forLink(…)
.
3
The preview object provided.
4
Additional elements added via explicit
….embed(…)
.
In HAL
_embedded
is also used to represent top collections.
They&#8217;re usually grouped under the link relation derived from the object&#8217;s type.
I.e. a list of orders would look like this in HAL:
{
"_embedded" : {
"orders : [
…
(1)
]
}
}
1
Individual order documents go here.
Creating such a representation is as easy as this:
Collection&lt;Order&gt; orders = …;
HalModelBuilder.emptyHalDocument()
.embed(orders);
That said, if the order is empty, there&#8217;s no way to derive the link relation to appear inside
_embedded
, so that the document will stay empty if the collection is empty.
If you prefer to explicitly communicate an empty collection, a type can be handed into the overload of the
….embed(…)
method taking a
Collection
.
If the collection handed into the method is empty, this will cause a field rendered with its link relation derived from the given type.
HalModelBuilder.emptyHalModel()
.embed(Collections.emptyList(), Order.class);
// or
.embed(Collections.emptyList(), LinkRelation.of("orders"));
will create the following, more explicit representation.
{
"_embedded" : {
"orders" : []
}
}
4.1.2. Configuring link rendering
In HAL, the
_links
entry is a JSON object. The property names are
link relations
and
each value is either
a link object or an array of link objects
.
For a given link relation that has two or more links, the spec is clear on representation:
Example 24. HAL document with two links associated with one relation
{
"_links": {
"item": [
{ "href": "https://myhost/cart/42" },
{ "href": "https://myhost/inventory/12" }
]
},
"customer": "Dave Matthews"
}
But if there is only one link for a given relation, the spec is ambiguous. You could render that as either a single object
or as a single-item array.
By default, Spring HATEOAS uses the most terse approach and renders a single-link relation like this:
Example 25. HAL document with single link rendered as an object
{
"_links": {
"item": { "href": "https://myhost/inventory/12" }
},
"customer": "Dave Matthews"
}
Some users prefer to not switch between arrays and objects when consuming HAL. They would prefer this type of rendering:
Example 26. HAL with single link rendered as an array
{
"_links": {
"item": [{ "href": "https://myhost/inventory/12" }]
},
"customer": "Dave Matthews"
}
If you wish to customize this policy, all you have to do is inject a
HalConfiguration
bean into your application configuration.
There are multiple choices.
Example 27. Global HAL single-link rendering policy
@Bean
public HalConfiguration globalPolicy() {
return new HalConfiguration() //
.withRenderSingleLinks(RenderSingleLinks.AS_ARRAY);
(1)
}
1
Override Spring HATEOAS&#8217;s default by rendering ALL single-link relations as arrays.
If you prefer to only override some particular link relations, you can create a
HalConfiguration
bean like this:
Example 28. Link relation-based HAL single-link rendering policy
@Bean
public HalConfiguration linkRelationBasedPolicy() {
return new HalConfiguration() //
.withRenderSingleLinksFor( //
IanaLinkRelations.ITEM, RenderSingleLinks.AS_ARRAY)
(1)
.withRenderSingleLinksFor( //
LinkRelation.of("prev"), RenderSingleLinks.AS_SINGLE);
(2)
}
1
Always render
item
link relations as an array.
2
Render
prev
link relations as an object when there is only one link.
If neither of these match your needs, you can use an Ant-style path pattern:
Example 29. Pattern-based HAL single-link rendering policy
@Bean
public HalConfiguration patternBasedPolicy() {
return new HalConfiguration() //
.withRenderSingleLinksFor( //
"http*", RenderSingleLinks.AS_ARRAY);
(1)
}
1
Render all link relations that start with
http
as an array.
The pattern-based approach uses Spring&#8217;s
AntPathMatcher
.
All of these
HalConfiguration
withers can be combined to form one comprehensive policy. Be sure to test your API
extensively to avoid surprises.
4.1.3. Link title internationalization
HAL defines a
title
attribute for its link objects.
These titles can be populated by using Spring&#8217;s resource bundle abstraction and a resource bundle named
rest-messages
so that clients can use them in their UIs directly.
This bundle will be set up automatically and is used during HAL link serialization.
To define a title for a link, use the key template
_links.$relationName.title
as follows:
Example 30. A sample
rest-messages.properties
_links.cancel.title=Cancel order
_links.payment.title=Proceed to checkout
This will result in the following HAL representation:
Example 31. A sample HAL document with link titles defined
{
"_links" : {
"cancel" : {
"href" : "…"
"title" : "Cancel order"
},
"payment" : {
"href" : "…"
"title" : "Proceed to checkout"
}
}
}
4.1.4.
Using the
CurieProvider
API
The
Web Linking RFC
describes registered and extension link relation types. Registered rels are well-known strings registered with the
IANA registry of link relation types
. Extension
rel
URIs can be used by applications that do not wish to register a relation type. Each one is a URI that uniquely identifies the relation type. The
rel
URI can be serialized as a compact URI or
Curie
. For example, a curie of
ex:persons
stands for the link relation type
example.com/rels/persons
if
ex
is defined as
example.com/rels/{rel}
. If curies are used, the base URI must be present in the response scope.
The
rel
values created by the default
RelProvider
are extension relation types and, as a result, must be URIs, which can cause a lot of overhead. The
CurieProvider
API takes care of that: It lets you define a base URI as a URI template and a prefix that stands for that base URI. If a
CurieProvider
is present, the
RelProvider
prepends all
rel
values with the curie prefix. Furthermore a
curies
link is automatically added to the HAL resource.
The following configuration defines a default curie provider:
@Configuration
@EnableWebMvc
@EnableHypermediaSupport(type= {HypermediaType.HAL})
public class Config {
@Bean
public CurieProvider curieProvider() {
return new DefaultCurieProvider("ex", new UriTemplate("https://www.example.com/rels/{rel}"));
}
}
Note that now the
ex:
prefix automatically appears before all rel values that are not registered with IANA, as in
ex:orders
. Clients can use the
curies
link to resolve a curie to its full form.
The following example shows how to do so:
{
"_links": {
"self": {
"href": "https://myhost/person/1"
},
"curies": {
"name": "ex",
"href": "https://example.com/rels/{rel}",
"templated": true
},
"ex:orders": {
"href": "https://myhost/person/1/orders"
}
},
"firstname": "Dave",
"lastname": "Matthews"
}
Since the purpose of the
CurieProvider
API is to allow for automatic curie creation, you can define only one
CurieProvider
bean per application scope.
4.2. HAL-FORMS
HAL-FORMS
is designed to add runtime FORM support to the
HAL media type
.
HAL-FORMS "looks like HAL." However, it is important to keep in mind that HAL-FORMS is not the same as HAL — the two
should not be thought of as interchangeable in any way.
&#8212; Mike Amundsen
HAL-FORMS spec
To enable this media type, put the following configuration in your code:
Example 32. HAL-FORMS enabled application
@Configuration
@EnableHypermediaSupport(type = HypermediaType.HAL_FORMS)
public class HalFormsApplication {
}
Anytime a client supplies an
Accept
header with
application/prs.hal-forms+json
, you can expect something like this:
Example 33. HAL-FORMS sample document
{
"firstName" : "Frodo",
"lastName" : "Baggins",
"role" : "ring bearer",
"_links" : {
"self" : {
"href" : "http://localhost:8080/employees/1"
}
},
"_templates" : {
"default" : {
"method" : "put",
"contentType" : "",
"properties" : [ {
"name" : "firstName",
"required" : true
}, {
"name" : "lastName",
"required" : true
}, {
"name" : "role",
"required" : true
} ]
},
"partiallyUpdateEmployee" : {
"method" : "patch",
"contentType" : "",
"properties" : [ {
"name" : "firstName",
"required" : false
}, {
"name" : "lastName",
"required" : false
}, {
"name" : "role",
"required" : false
} ]
}
}
}
Check out the
HAL-FORMS spec
to understand the details of the
_templates
attribute.
Read about the
Affordances API
to augment your controllers with this extra metadata.
As for single-item (
EntityModel
) and aggregate root collections (
CollectionModel
), Spring HATEOAS renders them
identically to
HAL documents
.
4.2.1. Defining HAL-FORMS metadata
HAL-FORMS allows to describe criterias for each form field.
Spring HATEOAS allows to customize those by shaping the model type for the input and output types and using annotations on them.
Attribute
Description
readOnly
Set to
true
if there&#8217;s no setter method for the property. If that is present, use Jackson&#8217;s
@JsonProperty(Access.READ_ONLY)
on the accessors or field explicitly. Not rendered by default, thus defaulting to
false
.
regex
Can be customized by using JSR-303&#8217;s
@Pattern
annotation either on the field or a type. In case of the latter the pattern will be used for every property declared as that particular type. Not rendered by default.
required
Can be customized by using JSR-303&#8217;s
@NotNull
. Not rendered by default and thus defaulting to
false
. Templates using
PATCH
as method will automatically have all properties set to not required.
For types that you cannot annotate manually, you can register a custom pattern via a
HalFormsConfiguration
bean present in the application context.
@Configuration
class CustomConfiguration {
@Bean
HalFormsConfiguration halFormsConfiguration() {
HalFormsConfiguration configuration = new HalFormsConfiguration();
configuration.registerPatternFor(CreditCardNumber.class, "[0-9]{16}");
}
}
This setup will cause the HAL-FORMS template properties for representation model properties of type
CreditCardNumber
to declare a
regex
field with value
[0-9]{16}
.
4.2.2. Internationalization of form attributes
HAL-FORMS contains attributes that are intended for human interpretation, like a template&#8217;s title or property prompts.
These can be defined and internationalized us
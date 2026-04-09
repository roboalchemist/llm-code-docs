Package jakarta.faces.application

# Class ApplicationConfigurationPopulator

java.lang.Object
jakarta.faces.application.ApplicationConfigurationPopulator

---

public abstract class ApplicationConfigurationPopulator
extends Object

 This class defines a `java.util.ServiceLoader` service which enables programmatic configuration of the Jakarta
 Server Faces runtime using the existing Application Configuration Resources schema. See the
 section 11.3.2 "Application Startup Behavior" in the Jakarta Faces Specification Document
 for the specification on when and how implementations of this
 service are used.

Since:
2.2

-

## Constructor Summary

Constructors

Constructor
Description
`ApplicationConfigurationPopulator()`

-

## Method Summary

Modifier and Type
Method
Description
`abstract void`
`populateApplicationConfiguration(Document toPopulate)`

 Service providers that implement this service must be called by the Jakarta Faces runtime exactly once for
 each implementation, at startup, before any requests have been serviced.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

-

## Constructor Details

-

### ApplicationConfigurationPopulator

public ApplicationConfigurationPopulator()

-

## Method Details

-

### populateApplicationConfiguration

public abstract void populateApplicationConfiguration(Document toPopulate)

 Service providers that implement this service must be called by the Jakarta Faces runtime exactly once for
 each implementation, at startup, before any requests have been serviced. Before calling the
 `populateApplicationConfiguration(org.w3c.dom.Document)` method, the runtime must ensure that the `Document` argument is empty
 aside from being pre-configured to be in the proper namespace for an Application Configuration Resources file:
 `https://jakarta.ee/xml/ns/jakartaee`. Implementations of this service must ensure that any changes made to the
 argument `
Document` conform to that schema as defined in the specification. The Jakarta Faces runtime is not required to
 validate the `Document` after control returns from the service implementation, though it may do so.

 Ordering of Artifacts

 If the document is made to contain an `<ordering>` element, as specified in the
 section 11.3.8 "Ordering of Artifacts" in the Jakarta Faces Specification Document,
 the document will be prioritized accordingly. Otherwise, the
 runtime must place the document in the list of other Application Configuration Resources documents at the "lowest"
 priority, meaning any conflicts that may arise between the argument document and any other Application Configuration
 Resources are resolved in favor of the other document.

Parameters:
`toPopulate` - The Document to populate with configuration.
Since:
2.2

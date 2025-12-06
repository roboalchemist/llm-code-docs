# Source: https://docs.vespa.ai/en/applications/containers.html.md

# Container clusters

 

Vespa's Java container - JDisc, hosts all application components as well as the stateless logic of Vespa itself. Which particular components are hosted by a container cluster is configured in services.xml. The main features of JDIsc are:

- HTTP serving out of the box from an embedded Jetty server, and support for plugging in other transport mechanisms.
- Integration with the config system of Vespa which allows components to [receive up-to-date config](configuring-components.html) (by constructor injection) resulting from application deployment.
- [Dependency injection based on Guice](dependency-injection.html) (Felix), but extended for configs and component collections.
- A component model based on [OSGi](bundles.html) which allows component to be (re)deployed to running servers, and to control which APIs they expose to others.
- The features above combine to allow application package changes (changes to components, configuration or data) to be applied by Vespa without disrupting request serving nor requiring restarts.
- Standard component types exists for 
  - [general request handling](request-handlers.html)
  - [chained request-response processing](processing.html)
  - [processing document writes](document-processors.html)
  - [intercepting queries and results](searchers.html)
  - [rendering responses](result-renderers.html)

 Application components can be of any other type as well and do not need to reference any Vespa API to be loaded and managed by the container. 
- A general [chain composition](chaining.html) mechanism for components.

## Developing Components

- The JDisc container provides a framework for processing requests and responses, named _Processing_ - its building blocks are: 
  - [Chains](chaining.html) of other components that are to be executed serially, with each providing some service or transform 
  - [Processors](processing.html) that change the request and / or the response. They may also make multiple forward requests, in series or parallel, or manufacture the response content themselves 
  - [Renderers](processing.html#response-rendering) that are used to serialize a Processor's response before returning it to a client 

- Application Lifecycle and unit testing: 
  - [Configuring components](configuring-components.html) with custom configuration 
  - [Component injection](dependency-injection.html) allows components to access other application components 
  - Learn how to [build OSGi bundles](bundles.html) and how to [troubleshoot](bundles.html#troubleshooting) classloading issues 
  - Using [Libraries for Pluggable Frameworks](pluggable-frameworks.html) from a component may result in class loading issues that require extra setup in the application 
  - [Unit testing configurable components](unit-testing.html#unit-testing-configurable-components)

- Handlers and filters: 
  - [Http servers and security filters](http-servers-and-filters.html) for incoming connections on HTTP and HTTPS 
  - [Request handlers](request-handlers.html) to process incoming requests and generate responses 

- Searchers and Document Processors: 
  - [Searcher](searchers.html) and [search result renderer](result-renderers.html) development 
  - [Document processing](document-processors.html)

## Reference documentation

- [services.xml](../reference/applications/services/container.html)

## Other related documents

- [Designing RESTful web services](web-services.html) as Vespa Components 
- [healthchecks](../reference/operations/health-checks.html) - using the Container with a VIP 
- [Vespa Component Reference](../reference/applications/components.html): The Container's request processing lifecycle 

 Copyright © 2025 - [Cookie Preferences](#)


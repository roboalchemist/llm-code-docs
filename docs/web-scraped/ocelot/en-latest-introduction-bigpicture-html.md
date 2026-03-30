# Source: https://ocelot.readthedocs.io/en/latest/introduction/bigpicture.html

Title: Big Picture — Ocelot Gateway 24.1 "Globality" documentation

URL Source: https://ocelot.readthedocs.io/en/latest/introduction/bigpicture.html

Markdown Content:
Ocelot is aimed at people using .NET running a microservices (service-oriented) architecture (aka SOA) that need a unified point of entry into their system. However it will work with anything that speaks HTTP(S) and run on any platform that [ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/) supports.

Ocelot consists of a series of ASP.NET Core [middlewares](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/) arranged in a specific order.

Ocelot manipulates the `HttpRequest` object into a state specified by its configuration until it reaches a request builder middleware, where it creates a `HttpRequestMessage` object which is used to make a request to a downstream service. The middleware that makes the request is the last thing in the Ocelot pipeline. It does not call the next middleware. The response from the downstream service is retrieved as the request goes back up the Ocelot pipeline. There is a piece of middleware that maps the `HttpResponseMessage` onto the `HttpResponse` object, and that is returned to the client. That is basically it with a bunch of other features!

The following are configurations that you use when deploying Ocelot.

Basic Implementation[¶](https://ocelot.readthedocs.io/en/latest/introduction/bigpicture.html#basic-implementation "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------

![Image 1: ../_images/OcelotBasic.jpg](https://ocelot.readthedocs.io/en/latest/_images/OcelotBasic.jpg)
Multiple Instances[¶](https://ocelot.readthedocs.io/en/latest/introduction/bigpicture.html#multiple-instances "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------

![Image 2: ../_images/OcelotMultipleInstances.jpg](https://ocelot.readthedocs.io/en/latest/_images/OcelotMultipleInstances.jpg)
With Consul[¶](https://ocelot.readthedocs.io/en/latest/introduction/bigpicture.html#with-consul "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------

![Image 3: ../_images/OcelotMultipleInstancesConsul.jpg](https://ocelot.readthedocs.io/en/latest/_images/OcelotMultipleInstancesConsul.jpg)
With Service Fabric[¶](https://ocelot.readthedocs.io/en/latest/introduction/bigpicture.html#with-service-fabric "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------

![Image 4: ../_images/OcelotServiceFabric.jpg](https://ocelot.readthedocs.io/en/latest/_images/OcelotServiceFabric.jpg)

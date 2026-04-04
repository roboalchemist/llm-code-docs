# Source: https://archivedocs.stackstate.com/5.1/develop/developer-guides/integrating_external_services.md

# Integrate external services

Not all custom logic needs to be coded using the [StackState Scripting Language (STSL)](https://archivedocs.stackstate.com/5.1/develop/reference/scripting). When your logic grows very complex you may want to call out to your own service, written in any programming language that fits your needs.

Integrating external services with StackState is done by using the [HTTP script API](https://archivedocs.stackstate.com/5.1/develop/reference/scripting/script-apis/http) from a [function](https://archivedocs.stackstate.com/5.1/develop/developer-guides/custom-functions/functions). This is similar to a webhook, but more flexible. Whereas with a webhook your webserver needs to follow a predefined protocol and receives a predefined set of data, which may not fit your needs, with this mechanism you can define your own protocol and decide what extra information you want to retrieve from StackState before sending a request to your microservice.

## Example

Let's say you have developed a service that has a list of components that should not propagate their state. This service can be developed in any language, but is accessible via a REST API.

Whenever you call your HTTP server with `/propagation?componentName=SOMENAME` it will respond with: `{ "allow": "OK" }` or `{ "allow": "NOK" }` depending on the passed name of the component.

You could then integrate your service by making a propagation function with the following script:

{% code lineNumbers="true" %}

```
Component.withId(componentId).get().then { component ->  
    Http.get("http://mydomain/propagation").param("componentName", component.name).jsonBody() 
}.then { response ->
    if (response.allow) return transparentState;
    else return CLEAR
}
```

{% endcode %}

This function first gets the name of the component, then calls out via HTTP to the external service and then uses its response to decide how StackState should propagate the state of the given component.

## Requirements

* Your service should be network-resolvable and accessible by the StackState servers that run the scripts.
* HTTPS is supported only for certificates that are signed by the Certificate Authorities known to the Java Keystore accessible by the StackState server.
* StackState scripts have a default configurable timeout, for example 15 seconds. If your service doesn't respond in a timely fashion an error will be logged and depending on the type of function different types of error behavior will be observed.
* Make sure your service can keep up with the demand. Depending on the type of function and the size of the 4T model, StackState might make a lot of calls to your service.

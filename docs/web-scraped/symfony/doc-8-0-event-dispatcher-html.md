# Source: https://symfony.com/doc/8.0/event_dispatcher.html

Title: Events and Event Listeners (Symfony Docs)

URL Source: https://symfony.com/doc/8.0/event_dispatcher.html

Markdown Content:
During the execution of a Symfony application, lots of event notifications are triggered. Your application can listen to these notifications and respond to them by executing any piece of code.

Symfony triggers several [events related to the kernel](https://symfony.com/doc/current/reference/events.html) while processing the HTTP Request. Third-party bundles may also dispatch events, and you can even dispatch [custom events](https://symfony.com/doc/current/components/event_dispatcher.html) from your own code.

All the examples shown in this article use the same `KernelEvents::EXCEPTION` event for consistency purposes. In your own application, you can use any event and even mix several of them in the same subscriber.

[Creating an Event Listener](https://symfony.com/doc/8.0/event_dispatcher.html#creating-an-event-listener "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------------------------

The most common way to listen to an event is to register an **event listener**:

Now that the class is created, you need to register it as a service and notify Symfony that it is an event listener by using a special "tag":

Symfony follows this logic to decide which method to call inside the event listener class:

1. If the `kernel.event_listener` tag defines the `method` attribute, that's the name of the method to be called;
2. If no `method` attribute is defined, try to call the `__invoke()` magic method (which makes event listeners invokable);
3. If the `__invoke()` method is not defined either, throw an exception.

Note

There is an optional attribute for the `kernel.event_listener` tag called `priority`, which is a positive or negative integer that defaults to `0` and it controls the order in which listeners are executed (the higher the number, the earlier a listener is executed). This is useful when you need to guarantee that one listener is executed before another. The priorities of the internal Symfony listeners usually range from `-256` to `256` but your own listeners can use any positive or negative integer.

Note

There is an optional attribute for the `kernel.event_listener` tag called `event` which is useful when listener `$event` argument is not typed. If you configure it, it will change type of `$event` object. For the `kernel.exception` event, it is [ExceptionEvent](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Event/ExceptionEvent.php "Symfony\Component\HttpKernel\Event\ExceptionEvent"). Check out the [Symfony events reference](https://symfony.com/doc/current/reference/events.html) to see what type of object each event provides.

With this attribute, Symfony follows this logic to decide which method to call inside the event listener class:

1. If the `kernel.event_listener` tag defines the `method` attribute, that's the name of the method to be called;
2. If no `method` attribute is defined, try to call the method whose name is `on` + "PascalCased event name" (e.g. `onKernelException()` method for the `kernel.exception` event);
3. If that method is not defined either, try to call the `__invoke()` magic method (which makes event listeners invokable);
4. If the `__invoke()` method is not defined either, throw an exception.

### [Defining Event Listeners with PHP Attributes](https://symfony.com/doc/8.0/event_dispatcher.html#defining-event-listeners-with-php-attributes "Permalink to this headline")

An alternative way to define an event listener is to use the [AsEventListener](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/EventDispatcher/Attribute/AsEventListener.php "Symfony\Component\EventDispatcher\Attribute\AsEventListener") PHP attribute. This allows you to configure the listener inside its class, without having to add any configuration in external files:

You can add multiple `#[AsEventListener]` attributes to configure different methods. The `method` property is optional, and when not defined, it defaults to `on` + uppercased event name. In the example below, the `'foo'` event listener doesn't explicitly define its method, so the `onFoo()` method will be called:

[AsEventListener](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/EventDispatcher/Attribute/AsEventListener.php "Symfony\Component\EventDispatcher\Attribute\AsEventListener") can also be applied to methods directly:

Note

Note that the attribute doesn't require its `event` parameter to be set if the method already type-hints the expected event.

[Creating an Event Subscriber](https://symfony.com/doc/8.0/event_dispatcher.html#creating-an-event-subscriber "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------------------------

Another way to listen to events is via an **event subscriber**, which is a class that defines one or more methods that listen to one or various events. The main difference with the event listeners is that subscribers always know the events to which they are listening.

If different event subscriber methods listen to the same event, their order is defined by the `priority` parameter. This value is a positive or negative integer which defaults to `0`. The higher the number, the earlier the method is called. **Priority is aggregated for all listeners and subscribers**, so your methods could be called before or after the methods defined in other listeners and subscribers. To learn more about event subscribers, read [The EventDispatcher Component](https://symfony.com/doc/current/components/event_dispatcher.html).

The following example shows an event subscriber that defines several methods which listen to the same [kernel.exception event](https://symfony.com/doc/current/components/http_kernel.html#component-http-kernel-kernel-exception) via its `ExceptionEvent` class:

That's it! Your `services.yaml` file should already be setup to load services from the `EventSubscriber` directory. Symfony takes care of the rest.

Tip

If your methods are _not_ called when an exception is thrown, double-check that you're [loading services](https://symfony.com/doc/current/service_container.html#service-container-services-load-example) from the `EventSubscriber` directory and have [autoconfigure](https://symfony.com/doc/current/service_container.html#services-autoconfigure) enabled. You can also manually add the `kernel.event_subscriber` tag.

[Request Events, Checking Types](https://symfony.com/doc/8.0/event_dispatcher.html#request-events-checking-types "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------------------------

A single page can make several requests (one main request, and then multiple sub-requests - typically when [embedding controllers in templates](https://symfony.com/doc/current/templates.html#templates-embed-controllers)). For the core Symfony events, you might need to check to see if the event is for a "main" request or a "sub request":

Certain things, like checking information on the _real_ request, may not need to be done on the sub-request listeners.

[Listeners or Subscribers](https://symfony.com/doc/8.0/event_dispatcher.html#listeners-or-subscribers "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------------

Listeners and subscribers can be used in the same application indistinctly. The decision to use either of them is usually a matter of personal taste. However, there are some minor advantages for each of them:

* **Subscribers are easier to reuse** because the knowledge of the events is kept in the class rather than in the service definition. This is the reason why Symfony uses subscribers internally;
* **Listeners are more flexible** because bundles can enable or disable each of them conditionally depending on some configuration value.

[Event Aliases](https://symfony.com/doc/8.0/event_dispatcher.html#event-aliases "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------

When configuring event listeners and subscribers via dependency injection, Symfony's core events can also be referred to by the fully qualified class name (FQCN) of the corresponding event class:

Internally, the event FQCN are treated as aliases for the original event names. Since the mapping already happens when compiling the service container, event listeners and subscribers using FQCN instead of event names will appear under the original event name when inspecting the event dispatcher.

This alias mapping can be extended for custom events by registering the compiler pass `AddEventAliasesPass`:

The compiler pass will always extend the existing list of aliases. Because of that, it is safe to register multiple instances of the pass with different configurations.

[Debugging Event Listeners](https://symfony.com/doc/8.0/event_dispatcher.html#debugging-event-listeners "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------------------

You can find out what listeners are registered in the event dispatcher using the console. To show all events and their listeners, run:

You can get registered listeners for a particular event by specifying its name:

or can get everything which partial matches the event name:

The [security](https://symfony.com/doc/current/security.html) system uses an event dispatcher per firewall. Use the `--dispatcher` option to get the registered listeners for a particular event dispatcher:

[How to Set Up Before and After Filters](https://symfony.com/doc/8.0/event_dispatcher.html#how-to-set-up-before-and-after-filters "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------------------------------------------------

It is quite common in web application development to need some logic to be performed right before or directly after your controller actions acting as filters or hooks.

Some web frameworks define methods like `preExecute()` and `postExecute()`, but there is no such thing in Symfony. The good news is that there is a much better way to interfere with the Request -> Response process using the [EventDispatcher component](https://symfony.com/doc/current/components/event_dispatcher.html).

### [Token Validation Example](https://symfony.com/doc/8.0/event_dispatcher.html#token-validation-example "Permalink to this headline")

Imagine that you need to develop an API where some controllers are public but some others are restricted to one or some clients. For these private features, you might provide a token to your clients to identify themselves.

So, before executing your controller action, you need to check if the action is restricted or not. If it is restricted, you need to validate the provided token.

Note

Please note that for simplicity in this recipe, tokens will be defined in config and neither database setup nor authentication via the Security component will be used.

### [Before Filters with the `kernel.controller` Event](https://symfony.com/doc/8.0/event_dispatcher.html#before-filters-with-the-kernel-controller-event "Permalink to this headline")

First, define some token configuration as parameters:

#### [Tag Controllers to Be Checked](https://symfony.com/doc/8.0/event_dispatcher.html#tag-controllers-to-be-checked "Permalink to this headline")

A `kernel.controller` (aka `KernelEvents::CONTROLLER`) listener gets notified on _every_ request, right before the controller is executed. So, first, you need some way to identify if the controller that matches the request needs token validation.

A clean and simple way is to create an empty interface and make the controllers implement it:

A controller that implements this interface looks like this:

#### [Creating an Event Subscriber](https://symfony.com/doc/8.0/event_dispatcher.html#creating-an-event-subscriber-1 "Permalink to this headline")

Next, you'll need to create an event subscriber, which will hold the logic that you want to be executed before your controllers. If you're not familiar with event subscribers, you can learn more about [how to use them](https://symfony.com/doc/current/event_dispatcher.html#events-subscriber):

That's it! Your `services.yaml` file should already be setup to load services from the `EventSubscriber` directory. Symfony takes care of the rest. Your `TokenSubscriber``onKernelController()` method will be executed on each request. If the controller that is about to be executed implements `TokenAuthenticatedController`, token authentication is applied. This lets you have a "before" filter on any controller you want.

Tip

If your subscriber is _not_ called on each request, double-check that you're [loading services](https://symfony.com/doc/current/service_container.html#service-container-services-load-example) from the `EventSubscriber` directory and have [autoconfigure](https://symfony.com/doc/current/service_container.html#services-autoconfigure) enabled. You can also manually add the `kernel.event_subscriber` tag.

### [After Filters with the `kernel.response` Event](https://symfony.com/doc/8.0/event_dispatcher.html#after-filters-with-the-kernel-response-event "Permalink to this headline")

In addition to having a "hook" that's executed _before_ your controller, you can also add a hook that's executed _after_ your controller. For this example, imagine that you want to add a `sha1` hash (with a salt using that token) to all responses that have passed this token authentication.

Another core Symfony event - called `kernel.response` (aka `KernelEvents::RESPONSE`) - is notified on every request, but after the controller returns a Response object. To create an "after" listener, create a listener class and register it as a service on this event.

For example, take the `TokenSubscriber` from the previous example and first record the authentication token inside the request attributes. This will serve as a basic flag that this request underwent token authentication:

Now, configure the subscriber to listen to another event and add `onKernelResponse()`. This will look for the `auth_token` flag on the request object and set a custom header on the response if it's found:

That's it! The `TokenSubscriber` is now notified before every controller is executed (`onKernelController()`) and after every controller returns a response (`onKernelResponse()`). By making specific controllers implement the `TokenAuthenticatedController` interface, your listener knows which controllers it should take action on. And by storing a value in the request's "attributes" bag, the `onKernelResponse()` method knows to add the extra header. Have fun!

[How to Customize a Method Behavior without Using Inheritance](https://symfony.com/doc/8.0/event_dispatcher.html#how-to-customize-a-method-behavior-without-using-inheritance "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you want to do something right before, or directly after a method is called, you can dispatch an event respectively at the beginning or at the end of the method:

In this example, two events are dispatched:

1. `mailer.pre_send`, before the method is called,
2. and `mailer.post_send` after the method is called.

Tip

When injecting the event dispatcher, type-hint one of its interfaces instead of the concrete `EventDispatcher` class. Use [EventDispatcherInterface](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Contracts/EventDispatcher/EventDispatcherInterface.php "Symfony\Contracts\EventDispatcher\EventDispatcherInterface") when you only need to dispatch events, or [EventDispatcherInterface](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/EventDispatcher/EventDispatcherInterface.php "Symfony\Component\EventDispatcher\EventDispatcherInterface") if you also need to inspect or manage listeners (e.g. `addListener()`, `removeListener()`).

Each uses a custom Event class to communicate information to the listeners of the two events. For example, `BeforeSendMailEvent` might look like this:

And the `AfterSendMailEvent` even like this:

Both events allow you to get some information (e.g. `getMessage()`) and even change that information (e.g. `setMessage()`).

Now, you can create an event subscriber to hook into this event. For example, you could listen to the `mailer.post_send` event and change the method's return value:

That's it! Your subscriber should be called automatically (or read more about [event subscriber configuration](https://symfony.com/doc/current/event_dispatcher.html#ref-event-subscriber-configuration)).

[Learn More](https://symfony.com/doc/8.0/event_dispatcher.html#learn-more "Permalink to this headline")
-------------------------------------------------------------------------------------------------------

* [The Request-Response Lifecycle](https://symfony.com/doc/current/components/http_kernel.html#the-workflow-of-a-request)
* [Built-in Symfony Events](https://symfony.com/doc/current/reference/events.html)
* [Security-related Events](https://symfony.com/doc/current/security.html#security-security-events)
* [The EventDispatcher Component](https://symfony.com/doc/current/components/event_dispatcher.html)

This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.

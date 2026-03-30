# Source: https://symfony.com/doc/8.0/components/http_kernel.html

Title: The HttpKernel Component (Symfony Docs)

URL Source: https://symfony.com/doc/8.0/components/http_kernel.html

Markdown Content:
[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/components/http_kernel.rst)

> The HttpKernel component provides a structured process for converting a `Request` into a `Response` by making use of the EventDispatcher component. It's flexible enough to create a full-stack framework (Symfony) or an advanced CMS (Drupal).

[Installation](https://symfony.com/doc/8.0/components/http_kernel.html#installation "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------

Note

If you install this component outside of a Symfony application, you must require the `vendor/autoload.php` file in your code to enable the class autoloading mechanism provided by Composer. Read [this article](https://symfony.com/doc/current/components/using_components.html) for more details.

[The Request-Response Lifecycle](https://symfony.com/doc/8.0/components/http_kernel.html#the-request-response-lifecycle "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------------------------------

See also

This article explains how to use the HttpKernel features as an independent component in any PHP application. In Symfony applications everything is already configured and ready to use. Read the [Controller](https://symfony.com/doc/current/controller.html) and [Events and Event Listeners](https://symfony.com/doc/current/event_dispatcher.html) articles to learn about how to use it to create controllers and define events in Symfony applications.

Every HTTP web interaction begins with a request and ends with a response. Your job as a developer is to create PHP code that reads the request information (e.g. the URL) and creates and returns a response (e.g. an HTML page or JSON string). This is a simplified overview of the request-response lifecycle in Symfony applications:

1. The **user** asks for a **resource** in a **browser**;
2. The **browser** sends a **request** to the **server**;
3. **Symfony** gives the **application** a **Request** object;
4. The **application** generates a **Response** object using the data of the **Request** object;
5. The **server** sends back the **response** to the **browser**;
6. The **browser** displays the **resource** to the **user**.

Typically, some sort of framework or system is built to handle all the repetitive tasks (e.g. routing, security, etc) so that a developer can build each _page_ of the application. Exactly _how_ these systems are built varies greatly. The HttpKernel component provides an interface that formalizes the process of starting with a request and creating the appropriate response. The component is meant to be the heart of any application or framework, no matter how varied the architecture of that system:

Internally, [HttpKernel::handle()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/HttpKernel.php#:~:text=function%20handle "Symfony\Component\HttpKernel\HttpKernel::handle()") - the concrete implementation of [HttpKernelInterface::handle()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/HttpKernelInterface.php#:~:text=function%20handle "Symfony\Component\HttpKernel\HttpKernelInterface::handle()") - defines a lifecycle that starts with a [Request](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpFoundation/Request.php "Symfony\Component\HttpFoundation\Request") and ends with a [Response](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpFoundation/Response.php "Symfony\Component\HttpFoundation\Response").

The exact details of this lifecycle are the key to understanding how the kernel (and the Symfony Framework or any other library that uses the kernel) works.

### [HttpKernel: Driven by Events](https://symfony.com/doc/8.0/components/http_kernel.html#httpkernel-driven-by-events "Permalink to this headline")

The `HttpKernel::handle()` method works internally by dispatching events. This makes the method both flexible, but also a bit abstract, since all the "work" of a framework/application built with HttpKernel is actually done in event listeners.

To help explain this process, this document looks at each step of the process and talks about how one specific implementation of the HttpKernel - the Symfony Framework - works.

Initially, using the [HttpKernel](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/HttpKernel.php "Symfony\Component\HttpKernel\HttpKernel") does not take many steps. You create an [event dispatcher](https://symfony.com/doc/current/components/event_dispatcher.html) and a [controller and argument resolver](https://symfony.com/doc/current/components/http_kernel.html#component-http-kernel-resolve-controller) (explained below). To complete your working kernel, you'll add more event listeners to the events discussed below:

See "[A full working example](https://symfony.com/doc/current/components/http_kernel.html#http-kernel-working-example)" for a more concrete implementation.

For general information on adding listeners to the events below, see [Creating an Event Listener](https://symfony.com/doc/current/components/http_kernel.html#http-kernel-creating-listener).

See also

There is a wonderful tutorial series on using the HttpKernel component and other Symfony components to create your own framework. See [Introduction](https://symfony.com/doc/current/create_framework/introduction.html).

### [1) The `kernel.request` Event](https://symfony.com/doc/8.0/components/http_kernel.html#1-the-kernel-request-event "Permalink to this headline")

**Typical Purposes**: To add more information to the `Request`, initialize parts of the system, or return a `Response` if possible (e.g. a security layer that denies access).

[Kernel Events Information Table](https://symfony.com/doc/current/components/http_kernel.html#component-http-kernel-event-table)

The first event that is dispatched inside [HttpKernel::handle](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/HttpKernel.php#:~:text=function%20handle "Symfony\Component\HttpKernel\HttpKernel::handle()") is `kernel.request`, which may have a variety of different listeners.

Listeners of this event can be quite varied. Some listeners - such as a security listener - might have enough information to create a `Response` object immediately. For example, if a security listener determined that a user doesn't have access, that listener may return a [RedirectResponse](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpFoundation/RedirectResponse.php "Symfony\Component\HttpFoundation\RedirectResponse") to the login page or a 403 Access Denied response.

If a `Response` is returned at this stage, the process skips directly to the [kernel.response](https://symfony.com/doc/current/components/http_kernel.html#component-http-kernel-kernel-response) event.

Other listeners initialize things or add more information to the request. For example, a listener might determine and set the locale on the `Request` object.

Another common listener is routing. A router listener may process the `Request` and determine the controller that should be rendered (see the next section). In fact, the `Request` object has an "[attributes](https://symfony.com/doc/current/components/http_foundation.html#component-foundation-attributes)" bag which is a perfect spot to store this extra, application-specific data about the request. This means that if your router listener somehow determines the controller, it can store it on the `Request` attributes (which can be used by your controller resolver).

Overall, the purpose of the `kernel.request` event is either to create and return a `Response` directly, or to add information to the `Request` (e.g. setting the locale or setting some other information on the `Request` attributes).

Note

When setting a response for the `kernel.request` event, the propagation is stopped. This means listeners with lower priority won't be executed.

### [2) Resolve the Controller](https://symfony.com/doc/8.0/components/http_kernel.html#2-resolve-the-controller "Permalink to this headline")

Assuming that no `kernel.request` listener was able to create a `Response`, the next step in HttpKernel is to determine and prepare (i.e. resolve) the controller. The controller is the part of the end-application's code that is responsible for creating and returning the `Response` for a specific page. The only requirement is that it is a PHP callable - i.e. a function, method on an object or a `Closure`.

But _how_ you determine the exact controller for a request is entirely up to your application. This is the job of the "controller resolver" - a class that implements [ControllerResolverInterface](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Controller/ControllerResolverInterface.php "Symfony\Component\HttpKernel\Controller\ControllerResolverInterface") and is one of the constructor arguments to `HttpKernel`.

Your job is to create a class that implements the interface and fill in its method: `getController()`. In fact, one default implementation already exists, which you can use directly or learn from: [ControllerResolver](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Controller/ControllerResolver.php "Symfony\Component\HttpKernel\Controller\ControllerResolver"). This implementation is explained more in the sidebar below:

Internally, the `HttpKernel::handle()` method first calls [getController()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Controller/ControllerResolverInterface.php#:~:text=function%20getController "Symfony\Component\HttpKernel\Controller\ControllerResolverInterface::getController()") on the controller resolver. This method is passed the `Request` and is responsible for somehow determining and returning a PHP callable (the controller) based on the request's information.

### [3) The `kernel.controller` Event](https://symfony.com/doc/8.0/components/http_kernel.html#3-the-kernel-controller-event "Permalink to this headline")

**Typical Purposes**: Initialize things or change the controller just before the controller is executed.

[Kernel Events Information Table](https://symfony.com/doc/current/components/http_kernel.html#component-http-kernel-event-table)

After the controller callable has been determined, `HttpKernel::handle()` dispatches the `kernel.controller` event. Listeners to this event might initialize some part of the system that needs to be initialized after certain things have been determined (e.g. the controller, routing information) but before the controller is executed.

Another typical use-case for this event is to retrieve the attributes from the controller using the [getAttributes()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Event/ControllerEvent.php#:~:text=function%20getAttributes "Symfony\Component\HttpKernel\Event\ControllerEvent::getAttributes()") method. See the Symfony section below for some examples.

Listeners to this event can also change the controller callable completely by calling [ControllerEvent::setController](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Event/ControllerEvent.php#:~:text=function%20setController "Symfony\Component\HttpKernel\Event\ControllerEvent::setController()") on the event object that's passed to listeners on this event.

### [4) Getting the Controller Arguments](https://symfony.com/doc/8.0/components/http_kernel.html#4-getting-the-controller-arguments "Permalink to this headline")

Next, `HttpKernel::handle()` calls [ArgumentResolverInterface::getArguments()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Controller/ArgumentResolverInterface.php#:~:text=function%20getArguments "Symfony\Component\HttpKernel\Controller\ArgumentResolverInterface::getArguments()"). Remember that the controller returned in `getController()` is a callable. The purpose of `getArguments()` is to return the array of arguments that should be passed to that controller. Exactly how this is done is completely up to your design, though the built-in [ArgumentResolver](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Controller/ArgumentResolver.php "Symfony\Component\HttpKernel\Controller\ArgumentResolver") is a good example.

At this point the kernel has a PHP callable (the controller) and an array of arguments that should be passed when executing that callable.

### [5) Calling the Controller](https://symfony.com/doc/8.0/components/http_kernel.html#5-calling-the-controller "Permalink to this headline")

The next step of `HttpKernel::handle()` is executing the controller.

The job of the controller is to build the response for the given resource. This could be an HTML page, a JSON string or anything else. Unlike every other part of the process so far, this step is implemented by the "end-developer", for each page that is built.

Usually, the controller will return a `Response` object. If this is true, then the work of the kernel is just about done! In this case, the next step is the [kernel.response](https://symfony.com/doc/current/components/http_kernel.html#component-http-kernel-kernel-response) event.

But if the controller returns anything besides a `Response`, then the kernel has a little bit more work to do - [kernel.view](https://symfony.com/doc/current/components/http_kernel.html#component-http-kernel-kernel-view) (since the end goal is _always_ to generate a `Response` object).

Note

A controller must return _something_. If a controller returns `null`, an exception will be thrown immediately.

### [6) The `kernel.view` Event](https://symfony.com/doc/8.0/components/http_kernel.html#6-the-kernel-view-event "Permalink to this headline")

**Typical Purposes**: Transform a non-`Response` return value from a controller into a `Response`

[Kernel Events Information Table](https://symfony.com/doc/current/components/http_kernel.html#component-http-kernel-event-table)

If the controller doesn't return a `Response` object, then the kernel dispatches another event - `kernel.view`. The job of a listener to this event is to use the return value of the controller (e.g. an array of data or an object) to create a `Response`.

This can be useful if you want to use a "view" layer: instead of returning a `Response` from the controller, you return data that represents the page. A listener to this event could then use this data to create a `Response` that is in the correct format (e.g HTML, JSON, etc).

At this stage, if no listener sets a response on the event, then an exception is thrown: either the controller _or_ one of the view listeners must always return a `Response`.

Note

When setting a response for the `kernel.view` event, the propagation is stopped. This means listeners with lower priority won't be executed.

### [7) The `kernel.response` Event](https://symfony.com/doc/8.0/components/http_kernel.html#7-the-kernel-response-event "Permalink to this headline")

**Typical Purposes**: Modify the `Response` object just before it is sent

[Kernel Events Information Table](https://symfony.com/doc/current/components/http_kernel.html#component-http-kernel-event-table)

The end goal of the kernel is to transform a `Request` into a `Response`. The `Response` might be created during the [kernel.request](https://symfony.com/doc/current/components/http_kernel.html#component-http-kernel-kernel-request) event, returned from the [controller](https://symfony.com/doc/current/components/http_kernel.html#component-http-kernel-calling-controller), or returned by one of the listeners to the [kernel.view](https://symfony.com/doc/current/components/http_kernel.html#component-http-kernel-kernel-view) event.

Regardless of who creates the `Response`, another event - `kernel.response` is dispatched directly afterwards. A typical listener to this event will modify the `Response` object in some way, such as modifying headers, adding cookies, or even changing the content of the `Response` itself (e.g. injecting some JavaScript before the end `</body>` tag of an HTML response).

After this event is dispatched, the final `Response` object is returned from [handle()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/HttpKernel.php#:~:text=function%20handle "Symfony\Component\HttpKernel\HttpKernel::handle()"). In the most typical use-case, you can then call the [send()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpFoundation/Response.php#:~:text=function%20send "Symfony\Component\HttpFoundation\Response::send()") method, which sends the headers and prints the `Response` content.

### [8) The `kernel.terminate` Event](https://symfony.com/doc/8.0/components/http_kernel.html#8-the-kernel-terminate-event "Permalink to this headline")

**Typical Purposes**: To perform some "heavy" action after the response has been streamed to the user

[Kernel Events Information Table](https://symfony.com/doc/current/components/http_kernel.html#component-http-kernel-event-table)

The final event of the HttpKernel process is `kernel.terminate` and is unique because it occurs _after_ the `HttpKernel::handle()` method, and after the response is sent to the user. Recall from above, then the code that uses the kernel, ends like this:

As you can see, by calling `$kernel->terminate` after sending the response, you will trigger the `kernel.terminate` event where you can perform certain actions that you may have delayed in order to return the response as quickly as possible to the client (e.g. sending emails).

Warning

Internally, the HttpKernel makes use of the [fastcgi_finish_request](https://secure.php.net/manual/en/function.fastcgi-finish-request.php "fastcgi_finish_request") PHP function. This means that at the moment, only the [PHP FPM](https://www.php.net/manual/en/install.fpm.php) API and the [FrankenPHP](https://frankenphp.dev/) server are able to send a response to the client while the server's PHP process still performs some tasks. With all other server APIs, listeners to `kernel.terminate` are still executed, but the response is not sent to the client until they are all completed.

Note

Using the `kernel.terminate` event is optional, and should only be called if your kernel implements [TerminableInterface](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/TerminableInterface.php "Symfony\Component\HttpKernel\TerminableInterface").

### [9) Handling Exceptions: the `kernel.exception` Event](https://symfony.com/doc/8.0/components/http_kernel.html#9-handling-exceptions-the-kernel-exception-event "Permalink to this headline")

**Typical Purposes**: Handle some type of exception and create an appropriate `Response` to return for the exception

[Kernel Events Information Table](https://symfony.com/doc/current/components/http_kernel.html#component-http-kernel-event-table)

If an exception is thrown at any point inside `HttpKernel::handle()`, another event - `kernel.exception` is dispatched. Internally, the body of the `handle()` method is wrapped in a try-catch block. When any exception is thrown, the `kernel.exception` event is dispatched so that your system can somehow respond to the exception.

Each listener to this event is passed a [ExceptionEvent](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Event/ExceptionEvent.php "Symfony\Component\HttpKernel\Event\ExceptionEvent") object, which you can use to access the original exception via the [getThrowable()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Event/ExceptionEvent.php#:~:text=function%20getThrowable "Symfony\Component\HttpKernel\Event\ExceptionEvent::getThrowable()") method. A typical listener on this event will check for a certain type of exception and create an appropriate error `Response`.

For example, to generate a 404 page, you might throw a special type of exception and then add a listener on this event that looks for this exception and creates and returns a 404 `Response`. In fact, the HttpKernel component comes with an [ErrorListener](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/EventListener/ErrorListener.php "Symfony\Component\HttpKernel\EventListener\ErrorListener"), which if you choose to use, will do this and more by default (see the sidebar below for more details).

The [ExceptionEvent](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Event/ExceptionEvent.php "Symfony\Component\HttpKernel\Event\ExceptionEvent") exposes the [isKernelTerminating()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Event/ExceptionEvent.php#:~:text=function%20isKernelTerminating "Symfony\Component\HttpKernel\Event\ExceptionEvent::isKernelTerminating()") method, which you can use to determine if the kernel is currently terminating at the moment the exception was thrown.

Note

When setting a response for the `kernel.exception` event, the propagation is stopped. This means listeners with lower priority won't be executed.

### [10) Resetting the State After the Request/Response Cycle](https://symfony.com/doc/8.0/components/http_kernel.html#10-resetting-the-state-after-the-request-response-cycle "Permalink to this headline")

PHP is inherently stateless: no resources are shared across different requests. However, certain runtimes (e.g. [FrankenPHP](https://frankenphp.dev/) in worker mode) allow the kernel to handle multiple requests within the same process. In that scenario, services may retain state between requests, potentially causing memory leaks or unexpected behavior.

To prevent this, make your service implement [ResetInterface](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Contracts/Service/ResetInterface.php "Symfony\Contracts\Service\ResetInterface") and clean up any accumulated state in the `reset()` method. The kernel calls this method automatically after each request/response cycle in long-running processes.

[Creating an Event Listener](https://symfony.com/doc/8.0/components/http_kernel.html#creating-an-event-listener "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------------------------------

As you've seen, you can create and attach event listeners to any of the events dispatched during the `HttpKernel::handle()` cycle. Typically a listener is a PHP class with a method that's executed, but it can be anything. For more information on creating and attaching event listeners, see [The EventDispatcher Component](https://symfony.com/doc/current/components/event_dispatcher.html).

The name of each of the "kernel" events is defined as a constant on the [KernelEvents](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/KernelEvents.php "Symfony\Component\HttpKernel\KernelEvents") class. Additionally, each event listener is passed a single argument, which is some subclass of [KernelEvent](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Event/KernelEvent.php "Symfony\Component\HttpKernel\Event\KernelEvent"). This object contains information about the current state of the system and each event has their own event object:

| Name | `KernelEvents` Constant | Argument passed to the listener |
| --- | --- | --- |
| kernel.request | `KernelEvents::REQUEST` | [RequestEvent](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Event/RequestEvent.php "Symfony\Component\HttpKernel\Event\RequestEvent") |
| kernel.controller | `KernelEvents::CONTROLLER` | [ControllerEvent](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Event/ControllerEvent.php "Symfony\Component\HttpKernel\Event\ControllerEvent") |
| kernel.controller_arguments | `KernelEvents::CONTROLLER_ARGUMENTS` | [ControllerArgumentsEvent](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Event/ControllerArgumentsEvent.php "Symfony\Component\HttpKernel\Event\ControllerArgumentsEvent") |
| kernel.view | `KernelEvents::VIEW` | [ViewEvent](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Event/ViewEvent.php "Symfony\Component\HttpKernel\Event\ViewEvent") |
| kernel.response | `KernelEvents::RESPONSE` | [ResponseEvent](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Event/ResponseEvent.php "Symfony\Component\HttpKernel\Event\ResponseEvent") |
| kernel.finish_request | `KernelEvents::FINISH_REQUEST` | [FinishRequestEvent](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Event/FinishRequestEvent.php "Symfony\Component\HttpKernel\Event\FinishRequestEvent") |
| kernel.terminate | `KernelEvents::TERMINATE` | [TerminateEvent](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Event/TerminateEvent.php "Symfony\Component\HttpKernel\Event\TerminateEvent") |
| kernel.exception | `KernelEvents::EXCEPTION` | [ExceptionEvent](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Event/ExceptionEvent.php "Symfony\Component\HttpKernel\Event\ExceptionEvent") |

[A full Working Example](https://symfony.com/doc/8.0/components/http_kernel.html#a-full-working-example "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------------------

When using the HttpKernel component, you're free to attach any listeners to the core events, use any controller resolver that implements the [ControllerResolverInterface](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Controller/ControllerResolverInterface.php "Symfony\Component\HttpKernel\Controller\ControllerResolverInterface") and use any argument resolver that implements the [ArgumentResolverInterface](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Controller/ArgumentResolverInterface.php "Symfony\Component\HttpKernel\Controller\ArgumentResolverInterface"). However, the HttpKernel component comes with some built-in listeners and everything else that can be used to create a working example:

[Sub Requests](https://symfony.com/doc/8.0/components/http_kernel.html#sub-requests "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------

In addition to the "main" request that's sent into `HttpKernel::handle()`, you can also send a so-called "sub request". A sub request looks and acts like any other request, but typically serves to render just one small portion of a page instead of a full page. You'll most commonly make sub-requests from your controller (or perhaps from inside a template, that's being rendered by your controller).

To execute a sub request, use `HttpKernel::handle()`, but change the second argument as follows:

This creates another full request-response cycle where this new `Request` is transformed into a `Response`. The only difference internally is that some listeners (e.g. security) may only act upon the main request. Each listener is passed some subclass of [KernelEvent](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Event/KernelEvent.php "Symfony\Component\HttpKernel\Event\KernelEvent"), whose [isMainRequest()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Event/KernelEvent.php#:~:text=function%20isMainRequest "Symfony\Component\HttpKernel\Event\KernelEvent::isMainRequest()") method can be used to check if the current request is a "main" or "sub" request.

For example, a listener that only needs to act on the main request may look like this:

Note

The default value of the `_format` request attribute is `html`. If your sub request returns a different format (e.g. `json`) you can set it by defining the `_format` attribute explicitly on the request:

[Locating Resources](https://symfony.com/doc/8.0/components/http_kernel.html#locating-resources "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------

The HttpKernel component is responsible of the bundle mechanism used in Symfony applications. One of the key features of the bundles is that you can use logic paths instead of physical paths to refer to any of their resources (config files, templates, controllers, translation files, etc.)

This allows you to import resources even if you don't know where in the filesystem a bundle will be installed. For example, the `services.xml` file stored in the `Resources/config/` directory of a bundle called FooBundle can be referenced as `@FooBundle/Resources/config/services.xml` instead of `__DIR__/Resources/config/services.xml`.

This is possible thanks to the [locateResource()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpKernel/Kernel.php#:~:text=function%20locateResource "Symfony\Component\HttpKernel\Kernel::locateResource()") method provided by the kernel, which transforms logical paths into physical paths:

This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.

# Source: https://symfony.com/doc/8.0/service_container.html

Title: Service Container (Symfony Docs)

URL Source: https://symfony.com/doc/8.0/service_container.html

Markdown Content:
Your application is _full_ of useful objects: a "Mailer" object might help you send emails while another object might help you save things to the database. Almost _everything_ that your app "does" is actually done by one of these objects. And each time you install a new bundle, you get access to even more!

In Symfony, these useful objects are called **services** and each service lives inside a very special object called the **service container**. The container allows you to centralize the way objects are constructed. It makes your life easier, promotes a strong architecture and is super fast!

[Fetching and using Services](https://symfony.com/doc/8.0/service_container.html#fetching-and-using-services "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------

The moment you start a Symfony app, your container _already_ contains many services. These are like _tools_: waiting for you to take advantage of them. In your controller, you can "ask" for a service from the container by type-hinting an argument with the service's class or interface name. Want to [log](https://symfony.com/doc/current/logging.html) something? No problem:

What other services are available? Find out by running:

When you use these type-hints in your controller methods or inside your [own services](https://symfony.com/doc/current/service_container.html#service-container-creating-service), Symfony will automatically pass you the service object matching that type.

Throughout the docs, you'll see how to use the many different services that live in the container.

[Creating/Configuring Services in the Container](https://symfony.com/doc/8.0/service_container.html#creating-configuring-services-in-the-container "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can also organize your _own_ code into services. For example, suppose you need to show your users a random, happy message. If you put this code in your controller, it can't be re-used. Instead, you decide to create a new class:

Congratulations! You've created your first service class! You can use it immediately inside your controller:

When you ask for the `MessageGenerator` service, the container constructs a new `MessageGenerator` object and returns it (see sidebar below). But if you never ask for the service, it's _never_ constructed: saving memory and speed. As a bonus, the `MessageGenerator` service is only created _once_: the same instance is returned each time you ask for it.

### [Limiting Services to a specific Symfony Environment](https://symfony.com/doc/8.0/service_container.html#limiting-services-to-a-specific-symfony-environment "Permalink to this headline")

You can limit service registration to specific environments as follows:

Warning

The `_defaults` section applies only to services defined in the same `services` block. Each `when@<env>` block has its own scope and does not inherit `_defaults` from the main `services` section. Redefine `_defaults` in every `when@<env>` block where you need it:

If you want to exclude a service from being registered in a specific environment, you can use the `#[WhenNot]` attribute:

[Injecting Services/Config into a Service](https://symfony.com/doc/8.0/service_container.html#injecting-services-config-into-a-service "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

What if you need to access the `logger` service from within `MessageGenerator`? No problem! Create a `__construct()` method with a `$logger` argument that has the `LoggerInterface` type-hint. Set this on a new `$logger` property and use it later:

That's it! The container will _automatically_ know to pass the `logger` service when instantiating the `MessageGenerator`. How does it know to do this? [Autowiring](https://symfony.com/doc/current/service_container.html#services-autowire). The key is the `LoggerInterface` type-hint in your `__construct()` method and the `autowire: true` config in `services.yaml`. When you type-hint an argument, the container will automatically find the matching service. If it can't, you'll see a clear exception with a helpful suggestion.

By the way, this method of adding dependencies to your `__construct()` method is called _dependency injection_.

How should you know to use `LoggerInterface` for the type-hint? You can either read the docs for whatever feature you're using, or get a list of autowireable type-hints by running:

In addition to injecting services, you can also pass scalar values and collections as arguments of other services:

### [Handling Multiple Services](https://symfony.com/doc/8.0/service_container.html#handling-multiple-services "Permalink to this headline")

Suppose you also want to email a site administrator each time a site update is made. To do that, you create a new class:

This needs the `MessageGenerator`_and_ the `Mailer` service. That's no problem, we ask them by type hinting their class and interface names! Now, this new service is ready to be used. In a controller, for example, you can type-hint the new `SiteUpdateManager` class and use it:

Thanks to autowiring and your type-hints in `__construct()`, the container creates the `SiteUpdateManager` object and passes it the correct argument. In most cases, this works perfectly.

### [Manually Wiring Arguments](https://symfony.com/doc/8.0/service_container.html#manually-wiring-arguments "Permalink to this headline")

But there are a few cases when an argument to a service cannot be autowired. For example, suppose you want to make the admin email configurable:

If you make this change and refresh, you'll see an error:

> Cannot autowire service "App\Service\SiteUpdateManager": argument "$adminEmail" of method "__construct()" must have a type-hint or be given a value explicitly.

That makes sense! There is no way that the container knows what value you want to pass here. No problem! In your configuration, you can explicitly set this argument:

Thanks to this, the container will pass `manager@example.com` to the `$adminEmail` argument of `__construct` when creating the `SiteUpdateManager` service. The other arguments will still be autowired.

But, isn't this fragile? Fortunately, no! If you rename the `$adminEmail` argument to something else - e.g. `$mainEmail` - you will get a clear exception when you reload the next page (even if that page doesn't use this service).

[Service Parameters](https://symfony.com/doc/8.0/service_container.html#service-parameters "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------

In addition to holding service objects, the container also holds configuration, called **parameters**. The main article about Symfony configuration explains the [configuration parameters](https://symfony.com/doc/current/configuration.html#configuration-parameters) in detail and shows all their types (string, boolean, array, binary and PHP constant parameters).

However, there is another type of parameter related to services. In YAML config, any string which starts with `@` is considered as the ID of a service, instead of a regular string. In PHP config use the `service()` function:

Working with container parameters is straightforward using the container's accessor methods for parameters:

Warning

The used `.` notation is a [Symfony convention](https://symfony.com/doc/current/contributing/code/standards.html#service-naming-conventions) to make parameters easier to read. Parameters are flat key-value elements, they can't be organized into a nested array

Note

You can only set a parameter before the container is compiled, not at run-time. To learn more about compiling the container see [Compiling the Container](https://symfony.com/doc/current/components/dependency_injection/compilation.html).

[Choose a Specific Service](https://symfony.com/doc/8.0/service_container.html#choose-a-specific-service "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------

The `MessageGenerator` service created earlier requires a `LoggerInterface` argument:

However, there are _multiple_ services in the container that implement `LoggerInterface`, such as `logger`, `monolog.logger.request`, `monolog.logger.php`, etc. How does the container know which one to use?

In these situations, the container is usually configured to automatically choose one of the services - `logger` in this case (read more about why in [Defining Services Dependencies Automatically (Autowiring)](https://symfony.com/doc/current/service_container/autowiring.html#service-autowiring-alias)). But, you can control this and pass in a different logger:

This tells the container that the `$logger` argument to `__construct` should use service whose id is `monolog.logger.request`.

For a list of possible logger services that can be used with autowiring, run:

For a full list of _all_ possible services in the container, run:

[Remove Services](https://symfony.com/doc/8.0/service_container.html#remove-services "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------

A service can be removed from the service container if needed. This is useful for example to make a service unavailable in some [configuration environment](https://symfony.com/doc/current/configuration.html#configuration-environments) (e.g. in the `test` environment):

Now, the container will not contain the `App\RemovedService` in the `test` environment.

[Injecting a Closure as an Argument](https://symfony.com/doc/8.0/service_container.html#injecting-a-closure-as-an-argument "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------------------

It is possible to inject a callable as an argument of a service. Let's add an argument to our `MessageGenerator` constructor:

Now, we would add a new invokable service to generate the message hash:

Our configuration looks like this:

[Binding Arguments by Name or Type](https://symfony.com/doc/8.0/service_container.html#binding-arguments-by-name-or-type "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------------------

You can also use the `bind` keyword to bind specific arguments by name or type:

By putting the `bind` key under `_defaults`, you can specify the value of _any_ argument for _any_ service defined in this file! You can bind arguments by name (e.g. `$adminEmail`), by type (e.g. `Psr\Log\LoggerInterface`) or both (e.g. `Psr\Log\LoggerInterface $requestLogger`).

The `bind` config can also be applied to specific services or when [loading many services at once](https://symfony.com/doc/current/service_container.html#service-psr4-loader)).

[Abstract Service Arguments](https://symfony.com/doc/8.0/service_container.html#abstract-service-arguments "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------------------

Sometimes, the values of some service arguments can't be defined in the configuration files because they are calculated at runtime using a [compiler pass](https://symfony.com/doc/current/service_container/compiler_passes.html) or [bundle extension](https://symfony.com/doc/current/bundles/extension.html).

In those cases, you can use the `abstract` argument type to define at least the name of the argument and some short description about its purpose:

If you don't replace the value of an abstract argument during runtime, a `RuntimeException` will be thrown with a message like `Argument "$rootNamespace" of service "App\Service\MyService" is abstract: should be defined by Pass.`

[The autowire Option](https://symfony.com/doc/8.0/service_container.html#the-autowire-option "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------

Above, the `services.yaml` file has `autowire: true` in the `_defaults` section so that it applies to all services defined in that file. With this setting, you're able to type-hint arguments in the `__construct()` method of your services and the container will automatically pass you the correct arguments. This entire entry has been written around autowiring.

For more details about autowiring, check out [Defining Services Dependencies Automatically (Autowiring)](https://symfony.com/doc/current/service_container/autowiring.html).

[The autoconfigure Option](https://symfony.com/doc/8.0/service_container.html#the-autoconfigure-option "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------

Above, the `services.yaml` file has `autoconfigure: true` in the `_defaults` section so that it applies to all services defined in that file. With this setting, the container will automatically apply certain configuration to your services, based on your service's _class_. This is mostly used to _auto-tag_ your services.

For example, to create a Twig extension, you need to create a class, register it as a service, and [tag](https://symfony.com/doc/current/service_container/tags.html) it with `twig.extension`.

But, with `autoconfigure: true`, you don't need the tag. In fact, if you're using the [default services.yaml config](https://symfony.com/doc/current/service_container.html#service-container-services-load-example), you don't need to do _anything_: the service will be automatically loaded. Then, `autoconfigure` will add the `twig.extension` tag _for_ you, because your class implements `Twig\Extension\ExtensionInterface`. And thanks to `autowire`, you can even add constructor arguments without any configuration.

Autoconfiguration also works with attributes. Some attributes like [AsMessageHandler](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Messenger/Attribute/AsMessageHandler.php "Symfony\Component\Messenger\Attribute\AsMessageHandler"), [AsEventListener](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/EventDispatcher/Attribute/AsEventListener.php "Symfony\Component\EventDispatcher\Attribute\AsEventListener") and [AsCommand](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Console/Attribute/AsCommand.php "Symfony\Component\Console\Attribute\AsCommand") are registered for autoconfiguration. Any class using these attributes will have tags applied to them.

[Linting Service Definitions](https://symfony.com/doc/8.0/service_container.html#linting-service-definitions "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------

The `lint:container` command performs additional checks to ensure the container is properly configured. It is useful to run this command before deploying your application to production (e.g. in your continuous integration server):

Performing those checks whenever the container is compiled can hurt performance. That's why they are implemented in [compiler passes](https://symfony.com/doc/current/service_container/compiler_passes.html) called `CheckTypeDeclarationsPass` and `CheckAliasValidityPass`, which are disabled by default and enabled only when executing the `lint:container` command. If you don't mind the performance loss, you can enable these compiler passes in your application.

[Public Versus Private Services](https://symfony.com/doc/8.0/service_container.html#public-versus-private-services "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------------

Every service defined is private by default. When a service is private, you cannot access it directly from the container using `$container->get()`. As a best practice, you should only create _private_ services and you should fetch services using dependency injection instead of using `$container->get()`.

If you need to fetch services lazily, instead of using public services you should consider using a [service locator](https://symfony.com/doc/current/service_container/service_subscribers_locators.html#service-locators).

But, if you _do_ need to make a service public, override the `public` setting:

It is also possible to define a service as public thanks to the `#[Autoconfigure]` attribute. This attribute must be used directly on the class of the service you want to configure:

[Importing Many Services at once with resource](https://symfony.com/doc/8.0/service_container.html#importing-many-services-at-once-with-resource "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You've already seen that you can import many services at once by using the `resource` key. For example, the default Symfony configuration contains this:

Tip

The value of the `resource` and `exclude` options can be any valid [glob pattern](https://en.wikipedia.org/wiki/Glob_(programming)). If you want to exclude only a few services, you may use the [Exclude](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/DependencyInjection/Attribute/Exclude.php "Symfony\Component\DependencyInjection\Attribute\Exclude") attribute directly on your class to exclude it:

This can be used to quickly make many classes available as services and apply some default configuration. The `id` of each service is its fully-qualified class name. You can override any service that's imported by using its id (class name) below (e.g. see [how to manually wire arguments](https://symfony.com/doc/current/service_container.html#services-manually-wire-args)). If you override a service, none of the options (e.g. `public`) are inherited from the import (but the overridden service _does_ still inherit from `_defaults`).

You can also `exclude` certain paths. This is optional, but will slightly increase performance in the `dev` environment: excluded paths are not tracked and so modifying them will not cause the container to be rebuilt.

Note

Wait, does this mean that _every_ class in `src/` is registered as a service? Even model classes? Actually, no. As long as you keep your imported services as [private](https://symfony.com/doc/current/service_container.html#container-public), all classes in `src/` that are _not_ explicitly used as services are automatically removed from the final container. In reality, the import means that all classes are "available to be _used_ as services" without needing to be manually configured.

### [Multiple Service Definitions Using the Same Namespace](https://symfony.com/doc/8.0/service_container.html#multiple-service-definitions-using-the-same-namespace "Permalink to this headline")

If you define services using the YAML config format, the PHP namespace is used as the key of each configuration, so you can't define different service configs for classes under the same namespace.

In order to have multiple definitions, add the `namespace` option and use any unique string as the key of each service config:

[Explicitly Configuring Services and Arguments](https://symfony.com/doc/8.0/service_container.html#explicitly-configuring-services-and-arguments "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Loading services automatically](https://symfony.com/doc/current/service_container.html#service-container-services-load-example) and [autowiring](https://symfony.com/doc/current/service_container.html#services-autowire) are optional. And even if you use them, there may be some cases where you want to manually wire a service. For example, suppose that you want to register _2_ services for the `SiteUpdateManager` class - each with a different admin email. In this case, each needs to have a unique service id:

In this case, _two_ services are registered: `site_update_manager.superadmin` and `site_update_manager.normal_users`. Thanks to the alias, if you type-hint `SiteUpdateManager` the first (`site_update_manager.superadmin`) will be passed.

If you want to pass the second, you'll need to [manually wire the service](https://symfony.com/doc/current/service_container.html#services-wire-specific-service) or to create a named [autowiring alias](https://symfony.com/doc/current/service_container/autowiring.html#autowiring-alias).

Warning

If you do _not_ create the alias and are [loading all services from src/](https://symfony.com/doc/current/service_container.html#service-container-services-load-example), then _three_ services have been created (the automatic service + your two services) and the automatically loaded service will be passed - by default - when you type-hint `SiteUpdateManager`. That's why creating the alias is a good idea.

When using PHP closures to configure your services, it is possible to automatically inject the current environment value by adding a string argument named `$env` to the closure:

[Generating Adapters for Functional Interfaces](https://symfony.com/doc/8.0/service_container.html#generating-adapters-for-functional-interfaces "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Functional interfaces are interfaces with a single method. They are conceptually very similar to a closure except that their only method has a name. Moreover, they can be used as type-hints across your code.

The [AutowireCallable](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/DependencyInjection/Attribute/AutowireCallable.php "Symfony\Component\DependencyInjection\Attribute\AutowireCallable") attribute can be used to generate an adapter for a functional interface. Let's say you have the following functional interface:

You also have a service that defines many methods and one of them is the same `format()` method of the previous interface:

Thanks to the `#[AutowireCallable]` attribute, you can now inject this `MessageUtils` service as a functional interface implementation:

Instead of using the `#[AutowireCallable]` attribute, you can also generate an adapter for a functional interface through configuration:

By doing so, Symfony will generate a class (also called an _adapter_) implementing `MessageFormatterInterface` that will forward calls of `MessageFormatterInterface::format()` to your underlying service's method `MessageUtils::format()`, with all its arguments.

[Learn more](https://symfony.com/doc/8.0/service_container.html#learn-more "Permalink to this headline")
--------------------------------------------------------------------------------------------------------

* [How to Create Service Aliases and Mark Services as Public](https://symfony.com/doc/current/service_container/alias_private.html)
* [Defining Services Dependencies Automatically (Autowiring)](https://symfony.com/doc/current/service_container/autowiring.html)
* [Service Method Calls and Setter Injection](https://symfony.com/doc/current/service_container/calls.html)
* [How to Work with Compiler Passes](https://symfony.com/doc/current/service_container/compiler_passes.html)
* [How to Configure a Service with a Configurator](https://symfony.com/doc/current/service_container/configurators.html)
* [How to Debug the Service Container & List Services](https://symfony.com/doc/current/service_container/debug.html)
* [How to work with Service Definition Objects](https://symfony.com/doc/current/service_container/definitions.html)
* [How to Inject Values Based on Complex Expressions](https://symfony.com/doc/current/service_container/expression_language.html)
* [Using a Factory to Create Services](https://symfony.com/doc/current/service_container/factories.html)
* [How to Import Configuration Files/Resources](https://symfony.com/doc/current/service_container/import.html)
* [Types of Injection](https://symfony.com/doc/current/service_container/injection_types.html)
* [Lazy Services](https://symfony.com/doc/current/service_container/lazy_services.html)
* [How to Make Service Arguments/References Optional](https://symfony.com/doc/current/service_container/optional_dependencies.html)
* [How to Manage Common Dependencies with Parent Services](https://symfony.com/doc/current/service_container/parent_services.html)
* [How to Retrieve the Request from the Service Container](https://symfony.com/doc/current/service_container/request.html)
* [Service Closures](https://symfony.com/doc/current/service_container/service_closures.html)
* [How to Decorate Services](https://symfony.com/doc/current/service_container/service_decoration.html)
* [Service Subscribers & Locators](https://symfony.com/doc/current/service_container/service_subscribers_locators.html)
* [How to Define Non Shared Services](https://symfony.com/doc/current/service_container/shared.html)
* [How to Inject Instances into the Container](https://symfony.com/doc/current/service_container/synthetic_services.html)
* [How to Work with Service Tags](https://symfony.com/doc/current/service_container/tags.html)

This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.

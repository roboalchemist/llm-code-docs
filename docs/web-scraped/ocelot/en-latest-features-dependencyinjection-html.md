# Source: https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html

Title: Dependency Injection — Ocelot Gateway 24.1 "Globality" documentation

URL Source: https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html

Markdown Content:
> Namespace: `Ocelot.DependencyInjection`

Services Overview[¶](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#services-overview "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------

_Dependency Injection_ feature in Ocelot is designed to extend and/or control the building of Ocelot Core as ASP.NET Core pipeline services. The main methods of the [ServiceCollectionExtensions](https://github.com/ThreeMammals/Ocelot/blob/main/src/Ocelot/DependencyInjection/ServiceCollectionExtensions.cs) class are:

*   The [AddOcelot method](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#di-services-addocelot-method) adds the required Ocelot services to the DI container and adds default services using the [AddDefaultAspNetServices method](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#di-adddefaultaspnetservices-method).

*   The [AddOcelotUsingBuilder method](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#di-addocelotusingbuilder-method) adds the required Ocelot services to the DI container and adds custom ASP.NET services with configuration injected implicitly or explicitly.

Use [IServiceCollection extensions](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#di-iservicecollection-extensions) in your [Program](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/Program.cs) (ASP.NET Core app) to add and build Ocelot Core services. The fact is, the [OcelotBuilder class](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#di-ocelotbuilder-class) is Ocelot’s cornerstone logic.

`IServiceCollection` extensions[¶](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#iservicecollection-extensions "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Based on the current implementations for the [OcelotBuilder class](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#di-ocelotbuilder-class), the [AddOcelot method](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#di-services-addocelot-method) adds the required ASP.NET services to the DI container. You could call the more extended [AddOcelotUsingBuilder method](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#di-addocelotusingbuilder-method) while configuring services to build and use a custom builder via an `IMvcCoreBuilder` object.

### `AddOcelot` method[¶](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#addocelot-method "Link to this heading")

**Signatures**:

IOcelotBuilder AddOcelot(this IServiceCollection services);
IOcelotBuilder AddOcelot(this IServiceCollection services, IConfiguration configuration);

These `IServiceCollection` extension methods add default ASP.NET services and Ocelot application services with configuration injected implicitly or explicitly.

> **Note**: Both methods add the required and _default_ ASP.NET Core services for Ocelot Core in the [AddDefaultAspNetServices method](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#di-adddefaultaspnetservices-method), which is the default builder.

In this scenario, you do nothing other than call the `AddOcelot` method, which is often mentioned in feature chapters if additional startup settings are required. With this method, you simply reuse the default settings to build the Ocelot Core. The alternative is the `AddOcelotUsingBuilder` method; see the next subsection.

### `AddOcelotUsingBuilder` method[¶](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#addocelotusingbuilder-method "Link to this heading")

**Signatures**:

using CustomBuilderFunc = System.Func<IMvcCoreBuilder, Assembly, IMvcCoreBuilder>;

IOcelotBuilder AddOcelotUsingBuilder(this IServiceCollection services, CustomBuilderFunc customBuilder);
IOcelotBuilder AddOcelotUsingBuilder(this IServiceCollection services, IConfiguration configuration, CustomBuilderFunc customBuilder);

These `IServiceCollection` extension methods add Ocelot application services and **custom** ASP.NET Core services with configuration injected implicitly or explicitly.

> **Note**: The method adds **custom** ASP.NET Core services required for Ocelot Core using a custom builder (aka `customBuilder` parameter). It is highly recommended to read the documentation of the [AddDefaultAspNetServices method](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#di-adddefaultaspnetservices-method), or even review the implementation to understand the default ASP.NET Core services which are the minimal part of the gateway pipeline.

In this custom scenario, you control everything during the ASP.NET Core build process, and you provide custom settings to build Ocelot Core.

`OcelotBuilder` class[¶](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#ocelotbuilder-class "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------

The [OcelotBuilder](https://github.com/ThreeMammals/Ocelot/blob/main/src/Ocelot/DependencyInjection/OcelotBuilder.cs) class is the core of Ocelot which does the following:

*   Contructs itself by single public constructor:

public OcelotBuilder(IServiceCollection services, IConfiguration configurationRoot, Func<IMvcCoreBuilder, Assembly, IMvcCoreBuilder> customBuilder = null); 
*   Initializes and stores public properties: `Services` (of `IServiceCollection` type), `Configuration` (of `IConfiguration` type), and `MvcCoreBuilder` (of `IMvcCoreBuilder` type).

*   Adds _all application services_ during the construction phase via the `Services` property.

*   Adds ASP.NET Core services by builder using `Func<IMvcCoreBuilder, Assembly, IMvcCoreBuilder>` object in these 2 development scenarios:

*   Adds ASP.NET Core services by builder using a `Func<IMvcCoreBuilder, Assembly, IMvcCoreBuilder>` object in these two development scenarios:

> 1.   By default builder ([AddDefaultAspNetServices method](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#di-adddefaultaspnetservices-method)) if there is no `customBuilder` parameter provided.
> 
>     2.   By [Custom Builder](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#di-custom-builder) with the provided delegate object as the `customBuilder` parameter.

*   Adds (switches on/off) Ocelot features through the following methods:

    *   `AddSingletonDefinedAggregator` and `AddTransientDefinedAggregator` methods

    *   `AddCustomLoadBalancer` method

    *   `AddDelegatingHandler` method

    *   `AddConfigPlaceholders` method

### `AddDefaultAspNetServices` method[¶](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#adddefaultaspnetservices-method "Link to this heading")

> Part of the [OcelotBuilder class](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#di-ocelotbuilder-class)

Currently, the method is protected, and overriding is forbidden. The role of the method is to inject the required services via both the `IServiceCollection` and `IMvcCoreBuilder` interface objects for the minimal part of the gateway pipeline.

Current [implementation](https://github.com/search?q=repo%3AThreeMammals%2FOcelot+AddDefaultAspNetServices+language%3AC%23&type=code&l=C%23) is the folowing:

protected IMvcCoreBuilder AddDefaultAspNetServices(IMvcCoreBuilder builder, Assembly assembly)
{
 Services
 .AddLogging()
 .AddMiddlewareAnalysis()
 .AddWebEncoders();
 return builder
 .AddApplicationPart(assembly)
 .AddControllersAsServices()
 .AddAuthorization()
 .AddNewtonsoftJson();
}

The method cannot be overridden. It is not virtual, and there is no way to override the current behavior by inheritance. The method is the default builder of Ocelot Core when calling the [AddOcelot method](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#di-services-addocelot-method). As an alternative, to “override” this default builder, you can design and reuse a custom builder as a `Func<IMvcCoreBuilder, Assembly, IMvcCoreBuilder>` delegate object and pass it as a parameter to the [AddOcelotUsingBuilder method](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#di-addocelotusingbuilder-method). It gives you full control over the design and building of Ocelot Core, but be careful when designing your custom Ocelot pipeline as a customizable ASP.NET Core pipeline.

> **Warning**: Most of the services from the minimal part of the pipeline should be reused, but only a few services can be removed.
> 
> 
> **Warning**: The method above is called after adding the required services of the ASP.NET Core pipeline by the [AddMvcCore](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.mvccoreservicecollectionextensions.addmvccore) method via the `Services` property in the upper calling context. These services are the absolute minimum core services for the ASP.NET MVC pipeline. They must always be added to the DI container and are added implicitly before calling the method by the caller in the upper context. So, `AddMvcCore` creates an `IMvcCoreBuilder` object and assigns it to the `MvcCoreBuilder` property. Finally, as a default builder, the method above receives the `IMvcCoreBuilder` object, making it ready for further extensions.

The next section shows you an example of designing a custom Ocelot Core using a custom builder.

Custom Builder[¶](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#custom-builder "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------

**Goal**: Replace `Newtonsoft.Json` services with `System.Text.Json` services.

### Problem[¶](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#problem "Link to this heading")

The main [AddOcelot method](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#di-services-addocelot-method) adds [Newtonsoft JSON](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.newtonsoftjsonmvccorebuilderextensions.addnewtonsoftjson) services using the `AddNewtonsoftJson` extension method in the default builder ([AddDefaultAspNetServices method](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#di-adddefaultaspnetservices-method)). The `AddNewtonsoftJson` method was introduced in earlier .NET and Ocelot releases, which was necessary before Microsoft launched the `System.Text.Json` library. However, it now affects normal use, so we intend to solve the problem.

Modern [JSON services](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.mvccoremvccorebuilderextensions.addjsonoptions) out of [the box](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.mvccoremvccorebuilderextensions) will help configure JSON settings using the `JsonSerializerOptions` property for JSON formatters during (de)serialization.

### Solution[¶](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#solution "Link to this heading")

We have the following methods in [ServiceCollectionExtensions](https://github.com/ThreeMammals/Ocelot/blob/main/src/Ocelot/DependencyInjection/ServiceCollectionExtensions.cs) class:

IOcelotBuilder AddOcelotUsingBuilder(this IServiceCollection services, Func<IMvcCoreBuilder, Assembly, IMvcCoreBuilder> customBuilder);
IOcelotBuilder AddOcelotUsingBuilder(this IServiceCollection services, IConfiguration configuration, Func<IMvcCoreBuilder, Assembly, IMvcCoreBuilder> customBuilder);

These methods with a custom builder allow you to use any desired JSON library for (de)serialization. However, we are going to create a custom `MvcCoreBuilder` with support for JSON services, such as `System.Text.Json`. To do that, we need to call the `AddJsonOptions` extension of the `MvcCoreMvcCoreBuilderExtensions` class (NuGet [Microsoft.AspNetCore.Mvc.Core](https://www.nuget.org/packages/Microsoft.AspNetCore.Mvc.Core/) package) in [Program](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/Program.cs):

 builder.Services
 .AddLogging()
 .AddMiddlewareAnalysis()
 .AddWebEncoders()
 // Add your custom builder
 .AddOcelotUsingBuilder(builder.Configuration, MyCustomBuilder);
 static IMvcCoreBuilder MyCustomBuilder(IMvcCoreBuilder builder, Assembly assembly) => builder
 .AddApplicationPart(assembly)
 .AddControllersAsServices()
 .AddAuthorization()
 // Replace AddNewtonsoftJson() by AddJsonOptions()
 .AddJsonOptions(options =>
 {
 options.JsonSerializerOptions.WriteIndented = true; // use System.Text.Json
 });

The sample code provides settings to render JSON as indented text rather than as compressed plain JSON text without spaces. This is just one common use case, and you can add additional services to the builder.

* * *

Configuration Overview[¶](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#configuration-overview "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------

_Dependency Injection_ for the [Configuration](https://ocelot.readthedocs.io/en/latest/features/configuration.html) feature in Ocelot is designed to extend and set up the configuration of the Ocelot Core **before** the stage of building ASP.NET Core services (see [Services Overview](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#di-services-overview)). To configure the Ocelot Core services, use the [IConfigurationBuilder extensions](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#di-configuration-extensions) in your [Program](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/Program.cs) of your gateway app.

`IConfigurationBuilder` extensions[¶](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#iconfigurationbuilder-extensions "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The main methods are the [AddOcelot methods](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#di-configuration-addocelot-methods) within the [ConfigurationBuilderExtensions](https://github.com/ThreeMammals/Ocelot/blob/main/src/Ocelot/DependencyInjection/ConfigurationBuilderExtensions.cs) class. These methods have a list of overloaded versions with corresponding signatures.

The purpose of the `AddOcelot` method is to prepare everything before actually configuring with native extensions. It involves the following steps:

1.   **Merging Partial JSON Files**: The `GetMergedOcelotJson` method merges partial JSON files.

2.   **Selecting Merge Type**: It allows you to choose a merge type to save the merged JSON configuration data either `ToFile` or `ToMemory`.

3.   **Framework Extensions**: Finally, the method calls the following native `IConfigurationBuilder` framework extensions:

> *   The `AddJsonFile` method adds the primary configuration file (commonly known as [ocelot.json](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/ocelot.json)) after the merge stage. It writes the file back _to the file system_ using the `ToFile` merge type option, which is implicitly the default.
> 
> *   The `AddJsonStream` method adds the JSON data of the primary configuration file as a UTF-8 stream _into memory_ after the merge stage. It uses the `ToMemory` merge type option.

### `AddOcelot` methods[¶](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#addocelot-methods "Link to this heading")

**Signatures** of the most common versions:

IConfigurationBuilder AddOcelot(this IConfigurationBuilder builder, IWebHostEnvironment env);
IConfigurationBuilder AddOcelot(this IConfigurationBuilder builder, string folder, IWebHostEnvironment env);

> **Note**: These versions use the implicit `ToFile` merge type to write [ocelot.json](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/ocelot.json) back to disk. Finally, they call the `AddJsonFile` extension.

**Signatures** of the versions to specify a `MergeOcelotJson` option:

IConfigurationBuilder AddOcelot(this IConfigurationBuilder builder, IWebHostEnvironment env, MergeOcelotJson mergeTo,
 string primaryConfigFile = null, string globalConfigFile = null, string environmentConfigFile = null, bool? optional = null, bool? reloadOnChange = null);
IConfigurationBuilder AddOcelot(this IConfigurationBuilder builder, string folder, IWebHostEnvironment env, MergeOcelotJson mergeTo,
 string primaryConfigFile = null, string globalConfigFile = null, string environmentConfigFile = null, bool? optional = null, bool? reloadOnChange = null);

> **Note**: These versions include optional arguments to specify the location of the three main files involved in the merge operation. In theory, these files can be located anywhere, but in practice, it is better to keep them in one folder.

**Signatures** of the versions to indicate the `FileConfiguration` object of a self-created out-of-the-box configuration: [[1]](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#f1)

IConfigurationBuilder AddOcelot(this IConfigurationBuilder builder, FileConfiguration fileConfiguration,
 string primaryConfigFile = null, bool? optional = null, bool? reloadOnChange = null);
IConfigurationBuilder AddOcelot(this IConfigurationBuilder builder, FileConfiguration fileConfiguration, IWebHostEnvironment env, MergeOcelotJson mergeTo,
 string primaryConfigFile = null, string globalConfigFile = null, string environmentConfigFile = null, bool? optional = null, bool? reloadOnChange = null);

> **Note 1**: These versions include optional arguments to specify the location of the three main files involved in the merge operation.
> 
> 
> **Note 2**: Your `FileConfiguration` object can be serialized/deserialized from anywhere: local or remote storage, Consul KV storage, and even a database. For more information about this super useful feature, please read PR [1569](https://github.com/ThreeMammals/Ocelot/pull/1569).

* * *

# Source: https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-11-to-12

Title: Migrate Hot Chocolate from 11 to 12 - Hot Chocolate v14

URL Source: https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-11-to-12

Markdown Content:
This guide will walk you through the manual migration steps to get your Hot Chocolate GraphQL server to version 12.

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-11-to-12#resolvers)Resolvers
----------------------------------------------------------------------------------------------------

We have reworked the resolver compiler and are now demanding that the `ParentAttribute` is used when an argument is referring to the parent object. This is done since in some cases people want to get the parent object which is the same runtime type as an argument value.

**v11**

C#

public string MyResolver(Person parent, string additionalInput)

{

}

**v12**

C#

public string MyResolver([Parent] Person parent, string additionalInput)

{

}

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-11-to-12#scalars)Scalars
------------------------------------------------------------------------------------------------

We changed some defaults around scalars. These new defaults can break your existing schema but are, in general, better for newcomers and align better with the overall GraphQL ecosystem. Of course, you can naturally opt out of these new defaults to preserve your current schema's integrity.

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-11-to-12#uuid)UUID
------------------------------------------------------------------------------------------

We changed the name of the UUID scalar from `Uuid` to `UUID`. To maintain the old name, register the type manually like the following:

C#

services

.AddGraphQLServer()

.AddType(() => new UuidType("Uuid"));

Further, we changed the default serialization of UUID values from format `N` (`nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn`) to format `D` (`nnnnnnnn-nnnn-nnnn-nnnn-nnnnnnnnnnnn`). While the format `N` saved a few payload characters, new users, in general, often had issues with that format and some other tooling. New users will now, by default, have a better experience when using non-ChilliCream tooling.

To preserve the old format, you can directly provide the format in the scalar.

C#

services

.AddGraphQLServer()

.AddType(() => new UuidType(defaultFormat: 'N'));

In order to fully preserve version 11 behavior do:

C#

services

.AddGraphQLServer()

.AddType(() => new UuidType("Uuid", defaultFormat: 'N'));

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-11-to-12#url)URL
----------------------------------------------------------------------------------------

We changed the name of the URL scalar from `Url` to `URL`. To maintain the old name, register the type manually like the following:

C#

services

.AddGraphQLServer()

.AddType(() => new UrlType("Url"));

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-11-to-12#connectiontype)ConnectionType
--------------------------------------------------------------------------------------------------------------

In v12 we have removed the `ConnectionType<T>` and `ConnectionType`.

**v11**

C#

descriptor

.Field("users")

.UsePaging()

.Type<ConnectionType<UserType>>()

.Resolver(context =>

{

});

**v12**

C#

descriptor

.Field("users")

.UsePaging<UserType>()

.Resolver(context =>

{

});

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-11-to-12#connection-naming)Connection naming
--------------------------------------------------------------------------------------------------------------------

We have changed the way we infer the name for the connection type when using cursor-based pagination. By default, the connection name is now inferred from the field name instead of the type name.

SDL

type Person {

friends: [Person]

}

In version 11, we would have created a connection named `PersonConnection`.

SDL

type Person {

friends(first: Int, last: Int, after: String, before: String): PersonConnection

}

In version 12, we now will infer the connection name as `FriendsConnection`.

SDL

type Person {

friends(first: Int, last: Int, after: String, before: String): FriendsConnection

}

To keep your schema stable when you migrate, you can switch the behavior back to how you did in version 11.

C#

services

.AddGraphQLServer()

.SetPagingOptions(new PagingOptions{ InferConnectionNameFromField = false })

...

Moreover, you now can explicitly define the connection name per field.

C#

public class Person

{

[UsePaging(ConnectionName = "Persons")]

public IQueryable<Person> GetFriends() => ...

}

[Reference](https://chillicream.com/docs/hotchocolate/v12/fetching-data/pagination#naming)

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-11-to-12#mongodb-paging)MongoDB Paging
--------------------------------------------------------------------------------------------------------------

In version 11 we had the `UseMongoDbPagingAttribute` and the `UseMongoDbOffsetPagingAttribute`, which we removed with version 11. In version 12 you now can use the standard attributes `UsePagingAttribute` and `UseOffsetPagingAttribute`.

To use these attributes with mongo, you need to register the mongo paging provider with your GraphQL configuration:

C#

services

.AddGraphQLServer()

.AddMongoDbPagingProviders()

...

[Reference](https://chillicream.com/docs/hotchocolate/v12/fetching-data/pagination#providers)

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-11-to-12#records)Records
------------------------------------------------------------------------------------------------

With version 11, we added support for records and added the ability to infer attributes from parameters. This, in the end, leads to more errors than benefits. With version 12, we removed this feature. Use the official' property' keyword to write records in C# short-hand syntax when annotating properties.

C#

public record Foo([property: ID] string Id);

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-11-to-12#instrumentation)Instrumentation
----------------------------------------------------------------------------------------------------------------

We added more instrumentation events and generalized more how one can tap into our internal events. The class `DiagnosticEventListener` is now obsolete and replaced with `ExecutionDiagnosticEventListener`. This is due to new event listener classes like `DataLoaderDiagnosticEventListener`. Most virtual methods previously returning IActivityScope now return IDisposable.

[Learn more about instrumentation](https://chillicream.com/docs/hotchocolate/v12/server/instrumentation)

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-11-to-12#relay)Relay
--------------------------------------------------------------------------------------------

Previously the configuration of the Relay integration was focused around the `EnableRelaySupport()` method. It allowed you to enable Global Object Identification and automatically adding a query field to mutation payloads.

The problem is that `EnableRelaySupport()` always enabled the Global Object Identification feature. This is not obviously implied by the name and also prevents you from using the other feature in isolation.

Therefore we introduced two separate APIs to give you more explicit control over which parts of the Relay integration you want to enable.

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-11-to-12#global-object-identification)Global Object Identification
------------------------------------------------------------------------------------------------------------------------------------------

**v11**

C#

services

.AddGraphQLServer()

.EnableRelaySupport();

**v12**

C#

services

.AddGraphQLServer()

.AddGlobalObjectIdentification();

[Learn more about Global Object Identification](https://chillicream.com/docs/hotchocolate/v12/defining-a-schema/relay#global-object-identification)

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-11-to-12#query-field-in-mutation-payloads)Query field in Mutation payloads
--------------------------------------------------------------------------------------------------------------------------------------------------

**v11**

C#

services

.AddGraphQLServer()

.EnableRelaySupport(new RelayOptions

{

AddQueryFieldToMutationPayloads = true,

QueryFieldName = "rootQuery",

MutationPayloadPredicate = type => type.Name.Value.EndsWith("Result")

});

**v12**

C#

services

.AddGraphQL()

.AddQueryFieldToMutationPayloads(options =>

{

options.QueryFieldName = "rootQuery";

options.MutationPayloadPredicate =

type => type.Name.Value.EndsWith("Result");

});

If you just want to enable the feature without further configuration, you can omit the `options =>` action.

Warning

Since `EnableRelaySupport()` previously always implied the usage of Global Object Identification, you might have to enable Global Object Identification separately as well.

[Learn more about Query field in Mutation payloads](https://chillicream.com/docs/hotchocolate/v12/defining-a-schema/relay#query-field-in-mutation-payloads)

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-11-to-12#dataloader)DataLoader
------------------------------------------------------------------------------------------------------

We have consolidated the DataLoader base classes into the GreenDonut package which has no dependency on any HotChocolate packages. This allows for people using DataLoader in their business layer without having to reference GraphQL related packages. In your DataLoader classes the namespace `HotChocolate.Fetching` and `HotChocolate.DataLOader` are no longer needed.

Second, we optimized memory usage of DataLoader and it is now best practice to let the DI inject the DataLoaderOptions into the DataLoader.

**v11**

C#

public class CustomBatchDataLoader : BatchDataLoader<string, string?>

{

public CustomBatchDataLoader(IBatchScheduler batchScheduler)

: base(batchScheduler)

{

}

}

**v12**

C#

public class CustomBatchDataLoader : BatchDataLoader<string, string?>

{

public CustomBatchDataLoader(IBatchScheduler batchScheduler, DataLoaderOptions options)

: base(batchScheduler, options)

{

}

}

Allowing the DI to inject the options will allow the DataLoader to use the new shared pooled cache objects.

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-11-to-12#custom-naming-conventions)Custom naming conventions
------------------------------------------------------------------------------------------------------------------------------------

If you're using a custom naming convention and have xml documentation enabled, you'll need to modify the way the naming convention is hooked up else your comments will disappear from your schema.

**v11**

C#

public class CustomNamingConventions : DefaultNamingConventions

{

public CustomNamingConventions()

: base() { }

}

services

.AddGraphQLServer()

.AddConvention<INamingConventions>(sp => new CustomNamingConventions())

.AddConvention<INamingConventions, CustomNamingConventions>();

**v12**

C#

public class CustomNamingConventions : DefaultNamingConventions

{

public CustomNamingConventions(IDocumentationProvider documentationProvider)

: base(documentationProvider) { }

}

IReadOnlySchemaOptions capturedSchemaOptions;

services

.AddGraphQLServer()

.ModifyOptions(opt => capturedSchemaOptions = opt)

.AddConvention<INamingConventions>(sp => new CustomNamingConventions(

new XmlDocumentationProvider(

new XmlDocumentationFileResolver(

capturedSchemaOptions.ResolveXmlDocumentationFileName),

sp.GetApplicationService<ObjectPool<StringBuilder>>()

?? new NoOpStringBuilderPool())));

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-11-to-12#miscellaneous)Miscellaneous
------------------------------------------------------------------------------------------------------------

*   `IObjectField`
    *   If you were using `IObjectField.Member`, you'll likely want to move to `IObjectField.ResolverMember` (as `.Member` can be `null` in some cases now where it previously wasn't; and `.ResolverMember` will fall back to `.Member`).

Last updated on **2026-02-17** by**Tobias Tengler**

# Source: https://learn.microsoft.com/en-us/ef/core/what-is-new/ef-core-10.0/breaking-changes

Title: Breaking changes in EF Core 10 (EF10) - EF Core

URL Source: https://learn.microsoft.com/en-us/ef/core/what-is-new/ef-core-10.0/breaking-changes

Markdown Content:
This page documents API and behavior changes that have the potential to break existing applications updating from EF Core 9 to EF Core 10. Make sure to review earlier breaking changes if updating from an earlier version of EF Core:

* [Breaking changes in EF Core 9](https://learn.microsoft.com/en-us/ef/core/what-is-new/ef-core-9.0/breaking-changes)
* [Breaking changes in EF Core 8](https://learn.microsoft.com/en-us/ef/core/what-is-new/ef-core-8.0/breaking-changes)
* [Breaking changes in EF Core 7](https://learn.microsoft.com/en-us/ef/core/what-is-new/ef-core-7.0/breaking-changes)
* [Breaking changes in EF Core 6](https://learn.microsoft.com/en-us/ef/core/what-is-new/ef-core-6.0/breaking-changes)

Note

If you are using Microsoft.Data.Sqlite, please see the [separate section below on Microsoft.Data.Sqlite breaking changes](https://learn.microsoft.com/en-us/ef/core/what-is-new/ef-core-10.0/breaking-changes#MDS-breaking-changes).

| **Breaking change** | **Impact** |
| --- | --- |
| [EF tools now require framework to be specified for multi-targeted projects](https://learn.microsoft.com/en-us/ef/core/what-is-new/ef-core-10.0/breaking-changes#ef-tools-multi-targeting) | Medium |
| [Application Name is now injected into the connection string](https://learn.microsoft.com/en-us/ef/core/what-is-new/ef-core-10.0/breaking-changes#sqlserver-application-name) | Low |
| [SQL Server json data type used by default on Azure SQL and compatibility level 170](https://learn.microsoft.com/en-us/ef/core/what-is-new/ef-core-10.0/breaking-changes#sqlserver-json-data-type) | Low |
| [Parameterized collections now use multiple parameters by default](https://learn.microsoft.com/en-us/ef/core/what-is-new/ef-core-10.0/breaking-changes#parameterized-collections) | Low |
| [ExecuteUpdateAsync now accepts a regular, non-expression lambda](https://learn.microsoft.com/en-us/ef/core/what-is-new/ef-core-10.0/breaking-changes#ExecuteUpdateAsync-lambda) | Low |
| [Complex type column names are now uniquified](https://learn.microsoft.com/en-us/ef/core/what-is-new/ef-core-10.0/breaking-changes#complex-type-column-uniquification) | Low |
| [Nested complex type properties use full path in column names](https://learn.microsoft.com/en-us/ef/core/what-is-new/ef-core-10.0/breaking-changes#nested-complex-type-column-names) | Low |
| [IDiscriminatorPropertySetConvention signature changed](https://learn.microsoft.com/en-us/ef/core/what-is-new/ef-core-10.0/breaking-changes#discriminator-convention-signature) | Low |
| [IRelationalCommandDiagnosticsLogger methods add logCommandText parameter](https://learn.microsoft.com/en-us/ef/core/what-is-new/ef-core-10.0/breaking-changes#logger-logcommandtext) | Low |

[Tracking Issue #37230](https://github.com/dotnet/efcore/issues/37230)

Previously, the EF tools (dotnet-ef) could be used on projects targeting multiple frameworks without specifying which framework to use.

Starting with EF Core 10.0, when running EF tools on a project that targets multiple frameworks (using `<TargetFrameworks>` instead of `<TargetFramework>`), you must explicitly specify which target framework to use with the `--framework` option. Without this option, the following error will be thrown:

> The project targets multiple frameworks. Use the --framework option to specify which target framework to use.

In EF Core 10, the tools started relying on the `ResolvePackageAssets` MSBuild task to get more accurate information about project dependencies. However, this task is not available if the project is targeting multiple target frameworks (TFMs). The solution requires users to select which framework should be used.

When running any EF tools command on a project that targets multiple frameworks, specify the target framework using the `--framework` option. For example:

```
dotnet ef migrations add MyMigration --framework net9.0
```

```
dotnet ef database update --framework net9.0
```

```
dotnet ef migrations script --framework net9.0
```

If your project file looks like this:

```
<PropertyGroup>
  <TargetFrameworks>net8.0;net9.0</TargetFrameworks>
</PropertyGroup>
```

You'll need to choose one of the frameworks (e.g., `net9.0`) when running the EF tools.

[Tracking Issue #35730](https://github.com/dotnet/efcore/issues/35730)

When a connection string without an `Application Name` is passed to EF, EF now inserts an `Application Name` containing anonymous information about the EF and SqlClient versions being used. In the vast majority of cases, this doesn't impact the application in any way, but can affect behavior in some edge cases. For example, if you connect to the same database with both EF and another non-EF data access technology (e.g. Dapper, ADO.NET), SqlClient will use a different internal connection pool, as EF will now use a different, updated connection string (one where `Application Name` has been injected). If this sort of mixed access is done within a `TransactionScope`, this can cause escalation to a distributed transaction where previously none was necessary, due of the usage of two connection strings which SqlClient identifies as two distinct databases.

A mitigation is to simply define an `Application Name` in your connection string. Once one is defined, EF does not overwrite it and the original connection string is preserved exactly as-is.

[Tracking Issue #36372](https://github.com/dotnet/efcore/issues/36372)

Previously, when mapping primitive collections or owned types to JSON in the database, the SQL Server provider stored the JSON data in an `nvarchar(max)` column:

```
public class Blog
{
    // ...

    // Primitive collection, mapped to nvarchar(max) JSON column
    public string[] Tags { get; set; }
    // Owned entity type mapped to nvarchar(max) JSON column
    public List<Post> Posts { get; set; }
}

protected override void OnModelCreating(ModelBuilder modelBuilder)
{
    modelBuilder.Entity<Blog>().OwnsMany(b => b.Posts, b => b.ToJson());
}
```

For the above, EF previously generated the following table:

```
CREATE TABLE [Blogs] (
    ...
    [Tags] nvarchar(max),
    [Posts] nvarchar(max)
);
```

With EF 10, if you configure EF with [UseAzureSql](https://learn.microsoft.com/en-us/dotnet/api/microsoft.entityframeworkcore.sqlserverdbcontextoptionsextensions.useazuresql) ([see documentation](https://learn.microsoft.com/en-us/ef/core/providers/sql-server/#usage-and-configuration)), or configure EF with a compatibility level of 170 or above ([see documentation](https://learn.microsoft.com/en-us/ef/core/providers/sql-server/#compatibility-level)), EF will map to the new JSON data type instead:

```
CREATE TABLE [Blogs] (
    ...
    [Tags] json
    [Posts] json
);
```

Although the new JSON data type is the recommended way to store JSON data in SQL Server going forward, there may be some behavioral differences when transitioning from `nvarchar(max)`, and some specific querying forms may not be supported. For example, SQL Server does not support the DISTINCT operator over JSON arrays, and queries attempting to do so will fail.

Note that if you have an existing table and are using [UseAzureSql](https://learn.microsoft.com/en-us/dotnet/api/microsoft.entityframeworkcore.sqlserverdbcontextoptionsextensions.useazuresql), upgrading to EF 10 will cause a migration to be generated which alters all existing `nvarchar(max)` JSON columns to `json`. This alter operation is supported and should get applied seamlessly and without any issues, but is a non-trivial change to your database.

The new JSON data type introduced by SQL Server is a superior, 1st-class way to store and interact with JSON data in the database; it notably brings significant performance improvements ([see documentation](https://learn.microsoft.com/en-us/sql/t-sql/data-types/json-data-type)). All applications using Azure SQL Database or SQL Server 2025 are encouraged to migrate to the new JSON data type.

If you are targeting Azure SQL Database and do not wish to transition to the new JSON data type right away, you can configure EF with a compatibility level lower than 170:

```
protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
{
    optionsBuilder.UseAzureSql("<connection string>", o => o.UseCompatibilityLevel(160));
}
```

If you're targeting on-premises SQL Server, the default compatibility level with `UseSqlServer` is currently 150 (SQL Server 2019), so the JSON data type is not used.

As an alternative, you can explicitly set the column type on specific properties to be `nvarchar(max)`:

```
public class Blog
{
    public string[] Tags { get; set; }
    public List<Post> Posts { get; set; }
}

protected override void OnModelCreating(ModelBuilder modelBuilder)
{
    modelBuilder.Entity<Blog>().PrimitiveCollection(b => b.Tags).HasColumnType("nvarchar(max)");
    modelBuilder.Entity<Blog>().OwnsMany(b => b.Posts, b => b.ToJson().HasColumnType("nvarchar(max)"));
    modelBuilder.Entity<Blog>().ComplexProperty(e => e.Posts, b => b.ToJson());
}
```

[Tracking Issue #34346](https://github.com/dotnet/efcore/issues/34346)

In EF Core 9 and earlier, parameterized collections in LINQ queries (such as those used with `.Contains()`) were translated to SQL using a JSON array parameter by default. Consider the following query:

```
int[] ids = [1, 2, 3];
var blogs = await context.Blogs.Where(b => ids.Contains(b.Id)).ToListAsync();
```

On SQL Server, this generated the following SQL:

```
@__ids_0='[1,2,3]'

SELECT [b].[Id], [b].[Name]
FROM [Blogs] AS [b]
WHERE [b].[Id] IN (
    SELECT [i].[value]
    FROM OPENJSON(@__ids_0) WITH ([value] int '$') AS [i]
)
```

Starting with EF Core 10.0, parameterized collections are now translated using multiple scalar parameters by default:

```
SELECT [b].[Id], [b].[Name]
FROM [Blogs] AS [b]
WHERE [b].[Id] IN (@ids1, @ids2, @ids3)
```

The new default translation provides the query planner with cardinality information about the collection, which can lead to better query plans in many scenarios. The multiple parameter approach balances between plan cache efficiency (by parameterizing) and query optimization (by providing cardinality).

However, different workloads may benefit from different translation strategies depending on collection sizes, query patterns, and database characteristics.

Note

While the new default translation will not cause any behavioral change or performance regression in the majority of cases, the change in how queries are translated to SQL may have adverse consequences in some scenarios.

Applications that were built with EF Core 8 or 9, and rely on the performance characteristics of the JSON array parameter translation (using `OPENJSON` or similar database-specific functions) may experience performance differences when upgrading to EF Core 10. This is especially relevant for queries with large collections or specific query patterns that benefited from the previous translation strategy.

If you experience performance regressions after upgrading, consider using the mitigation strategies below to revert to the previous behavior globally or for specific queries.

If you encounter issues with the new default behavior (such as performance regressions), you can configure the translation mode globally:

```
protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    => optionsBuilder
        .UseSqlServer("<CONNECTION STRING>", 
            o => o.UseParameterizedCollectionMode(ParameterTranslationMode.Constant));
```

Available modes are:

* `ParameterTranslationMode.MultipleParameters` - The new default (multiple scalar parameters)
* `ParameterTranslationMode.Constant` - Inlines values as constants (pre-EF8 default behavior)
* `ParameterTranslationMode.Parameter` - Uses JSON array parameter (EF8-9 default)

You can also control the translation on a per-query basis:

```
// Use constants instead of parameters for this specific query
var blogs = await context.Blogs
    .Where(b => EF.Constant(ids).Contains(b.Id))
    .ToListAsync();

// Use a single parameter (e.g. JSON parameter with OPENJSON) instead of parameters for this specific query
var blogs = await context.Blogs
    .Where(b => EF.Parameter(ids).Contains(b.Id))
    .ToListAsync();

// Use multiple scalar parameters for this specific query. This is the default in EF 10, but is useful if the default was changed globally:
var blogs = await context.Blogs
    .Where(b => EF.MultipleParameters(ids).Contains(b.Id))
    .ToListAsync();
```

For more information about parameterized collection translation, [see the documentation](https://learn.microsoft.com/en-us/ef/core/what-is-new/ef-core-10.0/whatsnew#parameterized-collection-translation).

[Tracking Issue #32018](https://github.com/dotnet/efcore/issues/32018)

Previously, [ExecuteUpdate](https://learn.microsoft.com/en-us/dotnet/api/microsoft.entityframeworkcore.relationalqueryableextensions.executeupdate) accepted an expression tree argument (`Expression<Func<...>>`) for the column setters.

Starting with EF Core 10.0, [ExecuteUpdate](https://learn.microsoft.com/en-us/dotnet/api/microsoft.entityframeworkcore.relationalqueryableextensions.executeupdate) now accepts a non-expression argument (`Func<...>`) for the column setters. If you were building expression trees to dynamically create the column setters argument, your code will no longer compile - but can be replaced with a much simpler alternative (see below).

The fact that the column setters parameter was an expression tree made it quite difficult to do dynamic construction of the column setters, where some setters are only present based on some condition (see Mitigations below for an example).

Code that was building expression trees to dynamically create the column setters argument will need to be rewritten - but the result will be much simpler. For example, let's assume we want to update a Blog's Views, but conditionally also its Name. Since the setters argument was an expression tree, code such as the following needed to be written:

```
// Base setters - update the Views only
Expression<Func<SetPropertyCalls<Blog>, SetPropertyCalls<Blog>>> setters =
    s => s.SetProperty(b => b.Views, 8);

// Conditionally add SetProperty(b => b.Name, "foo") to setters, based on the value of nameChanged
if (nameChanged)
{
    var blogParameter = Expression.Parameter(typeof(Blog), "b");

    setters = Expression.Lambda<Func<SetPropertyCalls<Blog>, SetPropertyCalls<Blog>>>(
        Expression.Call(
            instance: setters.Body,
            methodName: nameof(SetPropertyCalls<Blog>.SetProperty),
            typeArguments: [typeof(string)],
            arguments:
            [
                Expression.Lambda<Func<Blog, string>>(Expression.Property(blogParameter, nameof(Blog.Name)), blogParameter),
                Expression.Constant("foo")
            ]),
        setters.Parameters);
}

await context.Blogs.ExecuteUpdateAsync(setters);
```

Manually creating expression trees is complicated and error-prone, and made this common scenario much more difficult than it should have been. Starting with EF 10, you can now write the following instead:

```
await context.Blogs.ExecuteUpdateAsync(s =>
{
    s.SetProperty(b => b.Views, 8);
    if (nameChanged)
    {
        s.SetProperty(b => b.Name, "foo");
    }
});
```

[Tracking Issue #4970](https://github.com/dotnet/EntityFramework.Docs/issues/4970)

Previously, when mapping complex types to table columns, if multiple properties in different complex types had the same column name, they would silently share the same column.

Starting with EF Core 10.0, complex type column names are uniquified by appending a number at the end if another column with the same name exists on the table.

This prevents data corruption that could occur when multiple properties are unintentionally mapped to the same column.

If you need multiple properties to share the same column, configure them explicitly using [Property](https://learn.microsoft.com/en-us/dotnet/api/microsoft.entityframeworkcore.metadata.builders.complexpropertybuilder.property) and [HasColumnName](https://learn.microsoft.com/en-us/dotnet/api/microsoft.entityframeworkcore.relationalpropertybuilderextensions.hascolumnname):

```
modelBuilder.Entity<Customer>(b =>
{
    b.ComplexProperty(c => c.ShippingAddress, p => p.Property(a => a.Street).HasColumnName("Street"));
    b.ComplexProperty(c => c.BillingAddress, p => p.Property(a => a.Street).HasColumnName("Street"));
});
```

Previously, properties on nested complex types were mapped to columns using just the declaring type name. For example, `EntityType.Complex.NestedComplex.Property` was mapped to column `NestedComplex_Property`.

Starting with EF Core 10.0, properties on nested complex types use the full path to the property as part of the column name. For example, `EntityType.Complex.NestedComplex.Property` is now mapped to column `Complex_NestedComplex_Property`.

This provides better column name uniqueness and makes it clearer which property maps to which column.

If you need to maintain the old column names, configure them explicitly using [Property](https://learn.microsoft.com/en-us/dotnet/api/microsoft.entityframeworkcore.metadata.builders.complexpropertybuilder.property) and [HasColumnName](https://learn.microsoft.com/en-us/dotnet/api/microsoft.entityframeworkcore.relationalpropertybuilderextensions.hascolumnname):

```
modelBuilder.Entity<EntityType>()
    .ComplexProperty(e => e.Complex)
    .ComplexProperty(o => o.NestedComplex)
    .Property(c => c.Property)
    .HasColumnName("NestedComplex_Property");
```

Previously, `IDiscriminatorPropertySetConvention.ProcessDiscriminatorPropertySet` took `IConventionEntityTypeBuilder` as a parameter.

Starting with EF Core 10.0, the method signature changed to take `IConventionTypeBaseBuilder` instead of `IConventionEntityTypeBuilder`.

This change allows the convention to work with both entity types and complex types.

Update your custom convention implementations to use the new signature:

```
public virtual void ProcessDiscriminatorPropertySet(
    IConventionTypeBaseBuilder typeBaseBuilder, // Changed from IConventionEntityTypeBuilder
    string name,
    Type type,
    MemberInfo memberInfo,
    IConventionContext<IConventionProperty> context)
```

[Tracking Issue #35757](https://github.com/dotnet/efcore/issues/35757)

Previously, methods on `IRelationalCommandDiagnosticsLogger` such as `CommandReaderExecuting`, `CommandReaderExecuted`, `CommandScalarExecuting`, and others accepted a `command` parameter representing the database command being executed.

Starting with EF Core 10.0, these methods now require an additional `logCommandText` parameter. This parameter contains the SQL command text that will be logged, which may have sensitive data redacted when [EnableSensitiveDataLogging](https://learn.microsoft.com/en-us/dotnet/api/microsoft.entityframeworkcore.dbcontextoptionsbuilder.enablesensitivedatalogging) is not enabled.

This change supports the new feature to [redact inlined constants from logging by default](https://learn.microsoft.com/en-us/ef/core/what-is-new/ef-core-10.0/whatsnew#redact-inlined-constants-from-logging-by-default). When EF inlines parameter values into SQL (e.g., when using `EF.Constant()`), those values are now redacted from logs unless sensitive data logging is explicitly enabled. The `logCommandText` parameter provides the redacted SQL for logging purposes, while the `command` parameter contains the actual SQL that gets executed.

If you have a custom implementation of `IRelationalCommandDiagnosticsLogger`, you'll need to update your method signatures to include the new `logCommandText` parameter. For example:

```
public InterceptionResult<DbDataReader> CommandReaderExecuting(
    IRelationalConnection connection,
    DbCommand command,
    DbContext context,
    Guid commandId,
    Guid connectionId,
    DateTimeOffset startTime,
    string logCommandText) // New parameter
{
    // Use logCommandText for logging purposes
    // Use command for execution-related logic
}
```

The `logCommandText` parameter contains the SQL to be logged (with inlined constants potentially redacted), while `command.CommandText` contains the actual SQL that will be executed against the database.

| **Breaking change** | **Impact** |
| --- | --- |
| [Using GetDateTimeOffset without an offset now assumes UTC](https://learn.microsoft.com/en-us/ef/core/what-is-new/ef-core-10.0/breaking-changes#DateTimeOffset-read) | High |
| [Writing DateTimeOffset into REAL column now writes in UTC](https://learn.microsoft.com/en-us/ef/core/what-is-new/ef-core-10.0/breaking-changes#DateTimeOffset-write) | High |
| [Using GetDateTime with an offset now returns value in UTC](https://learn.microsoft.com/en-us/ef/core/what-is-new/ef-core-10.0/breaking-changes#DateTime-read) | High |

[Tracking Issue #36195](https://github.com/dotnet/efcore/issues/36195)

Previously, when using `GetDateTimeOffset` on a textual timestamp that did not have an offset (e.g., `2014-04-15 10:47:16`), Microsoft.Data.Sqlite would assume the value was in the local time zone. I.e. the value was parsed as `2014-04-15 10:47:16+02:00` (assuming local time zone was UTC+2).

Starting with Microsoft.Data.Sqlite 10.0, when using `GetDateTimeOffset` on a textual timestamp that does not have an offset, Microsoft.Data.Sqlite will assume the value is in UTC.

Is is to align with SQLite's behavior where timestamps without an offset are treated as UTC.

Code should be adjusted accordingly.

As a last/temporary resort, you can revert to previous behavior by setting `Microsoft.Data.Sqlite.Pre10TimeZoneHandling` AppContext switch to `true`, see [AppContext for library consumers](https://learn.microsoft.com/en-us/dotnet/api/system.appcontext#ForConsumers) for more details.

```
AppContext.SetSwitch("Microsoft.Data.Sqlite.Pre10TimeZoneHandling", isEnabled: true);
```

[Tracking Issue #36195](https://github.com/dotnet/efcore/issues/36195)

Previously, when writing a `DateTimeOffset` value into a REAL column, Microsoft.Data.Sqlite would write the value without taking the offset into account.

Starting with Microsoft.Data.Sqlite 10.0, when writing a `DateTimeOffset` value into a REAL column, Microsoft.Data.Sqlite will convert the value to UTC before doing the conversions and writing it.

The value written was incorrect, not aligning with SQLite's behavior where REAL timestamps are asummed to be UTC.

Code should be adjusted accordingly.

As a last/temporary resort, you can revert to previous behavior by setting `Microsoft.Data.Sqlite.Pre10TimeZoneHandling` AppContext switch to `true`, see [AppContext for library consumers](https://learn.microsoft.com/en-us/dotnet/api/system.appcontext#ForConsumers) for more details.

```
AppContext.SetSwitch("Microsoft.Data.Sqlite.Pre10TimeZoneHandling", isEnabled: true);
```

[Tracking Issue #36195](https://github.com/dotnet/efcore/issues/36195)

Previously, when using `GetDateTime` on a textual timestamp that had an offset (e.g., `2014-04-15 10:47:16+02:00`), Microsoft.Data.Sqlite would return the value with `DateTimeKind.Local` (even if the offset was not local). The time was parsed correctly taking the offset into account.

Starting with Microsoft.Data.Sqlite 10.0, when using `GetDateTime` on a textual timestamp that has an offset, Microsoft.Data.Sqlite will convert the value to UTC and return it with `DateTimeKind.Utc`.

Even though the time was parsed correctly it was dependent on the machine-configured local time zone, which could lead to unexpected results.

Code should be adjusted accordingly.

As a last/temporary resort, you can revert to previous behavior by setting `Microsoft.Data.Sqlite.Pre10TimeZoneHandling` AppContext switch to `true`, see [AppContext for library consumers](https://learn.microsoft.com/en-us/dotnet/api/system.appcontext#ForConsumers) for more details.

```
AppContext.SetSwitch("Microsoft.Data.Sqlite.Pre10TimeZoneHandling", isEnabled: true);
```

# Source: https://fluentmigrator.github.io/intro/quick-start.html

Title: Quick Start Guide | FluentMigrator

URL Source: https://fluentmigrator.github.io/intro/quick-start.html

Markdown Content:
Get up and running with FluentMigrator in just a few minutes. This guide will walk you through creating your first migration and running it against a database.

Choose a Migration Runner [​](https://fluentmigrator.github.io/intro/quick-start.html#choose-a-migration-runner)
----------------------------------------------------------------------------------------------------------------

FluentMigrator provides several ways to execute your migrations, from in-process execution to command-line tools. We recommend using the in-process runner when possible for better integration with your application.

### Available Runners [​](https://fluentmigrator.github.io/intro/quick-start.html#available-runners)

| Runner | Use Case | Platform Support |
| --- | --- | --- |
| [In-Process Runner](https://fluentmigrator.github.io/runners/in-process.html) | Application startup, integrated execution | .NET Core/.NET 5+ |
| [Console Tool (Migrate.exe)](https://fluentmigrator.github.io/runners/console.html) | Build scripts, deployment automation | .NET Framework |
| [dotnet-fm](https://fluentmigrator.github.io/runners/dotnet-fm.html) | .NET Core CLI integration | .NET Core/.NET 5+ |

### Choosing the Right Runner [​](https://fluentmigrator.github.io/intro/quick-start.html#choosing-the-right-runner)

#### In-Process Runner ✅ **Recommended**[​](https://fluentmigrator.github.io/intro/quick-start.html#in-process-runner-%E2%9C%85-recommended)

*   **Best for**: Most applications
*   **Pros**: Type safety, better error handling, dependency injection support
*   **Cons**: Requires code changes

#### Console Tool (Migrate.exe) [​](https://fluentmigrator.github.io/intro/quick-start.html#console-tool-migrate-exe)

*   **Best for**: Legacy .NET Framework applications, external deployment scripts
*   **Pros**: No code changes required, works with any .NET application
*   **Cons**: Platform-specific, less flexible

#### dotnet-fm CLI Tool [​](https://fluentmigrator.github.io/intro/quick-start.html#dotnet-fm-cli-tool)

*   **Best for**: .NET Core applications, CI/CD pipelines
*   **Pros**: Cross-platform, integrates with dotnet CLI
*   **Cons**: Requires .NET Core SDK

### Quick Start Examples [​](https://fluentmigrator.github.io/intro/quick-start.html#quick-start-examples)

#### In-Process (Recommended) [​](https://fluentmigrator.github.io/intro/quick-start.html#in-process-recommended)

csharp

```
using var serviceProvider = new ServiceCollection()
    .AddFluentMigratorCore()
    .ConfigureRunner(rb => rb
        .AddSqlServer()
        .WithGlobalConnectionString(connectionString)
        .ScanIn(typeof(MyMigration).Assembly).For.All())
    .BuildServiceProvider(false);

using var scope = serviceProvider.CreateScope();
var runner = scope.ServiceProvider.GetRequiredService<IMigrationRunner>();
runner.MigrateUp();
```

A more complete sample is available [below](https://fluentmigrator.github.io/intro/quick-start.html#step-3-configure-the-migration-runner).

#### dotnet-fm CLI [​](https://fluentmigrator.github.io/intro/quick-start.html#dotnet-fm-cli)

bash

```
# Install globally
dotnet tool install -g FluentMigrator.DotNet.Cli

# Run migrations
dotnet fm migrate -p sqlite -c "Data Source=test.db" -a "MyApp.dll"
```

#### Console Tool [​](https://fluentmigrator.github.io/intro/quick-start.html#console-tool)

bash

```
# Install via NuGet
Install-Package FluentMigrator.Console

# Run from tools directory
..\tools\net48\Migrate.exe -p sqlserver -c "Server=.;Database=MyDb;Integrated Security=true" -a "MyApp.dll"
```

Prerequisites [​](https://fluentmigrator.github.io/intro/quick-start.html#prerequisites)
----------------------------------------------------------------------------------------

*   .NET 8.0 or later
*   A supported database (SQL Server, PostgreSQL, MySQL, SQLite, etc.)
*   Basic knowledge of C# and database concepts

Step 1: Install FluentMigrator [​](https://fluentmigrator.github.io/intro/quick-start.html#step-1-install-fluentmigrator)
-------------------------------------------------------------------------------------------------------------------------

### Using Package Manager Console [​](https://fluentmigrator.github.io/intro/quick-start.html#using-package-manager-console)

powershell

```
Install-Package FluentMigrator
Install-Package FluentMigrator.Runner
```

### Using .NET CLI [​](https://fluentmigrator.github.io/intro/quick-start.html#using-net-cli)

bash

```
dotnet add package FluentMigrator
dotnet add package FluentMigrator.Runner
```

### Using PackageReference [​](https://fluentmigrator.github.io/intro/quick-start.html#using-packagereference)

Add these to your `.csproj` file:

xml

```
<PackageReference Include="FluentMigrator" Version="7.2.0" /> <!-- Use the latest stable version -->
<PackageReference Include="FluentMigrator.Runner" Version="7.2.0" />
```

You'll also need one of the [database provider packages](https://fluentmigrator.github.io/intro/installation.html#database-provider-packages).

Step 2: Create Your First Migration [​](https://fluentmigrator.github.io/intro/quick-start.html#step-2-create-your-first-migration)
-----------------------------------------------------------------------------------------------------------------------------------

Create a new class that inherits from `Migration`:

csharp

```
using FluentMigrator;

[Migration(20240101120000)]
public class CreateUsersTable : Migration
{
    public override void Up()
    {
        Create.Table("Users")
            .WithColumn("Id").AsInt32().NotNullable().PrimaryKey().Identity()
            .WithColumn("Username").AsString(50).NotNullable().Unique()
            .WithColumn("Email").AsString(255).NotNullable()
            .WithColumn("FirstName").AsString(100).Nullable()
            .WithColumn("LastName").AsString(100).Nullable()
            .WithColumn("IsActive").AsBoolean().NotNullable().WithDefaultValue(true)
            .WithColumn("CreatedAt").AsDateTime().NotNullable().WithDefault(SystemMethods.CurrentDateTime);
    }

    public override void Down()
    {
        Delete.Table("Users");
    }
}
```

### Key Points: [​](https://fluentmigrator.github.io/intro/quick-start.html#key-points)

*   **Migration Attribute**: `[Migration(20240101120000)]` - Use a timestamp format (YYYYMMDDhhmmss)
*   **Up Method**: Defines changes to apply when migrating forward
*   **Down Method**: Defines how to undo the changes (for rollbacks)

Step 3: Configure the Migration Runner [​](https://fluentmigrator.github.io/intro/quick-start.html#step-3-configure-the-migration-runner)
-----------------------------------------------------------------------------------------------------------------------------------------

Create a console application or add migration support to your existing app:

csharp

```
using FluentMigrator.Runner;
using Microsoft.Extensions.DependencyInjection;

class Program
{
    static void Main(string[] args)
    {
        var serviceProvider = CreateServices();

        // Put the database update into a scope to ensure
        // that all resources will be disposed.
        using (var scope = serviceProvider.CreateScope())
        {
            UpdateDatabase(scope.ServiceProvider);
        }
    }

    /// <summary>
    /// Configure the dependency injection services
    /// </summary>
    private static ServiceProvider CreateServices()
    {
        return new ServiceCollection()
            // Add common FluentMigrator services
            .AddFluentMigratorCore()
            .ConfigureRunner(rb => rb
                // Add SQL Server support to FluentMigrator
                .AddSqlServer()
                // Set the connection string
                .WithGlobalConnectionString("Server=.;Database=MyApp;Trusted_Connection=true;")
                // Define the assembly containing the migrations
                .ScanIn(typeof(CreateUsersTable).Assembly).For.Migrations())
            // Enable logging to console in the FluentMigrator way
            .AddLogging(lb => lb.AddFluentMigratorConsole())
            // Build the service provider
            .BuildServiceProvider(false);
    }

    /// <summary>
    /// Update the database
    /// </summary>
    private static void UpdateDatabase(IServiceProvider serviceProvider)
    {
        // Instantiate the runner
        var runner = serviceProvider.GetRequiredService<IMigrationRunner>();

        // Execute the migrations
        runner.MigrateUp();
    }
}
```

Step 4: Run Your Migration [​](https://fluentmigrator.github.io/intro/quick-start.html#step-4-run-your-migration)
-----------------------------------------------------------------------------------------------------------------

Run your application and FluentMigrator will:

1.   Create a version tracking table (usually named `VersionInfo`)
2.   Execute your migration
3.   Mark the migration as completed in the tracking table

Step 5: Add More Migrations [​](https://fluentmigrator.github.io/intro/quick-start.html#step-5-add-more-migrations)
-------------------------------------------------------------------------------------------------------------------

As your application evolves, add more migrations:

csharp

```
[Migration(20240102090000)]
public class AddUserRoles : Migration
{
    public override void Up()
    {
        Create.Table("Roles")
            .WithColumn("Id").AsInt32().NotNullable().PrimaryKey().Identity()
            .WithColumn("Name").AsString(50).NotNullable().Unique()
            .WithColumn("Description").AsString(255).Nullable();

        Insert.IntoTable("Roles")
            .Row(new { Name = "Admin", Description = "Administrator" })
            .Row(new { Name = "User", Description = "Regular User" });

        Alter.Table("Users")
            .AddColumn("RoleId").AsInt32().Nullable()
                .ForeignKey("FK_Users_Roles", "Roles", "Id");
    }

    public override void Down()
    {
        Delete.ForeignKey("FK_Users_Roles").OnTable("Users");
        Delete.Column("RoleId").FromTable("Users");
        Delete.Table("Roles");
    }
}
```

Alternative Database Configurations [​](https://fluentmigrator.github.io/intro/quick-start.html#alternative-database-configurations)
------------------------------------------------------------------------------------------------------------------------------------

For comprehensive database provider configuration and advanced options, see the [Configuration Guide](https://fluentmigrator.github.io/intro/configuration.html).

### PostgreSQL [​](https://fluentmigrator.github.io/intro/quick-start.html#postgresql)

csharp

```
.AddPostgres()
.WithGlobalConnectionString("Host=localhost;Database=myapp;Username=myuser;Password=mypass")
```

### MySQL [​](https://fluentmigrator.github.io/intro/quick-start.html#mysql)

csharp

```
.AddMySql5()
.WithGlobalConnectionString("Server=localhost;Database=myapp;Uid=myuser;Pwd=mypass;")
```

### SQLite [​](https://fluentmigrator.github.io/intro/quick-start.html#sqlite)

csharp

```
.AddSQLite()
.WithGlobalConnectionString("Data Source=myapp.db")
```

Using appsettings.json [​](https://fluentmigrator.github.io/intro/quick-start.html#using-appsettings-json)
----------------------------------------------------------------------------------------------------------

For real applications, store connection strings in configuration:

json

```
{
  "ConnectionStrings": {
    "Default": "Server=.;Database=MyApp;Trusted_Connection=true;"
  }
}
```

csharp

```
var configuration = new ConfigurationBuilder()
    .AddJsonFile("appsettings.json")
    .Build();

var connectionString = configuration.GetConnectionString("Default");

return new ServiceCollection()
    .AddFluentMigratorCore()
    .ConfigureRunner(rb => rb
        .AddSqlServer()
        .WithGlobalConnectionString(connectionString)
        .ScanIn(typeof(CreateUsersTable).Assembly).For.Migrations())
    .AddLogging(lb => lb.AddFluentMigratorConsole())
    .BuildServiceProvider(false);
```

Next Steps [​](https://fluentmigrator.github.io/intro/quick-start.html#next-steps)
----------------------------------------------------------------------------------

Now that you have your first migration running, explore these topics:

*   [Configuration](https://fluentmigrator.github.io/intro/configuration.html) - Comprehensive configuration guide for all runners and scenarios
*   [Creating Tables](https://fluentmigrator.github.io/operations/create-tables.html) - Learn all the options for creating tables
*   [Altering Tables](https://fluentmigrator.github.io/operations/alter-tables.html) - Modify existing tables safely
*   [Database Providers](https://fluentmigrator.github.io/providers/sql-server.html) - Provider-specific features and considerations
*   [Best Practices](https://fluentmigrator.github.io/advanced/best-practices.html) - Tips for writing maintainable migrations

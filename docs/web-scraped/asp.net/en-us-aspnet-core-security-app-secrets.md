# Source: https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets?view=aspnetcore-10.0

Title: Safe storage of app secrets in development in ASP.NET Core

URL Source: https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets?view=aspnetcore-10.0

Markdown Content:
By [Rick Anderson](https://twitter.com/RickAndMSFT) and [Kirk Larkin](https://twitter.com/serpent5)

[View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/security/app-secrets/samples) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample))

This article explains how to manage sensitive data for an ASP.NET Core app on a development machine. Never store passwords or other sensitive data in source code or configuration files. Production secrets shouldn't be used for development or test. Secrets shouldn't be deployed with the app. Production secrets should be accessed through a controlled means like Azure Key Vault. Azure test and production secrets can be stored and protected with the [Azure Key Vault configuration provider](https://learn.microsoft.com/en-us/aspnet/core/security/key-vault-configuration?view=aspnetcore-10.0).

For more information on authentication for deployed test and production apps, see [Secure authentication flows](https://learn.microsoft.com/en-us/aspnet/core/security/?view=aspnetcore-10.0#secure-authentication-flows).

To use user secrets in a .NET console app, see [this GitHub issue](https://github.com/dotnet/EntityFramework.Docs/issues/3939#issuecomment-1191978026).

Environment variables are used to avoid storage of app secrets in code or in local configuration files. Environment variables override configuration values for all previously specified configuration sources.

Consider an ASP.NET Core web app in which **Individual Accounts** security is enabled. A default database connection string is included in the project's `appsettings.json` file with the key `DefaultConnection`. The default connection string is for LocalDB, which runs in user mode and doesn't require a password. During app deployment, the `DefaultConnection` key value can be overridden with an environment variable's value. The environment variable may store the complete connection string with sensitive credentials.

Warning

Environment variables are generally stored in plain, unencrypted text. If the machine or process is compromised, environment variables can be accessed by untrusted parties. Additional measures to prevent disclosure of user secrets may be required.

The `:` separator doesn't work with environment variable hierarchical keys on all platforms. For example, the `:` separator isn't supported by [Bash](https://linuxhint.com/bash-environment-variables/). The double underscore, `__`, is supported by all platforms and automatically replaced by a colon, `:`.

The Secret Manager tool stores sensitive data during application development. In this context, a piece of sensitive data is an app secret. App secrets are stored in a separate location from the project tree. The app secrets are associated with a specific project or shared across several projects. The app secrets aren't checked into source control.

Warning

The Secret Manager tool doesn't encrypt the stored secrets and shouldn't be treated as a trusted store. It's for development purposes only. The keys and values are stored in a JSON configuration file in the user profile directory.

The Secret Manager tool hides implementation details, such as where and how the values are stored. You can use the tool without knowing these implementation details. The values are stored in a JSON file in the local machine's user profile folder:

*   [Windows](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets?view=aspnetcore-10.0#tabpanel_1_windows)
*   [Linux / macOS](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets?view=aspnetcore-10.0#tabpanel_1_linux+macos)

File system path:

`~/.microsoft/usersecrets/<user_secrets_id>/secrets.json`

In the preceding file paths, replace `<user_secrets_id>` with the `UserSecretsId` value specified in the project file.

Don't write code that depends on the location or format of data saved with the Secret Manager tool. These implementation details may change. For example, the secret values aren't encrypted.

The Secret Manager tool operates on project-specific configuration settings stored in your user profile.

The Secret Manager tool includes an `init` command. To use user secrets, run the following command in the project directory:

```
dotnet user-secrets init
```

The preceding command adds a `UserSecretsId` element within a `PropertyGroup` of the project file. By default, the inner text of `UserSecretsId` is a GUID. The inner text is arbitrary, but is unique to the project.

![Image 1: The UserSecretsId MSBuild property configuration in the app's project file.](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets/_static/usersecretsid.png?view=aspnetcore-10.0)

In Visual Studio, right-click the project in Solution Explorer, and select **Manage User Secrets** from the context menu. This gesture adds a `UserSecretsId` element, populated with a GUID, to the project file.

If the generation of assembly info attributes is disabled, manually add the [UserSecretsIdAttribute](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.configuration.usersecrets.usersecretsidattribute) in `AssemblyInfo.cs`. For example:

```
[assembly: UserSecretsId("your_user_secrets_id")]
```

When manually adding the `UserSecretsId` attribute to `AssemblyInfo.cs`, the `UserSecretsId` value must match the value in the project file.

Define an app secret consisting of a key and its value. The secret is associated with the project's `UserSecretsId` value. For example, run the following command from the directory in which the project file exists:

```
dotnet user-secrets set "Movies:ServiceApiKey" "12345"
```

In the preceding example, the colon denotes that `Movies` is an object literal with a `ServiceApiKey` property.

The Secret Manager tool can be used from other directories too. Use the `--project` option to supply the file system path at which the project file exists. For example:

```
dotnet user-secrets set "Movies:ServiceApiKey" "12345" --project "C:\apps\WebApp1\src\WebApp1"
```

Visual Studio's **Manage User Secrets** gesture opens a `secrets.json` file in the text editor. Replace the contents of `secrets.json` with the key-value pairs to be stored. For example:

```
{
  "Movies": {
    "ConnectionString": "Server=(localdb)\\mssqllocaldb;Database=Movie-1;Trusted_Connection=True;MultipleActiveResultSets=true",
    "ServiceApiKey": "12345"
  }
}
```

The JSON structure is flattened after modifications via `dotnet user-secrets remove` or `dotnet user-secrets set`. For example, running `dotnet user-secrets remove "Movies:ConnectionString"` collapses the `Movies` object literal. The modified file resembles the following JSON:

```
{
  "Movies:ServiceApiKey": "12345"
}
```

A batch of secrets can be set by piping JSON to the `set` command. In the following example, the `input.json` file's contents are piped to the `set` command.

*   [Windows](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets?view=aspnetcore-10.0#tabpanel_2_windows)
*   [Linux / macOS](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets?view=aspnetcore-10.0#tabpanel_2_linux+macos)

Open a command shell, and execute the following command:

```
cat ./input.json | dotnet user-secrets set
```

To access a secret, complete the following steps:

1.   [Register the user secrets configuration source](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets?view=aspnetcore-10.0#register-the-user-secrets-configuration-source)
2.   [Read the secret via the Configuration API](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets?view=aspnetcore-10.0#read-the-secret-via-the-configuration-api)

The user secrets [configuration provider](https://learn.microsoft.com/en-us/dotnet/core/extensions/configuration-providers) registers the appropriate configuration source with the .NET [Configuration API](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-10.0).

ASP.NET Core web apps created with [dotnet new](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-new) or Visual Studio generate the following code:

```
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => "Hello World!");

app.Run();
```

[WebApplication.CreateBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.webapplication.createbuilder) initializes a new instance of the [WebApplicationBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.webapplicationbuilder) class with preconfigured defaults. The initialized `WebApplicationBuilder` (`builder`) provides default configuration and calls [AddUserSecrets](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.configuration.usersecretsconfigurationextensions.addusersecrets) when the [EnvironmentName](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.ihostenvironment.environmentname#microsoft-extensions-hosting-ihostenvironment-environmentname) is [Development](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.environmentname.development#microsoft-extensions-hosting-environmentname-development):

Consider the following examples of reading the `Movies:ServiceApiKey` key:

**Program.cs file:**

```
var builder = WebApplication.CreateBuilder(args);
var movieApiKey = builder.Configuration["Movies:ServiceApiKey"];

var app = builder.Build();

app.MapGet("/", () => movieApiKey);

app.Run();
```

**Razor Pages page model:**

```
public class IndexModel : PageModel
{
    private readonly IConfiguration _config;

    public IndexModel(IConfiguration config)
    {
        _config = config;
    }

    public void OnGet()
    {
        var moviesApiKey = _config["Movies:ServiceApiKey"];

        // call Movies service with the API key
    }
}
```

For more information, see [Configuration in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-10.0).

Mapping an entire object literal to a POCO (a simple .NET class with properties) is useful for aggregating related properties.

Assume the app's `secrets.json` file contains the following two secrets:

```
{
  "Movies:ConnectionString": "Server=(localdb)\\mssqllocaldb;Database=Movie-1;Trusted_Connection=True;MultipleActiveResultSets=true",
  "Movies:ServiceApiKey": "12345"
}
```

To map the preceding secrets to a POCO, use the .NET Configuration API's [object graph binding](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-10.0#bind-an-array) feature. The following code binds to a custom `MovieSettings` POCO and accesses the `ServiceApiKey` property value:

```
var moviesConfig = 
    Configuration.GetSection("Movies").Get<MovieSettings>();
_moviesApiKey = moviesConfig.ServiceApiKey;
```

The `Movies:ConnectionString` and `Movies:ServiceApiKey` secrets are mapped to the respective properties in `MovieSettings`:

```
public class MovieSettings
{
    public string ConnectionString { get; set; }

    public string ServiceApiKey { get; set; }
}
```

Storing passwords in plain text is insecure. Never store secrets in a configuration file such as `appsettings.json`, which might get checked in to a source code repository.

For example, a database connection string stored in `appsettings.json` should not include a password. Instead, store the password as a secret, and include the password in the connection string at runtime. For example:

```
dotnet user-secrets set "DbPassword" "`<secret value>`"
```

Replace the `<secret value>` placeholder in the preceding example with the password value. Set the secret's value on a [SqlConnectionStringBuilder](https://learn.microsoft.com/en-us/dotnet/api/system.data.sqlclient.sqlconnectionstringbuilder) object's [Password](https://learn.microsoft.com/en-us/dotnet/api/system.data.sqlclient.sqlconnectionstringbuilder.password) property to include it as the password value in the connection string:

```
using System.Data.SqlClient;

var builder = WebApplication.CreateBuilder(args);

var conStrBuilder = new SqlConnectionStringBuilder(
        builder.Configuration.GetConnectionString("Movies"));
conStrBuilder.Password = builder.Configuration["DbPassword"];
var connection = conStrBuilder.ConnectionString;

var app = builder.Build();

app.MapGet("/", () => connection);

app.Run();
```

Assume the app's `secrets.json` file contains the following two secrets:

```
{
  "Movies:ConnectionString": "Server=(localdb)\\mssqllocaldb;Database=Movie-1;Trusted_Connection=True;MultipleActiveResultSets=true",
  "Movies:ServiceApiKey": "12345"
}
```

Run the following command from the directory in which the project file exists:

```
dotnet user-secrets list
```

The following output appears:

```
Movies:ConnectionString = Server=(localdb)\mssqllocaldb;Database=Movie-1;Trusted_Connection=True;MultipleActiveResultSets=true
Movies:ServiceApiKey = 12345
```

In the preceding example, a colon in the key names denotes the object hierarchy within `secrets.json`.

Assume the app's `secrets.json` file contains the following two secrets:

```
{
  "Movies:ConnectionString": "Server=(localdb)\\mssqllocaldb;Database=Movie-1;Trusted_Connection=True;MultipleActiveResultSets=true",
  "Movies:ServiceApiKey": "12345"
}
```

Run the following command from the directory in which the project file exists:

```
dotnet user-secrets remove "Movies:ConnectionString"
```

The app's `secrets.json` file was modified to remove the key-value pair associated with the `Movies:ConnectionString` key:

```
{
  "Movies": {
    "ServiceApiKey": "12345"
  }
}
```

`dotnet user-secrets list` displays the following message:

```
Movies:ServiceApiKey = 12345
```

Assume the app's `secrets.json` file contains the following two secrets:

```
{
  "Movies:ConnectionString": "Server=(localdb)\\mssqllocaldb;Database=Movie-1;Trusted_Connection=True;MultipleActiveResultSets=true",
  "Movies:ServiceApiKey": "12345"
}
```

Run the following command from the directory in which the project file exists:

```
dotnet user-secrets clear
```

All user secrets for the app have been deleted from the `secrets.json` file:

```
{}
```

Running `dotnet user-secrets list` displays the following message:

```
No secrets configured for this application.
```

To manage user secrets in Visual Studio, right click the project in solution explorer and select **Manage User Secrets**:

![Image 2: Visual Studio showing Manage User Secrets](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets/_static/usvs.png?view=aspnetcore-10.0)

See [this GitHub issue](https://github.com/dotnet/AspNetCore.Docs/issues/27611).

Projects that target `Microsoft.NET.Sdk.Web` automatically include support for user secrets. For projects that target `Microsoft.NET.Sdk`, such as console applications, install the configuration extension and user secrets NuGet packages explicitly.

Using PowerShell:

```
Install-Package Microsoft.Extensions.Configuration
Install-Package Microsoft.Extensions.Configuration.UserSecrets
```

Using the .NET CLI:

```
dotnet add package Microsoft.Extensions.Configuration
dotnet add package Microsoft.Extensions.Configuration.UserSecrets
```

Once the packages are installed, [initialize the project](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets?view=aspnetcore-10.0#enable-secret-storage) and [set secrets](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets?view=aspnetcore-10.0#set-a-secret) the same way as for a web app. The following example shows a console application that retrieves the value of a secret that was set with the key "AppSecret":

```
using Microsoft.Extensions.Configuration;

namespace ConsoleApp;

class Program
{
    static void Main(string[] args)
    {
        IConfigurationRoot config = new ConfigurationBuilder()
            .AddUserSecrets<Program>()
            .Build();

        Console.WriteLine(config["AppSecret"]);
    }
}
```

*   See [this issue](https://github.com/dotnet/AspNetCore.Docs/issues/30378) and [this issue](https://github.com/dotnet/AspNetCore.Docs/issues/16328) for information on accessing user secrets from IIS.
*   [Configuration in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-10.0)
*   [Azure Key Vault configuration provider in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/key-vault-configuration?view=aspnetcore-10.0)

By [Rick Anderson](https://twitter.com/RickAndMSFT), [Kirk Larkin](https://twitter.com/serpent5), [Daniel Roth](https://github.com/danroth27), and [Scott Addie](https://github.com/scottaddie)

[View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/security/app-secrets/samples) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample))

This article explains how to manage sensitive data for an ASP.NET Core app on a development machine. Never store passwords or other sensitive data in source code or configuration files. Production secrets shouldn't be used for development or test. Secrets shouldn't be deployed with the app. Production secrets should be accessed through a controlled means like Azure Key Vault. Azure test and production secrets can be stored and protected with the [Azure Key Vault configuration provider](https://learn.microsoft.com/en-us/aspnet/core/security/key-vault-configuration?view=aspnetcore-10.0).

For more information on authentication for test and production environments, see [Secure authentication flows](https://learn.microsoft.com/en-us/aspnet/core/security/?view=aspnetcore-10.0#secure-authentication-flows).

Environment variables are used to avoid storage of app secrets in code or in local configuration files. Environment variables override configuration values for all previously specified configuration sources.

Consider an ASP.NET Core web app in which **Individual User Accounts** security is enabled. A default database connection string is included in the project's `appsettings.json` file with the key `DefaultConnection`. The default connection string is for LocalDB, which runs in user mode and doesn't require a password. During app deployment, the `DefaultConnection` key value can be overridden with an environment variable's value. The environment variable may store the complete connection string with sensitive credentials.

Warning

Environment variables are generally stored in plain, unencrypted text. If the machine or process is compromised, environment variables can be accessed by untrusted parties. Additional measures to prevent disclosure of user secrets may be required.

The `:` separator doesn't work with environment variable hierarchical keys on all platforms. For example, the `:` separator isn't supported by [Bash](https://linuxhint.com/bash-environment-variables/). The double underscore, `__`, is supported by all platforms and automatically replaced by a colon, `:`.

The Secret Manager tool stores sensitive data during application development. In this context, a piece of sensitive data is an app secret. App secrets are stored in a separate location from the project tree. The app secrets are associated with a specific project or shared across several projects. The app secrets aren't checked into source control.

Warning

The Secret Manager tool doesn't encrypt the stored secrets and shouldn't be treated as a trusted store. It's for development purposes only. The keys and values are stored in a JSON configuration file in the user profile directory.

The Secret Manager tool hides implementation details, such as where and how the values are stored. You can use the tool without knowing these implementation details. The values are stored in a JSON file in the local machine's user profile folder:

*   [Windows](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets?view=aspnetcore-10.0#tabpanel_1_windows)
*   [Linux / macOS](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets?view=aspnetcore-10.0#tabpanel_1_linux+macos)

File system path:

`~/.microsoft/usersecrets/<user_secrets_id>/secrets.json`

In the preceding file paths, replace `<user_secrets_id>` with the `UserSecretsId` value specified in the project file.

Don't write code that depends on the location or format of data saved with the Secret Manager tool. These implementation details may change. For example, the secret values aren't encrypted, but could be in the future.

The Secret Manager tool operates on project-specific configuration settings stored in your user profile.

The Secret Manager tool includes an `init` command in .NET Core SDK 3.0.100 or later. To use user secrets, run the following command in the project directory:

```
dotnet user-secrets init
```

The preceding command adds a `UserSecretsId` element within a `PropertyGroup` of the project file. By default, the inner text of `UserSecretsId` is a GUID. The inner text is arbitrary, but is unique to the project.

```
<PropertyGroup>
  <TargetFramework>netcoreapp3.1</TargetFramework>
  <UserSecretsId>79a3edd0-2092-40a2-a04d-dcb46d5ca9ed</UserSecretsId>
</PropertyGroup>
```

In Visual Studio, right-click the project in Solution Explorer, and select **Manage User Secrets** from the context menu. This gesture adds a `UserSecretsId` element, populated with a GUID, to the project file.

Define an app secret consisting of a key and its value. The secret is associated with the project's `UserSecretsId` value. For example, run the following command from the directory in which the project file exists:

```
dotnet user-secrets set "Movies:ServiceApiKey" "12345"
```

In the preceding example, the colon denotes that `Movies` is an object literal with a `ServiceApiKey` property.

The Secret Manager tool can be used from other directories too. Use the `--project` option to supply the file system path at which the project file exists. For example:

```
dotnet user-secrets set "Movies:ServiceApiKey" "12345" --project "C:\apps\WebApp1\src\WebApp1"
```

Visual Studio's **Manage User Secrets** gesture opens a `secrets.json` file in the text editor. Replace the contents of `secrets.json` with the key-value pairs to be stored. For example:

```
{
  "Movies": {
    "ConnectionString": "Server=(localdb)\\mssqllocaldb;Database=Movie-1;Trusted_Connection=True;MultipleActiveResultSets=true",
    "ServiceApiKey": "12345"
  }
}
```

The JSON structure is flattened after modifications via `dotnet user-secrets remove` or `dotnet user-secrets set`. For example, running `dotnet user-secrets remove "Movies:ConnectionString"` collapses the `Movies` object literal. The modified file resembles the following JSON:

```
{
  "Movies:ServiceApiKey": "12345"
}
```

A batch of secrets can be set by piping JSON to the `set` command. In the following example, the `input.json` file's contents are piped to the `set` command.

*   [Windows](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets?view=aspnetcore-10.0#tabpanel_2_windows)
*   [Linux / macOS](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets?view=aspnetcore-10.0#tabpanel_2_linux+macos)

Open a command shell, and execute the following command:

```
cat ./input.json | dotnet user-secrets set
```

To access a secret, complete the following steps:

1.   [Register the user secrets configuration source](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets?view=aspnetcore-10.0#register-the-user-secrets-configuration-source)
2.   [Read the secret via the Configuration API](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets?view=aspnetcore-10.0#read-the-secret-via-the-configuration-api)

The user secrets [configuration provider](https://learn.microsoft.com/en-us/dotnet/core/extensions/configuration-providers) registers the appropriate configuration source with the .NET [Configuration API](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-10.0).

The user secrets configuration source is automatically added in Development mode when the project calls [CreateDefaultBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.host.createdefaultbuilder). `CreateDefaultBuilder` calls [AddUserSecrets](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.configuration.usersecretsconfigurationextensions.addusersecrets) when the [EnvironmentName](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.ihostenvironment.environmentname#microsoft-extensions-hosting-ihostenvironment-environmentname) is [Development](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.environmentname.development#microsoft-extensions-hosting-environmentname-development):

```
public static IHostBuilder CreateHostBuilder(string[] args) =>
    Host.CreateDefaultBuilder(args)
        .ConfigureWebHostDefaults(webBuilder =>
        {
            webBuilder.UseStartup<Startup>();
        });
```

When `CreateDefaultBuilder` isn't called, add the user secrets configuration source explicitly by calling [AddUserSecrets](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.configuration.usersecretsconfigurationextensions.addusersecrets) in [ConfigureAppConfiguration](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.hostbuilder.configureappconfiguration). Call `AddUserSecrets` only when the app runs in the `Development` environment, as shown in the following example:

```
public class Program
{
    public static void Main(string[] args)
    {
        var host = new HostBuilder()
            .ConfigureAppConfiguration((hostContext, builder) =>
            {
                // Add other providers for JSON, etc.

                if (hostContext.HostingEnvironment.IsDevelopment())
                {
                    builder.AddUserSecrets<Program>();
                }
            })
            .Build();
        
        host.Run();
    }
}
```

If the user secrets configuration source is registered, the .NET Configuration API can read the secrets. [Constructor injection](https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection/overview#constructor-injection-behavior) can be used to gain access to the .NET Configuration API. Consider the following examples of reading the `Movies:ServiceApiKey` key:

**Startup class:**

```
public class Startup
{
    private string _moviesApiKey = null;

    public Startup(IConfiguration configuration)
    {
        Configuration = configuration;
    }

    public IConfiguration Configuration { get; }

    public void ConfigureServices(IServiceCollection services)
    {
        _moviesApiKey = Configuration["Movies:ServiceApiKey"];
    }

    public void Configure(IApplicationBuilder app)
    {
        app.Run(async (context) =>
        {
            var result = string.IsNullOrEmpty(_moviesApiKey) ? "Null" : "Not Null";
            await context.Response.WriteAsync($"Secret is {result}");
        });
    }
}
```

**Razor Pages page model:**

```
public class IndexModel : PageModel
{
    private readonly IConfiguration _config;

    public IndexModel(IConfiguration config)
    {
        _config = config;
    }

    public void OnGet()
    {
        var moviesApiKey = _config["Movies:ServiceApiKey"];

        // call Movies service with the API key
    }
}
```

For more information, see [Access configuration in Startup](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-10.0#access-configuration-in-startup) and [Access configuration in Razor Pages](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-10.0#access-configuration-in-razor-pages).

Mapping an entire object literal to a POCO (a simple .NET class with properties) is useful for aggregating related properties.

Assume the app's `secrets.json` file contains the following two secrets:

```
{
  "Movies:ConnectionString": "Server=(localdb)\\mssqllocaldb;Database=Movie-1;Trusted_Connection=True;MultipleActiveResultSets=true",
  "Movies:ServiceApiKey": "12345"
}
```

To map the preceding secrets to a POCO, use the .NET Configuration API's [object graph binding](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-10.0#bind-an-array) feature. The following code binds to a custom `MovieSettings` POCO and accesses the `ServiceApiKey` property value:

```
var moviesConfig = 
    Configuration.GetSection("Movies").Get<MovieSettings>();
_moviesApiKey = moviesConfig.ServiceApiKey;
```

The `Movies:ConnectionString` and `Movies:ServiceApiKey` secrets are mapped to the respective properties in `MovieSettings`:

```
public class MovieSettings
{
    public string ConnectionString { get; set; }

    public string ServiceApiKey { get; set; }
}
```

Storing passwords in plain text is insecure. Never store secrets in a configuration file such as `appsettings.json`, which might get checked in to a source code repository.

For example, a database connection string stored in `appsettings.json` should not include a password. Instead, store the password as a secret, and include the password in the connection string at runtime. For example:

```
dotnet user-secrets set "DbPassword" "<secret value>"
```

Replace the `<secret value>` placeholder in the preceding example with the password value. Set the secret's value on a [SqlConnectionStringBuilder](https://learn.microsoft.com/en-us/dotnet/api/system.data.sqlclient.sqlconnectionstringbuilder) object's [Password](https://learn.microsoft.com/en-us/dotnet/api/system.data.sqlclient.sqlconnectionstringbuilder.password) property to include it as the password value in the connection string:

```
using System.Data.SqlClient;

var builder = WebApplication.CreateBuilder(args);

var conStrBuilder = new SqlConnectionStringBuilder(
        builder.Configuration.GetConnectionString("Movies"));
conStrBuilder.Password = builder.Configuration["DbPassword"];
var connection = conStrBuilder.ConnectionString;

var app = builder.Build();

app.MapGet("/", () => connection);

app.Run();
```

Assume the app's `secrets.json` file contains the following two secrets:

```
{
  "Movies:ConnectionString": "Server=(localdb)\\mssqllocaldb;Database=Movie-1;Trusted_Connection=True;MultipleActiveResultSets=true",
  "Movies:ServiceApiKey": "12345"
}
```

Run the following command from the directory in which the project file exists:

```
dotnet user-secrets list
```

The following output appears:

```
Movies:ConnectionString = Server=(localdb)\mssqllocaldb;Database=Movie-1;Trusted_Connection=True;MultipleActiveResultSets=true
Movies:ServiceApiKey = 12345
```

In the preceding example, a colon in the key names denotes the object hierarchy within `secrets.json`.

Assume the app's `secrets.json` file contains the following two secrets:

```
{
  "Movies:ConnectionString": "Server=(localdb)\\mssqllocaldb;Database=Movie-1;Trusted_Connection=True;MultipleActiveResultSets=true",
  "Movies:ServiceApiKey": "12345"
}
```

Run the following command from the directory in which the project file exists:

```
dotnet user-secrets remove "Movies:ConnectionString"
```

The app's `secrets.json` file was modified to remove the key-value pair associated with the `MoviesConnectionString` key:

```
{
  "Movies": {
    "ServiceApiKey": "12345"
  }
}
```

`dotnet user-secrets list` displays the following message:

```
Movies:ServiceApiKey = 12345
```

Assume the app's `secrets.json` file contains the following two secrets:

```
{
  "Movies:ConnectionString": "Server=(localdb)\\mssqllocaldb;Database=Movie-1;Trusted_Connection=True;MultipleActiveResultSets=true",
  "Movies:ServiceApiKey": "12345"
}
```

Run the following command from the directory in which the project file exists:

```
dotnet user-secrets clear
```

All user secrets for the app have been deleted from the `secrets.json` file:

```
{}
```

Running `dotnet user-secrets list` displays the following message:

```
No secrets configured for this application.
```

To manage user secrets in Visual Studio, right click the project in solution explorer and select **Manage User Secrets**:

![Image 3: Visual Studio showing Manage User Secrets](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets/_static/usvs.png?view=aspnetcore-10.0)

See [this GitHub issue](https://github.com/dotnet/AspNetCore.Docs/issues/27611).

Projects that target `Microsoft.NET.Sdk.Web` automatically include support for user secrets. For projects that target `Microsoft.NET.Sdk`, such as console applications, install the configuration extension and user secrets NuGet packages explicitly.

Using PowerShell:

```
Install-Package Microsoft.Extensions.Configuration
Install-Package Microsoft.Extensions.Configuration.UserSecrets
```

Using the .NET CLI:

```
dotnet add package Microsoft.Extensions.Configuration
dotnet add package Microsoft.Extensions.Configuration.UserSecrets
```

Once the packages are installed, [initialize the project](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets?view=aspnetcore-10.0#enable-secret-storage) and [set secrets](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets?view=aspnetcore-10.0#set-a-secret) the same way as for a web app. The following example shows a console application that retrieves the value of a secret that was set with the key "AppSecret":

```
using Microsoft.Extensions.Configuration;

namespace ConsoleApp;

class Program
{
    static void Main(string[] args)
    {
        IConfigurationRoot config = new ConfigurationBuilder()
            .AddUserSecrets<Program>()
            .Build();

        Console.WriteLine(config["AppSecret"]);
    }
}
```

*   See [this issue](https://github.com/dotnet/AspNetCore.Docs/issues/30378) and [this issue](https://github.com/dotnet/AspNetCore.Docs/issues/16328) for information on accessing user secrets from IIS.
*   [Configuration in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-10.0)
*   [Azure Key Vault configuration provider in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/key-vault-configuration?view=aspnetcore-10.0)

# Source: https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/connection-strings-and-configuration-files

Title: Connection Strings and Configuration Files - ADO.NET

URL Source: https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/connection-strings-and-configuration-files

Markdown Content:
Embedding connection strings in your application's code can lead to security vulnerabilities and maintenance problems. Unencrypted connection strings compiled into an application's source code can be viewed using the [Ildasm.exe (IL Disassembler)](https://learn.microsoft.com/en-us/dotnet/framework/tools/ildasm-exe-il-disassembler) tool. Moreover, if the connection string ever changes, your application must be recompiled. For these reasons, we recommend storing connection strings in an application configuration file.

Important

Microsoft recommends that you use the most secure authentication flow available. If you're connecting to Azure SQL, [Managed Identities for Azure resources](https://learn.microsoft.com/en-us/sql/connect/ado-net/sql/azure-active-directory-authentication#using-managed-identity-authentication) is the recommended authentication method.

Application configuration files contain settings that are specific to a particular application. For example, an ASP.NET application can have one or more **web.config** files, and a Windows application can have an optional **app.config** file. Configuration files share common elements, although the name and location of a configuration file vary depending on the application's host.

Connection strings can be stored as key/value pairs in the `connectionStrings` section of the `configuration` element of an application configuration file. Child elements include **add**, **clear**, and **remove**.

The following configuration file fragment demonstrates the schema and syntax for storing a connection string. The `name` attribute is a name that you provide to uniquely identify a connection string so that it can be retrieved at runtime. The `providerName` is the invariant name of the .NET Framework data provider, which is registered in the machine.config file.

```
<?xml version='1.0' encoding='utf-8'?>
  <configuration>
    <connectionStrings>
      <clear />
      <add name="Name"
       providerName="System.Data.ProviderName"
       connectionString="Valid Connection String;" />
    </connectionStrings>
  </configuration>
```

Note

You can save part of a connection string in a configuration file and use the [DbConnectionStringBuilder](https://learn.microsoft.com/en-us/dotnet/api/system.data.common.dbconnectionstringbuilder) class to complete it at runtime. This is useful in scenarios where you do not know elements of the connection string ahead of time, or when you don't want to save sensitive information in a configuration file. For more information, see [Connection String Builders](https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/connection-string-builders).

External configuration files are separate files that contain a fragment of a configuration file consisting of a single section. The external configuration file is then referenced by the main configuration file. Storing the `connectionStrings` section in a physically separate file is useful in situations where connection strings might be edited after the application is deployed. For example, the standard ASP.NET behavior is to restart an application domain when configuration files are modified, which results in state information being lost. However, modifying an external configuration file does not cause an application restart. External configuration files are not limited to ASP.NET; they can also be used by Windows applications. In addition, file access security and permissions can be used to restrict access to external configuration files. Working with external configuration files at runtime is transparent, and requires no special coding.

To store connection strings in an external configuration file, create a separate file that contains only the `connectionStrings` section. Do not include any additional elements, sections, or attributes. This example shows the syntax for an external configuration file.

```
<connectionStrings>
  <add name="Name"
   providerName="System.Data.ProviderName"
   connectionString="Valid Connection String;" />
</connectionStrings>
```

In the main application configuration file, you use the `configSource` attribute to specify the fully qualified name and location of the external file. This example refers to an external configuration file named `connections.config`.

```
<?xml version='1.0' encoding='utf-8'?>
<configuration>
    <connectionStrings configSource="connections.config"/>
</configuration>
```

.NET Framework 2.0 introduced new classes in the [System.Configuration](https://learn.microsoft.com/en-us/dotnet/api/system.configuration) namespace to simplify retrieving connection strings from configuration files at runtime. You can programmatically retrieve a connection string by name or by provider name.

Note

The **machine.config** file also contains a `connectionStrings` section, which contains connection strings used by Visual Studio. When retrieving connection strings by provider name from the **app.config** file in a Windows application, the connection strings in **machine.config** get loaded first, and then the entries from **app.config**. Adding `clear` immediately after the `connectionStrings` element removes all inherited references from the data structure in memory, so that only the connection strings defined in the local **app.config** file are considered.

Starting with .NET Framework 2.0, [ConfigurationManager](https://learn.microsoft.com/en-us/dotnet/api/system.configuration.configurationmanager) is used when working with configuration files on the local computer, replacing the deprecated [ConfigurationSettings](https://learn.microsoft.com/en-us/dotnet/api/system.configuration.configurationsettings) class. [WebConfigurationManager](https://learn.microsoft.com/en-us/dotnet/api/system.web.configuration.webconfigurationmanager) is used to work with ASP.NET configuration files. It is designed to work with configuration files on a Web server, and allows programmatic access to configuration file sections such as **system.web**.

Note

Accessing configuration files at runtime requires granting permissions to the caller; the required permissions depend on the type of application, configuration file, and location. For more information, see [WebConfigurationManager](https://learn.microsoft.com/en-us/dotnet/api/system.web.configuration.webconfigurationmanager) for ASP.NET applications, and [ConfigurationManager](https://learn.microsoft.com/en-us/dotnet/api/system.configuration.configurationmanager) for Windows applications.

You can use the [ConnectionStringSettingsCollection](https://learn.microsoft.com/en-us/dotnet/api/system.configuration.connectionstringsettingscollection) to retrieve connection strings from application configuration files. It contains a collection of [ConnectionStringSettings](https://learn.microsoft.com/en-us/dotnet/api/system.configuration.connectionstringsettings) objects, each of which represents a single entry in the `connectionStrings` section. Its properties map to connection string attributes, allowing you to retrieve a connection string by specifying the name or the provider name.

| Property | Description |
| --- | --- |
| [Name](https://learn.microsoft.com/en-us/dotnet/api/system.configuration.connectionstringsettings.name) | The name of the connection string. Maps to the `name` attribute. |
| [ProviderName](https://learn.microsoft.com/en-us/dotnet/api/system.configuration.connectionstringsettings.providername) | The fully qualified provider name. Maps to the `providerName` attribute. |
| [ConnectionString](https://learn.microsoft.com/en-us/dotnet/api/system.configuration.connectionstringsettings.connectionstring) | The connection string. Maps to the `connectionString` attribute. |

This example iterates through the [ConnectionStringSettingsCollection](https://learn.microsoft.com/en-us/dotnet/api/system.configuration.connectionstringsettingscollection) and displays the [ConnectionStringSettings.Name](https://learn.microsoft.com/en-us/dotnet/api/system.configuration.connectionstringsettings.name), [ConnectionStringSettings.ProviderName](https://learn.microsoft.com/en-us/dotnet/api/system.configuration.connectionstringsettings.providername), and [ConnectionStringSettings.ConnectionString](https://learn.microsoft.com/en-us/dotnet/api/system.configuration.connectionstringsettings.connectionstring) properties in the console window.

Note

System.Configuration.dll is not included in all project types, and you might need to set a reference to it in order to use the configuration classes. The name and location of a particular application configuration file varies by the type of application and the hosting process.

```
using System.Configuration;

static class Program
{
    static void Main()
    {
        GetConnectionStrings();
        Console.ReadLine();
    }

    static void GetConnectionStrings()
    {
        ConnectionStringSettingsCollection settings =
            ConfigurationManager.ConnectionStrings;

        foreach (ConnectionStringSettings cs in settings)
        {
            Console.WriteLine(cs.Name);
            Console.WriteLine(cs.ProviderName);
            Console.WriteLine(cs.ConnectionString);
        }
    }
}
```

This example demonstrates how to retrieve a connection string from a configuration file by specifying its name. The code creates a [ConnectionStringSettings](https://learn.microsoft.com/en-us/dotnet/api/system.configuration.connectionstringsettings) object, matching the supplied input parameter to the [ConnectionStrings](https://learn.microsoft.com/en-us/dotnet/api/system.configuration.configurationmanager.connectionstrings) name. If no matching name is found, the function returns `null` (`Nothing` in Visual Basic).

```
// Retrieves a connection string by name.
// Returns null if the name is not found.
static string? GetConnectionStringByName(string name)
{
    // Look for the name in the connectionStrings section.
    ConnectionStringSettings? settings =
        ConfigurationManager.ConnectionStrings[name];

    // If found, return the connection string (otherwise return null)
    return settings?.ConnectionString;
}
```

This example demonstrates how to retrieve a connection string by specifying the provider-invariant name in the format _System.Data.ProviderName_. The code iterates through the [ConnectionStringSettingsCollection](https://learn.microsoft.com/en-us/dotnet/api/system.configuration.connectionstringsettingscollection) and returns the connection string for the first [ProviderName](https://learn.microsoft.com/en-us/dotnet/api/system.configuration.connectionstringsettings.providername) found. If the provider name is not found, the function returns `null` (`Nothing` in Visual Basic).

```
// Retrieve a connection string by specifying the providerName.
// Assumes one connection string per provider in the config file.
static string? GetConnectionStringByProvider(string providerName)
{
    // Get the collection of connection strings.
    ConnectionStringSettingsCollection? settings =
        ConfigurationManager.ConnectionStrings;

    // Walk through the collection and return the first
    // connection string matching the providerName.
    if (settings != null)
    {
        foreach (ConnectionStringSettings cs in settings)
        {
            if (cs.ProviderName == providerName)
            {
                return cs.ConnectionString;
            }
        }
    }
    return null;
}
```

ASP.NET 2.0 introduced a new feature, called _protected configuration_, that enables you to encrypt sensitive information in a configuration file. Although primarily designed for ASP.NET, protected configuration can also be used to encrypt configuration file sections in Windows applications.

The following configuration file fragment shows the `connectionStrings` section after it has been encrypted. The `configProtectionProvider` specifies the protected configuration provider used to encrypt and decrypt the connection strings. The `EncryptedData` section contains the cipher text.

```
<connectionStrings configProtectionProvider="DataProtectionConfigurationProvider">
  <EncryptedData>
    <CipherData>
      <CipherValue>AQAAANCMnd8BFdERjHoAwE/Cl+sBAAAAH2... </CipherValue>
    </CipherData>
  </EncryptedData>
</connectionStrings>
```

When the encrypted connection string is retrieved at runtime, .NET Framework uses the specified provider to decrypt the `CipherValue` and make it available to your application. You do not need to write any additional code to manage the decryption process.

Protected configuration providers are registered in the `configProtectedData` section of the **machine.config** file on the local computer, as shown in the following fragment, which shows the two protected configuration providers supplied with .NET Framework. The values shown here have been truncated for readability.

```
<configProtectedData defaultProvider="RsaProtectedConfigurationProvider">
  <providers>
    <add name="RsaProtectedConfigurationProvider"
      type="System.Configuration.RsaProtectedConfigurationProvider" />
    <add name="DataProtectionConfigurationProvider"
      type="System.Configuration.DpapiProtectedConfigurationProvider" />
  </providers>
</configProtectedData>
```

You can configure additional protected configuration providers by adding them to the **machine.config** file. You can also create your own protected configuration provider by inheriting from the [ProtectedConfigurationProvider](https://learn.microsoft.com/en-us/dotnet/api/system.configuration.protectedconfigurationprovider) abstract base class. The following table describes the two configuration files included with .NET Framework.

| Provider | Description |
| --- | --- |
| [RsaProtectedConfigurationProvider](https://learn.microsoft.com/en-us/dotnet/api/system.configuration.rsaprotectedconfigurationprovider) | Uses the RSA encryption algorithm to encrypt and decrypt data. The RSA algorithm can be used for both public key encryption and digital signatures. It is also known as "public key" or asymmetrical encryption because it employs two different keys. You can use the [ASP.NET IIS Registration Tool (Aspnet_regiis.exe)](https://learn.microsoft.com/en-us/previous-versions/dotnet/netframework-3.5/k6h9cz8h(v=vs.90)) to encrypt sections in a Web.config file and manage the encryption keys. ASP.NET decrypts the configuration file when it processes the file. The identity of the ASP.NET application must have read access to the encryption key that is used to encrypt and decrypt the encrypted sections. |
| [DpapiProtectedConfigurationProvider](https://learn.microsoft.com/en-us/dotnet/api/system.configuration.dpapiprotectedconfigurationprovider) | Uses the Windows Data Protection API (DPAPI) to encrypt configuration sections. It uses the Windows built-in cryptographic services and can be configured for either machine-specific or user-account-specific protection. Machine-specific protection is useful for multiple applications on the same server that need to share information. User-account-specific protection can be used with services that run with a specific user identity, such as a shared hosting environment. Each application runs under a separate identity which restricts access to resources such as files and databases. |

Both providers offer strong encryption of data. However, if you are planning to use the same encrypted configuration file on multiple servers, such as a Web farm, only the [RsaProtectedConfigurationProvider](https://learn.microsoft.com/en-us/dotnet/api/system.configuration.rsaprotectedconfigurationprovider) enables you to export the encryption keys used to encrypt the data and import them on another server. For more information, see [Importing and Exporting Protected Configuration RSA Key Containers](https://learn.microsoft.com/en-us/previous-versions/aspnet/yxw286t2(v=vs.100)).

The [System.Configuration](https://learn.microsoft.com/en-us/dotnet/api/system.configuration) namespace provides classes to work with configuration settings programmatically. The [ConfigurationManager](https://learn.microsoft.com/en-us/dotnet/api/system.configuration.configurationmanager) class provides access to machine, application, and user configuration files. If you are creating an ASP.NET application, you can use the [WebConfigurationManager](https://learn.microsoft.com/en-us/dotnet/api/system.web.configuration.webconfigurationmanager) class, which provides the same functionality while also allowing you to access settings that are unique to ASP.NET applications, such as those found in **<system.web>**.

Note

The [System.Security.Cryptography](https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography) namespace contains classes that provide additional options for encrypting and decrypting data. Use these classes if you require cryptographic services that are not available using protected configuration. Some of these classes are wrappers for the unmanaged Microsoft CryptoAPI, while others are purely managed implementations.

This example demonstrates how to toggle encrypting the `connectionStrings` section in an **app.config** file for a Windows application. In this example, the procedure takes the name of the application as an argument, for example, "MyApplication.exe". The **app.config** file is then encrypted and copied to the folder that contains the executable under the name of "MyApplication.exe.config".

The code uses the [OpenExeConfiguration](https://learn.microsoft.com/en-us/dotnet/api/system.configuration.configurationmanager.openexeconfiguration) method to open the **app.config** file for editing, and the [GetSection](https://learn.microsoft.com/en-us/dotnet/api/system.configuration.configurationmanager.getsection) method returns the `connectionStrings` section. The code then checks the [IsProtected](https://learn.microsoft.com/en-us/dotnet/api/system.configuration.sectioninformation.isprotected) property, calling the [ProtectSection](https://learn.microsoft.com/en-us/dotnet/api/system.configuration.sectioninformation.protectsection) to encrypt the section if it is not encrypted. The [UnprotectSection](https://learn.microsoft.com/en-us/dotnet/api/system.configuration.sectioninformation.unprotectsection) method is invoked to decrypt the section. (The connection string can only be decrypted on the computer on which it was encrypted.) The [Save](https://learn.microsoft.com/en-us/dotnet/api/system.configuration.configuration.save) method completes the operation and saves the changes.

You must add a reference to `System.Configuration.dll` in your project for the code to run.

Important

Microsoft recommends that you use the most secure authentication flow available. If you're connecting to Azure SQL, [Managed Identities for Azure resources](https://learn.microsoft.com/en-us/sql/connect/ado-net/sql/azure-active-directory-authentication#using-managed-identity-authentication) is the recommended authentication method.

```
static void ToggleConfigEncryption(string exeFile)
{
    // Get the application path needed to obtain
    // the application configuration file.

    // Takes the executable file name without the
    // .config extension.
    var exePath = exeFile.Replace(".config", "");

    try
    {
        // Open the configuration file and retrieve
        // the connectionStrings section.
        Configuration config = ConfigurationManager.
            OpenExeConfiguration(exePath);

        var section =
            config.GetSection("connectionStrings")
            as ConnectionStringsSection;

        if (section != null)
        {
            if (section.SectionInformation.IsProtected)
            {
                // Remove encryption.
                section.SectionInformation.UnprotectSection();
            }
            else
            {
                // Encrypt the section.
                section.SectionInformation.ProtectSection(
                    "DataProtectionConfigurationProvider");
            }
        }
        // Save the current configuration.
        config.Save();

        Console.WriteLine($"Protected={section?.SectionInformation.IsProtected}");
    }
    catch (Exception ex)
    {
        Console.WriteLine(ex.Message);
    }
}
```

This example uses the [OpenWebConfiguration](https://learn.microsoft.com/en-us/dotnet/api/system.web.configuration.webconfigurationmanager.openwebconfiguration) method of the `WebConfigurationManager`. In this case, you can supply the relative path to the **Web.config** file by using a tilde. The code requires a reference to the `System.Web.Configuration` class.

```
static void ToggleWebEncrypt()
{
    // Open the Web.config file.
    Configuration config = WebConfigurationManager.
        OpenWebConfiguration("~");

    // Get the connectionStrings section.
    var section =
        config.GetSection("connectionStrings")
        as ConnectionStringsSection;

    // Toggle encryption.
    if (section.SectionInformation.IsProtected)
    {
        section.SectionInformation.UnprotectSection();
    }
    else
    {
        section.SectionInformation.ProtectSection(
            "DataProtectionConfigurationProvider");
    }

    // Save changes to the Web.config file.
    config.Save();
}
```

For more information about securing ASP.NET applications, see [Securing ASP.NET web sites](https://learn.microsoft.com/en-us/previous-versions/aspnet/91f66yxt(v=vs.100)).

* [Connection String Builders](https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/connection-string-builders)
* [Protecting Connection Information](https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/protecting-connection-information)
* [Using the Configuration Classes](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2008/ms228063(v=vs.90))
* [Configuring Apps](https://learn.microsoft.com/en-us/dotnet/framework/configure-apps/)
* [ASP.NET Web Site Administration](https://learn.microsoft.com/en-us/previous-versions/aspnet/6hy1xzbw(v=vs.100))
* [ADO.NET Overview](https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/ado-net-overview)

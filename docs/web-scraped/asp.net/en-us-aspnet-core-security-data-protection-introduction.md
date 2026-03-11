# Source: https://learn.microsoft.com/en-us/aspnet/core/security/data-protection/introduction?view=aspnetcore-10.0

Title: ASP.NET Core Data Protection Overview

URL Source: https://learn.microsoft.com/en-us/aspnet/core/security/data-protection/introduction?view=aspnetcore-10.0

Markdown Content:
ASP.NET Core provides a cryptographic API to protect data, including key management and rotation.

Web apps often need to store sensitive data. The Windows data protection API ([DPAPI](https://learn.microsoft.com/en-us/dotnet/standard/security/how-to-use-data-protection)) isn't intended for use in web apps.

The ASP.NET Core data protection stack was designed to:

*   Provide a built in solution for most Web scenarios.
*   Address many of the deficiencies of the previous encryption system.
*   Serve as the replacement for the `<machineKey>` element in ASP.NET 1.x - 4.x.

_I need to persist trusted information for later retrieval, but I don't trust the persistence mechanism._ In web terms, this might be written as _I need to round-trip trusted state via an untrusted client._

Authenticity, integrity, and tamper-proofing is a requirement. The canonical example of this is an authentication cookie or bearer token. The server generates an _**I am Groot and have xyz permissions**_ token and sends it to the client. The client presents that token back to the server, but the server needs some kind of assurance that the client hasn't forged the token.

Confidentiality is a requirement. Since the persisted state is trusted by the server, this state could contain information that shouldn't be disclosed to an untrusted client. For example:

*   A file path.
*   A permission.
*   A handle or other indirect reference.
*   Some server-specific data.

Isolation is a requirement. Since modern apps are componentized, individual components want to take advantage of this system without regard to other components in the system. For instance, consider a bearer token component using this stack. It should operate without any interference, for example, from an anti-CSRF mechanism also using the same stack.

Some common assumptions can narrow the scope of requirements:

*   All services operating within the cryptosystem are equally trusted.
*   The data doesn't need to be generated or consumed outside of the services under our direct control.
*   Operations must be fast since each request to the web service might go through the cryptosystem one or more times. The speed requirement makes symmetric cryptography ideal. Asymmetric cryptography isn't used until it's required.

ASP.NET Core data protection is an [easy to use](https://learn.microsoft.com/en-us/aspnet/core/security/data-protection/using-data-protection?view=aspnetcore-10.0) data protection stack. It's based on the following principles:

*   Ease of configuration. The system strives for zero configuration. In situations where developers need to configure a specific aspect, such as the key repository, those specific configurations aren't difficult.
*   Offer a basic consumer-facing API. The APIs are straight forward to use correctly and difficult to use incorrectly.
*   Developers don't have to learn key management principles. The system handles algorithm selection and key lifetime on behalf of the developer. The developer doesn't have access to the raw key material.
*   Keys are protected at rest as much as possible. The system figures out an appropriate default protection mechanism and applies it automatically.

The data protection APIs aren't primarily intended for indefinite persistence of confidential payloads. Other technologies, such as [Windows CNG DPAPI](https://learn.microsoft.com/en-us/windows/win32/seccng/cng-dpapi) and [Azure Rights Management](https://learn.microsoft.com/en-us/rights-management/) are more suited to the scenario of indefinite storage. They have correspondingly strong key management capabilities. That said, the ASP.NET Core data protection APIs can be used for long-term protection of confidential data.

The data protection system provides APIs that target three main audiences:

1.   The [consumer APIs](https://learn.microsoft.com/en-us/aspnet/core/security/data-protection/consumer-apis/overview?view=aspnetcore-10.0) target application and framework developers.

_I don't want to learn about how the stack operates or about how it's configured. I just want to perform some operation with high probability of using the APIs successfully._

2.   The [configuration APIs](https://learn.microsoft.com/en-us/aspnet/core/security/data-protection/configuration/overview?view=aspnetcore-10.0) target app developers and system administrators.

_I need to tell the data protection system that my environment requires non-default paths or settings._

3.   The extensibility APIs target developers in charge of implementing custom policy. Usage of these APIs is limited to rare situations and developers with security experience.

_I need to replace an entire component within the system because I have truly unique behavioral requirements. I'm willing to learn uncommonly used parts of the API surface in order to build a plugin that fulfills my requirements._

The data protection stack consists of five packages:

*   [Microsoft.AspNetCore.DataProtection.Abstractions](https://www.nuget.org/packages/Microsoft.AspNetCore.DataProtection.Abstractions/) contains:

    *   [IDataProtectionProvider](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.dataprotection.idataprotectionprovider) and [IDataProtector](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.dataprotection.idataprotector) interfaces to create data protection services.
    *   Useful extension methods for working with these types. for example, [IDataProtector.Protect](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.dataprotection.idataprotector.protect)

If the data protection system is instantiated elsewhere and you're consuming the API, reference `Microsoft.AspNetCore.DataProtection.Abstractions`.

*   [Microsoft.AspNetCore.DataProtection](https://www.nuget.org/packages/Microsoft.AspNetCore.DataProtection/) contains the core implementation of the data protection system, including:

    *   Core cryptographic operations.
    *   Key management.
    *   Configuration and extensibility.

To instantiate the data protection system, reference `Microsoft.AspNetCore.DataProtection`. You might need to reference the data protection system when:

    *   Adding it to an [IServiceCollection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection).
    *   Modifying or extending its behavior.

*   [Microsoft.AspNetCore.DataProtection.Extensions](https://www.nuget.org/packages/Microsoft.AspNetCore.DataProtection.Extensions/) contains additional APIs which developers might find useful but which don't belong in the core package. For instance, this package contains:

    *   Factory methods to instantiate the data protection system to store keys at a location on the file system without dependency injection. See [DataProtectionProvider](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.dataprotection.dataprotectionprovider).
    *   Extension methods for limiting the lifetime of protected payloads. See [ITimeLimitedDataProtector](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.dataprotection.itimelimiteddataprotector).

*   [Microsoft.AspNetCore.DataProtection.SystemWeb](https://www.nuget.org/packages/Microsoft.AspNetCore.DataProtection.SystemWeb/) can be installed into an existing ASP.NET 4.x app to redirect its `<machineKey>` operations to use the new ASP.NET Core data protection stack. For more information, see [Replace the ASP.NET machineKey in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/data-protection/compatibility/replacing-machinekey?view=aspnetcore-10.0).

*   [Microsoft.AspNetCore.Cryptography.KeyDerivation](https://www.nuget.org/packages/Microsoft.AspNetCore.Cryptography.KeyDerivation/) provides an implementation of the PBKDF2 password hashing routine and can be used by systems that must handle user passwords securely. For more information, see [Hash passwords in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/data-protection/consumer-apis/password-hashing?view=aspnetcore-10.0).

*   [Get started with the Data Protection APIs in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/data-protection/using-data-protection?view=aspnetcore-10.0)
*   [Host ASP.NET Core in a web farm](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/web-farm?view=aspnetcore-10.0)

ASP.NET Core provides a cryptographic API to protect data, including key management and rotation.

Web apps often need to store sensitive data. The Windows data protection API ([DPAPI](https://learn.microsoft.com/en-us/dotnet/standard/security/how-to-use-data-protection)) isn't intended for use in web apps.

The ASP.NET Core data protection stack was designed to:

*   Provide a built in solution for most Web scenarios.
*   Address many of the deficiencies of the previous encryption system.
*   Serve as the replacement for the `<machineKey>` element in ASP.NET 1.x - 4.x.

_I need to persist trusted information for later retrieval, but I don't trust the persistence mechanism._ In web terms, this might be written as _I need to round-trip trusted state via an untrusted client._

Authenticity, integrity, and tamper-proofing is a requirement. The canonical example of this is an authentication cookie or bearer token. The server generates an _**I am Groot and have xyz permissions**_ token and sends it to the client. The client presents that token back to the server, but the server needs some kind of assurance that the client hasn't forged the token.

Confidentiality is a requirement. Since the persisted state is trusted by the server, this state could contain information that shouldn't be disclosed to an untrusted client. For example:

*   A file path.
*   A permission.
*   A handle or other indirect reference.
*   Some server-specific data.

Isolation is a requirement. Since modern apps are componentized, individual components want to take advantage of this system without regard to other components in the system. For instance, consider a bearer token component using this stack. It should operate without any interference, for example, from an anti-CSRF mechanism also using the same stack.

Some common assumptions can narrow the scope of requirements:

*   All services operating within the cryptosystem are equally trusted.
*   The data doesn't need to be generated or consumed outside of the services under our direct control.
*   Operations must be fast since each request to the web service might go through the cryptosystem one or more times. The speed requirement makes symmetric cryptography ideal. Asymmetric cryptography isn't used until it's required.

ASP.NET Core data protection is an [easy to use](https://learn.microsoft.com/en-us/aspnet/core/security/data-protection/using-data-protection?view=aspnetcore-10.0) data protection stack. It's based on the following principles:

*   Ease of configuration. The system strives for zero configuration. In situations where developers need to configure a specific aspect, such as the key repository, those specific configurations aren't difficult.
*   Offer a basic consumer-facing API. The APIs are straight forward to use correctly and difficult to use incorrectly.
*   Developers don't have to learn key management principles. The system handles algorithm selection and key lifetime on behalf of the developer. The developer doesn't have access to the raw key material.
*   Keys are protected at rest as much as possible. The system figures out an appropriate default protection mechanism and applies it automatically.

The data protection APIs aren't primarily intended for indefinite persistence of confidential payloads. Other technologies, such as [Windows CNG DPAPI](https://learn.microsoft.com/en-us/windows/win32/seccng/cng-dpapi) and [Azure Rights Management](https://learn.microsoft.com/en-us/rights-management/) are more suited to the scenario of indefinite storage. They have correspondingly strong key management capabilities. That said, the ASP.NET Core data protection APIs can be used for long-term protection of confidential data.

The data protection system provides APIs that target three main audiences:

1.   The [consumer APIs](https://learn.microsoft.com/en-us/aspnet/core/security/data-protection/consumer-apis/overview?view=aspnetcore-10.0) target application and framework developers.

_I don't want to learn about how the stack operates or about how it's configured. I just want to perform some operation with high probability of using the APIs successfully._

2.   The [configuration APIs](https://learn.microsoft.com/en-us/aspnet/core/security/data-protection/configuration/overview?view=aspnetcore-10.0) target app developers and system administrators.

_I need to tell the data protection system that my environment requires non-default paths or settings._

3.   The extensibility APIs target developers in charge of implementing custom policy. Usage of these APIs is limited to rare situations and developers with security experience.

_I need to replace an entire component within the system because I have truly unique behavioral requirements. I'm willing to learn uncommonly used parts of the API surface in order to build a plugin that fulfills my requirements._

The data protection stack consists of five packages:

*   [Microsoft.AspNetCore.DataProtection.Abstractions](https://www.nuget.org/packages/Microsoft.AspNetCore.DataProtection.Abstractions/) contains:

    *   [IDataProtectionProvider](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.dataprotection.idataprotectionprovider) and [IDataProtector](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.dataprotection.idataprotector) interfaces to create data protection services.
    *   Useful extension methods for working with these types. for example, [IDataProtector.Protect](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.dataprotection.idataprotector.protect)

If the data protection system is instantiated elsewhere and you're consuming the API, reference `Microsoft.AspNetCore.DataProtection.Abstractions`.

*   [Microsoft.AspNetCore.DataProtection](https://www.nuget.org/packages/Microsoft.AspNetCore.DataProtection/) contains the core implementation of the data protection system, including:

    *   Core cryptographic operations.
    *   Key management.
    *   Configuration and extensibility.

To instantiate the data protection system, reference `Microsoft.AspNetCore.DataProtection`. You might need to reference the data protection system when:

    *   Adding it to an [IServiceCollection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection).
    *   Modifying or extending its behavior.

*   [Microsoft.AspNetCore.DataProtection.Extensions](https://www.nuget.org/packages/Microsoft.AspNetCore.DataProtection.Extensions/) contains additional APIs which developers might find useful but which don't belong in the core package. For instance, this package contains:

    *   Factory methods to instantiate the data protection system to store keys at a location on the file system without dependency injection. See [DataProtectionProvider](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.dataprotection.dataprotectionprovider).
    *   Extension methods for limiting the lifetime of protected payloads. See [ITimeLimitedDataProtector](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.dataprotection.itimelimiteddataprotector).

*   [Microsoft.AspNetCore.DataProtection.SystemWeb](https://www.nuget.org/packages/Microsoft.AspNetCore.DataProtection.SystemWeb/) can be installed into an existing ASP.NET 4.x app to redirect its `<machineKey>` operations to use the new ASP.NET Core data protection stack. For more information, see [Replace the ASP.NET machineKey in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/data-protection/compatibility/replacing-machinekey?view=aspnetcore-10.0).

*   [Microsoft.AspNetCore.Cryptography.KeyDerivation](https://www.nuget.org/packages/Microsoft.AspNetCore.Cryptography.KeyDerivation/) provides an implementation of the PBKDF2 password hashing routine and can be used by systems that must handle user passwords securely. For more information, see [Hash passwords in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/data-protection/consumer-apis/password-hashing?view=aspnetcore-10.0).

*   [Get started with the Data Protection APIs in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/data-protection/using-data-protection?view=aspnetcore-10.0)
*   [Host ASP.NET Core in a web farm](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/web-farm?view=aspnetcore-10.0)

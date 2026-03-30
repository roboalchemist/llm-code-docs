# Source: https://help.cloudsmith.io/docs/signing-nuget-packages.md

# Signing NuGet Packages

Cloudsmith supports natively signing all NuGet packages using an X.509 certificate, enabling consumers to verify package repository signatures in native tooling or the NuGet CLI command, ensuring the integrity and authenticity of the packages.

## Getting started

To get started, navigate to Repository Settings >> Miscellaneous, and check the box "NuGet Native Signing Enabled?"

<Image align="center" src="https://files.readme.io/0f5e729ecda147b402aa28830e82378540209df738d30dea93d0e4a3685b7584-nuget-signing.png" />

> 📘 Signing of existing NuGet packages
>
> Packages uploaded prior to enabling NuGet Native Signing will not be signed or have a certificate in the index. Once this setting is enabled, you will need to resync existing NuGet packages to sign them.

## How it works

When native NuGet signing is enabled for a Cloudsmith repository, a unique X.509 certificate is issued for that repository.

When a NuGet package is uploaded or resynced to that repository, Cloudsmith will create a repository signature. The certificate will be available in the `RepositorySignatures` resource in the [service index](https://learn.microsoft.com/en-us/nuget/api/service-index). If a NuGet package contains an author signature, Cloudsmith will countersign the package.

If the repository upstream NuGet repositories configured, Cloudsmith will index the RepositorySignature endpoint from the Nuget service index. The upstream repository's signing certificates will then be available for client-side verification as well.

### Client-side verification

To enable client-side verification, the trusted certificates need to be added to the consumer's machine. Cloudsmith issues signing certificates using our own Certificate Authority. The Certificate Authority chain will need to be added to NuGet's trusted roots bundle.

#### Linux and MacOS

For Linux and MacOS, this is located at: `/usr/local/share/dotnet/sdk/\<NUGET_SDK_VERSION>/trustedroots/codesignctl.pem`

#### Windows

For Windows, this is managed by the operating system. Please reference Microsoft's [Trusted Root Certification Authorities Certificate Store](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/trusted-root-certification-authorities-certificate-store) for more information.

You can download Cloudsmith’s root Certificate Authority chain by going to the Key Management tab in your repository or by calling the [x509-rsa API endpoint](https://help.cloudsmith.io/reference/repos_x509_rsa_list).
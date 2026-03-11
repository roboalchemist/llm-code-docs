# Source: https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/versions-and-dependencies

Title: .NET Framework & Windows OS versions - .NET Framework

URL Source: https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/versions-and-dependencies

Markdown Content:
Each version of .NET Framework contains the common language runtime (CLR), the base class libraries, and other managed libraries. This article describes the key features of .NET Framework by version, provides information about the underlying CLR versions and associated development environments, and identifies the versions that are installed by the Windows operating system (OS).

Each new version of .NET Framework adds new features but retains features from previous versions.

Note

.NET Framework is serviced independently from Windows updates with security and reliability bug fixes. In general, security updates are released quarterly. .NET Framework will continue to be included with Windows, with no plans to remove it. You don't need to migrate your .NET Framework apps, but for new development, use [.NET instead of .NET Framework](https://learn.microsoft.com/en-us/dotnet/core/introduction).

The CLR is identified by its own version number. The .NET Framework version number is incremented at each release, but the CLR version is not always incremented. For example, .NET Framework 4, 4.5, and later releases include CLR 4, but .NET Framework 2.0, 3.0, and 3.5 include CLR 2.0. (There was no version 3 of the CLR.)

Tip

* For a complete list of supported operating systems, see [System requirements](https://learn.microsoft.com/en-us/dotnet/framework/get-started/system-requirements).
* For downloads, see [Install .NET Framework for developers](https://learn.microsoft.com/en-us/dotnet/framework/install/guide-for-developers).
* For information about determining which versions of .NET Framework are installed on a computer, see [How to determine which .NET Framework versions are installed](https://learn.microsoft.com/en-us/dotnet/framework/install/how-to-determine-which-versions-are-installed).

The tables that follow summarize .NET Framework version history and correlate each version with Visual Studio, Windows, and Windows Server. Visual Studio supports multi-targeting, so you're not limited to the version of .NET Framework that's listed.

* The check mark icon ✔️ denotes OS versions on which .NET Framework is installed by default.
* The plus sign icon ➕ denotes OS versions on which .NET Framework doesn't come installed but can be installed.
* The asterisk ***** denotes OS versions on which .NET Framework (whether preinstalled or not) must be enabled [in Control Panel](https://learn.microsoft.com/en-us/dotnet/framework/install/dotnet-35-windows#enable-net-framework-35-on-windows) or, for Windows Server, through the [Server Manager](https://learn.microsoft.com/en-us/dotnet/framework/install/dotnet-35-windows#enable-net-framework-35-on-windows-server).

Jump to:

* [.NET Framework 4.8.1](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/versions-and-dependencies#net-framework-481)
* [.NET Framework 4.8](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/versions-and-dependencies#net-framework-48)
* [.NET Framework 4.7.2](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/versions-and-dependencies#net-framework-472)
* [.NET Framework 4.7.1](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/versions-and-dependencies#net-framework-471)
* [.NET Framework 4.7](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/versions-and-dependencies#net-framework-47)
* [.NET Framework 4.6.2](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/versions-and-dependencies#net-framework-462)
* [.NET Framework 4.6.1](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/versions-and-dependencies#net-framework-461)
* [.NET Framework 4.6](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/versions-and-dependencies#net-framework-46)
* [.NET Framework 4.5.2](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/versions-and-dependencies#net-framework-452)
* [.NET Framework 4.5.1](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/versions-and-dependencies#net-framework-451)
* [.NET Framework 4.5](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/versions-and-dependencies#net-framework-45)
* [.NET Framework 4](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/versions-and-dependencies#net-framework-4)
* [.NET Framework 3.5](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/versions-and-dependencies#net-framework-35)
* [.NET Framework 3.0](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/versions-and-dependencies#net-framework-30)
* [.NET Framework 2.0](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/versions-and-dependencies#net-framework-20)
* [.NET Framework 1.1](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/versions-and-dependencies#net-framework-11)
* [.NET Framework 1.0](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/versions-and-dependencies#net-framework-10)

* [New features](https://learn.microsoft.com/en-us/dotnet/framework/whats-new/#whats-new-in-net-framework-481)
* New accessibility features
* [Release notes](https://github.com/Microsoft/dotnet/tree/main/releases/net481/README.md)

|  | Versions |
| --- | --- |
| CLR | 4 |
| Windows | ✔️ 11 September 2025 Release (version 26200) ✔️ 11 October 2024 Release (version 26100) ✔️ 11 October 2023 Release (version 22631) ✔️ 11 September 2022 Release (version 22621) ➕ 11 October 2021 Release (version 22000) ➕ 10 October 2022 Update (22H2) ➕ 10 November 2021 Update ➕ 10 May 2021 Update ➕ 10 October 2020 Update |
| Windows Server | ✔️ Windows Server 2025 ➕ Windows Server 2022 |

To determine the installed .NET version, use the following `Release` DWORD:

* 533509 (Windows 11 September 2025 Release)
* 533320 (Windows 11 September 2022 Release and Windows 11 October 2023 Release)
* 533325 (all other OS versions)

For more information, see [instructions](https://learn.microsoft.com/en-us/dotnet/framework/install/how-to-determine-which-versions-are-installed).

* [New features](https://learn.microsoft.com/en-us/dotnet/framework/whats-new/#whats-new-in-net-framework-48)
* [New in accessibility](https://learn.microsoft.com/en-us/dotnet/framework/whats-new/whats-new-in-accessibility#whats-new-in-accessibility-in-net-framework-48)
* [Release notes](https://github.com/Microsoft/dotnet/tree/main/releases/net48/README.md)

|  | Versions |
| --- | --- |
| CLR | 4 |
| Windows | ✔️ 11 October 2021 Release (Version 22000) ✔️ 10 October 2022 Update (22H2) ✔️ 10 November 2021 Update ✔️ 10 May 2021 Update ✔️ 10 October 2020 Update ✔️ 10 May 2020 Update ✔️ 10 November 2019 Update ✔️ 10 May 2019 Update ➕ 10 October 2018 Update (Version 1809) ➕ 10 April 2018 Update (Version 1803) ➕ 10 Fall Creators Update (Version 1709) ➕ 10 Creators Update (Version 1703) ➕ 10 Anniversary Update (Version 1607) ➕ 8.1 ➕7 |
| Windows Server | ✔️ Windows Server 2022 ➕ Windows Server 2019 ➕ Windows Server, version 1809 ➕ Windows Server, version 1803 ➕ 2016 ➕ 2012 R2 ➕ 2012 ➕ 2008 R2 SP1 |

To determine the installed .NET version, use the following `Release` DWORD:

* 528449 (Windows 11 and Windows Server 2022)
* 528372 (Windows 10 May 2020 Update and Windows 10 October 2020 Update and Windows 10 May 2021 Update)
* 528040 (Windows 10 May 2019 Update and Windows 10 November 2019 Update)
* 528049 (all other OS versions)

For more information, see [instructions](https://learn.microsoft.com/en-us/dotnet/framework/install/how-to-determine-which-versions-are-installed).

* [New features](https://learn.microsoft.com/en-us/dotnet/framework/whats-new/#whats-new-in-net-framework-472)
* [New in accessibility](https://learn.microsoft.com/en-us/dotnet/framework/whats-new/whats-new-in-accessibility#whats-new-in-accessibility-in-net-framework-472)
* [Release notes](https://github.com/Microsoft/dotnet/tree/main/releases/net472/README.md)

|  | Versions |
| --- | --- |
| CLR | 4 |
| Included in Visual Studio | 2019† |
| Windows | ✔️ 10 October 2018 Update (Version 1809) ✔️ 10 April 2018 Update (Version 1803) ➕ 10 Fall Creators Update (Version 1709) ➕ 10 Creators Update (Version 1703) ➕ 10 Anniversary Update (Version 1607) ➕ 8.1 ➕7 |
| Windows Server | ✔️ Windows Server 2019 ✔️ Windows Server, version 1809 ✔️ Windows Server, version 1803 ➕ Windows Server, version 1709 ➕ 2016 ➕ 2012 R2 ➕ 2012 ➕ 2008 R2 SP1 |

†Requires installing the **.NET desktop development**, **ASP.NET and web development**, **Azure development**, **Office/SharePoint development**, **Mobile development with .NET**, or **.NET Core cross-platform development** workloads.

To determine the installed .NET version, use the following `Release` DWORD:

* 461814 (Windows 10 October 2018 Update)
* 461808 (Windows 10 April 2018 Update and Windows Server, version 1803)
* 461814 (all other OS versions)

For more information, see [instructions](https://learn.microsoft.com/en-us/dotnet/framework/install/how-to-determine-which-versions-are-installed).

* [New features](https://learn.microsoft.com/en-us/dotnet/framework/whats-new/#whats-new-in-net-framework-471)
* [New in accessibility](https://learn.microsoft.com/en-us/dotnet/framework/whats-new/whats-new-in-accessibility#whats-new-in-accessibility-in-net-framework-471)
* [Release notes](https://github.com/Microsoft/dotnet/tree/main/releases/net471/README.md)

|  | Versions |
| --- | --- |
| CLR | 4 |
| Windows | ✔️ 10 Fall Creators Update (Version 1709) ➕ 10 Creators Update (Version 1703) ➕ 10 Anniversary Update (Version 1607) ➕ 8.1 ➕7 |
| Windows Server | ➕ Windows Server, version 1803 ✔️ Windows Server, version 1709 ➕ 2016 ➕ 2012 R2 ➕ 2012 ➕ 2008 R2 SP1 |

To determine the installed .NET version, use the following `Release` DWORD:

* 461308 (Windows 10 Creators Update and Windows Server, version 1709)
* 461310 (all other OS versions)

For more information, see [instructions](https://learn.microsoft.com/en-us/dotnet/framework/install/how-to-determine-which-versions-are-installed).

* [New features](https://learn.microsoft.com/en-us/dotnet/framework/whats-new/#whats-new-in-net-framework-47)
* [Release notes](https://github.com/Microsoft/dotnet/tree/main/releases/net47/README.md)

|  | Versions |
| --- | --- |
| CLR | 4 |
| Windows | ✔️ 10 Creators Update (Version 1703) ➕ 10 Anniversary Update (Version 1607) ➕ 8.1 ➕7 |
| Windows Server | ➕ 2016 ➕ 2012 R2 ➕ 2012 ➕ 2008 R2 SP1 |

To determine the installed .NET version, use the following `Release` DWORD:

* 460798 (Windows 10 Creators Update)
* 460805 (all other OS versions)

For more information, see [instructions](https://learn.microsoft.com/en-us/dotnet/framework/install/how-to-determine-which-versions-are-installed).

* [New features](https://learn.microsoft.com/en-us/dotnet/framework/whats-new/#whats-new-in-net-framework-462)
* [Release notes](https://github.com/Microsoft/dotnet/tree/main/releases/net462/README.md)

|  | Versions |
| --- | --- |
| CLR | 4 |
| Windows | ✔️ 10 Anniversary Update (Version 1607) ➕ 10 November Update (Version 1511) ➕ 10 ➕ 8.1 ➕ 7 |
| Windows Server | ✔️ 2016 ➕ 2012 R2 ➕ 2012 ➕ 2008 R2 SP1 ➕ 2008 SP2 |

To determine the installed .NET version, use the following `Release` DWORD:

* 394802 (Windows 10 Anniversary Update and Windows Server 2016)
* 394806 (all other OS versions)

For more information, see [instructions](https://learn.microsoft.com/en-us/dotnet/framework/install/how-to-determine-which-versions-are-installed).

* [New features](https://learn.microsoft.com/en-us/dotnet/framework/whats-new/#whats-new-in-net-framework-461)
* [Release notes](https://github.com/Microsoft/dotnet/tree/main/releases/net461/README.md)

|  | Versions |
| --- | --- |
| CLR | 4 |
| Included in Visual Studio | 2017 1 |
| Windows | ✔️ 10 November Update (Version 1511) ➕ 10 ➕ 8.1 ➕ 8 ➕ 7 |
| Windows Server | ➕ 2012 R2 ➕ 2012 ➕ 2008 R2 SP1 |

1 Requires installing the **.NET desktop development**, **ASP.NET and web development**, **Azure development**, **Office/SharePoint development**, **Mobile development with .NET**, or **.NET Core cross-platform development** workloads.

To determine the installed .NET version, use the following `Release` DWORD:

* 394254 (Windows 10 November Update)
* 394271 (all other OS versions)

For more information, see [instructions](https://learn.microsoft.com/en-us/dotnet/framework/install/how-to-determine-which-versions-are-installed).

* [New features](https://learn.microsoft.com/en-us/dotnet/framework/whats-new/#whats-new-in-net-2015)
* [Release notes](https://github.com/Microsoft/dotnet/tree/main/releases/net46/README.md)

|  | Versions |
| --- | --- |
| CLR | 4 |
| Included in Visual Studio | 2015 |
| Windows | ✔️ 10 ➕ 8.1 ➕ 8 ➕ 7 ➕ Vista |
| Windows Server | ➕ 2012 R2 ➕ 2012 ➕ 2008 R2 SP1 ➕ 2008 SP2 |

To determine the installed .NET version, use the following `Release` DWORD:

* 393295 (Windows 10)
* 393297 (all other OS versions)

For more information, see [instructions](https://learn.microsoft.com/en-us/dotnet/framework/install/how-to-determine-which-versions-are-installed).

* [New features](https://learn.microsoft.com/en-us/dotnet/framework/whats-new/#whats-new-in-net-framework-452)
* [Release notes](https://github.com/Microsoft/dotnet/tree/main/releases/net452/README.md)

|  | Versions |
| --- | --- |
| CLR | 4 |
| Windows | ➕ 8.1 ➕ 8 ➕ 7 ➕ Vista |
| Windows Server | ➕ 2012 R2 ➕ 2012 ➕ 2008 R2 SP1 ➕ 2008 SP2 |

To determine the installed .NET version, use `Release` DWORD 379893. For more information, see [instructions](https://learn.microsoft.com/en-us/dotnet/framework/install/how-to-determine-which-versions-are-installed).

* [New features](https://learn.microsoft.com/en-us/dotnet/framework/whats-new/#whats-new-in-net-framework-451)
* [Release notes](https://github.com/Microsoft/dotnet/tree/main/releases/net451/README.md)

|  | Versions |
| --- | --- |
| CLR | 4 |
| Included in Visual Studio | 2013 |
| Windows | ✔️ 8.1 ➕ 8 ➕ 7 ➕ Vista |
| Windows Server | ✔️ 2012 R2 ➕ 2012 ➕ 2008 R2 SP1 ➕ 2008 SP2 |

To determine the installed .NET version, use the following `Release` DWORD:

* 378675 (Windows 8.1)
* 378758 (all other Windows versions)

For more information, see [instructions](https://learn.microsoft.com/en-us/dotnet/framework/install/how-to-determine-which-versions-are-installed).

Important

Starting with Visual Studio 2022, Visual Studio no longer includes .NET Framework components for .NET Framework 4.0 - 4.5.1 because these versions are no longer supported. Visual Studio 2022 and later versions can't build apps that target .NET Framework 4.0 through .NET Framework 4.5.1. To continue building these apps, you can use Visual Studio 2019 or an earlier version.

* [New features](https://learn.microsoft.com/en-us/dotnet/framework/whats-new/#whats-new-in-net-framework-45)
* [Release notes](https://github.com/Microsoft/dotnet/tree/main/releases/net45/README.md)

|  | Versions |
| --- | --- |
| CLR | 4 |
| Included in Visual Studio | 2012 |
| Windows | ✔️ 8 ➕ 7 ➕ Vista |
| Windows Server | ✔️ 2012 ➕ 2008 R2 SP1 ➕ 2008 SP2 |

To determine the installed .NET version, use `Release` DWORD 378389. For more information, see [instructions](https://learn.microsoft.com/en-us/dotnet/framework/install/how-to-determine-which-versions-are-installed).

Important

Starting with Visual Studio 2022, Visual Studio no longer includes .NET Framework components for .NET Framework 4.0 - 4.5.1 because these versions are no longer supported. Visual Studio 2022 and later versions can't build apps that target .NET Framework 4.0 through .NET Framework 4.5.1. To continue building these apps, you can use Visual Studio 2019 or an earlier version.

[New features](https://learn.microsoft.com/en-us/previous-versions/dotnet/netframework-4.0/ms171868(v=vs.100))

|  | Versions |
| --- | --- |
| CLR | 4 |
| Included in Visual Studio | 2010 |
| Windows | ➕ 7 ➕ Vista |
| Windows Server | ➕ 2008 R2 SP1 ➕ 2008 SP2 ➕ 2003 |

**To determine installed .NET version**: See [instructions](https://learn.microsoft.com/en-us/dotnet/framework/install/how-to-determine-which-versions-are-installed).

Important

Starting with Visual Studio 2022, Visual Studio no longer includes .NET Framework components for .NET Framework 4.0 - 4.5.1 because these versions are no longer supported. Visual Studio 2022 and later versions can't build apps that target .NET Framework 4.0 through .NET Framework 4.5.1. To continue building these apps, you can use Visual Studio 2019 or an earlier version.

[New features](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2008/ms171868(v=vs.90)):

* LINQ
* Expression trees
* Improved ASP.NET support for AJAX development
* HashSet collections
* DateTimeOffset
* WCF and WF integration
* Peer-to-Peer networking
* Add-ins for extensibility

|  | Versions |
| --- | --- |
| CLR | 2.0 |
| Included in Visual Studio | 2008 |
| Windows | ✔️ 10*✔️ 8.1* ✔️ 8* ✔️ 7 ➕ Vista |
| Windows Server | ➕ Windows Server, version 1803*➕ Windows Server, version 1709* ➕ 2016*➕ 2012 R2* ➕ 2012*✔️2008 R2 SP1* ➕ 2008 SP2 ➕ 2003 |

**To determine installed .NET version**: See [instructions](https://learn.microsoft.com/en-us/dotnet/framework/install/how-to-determine-which-versions-are-installed).

[New features](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2008/bb822048(v=vs.90)):

* Windows Presentation Foundation
* Windows Communication Foundation
* Windows Workflow Foundation
* Windows CardSpace

|  | Versions |
| --- | --- |
| CLR | 2.0 |
| Windows | ✔️ Vista |
| Windows Server | ✔️ 2008 R2 SP1*✔️ 2008 SP2* ➕ 2003 |

**To determine installed .NET version**: See [instructions](https://learn.microsoft.com/en-us/dotnet/framework/install/how-to-determine-which-versions-are-installed).

[New features](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2008/t357fb32(v=vs.90)):

* Generics
* Debugger edit and continue
* Improved scalability and performance
* ClickOnce deployment
* In ASP.NET 2.0, new controls and support for a broad array of browsers
* 64-bit support

|  | Versions |
| --- | --- |
| CLR | 2.0 |
| Included in Visual Studio | 2005 |
| Windows | N/A |
| Windows Server | ✔️ 2008 R2 SP1 ✔️ 2008 SP2 ✔️ 2003 |

**To determine installed .NET version**: See [instructions](https://learn.microsoft.com/en-us/dotnet/framework/install/how-to-determine-which-versions-are-installed).

[New features](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2008/h88tthh0(v=vs.90)):

* ASP.NET mobile controls
* Side-by-side execution
* IPv6 support

|  | Versions |
| --- | --- |
| CLR | 1.1 |
| Included in Visual Studio | 2003 |
| Windows | N/A |
| Windows Server | ✔️ 2003 |

**To determine installed .NET version**: See [instructions](https://learn.microsoft.com/en-us/dotnet/framework/install/how-to-determine-which-versions-are-installed).

|  | Versions |
| --- | --- |
| CLR | 1.0 |
| Included in Visual Studio | Visual Studio .NET |
| Windows | N/A |
| Windows Server | N/A |

**To determine installed .NET version**: See [instructions](https://learn.microsoft.com/en-us/dotnet/framework/install/how-to-determine-which-versions-are-installed).

Note

* .NET Framework must be enabled on this operating system through [Control Panel (for Windows)](https://learn.microsoft.com/en-us/dotnet/framework/install/dotnet-35-windows#enable-net-framework-35-on-windows) or the [Server Manager (for Windows Server)](https://learn.microsoft.com/en-us/dotnet/framework/install/dotnet-35-windows#enable-net-framework-35-on-windows-server).
* In general, you should not uninstall any versions of .NET Framework that are installed on your computer, because an application you use may depend on a specific version and may break if that version is removed. You can load multiple versions of .NET Framework on a single computer at the same time. This means that you can install .NET Framework without having to uninstall previous versions. For more information, see [Getting Started](https://learn.microsoft.com/en-us/dotnet/framework/get-started/).

.NET Framework 4.5 is an in-place update that replaces .NET Framework 4 on your computer, and similarly, .NET Framework 4.5.1, 4.5.2, 4.6, 4.6.1, 4.6.2, 4.7, 4.7.1, 4.7.2, and 4.8 are in-place updates to .NET Framework 4.5. In-place update means that they use the same runtime version, but the assembly versions are updated and include new types and members. After you install one of these updates, your .NET Framework 4, .NET Framework 4.5, .NET Framework 4.6, or .NET Framework 4.7 apps should continue to run without requiring recompilation. However, the reverse is not true. We do not recommend running apps that target a later version of .NET Framework on an earlier version. For example, we do not recommend that you run an app the targets .NET Framework 4.6 on .NET Framework 4.5.

The following guidelines apply:

* In Visual Studio, you can choose .NET Framework 4.5 as the target framework for a project (this sets the [GetReferenceAssemblyPaths.TargetFrameworkMoniker](https://learn.microsoft.com/en-us/dotnet/api/microsoft.build.tasks.getreferenceassemblypaths.targetframeworkmoniker) property) to compile the project as a .NET Framework 4.5 assembly or executable. This assembly or executable can then be used on any computer that has .NET Framework 4.5, 4.5.1, 4.5.2, 4.6, 4.6.1, 4.6.2, 4.7, 4.7.1, 4.7.2, or 4.8 installed.

* In Visual Studio, you can choose .NET Framework 4.5.1 as the target framework for a project to compile it as a .NET Framework 4.5.1 assembly or executable. Only run this assembly or executable on computers that have .NET Framework 4.5.1 or later installed. An executable that targets .NET Framework 4.5.1 will be blocked from running on a computer that only has an earlier version of .NET Framework, such as .NET Framework 4.5, installed. The user will be prompted to install .NET Framework 4.5.1. In addition, .NET Framework 4.5.1 assemblies should not be called from an app that targets an earlier version of .NET Framework, such as .NET Framework 4.5.

Note

.NET Framework 4.5.1 and .NET Framework 4.5 are used here only as examples. The principle described applies to any app that targets a later version of .NET Framework than the one installed on the system on which it's running.

Some changes in .NET Framework may require changes to your app code; see [Application Compatibility](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/application-compatibility) before you run your existing apps with .NET Framework 4.5 or later versions. For more information about installing the current version, see [Install the .NET Framework for developers](https://learn.microsoft.com/en-us/dotnet/framework/install/guide-for-developers). For information about support for the .NET Framework, see [.NET Framework official support policy](https://dotnet.microsoft.com/platform/support/policy/dotnet-framework) on the .NET website.

.NET Framework versions 2.0, 3.0, and 3.5 are built with the same version of the CLR (CLR 2.0). These versions represent successive layers of a single installation. Each version is built incrementally on top of the earlier versions. It's not possible to run versions 2.0, 3.0, and 3.5 side by side on a computer. When you install version 3.5, you get the 2.0 and 3.0 layers automatically, and apps that were built for versions 2.0, 3.0, and 3.5 can all run on version 3.5. However, .NET Framework 4 ends this layering approach, and it and later releases (.NET Framework 4.5, 4.5.1, 4.5.2, 4.6, 4.6.1, 4.6.2, 4.7, 4.7.1, 4.7.2, and 4.8) also represent successive layers of a single installation. Starting with .NET Framework 4, you can use in-process, side by side hosting to run multiple versions of the CLR in a single process. For more information, see [Assemblies and Side-by-Side Execution](https://learn.microsoft.com/en-us/dotnet/standard/assembly/side-by-side-execution).

In addition, if your app targets version 2.0, 3.0, or 3.5, your users may be required to enable .NET Framework 3.5 on a Windows 8, Windows 8.1, or Windows 10 computer before they can run your app. For more information, see [Install the .NET Framework 3.5 on Windows 11, Windows 10, Windows 8.1, and Windows 8](https://learn.microsoft.com/en-us/dotnet/framework/install/dotnet-35-windows).

Important

Starting with Visual Studio 2022, Visual Studio no longer includes .NET Framework components for .NET Framework 4.0 - 4.5.1 because these versions are no longer supported. Visual Studio 2022 and later versions can't build apps that target .NET Framework 4.0 through .NET Framework 4.5.1. To continue building these apps, you can use Visual Studio 2019 or an earlier version.

* If you're new to the .NET Framework, see the [overview](https://learn.microsoft.com/en-us/dotnet/framework/get-started/overview) for an introduction to key concepts and features.

* For new features and improvements in the .NET Framework 4.5 and its point releases, see [What's new in the .NET Framework](https://learn.microsoft.com/en-us/dotnet/framework/whats-new/).

* For information about migrating your app to a newer version of the .NET Framework, see the [migration guide](https://learn.microsoft.com/en-us/dotnet/framework/install/).

* For information about determining which versions or updates are installed on a computer, see [How to: Determine Which .NET Framework Versions Are Installed](https://learn.microsoft.com/en-us/dotnet/framework/install/how-to-determine-which-versions-are-installed) and [How to: Determine Which .NET Framework Updates Are Installed](https://learn.microsoft.com/en-us/dotnet/framework/install/how-to-determine-which-net-framework-updates-are-installed).

* [Version compatibility](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/version-compatibility)
* [.NET Framework official support policy](https://dotnet.microsoft.com/platform/support/policy/dotnet-framework)
* [Troubleshoot blocked .NET Framework installations and uninstallations](https://learn.microsoft.com/en-us/dotnet/framework/install/troubleshoot-blocked-installations-and-uninstallations)

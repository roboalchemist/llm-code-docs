# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/dotnet-environments/getting-started-with-net.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/dotnet-environments/getting-started-with-net.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/dotnet-environments/getting-started-with-net.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/dotnet-environments/getting-started-with-net.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/dotnet-environments/getting-started-with-net.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/dotnet-environments/getting-started-with-net.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/dotnet-environments/getting-started-with-net.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/dotnet-environments/getting-started-with-net.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/dotnet-environments/getting-started-with-net.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/dotnet-environments/getting-started-with-net.md

# Getting started with .NET

Setting up a .NET analysis with Sonar involves different configurations depending on your .NET environment and the CI integration used for your workflow. This page helps you get started by looking at the prerequisites, provides information to identify the version of the .NET scanner you should use, followed by links to setting up your CI environment and concluding with an overview of establishing code coverage to generate reports.

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

Knowing which .NET version you are running is important; check this [Microsoft documentation](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/how-to-determine-which-versions-are-installed) to learn which versions you have installed.

The SonarScanner for .NET must be installed in the same environment where you build your application. For example, if you’re building projects locally, the scanner must be installed locally; similarly, if you’re working with Azure Pipelines, you must add SonarScanner tasks to the pipeline.

The SonarScanner is working during the build process therefore, don’t be worried if everything takes a little longer because as mentioned above, the build is now also running an analysis *during the build*.

#### Your environment <a href="#your-environment" id="your-environment"></a>

**SonarQube Server**

The SonarScanner for .NET works with supported versions of SonarQube Server and with SonarQube Cloud.

* SonarQube 10.4 and newer requires the SonarScanner for .NET 5.14 or newer.
* SonarQube 8.9 is deprecated in the SonarScanner for .NET 9.0. The SonarScanner will fail to start if SonarQube 8.8 or older is detected.

**Java**

Depending on the version of the SonarScanner for .NET and SonarQube Server combination you are using, you might need to install Java. When running SonarQube 10.6 or newer with the scanner version 7.0 or newer, installing a JRE is not required because it will be automatically obtained from the server.

* You can disable JRE auto-provisioning and specify your own version of Java; please check the scanner’s page [general-requirements](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/scanner-environment/general-requirements "mention") when using JRE auto-provisioning.

Otherwise, you must have at least the minimal version of Java supported by your version of SonarQube Server.

* Before scanner version 6.0, Java 11 or newer is required.
* From and including scanner version 6.0, Java 17 or newer is required.

Open the **SonarScanner for .NET** version Update Center expandable box (next, below); then find the scanner version that fits with your version of SonarQube Server and your runtime to download the correct version. We recommend that you choose the latest version of the scanner.

<details>

<summary>SonarScanner for .NET — 11.0.0.126294 | <a href="https://github.com/SonarSource/sonar-scanner-msbuild/issues">Issue Tracker</a></summary>

**11.0.0.126294** <sup><sub>**2025-10-15**<sub></sup>\ <sup>The Scanner for .NET does not embed the SonarScanner CLI anymore and downloads it when needed. Adds support for MSTest 4.</sup>\
Download scanner for: [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/11.0.0.126294/sonar-scanner-11.0.0.126294-net.zip) [.NET Framework 4.6.2+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/11.0.0.126294/sonar-scanner-11.0.0.126294-net-framework.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/11.0.0.126294)

***

**10.4.1.124928** <sup><sub>**2025-09-23**<sub></sup>\ <sup>Fix a bug that erroneously warns that Community Build is not supported.</sup>\
Download scanner for: [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/10.4.1.124928/sonar-scanner-10.4.1.124928-net.zip) [.NET Framework 4.6.2+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/10.4.1.124928/sonar-scanner-10.4.1.124928-net-framework.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/10.4.1.124928)

***

**10.4.0.124828** <sup><sub>**2025-09-22**<sub></sup>\ <sup>New communication system with SonarQube.</sup>\
Download scanner for: [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/10.4.0.124828/sonar-scanner-10.4.0.124828-net.zip) [.NET Framework 4.6.2+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/10.4.0.124828/sonar-scanner-10.4.0.124828-net-framework.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/10.4.0.124828)

***

**10.3.0.120579** <sup><sub>**2025-07-16**<sub></sup>\ <sup>Support xUnit v3, fix RunDeploymentRoot in trx files, remove sonar.scanner.scanAll analysis warning.</sup>\
Download scanner for: [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/10.3.0.120579/sonar-scanner-10.3.0.120579-net.zip) [.NET Framework 4.6.2+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/10.3.0.120579/sonar-scanner-10.3.0.120579-net-framework.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/10.3.0.120579)

***

**10.2.0.117568** <sup><sub>**2025-06-03**<sub></sup>\ <sup>Fix a vulnerability from embedded scanner-cli.</sup>\
Download scanner for: [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/10.2.0.117568/sonar-scanner-10.2.0.117568-net.zip) [.NET Framework 4.6.2+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/10.2.0.117568/sonar-scanner-10.2.0.117568-net-framework.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/10.2.0.117568)

***

**10.1.2.114627** <sup><sub>**2025-04-16**<sub></sup>\ <sup>Add 'sonar' default truststore passord fallback.</sup>\
Download scanner for: [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/10.1.2.114627/sonar-scanner-10.1.2.114627-net.zip) [.NET Framework 4.6.2+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/10.1.2.114627/sonar-scanner-10.1.2.114627-net-framework.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/10.1.2.114627)

***

**10.1.1.111189** <sup><sub>**2025-03-25**<sub></sup>\ <sup>Maintenance and dependencies updates.</sup>\
Download scanner for: [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/10.1.1.111189/sonar-scanner-10.1.1.111189-net.zip) [.NET Framework 4.6.2+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/10.1.1.111189/sonar-scanner-10.1.1.111189-net-framework.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/10.1.1.111189)

***

**10.1.0** <sup><sub>**2025-03-19**<sub></sup>\ <sup>Maintenance and dependencies updates.</sup>\
Download scanner for: [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/10.1.0.110937/sonar-scanner-10.1.0.110937-net.zip) [.NET Framework 4.6.2+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/10.1.0.110937/sonar-scanner-10.1.0.110937-net-framework.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/10.1.0.110937)

***

**10.0.0** <sup><sub>**2025-03-13**<sub></sup>\ <sup>Fix a vulnerability. Mandate that the truststore password is passed in the end step if used in the begin step. Added support for 7 new languages.</sup>\
Download scanner for: [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/10.0.0.110776/sonar-scanner-10.0.0.110776-net.zip) [.NET Framework 4.6.2+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/10.0.0.110776/sonar-scanner-10.0.0.110776-net-framework.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/10.0.0.110776)

***

**9.2.1** <sup><sub>**2025-02-25**<sub></sup>\ <sup>DEPRECATED. Use system trusted certificate or JVM certificate store.</sup>\
Download scanner for: [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/9.2.1.110358/sonar-scanner-9.2.1.110358-net.zip) [.NET Framework 4.6.2+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/9.2.1.110358/sonar-scanner-9.2.1.110358-net-framework.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/9.2.1.110358)

***

**9.2.0** <sup><sub>**2025-02-19**<sub></sup>\ <sup>DEPRECATED. Support for local trust store for private and self-signed certificates.</sup>\
Download scanner for: [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/9.2.0.110275/sonar-scanner-9.2.0.110275-net.zip) [.NET Framework 4.6.2+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/9.2.0.110275/sonar-scanner-9.2.0.110275-net-framework.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/9.2.0.110275)

***

**9.1.0** <sup><sub>**2025-02-06**<sub></sup>\ <sup>Read new properties for downloading plugins</sup>\
Download scanner for: [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/9.1.0.109947/sonar-scanner-9.1.0.109947-net.zip) [.NET Framework 4.6.2+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/9.1.0.109947/sonar-scanner-9.1.0.109947-net-framework.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/9.1.0.109947)

***

**9.0.2** <sup><sub>**2024-11-12**<sub></sup>\ <sup>sonar.projectBaseDir passed through extraProperties is respected with Azure DevOps extensions. Do not fail during file indexing when a directory cannot be accessed.</sup>\
Download scanner for: [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/9.0.2.104486/sonar-scanner-9.0.2.104486-net.zip) [.NET Framework 4.6.2+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/9.0.2.104486/sonar-scanner-9.0.2.104486-net-framework.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/9.0.2.104486)

***

**9.0.1** <sup><sub>**2024-10-25**<sub></sup>\ <sup>Fix projectBaseDir path detection on Azure DevOps Linux agents.</sup>\
Download scanner for: [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/9.0.1.102776/sonar-scanner-9.0.1.102776-net.zip) [.NET Framework 4.6.2+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/9.0.1.102776/sonar-scanner-9.0.1.102776-net-framework.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/9.0.1.102776)

***

**9.0.0** <sup><sub>**2024-09-27**<sub></sup>\ <sup>Ignore sonar.sources and sonar.tests properties.</sup>\
Download scanner for: [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/9.0.0.100868/sonar-scanner-9.0.0.100868-net.zip) [.NET Framework 4.6.2+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/9.0.0.100868/sonar-scanner-9.0.0.100868-net-framework.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/9.0.0.100868)

***

**8.0.3** <sup><sub>**2024-09-13**<sub></sup>\ <sup>Exclude XML files from the new automatic analysis. Do not crash on mlaformed paths. Make sure server-side exclusions are not overridden.</sup>\
Download scanner for: [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/8.0.3.99785/sonar-scanner-8.0.3.99785-net.zip) [.NET Framework 4.6.2+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/8.0.3.99785/sonar-scanner-8.0.3.99785-net-framework.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/8.0.3.99785)

***

**8.0.2** <sup><sub>**2024-09-02**<sub></sup>\ <sup>Re-enabled sonar.exclusions support. Automatically exclude files passed-in as coverage. Skip transient projects that do not exist after the build.</sup>\
Download scanner for: [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/8.0.2.98917/sonar-scanner-8.0.2.98917-net.zip) [.NET Framework 4.6.2+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/8.0.2.98917/sonar-scanner-8.0.2.98917-net-framework.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/8.0.2.98917)

***

**8.0.1** <sup><sub>**2024-08-21**<sub></sup>\ <sup>Bug fix release which addresses two issues, improvements on messages emmitted during the analysis.</sup>\
Download scanner for: [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/8.0.1.97834/sonar-scanner-8.0.1.97834-net.zip) [.NET Framework 4.6.2+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/8.0.1.97834/sonar-scanner-8.0.1.97834-net-framework.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/8.0.1.97834)

***

**8.0** <sup><sub>**2024-08-12**<sub></sup>\ <sup>The scanner is now supporting multi-language analysis. Files for other languages are automatically picked up (SQL, YAML, XML, JSON, CSS, HTML, JS, TS)</sup>\
Download scanner for: [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/8.0.0.97025/sonar-scanner-8.0.0.97025-net.zip) [.NET Framework 4.6.2+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/8.0.0.97025/sonar-scanner-8.0.0.97025-net-framework.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/8.0.0.97025)

***

**7.1.1** <sup><sub>**2024-07-24**<sub></sup>\ <sup>Fixed a small issue when not specifying sonar.host.url (defaults to <https://sonarcloud.io>)</sup>\
Download scanner for: [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/7.1.1.96069/sonar-scanner-7.1.1.96069-net.zip) [.NET Framework 4.6.2+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/7.1.1.96069/sonar-scanner-7.1.1.96069-net-framework.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/7.1.1.96069)

***

**7.1** <sup><sub>**2024-07-19**<sub></sup>\ <sup>Fixed a small issue when not specifying sonar.host.url (defaults to <https://sonarcloud.io>)</sup>\
Download scanner for: [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/7.1.0.95705/sonar-scanner-7.1.0.95705-net.zip) [.NET Framework 4.6.2+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/7.1.0.95705/sonar-scanner-7.1.0.95705-net-framework.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/7.1.0.95705)

***

**7.0** <sup><sub>**2024-07-18**<sub></sup>\ <sup>This version does not require a JRE to be present on the machine anymore</sup>\
Download scanner for: [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/7.0.0.95646/sonar-scanner-7.0.0.95646-net.zip) [.NET Framework 4.6.2+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/7.0.0.95646/sonar-scanner-7.0.0.95646-net-framework.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/7.0.0.95646)

***

**6.2** <sup><sub>**2024-02-16**<sub></sup>\ <sup>Fixes the failing analysis on macOS with .NET 8.0. New optional sonar.http.timeout command line parameter</sup>\
Download scanner for: [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/6.2.0.85879/sonar-scanner-6.2.0.85879-net.zip) [.NET Framework 4.6.2+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/6.2.0.85879/sonar-scanner-6.2.0.85879-net-framework.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/6.2.0.85879)

***

**6.1** <sup><sub>**2024-01-29**<sub></sup>\ <sup>Drop support for MSBuild 14, deprecate MSBuild 15</sup>\
Download scanner for: [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/6.1.0.83647/sonar-scanner-6.1.0.83647-net.zip) [.NET Framework 4.6.2+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/6.1.0.83647/sonar-scanner-6.1.0.83647-net-framework.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/6.1.0.83647)

***

**6.0** <sup><sub>**2023-12-04**<sub></sup>\ <sup>Packaging change, drop support for .Net Framework 4.6, Net 2.1, and .Net 3.0. Drop Java 11 support. Drop support of SonarQube versions prior to 8.9</sup>\
Download scanner for: [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/6.0.0.81631/sonar-scanner-6.0.0.81631-net.zip) [.NET Framework 4.6.2+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/6.0.0.81631/sonar-scanner-6.0.0.81631-net-framework.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/6.0.0.81631)

***

**5.15.1** <sup><sub>**2024-03-26**<sub></sup>\ <sup>Fix analysis on MacOSX with .NET 8 when begin runtime doesn't match with build runtime</sup>\
Download scanner for: [.NET 5+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.15.1.88158/sonar-scanner-msbuild-5.15.1.88158-net5.0.zip) [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.15.1.88158/sonar-scanner-msbuild-5.15.1.88158-netcoreapp3.0.zip) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.15.1.88158/sonar-scanner-msbuild-5.15.1.88158-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.15.1.88158/sonar-scanner-msbuild-5.15.1.88158-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/5.15.1.88158)

***

**5.15** <sup><sub>**2023-11-20**<sub></sup>\ <sup>Add an option to specify the scanner's temporary working directory</sup>\
Download scanner for: [.NET 5+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.15.0.80890/sonar-scanner-msbuild-5.15.0.80890-net5.0.zip) [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.15.0.80890/sonar-scanner-msbuild-5.15.0.80890-netcoreapp3.0.zip) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.15.0.80890/sonar-scanner-msbuild-5.15.0.80890-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.15.0.80890/sonar-scanner-msbuild-5.15.0.80890-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/5.15.0.80890)

***

**5.14** <sup><sub>**2023-10-02**<sub></sup>\ <sup>Support upcoming SonarQube 10.4 API changes</sup>\
Download scanner for: [.NET 5+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.14.0.78575/sonar-scanner-msbuild-5.14.0.78575-net5.0.zip) [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.14.0.78575/sonar-scanner-msbuild-5.14.0.78575-netcoreapp3.0.zip) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.14.0.78575/sonar-scanner-msbuild-5.14.0.78575-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.14.0.78575/sonar-scanner-msbuild-5.14.0.78575-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/5.14.0.78575)

***

**5.13.1** <sup><sub>**2023-08-14**<sub></sup>\ <sup>SonarScanner CLI update</sup>\
Download scanner for: [.NET 5+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.13.1.76110/sonar-scanner-msbuild-5.13.1.76110-net5.0.zip) [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.13.1.76110/sonar-scanner-msbuild-5.13.1.76110-netcoreapp3.0.zip) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.13.1.76110/sonar-scanner-msbuild-5.13.1.76110-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.13.1.76110/sonar-scanner-msbuild-5.13.1.76110-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/5.13.1.76110)

***

**5.13** <sup><sub>**2023-04-05**<sub></sup>\ <sup>Support for sonar.token parameter and improved error messages</sup>\
Download scanner for: [.NET 5+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.13.0.66756/sonar-scanner-msbuild-5.13.0.66756-net5.0.zip) [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.13.0.66756/sonar-scanner-msbuild-5.13.0.66756-netcoreapp3.0.zip) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.13.0.66756/sonar-scanner-msbuild-5.13.0.66756-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.13.0.66756/sonar-scanner-msbuild-5.13.0.66756-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/5.13.0.66756)

***

**5.12** <sup><sub>**2023-03-17**<sub></sup>\ <sup>Fast PR Analysis Support For Azure Devops</sup>\
Download scanner for: [.NET 5+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.12.0.64969/sonar-scanner-msbuild-5.12.0.64969-net5.0.zip) [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.12.0.64969/sonar-scanner-msbuild-5.12.0.64969-netcoreapp3.0.zip) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.12.0.64969/sonar-scanner-msbuild-5.12.0.64969-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.12.0.64969/sonar-scanner-msbuild-5.12.0.64969-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/5.12.0.64969)

***

**5.11** <sup><sub>**2023-01-27**<sub></sup>\ <sup>Fast PR Analysis Compatibility Fix</sup>\
Download scanner for: [.NET 5+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.11.0.60783/sonar-scanner-msbuild-5.11.0.60783-net5.0.zip) [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.11.0.60783/sonar-scanner-msbuild-5.11.0.60783-netcoreapp3.0.zip) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.11.0.60783/sonar-scanner-msbuild-5.11.0.60783-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.11.0.60783/sonar-scanner-msbuild-5.11.0.60783-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/5.11.0.60783)

***

**5.10** <sup><sub>**2023-01-13**<sub></sup>\ <sup>Improved FIPS Compliance</sup>\
Download scanner for: [.NET 5+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.10.0.59947/sonar-scanner-msbuild-5.10.0.59947-net5.0.zip) [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.10.0.59947/sonar-scanner-msbuild-5.10.0.59947-netcoreapp3.0.zip) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.10.0.59947/sonar-scanner-msbuild-5.10.0.59947-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.10.0.59947/sonar-scanner-msbuild-5.10.0.59947-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/5.10.0.59947)

***

**5.9.2** <sup><sub>**2022-12-14**<sub></sup>\ <sup>Bug Fix Release related to PR analysis</sup>\
Download scanner for: [.NET 5+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.9.2.58699/sonar-scanner-msbuild-5.9.2.58699-net5.0.zip) [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.9.2.58699/sonar-scanner-msbuild-5.9.2.58699-netcoreapp3.0.zip) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.9.2.58699/sonar-scanner-msbuild-5.9.2.58699-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.9.2.58699/sonar-scanner-msbuild-5.9.2.58699-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/5.9.2.58699)

***

**5.9.1** <sup><sub>**2022-12-06**<sub></sup>\ <sup>Bug Fix Release</sup>\
Download scanner for: [.NET 5+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.9.1.58166/sonar-scanner-msbuild-5.9.1.58166-net5.0.zip) [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.9.1.58166/sonar-scanner-msbuild-5.9.1.58166-netcoreapp3.0.zip) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.9.1.58166/sonar-scanner-msbuild-5.9.1.58166-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.9.1.58166/sonar-scanner-msbuild-5.9.1.58166-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/5.9.1.58166)

***

**5.9.0** <sup><sub>**2022-12-01**<sub></sup>\ <sup>.NET 7 bug fixes and preparation for fast PR analysis</sup>\
Download scanner for: [.NET 5+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.9.0.57893/sonar-scanner-msbuild-5.9.0.57893-net5.0.zip) [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.9.0.57893/sonar-scanner-msbuild-5.9.0.57893-netcoreapp3.0.zip) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.9.0.57893/sonar-scanner-msbuild-5.9.0.57893-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.9.0.57893/sonar-scanner-msbuild-5.9.0.57893-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/5.9.0.57893)

***

**5.8.0** <sup><sub>**2022-08-24**<sub></sup>\ <sup>Analysis of Azure Functions on Github Actions no longer hard fails with default behavior. See release notes for details.</sup>\
Download scanner for: [.NET 5+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.8.0.52797/sonar-scanner-msbuild-5.8.0.52797-net5.0.zip) [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.8.0.52797/sonar-scanner-msbuild-5.8.0.52797-netcoreapp3.0.zip) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.8.0.52797/sonar-scanner-msbuild-5.8.0.52797-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.8.0.52797/sonar-scanner-msbuild-5.8.0.52797-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/5.8.0.52797)

***

**5.7.2** <sup><sub>**2022-07-12**<sub></sup>\ <sup>Log warning instead of error when not parsing environment variables to avoid hard failure when Newtonsoft does not get resolved</sup>\
Download scanner for: [.NET 5+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.7.2.50892/sonar-scanner-msbuild-5.7.2.50892-net5.0.zip) [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.7.2.50892/sonar-scanner-msbuild-5.7.2.50892-netcoreapp3.0.zip) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.7.2.50892/sonar-scanner-msbuild-5.7.2.50892-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.7.2.50892/sonar-scanner-msbuild-5.7.2.50892-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/5.7.2.50892)

***

**5.7.1** <sup><sub>**2022-06-21**<sub></sup>\ <sup>Bug Fix Release</sup>\
Download scanner for: [.NET 5+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.7.1.49528/sonar-scanner-msbuild-5.7.1.49528-net5.0.zip) [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.7.1.49528/sonar-scanner-msbuild-5.7.1.49528-netcoreapp3.0.zip) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.7.1.49528/sonar-scanner-msbuild-5.7.1.49528-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.7.1.49528/sonar-scanner-msbuild-5.7.1.49528-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/5.7.1.49528)

***

**5.7.0** <sup><sub>**2022-06-20**<sub></sup>\ <sup>Bug Fix Release</sup>\
Download scanner for: [.NET 5+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.7.0.49456/sonar-scanner-msbuild-5.7.0.49456-net5.0.zip) [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.7.0.49456/sonar-scanner-msbuild-5.7.0.49456-netcoreapp3.0.zip) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.7.0.49456/sonar-scanner-msbuild-5.7.0.49456-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.7.0.49456/sonar-scanner-msbuild-5.7.0.49456-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/5.7.0.49456)

***

**5.6.0** <sup><sub>**2022-05-30**<sub></sup>\ <sup>Send warnings to users of versions where support will change</sup>\
Download scanner for: [.NET 5+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.6.0.48455/sonar-scanner-msbuild-5.6.0.48455-net5.0.zip) [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 3.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.6.0.48455/sonar-scanner-msbuild-5.6.0.48455-netcoreapp3.0.zip) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.6.0.48455/sonar-scanner-msbuild-5.6.0.48455-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.6.0.48455/sonar-scanner-msbuild-5.6.0.48455-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/5.6.0.48455)

***

**5.5.3** <sup><sub>**2022-02-14**<sub></sup>\ <sup>Support for .NET 6 Web Projects, TLS Version selection logic removed - now responsibility of OS, Fix "MSB3677 Unable to move file" regression</sup>\
Download scanner for: [.NET 5+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.5.3.43281/sonar-scanner-msbuild-5.5.3.43281-net5.0.zip) [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.5.3.43281/sonar-scanner-msbuild-5.5.3.43281-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.5.3.43281/sonar-scanner-msbuild-5.5.3.43281-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/5.5.3.43281)

***

**5.5.2** <sup><sub>**2022-02-10**<sub></sup>\ <sup>Support for .NET 6 Web Projects, TLS Version selection logic removed, now responsibility of OS</sup>\
Download scanner for: [.NET 5+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.5.2.43124/sonar-scanner-msbuild-5.5.2.43124-net5.0.zip) [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.5.2.43124/sonar-scanner-msbuild-5.5.2.43124-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.5.2.43124/sonar-scanner-msbuild-5.5.2.43124-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/5.5.2.43124)

***

**5.5.1** <sup><sub>**2022-02-08**<sub></sup>\ <sup>Support for .NET 6 Web Projects, support TLS 1.3 where supported by environment</sup>\
Download scanner for: [.NET 5+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.5.1.42999/sonar-scanner-msbuild-5.5.1.42999-net5.0.zip) [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.5.1.42999/sonar-scanner-msbuild-5.5.1.42999-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.5.1.42999/sonar-scanner-msbuild-5.5.1.42999-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/5.5.1.42999)

***

**5.5.0** <sup><sub>**2022-02-07**<sub></sup>\ <sup>Support for .NET 6 Web Projects, support TLS 1.3</sup>\
Download scanner for: [.NET 5+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.5.0.42949/sonar-scanner-msbuild-5.5.0.42949-net5.0.zip) [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.5.0.42949/sonar-scanner-msbuild-5.5.0.42949-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.5.0.42949/sonar-scanner-msbuild-5.5.0.42949-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/5.5.0.42949)

***

**5.4.1** <sup><sub>**2021-12-23**<sub></sup>\ <sup>Updated Newtonsoft.Json to latest</sup>\
Download scanner for: [.NET 5+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.4.1.41282/sonar-scanner-msbuild-5.4.1.41282-net5.0.zip) [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.4.1.41282/sonar-scanner-msbuild-5.4.1.41282-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.4.1.41282/sonar-scanner-msbuild-5.4.1.41282-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/5.4.1.41282)

***

**5.4** <sup><sub>**2021-11-26**<sub></sup>\ <sup>Updated .NET 5 Version to be forward compatible and support .NET 6 environments</sup>\
Download scanner for: [.NET 5+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.4.0.40033/sonar-scanner-msbuild-5.4.0.40033-net5.0.zip) [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.4.0.40033/sonar-scanner-msbuild-5.4.0.40033-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.4.0.40033/sonar-scanner-msbuild-5.4.0.40033-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/5.4.0.40033)

***

**5.3.2** <sup><sub>**2021-10-28**<sub></sup>\ <sup>Added parameters sonar.clientcert.path and sonar.clientcert.password for securing connections to SonarQube</sup>\
Download scanner for: [.NET 5+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.3.2.38712/sonar-scanner-msbuild-5.3.2.38712-net5.0.zip) [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.3.2.38712/sonar-scanner-msbuild-5.3.2.38712-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.3.2.38712/sonar-scanner-msbuild-5.3.2.38712-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/5.3.2.38712)

***

**5.3.1** <sup><sub>**2021-09-01**<sub></sup>\ <sup>Update scanner-cli, Compile with .NET Core 2.1 and 3.1, Improve uninstall of targets if multiple builds in the same pipeline</sup>\
Download scanner for: [.NET 5+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.3.1.36242/sonar-scanner-msbuild-5.3.1.36242-net5.0.zip) [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.3.1.36242/sonar-scanner-msbuild-5.3.1.36242-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.3.1.36242/sonar-scanner-msbuild-5.3.1.36242-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/5.3.1.36242)

***

**5.2.2** <sup><sub>**2021-06-24**<sub></sup>\ <sup>Fix test assembly detection + mTLS certificate with password</sup>\
Download scanner for: [.NET 5+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.2.2.33595/sonar-scanner-msbuild-5.2.2.33595-net5.0.zip) [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.2.2.33595/sonar-scanner-msbuild-5.2.2.33595-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.2.2.33595/sonar-scanner-msbuild-5.2.2.33595-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/5.2.2.33595)

***

**5.2.1** <sup><sub>**2021-04-30**<sub></sup>\ <sup>Update embedded SonarScanner CLI</sup>\
Download scanner for: [.NET 5+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.2.1.31210/sonar-scanner-msbuild-5.2.1.31210-net5.0.zip) [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.2.1.31210/sonar-scanner-msbuild-5.2.1.31210-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.2.1.31210/sonar-scanner-msbuild-5.2.1.31210-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/5.2.1.31210)

***

**5.2** <sup><sub>**2021-04-09**<sub></sup>\ <sup>Support for test code analysis</sup>\
Download scanner for: [.NET 5+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.2.0.29862/sonar-scanner-msbuild-5.2.0.29862-net5.0.zip) [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.2.0.29862/sonar-scanner-msbuild-5.2.0.29862-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.2.0.29862/sonar-scanner-msbuild-5.2.0.29862-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/5.2.0.29862)

***

**5.1** <sup><sub>**2021-03-09**<sub></sup>\ <sup>Support for .NET 5, support for solo .NET Core project (without .sln)</sup>\
Download scanner for: [.NET 5+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.1.0.28487/sonar-scanner-msbuild-5.1.0.28487-net5.0.zip) [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.1.0.28487/sonar-scanner-msbuild-5.1.0.28487-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.1.0.28487/sonar-scanner-msbuild-5.1.0.28487-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/5.1.0.28487)

***

**5.0.4** <sup><sub>**2020-11-11**<sub></sup>\ <sup>Support for .NET 5, support for solo .NET Core project (without .sln)</sup>\
Download scanner for: [.NET 5+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.0.4.24009/sonar-scanner-msbuild-5.0.4.24009-net5.0.zip) [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.0.4.24009/sonar-scanner-msbuild-5.0.4.24009-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.0.4.24009/sonar-scanner-msbuild-5.0.4.24009-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/5.0.4.24009)

***

**5.0.3** <sup><sub>**2020-11-10**<sub></sup>\ <sup>Support for .NET 5, support for solo .NET Core project (without .sln)</sup>\
Download scanner for: [.NET 5+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.0.3.23901/sonar-scanner-msbuild-5.0.3.23901-net5.0.zip) [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.0.3.23901/sonar-scanner-msbuild-5.0.3.23901-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.0.3.23901/sonar-scanner-msbuild-5.0.3.23901-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/5.0.3.23901)

***

**5.0** <sup><sub>**2020-11-05**<sub></sup>\ <sup>Support for .NET 5, support for solo .NET Core project (without .sln)</sup>\
Download scanner for: [.NET 5+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.0.0.23533/sonar-scanner-msbuild-5.0.0.23533-net5.0.zip) [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.0.0.23533/sonar-scanner-msbuild-5.0.0.23533-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/5.0.0.23533/sonar-scanner-msbuild-5.0.0.23533-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/5.0.0.23533)

***

**4.10** <sup><sub>**2020-06-29**<sub></sup>\ <sup>Support FIPS compliant cryptographic algorithm</sup>\
Download scanner for: [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/4.10.0.19059/sonar-scanner-msbuild-4.10.0.19059-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/4.10.0.19059/sonar-scanner-msbuild-4.10.0.19059-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/4.10.0.19059)

***

**4.9** <sup><sub>**2020-05-05**<sub></sup>\ <sup>Improve detection of duplicated coverage reports, fix categorization of fakes projects</sup>\
Download scanner for: [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/4.9.0.17385/sonar-scanner-msbuild-4.9.0.17385-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/4.9.0.17385/sonar-scanner-msbuild-4.9.0.17385-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/4.9.0.17385)

***

**4.8** <sup><sub>**2019-11-06**<sub></sup>\ <sup>Enable scanner execution when only .NET Core 3 is installed</sup>\
Download scanner for: [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/4.8.0.12008/sonar-scanner-msbuild-4.8.0.12008-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/4.8.0.12008/sonar-scanner-msbuild-4.8.0.12008-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/4.8.0.12008)

***

**4.7.1** <sup><sub>**2019-09-10**<sub></sup>\ <sup>Update SonarScanner to version 4.1</sup>\
Download scanner for: [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/4.7.1.2311/sonar-scanner-msbuild-4.7.1.2311-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/4.7.1.2311/sonar-scanner-msbuild-4.7.1.2311-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/4.7.1.2311)

***

**4.7** <sup><sub>**2019-09-03**<sub></sup>\ <sup>Support dash and forward-slash in dotnet command line arguments, analyze XAML files, add analyzed targets in logs</sup>\
Download scanner for: [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) [.NET Core 2.1](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/4.7.0.2295/sonar-scanner-msbuild-4.7.0.2295-netcoreapp2.0.zip) [.NET Framework 4.6](https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/4.7.0.2295/sonar-scanner-msbuild-4.7.0.2295-net46.zip)\
\
[Release notes](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/4.7.0.2295)

</details>

### Identify your SonarScanner version <a href="#your-sonarscanner-version" id="your-sonarscanner-version"></a>

Each .NET environment is slightly different. Check the appropriate tab for requirements and notes about the installation.

{% tabs %}
{% tab title=".NET" %}
**Install your .NET environment**

If you are using the .NET version of the scanner or the [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) you will need [.NET Core SDK 3.1 or above](https://dotnet.microsoft.com/en-us/download/dotnet). See this [Microsoft page](https://dotnet.microsoft.com/en-us/download) to download .NET.

The SonarScanner for .NET works with .NET environments including .NET Core 3.1 and newer.
{% endtab %}

{% tab title=".NET FRAMEWORK" %}
**Install your .NET Framework environment**

If you are using the .NET Framework version of the scanner you will need .NET Framework v4.6.2 or above. For commercial versions of SonarQube Server to benefit from security analysis you will need .NET Framework v4.7.2 or above. See this [Microsoft page](https://dotnet.microsoft.com/en-us/download/dotnet-framework) to download supported versions of .NET Framework.
{% endtab %}
{% endtabs %}

#### Installing the scanner <a href="#installing-the-scanner" id="installing-the-scanner"></a>

SonarQube Server knows which analyzer plugins you need for a given version however, choosing the correct SonarScanner version is up to you according to your .NET environment. You can use any version of the SonarScanner that supports your .NET runtime. For full details, check the [installing](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/dotnet/installing "mention") page for the prerequisites and install instructions.

Below, choose the SDK corresponding to your build system for a getting started overview:

{% tabs %}
{% tab title=".NET" %}

### **Install scanner for .NET**

You can install the SonarScanner for .NET from Nuget using the .NET global tool, or download a standalone file to execute.

#### **.NET global tool**

If you are using .NET on an already installed instance of SonarQube Server, the simplest way to install the scanner is to use the dotnet install tool from the command line. The [.NET Global Tool](https://www.nuget.org/packages/dotnet-sonarscanner) is available from .NET Core 3.1+.

```bash
dotnet tool install --global dotnet-sonarscanner --version x.x.x
```

The `--version` argument is optional; if omitted, the latest version will be installed. The full list of release versions is available on the [NuGet page](https://www.nuget.org/packages/dotnet-sonarscanner#versions-body-tab).

If you can’t use the dotnet install tool, other versions are available for download in the SonarScanner Update Center collapsible (access above, select **Show more**).

#### **Standalone executable**

You can install the SonarScanner for .NET via the *.NET Core* hyperlink in the Sonar Update Center panel above, or directly from the [releases page](https://github.com/SonarSource/sonar-scanner-msbuild/releases).

* Expand the downloaded file into the directory of your choice. We’ll refer to it as `<INSTALL_DIRECTORY>` in the next steps.
  * On Windows, you might need to unblock the ZIP file first (right-click **file** > **Properties** > **Unblock**).
  * On Linux/OSX you may need to set execute permissions on the files in `<INSTALL_DIRECTORY>/sonar-scanner-(version)/bin`.
* Uncomment, and update the global settings to point to your instance of SonarQube Server by editing `<INSTALL_DIRECTORY>/SonarQube.Analysis.xml`. Values set in this file will be applied to all analyses of all projects unless overwritten locally. Consider setting file system permissions to restrict access to this file.

```xml
<SonarQubeAnalysisProperties  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://www.sonarsource.com/msbuild/integration/2015/1">
  <Property Name="sonar.host.url">http://localhost:9000</Property>
  <Property Name="sonar.token">[my-user-token]</Property>
</SonarQubeAnalysisProperties>
```

* Add `<INSTALL_DIRECTORY>` to your `PATH` environment variable.

Previous versions of the .NET Framework SonarScanner are available on the releases page or found by expanding the SonarScanner for .NET version Update Center expandable box, above.
{% endtab %}

{% tab title=".NET FRAMEWORK" %}

### **Install scanner for .NET Framework**

You can install the SonarScanner for .NET by downloading a standalone file to execute.

#### **Standalone executable**

You can install the SonarScanner for .NET via the *.NET Framework* hyperlink in the Sonar Update Center panel above, or directly from the [releases page](https://github.com/SonarSource/sonar-scanner-msbuild/releases).

* Expand the downloaded file into the directory of your choice. We’ll refer to it as `<INSTALL_DIRECTORY>` in the next steps.
  * On Windows, you might need to unblock the ZIP file first (right-click **File** > **Properties** > **Unblock**).
  * On Linux/OSX you may need to set execute permissions on the files in `<INSTALL_DIRECTORY>/sonar-scanner-(version)/bin`.
* Uncomment, and update the global settings to point to your SonarQube Server’s instance by editing `<INSTALL_DIRECTORY>/SonarQube.Analysis.xml`. Values set in this file will be applied to all analyses of all projects unless overwritten locally. Consider setting file system permissions to restrict access to this file.

```xml
<SonarQubeAnalysisProperties  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://www.sonarsource.com/msbuild/integration/2015/1">
  <Property Name="sonar.host.url">http://localhost:9000</Property>
  <Property Name="sonar.token">[my-user-token]</Property>
</SonarQubeAnalysisProperties>
```

* Add `<INSTALL_DIRECTORY>` to your `PATH` environment variable.

Previous versions of the .NET Framework SonarScanner are available on the releases page or found by expanding the SonarScanner for .NET version Update Center expandable box, above.
{% endtab %}
{% endtabs %}

### Setting up your pipeline <a href="#your-pipeline" id="your-pipeline"></a>

How you set up the SonarScanner for .NET in your pipeline depends on your production environment. Here we will give a high-level overview, and link to pages with more detail, covering the most common CI environments:

#### Basic steps <a href="#basic-steps" id="basic-steps"></a>

For the most part, your pipeline should include these basic steps to run properly:

1. Check and install the [#prerequisites](https://docs.sonarsource.com/sonarqube-server/scanners/dotnet/installing#prerequisites "mention") in your environment (Java).
2. Download the correct SonarScanner version for your .NET runtime, and install it on your CI.
3. Then, as described on the [using](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/dotnet/using "mention") page:
   * specify your Begin step arguments to prepare your project for analysis,
   * build your project which will generate the analysis data,
   * and define the End step arguments to collect the analysis data.
4. Finally, focus your analysis as part of your build process by setting up your [dotnet-test-coverage](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/test-coverage/dotnet-test-coverage "mention") using a third-party tool to access important metrics.

For more details, select the tab box below that matches your CI:

{% tabs %}
{% tab title="AZURE" %}
**Azure DevOps Pipelines**

SonarQube Server can be integrated with both Azure DevOps Server and Azure DevOps Services. To get your analysis up and running, you will need to:

* add an Azure Personal Access Token (PAT) to your instance of SonarQube Server.
* install the [SonarQube Server extension](https://marketplace.visualstudio.com/items?itemName=SonarSource.sonarqube) from the Visual Studio Marketplace. The Azure DevOps Extension for SonarQube Server embeds the most recent SonarScanner for .NET. Check [the extension’s page](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/sonarqube-extension-for-azure-devops) for more details.
* add a new SonarQube Server service endpoint.
* finally, configure your Azure pipeline to send the analysis results to SonarQube Server.

The [dotnet-project](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/dotnet-project "mention") page has all of the details to complete this process.
{% endtab %}

{% tab title="GITHUB" %}
**GitHub Actions**

SonarQube Server can be integrated with both GitHub Enterprise and GitHub.com repositories. To get your analysis up and running, you will need to:

1. create a GitHub app. Please see GitHub’s documentation on [creating a GitHub App](https://docs.github.com/apps/building-github-apps/creating-a-github-app/).
2. install your GitHub App in your organization. GitHub has documentation on [installing GitHub Apps](https://docs.github.com/en/free-pro-team@latest/developers/apps/installing-github-apps).
3. update your SonarQube Server global settings with your GitHub App information. This information can be found on the [importing-github-repositories](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/github-integration/importing-github-repositories "mention") page.
4. finally, configure your .github/workflows/build.yml file so that the SonarScanner and GitHub can talk together to send your analysis results to SonarQube Server.

The [introduction](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/github-integration/introduction "mention") page is your entry point to find all of the details to complete this process.
{% endtab %}

{% tab title="GITLAB" %}
**GitLab integration**

SonarQube Server can be integrated with GitLab self-managed and GitLab SaaS subscription repositories. To get your analysis up and running, you will need to:

1. set your environment variables for all pipelines in GitLab’s settings. You’ll need to generate a Sonar Token and define your Sonar Host URL.
2. finally, configure your .gitlab-ci.yml file so that the SonarScanner can be installed and send your analysis results to SonarQube Server. If you’re running SonarQube Commercial editions and GitLab Ultimate, you can report vulnerabilities directly in GitLab.

For more details about completing this process, check out the [adding-analysis-to-gitlab-ci-cd](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/gitlab-integration/adding-analysis-to-gitlab-ci-cd "mention") page.

Here is a code sample for your gitlab-ci.yml file:

<details>

<summary>SonarScanner for .NET</summary>

**Configure your .gitlab-ci.yml file for .NET**

```yml
sonarqube-check:
  image: mcr.microsoft.com/dotnet/core/sdk:latest
  variables:
    SONAR_USER_HOME: "${CI_PROJECT_DIR}/.sonar"  # Defines the location of the analysis task cache
    GIT_DEPTH: "0"  # Tells git to fetch all the branches of the project, required by the analysis task
  cache:
    key: "${CI_JOB_NAME}"
    paths:
      - .sonar/cache
  script: 
      - "apt-get update"
      - "apt-get install --yes openjdk-17-jre"
      - "dotnet tool install --global dotnet-sonarscanner"
      - "export PATH=\"$PATH:$HOME/.dotnet/tools\""
      - "dotnet sonarscanner begin /k:\"projectKey" /d:sonar.token=\"$SONAR_TOKEN\" /d:\"sonar.host.url=$SONAR_HOST_URL\" "  #Replace "projectKey" with your project key
      - "dotnet build"
      - "dotnet sonarscanner end /d:sonar.token=\"$SONAR_TOKEN\""
  allow_failure: true
  only:
    - merge_requests
    - master
    - main
    - develop
```

</details>
{% endtab %}

{% tab title="JENKINS" %}
**Jenkins integration**

A SonarQube Server analysis using the SonarScanner for .NET can be triggered from Jenkins using the standard Jenkins Build Steps or the Jenkins Pipeline DSL. To get your analysis up and running, you will need to:

1. Install the [jenkins-extension-sonarqube](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/jenkins-extension-sonarqube "mention") via the [Jenkins Update Center](https://plugins.jenkins.io/sonar/).
2. To trigger your analysis, add the SonarScanner for .NET to the Jenkins Global Tool Configuration. [global-setup](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/ci-integration/jenkins-integration/global-setup "mention") provides complete instructions.
3. Finally, construct your Jenkins pipeline, adding a `withSonarQubeEnv` block that allows you to select SonarQube Server.

Additional configurations are available to manage your pipeline for [global-setup](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/ci-integration/jenkins-integration/global-setup "mention") and [pipeline-pause](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/ci-integration/jenkins-integration/pipeline-pause "mention") while the quality gate is computed. The *Jenkins* *extension for SonarQube* and [global-setup](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/ci-integration/jenkins-integration/global-setup "mention") pages will have complete details.
{% endtab %}

{% tab title="BITBUCKET" %}
**Bitbucket integration**

SonarQube Server integrates well with Bitbucket Cloud. To get your analysis up and running, you will need to:

1. import your Bitbucket Cloud repository into SonarQube Server.
2. finally, set up your pipeline to install the SonarScanner for .NET by [#configuring-your-bitbucket-pipelines.yml-file](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/bitbucket-integration/bitbucket-cloud-integration/bitbucket-pipelines#configuring-your-bitbucket-pipelines.yml-file "mention").

It’s possible to configure more details like *reporting your quality gate status in Bitbucket Cloud* or *failing the pipeline when the quality gate fails*. Check the [bitbucket-cloud-integration](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/bitbucket-integration/bitbucket-cloud-integration "mention") page for full details.
{% endtab %}
{% endtabs %}

### Managing your analysis <a href="#managing-your-analysis" id="managing-your-analysis"></a>

Once your CI pipeline is up and running, you can improve it to integrate pull request analyses and use your quality gate status to prevent merges when the quality gate fails. Each CI, as linked to above, manages pull requests in different ways and you’ll have to check the appropriate tab item for your CI to get the details.

The [pull request analysis introduction](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/pull-request-analysis) page provides an overview of how pull requests work in SonarQube Server. The [setting-up-the-pull-request-analysis](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/pull-request-analysis/setting-up-the-pull-request-analysis "mention") page will provide you with information about pull request parameters before pointing you to pages that help configure the quality gate status.

Essentially, the main steps of the analysis process are:

1. Your build or CI pipeline starts the SonarScanner.
2. The SonarScanner scans the local repository and determines the files to be analyzed according to the configured analysis scope.
3. The scanner sends an analysis request to the respective language analyzer which retrieves the files to be analyzed from the file system and analyzes them according to the configured [quality profiles](https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/managing-quality-profiles).
4. The analyzer sends the analysis results to the scanner which forwards them to SonarQube Server in the form of a report. See also the [metrics-definition](https://docs.sonarsource.com/sonarqube-server/user-guide/code-metrics/metrics-definition "mention") and [solution-overview](https://docs.sonarsource.com/sonarqube-server/user-guide/issues/solution-overview "mention") pages.
5. SonarQube Server computes the analysis results asynchronously to perform the following:
   * It identifies the new issues according to the configured [new code definition](https://docs.sonarsource.com/sonarqube-server/user-guide/about-new-code) and raises them in both the new code and the overall code (It uploads the code as part of the analysis and shows users the code that it raised issues on. Unanalyzed changes in the code are not visible.).
   * It computes the [quality gates](https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/managing-quality-gates/introduction-to-quality-gates).
   * It generates reports.

The next article, [#test-coverage](#test-coverage "mention"), explains how SonarQube Server reports work.

### Test Coverage <a href="#test-coverage" id="test-coverage"></a>

Test coverage reports and test execution reports are important metrics to help you assess the quality of your code.

* Test coverage reports tell you what percentage of your code is covered by test cases.
* Test execution reports tell you which tests have been run and their results.

To track code coverage in Sonar, you must use one of the supported coverage tools during your test run before the scanner can pick up the report. For instructions and examples of how to manage code coverage, refer to the [dotnet-test-coverage](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/test-coverage/dotnet-test-coverage "mention") page.

Running a standard project analysis is slightly different than running an analysis on a test project. Please see the [specify-test-project-analysis](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/dotnet-environments/specify-test-project-analysis "mention") page for more complete details.

If you’re still confused about code coverage and test data, we prepared some Community guides that might be helpful. A full list of guides on the [troubleshooting](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/dotnet-environments/troubleshooting "mention") page.

# Source: https://xunit.net/

Title: Home | xUnit.net

URL Source: https://xunit.net/

Published Time: Mon, 09 Mar 2026 16:09:07 GMT

Markdown Content:
[![Image 1: .NET Foundation logo](https://raw.githubusercontent.com/xunit/media/main/dotnet-foundation.svg)](https://raw.githubusercontent.com/xunit/media/main/dotnet-foundation.svg)

About x Unit.net
----------------

xUnit.net is a free, open source, community-focused unit testing tool for C#, F#, and Visual Basic. xUnit.net v3 supports .NET 8.0 or later, and .NET Framework 4.7.2 or later.

xUnit.net works with the [.NET SDK](https://dotnet.microsoft.com/download) command line tools, [Visual Studio](https://visualstudio.microsoft.com/), [Visual Studio Code](https://code.visualstudio.com/), [JetBrains Rider](https://www.jetbrains.com/rider/), [NCrunch](https://www.ncrunch.net/), and any development environment compatible with [Microsoft.Testing.Platform](https://learn.microsoft.com/dotnet/core/testing/microsoft-testing-platform-intro) or [VSTest](https://github.com/microsoft/vstest).

xUnit.net is part of the [.NET Foundation](https://www.dotnetfoundation.org/) and operates under their [code of conduct](https://www.dotnetfoundation.org/code-of-conduct). It is licensed under [Apache 2](https://opensource.org/licenses/Apache-2.0) (an OSI approved license). The project is [governed](https://xunit.net/governance) by a Project Lead.

> Follow: [xUnit.net on Mastodon](https://dotnet.social/@xunit), [xUnit.net on Bluesky](https://bsky.app/profile/xunit.net), [Brad Wilson](https://bradwilson.dev/), [James Newkirk](https://www.jamesnewkirk.com/)
> 
>  JetBrains Rider support is provided and supported by [JetBrains](https://www.jetbrains.com/).
> 
>  NCrunch support is provided and supported by [Remco Software](https://www.ncrunch.net/).
> 
>  The xUnit.net logo was designed by [Nathan Young](https://mas.to/@nathanyoung).

Quick Start with .NET SDK[](https://xunit.net/#quick-start)
-----------------------------------------------------------

*   [C#](https://xunit.net/#tabpanel_1_cs)
*   [F#](https://xunit.net/#tabpanel_1_fs)
*   [Visual Basic](https://xunit.net/#tabpanel_1_vb)

Install the xUnit.net v3 project templates:

```
dotnet new install xunit.v3.templates
```
[](https://xunit.net/# "Copy")
```
The following template packages will be installed:
    xunit.v3.templates

Success: xunit.v3.templates::2.0.3 installed the following templates:
Template Name                   Short Name        Language    Tags
------------------------------  ----------------  ----------  ----------
xUnit.net v3 Extension Project  xunit3-extension  [C#],F#,VB  Test/xUnit
xUnit.net v3 Test Project       xunit3            [C#],F#,VB  Test/xUnit
```
[](https://xunit.net/# "Copy")
Create a unit test project:

```
dotnet new xunit3 --language C#
```
[](https://xunit.net/# "Copy")
```
The template "xUnit.net v3 Test Project" was created successfully.

Processing post-creation actions...
Restoring C:\Dev\SampleProject\SampleProject.csproj:
Restore succeeded.
```
[](https://xunit.net/# "Copy")
Edit `UnitTest1.cs`:

```
namespace SampleProject;

public class UnitTest1
{
    public static int Add(int x, int y) =>
        x + y;

    [Fact]
    public void Good() =>
        Assert.Equal(4, Add(2, 2));

    [Fact]
    public void Bad() =>
        Assert.Equal(5, Add(2, 2));
}
```
[](https://xunit.net/# "Copy")
Execute the tests:

```
dotnet run
```
[](https://xunit.net/# "Copy")
```
xUnit.net v3 In-Process Runner v2.0.3+216a74a292 (64-bit .NET 8.0.17)
  Discovering: SampleProject
  Discovered:  SampleProject
  Starting:    SampleProject
    SampleProject.UnitTest1.Bad [FAIL]
      Assert.Equal() Failure: Values differ
      Expected: 5
      Actual:   4
      Stack Trace:
        UnitTest1.cs(14,0): at SampleProject.UnitTest1.Bad()
  Finished:    SampleProject
=== TEST EXECUTION SUMMARY ===
    SampleProject  Total: 2, Errors: 0, Failed: 1, Skipped: 0, Not Run: 0, Time: 0.054s
```
[](https://xunit.net/# "Copy")

Latest Release Notes[](https://xunit.net/#release-notes)
--------------------------------------------------------

|  | Stable | Prerelease |
| --- | --- | --- |
| Core Framework v3 | [3.2.2](https://xunit.net/releases/v3/3.2.2) | _None_ |
| Core Framework v2 | [2.9.3](https://xunit.net/releases/v2/2.9.3) | _None_ |
| Analyzers | [1.27.0](https://xunit.net/releases/analyzers/1.27.0) | _None_ |
| Visual Studio adapter | [3.1.5](https://xunit.net/releases/visualstudio/3.1.5) | _None_ |

_For older release notes, see the [full release notes list](https://xunit.net/releases/)._

Latest Nu Get Packages[](https://xunit.net/#packages)
-----------------------------------------------------

|  | Latest stable | Latest CI ([how to use](https://xunit.net/docs/using-ci-builds)) | Build status |
| --- | --- | --- | --- |
| `xunit.v3` | [![Image 2](https://img.shields.io/nuget/v/xunit.v3.svg?logo=nuget)](https://www.nuget.org/packages/xunit.v3) | [![Image 3](https://img.shields.io/endpoint.svg?url=https://f.feedz.io/xunit/xunit/shield/xunit.v3/latest&logo=nuget&color=f58142)](https://feedz.io/org/xunit/repository/xunit/packages/xunit.v3) | [![Image 4](https://img.shields.io/endpoint.svg?url=https://actions-badge.atrox.dev/xunit/xunit/badge%3Fref%3Dmain&label=build)](https://actions-badge.atrox.dev/xunit/xunit/goto?ref=main) |
| `xunit` | [![Image 5](https://img.shields.io/nuget/v/xunit.svg?logo=nuget)](https://www.nuget.org/packages/xunit) | [![Image 6](https://img.shields.io/endpoint.svg?url=https://f.feedz.io/xunit/xunit/shield/xunit/latest&logo=nuget&color=f58142)](https://feedz.io/org/xunit/repository/xunit/packages/xunit) | [![Image 7](https://img.shields.io/endpoint.svg?url=https://actions-badge.atrox.dev/xunit/xunit/badge%3Fref%3Dv2&label=build)](https://actions-badge.atrox.dev/xunit/xunit/goto?ref=v2) |
| `xunit.analyzers` | [![Image 8](https://img.shields.io/nuget/v/xunit.analyzers.svg?logo=nuget)](https://www.nuget.org/packages/xunit.analyzers) | [![Image 9](https://img.shields.io/endpoint.svg?url=https://f.feedz.io/xunit/xunit/shield/xunit.analyzers/latest&logo=nuget&color=f58142)](https://feedz.io/org/xunit/repository/xunit/packages/xunit.analyzers) | [![Image 10](https://img.shields.io/endpoint.svg?url=https://actions-badge.atrox.dev/xunit/xunit.analyzers/badge%3Fref%3Dmain&label=build)](https://actions-badge.atrox.dev/xunit/xunit.analyzers/goto?ref=main) |
| `xunit.runner.visualstudio` | [![Image 11](https://img.shields.io/nuget/v/xunit.runner.visualstudio.svg?logo=nuget)](https://www.nuget.org/packages/xunit.runner.visualstudio) | [![Image 12](https://img.shields.io/endpoint.svg?url=https://f.feedz.io/xunit/xunit/shield/xunit.runner.visualstudio/latest&logo=nuget&color=f58142)](https://feedz.io/org/xunit/repository/xunit/packages/xunit.runner.visualstudio) | [![Image 13](https://img.shields.io/endpoint.svg?url=https://actions-badge.atrox.dev/xunit/visualstudio.xunit/badge%3Fref%3Dmain&label=build)](https://actions-badge.atrox.dev/xunit/visualstudio.xunit/goto?ref=main) |

Issues and Discussions[](https://xunit.net/#issues)
---------------------------------------------------

*   Issues in the core framework and analyzers should be reported in the [primary issue tracker](https://github.com/xunit/xunit/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
*   Issues in `xunit.runner.visualstudio` should be reported in the [project issue tracker](https://github.com/xunit/visualstudio.xunit/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
*   Discussions are hosted in the [primary discussion forums](https://github.com/xunit/xunit/discussions?discussions_q=is%3Aunanswered+is%3Aopen)

Github Projects[](https://xunit.net/#github)
--------------------------------------------

*   [xUnit.net](https://github.com/xunit/xunit) (core framework, built-in runners)
*   [Assertion library](https://github.com/xunit/assert.xunit)
*   [Analyzers](https://github.com/xunit/xunit.analyzers)
*   [Visual Studio adapter](https://github.com/xunit/visualstudio.xunit)
*   [Media files](https://github.com/xunit/media)
*   [This site](https://github.com/xunit/xunit.net)

Links to Resources[](https://xunit.net/#links)
----------------------------------------------

*   [Visual Studio Community](https://visualstudio.microsoft.com/vs/community/)
*   [MSBuild Reference](https://docs.microsoft.com/visualstudio/msbuild/msbuild-reference)

[![Image 14: Powered by NDepend](https://raw.githubusercontent.com/xunit/media/refs/heads/main/powered-by-ndepend-transparent.svg)](https://www.ndepend.com/)

Help support this project by becoming a sponsor through [GitHub Sponsors](https://github.com/sponsors/xunit).

Additional copyrights[](https://xunit.net/#copyrights)
------------------------------------------------------

Portions copyright The Legion Of The Bouncy Castle

##### In this article

*   [Quick Start with .NET SDK](https://xunit.net/#quick-start)
*   [Latest Release Notes](https://xunit.net/#release-notes)
*   [Latest Nu Get Packages](https://xunit.net/#packages)
*   [Issues and Discussions](https://xunit.net/#issues)
*   [Github Projects](https://xunit.net/#github)
*   [Links to Resources](https://xunit.net/#links)
*   [Sponsors](https://xunit.net/#sponsors)
*   [Additional copyrights](https://xunit.net/#copyrights)

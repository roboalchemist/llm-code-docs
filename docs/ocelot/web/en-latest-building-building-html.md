# Source: https://ocelot.readthedocs.io/en/latest/building/building.html

Title: Building — Ocelot Gateway 24.1 "Globality" documentation

URL Source: https://ocelot.readthedocs.io/en/latest/building/building.html

Markdown Content:
This document summarises the build and release process for the [Ocelot](https://github.com/ThreeMammals/Ocelot) project. The build scripts are written using [Cake](https://cakebuild.net/) (C# Make), with relevant build tasks defined in the ‘[build.cake](https://github.com/ThreeMammals/Ocelot/blob/main/build.cake)’ file located in the root of the [Ocelot](https://github.com/ThreeMammals/Ocelot) project. The scripts are designed to be run by developers locally in a [Bash](https://www.gnu.org/software/bash) terminal (on any OS), in Command Prompt (CMD) or PowerShell consoles (on Windows OS), or by a CI/CD server (currently [GitHub Actions](https://docs.github.com/en/actions)), with minimal logic defined in the build server itself.

The final goal of the build process is to create `Ocelot.*`[NuGet](https://www.nuget.org/profiles/ThreeMammals) packages (.nupkg files) for redistribution via the [NuGet](https://www.nuget.org/profiles/ThreeMammals) repository or manually. The build process consists of several steps: (1) compilation, (2) testing, (3) creating and publishing [NuGet](https://www.nuget.org/profiles/ThreeMammals) packages, and (4) making an official GitHub release. The build process requires pre-installed .NET SDKs on the build machine (host) for all target framework monikers: TFMs are `net8.0` and `net9.0` currently. In general, the build process is the same across all environments and tools, with a few differences described below.

In IDE[¶](https://ocelot.readthedocs.io/en/latest/building/building.html#in-ide "Link to this heading")
-------------------------------------------------------------------------------------------------------

In an IDE, a DevOps engineer can build the project in Visual Studio IDE or another IDE in [Release configuration](https://learn.microsoft.com/en-us/visualstudio/debugger/how-to-set-debug-and-release-configurations?view=vs-2022) mode, but the latest .NET 8/9 SDKs must be pre-installed on the local machine. However, this approach is not practical because the generated ‘.nupkg’ files must be uploaded to [NuGet](https://www.nuget.org/profiles/ThreeMammals) manually, and the GitHub release must also be created manually. A better approach is to utilize the ‘[build.cake](https://github.com/ThreeMammals/Ocelot/blob/main/build.cake)’ script [In terminal](https://ocelot.readthedocs.io/en/latest/building/building.html#b-in-terminal), which covers all building scenarios.

In terminal[¶](https://ocelot.readthedocs.io/en/latest/building/building.html#in-terminal "Link to this heading")
-----------------------------------------------------------------------------------------------------------------

> Folder: [./](https://github.com/ThreeMammals/Ocelot/tree/main/)

These are local machine or remote server building scenarios using build scripts, aka ‘[build.cake](https://github.com/ThreeMammals/Ocelot/blob/main/build.cake)’. In these scenarios, the following two commands should be run in a terminal from the project’s root folder:

dotnet tool restore && dotnet cake # In Bash terminal
dotnet tool restore; dotnet cake # In PowerShell terminal

> **Note**: The default target task (“Default”) is “Build”, and output files will be stored in the `./artifacts` directory.

To run a desired target task, you need to specify its _name_:

dotnet tool restore && dotnet cake --target=name # In Bash terminal
dotnet tool restore; dotnet cake --target=name # In PowerShell terminal

For example,

*   dotnet cake --target=Build 
It runs a local build, performing compilation and testing only.

*   dotnet cake --target=Version 
It checks the next version to be tagged in the Git repository during the next release, without performing compilation or testing tasks.

*   dotnet cake --target=CreateReleaseNotes 
It generates Release Notes artifacts in the `/artifacts/Packages` folder using the `ReleaseNotes.md` template file.

*   dotnet cake --target=Release 
It creates a release, consisting of the following steps: compilation, testing, generating release notes, creating .nupkg files, publishing [NuGet](https://www.nuget.org/profiles/ThreeMammals) packages, and finally, making a GitHub release.

> **Note 1**: The building tools for the `dotnet tool restore` command are configured in the [dotnet-tools.json](https://github.com/ThreeMammals/Ocelot/blob/main/.config/dotnet-tools.json) file.
> 
> 
> **Note 2**: Some targets (build tasks) require appropriate environment variables to be defined directly in the terminal session (aka secret tokens).

With Docker[¶](https://ocelot.readthedocs.io/en/latest/building/building.html#with-docker "Link to this heading")
-----------------------------------------------------------------------------------------------------------------

The best way to replicate the CI/CD process and build [Ocelot](https://github.com/ThreeMammals/Ocelot) locally is by using the [Dockerfile.build](https://github.com/ThreeMammals/Ocelot/blob/main/docker/Dockerfile.build) file, which can be found in the ‘[docker](https://github.com/ThreeMammals/Ocelot/tree/main/docker)’ folder in the [Ocelot](https://github.com/ThreeMammals/Ocelot) root directory. For example, use the following command:

docker build --platform linux/amd64 -f ./docker/Dockerfile.build .

You may need to adjust the platform flag depending on your system.

> **Note**: This approach is somewhat excessive, but it will work if you are a masterful Docker user. 🙂 The Ocelot team has not followed this approach since version [24.0](https://github.com/ThreeMammals/Ocelot/releases/tag/24.0.0), favoring [With CI/CD](https://ocelot.readthedocs.io/en/latest/building/building.html#b-with-ci-cd)-based builds and occasionally building [In terminal](https://ocelot.readthedocs.io/en/latest/building/building.html#b-in-terminal) instead.

With CI/CD[¶](https://ocelot.readthedocs.io/en/latest/building/building.html#with-ci-cd "Link to this heading")
---------------------------------------------------------------------------------------------------------------

The [Ocelot](https://github.com/ThreeMammals/Ocelot) project utilizes [GitHub Actions](https://docs.github.com/en/actions) as a CI/CD provider, offering seamless integrations with the GitHub ecosystem and APIs. Starting from version [24.0](https://github.com/ThreeMammals/Ocelot/releases/tag/24.0.0), all pull requests, development commits, and releases are built using [GitHub Actions](https://docs.github.com/en/actions) workflows. There are three [workflows](https://github.com/ThreeMammals/Ocelot/tree/main/.github/workflows): one for pull requests ([PR](https://github.com/ThreeMammals/Ocelot/actions/workflows/pr.yml)), one for the `develop` branch ([Develop](https://github.com/ThreeMammals/Ocelot/actions/workflows/develop.yml)), and one for the `main` branch ([Release](https://github.com/ThreeMammals/Ocelot/actions/workflows/release.yml)).

> **Note**: Each workflow has a dedicated status badge in the [Ocelot README](https://github.com/ThreeMammals/Ocelot/blob/main/README.md): the [![Image 1: Release Status](https://github.com/ThreeMammals/Ocelot/actions/workflows/release.yml/badge.svg)](https://github.com/ThreeMammals/Ocelot/actions/workflows/release.yml) button and the [![Image 2: Development Status](https://github.com/ThreeMammals/Ocelot/actions/workflows/develop.yml/badge.svg)](https://github.com/ThreeMammals/Ocelot/actions/workflows/develop.yml) button, with the [PR](https://github.com/ThreeMammals/Ocelot/actions/workflows/pr.yml) status being published directly in a pull request under the “Checks” tab.

The [PR](https://github.com/ThreeMammals/Ocelot/actions/workflows/pr.yml) workflow will track code coverage using [Coveralls](https://coveralls.io/). After opening a pull request or submitting a new commit to a pull request, [Coveralls](https://coveralls.io/) will publish a short message with the current code coverage once the top commit is built. Considering that [Coveralls](https://coveralls.io/) retains the entire history but does not fail the build if coverage falls below the threshold, all workflows have a built-in 80% threshold, applied internally within the `build-cake` job, particularly during the “[Cake Build](https://github.com/search?q=repo%3AThreeMammals%2FOcelot+%22cake-build%2F%22+path%3A%2F%5E%5C.github%5C%2Fworkflows%5C%2F%2F&type=code)” step-action. If the code coverage of a newly opened pull request drops below the 80% threshold, the [‘build-cake’ job](https://github.com/search?q=repo%3AThreeMammals%2FOcelot+%22-cake%3A%22+path%3A%2F%5E%5C.github%5C%2Fworkflows%5C%2F%2F&type=code) will fail, logging an appropriate message in the “[Cake Build](https://github.com/search?q=repo%3AThreeMammals%2FOcelot+%22cake-build%2F%22+path%3A%2F%5E%5C.github%5C%2Fworkflows%5C%2F%2F&type=code)” step.

> **Note 1**: There are special code coverage badges in [Ocelot README](https://github.com/ThreeMammals/Ocelot/blob/main/README.md): the [Develop](https://github.com/ThreeMammals/Ocelot/actions/workflows/develop.yml)[![Image 3: Coveralls Status](https://coveralls.io/repos/github/ThreeMammals/Ocelot/badge.svg?branch=develop)](https://coveralls.io/github/ThreeMammals/Ocelot?branch=develop) button and the [Release](https://github.com/ThreeMammals/Ocelot/actions/workflows/release.yml)[![Image 4: Coveralls Status](https://coveralls.io/repos/github/ThreeMammals/Ocelot/badge.svg?branch=main)](https://coveralls.io/github/ThreeMammals/Ocelot?branch=main) button.
> 
> 
> **Note 2**: The current code coverage of the [Ocelot](https://github.com/ThreeMammals/Ocelot) project is around 85-86%. The coverage threshold is subject to change in upcoming releases. All [Coveralls](https://coveralls.io/) builds can be viewed by navigating to the [ThreeMammals/Ocelot](https://coveralls.io/github/ThreeMammals/Ocelot) project on Coveralls.io.

Documentation[¶](https://ocelot.readthedocs.io/en/latest/building/building.html#documentation "Link to this heading")
---------------------------------------------------------------------------------------------------------------------

Documentation building is configured using the ‘[.readthedocs.yaml](https://github.com/ThreeMammals/Ocelot/blob/main/.readthedocs.yaml)’ integration file, which allows builds to run separately via the [Read the Docs](https://about.readthedocs.com/) publisher. All build artifacts and document sources are located in the ‘[docs](https://github.com/ThreeMammals/Ocelot/tree/main/docs)’ folder. More details on the documentation build process can be found in the [README](https://github.com/ThreeMammals/Ocelot/blob/main/docs/readme.md).

> **Note 1**: Documentation builds have a dedicated status badges in [Ocelot README](https://github.com/ThreeMammals/Ocelot/blob/main/README.md): the [Develop](https://github.com/ThreeMammals/Ocelot/actions/workflows/develop.yml)[![Image 5: ReadTheDocs Status](https://readthedocs.org/projects/ocelot/badge/?version=develop&style=flat-square)](https://app.readthedocs.org/projects/ocelot/builds/?version__slug=develop) button and the [Release](https://github.com/ThreeMammals/Ocelot/actions/workflows/release.yml)[![Image 6: ReadTheDocs Status](https://readthedocs.org/projects/ocelot/badge/?version=latest&style=flat-square)](https://app.readthedocs.org/projects/ocelot/builds/?version__slug=latest) button.
> 
> 
> **Note**: Documentation can be easily built locally in a terminal from the ‘[docs](https://github.com/ThreeMammals/Ocelot/tree/main/docs)’ folder by running the `make.sh` or `make.bat` scripts. The resulting documentation build files will be located in the `./docs/_build` folder, with the HTML documentation specifically written to the `./docs/_build/html` folder.

Testing[¶](https://ocelot.readthedocs.io/en/latest/building/building.html#testing "Link to this heading")
---------------------------------------------------------------------------------------------------------

The tests should run and function correctly as part of the _building_ process using the `dotnet test` command. You can also run them in Visual Studio IDE within the Test Explorer window. Depending on your build scenario, [Ocelot](https://github.com/ThreeMammals/Ocelot)_testing_ can be performed as follows.

[In IDE](https://ocelot.readthedocs.io/en/latest/building/building.html#b-in-ide): Simply run tests via the Test Explorer window of Visual Studio IDE.

[In terminal](https://ocelot.readthedocs.io/en/latest/building/building.html#b-in-terminal): There are two main approaches:

1.   Run the `dotnet test` command to perform all tests (unit, integration, and acceptance):

dotnet test -f net8.0 ./Ocelot.sln 
Or run tests separately per project:

dotnet test -f net8.0 ./test/Ocelot.UnitTests/Ocelot.UnitTests.csproj # Unit tests only
dotnet test -f net8.0 ./test/Ocelot.IntegrationTests/Ocelot.IntegrationTests.csproj # Integration tests only
dotnet test -f net8.0 ./test/Ocelot.AcceptanceTests/Ocelot.AcceptanceTests.csproj # Acceptance tests only 
2.   Run `dotnet cake` command: `dotnet cake --target=Tests` to perform all tests (unit, integration and acceptance). Or run tests separately per _testing_ project:

dotnet cake --target=UnitTests # unit tests only
dotnet cake --target=IntegrationTests # integration tests only
dotnet cake --target=AcceptanceTests # acceptance tests only 

[With Docker](https://ocelot.readthedocs.io/en/latest/building/building.html#b-with-docker): This approach is not recommended. Instead, perform automated testing [With CI/CD](https://ocelot.readthedocs.io/en/latest/building/building.html#b-with-ci-cd) or opt for [In terminal](https://ocelot.readthedocs.io/en/latest/building/building.html#b-in-terminal)-based testing, which is a more advanced method.

[With CI/CD](https://ocelot.readthedocs.io/en/latest/building/building.html#b-with-ci-cd): In [GitHub Actions](https://docs.github.com/en/actions)[workflows](https://github.com/ThreeMammals/Ocelot/tree/main/.github/workflows), the _testing_ process consists of separate testing steps, organized per job:

*   In the [‘build’ job](https://github.com/search?q=repo%3AThreeMammals%2FOcelot+build%3A+path%3A%2F%5E%5C.github%5C%2Fworkflows%5C%2F%2F&type=code): There are ‘[Unit Tests](https://github.com/search?q=repo%3AThreeMammals%2FOcelot+%22Unit+Tests%22+path%3A%2F%5E%5C.github%5C%2Fworkflows%5C%2F%2F&type=code)’, ‘[Integration Tests](https://github.com/search?q=repo%3AThreeMammals%2FOcelot+%22Integration+Tests%22+path%3A%2F%5E%5C.github%5C%2Fworkflows%5C%2F%2F&type=code)’, and ‘[Acceptance Tests](https://github.com/search?q=repo%3AThreeMammals%2FOcelot+%22Acceptance+Tests%22+path%3A%2F%5E%5C.github%5C%2Fworkflows%5C%2F%2F&type=code)’ steps.

*   In the [‘build-cake’ job](https://github.com/search?q=repo%3AThreeMammals%2FOcelot+%22-cake%3A%22+path%3A%2F%5E%5C.github%5C%2Fworkflows%5C%2F%2F&type=code): There is a ‘[Cake Build](https://github.com/search?q=repo%3AThreeMammals%2FOcelot+%22cake-build%2F%22+path%3A%2F%5E%5C.github%5C%2Fworkflows%5C%2F%2F&type=code)’ step responsible for performing tests internally.

SSL certificate[¶](https://ocelot.readthedocs.io/en/latest/building/building.html#ssl-certificate "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------

To create a certificate for [Testing](https://ocelot.readthedocs.io/en/latest/building/building.html#b-testing), you can use [OpenSSL](https://www.openssl.org/):

*   Install the [openssl](https://github.com/openssl/openssl) package (if you are using Windows, download the binaries [here](https://www.openssl.org/source/)).

*   Generate a private key:

openssl genrsa 2048 > private.pem 
*   Generate a self-signed certificate:

openssl req -x509 -days 1000 -new -key private.pem -out public.pem 
*   If needed, create a PFX file:

openssl pkcs12 -export -in public.pem -inkey private.pem -out mycert.pfx

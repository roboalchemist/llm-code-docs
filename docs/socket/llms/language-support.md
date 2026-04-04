# Source: https://docs.socket.dev/docs/language-support.md

# Ecosystem Support

Languages ecosystems, programming languages, package managers, and features that Socket supports.

# Ecosystem Maturity Levels

Socket language ecosystems are classified into three maturity levels:

* Generally Available (GA)
* Beta
* Experimental

The differences are as follows:

| Feature                                                     | GA                                                                                                        | Beta                                                                                                      | Experimental                                                                                              |
| :---------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------- |
| **Availability**                                            | Available for **all** Socket users.                                                                       | Available for **all** Socket users.                                                                       | Enterprise plan users can [contact us](https://docs.socket.dev/docs/contact-support) to get access.       |
| **[Alert Types](https://docs.socket.dev/docs/issues-list)** | Supports **25+** alert types (including Supply Chain Risk, CVE, Quality, Maintenance, and License types). | Supports **20+** alert types (including Supply Chain Risk, CVE, Quality, Maintenance, and License types). | Supports **15+** alert types (including Supply Chain Risk, CVE, Quality, Maintenance, and License types). |
| **Support**                                                 | Premium support from the Socket team. Any reported issues are resolved promptly.                          | Support from the Socket team. Any reported issues are resolved promptly, but after GA ecosystems.         | Reported issues are tracked and prioritized with best effort.                                             |

# Ecosystem Support

<Table align={["left","left","left","left","left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Ecosytem
      </th>

      <th style={{ textAlign: "left" }}>
        Package manager
      </th>

      <th style={{ textAlign: "left" }}>
        Maturity level
      </th>

      <th style={{ textAlign: "left" }}>
        Next-gen SCA
      </th>

      <th style={{ textAlign: "left" }}>
        Socket scores
      </th>

      <th style={{ textAlign: "left" }}>
        [Reachability analysis](https://docs.socket.dev/docs/reachability-analysis)
      </th>

      <th style={{ textAlign: "left" }}>
        Autofix
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        **[JavaScript and TypeScript](https://docs.socket.dev/docs/language-support#javascript-and-typescript)**
      </td>

      <td style={{ textAlign: "left" }}>
        npm, yarn, pnpm, Bun†, VLT†
      </td>

      <td style={{ textAlign: "left" }}>
        GA
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **[Python](https://docs.socket.dev/docs/language-support#python)**
      </td>

      <td style={{ textAlign: "left" }}>
        uv, pip, Poetry, Anaconda
      </td>

      <td style={{ textAlign: "left" }}>
        GA
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **[Go](https://docs.socket.dev/docs/language-support#go)**
      </td>

      <td style={{ textAlign: "left" }}>
        Go Modules
      </td>

      <td style={{ textAlign: "left" }}>
        GA
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **[Java](https://docs.socket.dev/docs/language-support#java)**
      </td>

      <td style={{ textAlign: "left" }}>
        Maven, Gradle
      </td>

      <td style={{ textAlign: "left" }}>
        GA
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>

      <td style={{ textAlign: "left" }}>
        ✅\*
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **[Ruby](#ruby)**
      </td>

      <td style={{ textAlign: "left" }}>
        Bundler
      </td>

      <td style={{ textAlign: "left" }}>
        GA
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **[.NET (C#, F#, Visual Basic)](https://docs.socket.dev/docs/language-support#net-c-f-visual-basic)**
      </td>

      <td style={{ textAlign: "left" }}>
        Nuget
      </td>

      <td style={{ textAlign: "left" }}>
        GA
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **[Scala](#scala)**
      </td>

      <td style={{ textAlign: "left" }}>
        sbt, Maven, Gradle
      </td>

      <td style={{ textAlign: "left" }}>
        GA
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>

      <td style={{ textAlign: "left" }}>
        ✅\*
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **[Kotlin](#kotlin)**
      </td>

      <td style={{ textAlign: "left" }}>
        Maven, Gradle
      </td>

      <td style={{ textAlign: "left" }}>
        GA
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>

      <td style={{ textAlign: "left" }}>
        ✅\*
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **[Rust](#rust)**
      </td>

      <td style={{ textAlign: "left" }}>
        cargo
      </td>

      <td style={{ textAlign: "left" }}>
        GA
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **[GitHub Actions](#github-actions)**
      </td>

      <td style={{ textAlign: "left" }}>
        GitHub Actions
      </td>

      <td style={{ textAlign: "left" }}>
        Experimental
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>

      <td style={{ textAlign: "left" }}>
        :x:
      </td>

      <td style={{ textAlign: "left" }}>
        :x:
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **PHP**
      </td>

      <td style={{ textAlign: "left" }}>
        Composer
      </td>

      <td style={{ textAlign: "left" }}>
        Experimental
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>

      <td style={{ textAlign: "left" }}>
        ⏳ Planned
      </td>

      <td style={{ textAlign: "left" }}>
        ⏳ Planned
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **Swift**\*\*
      </td>

      <td style={{ textAlign: "left" }}>
        Swift Package Manager
      </td>

      <td style={{ textAlign: "left" }}>
        GA
      </td>

      <td style={{ textAlign: "left" }}>
        ✅ CVE only
        🚧 [Full Support In Progress](https://feedback.socket.dev/feature-requests/p/swift-and-objective-c-cocoapods-and-swift-package-manager-support) (Q1)
      </td>

      <td style={{ textAlign: "left" }}>
        🚧
      </td>

      <td style={{ textAlign: "left" }}>
        :x:
      </td>

      <td style={{ textAlign: "left" }}>
        ⏳ Planned
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **[C/C++](#cc)**\*\*
      </td>

      <td style={{ textAlign: "left" }}>
        conan
      </td>

      <td style={{ textAlign: "left" }}>
        GA
      </td>

      <td style={{ textAlign: "left" }}>
        ✅ CVE only
      </td>

      <td style={{ textAlign: "left" }}>
        ⏳ Planned
      </td>

      <td style={{ textAlign: "left" }}>
        :x:
      </td>

      <td style={{ textAlign: "left" }}>
        ⏳ Planned
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **Julia**\*\*
      </td>

      <td style={{ textAlign: "left" }}>
        Pkg
      </td>

      <td style={{ textAlign: "left" }}>
        GA
      </td>

      <td style={{ textAlign: "left" }}>
        ✅ CVE only
      </td>

      <td style={{ textAlign: "left" }}>
        ⏳ Planned
      </td>

      <td style={{ textAlign: "left" }}>
        :x:
      </td>

      <td style={{ textAlign: "left" }}>
        ⏳ Planned
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **Dart**\*\*
      </td>

      <td style={{ textAlign: "left" }}>
        Pub
      </td>

      <td style={{ textAlign: "left" }}>
        GA
      </td>

      <td style={{ textAlign: "left" }}>
        ✅ CVE only
      </td>

      <td style={{ textAlign: "left" }}>
        ⏳ Planned
      </td>

      <td style={{ textAlign: "left" }}>
        :x:
      </td>

      <td style={{ textAlign: "left" }}>
        ⏳ Planned
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **Elixir and Erlang**\*\*
      </td>

      <td style={{ textAlign: "left" }}>
        hex
      </td>

      <td style={{ textAlign: "left" }}>
        GA
      </td>

      <td style={{ textAlign: "left" }}>
        ✅ CVE only
      </td>

      <td style={{ textAlign: "left" }}>
        ⏳ Planned
      </td>

      <td style={{ textAlign: "left" }}>
        :x:
      </td>

      <td style={{ textAlign: "left" }}>
        ⏳ Planned
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **Objective-C**
      </td>

      <td style={{ textAlign: "left" }}>
        CocoaPods
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        ⏳ [Planned](https://socketdev.canny.io/feature-requests/p/swift-and-objective-c-cocoapods-and-swift-package-manager-support) (Q2)
      </td>

      <td style={{ textAlign: "left" }}>
        ⏳ Planned
      </td>

      <td style={{ textAlign: "left" }}>
        :x:
      </td>

      <td style={{ textAlign: "left" }}>
        ⏳ Planned
      </td>
    </tr>
  </tbody>
</Table>

\*: Autofix for Gradle currently requires projects to use lock files.

\*\*: Requires [Socket Basics](https://socket.dev/blog/socket-basics) .

†: Bun and VLT package managers are currently in public beta.

> 👍 Vote for the languages you want us to support next!
>
> At Socket, we're committed to expanding our ecosystem support to support diverse programming languages and package managers. We're driven by the needs of our users so if there's a language you'd like us to support, we [encourage you let us know](https://socket.dev/contact). Your votes directly influence our prioritization. If you're considering becoming an enterprise customer, we'd [love to hear from you](https://socket.dev/demo) –  we can prioritize language support based on your needs. Please reach out to us to discuss your specific requirements.

# Extension Scanning

Socket has launched experimental protection for Chrome extensions and other extension ecosystems, scanning for malware and risky permissions to prevent silent supply chain attacks.

This is a new experimental product from Socket. [Contact us](https://docs.socket.dev/docs/contact-support) to get access.

| Ecosystem                                                                              | Maturity level | Support Level       |
| :------------------------------------------------------------------------------------- | :------------- | :------------------ |
| **Chrome extensions**                                                                  | Experimental   | ✅ Supported         |
| **OpenVSX extensions**                                                                 | Beta           | ✅ Supported         |
| **[Skills.sh](https://socket.dev/blog/socket-brings-supply-chain-security-to-skills)** | Experimental   | ✅ Supported         |
| **VSCode extensions**                                                                  |                | 🚧 In Progress (Q1) |
| **Firefox extensions**                                                                 |                | ⏳ Planned           |
| **Custom skills**                                                                      |                | ⏳ Planned           |

# AI model Scanning Support

Socket scans the contents of AI model files, including those used by popular LLMs, to scan for the full suite of [Socket Alerts](https://docs.socket.dev/docs/issues-list) .

| Package Manager   | Support Level | Notes                                                                                                                                                                                           |
| :---------------- | :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PyPI Pickle files | ✅ Supported   | Socket scans all pickle files within [PyPI packages](#python)                                                                                                                                   |
| Hugging Face      | ✅ Supported   | Socket scans *deserialization* and *runtime* threats from AI model files. The supported model formats include Pickle, PyTorch, Keras, Nemo, Joblib, TensorFlow, GGUF, Llamafile, LiteRT/TFLite. |

# JavaScript and TypeScript

Socket officially supports npm, yarn, and pnpm.

| Package Manager | Support Level        | Notes                         |
| :-------------- | :------------------- | :---------------------------- |
| npm             | ✅ [Supported](#npm)  | npm versions 6 - 11 (latest)  |
| Yarn            | ✅ [Supported](#yarn) | yarn versions 1 - 3           |
| pnpm            | ✅ [Supported](#pnpm) | pnpm versions 5 - 10 (latest) |

## npm

Socket supports npm (versions 6, 7, 8, and 9).

| Feature                                                                                   | Support Level | Notes                                         |
| :---------------------------------------------------------------------------------------- | :------------ | :-------------------------------------------- |
| [npm lockfile](https://docs.npmjs.com/files/package-lock.json/) (`package-lock.json`)     | ✅ Supported   | Socket supports lockfile versions 1, 2, and 3 |
| [npm workspaces](https://docs.npmjs.com/cli/v9/using-npm/workspaces)                      | ✅ Supported   |                                               |
| [Package overrides](https://docs.npmjs.com/cli/v8/configuring-npm/package-json#overrides) | ✅ Supported   |                                               |
| `file:` dependencies                                                                      | ✅ Supported   |                                               |
| shrinkwrap dependencies                                                                   | ✅ Supported   |                                               |
| bundled dependencies                                                                      | ✅ Supported   |                                               |

## Yarn

Socket fully supports Yarn (versions versions 1, 2, and 3).

| Feature                                                                                                                         | Support Level      | Notes |
| :------------------------------------------------------------------------------------------------------------------------------ | :----------------- | :---- |
| [Yarn lockfile](https://classic.yarnpkg.com/lang/en/docs/yarn-lock/) (`yarn.lock`)                                              | ✅ Supported        |       |
| [Yarn workspaces](https://yarnpkg.com/features/workspaces)                                                                      | ✅ Supported        |       |
| [Selective dependency resolutions](https://classic.yarnpkg.com/lang/en/docs/selective-version-resolutions/) (Package overrides) | ✅ Supported        |       |
| `file:` dependencies                                                                                                            | ✅ Supported        |       |
| shrinkwrap dependencies                                                                                                         | ✅ Supported        |       |
| bundled dependencies                                                                                                            | ✅ Supported        |       |
| [Yarn protocols](https://yarnpkg.com/features/protocols)                                                                        | 🚧 Partial support |       |
| [Yarn plugins](https://yarnpkg.com/features/plugins) and [Plug'n'Play](https://yarnpkg.com/features/pnp)                        | ⏳ Planned          |       |

## pnpm

Socket fully supports pnpm (versions 5, 6, and 7).

| Feature                                                                                         | Support Level      | Notes |
| :---------------------------------------------------------------------------------------------- | :----------------- | :---- |
| [pnpm lockfile](https://pnpm.io/cli/install) (`pnpm-lock.yaml`)                                 | ✅ Supported        |       |
| [pnpm workspaces](https://pnpm.io/workspaces)                                                   | ✅ Supported        |       |
| [Package overrides/resolutions](https://pnpm.io/package_json#pnpmoverrides) (Package overrides) | ✅ Supported        |       |
| `file:` dependencies                                                                            | ✅ Supported        |       |
| shrinkwrap dependencies                                                                         | ✅ Supported        |       |
| bundled dependencies                                                                            | ✅ Supported        |       |
| pnpm protocols                                                                                  | 🚧 Partial support |       |
| [pnpm patch](https://pnpm.io/cli/patch)                                                         | ⏳ Planned          |       |

# Python

Socket supports Python (uv, pip, Poetry, and Anaconda).

| Package Manager    | Support Level                   | Notes                            |
| :----------------- | :------------------------------ | :------------------------------- |
| [uv](#uv)          | ✅ Supported                     | uv versions 0.x (latest)         |
| [pip](#pip)        | ✅ Supported                     | pip versions 20 - 25 (latest)    |
| [Poetry](#poetry)  | ✅ Supported                     | Poetry versions 1 - 2            |
| [PDM](#pdm)        | ✅ Supported                     | TODO                             |
| Anaconda (`conda`) | 🚧 [Partial support](#anaconda) | Anaconda versions 22-25 (latest) |

## uv

`uv` is the [preferred Python package manager](https://socket.dev/blog/socket-now-supports-uv-lock-files) for Socket. This is because `uv` generates truly deterministic lockfiles through universal resolution. This approach ensures that dependencies are locked consistently across all platforms and environments.

| Feature                                                                                                                                                                                                  | Support Level | Notes |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------ | :---- |
| [`uv.lock`](https://docs.astral.sh/uv/concepts/projects/sync/)                                                                                                                                           | ✅ Supported   |       |
| `pyproject.toml` ( [PEP517](https://peps.python.org/pep-0517/)  [PEP518](https://peps.python.org/pep-0518/)  [PEP621](https://peps.python.org/pep-0621/)  [PEP660](https://peps.python.org/pep-0660/)  ) | ✅ Supported   |       |
| `pylock.toml`                                                                                                                                                                                            | ✅ Supported   |       |
| [Optional dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/#optional-dependencies)                                                                                                 | ✅ Supported   |       |
| [Python environments](https://docs.astral.sh/uv/pip/environments/)                                                                                                                                       | ✅ Supported   |       |

## pip

`pip` dependency resolution is non-deterministic. This is a fundamental limitation of the `pip` package manager. For best accuracy, [Socket recommends](https://socket.dev/blog/socket-now-supports-uv-lock-files) using [`uv`](#uv)  if possible.

| Feature                                                                                                                                                                                                  | Support Level | Notes |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------ | :---- |
| [`Pipfile` and `Pipfile.lock`](https://github.com/pypa/pipfile#pipfile-the-replacement-for-requirementstxt)                                                                                              | ✅ Supported   |       |
| [`setup.py`](https://setuptools.pypa.io/en/latest/userguide/quickstart.html)                                                                                                                             | ✅ Supported   |       |
| [requirements files](https://pip.pypa.io/en/stable/reference/requirements-file-format/)  ( `requirements.txt` )                                                                                          | ✅ Supported   |       |
| `pyproject.toml` ( [PEP517](https://peps.python.org/pep-0517/)  [PEP518](https://peps.python.org/pep-0518/)  [PEP621](https://peps.python.org/pep-0621/)  [PEP660](https://peps.python.org/pep-0660/)  ) | ✅ Supported   |       |
| `pylock.toml`                                                                                                                                                                                            | ✅ Supported   |       |
| pip extras                                                                                                                                                                                               | ✅ Supported   |       |

## Poetry

For best accuracy, [Socket recommends](https://socket.dev/blog/socket-now-supports-uv-lock-files) using [`uv`](#uv)  if possible.

| Feature                                                                                                                                                                                                  | Support Level | Notes                                                                                                                                                                                                                                                                            |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`pyproject.toml#tool.poetry`](https://python-poetry.org/docs/pyproject/)                                                                                                                                | ✅ Supported   |                                                                                                                                                                                                                                                                                  |
| [`poetry.lock`](https://python-poetry.org/docs/basic-usage/#installing-with-poetrylock)                                                                                                                  | ✅ Supported   | Optional dependencies and extras are not supported for `poetry.lock`. This is because the lockfile does not lock your optional dependencies. For best accuracy, [Socket recommends](https://socket.dev/blog/socket-now-supports-uv-lock-files)  using [`uv`](#uv)   if possible. |
| `pylock.toml`                                                                                                                                                                                            | ✅ Supported   |                                                                                                                                                                                                                                                                                  |
| `pyproject.toml` ( [PEP517](https://peps.python.org/pep-0517/)  [PEP518](https://peps.python.org/pep-0518/)  [PEP621](https://peps.python.org/pep-0621/)  [PEP660](https://peps.python.org/pep-0660/)  ) | ✅ Supported   |                                                                                                                                                                                                                                                                                  |

## PDM

TODO

## Anaconda

| Feature                                                                                                          | Support Level | Notes                                                                                                                                                                                                                            |
| :--------------------------------------------------------------------------------------------------------------- | :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [requirements files](https://pip.pypa.io/en/stable/reference/requirements-file-format/)   ( `requirements.txt` ) | ✅ Supported   | Anaconda scanning is supported via `requirements.txt`. See detailed [Anaconda setup instructions](https://docs.socket.dev/docs/anaconda-setup-instructions). Your Technical Account Manager can help you with this process.                               |
| Anaconda Cloud                                                                                                   | ⏳ Planned     | Socket scans artifacts published to PyPI, with Anaconda Cloud support planned on Socket’s roadmap. Socket supports the PyPI registry and therefore we can report risks for any Anaconda package which is also published to PyPI. |

# Go

Socket supports Go. [Contact us](https://docs.socket.dev/docs/contact-support) to get access.

| Package Management                 | Support Level | Notes |
| :--------------------------------- | :------------ | :---- |
| Go Modules (`go.mod` and `go.sum`) | ✅ Supported   |       |

# Java

Socket supports Java.

<HTMLBlock>
  {`
  <table style="width: 100%; border-collapse: collapse;">
  <thead>
  <tr>
    <th style="border: 1px solid #ddd; padding: 8px;">Package Management</th>
    <th style="border: 1px solid #ddd; padding: 8px;">Support Level</th>
    <th style="border: 1px solid #ddd; padding: 8px;">Notes</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="https://maven.apache.org/guides/introduction/introduction-to-the-pom.html"><code>pom.xml</code></a></p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>✅ Supported</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>Support for <code>&lt;exclusions&gt;</code>, <code>&lt;scope&gt;</code>s, <code>&lt;dependencyManagement&gt;</code>, property inheritance, and parent pom resolution.</p>
  </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>Maven support</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>✅ Supported</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>Maven Central</p>
  </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>Gradle support</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>✅ Supported</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>Gradle is fully supported. For the simplest setup, commit a <code>gradle.lockfile</code> (recommended).<br>See the detailed <a href="doc:gradle-setup-instructions-for-java-kotlin-and-scala">Gradle setup instructions (for Java, Kotlin, and Scala)</a> . Your Technical Account Manager can help you with this process.</p>
  </td>
  </tr>
  </tbody>
  </table>
  `}
</HTMLBlock>

# Ruby

Socket supports Ruby.

| Package Management      | Support Level      | Notes                                                                                                                                                                                                                   |
| :---------------------- | :----------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Gemfile.lock`          | ✅ Supported        | Lockfiles are fully supported - for the best accuracy ensure `Gemfile.lock` is committed to source control.                                                                                                             |
| `Gemfile` / `*.gemspec` | ⚠️ Partial Support | Use the open source [CycloneDX Ruby gem plugin](https://github.com/CycloneDX/cyclonedx-ruby-gem)  to generate and commit an SBOM which Socket will scan. Your Technical Account Manager can help you with this process. |

# .NET (C#, F#, Visual Basic)

Socket supports .NET (C#, F#, Visual Basic).

<HTMLBlock>
  {`
  <table style="width: 100%; border-collapse: collapse;">
  <thead>
  <tr>
    <th style="border: 1px solid #ddd; padding: 8px;">Package Management</th>
    <th style="border: 1px solid #ddd; padding: 8px;">Support Level</th>
    <th style="border: 1px solid #ddd; padding: 8px;">Notes</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>NuGet (<code>*.*proj</code>, <code>packages.lock.json</code>, <code>*.nuspec</code>, and <code>packages.config</code>)</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>✅ Supported</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>Lockfiles are fully supported and provide the best accuracy - ensure all <code>packages.lock.json</code> files are committed to source control.  </p>
  <p>Other MSBuild / Nuget manifests are fully supported but SBOM accuracy depends on the complexity of the projects&#39; configuration.</p>
  </td>
  </tr>
  </tbody>
  </table>
  `}
</HTMLBlock>

# Scala

Socket supports Scala. See detailed [Scala setup instructions](https://docs.socket.dev/docs/scala-setup-instructions).

<HTMLBlock>
  {`
  <table style="width: 100%; border-collapse: collapse;">
  <thead>
  <tr>
    <th style="border: 1px solid #ddd; padding: 8px;">Package Management</th>
    <th style="border: 1px solid #ddd; padding: 8px;">Support Level</th>
    <th style="border: 1px solid #ddd; padding: 8px;">Notes</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="https://www.scala-sbt.org/1.x/docs/Basic-Def.html">build.sbt</a></p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>✅ Supported</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>See detailed <a href="doc:scala-setup-instructions">Scala setup instructions</a>  .Your Technical Account Manager can help you with this process.</p>
  </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>Gradle support</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>✅ Supported</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>Gradle is fully supported. For the simplest setup, commit a <code>gradle.lockfile</code> (recommended).<br>See the detailed <a href="https://docs.socket.dev/docs/gradle-setup-instructions-for-java-kotlin-and-scala">Gradle setup instructions (for Java, Kotlin, and Scala)</a> . Your Technical Account Manager can help you with this process.</p>
  </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>Maven support</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>✅ Supported</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>Maven Central</p>
  </td>
  </tr>
  </tbody>
  </table>
  `}
</HTMLBlock>

# Kotlin

Socket supports Kotlin. See detailed [Kotlin setup instructions](https://docs.socket.dev/docs/kotlin-setup-instructions).

<HTMLBlock>
  {`
  <table style="width: 100%; border-collapse: collapse;">
  <thead>
  <tr>
    <th style="border: 1px solid #ddd; padding: 8px;">Package Management</th>
    <th style="border: 1px solid #ddd; padding: 8px;">Support Level</th>
    <th style="border: 1px solid #ddd; padding: 8px;">Notes</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>Gradle support (<a href="https://docs.gradle.org/current/userguide/kotlin_dsl.html"><code>build.gradle.kts</code></a>)</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>✅ Supported</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>Gradle is fully supported. For the simplest setup, commit a <code>gradle.lockfile</code> (recommended).<br>See the detailed <a href="https://docs.socket.dev/docs/gradle-setup-instructions-for-java-kotlin-and-scala">Gradle setup instructions (for Java, Kotlin, and Scala)</a> . Your Technical Account Manager can help you with this process.</p>
  </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>Maven support</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>✅ Supported</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>Maven Central</p>
  </td>
  </tr>
  </tbody>
  </table>
  `}
</HTMLBlock>

# Rust

Socket supports Rust.

| Package Management | Support Level | Notes           |
| :----------------- | :------------ | :-------------- |
| `cargo.lock`       | ✅ Supported   | Fully supported |

# GitHub Actions

Socket supports GitHub Actions.

| Package Management                                      | Support Level | Notes           |
| :------------------------------------------------------ | :------------ | :-------------- |
| GitHub Actions workflows (`.github/workflows/*.y{a}ml`) | ✅ Supported   | Fully supported |

# C/C++

NOTE: C/C++ support is CVE-only.

| Package Management   | Support Level        | Notes                 |
| :------------------- | :------------------- | :-------------------- |
| Details coming soon. | Details coming soon. | Details coming soon.. |

> 📘 Something missing?
>
> Please add a [feature request](https://feedback.socket.dev/) and we will do our best to make your wish come true!
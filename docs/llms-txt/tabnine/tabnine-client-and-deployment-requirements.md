# Source: https://docs.tabnine.com/main/welcome/readme/system-requirements/tabnine-client-and-deployment-requirements.md

# Tabnine Client & Deployment Requirements

## Tabnine Client Requirements <a href="#tabnine-client-ide-plugin" id="tabnine-client-ide-plugin"></a>

The Tabnine client runs as an IDE plugin/extension on the end user's machine.

**Machine specs**

* OS/Arch of the following:
  * Windows (Windows 10+), x86\_64 or i686
  * Linux (kernel 6.2+), x86\_64
  * Mac OS (13+), x86\_64 or aarch64
* 16 GB+ RAM
* 8+ CPU cores
* Storage: 100 GB available space

**Supported IDEs**

<table><thead><tr><th width="46"></th><th>IDE</th><th>Minimal supported version</th><th>Latest supported version</th><th data-type="checkbox">Windows OS</th><th data-type="checkbox">Mac OS</th><th data-type="checkbox">Linux OS</th></tr></thead><tbody><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d6a3275f1b33c468b61ce3faf912a0fc5a134a7b%2Fvsc%20(1).webp?alt=media" alt="" data-size="line"></td><td>VS Code</td><td>1.86</td><td>1.111</td><td>true</td><td>true</td><td>true</td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-74716d5d81d7c0b8ecb601c7d0ac00a6bda75c6b%2FJetBrains.png?alt=media" alt="" data-size="line"></td><td>JetBrains IDEs*</td><td>2023.3</td><td>2025.3</td><td>true</td><td>true</td><td>true</td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-dd5c75287f8ff150beba6ccb574e490613d88d2c%2Feclipse%20logo.webp?alt=media" alt="" data-size="line"></td><td>Eclipse</td><td>4.28 (2023-06)</td><td>4.38 (2025-12)</td><td>true</td><td>true</td><td>true</td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-0920f6c4e65f036c6c903f4f4357aa6baf40aee1%2Fvs%20(1).webp?alt=media" alt="" data-size="line"></td><td>Visual Studio 2022</td><td>17.10</td><td>17.14</td><td>true</td><td>false</td><td>false</td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FnAs1fEuLCy9uwHFbqPXC%2FVs2026_logo.png?alt=media&#x26;token=a45e1da6-d62a-4139-a3e4-d9b985c3d090" alt=""></td><td>Visual Studio 2026</td><td>18.1</td><td>18.3</td><td>true</td><td>false</td><td>false</td></tr></tbody></table>

*\* JetBrains IDEs including IntelliJ, PyCharm, WebStorm, PhpStorm, GoLand, RubyMine, CLion, AppCode, Rider, DataGrip, and Android Studio*

**Network connection**

* Connection to the Tabnine cluster on port 443
* Recommended for the initial install: Access to the IDE marketplaces (i.e., VS Code\
  Marketplace, JetBrains Plugin Marketplace)

**Permissions**

* Execute permissions for the following executables:
  * `TabNine`
  * `TabNine-deep-local`
  * `TabNine-deep-cloud`
  * `WD-TabNine`
  * `TabNine-server-runner`
  * `vdb`
  * `jdtls`
  * `typescript-language-server`
* Write and execute permissions for the following machine paths:
  * Linux: `~/.config & ~/.tabnine`
  * Mac OS: `/Users/{{username}}/Library/Preferences & /Users/{{username}}/Library/Application Support`
  * Windows: <mark style="color:yellow;background-color:blue;">`C:\Users\{{username}}\AppData\Roaming\`</mark>

***

## Tabnine Deployment Options

Tabnine can be deployed in one of the following ways:

1. Single/Multi-Tenant SaaS
2. Private cloud / On-prem installation using private API endpoints
3. Private cloud / On-prem installation using open-weight models

### Single/Multi-Tenant SaaS

This deployment allows you to utilize Tabnine’s private LLM endpoints to support both Chat and Agentic workflows.

#### **Models**

These utilize the following families of LLMs for both Chat and Agent:

* GPT
* Claude
* Gemini

#### **Hardware Requirements**

*None.*

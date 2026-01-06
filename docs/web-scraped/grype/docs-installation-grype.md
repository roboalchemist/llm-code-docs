# Source: https://oss.anchore.com/docs/installation/grype/

- Installing Grype | Anchore Open Source**Enterprise Docs
- **Events
- **Blog
- **GitHub
- **Discourse
- 

Light

- 

Dark

- 

Auto

Search
Ctrl K- Open SourceProjects
- InstallationSyft*
- Grype
- Grant
- Verifying Downloads
- GuidesSBOM GenerationGetting Started
- Scan Targets
- Output Formats
- Working with JSON
- Package Catalogers
- File Selection
- Using Templates
- Format Conversion
- Attestation
- Vulnerability ScanningGetting Started
- Scan Targets
- Package ecosystems
- Understanding Results
- Working with JSON
- Filter scan results
- Vulnerability Database
- License ScanningGetting Started
- Policies
- Private Registries
- CapabilitiesSupported OSs
- Supported packages
- ALPMarch
- APKalpine+
- DPKGdebian+
- Portagegentoo
- RPMredhat+
- Conda
- C/C++
- Dart
- .NET
- Elixir
- Erlang
- Go
- Haskell
- Java
- JavaScript
- Lua
- Nix
- OCaml
- PHP
- Prolog
- Python
- R
- Ruby
- Rust
- Swift
- AI
- Binary
- Bitnami
- GitHub Actions
- Homebrew
- Linux Kernel
- SBOM
- Snap
- Terraform
- Wordpress
- ContributingIssues and Discussions
- Pull Requests
- Sign-off Commits
- Security Policy
- Code of Conduct
- Syft
- Grype
- Grype DB
- Vunnel
- Grant
- SBOM Action
- Scan Action
- Docs (this site!)
- ReferenceConfiguration Rules
- Command Line
- Configuration
- JSON Schemav16latest
- Command Line
- Configuration
- Data sources
- Command Line
- Configuration
- ArchitectureGo CLI patterms
- Syft
- Grype
- Grype DB
- Vunnel
- AboutEvents
- Adopters
- Discussion
- Glossary
- Official buildsInstaller script
- Updating Grype
- Docker container
- GitHub releases
- Community builds of GrypeArch Linux
- Homebrew
- MacPorts
- Winget
- Scoop
- Snapcraft
Categories- architecture5
- community3
- developer7
- reference6
Tags- attestation1
- authentication1
- catalogers1
- cli1
- container1
- cyclonedx2
- data-sources1
- docker1
- ecosystems1
- filtering1
- formats2
- grant11
- grype18
- grype-db4
- jq1
- json4
- licenses3
- output2
- sbom11
- sbom-action1
- scan-action1
- sources1
- spdx2
- stereoscope1
- syft21
- templates1
- vex1
- vulnerabilities7
- vunnel5
Installation
grype- Open Source
- Installation
- Grype

*- ** Edit this page
- [** Create documentation issue](https://github.com/anchore/oss-docs/issues/new?title=Installing%20Grype)
- ** View page source
- [** Create child page](https://github.com/anchore/oss-docs/new/main/content/docs/installation?filename=change-me.md&amp;value=---%0Atitle%3A+%22Long+Page+Title%22%0AlinkTitle%3A+%22Short+Nav+Title%22%0Aweight%3A+100%0Adescription%3A+%3E-%0A+++++Page+description+for+heading+and+indexes.%0A---%0A%0A%23%23+Heading%0A%0AEdit+this+template+to+create+your+new+page.%0A%0A%2A+Give+it+a+good+name%2C+ending+in+%60.md%60+-+e.g.+%60getting-started.md%60%0A%2A+Edit+the+%22front+matter%22+section+at+the+top+of+the+page+%28weight+controls+how+its+ordered+amongst+other+pages+in+the+same+directory%3B+lowest+number+first%29.%0A%2A+Add+a+good+commit+message+at+the+bottom+of+the+page+%28%3C80+characters%3B+use+the+extended+description+field+for+more+detail%29.%0A%2A+Create+a+new+branch+so+you+can+preview+your+new+file+and+request+a+review+via+Pull+Request.%0A)
- ** Create project issue
- ** Print entire section
# Installing Grype
Tags:- grype
## Official builds
- 
The Anchore OSS team publish official source archives and binary builds of Grype for Linux, macOS and Windows. There are also numerous community-maintained builds of the tools for different platforms.### Installer script

Grype binaries are provided for Linux, macOS and Windows.```
`curl -sSfL https://get.anchore.io/grype | sudo sh -s -- -b /usr/local/bin
`
```
Install script options:`-b`: Specify a custom installation directory (defaults to ./bin)
- `-d`: More verbose logging levels (-d for debug, -dd for trace)
- `-v`: Verify the signature of the downloaded artifact before installation (requires cosign to be installed)
### Updating Grype
- 
Grype checks for new versions on launch. It will print a message at the end of the output if the version in use is not the latest.```
`A newer version of grype is available for download: 0.92.0 (installed version is 0.91.2)
`
```
### Docker container

```
`docker pull anchore/grype
`
```
### GitHub releases

Download the file for your operating system and architecture from the GitHub releases page
- In the case of `.deb` or `.rpm`, install them using your package manager
- For compressed archives, unpack the file, and copy the `grype` binary to a folder in your path such as `/usr/local/bin`
## Community builds of Grype
- 
### Arch Linux

```
`sudo pacman -S grype-bin
`
```
### Homebrew

```
`brew tap anchore/grype
brew install grype
`
```
### MacPorts

```
`sudo port install grype
`
```
### Winget

```
`winget install Anchore.Grype
`
```
### Scoop

```
`scoop bucket add main
scoop install main/grype
`
```
### Snapcraft

```
`snap install grype
`
```
Last modified January 2, 2026: only allow one workflow run of the docs generation (#110) (c1b6cc1)**
- **
- **
- **
- **
- **
- **
- **
&copy;
2026
Anchore IncAll Rights ReservedPrivacy Policy

&#215;
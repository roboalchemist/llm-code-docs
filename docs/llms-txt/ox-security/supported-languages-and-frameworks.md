# Source: https://docs.ox.security/supported-languages-and-frameworks.md

# Supported Languages and Frameworks

The following is the overview of supported languages across different OX Security categories:

* [Code security](#code-security-support)
* [Open Source Security & SBOM](#sca-and-sbom-support)
* [API BOM](#api-bom-support)
* [Infrastructure](#infrastructure-as-code-support)

## Code Security Support

OX supports static code analysis for the following programming languages.

| Language                    | Code Scanning | AI Fix Support |
| --------------------------- | ------------- | -------------- |
| **Python**                  | Yes           | Yes            |
| **JavaScript / TypeScript** | Yes           | Yes            |
| **Java**                    | Yes           | Yes            |
| **C#**                      | Yes           | Yes            |
| **PHP**                     | Yes           | No             |
| **Swift**                   | Yes           | No             |
| **Go**                      | Yes           | No             |
| **Rust**                    | Yes           | No             |
| **Dart**                    | Yes           | No             |
| **Ruby**                    | Yes           | No             |
| **C / C++**                 | Yes           | No             |
| **Scala**                   | Yes           | No             |
| **Kotlin**                  | Yes           | No             |
| **COBOL**                   | Yes           | No             |
| **Visual Basic .NET**       | Yes           | No             |

## SCA & SBOM Support

OX supports Software Composition Analysis (SCA) and Software Bill of Materials (SBOM) generation for the following package manager files.

| Language                | <p>Package<br>Manager</p> | <p>License<br>Scanning</p> | <p>Vulnerability<br>Scan</p> | <p>Dependency<br>Graph</p> | <p>Reachability<br>Analysis</p> | <p>Pull Request<br>Fix</p> | <p>Private Dependency<br>Scanning</p> | <p>Dependency<br>Confusion</p> | <p>Deprecated<br>Dependencies</p> | <p>Malicious<br>Dependencies</p> |
| ----------------------- | ------------------------- | -------------------------- | ---------------------------- | -------------------------- | ------------------------------- | -------------------------- | ------------------------------------- | ------------------------------ | --------------------------------- | -------------------------------- |
| **JavaScript**          | `npm`                     | Yes                        | Yes                          | Yes                        | Yes                             | Yes                        | Yes                                   | Yes                            | Yes                               | Yes                              |
|                         | `yarn`                    | Yes                        | Yes                          | Yes                        | Yes                             | Yes                        | Yes                                   | Yes                            | Yes                               | Yes                              |
|                         | `pnpm`                    | Yes                        | Yes                          | Yes                        | Yes                             | Yes                        | Yes                                   | No                             | Yes                               | Yes                              |
| **Python**              | `pip`                     | Yes                        | Yes                          | Yes                        | Yes                             | Yes                        | No                                    | Yes                            | No                                | Yes                              |
|                         | `Poetry`                  | Yes                        | Yes                          | Yes                        | Yes                             | Yes                        | No                                    | No                             | No                                | Yes                              |
|                         | `Pipenv`                  | Yes                        | Yes                          | Yes                        | Yes                             | Yes                        | No                                    | No                             | No                                | Yes                              |
|                         | `uv`                      | Yes                        | Yes                          | Yes                        | Yes                             | Yes                        | No                                    | No                             | No                                | Yes                              |
| **Java**                | `Maven`                   | Yes                        | Yes                          | Yes                        | Yes                             | Yes                        | Yes                                   | No                             | No                                | Yes                              |
|                         | `Gradle`                  | Yes                        | Yes                          | Yes                        | Yes                             | Yes                        | Yes                                   | No                             | No                                | Yes                              |
| **Scala**               | `SBT`                     | Yes                        | Yes                          | Yes                        | No                              | No                         | No                                    | No                             | No                                | Yes                              |
|                         | `Maven`                   | Yes                        | Yes                          | Yes                        | No                              | Yes                        | Yes                                   | No                             | No                                | Yes                              |
|                         | `Gradle`                  | Yes                        | Yes                          | Yes                        | No                              | Yes                        | Yes                                   | No                             | No                                | Yes                              |
| **Kotlin**              | `Maven`                   | Yes                        | Yes                          | Yes                        | Yes                             | Yes                        | Yes                                   | No                             | No                                | Yes                              |
|                         | `Gradle`                  | Yes                        | Yes                          | Yes                        | Yes                             | Yes                        | Yes                                   | No                             | No                                | Yes                              |
| **Objective-C / Swift** | `CocoaPods`               | Yes                        | Yes                          | Yes                        | No                              | No                         | No                                    | No                             | No                                | No                               |
|                         | `SwiftPM`                 | Yes                        | Yes                          | Yes                        | Yes                             | Yes                        | No                                    | No                             | No                                | No                               |
|                         | `XcodeGen`                | Yes                        | Yes                          | Yes                        | Yes                             | Yes                        | No                                    | No                             | No                                | No                               |
| **Go**                  | `Go Modules`              | Yes                        | Yes                          | Yes                        | Yes                             | Yes                        | No                                    | No                             | No                                | Yes                              |
| **Dart**                | `Dart`                    | Yes                        | Yes                          | Yes                        | Yes                             |                            |                                       |                                |                                   |                                  |
| **Rust**                | `Rust`                    | Yes                        | Yes                          | Yes                        | Yes                             |                            |                                       |                                |                                   |                                  |
| **Ruby**                | `RubyGems`                | Yes                        | Yes                          | Yes                        | No                              | No                         | No                                    | No                             | No                                | Yes                              |
| **C#**                  | `NuGet`                   | Yes                        | Yes                          | Yes                        | Yes                             | Yes                        | Yes                                   | No                             | No                                | Yes                              |
| **Visual Basic .NET**   | `NuGet`                   | Yes                        | Yes                          | Yes                        | Yes                             |                            |                                       |                                |                                   |                                  |
| **PHP**                 | `Cpmposer`                | No                         | Yes                          | Yes                        | No                              | Yes                        | No                                    | No                             | No                                | Yes                              |

## API BOM Support

OX supports API analysis and detection for specific specifications and frameworks.

<table><thead><tr><th>Language</th><th width="128">Web framework</th><th>API detection</th><th>API/Issue correlation¹</th></tr></thead><tbody><tr><td><strong>OpenAPI specification file</strong></td><td>—</td><td>Yes</td><td>N/A</td></tr><tr><td><strong>Python</strong></td><td>Flask</td><td>Yes</td><td>Yes</td></tr><tr><td></td><td>FastAPI</td><td>Yes</td><td>Yes</td></tr><tr><td></td><td>Django</td><td>Yes</td><td>Yes</td></tr><tr><td></td><td>Connexion</td><td>Yes</td><td>Yes</td></tr><tr><td></td><td>Graphene</td><td>Yes</td><td>Yes</td></tr><tr><td><strong>JavaScript &#x26; TypeScript</strong></td><td>Express.js</td><td>Yes</td><td>Yes</td></tr><tr><td></td><td>NestJS</td><td>Yes</td><td>Yes</td></tr><tr><td></td><td>Koa</td><td>Yes</td><td>Yes</td></tr><tr><td></td><td>Apollo GraphQL</td><td>Yes</td><td>Yes</td></tr><tr><td><strong>Java</strong></td><td>SpringBoot</td><td>Yes</td><td>Yes</td></tr><tr><td><strong>Go</strong></td><td>Gin</td><td>Yes</td><td>N/A</td></tr><tr><td><strong>Scala</strong></td><td>Play</td><td>Yes</td><td>Yes</td></tr><tr><td></td><td>SpringBoot</td><td>Yes</td><td>Yes</td></tr><tr><td><strong>Kotlin</strong></td><td>SpringBoot</td><td>Yes</td><td>Yes</td></tr><tr><td></td><td>Ktor</td><td>Yes</td><td>Yes</td></tr><tr><td><strong>C#</strong></td><td>Microsoft ASP.NET Core MVC</td><td>Yes</td><td>Yes</td></tr></tbody></table>

## Infrastructure as Code Support

OX detects and supports IaC tools and deployment configurations for the following platforms.

| Tool           | Supported Deployments                       |
| -------------- | ------------------------------------------- |
| Terraform      | Alibaba, AWS, GCP, Azure, Yandex, OpenStack |
| Argo Workflows | Kubernetes                                  |
| CloudFormation | AWS                                         |
| Dockerfile     | Any                                         |
| Kubernetes     | Any                                         |

# Source: https://docs.socket.dev/docs/package-search.md

# Package Search

## Introduction

The Socket Package Search feature allows users to explore and analyze different software packages across multiple ecosystems, including npm, Go, Maven, and PyPI. This functionality provides in-depth insights into package details, dependencies, maintainers, versions, alerts, and more.

<Image align="center" src="https://files.readme.io/63ba893-Screenshot_2024-06-27_at_1.40.19_PM.png" />

### Key Features

1. **Comprehensive Package Analysis**:
   * View detailed information about any package, including its dependencies, maintainers, versions, and associated alerts.
   * Example: For npm packages, you can view dependencies, maintainers, versions, and alerts for in-depth analysis of the package.

2. **Security and Quality Metrics**:
   * Access metrics like supply chain security, quality, maintenance, vulnerabilities, and license compliance.
   * Example: Each package version is evaluated and scored on parameters such as supply chain security, quality, maintenance, vulnerabilities, and license compliance.

3. **Alerts and Risks**:
   * Identify and understand potential risks such as known malware, install scripts, shell access, and possible typosquat attacks.
   * Example: Alerts include possible typosquat attacks, known malware, and install scripts that may compromise your system.

### Inline Alerts and File Explorer

<Image align="center" src="https://files.readme.io/070942d-Screenshot_2024-06-26_at_3.32.27_PM.png" />

* **Inline Alerts**: Displays alerts directly in the search results for immediate attention.
* **File Explorer**: Provides a detailed view of the package files, highlighting any critical alerts or potential issues.

## How to Use the Package Search

1. **Navigating to the Package Search**:
   * Use the search bar at the top of the [Socket](https://socket.dev/) interface to search for packages across different ecosystems (npm, Go, Maven, PyPI).
   * Select the appropriate ecosystem to refine your search.

2. **Exploring Package Information**:
   * Once you have selected a package, you can navigate through different tabs to explore various aspects of the package.
     * **Package Overview**: General information about the package.
     * **Dependencies**: List of dependencies and their details.
     * **Maintainers**: Information about the maintainers of the package.
     * **Versions**: Different versions of the package along with their respective scores.
     * **Alerts**: Security alerts and issues associated with the package.
     * **File Explorer**: Explore the files contained in the package.
     * **License**: Detailed license information and compliance.

3. **Interpreting Package Metrics and Alerts**:
   * **Supply Chain Security**: Measures the security of the package's supply chain.
   * **Quality**: Assesses the overall quality of the package.
   * **Maintenance**: Evaluates the maintenance status of the package.
   * **Vulnerabilities**: Identifies known vulnerabilities within the package.
   * **License Compliance**: Ensures the package complies with relevant licenses.

## Example Screenshot

<Image align="center" src="https://files.readme.io/90f6358-Screenshot_2024-06-26_at_3.26.20_PM.png" />

### Inline Alerts

* **Critical Alerts**: Highlighted in red, these alerts indicate severe issues that need immediate attention.
* **Medium Risk Alerts**: Highlighted in yellow, these alerts indicate potential issues that should be reviewed.

### File Details

* Click on any file in the file explorer to view its contents.
* Inline alerts within the file contents provide additional context and details about the identified issues.

By utilizing the Socket Package Search feature, developers can ensure they are using secure and reliable packages, reducing the risk of vulnerabilities in their projects.

### Example: npm Package "webpack-dev-server"

1. Select `npm` from the ecosystem dropdown.
2. Enter the package name, e.g., `webpack-dev-esrver`.
3. Click on the package name to view the detailed file explorer.
4. <br />

   <Image align="center" src="https://files.readme.io/3dd32ba-Screenshot_2024-06-26_at_3.58.29_PM.png" />

#### Package Overview

* Displays the overall status and description of the package.
* Example: "webpack-dev-server" is a package used to create HTTP error objects. `webpback-dev-esrver` misnaming is a possible package typosquat attempt.  (*The example package has been unpublished*)
* <br />

  <Image align="center" src="https://files.readme.io/ee23675-Screenshot_2024-06-26_at_3.39.36_PM.png" />

#### Dependencies

* Lists all the dependencies associated with the package.
* Example: The package has 52 dependencies, including "ajv", "asn1", "assert-plus", etc.
* <br />

  <Image align="center" src="https://files.readme.io/866c2d1-Screenshot_2024-06-26_at_3.39.10_PM.png" />

#### Maintainers

* Information about the people maintaining the package.
* Example: The maintainer for "webpack-dev-server" is user "17b4a931".
* <br />

  <Image align="center" src="https://files.readme.io/7162880-Screenshot_2024-06-26_at_3.38.52_PM.png" />

#### Versions

* Lists the different versions of the package along with their scores.
* Example: Version "1.2.0" has a supply chain security score of 27, quality score of 100, maintenance score of 76, vulnerability score of 100, and license score of 100.
* <br />

  <Image align="center" src="https://files.readme.io/818be09-Screenshot_2024-06-26_at_3.38.40_PM.png" />

#### Alerts

* Highlights security alerts and issues such as known malware and possible typosquat attacks.
* Example: Alerts for "webpack-dev-server" include known malware, possible typosquat attacks, install scripts, and shell access risks.
* <br />

  <Image align="center" src="https://files.readme.io/1d97ca2-Screenshot_2024-06-26_at_3.38.30_PM.png" />

#### File Explorer

* Allows users to browse the files contained in the package.
* Example: Files such as "HISTORY.md", "index.js", "LICENSE", "package.json", and "README.md" are available for review.
* <br />

  <Image align="center" src="https://files.readme.io/7833387-Screenshot_2024-06-26_at_3.38.16_PM.png" />

#### License

* Provides detailed license information for the package.
* Example: The "webpack-dev-server" package is licensed under MIT, with details about locations and compliance levels.
* <br />

  <Image align="center" src="https://files.readme.io/b28b7dd-Screenshot_2024-06-26_at_3.38.03_PM.png" />

### Conclusion

The Socket Package Search feature is a powerful tool for developers and security professionals to analyze and ensure the integrity of software packages. By providing comprehensive insights into packages, dependencies, maintainers, and security alerts, it helps users make informed decisions and maintain high standards of security and quality in their projects.
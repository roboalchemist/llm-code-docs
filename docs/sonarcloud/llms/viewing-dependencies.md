# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/advanced-security/viewing-dependencies.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/advanced-security/viewing-dependencies.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/advanced-security/viewing-dependencies.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/advanced-security/viewing-dependencies.md

# Source: https://docs.sonarsource.com/sonarqube-server/advanced-security/viewing-dependencies.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-security/viewing-dependencies.md

# Viewing dependencies

Advanced Security is an add-on that requires a separate subscription to your SonarQube Cloud's [Enterprise plan](https://www.sonarsource.com/plans-and-pricing/#sonarqube-cloud-features).

During project analysis, SonarQube Advanced Security conducts software composition analysis (SCA) to identify and list project dependencies and associated risks. It's also possible to export the software bill of materials (SBOM) for your project.

### Viewing the list of dependencies <a href="#viewing-the-list-of-dependencies" id="viewing-the-list-of-dependencies"></a>

You must build, or rebuild your project's main branch to see the SCA results. After an analysis, a list of dependencies becomes available in the SonarQube Cloud UI under the **Dependencies** tab for projects and portfolios. It is updated with each analysis. You need the **Browse** permission to view dependencies on private projects and portfolios.

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-224f8458b6934acd73dd868805cb4c8058dfc2b1%2Fimage%20(2).png?alt=media" alt="List of dependencies in the SonarQube Cloud UI"><figcaption></figcaption></figure>

You can use **Filters** to narrow down the results. Dependencies can be filtered by:

* **Dependency type**: Direct or Transitive
* **Dependency scope**: Production or Development
* **Package manager**: A list of package managers. See [Analyzing projects for dependencies](https://docs.sonarsource.com/sonarqube-cloud/advanced-security/analyzing-projects-for-dependencies-sca) for supported package managers and languages.

Use the search feature to find specific dependencies.

The following information is displayed for each dependency card in the list:

<figure><img src="https://assets-eu-01.kc-usercontent.com/b1eeb429-d9e0-0100-be87-468f6802040a/ded013f1-73f7-490d-bd02-c352dc49636e/dependency-info.png?w=512&#x26;h=151&#x26;auto=format&#x26;fit=crop" alt="Information on a dependency in SonarQube Cloud." height="151" width="512"><figcaption></figcaption></figure>

1. Dependency name
2. Dependency version
3. Dependency type
4. Dependency scope
5. Files where the dependency was identified
6. Package manager
7. License

Click on the dependency name to open a detailed view.

### Detailed view <a href="#detailed-view" id="detailed-view"></a>

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-30cb76ce0a5a4cde02b800285401e8285131b705%2Fimage%20(3).png?alt=media" alt="The detailed view of a dependency in SonarQube Cloud"><figcaption></figcaption></figure>

The detailed view of a dependency provides the following information:

* Details of the dependency, including **Dependency type**, **Dependency scope**, **Identified using**, **Package manager** and **License**. Click on the info icon for **Identify using** to reveal all the files where the dependency was identified.
* Dependency chains: A list of direct and transitive dependency chains, if available.

#### About dependency chains <a href="#about-dependency-chains" id="about-dependency-chains"></a>

Dependency chains show how a dependency is brought into your project.

Project components often rely on other components, creating dependencies. These dependencies can be direct, where one component immediately uses another, or transitive, where a component relies on another component which, in turn, depends on yet another.

For example In a Project > Component 1 > Component 2 scenario:

* The dependency between Project and Component 1 is direct.
* The dependency between Project and Component 2 is transitive because Component 1 is built using Component 2.

The detailed view indicates whether a dependency has direct and transitive dependency chains and displays the complete path for transitive dependencies.

### Getting a high-level view of your dependency usage <a href="#global-view-dependency-usage" id="global-view-dependency-usage"></a>

You can also view dependencies for portfolios to get a higher-level view of your dependency usage. For example, to get a list, or bill of materials, for all software in use by your organization, you can create a [portfolio](https://docs.sonarsource.com/sonarqube-cloud/managing-portfolios) of **All Projects**.

After you create and refresh a portfolio, you can view **Dependencies** and **Dependency Risks**. Searching Dependencies by name allows you to see where a dependency is used in your organization. Searching Dependency Risks by a CVE name allows you to discover where your in organization you may be affected by a newly reported CVE.

### Software Bill of Materials (SBOM) <a href="#software-bill-of-materials" id="software-bill-of-materials"></a>

A software bill of materials (SBOM) is an inventory of components your project is built with, including details such as the component name, version, and license.

Because your project depends on these components to build and run your software, getting the SBOM for a project is a key element to track all the items that you depend on for both internal use in the remediation of dependency risks, and external use for compliance with regulations.

Compliance teams can use SBOMs as an index to keep an inventory of licenses in use. Developers can use SBOMs to manage dependencies. All of this creates greater interoperability and efficiency within an organization. It is a shared language for all of these teams that can be passively generated and maintained based on application builds.

Sonar supports exporting an SBOM in two major SBOM formats: Software Package Data Exchange (SPDX) and CycloneDX.

#### Exporting the SBOM <a href="#exporting-the-sbom" id="exporting-the-sbom"></a>

You can export the SBOM from the **Dependencies** page of **Projects** and **Portfolios**. SBOMs are available in the CycloneDX and SPDX, in both XML and JSON formats.

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-f32c9e593db365a7fbbb4dfd00f2dbdd856dd22a%2Fimage%20(4).png?alt=media" alt="The Export SBOM button on the SonarQube Cloud UI"><figcaption></figcaption></figure>

SBOMs are generated when requested in the UI or API; there is no storage or history for SBOMs in SonarQube. If your needs require storing SBOMs for particular released versions of your projects or portfolios, you should export a SBOM at release time and save it somewhere outside of SonarQube for later use.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [Reviewing and fixing dependency risks](https://docs.sonarsource.com/sonarqube-cloud/advanced-security/reviewing-and-fixing-dependency-risks)
* [Analyzing projects for dependencies](https://docs.sonarsource.com/sonarqube-cloud/advanced-security/analyzing-projects-for-dependencies-sca)
* [Managing license profiles and policies](https://docs.sonarsource.com/sonarqube-cloud/advanced-security/managing-license-profiles-and-policies)
* [Troubleshooting](https://docs.sonarsource.com/sonarqube-cloud/appendices/troubleshooting)
* [Best practices for managing dependency risks](https://docs.sonarsource.com/sonarqube-cloud/advanced-security/best-practices-for-managing-dependency-risks)

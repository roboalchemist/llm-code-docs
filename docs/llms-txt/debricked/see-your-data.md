# Source: https://docs.debricked.com/product/vulnerability-management/see-your-data.md

# See your data

In order to efficiently work with vulnerabilities in your repositories, you need an overview of all repositories you have along with the vulnerabilities affecting them. OpenText Core SCA provides you with an overview of all your projects and their security status.

### **See all your repositories** <a href="#howdoiseeallofmyrepositories" id="howdoiseeallofmyrepositories"></a>

To get an overview of all your repositories, click **Repositories** in the left side menu.

In this view, all your repositories are shown, by default sorted by the amount of vulnerabilities, along with the data:

* Name: The name of the repository prepended with the name of the owner.
* Total vulnerabilities: The total number of vulnerabilities found (including indirect dependencies).
* Vulnerability priority: The total number of vulnerabilities where the [CVSS score](https://docs.debricked.com/product/vulnerability-management/security-terms) is *critical* or *high.*
* Review status: The total number of vulnerabilities, where the [review status](https://docs.debricked.com/product/vulnerability-management/set-a-review-status) is set to *vulnerable*, *unexamined*, *paused/snoozed*, and *unaffected.*
* Total vulnerabilities with exploits: The total amount of vulnerabilities that have at least one known exploit.

> You can export the filtered and visible repository data in the table to a CSV file. To do so, click **Export Table** located at the top-right corner of the table. *For more information, refer to the* [*Export table data*](https://docs.debricked.com/product/administration/repositories/export-table-data) *topic.*

### **See vulnerabilities in a specific repository** <a href="#howdoiseevulnerabilitiesinaspecificrepository" id="howdoiseevulnerabilitiesinaspecificrepository"></a>

To show all vulnerabilities in a specific repository, click the repository name. This displays a view specific for that repository.

In this view, you get detailed information regarding the vulnerabilities discovered in your repository:

* Name: The vulnerability name, which is usually a CVE identifier. Any vulnerabilities identified through the LLM-based analysis will include an ‘LLM’ tag next to the vulnerability name.

*For more information on LLM-based vulnerability detection, refer 'LLM‑based vulnerability detection' section in the* [*Data sources*](https://docs.debricked.com/product/vulnerability-management/data-sources) *topic.*

* Discovered: The date at which the vulnerability was discovered in your code or repository.
* CVSS: The CVSS score for this vulnerability.
* Dependencies: The dependency in which the vulnerability was discovered.
* [Review status:](https://docs.debricked.com/product/vulnerability-management/set-a-review-status) Indicates whether the vulnerability is known to be vulnerable, unaffected, or unexamined.
* Reachable Path: Displays if the vulnerable functionality is reachable or not through your code. This field is conditionally displayed based on whether [Reachability Analysis](https://docs.debricked.com/product/vulnerability-management/reachability-analysis) was run or not.&#x20;
* Exploited (CISA): Determines whether the vulnerability is exploited or not, based on the CISA KEV catalog.

To see all commits related to this repository, or all related dependencies, click one of the tabs.

> You can export the filtered and visible vulnerability data in the table to a CSV file. To do so, click **Export Table** located at the top-right corner of the table. *For more information, refer to the* [*Export table data*](https://docs.debricked.com/product/administration/repositories/export-table-data) *topic.*

### **See information about a specific vulnerability** <a href="#howdoiseeinformationaboutaspecificvulnerability" id="howdoiseeinformationaboutaspecificvulnerability"></a>

To get detailed information about a specific vulnerability in a repository, click the vulnerability ID. This view contains links to advisories, such as NVD and GitHub along with a summary of the severity.

The summary contains the following information about the vulnerability:

* File(s) in which the vulnerability was found and the dependencies that introduced vulnerabilities.
* Indicates if the vulnerability is detected through LLM.

*For more information on LLM-based vulnerability detection, refer 'LLM‑based vulnerability detection' section in the* [*Data sources*](https://docs.debricked.com/product/vulnerability-management/data-sources) *topic.*

* Versions of vulnerable dependencies, and suggested safer alternative versions that can be used wherever possible.
* Breakdown of the CVSS scores

You will also get a list of external references that contain information about remediations, patches, real-world exploits, as well as documentation from issue trackers.

### **See all vulnerabilities across all projects** <a href="#howdoiseeallofthevulnerabilitiesacrossallprojects" id="howdoiseeallofthevulnerabilitiesacrossallprojects"></a>

To get an overview of all vulnerabilities found in all scanned repositories, click **Vulnerabilities** in the left side menu.

This view is similar to the view for a specific repository, but here all vulnerabilities found in all your repositories are included.

> You can export the filtered and visible vulnerability data in the table to a CSV file. To do so, click **Export Table** located at the top-right corner of the table. *For more information, refer to the* [*Export table data*](https://docs.debricked.com/product/administration/repositories/export-table-data) *topic.*

### **See all your dependencies** <a href="#howdoiseeallofmydependencies" id="howdoiseeallofmydependencies"></a>

To get an overview of all imported dependencies, including indirect dependencies, click **Dependencies** in the left side menu.

In this view, you are presented with a list of all dependencies found in all scanned repositories. It includes details such as:

* Name: The name of the dependency.
* Version status: The version used by the dependency. The valid values are 'Recent', 'Latest' and 'Outdated'.
  * Recent: The dependency is not using the latest available version; however, the version in use is still considered current. Updating to the latest version is optional.
  * Latest: The dependency is using the latest available version.
  * Outdated: The dependency is currently using an outdated version, which may pose a risk. Updating to the latest version is recommended.

> *You can configure the outdated version threshold from Admin Tools → Company Settings.*

* Total vulnerabilities: The total number of vulnerabilities found (including indirect dependencies).
* Vulnerability priority: The total number of vulnerabilities where the [CVSS score](https://docs.debricked.com/product/vulnerability-management/security-terms) is *critical* or *high.*
* Review status: The total number of vulnerabilities, where the [review status](https://docs.debricked.com/product/vulnerability-management/set-a-review-status) is set to *vulnerable*, *unexamined*, *paused/snoozed*, and *unaffected*.&#x20;
* Licenses: The license under which the dependency is released.
* Health Scores: The [Popularity score](https://docs.debricked.com/product/project-health/popularity) and the [Contributor score](https://docs.debricked.com/product/project-health/contributors) of this dependency.

> You can export the filtered and visible dependency data in the table to a CSV file. To do so, click **Export Table** located at the top-right corner of the table. *For more information, refer to the* [*Export table data*](https://docs.debricked.com/product/administration/repositories/export-table-data) *topic.*

#### Symbols <a href="#symbols" id="symbols"></a>

The column *Name* contains additional symbols providing you with more information:

* **?** - This is used for dependencies for which we were not able to parse the dependency tree (see [Language Suppor](https://docs.debricked.com/overview/language-support)[t](https://docs.debricked.com/overview/language-support)).
* ▼ - This is used for direct dependencies which include indirect dependencies (see section below).
* *dependency* symbol - This is used for indirect dependencies which are related to the main dependencies.
* no symbol - This is used for direct dependencies that do not include any indirect dependencies.

#### Direct or indirect dependencies <a href="#direct-indirectdependencies" id="direct-indirectdependencies"></a>

use the ▼ button next to the name of the direct dependency to see its indirect dependencies. The indirect dependencies are marked with an icon in the *Name* column to make it easier for you to differentiate them. To expand all direct dependencies in the current page, click the **Expand all/Collapse all** toggle button at the top.

### Search for dependencies <a href="#searchfordependencies" id="searchfordependencies"></a>

You can type the name of a package in the Search bar, to search for a specific dependency (direct or indirect), or the name of a license to see all the dependencies related to one license.

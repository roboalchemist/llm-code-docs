# Source: https://docs.debricked.com/product/exporting-sbom/overview.md

# Overview

Clicking **Overview** on the left side menu will take you to a dashboard allowing you to get a clear overview of all vulnerabilities found in your organization.

### **Filters** <a href="#filters" id="filters"></a>

#### Repository or Branch <a href="#filters" id="filters"></a>

The data presented in the Overview can be filtered depending on your needs. The repository picker enables you to select either a specific repository/branch or all your repositories altogether. When an individual repository is selected a specific branch selector shows up to further narrow down your data. The *All repositories* view shows data from the sum of the default branches present in all repositories.

Due to limitations, it is not always possible to identify the default branch except for GitLab users. For other users, the default branch can be identified if the branch name is either master or main. An effort is still made to identify your default branch correctly. This effort consists of looking for the branch with the most activity as it is assumed that, at least over time, this is the most interesting branch to look at.

#### Time period <a href="#timeperiod" id="timeperiod"></a>

The OpenText Core SCA API allows you to see data for any given interval. Keep in mind that for the period prior to the first snapshot, the data will be padded with 0 values. Since the snapshots older than a month are pruned, the intervals beginning over 30 days ago must have a two-week range.

### Vulnerability graph <a href="#vulnerabilitygraph" id="vulnerabilitygraph"></a>

The main dashboard presents your organization’s historical data in the form of a graph. This view visualizes the total amount of vulnerabilities in selected repositories, grouped by severity. You can adjust the graph according to your needs, by changing the values in the repository/branch and time period pickers.

### License risk widget <a href="#licenseriskwidget" id="licenseriskwidget"></a>

The bottom widget presents your current licence compliance risks, grouped by risk levels: critical, high, medium, low, and unknown. Keep in mind that this widget always shows you the current data, unaffected by the time period picker. You are still able to customize it by changing the selected repository/branch.

### Fixed vulnerabilities widget <a href="#fixedvulnerabilitieswidget" id="fixedvulnerabilitieswidget"></a>

The left-side widget presents information about your recently fixed vulnerabilities, including:

* The total amount of fixed vulnerabilities.
* The number of vulnerabilities fixed over the time period selected with the picker.
* A graph visualizing your fixed vulnerabilities over a time period.
* A sorted list of fixed vulnerabilities, the vulnerabilities fixed most recently shown at the top. You can also find their severity and the date they were fixed on.&#x20;
  * Click the name of the vulnerability to view the Vulnerability page.&#x20;
  * Click the folder icon to open the repository where the vulnerability was found.&#x20;
  * Click **View More** to view the complete list of fixed vulnerabilities in the currently selected scope.

You can also:

* Search the list of fixed vulnerabilities.&#x20;
* Customize this widget by selecting the repository or branch and time period, using the filters.&#x20;

### **Snapshots** <a href="#snapshots" id="snapshots"></a>

In order to accurately represent data in the overview, OpenText Core SCA periodically saves snapshots of the state of users' repositories. These snapshots contain the number of unknown-, low-, high-, and critical-severity vulnerabilities in a given repository. This evaluation is based on CVSS scores, with CVSS4 always taking precedence over CVSS3 and CVSS2. When a vulnerability does not have a CVSS score, it is assigned the unknown severity. The snapshots don’t record any other details about the vulnerabilities, only the quantity. They are created once per day and are updated upon each successful scan of a repository. Keep in mind that only snapshots coupled to the branch(es) being scanned will be updated.

### **Pruning** <a href="#pruning" id="pruning"></a>

In order to limit the amount of data that has to be stored, OpenText Core SCA periodically prunes the snapshots. All Sunday snapshots are saved indefinitely, but the snapshots taken on other days are only retained for one month. That results in the resolution of the dashboard graph being drastically reduced for data older than one month.

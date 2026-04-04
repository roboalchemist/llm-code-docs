# Source: https://docs.sonarsource.com/sonarqube-server/9.9/instance-administration/lines-of-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/instance-administration/lines-of-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/instance-administration/lines-of-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/instance-administration/lines-of-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/instance-administration/lines-of-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/instance-administration/monitoring/lines-of-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/instance-administration/monitoring/lines-of-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/instance-administration/monitoring/lines-of-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/server-upgrade-and-maintenance/monitoring/lines-of-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/server-upgrade-and-maintenance/monitoring/lines-of-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/server-update-and-maintenance/monitoring/lines-of-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-update-and-maintenance/monitoring/lines-of-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-update-and-maintenance/monitoring/lines-of-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/monitoring/lines-of-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-update-and-maintenance/monitoring/lines-of-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-update-and-maintenance/monitoring/lines-of-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/monitoring/lines-of-code.md

# Lines of Code

In SonarQube Server, the number of Lines of Code (LOC) you intend to analyze plays an important role in your choice of commercial edition (Developer, Enterprise, or Data Center). See the Sonar [Plans and Pricing](https://www.sonarsource.com/plans-and-pricing/) page for more details.

### LOC definition <a href="#calculating-lines-of-code" id="calculating-lines-of-code"></a>

Your instance’s LOC is calculated by adding up the LOC of each project analyzed. In the case of a Data Center Edition, the LOC from each project in each cluster node is summed up.

To calculate the LOC of a project, SonarQube Server counts the lines of code found on the most recent analysis of the largest branch or pull request of the project by excluding:

* Test code.
* Files excluded from analysis.
* Code in unsupported languages.
* Comments or blank lines.

**Example**: Your instance has two projects:

* Project1 has 500 lines of code on its main branch and 400 on a secondary long-lived branch: its LOC is 500.
* Project2 has 0 lines of code on its main branch (provisioned but never analyzed) and 200 on a secondary long-lived branch: its LOC is 200.
* The total LOC for the organization is 500 + 200 = 700.

Note that you can’t *use up your license* by reanalyzing the same code (with the same number of lines).

{% hint style="info" %}
Lines of code found in an A*pplication* do not count against your LOC. This is because Applications aggregate code from projects, and we already count the LOC once for the "parent" *project*.
{% endhint %}

### Checking your LOC consumption <a href="#checking-your-lines-of-code-consumption" id="checking-your-lines-of-code-consumption"></a>

Go to **Administration** > **Configuration** > **License Manager** to check how many lines of code you are currently using. Select **Edit notification threshold** to define when an email should be sent with information in regards to the impending lines of code limit. You cannot exceed your LOC threshold. If you’re near your limit, you may need to purchase additional lines of code.

<figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/IxhZz8b8mODBP28IVpYv/lines-of-code.png" alt="Lines of code displayed on the SonarQube license page"><figcaption></figcaption></figure>

You can check your LOC per project, per branch, in three different locations:

* Select **Project Information** to reveal the LOC on your main branch (for that project). Note that this may not exactly be your max LOC, for example, another branch or PR might have more lines of code.
* Navigate to the *Your Project* > **Measures** > **Size** page via the UI for a list of folders & files with a count of each folders’ and files’ LOC.
* Navigate to *Your Project* > **Code** page for a list of folders & files with a count of each folders’ and files’ LOC.

{% hint style="info" %}
The LOC is a metric (`ncloc`) you can retrieve through the [web-api](https://docs.sonarsource.com/sonarqube-server/extension-guide/web-api "mention") by using the `/api/measures` endpoint.
{% endhint %}

### If you exceed your LOC threshold <a href="#exceeding-your-loc-threshold" id="exceeding-your-loc-threshold"></a>

Once you are near your limit, you will receive a notification. On the **License Manager** page, select the **Edit notification threshold** button to define *when* notifications will be sent.

If you reach your limit, you will receive an error message and the SonarQube Server instance will reject any analysis whose total lines of code exceed the limit defined by your license. In no way does this affect access to basic functionalities such as saving configuration changes and allowing project browsing. In all cases, you can still analyze your code if the new analysis doesn’t surpass the LOC limit defined by your license.

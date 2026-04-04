# Source: https://docs.sonarsource.com/sonarqube-server/8.9/project-administration/managing-portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/project-administration/managing-portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/project-administration/managing-portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/project-administration/managing-portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/project-administration/managing-portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/project-administration/managing-portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/project-administration/managing-portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/project-administration/managing-portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/project-administration/managing-portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/project-administration/managing-portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/project-administration/managing-portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/project-administration/managing-portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/project-administration/managing-portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/project-administration/managing-portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/project-administration/managing-portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/project-administration/managing-portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/project-administration/managing-portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/project-administration/managing-portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/project-administration/managing-portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-portfolios.md

# Managing portfolios

This feature is only available in the [Enterprise plan](https://www.sonarsource.com/plans-and-pricing/).

Releasability is based on the projects’ quality gates included in your portfolio. Each portfolio home page offers an aggregate view of the releasability status of all projects in the portfolio. See [viewing-portfolios](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/viewing-enterprise-reports/viewing-portfolios "mention") for more information.

### Permissions <a href="#permissions" id="permissions"></a>

To manage a portfolio, you will need at least Edit permissions granted by the portfolio’s administrator. See [administering-portfolios](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/administering-portfolios "mention") for more details.

### Creating a portfolio <a href="#creating-portfolio" id="creating-portfolio"></a>

You can create a portfolio if you have the **Create Portfolio** permission enabled. See [#create-portfolios-permission](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/administering-portfolios#create-portfolios-permission "mention") for more details.

1. Select **My Portfolios** in the top navigation bar and select the enterprise to which you want to add a new portfolio.
2. Select **Create portfolio** on the Portfolios home page to start the portfolio creation wizard.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-96b72e3af66319509cc5342f0493484edf71f8cf%2Fe4200453abf928adacddf3cca6f5c1ef7aa3559e.png?alt=media" alt="The Create portfolio button is found on your SonarQube Cloud organization&#x27;s Portfolios page."><figcaption></figcaption></figure></div>

You can also create a portfolio by selecting the ‘+’ sign at the top right of the page.

#### Portfolio creation wizard

The wizard takes you through 4 steps of the portfolio creation process and the system automatically saves the information you have entered when you go to the next step. You can find the draft portfolios on the Portfolios home page and resume the process in case you get interrupted.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-63ea0c862bcecbd17cc0614b01ef5e49c8179e3a%2F7eadfa9af3596e9e587cb07243ae2390b836e055.png?alt=media" alt="The third step when creating a portfolio in SonarQube Cloud is to set permissions for users. Select Save and continue when finished."><figcaption></figcaption></figure></div>

The portfolio creation process consists of the following steps:

1. **Add details**: Choose the enterprise where the portfolio will reside if you have permission to more than one enterprise. Then, enter the portfolio name and description.
2. **Add projects**: From the **How do you want to add projects?** dropdown menu choose projects either:
   * **By name**: This option shows the list of organizations and projects associated with them. Select the projects and choose the project’s branch you want to include in the portfolio.
   * **By tags**: Select existing tags by which you want to query projects and define the project branch to add to the portfolio. If you choose a branch other than the main branch, you need to specify the branch’s name.
   * **By regular expression** (RegEx) using project keys: Write RegEx to query the project by project key and define the project branch to add to the portfolio. If you choose a branch other than the main branch, you need to specify the branch’s name.
   * **By organization**: Select the organizations and define the project’s branch to include in the portfolio. If you choose a branch other than the main branch, you need to specify the branch’s name.
3. **Set permissions**: Add portfolio Administer, Edit, and View permissions to specific groups and users or apply a permission template.
4. **Review**: Take a final look at all the portfolio details and select **Complete** to finalize the process.

{% hint style="info" %}
Currently, you cannot mix and match portfolio creation methods. For example, mixing RegEx and Tags to generate a list of projects for a portfolio is not possible. You can only use one method.
{% endhint %}

Once the portfolio is created, it will be populated with ratings for Releasability, Security, Reliability, Maintainability, and Security Review.

{% hint style="info" %}
The maximum number of projects that you can add to your portfolio is 5,000.
{% endhint %}

#### Ensuring a reliable security report

To ensure a reliable security report, check that the relevant security rules are activated in your quality profiles for projects you have included in your portfolio. For instance, if no rule corresponding to a given OWASP category is activated in your quality profile, you won’t get Security issues or Security Hotspots linked to that specific category in the OWASP report. See [#checking-security-rules](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/viewing-enterprise-reports/project-security-reports#checking-security-rules "mention") for more information.

### Defining a portfolio with regular expressions (RegEx)

You write RegEx against project keys included in your enterprise. A project key is not necessarily the same as a project name and, by default, it starts with the name of the organization that the project belongs to.

* To retrieve a project key, go to your project and select **Information** located in the left side bar.
* To change a project key, go to *Your Project* > **Administration** > **Update Key** and enter the new project key.

Following are examples of RegEx that may help you write your own expressions and retrieve matches against project keys.

Selects all projects with a key that includes `python`:

```regex
.*python.*
```

Selects all projects with a key that starts with `sonar`:

```regex
^sonar.*
```

Select all projects with a key that starts with either `docs` or `Docs`. Keep in mind that RegEx matches are case sensitive.

```regex
^[dD]ocs.*
```

Selects all projects with a key that ends with `-scanner`:

<pre class="language-regex"><code class="lang-regex"><strong>.*-scanner$
</strong></code></pre>

Select all projects with a key that contains `sonar` but does not contain `test`. If your enterprise has a large number of projects, more complex expressions might impact performance.

```regex
(?=.*sonar)(?!.*test).*
```

For more information about how to write regular expressions, see [regex101.com](https://regex101.com/). When testing your RegEx in third-party tools such as [regex101.com](https://regex101.com/) make sure that the whole test string is selected when the match is found.

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-0dcefb19c6b231d20d5de7b46e4126e1f90412ff%2Fportfolios-regex-test.png?alt=media" alt="testing regex"><figcaption></figcaption></figure>

### Editing a portfolio <a href="#editing-portfolio" id="editing-portfolio"></a>

With the Edit permission on a portfolio, you can add and remove projects from it. Note that you don’t add a project, but a long-lived branch of a project. Currently, you can only add a single branch per project.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-8632600e636c77349cc7d34c38ab3889c0ab6c04%2F511c69f36486f2ca339f4fc794f760d1410b01b5.png?alt=media" alt="To edit a portfolio in SonarQube Cloud, select Portfolio Definition from the Settings menu."><figcaption></figcaption></figure></div>

Proceed as follows:

1. In the top navigation bar, go to **My Portfolios** and select your enterprise from the drop-down menu.
2. On the Portfolios home page, select the portfolio you want to edit.
3. Go to **Settings** > **Portfolio Definition**.
4. Select **Edit selection**.
5. From a list of organizations and projects to which you have permissions, select projects to include or exclude from the portfolio. Alternatively, use the search field to find projects by name.
6. If the selected project contains several long-lived branches, select the branch to be added. By default, the **main** branch is selected.
7. Select **Save**.

### Deleting a portfolio <a href="#deleting-portfolio" id="deleting-portfolio"></a>

With the Edit permission on a portfolio, you can remove it from the system.

1. In the top navigation bar, go to **My Portfolios** and select your enterprise from the drop-down menu.
2. Select the portfolio you want to remove.
3. Go to **Settings** > **Delete** portfolio.

### Portfolio recomputation <a href="#portfolio-recomputation" id="portfolio-recomputation"></a>

The following events will trigger the recalculation of a portfolio:

* When a project within the portfolio has a new analysis.
* If a project is removed from an organization within the enterprise.
* When an organization is removed from the enterprise.

For information on how ratings are calculated, see [metric-definitions](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions "mention") for more information.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [introduction](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/introduction "mention") to Getting started with Enterprise
* [viewing-portfolios](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/viewing-enterprise-reports/viewing-portfolios "mention")
* [administering-portfolios](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/administering-portfolios "mention")

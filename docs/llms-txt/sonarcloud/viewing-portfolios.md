# Source: https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/viewing-enterprise-reports/viewing-portfolios.md

# Viewing portfolios

This feature is only available in the [Enterprise plan](https://www.sonarsource.com/plans-and-pricing/#sonarqube-cloud-features).

A portfolio is a set of projects within your enterprise that enables an aggregate view of the project metrics and risks. More precisely, a portfolio consists of project branches and for each project, you can add a single long-lived branch to the portfolio.

{% hint style="info" %}
Before you can view the Enterprise-level reports, your organization must be added to an enterprise. For more information, see [managing-enterprise](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise "mention").
{% endhint %}

### Retrieving a portfolio <a href="#retrieving-portfolio" id="retrieving-portfolio"></a>

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-f4bcde8f6cdf880d417a2d61d542cb8f7b59c659%2Fdc7fa028f4a4704aec6f09faf21ff67f8309bd99.png?alt=media" alt="An overview of all of your portfolios can be found on your Enterprise&#x27;s Portfolios page."><figcaption></figcaption></figure></div>

1. Click **My Portfolios** in the top navigation bar and select your enterprise
2. The **Portfolios** home page lists all the portfolios that belong to this organization. Use the search box to narrow down the results.
3. Here, you can review the portfolio’s overall code ratings, including the number of projects with the worst rating, see the number of Lines of Code analyzed, and see the number of projects included in the portfolio.
4. Click on the portfolio name to view more details.

See [managing-portfolios](https://docs.sonarsource.com/sonarqube-cloud/managing-portfolios "mention") for more information about how to create, edit, and delete portfolios.

### Portfolio metrics <a href="#portfolio-metrics" id="portfolio-metrics"></a>

The reliability, security vulnerabilities, security review, and maintainability ratings are calculated as the average of the ratings for all projects included in the portfolio.

SonarQube Cloud converts each project’s letter rating to a number, calculates an average number for the projects in the portfolio, and converts that average to a letter rating. Averages ending with .5 are rounded up, resulting in the "lower" of the two possible ratings, so an average of 2.5 would be rounded up to 3 and result in a "C" rating).

This gives a "problem density" measure for your portfolio’s four axes: reliability, security vulnerabilities, security review, and maintainability.

Rating conversion: E->5, D->4, C->3, B->2, A->1

A risk level is associated with each metric, except for the Releasability:

* **High**: if at least one project in the portfolio is rated E or D.
* **Medium**: if at least one project in the portfolio is rated C or B.
* **Low**: If all projects in the portfolio are rated A.

Each metric is calculated by SonarQube Cloud for New and Overall Code.

<details>

<summary>Releasability</summary>

* The releasability rating is based on the proportion of projects in the portfolio that have passed their quality gate. The rating is as follows:\
  **A**: > 80%\
  **B**: > 60% and <= 80%\
  **C**: > 40% and <= 60%\
  **D**: > 20% and <= 40%\
  **E**: <= 20%
* At the project level: The state of the quality gate associated with the project can be passed or failed.

</details>

<details>

<summary>Security</summary>

* The average security rating of all projects in the portfolio.
* At the project level: The security rating is related to issues that mark potential weaknesses to hackers. The rating is as follows:\
  **A**: 0 vulnerability\
  **B**: at least one minor vulnerability\
  **C**: at least one major vulnerability\
  **D**: at least one critical vulnerability\
  **E**: at least one blocker vulnerability

</details>

<details>

<summary>Reliability</summary>

* The average reliability rating of all projects in the portfolio.
* At the project level: The reliability rating is related to issues that mark code where you will get behavior other than what was expected. The rating is as follows:\
  **A**: 0 bugs\
  **B**: at least one minor bug\
  **C**: at least one major bug\
  **D**: at least one critical bug\
  **E**: at least one blocker bug

</details>

<details>

<summary>Maintainability</summary>

* The average maintainability rating of all projects in the portfolio.
* At the project level: The maintainability rating is related to issues that mark code that will be more difficult to update competently than it should. The maintainability rating is based on the technical debt ratio value (the ratio between the cost to develop the software and the cost to fix it). The default rating is as follows (this rating definition can be changed):\
  **A**: <= 0.05\
  **B**: > 0.05 and <= 0.1\
  **C**: > 0.1 and <= 0.20\
  **D**: > 0.2 and <= 0.5\
  **E**: > 0.5

</details>

<details>

<summary>Security review</summary>

* The average security review rating of all projects in the portfolio.
* At the project level: The security review rating is based on the percentage of reviewed security hotspots. Note that security hotspots are considered reviewed if they are marked as **Fixed** or **Safe**. The rating is as follows:\
  **A**: >= 80%\
  **B**: >= 70% and <80%\
  **C**: >= 50% and <70%\
  **D**: >= 30% and <50%\
  **E**: < 30%

</details>

### Overview page <a href="#overview-page" id="overview-page"></a>

Once you retrieve a portfolio, you will land on an Overview page, which displays a summary of information from the project branches included in the portfolio for Releasability, Security, Reliability, Maintainability, and Security Review. The ratings are calculated on new and overall code and include project distribution for a rating as well as a risk level.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2FrtPHFWnRdLbQ9DOGltsq%2Fportfolio-overview-page.png?alt=media&#x26;token=9353e239-f7f8-44d7-8efe-36f8d62eac69" alt="Overview page with quality gates ratio and ratings"><figcaption></figcaption></figure></div>

### Portfolio Breakdown page <a href="#portfolio-breakdown-page" id="portfolio-breakdown-page"></a>

The Portfolio Breakdown page lists projects included in the portfolio for which you have the **Browse** permission. They are ordered alphabetically, and you can switch between **New code** and **Overall code** views.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2F9XPadY75mWvKdP5ghK5q%2Fportfolio-breakdown-page.png?alt=media&#x26;token=5bcd3fa9-3490-4e4f-a772-3a931eb50e27" alt="The Portfolio Breakdown page reveals even more detail about each project in the portfolio."><figcaption></figcaption></figure></div>

### Measures page <a href="#measures-page" id="measures-page"></a>

The Measures page provides an in-depth breakdown of metrics across your portfolio projects, helping you gain broader visibility. It includes:

* **Software quality rating breakdown**: View ratings breakdown across multiple projects at once.
* **Code coverage visibility**: Easily see code coverage at the portfolio level without manually aggregating project data.
* **Duplication insights**: View duplications by project in your portfolio to maintain high-quality, maintainable software. Note that his feature does not cover cross-project duplications.
* **Lines of Code (LOC) tracking**: Quickly understand LOC usage breakdown by language and by project.

See [metric-definitions](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions "mention") for more information about code metrics used in the Sonar solution.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [managing-portfolios](https://docs.sonarsource.com/sonarqube-cloud/managing-portfolios "mention")
* [administering-portfolios](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/administering-portfolios "mention")
* [portfolio-security-reports](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/viewing-enterprise-reports/portfolio-security-reports "mention")
* [managing-enterprise](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise "mention")
* [viewing-portfolio-pdf-reports](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/viewing-enterprise-reports/viewing-portfolio-pdf-reports "mention")

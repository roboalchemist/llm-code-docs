# Source: https://docs.sonarsource.com/sonarqube-server/8.9/user-guide/portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/user-guide/portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/user-guide/portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/user-guide/portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/user-guide/portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/user-guide/portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/user-guide/portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/user-guide/portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/user-guide/portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/user-guide/portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/user-guide/viewing-reports/portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/user-guide/viewing-reports/portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/user-guide/viewing-reports/portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/user-guide/viewing-reports/portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/user-guide/viewing-reports/portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/viewing-reports/portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/user-guide/viewing-reports/portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/user-guide/viewing-reports/portfolios.md

# Source: https://docs.sonarsource.com/sonarqube-server/user-guide/viewing-reports/portfolios.md

# Portfolios

*Portfolios are available starting in* [*Enterprise Edition*](https://www.sonarsource.com/plans-and-pricing/enterprise/)*.*

### Portfolio Overview page <a href="#portfolios-home-page" id="portfolios-home-page"></a>

The Portfolio Overview page is the central place for managers and tech leads to keep an eye on the releasability of the projects under their supervision. Releasability is based on the projects’ quality gates included in the portfolio. Each portfolio home page offers an aggregate view of the releasability status of all projects in the portfolio.

Depending on the configuration of your SonarQube Server instance, the portfolio report is generated with metrics either from [standard-experience](https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/instance-mode/standard-experience "mention") or [mqr-mode](https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/instance-mode/mqr-mode "mention").

At the top of the page, you can see the overall releasablilty of the portfolio, a graph showing the releasability trend, and the number of project branches that are failing and passing their quality gate.

Reliability, Security (in MQR Mode) or Security Vulnerabilities (in Standard Experience), Security Review, and Maintainability ratings show the portfolio’s overall health, both for new code and overall code.

Below the new code rating for each metric, you see how many project branches are doing well and how many are at risk.

Below the overall code rating, a graph showing the trend for each metric is displayed, along with the number of at risk project branches.

### Releasability rating <a href="#releasability-rating" id="releasability-rating"></a>

The releasability rating is the ratio of projects in the portfolio that have a **passed** quality gate:

**A**: > 80%\
**B**: > 60%\
**C**: > 40%\
**D**: > 20%\
**E**: <= 20%

### Rating conversion <a href="#reliability-security-vulnerabilities-security-review-and-maintainability-ratings" id="reliability-security-vulnerabilities-security-review-and-maintainability-ratings"></a>

Reliability, Security (in MQR Mode) or Security Vulnerabilities (in Standard Experience), Security Review, and Maintainability ratings for a portfolio are calculated as the average of the ratings for all projects included in the portfolio.

SonarQube Server converts each project’s letter rating to a number (see conversion table below), calculates an average number for the projects in the portfolio, and converts that average to a letter rating. Averages ending with .5 are rounded up resulting in the "lower" of the two possible ratings, so an average of 2.5 would be rounded up to 3 and result in a "C" rating).

This gives a *problem density* measure on the four axes of Reliability, Security (in MQR Mode) or Security Vulnerability (in Standard Experience), Security Review, and Maintainability for your portfolio.

Rating conversion:

**E**: 5\
**D**: 4\
**C**: 3\
**B**: 2\
**A**: 1

*Note: the Portfolio Overview page is also available at the sub-portfolio level*

### Portfolio breakdown <a href="#portfolio-breakdown" id="portfolio-breakdown"></a>

The Portfolio Breakdown page shows ratings for your portfolio’s **Releasability**, **Security**, **Reliability**, **Maintainability**, and **Security Review** for new and overall code. Additional columns include **Lines of code** and **Last analysis**.

#### Viewing your portfolio details <a href="#viewing-your-portfolio-details" id="viewing-your-portfolio-details"></a>

The **Portfolio details** section shows the aggregated portfolio rating. If the projects included in the portfolio have AI Code Assurance enabled on their quality gates, additional ratings appear for:

* **AI Code Assurance enabled projects**
* **Projects without AI Code Assurance enabled**

See the [ai-code-assurance](https://docs.sonarsource.com/sonarqube-server/ai-capabilities/ai-code-assurance "mention") page for more information about enabling AI Code Assurance on your projects.

#### Viewing the portfolio breakdown <a href="#viewing-the-portfolio-breakdown" id="viewing-the-portfolio-breakdown"></a>

The breakdown section includes a list of all projects, applications and nested portfolios included in your portfolio. The ![$contains-ai-code](https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/deARgTT8I1JCv43oMpXD/c151514ef7beca0f865ee429bc9fe0e33b05ceb4.svg) label indicates that the item includes AI-generated code, as marked by a Quality Standard admin.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [pdf-reports](https://docs.sonarsource.com/sonarqube-server/user-guide/viewing-reports/pdf-reports "mention")
* [managing-portfolios](https://docs.sonarsource.com/sonarqube-server/project-administration/managing-portfolios "mention")

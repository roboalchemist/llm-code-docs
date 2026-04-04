# Source: https://docs.sonarsource.com/sonarqube-server/8.9/user-guide/applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/user-guide/applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/user-guide/applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/user-guide/applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/user-guide/applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/user-guide/applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/user-guide/applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/user-guide/applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/user-guide/applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/user-guide/applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/user-guide/applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/user-guide/applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/user-guide/applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/user-guide/applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/user-guide/applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/user-guide/applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/user-guide/applications.md

# Source: https://docs.sonarsource.com/sonarqube-server/user-guide/applications.md

# Using applications

### Using applications <a href="#using-applications" id="using-applications"></a>

Assume that you have a set of projects which have been split for technical reasons, but which share a life cycle; they interact directly in production and are always released together. With an application, they can be treated as a single entity in SonarQube Server with a unified project homepage, issues list, measures space, and most importantly, pass through the same quality gate.

#### Applications vs. portfolios <a href="#applications-vs-portfolios" id="applications-vs-portfolios"></a>

Applications and portfolios are both aggregations of projects but have different goals and, therefore, different presentations. A portfolio is designed to provide a very high-level, executive overview that gives a perspective on quality between what may be only tangentially related projects. Applications allow you to see your set of projects as a larger, overall meta-project. For instance, because all the projects in an application ship together, if one of them isn’t releasable, then none of them are, and an Application’s consolidated quality gate gives you an immediate summary of what must be fixed across all projects in order to allow you to release the set.

### Application setup <a href="#application-setup" id="application-setup"></a>

You can create an application by selecting **Create Application** in the upper-right corner of the **Projects** homepage.

Starting in [Enterprise Edition](https://www.sonarsource.com/plans-and-pricing/enterprise/), you can also create and edit applications in the global portfolio administration interface at **Administration** > **Configuration** > **Portfolios**.

For more information on setting up applications, see [managing-applications](https://docs.sonarsource.com/sonarqube-server/project-administration/managing-applications "mention").

#### Populating application data <a href="#populating-application-data" id="populating-application-data"></a>

An application is automatically re-calculated after each analysis of one of its projects. If you want immediate (re)calculation, anyone with **Administration** user rights on the application can use the **Recompute** button in the application-level **Application Settings** > **Edit Definition** interface.

Starting in [Enterprise Edition](https://www.sonarsource.com/plans-and-pricing/enterprise/), the global Portfolio administration interface, **Administration** > **Configuration** > **Portfolios**, offers the ability to queue the analysis of all Applications and Portfolios at once.

### Applications and branch analysis <a href="#applications-and-branch-analysis" id="applications-and-branch-analysis"></a>

Branches are available for applications. They allow you to aggregate branches from the projects in an Application.

**Note:** To prevent issues with your Application status, avoid adding branches to your application that will be deleted.

Once an Application has been set up, anyone with **Administration** user rights on the application can manually create a new branch in the **Application Settings** > **Edit Definition** interface. In Enterprise Edition and above, you can also manage branches from the global **Administration** > **Configuration** > **Portfolios** interface. For each application branch, you can choose which project branch should be included or decide whether the project should be represented in the branch at all.

### Using application badges to promote application health <a href="#application-badges" id="application-badges"></a>

You can promote your application’s status in third-party tools and external websites using application badges. You can find the application badges by opening the **Application Information** menu in the upper-right corner of the application home page and clicking **Get application badges**. From here, you can choose and fine-tune your badge then copy the markdown text or image URL. Each application badge has a unique security token, which is required to make it accessible from third-party tools.

Using application badges can expose sensitive information like your security rating and other metrics. Because of this, you should only use them in trusted environments. If an application badge URL is accessed by someone who should not have access to it, a project administrator can renew the application badge’s unique token by clicking the **Renew token** button. This invalidates any existing application badge URLs, and you’ll have to update all locations where the badge is being used.

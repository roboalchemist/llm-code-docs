# Source: https://docs.axonius.com/docs/saas-applications-repository.md

# SaaS Applications Repository

The SaaS Application Repository page contains data and pages for a myriad of SaaS applications that you can use to evaluate potential vendors. This includes general information about these apps and their vendors, and is not limited to applications that are used in your organization.

For information on SaaS applications discovered in your organization, see the SaaS Applications asset page.

Each application profile in the repository contains the following information:

* [Risk level](/docs/application-risk-score)

* Company location

* Employee count

* Founding Year

* Compliance standards

* whether the company is private or public

* And much more

<Image alt="SaaSAppsREpoNewUI.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SaaSAppsREpoNewUI.png" />

For more information about SaaS Applications discovered in your organization, see the [SaaS Applications](/docs/saas-applications) asset page.

## Views

The **SaaS Applications** page opens displaying the default **Tables** view. You can change to the **Tiles** view by selecting the Tiles icon ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TilesIcon.png).

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SelectTiles.png)

For more information on using Tiles view, see [SaaS Applications](/docs/saas-applications).

## Creating Queries on SaaS Applications

You can create queries on the SaaS Application Repository page using the Query Wizard or the Basic Query and query fields such as the Category, and compliance fields. You can add additional levels to the query, such as querying by risk and security policy. Use these queries to find out which applications exist with asset context in your environment or how many applications have a particular risk score. Refer to [Creating Queries with the Queries Wizard](/docs/query-wizard-and-query-filter) and [how to create Queries in Basic mode](/docs/basic-query-mode) to learn more about creating queries.

For example, this query enables you to low-risk monitoring applications that are sold by publicly owned companies:
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SARepositoryQuery.png)

After running the query, the overview and table show the queried applications, filtered by the criteria you defined in your query.

## Adding Custom Data to an Application

You can add custom fields to one or more SaaS Application assets in the repository at the same time. For example, you can add notes, custom risk Evaluations, or other data points that you can edit for an application.

Select one or more applications and from the **Actions** menu choose **Add Custom Fields**.

<Image alt="AddCustFieldSaaSAppRepo.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AddCustFieldSaaSAppRepo.png" />

Any data added to an application record, remains on the application when it is discovered on your system.

Refer to [Working with Custom Data](/docs/working-with-custom-data) to learn about adding custom fields.

## Add Tags to SaaS Applications

Use tags to assign context to your assets for granular filters and queries. Apply new or existing tags to the selected applications. The list of selected tags is applied to all selected applications.

Any tags added to an application record remain on the application when it is discovered on your system.

Refer to [Working with Tags](/docs/working-with-tags) to learn about adding tags to applications.

## View an Application Profile

To open an application's page and review its details in greater depth, click its corresponding row. For applications discovered in your organization, the data displayed here is to that in the [application's profile page](/docs/saas-applications#view-an-application-profile).
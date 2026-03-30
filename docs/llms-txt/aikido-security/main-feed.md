# Source: https://help.aikido.dev/getting-started/core-functionalities/main-feed.md

# Main Feed

## Main Feed

### Introduction <a href="#introduction" id="introduction"></a>

Aikido's Feed is meticulously designed to streamline security management: it groups similar issues for clarity, allows for customizable views to highlight what's currently important. The main feed focusses on open issues only. Snoozed and ignored issues are accessible on a separate page for a clean giving a focused and clean overview.

### Aikido's Main Feed <a href="#aikidos-main-feed" id="aikidos-main-feed"></a>

The **Feed** is the central hub for monitoring and managing security issues. A similar view can be found all over Aikido when going into details of repositories, clouds and domains.

By default, Aikido enables the **Focus** view, containing all issues that are important to follow-up. By toggling to **All** we will also show issues that have been auto-triaged and ignored.

*Status Column*

Shows the status of the particular issue.

* *New*: issues that have been around for less than 7 days
* *To Do:* all other issues that are still unresolved
* *Task Open:* only when a task manager is linked
* *PR Open:* clicking will take you to PR / branch scan overview.

![Security dashboard showing vulnerability status, severity, fix times, and task assignments for issues.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-5cb555f73d17f6d317932191188f13d4677b5de0%2Fmain-feed_e134c1d8-5218-4f06-96d2-2cb099968f41.png?alt=media)

### Sidebar <a href="#sidebar" id="sidebar"></a>

Aikido's Feed is equipped with a detailed sidebar, designed to provide users with comprehensive information and actionable options for each security issue. The image below shows the main important actions one can take.

**#1 Group Actions:** these are actions that can be taken on group level of an issue.

**#2 Subissue Actions:** you can also take actions on a subissue separately. This can be important when certain subissues want to be snoozed or ignored, but the overal issue group should remain in the main feed.

**#3 Reachability Analysis:** visualizes accessible code paths for that specific issue.

**#4 Detail Screen**: Separate detail screen with even more information (e.g., CVE information).

![Security dashboard showing a critical vulnerability in the 'bson' package with actionable steps.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-1f6fb449f589e649ad898af25e94711cbc0fffaf%2Fmain-feed_7d0dadc8-a23e-4f23-b207-c1710b0ce1df.png?alt=media)

**Reachability Analysis**

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-1251e9ff34ebcce7f172efe396d5a5f537a061bb%2Fmain-feed_1aabe4cf-b6b9-44e5-b953-41f35c7ef824.png?alt=media)

### Filter Issues <a href="#filter-issues" id="filter-issues"></a>

You can easily adjust the view in order to filter on those issues that are most important to you in the moment. These filters can be found above the issue table in every feed view. You can filter on

* **Issue Type**
* **Predefined filtered views**
  * If you are using the [**SLA functionality**](https://help.aikido.dev/en/articles/8926339-enabling-slas-in-aikido), you will be able to see all upcoming and out of SLA issues

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-8c544a031cfaa1e383902af5efee62f1a0c14dc7%2Fmain-feed_ac998c65-834e-4bad-b76b-550ca0c2db6b.png?alt=media)

### Export Issues to CSV or PDF <a href="#export-issues-to-csv-or-pdf" id="export-issues-to-csv-or-pdf"></a>

You can export a CSV or PDF of issues. You can configure which issues to export exactly. This can be triggered from the Actions menu in the top right.

![Export issues: Filter by status, type, team, and format for CSV or PDF download.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-10981ff893e46976c3e8e0f2e87817e9308b46a7%2Fmain-feed_fc64121c-f6e4-4e98-87b9-e2c0cedcdf20.png?alt=media)

### Show issues per team or project <a href="#show-issues-per-team-or-project" id="show-issues-per-team-or-project"></a>

**Aikido's Feed** features a **team filter** at the top of the page. This filter allows users to tailor the feed to display only the issues relevant to selected teams ([📖 Set Up Teams](https://help.aikido.dev/en/articles/9005606-using-teams-for-repository-and-user-management)).

![Team selector dropdown with search and statistics on solved and new issues.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-61296e08665b9c3e6e29330ab62bf16a1916b53d%2Fmain-feed_7d1a69e7-7618-4eae-b374-ee6322f9fd43.png?alt=media)

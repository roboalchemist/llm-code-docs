# Source: https://docs.sonarsource.com/sonarqube-server/8.9/user-guide/project-page.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/user-guide/project-page.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/user-guide/project-page.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/user-guide/project-page.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/user-guide/project-page.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/user-guide/project-page.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/user-guide/project-page.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/user-guide/project-page.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/user-guide/project-page.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/user-guide/project-page.md

# Project page

The **Project homepage** is the entry point of any project showing:

* the releasability status of the project.
* the current state of its quality.
* the quality of what has been produced since the start of your [defining-new-code](https://docs.sonarsource.com/sonarqube-server/10.6/project-administration/clean-as-you-code-settings/defining-new-code "mention").

The **Project homepage** answers two questions:

* Can I release my project today?
* If I cannot release it today, what should I improve to make the project pass it’s quality gate?

### Quality gate <a href="#quality-gate" id="quality-gate"></a>

Since the [quality-gates](https://docs.sonarsource.com/sonarqube-server/10.6/user-guide/quality-gates "mention") is your most powerful tool to enforce your quality policy, the page starts with the project’s current quality gate status. If the project passes, the **Quality Gate Status** will show a simple, green all-clear banner.

If not, details and drill-downs are immediately available to quickly identify what went wrong, with a section for each error condition showing what the current project value is and what it should be. As usual, you’ll be able to click through on current values to get more details about each issue.

### Prioritizing issues <a href="#prioritizing-issues" id="prioritizing-issues"></a>

Because the best way to improve a project’s quality is to catch and fix new problems before they become entrenched, the first view of a project is centered around *new code* which is highlighted in yellow on the right of the project homepage. The project space page shows a high-level summary of critical metrics, including current values, and their new code values.

Just below the quality gate information, you have the numbers of old and new issues in the reliability and security domains and then the maintainability domain. Clicking on any figure on the page will take you to a detailed view, either on the **Measures** page or the **Issues** page.

The most important thing a developer must do is to ensure the new issues in the yellow part of the screen are acknowledged, reviewed, and fixed to make sure that new code is covered by tests that help prevent future regressions. Regardless of how many Issues were introduced in the past or how little test coverage there is overall, focusing on newly added issues will ensure that the situation won’t degrade versus the version you previously released in production.

Which issues should you go after first? Bugs, vulnerabilities or code smells? The correct answer depends on the nature of your issues. Let’s say you have issues with a block of code that is duplicated 5 times, and inside this duplicated block of code, you have 3 bugs and 5 security issues. The best approach is probably to fix the duplication first, then resolve the bugs and vulnerabilities in the new centralized location, rather than fixing each bug and vulnerability 5 times.

This is why you need to review your new issues before jumping into resolving each.

### Viewing project measures at a lower level <a href="#viewing-project-measures-at-a-lower-level" id="viewing-project-measures-at-a-lower-level"></a>

The project-level **Measures** menu item takes you to a dedicated sub-space where you see all project measures. Select a measure for more details. Both list and tree views are available for each measure, and treemaps are available for percentages and ratings.

#### Viewing all issues in a project <a href="#viewing-all-issues-in-a-project" id="viewing-all-issues-in-a-project"></a>

The project-level **Issues** menu item takes you to a project-specific issues page, where you can perform all the same actions you can at the higher level. On this page, you can easily narrow the list to the new issues as set by your new code definition, by selecting *New Code* in the **Creation Date** facet.

### Viewing project structure and code <a href="#viewing-project-structure-and-code" id="viewing-project-structure-and-code"></a>

The project-level **Code** menu item takes you to an outline of your project structure. Drill down to see files in a directory, and choose a file to see its code.

If your project is too large for easy exploration via drilling, the search feature on this page will help. While the global search in the main menu returns results from throughout the SonarQube instance, the localized search on the code page is restricted to files and directories in the current project.

### Viewing project activity and history <a href="#viewing-project-activity-and-history" id="viewing-project-activity-and-history"></a>

The project-level **Activity** menu item takes you to the full list of code scans performed on your project since it was created in SonarQube. By going there you can follow the evolution of the quality gate, see the changes in quality profiles, and know discover when a given version of your code has been scanned, and more. For details, see [activity-and-history](https://docs.sonarsource.com/sonarqube-server/10.6/user-guide/activity-and-history "mention").

### Spotting risks with visualizations <a href="#spotting-risks-with-visualizations" id="spotting-risks-with-visualizations"></a>

Visualizations allow you to compare project components and quickly spot the ones that represent the greatest risks. The **Activity** page offers several pre-defined visualizations, and you can also create custom visualizations with the metrics of your choice.

### Using project badges to promote project health <a href="#using-project-badges-to-promote-project-health" id="using-project-badges-to-promote-project-health"></a>

You can promote your project’s status in third-party tools and external websites using project badges. To find the project badges, go to *your project’s homepage* > **Project Information** > **Get project badges**.

From there, you can choose and fine-tune your badge then copy the markdown text or image URL for it. Each project badge has a unique security token, which is required to make it accessible from third-party tools.

Using project badges can expose sensitive information like your security rating and other metrics. You should only use them in trusted environments. If a project badge URL is accessed by someone who should not have access to it, a project administrator can renew the project badge’s unique token by clicking **Renew token**. This invalidates any existing project badge URLs, and you’ll have to update all locations where the badge is being used.

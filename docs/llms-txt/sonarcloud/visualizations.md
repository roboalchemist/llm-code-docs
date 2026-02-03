# Source: https://docs.sonarsource.com/sonarqube-server/8.9/user-guide/visualizations.md

# Visualizations

Visualizations are available to help you gain deeper insights into your projects’ current statuses and histories.

### How do I compare current state for multiple projects or project components? <a href="#compare-current-state-for-multiple-projects-or-project-components" id="compare-current-state-for-multiple-projects-or-project-components"></a>

The projects space allows you to filter the projects in your instance by multiple, measure-based criteria. Once you’ve chosen your set, you don’t have to stare at the raw numbers to identify the risks its projects face. Instead, several visualizations (**Projects** > **Perspective**) are available to help you understand each project’s relative position in terms of each of the major axes:

* Risk: reliability and security ratings, test coverage, technical debt, and lines of code.
* Reliability: reliability rating, reliability remediation effort, lines of code, and bug count.
* Security: security rating, security remediation effort, lines of code, and vulnerability count.
* Maintainability: maintainability rating, technical debt, lines of code, and code smell count.
* Coverage: coverage, complexity, and uncovered lines.
* Duplications: duplicated lines %, lines of code, and duplicated blocks.
* At the project level, these same visualizations are available in the measures tab to help you compare project components. The project overview corresponds to the risk visualization in the projects space, For the other five graphs, choose the overview option under the relevant domain.

Additionally, treemaps are also available for percentage and rating metrics at the project level. Navigate to them in the **Measures** tab using the perspective selector in the right pane.

### How to visualize metric history <a href="#how-to-visualize-metric-history" id="how-to-visualize-metric-history"></a>

At the project level, the activity tab offers several canned line graphs of selected metrics across time, with convenient mouseovers to show graph details and the ability to easily narrow the graph to a slice of the project’s history. Beyond the canned graphs, you also have the ability to map the metrics of your choice against each other in a custom graph.

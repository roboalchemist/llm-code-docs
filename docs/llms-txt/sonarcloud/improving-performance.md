# Source: https://docs.sonarsource.com/sonarqube-server/10.4/instance-administration/improving-performance.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/instance-administration/improving-performance.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/instance-administration/improving-performance.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/server-upgrade-and-maintenance/maintenance/improving-performance.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/server-upgrade-and-maintenance/maintenance/improving-performance.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/server-update-and-maintenance/maintenance/improving-performance.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-update-and-maintenance/data-center-edition/improving-performance.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-update-and-maintenance/maintenance/improving-performance.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-update-and-maintenance/data-center-edition/improving-performance.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-update-and-maintenance/maintenance/improving-performance.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/maintenance/improving-performance.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-update-and-maintenance/data-center-edition/improving-performance.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-update-and-maintenance/maintenance/improving-performance.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-update-and-maintenance/data-center-edition/improving-performance.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-update-and-maintenance/maintenance/improving-performance.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/data-center-edition/improving-performance.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/maintenance/improving-performance.md

# Improving performance

The following options are available to help you improve the performance of your SonarQube Server instance.

### Increasing the number of Compute Engine workers <a href="#increasing-the-number-of-compute-engine-workers" id="increasing-the-number-of-compute-engine-workers"></a>

{% hint style="info" %}
The ability to manage Compute Engine performance is available as part of [Enterprise edition](https://www.sonarsource.com/plans-and-pricing/enterprise/) and above.
{% endhint %}

If analyses are taking too long to process, it may be that you need to increase the number of Compute Engine (CE) workers (**Administration** > **Projects** > **Background Tasks** > **Number of Workers**).

There are two cases to consider:

1. Slowness comes from the fact that the queue is often full of pending tasks.
2. Individual tasks take a long time to process.

In the first case, increasing the number of workers could help. The second case should be carefully evaluated. In either case, when considering increasing the number of CE workers, two questions should be answered.

* Does my infrastructure allow me to increase the number of workers?
* To what extent should I increase the number of workers? What number should I configure?

Increasing the number of workers will increase the stress on the resources consumed by the CE. Those resources are:

* the DB.
* disk I/O.
* the network.
* heap.
* CPU.

Of those, only the last two are internal to the CE.

If slowness comes from any of the external resources (DB, disk I/O, network), then increasing the number of workers could actually slow the processing of individual reports (think of two people trying to go through a door at the same time). However, if your slow speed is caused by large individual analysis reports hogging the CE worker for extended periods of time, then enabling parallel processing by adding another worker could help. If parallel processing is enabled, you will need to take a look at the internal resources.

CE workers are not CPU-intensive and memory use depends entirely on the project that was analyzed. Some workers need a lot of memory, while others don’t. With multiple CE workers, you should increase CE heap size by a multiple of the number of workers. The same logic applies to CPU: if running with one worker consumes up to Y% of CPU, then you should plan for Z workers requiring Y\*Z% of CPU.

{% hint style="warning" %}
If you are increasing your CE worker count, the memory allocation for `sonar.ce.javaOpts` in your `sonar.properties` file should also be increased. Adjusting your CE worker count without adjusting the total memory available can negatively impact performance because the available memory is divided among all workers.&#x20;

See the [#memory-settings](https://docs.sonarsource.com/sonarqube-server/monitoring/instance#memory-settings "mention") article for information and restart SonarQube when changing your memory allocation.
{% endhint %}

To accurately diagnose your situation, monitor network latency, the I/O of the SonarQube Server instance, the database CPU, and memory usage to evaluate whether slowness is mainly/mostly/only related to external resources.

If you increase the number of CE for clusters (*available in* [*Data Center edition*](https://redirect.sonarsource.com/editions/datacenter.html)), CE workers are replicated across each application node. The number of workers is global and cannot be configured at the application node level.

For example, if you set 4 workers in SonarQube Server UI and you have 2 application nodes, you have configured 8 workers total after you finish restarting all the application nodes (4 workers \* 2 nodes = 8 workers total). See the [dce-topology](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/dce-topology "mention") page for more information.

### Parallel processing of pull request and branch analyses <a href="#parallel-processing-of-pull-request-and-branch-analyses" id="parallel-processing-of-pull-request-and-branch-analyses"></a>

{% hint style="info" %}
This feature is available as part of [Enterprise edition](https://www.sonarsource.com/plans-and-pricing/enterprise/) and above.
{% endhint %}

By default, SonarQube Server’s Compute Engine (CE) is enabled to perform parallel processing of pull request analyses and branch analyses for each project, thus enabling it to analyze one branch and several pull requests together at any given time. To avoid errors, the main branch of a project must be analyzed first, before any other branches or PRs are analyzed in parallel.

You have the option to disable this feature if you want the CE to process one analysis at a time for each project, even if there are multiple CE workers available.

To deactivate this option, go to **Administration** > **General Settings** > **General** > **Performance** and check the **Disable running project analysis tasks in parallel** option.

### Optimizing the loading of analyzers <a href="#optimizing-the-loading-of-analyzers" id="optimizing-the-loading-of-analyzers"></a>

SonarQube Server optimizes the loading of analyzers by downloading only those required for the detected languages.

For example, if you don’t have any COBOL files in your repository, the COBOL analyzer won’t be downloaded before analysis, saving network bandwidth, disk space, and time to bootstrap the code scan.

This behavior is enabled by default. To disable it:

1. Go to **Administration** > **General Settings** > **General** > **Performance**.
2. Disable the **Analyzers loading optimization** option.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [performance-issues](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/troubleshooting/performance-issues "mention")

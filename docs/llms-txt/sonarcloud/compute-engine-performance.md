# Source: https://docs.sonarsource.com/sonarqube-server/8.9/instance-administration/compute-engine-performance.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/instance-administration/compute-engine-performance.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/instance-administration/compute-engine-performance.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/instance-administration/compute-engine-performance.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/instance-administration/compute-engine-performance.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/instance-administration/compute-engine-performance.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/instance-administration/compute-engine-performance.md

# Compute engine performance

{% hint style="info" %}
The ability to manage Compute Engine performance is available as part of [Enterprise Edition](https://www.sonarsource.com/plans-and-pricing/enterprise/) and above.
{% endhint %}

### Increasing the number of Compute Engine workers <a href="#increasing-the-number-of-compute-engine-workers" id="increasing-the-number-of-compute-engine-workers"></a>

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

To accurately diagnose your situation, monitor network latency, the I/O of the SonarQube instance, the database CPU, and memory usage to evaluate whether slowness is mainly/mostly/only related to external resources.

### Parallel processing of pull request and branch analyses <a href="#parallel-processing-of-pull-request-and-branch-analyses" id="parallel-processing-of-pull-request-and-branch-analyses"></a>

{% hint style="info" %}
This feature is available as part of [Enterprise Edition](https://www.sonarsource.com/plans-and-pricing/enterprise/) and above.
{% endhint %}

By default, SonarQube only processes one analysis at a time for each project, even if there are multiple CE workers available. Pull request analyses and branch analyses are put in the same queue and processed in their order of insertion.

To speed up the process, you can configure the CE to enable parallel processing of pull request analyses and branch analyses for each project. Once enabled, SonarQube can analyze one branch and several pull requests together at any given time.

To activate this option, go to **Administration > General Settings > General > Compute Engine** and check the **Enable running project analysis tasks in parallel** option.

This feature requires multiple CE workers to be configured. Note that enabling this feature may impact the accuracy of issue tracking between branches.

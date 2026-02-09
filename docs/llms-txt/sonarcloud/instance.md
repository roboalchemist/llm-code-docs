# Source: https://docs.sonarsource.com/sonarqube-community-build/server-update-and-maintenance/monitoring/instance.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/instance-administration/monitoring/instance.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/instance-administration/monitoring/instance.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/instance-administration/monitoring/instance.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/server-upgrade-and-maintenance/monitoring/instance.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/server-upgrade-and-maintenance/monitoring/instance.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/server-update-and-maintenance/monitoring/instance.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-update-and-maintenance/monitoring/instance.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-update-and-maintenance/monitoring/instance.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/monitoring/instance.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-update-and-maintenance/monitoring/instance.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-update-and-maintenance/monitoring/instance.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/monitoring/instance.md

# SonarQube Server instance

As a start, you can use this Web API to get an overview of the health of your SonarQube Server installation:

* `api/system/health`

### Java process memory <a href="#java-process-memory" id="java-process-memory"></a>

SonarQube Server consists of three main Java processes:

* Compute Engine
* Elasticsearch
* Web (including embedded web server)

Each of these Java processes has its own memory settings that can be configured in the `<sonarqubeHome>/conf/sonar.properties` file. The default memory settings that ship with SonarQube Server are fine for most instances. If you are supporting a large SonarQube Server instance (more than 100 users or more than 5,000,000 lines of code) or an instance that is part of your continuous integration pipeline, you should monitor the memory and CPU usage of all three key Java processes on your instance, along with overall disk space. Monitoring will allow you to see if any of the processes is running short of resources and take action ahead of resource shortages. There are numerous monitoring tools available, both open-source and commercial, to help you with this task. Sonar does not recommend or endorse any particular tool.

### Memory settings <a href="#memory-settings" id="memory-settings"></a>

You may need to increase your memory settings if you see the following symptoms:

* Your monitoring tools show one or more of the SonarQube Server processes is reaching its memory limit.
* Any of the SonarQube Server processes crashes and/or generates an out-of-memory error in the sonar.log file.
* A SonarQube Server background task fails with an out-of-memory error in the background task log.
* The store size of the Issues index of your Elasticsearch instance (visible in the System Info) is greater than or equal to the memory allocated to the Elasticsearch Java process.

You can increase the maximum memory allocated to the appropriate process by increasing the `-Xmx` memory setting for the corresponding Java process in your `<sonarqubeHome>/conf/sonar.properties` file:

| **Java Process** | **SonarQube Server Property** | **Notes**                                                                                                                                                                                                  |
| ---------------- | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compute Engine   | `sonar.ce.javaOpts`           | <p><br></p>                                                                                                                                                                                                |
| Elasticsearch    | `sonar.search.javaOpts`       | It is recommended to set the min and max memory to the same value to prevent the heap from resizing at runtime, which diverts JVM resources and can greatly increase response times of in-flight requests. |
| Web              | `sonar.web.javaOpts`          | <p><br></p>                                                                                                                                                                                                |

The `-Xmx` parameter accepts numbers in both megabytes (e.g. `-Xmx2048m`) and gigabytes (e.g. `-Xmx2G`). The metric suffix is case-insensitive.

### Exposed JMX MBeans <a href="#exposed-jmx-mbeans" id="exposed-jmx-mbeans"></a>

SonarQube Server offers visibility about what happens internally through the exposure of JMX MBeans.

In addition to the classical Java MBeans providing information about the ClassLoader, OS, Memory, and Threads you have access to three more MBeans in SonarQube Server:

* ComputeEngine
* Database
* SonarQube

All these MBeans are read-only. It’s not possible to modify or reset their values in real time.

<details>

<summary>ComputeEngineTasks MBean</summary>

| **Attribute Name** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ProcessingTime     | The measure the time (in ms) spent processing background tasks since the last restart of SonarQube Server. Its value will always increase and will be reset by a restart of SonarQube Server. This measure is very powerful when combined with SuccessCount and ErrorCount measures to get the average time to handle a Background Task, or when used to understand how much time the SonarQube Server is spending during a day handling Background Tasks. It gives you an indication of the load on your server. |
| ErrorCount         | The number of background tasks that failed since the last restart of SonarQube Server.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| PendingCount       | The number of background tasksThe number waiting to be processed since the last restart of SonarQube Server. This measure is the same for all Compute Engine workers since Background Tasks are waiting in a common queue.                                                                                                                                                                                                                                                                                        |
| InProgressCount    | The number of background tasks currently processing. Its value is either 1 or 0, since SonarQube Server can process only one task at a time.                                                                                                                                                                                                                                                                                                                                                                      |
| SuccessCount       | The number of background tasks successfully processed since the last restart of SonarQube Server.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| WorkerCount        | The number of background tasks that can be processed at the same time.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| PendingTime        | The amount of time (in ms) that the oldest background task has been waiting to be processed. This measure, together with PendingCount, helps you know if analyses are stacking and taking too long to start processing. This helps you evaluate if it might be worth configuring additional Compute Engine workers (Enterprise Edition) or additional nodes (Data Center Edition) to improve SonarQube Server performance.                                                                                        |

{% hint style="info" %}
Note that the total number of background tasks handled since the last restart of SonarQube Server is equal to SuccessCount + ErrorCount. Also, all values will reset to their default values after restarting SonarQube Server.
{% endhint %}

</details>

<details>

<summary>Database MBean</summary>

**The same attributes are available for both ComputeEngineServer and WebServer.**

| **Attribute Name**                | **Description**                                                                                                                |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| MigrationStatus                   | Possible values are: `UP_TO_DATE`, `REQUIRES_UPGRADE`*,* `REQUIRES_DOWNGRADE`, `FRESH_INSTALL` (only available for WebServer). |
| PoolActiveConnections             | Number of active database connections                                                                                          |
| PoolIdleConnections               | Number of database connections waiting to be used                                                                              |
| PoolInitialSize                   | Initial size of the database connections pool.                                                                                 |
| PoolMaxActiveConnections          | Maximum number of active database connections                                                                                  |
| PoolMaxIdleConnections            | Maximum number of database connections waiting to be used                                                                      |
| PoolMaxWaitMillis                 | In milliseconds                                                                                                                |
| PoolRemoveAbandoned               | Possible values : `true`, `false`                                                                                              |
| PoolRemoveAbandonedTimeoutSeconds | In seconds                                                                                                                     |

</details>

<details>

<summary>SonarQube MBean</summary>

| **Attribute Name** | **Description**               |
| ------------------ | ----------------------------- |
| LogLevel           | Log Level: INFO, DEBUG, TRACE |
| ServerId           | SonarQube Server host ID      |
| Version            | SonarQube Server Version      |

</details>

### How do I activate JMX? <a href="#how-do-i-activate-jmx" id="how-do-i-activate-jmx"></a>

#### Local access <a href="#local-access" id="local-access"></a>

There is nothing to activate to view SonarQube MBeans if your tool is running on the same server as the SonarQube Server.

#### Remote access <a href="#remote-access" id="remote-access"></a>

Here are examples of configurations to activate remote access to JMX MBeans.

For the WebServer:

```css-79elbk
# JMX WEB - 10443/10444
sonar.web.javaAdditionalOpts=-Dcom.sun.management.jmxremote=true -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.authenticate=true -Dcom.sun.management.jmxremote.port=10443 -Dcom.sun.management.jmxremote.rmi.port=10444 -Dcom.sun.management.jmxremote.password.file=/opt/sonarsource/sonar/conf/jmxremote.password -Dcom.sun.management.jmxremote.access.file=/opt/sonarsource/sonar/conf/jmxremote.access
```

For the ComputeEngine, there is no specific `javaAdditionalOpts` entry, simply amend `sonar.ce.javaOpts`.

Example of `jmxremote.access`:

```css-79elbk
#
# JMX Access Control file
#
reader readonly
admin  readwrite \
    create javax.management.monitor.*,javax.management.timer.*,com.sun.management.*,com.oracle.jrockit.* \
    unregister
```

Example of `jmxremote.password`:

```css-79elbk
#
# JMX Access Password file
#
reader readerpassword
admin  adminpassword
```

Note: You should apply `chmod 600` or `400` on the file `jmxremote.password`, for security reasons.

### Prometheus monitoring <a href="#prometheus-monitoring" id="prometheus-monitoring"></a>

You can monitor your SonarQube instance using SonarQube’s core integration with Prometheus. Through this integration, you can ensure your instance is running properly and know if you need to take action to prevent future issues.

See Setting up the monitoring of a Kubernetes deployment [introduction](https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/set-up-monitoring/introduction "mention") page.

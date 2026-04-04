# Source: https://docs.sonarsource.com/sonarqube-server/8.9/instance-administration/server-logs-and-system-info.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/instance-administration/server-logs-and-system-info.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/instance-administration/server-logs-and-system-info.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/instance-administration/server-logs-and-system-info.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/instance-administration/server-logs-and-system-info.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/instance-administration/server-logs-and-system-info.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/instance-administration/server-logs-and-system-info.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/instance-administration/server-logs-and-system-info.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/instance-administration/server-logs-and-system-info.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/instance-administration/server-logs-and-system-info.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/system-functions/server-logs-and-system-info.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/system-functions/server-logs-and-system-info.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/system-functions/server-logs-and-system-info.md

# Server logs and system info

### Viewing your system Info <a href="#system-info" id="system-info"></a>

The **System Info** page is found at **Administration** > **System**. It gives you access to detailed information on the state of your SonarQube Server instance.

You can browse details about your running instance on this page.

#### Downloading your system info <a href="#downloading-your-system-info" id="downloading-your-system-info"></a>

If you have a support contract, you might be asked by a support representative to send in your system info, which can be downloaded using the **Download System Info** button at the top.

### Getting your Server ID <a href="#server-id" id="server-id"></a>

If you want to switch to a paid SonarQube Server edition, you will be asked by your sales representative to send in your Server ID.

Your server ID can be found at the top of the page **Administration** > **System**.

If you’re running a commercial instance, you can also find this value on the **License** page (**Administration** > **Configuration** > **License Manager**)

### Viewing the server logs <a href="#view-server-logs" id="view-server-logs"></a>

See [checking-server-logs](https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/troubleshooting/checking-server-logs "mention").

### Setting up the server-side logging <a href="#set-up-logging" id="set-up-logging"></a>

Server-side logging is controlled by properties set in `<sonarqubeHome>/conf/sonar.properties`. The standard output of SonarQube Server logs can be converted to JSON with the environment variable `SONAR_LOG_JSONOUTPUT=true`. A configuration of the log format is currently not possible.

#### Log level <a href="#log-level" id="log-level"></a>

The server-side log level can be customized via the `sonar.log.level` property in `<sonarqubeHome>/conf/sonar.properties`. Supported values are:

* **`INFO`**: The default.
* **`DEBUG`**: For advanced logs. Starting from this log level, some personal user information can be logged.
* **`TRACE`**: Show advanced logs and all SQL and ElasticSearch requests. `TRACE` level logging slows down the server environment, and should be used only for tracking web request performance problems.

{% hint style="info" %}
You can tune the log level via controls at the top of the page **Administration > System**. Changes made here are temporary, and last only until the next time the instance is restarted, at which point the level will be reset to the more permanent value set in `sonar.properties`. Regardless, if you change your log level *from* `INFO`, be sure to change it back as soon as is practical; log files can get very large very quickly at lower log levels.
{% endhint %}

#### Log level by process <a href="#log-level-by-process" id="log-level-by-process"></a>

The server-side log level can be adjusted more precisely for the four processes of SonarQube Server via the following properties:

* **`sonar.log.level.app`**: for the Main process of SonarQube Server (aka WrapperSimpleApp, the bootstrapper process starting the 3 others)
* **`sonar.log.level.web`**: for the WebServer
* **`sonar.log.level.ce`**: for the ComputeEngineServer
* **`sonar.log.level.es`**: for the SearchServer

#### Log rotation <a href="#log-rotation" id="log-rotation"></a>

To control log rolling, use the `sonar.log.rollingPolicy`.

* **`time:[value]`**: for time-based rotation. For example, use `time:yyyy-MM-dd` for daily rotation, and `time:yyyy-MM` for monthly rotation.
* **`size:[value]`**: for size-based rotation. For example, `size:10MB`.
* **`none`**: for no rotation. Typically this would be used when logs are handled by an external system like logrotate.

`sonar.log.maxFiles` is the maximum number of files to keep. This property is ignored if `sonar.log.rollingPolicy=none`.

### Retrieving the total Lines of Code (LOC) <a href="#total-lines-of-code" id="total-lines-of-code"></a>

The number of [lines-of-code](https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/monitoring/lines-of-code "mention") (for licensing purposes) in an instance can be found in the **System** section of the **System Info** page and on the **License page** (**Administration** > **Configuration** > **License Manager**) in commercial editions.

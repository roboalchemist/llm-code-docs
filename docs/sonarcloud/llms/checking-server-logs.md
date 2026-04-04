# Source: https://docs.sonarsource.com/sonarqube-server/10.8/server-upgrade-and-maintenance/troubleshooting/checking-server-logs.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/troubleshooting/checking-server-logs.md

# Checking the server logs

If you’re having trouble starting your server for the first time (or any subsequent time!) the first thing to do is check your server logs.

The following log files are created (log files rotate on a regular basis):

* One per SonarQube Server process (main process, compute engine, search engine, and web server).
* The access log.
* The deprecation logs which stores the Web API requests that use deprecated Web API endpoints or parameters. See [api-deprecation](https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/monitoring/api-deprecation "mention") for more details.

If you have a support contract, you can download your instance’s current log files from the UI. To do so:

* Go to **Administration > System** and click **Download logs** in the top right corner.

Otherwise, you’ll find them in `<sonarqubeHome>/logs`:

* `sonar.log`: Log for the main process. Holds general information about startup and shutdown. You’ll get overall status here but not details. Look to the other logs for that.
* `web.log`: Information about initial connection to the database, database migration and reindexing, and the processing of HTTP requests. This includes database and search engine logs related to those requests.
* `ce.log`: Information about background task processing and the database and search engine logs related to those tasks.
* `es.log`: Ops information from the search engine, such as Elasticsearch startup, health status changes, cluster-, node- and index-level operations, etc.
* `access.log`: access log.

### Understanding the logs <a href="#understanding-the-logs" id="understanding-the-logs"></a>

When there’s an error, you’ll very often find a stacktrace in the logs. If you’re not familiar stacktraces, they can be intimidatingly tall walls of incomprehensible text. As a sample, here’s a fairly short one:

```css-79elbk
java.lang.IllegalStateException: Unable to blame file **/**/foo.java
    at org.sonarsource.scm.git.JGitBlameCommand.blame(JGitBlameCommand.java:128)
    at org.sonarsource.scm.git.JGitBlameCommand.access$000(JGitBlameCommand.java:44)
    at org.sonarsource.scm.git.JGitBlameCommand$1.call(JGitBlameCommand.java:112)
    at org.sonarsource.scm.git.JGitBlameCommand$1.call(JGitBlameCommand.java:109)
    at java.util.concurrent.FutureTask.run(Unknown Source)
    at java.util.concurrent.ThreadPoolExecutor.runWorker(Unknown Source)
    at java.util.concurrent.ThreadPoolExecutor$Worker.run(Unknown Source)
    at java.lang.Thread.run(Unknown Source)
Caused by: java.lang.NullPointerException
    at org.eclipse.jgit.treewalk.filter.PathFilter.create(PathFilter.java:77)
    at org.eclipse.jgit.blame.BlameGenerator.<init>(BlameGenerator.java:161)
    at org.eclipse.jgit.api.BlameCommand.call(BlameCommand.java:203)
    at org.sonarsource.scm.git.JGitBlameCommand.blame(JGitBlameCommand.java:126)
    ... 7 more
```

Unless you wrote the code that produced this error, you really only care about:

* the first line, which ought to have a human-readable message after the colon. In this case, it’s Unable to blame file `**/**/foo.java`
* and any line that starts with `Caused by`. There are often several `Caused by` lines, and indentation makes them easy to find as you scroll through the error. Be sure to read each of these lines. Very often one of them - the last one or next-to-last one - contains the real problem.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [server-logs-and-system-info](https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/system-functions/server-logs-and-system-info "mention")
* [performance-issues](https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/troubleshooting/performance-issues "mention")
* [database-related-issues](https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/troubleshooting/database-related-issues "mention")
* [elasticsearch](https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/troubleshooting/elasticsearch "mention")
* [other-issues](https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/troubleshooting/other-issues "mention")

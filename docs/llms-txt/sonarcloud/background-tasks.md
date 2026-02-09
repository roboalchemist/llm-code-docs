# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/background-tasks.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/analyzing-source-code/background-tasks.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/analyzing-source-code/background-tasks.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code/background-tasks.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/background-tasks.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/analyzing-source-code/background-tasks.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/analyzing-source-code/background-tasks.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/analyzing-source-code/background-tasks.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/background-tasks.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/background-tasks.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/background-tasks.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/background-tasks.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/background-tasks.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/background-tasks.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/background-tasks.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/background-tasks.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/background-tasks.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/background-tasks.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/background-tasks.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/background-tasks.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/background-tasks.md

# Background tasks

The processing of the scanner results is called a background task. Analysis is not complete until the relevant background task has been completed.

### What happens after the scanner is done analyzing? <a href="#what-happens-after-the-scanner-is-done-analyzing" id="what-happens-after-the-scanner-is-done-analyzing"></a>

Analysis is not complete until the relevant background task has been completed. Even though the SonarScanner’s log shows `EXECUTION SUCCESS`, the analysis results will not be visible in the SonarQube Cloud project until the background task has been completed. After a SonarScanner has finished analyzing your code, the result of the analysis (sources, issues, metrics) - the analysis report - is sent to SonarQube Cloud server for final processing by the compute engine. Analysis reports are queued and processed serially.

At the project level, when there is a pending analysis report waiting to be consumed, you can see a "pending" notification in the header, next to the date of the most recently completed analysis.

Project administrators can see the tasks for a project at **Administration** > **Background Tasks**.

### How do I know when analysis report processing fails? <a href="#how-do-i-know-when-analysis-report-processing-fails" id="how-do-i-know-when-analysis-report-processing-fails"></a>

Background tasks usually succeed, but sometimes unusual circumstances cause processing to fail. Examples include:

* Running out of memory while processing a report from a very large project
* Hitting a clash between the key of an existing module or project and one in the report

If that happens, the failed status displays on the project homepage, but that requires someone to notice it. You can also choose to be notified by email when background tasks fail - either on a project by project basis, or globally, on all projects where you have administration rights in the **Notifications** section of your profile.

### How do I diagnose a failing background task? <a href="#how-do-i-diagnose-a-failing-background-task" id="how-do-i-diagnose-a-failing-background-task"></a>

For each analysis report, there is a dropdown menu allowing you to access the scanner context that shows you the Scanner’s configuration at the moment when the code scan was run.

If processing failed for the task, an additional option is available: "Show Error Details", to get the technical details of why the background task processing failed.

### How do I cancel a pending analysis report? <a href="#how-do-i-cancel-a-pending-analysis-report" id="how-do-i-cancel-a-pending-analysis-report"></a>

Administrators can cancel the processing of a pending task by clicking:

* on the red ‘x’ available on each line of a `pending` task
* on the red "bulk cancel" option next to the pending jobs count. This button cancels all pending tasks.

Once processing has begun on a report, it’s too late to cancel it.

### How long is the history kept for background tasks? <a href="#background-task-history" id="background-task-history"></a>

The history for background tasks is retained for 6 months.

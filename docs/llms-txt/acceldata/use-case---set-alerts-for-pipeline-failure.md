# Source: https://docs.acceldata.io/documentation/use-case---set-alerts-for-pipeline-failure.md

# Set Alerts for Pipeline Failure

## Proactive Alerts for Any Pipeline Failure

**Scenario:** You are the owner of a critical daily pipeline. You need to be notified immediately via Slack and email whenever a pipeline run fails for any reason.

**Goal:** Generate a comprehensive alert for all pipeline failures.

**Steps:**

1. From the **Pipelines** list, click the name of the pipeline you want to monitor.
2. From the ellipsis icon on the left, navigate to the [Control Pipeline](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/control-pipeline) tab.
3. Select [Configure Monitoring Policies](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/control-pipeline).
4. Locate the **Pipeline Execution Failure Settings** section at the top of the page and click **Edit**.
5. Configure the alert details:
    - **Severity**: Set the level to `Critical` to reflect the importance of the pipeline.
    - **Notification Channels:** Select your team's Slack channel and email distribution list from the dropdown.

6. Click **Save**.

**Conclusion:**
The alert rule is now active. Should this pipeline fail in the future, a critical alert will be dispatched instantly to the designated Slack channel and email addresses, facilitating a swift response.

---

## Setting an SLA for a Long-Running Pipeline

**Scenario:** As a pipeline observer, you notice that the pipeline is not failing outright, but its performance is degrading.
To meet the business Service Level Agreement (SLA), the process must be completed within 15 minutes. An alert is required if this threshold is exceeded.

**Goal**: Create a specific alert if the pipeline duration exceeds 15 minutes.

**Steps:**

1. Navigate to the [Configure Monitoring Policies](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/control-pipeline#configure-a-monitoring-policy) screen for your pipeline.
2. Click the **Add Monitoring Policy** button.
3. **Select Metric Type:** Choose `Pipeline` to monitor the overall execution.
4. **Define the Rule:**
    - **Select Metric**: Choose `Pipeline Duration`.
    - **Configure Comparison:** Select `User Threshold` to set a fixed limit.
    - **Configure Threshold:** Set the condition to `Greater Than` and enter `00:15:00`. 
    - **Set Alert Severity:** Set the severity to `High`, as this is a breach of an SLA. 
    - **Select Notification Channel:** Choose the appropriate on-call team channel (e.g., PagerDuty, a specific Slack channel).

5. Click **Save**.

**Conclusion:**

A new ADOC monitoring policy is active: pipeline runs exceeding 15 minutes will trigger a high-severity alert for performance issue investigation.
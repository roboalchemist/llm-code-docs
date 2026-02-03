# Source: https://docs.sonarsource.com/sonarqube-server/8.9/instance-administration/custom-measures.md

# Custom measures

SonarQube collects a maximum of measures in an automated manner but there are some measures for which this is not possible, such as when: the information is not available for collection, the measure is computed by a human, and so on. Whatever the reason, SonarQube provides a service to inject those measures manually and allows you to benefit from other services: the Manual Measures service. The manual measures entered will be picked during the next analysis of the project and thereafter treated as "normal" measures.

### Managing custom metrics <a href="#managing-custom-metrics" id="managing-custom-metrics"></a>

As with measures that are collected automatically, manual measures are the values collected in each analysis for manual metrics. Therefore, the first thing to do is create the metric you want to save your measure against. In order to do so, log in as a system administrator and go to **Administration** > **Configuration** > **Custom Metrics**, where the interface will guide you in creating the metric you need.

### Managing custom measures <a href="#managing-custom-measures" id="managing-custom-measures"></a>

Custom measures can be entered at the project level. To add a measure, sign in as a project administrator, navigate to the desired project and choose **Project Settings** > **Custom Measures**, where you will find a table with the latest measure value entered for each metric.

Values entered in this interface are **Pending**, and will not be visible outside this administrative interface until the next analysis.

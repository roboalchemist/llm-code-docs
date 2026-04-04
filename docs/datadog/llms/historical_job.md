# Source: https://docs.datadoghq.com/security/cloud_siem/detect_and_monitor/custom_detection_rules/create_rule/historical_job.md

---
title: Create a Historical Job
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Cloud SIEM > Detect and Monitor > Custom Detection
  Rules > Create a Custom Rule > Create a Historical Job
---

# Create a Historical Job

## Overview{% #overview %}

Historical jobs are one-time executable queries on historical logs used to backtest detection rules and assess their effectiveness on past data. The generated job results are lightweight versions of signals providing information on potential threats and anomalies on historical logs. After reviewing the results, you can convert results needing immediate action into signals.

## Create a rule{% #create-a-rule %}

1. To create a threshold detection rule or job, navigate to the [Create a New Detection](https://app.datadoghq.com/security/siem/rules/new) page.
1. Select **Historical Job**.

## Define your historical job{% #define-your-historical-job %}

1. Select the logs index and time range for the job.
1. Select the detection method you want to use for creating signals.

## Define search queries{% #define-search-queries %}

{% tab title="Threshold" %}

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/detection_rules/threshold_20250310.5ad2188a658fd5fb9c591f4570f334e3.png?auto=format"
   alt="Define the search query" /%}

1. To search Audit Trail events or events from Events Management, click the down arrow next to **Logs** and select **Audit Trail** or **Events**.

1. Construct a search query for your logs or events using the [Log Explorer search syntax](https://docs.datadoghq.com/logs/search_syntax/).

1. (Optional) In the **Count** dropdown menu, select attributes whose unique values are counted over the specified time frame.

1. (Optional) In the **group by** dropdown menu, select attributes you want to group by.

   - The defined `group by` generates a signal for each `group by` value.
   - Typically, the `group by` is an entity (like user, or IP). The `group by` is also used to join the queries together.
   - Joining logs that span a time frame can increase the confidence or severity of the security signal. For example, to detect a successful brute force attack, both successful and unsuccessful authentication logs must be correlated for a user.

1. (Optional) To create calculated fields that transform your logs during query time:

   1. Click **Add** and select **Calculated fields**.
   1. In **Name your field**, enter a descriptive name that indicates the purpose of the calculated field.
      - For example, if you want to combine users' first and last name into one field, you might name the calculated field `fullName`.
   1. In the **Define your formula** field, enter a formula or expression, which determines the result to be computed and stored as the value of the calculated field for each log event.
      - See [Calculated Fields Expressions Language](https://docs.datadoghq.com/logs/explorer/calculated_fields/expression_language/) for information on syntax and language constructs.

1. (Optional) To filter logs using references tables:

   1. Click the **Add** button next to the query editor and select **Join with Reference Table**.
   1. In the **Inner join with reference table** dropdown menu, select your reference table.
   1. In the **where field** dropdown menu, select the log field to join on.
   1. Select the **IN** or **NOT IN** operator to filter in or filter out matching logs.
   1. In the **column** dropdown menu, select the column of the reference table to join on.

1. (Optional) To test your rules against sample logs, click **Unit Test**.

   1. To construct a sample log, you can:
      1. Navigate to [Log Explorer](https://app.datadoghq.com/logs) in a new window.
      1. In the search bar, enter the query you are using for the detection rule.
   1. Select one of the logs.
   1. Click the export button at the top right side of the log side panel, and then select **Copy**.
   1. Navigate back to the **Unit Test** modal, and then paste the log into the text box. Edit the sample as needed for your use case.
   1. Toggle the switch for **Query is expected to match based on the example event** to fit your use case.
   1. Click **Run Query Test**.

{% /tab %}

{% tab title="New Value" %}

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/detection_rules/new_value_20250310.1481920276a722442fd96535404612d3.png?auto=format"
   alt="Define the search query" /%}

1. To search Audit Trail events or events from Events Management, click the down arrow next to **Logs** and select **Audit Trail** or **Events**.

1. Construct a search query for your logs or events using the [Log Explorer search syntax](https://docs.datadoghq.com/logs/search_syntax/).

1. In the **Detect new value** dropdown menu, select the attributes you want to detect.

   - For example, if you create a query for successful user authentication with the following settings:
     - **Detect new value** is `country`
     - **group by** is `user`
     - Learning duration is `after 7 days`Then, logs coming in over the next 7 days are evaluated with those configured values. If a log comes in with a new value after the learning duration (`7 days`), a signal is generated, and the new value is learned to prevent future signals with this value.
   - You can also identify users and entities using multiple **Detect new value** attributes in a single query.
     - For example, if you want to detect when a user signs in from a new device and from a country that they've never signed in from before, add `device_id` and `country_name` to the **Detect new value** field.

1. (Optional) Define a signal grouping in the **group by** dropdown menu.

   - The defined `group by` generates a signal for each `group by` value.
   - Typically, the `group by` is an entity (like user or IP address).

1. In the dropdown menu to the right of **group by**, select the learning duration.

1. (Optional) Define a signal grouping in the **group by** dropdown menu.

   - The defined `group by` generates a signal for each `group by` value.
   - Typically, the `group by` is an entity (like user or IP address).

1. In the dropdown menu to the right of **group by**, select the learning duration.

1. (Optional) To create calculated fields that transform your logs during query time:

   1. Click **Add** and select **Calculated fields**.
   1. In **Name your field**, enter a descriptive name that indicates the purpose of the calculated field.
      - For example, if you want to combine users' first and last name into one field, you might name the calculated field `fullName`.
   1. In the **Define your formula** field, enter a formula or expression, which determines the result to be computed and stored as the value of the calculated field for each log event.
      - See [Calculated Fields Expressions Language](https://docs.datadoghq.com/logs/explorer/calculated_fields/expression_language/) for information on syntax and language constructs.

1. (Optional) To filter logs using references tables:

   1. Click the **Add** button next to the query editor and select **Join with Reference Table**.
   1. In the **Inner join with reference table** dropdown menu, select your reference table.
   1. In the **where field** dropdown menu, select the log field to join on.
   1. Select the **IN** or **NOT IN** operator to filter in or filter out matching logs.
   1. In the **column** dropdown menu, select the column of the reference table to join on.

1. (Optional) To test your rules against sample logs, click **Unit Test**.

   1. To construct a sample log, you can:
      1. Navigate to [Log Explorer](https://app.datadoghq.com/logs) in a new window.
      1. In the search bar, enter the query you are using for the detection rule.
   1. Select one of the logs.
   1. Click the export button at the top right side of the log side panel, and then select **Copy**.
   1. Navigate back to the **Unit Test** modal, and then paste the log into the text box. Edit the sample as needed for your use case.
   1. Toggle the switch for **Query is expected to match based on the example event** to fit your use case.
   1. Click **Run Query Test**.

{% /tab %}

{% tab title="Anomaly" %}

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/detection_rules/anomaly_query.19923a9476fb314fd203d59d7ea8a3fb.png?auto=format"
   alt="Define the search query" /%}

1. To search Audit Trail events or events from Events Management, click the down arrow next to **Logs** and select **Audit Trail** or **Events**.

1. Construct a search query for your logs or events using the [Log Explorer search syntax](https://docs.datadoghq.com/logs/search_syntax/).

1. (Optional) In the **Count** dropdown menu, select attributes whose unique values you want to count during the specified time frame.

1. (Optional) In the **group by** dropdown menu, select attributes you want to group by.

   - The defined `group by` generates a signal for each `group by` value.
   - Typically, the `group by` is an entity (like user or IP). The `group by` can also join the queries together.
   - Joining logs that span a time frame can increase the confidence or severity of the security signal. For example, if you want to detect a successful brute force attack, both successful and unsuccessful authentication logs must be correlated for a user.
   - Anomaly detection inspects how the `group by` attribute has behaved in the past. If a `group by` attribute is seen for the first time (for example, the first time an IP is communicating with your system) and is anomalous, it does not generate a security signal because the anomaly detection algorithm has no historical data to compare with.

1. (Optional) To create calculated fields that transform your logs during query time:

   1. Click **Add** and select **Calculated fields**.
   1. In **Name your field**, enter a descriptive name that indicates the purpose of the calculated field.
      - For example, if you want to combine users' first and last name into one field, you might name the calculated field `fullName`.
   1. In the **Define your formula** field, enter a formula or expression, which determines the result to be computed and stored as the value of the calculated field for each log event.
      - See [Calculated Fields Expressions Language](https://docs.datadoghq.com/logs/explorer/calculated_fields/expression_language/) for information on syntax and language constructs.

1. (Optional) To filter logs using references tables:

   1. Click the **Add** button next to the query editor and select **Join with Reference Table**.
   1. In the **Inner join with reference table** dropdown menu, select your reference table.
   1. In the **where field** dropdown menu, select the log field to join on.
   1. Select the **IN** or **NOT IN** operator to filter in or filter out matching logs.
   1. In the **column** dropdown menu, select the column of the reference table to join on.

1. (Optional) To test your rules against sample logs, click **Unit Test**.

   1. To construct a sample log, you can:
      1. Navigate to [Log Explorer](https://app.datadoghq.com/logs) in a new window.
      1. In the search bar, enter the query you are using for the detection rule.
   1. Select one of the logs.
   1. Click the export button at the top right side of the log side panel, and then select **Copy**.
   1. Navigate back to the **Unit Test** modal, and then paste the log into the text box. Edit the sample as needed for your use case.
   1. Toggle the switch for **Query is expected to match based on the example event** to fit your use case.
   1. Click **Run Query Test**.

{% /tab %}

{% tab title="Content Anomaly" %}

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/detection_rules/content_anomaly_query.dfd62c07fd232437cb885823e91eb6e4.png?auto=format"
   alt="Define the search query" /%}

1. To search Audit Trail events or events from Events Management, click the down arrow next to **Logs** and select **Audit Trail** or **Events**.

1. Construct a search query for your logs or events using the [Log Explorer search syntax](https://docs.datadoghq.com/logs/search_syntax/).

1. In the **Detect anomaly** field, specify the fields whose values you want to analyze.

1. In the **group by** field, specify the fields you want to group by.

   - The defined `group by` generates a signal for each `group by` value.
   - Typically, the `group by` is an entity (like user or IP). The `group by` can also join the queries together.
   - Joining logs that span a time frame can increase the confidence or severity of the security signal. For example, to detect a successful brute force attack, both successful and unsuccessful authentication logs must be correlated for a user.

1. In the **Learn for** dropdown menu, select the number of days for the learning period. During the learning period, the rule sets a baseline of normal field values and does not generate any signals.

   - **Note**: If the detection rule is modified, the learning period restarts at day `0`.

1. (Optional) To create calculated fields that transform your logs during query time:

   1. Click **Add** and select **Calculated fields**.
   1. In **Name your field**, enter a descriptive name that indicates the purpose of the calculated field.
      - For example, if you want to combine users' first and last name into one field, you might name the calculated field `fullName`.
   1. In the **Define your formula** field, enter a formula or expression, which determines the result to be computed and stored as the value of the calculated field for each log event.
      - See [Calculated Fields Expressions Language](https://docs.datadoghq.com/logs/explorer/calculated_fields/expression_language/) for information on syntax and language constructs.

1. (Optional) To filter logs using references tables:

   1. Click the **Add** button next to the query editor and select **Join with Reference Table**.
   1. In the **Inner join with reference table** dropdown menu, select your reference table.
   1. In the **where field** dropdown menu, select the log field to join on.
   1. Select the **IN** or **NOT IN** operator to filter in or filter out matching logs.
   1. In the **column** dropdown menu, select the column of the reference table to join on.

1. (Optional) To test your rules against sample logs, click **Unit Test**.

   1. To construct a sample log, you can:
      1. Navigate to [Log Explorer](https://app.datadoghq.com/logs) in a new window.
      1. In the search bar, enter the query you are using for the detection rule.
   1. Select one of the logs.
   1. Click the export button at the top right side of the log side panel, and then select **Copy**.
   1. Navigate back to the **Unit Test** modal, and then paste the log into the text box. Edit the sample as needed for your use case.
   1. Toggle the switch for **Query is expected to match based on the example event** to fit your use case.
   1. Click **Run Query Test**.

{% /tab %}

{% tab title="Impossible Travel" %}

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/detection_rules/impossible_travel_query.764df6c2228f9605ccbeb97d45bf64f7.png?auto=format"
   alt="Define the search query" /%}

1. To search Audit Trail events or events from Events Management, click the down arrow next to **Logs** and select **Audit Trail** or **Events**.
1. Construct a search query for your logs or events using the [Log Explorer search syntax](https://docs.datadoghq.com/logs/search_syntax/).
1. In the **User attribute** dropdown menu, select the log attribute that contains the user ID. This can be an identifier like an email address, user name, or account identifier.
1. The **Location attribute** value is automatically set to `@network.client.geoip`.
   - The `location attribute` specifies which field holds the geographic information for a log.
   - The only supported value is `@network.client.geoip`, which is enriched by the [GeoIP parser](https://docs.datadoghq.com/logs/log_configuration/processors/?tab=ui#geoip-parser) to give a log location information based on the client's IP address.
1. Click the **Baseline user locations** checkbox if you want Datadog to learn regular access locations before triggering a signal.
   - When selected, signals are suppressed for the first 24 hours. During that time, Datadog learns the user's regular access locations. This can be helpful to reduce noise and infer VPN usage or credentialed API access.
   - See [How the impossible detection method works](https://docs.datadoghq.com/security/cloud_siem/detect_and_monitor/custom_detection_rules/impossible_travel/#how-the-impossible-travel-method-works) for more information.

1. (Optional) To create calculated fields that transform your logs during query time:

   1. Click **Add** and select **Calculated fields**.
   1. In **Name your field**, enter a descriptive name that indicates the purpose of the calculated field.
      - For example, if you want to combine users' first and last name into one field, you might name the calculated field `fullName`.
   1. In the **Define your formula** field, enter a formula or expression, which determines the result to be computed and stored as the value of the calculated field for each log event.
      - See [Calculated Fields Expressions Language](https://docs.datadoghq.com/logs/explorer/calculated_fields/expression_language/) for information on syntax and language constructs.

1. (Optional) To filter logs using references tables:

   1. Click the **Add** button next to the query editor and select **Join with Reference Table**.
   1. In the **Inner join with reference table** dropdown menu, select your reference table.
   1. In the **where field** dropdown menu, select the log field to join on.
   1. Select the **IN** or **NOT IN** operator to filter in or filter out matching logs.
   1. In the **column** dropdown menu, select the column of the reference table to join on.

1. (Optional) To test your rules against sample logs, click **Unit Test**.

   1. To construct a sample log, you can:
      1. Navigate to [Log Explorer](https://app.datadoghq.com/logs) in a new window.
      1. In the search bar, enter the query you are using for the detection rule.
   1. Select one of the logs.
   1. Click the export button at the top right side of the log side panel, and then select **Copy**.
   1. Navigate back to the **Unit Test** modal, and then paste the log into the text box. Edit the sample as needed for your use case.
   1. Toggle the switch for **Query is expected to match based on the example event** to fit your use case.
   1. Click **Run Query Test**.

**Note**: All logs and events matching this query are analyzed for a potential impossible travel.
{% /tab %}

{% tab title="Third Party" %}

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/detection_rules/third_party_query.ef079282a8c45974ca85c18334547cf8.png?auto=format"
   alt="Define the search query" /%}

1. To search Audit Trail events or events from Events Management, click the down arrow next to **Logs** and select **Audit Trail** or **Events**.

1. Construct a root query for your logs or events using the [Log Explorer search syntax](https://docs.datadoghq.com/logs/search_syntax/).

1. In the **Trigger for each new** dropdown menu, select the attributes where each attribute generates a signal for each new attribute value over 24-hour roll-up period.

1. (Optional) To create calculated fields that transform your logs during query time:

   1. Click **Add** and select **Calculated fields**.
   1. In **Name your field**, enter a descriptive name that indicates the purpose of the calculated field.
      - For example, if you want to combine users' first and last name into one field, you might name the calculated field `fullName`.
   1. In the **Define your formula** field, enter a formula or expression, which determines the result to be computed and stored as the value of the calculated field for each log event.
      - See [Calculated Fields Expressions Language](https://docs.datadoghq.com/logs/explorer/calculated_fields/expression_language/) for information on syntax and language constructs.

   - See [Calculated Fields Expressions Language][3] for information on syntax and language constructs.

1. (Optional) To create calculated fields that transform your logs during query time:

   1. Click **Add** and select **Calculated fields**.
   1. In **Name your field**, enter a descriptive name that indicates the purpose of the calculated field.
      - For example, if you want to combine users' first and last name into one field, you might name the calculated field `fullName`.
   1. In the **Define your formula** field, enter a formula or expression, which determines the result to be computed and stored as the value of the calculated field for each log event.
      - See [Calculated Fields Expressions Language](https://docs.datadoghq.com/logs/explorer/calculated_fields/expression_language/) for information on syntax and language constructs.

1. (Optional) To filter logs using references tables:

   1. Click the **Add** button next to the query editor and select **Join with Reference Table**.
   1. In the **Inner join with reference table** dropdown menu, select your reference table.
   1. In the **where field** dropdown menu, select the log field to join on.
   1. Select the **IN** or **NOT IN** operator to filter in or filter out matching logs.
   1. In the **column** dropdown menu, select the column of the reference table to join on.

1. (Optional) To test your rules against sample logs, click **Unit Test**.

   1. To construct a sample log, you can:
      1. Navigate to [Log Explorer](https://app.datadoghq.com/logs) in a new window.
      1. In the search bar, enter the query you are using for the detection rule.
   1. Select one of the logs.
   1. Click the export button at the top right side of the log side panel, and then select **Copy**.
   1. Navigate back to the **Unit Test** modal, and then paste the log into the text box. Edit the sample as needed for your use case.
   1. Toggle the switch for **Query is expected to match based on the example event** to fit your use case.
   1. Click **Run Query Test**.

Click **Add Root Query** to add additional queries.
{% /tab %}

## Set conditions{% #set-conditions %}

{% tab title="Threshold" %}

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/detection_rules/threshold_historical_condition.96e975107a46b8695ee7e475cd9be018.png?auto=format"
   alt="Set your conditions, severity, and notification recipients" /%}

1. If you have a single query, skip to step 2. If you have multiple queries, you can create a **Simple condition** or **Then condition**.
   - If you want to create a simple condition, leave the selection as is.
   - If you want to create a `then` condition, click **THEN condition**.
     - Use the **Then condition** when you want to trigger a signal if query A occurs and then query B occurs.
     - **Note**: The `then` operator can only be used on a single rule condition.
1. (Optional) Click the pencil icon next to **Condition 1** if you want to rename the condition. This name is appended to the rule name when a signal is generated.
1. In the **Set severity to** dropdown menu, select the appropriate severity level (`INFO`, `LOW`, `MEDIUM`, `HIGH`, `CRITICAL`).
1. If you are creating a **Simple condition**, enter the condition when a signal should be created. If you are creating a **Then condition**, enter the conditions required for a signal to be generated.
   - All rule conditions are evaluated as condition statements. Thus, the order of the conditions affects which notifications are sent because the first condition to match generates the signal. Click and drag your rule conditions to change their order.
   - A rule condition contains logical operations (`>`, `>=`, `<`, `&&`, `||`) to determine if a signal should be generated based on the event counts in the previously defined queries.
   - The ASCII lowercase query labels are referenced in this section. An example rule condition for query `a` is `a > 3`.
   - **Note**: The query label must precede the operator. For example, `a > 3` is allowed; `3 < a` is not allowed.
1. (Optional) In the **Add notify** section, click **Add Recipient** to configure [notification targets](https://docs.datadoghq.com/security_platform/notifications/#notification-channels).
   - You can also create [notification rules](https://docs.datadoghq.com/security/notifications/rules/) to avoid manual edits to notification preferences for individual detection rules.

### Other parameters{% #other-parameters %}

#### 1. Job multi-triggering{% #job-multi-triggering-threshold %}

In the **Job multi-triggering behavior** section, configure how often to keep updating the same signal when new values are detected within a specified time frame. For example, the same signal updates when any new value is detected within 1 hour, for a maximum duration of 24 hours.

- An `evaluation window` defines a sliding period in which at least one case evaluates as true and assesses cases in real time.
- After a signal is generated, the signal remains "open" if a case is matched at least once within the `keep alive` window. Each time a new event matches any of the cases, the *last updated* timestamp is updated for the signal.
- A signal closes after the time exceeds the `maximum signal duration`, regardless of the query being matched. This time is calculated from the first seen timestamp.
- **Note**: The `evaluation window` must be less than or equal to the `keep alive` and `maximum signal duration`.

#### 2. Enable optional group by{% #enable-group-by-historical-threshold %}

Toggle **Enable Optional Group By** section if you want to group events even when values are missing. If there is a missing value, a sample value is generated so that the log does not get excluded.
{% /tab %}

{% tab title="New Value" %}
### Other parameters{% #other-parameters %}

#### 1. Forget value{% #forget-value-historical-new-value %}

In the **Forget Value** dropdown, select the number of days (**1**-**30 days**) after which the value is forgotten.

#### 2. Job multi-triggering behavior{% #job-multi-triggering-historical-new-value %}

In the **Job multi-triggering behavior** section, configure how often to keep updating the same signal when new values are detected within a specified time frame. For example, the same signal updates when any new value is detected within 1 hour, for a maximum duration of 24 hours.

- An `evaluation window` defines a sliding period in which at least one case evaluates as true and assesses cases in real time.
- After a signal is generated, the signal remains "open" if a case is matched at least once within the `keep alive` window. Each time a new event matches any of the cases, the *last updated* timestamp is updated for the signal.
- A signal closes after the time exceeds the `maximum signal duration`, regardless of the query being matched. This time is calculated from the first seen timestamp.
- **Note**: The `evaluation window` must be less than or equal to the `keep alive` and `maximum signal duration`.

#### 3. Enable optional group by{% #enable-group-by-historical-new-value %}

Toggle **Enable Optional Group By** section if you want to group events even when values are missing. If there is a missing value, a sample value is generated so that the log does not get excluded.

#### 4. Enable instantaneous baseline

Toggle **Enable instantaneous baseline** if you want to build the baseline based on past events for the first event received.
{% /tab %}

{% tab title="Anomaly" %}
### Other parameters{% #other-parameters %}

#### 1. Job multi-triggering{% #job-multi-triggering-historical-anomaly %}

In the **Job multi-triggering behavior** section, configure how often to keep updating the same signal when new values are detected within a specified time frame. For example, the same signal updates when any new value is detected within 1 hour, for a maximum duration of 24 hours.

- An `evaluation window` defines a sliding period in which at least one case evaluates as true and assesses cases in real time.
- After a signal is generated, the signal remains "open" if a case is matched at least once within the `keep alive` window. Each time a new event matches any of the cases, the *last updated* timestamp is updated for the signal.
- A signal closes after the time exceeds the `maximum signal duration`, regardless of the query being matched. This time is calculated from the first seen timestamp.
- **Note**: The `evaluation window` must be less than or equal to the `keep alive` and `maximum signal duration`.

#### 2. Enable optional group by{% #enable-group-by-historical-anomaly %}

Toggle **Enable Optional Group By** section if you want to group events even when values are missing. If there is a missing value, a sample value is generated so that the log does not get excluded.
{% /tab %}

{% tab title="Content Anomaly" %}

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/detection_rules/content_anomaly_historical_condition.077c309ecc300edf8b9123d0340551a1.png?auto=format"
   alt="Set your condition, severity, and notification recipients" /%}

1. (Optional) Click the pencil icon next to **Condition 1** if you want to rename the condition. This name is appended to the rule name when a signal is generated.
1. In the **Anomaly count** field, enter the condition for how many anomalous logs within the specified window are required to trigger a signal.
   - For example, if the condition is `a >= 3` where `a` is the query, a signal is triggered if there are at least three anomalous logs within the evaluation window.
   - All rule conditions are evaluated as condition statements. Thus, the order of the conditions affects which notifications are sent because the first condition to match generates the signal. Click and drag your rule conditions to change their ordering.
   - A rule condition contains logical operations (`>`, `>=`, `&&`, `||`) to determine if a signal should be generated based on the event counts in the previously defined queries.
   - The ASCII lowercase query labels are referenced in this section. An example rule condition for query `a` is `a > 3`.
   - **Note**: The query label must precede the operator. For example, `a > 3` is allowed; `3 < a` is not allowed.
1. In the **within a window of** dropdown menu, select the time period during which a signal is triggered if the condition is met.
   - An `evaluation window` is specified to match when at least one of the cases matches true. This is a sliding window and evaluates cases in real time.

### Other parameters{% #other-parameters %}

#### 1. Content anomaly detection{% #content-anomaly-historical-content-anomaly %}

In the **Content anomaly detection options** section, specify the parameters to assess whether a log is anomalous or not.

- Content anomaly detection balances precision and sensitivity using several rule parameters that you can set:
  1. Similarity threshold: Defines how dissimilar a field value must be to be considered anomalous (default: `70%`).
  1. Minimum similar items: Sets how many similar historical logs must exist for a value to be considered normal (default: `1`).
  1. Evaluation window: The time frame during which anomalies are counted toward a signal (for example, a 10-minute time frame).
- These parameters help to identify field content that is both unusual and rare, filtering out minor or common variations.
- See [Anomaly detection parameters](https://docs.datadoghq.com/security/cloud_siem/detect_and_monitor/custom_detection_rules/content_anomaly/#anomaly-detection-parameters) for more information.

#### 2. Job multi-triggering behavior{% #job-multi-triggering-historical-content-anomaly %}

Configure how often you want to keep updating the same signal if new values are detected within a specified time frame. For example, the same signal updates if any new value is detected within 1 hour, for a maximum duration of 24 hours.

- After a signal is generated, the signal remains "open" if a case is matched at least once within the `keep alive` window. Each time a new event matches any of the cases, the *last updated* timestamp is updated for the signal.
- A signal closes after the time exceeds the `maximum signal duration`, regardless of the query being matched. This time is calculated from the first seen timestamp.
- **Note**: The `evaluation window` must be less than or equal to the `keep alive` and `maximum signal duration`.

#### 3. Enable optional group by{% #enable-group-by-historical-content-anomaly %}

Toggle **Enable Optional Group By** section if you want to group events even when values are missing. If there is a missing value, a sample value is generated so that the log does not get excluded.
{% /tab %}

{% tab title="Impossible Travel" %}
### Other parameters{% #other-parameters %}

#### 1. Job multi-triggering{% #job-multi-triggering-historical-anomaly %}

In the **Job multi-triggering behavior** section, configure how often to keep updating the same signal when new values are detected within a specified time frame. For example, the same signal updates when any new value is detected within 1 hour, for a maximum duration of 24 hours.

- An `evaluation window` defines a sliding period in which at least one case evaluates as true and assesses cases in real time.
- After a signal is generated, the signal remains "open" if a case is matched at least once within the `keep alive` window. Each time a new event matches any of the cases, the *last updated* timestamp is updated for the signal.
- A signal closes after the time exceeds the `maximum signal duration`, regardless of the query being matched. This time is calculated from the first seen timestamp.
- **Note**: The `evaluation window` must be less than or equal to the `keep alive` and `maximum signal duration`.

#### 2. Enable optional group by{% #enable-group-by-historical-anomaly %}

Toggle **Enable Optional Group By** section if you want to group events even when values are missing. If there is a missing value, a sample value is generated so that the log does not get excluded.
{% /tab %}

{% tab title="Third Party" %}

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/detection_rules/set_condition_root_query.93eb4c01b6f336e0e14c9a6c33194010.png?auto=format"
   alt="Set your conditions, severity, and notification recipients" /%}

1. (Optional) Click the pencil icon next to **Condition 1** if you want to rename the condition. This name is appended to the rule name when a signal is generated.
1. In the **Query** field, enter the tags of a log that you want to trigger a signal.
   - For example, if you want logs with the tag `dev:demo` to trigger signals with a severity of `INFO`, enter `dev:demo` in the query field. Similarly, if you want logs with the tag `dev:prod` to trigger signals with a severity of `MEDIUM`, enter `dev:prod` in the query field.

### Other parameters{% #other-parameters %}

Toggle **Enable Optional Group By** section if you want to group events even when values are missing. If there is a missing value, a sample value is generated so that the log does not get excluded.
{% /tab %}

## Notify when job is complete{% #notify-when-job-is-complete %}

(Optional) Click **Add Recipient** to send notifications upon the completion of job analysis. See [Notification channels](https://docs.datadoghq.com/security_platform/notifications/#notification-channels) for more information.

## Describe your playbook{% #describe-your-playbook %}

1. Enter a **Rule name**. The name appears in the detection rules list view and the title of the security signal.
1. In the **Rule message** section, use [notification variables](https://docs.datadoghq.com/security_platform/notifications/variables/) and Markdown to customize the notifications sent when a signal is generated.
   - You can use [template variables](https://docs.datadoghq.com/security_platform/notifications/variables/#template-variables) in the notification to inject dynamic context from triggered logs directly into a security signal and its associated notifications.
   - See the [Notification Variables documentation](https://docs.datadoghq.com/security_platform/notifications/variables/) for more information and examples.
1. Use the **Tag resulting signals** dropdown menu to add tags to your signals. For example, `security:attack` or `technique:T1110-brute-force`.
   - **Note**: the tag `security` is special. This tag is used to classify the security signal. The recommended options are: `attack`, `threat-intel`, `compliance`, `anomaly`, and `data-leak`.

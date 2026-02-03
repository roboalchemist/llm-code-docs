# Source: https://docs.datadoghq.com/security/cloud_siem/detect_and_monitor/custom_detection_rules/create_rule/real_time_rule.md

---
title: Create a Real-Time Rule
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Cloud SIEM > Detect and Monitor > Custom Detection
  Rules > Create a Custom Rule > Create a Real-Time Rule
---

# Create a Real-Time Rule

## Overview{% #overview %}

Real-time detection rules continuously monitors and analyzes incoming logs for security threats. These rules trigger immediate alerts when specific patterns or anomalies are detected, enabling quicker response to potential incidents.

## Create a rule{% #create-a-rule %}

1. To create a detection rule, navigate to the [Create a New Detection](https://app.datadoghq.com/security/siem/rules/new) page.
1. Select **Real-Time Rule**.

## Define your real-time rule{% #define-your-real-time-rule %}

Select the detection method you want to use for creating signals.

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

1. (Optional) In the **Count** dropdown menu, select attributes whose unique values you want to count during the specified time frame.

1. (Optional) In the **group by** dropdown menu, select attributes you want to group by.

   - The defined `group by` generates a signal for each `group by` value.
   - Typically, the `group by` is an entity (like user or IP). The `group by` can also join the queries together.
   - Joining logs that span a time frame can increase the confidence or severity of the security signal. For example, if you want to detect a successful brute force attack, both successful and unsuccessful authentication logs must be correlated for a user.
   - Anomaly detection inspects how the `group by` attribute has behaved in the past. If a `group by` attribute is seen for the first time (for example, the first time an IP is communicating with your system) and is anomalous, it does not generate a security signal because the anomaly detection algorithm has no historical data to compare with.

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

{% tab title="Signal Correlation" %}

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/detection_rules/signal_correlation_query.59a0beeac3db5594e5dbd8e945444cda.png?auto=format"
   alt="Define the search query" /%}

1. Select a rule for **Rule a**.
1. Click the pencil icon to rename the rule.
1. Use the **correlated by** dropdown to define the correlating attribute.
   - You can select multiple attributes (maximum of 3) to correlate the selected rules.
1. Select a rule for **Rule b** in the second Rule editor's dropdown.
   - The attributes and sliding window time frame is automatically set to what was selected for **Rule a**.
1. Click the pencil icon to rename the rule.

{% /tab %}

{% tab title="Sequence" %}

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/detection_rules/sequence/sequence_queries.45e05b16842f0b49425697f5db45de45.png?auto=format"
   alt="Sequence editor page showing the sequence with two steps" /%}

#### Add step{% #add-step %}

1. To search a different data type, click the down arrow next to **Logs** and select **Signals** or **Rules**.
1. Define the condition for the step.
   - **Logs**: Construct a search query using the [Log Explorer search syntax](https://docs.datadoghq.com/logs/search_syntax/).
   - **Signals**: Reference an existing rule or query on signal fields.
   - **Rules**: Select a rule.
1. Set **group by** fields (for example, `@usr.email` or `@ip.address`) to link entities across steps.
1. Enter a threshold condition, such as `>10`.
1. If you want to use another query, connect this query with the next query using `AND` or `OR` and repeat steps 1-4.
1. In the **roll-up over** dropdown menu, select the time frame all queries in that step must occur to transition to the next step.

#### Define step transitions{% #define-step-transitions %}

For the current step and the next step:

1. In the **within** dropdown menu, select an evaluation window for the transition.
   - **Note**: The total evaluation time across the sequence can be up to 24 hours.
1. Follow the instructions in Add step to complete the step.
   - **Note**: You can select different `group by` fields between steps. For example, link `@usr.email`from an earlier step to `@ip.address` in a later step.
1. Click **Add Step** if you want to add more steps.

#### Severity and notification{% #severity-and-notification %}

1. In the **Trigger** dropdown menu, select the severity status.
1. (Optional) In the **Add notify** section, click **Add Recipient** to configure [notification targets](https://docs.datadoghq.com/security_platform/notifications/#notification-channels).
   - You can create [notification rules](https://docs.datadoghq.com/security/notifications/rules/) to manage notifications automatically, avoiding manual edits for each detection rule.

#### Review the sequence preview{% #review-the-sequence-preview %}

In the **Preview detection** section, check the steps, transitions, and time window in the visualization of the steps. Reorder the steps and adjust time windows as needed.
{% /tab %}

## Set conditions{% #set-conditions %}

{% tab title="Threshold" %}

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/detection_rules/condition_simple_then.f6b444aa6c435356bc58e5f73180dd8b.png?auto=format"
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

#### 1. Rule multi-triggering{% #rule-multi-triggering-rt-threshold %}

Configure how often you want to keep updating the same signal if new values are detected within a specified time frame. For example, the same signal updates if any new value is detected within 1 hour, for a maximum duration of 24 hours.

- An `evaluation window` is specified to match when at least one of the cases matches true. This is a sliding window and evaluates cases in real time.
- After a signal is generated, the signal remains "open" if a case is matched at least once within the `keep alive` window. Each time a new event matches any of the cases, the *last updated* timestamp is updated for the signal.
- A signal closes after the time exceeds the `maximum signal duration`, regardless of the query being matched. This time is calculated from the first seen timestamp.
- **Note**: The `evaluation window` must be less than or equal to the `keep alive` and `maximum signal duration`.

#### 2. Decrease severity for non-production environments{% #decrease-severity-rt-threshold %}

Toggle **Decrease severity for non-production environments** if you want to prioritize production environment signals over non-production signals.

- The severity of signals in non-production environments are decreased by one level from what is defined by the rule case.
- The severity decrement is applied to signals with an environment tag starting with `staging`, `test`, or `dev`.

#### 3. Enable optional group by{% #enable-group-by-rt-threshold %}

Toggle **Enable Optional Group By** section if you want to group events even when values are missing. If there is a missing value, a sample value is generated so that the log does not get excluded.
{% /tab %}

{% tab title="New Value" %}

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/detection_rules/severity_notification.e8bbde3d25eac5442ab806986df2c96f.png?auto=format"
   alt="Set your severity and notification recipients" /%}

1. In the **Set severity to** dropdown menu, select the appropriate severity level (`INFO`, `LOW`, `MEDIUM`, `HIGH`, `CRITICAL`).
1. (Optional) In the **Add notify** section, click **Add Recipient** to configure [notification targets](https://docs.datadoghq.com/security_platform/notifications/#notification-channels).
   - You can create [notification rules](https://docs.datadoghq.com/security/notifications/rules/) to manage notifications automatically, avoiding manual edits for each detection rule.

### Other parameters{% #other-parameters %}

#### 1. Forget value{% #forget-value-rt-new-value %}

In the **Forget Value** dropdown, select the number of days (**1**-**30 days**) after which the value is forgotten.

#### 2. Rule multi-triggering behavior{% #rule-multi-triggering-rt-new-value %}

Configure how often you want to keep updating the same signal if new values are detected within a specified time frame. For example, the same signal updates if any new value is detected within 1 hour, for a maximum duration of 24 hours.

- An `evaluation window` is specified to match when at least one of the cases matches true. This is a sliding window and evaluates cases in real time.
- After a signal is generated, the signal remains "open" if a case is matched at least once within the `keep alive` window. Each time a new event matches any of the cases, the *last updated* timestamp is updated for the signal.
- A signal closes after the time exceeds the `maximum signal duration`, regardless of the query being matched. This time is calculated from the first seen timestamp.
- **Note**: The `evaluation window` must be less than or equal to the `keep alive` and `maximum signal duration`.

#### 3. Decrease severity for non-production environments{% #decrease-severity-new-value %}

Toggle **Decrease severity for non-production environments** if you want to prioritize production environment signals over non-production signals.

- The severity of signals in non-production environments are decreased by one level from what is defined by the rule case.
- The severity decrement is applied to signals with an environment tag starting with `staging`, `test`, or `dev`.

#### 4. Enable optional group by{% #enable-group-by-rt-new-value %}

Toggle **Enable Optional Group By** section if you want to group events even when values are missing. If there is a missing value, a sample value is generated so that the log does not get excluded.
{% /tab %}

{% tab title="Anomaly" %}

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/detection_rules/severity_notification.e8bbde3d25eac5442ab806986df2c96f.png?auto=format"
   alt="Set your severity and notification recipients" /%}

1. In the **Set severity to** dropdown menu, select the appropriate severity level (`INFO`, `LOW`, `MEDIUM`, `HIGH`, `CRITICAL`).
1. (Optional) In the **Add notify** section, click **Add Recipient** to configure [notification targets](https://docs.datadoghq.com/security_platform/notifications/#notification-channels).
   - You can create [notification rules](https://docs.datadoghq.com/security/notifications/rules/) to manage notifications automatically, avoiding manual edits for each detection rule.

### Other parameters{% #other-parameters %}

#### 1. Rule multi-triggering{% #rule-multi-triggering-rt-anomaly %}

Configure how often you want to keep updating the same signal if new values are detected within a specified time frame. For example, the same signal updates if any new value is detected within 1 hour, for a maximum duration of 24 hours.

- An `evaluation window` is specified to match when at least one of the cases matches true. This is a sliding window and evaluates cases in real time.
- After a signal is generated, the signal remains "open" if a case is matched at least once within the `keep alive` window. Each time a new event matches any of the cases, the *last updated* timestamp is updated for the signal.
- A signal closes after the time exceeds the `maximum signal duration`, regardless of the query being matched. This time is calculated from the first seen timestamp.
- **Note**: The `evaluation window` must be less than or equal to the `keep alive` and `maximum signal duration`.

#### 2. Decrease severity for non-production environments{% #decrease-severity-rt-anomaly %}

Toggle **Decrease severity for non-production environments** if you want to prioritize production environment signals over non-production signals.

- The severity of signals in non-production environments are decreased by one level from what is defined by the rule case.
- The severity decrement is applied to signals with an environment tag starting with `staging`, `test`, or `dev`.

#### 3. Enable optional group by{% #enable-group-by-rt-anomaly %}

Toggle **Enable Optional Group By** section if you want to group events even when values are missing. If there is a missing value, a sample value is generated so that the log does not get excluded.
{% /tab %}

{% tab title="Content Anomaly" %}

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/detection_rules/condition_content_anomaly.0c9944113fa88417e4fdb2425c4210da.png?auto=format"
   alt="Set your condition, severity, and notification recipients" /%}

1. (Optional) Click the pencil icon next to **Condition 1** if you want to rename the condition. This name is appended to the rule name when a signal is generated.
1. In the **Set severity to** dropdown menu, select the appropriate severity level (`INFO`, `LOW`, `MEDIUM`, `HIGH`, `CRITICAL`).
1. In the **Anomaly count** field, enter the condition for how many anomalous logs within the specified window are required to trigger a signal.
   - For example, if the condition is `a >= 3` where `a` is the query, a signal is triggered if there are at least three anomalous logs within the evaluation window.
   - All rule conditions are evaluated as condition statements. Thus, the order of the conditions affects which notifications are sent because the first condition to match generates the signal. Click and drag your rule conditions to change their ordering.
   - A rule condition contains logical operations (`>`, `>=`, `&&`, `||`) to determine if a signal should be generated based on the event counts in the previously defined queries.
   - The ASCII lowercase query labels are referenced in this section. An example rule condition for query `a` is `a > 3`.
   - **Note**: The query label must precede the operator. For example, `a > 3` is allowed; `3 < a` is not allowed.
1. In the **within a window of** dropdown menu, select the time period during which a signal is triggered if the condition is met.
   - An `evaluation window` is specified to match when at least one of the cases matches true. This is a sliding window and evaluates cases in real time.
1. In the **Add notify** section, click **Add Recipient** to optionally configure [notification targets](https://docs.datadoghq.com/security_platform/notifications/#notification-channels).
   - You can also create [notification rules](https://docs.datadoghq.com/security/notifications/rules/) to avoid manual edits to notification preferences for individual detection rules.

### Other parameters{% #other-parameters %}

#### 1. Content anomaly detection{% #content-anomaly-rt-content-anomaly %}

In the **Content anomaly detection options** section, specify the parameters to assess whether a log is anomalous or not.

- Content anomaly detection balances precision and sensitivity using several rule parameters that you can set:
  1. Similarity threshold: Defines how dissimilar a field value must be to be considered anomalous (default: `70%`).
  1. Minimum similar items: Sets how many similar historical logs must exist for a value to be considered normal (default: `1`).
  1. Evaluation window: The time frame during which anomalies are counted toward a signal (for example, a 10-minute time frame).
- These parameters help to identify field content that is both unusual and rare, filtering out minor or common variations.
- See [Anomaly detection parameters](https://docs.datadoghq.com/security/cloud_siem/detect_and_monitor/custom_detection_rules/content_anomaly/#anomaly-detection-parameters) for more information.

#### 2. Rule multi-triggering behavior{% #rule-multi-triggering-rt-content-anomaly %}

Configure how often you want to keep updating the same signal if new values are detected within a specified time frame. For example, the same signal updates if any new value is detected within 1 hour, for a maximum duration of 24 hours.

- After a signal is generated, the signal remains "open" if a case is matched at least once within the `keep alive` window. Each time a new event matches any of the cases, the *last updated* timestamp is updated for the signal.
- A signal closes after the time exceeds the `maximum signal duration`, regardless of the query being matched. This time is calculated from the first seen timestamp.
- **Note**: The `evaluation window` must be less than or equal to the `keep alive` and `maximum signal duration`.

#### 3. Decrease severity for non-production environments{% #decrease-severity-rt-content-anomaly %}

Toggle **Decrease severity for non-production environments** if you want to prioritize production environment signals over non-production signals.

- The severity of signals in non-production environments are decreased by one level from what is defined by the rule case.
- The severity decrement is applied to signals with an environment tag starting with `staging`, `test`, or `dev`.

#### 4. Enable optional group by{% #enable-group-by-rt-content-anomaly %}

Toggle **Enable Optional Group By** section if you want to group events even when values are missing. If there is a missing value, a sample value is generated so that the log does not get excluded.
{% /tab %}

{% tab title="Impossible Travel" %}

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/detection_rules/severity_notification.e8bbde3d25eac5442ab806986df2c96f.png?auto=format"
   alt="Set your severity and notification recipients" /%}

1. In the **Set severity to** dropdown menu, select the appropriate severity level (`INFO`, `LOW`, `MEDIUM`, `HIGH`, `CRITICAL`).
1. (Optional) In the **Add notify** section, click **Add Recipient** to configure [notification targets](https://docs.datadoghq.com/security_platform/notifications/#notification-channels).
   - You can create [notification rules](https://docs.datadoghq.com/security/notifications/rules/) to manage notifications automatically, avoiding manual edits for each detection rule.

### Other parameters{% #other-parameters %}

#### 1. Rule multi-triggering{% #rule-multi-triggering-rt-impossible-travel %}

Configure how often you want to keep updating the same signal if new values are detected within a specified time frame. For example, the same signal updates if any new value is detected within 1 hour, for a maximum duration of 24 hours.

- An `evaluation window` is specified to match when at least one of the cases matches true. This is a sliding window and evaluates cases in real time.
- After a signal is generated, the signal remains "open" if a case is matched at least once within the `keep alive` window. Each time a new event matches any of the cases, the *last updated* timestamp is updated for the signal.
- A signal closes after the time exceeds the `maximum signal duration`, regardless of the query being matched. This time is calculated from the first seen timestamp.
- **Note**: The `evaluation window` must be less than or equal to the `keep alive` and `maximum signal duration`.

#### 2. Decrease severity for non-production environments{% #decrease-severity-rt-impossible-travel %}

Toggle **Decrease severity for non-production environments** if you want to prioritize production environment signals over non-production signals.

- The severity of signals in non-production environments are decreased by one level from what is defined by the rule case.
- The severity decrement is applied to signals with an environment tag starting with `staging`, `test`, or `dev`.

#### 3. Enable optional group by{% #enable-group-by-rt-impossible-travel %}

Toggle **Enable Optional Group By** section if you want to group events even when values are missing. If there is a missing value, a sample value is generated so that the log does not get excluded.
{% /tab %}

{% tab title="Third Party" %}

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/detection_rules/condition_else.b7196e7931f3562be1d01fc5eadb83be.png?auto=format"
   alt="Set your conditions, severity, and notification recipients" /%}

1. (Optional) Click the pencil icon next to **Condition 1** if you want to rename the condition. This name is appended to the rule name when a signal is generated.
1. In the **Set severity to** dropdown menu, select the appropriate severity level (`INFO`, `LOW`, `MEDIUM`, `HIGH`, `CRITICAL`).
1. In the **Query** field, enter the tags of a log that you want to trigger a signal.
   - For example, if you want logs with the tag `dev:demo` to trigger signals with a severity of `INFO`, enter `dev:demo` in the query field. Similarly, if you want logs with the tag `dev:prod` to trigger signals with a severity of `MEDIUM`, enter `dev:prod` in the query field.
1. (Optional) In the **Add notify** section, click **Add Recipient** to configure [notification targets](https://docs.datadoghq.com/security_platform/notifications/#notification-channels).
   - You can also create [notification rules](https://docs.datadoghq.com/security/notifications/rules/) to avoid manual edits to notification preferences for individual detection rules.
1. For the `else` condition, follow steps 3 and 4.
   - The `else` condition is the default condition. If you don't add any other conditions, then all logs trigger a signal with the severity set in the default condition.

### Other parameters{% #other-parameters %}

#### 1. Decrease severity for non-production environments{% #decrease-severity-rt-third-party %}

Toggle **Decrease severity for non-production environments** if you want to prioritize production environment signals over non-production signals.

- The severity of signals in non-production environments are decreased by one level from what is defined by the rule case.
- The severity decrement is applied to signals with an environment tag starting with `staging`, `test`, or `dev`.

#### 2. Enable optional group by{% #enable-group-by-rt-third-party %}

Toggle **Enable Optional Group By** section if you want to group events even when values are missing. If there is a missing value, a sample value is generated so that the log does not get excluded.
{% /tab %}

{% tab title="Signal Correlation" %}

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/detection_rules/condition_simple_then.f6b444aa6c435356bc58e5f73180dd8b.png?auto=format"
   alt="Set your conditions, severity, and notification recipients" /%}

1. If you want to create a simple condition, leave the selection as is. If you want to create a `then` condition, click **THEN condition**.
   - Use the **Then condition** when you want to trigger a signal if query A occurs and then query B occurs.
   - **Note**: The `then` operator can only be used on a single rule condition.
1. (Optional) Click the pencil icon next to **Condition 1** if you want to rename the condition. This name is appended to the rule name when a signal is generated.
1. In the **Set severity to** dropdown menu, select the appropriate severity level (`INFO`, `LOW`, `MEDIUM`, `HIGH`, `CRITICAL`).
1. If you are creating a **Simple condition**, enter the condition when a signal should be created. If you are creating a **Then condition**, enter the conditions required for a signal to be generated.
   - All rule conditions are evaluated as conditional statements. Thus, the order of the conditions affects which notifications are sent because the first condition to match generates the signal. Click and drag your rule conditions to change their order.
   - A rule condition contains logical operations (`>`, `>=`, `<`, `&&`, `||`) to determine if a signal should be generated based on the event counts in the previously defined queries.
   - The ASCII lowercase query labels are referenced in this section. An example rule condition for query `a` is `a > 3`.
   - **Note**: The query label must precede the operator. For example, `a > 3` is allowed; `3 < a` is not allowed.
1. In the **Add notify** section, click **Add Recipient** to optionally configure [notification targets](https://docs.datadoghq.com/security_platform/notifications/#notification-channels).
   - You can create [notification rules](https://docs.datadoghq.com/security/notifications/rules/) to manage notifications automatically, avoiding manual edits for each detection rule.

### Other parameters{% #other-parameters %}

#### 1. Rule multi-triggering{% #rule-multi-triggering-rt-signal-correlation %}

Configure how often you want to keep updating the same signal if new values are detected within a specified time frame. For example, the same signal updates if any new value is detected within 1 hour, for a maximum duration of 24 hours.

- An `evaluation window` is specified to match when at least one of the cases matches true. This is a sliding window and evaluates cases in real time.
- After a signal is generated, the signal remains "open" if a case is matched at least once within the `keep alive` window. Each time a new event matches any of the cases, the *last updated* timestamp is updated for the signal.
- A signal closes after the time exceeds the `maximum signal duration`, regardless of the query being matched. This time is calculated from the first seen timestamp.
- **Note**: The `evaluation window` must be less than or equal to the `keep alive` and `maximum signal duration`.

#### 2. Decrease severity for non-production environments{% #decrease-severity-rt-signal-correlation %}

Toggle **Decrease severity for non-production environments** if you want to prioritize production environment signals over non-production signals.

- The severity of signals in non-production environments are decreased by one level from what is defined by the rule case.
- The severity decrement is applied to signals with an environment tag starting with `staging`, `test`, or `dev`.

{% /tab %}

{% tab title="Sequence" %}
#### 1. Rule multi-triggering{% #rule-multi-triggering-rt-sequence %}

Configure how often you want to keep updating the same signal if new values are detected within a specified time frame. For example, the same signal updates if any new value is detected within 1 hour, for a maximum duration of 24 hours.

- An `evaluation window` is specified to match when at least one of the cases matches true. This is a sliding window and evaluates cases in real time.
- After a signal is generated, the signal remains "open" if a case is matched at least once within the `keep alive` window. Each time a new event matches any of the cases, the *last updated* timestamp is updated for the signal.
- A signal closes after the time exceeds the `maximum signal duration`, regardless of the query being matched. This time is calculated from the first seen timestamp.
- **Note**: The `evaluation window` must be less than or equal to the `keep alive` and `maximum signal duration`.

#### 2. Decrease severity for non-production environments{% #decrease-severity-rt-sequence %}

Toggle **Decrease severity for non-production environments** if you want to prioritize production environment signals over non-production signals.

- The severity of signals in non-production environments are decreased by one level from what is defined by the rule case.
- The severity decrement is applied to signals with an environment tag starting with `staging`, `test`, or `dev`.

#### 3. Enable optional group by{% #enable-group-by-rt-sequence %}

Toggle **Enable Optional Group By** section if you want to group events even when values are missing. If there is a missing value, a sample value is generated so that the log does not get excluded.
{% /tab %}

## Describe your playbook{% #describe-your-playbook %}

1. Enter a **Rule name**. The name appears in the detection rules list view and the title of the security signal.
1. In the **Rule message** section, use [notification variables](https://docs.datadoghq.com/security_platform/notifications/variables/) and Markdown to customize the notifications sent when a signal is generated.
   - You can use [template variables](https://docs.datadoghq.com/security_platform/notifications/variables/#template-variables) in the notification to inject dynamic context from triggered logs directly into a security signal and its associated notifications.
   - See the [Notification Variables documentation](https://docs.datadoghq.com/security_platform/notifications/variables/) for more information and examples.
1. Use the **Tag resulting signals** dropdown menu to add tags to your signals. For example, `security:attack` or `technique:T1110-brute-force`.
   - **Note**: the tag `security` is special. This tag is used to classify the security signal. The recommended options are: `attack`, `threat-intel`, `compliance`, `anomaly`, and `data-leak`.

## Create a suppression{% #create-a-suppression %}

(Optional) Create a suppression or add the rule to an existing suppression to prevent a signal from getting generated in specific cases. For example, if a user `john.doe` is triggering a signal, but their actions are benign and you do not want signals triggered from this user, add the following query into the **Add a suppression query** field: `@user.username:john.doe`.

#### Create new suppression{% #create-new-suppression %}

1. Enter a name for the suppression rule.
1. (Optional) Enter a description.
1. Enter a suppression query.
1. (Optional) Add a log exclusion query to exclude logs from being analyzed. These queries are based on **log attributes**.
   - **Note**: The legacy suppression was based on log exclusion queries, but it is now included in the suppression rule's **Add a suppression query** step.

#### Add to existing suppression{% #add-to-existing-suppression %}

1. Click **Add to Existing Suppression**.
1. Select an existing suppression in the dropdown menu.

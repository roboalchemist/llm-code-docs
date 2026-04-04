# Source: https://docs.datadoghq.com/security/cloud_siem/detect_and_monitor/custom_detection_rules/new_value.md

---
title: New Value
description: Learn about how the new value detection method works.
breadcrumbs: >-
  Docs > Datadog Security > Cloud SIEM > Detect and Monitor > Custom Detection
  Rules > New Value
---

# New Value

## Overview{% #overview %}

The new value detection method alerts when attribute values that have not been seen before, such as a new user, account, API key, or object ID, appear in your logs.

See [Create Rule](https://docs.datadoghq.com/security/cloud_siem/detect_and_monitor/custom_detection_rules/create_rule/real_time_rule?tab=newvalue) for instructions on how to configure a new value rule.

## How the new value detection method works{% #how-the-new-value-detection-method-works %}

A new value detection rule:

- Learns the values of the fields you have selected, such as `@userIdentity.arn`.
- Learns by recording values over a learning period or uses a threshold method that does not require a learning period. See Learning duration for more information.
- Triggers a signal when a value appears that has not been observed within the current scope.
- Forgets a learned value if the value has not been observed for the number of days set in the Forget value option. If the value has been forgotten, the rule alerts when the value reappears.

### Configuration options{% #configuration-options %}

#### Detect new values{% #detect-new-values %}

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/detection_rules/new_value/detect_new_value.e18940a4c360fcb79565352e1385dc1f.png?auto=format"
   alt="A new value rule's query with the detect new value setting highlighted" /%}

The **Detect new value** field defines the attributes containing the values to learn. You can add up to five attributes.

#### Group-by fields{% #group-by-fields %}

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/detection_rules/new_value/group_by.306e7aa6bc680fa4abe2e9ccc70d218c.png?auto=format"
   alt="A new value rule's query's group by field highlighted" /%}

The `group by` field defines the scope within which new values are evaluated, such as per account.

#### Learning duration{% #learning-duration %}

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/detection_rules/new_value/learning_duration.63f0c74c7d95d7965607d28d6dfbc9ac.png?auto=format"
   alt="A new value rule's query with the learning duration setting highlighted" /%}

The learning duration has the following options:

- **for all new values**: The rule triggers on any new values.
- **after the first seen value**: The rule triggers on any new values after the value has been observed once.
- **after**: Define the length of time the rule learns values for the selected fields. For example, if you select **after 7 days**, the rule learns the values for the first seven days and then triggers on any new values after the seven days. The maximum learning duration is 30 days.

#### Forget value{% #forget-value %}

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/detection_rules/new_value/forget_after.3789bee18971c9cbdef516d10bb1e7f6.png?auto=format"
   alt="A new value rule's other parameters section showing the forget after option" /%}

The [Forget value](https://docs.datadoghq.com/security/cloud_siem/detect_and_monitor/custom_detection_rules/create_rule/real_time_rule?tab=newvalue#forget-value-rt-new-value) option determines how long the rule keeps a value known. After this period has passed, the value is forgotten and the rule alerts on the value again. The maximum number of days for **Forget value** is 30 days.

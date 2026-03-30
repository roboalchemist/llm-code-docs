# Source: https://docs.datadoghq.com/security/cloud_siem/detect_and_monitor/suppressions.md

# Source: https://docs.datadoghq.com/security/suppressions.md

---
title: Suppressions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > Suppressions
---

# Suppressions
Available for:
{% icon name="icon-siem" /%}
 Cloud SIEM |
{% icon name="icon-cloud-security-management" /%}
 Workload Protection |
{% icon name="icon-app-sec" /%}
 App and API Protection
## Overview{% #overview %}

Suppressions are specific conditions for when a signal should not be generated, which can improve the accuracy and relevance of the signals that are generated.

## Suppression routes{% #suppression-routes %}

You can set up a suppression query within an individual detection rule, or define a separate suppression rule to suppress signals across one or more detection rules.

### Detection rules{% #detection-rules %}

When you [create](https://app.datadoghq.com/security/configuration/siem/rules/new) or [modify](https://docs.datadoghq.com/security/detection_rules/) a detection rule, you can define a suppression query to prevent a signal from getting generated. For example, add a rule query to determine when a detection rule triggers a security signal. You can also customize the suppression query to suppress signals for a specific attribute value.

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/suppressions/detection_suppression_rule.6953ad1cb273562425ad7da4bd4f7610.png?auto=format"
   alt="The detection rule editor showing the add suppression query section" /%}

### Suppression rules{% #suppression-rules %}

Use suppression rules to set general suppression conditions across multiple detection rules instead of setting up suppression conditions for each individual detection rule. For example, you can set up a suppression rule to suppress any signal that contains a specific IP.

## Suppressions configuration{% #suppressions-configuration %}

### Suppression list{% #suppression-list %}

The [suppression list](https://app.datadoghq.com/security/configuration/suppressions) provides a centralized and organized way for you to manage suppressions across multiple detection rules.

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/suppressions/suppression_list.3dbe59e1bf23c6aceb4f46842b519efe.png?auto=format"
   alt="The suppressions page showing a list of suppression rules" /%}

## Create a suppression rule{% #create-a-suppression-rule %}

1. Navigate to the [Suppressions](https://app.datadoghq.com/security/configuration/suppressions) page.
1. Click **+ New Suppression**.
1. Enter a name for the suppression query.
1. Add a description to provide context on why this suppression is being applied.
1. Optionally, add an expiration date on which this suppression will be deactivated.
1. Select the detection rules you want to apply this suppression to. You can select multiple detection rules.
1. In the **Add Suppression Query** section, you have the option to enter suppression queries so that a signal is not generated when the values are met. For example, if a user `john.doe` is triggering a signal, but their actions are benign and you no longer want signals triggered from this user, input the log query: `@user.username:john.doe`.
   {% image
      source="https://datadog-docs.imgix.net/images/security/security_monitoring/suppressions/suppression_query.bd5a9b11e5cf585622eac2e5d0be91eb.png?auto=format"
      alt="The add suppression query with the query @user.username:john.doe" /%}
Suppression rule queries are based on **signal attributes**.
1. Additionally, you can add a log exclusion query to exclude logs from being analyzed. These queries are based on **log attributes**. **Note**: The legacy suppression was based on log exclusion queries, but it is now included in the suppression rule's **Add a suppression query** step.

### Restrict edit permissions{% #restrict-edit-permissions %}

By default, all users have view and edit access to [suppressions](https://docs.datadoghq.com/security/suppressions/). To use granular access controls to limit the roles that may edit a suppression rule:

1. Click the vertical three-dot menu for the rule and select **Permissions**.
1. Click **Restrict Access**. The dialog box updates to show that members of your organization have **Viewer** access by default. Use that dropdown menu to select one or more roles, teams, or users that may edit the suppression rule.
1. Click **Add**.
1. Click **Save**.

**Note**: To maintain your edit access to the rule, Datadog requires you to include at least one role that you are a member of before saving.

To restore access to a rule:

1. Click the vertical three-dot menu for the rule and select **Permissions**.
1. Click **Restore Full Access**.
1. Click **Save**.

## Further reading{% #further-reading %}

- [Learn more about detection rules](https://docs.datadoghq.com/security/detection_rules/)

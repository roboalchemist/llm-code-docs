# Source: https://docs.datadoghq.com/security/default_rules/def-000-x8l.md

---
title: Retention policies should be configured using bucket lock on log buckets
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Retention policies should be configured
  using bucket lock on log buckets
---

# Retention policies should be configured using bucket lock on log buckets

## Description{% #description %}

Enabling retention policies on log buckets protects logs stored in cloud storage buckets from being overwritten or accidentally deleted. It is recommended to set up retention policies and configure `Bucket Lock` on all storage buckets that are used as log sinks.

### Default value{% #default-value %}

By default, storage buckets used as log sinks do not have retention policies and `Bucket Lock` configured.

## Rationale{% #rationale %}

Logs can be exported by creating one or more sinks that include a log filter and a destination. As Cloud Logging receives new log entries, they are compared against each sink. If a log entry matches a sink's filter, then a copy of the log entry is written to the destination. Sinks can be configured to export logs in storage buckets. It is recommended to configure a data retention policy for these cloud storage buckets and to lock the data retention policy, thus permanently preventing the policy from being reduced or removed. This way, if the system is ever compromised by an attacker or a malicious insider who wants to cover their tracks, the activity logs are definitely preserved for forensics and security investigations.

### Impact{% #impact %}

Locking a bucket is an irreversible action. Once you lock a bucket, you cannot remove the retention policy from the bucket or decrease the retention period for the policy. You then have to wait for the retention period for all items within the bucket before you can delete them, and then delete the bucket.

## Additional Information{% #additional-information %}

- **Caution**: Locking a retention policy is an irreversible action. Once locked, you must delete the entire bucket in order to "remove" the bucket's retention policy. However, before you can delete the bucket, you must be able to delete all the objects in the bucket, which itself is only possible if all the objects have reached the retention period set by the retention policy.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. If sinks are not configured, first follow the instructions in the recommendation: Ensure that sinks are configured for all log entries.
1. For each storage bucket configured as a sink, go to the Cloud Storage browser at [https://console.cloud.google.com/storage/browser/](https://console.cloud.google.com/storage/browser/)<BUCKET_NAME>.
1. Select the **Bucket Lock** tab near the top of the page.
1. In the **Retention policy** section, click the **Add Duration** link. The **Set retention policy?** dialog box appears
1. Enter the desired length of time for the retention period and click **Save Policy**
1. Set the **Lock Status** for this retention policy to **Locked**
1. Click **Lock policy**

### From the command line{% #from-the-command-line %}

1. To list all sinks destined to storage buckets:

   ```
   gcloud logging sinks list --folder=FOLDER_ID | --organization=ORGANIZATION_ID
   | --project=PROJECT_ID
   ```

1. For each storage bucket listed above, set a retention policy and lock it:

   ```
   gsutil retention set [TIME_DURATION] gs://[BUCKET_NAME]
   gsutil retention lock gs://[BUCKET_NAME]
   ```

For more information, visit [Set a retention policy on a bucket](https://cloud.google.com/storage/docs/using-bucket-lock#set-policy).

## References{% #references %}

1. [Retention policies and retention policy locks](https://cloud.google.com/storage/docs/bucket-lock)
1. [Use and lock retention policies](https://cloud.google.com/storage/docs/using-bucket-lock)

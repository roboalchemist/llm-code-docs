# Source: https://docs.tabnine.com/main/administering-tabnine/managing-your-team/reporting/reporting/configuring-scheduled-csv-reports.md

# Configuring scheduled CSV reports

You can schedule sending the CSV-based usage reports by email.

{% hint style="info" %}
**Prerequisites**

Your Tabnine private installation must have [SMTP configuration](https://docs.tabnine.com/main/administering-tabnine/settings/email-settings#configure-smtp) in place.
{% endhint %}

### Enabling schedule CSV-based usage report

1. Go to the `value.yaml` file of your Tabnine [private installation](https://github.com/codota/docs/blob/main/main/administering-tabnine/private-installation/managing-your-team/reporting/reporting/broken-reference/README.md).
2. Add the following `analytics` section to the `values.yaml` file. If you already have an `analytics` section, append the following content to the existing one. (Duplicated sections in the yaml file may result in unexpected behavior.)

```
analytics:
  ScheduledCsvEmailReporting:
    cronScheduling: 0 0 * * *
    enabled: true
  csvReportEmails: yourname@yourcompany.com
```

`enabled`: True/false toggle of the scheduling of the report email.

`cronScheduling` : A [cron](https://en.wikipedia.org/wiki/Cron) timer representation of the recurrence of the report. In the above example, the email scheduling will be every day at midnight.

`csvReportEmails` : List of comma-separated emails of the report email recipients.

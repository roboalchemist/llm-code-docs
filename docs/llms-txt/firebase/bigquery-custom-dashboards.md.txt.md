# Source: https://firebase.google.com/docs/crashlytics/bigquery-custom-dashboards.md.txt

<br />

You can use your exported Crashlytics and (optionally) Firebase sessions
data in BigQuery to create custom dashboards.

## Visualize exported Crashlytics data with Looker Studio

[Looker Studio](https://cloud.google.com/looker-studio)
turns your Crashlytics datasets in BigQuery into reports that are
easier to read, easier to share, and fully customizable.

To learn more about using Looker Studio, check out their
[welcome guide](https://cloud.google.com/looker/docs/studio).

### Use a Crashlytics report template

Looker Studio has a sample report for Crashlytics that includes a
comprehensive set of dimensions and metrics from the exported Crashlytics
BigQuery schema. If you've enabled Crashlytics streaming export
to BigQuery, then you can view that data on the **Realtime trends**
page of the Looker Studio template. You can use the sample as a
template to quickly create new reports and visualizations based on your own
app's raw crash data:

1. Open the
   [Crashlytics Looker Studio Dashboard template](https://datastudio.google.com/c/reporting/10TMAKxL0ZxcNGTLDQy1LAF5V7uNDYxRC/page/1xZU/preview).

2. Click **Use Template** in the upper-right corner.

3. In the **New Data Source** drop-down, select **Create New Data Source**.

4. Click **Select** on the **BigQuery** card.

5. Select a table containing exported Crashlytics data by choosing
   **My Projects \> <var translate="no">PROJECT_ID</var> \> firebase_crashlytics \> <var translate="no">TABLE_NAME</var>**.

   Your batch table is always available to select. If
   Crashlytics streaming export to BigQuery is enabled, then you
   can select your realtime table instead.
6. Under **Configuration** , set **Crashlytics Template level** to
   **Default**.

7. Click **Connect** to create the new data source.

8. Click **Add to Report** to return to the Crashlytics template.

9. Finally, click **Create Report** to create your copy of the Crashlytics
   Looker Studio Dashboard template.

> [!NOTE]
> **Note:** If you linked Crashlytics to BigQuery before December 6, 2018, then your dataset is named **My Projects \> <var translate="no">PROJECT_ID</var> \> crashlytics \> <var translate="no">TABLE_NAME</var>**.
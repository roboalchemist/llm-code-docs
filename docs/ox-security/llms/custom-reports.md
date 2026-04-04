# Source: https://docs.ox.security/generate-reports/custom-reports.md

# Custom Reports

> **Note:** This capability is currently in Beta.

Custom reports let you turn OX data into focused dashboards that answer specific questions for your team. You combine predefined widgets with your own charts and tables, apply filters, and share the result as a public or private report.

Why use custom reports:

* Align views to your goals. Build dashboards per product, business unit, or initiative.
* Reduce noise. Filter by application, severity, category, owner, time window, or tags.
* Share the right context. Make reports public for the organization or keep them private while you iterate.
* Move work forward. Keep critical KPIs and queues visible so teams act on them.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-3c45cbc060ffdaca23e35b617291f7e32d3b8a51%2Fgeneral_custom_reports.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

**To create a custom report:**

1. Go to **Reports > Custom Reports** and select **+** **Create report**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-7afd75538ade24636eda0160ac8b537adf12d69f%2Fcreate_new_report.png?alt=media" alt="" width="405"><figcaption></figcaption></figure>

1. Add a **Report Name** and select visibility:

* **Public:** Visible to all users in your organization.
* **Private:** Visible only to you.

1. Select **CREATE NEW REPORT**. Now you can start adding widgets.

> **Note:** The page opens with a creation picker. A full list of saved reports may not be available yet.

## Add widgets

Custom Reports include three widget types that share the same filter model and preview behavior. Choose the type that matches the level of detail you want, then apply filters to focus the data.

| Widget Type                                                                                                  | Purpose                                                                                 | Data granularity            | Editable settings                                                                  |
| ------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- | --------------------------- | ---------------------------------------------------------------------------------- |
| [**Gallery widget**](https://docs.ox.security/generate-reports/custom-reports/add-a-widget-from-the-gallery) | Pick Gallery widget to add a ready-made insight quickly.                                | Aggregated                  | Title, chart type, widget-level filters                                            |
| [**Custom chart**](https://docs.ox.security/generate-reports/custom-reports/add-a-custom-visualization)      | Pick Custom visualization for trends or distributions by a field, with optional series. | Aggregated                  | Title, data source, group by, optional sub-group, chart type, widget-level filters |
| [**Custom table**](https://docs.ox.security/generate-reports/custom-reports/add-a-custom-table-widget)       | Pick Custom table when you need item-level details for triage and follow-up.            | Granular (one row per item) | Title, data source, columns and order, widget-level filters                        |

### Filters

All widget types support the same filter controls:

* **Common filters:** Application, Severity, Category, App Tag
* **Additional filters:** Time window and other context fields, depending on the data source
* **Scope:** Widget-level filters apply only to the selected widget and persist. Report-level filters apply to all widgets and reset when you reopen the report.

> Note: Filters set for a widget apply to this widget only. Report-level filters do not overwrite widget-level filters.

### Widget Examples

* **Critical issues table:**\
  Data source: Issues.\
  Columns: Severity, Name, First seen, Issue owner.\
  Type: Custom table.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-d403b918da64202b36f84e218db8394a5069203b%2Fexample_Critical%20issues%20table.png?alt=media" alt="" width="360"><figcaption></figcaption></figure>

* **Issues by severity**\
  Data source: Issues.\
  Group by: Severity.\
  Chart: Bar chart.\
  Filters > Severity: Critical, High, Medium.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-4b2a0df81709c0771d92eac9cada1f5334a7a911%2Fexample_Issue%20by%20severity.png?alt=media" alt="" width="347"><figcaption></figcaption></figure>

* **SLA trend**\
  Gallery: SLA trend.\
  Optional: adjust visualization and time filter.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-47024eadae8d173f630e76d178633d1aac9e485a%2Fexample_SLA%20trend.png?alt=media" alt="" width="353"><figcaption></figcaption></figure>

# Source: https://docs.axonius.com/docs/csv-specific-adapters.md

# CSV Asset-Specific Adapters

Asset-specific CSV adapters are purpose-built to ingest data for a single, predefined asset type. Unlike the general CSV adapter, which offers a flexible schema to map various inventory types (Devices, Users, Databases, and more), these adapters are hardcoded with logic tailored to specific business domains. For example, the [CSV - Applications](https://docs.axonius.com/axonius-help-docs/docs/applications-csv) adapter has built-in field mapping rules optimized for SaaS vendor management.

Use asset-specific CSV adapters to reduce manual configuration of the general CSV adapter, and use a streamlined workflow with a fixed schema.

<Callout icon="📘" theme="info">
  **Note**

  If [Custom Files](https://docs.axonius.com/axonius-help-docs/docs/custom-files) supports a specific asset type you want to import data from, it is recommended to use Custom Files and not a CSV-specific adapters.
</Callout>

<br />
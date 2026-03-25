# Source: https://docs.mage.ai/integrations/compute/databricks.md

# Source: https://docs.mage.ai/data-integrations/destinations/databricks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Databricks

> How to configure Databricks as a destination in Mage to write pipeline data to Databricks SQL warehouses using Unity Catalog.

export const ProOnly = ({button = 'Get started for free', description = 'Try our fully managed solution to access this advanced feature.', source = 'documentation', title = 'Only in Mage Pro.'}) => <a href={`https://cloud.mage.ai/sign-up?source=${source}`} className="block my-4 px-5 py-4 overflow-hidden rounded-xl flex gap-3 border border-emerald-500/20 bg-emerald-50/50 dark:border-emerald-500/30 dark:bg-emerald-500/10" target="_blank">
    <div style={{
  display: 'flex',
  alignItems: 'center',
  width: '100%'
}}>
      <div className="text-sm prose min-w-0 text-emerald-900 dark:text-emerald-200" style={{
  flex: 1
}}>
        {title}
        <p className="normal">{description}</p>
      </div>

      <div> </div>

      <div>
        <ProButton label={button} href={`https://cloud.mage.ai/sign-up?source=${source}`} />
      </div>
    </div>
  </a>;

export const ProButton = ({href, label = 'Get started with Mage Pro for free', source = 'documentation'}) => <div style={{
  height: 32,
  position: 'relative'
}}>
    <a target="_blank" className="group px-4 py-1.5 relative inline-flex items-center text-sm font-medium rounded-full" href={href ?? `https://cloud.mage.ai/sign-up?source=${source}`}>
      <span className="absolute inset-0 bg-primary-dark dark:bg-primary-light/10 border-primary-light/30 rounded-full dark:border group-hover:opacity-[0.9] dark:group-hover:border-primary-light/60">
      </span>

      <div className="mr-0.5 space-x-2.5 flex items-center">
        <span class="z-10 text-white dark:text-primary-light">
          {label}
        </span>

        <svg width="3" height="24" viewBox="0 -9 3 24" class="h-5 rotate-0 overflow-visible text-white/90 dark:text-primary-light">
          <path d="M0 0L3 3L0 6" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path>
        </svg>
      </div>
    </a>
  </div>;

<ProOnly source="data-integration" />

Use **Databricks** as a destination in Mage to load structured data into your Databricks workspace. Mage integrates with Databricks SQL warehouses and uses **Unity Catalog** for table management.

This destination is ideal for exporting transformed pipeline data to Databricks for analytics, ML workloads, or data lakehouse operations.

***

## Required Configuration

Provide the following credentials when configuring Databricks as a destination:

| Key               | Description                                           | Example Value                     | Required |
| ----------------- | ----------------------------------------------------- | --------------------------------- | -------- |
| `access_token`    | Personal access token to authenticate with Databricks | `dapi123abc...`                   | ✅        |
| `server_hostname` | Hostname of your Databricks workspace                 | `dbc-123456.cloud.databricks.com` | ✅        |
| `http_path`       | HTTP path of the Databricks SQL warehouse or cluster  | `/sql/1.0/warehouses/abc123`      | ✅        |
| `schema`          | Name of the schema (database) within the catalog      | `analytics`                       | ✅        |
| `table`           | Name of the table to write data into                  | `user_events`                     | ✅        |

***

## Optional Configuration

| Key                    | Description                                                                     | Example Value | Default |
| ---------------------- | ------------------------------------------------------------------------------- | ------------- | ------- |
| `catalog`              | Name of the Unity Catalog to use                                                | `workspace`   | -       |
| `skip_schema_creation` | If `true`, Mage won't run `CREATE SCHEMA`. Useful if the schema already exists. | `true`        | `false` |
| `lower_case`           | If `true`, all column names will be lowercased.                                 | `true`        | `true`  |
| `allow_reserved_words` | If `true`, Mage will allow use of SQL reserved words as column names.           | `false`       | `false` |

***

## Notes

* **Unity Catalog**: Set `catalog` to your Unity Catalog name. This is an optional field for table management in Databricks.
* **Access Token**: Generate a personal access token from your Databricks workspace settings.
* **HTTP Path**: Find the HTTP path in your SQL warehouse or cluster connection details.
* **Permissions**: Ensure your access token has permissions to create schemas and write to tables in the specified catalog and schema.

***

## Related Resources

* [Databricks SQL Documentation](https://docs.databricks.com/sql/)
* [Unity Catalog Overview](https://docs.databricks.com/data-governance/unity-catalog/index.html)
* [Databricks Personal Access Tokens](https://docs.databricks.com/dev-tools/auth/pat.html)


Built with [Mintlify](https://mintlify.com).
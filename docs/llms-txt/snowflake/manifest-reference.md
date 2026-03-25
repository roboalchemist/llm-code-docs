# Source: https://docs.snowflake.com/en/developer-guide/native-apps/manifest-reference.md

# Source: https://docs.snowflake.com/en/developer-guide/declarative-sharing/manifest-reference.md

# Declarative Native App manifest reference

Providers create a manifest file as part of a [package](package.md).

The manifest file is a text-based [YAML](https://yaml.org/spec/) file, with the filename: `manifest.yml`. It’s used to declaratively share data and logic with consumers, such as notebooks, user-defined functions, stored procedures, tables, and views.

The manifest file also defines [app roles](app-roles.md), which app owners can use to share a subset of the app’s data and features to teams in their organization teams by role.

For information about developing an application package, see [Application Packages in Declarative Sharing in the Native Application Framework](package.md).

## Declarative Native App manifest

The general format of a Declarative Native App manifest contains:

```yaml
manifest_version: # Added automatically. Don't include.
application_content: # Optional, describes associated app logic
roles: # Optional, describes roles associated with shared_content
shared_content: # Required, describes associated data to be shared
```

## Fields

Declarative Native App manifests include the following fields:

### `manifest_version` field

This field is added automatically to the manifest file when you release a new version of an application package.

Don’t include this field when creating a manifest file to include in an application package. Editing this field manually is not supported.

The `manifest_version` top level field (Integer, required) specifies the version
number of the manifest file.

For more information about versioning, see [Package Versions in Declarative Sharing in the Native Application Framework](versioning.md).

### `application_content` field

The `application_content` field (list, optional) defines bundled content declaratively shared by the app.

This field includes a single `notebooks` field:

* `application_content.notebooks` (List, required): A list of named [notebooks](../../user-guide/ui-snowsight/notebooks.md).

#### `application_content.notebooks.{named notebook}` field

Each named notebook supports the following name value pairs:

* `main_file` (string, required) the path to the interactive Python notebook (.ipynb) file, relative to the root of the package version.
* `comment` (string, optional): A comment describing the notebook.
* `runtime_environment_version` (string, optional): Specifies a particular [runtime environment version](../../user-guide/ui-snowsight/notebooks.md)
  for the notebook execution context, if applicable within the platform.
* `roles` (list, optional): A list of app roles that can grant access to the notebook, for example, `[sales,marketing]`. When this field is empty (`[]`) or omitted, then only app owners and roles with [granted IMPORTED PRIVILEGES](consumer/install.md) receive access. The included roles must be defined in the top-level roles field.

> **Note:**
>
> The `main_file` path is always relative to the root of the package
> version (the `snow://package/<DECL_SHARE_APP_PKG>/versions/<version>` prefix).
> For example, if the full path to the notebook file is
> `snow://package/<DECL_SHARE_APP_PKG>/versions/LIVE/NOTEBOOK.ipynb`,
> then specify `main_file` as just `NOTEBOOK.ipynb`.

##### `application_context` example

In this example, a single notebook, **salesbook**, is defined using the
notebook file **NOTEBOOK1.ipynb** which uses the known runtime **stable**
and provides access to those granted either the **sales** or **marketing** roles.

```yaml
application_content:
    notebooks:
        - salesbook:
              roles: [sales, marketing]
              main_file: NOTEBOOK1.ipynb
              comment: Notebook1: Sales and marketing notebook
              runtime_environment_version: stable

roles:
  - sales:
  - marketing:
```

### `roles` field

The `roles` top level field (list, optional) defines a list of [app roles](app-roles.md). These roles allow app owners to provide access to shared objects in an app — such as schemas, tables, views, and notebooks — to their organization.

Each named role can optionally contain a `comment`, which appears as a description when the app owner lists the roles in the application.

These roles are referenced in the manifest by shared objects, at the named `notebook`, `schema`, `table`, `view`, or `semantic_view` level. For objects at the `table`, `view`, or `semantic_view` level, roles must also be specified at the `schema` level.

> **Note:**
>
> * All content in the manifest is accessible to the app owner, the ACCOUNTADMIN, and to roles that are granted [IMPORTED PRIVILEGES](consumer/install.md) to the app.
> * The object name defined in this manifest file is used for the runtime object resolution. If the provider changes the object name without updating the manifest file with a new version, consumers will lose access to the object.

#### `roles` example

```yaml
roles:
  - sales:
  - marketing:

application_content:
  notebooks:
    - salesbook:
        roles: [sales, marketing]
        main_file: NOTEBOOK1.ipynb
        comment: Sales and marketing notebook

shared_content:
  databases:
    - sales:
        schemas:
          - orders:
              roles: [sales, marketing]
              tables:
                - january_2025:        # App owners/assignees only
                - february_2025:
                    roles: [sales]     # Accessible to sales only
                - march_2025:
                    roles: [marketing] # Accessible to marketing only
    - customer_info:
        schemas:
          - customer_contact:
              roles: [customer_support]
              views:
                - customer_address:
                    roles: [customer_support] # Accessible to customer_support
                - customer_details:
                    roles: []                 # App owners/assignees only
```

For more information about roles, see [app roles](app-roles.md).

### `shared_content` field

The `shared_content` field (list, required) defines a list of databases declaratively shared by the app. Each database includes a list of named `schemas`. Each schema can include a list of named entities grouped by type.

This field includes a single `databases` field and an optional `required_databases` field:

* `shared_content.databases` (List, required): A list of named database instances and the underlying objects to share. In the example below, the manifest adds a database named `sales`.

#### `shared_content.databases.{named database}` field

Each named database supports the following name value pairs:

* `schemas` (list, required): A list of schemas within the database.

#### `shared_content.required_databases.{named database}` field

The `required_databases` field (list, optional) defines a list of databases that
are dependencies of the shared databases. These databases are referenced by
views in the shared databases, but are not shared directly. For more information
about managing cross-database dependencies, see [Dependency databases: Managing cross-database references](dependency-databases.md).

When your application shares data from multiple databases, you must explicitly list all
additional databases that are referenced by objects in your shared content under
the `required_databases` field. This ensures that the application can be
deployed successfully in other regions where these databases may not exist by
default.

Including a database in the `required_databases` field is similar to
referencing a database using the REFERENCE_USAGE privilege in traditional
Secure Data Sharing. For information about the REFERENCE_USAGE privilege and how
dependent databases are shared in traditional data sharing, see
[Share data from multiple databases](../../user-guide/data-sharing-multiple-db.md).

#### `schemas.{named schema}` field

Each named schema supports the following name value pairs:

* `tables` (list, [OneOfRequired]): A list of named tables, which can include [dynamic tables](../../user-guide/dynamic-tables-about.md) and [Apache Iceberg tables](../../user-guide/tables-iceberg.md).
* `views` (list, [OneOfRequired]): A list of named views.
* `semantic_views` (list, [OneOfRequired]): A list of named semantic views.
* `functions` (list, [OneOfRequired]): A list of named user-defined functions (UDFs).
* `procedures` (list, [OneOfRequired]): A list of named stored procedures.
* `cortex_agents` (list, [OneOfRequired]): A list of named [Cortex Agents](../../user-guide/snowflake-cortex/cortex-agents.md).
* `roles` (list, optional): A list of app roles that the objects in the schema can use, for example, `[sales,marketing]`. When this field is empty (`[]`) or omitted, then only app owners and roles with [granted IMPORTED PRIVILEGES](consumer/install.md) receive access. The included roles must be defined in the top-level roles field.

[OneOfRequired]
(1,2,3,4,5,6,7,8,9,10,11,12)

at least one of `tables`, `views`, `semantic_views`, `functions`, `procedures`, or `cortex_agents` is required.

> **Important:**
>
> You must enforce schema separation between data objects (objects shared by reference: `tables`, `views`, and `semantic_views`) and logic objects (objects shared by copy: `functions`, `procedures`, and :`cortex_agents`). You can’t mix data and logic objects in the same schema.

#### `tables.{named table}` field

Each named standard table, [dynamic table](../../user-guide/dynamic-tables-about.md), and [Apache Iceberg table](../../user-guide/tables-iceberg.md) (List, required [OneOfRequired] ) supports the following name value pair:

* `roles` (list, optional): A list of app roles that can access the table; for example, `[sales]`. When this field is empty (`[]`) or omitted, then only app owners and roles with [granted IMPORTED PRIVILEGES](consumer/install.md) receive access. The included roles must be defined in the top-level roles field and included in the {named schema}.roles field.

> **Note:**
>
> Shared [dynamic tables](../../user-guide/dynamic-tables-about.md) and [Apache Iceberg tables](../../user-guide/tables-iceberg.md) replicated to remote regions are read-only and do not refresh automatically. Data freshness depends on the replication frequency from the source, and underlying source objects do not need to be replicated. For details, see [Replication considerations](../../user-guide/account-replication-considerations.md).

> **Note:**
>
> To allow consumers to create streams on this shared object (for change data capture or incremental loading), you must enable `CHANGE_TRACKING = TRUE` on the source table in your provider account using standard SQL commands (for example, `ALTER TABLE ... SET CHANGE_TRACKING = TRUE`). This setting can’t be changed by the consumer on the shared object; it must be set on the source.

#### `views.{named view}` field

Each named view (List, required [OneOfRequired] ): supports the following name value pair:

* `roles` (list, optional): A list of app roles that can access the view; for example, `[marketing]`. When this field is empty (`[]`) or omitted, then only app owners and roles with [granted IMPORTED PRIVILEGES](consumer/install.md) receive access. The included roles must be defined in the top-level roles field and included in the {named schema}.roles field.

> **Note:**
>
> To allow consumers to create streams on this shared object (for change data capture or incremental loading), you must enable `CHANGE_TRACKING = TRUE` on the source table in your provider account using standard SQL commands (for example, `ALTER TABLE ... SET CHANGE_TRACKING = TRUE`). This setting can’t be changed by the consumer on the shared object; it must be set on the source.

#### `semantic_views.{named semantic view}` field

Each named semantic view (List, required [OneOfRequired] ): supports the following name value pair:

* `roles` (list, optional): A list of app roles that can access the semantic view; for example, `[sales]`. Note that, when sharing a semantic view, its referenced tables or views must be shared as well. When this field is empty (`[]`) or omitted, then only app owners and roles with [granted IMPORTED PRIVILEGES](consumer/install.md) receive access. The included roles must be defined in the top-level roles field and included in the {named schema}.roles field.

#### `functions.{named function}` field

Each named function (List, required [OneOfRequired] ): supports the following name value pair:

* `roles` (list, optional): A list of app roles that can access the function; for example, `[analyst]`. When this field is empty (`[]`) or omitted, then only app owners and roles with [granted IMPORTED PRIVILEGES](consumer/install.md) receive access. The included roles must be defined in the top-level roles field and included in the {named schema}.roles field.

#### `procedures.{named procedure}` field

Each named stored procedure (List, required [OneOfRequired] ): supports the following name value pair:

* `roles` (list, optional): A list of app roles that can access the procedure; for example, `[analyst]`. When this field is empty (`[]`) or omitted, then only app owners and roles with [granted IMPORTED PRIVILEGES](consumer/install.md) receive access. The included roles must be defined in the top-level roles field and included in the {named schema}.roles field.

#### `cortex_agents.{named cortex agent}` field

Each named [Cortex Agent](../../user-guide/snowflake-cortex/cortex-agents.md) (List, required [OneOfRequired] ): supports the following name value pair:

* `roles` (list, optional): A list of app roles that can access the Cortex Agent; for example, `[app_user]`. When this field is empty (`[]`) or omitted, then only app owners and roles with [granted IMPORTED PRIVILEGES](consumer/install.md) receive access. The included roles must be defined in the top-level roles field and included in the {named schema}.roles field.

#### `shared_content` example

In this example, two databases are exposed: **sales** and **customer_info**.
Within these databases the **orders.[january_2025|february_2025]** tables are exposed
as well as the **customer_contact.customer_address** view.

Two required databases are also exposed: **sales_projections** and **customer_analytics**.
These databases can be referenced by views in the shared databases, but are not shared directly.

```yaml
roles:
  - sales:
  - marketing:

shared_content:
  required_databases:
    sales_projections
    customer_analytics
  databases:
    - sales:
        schemas:
          - orders:
              roles: [sales, marketing]
              tables:
                - january_2025:        # App owners/assignees only
                - february_2025:
                    roles: [sales]     # Accessible to sales only
                - march_2025:
                    roles: [marketing] # Accessible to marketing only
    - customer_info:
        schemas:
          - customer_contact:
              roles: [customer_support]
              views:
                - customer_address:
                    roles: [customer_support] # Accessible to customer_support
                - customer_details:
                    roles: []                 # App owners/assignees only
```

## Manifest file example

The following code block is an example of a Declarative Native App manifest file.

Note that data and code objects must be in different schemas.

```yaml
manifest_version: 2

roles:
  - VIEWER:
      comment: "The VIEWER role provides access to only one view."
  - ANALYST:
      comment: "The ANALYST role provides access to views, the table, and logic."
  - APP_USER:
      comment: "The APP_USER role provides access to the Cortex Agent and the underlying data."

shared_content:
  databases:
    - SNAF_POPULATION_DB:
        schemas:
          - DATA_SCHEMA:
              roles: [VIEWER, ANALYST]
              tables:
                - COUNTRY_POP_BY_YEAR:
                    roles: [ANALYST]
                - POPULATION_DYNAMIC_TABLE:
                    roles: [ANALYST]
                - MANAGED_POPULATION_ICEBERG_TABLE:
                    roles: [ANALYST]
              views:
                - COUNTRY_POP_BY_YEAR_2000:
                    roles: [VIEWER, ANALYST]
          - LOGIC_SCHEMA:
              roles: [ANALYST]
              functions:
                - POPULATION_ANALYSIS_FUNCTION(NUMBER):
                    roles: [ANALYST]
              procedures:
                - POPULATION_ANALYSIS_PROCEDURE():
                    roles: [ANALYST]
          - AGENT_SCHEMA:
              roles: [APP_USER]
              cortex_agents:
                - PRODUCT_AGENT:
                    roles: [APP_USER]
application_content:
  notebooks:
      - intro_notebook:
          roles: [VIEWER, ANALYST]
          main_file: INTRO_NB.ipynb
      - analyst_notebook:
          roles: [ANALYST]
          main_file: ANALYST_NB.ipynb
```

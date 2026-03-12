# Source: https://docs.snowflake.com/en/developer-guide/snowflake-ml/model-registry/model-management.md

# Managing models with the Snowflake Model Registry

The Snowflake Model Registry simplifies the process of bringing a machine learning model from development to production.
A well-organized model registry serves as the central hub and single source for all models, their metrics, and their
metadata. Logging your model in the registry is the first and most significant step in your Snowflake ML Ops journey,
bringing your machine learning operations under the control, security, and governance Snowflake is known for.

The Snowflake Model Registry is flexible enough to address a wide range of ML model management use cases and scenarios.
This topic offers guidance on how best to use the registry to seamlessly manage models from development to production,
including:

* How to control access to models so that the right group of users or roles can perform various operations.
* How to query the metrics and other metadata of all your models.
* How to manage the lifecycle of a model from development to production.
* How to roll out a new version of a model without any changes to production code.

## Governance

Because [machine learning models](../../../sql-reference/commands-model.md) are first-class objects in Snowflake, you
can use all standard Snowflake governance capabilities with them, including role-based access control and the
information schema.

### Role-based access control

Model objects have three privileges: OWNERSHIP, USAGE, and READ.

| Privilege | Description |
| --- | --- |
| OWNERSHIP | Full control of the model, including managing model versions, accessing artifacts, and updating model metadata. Only one role can own the model, but you can [grant that role](../../../sql-reference/sql/grant-role.md) to multiple users or to other roles. |
| USAGE | Read-only access to the model, allowing warehouse inference (prediction) and use of the SHOW MODELS and SHOW VERSIONS IN MODEL commands. Roles with only USAGE cannot access the model code, weights, or other artifacts. |
| READ | Read-only access to the model, allowing SPCS inference (prediction), model files, metadata and use of the SHOW MODELS and SHOW VERSIONS IN MODEL commands. |

The owner of a model can grant access to any role as follows:

```sqlexample
GRANT USAGE ON MODEL my_model TO ROLE prod_role;
-- OR
GRANT READ ON MODEL my_model TO ROLE prod_role;
```

### Information schema queries

Like all Snowflake objects, models are represented in a view in the [Snowflake Information Schema](../../../sql-reference/info-schema.md). The view for
models and their versions is [INFORMATION_SCHEMA.MODEL_VERSIONS](../../../sql-reference/info-schema/model_versions.md).
Model version information is a superset of the information for models, so there is no separate MODEL view.

Through this view, you can query the registry itself. For example, assume that you maintain an accuracy metric, adding
it to each model version using SQL like the following.

```sqlexample
ALTER MODEL my_model MODIFY VERSION v1
    SET METADATA = '{"metric": {"accuracy": 0.769}}';
```

> **Note:**
>
> You can also [set metrics with the registry’s Python API](overview.md).
>
> ```python
> mv = reg.get_model("my_model").version("v1").set_metric("accuracy", 0.769)
> ```

After you have added this metric to all versions of your models, you can use a query like the one here to retrieve information
about all model objects and list them in order of highest accuracy to lowest.

```sqlexample
SELECT
    catalog_name,
    schema_name,
    model_name,
    model_version_name,
    metadata:metric:accuracy AS accuracy,
    comment,
    owner,
    functions,
    created_on,
    last_altered_on
FROM my_database.INFORMATION_SCHEMA.MODEL_VERSIONS
ORDER BY accuracy DESC;
```

You can create more complex queries that join to other information schema views or other tables for more detailed
analysis.

## Model lifecycle management

To meet the diverse needs of small and large enterprises, the Snowflake Model Registry provides four simple, yet
powerful, schemes for managing the lifecycle of a model from development to production. Choose the one that works
best for you based on the governance structure you prefer.

* Using the default version
* Using aliases
* Using tags
* Using multiple schemas

### Using the default version

Models are versioned, and one version is designated as the default version. You can treat the default version of a model
as the production version by convention; production code only ever calls the default version of the model.

In this scenario, you promote a model version to production simply by setting it as the default, perhaps after it meets
your model scoring or performance evaluation workflow requirements. This is the simplest way to control which version of
a model is used in production.

*Use this method when:*

* The owner of the model has the authority to decide which version to use in production.
* You don’t need to track any lifecycle stages besides development/production.

#### Initial setup

The model owner grants usage on the model to a production role.

```sqlexample
GRANT USAGE ON MODEL my_model TO ROLE prod_role;
```

When the model is initially logged, its sole version is the default, and that version is ready to be used.

> **Important:**
>
> A model must always have a default version. Under this scheme, then, you can’t designate a model as not yet having a
> production version. If you need to prevent models from being used before they’re ready, you might log an initial
> version that immediately throws an error. This version would remain the default until some other version is ready.

#### Promoting a model to production

When a new version, called `new_version` in the SQL below, has cleared the quality bar, designate it as the
default to mark it as the production version.

```sqlexample
ALTER MODEL my_model SET DEFAULT_VERSION = new_version;
```

#### Using the model in production

In production, call the model directly to use the default version.

```sqlexample
SELECT my_model!predict(...) ... ;
```

#### Development and testing

To use a pre-release version, call the desired model version by name:

```sqlexample
WITH my_version AS MODEL my_model VERSION new_version
    SELECT my_version!predict(...) ...;
```

### Using aliases

Many organizations manage model lifecycles using multiple stages, such as development, canary, staging, production, and
deprecation. Model versions can have [aliases](overview.md), user-defined
labels or tags that you can exclusively attach to any of a model’s versions. You can you use aliases to represent the
lifecycle stages your organization uses.

*Use this method when:*

* The model owner has the authority to make model lifecycle stage decisions.
* You want to track multiple lifecycle stages, not just development/production.

The example below uses two preproduction stages (`alpha` and `beta`) and one production stage (`production`).

#### Initial setup

The model owner grants usage on the model to a production role.

```sqlexample
GRANT USAGE ON MODEL my_model TO ROLE prod_role;
```

#### Promoting the initial version of the model

When you log the model, set the `production` alias to point to the first version, here named `v1`.

```sqlexample
ALTER MODEL my_model VERSION v1 SET ALIAS = production;
```

#### Managing preproduction versions

Initially, the model has no designated `alpha` or `beta` version. When you add a new version, initially designate it
`alpha`.

```sqlexample
ALTER MODEL my_model VERSION v2 SET ALIAS = alpha;
```

Later, to promote the new version to `beta`:

```sqlexample
ALTER MODEL my_model VERSION v2 UNSET ALIAS;
ALTER MODEL my_model VERSION v2 SET ALIAS = beta;
```

#### Promoting subsequent versions of the model

When a new version of a model has passed muster, remove the `production` alias from the current production version,
here `v1`, and apply it to the new version, here `v2`.

```sqlexample
ALTER MODEL my_model VERSION v1 UNSET ALIAS;
ALTER MODEL my_model VERSION v2 UNSET ALIAS;
ALTER MODEL my_model VERSION v2 SET ALIAS = production;
```

#### Using the model in production

Call the production version of the model through the `production` alias.

```sqlexample
WITH my_version AS MODEL my_model VERSION production
    SELECT my_version!predict(...) ...;
```

#### Development and testing

To use pre-release versions, call the model through the `alpha` or `beta` alias instead. For example, to test the
alpha version:

```sqlexample
WITH my_version AS MODEL my_model VERSION alpha
    SELECT my_version!predict(...) ...;
```

### Using tags

The default version and
alias lifecycle management schemes already described assume that the
model owner can manage model lifecycles. In many organizations, though, this responsibility rests with a separate production
engineering role, and data scientists don’t have the authority to promote model versions to production. Because models
are first-class Snowflake objects, you can apply [tags](../../../user-guide/object-tagging/introduction.md) to them for this purpose. Tags are
securable by role-based access control and are suitable for this separation of responsibility.

*Use this method when:*

* A role other than the model owner determines when to promote a model version from one lifecycle stage to the next.

#### Initial setup

The model owner grants usage on the model to a production role.

```sqlexample
GRANT USAGE ON MODEL my_model TO ROLE prod_role;
```

The production role also needs the ability to see the tags on a model and to read the tag values. Here, the
former is achieved by granting the broad APPLY TAG privilege on the account to the role. The latter is achieved
by granting the USAGE privilege on the schema.

```sqlexample
USE ROLE ACCOUNTADMIN;
GRANT APPLY TAG ON ACCOUNT TO ROLE prod_role;
GRANT USAGE ON SCHEMA model_database.model_schema TO ROLE prod_role;
```

To create tags, a role needs the CREATE TAG privilege on the schema.

Create a tag named `live_version` in a schema owned by `prod_role` to hold the name of the current production
version of the model.

```sqlexample
USE ROLE prod_role;
USE SCHEMA prod_db.prod_schema;

CREATE TAG live_version;
```

> **Note:**
>
> Here, the tag is created in the production schema, as it is managed by the production role. When using it in other
> schemas, use its fully-qualified name.

#### Promoting the initial version of the model

To make a model available in production, apply the `live_version` tag to the model, specifying the initial production
version as the value of the tag.

```sqlexample
USE ROLE prod_role;
USE SCHEMA prod_db.prod_schema;

ALTER MODEL model_database.model_schema.my_model
    SET TAG live_version = 'V1';
```

#### Promoting subsequent versions of the model

When a new version of the model is ready, update the `live_version` tag with the name of that version.

```sqlexample
USE ROLE prod_role;

ALTER MODEL model_database.model_schema.my_model
    SET TAG prod_db.prod_schema.live_version = 'V2';
```

#### Using the model in production

Call the production version of the model by retrieving the value of the `live_version` tag from the model using
[SYSTEM$GET_TAG](../../../sql-reference/functions/system_get_tag.md), then calling the model version that has that name. The following SQL
shows this two-step process.

> **Note:**
>
> The SQL domain of models, for use with SYSTEM$GET_TAG, is MODULE.

```sqlexample
-- get production model version from live_version tag
SET live_version = (SELECT
    SYSTEM$GET_TAG('prod_db.prod_schema.live_version', 'my_model', 'MODULE'));

-- call that version
WITH my_version AS MODEL my_model VERSION IDENTIFIER($live_version)
    SELECT my_version!predict(...) ... ;
```

#### Development and testing

For pre-release versions, you can use the same method with additional tags (such as `alpha_version` and
`beta_version`). In many organizations, however, only promotion to production is managed by engineering, and it’s
reasonable to manage pre-release stages using the simpler alias
method.

### Using multiple schemas

You can use multiple schemas to manage lifecycle stages. With this approach, code exclusively calls models in a
designated production schema, which holds only models being used in production. Models in other stages are stored
elsewhere. When a model version is ready for production, it is copied to the production schema. Because the production
models are separate objects with their own access control, you can protect them from accidental modification while
model developers have free rein over models in development stages.

*Use this method when:*

* A role other than the owner of the model promotes models to production.
* You want strong separation between development and production environments.

Note that the role that promotes models to production should have OWNERSHIP or READ privilege on the source model.

#### Initial setup

Create a role (called, for example, `ml_admin`) that has access to both the development and production schemas. In
this example, access to these two environments is encapsulated in existing roles named `model_owner` and
`prod_role`, which contain privileges like USAGE and CREATE MODEL on the development and production schemas,
respectively. The new `ml_admin` role gets the privileges it needs by being granted those roles.

```sqlexample
USE ROLE ACCOUNTADMIN;
CREATE ROLE ml_admin;

USE ROLE model_owner;
GRANT ROLE model_owner TO ROLE ml_admin;

USE ROLE prod_role;
GRANT ROLE prod_role TO ROLE ml_admin;
```

#### Promoting the initial version of the model

Use the `ml_admin` role to copy model versions from the development schema to the production schema, performing the
initial copy using CREATE MODEL … FROM MODEL to copy just the desired version. You can use the same identifier for the
production version or establish a different numbering scheme for production. Here, development version `V12` becomes
production version `V1`.

```sqlexample
USE ROLE ml_admin;

CREATE MODEL prod_db.prod_schema.prod_model WITH VERSION V1
    FROM MODEL dev_db.dev_sch.dev_model VERSION V12;
```

After creating the initial production version of the model, grant USAGE or OWNERSHIP to the production
role based on need.

```sqlexample
USE ROLE ml_admin;

GRANT USAGE ON MODEL my_model TO ROLE prod_role;
```

#### Promoting subsequent versions of the model

When a new version of the model is ready for production, copy just the new model version to the production environment.
Here, development version `V24` becomes production version `V2`. `V2` is then set as the default version.

```sqlexample
USE ROLE ml_admin;

ALTER MODEL prod_db.prod_schema.prod_model ADD VERSION V2
    FROM MODEL dev_db.dev_schema.dev_model VERSION V24;

ALTER MODEL prod_db.prod_schema.prod_model
    SET DEFAULT_VERSION = V2;
```

> **Tip:**
>
> It’s a good idea to keep previous production versions in case you need to roll back, which you can do by
> setting the default version to a previous version, as shown below.
>
> ```sqlexample
> ALTER MODEL prod_db.prod_schema.prod_model SET DEFAULT_VERSION = V1;
> ```
>
> Establish a policy around how many old versions to keep and how long to keep them.

#### Using the model in production

In production, call the default version of the model.

```sqlexample
SELECT prod_model!predict(...) ... ;
```

#### Development and testing

To manage pre-release versions, you could use additional schemas, promoting versions from one stage to the next by
copying them from one schema to the next. If the owner of the model can manage pre-production stages, you could
use a simpler method such as aliases to manage these versions. Using
additional schemas still may be useful to segregate multiple pre-production environments, such as development and
testing, when one or more of these stages is managed by another role.

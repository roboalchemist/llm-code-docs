# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/project-definitions/specify-entities.md

# Specify entities

In the `snowflake.yml` definition file, you can specify multiple entities. Each entity is identified by a unique key. The example below specifies two entities with the `entity_a` and `entity_b` keys:

```yaml
entities:
  entity_a:
    ...
  entity_b:
    ...
```

Each entity has to specify a type. Currently supported types include:

* [function](about.md)
* [procedure](about.md)
* [streamlit](../streamlit-apps/manage-apps/initialize-app.md)
* [application package](../native-apps/project-definitions.md)
* [application](../native-apps/project-definitions.md)

## Entity identifiers

You can specify multiple entities of the same type in the `snowflake.yml` file. You can name entities in the following ways:

* Use a unique key in the entities list.

  The following example shows using `entity_a` and `entity_b` as the unique keys:

  ```yaml
  entities:
    entity_a:
      ...
    entity_b:
      ...
  ```

* Specify an `identifier` name to each entity.

  The following example adds identifier names to the `entity_a` and `entity_b` entities:

  ```yaml
  entities:
    entity_a:
      identifier: entity_a_name
      ...
    entity_b:
      identifier:
        name: entity_a_name
  ```

* Add an `identifier` object to each entity.

  Using identifier objects allow to specify a name, database, and schema for each entity, as shown in the following example:

  ```yaml
  entities:
    entity_b:
      identifier:
        name: entity_a_name
        schema: public
        database: DEV
  ```

If you don’t specify an identifier, the entity key is used as the name of the object, without any database or schema qualification.

## Project mixins

In many cases you might find it useful to define project-wide default values. Mixins provide a way to extract common attributes out of individual entities. You can specify multiple mixins. You need to declare which mixins should be used by each entity using `meta.use_mixins` property.

When using mixins with an entity, you must ensure that all properties of a mixin can be applied to that entity. Applying a property that is not available on an entity causes an error. Consequently, in some cases you might need to use multiple mixins.

> **Note:**
>
> Mixin values are overridden by explicitly-declared entity attributes.

The following example includes two mixins: `stage_mixin` and `snowpark_shared`. The `my_dashboard` entity uses only `stage_mixin`, while the `my_function` entity uses both of the mixins.

```yaml
definition_version: 2
mixins:
  stage_mixin:
    stage: "my_stage"
  snowpark_shared:
    artifacts: ["app/"]
    imports: ["@package_stage/package.zip"]

entities:
  my_function:
    type: "function"
    ...
    meta:
      use_mixins:
        - "stage_mixin"
        - "snowpark_shared"
  my_dashboard:
    type: "dashboard"
    ...
    meta:
      use_mixins:
        - "stage_mixin"
```

If an entity uses multiple mixins that specify the same property, the entity uses the value of later mixin. In the following example, the value of key on the `foo` entity will be `mixin_2_value`.

```yaml
mixins:
  mixin_1:
    key: mixin_1_value
  mixin_2:
    key: mixin_2_value

entities:
  foo:
    meta:
      use_mixin:
      - mixin_1
      - mixin_2
```

The behavior of applying mixins values depends on value type. For scalar values (strings, numbers, Booleans) values are overridden.

| Mixin notation | Explicit result |
| --- | --- |
| ```yaml definition_version: 2 mixins:   mix1:     stage: A    mix2:     stage: B  entities:   test_procedure:     stage: C     meta:       use_mixins:         - mix1         - mix2``` | ```yaml definition_version: 2 entities:   test_procedure:     stage: C``` |

In case of sequences, values are merged to create a new sequence. This implementation avoids creating duplicate entries in the sequence.

| Mixin notation | Explicit result |
| --- | --- |
| ```yaml definition_version: 2 mixins:   mix1:     artifacts:     - a.py    mix2:     artifacts:     - b.py  entities:   test_procedure:     artifacts:       - app/     meta:       use_mixins:         - mix1         - mix2``` | ```yaml definition_version: 2 entities:   test_procedure:     artifacts:       - a.py       - b.py       - app/``` |

For mapping values new keys are being added and existing values are updated. The update is recursive.

| Mixin notation | Explicit result |
| --- | --- |
| ```yaml definition_version: 2 mixins:   mix1:     secrets:       secret1: v1    mix2:     secrets:       secret2: v2  entities:   test_procedure:     secrets:       secret3: v3     meta:       use_mixins:         - mix1         - mix2``` | ```yaml definition_version: 2 entities:   test_procedure:     secrets:       secret1: v1       secret2: v2       secret3: v3``` |
| ```yaml definition_version: 2 mixins:   mix1:     secrets:       secret_name: v1    mix2:     secrets:       secret_name: v2  entities:   test_procedure:     secrets:       secret_name: v3     meta:       use_mixins:         - mix1         - mix2``` | ```yaml definition_version: 2 entities:   test_procedure:     secrets:       secret_name: v3``` |
| ```yaml definition_version: 2 mixins:   shared:     identifier:       schema: foo  entities:   sproc1:     identifier:       name: sproc     meta:       use_mixins: ["shared"]   sproc2:     identifier:       name: sproc       schema: from_entity     meta:       use_mixins: ["shared"]``` | ```yaml definition_version: 2 entities:   sproc1:     identifier:       name: sproc       schema: foo   sproc2:     identifier:       name: sproc       schema: from_entity``` |

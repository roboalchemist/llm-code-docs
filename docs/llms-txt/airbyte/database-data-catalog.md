# Source: https://docs.airbyte.com/platform/understanding-airbyte/database-data-catalog.md

# Source: https://docs.airbyte.com/platform/2.0/understanding-airbyte/database-data-catalog.md

# Source: https://docs.airbyte.com/platform/1.8/understanding-airbyte/database-data-catalog.md

# Source: https://docs.airbyte.com/platform/1.7/understanding-airbyte/database-data-catalog.md

# Source: https://docs.airbyte.com/platform/1.6/understanding-airbyte/database-data-catalog.md

# Airbyte Databases Data Catalog

Copy Page

## Config Database[​](#config-database "Direct link to Config Database")

### `active_declarative_manifest`[​](#active_declarative_manifest "Direct link to active_declarative_manifest")

| Column Name           | Datatype  | Description                                           |
| --------------------- | --------- | ----------------------------------------------------- |
| actor\_definition\_id | UUID      | Primary key. References the `actor_definition` table. |
| version               | BIGINT    | Version of the manifest.                              |
| created\_at           | TIMESTAMP | Timestamp when the record was created.                |
| updated\_at           | TIMESTAMP | Timestamp when the record was last updated.           |

#### Indexes and Constraints[​](#indexes-and-constraints "Direct link to Indexes and Constraints")

* Primary Key: (`actor_definition_id`)
* Foreign Key: `actor_definition_id` references `actor_definition(id)`

***

### `actor`[​](#actor "Direct link to actor")

| Column Name            | Datatype     | Description                                             |
| ---------------------- | ------------ | ------------------------------------------------------- |
| id                     | UUID         | Primary key. Unique identifier for the actor.           |
| workspace\_id          | UUID         | Foreign key referencing the `workspace` table.          |
| actor\_definition\_id  | UUID         | Foreign key referencing `actor_definition` table.       |
| name                   | VARCHAR(256) | Name of the actor.                                      |
| configuration          | JSONB        | Configuration JSON blob specific to the actor.          |
| actor\_type            | ENUM         | Indicates whether the actor is a source or destination. |
| tombstone              | BOOLEAN      | Soft delete flag.                                       |
| created\_at            | TIMESTAMP    | Timestamp when the record was created.                  |
| updated\_at            | TIMESTAMP    | Timestamp when the record was last updated.             |
| resource\_requirements | JSONB        | Defines resource requirements for the actor.            |

#### Indexes and Constraints[​](#indexes-and-constraints-1 "Direct link to Indexes and Constraints")

* Primary Key: (`id`)
* Foreign Key: `workspace_id` references `workspace(id)`
* Foreign Key: `actor_definition_id` references `actor_definition(id)`
* Index: `actor_definition_id_idx` on (`actor_definition_id`)
* Index: `actor_workspace_id_idx` on (`workspace_id`)

***

### `actor_catalog`[​](#actor_catalog "Direct link to actor_catalog")

| Column Name   | Datatype    | Description                                     |
| ------------- | ----------- | ----------------------------------------------- |
| id            | UUID        | Primary key. Unique identifier for the catalog. |
| catalog       | JSONB       | JSON representation of the catalog.             |
| catalog\_hash | VARCHAR(32) | Hash of the catalog for quick comparison.       |
| created\_at   | TIMESTAMP   | Timestamp when the record was created.          |
| modified\_at  | TIMESTAMP   | Timestamp when the record was last modified.    |

#### Indexes and Constraints[​](#indexes-and-constraints-2 "Direct link to Indexes and Constraints")

* Primary Key: (`id`)
* Index: `actor_catalog_catalog_hash_id_idx` on (`catalog_hash`)

***

### `actor_catalog_fetch_event`[​](#actor_catalog_fetch_event "Direct link to actor_catalog_fetch_event")

| Column Name        | Datatype     | Description                                              |
| ------------------ | ------------ | -------------------------------------------------------- |
| id                 | UUID         | Primary key. Unique identifier for the fetch event.      |
| actor\_catalog\_id | UUID         | Foreign key referencing `actor_catalog(id)`.             |
| actor\_id          | UUID         | Foreign key referencing `actor(id)`.                     |
| config\_hash       | VARCHAR(32)  | Hash of the configuration at the time of the fetch.      |
| actor\_version     | VARCHAR(256) | Version of the actor definition when the fetch occurred. |
| created\_at        | TIMESTAMP    | Timestamp when the record was created.                   |
| modified\_at       | TIMESTAMP    | Timestamp when the record was last modified.             |

#### `Indexes and Constraints`[​](#indexes-and-constraints-3 "Direct link to indexes-and-constraints-3")

* Primary Key: (`id`)
* Foreign Key: `actor_catalog_id` references `actor_catalog(id)`
* Foreign Key: `actor_id` references `actor(id)`
* Index: `actor_catalog_fetch_event_actor_catalog_id_idx` on (`actor_catalog_id`)
* Index: `actor_catalog_fetch_event_actor_id_idx` on (`actor_id`)

***

### `actor_definition`[​](#actor_definition "Direct link to actor_definition")

| Column Name                     | Datatype     | Description                                              |
| ------------------------------- | ------------ | -------------------------------------------------------- |
| id                              | UUID         | Primary key. Unique identifier for the actor definition. |
| name                            | VARCHAR(256) | Name of the connector.                                   |
| icon                            | VARCHAR(256) | Icon for the connector.                                  |
| actor\_type                     | ENUM         | Indicates whether the actor is a source or destination.  |
| source\_type                    | ENUM         | Source category (e.g., API, Database).                   |
| created\_at                     | TIMESTAMP    | Timestamp when the record was created.                   |
| updated\_at                     | TIMESTAMP    | Timestamp when the record was last modified.             |
| tombstone                       | BOOLEAN      | Soft delete flag.                                        |
| resource\_requirements          | JSONB        | Defines default resource requirements.                   |
| public                          | BOOLEAN      | Determines if the definition is publicly available.      |
| custom                          | BOOLEAN      | Indicates if the connector is user-defined.              |
| max\_seconds\_between\_messages | INT          | Maximum allowed seconds between messages.                |
| default\_version\_id            | UUID         | Foreign key referencing `actor_definition_version(id)`.  |
| icon\_url                       | VARCHAR(256) | URL of the icon image.                                   |
| metrics                         | JSONB        | Metadata about the connector.                            |
| enterprise                      | BOOLEAN      | Whether the connector is part of the enterprise edition. |

#### Indexes and Constraints[​](#indexes-and-constraints-4 "Direct link to Indexes and Constraints")

* Primary Key: (`id`)
* Foreign Key: `default_version_id` references `actor_definition_version(id)`

***

### `actor_definition_breaking_change`[​](#actor_definition_breaking_change "Direct link to actor_definition_breaking_change")

| Column Name                   | Datatype     | Description                                     |
| ----------------------------- | ------------ | ----------------------------------------------- |
| actor\_definition\_id         | UUID         | Foreign key referencing `actor_definition(id)`. |
| version                       | VARCHAR(256) | Version of the breaking change.                 |
| migration\_documentation\_url | VARCHAR(256) | URL linking to migration documentation.         |
| upgrade\_deadline             | DATE         | Deadline for upgrading to the new version.      |
| message                       | TEXT         | Description of the breaking change.             |
| created\_at                   | TIMESTAMP    | Timestamp when the record was created.          |
| updated\_at                   | TIMESTAMP    | Timestamp when the record was last modified.    |
| scoped\_impact                | JSONB        | JSON object describing the impact scope.        |
| deadline\_action              | VARCHAR(256) | Action required before the deadline.            |

#### Indexes and Constraints[​](#indexes-and-constraints-5 "Direct link to Indexes and Constraints")

* Primary Key: (`actor_definition_id`, `version`)
* Foreign Key: `actor_definition_id` references `actor_definition(id)`

***

### `actor_definition_config_injection`[​](#actor_definition_config_injection "Direct link to actor_definition_config_injection")

| Column Name           | Datatype  | Description                                     |
| --------------------- | --------- | ----------------------------------------------- |
| json\_to\_inject      | JSONB     | JSON configuration to inject.                   |
| injection\_path       | VARCHAR   | Path where the injection applies.               |
| actor\_definition\_id | UUID      | Foreign key referencing `actor_definition(id)`. |
| created\_at           | TIMESTAMP | Timestamp when the record was created.          |
| updated\_at           | TIMESTAMP | Timestamp when the record was last modified.    |

#### Indexes and Constraints[​](#indexes-and-constraints-6 "Direct link to Indexes and Constraints")

* Primary Key: (`actor_definition_id`, `injection_path`)
* Foreign Key: `actor_definition_id` references `actor_definition(id)`

***

### `actor_definition_version`[​](#actor_definition_version "Direct link to actor_definition_version")

| Column Name           | Datatype     | Description                                     |
| --------------------- | ------------ | ----------------------------------------------- |
| id                    | UUID         | Primary key. Unique identifier for the version. |
| actor\_definition\_id | UUID         | Foreign key referencing `actor_definition(id)`. |
| created\_at           | TIMESTAMP    | Timestamp when the record was created.          |
| updated\_at           | TIMESTAMP    | Timestamp when the record was last modified.    |
| documentation\_url    | VARCHAR(256) | Documentation URL for this version.             |
| docker\_repository    | VARCHAR(256) | Docker repository name.                         |
| docker\_image\_tag    | VARCHAR(256) | Docker image tag for this version.              |
| spec                  | JSONB        | Specification JSON blob.                        |

#### Indexes and Constraints[​](#indexes-and-constraints-7 "Direct link to Indexes and Constraints")

* Primary Key: (`id`)
* Foreign Key: `actor_definition_id` references `actor_definition(id)`
* Unique Constraint: `actor_definition_id, docker_image_tag`

***

### `actor_definition_workspace_grant`[​](#actor_definition_workspace_grant "Direct link to actor_definition_workspace_grant")

| Column Name           | Datatype | Description                                     |
| --------------------- | -------- | ----------------------------------------------- |
| actor\_definition\_id | UUID     | Foreign key referencing `actor_definition(id)`. |
| workspace\_id         | UUID     | Foreign key referencing `workspace(id)`.        |
| scope\_id             | UUID     | Scope identifier.                               |

#### Indexes and Constraints[​](#indexes-and-constraints-8 "Direct link to Indexes and Constraints")

* Unique Constraint: `actor_definition_id, scope_id, scope_type`

***

### `actor_oauth_parameter`[​](#actor_oauth_parameter "Direct link to actor_oauth_parameter")

| Column Name           | Datatype | Description                                     |
| --------------------- | -------- | ----------------------------------------------- |
| id                    | UUID     | Primary key. Unique identifier.                 |
| workspace\_id         | UUID     | Foreign key referencing `workspace(id)`.        |
| actor\_definition\_id | UUID     | Foreign key referencing `actor_definition(id)`. |

#### Indexes and Constraints[​](#indexes-and-constraints-9 "Direct link to Indexes and Constraints")

* Primary Key: (`id`)
* Foreign Key: `workspace_id` references `workspace(id)`
* Foreign Key: `actor_definition_id` references `actor_definition(id)`

***

### `airbyte_configs_migrations`[​](#airbyte_configs_migrations "Direct link to airbyte_configs_migrations")

| Column Name     | Datatype      | Description                                     |
| --------------- | ------------- | ----------------------------------------------- |
| installed\_rank | INT           | Primary key. Rank of the installed migration.   |
| version         | VARCHAR(50)   | Version number of the migration.                |
| description     | VARCHAR(200)  | Description of the migration.                   |
| type            | VARCHAR(20)   | Type of migration.                              |
| script          | VARCHAR(1000) | Script executed for the migration.              |
| checksum        | INT           | Checksum of the migration script.               |
| installed\_by   | VARCHAR(100)  | User who installed the migration.               |
| installed\_on   | TIMESTAMP     | Timestamp when the migration was installed.     |
| execution\_time | INT           | Time taken to execute the migration.            |
| success         | BOOLEAN       | Indicates whether the migration was successful. |

#### Indexes and Constraints[​](#indexes-and-constraints-10 "Direct link to Indexes and Constraints")

* Primary Key: (`installed_rank`)

***

### `application`[​](#application "Direct link to application")

| Column Name    | Datatype  | Description                                         |
| -------------- | --------- | --------------------------------------------------- |
| id             | UUID      | Primary key. Unique identifier for the application. |
| user\_id       | UUID      | Foreign key referencing `user(id)`.                 |
| name           | VARCHAR   | Name of the application.                            |
| client\_id     | VARCHAR   | Client ID for authentication.                       |
| client\_secret | VARCHAR   | Secret key for authentication.                      |
| created\_at    | TIMESTAMP | Timestamp when the record was created.              |

#### Indexes and Constraints[​](#indexes-and-constraints-11 "Direct link to Indexes and Constraints")

* Primary Key: (`id`)
* Foreign Key: `user_id` references `user(id)`

***

### `auth_refresh_token`[​](#auth_refresh_token "Direct link to auth_refresh_token")

| Column Name | Datatype  | Description                                   |
| ----------- | --------- | --------------------------------------------- |
| value       | VARCHAR   | Primary key. Refresh token value.             |
| session\_id | VARCHAR   | ID of the session associated with the token.  |
| revoked     | BOOLEAN   | Indicates whether the token has been revoked. |
| created\_at | TIMESTAMP | Timestamp when the record was created.        |
| updated\_at | TIMESTAMP | Timestamp when the record was last modified.  |

#### Indexes and Constraints[​](#indexes-and-constraints-12 "Direct link to Indexes and Constraints")

* Primary Key: (`value`)
* Unique Constraint: (`session_id`, `value`)

***

### `auth_user`[​](#auth_user "Direct link to auth_user")

| Column Name    | Datatype  | Description                                       |
| -------------- | --------- | ------------------------------------------------- |
| id             | UUID      | Primary key. Unique identifier for the auth user. |
| user\_id       | UUID      | Foreign key referencing `user(id)`.               |
| auth\_user\_id | VARCHAR   | ID of the authenticated user.                     |
| auth\_provider | ENUM      | Authentication provider used.                     |
| created\_at    | TIMESTAMP | Timestamp when the record was created.            |
| updated\_at    | TIMESTAMP | Timestamp when the record was last modified.      |

#### Indexes and Constraints[​](#indexes-and-constraints-13 "Direct link to Indexes and Constraints")

* Primary Key: (`id`)
* Foreign Key: `user_id` references `user(id)`
* Unique Constraint: (`auth_user_id`, `auth_provider`)

***

### `connection`[​](#connection "Direct link to connection")

| Column Name            | Datatype  | Description                                        |
| ---------------------- | --------- | -------------------------------------------------- |
| id                     | UUID      | Primary key. Unique identifier for the connection. |
| namespace\_definition  | ENUM      | Defines how the namespace is set.                  |
| namespace\_format      | VARCHAR   | Format for the namespace when using `custom`.      |
| prefix                 | VARCHAR   | Prefix added to destination tables.                |
| source\_id             | UUID      | Foreign key referencing `actor(id)`.               |
| destination\_id        | UUID      | Foreign key referencing `actor(id)`.               |
| name                   | VARCHAR   | Name of the connection.                            |
| catalog                | JSONB     | JSON blob defining the connection catalog.         |
| status                 | ENUM      | Connection status (`active`, `inactive`, etc.).    |
| schedule               | JSONB     | JSON blob defining the connection schedule.        |
| manual                 | BOOLEAN   | Indicates if the connection runs manually.         |
| resource\_requirements | JSONB     | Resource requirements for the connection.          |
| created\_at            | TIMESTAMP | Timestamp when the record was created.             |
| updated\_at            | TIMESTAMP | Timestamp when the record was last modified.       |

#### Indexes and Constraints[​](#indexes-and-constraints-14 "Direct link to Indexes and Constraints")

* Primary Key: (`id`)
* Foreign Key: `source_id` references `actor(id)`
* Foreign Key: `destination_id` references `actor(id)`
* Index: `connection_source_id_idx` on (`source_id`)
* Index: `connection_destination_id_idx` on (`destination_id`)

***

### `connection_operation`[​](#connection_operation "Direct link to connection_operation")

| Column Name    | Datatype  | Description                                    |
| -------------- | --------- | ---------------------------------------------- |
| id             | UUID      | Primary key. Unique identifier for the record. |
| connection\_id | UUID      | Foreign key referencing `connection(id)`.      |
| operation\_id  | UUID      | Foreign key referencing `operation(id)`.       |
| created\_at    | TIMESTAMP | Timestamp when the record was created.         |
| updated\_at    | TIMESTAMP | Timestamp when the record was last modified.   |

#### Indexes and Constraints[​](#indexes-and-constraints-15 "Direct link to Indexes and Constraints")

* Primary Key: (`id`, `connection_id`, `operation_id`)
* Foreign Key: `connection_id` references `connection(id)`
* Foreign Key: `operation_id` references `operation(id)`
* Index: `connection_operation_connection_id_idx` on (`connection_id`)

***

### `connection_tag`[​](#connection_tag "Direct link to connection_tag")

| Column Name    | Datatype  | Description                                    |
| -------------- | --------- | ---------------------------------------------- |
| id             | UUID      | Primary key. Unique identifier for the record. |
| tag\_id        | UUID      | Foreign key referencing `tag(id)`.             |
| connection\_id | UUID      | Foreign key referencing `connection(id)`.      |
| created\_at    | TIMESTAMP | Timestamp when the record was created.         |
| updated\_at    | TIMESTAMP | Timestamp when the record was last modified.   |

#### Indexes and Constraints[​](#indexes-and-constraints-16 "Direct link to Indexes and Constraints")

* Primary Key: (`id`)
* Foreign Key: `tag_id` references `tag(id)`
* Foreign Key: `connection_id` references `connection(id)`
* Unique Constraint: (`tag_id`, `connection_id`)

***

### `connection_timeline_event`[​](#connection_timeline_event "Direct link to connection_timeline_event")

| Column Name    | Datatype  | Description                                   |
| -------------- | --------- | --------------------------------------------- |
| id             | UUID      | Primary key. Unique identifier for the event. |
| connection\_id | UUID      | Foreign key referencing `connection(id)`.     |
| user\_id       | UUID      | Foreign key referencing `user(id)`.           |
| event\_type    | VARCHAR   | Type of event that occurred.                  |
| summary        | JSONB     | JSON blob containing event details.           |
| created\_at    | TIMESTAMP | Timestamp when the event occurred.            |

#### Indexes and Constraints[​](#indexes-and-constraints-17 "Direct link to Indexes and Constraints")

* Primary Key: (`id`)
* Foreign Key: `connection_id` references `connection(id)`
* Foreign Key: `user_id` references `user(id)`
* Index: `idx_connection_timeline_connection_id` on (`connection_id`, `created_at`, `event_type`)

***

### `connector_builder_project`[​](#connector_builder_project "Direct link to connector_builder_project")

| Column Name                          | Datatype  | Description                                             |
| ------------------------------------ | --------- | ------------------------------------------------------- |
| id                                   | UUID      | Primary key. Unique identifier for the project.         |
| workspace\_id                        | UUID      | Foreign key referencing `workspace(id)`.                |
| name                                 | VARCHAR   | Name of the connector project.                          |
| manifest\_draft                      | JSONB     | JSON draft of the connector manifest.                   |
| actor\_definition\_id                | UUID      | Foreign key referencing `actor_definition(id)`.         |
| tombstone                            | BOOLEAN   | Indicates if the project is deleted.                    |
| created\_at                          | TIMESTAMP | Timestamp when the record was created.                  |
| updated\_at                          | TIMESTAMP | Timestamp when the record was last modified.            |
| testing\_values                      | JSONB     | JSON containing test values for the connector.          |
| base\_actor\_definition\_version\_id | UUID      | Foreign key referencing `actor_definition_version(id)`. |
| contribution\_pull\_request\_url     | VARCHAR   | URL for the contribution PR.                            |
| contribution\_actor\_definition\_id  | UUID      | Foreign key referencing `actor_definition(id)`.         |
| components\_file\_content            | TEXT      | Raw content of component files.                         |

#### Indexes and Constraints[​](#indexes-and-constraints-18 "Direct link to Indexes and Constraints")

* Primary Key: (`id`)
* Foreign Key: `workspace_id` references `workspace(id)`
* Foreign Key: `actor_definition_id` references `actor_definition(id)`
* Foreign Key: `base_actor_definition_version_id` references `actor_definition_version(id)`
* Foreign Key: `contribution_actor_definition_id` references `actor_definition(id)`
* Index: `connector_builder_project_workspace_idx` on (`workspace_id`)

***

### `connector_rollout`[​](#connector_rollout "Direct link to connector_rollout")

| Column Name                     | Datatype  | Description                                             |
| ------------------------------- | --------- | ------------------------------------------------------- |
| id                              | UUID      | Primary key. Unique identifier for the rollout.         |
| actor\_definition\_id           | UUID      | Foreign key referencing `actor_definition(id)`.         |
| release\_candidate\_version\_id | UUID      | Foreign key referencing `actor_definition_version(id)`. |
| initial\_version\_id            | UUID      | Foreign key referencing `actor_definition_version(id)`. |
| state                           | VARCHAR   | Current state of the rollout.                           |
| initial\_rollout\_pct           | INT       | Initial rollout percentage.                             |
| current\_target\_rollout\_pct   | INT       | Current target rollout percentage.                      |
| final\_target\_rollout\_pct     | INT       | Final target rollout percentage.                        |
| has\_breaking\_changes          | BOOLEAN   | Indicates if the rollout has breaking changes.          |
| max\_step\_wait\_time\_mins     | INT       | Maximum wait time between rollout steps.                |
| updated\_by                     | UUID      | Foreign key referencing `user(id)`.                     |
| created\_at                     | TIMESTAMP | Timestamp when the rollout started.                     |
| updated\_at                     | TIMESTAMP | Timestamp when the record was last modified.            |
| completed\_at                   | TIMESTAMP | Timestamp when the rollout was completed.               |
| expires\_at                     | TIMESTAMP | Timestamp when the rollout expires.                     |
| error\_msg                      | VARCHAR   | Error message if the rollout failed.                    |
| failed\_reason                  | VARCHAR   | Reason for failure.                                     |
| rollout\_strategy               | VARCHAR   | Strategy used for the rollout.                          |
| workflow\_run\_id               | VARCHAR   | Workflow run identifier.                                |
| paused\_reason                  | VARCHAR   | Reason for pausing the rollout.                         |

#### Indexes and Constraints[​](#indexes-and-constraints-19 "Direct link to Indexes and Constraints")

* Primary Key: (`id`)
* Foreign Key: `actor_definition_id` references `actor_definition(id)`
* Foreign Key: `release_candidate_version_id` references `actor_definition_version(id)`
* Foreign Key: `initial_version_id` references `actor_definition_version(id)`
* Foreign Key: `updated_by` references `user(id)`
* Unique Index: `actor_definition_id_state_unique_idx` on `actor_definition_id`
  * Condition: (`state` in \['errored', 'finalizing', 'in\_progress', 'initialized', 'paused', 'workflow\_started'])

***

### `dataplane`[​](#dataplane "Direct link to dataplane")

| Column Name          | Datatype  | Description                                       |
| -------------------- | --------- | ------------------------------------------------- |
| id                   | UUID      | Primary key. Unique identifier for the dataplane. |
| dataplane\_group\_id | UUID      | Foreign key referencing `dataplane_group(id)`.    |
| name                 | VARCHAR   | Name of the dataplane.                            |
| enabled              | BOOLEAN   | Indicates if the dataplane is enabled.            |
| created\_at          | TIMESTAMP | Timestamp when the record was created.            |
| updated\_at          | TIMESTAMP | Timestamp when the record was last modified.      |
| updated\_by          | UUID      | Foreign key referencing `user(id)`.               |
| tombstone            | BOOLEAN   | Indicates if the record is deleted.               |

#### Indexes and Constraints[​](#indexes-and-constraints-20 "Direct link to Indexes and Constraints")

* Primary Key: (`id`)
* Foreign Key: `dataplane_group_id` references `dataplane_group(id)`
* Foreign Key: `updated_by` references `user(id)`
* Unique Constraint: (`dataplane_group_id`, `name`)

***

### `dataplane_group`[​](#dataplane_group "Direct link to dataplane_group")

| Column Name      | Datatype  | Description                                   |
| ---------------- | --------- | --------------------------------------------- |
| id               | UUID      | Primary key. Unique identifier for the group. |
| organization\_id | UUID      | Foreign key referencing `organization(id)`.   |
| name             | VARCHAR   | Name of the dataplane group.                  |
| enabled          | BOOLEAN   | Indicates if the group is enabled.            |
| created\_at      | TIMESTAMP | Timestamp when the record was created.        |
| updated\_at      | TIMESTAMP | Timestamp when the record was last modified.  |
| updated\_by      | UUID      | Foreign key referencing `user(id)`.           |
| tombstone        | BOOLEAN   | Indicates if the record is deleted.           |

#### Indexes and Constraints[​](#indexes-and-constraints-21 "Direct link to Indexes and Constraints")

* Primary Key: (`id`)
* Foreign Key: `organization_id` references `organization(id)`
* Foreign Key: `updated_by` references `user(id)`
* Unique Constraint: (`organization_id`, `name`)

***

### `declarative_manifest`[​](#declarative_manifest "Direct link to declarative_manifest")

| Column Name           | Datatype  | Description                                     |
| --------------------- | --------- | ----------------------------------------------- |
| actor\_definition\_id | UUID      | Foreign key referencing `actor_definition(id)`. |
| description           | VARCHAR   | Description of the manifest.                    |
| manifest              | JSONB     | JSON representation of the manifest.            |
| spec                  | JSONB     | JSON specification for the manifest.            |
| version               | BIGINT    | Version number of the manifest.                 |
| created\_at           | TIMESTAMP | Timestamp when the record was created.          |

#### Indexes and Constraints[​](#indexes-and-constraints-22 "Direct link to Indexes and Constraints")

* Primary Key: (`actor_definition_id`, `version`)

***

### `declarative_manifest_image_version`[​](#declarative_manifest_image_version "Direct link to declarative_manifest_image_version")

| Column Name    | Datatype  | Description                                  |
| -------------- | --------- | -------------------------------------------- |
| major\_version | INT       | Primary key. Major version number.           |
| image\_version | VARCHAR   | Version of the image.                        |
| created\_at    | TIMESTAMP | Timestamp when the record was created.       |
| updated\_at    | TIMESTAMP | Timestamp when the record was last modified. |
| image\_sha     | VARCHAR   | SHA checksum of the image.                   |

#### Indexes and Constraints[​](#indexes-and-constraints-23 "Direct link to Indexes and Constraints")

* Primary Key: (`major_version`)

***

### `notification_configuration`[​](#notification_configuration "Direct link to notification_configuration")

| Column Name        | Datatype  | Description                                                        |
| ------------------ | --------- | ------------------------------------------------------------------ |
| id                 | UUID      | Primary key. Unique identifier for the notification configuration. |
| enabled            | BOOLEAN   | Indicates if the notification is enabled.                          |
| notification\_type | ENUM      | Type of notification.                                              |
| connection\_id     | UUID      | Foreign key referencing `connection(id)`.                          |
| created\_at        | TIMESTAMP | Timestamp when the record was created.                             |
| updated\_at        | TIMESTAMP | Timestamp when the record was last modified.                       |

#### Indexes and Constraints[​](#indexes-and-constraints-24 "Direct link to Indexes and Constraints")

* Primary Key: (`id`)
* Foreign Key: `connection_id` references `connection(id)`

***

### `operation`[​](#operation "Direct link to operation")

| Column Name             | Datatype  | Description                                       |
| ----------------------- | --------- | ------------------------------------------------- |
| id                      | UUID      | Primary key. Unique identifier for the operation. |
| workspace\_id           | UUID      | Foreign key referencing `workspace(id)`.          |
| name                    | VARCHAR   | Name of the operation.                            |
| operator\_type          | ENUM      | Type of operator (`dbt`, `normalization`, etc.).  |
| operator\_normalization | JSONB     | JSON blob defining normalization settings.        |
| operator\_dbt           | JSONB     | JSON blob defining dbt settings.                  |
| tombstone               | BOOLEAN   | Indicates if the operation is deleted.            |
| created\_at             | TIMESTAMP | Timestamp when the record was created.            |
| updated\_at             | TIMESTAMP | Timestamp when the record was last modified.      |
| operator\_webhook       | JSONB     | JSON blob defining webhook settings.              |

#### Indexes and Constraints[​](#indexes-and-constraints-25 "Direct link to Indexes and Constraints")

* Primary Key: (`id`)
* Foreign Key: `workspace_id` references `workspace(id)`

***

### `organization`[​](#organization "Direct link to organization")

| Column Name | Datatype  | Description                                          |
| ----------- | --------- | ---------------------------------------------------- |
| id          | UUID      | Primary key. Unique identifier for the organization. |
| name        | VARCHAR   | Name of the organization.                            |
| user\_id    | UUID      | Foreign key referencing `user(id)`.                  |
| email       | VARCHAR   | Contact email for the organization.                  |
| created\_at | TIMESTAMP | Timestamp when the record was created.               |
| updated\_at | TIMESTAMP | Timestamp when the record was last modified.         |
| tombstone   | BOOLEAN   | Indicates if the organization is deleted.            |

#### Indexes and Constraints[​](#indexes-and-constraints-26 "Direct link to Indexes and Constraints")

* Primary Key: (`id`)
* Foreign Key: `user_id` references `user(id)`

***

### `organization_email_domain`[​](#organization_email_domain "Direct link to organization_email_domain")

| Column Name      | Datatype  | Description                                    |
| ---------------- | --------- | ---------------------------------------------- |
| id               | UUID      | Primary key. Unique identifier for the record. |
| organization\_id | UUID      | Foreign key referencing `organization(id)`.    |
| email\_domain    | VARCHAR   | Email domain associated with the organization. |
| created\_at      | TIMESTAMP | Timestamp when the record was created.         |

#### Indexes and Constraints[​](#indexes-and-constraints-27 "Direct link to Indexes and Constraints")

* Primary Key: (`id`)
* Foreign Key: `organization_id` references `organization(id)`
* Unique Constraint: (`organization_id`, `email_domain`)
* Index: `organization_email_domain_organization_id_idx` on (`organization_id`)

***

### `organization_payment_config`[​](#organization_payment_config "Direct link to organization_payment_config")

| Column Name               | Datatype  | Description                                                                |
| ------------------------- | --------- | -------------------------------------------------------------------------- |
| organization\_id          | UUID      | Primary key. Unique identifier for the organization payment configuration. |
| payment\_provider\_id     | VARCHAR   | Payment provider ID.                                                       |
| payment\_status           | ENUM      | Status of the organization's payment.                                      |
| grace\_period\_end\_at    | TIMESTAMP | End timestamp for the grace period.                                        |
| usage\_category\_override | ENUM      | Override for usage category.                                               |
| created\_at               | TIMESTAMP | Timestamp when the record was created.                                     |
| updated\_at               | TIMESTAMP | Timestamp when the record was last modified.                               |
| subscription\_status      | ENUM      | Status of the organization's subscription.                                 |

#### Indexes and Constraints[​](#indexes-and-constraints-28 "Direct link to Indexes and Constraints")

* Primary Key: (`organization_id`)
* Unique Constraint: (`payment_provider_id`)
* Foreign Key: `organization_id` references `organization(id)`
* Index: `organization_payment_config_payment_status_idx` on (`payment_status`)
* Index: `organization_payment_config_payment_provider_id_idx` on (`payment_provider_id`)

***

### `permission`[​](#permission "Direct link to permission")

| Column Name      | Datatype  | Description                                        |
| ---------------- | --------- | -------------------------------------------------- |
| id               | UUID      | Primary key. Unique identifier for the permission. |
| user\_id         | UUID      | Foreign key referencing `user(id)`.                |
| workspace\_id    | UUID      | Foreign key referencing `workspace(id)`.           |
| created\_at      | TIMESTAMP | Timestamp when the record was created.             |
| updated\_at      | TIMESTAMP | Timestamp when the record was last modified.       |
| organization\_id | UUID      | Foreign key referencing `organization(id)`.        |
| permission\_type | ENUM      | Type of permission assigned.                       |

#### Indexes and Constraints[​](#indexes-and-constraints-29 "Direct link to Indexes and Constraints")

* Primary Key: (`id`)
* Foreign Key: `user_id` references `user(id)`
* Foreign Key: `workspace_id` references `workspace(id)`
* Foreign Key: `organization_id` references `organization(id)`
* Unique Constraint: (`user_id`, `organization_id`)
* Unique Constraint: (`user_id`, `workspace_id`)
* Index: `permission_organization_id_idx` on (`organization_id`)
* Index: `permission_workspace_id_idx` on (`workspace_id`)

***

### `schema_management`[​](#schema_management "Direct link to schema_management")

| Column Name               | Datatype  | Description                                           |
| ------------------------- | --------- | ----------------------------------------------------- |
| id                        | UUID      | Primary key. Unique identifier for schema management. |
| connection\_id            | UUID      | Foreign key referencing `connection(id)`.             |
| created\_at               | TIMESTAMP | Timestamp when the record was created.                |
| updated\_at               | TIMESTAMP | Timestamp when the record was last modified.          |
| auto\_propagation\_status | ENUM      | Status of automatic schema propagation.               |
| backfill\_preference      | ENUM      | User preference for backfill operations.              |

#### Indexes and Constraints[​](#indexes-and-constraints-30 "Direct link to Indexes and Constraints")

* Primary Key: (`id`)
* Foreign Key: `connection_id` references `connection(id)`
* Index: `connection_idx` on (`connection_id`)

***

### `scoped_configuration`[​](#scoped_configuration "Direct link to scoped_configuration")

| Column Name    | Datatype  | Description                                                  |
| -------------- | --------- | ------------------------------------------------------------ |
| id             | UUID      | Primary key. Unique identifier for the scoped configuration. |
| key            | VARCHAR   | Configuration key.                                           |
| resource\_type | ENUM      | Type of resource associated with the configuration.          |
| resource\_id   | UUID      | Identifier of the associated resource.                       |
| scope\_type    | ENUM      | Type of scope (e.g., workspace, organization).               |
| scope\_id      | UUID      | Identifier for the scope of the configuration.               |
| value          | VARCHAR   | Value of the configuration.                                  |
| description    | TEXT      | Description of the configuration setting.                    |
| reference\_url | VARCHAR   | URL reference for more information.                          |
| origin\_type   | ENUM      | Type of origin for the configuration setting.                |
| origin         | VARCHAR   | Source of the configuration setting.                         |
| expires\_at    | DATE      | Expiration date of the configuration.                        |
| created\_at    | TIMESTAMP | Timestamp when the record was created.                       |
| updated\_at    | TIMESTAMP | Timestamp when the record was last modified.                 |

#### Indexes and Constraints[​](#indexes-and-constraints-31 "Direct link to Indexes and Constraints")

* Primary Key: (`id`)
* Unique Constraint: (`key`, `resource_type`, `resource_id`, `scope_type`, `scope_id`)

***

### `secret_persistence_config`[​](#secret_persistence_config "Direct link to secret_persistence_config")

| Column Name                             | Datatype  | Description                                                          |
| --------------------------------------- | --------- | -------------------------------------------------------------------- |
| id                                      | UUID      | Primary key. Unique identifier for secret persistence configuration. |
| scope\_id                               | UUID      | Identifier for the scope of the secret.                              |
| scope\_type                             | ENUM      | Scope type (`organization`, `workspace`, etc.).                      |
| secret\_persistence\_config\_coordinate | VARCHAR   | Coordinate for secret persistence configuration.                     |
| secret\_persistence\_type               | ENUM      | Type of secret persistence method.                                   |
| created\_at                             | TIMESTAMP | Timestamp when the record was created.                               |
| updated\_at                             | TIMESTAMP | Timestamp when the record was last modified.                         |

#### Indexes and Constraints[​](#indexes-and-constraints-32 "Direct link to Indexes and Constraints")

* Primary Key: (`id`)
* Unique Constraint: (`scope_id`, `scope_type`)

***

### `sso_config`[​](#sso_config "Direct link to sso_config")

| Column Name      | Datatype  | Description                                               |
| ---------------- | --------- | --------------------------------------------------------- |
| id               | UUID      | Primary key. Unique identifier for the SSO configuration. |
| organization\_id | UUID      | Foreign key referencing `organization(id)`.               |
| keycloak\_realm  | VARCHAR   | Keycloak realm associated with the organization.          |
| created\_at      | TIMESTAMP | Timestamp when the record was created.                    |
| updated\_at      | TIMESTAMP | Timestamp when the record was last modified.              |

#### Indexes and Constraints[​](#indexes-and-constraints-33 "Direct link to Indexes and Constraints")

* Primary Key: (`id`)
* Foreign Key: `organization_id` references `organization(id)`
* Unique Constraint: (`keycloak_realm`)
* Unique Constraint: (`organization_id`)
* Index: `sso_config_keycloak_realm_idx` on (`keycloak_realm`)
* Index: `sso_config_organization_id_idx` on (`organization_id`)

***

### `state`[​](#state "Direct link to state")

| Column Name    | Datatype  | Description                                          |
| -------------- | --------- | ---------------------------------------------------- |
| id             | UUID      | Primary key. Unique identifier for the state record. |
| connection\_id | UUID      | Foreign key referencing `connection(id)`.            |
| state          | JSONB     | JSON blob storing the state information.             |
| created\_at    | TIMESTAMP | Timestamp when the record was created.               |
| updated\_at    | TIMESTAMP | Timestamp when the record was last modified.         |
| stream\_name   | TEXT      | Name of the stream associated with this state.       |
| namespace      | TEXT      | Namespace of the stream.                             |
| type           | ENUM      | Type of state (`STREAM`, `GLOBAL`, `LEGACY`).        |

#### Indexes and Constraints[​](#indexes-and-constraints-34 "Direct link to Indexes and Constraints")

* Primary Key: (`id`, `connection_id`)
* Foreign Key: `connection_id` references `connection(id)`
* Unique Constraint: (`connection_id`, `stream_name`, `namespace`)

***

### `stream_generation`[​](#stream_generation "Direct link to stream_generation")

| Column Name       | Datatype  | Description                                                      |
| ----------------- | --------- | ---------------------------------------------------------------- |
| id                | UUID      | Primary key. Unique identifier for the stream generation record. |
| connection\_id    | UUID      | Foreign key referencing `connection(id)`.                        |
| stream\_name      | VARCHAR   | Name of the stream.                                              |
| stream\_namespace | VARCHAR   | Namespace of the stream.                                         |
| generation\_id    | BIGINT    | Identifier for the stream generation.                            |
| start\_job\_id    | BIGINT    | Job ID that started this stream generation.                      |
| created\_at       | TIMESTAMP | Timestamp when the record was created.                           |
| updated\_at       | TIMESTAMP | Timestamp when the record was last modified.                     |

#### Indexes and Constraints[​](#indexes-and-constraints-35 "Direct link to Indexes and Constraints")

* Primary Key: (`id`)
* Foreign Key: `connection_id` references `connection(id)`
* Index: `stream_generation_connection_id_stream_name_generation_id_idx` on (`connection_id`, `stream_name`, `generation_id`)
* Index: `stream_generation_connection_id_stream_name_stream_namespace_idx` on (`connection_id`, `stream_name`, `stream_namespace`, `generation_id`)

***

### `stream_refreshes`[​](#stream_refreshes "Direct link to stream_refreshes")

| Column Name       | Datatype  | Description                                                   |
| ----------------- | --------- | ------------------------------------------------------------- |
| id                | UUID      | Primary key. Unique identifier for the stream refresh record. |
| connection\_id    | UUID      | Foreign key referencing `connection(id)`.                     |
| stream\_name      | VARCHAR   | Name of the stream.                                           |
| stream\_namespace | VARCHAR   | Namespace of the stream.                                      |
| created\_at       | TIMESTAMP | Timestamp when the record was created.                        |
| refresh\_type     | ENUM      | Type of refresh operation performed.                          |

#### Indexes and Constraints[​](#indexes-and-constraints-36 "Direct link to Indexes and Constraints")

* Primary Key: (`id`)
* Foreign Key: `connection_id` references `connection(id)`
* Index: `stream_refreshes_connection_id_idx` on (`connection_id`)
* Index: `stream_refreshes_connection_id_stream_name_idx` on (`connection_id`, `stream_name`)
* Index: `stream_refreshes_connection_id_stream_name_stream_namespace_idx` on (`connection_id`, `stream_name`, `stream_namespace`)

***

### `stream_reset`[​](#stream_reset "Direct link to stream_reset")

| Column Name       | Datatype  | Description                                                 |
| ----------------- | --------- | ----------------------------------------------------------- |
| id                | UUID      | Primary key. Unique identifier for the stream reset record. |
| connection\_id    | UUID      | Foreign key referencing `connection(id)`.                   |
| stream\_namespace | TEXT      | Namespace of the stream.                                    |
| stream\_name      | TEXT      | Name of the stream being reset.                             |
| created\_at       | TIMESTAMP | Timestamp when the record was created.                      |
| updated\_at       | TIMESTAMP | Timestamp when the record was last modified.                |

#### Indexes and Constraints[​](#indexes-and-constraints-37 "Direct link to Indexes and Constraints")

* Primary Key: (`id`)
* Foreign Key: `connection_id` references `connection(id)`
* Unique Constraint: (`connection_id`, `stream_name`, `stream_namespace`)
* Index: `connection_id_stream_name_namespace_idx` on (`connection_id`, `stream_name`, `stream_namespace`)

***

### `tag`[​](#tag "Direct link to tag")

| Column Name   | Datatype  | Description                                  |
| ------------- | --------- | -------------------------------------------- |
| id            | UUID      | Primary key. Unique identifier for the tag.  |
| workspace\_id | UUID      | Foreign key referencing `workspace(id)`.     |
| name          | VARCHAR   | Name of the tag.                             |
| color         | CHAR(6)   | Hexadecimal color code for the tag.          |
| created\_at   | TIMESTAMP | Timestamp when the record was created.       |
| updated\_at   | TIMESTAMP | Timestamp when the record was last modified. |

#### Indexes and Constraints[​](#indexes-and-constraints-38 "Direct link to Indexes and Constraints")

* Primary Key: (`id`)
* Foreign Key: `workspace_id` references `workspace(id)`
* Unique Constraint: (`name`, `workspace_id`)
* Index: `tag_workspace_id_idx` on (`workspace_id`)

***

### `user`[​](#user "Direct link to user")

| Column Name            | Datatype  | Description                                   |
| ---------------------- | --------- | --------------------------------------------- |
| id                     | UUID      | Primary key. Unique identifier for the user.  |
| name                   | VARCHAR   | Name of the user.                             |
| default\_workspace\_id | UUID      | Foreign key referencing `workspace(id)`.      |
| status                 | ENUM      | Status of the user account.                   |
| company\_name          | VARCHAR   | Name of the company associated with the user. |
| email                  | VARCHAR   | Email address of the user.                    |
| news                   | BOOLEAN   | Whether the user subscribes to newsletters.   |
| ui\_metadata           | JSONB     | UI metadata associated with the user.         |
| created\_at            | TIMESTAMP | Timestamp when the record was created.        |
| updated\_at            | TIMESTAMP | Timestamp when the record was last modified.  |

#### Indexes and Constraints[​](#indexes-and-constraints-39 "Direct link to Indexes and Constraints")

* Primary Key: (`id`)
* Foreign Key: `default_workspace_id` references `workspace(id)`
* Unique Constraint: (`email`)
* Index: `user_email_idx` on (`email`)
* Unique Index: `user_email_unique_key` on `lower(email)`

***

### `user_invitation`[​](#user_invitation "Direct link to user_invitation")

| Column Name            | Datatype  | Description                                             |
| ---------------------- | --------- | ------------------------------------------------------- |
| id                     | UUID      | Primary key. Unique identifier for the invitation.      |
| invite\_code           | VARCHAR   | Unique code for the invitation.                         |
| inviter\_user\_id      | UUID      | Foreign key referencing `user(id)`.                     |
| invited\_email         | VARCHAR   | Email of the invited user.                              |
| permission\_type       | ENUM      | Type of permission granted to the invited user.         |
| status                 | ENUM      | Status of the invitation (`pending`, `accepted`, etc.). |
| created\_at            | TIMESTAMP | Timestamp when the record was created.                  |
| updated\_at            | TIMESTAMP | Timestamp when the record was last modified.            |
| scope\_id              | UUID      | Scope ID for the invitation.                            |
| scope\_type            | ENUM      | Type of scope (`organization`, `workspace`, etc.).      |
| accepted\_by\_user\_id | UUID      | Foreign key referencing `user(id)`.                     |
| expires\_at            | TIMESTAMP | Expiration timestamp of the invitation.                 |

#### Indexes and Constraints[​](#indexes-and-constraints-40 "Direct link to Indexes and Constraints")

* Primary Key: (`id`)
* Foreign Key: `inviter_user_id` references `user(id)`
* Foreign Key: `accepted_by_user_id` references `user(id)`
* Unique Constraint: (`invite_code`)
* Index: `user_invitation_invite_code_idx` on (`invite_code`)
* Index: `user_invitation_invited_email_idx` on (`invited_email`)
* Index: `user_invitation_scope_id_index` on (`scope_id`)
* Index: `user_invitation_scope_type_and_scope_id_index` on (`scope_type`, `scope_id`)
* Index: `user_invitation_accepted_by_user_id_index` on (`accepted_by_user_id`)
* Index: `user_invitation_expires_at_index` on (`expires_at`)

***

### `workload`[​](#workload "Direct link to workload")

| Column Name         | Datatype  | Description                                          |
| ------------------- | --------- | ---------------------------------------------------- |
| id                  | VARCHAR   | Primary key. Unique identifier for the workload.     |
| dataplane\_id       | VARCHAR   | Identifier for the dataplane handling this workload. |
| status              | ENUM      | Status of the workload (`pending`, `running`, etc.). |
| created\_at         | TIMESTAMP | Timestamp when the record was created.               |
| updated\_at         | TIMESTAMP | Timestamp when the record was last modified.         |
| last\_heartbeat\_at | TIMESTAMP | Timestamp of the last heartbeat received.            |
| input\_payload      | TEXT      | Payload associated with the workload.                |
| log\_path           | TEXT      | Path to logs for the workload.                       |
| geography           | VARCHAR   | Geography associated with the workload.              |
| mutex\_key          | VARCHAR   | Mutex key used for workload execution control.       |
| type                | ENUM      | Type of workload being processed.                    |
| termination\_source | VARCHAR   | Source that terminated the workload.                 |
| termination\_reason | TEXT      | Reason for workload termination.                     |
| auto\_id            | UUID      | Auto-generated identifier for the workload.          |
| deadline            | TIMESTAMP | Deadline for workload execution.                     |
| signal\_input       | TEXT      | Signal input for the workload.                       |
| dataplane\_group    | VARCHAR   | Dataplane group associated with the workload.        |
| priority            | INT       | Priority level of the workload.                      |

#### Indexes and Constraints[​](#indexes-and-constraints-41 "Direct link to Indexes and Constraints")

* Primary Key: (`id`)
* Index: `active_workload_by_mutex_idx` on (`mutex_key`) where (`status` is active)
* Index: `workload_deadline_idx` on (`deadline`) where (`deadline IS NOT NULL`)
* Index: `workload_mutex_idx` on (`mutex_key`)
* Index: `workload_status_idx` on (`status`)

***

### `workload_label`[​](#workload_label "Direct link to workload_label")

| Column Name  | Datatype | Description                                   |
| ------------ | -------- | --------------------------------------------- |
| id           | UUID     | Primary key. Unique identifier for the label. |
| workload\_id | VARCHAR  | Foreign key referencing `workload(id)`.       |
| key          | VARCHAR  | Label key.                                    |
| value        | VARCHAR  | Label value.                                  |

#### Indexes and Constraints[​](#indexes-and-constraints-42 "Direct link to Indexes and Constraints")

* Primary Key: (`id`)
* Foreign Key: `workload_id` references `workload(id)`
* Unique Constraint: (`workload_id`, `key`)
* Index: `workload_label_workload_id_idx` on (`workload_id`)

***

### `workspace`[​](#workspace "Direct link to workspace")

| Column Name                 | Datatype  | Description                                       |
| --------------------------- | --------- | ------------------------------------------------- |
| id                          | UUID      | Primary key. Unique identifier for the workspace. |
| customer\_id                | UUID      | Customer associated with the workspace.           |
| name                        | VARCHAR   | Name of the workspace.                            |
| slug                        | VARCHAR   | Slug identifier for the workspace.                |
| email                       | VARCHAR   | Contact email for the workspace.                  |
| initial\_setup\_complete    | BOOLEAN   | Whether the initial setup is complete.            |
| anonymous\_data\_collection | BOOLEAN   | Whether anonymous data collection is enabled.     |
| send\_newsletter            | BOOLEAN   | Whether the user is subscribed to newsletters.    |
| send\_security\_updates     | BOOLEAN   | Whether security updates are sent.                |
| display\_setup\_wizard      | BOOLEAN   | Whether the setup wizard should be displayed.     |
| tombstone                   | BOOLEAN   | Whether the workspace is deleted.                 |
| notifications               | JSONB     | Notification settings.                            |
| first\_sync\_complete       | BOOLEAN   | Whether the first sync has completed.             |
| feedback\_complete          | BOOLEAN   | Whether feedback collection is completed.         |
| created\_at                 | TIMESTAMP | Timestamp when the record was created.            |
| updated\_at                 | TIMESTAMP | Timestamp when the record was last modified.      |
| geography                   | ENUM      | Geography associated with the workspace.          |
| webhook\_operation\_configs | JSONB     | Webhook operation configurations.                 |
| notification\_settings      | JSONB     | Notification settings for the workspace.          |
| organization\_id            | UUID      | Foreign key referencing `organization(id)`.       |

#### Indexes and Constraints[​](#indexes-and-constraints-43 "Direct link to Indexes and Constraints")

* Primary Key: (`id`)
* Foreign Key: `organization_id` references `organization(id)`

***

### `workspace_service_account`[​](#workspace_service_account "Direct link to workspace_service_account")

| Column Name             | Datatype  | Description                                  |
| ----------------------- | --------- | -------------------------------------------- |
| workspace\_id           | UUID      | Foreign key referencing `workspace(id)`.     |
| service\_account\_id    | VARCHAR   | Service account ID.                          |
| service\_account\_email | VARCHAR   | Email associated with the service account.   |
| json\_credential        | JSONB     | JSON blob storing credentials.               |
| hmac\_key               | JSONB     | JSON blob storing HMAC keys.                 |
| created\_at             | TIMESTAMP | Timestamp when the record was created.       |
| updated\_at             | TIMESTAMP | Timestamp when the record was last modified. |

#### Indexes and Constraints[​](#indexes-and-constraints-44 "Direct link to Indexes and Constraints")

* Primary Key: (`workspace_id`, `service_account_id`)
* Foreign Key: `workspace_id` references `workspace(id)`

## Jobs Database[​](#jobs-database "Direct link to Jobs Database")

### `jobs`[​](#jobs "Direct link to jobs")

| Column Name    | Datatype                      | Description                                                         |
| -------------- | ----------------------------- | ------------------------------------------------------------------- |
| `id`           | `bigint`                      | Primary key, uniquely identifies a job.                             |
| `config_type`  | `job_config_type`             | Type of job (`sync`, `reset`).                                      |
| `scope`        | `varchar(255)`                | Identifier for the connection or scope of the job.                  |
| `config`       | `jsonb`                       | JSON blob containing job configuration.                             |
| `status`       | `job_status`                  | Current status of the job (`running`, `failed`, `succeeded`, etc.). |
| `started_at`   | `timestamp(6) with time zone` | Timestamp when the job started.                                     |
| `created_at`   | `timestamp(6) with time zone` | Timestamp when the job was created.                                 |
| `updated_at`   | `timestamp(6) with time zone` | Timestamp when the job was last updated.                            |
| `metadata`     | `jsonb`                       | JSON blob containing metadata for the job.                          |
| `is_scheduled` | `boolean`                     | Whether the job was scheduled automatically (default: `true`).      |

#### Indexes & Constraints[​](#indexes--constraints "Direct link to Indexes & Constraints")

* Primary Key: `id`

* Indexes:

  <!-- -->

  * `jobs_config_type_idx` → (`config_type`)
  * `jobs_scope_idx` → (`scope`)
  * `jobs_status_idx` → (`status`)
  * `jobs_updated_at_idx` → (`updated_at`)
  * `scope_created_at_idx` → (`scope`, `created_at` DESC)
  * `scope_non_terminal_status_idx` → (`scope`, `status`) (only for non-terminal statuses: not `failed`, `succeeded`, or `cancelled`)

***

### `attempts`[​](#attempts "Direct link to attempts")

| Column Name             | Datatype                      | Description                                               |
| ----------------------- | ----------------------------- | --------------------------------------------------------- |
| `id`                    | `bigint`                      | Primary key, uniquely identifies an attempt.              |
| `job_id`                | `bigint`                      | Foreign key to `jobs(id)`, linking the attempt to a job.  |
| `attempt_number`        | `int`                         | Number of the attempt for a given job.                    |
| `log_path`              | `varchar(255)`                | Path where logs for this attempt are stored.              |
| `output`                | `jsonb`                       | JSON blob containing the attempt's output details.        |
| `status`                | `attempt_status`              | Status of the attempt (`running`, `failed`, `succeeded`). |
| `created_at`            | `timestamp(6) with time zone` | Timestamp when the attempt was created.                   |
| `updated_at`            | `timestamp(6) with time zone` | Timestamp when the attempt was last updated.              |
| `ended_at`              | `timestamp(6) with time zone` | Timestamp when the attempt ended.                         |
| `failure_summary`       | `jsonb`                       | JSON blob containing failure reason details.              |
| `processing_task_queue` | `varchar(255)`                | Task queue identifier for processing.                     |
| `attempt_sync_config`   | `jsonb`                       | JSON blob for sync configuration.                         |

#### Indexes & Constraints[​](#indexes--constraints-1 "Direct link to Indexes & Constraints")

* Primary Key: `id`

* Foreign Key: `job_id` → `jobs(id)`

* Indexes:

  <!-- -->

  * `attempts_status_idx` → (`status`)
  * `job_attempt_idx` → (`job_id`, `attempt_number`) (Unique)

***

### `airbyte_metadata`[​](#airbyte_metadata "Direct link to airbyte_metadata")

| Column Name | Datatype       | Description                                      |
| ----------- | -------------- | ------------------------------------------------ |
| `key`       | `varchar(255)` | Primary key, uniquely identifies a metadata key. |
| `value`     | `varchar(255)` | Value associated with the key.                   |

#### Indexes & Constraints[​](#indexes--constraints-2 "Direct link to Indexes & Constraints")

* Primary Key: `key`

***

### `airbyte_jobs_migrations`[​](#airbyte_jobs_migrations "Direct link to airbyte_jobs_migrations")

| Column Name      | Datatype        | Description                               |
| ---------------- | --------------- | ----------------------------------------- |
| `installed_rank` | `int`           | Primary key, rank of migration execution. |
| `version`        | `varchar(50)`   | Version number of the migration.          |
| `description`    | `varchar(200)`  | Description of the migration.             |
| `type`           | `varchar(20)`   | Type of migration.                        |
| `script`         | `varchar(1000)` | Name of the migration script.             |
| `checksum`       | `int`           | Checksum of the migration script.         |
| `installed_by`   | `varchar(100)`  | User who installed the migration.         |
| `installed_on`   | `timestamp(6)`  | Timestamp when migration was installed.   |
| `execution_time` | `int`           | Execution time in milliseconds.           |
| `success`        | `boolean`       | Whether the migration succeeded.          |

#### Indexes & Constraints[​](#indexes--constraints-3 "Direct link to Indexes & Constraints")

* Primary Key: `installed_rank`
* Indexes:
  <!-- -->
  * `airbyte_jobs_migrations_s_idx` → (`success`)

***

### `normalization_summaries`[​](#normalization_summaries "Direct link to normalization_summaries")

| Column Name  | Datatype                      | Description                                               |
| ------------ | ----------------------------- | --------------------------------------------------------- |
| `id`         | `uuid`                        | Primary key, uniquely identifies a normalization summary. |
| `attempt_id` | `bigint`                      | Foreign key to `attempts(id)`.                            |
| `start_time` | `timestamp(6) with time zone` | Start time of the normalization process.                  |
| `end_time`   | `timestamp(6) with time zone` | End time of the normalization process.                    |
| `failures`   | `jsonb`                       | JSON blob containing failure details.                     |
| `created_at` | `timestamp(6) with time zone` | Timestamp when the summary was created.                   |
| `updated_at` | `timestamp(6) with time zone` | Timestamp when the summary was last updated.              |

#### Indexes & Constraints[​](#indexes--constraints-4 "Direct link to Indexes & Constraints")

* Primary Key: `id`
* Foreign Key: `attempt_id` → `attempts(id)`
* Indexes:
  <!-- -->
  * `normalization_summary_attempt_id_idx` → (`attempt_id`)

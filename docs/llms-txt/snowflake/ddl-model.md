# Source: https://docs.snowflake.com/en/sql-reference/ddl-model.md

# Machine learning model DDL

The following DDL commands are used to create, view, and manage machine-learning models and their versions.

A model is a schema-level object that contains a machine learning model that has been trained and stored in the Snowpark
ML Registry. Model commands let you create and manage models in SQL. You can also create and manage models in Python
using the Snowpark ML Registry API.

Model monitors allow you to monitor the performance of machine learning models you have deployed in Snowflake.

## Machine learning models

|  |  |
| --- | --- |
| [CREATE MODEL](sql/create-model.md) | Creates a new machine learning model in the current/specified schema or replaces an existing model. |
| [ALTER MODEL](sql/alter-model.md) | Modifies the properties for an existing model, including its name, tags, default version, or comment. |
| [SHOW MODELS](sql/show-models.md) | Lists the machine learning models that you have privileges to access. |
| [DROP MODEL](sql/drop-model.md) | Removes a machine learning model from the current/specified schema. |

## Machine learning model versions

|  |  |
| --- | --- |
| [ALTER MODEL … ADD VERSION](sql/alter-model-add-version.md) | Adds a new version to an existing model from an internal stage. |
| [ALTER MODEL … DROP VERSION](sql/alter-model-drop-version.md) | Removes a version from an existing model. |
| [ALTER MODEL … MODIFY VERSION](sql/alter-model-modify-version.md) | Modifies a version of a model, changing the version’s comment or metadata. |
| [SHOW VERSIONS IN MODEL](sql/show-versions-in-model.md) | Lists the versions in a machine learning model. |

## Machine learing model functions

|  |  |
| --- | --- |
| [SHOW FUNCTIONS IN MODEL](sql/show-functions-in-model.md) | Shows the models (methods) attached to a machine learing model. |

## Machine learning model monitors

|  |  |
| --- | --- |
| [CREATE MODEL MONITOR](sql/create-model-monitor.md) | Create a new model monitor. |
| [ALTER MODEL MONITOR](sql/alter-model-monitor.md) | Modify the properties of an existing model monitor, including its refresh interval and warehouse, or suspend or resume it. |
| [SHOW MODEL MONITORS](sql/show-model-monitors.md) | Lists the model monitors that you have privileges to access. |
| [DESCRIBE MODEL MONITOR](sql/desc-model-monitor.md) | Shows the properties of a model monitor. |
| [DROP MODEL MONITOR](sql/drop-model-monitor.md) | Removes a model monitor from the current/specified schema. |

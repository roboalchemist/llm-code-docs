# Source: https://airflow.apache.org/docs/apache-airflow-providers-databricks/stable/index.html

Title: apache-airflow-providers-databricks — apache-airflow-providers-databricks Documentation

URL Source: https://airflow.apache.org/docs/apache-airflow-providers-databricks/stable/index.html

Markdown Content:
apache-airflow-providers-databricks package[¶](https://airflow.apache.org/docs/apache-airflow-providers-databricks/stable/index.html#apache-airflow-providers-databricks-package "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Databricks](https://databricks.com/)

Release: 7.9.1

Provider package[¶](https://airflow.apache.org/docs/apache-airflow-providers-databricks/stable/index.html#provider-package "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------

This package is for the `databricks` provider. All classes for this package are included in the `airflow.providers.databricks` python package.

Installation[¶](https://airflow.apache.org/docs/apache-airflow-providers-databricks/stable/index.html#installation "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------

You can install this package on top of an existing Airflow installation via `pip install apache-airflow-providers-databricks`. For the minimum Airflow version supported, see `Requirements` below.

Requirements[¶](https://airflow.apache.org/docs/apache-airflow-providers-databricks/stable/index.html#requirements "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------

The minimum Apache Airflow version supported by this provider distribution is `2.11.0`.

| PIP package | Version required |
| --- | --- |
| `apache-airflow` | `>=2.11.0` |
| `apache-airflow-providers-common-compat` | `>=1.13.0` |
| `apache-airflow-providers-common-sql` | `>=1.27.0` |
| `requests` | `>=2.32.0,<3` |
| `databricks-sql-connector` | `>=4.0.0` |
| `aiohttp` | `>=3.9.2,<4` |
| `mergedeep` | `>=1.3.4` |
| `pandas` | `>=2.1.2; python_version < "3.13"` |
| `pandas` | `>=2.2.3; python_version >= "3.13"` |
| `pyarrow` | `>=16.1.0; python_version < "3.13"` |
| `pyarrow` | `>=18.0.0; python_version >= "3.13"` |

Cross provider package dependencies[¶](https://airflow.apache.org/docs/apache-airflow-providers-databricks/stable/index.html#cross-provider-package-dependencies "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Those are dependencies that might be needed in order to use all the features of the package. You need to install the specified provider distributions in order to use them.

You can install such cross-provider dependencies when installing from PyPI. For example:

pip install apache-airflow-providers-databricks[common.compat]

| Dependent package | Extra |
| --- | --- |
| [apache-airflow-providers-common-compat](https://airflow.apache.org/docs/apache-airflow-providers-common-compat) | `common.compat` |
| [apache-airflow-providers-common-sql](https://airflow.apache.org/docs/apache-airflow-providers-common-sql) | `common.sql` |
| [apache-airflow-providers-google](https://airflow.apache.org/docs/apache-airflow-providers-google) | `google` |
| [apache-airflow-providers-openlineage](https://airflow.apache.org/docs/apache-airflow-providers-openlineage) | `openlineage` |

Downloading official packages[¶](https://airflow.apache.org/docs/apache-airflow-providers-databricks/stable/index.html#downloading-official-packages "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can download officially released packages and verify their checksums and signatures from the [Official Apache Download site](https://downloads.apache.org/airflow/providers/)

*   [The apache-airflow-providers-databricks 7.9.1 sdist package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_databricks-7.9.1.tar.gz) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_databricks-7.9.1.tar.gz.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_databricks-7.9.1.tar.gz.sha512))

*   [The apache-airflow-providers-databricks 7.9.1 wheel package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_databricks-7.9.1-py3-none-any.whl) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_databricks-7.9.1-py3-none-any.whl.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_databricks-7.9.1-py3-none-any.whl.sha512))

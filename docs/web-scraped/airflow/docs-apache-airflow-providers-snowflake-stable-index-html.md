# Source: https://airflow.apache.org/docs/apache-airflow-providers-snowflake/stable/index.html

Title: apache-airflow-providers-snowflake — apache-airflow-providers-snowflake Documentation

URL Source: https://airflow.apache.org/docs/apache-airflow-providers-snowflake/stable/index.html

Markdown Content:
apache-airflow-providers-snowflake package[¶](https://airflow.apache.org/docs/apache-airflow-providers-snowflake/stable/index.html#apache-airflow-providers-snowflake-package "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Snowflake](https://www.snowflake.com/)

Release: 6.9.1

Provider package[¶](https://airflow.apache.org/docs/apache-airflow-providers-snowflake/stable/index.html#provider-package "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------

This package is for the `snowflake` provider. All classes for this package are included in the `airflow.providers.snowflake` python package.

Installation[¶](https://airflow.apache.org/docs/apache-airflow-providers-snowflake/stable/index.html#installation "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------

You can install this package on top of an existing Airflow installation via `pip install apache-airflow-providers-snowflake`. For the minimum Airflow version supported, see `Requirements` below.

Requirements[¶](https://airflow.apache.org/docs/apache-airflow-providers-snowflake/stable/index.html#requirements "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------

The minimum Apache Airflow version supported by this provider distribution is `2.11.0`.

| PIP package | Version required |
| --- | --- |
| `apache-airflow` | `>=2.11.0` |
| `apache-airflow-providers-common-compat` | `>=1.12.0` |
| `apache-airflow-providers-common-sql` | `>=1.27.5` |
| `pandas` | `>=2.1.2; python_version < "3.13"` |
| `pandas` | `>=2.2.3; python_version >= "3.13"` |
| `pyarrow` | `>=16.1.0; python_version < "3.13"` |
| `pyarrow` | `>=18.0.0; python_version >= "3.13"` |
| `snowflake-connector-python` | `>=3.16.0` |
| `snowflake-sqlalchemy` | `>=1.7.0` |
| `snowflake-snowpark-python` | `>=1.17.0,<9999; python_version < "3.12"` |
| `snowflake-snowpark-python` | `>=1.27.0,<9999; python_version >= "3.12" and python_version < "3.14"` |
| `setuptools` | `>=80.0.0,<9999` |

Cross provider package dependencies[¶](https://airflow.apache.org/docs/apache-airflow-providers-snowflake/stable/index.html#cross-provider-package-dependencies "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Those are dependencies that might be needed in order to use all the features of the package. You need to install the specified provider distributions in order to use them.

You can install such cross-provider dependencies when installing from PyPI. For example:

pip install apache-airflow-providers-snowflake[common.compat]

| Dependent package | Extra |
| --- | --- |
| [apache-airflow-providers-common-compat](https://airflow.apache.org/docs/apache-airflow-providers-common-compat) | `common.compat` |
| [apache-airflow-providers-common-sql](https://airflow.apache.org/docs/apache-airflow-providers-common-sql) | `common.sql` |
| [apache-airflow-providers-microsoft-azure](https://airflow.apache.org/docs/apache-airflow-providers-microsoft-azure) | `microsoft.azure` |
| [apache-airflow-providers-openlineage](https://airflow.apache.org/docs/apache-airflow-providers-openlineage) | `openlineage` |

Downloading official packages[¶](https://airflow.apache.org/docs/apache-airflow-providers-snowflake/stable/index.html#downloading-official-packages "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can download officially released packages and verify their checksums and signatures from the [Official Apache Download site](https://downloads.apache.org/airflow/providers/)

*   [The apache-airflow-providers-snowflake 6.9.1 sdist package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_snowflake-6.9.1.tar.gz) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_snowflake-6.9.1.tar.gz.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_snowflake-6.9.1.tar.gz.sha512))

*   [The apache-airflow-providers-snowflake 6.9.1 wheel package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_snowflake-6.9.1-py3-none-any.whl) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_snowflake-6.9.1-py3-none-any.whl.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_snowflake-6.9.1-py3-none-any.whl.sha512))

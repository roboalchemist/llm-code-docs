# Source: https://airflow.apache.org/docs/apache-airflow-providers-mysql/stable/index.html

Title: apache-airflow-providers-mysql — apache-airflow-providers-mysql Documentation

URL Source: https://airflow.apache.org/docs/apache-airflow-providers-mysql/stable/index.html

Markdown Content:
apache-airflow-providers-mysql package[¶](https://airflow.apache.org/docs/apache-airflow-providers-mysql/stable/index.html#apache-airflow-providers-mysql-package "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[MySQL](https://www.mysql.com/)

Release: 6.4.3

Provider package[¶](https://airflow.apache.org/docs/apache-airflow-providers-mysql/stable/index.html#provider-package "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------

This package is for the `mysql` provider. All classes for this package are included in the `airflow.providers.mysql` python package.

Installation[¶](https://airflow.apache.org/docs/apache-airflow-providers-mysql/stable/index.html#installation "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------

You can install this package on top of an existing Airflow installation via `pip install apache-airflow-providers-mysql`. For the minimum Airflow version supported, see `Requirements` below.

Requirements[¶](https://airflow.apache.org/docs/apache-airflow-providers-mysql/stable/index.html#requirements "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------

The minimum Apache Airflow version supported by this provider distribution is `2.11.0`.

| PIP package | Version required |
| --- | --- |
| `apache-airflow` | `>=2.11.0` |
| `apache-airflow-providers-common-compat` | `>=1.12.0` |
| `apache-airflow-providers-common-sql` | `>=1.20.0` |
| `mysqlclient` | `>=2.2.5; sys_platform != "darwin"` |
| `mysql-connector-python` | `>=9.1.0` |
| `aiomysql` | `>=0.2.0` |

Cross provider package dependencies[¶](https://airflow.apache.org/docs/apache-airflow-providers-mysql/stable/index.html#cross-provider-package-dependencies "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Those are dependencies that might be needed in order to use all the features of the package. You need to install the specified provider distributions in order to use them.

You can install such cross-provider dependencies when installing from PyPI. For example:

pip install apache-airflow-providers-mysql[amazon]

| Dependent package | Extra |
| --- | --- |
| [apache-airflow-providers-amazon](https://airflow.apache.org/docs/apache-airflow-providers-amazon) | `amazon` |
| [apache-airflow-providers-common-compat](https://airflow.apache.org/docs/apache-airflow-providers-common-compat) | `common.compat` |
| [apache-airflow-providers-common-sql](https://airflow.apache.org/docs/apache-airflow-providers-common-sql) | `common.sql` |
| [apache-airflow-providers-openlineage](https://airflow.apache.org/docs/apache-airflow-providers-openlineage) | `openlineage` |
| [apache-airflow-providers-presto](https://airflow.apache.org/docs/apache-airflow-providers-presto) | `presto` |
| [apache-airflow-providers-trino](https://airflow.apache.org/docs/apache-airflow-providers-trino) | `trino` |
| [apache-airflow-providers-vertica](https://airflow.apache.org/docs/apache-airflow-providers-vertica) | `vertica` |

Downloading official packages[¶](https://airflow.apache.org/docs/apache-airflow-providers-mysql/stable/index.html#downloading-official-packages "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can download officially released packages and verify their checksums and signatures from the [Official Apache Download site](https://downloads.apache.org/airflow/providers/)

*   [The apache-airflow-providers-mysql 6.4.3 sdist package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_mysql-6.4.3.tar.gz) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_mysql-6.4.3.tar.gz.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_mysql-6.4.3.tar.gz.sha512))

*   [The apache-airflow-providers-mysql 6.4.3 wheel package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_mysql-6.4.3-py3-none-any.whl) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_mysql-6.4.3-py3-none-any.whl.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_mysql-6.4.3-py3-none-any.whl.sha512))

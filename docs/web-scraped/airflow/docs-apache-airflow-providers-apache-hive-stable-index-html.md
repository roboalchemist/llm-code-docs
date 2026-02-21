# Source: https://airflow.apache.org/docs/apache-airflow-providers-apache-hive/stable/index.html

Title: apache-airflow-providers-apache-hive — apache-airflow-providers-apache-hive Documentation

URL Source: https://airflow.apache.org/docs/apache-airflow-providers-apache-hive/stable/index.html

Markdown Content:
apache-airflow-providers-apache-hive package[¶](https://airflow.apache.org/docs/apache-airflow-providers-apache-hive/stable/index.html#apache-airflow-providers-apache-hive-package "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Apache Hive](https://hive.apache.org/)

Release: 9.2.5

Provider package[¶](https://airflow.apache.org/docs/apache-airflow-providers-apache-hive/stable/index.html#provider-package "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------

This package is for the `apache.hive` provider. All classes for this package are included in the `airflow.providers.apache.hive` python package.

Installation[¶](https://airflow.apache.org/docs/apache-airflow-providers-apache-hive/stable/index.html#installation "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------

You can install this package on top of an existing Airflow installation via `pip install apache-airflow-providers-apache-hive`. For the minimum Airflow version supported, see `Requirements` below.

Requirements[¶](https://airflow.apache.org/docs/apache-airflow-providers-apache-hive/stable/index.html#requirements "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------

The minimum Apache Airflow version supported by this provider distribution is `2.11.0`.

| PIP package | Version required |
| --- | --- |
| `apache-airflow` | `>=2.11.0` |
| `apache-airflow-providers-common-compat` | `>=1.12.0` |
| `apache-airflow-providers-common-sql` | `>=1.26.0` |
| `hmsclient` | `>=0.1.0` |
| `pandas` | `>=2.1.2; python_version < "3.13"` |
| `pandas` | `>=2.2.3; python_version >= "3.13"` |
| `pyhive[hive_pure_sasl]` | `>=0.7.0` |
| `jmespath` | `>=0.7.0` |

Cross provider package dependencies[¶](https://airflow.apache.org/docs/apache-airflow-providers-apache-hive/stable/index.html#cross-provider-package-dependencies "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Those are dependencies that might be needed in order to use all the features of the package. You need to install the specified provider distributions in order to use them.

You can install such cross-provider dependencies when installing from PyPI. For example:

pip install apache-airflow-providers-apache-hive[amazon]

| Dependent package | Extra |
| --- | --- |
| [apache-airflow-providers-amazon](https://airflow.apache.org/docs/apache-airflow-providers-amazon) | `amazon` |
| [apache-airflow-providers-common-compat](https://airflow.apache.org/docs/apache-airflow-providers-common-compat) | `common.compat` |
| [apache-airflow-providers-common-sql](https://airflow.apache.org/docs/apache-airflow-providers-common-sql) | `common.sql` |
| [apache-airflow-providers-microsoft-mssql](https://airflow.apache.org/docs/apache-airflow-providers-microsoft-mssql) | `microsoft.mssql` |
| [apache-airflow-providers-mysql](https://airflow.apache.org/docs/apache-airflow-providers-mysql) | `mysql` |
| [apache-airflow-providers-presto](https://airflow.apache.org/docs/apache-airflow-providers-presto) | `presto` |
| [apache-airflow-providers-samba](https://airflow.apache.org/docs/apache-airflow-providers-samba) | `samba` |
| [apache-airflow-providers-vertica](https://airflow.apache.org/docs/apache-airflow-providers-vertica) | `vertica` |

Downloading official packages[¶](https://airflow.apache.org/docs/apache-airflow-providers-apache-hive/stable/index.html#downloading-official-packages "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can download officially released packages and verify their checksums and signatures from the [Official Apache Download site](https://downloads.apache.org/airflow/providers/)

*   [The apache-airflow-providers-apache-hive 9.2.5 sdist package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_apache_hive-9.2.5.tar.gz) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_apache_hive-9.2.5.tar.gz.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_apache_hive-9.2.5.tar.gz.sha512))

*   [The apache-airflow-providers-apache-hive 9.2.5 wheel package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_apache_hive-9.2.5-py3-none-any.whl) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_apache_hive-9.2.5-py3-none-any.whl.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_apache_hive-9.2.5-py3-none-any.whl.sha512))

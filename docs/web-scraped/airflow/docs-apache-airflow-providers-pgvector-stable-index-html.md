# Source: https://airflow.apache.org/docs/apache-airflow-providers-pgvector/stable/index.html

Title: apache-airflow-providers-pgvector — apache-airflow-providers-pgvector Documentation

URL Source: https://airflow.apache.org/docs/apache-airflow-providers-pgvector/stable/index.html

Markdown Content:
apache-airflow-providers-pgvector package[¶](https://airflow.apache.org/docs/apache-airflow-providers-pgvector/stable/index.html#apache-airflow-providers-pgvector-package "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[pgvector](https://github.com/pgvector/pgvector)

Release: 1.6.1

Provider package[¶](https://airflow.apache.org/docs/apache-airflow-providers-pgvector/stable/index.html#provider-package "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------

This package is for the `pgvector` provider. All classes for this package are included in the `airflow.providers.pgvector` python package.

Installation[¶](https://airflow.apache.org/docs/apache-airflow-providers-pgvector/stable/index.html#installation "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------

You can install this package on top of an existing Airflow installation via `pip install apache-airflow-providers-pgvector`. For the minimum Airflow version supported, see `Requirements` below.

Requirements[¶](https://airflow.apache.org/docs/apache-airflow-providers-pgvector/stable/index.html#requirements "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------

The minimum Apache Airflow version supported by this provider distribution is `2.11.0`.

| PIP package | Version required |
| --- | --- |
| `apache-airflow` | `>=2.11.0` |
| `apache-airflow-providers-common-compat` | `>=1.8.0` |
| `apache-airflow-providers-postgres` | `>=5.7.1` |
| `pgvector` | `>=0.3.1` |

Cross provider package dependencies[¶](https://airflow.apache.org/docs/apache-airflow-providers-pgvector/stable/index.html#cross-provider-package-dependencies "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Those are dependencies that might be needed in order to use all the features of the package. You need to install the specified provider distributions in order to use them.

You can install such cross-provider dependencies when installing from PyPI. For example:

pip install apache-airflow-providers-pgvector[common.sql]

| Dependent package | Extra |
| --- | --- |
| [apache-airflow-providers-common-sql](https://airflow.apache.org/docs/apache-airflow-providers-common-sql) | `common.sql` |
| [apache-airflow-providers-postgres](https://airflow.apache.org/docs/apache-airflow-providers-postgres) | `postgres` |

Downloading official packages[¶](https://airflow.apache.org/docs/apache-airflow-providers-pgvector/stable/index.html#downloading-official-packages "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can download officially released packages and verify their checksums and signatures from the [Official Apache Download site](https://downloads.apache.org/airflow/providers/)

*   [The apache-airflow-providers-pgvector 1.6.1 sdist package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_pgvector-1.6.1.tar.gz) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_pgvector-1.6.1.tar.gz.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_pgvector-1.6.1.tar.gz.sha512))

*   [The apache-airflow-providers-pgvector 1.6.1 wheel package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_pgvector-1.6.1-py3-none-any.whl) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_pgvector-1.6.1-py3-none-any.whl.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_pgvector-1.6.1-py3-none-any.whl.sha512))

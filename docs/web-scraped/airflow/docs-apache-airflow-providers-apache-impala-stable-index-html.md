# Source: https://airflow.apache.org/docs/apache-airflow-providers-apache-impala/stable/index.html

Title: apache-airflow-providers-apache-impala — apache-airflow-providers-apache-impala Documentation

URL Source: https://airflow.apache.org/docs/apache-airflow-providers-apache-impala/stable/index.html

Markdown Content:
apache-airflow-providers-apache-impala package[¶](https://airflow.apache.org/docs/apache-airflow-providers-apache-impala/stable/index.html#apache-airflow-providers-apache-impala-package "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Apache Impala](https://impala.apache.org/).

Release: 1.8.1

Provider package[¶](https://airflow.apache.org/docs/apache-airflow-providers-apache-impala/stable/index.html#provider-package "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

This package is for the `apache.impala` provider. All classes for this package are included in the `airflow.providers.apache.impala` python package.

Installation[¶](https://airflow.apache.org/docs/apache-airflow-providers-apache-impala/stable/index.html#installation "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------

You can install this package on top of an existing Airflow installation via `pip install apache-airflow-providers-apache-impala`. For the minimum Airflow version supported, see `Requirements` below.

Requirements[¶](https://airflow.apache.org/docs/apache-airflow-providers-apache-impala/stable/index.html#requirements "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------

The minimum Apache Airflow version supported by this provider distribution is `2.11.0`.

| PIP package | Version required |
| --- | --- |
| `impyla` | `>=0.22.0,<1.0` |
| `apache-airflow-providers-common-compat` | `>=1.12.0` |
| `apache-airflow-providers-common-sql` | `>=1.26.0` |
| `apache-airflow` | `>=2.11.0` |

Cross provider package dependencies[¶](https://airflow.apache.org/docs/apache-airflow-providers-apache-impala/stable/index.html#cross-provider-package-dependencies "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Those are dependencies that might be needed in order to use all the features of the package. You need to install the specified provider distributions in order to use them.

You can install such cross-provider dependencies when installing from PyPI. For example:

pip install apache-airflow-providers-apache-impala[common.compat]

| Dependent package | Extra |
| --- | --- |
| [apache-airflow-providers-common-compat](https://airflow.apache.org/docs/apache-airflow-providers-common-compat) | `common.compat` |
| [apache-airflow-providers-common-sql](https://airflow.apache.org/docs/apache-airflow-providers-common-sql) | `common.sql` |

Downloading official packages[¶](https://airflow.apache.org/docs/apache-airflow-providers-apache-impala/stable/index.html#downloading-official-packages "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can download officially released packages and verify their checksums and signatures from the [Official Apache Download site](https://downloads.apache.org/airflow/providers/)

*   [The apache-airflow-providers-apache-impala 1.8.1 sdist package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_apache_impala-1.8.1.tar.gz) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_apache_impala-1.8.1.tar.gz.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_apache_impala-1.8.1.tar.gz.sha512))

*   [The apache-airflow-providers-apache-impala 1.8.1 wheel package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_apache_impala-1.8.1-py3-none-any.whl) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_apache_impala-1.8.1-py3-none-any.whl.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_apache_impala-1.8.1-py3-none-any.whl.sha512))

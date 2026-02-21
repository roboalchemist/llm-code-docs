# Source: https://airflow.apache.org/docs/apache-airflow-providers-exasol/stable/index.html

Title: apache-airflow-providers-exasol — apache-airflow-providers-exasol Documentation

URL Source: https://airflow.apache.org/docs/apache-airflow-providers-exasol/stable/index.html

Markdown Content:
apache-airflow-providers-exasol package[¶](https://airflow.apache.org/docs/apache-airflow-providers-exasol/stable/index.html#apache-airflow-providers-exasol-package "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Exasol](https://www.exasol.com/)

Release: 4.9.3

Provider package[¶](https://airflow.apache.org/docs/apache-airflow-providers-exasol/stable/index.html#provider-package "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------

This package is for the `exasol` provider. All classes for this package are included in the `airflow.providers.exasol` python package.

Installation[¶](https://airflow.apache.org/docs/apache-airflow-providers-exasol/stable/index.html#installation "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------

You can install this package on top of an existing Airflow installation via `pip install apache-airflow-providers-exasol`. For the minimum Airflow version supported, see `Requirements` below.

Requirements[¶](https://airflow.apache.org/docs/apache-airflow-providers-exasol/stable/index.html#requirements "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------

The minimum Apache Airflow version supported by this provider distribution is `2.11.0`.

| PIP package | Version required |
| --- | --- |
| `apache-airflow` | `>=2.11.0` |
| `apache-airflow-providers-common-compat` | `>=1.12.0` |
| `apache-airflow-providers-common-sql` | `>=1.26.0` |
| `pyexasol` | `>=0.26.0` |
| `pandas` | `>=2.1.2; python_version < "3.13"` |
| `pandas` | `>=2.2.3; python_version >= "3.13"` |

Cross provider package dependencies[¶](https://airflow.apache.org/docs/apache-airflow-providers-exasol/stable/index.html#cross-provider-package-dependencies "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Those are dependencies that might be needed in order to use all the features of the package. You need to install the specified provider distributions in order to use them.

You can install such cross-provider dependencies when installing from PyPI. For example:

pip install apache-airflow-providers-exasol[common.compat]

| Dependent package | Extra |
| --- | --- |
| [apache-airflow-providers-common-compat](https://airflow.apache.org/docs/apache-airflow-providers-common-compat) | `common.compat` |
| [apache-airflow-providers-common-sql](https://airflow.apache.org/docs/apache-airflow-providers-common-sql) | `common.sql` |

Downloading official packages[¶](https://airflow.apache.org/docs/apache-airflow-providers-exasol/stable/index.html#downloading-official-packages "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can download officially released packages and verify their checksums and signatures from the [Official Apache Download site](https://downloads.apache.org/airflow/providers/)

*   [The apache-airflow-providers-exasol 4.9.3 sdist package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_exasol-4.9.3.tar.gz) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_exasol-4.9.3.tar.gz.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_exasol-4.9.3.tar.gz.sha512))

*   [The apache-airflow-providers-exasol 4.9.3 wheel package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_exasol-4.9.3-py3-none-any.whl) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_exasol-4.9.3-py3-none-any.whl.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_exasol-4.9.3-py3-none-any.whl.sha512))

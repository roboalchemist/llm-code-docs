# Source: https://airflow.apache.org/docs/apache-airflow-providers-teradata/stable/index.html

Title: apache-airflow-providers-teradata — apache-airflow-providers-teradata Documentation

URL Source: https://airflow.apache.org/docs/apache-airflow-providers-teradata/stable/index.html

Markdown Content:
apache-airflow-providers-teradata package[¶](https://airflow.apache.org/docs/apache-airflow-providers-teradata/stable/index.html#apache-airflow-providers-teradata-package "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Teradata](https://www.teradata.com/)

Release: 3.4.3

Provider package[¶](https://airflow.apache.org/docs/apache-airflow-providers-teradata/stable/index.html#provider-package "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------

This package is for the `teradata` provider. All classes for this package are included in the `airflow.providers.teradata` python package.

Installation[¶](https://airflow.apache.org/docs/apache-airflow-providers-teradata/stable/index.html#installation "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------

You can install this package on top of an existing Airflow installation via `pip install apache-airflow-providers-teradata`. For the minimum Airflow version supported, see `Requirements` below.

Requirements[¶](https://airflow.apache.org/docs/apache-airflow-providers-teradata/stable/index.html#requirements "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------

The minimum Apache Airflow version supported by this provider distribution is `2.11.0`.

| PIP package | Version required |
| --- | --- |
| `apache-airflow` | `>=2.11.0` |
| `apache-airflow-providers-common-compat` | `>=1.12.0` |
| `apache-airflow-providers-common-sql` | `>=1.20.0` |
| `teradatasqlalchemy` | `>=17.20.0.0` |
| `teradatasql` | `>=17.20.0.28` |

Cross provider package dependencies[¶](https://airflow.apache.org/docs/apache-airflow-providers-teradata/stable/index.html#cross-provider-package-dependencies "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Those are dependencies that might be needed in order to use all the features of the package. You need to install the specified provider distributions in order to use them.

You can install such cross-provider dependencies when installing from PyPI. For example:

pip install apache-airflow-providers-teradata[amazon]

| Dependent package | Extra |
| --- | --- |
| [apache-airflow-providers-amazon](https://airflow.apache.org/docs/apache-airflow-providers-amazon) | `amazon` |
| [apache-airflow-providers-common-compat](https://airflow.apache.org/docs/apache-airflow-providers-common-compat) | `common.compat` |
| [apache-airflow-providers-common-sql](https://airflow.apache.org/docs/apache-airflow-providers-common-sql) | `common.sql` |
| [apache-airflow-providers-microsoft-azure](https://airflow.apache.org/docs/apache-airflow-providers-microsoft-azure) | `microsoft.azure` |
| [apache-airflow-providers-ssh](https://airflow.apache.org/docs/apache-airflow-providers-ssh) | `ssh` |

Downloading official packages[¶](https://airflow.apache.org/docs/apache-airflow-providers-teradata/stable/index.html#downloading-official-packages "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can download officially released packages and verify their checksums and signatures from the [Official Apache Download site](https://downloads.apache.org/airflow/providers/)

*   [The apache-airflow-providers-teradata 3.4.3 sdist package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_teradata-3.4.3.tar.gz) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_teradata-3.4.3.tar.gz.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_teradata-3.4.3.tar.gz.sha512))

*   [The apache-airflow-providers-teradata 3.4.3 wheel package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_teradata-3.4.3-py3-none-any.whl) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_teradata-3.4.3-py3-none-any.whl.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_teradata-3.4.3-py3-none-any.whl.sha512))

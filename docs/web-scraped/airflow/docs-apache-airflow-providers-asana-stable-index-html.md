# Source: https://airflow.apache.org/docs/apache-airflow-providers-asana/stable/index.html

Title: apache-airflow-providers-asana — apache-airflow-providers-asana Documentation

URL Source: https://airflow.apache.org/docs/apache-airflow-providers-asana/stable/index.html

Markdown Content:
apache-airflow-providers-asana package[¶](https://airflow.apache.org/docs/apache-airflow-providers-asana/stable/index.html#apache-airflow-providers-asana-package "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Asana](https://asana.com/)

Release: 2.11.1

Provider package[¶](https://airflow.apache.org/docs/apache-airflow-providers-asana/stable/index.html#provider-package "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------

This package is for the `asana` provider. All classes for this package are included in the `airflow.providers.asana` python package.

Installation[¶](https://airflow.apache.org/docs/apache-airflow-providers-asana/stable/index.html#installation "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------

You can install this package on top of an existing Airflow installation via `pip install apache-airflow-providers-asana`. For the minimum Airflow version supported, see `Requirements` below.

Requirements[¶](https://airflow.apache.org/docs/apache-airflow-providers-asana/stable/index.html#requirements "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------

The minimum Apache Airflow version supported by this provider distribution is `2.11.0`.

| PIP package | Version required |
| --- | --- |
| `apache-airflow` | `>=2.11.0` |
| `apache-airflow-providers-common-compat` | `>=1.8.0` |
| `asana` | `>=5.0.0` |

Cross provider package dependencies[¶](https://airflow.apache.org/docs/apache-airflow-providers-asana/stable/index.html#cross-provider-package-dependencies "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Those are dependencies that might be needed in order to use all the features of the package. You need to install the specified provider distributions in order to use them.

You can install such cross-provider dependencies when installing from PyPI. For example:

pip install apache-airflow-providers-asana[common.compat]

| Dependent package | Extra |
| --- | --- |
| [apache-airflow-providers-common-compat](https://airflow.apache.org/docs/apache-airflow-providers-common-compat) | `common.compat` |

Downloading official packages[¶](https://airflow.apache.org/docs/apache-airflow-providers-asana/stable/index.html#downloading-official-packages "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can download officially released packages and verify their checksums and signatures from the [Official Apache Download site](https://downloads.apache.org/airflow/providers/)

*   [The apache-airflow-providers-asana 2.11.1 sdist package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_asana-2.11.1.tar.gz) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_asana-2.11.1.tar.gz.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_asana-2.11.1.tar.gz.sha512))

*   [The apache-airflow-providers-asana 2.11.1 wheel package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_asana-2.11.1-py3-none-any.whl) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_asana-2.11.1-py3-none-any.whl.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_asana-2.11.1-py3-none-any.whl.sha512))

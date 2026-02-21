# Source: https://airflow.apache.org/docs/apache-airflow-providers-dbt-cloud/stable/index.html

Title: apache-airflow-providers-dbt-cloud — apache-airflow-providers-dbt-cloud Documentation

URL Source: https://airflow.apache.org/docs/apache-airflow-providers-dbt-cloud/stable/index.html

Markdown Content:
dbt Cloud is a hosted service that helps data analysts and engineers productionalize dbt deployments. It comes equipped with turnkey support for scheduling jobs, CI/CD, serving documentation, monitoring & alerting, and an Integrated Developer Environment (IDE).

apache-airflow-providers-dbt-cloud package[¶](https://airflow.apache.org/docs/apache-airflow-providers-dbt-cloud/stable/index.html#apache-airflow-providers-dbt-cloud-package "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[dbt Cloud](https://www.getdbt.com/product/dbt-cloud/)

Release: 4.6.4

Provider package[¶](https://airflow.apache.org/docs/apache-airflow-providers-dbt-cloud/stable/index.html#provider-package "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------

This package is for the `dbt.cloud` provider. All classes for this package are included in the `airflow.providers.dbt.cloud` python package.

Installation[¶](https://airflow.apache.org/docs/apache-airflow-providers-dbt-cloud/stable/index.html#installation "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------

You can install this package on top of an existing Airflow installation via `pip install apache-airflow-providers-dbt-cloud`. For the minimum Airflow version supported, see `Requirements` below.

Requirements[¶](https://airflow.apache.org/docs/apache-airflow-providers-dbt-cloud/stable/index.html#requirements "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------

The minimum Apache Airflow version supported by this provider distribution is `2.11.0`.

| PIP package | Version required |
| --- | --- |
| `apache-airflow` | `>=2.11.0` |
| `apache-airflow-providers-common-compat` | `>=1.12.0` |
| `apache-airflow-providers-http` |  |
| `asgiref` | `>=2.3.0` |
| `aiohttp` | `>=3.9.2` |
| `tenacity` | `>=8.3.0` |

Cross provider package dependencies[¶](https://airflow.apache.org/docs/apache-airflow-providers-dbt-cloud/stable/index.html#cross-provider-package-dependencies "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Those are dependencies that might be needed in order to use all the features of the package. You need to install the specified provider distributions in order to use them.

You can install such cross-provider dependencies when installing from PyPI. For example:

pip install apache-airflow-providers-dbt-cloud[common.compat]

| Dependent package | Extra |
| --- | --- |
| [apache-airflow-providers-common-compat](https://airflow.apache.org/docs/apache-airflow-providers-common-compat) | `common.compat` |
| [apache-airflow-providers-http](https://airflow.apache.org/docs/apache-airflow-providers-http) | `http` |
| [apache-airflow-providers-openlineage](https://airflow.apache.org/docs/apache-airflow-providers-openlineage) | `openlineage` |

Downloading official packages[¶](https://airflow.apache.org/docs/apache-airflow-providers-dbt-cloud/stable/index.html#downloading-official-packages "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can download officially released packages and verify their checksums and signatures from the [Official Apache Download site](https://downloads.apache.org/airflow/providers/)

*   [The apache-airflow-providers-dbt-cloud 4.6.4 sdist package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_dbt_cloud-4.6.4.tar.gz) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_dbt_cloud-4.6.4.tar.gz.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_dbt_cloud-4.6.4.tar.gz.sha512))

*   [The apache-airflow-providers-dbt-cloud 4.6.4 wheel package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_dbt_cloud-4.6.4-py3-none-any.whl) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_dbt_cloud-4.6.4-py3-none-any.whl.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_dbt_cloud-4.6.4-py3-none-any.whl.sha512))

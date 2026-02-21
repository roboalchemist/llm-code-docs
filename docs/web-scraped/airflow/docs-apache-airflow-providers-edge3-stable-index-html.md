# Source: https://airflow.apache.org/docs/apache-airflow-providers-edge3/stable/index.html

Title: apache-airflow-providers-edge3 — apache-airflow-providers-edge3 Documentation

URL Source: https://airflow.apache.org/docs/apache-airflow-providers-edge3/stable/index.html

Markdown Content:
apache-airflow-providers-edge3 package[¶](https://airflow.apache.org/docs/apache-airflow-providers-edge3/stable/index.html#apache-airflow-providers-edge3-package "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Handle edge workers on remote sites via HTTP(s) connection and orchestrates work over distributed sites.

When tasks need to be executed on remote sites where the connection need to pass through firewalls or other network restrictions, the Edge Worker can be deployed. The Edge Worker is a lightweight process with reduced dependencies. The worker only needs to be able to communicate with the central Airflow site via HTTPS.

In the central Airflow site the EdgeExecutor is used to orchestrate the work. The EdgeExecutor is a custom executor which is used to schedule tasks on the edge workers. The EdgeExecutor can co-exist with other executors (for example CeleryExecutor or KubernetesExecutor) in the same Airflow site.

Additional REST API endpoints are provided to distribute tasks and manage the edge workers. The endpoints are provided by the API server.

Release: 3.0.2

Provider package[¶](https://airflow.apache.org/docs/apache-airflow-providers-edge3/stable/index.html#provider-package "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------

This package is for the `edge3` provider. All classes for this package are included in the `airflow.providers.edge3` python package.

Installation[¶](https://airflow.apache.org/docs/apache-airflow-providers-edge3/stable/index.html#installation "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------

You can install this package on top of an existing Airflow installation via `pip install apache-airflow-providers-edge3`. For the minimum Airflow version supported, see `Requirements` below.

Requirements[¶](https://airflow.apache.org/docs/apache-airflow-providers-edge3/stable/index.html#requirements "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------

The minimum Apache Airflow version supported by this provider distribution is `3.0.0`.

| PIP package | Version required |
| --- | --- |
| `apache-airflow` | `>=3.0.0,!=3.1.0` |
| `apache-airflow-providers-common-compat` | `>=1.13.0` |
| `pydantic` | `>=2.11.0` |
| `retryhttp` | `>=1.4.0` |
| `aiofiles` | `>=23.2.0` |
| `aiohttp` | `>=3.9.2` |

Cross provider package dependencies[¶](https://airflow.apache.org/docs/apache-airflow-providers-edge3/stable/index.html#cross-provider-package-dependencies "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Those are dependencies that might be needed in order to use all the features of the package. You need to install the specified provider distributions in order to use them.

You can install such cross-provider dependencies when installing from PyPI. For example:

pip install apache-airflow-providers-edge3[common.compat]

| Dependent package | Extra |
| --- | --- |
| [apache-airflow-providers-common-compat](https://airflow.apache.org/docs/apache-airflow-providers-common-compat) | `common.compat` |

Downloading official packages[¶](https://airflow.apache.org/docs/apache-airflow-providers-edge3/stable/index.html#downloading-official-packages "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can download officially released packages and verify their checksums and signatures from the [Official Apache Download site](https://downloads.apache.org/airflow/providers/)

*   [The apache-airflow-providers-edge3 3.0.2 sdist package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_edge3-3.0.2.tar.gz) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_edge3-3.0.2.tar.gz.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_edge3-3.0.2.tar.gz.sha512))

*   [The apache-airflow-providers-edge3 3.0.2 wheel package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_edge3-3.0.2-py3-none-any.whl) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_edge3-3.0.2-py3-none-any.whl.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_edge3-3.0.2-py3-none-any.whl.sha512))

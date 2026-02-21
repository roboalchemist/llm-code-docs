# Source: https://airflow.apache.org/docs/apache-airflow-providers-fab/stable/index.html

Title: apache-airflow-providers-fab — apache-airflow-providers-fab Documentation

URL Source: https://airflow.apache.org/docs/apache-airflow-providers-fab/stable/index.html

Markdown Content:
apache-airflow-providers-fab package[¶](https://airflow.apache.org/docs/apache-airflow-providers-fab/stable/index.html#apache-airflow-providers-fab-package "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Flask App Builder](https://flask-appbuilder.readthedocs.io/)

Release: 3.3.0

Provider package[¶](https://airflow.apache.org/docs/apache-airflow-providers-fab/stable/index.html#provider-package "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------

This package is for the `fab` provider. All classes for this package are included in the `airflow.providers.fab` python package.

Installation[¶](https://airflow.apache.org/docs/apache-airflow-providers-fab/stable/index.html#installation "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------

You can install this package on top of an existing Airflow installation via `pip install apache-airflow-providers-fab`. For the minimum Airflow version supported, see `Requirements` below.

Requirements[¶](https://airflow.apache.org/docs/apache-airflow-providers-fab/stable/index.html#requirements "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------

The minimum Apache Airflow version supported by this provider distribution is `3.0.2`.

| PIP package | Version required |
| --- | --- |
| `apache-airflow` | `>=3.0.2` |
| `apache-airflow-providers-common-compat` | `>=1.12.0` |
| `blinker` | `>=1.6.2; python_version < "3.13"` |
| `flask` | `>=2.2.1,<2.3; python_version < "3.13"` |
| `flask-appbuilder` | `==5.0.1; python_version < "3.13"` |
| `flask-login` | `>=0.6.2; python_version < "3.13"` |
| `flask-session` | `>=0.8.0; python_version < "3.13"` |
| `msgpack` | `>=1.0.0; python_version < "3.13"` |
| `flask-sqlalchemy` | `>=3.0.5; python_version < "3.13"` |
| `flask-wtf` | `>=1.1.0; python_version < "3.13"` |
| `connexion[flask]` | `>=2.14.2,<3.0; python_version < "3.13"` |
| `jmespath` | `>=0.7.0; python_version < "3.13"` |
| `werkzeug` | `>=2.2,<4; python_version < "3.13"` |
| `wtforms` | `>=3.0,<4; python_version < "3.13"` |
| `cachetools` | `>=6.0; python_version < "3.13"` |
| `flask_limiter` | `>3,!=3.13,<4` |

Cross provider package dependencies[¶](https://airflow.apache.org/docs/apache-airflow-providers-fab/stable/index.html#cross-provider-package-dependencies "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Those are dependencies that might be needed in order to use all the features of the package. You need to install the specified provider distributions in order to use them.

You can install such cross-provider dependencies when installing from PyPI. For example:

pip install apache-airflow-providers-fab[common.compat]

| Dependent package | Extra |
| --- | --- |
| [apache-airflow-providers-common-compat](https://airflow.apache.org/docs/apache-airflow-providers-common-compat) | `common.compat` |

Downloading official packages[¶](https://airflow.apache.org/docs/apache-airflow-providers-fab/stable/index.html#downloading-official-packages "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can download officially released packages and verify their checksums and signatures from the [Official Apache Download site](https://downloads.apache.org/airflow/providers/)

*   [The apache-airflow-providers-fab 3.3.0 sdist package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_fab-3.3.0.tar.gz) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_fab-3.3.0.tar.gz.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_fab-3.3.0.tar.gz.sha512))

*   [The apache-airflow-providers-fab 3.3.0 wheel package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_fab-3.3.0-py3-none-any.whl) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_fab-3.3.0-py3-none-any.whl.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_fab-3.3.0-py3-none-any.whl.sha512))

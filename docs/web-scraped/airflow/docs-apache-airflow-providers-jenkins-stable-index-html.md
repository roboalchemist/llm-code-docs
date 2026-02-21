# Source: https://airflow.apache.org/docs/apache-airflow-providers-jenkins/stable/index.html

Title: apache-airflow-providers-jenkins — apache-airflow-providers-jenkins Documentation

URL Source: https://airflow.apache.org/docs/apache-airflow-providers-jenkins/stable/index.html

Markdown Content:
apache-airflow-providers-jenkins package[¶](https://airflow.apache.org/docs/apache-airflow-providers-jenkins/stable/index.html#apache-airflow-providers-jenkins-package "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Jenkins](https://jenkins.io/)

Release: 4.2.2

Provider package[¶](https://airflow.apache.org/docs/apache-airflow-providers-jenkins/stable/index.html#provider-package "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------

This package is for the `jenkins` provider. All classes for this package are included in the `airflow.providers.jenkins` python package.

Installation[¶](https://airflow.apache.org/docs/apache-airflow-providers-jenkins/stable/index.html#installation "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------

You can install this package on top of an existing Airflow installation via `pip install apache-airflow-providers-jenkins`. For the minimum Airflow version supported, see `Requirements` below.

Requirements[¶](https://airflow.apache.org/docs/apache-airflow-providers-jenkins/stable/index.html#requirements "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------

The minimum Apache Airflow version supported by this provider distribution is `2.11.0`.

| PIP package | Version required |
| --- | --- |
| `apache-airflow` | `>=2.11.0` |
| `apache-airflow-providers-common-compat` | `>=1.10.1` |
| `python-jenkins` | `>=1.8.2` |

Cross provider package dependencies[¶](https://airflow.apache.org/docs/apache-airflow-providers-jenkins/stable/index.html#cross-provider-package-dependencies "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Those are dependencies that might be needed in order to use all the features of the package. You need to install the specified provider distributions in order to use them.

You can install such cross-provider dependencies when installing from PyPI. For example:

pip install apache-airflow-providers-jenkins[common.compat]

| Dependent package | Extra |
| --- | --- |
| [apache-airflow-providers-common-compat](https://airflow.apache.org/docs/apache-airflow-providers-common-compat) | `common.compat` |

Downloading official packages[¶](https://airflow.apache.org/docs/apache-airflow-providers-jenkins/stable/index.html#downloading-official-packages "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can download officially released packages and verify their checksums and signatures from the [Official Apache Download site](https://downloads.apache.org/airflow/providers/)

*   [The apache-airflow-providers-jenkins 4.2.2 sdist package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_jenkins-4.2.2.tar.gz) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_jenkins-4.2.2.tar.gz.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_jenkins-4.2.2.tar.gz.sha512))

*   [The apache-airflow-providers-jenkins 4.2.2 wheel package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_jenkins-4.2.2-py3-none-any.whl) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_jenkins-4.2.2-py3-none-any.whl.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_jenkins-4.2.2-py3-none-any.whl.sha512))

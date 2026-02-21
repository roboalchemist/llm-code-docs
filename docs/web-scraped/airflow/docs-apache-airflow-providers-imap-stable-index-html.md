# Source: https://airflow.apache.org/docs/apache-airflow-providers-imap/stable/index.html

Title: apache-airflow-providers-imap — apache-airflow-providers-imap Documentation

URL Source: https://airflow.apache.org/docs/apache-airflow-providers-imap/stable/index.html

Markdown Content:
apache-airflow-providers-imap package[¶](https://airflow.apache.org/docs/apache-airflow-providers-imap/stable/index.html#apache-airflow-providers-imap-package "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Internet Message Access Protocol (IMAP)](https://tools.ietf.org/html/rfc3501)

Release: 3.11.0

Provider package[¶](https://airflow.apache.org/docs/apache-airflow-providers-imap/stable/index.html#provider-package "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

This package is for the `imap` provider. All classes for this package are included in the `airflow.providers.imap` python package.

Installation[¶](https://airflow.apache.org/docs/apache-airflow-providers-imap/stable/index.html#installation "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------

You can install this package on top of an existing Airflow installation via `pip install apache-airflow-providers-imap`. For the minimum Airflow version supported, see `Requirements` below.

Requirements[¶](https://airflow.apache.org/docs/apache-airflow-providers-imap/stable/index.html#requirements "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------

The minimum Apache Airflow version supported by this provider distribution is `2.11.0`.

| PIP package | Version required |
| --- | --- |
| `apache-airflow` | `>=2.11.0` |
| `apache-airflow-providers-common-compat` | `>=1.12.0` |

Cross provider package dependencies[¶](https://airflow.apache.org/docs/apache-airflow-providers-imap/stable/index.html#cross-provider-package-dependencies "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Those are dependencies that might be needed in order to use all the features of the package. You need to install the specified provider distributions in order to use them.

You can install such cross-provider dependencies when installing from PyPI. For example:

pip install apache-airflow-providers-imap[common.compat]

| Dependent package | Extra |
| --- | --- |
| [apache-airflow-providers-common-compat](https://airflow.apache.org/docs/apache-airflow-providers-common-compat) | `common.compat` |

Downloading official packages[¶](https://airflow.apache.org/docs/apache-airflow-providers-imap/stable/index.html#downloading-official-packages "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can download officially released packages and verify their checksums and signatures from the [Official Apache Download site](https://downloads.apache.org/airflow/providers/)

*   [The apache-airflow-providers-imap 3.11.0 sdist package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_imap-3.11.0.tar.gz) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_imap-3.11.0.tar.gz.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_imap-3.11.0.tar.gz.sha512))

*   [The apache-airflow-providers-imap 3.11.0 wheel package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_imap-3.11.0-py3-none-any.whl) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_imap-3.11.0-py3-none-any.whl.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_imap-3.11.0-py3-none-any.whl.sha512))

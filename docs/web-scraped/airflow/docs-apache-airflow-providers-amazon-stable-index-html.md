# Source: https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/index.html

Title: apache-airflow-providers-amazon — apache-airflow-providers-amazon Documentation

URL Source: https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/index.html

Markdown Content:
apache-airflow-providers-amazon package[¶](https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/index.html#apache-airflow-providers-amazon-package "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Amazon integration (including [Amazon Web Services (AWS)](https://aws.amazon.com/)).

Release: 9.21.0

Provider package[¶](https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/index.html#provider-package "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------

This package is for the `amazon` provider. All classes for this package are included in the `airflow.providers.amazon` python package.

Installation[¶](https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/index.html#installation "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------

You can install this package on top of an existing Airflow installation via `pip install apache-airflow-providers-amazon`. For the minimum Airflow version supported, see `Requirements` below.

Requirements[¶](https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/index.html#requirements "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------

The minimum Apache Airflow version supported by this provider distribution is `2.11.0`.

| PIP package | Version required |
| --- | --- |
| `apache-airflow` | `>=2.11.0` |
| `apache-airflow-providers-common-compat` | `>=1.13.0` |
| `apache-airflow-providers-common-sql` | `>=1.27.0` |
| `apache-airflow-providers-http` |  |
| `boto3` | `>=1.37.2` |
| `botocore` | `>=1.37.2` |
| `inflection` | `>=0.5.1` |
| `watchtower` | `>=3.3.1,<4` |
| `jsonpath_ng` | `>=1.5.3` |
| `redshift_connector` | `>=2.1.3` |
| `asgiref` | `>=2.3.0` |
| `PyAthena` | `>=3.10.0` |
| `jmespath` | `>=0.7.0` |
| `sagemaker-studio` | `>=1.0.9` |
| `pydynamodb` | `>=0.7.5; python_version >= "3.13"` |
| `sqlean.py` | `>=3.47.0; python_version >= "3.13"` |
| `marshmallow` | `>=3` |

Cross provider package dependencies[¶](https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/index.html#cross-provider-package-dependencies "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Those are dependencies that might be needed in order to use all the features of the package. You need to install the specified provider distributions in order to use them.

You can install such cross-provider dependencies when installing from PyPI. For example:

pip install apache-airflow-providers-amazon[apache.hive]

| Dependent package | Extra |
| --- | --- |
| [apache-airflow-providers-apache-hive](https://airflow.apache.org/docs/apache-airflow-providers-apache-hive) | `apache.hive` |
| [apache-airflow-providers-cncf-kubernetes](https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes) | `cncf.kubernetes` |
| [apache-airflow-providers-common-compat](https://airflow.apache.org/docs/apache-airflow-providers-common-compat) | `common.compat` |
| [apache-airflow-providers-common-messaging](https://airflow.apache.org/docs/apache-airflow-providers-common-messaging) | `common.messaging` |
| [apache-airflow-providers-common-sql](https://airflow.apache.org/docs/apache-airflow-providers-common-sql) | `common.sql` |
| [apache-airflow-providers-exasol](https://airflow.apache.org/docs/apache-airflow-providers-exasol) | `exasol` |
| [apache-airflow-providers-ftp](https://airflow.apache.org/docs/apache-airflow-providers-ftp) | `ftp` |
| [apache-airflow-providers-google](https://airflow.apache.org/docs/apache-airflow-providers-google) | `google` |
| [apache-airflow-providers-http](https://airflow.apache.org/docs/apache-airflow-providers-http) | `http` |
| [apache-airflow-providers-imap](https://airflow.apache.org/docs/apache-airflow-providers-imap) | `imap` |
| [apache-airflow-providers-microsoft-azure](https://airflow.apache.org/docs/apache-airflow-providers-microsoft-azure) | `microsoft.azure` |
| [apache-airflow-providers-mongo](https://airflow.apache.org/docs/apache-airflow-providers-mongo) | `mongo` |
| [apache-airflow-providers-openlineage](https://airflow.apache.org/docs/apache-airflow-providers-openlineage) | `openlineage` |
| [apache-airflow-providers-salesforce](https://airflow.apache.org/docs/apache-airflow-providers-salesforce) | `salesforce` |
| [apache-airflow-providers-ssh](https://airflow.apache.org/docs/apache-airflow-providers-ssh) | `ssh` |

Downloading official packages[¶](https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/index.html#downloading-official-packages "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can download officially released packages and verify their checksums and signatures from the [Official Apache Download site](https://downloads.apache.org/airflow/providers/)

*   [The apache-airflow-providers-amazon 9.21.0 sdist package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_amazon-9.21.0.tar.gz) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_amazon-9.21.0.tar.gz.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_amazon-9.21.0.tar.gz.sha512))

*   [The apache-airflow-providers-amazon 9.21.0 wheel package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_amazon-9.21.0-py3-none-any.whl) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_amazon-9.21.0-py3-none-any.whl.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_amazon-9.21.0-py3-none-any.whl.sha512))

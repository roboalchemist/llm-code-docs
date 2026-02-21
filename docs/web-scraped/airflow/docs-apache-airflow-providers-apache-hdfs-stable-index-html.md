# Source: https://airflow.apache.org/docs/apache-airflow-providers-apache-hdfs/stable/index.html

Title: apache-airflow-providers-apache-hdfs — apache-airflow-providers-apache-hdfs Documentation

URL Source: https://airflow.apache.org/docs/apache-airflow-providers-apache-hdfs/stable/index.html

Markdown Content:
apache-airflow-providers-apache-hdfs package[¶](https://airflow.apache.org/docs/apache-airflow-providers-apache-hdfs/stable/index.html#apache-airflow-providers-apache-hdfs-package "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Hadoop Distributed File System (HDFS)](https://hadoop.apache.org/docs/r1.2.1/hdfs_design.html) and [WebHDFS](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/WebHDFS.html).

Release: 4.11.3

Provider package[¶](https://airflow.apache.org/docs/apache-airflow-providers-apache-hdfs/stable/index.html#provider-package "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------

This package is for the `apache.hdfs` provider. All classes for this package are included in the `airflow.providers.apache.hdfs` python package.

Installation[¶](https://airflow.apache.org/docs/apache-airflow-providers-apache-hdfs/stable/index.html#installation "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------

You can install this package on top of an existing Airflow installation via `pip install apache-airflow-providers-apache-hdfs`. For the minimum Airflow version supported, see `Requirements` below.

Requirements[¶](https://airflow.apache.org/docs/apache-airflow-providers-apache-hdfs/stable/index.html#requirements "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------

The minimum Apache Airflow version supported by this provider distribution is `2.11.0`.

| PIP package | Version required |
| --- | --- |
| `apache-airflow` | `>=2.11.0` |
| `apache-airflow-providers-common-compat` | `>=1.12.0` |
| `hdfs[avro,dataframe,kerberos]` | `>=2.5.4; python_version < "3.12"` |
| `hdfs[avro,dataframe,kerberos]` | `>=2.7.3; python_version >= "3.12"` |
| `fastavro` | `>=1.10.0; python_version >= "3.13"` |
| `pandas` | `>=2.1.2; python_version < "3.13"` |
| `pandas` | `>=2.2.3; python_version >= "3.13"` |

Cross provider package dependencies[¶](https://airflow.apache.org/docs/apache-airflow-providers-apache-hdfs/stable/index.html#cross-provider-package-dependencies "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Those are dependencies that might be needed in order to use all the features of the package. You need to install the specified provider distributions in order to use them.

You can install such cross-provider dependencies when installing from PyPI. For example:

pip install apache-airflow-providers-apache-hdfs[common.compat]

| Dependent package | Extra |
| --- | --- |
| [apache-airflow-providers-common-compat](https://airflow.apache.org/docs/apache-airflow-providers-common-compat) | `common.compat` |

Downloading official packages[¶](https://airflow.apache.org/docs/apache-airflow-providers-apache-hdfs/stable/index.html#downloading-official-packages "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can download officially released packages and verify their checksums and signatures from the [Official Apache Download site](https://downloads.apache.org/airflow/providers/)

*   [The apache-airflow-providers-apache-hdfs 4.11.3 sdist package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_apache_hdfs-4.11.3.tar.gz) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_apache_hdfs-4.11.3.tar.gz.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_apache_hdfs-4.11.3.tar.gz.sha512))

*   [The apache-airflow-providers-apache-hdfs 4.11.3 wheel package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_apache_hdfs-4.11.3-py3-none-any.whl) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_apache_hdfs-4.11.3-py3-none-any.whl.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_apache_hdfs-4.11.3-py3-none-any.whl.sha512))

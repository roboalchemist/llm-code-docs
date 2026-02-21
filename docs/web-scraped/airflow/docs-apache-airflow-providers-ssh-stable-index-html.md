# Source: https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/index.html

Title: apache-airflow-providers-ssh — apache-airflow-providers-ssh Documentation

URL Source: https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/index.html

Markdown Content:
apache-airflow-providers-ssh — apache-airflow-providers-ssh Documentation
===============

[](https://airflow.apache.org/)

[Community](https://airflow.apache.org/community/)[Meetups](https://airflow.apache.org/meetups/)[Documentation](https://airflow.apache.org/docs/)[Use Cases](https://airflow.apache.org/use-cases/)[Announcements](https://airflow.apache.org/announcements/)[Blog](https://airflow.apache.org/blog/)[Ecosystem](https://airflow.apache.org/ecosystem/)

*    Light 
*    Dark 
*    Auto 

[Community](https://airflow.apache.org/community/)[Meetups](https://airflow.apache.org/meetups/)[Documentation](https://airflow.apache.org/docs/)[Use Cases](https://airflow.apache.org/use-cases/)[Announcements](https://airflow.apache.org/announcements/)[Blog](https://airflow.apache.org/blog/)[Ecosystem](https://airflow.apache.org/ecosystem/)

Content

[](https://airflow.apache.org/)

[Version: 4.3.1](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/index.html#)

[Stable (4.3.1)](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/index.html)[4.3.1](https://airflow.apache.org/docs/apache-airflow-providers-ssh/4.3.1/index.html)[4.2.1](https://airflow.apache.org/docs/apache-airflow-providers-ssh/4.2.1/index.html)[4.1.6](https://airflow.apache.org/docs/apache-airflow-providers-ssh/4.1.6/index.html)[4.0.1](https://airflow.apache.org/docs/apache-airflow-providers-ssh/4.0.1/index.html)[3.14.0](https://airflow.apache.org/docs/apache-airflow-providers-ssh/3.14.0/index.html)[3.13.1](https://airflow.apache.org/docs/apache-airflow-providers-ssh/3.13.1/index.html)[3.12.0](https://airflow.apache.org/docs/apache-airflow-providers-ssh/3.12.0/index.html)[3.11.2](https://airflow.apache.org/docs/apache-airflow-providers-ssh/3.11.2/index.html)[3.10.1](https://airflow.apache.org/docs/apache-airflow-providers-ssh/3.10.1/index.html)[3.9.0](https://airflow.apache.org/docs/apache-airflow-providers-ssh/3.9.0/index.html)[3.8.1](https://airflow.apache.org/docs/apache-airflow-providers-ssh/3.8.1/index.html)[3.7.3](https://airflow.apache.org/docs/apache-airflow-providers-ssh/3.7.3/index.html)[3.6.0](https://airflow.apache.org/docs/apache-airflow-providers-ssh/3.6.0/index.html)[3.5.0](https://airflow.apache.org/docs/apache-airflow-providers-ssh/3.5.0/index.html)[3.4.0](https://airflow.apache.org/docs/apache-airflow-providers-ssh/3.4.0/index.html)[3.3.0](https://airflow.apache.org/docs/apache-airflow-providers-ssh/3.3.0/index.html)[3.2.0](https://airflow.apache.org/docs/apache-airflow-providers-ssh/3.2.0/index.html)[3.1.0](https://airflow.apache.org/docs/apache-airflow-providers-ssh/3.1.0/index.html)[3.0.0](https://airflow.apache.org/docs/apache-airflow-providers-ssh/3.0.0/index.html)[2.4.4](https://airflow.apache.org/docs/apache-airflow-providers-ssh/2.4.4/index.html)

Search docs⌘K

Basics

*   [Home](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/index.html#)
*   [Changelog](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/changelog.html)
*   [Security](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/security.html)

Guides

*   [Connection types](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/connections/ssh.html)
*   [Operators](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/operators/ssh_remote_job.html)

References

*   [Python API](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/_api/airflow/providers/ssh/index.html)

Resources

*   [PyPI Repository](https://pypi.org/project/apache-airflow-providers-ssh/)
*   [Installing from sources](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/installing-providers-from-sources.html)

Commits

*   [Detailed list of commits](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/commits.html)

[Version: 4.3.1](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/index.html#)

[Stable (4.3.1)](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/index.html)[4.3.1](https://airflow.apache.org/docs/apache-airflow-providers-ssh/4.3.1/index.html)[4.2.1](https://airflow.apache.org/docs/apache-airflow-providers-ssh/4.2.1/index.html)[4.1.6](https://airflow.apache.org/docs/apache-airflow-providers-ssh/4.1.6/index.html)[4.0.1](https://airflow.apache.org/docs/apache-airflow-providers-ssh/4.0.1/index.html)[3.14.0](https://airflow.apache.org/docs/apache-airflow-providers-ssh/3.14.0/index.html)[3.13.1](https://airflow.apache.org/docs/apache-airflow-providers-ssh/3.13.1/index.html)[3.12.0](https://airflow.apache.org/docs/apache-airflow-providers-ssh/3.12.0/index.html)[3.11.2](https://airflow.apache.org/docs/apache-airflow-providers-ssh/3.11.2/index.html)[3.10.1](https://airflow.apache.org/docs/apache-airflow-providers-ssh/3.10.1/index.html)[3.9.0](https://airflow.apache.org/docs/apache-airflow-providers-ssh/3.9.0/index.html)[3.8.1](https://airflow.apache.org/docs/apache-airflow-providers-ssh/3.8.1/index.html)[3.7.3](https://airflow.apache.org/docs/apache-airflow-providers-ssh/3.7.3/index.html)[3.6.0](https://airflow.apache.org/docs/apache-airflow-providers-ssh/3.6.0/index.html)[3.5.0](https://airflow.apache.org/docs/apache-airflow-providers-ssh/3.5.0/index.html)[3.4.0](https://airflow.apache.org/docs/apache-airflow-providers-ssh/3.4.0/index.html)[3.3.0](https://airflow.apache.org/docs/apache-airflow-providers-ssh/3.3.0/index.html)[3.2.0](https://airflow.apache.org/docs/apache-airflow-providers-ssh/3.2.0/index.html)[3.1.0](https://airflow.apache.org/docs/apache-airflow-providers-ssh/3.1.0/index.html)[3.0.0](https://airflow.apache.org/docs/apache-airflow-providers-ssh/3.0.0/index.html)[2.4.4](https://airflow.apache.org/docs/apache-airflow-providers-ssh/2.4.4/index.html)

Search docs⌘K

Basics

*   [Home](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/index.html#)
*   [Changelog](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/changelog.html)
*   [Security](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/security.html)

Guides

*   [Connection types](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/connections/ssh.html)
*   [Operators](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/operators/ssh_remote_job.html)

References

*   [Python API](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/_api/airflow/providers/ssh/index.html)

Resources

*   [PyPI Repository](https://pypi.org/project/apache-airflow-providers-ssh/)
*   [Installing from sources](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/installing-providers-from-sources.html)

Commits

*   [Detailed list of commits](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/commits.html)

*   [Home](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/index.html#)
*   [`apache-airflow-providers-ssh`](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/index.html)

↑↓ Navigate⏎ Select Esc Close

`apache-airflow-providers-ssh`[¶](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/index.html#apache-airflow-providers-ssh "Link to this heading")
=====================================================================================================================================================================

apache-airflow-providers-ssh package[¶](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/index.html#apache-airflow-providers-ssh-package "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Secure Shell (SSH)](https://tools.ietf.org/html/rfc4251)

Release: 4.3.1

Provider package[¶](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/index.html#provider-package "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------

This package is for the `ssh` provider. All classes for this package are included in the `airflow.providers.ssh` python package.

Installation[¶](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/index.html#installation "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------

You can install this package on top of an existing Airflow installation via `pip install apache-airflow-providers-ssh`. For the minimum Airflow version supported, see `Requirements` below.

Requirements[¶](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/index.html#requirements "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------

The minimum Apache Airflow version supported by this provider distribution is `2.11.0`.

| PIP package | Version required |
| --- | --- |
| `apache-airflow` | `>=2.11.0` |
| `apache-airflow-providers-common-compat` | `>=1.12.0` |
| `asyncssh` | `>=2.12.0` |
| `paramiko` | `>=2.9.0,<4.0.0` |
| `sshtunnel` | `>=0.3.2` |

Cross provider package dependencies[¶](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/index.html#cross-provider-package-dependencies "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Those are dependencies that might be needed in order to use all the features of the package. You need to install the specified provider distributions in order to use them.

You can install such cross-provider dependencies when installing from PyPI. For example:

pip install apache-airflow-providers-ssh[common.compat]

| Dependent package | Extra |
| --- | --- |
| [apache-airflow-providers-common-compat](https://airflow.apache.org/docs/apache-airflow-providers-common-compat) | `common.compat` |

Downloading official packages[¶](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/index.html#downloading-official-packages "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can download officially released packages and verify their checksums and signatures from the [Official Apache Download site](https://downloads.apache.org/airflow/providers/)

*   [The apache-airflow-providers-ssh 4.3.1 sdist package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_ssh-4.3.1.tar.gz) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_ssh-4.3.1.tar.gz.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_ssh-4.3.1.tar.gz.sha512))

*   [The apache-airflow-providers-ssh 4.3.1 wheel package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_ssh-4.3.1-py3-none-any.whl) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_ssh-4.3.1-py3-none-any.whl.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_ssh-4.3.1-py3-none-any.whl.sha512))

Previous[Next](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/changelog.html "Changelog")

Was this entry helpful?

*   [`apache-airflow-providers-ssh`](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/index.html#)
    *   [apache-airflow-providers-ssh package](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/index.html#apache-airflow-providers-ssh-package)
    *   [Provider package](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/index.html#provider-package)
    *   [Installation](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/index.html#installation)
    *   [Requirements](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/index.html#requirements)
    *   [Cross provider package dependencies](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/index.html#cross-provider-package-dependencies)
    *   [Downloading official packages](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/index.html#downloading-official-packages)

[Suggest a change on this page](https://github.com/apache/airflow/edit/main/providers/ssh/docs/index.rst)

[](https://github.com/apache/airflow)[](https://github.com/apache/airflow/issues)[](https://s.apache.org/airflow-slack)[](https://stackoverflow.com/questions/tagged/airflow)[](https://www.youtube.com/channel/UCSXwxpWZQ7XZ1WL3wqevChA)

Want to be a part of Apache Airflow?[Join community](https://airflow.apache.org/community)

© The Apache Software Foundation 2026

[License](https://www.apache.org/licenses/)[Donate](https://www.apache.org/foundation/sponsorship.html)[Events](https://events.apache.org/)[Thanks](https://www.apache.org/foundation/thanks.html)[Security](https://www.apache.org/security/)[Privacy](https://privacy.apache.org/policies/privacy-policy-public.html)[Code of conduct](https://airflow.apache.org/code-of-conduct/)

 Apache Airflow, Apache, Airflow, the Airflow logo, and the Apache logo are either registered trademarks or trademarks of The Apache Software Foundation. All other products or name brands are trademarks of their respective holders, including The Apache Software Foundation.

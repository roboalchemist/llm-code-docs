# Source: https://docs.envzero.com/changelogs/2022/09/removing-python-2-and-other-3rd-party-updates.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🐍 Removing Python 2, and other 3rd party updates

> To improve the security of our system we periodically update 3rd party software we are using. On **2022 Oct 30** we are going to release a massive update to the env0 deployment container, but unfortunately this will introduce breaking changes and we want to give you heads up, so you can prepare in advance.

To improve the security of our system we periodically update 3rd party software we are using. On **2022 Oct 30** we are going to release a massive update to the env0 [deployment container](/guides/admin-guide/custom-flows#the-deployment-container), but unfortunately, this will introduce breaking changes and we want to give you a heads up, so you can prepare in advance.

> 📘
>
> If you are not using [custom flows](/guides/admin-guide/custom-flows) you shouldn't notice any difference.

### Alpine Linux update

We are updating our container's base image from `alpine:3.11` to `alpine:3.16`.

### Python 2 has been removed

Our container will not have `python2` anymore, `python` and `pip` will pointing to `python3` and `pip3` respectively.

### Other updates

|                   | Old version                        | New version                          |
| :---------------- | :--------------------------------- | :----------------------------------- |
| Alpine Linux      | 3.11.12                            | 3.16.2                               |
| bash              | 5.0.11(1)-release                  | 5.1.16(1)-release                    |
| NodeJS            | 16.10.0                            | 16.17.0                              |
| npm               | 7.24.0                             | 8.19.2                               |
| yarn              | 1.22.5                             | 1.22.19                              |
| git               | 2.24.4                             | 2.36.2                               |
| python2           | 2.7.18                             | **Removed**                          |
| pip2              | 18.1                               | **Removed**                          |
| python3           | 3.8.2                              | 3.10.5                               |
| pip3              | 20.2                               | 22.1.1                               |
| aws (AWS CLI v1)  | 1.18.115                           | 1.22.77                              |
| az (Azure CLI)    | 2.28.1                             | 2.40.0                               |
| pwsh (PowerShell) | 7.0.3                              | 7.2.6                                |
| jq                | jq-master-v20191114-85-g260888d269 | jq-master-v20220328-1108-g836ca403de |
| OpenSSL           | 1.1.1g                             | 1.1.1q                               |
| OpenSSH           | 8.1p1                              | 9.0p1                                |

Built with [Mintlify](https://mintlify.com).

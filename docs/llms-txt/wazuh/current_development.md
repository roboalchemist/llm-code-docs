# Source: https://documentation.wazuh.com/current/development/index.md

<!-- Copyright (C) 2015, Wazuh, Inc. -->

<a id="development"></a>

# Development

This section of the documentation helps developers to understand Wazuh at the development level. It provides the technical resources required to understand the Wazuh architecture, extend its capabilities, and tailor the platform to specific operational requirements.

> ##### Contents
> 
> * [Client keys file](client-keys.md)
>   * [File format](client-keys.md#file-format)
>   * [Void entries](client-keys.md#void-entries)
>   * [Examples](client-keys.md#examples)
> * [Standard Wazuh message format](message-format.md)
>   * [Input logs](message-format.md#input-logs)
>   * [Standard Wazuh event](message-format.md#standard-wazuh-event)
>   * [Secure message format](message-format.md#secure-message-format)
> * [Makefile options](makefile.md)
>   * [Compiling the source code](makefile.md#compiling-the-source-code)
>   * [Makefile reference](makefile.md#makefile-reference)
> * [Wazuh server cluster](wazuh-cluster.md)
>   * [Introduction](wazuh-cluster.md#introduction)
>   * [Architecture overview](wazuh-cluster.md#architecture-overview)
>   * [Code structure](wazuh-cluster.md#code-structure)
>   * [Troubleshooting](wazuh-cluster.md#troubleshooting)
> * [Wazuh package generation](packaging/index.md)
>   * [Virtual machine](packaging/generate-ova.md)
>   * [Wazuh server](packaging/generate-server-package.md)
>   * [Wazuh indexer](packaging/generate-indexer-package.md)
>   * [Wazuh dashboard](packaging/generate-dashboard-package.md)
>   * [Wazuh agent](packaging/generate-agent-package.md)
> * [Wazuh-Logtest](wazuh-logtest.md)
>   * [Sessions](wazuh-logtest.md#sessions)
> * [RBAC database integrity](rbac-database-integrity.md)
>   * [How the database upgrade process works](rbac-database-integrity.md#how-the-database-upgrade-process-works)
>   * [Migration examples](rbac-database-integrity.md#migration-examples)
> * [Configuring core dump generation](coredump.md)
>   * [Red Hat based OSs](coredump.md#red-hat-based-oss)
>   * [Debian based OSs](coredump.md#debian-based-oss)
>   * [macOS endpoints](coredump.md#macos-endpoints)
>   * [Windows endpoints](coredump.md#windows-endpoints)

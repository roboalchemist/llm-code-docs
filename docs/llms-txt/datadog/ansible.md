# Source: https://docs.datadoghq.com/agent/supported_platforms/ansible.md

---
title: Ansible
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Agent > Supported Platforms > Ansible
source_url: https://docs.datadoghq.com/supported_platforms/ansible/index.html
---

# Ansible

## Overview{% #overview %}

The [Datadog Ansible collection](https://github.com/ansible-collections/Datadog), `datadog.dd`, is the official collection of Ansible-related Datadog content. It contains the [Ansible Datadog Role](https://github.com/DataDog/ansible-datadog/), which can be accessed as `datadog.dd.agent`, allowing you to install and configure the Datadog Agent and integrations.

## Prerequisites{% #prerequisites %}

- Ansible v2.10+.

- Supports most Debian, RHEL-based and SUSE-based Linux distributions, macOS, and Windows.

- To manage Windows hosts, install the `ansible.windows` collection:

  ```shell
  ansible-galaxy collection install ansible.windows
  ```

- When managing openSUSE/SLES hosts, install the `community.general` collection:

  ```shell
  ansible-galaxy collection install community.general
  ```

## Setup{% #setup %}

### Installing the ansible collection{% #installing-the-ansible-collection %}

Before using this collection, install it with the Ansible Galaxy command-line tool:

```
ansible-galaxy collection install datadog.dd
```

Alternatively, include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`. Include the following in `requirments.yml`:

```yaml
collections:
  - name: datadog.dd
```

**Note**: If you install the collection from Ansible Galaxy, it will not be upgraded automatically when you upgrade the Ansible package. To upgrade the collection to the latest available version, run the following command:

```
ansible-galaxy collection install datadog.dd --upgrade
```

You can install a specific version of the collection, for example, if you need to downgrade when something is broken in the latest version (please report an issue in this repository). The following syntax shows how to install version 5.0.0:

```
ansible-galaxy collection install datadog.dd:==5.0.0
```

See [using Ansible collections](https://docs.ansible.com/ansible/devel/user_guide/collections_using.html) for more details.

The Datadog Ansible collection is also available through the [Red Hat Automation Hub](https://console.redhat.com/ansible/automation-hub/repo/published/datadog/dd/), where it is officially certified by Red Hat.

### Installing the Agent{% #installing-the-agent %}

Follow the [in-app instructions in Fleet Automation](https://app.datadoghq.com/fleet/install-agent/latest?platform=ansible) to install the Datadog Ansible Collection for your platform (Linux, Windows or macOS) and copy a pre-filled playbook snippet. **Note**: You must run Ansible `v2.10` or higher.

### Deploying the Agent{% #deploying-the-agent %}

To deploy the Datadog Agent on hosts, add the Datadog role and your API key to your playbook:

```yaml
- hosts: servers
  tasks:
    - name: Import the Datadog Agent role from the Datadog collection
      import_role:
        name: datadog.dd.agent
  vars:
    datadog_api_key: "<YOUR_DD_API_KEY>"
```

**Note**: If you install the collection through the Ansible Automation Hub, OpenSUSE/SLES functionality depends on a community collection `community.general`. Red Hat Support does not provide support for issues related to community content. Direct all support issues for OpenSUSE/SLES to [Datadog Support](https://docs.datadoghq.com/help/).

## Testing{% #testing %}

The Datadog Collection is tested on CentOS, Debian, Rocky Linux, OpenSUSE, Windows and macOS. Tests are run with latest `ansible-lint` version and sanity checks running with Python 3.9 to Python 3.12.

## Support{% #support %}

If you need support, you can create an issue in the [`ansible-collections` GitHub repo](https://github.com/ansible-collections/Datadog), or contact [Datadog Support](https://docs.datadoghq.com/help/).

## Release notes{% #release-notes %}

You can follow changes in the [CHANGELOG](https://github.com/ansible-collections/Datadog/blob/main/CHANGELOG.rst) file.

## Further reading{% #further-reading %}

- [Automate Agent installation with the Datadog Ansible collection](https://www.datadoghq.com/blog/datadog-ansible-collection/)
- Collection role: `datadog.dd.agent`: Installation and configuration of the Datadog Agent.
  - See [the official documentation for the role](https://docs.datadoghq.com/agent/guide/ansible_standalone_role/#setup).
  - See [the repository for the standalone role](https://github.com/DataDog/ansible-datadog#readme).

## License information{% #license-information %}

The Datadog Ansible collection is published under [Apache License 2.0](https://github.com/ansible-collections/Datadog/blob/main/LICENSE).

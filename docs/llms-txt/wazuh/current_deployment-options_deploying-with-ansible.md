# Source: https://documentation.wazuh.com/current/deployment-options/deploying-with-ansible/index.md

<!-- Copyright (C) 2015, Wazuh, Inc. -->

<a id="wazuh-ansible"></a>

# Deployment with Ansible

Ansible is an open source platform designed for automating tasks. It comes with playbooks, a descriptive language based on YAML, that makes it easy to create and describe automation jobs. Also, Ansible communicates with every host over SSH, making it very secure. See [Ansible overview](https://www.ansible.com/how-ansible-works) for more information. You can use Ansible to deploy a Wazuh environment with the Wazuh indexer, dashboard, manager, and agents.

> ##### Contents
> 
> * [Requirements](guide/requirements.md)
> * [Installing Ansible](guide/install-ansible.md)
>   * [Installation on CentOS/RHEL/Fedora](guide/install-ansible.md#installation-on-centos-rhel-fedora)
>   * [Installation on Debian/Ubuntu](guide/install-ansible.md#installation-on-debian-ubuntu)
> * [Remote endpoint connection](setup-remote-systems.md)
>   * [Managing Linux endpoints with Ansible](setup-remote-systems.md#managing-linux-endpoints-with-ansible)
>     * [Authenticate with passwords](setup-remote-systems.md#authenticate-with-passwords)
>     * [Authenticate with SSH key-pairing](setup-remote-systems.md#authenticate-with-ssh-key-pairing)
>   * [Managing Windows endpoints with Ansible](setup-remote-systems.md#managing-windows-endpoints-with-ansible)
>     * [Requirements](setup-remote-systems.md#requirements)
>     * [Configuring WinRM on Windows endpoints](setup-remote-systems.md#configuring-winrm-on-windows-endpoints)
>   * [Adding endpoints to the inventory](setup-remote-systems.md#adding-endpoints-to-the-inventory)
>   * [Testing the Ansible connection to remote endpoints](setup-remote-systems.md#testing-the-ansible-connection-to-remote-endpoints)
>     * [Linux endpoints](setup-remote-systems.md#linux-endpoints)
>     * [Windows endpoints](setup-remote-systems.md#windows-endpoints)
> * [Deploying Wazuh](guide/index.md)
>   * [Installing the Wazuh central components](guide/index.md#installing-the-wazuh-central-components)
>     * [All-in-one deployment](guide/index.md#all-in-one-deployment)
>     * [Wazuh cluster deployment](guide/index.md#wazuh-cluster-deployment)
>   * [Installing the Wazuh agent](guide/index.md#installing-the-wazuh-agent)
>     * [Prerequisites](guide/index.md#prerequisites)
>     * [Access the wazuh-ansible directory](guide/index.md#agent-access-wazuh-ansible-directory)
>     * [Prepare the playbook](guide/index.md#agent-prepare-playbook)
>     * [Run the playbook](guide/index.md#agent-run-playbook)
> * [Roles](roles/index.md)
>   * [Wazuh indexer](roles/wazuh-indexer.md)
>   * [Wazuh dashboard](roles/wazuh-dashboard.md)
>   * [Filebeat](roles/wazuh-filebeat.md)
>   * [Wazuh manager](roles/wazuh-manager.md)
>   * [Wazuh agent](roles/wazuh-agent.md)
> * [Variables references](reference.md)
>   * [Wazuh indexer](reference.md#wazuh-indexer)
>   * [Wazuh dashboard](reference.md#wazuh-dashboard)
>   * [Filebeat](reference.md#filebeat)
>   * [Wazuh manager](reference.md#wazuh-manager)
>   * [Wazuh agent](reference.md#wazuh-agent)

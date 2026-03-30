# Source: https://docs.infrahub.app/demo-dc/install.md

# Source: https://docs.infrahub.app/backup/guides/install.md

# Source: https://docs.infrahub.app/ansible/references/roles/install.md

The **Infrahub Installation Role** in the **OpsMill Infrahub Ansible Collection** allows you to install and configure Infrahub using `Docker` and `systemd`.

# Overview

This role automates the installation and configuration of Infrahub by:

* Setting up the required directory structure
* Configuring Docker Compose
* Installing and configuring `systemd` services
* Managing Infrahub configuration

# Requirements

This role requires:

* Docker Engine with Docker Compose v2 to be installed
* Root or `sudo` access for `systemd` service installation (on the target server)

# Role variables

| Variable                                 | Type   | Default                       | Description                                                                                                |
| ---------------------------------------- | ------ | ----------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `install_infrahub_version`               | `str`  |                               | Version of Infrahub to install. Can be any Docker image tag name.                                          |
| `install_infrahub_url`                   | `str`  | `https://infrahub.opsmill.io` | URL from where to fetch the Infrahub Docker Compose file.                                                  |
| `install_infrahub_install_directory`     | `str`  | `/opt/infrahub`               | Install directory for the Infrahub files (Docker Compose and configuration file).                          |
| `install_infrahub_config`                | `dict` |                               | Environment variables to pass as configuration for Infrahub.                                               |
| `install_infrahub_docker_project`        | `str`  | `infrahub`                    | Docker project name to use when starting Infrahub.                                                         |
| `install_infrahub_docker_pull_images`    | `bool` | `true`                        | Whether to pull the required Docker images.                                                                |
| `install_infrahub_setup_systemd`         | `bool` | `true`                        | Whether to install the `systemd` service for Infrahub.                                                     |
| `install_infrahub_systemd_directory`     | `str`  | `/etc/systemd/system/`        | Where to install the `systemd` service unit file.                                                          |
| `install_infrahub_systemd_service_state` | `str`  | `restarted`                   | Target state of the `systemd` service. Can be used to avoid starting Infrahub during the role's execution. |

# Installation example

* Quick start
* Production setup

For a basic installation with default settings:

install\_infrahub\_minimal.yml

```
- name: Install Infrahub
  hosts: infrahub_servers
  become: true

  roles:
    - role: opsmill.infrahub.install
      vars:
        install_infrahub_version: "latest"
```

## Production setup[​](#production-setup "Direct link to Production setup")

For a production environment with custom configuration:

install\_infrahub\_advanced.yml

```
- name: Install Infrahub with custom configuration
  hosts: infrahub_servers
  become: true

  roles:
    - role: opsmill.infrahub.install
      vars:
        install_infrahub_version: "2.0.0"
        install_infrahub_install_directory: "/usr/local/infrahub"
        install_infrahub_docker_project: "infrahub_prod"
        install_infrahub_docker_pull_images: true
        install_infrahub_setup_systemd: true
        install_infrahub_systemd_service_state: "started"
        infrahub_config:
          INFRAHUB_ADMIN_EMAIL: "admin@example.com"
          INFRAHUB_ADMIN_PASSWORD: "secure_password"
          INFRAHUB_DATABASE_URL: "postgresql://user:pass@db:5432/infrahub"
```

# Usage

To install Infrahub, use:

```
ansible-playbook install_infrahub.yml -i inventory.yml
```

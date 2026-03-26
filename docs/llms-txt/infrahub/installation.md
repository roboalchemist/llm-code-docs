# Source: https://docs.infrahub.app/guides/installation.md

# Source: https://docs.infrahub.app/sync/guides/installation.md

# Source: https://docs.infrahub.app/python-sdk/guides/installation.md

# Source: https://docs.infrahub.app/mcp/guides/installation.md

# Source: https://docs.infrahub.app/exporter/guides/installation.md

# Source: https://docs.infrahub.app/emma/getting-started/installation.md

# Source: https://docs.infrahub.app/demo-service-catalog/getting-started/installation.md

# Source: https://docs.infrahub.app/ansible/guides/installation.md

# Install `opsmill.infrahub` Ansible collection

info

This guide assumes you have basic knowledge of Ansible and its ecosystem. For more information on using Ansible, please refer to the [official Ansible documentation](https://docs.ansible.com/ansible/latest/index.html).

## Requirements[​](#requirements "Direct link to Requirements")

* You must be running one of the two most recent releases of Infrahub
* A Infrahub API token when using modules (at least read-only for the inventory).
* Python 3.10+
* Python modules:
  <!-- -->
  * infrahub-sdk
* Ansible 2.15+

## Installation[​](#installation "Direct link to Installation")

### Python modules and Ansible[​](#python-modules-and-ansible "Direct link to Python modules and Ansible")

```
pip install infrahub-sdk
pip install ansible
```

### Infrahub Ansible collection[​](#infrahub-ansible-collection "Direct link to Infrahub Ansible collection")

Before using this collection, you need to install it with the Ansible Galaxy command-line tool:

```
ansible-galaxy collection install opsmill.infrahub
```

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:

```
collections:
  - name: opsmill.infrahub
```

To upgrade the collection to the latest available version, run the following command:

```
ansible-galaxy collection install opsmill.infrahub --upgrade
```

You can also install a specific version of the collection, for example, if you need to downgrade. Use the following syntax to install a specific version:

```
ansible-galaxy collection install opsmill.infrahub:==VERSION
```

See using [Ansible collections](https://docs.ansible.com/ansible/latest/collections_guide/collections_installing.html) for more Collapsible.

### Other installation options[​](#other-installation-options "Direct link to Other installation options")

#### Build from source[​](#build-from-source "Direct link to Build from source")

* Build from source
* Build from source (Pull Request)

1. **Step 1**: `git clone git@github.com:opsmill/infrahub-ansible.git`
2. **Step 2**: `cd ansible_modules`
3. **Step 3**: `ansible-galaxy collection build .`
4. **Step 4**: `ansible-galaxy collection install opsmill-infrahub*.tar.gz`

*For more Collapsible on building from source, please refer to \[our dedicated documentation]\(link if available).*

*Useful for testing changes in Pull Requests.*

1. **Step 1**: `git clone git@github.com:opsmill/infrahub-ansible.git`
2. **Step 2**: `cd ansible_modules`
3. **Step 3**: `git fetch origin pull/<pr #>/head:`
4. **Step 4**: `git checkout <branch_name>`
5. **Step 5**: `ansible-galaxy collection build .`
6. **Step 6**: `ansible-galaxy collection install opsmill-infrahub*.tar.gz`

*For detailed information on checking out pull requests locally, please refer to [GitHub's Documentation](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/checking-out-pull-requests-locally).*

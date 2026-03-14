# Source: https://ansible-runner.readthedocs.io/

Title: Ansible Runner — Ansible Runner Documentation

URL Source: https://ansible-runner.readthedocs.io/

Markdown Content:
Ansible Runner is a tool and python library that helps when interfacing with Ansible directly or as part of another system whether that be through a container image interface, as a standalone tool, or as a Python module that can be imported. The goal is to provide a stable and consistent interface abstraction to Ansible. This allows **Ansible** to be embedded into other systems that don’t want to manage the complexities of the interface on their own (such as CI/CD platforms, Jenkins, or other automated tooling).

**Ansible Runner** represents the modularization of the part of [Ansible AWX](https://github.com/ansible/awx) that is responsible for running `ansible` and `ansible-playbook` tasks and gathers the output from it. It does this by presenting a common interface that doesn’t change, even as **Ansible** itself grows and evolves.

Part of what makes this tooling useful is that it can gather its inputs in a flexible way (See [Introduction to Ansible Runner](https://docs.ansible.com/projects/runner/en/latest/intro/#intro):). It also has a system for storing the output (stdout) and artifacts (host-level event data, fact data, etc) of the playbook run.

There are 3 primary ways of interacting with **Runner**

* A standalone command line tool (`ansible-runner`) that can be started in the foreground or run in the background asynchronously

* A python module - library interface

**Ansible Runner** can also be configured to send status and event data to other systems using a plugin interface, see [Sending Runner Status and Events to External Systems](https://docs.ansible.com/projects/runner/en/latest/external_interface/#externalintf).

Examples of this could include:

* Sending status to Ansible AWX

* Sending events to an external logging service

Contents:

* [Introduction to Ansible Runner](https://docs.ansible.com/projects/runner/en/latest/intro/)
* [Installing Ansible Runner](https://docs.ansible.com/projects/runner/en/latest/install/)
* [Community](https://docs.ansible.com/projects/runner/en/latest/community/)
* [Sending Runner Status and Events to External Systems](https://docs.ansible.com/projects/runner/en/latest/external_interface/)
* [Using Runner as a standalone command line tool](https://docs.ansible.com/projects/runner/en/latest/standalone/)
* [Using Runner as a Python Module Interface to Ansible](https://docs.ansible.com/projects/runner/en/latest/python_interface/)
* [Using Runner with Execution Environments](https://docs.ansible.com/projects/runner/en/latest/execution_environments/)
* [Remote job execution](https://docs.ansible.com/projects/runner/en/latest/remote_jobs/)
* [Developer Documentation](https://docs.ansible.com/projects/runner/en/latest/modules/)

Indices and tables[](https://ansible-runner.readthedocs.io/#indices-and-tables "Link to this heading")
-------------------------------------------------------------------------------------------------------

* [Index](https://docs.ansible.com/projects/runner/en/latest/genindex/)

* [Module Index](https://docs.ansible.com/projects/runner/en/latest/py-modindex/)

* [Search Page](https://docs.ansible.com/projects/runner/en/latest/search/)

# quick_start

Source: https://developer.ui.com/protect/v6.2.83/quick_start

UniFi APIEndpoints combined into Ansible Modules for customized workflows.Installation
Python dependencies
The module requires httpx and urllib3 python packages to be installed.
You can install them using pip:
pip install httpx urllib3
Installing the Ansible Collection
You can install the ubiquiti.unifi_api Ansible collection by downloading the collection archive and installing it with the following commands:
curl -L -o ubiquiti-unifi_api-latest.tar.gz https://apidoc-cdn.ui.com/ansible-module/ubiquiti-unifi_api-latest.tar.gzansible-galaxy collection install ubiquiti-unifi_api-latest.tar.gz
UniFi Protect API – Ansible Usage Guide
Version: 6.2.83
This guide shows how to call each operation using the ubiquiti.unifi_api.protect Ansible module.
Quick Start
Here is a basic example of how to use the ubiquiti.unifi_api.protect module to interact with the API.
Setting module_defaults allows you to avoid repeating common parameters for each task.
---- name: Using ubiquiti.unifi_api.protect with this API  hosts: localhost  gather_facts: false  vars:    site_id: "12341234-5656-7878-9090-123456789012" # Replace with your site ID  module_defaults:    group/ubiquiti.unifi_api.common:      base_url: "https://10.2.0.0" # Replace with your console IP      token: "{{ lookup('env', 'UBIQUITI_API_TOKEN') }}" # export UBIQUITI_API_TOKEN=... in your shell
You can then add tasks to call specific API operations. For example, to retrieve site information, you might add:
tasks:    - name: Get application info      ubiquiti.unifi_api.protect:        path: "/v1/meta/info"        method: GET      register: info
    - debug:        var: site_info.data
Idempotency
Currently, the ubiquiti.unifi_api.protect module does not guarantee idempotency for all operations.
When using operations that modify resources (e.g., create, update, delete),
it is recommended to implement additional checks in your playbooks to ensure that the desired state is achieved without
unintended side effects.
Example:
tasks:    - name: Get all live views      ubiquiti.unifi_api.protect:        path: "/v1/liveviews"        method: GET      register: result
    - name: Create live view      when: result.data | selectattr('name', 'equalto', 'TEST_VIEW') | list | length == 0      ubiquiti.unifi_api.protect:        path: "/v1/liveviews"        method: POST        body:          name: TEST_VIEW          layout: 1          isGlobal: true          slots: [ { cameras: [ "CAMERA_ID" ], cycleMode: "motion", cycleInterval: 10 } ]
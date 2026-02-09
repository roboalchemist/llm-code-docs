# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.netapp_active_directory.dataset.md

---
title: NetApp Active Directory
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > NetApp Active Directory
---

# NetApp Active Directory

NetApp Active Directory in Google Cloud is a managed service that integrates Cloud Volumes Service for NetApp with Microsoft Active Directory. It allows seamless authentication and access control for file shares using existing AD credentials. This enables centralized identity management, simplifies user access, and supports enterprise security policies for workloads that rely on Windows-based authentication.

```
gcp.netapp_active_directory
```

## Fields

| Title                  | ID   | Type          | Data Type                                                                                                                                                   | Description |
| ---------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string        |
| administrators         | core | array<string> | Optional. Users to be added to the Built-in Admininstrators group.                                                                                          |
| aes_encryption         | core | bool          | If enabled, AES encryption will be enabled for SMB communication.                                                                                           |
| ancestors              | core | array<string> |
| backup_operators       | core | array<string> | Optional. Users to be added to the Built-in Backup Operator active directory group.                                                                         |
| create_time            | core | timestamp     | Output only. Create time of the active directory.                                                                                                           |
| datadog_display_name   | core | string        |
| description            | core | string        | Description of the active directory.                                                                                                                        |
| dns                    | core | string        | Required. Comma separated list of DNS server IP addresses for the Active Directory domain.                                                                  |
| domain                 | core | string        | Required. Name of the Active Directory domain                                                                                                               |
| encrypt_dc_connections | core | bool          | If enabled, traffic between the SMB server to Domain Controller (DC) will be encrypted.                                                                     |
| kdc_hostname           | core | string        | Name of the active directory machine. This optional parameter is used only while creating kerberos volume                                                   |
| kdc_ip                 | core | string        | KDC server IP address for the active directory machine.                                                                                                     |
| labels                 | core | array<string> | Labels for the active directory.                                                                                                                            |
| ldap_signing           | core | bool          | Specifies whether or not the LDAP traffic needs to be signed.                                                                                               |
| name                   | core | string        | Identifier. The resource name of the active directory. Format: `projects/{project_number}/locations/{location_id}/activeDirectories/{active_directory_id}`. |
| net_bios_prefix        | core | string        | Required. NetBIOSPrefix is used as a prefix for SMB server name.                                                                                            |
| nfs_users_with_ldap    | core | bool          | If enabled, will allow access to local users and LDAP users. If access is needed for only LDAP users, it has to be disabled.                                |
| organization_id        | core | string        |
| organizational_unit    | core | string        | The Organizational Unit (OU) within the Windows Active Directory the user belongs to.                                                                       |
| parent                 | core | string        |
| password               | core | string        | Required. Password of the Active Directory domain administrator.                                                                                            |
| project_id             | core | string        |
| project_number         | core | string        |
| region_id              | core | string        |
| resource_name          | core | string        |
| security_operators     | core | array<string> | Optional. Domain users to be given the SeSecurityPrivilege.                                                                                                 |
| site                   | core | string        | The Active Directory site the service will limit Domain Controller discovery too.                                                                           |
| state                  | core | string        | Output only. The state of the AD.                                                                                                                           |
| state_details          | core | string        | Output only. The state details of the Active Directory.                                                                                                     |
| tags                   | core | hstore_csv    |
| username               | core | string        | Required. Username of the Active Directory domain administrator.                                                                                            |
| zone_id                | core | string        |

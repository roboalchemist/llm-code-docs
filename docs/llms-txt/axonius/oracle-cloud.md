# Source: https://docs.axonius.com/docs/oracle-cloud.md

# Oracle Cloud

Oracle Cloud is a computing service providing servers, storage, network, applications and services.

**Related Enforcement Actions:**

* [Oracle Cloud - Start or Stop Compute Instances](/docs/oracle-cloud-compute-action)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users
* Groups
* Compute Services
* Load Balancers
* Databases
* Compute Images
* Network/Firewall Rules
* Application Resources

## Parameters

1. **User OCID** - Specify the Oracle Cloud Identifier (OCID) for the Axonius user. For more details on User OCID, see [Oracle Cloud Infrastructure Documentation - Where to Get the Tenancy's OCID and User's OCID](https://docs.cloud.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#Other).

2. **Oracle Key File** - Upload an RSA key pair in PEM format (minimum 2048 bits). For more details on generating such key, see [Oracle Cloud Infrastructure Documentation - How to Generate an API Signing Key](https://docs.cloud.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#How).

3. **Key-Pair Fingerprint** - Specify the key fingerprint. To get the key fingerprint, you need to upload the PEM public key in the Oracle Cloud console. For more details, see [Oracle Cloud Infrastructure Documentation - How to Upload the Public Key](https://docs.cloud.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#How2).

4. **Tenancy OCID** -  Specify your tenancy Oracle Cloud Identifier (OCID). For more details on User OCID, see [Oracle Cloud Infrastructure Documentation - Where to Get the Tenancy's OCID and User's OCID](https://docs.cloud.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#Other).

5. **Oracle Cloud Infrastructure Region** - Specify your Region Identifier. For the complete region list, see [Oracle Cloud Infrastructure Documentation - Regions and Availability Domains](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/regions.htm).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Oracle%20Cloud" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Oracle%20Cloud.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Oracle Cloud services to fetch as devices** - Select the Oracle Cloud services to fetch as devices. Select from VM Clusters, Database Service, Kubernetes Clusters, Auto Scaling Groups, Network Firewall and Load Balancers.
2. **List of tags to parse as fields** - Enter a comma-separated list of tag keys to be saved as fields.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Required Permissions

To fetch information from Oracle Cloud API, you first need to create a user for Axonius, and put that user in at least one IAM group with any desired read-only permissions. For more details, see [Oracle Cloud Infrastructure Documentation - Adding Users](https://docs.cloud.oracle.com/iaas/Content/GSG/Tasks/addingusers.htm).

To add the appropriate permissions for the type of data you want to fetch, follow these steps on your Oracle console:

1. From the left hand navigation menu, select **Identity & Security** `>` **Policies**.
2. Use the compartment selector at the top of the **Policies** page to select which compartment you want to apply the policy to. For tenancy-wide policies, you usually need to select the root compartment.
3. After adding the appropriate compartment, you need to add permissions to the policy. Either select an existing policy to edit or click **Create Policy** to create a new one.
4. In the **Policy Editor**, add a **Policy Statement** - for example, `Allow group Admins to read users in tenancy`. Then, click **Create** or **Save Changes**.

All the permissions and policy statements you can add are listed below.

| Category                              | Permission                                      | Policy Statement                                                                                   |
| ------------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Compute Service                       | list\_instances                                 | Allow group `<group_name>` to read instances in compartment `<compartment_name>`                   |
| Compute Service                       | list\_vnic\_attachments                         | Allow group `<group_name>` to read vnic-attachments in compartment `<compartment_name>`            |
| Compute Service                       | list\_image/get\_image                          | Allow group `<group_name>` to read images in compartment `<compartment_name>`                      |
| Networking Service                    | list\_network\_security\_group\_security\_rules | Allow group `<group_name>` to read network-security-groups in compartment `<compartment_name>`     |
| Networking Firewall                   | list\_network\_firewalls                        | Allow group `<group_name>` to read network-firewalls in tenancy                                    |
| Networking Service                    | list\_public\_ips                               | Allow group `<group_name>` to read virtual-network-family in compartment `<compartment_name>`      |
| Networking Service                    | list\_security\_lists                           | Allow group `<group_name>` to read security-lists in compartment `<compartment_name>`              |
| Networking Service                    | get\_subnet                                     | Allow group `<group_name>` to inspect subnets in compartment `<compartment_name>`                  |
| Networking Service                    | get\_private\_ip                                | Allow group `<group_name>` to read virtual-network-family in compartment `<compartment_name>`      |
| Networking Service                    | get\_vnic                                       | Allow group `<group_name>` to read vnic in compartment `<compartment_name>`                        |
| Networking Service                    | list\_vcns                                      | Allow group `<group_name>` to read vcns in compartment `<compartment_name>`                        |
| Networking Service                    | get\_security\_list                             | Allow group `<group_name>` to read security-lists in compartment `<compartment_name>`              |
| Database Service                      | list\_db\_systems                               | Allow group `<group_name>` to read db-systems in compartment `<compartment_name>`                  |
| Database Service                      | list\_db\_homes                                 | Allow group `<group_name>` to read db-homes in compartment `<compartment_name>`                    |
| Database Service                      | list\_databases                                 | Allow group `<group_name>` to read databases in compartment `<compartment_name>`                   |
| Database Service                      | list\_autonomous\_databases                     | Allow group `<group_name>` to read autonomous-databases in compartment `<compartment_name>`        |
| Database Service                      | list\_pluggable\_databases                      | Allow group `<group_name>` to read pluggable-databases in compartment `<compartment_name>`         |
| Database Service                      | get\_db\_system/list\_db\_systems               | Allow group `<group_name>` to read db-systems in compartment `<compartment_name>`                  |
| NoSQL Database Service                | list\_tables                                    | Allow group `<group_name>` to read tables in compartment `<compartment_name>`                      |
| Container Engine for Kubernetes (OKE) | list\_clusters                                  | Allow group `<group_name>` to read clusters in compartment `<compartment_name>`                    |
| Identity and Access Management (IAM)  | get\_compartment                                | Allow group `<group_name>` to read compartments in tenancy                                         |
| Identity and Access Management (IAM)  | list\_compartments                              | Allow group `<group_name>` to read compartments in tenancy                                         |
| Identity and Access Management (IAM)  | list\_users                                     | Allow group `<group_name>` to read users in tenancy                                                |
| Identity and Access Management (IAM)  | list\_groups                                    | Allow group `<group_name>` to read groups in tenancy                                               |
| Identity and Access Management (IAM)  | list\_api\_keys                                 | Allow group `<group_name>` to read api-keys in compartment `<compartment_name>`                    |
| Identity and Access Management (IAM)  | list\_user\_group\_memberships                  | Allow group `<group_name>` to read group-memberships in compartment `<compartment_name>`           |
| OCI Auto Scaling                      | list\_auto\_scaling\_configurations             | Allow group `<group_name>` to read auto-scaling-configurations in compartment `<compartment_name>` |
| Load Balancers                        | list\_auto\_scaling\_configurations             | Allow group `<group_name>` to read load-balancers in tenancy                                       |
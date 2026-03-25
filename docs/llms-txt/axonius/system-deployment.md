# Source: https://docs.axonius.com/docs/system-deployment.md

# System Deployment - Deploying the Virtual Appliance

The Axonius solution is installed as a virtual appliance in VMware ESXi, Amazon AWS, Microsoft Azure, and GCP.

## Sizing Recommendations

| Count of Unique Assets or Adapters (whichever comes first) | RAM                                               | CPU Cores                                   | Disk                                        | Disk IOPS                                                                      | Additional Requirements                                  | AWS Instance Type                           | Azure Instance Type                         | GCP Instance Type                           |
| ---------------------------------------------------------- | ------------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| Minimum Requirements                                       | 64 GB for core nodes<br />32 GB for compute nodes | 8 virtual cores                             | 500 GB                                      | Any SSD                                                                        | None                                                     | m5.2xlarge                                  | D8 v5                                       | c3-standard-8                               |
| > 25k assets and / or > 5 adapters                         | 64 GB                                             | 16 virtual cores                            | 500 GB                                      | Any SSD                                                                        | None                                                     | m5.4xlarge                                  | D16 v5                                      | c3-standard-22                              |
| >100k but \<500k assets and/or >10 but \<20 adapters       | 128 GB                                            | 16 virtual cores                            | 1000 GB                                     | Minimum 10,000 IOPS Recommended: 10 IOPS per GB, with 10,000 IOPS minimum      | Additional Compute Node required for specific adapters\* | r5.4xlarge                                  | E16 v4/5                                    | c3-standard-44                              |
| > 500k assets and / or > 20 adapters                       | 256 GB                                            | 32 virtual cores                            | 1500 GB                                     | Minimum 15,000 IOPS Recommended: 10 IOPS per GB, with 15,000 IOPS minimum IOPS | Additional Compute Node required for specific adapters\* | r5.8xlarge                                  | E32 v4/5                                    | c3-standard-88                              |
| > 1,000k assets and / or > 20 adapters                     | Multi tiered architecture. Contact Axonius.       | Multi tiered architecture. Contact Axonius. | Multi tiered architecture. Contact Axonius. | Multi tiered architecture. Contact Axonius.                                    | Additional Compute Node required for specific adapters\* | Multi tiered architecture. Contact Axonius. | Multi tiered architecture. Contact Axonius. | Multi tiered architecture. Contact Axonius. |

**Note:** The adapters listed below fetch a large amount of data. If any of the adapters below are configured and fetch more than 100,000 devices, additional computation power is required. Additional memory needs to be added to the primary instance or configured as a separate compute node.

* Amazon Web Services (AWS)
* Infoblox DDI
* Infoblox NetMRI
* Jamf Pro
* Microsoft Endpoint Configuration Manager (MECM) (formerly SCCM)
* Qualys Cloud Platform
* ServiceNow
* Tenable.io
* VMware Workspace ONE (AirWatch)
* Wiz

The table below details the additional memory that needs to be added to the primary instance or configured as a separate compute node.

| Count | Additional RAM / Size of compute node |
| ----- | ------------------------------------- |
| 1-3   | 64 GB                                 |
| 4-6   | 128 GB                                |
| >6    | Contact Axonius Support               |

<Callout icon="📘" theme="info">
  Note:

  It is possible to scale to significantly larger environments using a more advanced multi-node configuration. If you require capacity for an environment larger than our recommendations, feel free to contact Axonius for assistance. Documentation for running additional Axonius nodes can be found [here](/docs/connecting-additional-axonius-nodes).
</Callout>

#### Exposures

For customers with Exposures and up to 1 million Vulnerability Instances, we recommend allocating 50% more computing resources for your Axonius deployment than the Sizing Recommendations listed above. As the number of vulnerabilities fetched increases, the resources required also increase.

If you have over 1 million Vulnerability Instances, work closely with your Axonius representative for proper sizing.

## VMware ESXi Virtual Machine Installed as an OVA

The VM has the following minimum requirements:

* 500 GB Hard Drive (SSD)
* Dynamic or static IP address
* See the [Sizing Recommendations](#sizing-recommendations) above for additional sizing guidelines

### Installation steps:

1. Download the OVA from the location (URL) provided by your Axonius account representative.
2. Install in ESXi via VMware vCenter.

<Callout icon="📘" theme="info">
  Note:

  You do not need to create any disks in order to do this. It is only needed to import the OVA and allow it to require all needed disks and add required storage.
</Callout>

## Amazon AWS

This instance has the following minimum requirements:

* 500 GB Hard Drive

  * EBS (permanent storage) MUST be used.
  * Any additional disks must be in EBS.
  * SSD with 10 IOPS per 1 GB of space is strongly recommended to ensure best performance.
  * Please reach out to Axonius Customer Success for additional questions.

See the [Sizing Recommendations](#sizing-recommendations) above for additional sizing guidelines.

### Installation Steps:

Please provide Axonius with your AWS account number and region, and we will make the AMI available to your account.

<Callout icon="📘" theme="info">
  Note:

  Using two disks is a requirement when creating an Axonius instance from an AMI.
</Callout>

Once the AMI has been made available to your account, deploy it using the following steps:

1. Access the EC2 management console within AWS.
2. Navigate to the Images/AMI section.
3. Select “Private Images” from the dropdown next to the Search bar. You should see the Axonius AMI listed.
4. Select the Axonius AMI and click “Launch.”
5. When prompted for Family, select one of the following:

   * m4
   * m5
   * r5
   * m6i
6. Complete any other required configuration and launch the instance.

<Callout icon="📘" theme="info">
  Note:

  For added security, we recommend [disabling version 1 of AWS' Instance Metadata API](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html)(IMDSv1), as Axonius is fully-compatible with IMDSv2.
</Callout>

## Microsoft Azure

This instance has the following minimum requirements:

* 30GB base root disk as provisioned by default in Azure for the operating system
* An additional 500 GB Hard Drive

  * The default additional disk is NOT permanent. You must select a permanent disk type.
  * "Premium SSD V2" is recommended.
  * Please reach out to Axonius Customer Success for additional questions.

See the [Sizing Recommendations](#sizing-recommendations) above for additional sizing guidelines.

<Callout icon="📘" theme="info">
  Note:

  Information on the required Network/Firewall Ports can be found [here](https://support.axonius.com/hc/en-us/articles/1500004640901).
</Callout>

## Google Cloud Platform (GCP)

This instance has the following minimum requirements:

* Any default disk space required for the operating system.
* An additional 500 GB hard drive (the disk must be SSD).
* Provide Axonius with the email address of a user that can provision new images in their GCP environment. Axonius will share the image with this user and will provide the name of the image shared.
* See the [Sizing Recommendations](#sizing-recommendations) above for additional sizing guidelines.

<Callout icon="📘" theme="info">
  Note:

  Information on the required Network/Firewall Ports can be found [here](https://support.axonius.com/hc/en-us/articles/1500004640901).
</Callout>
# Source: https://docs.curator.interworks.com/get_started/self_hosted_overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Self-hosted

> Quick start guide for installing Curator on various platforms

<Warning>
  Self-hosted Curator CMS no longer our recommended offering.  Check out our [Curator SaaS](/get_started/curator_saas) for a modern, fully managed experience with expert guidance and no infrastructure to maintain.
</Warning>

*If you're an existing customer looking for requirements or there is another reason why you are installing locally, this is what you need to know:*

## Server Requirements

### General Requirements

Your Curator server must be its own standalone web server. Installing on the same web server as Tableau Server is **not** supported.

Containerized deployments are also **not** currently supported.

Your Curator server will need to be able to communicate directly with your Tableau Server, and your Tableau Server will need the REST and Metadata APIs enabled.

### Curator Standard/Enterprise

If you are hosting, you will need a standalone web server on which to install the software.

This can be highly customized, but plan on following minimum specifications:

* Linux (preferred) or Windows
* At least 4 CPU, 8GB of RAM and 20GB of disk space available
* Ports open for web traffic (80 and 443)
* A disaster recovery plan

#### AWS-Hosted Instances

For AWS-hosted instances, we recommend:

| Linux (preferred)                    | Windows                              |
| ------------------------------------ | ------------------------------------ |
| m8g.large                            | m8i.xlarge                           |
| Ubuntu 24.04 LTS or above            | Windows 2019 or above                |
| 20GB of gp3 SSD @ 3000 IOPS/125 MB/s | 20GB of gp3 SSD @ 3000 IOPS/125 MB/s |

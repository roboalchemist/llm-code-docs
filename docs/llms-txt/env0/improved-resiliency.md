# Source: https://docs.envzero.com/changelogs/2023/11/improved-resiliency.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🛠️ BREAKING CHANGE - incoming traffic from env0 extended IP list

> The env0 engineering team is dedicated to enhancing the system for increased stability and resilience. As part of our ongoing efforts, we have expanded our resources across more Availability Zones (AZs) and regions, ensuring rapid recovery in the event of a complete AZ or region failure.

The env0 engineering team is dedicated to enhancing the system for increased stability and resilience. As part of our ongoing efforts, we have expanded our resources across more Availability Zones (AZs) and regions, ensuring rapid recovery in the event of a complete AZ or region failure.

To facilitate a seamless transition for our clients, who had previously whitelisted our static IP addresses, we kindly ask them to include the new IP addresses in their allow-list. You can find a comprehensive list of all the IP addresses in our [documentation](/guides/admin-guide/custom-flows#faq) and at the bottom of this message. Rest assured, the previous IP addresses will continue to be in use.

Commencing Dec. 4, 2023, the new addresses will be active, and clients can anticipate incoming traffic from any address within the provided list.

It's important to note that these changes may impact the [Terraform Provider](https://github.com/env0/terraform-provider-env0) associated with env0. Customers using Terraform to manage their projects may need to validate and update their Terraform configurations to align with the new IP addresses

Full list of addresses:

3.209.36.240\
3.222.51.117\
3.226.24.146\
18.214.49.142\
18.214.210.123\
35.81.146.242\
35.85.88.233\
44.195.170.230\
44.205.134.220\
44.212.144.113\
44.227.16.37\
44.228.227.2\
44.240.181.100\
52.73.227.111\
54.68.137.240\
54.88.50.2\
54.149.16.114\
54.165.19.49

Built with [Mintlify](https://mintlify.com).

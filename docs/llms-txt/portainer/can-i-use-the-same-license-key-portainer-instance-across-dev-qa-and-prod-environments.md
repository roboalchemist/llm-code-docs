# Source: https://docs.portainer.io/2.33-lts/faqs/licensing/can-i-use-the-same-license-key-portainer-instance-across-dev-qa-and-prod-environments.md

# Source: https://docs.portainer.io/sts/faqs/licensing/can-i-use-the-same-license-key-portainer-instance-across-dev-qa-and-prod-environments.md

# Source: https://docs.portainer.io/faqs/licensing/can-i-use-the-same-license-key-portainer-instance-across-dev-qa-and-prod-environments.md

# Can I use the same license key / Portainer instance across Dev, QA and Prod environments?

Yes.  You can use the same license key in separate Dev, QA and Prod environments as long as the [total number of nodes](https://docs.portainer.io/faqs/licensing/what-is-a-node-for-licensing-purposes) does not exceed the number you have purchased.

For example, assume a 25 node license, and assume three separate Kubernetes clusters; one for Dev, one for QA, and one for Prod, each with 5 nodes.  If the Portainer instance is deployed in one of these environments and then the other two environments are added to that Portainer instance, 15 licenses would be used.   Each individual environment, Dev, QA, and Prod, would be manageable from the single Portainer UI.

Alternatively; if you wish to have Portainer manage all three environments from outside of the environments, perhaps so that one environment doesn’t “own” Portainer, you can simply run Portainer outside of all three environments and then add each environment to that Portainer instance.  In this scenario, 16 licenses would be utilized; one for the Portainer instance and one for each node in each cluster being managed.&#x20;

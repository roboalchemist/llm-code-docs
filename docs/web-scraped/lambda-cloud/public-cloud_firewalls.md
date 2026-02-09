# Firewalls -

Source: https://docs.lambda.ai/public-cloud/firewalls/

---

[1-click clusters](../../tags/#tag:1-click-clusters) [on-demand cloud](../../tags/#tag:on-demand-cloud)

# Firewalls

You can restrict incoming traffic to your instances, including [1-Click Cluster](../1-click-clusters/) management (head) nodes, by creating firewall rules on the [Firewall page](https://cloud.lambda.ai/firewall) in the Lambda Cloud console. You can create global rules that apply to all of your instances, or rulesets scoped to individual instances and their regions.

By default, Lambda allows only incoming ICMP traffic or TCP traffic on port 22 (SSH).

Note

You can also use the Lambda Cloud API to manage your global firewall rules and per-instance rulesets programmatically. For details, see [Firewalls](https://docs.lambda.ai/api/cloud#Firewalls) in the Lambda Cloud API browser.

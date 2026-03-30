# Source: https://docs.aws.amazon.com/recovery-cluster/latest/api/llms.txt

# Amazon Route 53 Application Recovery Controller Recovery Control Configuration API Reference Guide

> With recovery control configuration in Amazon Application Recovery Controller (ARC), you can improve application availability by centrally coordinating failovers within an AWS Region or across multiple Regions. Recovery control configuration in ARC provides routing controls, which are extremely reliable failover triggers that enable you to recover applications across Availability Zones and Regions.

- [What is recovery control configuration in Amazon Application Recovery Controller (ARC)?](https://docs.aws.amazon.com/recovery-cluster/latest/api/what-is-recovery-control.html)
- [Document history](https://docs.aws.amazon.com/recovery-cluster/latest/api/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/recovery-cluster/latest/api/glossary.html)

## [Resources](https://docs.aws.amazon.com/recovery-cluster/latest/api/resources.html)

- [CreateControlPanel, UpdateControlPanel](https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanel.html)
- [CreateRoutingControl, UpdateRoutingControl](https://docs.aws.amazon.com/recovery-cluster/latest/api/routingcontrol.html)
- [CreateSafetyRule, UpdateSafetyRule](https://docs.aws.amazon.com/recovery-cluster/latest/api/safetyrule.html)
- [DescribeCluster, DeleteCluster](https://docs.aws.amazon.com/recovery-cluster/latest/api/cluster-clusterarn.html)
- [DescribeControlPanel, DeleteControlPanel](https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanel-controlpanelarn.html)
- [DescribeRoutingControl, DeleteRoutingControl](https://docs.aws.amazon.com/recovery-cluster/latest/api/routingcontrol-routingcontrolarn.html)
- [DescribeSafetyRule, DeleteSafetyRule](https://docs.aws.amazon.com/recovery-cluster/latest/api/safetyrule-safetyrulearn.html)
- [GetResourcePolicy](https://docs.aws.amazon.com/recovery-cluster/latest/api/resourcepolicy-resourcearn.html): Returns the current resource policy for a cluster.
- [ListAssociatedRoute53HealthChecks](https://docs.aws.amazon.com/recovery-cluster/latest/api/routingcontrol-routingcontrolarn-associatedroute53healthchecks.html)
- [ListClusters, CreateCluster, UpdateCluster](https://docs.aws.amazon.com/recovery-cluster/latest/api/cluster.html)
- [ListControlPanels](https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanels.html)
- [ListRoutingControls](https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanel-controlpanelarn-routingcontrols.html)
- [ListSafetyRules](https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanel-controlpanelarn-safetyrules.html)
- [ListTagsForResource, TagResource, UntagResource](https://docs.aws.amazon.com/recovery-cluster/latest/api/tags-resourcearn.html)


## [CLI examples](https://docs.aws.amazon.com/recovery-cluster/latest/api/examples-cli-control.html)

- [Create a cluster](https://docs.aws.amazon.com/recovery-cluster/latest/api/create-cluster.html): The following is an example of a request to create a cluster, and the response.
- [List clusters](https://docs.aws.amazon.com/recovery-cluster/latest/api/list-clusters.html): The following is an example of a request to list the clusters in an account, and the response.
- [Describe a cluster](https://docs.aws.amazon.com/recovery-cluster/latest/api/describe-cluster.html): The following is an example of a request to describe a cluster, and the response.
- [Update a cluster](https://docs.aws.amazon.com/recovery-cluster/latest/api/update-cluster.html): The following is an example of a request to update a cluster, and the response.
- [Delete a cluster](https://docs.aws.amazon.com/recovery-cluster/latest/api/delete-cluster.html): The following is an example of a request to delete a cluster.
- [Create a control panel](https://docs.aws.amazon.com/recovery-cluster/latest/api/create-control-panel.html): A control panel is a logical grouping for organizing your Amazon Route 53 Application Recovery Controller routing controls.
- [List control panels](https://docs.aws.amazon.com/recovery-cluster/latest/api/list-control-panels.html): A control panel is a logical grouping for organizing your Amazon Route 53 Application Recovery Controller routing controls.
- [Describe a control panel](https://docs.aws.amazon.com/recovery-cluster/latest/api/describe-control-panel.html): The following is an example of a request to describe a control panel, and the response.
- [Delete a control panel](https://docs.aws.amazon.com/recovery-cluster/latest/api/delete-control-panel.html): The following is an example of a request to delete a control panel.
- [Create a routing control](https://docs.aws.amazon.com/recovery-cluster/latest/api/create-routing-control.html): When you create a routing control, at a minimum you must specify the Amazon Resource Name (ARN) of the cluster that you want the routing control to be in.
- [List routing controls](https://docs.aws.amazon.com/recovery-cluster/latest/api/list-routing-controls.html): The following is an example of a request to list the routing controls in a control panel, and the response.
- [Describe a routing control](https://docs.aws.amazon.com/recovery-cluster/latest/api/describe-routing-control.html): The following is an example of a request to describe a routing control, and the response.
- [Delete a routing control](https://docs.aws.amazon.com/recovery-cluster/latest/api/delete-routing-control.html): The following is an example of a request to delete a routing control.
- [Create safety rules](https://docs.aws.amazon.com/recovery-cluster/latest/api/create-safety-rule.html): The following are examples of requests to create the two types of safety rules, assertion rules and gating rules, and the responses.
- [List safety rules](https://docs.aws.amazon.com/recovery-cluster/latest/api/list-safety-rules.html): The following is an example of a request to list the safety rules in a control panel, and the response.
- [Describe a safety rule](https://docs.aws.amazon.com/recovery-cluster/latest/api/describe-safety-rule.html): The following is an example of a request to describe a type of safety rule, and the response.
- [Delete a safety rule](https://docs.aws.amazon.com/recovery-cluster/latest/api/delete-safety-rule.html): The following is an example of a request to delete a safety rule.
- [Get routing control state](https://docs.aws.amazon.com/recovery-cluster/latest/api/get-routing-control-state.html): The following is an example of a request to get a routing control state, and the response.
- [Update state for one routing control](https://docs.aws.amazon.com/recovery-cluster/latest/api/update-routing-control-state.html): The following is an example of a request to update a routing control state to be ON.
- [Update state for two routing controls at the same time, in a batch](https://docs.aws.amazon.com/recovery-cluster/latest/api/update-routing-control-state-batch.html): The following is an example of a request to update two routing control states at the same time.

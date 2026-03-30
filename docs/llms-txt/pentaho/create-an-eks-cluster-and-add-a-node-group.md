# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/hyperscalers-landing-page/installing-pentaho-on-aws/installing-the-platform-or-pdi-server-on-aws/create-an-eks-cluster-and-add-a-node-group.md

# Create an EKS cluster and add a node group

Use Amazon Elastic Kubernetes Service (EKS) to create a cluster for running the Platform or PDI Server.

1. Create an EKS cluster on AWS.

   For instructions, see [Create an Amazon EKS cluster](https://docs.aws.amazon.com/eks/latest/userguide/create-cluster.html).

   For a beginner's introduction to EKS, see [Getting started with Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html).

   For information about creating roles to delegate permissions to an AWS service, see [Create a role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html).

| Settings                                              | Actions                                                                                                                                                                                                                                                                                                                                           |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cluster service role                                  | <p>You can select any existing role, as long as the following policies are attached to the role:</p><ul><li>AmazonEKSClusterPolicy</li><li>AmazonS3FullAccess</li><li>AmazonEKSServicePolicy</li></ul>                                                                                                                                            |
| VPC                                                   | <p>In the Networking section, do the following:</p><ol><li>Select an existing VPC. The selected VPC populates a group of subnets. It should be created before you create a computing or cloud stack.</li><li>Make sure that the <strong>Auto-assign public IPv4 address</strong> property under subnets is set to <strong>Yes</strong>.</li></ol> |
| Cluster endpoint access                               | Select the **Public and private** option.                                                                                                                                                                                                                                                                                                         |
| <p>Amazon VPC CNI</p><p>CoreDNS</p><p>kube\_proxy</p> | Select all three EKS add-ons with their default configurations.                                                                                                                                                                                                                                                                                   |

2\. Record the newly created EKS cluster name in the \[Worksheet for AWS hyperscaler]\(../Running%20PDI-CLI%20on%20AWS/Worksheet%20for%20AWS%20hyperscaler%20(common).md).

3. On the **Compute** tab under Node groups, add a node group to the EKS cluster by clicking **Add node group**.

   **Note:** The EKS cluster must be in active state before starting the process of creating a node. For further instructions, see [Create a managed node group](https://docs.aws.amazon.com/eks/latest/userguide/create-managed-node-group.html).
4. In the Node group configuration section, add the group **Name**.
5. Select a Node IAM role from the list or create a new role. Make sure that the role contains the following policies:
   * AmazonS3FullAccess
   * AmazonEC2ContainerRegistryReadOnly
   * AmazonEKSWorkerNodePolicy
   * AmazonEKS\_CNI\_Policy
6. Set the instance type to one that has at least 8 GB of memory.
7. In the Node group scaling configuration section, set the value for **Desired size**, **Minimum size**, and **Maximum size** to the desired number of nodes.
8. In the Node group network configuration section, select the subnets for your node group.
9. For the subnets, set the **Auto-assign public IPv4 address** property to **Yes**.

   For further instructions, contact your AWS administrator or see [IP addressing for your VPCs and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-ip-addressing.html#subnet-public-ip).
10. Select a load balancer.

    For instructions on how to create an AWS Application load balancer, see [Application load balancing on Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/alb-ingress.html).

# Source: https://docs.anyscale.com/admin/cloud/create-eks-cloud.md

# Deploy Anyscale on Amazon EKS

[View Markdown](/admin/cloud/create-eks-cloud.md)

## 1. Install Anyscale's python client package[​](#1-install-anyscales-python-client-package "Direct link to 1. Install Anyscale's python client package")

```
pip install -U anyscale
anyscale login # authenticate
```

## 2. Configure your Cloud Provider account[​](#2-configure-your-cloud-provider-account "Direct link to 2. Configure your Cloud Provider account")

Set up your AWS credentials locally if you haven't done it before (for more details see [the AWS configuration guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html#getting-started-quickstart-new-command)).

```
aws configure
```

note

Before you continue to the next step, make sure your AWS credentials have the following permissions ([learn more](/administration/cloud-deployment/manage-aws-cloud.md)):

* Launch EC2 instances in the AWS region you plan to use
* Manage these resources: VPC, subnets, Security Group, IAM, S3, and EFS

## 3. Terraform your AWS Account to create an EKS cluster[​](#3-terraform-your-aws-account-to-create-an-eks-cluster "Direct link to 3. Terraform your AWS Account to create an EKS cluster")

note

If you wish to use an existing EKS cluster, follow [this example](https://github.com/anyscale/terraform-kubernetes-anyscale-foundation-modules/tree/main/examples/aws/eks-existing) or explore [the Anyscale Operator documentation](/admin/cloud/kubernetes.md) and the [Anyscale Terraform Github](https://github.com/anyscale/terraform-kubernetes-anyscale-foundation-modules) repository.

**Enter information about where you want to deploy your EKS cluster.**

Anyscale Cloud Namemy-eks-cloud

AWS Account ID1234567890

AWS Regionus-west-2

EKS Cluster Namemy-eks-cluster

Run the following commands to create an Anyscale Cloud with a basic EKS cluster.

```
git clone https://github.com/anyscale/terraform-kubernetes-anyscale-foundation-modules
cd terraform-kubernetes-anyscale-foundation-modules/examples/aws/eks-public/
```

Create and populate the Terraform variable file with additional variables (automatically populated).

```
cat <<EOF > terraform.tfvars
eks_cluster_name = "<your_eks_cluster_name>"
aws_region = "<your_aws_region>"
EOF
```

Apply the Terraform and wait for resources to be created. This may take a couple minutes.

```
terraform init
terraform plan
terraform apply
```

*Note: some Terraform errors may be resolved by re-running terraform apply.*

note

The Terraform output provides an example Cloud registration command. Take note of the following outputs:

* The Availability Zones for the EKS cluster
* The IAM role name
* The name of the S3 bucket
* The EFS ID

**Provide information from the Terraform output:**

Availability Zonesus-west-2a,us-west-2b

Operator IAM role namedefault-eks-node-group

Storage Bucket Nameanyscale-1234

EFS IDfs-1234

## 4. Install additional EKS components[​](#4-install-additional-eks-components "Direct link to 4. Install additional EKS components")

Connect your terminal to the EKS cluster, replacing the cluster name if it has been modified.

```
aws eks update-kubeconfig --region <your_aws_region> --name <your_eks_cluster_name>
```

Run the following commands to install the default ingress for externally facing autoscaling, load balancing, and related drivers. For more information about customizing EKS, refer to the [Anyscale Terraform Github](https://github.com/anyscale/terraform-kubernetes-anyscale-foundation-modules) repository.

Install the Kubernetes Autoscaler helm chart.

```
helm repo add autoscaler https://kubernetes.github.io/autoscaler
```

```
helm upgrade cluster-autoscaler autoscaler/cluster-autoscaler \
  --version 9.46.0 \
  --namespace kube-system \
  --set awsRegion=<your_aws_region> \
  --set 'autoDiscovery.clusterName'=<your_eks_cluster_name> \
  --install
```

Install the AWS LBC (load balancer controller).

```
helm repo add eks https://aws.github.io/eks-charts
```

```
helm upgrade aws-load-balancer-controller eks/aws-load-balancer-controller \
  --version 1.11.0 \
  --namespace kube-system \
  --set clusterName=<your_eks_cluster_name> \
  --install
```

Install the nginx ingress controller.

```
helm repo add nginx https://kubernetes.github.io/ingress-nginx
```

```
helm upgrade ingress-nginx nginx/ingress-nginx \
  --version 4.12.1 \
  --namespace ingress-nginx \
  --values sample-values_nginx.yaml \
  --create-namespace \
  --install
```

(Optional) Install the Nvidia device plugin.

```
helm repo add nvdp https://nvidia.github.io/k8s-device-plugin
```

```
helm upgrade nvdp nvdp/nvidia-device-plugin \
  --namespace nvidia-device-plugin \
  --version 0.17.0 \
  --values sample-values_nvdp.yaml \
  --create-namespace \
  --install
```

## 5. Install the Anyscale Operator Helm chart[​](#5-install-the-anyscale-operator-helm-chart "Direct link to 5. Install the Anyscale Operator Helm chart")

Run the following command to install and update the Helm chart for the Anyscale Operator.

```
helm repo add anyscale https://anyscale.github.io/helm-charts
helm repo update anyscale
```

If you wish to customize the Helm chart to add custom Patches or additional pod shapes follow [these instructions](/k8s/configure-helm.md) in the documentation.

## 6. Register the Anyscale Cloud resources[​](#6-register-the-anyscale-cloud-resources "Direct link to 6. Register the Anyscale Cloud resources")

Run the command produced by the Terraform script. The command should look similar to the commands below. Verify all variables are entered correctly.

```
anyscale cloud register --name <your_cloud_name> \
  --provider aws \
  --region <your_aws_region> \
  --compute-stack k8s \
  --kubernetes-zones us-west-2a,us-west-2b \
  --anyscale-operator-iam-identity=arn:aws:iam::<your_aws_account_id>:role/<your_anyscale_operator_iam_role> \
  --s3-bucket-id s3://<your_storage_bucket_name> \
  --efs-id <your_efs_id>
```

note

Take note of the Cloud Deployment ID in the output.

**Record the Cloud Resource ID:**

Cloud Resource IDcldrsrc\_1234

## 7. Deploy the Anyscale Operator on your EKS cluster[​](#7-deploy-the-anyscale-operator-on-your-eks-cluster "Direct link to 7. Deploy the Anyscale Operator on your EKS cluster")

Run the following commands to deploy the Anyscale Operator with your Cloud Deployment ID. Verify all variables are entered correctly. The release name and namespace are up to you to define.

```
helm upgrade <your_cloud_name>-v0 anyscale/anyscale-operator \
  --set-string global.cloudDeploymentId=<your_cloud_deployment_id> \
  --set-string global.cloudProvider=aws \
  --set-string global.aws.region=<your_aws_region> \
  --set-string workloads.serviceAccount.name=anyscale-operator \
  --namespace <your_cloud_name> \
  --create-namespace \
  -i
```

It may take several minutes for your Anyscale Cloud to be ready to use. You can watch the deployment status using the following command.

```
kubectl get deployments anyscale-operator -n <your_cloud_name> -w
```

## 8. Verify your Anyscale Cloud[​](#8-verify-your-anyscale-cloud "Direct link to 8. Verify your Anyscale Cloud")

It may take several minutes for your Anyscale Cloud to be ready to use. Run the following command to verify that your newly created Anyscale Cloud is fully functional and ready to use.

```
anyscale job submit --cloud <your_cloud_name> --working-dir https://github.com/anyscale/docs_examples/archive/refs/heads/main.zip -- python hello_world.py
```

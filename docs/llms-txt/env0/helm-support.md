# Source: https://docs.envzero.com/changelogs/2023/06/helm-support.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🚢 Helm Support

> Helm is a popular package manager for Kubernetes, an open-source container orchestration platform. It simplifies the deployment and management of applications in Kubernetes clusters by providing a templating system and a standardized way to package, distribute, and deploy software. We are excited to announce that Helm is now a first-class citizen in env0 alongside all of the other Infrastructure as code frameworks we support like Terraform, Terragrunt, Pulumi and Kubernetes.

[Helm](https://helm.sh/) is a popular package manager for Kubernetes, an open-source container orchestration platform. It simplifies the deployment and management of applications in Kubernetes clusters by providing a templating system and a standardized way to package, distribute, and deploy software.

We are excited to announce that Helm is now a first-class citizen in env0 alongside all of the other Infrastructure as code frameworks we support like Terraform, Terragrunt, Pulumi and Kubernetes.

## ✨ Helm - How does it work ✨

You can use Helm with all its advantages while enjoying all of the benefits env zero has to offer out of the box such as Approval flow, Plan on Pull Request, Drift Detection, TTL, Scheduling, and more!

In order to manage your Helm deployments using env zero, you will need to create a new Helm template, or run an environment directly from a VCS and choose the type Helm:

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/U9rcMIDzc38oPcXx/images/changelogs/2023/06/9ac9703-image.png?fit=max&auto=format&n=U9rcMIDzc38oPcXx&q=85&s=8614530fafab8421db9f547e6c37fc5a" alt="Helm template creation interface showing Helm as a deployment type option" width="1415" height="433" data-path="images/changelogs/2023/06/9ac9703-image.png" />
</Frame>

Other than that all the rest of the features are available for Helm as well.\
You can learn more about Helm templates [here](/guides/admin-guide/templates/helm).

Built with [Mintlify](https://mintlify.com).

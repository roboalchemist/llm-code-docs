# Source: https://docs.envzero.com/changelogs/2023/08/better-kubernetes-support.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🎱🔐 Native Kubernetes Authentication

> As env0 supports various Infrastructures as code frameworks, each one has its own way of handling authentication in different ways. For Kubernetes, the authentication is not very straightforward, and now we are simplifying the process by adding native support to set up Kubernetes configuration via `kubeconfig`, `AWS EKS`, `Azure AKS` and `GCP GKE` credentials!

As env0 supports various Infrastructures as code frameworks, each one has its own way of handling authentication in different ways. For Kubernetes, the authentication is not very straightforward, and now we are simplifying the process by adding native support to set up Kubernetes configuration via `kubeconfig`, `AWS EKS`, `Azure AKS` and `GCP GKE` credentials!

This also means that you can control the authentication to a specific cluster based on the project settings.

## Set Up Kubernetes Credentials

Navigate into `Organization Settings > Credentials`\
Under `Deployment Credentials`, click the `+ Add Credential` button

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/U9rcMIDzc38oPcXx/images/changelogs/2023/08/c8ec425-image.png?fit=max&auto=format&n=U9rcMIDzc38oPcXx&q=85&s=2b399d63d402c6d218738e639f7a77c0" alt="Feature demonstration screenshot showing new functionality" width="1884" height="824" data-path="images/changelogs/2023/08/c8ec425-image.png" />
</Frame>

Inside the opened modal, select the desired Kubernetes Cluster authentication method you like.

Select the `Kubernetes - <Cluster Type / kubeconfig>` credential from the `Type` dropdown:

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/U9rcMIDzc38oPcXx/images/changelogs/2023/08/d0965d0-image.png?fit=max&auto=format&n=U9rcMIDzc38oPcXx&q=85&s=4639b010bae3270d46cda98c70a56094" alt="Feature demonstration screenshot showing new functionality" width="515" height="524" data-path="images/changelogs/2023/08/d0965d0-image.png" />
</Frame>

Next, You'll need to associate the created credential with your project.

In your `Project Settings`, click `Credentials`. Then, check the `Kubernetes` checkbox and select your created credential from the dropdown

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/U9rcMIDzc38oPcXx/images/changelogs/2023/08/05779aa-image.png?fit=max&auto=format&n=U9rcMIDzc38oPcXx&q=85&s=827fad77a8de9d0f1f239794ada27e2a" alt="Feature demonstration screenshot showing new functionality" width="1637" height="548" data-path="images/changelogs/2023/08/05779aa-image.png" />
</Frame>

Lean more by reading our [docs](/guides/getting-started/getting-started/connect-your-cloud-account#kubernetes)

Built with [Mintlify](https://mintlify.com).

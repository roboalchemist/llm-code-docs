# Source: https://help.cloudsmith.io/docs/argocd.md

# ArgoCD

How to integrate ArgoCD with Cloudsmith

<Image align="center" src="https://files.readme.io/8524c25d9eb6c9262744d38181ea4912acbb89b857b55722b476c0cdfc4cf43d-Integration_3.png" />

You can integrate Cloudsmith with Argo CD to automate the deployment of your Kubernetes applications using Helm charts and Docker images securely stored in Cloudsmith repositories. This guide covers the steps to set up both Helm charts and Docker images with Cloudsmith in Argo CD, including secure authentication for private repositories.

It currently supports pulling:

* [Docker](https://help.cloudsmith.io/docs/docker-registry)
* [Helm](https://help.cloudsmith.io/docs/helm-chart-repository)

<HTMLBlock>
  {`
  <div class="row cs-box-row">
    <div class="cs-box cs-box-66 cs-box-green">
      <div class="cs-box-title cs-box-title-green">No Code Uploading</div>
      <p>The Cloudsmith CLI gives you full control when connecting to any CI/CD process; allowing you to upload any of our support formats or query your repositories. Just configure your API Key, install the CLI, and you'll be all set.</p>
    </div>
  </div>
  `}
</HTMLBlock>

## With this integration, you can

* Use Cloudsmith to securely store and manage Helm charts and container images.
* Automate deployments of applications to Kubernetes clusters using ArgoCD.
* Maintain version control of your deployment artifacts.

## What you’ll need

* A Cloudsmith account with a repository to store your Helm charts or container images.
* An ArgoCD installation configured to deploy applications to your Kubernetes cluster.
* API keys or OIDC tokens for secure authentication with private Cloudsmith repositories.

***

## Getting Started

### Step 1: Tag and Push the Docker Image to Cloudsmith

```Text bash
docker tag your-existing-image:latest docker.cloudsmith.io/your-namespace/your-repo/image-name:latest
docker push docker.cloudsmith.io/your-namespace/your-repo/image-name:latest
```

> 📘
>
> Replace your-existing-image:latest with the name of your Docker image, and ensure that the target repository details (your-namespace/your-repo) match your Cloudsmith setup.

This command uploads your Docker image to the specified Cloudsmith repository, where it will be available for deployment.

### Step 2: Handling Image Pull Secrets

If your Docker image is stored in a private Cloudsmith repository, you’ll need to create an image pull secret for Kubernetes to pull the image.

**Create the Docker Registry Secret for Image Pull**

```Text bash
kubectl create secret docker-registry cloudsmith-regcred \
  --docker-server=docker.cloudsmith.io \
  --docker-username=your-username \
  --docker-password=your-api-key \
  --docker-email=your-email@example.com \
  -n default
```

This secret allows your Kubernetes cluster to authenticate with Cloudsmith to pull the Docker image securely.

**Reference the Image Pull Secret in Deployment**

Ensure that the Helm chart or deployment configuration references the image pull secret:

```yaml yaml
spec:
  template:
    spec:
      imagePullSecrets:
        - name: cloudsmith-regcred
```

### Step 3: Publish Helm Chart to Cloudsmith

If you have a Helm chart that defines your application’s deployment, you can push it to Cloudsmith as follows:

```scss bash
helm package ./my-test-app
cloudsmith push helm your-namespace/your-repo ./my-test-app-0.1.0.tgz
```

### Step 4: Add Cloudsmith Helm Repository to Argo CD

Argo CD requires that you add the Helm repository from Cloudsmith to access the chart during deployments. You can do this using the Argo CD CLI or the Web UI.

**Adding the Helm Repository via ArgoCD CLI**

```Text bash
argocd repo add --name cloudsmith-helm --type helm https://dl.cloudsmith.io/basic/OWNER/REPOSITORY/helm/charts/ \
  --username your-username \
  --password your-api-key
```

* dl.cloudsmith.io/basic/OWNER/REPOSITORY/helm/charts/: Replace with the correct URL of your Cloudsmith Helm repository.
* \--username and --password: Please use your Cloudsmith username with the API key for authentication, as using username and password is deprecated.

> 📘
>
> Where possible, use Entitlement tokens instead of API keys for more secure and flexible authentication when integrating with ArgoCD. Entitlement tokens are easier to manage and can be rotated more frequently for enhanced security.

In case of Entitlement token the command for adding the helm repo via ArgoCD CLI will be:

```Text bash
argocd repo add --name cloudsmith-helm --type helm \
  https://dl.cloudsmith.io/TOKEN/OWNER/REPOSITORY/helm/charts/
```

### Step 5: Create an Argo CD Application Manifest

Configure your Argo CD application to deploy the Helm chart from Cloudsmith to your Kubernetes cluster using the following manifest:

```yaml argocd-application.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-cloudsmith-app
  namespace: argocd
spec:
  project: default
  source:
    repoURL: "https://dl.cloudsmith.io/TOKEN/OWNER/REPOSITORY/helm/charts/"
    targetRevision: "0.1.0"
    chart: my-test-app
  destination:
    server: https://kubernetes.default.svc
    namespace: default
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

**Explanation**

* **repoURL**: Points to the Helm chart repository hosted on Cloudsmith.
* **targetRevision**: Specifies the version of the Helm chart you want to deploy.
* **chart**: The name of the chart in the Cloudsmith repository.

### Step 6: Deploy the Application with Argo CD

1. Apply the Application manifest to ArgoCD:
   ```Text bash
   kubectl apply -f argocd-application.yaml
   ```
2. Sync the application to start the deployment process:
   ```shell bash
   argocd app sync my-cloudsmith-app
   ```
3. Sync the application to start the deployment process:
   ```shell bash
   argocd app get my-cloudsmith-app
   ```

***

## Best Practices

* **Use Entitlement token Authentication**: As ArgoCD only pulls images, use Entitlement tokens for authentication to avoid using long-lived API keys.
* **Secure Secrets**: Store sensitive information like API keys/Entitlement tokens in Kubernetes secrets instead of hardcoding them in your deployment manifests.
* **Enable Auto-Sync**: Configure Argo CD’s auto-sync feature to ensure that your Kubernetes clusters always have the latest artifacts.

## Troubleshooting

* **Image Pull Issues**: Verify that the image pull secret is correctly configured in the namespace where your application is running.
* **Helm Chart Errors**: Ensure that the Helm chart version specified in the Argo CD manifest exists in the Cloudsmith repository.
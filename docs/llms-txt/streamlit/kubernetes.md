# Source: https://docs.streamlit.io/deploy/tutorials/kubernetes

# Deploy Streamlit using Kubernetes

So you have an amazing app and you want to start sharing it with other people, what do you do? You have a few options. First, where do you want to run your Streamlit app, and how do you want to access it?

- **On your corporate network**: Most corporate networks are closed to the outside world. You typically use a VPN to log onto your corporate network and access resources there. You could run your Streamlit app on a server in your corporate network for security reasons, to ensure that only folks internal to your company can access it.
- **On the cloud**: If you'd like to access your Streamlit app from outside of a corporate network, or share your app with folks outside of your home network or laptop, you might choose this option. In this case, it'll depend on your hosting provider. We have [community-submitted guides](https://docs.streamlit.io/knowledge-base/deploy/deploy-streamlit-heroku-aws-google-cloud) from Heroku, AWS, and other providers.

Wherever you decide to deploy your app, you will first need to containerize it. This guide walks you through using Kubernetes to deploy your app. If you prefer Docker, see [Deploy Streamlit using Docker](https://docs.streamlit.io/deploy/tutorials/docker).

## Prerequisites

1. **Install Docker Engine**
2. **Install the gcloud CLI**

## Install Docker Engine

If you haven't already done so, install [Docker](https://docs.docker.com/engine/install/#server) on your server. Docker provides [deb](https://docs.docker.com/engine/install/debian/) and [rpm](https://docs.docker.com/engine/install/ubuntu/) packages from many Linux distributions, including:

- [Debian](https://docs.docker.com/engine/install/debian/)
- [Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

Verify that Docker Engine is installed correctly by running the `hello-world` Docker image:

```bash
sudo docker run hello-world
```

Follow Docker's official [post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/) to run Docker as a non-root user, so that you don't have to preface the `docker` command with `sudo`.

## Install the gcloud CLI

In this guide, we will orchestrate Docker containers with Kubernetes and host Docker images on the Google Container Registry (GCR). As GCR is a Google-supported Docker registry, we need to register [gcloud](https://cloud.google.com/sdk/gcloud/reference) as the Docker credential helper.

Follow the official documentation to [Install the gcloud CLI](https://cloud.google.com/sdk/docs/install) and initialize it.

## Create a Docker Image

Put the above files (`run.sh` and `Dockerfile`) in the same folder and build the Docker image:

```bash
docker build --platform linux/amd64 -t gcr.io/<GCP_PROJECT_ID>/k8s-streamlit:test .
```

Replace `<GCP_PROJECT_ID>` in the above command with the name of your Google Cloud project.

## Upload the Docker Image to a Container Registry

The next step is to upload the Docker image to a container registry. In this example, we will use the [Google Container Registry (GCR)](https://cloud.google.com/container-registry). Start by enabling the Container Registry API. Sign in to Google Cloud and navigate to your project’s [Container Registry](https://cloud.google.com/container-registry) and click [Enable](https://cloud.google.com/container-registry/docs/enable).

We can now build the Docker image from the previous step and push it to our project’s GCR. Be sure to replace `<GCP_PROJECT_ID>` in the `docker push` command with the name of your project:

```bash
gcloud auth configure-docker
docker push gcr.io/<GCP_PROJECT_ID>/k8s-streamlit:test
```

## Create a Kubernetes Deployment

For this step, you will need a:

- Running Kubernetes service
- Custom domain for which you can generate a TLS certificate
- DNS service where you can configure your custom domain to point to the application IP

As the image was uploaded to the container registry in the previous step, we can run it in Kubernetes using the below configurations:

### Install and Run Kubernetes

Make sure your [Kubernetes client](https://kubernetes.io/docs/tasks/tools/#kubectl), `kubectl`, is installed and running on your machine.

### Configure a Google OAuth Client and OAuth2-Proxy

For configuring the Google OAuth Client, please see [Google Auth Provider](https://oauth2-proxy.github.io/oauth2-proxy/docs/configuration/oauth_provider#google-auth-provider). Configure OAuth2-Proxy to use the desired [OAuth Provider Configuration](https://oauth2-proxy.github.io/oauth2-proxy/docs/configuration/oauth_provider) and update the OAuth2-Proxy config in the config map.

The below configuration contains an OAuth2-Proxy sidecar container which handles the authentication with Google. You can learn more from the [OAuth2-Proxy repository](https://github.com/oauth2-proxy/oauth2-proxy).

### Create a Kubernetes Configuration File

Create a [YAML](https://yaml.org/) `k8s-streamlit.yaml` configuration file named `k8s-streamlit.yaml`:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: streamlit-configmap
data:
  oauth2-proxy.cfg: |
    http_address = "0.0.0.0:4180"
    upstreams = ["http://127.0.0.1:8501/"]
    email_domains = ["*"]
    client_id = "<GOOGLE_CLIENT_ID>"
    client_secret = "<GOOGLE_CLIENT_SECRET>"
    cookie_secret = "<16, 24, or 32 bytes>"
    redirect_url = <REDIRECT_URL>

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: streamlit-deployment
  labels:
    app: streamlit
spec:
  replicas: 1
  selector:
    matchLabels:
      app: streamlit
  template:
    metadata:
      labels:
        app: streamlit
    spec:
      containers:
        - name: oauth2-proxy
          image: quay.io/oauth2-proxy/oauth2-proxy:v7.2.0
          args: ["--config", "/etc/oauth2-proxy/oauth2-proxy.cfg"]
          ports:
            - containerPort: 4180
          livenessProbe:
            httpGet:
              path: /ping
              port: 4180
              scheme: HTTP
          readinessProbe:
            httpGet:
              path: /ping
              port: 4180
              scheme: HTTP
          resources:
            limits:
              cpu: 1
              memory: 2Gi
            requests:
              cpu: 100m
              memory: 745Mi
      volumes:
        - name: oauth2-config
          configMap:
            name: streamlit-configmap
```

### Set Up TLS Support

Since you are using the Google authentication, you will need to set up TLS support. Find out how in [TLS Configuration](https://oauth2-proxy.github.io/oauth2-proxy/docs/configuration/tls).

### Verify the Deployment

Once the deployment and the service are created, we need to wait a couple of minutes for the public IP address to become available. We can check when that is ready by running:

```bash
kubectl get service streamlit-service -o jsonpath='{.status.loadBalancer.ingress[0].ip}'
```

After the public IP is assigned, you will need to configure in your DNS service an `A record` pointing to the above IP address.
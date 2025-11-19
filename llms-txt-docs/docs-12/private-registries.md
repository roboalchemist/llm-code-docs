# Source: https://docs.baseten.co/development/model/private-registries.md

# Private Docker Registries

> A guide to configuring a private container registry for your truss

Truss uses containerized environments to ensure consistent model execution across deployments. When deploying a custom base image or a custom server from a private registry, you must grant Baseten access to download that image.

## AWS Elastic Cloud Registry (ECR)

AWS supports using either [service accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html), or [access tokens](https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry_auth.html#registry-auth-token) for short lived access for container registry authentication.

### AWS IAM Service accounts

To use an IAM service account for long-lived access, you can use the `AWS_IAM` authentication method in Truss.

1. Get an AWS\_ACCESS\_KEY\_ID and AWS\_SECRET\_ACCESS\_KEY from the AWS dashboard

2. Add these as [secrets](https://app.baseten.co/settings/secrets) in Baseten. These should be named `aws_access_key_id` and `aws_secret_access_key`
   respectively.

3. Choose the `AWS_IAM` authentication method when setting up your Truss. The `config.yaml` file should look something like this:

```
...
  base_image:
    image: <aws account id>.dkr.ecr.<region>.amazonaws.com/path/to/image
    docker_auth:
      auth_method: AWS_IAM
      registry: <aws account id>.dkr.ecr.<region>.amazonaws.com
  secrets:
    aws_access_key_id: null
    aws_secret_access_key: null
...
```

Note here that you need to specify the registry and image separately.

If you'd like to use different secret names besides the default, you can configure these using the
`aws_access_key_id_secret_name` and `aws_secret_access_key_secret_name` options
under `docker_auth`:

```
...
base_image:
  ...
  docker_auth:
    auth_method: AWS_IAM
    registry: <aws account id>.dkr.ecr.<region>.amazonaws.com
    aws_access_key_id_secret_name: custom_aws_access_key_secret
    aws_secret_access_key_secret_name: custom_aws_secret_key_secret
secrets:
  custom_aws_access_key_secret: null
  custom_aws_secret_key_secret: null

```

### Access Token

1. Get the a **Base64-encoded** secret:

```sh  theme={"system"}
PASSWORD=`aws ecr get-login-password --region {us-east-1}`
echo -n "AWS:$PASSWORD" | base64
```

2. Add a new [secret](https://app.baseten.co/settings/secrets) to Baseten named `DOCKER_REGISTRY_{aws account id}.dkr.ecr.{us-east-1}.amazonaws.com` with the `Base64-encoded secret` as the value.

3. Add the secret name to the `secrets` section of the `config.yaml` to allow this model to access the secret when it is pushed.

```yaml config.yaml theme={"system"}
secrets:
  DOCKER_REGISTRY_{aws account id}.dkr.ecr.{us-east-1}.amazonaws.com: null
```

## Google Cloud Artifact Registry

GCP supports using either [access tokens](https://cloud.google.com/artifact-registry/docs/docker/authentication#token) for short lived access or [service accounts](https://cloud.google.com/iam/docs/service-account-overview) for container registry authentication.

### Service Account

1. Get your [service account key](https://cloud.google.com/artifact-registry/docs/docker/authentication#json-key) as a JSON key blob.

2. Add a new [secret](https://app.baseten.co/settings/secrets) to Baseten named `gcp-service-account` (or similar) with the JSON key blob as the value.

3. Add the secret name that you used to the `secrets` section of the `config.yaml` to allow this model to access the secret when it is pushed.

```yaml config.yaml theme={"system"}
secrets:
  gcp-service-account: null
```

4. Configure the `docker_auth` section of your `base_image:` to ensure that the service account authentication method will be used.

```
base_image:
  ...
  docker_auth:
    auth_method: GCP_SERVICE_ACCOUNT_JSON
    secret_name: gcp-service-account
    registry: {us-west2}-docker.pkg.dev
```

Note that here, `secret_name` should match the name of the secret that is contains the JSON key blob.

### Access Token

1. Get your [access token](https://cloud.google.com/artifact-registry/docs/docker/authentication#token)

2. Add a new [secret](https://app.baseten.co/settings/secrets) to Baseten named `DOCKER_REGISTRY_{us-west2}-docker.pkg.dev` with the `Base64-encoded secret` as the value.

3. Add the secret name to the `secrets` section of the `config.yaml` to allow this model to access the secret when it is pushed.

```yaml config.yaml theme={"system"}
secrets:
  DOCKER_REGISTRY_{us-west2}-docker.pkg.dev: null
```

## Docker Hub

1. Get the a **Base64-encoded** secret:

```sh  theme={"system"}
echo -n 'username:password' | base64
```

2. Add a new [secret](https://app.baseten.co/settings/secrets) to Baseten named `DOCKER_REGISTRY_https://index.docker.io/v1/` with the `Base64-encoded secret` as the value.

3. Add the secret name to the `secrets` section of the `config.yaml` to allow this model to access the secret when it is pushed.

```
Name: DOCKER_REGISTRY_https://index.docker.io/v1/
Token: <Base64-encoded secret>
```

Then, this to `config.yaml`:

```yaml config.yaml theme={"system"}
secrets:
  DOCKER_REGISTRY_https://index.docker.io/v1/: null
```

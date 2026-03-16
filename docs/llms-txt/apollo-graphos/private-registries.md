# Source: https://www.apollographql.com/docs/apollo-operator/configuration/private-registries.md

# Private Registry Configuration

The Apollo GraphOS Operator supports authentication with private container registries to fetch GraphQL schemas stored as OCI artifacts.

## Configuration Methods

### 1. Docker Helper

The operator comes bundled with credential helpers for Amazon ECR and Google Artifact Registry.

```yaml title=values.yaml
# For Amazon ECR with static credentials
container:
  envFrom:
    - secretRef:
        name: aws-credentials
dockerConfig:
  credHelpers:
    '<account-id>.dkr.ecr.<region>.amazonaws.com': ecr-login
```

```yaml title=values.yaml
# For Google Artifact Registry
podTemplate:
  volumes:
    - name: gcp-credentials
      secret:
        secretName: gcp-credentials
container:
  volumeMounts:
    - name: gcp-credentials
      mountPath: /.config/gcloud
      readOnly: true
dockerConfig:
  credHelpers:
    '<region>-docker.pkg.dev': gcr
```

#### Amazon ECR with IAM Roles for Service Accounts (IRSA)

IRSA allows you to authenticate with AWS services using IAM roles instead of static credentials. When configured, the ECR credential helper automatically uses the IAM role associated with your Kubernetes service account to obtain temporary credentials for pulling images from ECR.

The `dockerConfig` section maps your ECR registry URLs to the `ecr-login` credential helper. It does not contain any credentials - the credential helper retrieves them automatically using your IRSA configuration.

```yaml title=values.yaml
# For Amazon ECR with IRSA
operator-chart:
  serviceAccount:
    annotations:
      eks.amazonaws.com/role-arn: arn:aws:iam::<account-id>:role/<role-name>
  container:
    env:
      - name: AWS_STS_REGIONAL_ENDPOINTS
        value: regional
      - name: AWS_DEFAULT_REGION
        value: <region>
      - name: AWS_REGION
        value: <region>
      - name: AWS_ROLE_ARN
        value: arn:aws:iam::<account-id>:role/<role-name>
      - name: AWS_WEB_IDENTITY_TOKEN_FILE
        value: /var/run/secrets/eks.amazonaws.com/serviceaccount/token
      - name: DOCKER_CONFIG
        value: /.docker
    volumeMounts:
      - name: aws-iam-token
        mountPath: /var/run/secrets/eks.amazonaws.com/serviceaccount
        readOnly: true
  podTemplate:
    volumes:
      - name: aws-iam-token
        projected:
          defaultMode: 420
          sources:
            - serviceAccountToken:
                audience: sts.amazonaws.com
                expirationSeconds: 86400
                path: token
  dockerConfig:
    credHelpers:
      '<account-id>.dkr.ecr.<region>.amazonaws.com': ecr-login
```

### 2. Mount Docker Config Secret

For sensitive credentials or other registries, mount a Kubernetes secret at `/.docker`:

```yaml
# Create the secret
apiVersion: v1
kind: Secret
metadata:
  name: docker-config
type: kubernetes.io/dockerconfigjson
data:
  config.json: <base64-encoded-docker-config>
```

```yaml title=values.yaml
podTemplate:
  volumes:
    - name: docker-config
      secret:
        secretName: docker-config
container:
  volumeMounts:
    - name: docker-config
      mountPath: /.docker
      readOnly: true
```

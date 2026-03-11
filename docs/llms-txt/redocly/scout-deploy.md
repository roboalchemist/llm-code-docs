# Source: https://redocly.com/docs/realm/scout/guides/scout-deploy.md

# Redocly Scout

Redocly Scout is a discovery and publishing tool for APIs and documentation.
It is designed to be deployed in a customer's infrastructure and to be used with Reunite.

## Before you begin

Make sure the following before you begin:

- [create or use the existing Redocly organization and project IDs](https://github.com/Redocly/redocly-scout#redocly-portal)
- [register Scout as a GitHub App to the GitHub organization account](https://github.com/Redocly/redocly-scout#github-application)
- [build the Docker image](https://github.com/Redocly/redocly-scout#build-docker-image)


## Deploy with AWS Console

### Create ECR repository

1. Open [AWS ECR Repositories](https://us-east-1.console.aws.amazon.com/ecr/repositories?region=us-east-1).
2. Click "Create repository". ![create-a-new-repository.png](/assets/create-a-new-repository.9b88082ce985794752c4e614ef8d3d82bce84c84a2a59a5a98ae6f5a38bfc234.07c68af1.png)
3. Fill "Repository name" field. ![fill-repository-name.png](/assets/fill-repository-name.9b63d04ce28dd9ed3a8893de2622522ff3a600fd9e0cabac3bf77de6cdc9272b.07c68af1.png)
4. Click "Create repository".


### Build docker image and push to ECR repository

1. Open created repository.
2. Click "View push command". ![view-push-commands.png](/assets/view-push-commands.8d8e1576599d97e3b88fa316bde4e96fa9c8bbd2fb3d2271fb1678b087c42f09.07c68af1.png)
3. Execute provided commands. ![push-commands.png](/assets/push-commands.b74fb34aef0aa56500d12bd6e4b318b849c32136b5764924080c5eefd490012a.07c68af1.png)
> NOTE: Skip second step since you already built the Docker image.


### Create secrets

Sensitive data such as the GitHub private key, Redocly API key, and GitHub webhook secret should be stored in the AWS secret
manager.

1. Open [AWS Secrets Manager](https://us-east-1.console.aws.amazon.com/secretsmanager/listsecrets?region=us-east-1).
2. Click "Store a new secret". ![create-a-new-secret.png](/assets/create-a-new-secret.eecc969fc66cf4684c4a62b553037c5c9fa7614c321e900333bdc8dfe56bcc7b.07c68af1.png)
3. Choose secret type: "Other type of secret" -> "Plaintext" and specify its value and click "
Next". ![fill-secret-value.png](/assets/fill-secret-value.b7fd43009d7c3d4a3ac743ddcdcbb19ea58bb173f7018a4dec53e33cc362b6c9.07c68af1.png)
4. Fill "Secret name" field and click "Next". ![fill-secret-name.png](/assets/fill-secret-name.c2c29122999e2caa308495343623a5b97756477088a2300dd1e8f0037cc3e235.07c68af1.png)
5. Click "Store".


### Create task execution role

1. Open [AWS IAM Roles](https://us-east-1.console.aws.amazon.com/iamv2/home?#/roles)
2. Click "Create role"
3. Select "Custom trust policy"
4. Insert the following configuration in the "Custom trust policy" field.



```json
{
  "Version": "2008-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "ecs-tasks.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

1. Click "Next"
2. Select `AmazonECSTaskExecutionRolePolicy` permission policy and click "Next"
3. Fill "Role name" and "Description" and click "Create role"


### Assign read secrets permission to the role

1. Open created on the previous step role
2. Click "Permissions policies" -> "Add permission" -> "Create inline policy"
3. Select "Secrets Manager" service -> Access level "Read" -> "GetSecretValue"
4. In the "Resources" section specify ARNs of created secrets.
5. Click "Next"
6. Fill "Policy name" and click "Create policy".


### Create task definition

1. Open [AWS ECS Task definitions](https://us-east-1.console.aws.amazon.com/ecs/v2/task-definitions?region=us-east-1).
2. Click "Create new task definition". ![create-a-new-task-definition.png](/assets/create-a-new-task-definition.5b9683934d560d751c8e0291ff50c8f75f37a14fe5943775dd707ccc1cea9b59.07c68af1.png)
3. Fill "Task definition family" field and container image
URI. ![fill-task-definition-family.png](/assets/fill-task-definition-family.fed7078130b2dd261d4fce57871bdb7a9d505161aa480eeda483584b1c63dd98.07c68af1.png)
4. Add container port mappings and environment variables. ![fill-task-definition-port-mapping.png](/assets/fill-task-definition-port-mapping.476f9560f735bf85a39e90c08514baf51edd8b924b95ce92909a0df390d86c0e.07c68af1.png)
The list of ENV variables:


- PORT - the port the application is run on (default `8080`).
- MAX_CONCURRENT_JOBS - the number of jobs that can be executed in parallel (default `2`).
- AUTO_MERGE - merge PRs when updates are pushed to the main branch.
One of [`true`, `false`] (default `false`).
- API_FOLDER - the path in the repository where Scout looks for API definitions (default `/`).
- DATA_FOLDER - the path to the folder where Scout stores temporary data.
- REDOCLY_API_URL - Redocly API base URL.
- REDOCLY_API_KEY - Redocly organization API token.
- REDOCLY_ORG_ID - Redocly organization ID.
- REDOCLY_PROJECT_ID - Redocly project ID.
- PORTAL_APIS_FOLDER - the path where Scout pushes discovered API definitions.
- REDOCLY_APIS - A JSON array of API configurations. Each configuration has the following fields:
  - `name` - API name.
  - `url` - API URL.
  - `apiKey` - API key.
  - `orgId` - Organization ID.
  - `projectId` - Project ID.
  - `jobContext` - A job execution context.
  - `metadataRequired` - If set to `true`, Scout requires metadata in the repository to run.
  - `detectChanges` - If set to `true`, Scout detects changes in the API definitions and create a changelog.
  - `autoMerge` - If set to `true`, Scout merges PRs when updates are pushed to the main branch.
  - `destFolderPath` - The path to the location where Scout pushes discovered API definitions.
  - `mountBranchName` - The branch name to mount the API definitions to.
> NOTE: Extract sensitive data from a secrets manager. The sensitive data can be referred to within the definition of other values:

```shell
REDOCLY_APIS='[{
  "name": "external",
  "url": "https://api.redocly.com/api",
  "apiKey": "${REDOCLY_API_KEY}",
  "orgId": "org_xxx",
  "projectId": "prj_xxx",
  "jobContext": "{metadata.team}",
  "metadataRequired": true,
  "detectChanges": true,
  "autoMerge": true,
  "destFolderPath": "apis/{metadata.team}/{repoId}/{title}",
}]'
REDOCLY_API_KEY='sk_xxx'
```
- LOG_FORMAT - one of [`pretty`, `json`] (default `json`).
- LOG_LEVEL - one of [`trace`, `debug`, `info`, `warn`, `error`, `fatal`] (default `info`).
- GITHUB_PROVIDERS - JSON array of GitHub app configurations. Each configuration has the following fields:
  - `url` - GitHub server url.
Omit in case of GitHub cloud.
  - `appId` - GitHub application ID.
`https://{github-server-url}/organizations/{org}/settings/apps` -> Redocly Scout -> `App ID`.
  - `appUserId` - GitHub application user that leaves Scout-related comments. `https://{github-server-url}/users/{app slug name}[bot]`
  - `privateKey` - GitHub application private key created during application configuration.
  - `webhookSecret` - GitHub webhook secret, created during application configuration.
> NOTE: Sensitive data should be extracted from secrets manager. It can be referred to within the definition of other values:

```shell
GITHUB_PROVIDERS='[{
  "appId": "123",
  "appUserId": "456",
  "privateKey": "${MY_PRIVATE_KEY}",
  "webhookSecret": "${MY_WH_SECRET}"
}]'
MY_PRIVATE_KEY='-----BEGIN RSA PRIVATE KEY-----
MIIEp...6G2Hg==
-----END RSA PRIVATE KEY-----'
MY_WH_SECRET='my-secret'
```
- `GITLAB_PROVIDERS` - JSON array of GitLab instance configurations. Each configuration has the following fields:
  - `url` - GitLab instance url.
Omit if you use GitLab.com (GitLab Cloud).
  - `userId` - GitLab user ID; instructions for how to obtain it are available in [GitLab section](https://redocly.com/docs/realm/scout/guides/install/#gitlab).
  - `privateToken` - GitLab private token generated on the user's account.
  - `webhookSecret` - GitLab secret used when creating a webhook on GitLab.
> NOTE: Sensitive data should be stored in a secrets manager and referred to within the definition of other values:

```shell
GITLAB_PROVIDERS='[{
  "userId": "456",
  "privateToken": "${MY_PRIVATE_TOKEN}",
  "webhookSecret": "${MY_WH_SECRET}"
}]'
MY_PRIVATE_TOKEN='my-private-token'
MY_WH_SECRET='my-secret'
```


1. Configure task resources CPU/memory/storage and select task execution
role. ![fill-task-definition-resources.png](/assets/fill-task-definition-resources.02babdfa4e3dd0466e63d46fb2177b2439551defb15b0a2de5f25869a644e287.07c68af1.png)
> NOTE: There is a default `escTaskExecutionRole` role, but you could create a new one
2. Click "Create".


### Create ECS cluster

1. Open [AWS ECS Clusters](https://us-east-1.console.aws.amazon.com/ecs/v2/clusters?region=us-east-1).
2. Click "Create cluster". ![create-a-new-cluster.png](/assets/create-a-new-cluster.4d514f7dd04f5440b64b999200330ea30a983922ba2c43723acf6e6af5331859.07c68af1.png)
3. Fill "Cluster name" field, select VPC and subnets. ![fill-cluster-name.png](/assets/fill-cluster-name.06bf854d1dd1e8bca5bd932329b68797edd48f8e579e877bf834757e38c7619f.07c68af1.png)
4. Click "Create".


### Create Service

1. Open [AWS ECS Clusters](https://us-east-1.console.aws.amazon.com/ecs/v2/clusters?region=us-east-1) and select created
cluster.
2. On the "Services" tab click "Create".
3. Fill service name and select the created task family. ![fill-service-name.png](/assets/fill-service-name.15f079197bab367d2a295e643a0acf9b32c0795f1774621aeb466f60bab3656f.07c68af1.png)
4. In the networking tab select VPC and its private subnets
> NOTE: There are shouldn't be public subnets
5. Configure a new security group ![fill-service-security-group.png](/assets/fill-service-security-group.019efa44bdcb12e68de5db84908a25aa15a83c554dfd0c6b4b0ee4edb9984739.07c68af1.png)
6. Turn off "Public IP" switch.
7. Create a new Application load balancer. ![fill-service-load-balancer.png](/assets/fill-service-load-balancer.0e7c64c8faf4d4a8a25713b4ba7a48f51f57938cbfcadc5e8f330b6032e52c59.07c68af1.png)
8. Configure SSL certificates, target group and its
healthcheck. ![fill-service-target-group.png](/assets/fill-service-target-group.7877bd4fef951cc0acf6703f2e8de2d6a72ca29cf33585cfa65e3a0b5d05a777.07c68af1.png)
9. Click "Create".


### Configure Load Balancer subnets

1. Open created service
2. Click "View load balancer"
3. Click "Actions" -> "Edit subnets"
4. In the networking mapping section select public subnets
5. Click "Save changes"


### Assign domain name

1. Copy load balancer domain name.
"View load balancer" -> "DNS name".
2. Open [AWS Route 53](https://us-east-1.console.aws.amazon.com/route53/v2/home#Dashboard).
3. Select hosted zone for selected SSL certificate.
4. Click "Create record".
5. Fill record details. ![fill-dns-details.png](/assets/fill-dns-details.a6ec78c952b8c251dd1b6ed8026b8d6e2cf2a6129b4145dc472a49c2e07d9d1d.07c68af1.png)
6. Click "Create records".


## Deploy with AWS CLI

### Create ECR repository


```shell
aws ecr create-repository --repository-name redocly-scout
```

### Build docker image and push to ECR repository


```shell
docker tag redocly-scout:latest <ECR repository ARN>:<image version>
docker push <ECR repository ARN>:<image version>
```

### Create task secrets


```shell
aws secretsmanager create-secret --name scout-redocly-api-key --secret-string <Redocly API key>
aws secretsmanager create-secret --name scout-github-private-key --secret-string <GitHub app private key>
aws secretsmanager create-secret --name scout-github-webhook-secret --secret-string <GitHub app webhook secret>
```

### Create task definition

Please follow the official [AWS tutorial](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_AWSCLI_Fargate.html) to create ECS Task

Example of `task_definition.json`:


```json
{
  "family": "redocly-scout-task",
  "containerDefinitions": [
    {
      "name": "redocly-scout",
      "image": "<image ARN>",
      "portMappings": [
        {
          "name": "redocly-scout-8080-tcp",
          "containerPort": 8080,
          "hostPort": 8080,
          "protocol": "tcp",
          "appProtocol": "http"
        }
      ],
      "essential": true,
      "environment": [
        {
          "name": "PORT",
          "value": "8080"
        },
        {
          "name": "DATA_FOLDER",
          "value": "/tmp/redocly/scout-data/"
        },
        {
          "name": "REDOCLY_API_URL",
          "value": "https://<Redocly hostname>/api"
        },
        {
          "name": "MAX_CONCURRENT_JOBS",
          "value": "5"
        },
        {
          "name": "PORTAL_APIS_FOLDER",
          "value": "/apis"
        },
        {
          "name": "REDOCLY_PROJECT_ID",
          "value": "<Redocly project ID>"
        },
        {
          "name": "API_FOLDER",
          "value": "/"
        },
        {
          "name": "AUTO_MERGE",
          "value": "true"
        },
        {
          "name": "LOG_FORMAT",
          "value": "json"
        },
        {
          "name": "REDOCLY_ORG_ID",
          "value": "<Redocly organization ID>"
        },
        {
          "name": "LOG_LEVEL",
          "value": "debug"
        },
        {
          "name": "GITHUB_PROVIDERS",
          "value": "[{\"appId\": \"123\",\"appUserId\": \"456\",\"privateKey\": \"${MY_PRIVATE_KEY}\",\"webhookSecret\": \"${MY_WH_SECRET}\"}]"
        }
      ],
      "secrets": [
        {
          "name": "REDOCLY_API_KEY",
          "valueFrom": "<Redocly API key secret ARN>"
        },
        {
          "name": "MY_WH_SECRET",
          "valueFrom": "<GitHub app webhook secret ARN>"
        },
        {
          "name": "MY_PRIVATE_KEY",
          "valueFrom": "<GitHub app private key secret ARN>"
        }
      ]
    }
  ],
  "requiresCompatibilities": ["FARGATE"],
  "executionRoleArn": "<Execution role ARN>",
  "volumes": [],
  "networkMode": "awsvpc",
  "cpu": "1024",
  "memory": "2048"
}
```
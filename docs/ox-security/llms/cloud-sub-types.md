# Source: https://docs.ox.security/api-documentation/api-reference/api--artifact/types/enums/cloud-sub-types.md

# cloudSubTypes

Types of cloud computing services.

### Examples

```graphql
enum CloudSubTypes {
  Lambda
  CloudFunction
  ECS
  EKS
  AKS
  GKE
  OpenShift
  EC2
  ComputeEngine
  Generic
}
```

### Enum values

| Enum value    | Description                       |
| ------------- | --------------------------------- |
| Lambda        | AWS Lambda serverless functions   |
| CloudFunction | Google Cloud Functions            |
| ECS           | Amazon Elastic Container Service  |
| EKS           | Amazon Elastic Kubernetes Service |
| AKS           | Azure Kubernetes Service          |
| GKE           | Google Kubernetes Engine          |
| OpenShift     | Red Hat OpenShift                 |
| EC2           | Amazon Elastic Compute Cloud      |
| ComputeEngine | Google Compute Engine             |
| Generic       | For Kubernetes Cloud              |

### References

#### Fields with this object

* [{} CloudDescription.subType](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/cloud-description)

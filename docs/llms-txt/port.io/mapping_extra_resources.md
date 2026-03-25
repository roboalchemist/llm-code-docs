# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/cloud-providers/gcp/examples/mapping_extra_resources.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/resource_templates/mapping_extra_resources.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws/examples/mapping_extra_resources.md

# Mapping Extra Resources

As you've probably looked at the [Examples](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws/examples/.md) page, you've noticed that the AWS Integration supports some AWS resources, but most of them are not documented in the Examples page.

This page will help you understand what kind of AWS resources are supported by the AWS integration and how to map them into Port.

## Is the resource supported by the AWS Integration?[â](#is-the-resource-supported-by-the-aws-integration "Direct link to Is the resource supported by the AWS Integration?")

The AWS Integration relies on AWS's Cloud Control API. That means:

1. Is the type of resource I want to ingest listed [here](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/supported-resources.html) and supported by the list method?

   <!-- -->

   * **If so**: Great! It's supported.
   * **If not**: Please contact us or contribute by [adding support](https://ocean.getport.io/develop-an-integration/) to [the integration](https://github.com/port-labs/ocean/tree/main/integrations/aws) yourself.

For the full list of supported resources, refer to [AWS Cloud Control API Supported resources](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/supported-resources.html).

## Resources supported by Cloud Control API but not supported in AWS Integration[â](#resources-supported-by-cloud-control-api-but-not-supported-in-aws-integration "Direct link to Resources supported by Cloud Control API but not supported in AWS Integration")

The AWS Integration relies on AWS's Cloud Control API. While many resources are supported, some require additional inputs to be queried, which the integration currently does not support. Below is a list of the resources that are unsupported due to this limitation.

### List of unsupported resources[â](#list-of-unsupported-resources "Direct link to List of unsupported resources")

AWS resources that requires additional input

```
AWS::Amplify::Branch
AWS::AmplifyUIBuilder::Component
AWS::AmplifyUIBuilder::Form
AWS::AmplifyUIBuilder::Theme
AWS::ApiGateway::Authorizer
AWS::ApiGateway::BasePathMapping
AWS::ApiGateway::DocumentationPart
AWS::ApiGateway::Deployment
AWS::ApiGateway::DocumentationVersion
AWS::ApiGateway::GatewayResponse
AWS::ApiGateway::Model
AWS::ApiGateway::RequestValidator
AWS::ApiGateway::Resource
AWS::ApiGateway::Stage
AWS::ApiGateway::UsagePlanKey
AWS::ApiGatewayV2::Authorizer
AWS::ApiGatewayV2::ApiMapping
AWS::ApiGatewayV2::Deployment
AWS::ApiGatewayV2::Model
AWS::ApiGatewayV2::Integration
AWS::ApiGatewayV2::Route
AWS::AppConfig::ConfigurationProfile
AWS::AppConfig::Environment
AWS::AppConfig::HostedConfigurationVersion
AWS::ApplicationAutoScaling::ScalingPolicy
AWS::AppSync::FunctionConfiguration
AWS::AppSync::Resolver
AWS::AppSync::SourceApiAssociation
AWS::APS::RuleGroupsNamespace
AWS::Athena::PreparedStatement
AWS::Bedrock::DataSource
AWS::Bedrock::AgentAlias
AWS::Bedrock::FlowAlias
AWS::Bedrock::FlowVersion
AWS::Bedrock::PromptVersion
AWS::CleanRooms::AnalysisTemplate
AWS::CleanRooms::ConfiguredTableAssociation
AWS::CleanRooms::IdMappingTable
AWS::CleanRooms::IdNamespaceAssociation
AWS::CleanRooms::PrivacyBudgetTemplate
AWS::CloudFormation::ResourceVersion
AWS::CodeArtifact::PackageGroup
AWS::Cognito::IdentityPoolPrincipalTag
AWS::Cognito::IdentityPoolRoleAttachment
AWS::Cognito::UserPoolClient
AWS::Cognito::UserPoolGroup
AWS::Cognito::UserPoolResourceServer
AWS::Cognito::UserPoolUser
AWS::ControlTower::EnabledControl
AWS::CustomerProfiles::EventStream
AWS::CustomerProfiles::Integration
AWS::CustomerProfiles::ObjectType
AWS::DataZone::DataSource
AWS::DataZone::Environment
AWS::DataZone::EnvironmentActions
AWS::DataZone::EnvironmentBlueprintConfiguration
AWS::DataZone::EnvironmentProfile
AWS::DataZone::GroupProfile
AWS::DataZone::Project
AWS::DataZone::ProjectMembership
AWS::DataZone::SubscriptionTarget
AWS::DataZone::UserProfile
AWS::Deadline::Fleet
AWS::Deadline::MeteredProduct
AWS::Deadline::Queue
AWS::Deadline::QueueEnvironment
AWS::Deadline::QueueFleetAssociation
AWS::Deadline::StorageProfile
AWS::EC2::IPAMAllocation
AWS::EC2::IPAMPoolCidr
AWS::EC2::Route
AWS::EC2::TransitGatewayMulticastDomainAssociation
AWS::EC2::TransitGatewayMulticastGroupMember
AWS::EC2::TransitGatewayMulticastGroupSource
AWS::EC2::TransitGatewayRoute
AWS::EC2::TransitGatewayRouteTableAssociation
AWS::EC2::TransitGatewayRouteTablePropagation
AWS::EC2::VPCCidrBlock
AWS::ECS::TaskSet
AWS::EFS::MountTarget
AWS::EKS::AccessEntry
AWS::EKS::Addon
AWS::EKS::FargateProfile
AWS::EKS::IdentityProviderConfig
AWS::EKS::Nodegroup
AWS::EKS::PodIdentityAssociation
AWS::ElasticLoadBalancingV2::Listener
AWS::ElasticLoadBalancingV2::ListenerRule
AWS::ElasticLoadBalancingV2::TrustStoreRevocation
AWS::EntityResolution::PolicyStatement
AWS::EventSchemas::Schema
AWS::FIS::TargetAccountConfiguration
AWS::Glue::SchemaVersion
AWS::Glue::SchemaVersionMetadata
AWS::GreengrassV2::ComponentVersion
AWS::IdentityStore::Group
AWS::IdentityStore::GroupMembership
AWS::ImageBuilder::Component
AWS::ImageBuilder::Image
AWS::ImageBuilder::Workflow
AWS::IoTSiteWise::AccessPolicy
AWS::IoTSiteWise::Dashboard
AWS::IoTTwinMaker::ComponentType
AWS::IoTTwinMaker::Entity
AWS::IoTTwinMaker::SyncJob
AWS::IoTTwinMaker::Scene
AWS::IVS::StreamKey
AWS::Kendra::DataSource
AWS::Kendra::Faq
AWS::Lambda::Alias
AWS::Lambda::EventInvokeConfig
AWS::Lambda::Permission
AWS::Lambda::Url
AWS::Lambda::Version
AWS::Logs::AccountPolicy
AWS::Logs::LogStream
AWS::Logs::SubscriptionFilter
AWS::MediaConnect::FlowEntitlement
AWS::MediaConnect::FlowOutput
AWS::MediaConnect::FlowSource
AWS::MediaConnect::FlowVpcInterface
AWS::MediaLive::ChannelPlacementGroup
AWS::MediaLive::Multiplexprogram
AWS::MediaPackage::Asset
AWS::MediaPackage::PackagingConfiguration
AWS::MediaPackageV2::Channel
AWS::MediaPackageV2::OriginEndpoint
AWS::MediaTailor::LiveSource
AWS::MediaTailor::VodSource
AWS::MSK::BatchScramSecret
AWS::MSK::ClusterPolicy
AWS::NetworkFirewall::LoggingConfiguration
AWS::NetworkManager::CustomerGatewayAssociation
AWS::NetworkManager::Device
AWS::NetworkManager::Link
AWS::NetworkManager::LinkAssociation
AWS::NetworkManager::Site
AWS::NetworkManager::TransitGatewayRegistration
AWS::OpenSearchServerless::AccessPolicy
AWS::OpenSearchServerless::LifecyclePolicy
AWS::OpenSearchServerless::SecurityConfig
AWS::OpenSearchServerless::SecurityPolicy
AWS::Organizations::OrganizationalUnit
AWS::Organizations::Policy
AWS::PCAConnectorAD::ServicePrincipalName
AWS::PCAConnectorAD::Template
AWS::PCAConnectorAD::TemplateGroupAccessControlEntry
AWS::PCAConnectorSCEP::Challenge
AWS::QLDB::Stream
AWS::QuickSight::Analysis
AWS::QuickSight::Dashboard
AWS::QuickSight::DataSet
AWS::QuickSight::DataSource
AWS::QuickSight::RefreshSchedule
AWS::QuickSight::Template
AWS::QuickSight::Theme
AWS::RDS::DBProxyTargetGroup
AWS::RefactorSpaces::Application
AWS::RefactorSpaces::Route
AWS::RefactorSpaces::Service
AWS::Route53Profiles::ProfileResourceAssociation
AWS::S3Outposts::AccessPoint
AWS::S3Outposts::Bucket
AWS::SageMaker::ImageVersion
AWS::ServiceCatalog::ServiceActionAssociation
AWS::ServiceCatalogAppRegistry::AttributeGroupAssociation
AWS::ServiceCatalogAppRegistry::ResourceAssociation
AWS::Signer::ProfilePermission
AWS::SSO::Application
AWS::SSO::Assignment
AWS::SSO::InstanceAccessControlAttributeConfiguration
AWS::SSO::PermissionSet
AWS::StepFunctions::StateMachineAlias
AWS::StepFunctions::StateMachineVersion
AWS::Transfer::Agreement
AWS::VerifiedPermissions::IdentitySource
AWS::VerifiedPermissions::Policy
AWS::VerifiedPermissions::PolicyTemplate
AWS::VpcLattice::AccessLogSubscription
AWS::VpcLattice::Listener
AWS::VpcLattice::Rule
AWS::WAFv2::IPSet
AWS::WAFv2::RegexPatternSet
AWS::WAFv2::RuleGroup
AWS::WAFv2::WebACL
AWS::WorkSpacesWeb::IdentityProvider
```

### What can you do?[â](#what-can-you-do "Direct link to What can you do?")

* **Contact us**: If you require support for any of these resources, please reach out to our team for assistance.
* **Submit a feature request**: Contribute to our integration's improvement by [submitting a feature request](https://roadmap.getport.io/).
* **Contribute directly**: Developers are encouraged to [contribute](https://ocean.getport.io/develop-an-integration/) by adding support for these resources [here](https://github.com/port-labs/ocean/tree/main/integrations/aws).

## Configuration[â](#configuration "Direct link to Configuration")

Port integrations use a [YAML mapping block](/build-your-software-catalog/customize-integrations/configure-mapping.md#configuration-structure) to ingest data from the third-party api into Port.

The mapping makes use of the [JQ JSON processor](https://stedolan.github.io/jq/manual/) to select, modify, concatenate, transform and perform other operations on existing fields and values from the integration API.

### `useGetResourceAPI` property support[â](#usegetresourceapi-property-support "Direct link to usegetresourceapi-property-support")

* By default the integration uses the [`CloudControl:ListResources`](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_ListResources.html) API to get the resources. The integration can also enrich each resource by running [`CloudControl:GetResource`](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_GetResource.html) on each resource, you can use this by enabling `useGetResourceAPI` option.

  The `useGetResourceAPI` option is only available for resources that support the `CloudControl:GetResource` API.

```
resources:
  - kind: AWS::Lambda::Function
    selector:
      query: 'true' # JQ boolean query. If evaluated to false - skip syncing the object.
      useGetResourceAPI: 'true'
    port:
      entity:
        mappings: # Mappings between one AWS object to a Port entity. Each value is a JQ query.
          identifier: '.Identifier'
          title: '.Properties.FunctionName'
          blueprint: 'lambda'
          properties:
            kind: '.__Kind'
            region: '.__Region'
            link: "'https://console.aws.amazon.com/go/view?arn=' + .Properties.Arn"
            description: '.Properties.Description'
            memorySize: '.Properties.MemorySize'
            ephemeralStorageSize: '.Properties.EphemeralStorage.Size'
            timeout: '.Properties.Timeout'
            runtime: '.Properties.Runtime'
            packageType: '.Properties.PackageType'
            environment: '.Properties.Environment'
            architectures: '.Properties.Architectures'
            layers: '.Properties.Layers'
            tags: '.Properties.Tags'
            iamRole: "'https://console.aws.amazon.com/go/view?arn=' + .Properties.Role"
            arn: '.Properties.Arn'
          relations:
            account: '.__AccountId'
```

**Note: Using the `useGetResourceAPI` option will make each resync run slower and use a lot more memory and cpu so you might want to add memory and cpu limits.**

Get an example of the AWS resource properties

To get an example of the AWS resource properties, you can use the [AWS Cloud Control API](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/what-is-cloudcontrolapi.html) to get the resource properties.

For example for the `AWS::Lambda::Function` resource, you can use the following command to get the resource properties:

```
aws cloudcontrol list-resources --type-name AWS::Lambda::Function --max-items 1 | jq .ResourceDescriptions
```

### Querying resources from specific regions[â](#querying-resources-from-specific-regions "Direct link to Querying resources from specific regions")

The `regionPolicy` option allows users to define a policy for querying resources in specific AWS regions. This feature enables finer control over which AWS regions are included or excluded when fetching resources. The `regionPolicy` option works with `allow` and `deny` lists to specify allowed or restricted regions.

* **allow**: A list of regions explicitly permitted for querying.
* **deny**: A list of regions explicitly restricted from querying.

#### How `regionPolicy` Works[â](#how-regionpolicy-works "Direct link to how-regionpolicy-works")

1. **If both lists are empty**: All regions are allowed.
2. **If the region is in `deny`**: It is excluded unless explicitly allowed.
3. **If the region is in `allow`**: It is included for querying.
4. **If a region appears in both lists**: It is excluded.
5. **If only `deny` is specified**: Only regions in the `deny` list are excluded.
6. **If only `allow` is specified**: Only regions in the `allow` list are included.

#### Example Configuration[â](#example-configuration "Direct link to Example Configuration")

```
resources:
  - kind: AWS::Lambda::Function
    selector:
      query: 'true'
      useGetResourceAPI: 'true'
      regionPolicy:
        allow: ["us-east-1", "eu-west-1"]
        deny: ["us-west-2"]
    port:
      entity:
        mappings:
          identifier: '.Identifier'
          title: '.Properties.FunctionName'
          blueprint: 'lambda'
          properties:
            region: '.__Region'
            description: '.Properties.Description'
            arn: '.Properties.Arn'
          relations:
            account: '.__AccountId'
```

In this example, resources in the `us-east-1` and `eu-west-1` regions are allowed, while `us-west-2` is denied.

## Mapping the resource to Port[â](#mapping-the-resource-to-port "Direct link to Mapping the resource to Port")

After you've found the resource in the [AWS Cloud Control API Docs](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/supported-resources.html), you can map it to Port by following these steps:

### Compute resources blueprint example[â](#compute-resources-blueprint-example "Direct link to Compute resources blueprint example")

Create a Port blueprint definition for the resource. The blueprint definition is based on the resource API specified per asset type. A few examples of blueprints for compute resources are provided below:

Lightsail Instance Blueprint

Create in Port

```
{
  "identifier": "lightsailInstance",
  "description": "This blueprint represents an AWS Lightsail Instance in our software catalog",
  "title": "Lightsail Instance",
  "icon": "AWS",
  "schema": {
    "properties": {
      "link": {
        "type": "string",
        "format": "url",
        "title": "Link"
      },
      "state": {
        "type": "string",
        "title": "State"
      },
      "blueprintId": {
        "type": "string",
        "title": "Blueprint ID"
      },
      "bundleId": {
        "type": "string",
        "title": "Bundle ID"
      },
      "arn": {
        "type": "string",
        "title": "ARN"
      },
      "privateIpAddress": {
        "type": "string",
        "title": "Private IP Address"
      },
      "publicIpAddress": {
        "type": "string",
        "title": "Public IP Address"
      },
      "cpuCount": {
        "type": "number",
        "title": "CPU Count"
      },
      "ramSize": {
        "type": "number",
        "title": "RAM Size (GB)"
      },
      "regionName": {
        "type": "string",
        "title": "Region Name"
      },
      "availabilityZone": {
        "type": "string",
        "title": "Availability Zone"
      },
      "monthlyTransfer": {
        "type": "number",
        "title": "Monthly Transfer (GB)"
      },
      "ports": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "title": "Ports"
      },
      "username": {
        "type": "string",
        "title": "Username"
      },
      "tags": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "title": "Tags"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {
    "account": {
      "title": "Account",
      "target": "awsAccount",
      "required": true,
      "many": false
    }
  }
}
```

Elastic Beanstalk Application Blueprint

Create in Port

```
{
  "identifier": "elasticBeanstalkApplication",
  "description": "This blueprint represents an AWS Elastic Beanstalk Application in our software catalog",
  "title": "Elastic Beanstalk Application",
  "icon": "AWS",
  "schema": {
    "properties": {
      "link": {
        "type": "string",
        "format": "url",
        "title": "Link"
      },
      "applicationName": {
        "type": "string",
        "title": "Application Name"
      },
      "maxAgeInDays": {
        "type": "number",
        "title": "Max Age In Days"
      },
      "maxCount": {
        "type": "number",
        "title": "Max Count"
      },
      "kind": {
        "type": "string",
        "title": "Kind"
      },
      "region": {
        "type": "string",
        "title": "Region"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {
    "account": {
      "title": "Account",
      "target": "awsAccount",
      "required": true,
      "many": false
    }
  }
}
```

ECS Service Blueprint

Create in Port

```
{
  "identifier": "ecsService",
  "description": "This blueprint represents an AWS ECS Service in our software catalog",
  "title": "ECS Service",
  "icon": "AWS",
  "schema": {
    "properties": {
      "link": {
        "type": "string",
        "format": "url",
        "title": "Link"
      },
      "desiredCount": {
        "type": "number",
        "title": "Desired Count"
      },
      "taskDefinition": {
        "type": "string",
        "title": "Task Definition"
      },
      "launchType": {
        "type": "string",
        "enum": ["EC2", "FARGATE", "EXTERNAL"],
        "title": "Launch Type"
      },
      "schedulingStrategy": {
        "type": "string",
        "enum": ["REPLICA", "DAEMON"],
        "title": "Scheduling Strategy"
      },
      "loadBalancers": {
        "type": "array",
        "title": "Load Balancers"
      },
      "securityGroups": {
        "type": "array",
        "title": "Security Groups"
      },
      "subnets": {
        "type": "array",
        "title": "Subnets"
      },
      "iamRole": {
        "type": "string",
        "format": "url",
        "title": "IAM Role",
        "icon": "Unlock"
      },
      "arn": {
        "type": "string",
        "title": "ARN"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {
    "account": {
      "title": "Account",
      "target": "awsAccount",
      "required": true,
      "many": false
    }
  }
}
```

SQS Blueprint

Create in Port

```
{
  "identifier": "sqs",
  "description": "This blueprint represents an AWS SQS service in our software catalog",
  "title": "SQS",
  "icon": "AWS",
  "schema": {
    "properties": {
      "link": {
        "type": "string",
        "format": "url",
        "title": "Link"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {
    "account": {
      "title": "Account",
      "target": "awsAccount",
      "required": true,
      "many": false
    }
  }
}
```

Lambda Blueprint

Create in Port

```
{
  "identifier": "lambda",
  "description": "This blueprint represents an AWS Lambda function in our software catalog",
  "title": "Lambda",
  "icon": "Lambda",
  "schema": {
    "properties": {
      "link": {
        "type": "string",
        "format": "url",
        "title": "Link"
      },
      "description": {
        "type": "string",
        "title": "Description"
      },
      "memorySize": {
        "type": "number",
        "title": "Memory Size"
      },
      "ephemeralStorageSize": {
        "type": "number",
        "title": "Ephemeral Storage Size"
      },
      "timeout": {
        "type": "number",
        "title": "Timeout"
      },
      "runtime": {
        "type": "string",
        "title": "Runtime"
      },
      "packageType": {
        "type": "string",
        "enum": ["Image", "Zip"],
        "title": "Package Type"
      },
      "environment": {
        "type": "object",
        "title": "Environment"
      },
      "architectures": {
        "type": "array",
        "items": {
          "type": "string",
          "enum": ["x86_64", "arm64"]
        },
        "title": "Architectures"
      },
      "layers": {
        "type": "array",
        "title": "Layers"
      },
      "tags": {
        "type": "array",
        "title": "Tags"
      },
      "iamRole": {
        "type": "string",
        "format": "url",
        "title": "IAM Role",
        "icon": "Unlock"
      },
      "arn": {
        "type": "string",
        "title": "ARN"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {
    "account": {
      "title": "Account",
      "target": "awsAccount",
      "required": true,
      "many": false
    }
  }
}
```

### Compute resources integration configuration example[â](#compute-resources-integration-configuration-example "Direct link to Compute resources integration configuration example")

Create an integration configuration for the resource. The integration configuration is a YAML file that describes the ETL process to load data into the developer portal.

Mapping Configuration for Lambda, ECS Service, SQS, Lightsail, ElasticBeanstalk

```
resources:
  - kind: AWS::Lambda::Function
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .Identifier
          title: .Properties.FunctionName
          blueprint: '"lambda"'
          properties:
            kind: .__Kind
            region: .__Region
            link: "'https://console.aws.amazon.com/go/view?arn=' + .Properties.Arn"
            description: .Properties.Description
            memorySize: .Properties.MemorySize
            ephemeralStorageSize: .Properties.EphemeralStorage.Size
            timeout: .Properties.Timeout
            runtime: .Properties.Runtime
            packageType: .Properties.PackageType
            environment: .Properties.Environment
            architectures: .Properties.Architectures
            layers: .Properties.Layers
            tags: .Properties.Tags
            iamRole: "'https://console.aws.amazon.com/go/view?arn=' + .Properties.Role"
            arn: .Properties.Arn
          relations:
            account: .__AccountId
  - kind: AWS::ECS::Service
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .Identifier | split(":")[5] | split("/")[2] | split("|")[0]
          title: .Identifier
          blueprint: '"ecsService"'
          properties:
            kind: .__Kind
            region: .__Region
            link: >-
              'https://console.aws.amazon.com/go/view?arn=' +
              .Properties.ServiceArn
            desiredCount: .Properties.DesiredCount
            launchType: .Properties.LaunchType
            cluster: .Properties.Cluster
            schedulingStrategy: .Properties.SchedulingStrategy
            loadBalancers: .Properties.LoadBalancers
            securityGroups: >-
              .Properties.NetworkConfiguration.AwsvpcConfiguration.SecurityGroups
            subnets: .Properties.NetworkConfiguration.AwsvpcConfiguration.Subnets
            taskDefinition: .Properties.TaskDefinition
            iamRole: >-
              .Role | if . == null then null else
              'https://console.aws.amazon.com/go/view?arn=' + . end
            arn: .Properties.ServiceArn
          relations:
            account: .__AccountId
  - kind: AWS::SQS::Queue
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .Identifier | split("/")[4]
          title: .Properties.QueueUrl | split("/")[4]
          blueprint: '"sqs"'
          properties:
            kind: .__Kind
            region: .__Region
            link: .Properties.QueueUrl
          relations:
            account: .__AccountId
  - kind: AWS::Lightsail::Instance
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .Identifier
          title: .Properties.InstanceName
          blueprint: '"lightsailInstance"'
          properties:
            link: >-
                'https://console.aws.amazon.com/go/view?arn=' +
                .Properties.InstanceArn
            state: .Properties.State.Name
            blueprintId: .Properties.BlueprintId
            bundleId: .Properties.BundleId
            arn: .Properties.InstanceArn
            privateIpAddress: .Properties.PrivateIpAddress
            publicIpAddress: .Properties.PublicIpAddress
            cpuCount: .Properties.Hardware.CpuCount
            ramSize: .Properties.Hardware.RamSizeInGb
            regionName: Properties.RegionName
            availabilityZone: .Properties.AvailabilityZone
            monthlyTransfer: .Properties.MonthlyTransfer.GbPerMonthAllocated
            ports: .Properties.Networking.Ports[](.FromPort | tostring + ' - ' + .ToPort | tostring + ' - ' + .AccessDirection)
            username: .Properties.UserName
            tags: .Properties.Tags
          relations:
            account: .__AccountId
  - kind: AWS::ElasticBeanstalk::Application
    selector:
      query: 'true'
      useGetResourceAPI: 'true'
    port:
      entity:
        mappings:
          identifier: .Identifier
          title: .Properties.ApplicationName
          blueprint: '"elasticBeanstalkApplication"'
          properties:
            link: >-
                'https://console.aws.amazon.com/elasticbeanstalk/home?region=' +
                .__Region +
                '/application/overview?applicationName=' + .Properties.ApplicationName
            applicationName: .Properties.ApplicationName
            maxAgeInDays: .Properties.ResourceLifecycleConfig.VersionLifecycleConfig.MaxAgeRule.MaxAgeInDays
            maxCount: .Properties.ResourceLifecycleConfig.VersionLifecycleConfig.MaxCountRule.MaxCount
            kind: .__Kind
            region: .__Region
          relations:
            account: .__AccountId
```

### Developer tools blueprint and configuration example[â](#developer-tools-blueprint-and-configuration-example "Direct link to Developer tools blueprint and configuration example")

Amplify App Blueprint

Create in Port

```
{
  "identifier": "amplifyApp",
  "description": "This blueprint represents an AWS Amplify App in our software catalog",
  "title": "Amplify App",
  "icon": "AWS",
  "schema": {
    "properties": {
      "link": {
        "type": "string",
        "format": "url",
        "title": "Link"
      },
      "appId": {
        "type": "string",
        "title": "App ID"
      },
      "repository": {
        "type": "string",
        "title": "Repository"
      },
      "platform": {
        "type": "string",
        "title": "Platform"
      },
      "defaultDomain": {
        "type": "string",
        "title": "Default Domain"
      },
      "customHeaders": {
        "type": "string",
        "title": "Custom Headers"
      },
      "appName": {
        "type": "string",
        "title": "App Name"
      },
      "arn": {
        "type": "string",
        "title": "ARN"
      },
      "kind": {
        "type": "string",
        "title": "Kind"
      },
      "region": {
        "type": "string",
        "title": "Region"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {
    "account": {
      "title": "Account",
      "target": "awsAccount",
      "required": true,
      "many": false
    }
  }
}
```

Mapping Configuration for Amplify App

```
resources:
  - kind: AWS::Amplify::App
    selector:
      query: 'true'
      useGetResourceAPI: 'true'
    port:
      entity:
        mappings:
          identifier: .Identifier
          title: .Properties.AppName
          blueprint: '"amplifyApp"'
          properties:
            link: >-
                'https://console.aws.amazon.com/go/view?arn=' +
                .Properties.Arn
            appId: .Properties.AppId
            repository: .Properties.Repository
            platform: .Properties.Platform
            defaultDomain: .Properties.DefaultDomain
            customHeaders: .Properties.CustomHeaders
            appName: .Properties.AppName
            arn: .Properties.Arn
            kind: .__Kind
            region: .__Region
          relations:
            account: .__AccountId
```

### Application integration blueprint and configuration example[â](#application-integration-blueprint-and-configuration-example "Direct link to Application integration blueprint and configuration example")

Kinesis Stream Blueprint

Create in Port

```
{
  "identifier": "kinesisStream",
  "description": "This blueprint represents an AWS Kinesis Stream in our software catalog",
  "title": "Kinesis Stream",
  "icon": "AWS",
  "schema": {
    "properties": {
      "link": {
        "type": "string",
        "format": "url",
        "title": "Link"
      },
      "streamMode": {
        "type": "string",
        "title": "Stream Mode"
      },
      "shardCount": {
        "type": "number",
        "title": "Shard Count"
      },
      "retentionPeriodHours": {
        "type": "number",
        "title": "Retention Period Hours"
      },
      "shardLevelMetrics": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "title": "Shard Level Metrics"
      },
      "arn": {
        "type": "string",
        "title": "ARN"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {
    "account": {
      "title": "Account",
      "target": "awsAccount",
      "required": true,
      "many": false
    }
  }
}
```

SNS Topic Blueprint

Create in Port

```
{
  "identifier": "snsTopic",
  "description": "This blueprint represents an AWS SNS Topic in our software catalog",
  "title": "SNS Topic",
  "icon": "AWS",
  "schema": {
    "properties": {
      "link": {
        "type": "string",
        "format": "url",
        "title": "Link"
      },
      "arn": {
        "type": "string",
        "title": "ARN"
      },
      "kind": {
        "type": "string",
        "title": "Kind"
      },
      "region": {
        "type": "string",
        "title": "Region"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {
    "account": {
      "title": "Account",
      "target": "awsAccount",
      "required": true,
      "many": false
    }
  }
}
```

Mapping Configuration for Kinesis Stream and SNS Topic

```
resources:
  - kind: AWS::Kinesis::Stream
    selector:
      query: 'true'
      useGetResourceAPI: 'true'
    port:
      entity:
        mappings:
          identifier: .Identifier
          title: .Properties.Name
          blueprint: '"kinesisStream"'
          properties:
            link: >-
               'https://console.aws.amazon.com/go/view?arn=' +
               .Properties.Arn
            streamMode: .Properties.StreamModeDetails.StreamMode
            shardCount: .Properties.ShardCount
            retentionPeriodHours: .Properties.RetentionPeriodHours
            shardLevelMetrics: .Properties.DesiredShardLevelMetrics
            arn: .Properties.Arn
          relations:
            account: .__AccountId
  - kind: AWS::SNS::Topic
    selector:
      query: 'true'
      useGetResourceAPI: 'true'
    port:
      entity:
        mappings:
          identifier: .Identifier
          title: .Properties.TopicName
          blueprint: '"snsTopic"'
          properties:
            link: >-
               'https://console.aws.amazon.com/go/view?arn=' +
                .Properties.TopicArn
            arn: .Properties.TopicArn
            kind: .__Kind
            region: .__Region
          relations:
            account: .__AccountId
```

### Machine learning blueprint and configuration example[â](#machine-learning-blueprint-and-configuration-example "Direct link to Machine learning blueprint and configuration example")

Lex Bot Blueprint

Create in Port

```
{
  "identifier": "lexBot",
  "description": "This blueprint represents an AWS Lex Bot in our software catalog",
  "title": "Lex Bot",
  "icon": "AWS",
  "schema": {
    "properties": {
      "link": {
        "type": "string",
        "format": "url",
        "title": "Link"
      },
      "arn": {
        "type": "string",
        "title": "ARN"
      },
      "role": {
        "type": "string",
        "title": "Role ARN"
      },
      "name": {
        "type": "string",
        "title": "Name"
      },
      "idleSessionTTLInSeconds": {
        "type": "number",
        "title": "Idle Session TTL In Seconds"
      },
      "dataPrivacy": {
        "type": "object",
        "title": "Data Privacy",
        "properties": {
          "childDirected": {
            "type": "boolean",
            "title": "Child Directed"
          }
        }
      },
      "kind": {
        "type": "string",
        "title": "Kind"
      },
      "region": {
        "type": "string",
        "title": "Region"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {
    "account": {
      "title": "Account",
      "target": "awsAccount",
      "required": true,
      "many": false
    }
  }
}
```

Mapping Configuration for Lex Bot

```
resources:
  - kind: AWS::Lex::Bot
    selector:
      query: 'true'
      useGetResourceAPI: 'true'
    port:
      entity:
        mappings:
          identifier: .Identifier
          title: .Properties.Name
          blueprint: '"lexBot"'
          properties:
            link: >-
                'https://console.aws.amazon.com/go/view?arn=' +
                .Properties.Arn
            arn: .Properties.Arn
            role: .Properties.RoleArn
            name: .Properties.Name
            idleSessionTTLInSeconds: .Properties.IdleSessionTTLInSeconds
            dataPrivacy: .Properties.DataPrivacy
            kind: .__Kind
            region: .__Region
          relations:
            account: .__AccountId
```

### Management and governance blueprint and configuration example[â](#management-and-governance-blueprint-and-configuration-example "Direct link to Management and governance blueprint and configuration example")

Auto Scaling Group Blueprint

Create in Port

```
{
  "identifier": "autoScalingGroup",
  "description": "This blueprint represents an AWS Auto Scaling Group in our software catalog",
  "title": "Auto Scaling Group",
  "icon": "AWS",
  "schema": {
    "properties": {
      "link": {
        "type": "string",
        "format": "url",
        "title": "Link"
      },
      "desiredCapacity": {
        "type": "number",
        "title": "Desired Capacity"
      },
      "minSize": {
        "type": "number",
        "title": "Minimum Size"
      },
      "maxSize": {
        "type": "number",
        "title": "Maximum Size"
      },
      "arn": {
        "type": "string",
        "title": "ARN"
      },
      "role": {
        "type": "string",
        "format": "url",
        "title": "Service Linked Role ARN"
      },
      "kind": {
        "type": "string",
        "title": "Kind"
      },
      "region": {
        "type": "string",
        "title": "Region"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {
    "account": {
      "title": "Account",
      "target": "awsAccount",
      "required": true,
      "many": false
    }
  }
}
```

CloudFormation Stack Blueprint

Create in Port

```
{
  "identifier": "cloudformationStack",
  "description": "This blueprint represents an AWS CloudFormation Stack in our software catalog",
  "title": "CloudFormation Stack",
  "icon": "AWS",
  "schema": {
    "properties": {
      "link": {
        "type": "string",
        "format": "url",
        "title": "Link"
      },
      "arn": {
        "type": "string",
        "title": "ARN"
      },
      "kind": {
        "type": "string",
        "title": "Kind"
      },
      "region": {
        "type": "string",
        "title": "Region"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {
    "account": {
      "title": "Account",
      "target": "awsAccount",
      "required": true,
      "many": false
    }
  }
}
```

Mapping Configuration for CloudFormation Stack and Auto Scaling Group

```
resources:
  - kind: AWS::CloudFormation::Stack
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .StackId
          title: .StackName
          blueprint: '"cloudformationStack"'
          properties:
            link: '"https://console.aws.amazon.com/go/view?arn=" + .StackId'
            arn: .StackId
            kind: .__Kind
            region: .__Region
          relations:
            account: .__AccountId
  - kind: AWS::AutoScaling::AutoScalingGroup
    selector:
      query: 'true'
      useGetResourceAPI: 'true'
    port:
      entity:
        mappings:
          identifier: .Identifier
          title: .Properties.AutoScalingGroupName
          blueprint: '"autoScalingGroup"'
          properties:
            link: >-
                'https://console.aws.amazon.com/ec2/home?region=' +
                .__Region + '#AutoScalingGroupDetails:id=' +
                .Properties.AutoScalingGroupName + ';view=details'
            desiredCapacity: .Properties.DesiredCapacity
            minSize: .Properties.MinSize
            maxSize: .Properties.MaxSize
            arn: .Properties.AutoScalingGroupARN
            role: >-
                'https://console.aws.amazon.com/go/view?arn=' +
                .Properties.ServiceLinkedRoleARN
            kind: .__Kind
            region: .__Region
          relations:
            account: .__AccountId
```

### Networking and content delivery blueprint and configuration example[â](#networking-and-content-delivery-blueprint-and-configuration-example "Direct link to Networking and content delivery blueprint and configuration example")

CloudFront Distribution Blueprint

Create in Port

```
{
  "identifier": "cloudFrontDistribution",
  "description": "This blueprint represents an AWS CloudFront Distribution in our software catalog",
  "title": "CloudFront Distribution",
  "icon": "AWS",
  "schema": {
    "properties": {
      "link": {
        "type": "string",
        "format": "url",
        "title": "Link"
      },
      "status": {
        "type": "string",
        "title": "Status"
      },
      "domainName": {
        "type": "string",
        "title": "Domain Name"
      },
      "lastModifiedTime": {
        "type": "string",
        "format": "date-time",
        "title": "Last Modified Time"
      },
      "allowedMethods": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "title": "Allowed Methods"
      },
      "originDomainNames": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "title": "Origin Domain Names"
      },
      "originIds": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "title": "Origin IDs"
      },
      "enabled": {
        "type": "boolean",
        "title": "Enabled"
      },
      "isIpv6Enabled": {
        "type": "boolean",
        "title": "IPv6 Enabled"
      },
      "httpVersion": {
        "type": "string",
        "title": "HTTP Version"
      },
      "isStaging": {
        "type": "boolean",
        "title": "Is Staging"
      },
      "kind": {
        "type": "string",
        "title": "Kind"
      },
      "region": {
        "type": "string",
        "title": "Region"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {
    "account": {
      "title": "Account",
      "target": "awsAccount",
      "required": true,
      "many": false
    }
  }
}
```

Mapping Configuration for CloudFront Distribution

```
resources:
  - kind: AWS::CloudFront::Distribution
    selector:
      query: 'true'
      useGetResourceAPI: 'true'
    port:
      entity:
        mappings:
          identifier: .Identifier
          title: .Properties.DomainName
          blueprint: '"cloudFrontDistribution"'
          properties:
            link: >-
                'https://console.aws.amazon.com/cloudfront/home?region=' +
                .__Region + '#/distribution/' +
                .Properties.Id
            status: .Properties.Status
            domainName: .Properties.DomainName
            lastModifiedTime: .Properties.LastModifiedTime
            allowedMethods: .Properties.DefaultCacheBehavior.AllowedMethods
            originDomainNames: .Properties.Origins[].DomainName
            originIds: .Properties.Origins[].Id
            enabled: .Properties.Enabled
            isIpv6Enabled: .Properties.IPV6Enabled
            httpVersion: .Properties.HttpVersion
            isStaging: .Properties.Staging
            kind: .__Kind
            region: .__Region
          relations:
            account: .__AccountId
```

### Security, identity, and compliance blueprint and configuration example[â](#security-identity-and-compliance-blueprint-and-configuration-example "Direct link to Security, identity, and compliance blueprint and configuration example")

Cognito User Pool Blueprint

Create in Port

```
{
  "identifier": "cognitoUserPool",
  "description": "This blueprint represents an AWS Cognito User Pool in our software catalog",
  "title": "Cognito User Pool",
  "icon": "AWS",
  "schema": {
    "properties": {
      "link": {
        "type": "string",
        "format": "url",
        "title": "Link"
      },
      "arn": {
        "type": "string",
        "title": "ARN"
      },
      "userPoolId": {
        "type": "string",
        "title": "User Pool ID"
      },
      "providerName": {
        "type": "string",
        "title": "Provider Name"
      },
      "status": {
        "type": "string",
        "title": "Status"
      },
      "creationDate": {
        "type": "string",
        "format": "date-time",
        "title": "Creation Date"
      },
      "mfaConfiguration": {
        "type": "string",
        "title": "MFA Configuration"
      },
      "kind": {
        "type": "string",
        "title": "Kind"
      },
      "region": {
        "type": "string",
        "title": "Region"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {
    "account": {
      "title": "Account",
      "target": "awsAccount",
      "required": true,
      "many": false
    }
  }
}
```

Mapping Configuration for Cognito User Pool

```
resources:
  - kind: AWS::Cognito::UserPool
    selector:
      query: 'true'
      useGetResourceAPI: 'true'
    port:
      entity:
        mappings:
          identifier: .Identifier
          title: .Properties.UserPoolName
          blueprint: '"cognitoUserPool"'
          properties:
            link: >-
                'https://console.aws.amazon.com/go/view?arn=' +
                .Properties.Arn
            arn: .Properties.Arn
            userPoolId: .Properties.UserPoolId
            providerName: .Properties.ProviderName
            status: .Properties.Status
            creationDate: .Properties.CreationDate
            mfaConfiguration: .Properties.MfaConfiguration
            kind: .__Kind
            region: .__Region
          relations:
            account: .__AccountId
```

### Storage blueprint and configuration example[â](#storage-blueprint-and-configuration-example "Direct link to Storage blueprint and configuration example")

DynamoDB Table Blueprint

Create in Port

```
{
  "identifier": "dynamoDBTable",
  "description": "This blueprint represents an AWS DynamoDB Table in our software catalog",
  "title": "DynamoDB Table",
  "icon": "AWS",
  "schema": {
    "properties": {
      "link": {
        "type": "string",
        "format": "url",
        "title": "Link"
      },
      "tableStatus": {
        "type": "string",
        "title": "Table Status"
      },
      "itemCount": {
        "type": "number",
        "title": "Item Count"
      },
      "creationDateTime": {
        "type": "string",
        "format": "date-time",
        "title": "Creation Date Time"
      },
      "billingMode": {
        "type": "string",
        "title": "Billing Mode"
      },
      "writeCapacityUnits": {
        "type": "number",
        "title": "Write Capacity Units"
      },
      "readCapacityUnits": {
        "type": "number",
        "title": "Read Capacity Units"
      },
      "timeToLive": {
        "type": "boolean",
        "title": "Time to Live"
      },
      "pointInTimeRecovery": {
        "type": "boolean",
        "title": "Point in Time Recovery"
      },
      "deletionProtection": {
        "type": "boolean",
        "title": "Deletion Protection"
      },
      "arn": {
        "type": "string",
        "title": "ARN"
      },
      "kind": {
        "type": "string",
        "title": "Kind"
      },
      "region": {
        "type": "string",
        "title": "Region"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {
    "account": {
      "title": "Account",
      "target": "awsAccount",
      "required": true,
      "many": false
    }
  }
}
```

ElastiCache Serverless Cache Blueprint

Create in Port

```
{
  "identifier": "elasticacheServerless",
  "description": "This blueprint represents an AWS ElastiCache Serverless Cache in our software catalog",
  "title": "ElastiCache Serverless Cache",
  "icon": "AWS",
  "schema": {
    "properties": {
      "link": {
        "type": "string",
        "format": "url",
        "title": "Link"
      },
      "engine": {
        "type": "string",
        "title": "Engine"
      },
      "engineVersion": {
        "type": "string",
        "title": "Full Engine Version"
      },
      "status": {
        "type": "string",
        "title": "Status"
      },
      "description": {
        "type": "string",
        "title": "Description"
      },
      "createTime": {
        "type": "string",
        "format": "date-time",
        "title": "Create Time"
      },
      "securityGroupIds": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "title": "Security Group IDs"
      },
      "subnetIds": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "title": "Subnet IDs"
      },
      "endpoint": {
        "type": "string",
        "title": "Endpoint"
      },
      "port": {
        "type": "number",
        "title": "Port"
      },
      "readerEndpoint": {
        "type": "string",
        "title": "Reader Endpoint"
      },
      "readerPort": {
        "type": "number",
        "title": "Reader Port"
      },
      "dailySnapshotTime": {
        "type": "string",
        "title": "Daily Snapshot Time"
      },
      "snapshotRetentionLimit": {
        "type": "number",
        "title": "Snapshot Retention Limit"
      },
      "serverlessCacheName": {
        "type": "string",
        "title": "Serverless Cache Name"
      },
      "arn": {
        "type": "string",
        "title": "ARN"
      },
      "kind": {
        "type": "string",
        "title": "Kind"
      },
      "region": {
        "type": "string",
        "title": "Region"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {
    "account": {
      "title": "Account",
      "target": "awsAccount",
      "required": true,
      "many": false
    }
  }
}
```

RDS Instance Blueprint

Create in Port

```
{
  "identifier": "rdsInstance",
  "description": "This blueprint represents an AWS RDS DBInstance in our software catalog",
  "title": "RDS Instance",
  "icon": "AWS",
  "schema": {
    "properties": {
      "link": {
        "type": "string",
        "format": "url",
        "title": "Link"
      },
      "dbInstanceClass": {
        "type": "string",
        "title": "DB Instance Class"
      },
      "dbInstanceStatus": {
        "type": "string",
        "title": "DB Instance Status"
      },
      "engine": {
        "type": "string",
        "title": "Engine"
      },
      "storageType": {
        "type": "string",
        "title": "Storage Type"
      },
      "engineVersion": {
        "type": "string",
        "title": "Engine Version"
      },
      "port": {
        "type": "number",
        "title": "Port"
      },
      "allocatedStorage": {
        "type": "number",
        "title": "Allocated Storage"
      },
      "endpoint": {
        "type": "string",
        "title": "Endpoint"
      },
      "multiAZ": {
        "type": "boolean",
        "title": "Multi-AZ"
      },
      "deletionProtection": {
        "type": "boolean",
        "title": "Deletion Protection"
      },
      "availabilityZone": {
        "type": "string",
        "title": "Availability Zone"
      },
      "masterUsername": {
        "type": "string",
        "title": "Master Username"
      },
      "publicAccess": {
        "type": "boolean",
        "title": "Public Access"
      },
      "vpcSecurityGroups": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "title": "VPC Security Groups"
      },
      "arn": {
        "type": "string",
        "title": "ARN"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {
    "account": {
      "title": "Account",
      "target": "awsAccount",
      "required": true,
      "many": false
    }
  }
}
```

Mapping Configuration for RDS Instance, ElastiCache, DynamoDB Table

```
resources:
  - kind: AWS::RDS::DBInstance
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .Identifier
          title: .Properties.DBInstanceIdentifier
          blueprint: '"rdsInstance"'
          properties:
            link: >-
               'https://console.aws.amazon.com/go/view?arn=' +
               .Properties.DBInstanceArn
            dbInstanceClass: .Properties.DBInstanceClass
            dbInstanceStatus: .Properties.DBInstanceStatus
            engine: .Properties.Engine
            storageType: .Properties.StorageType
            engineVersion: .Properties.EngineVersion
            port: .Properties.Endpoint.Port
            allocatedStorage: .Properties.AllocatedStorage
            endpoint: .Properties.Endpoint.Address
            multiAZ: .Properties.MultiAZ
            deletionProtection: .Properties.DeletionProtection
            availabilityZone: .Properties.AvailabilityZone
            masterUsername: .Properties.MasterUsername
            publicAccess: .Properties.PubliclyAccessible
            vpcSecurityGroups: .Properties.VpcSecurityGroups
            arn: .Properties.DBInstanceArn
          relations:
            account: .__AccountId
  - kind: AWS::DynamoDB::Table
    selector:
      query: 'true'
      useGetResourceAPI: 'true'
    port:
      entity:
        mappings:
          identifier: .Identifier
          title: .Properties.TableName
          blueprint: '"dynamoDBTable"'
          properties:
            link: >-
                'https://console.aws.amazon.com/go/view?arn=' +
                .Properties.Arn
            tableStatus: .Properties.TableStatus
            itemCount: .Properties.ItemCount
            creationDateTime: .Properties.CreationDateTime
            billingMode: .Properties.BillingMode
            writeCapacityUnits: .Properties.ProvisionedThroughput.WriteCapacityUnits
            readCapacityUnits: .Properties.ProvisionedThroughput.ReadCapacityUnits
            timeToLive: .Properties.TimeToLiveSpecification.Enabled
            pointInTimeRecovery: .Properties.PointInTimeRecoverySpecification.PointInTimeRecoveryEnabled
            deletionProtection: .Properties.DeletionProtectionEnabled
            arn: .Properties.Arn
            kind: .__Kind
            region: .__Region
          relations:
            account: .__AccountId
  - kind: AWS::ElastiCache::ServerlessCache
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .Identifier
          title: .Properties.ServerlessCacheName
          blueprint: '"elasticacheServerless"'
          properties:
            link: >-
                'https://console.aws.amazon.com/go/view?arn=' +
                .Properties.ARN
            engine: .Properties.Engine
            engineVersion: .Properties.FullEngineVersion
            status: .Properties.Status
            description: .Properties.Description
            createTime: .Properties.CreateTime
            securityGroupIds: .Properties.SecurityGroupIds
            subnetIds: .Properties.SubnetIds
            endpoint: .Properties.Endpoint.Address
            port: .Properties.Endpoint.Port
            readerEndpoint: .Properties.ReaderEndpoint.Address
            readerPort: .Properties.ReaderEndpoint.Port
            dailySnapshotTime: .Properties.DailySnapshotTime
            snapshotRetentionLimit: .Properties.SnapshotRetentionLimit
            serverlessCacheName: .Properties.ServerlessCacheName
            arn: .Properties.ARN
            kind: .__Kind
            region: .__Region
          relations:
            account: .__AccountId
```

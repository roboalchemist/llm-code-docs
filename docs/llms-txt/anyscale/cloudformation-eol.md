# Source: https://docs.anyscale.com/services/cloudformation-eol.md

# Update your IAM role for services on Anyscale clouds on AWS

[View Markdown](/services/cloudformation-eol.md)

# Update your IAM role for services on Anyscale clouds on AWS

This page provides an overview of new default behavior for deploying services on Anyscale clouds on AWS, a description of the legacy infrastructure, instructions for migrating, and details on the end-of-life (EOL) for legacy support for CloudFormation.

important

If you deployed your Anyscale cloud on AWS after August 11, 2025, your cloud deployment should have the correct IAM permissions by default.

You must use the Anyscale CLI version 0.26.33 or later to deploy or update an Anyscale cloud with the correct IAM permissions for services using either `anyscale cloud setup` or `anyscale cloud update`.

When deploying a custom Anyscale cloud on AWS using `anyscale cloud register`, you control the IAM permissions. Anyscale provides the minimum IAM permissions required to support services. See [Update IAM roles for a custom cloud deployment](#register).

## EOL for services with CloudFormation is February 11, 2026[​](#eol "Direct link to EOL for services with CloudFormation is February 11, 2026")

Legacy Anyscale clouds deployed on AWS used CloudFormation to configure Elastic Load Balancing resources when deploying Anyscale services. This pattern requires a set of IAM permissions that allow the Anyscale control plane to use CloudFormation and for CloudFormation to configure Elastic Load Balancing. These IAM permissions no longer fulfill the requirements for deploying Anyscale services in the new control plane architecture.

Anyscale used the legacy IAM roles when deploying clouds with `anyscale cloud setup`, and all instructions and Terraform modules guided users toward the legacy IAM roles when using `anyscale cloud register`.

You must update the IAM roles for your Anyscale cloud on AWS to continue using services. Once you update your IAM permissions, Anyscale uses the new process for deploying services in your cloud.

## Benefits to migration[​](#benefits "Direct link to Benefits to migration")

Removing CloudFormation from the Anyscale services deployment removes limitations around increasing the number of services that a single Anyscale cloud can support and improves reliability and stability during service deployment.

Migration doesn't interrupt your production services. Anyscale deploys a new Application Load Balancer for your services and switches over the DNS automatically.

During the migration, Anyscale keeps the load balancing resources deployed by CloudFormation available and rolls the migration back in case of failure.

## Migration details for the Anyscale control plane IAM permissions[​](#migration-details "Direct link to Migration details for the Anyscale control plane IAM permissions")

The following are the key updates to the IAM permissions:

* The Anyscale control plane needs permission to describe tags for Elastic Load Balancing.

  You must add the following permission to your control plane role:

  ```
  "elasticloadbalancing:DescribeTags"
  ```

* The Anyscale control plane directly interacts with Elastic Load Balancing instead of going through CloudFormation.

  You must remove the following condition from your control plane role:

  ```
  "Condition": {
    "StringEquals": {"aws:CalledViaFirst": "cloudformation.amazonaws.com"}
  },
  ```

The Anyscale Terraform provider scripts model further locking down permissions. See [Update IAM roles for a custom cloud deployment](#register).

Contact [Anyscale support](mailto:support@anyscale.com) with questions or concerns.

## Update IAM roles for a default cloud deployment[​](#update-default "Direct link to Update IAM roles for a default cloud deployment")

If you deployed your Anyscale cloud on AWS using the default deployment with `anyscale cloud setup`, you can upgrade to the new IAM permissions by running the following command:

```
anyscale cloud update
```

## Update IAM roles for a custom cloud deployment[​](#register "Direct link to Update IAM roles for a custom cloud deployment")

If you deployed your Anyscale cloud on AWS using a custom deployment with `anyscale cloud register`, you can upgrade to the new IAM permissions by modifying your IAM roles in your AWS account or running [Anyscale-provided Terraform modules](https://github.com/anyscale/terraform-aws-anyscale-cloudfoundation-modules).

The variable `anyscale_servicesv2_create_elb_service_linked_role` controls permissions tied to Anyscale services. Contact [Anyscale support](mailto:support@anyscale.com) for help customizing and running the scripts to scope IAM permissions as narrowly as possible.

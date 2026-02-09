# Source: https://docs.datadoghq.com/security/default_rules/rrv-fo1-7oh.md

---
title: ElastiCache clusters should be provisioned in a VPC
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > ElastiCache clusters should be
  provisioned in a VPC
---

# ElastiCache clusters should be provisioned in a VPC
 
## Description{% #description %}

Provision your AWS EC2-VPC ElastiCache cluster within the AWS ECS-VPC platform.

## Rationale{% #rationale %}

Using the EC2-Classic platform minimizes control over cache cluster security and traffic routing. Provisioning with AWS EC2-VPC enables better networking infrastructure, control over VPC security groups, and more.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the [Getting started with Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-getting-started.html) docs to configure AWS EC2-VPC for your ElastiCache clusters.

### From the command line{% #from-the-command-line %}

1. Run `create-vpc` to [create a new Virtual Private Cloud (VPC)](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-vpc.html#synopsis) for your ElastiCache cluster.

In the `create-vpc.sh` file:

```bash
  aws ec2 create-vpc
      --cidr-block 10.0.0.0/16
  
```

Run `aws ec2 create-internet-gateway` to [create a new AWS Internet Gateway](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-internet-gateway.html#synopsis) for your new VPC.

Run `attach-internet-gateway` with the [VPC ID returned in step 1, and the internet gateway ID returned in step 2](https://docs.aws.amazon.com/cli/latest/reference/ec2/attach-internet-gateway.html#synopsis).

In the `create-subnet.sh` file:

```bash
  aws ec2 create-subnet
      --vpc-id vpc-ab12c345
      --cidr-block 10.0.1.0/24
  
```
Run `create-route-table` with [your VPC ID](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-route-table.html#synopsis) created in step 1.
In the `create-route-table.sh` file:

```bash
  aws ec2 create-route-table
      --vpc-id vpc-ab12c345
  
```
Run `associated-route-table` with the [subnet ID returned in step 3, and the route table ID returned in step 4](https://docs.aws.amazon.com/cli/latest/reference/ec2/associate-route-table.html#synopsis).
In the `associate-route-table.sh` file:

```bash
  aws ec2 associate-route-table
    --route-table-id rta-12345678
    --subnet-id subnet-ab123c45
  
```
Run `create-route` to [add a new route](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-route.html#synopsis) to your new VPC route table.
In the `create-route.sh` file:

```bash
  aws ec2 create-route
    --route-table-id rta-12345678
    --destination-cidr-block 0.0.0.0/0
    --gateway-id gwi-123a4b56
  
```
Run `create-security-group` with your new VPC ID to [create a security group](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-security-group.html#synopsis) for your new cluster.
In the `create-security-group.sh` file:

```bash
  aws ec2 create-security-group
    --group-name ECSecurityGroup
    --description "Redis CC Security Group"
    --vpc-id vpc-ab12c345
  
```
Run `authorize-security-group-ingress` to [add more inbound rules](https://docs.aws.amazon.com/cli/latest/reference/ec2/authorize-security-group-ingress.html#synopsis) to the security group created in step 7.
In the `authorize-security-group-ingress.sh` file:

```bash
  aws ec2 authorize-security-group-ingress
    --group-id se-a12345b0
    --protocol tcp
    --port 1234
    --cidr 10.0.0.0/16
  
```
Run `create-cache-cluster` to recreate your EC2-Classic cache cluster within your new AWS VPC. Use the newly created [ElastiCache cluster configuration attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/create-cache-cluster.html#synopsis) returned in the steps above.
In the `create-cache-cluster.sh` file:

```bash
  aws elasticache create-cache-cluster
    --cache-cluster-id vpccachecluster
    --az-mode single-az
    --cache-node-type cache.m5.large
    --num-cache-nodes 1
    --engine redis
    --engine-version "2.6.13"
    --security-group-ids "se-a12345b0"
    --port 1234
    --auto-minor-version-upgrade
  
```

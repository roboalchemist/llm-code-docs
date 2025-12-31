# Source: https://planetscale.com/docs/vitess/managed/aws/reverse-privatelink.md

# Set up AWS Reverse PrivateLink with PlanetScale Managed

> [PlanetScale Managed](/docs/vitess/managed/aws) can connect to your existing databases via AWS PrivateLink for the purposes of data imports.

Often, one of the first tasks for a new Managed deployment is to import data from an existing MySQL database housed in a separate AWS Organizations member account.

This guide explains how to set up AWS PrivateLink components that enable cross-account communication to facilitate this process. In PrivateLink parlance, the MySQL database that serves as the import source is known as the "producer", and PlanetScale is the "consumer".

While there are a number of different ways to set up and configure PrivateLink components, in this guide we'll be using the AWS CLI tool.

## How PlanetScale Managed and AWS PrivateLink work

Broadly speaking, there are three major components to this PrivateLink setup:

* A [VPC Endpoint Service](https://docs.aws.amazon.com/vpc/latest/privatelink/endpoint-service-overview.html) conceptually lives in the producer's VPC and AWS account. Once configured, it allows authorized principals (e.g. AWS accounts, IAM users) to establish a connection to an existing VPC Endpoint Service ID.

* A [VPC Endpoint Interface](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html) exists on the consumer side, and once configured with an endpoint service address exposes an internal IP address and port which consumers may use for cross-account communication.

* A [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) (NLB) is created on the producer side, and by managing the IP target group on this NLB you can choose which internal services to expose via the PrivateLink Endpoint Service.

## Starting state

Below is a simplified diagram of our initial state. We've got two separate accounts, each with their own VPCs and availability zones. We're using AWS [AZ IDs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#az-ids) as well as of AZ names to ensure that we're always referring to the correct AZ, as AZ names are not consistent across AWS accounts. On the producer side, we have a network subnet inside each AZ.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/starting-state.png?fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=5deee8a67f89d51fa74135640d3bbe9a" alt="starting state" data-og-width="1488" width="1488" data-og-height="1478" height="1478" data-path="docs/images/assets/docs/managed/aws/privatelink/starting-state.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/starting-state.png?w=280&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=00a77eb5a5fc95c2e68b2de6e0db73da 280w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/starting-state.png?w=560&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=b9500773b6bc70c6159f9344ce919de3 560w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/starting-state.png?w=840&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=e213ec13620b59b9f60f82244a8bdb14 840w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/starting-state.png?w=1100&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=f11e87eaae534618eb57eb53aeb79338 1100w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/starting-state.png?w=1650&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=ee9b65ee2504663086851148f5856894 1650w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/starting-state.png?w=2500&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=5de25c745ba323f49369f419a442dc88 2500w" />
</Frame>

## Create and configure the NLB

First, create the Network Load Balancer in the producer AWS account. You want the NLB to be available in each of the three AZs that the two accounts share. This is done by adding the ids of the three subnets associated with those AZs using the `--subnets` option.

```bash  theme={null}
aws elbv2 create-load-balancer \
  --name pl-nlb \
  --scheme internal \
  --type network \
  --subnets subnet-cafed00d subnet-c0ffee subnet-cafef00d
  --security-groups sg-f00
```

If you want to attach a security group to your NLB, you must do so at creation time. This allows you to restrict the inbound protocol and port range to `TCP:3306`. This command will return an ARN that uniquely identifies the newly created NLB. You'll need this later.

### Create an IP target group

Run the following to create an empty IP target group on `TCP:3306` in the producer VPC:

```bash  theme={null}
aws elbv2 create-target-group \
  --name pl-nlb-target-group \
  --protocol TCP \
  --port 3306 \
  --vpc-id vpc-f00 \
  --target-type ip
```

This will return an ARN that uniquely identifies the target group.

### Register a target

This step adds the IP address of the existing Primary RDS instance to the target group. You want to make sure that only the RDS writer is registered as a target.

```bash  theme={null}
aws elbv2 register-targets \
  --target-group-arn <arn>
  --targets Id=10.0.0.1
```

### Create a listener

Finally, associate the target group NLB by creating a listener.

```bash  theme={null}
aws elbv2 create-listener \
   --load-balancer-arn <arn>\
   --protocol TCP \
   --port 3306 \
   --default-actions Type=forward,TargetGroupArn=<arn>
```

Now that you've created the NLB and configured it, you can add the NLB to the diagram. Although on the diagram it looks like there are three separate NLBs, it's meant to represent a single NLB object that has network interfaces in three different subnets.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/create-and-configure-nlb.png?fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=112c3d0ba385b85f81533d16c84c30ff" alt="create and configure nlb" data-og-width="1752" width="1752" data-og-height="1630" height="1630" data-path="docs/images/assets/docs/managed/aws/privatelink/create-and-configure-nlb.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/create-and-configure-nlb.png?w=280&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=976c99c5481760e33889dc382e889689 280w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/create-and-configure-nlb.png?w=560&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=2a4ad955209557756fbdfc6aaf9ca922 560w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/create-and-configure-nlb.png?w=840&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=b4ed0378ff16f03c08f48813d1228374 840w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/create-and-configure-nlb.png?w=1100&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=d4d06f6f4b9ecf1a8ea9765b8a587a92 1100w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/create-and-configure-nlb.png?w=1650&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=1c1243a4da82e114b7cab71e6e8e1da6 1650w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/create-and-configure-nlb.png?w=2500&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=a1a9dc6424e909834d34753ca1afcd4c 2500w" />
</Frame>

## Create and configure the PrivateLink VPC Endpoint Service

Now, let's configure the endpoint service. You'll need the ARN of your load balancer for this.

```bash  theme={null}
aws ec2 create-vpc-endpoint-service-configuration \
  --network-load-balancer-arn <arn> \
  --no-acceptance-required
```

This will return a VPC service id.

## Allow inbound traffic from VPC's subnet

After setting up the NLB and the VPC Endpoint Service, you need to ensure that the security group attached to the NLB permits inbound traffic from the subnet(s) of the consumer VPC where the interface VPC endpoint resides.

<Steps>
  <Step>
    Locate the security group associated with your NLB
  </Step>

  <Step>
    Edit Inbound Rules:

    * Protocol: TCP
    * Port Range: Specify the port your MySQL database is listening on (default is 3306)
    * Source: Enter the CIDR block of the consumer VPC's subnet (e.g., 10.0.1.0/24)
  </Step>

  <Step>
    Save changes to apply the updated rules
  </Step>
</Steps>

### Configure service permissions

You only want to allow incoming connections on this endpoint service from the PlanetScale Managed AWS Organizations member account. This step requires the account number.

```bash  theme={null}
aws ec2 modify-vpc-endpoint-service-permissions \
  --service-id vpce-svc-f00 \
  --add-allowed-principals '["arn:aws:iam::123456789012:root"]'
```

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/create-and-configure-vpce-svc.png?fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=39abee3e37dd45e21badebdda42c98e2" alt="create and configure vpce svc" data-og-width="2102" width="2102" data-og-height="1630" height="1630" data-path="docs/images/assets/docs/managed/aws/privatelink/create-and-configure-vpce-svc.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/create-and-configure-vpce-svc.png?w=280&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=82bb056ccc1767ef869bb714cd3985e2 280w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/create-and-configure-vpce-svc.png?w=560&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=ec2505a1ac59a309b1ae84c6c6d935cf 560w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/create-and-configure-vpce-svc.png?w=840&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=794a182c9d5b9aed881a900e1bcc1017 840w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/create-and-configure-vpce-svc.png?w=1100&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=5db59c752c91a658f5c54af37b8c82e7 1100w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/create-and-configure-vpce-svc.png?w=1650&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=9c23e06ded7ceb964dfd70d692d2c0d8 1650w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/create-and-configure-vpce-svc.png?w=2500&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=2480fbcaf1f5af77cbcac722abd076b0 2500w" />
</Frame>

## Wrapping Up

Once you've communicated your newly created VPC Service Endpoint ID to your Solutions Engineer, the PlanetScale Engineering team can then complete the rest of the process. This involves creating, configuring, and testing the PrivateLink VPC Interface Endpoint. The diagram below illustrates the completed system.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/wrapping-up.png?fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=4d12fa0711cc37762b0b6f03760e6318" alt="wrapping up" data-og-width="2470" width="2470" data-og-height="2218" height="2218" data-path="docs/images/assets/docs/managed/aws/privatelink/wrapping-up.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/wrapping-up.png?w=280&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=13a870bfd4efbf456aab6d158c516ee5 280w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/wrapping-up.png?w=560&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=bdf7d9967162ded1ddf9a0128fe7693f 560w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/wrapping-up.png?w=840&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=db83ddf96c82de2b0ea979c79974909e 840w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/wrapping-up.png?w=1100&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=25caca1dc84219490dd2f5bcde43d8d0 1100w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/wrapping-up.png?w=1650&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=ba3eb7f4b549a4a2983b104bec8af01d 1650w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/wrapping-up.png?w=2500&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=3943c1f3dc0261b433a5cc8f0f1c68e0 2500w" />
</Frame>

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt
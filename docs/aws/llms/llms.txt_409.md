# Source: https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/llms.txt

#  FleetIQ Developer Guide

> Learn how to use Amazon GameLift ServersÂ FleetIQ with Amazon EC2 Spot Instances to set up cost-efficient game hosting in the cloud. With Amazon GameLift ServersÂ FleetIQ as a standalone solution, you can use Amazon GameLift Servers game hosting with your existing cloud-based or on-premises systems.

- [Monitor with CloudWatch](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-metrics.html)
- [Security with FleetIQ](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-security.html)
- [AWS Glossary](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/glossary.html)

## [What is Amazon GameLift ServersÂ FleetIQ?](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-intro.html)

### [How FleetIQ works](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-howitworks.html)

Learn about how you can optimize Amazon EC2 Spot Instances for game hosting with Amazon GameLift Servers FleetIQ.

- [Amazon GameLift ServersÂ FleetIQ logic](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-howitworks-logic.html): The following diagram illustrates the role of Amazon GameLift ServersÂ FleetIQ when it is working with Amazon EC2 for game hosting.
- [Key resources and components](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-howitworks-resources.html): Create the following resources in your AWS account before you set up your game hosting resources with Amazon GameLift ServersÂ FleetIQ.
- [Game architecture](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-architecture.html): Learn about game architecture options with Amazon GameLift ServersÂ FleetIQ.
- [Life of a game server group](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-howitworks-lifecycle-gameservergroup.html): Game server groups go through the following life cycle, including provisioning and status updates.
- [Life of a game server](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-howitworks-lifecycle-gameserver.html): With Amazon GameLift ServersÂ FleetIQ, game servers go through the following life cycle, including provisioning and status updates.
- [Spot balancing process](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-lifecycle-rebalance.html): Amazon GameLift ServersÂ FleetIQ periodically balances the instances in an Auto Scaling group that has Spot Instances.
- [Best practices](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-best-practices.html): Get tips and best practices for setting up game hosting on Amazon EC2 Spot Instances.


## [Setting Up](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-setting-up.html)

- [Supported software](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-supported.html): Learn how Amazon GameLift ServersÂ FleetIQ can support your games.

### [Set up your AWS account](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-iam-permissions.html)

Learn about AWS account settings and user permissions required to work with Amazon GameLift Servers FleetIQ.

- [Create an AWS account](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-iam-permissions-account.html): Create an account and set up an administrative user for Amazon GameLift Servers FleetIQ.

### [Manage user permissions for Amazon GameLift ServersÂ FleetIQ](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-iam-permissions-users.html)

Set user and user group permissions for Amazon GameLift ServersÂ FleetIQ.

- [Reference: Amazon GameLift ServersÂ FleetIQ_policy](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-iam-permissions-users-policy.html): The following is an example of the Amazon GameLift ServersÂ FleetIQ_policy for your reference:
- [Additional permissions for CloudFormation](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-iam-permissions-users-policycfn.html): If you use CloudFormationto manage your game hosting resources, add the CloudFormation permissions to the policy syntax.
- [Set up programmatic access for users](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-iam-permissions-users-access-keys.html): Users need programmatic access if they want to interact with AWS outside of the AWS Management Console.

### [Create IAM roles for cross-service interaction](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-iam-permissions-roles.html)

Create IAM service roles with cross-service permissions that are required for Amazon GameLift Servers FleetIQ.

- [Create a role for Amazon GameLift ServersÂ FleetIQ](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-iam-permissions-roles-gamelift.html): This role allows Amazon GameLift ServersÂ FleetIQ to access and modify your Amazon EC2 instances, Auto Scaling groups, and lifecycle hooks as part of its Spot balancing and automatic scaling activities.
- [Create a role for Amazon EC2](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-iam-permissions-roles-ec2.html): This role enables your Amazon EC2 resources to communicate with Amazon GameLift ServersÂ FleetIQ.


## [Preparing games for FleetIQ](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-integration-intro.html)

- [Integration steps](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-getting-started.html): Set up Amazon GameLift ServersÂ FleetIQ optimizations when hosting games on Amazon EC2 with Spot Instances.

### [Manage game server groups](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-integrate-gameservergroup.html)

Learn to create and update your Amazon GameLift ServersÂ FleetIQ game server groups.

- [Create a game server group](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-integrate-gameservergroup-create.html): To create a game server group, call CreateGameServerGroup().
- [Update a game server group](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-integrate-gameservergroup-update.html): You can update game server group properties that affect how Amazon GameLift ServersÂ FleetIQ manages hosting for game servers, including resource type optimizations.
- [Track game server group instances](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-integrate-gameservergroup-track.html): After you create and deploy instances to your game server group and Auto Scaling group, you can track the status of game server instances by calling DescribeGameServerInstances().

### [Integrate a game server](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-integrate-gameserver.html)

Learn about how to enable your game server to communicate with Amazon GameLift ServersÂ FleetIQ.

- [Register game servers](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-integrate-gameserver-register.html): When a game server process is launched and ready to host live gameplay, it must register with Amazon GameLift ServersÂ FleetIQ by calling RegisterGameServer().
- [Update game server status](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-integrate-gameserver-update.html): Once a game server is registered, it should regularly report health and utilization status in order to keep the state of server capacity in sync on Amazon GameLift ServersÂ FleetIQ.
- [Deregister game servers](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-integrate-gameserver-deregister.html): When a game concludes, the game server must deregister from Amazon GameLift ServersÂ FleetIQ using DeregisterGameServer().

### [Integrate a Game Client](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-integrate-gameclient.html)

Learn how to set up your game client to request a game server with Amazon GameLift ServersÂ FleetIQ.

- [Let Amazon GameLift ServersÂ FleetIQ choose a game server](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-integrate-gameclient-automatic.html): To have Amazon GameLift ServersÂ FleetIQ choose an available game server, call ClaimGameServer() without specifying a game server ID.
- [Choose your own game server](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-integrate-gameclient-optimized.html): With the "list and pick" method, your game client or matchmaker requests a list of available game servers by calling ListGameServers().


## [Amazon GameLift ServersÂ FleetIQ reference](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-reference-intro.html)

### [Service API reference (AWS SDK)](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/reference-awssdk-fleetiq.html)

View a task-based listing of the Amazon GameLift Servers FleetIQ API operations in the AWS SDK.

- [Amazon GameLift ServersÂ FleetIQ API actions](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/reference-awssdk-fleetiq-api.html): The following operations allow you to manage your Amazon GameLift ServersÂ FleetIQ resources, including game server groups and game servers, in conjunction with Amazon EC2 and Auto Scaling groups.
- [Available programming languages](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/reference-awssdk-langlist.html): The AWS SDK with support for Amazon GameLift Servers is available in the following languages.
- [Release notes and SDK versions](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-release-notes.html): View SDK version history and release notes for Amazon GameLift Servers FleetIQ.
- [All Amazon GameLift Servers guides](https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-guides.html): View all Amazon GameLift Servers developer resources.

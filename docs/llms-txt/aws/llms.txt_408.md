# Source: https://docs.aws.amazon.com/gameliftservers/latest/developerguide/llms.txt

#  Hosting Guide

> Describes key concepts of Amazon GameLift Servers and its features, including FlexMatch matchmaking, Amazon GameLift ServersÂ Realtime for standing up lightweight servers, and FleetIQ optimizations to lower hosting costs. Provides guidance on integrating and deploying your game with Amazon GameLift Servers.

- [Release notes and SDK versions](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/release-notes.html)

## [What is Amazon GameLift Servers?](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-intro.html)

- [Game hosting options](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-intro-flavors.html): Learn about how Amazon GameLift Servers can help you build a hosting solution for your session-based, multiplayer games.
- [How it works](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-howitworks.html): Learn about the core components of a complete Amazon GameLift Servers hosting solution and how they work together to deliver multiplayer game sessions to players.
- [Player experience](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/game-sessions-intro.html): Learn how Amazon GameLift Servers features directly enhance multiplayer gaming experiences by providing fast, fair, and reliable gameplay for players worldwide.
- [Game hosting in production](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-prod-hosting.html): Find tools and resources for managing a game hosting system that uses Amazon GameLift Servers to run game servers and manage game session management and player placement.
- [Key terms](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-key-terms.html): Key technical terms and definitions for Amazon GameLift Servers features and concepts.


## [Getting started](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/getting-started-intro.html)

### [Set up an AWS account](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/setting-up-aws-login.html)

To use Amazon GameLift Servers, you need to have an AWS account user with permissions to use the Amazon GameLift Servers service.

- [IAM permission examples](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-iam-policy-examples.html): Use these permission syntax examples to manage user access for Amazon GameLift Servers.
- [Set up an IAM service role](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/setting-up-role.html): Learn how to set up an IAM role to grant Amazon GameLift Servers limited access to your AWS resources.
- [Get development tools](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-supported.html): Find tools and resources for developing multiplayer game hosting solution, including support for programming languages, game engines, and game operating systems.
- [Tutorial: Quick onboarding with the Amazon GameLift Servers wrapper](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-wrapper-tutorial.html): Learn how to rapidly deploy your game server using the Amazon GameLift Servers wrapper for quick hosting without SDK integration.
- [Amazon GameLift Servers examples](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/getting-started-examples.html): Learn how to get started with managed Amazon GameLift Servers using example tools and sample games.


## [Building a game hosting solution](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/building-intro.html)

### [Development roadmaps](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/roadmaps-intro.html)

Choose a development roadmap that matches your hosting solution type to get step-by-step guidance for building your game hosting infrastructure.

- [Managed EC2 development roadmap](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-roadmap-managed.html): Get a head start on developing a managed game hosting solution with Amazon GameLift Servers for your session-based multiplayer game.
- [Managed containers development roadmap](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-roadmap-containers.html): Review the steps required to get your containerized game servers up and running with Amazon GameLift Servers.
- [Anywhere development roadmap](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-roadmap-anywhere.html): Get a head start on developing a game hosting solution for your on-premises hardware or virtual resources with Amazon GameLift Servers Anywhere.
- [Hybrid hosting development roadmap](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-roadmap-hybrid.html): Get a head start on developing a hybrid game hosting solution with Amazon GameLift Servers for your session-based multiplayer game.

### [Prepare a game for hosting](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/integration-intro.html)

Learn how to integrate your game server with the Amazon GameLift Servers Server SDK and build a backend service to manage game sessions and player connections.

### [Prepare with the game engine plugin](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/getting-started-plugin.html)

Learn how to integrate your Unreal games for cloud hosting using the Amazon GameLift ServersÂ plugin for Unreal Engine.

### [Plugin for Unreal Engine](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/unreal-plugin.html)

Learn how to integrate and deploy your Unreal games for cloud hosting using the Amazon GameLift ServersÂ plugin for Unreal Engine.

- [Set up an AWS user profile](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/unreal-plugin-profiles.html): After installing the plugin, set up a user profile with a valid AWS account.
- [Integrate your game code](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/unreal-plugin-integrate.html): Before you can deploy your game server to a fleet, you need to make a series of updates to game code and package game components for use with the Amazon GameLift Servers service.
- [Host your game locally with Anywhere](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/unreal-plugin-anywhere.html): Use this workflow to set up your local workstation as a game server host using an Anywhere fleet.
- [Deploy to a managed Amazon EC2 fleet](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/unreal-plugin-ec2.html): In this workflow, deploy your game for hosting on cloud-based compute resources managed by Amazon GameLift Servers.
- [Deploy to a managed container fleet](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/unreal-plugin-container.html): Use this guided plugin workflow to create a container image for your game server and deploy it to a container-based hosting solution.

### [Plugin for Unity (server SDK 5.x)](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/unity-plug-in.html)

Learn how to integrate your Unity games for cloud hosting using the Amazon GameLift ServersÂ plugin for Unity with server SDK 5.x.

- [Set up an AWS user profile](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/unity-plug-in-profiles.html): After installing the plugin, set up a user profile with a valid AWS account.
- [Set up local testing with Anywhere](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/unity-plug-in-anywhere.html): In this workflow, you add client and server game code for Amazon GameLift Servers functionality and use the plugin to designate your local workstation as a test game server host.
- [Deploy to a managed Amazon EC2 fleet](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/unity-plug-in-ec2.html): In this workflow, you use the plugin to prepare your game for hosting on cloud-based compute resources that are managed by Amazon GameLift Servers.
- [Deploy to a managed container fleet](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/unity-plug-in-container.html): Use this guided plugin workflow to create a container image for your game server and deploy it to a container-based hosting solution.

### [Plugin for Unity (server SDK 4)](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/unity-plug-in-sdk4.html)

Learn more about how to use the Amazon GameLift Servers standalone plugin for Unity (server SDK 4 or earlier).

- [Integrate a Unity game server](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/integration-unity-server-sdk4.html): Integrate Amazon GameLift Servers into your Unity game server project.
- [Integrate a Unity game client](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/integration-unity-client-sdk4.html): Use the Unity plugin to integrate Amazon GameLift Servers with your game client project.

### [Integrate a game server](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-sdk-server.html)

Learn how to integrate your game server project with Amazon GameLift Servers.

- [Integrate with the server SDK](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-sdk-server-api.html): Learn how to set up your game servers to communicate with Amazon GameLift Servers using the server SDK.

### [Integrate the server SDK for game engines](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/integration-engines.html)

Learn how to use Amazon GameLift Servers with your preferred game engine.

- [Integration with Unreal Engine](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/integration-engines-setup-unreal.html): Use the server SDK for Amazon GameLift Servers to integrate your Unreal Engine game project.
- [Integration with Unity](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/integration-engines-unity-using.html): Integrate the Amazon GameLift Servers SDK for Unity with you game server project.

### [Package a game server build](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-build-intro.html)

Get ready to deploy your game server build for hosting with Amazon GameLift Servers.

### [Create a game server build](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-build-cli-uploading.html)

Get your your custom game server software ready to deploy to Amazon GameLift Servers for hosting with managed EC2.

- [Package your game build files](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-build-packaging.html): Learn how to package your game server software for uploading to Amazon GameLift Servers.
- [Add a build install script](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-build-cli-uploading-install.html): Find tips on creating an install script for your game server build when hosting with Amazon GameLift Servers.

### [Create a build for managed hosting](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-build-cli-uploading-builds.html)

Learn about methods for uploading your game server software and create Amazon GameLift Servers build resource for managed hosting.

- [Create a build from a file directory](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-build-cli-uploading-upload-build.html): Learn how to upload a game server build to Amazon GameLift Servers from a local directory.
- [Create a build with files in Amazon S3](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-build-cli-uploading-create-build.html): Learn how to upload a game server build to Amazon GameLift Servers from an Amazon S3 bucket.
- [Build a container image](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/containers-prepare-images.html): Learn how to create and deploy a game server container image for use with Amazon GameLift Servers managed containers, including steps to build the image, push it to Amazon ECR, and prepare it for deployment to an Amazon GameLift Servers container fleet.
- [Amazon GameLift Servers interactions](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-sdk-interactions.html): Learn about the interactions that occur between a hosted game server, the Amazon GameLift Servers service, a backend service, and a game client.

### [Build a backend service](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift_quickstart_customservers_designbackend.html)

Get guidance on how to build a game backend service that authenticates players and communicates with the Amazon GameLift Servers service to request and receive information about game sessions .

- [Integrate game client functionality](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-sdk-client-api.html): Use the AWS SDK for C++ with Amazon GameLift Servers to set up a game client.
- [Serverless backend](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift_quickstart_customservers_designbackend_arch_serverless.html): Learn how to use Amazon GameLift Servers with other AWS services to create a serverless backend for your standalone game sessions servers.
- [WebSocket-based backend](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift_quickstart_customservers_designbackend_arch_websockets.html): Learn how to use an API Gateway WebSocket-based architecture to make matchmaking requests for your game hosted on Amazon GameLift Servers.

### [Deploy hosting fleets](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/fleets-intro.html)

Set up the hosting infrastructure for your game by choosing the right fleet type and configuring the compute resources that will run your game servers.

- [Choose a hosting option](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/fleets-decision-guide.html): Compare Amazon GameLift Servers hosting options to determine which approach best fits your game's requirements, technical constraints, and business goals.

### [Managed EC2 fleets](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/fleets-intro-managed.html)

Learn how Amazon GameLift Servers managed EC2 fleets provide cloud-based resources for game hosting, including automated deployment, scaling, and management of EC2 instances optimized for multiplayer games.

- [Create a managed EC2 fleet](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/fleets-creating.html): Learn how to create and configure an Amazon GameLift Servers managed EC2 fleet for game hosting, including selecting compute types, setting up runtime configurations, and managing game session resources.

### [Managed container fleets](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/fleets-intro-containers.html)

Learn how Amazon GameLift Servers managed container fleets provide a cloud-based platform for hosting containerized game servers, offering automated deployment, scaling, and management of EC2 instances optimized for multiplayer games.

- [How containers work](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/containers-howitworks.html): Learn how to structure, deploy, and manage Amazon GameLift Servers container fleets, including understanding core components, implementing common architectures, and leveraging key features such as active fleet updates, container packing, capacity scaling, and network configurations for optimal game server hosting.
- [Create a container fleet](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/containers-build-fleet.html): Learn how to create and configure a container fleet for game hosting, using the Amazon GameLift Servers console or the AWS CLI.
- [Create a container group definition](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/containers-create-groups.html): Learn about how to define your container architecture for an Amazon GameLift Servers container fleet.

### [Anywhere fleets](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/fleets-intro-anywhere.html)

Learn how to leverage Amazon GameLift Servers features with your own hosting resources using Anywhere fleets, self-manage your compute resources, and implement hybrid hosting solutions.

- [Create an Anywhere fleet](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/fleets-creating-anywhere.html): Learn how to create and manage Amazon GameLift Servers Anywhere fleets, including setting up custom locations, registering computes, and launching game servers for hybrid hosting solutions.
- [Build a hybrid hosting solution](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/hybrid-solution-guide.html): Learn how to combine multiple Amazon GameLift Servers fleet types to create a hybrid hosting solution that optimizes for cost, performance, and operational requirements.

### [Configure game session placement](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/queues-intro.html)

Set up game session queues to intelligently place new game sessions across your hosting resources, optimizing for player latency, resource utilization, and cost.

- [Create a queue](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/queues-creating.html): Create a Amazon GameLift Servers queue to find available game servers to host new game sessions, using FleetIQ to locate optimal placements across multiple locations.
- [Set up event notification](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/queue-notification.html): Learn how to set up event notifications for your Amazon GameLift Servers game session placements.

### [Customize your game hosting solution](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/customize-solution-intro.html)

Enhance your game hosting solution with advanced features like player session management, matchmaking, multi-region deployment, and cost optimization strategies.

### [Game server builds](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/customize-game-server-builds.html)

Enhance your game server builds with additional functionality, including integration with other AWS services.

- [Connect your game server to other AWS resources](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-sdk-server-resources.html): Learn how to access other AWS resources from applications hosted on your Amazon GameLift Servers fleets.
- [Let your game server access fleet data](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-sdk-server-fleetinfo.html): Learn how to access fleet and build information for a specific game server running on Amazon GameLift Servers.
- [Set up VPC peering](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/vpc-peering.html): Set up a network connection between your Amazon GameLift Servers game servers and other AWS resources.

### [Player sessions and matchmaking](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/customize-player-sessions-matchmaking.html)

Implement advanced player management and matchmaking features to enhance the multiplayer experience.

- [Generate player IDs](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/player-sessions-player-identifiers.html): Learn how to generate unique player IDs for Amazon GameLift Servers.
- [Add FlexMatch matchmaking](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-match-intro.html): Set up your game to use FlexMatch with Amazon GameLift Servers hosting to match players into games.

### [Game session placements](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/customize-game-session-placement.html)

Configure advanced game session placement strategies to optimize player experience and resource utilization.

### [Customize a queue](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/queues-design.html)

Customize the default configuration settings for an Amazon GameLift Servers game session queue to optimize how game sessions are placed based on resource usage, player experiences, and cost savings.

- [Define a queue's scope](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/queues-design-scope.html): Your game's player population might have groups of players who shouldn't play together.
- [Build a multi-location queue](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/queues-design-multiregion.html): We recommend a multi-location design for all queues.
- [Evaluate queue metrics](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/queues-design-metrics.html): Use metrics to evaluate how well your queues are performing.

### [Prioritize game session placement](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/queues-design-priority.html)

Amazon GameLift Servers uses an algorithm to determine how to prioritize a queue's destinations and determine where to place a new game session.

- [Create a player latency policy](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/queues-design-latency.html): Learn how to use player latency policies in Amazon GameLift Servers to optimize game session placement and prevent high-latency experiences for players.
- [Build a queue for Spot](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/spot-tasks.html): Create a resilient queue to boost effectiveness for your lower-cost Spot fleets with Amazon GameLift Servers game hosting.

### [Hosting resources](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/fleets-design.html)

Optimize your hosting infrastructure with advanced fleet configurations, cost management strategies, and deployment options.

- [Choose compute resources](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-compute.html): Choose the right hosting resources for your Amazon GameLift Servers managed EC2 or managed container fleets.
- [Customize a container fleet](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/containers-design-fleet.html): Learn how to customize and optimize Amazon GameLift Servers managed containers by setting resource limits, designating essential containers, configuring network connections, setting up health checks, managing container dependencies, and configuring container fleets for optimal performance and scalability.
- [Reduce hosting costs with Spot fleets](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/fleets-spot.html): Lower Amazon GameLift Servers hosting costs by adding Spot Instances to your hosting solution.
- [Optimize game servers runtime configuration](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/fleets-multiprocess.html): Set up Amazon GameLift Servers to run multiple game server processes concurrently on each instance in a managed EC2 fleet.
- [Work with the Agent](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/integration-dev-iteration-agent.html): Learn more about using the Amazon GameLift Servers Agent for testing with Amazon GameLift ServersÂ Anywhere.

### [Abstract a fleet with an alias](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/aliases-intro.html)

Learn how to use aliases to create persistent identifiers for your Amazon GameLift Servers hosting destinations.

- [Create an alias](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/aliases-creating.html): Learn how to edit Amazon GameLift Servers aliases, which represent destinations for game session placement.


## [Managing a game hosting solution](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/managing-hosting-solution.html)

### [Manage game hosting resources](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-console-intro.html)

Create, view, update, or delete Amazon GameLift Servers resources using the Amazon GameLift Servers console or the AWS CLI.

- [Console dashboard](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-console-dashboard.html): Learn about the Amazon GameLift Servers dashboard to get information about builds, fleets, resources, and the status of your hosting solutions.

### [Builds](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-console-builds.html)

On the Builds page of the Amazon GameLift Servers console, get detailed information about the game server builds that have been uploaded to Amazon GameLift Servers for deployment on managed EC2 fleets.

- [Update a build](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-build-cli-uploading-update-build-files.html): Learn about options for updating a game server build that's uploaded to Amazon GameLift Servers for managed hosting.

### [Fleets](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-console-fleets.html)

Use the Amazon GameLift Servers console to monitor and manage all types of hosting fleets and view game and player session info for a fleet.

### [Update a fleet configuration](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/fleets-editing.html)

Learn how to update Amazon GameLift Servers fleet settings, including using the fast build update tool for development.

- [Update fleet locations](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/fleets-update-locations.html): Learn how to update Amazon GameLift Servers fleet locations, including adding and removing remote locations, using either the Amazon GameLift Servers console or AWS CLI commands for efficient fleet management.
- [Delete a fleet](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/fleets-deleting.html): Learn how to delete Amazon GameLift Servers fleets, including those with VPC peering connections, using the Amazon GameLift Servers console or AWS CLI, and understanding the implications of fleet deletion on associated data and resources.
- [Fleet details](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-console-fleets-metrics.html): Use the Amazon GameLift Servers console to view detailed information about individual fleets, including configuration settings, fleet activity, health, and metrics.

### [Game sessions and player sessions](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-console-game-player-sessions-metrics.html)

Use the Amazon GameLift Servers console to view information about game session and player session activity.

- [Look up player session data](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/player-sessions.html): Use the Amazon GameLift Servers console to find game session activity for individual players.
- [Shut down a game session](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/terminate-sessions.html): Use the Amazon GameLift Servers console to shut down a game session.
- [Update a container fleet](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/containers-update-fleet.html): Learn how to update Amazon GameLift Servers managed container fleets, including modifying properties that require fleet redeployment, configuring redeployment options, and tracking deployment status using the Amazon GameLift Servers console or AWS CLI.
- [Update a container group definition](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/containers-modify-groups.html): Learn how to update Amazon GameLift Servers container group definitions, including modifying properties, managing version control, and deploying changes to new or existing container fleets using the Amazon GameLift Servers console or AWS CLI tools.
- [Delete a container group definition](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/containers-delete-groups.html): Learn how to delete container group definitions for Amazon GameLift Servers container fleets, including options for deleting specific versions, all versions, or older versions while retaining newer ones.

### [Aliases](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-console-aliases.html)

Use the Amazon GameLift Servers console to view, edit, and create aliases for your hosting solution.

- [Edit an alias](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/aliases-editing.html): Learn how to edit Amazon GameLift Servers aliases, which represent destinations for game session placement.
- [Game session queues](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/queues-console.html): Use the Amazon GameLift Servers console to monitor and manage game session queues and view queue metrics.
- [Prepare for game launch](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift_quickstart_customservers_checklist.html): Follow checklists for getting your Amazon GameLift Servers game hosting solution ready for production-level traffic.
- [Manage game hosting resources with CloudFormation](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/resources-cloudformation.html): Learn about how to build and manage Amazon GameLift Servers game hosting resources using CloudFormation.


## [DDoS protection](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/ddos-protection-intro.html)

- [How player gateway works](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/ddos-protection-howitworks.html): Learn about player gateway architecture, components, and traffic flow.
- [Enable player gateway on fleets](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/ddos-protection-enable.html): Configure player gateway on Amazon GameLift Servers fleets to protect game servers from DDoS attacks.
- [Integrate player gateway into a game](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/ddos-protection-integrate.html): Integrate player gateway into your game client and backend to route traffic through relay endpoints.


## [Testing and troubleshooting](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/troubleshooting-intro.html)

### [Set up for iterative development](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/integration-dev-iteration.html)

Learn how to create a hosted test environment for use during game development with Amazon GameLift Servers.

- [Build a cloud-based test environment](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/integration-dev-iteration-cloud.html): Create a cloud-based test environment for iterative development of your multiplayer game project with Amazon GameLift Servers hosting.
- [Set up local testing](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/integration-testing.html): Test your game server and client integration using your own local hardware.
- [Set up local testing (legacy)](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/integration-testing-local.html): Test your game server and client integration locally without having to deploy server fleets on Amazon GameLift Servers.
- [Debug fleet issues](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/fleets-creating-debug.html): Learn how to troubleshoot and resolve issues with Amazon GameLift Servers managed EC2 fleets, including problems during fleet creation, server process activation, fleet deletion.
- [Remotely connect to fleet instances](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/fleets-remote-access.html): Learn how to remotely connect to Amazon GameLift Servers managed EC2 and container fleet instances for troubleshooting, fine-tuning, and monitoring game server activity, including gathering instance data and accessing files on remote instances.


## [Scaling](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/fleets-manage-capacity.html)

- [Set hosting capacity limits](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/fleets-capacity-limits.html): Learn how to set and manage scaling limits for Amazon GameLift Servers fleet locations.
- [Manually set fleet capacity](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/fleets-updating-capacity.html): Learn how to manage player capacity for an Amazon GameLift Servers hosting fleet.

### [Auto scale fleet capacity](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/fleets-autoscaling.html)

Learn how to implement and manage auto scaling in Amazon GameLift Servers using target-based and rule-based policies to dynamically adjust fleet capacity, optimize resource utilization, and maintain a smooth player experience while minimizing hosting costs.

- [Target-based auto scaling](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/fleets-autoscaling-target.html): Learn how to implement and manage auto scaling for Amazon GameLift Servers fleets by setting a target capacity that sets a target capacity , including setting buffer sizes, adjusting capacity limits, and optimizing the balance between player wait times and resource costs.
- [Rule-based auto scaling](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/fleets-autoscaling-rule.html): Learn how to implement and manage a set of custom rules for automatically scaling Amazon GameLift Servers fleet capacity, including creating, updating, and deleting policies, understanding policy syntax, and applying best practices for optimizing fleet capacity management.
- [Manage Scaling a Fleet To/From Zero](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/fleets_scale-to-from-zero.html): Amazon GameLift Servers supports automatic scaling to and from zero instances based on game session activity.
- [Scale container fleets](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/containers-scaling.html): Learn how to effectively scale Amazon GameLift Servers managed container fleets by adjusting fleet capacity, implementing automatic scaling with target tracking, and understanding the impact of scaling on game session and player hosting capabilities.


## [Monitoring](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/monitoring-overview.html)

- [Monitor with CloudWatch](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/monitoring-cloudwatch.html): Use Amazon CloudWatch tools to monitor your Amazon GameLift Servers metrics.

### [Monitor with server telemetry metrics](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/monitoring-gamelift-servers-metrics.html)

Monitor your game servers with telemetry Amazon GameLift Servers metrics that can be collected and published to Amazon CloudWatch and Amazon Managed Service for Prometheus when deployed with your server build.

- [Implementation](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-servers-metrics-setup.html): Select your implementation path based on your development environment:
- [Available metrics](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-servers-metrics-types.html): Metrics fall into three categories:
- [How it works](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-servers-metrics-architecture.html): The telemetry metrics system follows a simple four-stage data flow from your game servers to visualization dashboards.
- [Dashboard organization and usage](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-servers-metrics-dashboards.html): View your metrics on comprehensive dashboards in Amazon Managed Grafana.
- [Common monitoring scenarios](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-servers-metrics-scenarios.html)
- [Troubleshooting guide](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-servers-metrics-troubleshooting.html)
- [Logging API calls](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/logging-using-cloudtrail.html): Use AWS CloudTrail to log all API calls to Amazon GameLift Servers actions.

### [Logging server messages](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/logging-server-messages.html)

Learn how to log server messages in Amazon GameLift Servers.

- [EC2 vs Container logging](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/logging-server-messages-ec2-vs-containers.html): Learn about the key differences in logging between managed EC2 fleets and container fleets.
- [Logging for custom servers](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/logging-server-messages-custom.html): Learn how to log server messages for Amazon GameLift Servers custom servers.


## [Security](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/security.html)

- [Data protection](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/data-protection.html): Learn about data protection measures for Amazon GameLift Servers, including understanding the AWS shared responsibility model, securing AWS credentials, encrypting data at rest and in transit, and managing internetwork traffic privacy for game server instances.

### [Identity and access management](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/security-iam.html)

How to authenticate requests and manage access to your Amazon GameLift Servers resources.

- [How Amazon GameLift Servers works with IAM](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon GameLift Servers, learn what IAM features are available to use with Amazon GameLift Servers.
- [Identity-based policy examples](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Amazon GameLift Servers resources.
- [Troubleshooting](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon GameLift Servers and AWS Identity and Access Management (IAM).
- [AWS managed policies](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon GameLift Servers and recent changes to those policies.
- [Logging and monitoring with Amazon GameLift Servers](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/logging-and-monitoring.html): Learn about how Amazon GameLift Servers uses AWS CloudTrail to capture and log all Amazon GameLift Servers API calls.
- [Compliance validation](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-compliance.html): Learn about compliance programs supported by Amazon GameLift Servers.
- [Resilience](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/disaster-recovery-resiliency.html): Learn how Amazon GameLift Servers leverages AWS global infrastructure and provides additional features like multi-region queues, automatic capacity scaling, and distributed instance management to enhance data resiliency and maintain high availability for game hosting services.
- [Infrastructure security](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/infrastructure-security.html): Learn how Amazon GameLift Servers isolates service traffic.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/vulnerability-analysis-management.html): Find best practices for regularly patching, updating, and securing the operating system and applications on your Amazon GameLift Servers instances.
- [Security best practices](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/security-best-practices.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon GameLift Servers features for data resiliency.


## [Pricing](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-intro-pricing.html)

- [Generate pricing estimates](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-calculator.html): Use AWS Pricing Calculator to create estimates for managed game hosting with Amazon GameLift Servers.
- [Cost optimization strategies](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-pricing-cost-optimization.html): Use these strategies with a managed hosting solution to help reduce your cloud hosting costs while maintaining high performance and player experience.


## [Reference guides](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/reference-intro.html)

- [Service API (AWS SDK)](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/reference-awssdk.html): View a task-based listing of Amazon GameLift Servers Service API operations for game hosting.

### [Server SDK 5.x](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/reference-serversdk.html)

Look up technical information for using the Amazon GameLift Servers server SDK.

- [Migrate to server SDK 5.x](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/reference-serversdk5-migration.html): Learn how to migrate your game project to server SDK for Amazon GameLift Servers version 5.x.

### [C++ server SDK](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/integration-server-sdk5-cpp-actions.html)

Use this Amazon GameLift Servers SDK reference when integrating Amazon GameLift Servers into a C++ multiplayer game server project.

- [Data types](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/integration-server-sdk5-cpp-datatypes.html): Use this SDK reference when integrating Amazon GameLift Servers into a multiplayer game server.

### [C# server SDK](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/integration-server-sdk5-csharp-actions.html)

Use this Amazon GameLift Servers API reference when integrating Amazon GameLift Servers into a C# multiplayer game server project.

- [Data types](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/integration-server-sdk5-csharp-datatypes.html): Use this API reference when integrating Amazon GameLift Servers into a multiplayer game server.

### [Go server SDK](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/integration-server-sdk-go-actions.html)

Use this Amazon GameLift Servers API reference when integrating Amazon GameLift Servers into a Go multiplayer game server project.

- [Data types](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/integration-server-sdk-go-datatypes.html): Use this SDK reference when integrating Amazon GameLift Servers into a multiplayer game server.

### [C++ (Unreal) server SDK: Actions](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/integration-server-sdk5-unreal-actions.html)

Use this Amazon GameLift Servers SDK reference when integrating Amazon GameLift Servers into an Unreal multiplayer game server project.

- [Data types](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/integration-server-sdk5-unreal-datatypes.html): Use this SDK reference when integrating Amazon GameLift Servers into a multiplayer game server.

### [Server SDK 4 and earlier](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/reference-serversdk4.html)

Look up technical information for using the server SDK for Amazon GameLift Servers, version 4 or earlier.

### [Server SDK for C++: Actions](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/integration-server-sdk-cpp-ref-actions.html)

Use this Amazon GameLift Servers SDK reference when integrating Amazon GameLift Servers into a C++ multiplayer game server project.

- [Data types](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/integration-server-sdk-cpp-ref-datatypes.html): Use this Amazon GameLift Servers SDK reference when integrating Amazon GameLift Servers into a multiplayer game server.

### [Server SDK for C#: Actions](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/integration-server-sdk-csharp-ref-actions.html)

Use this Amazon GameLift Servers SDK reference when integrating Amazon GameLift Servers into a C# multiplayer game server project.

- [Data types](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/integration-server-sdk-csharp-ref-datatypes.html): Use this SDK reference when integrating Amazon GameLift Servers into a multiplayer game server.

### [Server SDK for Unreal: Actions](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/integration-server-sdk-unreal-ref-actions.html)

Use this Amazon GameLift Servers API reference when integrating Amazon GameLift Servers into a Unreal multiplayer game server project.

- [Data types](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/integration-server-sdk-unreal-ref-datatypes.html): Use this Amazon GameLift Servers API reference when integrating Amazon GameLift Servers into a multiplayer game server.
- [Game session placement events](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/queue-events.html): Look up syntax for game session placement event types that are emitted by Amazon GameLift Servers game session queues.
- [AMI versions](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/reference-ec2-ami-version-history.html): Look up version history for the EC2 AMIs that Amazon GameLift Servers uses for its managed EC2 game hosting.
- [Service locations](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-regions.html): Learn about how Amazon GameLift Servers features are available in multiple geographic locations, including AWS Regions and Local Zones.
- [Service endpoints and quotas](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/limits-regions.html): Learn about endpoints and quotas for the Amazon GameLift Servers service.

### [Amazon GameLift Servers API limits](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/api-limits-table.html)

This table provides information about the default API limits for Amazon GameLift Servers.

- [API limits reference](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/api-limits-common.html): The following table lists the default rate limits for Amazon GameLift Servers API operations.
- [Resource-level throttling](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/api-limits-resource-throttling.html): Some API operations are subject to resource-level throttling to prevent database hot key issues.
- [Amazon GameLift Servers SDK API limits](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/servers-api-limits-table.html): This table provides information about the default SDK API limits for Amazon GameLift Servers.
- [UDP ping beacons](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/reference-udp-ping-beacons.html): Learn how to use Amazon GameLift Servers's UDP ping beacons to accurately measure network latency between player devices and game server locations.

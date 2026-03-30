# Source: https://docs.aws.amazon.com/medialive/latest/ug/llms.txt

# MediaLive User Guide

> Use MediaLive to create live outputs for broadcast and streaming delivery. This documentation is offered here as a free Kindle book, or you can read it online or in PDF format at https://aws.amazon.com/documentation/medialive/.

- [How MediaLive Works](https://docs.aws.amazon.com/medialive/latest/ug/how-medialive-works-channels.html)
- [Quotas](https://docs.aws.amazon.com/medialive/latest/ug/limits.html)
- [Feature rules and limits](https://docs.aws.amazon.com/medialive/latest/ug/eml-limitations-and-rules.html)
- [Preliminary setup steps](https://docs.aws.amazon.com/medialive/latest/ug/setting-up.html)
- [Operations: Start, stop, and pause channel](https://docs.aws.amazon.com/medialive/latest/ug/starting-stopping-deleting-a-channel.html)
- [Document history](https://docs.aws.amazon.com/medialive/latest/ug/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/medialive/latest/ug/glossary.html)

## [What Is MediaLive?](https://docs.aws.amazon.com/medialive/latest/ug/what-is.html)

- [Terminology](https://docs.aws.amazon.com/medialive/latest/ug/what-is-terminology.html)
- [Related Services](https://docs.aws.amazon.com/medialive/latest/ug/related-services.html): Amazon CloudWatch is a monitoring service for AWS Cloud resources and the applications that you run on AWS.
- [Accessing MediaLive](https://docs.aws.amazon.com/medialive/latest/ug/what-is-accessing.html): You can access MediaLive using any of the following methods:


## [Pricing and reservations](https://docs.aws.amazon.com/medialive/latest/ug/pricing-and-reservations.html)

- [Pricing in MediaLive](https://docs.aws.amazon.com/medialive/latest/ug/pricing.html): As with other AWS products, there are no contracts or minimum commitments for using AWS Elemental MediaLive.

### [Reservations](https://docs.aws.amazon.com/medialive/latest/ug/reservations.html)

Reduce processing rates by purchasing reservations for input and output configurations in AWS Elemental MediaLive, or automatically renew reservations.

- [How input and output reservations work](https://docs.aws.amazon.com/medialive/latest/ug/input-output-reservations.html): MediaLive offers input and output reservations.
- [Add-on reservations](https://docs.aws.amazon.com/medialive/latest/ug/addon-reservations.html): Reservations are available for those items in the MediaLive price list that are considered to be add-ons, such as codec licenses.
- [Purchasing a reservation](https://docs.aws.amazon.com/medialive/latest/ug/purchasing-reservations.html): On the console, use the Reservations tab to purchase one or more reservations.
- [Viewing purchased reservations](https://docs.aws.amazon.com/medialive/latest/ug/view-reservations.html): On the console, you can view the reservations that you have purchased.
- [Deleting an expired reservation](https://docs.aws.amazon.com/medialive/latest/ug/deleting-reservations.html): When a reservation has expired, you can delete the reservation from the list.


## [IAM permissions for users](https://docs.aws.amazon.com/medialive/latest/ug/setting-up-for-production.html)

- [Reference: summary of user access](https://docs.aws.amazon.com/medialive/latest/ug/setup-users-step-1-summary.html): Consult a table that shows all the types of permissions that you might need to assign to AWS Elemental MediaLive users.
- [MediaLive](https://docs.aws.amazon.com/medialive/latest/ug/requirements-for-medialive.html): Learn about the permissions to give to users so that they can use MediaLive features.
- [MediaLive Anywhere](https://docs.aws.amazon.com/medialive/latest/ug/requirements-for-emla.html): Learn about the permissions to give to users so that they can configure the MediaLive Anywhere clusters, and so that they can work with MediaLive Anywhere resources when creating channels.
- [CloudFormation](https://docs.aws.amazon.com/medialive/latest/ug/requirements-for-CFN.html): Learn about the permissions that you might need to give to AWS Elemental MediaLive users so that they can work with AWS CloudFormation features.
- [CloudFront](https://docs.aws.amazon.com/medialive/latest/ug/requirements-for-CFront.html): Learn about the permissions that you might need to give to AWS Elemental MediaLive users so that they can use the MediaLive workflow wizard.
- [CloudTrail](https://docs.aws.amazon.com/medialive/latest/ug/requirements-for-cloudtrail.html): Learn about the permissions that you might need to give to users so that they MediaLive can log API calls in AWS CloudTrail.
- [CloudWatchâchannel health](https://docs.aws.amazon.com/medialive/latest/ug/requirements-for-monitor-channel-health.html): Learn about the permissions that you might need to give to AWS Elemental MediaLive users so that they can monitor MediaLive activity using Amazon CloudWatch.
- [CloudWatch and Amazon SNSâemail notification](https://docs.aws.amazon.com/medialive/latest/ug/requirements-for-email-notification.html): Learn about the permissions that you might need to give to AWS Elemental MediaLive users so that they can monitor activity using Amazon CloudWatch and Amazon Simple Notification Service.
- [CloudWatch Logsâchannel logging](https://docs.aws.amazon.com/medialive/latest/ug/requirements-for-console-logging.html): Learn about the permissions that you might need to give to AWS Elemental MediaLive users so that they can use MediaLive activity in Amazon CloudWatch Logs.
- [EC2 âVPC inputs](https://docs.aws.amazon.com/medialive/latest/ug/requirements-for-vpc-input.html): Learn about the permissions that you might need to give to AWS Elemental MediaLive users so that they can run use push inputs in your VPC.
- [EC2 âdelivery via VPC](https://docs.aws.amazon.com/medialive/latest/ug/requirements-vpc-delivery.html): Learn about the permissions that you might need to give to AWS Elemental MediaLive users so that they can run MediaLive channels in your VPC.
- [Link](https://docs.aws.amazon.com/medialive/latest/ug/requirements-for-link.html): Your organization might deploy AWS Elemental Link hardware devices in one or both of these ways:
- [MediaConnect](https://docs.aws.amazon.com/medialive/latest/ug/requirements-for-media-connect.html): Learn about the permissions that you might need to give to AWS Elemental MediaLive users so that they can use MediaLive with AWS Elemental MediaConnect flows.
- [MediaPackage](https://docs.aws.amazon.com/medialive/latest/ug/requirements-for-mediapackage.html): Learn about the permissions that you might need to give to AWS Elemental MediaLive users so that they can use MediaLive with AWS Elemental MediaPackage channels.
- [Resource Groupsâtagging](https://docs.aws.amazon.com/medialive/latest/ug/requirements-for-tagging.html): Learn about the permissions that you might need to give to AWS Elemental MediaLive users so that they can use work with tags.
- [Amazon S3](https://docs.aws.amazon.com/medialive/latest/ug/requirements-for-s3.html): Learn about the permissions that you might need to give to AWS Elemental MediaLive users so that they work with assets stored in Amazon Simple Storage Service buckets.
- [Secrets Manager secrets](https://docs.aws.amazon.com/medialive/latest/ug/requirements-for-secrets.html): Your deployment might include the following resources:
- [Systems Manager parameter store](https://docs.aws.amazon.com/medialive/latest/ug/requirements-for-EC2.html): The AWS Elemental MediaLive console includes a feature that lets a user create a password parameter in the AWS Systems Manager Parameter Store.


## [IAM permissions for trusted entity](https://docs.aws.amazon.com/medialive/latest/ug/setting-up-trusted-entity.html)

- [About the trusted entity role](https://docs.aws.amazon.com/medialive/latest/ug/about-trusted-entity.html): Learn about why AWS Elemental MediaLive must be set up as a trusted entity in your organization's AWS account.
- [Choose the option](https://docs.aws.amazon.com/medialive/latest/ug/scenarios-for-medialive-role.html): Learn about the two options available for setting up AWS Elemental MediaLive as a trusted entity in your organization's AWS account.
- [Set up with simple option](https://docs.aws.amazon.com/medialive/latest/ug/setup-trusted-entity-simple.html): Learn how to set up AWS Elemental MediaLive with the standard trusted entity role.

### [Set up with complex option](https://docs.aws.amazon.com/medialive/latest/ug/setup-trusted-entity-complex.html)

Learn how to set up AWS Elemental MediaLive with a custom trusted entity role.

- [Step 1: Identify requirements](https://docs.aws.amazon.com/medialive/latest/ug/complex-scenario-create-trusted-entity-role-step1.html): Learn how to identify access requirements that AWS Elemental MediaLive needs when you set it up with a custom trusted entity role.
- [Step 2: Create policies](https://docs.aws.amazon.com/medialive/latest/ug/complex-scenario-create-trusted-entity-role-step2.html): Learn how to create the policies that the trusted entity for AWS Elemental MediaLive needs, when you set it up with a custom trusted entity role.
- [Step 3: Create roles](https://docs.aws.amazon.com/medialive/latest/ug/complex-scenario-create-trusted-entity-role-step3.html): Learn how to create the roles that the trusted entity for AWS Elemental MediaLive needs, when you set it up with a custom trusted entity role.
- [Step 4: Set up user permissions](https://docs.aws.amazon.com/medialive/latest/ug/requirements-medialiverole-complex-permissions.html): Learn about the permissions that you must give to users when you set up AWS Elemental MediaLive up with a custom trusted entity role.
- [Access requirements](https://docs.aws.amazon.com/medialive/latest/ug/trusted-entity-requirements.html): Read the list of permissions that the trusted entity for AWS Elemental MediaLive needs, when you set it up with a custom trusted entity role.


## [Ways to work with MediaLive](https://docs.aws.amazon.com/medialive/latest/ug/getting-started.html)

### [Workflow wizard](https://docs.aws.amazon.com/medialive/latest/ug/wizard.html)

Learn how to use the workflow wizard to quickly create a functioning channel.

- [About the workflow wizard](https://docs.aws.amazon.com/medialive/latest/ug/wizard-about.html)
- [Using the workflow wizard](https://docs.aws.amazon.com/medialive/latest/ug/wizard-procedure.html)
- [Next stepsânovice users](https://docs.aws.amazon.com/medialive/latest/ug/wizard-next-step-novice.html): If you are new to the world of video streaming and have fairly modest requirements, you might find that the workflow wizard implements all the features you need, and that the Workflow Details page gives you the monitoring details and runtime controls you require.
- [Next stepsâexperienced video users](https://docs.aws.amazon.com/medialive/latest/ug/wizard-next-step-experienced.html): If you have experience with video streaming and with other AWS services, you might want to add more MediaLive resources and more resources from other AWS services to the workflow.

### [Tutorial](https://docs.aws.amazon.com/medialive/latest/ug/getting-started-tutorial.html)

Follow this tutorial to learn the basics of creating an AWS Elemental MediaLive workflow.

- [Prerequisites for the tutorial](https://docs.aws.amazon.com/medialive/latest/ug/getting-started-prerequisites.html): Before you can use MediaLive, you need an AWS account and the appropriate permissions to access, create, and view MediaLive components.
- [Step 1: Set up the upstream system](https://docs.aws.amazon.com/medialive/latest/ug/getting-started-step1.html): The upstream system is the system that streams the video to MediaLive.
- [Step 2: Set up the downstream system](https://docs.aws.amazon.com/medialive/latest/ug/getting-started-step2.html): In this tutorial, the downstream system (the destination for the output from MediaLive) is AWS Elemental MediaPackage.
- [Step 3: Create an input](https://docs.aws.amazon.com/medialive/latest/ug/getting-started-step3.html): You must create an input. the input defines how the upstream system provides the source video stream to MediaLive. in this tutorial, you create an rtp input.
- [Step 4: Set up key information](https://docs.aws.amazon.com/medialive/latest/ug/getting-started-step4.html): The first step to creating a channel from scratch is to choose the IAM role that MediaLive will use to access the channel when the channel is running (started) and specify key characteristics of the input.
- [Step 5: Attach the input](https://docs.aws.amazon.com/medialive/latest/ug/getting-started-step4b.html): Now you are ready to identify the input that the channel will ingest.
- [Step 6: Set up input video, audio, captions](https://docs.aws.amazon.com/medialive/latest/ug/getting-started-step4a-input-selectors.html): You can create "selectors" to identify the specific video, audio, and captions that you want to extract from the input.
- [Step 7: Create an HLS output group](https://docs.aws.amazon.com/medialive/latest/ug/getting-started-step5.html): Once you have set up the input, you continue with the channel creation by creating an output group.
- [Step 8: Set up the output and encodes](https://docs.aws.amazon.com/medialive/latest/ug/getting-started-step6.html): Now that you have defined one output group in the channel, you can set up an output ins that output group, and specify how you want to encode the video output and the audio output.
- [Step 9: Create your channel](https://docs.aws.amazon.com/medialive/latest/ug/getting-started-step7.html): You have entered the minimum required information, so you are ready to create the channel.
- [Step 10: Start the upstream system and the channel](https://docs.aws.amazon.com/medialive/latest/ug/getting-started-step8.html): You can now start the upstream system in order to push the streaming content to MediaLive, encode the content, and send it to AWS Elemental MediaPackage.
- [Step 11: Clean up](https://docs.aws.amazon.com/medialive/latest/ug/getting-started-step9.html): To avoid extraneous charges, delete this channel and input when you have finished working with it.


## [Setup: MediaLive Anywhere](https://docs.aws.amazon.com/medialive/latest/ug/setup-emla.html)

- [How MediaLive Anywhere works](https://docs.aws.amazon.com/medialive/latest/ug/about-emla.html): Read about how AWS Elemental MediaLive Anywhere organizes on-premises node hardware into clusters in your network.
- [Design the cluster](https://docs.aws.amazon.com/medialive/latest/ug/emla-deploy-design-cluster.html): Learn how to organize your on-premises nodes into AWS Elemental MediaLive Anywhere clusters, and how to integrate the cluster of nodes into your network.
- [Identify network resources](https://docs.aws.amazon.com/medialive/latest/ug/emla-deploy-identify-network-requirements.html): Read about how to allocate resources on your organization's networks for the user of the nodes in an AWS Elemental MediaLive Anywhere cluster.
- [Design mappings](https://docs.aws.amazon.com/medialive/latest/ug/emla-design-mappings.html): Learn how to design the mappings that connect the network interfaces on the nodes to the network that each interface uses.

### [Set up in IAM](https://docs.aws.amazon.com/medialive/latest/ug/emla-deploy-iam.html)

You must perform some setup in AWS Identity and Access Management.

- [Create the instance role](https://docs.aws.amazon.com/medialive/latest/ug/emla-deploy-instance-role.html): To use MediaLive Anywhere, you must create a trusted entity configuration that lets AWS Systems Manager perform actions on the on-premises node hardware where MediaLive is running.

### [Set up users](https://docs.aws.amazon.com/medialive/latest/ug/emla-deploy-users.html)

You must set up IAM users with permissions so that they can configure a MediaLive Anywhere cluster, and/or so that they can run channels on on-premises node hardware.

- [Create users and assign permissions](https://docs.aws.amazon.com/medialive/latest/ug/emla-deploy-users-permissions.html): If you haven't set up users who will run channels on on-premises hardware, you should do that now.
- [Create special FAS policies](https://docs.aws.amazon.com/medialive/latest/ug/emla-deploy-users-ecs-permissions.html): After you have assigned permissions to MediaLive Anywhere users, you must create two extra policies:
- [Modifying the MediaLive trusted entity](https://docs.aws.amazon.com/medialive/latest/ug/emla-deploy-modify-ml-trusted-entity.html): You must modify the trusted entity role that you created for MediaLive.

### [Create the cluster](https://docs.aws.amazon.com/medialive/latest/ug/emla-setup-cluster.html)

Learn how to set up the networks, clusters, nodes, and SDI sources that you have identified for your AWS Elemental MediaLive Anywhere deployment.

- [Create the networks](https://docs.aws.amazon.com/medialive/latest/ug/emla-setup-cl-networks.html): Create the networks that you identified when you designed the cluster.
- [Create the clusters](https://docs.aws.amazon.com/medialive/latest/ug/emla-setup-cl-create.html): Create the clusters after you have created the networks.
- [Create the nodes](https://docs.aws.amazon.com/medialive/latest/ug/emla-setup-cl-nodes-create.html): Create all the nodes for one cluster.
- [Create SDI sources](https://docs.aws.amazon.com/medialive/latest/ug/emla-setup-cl-sdi.html): If some of the nodes in a cluster include SDI cards and ports, you must create SDI sources and SDI mappings:
- [Result of this setup](https://docs.aws.amazon.com/medialive/latest/ug/emla-setup-cl-result.html): You have now performed the hardware and network setup for the MediaLive Anywhere deployment.


## [Setup: Planning a MediaLive workflow](https://docs.aws.amazon.com/medialive/latest/ug/container-planning-workflow.html)

### [Part 1: Preparing](https://docs.aws.amazon.com/medialive/latest/ug/container-planning-uss-dss.html)

As the first stage in planning the workflow, you must set up the upstream and downstream systems.

### [Step 1: Identify output group types](https://docs.aws.amazon.com/medialive/latest/ug/identify-downstream-system.html)

The first step in planning any AWS Elemental MediaLive workflow is to determine which types of output groups you need to produce, based on the requirements and capabilities of the systems that are downstream of MediaLive.

- [Choosing among the AWS media services](https://docs.aws.amazon.com/medialive/latest/ug/dss-choose-service.html): If your preferred downstream system is another AWS media service, following are some useful tips for choosing the service to use:
- [HLS versus MediaPackage](https://docs.aws.amazon.com/medialive/latest/ug/hls-choosing-hls-vs-emp.html): If you want to deliver HLS output to AWS Elemental MediaPackage, you must decide if you want to create an HLS output group or a MediaPackage output group.
- [Options for Microsoft Smooth](https://docs.aws.amazon.com/medialive/latest/ug/downstream-system-for-mss.html): If you are delivering to a Microsoft Smooth Streaming server, the setup depends on whether you want to protect your content with a digital rights management (DRM) solution.
- [Step 2: Identify encode requirements](https://docs.aws.amazon.com/medialive/latest/ug/identify-dss-video-audio.html): After you have identified the output groups that you need to create, you must identify the requirements for the video and audio encodes that you will include in each output group.
- [Step 3: Identify resiliency requirements](https://docs.aws.amazon.com/medialive/latest/ug/plan-redundancy.html): Resiliency is the ability of the channel to continue to work when problems occur.

### [Step 4: Assess the upstream system](https://docs.aws.amazon.com/medialive/latest/ug/evaluate-upstream-system.html)

Learn how to assess the upstream system and the source content to verify that AWS Elemental MediaLive can work with them.

- [Assess source formats and packaging](https://docs.aws.amazon.com/medialive/latest/ug/uss-obtain-info.html): Learn how to assess the upstream system and the source content to verify that AWS Elemental MediaLive can work with them.
- [Encrypted HLS content](https://docs.aws.amazon.com/medialive/latest/ug/planning-hls-input-encrypted.html): Learn about the types of encrypted HLS content that AWS Elemental MediaLive can ingest.
- [Assess video content](https://docs.aws.amazon.com/medialive/latest/ug/assess-uss-source.html): Learn how to assess the source video that that you want AWS Elemental MediaLive to ingest.
- [Assess audio content](https://docs.aws.amazon.com/medialive/latest/ug/assess-uss-audio.html): Learn how to assess the source audio that that you want AWS Elemental MediaLive to ingest.
- [Assess captions](https://docs.aws.amazon.com/medialive/latest/ug/assess-uss-captions.html): Learn how to assess the source captions that that you want AWS Elemental MediaLive to ingest.

### [Step 5: Collect source information](https://docs.aws.amazon.com/medialive/latest/ug/planning-content-extract.html)

After you have assessed the source content and have identified suitable video, audio, and captions assets in that content, you must obtain information about those assets.

- [CDI source](https://docs.aws.amazon.com/medialive/latest/ug/extract-contents-cdi.html): The content in a CDI source always consists of uncompressed video, uncompressed audio, and captions.
- [AWS Elemental Link source](https://docs.aws.amazon.com/medialive/latest/ug/extract-contents-link.html): The content in an AWS Elemental Link source is always a transport stream (TS) that contains one video asset, one audio pair, and optional captions.
- [HLS source](https://docs.aws.amazon.com/medialive/latest/ug/extract-contents-hls.html): The content in an HLS container is always a transport stream (TS) that contains only one video rendition (program).
- [MediaConnect source](https://docs.aws.amazon.com/medialive/latest/ug/extract-content-emx.html): The content in an AWS Elemental MediaConnect source is always a transport stream (TS).
- [MP4 source](https://docs.aws.amazon.com/medialive/latest/ug/extract-contents-mp4.html): The content in an MP4 source always consists of one video track, one or more audio tracks, and optional captions.
- [RTMP source](https://docs.aws.amazon.com/medialive/latest/ug/extract-contents-rtmp.html): This procedure applies to both RTMP push and pull inputs from the internet, and to RTMP inputs from Amazon Virtual Private Cloud.
- [RTP source](https://docs.aws.amazon.com/medialive/latest/ug/extract-contents-rtp.html): This procedure applies to both RTP inputs from the internet and inputs from Amazon Virtual Private Cloud.
- [SMPTE 2110 source](https://docs.aws.amazon.com/medialive/latest/ug/extract-contents-s2110.html): The content in a SMPTE 2110 source is always a set of streams consisting of one video asset, zero or more audio assets, and zero or more captions (ancillary data) assets.
- [SRT source](https://docs.aws.amazon.com/medialive/latest/ug/extract-contents-srt.html): The content in an SRT input is always a transport stream (TS).
- [Step 6: Coordinate with downstream systems](https://docs.aws.amazon.com/medialive/latest/ug/setting-up-downstream-system.html): As the final step in preparing the downstream and upstream systems in your workflow, you must speak to the operator of the downstream system and coordinate information.

### [Part 2: Planning the outputs](https://docs.aws.amazon.com/medialive/latest/ug/planning-the-channel-in-workflow.html)

You should plan the AWS Elemental MediaLive channel as the second stage of planning a transcoding workflow.

### [Step 1: Identify the output encodes](https://docs.aws.amazon.com/medialive/latest/ug/planning-encodes.html)

When you prepared the downstream systems, you identified the output groups that you need.

- [Identify video](https://docs.aws.amazon.com/medialive/latest/ug/channel-planning-video-encodes.html): You must decide on the number of video encodes and their codecs.
- [Identify audio](https://docs.aws.amazon.com/medialive/latest/ug/channel-planning-audio-encodes.html): You must decide on the number of audio encodes.
- [Identify captions](https://docs.aws.amazon.com/medialive/latest/ug/channel-planning-captions-encodes.html): You must decide on the number of captions encodes.
- [Summary of encode rules](https://docs.aws.amazon.com/medialive/latest/ug/encode-rules.html): This table summarizes the rules for encodes for each output group.
- [Example of a plan](https://docs.aws.amazon.com/medialive/latest/ug/plan-encodes-example.html): After you have performed this procedure, you should have information that looks like this example.
- [Step 2: Map outputs to sources](https://docs.aws.amazon.com/medialive/latest/ug/channel-map-output-source.html): As part of the planning for an AWS Elemental MediaLive channel, learn how to identify the video, audio, and captions assets to extract from the sources.

### [Step 3: Design the encodes](https://docs.aws.amazon.com/medialive/latest/ug/designing-encodes.html)

In the first step of planning the channel, you identified the video, audio, and captions encodes to include in each output group.

- [Plan the encodes](https://docs.aws.amazon.com/medialive/latest/ug/plan-encodes.html): In , you sketched out a plan for the encodes you want to create in each output group.
- [Identify encode sharing opportunities](https://docs.aws.amazon.com/medialive/latest/ug/plan-encode-sharing.html): If you have already identified the details for all the output encodes, you can now identify opportunities for encode sharing.


## [Setup: Creating inputs](https://docs.aws.amazon.com/medialive/latest/ug/medialive-inputs.html)

- [Getting ready](https://docs.aws.amazon.com/medialive/latest/ug/input-create-getready.html): Before you create any input, you should plan the workflow.

### [CDI input](https://docs.aws.amazon.com/medialive/latest/ug/input-create-cdi-push.html)

This section describes how to create a CDI push input.

- [Step 1: Set up VPC](https://docs.aws.amazon.com/medialive/latest/ug/setup-vpc-cdi-vpc.html): An Amazon VPC user must set up the VPC, and identify subnets and security groups that both the upstream system and MediaLive will use.
- [Step 2: Create input](https://docs.aws.amazon.com/medialive/latest/ug/setup-input-cdi-vpc.html): After the Amazon VPC user has set up on the VPC, you can create the CDI input in MediaLive.
- [Step 3: Set up upstream](https://docs.aws.amazon.com/medialive/latest/ug/setup-uss-cdi-vpc.html): After you create the CDI input, you must make sure that the operator at the upstream system sets up correctly with your VPC, and that they push content to the correct locations in MediaLive.
- [Result of this procedure](https://docs.aws.amazon.com/medialive/latest/ug/setup-result-cdi-vpc.html): The results of this setup are illustrated in the diagram that follows.
- [CDI input â Partner CDI input](https://docs.aws.amazon.com/medialive/latest/ug/input-create-cdi-partners.html): A partner CDI input is a specific configuration of a CDI input.

### [Elemental Link input](https://docs.aws.amazon.com/medialive/latest/ug/input-create-link-device.html)

This section describes how to create an Elemental Link push input.

- [Step 1: Obtain information](https://docs.aws.amazon.com/medialive/latest/ug/setup-input-link-obtain-info.html): Obtain the following information from the operator of the AWS Elemental Link device:
- [Step 2: Create input](https://docs.aws.amazon.com/medialive/latest/ug/setup-uss-input-link.html): After you have obtained information about the AWS Elemental Link hardware device, you can create an Elemental Link input.
- [Result of this procedure](https://docs.aws.amazon.com/medialive/latest/ug/setup-link-result.html): As a result of this setup, an Elemental Link input (the blue box) exists that identifies the AWS Elemental Link device or devices (the purple box) that are connected to MediaLive.

### [HLS input](https://docs.aws.amazon.com/medialive/latest/ug/input-create-hls-pull.html)

This section describes how to create an HLS input.

- [Step 1: Obtain information](https://docs.aws.amazon.com/medialive/latest/ug/setup-hls-http.html): Obtain the following information from the operator at the upstream system:
- [Step 2: Create input](https://docs.aws.amazon.com/medialive/latest/ug/setup-input-hls.html): After you have obtained information from the upstream system, you can create an HLS input.
- [Step 3: Set up upstream](https://docs.aws.amazon.com/medialive/latest/ug/setup-uss-hls.html): An operator at the upstream server must set up the source content on the upstream system.
- [Result of this procedure](https://docs.aws.amazon.com/medialive/latest/ug/setup-hls-result.html): As a result of this setup, an HLS input exists that specifies one or two source URLs.

### [MediaConnect input](https://docs.aws.amazon.com/medialive/latest/ug/input-create-push-mediaconnect.html)

This section describes how to create a MediaConnect input.

- [Step 1: Set up MediaConnect](https://docs.aws.amazon.com/medialive/latest/ug/setup-emx-flows.html): A MediaConnect user must set up MediaConnect with flows to deliver source content to MediaLive.
- [Step 2: Create input](https://docs.aws.amazon.com/medialive/latest/ug/setup-input-emx.html): After MediaConnect is set up, you can create the MediaConnect input.
- [Result of this procedure](https://docs.aws.amazon.com/medialive/latest/ug/setup-result-emx.html): The results of this setup are illustrated in the diagram that follows.

### [MediaConnect Router input](https://docs.aws.amazon.com/medialive/latest/ug/input-create-mediaconnect-router.html)

This section describes how to create a MediaConnect Router input.

- [Step 1: Create input](https://docs.aws.amazon.com/medialive/latest/ug/setup-input-mediaconnect-router.html): Unlike MediaConnect Inputs, with MediaConnect Router Inputs there is no MediaConnect setup step required to create an input.

### [MP4 input](https://docs.aws.amazon.com/medialive/latest/ug/mp4-pull-input.html)

This section describes how to set up the source content on the upstream system, and how to create an MP4 input that connects the content source to MediaLive.

- [Step 1: Obtain information](https://docs.aws.amazon.com/medialive/latest/ug/setup-mp4-obtain-info.html): Obtain the following information from the operator at the upstream system:
- [Step 2: Create input](https://docs.aws.amazon.com/medialive/latest/ug/setup-input-mp4.html): After you have obtained information from the upstream system, you can create an MP4 input.
- [Step 3: Set up upstream system](https://docs.aws.amazon.com/medialive/latest/ug/setup-uss-mp4.html): An operator at the upstream server must set up the source content on the upstream system.
- [Result of this procedure](https://docs.aws.amazon.com/medialive/latest/ug/setup-result-mp4.html): As a result of this setup, a MediaLive input exists that specifies one or two source URLs.

### [RTMP pull input](https://docs.aws.amazon.com/medialive/latest/ug/input-create-rtmp-pull.html)

This section describes how to set up the source content on the upstream system, and how to create an RTMP pull input that connects the upstream system to MediaLive.

- [Step 1: Obtain information](https://docs.aws.amazon.com/medialive/latest/ug/setup-rtmp-pull-obtain-info.html): Obtain the following information from your contact person at the upstream system:
- [Step 2: Create input](https://docs.aws.amazon.com/medialive/latest/ug/setup-input-rtmp-pull.html): After you have obtained information from the upstream system, you can create an HLS input.
- [Step 3: Set up upstream](https://docs.aws.amazon.com/medialive/latest/ug/setup-uss-rtmp-pull.html): An operator at the upstream server must set up the source content on the upstream system.
- [Result of this procedure](https://docs.aws.amazon.com/medialive/latest/ug/setup-result-rtmp-pull.html): As a result of this setup, an RTMP pull input exists that specifies one or two source URLs.

### [RTMP push input](https://docs.aws.amazon.com/medialive/latest/ug/input-create-rtmp-push.html)

This section describes how to set up an upstream system that uses the RTMP Push protocol to deliver source content from the public internet.

- [Step 1: Obtain information](https://docs.aws.amazon.com/medialive/latest/ug/setup-rtmp-push-obtain-info.html): Obtain the following information from your contact person at the upstream system:
- [Step 2: Create input security group](https://docs.aws.amazon.com/medialive/latest/ug/setup-isg-rtmp.html): You must create an input security group.
- [Step 3: Create input](https://docs.aws.amazon.com/medialive/latest/ug/setup-input-rtmp-push.html): After you have created the input security group, you can create the RTMP push input.
- [Step 4: Set up upstream system](https://docs.aws.amazon.com/medialive/latest/ug/setup-uss-rtmp-push.html): You must make sure that the upstream system pushes content to the correct locations in MediaLive.
- [Result of this procedure](https://docs.aws.amazon.com/medialive/latest/ug/setup-result-rtmp-push.html): As a result of this setup, an RTMP push input exists that specifies one or two endpoint URLs.

### [RTMP VPC input](https://docs.aws.amazon.com/medialive/latest/ug/rtmp-push-vpc-input.html)

This section describes how to set up content that uses the RTMP Push protocol to deliver source content from an upstream system that is in your VPC from Amazon Virtual Private Cloud (Amazon VPC).

- [Step 1: Set up VPC](https://docs.aws.amazon.com/medialive/latest/ug/setup-vpc-rtmp-vpc.html): An Amazon VPC user must set up the VPC, and identify subnets and security groups that the upstream system and MediaLive will use.
- [Step 2: Create input](https://docs.aws.amazon.com/medialive/latest/ug/setup-input-rtmp-vpc.html): After the Amazon VPC user has set up on the VPC, you can create the RTMP VPC push input in MediaLive.
- [Step 3: Set up upstream system](https://docs.aws.amazon.com/medialive/latest/ug/setup-uss-rtmp-vpc.html): You must make sure that the upstream system sets up correctly with your VPC and pushes content to the correct locations in MediaLive.
- [Result of this procedure](https://docs.aws.amazon.com/medialive/latest/ug/setup-rtmp-vpc-result.html): As a result of this setup, an RTMP input exists that specifies one or two endpoint URLs.

### [RTP push input](https://docs.aws.amazon.com/medialive/latest/ug/input-create-rtp-push.html)

This section describes how to set up an upstream system that uses the RTP Push protocol to deliver source content from an upstream system that is in your VPC from Amazon VPC.

- [Step 1: Obtain information](https://docs.aws.amazon.com/medialive/latest/ug/setup-rtp-push-obtain-info.html): Obtain the following information from your contact person at the upstream system:
- [Step 2: Create an input security group](https://docs.aws.amazon.com/medialive/latest/ug/setup-isg-rtp-push.html): You must create an input security group.
- [Step 3: Create input](https://docs.aws.amazon.com/medialive/latest/ug/setup-input-rtp-push.html): After you have created the input security group, you can create the RTP push input.
- [Step 4: Set up upstream system](https://docs.aws.amazon.com/medialive/latest/ug/setup-uss-rtp-push.html): You must make sure that the upstream system pushes content to the correct locations in MediaLive.
- [Result of this procedure](https://docs.aws.amazon.com/medialive/latest/ug/setup-result-rtp-push.html): As a result of this setup, an RTP input exists that specifies one or two endpoint URLs.

### [RTP VPC input](https://docs.aws.amazon.com/medialive/latest/ug/rtp-push-vpc-input.html)

This section describes how to set up an upstream system that uses the RTP Push protocol to deliver source content from an upstream system that is in your Amazon Virtual Private Cloud (Amazon VPC).

- [Step 1: Set up VPC](https://docs.aws.amazon.com/medialive/latest/ug/setup-vpc-rtp-vpc.html): An Amazon VPC user must set up the VPC, and identify subnets and security groups that the upstream system and MediaLive will use.
- [Step 2: Create input](https://docs.aws.amazon.com/medialive/latest/ug/setup-input-rtp-vpc.html): After the Amazon VPC user has set up on the VPC, you can create the RTP VPC push input in MediaLive.
- [Step 3: Set up upstream system](https://docs.aws.amazon.com/medialive/latest/ug/setup-uss-rtp-vpc.html): You must make sure that the upstream system sets up correctly with your VPC and pushes content to the correct locations in MediaLive.
- [Result of this procedure](https://docs.aws.amazon.com/medialive/latest/ug/setup-rtp-vpc-result.html): As a result of this setup, an RTP input exists that specifies one or two endpoint URLs.

### [SMPTE 2110 input](https://docs.aws.amazon.com/medialive/latest/ug/input-create-s2110.html)

This section describes how to set up the source content on the upstream system, and how to create an SMPTE 2110 input that connects the upstream system to MediaLive.

- [Step 1: Obtain information](https://docs.aws.amazon.com/medialive/latest/ug/setup-s2110-pull-obtain-info.html): Obtain the following information from the video engineer who created the SMPTE 2110 SDP files:
- [Step 2: Create input](https://docs.aws.amazon.com/medialive/latest/ug/setup-input-s2110-pull.html): After you have obtained information from the upstream system, you can create a SMPTE 2110 input.

### [SRT Caller input](https://docs.aws.amazon.com/medialive/latest/ug/input-caller-srt.html)

Learn how to set up AWS Elemental MediaLive to ingest a transport stream (TS) that is sent from an upstream system that is set up as an SRT listener.

- [Step 1: Get ready](https://docs.aws.amazon.com/medialive/latest/ug/input-caller-srt-prereqs.html): Learn about the information that you must collect prior to setting up an SRT input in an AWS Elemental MediaLive channel.
- [Step 2: Set up the input](https://docs.aws.amazon.com/medialive/latest/ug/input-caller-srt-setup.html): Learn about how to set up an AWS Elemental MediaLive channel to include an SRT input.
- [Step 3: Set up upstream](https://docs.aws.amazon.com/medialive/latest/ug/setup-uss-srt-caller.html): An operator at the upstream server must set up the source content on the upstream system.
- [Step 4: Result of this procedure](https://docs.aws.amazon.com/medialive/latest/ug/input-caller-srt-result.html): As a result of this setup, an SRT caller input exists that specifies one or two source URLs.

### [SRT Listener input](https://docs.aws.amazon.com/medialive/latest/ug/input-listener-srt.html)

Learn how to set up AWS Elemental MediaLive to receive a transport stream (TS) that is pushed from an upstream system that is set up as an SRT caller.

- [Step 1: Get ready](https://docs.aws.amazon.com/medialive/latest/ug/input-listener-srt-prereqs.html): Learn about the information that you must collect prior to setting up an SRT Listener input in an AWS Elemental MediaLive channel.
- [Step 2: Set up the input](https://docs.aws.amazon.com/medialive/latest/ug/input-listener-srt-setup.html): Learn about how to set up an AWS Elemental MediaLive channel to include an SRT Listener input.
- [Step 3: Provide information to upstream](https://docs.aws.amazon.com/medialive/latest/ug/setup-uss-srt-listener.html): After you create the SRT Listener input, you must provide connection information to the operator at the upstream system so they can configure their SRT caller to connect to MediaLive.
- [Step 4: Result of this procedure](https://docs.aws.amazon.com/medialive/latest/ug/input-listener-srt-result.html): As a result of this setup, an SRT Listener input exists with one or two destination URLs.
- [Network locations](https://docs.aws.amazon.com/medialive/latest/ug/input-listener-srt-network-locations.html): SRT Listener inputs support the following network locations:
- [TS file input](https://docs.aws.amazon.com/medialive/latest/ug/ts-file-input.html): This section describes how to set up to ingest transport stream (TS) content that is stored as a file.
- [Next steps](https://docs.aws.amazon.com/medialive/latest/ug/input-create-nextsteps.html): After you have created all the inputs that you need for a channel, you are ready to start creating the channel.


## [Setup: Creating a channel](https://docs.aws.amazon.com/medialive/latest/ug/creating-channel-scratch.html)

- [Getting ready](https://docs.aws.amazon.com/medialive/latest/ug/creating-a-channel-getready.html): We recommend that before you start creating the MediaLive channel, you plan the workflow.

### [Channel and input details](https://docs.aws.amazon.com/medialive/latest/ug/creating-a-channel-step1.html)

The Channel and input details section of the Create channel page lets you do the following in the MediaLive that you are creating:

- [IAM role and ARN](https://docs.aws.amazon.com/medialive/latest/ug/role-and-remember-arn.html): This section describes how to complete the IAM role section in the General info section of the Channel and input details pane.
- [Channel class](https://docs.aws.amazon.com/medialive/latest/ug/channel-class.html): When you planned the workflow, you decided whether to set up the MediaLive channel as a standard channel (with two pipelines) or a single-pipeline channel.
- [Input specifications settings](https://docs.aws.amazon.com/medialive/latest/ug/input-specification.html)

### [Inputs part 1: Attach inputs](https://docs.aws.amazon.com/medialive/latest/ug/creating-a-channel-step2.html)

Before you started to create the MediaLive channel, you should have created all of inputs for all the content sources for the channel.

- [The procedure](https://docs.aws.amazon.com/medialive/latest/ug/attach-inputs-procedure.html)
- [Channel inputâCDI VPC push input](https://docs.aws.amazon.com/medialive/latest/ug/input-cdi.html): To verify that the input is set up correctly, look at the Input destinations section.
- [Channel inputâElemental Link push input](https://docs.aws.amazon.com/medialive/latest/ug/input-elink.html): To view the status of the AWS Elemental Link hardware device for this input, look at the Details.
- [Channel inputâHLS pull input](https://docs.aws.amazon.com/medialive/latest/ug/input-hls-pull.html): To verify that the input is set up correctly, look at the Input sources section.
- [Channel inputâMediaConnect push input](https://docs.aws.amazon.com/medialive/latest/ug/input-mediaconnect-push.html): To verify that the input is set up correctly, look at the MediaConnect flows section.
- [Channel inputâMediaConnect Router input](https://docs.aws.amazon.com/medialive/latest/ug/input-mediaconnect-router.html): To verify that the input is set up and ready to use, look at the state section.
- [Channel inputâMP4 pull input](https://docs.aws.amazon.com/medialive/latest/ug/input-mp4-pull.html): To verify that the input is set up correctly, look at the Input destinations section.
- [Channel inputâRTMP pull input](https://docs.aws.amazon.com/medialive/latest/ug/input-rtmp-pull.html): To verify that the input is set up correctly, look at the Input destinations section.
- [Channel inputâRTMP push input](https://docs.aws.amazon.com/medialive/latest/ug/input-rtmp-push.html): Follow these guidelines to verify that the input is set up correctly.
- [Channel inputâRTP push input](https://docs.aws.amazon.com/medialive/latest/ug/input-rtp-push.html): Follow these guidelines to verify that the input is set up correctly.
- [Channel inputâSMPTE 2110 input](https://docs.aws.amazon.com/medialive/latest/ug/input-s2110-pull.html): To verify that the input is set up correctly, look at the SMPTE 2110 Receiver Group section.
- [Channel inputâSRT caller input](https://docs.aws.amazon.com/medialive/latest/ug/input-srt-pull.html): To verify that the input is set up correctly, look at the SRT caller settings section.
- [Channel inputâSRT listener input](https://docs.aws.amazon.com/medialive/latest/ug/input-srt-push.html): Follow these guidelines to verify that the input is set up correctly.

### [Inputs part 2: Configure inputs](https://docs.aws.amazon.com/medialive/latest/ug/creating-a-channel-step2a.html)

As soon as you attach the input on the Attach input sections, the Input attachment section closes and the General input settings section appears for that input.

- [Input settingsâNetwork input settings](https://docs.aws.amazon.com/medialive/latest/ug/input-network-input.html): The fields in the Network input settings section apply only to HLS inputs and multicast inputs.
- [Input settingsâOther settings](https://docs.aws.amazon.com/medialive/latest/ug/input-other-settings.html): The fields that are not within the Network input settings section apply to all inputs.
- [Input settingsâVideo selector](https://docs.aws.amazon.com/medialive/latest/ug/input-video-selector.html): This section lets you identify the video to extract from the input, and lets you enable the optional color space feature.
- [Input settingsâAudio selectors](https://docs.aws.amazon.com/medialive/latest/ug/input-audio-selectors.html): If you want to extract audio from the input, this section is required.
- [Input settingsâCaption selectors](https://docs.aws.amazon.com/medialive/latest/ug/input-caption-selectors.html): If you want to extract captions from the input or to specify an external file as the source of the captions, this section is required.
- [General settings](https://docs.aws.amazon.com/medialive/latest/ug/creating-a-channel-step3.html): The General settings section in the Create channel page lets you configure global settings and global features:
- [Outputs](https://docs.aws.amazon.com/medialive/latest/ug/creating-a-channel-step4.html): The Outputs section lets you create output groups in the channel.
- [Save channel](https://docs.aws.amazon.com/medialive/latest/ug/creating-a-channel-step9.html): You can save the channel only after you have configured and created everything that you need.
- [Next step](https://docs.aws.amazon.com/medialive/latest/ug/create-channel-nextstep.html): For your next step in creating a MediaLive channel, we recommend that you read the chapter about the channel schedule.


## [Setup: Creating output groups](https://docs.aws.amazon.com/medialive/latest/ug/medialive-outputs.html)

### [Archive output group](https://docs.aws.amazon.com/medialive/latest/ug/opg-archive.html)

Learn how to design and create an Archive output group in an AWS Elemental MediaLive channel.

- [Organize encodes](https://docs.aws.amazon.com/medialive/latest/ug/design-archive-package.html): An Archive output group can contain the following:
- [Coordinate with the downstream system](https://docs.aws.amazon.com/medialive/latest/ug/archive-op-origin-server-s3.html): The destination for an Archive output group is always in an Amazon S3 bucket.

### [Create output group](https://docs.aws.amazon.com/medialive/latest/ug/creating-archive-output-group.html)

You create the output group and its outputs when you create or edit a MediaLive channel.

### [Destination fields](https://docs.aws.amazon.com/medialive/latest/ug/archive-destinations.html)

The following fields configure the location and names of the Archive output files (the destination).

- [Design the path for the output destination](https://docs.aws.amazon.com/medialive/latest/ug/archive-about-destination-path.html)
- [Complete the fields on the console](https://docs.aws.amazon.com/medialive/latest/ug/archive-specify-destination.html)
- [Examples](https://docs.aws.amazon.com/medialive/latest/ug/archive-examples.html): These examples show how to set up the fields that relate to file locations.
- [Container fields](https://docs.aws.amazon.com/medialive/latest/ug/archive-container.html): The following fields relate to the packaging and delivery of the archive transport stream:
- [Stream (encode) fields](https://docs.aws.amazon.com/medialive/latest/ug/archive-streams.html): The following fields relate to the encoding of the video, audio, and captions streams (encodes) in the output.

### [CMAF Ingest output group](https://docs.aws.amazon.com/medialive/latest/ug/opg-cmafi.html)

Learn how to design and create a CMAFI Ingest output group and outputs in an AWS Elemental MediaLive channel.

- [Organize encodes into outputs](https://docs.aws.amazon.com/medialive/latest/ug/design-cmafi-package.html): A CMAF Ingest output group typically set up as a video ABR stack.
- [Obtain destination](https://docs.aws.amazon.com/medialive/latest/ug/downstream-system-cmafi-empv2.html)
- [Create output group](https://docs.aws.amazon.com/medialive/latest/ug/creating-cmafi-output-group.html): You create the output group and its outputs when you create or edit a MediaLive channel.

### [Frame capture output group](https://docs.aws.amazon.com/medialive/latest/ug/opg-framecapture.html)

Learn how to design and create a Frame capture output group in a MediaLive channel.

- [Organize encodes](https://docs.aws.amazon.com/medialive/latest/ug/design-framecapture-package.html): A Frame capture output group can contain the following:
- [Coordinate with downstream system](https://docs.aws.amazon.com/medialive/latest/ug/framecapture-op-origin-server-s3.html): The destination for a Frame capture output group is always in an Amazon S3 bucket.

### [Create output group](https://docs.aws.amazon.com/medialive/latest/ug/creating-framecapture-output-group.html)

You create the output group and its outputs when you create or edit a MediaLive channel.

- [Destination fields](https://docs.aws.amazon.com/medialive/latest/ug/framecapture-destinations.html): The following fields configure the location and names of the frame capture files (the destination).
- [Stream fields](https://docs.aws.amazon.com/medialive/latest/ug/output-settings-framecapture.html): By default, the output is set up with one video encode.

### [HLS output group](https://docs.aws.amazon.com/medialive/latest/ug/opg-hls.html)

Learn how to design and create an HLS output group and outputs in an AWS Elemental MediaLive channel.

- [Organize encodes into outputs](https://docs.aws.amazon.com/medialive/latest/ug/design-hls-package.html): An HLS output group is typically set up as a video ABR stack.

### [Coordinate with the downstream system](https://docs.aws.amazon.com/medialive/latest/ug/hls-opg-coordinate-dss.html)

The HLS output group in AWS Elemental MediaLive supports several types of downstream systems.

- [HLS to Amazon S3](https://docs.aws.amazon.com/medialive/latest/ug/origin-server-hls-s3.html): Follow this procedure if you determined that you will create an HLS output group with Amazon S3 as the destination.
- [HLS to MediaStore](https://docs.aws.amazon.com/medialive/latest/ug/origin-server-ems.html): Follow this procedure if you determined that you will create an HLS output group, with AWS Elemental MediaStore as the destination.
- [HLS to MediaPackage](https://docs.aws.amazon.com/medialive/latest/ug/origin-server-hls-emp.html): Follow this procedure if you determined that you will create an HLS output group, and will send to AWS Elemental MediaPackage over HTTPS.
- [HLS to MediaPackage v2](https://docs.aws.amazon.com/medialive/latest/ug/origin-server-hls-empv2.html): Follow this procedure if you determined that you will create an HLS output group, and will send to MediaPackage v2.
- [HLS to HTTP](https://docs.aws.amazon.com/medialive/latest/ug/origin-server-http.html): Follow this procedure if you determined that you will create an HLS output group with one of the following downstream systems as the destination:

### [Create output group](https://docs.aws.amazon.com/medialive/latest/ug/creating-hls-output-group.html)

You create the output group and its outputs when you create or edit a MediaLive channel.

### [Destination fields](https://docs.aws.amazon.com/medialive/latest/ug/hls-destinations.html)

The HLS output group in MediaLive supports several types of destinations.

### [Amazon S3](https://docs.aws.amazon.com/medialive/latest/ug/hls-destinations-s3.html)

When you planned the destinations for the HLS output group, you might have decided to send the output to Amazon S3.

- [Step 1: Design the path](https://docs.aws.amazon.com/medialive/latest/ug/hls-destinations-s3-design.html): Perform this step if you haven't yet designed the full destination path or paths.
- [Step 2: Complete the fields](https://docs.aws.amazon.com/medialive/latest/ug/hls-destinations-s3-specify.html): After you have designed the output names and destination paths, you can set up the HLS output group.

### [MediaStore](https://docs.aws.amazon.com/medialive/latest/ug/hls-destinations-ems.html)

When you planned the destinations for the HLS output group, you might have decided to send the output to MediaStore.

- [Step 1: Design the path](https://docs.aws.amazon.com/medialive/latest/ug/hls-destinations-ems-design.html): Perform this step if you haven't yet designed the full destination path or paths.
- [Step 2: Complete the fields](https://docs.aws.amazon.com/medialive/latest/ug/hls-specify-destination-ems.html): After you have designed the output names and destination paths, you can set up the HLS output group.

### [MediaPackage](https://docs.aws.amazon.com/medialive/latest/ug/hls-destinations-emp.html)

When you planned the output to MediaPackage, you might have decided to send the output by creating an HLS output group. (Or you might have decided to create a MediaPackage output group.)

### [Step 1: Design the path](https://docs.aws.amazon.com/medialive/latest/ug/hls-destinations-emp-design.html)

Perform this step if you haven't yet designed the full destination path or paths.

- [Information for MediaPackage](https://docs.aws.amazon.com/medialive/latest/ug/hls-destinations-emp-info.html): For standard MediaPackage, the two URLs for a channel look like these examples:
- [Information for MediaPackage v2](https://docs.aws.amazon.com/medialive/latest/ug/hls-destinations-emp-info-v2.html): For MediaPackage v2, the two URLs for a channel look like these examples:
- [Syntax for path](https://docs.aws.amazon.com/medialive/latest/ug/hls-syntax-emp.html): An HLS output always includes three categories of files:
- [Name modifier](https://docs.aws.amazon.com/medialive/latest/ug/hls-nameModifier-design-emp.html): Design the nameModifier portions of the file name.
- [Segment modifier](https://docs.aws.amazon.com/medialive/latest/ug/hls-segmentModifier-design-emp.html): Design the segmentModifiers portion of the destination path.
- [Step 2: Complete the fields](https://docs.aws.amazon.com/medialive/latest/ug/hls-specify-destination-emp.html): After you have designed the output names and destination paths, you can set up the HLS output group.
- [Standard MediaPackage example](https://docs.aws.amazon.com/medialive/latest/ug/hls-example-mediapackage.html): This example shows how to set up the destination fields if the downstream system for the HLS output group is standard MediaPackage.
- [MediaPackage v2 example](https://docs.aws.amazon.com/medialive/latest/ug/hls-example-mediapackage-v2.html): This example shows how to set up the destination fields if the downstream system for the HLS output group is standard MediaPackage.

### [HTTP server](https://docs.aws.amazon.com/medialive/latest/ug/hls-destinations-http.html)

When you planned the destinations for the HLS output group, you might have decided to send the output to an HTTP server.

- [Step 1: Design the path](https://docs.aws.amazon.com/medialive/latest/ug/hls-destinations-design-step.html): Perform this step if you haven't yet designed the full destination path or paths.
- [Step 2: Complete the fields](https://docs.aws.amazon.com/medialive/latest/ug/hls-specify-destination.html): The following fields configure the location and names of the HLS media and manifest files (the destination).
- [HTTP example](https://docs.aws.amazon.com/medialive/latest/ug/hls-example-most-downstreamsystems.html): This example shows how to set up the destination fields if the downstream system is an HTTPS server that uses basic PUT.
- [Akamai example](https://docs.aws.amazon.com/medialive/latest/ug/hls-example-akamai.html): This example shows how to set up the destination fields if the downstream system is an Akamai server.
- [Container fields](https://docs.aws.amazon.com/medialive/latest/ug/hls-container.html): The following fields configure the container in each output.
- [Custom manifest path fields](https://docs.aws.amazon.com/medialive/latest/ug/hls-custom-manifests.html): Inside the main manifest, there are paths to each child manifest.
- [Redundant manifest fields](https://docs.aws.amazon.com/medialive/latest/ug/hls-opg-redundant-manifest.html): MediaLive supports redundant manifests as specified in the HLS specification.
- [Stream (encode) fields](https://docs.aws.amazon.com/medialive/latest/ug/hls-streams-section.html): The following fields relate to the encoding of the video, audio, and captions encodes in each output.
- [Other fields](https://docs.aws.amazon.com/medialive/latest/ug/hls-other-features.html): Topics

### [MediaPackage output group](https://docs.aws.amazon.com/medialive/latest/ug/opg-mediapackage.html)

Learn how to design and create a MediaPackage output group and outputs in an AWS Elemental MediaLive channel.

- [Organize encodes into outputs](https://docs.aws.amazon.com/medialive/latest/ug/design-emp-hls-package.html): An MediaPackage output group is typically set up as a video ABR stack.
- [Coordinate with MediaPackage operator](https://docs.aws.amazon.com/medialive/latest/ug/origin-server-emp.html): You and the operator of the AWS Elemental MediaPackage service must agree about the destination for the output of your MediaPackage output group.

### [Create output group](https://docs.aws.amazon.com/medialive/latest/ug/creating-mediapackage-output-group.html)

When you planned the workflow for your channel, you might have determined that you want to include a MediaPackage output group. (Or you might have decided to use an HLS output group to deliver to MediaPackage.)

- [Stream (encode) fields](https://docs.aws.amazon.com/medialive/latest/ug/mediapackage-encode-packaging.html): The following fields relate to the encoding of the video, audio, and captions streams (encodes) in the output.
- [Result of this procedure](https://docs.aws.amazon.com/medialive/latest/ug/mediapackage-create-result.html): With a MediaPackage output group, you don't configure as many fields as you do with a regular HLS output group.

### [Microsoft Smooth output group](https://docs.aws.amazon.com/medialive/latest/ug/opg-mss.html)

Learn how to design and create a Microsoft Smooth output group and outputs in an AWS Elemental MediaLive channel.

- [Organize encodes into outputs](https://docs.aws.amazon.com/medialive/latest/ug/organize-mss-package.html): A Microsoft Smooth output group is typically set up as a video ABR stack.
- [Coordinate with the downstream system](https://docs.aws.amazon.com/medialive/latest/ug/origin-server-mss.html): You and the operator of the downstream system must agree about the destination for the output of the Microsoft Smooth output group.

### [Create output group](https://docs.aws.amazon.com/medialive/latest/ug/creating-smooth-output-group.html)

When you planned the workflow for your channel, you might have determined that you want to include a Microsoft Smooth output group.

- [Destination fields](https://docs.aws.amazon.com/medialive/latest/ug/smooth-destinations.html): The following fields configure the destination of each Microsoft Smooth output.
- [Container fields](https://docs.aws.amazon.com/medialive/latest/ug/smooth-container.html): The following fields configure the container in each output.
- [Stream (encode) fields](https://docs.aws.amazon.com/medialive/latest/ug/smooth-streams-section.html): The following fields relate to the encoding of the video, audio, and captions streams (encodes) in the output.
- [Other fields](https://docs.aws.amazon.com/medialive/latest/ug/mss-other-fields.html)

### [RTMP output group](https://docs.aws.amazon.com/medialive/latest/ug/opg-rtmp.html)

Learn how to design and create an RTMP output group in an AWS Elemental MediaLive channel.

- [Organize encodes](https://docs.aws.amazon.com/medialive/latest/ug/design-rtmp-package.html): An RTMP output group can contain the following:
- [Coordinate with the downstream system](https://docs.aws.amazon.com/medialive/latest/ug/origin-server-rtmp.html): You and the operator of the downstream system must agree about the destination for each output of the RTMP output group.

### [Create output group](https://docs.aws.amazon.com/medialive/latest/ug/creating-rtmp-output-group.html)

When you planned the workflow for your channel, you might have determined that you want to include an RTMP output group.

- [Destination fields](https://docs.aws.amazon.com/medialive/latest/ug/rtmp-destinations.html): The following fields configure the location and names of the RTMP output files (the destination).
- [Connection fields](https://docs.aws.amazon.com/medialive/latest/ug/rtmp-connection.html): The following fields configure the logic for reconnection attempts:
- [Streams (encode) fields](https://docs.aws.amazon.com/medialive/latest/ug/rtmp-streams.html): The following fields relate to the encoding of the video, audio, and captions streams (encodes) in the output.
- [Other fields](https://docs.aws.amazon.com/medialive/latest/ug/rtmp-other.html): The following field relates to implementing resiliency in an RTMP output:

### [SRT output group](https://docs.aws.amazon.com/medialive/latest/ug/opg-srt.html)

Learn how to design and create an SRT output group in an AWS Elemental MediaLive channel.

- [Connection mode selection](https://docs.aws.amazon.com/medialive/latest/ug/srt-connection-mode-selection.html): When you create an SRT output group, you must choose the connection mode for each output.
- [Organize encodes into outputs](https://docs.aws.amazon.com/medialive/latest/ug/design-srt-package.html): An SRT output group can contain the following:
- [Plan for delivery using Amazon VPC](https://docs.aws.amazon.com/medialive/latest/ug/srt-get-ready.html): You might set up the MediaLive channel for the SRT output to have output endpoints in Amazon Virtual Private Cloud (Amazon VPC).
- [Set up in AWS Secrets Manager](https://docs.aws.amazon.com/medialive/latest/ug/srt-output-encryption-asm.html): You must set up for the mandatory encryption of the SRT output.

### [Caller mode outputs](https://docs.aws.amazon.com/medialive/latest/ug/creating-srt-caller-output.html)

This section describes how to create SRT outputs in caller mode, where MediaLive initiates connections to downstream systems.

- [Coordinate with the downstream system](https://docs.aws.amazon.com/medialive/latest/ug/downstream-system-srt-caller.html): With an SRT output group, you can create more than one output, in order to deliver the same content to more than one downstream system.
- [Create caller mode output](https://docs.aws.amazon.com/medialive/latest/ug/creating-srt-caller-output-group.html): After you have designed the contents of the output and you have coordinated delivery of the output with the downstream system, you can create the SRT output in caller mode.
- [Provide information to the downstream system](https://docs.aws.amazon.com/medialive/latest/ug/srt-caller-info-to-downstream.html): The downstream system might need the source IP addresses of the one or two MediaLive streams, so that they can allow these addresses to connect to them.

### [Listener mode outputs](https://docs.aws.amazon.com/medialive/latest/ug/creating-srt-listener-output.html)

This section describes how to create SRT outputs in listener mode, where downstream systems initiate connections to MediaLive.

- [Prerequisites](https://docs.aws.amazon.com/medialive/latest/ug/srt-listener-prerequisites.html): Before you create SRT outputs in listener mode, you must complete the following prerequisites:
- [Create listener mode output](https://docs.aws.amazon.com/medialive/latest/ug/creating-srt-listener-output-group.html): After you have completed the prerequisites and coordinated with the downstream systems, you can create the SRT output in listener mode.
- [MediaLive Anywhere setup](https://docs.aws.amazon.com/medialive/latest/ug/srt-listener-emla-setup.html): If you are creating an SRT listener output on a MediaLive Anywhere channel, there are additional configuration requirements:
- [Provide connection information](https://docs.aws.amazon.com/medialive/latest/ug/srt-listener-provide-info.html): After you create the channel with SRT outputs in listener mode, you must provide connection information to the operators of the downstream systems so they can configure their SRT callers to connect to MediaLive.
- [Validation rules](https://docs.aws.amazon.com/medialive/latest/ug/srt-listener-validation.html): MediaLive enforces the following validation rules when you create or update SRT outputs in listener mode:
- [Stream (encode) fields](https://docs.aws.amazon.com/medialive/latest/ug/srt-streams.html): The fields in this section relate to the encoding of the video, audio, and captions streams (encodes) in the output.

### [UDP output group](https://docs.aws.amazon.com/medialive/latest/ug/opg-udp.html)

Learn how to design and create a UDP output group in an AWS Elemental MediaLive channel.

- [Organize encodes into outputs](https://docs.aws.amazon.com/medialive/latest/ug/design-udp-package.html): A UDP output group can contain the following:
- [Coordinate with the downstream system](https://docs.aws.amazon.com/medialive/latest/ug/downstream-system-udp.html): You and the operator of the downstream system must agree about the destination for each output of the UDP output group.

### [Create output group](https://docs.aws.amazon.com/medialive/latest/ug/creating-udp-output-group.html)

When you planned the workflow for your channel, you might have determined that you want to include a UDP output group.

- [UDP destination fields](https://docs.aws.amazon.com/medialive/latest/ug/udp-destinations.html): The following fields configure the destination of the output:
- [Fields for the UDP transport](https://docs.aws.amazon.com/medialive/latest/ug/udp-container.html): The following fields configure the transport in each output:
- [Stream (encode) fields](https://docs.aws.amazon.com/medialive/latest/ug/udp-streams.html): The following fields relate to the encoding of the video, audio, and captions streams (encodes) in the output.
- [Other fields](https://docs.aws.amazon.com/medialive/latest/ug/udp-other.html): The following field relates to implementing resiliency in a UDP output:


## [Setup: Creating output encodes](https://docs.aws.amazon.com/medialive/latest/ug/container-output-encodes.html)

### [Set up video](https://docs.aws.amazon.com/medialive/latest/ug/creating-a-channel-step6.html)

Learn about the general procedure for creating video encodes in outputs in an AWS Elemental MediaLive channel.

- [Creating from scratch](https://docs.aws.amazon.com/medialive/latest/ug/create-video-scratch.html): Learn how to create video encodes from scratch in an AWS Elemental MediaLive channel.
- [Creating from scratch in Frame capture output](https://docs.aws.amazon.com/medialive/latest/ug/create-video-scratch-framecapture.html): Learn how to create a video encode from scratch in a Frame capture output in an AWS Elemental MediaLive channel.
- [Creating by sharing](https://docs.aws.amazon.com/medialive/latest/ug/create-video-share.html): Learn how to create one video encode and share it among several outputs in an AWS Elemental MediaLive channel.
- [Creating by cloning](https://docs.aws.amazon.com/medialive/latest/ug/create-video-clone.html): Learn how to create an AWS Elemental MediaLive video encode by cloning an existing video encode.

### [Set up audio](https://docs.aws.amazon.com/medialive/latest/ug/creating-a-channel-step7.html)

Learn about the general procedure for creating audio encodes in outputs in an AWS Elemental MediaLive channel.

- [Creating from scratch](https://docs.aws.amazon.com/medialive/latest/ug/create-audio-scratch.html): Learn how to create an audio encode from scratch in an AWS Elemental MediaLive channel.
- [Creating by sharing](https://docs.aws.amazon.com/medialive/latest/ug/create-audio-share.html): Learn how to create one audio encode and share it among several outputs in an AWS Elemental MediaLive channel.
- [Creating by cloning](https://docs.aws.amazon.com/medialive/latest/ug/create-audio-clone.html): Learn how to create an AWS Elemental MediaLive audio encode by cloning an existing audio encode.

### [Set up captions](https://docs.aws.amazon.com/medialive/latest/ug/creating-a-channel-step8.html)

Learn about the general procedure for creating captions encodes in outputs in an AWS Elemental MediaLive channel.

- [Creating from scratch](https://docs.aws.amazon.com/medialive/latest/ug/create-captions-scratch.html): Learn how to create a captions encode from scratch in an AWS Elemental MediaLive channel.
- [Creating by sharing](https://docs.aws.amazon.com/medialive/latest/ug/create-captions-share.html): Learn how to create one captions encode and share it among several outputs in an AWS Elemental MediaLive channel.
- [Creating by cloning](https://docs.aws.amazon.com/medialive/latest/ug/create-captions-clone.html): Learn how to create an AWS Elemental MediaLive captions encode by cloning an existing captions encode.
- [Next step](https://docs.aws.amazon.com/medialive/latest/ug/create-encodes-nextstep.html): Learn about your next steps after you have created all the output groups, outputs, and output encodes, you are ready to save the channel.


## [Setup: Creating a schedule](https://docs.aws.amazon.com/medialive/latest/ug/working-with-schedule.html)

- [Types of actions](https://docs.aws.amazon.com/medialive/latest/ug/x-actions-in-schedule.html): The schedule is a list of actions that a channel performs as it is running.
- [Types of timing](https://docs.aws.amazon.com/medialive/latest/ug/sched-timing-types.html): There are several ways to specify the timing for an action:

### [How actions work](https://docs.aws.amazon.com/medialive/latest/ug/sched-how-actions-work.html)

This section describes how MediaLive handles each combination of action type and start type.

- [Input switches](https://docs.aws.amazon.com/medialive/latest/ug/x-actions-in-schedule-ips.html): You can set up an action to switch the input that the running channel is ingesting.
- [Input prepare](https://docs.aws.amazon.com/medialive/latest/ug/x-actions-in-schedule-prep.html): You can set up an action to prepare an input that is associated with an immediate input switch, in order to reduce the delay that occurs when MediaLive performs the switch.
- [Image overlay](https://docs.aws.amazon.com/medialive/latest/ug/x-actions-in-schedule-image-overlay.html): You can set up an action to insert and remove an image overlay on the video:
- [Motion graphics overlay](https://docs.aws.amazon.com/medialive/latest/ug/x-actions-in-schedule-mg.html): You can set up an action to insert and remove a motion graphics overlay on the video:
- [SCTE 35](https://docs.aws.amazon.com/medialive/latest/ug/x-actions-in-schedule-SCTE35.html): You can set up an action to insert a SCTE 35 message in the channel.
- [ID3 metadata](https://docs.aws.amazon.com/medialive/latest/ug/x-actions-in-schedule-id3.html): You can set up an action to insert ID3 data in the channel.
- [ID3 segment tag](https://docs.aws.amazon.com/medialive/latest/ug/x-actions-in-schedule-id3-segment-tag.html): You can set up an action to insert ID3 data in each segment in the following types of outputs:
- [Pause and unpause](https://docs.aws.amazon.com/medialive/latest/ug/x-actions-in-schedule-pause.html): You can insert an action to pause and unpause one or both pipelines in the channel.

### [Working with the schedule (console)](https://docs.aws.amazon.com/medialive/latest/ug/schedule-using-console.html)

You can use the AWS Elemental MediaLive console to create or delete any of the schedule actions in a channel.

### [Creating actions](https://docs.aws.amazon.com/medialive/latest/ug/schedule-using-console-create.html)

You can create different actions in the schedule.

- [Input switch](https://docs.aws.amazon.com/medialive/latest/ug/schedule-fields-for-ips.html): This section describes how to complete the fields for these three types of input switches:
- [Input prepare](https://docs.aws.amazon.com/medialive/latest/ug/schedule-fields-for-input-prep.html): This section describes how to complete the fields for these three types of input prepares:
- [Activate global image overlay](https://docs.aws.amazon.com/medialive/latest/ug/schedule-fields-for-activate-image.html): This table shows the fields that apply for an action to activate an image overlay.
- [Deactivate global image overlay](https://docs.aws.amazon.com/medialive/latest/ug/schedule-fields-for-deactivate-image.html): This table shows the fields that apply for an action to deactivate an image overlay.
- [Activate per-outputs image overlay](https://docs.aws.amazon.com/medialive/latest/ug/schedule-fields-activate-image-per-output.html): This table shows the fields that apply for an action to activate an image overlay.
- [Deactivate per-outputs image overlay](https://docs.aws.amazon.com/medialive/latest/ug/schedule-fields-deactivate-image-per-output.html): This table shows the fields that apply for an action to deactivate the image.
- [Activate motion graphics overlay](https://docs.aws.amazon.com/medialive/latest/ug/schedule-fields-for-mg.html): This table shows the fields that apply for an action to activate a motion graphics overlay.
- [Deactivate motion graphics overlay](https://docs.aws.amazon.com/medialive/latest/ug/schedule-fields-for-mg-deactivate.html): This table shows the fields that apply for an action to deactivate an motion graphics overlay.
- [Splice_insert](https://docs.aws.amazon.com/medialive/latest/ug/schedule-fields-for-splice_insert.html): This table shows the fields that apply for an action to insert a splice_insert SCTE 35 message.
- [Time_signal](https://docs.aws.amazon.com/medialive/latest/ug/schedule-fields-for-time-signal.html): This table shows the fields that apply for an action to insert a time_signal SCTE 35 message.
- [Return-to-network](https://docs.aws.amazon.com/medialive/latest/ug/schedule-fields-for-return-to-network.html): This table shows the fields that apply for an action to insert a return-to-network SCTE 35 message.
- [ID3 metadata](https://docs.aws.amazon.com/medialive/latest/ug/schedule-fields-for-id3-userdata.html): This table shows the fields that apply for an action to perform a one-time insertion of ID3 metadata.
- [ID3 segment tags](https://docs.aws.amazon.com/medialive/latest/ug/schedule-fields-for-id3-segment-tags.html): This table shows the fields that apply for an action to insert ID3 metadata in every segment.
- [Pause](https://docs.aws.amazon.com/medialive/latest/ug/schedule-fields-for-pause.html): In Schedule action settings, complete the following fields.
- [Unpause](https://docs.aws.amazon.com/medialive/latest/ug/schedule-fields-for-unpause.html): In Schedule action settings, complete the following fields.
- [Deleting actions](https://docs.aws.amazon.com/medialive/latest/ug/schedule-using-console-delete.html): These rule apply when you add delete actions to the schedule:
- [Modifying actions](https://docs.aws.amazon.com/medialive/latest/ug/schedule-modify.html): You can't modify an action in the schedule, even if it hasn't been received by the channel.
- [Viewing the schedule](https://docs.aws.amazon.com/medialive/latest/ug/schedule-using-console-view.html): You can display the list of actions currently in the schedule and view them in list or timeline view.

### [Working with the schedule (AWS CLI)](https://docs.aws.amazon.com/medialive/latest/ug/schedule-using-cli.html)

You can use the AWS CLI to work with the schedule programmatically.

### [Update batch command](https://docs.aws.amazon.com/medialive/latest/ug/about-batch-update-schedule.html)

To create and delete actions in the schedule for a channel, you use the batch update schedule command.

- [How a batch request works](https://docs.aws.amazon.com/medialive/latest/ug/how-batch-schedule-requests-work.html): The intention of batching is to pass or fail all the actions together.
- [Batch command in different interfaces](https://docs.aws.amazon.com/medialive/latest/ug/batchupdatecommand-interfaces.html): The batch update schedule command is represented differently in different interfaces:
- [JSON payload in different interfaces](https://docs.aws.amazon.com/medialive/latest/ug/batchupdatecommand-payloads.html): The JSON payload for the command is different for the different interfaces:
- [Submitting a command](https://docs.aws.amazon.com/medialive/latest/ug/submitting-batch-command.html): The command for a batch update schedule command is identical for creating actions, deleting actions, or submitting a combination of create and delete actions.

### [JSON for create actions](https://docs.aws.amazon.com/medialive/latest/ug/schedule-create-json.html)

The following sections show the structure of the payload and an example of the payload for every type of create action for a MediaLive schedule.

- [Input switch action](https://docs.aws.amazon.com/medialive/latest/ug/cli-schedule-fields-for-input-switch.html): The following sections show the payload for input switch actions.
- [Input prepare action](https://docs.aws.amazon.com/medialive/latest/ug/cli-schedule-fields-for-input-prep.html): The following sections show the payload for input switch actions.
- [Activate global image action](https://docs.aws.amazon.com/medialive/latest/ug/cli-schedule-fields-for-activate-image.html): For information about the meaning and values for the fields in the following JSON, see .
- [Deactivate global overlay action](https://docs.aws.amazon.com/medialive/latest/ug/cli-schedule-fields-for-deactivate-image.html): For information about the meaning and values for the fields in the following JSON, see .
- [Activate per-outputs image action](https://docs.aws.amazon.com/medialive/latest/ug/cli-schedule-fields-for-activate-image-per-output.html): For information about the meaning and values for the fields in the following JSON, see .
- [Deactivate overlay action](https://docs.aws.amazon.com/medialive/latest/ug/cli-schedule-fields-for-deactivate-image-per-output.html): For information about the meaning and values for the fields in the following JSON, see .
- [Activate motion graphic overlay](https://docs.aws.amazon.com/medialive/latest/ug/cli-schedule-fields-activate-mgi.html): For information about the meaning and values for the fields in the following JSON, see .
- [Deactivate motion graphic overlay](https://docs.aws.amazon.com/medialive/latest/ug/cli-schedule-fields-deactivate-mgi.html): For information about the meaning and values for the fields in the following JSON, see .
- [Splice_insert message](https://docs.aws.amazon.com/medialive/latest/ug/cli-schedule-fields-for-splice-insert.html): For information about the meaning and values for the fields in the following JSON, see .
- [Time_signal message](https://docs.aws.amazon.com/medialive/latest/ug/cli-schedule-fields-for-time-signal.html): For information about the meaning and values for the fields in the following JSON, see .
- [Return-to-network message](https://docs.aws.amazon.com/medialive/latest/ug/cli-schedule-fields-for-return-network.html): For information about the meaning and values for the fields in the following JSON, see .
- [ID3 metadata item](https://docs.aws.amazon.com/medialive/latest/ug/cli-schedule-fields-for-id3.html): For information about the meaning and values for the fields in the following JSON, see .
- [ID3 segment tag item](https://docs.aws.amazon.com/medialive/latest/ug/cli-schedule-fields-id3-segment-tag.html): For information about the meaning and values for the fields in the following JSON, see .
- [Pause pipeline action](https://docs.aws.amazon.com/medialive/latest/ug/cli-schedule-fields-for-pause.html): For information about the meaning and values for the fields in the following JSON, see .
- [Combination of create actions](https://docs.aws.amazon.com/medialive/latest/ug/cli-example-multiple-creates.html): Here is an example of a JSON body to pass into the --creates parameter of the batch-update-schedule AWS CLI command.
- [JSON for delete actions](https://docs.aws.amazon.com/medialive/latest/ug/cli-schedule-delete-json.html): In the Deletes section, include the list of actions to delete by entering an array of ActionNames.
- [JSON for combinations](https://docs.aws.amazon.com/medialive/latest/ug/schedule-create-and-delete-json.html): To combine a batch of creates and deletes, include both a Creates section and a Deletes section in the JSON payload.
- [Viewing the schedule](https://docs.aws.amazon.com/medialive/latest/ug/viewing-schedule-using-cli.html): You can use the AWS CLI to view a list of the actions that are currently in the schedule for one channel:


## [Operations: Monitoring run-time activity](https://docs.aws.amazon.com/medialive/latest/ug/monitoring-channels.html)

### [Types of activity that can be monitored](https://docs.aws.amazon.com/medialive/latest/ug/monitor-activity-types.html)

Learn about the types of AWS Elemental MediaLive activity that you can monitor, and learn about the AWS services to use to monitor.

- [States for channels and multiplexes](https://docs.aws.amazon.com/medialive/latest/ug/monitor-activity-types-channel.html): Learn about the types of AWS Elemental MediaLive activity that you can monitor, and learn about the AWS services to use to monitor.
- [Alerts](https://docs.aws.amazon.com/medialive/latest/ug/monitor-activity-alerts.html): Learn about the alerts that AWS Elemental MediaLive can generate when a channel is running.
- [Metrics](https://docs.aws.amazon.com/medialive/latest/ug/monitor-activity-types-metrics.html): Learn about the types of AWS Elemental MediaLive activity that you can monitor, and learn about the AWS services to use to monitor.
- [Logs](https://docs.aws.amazon.com/medialive/latest/ug/monitor-activity-types-logs.html): Learn about the types of AWS Elemental MediaLive activity that you can monitor, and learn about the AWS services to use to monitor.
- [Alerts list - channels](https://docs.aws.amazon.com/medialive/latest/ug/monitor-activity-types-alerts-channels.html): Consult a list of the alerts that AWS Elemental MediaLive can generate when a channel is running.
- [Alerts list - multiplexes](https://docs.aws.amazon.com/medialive/latest/ug/monitor-activity-types-alerts-multiplex.html): Consult a list of the alerts that AWS Elemental MediaLive can generate when a multiplex is running.
- [Monitor from the console](https://docs.aws.amazon.com/medialive/latest/ug/monitoring-console-general.html): Learn about how to monitor activity on the AWS Elemental MediaLive console.
- [Monitor alerts with SDK or API](https://docs.aws.amazon.com/medialive/latest/ug/monitoring-api.html): Learn about how to programatically monitor alerts in AWS Elemental MediaLive.

### [Monitor with CloudWatch events](https://docs.aws.amazon.com/medialive/latest/ug/monitoring-via-cloudwatch.html)

Learn how to use Amazon CloudWatch Events to monitor AWS Elemental MediaLive.

- [JSON for a state change event](https://docs.aws.amazon.com/medialive/latest/ug/monitoring-cloudwatch-json-state-change.html): Learn how to use Amazon CloudWatch Events to monitor AWS Elemental MediaLive.
- [JSON for an alert event](https://docs.aws.amazon.com/medialive/latest/ug/monitoring-cloudwatch-json-alert.html): Learn how to use Amazon CloudWatch Events to monitor AWS Elemental MediaLive.
- [Option 1: Events for all channel](https://docs.aws.amazon.com/medialive/latest/ug/option-1.html): Learn how to send all AWS Elemental MediaLive events to an email address.
- [Option 2: Events for specific channels](https://docs.aws.amazon.com/medialive/latest/ug/option-2.html): Learn how to send specific AWS Elemental MediaLive events to an email address.

### [Monitor channels with metrics](https://docs.aws.amazon.com/medialive/latest/ug/monitoring-eml-metrics.html)

Learn how to use Amazon CloudWatch metrics to monitor AWS Elemental MediaLive.

- [Components of a metric](https://docs.aws.amazon.com/medialive/latest/ug/eml-metrics-gen-info.html): Learn some general tips about AWS Elemental MediaLive metrics.
- [Pricing](https://docs.aws.amazon.com/medialive/latest/ug/eml-metrics-pricing.html): There is no charge to view metrics on the Health tab of the MediaLive console.
- [Viewing metrics](https://docs.aws.amazon.com/medialive/latest/ug/eml-metrics-view.html): You can view some metrics in the MediaLive console.
- [Alphabetical list of MediaLive metrics](https://docs.aws.amazon.com/medialive/latest/ug/eml-metrics-alpha-list.html): View an alphabetical list of all AWS Elemental MediaLive metrics.
- [Global metrics](https://docs.aws.amazon.com/medialive/latest/ug/eml-metrics-global.html): Learn about metrics that relate to the general performance of AWS Elemental MediaLive.
- [Input metrics](https://docs.aws.amazon.com/medialive/latest/ug/eml-metrics-input-metrics.html): Learn about metrics that relate to inputs that AWS Elemental MediaLive works with.
- [MQCS metrics](https://docs.aws.amazon.com/medialive/latest/ug/eml-metrics-quality-score.html): Learn about metrics that related to MQCS (media quality confidence score) in AWS Elemental MediaLive.
- [Output metrics](https://docs.aws.amazon.com/medialive/latest/ug/eml-metrics-output-metrics.html): Learn about metrics that relate to AWS Elemental MediaLive outputs.
- [Pipeline locking metrics](https://docs.aws.amazon.com/medialive/latest/ug/eml-metrics-output-lock.html): Learn about metrics that relate to pipeline locking in AWS Elemental MediaLive.

### [CloudWatch Logs](https://docs.aws.amazon.com/medialive/latest/ug/monitoring-with-logs.html)

Learn how to use Amazon CloudWatch Logs to monitor AWS Elemental MediaLive activity.

- [About channel logs](https://docs.aws.amazon.com/medialive/latest/ug/monitoring-logs-about.html): Learn how to use Amazon CloudWatch Logsto monitor AWS Elemental MediaLive activity.
- [Enabling channel encoder logs](https://docs.aws.amazon.com/medialive/latest/ug/enabling-disabling-logs.html): Learn how to enable and disable AWS Elemental MediaLive channel encoder logs.
- [Working with logs](https://docs.aws.amazon.com/medialive/latest/ug/working-with-logs.html): Learn how to use Amazon CloudWatch Logs to view AWS Elemental MediaLive encoder logs.
- [CloudTrail logging](https://docs.aws.amazon.com/medialive/latest/ug/logging-using-cloudtrail.html): Learn how to use AWS CloudTrail to monitor AWS Elemental MediaLive activity.

### [Workflow monitor](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor.html)

Analyze AWS media services and create signal maps between those services.

### [Configuring workflow monitor](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure.html)

To setup workflow monitor for the first time; you create the alarm and event templates, and discover signal maps that are used to monitor your media workflows.

### [Getting started](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-getting-started.html)

The following steps provide a basic overview of using workflow monitor for the first time.

- [Workflow monitor IAM policies](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-getting-started-IAM.html): Workflow monitor interacts with multiple AWS services to create signal maps, build CloudWatch and EventBridge resources, and CloudFormation templates.

### [Templates](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-templates.html)

Learn how to configure the alarm and event templates that will be used to monitor your workflow.

### [CloudWatch alarms](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-alarms.html)

Learn how to configure the alarm groups and templates that will be used to monitor your workflow.

- [Recommended templates](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-alarms-recommended-templates.html): Learn how to use the recommended alarm templates created by AWS.
- [EventBridge rules](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-notifications.html): Learn how to configure the EventBridge groups and templates that will be used to monitor your workflow.

### [Signal maps](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-signal-maps.html)

Learn how to configure the workflow monitor signal maps.

- [Creating signal maps](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-signal-maps-create.html): Learn how to create the workflow monitor signal maps using the automatic discovery process.
- [Viewing signal maps](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-signal-maps-view.html): Workflow monitor signal maps allow you to see a visual mapping of all connected AWS resources in your media workflow.
- [Attaching templates](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-signal-maps-attach.html): After you have created alarm and event templates, you need to attach these to a signal map.
- [Deploying monitoring templates](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-deploy.html): After you have attached the alarm and event templates to your signal map, you must deploy the monitoring.
- [Updating signal maps](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-signal-maps-update.html): If a change is made to your workflow, you might need to rediscover the signal map and redeploy monitoring resources.
- [Deleting signal maps](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-signal-maps-delete.html): If you not longer need a signal map, it can be deleted.
- [Quotas](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-quotas.html): The following section contains quotas for workflow monitor resources.

### [Using workflow monitor](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-operate.html)

Use the overview and signal maps sections of the workflow monitor console to review the current status of the workflows and any associated alarms, metrics, and logs.

- [Overview](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-operate-overview.html): The Overview section of the workflow monitor console is a dashboard that provides at-a-glance information about your signal maps.
- [Logs and metrics](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-operate-logs-metrics.html): To view CloudWatch metrics and logs for a signal map, select the radio button next to the name of the signal map.
- [Using signal maps](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-operate-signal-maps.html): From the overview section of the console, you can select a specific signal map to view more information about that signal map and its attached monitoring resources.


## [Operations: Monitoring devices](https://docs.aws.amazon.com/medialive/latest/ug/monitoring-devices.html)

- [Device thumbnails](https://docs.aws.amazon.com/medialive/latest/ug/monitoring-link-device-thumbnails.html): Learn how to display thumbnails of the content that is currently being pushed to MediaLive by an AWS Elemental Link hardware device
- [Monitor devices with metrics](https://docs.aws.amazon.com/medialive/latest/ug/eml-metrics-input-devices.html): Learn how input device metrics for AWS Elemental MediaLive relate to Link devices.


## [Operations: Maintenance](https://docs.aws.amazon.com/medialive/latest/ug/maintenance.html)

- [Viewing information](https://docs.aws.amazon.com/medialive/latest/ug/viewing-maintenance.html): You can view maintenance information from the MediaLive console or from the Personal Health Dashboard in Health Dashboard.
- [Managing notifications](https://docs.aws.amazon.com/medialive/latest/ug/maintenance-setup-notifications.html): When a channel needs maintenance, you receive notification in the Health Dashboard, one notification for each channel.
- [Working with the event](https://docs.aws.amazon.com/medialive/latest/ug/setting-maintenance.html): You receive notification of upcoming maintenance for a channel at least 21 calendar days before the deadline for the maintenance.
- [Changing the maintenance window](https://docs.aws.amazon.com/medialive/latest/ug/set-maintenance-change-steps.html): There are two ways to change the maintenance window (red mark).
- [How MediaLive performs channel maintenance](https://docs.aws.amazon.com/medialive/latest/ug/maintenance-how.html): At some point during the maintenance window (red mark), MediaLive starts the maintenance.


## [Reference](https://docs.aws.amazon.com/medialive/latest/ug/reference.html)

### [Captions: Supported formats](https://docs.aws.amazon.com/medialive/latest/ug/supported-captions.html)

Obtain information about the caption formats that are supported in inputs, and the caption formats that are supported in outputs in AWS Elemental MediaLive.

- [Supported formats](https://docs.aws.amazon.com/medialive/latest/ug/general-information-supported-formats.html): The following table shows the formats that are supported in MediaLive.
- [Captions categories](https://docs.aws.amazon.com/medialive/latest/ug/categories-captions.html): Captions are grouped into five categories, based on how the captions are included in the output.
- [Reading the information](https://docs.aws.amazon.com/medialive/latest/ug/how-to-read-the-support-information.html): With captions, there are constraints on the ability to produce a specific output format from the input format.
- [Archive output](https://docs.aws.amazon.com/medialive/latest/ug/supported-formats-archive-output.html): In this table, look up your input container and captions type.
- [CMAF Ingest output](https://docs.aws.amazon.com/medialive/latest/ug/supported-formats-cmafi-output.html): In this table, look up your input container and captions type.
- [HLS or MediaPackage output](https://docs.aws.amazon.com/medialive/latest/ug/supported-formats-hls-output.html): In this table, look up your input container and captions type.
- [Microsoft Smooth output](https://docs.aws.amazon.com/medialive/latest/ug/supported-formats-smooth-output.html): In this table, look up your input container and captions type.
- [RTMP output](https://docs.aws.amazon.com/medialive/latest/ug/supported-formats-rtmp-output.html): In this table, look up your input container and captions type.
- [UDP, SRT, or multiplex output](https://docs.aws.amazon.com/medialive/latest/ug/supported-formats-ts-output.html): In this table, look up your input container and captions type.

### [Input types](https://docs.aws.amazon.com/medialive/latest/ug/inputs-supported-containers.html)

Obtain information about the types of media, audio codecs, and video codecs that AWS Elemental MediaLive can ingest.

- [Supported input types](https://docs.aws.amazon.com/medialive/latest/ug/inputs-supported-types.html): MediaLive supports the following input types.
- [Input types, protocols, upstream systems](https://docs.aws.amazon.com/medialive/latest/ug/inputs-supported-formats.html): The following table lists the input types that are supported in MediaLive, and describes how the input handles the source content.
- [Input deployments](https://docs.aws.amazon.com/medialive/latest/ug/inputs-emla.html): Inputs are categorized by the deployment mode of the channel that they are attached to:
- [Push and pull inputs](https://docs.aws.amazon.com/medialive/latest/ug/inputs-push-pull.html): When an input is being deployed in the AWS Cloud, it is categorized in terms of how MediaLive and the upstream system negotiate delivery:
- [Support for live and file sources](https://docs.aws.amazon.com/medialive/latest/ug/inputs-live-vs-file.html): A source might be a live source or a file (VOD) source:
- [Supported input class](https://docs.aws.amazon.com/medialive/latest/ug/inputs-single-standard-vpc.html): In MediaLive there are two kinds of class for inputs â standard class inputs and single-class inputs.
- [Support for setup as a VPC input](https://docs.aws.amazon.com/medialive/latest/ug/inputs-vpc-support.html): Some MediaLive inputs can be set up in Amazon Virtual Private Cloud (Amazon VPC).

### [Input codecs](https://docs.aws.amazon.com/medialive/latest/ug/inputs-supported-codecs.html)

Obtain information about the types of video codecs, and audio codecs that AWS Elemental MediaLive can ingest.

- [Supported codecs](https://docs.aws.amazon.com/medialive/latest/ug/inputs-supported-list.html): MediaLive supports the following video codecs in sources:
- [Supported codecs by input type](https://docs.aws.amazon.com/medialive/latest/ug/inputs-supported-codecs-by-input-type.html): The following table lists the video and audio codecs that each type of MediaLive input type supports.
- [Characteristics for sources](https://docs.aws.amazon.com/medialive/latest/ug/inputs-video-audio-characteristics.html): Orientation

### [Output types](https://docs.aws.amazon.com/medialive/latest/ug/supported-containers-output.html)

Obtain information about the media types, container types, video codecs, and audio codecs that AWS Elemental MediaLive supports in outputs.

- [Supported output types](https://docs.aws.amazon.com/medialive/latest/ug/outputs-supported-containers.html): MediaLive supports the following containers.
- [Containers, protocols, downstream systems](https://docs.aws.amazon.com/medialive/latest/ug/outputs-supported-containers-downstream-systems.html): The following table lists the output formats and protocols that MediaLive supports.
- [Support for delivery in VPC](https://docs.aws.amazon.com/medialive/latest/ug/outputs-support-vpc.html): The following table specifies which MediaLive containers can be delivered to a destination in the VPC, when the channel that is set up for VPC delivery.

### [Output codecs](https://docs.aws.amazon.com/medialive/latest/ug/supported-containers-and-codecs-output.html)

Obtain information about the video codecs, audio codecs, encoding schemes, and video resolutions that AWS Elemental MediaLive supports in outputs.

- [Supported codecs](https://docs.aws.amazon.com/medialive/latest/ug/outputs-list-codecs.html): MediaLive supports the following video codecs in outputs.
- [Supported codecs by output type](https://docs.aws.amazon.com/medialive/latest/ug/outputs-supported-codecs.html): The following table lists the video and audio codecs that each type of MediaLive output container (output group) supports.
- [AAC audio characteristics](https://docs.aws.amazon.com/medialive/latest/ug/aac-four-characteristics.html): This section explains how to set the following four properties of the AAC audio codec when you are setting up an audio encode in MediaLive:
- [Video encoding schemes by codec](https://docs.aws.amazon.com/medialive/latest/ug/video-characteristics-encoding-schemes.html): Topics
- [Video resolutions by codec](https://docs.aws.amazon.com/medialive/latest/ug/video-characteristics-resolution.html): In the following table, each row defines the video resolutions that apply to the terms SD, HD, and UHD.
- [Variable data: Supported identifiers](https://docs.aws.amazon.com/medialive/latest/ug/variable-data-identifiers.html): Obtain information about the variable data identifiers that AWS Elemental MediaLive supports.


## [Features of MediaLive](https://docs.aws.amazon.com/medialive/latest/ug/features.html)

- [Audio - Accessibility data](https://docs.aws.amazon.com/medialive/latest/ug/audio-accessibility.html): Learn how to include accessibility data in audio encodes in AWS Elemental MediaLive.

### [Audio â Audio-only outputs](https://docs.aws.amazon.com/medialive/latest/ug/audio-only.html)

Learn how to set up an AWS Elemental MediaLive channel with an output group that contains only audio.

- [Setting up on the input side](https://docs.aws.amazon.com/medialive/latest/ug/audio-only-inputs.html): Learn how to set up the input source in an audio-only output.
- [Setting up the output](https://docs.aws.amazon.com/medialive/latest/ug/audio-only-outputs-and-outputgroups.html): Learn how to set up outputs that contain only audio.
- [Setting up the encodes](https://docs.aws.amazon.com/medialive/latest/ug/audio-only-streams-and-encodes.html): Learn how to set up the the encodes in an audio-only output.
- [Audio â Dolby Digital Plus with Dolby Atmos](https://docs.aws.amazon.com/medialive/latest/ug/feature-dolbyatmos.html): Learn how to include Dolby Digital Plus with Dolby Atmos audio in an output.
- [Audio â Dolby E](https://docs.aws.amazon.com/medialive/latest/ug/feature-dolby-E-input.html): Learn how to set up MediaLive to ingest Dolby E audio that is wrapped in PCM.

### [Audio â audio rendition groups for HLS](https://docs.aws.amazon.com/medialive/latest/ug/audio-renditions.html)

Learn how to set up AWS Elemental MediaLive with an HLS output group that includes an audio rendition group.

- [About rendition groups](https://docs.aws.amazon.com/medialive/latest/ug/ARGs-about.html): View examples of audio rendition groups in HLS output group in AWS Elemental MediaLive.

### [Creating a rendition group](https://docs.aws.amazon.com/medialive/latest/ug/ARG-create.html)

Learn how to create audio rendition groups in an HLS output group in an AWS Elemental MediaLive channel.

- [Step 1: Identify encodes](https://docs.aws.amazon.com/medialive/latest/ug/ARG-step-create-mapping.html): Learn how to create audio rendition groups in an HLS output group in an AWS Elemental MediaLive channel.
- [Step 2: Determine Defaults](https://docs.aws.amazon.com/medialive/latest/ug/ARG-step-defaults.html): Learn how to create audio rendition groups in an HLS output group in an AWS Elemental MediaLive channel.
- [Step 3: Create video](https://docs.aws.amazon.com/medialive/latest/ug/ARG-step-create-video.html): Learn how to create audio rendition groups in an HLS output group in an AWS Elemental MediaLive channel.
- [Step 4: Create audio](https://docs.aws.amazon.com/medialive/latest/ug/ARG-step-create-audio.html): Learn how to create audio rendition groups in an HLS output group in an AWS Elemental MediaLive channel.
- [Summary](https://docs.aws.amazon.com/medialive/latest/ug/ARG-create-summary.html): Learn how to create audio rendition groups in an HLS output group in an AWS Elemental MediaLive channel.
- [Sample manifest](https://docs.aws.amazon.com/medialive/latest/ug/sample-manifest.html): View a typical manifest that AWS Elemental MediaLive produces for an HLS output that includes audio rendition groups.

### [Automatic input failover](https://docs.aws.amazon.com/medialive/latest/ug/automatic-input-failover.html)

When you set up the inputs for a MediaLive channel, you can set up inputs as an input failover pair (or failover pair).

- [Automatic input failover in a single-pipeline channel](https://docs.aws.amazon.com/medialive/latest/ug/aif-single-pipeline-how.html): You can implement automatic input failover (AIF) in a single-pipeline channel to protect the MediaLive channel from failure in the upstream system or the network connection that is upstream of MediaLive.
- [Automatic input failover in a standard channel](https://docs.aws.amazon.com/medialive/latest/ug/aif-standard-pipeline-how.html): You can implement automatic input failover in a standard MediaLive channel to protect the MediaLive channel from failure in the upstream system or the network connection that is upstream of MediaLive.
- [Setting up: CDI inputs](https://docs.aws.amazon.com/medialive/latest/ug/aif-setup-cdi.html): To use CDI inputs with automatic input failover in MediaLive, you must make sure that the upstream system provides sources in the correct way, and you must set up the inputs and the channels in a specific way.
- [Setting up: MediaConnect inputs](https://docs.aws.amazon.com/medialive/latest/ug/aif-setup-emx.html): To use MediaConnect inputs with automatic input failover, you must set up both the inputs and the MediaLive channels in a specific way.
- [Setting up: other inputs](https://docs.aws.amazon.com/medialive/latest/ug/aif-setup-other-inputs.html): To use RTMP push inputs and RTP inputs with automatic input failover in MediaLive, you must make sure that the upstream system provides sources in the correct way, and you must set up the inputs and the channels in a specific way.
- [Changing the roles of the failover pair](https://docs.aws.amazon.com/medialive/latest/ug/aif-setup-inverting.html): When you set up for input failover in a MediaLive channel, you can reverse the roles of the two failover inputs, so that the primary input becomes the secondary input.
- [Starting the channel](https://docs.aws.amazon.com/medialive/latest/ug/aif-behavior-startup.html): Start the MediaLive channel in the usual way.
- [Manually forcing a failover](https://docs.aws.amazon.com/medialive/latest/ug/aif-and-input-switching-failoverpair.html): You can set up automatic input failover to allow the MediaLive operator to perform a manual failover.
- [Automatic input failover and input switching](https://docs.aws.amazon.com/medialive/latest/ug/aif-and-input-switching.html): When you implement automatic input failover in MediaLive, you can still implement input switching.

### [Captions](https://docs.aws.amazon.com/medialive/latest/ug/captions.html)

Learn about setting up an AWS Elemental MediaLive channel to include captions in the outputs.

### [Supported features](https://docs.aws.amazon.com/medialive/latest/ug/captions-supported-features.html)

Learn about the different features of captions that AWS Elemental MediaLive supports.

- [Supported captions formats](https://docs.aws.amazon.com/medialive/latest/ug/supported-formats.html): Learn about the captions that AWS Elemental MediaLive can ingest from sources and produce in outputs.
- [Format support by output container](https://docs.aws.amazon.com/medialive/latest/ug/supported-format-outputs.html): Learn about the factors that control your ability to include captions of a specific format in outputs in an AWS Elemental MediaLive channel.
- [Constraints with OCR conversion](https://docs.aws.amazon.com/medialive/latest/ug/captions-languages-ocr.html): Learn about the constraints for using OCR conversion when converting source captions to output captions in an AWS Elemental MediaLive channel.
- [Support for multiple languages](https://docs.aws.amazon.com/medialive/latest/ug/support-for-languages.html): Learn about how AWS Elemental MediaLive can support multiple captions languages in the outputs in a channel.
- [Font styles in output captions](https://docs.aws.amazon.com/medialive/latest/ug/support-for-font-styles-in-output-captions.html): Learn about the different ways that you can configure font styling in output captions in an AWS Elemental MediaLive channel.

### [Typical scenarios](https://docs.aws.amazon.com/medialive/latest/ug/typical-scenarios.html)

Learn some typical scenarios for handling captions in an AWS Elemental MediaLive channel.

- [Use case A](https://docs.aws.amazon.com/medialive/latest/ug/use-case-one-input-format-to-one-output-format-not-converted.html): Learn about how to set up to pass through captions in an AWS Elemental MediaLive channel when the channel has one input and one output.
- [Use case B](https://docs.aws.amazon.com/medialive/latest/ug/use-case-one-input-format-to-different-output-formats.html): Learn about how to set up to convert captions in an AWS Elemental MediaLive channel when the channel has one input and one output.
- [Use case C](https://docs.aws.amazon.com/medialive/latest/ug/use-case-one-input-format-to-several-output-formats.html): Learn about how to set up to convert captions to different formats in different outputs in in an AWS Elemental MediaLive channel.
- [Use Case D](https://docs.aws.amazon.com/medialive/latest/ug/use-case-one-captions-output-multiple-video-encodes.html): Learn about how to set up for captions encode sharing in an AWS Elemental MediaLive channel.
- [Step 1: Set up inputs](https://docs.aws.amazon.com/medialive/latest/ug/identify-captions-in-the-input.html): Learn about how to create captions selectors in order to extract specific captions from the sources for an AWS Elemental MediaLive channel.
- [Step 2: Plan outputs](https://docs.aws.amazon.com/medialive/latest/ug/planning-captions-in-the-outputs.html): Learn how to plan the captions information for the outputs in an AWS Elemental MediaLive channel.
- [Step 3: Match formats](https://docs.aws.amazon.com/medialive/latest/ug/match-categories-captions.html): Learn about the correct procedure to follow to create captions encodes in the outputs in an AWS Elemental MediaLive channel.

### [Step 4: Set up outputs](https://docs.aws.amazon.com/medialive/latest/ug/create-captions-encodes.html)

Learn how to create captions encodes in the outputs in an AWS Elemental MediaLive channel.

- [Embedded or object captions encodes](https://docs.aws.amazon.com/medialive/latest/ug/output-embedded-and-more.html): Learn how create embedded or object captions encodes in the outputs in an AWS Elemental MediaLive channel.
- [Sidecar or SMPTE-TT captions encodes](https://docs.aws.amazon.com/medialive/latest/ug/output-sidecar-and-smptett-mss.html): Learn how create sidecar or SMPTE-TT captions encodes in the outputs in an AWS Elemental MediaLive channel.
- [Including accessibility data in captions in MediaLive](https://docs.aws.amazon.com/medialive/latest/ug/captions-accessibility.html): Learn how to include accessibility data in captions encodes in AWS Elemental MediaLive.

### [Details for specific output formats](https://docs.aws.amazon.com/medialive/latest/ug/captions-outputs-details-specific-formats.html)

Learn how create embedded or object captions encodes in the outputs in an AWS Elemental MediaLive channel.

- [Font styles for Burn-in or DVB-Sub](https://docs.aws.amazon.com/medialive/latest/ug/font-styles-for-burn-in.html): Learn about font styles for burn-in or DVB-Sub captions formats in AWS Elemental MediaLive.
- [PIDs for ARIB](https://docs.aws.amazon.com/medialive/latest/ug/complete-the-pids-for-arib.html): Learn about how to specify PIDs for ARIB captions in AWS Elemental MediaLive.
- [PIDs for DVB-Sub](https://docs.aws.amazon.com/medialive/latest/ug/complete-the-pids-for-dvb-sub.html): Learn about how to specify PIDs for DVB-Sub captions in AWS Elemental MediaLive.
- [PIDs for Teletext](https://docs.aws.amazon.com/medialive/latest/ug/complete-the-pids-for-teletext.html): Learn about how to specify PIDs for Teletext captions in AWS Elemental MediaLive.
- [Language information in HLS manifests](https://docs.aws.amazon.com/medialive/latest/ug/set-up-the-hls-manifest.html): Learn about how to include captions language information in the manifest in HLS outputs in AWS Elemental MediaLive.
- [Font styles for EBU-TT-D](https://docs.aws.amazon.com/medialive/latest/ug/ebu-tt-font-styles.html): Learn about how to specify font styles for EBU-TT-D captions in AWS Elemental MediaLive.
- [Font styles for TTML](https://docs.aws.amazon.com/medialive/latest/ug/ttml-font-styles.html): Learn about how to specify font styles for TTML captions in AWS Elemental MediaLive.
- [Font styles for WebVTT](https://docs.aws.amazon.com/medialive/latest/ug/webvtt-font-styles.html): Learn about how to pass through font style information for embedded or Teletext output captions in AWS Elemental MediaLive.

### [Examples of handling captions in MediaLive](https://docs.aws.amazon.com/medialive/latest/ug/examples.html)

Look at some examples for handling captions in AWS Elemental MediaLive.

- [Use case A](https://docs.aws.amazon.com/medialive/latest/ug/use-case-one-input-format-to-one-output.html): This example for captions in MediaLive shows how to implement the first use case from the typical scenarios.
- [Use case B](https://docs.aws.amazon.com/medialive/latest/ug/use-case-one-input-format-to-one-different-output-format.html): This example for captions in MediaLive shows how to implement the second use case from the typical scenarios.
- [Use case C](https://docs.aws.amazon.com/medialive/latest/ug/use-case-one-input-format-different-format-for-each-output.html): This example for captions in MediaLive shows how to implement the third use case from the typical scenarios.

### [Use case D](https://docs.aws.amazon.com/medialive/latest/ug/use-case-one-captions-output-shared-by-multiple-video-encode.html)

This example for captions in MediaLive shows how to set up captions in an ABR workflow.

- [Setup with Embedded or object-style captions](https://docs.aws.amazon.com/medialive/latest/ug/setup-with-procedure-a-captions.html): This example for captions in MediaLive shows how to implement the fourth use case from the typical scenarios.
- [Setup with sidecar captions](https://docs.aws.amazon.com/medialive/latest/ug/setup-with-procedure-b-captions.html): This example for captions in MediaLive shows an ABR workflow where the captions are in sidecars.
- [CDI inputs as partner inputs](https://docs.aws.amazon.com/medialive/latest/ug/feature-cdi-partner.html): Learn how to set up two CDI inputs as a set of partner CDI inputs.

### [Channel security groups](https://docs.aws.amazon.com/medialive/latest/ug/feature-channel-security-groups.html)

Learn how to use channel security groups to control inbound traffic to AWS Elemental MediaLive channel outputs.

- [About channel security groups](https://docs.aws.amazon.com/medialive/latest/ug/channel-security-groups-about.html): A channel security group allows you to control which IP addresses can connect to your MediaLive channel outputs.
- [When to use channel security groups](https://docs.aws.amazon.com/medialive/latest/ug/channel-security-groups-use-cases.html): Channel security groups are required in the following situations:
- [How channel security groups work](https://docs.aws.amazon.com/medialive/latest/ug/channel-security-groups-how-it-works.html): When you attach a channel security group to a channel, MediaLive performs the following actions:
- [Rules and constraints](https://docs.aws.amazon.com/medialive/latest/ug/channel-security-groups-rules.html): The following rules apply to channel security groups:

### [Setting up a channel security group](https://docs.aws.amazon.com/medialive/latest/ug/channel-security-groups-setup.html)

To use a channel security group, you must first have an input security group with the appropriate CIDR allow list rules.

- [Step 1: Create or identify an input security group](https://docs.aws.amazon.com/medialive/latest/ug/channel-security-groups-create-isg.html): Before you create the channel, you must have an input security group that contains the CIDR allow list rules for the downstream systems that will connect to your SRT outputs configured in listener mode.
- [Step 2: Attach the channel security group to the channel](https://docs.aws.amazon.com/medialive/latest/ug/channel-security-groups-attach.html): When you create a channel with SRT outputs in listener mode, you must attach a channel security group.

### [Managing channel security groups](https://docs.aws.amazon.com/medialive/latest/ug/channel-security-groups-manage.html)

After you have created a channel with a channel security group, you can view, update, or remove the channel security group.

- [Viewing channel security group details](https://docs.aws.amazon.com/medialive/latest/ug/channel-security-groups-view.html)
- [Updating or removing a channel security group](https://docs.aws.amazon.com/medialive/latest/ug/channel-security-groups-update.html): You can change which input security group is used as the channel security group, or you can remove the channel security group entirely.
- [Updating CIDR rules](https://docs.aws.amazon.com/medialive/latest/ug/channel-security-groups-update-rules.html): To update the CIDR allow list rules for a channel security group, you update the underlying input security group.
- [Class: Channel classes and input classes](https://docs.aws.amazon.com/medialive/latest/ug/class-channel-input.html): One of the characteristics of a MediaLive channel is its class.
- [Dynamic inputs](https://docs.aws.amazon.com/medialive/latest/ug/dynamic-inputs.html): You can use dynamic file inputs in a multiple-input MediaLive channel in order to increase the number of video sources that you can use in the channel, while still observing the limit on the number of inputs that you can attach to the channel.
- [Elemental inference](https://docs.aws.amazon.com/medialive/latest/ug/elemental-inference.html): AWS Elemental MediaLive includes features that are seamless implementations of the features of AWS Elemental Inference.
- [Event clipping](https://docs.aws.amazon.com/medialive/latest/ug/elemental-inference-event-clip.html)

### [ID3 metadata](https://docs.aws.amazon.com/medialive/latest/ug/id3-metadata.html)

Learn how to include metadata into ID3 metadata in Archive outputs, HLS outputs, MediaPackage outputs, and UDP outputs of an AWS Elemental MediaLive channel.

- [Different mechanisms for including metadata](https://docs.aws.amazon.com/medialive/latest/ug/id3-enable-result.html): You can include metadata in the following ways.
- [Passthrough](https://docs.aws.amazon.com/medialive/latest/ug/enable-passthrough-id3.html): You can set up one or more outputs in a MediaLive channel so that ID3 metadata that is in a source is automatically passed through to the output.
- [Inserting when creating channel](https://docs.aws.amazon.com/medialive/latest/ug/insert-timed-metadata.html): When you create or edit the channel, you can set up the following types of output groups so that MediaLive inserts a timestamp at a regular interval.
- [Inserting using schedule](https://docs.aws.amazon.com/medialive/latest/ug/insert-id3-metadata-via-schedule.html): You can create actions in the channel schedule to insert ID3 metadata in one or more outputs.

### [Image overlays](https://docs.aws.amazon.com/medialive/latest/ug/working-with-image-overlay.html)

You can impose static images onto a video in an AWS Elemental MediaLive channel.

- [Two options: global overlay and per-output overlay](https://docs.aws.amazon.com/medialive/latest/ug/image-overlay-features.html): There are two options for inserting and removing image overlays in a MediaLive channel â the global option and the per-output option.
- [Step 1: Prepare the image](https://docs.aws.amazon.com/medialive/latest/ug/image-overlay-prepare-step.html): You must prepare each image overlay that you want to use in your MediaLive channel, and store it in a suitable location, such as an Amazon S3 bucket.
- [Step 2: Handle encode sharing](https://docs.aws.amazon.com/medialive/latest/ug/image-overlay-encode-sharing.html): Read this section if you plan to use the per-output option to insert overlays in MediaLive outputs, and you have already set up output groups to use video encode sharing.
- [Step 3: Insert overlay](https://docs.aws.amazon.com/medialive/latest/ug/image-overlay-insert.html): When you are ready, you can create an action in the MediaLive channel schedule to activate (insert) the overlay.
- [Input clipping](https://docs.aws.amazon.com/medialive/latest/ug/input-clipping.html): You can clip a file input so that MediaLive ingests only a portion of the file.
- [Input loss handling](https://docs.aws.amazon.com/medialive/latest/ug/feature-input-loss.html): Learn how to customize how AWS Elemental MediaLive handles media when the input into a channel is lost.

### [Input prepare](https://docs.aws.amazon.com/medialive/latest/ug/feature-prepare-input.html)

You can prepare an AWS Elemental MediaLive input that is associated with an immediate input switch, in order to reduce the delay that occurs when MediaLive performs the switch.

- [Rules and limits](https://docs.aws.amazon.com/medialive/latest/ug/input-prep-rules.html)

### [Setting up input prepares](https://docs.aws.amazon.com/medialive/latest/ug/prepare-input-procedure.html)

Follow this procedure to add input prepare actions to the channel schedule, in order to prepare any input ahead of the switch action to that input.

- [Enabling the feature](https://docs.aws.amazon.com/medialive/latest/ug/input-prep-enable.html): Before you add input prepare actions to the MediaLive schedule, you must enable the feature.

### [Planning start](https://docs.aws.amazon.com/medialive/latest/ug/input-prep-plan-start.html)

Before you add an input prepare action to the schedule, decide on the start type for the action.

- [Types of starts](https://docs.aws.amazon.com/medialive/latest/ug/plan-prep-start-types.html): There are three start types for input prepare actions in MediaLive.
- [Guidelines for start type](https://docs.aws.amazon.com/medialive/latest/ug/plan-prep-tips.html): Following are some guidelines for deciding which start type to use with an input prepare in the MediaLive schedule.
- [Input prepare and dynamic inputs](https://docs.aws.amazon.com/medialive/latest/ug/input-prep-dynamic.html): You can prepare for an input switch in a MediaLive channel when the associated input is a dynamic input.
- [Input prepare with clipping](https://docs.aws.amazon.com/medialive/latest/ug/input-prep-clip.html): You can prepare for an input switch in a MediaLive channel when the associated input is a file input that includes input clipping.
- [Input prepare and automatic input failover](https://docs.aws.amazon.com/medialive/latest/ug/input-prep-aif.html): Your MediaLive channel might include some inputs that are set up as automatic input failover pairs.
- [Runtime behavior](https://docs.aws.amazon.com/medialive/latest/ug/input-prep-runtime.html): All prepare actions that you add to the MediaLive schedule sit in the schedule until the start time.
- [Modifying](https://docs.aws.amazon.com/medialive/latest/ug/input-prep-modify.html): For information on modifying an input prepare action that is in the MediaLive schedule, see .
- [Deleting and stopping](https://docs.aws.amazon.com/medialive/latest/ug/input-prep-delete.html): You can delete input prepare actions from the schedule.

### [Input switching](https://docs.aws.amazon.com/medialive/latest/ug/scheduled-input-switching.html)

You can set up an AWS Elemental MediaLive channel to ingest multiple sequential inputs, rather than setting it up to ingest only one input.

### [About input switching](https://docs.aws.amazon.com/medialive/latest/ug/ips-overview.html)

You set up input switching in a MediaLive channel in order to ingest the inputs in a multiple-input channel.

- [Multiple-input channels and the schedule](https://docs.aws.amazon.com/medialive/latest/ug/schedule-and-switching.html): Input switching in a MediaLive channel works as follows: You create a channel that contains more than one input attachment.
- [Typical use cases](https://docs.aws.amazon.com/medialive/latest/ug/typical-use-cases.html): Scheduled input switching in a MediaLive channel supports the following use cases.
- [Fixed, immediate, and follow switches](https://docs.aws.amazon.com/medialive/latest/ug/ips-switch-types.html): In MediaLive, you can categorize input switches according to the start types for the switch.
- [Dynamic inputs](https://docs.aws.amazon.com/medialive/latest/ug/how-dynamic-inputs-work.html): If your MediaLive channel includes files inputs, you should decide if you want to set up each input as a static input or as a dynamic input.
- [Input Prepare](https://docs.aws.amazon.com/medialive/latest/ug/ips-input-prepare.html): The MediaLive schedule includes an input prepare action that is a helper action for input switches.
- [Rules and limits](https://docs.aws.amazon.com/medialive/latest/ug/ips-limits.html): This section describes the rules and limits that apply to input switches in the MediaLive schedule.

### [Setting up for input switching](https://docs.aws.amazon.com/medialive/latest/ug/setup-ips.html)

When you plan for a MediaLive channel that includes multiple inputs that you will switch between, there are special requirements that you must consider.

- [Step 1: Plan outputs](https://docs.aws.amazon.com/medialive/latest/ug/ips-step-plan-outputs.html): Plan the output side of the MediaLive channel in the normal way:

### [Step 2: Assess sources](https://docs.aws.amazon.com/medialive/latest/ug/ips-step-plan-inputs.html)

When planning a multiple-input MediaLive channel, you must identify all the sources that you need.

- [Identify sources](https://docs.aws.amazon.com/medialive/latest/ug/ips-collect-sources.html)
- [Assess video](https://docs.aws.amazon.com/medialive/latest/ug/ips-assess-video.html): There are no special requirements for the video when planning a multiple-input MediaLivechannel.
- [Assess audio](https://docs.aws.amazon.com/medialive/latest/ug/ips-assess-audio.html): MediaLive provides flexibility in extracting audio from sources in a multiple-input MediaLive channel.
- [Assess captions](https://docs.aws.amazon.com/medialive/latest/ug/ips-assess-captions.html): There are special requirements for the captions in sources for a MediaLive multiple-input channel.
- [Step 3: Organize sources into inputs](https://docs.aws.amazon.com/medialive/latest/ug/ips-step-design-inputs.html): This section is a supplement to the information in .

### [Step 4: Design selectors for inputs](https://docs.aws.amazon.com/medialive/latest/ug/ips-step-plan-attachments.html)

After you follow step 3 to organize sources into different inputs and input types (static and dynamic), you must identify the content to extract from each MediaLive input.

- [Plan input names](https://docs.aws.amazon.com/medialive/latest/ug/ips-plan-input-names.html): You should plan the names for the input and the input attachment.
- [Plan video selectors](https://docs.aws.amazon.com/medialive/latest/ug/ips-plan-video-sels.html): You can extract only one video from each MediaLive input.
- [Plan audio selectors](https://docs.aws.amazon.com/medialive/latest/ug/ips-plan-audio-sels.html): There are several rules you must follow when planning the audio selectors for MediaLive inputs.
- [Plan captions selectors](https://docs.aws.amazon.com/medialive/latest/ug/ips-plan-captions-sels.html): When you set up the captions selectors for a MediaLive input, you specify both the format and the language to extract from the input.

### [Step 5: Plan input switches](https://docs.aws.amazon.com/medialive/latest/ug/ips-step-plan-switches.html)

After you design the selectors for each input (step 4), you must plan the order that you want MediaLive to follow when it ingests these inputs.

- [Plan action names](https://docs.aws.amazon.com/medialive/latest/ug/ips-plan-action-names.html): You should plan the names for the input switch action in the MediaLive schedule.
- [Plan order of switches](https://docs.aws.amazon.com/medialive/latest/ug/ips-order-switches.html): We recommend that you plan the order of the input switches before you create the actions in the MediaLive schedule.
- [Handling a fixed or immediate transition](https://docs.aws.amazon.com/medialive/latest/ug/ips-transition-gap.html): When planning the schedule, you should ensure that there is no gap when switching from a file input (input A) to an input (input B) that starts at a fixed time or that starts immediately.
- [Handling a follow transition](https://docs.aws.amazon.com/medialive/latest/ug/transition-follow-success.html): When planning the schedule, you should ensure that a switch from one input to a "follow input" can succeed.

### [Step 6: Create inputs and channel](https://docs.aws.amazon.com/medialive/latest/ug/ips-step-create-inputs-channel.html)

After you perform the planning in steps 1 to 5, you are ready to create the inputs and create the MediaLive channel.

- [Create the inputs](https://docs.aws.amazon.com/medialive/latest/ug/ips-create-inputs-tips.html): This section is a supplement to the information in .
- [Identify first input](https://docs.aws.amazon.com/medialive/latest/ug/ips-plan-first-input.html): Identify an input that you will set up as the first input in the list of input attachments for the MediaLive channel:
- [Create the channel](https://docs.aws.amazon.com/medialive/latest/ug/ips-create-channel-tips.html): This section is a supplement to the information in .
- [Step 7: Set up the schedule](https://docs.aws.amazon.com/medialive/latest/ug/ips-set-up-schedule.html): After you create the inputs and the channel (step 6), you must create actions in the MediaLive schedule to set up the input switches that you want.
- [Deleting actions from the schedule](https://docs.aws.amazon.com/medialive/latest/ug/ips-manage-schedule.html): You can delete input switch actions from the MediaLive schedule.
- [Starting and restarting the channel](https://docs.aws.amazon.com/medialive/latest/ug/ips-start-channel-multi-inputs.html): After you create the MediaLive channel and add actions to its schedule, you can start the channel.
- [KLV metadata](https://docs.aws.amazon.com/medialive/latest/ug/klv-metadata.html): Learn how to extract KLV metadata from an input and to pass it through in TS outputs in MediaLive.

### [Link](https://docs.aws.amazon.com/medialive/latest/ug/feature-elink.html)

Learn how to set up an AWS Elemental Link hardware device as a video source for an AWS Elemental MediaLive channel.

- [With a MediaLive input](https://docs.aws.amazon.com/medialive/latest/ug/elink-using.html): You can set up an HD device or a UHD device as the source for a MediaLive input.
- [With a MediaConnect flow](https://docs.aws.amazon.com/medialive/latest/ug/elink-using-flow.html): You can set up a UHD device as the source for a MediaConnect flow You can't set up an HD device for this usage.
- [Link devices and inputs](https://docs.aws.amazon.com/medialive/latest/ug/link-see.html): For an overview of AWS Elemental Link devices, see .
- [Low latency outputs](https://docs.aws.amazon.com/medialive/latest/ug/mediapackage-v2-low-latency.html): You can create a glass-to-glass low latency workflow that uses AWS Elemental MediaLive and AWS Elemental MediaPackage.

### [Manifests â custom HLS manifest paths](https://docs.aws.amazon.com/medialive/latest/ug/hls-manifest-paths.html)

When you create an HLS output group in a standard MediaLive channel, you can set up custom manifests.

- [Procedure](https://docs.aws.amazon.com/medialive/latest/ug/hls-custom-manifests-procedure.html): Customizing the manifest paths involves working with the following fields:
- [How manifests work](https://docs.aws.amazon.com/medialive/latest/ug/hls-manifests-how-work.html): The following sections describe how MediaLive handles manifest paths.
- [Rules for custom paths](https://docs.aws.amazon.com/medialive/latest/ug/hls-custom-paths-rules.html): After you have set up to customize the manifests in a MediaLive HLS output group, you should share the following rules with your contact person at the downstream system.
- [Guidance for setting up for custom paths](https://docs.aws.amazon.com/medialive/latest/ug/hls-custom-paths-guidance.html): The content in the customized path in an HLS output must be appropriate for the system that is downstream of MediaLive.
- [Examples of custom paths](https://docs.aws.amazon.com/medialive/latest/ug/hls-custom-paths-examples.html): Following are examples of the different ways that you might customize the manifests in a MediaLive HLS output group.

### [Manifests â Redundant HLS manifests](https://docs.aws.amazon.com/medialive/latest/ug/hls-redundant-manifests.html)

When you create an HLS output group in a standard MediaLive channel, you can enable redundant manifests.

- [Procedure](https://docs.aws.amazon.com/medialive/latest/ug/hls-rm-procedure.html): There are two parts to setting up redundant manifests in MediaLive HLS outputs.
- [The media contents of an HLS manifest](https://docs.aws.amazon.com/medialive/latest/ug/hls-rm-manifests-contents.html): When you set up redundant manifests in an HLS output, MediaLive changes the contents of the manifest.
- [Rules for most systems](https://docs.aws.amazon.com/medialive/latest/ug/hls-redundant-manif-most-systems.html): You can set up redundant manifests in a MediaLive HLS output group so long as the downstream system can work with specific rules.
- [Rules for Akamai](https://docs.aws.amazon.com/medialive/latest/ug/hls-redundant-manif-akamai.html): You can set up redundant manifests in a MediaLive HLS output group so long as the downstream system can work with specific rules.
- [Combining redundant manifests with other features](https://docs.aws.amazon.com/medialive/latest/ug/hls-redundant-manif-combine.html)
- [MediaLive Anywhere](https://docs.aws.amazon.com/medialive/latest/ug/feature-emla.html): Learn about the features that are available when you run a channel in a AWS Elemental MediaLive Anywhere cluster.
- [MQCS](https://docs.aws.amazon.com/medialive/latest/ug/mqcs.html): Learn about the MQCS (media quality confidence score) that AWS Elemental MediaLive generates for specific output groups.
- [Metadata](https://docs.aws.amazon.com/medialive/latest/ug/medialive-metadata.html): Read a list of metadata that AWS Elemental MediaLive supports.

### [Motion graphics overlay](https://docs.aws.amazon.com/medialive/latest/ug/feature-mgi.html)

Learn how to use the motion graphics overlay feature to superimpose a motion graphic onto the video in an AWS Elemental MediaLive channel.

- [Step 1: Prepare the motion graphic asset](https://docs.aws.amazon.com/medialive/latest/ug/mgi-prepare-asset.html): You use an authoring system to create the asset and to manage the content, including implementation of features such as fade or opacity.
- [Step 2: Enable the feature](https://docs.aws.amazon.com/medialive/latest/ug/mgi-prepare-channel.html): Perform this step for each MediaLive channel where you want to insert a motion graphic overlay.
- [Step 3: Insert the overlay](https://docs.aws.amazon.com/medialive/latest/ug/mgi-insert-overlay.html): When you are ready, you can create an action in the MediaLive channel schedule to activate (insert) the overlay.

### [Multiplex and MPTS](https://docs.aws.amazon.com/medialive/latest/ug/feature-multiplex.html)

You can set up a MediaLive multiplex to create a multi-program transport stream (MPTS).

- [Overview of multiplex and MPTS](https://docs.aws.amazon.com/medialive/latest/ug/mpts-general.html): A multi-program transport stream (MPTS) is a UDP transport stream (TS) that carries multiple programs.
- [Restrictions for multiplexes](https://docs.aws.amazon.com/medialive/latest/ug/mpts-limits.html): Following is a summary of the restrictions associated with multiplexes:
- [Setting up a multiplex](https://docs.aws.amazon.com/medialive/latest/ug/setting-up-multiplex.html): There are three components involved in an MPTS: a MediaLive multiplex, MediaLive programs, and MediaLive channels (and their attached MediaLive inputs).

### [Starting, pausing, or stopping a multiplex](https://docs.aws.amazon.com/medialive/latest/ug/start-pause-stop-multiplex.html)

At runtime, you start both the multiplex and the channels in the multiplex.

- [Summary of these actions](https://docs.aws.amazon.com/medialive/latest/ug/multiplex-start-stop-pause-summary.html): The following table summarizes the start, stop and pause capabilities for the multiplex, program, and channel.
- [Starting the multiplex](https://docs.aws.amazon.com/medialive/latest/ug/start-multiplex.html): To start streaming the MPTS, start the multiplex and the channels.
- [Pausing activity in the multiplex](https://docs.aws.amazon.com/medialive/latest/ug/pause-multiplex.title.html): You can't pause a multiplex.
- [Stopping activity in the multiplex](https://docs.aws.amazon.com/medialive/latest/ug/stop-multiplex.title.html): You can stop a multiplex or a channel.

### [Nielsen watermarks](https://docs.aws.amazon.com/medialive/latest/ug/feature-nielsen-watermark.html)

Learn how to configure an AWS Elemental MediaLive channel to insert Nielsen watermarks in the output.

- [Audio requirements](https://docs.aws.amazon.com/medialive/latest/ug/supportedaudio.html): Learn about the requirements for the source audio where you want to insert Nielsen watermarks using AWS Elemental MediaLive.
- [Get ready](https://docs.aws.amazon.com/medialive/latest/ug/nielsen-watermark-getready.html): Learn about the information you must obtain about Nielsen watermarks, before you configure an AWS Elemental MediaLive channel to insert Nielsen watermarks in the output.
- [Set up](https://docs.aws.amazon.com/medialive/latest/ug/watermark-procedure.html): Learn how to configure an AWS Elemental MediaLive channel to insert Nielsen watermarks in the output.
- [Nielsen watermarks to ID3](https://docs.aws.amazon.com/medialive/latest/ug/feature-nielsen-id3.html): You can configure an AWS Elemental MediaLive channel to convert Nielsen watermarks to ID3 metadata.

### [Pipeline locking (output locking)](https://docs.aws.amazon.com/medialive/latest/ug/pipeline-lock.html)

Learn how AWS Elemental MediaLive uses pipeline locking to ensure that outputs are frame accurate with each other.

- [Step 1: Verify the input](https://docs.aws.amazon.com/medialive/latest/ug/pipeline-locking-verify-input.html): Read about the characteristics that must apply to the channel content in order for AWS Elemental MediaLive to successfully lock the outputs in a standard channel.
- [Step 2: Configuring pipeline locking](https://docs.aws.amazon.com/medialive/latest/ug/pipeline-locking-set-up.html): Learn how to configure pipeline locking and epoch locking in a AWS Elemental MediaLive channel.
- [Troubleshooting](https://docs.aws.amazon.com/medialive/latest/ug/pipeline-locking-tshoot.html): Learn some tips for troubleshooting the pipeline locking that occurs in an AWS Elemental MediaLive channel.

### [Pipeline redundancy](https://docs.aws.amazon.com/medialive/latest/ug/plan-redundancy-mode.html)

You can set up a MediaLive channel with two encoding pipelines, to provide resiliency within the channel processing pipeline.

- [Deciding to implement](https://docs.aws.amazon.com/medialive/latest/ug/pipeline-redundancy-guidelines.html): In MediaLive, pipeline redundancy is controlled by the class that you assign to the channel.
- [Standard channel](https://docs.aws.amazon.com/medialive/latest/ug/standard-channel-procedure.html): When you followed the guidelines for implementing pipeline redundancy in a MediaLive channel, you might have decided that you might want to implement pipeline redundancy.
- [Single-pipeline channel with upgrade options](https://docs.aws.amazon.com/medialive/latest/ug/single-channel-upgrade.html): When you followed the guidelines for implementing pipeline redundancy in a MediaLive channel, you might have decided that you want to create the channel without pipeline redundancy.
- [Single-pipeline channel without upgrade](https://docs.aws.amazon.com/medialive/latest/ug/single-pipeline-no-upgrade.html): When you followed the guidelines for implementing pipeline redundancy in a MediaLive channel, you might have decided one of the following:
- [Changing an existing channel](https://docs.aws.amazon.com/medialive/latest/ug/pipeline-redundancy-change.html): To enable or disable pipeline redundancy on an existing MediaLive channel, you must update the channel class.
- [Resiliency](https://docs.aws.amazon.com/medialive/latest/ug/resiliency-channel.html): AWS Elemental MediaLive has several features that provide resiliency in the channel:
- [Smart crop](https://docs.aws.amazon.com/medialive/latest/ug/elemental-inference-smart-crop.html): In an AWS Elemental MediaLive channel, you can enable the smart crop feature in order to set up one or more outputs with an aspect ratio that is different from the source aspect ratio.

### [SCTE 35](https://docs.aws.amazon.com/medialive/latest/ug/scte-35-message-processing.html)

Learn how to configure an AWS Elemental MediaLive channel to handle SCTE 35 messages.

### [About message processing](https://docs.aws.amazon.com/medialive/latest/ug/about-message-processing.html)

SCTE 35 messages are messages that can be included in a source MPEG-2 transport stream (TS).

- [Supported features by input type](https://docs.aws.amazon.com/medialive/latest/ug/input-processing-options.html): SCTE 35 messages can appear only in the following types of MediaLive inputs:
- [Supported output features](https://docs.aws.amazon.com/medialive/latest/ug/processing-options.html): MediaLive supports different types of processing that you can implement in different combinations.
- [Processing features â default behavior](https://docs.aws.amazon.com/medialive/latest/ug/processing-options-default.html): The default handling of SCTE 35 by MediaLive is the following:
- [Scope of processing by feature](https://docs.aws.amazon.com/medialive/latest/ug/scope-by-feature.html): The SCTE 35 features that you can implement in a MediaLive channel have different scopes in terms of the output groups and outputs that they affect:

### [Supported features by output type](https://docs.aws.amazon.com/medialive/latest/ug/processing-applicability-by-output-type.html)

This section describes which SCTE 35 features apply to the various types of outputs that MediaLive supports.

- [Archive output with MPEG-2 container](https://docs.aws.amazon.com/medialive/latest/ug/archive-output-with-mpeg-2-container.html): In an Archive output (a transport stream in an MPEG-2 container), MediaLive supports SCTE 35 features as follows:
- [Frame capture output](https://docs.aws.amazon.com/medialive/latest/ug/framecapture-output.html): In a Frame capture output, MediaLive supports SCTE 35 features as follows:
- [HLS output](https://docs.aws.amazon.com/medialive/latest/ug/hls-output.html): In an HLS output (a transport stream), MediaLive supports SCTE 35 features as follows:
- [MediaPackage output](https://docs.aws.amazon.com/medialive/latest/ug/mediapackage-output.html): In a MediaPackage output, MediaLive supports SCTE 35 features as follows:
- [Microsoft Smooth output](https://docs.aws.amazon.com/medialive/latest/ug/ms-smooth-output.html): In a Microsoft Smooth output, MediaLive supports SCTE 35 features as follows:
- [RTMP output](https://docs.aws.amazon.com/medialive/latest/ug/adobe-rtmp-output.html): In an RTMP output, MediaLive supports SCTE 35 features as follows:
- [UDP or SRT output](https://docs.aws.amazon.com/medialive/latest/ug/udp-ts-output.html): In a transport stream output (for example, UDP or SRT), MediaLive supports SCTE 35 features as follows:
- [Get ready: Set the SCTE 35 source](https://docs.aws.amazon.com/medialive/latest/ug/scte35-getting-ready-source.html): If you have HLS inputs in a MediaLive channel, you must configure the input to identify the source of the SCTE 35 messages.
- [Get ready: Set ad avail mode](https://docs.aws.amazon.com/medialive/latest/ug/getting-ready-set-the-ad-avail-mode.html): You must set the mode for SCTE 35 handling.

### [Manifest decoration](https://docs.aws.amazon.com/medialive/latest/ug/enable-manifest-decoration.html)

You can choose to interpret SCTE 35 messages from the input sources in a MediaLive channel and insert corresponding instructions into the output manifest.

- [Enabling decoration â HLS](https://docs.aws.amazon.com/medialive/latest/ug/procedure-to-enable-decoration-hls.html): In an HLS output group, manifest decoration is enabled at the output group level, which means that the manifests for all outputs in that group include instructions based on the SCTE 35 content.
- [Enabling decoration â Microsoft Smooth](https://docs.aws.amazon.com/medialive/latest/ug/procedure-to-enable-decoration-ms-smooth.html): In a Microsoft Smooth output group, if you enable manifest decoration, instructions are inserted in the sparse track.
- [How SCTE 35 events are handled in manifests and sparse tracks](https://docs.aws.amazon.com/medialive/latest/ug/how-scte-35-events-are-handled-in-manifests.html): When you enable manifest decoration or sparse track in an HLS or Microsoft Smooth output group, MediaLive inserts up to three types of information.
- [Sample manifests - HLS](https://docs.aws.amazon.com/medialive/latest/ug/sample-manifests-hls.html): MediaLive supports the following HLS manifest styles for outputs:

### [Ad avail blanking](https://docs.aws.amazon.com/medialive/latest/ug/enable-ad-avail-blanking.html)

In a MediaLive channel, you can enable ad avail blanking to blank out the content for an SCTE 35 message that is considered an ad avail (as defined by the ad avail mode in ).

- [Enabling blanking](https://docs.aws.amazon.com/medialive/latest/ug/procedure-to-enable-ad-avail-blanking.html): Follow this procedure if you want to enable the ad avail blanking feature in a MediaLive channel.
- [Triggers for ad avail blanking](https://docs.aws.amazon.com/medialive/latest/ug/triggers-for-ad-avail-blanking.html): For ad avail blanking, the ad avail mode that you set controls which SCTE 35 events result in the blanking of the content in the MediaLive outputs.
- [Ad avail blanking restriction flags](https://docs.aws.amazon.com/medialive/latest/ug/ad-avail-blanking-restriction-flags.html): This section provides information about the restriction flags that you can set in a MediaLive channel, when you set up for ad avail blanking.

### [Blackout](https://docs.aws.amazon.com/medialive/latest/ug/enable-blackout.html)

In a MediaLive channel, you can enable blackout to blank out the content for an SCTE 35 message that is of type other event (as defined by the mode in ).

- [Enabling blackout](https://docs.aws.amazon.com/medialive/latest/ug/procedure-enable-blackout.html): Follow this procedure if you want to enable the blackout feature in a MediaLive channel.
- [Triggers for blackout](https://docs.aws.amazon.com/medialive/latest/ug/triggers-for-blackout.html): The blackout feature is triggered only by time_signal messages of segmentation type Other.
- [Blackout restriction flags](https://docs.aws.amazon.com/medialive/latest/ug/blackout-restriction-flags.html): This section provides information about the restriction flags that you can set in a MediaLive channel, when you set up for blackout.
- [Passthrough of SCTE 35 messages](https://docs.aws.amazon.com/medialive/latest/ug/scte-35-passthrough-or-removal.html): You can set up the MediaLive channel so that SCTE 35 messages from the input are passed through (included) in the data stream for the following outputs:
- [Inserting messages](https://docs.aws.amazon.com/medialive/latest/ug/setup-scte35-insertion.html): Use the channel schedule to insert SCTE 35 messages into the outptus of a MediaLive CHANNEL.

### [POIS signal conditioning](https://docs.aws.amazon.com/medialive/latest/ug/scte35-pois-conditioning.html)

Learn how to set up an MediaLive channel so that a POIS server can perform signal conditioning on the SCTE 35 messages that are in the source inputs for a channel.

- [Supported version of the specification](https://docs.aws.amazon.com/medialive/latest/ug/scte35-pois-about-spec.html): MediaLive communicates with a POIS server using the ESAM API.
- [About POIS signal conditioning](https://docs.aws.amazon.com/medialive/latest/ug/scte35-pois-about.html): You can configure a MediaLive channel so that your POIS server handles SCTE 35 message that are in the content.
- [Setting up for POIS signal conditioning](https://docs.aws.amazon.com/medialive/latest/ug/scte35-pois-setup.html): With POIS signal conditioning, the MediaLive channel and the POIS server must be set up with identical information.
- [Sharing and cloning encodes](https://docs.aws.amazon.com/medialive/latest/ug/feature-share-encode.html): You can share a single encode among several outputs within one MediaLive channel.

### [SMPTE 2038 metadata](https://docs.aws.amazon.com/medialive/latest/ug/smpte-2038.html)

Learn how to extract specific ancillary data from a SMPTE 2038 stream in specific MediaLive outputs.

- [Metadata that MediaLive can extract](https://docs.aws.amazon.com/medialive/latest/ug/smpte-23038-supported-metadata.html): MediaLive can extract the following data from a SMPTE 2038 stream that is in the source.
- [A well-formed SMPTE 2038 stream](https://docs.aws.amazon.com/medialive/latest/ug/smpte-2038-requirements.html): For MediaLive to extract and process the data appropriately, the SMPTE 2038 stream in the input must meet certain criteria:
- [Configuring inputs](https://docs.aws.amazon.com/medialive/latest/ug/smpte-2038-setup-input.html): If you want MediaLive to use the data in a SMPTE 2038 stream, you must configure the input to read the SMPTE 2038.
- [How MediaLive uses the SMPTE 2038 stream](https://docs.aws.amazon.com/medialive/latest/ug/smpte-2038-setup-output.html): If you set up to prefer SMPTE 2038 in an input, MediaLive uses the data according to the following rules.
- [Configuring outputs for KLV metadata](https://docs.aws.amazon.com/medialive/latest/ug/smpte-2038-klv-setup.html): You can choose to pass through the KLV metadata in specific types of output groups.
- [Amazon S3 access control lists (ACLs)](https://docs.aws.amazon.com/medialive/latest/ug/s3-canned-acl.html): Learn about using canned ACLs to transfer object ownership when the destination for an output is Amazon Simple Storage Service (Amazon S3).
- [Tagging resources](https://docs.aws.amazon.com/medialive/latest/ug/tagging.html): Create, view, edit, and delete tags on flows, outputs, and entitlements in AWS Elemental MediaLive.

### [Thumbnails for inputs](https://docs.aws.amazon.com/medialive/latest/ug/thumbnails.html)

Learn how to set up AWS Elemental MediaLive to generate thumbnails for the video inputs in channels.

- [Enabling thumbnails](https://docs.aws.amazon.com/medialive/latest/ug/thumbnails-enable.html): Learn how to enable thumbnails in AWS Elemental MediaLive.
- [Viewing thumbnails](https://docs.aws.amazon.com/medialive/latest/ug/thumbnails-view.html): Learn how to view thumbnails on the AWS Elemental MediaLive console.
- [Retrieving thumbnails](https://docs.aws.amazon.com/medialive/latest/ug/thumbnails-work-cli.html): Learn how to retrieve AWS Elemental MediaLive thumbnails programmatically.
- [Limit on thumbnails in MediaLive](https://docs.aws.amazon.com/medialive/latest/ug/thumbnail-limits.html): There is a limit to the number of MediaLivethumbnails that you can view or retrieve.

### [Timecodes and timestamps](https://docs.aws.amazon.com/medialive/latest/ug/timecode.html)

Learn about how AWS Elemental MediaLive uses timecodes in channels..

- [About timecodes and timestamps](https://docs.aws.amazon.com/medialive/latest/ug/timecodes-about.html): MediaLive has timecodes for the input pipeline and the output pipeline.
- [Configuring output timecode](https://docs.aws.amazon.com/medialive/latest/ug/timecode-configure-source.html): You can configure the start time for the output timecode that MediaLive includes in output encodes.
- [Timecode metadata](https://docs.aws.amazon.com/medialive/latest/ug/timecode-configure-metadata.html): You can set up a MediaLive channel to include timecode metadata in the individual output encode.
- [Timecode burnin](https://docs.aws.amazon.com/medialive/latest/ug/timecode-configure-burnin.html): You can set up any video encode in a MediaLive channel to burn in the output timecode.

### [Trick-play track](https://docs.aws.amazon.com/medialive/latest/ug/trick-play-solutions.html)

Trick-play is used in digital video players to mimic some capabilities of analog players, including fast-forward and rewind capabilities.

- [Trick-play track via I-frames](https://docs.aws.amazon.com/medialive/latest/ug/trick-play-i-frames.html): In a MediaLive HLS output group, you can support trick-play track by providing an I-frame-only manifest.
- [Trick-play track via the Image Media Playlist specification](https://docs.aws.amazon.com/medialive/latest/ug/trick-play-roku.html): In a MediaLive HLS or MediaPackage output group, you can support a trick-play track by providing an asset that follows the Image Media Playlist specification, version 0.4.

### [Video â color space conversion](https://docs.aws.amazon.com/medialive/latest/ug/color-space-simplified.html)

Learn about how MediaLive supports passthrough and conversion of color space and color space metadata.

- [Color space versus video resolution](https://docs.aws.amazon.com/medialive/latest/ug/color-space-vs-resolution.html): Learn about the difference between HDR and HD (or UHD), and between SDR and SD.

### [General information](https://docs.aws.amazon.com/medialive/latest/ug/about-color-metadata-simplified.html)

Learn about how AWS Elemental MediaLive supports color spaces, brightness functions (BT.1886, SMPTE 2084, HLG 2020), and display metadata (SMPTE 2086).

- [Components of color space](https://docs.aws.amazon.com/medialive/latest/ug/color-space-simplified-definitions.html): Read about the different components of the color space standards that MediaLive supports.
- [Supported color spaces](https://docs.aws.amazon.com/medialive/latest/ug/color-space-simplified-standards.html): Learn about the color space standards that MediaLive supports.
- [Passthrough](https://docs.aws.amazon.com/medialive/latest/ug/color-space-simplified-options-passthrough.html): You can set up to pass through the color space in a MediaLive output.

### [Conversion](https://docs.aws.amazon.com/medialive/latest/ug/color-space-simplified-options-convert.html)

You can set up to convert the color space itself, to change the pixels in the video.

- [Supported conversions](https://docs.aws.amazon.com/medialive/latest/ug/color-space-simplified-supported-conversions.html): You can configure a channel to use the standard MediaLive color corrector when converting the color space.
- [3D LUTs files](https://docs.aws.amazon.com/medialive/latest/ug/color-space-process-with-lut.html): You can configure a channel to use a 3D LUTs color correct file for conversion, instead of using the standard MediaLive color corrector file for conversion.
- [Input requirements](https://docs.aws.amazon.com/medialive/latest/ug/color-space-simplified-supported-inputs.html): Read about the characteristics that a video source must have in order for MediaLive to be able to work with its color space.
- [Output requirements](https://docs.aws.amazon.com/medialive/latest/ug/color-space-simplified-input-output-requirements.html): Read about the MediaLive output types and output video codecs that are supported for color space conversion. .
- [Metadata](https://docs.aws.amazon.com/medialive/latest/ug/color-space-simplified-options-metadata.html): When you set up in MediaLive to convert the color space, you can set up to include or omit the color space metadata.
- [Step 1: Configure the inputs](https://docs.aws.amazon.com/medialive/latest/ug/color-space-simplified-setup-input.html)
- [Step 2: Configure the outputs](https://docs.aws.amazon.com/medialive/latest/ug/color-space-simplified-output-handling.html): Learn about the options for handling the color space and color space metadata that is in the video output that AWS Elemental MediaLive produces.
- [Step 3: Results in outputs](https://docs.aws.amazon.com/medialive/latest/ug/colorspace-simplified-output-results.html): Read about how MediaLive handles color space in the output video when you pass through or when you convert the color space.
- [Reference: Location of fields](https://docs.aws.amazon.com/medialive/latest/ug/colorspace-simplified-fields.html): Look up the location on the Console of fields that relate to handling color space in video content.

### [Video â complex color space conversion](https://docs.aws.amazon.com/medialive/latest/ug/color-space.html)

Learn about how to configure MediaLive to convert and/or pass through video color space when you are working with source video that has undependable or missing color space metadata.

- [Options for handling](https://docs.aws.amazon.com/medialive/latest/ug/color-space-handling-options.html): Read a summary of the different ways that you can set up MediaLive to handle color space in the outputs you produce when you are working with source video that has undependable or missing color space metadata.

### [General information](https://docs.aws.amazon.com/medialive/latest/ug/about-color-metadata.html)

Learn about how MediaLive supports color spaces, brightness functions (BT.1886, SMPTE 2084, HLG 2020), and display metadata (SMPTE 2086).

- [Definition](https://docs.aws.amazon.com/medialive/latest/ug/color-space-definitions.html): There are four components to color space:
- [Supported color spaces](https://docs.aws.amazon.com/medialive/latest/ug/color-space-standards.html): Each color space standard follows a specific standard for the color space, and specific standards for the three sets of color data.
- [Passthrough](https://docs.aws.amazon.com/medialive/latest/ug/color-space-options-passthrough.html): You can set up to pass through the color space from the source to a MediaLive output.
- [Conversion](https://docs.aws.amazon.com/medialive/latest/ug/color-space-options-convert.html): You can set up to convert the color space itselfâto change the pixels in the video.
- [Input and output requirements](https://docs.aws.amazon.com/medialive/latest/ug/color-space-input-output-requirements.html): Topics
- [General procedure for handling color space](https://docs.aws.amazon.com/medialive/latest/ug/color-space-general-procedure.html): Read a summary of the steps for setting up a channel so that MediaLive can work with color space, when you are working with source video that has undependable or missing color space metadata.
- [Assess the color spaces in the sources](https://docs.aws.amazon.com/medialive/latest/ug/color-space-assess-inputs.html): Learn how to assess the color spaces and color space metadata that are in the video content that MediaLive ingests, when you are working with source video that has undependable or missing color space metadata.

### [Configuring color space metadata](https://docs.aws.amazon.com/medialive/latest/ug/color-space-input-handling.html)

Learn how to assess the color spaces and color space metadata that are in the video content that AWS Elemental MediaLive ingests, when you are working with source video that has undependable or missing color space metadata.

- [Step 1: Assess the metadata](https://docs.aws.amazon.com/medialive/latest/ug/color-space-input-procedure.html): Learn about how to assess the quality of the color space metadata in a MediaLive input for AWS Elemental Live, when you are working with source video that has undependable or missing color space metadata.

### [Step 2: Correcting metadata](https://docs.aws.amazon.com/medialive/latest/ug/color-space-cleanup-scenarios.html)

Read about different possible scenarios for handling color space and color space metadata in the video content that AWS Elemental MediaLive ingests, when you are working with source video that has undependable or missing color space metadata.

- [Accurate metadata](https://docs.aws.amazon.com/medialive/latest/ug/color-space-scenario-pass.html): During assessment of the MediaLive input, you might have determined the following:
- [Correct metadata with force](https://docs.aws.amazon.com/medialive/latest/ug/color-space-scenario-correct.html): During assessment of the MediaLive input, you might have determined the following:
- [Correct metadata with fallback](https://docs.aws.amazon.com/medialive/latest/ug/color-space-scenario-correct-one.html): During assessment of the MediaLive input, you might have determined the following:
- [Uncorrectable metadata](https://docs.aws.amazon.com/medialive/latest/ug/color-space-scenario-correct-multiple.html): During assessment of the MediaLive input, you might have determined the following:
- [Step 3: Set up inputs](https://docs.aws.amazon.com/medialive/latest/ug/color-space-input-setup.html): Learn how to set up inputs so that MediaLive can correct undependable or missing color space metadata.

### [Configuring outputs](https://docs.aws.amazon.com/medialive/latest/ug/color-space-output-handling.html)

Learn about the options for handling the color space and color space metadata that is in the video output that AWS Elemental MediaLive produces, when you are working with source video that has undependable or missing color space metadata.

- [Step 1: Set up enhanced VQ](https://docs.aws.amazon.com/medialive/latest/ug/color-space-output-config-vq.html): You must decide if you should enable enhanced VQ mode in each MediaLive output.
- [Step 2: Set up outputs](https://docs.aws.amazon.com/medialive/latest/ug/colorspace-output-setup.html): Learn how to configure color space handling in each output that AWS Elemental MediaLive produces, when you are working with source video that has undependable or missing color space metadata.

### [Results in outputs](https://docs.aws.amazon.com/medialive/latest/ug/colorspace-output-results.html)

Read about how MediaLive handles color space in the output video when you pass through or when you convert the color space, when you are working with source video that has undependable or missing color space metadata.

- [Passthrough](https://docs.aws.amazon.com/medialive/latest/ug/colorspace-output-passthrough.html): Read about how MediaLive handles color space when you set up an output to pass through the source color space.
- [Conversion to SDR](https://docs.aws.amazon.com/medialive/latest/ug/colorspace-output-sdr.html): Read about how MediaLive handles color space when you set up an output to convert the source color space to an SDR color space.
- [Conversion to HDR10](https://docs.aws.amazon.com/medialive/latest/ug/colorspace-output-hdr10.html): Read about how MediaLive handles color space when you set up an output to convert the source color space to HDR10.
- [Conversion to Dolby Vision 8.1](https://docs.aws.amazon.com/medialive/latest/ug/color-space-output-dolby81.html): Read about how MediaLive handles color space when you set up an output to convert the source color space to Dolby Vision 8.1.
- [Removal of metadata](https://docs.aws.amazon.com/medialive/latest/ug/colorspace-output-remove.html): Read about how MediaLive handles color space when you remove the color space metadata in the output.
- [Reference: Location of fields](https://docs.aws.amazon.com/medialive/latest/ug/colorspace-fields.html): Read this section if you know how to handle color space in MediaLive, and you only need a reminder of where the fields are located in the MediaLive Console.
- [Video â enhanced VQ](https://docs.aws.amazon.com/medialive/latest/ug/video-enhancedvq.html): You can configure the enhanced VQ mode in an output to produce slightly better video quality without an increase in the bitrate.
- [Video â rate control mode](https://docs.aws.amazon.com/medialive/latest/ug/video-encode-ratecontrol.html): If the codec in a video encode is AV1, H.264 (AVC), or H.265 (HEVC), you can configure the rate control mode.

### [VPC delivery](https://docs.aws.amazon.com/medialive/latest/ug/delivery-out-vpc.html)

You can set up a MediaLive channel to have output endpoints in Amazon Virtual Private Cloud (Amazon VPC).

- [How VPC delivery works](https://docs.aws.amazon.com/medialive/latest/ug/vpc-out-how-it-works.html): VPC delivery applies to each MediaLive channel.
- [Getting ready](https://docs.aws.amazon.com/medialive/latest/ug/vpc-out-get-ready-subnets.html): An Amazon VPC user must set up the VPC and identify subnets and security groups for the MediaLive channel.
- [Setting up for VPC delivery](https://docs.aws.amazon.com/medialive/latest/ug/vpc-out-setup-steps.html)
- [Changing the setup](https://docs.aws.amazon.com/medialive/latest/ug/vpc-out-change.html): If you have set up a MediaLive channel for VPC delivery, note the following:

### [Identifying subnet and Availability Zone requirements](https://docs.aws.amazon.com/medialive/latest/ug/vpc-out-AZ-subnet-reqs.html)

Subnets and Availability Zones apply as follows:

- [Use case A â no VPC inputs](https://docs.aws.amazon.com/medialive/latest/ug/vpc-out-caseA.html): This use case applies if the MediaLive channel won't have inputs that use the VPC:
- [Use case B â channel includes VPC inputs](https://docs.aws.amazon.com/medialive/latest/ug/vpc-out-caseB.html): This use case applies if the MediaLive channel includes inputs that use the VPC:


## [Working with resources](https://docs.aws.amazon.com/medialive/latest/ug/container-resources.html)

### [Channels](https://docs.aws.amazon.com/medialive/latest/ug/container-channel.html)

You can create an channel to transcode and package video content.

- [Creating a channel from scratch](https://docs.aws.amazon.com/medialive/latest/ug/channel-create-scratch.html): For information about creating a MediaLive channel from scratch, see .
- [Creating a channel from a template](https://docs.aws.amazon.com/medialive/latest/ug/creating-channel-template.html): You can create a channel in AWS Elemental MediaLive by using a template.
- [Creating a channel by cloning](https://docs.aws.amazon.com/medialive/latest/ug/creating-channel-clone.html): You can create a MediaLive channel in AWS Elemental MediaLive by cloning an existing channel.
- [Editing and deleting a channel](https://docs.aws.amazon.com/medialive/latest/ug/editing-deleting-channel.html): You can edit an existing AWS Elemental MediaLive channel to change how it processes the input, and you can delete a channel.
- [Updating channel class](https://docs.aws.amazon.com/medialive/latest/ug/edit-channel-class.html): You can edit the channel class in an existing AWS Elemental MediaLive channel to change whether the channel implements pipeline redundancy.
- [Viewing a channel configuration](https://docs.aws.amazon.com/medialive/latest/ug/viewing-channel-configuration.html): You can view information about the configuration of an AWS Elemental MediaLive channel.
- [Link input device](https://docs.aws.amazon.com/medialive/latest/ug/eml-devices.html): Learn how to set up an AWS Elemental Link hardware device as a video source for an MediaLive channel.

### [Inputs](https://docs.aws.amazon.com/medialive/latest/ug/creating-input.html)

You can create, edit, and delete MediaLive inputs.

- [Categories for inputs](https://docs.aws.amazon.com/medialive/latest/ug/input-categories.html): In MediaLive, inputs can be categorized in several ways:
- [Creating an input](https://docs.aws.amazon.com/medialive/latest/ug/create-input.html): For information about creating an input in MediaLive, see Creating a channel from scratch.
- [Editing an input](https://docs.aws.amazon.com/medialive/latest/ug/edit-input.html): The rules for editing an input in MediaLive are as follows.
- [Deleting an input](https://docs.aws.amazon.com/medialive/latest/ug/delete-input.html)
- [Detaching an input](https://docs.aws.amazon.com/medialive/latest/ug/detach-input.html): You can detach an input from a MediaLive channel.

### [Input security groups](https://docs.aws.amazon.com/medialive/latest/ug/working-with-input-security-groups.html)

You can create, edit, and delete the input security groups.

- [Purpose of an input security group](https://docs.aws.amazon.com/medialive/latest/ug/purpose-input-security-groups.html): In MediaLive, input security groups are used with specific push inputs where the upstream system for the source is on the public internet:
- [Creating an input security group](https://docs.aws.amazon.com/medialive/latest/ug/create-input-security-groups.html): In MediaLive, you create an input security group to specify a list of access rules.
- [Editing an input security group](https://docs.aws.amazon.com/medialive/latest/ug/edit-input-security-group.html): You can edit any of the fields in an input security group.
- [Deleting an input security group](https://docs.aws.amazon.com/medialive/latest/ug/delete-input-security-group.html): You can delete a MediaLive input security group so long as it is not attached to any inputs.

### [Multiplexes](https://docs.aws.amazon.com/medialive/latest/ug/eml-multiplex.html)

Learn how to create, edit, and delete a MediaLive multiplex.

- [Summary of actions](https://docs.aws.amazon.com/medialive/latest/ug/multiplex-create-delete-edit-summary.html): The following table summarizes the create, edit, and delete capabilities for the MediaLive multiplex, program, and channel.
- [Creating a multiplex and program](https://docs.aws.amazon.com/medialive/latest/ug/multiplex-create.html): A MediaLive multiplex provides configuration information for an MPTS, including the bitrate of the entire MPTS.
- [Creating a channel](https://docs.aws.amazon.com/medialive/latest/ug/multiplex-channel-create.html): The MediaLive channel attached to a program is a regular channel in which the output group is always a multiplex output group.
- [Editing multiplexes, programs, and channels](https://docs.aws.amazon.com/medialive/latest/ug/edit-multiplex-program-channel.html): In MediaLive, you can edit a multiplex, the programs in a multiplex, and the channels in a multiplex.
- [Deleting multiplexes, programs, and channels](https://docs.aws.amazon.com/medialive/latest/ug/delete-multiplex-program.html): In MediaLive, you can delete a multiplex, the programs in a multiplex, and the channels in a multiplex.


## [Setup: AWS Elemental Link](https://docs.aws.amazon.com/medialive/latest/ug/setup-devices.html)

- [HD and UHD Link devices](https://docs.aws.amazon.com/medialive/latest/ug/elink-device-hd-uhd.html): Learn about the differences between AWS Elemental Link HD and AWS Elemental Link UHD.
- [Deploying the hardware](https://docs.aws.amazon.com/medialive/latest/ug/elink-setup-device.html): Learn how to deploy the AWS Elemental Link hardware device into the AWS cloud.
- [Using Link with a MediaLive input](https://docs.aws.amazon.com/medialive/latest/ug/device-use-input.html): You can set up a Link HD or a Link UHD as the source for an input that you connect to a MediaLive channel.
- [Using Link with a MediaConnect flow](https://docs.aws.amazon.com/medialive/latest/ug/device-use-flow.html): Learn how to set up an AWS Elemental Link device so that your can use it as a source for a MediaConnect flow.

### [Managing Link devices](https://docs.aws.amazon.com/medialive/latest/ug/device-manage.html)

Learn how to perform operations on an AWS Elemental Link device so that your can use it as a source in a MediaLive channel or a MediaConnect flow.

- [Setting up users with IAM permissions](https://docs.aws.amazon.com/medialive/latest/ug/device-iam-for-user.html): Learn how to set up users with the permissions configure an AWS Elemental Link device to work with an AWS Elemental MediaLive input or an AWS Elemental MediaConnect flow.
- [Setting up MediaLive as a trusted entity](https://docs.aws.amazon.com/medialive/latest/ug/device-iam-for-medialive.html): Learn how to set up AWS Elemental MediaLive as a trusted entity so that it has permissions to work with an AWS Elemental MediaConnect flow.
- [Claiming a device](https://docs.aws.amazon.com/medialive/latest/ug/device-claim.html): If you purchase a device from an AWS reseller, you must claim the device.
- [Creating a device](https://docs.aws.amazon.com/medialive/latest/ug/device-create.html): Within MediaLive, the Link device is represented a resource that is called theLink input device.
- [Viewing details about devices](https://docs.aws.amazon.com/medialive/latest/ug/device-view.html): You can view a list of the Link devices in your AWS account, in the Region where you use AWS Elemental MediaLive.
- [Transferring account](https://docs.aws.amazon.com/medialive/latest/ug/device-transfers.html): You can transfer a device to a different AWS account, to transfer ownership of the device to that account.
- [Transferring Region](https://docs.aws.amazon.com/medialive/latest/ug/device-transfer-region.html): You can transfer a device to a different AWS Region. (If instead you want to transfer the device to a different Availability Zone in the existing Region, see .)
- [Configuring a device](https://docs.aws.amazon.com/medialive/latest/ug/device-edit.html): The Link device has properties that control how it behaves when it is streaming.
- [Attaching and detaching a device](https://docs.aws.amazon.com/medialive/latest/ug/device-attach.html): If you are using a Link device as the source for a MediaConnect flow, you must attach the flow to the device.
- [Starting and stopping a Link device](https://docs.aws.amazon.com/medialive/latest/ug/device-start-stop.html): You must start or stop a Link only if it is configured as the source for a MediaConnect flow. (You don't need to start or stop the device when it is configured as the source for a MediaLive input.
- [Rebooting a device](https://docs.aws.amazon.com/medialive/latest/ug/device-reboot.html): You can remotely reboot a Link device from the AWS console.
- [Updating device software](https://docs.aws.amazon.com/medialive/latest/ug/device-update.html): Link devices automatically install updates when they are powered on, assuming that the MediaLive channels that use the device have stopped.
- [Deleting a device](https://docs.aws.amazon.com/medialive/latest/ug/device-delete.html): You don't delete Link input devices.


## [Security](https://docs.aws.amazon.com/medialive/latest/ug/security.html)

- [Data protection](https://docs.aws.amazon.com/medialive/latest/ug/data-retention.html): Learn how the AWS shared responsibility model applies to data protection in AWS Elemental MediaLive.

### [Identity and Access Management](https://docs.aws.amazon.com/medialive/latest/ug/security-iam.html)

How to authenticate requests and manage access to your MediaLive resources.

- [How AWS Elemental MediaLive works with IAM](https://docs.aws.amazon.com/medialive/latest/ug/security_iam_service-with-iam.html): Before you use IAM to manage access to MediaLive, learn what IAM features are available to use with MediaLive.
- [Identity-based policy examples](https://docs.aws.amazon.com/medialive/latest/ug/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify MediaLive resources.
- [Troubleshooting](https://docs.aws.amazon.com/medialive/latest/ug/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with MediaLive and IAM.
- [AWS managed policies](https://docs.aws.amazon.com/medialive/latest/ug/security-iam-awsmanpol.html): Learn about AWS managed policies for MediaLive and recent changes to those policies.
- [Compliance validation](https://docs.aws.amazon.com/medialive/latest/ug/SERVICE-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/medialive/latest/ug/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Elemental MediaLive features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/medialive/latest/ug/infrastructure-security.html): Learn how AWS Elemental MediaLive isolates service traffic.

# Source: https://docs.aws.amazon.com/deepracer/latest/developerguide/llms.txt

# AWS DeepRacer Developer Guide

> Learn how to train and evaluate a reinforcement learning model for autonomous driving in simulation. The tasks include how define a reward function, customize the action space, set up the training configuration, and creating a training job using Amazon SageMaker and AWS RoboMaker. Find out how to submit a trained model to the AWS DeepRacer League to race against other AWS DeepRacer users in the online Virtual Circuit. Learn how to set up and calibrate your AWS DeepRacer vehicle, upload a trained AWS DeepRacer model to the vehicle, build a physical track for the vehicle to drive autonomously.

- [](https://docs.aws.amazon.com/deepracer/latest/developerguide/import-export-models.html)
- [Update and restore your AWS DeepRacer device](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-ubuntu-update.html)
- [Document history](https://docs.aws.amazon.com/deepracer/latest/developerguide/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/deepracer/latest/developerguide/glossary.html)

## [What is AWS DeepRacer?](https://docs.aws.amazon.com/deepracer/latest/developerguide/what-is-deepracer.html)

- [Explore reinforcement learning](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-is-a-learning-environment-for-reinforcement-learning.html): Reinforcement learning, especially deep reinforcement learning, has proven effective in solving a wide array of autonomous decision-making problems.
- [Concepts and terminology](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-basic-concept.html): AWS DeepRacer concepts and terminology


## [How it works](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-how-it-works.html)

- [Reinforcement learning](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-how-it-works-overview-reinforcement-learning.html): Learn the principles of training reinforcement learning models in AWS DeepRacer.
- [Action space and reward function](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-how-it-works-action-space.html): Learn how action space and reward function are used in AWS DeepRacer training
- [Training algorithms](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-how-it-works-reinforcement-learning-algorithm.html)
- [AWS DeepRacer workflow](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-how-it-works-solution-workflow.html): Training an AWS DeepRacer model involves the following general tasks:
- [Simulated-to-real performance gaps](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-how-it-works-virtual-to-physical.html): Because the simulation cannot capture all aspects of the real world accurately, the models trained in simulation may not work well in the real world.


## [Get started](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-get-started.html)

- [Train your first model](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-get-started-training-model.html): Learn how to use the AWS DeepRacer console to train a reinforcement learning model.
- [Evaluate models in simulation](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-get-started-test-in-simulator.html): After your training job is complete, you should evaluate the trained model to assess its convergency behavior.


## [Train and evaluate models](https://docs.aws.amazon.com/deepracer/latest/developerguide/create-deepracer-project.html)

- [Understanding racing types and enabling sensors](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-choose-race-type.html): Learn AWS DeepRacer-supported types of races as enabled by supported types of sensors and how they affect training.
- [Train and evaluate models using AWS DeepRacer console](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-console-train-evaluate-models.html): To train a reinforcement learning model, you can use the AWS DeepRacer console.

### [Reward function reference](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-reward-function-reference.html)

The following is the technical reference of the AWS DeepRacer reward function.

- [Reward function input parameters](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-reward-function-input.html): Explains the semantics of the AWS DeepRacer reward function input parameters.
- [Reward function examples](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-reward-function-examples.html): The following lists some examples of the AWS DeepRacer reward function.


## [Operate your vehicle](https://docs.aws.amazon.com/deepracer/latest/developerguide/operate-deepracer-vehicle.html)

### [Get to know your vehicle](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-prep-vehicle.html)

Your AWS DeepRacer vehicle is a machine learning-enabled, battery-powered, and Wi-Fi-connected 1/18th-scale model four-wheel drive car with a front-mounted 4-megapixel camera and an Ubuntu-based compute module.

- [LED indicators](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-vehicle-led-indicators.html): Document the AWS DeepRacer vehicle LED indicators and their color semantics.
- [Device spare parts](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-vehicle-chassis-parts.html): Lists AWS DeepRacer device parts for replacement and repair.
- [Set up your vehicle](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-set-up-vehicle.html): The first time you open your AWS DeepRacer vehicle, you must set it up to connect to a Wi-Fi network.
- [Launch device console](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-set-up-vehicle-test-drive.html): After you set up the vehicle's Wi-Fi connection and install required software updates, you should open the device console to verify if the vehicle's network connection is working.
- [Calibrate your vehicle](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-calibrate-vehicle.html)
- [Upload your model](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-upload-model-to-vehicle.html): Learn how to upload a model to the AWS DeepRacer vehicle using the AWS DeepRacer console.
- [Drive your vehicle](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-drive-your-vehicle.html): After setting up your AWS DeepRacer vehicle, you can start to drive your vehicle manually or let it drive autonomously, using the vehicle's device console.
- [Inspect and manage vehicle settings](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-manage-vehicle-settings.html): After the initial setup, you can use the AWS DeepRacer device control console to manage your vehicle's settings.
- [View vehicle logs](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-drive-vehicle-logs.html): Your AWS DeepRacer vehicle logs operational events that can be helpful for troubleshooting issues encountered in running your vehicle.


## [Build your physical track](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-build-your-track.html)

- [Materials and tools](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-build-your-track-materials-and-tools.html): Before you start to construct you track, get the following materials and tools ready.
- [Lay your track](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-build-your-track-construction.html): When you build your track, it's a good practice to start with a simple design, such as a straight or single-turn track.
- [Track design templates](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-track-examples.html): The following track design templates show AWS DeepRacer tracks that you can build by following the instructions presented in this section.


## [Join a race](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-racing-series.html)

- [Join a Virtual Circuit race](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-submit-model-to-leaderboard.html): In this section, learn how to use the AWS DeepRacer console to submit your trained model to a Virtual Circuit race.
- [Join a community race](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-join-community-race.html): Learn how to join an AWS DeepRacer community race.
- [Participate in a LIVE race](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-participate-live-race.html): Learn how to participate in a LIVE AWS DeepRacer race.


## [Organize a race](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-race-organizer.html)

- [](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-community-race-topics.html)
- [Create a race quick start](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-create-community-race.html): You can set up a virtual race quickly using the default community race settings.
- [Customize a race](https://docs.aws.amazon.com/deepracer/latest/developerguide/customize-community-race.html): To create a race that is tailored for your group, expand Race customizations on the Race details page.
- [Run a LIVE race](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-moderate-live-community-race.html): Learn how to manage the queue, set up the race simulator and launch your racers.
- [Broadcast a LIVE race](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-broadcast-live-community-race.html): Get tips and templates from the pros who broadcast the AWS DeepRacer League Championship Cup Races.
- [Manage a race](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-manage-community-races.html): Learn how to manage AWS DeepRacer community races.


## [Organize an event](https://docs.aws.amazon.com/deepracer/latest/developerguide/organize-an-event.html)

- [How events work and what to expect](https://docs.aws.amazon.com/deepracer/latest/developerguide/how-events-work-and-what-to-expect.html): Whether you want to provide education and hands-on practice with reinforcement learning for your team, promote your organization to attract new talent, or a combination of both, this guide provides the tools and resources to help you create and customize your own AWS DeepRacer event.
- [Getting started with your event](https://docs.aws.amazon.com/deepracer/latest/developerguide/getting-started-with-your-event.html): Once you've defined your organization's goals, you can use your project plan to begin narrowing down the type of event you want to hold.


## [Multi-user mode](https://docs.aws.amazon.com/deepracer/latest/developerguide/multi-user-mode.html)

- [Admin setup](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-multi-user-admin-set-up.html): Organizations may want to sponsor multiple participants under one AWS DeepRacer account.
- [Participant setup](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-multi-user-racer-experience.html): This section explains the experience of a participant whose account is sponsored by an organization in multi-user mode.


## [Educator tools](https://docs.aws.amazon.com/deepracer/latest/developerguide/educator.html)

- [Create a student race](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-create-student-community-race.html): This guide helps educators create AWS DeepRacer races for students.
- [Customize a student race](https://docs.aws.amazon.com/deepracer/latest/developerguide/customize-student-community-race.html): This guide helps educators customize AWS DeepRacer races for students.
- [Manage a student race](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-manage-student-community-races.html): Learn how to manage AWS DeepRacer Student community races.


## [Security](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-setup.html)

- [Data protection](https://docs.aws.amazon.com/deepracer/latest/developerguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS DeepRacer.
- [AWS DeepRacer-Dependent Services](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-dependent-aws-services.html): Learn what AWS services on which AWS DeepRacer depends on.
- [Required IAM roles](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-understand-required-permissions-and-iam-roles.html): Learn the required permissions and IAM roles for using AWS DeepRacer.

### [AWS Identity and Access Management](https://docs.aws.amazon.com/deepracer/latest/developerguide/security-iam.html)

How to authenticate requests and manage access your DeepRacer resources.

- [How AWS DeepRacer works with IAM](https://docs.aws.amazon.com/deepracer/latest/developerguide/security_iam_service-with-iam.html): Before you use IAM to manage access to DeepRacer, learn what IAM features are available to use with DeepRacer.
- [Identity-based policy examples](https://docs.aws.amazon.com/deepracer/latest/developerguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify DeepRacer resources.
- [AWS managed policies](https://docs.aws.amazon.com/deepracer/latest/developerguide/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS DeepRacer and recent changes to those policies.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/deepracer/latest/developerguide/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.
- [Troubleshooting](https://docs.aws.amazon.com/deepracer/latest/developerguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with DeepRacer and IAM.


## [Tagging](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-tagging.html)

- [Add, view, and edit tags for a new resource](https://docs.aws.amazon.com/deepracer/latest/developerguide/tags-new.html): Use the AWS DeepRacer console to add, view, and edit tags for a new car, model, or a leaderboard.
- [Add, view, and edit tags for an existing resource](https://docs.aws.amazon.com/deepracer/latest/developerguide/tags-exisiting.html): Use the AWS DeepRacer console to add, view, and edit tags for an existing AWS DeepRacer RL model or a leaderboard.


## [Troubleshoot common issues](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-troubleshooting.html)

- [How to resolve common AWS DeepRacer LIVE issues](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-troubleshooting-deepracer-live.html): Learn how to resolve common AWS DeepRacer LIVE issues.
- [Why can't I connect to the device console with USB connection between my computer and vehicle?](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-troubleshooting-connect-to-deepracer.aws.html): When setting up your vehicle for the first time, you might find it unable to open the device console (also known as the device web server, https://deepracer.aws, hosted on the vehicle) after connecting your AWS DeepRacer vehicle to your computer with a micro-USB/USB cable (USB is also referred to as USB-A).
- [How to switch AWS DeepRacer compute module power source from battery to a power outlet](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-troubleshooting-switch-battery-to-wall-power.html): If the compute module battery level is low when you set up your AWS DeepRacer for the first time, follow the steps below to switch the compute power supply from the battery to a power outlet:
- [How to use a USB flash drive to connect AWS DeepRacer to your Wi-Fi network](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-troubleshooting-wifi-connection-first-time.html): To connect an AWS DeepRacer vehicle to your home or office Wi-Fi network using a USB flash drive, you need the following:
- [How to charge the vehicle's drive module battery](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-troubleshooting-charge-vehicle-battery-first-time.html): The AWS DeepRacer drive module battery has two sets of cables with two different color JST connectors, white and red.
- [How to charge the vehicle's compute module battery](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-troubleshooting-charge-compute-battery.html): Follow the steps below to charge your AWS DeepRacer compute module battery:
- [My battery is charged but my vehicle doesn't move](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-troubleshooting-immobile-vehicle-with-charged-battery.html): Follow these steps if your AWS DeepRacer console is set up, your compute battery is charged, and your Wi-Fi is connected, but your vehicle still doesn't move:

### [Troubleshoot vehicle battery lockout](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-prevent-vehicle-battery-lockout.html)

Troubleshoot AWS DeepRacer vehicle battery lockout issues.

- [How to prevent vehicle battery lockout](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-prevent-vehicle-battery-lockout-actual.html): Learn how to prevent AWS DeepRacer vehicle battery lockout.
- [How to unlock AWS DeepRacer vehicle batteries](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-troubleshooting-unlock-dead-vehicle-batteries.html): Learn how to use the battery unlock cable to restart your AWS DeepRacer vehicle battery.
- [How to wrap a Dell battery connector cable when installing a LiDAR sensor](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-troubleshooting-dell-battery-evo-wrap.html): Learn how to wrap a Dell battery cable around your LiDAR sensor so the Evo shell fits over your AWS DeepRacer vehicle.
- [How to maintain your vehicle's connection](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-troubleshooting-maintain-vehicle-connection.html): The following troubleshooting guide provides you tips for maintaining your vehicle's connection.
- [How to get your device's Mac address](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-troubleshooting-get-mac-address.html): Learn how to get the Mac address of your AWS DeepRacer device.
- [How to recover device controller default password](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-troubleshooting-recover-device-web-server-password.html): Learn how to recover your AWS DeepRacer device console default password.
- [How to manually update your device](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-troubleshooting-manual-update-device.html): Learn how to manually update your AWS DeepRacer device using a downloaded update script.
- [How to diagnose and resolve common device operational issues](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-troubleshooting-device-operation-issues.html): Learn how to diagnose and resolve some common device issues with your AWS DeepRacer vehicle.

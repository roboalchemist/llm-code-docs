# Google Cloud overview  |  Get started  |  Google Cloud Documentation
# Source: https://docs.cloud.google.com/docs/overview
# Path: /docs/overview

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Get started ](https://docs.cloud.google.com/docs/get-started)
  * [ Guides ](https://docs.cloud.google.com/docs/overview)



Send feedback 

#  Google Cloud overview Stay organized with collections  Save and categorize content based on your preferences. 

This overview is designed to help you understand the overall landscape of Google Cloud. Here, you'll take a brief look at some of the commonly used features and get pointers to documentation that can help you go deeper. Knowing what's available and how the parts work together can help you make decisions about how to proceed. You'll also get pointers to some tutorials that you can use to try out Google Cloud in various scenarios. 

For general information on cloud computing, see [Advantages and disadvantages of cloud computing](https://cloud.google.com/learn/advantages-of-cloud-computing).

## Google Cloud resources

Google Cloud consists of a set of physical assets, such as computers and hard disk drives, and virtual resources, such as virtual machines (VMs), that are contained in [data centers](https://cloud.google.com/about/locations) around the globe. Each data center location is in a _region_. Regions are available in Asia, Australia, Europe, Africa, the Middle East, North America, and South America. Each region is a collection of _zones_ , which are isolated from each other within the region. Each zone is identified by a name that combines a letter identifier with the name of the region. For example, zone `a` in the East Asia region is named `asia-east1-a`.

This distribution of resources provides several benefits, including redundancy in case of failure and reduced latency by locating resources closer to clients. This distribution also introduces some rules about how resources can be used together.

## Accessing resources through services

In cloud computing, what you might be used to thinking of as software and hardware products, become _services_. These services provide access to the underlying resources. The [list of available Google Cloud services](https://cloud.google.com/products/) is long, and it keeps growing. When you develop your website or application on Google Cloud, you mix and match these services into combinations that provide the infrastructure you need, and then add your code to enable the scenarios you want to build.

## Global, regional, and zonal resources

Some resources can be accessed by any other resource, across regions and zones. These _global resources_ include preconfigured disk images, disk snapshots, and networks. Some resources can be accessed only by resources that are located in the same region. These _regional resources_ include static external IP addresses. Other resources can be accessed only by resources that are located in the same zone. These _zonal resources_ include VM instances, their types, and disks.

The following diagram shows the relationship between global scope, regions and zones, and some of their resources:

![A global network can contain region-specific resources such as IP
         addresses and zone-specific resources such as VMs and disks.](/static/docs/images/overview/regions-zones.svg)

The scope of an operation varies depending on what kind of resources you're working with. For example, creating a network is a global operation because a network is a global resource, while reserving an IP address is a regional operation because the address is a regional resource.

As you start to optimize your Google Cloud applications, it's important to understand how these regions and zones interact. For example, even if you could, you wouldn't want to attach a disk in one region to a computer in a different region because the latency you'd introduce would make for poor performance. Thankfully, Google Cloud won't let you do that; disks can only be attached to computers in the same zone.

Depending on the level of self-management required for the [computing and hosting service](/docs/overview/cloud-platform-services#computing-hosting) you choose, you might or might not need to think about how and where resources are allocated.

For more information about the geographical distribution of Google Cloud, see [Geography and Regions](/docs/geography-and-regions).

## Projects

Any Google Cloud resources that you allocate and use must belong to a project. You can think of a project as the organizing entity for what you're building. A project is made up of the settings, permissions, and other metadata that describe your applications. Resources within a single project can work together easily, for example by communicating through an internal network, subject to the regions-and-zones rules. A project can't access another project's resources unless you use [Shared VPC](/vpc/docs/shared-vpc) or [VPC Network Peering](/vpc/docs/vpc-peering).

Each Google Cloud project has the following:

  * A project name, which you provide.
  * A project ID, which you can provide or Google Cloud can provide for you.
  * A project number, which Google Cloud provides.



As you work with Google Cloud, you use these identifiers in certain commands and API calls. The following screenshot shows a project name, a project ID, and a project number:

![A screenshot of the Google Cloud console displaying project ID and name.](/static/docs/images/overview/console-ids.png)

In this example:

  * **Example Project** is the project name.
  * **example-id** is the project ID.
  * **123456789012** is the project number.



Each project ID is unique across Google Cloud. After you have created a project, you can delete the project but its ID can never be used again.

You can create multiple projects and use them to separate your work in whatever way makes sense for you. For example, you might have one project that can be accessed by all team members and a separate project that can only be accessed by certain team members.

When billing is enabled, each project is associated with one billing account. Multiple projects can have their resource usage billed to the same account.

A project serves as a namespace. This means every resource within each project must have a unique name, but you can usually reuse resource names if they are in separate projects. Some resource names must be globally unique. Refer to the documentation for the resource for details.

For more information, see [Creating and managing projects](/resource-manager/docs/creating-managing-projects).

## Ways to interact with the services

Google Cloud gives you three basic ways to interact with the services and resources.

### Google Cloud console

![A screenshot of the Google Cloud console illustrating a web UI.](/static/docs/images/overview/console.png)

The [Google Cloud console](https://console.cloud.google.com/) provides a web-based, graphical user interface that you can use to manage your Google Cloud projects and resources. When you use the Google Cloud console, you either create a new project or choose an existing project, and then use the resources that you create in the context of that project.

### Command-line interface

If you prefer to work at the command line, you can perform most Google Cloud tasks by using [the Google Cloud CLI](/sdk/gcloud). The gcloud CLI lets you manage development workflow and Google Cloud resources in a terminal window.

For example, you can create a Compute Engine virtual machine (VM) instance by running the [`gcloud compute instances create` command](/sdk/gcloud/reference/compute/instances/create) in the shell environment.

You can run `gcloud` commands in the following ways:

  * You can install the [Google Cloud CLI](/sdk/docs). The gcloud CLI lets you open a terminal window on your own computer and run commands to manage Google Cloud resources.

  * You can use [Cloud Shell](/shell/docs/features), which is a browser-based shell. Because it runs in a browser window, you don't need to install anything on your own computer. You can open the Cloud Shell from the [Google Cloud console](https://console.cloud.google.com/?cloudshell=true).

![A screenshot of the Cloud Shell interface.](/static/shell/docs/images/used-console-with-editor.png)




Cloud Shell provides the following:

  * A temporary Compute Engine virtual machine instance.
  * A [built-in code editor](/shell/docs/editor-overview).
  * 5 GB of persistent disk storage.
  * Pre-installed gcloud CLI and other tools.
  * Language support for Java, Go, Python, Node.js, PHP, Ruby and .NET.
  * Web preview functionality.
  * Built-in authorization for access to Google Cloud console projects and resources.



For a list of `gcloud` commands, see the [`gcloud` reference](/sdk/gcloud/reference).

For more information about Cloud Shell, see [How Cloud Shell works](/shell/docs/how-cloud-shell-works).

### Client libraries

Google Cloud provides [client libraries](/sdk/cloud-client-libraries) that enable you to easily create and manage resources. Google Cloud client libraries expose APIs for two main purposes:

  * _App APIs_ provide access to services. App APIs are optimized for supported languages, such as Node.js and Python. The libraries are designed around service metaphors, so you can work with the services more naturally and write less boilerplate code. The libraries also provide helpers for [authentication and authorization](/docs/authentication).

  * _Admin APIs_ offer functionality for resource management. For example, you can use admin APIs if you want to build your own automated tools.




You also can use the [Google API client libraries](https://developers.google.com/api-client-library/) to access APIs for products such as Google Maps, Google Drive, and YouTube.

## Pricing

To learn how to explore and evaluate Google Cloud at no cost, see [Free Google Cloud features and trial offer](/free/docs/free-cloud-features).

To browse pricing details for individual services, see the [price list](https://cloud.google.com/pricing/list).

To estimate your total costs for running a specific workload on Google Cloud, see the [pricing calculator](https://cloud.google.com/products/calculator).

##  Try Google Cloud 

If you're new to Google Cloud, create an account to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Get started for free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-17 UTC."],[],[]] 

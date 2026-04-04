# Source: https://docs.salad.com/container-engine/explanation/core-concepts/architectural-overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SCE Architectural Overview

> The world's largest distributed GPU cloud at the most competitive prices

*Last Updated: May 29, 2025*

<iframe src="https://player.vimeo.com/video/1088518526?transparent=0" width="100%" height="470px" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="fullscreen" />

## What is SaladCloud Container Engine (SCE)?

SaladCloud Container Engine (SCE) is a decentralized global GPU cloud that operates as a two-sided marketplace
connecting PC owners (called "chefs") to businesses with compute-intensive workloads. Our chefs sell time on their
gaming PCs when they aren't in use—an average of 22 hours per day—while businesses deploy containerized workloads to
access affordable GPU compute power.

### Global Distribution at Scale

<img src="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/users_by_state_province_normalized_2025-04-20_to_2025-05-20.png?fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=5ba734f46dbd58dbaa51e372d1ffdbc4" alt="" data-og-width="4252" width="4252" data-og-height="2395" height="2395" data-path="container-engine/images/users_by_state_province_normalized_2025-04-20_to_2025-05-20.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/users_by_state_province_normalized_2025-04-20_to_2025-05-20.png?w=280&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=81aa4fe6f27653025e62449bcfc4e4cf 280w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/users_by_state_province_normalized_2025-04-20_to_2025-05-20.png?w=560&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=3e0f1348ad5bb3464b14752c11f886ea 560w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/users_by_state_province_normalized_2025-04-20_to_2025-05-20.png?w=840&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=0d401ae53a9d3a3d5b05ea2273f74fc7 840w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/users_by_state_province_normalized_2025-04-20_to_2025-05-20.png?w=1100&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=89548f6d511fa797fbd0cea96fb08aca 1100w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/users_by_state_province_normalized_2025-04-20_to_2025-05-20.png?w=1650&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=d88d4b09592466ddeac908a523e943b5 1650w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/users_by_state_province_normalized_2025-04-20_to_2025-05-20.png?w=2500&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=461107e07d04837e23324192e524e1de 2500w" />

SCE comprises tens of thousands of Salad nodes distributed across the global Internet, with chefs operating from 156
countries in a sampled 30 day period. These machines are spread across more than 1,300 states and provinces worldwide,
with distribution roughly following population density patterns.

**Hardware Diversity:**

* GPU types range from older GTX series GPUs to mid-range RTX 3060s (available in 98 countries) to high-end RTX 4090s
  (concentrated in 63 countries, primarily US, Canada, and UK)
* Each node is equipped with consumer GPUs and varying CPU and memory configurations
* Maximum node configuration: 16 vCPUs, 60 GB RAM, RTX 5090 with 32 GB VRAM
* Up to 250 GB of ephemeral storage available while instances are running

**Network Characteristics:**

* Many nodes are located in residential networks with asymmetric bandwidth
* Upload speeds are typically lower than download speeds
* Connections are predominantly over residential internet, often shared with other household devices

## How SCE Works Under the Hood

### Chef Infrastructure

Chefs download and install a Windows desktop application that allows them to configure their sharing preferences,
including:

* Whether to share GPU or CPU resources
* Bandwidth sharing preferences
* Types of workloads they're willing to accept

The application installs Salad Enterprise Linux (SEL) in Windows Subsystem for Linux 2 (WSL2), which:

* Manages container workload lifecycles
* Coordinates with the SaladCloud backend
* Provides security features including intrusion detection
* Automatically requests work when the chef is away and the machine is idle

### Workload Deployment Process

<img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao3.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=000fede98aa1d5618de6423d9e123571" data-og-width="1186" width="1186" data-og-height="1328" height="1328" data-path="container-engine/images/sce_ao3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao3.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=84378bc5cf46af8a2e6bf5d1d62ac89c 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao3.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=9b1f8aa5333e821db900a902d1acf79f 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao3.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=ab1ebe70141fef4344bcdff3718e8e66 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao3.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=9f344a811eaf21bbc55f16a0263ef956 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao3.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=859bdc956228625ab54d17256e301dc5 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao3.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=d677791af147f73ce3060cb8bac759a1 2500w" />

When you deploy a container group, the following process occurs:

1. **Image Distribution:** Your container image is pulled from your registry to our internal cache (only once to
   minimize egress fees)
2. **Node Allocation:** Compatible machines are selected based on your hardware requirements
3. **Image Deployment:** The cached image is distributed to allocated nodes
4. **Startup:** Containers start running your application

Startup times vary from minutes to longer periods depending on image size and network conditions, with some nodes
starting earlier than others.

## Container Group Architecture

A SCE application (container group) consists of multiple replicas (instances) running the same container image, with
each instance deployed on a separate Salad node.

**Important Distinctions:**

* SCE instances are **not virtual machines or physical machines** with attached volumes
* Both the image and runtime data are removed when applications stop
* **Docker-in-Docker is not permitted**
* Instances must have continuously running processes (web servers, job queue workers, etc.)

## Preparing Container Images

### Dockerfile Best Practices

<img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao1.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=ee32b142a27333036c61bc6f8cbc7c56" data-og-width="1376" width="1376" data-og-height="1414" height="1414" data-path="container-engine/images/sce_ao1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao1.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=ec76d6badf3faab0fab70e269285c8bc 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao1.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=654967a73c31ae9f42a7499c77e3fccb 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao1.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=6eee2f658436417ec67f843a36d72a07 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao1.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=d2265c50624d467b8a7d6dd8e2acf9a9 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao1.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=18cba7a1551308403fd126fa5ed106fe 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao1.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=1b54dc908cd045b4c9e76bfc98ec2f28 2500w" />

Create a Dockerfile that:

* Selects a base image with GPU support
* Adds necessary dependencies
* Copies your code and data
* Defines the default command to run
* Uses environment variables for configuration

**Example workflow:**

```Code  theme={null}
# Build and test locally
docker image build -t docker.io/saladtechnologies/misc:test -f Dockerfile .
docker run --rm -it --gpus all docker.io/saladtechnologies/misc:test

# Push to registry
docker push docker.io/saladtechnologies/misc:test
```

**Supported container image size:** Up to 35 GB (compressed)

### Environment Variables

Use environment variables to pass information to your applications:

* Customization settings (listening ports, request limits)
* External service access (cloud storage, databases, APIs)
* Configuration parameters

## Deployment Options

<img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao2.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=20390e6cf5ebe48fb7604ae293dd239d" data-og-width="2368" width="2368" data-og-height="1132" height="1132" data-path="container-engine/images/sce_ao2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao2.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=5198345ee092b1c4e5cd86aff040428d 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao2.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=6ea4832dc0aa55bbb1d69e73a29442d0 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao2.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=b1c352b08b97b45483f7a6afb301c538 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao2.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=bc1df3db382739ffed9b2749957943c0 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao2.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=bdf6d94fd660e4bc3aff9ddba9ff51bd 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao2.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=992184a8b77d634f495f518394c6c77a 2500w" />

### Portal vs API Deployment

Two deployment methods are available:

* **SaladCloud Portal:** Web-based interface for easy deployment
* **API:** Programmatic deployment with advanced features

**Advanced API Features:**

* Deploy in specific countries
* Deploy and use Job Queues
* More flexible configuration options

## Accessing Your Applications

### Real-Time Access Patterns

**Container Gateway (HTTP Load Balancer):**

* Best for tasks of approximately equal size
* Ideal for processing times under 100 seconds
* Free and extremely easy to set up
* Perfect for stable, predictable, relatively quick workloads

**When Container Gateway Works Well:**

* Tasks complete in well under 100 seconds
* Fairly predictable and stable demand
* Consistent task sizes (e.g., always 512x512 pixel images)

<img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao4.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=c17e838c7875f03fc997938a364fae71" data-og-width="1426" width="1426" data-og-height="1274" height="1274" data-path="container-engine/images/sce_ao4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao4.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=ffd1a993386634b74ca986d63a0f699f 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao4.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=a91cf72792a5cb6fdf09d09bfecfbb5f 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao4.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=c76aa287878b532efa1a6414c513fcc7 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao4.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=cab31f8f42fdd65f3e001aba875c3440 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao4.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=ca5ff143571458f4ff53e19550beeca2 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao4.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=920309ae5eef28c4a0b64bd44ca5bcf0 2500w" />

### Job Queue Patterns

**When to Use Job Queues:**

* Variable request sizes (1024x1024 images take 4x longer than 512x512)
* Tasks exceeding 100-second limit
* Long-running workloads (AI video generation, molecular simulations, model fine-tuning)
* Multi-model pipelines with different architectures

**Available Options:**

* **Salad Job Queue:** On-platform solution (API-only currently)
* **External Job Queues:** AWS SQS, Redis, and other popular solutions
* **Salad Kelpie:** Specialized for very long-running tasks and data synchronization with AWS S3-compatible storage

**Trade-offs:**

* Job queues introduce asynchronous patterns
* Require polling, webhooks, or other completion mechanisms
* More complex than direct HTTP responses

<img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao5.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=1e3af6339c239ebc832bd13a95ca997b" data-og-width="1270" width="1270" data-og-height="1058" height="1058" data-path="container-engine/images/sce_ao5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao5.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=325d6137c9da57e64b6cc1c8375b412f 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao5.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=33793561f862278892df0dba2e5bc311 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao5.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=4835174c1ec4258ae4f226ded4f10a35 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao5.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=157a138e1e77c98824f3802c1db29b86 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao5.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=25323612d3a73b48e76cd7c4e3114ba7 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao5.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=84857ea946325a1c4c3eaf128bbb1f7f 2500w" />

## Handling Distributed Cloud Challenges

### Hardware Heterogeneity

<img src="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/node-variability.png?fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=69f97a9798c8b116aa191ed0b7be6e62" alt="" data-og-width="1971" width="1971" data-og-height="1571" height="1571" data-path="container-engine/images/node-variability.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/node-variability.png?w=280&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=8f8d0638edc54b4805a5a3ecf5c2e274 280w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/node-variability.png?w=560&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=fbb51326c25336fef7c1352efae1948c 560w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/node-variability.png?w=840&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=fa1e0d115aced1d37270330c74d8a0dd 840w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/node-variability.png?w=1100&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=6d3fa5b978bab9f3ebed61c5ba76da6c 1100w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/node-variability.png?w=1650&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=1ff08f59ae8e7ec71aabf592dfdf0d73 1650w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/node-variability.png?w=2500&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=8ce44069d14a7c8515576535f55bfcc1 2500w" />

**Challenge:** Significant variability in hardware configurations

* Custom-built PCs, gaming rigs, former crypto miners
* Different CPUs, RAM speeds, storage types
* Network connections from WiFi to 10 Gigabit Ethernet

**Solutions:**

* Understand your performance bottlenecks
* Handle error cases unlikely in data centers
* Monitor system metrics (e.g., GPU temperature over time)
* Implement graceful degradation strategies

### Network Variability

**Challenge:** Heterogeneous networking conditions

* Point-in-time bandwidth measurements
* Residential internet with shared connections
* Variable latency and throughput

**Solutions:**

* Monitor bandwidth availability over time within your application
* Respond to network conditions in real-time
* Set appropriate minimum requirements for your workloads

### Data Transfer Optimization

**Challenge:** All nodes are out-of-region for major cloud providers

**Solutions:**

* Use egress-free storage (CloudFlare R2, etc.)
* Minimize data transfer costs
* Cache container images automatically (handled by SCE)

## Managing Interruptions

### Understanding Interruptions

**Key Characteristics:**

* Machines can be interrupted without warning at unpredictable times
* Similar to spot instances but no minimum uptime guarantees
* No advance notification events (unlike AWS spot instances)
* Various causes: power issues, network problems, users wanting to game

**Recent Performance Metrics:**

* Greater than 99% success rate on requests within one attempt
* Even higher success rates with single retry
* Particularly reliable for shorter tasks like image generation

### Automatic Recovery

**SCE Handles:**

* Automatic reprovisioning of interrupted nodes
* Maintaining desired replica counts
* No charges during container image download periods
* Background replacement of failed instances

**Your Application Handles:**

* Implementing retry logic for failed requests
* Graceful handling of 500-series errors
* Client-side request management

## Long-Running Tasks

### Data Persistence Strategy

**Challenge:** Local storage is ephemeral—completely erased when containers exit or nodes are interrupted

**Solutions for Short Tasks:**

* Model outputs returned promptly to users
* Minimal local storage requirements

**Solutions for Long Tasks:**

* Regular checkpoint saving to cloud storage
* Resume from checkpoints after interruptions
* Use tools with built-in checkpoint support (molecular simulation, model fine-tuning frameworks)
* Handle data transfer asynchronously to avoid blocking GPU tasks

<img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao7.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=40e0022f65823c9aad19b38565fc1042" data-og-width="1264" width="1264" data-og-height="1416" height="1416" data-path="container-engine/images/sce_ao7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao7.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=4cebc2b774d89dc7501fb732927e4601 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao7.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=4f4dbf8738ade5bae309033054e8a437 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao7.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=acad07530c1edfc3feda0c543eaa4d2c 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao7.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=ab17b42c5ea7ae38f9fbd55fbbbd9ddd 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao7.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=ce51eed02cfbf501d2558d555458b347 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao7.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=96814237c96de3680f57ab16b4ec2999 2500w" />

### Optimization Techniques

**Bandwidth Optimization:**

* Select nodes with better upload bandwidth by performing a bandwidth test on start
* Use multithreaded downloading/uploading tools (s3parcp)

**Data Management:**

* Separate cloud storage folders for each job
* Include input files, state files, and output files
* Jobs contain only data references, not actual data

<img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao6.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=329248b311bf6b26de9b1bb3de87221b" data-og-width="1556" width="1556" data-og-height="858" height="858" data-path="container-engine/images/sce_ao6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao6.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=b3592eada5f5bee599c76278645ed4be 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao6.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=aa90fe5fe7a8b844061f9168216fe9e5 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao6.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=57a7ade3b12360f2d69c0b9c6ac818e8 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao6.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=24bb057c61fd71f33122a832b15193b3 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao6.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=3eb147ba6a9e2cae70f3f32cfd850f1d 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sce_ao6.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=dd7bbc7148d888f49a1aa9db6b6431c8 2500w" />

## Security and Compliance

### Security Measures

**Data Protection:**

* Container images and configurations encrypted at rest and in transit
* Images only decrypted at runtime
* Environment variables decrypted and passed at runtime (not stored locally)
* Private registry credentials discarded immediately after image caching

**Network Security:**

* Inbound connections disabled by default
* Secure connections via WireGuard when enabled
* Runtime security monitoring with Falco intrusion detection
* Immediate workload shutdown and chef banning for security violations

**Platform Security:**

* SOC 2 compliant
* No known leaks or compromised workloads to date
* Demonstrated adherence to security, availability, processing integrity, confidentiality, and privacy standards

### Compliance Considerations

**Appropriate Workloads:**

* Most AI inference and GPU-intensive computations
* Molecular dynamics simulations
* Model fine-tuning and training
* Batch processing tasks

**Inappropriate Workloads:**

* HIPAA-regulated workloads
* Single-instance applications requiring high availability guarantees
* UI-based applications requiring consistent user sessions
* Database applications requiring persistent storage

## Use Cases and Optimization

### Ideal Scenarios

**Large-Scale Operations:**

* AI inference involving tens to thousands of GPUs
* GPU-intensive computations requiring massive parallelization
* Cost-sensitive workloads where price performance is critical

**Model Support:**

* SDXL/Flux image generation models
* Whisper Large speech recognition
* LLM 7B/8B/9B and quantized 13B/34B models
* Molecular dynamics simulations
* Text to Speech (TTS) models

### Performance Optimization

**Replica Strategy:**

* Increase replica counts to enhance reliability and throughput
* Additional replicas may reduce waiting times without extra costs, as only running replicas incur charges
* Balance system capacity and reliability requirements

**Hardware Selection:**

* Older GPUs may offer better price-performance ratios
* Consider trade-offs between speed and cost
* Evaluate user experience requirements vs. cost controls

**Autoscaling:**

There are two simple autoscaling strategies to match your compute capacity to workload demand:

1. Queue-based autoscaling: Automatically scale up/down based on the number of jobs in the queue. This can be handled
   automatically by the Salad Job Queue or Kelpie.
2. Custom Autoscaling: Implement your own autoscaling logic using the
   [SCE API](/reference/saladcloud-api/container-groups/update-container-group#body-replicas) to update the number of
   replicas based on real-time metrics you collect from your application.

### Cost Optimization

**Storage Strategy:**

* Use egress-free cloud storage
* Implement efficient data transfer patterns
* Leverage SCE's image caching to minimize registry costs

## Getting Started

### Documentation and Resources

**Essential Resources:**

* [SaladCloud Documentation](/)
* [Interactive API reference](/reference)
* [Detailed how-to guides for popular use cases](/container-engine/explanation/core-concepts/overview)
* [SaladCloud Blog](https://blog.salad.com):
  * Performance benchmarks across different GPU types
  * Optimal hardware configuration guides
  * Price-performance analysis
  * Real-world case studies and best practices

### Best Practices Summary

**Architecture Patterns:**

* Design for distributed, dynamic environments
* Implement robust error handling and retry logic
* Use external storage for data persistence
* Plan for variable startup times and node reallocations

**Development Workflow:**

1. Build and test containers locally with GPU support
2. Optimize for heterogeneous hardware environments
3. Implement appropriate access patterns (gateway vs. queue)
4. Design for interruptions and automatic recovery
5. Test at scale with multiple replicas

**Monitoring and Observability:**

* Implement application-level performance monitoring
* Track success rates and retry patterns
* Monitor resource utilization across nodes
* Set up alerts for critical application metrics
* While SaladCloud offers basic log and terminal access, consider integrating with external logging and monitoring
  solutions for advanced observability. We like Axiom.

SCE provides unprecedented scale and cost-effectiveness for GPU-intensive workloads while requiring thoughtful
architecture to handle the unique characteristics of a decentralized, consumer-hardware-based cloud platform.

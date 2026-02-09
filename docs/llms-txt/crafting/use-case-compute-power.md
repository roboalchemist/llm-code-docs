# Source: https://docs.sandboxes.cloud/docs/use-case-compute-power.md

# Overcome Local Machine Slowness

In this section, we discuss the use case of using Crafting to overcome local machine slowness in development. As the complexity increases in modern software development, the codebase becomes larger and larger and there are more and more services for developers to handle. The decades-old practice of solely relying local machine for software development is no longer fitting the needs of developers. Top issues developers facing nowadays with dev environments that hurts their productivity includes:

* With a large codebase, it takes significant amount of time to just index the code with a powerful IDE and start coding locally.
* It takes a long time to build the code locally and/or run unit tests, which consumes a lot of CPU and memory.
* The services a developer needs to run locally consumes too much memory and local IDE runs super slowly because of that.
* When using remote machines for development, insufficient management of the cloud VMs result in huge waste in computing resources and poor developer experience.

In the rest of this section, we talk about the following topics:

* [Benefits of powerful cloud machines](#benefits-of-powerful-cloud-machines)
* [Optimize resource utilization and minimize development cost](#optimize-resource-utilization-and-minimize-development-cost)
* [Hybrid development for combining local and cloud](hybrid-development-for-combining-local-and-cloud)

## Benefits of powerful cloud machines

We all know that a local desktop or laptop only has limited computation power. Starting from last century when PC becomes prevalent, developers have been mainly using their local machines for development. We are so used to the idea of coding locally and don't put enough thoughts into it even though the age of cloud has come to us. Almost every productivity software we use are on cloud, and yet we are used to rely on the local machine based dev environments, which is clearly insufficient and suboptimal in today's world.

Even with powerful laptops that costs several thousand dollars, they can only alleviate some pain in the development and can not scale much further beyond that. Needless to say more powerful means larger power consumption, heavier battery, and lots of heating, all leading to inconvenience to use. It's completely going against current technology trend of mobility, connectivity, and convenience.

<Image align="center" className="border" width="60% " border={true} src="https://files.readme.io/23a426f-use-case-compute.png" />

Nowadays, cloud machines can easily scale beyond 64 cores or 128 cores per machine with more than 256 GB memory or even 1 TB memory to use, which means a cloud machine can potentially offer much more computational resources than what a local machine can provide.

Beyond a single cloud machine, Crafting offers better automation possibility that one can leverage a pool of machines to perform the heavy task. While copying files such as built images and artifacts between local and cloud are often limited by local bandwidth, copying them between cloud machines are often lightening fast, which brings more potentials of speedup. With Crafting, the developers can really get a ready-to-code environment quickly online.

For large number of services or multiple codebases, Crafting's distributed model scales beyond a single machine to as much as the cloud can offer. Please see [Scale beyond Docker Compose](https://docs.sandboxes.cloud/docs/use-case-compose) and [Kubernetes Development and Testing](https://docs.sandboxes.cloud/docs/use-case-kubernetes) for details.

Furthermore, using a homogenous cloud dev environment greatly improves its stability and maintenance, as shown in [Maintainable Dev Environments](https://docs.sandboxes.cloud/docs/use-case-standardization)

## Optimize resource utilization and minimize development cost

No matter with local machines or cloud VMs, the computing resource is not free, and the insufficient utilization can easily cause huge waste. For example, a powerful MacBook Pro costs $4000+ USD a piece, but really how often are they used to its full capacity? A powerful cloud machine also incurs a high cost monthly, but in reality many of them are just allocated ready without doing any real computation for days, weeks, or even months.

In order to leverage more powerful machines on cloud for development, the optimization of utilization is very critical. Fortunately, Crafting tailors towards development use case, and provides huge opportunities in resource optimization. As shown in the table below, combining *Activity-based auto suspension* and *Sharing VM resources among multiple dev containers*, it can achieve over 90% of resource saving.

| Resource saving techniques                         | Estimated resource saving |
| :------------------------------------------------- | :------------------------ |
| Activity-based auto suspension                     | 70-80%                    |
| Sharing VM resources among multiple dev containers | 60-70%                    |
| Combined                                           | 90%+                      |

### Activity-based auto suspension

Developers are human-beings and we don't work 24/7. Even during the working hours, we often are engaging with other activities such as meetings, code reviews, etc. which don't require us to code on a computer. Having dev environments running on expensive machines during these "off-times" are obviously wasteful.

Crafting monitors activities on the sandbox and can detect whether it is actively used by a developer. If it's idle for some customizable period of time, it can automatically suspend the sandbox while saving ongoing work in the workspaces in the files system. This frees up the machine resource in the machine pool, which can be automatically scaled down or up depending on the load.

The auto-suspension threshold on Crafting can be set very aggressively, e.g. 30 minutes or even 15 minutes, thanks to its capability of *full state saving* and *fast resuming*:

* Unlike many ephemeral environments which destroys most of the files and needing developers to carefully backup their change, Crafting saves everything in persisted volume and allows developers to pick up where they left.
* With full state saved on persistent volume, resuming a suspended sandbox happens very quickly, without the need of reinitialize everything from the scratch.

The resuming of the sandbox can be triggered manually or by Crafting when it detects developer attempts to access a suspended sandbox. It offers a very smooth experience to developers.

In our experience, the activity based auto-suspension can save between 70% to 80% of the computing resource in regular use patterns.

### Sharing VM resources among multiple dev containers

Even during the time when developers code actively on a machine, they don't need the peak performance of the machine all the time. In fact, during most coding hours, all we need is some relatively lightweight text editor functionality even running with a powerful IDE. Only very occasionally developers engage heavy operations on their dev machine, such as building code, indexing new code with IDE, running tests, etc.

By default, Crafting organizes workspaces as dev containers and allow multiple containers running on a shared powerful VM. Each dev container sees the resource for the whole VM and can leverage its peak performance when needed, while allowing other dev containers to use the shared resources when it doesn't engage heavy operations. Given developers heavy operations typically run in burst and could finish quickly if the peak performance of the machine is high, this model can effectively save significant amount of resource without hurting developer experience.

In our experience, this resource sharing can save between 60% to 70% of the computing resource in most common cases.

## Hybrid development for combining local and cloud

With Crafting, developers don't need to adopt a new workflow in order to take advantage of power of the cloud to overcome slowness on their local machine. Instead, they can start the first step by using the hybrid development model which combines the familiar local environment and power of the cloud. Here we talk about a few common ways that people who still prefer coding locally use Crafting for hybrid development. You can pick whichever way that fits your need the best.

### Code locally, build and run remotely with code sync

Sometimes just writing code locally is not too bad with the local resource available, but it takes too much time for building the code and running the unit/integration tests just with the local machine. In this case, Crafting offers a convenient code sync functionality to keep your local code folder and the code folder in your Crafting workspace in sync. This way, you can offload the heavy operations of building and running tests onto cloud machines while still coding locally with your familiar process and IDEs. See [here](https://docs.sandboxes.cloud/docs/code-sync) for details.

### Code and run locally, with context services on remote with port forwarding

Sometimes it's even fine for coding and running a single service on local machine, but it becomes a problem when end-to-end testing of the flow requires many microservices to run alongside your service. In this case, you can:

* Code and run the service your work on locally
* Use Crafting to launch all other services in a sandbox on cloud
* Use Crafting's two-way traffic forwarding functionality to virtually plugin your local service into the sandbox, making it able to call and available to be called by other services.

This way, all the context services do not consume your valuable local CPU and memory, solving your local slowness issue. See [here](https://docs.sandboxes.cloud/docs/port-forwarding) for details.
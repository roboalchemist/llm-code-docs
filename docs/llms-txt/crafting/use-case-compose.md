# Source: https://docs.sandboxes.cloud/docs/use-case-compose.md

# Scale beyond Docker Compose

In this section, we will talk about the use case of how to use Crafting to do multi-service development scaling beyond docker compose.

For modern software development, it's common for professional developers to work with a number of services which collectively implement the functionalities of the product. Even when a product only relies on one main service, it is often needed to be supported by multiple dependencies such as PostgreSQL database, Redis cache, etc.

In order to have standardized and repeatable dev environments on their local machine, developers often leverage containerization and uses docker (with docker compose) to set up their multi-service dev environments. While it's certainly a step better than ad hoc dev environment, this setup has its own issues:

* It still runs all the services using computing resources on a local machine, which limits its scalability and causes slowness when the number of services needed are beyond a threshold.
* Docker adds a layer which introduces further CPU and memory overhead and sometimes incompatibility with local OS.
* Even containerized, the service running in docker is still subject to local CPU architecture, e.g., MacBook Pro M1 chip is arm architecture, which may be inconsistent with the production.

In the rest of this section, we discuss the two ways how people use docker compose for their dev environments and point out how to upgrade to Crafting to solve the issues mentioned above.

* [Everything in container for end-to-end environment setup](#everything-in-container-for-end-to-end-environment-setup)
* [Only dependencies in container to support local service dev](#only-dependencies-in-container-to-support-local-service-dev)

## Everything in container for end-to-end environment setup

One common way developers do to set up their dev environments with docker compose is to put every service they need in container and set up an end-to-end environment. The advantage of this setup is that everything is containerized and standardized, ensure end-to-end reliability, with the downside that developers need to edit code and run services inside containers, which can be tricky to set up.

Crafting can offer a near drop-in replacement for the setup given everything is already containerized and standardized, specifically:

* You can convert your the docker-based configuration (docker files and docker compose file) to Crafting `template` in a semi-automated way. This way, you can create standardized dev environments (`sandboxes`) on cloud to have everything end-to-end.
* As services are using service name + port to connect to each other in docker compose, the same pattern is used in Crafting sandbox on the overlay network.
* All the services will be running on cloud with production-like containers and do not consume local resource anymore. You can access the Internet facing endpoints for running the whole deployment end-to-end.
* For code editing, you can do one of the following ways based on your preference:
  * SSH to remote codebase and edit with terminal: ideal for text-based editors like vim, emacs, nano, etc.
  * Direct IDE access to remote codebase: Crafting supports VS code, and JetBrains IDEs such as IntelliJ, RubyMine, PyCharm, GoLand, etc.
  * Sync between local folder and cloud workspace: Crafting supports automatic file sync between any local folder and folder in cloud workspace, to make sure the file changes you made on your local file propagates to your cloud workspace as you edit the file.
  * Local mount of remote folders: Crafting supports sshfs to mount your folders in your cloud workspace to your local file system.

Using this approach, you can have a Crafting environment quickly set up based on your existing docker-based configurations and scale beyond the limits of a single machine.

## Only dependencies in container to support local service dev

Another common approach for developers to do is to put dependency services in containers while leaving the target service they work on and its codebase outside of containers. The advantage of this approach is that coding editing and running of the target service is done local natively without any indirection, and it can access its dependencies using port mapping between local and in-container.

For this type of setup, Crafting's hybrid development model fits perfectly as a drop-in replacement, specifically:

* You can launch a Crafting sandbox on cloud to host the services that your target service depends on, directly based on your docker compose file, with a single command of `cs docker-compose up`. The services running on cloud can leverage a pool of VMs, which scales well as your app are having more and more services.
* The local port mapping in docker compose can easily be handled as port forwarding on Crafting to the services running in sandbox. Your target service running locally can access its dependencies the same way as when they are run by docker compose.
* You still code, run, test, and debug your target service locally with your favorite desktop IDE that you are already using. The main difference is that instead of consuming your local resources, the dependencies consumes resources on cloud, which frees up your local CPU and memory for your IDE and local testing.

Using this hybrid approach, you can offload the heavy dependencies to cloud machines to support a great local dev experiences.
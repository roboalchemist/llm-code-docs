# Source: https://docs.jfrog.com/artifactory/docs/getting-started.md

# Get Started with Binary Management (DevOps)

JFrog Artifactory is the single solution for housing and managing all your software artifacts, AI/ML models, binaries, packages, files, containers, components, and releases used in and generated across your organization’s software supply chain. 

# What is JFrog Artifactory?

Artifactory serves as your central hub for DevOps and developers - integrating with your tools and processes to improve automation, capture attestation, ensure release integrity, and provide unrivaled visibility and governance across your development processes.

* For information on how Artifactory operates as a proxy for package registries and repositories, see [Work with Package Management](https://docs.jfrog.com/artifactory/docs/working-with-package-management).
* To better understand artifacts, packages and other objects in JFrog Artifactory, see [Understand Artifacts and Packages](https://docs.jfrog.com/artifactory/docs/understanding-artifacts-and-packages).

***

# Set up Artifactory

Before starting you need to set up Artifactory. If you haven't done this yet, see [Set up Artifactory ](/setup/docs/get-started).

***

# Connect your package manager or IDE

Once you've set up Artifactory as your universal artifact repository, you need to take three primary steps to begin using Artifactory as your artifact repository:

<Image align="center" src="https://files.readme.io/ad1c13c1f1ebe3acecdae11e8d98a5d9188cd19324c5b455e4fdc273a8d4d21f-setMeUp.png" />

* **Create an Artifactory Repository**\
  Create a local repository to share binaries with your colleagues, a remote repository to proxy requests from external artifact registries and repositories, or a virtual repository to combine the two. For more information, see [Get Started with Repositories](https://docs.jfrog.com/artifactory/docs/repository-management-overview). Note you need Admin permissions to create repositories.

* **Update your Package Manager Client**\
  Every developer in your organization needs to update their package manager client on their workstation to point to Artifactory. Instructions are different for every repository and registry and every package manager.
  * **Connect to your registry**: For more information, see [Connect your Package Manager or IDE to Artifactory](https://docs.jfrog.com/artifactory/docs/connect-your-package-manager-to-artifactory) and follow the instructions for the specific registry or repository (e.g. Docker, Maven).
  * **Copy commands for Configuration**: via the set me up functionality to use for configuring your package manager. For more information, see [Use Artifactory Set Me Up for Configuring Package Manager Clients](https://docs.jfrog.com/artifactory/docs/use-artifactory-set-me-up-for-configuring-package-manager-clients).

* **Push and Pull Images**\
  Once you've created a repository and updated your package manager, you can begin to work. For more information see [Upload and Download Packages using Artifactory](https://docs.jfrog.com/artifactory/docs/upload-and-download-packages-using-artifactory).

Read about how Artifactory operates as your package manager in [Work with Package Management](https://docs.jfrog.com/artifactory/docs/working-with-package-management).

***

# Search for Artifacts and Packages

Get some guidance on [Searching for Artifacts and Packages](https://docs.jfrog.com/artifactory/docs/understanding-how-to-search-for-artifacts-and-packages), see [Supported Search Methods](https://docs.jfrog.com/artifactory/docs/supported-search-methods) and read about [Browsing Artifacts](https://docs.jfrog.com/artifactory/docs/browsing-artifacts).

***

# Learn about and work with Artifactory

<Cards columns={3}>
  <Card title="See Supported Package Types" href="/artifactory/docs/supported-package-types">
    See the list of the more than 50 registries and repositories supported by JFrog Artifactory.
  </Card>

  <Card title="Read Package Management Use Cases" href="/artifactory/docs/package-and-repositories-use-cases">
    Learn about package caching and proxying with Artifactory and about managing machine learning operations.
  </Card>

  <Card title="Learn about Package Management" href="/artifactory/docs/working-with-package-management">
    See how artifactory operates as your central package and artifact repository. Learn how to efficiently search and find your artifacts.
  </Card>

  <Card title="Get Started with the JFrog Trial" href="https://jfrog.com/start-free/try-cloud/" target="_blank">
    Not yet started? Register for the JFrog Trial and begin managing packages and artifacts.
  </Card>

  <Card title="Work with JFrog Repositories" href="/artifactory/docs/repository-management">
    Learn about the different types of repositories in JFrog, how to create and configure them and understand their purposes.
  </Card>

  <Card title="Distribute Packages" href="/artifactory/docs/jfrog-distribution">
    Use Artifactory to distribute artifacts and release bundles across edges.
  </Card>
</Cards>

<InjectContentHeadHeroStyles />
# Source: https://docs.vespa.ai/en/basics/deploy-an-application-local-java.html.md

# Deploy an application having Java components locally

 

Follow these steps to deploy a Vespa application having Java components on your own machine.

Alternative versions of this guide:

- [Deploy an application using pyvespa](https://vespa-engine.github.io/pyvespa/getting-started-pyvespa-cloud.html) - for Python developers
- [Deploy an application](deploy-an-application.html)
- [Deploy an application having Java components](deploy-an-application-java.html)
- [Deploy an application without Vespa CLI](deploy-an-application-shell.html)
- [Deploy an application without Java components locally](deploy-an-application-local.html)

This is tested with _vespaengine/vespa:8.634.24_ container image.

  

**Prerequisites:**

- Linux, macOS or Windows 10 Pro on x86\_64 or arm64, with [Podman Desktop](https://podman.io/) or [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed, with an engine running. 
  - Alternatively, start the Podman daemon:
```
$ podman machine init --memory 6000
$ podman machine start
```
  - See [Docker Containers](/en/operations/self-managed/docker-containers.html) for system limits and other settings.

- For CPUs older than Haswell (2013), see [CPU Support](/en/cpu-support.html).
- Memory: Minimum 4 GB RAM dedicated to Docker/Podman. [Memory recommendations](/en/operations/self-managed/node-setup.html#memory-settings). 
- Disk: Avoid `NO_SPACE` - the vespaengine/vespa container image + headroom for data requires disk space. [Read more](/en/writing/feed-block.html). 
- [Homebrew](https://brew.sh/) to install the [Vespa CLI](/en/clients/vespa-cli.html), or download the Vespa CLI from [Github releases](https://github.com/vespa-engine/vespa/releases). 
- [Java 17](https://openjdk.org/projects/jdk/17/).
- [Apache Maven](https://maven.apache.org/install.html) is used to build the application.

Steps:

1. **Validate the environment:**

2. **Install the [Vespa CLI](../clients/vespa-cli.html)** using [Homebrew](https://brew.sh/):

3. **Set local target:**

4. **Start a Vespa Docker container:**

5. **Clone a sample [application](applications.html):**

6. **Build it:**

7. **[Deploy](applications.html#deploying-applications) the application:**

8. **[Feed](../writing/reads-and-writes.html) [documents](../schemas/documents.html):**

9. **Run [queries](../querying/query-api.html):**

  

Congratulations, you have deployed your first Vespa application!

  

#### Next: [Vespa applications](applications.html)

```
$ docker rm -f vespa
```

 Copyright © 2026 - [Cookie Preferences](#)


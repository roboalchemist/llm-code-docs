# Source: https://docs.earthly.dev/ci-integration/vendor-specific-guides/jenkins.md

# Source: https://docs.earthly.dev/earthly-0.7/ci-integration/vendor-specific-guides/jenkins.md

# Source: https://docs.earthly.dev/earthly-0.6/ci-integration/vendor-specific-guides/jenkins.md

# Jenkins

## Overview

Jenkins has multiple modes of operation, and each of them require some consideration when installing Earthly. These modes include:

* Standalone, dedicated runners
* Ephemeral cloud runners

### Compatibility

Earthly has been tested with Jenkins in a standalone runner configuration, and using the Docker Cloud provider.

### Resources

* [Installing Jenkins](https://www.jenkins.io/doc/book/installing/)
* [Docker Cloud Plugin](https://plugins.jenkins.io/docker-plugin/)
* [Jenkins Credentials](https://www.jenkins.io/doc/book/using/using-credentials/)

## Setup (Standalone)

This should not differ in any meaningful way from the steps outlined in the [overview](https://docs.earthly.dev/earthly-0.6/ci-integration/overview).

## Setup (Docker Cloud)

Assuming you are following the steps outlined in the [overview](https://docs.earthly.dev/earthly-0.6/ci-integration/overview), here are the additional things you need to configure:

### Dependencies

Ensure that the Docker Cloud provider is installed and has a Docker daemon available. The Cloud provider does not provide a daemon.

### Installation

You'll need to [create your own runner image](https://docs.earthly.dev/earthly-0.6/ci-integration/build-an-earthly-ci-image). Heres an example of what this might look like, when basing your runner off our `earthly/earthly` image:

```docker
ARG VERSION=4.9
RUN apk add --update --no-cache curl bash git git-lfs openssh-client openssl procps \
  && curl --create-dirs -fsSLo /usr/share/jenkins/agent.jar https://repo.jenkins-ci.org/public/org/jenkins-ci/main/remoting/${VERSION}/remoting-${VERSION}.jar \
  && chmod 755 /usr/share/jenkins \
  && chmod 644 /usr/share/jenkins/agent.jar \
  && ln -sf /usr/share/jenkins/agent.jar /usr/share/jenkins/slave.jar \
  && apk del curl
```

`VERSION` is the version of the Jenkins runner to install.

### Configuration

Set `DOCKER_HOST` to point at a Docker daemon. This can easily be passed through by checking "Expose Docker Host" in the runner template configuration.

## Additional Notes

`earthly` misinterprets the Jenkins environment as a terminal. To hide the ANSI color codes, set `NO_COLOR` to `1`.

## Example

{% hint style="danger" %}
**Note**

This example is not production ready, and is intended to showcase configuration needed to get Earthly off the ground. If you run into any issues, or need help, [don't hesitate to reach out](https://github.com/earthly/earthly/issues/new)!
{% endhint %}

You can find our [Jenkins example on GitHub](https://github.com/earthly/ci-examples/tree/main/jenkins).

To run it yourself, clone the [`ci-examples` repository](https://github.com/earthly/ci-examples), and then run (from the root of the repository):

```go
earthly ./jenkins+start
```

This will start a local Jenkins server, minimally configured to spawn `earthly` builds using the Docker cloud plugin.

To run a build in this demo, you will need to configure a build pipeline. To do that, we have an [example project with a Jenkinsfile](https://github.com/earthly/ci-example-project). To configure the build pipeline for the example project:

* Open the Jenkins demo by going to [`http://localhost:8000`](http://localhost:8080/)
* Click "New Item", on the left

![Jenkins Dashboard with "New Item" highlighted](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-a3c78a2f3fc1b7c01948c0af5afb9dff68a3b832%2FJenkins1.png?alt=media\&token=8495fce5-6b8e-49bb-b57f-5188efe8ddba)

* Choose "Pipeline", give it a name (we chose "test"), and click "OK".

![Setting up a new build named test, configured as a Jenkins pipeline](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-c19da450d4ced10665975091f71d1428fde3068a%2FJenkins2.png?alt=media\&token=49995cd3-a3e6-46b8-afbb-f2431137a6cb)

* Scroll down to the "Pipeline" section.
* Make the following changes:
  * Choose "Pipeline script from SCM" for the Definition
  * Choose "Git" as the SCM, once the option appears
  * Set the repository URL to [`https://github.com/earthly/ci-example-project`](https://github.com/earthly/ci-example-project)
  * Set the branch specifier to `*/main`

![Configuring all the SCM options for the build](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-9cb6cb853ddff24260c7c0537c7adc52c89e2123%2FJenkins3.png?alt=media\&token=53c50e46-5a1a-466f-beb9-d1639b5c5d2c)

* Once those changes are made, click "Save". Jenkins will navigate to the Pipelines' main page. Once there, click "Build Now"

![Jenkins Dashboard for the example build, with "Build Now" highlighted](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-658373b8da1329a16dc8475ac6cd874f4fc4b478%2FJenkins4.png?alt=media\&token=1c72569f-b9dc-4183-8065-953e555dc6bb)

* Find the build in your build history, and watch it go!

![Console output in Jenkins from the test build](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-c5fc322f475f328bc2811f3f51f630c2de03ee88%2FJenkins5.png?alt=media\&token=15172bf6-e278-407a-8b41-a0f49340f10f)

### Notes

If you broke the example environment, you can run `earthly ./jenkins+cleanup` to clean up before trying to run again from scratch.

#### TLS

The example purposely runs a Docker-In-Docker (DIND) container without TLS for simplicity. This is *not* a recommended configuration. [Configuring TLS inside Docker.](https://docs.docker.com/engine/security/protect-access/#use-tls-https-to-protect-the-docker-daemon-socket)

To allow the `docker` client to access a daemon protected with TLS, you will need to add Jenkins credentials. Add the client key, certificate, and the server CA certificate as a credential. In our example, using the Docker Cloud provider, you can add them by choosing "Manage Jenkins", then "Manage Nodes and Clouds", and finally "Configure Clouds". Then, choose the cloud to configure for TLS, and click the "Add" button here:

![Configuring Docker credentials in Jenkins](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-e9eb085606c725a68c81ba87548dd274faa87613%2FJenkins6.png?alt=media\&token=0ab7bb30-fe14-42f4-9984-709044636053)

Also, ensure that you are using the correct port for TLS. In this image of our example cloud, we are using port `2375`, which is traditionally the insecure port for a `docker` daemon. In a TLS environment, `docker` expects port `2376`.

If you are using an external `earthly-buildkitd` with Jenkins, [you should be using mTLS](https://docs.earthly.dev/earthly-0.6/ci-integration/remote-buildkit). You will need to add the keys and certificates used there as credentials too.

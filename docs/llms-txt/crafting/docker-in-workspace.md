# Source: https://docs.sandboxes.cloud/docs/docker-in-workspace.md

# Docker in Workspace

The workspace has integrated docker CLI and daemon and will automatically start the docker daemon on the first time it's being used. For isolation and security, the docker daemon is only allowed to run in rootless mode.

### Use My Own Docker Installation

If the version of docker daemon provided by the workspace is not the desired one, you can install the full docker suite yourself. Here's an example of installing your own owner version (take `24.0.6` as an example):

```shell
curl -sSfL https://download.docker.com/linux/static/stable/x86_64/docker-24.0.6.tgz | sudo tar -C /usr/local -xz
sudo mv /usr/local/docker/docker /usr/local/bin/
```

After the workspace restarts (e.g. suspend/resume), the next time using docker, it will be the version you installed.

### Install buildx

The command `docker buildx` is provided by the [buildx docker CLI plugin](https://github.com/docker/buildx). Install it on Crafting sandbox is straightforward (please change the version in the URL accordingly):

```shell
sudo mkdir -p /usr/local/lib/docker/cli-plugins
sudo wget -O /usr/local/lib/docker/cli-plugins/docker-buildx https://github.com/docker/buildx/releases/download/v0.11.2/buildx-v0.11.2.linux-amd64
sudo chmod a+rx /usr/local/lib/docker/cli-plugins/docker-buildx
```

Now you can use `docker buildx`

### Install buildkit

[buildkit](https://github.com/moby/buildkit) provides extended capabilities for building container images, including multi-arch images etc. The installation on Crafting sandbox is straightforward (please change the version in the URL accordingly):

```shell
curl -sSfL https://github.com/moby/buildkit/releases/download/v0.12.2/buildkit-v0.12.2.linux-amd64.tar.gz | sudo tar -C /usr/local -zx
```

Then run it as a daemon by adding the file `/etc/sandbox.d/daemons/buildkit.yaml`

```yaml
name: buildkit
run:
  cmd: |
    mkdir -p /run/buildkit
    chown -R owner:owner /run/buildkit
    buildkitd --rootless --group owner
```

Now you can use `buildctl`.

The `buildkit.yaml` can also be embedded in the Template (see details in [Workspace System](https://docs.sandboxes.cloud/docs/sandbox-definition#workspace-system), for example:

```yaml
workspaces:
- name: example
  system:
    daemons:
    - name: buildkit
      run:
        cmd: |
          mkdir -p /run/buildkit
          chown -R owner:owner /run/buildkit
          buildkitd --rootless --group owner
```

#### Example buildkit as docker builder

The buildkit socket can be registered as a docker remote builder. Update the daemon as:

```yaml
name: buildkit
run:
  cmd: |
    docker buildx inspect buildkit >/dev/null 2>&1 || docker buildx create --name buildkit --platform linux/amd64,linux/arm64 --driver remote unix:///run/buildkit/buildkitd.sock
    mkdir -p /run/buildkit
    chown -R owner:owner /run/buildkit
    buildkitd --rootless --group owner
```

To build, use `docker buildx build --builder=buildkit ...`

### Pull Image from Private ECR

After setting up AWS Access (please refer to [AWS Setup](https://docs.sandboxes.cloud/docs/cloud-resources-setup#aws-guide)), use [AWS ECR credential helper](https://github.com/awslabs/amazon-ecr-credential-helper) to enable private ECR access without storing credentials. If not already installed, install using:

```shell Shell
sudo curl -o /usr/local/bin/docker-credential-ecr-login -sSfL https://amazon-ecr-credential-helper-releases.s3.us-east-2.amazonaws.com/0.7.1/linux-amd64/docker-credential-ecr-login
sudo chmod a+rx /usr/local/bin/docker-credential-ecr-login
```

And add the following to file `~/.docker/config.json`:

```json
{
  "credHelpers": {
		"<aws_account_id>.dkr.ecr.<region>.amazonaws.com": "ecr-login"
	}
}
```

Then try with `docker pull <aws_account_id>.dkr.ecr.<region>.amazonaws.com/...`
<!-- Source: https://docs.verda.com/clusters/instant-clusters/containers.md -->

# Containers

We present here a basic test for containerized environments using [Enroot](https://github.com/NVIDIA/enroot) and [Pyxis](https://github.com/NVIDIA/pyxis), both from NVIDIA.

First, for testing enroot:

```bash
enroot import docker://ubuntu
enroot create -n ubuntu ubuntu.sqsh
enroot start ubuntu sh -c 'grep PRETTY /etc/os-release'
> PRETTY_NAME="Ubuntu 24.04.2 LTS"
```

Secondly, we ensure we get the same results from testing Pyxis:

```bash
srun --container-image=ubuntu grep PRETTY /etc/os-release
> PRETTY_NAME="Ubuntu 24.04.2 LTS"
```

Alternatively to use a custom image built in dockerd:

1. Build a custom dockerfile with:

   ```bash
   docker build -f <file.dockerfile> -t <name:tag> .
   ```

1. [Import](https://github.com/NVIDIA/enroot/blob/master/doc/cmd/import.md) dockerd image to Enroot (Can be done with `docker://IMAGE:TAG` from registry)

   ```bash
   enroot import dockerd://<name:tag>
   ```

1. Use flag pointing to the <name:tag>.sqsh

   ```bash
   --container-image=<name:tag>.sqsh
   ```

## Example: torchtitan multi-node

We clone cluster-tests into `/home/ubuntu`:

```bash
git clone https://github.com/datacrunch-research/cluster-tests.git /home/ubuntu/cluster-tests
```

We build the image based on [torchtitan.dockerfile](https://github.com/datacrunch-research/cluster-tests/blob/main/containers/torchtitan.dockerfile):

> NOTE: we need to include the HF\_TOKEN in .bashrc or export it in the bash session with access granted for llama3 family models.

```bash
docker build -f torchtitan.dockerfile --build-arg HF_TOKEN="$HF_TOKEN" -t torchtitan_cuda128_torch27 .
```

Then we import the squash file, which Enroot will use:

```bash
enroot import -o /home/ubuntu/torchtitan_cuda128_torch27.sqsh dockerd://torchtitan_cuda128_torch27
```

Now, we execute [torchtitan\_multinode.sh](https://github.com/datacrunch-research/cluster-tests/blob/main/containers/torchtitan_multinode.sh):

```bash
sbatch torchtitan_multinode.sh
```

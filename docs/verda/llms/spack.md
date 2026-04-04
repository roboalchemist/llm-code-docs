# Source: https://docs.verda.com/clusters/instant-clusters/spack.md

# Environments

In the cluster one can use Python environments through preinstalled [uv](https://github.com/astral-sh/uv), for example if you to initiate a Pytorch environment run the following command from any user profile:

```bash
bash /home/pytorch.setup.sh
```

This command will install [Pytorch 2.8](https://pytorch.org/) with cuda 12.9 using the uv package manager.

## Spack

Alternatively you can build your packages using [Spack](https://spack.readthedocs.io/en/latest/index.html). Spack is an open-source package manager that allows the developers to easily manage multiple versions of the same software and its dependencies, for example by allowing to quickly switch between multiple `CUDA` or `gcc` versions.

## Installation

Let's get started with Spack on Verda instant cluster!

On your first boot, Spack is not added to your shell by default. To initialize Spack, please run:

```bash
. /home/spack/spack/share/spack/setup-env.sh
```

The above can also be added to your `.bashrc` to have Spack commands always available on login.

## Basic usage

We recommend you consult [Spack documentation](https://spack.readthedocs.io/en/latest/basic_usage.html) to learn more about its features. Below, we provide some basic examples.

You can make the specific version of a package active by running `spack load package@version` and conversely, deactivating it by running `spack unload package`. Behind the scenes, Spack handles the above by prepending to the `$PATH` environment variable.

### Example commands

List the currently installed packages:

```bash
spack find
```

On a freshly installed cluster this should provide output similar to:

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-421eddfaa9911dd2f097239730b66a1436ca4c0b%2Fspack-1.png?alt=media" alt=""><figcaption></figcaption></figure>

To find info on all installable versions of Nvidia CUDA:

```bash
spack info cuda
```

To install CUDA version 12.6.2:

```bash
spack install cuda@12.6.2
```

Once the package has been installed load it with:

```bash
spack load cuda@12.6.2
```

Verify that the package has been loaded:

```bash
spack find --loaded | grep cuda
```

Now the Nvidia CUDA Compiler path will be set to the Spack module corresponding to the loaded CUDA version:

```bash
which nvcc
```

Should output something like:

```bash
/home/spack/spack/opt/.../cuda-12.9.0-fguwwqog63caubyxg2q4mgcce5n5rmrv/bin/nvcc
```

## Troubleshooting

The Spack setup script is available here: `/usr/local/bin/spack.setup.sh`. If you for any reason delete your `/home/spack` directory, you can recreate it by running the above script.

We recommend you read `spack.setup.sh` before using it. It for example compiles NCCL with `cuda_arch=100a,90a` which might not be the right choice for you.

<!-- Source: https://namespace.so/docs/reference/cli/build -->

# nsc build

Build container images using [Namespace Remote Builders](/docs/solutions/docker-builders).

`build` builds a container image using provided `Dockerfile` and a "context".
A build's context is the set of files located in the specified `PATH`. The built
image can be either pushed to the target image registry or loaded to the local
docker registry.

## Usage

```
nsc build PATH [-f <Dockerfile>] [-t <tag[,tag]>] [-n <name[,name]>] [--build-arg <arg[,arg]>] [--platform <platform[,platform]>] [--push] [--load]
```

### Example

The following builds an image with name **app** using
docker file in the current directory (e.g. `./Dockerfile`) and pushes it to the user's
Workspace Container Registry (e.g. `nscr.io/8enum0hp1l5ii`).

```
$ nsc build . --name app --push
 
  Pushed for linux/amd64:
    nscr.io/8enum0hp1l5ii/app:latest
```

You can tag and push the container image to any Container Registry of your choice.
For example, the following would push to GitHub Container Registry.

```
$ nsc build . --tag ghcr.io/apprepo/app --push
 
  Pushed for linux/amd64:
    ghcr.io/apprepo/app:latest
```

`nsc build` uses your local Docker credentials provider. So to push images to container registries, you need to log in with `docker login`

## Options

### -f <Dockerfile>

To specify a Dockerfile to build. By default `PATH/Dockerfile` is used.

### -t <tag[,tag]>

Set the image name and optionally a tag (format: "name:tag"). This option can
accept multiple values as an input separated by a comma.

### -n <name[,name]>

Similarly to `-t`, it sets the image name and optionally a tag (format: "name:tag").
It automatically specifies the Workspace Registry repository as part of the tags (i.e. `nscr.io/<workspace ID>`).
This option can accept multiple values as an input separated by a comma.

### --build-arg <arg[,arg]>

This flag allows you to pass the build-time variables that are accessed like
regular environment variables in the `RUN` instruction of the Dockerfile.

### --platform <platform[,platform]>

Set the target platform for the build. The default value is the platform of the
local host. The value takes the form of `os/arch` or os/arch/variant.
For example, `linux/amd64` or `linux/arm/v7`.

This option can accept multiple values as an input separated by a comma. With
multiple values the result will be built for all the specified platforms and
joined together into a single manifest list.

### --push

Specify the option to push the build result to registry. `nsc` will push images
for all the provided with `-t` or `-n` options tags.

### --load

Specify the option to automatically load the single-platform build result to
the local docker registry. Note that `--load` doesn't support multi-platform
image builds.

### --secret

A secret to expose to the build. Format: `id=ID[,src=FILEPATH][,env=VARIABLE]`.
See also [build secrets usage](https://docs.docker.com/build/building/secrets/#using-build-secrets).

Last updated July 4, 2025

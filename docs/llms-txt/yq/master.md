# Source: https://mikefarah.gitbook.io/yq/v3.x/master.md

# yq

&#x20;![Build](https://github.com/mikefarah/yq/workflows/Build/badge.svg) ![Docker Pulls](https://img.shields.io/docker/pulls/mikefarah/yq.svg) ![Github Releases (by Release)](https://img.shields.io/github/downloads/mikefarah/yq/total.svg) ![Go Report](https://goreportcard.com/badge/github.com/mikefarah/yq)

## Deprecated Notice

v3 is now deprecated, critical bug fixes and security fixes will still be applied until August 2021.

## Install

`yq` has pre-built binaries for most platforms - checkout the [releases page](https://github.com/mikefarah/yq/releases) for the latest build. Alternatively - you can use one of the methods below:

### MacOs / Linux via Homebrew:

```bash
brew install yq@3
```

Note that as this is a versioned brew it will not add the `yq` command to your path automatically. Please follow the instructions given by brew upon installation.

### On Windows:

```bash
choco install yq
```

Kindly maintained by @chillum (<https://github.com/chillum/choco-packages/tree/master/yq>), <https://chocolatey.org/packages/yq>

### Alpine Linux

* Enable edge/community repo by adding `$MIRROR/alpine/edge/community` to `/etc/apk/repositories`
* Update database index with `apk update`
* Install yq with `apk add yq`

Supported by Tuan Hoang <https://pkgs.alpinelinux.org/package/edge/community/x86/yq>

### On Ubuntu and other Linux distributions supporting `snap` packages:

```bash
snap install yq --channel=v3/stable
```

#### Snap notes

`yq` installs with with [*strict confinement*](https://docs.snapcraft.io/snap-confinement/6233) in snap, this means it doesn't have direct access to root files. To read root files you can:

```bash
sudo cat /etc/myfile | yq r - somecommand
```

And to write to a root file you can either use [sponge](https://linux.die.net/man/1/sponge):

```bash
sudo cat /etc/myfile | yq r - somecommand | sudo sponge /etc/myfile
```

or write to a temporary file:

```bash
sudo cat /etc/myfile | yq r - somecommand | sudo tee /etc/myfile.tmp
sudo mv /etc/myfile.tmp /etc/myfile
rm /etc/myfile.tmp
```

### On Ubuntu 16.04 or higher from Debian package:

```bash
sudo add-apt-repository ppa:rmescandon/yq
sudo apt update
sudo apt install yq -y
```

Kindly maintained by @rmescandon

### go get:

```
GO111MODULE=on go get github.com/mikefarah/yq/v3
```

## Docker

Oneshot use:

```bash
docker run --rm -v ${PWD}:/workdir mikefarah/yq yq [flags] <command> FILE...
```

Run commands interactively:

```bash
docker run --rm -it -v ${PWD}:/workdir mikefarah/yq sh
```

It can be useful to have a bash function to avoid typing the whole docker command:

```bash
yq() {
  docker run --rm -i -v ${PWD}:/workdir mikefarah/yq yq $@
}
```

## Parsing engine and YAML spec support

Under the hood, yq uses [go-yaml v3](https://github.com/go-yaml/yaml/tree/v3) as the yaml parser, which supports [yaml spec 1.2](https://yaml.org/spec/1.2/spec.html). In particular, note that in 1.2 the values 'yes'/'no' are no longer interpreted as booleans, but as strings.

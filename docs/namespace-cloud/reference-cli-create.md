<!-- Source: https://namespace.so/docs/reference/cli/create -->

# nsc create

Create a new instance.

`create` starts a fresh Namespace instance in an ephemeral and isolated environment.
Namespace instances include a ready-to-use Kubernetes by default.
The Kubernetes distribution is [k3s](https://k3s.io/). The environment is uniquely identified
by an *instance ID*. You can specify the machine shape you need and a file to output the instance ID.
For example:

## Usage

```
nsc create [--machine_type [os/arch:]<cpu>x<mem>] \
    [--selectors <name1=value1,name2=value2>] \
    [--output_to <path>] \
    [--wait_kube_system]
```

### Example

The following example creates a new ephemeral Kubernetes instance with the
default machine shape (4 CPUs and 8 GiB of memory).

```
$ nsc create
  Created instance "h9am86n6gi25m"
    deadline: 2023-04-25T08:48:38Z
```

The below command creates a Kubernetes instance with 4 CPUs and 16 GiB of memory. Then, it writes the
instance ID into a file, which is especially useful for writing automation programs around `nsc` CLI.

```
$ nsc create --machine_type 4x16 --output_to /tmp/instance_id
  Created instance "hrc4b9nvoj7ki"
    deadline: 2023-04-25T08:58:58Z
 
$ cat /tmp/instance_id
  hrc4b9nvoj7ki
```

Availability of [machine shapes](/docs/architecture/compute/machine-shapes) is subject to your plan and your remaining concurrency.

## Options

### --machine\_type [os/arch:]<cpu>x<mem>

Specifying the machine shape. Namespace supports arbitrary machine shapes that
use any of [2, 4, 8, 16, 32] as CPU value, and [2, 4, 8, 16, 32, 64, 80, 96, 112, 128, 256, 384, 512]
as RAM value, with the constraint that RAM must always be larger or equal to CPU.

Instances of different architectures and operating systems can be started by
prepending `os/arch` to the machine shape. For example: `nsc create --machine_type linux/arm64:2x8` starts a 2 vCPU 8GB RAM, ARM64 machine running
Linux.

[Learn more about available Machine Shapes](/docs/architecture/compute/machine-shapes)

### --output\_to <path>

Write the *instance ID* to file. If file already exists, it will get overwritten.

### --wait\_kube\_system

If specified, `nsc` will wait until resources in `kube-system` Kubernetes
namespace are ready.

### --selectors

When starting a macOS instance select the desired base image based on properties specified as key-value pairs.
[Available Selectors](/docs/architecture/compute/macos#available-selectors).

### --label key=value

Annotate the new instance with the specified values. Multiple values can be
specified. They are rendered by default in the web UI, and can be used for
programmatic instance filtering.

### --duration

Specify how long an ephemeral environment should live for. E.g. `--duration 10m`.

### --bare

If set to true, `nsc` creates an environment with the minimal set of services (e.g. no Kubernetes).
Typically, it is used to create a remote instance to run containers.

### --volume

Attach a volume to the instance. It follows the format `{cache|persistent}:{tag}:{mountpoint}:{size}`, e.g. `cache:mytag:/cache:50gb`.
In case you select `cache` volume type, check how [Cache Volumes](/docs/architecture/storage/cache-volumes) work.

### --ingress

Configures the ingress of this instance. Valid options: wildcard.

## Experimental features

New features are often initially introduced under `experimental`.
Features here may graduate to be fully supported, or may end up being removed.

In order to use experimental features, pass `--experimental_from` pointing at a
json file where the features you want to use are specified.

Currently, the following experimental features are available:

- `disks`: specify an additional set of images to attach to the ephemeral
  environment. Each disk is created from a flattened container image, which you
  specify. And is mounted under `/disk/<name>`.

  **Note**: Currently only public images are supported. Private registries (like `nscr.io`) won't work.
- `containerd_shims`: specify an additional set of containerd shims to configure
  containerd with.

Example:

```
{
	"disks": [
		{
			"name": "gvisor",
			"image": "..."
		}
	],
	"containerd_shims": [
		{
			"name": "runsc",
			"runtime_type": "io.containerd.runsc.v1",
			"add_to_path": ["/disk/gvisor"]
		}
	]
}
```

Last updated October 17, 2025

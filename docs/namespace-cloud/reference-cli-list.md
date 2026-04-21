<!-- Source: https://namespace.so/docs/reference/cli/list -->

# nsc list

Print the list of all your instances.

`list` prints the list of all instances of the current workspace user logged in
into. The output table contains:

- instance ID
- number of CPUs and GiB of memory allocated to the instance
- instance architecture (*amd64* or *arm64*)
- created time
- time to live
- instance purpose (e.g. created manually or from CI)

## Usage

```
nsc list [-o <plain|json>]
```

### Example

The following example prints the list of instance in a human-friendly format:

```
$ nsc list
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Instance ID    CPU  Memory   Arch   Created         Time to live         Purpose                                         │
│──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────│
│ 1lf2ol9ioulce  4    4.0 GiB  amd64  5 minutes ago   24 minutes from now  Manually created from CLI                       │
│ ovkbmemc7qbp2  16   32 GiB   amd64  5 minutes ago   3 hours from now     GH Action: namespacelabs/foundation 4797424935  │
│ hgpfbghb3acg4  4    8.0 GiB  amd64  2 hours ago     1 hour from now      dev                                             │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

In the output above instance with ID `ovkbmemc7qbp2` (the second on the list) has
16 CPUs and 32 GiB of memory, architecture *amd64*, was created 5 minutes ago and
from the GitHub Actions Run `4797424935` of repository [namespacelabs/foundation](https://github.com/namespacelabs/foundation),
and has 3 hours time to live.

The json output contains more information. You can use
[jq](https://jqlang.org/tutorial/) to print a specific field.
To print the list in a machine-friendly format, use `-o json` CLI flag.

```
$ nsc list -o json
[
  {
    "cluster_id": "1lf2ol9ioulce",
    "created": "2023-04-25T12:54:53.803550026Z",
    "deadline": "2023-04-25T13:24:53.802943180Z",
    "documented_purpose": "Manually created from CLI",
    "shape": {
      "virtual_cpu": 4,
      "memory_megabytes": 4096,
      "machine_arch": "amd64"
    },
    "kubernetes_distribution": "k3s",
    "platform": [
      "linux/amd64"
    ],
    "ingress_domain": "ord2.namespaced.app",
    "label": [
      {
        "name": "nsc.modelver",
        "value": "2"
      },
      {
        "name": "nsc.containerd.features",
        "value": "[\"systemevents\"]"
      },
      {
        "name": "nsc.kubernetes",
        "value": "1.26"
      }
    ]
  },
  {
    "cluster_id": "ovkbmemc7qbp2",
    "created": "2023-04-25T12:54:53.803550026Z",
    "deadline": "2023-04-25T15:54:53.726213767Z",
    "documented_purpose": "Build machine",
    "shape": {
      "virtual_cpu": 16,
      "memory_megabytes": 32768,
      "machine_arch": "amd64"
    },
    "kubernetes_distribution": "k3s",
    "platform": [
      "linux/amd64"
    ],
    "ingress_domain": "ord2.namespaced.app",
    "label": [
      {
        "name": "nsc.modelver",
        "value": "2"
      },
      {
        "name": "nsc.containerd.features",
        "value": "[\"systemevents\"]"
      },
      {
        "name": "nsc.kubernetes",
        "value": "1.26"
      },
      {
        "name": "nsc.kind",
        "value": "build-cluster"
      }
    ],
    "github_workflow": {
      "repository": "namespacelabs/foundation",
      "run_id": "4797424935",
      "run_attempt": "1",
      "sha": "9d7b3e65892d9ca22e4f5687f3e014763af04e3e",
      "ref": "refs/heads/main",
      "actor": "n-g",
      "workflow": "e2e"
    }
  },
  {
    "cluster_id": "hgpfbghb3acg4",
    "created": "2023-04-25T10:44:54.352324407Z",
    "deadline": "2023-04-25T14:44:54.351715446Z",
    "documented_purpose": "dev",
    "shape": {
      "virtual_cpu": 4,
      "memory_megabytes": 8192,
      "machine_arch": "amd64"
    },
    "kubernetes_distribution": "k3s",
    "platform": [
      "linux/amd64"
    ],
    "ingress_domain": "ord2.namespaced.app",
    "label": [
      {
        "name": "nsc.modelver",
        "value": "2"
      },
      {
        "name": "nsc.containerd.features",
        "value": "[\"systemevents\"]"
      },
      {
        "name": "nsc.kubernetes",
        "value": "1.26"
      }
    ]
  }
]
```

## Options

### -o <type>

Specifying `list` command output format. Supported options are `json` and
`plain`. By default `plain` output format is used.

Last updated July 4, 2025

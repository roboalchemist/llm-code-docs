# Source: https://docs.infrahub.app/nornir/references/plugins/artifact_tasks.md

# Artifact management plugin

## `regenerate_host_artifact`[​](#regenerate_host_artifact "Direct link to regenerate_host_artifact")

Regenerates a host artifact for a given task.

This function retrieves an artifact node associated with the given artifact name from the InfrahubNode, then sends a request to regenerate the artifact using the Infrahub API.

### Parameters[​](#parameters "Direct link to Parameters")

| Parameter  | Type   | Required | Default | Description                                     |
| ---------- | ------ | -------- | ------- | ----------------------------------------------- |
| `task`     | `Task` | Yes      |         | The task instance containing host-related data. |
| `artifact` | `str`  | Yes      |         | The name of the artifact to regenerate.         |

### Examples[​](#examples "Direct link to Examples")

#### Regenerate artifact for a given device[​](#regenerate-artifact-for-a-given-device "Direct link to Regenerate artifact for a given device")

```
from nornir import InitNornir
from nornir.core.plugins.inventory import InventoryPluginRegister
from nornir_infrahub.plugins.inventory.infrahub import InfrahubInventory
from nornir_infrahub.plugins.tasks import regenerate_host_artifact

from nornir_utils.plugins.functions import print_result


def main():
    InventoryPluginRegister.register("InfrahubInventory", InfrahubInventory)
    nr = InitNornir(inventory=...)

    eos_devices = nr.filter(platform="eos")

    # regenerate an artifact for a host
    print_result(eos_devices.run(task=regenerate_host_artifact, artifact="startup-config"))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

## `generate_artifacts`[​](#generate_artifacts "Direct link to generate_artifacts")

Generates an artifact for a given task.

This function retrieves an artifact definition from the InfrahubNode and triggers an API request to generate the specified artifact.

### Parameters[​](#parameters-1 "Direct link to Parameters")

| Parameter  | Type   | Required | Default | Description                                     |
| ---------- | ------ | -------- | ------- | ----------------------------------------------- |
| `task`     | `Task` | Yes      |         | The task instance containing host-related data. |
| `artifact` | `str`  | Yes      |         | The name of the artifact to generate.           |
| `timeout`  | `int`  | No       | 10      | The request timeout in seconds. Defaults to 10. |

### Examples[​](#examples-1 "Direct link to Examples")

#### Example generating artifacts[​](#example-generating-artifacts "Direct link to Example generating artifacts")

```
from nornir import InitNornir
from nornir.core.plugins.inventory import InventoryPluginRegister
from nornir_infrahub.plugins.inventory.infrahub import InfrahubInventory
from nornir_infrahub.plugins.tasks import generate_artifacts


def main():
    InventoryPluginRegister.register("InfrahubInventory", InfrahubInventory)
    nr = InitNornir(inventory=...)

    # generate_artifacts, generates the artifact for all the targets in the Artifact definition
    # we only need to run this task once, per artifact definition
    run_once = nr.filter(name="jfk1-edge1")
    result = run_once.run(task=generate_artifacts, artifact="startup-config", timeout=20)
    ocfg_result = run_once.run(task=generate_artifacts, artifact="openconfig-interfaces", timeout=20)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

## `get_artifact`[​](#get_artifact "Direct link to get_artifact")

Retrieves the specified artifact from the Infrahub storage.

This function fetches an artifact node associated with the given artifact name or id and sends a request to retrieve its stored content. The response is returned as JSON or text, depending on the artifact's content type.

### Parameters[​](#parameters-2 "Direct link to Parameters")

| Parameter     | Type   | Required | Default | Description                                     |
| ------------- | ------ | -------- | ------- | ----------------------------------------------- |
| `task`        | `Task` | Yes      |         | The task instance containing host-related data. |
| `artifact`    | `str`  | No       |         | The name of the artifact to retrieve.           |
| `artifact_id` | `str`  | No       |         | The id of the artifact to retrieve.             |

### Examples[​](#examples-2 "Direct link to Examples")

#### Example getting artifacts from Infrahub[​](#example-getting-artifacts-from-infrahub "Direct link to Example getting artifacts from Infrahub")

```
from nornir import InitNornir
from nornir.core.plugins.inventory import InventoryPluginRegister
from nornir_infrahub.plugins.inventory.infrahub import InfrahubInventory
from nornir_infrahub.plugins.tasks import get_artifact
from nornir_utils.plugins.functions import print_result


def main():
    InventoryPluginRegister.register("InfrahubInventory", InfrahubInventory)
    nr = InitNornir(inventory=...)

    eos_devices = nr.filter(platform="eos")
    # retrieves the artifact for all the hosts in the inventory
    result = eos_devices.run(task=get_artifact, artifact="startup-config")
    print_result(result)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

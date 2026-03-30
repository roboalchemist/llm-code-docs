# Source: https://docs.anyscale.com/reference/machine-pool.md

# Machine Pool API Reference

[View Markdown](/reference/machine-pool.md)

# Machine Pool API Reference

#### Customer-hosted cloud features[​](#customer-hosted-only "Direct link to Customer-hosted cloud features")

note

Some features are only available on customer-hosted clouds. Reach out to <support@anyscale.com> for info.

## Machine Pool CLI[​](#machine-pool-cli "Direct link to Machine Pool CLI")

### `anyscale machine-pool create` Beta[​](#anyscale-machine-pool-create-beta "Direct link to anyscale-machine-pool-create-beta")

warning

This command undergoes rapid iteration. Users must be tolerant of change.

**Usage**

`anyscale machine-pool create [OPTIONS]`

Create a machine pool in Anyscale.

**Options**

* **`--name`**: Provide a machine pool name (must be unique within an organization).

#### Examples[​](#examples "Direct link to Examples")

* CLI

```
$ anyscale machine-pool create --name can-testing
Machine pool can-testing has been created successfully (ID mp_8ogdz85mdwxb8a92yo44nn84ox).
```

### `anyscale machine-pool update` Beta[​](#anyscale-machine-pool-update-beta "Direct link to anyscale-machine-pool-update-beta")

warning

This command undergoes rapid iteration. Users must be tolerant of change.

**Usage**

`anyscale machine-pool update [OPTIONS]`

Update a machine pool in Anyscale.

**Options**

* **`--name`**: Provide a machine pool name.
* **`--spec-file`**: Provide a path to a specification file.

#### Examples[​](#examples-1 "Direct link to Examples")

* CLI

```
$ anyscale machine-pool update --name can-testing --spec-file spec.yaml
Updated machine pool 'can-testing'.
```

### `anyscale machine-pool delete` Beta[​](#anyscale-machine-pool-delete-beta "Direct link to anyscale-machine-pool-delete-beta")

warning

This command undergoes rapid iteration. Users must be tolerant of change.

**Usage**

`anyscale machine-pool delete [OPTIONS]`

Delete a machine pool in Anyscale.

**Options**

* **`--name`**: Provide a machine pool name.

#### Examples[​](#examples-2 "Direct link to Examples")

* CLI

```
$ anyscale machine-pool delete --name can-testing
Deleted machine pool 'can-testing'.
```

### `anyscale machine-pool attach` Beta[​](#anyscale-machine-pool-attach-beta "Direct link to anyscale-machine-pool-attach-beta")

warning

This command undergoes rapid iteration. Users must be tolerant of change.

**Usage**

`anyscale machine-pool attach [OPTIONS]`

Attach a machine pool to a cloud or cloud resource.

**Options**

* **`--name`**: Provide a machine pool name.
* **`--cloud`**: Provide a cloud name.
* **`--resource`**: For multi-resource clouds, the name of the cloud resource to attach to. If not provided, attaches to the primary cloud resource in the cloud.

#### Examples[​](#examples-3 "Direct link to Examples")

* CLI

```
$ anyscale machine-pool attach --name can-testing --cloud my-cloud
Attached machine pool 'can-testing' to cloud 'my-cloud'.
```

### `anyscale machine-pool detach` Beta[​](#anyscale-machine-pool-detach-beta "Direct link to anyscale-machine-pool-detach-beta")

warning

This command undergoes rapid iteration. Users must be tolerant of change.

**Usage**

`anyscale machine-pool detach [OPTIONS]`

Detach a machine pool from a cloud or cloud resource.

**Options**

* **`--name`**: Provide a machine pool name.
* **`--cloud`**: Provide a cloud name.
* **`--resource`**: For multi-resource clouds, the name of the cloud resource to detach from. If not provided, detaches from the primary cloud resource in the cloud.

#### Examples[​](#examples-4 "Direct link to Examples")

* CLI

```
$ anyscale machine-pool detach --name can-testing --cloud my-cloud
Detached machine pool 'can-testing' from cloud 'my-cloud'.
```

### `anyscale machine-pool list` Beta[​](#anyscale-machine-pool-list-beta "Direct link to anyscale-machine-pool-list-beta")

warning

This command undergoes rapid iteration. Users must be tolerant of change.

**Usage**

`anyscale machine-pool list [OPTIONS]`

List machine pools in Anyscale.

**Options**

* **`--format`**: Output format (table, yaml).

#### Examples[​](#examples-5 "Direct link to Examples")

* CLI

```
$ anyscale machine-pool list
MACHINE POOL       ID                             Clouds
can-testing        mp_8ogdz85mdwxb8a92yo44nn84ox
```

### `anyscale machine-pool describe` Beta[​](#anyscale-machine-pool-describe-beta "Direct link to anyscale-machine-pool-describe-beta")

warning

This command undergoes rapid iteration. Users must be tolerant of change.

**Usage**

`anyscale machine-pool describe [OPTIONS]`

Describe a machine pool in Anyscale.

**Options**

* **`--name`**: Provide a machine pool name.
* **`--format`**: Output format (table, json).

#### Examples[​](#examples-6 "Direct link to Examples")

* CLI

```
$ anyscale machine-pool describe --name can-testing --mode machines
```

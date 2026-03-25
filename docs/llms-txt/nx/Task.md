# Source: https://nx.dev/docs/reference/devkit/Task.md

A representation of the invocation of an Executor

## Table of contents

### Properties

- [cache](/docs/reference/devkit/Task#cache)
- [continuous](/docs/reference/devkit/Task#continuous)
- [endTime](/docs/reference/devkit/Task#endtime)
- [hash](/docs/reference/devkit/Task#hash)
- [hashDetails](/docs/reference/devkit/Task#hashdetails)
- [id](/docs/reference/devkit/Task#id)
- [outputs](/docs/reference/devkit/Task#outputs)
- [overrides](/docs/reference/devkit/Task#overrides)
- [parallelism](/docs/reference/devkit/Task#parallelism)
- [projectRoot](/docs/reference/devkit/Task#projectroot)
- [startTime](/docs/reference/devkit/Task#starttime)
- [target](/docs/reference/devkit/Task#target)

## Properties

### cache

• `Optional` **cache**: `boolean`

Determines if a given task should be cacheable.

___

### continuous

• `Optional` **continuous**: `boolean`

This denotes if the task runs continuously

___

### endTime

• `Optional` **endTime**: `number`

Unix timestamp of when a Batch Task ends

___

### hash

• `Optional` **hash**: `string`

Hash of the task which is used for caching.

___

### hashDetails

• `Optional` **hashDetails**: `Object`

Details about the composition of the hash

#### Type declaration

| Name | Type | Description |
| :------ | :------ | :------ |
| `command` | `string` | Command of the task |
| `implicitDeps?` | \{ `[fileName: string]`: `string`;  } | Hashes of implicit dependencies which are included in the hash |
| `nodes` | \{ `[name: string]`: `string`;  } | Hashes of inputs used in the hash |
| `runtime?` | \{ `[input: string]`: `string`;  } | Hash of the runtime environment which the task was executed |

___

### id

• **id**: `string`

Unique ID

___

### outputs

• **outputs**: `string`[]

The outputs the task may produce

___

### overrides

• **overrides**: `any`

Overrides for the configured options of the target

___

### parallelism

• **parallelism**: `boolean`

Determines if a given task should be parallelizable.

___

### projectRoot

• `Optional` **projectRoot**: `string`

Root of the project the task belongs to

___

### startTime

• `Optional` **startTime**: `number`

Unix timestamp of when a Batch Task starts

___

### target

• **target**: `Object`

Details about which project, target, and configuration to run.

#### Type declaration

| Name | Type | Description |
| :------ | :------ | :------ |
| `configuration?` | `string` | The configuration of the target which the task invokes |
| `project` | `string` | The project for which the task belongs to |
| `target` | `string` | The target name which the task should invoke |

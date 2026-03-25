# Source: https://nx.dev/docs/reference/devkit/TaskHasher.md

## Table of contents

### Methods

- [hashTask](/docs/reference/devkit/TaskHasher#hashtask)
- [hashTasks](/docs/reference/devkit/TaskHasher#hashtasks)

## Methods

### hashTask

▸ **hashTask**(`task`): `Promise`\<[`Hash`](/docs/reference/devkit/Hash)\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `task` | [`Task`](/docs/reference/devkit/Task) |

#### Returns

`Promise`\<[`Hash`](/docs/reference/devkit/Hash)\>

**`Deprecated`**

use hashTask(task:Task, taskGraph: TaskGraph, env: NodeJS.ProcessEnv) instead. This will be removed in v20

▸ **hashTask**(`task`, `taskGraph`): `Promise`\<[`Hash`](/docs/reference/devkit/Hash)\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `task` | [`Task`](/docs/reference/devkit/Task) |
| `taskGraph` | [`TaskGraph`](/docs/reference/devkit/TaskGraph) |

#### Returns

`Promise`\<[`Hash`](/docs/reference/devkit/Hash)\>

**`Deprecated`**

use hashTask(task:Task, taskGraph: TaskGraph, env: NodeJS.ProcessEnv) instead. This will be removed in v20

▸ **hashTask**(`task`, `taskGraph`, `env`, `cwd?`): `Promise`\<[`Hash`](/docs/reference/devkit/Hash)\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `task` | [`Task`](/docs/reference/devkit/Task) |
| `taskGraph` | [`TaskGraph`](/docs/reference/devkit/TaskGraph) |
| `env` | `ProcessEnv` |
| `cwd?` | `string` |

#### Returns

`Promise`\<[`Hash`](/docs/reference/devkit/Hash)\>

___

### hashTasks

▸ **hashTasks**(`tasks`): `Promise`\<[`Hash`](/docs/reference/devkit/Hash)[]\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `tasks` | [`Task`](/docs/reference/devkit/Task)[] |

#### Returns

`Promise`\<[`Hash`](/docs/reference/devkit/Hash)[]\>

**`Deprecated`**

use hashTasks(tasks:Task[], taskGraph: TaskGraph, env: NodeJS.ProcessEnv) instead. This will be removed in v20

▸ **hashTasks**(`tasks`, `taskGraph`): `Promise`\<[`Hash`](/docs/reference/devkit/Hash)[]\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `tasks` | [`Task`](/docs/reference/devkit/Task)[] |
| `taskGraph` | [`TaskGraph`](/docs/reference/devkit/TaskGraph) |

#### Returns

`Promise`\<[`Hash`](/docs/reference/devkit/Hash)[]\>

**`Deprecated`**

use hashTasks(tasks:Task[], taskGraph: TaskGraph, env: NodeJS.ProcessEnv) instead. This will be removed in v20

▸ **hashTasks**(`tasks`, `taskGraph`, `env`, `cwd?`): `Promise`\<[`Hash`](/docs/reference/devkit/Hash)[]\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `tasks` | [`Task`](/docs/reference/devkit/Task)[] |
| `taskGraph` | [`TaskGraph`](/docs/reference/devkit/TaskGraph) |
| `env` | `ProcessEnv` |
| `cwd?` | `string` |

#### Returns

`Promise`\<[`Hash`](/docs/reference/devkit/Hash)[]\>

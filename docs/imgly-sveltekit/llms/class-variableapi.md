# Class: VariableAPI

Manage text variables within design templates.

Text variables enable dynamic content replacement in design templates. Variables are stored as key-value pairs and can be referenced in text blocks for automated content updates.

```
// Configure a text block that displays 'Hello, World'const block = cesdk.engine.block.create('text');cesdk.engine.block.setText(block, 'Hello, {{name}}!');cesdk.engine.variable.setString('name', 'World');
```

## Variable Management[#](#variable-management)

Create, update, retrieve, and remove text variables from the engine.

### findAll()[#](#findall)

  

Get all text variable names currently stored in the engine.

#### Returns[#](#returns)

`string`\[\]

List of variable names.

#### Signature[#](#signature)

```
findAll(): string[]
```

* * *

### setString()[#](#setstring)

  

Set a text variable’s value.

Creates a new variable if the key doesn’t exist, or updates an existing one.

#### Parameters[#](#parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| `key` | `string` | The variable’s key. |
| `value` | `string` | The text value to assign to the variable. |

#### Returns[#](#returns-1)

`void`

#### Signature[#](#signature-1)

```
setString(key: string, value: string): void
```

* * *

### getString()[#](#getstring)

  

Get a text variable’s value.

#### Parameters[#](#parameters-1)

| Parameter | Type | Description |
| --- | --- | --- |
| `key` | `string` | The variable’s key. |

#### Returns[#](#returns-2)

`string`

The text value of the variable.

#### Signature[#](#signature-2)

```
getString(key: string): string
```

* * *

### remove()[#](#remove)

  

Remove a text variable from the engine.

#### Parameters[#](#parameters-2)

| Parameter | Type | Description |
| --- | --- | --- |
| `key` | `string` | The variable’s key to remove. |

#### Returns[#](#returns-3)

`void`

#### Signature[#](#signature-3)

```
remove(key: string): void
```

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/classes/utilsapi)
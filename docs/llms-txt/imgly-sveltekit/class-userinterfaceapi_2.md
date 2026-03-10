# Class: UserInterfaceAPI

A public interface for controlling the UI of the Creative Editor SDK

## Constructors[#](#constructors)

### Constructor[#](#constructor)

  

`UserInterfaceAPI`

## Methods[#](#methods)

### setGlobalStateValue()[#](#setglobalstatevalue)

  

| Type Parameter | | ------ | | `T` |

#### Parameters[#](#parameters)

| Parameter | Type |
| --- | --- |
| `id` | `string` |
| `value` | `T` |

#### Returns[#](#returns)

`void`

#### Signature[#](#signature)

```
setGlobalStateValue(id: string, value: T): void
```

* * *

### getGlobalStateValue()[#](#getglobalstatevalue)

  

| Type Parameter | | ------ | | `T` |

#### Parameters[#](#parameters-1)

| Parameter | Type |
| --- | --- |
| `id` | `string` |
| `defaultValue?` | `T` |

#### Returns[#](#returns-1)

`T`

#### Signature[#](#signature-1)

```
getGlobalStateValue(id: string, defaultValue?: T): T
```

* * *

### hasGlobalStateValue()[#](#hasglobalstatevalue)

  

| Parameter | Type | | ------ | ------ | | `id` | `string` |

#### Returns[#](#returns-2)

`boolean`

#### Signature[#](#signature-2)

```
hasGlobalStateValue(id: string): boolean
```

* * *

### onGlobalStateChanged()[#](#onglobalstatechanged)

  

| Type Parameter | | ------ | | `T` |

#### Parameters[#](#parameters-2)

| Parameter | Type |
| --- | --- |
| `id` | `string` |
| `callback` | (`value`) => `void` |

#### Returns[#](#returns-3)

```
(): void;
```

##### Returns[#](#returns-4)

`void`

#### Signature[#](#signature-3)

```
onGlobalStateChanged(id: string, callback: (value: T) => void): () => void
```

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/documentation/namespaces/cesdkconfiguration/type-aliases/deprecatedkeys)
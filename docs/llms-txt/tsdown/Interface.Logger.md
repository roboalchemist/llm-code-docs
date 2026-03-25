# Source: https://tsdown.dev/reference/api/Interface.Logger.md

---
url: /reference/api/Interface.Logger.md
---
# Interface: Logger

Defined in: [src/utils/logger.ts:24](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/utils/logger.ts#L24)

## Properties

### clearScreen()

```ts
clearScreen: (type) => void;
```

Defined in: [src/utils/logger.ts:32](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/utils/logger.ts#L32)

#### Parameters

##### type

`LogType`

#### Returns

`void`

***

### error()

```ts
error: (...args) => void;
```

Defined in: [src/utils/logger.ts:30](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/utils/logger.ts#L30)

#### Parameters

##### args

...`any`\[]

#### Returns

`void`

***

### info()

```ts
info: (...args) => void;
```

Defined in: [src/utils/logger.ts:27](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/utils/logger.ts#L27)

#### Parameters

##### args

...`any`\[]

#### Returns

`void`

***

### level

```ts
level: LogLevel
```

Defined in: [src/utils/logger.ts:25](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/utils/logger.ts#L25)

***

### options?

```ts
optional options: LoggerOptions;
```

Defined in: [src/utils/logger.ts:26](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/utils/logger.ts#L26)

***

### success()

```ts
success: (...args) => void;
```

Defined in: [src/utils/logger.ts:31](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/utils/logger.ts#L31)

#### Parameters

##### args

...`any`\[]

#### Returns

`void`

***

### warn()

```ts
warn: (...args) => void;
```

Defined in: [src/utils/logger.ts:28](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/utils/logger.ts#L28)

#### Parameters

##### args

...`any`\[]

#### Returns

`void`

***

### warnOnce()

```ts
warnOnce: (...args) => void;
```

Defined in: [src/utils/logger.ts:29](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/utils/logger.ts#L29)

#### Parameters

##### args

...`any`\[]

#### Returns

`void`

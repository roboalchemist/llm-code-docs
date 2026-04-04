# Source: https://www.apibara.com/docs/getting-started/indexers#with-runtime-config

# Source: https://www.apibara.com/docs/getting-started/indexers

# Building indexers

Indexers are created using the `defineIndexer` higher-order function. This function takes a _stream definition_ and returns a function to define the indexer.

The job of an indexer is to stream and process historical data (backfilling) and then switch to real-time mode. Indexers built using our SDK are designed to handle chain-reorganizations automatically. If, for any reason, you need to receive notifications about reorgs, you can define [a custom `message:invalidate` hook](/docs/getting-started/plugins#hooks) to handle them.

By default, the indexer is stateless (restarts from the beginning on restart) and does not provide any storage. You can add persistence and storage by using one of the provided storage plugins.

## Examples

The following examples show how to create indexers for the Beacon Chain, EVM (Ethereum), and Starknet.

### Beacon Chain indexer

```ts
import { BeaconChainStream } from "@apibara/beaconchain";
import { defineIndexer } from "@apibara/indexer";

export default defineIndexer(BeaconChainStream)({
  /* ... */
});
```

### EVM (Ethereum) indexer

```ts
import { EvmStream } from "@apibara/evm";
import { defineIndexer } from "@apibara/indexer";

export default defineIndexer(EvmStream)({
  /* ... */
});
```

### Starknet indexer

```ts
import { StarknetStream } from "@apibara/starknet";
import { defineIndexer } from "@apibara/indexer";

export default defineIndexer(StarknetStream)({
  /* ... */
});
```

## With runtime config

To configure the indexer at runtime, export a function that takes the configuration and returns the indexer's definition.

```ts
import { EvmStream } from "@apibara/evm";
import type { ApibaraRuntimeConfig } from "apibara/types";
import { defineIndexer } from "@apibara/indexer";

export default function (runtimeConfig: ApibaraRuntimeConfig) {
  return defineIndexer(EvmStream)({
    // ...
  });
}
```

## Indexer configuration

All indexers take the same configuration options.

- **`streamUrl`** `string`
- **`filter`** `TFilter`
- **`finality`** `string | "finalized" | "accepted" | "pending"`
- **`startingCursor`** `{ orderKey: bigint, uniqueKey?: string }`
- **`debug`** `boolean`
- **`transform`** `({ block, cursor, endCursor, finality, context }) => Promise<void>`
- **`factory`** `({ block, context }) => Promise<{ filter?: TFilter }>`
- **`hooks`** `object`
- **`plugins`** `array`

### The transform function

The `transform` function is invoked for each block received from the DNA stream. This function is where you should implement your business logic.

**Arguments**

- **`block`** `TBlock`
- **`cursor`** `{ orderKey: bigint, uniqueKey?: string }`
- **`endCursor`** `{ orderKey: bigint, uniqueKey?: string }`
- **`finality`** `string | "finalized" | "accepted" | "pending"`
- **`context`** `object`

The following example shows a minimal indexer that streams block headers and prints them to the console.

```ts
import { EvmStream } from "@apibara/evm";
import { defineIndexer } from "@apibara/indexer";

export default defineIndexer(EvmStream)({
  streamUrl: "https://mainnet.ethereum.a5a.ch",
  filter: {
    header: "always",
  },
  async transform({ block }) {
    const { header } = block;
    console.log(header);
  },
});
```

### The factory function

The `factory` function is used to add data filters at runtime. This is useful for creating indexers for smart contracts that deploy other smart contracts like Uniswap V2 and its forks.

**Arguments**

- **`block`** `TBlock`
- **`context`** `object`

The following example shows a minimal indexer that streams `PairCreated` events from Uniswap V2 to detect new pools, and then streams the pool's events.

```ts
import { EvmStream } from "@apibara/evm";
import { defineIndexer } from "@apibara/indexer";

export default defineIndexer(EvmStream)({
  streamUrl: "https://mainnet.ethereum.a5a.ch",
  filter: {
    logs: [
      {
        /* ... */
      },
    ],
  },
  async factory({ block }) {
    const { logs } = block;
    return {
      /* ... */
    };
  },
  async transform({ block }) {
    const { header, logs } = block;
    console.log(header);
    console.log(logs);
  },
});
```
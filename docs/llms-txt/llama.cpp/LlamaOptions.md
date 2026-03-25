# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/LlamaOptions.md

---
url: /api/type-aliases/LlamaOptions.md
---
# Type Alias: LlamaOptions

```ts
type LlamaOptions = {
  gpu?:   | "auto"
     | LlamaGpuType
     | {
     type: "auto";
     exclude?: LlamaGpuType[];
   };
  logLevel?: LlamaLogLevel;
  logger?: (level: LlamaLogLevel, message: string) => void;
  build?: "auto" | "never" | "forceRebuild" | "try" | "autoAttempt";
  cmakeOptions?: Record<string, string>;
  existingPrebuiltBinaryMustMatchBuildOptions?: boolean;
  usePrebuiltBinaries?: boolean;
  progressLogs?: boolean;
  skipDownload?: boolean;
  maxThreads?: number;
  vramPadding?: number | (totalVram: number) => number;
  ramPadding?: number | (totalRam: number) => number;
  debug?: boolean;
  dryRun?: boolean;
  numa?: LlamaNuma;
};
```

Defined in: [bindings/getLlama.ts:37](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/getLlama.ts#L37)

## Properties

### gpu?

```ts
optional gpu: 
  | "auto"
  | LlamaGpuType
  | {
  type: "auto";
  exclude?: LlamaGpuType[];
};
```

Defined in: [bindings/getLlama.ts:51](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/getLlama.ts#L51)

The compute layer implementation type to use for llama.cpp.

* **`"auto"`**: Automatically detect and use the best GPU available (Metal on macOS, and CUDA or Vulkan on Windows and Linux)
* **`"metal"`**: Use Metal.
  Only supported on macOS.
  Enabled by default on Apple Silicon Macs.
* **`"cuda"`**: Use CUDA.
* **`"vulkan"`**: Use Vulkan.
* **`false`**: Disable any GPU support and only use the CPU.

`"auto"` by default.

#### See

Use the `getLlamaGpuTypes` function to get the available GPU types (from the above list) for the current machine at runtime.

***

### logLevel?

```ts
optional logLevel: LlamaLogLevel;
```

Defined in: [bindings/getLlama.ts:60](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/getLlama.ts#L60)

Set the minimum log level for llama.cpp.
Defaults to `"warn"`.

***

### logger()?

```ts
optional logger: (level: LlamaLogLevel, message: string) => void;
```

Defined in: [bindings/getLlama.ts:65](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/getLlama.ts#L65)

Set a custom logger for llama.cpp logs.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `level` | [`LlamaLogLevel`](../enumerations/LlamaLogLevel.md) |
| `message` | `string` |

#### Returns

`void`

***

### build?

```ts
optional build: "auto" | "never" | "forceRebuild" | "try" | "autoAttempt";
```

Defined in: [bindings/getLlama.ts:104](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/getLlama.ts#L104)

Set what build method to use.

* **`"auto"`**:
  Iterate over all available [gpu](#gpu) types from best to worst, and for each GPU type:

  * If a local build is found, use it.
  * Otherwise, if a prebuilt binary is found and working, use it.

  Otherwise, if no binary is available for any GPU type, build from source.
* **`"never"`**:
  Iterate over all available [gpu](#gpu) types from best to worst, and for each GPU type:

  * If a local build is found, use it.
  * Otherwise, if a prebuilt binary is found and working, use it.

  Otherwise, if no binary is available for any GPU type, throw a `NoBinaryFoundError` error.
* **`"forceRebuild"`**: Always build from source.
  Be cautious with this option, as it will cause the build to fail on Windows when the binaries are in use by another process.
* **`"try"`**:
  Iterate over all available [gpu](#gpu) types from best to worst, and for each GPU type:

  * If a local build is found, use it.

  If no local build is found, iterate over all available [gpu](#gpu) types from best to worst, and for each GPU type:

  * Try to build from source and use the resulting binary.

  If no build was successful, iterate over all available [gpu](#gpu) types from best to worst, and for each GPU type:

  * Use a prebuilt binary if found and working.
* **`"autoAttempt"`**:
  Iterate over all available [gpu](#gpu) types from best to worst, and for each GPU type:
  * If a local build is found, use it.
  * Otherwise, if a prebuilt binary is found and working, use it.
  * Otherwise, build from source and use the resulting binary.

When running from inside an Asar archive in Electron, building from source is not possible, so it'll never build from source.
To allow building from source in Electron apps, make sure you ship `node-llama-cpp` as an unpacked module.

Defaults to `"auto"`.
On Electron, defaults to `"never"`.

***

### cmakeOptions?

```ts
optional cmakeOptions: Record<string, string>;
```

Defined in: [bindings/getLlama.ts:109](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/getLlama.ts#L109)

Set custom CMake options for llama.cpp

***

### existingPrebuiltBinaryMustMatchBuildOptions?

```ts
optional existingPrebuiltBinaryMustMatchBuildOptions: boolean;
```

Defined in: [bindings/getLlama.ts:115](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/getLlama.ts#L115)

When a prebuilt binary is found, only use it if it was built with the same build options as the ones specified in `buildOptions`.
Disabled by default.

***

### usePrebuiltBinaries?

```ts
optional usePrebuiltBinaries: boolean;
```

Defined in: [bindings/getLlama.ts:121](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/getLlama.ts#L121)

Use prebuilt binaries if they match the build options.
Enabled by default.

***

### progressLogs?

```ts
optional progressLogs: boolean;
```

Defined in: [bindings/getLlama.ts:127](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/getLlama.ts#L127)

Print binary compilation progress logs.
Enabled by default.

***

### skipDownload?

```ts
optional skipDownload: boolean;
```

Defined in: [bindings/getLlama.ts:134](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/getLlama.ts#L134)

Don't download llama.cpp source if it's not found.
When set to `true`, and llama.cpp source is not found, a `NoBinaryFoundError` error will be thrown.
Disabled by default.

***

### maxThreads?

```ts
optional maxThreads: number;
```

Defined in: [bindings/getLlama.ts:145](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/getLlama.ts#L145)

The maximum number of threads to use for the Llama instance.

Set to `0` to have no thread limit.

When not using a GPU, defaults to the number of CPU cores that are useful for math (`.cpuMathCores`), or `4`, whichever is higher.

When using a GPU, there's no limit by default.

***

### vramPadding?

```ts
optional vramPadding: number | (totalVram: number) => number;
```

Defined in: [bindings/getLlama.ts:155](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/getLlama.ts#L155)

Pad the available VRAM for the memory size calculations, as these calculations are not always accurate.
Recommended to ensure stability.
This only affects the calculations of `"auto"` in function options and is not reflected in the `getVramState` function.

Defaults to `8%` of the total VRAM or 1.2GB, whichever is lower.
Set to `0` to disable.

***

### ramPadding?

```ts
optional ramPadding: number | (totalRam: number) => number;
```

Defined in: [bindings/getLlama.ts:166](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/getLlama.ts#L166)

Pad the available RAM for the memory size calculations, as these calculations are not always accurate.
Recommended to ensure stability.

Defaults to `25%` of the total RAM or 6GB (1GB on Linux), whichever is lower.
Set to `0` to disable.

> Since the OS also needs RAM to function, the default value can get up to 6GB on Windows and macOS, and 1GB on Linux.

***

### debug?

```ts
optional debug: boolean;
```

Defined in: [bindings/getLlama.ts:176](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/getLlama.ts#L176)

Enable debug mode to find issues with llama.cpp.
Makes logs print directly to the console from `llama.cpp` and not through the provided logger.

Defaults to `false`.

The default can be set using the `NODE_LLAMA_CPP_DEBUG` environment variable.

***

### dryRun?

```ts
optional dryRun: boolean;
```

Defined in: [bindings/getLlama.ts:191](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/getLlama.ts#L191)

Loads existing binaries without loading the `llama.cpp` backend,
and then disposes the returned `Llama` instance right away before returning it.

Useful for performing a fast and efficient test to check whether the given configuration can be loaded.
Can be used for determining which GPU types the current machine supports before actually using them.

Enabling this option implies that `build: "never"` and `skipDownload: true`.

The returned `Llama` instance will be disposed and cannot be used.

Defaults to `false`.

***

### numa?

```ts
optional numa: LlamaNuma;
```

Defined in: [bindings/getLlama.ts:211](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/getLlama.ts#L211)

NUMA (Non-Uniform Memory Access) allocation policy.

On multi-socket or multi-cluster machines, each CPU "socket" (or node) has its own local memory.
Accessing memory on your own socket is fast, but another socket's memory is slower.
Setting a NUMA (Non-Uniform Memory Access) allocation policy can
dramatically improve performance by keeping data local and "close" to the socket.

These are the available NUMA options:

* **`false`**: Don't set any NUMA policy - let the OS decide.
* **`"distribute"`**: Distribute the memory across all available NUMA nodes.
* **`"isolate"`**: Pin both threads and their memory to a single NUMA node to avoid cross-node traffic.
* **`"numactl"`**: Delegate NUMA management to the external `numactl` command (or `libnuma` library) to set the NUMA policy.
* **`"mirror"`**: Allocate memory on all NUMA nodes, and copy the data to all of them.
  This ensures minimal traffic between nodes, but uses more memory.

Defaults to `false` (no NUMA policy).

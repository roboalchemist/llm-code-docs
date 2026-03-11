# Source: https://docs.mage.ai/guides/blocks/batch-read-write.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Level 99 dynamic abilities

> Granular block settings for controlling read/write data partitions using output size, number of chunks, and item count.

export const ProOnly = ({button = 'Get started for free', description = 'Try our fully managed solution to access this advanced feature.', source = 'documentation', title = 'Only in Mage Pro.'}) => <a href={`https://cloud.mage.ai/sign-up?source=${source}`} className="block my-4 px-5 py-4 overflow-hidden rounded-xl flex gap-3 border border-emerald-500/20 bg-emerald-50/50 dark:border-emerald-500/30 dark:bg-emerald-500/10" target="_blank">
    <div style={{
  display: 'flex',
  alignItems: 'center',
  width: '100%'
}}>
      <div className="text-sm prose min-w-0 text-emerald-900 dark:text-emerald-200" style={{
  flex: 1
}}>
        {title}
        <p className="normal">{description}</p>
      </div>

      <div> </div>

      <div>
        <ProButton label={button} href={`https://cloud.mage.ai/sign-up?source=${source}`} />
      </div>
    </div>
  </a>;

export const ProButton = ({href, label = 'Get started with Mage Pro for free', source = 'documentation'}) => <div style={{
  height: 32,
  position: 'relative'
}}>
    <a target="_blank" className="group px-4 py-1.5 relative inline-flex items-center text-sm font-medium rounded-full" href={href ?? `https://cloud.mage.ai/sign-up?source=${source}`}>
      <span className="absolute inset-0 bg-primary-dark dark:bg-primary-light/10 border-primary-light/30 rounded-full dark:border group-hover:opacity-[0.9] dark:group-hover:border-primary-light/60">
      </span>

      <div className="mr-0.5 space-x-2.5 flex items-center">
        <span class="z-10 text-white dark:text-primary-light">
          {label}
        </span>

        <svg width="3" height="24" viewBox="0 -9 3 24" class="h-5 rotate-0 overflow-visible text-white/90 dark:text-primary-light">
          <path d="M0 0L3 3L0 6" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path>
        </svg>
      </div>
    </a>
  </div>;

## Batch read settings

On a block-by-block basis, customize how it reads data from its upstream blocks.

<ProOnly source="batch-read-write__read" />

### Read specific chunks

Downstream blocks can control the volume of data it loads into memory from its upstream block’s output.

The downstream block will only load the chunk from indigo\_mountain where power equals 5.

<Steps>
  <Step title="Load data">
    ```python  theme={"system"}
    import random

    import polars as pl

    from mage_ai.data.tabular.mocks import create_dataframe


    @data_loader
    def load_data(*args, **kwargs):
        dfs = []
        for i in range(10):
            df = create_dataframe(n_rows=100_000, use_pandas=False)
            df = df.with_columns(pl.lit(i).alias('power'))
            if i == 5:
                df = df.with_columns(pl.lit(i).cast(pl.Float64).alias('col_0'))
            dfs.append(df)
        return pl.concat(dfs)
    ```
  </Step>

  <Step title="Transform data">
    ```python  theme={"system"}
    @transformer
    def transform(data, *args, **kwargs):
        return data
    ```
  </Step>
</Steps>

### Input data types

Downstream blocks can control the strategy it implements when loading an upstream block’s
output data into memory.

#### Batch

Read data in batches.

```python  theme={"system"}
@transformer
def transform(data, *args, **kwargs):
    print('Batch size:', len(data[0]))
    print('Chunks:', len(data))
```

```
Batch size: 143
Chunks: 21105
```

#### Generator

Batch generator framework to operate and process 1,000+ gigabytes (GB) of data without running out of memory.

```python  theme={"system"}
@transformer
def transform(data, *args, **kwargs):
    for batch in data:
        df = batch.deserialize()
        print(df.shape)
```

```
(1337, 11)
(1337, 11)
(1337, 11)
(1337, 11)
(1337, 11)
(1337, 11)
(1337, 11)
(1337, 11)
(1337, 11)
(1337, 11)
...
```

<Steps>
  <Step title="Load data">
    ```python  theme={"system"}
    import random

    import polars as pl

    from mage_ai.data.tabular.mocks import create_dataframe


    @data_loader
    def load_data(*args, **kwargs):
        dfs = []
        for i in range(10):
            df = create_dataframe(n_rows=100_000, use_pandas=False)
            df = df.with_columns(pl.lit(i).alias('power'))
            if i == 5:
                df = df.with_columns(pl.lit(i).cast(pl.Float64).alias('col_0'))
            dfs.append(df)
        return pl.concat(dfs)
    ```
  </Step>

  <Step title="Transform data">
    ```python  theme={"system"}
    @transformer
    def transform(data, *args, **kwargs):
        for batch in data:
            df = batch.deserialize()
            print(df.shape)
    ```
  </Step>
</Steps>

#### Reader

Invoke methods on the reader object directly.

```python  theme={"system"}
from mage_ai.data.tabular.reader import (
    read_metadata,
    sample_batch_datasets,
    scan_batch_datasets_generator,
)

@transformer
def transform(data, *args, **kwargs):
    print(data.chunks)
    print(data.number_of_outputs)
    print(data.resource_usages)
    print(data.variable_path)
    print(data.variable_type)
    print(data.data_source)

    output = data.read_sync()
    for batch in output:
        df = batch.deserialize()
        print(df.shape)
```

***

## Batch write settings

Customize how data is written when outputting data from a block.

<ProOnly source="batch-read-write__write" />

```python  theme={"system"}
import random

import polars as pl

from mage_ai.data.tabular.mocks import create_dataframe


@data_loader
def load_data(*args, **kwargs):
    dfs = []
    for i in range(10):
        df = create_dataframe(n_rows=100_000, use_pandas=False)
        df = df.with_columns(pl.lit(i).alias('power'))
        if i == 5:
            df = df.with_columns(pl.lit(i).cast(pl.Float64).alias('col_0'))
        dfs.append(df)
    return pl.concat(dfs)
```

### Strategies

Explicitly set the chunking strategy when creating data partitions or batches of data.

Example: create chunks by the value in column `power`

#### Items per chunk

Example: each chunk can only contain a maximum number of 7,777 items.

#### Number of chunks

Example: each chunk must have at least 1,337 items and the total number of chunks cannot exceed 143.

#### Byte size per check

Example: each chunk cannot exceed 100MB in size on disk.

### Modes

Control how data is written.

1. Append
2. Replace


Built with [Mintlify](https://mintlify.com).
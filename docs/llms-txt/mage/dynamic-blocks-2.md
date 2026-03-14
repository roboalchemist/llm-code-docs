# Source: https://docs.mage.ai/guides/blocks/dynamic-blocks-2.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Level 99 dynamic abilities

> Execute 100,000+ dynamically created block runs concurrently with upgraded memory management and concurrency.

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

## Memory optimizations

In version 1.0 of dynamic blocks,
Mage was loading all the data of an upstream dynamic child block from disk into memory
in order to calculate how many dynamic child blocks should be created.
This can result in using large amounts of memory.

In version 2.0 of dynamic blocks,
Mage leverages the metadata of upstream block outputs
to calculate the number of downstream blocks for dynamic blocks and dynamic child blocks.
The metadata is only several bytes on disk and less than a kilobyte in RAM.

## Stream mode

Stream block output data to dynamically generated blocks without waiting for the upstream parent
block to finish executing.

<ProOnly source="dynamic-blocks-2__stream-mode" />

Here is a sample scenario to describe the previous and current state:

1. Dynamic block A returns a list of 10 items and has 1 direct downstream block B.
2. B is a dynamic child block and has 2 direct downstream block: C and D.
3. C is a dynamic child block and has 1 direct downstream block: D.

```mermaid  theme={"system"}
graph TD
  A --> B
  B --> C
  B --> D
  C --> D
```

In the past, this is the sequence of events:

1. Block A finishes executing and returns an output of 10 items.
2. Block B spawns 10 dynamic child blocks.
3. Block B executes all 10 dynamic blocks concurrently.
4. Once all 10 block runs from block B finishes, block C starts.
5. Block C spawns 10 child blocks and executes them.
6. Once Block C completes all 10 runs, block D starts.
7. Block D spawns 100 child blocks and executes them.

With dynamic block 2.0, you can enable stream mode which will allow downstream dynamic child blocks to execute as soon as its upstream parent dynamic child blocks finish. Here is the sequence of events in the new world:

1. Block A executes and can be handled in 2 ways:
   1. Serial: block A executes its code line by line and at the end, the return statement outputs the entire result of 10 items in a list.
   2. Generator: block A executes its code line by line up until a yield block. Once yield is called, the object that is yielded is stored as an output of block A. In this example, block A would yield 10 times, 1 for each item.
2. As soon as 1 output is detected from block A, block B spawns 1 dynamic child that consumes that single output as its input argument.
3. As soon as 1 output is detected from block B, block C spawns 1 dynamic child.
4. As soon as 1 output is detected from both block B and block C, block D spawns 1 dynamic child.

## Enabling stream mode

Stream mode allows downstream dynamic child blocks to execute without waiting for every upstream block to finish, improving pipeline performance.

### Accessing block settings

To enable stream mode, access the Dynamic block v2 configuration:

1. Click the **block settings button** next to the "Run code" button
   * Alternatively, use the **Block settings** tab in the right side navigation menu

### Configuration

1. Scroll down to the "Dynamic block v2 configuration" section
2. Select **"Stream"** from the Mode dropdown
3. Enter a **poll interval** in seconds - this is how often the system checks for new data or completed upstream blocks. Lower values (like 1 second) provide faster response times but use more system resources
4. **(Optional)** Toggle **"Combine all output into 1"** to consolidate outputs for downstream processing

Stream mode enables parallel processing and better resource utilization by allowing child blocks to start processing data as it becomes available.

<img alt="block-settings-button" src="https://raw.githubusercontent.com/mage-ai/assets/main/blocks/block-settings-button.png" />

## Memory generator

If a dynamic block contains a yield block,
the object yielded will be an output from that block. Once that object is stored,
it is released from memory and the next object in the generator within that block
is processed and loaded into memory.

<ProOnly source="dynamic-blocks-2__memory-generator" />

For example, if you want to loop through a total of 1 billion indexes in 1 million increments
so that you can load 1 million records into memory, you can use a yield block to process a
batch of 1 million, then yield the result as an output, release it from memory automatically,
and then proceed to the next batch.

```python  theme={"system"}
@custom
def process(*args, **kwargs):
    for i in range(1_000):
		    yield range(i * 1_000_000, (i + 1) * 1_000_000)
```


Built with [Mintlify](https://mintlify.com).
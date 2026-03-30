# Source: https://docs.mage.ai/guides/streaming/tutorials/streaming-stateful-store.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Stateful Streaming Pipeline

> Create and use stateful store in a streaming pipeline.

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

<ProOnly source="workspaces" />

Stateful store now is supported in the streaming pipeline. You can access it through the
`state_store` object in the `kwargs` parameter. Redis is the only supported state store.

## Configuration

State store configuration is required to set up in metadata.yml in order to enable stateful store in a streaming pipeline.

```yaml  theme={"system"}
state_store_config:
  type: 'REDIS'
  redis:
    redis_url: 'redis_url'
```

This configuration ensures that the pipeline can access and utilize Redis as its state store.

## Usage

Code example to access state store in your streaming pipeline:

```python  theme={"system"}
    state_store = kwargs['state_store']
    state_store.set_state('string_key', 'Transformer Hello, Redis!')
    state_store.set_state('int_key', 123)
    state_store.set_state('list_key', [1, 2, 3,4, 5])
    state_store.set_state('dict_key', {'key1': 'value1', 'key2': 'value2'})
```

```python  theme={"system"}
    state_store = kwargs['state_store']
    state_store.get_state('string_key')
    state_store.get_state('list_key')
    state_store.get_state('int_key')
    state_store.get_state('dict_key')
```

## Window Aggregation

The Window Aggregation Block is now supported in streaming pipeline, allowing for the aggregation of input data over a specified window of time and send it to down stream blocks.

### Usage

When you create a transformer and select the Window Aggregation type, it creates a window aggregation block with the following configuration:

```yaml  theme={"system"}
transformer_type: window_aggregation
method: time
type: tumbling
interval_window: 60 # seconds
advance_window: 10
```

You can update `interval_window` with the desired interval.
In the meantime, you can add the following blocks after the window aggregation block.
These blocks will be triggered periodically based on the configuration.
For example, you can add a transformer block to report those data into monitoring system.
It can be used as alerts to your pipeline.

### How It Works

The window block is registered during the streaming pipeline execution with the specified configuration. An independent thread is created to manage each window block and trigger it periodically based on the configuration. When triggered, the downstream blocks are also executed accordingly.

***

🚀 **With the stateful store and window aggregation support, your streaming pipeline can now efficiently manage and process stateful data.**


Built with [Mintlify](https://mintlify.com).
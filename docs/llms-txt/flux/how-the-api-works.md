# Source: https://docs.flux.ai/reference/how-the-api-works.md

# How the API works

We provide a state of the art built-in IDE based on Microsofts VSCode to write code.

![](https://image-archive.developerhub.io/image/upload/35409/cyebywqhmsaoep15ysbt/1596515556.jpg)

Any documents code operates within that documents scope and can not access data outside of it. At runtime the simulator will automatically flatten the document and sub document hierarchy to run the simulation in the background.

## Sandbox

All user code is sandboxed for security and additionally runs in a separate thread than the app itself for performance reasons.

This means you have no access to the [document global](https://developer.mozilla.org/en-US/docs/Web/API/Document) or any other globals that would allow you to escape the sandbox. A list of [Supported globals](https://docs.flux.ai/flux/reference/supported-globals) can be found here.

## Flux Global Object.

Most of the model API is accessible from [Flux global object](https://docs.flux.ai/flux/reference/flux). This includes functions to create nodes, access the nodes, show notifications, and much more. For example:

```typescript
flux.print("Hello world!"); 
flux.createOutputNode();
```



## State and Lifecycle

Let's introduce the concept of state and lifecycle in a model.

As you saw in previous code examples you can register/unregister lifecycle events via .on/.once/.off

An example:

```typescript
flux.on("setup", (event: LifeCycleEventContext) => {
    // Simulator is ready to start
  	// This is a good place to get your model ready
});

flux.on("beforeStep", (event: LifeCycleEventContext) => {
    // This event will fire just before the simulator computes the current step
  	// This is a great place to set variables on your primitives 
});

flux.on("afterStep", (event: LifeCycleEventContext) => {
    // This event fires right after the simulator computed the curret step
		// It's a great place to grab your output voltages/current and do something with them
});

flux.on("tearDown", (event: LifeCycleEventContext) => {
    // This event fires when the simulator is about to stop. Eg. because the circuit changed and the simulator restarts
  	// this is a great place to cleanup memory and write data
});
```



You will notice that the event callbacks provide a LifeCycleEventContext object. This object provides some stats about the current simulation:

```typescript
interface LifeCycleEventContext {
  step: number; // current step since last simulator start/restart
  time_since_simulation_start: number; // time in ms since last simulator start/restart
  time_since_last_step: number; // time in ms since last simulator frame
  step_size_time: number; // (ms) Length (in simulated time) of each step.
}
```


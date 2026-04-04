# Zenoh-Flow Guide

> **Note:** Zenoh-Flow has undergone significant API and schema changes between versions. The YAML descriptor format documented here uses the older schema (pre-0.6.0) with `flow:` top-level key and `uri:` field. Version 0.6.0-rc changed these to `name:` and `library:` respectively, and also redesigned the Rust node API and CLI tooling. Verify the schema against your installed version.

Zenoh-Flow is a dataflow programming framework built on top of Zenoh. It allows you to define processing pipelines as directed acyclic graphs (DAGs) of nodes, declare their topology in a YAML descriptor, and have the runtime distribute and execute those nodes across a network of Zenoh endpoints.

Where Zenoh handles publish/subscribe, storage, and query transport, Zenoh-Flow adds a structured execution layer: nodes have typed input/output ports, the runtime wires those ports together, and data flows through the graph according to the declared topology.

---

## Table of Contents

- [Core Concepts](#core-concepts)
  - [Dataflow Graph](#dataflow-graph)
  - [Dynamic Library Loading](#dynamic-library-loading)
  - [Runtime Infrastructure](#runtime-infrastructure)
- [YAML Descriptor Format](#yaml-descriptor-format)
  - [Minimal Structure](#minimal-structure)
  - [Field Reference](#field-reference)
  - [Configuration Passing](#configuration-passing)
  - [Template Variables](#template-variables)
- [Implementing Nodes in Rust](#implementing-nodes-in-rust)
  - [Cargo.toml](#cargotoml)
  - [Data Types](#data-types)
  - [Implementing a Source](#implementing-a-source)
  - [Implementing an Operator](#implementing-an-operator)
  - [Implementing a Sink](#implementing-a-sink)
- [Node Lifecycle](#node-lifecycle)
  - [1. `initialize(config)` — Startup](#1-initializeconfig-startup)
  - [2. `run(...)` — Execution](#2-run-execution)
  - [3. `finalize(state)` — Shutdown](#3-finalizestate-shutdown)
- [Zero-Copy Co-location](#zero-copy-co-location)
- [Distributed Deployment](#distributed-deployment)
  - [Router Configuration](#router-configuration)
  - [Deployment YAML](#deployment-yaml)
- [Complete Example: Gamepad Robot Teleoperation](#complete-example-gamepad-robot-teleoperation)
  - [Pipeline Topology](#pipeline-topology)
  - [Flow Descriptor (`flow.yaml`)](#flow-descriptor-flowyaml)
  - [Shared Data Types](#shared-data-types)
  - [Source Implementation](#source-implementation)
  - [Operator Implementation](#operator-implementation)
  - [Sink Implementation](#sink-implementation)
- [Autonomous Driving Pipeline Example](#autonomous-driving-pipeline-example)
  - [Flow Descriptor](#flow-descriptor)
- [TTTech Safety Patterns](#tttech-safety-patterns)
  - [Deterministic Dataflow](#deterministic-dataflow)
  - [Fault-Tolerant Pipeline Design](#fault-tolerant-pipeline-design)
  - [Real-Time Scheduling Integration](#real-time-scheduling-integration)
- [Building and Running](#building-and-running)
  - [Build All Nodes](#build-all-nodes)
  - [Run the Pipeline](#run-the-pipeline)
  - [Workspace Structure](#workspace-structure)
- [Key Types and Macros Reference](#key-types-and-macros-reference)
- [Relationship to Zenoh](#relationship-to-zenoh)

## Core Concepts

### Dataflow Graph

A Zenoh-Flow pipeline is a directed acyclic graph with three node types:

- **Source** — produces data, has no inputs. Examples: sensor drivers, file readers, camera capture.
- **Operator** — transforms data, has both inputs and outputs. Examples: object detection, data fusion, coordinate transforms.
- **Sink** — consumes data, has no outputs. Examples: actuator drivers, loggers, network publishers.

Links connect an output port of one node to an input port of another. Port types are declared in the YAML descriptor; when nodes are distributed across machines, Zenoh handles transport between them.

### Dynamic Library Loading

Each node is compiled as a Rust `cdylib` (dynamic shared library). The Zenoh-Flow runtime loads node implementations at startup using `file://` URIs pointing to `.so`/`.dylib`/`.dll` files. This makes the pipeline topology entirely declarative: swap a URI in the YAML to replace an implementation without recompiling the orchestrator.

### Runtime Infrastructure

The Zenoh-Flow runtime is embedded in a Zenoh daemon configured with the `storage_manager` plugin. Two key expression namespaces are reserved:

- `/zf/runtime/**` — runtime RPC bus (used for pipeline management operations)
- `/zenoh-flow/**` — flow state and metadata

Nodes on different machines communicate by connecting their Zenoh daemons, and the runtime uses Zenoh routing to move data between distributed operators transparently.

---

## YAML Descriptor Format

The pipeline descriptor is a YAML file with a top-level `flow` key naming the pipeline, followed by `sources`, `operators`, `sinks`, and `links` sections.

### Minimal Structure

```yaml
flow: my-pipeline

sources:
  - id: my-source
    uri: file:///path/to/libmy_source.dylib
    output:
      id: raw-data
      type: my-data-type
    period:
      length: 100
      unit: ms

operators:
  - id: my-operator
    uri: file:///path/to/libmy_operator.dylib
    inputs:
      - id: raw-data
        type: my-data-type
    outputs:
      - id: processed-data
        type: processed-type

sinks:
  - id: my-sink
    uri: file:///path/to/libmy_sink.dylib
    input:
      id: processed-data
      type: processed-type

links:
  - from:
      node: my-source
      output: raw-data
    to:
      node: my-operator
      input: raw-data

  - from:
      node: my-operator
      output: processed-data
    to:
      node: my-sink
      input: processed-data
```

### Field Reference

| Field | Description |
|-------|-------------|
| `flow` | Pipeline name (string) |
| `sources[].id` | Unique node identifier |
| `sources[].uri` | Path to the compiled dynamic library (`file://` scheme) |
| `sources[].output.id` | Name of the output port |
| `sources[].output.type` | Type tag for the port (matched against operator inputs) |
| `sources[].period` | Optional polling period (`length` + `unit`: `ms`, `s`) |
| `operators[].id` | Unique node identifier |
| `operators[].uri` | Path to the compiled dynamic library |
| `operators[].inputs[]` | Array of `{id, type}` — input port declarations |
| `operators[].outputs[]` | Array of `{id, type}` — output port declarations |
| `operators[].configuration` | Optional YAML map passed to `initialize()` as `Configuration` |
| `sinks[].id` | Unique node identifier |
| `sinks[].uri` | Path to the compiled dynamic library |
| `sinks[].input` | Single `{id, type}` — input port declaration |
| `links[].from.node` | Source node id |
| `links[].from.output` | Output port name on the source node |
| `links[].to.node` | Destination node id |
| `links[].to.input` | Input port name on the destination node |

### Configuration Passing

Operators can receive arbitrary configuration values via the `configuration` key:

```yaml
operators:
  - id: object-detector
    uri: file:///path/to/libdetector.dylib
    inputs:
      - id: frame
        type: image-frame
    outputs:
      - id: detections
        type: bounding-boxes
    configuration:
      model_path: /models/yolov8n.onnx
      confidence_threshold: 0.5
      device: cuda
```

The configuration is passed as `Option<Configuration>` to `initialize()`. `Configuration` is a type alias for `serde_json::Value`, so it can hold nested maps, arrays, strings, or numbers.

### Template Variables

The `vars` section defines template variables that can be substituted throughout the descriptor using `{{ VAR_NAME }}` syntax. This is useful for parameterizing library paths across environments:

```yaml
flow: my-pipeline

vars:
  BASE_PATH: /home/user/my-pipeline/target/release
  ROBOT_IP: 192.168.1.100

sources:
  - id: camera
    uri: file://{{ BASE_PATH }}/libcamera_source.so
    output:
      id: frame
      type: image-frame

sinks:
  - id: actuator
    uri: file://{{ BASE_PATH }}/libactuator_sink.so
    input:
      id: command
      type: twist
    configuration:
      robot_endpoint: tcp/{{ ROBOT_IP }}:7447
```

---

## Implementing Nodes in Rust

All nodes compile to `cdylib` crates and export a registration function via a macro. The `zenoh_flow` crate provides the traits and macros.

### Cargo.toml

```toml
[package]
name = "my-source"
version = "0.1.0"
edition = "2021"

[dependencies]
async-trait = "0.1"
zenoh-flow = { git = "https://github.com/eclipse-zenoh/zenoh-flow.git", tag = "v0.3.0" }

[lib]
name = "my_source"
crate-type = ["cdylib"]
```

### Data Types

All data flowing through ports must implement two traits: `ZFData` for serialization and `Deserializable` for deserialization. The `ZFData` derive macro handles the boilerplate when combined with explicit trait impls:

```rust
use serde::{Deserialize, Serialize};
use zenoh_flow::zenoh_flow_derive::ZFData;
use zenoh_flow::{Deserializable, ZFData, ZFError, ZFResult};

#[derive(Deserialize, Serialize, Debug, Clone, Copy, ZFData)]
pub struct SensorReading {
    pub temperature: f32,
    pub humidity: f32,
    pub timestamp_ms: u64,
}

impl ZFData for SensorReading {
    fn try_serialize(&self) -> ZFResult<Vec<u8>> {
        bincode::serialize(self).map_err(|_| ZFError::SerializationError)
    }
}

impl Deserializable for SensorReading {
    fn try_deserialize(bytes: &[u8]) -> ZFResult<Self> {
        bincode::deserialize(bytes).map_err(|_| ZFError::DeseralizationError)
    }
}
```

Serialization is only invoked when data crosses a distributed link (between nodes on different machines). Co-located nodes on the same machine share data by reference, bypassing serialization entirely (see [Zero-Copy Co-location](#zero-copy-co-location)).

### Implementing a Source

A Source produces data on a single output port. It implements two traits:

1. `Node` — lifecycle methods `initialize()` and `finalize()`
2. `Source` — the async `run()` method called periodically (or on demand)

```rust
use async_trait::async_trait;
use std::sync::Arc;
use zenoh_flow::{
    zenoh_flow_derive::ZFState, Configuration, Context, Data, Node, Source, State, ZFResult,
};

// Node state must derive ZFState to be type-erased into State
#[derive(Debug, ZFState)]
pub struct TemperatureSensorState {
    last_reading: f32,
    sensor_id: String,
}

pub struct TemperatureSensorSource;

impl Node for TemperatureSensorSource {
    fn initialize(&self, config: &Option<Configuration>) -> ZFResult<State> {
        // Extract configuration values if provided
        let sensor_id = config
            .as_ref()
            .and_then(|c| c.get("sensor_id"))
            .and_then(|v| v.as_str())
            .unwrap_or("default")
            .to_string();

        Ok(State::from(TemperatureSensorState {
            last_reading: 0.0,
            sensor_id,
        }))
    }

    fn finalize(&self, _state: &mut State) -> ZFResult<()> {
        // Release resources: close file handles, disconnect hardware, etc.
        Ok(())
    }
}

#[async_trait]
impl Source for TemperatureSensorSource {
    async fn run(&self, _ctx: &mut Context, state: &mut State) -> ZFResult<Data> {
        let s = state.try_get::<TemperatureSensorState>()?;

        // Read from actual sensor hardware, file, network, etc.
        let reading = SensorReading {
            temperature: read_temperature(&s.sensor_id),
            humidity: read_humidity(&s.sensor_id),
            timestamp_ms: current_time_ms(),
        };

        Ok(Data::from(reading))
    }
}

// Registration function — must match the macro name
zenoh_flow::export_source!(register);

fn register() -> ZFResult<Arc<dyn Source>> {
    Ok(Arc::new(TemperatureSensorSource) as Arc<dyn Source>)
}
```

**Key points:**
- `State::from(your_struct)` type-erases the struct into a `State` box
- `state.try_get::<YourStruct>()` retrieves it; returns `ZFError` on type mismatch
- `Data::from(value)` wraps a typed value for transmission
- `run()` is called every `period` milliseconds if a period is declared in the YAML; otherwise it is called continuously (cooperative scheduling)
- `export_source!(register)` exports the C ABI symbol the runtime looks for

### Implementing an Operator

An Operator receives data on one or more input ports and produces data on one or more output ports. It implements `Node` and `Operator`:

```rust
use std::{collections::HashMap, sync::Arc};
use zenoh_flow::{
    default_input_rule, default_output_rule, zf_empty_state, Data, DataMessage, InputToken,
    LocalDeadlineMiss, Node, NodeOutput, Operator, PortId, State, ZFError, ZFResult,
};

const INPUT_TEMP: &str = "temperature";
const INPUT_HUMIDITY: &str = "humidity";
const OUTPUT_ALERT: &str = "alert";

pub struct ThermalAlertOperator;

impl Node for ThermalAlertOperator {
    fn initialize(&self, _config: &Option<zenoh_flow::Configuration>) -> ZFResult<State> {
        // Use the zf_empty_state macro for stateless operators
        zf_empty_state!()
    }

    fn finalize(&self, _state: &mut State) -> ZFResult<()> {
        Ok(())
    }
}

impl Operator for ThermalAlertOperator {
    /// input_rule: decides whether to call run() based on available tokens.
    /// default_input_rule waits until ALL declared inputs have data.
    fn input_rule(
        &self,
        _ctx: &mut zenoh_flow::Context,
        state: &mut State,
        tokens: &mut HashMap<PortId, InputToken>,
    ) -> ZFResult<bool> {
        default_input_rule(state, tokens)
    }

    /// run: transforms inputs into outputs.
    fn run(
        &self,
        _ctx: &mut zenoh_flow::Context,
        _state: &mut State,
        inputs: &mut HashMap<PortId, DataMessage>,
    ) -> ZFResult<HashMap<PortId, Data>> {
        let mut outputs = HashMap::new();

        let temp_msg = inputs
            .remove(INPUT_TEMP)
            .ok_or_else(|| ZFError::InvalidData("missing temperature".into()))?;
        let reading = temp_msg.get_inner_data().try_get::<SensorReading>()?;

        if reading.temperature > 85.0 {
            outputs.insert(
                OUTPUT_ALERT.into(),
                Data::from(ThermalAlert {
                    temperature: reading.temperature,
                    sensor_id: reading.sensor_id.clone(),
                }),
            );
        }

        Ok(outputs)
    }

    /// output_rule: post-processes outputs before forwarding.
    /// default_output_rule passes all outputs through unchanged.
    fn output_rule(
        &self,
        _ctx: &mut zenoh_flow::Context,
        state: &mut State,
        outputs: HashMap<PortId, Data>,
        _deadline_miss: Option<LocalDeadlineMiss>,
    ) -> ZFResult<HashMap<PortId, NodeOutput>> {
        default_output_rule(state, outputs)
    }
}

zenoh_flow::export_operator!(register);

fn register() -> ZFResult<Arc<dyn Operator>> {
    Ok(Arc::new(ThermalAlertOperator) as Arc<dyn Operator>)
}
```

**Key points on the three Operator methods:**
- `input_rule()` — called before `run()`; return `true` to proceed, `false` to wait for more data. `default_input_rule` fires when all declared inputs have tokens.
- `run()` — the main transformation. `inputs` is keyed by port name; consume entries with `.remove()`. Return a map of output port name → data.
- `output_rule()` — called after `run()`; the `LocalDeadlineMiss` argument indicates if a deadline was missed. `default_output_rule` forwards all outputs without modification.

### Implementing a Sink

A Sink consumes data and produces no outputs. It implements `Node` and `Sink`:

```rust
use async_trait::async_trait;
use std::sync::Arc;
use zenoh_flow::{
    zenoh_flow_derive::ZFState, Context, DataMessage, Node, Sink, State, ZFResult,
};

#[derive(Debug, ZFState)]
pub struct LogSinkState {
    log_file: std::fs::File,
}

pub struct LogSink;

impl Node for LogSink {
    fn initialize(&self, config: &Option<zenoh_flow::Configuration>) -> ZFResult<State> {
        let path = config
            .as_ref()
            .and_then(|c| c.get("log_path"))
            .and_then(|v| v.as_str())
            .unwrap_or("/tmp/zenoh-flow.log");

        let file = std::fs::File::create(path)
            .map_err(|e| zenoh_flow::ZFError::IOError(e.to_string()))?;

        Ok(State::from(LogSinkState { log_file: file }))
    }

    fn finalize(&self, _state: &mut State) -> ZFResult<()> {
        Ok(())
    }
}

#[async_trait]
impl Sink for LogSink {
    async fn run(
        &self,
        _ctx: &mut Context,
        state: &mut State,
        mut input: DataMessage,
    ) -> ZFResult<()> {
        let s = state.try_get::<LogSinkState>()?;
        let reading = input.get_inner_data().try_get::<SensorReading>()?;

        use std::io::Write;
        writeln!(
            s.log_file,
            "{}: temp={:.1}°C humidity={:.1}%",
            reading.timestamp_ms, reading.temperature, reading.humidity
        )
        .map_err(|e| zenoh_flow::ZFError::IOError(e.to_string()))?;

        Ok(())
    }
}

zenoh_flow::export_sink!(register);

fn register() -> ZFResult<Arc<dyn Sink>> {
    Ok(Arc::new(LogSink) as Arc<dyn Sink>)
}
```

**Key points:**
- `Sink::run()` receives a single `DataMessage` (not a HashMap) since sinks declare one input port
- `export_sink!(register)` exports the expected C ABI symbol

---

## Node Lifecycle

Every node goes through three lifecycle phases:

### 1. `initialize(config)` — Startup

Called once when the runtime loads the node. The `config` argument is `Option<Configuration>` — `None` if no `configuration` block appears in the YAML.

Responsibilities:
- Allocate hardware resources (open file handles, connect to devices, load ML models)
- Parse configuration values
- Return initial operator state wrapped in `State::from(your_struct)`

### 2. `run(...)` — Execution

Called repeatedly during pipeline operation:
- **Source**: called on each polling period, returns `ZFResult<Data>`
- **Operator**: called when `input_rule` fires, returns `ZFResult<HashMap<PortId, Data>>`
- **Sink**: called on each incoming message, returns `ZFResult<()>`

State is passed in as `&mut State` and the node retrieves its concrete type with `state.try_get::<T>()`. The state persists between invocations — it is the node's memory.

The `Context` argument provides access to the Zenoh session if the node needs to publish/subscribe independently of the flow graph (e.g., a sink that writes to a zenoh key rather than a file).

### 3. `finalize(state)` — Shutdown

Called once when the runtime tears down the pipeline. Release resources: close file handles, disconnect hardware, flush buffers. The `state` argument allows accessing the node's state for cleanup.

---

## Zero-Copy Co-location

When multiple nodes run on the same machine in the same Zenoh-Flow daemon process, the runtime detects this and passes data between them by pointer — no serialization or deserialization occurs.

The `ZFData::try_serialize()` and `Deserializable::try_deserialize()` methods are only called when data must cross a network boundary (i.e., when the receiving node runs on a different machine).

**Performance implications:**
- Co-located operators: essentially zero overhead between nodes — data passes as `Arc<dyn ZFData>`
- Distributed operators: overhead is Zenoh transport + your serialization format (bincode, protobuf, CDR, etc.)
- CPU savings: no encode/decode cycles for co-located pipeline segments
- Latency: sub-microsecond between co-located nodes vs. network RTT + ser/deser for distributed

This makes it practical to prototype a full pipeline on a single machine and then selectively distribute heavy compute stages (e.g., ML inference) to remote GPU nodes without changing any node code — only the YAML deployment descriptor changes.

---

## Distributed Deployment

In a multi-machine deployment, each machine runs a Zenoh daemon configured as a Zenoh-Flow router. The daemons connect to each other via standard Zenoh peer or router links, and the Zenoh-Flow runtime uses Zenoh's routing to forward data between nodes on different hosts.

### Router Configuration

The Zenoh daemon must load the `storage_manager` plugin and reserve two key expression spaces for Zenoh-Flow's internal RPC mechanism:

```json
{
    "listen": {
        "endpoints": ["tcp/0.0.0.0:7447"]
    },
    "connect": {
        "endpoints": ["tcp/orchestrator-host:7447"]
    },
    "scouting": {
        "multicast": { "enabled": false }
    },
    "plugins_search_dirs": ["/usr/lib/"],
    "plugins": {
        "storage_manager": {
            "required": true,
            "storages": {
                "zfrpc": {
                    "key_expr": "/zf/runtime/**",
                    "volume": "memory"
                },
                "zf": {
                    "key_expr": "/zenoh-flow/**",
                    "volume": "memory"
                }
            }
        }
    }
}
```

Each worker node runs this configuration, connecting back to the orchestrator. The orchestrator also runs the same configuration plus the pipeline launch command.

### Deployment YAML

*Note: The distributed deployment syntax was evolving in zenoh-flow v0.3. The following reflects the architectural intent derived from the codebase and talks — actual syntax may vary. Check the zenoh-flow README for the current deployment descriptor format.*

In a distributed descriptor, each node can declare which runtime endpoint it runs on:

```yaml
flow: distributed-sensing

sources:
  - id: camera-source
    uri: file:///opt/pipeline/libcamera_source.so
    output:
      id: frame
      type: image-frame
    period:
      length: 33
      unit: ms
    # runs on the edge device
    runtime: tcp/edge-device:7447

operators:
  - id: ml-detector
    uri: file:///opt/pipeline/libml_detector.so
    inputs:
      - id: frame
        type: image-frame
    outputs:
      - id: detections
        type: bounding-boxes
    configuration:
      model: /models/detector.onnx
    # runs on the GPU server
    runtime: tcp/gpu-server:7447

sinks:
  - id: results-logger
    uri: file:///opt/pipeline/libresults_logger.so
    input:
      id: detections
      type: bounding-boxes
    # co-located with the orchestrator
    runtime: tcp/orchestrator:7447

links:
  - from:
      node: camera-source
      output: frame
    to:
      node: ml-detector
      input: frame
  - from:
      node: ml-detector
      output: detections
    to:
      node: results-logger
      input: detections
```

When the `camera-source → ml-detector` link crosses machines, Zenoh-Flow serializes the frame using `ZFData::try_serialize()` and routes it through the Zenoh daemon mesh. The `ml-detector → results-logger` link, if co-located, passes the bounding boxes by pointer.

---

## Complete Example: Gamepad Robot Teleoperation

This is the actual `gamepad-dragonbot` demo from the zenoh-demos repository. It illustrates all three node types in a working pipeline.

### Pipeline Topology

```
gamepad-input (Source)
    └── gamepad-input port
         ↓
    twist (Operator)
         └── twist port
              ↓
    sink-serialize (Sink)
         └── publishes to Zenoh key /rt/cmd_vel
```

### Flow Descriptor (`flow.yaml`)

```yaml
flow: gamepad-dragonbot

sources:
  - id: gamepad-input
    uri: file:///path/to/libsource_gamepad.dylib
    output:
      id: gamepad-input
      type: gamepad-input
    period:
      length: 100
      unit: ms

operators:
  - id: twist
    uri: file:///path/to/liboperator_twist.dylib
    inputs:
      - id: gamepad-input
        type: gamepad-input
    outputs:
      - id: twist
        type: twist

sinks:
  - id: sink-serialize
    uri: file:///path/to/libsink_serialize.dylib
    input:
      id: twist
      type: twist

links:
  - from:
      node: gamepad-input
      output: gamepad-input
    to:
      node: twist
      input: gamepad-input

  - from:
      node: twist
      output: twist
    to:
      node: sink-serialize
      input: twist
```

### Shared Data Types

Both `GamepadInput` and `Twist` use bincode for serialization. The derive macros handle the ZFData boilerplate:

```rust
use serde::{Deserialize, Serialize};
use zenoh_flow::zenoh_flow_derive::ZFData;
use zenoh_flow::{Deserializable, ZFData, ZFError, ZFResult};

#[derive(Deserialize, Serialize, Debug, Clone, Copy, ZFData)]
pub struct GamepadInput {
    pub left_trigger: f32,   // 0.0..1.0, goes backward
    pub right_trigger: f32,  // 0.0..1.0, goes forward
    pub left_stick_x: f32,   // -1.0..1.0, turns left/right
}

impl ZFData for GamepadInput {
    fn try_serialize(&self) -> ZFResult<Vec<u8>> {
        bincode::serialize(self).map_err(|_| ZFError::SerializationError)
    }
}

impl Deserializable for GamepadInput {
    fn try_deserialize(bytes: &[u8]) -> ZFResult<Self> {
        bincode::deserialize(bytes).map_err(|_| ZFError::DeseralizationError)
    }
}

#[derive(Deserialize, Serialize, Debug, Clone, Copy, ZFData)]
pub struct Twist {
    pub linear: f32,   // m/s
    pub angular: f32,  // rad/s
}

impl ZFData for Twist {
    fn try_serialize(&self) -> ZFResult<Vec<u8>> {
        bincode::serialize(self).map_err(|_| ZFError::SerializationError)
    }
}

impl Deserializable for Twist {
    fn try_deserialize(bytes: &[u8]) -> ZFResult<Self> {
        bincode::deserialize(bytes).map_err(|_| ZFError::DeseralizationError)
    }
}
```

### Source Implementation

The gamepad source polls the `gilrs` library every 100ms and emits the current button/stick state:

```rust
use async_trait::async_trait;
use gilrs::{EventType, Gilrs};
use std::sync::{Arc, Mutex};
use zenoh_flow::{
    zenoh_flow_derive::ZFState, Configuration, Context, Data, Node, Source, State, ZFError,
    ZFResult,
};

#[derive(Debug, ZFState)]
pub struct GamepadState {
    gilrs: Arc<Mutex<Gilrs>>,
    input: GamepadInput,
}

pub struct GamepadSource;

impl Node for GamepadSource {
    fn initialize(&self, _: &Option<Configuration>) -> ZFResult<State> {
        let gilrs = Gilrs::new().expect("Could not start Gilrs");
        Ok(State::from(GamepadState {
            gilrs: Arc::new(Mutex::new(gilrs)),
            input: GamepadInput::default(),
        }))
    }

    fn finalize(&self, _: &mut State) -> ZFResult<()> {
        Ok(())
    }
}

#[async_trait]
impl Source for GamepadSource {
    async fn run(&self, _: &mut Context, state: &mut State) -> ZFResult<Data> {
        let state = state.try_get::<GamepadState>()?;
        let mut gilrs = state.gilrs.lock().map_err(|_| ZFError::GenericError)?;

        // Drain all pending events, updating the accumulated input state
        while let Some(event) = gilrs.next_event() {
            match event.event {
                EventType::ButtonChanged(button, value, _) => match button {
                    gilrs::Button::LeftTrigger2 => state.input.left_trigger = value,
                    gilrs::Button::RightTrigger2 => state.input.right_trigger = value,
                    _ => (),
                },
                EventType::AxisChanged(stick, value, _) => {
                    if stick == gilrs::Axis::LeftStickX {
                        state.input.left_stick_x = value
                    }
                }
                _ => (),
            }
        }

        Ok(Data::from(state.input))
    }
}

zenoh_flow::export_source!(register);

fn register() -> ZFResult<Arc<dyn Source>> {
    Ok(Arc::new(GamepadSource) as Arc<dyn Source>)
}
```

### Operator Implementation

The twist operator converts raw gamepad axes into linear and angular velocity:

```rust
use std::{collections::HashMap, sync::Arc};
use zenoh_flow::{
    default_input_rule, default_output_rule, zf_empty_state, Data, Node, Operator, PortId, ZFError,
};

const INPUT_PORT_ID: &str = "gamepad-input";
const OUTPUT_PORT_ID: &str = "twist";

pub struct OperatorTwist;

impl Node for OperatorTwist {
    fn initialize(&self, _: &Option<zenoh_flow::Configuration>) -> zenoh_flow::ZFResult<zenoh_flow::State> {
        zf_empty_state!()   // stateless operator
    }

    fn finalize(&self, _: &mut zenoh_flow::State) -> zenoh_flow::ZFResult<()> {
        Ok(())
    }
}

impl Operator for OperatorTwist {
    fn input_rule(
        &self,
        _: &mut zenoh_flow::Context,
        state: &mut zenoh_flow::State,
        tokens: &mut HashMap<zenoh_flow::PortId, zenoh_flow::InputToken>,
    ) -> zenoh_flow::ZFResult<bool> {
        default_input_rule(state, tokens)
    }

    fn run(
        &self,
        _: &mut zenoh_flow::Context,
        _: &mut zenoh_flow::State,
        inputs: &mut HashMap<zenoh_flow::PortId, zenoh_flow::DataMessage>,
    ) -> zenoh_flow::ZFResult<HashMap<zenoh_flow::PortId, zenoh_flow::Data>> {
        let mut outputs = HashMap::<PortId, Data>::with_capacity(1);

        let mut gamepad_input_raw = inputs
            .remove(INPUT_PORT_ID)
            .ok_or_else(|| ZFError::InvalidData("No data".to_string()))?;

        let gamepad_input = gamepad_input_raw
            .get_inner_data()
            .try_get::<GamepadInput>()?;

        // Convert gamepad axes to Twist velocities
        let twist = Twist {
            linear: (gamepad_input.right_trigger - gamepad_input.left_trigger) * 0.20,
            angular: -gamepad_input.left_stick_x * 2.60,
        };

        outputs.insert(OUTPUT_PORT_ID.into(), Data::from::<Twist>(twist));
        Ok(outputs)
    }

    fn output_rule(
        &self,
        _: &mut zenoh_flow::Context,
        state: &mut zenoh_flow::State,
        outputs: HashMap<zenoh_flow::PortId, zenoh_flow::Data>,
        _: Option<zenoh_flow::LocalDeadlineMiss>,
    ) -> zenoh_flow::ZFResult<HashMap<zenoh_flow::PortId, zenoh_flow::NodeOutput>> {
        default_output_rule(state, outputs)
    }
}

zenoh_flow::export_operator!(register);

fn register() -> zenoh_flow::ZFResult<Arc<dyn Operator>> {
    Ok(Arc::new(OperatorTwist) as Arc<dyn Operator>)
}
```

### Sink Implementation

The serialize sink receives Twist messages and puts them as raw bytes onto a Zenoh key that a physical robot subscribes to:

```rust
use async_trait::async_trait;
use std::sync::Arc;
use zenoh::prelude::ZFuture;
use zenoh_flow::{zenoh_flow_derive::ZFState, Context, DataMessage, Node, Sink, State, ZFResult};

#[derive(Debug, ZFState)]
pub struct SinkState {
    buffer: [u8; 48],
    session: Option<zenoh::Session>,
    expr_id: u64,
}

pub struct SinkSerialize;

impl Node for SinkSerialize {
    fn initialize(&self, _: &Option<zenoh_flow::Configuration>) -> zenoh_flow::ZFResult<zenoh_flow::State> {
        let mut config = zenoh::config::default();
        config.connect.set_endpoints(
            vec!["tcp/192.168.86.12:7447"]
                .iter()
                .filter_map(|l| l.parse().ok())
                .collect(),
        ).expect("Could not set locator");

        let session = zenoh::open(config).wait().expect("Could not open Session.");
        let expr_id = session.declare_expr("/rt/cmd_vel").wait()
            .expect("Could not declare expression.");

        Ok(State::from(SinkState {
            buffer: [0u8; 48],
            session: Some(session),
            expr_id,
        }))
    }

    fn finalize(&self, dyn_state: &mut zenoh_flow::State) -> zenoh_flow::ZFResult<()> {
        let state = dyn_state.try_get::<SinkState>()?;
        if let Some(session) = &state.session {
            session.undeclare_expr(state.expr_id).wait()
                .expect("Could not undeclare expr");
        }
        state.session.take().unwrap().close().wait()
            .expect("Could not close Session");
        Ok(())
    }
}

#[async_trait]
impl Sink for SinkSerialize {
    async fn run(&self, _: &mut Context, dyn_state: &mut State, mut input: DataMessage) -> ZFResult<()> {
        let twist = input.get_inner_data().try_get::<Twist>()?;
        let state = dyn_state.try_get::<SinkState>()?;

        // Serialize Twist into the AVR float64 format expected by the robot firmware
        serialize_avr_float_64(&mut state.buffer[0..8], twist.linear);   // linear.x
        serialize_avr_float_64(&mut state.buffer[40..48], twist.angular); // angular.z

        if let Some(session) = &state.session {
            session.put(state.expr_id, &state.buffer[..]).wait()
                .expect("Could not put data.");
        }

        Ok(())
    }
}

zenoh_flow::export_sink!(register);

fn register() -> ZFResult<Arc<dyn Sink>> {
    Ok(Arc::new(SinkSerialize) as Arc<dyn Sink>)
}
```

---

## Autonomous Driving Pipeline Example

*This example is derived from the recorded 1h18m tutorial (YouTube: wGEM6-ByAL8) and represents the architectural pattern demonstrated — not a directly tested codebase.*

The tutorial builds a pipeline where a vehicle's perception and control stack runs across edge and cloud:

```
Camera Source ──────────┐
                        ↓
LIDAR Source ──→ Sensor Fusion Operator ──→ Object Detection Operator ──→ Path Planning Operator
                                                                                    ↓
GPS/IMU Source ─────────────────────────────────────────────────────────→ CAN Bus Sink
                                                                                    ↓
                                                                            Telemetry Sink
```

### Flow Descriptor

```yaml
flow: autonomous-driving-demo

vars:
  EDGE_LIB: /opt/pipeline/edge/target/release
  CLOUD_LIB: /opt/pipeline/cloud/target/release
  EDGE_NODE: tcp/edge-vehicle:7447
  CLOUD_NODE: tcp/cloud-gpu:7447

sources:
  - id: camera
    uri: file://{{ EDGE_LIB }}/libcamera_source.so
    output:
      id: frame
      type: image-frame
    period:
      length: 33
      unit: ms
    runtime: "{{ EDGE_NODE }}"

  - id: lidar
    uri: file://{{ EDGE_LIB }}/liblidar_source.so
    output:
      id: point-cloud
      type: lidar-scan
    period:
      length: 100
      unit: ms
    runtime: "{{ EDGE_NODE }}"

  - id: gps-imu
    uri: file://{{ EDGE_LIB }}/libgps_imu_source.so
    output:
      id: pose
      type: vehicle-pose
    period:
      length: 10
      unit: ms
    runtime: "{{ EDGE_NODE }}"

operators:
  - id: sensor-fusion
    uri: file://{{ EDGE_LIB }}/libsensor_fusion.so
    inputs:
      - id: frame
        type: image-frame
      - id: point-cloud
        type: lidar-scan
    outputs:
      - id: fused-scene
        type: fused-perception
    runtime: "{{ EDGE_NODE }}"

  - id: object-detection
    uri: file://{{ CLOUD_LIB }}/libobject_detection.so
    inputs:
      - id: fused-scene
        type: fused-perception
    outputs:
      - id: detections
        type: detection-list
    configuration:
      model: /models/yolov8-driving.onnx
      device: cuda:0
    runtime: "{{ CLOUD_NODE }}"

  - id: path-planning
    uri: file://{{ CLOUD_LIB }}/libpath_planning.so
    inputs:
      - id: detections
        type: detection-list
      - id: pose
        type: vehicle-pose
    outputs:
      - id: control-cmd
        type: vehicle-control
    configuration:
      max_speed_ms: 15.0
      safety_margin_m: 1.5
    runtime: "{{ CLOUD_NODE }}"

sinks:
  - id: can-bus
    uri: file://{{ EDGE_LIB }}/libcan_bus_sink.so
    input:
      id: control-cmd
      type: vehicle-control
    runtime: "{{ EDGE_NODE }}"

  - id: telemetry-logger
    uri: file://{{ CLOUD_LIB }}/libtelemetry_logger.so
    input:
      id: control-cmd
      type: vehicle-control
    configuration:
      influx_url: http://localhost:8086
      db: vehicle-telemetry
    runtime: "{{ CLOUD_NODE }}"

links:
  - from: { node: camera, output: frame }
    to:   { node: sensor-fusion, input: frame }

  - from: { node: lidar, output: point-cloud }
    to:   { node: sensor-fusion, input: point-cloud }

  - from: { node: sensor-fusion, output: fused-scene }
    to:   { node: object-detection, input: fused-scene }

  - from: { node: object-detection, output: detections }
    to:   { node: path-planning, input: detections }

  - from: { node: gps-imu, output: pose }
    to:   { node: path-planning, input: pose }

  - from: { node: path-planning, output: control-cmd }
    to:   { node: can-bus, input: control-cmd }

  - from: { node: path-planning, output: control-cmd }
    to:   { node: telemetry-logger, input: control-cmd }
```

**Distribution:** Camera, LIDAR, GPS/IMU, sensor fusion, and CAN bus run on the edge vehicle. Object detection and path planning run on the cloud GPU node. Zenoh-Flow serializes data at the `sensor-fusion → object-detection` boundary (edge → cloud) and at the `path-planning → can-bus` boundary (cloud → edge).

---

## TTTech Safety Patterns

*Derived from the recorded TTTech session (YouTube: GsEuPucS4F4). These describe architectural practices; consult current zenoh-flow documentation for implementation specifics.*

### Deterministic Dataflow

Zenoh-Flow's operator execution model supports determinism requirements for safety-critical systems:

- **Input rule control**: Custom `input_rule()` implementations can enforce strict ordering — for example, requiring a timestamp-monotonicity check before firing `run()`.
- **Deadline tracking**: The `LocalDeadlineMiss` parameter in `output_rule()` carries timing violation information. Safety-critical operators can check this value and take fail-safe action (e.g., emit a zero-velocity command) rather than processing stale data.
- **Bounded execution**: Zenoh-Flow's cooperative async model, combined with fixed polling periods on sources, provides bounded input rates. An operator's `run()` is never called at a rate higher than the slowest source it depends on.

### Fault-Tolerant Pipeline Design

For safety certification contexts, the pipeline architecture should separate concerns:

```yaml
# Safe pattern: dedicated watchdog sink monitors heartbeats
operators:
  - id: safety-monitor
    uri: file:///lib/libsafety_monitor.so
    inputs:
      - id: control-cmd
        type: vehicle-control
      - id: system-heartbeat
        type: heartbeat
    outputs:
      - id: safe-cmd
        type: vehicle-control
    configuration:
      heartbeat_timeout_ms: 200
      fallback_behavior: zero-velocity
```

**Patterns used in safety deployments:**

1. **Heartbeat sources**: A dedicated Source node emits periodic heartbeat tokens. A safety operator consumes both the control command and the heartbeat; if the heartbeat times out (detected via `input_rule`), it emits a safe fallback command instead.

2. **Redundant sinks**: Critical commands go to multiple sinks (actuator + logger + monitor). A monitoring sink can raise an alarm if the pipeline stalls.

3. **Separation of concerns**: Safety functions (watchdog, voting, mode arbitration) are implemented as dedicated operators with their own state, independent of functional operators. This allows the safety layer to be certified separately.

4. **Immutable state per invocation**: Because `run()` takes `&mut State` (node-private state) and inputs arrive as messages (not shared mutable references), there is no shared mutable state between concurrent operator invocations. This simplifies formal reasoning about operator behavior.

### Real-Time Scheduling Integration

Zenoh-Flow runs atop an async executor (typically async-std). For hard real-time guarantees, operators that require low-jitter execution should:

- Pin their Zenoh daemon to isolated CPU cores using OS-level CPU affinity
- Use real-time thread priorities (SCHED_FIFO/SCHED_RR on Linux) for the daemon process
- Minimize allocations inside `run()` — pre-allocate buffers in `initialize()`
- Keep `run()` execution time bounded and measurable

Zenoh-Flow itself does not enforce RTOS scheduling, but its architectural separation (sources run periodically, operators fire on input arrival) maps cleanly onto real-time task models.

---

## Building and Running

### Build All Nodes

Each node crate is a `cdylib`. Build them with Cargo:

```bash
# From the workspace root
cargo build --release

# Output: target/release/libsource_gamepad.dylib (macOS)
#                         libsource_gamepad.so   (Linux)
#                         source_gamepad.dll     (Windows)
```

Update the `uri` fields in `flow.yaml` to point to the built libraries.

### Run the Pipeline

*Note: The exact CLI invocation depends on the zenoh-flow runtime version. Check the zenoh-flow repository for current runtime tooling.*

```bash
# Start the Zenoh-Flow-enabled daemon
zenohd -c zenoh-zf-router.json

# Deploy and start the flow (CLI varies by version)
# For 0.6.0-rc+ standalone runtime:
# zenoh-flow-standalone-runtime ./flow.yaml
# For 0.6.0-rc+ daemon mode (zfctl):
# zfctl instance create flow.yaml
# zfctl instance start <uuid>
```

For the gamepad demo, the router connects to the robot at `tcp/192.168.86.12:7447` and the flow publishes Twist commands to `/rt/cmd_vel`.

### Workspace Structure

```
my-pipeline/
├── Cargo.toml          # [workspace] with member crates
├── flow.yaml           # Pipeline descriptor
├── zenoh-router.json   # Zenoh daemon config
├── types/              # Shared data types (ZFData impls)
│   ├── Cargo.toml
│   └── src/lib.rs
├── source-sensor/      # Source node
│   ├── Cargo.toml      # crate-type = ["cdylib"]
│   └── src/lib.rs
├── operator-process/   # Operator node
│   ├── Cargo.toml
│   └── src/lib.rs
└── sink-output/        # Sink node
    ├── Cargo.toml
    └── src/lib.rs
```

---

## Key Types and Macros Reference

| Item | Description |
|------|-------------|
| `Node` trait | `initialize(config) -> ZFResult<State>`, `finalize(state) -> ZFResult<()>` |
| `Source` trait | async `run(ctx, state) -> ZFResult<Data>` |
| `Operator` trait | `input_rule(ctx, state, tokens)`, `run(ctx, state, inputs)`, `output_rule(ctx, state, outputs, deadline)` |
| `Sink` trait | async `run(ctx, state, input) -> ZFResult<()>` |
| `State` | Type-erased node state; use `State::from(x)` and `state.try_get::<T>()` |
| `Data` | Type-erased data value; use `Data::from(x)` and `data.try_get::<T>()` |
| `DataMessage` | Incoming data message; call `.get_inner_data()` then `.try_get::<T>()` |
| `Configuration` | Alias for `serde_json::Value`; passed to `initialize()` |
| `Context` | Runtime context; provides Zenoh session access |
| `ZFData` trait | `try_serialize() -> ZFResult<Vec<u8>>` — implement for all port types |
| `Deserializable` trait | `try_deserialize(bytes) -> ZFResult<Self>` — implement for all port types |
| `ZFState` derive | Enables a struct to be stored in `State` |
| `ZFData` derive | Implements the derive-macro portion of `ZFData` |
| `zf_empty_state!()` | Macro: returns `Ok(State::from(EmptyState))` for stateless operators |
| `default_input_rule` | Fires `run()` when all inputs have tokens |
| `default_output_rule` | Forwards all outputs without modification |
| `export_source!(fn)` | Exports C ABI registration symbol for Source |
| `export_operator!(fn)` | Exports C ABI registration symbol for Operator |
| `export_sink!(fn)` | Exports C ABI registration symbol for Sink |
| `ZFError` | Error enum: `GenericError`, `InvalidData(String)`, `SerializationError`, `DeseralizationError`, `IOError(String)`, etc. |

---

## Relationship to Zenoh

Zenoh-Flow uses Zenoh as its transport layer but adds a structured execution model on top:

| Zenoh | Zenoh-Flow |
|-------|-----------|
| Pub/sub, queryable, storage | Dataflow pipeline orchestration |
| Key expressions route data | Typed ports connect nodes |
| Application manages session lifecycle | Runtime manages node lifecycle |
| Data is untyped bytes | Data has declared port types |
| No execution model | Source/Operator/Sink with lifecycle |
| Application handles serialization | Framework handles ser/deser at boundaries |

Zenoh-Flow does not replace Zenoh — a Sink can open its own Zenoh session to publish results to arbitrary key expressions (as the gamepad sink does to reach the robot). The flow graph handles structured pipeline data; plain Zenoh handles everything else.

---

*Sources: zenoh-demos/gamepad-dragonbot source code (v0.3.0), zenoh-flow crate API, YouTube sessions ik_ZwEzqmZk (introduction), wGEM6-ByAL8 (autonomous driving tutorial), GsEuPucS4F4 (TTTech safety patterns). Distributed deployment YAML and autonomous driving example are architectural reconstructions; verify against current zenoh-flow documentation before production use.*

## See Also

- [Programming Model Guide](programming-model-guide.md) — the underlying Zenoh pub/sub and query API that Zenoh-Flow nodes use internally
- [Node Types Guide](node-types-guide.md) — how the Zenoh router infrastructure hosts Zenoh-Flow runtimes
- [Key Expressions Guide](key-expressions-guide.md) — how Zenoh-Flow nodes interface with the broader Zenoh key expression namespace

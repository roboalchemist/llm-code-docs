# Source: https://docs.edgeimpulse.com/tutorials/topics/zephyr/zephyr-module-series.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Zephyr series overview

> A series of tutorials on using Edge Impulse Zephyr Module for deploying machine learning models using the Edge Impulse Zephyr Module

This series of tutorials builds on the static buffer deployment [Run Zephyr Module](/hardware/deployments/run-zephyr-module) tutorial, advancing from basic examples to application-level implementations using Edge Impulse Zephyr Module. You'll learn to deploy models, work with sensors, and port applications between different Zephyr-supported boards.

## Command Extension for Build & Deploy

```mermaid  theme={"system"}
graph LR
    A[Studio] -->|west ei-build| B[Build API]
    B -->|west ei-deploy| C[Download Model]
    C -->|west build| D[Compile Firmware]
    D -->|west flash| E[Deploy to Device]
    
    style A fill:#9b59b6
    style B fill:#3498db
    style C fill:#e67e22
    style D fill:#2ecc71
    style E fill:#f39c12
```

## Prerequisites

Basic knowledge of Zephyr is required before using the Edge Impulse Zephyr Module, there are many excellent resources available, and this series is not a Zephyr primer. Additionally, before beginning this series, complete the static buffer deployment tutorial to understand the foundational concepts of our [Edge Impulse Zephyr Module deployment](/hardware/deployments/run-zephyr-module).

## Getting started

First follow the Edge Impulse Zephyr module deployment instructions, then explore the other tutorials to enhance your Zephyr projects with Edge Impulse capabilities.

* [Getting Started with Edge Impulse Zephyr Module](/hardware/deployments/run-zephyr-module)

## Tutorials in this series

<CardGroup cols={2}>
  <Card title="Getting Started" icon="rocket" href="/hardware/deployments/run-zephyr-module">
    Deploy your first model (15 min)
  </Card>

  <Card title="Porting Between Boards" icon="arrows-rotate" href="./porting-between-boards">
    Move projects across hardware (20 min)
  </Card>

  <Card title="Using IMU Sensors" icon="rotate" href="./zephyr-module-imu">
    Accelerometer and gyroscope integration (30 min)
  </Card>

  <Card title="Microphone Keyword Spotting" icon="microphone" href="./zephyr-module-microphone-kws">
    Audio classification with PDM microphones (30 min)
  </Card>

  <Card title="Arduino Uno Q" icon="microchip" href="./arduino-unoq-zephyr">
    Dual-system board with unique debugging (25 min)
  </Card>

  <Card title="Thread Inferencing" icon="cubes" href="https://github.com/edgeimpulse/ei-zephyr-thread-inference">
    Run inference on Thread (30 min)
  </Card>

  <Card title="Data acquisition" icon="network-wired" href="https://github.com/edgeimpulse/ei-zephyr-sensors-dataforwarder">
    Stream sensor data to Edge Impulse (20 min)
  </Card>
</CardGroup>

...more tutorials coming soon!

## Repositories

* [Example Standalone Inferencing](https://github.com/edgeimpulse/example-standalone-inferencing-zephyr-module) Reference project with static buffer inference
* [Edge Impulse SDK Zephyr Module](https://github.com/edgeimpulse/edge-impulse-sdk-zephyr) Core SDK as Zephyr module
* [IMU Inference](https://github.com/edgeimpulse/ei-zephyr-imu-inference) Full firmware with sensors
* [Microphone Keyword Spotting Inference](https://github.com/edgeimpulse/ei-zephyr-mic-kws-inference) Full firmware with microphone input

## Need Help?

* [Edge Impulse Forum](https://forum.edgeimpulse.com/)
* [Report Issues](https://github.com/edgeimpulse/edge-impulse-sdk-zephyr/issues)


Built with [Mintlify](https://mintlify.com).
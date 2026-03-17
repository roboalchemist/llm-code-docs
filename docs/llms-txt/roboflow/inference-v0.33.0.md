# Source: https://docs.roboflow.com/changelog/january-2025/inference-v0.33.0.md

# Inference v0.33.0

## 🚀 Added

#### Llama Vision 3.2 🤝 other VLMs supported in Workflows

We welcome new block bringing [Llama Vision 3.2](https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/) to workflows ecosystem!

Llama 3.2 is a new generation of vision and lightweight models that fit on edge devices, tailored for use cases that require more private and personalized AI experiences.

Brought by [@AHB102](https://github.com/AHB102) in [#866](https://github.com/roboflow/inference/pull/866)

Related changes:

* Fix/onboarding llama 3.2 by [@PawelPeczek-Roboflow](https://github.com/PawelPeczek-Roboflow) in [#927](https://github.com/roboflow/inference/pull/927)
* Tests for LLama Vision 3.2 by [@PawelPeczek-Roboflow](https://github.com/PawelPeczek-Roboflow) in [#928](https://github.com/roboflow/inference/pull/928)

#### MQTT Writer Enterprise Workflow Block (added in [#930](https://github.com/roboflow/inference/pull/930))

This block enables our enterprise users to publish messages to an MQTT broker through Workflows.

MQTT (Message Queuing Telemetry Transport) is a lightweight messaging protocol designed for low-bandwidth, high-latency, or unreliable networks. It's widely used in applications where devices need to communicate with minimal overhead, such as the Internet of Things (IoT).

With this change workflows can communicate with the world through MQTT!

Change introduced by [@chandlersupple](https://github.com/chandlersupple)

#### Plc EthernetIP Enterprise Workflow Block (added in [#905](https://github.com/roboflow/inference/pull/905))

This block enables our enterprise users to interface with PLC.\
A Programmable Logic Controller (PLC) is an industrial computer specifically designed to automate machinery and processes in manufacturing and other industries. It monitors inputs (e.g., sensors), processes data based on a programmed logic, and controls outputs (e.g., actuators) to perform tasks.\
This block is utilizing `pylogix` library over Ethernet/IP. Block supports three modes of operation:

* read: Reads specified tags from the PLC.
* write: Writes specified values to the PLC tags.
* read\_and\_write: Performs both read and write operations in a single execution.

This change brings vision capabilities into real-world industrial plants!

Change introduced by [@reedajohns](https://github.com/reedajohns)

## 💪 Improved

#### Documentation improvements

[@yeldarby](https://github.com/yeldarby) transforms Inference docs with streamlined navigation, styling, and instant rendering!

* [Refresh README](https://github.com/roboflow/inference/pull/908)
* [Update Docs Styling & Nav](https://github.com/roboflow/inference/pull/912)
* [Add Side Nav to Blocks and Kinds Gallery Page](https://github.com/roboflow/inference/pull/910)
* [Add Instant Rendering for Docs](https://github.com/roboflow/inference/pull/917)
* [Docs: Update Links](https://github.com/roboflow/inference/pull/919)
* [Update Landing Page](https://github.com/roboflow/inference/pull/920)

More contributions enhancing Inference documentation:

* better version handling in generated block pages by [@hansent](https://github.com/hansent) in [#922](https://github.com/roboflow/inference/pull/922)
* Update README.md by [@ThatOrJohn](https://github.com/ThatOrJohn) in [#921](https://github.com/roboflow/inference/pull/921)

#### Improvements to CI by [@alexnorell](https://github.com/alexnorell)

* [Add readiness endpoint for dedicated deployments](https://github.com/roboflow/inference/pull/909)
* [Support forks](https://github.com/roboflow/inference/pull/924)
* [Remove explicit checkout ref](https://github.com/roboflow/inference/pull/925)

#### Other changes

* Add env-injectable headers to RF API requests by [@PawelPeczek-Roboflow](https://github.com/PawelPeczek-Roboflow) in [#932](https://github.com/roboflow/inference/pull/932)
* Pass roboflow workflow ID as usage\_workflow\_id if available by [@grzegorz-roboflow](https://github.com/grzegorz-roboflow) in [#926](https://github.com/roboflow/inference/pull/926)
* Collect usage after execution of decorated methods by [@grzegorz-roboflow](https://github.com/grzegorz-roboflow) in [#931](https://github.com/roboflow/inference/pull/931)
* Improved the SizeMeasurementBlock Docs by [@chandlersupple](https://github.com/chandlersupple) in [#916](https://github.com/roboflow/inference/pull/916)

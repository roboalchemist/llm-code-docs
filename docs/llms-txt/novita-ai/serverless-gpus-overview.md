# Source: https://novita.ai/docs/guides/serverless-gpus-overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

The GPU elastic container product designed specifically for **AI inference**. You only need to specify the container image address and make slight configurations according to your business scenarios to quickly deploy an AI inference service.

## Features

* With the capability of **elastic scaling**, it automatically scales up during peak business traffic and scales down during low traffic periods, ensuring service stability while saving costs as much as possible;
* Built-in efficient **load balancing** ensures that request loads are evenly distributed to each GPU container instance;
* Billing is **accurate to the second**, charging only for the actual running time of the GPU container instances;
* Through technologies such as GPU container instance reservation, image preheating, and high-performance hardware, it can achieve **second-level cold-start**, easily handling traffic peaks;
* Complete **log panel** supports querying real-time log streams, helping you quickly identify and resolve potential issues.

## Terminology

* **Container Image Address**: Refers to the Docker container image address, currently supporting **"public image"** and **"private image"**.
* **Serverless Endpoint**: Represents a GPU elastic container instance. It includes components such as **worker**, **load balancer**, and **elastic scaler**.
* **Worker**: A GPU container instance used by the serverless endpoint to handle specific requests. One Worker corresponds to one GPU container instance.
* **Scale Policy**: Used to control the logic of automatically scaling up during traffic peaks and scaling down during low traffic periods.
* **Health Check Path**: The built-in load balancer performs health checks through this path, determining whether to forward requests to the Worker based on whether the returned status code is `200`.


Built with [Mintlify](https://mintlify.com).
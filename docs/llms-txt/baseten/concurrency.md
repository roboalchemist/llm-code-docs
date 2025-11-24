# Source: https://docs.baseten.co/development/model/performance/concurrency.md

# Request concurrency

> A guide to setting concurrency for your model

Configuring concurrency optimizes **model performance**, balancing **throughput** and **latency**.

In Baseten & Truss, concurrency is managed at **two levels**:

1. **Concurrency Target** – Limits the number of requests **sent** to a single replica.
2. **Predict Concurrency** – Limits how many requests the predict function handles **inside the model container**.

## 1. Concurrency Target

* **Set in the Baseten UI** – Defines how many requests a single replica can process at once.
* **Triggers autoscaling** – If all replicas hit the concurrency target, additional replicas spin up.

**Example:**

* **Concurrency Target = 2, Single Replica**
* **5 requests arrive** → 2 are processed immediately, **3 are queued**.
* If max replicas aren't reached, **autoscaling spins up a new replica**.

## 2. Predict Concurrency

* **Set in** `config.yaml` – Controls how many requests can be **processed by** predict simultaneously.
* **Protects GPU resources** – Prevents multiple requests from overloading the GPU.

### Configuring Predict Concurrency

```yaml config.yaml theme={"system"}
model_name: "My model with concurrency limits"
runtime:
  predict_concurrency: 2  # Default is 1
```

### How It Works Inside a Model Pod

1. **Requests arrive** → All begin preprocessing (e.g., downloading images from S3).
2. **Predict runs on GPU** → Limited by `predict_concurrency`.
3. **Postprocessing begins** → Can run while other requests are still in inference.

## When to Use Predict Concurrency

* ✅ **Protect GPU resources** – Prevent multiple requests from degrading performance.
* ✅ **Allow parallel preprocessing/postprocessing** – I/O tasks can continue even when inference is blocked.

<Warning>Ensure `Concurrency Target` is set high enough to send enough requests to the container.</Warning>

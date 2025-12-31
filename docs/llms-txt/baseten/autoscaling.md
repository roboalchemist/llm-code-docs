# Source: https://docs.baseten.co/deployment/autoscaling.md

# Autoscaling

> Autoscaling dynamically adjusts the number of active replicas to **handle variable traffic** while minimizing idle compute costs.

<img noZoom src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-autoscaling.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=f867eb7ccef178bae2fd11117365bebb" data-og-width="964" width="964" data-og-height="552" height="552" data-path="images/deployment-autoscaling.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-autoscaling.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=b88950b4dd0eb765a37d74991ce29062 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-autoscaling.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=f0b5d2412ebf1a9117c165f9b5711f18 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-autoscaling.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=5eb7a1b115bd723b732d5889382742df 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-autoscaling.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=74fb3e685e86eddade1e04ef92b9e424 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-autoscaling.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=b9c25eb323072c47121cde1c20c12a44 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-autoscaling.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=61671a961d7da633fb3a95ab4becd92c 2500w" />

## Configuring autoscaling

Autoscaling settings are **per deployment** and are inherited when promoting a model to production unless overridden.

Configure autoscaling through:

* **UI** → Manage settings in your Baseten workspace.
* **API** → Use the **[autoscaling API](/reference/management-api/deployments/autoscaling)**.

### Replica Scaling

Each deployment scales within a configured range of replicas:

* **Minimum replicas** → The lowest number of active replicas.
  * Default: `0` (scale to zero).
  * Maximum value: Cannot exceed the **maximum replica count**.
* **Maximum replicas** → The upper limit of active replicas.
  * Default: `1`.
  * Max: `10` by default (contact support to increase).

When first deployed, the model starts with `1` replica (or the **minimum count**, if higher). As traffic increases, additional replicas **scale up** until the **maximum count** is reached. When traffic decreases, replicas **scale down** to match demand.

***

## Autoscaler settings

The **autoscaler logic** is controlled by three key parameters:

* **Autoscaling window** → Time window for traffic analysis before scaling up/down. Default: 60 seconds.
* **Scale down delay** → Time before an unused replica is removed. Default: 900 seconds (15 minutes).
* **Concurrency target** → Number of requests a replica should handle before scaling. Default: 1 request.
* **Target Utilization Percentage** → Target percentage of filled concurrency slots. Default: 70%.

A **short autoscaling window** with a **longer scale-down delay** is recommended for **fast upscaling** while maintaining capacity during temporary dips.

The **target utilization percentage** determines the amount of headroom available. A higher number means less headroom and more
usage on each replica, where a lower number means more headroom and buffer for traffic spikes.

***

## Autoscaling behavior

### Scaling Up

When the **average requests per active replica** exceed the **concurrency target** within the **autoscaling window**, more replicas are created until:

* The **concurrency target is met**, or
* The **maximum replica count** is reached.

Note here that the amount of headroom is determined by the **target utilization percentage**. For example, with a concurrency target of 10 requests and a
target utilization percentage of 70%, scaling will begin when the average requests per active replica exceeds 7.

### Scaling Down

When traffic drops below the **concurrency target**, excess replicas are flagged for removal. The **scale-down delay** ensures that replicas are not removed prematurely:

* If traffic **spikes again before the delay ends**, replicas remain active.
* If the **minimum replica count** is reached, no further scaling down occurs.

***

## Scale to zero

If you're just testing your model or anticipate light and inconsistent traffic, scale to zero can save you substantial amounts of money.

Scale to zero means that when a deployed model is not receiving traffic, it scales down to zero replicas. When the model is called, Baseten spins up a new instance to serve model requests.

To turn on scale to zero, just set a deployment's minimum replica count to zero. Scale to zero is enabled by default in the standard autoscaling config.

<Note>
  Models that have not received any traffic for more than **two weeks** will be
  automatically deactivated. These models will need to be activated manually
  before they can serve requests again. For **production deployments this threshold
  is two months**.
</Note>

***

## Cold starts

A **cold start** is the time required to **initialize a new replica** when scaling up. Cold starts impact:

* **Scaled-to-zero deployments** → The first request must wait for a new replica to start.
* **Scaling events** → When traffic spikes and a deployment requires more replicas.

### Cold Start Optimizations

**Network accelerator**

Baseten speeds up model loading from **Hugging Face, CloudFront, S3, and OpenAI** using parallelized **byte-range downloads**, reducing cold start delays.

**Cold start pods**

Baseten pre-warms specialized **cold start pods** to accelerate loading times. These pods appear in logs as `[Coldboost]`.

```md Example coldboost log line theme={"system"}
Oct 09 9:20:25pm [Coldboost] Completed model.load() execution in 12650 ms
```

**Model Image streaming and optimization**

To further reduce initialization latency, Baseten uses **image streaming** to optimize container startup.

1. **Initial non-optimized image:**
   When a model is first deployed, a standard image is built without optimization. During this stage, the runtime monitors which parts of the image are accessed during startup and inference.

2. **Call graph–based optimization:**
   Baseten analyzes the model’s call graph to identify which layers, weights, and binaries are actually needed during initialization. This information drives creation of an **optimized image**.

3. **Prefetch and lazy fetch:**
   The optimized image is split into two content groups:
   * **Prefetched content:** Frequently accessed layers and dependencies are loaded eagerly at container start.
   * **Lazy-fetched content:** Less critical data is fetched on demand, reducing initial I/O overhead.

4. **Streaming-enabled image pull:**
   Images optimized through this process are streamed into the node filesystem during startup, allowing the model to begin loading before the entire image is downloaded.
   Pulling an optimized image appears in logs as:

   ```md Example streaming image pull log line theme={"system"}
   Successfully pulled streaming-enabled image in 15.851s. Image size: 32 GB.
   ```

***

## Autoscaling for development deployments

Development deployments have **fixed autoscaling constraints** to optimize for **live reload workflows**:

* **Min replicas:** `0`
* **Max replicas:** `1`
* **Autoscaling window:** `60 seconds`
* **Scale down delay:** `900 seconds (15 min)`
* **Concurrency target:** `1 request`

To enable full autoscaling, **promote the deployment and environment** like production.

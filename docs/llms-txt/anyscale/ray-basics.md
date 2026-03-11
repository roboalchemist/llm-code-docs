# Source: https://docs.anyscale.com/get-started/ray-basics.md

# Ray basics

[View Markdown](/get-started/ray-basics.md)

# Ray basics

Ray is a unified open-source framework that abstracts the complexity of distributed computing, providing a universal compute layer to scale production data processing and AI workloads. It orchestrates your compute cluster, schedules processes, provides fault tolerance, auto-scales nodes, and provides observability tools through a lightweight interface.

## Use Ray to parallelize a Python loop[​](#parallelize "Direct link to Use Ray to parallelize a Python loop")

This example demonstrates how you can use Ray for parallel computing in your applications.

The provided example is a simple Python `for` loop that iterates through a list and prints values with a sleep duration controlled by the index of the item. This example emulates Python serial processing from a database, where many calls happen in serial with variable response times.

A common way to demonstrate the power of Ray is to run an example on your laptop. To see Ray parallelization in action, run the provided code without Ray and review the results. Then use the provided Ray code to parallelize the function and run it again to see the difference in performance.

### Serial function (without Ray)[​](#serial "Direct link to Serial function (without Ray)")

Consider the following code that runs one task at a time. If the item with index 5 takes half a second (5/10.), an estimate of the total runtime to retrieve all eight items sequentially is (0+1+2+3+4+5+6+7)/10. = 2.8 seconds. Run the following code to get the actual time:

```
import time

database = ["Learning", "Ray", "Flexible", "Distributed", "Python", "for", "Machine", "Learning"]

def retrieve(item):    
    time.sleep(item / 10.)
    return item, database[item]

def print_runtime(input_data, start_time):
    print(f'Runtime: {time.time() - start_time:.2f} seconds, data:')
    print(*input_data, sep="\n")


start = time.time()
data = [retrieve(item) for item in range(8)]
print_runtime(data, start)
```

Serial execution results in:

* Sample runtime on a typical laptop: 2.83 s.
* All tasks executed sequentially, one after another.
* Total time = sum of all individual task times.

You can explore the dashboard information such as the number of CPU cores available and the total utilization of your current Ray application.

To see the resource utilization of your Ray cluster within a Python script, use the `ray.cluster_resources()` function. A typical laptop output is as follows:

```
{'CPU': 10.0,
 'node:127.0.0.1': 1.0,
 'node:__internal_head__': 1.0,
 'memory': 37722439680.0,
 'object_store_memory': 2147483648.0}
```

### Parallel task with Ray[​](#parallel "Direct link to Parallel task with Ray")

With Ray, you can parallelize a function by:

1. Adding `@ray.remote` decorator to your function.
2. Calling the function with `.remote()` instead of direct calls.
3. Using `ray.get()` to retrieve results.

You can run the same function in parallel by wrapping it in a `@ray.remote` decorator without modifying the original function. Ray doesn’t disrupt your natural programming style.

Ray converts functions decorated with `@ray.remote` into stateless *tasks* that it can schedule on any worker node in the cluster to enable parallel execution of functions across a distributed system.

You can extend this example to run on multiple nodes. Start by adding the following function to retrieve items using the `@ray.remote` decorator.

```
import ray 

@ray.remote
def retrieve_task(item):
    return retrieve(item)
```

With the decorator, the function `retrieve_task` becomes a Ray task. Ray executes the task on a different process than it was called from, potentially on a different machine.

The items in the `object_references` list in the code snippet don’t directly contain the results. If you check the Python type of the first item using `type(object_references[0])`, you see that it’s an ObjectRef. These object references correspond to *futures* for which you need to request the result. The `ray.get()` call is for requesting the result.

```
start = time.time()
object_references = [
    retrieve_task.remote(item) for item in range(8)
]
data = ray.get(object_references)
print_runtime(data, start)
```

Parallel execution results in:

* Runtime: 0.7 s.
* All tasks executed simultaneously across multiple CPU cores.
* Performance Improvement: 3x.

Ray extends the task abstraction for functions, by introducing actors for classes to enable stateful computation. To maximize performance and utilization across the cluster you can set resource requirements like CPUs and GPUs per task or actor. To run tasks and actors on remote machines, Ray manages dependencies with runtime environments, which it installs on every machine in the cluster.

## Key concepts[​](#key-concepts "Direct link to Key concepts")

These foundational abstractions simplify distributed computing with Ray:

* [**Task**](https://docs.ray.io/en/latest/ray-core/tasks.html): Invocation of an arbitrary function that you wrap with the `@ray.remote` decorator. Ray executes this remote function asynchronously, enabling parallel execution, on a separate worker process. Tasks support fine-grained and fractional CPU and GPU resource requirements to maximize resource utilization.
* [**Actor**](https://docs.ray.io/en/latest/ray-core/actors.html): An actor is a stateful worker, an extension of the Ray API from functions (tasks) to classes. When you instantiate a new actor, Ray creates a new worker and schedules methods of the actor on that specific worker. The methods can access and mutate the state of that worker. Actors support fine-grained and fractional CPU and GPU resource requirements to maximize resource utilization.
* [**Object store**](https://docs.ray.io/en/latest/ray-core/key-concepts.html#objects): A distributed in-memory data store for storing Ray objects, which are application values.
* [**Object reference**](https://docs.ray.io/en/latest/ray-core/objects.html#objects): A pointer to an application value, which Ray can store anywhere in the cluster. Calling \`foo.remote()\` creates and returns ObjectRef, which is a *future*.
* [**Runtime environments**](https://docs.ray.io/en/latest/ray-core/handling-dependencies.html#runtime-environments): A collection of dependencies installed on each node of the cluster. These environment dependencies include Python packages, local files, and environment variables.
* [**Resources**](https://docs.ray.io/en/latest/ray-core/scheduling/resources.html#resources): Logical resources like CPUs and GPUs that you set as compute requirements for tasks and actors.

## Ray workload libraries[​](#ray-workload-libraries "Direct link to Ray workload libraries")

![Diagram showing Ray workload libraries](/img/get-started/map-of-ray.svg)

Ray libraries integrate with traditional ML libraries enabling you to run data processing and AI workloads on a unified platform:

* Batch inference and data processing: [Ray Data](/get-started/what-is-ray.md#ray-data) features a [streaming execution](https://docs.ray.io/en/latest/data/key-concepts.html#streaming-execution) to efficiently process large datasets and maintain high utilization across both CPU and GPU workloads for structured and unstructured data.
* Fine-tuning and training: [Ray Train](/get-started/what-is-ray.md#ray-train) sets up distributed training across popular frameworks like PyTorch and TensorFlow.
* Hyperparameter tuning: [Ray Tune](/get-started/what-is-ray.md#ray-tune) is a Python library for scalable experiment execution and hyperparameter tuning.
* Model serving: [Ray Serve](/get-started/what-is-ray.md#ray-serve) provides scalable and programmable serving for ML models and business logic. Deploy models from any framework with production-ready performance.
* Reinforcement learning: [Ray RLlib](/get-started/what-is-ray.md#ray-rllib) offers high scalability and unified APIs for a variety of industry and research applications.

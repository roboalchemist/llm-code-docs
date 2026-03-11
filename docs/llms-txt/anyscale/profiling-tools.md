# Source: https://docs.anyscale.com/monitoring/workload-debugging/profiling-tools.md

# Train dashboard profiling tools

[View Markdown](/monitoring/workload-debugging/profiling-tools.md)

# Train dashboard profiling tools

The Train dashboard integrates CPU and GPU profiling tools to help you identify performance bottlenecks in distributed training workloads. You can launch these profiling tools with a single click from the worker detail page.

## On-demand CPU profiling[​](#on-demand-cpu-profiling "Direct link to On-demand CPU profiling")

The Train dashboard allows you to take an on-demand CPU profile of a training run using [py-spy](https://github.com/benfred/py-spy), a sampling-based profiling tool that generates flame graphs and stack traces. Use CPU profiling to identify performance bottlenecks, such as slow data preprocessing, inefficient custom operators, or training code that's waiting on resources.

CPU profiling works by periodically sampling the training worker process to capture what code is executing. This sampling-based approach has minimal performance impact on your training job.

### Collect a CPU profile[​](#collect-a-cpu-profile "Direct link to Collect a CPU profile")

Complete the following steps to generate a CPU profile for your training worker:

1. Navigate to an active Train run page.
2. Click on a worker to view its detail page.
3. Click the **CPU Profiling** button.
4. Enter the profiling duration in the configuration window.
5. Wait for profiling to finish. The profiling result generates a flame graph showing where CPU time is being spent.

The flame graph visualizes the call stack. The width of each bar represents the amount of CPU time that function consumes. Wider bars indicate functions consuming more CPU time, helping you quickly identify optimization opportunities.

For more information about interpreting flame graphs and using py-spy, see the [py-spy documentation](https://github.com/benfred/py-spy).

## On-demand GPU profiling[​](#on-demand-gpu-profiling "Direct link to On-demand GPU profiling")

note

This feature requires Ray 2.47.0 or later. Use this feature to profile PyTorch training runs for PyTorch versions 2.0 or later.

The Train dashboard allows you to take an on-demand GPU profile of a PyTorch training run to generate a [trace](https://docs.pytorch.org/tutorials/recipes/recipes/profiler_recipe.html) that shows a timeline of CPU and GPU operations. Use this trace to diagnose training bottlenecks and gain a better understanding of the computation and communication operations that are happening under the hood.

The following is an example of a trace visualization generated from on-demand GPU profiling on Anyscale. This trace can help identify bottlenecks on both the CPU and GPU sides by showing a timeline of CPU operations and GPU kernels. The example trace shows a collective all-reduce operation which is part of the Distributed Data Parallel algorithm for distributed training.

![Example GPU trace](/assets/images/gputrace-5789fc674fd2cf583512d31403fd9ea0.png)

### Configure GPU profiling for Anyscale[​](#configure-gpu-profiling-for-anyscale "Direct link to Configure GPU profiling for Anyscale")

This feature relies on [Dynolog](https://github.com/facebookincubator/dynolog). Complete the following steps to set up dependencies:

1. Anyscale base images include Dynolog binaries for all Ray versions 2.47.0 or later. If you're building your own image and not extending an Anyscale base image, install the Dynolog binaries on your container image. See [the installation instructions on the Dynolog repo](https://github.com/facebookincubator/dynolog).
2. Set the `KINETO_USE_DAEMON` and `KINETO_DAEMON_INIT_DELAY_S` environment variables on the training workers. Here's how you can do this with Ray Train:

```
trainer = ray.train.torch.TorchTrainer(
    ...,
    run_config=ray.train.RunConfig(
        ...,
        worker_runtime_env={
            "env_vars": {"KINETO_USE_DAEMON": "1", "KINETO_DAEMON_INIT_DELAY_S": "5"}
        },
    )
)
```

### Collect a GPU profile[​](#collect-a-gpu-profile "Direct link to Collect a GPU profile")

Complete the following steps to generate a profile for your GPU training worker.

1. Navigate to an active Train run page.
2. Click on the `GPU Profiling` button on one of the workers.
3. Enter the profiling duration in the configuration window that appears.
4. Wait for profiling to finish. Anyscale downloads the profiling result as a JSON file that you can view in `chrome://tracing` on a Chrome browser or [Perfetto trace viewer](https://ui.perfetto.dev/).

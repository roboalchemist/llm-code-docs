# Source: https://docs.anyscale.com/tutorials/submit-a-job.md

# Get started with jobs

[View Markdown](/tutorials/submit-a-job.md)

# Get started with jobs

Run discrete workloads in production such as batch inference, bulk embeddings generation, or model fine-tuning.

***

Anyscale jobs allow you to submit applications developed on workspaces to a standalone Ray cluster for execution. Built for production and designed to fit into your CI/CD pipeline, jobs ensure scalable and reliable performance.

Run your first job with the following instructions.

## 1. Install the Anyscale CLI[​](#install "Direct link to 1. Install the Anyscale CLI")

```
pip install -U anyscale
anyscale login
```

## 2. Submit a job[​](#submit "Direct link to 2. Submit a job")

Clone the example from GitHub.

```
git clone https://github.com/anyscale/examples.git
cd examples/01_job_hello_world
```

The code in [main.py](https://github.com/anyscale/examples/blob/main/02_service_hello_world/main.py) runs 100 tasks that each take a number and square it.

```
import os
import ray


@ray.remote
def f(i):
    # This print statement is running in a separate worker process.
    print(f"The value of EXAMPLE_ENV_VAR is {os.environ['EXAMPLE_ENV_VAR']}.")
    return i ** 2


# Execute 100 tasks across the cluster.
results = ray.get([f.remote(i) for i in range(100)])
print(results)
```

Also take a look at `job.yaml`. This file specifies the container image, compute resources, script entrypoint, and a few other fields.

Submit the job:

```
anyscale job submit -f job.yaml
```

## 3. Inspect the results[​](#inspect "Direct link to 3. Inspect the results")

Navigate to the Anyscale [**Jobs** page](https://console.anyscale.com/v2/cld_kvedZWag2qA8i5BjxUevf5i7/prj_cz951f43jjdybtzkx1s5sjgz99/jobs) and take a look at the results.

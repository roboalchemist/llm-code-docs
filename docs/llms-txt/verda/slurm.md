# Source: https://docs.verda.com/clusters/instant-clusters/slurm.md

# Slurm

## Overview

Verda instant clusters have [Slurm](https://slurm.schedmd.com/documentation.html) job-scheduling system preinstalled. You can verify that Slurm is working by running a simple job that uses 16 GPUs. This will execute on at least two physical nodes, since each server has 8 GPUs:

```bash
srun --gpus=16 nvidia-smi
```

## Example Slurm job

### Pre-requisites

The following example utilizes [Spack](https://spack.readthedocs.io/en/latest/) package system. You can also check out our [simple Spack tutorial](https://docs.verda.com/clusters/instant-clusters/spack) and the [official Spack documentation](https://spack.readthedocs.io/en/latest/basic_usage.html) to learn more.

Spack is pre-installed into `/home/spack`.

To get spack commands available in your terminal run:

```bash
. /home/spack/spack/share/spack/setup-env.sh
```

You can see how we build Spack by looking inside this script: `/usr/local/bin/spack.setup.sh`

### Simple Slurm job

Below is an example of simple Slurm job that runs the `all_reduce_perf` from [nccl-tests](https://github.com/NVIDIA/nccl-tests) with 16 GPUs on two nodes.

The example job description is created by the Spack installation script and is placed here: `/home/ubuntu/all_reduce_example_slurm.job`:

```bash
#!/bin/bash
#SBATCH --job-name=all_reduce_perf
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=8
#SBATCH --gres=gpu:8
#SBATCH --cpus-per-task=22
#SBATCH --time=00:05:00

. /home/spack/spack/share/spack/setup-env.sh

spack load nccl-tests@2.16.7

srun --mpi=pmix all_reduce_perf -b 1M -e 1G -f 2 -g 1

```

You can execute the above job by running:

```bash
$ sbatch /home/ubuntu/all_reduce_example_slurm.job
```

Briefly, the above script does the following:

* Lines starting with `#SBATCH` define the requirements for the job
* Next, Spack is initialized, making `spack`command available
* `spack load nccl-tests@2.16.7` makes `all_reduce_perf` available in the `$PATH`
* `srun` executes the actual command.

To read what the job printed to `stdout`, look in the file `slurm-jobid.out` located in the same directory where you called the job from. You can run `squeue -a` to list all Slurm jobs and their status.

## Troubleshooting

Get the general state of worker nodes with the command `sinfo`

In an unlikely case that the Slurm does not see the worker nodes after the reboot, you can make them available again with:

```bash
scontrol update NodeName=cluster-name-1 State=RESUME
```

If a node becomes unhealthy (for example, a full `/` partition), it will enter the drained state. Check the reason with:

```bash
scontrol show node cluster-name-1
```

To troubleshoot Slurm distributed workloads it's crucial to capture logs from both the head node and the worker nodes.

### Logging

Use the following `#SBATCH` directives at the top of your Slurm script to capture logs produced by commands executed in the main script body (typically run on the head node):

```bash
#SBATCH --output=/path/to/logs/headnode/jobname_%j.out
#SBATCH --error=/path/to/logs/headnode/jobname_%j.err
```

* `--output` captures the `STDOUT` from the head node script body
* `--error` captures the `STDERR` from the head node script body
* `%j` is replaced with the Slurm job ID, keeping logs organized

To capture logs from each worker node, use the `--output` and `--error` flags inside the **`srun`** command:

```bash
srun \
  --output=/path/to/logs/workernodes/jobname_%j_node%N.out \
  --error=/path/to/logs/workernodes/jobname_%j_node%N.err \
  your_distributed_command
```

* `%j` - Slurm job id
* `%N` - node name (e.g., `node001`), ensuring per-node log separation.

These logs will capture:

* Logs from each task/rank running under `srun`
* Application-specific output (e.g. print statements, warnings, stack traces)
* Environment or setup errors during distributed execution

{% hint style="info" %}
It's recommended to differentiate head node logs from worker logs using directory structure or filenames (`headnode/` vs `workernodes/`), so you don't run into stale files and race conditions while writing to the logs.
{% endhint %}

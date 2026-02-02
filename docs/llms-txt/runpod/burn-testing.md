# Source: https://docs.runpod.io/hosting/burn-testing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.runpod.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Burn testing

Machines should be thoroughly tested before they are listed on the Runpod platform. Here is a simple guide to running a burn test for a few days.

Stop the Runpod agent by running:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark"}}
sudo systemctl stop runpod
```

Then you can kick off a gpu-burn run by typing:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark"}}
docker run --gpus all --rm jorghi21/gpu-burn-test 172800
```

You should also verify that your memory, CPU, and disk are up to the task. You can use the [ngstress library](https://wiki.ubuntu.com/Kernel/Reference/stress-ngstress) to accomplish this.

When everything is verified okay, start the Runpod agent again by running

```bash  theme={"theme":{"light":"github-light","dark":"github-dark"}}
sudo systemctl start runpod
```

Then, on your [machine dashboard](https://www.console.runpod.io/host/machines), self rent your machine to ensure it's working well with most popular templates.

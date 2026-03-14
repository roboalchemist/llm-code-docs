# Source: https://docs.mage.ai/guides/train/complete-project.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Use a completed pipeline

## 1. Clone project

In your terminal, clone this [repository](https://github.com/mage-ai/demo_project)
by running the following command:

```bash  theme={"system"}
git clone https://github.com/mage-ai/demo_project.git
```

## 2. Start the tool

<b>Docker</b>

```bash  theme={"system"}
./scripts/start.sh demo_project
```

<b>pip</b>

```bash  theme={"system"}
mage start demo_project
```

Open [http://localhost:6789](http://localhost:6789) in your browser.

On the left side in the file browser underneath the folder `demo_project/pipelines`,
click the pipeline named `titanic_survivors`.

## 3. Follow the quick start tutorial

Go back to the [quick start tutorial](/guides/train-model),
start from step <b>3. Play around with scratchpad</b>,
and use the existing code to follow along.


Built with [Mintlify](https://mintlify.com).
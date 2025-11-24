# Source: https://docs.crewai.com/en/enterprise/features/traces.md

# Traces

> Using Traces to monitor your Crews

## Overview

Traces provide comprehensive visibility into your crew executions, helping you monitor performance, debug issues, and optimize your AI agent workflows.

## What are Traces?

Traces in CrewAI AMP are detailed execution records that capture every aspect of your crew's operation, from initial inputs to final outputs. They record:

* Agent thoughts and reasoning
* Task execution details
* Tool usage and outputs
* Token consumption metrics
* Execution times
* Cost estimates

<Frame>
    <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=9c02d5b7306bf7adaeadd77a018f8fea" alt="Traces Overview" data-og-width="2244" width="2244" data-og-height="1422" height="1422" data-path="images/enterprise/traces-overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=e66e7c56a8848b69266563ea8cddfc4e 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f590b3901aaa5994042c79426d78bd6c 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=0ecb9dcb307e8f130f53393bd3abc12d 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5fc6fcfc51c4e8f4ce16d237228043d6 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=253eaed4ec34a35798dad42e9a388859 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=ec818e09bc20b3f72b1bcf1970804d13 2500w" />
</Frame>

## Accessing Traces

<Steps>
  <Step title="Navigate to the Traces Tab">
    Once in your CrewAI AMP dashboard, click on the **Traces** to view all execution records.
  </Step>

  <Step title="Select an Execution">
    You'll see a list of all crew executions, sorted by date. Click on any execution to view its detailed trace.
  </Step>
</Steps>

## Understanding the Trace Interface

The trace interface is divided into several sections, each providing different insights into your crew's execution:

### 1. Execution Summary

The top section displays high-level metrics about the execution:

* **Total Tokens**: Number of tokens consumed across all tasks
* **Prompt Tokens**: Tokens used in prompts to the LLM
* **Completion Tokens**: Tokens generated in LLM responses
* **Requests**: Number of API calls made
* **Execution Time**: Total duration of the crew run
* **Estimated Cost**: Approximate cost based on token usage

<Frame>
    <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-summary.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=a6a26eda2add26a6f649b1727bf90d8d" alt="Execution Summary" data-og-width="2576" width="2576" data-og-height="916" height="916" data-path="images/enterprise/trace-summary.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-summary.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=52f47a0c5d9f2dc1d0c93d1c2446cb10 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-summary.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=584cdc9fded1e3875799da73e60cdebd 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-summary.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=2e4f500438545badfa9b3bb3704786ce 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-summary.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c3e0987a95638f9512ba6c64a5927eda 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-summary.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d80e2d9de9db7449368151ccaac8106b 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-summary.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=39ccb1a6b12aecd0f6863f2783b1bfc6 2500w" />
</Frame>

### 2. Tasks & Agents

This section shows all tasks and agents that were part of the crew execution:

* Task name and agent assignment
* Agents and LLMs used for each task
* Status (completed/failed)
* Individual execution time of the task

<Frame>
    <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-tasks.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f0358b4a17e78532500b4a14964bc30c" alt="Task List" data-og-width="1778" width="1778" data-og-height="594" height="594" data-path="images/enterprise/trace-tasks.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-tasks.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=a775268b18c71e0ffa497c9a4e1ad179 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-tasks.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=3dadaad60870c3841f859857d5d6f53d 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-tasks.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=a0a1d24573dd32cb9d5a3f089536c547 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-tasks.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=2ccc370f5e0b6b38521a5ed39e02b062 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-tasks.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=4d717a70fd61ce713f7d5d91ccf867fe 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-tasks.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=2c577a5f8e1acea3942de29c5ca49343 2500w" />
</Frame>

### 3. Final Output

Displays the final result produced by the crew after all tasks are completed.

<Frame>
    <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/final-output.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5ca9ef8e4071ee570c3e0c8f93ff4253" alt="Final Output" data-og-width="2212" width="2212" data-og-height="1572" height="1572" data-path="images/enterprise/final-output.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/final-output.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=ab97b6b386304f03fe21c6ba2393c683 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/final-output.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=3839e312b2a9caa45f3f4b72345ea87b 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/final-output.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b032c2c57ffcd5fb558c43915d385f9a 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/final-output.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=63390d70d70f1a2265a224e8c20d0204 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/final-output.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=abc4a7b81c51049ca606130a0dd543f7 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/final-output.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=9fc40fc5f8ad52996aba482d62348f0f 2500w" />
</Frame>

### 4. Execution Timeline

A visual representation of when each task started and ended, helping you identify bottlenecks or parallel execution patterns.

<Frame>
    <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-timeline.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c860975d3e15e3a6988bedc7d1bf6ba4" alt="Execution Timeline" data-og-width="2210" width="2210" data-og-height="1406" height="1406" data-path="images/enterprise/trace-timeline.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-timeline.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b74d67bda34ce88ea23c30c580dfb2fc 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-timeline.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=99c6688c1d290548cc480232bb13b0e0 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-timeline.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=4876c794ddde894e1e2cf15f1926efcb 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-timeline.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c44f7eec8f0998e488bc951eee8961ea 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-timeline.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c25e4827f5a83172483c38f40e6685de 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-timeline.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b3b2f72954e565f7177b5175d89dfe79 2500w" />
</Frame>

### 5. Detailed Task View

When you click on a specific task in the timeline or task list, you'll see:

<Frame>
    <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-detailed-task.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=74f5e92354196325edca8d62c29363c7" alt="Detailed Task View" data-og-width="2036" width="2036" data-og-height="1572" height="1572" data-path="images/enterprise/trace-detailed-task.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-detailed-task.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d260407501639bcd1a45da51762f488e 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-detailed-task.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=e577e06eb7658f045e56f2e40e03cf94 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-detailed-task.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=fcafbac3507eb800e08153352016bf14 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-detailed-task.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=9b2b0decb758802aaa2d8b0b2bd39e6f 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-detailed-task.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=66a9362f6d8f2edd5a2dad353700e440 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-detailed-task.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=faadd7f3c9e9176060e21c2987c3d8c9 2500w" />
</Frame>

* **Task Key**: Unique identifier for the task
* **Task ID**: Technical identifier in the system
* **Status**: Current state (completed/running/failed)
* **Agent**: Which agent performed the task
* **LLM**: Language model used for this task
* **Start/End Time**: When the task began and completed
* **Execution Time**: Duration of this specific task
* **Task Description**: What the agent was instructed to do
* **Expected Output**: What output format was requested
* **Input**: Any input provided to this task from previous tasks
* **Output**: The actual result produced by the agent

## Using Traces for Debugging

Traces are invaluable for troubleshooting issues with your crews:

<Steps>
  <Step title="Identify Failure Points">
    When a crew execution doesn't produce the expected results, examine the trace to find where things went wrong. Look for:

    * Failed tasks
    * Unexpected agent decisions
    * Tool usage errors
    * Misinterpreted instructions

    <Frame>
            <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/failure.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c892a75b7a22a57949a2641a0fe45bfa" alt="Failure Points" data-og-width="820" width="820" data-og-height="924" height="924" data-path="images/enterprise/failure.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/failure.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=ecbcbd312dd467cb5cc1dae4a443c56d 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/failure.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c0452a9db1f339e63686941a533d8946 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/failure.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=ded3f2fff055c8d16bcad99ad537da46 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/failure.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f871feb85f88ba397a259ee8392aef3e 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/failure.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=2acf042b2e6b185f1fbc41100751e03f 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/failure.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=1e9fc9104e6b55b586a9b13e120de908 2500w" />
    </Frame>
  </Step>

  <Step title="Optimize Performance">
    Use execution metrics to identify performance bottlenecks:

    * Tasks that took longer than expected
    * Excessive token usage
    * Redundant tool operations
    * Unnecessary API calls
  </Step>

  <Step title="Improve Cost Efficiency">
    Analyze token usage and cost estimates to optimize your crew's efficiency:

    * Consider using smaller models for simpler tasks
    * Refine prompts to be more concise
    * Cache frequently accessed information
    * Structure tasks to minimize redundant operations
  </Step>
</Steps>

## Performance and batching

CrewAI batches trace uploads to reduce overhead on high-volume runs:

* A TraceBatchManager buffers events and sends them in batches via the Plus API client
* Reduces network chatter and improves reliability on flaky connections
* Automatically enabled in the default trace listener; no configuration needed

This yields more stable tracing under load while preserving detailed task/agent telemetry.

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with trace analysis or any other CrewAI AMP features.
</Card>

# Execution Model

Luigi has a quite simple model for execution and triggering.

## Workers and task execution

The most important aspect is that *no execution is transferred*.
When you run a Luigi workflow,
the worker schedules all tasks, and
also executes the tasks within the process.
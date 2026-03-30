# Source: https://docs.snowflake.com/en/release-notes/2026/other/2026-01-26-dynamic-task-config.md

# Jan 26, 2026: Specify a dynamic task configuration with EXECUTE TASK

You can now dynamically override a task configuration for a single execution with the
EXECUTE TASK command. Use the `USING CONFIG` clause to run ad-hoc executions
without changing the task definition.

For more information, see [EXECUTE TASK](../../../sql-reference/sql/execute-task.md).

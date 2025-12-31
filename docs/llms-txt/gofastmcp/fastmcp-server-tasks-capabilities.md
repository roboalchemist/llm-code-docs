# Source: https://gofastmcp.com/python-sdk/fastmcp-server-tasks-capabilities.md

# capabilities

# `fastmcp.server.tasks.capabilities`

SEP-1686 task capabilities declaration.

## Functions

### `get_task_capabilities` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/server/tasks/capabilities.py#L6" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={"theme":{"light":"snazzy-light","dark":"dark-plus"}}
get_task_capabilities() -> dict[str, Any]
```

Return the SEP-1686 task capabilities structure.

This is the standard capabilities map advertised to clients,
declaring support for list, cancel, and request operations.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://gofastmcp.com/llms.txt
# Source: https://rolldown.rs/reference/Variable.getLogFilter.md

---
url: /reference/Variable.getLogFilter.md
---
# Variable: getLogFilter

* **Exported from**: `rolldown/getLogFilter`
* **Type**: [`GetLogFilter`](TypeAlias.GetLogFilter.md)

A helper function to generate log filters using the same syntax as the CLI.

## Example

```ts
import { defineConfig } from 'rolldown';
import { getLogFilter } from 'rolldown/getLogFilter';

const logFilter = getLogFilter(['code:FOO', 'code:BAR']);

export default defineConfig({
	input: 'main.js',
	onLog(level, log, handler) {
		if (logFilter(log)) {
			handler(level, log);
		}
	}
});
```

# Source: https://rolldown.rs/reference/TypeAlias.RolldownWatcherWatcherEventMap.md

---
url: /reference/TypeAlias.RolldownWatcherWatcherEventMap.md
---
# Type Alias: RolldownWatcherWatcherEventMap

* **Type**: { `change`: \[`string`, { `event`: `ChangeEvent`; }]; `close`: \[]; `event`: \[[`RolldownWatcherEvent`](TypeAlias.RolldownWatcherEvent.md)]; `restart`: \[]; }

## Properties

### change

* **Type**: \[`string`, { `event`: `ChangeEvent`; }]

a file was modified

***

### close

* **Type**: \[]

the watcher was closed

***

### event

* **Type**: \[[`RolldownWatcherEvent`](TypeAlias.RolldownWatcherEvent.md)]

***

### restart

* **Type**: \[]

a new run was triggered

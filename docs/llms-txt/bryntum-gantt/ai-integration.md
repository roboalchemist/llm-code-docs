# Source: https://bryntum.com/products/gantt/docs-llm/guide/Gantt/advanced/ai-integration.md

# AI integration

<div class="note">

The AI feature and all its related components are marked as <strong>experimental</strong> and are subject to change.

</div>

The Gantt chart ships with an AI feature that lets users interact with project data using natural language through a
chat panel. Users can filter tasks, update schedules, toggle critical paths, and more — all using conversational
commands.

The Gantt AI feature builds on top of the Scheduler AI feature. Please read both of these guides first:

* [Grid AI integration guide](#Grid/guides/advanced/ai-integration.md) — covers setup, backend configuration, API
plugins, custom tools, voice features, user settings, and more
* [Scheduler AI integration guide](#Scheduler/guides/advanced/ai-integration.md) — covers event tools and the
`defaultRange` config

All configurations described in those guides apply to the Gantt as well.

## Minimum configuration

```javascript
import { Gantt, OpenAIPlugin } from '@bryntum/gantt';

const gantt = new Gantt({
    features : {
        ai : {
            promptUrl  : '/api/ai/prompt',
            apiPlugin  : OpenAIPlugin,
            model      : 'gpt-4-1',
            chatButton : true
        }
    }
});
```

## Default date range

Like the Scheduler, the Gantt has a `defaultRange` config. For Gantt, it defaults to `'all'`:

```javascript
features : {
    ai : {
        defaultRange : 'all'  // 'timeline' | 'in-view' | 'all'
    }
}
```

## Additional tools

In addition to the [Grid tools](#Grid/guides/advanced/ai-integration.md) and
[Scheduler tools](#Scheduler/guides/advanced/ai-integration.md), the Gantt adds project-specific tools:

| Tool | Description |
|------|-------------|
| `getChildren` | Retrieves child tasks for a parent task |
| `criticalPath` | Enables/disables the [CriticalPaths](#Gantt/feature/CriticalPaths) feature |
| `tableSections` | Changes visible table columns |

## API docs

* [Gantt AI feature](#Gantt/feature/AI)
* [Scheduler AI feature](#Scheduler/feature/AI)
* [Grid AI feature](#Grid/feature/AI)
* [AIBase (base class)](#Core/feature/ai/AIBase)

## Demo

* [AI Gantt](https://bryntum.com/products/gantt/examples/ai-gantt/) — Gantt chart with AI assistant

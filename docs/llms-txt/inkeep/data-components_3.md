# Source: https://docs.inkeep.com/visual-builder/structured-outputs/data-components

# Data Components in Visual Builder (/visual-builder/structured-outputs/data-components)

Create and manage data components for rich, interactive agent messages using the Visual Builder.



<>
  ## What are Data Components?

  Data Components allow your agents to return rich, interactive content instead of just text. Think of them as reusable UI building blocks that your agent can populate with data.

  For example, instead of returning "You have 3 tasks: Task #123 (shipped), Task #124 (processing)...", your agent can return a properly formatted task list component.
</>

<>
  ## Model Recommendations

  <Warning>
    **Data components require high-capability models for best results.**

    Configure the structured output model in your agent settings with one of these recommended models:

    | Provider      | Recommended Models                   |
    | ------------- | ------------------------------------ |
    | **Anthropic** | `claude-sonnet-4+`, `claude-opus-4+` |
    | **OpenAI**    | `gpt-4.1`, `gpt-5.1`, `gpt-5.2`      |
    | **Google**    | `gemini-3.0-pro`                     |

    **Not recommended:** Lower-tier models (`gpt-4.1-mini`, `gpt-4.1-nano`, `gemini-2.5-flash`, `gemini-2.5-flash-lite`), or custom models.

    Data components use structured output generation, which requires frontier-level reasoning capabilities.
  </Warning>
</>

## How to create a data component

1. Go to the Data Components tab in the left sidebar. Then select "New data component".
2. Add in an id, name, and description. These are required fields.
3. Enter a JSON schema defining the structure of your data component.
4. Click "Submit".

To visually add the data component to the Agent, see the [Sub Agents](/visual-builder/sub-agents#adding-data-components) page for details.

### Example JSON Schema

```json
{
  "type": "object",
  "properties": {
    "tasks": {
      "type": "array",
      "description": "Array of user tasks",
      "items": {
        "type": "object",
        "properties": {
          "id": { "type": "string", "description": "Task ID" },
          "title": { "type": "string", "description": "Task title" },
          "completed": { "type": "boolean", "description": "Task status" }
        }
      }
    },
    "totalCount": { "type": "number", "description": "Total tasks" }
  }
}
```

## Frontend Integration

Create a React component that receives the props defined by your data component schema:

```tsx
const TaskList = ({ tasks, totalCount }) => (
  <div className="task-list">
    <h3>Your Tasks ({totalCount} total)</h3>
    {tasks.map((task) => (
      <div key={task.id} className={task.completed ? "completed" : ""}>
        {task.title}
      </div>
    ))}
  </div>
);
```

If you have generated component UI (render code) for this data component in the dashboard, you can add the component file to your app instead via the CLI:

```bash
inkeep add --ui <component-id>
```

The CLI writes the component to `apps/agents-ui/src/ui` (or your project’s equivalent).

Register the component with the chat widget. The **key** in `components` must be the component name as shown in the dashboard (exact string), and the **value** is your imported React component:

```tsx
import { TaskList } from './ui/TaskList';

<InkeepSidebarChat
  aiChatSettings={{
    agentUrl: "your-agent-url",
    components: {
      "Task List": TaskList, // Key = dashboard component name; value = your component
    },
  }}
/>
```

The agent will automatically return structured data that renders as your React component.

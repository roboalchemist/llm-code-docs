# Source: https://docs.augmentcode.com/cli/interactive/task-management.md

# Using Task Manager

> Use /task to break down complex problems into manageable steps.

export const Command = ({text}) => <span className="font-bold">{text}</span>;

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

## About the Task Manager

The Auggie CLI task manager allows you to break down complex problems into discrete, manageable actions and track your progress through each step. It's particularly useful for automation workflows and keeping the agent focused on multi-step tasks.

The task manager maintains state per session and stores tasks under `~/.augment` for persistence across CLI sessions.

## Activating the Task Manager

Start Auggie in interactive mode and use the `/task` slash command:

```bash  theme={null}
# Start Auggie in interactive mode
auggie

# Then type the slash command
/task
```

This opens the task manager interface, which takes over the main panel and provides a focused environment for task management.

### Alternative Access

You can also ask the agent to create a task list for you:

```bash  theme={null}
auggie "Start a task list to implement user authentication"
```

The agent will automatically create and populate a task list when it encounters complex, multi-step problems.

## Task Manager Interface

The task manager provides a scrollable interface with comprehensive theming and visual feedback. When active, it replaces the main chat interface to provide a focused task management experience.

### Navigation and Interaction

Use your keyboard to interact with the Task Manager:

| Key        | Action                                                                                     |
| :--------- | :----------------------------------------------------------------------------------------- |
| `↑` / `↓`  | Navigate between tasks. The active task is highlighted with • next to the \[ ] Task Title. |
| `J` / `K`  | Alternative vim-style navigation (up/down)                                                 |
| `A`        | Add a new task                                                                             |
| `E`        | Edit the active task's title and description                                               |
| `D`        | Delete the active task                                                                     |
| `Spacebar` | Toggle task status                                                                         |
| `Esc`      | Dismiss the Task Manager                                                                   |

## Task Status Indicators

Tasks have three distinct states with corresponding visual status indicators:

* **\[ ] Not Started** - Empty checkbox, task has not been started
* **\[✓] Done** - Checkmark, task has been completed
* **\[-] Cancelled** - Dash, task has been cancelled or is no longer needed

## Working with Tasks

### Creating Tasks

**Manual Creation:**

1. Press `A` to add a new task
2. Enter the task title when prompted
3. Optionally add a description for more detailed context

**Agent-Generated Tasks:**
The agent automatically creates tasks inside the Task Manager when it encounters complex problems. You can also explicitly request task creation:

```bash  theme={null}
"Create a task list to refactor the authentication system"
```

### Editing Tasks

1. Navigate to the desired task using arrow keys or J/K
2. Press `E` to edit
3. Modify the title first, then the description
4. The task manager provides inline editing with clear visual feedback

### Task Execution

**Manual Execution:**

* Use the task list as a checklist, manually updating status as you complete work
* Toggle status with `Spacebar` to track progress

**Agent Execution:**
You can ask the agent to work on specific tasks from the task manager:

```bash  theme={null}
"Work on the first incomplete task in my task list"
"Complete the database migration task"
```

The agent will access your task list and update task status as it works.

## Advanced Features

### Task Hierarchy and Subtasks

The task manager supports nested task structures:

* Main tasks can have subtasks for complex workflows
* Subtasks are automatically indented and organized hierarchically
* Navigate through nested structures using standard navigation keys

### Persistence and Sessions

* Tasks are automatically saved per session under `~/.augment`
* Task lists persist across CLI restarts within the same session
* Each conversation session maintains its own task list

### Integration with Agent Workflow

The task manager is designed to work seamlessly with agent automation:

* **Keeps agents focused**: Provides clear structure for multi-step workflows
* **Progress tracking**: Agent can update task status as it completes work
* **Context preservation**: Tasks maintain context across long conversations
* **Automation-friendly**: Particularly useful for non-interactive automation workflows

## Use Cases and Examples

### Development Workflow

```bash  theme={null}
auggie "Create a task list to implement user registration feature"
# Agent creates tasks like:
# [ ] Design user registration API endpoints
# [ ] Create user model and database schema
# [ ] Implement registration validation
# [ ] Add password hashing and security
# [ ] Write unit tests for registration
# [ ] Update API documentation
```

### Code Refactoring

```bash  theme={null}
auggie "Break down refactoring the payment system into tasks"
# Agent creates structured tasks for complex refactoring
```

### Bug Investigation

```bash  theme={null}
auggie "Create tasks to investigate and fix the login timeout issue"
# Agent creates systematic debugging tasks
```

## Tips for Effective Task Management

1. **Be Specific**: Create clear, actionable task descriptions
2. **Break Down Complex Work**: Use subtasks for multi-step processes
3. **Regular Updates**: Keep task status current for accurate progress tracking
4. **Agent Collaboration**: Let the agent help create and organize task structures
5. **Session Organization**: Use task lists to maintain focus across long sessions

## Troubleshooting

**Task Manager Won't Open:**

* Ensure you're in interactive mode (`auggie` without `-p` flag)
* Try typing `/task` exactly as shown
* Check that you're not in the middle of another operation

**Tasks Not Persisting:**

* Tasks are saved per session - starting a new session creates a new task list
* Check that `~/.augment` directory has proper write permissions

**Navigation Issues:**

* Use either arrow keys (↑/↓) or vim keys (J/K) for navigation
* Ensure the task manager has focus (not in edit mode)

## Related Features

* [Prompt Enhancer](/cli/interactive/prompt-enhancer) - Enhance task descriptions with context
* [Keyboard Shortcuts](/cli/interactive#shortcuts) - Learn other useful CLI shortcuts
* [Slash Commands](/cli/interactive#slash-commands) - Discover other interactive commands

# Source: https://docs.livekit.io/agents/logic/tasks.md

# Source: https://docs.livekit.io/agents/build/tasks.md

LiveKit docs › Building voice agents › Tasks & task groups

---

# Tasks and task groups

> Use tasks to build complex workflows for your voice AI agents.

Available in:
- [ ] Node.js
- [x] Python

## Overview

Tasks are focused, reusable units that perform a specific objective and return a typed result. They run inside an agent and take control of the session only until their goal is achieved. A task can define its own [tools](https://docs.livekit.io/agents/build/tools.md) and starts executing when it's created within the context of an agent.

For multi-step flows, the framework provides `TaskGroup`. A task group executes an ordered sequence of tasks while allowing users to return to earlier steps for corrections. All tasks in a group share conversation context, and when the group finishes, a summarized result is returned to the agent that started it.

Tasks and task groups are core building blocks for complex voice AI [workflows](https://docs.livekit.io/agents/build/workflows.md). Common use cases for tasks include:

- Obtaining recording consent at the start of a call.
- Collecting structured information such as an address or payment details.
- Walking through a series of questions one step at a time.
- Any discrete action that should complete and yield control.
- Any multi-step process that can be decomposed into ordered tasks.

## Defining a task

Define a task by extending the `AgentTask` class and specifying a result type using [generics](https://typing.python.org/en/latest/reference/generics.html). Use the `on_enter` method to begin the task's interaction with the user, and call the `complete` method with a result when complete. The task has full support for tools, similar to an agent.

```python
from livekit.agents import AgentTask, function_tool

class CollectConsent(AgentTask[bool]):
    def __init__(self, chat_ctx=None):
        super().__init__(
            instructions="""
            Ask for recording consent and get a clear yes or no answer.
            Be polite and professional.
            """,
            chat_ctx=chat_ctx,
        )

    async def on_enter(self) -> None:
        await self.session.generate_reply(
            instructions="""
            Briefly introduce yourself, then ask for permission to record the call for quality assurance and training purposes.
            Make it clear that they can decline.
            """
        )

    @function_tool
    async def consent_given(self) -> None:
        """Use this when the user gives consent to record."""
        self.complete(True)

    @function_tool
    async def consent_denied(self) -> None:
        """Use this when the user denies consent to record."""
        self.complete(False)

```

### Running a task

A task must be created within the context of an [active](https://docs.livekit.io/agents/build/agents-handoffs.md#active-agent) `Agent`, and runs automatically when it's created. The task takes control of the session until it returns a result. Await the task to receive its result.

```python
from livekit.agents import Agent, function_tool, get_job_context

class CustomerServiceAgent(Agent):
    def __init__(self):
        super().__init__(instructions="You are a friendly customer service representative.")

    async def on_enter(self) -> None:
        if await CollectConsent(chat_ctx=self.chat_ctx):
            await self.session.generate_reply(instructions="Offer your assistance to the user.")
        else:
            await self.session.generate_reply(instructions="Inform the user that you are unable to proceed and will end the call.")
            job_ctx = get_job_context()
            await job_ctx.api.room.delete_room(api.DeleteRoomRequest(room=job_ctx.room.name))

```

### Task results

Use any result type you want. For complex results, use a custom dataclass.

```python
from dataclasses import dataclass

@dataclass
class ContactInfoResult:
    name: str
    email_address: str
    phone_number: str

class GetContactInfoTask(AgentTask[ContactInfoResult]):
    # ....

```

### Unordered collection within tasks

You can use a single task to collect multiple pieces of information in any order. The following example collects strengths, weaknesses, and work style in a hypothetical interview. Candidates can answer the questions in any order:

```python
@dataclass
class BehavioralResults:
    strengths: str
    weaknesses: str
    work_style: str

class BehavioralTask(AgentTask[BehavioralResults]):
    def __init__(self) -> None:
        super().__init__(
            instructions="Collect strengths, weaknesses, and work style in any order."
        )
        self._results = {}
    
    @function_tool()
    async def record_strengths(self, strengths_summary: str):
        """Record candidate's strengths"""
        self._results["strengths"] = strengths_summary
        self._check_completion()
    
    @function_tool()
    async def record_weaknesses(self, weaknesses_summary: str):
        """Record candidate's weaknesses"""
        self._results["weaknesses"] = weaknesses_summary
        self._check_completion()
    
    @function_tool()
    async def record_work_style(self, work_style: str):
        """Record candidate's work style"""
        self._results["work_style"] = work_style
        self._check_completion()
    
    def _check_completion(self):
        required_keys = {"strengths", "weaknesses", "work_style"}
        if self._results.keys() == required_keys:
            results = BehavioralResults(
                strengths=self._results["strengths"],
                weaknesses=self._results["weaknesses"],
                work_style=self._results["work_style"]
            )
            self.complete(results)
        else:
            self.session.generate_reply(
                instructions="Continue collecting remaining information."
            )

```

## Prebuilt tasks

Available in (BETA):
- [ ] Node.js
- [x] Python

The framework includes prebuilt tasks for common use cases within the module [livekit.agents.beta.workflows](https://docs.livekit.io/reference/python/v1/livekit/agents/beta/workflows/index.html.md). These include the following tasks:

- [GetEmailTask](#getemailtask)
- [GetAddressTask](#getaddresstask)
- [GetDtmfTask](#getdtmftask)

### Customizing prebuilt tasks

You can customize the behavior of prebuilt tasks by passing in extra instructions for the LLM. Use the `extra_instructions` parameter when you create the task. For an example, see the [Customize GetEmailTask](#customize-getemailtask) section.

### GetEmailTask

Use `GetEmailTask` to reliably collect and validate an email address from the user.

```python
from livekit.agents.beta.workflows import GetEmailTask

# ... within your agent ...
email_result = await GetEmailTask(chat_ctx=self.chat_ctx)
print(f"Collected email: {email_result.email_address}")

```

#### Customize GetEmailTask

In addition to the `extra_instructions` parameter, `GetEmailTask` also accepts a list of additional tools to use. Customize the behavior of this specific task by passing additional parameters:

- `extra_instructions`: Additional instructions for the LLM
- `tools`: Additional tools to use

By default `GetEmailTask` calls its `decline_email_capture()` tool when the user doesn't provide an email address. The following example customizes the task to instead collect alternative contact information by passing extra instructions and an alternate tool:

```python
from livekit.agents.beta.workflows import GetEmailTask
from livekit.agents import function_tool, RunContext
    
@function_tool()
async def get_alternate_contact_info(context: RunContext, contact_method: str, contact_value: str) -> None:
    """Collect alternative contact information when email isn't available"""
    # Store the alternative contact info
    context.session.userdata.alternate_contact_method = contact_method
    context.session.userdata.alternate_contact_value = contact_value
    
    await context.session.generate_reply(
        instructions=f"Acknowledge that you've recorded their {contact_method}: {contact_value}. Let them know this will be used for communication instead of email."
    )

# Customize GetEmailTask with extra instructions and tools
# ... within your agent ...
@function_tool()
async def collect_contact_info(context: RunContext) -> None:
    """Collect email or alternative contact information"""
    email_result = await GetEmailTask(
        chat_ctx=self.chat_ctx,
        extra_instructions="If the user cannot provide an email, call get_alternate_contact_info() instead of decline_email_capture().",
        tools=[get_alternate_contact_info]
    )

    return f"Collected email: {email_result.email_address}"

```

### GetAddressTask

Use `GetAddressTask` to collect and validate a complete mailing address from the user. The task supports international addresses and automatically normalizes spoken address formats.

It returns a `GetAddressResult` dataclass with one field: `address`.

#### Example

The following example uses `GetAddressTask` to collect a user's shipping address:

```python
from livekit.agents.beta.workflows import GetAddressTask
from livekit.agents import Agent, function_tool
    
@function_tool()
async def collect_shipping_address(self) -> str:
    """Collect the user's shipping address"""
    address_result = await GetAddressTask(
        chat_ctx=self.chat_ctx,
        extra_instructions="Emphasize that this is for shipping purposes and accuracy is important."
    )
    
    return f"Shipping address recorded: {address_result.address}"

```

### GetDtmfTask

Use `GetDtmfTask` to collect a series of keypad inputs from callers. The task can handle both Dual-tone multi-frequency (DTMF) tones and spoken digits. This is essential for Interactive Voice Response (IVR) systems and telephony apps. To learn more, see [Handling DTMF](https://docs.livekit.io/sip/dtmf.md).

The following example asks the caller to provide a 10-digit phone number and confirms the number with the caller:

**Python**:

```python
from livekit.agents.beta.workflows.dtmf_inputs import GetDtmfTask
from livekit.agents import function_tool, RunContext

@function_tool
async def ask_for_phone_number(self, context: RunContext) -> str:
    """Ask user to provide a phone number."""
    result = await GetDtmfTask(
        num_digits=10,
        chat_ctx=self.chat_ctx.copy(
            exclude_instructions=True, 
            exclude_function_call=True
        ),
        ask_for_confirmation=True,
        extra_instructions=(
            "Let the caller know you'll record their 10-digit phone number "
            "and that they can speak or dial it. Provide an example such as "
            "415 555 0199, then capture the digits."
        ),
    )
    
    return f"User's phone number is {result.user_input}"

```

#### Configuration options

The following parameters are supported for `GetDtmfTask`:

- `num_digits`: Number of digits to collect
- `ask_for_confirmation`: Whether to confirm inputs with the user
- `dtmf_input_timeout`: Timeout between digit inputs (default: 4.0 seconds)
- `dtmf_stop_event`: Event to stop collection (default: `#`)
- `extra_instructions`: Additional instructions for the LLM

#### Additional resources

The following additional resources provide more information about the topics discussed in this section:

- **[DTMF example](https://github.com/livekit/agents/blob/main/examples/dtmf/basic_dtmf_agent.py)**: A menu-based example that demonstrates using DTMF to collect user input.

- **[Handling DTMF](https://docs.livekit.io/sip/dtmf.md)**: Sending and receiving DTMF in LiveKit telephony apps.

## Task group

> 🔥 **Experimental feature**
> 
> `TaskGroup` is currently experimental and the API might change in a future release.

Task groups let you build complex, user-friendly workflows that mirror real conversational behavior—where users might need to revisit or correct earlier steps without losing context. They're designed as ordered, multi-step flows that can be broken into discrete tasks, with built-in regression support for safely moving backward.

`TaskGroup` supports task chaining, which allows tasks to call or re-enter other tasks dynamically while maintaining the overall flow order. This lets users return to earlier steps as often as needed. All tasks in the group share the same conversation context, and when the group finishes, the summarized context is passed back to the controlling agent.

### Basic usage

Initialize and set up a `TaskGroup` by adding tasks to it. Add tasks in the order they should be executed:

```python
from livekit.agents.beta.workflows import GetEmailTask, TaskGroup

# Create and configure TaskGroup
task_group = TaskGroup()

# Add tasks using lambda factories
task_group.add(
    lambda: GetEmailTask(), 
    id="get_email_task", 
    description="Collects the user's email"
)
task_group.add(
    lambda: GetCommuteTask(), 
    id="get_commute_task", 
    description="Records the user's commute flexibility"
)

# Execute the task group
results = await task_group  # Returns TaskGroupResult object
task_results = results.task_results

# Access results by task ID
print(task_results)
# Output: {
#   "get_email_task": GetEmailResult(email="john.doe@gmail.com"), 
#   "get_commute_task": CommuteResult(can_commute=True, commute_method="subway")
# }

```

The `TaskGroup.add()` method takes three parameters:

- `task_factory`: A callable that returns a task instance (typically a lambda function).
- `id`: A string identifier for the task used to access results.
- `description`: A string description that helps the LLM understand when to regress to this task.

The lambda function allows for tasks to be reinitialized with the same arguments when revisited. The task id and description are passed to the LLM as task identifiers when the LLM needs to regress to a previous task. This allows the LLM to understand the task's purpose and context when revisiting it. Task chaining is supported, allowing users to return to earlier steps as often as needed.

All tasks share the same conversation context. The context is summarized and passed back to the controlling agent when the group finishes. This option can be disabled by passing `summarize_chat_ctx=False` when initializing the task group:

```python
# Disable context summarization
task_group = TaskGroup(summarize_chat_ctx=False)

```

### Complete workflow example

The following is a complete example showing how to build an interview workflow with `TaskGroup`. It collects basic candidate information and then asks about their commute flexibility:

```python
from livekit.agents import AgentTask, function_tool, RunContext
from livekit.agents.beta.workflows import TaskGroup
from dataclasses import dataclass

@dataclass
class IntroResults:
    name: str
    intro: str

@dataclass 
class CommuteResults:
    can_commute: bool
    commute_method: str

class IntroTask(AgentTask[IntroResults]):
    def __init__(self) -> None:
        super().__init__(
            instructions="Welcome the candidate and collect their name and introduction."
        )
    
    async def on_enter(self) -> None:
        await self.session.generate_reply(
            instructions="Welcome the candidate and gather their name."
        )
    
    @function_tool()
    async def record_intro(self, context: RunContext, name: str, intro_notes: str) -> None:
        """Record the candidate's name and introduction"""
        context.session.userdata.candidate_name = name
        results = IntroResults(name=name, intro=intro_notes)
        self.complete(results)

class CommuteTask(AgentTask[CommuteResults]):
    def __init__(self) -> None:
        super().__init__(
            instructions="Ask about the candidate's ability to commute to the office."
        )
    
    @function_tool()
    async def record_commute_flexibility(
        self, 
        context: RunContext, 
        can_commute: bool, 
        commute_method: str
    ) -> None:
        """Record commute flexibility and transportation method"""
        results = CommuteResults(can_commute=can_commute, commute_method=commute_method)
        self.complete(results)

# Set up the workflow
task_group = TaskGroup()
task_group.add(
    lambda: IntroTask(), 
    id="intro_task", 
    description="Collects name and introduction"
)
task_group.add(
    lambda: CommuteTask(), 
    id="commute_task", 
    description="Asks about commute flexibility"
)

# Execute and get results
results = await task_group
task_results = results.task_results

```

## Additional resources

The following topics provider more information on creating complex workflows for your voice AI agents.

- **[Workflows](https://docs.livekit.io/agents/build/workflows.md)**: Complete guide to defining and using workflows in your agents.

- **[Tool definition and use](https://docs.livekit.io/agents/build/tools.md)**: Complete guide to defining and using tools in your agents.

- **[Nodes](https://docs.livekit.io/agents/build/nodes.md)**: Add custom behavior to any component of the voice pipeline.

- **[Testing & evaluation](https://docs.livekit.io/agents/build/testing.md)**: Test every aspect of your agents with a custom test suite.

---

This document was rendered at 2025-11-18T23:55:03.441Z.
For the latest version of this document, see [https://docs.livekit.io/agents/build/tasks.md](https://docs.livekit.io/agents/build/tasks.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).
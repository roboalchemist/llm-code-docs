# Source: https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/agent-configuration/instructions.md

# Instructions

Configure instructions and prompts for your AI agents.

![Instructions Management](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-ec97c5c1f4cae2a56eb24c12df5cea992e75d4b5%2Finstructions_list_view.png?alt=media)

## Overview

The Instructions Management section allows you to create, manage, and organize instruction sets that define how your AI agents behave. Instructions include system prompts, role definitions, tasks, guidelines, and constraints.

## Instructions Dashboard

The dashboard displays key metrics at a glance:

**Summary Cards**:

* **Total Instructions**: Total number of instructions configured (system and agent-level)
* **Active**: Number of active instructions
* **Draft**: Number of draft instructions

## Instruction List View

The instructions table shows all instruction sets with the following information:

**Columns**:

* **Name**: Instruction name and description
* **Type**: Instruction type with color-coded badges (Agent, System, Organization)
* **Agent**: Associated agent name
* **Sections**: Section badges (Context, Role, Tasks, Guidelines, Questions, Examples, Constraints)
* **Priority**: Priority level (1-10)
* **Status**: Current status (Active, Draft)
* **Updated**: Last update date
* **Actions**: Quick actions menu

**Filtering and Search**:

* Search by instruction name
* Filter by Type (Agent, System, Organization)
* Filter by Status (Active, Draft)
* Filter by Agent

## Creating an Instruction

Navigate to **Agent Configuration** → **Instructions** → Click **Create**

![Create Instruction](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-f149aa7f4bdf25333c5b5bd92c0df71c0717c4a0%2Finstruction_create_form.png?alt=media)

### Basic Information

**Instruction Name**\* (Required)

* A descriptive name for this instruction set
* Example: `Code Review Guidelines`

**Instruction Type**\* (Required)

* Select from dropdown: Agent, System, Organization
* Default: `Agent`
* Helper text: "Type determines scope and priority"

**Priority**\* (Required)

* Merge order (lower = higher priority)
* Example: `2`
* Helper text: "Merge order (lower = higher priority)"

**Status**\* (Required)

* Select from dropdown: Active, Draft
* Default: `Active`
* Helper text: "Current status of this instruction"

### Instruction Sections

The instruction sections define the complete behavior and guidelines for the agent. Click to expand/collapse each section.

**Context**

* Background information for the agent
* Example: "You are reviewing code for best practices and potential issues."
* Helper text: "Background information for the agent"

**Role**

* Define the agent's role or persona
* Example: "Senior software engineer and code reviewer"
* Helper text: "Define the agent's role or persona"

**Tasks**

* Specific tasks the agent should perform
* Example: "Review code quality, suggest improvements, identify bugs"
* Helper text: "Specific tasks the agent should perform"

**Guidelines**

* Guidelines and rules to follow
* Example: "Focus on readability, performance, and maintainability"
* Helper text: "Guidelines and rules to follow"

**Questions**

* Clarifying questions to ask
* Example: (empty or specific questions)
* Helper text: "Clarifying questions to ask"

**Examples**

* Example responses or interactions
* Example: (empty or specific examples)
* Helper text: "Example responses or interactions"

**Constraints**

* Limitations and things to avoid
* Example: "Do not approve code with security vulnerabilities"
* Helper text: "Limitations and things to avoid"

### Advanced Settings

Click to expand for additional configuration options (collapsed by default).

### Actions

* **Cancel**: Discard and close
* **Create Instruction**: Save the instruction

## Viewing Instruction Details

To view detailed information about an instruction:

1. Navigate to **Agent Configuration** → **Instructions**
2. Click on an instruction from the list
3. View comprehensive details in the modal dialog

![View Instruction Details](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-e23d91eb337e5d919ff6b1d45081aab1dba7b56e%2Finstruction_details_view.png?alt=media)

**Details Panel Sections**:

**Basic Information**:

* **Instruction Name**: e.g., "Code Review Guidelines"
* **Instruction Type**: Agent, System, or Organization
* **Priority**: Merge order number
* **Status**: Active or Draft

**Instruction Sections** (Expandable): All sections are displayed in read-only mode:

* Context
* Role
* Tasks
* Guidelines
* Questions
* Examples
* Constraints

**Advanced Settings** (Expandable): Additional configuration options if set.

## Editing an Instruction

To update an instruction:

1. Open instruction details page
2. Click **Edit** button (or three-dot menu → Edit)
3. Modify editable fields in the Edit Instruction modal

![Edit Instruction Form](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-b217fae0883017b23384e09a7c995162603a68d8%2Finstruction_edit_form.png?alt=media)

4. Click **Update Instruction** to save changes

> \[!NOTE] The Edit form is identical to the Create/View form, but with an "Update Instruction" button.

**Editable Fields**:

* ✅ Instruction Name
* ✅ Priority
* ✅ Status (Active ↔ Draft)
* ✅ All instruction sections (Context, Role, Tasks, Guidelines, Questions, Examples, Constraints)
* ✅ Advanced Settings
* ❌ Instruction Type (cannot edit after creation)

## Instruction Types

**Agent Instructions**:

* Specific to individual agents
* Define agent-specific behavior
* Override system defaults
* Blue badge in list view

**System Instructions**:

* Apply to all agents by default
* Lowest priority (merged first)
* Define baseline behavior
* Red badge in list view

**Organization Instructions**:

* Company-wide standards
* Apply across all agents
* Medium priority
* Orange badge in list view

## Priority and Merging

**How Priority Works**:

* Lower number = Higher priority
* Instructions are merged in priority order
* Higher priority instructions override lower ones

**Merge Order**:

1. System instructions (priority: -1)
2. Organization instructions (priority: 0)
3. Agent instructions (priority: 1, 2, 3, etc.)

**Example**:

* System Default: Priority -1 (applied first)
* Organization Style: Priority 0 (overrides system)
* Code Review: Priority 2 (final overrides)

## Instruction Sections Explained

**Context**:

* Sets the scene for the agent
* Provides background information
* Explains the situation or environment

**Role**:

* Defines who the agent is
* Sets the persona or character
* Establishes expertise level

**Tasks**:

* Specific actions to perform
* Clear, actionable items
* What the agent should do

**Guidelines**:

* Rules and best practices
* How to approach tasks
* Quality standards

**Questions**:

* Clarifying questions to ask users
* Information gathering prompts
* Validation questions

**Examples**:

* Sample interactions
* Expected responses
* Format examples

**Constraints**:

* What NOT to do
* Limitations and boundaries
* Safety guidelines

## Managing Instructions

### Activating/Deactivating

To change instruction status:

1. Edit the instruction
2. Change Status field
3. Save changes

**Active**: Instruction is in use **Draft**: Instruction is saved but not applied

### Deleting an Instruction

To remove an instruction:

1. Navigate to instruction details or list
2. Click **Delete** button
3. Confirm deletion

> \[!WARNING] Deleting an instruction will affect any agents using it. Make sure to update agent configurations before deleting.

## Best Practices

**Clear and Specific**:

* Be explicit about expected behavior
* Use clear, unambiguous language
* Provide concrete examples

**Structured Sections**:

* Use all relevant sections
* Keep sections focused
* Avoid redundancy between sections

**Priority Management**:

* Use system instructions for defaults
* Use organization instructions for company standards
* Use agent instructions for specific behaviors
* Keep priority numbers organized

**Testing**:

* Test instructions with agents
* Verify behavior matches expectations
* Iterate based on results

**Version Control**:

* Keep drafts for testing
* Document changes in descriptions
* Maintain instruction history

**Security**:

* Include safety constraints
* Define boundaries clearly
* Specify what agents should NOT do

## Next Steps

* Configure [Tools](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/agent-configuration/tools) for your agents
* Set up [Platform Connections](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/agent-configuration/platform-connections)
* Define [Routes](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/agent-configuration/routes) for agent workflows
* Link instructions to agents in [Organization → Agents](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/organization/agents)

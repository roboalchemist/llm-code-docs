# Source: https://docs.flux.ai/reference/copilot.md

# Flux: AI-Powered PCB Design Assistant


Flux is your AI-powered design assistant that lives in your Flux Editor projects, answers complex questions, and helps you move faster by automating PCB design tasks.

Overview

Flux is an AI-powered hardware design assistant integrated directly into Flux Editor. This custom-trained large language model (LLM) understands your schematics, components, electrical connections, and bill of materials. **With Flux, you can accelerate part selection, evaluate alternatives, receive design feedback, and with your approval, make direct changes to your schematic.**

Join the Flux channel in our [Slack community](https://www.flux.ai/slack) to share your experiences and discover new use cases.

## Getting Started with Flux

Access Flux through the Chat tab in the right sidebar or by right-clicking anywhere on your project canvas and selecting "Flux". For detailed guidance on using AI in your design process, see our [AI-assisted PCB design tutorial](https://docs.flux.ai/flux/tutorials/ai-for-hardware-design).

### Starting a conversation

Simply type your question or request in the Chat tab. Flux maintains context within conversation threads, allowing for natural back-and-forth exchanges about your design.

> Flux may take a few seconds to respond as it processes your design information.


### What can Flux do?

- **Answer questions:** Get relevant information for part selection, design feedback, and circuit optimization. [Learn more](https://docs.flux.ai/flux/tutorials/ai-for-hardware-design#design-optimization)
- **Parse datasheets:** Save time by having Flux extract and reference datasheet information. [Learn more](https://docs.flux.ai/flux/tutorials/ai-for-hardware-design#browse-through-datasheets-in-seconds)
- **Modify your design:** Let Flux make connections and changes directly in your schematic with your approval. [Learn more](https://docs.flux.ai/flux/tutorials/ai-for-hardware-design#design-optimization)
- **Access documentation:** Get help with Flux Editor features and workflows. [Learn more](https://docs.flux.ai/flux/tutorials/getting-started-copilot)
- **Find components:** Search the library for parts that meet your specifications. [Learn more](https://docs.flux.ai/flux/tutorials/ai-generated-component-libraries)
- **Generate FMEA reports:** Identify potential failure modes and assess risks with [FMEA analysis](https://docs.flux.ai/flux/reference/fmea-report-generation)
- **Perform calculations:** Evaluate engineering formulas and analyze circuit parameters. [Learn more](https://docs.flux.ai/flux/tutorials/copilot-use-cases)
- **Generate code:** Create Python scripts for data analysis and visualization. [Learn more](https://docs.flux.ai/flux/tutorials/ai-for-hardware-design)
- **Simulate circuits:** Verify circuit behavior using SPICE simulation. [Learn more](https://docs.flux.ai/flux/reference/simulator-tool)

### Specialized Tools

- [@file](https://docs.flux.ai/flux/reference/file-tool) – Access attached datasheets and project files
- [@library](https://docs.flux.ai/flux/reference/library-tool) – Search the Flux component library for part selection
- [@calculator](https://docs.flux.ai/flux/reference/calculator-tool) – Extract equations from datasheets for calculations
- [@code](https://docs.flux.ai/flux/reference/code-tool) – Generate Python scripts and charts
- [@help](https://docs.flux.ai/flux/reference/help-tool) – Search Flux documentation for guidance
- [@simulator](https://docs.flux.ai/flux/reference/simulator-tool) – Perform SPICE circuit simulations

### Project Context Access

Flux analyzes your project to provide relevant suggestions:

- **Project metadata:** Uses project name and description for context
- **Components and netlist:** Understands your circuit's structure and connections
- **Part information:** Accesses datasheets for compatibility and design recommendations
- **Layout**: Understands your projects layout with its footprints, silk and traces
- **Comment locations:** Recognizes the physical context of your questions
- **Flux Editor documentation:** Provides guidance on tool features and workflows

> Flux primarily works with schematics and currently has limited understanding of PCB layout and trace positioning.


## Key Features

### Chat Interface

- **Model Selection**: Choose AI models optimized for different tasks
- **Context Controls**: Select what project information Flux uses
- **File Attachments**: Upload datasheets and reference documents
- **Branching Conversations**: Explore multiple design approaches
- **Response Regeneration**: Get alternative suggestions with "Try Again"

### Design Actions

Flux can directly modify your design upon request:

- **Component Management**: Add, edit, or remove components
- **Designator Changes**: Rename and organize component references
- **Net Modifications**: Create and modify electrical connections
- **Property Editing**: Update component and design parameters

### Keyboard Shortcuts

| Action | Shortcut | 
| ---- | ---- | 
| Open Chat Tab | Alt + C | 
| Focus on chat input | / | 
| Submit message | Ctrl + Enter | 
| Navigate history | Up/Down arrows | 



For detailed usage instructions, see our [Getting Started with Flux](/flux/tutorials/getting-started-copilot) tutorial.

## Privacy and Security

Your design data remains private and secure. For details on our privacy practices, see our [Privacy Statement](/flux/legal/privacy-statement).

## Current Limitations

- **Thread-specific context**: Flux only considers messages within the current conversation thread

## Troubleshooting

| Issue | Solution | 
| ---- | ---- | 
| **No response** | Ensure you're using the Chat tab or right-click menu and have sufficient ACUs | 
| **Incorrect actions** | Review proposed changes before approval and use "Try Again" for alternatives | 
| **Context confusion** | Break complex questions into smaller queries and provide specific context | 



## ACU System

Flux uses ACUs (Agent Compute Units) for AI usage beyond free limits. **All plans include monthly ACUs**, with additional ACUs available on Pro and Organization plans. Learn more about [individual ACUs](https://docs.flux.ai/flux/reference/copilot-credits#acus-for-individual-users) or [organization ACUs](https://docs.flux.ai/flux/reference/copilot-credits#acus-for-organizations).

## Next Steps

- [AI for Hardware Design](https://docs.flux.ai/flux/tutorials/ai-for-hardware-design) - Leverage AI in your design process
- [Flux Use Cases](https://docs.flux.ai/flux/tutorials/copilot-use-cases) - Practical applications
- [Getting Started with Flux](https://docs.flux.ai/flux/tutorials/getting-started-copilot) - Step-by-step guide
- [Schematic Editor](https://docs.flux.ai/flux/reference/reference-schematic-editor) - Master the design environment

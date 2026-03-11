# Source: https://docs.flux.ai/reference/model-selection.md

# AI Model Selection


Flux supports multiple AI models with different capabilities, performance characteristics, and costs. Understanding these models helps you choose the right one for your specific design tasks.

## Overview

Model selection in Flux allows you to:

- Choose between different AI models based on task complexity
- Balance response speed with reasoning capability
- Optimize costs for different types of queries
- Access advanced features like vision support

Each model has unique strengths, and selecting the right one can significantly impact your design workflow efficiency and ACU usage.

## Available Models

Flux offers four AI models, each optimized for different use cases:

### Next Gen (Beta)

**Our most advanced next generation model**

- **Best for**: Cutting-edge capabilities and complex design challenges
- **Capabilities**:
    - Streaming support for real-time responses
    - Vision support for analyzing images and schematics
    - Advanced reasoning for complex PCB design problems

- **When to use**: When you need the absolute latest AI capabilities or are working on particularly novel or challenging design problems

### Advanced Reasoning

**Slower, more capable**

- **Best for**: Complex PCB design problems requiring deep analysis
- **Capabilities**:
    - Streaming support for real-time responses
    - Vision support for analyzing schematics and layouts
    - Enhanced reasoning effort for thorough analysis

- **When to use**:
    - Troubleshooting intricate circuit behavior
    - Designing complex multi-layer PCB layouts
    - Analyzing signal integrity or power distribution issues
    - Making critical design decisions that require comprehensive analysis

### General - Default

**Fast and capable**

- **Best for**: Most everyday PCB design tasks
- **Capabilities**:
    - Streaming support for real-time responses
    - Vision support for image analysis
    - Balanced reasoning for typical design questions

- **When to use**:
    - Performing most everyday design tasks
    - Getting component recommendations
    - Asking general questions about your design
    - When you want a good balance of speed, capability, and cost
    - Creating schematic layouts

This is the default model and provides excellent results for the majority of Flux interactions.

### Speedy

**Faster, less capable**

- **Best for**: Quick queries and simple design assistance
- **Capabilities**:
    - Streaming support for real-time responses
    - Vision support for basic image analysis
    - Fast response times for simple queries

- **When to use**:
    - Need quick responses to straightforward questions
    - Asking simple questions about components or connections
    - Getting basic component information
    - Performing routine design tasks
    - When response speed is more important than deep reasoning

## How to Select a Model

Selecting a model is simple and can be done at any time during your design session:

1. Open the Flux Chat panel in your project
2. Look for the model picker button at the bottom of the chat interface (typically shows the current model name)
3. Click the button to open the model selection menu
4. Select your preferred model from the list of four options
5. The selected model will be used for all subsequent queries until you change it again

![]([SCREENSHOT_MODEL_PICKER_BUTTON])


Your model selection persists throughout your session, so you can switch models as needed based on the complexity of different tasks.

## Cost Considerations

All models consume [Flux ACUs](https://docs.flux.ai/flux/reference/copilot-credits) based on usage. Understanding the cost structure helps you optimize your ACU usage:

**Key insights:**

- **Advanced Reasoning** has the highest per-token cost but delivers the most thorough analysis
- **General** offers the best value for most tasks with good capability at moderate cost
- **Speedy** provides a cost-effective option for simple queries despite moderate pricing
- **Next Gen** offers cutting-edge features at premium pricing

Consider your ACU budget and task complexity when selecting a model. For most users, the General model provides the best balance of capability and cost for everyday design work.

## Performance Trade-offs

Each model balances three key factors differently:

| Model | Response Speed | Reasoning Capability | Cost Efficiency | Best Use Case | 
| ---- | ---- | ---- | ---- | ---- | 
| Next Gen (Beta) | Medium | Highest | Premium | Cutting-edge features, novel problems | 
| Advanced Reasoning | Slower | Very High | Lower | Complex design challenges | 
| General | Fast | High | High | Everyday PCB design tasks | 
| Speedy | Fastest | Moderate | Moderate | Quick queries, simple tasks | 



**Understanding the trade-offs:**

- **Speed vs. Capability**: Faster models (Speedy, General) provide quicker responses but may not capture all nuances of complex problems. Slower models (Advanced Reasoning) take more time but offer deeper insights.
- **Cost vs. Quality**: Higher-cost models (Advanced Reasoning, Next Gen) provide more thorough analysis and better handling of edge cases. Lower-cost options work well for straightforward tasks.
- **Task Matching**: The best model depends on your specific task. Use faster, cheaper models for exploration and information gathering, then switch to more capable models for critical design decisions.

## Best Practices for Model Selection

Follow these guidelines to get the most value from Flux's multi-model system:

### Start with General

The default General model handles most PCB design tasks effectively. It provides a good balance of speed, capability, and cost, making it ideal for:

- Initial project exploration
- Routine component selection
- Standard schematic creation
- General design questions

### Upgrade for Complexity

Switch to Advanced Reasoning when you encounter:

- Complex signal integrity analysis
- Multi-layer board design challenges
- Power distribution network optimization
- Difficult debugging scenarios
- Critical design trade-off decisions

### Use Speedy for Exploration

The Speedy model is perfect for:

- Quick lookups of component specifications
- Simple "yes/no" questions
- Rapid iteration during brainstorming
- Basic connectivity checks
- When you need immediate feedback

### Try Next Gen for Innovation

Experiment with the Next Gen (Beta) model when:

- Working on cutting-edge or novel designs
- Existing models struggle with your problem
- You want access to the latest AI capabilities
- The problem is particularly unique or complex

### Consider Iterative Approaches

Optimize ACU usage by combining models:

1. Use **Speedy** to quickly explore multiple design options
2. Switch to **General** to develop the most promising approach
3. Upgrade to **Advanced Reasoning** for final validation and optimization
4. Try **Next Gen** if standard approaches aren't working

### Monitor Your ACUs

Keep track of your [Flux ACU usage](https://docs.flux.ai/flux/reference/copilot-credits) to understand:

- Which models work best for your typical tasks
- Where you can optimize by using less expensive models
- When investing in more capable models saves time overall

## Common Usage Patterns

### Component Selection Workflow

1. **Speedy**: "What types of voltage regulators could I use?"
2. **General**: "Compare these three voltage regulators for my 5V, 2A application"
3. **Advanced Reasoning**: "Analyze the thermal performance of this regulator in my specific layout"

### Troubleshooting Workflow

1. **General**: "My circuit isn't working as expected, what could be wrong?"
2. **Advanced Reasoning**: "Perform a detailed analysis of the signal integrity issues"
3. **Next Gen**: "Suggest innovative solutions to this complex problem"

### Learning and Exploration

- **Speedy**: Quick questions about PCB design concepts
- **General**: Detailed explanations of design principles
- **Advanced Reasoning**: Deep dives into advanced topics

## Tips for Effective Model Use

1. **Match model to task complexity**: Don't use Advanced Reasoning for simple queries or Speedy for complex analysis
2. **Switch models mid-conversation**: If a model isn't providing the depth you need, switch to a more capable one and continue the conversation
3. **Provide context for better results**: All models perform better when given clear context about your design goals and constraints
4. **Use vision capabilities**: All models support vision, so share screenshots of your schematics or layouts for more accurate assistance
5. **Experiment to find your workflow**: Try different models for your common tasks to discover which provides the best results for your needs
6. **Consider response time**: If you're blocked waiting for an answer, a faster model might help you maintain momentum

## Frequently Asked Questions

**Q: Can I switch models in the middle of a conversation?**
A: Yes! Your conversation context is preserved when switching models, allowing you to seamlessly upgrade or downgrade as needed.

**Q: Which model should I use for my first Flux session?**
A: Start with the General model (default). It handles most tasks well and helps you understand Flux's capabilities before experimenting with other models.

**Q: Do all models support image analysis?**
A: Yes, all four models have vision support and can analyze screenshots of your schematics, layouts, and datasheets.

**Q: How do I know which model is currently selected?**
A: The model picker button at the bottom of the Flux Chat shows the name of your currently selected model.

**Q: Will more models be added in the future?**
A: Flux continually evaluates new AI models to provide the best capabilities to users. The Next Gen (Beta) model represents our ongoing commitment to bringing cutting-edge AI to PCB design.

## Related Features

- **[Flux ACUs](https://docs.flux.ai/flux/reference/copilot-credits)** - Understand how model selection affects ACU usage and manage your ACU balance
- **[Getting Started With Flux](https://docs.flux.ai/flux/tutorials/getting-started-copilot)** - Learn the basics of using Flux in your PCB design workflow
- **[Flux context menu](https://docs.flux.ai/flux/reference/ai-for-hardware-designo8k)** - Quick access to common Flux actions through right-click menus
- **[Library Tool](https://docs.flux.ai/flux/reference/library-tool)** - Search for components using Flux's natural language interface
- **[Simulator Tool](https://docs.flux.ai/flux/reference/simulator-tool)** - Run SPICE simulations directly from Flux chat

By understanding the strengths and trade-offs of each AI model, you can make informed decisions that optimize both your design workflow and ACU usage. Experiment with different models to discover which works best for your specific needs and design style.

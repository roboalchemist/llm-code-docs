# Source: https://docs.flux.ai/tutorials/ai-design-reviews.md

# AI-Powered Design Reviews for PCB Projects with Flux




Check your board for common errors. Flux proactively highlights issues so you can address them before manufacturing.





## Overview

Before you finalize a design and put it into manufacturing, it's essential to review the design first. Any problems that could cause an assembled board to malfunction or create manufacturing defects should be identified before the design is finalized.

Design reviews in Flux make this process efficient by offering automated checks for common errors, guiding you through potential issues, and providing tools for collaborative review across teams.

![](https://uploads.developerhub.io/prod/86Yw/4d1ydk216kfmt6uka1bf75ess2aqaquur0hyp9tpuevmwwop81v3bl74y4hitru1.png)



## Getting Started

Reviewing a PCB design is crucial before manufacturing to avoid defects and functional issues that may arise from design oversights. Design reviews in Flux make this process efficient by offering automated checks for common errors, guiding you through potential issues, and providing tools for collaborative review across teams.

Different stages of your design process benefit from specific reviews. For example:

- **Early Stages:** Run Parts Availability checks to confirm that components are readily available.
- **Component Selection**: Use Resistor Power Rating and Capacitor Voltage Rating checks to validate your design's tolerance for power dissipation and voltage stress.
- **Finalizing Layout**: Let DRCs run automatically with each layout update, addressing physical rule checks to ensure manufacturing readiness.

### AI Design Reviews

AI Design Review goes beyond traditional electrical rule checks (ERC) by interpreting your design's specific context and constraints. It's designed to help you detect not only obvious mistakes but also subtle errors and potential optimizations. With AI assistance, you'll have insights and suggestions that feel like working with an experienced engineer at every review.

Below is a list of all the available reviews. We're constantly adding new ones, so stay tuned:

- **Passive Components Checks**
    - **Resistor Power Rating:** Ensures your resistors can handle the expected power dissipation.
    - **Pull-Up/Pull-Down Resistors:** Checks configuration correctness based on the IC's datasheet requirements.
    - **Capacitor Voltage Rating:** Validates that your capacitors won't fail under your design's voltage conditions.

- **Manufacturing Check**
    - **Parts Availability:** Confirms your selected components are readily available on main distributors.

![](https://uploads.developerhub.io/prod/86Yw/52rty3sl9kh8o9awc8ly859q1ns54p1ccr4nbi0u5a3ubzke18puxv8uv0c7703u.png)



> As with any other AI functionality in Flux, AI Design reviews consume Flux ACUs.



## Collaborative Reviews

Flux's collaboration features let you work with other engineers to review, discuss, and resolve design issues in real-time. Team members can annotate issues, request changes, and track progress, simplifying the review and revision cycle.

For more information on how to use messages to communicate with other team members, please refer to the [collaboration tutorial](https://docs.flux.ai/flux/tutorials/tutorial-collaboration-deep-dive).

## Initiating Reviews

To run a manual AI Design Review, follow these steps:

1. **Navigate to the Review Tab**
    1. Open the Review tab from your project dashboard.

2. **Choose a Category of Reviews**
    1. Expand the review category you want to check for.
    2. Click on the ▶️ icon on the left of the check to run it
        1. Each check needs to be run individually to avoid consuming extra ACUs inadvertently.
        2. DRCs run automatically, there's no need to manually trigger a check.

3. **Run the Check**
    1. The system will execute a series of checks and present the results.

![](https://uploads.developerhub.io/prod/86Yw/sh5gj77oa26dwlzfev8te6s974m2oivul2ky4sg3q8180ri3gxvahtsrzlyyle1m.gif)



## Resolving Issues

Depending on the result, you might need to take specific actions to resolve the issues before moving forward with your design.

1. **Evaluate Results**
    1. Decide whether the result requires your immediate attention.
    2. Flux provides different alarm levels to help guide your attention towards the most important issues.
        1. ❌  for errors, ⚠️ for warnings, and ✅ for pass

2. **Ask Flux for Clarification**
    1. Need more context to resolve the issue? Use Flux to learn about the issue and its impact.
    2. Click on any warning or error to initiate a conversation with Flux and ask any clarifying question you need.

3. **Make Necessary Fixes**
    1. Adjust your design to resolve errors or warnings.

4. **Re-Run the Check**
    1. After applying fixes, re-run the check to confirm that the issue has been resolved.

![](https://uploads.developerhub.io/prod/86Yw/rtrexygtjpnc15asogs3gfj89i197mu7hsentgh5nisq8p03wt8i4ansqp7ec03n.gif)



## Best Practices for AI-Assisted Design Reviews

1. **Run reviews early and often**: Don't wait until the end of your design process to check for issues
2. **Prioritize critical checks**: Focus first on checks that could impact functionality or manufacturability
3. **Attach datasheets**: Provide high-quality datasheets for all components to help Flux provide the most accurate checks
4. **Document decisions**: Keep track of why certain design choices were made, especially when ignoring warnings
5. **Stage your reviews**: Use specific checks during different stages of your design to catch errors early and reduce rework

## Troubleshooting Common Issues

### Resistor Power Rating Issues
- Check your circuit's current requirements and ensure resistors are properly sized
- Consider using higher wattage resistors in power-critical paths
- Verify that thermal considerations have been addressed for high-power resistors

### Capacitor Voltage Rating Problems
- Ensure capacitors are rated for at least 1.5x the maximum expected voltage
- Pay special attention to capacitors in power supply circuits
- Consider voltage spikes and transients when selecting capacitor ratings

### Parts Availability Concerns
- Look for alternative components with similar specifications
- Consider second-source options from different manufacturers
- Evaluate whether design modifications could allow for more readily available components

## What's Next

Now that you've learned how to use Flux for design reviews, you might want to explore:

- [AI Architecture Design](/tutorials/copilot-use-cases/ai-architecture-design) - Learn how to use Flux to develop system architectures
- [AI Component Research](/tutorials/copilot-use-cases/ai-component-research) - Discover how Flux can help with component selection
- [Auto Layout](/tutorials/copilot-use-cases/auto-layout) - See how Flux can assist with PCB layout optimization
- [AI Testing and Debugging](/tutorials/copilot-use-cases/ai-testing-debugging) - Learn how Flux can help troubleshoot design issues

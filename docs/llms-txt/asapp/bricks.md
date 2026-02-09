# Source: https://docs.asapp.com/generativeagent/configuring/tasks-and-functions/bricks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Bricks

> A modular system for composing prompts from reusable and configurable fragments

Bricks are reusable prompt fragments that are managed centrally and can be inserted into task instructions.

This enables you to author, reuse, and safely update modular prompts across GenerativeAgent tasks, reducing duplication, inconsistency, and risk.

Each brick is traceable and synchronized across tasks, unlocking faster onboarding, more consistent customer experiences, and safer experimentation.

<Frame>
  <img src="https://mintcdn.com/asapp/aWb0zjKB3QGaXsPi/images/generativeagent/bricks-overview.png?fit=max&auto=format&n=aWb0zjKB3QGaXsPi&q=85&s=584c5a111ef6f407af12e3d5a222f0c5" alt="Bricks Overview" data-og-width="2893" width="2893" data-og-height="1803" height="1803" data-path="images/generativeagent/bricks-overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/aWb0zjKB3QGaXsPi/images/generativeagent/bricks-overview.png?w=280&fit=max&auto=format&n=aWb0zjKB3QGaXsPi&q=85&s=ce9504aaaa52c5b74ddfef81b82c866f 280w, https://mintcdn.com/asapp/aWb0zjKB3QGaXsPi/images/generativeagent/bricks-overview.png?w=560&fit=max&auto=format&n=aWb0zjKB3QGaXsPi&q=85&s=664b1b4aed9c8ca61d06eb77a9363885 560w, https://mintcdn.com/asapp/aWb0zjKB3QGaXsPi/images/generativeagent/bricks-overview.png?w=840&fit=max&auto=format&n=aWb0zjKB3QGaXsPi&q=85&s=6d8e3cabffe8dd3abc9c61fc4add18ea 840w, https://mintcdn.com/asapp/aWb0zjKB3QGaXsPi/images/generativeagent/bricks-overview.png?w=1100&fit=max&auto=format&n=aWb0zjKB3QGaXsPi&q=85&s=7b55fc8874c7631801864d3fa6a64bbb 1100w, https://mintcdn.com/asapp/aWb0zjKB3QGaXsPi/images/generativeagent/bricks-overview.png?w=1650&fit=max&auto=format&n=aWb0zjKB3QGaXsPi&q=85&s=c872c30cab4ddc048c091ea0b589c418 1650w, https://mintcdn.com/asapp/aWb0zjKB3QGaXsPi/images/generativeagent/bricks-overview.png?w=2500&fit=max&auto=format&n=aWb0zjKB3QGaXsPi&q=85&s=63c97f8d9c1197903f23f3e18cb2d514 2500w" />
</Frame>

### When to use Bricks

Use bricks for any content you want to reuse across multiple tasks:

* Greetings and standard opening messages
* Disclaimers and legal notices
* Business policies and guidelines
* Company information and context
* Tone guidelines for customer interactions
* Common instructions that don't change

## Configuring Bricks

Here is a step-by-step overview of how to configure and use Bricks:

<Steps>
  <Step title="Create a Brick">
    1. Navigate to **Bricks** under the **Build** section.
    2. Click on **Create Brick**.
    3. Under **Variable Name**, provide a unique name for the Brick.
    4. Under **Description**, provide a brief description of the Brick's purpose.
    5. Click **Create** to save the Brick.
    6. Add the prompt of the Brick in the text area.
    7. Click **Save** to save the content of the Brick.

    Bricks support [conditional templates](/generativeagent/configuring/tasks-and-functions/conditional-templates) which enables you to reference variables and implement conditional logic in your bricks.

    <Warning>
      When using a variable, ensure you have set the variable within the task instructions.
    </Warning>
  </Step>

  <Step title="Reference Bricks in a Task or other components">
    Reference bricks wherever [Jinja variables](/generativeagent/configuring/tasks-and-functions/conditional-templates) are supported, including prompts and other text fields.

    For this example, we will reference the Brick in a Task.

    1. Navigate to **Tasks** under the **Build** section.
    2. Select an existing Task or create a new one.
    3. In the Task editor, navigate to where you want to insert the Brick (e.g., Task Instructions, Talker Prompt, Reasoner Prompt).
    4. Use the Jinja syntax to reference the Brick by its variable name, e.g., `@brick{brick_variable_name}`.
    5. Click **Save** to save the Task.
  </Step>

  <Step title="Preview & Validate">
    Use the Previewer to test how the updated Bricks affect the behavior of the GenerativeAgent.
  </Step>

  <Step title="Deployment">
    1. Click on **Deploy** to deploy the updated tasks with the new Brick content.
    2. Under **Select Resource**, choose **General Configurations**.
    3. Select the variable names of the Bricks you want to deploy.
    4. Click **Deploy** to apply the changes.
  </Step>
</Steps>

## Updating Bricks

When a Brick is updated and deployed, all tasks that reference that Brick automatically receive the updated content upon the  deployment. This ensures consistency across all tasks using the same Brick.

Tasks referencing that Brick will not need to be redeployed.

Before making changes or deploying updates to a Brick, you can check which tasks reference that Brick to understand the impact.

<Frame>
  <img width="300px" src="https://mintcdn.com/asapp/aWb0zjKB3QGaXsPi/images/generativeagent/configuring/referenced-tasks-bricks.png?fit=max&auto=format&n=aWb0zjKB3QGaXsPi&q=85&s=04ffdc4cedb0e56fe9aa9788ee78ca85" alt="References to Tasks in Bricks" data-og-width="542" data-og-height="585" data-path="images/generativeagent/configuring/referenced-tasks-bricks.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/aWb0zjKB3QGaXsPi/images/generativeagent/configuring/referenced-tasks-bricks.png?w=280&fit=max&auto=format&n=aWb0zjKB3QGaXsPi&q=85&s=cafd7307dc29f3941522cc87ae596d98 280w, https://mintcdn.com/asapp/aWb0zjKB3QGaXsPi/images/generativeagent/configuring/referenced-tasks-bricks.png?w=560&fit=max&auto=format&n=aWb0zjKB3QGaXsPi&q=85&s=d9d52a62adcbaae5e3637347fb801e71 560w, https://mintcdn.com/asapp/aWb0zjKB3QGaXsPi/images/generativeagent/configuring/referenced-tasks-bricks.png?w=840&fit=max&auto=format&n=aWb0zjKB3QGaXsPi&q=85&s=dbb865cfb95ac011e4bccb548484d9f1 840w, https://mintcdn.com/asapp/aWb0zjKB3QGaXsPi/images/generativeagent/configuring/referenced-tasks-bricks.png?w=1100&fit=max&auto=format&n=aWb0zjKB3QGaXsPi&q=85&s=9776f9915db52e208b422eba2c307ea3 1100w, https://mintcdn.com/asapp/aWb0zjKB3QGaXsPi/images/generativeagent/configuring/referenced-tasks-bricks.png?w=1650&fit=max&auto=format&n=aWb0zjKB3QGaXsPi&q=85&s=ef127ada6a4ea875832c259a55a14852 1650w, https://mintcdn.com/asapp/aWb0zjKB3QGaXsPi/images/generativeagent/configuring/referenced-tasks-bricks.png?w=2500&fit=max&auto=format&n=aWb0zjKB3QGaXsPi&q=85&s=ef17824fba0d61949af8c555650bd317 2500w" />
</Frame>

## Next Steps

<CardGroup>
  <Card title="Referencing a Variable" href="generativeagent/configuring/tasks-and-functions/reference-variables">
    Learn how to use reference variables to store and reuse data from function responses
  </Card>

  <Card title="Building your first GenerativeAgent" href="/generativeagent/getting-started">
    Learn how to build your first GenerativeAgent that can use your KnowledgeBase to start answering your users' questions.
  </Card>
</CardGroup>

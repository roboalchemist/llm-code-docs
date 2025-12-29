# Source: https://docs.ultravox.ai/gettingstarted/quickstart/tools.md

# Tools Quickstart

> Learn how to start using built-in tools and how to create custom tools.

This quickstart contains two parts. This guide will use the [Ultravox Web App](https://app.ultravox.ai) but you can also use the [Ultravox API](/api-reference/introduction) if you prefer (not covered in this guide).

<CardGroup cols={1}>
  <Card title="Part 1: Using the Built-in Hang Up Tool" icon="screwdriver-wrench" href="#using-the-built-in-hangup-tool">
    Add the `hangUp` tool so the agent can end the call at the right time.
  </Card>

  <Card title="Part 2: Creating a Custom Tool" icon="wand-magic-sparkles" href="#creating-a-custom-tool">
    Create a custom tool that retrieves information from a 3rd party API and provides the information to the user.
  </Card>
</CardGroup>

## Using the Built-in `hangUp` Tool

<Steps>
  <Step title="Start with the Ultravox Console">
    Go to [Agents](https://app.ultravox.ai/agents).

    <img className="block dark:hidden" src="https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-agent-light.png?fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=5075ea371cc6e5d7bae4aac031e72fca" data-og-width="2880" width="2880" data-og-height="1604" height="1604" data-path="images/screenshots/quickstart-agent-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-agent-light.png?w=280&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=8cfe96895b4f554235a048aec802a58a 280w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-agent-light.png?w=560&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=8eb552c756a253b0ccb30e04232042a8 560w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-agent-light.png?w=840&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=9476514a9922128fbbcad9a660d901fc 840w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-agent-light.png?w=1100&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=b3e9ccde9631662b95b538f89cd356f7 1100w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-agent-light.png?w=1650&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=120d3588fe93728f8c1c29881405392d 1650w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-agent-light.png?w=2500&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=3b8dfeba63d3543bf1d4034c00cc6f6d 2500w" />

    <img className="hidden dark:block" src="https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-agent-dark.png?fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=39967822ec3a25f4851e792239bf3b9c" data-og-width="2880" width="2880" data-og-height="1604" height="1604" data-path="images/screenshots/quickstart-agent-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-agent-dark.png?w=280&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=75404bc81853297728af30ee17581081 280w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-agent-dark.png?w=560&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=af5ac84086330b9c921a3d01b34a07d0 560w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-agent-dark.png?w=840&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=2abba28a6d0d53a947c77fab98b8ba68 840w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-agent-dark.png?w=1100&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=44a71b26bd1d15df6b4eb3b23c8ab3b9 1100w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-agent-dark.png?w=1650&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=982c5d5758bab627e69886ad8d2ff952 1650w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-agent-dark.png?w=2500&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=989797480356143c344c6b9784657f8e 2500w" />
  </Step>

  <Step title="Create a New Agent">
    Click on `New Agent` in the top right corner.
  </Step>

  <Step title="Enter a Name and Prompt">
    Copy & paste the following for the name of your agent:

    ```text  theme={null}
    Tools_Agent
    ```

    Next, copy and paste this system prompt:

    ```text  theme={null}
    If the user says "Oklahoma" you must immediately call the 'hangUp' tool.
    ```
  </Step>

  <Step title="Add the hangUp Tool">
    Use the `Tools` drop-down and select the `hangUp` tool.

    <img className="block dark:hidden" src="https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-tools-add-light.png?fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=abf3f476528af11cc7662fc21d8a0863" data-og-width="2880" width="2880" data-og-height="1600" height="1600" data-path="images/screenshots/quickstart-tools-add-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-tools-add-light.png?w=280&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=0478cdcefdd2d80e3897b7f2ef16940e 280w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-tools-add-light.png?w=560&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=6261363a6905a514873cce2fe40f4d9e 560w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-tools-add-light.png?w=840&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=3fc52a69ebcc41ecb1ffcb9d02f2cca4 840w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-tools-add-light.png?w=1100&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=33858223fb1a3124cac2da8c0adc061f 1100w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-tools-add-light.png?w=1650&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=ddeaff696fd4ce87a4398ba228b083b4 1650w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-tools-add-light.png?w=2500&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=33f7db49eb8eeda7f8952edb4213d669 2500w" />

    <img className="hidden dark:block" src="https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-tools-add-dark.png?fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=f4cb20b2bde647ecd3afbb0d5d70277f" data-og-width="2880" width="2880" data-og-height="1600" height="1600" data-path="images/screenshots/quickstart-tools-add-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-tools-add-dark.png?w=280&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=90cbb72680f8baf923ba1a0ab9594e00 280w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-tools-add-dark.png?w=560&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=b36515d2f8d3c88d218c2cf435c674c8 560w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-tools-add-dark.png?w=840&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=db41cc3be59d6c78ef7657c2c84b44c1 840w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-tools-add-dark.png?w=1100&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=d82e2a289542ba6b489460fdae065699 1100w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-tools-add-dark.png?w=1650&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=aa2c85fbe9e31b9d22fa7a2fdb071a2b 1650w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-tools-add-dark.png?w=2500&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=ccc0139b4b13802cc733c88c0de0e9bf 2500w" />
  </Step>

  <Step title="Save & Test the Agent">
    * Save the agent using the `Save` button. This agent will be used in part two of this quickstart.

    * Start a call with your agent by clicking the `Test Agent` button on the bottom right.

    * When you say the word "Oklahoma", the agent will call the tool and the call will end and you will see the call state change to `DISCONNECTED`.
  </Step>
</Steps>

## Creating a Custom Tool

<Info>
  This part uses the `Tools_Agent` we created above in [Using Built-in Tools](#using-built-in-tools).
</Info>

<Steps>
  <Step title="Create the getAdvice Tool">
    <img className="block dark:hidden" src="https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-tools-custom-light.png?fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=2038041d0c59325505a4768149157ddf" data-og-width="2880" width="2880" data-og-height="1600" height="1600" data-path="images/screenshots/quickstart-tools-custom-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-tools-custom-light.png?w=280&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=d447e85980639547267360f5ba251a3a 280w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-tools-custom-light.png?w=560&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=51ad43c87c82c2c2305d57b81527e35d 560w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-tools-custom-light.png?w=840&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=7629df695c4c828391d356d00e3cb6cb 840w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-tools-custom-light.png?w=1100&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=92a22f8208dea9fc6f26eb2e103b8793 1100w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-tools-custom-light.png?w=1650&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=2f7318392a08c91ba447838af4c5c3e9 1650w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-tools-custom-light.png?w=2500&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=90397b33dbfff3026d11daea9a41f076 2500w" />

    <img className="hidden dark:block" src="https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-tools-custom-dark.png?fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=44859e27f91959cbecc01158f40d1bd0" data-og-width="2880" width="2880" data-og-height="1600" height="1600" data-path="images/screenshots/quickstart-tools-custom-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-tools-custom-dark.png?w=280&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=8b9c6aba2b9345d0b922b512e48b4efd 280w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-tools-custom-dark.png?w=560&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=1817eddc3d19bcd8a68640bc4824ecc4 560w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-tools-custom-dark.png?w=840&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=af4a65dfd0018bb713880ced46287443 840w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-tools-custom-dark.png?w=1100&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=e0d9db202f92a7ed31b1ee632590dd79 1100w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-tools-custom-dark.png?w=1650&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=2ae5396f81a8365318494a01a5a5796d 1650w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/quickstart-tools-custom-dark.png?w=2500&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=a08ef6c28595e1209a012af06233bfda 2500w" />

    Under `Tools` click on [New Tool](https://app.ultravox.ai/tools/new). Set properties as follows and then click on `Save`:

    **Tool Name:**

    ```text  theme={null}
    getAdvice
    ```

    **Description:**

    ```text  theme={null}
    This tool provides random advice.
    ```

    **Custom Endpoint URL:**

    ```text  theme={null}
    api.adviceslip.com/advice
    ```

    <Note>We are using the public adviceslip API as a quick example.</Note>
  </Step>

  <Step title="Edit Tools_Agent">
    * Go to [Agents](https://app.ultravox.ai/agents)
    * Click `...` on the right side of our `Tools_Agent`
    * Choose `Edit`
  </Step>

  <Step title="Add the getAdvice Tool">
    Use the `Tools` drop-down and select the `getAdvice` tool. You can keep the `hangUp` tool selected.
  </Step>

  <Step title="Update Prompt">
    Copy & paste the following for the system prompt:

    ```text  theme={null}
    You are the world's best companion. You love talking to people.

    If someone asks for or needs advice, you must use the 'getAdvice' tool. 
    When you receive advice from the tool call, relay it back to the user.

    If the user says "Oklahoma" you must immediately call the 'hangUp' tool.
    ```
  </Step>

  <Step title="Save & Test the Agent">
    * Save the agent using the `Save` button.

    * Start a call with your agent by clicking the `Test Agent` button on the bottom right.

    * If you ask for advice, the agent will now use the tool to get random advice from the adviceslip API.

    * Saying "Oklahoma" will continue to trigger the hangUp tool.
  </Step>
</Steps>

## Next Steps

1. Learn more about [Built-in Tools](/tools/built-in-tools) you can use.
2. Dig into [HTTP vs. Client Tools](/tools/custom/http-vs-client-tools) to understand the differences.
3. Read about [Durable vs. Temp Tools](/tools/custom/durable-vs-temporary-tools).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.ultravox.ai/llms.txt
# Source: https://docs.crewai.com/en/enterprise/guides/enable-crew-studio.md

# Enable Crew Studio

> Enabling Crew Studio on CrewAI AMP

<Tip>
  Crew Studio is a powerful **no-code/low-code** tool that allows you to quickly scaffold or build Crews through a conversational interface.
</Tip>

## What is Crew Studio?

Crew Studio is an innovative way to create AI agent crews without writing code.

<Frame>
    <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=c4f5428b111816273b3b53d9cef14fad" alt="Crew Studio Interface" data-og-width="2654" width="2654" data-og-height="1710" height="1710" data-path="images/enterprise/crew-studio-interface.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=35ea9140f0b9e57da5f45adbc7e2f166 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=ae6f0c18ef3679b5466177710fbc4a94 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=6c3e2fe013ab4826da90c937a9855635 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=7f1474dd7f983532dc910363b96f783a 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f1a6d7e744e6862af5e72dce4deb0fd1 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=74aeb1ccd8e2c8f84d4247b8d0259737 2500w" />
</Frame>

With Crew Studio, you can:

* Chat with the Crew Assistant to describe your problem
* Automatically generate agents and tasks
* Select appropriate tools
* Configure necessary inputs
* Generate downloadable code for customization
* Deploy directly to the CrewAI AMP platform

## Configuration Steps

Before you can start using Crew Studio, you need to configure your LLM connections:

<Steps>
  <Step title="Set Up LLM Connection">
    Go to the **LLM Connections** tab in your CrewAI AMP dashboard and create a new LLM connection.

    <Note>
      Feel free to use any LLM provider you want that is supported by CrewAI.
    </Note>

    Configure your LLM connection:

    * Enter a `Connection Name` (e.g., `OpenAI`)
    * Select your model provider: `openai` or `azure`
    * Select models you'd like to use in your Studio-generated Crews
      * We recommend at least `gpt-4o`, `o1-mini`, and `gpt-4o-mini`
    * Add your API key as an environment variable:
      * For OpenAI: Add `OPENAI_API_KEY` with your API key
      * For Azure OpenAI: Refer to [this article](https://blog.crewai.com/configuring-azure-openai-with-crewai-a-comprehensive-guide/) for configuration details
    * Click `Add Connection` to save your configuration

    <Frame>
            <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-connection-config.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c06fcdb008733c7e1d6ec7fcd055ff2c" alt="LLM Connection Configuration" data-og-width="2526" width="2526" data-og-height="1794" height="1794" data-path="images/enterprise/llm-connection-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-connection-config.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=929f529b52c50511a773f2ec0791cd9a 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-connection-config.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=3f922308dfa3d65a392d5ebecec593dd 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-connection-config.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=df92dce860921dac542382ca3882decb 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-connection-config.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=1772f4775c3f02e17d152bc00a08ba45 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-connection-config.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=508cb4812120d6bc6b3010415f118a4a 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-connection-config.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=2eb75a3247fbc61ab727978b8a6ce371 2500w" />
    </Frame>
  </Step>

  <Step title="Verify Connection Added">
    Once you complete the setup, you'll see your new connection added to the list of available connections.

    <Frame>
            <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connection-added.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3726ffaa33f0bfdf221dd542ae729f69" alt="Connection Added" data-og-width="1966" width="1966" data-og-height="532" height="532" data-path="images/enterprise/connection-added.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connection-added.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=4acf6c926c288b5d32f9c537329b4611 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connection-added.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=9bdfd3df0a3d3f3ba1d2f91472471ba0 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connection-added.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1658dc464f8869ad3f0eb0595faf4048 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connection-added.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=a0e1b1b559acc03bfbc3a40f17920e40 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connection-added.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=837c27260c5c258d9da4c306e4d16ae0 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connection-added.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=649700c55072c94135d7a44e07b5f0df 2500w" />
    </Frame>
  </Step>

  <Step title="Configure LLM Defaults">
    In the main menu, go to **Settings → Defaults** and configure the LLM Defaults settings:

    * Select default models for agents and other components
    * Set default configurations for Crew Studio

    Click `Save Settings` to apply your changes.

    <Frame>
            <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-defaults.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b773c2d7e8338e8dbf609ff45ce16eda" alt="LLM Defaults Configuration" data-og-width="2534" width="2534" data-og-height="1128" height="1128" data-path="images/enterprise/llm-defaults.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-defaults.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b08470ddaeb12d378083dff2e852934b 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-defaults.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=e58e547acb63b13b01fdf52c1771d42d 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-defaults.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c9b45ef41f6b3068580a4085c5c914cf 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-defaults.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=4366e6bb2207f83d10b825a6e5393743 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-defaults.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=1a48e293ccbcb1c990cfb0a56d386b32 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-defaults.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f11e748fbc1d3ef89abfef88b95ba9fb 2500w" />
    </Frame>
  </Step>
</Steps>

## Using Crew Studio

Now that you've configured your LLM connection and default settings, you're ready to start using Crew Studio!

<Steps>
  <Step title="Access Studio">
    Navigate to the **Studio** section in your CrewAI AMP dashboard.
  </Step>

  <Step title="Start a Conversation">
    Start a conversation with the Crew Assistant by describing the problem you want to solve:

    ```md  theme={null}
    I need a crew that can research the latest AI developments and create a summary report.
    ```

    The Crew Assistant will ask clarifying questions to better understand your requirements.
  </Step>

  <Step title="Review Generated Crew">
    Review the generated crew configuration, including:

    * Agents and their roles
    * Tasks to be performed
    * Required inputs
    * Tools to be used

    This is your opportunity to refine the configuration before proceeding.
  </Step>

  <Step title="Deploy or Download">
    Once you're satisfied with the configuration, you can:

    * Download the generated code for local customization
    * Deploy the crew directly to the CrewAI AMP platform
    * Modify the configuration and regenerate the crew
  </Step>

  <Step title="Test Your Crew">
    After deployment, test your crew with sample inputs to ensure it performs as expected.
  </Step>
</Steps>

<Tip>
  For best results, provide clear, detailed descriptions of what you want your crew to accomplish. Include specific inputs and expected outputs in your description.
</Tip>

## Example Workflow

Here's a typical workflow for creating a crew with Crew Studio:

<Steps>
  <Step title="Describe Your Problem">
    Start by describing your problem:

    ```md  theme={null}
    I need a crew that can analyze financial news and provide investment recommendations
    ```
  </Step>

  <Step title="Answer Questions">
    Respond to clarifying questions from the Crew Assistant to refine your requirements.
  </Step>

  <Step title="Review the Plan">
    Review the generated crew plan, which might include:

    * A Research Agent to gather financial news
    * An Analysis Agent to interpret the data
    * A Recommendations Agent to provide investment advice
  </Step>

  <Step title="Approve or Modify">
    Approve the plan or request changes if necessary.
  </Step>

  <Step title="Download or Deploy">
    Download the code for customization or deploy directly to the platform.
  </Step>

  <Step title="Test and Refine">
    Test your crew with sample inputs and refine as needed.
  </Step>
</Steps>

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Crew Studio or any other CrewAI AMP features.
</Card>

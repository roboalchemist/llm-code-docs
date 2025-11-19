# Source: https://dev.writer.com/no-code/chat-kg.md

# Chat with Knowledge Graph

export const PromptComponent = ({prompt}) => <div>
    <p class="prompts">{prompt}</p>
  </div>;

With Knowledge Graph mode for chat agents, you can create agents that can search for information and answer questions specific to your company's data.

This guide walks through the steps to create a Knowledge Graph from a Confluence space. Then, it creates a chat agent that uses that Knowledge Graph to answer questions about your company's policies.

<img src="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/kg-chat.png?fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=f2b69a1452da4362760df54c118fad56" alt="Example of a chat agent with Knowledge Graph" data-og-width="2604" width="2604" data-og-height="1454" height="1454" data-path="images/no-code/kg-chat.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/kg-chat.png?w=280&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=388ba12ff2e2489cba4dc624d06b58b3 280w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/kg-chat.png?w=560&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=f939b2a6e7cff05f9160c139c7df64e9 560w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/kg-chat.png?w=840&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=7c581656ae9f87845aba994adee3537c 840w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/kg-chat.png?w=1100&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=dcd328af235ac3628525e391be13c42a 1100w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/kg-chat.png?w=1650&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=e0d0da304088f89fc9e9fcd8da255cf0 1650w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/kg-chat.png?w=2500&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=359d20d587933f6dcdabb384fc6e4f03 2500w" />

<Steps>
  <Step title="Create a Knowledge Graph">
    To get started, set up a Knowledge Graph in Writer.

    From the home screen of AI Studio, click **Knowledge Graphs** in the left sidebar and click **Add a Graph**.

        <img src="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/create-knowledge-graph.png?fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=9b80b6d0ab802bef51dfc98eeeb3d80d" alt="Create a Knowledge Graph" data-og-width="2638" width="2638" data-og-height="1636" height="1636" data-path="images/no-code/create-knowledge-graph.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/create-knowledge-graph.png?w=280&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=996b297d7b0b9e5bed39aa2ca07a17ec 280w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/create-knowledge-graph.png?w=560&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=83897e464a415ac0a7b1dc286bf8fff5 560w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/create-knowledge-graph.png?w=840&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=d229508e62a2e4045c020a43c0ffd240 840w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/create-knowledge-graph.png?w=1100&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=7fe111a9b9588201246fdb48b3b2ad10 1100w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/create-knowledge-graph.png?w=1650&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=20cc5d72a426404a061d28a2b310e0d5 1650w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/create-knowledge-graph.png?w=2500&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=b29e27b4b9cb6abf00597a222b1637f6 2500w" />

    <Warning>Knowledge graphs created in AI Studio aren't accessible in the Ask Writer core app unless you define the Knowledge Graph as part of a custom agent.</Warning>
  </Step>

  <Step title="Add graph name and description">
    In the modal that appears, give your graph a name and description.
    <img src="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/kg-options.png?fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=aa2cb203def92473b5653cdacde86102" alt="Add a graph" data-og-width="874" width="874" data-og-height="422" height="422" data-path="images/no-code/kg-options.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/kg-options.png?w=280&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=36bb4a0ae4078ad75a6b35c11df07920 280w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/kg-options.png?w=560&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=62480e9b177d68479f004c6488e73649 560w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/kg-options.png?w=840&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=801f1aa00b4cbfdcc54a15232e4d8873 840w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/kg-options.png?w=1100&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=6c3027704ea76359fb16bc4ebbf3de55 1100w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/kg-options.png?w=1650&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=aade89497d235376bd3cb0bed4b6e32b 1650w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/kg-options.png?w=2500&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=495fa7590806a598a36ad191fb0148bb 2500w" />
  </Step>

  <Step title="Add data to your graph">
    Choose how you want to add your data to the graph and add your data:

    * Add via manual file upload: Upload files manually from your device
    * Add via data connector: Integrate data from an existing tool such as Confluence, Notion, and Google Drive
    * Add via API: Send docs to Writer [via the API](/home/knowledge-graph)
    * Add websites: Create a list of websites to search

    This example uses the **Add via data connector** option to integrate data from a Confluence space. To use this option, you need to have access to the Confluence space you want to integrate.

    Learn more about creating and managing a Knowledge Graph in the [Knowledge Graphs support article](https://support.writer.com/article/242-how-to-create-and-manage-a-knowledge-graph).
  </Step>

  <Step title="Create an agent with chat capabilities">
    Once you create your Knowledge Graph, you can then create an agent with chat capabilities and add the Knowledge Graph to the agent.

    From the [AI Studio home page](https://app.writer.com/ai-studio), click **Build an agent** in the top right corner. Then, select **Chat** as the type of agent you want to create.
  </Step>

  <Step title="Enable the Knowledge Graph mode">
    For this example, enable only the **Knowledge Graph mode** so the chat agent answers questions specifically about your company's data from the Knowledge Graph.

    In the agent configuration, turn off the **General chat mode** toggle and turn on the **Knowledge Graph mode**.

    Next, select **Always stay connected to a specific set of graphs** and select the Knowledge Graph you created in the previous step. This ensures that the agent only answers questions about the data in the Knowledge Graph you provide, and doesn't allow the user to switch to a different Knowledge Graph.

        <img src="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/enable-kg.png?fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=61b7035d642b6c4dc07c40738b46d92d" alt="Enable Knowledge Graph" data-og-width="1226" width="1226" data-og-height="1508" height="1508" data-path="images/no-code/enable-kg.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/enable-kg.png?w=280&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=b73e68dbe726079fd5ef48f550643177 280w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/enable-kg.png?w=560&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=0435c9298b3e67aefcee53bf934d5053 560w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/enable-kg.png?w=840&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=6352fad8a901b88acb4f68bac7c536fc 840w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/enable-kg.png?w=1100&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=daec8e7afd32e7eecf7b663a0bdcf3a9 1100w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/enable-kg.png?w=1650&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=5653ea72f0f502b820a6ae21c0b1a2db 1650w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/enable-kg.png?w=2500&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=2b750ba482903ef0555f7a097952e28e 2500w" />

    <Tip>
      **Want to further customize Knowledge Graph behavior?** You can fine-tune how your agent searches, ranks, and retrieves content from your Knowledge Graph using advanced configuration options. Learn more about [configuring Knowledge Graph settings](/no-code/chat#configure-knowledge-graph-settings) for detailed control over grounding level, search balance, response length, and more.
    </Tip>
  </Step>

  <Step title="Add instructions for the model">
    You can add additional instructions for Knowledge Graph mode by clicking **Add instructions**.

    The instructions can include context for the model to understand what this agent does, and what types of answers it should provide. You may also want to include instructions on what to output if someone asks a question that isn't specific to a customer story or quote.

    For example, you could include: <PromptComponent prompt={`If you get a question about a company other than Writer, output: I don't have any information on that.`} />
  </Step>

  <Step title="Test your agent">
    On the right side of the screen, you can see what your agent looks like and test it.

    Try asking a variety of questions to make sure you're getting the types of answers you expect. You can continue to update the instructions until you're happy with the answers you receive.
  </Step>

  <Step title="Deploy your agent">
    Once you're happy with how everything looks, [deploy your agent](/no-code/deploying-an-agent) so that everyone can use it.
  </Step>
</Steps>

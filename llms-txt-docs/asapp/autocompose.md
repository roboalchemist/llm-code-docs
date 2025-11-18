# Source: https://docs.asapp.com/changelog/autocompose.md

# AutoCompose Updates

> New updates and improvements across AutoCompose

<Update label="2023-10-16 - Sandbox for AutoCompose">
  AutoCompose Sandbox is a playground environment that allows administrators to preview and test the AutoCompose experience before integration. The sandbox provides a realistic simulation of how agents will interact with AutoCompose's suggestion features, including:

  * Complete response suggestions above the composer
  * In-line suggestions while typing
  * Custom response management through the AutoCompose panel
  * Access to the global response library

  The sandbox environment helps administrators understand the agent experience and evaluate AutoCompose's capabilities firsthand.

  <Frame caption="AutoCompose running in a sandbox environment.">
    <img src="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-780cd7be-c1db-c5f1-cef1-8627c8e2eec3.png?fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=e9ca1363e0d6d364460a5846af551d22" data-og-width="1600" width="1600" data-og-height="810" height="810" data-path="image/uuid-780cd7be-c1db-c5f1-cef1-8627c8e2eec3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-780cd7be-c1db-c5f1-cef1-8627c8e2eec3.png?w=280&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=8b79c3df56e4dcfbaeedb1a9b07eb52c 280w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-780cd7be-c1db-c5f1-cef1-8627c8e2eec3.png?w=560&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=4ddfa61031ab21c8ec0c3da4f7c5718d 560w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-780cd7be-c1db-c5f1-cef1-8627c8e2eec3.png?w=840&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=ff3e10a5d16cc5cfbfa204a40e7d5c74 840w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-780cd7be-c1db-c5f1-cef1-8627c8e2eec3.png?w=1100&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=461babcfbbd3d5ab9daecf33c023a832 1100w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-780cd7be-c1db-c5f1-cef1-8627c8e2eec3.png?w=1650&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=ef117a75cd0dcf41206913fd60bc7360 1650w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-780cd7be-c1db-c5f1-cef1-8627c8e2eec3.png?w=2500&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=22125fc2c65ac06b9dffbe527df850a2 2500w" />
  </Frame>

  <Accordion title="How It Works">
    ## How It Works

    Watch the following video walkthrough to learn how to use the AutoCompose Sandbox:

    <iframe width="560" height="315" allow="fullscreen *" src="https://fast.wistia.net/embed/iframe/ezkjx798f7" />

    AutoCompose Sandbox enables you to play both sides of the conversation. AutoCompose won't suggest anything while simulating a customer, but suggestions will populate for the agent role.

    The AutoCompose panel situated on the right side allows you to define and browse custom responses, which can then be accessed as suggestions in the composer. It also enables browsing of the global response list that has been defined globally. Finally, it allows an agent to customize the behavior of AutoPilot.

    As agents use the suggestions provided by AutoCompose, the response library will grow, which will be reflected in the suggestions produced by AutoCompose.
  </Accordion>
</Update>

<Update label="2022-12-07 - Tooling for AutoCompose">
  AutoCompose now supports configuration of the global response list in ASAPP's AI-Console. Users can manage responses through bulk uploads via CSV files or targeted edits in the UI. This self-serve capability enables teams to maintain an up-to-date response library that improves suggestion quality and coverage for agents.

  <Frame>
    <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e57d895e-a797-9b64-158c-beebfd45d4db.png?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=f0d51b84db8df8e1140bf3fb048a1f1a" data-og-width="1930" width="1930" data-og-height="1372" height="1372" data-path="image/uuid-e57d895e-a797-9b64-158c-beebfd45d4db.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e57d895e-a797-9b64-158c-beebfd45d4db.png?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=cfa75ee485e2429dfd718c7663177dfc 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e57d895e-a797-9b64-158c-beebfd45d4db.png?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=20e6549d5eaf889b46e8081e04975148 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e57d895e-a797-9b64-158c-beebfd45d4db.png?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=13e080dbccf860b0760682af7696e392 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e57d895e-a797-9b64-158c-beebfd45d4db.png?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=579f934170d2fc7c6bd1da9efdd7b622 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e57d895e-a797-9b64-158c-beebfd45d4db.png?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=5ecbbcf061956b7ca8754471a51673ee 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e57d895e-a797-9b64-158c-beebfd45d4db.png?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=509bd81e7f86cdadd69e6a559d9f72e9 2500w" />
  </Frame>

  <Accordion title="How It Works">
    ## How It Works

    Watch the video walkthrough below to learn how to manage global responses in AI-Console:

    <iframe width="560" height="315" allow="fullscreen *" src="https://fast.wistia.net/embed/iframe/kz017a1yi7" />

    **Configurable Response Elements**

    Users can configure four data elements for each global response:

    * **Response text**: The text of the response (required)
    * **Folder path**: The hierarchy that dictates where the response resides
    * **Title**: The short-form title of the response
    * **Metadata filters**: A key and value used to specify the set of conversations for which a response is available

    <Frame>
      <img src="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-1260d78d-5635-43c9-a4a3-e2bb201a511d.png?fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=f9c2dc800835b8970844ab70358c2939" data-og-width="868" width="868" data-og-height="1194" height="1194" data-path="image/uuid-1260d78d-5635-43c9-a4a3-e2bb201a511d.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-1260d78d-5635-43c9-a4a3-e2bb201a511d.png?w=280&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=2d46db87659ac275d92b09ab1894e5cb 280w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-1260d78d-5635-43c9-a4a3-e2bb201a511d.png?w=560&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=0c4da0680b0499dda73cec25f042a607 560w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-1260d78d-5635-43c9-a4a3-e2bb201a511d.png?w=840&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=f2e528518cb5b40fae4d6752cb06a0c3 840w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-1260d78d-5635-43c9-a4a3-e2bb201a511d.png?w=1100&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=181685cb4c08631dadd73ca523be7411 1100w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-1260d78d-5635-43c9-a4a3-e2bb201a511d.png?w=1650&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=3e917eb0fba3889b0c5887916d69e365 1650w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-1260d78d-5635-43c9-a4a3-e2bb201a511d.png?w=2500&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=61f3ca3347c01e9127c37c02addd4ea4 2500w" />
    </Frame>

    **Saving and Deploying**

    Saving changes to the global response list or uploading a new list creates a new version. Past versions can also be viewed and restored as needed.

    The global response list can be easily deployed into testing or production environments, with an indicator at the top of each version showing the status of the response list (e.g. Live in production).

    <Frame>
      <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-aeb37fd0-b374-4ffd-7cc1-35cf8f7fa4d8.png?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=2bb0737aa84ceef886c8917d389a7c37" data-og-width="980" width="980" data-og-height="428" height="428" data-path="image/uuid-aeb37fd0-b374-4ffd-7cc1-35cf8f7fa4d8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-aeb37fd0-b374-4ffd-7cc1-35cf8f7fa4d8.png?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=897ea011d072c7e4990603b4b0246bbb 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-aeb37fd0-b374-4ffd-7cc1-35cf8f7fa4d8.png?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=e1298f167344820114192315ef86ecb9 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-aeb37fd0-b374-4ffd-7cc1-35cf8f7fa4d8.png?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=f37b60a2c68cb725c437b61590f2c676 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-aeb37fd0-b374-4ffd-7cc1-35cf8f7fa4d8.png?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=850954d109487b523a8097e7fae0fd98 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-aeb37fd0-b374-4ffd-7cc1-35cf8f7fa4d8.png?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=969ae1c63fc91eb04718bedebe74366f 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-aeb37fd0-b374-4ffd-7cc1-35cf8f7fa4d8.png?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=b1cc48b9c5aaa0bfd40a06592f181d51 2500w" />
    </Frame>

    Visit the [Tooling Guide](/autocompose/autocompose-tooling-guide "AutoCompose Tooling Guide") for more information on using AI-Console to manage the AutoCompose global response list.

    ## FAQs

    1. **How do you access AutoCompose in AI-Console?**

       Provided that you have permission to access AutoCompose in AI-Console, it will appear in the AI Services section of your homepage.
       To access AutoCompose from any other AI-Console page, select the menu icon in the top left corner and then select AutoCompose.

    2. **How does response metadata work?**

       AutoCompose uses response metadata in two main ways:

       * **As a data insert:** Variable metadata such as customer name or time of day is dynamically inserted into templated response text when a suggestion is made to the agent. Read more about templated responses in the AutoCompose Product Guide Features
       * **As a filter:** Responses are only made available for suggestion when the conversation's metadata matches the attribute set for a given response (e.g. a response only being available when `queue` = `general`).

       <Note>
         Agent first name, customer first name and time of day inserts are available by default. Consult your ASAPP account team for assistance with adding metadata for use as an insert or a filter.
       </Note>

    3. **How can I search the list for specific responses?**

       There is a search bar to look up specific words from response text. Dropdown menus can also be used to filter by folder path and metadata filter.
  </Accordion>
</Update>

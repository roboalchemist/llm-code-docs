# Source: https://developers.webflow.com/designer/reference/app-intents-and-connections.mdx

***

title: App Intents and Connections
slug: designer/reference/app-intents-and-connections
description: >-
Use App Intents and Connections to launch Apps directly from a user's workflow
in the Webflow Designer
hidden: true
'og:title': 'Webflow Designer API: App Intents and Connections'
'og:description': >-
Use App Intents and Connections to launch Apps directly from a user's workflow
in the Webflow Designer
-----------------------

Make your Apps more discoverable in the Designer with App Intents and Connections.

Use App Intents and Connections to give users more opportunities to find and launch your App in the designer. These features display links to your App in contextual locations like the 'Element Settings' panel, creating smoother and more relevant interactions when users are creating and editing elements on their sites.

<Tabs>
  <Tab title="App Intents">
    App Intents make your App discoverable when users create or modify elements. By adding an Intent to your App's `webflow.json` file, users will be prompted to use your App for managing element settings directly within their existing workflow. Adding an intent allows your App to stand out as a relevant tool in the Designer.
    ![App Intents](https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/96ba921c7895e12f2afb0708d042a25ce90de0d6d6bb6d18369c75296242b950/assets/images/app-intent-image.png)
  </Tab>

  <Tab title="App Connections">
    App Connections link elements to your App via the Designer APIs. Once a connection is established, a button highlighting your App appears in the element's settings panel, prompting users to launch your App for managing element-specific settings.

    ![App Connections](https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/84241e15ed6e4742fd27e37578396bacd01a31b558f322ec9a083f2a88856193/assets/images/app-connection-image.png)
  </Tab>
</Tabs>

<Note title="Supported Elements">
  App Intents and connections currently supports the following elements:
  `Image`, `FormForm`, and `FormWrapper`.
</Note>

## How App Intents and Connections work

<AccordionGroup>
  <Accordion title="App Intents">
    When your App is configured to use App Intents for a supported element, your App will appear in the "Connections" section in an element's settings panel.

    If a user has already installed your App to their site, but aren't already using connections to manage their elements, they'll see a "Connections" section in the element settings panel. If they click the "+" button in this section, they'll see your App listed in the "Connect an App" section.

    <Frame>
      <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/f7f757f5f7c96eaec80ab142dd51769e8f542502913cf3d131623c8b5c9512a2/assets/images/app-intents-no-connection-found.png" alt="Connect an App" />

      <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/de394466b893a030a6cdd550c2836b38b04d247a1c39e044f236865e77670a82/assets/images/app-intents-connect-an-app.png" alt="App Intents" />
    </Frame>

    When your App launches from the element settings panel, your App will receive important context about the element that triggered the launch, which you can access using the [`getLaunchContext()`](/designer/reference/get-launch-context) method.

    Use this context to show the most relevant interface for a user's workflow.

    <Frame caption="We've configured the API Playground to use App Intents for the Image element. When the API Playground is launched from the Element Settings Panel, the App will show the launch context in an info box and preselect the API Category to 'Elements' and the API Method to `getAltText()` ,">
      <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/5b75d1b0956a30c4974a38fe85afe464313da169632d30de3f212daa1d6afbd6/assets/images/api-playground-launch-context.png" />
    </Frame>
  </Accordion>

  <Accordion title="App Connections">
    App Connections establish links between supported elements and your App. Using the [`element.setAppConnection()`](/designer/reference/set-app-connection) method, you can create a direct connection that prompts users to manage that element's settings through your App. For example, you can connect an image element to your App so users choose to manage assets and alt text in your App rather than managing the settings themselves.

    ![App Connections](https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/e8eda5bfd0808ae08ec1f49d8a918ea5d2861b015b25ffd721e9ca37f70f7613/assets/images/set-app-connection-diagram.png)

    When your App creates a connection with an element:

    * Webflow adds a button in the element's settings panel to launch your App
    * Webflow opens your App with context about the specific element

    Your App knows exactly which element launched it and can instantly show the most relevant interface for a user's workflow. Instead of dropping users at your App's home screen, you can welcome them with the tools and settings they need for that specific element; creating a personalized entrance for every connected element.

    ![App Connection Button](https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/898884ced7aa62819e5ceaf253ef864cd4132fbe813ff7d01d7231dc6e5ff6a3/assets/images/app-connections-open.gif)

    <Info title="Try App Connections on Your Site">
      Explore App Connections firsthand. [Download and run our example App](https://github.com/Webflow-Examples/app-connections-tester) on your site to see how it integrates directly into your workflow.

      <a href="https://github.com/Webflow-Examples/app-connections-tester">
        <button class="button cc-primary">Test App Connections</button>
      </a>
    </Info>
  </Accordion>
</AccordionGroup>

## Setting up App Intents and Connections

In the steps below, we'll walk through the following:

<Accordion title="1. Configuring your App">
  With the addition of App Intents and Connections, your [`webflow.json`](/designer/reference/app-settings) can now use two additional properties: `appIntents` and `appConnections`.

  ### Adding App Intents

  In [`webflow.json`](/designer/reference/app-settings), add a new property called `appIntents`. Create an object with a key for each element type you'd like to support. Each key should have a value of an array of strings, where each string is a unique identifier for an App Intent.

  <Note>
    As we improve support for more elements and intents, you'll be able to add them to your App Intents list.
  </Note>

  ```json webflow.json
  {
      "appIntents": {
          "image": ["manage"],
          "form": ["manage"]
      }
  }
  ```

  Once this is added to your `webflow.json`, your App will appear in the "Connections" section of the supported elements' settings panels.

  ### Adding App Connections

  In [`webflow.json`](/designer/reference/app-settings), add a new property called `appConnections`. Set it to an array of strings, where each string is a unique identifier for an App Connection.

  ```json webflow.json
  {
    "appConnections": ["manageImageElement", "manageFormElement"]
  }
  ```
</Accordion>

<Accordion title="2. Listening for Launch Context from an App Intent">
  When your App launches from the element settings panel, Webflow will send information about how your App was launched back to your App. To get this information, you'll need to listen for launch context from the Webflow Designer by calling the [`getLaunchContext()`](/designer/reference/get-launch-context) method.

  When your App is launched from an App Intent, [`getLaunchContext()`](/designer/reference/get-launch-context) returns an object with the following structure:

  ```typescript
  type LaunchContext = {
      type: 'AppIntent';
      value: {
          image: 'manage'; // Will only be present if the App Intent is for managing images
          form: 'manage'; // Will only be present if the App Intent is for managing forms
      };
  };
  ```

  It's most appropriate to call [`getLaunchContext()`](/designer/reference/get-launch-context) on the main page of your App, such as the entry point of a React App.

  ```typescript main.tsx{9}
  // Initialize state to store the launch context
  const [launchContext, setLaunchContext] = React.useState(null);

  React.useEffect(() => {
      // Define async function to fetch launch context
      async function onLoad() {

          // Get context from Webflow Designer when App is launched
          const context = await webflow.getLaunchContext();
          setLaunchContext(context); // Update state with the received context

          // Determine which page to show based on launch context
          if (context?.type === 'AppIntent') {
              if (context.value?.image === 'manage') {
                  navigate('/image-manager');
              } else if (context.value?.form === 'manage') {
                  navigate('/form-manager');
              } else {
                  navigate('/');
              }
          } else {
              navigate('/');
          }
      }

      // Call onLoad immediately when component mounts
      onLoad();
  }, []); // Empty dependency array means this effect runs once on mount
  ```
</Accordion>

<Accordion title="3. Create an App Connection">
  Now that you've retrieved the launch context, you can access the details of the element that launched your App. From there, you can [create an App Connection](#setting-up-an-app-connection) to the element so that users are prompted to use your App each time they open that element's settings panel.

  Since an element will always be selected in the Designer when accessing its settings, you can simply call the [`getSelectedElement()`](/designer/reference/get-selected-element) method to get the element that launched your App. Then you can create an App Connection to the element using the identifier you configured in [`webflow.json`](/designer/reference/app-settings).

  ```tsx main.tsx{13,19,22}
  // Initialize state to store the launch context and selected element
  const [launchContext, setLaunchContext] = React.useState(null);
  const [selectedElement, setSelectedElement] = React.useState(null);

  React.useEffect(() => {
      // Define async function to fetch launch context and selected element
      async function onLoad() {
          // Get context from Webflow Designer when App is launched
          const context = await webflow.getLaunchContext();
          setLaunchContext(context); // Update state with the received context

          // Get and set the selected element
          const element = await webflow.getSelectedElement();
          setSelectedElement(element);

          // Set the App Connection based on element type and determine which page to show your user
          if (context?.type === 'AppIntent') {
              if (context.value?.image === 'manage') {
                  await element.setAppConnection('manageImageElement');
                  navigate('/image-manager');
              } else if (context.value?.form === 'manage') {
                  await element.setAppConnection('manageFormElement');
                  navigate('/form-manager');
              } else {
                  navigate('/');
              }
          } else {
              navigate('/');
          }
      }

      // Call onLoad immediately when component mounts
      onLoad();
  }, []); // Empty dependency array means this effect runs once on mount
  ```
</Accordion>

<Accordion title="4. Listening for Launch Context from an App Connection">
  As with App Intents, when your App is launched from an App Connection, Webflow will send information about how your App was launched back to your App. To get this information, you'll need to listen for launch context from the Webflow Designer by calling the [`getLaunchContext()`](/designer/reference/get-launch-context) method.

  When launched from an App Connection, the LaunchContext object will have the following structure:

  ```ts
  type LaunchContext = {
      type: 'AppConnection';
      value: string; // The identifier for the App Connection
  };
  ```

  Let's reconfigure our App to listen for launch context from either an App Intent or App Connection.

  ```ts main.tsx {9,28}
  // Initialize state to store the launch context and selected element
  const [launchContext, setLaunchContext] = React.useState(null);
  const [selectedElement, setSelectedElement] = React.useState(null);

  React.useEffect(() => {
      // Define async function to fetch launch context and selected element
      async function onLoad() {
          // Get context from Webflow Designer when App is launched
          const context = await webflow.getLaunchContext();
          setLaunchContext(context); // Update state with the received context

          // Get and set the selected element
          const element = await webflow.getSelectedElement();
          setSelectedElement(element);

          // Handle different launch contexts
          if (context?.type === 'AppIntent') {
              // Handle App Intent launches
              if (context.value?.image === 'manage') {
                  await element.setAppConnection('manageImageElement');
                  navigate('/image-manager');
              } else if (context.value?.form === 'manage') {
                  await element.setAppConnection('manageFormElement');
                  navigate('/form-manager');
              } else {
                  navigate('/');
              }
          } else if (context?.type === 'AppConnection') {
              // Handle App Connection launches
              switch (context.value) {
                  case 'manageImageElement':
                      navigate('/image-manager');
                      break;
                  case 'manageFormElement':
                      navigate('/form-manager');
                      break;
                  default:
                      navigate('/');
              }
          } else {
              // Handle direct launches (not from Intent or Connection)
              navigate('/');
          }
      }

      // Call onLoad immediately when component mounts
      onLoad();
  }, []); // Empty dependency array means this effect runs once on mount
  ```
</Accordion>

<Accordion title="5. Listing App Connections">
  If your App manages multiple resources, you may want to organize and list them in your App for users to reference. You can retrieve a list of all App Connections for a given element using the [`getAppConnections()`](/designer/reference/get-app-connections) method on an individual element.

  To do this, let's get a list of all elements on the page and then retrieve the App Connections for each element.

  ```ts
  async function findConnectedElements() {
      // Get all elements on the page
      const elements = await webflow.getAllElements();
      const connectedElements = [];

      // Iterate through elements and check for connections
      for (const element of elements) {
          try {
              // Check if element supports App Connections
              if (element.getAppConnections) {
                  const connections = await element.getAppConnections();

                  // If element has connections, store it with relevant info
                  if (connections && connections.length > 0) {
                      connectedElements.push({
                          connections,
                          type: element.type,
                          id: element.id
                      });
                  }
              }
          } catch (error) {
              console.error(`Error checking connections for element: ${element.id}`, error);
          }
      }

      return connectedElements;
  }
  ```
</Accordion>

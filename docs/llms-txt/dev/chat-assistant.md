# Source: https://dev.writer.com/framework/chat-assistant.md

# Chat assistant

In this tutorial, you'll use the Writer Framework to create a simple yet powerful chat assistant that can engage in conversations on various topics, provide answers to your questions, and maybe even help you when you're experiencing writer's block!

The process will take only minutes using a drag-and-drop visual editor to build the user interface and Python for the back-end code.

Here's what the finished project will look like:

<img src="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_1.png?fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=0c3c814df95473821d822abc1c883f92" alt="Finished chat assistant project" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/chat/chat_assistant_1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_1.png?w=280&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=fa7bca35d56c24e51601aff02f8713b7 280w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_1.png?w=560&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=de595a50ea49b2c4e93c9e8432ae001a 560w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_1.png?w=840&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=bac921d51aaf59d4b98ea0b3e18059b4 840w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_1.png?w=1100&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=0fd285e58aa58a4a8b128de62e5f7f10 1100w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_1.png?w=1650&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=604ef672be0e1d080707bca27436eab7 1650w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_1.png?w=2500&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=1152510dac531569252a4b5432e1ed1b 2500w" />

## Prerequisites

Before starting, ensure you have:

* **A Writer account:** You don't need an account to use Writer Framework, but you'll need one to use the AI module. [Sign up for a free account here](https://app.writer.com/register).
* **Python 3.9.2 or later**: Use the installer from [python.org](https://www.python.org/downloads/).
* **pip:** This command-line application comes with Python and is used for installing Python packages, including those from Writer.
* **A basic understanding of Python:** You should be familiar with the basics of the language.
* **Your favorite code editor (optional):** There's a code editor built into Writer for editing back-end code, but you can also use Visual Studio Code, Notepad++, Vim, Emacs, or any text editor made for programming if you prefer.

## Setting up your project

### Create a Writer app and get its API key

First, you'll need to create a new app within Writer.

<Steps>
  <Step title="Create the app in Writer">
    Log into Writer. From the Home screen, click on the **Build an app** button.

        <img src="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2.png?fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=580c843c75a49b10e62d893751849a7e" alt="Writer home screen" data-og-width="3220" width="3220" data-og-height="1900" height="1900" data-path="framework/images/tutorial/chat/chat_assistant_2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2.png?w=280&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=14da42dfdd22f5a3c7c088ba7e004827 280w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2.png?w=560&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=a162e3880d6802253d60c81a642f5cdb 560w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2.png?w=840&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=67ea4b3646ba0d811cbd14ad5e1c793d 840w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2.png?w=1100&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=d28d6e6897cebb901811cc182187aa79 1100w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2.png?w=1650&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=ffaead4db6e120663c824ee5eeb385d3 1650w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2.png?w=2500&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=7d3c7cef527973e07c6fbf1130998ea2 2500w" />

    The **Start building** menu will appear, presenting options for the types of apps you can create.

    Select **Framework**, located under **Developer tools**. This will create a brand new app based on Writer Framework.

        <img src="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_3.png?fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=43c43a9a53829617c068bf5d37e9c36d" alt="&#x22;Start building&#x22; menu" data-og-width="3220" width="3220" data-og-height="1900" height="1900" data-path="framework/images/tutorial/chat/chat_assistant_3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_3.png?w=280&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=b13af18582ffd2532fd5154b49e52eca 280w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_3.png?w=560&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=781336993d597dafe61f0e377c463d98 560w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_3.png?w=840&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=611adc83c03d3f3d40066c61091d5650 840w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_3.png?w=1100&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=280bb75fe6f9fea8859ed4938e57be5b 1100w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_3.png?w=1650&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=0d9057a9cac49933b974a5c412620c05 1650w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_3.png?w=2500&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=119efe8d7d02a00b2329db578f9740eb 2500w" />
  </Step>

  <Step title="Copy your app's API key">
    On the next screen, titled **How to deploy an application**, you can get the API key for the app by clicking on the **Reveal key** button, located under the text **Authenticate with an API key**. Your complete API key will be displayed, and a "copy" button will appear. Click this button to copy the key; you'll use it in the next step.

        <img src="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2a.png?fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=427ce6f509ecfa7fdbc8f44c8b0f7404" alt="&#x22;How to deploy an application&#x22; page" data-og-width="3203" width="3203" data-og-height="2000" height="2000" data-path="framework/images/tutorial/chat/chat_assistant_2a.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2a.png?w=280&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=047939ffccef0d1a710dd393fe2f68e0 280w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2a.png?w=560&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=5df4d481e871669d8f64f98b7ca8a97b 560w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2a.png?w=840&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=010823e4cd6909f83012d667aea0470c 840w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2a.png?w=1100&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=32896a96beebe05859f1c7932519e8cb 1100w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2a.png?w=1650&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=792d2c91266c5f53137e4ecda4ca1727 1650w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2a.png?w=2500&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=464eed68c1fdbbdf42c5a69e38e59602 2500w" />
  </Step>
</Steps>

### Set up your computer and create the app's project

The next step is to set up the Writer Framework environment on your computer. You'll do this by creating a directory for the project, installing dependencies, and creating the project for the application using a template.

<Steps>
  <Step title="Open your terminal application">
    Open your terminal application. On macOS and Linux, this application goes by the name *Terminal*; on Windows, you can use either *Windows PowerShell* (which is preferred) or *Command Prompt*.
  </Step>

  <Step title="Install the dependencies">
    <Note>If you already have the `writer` and `python-dotenv` packages installed on your computer, you can skip this step.</Note>

    Install the `writer` and `python-dotenv` packages by entering the following commands in your terminal application:

    ```
    pip install writer python-dotenv
    ```

    This command tells `pip`, the Python package installer, to install two packages:

    * `writer`, which provides some command-line commands and enables Python code to interact with Writer and the Writer Framework.
    * `python-dotenv`, which makes it easy to manage environment variables by loading them from a `.env` file. This one is optional for this exercise, but you might find it useful when working on larger projects.
  </Step>

  <Step title="Set the API key environment variable">
    To pass your API key to the Writer Framework, you need to set an environment variable called `WRITER_API_KEY`.

    Select your operating system and terminal application below, then copy and paste the command into your terminal application, replacing `[your_api_key]` with the API key you copied earlier:

    <CodeGroup>
      ```sh macOS/Linux (Terminal) theme={null}
      export WRITER_API_KEY=[your_api_key]
      ```

      ```sh On Windows (Windows PowerShell) theme={null}
      $env:WRITER_API_KEY=[your_api_key]
      ```

      ```sh On Windows (Command Prompt) theme={null}
      set WRITER_API_KEY=[your_api_key]
      ```
    </CodeGroup>

    The `WRITER_API_KEY` environment variable will remain defined as long your terminal session is open (that is, until you close your terminal application’s window).
  </Step>

  <Step title="Create the project">
    Create the project by entering this command into your terminal application:

    ```
    writer create chat-assistant --template=ai-starter
    ```

    This command sets up a new project called `chat-assistant` using a starter template called `ai-starter` so that you're not starting "from scratch."
  </Step>
</Steps>

## Build the UI

Now that you've created the project, it's time to define the UI. The Writer Framework's drag-and-drop capabilities make it easy — even if you haven't done much UI work before!

The project editor is a web application that runs on your computer and enables you to define and edit your app's user interface. Launch it by typing the following into your terminal application:

```
writer edit chat-assistant
```

You'll see a URL. Control-click it (command-click on macOS) to open it, or copy the URL and paste it into the address bar of a browser window.

The browser window will contain the project editor, which will look like this:

<img src="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2b.png?fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=75f2df9ca6f896d9461ed2604b58d398" alt="Project editor" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/chat/chat_assistant_2b.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2b.png?w=280&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=b77d621f498144591ed98523c2c0fdfe 280w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2b.png?w=560&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=0d5153d85cfb377525842350316c92fa 560w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2b.png?w=840&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=4a255114f8905ce23c6b0d0d064972fa 840w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2b.png?w=1100&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=a776c47f01c836d8c4fd1c17dd71b2fb 1100w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2b.png?w=1650&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=08ac862758105c5748666a8b5efe00d9 1650w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2b.png?w=2500&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=e04cb051c6e2bbc9b1c3d97d4bf676ee 2500w" />

You'll see the following:

* The **canvas** is in the center. It displays the app's user interface.
* The column on the left contains:
  * The **Core toolkit**, which contains all the UI components. You define the user interface by dragging components from the Toolkit and placing them on the canvas.
  * The **Component tree**, which shows the arrangement of the UI components on the canvas. It's also useful for selecting items on the canvas, especially when it has a lot of UI components.

It's time to build the UI!

<Steps>
  <Step title="Examine the header">
    Select the **Header** component by clicking it — it's the component at the top, containing the title **AI STARTER** and a gray area labeled **Empty Header**.

    When you click it, you'll see the **properties** panel appear on the right side of the page. This lets you view and edit the properties of the selected component.

        <img src="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2c.png?fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=30ee76df7d06491491699e17d0c7e64b" alt="The selected header and its properties panel" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/chat/chat_assistant_2c.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2c.png?w=280&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=0576f4bf2e5a1224ad01d2b8c3faf698 280w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2c.png?w=560&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=895bb16475579114cee9e3f3a8500be3 560w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2c.png?w=840&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=1ef9edce99ddfc64296bf0022c070a90 840w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2c.png?w=1100&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=3d40579ccefad716025870fc0f15f909 1100w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2c.png?w=1650&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=fc1572d84faaa5e022c0cf612db835ed 1650w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2c.png?w=2500&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=60ed2e9a7934bd08a04e6e34bb6939ec 2500w" />

    The first property you'll see in the panel is the **Text** property, which defines the text that appears as the header's title. It should contain the value `@{my_app.title}`. The `@{` and `}` indicate that `my_app.title` is a variable and that its contents should be the text displayed instead of the literal text "my\_app.title". You'll set the value of this variable soon.
  </Step>

  <Step title="Clear the Section's default title">
    Select the **Section** component by clicking it — it's just below the **Header** component and contains the title **Section Title** and a gray area labeled **Empty Section**.

    In the **properties** panel, clear out the value of the **Title** property. This will remove the **Section**'s default title.

        <img src="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2d.png?fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=188d524f61e214d47483571614ed6fd9" alt="The selected section and its properties panel" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/chat/chat_assistant_2d.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2d.png?w=280&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=0a6a31b1429c6bfd0b44f05524b934b9 280w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2d.png?w=560&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=fa2ef1e1fd4f4c10a3e3f348e6afc3e7 560w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2d.png?w=840&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=7bf3e3f25d4828e0d5d0d135129031cf 840w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2d.png?w=1100&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=4d056521caeea8510ffe192bcd428110 1100w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2d.png?w=1650&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=870a4aed11c18832e5ad6cbed17b0e66 1650w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2d.png?w=2500&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=8870fc19667eb73443b9a9c52e499c8d 2500w" />
  </Step>

  <Step title="Add a Text component to the Section">
    Drag a **Text** component from the **Core toolkit** panel on the left (it's under **Content**, and you may need to scroll down a little to find it) and into the *Section*. Sections can act as containers for other components.

    <Note>You can search for a specific component by using the search bar at the top of the **Core toolkit** panel.</Note>

    Select the **Text** component. In the **properties** panel, set the **Text** property to provide instructions or context for your chat assistant. Here's an example: `Welcome to the Chat Assistant. Ask me anything!`

        <img src="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2e.png?fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=fc1c5e1409d44ea510ea6ef0af471d7a" alt="The text component and its properties panel" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/chat/chat_assistant_2e.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2e.png?w=280&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=bb5239380e6d4fb29cb8f693442523f2 280w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2e.png?w=560&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=0170baa8c1da2508663fc62750b13a23 560w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2e.png?w=840&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=2a26f3935c76448f148715f4bece8783 840w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2e.png?w=1100&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=17f768353cf3b3de2a26e3261eccee98 1100w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2e.png?w=1650&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=054ddc499076c6913cd41bf0705994de 1650w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2e.png?w=2500&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=94e710e45bd90a36044380cd143d0df2 2500w" />
  </Step>

  <Step title="Add a Chatbot component to the Section">
    The heart of this app is the **Chatbot** component, a pre-built component that displays the conversation between the LLM and the user and provides a text field where the user can enter prompts.

    Drag a **Chatbot** component from the **Core toolkit** panel (it's under **Content**) into the *Section*, just below the Text box.

        <img src="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2f.png?fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=7bd7ea78e5115c2057646121dee641eb" alt="The chatbot component" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/chat/chat_assistant_2f.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2f.png?w=280&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=6ae6ed95e83a07525ccfe9da191d935c 280w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2f.png?w=560&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=3ded210ea2a9a456ac662a71775dcdc6 560w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2f.png?w=840&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=b497a7bad8c00a432900231036b1d594 840w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2f.png?w=1100&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=49783436f65acccccdcf4a22f5bc5a4e 1100w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2f.png?w=1650&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=e2ccb824adfe48fe25faad8d9a769529 1650w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2f.png?w=2500&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=ce7760e4a68e38d89f08acacb45549ae 2500w" />
  </Step>
</Steps>

## Add the back-end code

With the UI laid out, it's time to work on the logic behind it.

The logic behind the user interface is defined in a file named `main.py`, which is in your project's directory. This file was automatically generated; you'll update the code in it to define the behavior of your app.

The simplest way to edit `main.py` is within the project editor. Click on the "toggle code" button (beside the word **Code**) near the lower left corner of the project editor page.

<img src="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2g.png?fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=16baa189672daa68f3d956dc3053a348" alt="Project editor with arrow pointing to toggle code button" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/chat/chat_assistant_2g.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2g.png?w=280&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=8a9ea12f46e5d4b478c11b27a4d2f77c 280w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2g.png?w=560&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=c40facf483b26c9062bc181cdcae6d02 560w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2g.png?w=840&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=09ecf7e655989a91cf5255ad7489faf3 840w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2g.png?w=1100&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=7173f0edfca6bc95635c17ea5ea986e7 1100w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2g.png?w=1650&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=6b4615255f37ab071f055ef62aaaf74f 1650w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2g.png?w=2500&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=4d15816852ab9880ff9353a2d2bcb336 2500w" />

A pane with the name **Code** will appear at the bottom half of the screen, displaying an editor for the the contents of `main.py`.

<img src="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2h.png?fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=e82dd26da8afd23ea8f48ee8f949f105" alt="Project editor with the code editor displayed" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/chat/chat_assistant_2h.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2h.png?w=280&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=b708c023eb3cd0db9b5c5e70395a0f0d 280w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2h.png?w=560&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=2b1b97ff4a58f4e9805b4a6cc335eb59 560w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2h.png?w=840&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=6af325b8cff48665f1d5f745e33df2c1 840w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2h.png?w=1100&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=3a36b31d085e49c94fab9d947986151a 1100w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2h.png?w=1650&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=ac9656038560f29817850d8fc0c46b4b 1650w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2h.png?w=2500&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=89f33d9a27a473fab4b2a4ee30811a2c 2500w" />

<Note>If you'd rather use a code editor instead of coding in the browser, use it to open the `main.py` file in your project's directory.</Note>

Now follow these steps:

<Steps>
  <Step title="Import libraries and load the Writer Framework API key">
    You should see the following at the start of the file:

    ```python  theme={null}
    import writer as wf
    import writer.ai
    ```

    Replace that code with the following:

    ```python  theme={null}
    import os
    import writer as wf
    import writer.ai

    # Set the API key
    wf.api_key = os.getenv("WRITER_API_KEY")
    ```

    This code imports the libraries that the application will need and then reads your Writer Framework API key in the `WRITER_API_KEY` environment variable.
  </Step>

  <Step title="Create a handler to respond to the user's input">
    The application needs a function to handle incoming chat messages. Find these comments in the code...

    ```python  theme={null}
    # Welcome to Writer Framework! 
    # This template is a starting point for your AI apps.
    # More documentation is available at https://dev.writer.com/framework
    ```

    ...and replace them with the following function:

    ```python  theme={null}
    def generate_completion(state, payload):
      print(f"Here's what the user entered: {payload['content']}")
      state["conversation"] += payload
      print(f"Conversation: {state['conversation'].messages}")
      try:
          for index, chunk in enumerate(state["conversation"].stream_complete()):
              print(f"Chunk {index}: {chunk}")
              if not chunk.get("content"):
                  chunk["content"] = ""
              state["conversation"] += chunk
              
          print(f"state['conversation']:\n{state['conversation'].messages}")
      except Exception as e:
          print(f"Error during stream_complete: {e}")
    ```

    The `generate_completion()` function will be called when the user enters a prompt, which is contained in the `payload` object. The `payload` object is added to the `conversation` object contained in the application's `state`, which adds the user's prompt to the record of the conversation between the user and the LLM.

    After adding the user's prompt to the conversational record, `generate_completion()` calls the `conversation` object's `stream_complete()` method, which generates an LLM completion based on the conversation so far. As its name implies, `stream_complete()` returns the completion as a stream of text chunks, which are captured and added to the `conversation` object.

    <Note>The `conversation` object in the code above is an instance of Writer’s `Conversation` class. You can find out more about this class on our [*Writer AI module*](https://dev.writer.com/framework/ai-module) page.</Note>

    Note that `generate_completion()` completion uses a lot of `print()` functions for debugging purposes, and you can use them to get a better idea of what's happening in the function. You'll see their output in both your terminal application and in the project editor's 'log' pane (which will be covered shortly) as you use the chat assistant. This output will include:

    * The prompt the user entered
    * The chunks of data that make up the LLM's response as they are generated
    * The record of the conversation between the user and the LLM.

    The `print()` functions don't affect the operation of the chat assistant in any way, and you can remove them if you wish.
  </Step>

  <Step title="Initialize the application">
    The final step is to set the application's initial state. Find this code, which should be just after the `generate_completion()` function...

    ```python  theme={null}
    # Initialise the state
    wf.init_state({
        "my_app": {
            "title": "AI STARTER"
        },
    })
    ```

    ...and replace it with this:

    ```python  theme={null}
    # Initialize the state
    wf.init_state({
        "conversation": writer.ai.Conversation(),
        "my_app": {
            "title": "CHAT ASSISTANT"
        },
    })
    ```

    The Writer Framework's `init_state()` method sets the initial value of `state`, a dictionary containing values that define the state of the application. The key-value pairs in `state` are how you store values used by your app and how you pass data between the back-end code and the UI.

    The code above sets the initial value of `state` so that it has two key-value pairs:

    * `conversation`: An object that keeps a record of the conversation that the user is having with the LLM. You'll bind its value to the **Chatbot** component soon.
    * `my_app`: A dictionary containing values that define the application's appearance. This dictionary has a single key-value pair, `title`, which defines the text that appears as the application's title in the **Header**.

    <Note>For more details about the `state` variable, see our [*Application state*](https://dev.writer.com/framework/application-state#application-state) page.</Note>
  </Step>

  <Step title="Save the updated code and hide the code editor">
    That’s all the code. If you edited the code in the browser, save it by clicking the “save” button near the top right corner of the code editor.

        <img src="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2i.png?fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=0a10aed680c79ebfcb54b5d679d16d84" alt="Project editor and code editor, with arrow pointing to save button" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/chat/chat_assistant_2i.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2i.png?w=280&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=f10e18a6fad936845d065e48bf840532 280w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2i.png?w=560&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=49e455e8092baeb7ad37b0be0fd0706b 560w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2i.png?w=840&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=7e4f1af58e861096beb392925a0b61da 840w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2i.png?w=1100&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=eb5e2c6c90597f7468d571ad94566389 1100w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2i.png?w=1650&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=3bb55201c963d3c01f9dbed767313f39 1650w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2i.png?w=2500&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=1faf72c274e4a6d5566afe26abfc949b 2500w" />

    Click the "toggle code" button to hide the code editor.
  </Step>
</Steps>

## Bind the UI to the back-end code

You've built the UI and written the code behind it. Let's connect the two! Go back to the browser window with the project editor and do the following:

<Steps>
  <Step title="Observe that the heading at the top of the app is now 'CHATBOT ASSISTANT'">
    Earlier, you saw that the **Header** component's **Text** property was set to `@{my_app.title}`, a value in the app's `state` variable. You changed this value when you update the call to the Writer Framework's `init_state()` method.
  </Step>

  <Step title="Bind the Chatbot component to the 'state' variable's 'conversation' key">
    Recall that the `conversation` object contained within the `state` variable contains the record of the conversation that the user is having with the LLM. Binding the **Chatbot** component to this object allows it to display the conversation to the user.

    Select the **Chatbot** component. In the **properties** panel, find the **Conversation** property and set its value to `@{conversation}`.

        <img src="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2j.png?fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=03d1547aad9b8898fc274a285434bb26" alt="Updating the Chatbot's conversation property" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/chat/chat_assistant_2j.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2j.png?w=280&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=2e17c8dc02d7b894493fc3a706bb5757 280w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2j.png?w=560&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=0994af3d8451405925c72db97e2747c1 560w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2j.png?w=840&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=cbb9a2dd8094a16f740bfc99ff95d71f 840w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2j.png?w=1100&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=fa84cb3e80c4f29f65b90def4cfb9c19 1100w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2j.png?w=1650&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=b886ea51b9fc2e678b105ddc2385fe79 1650w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2j.png?w=2500&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=80b8003366d8ccbd55463a68d0cecefa 2500w" />

    The value `@{conversation}` specifies that the **Chatbot** component should get its information from the value corresponding to the `conversation` key in the application's `state` variable.
  </Step>

  <Step title="Specify the Chatbot component's event handler">
    You need to specify that the **Chatbot** component should call the `generate_completion()` function when the user enters a prompt.

    Do this by scrolling down the **properties** panel to the **Events** section until you see a property called **`wf_chatbot_message`**. Select **`generate_completion`** from its menu.

        <img src="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2k.png?fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=5a9ddfbaa789a46bf3dd26c889038588" alt="Updating the Chatbot's wf_chatbot_message property" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/chat/chat_assistant_2k.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2k.png?w=280&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=8221f0cadc49673cbe559622362b15b9 280w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2k.png?w=560&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=90a2ed74e8cb9951bc553488a7d1b527 560w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2k.png?w=840&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=a0f1e4e70dc8999abbe81ad4483efa34 840w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2k.png?w=1100&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=b55ecb5795e0773ffd004908cc69b72b 1100w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2k.png?w=1650&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=dd26464d92711581a6967a954f2b2580 1650w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2k.png?w=2500&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=c93b80f9980ab0663aab4f1262eb42ad 2500w" />
  </Step>
</Steps>

## Test the application

You've completed all the steps to make a working chat assistant, and you can try using it right now, even while editing the user interface!

Try entering some prompts into the text entry at the bottom of the **Chatbot** component. The LLM should respond accordingly:

<img src="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2l.png?fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=3fde15b8d95e47d25d9200b33becdb91" alt="The chat assistant, with the project editor in &#x22;UI&#x22; mode" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/chat/chat_assistant_2l.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2l.png?w=280&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=c93159237969855506c096a1bb349e10 280w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2l.png?w=560&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=b8d58177872af89fa8f10a49461c5949 560w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2l.png?w=840&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=7fa2406ae9d1af581825b6c6f0665372 840w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2l.png?w=1100&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=e73b6e7de0dcd6575ea8b61d51a35833 1100w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2l.png?w=1650&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=ab030b0090a21c2cb96104b781794275 1650w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2l.png?w=2500&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=812879050adb0606eda9e88e027dd337 2500w" />

To get a better sense of what the experience will be like for the user, switch to the preview by changing the edit mode (located near the upper left corner of the page) from *UI* mode to *Preview* mode by selecting the **Preview** option:

<img src="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2m.png?fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=7634299b9d42ca51e53b36aa8ff6a172" alt="The project editor with an arrow pointing to the Preview button" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/chat/chat_assistant_2m.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2m.png?w=280&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=1cad128f9a48d4d8b78f1188a75cf68d 280w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2m.png?w=560&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=44593deded18c61695783a9e5f219e30 560w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2m.png?w=840&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=eeae0e06dce428d535a46f246286b6f1 840w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2m.png?w=1100&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=ff719f92a98d884bee628287c3bd5988 1100w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2m.png?w=1650&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=6078067c552b25055f2a04b4b903cb94 1650w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2m.png?w=2500&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=8dcca27edc7b79b6e0c9056b309e6309 2500w" />

Here’s what the app looks like in *Preview* mode:

<img src="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2n.png?fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=695a087df7fdfec75e0c3c6a2d56d77a" alt="The chat assistant, with the project editor in &#x22;Preview&#x22; mode" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/chat/chat_assistant_2n.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2n.png?w=280&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=468bd8357245c4da4557b2da6f9f564e 280w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2n.png?w=560&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=78cfeba2f270b450a06b71347de1aa68 560w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2n.png?w=840&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=bf7acefa8403db0beb2a1eb6bed04d1c 840w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2n.png?w=1100&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=4183530e5d4d3c2e7cc569c659b9a4ef 1100w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2n.png?w=1650&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=84d3fc29e1932be3d7dda3a1ea8483fb 1650w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2n.png?w=2500&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=8770674992e24df9418e38547351ed59 2500w" />

You can see the output of any `print()` functions and error messages by clicking on the **Log** button located near the upper right corner of the page:

<img src="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2o.png?fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=abccbdbea8cff7ecc7e28b71cc2f11c8" alt="The chat assistant with an arrow pointing to the Log button" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/chat/chat_assistant_2o.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2o.png?w=280&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=feb9a0e40e13607352f9ec3ddc87dfe6 280w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2o.png?w=560&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=a43936f8fb0c17e64bfcef0a9beff2de 560w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2o.png?w=840&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=f1856c39caba131ecbb800cfb86b6fb7 840w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2o.png?w=1100&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=050738a03ac4604c7d9025f837423354 1100w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2o.png?w=1650&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=e14c06910dc7f76d10b5763c31a2c265 1650w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2o.png?w=2500&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=ef73b05b3d33ae01321850192ecb9623 2500w" />

Here’s what the app looks like when displaying the log:

<img src="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2p.png?fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=7aca8100f0079306e2a7ec9e52bff79c" alt="The working chat assistant, with the log pane displayed" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/chat/chat_assistant_2p.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2p.png?w=280&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=5c4b2f270b0b9c02fcec5a3a029caeac 280w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2p.png?w=560&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=7b32270e85785a15c7ab963ff9b91074 560w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2p.png?w=840&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=ac58ab5b6d26cfff786ac1bc49fe824b 840w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2p.png?w=1100&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=aadda9390cb65db8e5a1d8e401caed45 1100w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2p.png?w=1650&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=7133138e8395379d2663a7f60dac040e 1650w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_2p.png?w=2500&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=5d4abf8af38cdff5225a6d04335a88dd 2500w" />

It's very helpful to be able to test the application while editing it. As you continue to work with Writer Framework, you'll find yourself alternating between making changes to your application and testing those changes without having to leave the project editor.

## Run the application locally

Once you've tested the application, it's time to run it locally.

Switch back to your terminal application. Stop the project editor with ctrl-c, then run the application by entering the following command:

```
writer run chat-assistant
```

Note that the command starts with `writer run` as opposed to `writer edit`. This launches the application as your users will see it, without any of the editing tools. Even though you can preview your applications in the project editor, it's still a good idea to test it by running it on your computer, outside the project editor, before deploying it.

You'll be able to access the application with your browser at the URL that appears on the command line. It should look like this:

<img src="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_1.png?fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=0c3c814df95473821d822abc1c883f92" alt="Finished chat assistant project" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/chat/chat_assistant_1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_1.png?w=280&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=fa7bca35d56c24e51601aff02f8713b7 280w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_1.png?w=560&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=de595a50ea49b2c4e93c9e8432ae001a 560w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_1.png?w=840&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=bac921d51aaf59d4b98ea0b3e18059b4 840w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_1.png?w=1100&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=0fd285e58aa58a4a8b128de62e5f7f10 1100w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_1.png?w=1650&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=604ef672be0e1d080707bca27436eab7 1650w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/chat/chat_assistant_1.png?w=2500&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=1152510dac531569252a4b5432e1ed1b 2500w" />

<Note>The Writer editor, which you launched with `writer edit chat-assistant`, and your application, which you launched with `writer run chat-assistant`, run  on the same URL, but on different *ports* (specified by the number after the `:` character at the end of the URL).</Note>

## Conclusion

That's it — you've built a functional chat assistant using the Writer Framework!

Feel free to modify this project! The Writer platform is flexible enough for you to customize, extend, and evolve your application into something completely different! To find out what else you can do, check out the documentation for [Writer Framework](https://dev.writer.com/framework/introduction) and the [Writer API](https://dev.writer.com/introduction).

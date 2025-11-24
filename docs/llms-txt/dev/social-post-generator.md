# Source: https://dev.writer.com/framework/social-post-generator.md

# Social post generator

In this tutorial, you'll use the Writer Framework to build an AI-powered tool for generating social media posts and tags based on the input you provide!

The process will take only minutes using a drag-and-drop visual editor to build the user interface and Python for the back-end code.

Here's what the finished project will look like:

<img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2ab.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=e38dd8f9a9fe0a6b6976706902b45761" alt="Finished social post generator project" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/social_post/sp_gen_2ab.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2ab.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=33377c60d8cb103cb857c06aa1a31e7e 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2ab.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=60df3811ecd7566018b07c5fe7fc36cd 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2ab.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=6341f4458526199a5e4333b3a2187728 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2ab.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=f2221fca93c548a5fbedc208e7842de6 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2ab.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=efd3624129c3b4d65434eec07b212ebb 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2ab.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=c6a0a9a8baca8a45ef096077e29a67d3 2500w" />

## Prerequisites

Before starting, ensure you have:

* **A Writer account:** You don't need an account to use Writer Framework, but you'll need one to use the AI module. [Sign up for a free account here](https://app.writer.com/register).
* **Python 3.9.2 or later**: Use the installer from [python.org](https://www.python.org/downloads/).
* **pip:** This command-line application comes with Python and is used for installing Python packages, including those from Writer.
* **A basic understanding of Python:** You should be familiar with the basics of the language.
* **Your favorite code editor (optional):** There's a code editor built into Writer for writing back-end code, but you can also use Visual Studio Code, Notepad++, Vim, Emacs, or any text editor made for programming if you prefer.

## Setting up your project

### Create a Writer app and get its API key

First, you'll need to create a new app within Writer.

<Steps>
  <Step title="Create the app in Writer">
    Log into Writer. From the Home screen, click on the **Build an app** button.

        <img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=8f7d36049df01e27d405a7f07401b8dc" alt="Writer home screen" data-og-width="3220" width="3220" data-og-height="1900" height="1900" data-path="framework/images/tutorial/social_post/sp_gen_2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=722dbfe871b173205e61e3104fdeb494 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=21ce9a596e58987a6de548951569cc86 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=f8c80ffff0051eaf9165564ec0a62732 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=f3abfcf46e416659a9f0b1589a5c9bed 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=d1190e19d88522d39088cb0ae704df30 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=ac468efbcebca5084a97b5a152cc6829 2500w" />

    The **Start building** menu will appear, presenting options for the types of apps you can create.

    Select **Framework**, located under **Developer tools**. This will create a brand new app based on Writer Framework.

        <img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_3.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=8e8988274dfd797dde727d2070948200" alt="&#x22;Start building&#x22; menu" data-og-width="3220" width="3220" data-og-height="1900" height="1900" data-path="framework/images/tutorial/social_post/sp_gen_3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_3.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=faa7d8516962e4104b57b74e4c9fc8ce 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_3.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=f3d763caf6cae9b69b443b455d22d6f4 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_3.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=55b60a12306dc62737634f3c4543cba1 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_3.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=81f140d620c610bcac9d85ffea91bcbf 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_3.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=59a3d91f4e98b5d8146e2ae37d1d2c4c 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_3.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=80e707d1223c5259803150c46f9367d0 2500w" />
  </Step>

  <Step title="Copy your app's API key">
    On the next screen, titled **How to deploy an application**, you can get the API key for the app by clicking on the **Reveal key** button, located under the text **Authenticate with an API key**. Your complete API key will be displayed, and a "copy" button will appear. Click this button to copy the key; you'll use it in the next step.

        <img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2a.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=1ac1226cb669cb98048760f5d2dd1285" alt="&#x22;How to deploy an application&#x22; page" data-og-width="3203" width="3203" data-og-height="2000" height="2000" data-path="framework/images/tutorial/social_post/sp_gen_2a.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2a.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=2042f479b12cdcd0c3760bf6792c3d91 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2a.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=6ac077a1e384fcf131946456d35d073c 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2a.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=ac026f1a626599199e32b5f4d2dcf93a 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2a.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=59b1d213f135dbef6f0a8c6e70dc9da6 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2a.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=93a343a5713b8fa001eeb778fa2ed851 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2a.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=0eac64bc92042b9340742561bcb73d5a 2500w" />
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
    writer create social-post-generator --template=ai-starter
    ```

    This command sets up a new project called `social-post-generator` using a starter template called `ai-starter` so that you're not starting "from scratch."
  </Step>
</Steps>

## Build the UI

Now that you've created the project, it's time to define the UI. The Writer Framework's drag-and-drop capabilities make it easy — even if you haven't done much UI work before!

The project editor is a web application that runs on your computer and enables you to define and edit your app's user interface. Launch it by typing the following into your terminal application:

```
writer edit social-post-generator
```

You'll see a URL. Control-click it (command-click on macOS) to open it, or copy the URL and paste it into the address bar of a browser window.

The browser window will contain the project editor, which will look like this:

<img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2b.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=d8e5d597c75f4303eb3f588e7ef5f7a8" alt="Project editor" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/social_post/sp_gen_2b.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2b.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=40eac2c2fdb66c7c1ad78a507194de57 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2b.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=270b34c881ea7a4afa734cbb6c8711dc 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2b.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=99630b2d6861552b72d880eb133a284a 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2b.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=eaf255ca1e4c9277ee036e78ac8748ca 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2b.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=5cb29aa4d9ded211468acd71cb88077d 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2b.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=ac4f410d9b268d4c2a533c6d0bc4cd76 2500w" />

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

        <img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2c.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=1ba5e3c03ec68463569c76c6e55baff2" alt="The selected header and its properties panel" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/social_post/sp_gen_2c.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2c.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=33ddaf22f51687d97c1785a66f08b107 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2c.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=1647f3741c5c300200f94aeb43dbbc55 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2c.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=597388f9b002b0600a0d03c2f3cd274a 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2c.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=6c6129c60fb2e9c873a53c78494e8388 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2c.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=21ffa20b393bb20a7c8786af0c2659cc 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2c.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=b7e9137b9c7ec749152fba689e6c046b 2500w" />

    The first property you'll see in the panel is the **Text** property, which defines the text that appears as the header's title. It should contain the value `@{my_app.title}`. The `@{` and `}` indicate that `my_app.title` is a variable and that its contents should be the text displayed instead of the literal text "my\_app.title". You'll set the value of this variable soon.
  </Step>

  <Step title="Clear the Section's default title">
    Select the **Section** component by clicking it — it's just below the **Header** component and contains the title **Section Title** and a gray area labeled **Empty Section**.

    In the **properties** panel, clear out the value of the **Title** property. This will remove the *Section*'s default title.

        <img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2d.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=6d404fbbeea27b1ccd0214ac42622a2a" alt="The selected section and its properties panel" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/social_post/sp_gen_2d.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2d.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=9034e8de81b31ce6f4396b0ff36a9d02 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2d.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=0d16f298f4e4463db4baae3761dcf986 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2d.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=3a6baa8cd24981da5095eab397271d43 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2d.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=23c058d9283ed46a3cac3e4666f903b4 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2d.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=060c5b6d55ccdd43549e36b4944c1881 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2d.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=6fc4c1dc53668d9357dc732610cc9580 2500w" />
  </Step>

  <Step title="Add a Text Input component">
    The user will need a place to enter words or phrases that the app will use as the basis for generating posts and tags.

    Drag a **Text Input** component — and note, it's **Text *Input***, not **Text** —  from the **Core toolkit** panel on the left (it's under **Input**, and you may need to scroll down a little to find it) and into the **Section**. Sections can act as containers for other components.

    <Note>You can search for a specific component by using the search bar at the top of the **Core toolkit** panel.</Note>

    Select the **Text Input** component. In the **properties** panel:

    * Find the **Label** property and set its value to `Topic for social posts and tags`.
    * (Optional) Feel free to add some placeholder to the *Text Input* component by setting the value of the **Placeholder** property with something like `Enter words or phrases describing your topic`.

        <img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2e.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=7922ce43b1b0dc522ce4fa3d7de4daae" alt="The text input component and its properties panel" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/social_post/sp_gen_2e.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2e.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=280d66e8d6a54b3c3d75e5b6753e9d9d 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2e.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=34e6a60812b5c4b43296c1f3da09e4ed 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2e.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=66aae4b9ac28e44529ae2e74a19e33c4 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2e.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=02eada6d4c8a431a23f12350be5d4e76 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2e.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=e5e23bf413c5b352c3bc03df363435a4 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2e.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=0b0a7f588379d0b69baa6996190dd607 2500w" />
  </Step>

  <Step title="Add a Button component">
    Drag a **Button** component from the **Core toolkit** panel (it's under **Other**, and you may need to scroll down a little to find it) into the **Section**, directly below the **Text Input**. The user will click this button to submit their prompt.

    Select the **Button**. In the **properties** panel:

    * Set the **Text** property's value to `Generate posts`.
    * Find the **Icon** property, and set its value to `arrow_forward`.

        <img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2f.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=bf1cd3c45cf7aaa3089e45c1103285ff" alt="The button component and its properties panel" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/social_post/sp_gen_2f.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2f.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=7ab6001de98bbb197acf04c70aa7d6e6 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2f.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=41df85f7374d6e119c81a75aa28b6e35 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2f.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=14e1fe3f6c0e4979d7d3c84f59585985 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2f.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=0bff970540e8be8aa08fd612d03e3b68 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2f.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=7f1efebd0a5960848a82d1261898eaf8 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2f.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=4125cae2556634102422cee2990d4553 2500w" />
  </Step>

  <Step title="Add a Message component">
    The process of creating social media posts and tags takes a few moments. In order to reassure the user that the app is working and hasn't crashed, it will use a **Message** component to display something reassuring while it's generating.

    Drag a **Message** component from the **Core toolkit** panel into the **Section** positioning it immediately below the **Button**.

    Select the **Message** component. In the **properties** panel:

    * Scroll down to the **Style** section and look for the **Loading** property, which sets the color of the **Message** component when it's loading.
    * Click its **CSS** button, which will cause a text field to appear below it.
    * Enter this color value into the text field: `#D4FFF2`.

        <img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2g.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=193337b7397365784f224687ae4ca8b3" alt="The message component and its properties panel" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/social_post/sp_gen_2g.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2g.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=654d0dc8189fd00fd197a1bf3650e4ec 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2g.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=1062688bdd8099eaed05df522b7388bf 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2g.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=cc30bae0044c6c97b5733410f99fc018 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2g.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=a0a175d5741124f86279c5b803d2fc84 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2g.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=18a30778946bc0c41c1588b62b69ba28 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2g.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=96fbbbffa568eef28b59c0698ae9ada9 2500w" />
  </Step>

  <Step title="Add a new Section">
    The **Section** that you were working on is for user input. Let's add a new **Section** to hold the output — the social media posts and tags the app will generate.

    Drag a **Section** component from the **Toolbox** panel and place it *inside* the **Section** that's already there, just below the **Message** component.

    <Note>That's right — **Sections** can contain other **Sections**!</Note>

        <img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2h.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=11dc51570178c77b7b1248f8b0d00110" alt="The new section inside the existing section" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/social_post/sp_gen_2h.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2h.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=5ccdb8e5f35e05105b1ac04adb00566a 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2h.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=27a244c17402ca3f24ac553c2ca83b87 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2h.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=96b529b865b31ed28d3e8a445f6fdae7 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2h.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=8bd12d5e7ec9b9c6714ce47f796dd71b 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2h.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=3c35cfdf33581d6c348113740536917d 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2h.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=3e14a6e4b1fd8979892aa95f3cc06a39 2500w" />

    Select the **Section** you just added. In the **properties** panel:

    * Find the **Title** property and clear it its value to remove the **Section**'s title.
    * Scroll down to the **Style** section and look for the **Container background** property, which sets the **Section**'s background color.
    * Click its **CSS** button, which will cause a text field to appear below it.
    * Enter this color value into the text field: `#F6EFFD`.

        <img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2i.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=462524d0c44ea635930c7c8aeda22087" alt="The new section and its properties" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/social_post/sp_gen_2i.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2i.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=16545f27975df973a3c0f14ee7465b08 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2i.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=0b84637fd8528dcae981ff7b7b978d56 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2i.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=fa62da1b6f695c475725192eaafef280 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2i.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=e6ed03a1f9b8acb5df9d36b2ed2d6d20 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2i.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=bbd116b65a36289d937ae8d4b7bf8656 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2i.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=c546d5f5c00b51cfd9de18cdbf13769b 2500w" />
  </Step>

  <Step title="Add a Tags component">
    Writer Framework has a number of useful components to make your apps more functional and beautiful. One of these is the **Tags** component, which can take a list of hashtags (or words, or short phrases) and display them inside colorful "bubbles" to make them stand out. This app will display the social media tags it generates in a **Tags** component.

    Drag a **Tags** component from the **Toolbox** panel and place it inside the new **Section**.

        <img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2j.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=54bac04c46c186245193ff0b18e1df9a" alt="The tags component" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/social_post/sp_gen_2j.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2j.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=efb43ec85dd06574286d42a040002de4 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2j.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=52ec6aafabad02ad51e6acc7088bc415 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2j.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=50db19703d6dc986e8a4f3f377074a18 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2j.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=970ad9debb16c2fd335acdacc8a8a547 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2j.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=c53364276bad24acdd0240d1da8b256c 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2j.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=6bf132a7a7672dda82a4a924a094909a 2500w" />
  </Step>

  <Step title="Add a Separator">
    Drag a **Separator** component from the **Toolbox** panel and place it inside the new **Section**, just below the **Tags** component. This will separate the tags from the posts.

        <img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2k.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=3f7e4b3524ce030c809588e275930e64" alt="The separator" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/social_post/sp_gen_2k.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2k.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=973ca6c4b306570aeaefbdedb048c8d7 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2k.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=893b25ea50f95aa75436b99d6003e7d9 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2k.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=620eca92f532d4e1425c87679f7fea6e 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2k.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=da97480d037f1f9cafe4a910908cbcb1 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2k.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=911dfc7ffc53ea733841f3863ba73b8b 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2k.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=afa6fb9ee733ddd8c359db24491fa968 2500w" />
  </Step>

  <Step title="Add a Text component">
    Finally, drag a **Text** component from the **Toolbox** panel and position it below the **Separator**. This will hold the generated social media posts.

        <img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2l.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=33db8853d9ac0c7cdebc2e54e856da7a" alt="The text component" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/social_post/sp_gen_2l.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2l.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=6081285ef9d29b93a8f2fb6d3831c41b 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2l.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=6d6daa8ea665574870a5200ef4839b52 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2l.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=f1f09d73c26d81082734194a3cc4c1c2 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2l.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=039ba580e608de1df268610db0f7820a 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2l.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=b37a7981523ba28219b0c97987763279 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2l.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=4a287685943213991111de7795be3e9d 2500w" />
  </Step>
</Steps>

## Add the back-end code

With the UI laid out, it's time to work on the logic behind it.

The logic behind the user interface is defined in a file named `main.py`, which is in your project's directory. This file was automatically generated; you'll update the code in it to define the behavior of your app.

The simplest way to edit `main.py` is within the project editor. Click on the "toggle code" button (beside the word **Code**) near the lower left corner of the project editor page.

<img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2m.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=23215946becf66a071916c4bfe27aabe" alt="Project editor with arrow pointing to toggle code button" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/social_post/sp_gen_2m.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2m.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=6db2fb8597b6e1fd4e6b7f01de16decf 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2m.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=bc95fe634d1facd4de24c161341af291 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2m.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=93cb55a9bc570bb21c931fe023941cf8 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2m.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=52ca2ac754c0c8c760410ff4cd75a26d 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2m.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=83d360d3ae0d4bf6250d3ea179f80056 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2m.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=3946dcecf43d8696e538b4aaa6162cf4 2500w" />

A pane with the name **Code** will appear at the bottom half of the screen, displaying an editor for the the contents of `main.py`.

<img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2n.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=dcf19ac48e57128e2b3487fb23cb22d7" alt="Project editor with the code editor displayed" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/social_post/sp_gen_2n.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2n.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=76688c2d663b761276a9d6f9809c3b7f 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2n.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=82b7b4f2d47e78d452e3e784e359990d 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2n.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=d0ea16a7e67c40c48eba0efe7a2bf459 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2n.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=af90ceaee74951fa31a835cad855b981 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2n.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=adb561caea9d1d4b32000141421cd350 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2n.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=7ce04ea912dd0f4818067c62ded5c2df 2500w" />

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
    import re
    import writer as wf
    import writer.ai

    # Set the API key
    wf.api_key = os.getenv("WRITER_API_KEY")
    ```

    This code imports the libraries that the application will need and then reads your Writer Framework API key in the `WRITER_API_KEY` environment variable.
  </Step>

  <Step title="Create a handler to respond to the user's input">
    When the user presses the app's **Button**, the app needs to call a function to generate and display the social media posts and tags. Find these comments in the code...

    ```python  theme={null}
    # Welcome to Writer Framework! 
    # This template is a starting point for your AI apps.
    # More documentation is available at https://dev.writer.com/framework
    ```

    ...and replace them with the following function:

    ```python  theme={null}
    def generate_and_display_posts_and_tags(state):
        print(f"Here's what the user entered: {state['topic']}")

        # Display message
        state["message"] = "% Generating social media posts and tags for you..."

        # Generate and display social posts
        prompt = f"You are a social media expert. Generate 5 engaging social media posts about {state['topic']}. Include emojis, and put a blank line between each post."
        state["posts"] = writer.ai.complete(prompt)
        print(f"Posts: {state['posts']}")

        # Generate and display hashtags
        prompt = f"You are a social media expert. Generate around 5 hashtags about {state['topic']}, delimited by spaces. For example, #dogs #cats #ducks #elephants #badgers"
        pattern = r"#\w+"
        hashtags = re.findall(pattern, writer.ai.complete(prompt))
        state["tags"] = {item: item for item in hashtags}
        print(f"Tags: {state['tags']}")

        # Hide message
        state["message"] = ""
    ```

    The `%` at the start of the string being assigned to `state["message"]` will be replaced by a “spinning circle” progress indicator graphic in the *Message* component.

    The `pattern` variable in the `# Generate and display hashtags` section defines a regular expression pattern to search for words that begin with the `#` character. The `r` in front of the opening quote specifies that the string is a *raw string*, which means that the `\` character should be treated as a literal backslash and not as the start of an escape character sequence.

    Note that `generate_and_display_posts_and_tags()` uses `print()` functions for debugging purposes, and you can use them to get a better idea of what's happening in the function. You'll see their output in both your terminal application and in the project editor's 'log' pane (which will be covered shortly) as you use the social post generator. This output will include:

    * The topic the user entered
    * The posts generated by the LLM
    * The hashtags generated by the LLM

    The `print()` functions don't affect the operation of the social post generator in any way, and you can remove them if you wish.
  </Step>

  <Step title="Initialize the application">
    The final step is to set the application's initial state. Find this code, which should be just after the `generate_and_display_posts_and_tags()` function...

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
        "topic": "writing",
        "message": "",
        "tags": {},
        "posts": "",
        "my_app": {
            "title": "SOCIAL POST GENERATOR"
        }
    })
    ```

    The Writer Framework's `init_state()` method sets the initial value of `state`, a dictionary containing values that define the state of the application. The key-value pairs in `state` are how you store values used by your app and how you pass data between the back-end code and the UI.

    The code above sets the initial value of `state` so that it has these key-value pairs:

    * `topic`: A string containing the topic that the application should generate social media posts and tags for. You'll bind its value to the *Text Input* component where the user will enter the topic.
    * `message`: A string containing text of the message that will be displayed to the user while the application is generating posts and tags. You'll bind its value to the **Message** component.
    * `tags`: A list containing the hashtags generated by the LLM. You'll bind its value to the **Tags** component.
    * `posts`: A string containing the social media posts generated by the LLM. You'll bind its value to the **Text** component.
    * `my_app`: A dictionary containing values that define the application's appearance. This dictionary has a single key-value pair, `title`, which defines the text that appears as the application's title.

    <Note>For more details about the `state` variable, see our [*Application state*](https://dev.writer.com/framework/application-state#application-state) page.</Note>
  </Step>

  <Step title="Save the updated code and hide the code editor">
    That’s all the code. If you edited the code in the browser, save it by clicking the “save” button near the top right corner of the code editor.

        <img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2o.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=d8da7e0bd7c4e66f1754e538246bf465" alt="Project editor and code editor, with arrow pointing to save button" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/social_post/sp_gen_2o.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2o.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=28d7e3222bac8aedf3b40ffcaff6e3c3 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2o.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=a66818a60fb9f140caa3ddbe99cc9d03 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2o.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=063ea0d4fb7f6d2b1a2f180cd2aae044 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2o.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=fbb69badb025d4a41262b966640c3571 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2o.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=aec6d1b2428698d9cb2df8f841a0d298 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2o.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=7dd86bfa71bf0570053ac3a0419b9144 2500w" />

    Click the "toggle code" button to hide the code editor.
  </Step>
</Steps>

## Bind the UI to the back-end code

You've built the UI and written the code behind it. Let's connect the two! Go back to the browser window with the project editor and do the following:

<Steps>
  <Step title="Observe that the heading at the top of the app is now 'SOCIAL POST GENERATOR'">
    Earlier, you saw that the **Header** component's **Text** property was set to `@{my_app.title}`, a value in the app's `state` variable. You changed this value when you update the call to the Writer Framework's `init_state()` method.
  </Step>

  <Step title="Bind the Text Input component to the 'state' variable's 'topic' key">
    Select the **Text Input** component. In the **properties** panel, scroll down to the **Binding** section and find the **State element** property. This is where you specify the `state` variable key whose value will be connected to the **Text Input** component. Set its value to `topic`.

        <img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2p.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=fc53611bc4959c8bad1b2d7af7e19cbb" alt="Updating the text input component's state element property" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/social_post/sp_gen_2p.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2p.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=0cd31f698e0e8c034fea80c9c847b2d3 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2p.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=b20b208a72cf630085dc77e178b41ac2 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2p.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=6daa47701108ac2f5cd9aa801f545ff1 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2p.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=daaf7ab6aeac1893d69c8a2e7541f58d 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2p.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=19030fe499e826163cfe42317a9459d4 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2p.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=e761fc92b561ccb92681e0dd58d87151 2500w" />
  </Step>

  <Step title="Connect the Button component to the 'generate_and_display_posts_and_tags()' function">
    Select the **Button** component. In the **properties** panel, scroll down to the **Events** section and find the **`wf-click`** property. This is where you specify the function to call when the user clicks the button — set its value to `generate_and_display_posts_and_tags`.

        <img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2q.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=c9c623a7061f1baa2ba98c606a1b8cd2" alt="Updating the button's wf-click property" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/social_post/sp_gen_2q.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2q.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=96a4c733613a0924cd0925c81afc3581 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2q.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=6ead01e5fafee74233abfc854372e42a 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2q.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=67ed1edcad22b98de8aad64374349fb9 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2q.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=242b28f9ae95bcb9d2a34852c0cbe6d3 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2q.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=368697602f57ed075943d377a7e3aafe 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2q.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=b387f580b2d4fcdee2e4e12526c2abb7 2500w" />
  </Step>

  <Step title="Bind the Message component to the 'state' variable's 'message' key">
    Select the **Message** component. In the **properties** panel, find the **Message** property, which specifies the content of the **Message** component. Set its value to `@{message}`.

        <img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2r.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=6ad60398867b52bd8a9843f725963a9d" alt="Updating the message's message property" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/social_post/sp_gen_2r.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2r.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=851656795dc55f741bbc7e3abc5b50e4 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2r.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=4ca2267376aeb709d982f4e76c3d4820 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2r.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=5c1a19f1c9e9479cbe289b92043d4aca 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2r.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=6c7f84e5ec8d45aa9452c09a7d76d528 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2r.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=bc1397a70f33fec01170731a6a0dee98 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2r.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=fbbaf6bd939b02a8c7f92839a66546dd 2500w" />
  </Step>

  <Step title="Bind the Tags component to the 'state' variable's 'tags' key.">
    Select the **Tags** component. In the **properties** panel:

    * Find the **Tags** property, which specifies the source of the tags that the component will display.
    * Click its **JSON** button.
    * In the text field below the **JSON** button, set the **Tags** property's value to `@{tags}`.

        <img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2s.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=58a4c76ca5d884b5248f9cf7d001e0d8" alt="Updating the tags component's tags property" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/social_post/sp_gen_2s.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2s.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=fdcb8f643eeab66f37e5a7b62eba47b2 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2s.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=383868e92f86e2709c44e0eee5d5b1b9 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2s.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=0f38ec2ea3d68e205f8f6013ebc20235 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2s.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=d18a775e3138dd72d3ff69e672d5dc8e 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2s.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=e3774351e6f0395b69445420a5508e36 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2s.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=b883fa614c73890a673fa5a0e35782ac 2500w" />
  </Step>

  <Step title="Bind the Text component to the 'state' variable's 'posts' key">
    Select the **Text** component. In the **properties** panel:

    * Find the **Text** property, which specifies the content of the **Text** component. Set its value to `@{posts}`.
    * Set the **Use Markdown** property to **yes**.

        <img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2t.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=c2b407d36da8a80322e9b59726a57e3d" alt="Updating the text component's properties" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/social_post/sp_gen_2t.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2t.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=6426026b1f8a196b86e7f33a62d5df78 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2t.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=dc64ca5ed5b5e619ec8d312e939b1ee8 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2t.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=fd19e874681ab9335b7397fae2980a56 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2t.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=8f1f26640293be54167ad0c7404a7f85 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2t.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=a144af80ba30e92b6fd52b4552b89b54 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2t.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=6121dff59ad96ea17650e3e2103c1c59 2500w" />
  </Step>

  <Step title="Set the visiblity of the Section component containing the Tags and Text components based on the 'state' variable's 'posts' key">
    Select the **Section** component containing the **Tags** and **Text** components. In the **properties** panel:

    * Scroll to the **Visibility** property at the bottom.
    * Click on the **Custom** button.
    * In the **Visibility value** field, set the value to `posts`. This will cause the **Section** to be visible only when the `state` variable's `posts` key has a non-empty value.

        <img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2u.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=66dd75bc9f809d79c0c176b02344ed3b" alt="Updating the inner section's visibility property" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/social_post/sp_gen_2u.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2u.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=abbfa1fc4b1c5360e0fae75d9cf399b3 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2u.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=0dc01388ba6625f3cfdb89b5a07a87a2 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2u.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=ed77d9dd83e631d78b9a18a7594045f2 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2u.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=f95c14d35f1e849a0da90836f323d090 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2u.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=a76db2f8ac00044c4728b8a970c01515 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2u.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=05d3f1c71444f6716f287ec495fe1f4e 2500w" />
  </Step>
</Steps>

## Test the application

You've completed all the steps to make a working social post generator, and you can try using it right now, even while editing the user interface!

Enter a topic into the **Topic for social posts and tags** text field, then click the **Generate Posts** button\* *twice* — the first time will cause the **properties** panel to appear, and the second click will register as a click. You'll know that you've clicked the button when you see the **Message** component display the text “Generating social media posts and tags for you...”

<img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2v.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=447377026cf15c91a31ae023e09a8a40" alt="Waiting for the generator to finish while the message component displays its message" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/social_post/sp_gen_2v.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2v.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=d5303b3864f3a7418e72f79e1dec8631 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2v.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=f14c537495df808a93f39670e77905ef 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2v.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=fe2729b0916e6fb8870c6aad66e31eb2 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2v.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=864a178c6b70214ba375c4bae0c22de4 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2v.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=75d60bc5968f95076655e0eeaecb407a 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2v.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=46ece4baf1dc499b9cc87a080af6499c 2500w" />

...and soon after that, you should see some results:

<img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2w.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=8592349842ed1474717e26c14496c515" alt="The results" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/social_post/sp_gen_2w.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2w.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=0367966dd0ae3a215dae55367c3e49a3 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2w.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=f8ca68bb7a924ecacde216a031a26f40 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2w.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=279c69ac16a406a0f6f3d996c93dc802 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2w.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=0ac16a8f214f8a8314a4f1097b3383f4 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2w.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=2f01654cf89ac5af43221d7528769660 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2w.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=46ad058e1c70ca9c0184bf45ddae7b06 2500w" />

To get a better sense of what the experience will be like for the user, switch to the preview by changing the edit mode (located near the upper left corner of the page) from *UI* mode to *Preview* mode by selecting the **Preview** option:

<img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2x.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=80d54c9686267c8e3b98c45478ecf7e9" alt="The project editor with an arrow pointing to the Preview button" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/social_post/sp_gen_2x.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2x.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=1488ff4e84b8a606015670d2e953c3f8 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2x.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=fb571bfdfd93747150f3494b93283b18 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2x.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=877d4a455cdc3ea9d319bd97c9d672c3 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2x.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=ff782d28022907591d2be1f35b18341b 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2x.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=dbdbb68c1c61859882c89a3e4b14fdbe 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2x.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=19ff7808ba667abfa49c1523877d410d 2500w" />

Here’s what the app looks like in *Preview* mode:

<img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2y.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=5a85e393eff468bcadf056e260e23b95" alt="The working social post generator, with the project editor in &#x22;Preview&#x22; mode" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/social_post/sp_gen_2y.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2y.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=c9ac3737213b9fd46d8ed3778be9c124 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2y.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=4329e9461fa4d9dbc3380822f1b7f2ed 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2y.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=b53cf707b21d64d47b78a6e6091b3dcc 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2y.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=d9a729c17c7c59117311c892ea569653 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2y.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=29c916c3b56deb8e9f97eb9dfdb8395d 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2y.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=8fd27c33aa50de95b83c5826e3667b97 2500w" />

You can see the output of any `print()` functions and error messages by clicking on the **Log** button located near the upper right corner of the page:

<img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2z.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=8d7cd482ba5658595eba7246578fbe28" alt="The social post generator with an arrow pointing to the Log button" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/social_post/sp_gen_2z.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2z.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=7cf17ff51372c4b20d30402e95a1ad6c 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2z.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=3eae356f8b94d4e7eea89eb9f94dffd6 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2z.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=2a0f8acda96054996aa2f0b9a4571e46 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2z.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=df6e0ae96498976d9365f7385306568b 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2z.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=97cd57fde5700cb4571dbedd5d9297ee 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2z.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=dc57818fb5b27dcbe3cd92cc1589fbaf 2500w" />

Here’s what the app looks like when displaying the log:

<img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2aa.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=c27dfb7ee4bed11a5c0908343a4bac3d" alt="The social post generator, with the log pane displayed" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/social_post/sp_gen_2aa.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2aa.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=5488493d642c1bdbbaba9716d94c6bf1 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2aa.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=30eaa564df190f38c4c0d4b1266067b0 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2aa.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=46f5d207ff4e6b5b65e1f96b45bb1d3e 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2aa.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=33e7a4d67b1152b74c41a151d5e05871 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2aa.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=5bb3e3b986ad597463ae94f1668bfe0b 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2aa.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=78688714e7ec521206f68e546573b808 2500w" />

It's very helpful to be able to test the application while editing it. As you continue to work with Writer Framework, you'll find yourself alternating between making changes to your application and testing those changes without having to leave the project editor.

## Run the application locally

Once you've tested the application, it's time to run it locally.

Switch back to your terminal application. Stop the editor with ctrl-c, then run the application by entering the following command:

```
writer run social-post-generator
```

Note that the command starts with `writer run` as opposed to `writer edit`. This launches the application as your users will see it, without any of the editing tools. Even though you can preview your applications in the project editor, it's still a good idea to test it by running it on your computer, outside the project editor, before deploying it.

You'll be able to access the application with your browser at the URL that appears on the command line. It should look like this:

<img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2ab.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=e38dd8f9a9fe0a6b6976706902b45761" alt="Finished social post generator project" data-og-width="3000" width="3000" data-og-height="2000" height="2000" data-path="framework/images/tutorial/social_post/sp_gen_2ab.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2ab.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=33377c60d8cb103cb857c06aa1a31e7e 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2ab.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=60df3811ecd7566018b07c5fe7fc36cd 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2ab.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=6341f4458526199a5e4333b3a2187728 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2ab.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=f2221fca93c548a5fbedc208e7842de6 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2ab.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=efd3624129c3b4d65434eec07b212ebb 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/social_post/sp_gen_2ab.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=c6a0a9a8baca8a45ef096077e29a67d3 2500w" />

<Note>The Writer editor, which you launched with `writer edit social-post-generator`, and your application, which you launched with `writer run social-post-generator`, run  on the same URL, but on different *ports* (specified by the number after the `:` character at the end of the URL).</Note>

## Conclusion

That's it — you've built a functional social post generator using the Writer Framework!

Feel free to modify this project! The Writer platform is flexible enough for you to customize, extend, and evolve your application into something completely different! To find out what else you can do, check out the documentation for [Writer Framework](https://dev.writer.com/framework/introduction) and the [Writer API](https://dev.writer.com/introduction).

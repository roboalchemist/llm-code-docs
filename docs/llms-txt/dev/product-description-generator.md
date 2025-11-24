# Source: https://dev.writer.com/framework/product-description-generator.md

# Product description generator

In this tutorial, you'll use the Writer Framework to build a Saturn Snacks product description generator for a variety of food outlets. After adding the initial functionality of the app, you'll also extend the app to include a chart of SEO keyword analysis and the ability for users to add their own food outlet.

<img src="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_1.png?fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=7a650f72a50ecfe26f26954850752c7c" alt="Finished application" data-og-width="3220" width="3220" data-og-height="1478" height="1478" data-path="framework/images/tutorial/product_desciption/pd_gen_1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_1.png?w=280&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=f51b23322b4be0350fb505dd6df579bb 280w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_1.png?w=560&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=1fb3fe7c91fd2ada3e63c50311d86a49 560w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_1.png?w=840&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=f8c001b84134fc8ccb8b8e89148bc9e1 840w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_1.png?w=1100&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=e96936de6c072de5d1dd7828e56d8886 1100w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_1.png?w=1650&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=1d0024d21a3ab9d9d313dcaf4f42eafe 1650w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_1.png?w=2500&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=5b359a2430a3e566d68de0367d2ccfd0 2500w" />

## Setting up your project

### Creating a Writer app and getting your API key

From the Home screen, click on **Build an app**.

<img src="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_2.png?fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=8982373a5960f4538f99cee7560e3b65" alt="Writer home screen" data-og-width="3220" width="3220" data-og-height="1900" height="1900" data-path="framework/images/tutorial/product_desciption/pd_gen_2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_2.png?w=280&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=5c2454d14780cf7aae43cb82253aa74c 280w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_2.png?w=560&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=51821cad51cfeaf32a13be0be4811e12 560w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_2.png?w=840&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=e2d473c6aac1012d979c30dac76f1866 840w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_2.png?w=1100&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=0a27dca388972153920ad509f1505305 1100w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_2.png?w=1650&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=dd34f18129689b559399163eba8a2184 1650w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_2.png?w=2500&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=2983c5446c80f7211c90dcbe9a926580 2500w" />

Select Framework as the app type you’d like to create, enabling you to generate keys and build your app with the Writer Framework.

<img src="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_3.png?fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=ca942a84ade3518427b5ccbc58a12f4f" alt="App type selection" data-og-width="3220" width="3220" data-og-height="1900" height="1900" data-path="framework/images/tutorial/product_desciption/pd_gen_3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_3.png?w=280&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=898d65a6574077b0db7681fc98b33964 280w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_3.png?w=560&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=260c95c4aa910af480100c09afd40e6c 560w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_3.png?w=840&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=fed60ebc4ab8f79d0f1d410dc9137af0 840w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_3.png?w=1100&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=eb8c794b63d639d50fe2c4f473665348 1100w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_3.png?w=1650&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=927dc6214469ae5c129d59ed99ba7db2 1650w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_3.png?w=2500&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=0ed409b8c656219754bca631d8659d7a 2500w" />

On the next screen, you can edit your Writer application name in the upper left. Underneath “Authenticate with an API key,” click on “Reveal” to see and copy your API key.

### Creating the application

Next, open your terminal and navigate to the directory where you want to create your application directory.

<Steps>
  <Step title="Set the API key environment variable">
    To pass your API key to the Writer Framework, you'll need to set an environment variable called `WRITER_API_KEY`. Here’s how you can set this variable in your terminal session:

    <CodeGroup>
      ```sh On macOS/Linux theme={null}
      export WRITER_API_KEY=[key]
      ```

      ```sh On Windows theme={null}
      set WRITER_API_KEY=[key]
      ```
    </CodeGroup>
  </Step>

  <Step title="Create the application">
    Run the following command to create your application. Replace `product-description-app` with your desired project name and `pdg-tutorial` with the template you wish to use:

    ```
    writer create product-description-app --template=pdg-tutorial
    ```

    This command sets up a new project called `product-description-app` in the specified directory using a template designed for this tutorial.
  </Step>

  <Step title="Edit your project">
    To edit your project, run the below commands. This will bring up the console, where Framework-wide messages and errors will appear, including logs from the API. By default, the Writer Framework Builder is accessible at `localhost:4005`. If that port is in use, you can specify a different port. Open this address in your browser to view your default application setup.

    <CodeGroup>
      ```bash Standard port theme={null}
       writer edit product-description-app
      ```

      ```bash Custom port theme={null}
       writer edit product-description-app --port=3007
      ```
    </CodeGroup>
  </Step>
</Steps>

## Introduction to the application setup

When you first start up the application, you're going to see two main layout items provided by the template:

1. A Header component with the name of the application
2. A Column container that'll house most of the UI of the app

The left column includes a form that has three text inputs and a button. These three text inputs are bound to corresponding state elements. The right column contains a Message component for loading and status messages, as well as an empty Tab container which you'll use to display the product descriptions of the various outlets.

### Code overview

Looking at the code in `main.py`, you'll see that the template already imported the Writer Framework, the AI module, and the product description prompts that you'll use throughout this tutorial.

```python  theme={null}
import writer as wf
import writer.ai
from prompts import base_prompts, user_prompt, seo_keywords
```

The prompts are stored in a separate file called `prompts.py`. You are welcome to open this project in the IDE of your choice and modify the prompts however you wish. However, you don't need to make any changes to this file to follow this tutorial.

You'll also see the state initialization:

```python  theme={null}
wf.init_state({
   "form": {
       "title": "",
       "description": "",
       "keywords": ""
   },
   "message": "Fill in the inputs and click \"Generate\" to get started.",
})
```

The form elements and the message have been initialized as strings. You'll add to this state dictionary throughout the tutorial.

## Implementing the Product description generator

Your first goal is to generate product descriptions for the various food outlets, with each outlet appearing as a tab to the right of the form.

<img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_4.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=fdcee7cedc90faff3147219526a74da7" alt="Finished product description tabs" data-og-width="3220" width="3220" data-og-height="1630" height="1630" data-path="framework/images/tutorial/product_desciption/pd_gen_4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_4.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=9e61507dde6186d0efbb4f51532e5325 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_4.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=d73778b217624d68714c60dc01a7a200 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_4.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=075767fcb8a242fa50573fbda5134820 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_4.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=ba6d2ed4ec7410ee9c937e9677f70a8c 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_4.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=64ac8b47e3153d392b017a5e4cc6d606 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_4.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=435ffead4cc607517597846666addb87 2500w" />

### Setting up the code

First, integrate new functionality into your code for generating product descriptions.

<Steps>
  <Step title="Add a private helper method">
    Paste the following method on line 5 after all of the imports to create a helper function for generating product descriptions:

    ```python  theme={null}
    def _generate_product_description(base_prompt, product_info):
       prompt = base_prompt.format(**product_info)
       description = writer.ai.complete(prompt)
       return description
    ```

    This function, `_generate_product_description`, accepts a base prompt and the product information from a form on the page. The underscore at the beginning of its name indicates that it's a private method not exposed to the UI.
  </Step>

  <Step title="Initialize additional state elements">
    Update the `wf.init_state()` to include a `product_description` dictionary with visibility control and outlets for descriptions:

    ```python  theme={null}
    wf.init_state({
       "form": {
           "title": "",
           "description": "",
           "keywords": ""
       },
       "message": "Fill in the inputs and click \"Generate\" to get started.",
       "product_descriptions": {
           "visible": False,
           "outlets": {}
       }
    })
    ```

    This setup includes a variable `visible` to control whether product description tabs are shown or hidden, and an empty dictionary `outlets` for storing descriptions.
  </Step>

  <Step title="Add a button click handler">
    Paste the following method beneath `_generate_product_description` to handle button clicks and generate descriptions:

    ```python  theme={null}
    def handle_click(state):
       state["product_descriptions"]["visible"] = False

       # Loop through all the base prompts to generate versions tailored to each outlet
       for outlet, base_prompt in base_prompts.items():
           state["message"] = f"% Generating product description for {outlet}..."
           product_description = _generate_product_description(base_prompt, state["form"].to_dict())
           state["product_descriptions"]["outlets"][outlet] = product_description

       state["product_descriptions"]["visible"] = True
       state["message"] = ""
    ```

    This handler will loop through each imported base prompt, format it with the form information, and pass it to the helper method. The handler also manages UI interactions, such as displaying and hiding product descriptions and managing loading messages.
  </Step>
</Steps>

### Setting up the user interface

You can now set up the UI to iterate over the product descriptions dictionary and create tabs. Begin by opening the User Interface.

<Steps>
  <Step title="Add and configure the Repeater component">
    In the toolkit, drag a Repeater component from the Other section into the empty Tab Container. Click on the Repeater component to open its component settings. Under Properties, add `@{product_descriptions.outlets}` as the Repeater object to be used for repeating the child components. Replace the default “Key variable name” with `itemId`. You can leave “Value variable name” as `item`.

        <img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_5.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=fc355793aa67411f6a538a293c43b411" alt="Repeater settings" data-og-width="3220" width="3220" data-og-height="1402" height="1402" data-path="framework/images/tutorial/product_desciption/pd_gen_5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_5.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=79484e44a2a3c99a2951e8c1d4a9287a 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_5.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=7548d28a47bdb889e4fe9b2ff33547af 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_5.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=177cc6261d00ece5aa6807529a619d85 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_5.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=f92adf18c186b88825445b7e2d070d00 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_5.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=40e60532d8312f4b663c574d1fc35a4a 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_5.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=7ec964b2b0aa78fcea6aac39817e81d2 2500w" />
  </Step>

  <Step title="Add and configure the Tab component">
    From the Layout section of the toolkit, drag a Tab component into the Repeater. Click on the Tab to bring up the component settings and add `@{itemId}` to the Name property to display the outlet name on the tab.

        <img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_6.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=b52573eaafb4307107563db4eaf73128" alt="Tab settings" data-og-width="3220" width="3220" data-og-height="572" height="572" data-path="framework/images/tutorial/product_desciption/pd_gen_6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_6.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=705260ded9c5269cf53935ab0f162d7b 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_6.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=a25eac802081c1820e54869b0ed8bfe6 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_6.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=4b3bec98ba5f2d300dc3cb2202923eaf 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_6.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=e7c4467018b7ad8dfac2212b261766b4 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_6.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=ef75608900dfc90bad8c48324114f50d 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_6.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=8baf2962fd6ef6f46bbc857a4b439052 2500w" />
  </Step>

  <Step title="Add and configure the Text component">
    Drag a Text component from the Content section of the Toolkit into the Tab. Click on the Text component to open the Component settings and set the Text property to `@{item}`. You may also choose to set “Use Markdown” to “yes.”

        <img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_7.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=51935abb3a9f642cfd11e0966936c602" alt="Text settings" data-og-width="3220" width="3220" data-og-height="972" height="972" data-path="framework/images/tutorial/product_desciption/pd_gen_7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_7.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=5a505c334fd997502f45b0a436191cc4 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_7.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=bffa5b8209095892335f75f7215c1b48 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_7.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=8687b7c8a2d60b72eed4ee91bee622cb 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_7.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=432913911bbced0d1b40ebab3a2e9552 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_7.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=f82908b6790844eb9e7d034003b703dd 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_7.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=d5597445a5f231d2d4b975adc9cf19a7 2500w" />
  </Step>

  <Step title="Control the visibility of the Tab container">
    Click on the Tab container to bring up its Component settings. Scroll to the bottom and, under Visibility, click “Custom” and add `product_descriptions.visible` to the Visibility value input.

        <img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_8.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=07d61f8ca1ac93e21cf12561cfb07481" alt="Tab container visibility settings" data-og-width="3220" width="3220" data-og-height="690" height="690" data-path="framework/images/tutorial/product_desciption/pd_gen_8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_8.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=7506a44dffc772937092c197fc5cfc11 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_8.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=ad8e38732b4c09dc940a6c2cecf7c7c5 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_8.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=730d05796d4760dcf20c97dc5651b6ad 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_8.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=61abacda8ab17862c583fa33ddd6c77a 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_8.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=cf0b628590908ba3a8438ef827e2e940 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_8.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=f4e55c6c761b92b38bfe9ac732862011 2500w" />
  </Step>

  <Step title="Wire up the form with the Generate button">
    Click on the Generate button inside the form to bring up its Component settings. In the Events section, select `handle_click` for the `wf-click` event.

        <img src="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_9.png?fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=2732d5fb788b351d640f6f34676e76f3" alt="Button settings" data-og-width="3220" width="3220" data-og-height="566" height="566" data-path="framework/images/tutorial/product_desciption/pd_gen_9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_9.png?w=280&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=d6303dbaf51377170ecc88a90fe795d0 280w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_9.png?w=560&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=3662333ce52b85179ea821c7c10e9287 560w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_9.png?w=840&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=d253a083db55b68430243ddf9d88968f 840w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_9.png?w=1100&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=e4b05c62c02fac5f5c5cdb3d2be63c42 1100w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_9.png?w=1650&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=407c60da37223b1e68f4d7f0df3d03fd 1650w, https://mintcdn.com/writer/PCF7UWM79DSDrLoF/framework/images/tutorial/product_desciption/pd_gen_9.png?w=2500&fit=max&auto=format&n=PCF7UWM79DSDrLoF&q=85&s=1b7348732b4b2627517f9f53c415077c 2500w" />
  </Step>

  <Step title="Preview and test the application">
    Click **Preview** in the top toolbar, enter some test data, and click the **Generate** button. You should see a loading message, as well as three example food outlets displayed in the tabs. The loading message should disappear when everything is loaded, and the tab should remain visible once the data has loaded.

    Great work!
  </Step>
</Steps>

## Expanding the application: SEO keyword analysis

You can expand on this application by adding a chart that displays the top ten SEO keywords present in the product descriptions.

### Updating the code

To do this, back in the code, first add the following helper function underneath your ` _generate_product_description` helper method:

```python  theme={null}
def _generate_seo_keywords(outlets):
   combined_descriptions = "\n".join(f"{key}: {value}" for key, value in outlets.items())


   # Generate the prompt with the provided descriptions
   prompt = seo_keywords.format(descriptions=combined_descriptions)
   # Strip out whitespace and backticks from the response
   return writer.ai.complete(prompt).strip(" `\n")

```

This method concatenates all of the product descriptions and incorporates them into a prompt in `prompts.py`. It then sends the formatted prompt to the Palmyra LLM using the `complete` method. The prompt not only analyzes the descriptions for SEO keywords, but also outputs a [Plotly.js](/components/plotlygraph) schema object that you can use directly with a Plotly graph component.

With the helper method in place, you can now update the click handler for the button. On line 27, add the following code before the product description visibility is set:

```python  theme={null}
# Create the SEO analysis
   state["message"] = "Analyzing SEO keywords..."
   outlets = state["product_descriptions"]["outlets"]
   state["seo_analysis"] = _generate_seo_keywords(outlets)
```

This code sets the loading message and passes all of the product descriptions to the SEO keyword helper method.

### Adding SEO analysis to the UI

To update the UI to display this chart, first drag a new tab from the Layout section of the toolkit into the Tab container. This tab should not be inside of the Repeater, but can be either before or after it. Click on the tab to open the component settings, and change the name to “SEO Analysis.” If you'd like, you can also set the Visibility to “Custom” and set `seo_analysis` as the visibility value.

<img src="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_10.png?fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=67e6e702fc5c59121a6a5b32deb02bad" alt="SEO Tab" data-og-width="3220" width="3220" data-og-height="578" height="578" data-path="framework/images/tutorial/product_desciption/pd_gen_10.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_10.png?w=280&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=ea0cd7696f191cc33fba836a85b9cdb3 280w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_10.png?w=560&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=47b0069b1f663f8ee5a4404f7d03ac29 560w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_10.png?w=840&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=a57b70813e60af3b2adf271a8e056e04 840w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_10.png?w=1100&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=ede88933adfba60a96f605785803c6d1 1100w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_10.png?w=1650&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=684a352c0b7a09f8dee7e1f99f6c1c8d 1650w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_10.png?w=2500&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=0550613714d5b5717b673841d9952148 2500w" />

To display the chart, drag a Plotly graph component from the Content section of the toolkit into your new tab. Click on the component to bring up the component settings. The Plotly graph component accepts a graph specification. Add `@{seo_analysis}` to pass the LLM-generated graph specification to the component.

Click preview, add some data to the form, and click generate. You should see a new SEO analysis tab appear with a nicely formatted and labeled chart.

<img src="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_11.png?fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=46c9e35d8235fa33e8a5637175275b67" alt="SEO analysis tab and chart" data-og-width="3220" width="3220" data-og-height="1300" height="1300" data-path="framework/images/tutorial/product_desciption/pd_gen_11.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_11.png?w=280&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=4669d84999baede47a87902d23be2b1e 280w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_11.png?w=560&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=65114d024289d2b777cbbe6d38d0ea37 560w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_11.png?w=840&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=67918c739a5aff5808b75a4b2d8c9088 840w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_11.png?w=1100&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=2834a67c7d97601da15c0922db0576fb 1100w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_11.png?w=1650&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=55c5ce937242e60dda961ea5889faf47 1650w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_11.png?w=2500&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=6db3aad9d9e7aae1a42219dfac6b86ea 2500w" />

## Extending the application: user-added outlet

Finally, you can extend this application even further by allowing users to add their own custom food outlet and derive a new description from a custom prompt.

### Adding the new form

Start by building the UI for this new form. From the Layout section of the Toolkit, drag a new Section component into the column where the current form is and drop it above or below it. Click on the Section and change the Name to “Add an outlet.”

To create the inputs for the form, drag a Text Input and a Number Input from the Input section of the Toolkit into the newly created section. Click on the Text Input component to change the Label to “Outlet name.” Click on the Number Input and change the label to “Character max.”

Finally, add a Button from the Other section of the toolkit to the bottom of the new section. Click on the button and change the text to “Add and Generate.” You can also add `laps` or another [Material Symbols](https://fonts.google.com/icons) ID to the Icon input if you wish.

<img src="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_12.png?fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=239f082ca68d09a76779f48ccd55e783" alt="Add outlet form" data-og-width="3220" width="3220" data-og-height="740" height="740" data-path="framework/images/tutorial/product_desciption/pd_gen_12.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_12.png?w=280&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=44c25a82313f0f00e95ad8e112c725ea 280w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_12.png?w=560&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=71abb40de349904112493f96e0f52363 560w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_12.png?w=840&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=a43591a160388f83d2bc3dae0f661685 840w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_12.png?w=1100&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=d5a5c4d570fea7ee64b6a5c7e3abd4e6 1100w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_12.png?w=1650&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=c88d37f4240c2a2925187a2ce8dd62dc 1650w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_12.png?w=2500&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=3396f96b72b7baae6f16b3e3a82035ab 2500w" />

### Updating the code

In the code, you next need to add corresponding state elements for the new form components to `wf.init_state()`. Add the following to the state dictionary:

```python  theme={null}
"outlet_form": {
       "name": "",
       "character_max": "",
   },
```

Don't forget to check your commas when adding to the state dictionary. Your completed state should look like this:

```python  theme={null}
wf.init_state({
   "form": {
       "title": "",
       "description": "",
       "keywords": ""
   },
   "outlet_form": {
       "name": "",
       "character_max": "",
   },
   "message": "Fill in the inputs and click \"Generate\" to get started.",
   "product_descriptions": {
       "visible": False,
       "outlets": {}
   }
})
```

The `outlet_form` state elements will bind to the form elements.

Next, add the click handler for the new button. Copy and paste this `handle_add_outlet` method into the code under the `handle_click` method:

```python  theme={null}
def handle_add_outlet(state):
   # Create a new base prompt for the new outlet
   new_outlet_name = state["outlet_form"]["name"]
   product_info = {**state["outlet_form"].to_dict(), **state["form"].to_dict()}
   base_prompt = user_prompt.format(**product_info)


   # Add the new base prompt to the base_prompts dictionary
   base_prompts[new_outlet_name] = base_prompt


   # Generate the product description for the new outlet
   state["message"] = f"% Generating product description for {new_outlet_name}..."
   product_description = _generate_product_description(base_prompt, state["form"].to_dict())
   state["product_descriptions"]["outlets"][new_outlet_name] = product_description


   # Update the SEO analysis
   state["message"] = "Updating SEO analysis..."
   outlets = state["product_descriptions"]["outlets"]
   state["seo_analysis"] = _generate_seo_keywords(outlets)


   state["message"] = ""
```

This method formats the input from both forms into the imported `user_prompt` and adds the formatted prompt to the `base_prompts` dictionary. It then generates the product description for the new food outlet, updates the SEO analysis, and clears the status message.

### Binding the elements and handler to the UI

Finalize your setup by binding the state elements and configuring the click handler to the UI components.

<Steps>
  <Step title="Bind text inputs to state elements">
    * **Outlet Name**: Click on the “Outlet name” Text Input component. In the Binding section of the component settings, set the state element to `outlet_form.name`.
    * **Character Max**: Move to the “Character max” Text Input. Update its state element binding to `outlet_form.character_max`.
  </Step>

  <Step title="Assign click handler to button">
    Click on the **Add and Generate** Button. In the Events section of the component settings, select `handle_add_outlet` for the `wf-click` event.
  </Step>

  <Step title="Configure form visibility">
    To conditionally display the form based on whether descriptions have been generated, click on the Section containing the form. In the Visibility section, choose “Custom” and set `product_descriptions.visible` as the “Visibility value.”
  </Step>
</Steps>

### Testing the finished product

To see the result of your hard work, click **Preview** in the top toolbar, enter some information into the original product description form, and click **Generate**. The “Add an outlet” form should appear once the product descriptions have been generated. Add a new example outlet name and a character max and click “Add and Generate.” You should see a new tab appear with your new outlet, as well as an updated SEO analysis chart.

<img src="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_13.png?fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=59ef5c5e0698b04cf625075ace0b9338" alt="Finished application" data-og-width="3220" width="3220" data-og-height="1478" height="1478" data-path="framework/images/tutorial/product_desciption/pd_gen_13.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_13.png?w=280&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=05bec1820af5f3d82f59be591dea578a 280w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_13.png?w=560&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=0f5a48f94d10930266fa2d96a749cadd 560w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_13.png?w=840&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=59f25090ea6058766b48616611449cbe 840w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_13.png?w=1100&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=2cc2e102409467d2afa635d12e01972d 1100w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_13.png?w=1650&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=e16c4506317a30b4c5f5ce1da859aa5d 1650w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/tutorial/product_desciption/pd_gen_13.png?w=2500&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=2ae801ff28a1ee5cc676e1237d7e9f19 2500w" />

You can add whatever additional form inputs you wish to the outlet form, but be sure to update `user_prompt` in the `prompts.py` file using your favorite editor.

## Conclusion

You’ve now built a full application with the Writer Framework and the Writer AI module. Congratulations! This application not only demonstrates the platform's capabilities but also provides a foundation on which you can build more complex applications. To learn more, explore the rest of the Writer Framework documentation and the API documentation.

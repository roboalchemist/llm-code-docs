# Source: https://docs.vast.ai/langflow-ollama.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Langflow + Ollama

<script
  type="application/ld+json"
  dangerouslySetInnerHTML={{
__html: JSON.stringify({
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Use Langflow with Ollama on Vast.ai",
  "description": "A step-by-step guide to setting up and using Langflow's node-based agent builder with Ollama for running open weight language models on Vast.ai's GPU instances.",
  "step": [
    {
      "@type": "HowToStep",
      "name": "Setup Account and Find the Template",
      "text": "Setup your Vast account and add credit by reviewing the quickstart guide. Find the Langflow template in the recommended templates page. Before loading it, click the pencil icon to open the template editor."
    },
    {
      "@type": "HowToStep",
      "name": "Configure Template Variables",
      "text": "In the template editor, configure OLLAMA_MODEL (the most important variable to choose which model should be downloaded when instance starts) and LANGFLOW_ARGS (allows you to pass alternative startup arguments to langflow application). When finished, click 'Create & Use' button to save your copy of the template."
    },
    {
      "@type": "HowToStep",
      "name": "Choose a GPU and Rent Instance",
      "text": "The most important consideration when picking an instance is VRAM. For best performance, model weights must fit into GPU VRAM with room for context window. You can use multi-GPU setups as an alternative to single high VRAM instances. Find a suitable instance and click the 'Rent' button to start the loading phase."
    },
    {
      "@type": "HowToStep",
      "name": "Access the Instance",
      "text": "After a short time, click the 'Open' button to access the Instance Portal. This page gives easy access to both Langflow application and Ollama API. Click Langflow's 'Launch Application' button. Note: It will take time for Langflow and Ollama to install and for the Ollama model to download. Monitor loading status in Instance Portal 'Logs' tab."
    },
    {
      "@type": "HowToStep",
      "name": "Create and Configure Workflow in Langflow",
      "text": "After opening Langflow, click 'Create first flow'. Select a workflow template (e.g., Content Generation -> Blog Writer). Replace the default Language Model node with the Ollama component from the left side menu. Configure Ollama node with Base URL 'http://localhost:11434', select your Ollama model, and reconnect the nodes. Customize workflow settings (URL, instructions, etc.) and click 'Run flow' button to execute."
    }
  ]
})
}}
/>

Langflow is a node-based agent builder you can use from your web browser.  While it integrates with many frontier language models it also has a fantastic Ollama integration which makes it really easy to use with open weight models as well as custom fine-tunes.

We have two templates you can choose for this guide.  The **Langflow template** provides both Ollama and Langflow installed within the instance.  You can also use the [**Ollama standalone template**](https://cloud.vast.ai/?ref_id=62897\&creator_id=62897\&name=Ollama) to integrate with a local langflow installation via [ssh local port forwarding](/documentation/instances/sshscp#Yj5Wh).  The choice is yours. For this guide we will use the Langflow bundled template.

Before moving on with the guide,**&#x20;Setup your Vast account and add credit**. Review the [quickstart guide](/documentation/get-started/quickstart) to get familar with the service if you do not have an account with credits loaded.

## Initial Setup

Let's get started with the configuration - There is not much you need to change here but it's a good idea to create a customized version of the template so Ollama automatically downloads your preferred model.

### Find the Template

You can find the Langflow template in our [recommended templates](https://cloud.vast.ai/templates/) page.  Before loading it up, click the pencil icon to open up the template editor

<Frame caption="Langflow Template">
    <img src="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents.webp?fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=4894e927eb3abf183b71e83feb7b99fd" alt="Langflow template card" data-og-width="800" width="800" data-og-height="518" height="518" data-path="images/use-cases-ai-agents.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents.webp?w=280&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=273a100e8135212393b375ea94a9cdcb 280w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents.webp?w=560&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=3e5b31f8217b7752cdbe5cd119f859bc 560w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents.webp?w=840&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=859b9a7c9927d4ffe5e49c3b0ef14447 840w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents.webp?w=1100&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=1ac547d0dd85e01886e96689b7225a59 1100w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents.webp?w=1650&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=01720ba1c6d8f9f8827e70cdee8f14fc 1650w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents.webp?w=2500&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=07712a78a33eb9594526b1f90fb5e5a0 2500w" />
</Frame>

### Custom configuration

In the template editor you'll find two really useful configuration variables.

* `OLLAMA_MODEL` is the most important variable.  Here you can choose which model should be downloaded when the instance starts.
* `LANGFLOW_ARGS`allows you to pass alternative startup arguments to the langflow application.  The defaults should be fine for this demo, but you are free to change these as you need.

<img src="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-2.webp?fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=3e1803266c92d85e7641de9e5e5240a7" alt="" data-og-width="942" width="942" data-og-height="172" height="172" data-path="images/use-cases-ai-agents-2.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-2.webp?w=280&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=92c4b909fa03f3441a720f6863a7a863 280w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-2.webp?w=560&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=2de4688fae01b5e9838b2f3024cb8061 560w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-2.webp?w=840&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=510217d0b0eca19a3f6fb6b2e205a9b2 840w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-2.webp?w=1100&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=23c4a49b82270bacf5c544d1b3ae0fdd 1100w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-2.webp?w=1650&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=ad7a28d4ffa45913839fe7f61dba5007 1650w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-2.webp?w=2500&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=001332169c1fc771143ab995b5b2f22a 2500w" />

When you have finished entering your settings click the '**Create & Use**' button to save your copy of the template.

You'll be taken to the search interface where you can choose an appropriate GPU instance to run your model.  You can access your custom template in future from the 'My Templates' section of the templates page.

## Starting the Instance

It's now time to use your template to start a GPU instance.

### Choose a GPU

The most important consideration when picking an instance to run language models is the VRAM.  For best performance, your model weights must fit into the GPU VRAM with room left over for the context window.&#x20;

You do not have to use a single GPU when running LLMs - Sometimes a multi-GPU setup can be as effective of better than a single high VRAM instance.

### Rent an Instance

When you have found a suitable instance it's time to click the '**Rent**' button.  This will start the loading phase.

<Note>
  If you are not sure which instance to choose - Try one.  There is no minimum rental period and if it is not suitable you are able to destroy that instance and start another, paying only for the time the instance was in the 'running' state
</Note>

## Accessing the Instance

After a short time, your instance will be ready to access.  Simply click the 'Open' button to get started.

<img src="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-3.webp?fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=ad8aef19558d8a9b5e30ba3f6a8f4c17" alt="" data-og-width="917" width="917" data-og-height="225" height="225" data-path="images/use-cases-ai-agents-3.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-3.webp?w=280&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=2484c5ca420241ba1eb64c992065df43 280w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-3.webp?w=560&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=b06d59c62b4ad581514bf5d3b4d2b026 560w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-3.webp?w=840&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=b67fa69a5b16ecad06ab676262a92ab6 840w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-3.webp?w=1100&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=11e49321ea2183a77833fe2d924de79d 1100w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-3.webp?w=1650&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=37d9c1e7458b1a22e21578e39cc97d89 1650w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-3.webp?w=2500&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=0b62717f36ef9cc571b4986b8a033941 2500w" />

You will now find the Instance Portal has opened.&#x20;

<Frame caption="Instance Portal">
    <img src="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-4.webp?fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=768955d5c2635603121144a5bc474fd6" alt="Instance Portal" data-og-width="1149" width="1149" data-og-height="726" height="726" data-path="images/use-cases-ai-agents-4.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-4.webp?w=280&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=81706186ff63c088f469cb700a3396b4 280w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-4.webp?w=560&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=283b158e484858b3648e38a40538a912 560w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-4.webp?w=840&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=9593370ae0d6c992df9bd6fc629ae031 840w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-4.webp?w=1100&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=d314e8ab7de123d2e1ca865bf4ba7c5f 1100w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-4.webp?w=1650&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=d270be5f688126695ff08265ed11a50d 1650w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-4.webp?w=2500&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=eedd4ad13919c3fe1d75bdac9dd1e1f8 2500w" />
</Frame>

This page gives you easy access to both the Langflow application and the Ollama API.  Click Langflow's 'Launch Application' button.&#x20;

<Note>
  It will take some time for Langflow and Ollama to be installed and for the Ollama model to download.  You can monitor the loading status in the Instance Portal 'Logs' tab&#x20;
</Note>

## Getting Started with Langflow

After opening Langflow, click the '**Create first flow**' button.

<img src="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-5.webp?fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=5ef99a459c076fc71d54e1800c479769" alt="" data-og-width="800" width="800" data-og-height="749" height="749" data-path="images/use-cases-ai-agents-5.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-5.webp?w=280&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=f32d45f14eb2906952cbe7ab82aa1aec 280w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-5.webp?w=560&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=318b5d55c7dcabd82133b20a608a1ee4 560w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-5.webp?w=840&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=4e14674adaedbae2f6e96c6c36e33813 840w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-5.webp?w=1100&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=37d0528a5d2ba65cf527ffde7a65c0b6 1100w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-5.webp?w=1650&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=8f85f3aede63e4d1fd561b84141b9e1b 1650w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-5.webp?w=2500&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=83bf931e433abdd97ad2371b4ac38c9f 2500w" />

While Langflow is extremely powerful, for this example we will create a simple blow post writer.

Select **Content Generation** -> **Blog Writer**

<img src="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-6.webp?fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=c380220d81e56ecaea1f07dc7382824e" alt="" data-og-width="1242" width="1242" data-og-height="665" height="665" data-path="images/use-cases-ai-agents-6.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-6.webp?w=280&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=b5ae2a71a2ae2e90fe69a51c33642c5f 280w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-6.webp?w=560&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=b11251edb3ea1e922416dc027c639e5d 560w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-6.webp?w=840&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=160b9b87fc78ca7ca13b8763858cd67f 840w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-6.webp?w=1100&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=02eee6eb8f779b2cee683f325493c47e 1100w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-6.webp?w=1650&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=878a352258a7a539347cbbf3f7e984da 1650w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-6.webp?w=2500&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=fc187e3bc9abc309956a7aba0cb7e502 2500w" />

Initially, the flow will look like this

<Frame caption="Blog Writer Defaults">
    <img src="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-7.webp?fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=921b66728895c8c3e1bd66ef8adca884" alt="blog writer flow" data-og-width="1280" width="1280" data-og-height="455" height="455" data-path="images/use-cases-ai-agents-7.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-7.webp?w=280&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=65cef733272b3985106eee5695080205 280w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-7.webp?w=560&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=eebcf345024da263fd589ef382fac8d8 560w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-7.webp?w=840&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=3c8c3c6d7f5bfa0efb48a54297942547 840w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-7.webp?w=1100&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=1023e60f00767d3ed09fa5febfa2635d 1100w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-7.webp?w=1650&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=5d4f9010d55c1f6fa3fbaa8f4d695276 1650w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-7.webp?w=2500&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=6e87512b6469df366c1c8730457c278d 2500w" />
</Frame>

We will need to replace the Language Model with the Ollama alternative to make use of the GPU and avoid having to make API calls to external services.&#x20;

Click on the **Language Model** node and using the three dot icon, choose **Delete.**

<Frame caption="Delete Language Model">
    <img src="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-8.webp?fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=c794d16e4c1881ba9c3519d6a7c1051d" alt="delete language model" data-og-width="800" width="800" data-og-height="938" height="938" data-path="images/use-cases-ai-agents-8.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-8.webp?w=280&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=d6fb89ceb811a6495523bf2b0dce271f 280w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-8.webp?w=560&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=1e21f7c2da8eb06945a06357568f3d56 560w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-8.webp?w=840&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=c242353a7341ee633334398e43dd2b67 840w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-8.webp?w=1100&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=1ba931100a28cd3566e68a961ada8dd1 1100w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-8.webp?w=1650&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=daf93cb3369b835ee12818d25d4ddff7 1650w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-8.webp?w=2500&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=0511c078357a838e3519767bedb8950c 2500w" />
</Frame>

Next, from the left side menu, select the **Ollama** component and drag it to the space created by deleting the original language model component.

<Frame caption="Add Ollama Node">
    <img src="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-9.webp?fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=66e249067470e2c74be5ccfd965556e8" alt="Add Ollama node" data-og-width="800" width="800" data-og-height="843" height="843" data-path="images/use-cases-ai-agents-9.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-9.webp?w=280&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=18abfc9ce3b6ab95ba7a9a899d9c359d 280w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-9.webp?w=560&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=46485863fffed4f8a33428fbebf375a1 560w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-9.webp?w=840&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=a6748a0828df0e1de0dec0339f987cc3 840w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-9.webp?w=1100&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=79600066b518a1a7412c264640f7ba19 1100w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-9.webp?w=1650&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=303005a34ab24f135100c4d2487d41b3 1650w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-9.webp?w=2500&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=11b1ac1efa569b6e94acb76a6a4eb7db 2500w" />
</Frame>

Now that is in place it must be configured to communicate with the Ollama API. Enter `http://localhost:11434` in the Base URL field.  You'll need to then select your Ollama model and re-connect the nodes as shown below.

<Frame caption="Ollama Node Connected">
    <img src="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-10.webp?fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=19f569fdc75304ba01faf90a41a8f8e1" alt="Ollama node connected" data-og-width="1280" width="1280" data-og-height="466" height="466" data-path="images/use-cases-ai-agents-10.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-10.webp?w=280&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=2ea9378bb2d757d8d161dc634811d51f 280w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-10.webp?w=560&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=cfb34dc5039310feb083e29dab019348 560w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-10.webp?w=840&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=5daa888965fe175b693998c0b94af19b 840w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-10.webp?w=1100&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=5114cf922b22f1fc9963d89990503b81 1100w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-10.webp?w=1650&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=8db43998f81bc8880ce3397d6417e3aa 1650w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-10.webp?w=2500&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=39b5bb30cfece65c6595a768ff1cb400 2500w" />
</Frame>

<Note>
  If the model field does not immediately show your available models, simply toggle the 'Tool Mode Enabled' switch.
</Note>

### Configuring the Workflow

You could run this node immediately, but first let's make some minor modifications.

Change the **URL** in the **URL node** to `https://vast.ai`and set the **Depth** to `2`

Change the **Text** in the **Instructions node** to `Use the references above for style to write a new blog/tutorial about how Vast.ai can empower people who want to leverage affordable GPU resources`

### Run the Workflow

Simply click the **Playground** button followed by the **Run flow** button and wait for the agent to learn about the subject matter and write a blog post.  It'll only take a few seconds.

<Frame caption="Completed Blog Post">
    <img src="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-11.webp?fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=a169244ebdb342711ed2a3fb5281ffbe" alt="Completed Blog Post" data-og-width="846" width="846" data-og-height="893" height="893" data-path="images/use-cases-ai-agents-11.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-11.webp?w=280&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=e04736deab750dd351af117ff5ba4201 280w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-11.webp?w=560&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=1aea70978d5d26bd72b9b84cf70f4216 560w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-11.webp?w=840&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=116b39f1295baccaa1a5b44551a4722c 840w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-11.webp?w=1100&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=7ee1818360fa1c074a75a0fb983b59fc 1100w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-11.webp?w=1650&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=fe888bd8e8f9385696f5407640b5edfd 1650w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-agents-11.webp?w=2500&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=4d2192bc86177af51696c5978611ee1b 2500w" />
</Frame>

## Advanced Usage

This short guide serves only as an introduction to Langflow, but it is extremely capabale and easy to use with some practice.  We recommend that you check out the excellent [documentation](https://docs.langflow.org/about-langflow) to assist you in creating complex projects.

Remember, any *Language Model* component can be replaced with the *Ollama* component, and any *Agent* component can be configured to use *Ollama* as a custom provider.

# Source: https://docs.embedchain.ai/deployment/gradio_app.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Gradio.app

> Deploy your RAG application to gradio.app platform

Embedchain offers a Streamlit template to facilitate the development of RAG chatbot applications in just three easy steps.

Follow the instructions given below to deploy your first application quickly:

## Step-1: Create RAG app

We provide a command line utility called `ec` in embedchain that inherits the template for `gradio.app` platform and help you deploy the app. Follow the instructions to create a gradio.app app using the template provided:

```bash Install embedchain theme={null}
pip install embedchain
```

```bash Create application theme={null}
mkdir my-rag-app
ec create --template=gradio.app
```

This will generate a directory structure like this:

```bash  theme={null}
├── app.py
├── embedchain.json
└── requirements.txt
```

Feel free to edit the files as required.

* `app.py`: Contains API app code
* `embedchain.json`: Contains embedchain specific configuration for deployment (you don't need to configure this)
* `requirements.txt`: Contains python dependencies for your application

## Step-2: Test app locally

You can run the app locally by simply doing:

```bash Run locally theme={null}
pip install -r requirements.txt
ec dev
```

## Step-3: Deploy to gradio.app

```bash Deploy to gradio.app theme={null}
ec deploy
```

This will run `gradio deploy` which will prompt you questions and deploy your app directly to huggingface spaces.

<img src="https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/gradio_app.png?fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=b2849b80a507a23f03f59e927180cfcd" alt="gradio app" data-og-width="2852" width="2852" data-og-height="1634" height="1634" data-path="images/gradio_app.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/gradio_app.png?w=280&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=5636ccb92bb1b63ea05731196bed2d74 280w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/gradio_app.png?w=560&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=3fa054d8f1f70baa66ab0b4a5293dbe8 560w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/gradio_app.png?w=840&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=deb07e82609cd541dd3c1eacb9f31c3c 840w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/gradio_app.png?w=1100&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=f8cf72082dae2305be9f6f3c212d5547 1100w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/gradio_app.png?w=1650&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=53bdfd24a9a89f0116a5e2d7b05a28b7 1650w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/gradio_app.png?w=2500&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=dc38e29994155c95632dc62bcf7167d7 2500w" />

## Seeking help?

If you run into issues with deployment, please feel free to reach out to us via any of the following methods:

<Snippet file="get-help.mdx" />

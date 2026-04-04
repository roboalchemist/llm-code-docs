# Source: https://docs.embedchain.ai/deployment/render_com.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Render.com

> Deploy your RAG application to render.com platform

Embedchain has a nice and simple abstraction on top of the [render.com](https://render.com/) tools to let developers deploy RAG application to render.com platform seamlessly.

Follow the instructions given below to deploy your first application quickly:

## Step-1: Install `render` command line

<CodeGroup>
  ```bash OSX theme={null}
  brew tap render-oss/render
  brew install render
  ```

  ```bash Linux theme={null}
  # Make sure you have deno installed -> https://docs.render.com/docs/cli#from-source-unsupported-operating-systems
  git clone https://github.com/render-oss/render-cli
  cd render-cli
  make deps
  deno task run
  deno compile
  ```

  ```bash Windows theme={null}
  choco install rendercli
  ```
</CodeGroup>

In case you run into issues, refer to official [render.com docs](https://docs.render.com/docs/cli).

## Step-2 Create RAG application:

We provide a command line utility called `ec` in embedchain that inherits the template for `render.com` platform and help you deploy the app. Follow the instructions to create a render.com app using the template provided:

```bash Create application theme={null}
pip install embedchain
mkdir my-rag-app
ec create --template=render.com
```

This `create` command will open a browser window and ask you to login to your render.com account and will generate a directory structure like this:

```bash  theme={null}
├── app.py
├── .env
├── render.yaml
├── embedchain.json
└── requirements.txt
```

Feel free to edit the files as required.

* `app.py`: Contains API app code
* `.env`: Contains environment variables for production
* `render.yaml`: Contains render.com specific configuration for deployment (configure this according to your needs, follow [this](https://docs.render.com/docs/blueprint-spec) for more info)
* `embedchain.json`: Contains embedchain specific configuration for deployment (you don't need to configure this)
* `requirements.txt`: Contains python dependencies for your application

## Step-3: Test app locally

You can run the app locally by simply doing:

```bash Run locally theme={null}
pip install -r requirements.txt
ec dev
```

## Step-4: Deploy to render.com

Before deploying to render.com, you only have to set up one thing.

In the render.yaml file, make sure to modify the repo key by inserting the URL of your Git repository where your application will be hosted. You can create a repository from [GitHub](https://github.com) or [GitLab](https://gitlab.com/users/sign_in).

After that, you're ready to deploy on render.com.

```bash Deploy app theme={null}
ec deploy
```

When you run this, it should open up your render dashboard and you can see the app being deployed. You can find your hosted link over there only.

You can also check the logs, monitor app status etc on their dashboard by running command `render dashboard`.

<img src="https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fly_io.png?fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=0aa9e31a9beed2a53eafce3b1f677f07" data-og-width="2892" width="2892" data-og-height="1592" height="1592" data-path="images/fly_io.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fly_io.png?w=280&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=10df3c3ae0a3f669410e20d4a9505377 280w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fly_io.png?w=560&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=3ff240394115f455aafc232527b71e8c 560w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fly_io.png?w=840&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=ee8effc2f3c044353794129a3834a6ad 840w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fly_io.png?w=1100&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=14c42bac49c7ab38566373e5876fc09d 1100w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fly_io.png?w=1650&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=79ac4dd5e6d44e71c3deb5d29941c0aa 1650w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fly_io.png?w=2500&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=4a13bad7935459e7e73626f11b59a67f 2500w" />

## Seeking help?

If you run into issues with deployment, please feel free to reach out to us via any of the following methods:

<Snippet file="get-help.mdx" />

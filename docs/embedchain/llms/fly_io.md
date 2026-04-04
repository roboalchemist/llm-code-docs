# Source: https://docs.embedchain.ai/deployment/fly_io.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Fly.io

> Deploy your RAG application to fly.io platform

Embedchain has a nice and simple abstraction on top of the [Fly.io](https://fly.io/) tools to let developers deploy RAG application to fly.io platform seamlessly.

Follow the instructions given below to deploy your first application quickly:

## Step-1: Install flyctl command line

<CodeGroup>
  ```bash OSX theme={null}
  brew install flyctl
  ```

  ```bash Linux theme={null}
  curl -L https://fly.io/install.sh | sh
  ```

  ```bash Windows theme={null}
  pwsh -Command "iwr https://fly.io/install.ps1 -useb | iex"
  ```
</CodeGroup>

Once you have installed the fly.io cli tool, signup/login to their platform using the following command:

<CodeGroup>
  ```bash Sign up theme={null}
  fly auth signup
  ```

  ```bash Sign in theme={null}
  fly auth login
  ```
</CodeGroup>

In case you run into issues, refer to official [fly.io docs](https://fly.io/docs/hands-on/install-flyctl/).

## Step-2: Create RAG app

We provide a command line utility called `ec` in embedchain that inherits the template for `fly.io` platform and help you deploy the app. Follow the instructions to create a fly.io app using the template provided:

```bash Install embedchain theme={null}
pip install embedchain
```

```bash Create application theme={null}
mkdir my-rag-app
ec create --template=fly.io
```

This will generate a directory structure like this:

```bash  theme={null}
├── Dockerfile
├── app.py
├── fly.toml
├── .env
├── .env.example
├── embedchain.json
└── requirements.txt
```

Feel free to edit the files as required.

* `Dockerfile`: Defines the steps to setup the application
* `app.py`: Contains API app code
* `fly.toml`: fly.io config file
* `.env`: Contains environment variables for production
* `.env.example`: Contains dummy environment variables (can ignore this file)
* `embedchain.json`: Contains embedchain specific configuration for deployment (you don't need to configure this)
* `requirements.txt`: Contains python dependencies for your application

## Step-3: Test app locally

You can run the app locally by simply doing:

```bash Run locally theme={null}
pip install -r requirements.txt
ec dev
```

## Step-4: Deploy to fly.io

You can deploy to fly.io using the following command:

```bash Deploy app theme={null}
ec deploy
```

Once this step finished, it will provide you with the deployment endpoint where you can access the app live. It will look something like this (Swagger docs):

You can also check the logs, monitor app status etc on their dashboard by running command `fly dashboard`.

<img src="https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fly_io.png?fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=0aa9e31a9beed2a53eafce3b1f677f07" data-og-width="2892" width="2892" data-og-height="1592" height="1592" data-path="images/fly_io.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fly_io.png?w=280&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=10df3c3ae0a3f669410e20d4a9505377 280w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fly_io.png?w=560&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=3ff240394115f455aafc232527b71e8c 560w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fly_io.png?w=840&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=ee8effc2f3c044353794129a3834a6ad 840w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fly_io.png?w=1100&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=14c42bac49c7ab38566373e5876fc09d 1100w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fly_io.png?w=1650&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=79ac4dd5e6d44e71c3deb5d29941c0aa 1650w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fly_io.png?w=2500&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=4a13bad7935459e7e73626f11b59a67f 2500w" />

## Seeking help?

If you run into issues with deployment, please feel free to reach out to us via any of the following methods:

<Snippet file="get-help.mdx" />

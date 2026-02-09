# Source: https://docs.embedchain.ai/get-started/full-stack.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 💻 Full stack

Get started with full-stack RAG applications using Embedchain's easy-to-use CLI tool. Set up everything with just a few commands, whether you prefer Docker or not.

## Prerequisites

Choose your setup method:

* [Without docker](#without-docker)
* [With Docker](#with-docker)

### Without Docker

Ensure these are installed:

* Embedchain python package (`pip install embedchain`)
* [Node.js](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) and [Yarn](https://classic.yarnpkg.com/lang/en/docs/install/)

### With Docker

Install Docker from [Docker's official website](https://docs.docker.com/engine/install/).

## Quick Start Guide

### Install the package

Before proceeding, make sure you have the Embedchain package installed.

```bash  theme={null}
pip install embedchain -U
```

### Setting Up

For the purpose of the demo, you have to set `OPENAI_API_KEY` to start with but you can choose any llm by changing the configuration easily.

### Installation Commands

<CodeGroup>
  ```bash without docker theme={null}
  ec create-app my-app
  cd my-app
  ec start
  ```

  ```bash with docker theme={null}
  ec create-app my-app --docker
  cd my-app
  ec start --docker
  ```
</CodeGroup>

### What Happens Next?

1. Embedchain fetches a full stack template (FastAPI backend, Next.JS frontend).
2. Installs required components.
3. Launches both frontend and backend servers.

### See It In Action

Open [http://localhost:3000](http://localhost:3000) to view the chat UI.

<img src="https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fullstack.png?fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=7363841f4336e4bebcef4962525a77a5" alt="full stack example" data-og-width="3116" width="3116" data-og-height="2104" height="2104" data-path="images/fullstack.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fullstack.png?w=280&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=e6013b6b4a42090b9aebbe76360befe0 280w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fullstack.png?w=560&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=98c3682d0e56f7c3eaa944d02e36089b 560w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fullstack.png?w=840&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=78705b25b2c734a35dcb732b17344823 840w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fullstack.png?w=1100&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=9694826d8e248278087e2f1139668a16 1100w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fullstack.png?w=1650&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=5cad7a0a212c61c55d9d4eb1fa1df2b4 1650w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fullstack.png?w=2500&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=ad8addaf3cbdd034e617c28e4e1688bf 2500w" />

### Admin Panel

Check out the Embedchain admin panel to see the document chunks for your RAG application.

<img src="https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fullstack-chunks.png?fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=fcf336ad71c16c66b37744acf7afee99" alt="full stack chunks" data-og-width="2526" width="2526" data-og-height="1866" height="1866" data-path="images/fullstack-chunks.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fullstack-chunks.png?w=280&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=8e0f9b00e35f5e0a07f4f31b6bf28ac8 280w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fullstack-chunks.png?w=560&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=aa3bc3e8e2413da218269b5b9c6ba1dd 560w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fullstack-chunks.png?w=840&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=b818010e3594d5421be3d5b63f5a59bf 840w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fullstack-chunks.png?w=1100&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=19d5d3076890511d2661a99568089d0e 1100w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fullstack-chunks.png?w=1650&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=503e46917a2e3a8e966359c845ddbf88 1650w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fullstack-chunks.png?w=2500&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=4f4e364e93a79103f93c9e860b8f3885 2500w" />

### API Server

If you want to access the API server, you can do so at [http://localhost:8000/docs](http://localhost:8000/docs).

<img src="https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fullstack-api-server.png?fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=7603f950f746c20e429b64088cd839d7" alt="API Server" data-og-width="2980" width="2980" data-og-height="1728" height="1728" data-path="images/fullstack-api-server.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fullstack-api-server.png?w=280&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=7f4ee4bf9906e445c5d4a35c17fc9d5f 280w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fullstack-api-server.png?w=560&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=275eab0247d9f4846e4b773fdaf0e97a 560w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fullstack-api-server.png?w=840&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=cdd7f4837de8b1bbdfd0db04c1f22fd7 840w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fullstack-api-server.png?w=1100&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=28d6d8bc9c81a3d538e86ba1d5c23069 1100w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fullstack-api-server.png?w=1650&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=53c0dfd99c608ecff453433f1379afa8 1650w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/fullstack-api-server.png?w=2500&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=13320d08662aaa36f902733faa9920e7 2500w" />

You can customize the UI and code as per your requirements.

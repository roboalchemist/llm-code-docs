# Source: https://docs.embedchain.ai/examples/slack-AI.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# null

[Embedchain Examples Repo](https://github.com/embedchain/examples) contains code on how to build your own Slack AI to chat with the unstructured data lying in your slack channels.

<img src="https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/slack-ai.png?fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=35a7bc2e04f1619f25e939532e342607" alt="Slack AI Demo" data-og-width="2630" width="2630" data-og-height="2140" height="2140" data-path="images/slack-ai.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/slack-ai.png?w=280&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=858368e83709c5cb0feda8d911816529 280w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/slack-ai.png?w=560&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=2834586a894fdb02ebd8d57ea0202732 560w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/slack-ai.png?w=840&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=7689ac5bbe8088f9a675ed4afa5d56a5 840w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/slack-ai.png?w=1100&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=18c0fafce6c18946c35761cea459b033 1100w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/slack-ai.png?w=1650&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=0bf813bd2db2f13f794432906634db0a 1650w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/slack-ai.png?w=2500&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=d5cd03b6c8abc89a2de1633c8b60c222 2500w" />

## Getting started

Create a Slack AI involves 3 steps

* Create slack user
* Set environment variables
* Run the app locally

### Step 1: Create Slack user token

Follow the steps given below to fetch your slack user token to get data through Slack APIs:

1. Create a workspace on Slack if you don’t have one already by clicking [here](https://slack.com/intl/en-in/).

2. Create a new App on your Slack account by going [here](https://api.slack.com/apps).

3. Select `From Scratch`, then enter the App Name and select your workspace.

4. Navigate to `OAuth & Permissions` tab from the left sidebar and go to the `scopes` section. Add the following scopes under `User Token Scopes`:

   ```
   # Following scopes are needed for reading channel history
   channels:history
   channels:read

   # Following scopes are needed to fetch list of channels from slack
   groups:read
   mpim:read
   im:read
   ```

5. Click on the `Install to Workspace` button under `OAuth Tokens for Your Workspace` section in the same page and install the app in your slack workspace.

6. After installing the app you will see the `User OAuth Token`, save that token as you will need to configure it as `SLACK_USER_TOKEN` for this demo.

### Step 2: Set environment variables

Navigate to `api` folder and set your `HUGGINGFACE_ACCESS_TOKEN` and `SLACK_USER_TOKEN` in `.env.example` file. Then rename the `.env.example` file to `.env`.

<Note>
  By default, we use `Mixtral` model from Hugging Face. However, if you prefer to use OpenAI model, then set `OPENAI_API_KEY` instead of `HUGGINGFACE_ACCESS_TOKEN` along with `SLACK_USER_TOKEN` in `.env` file, and update the code in `api/utils/app.py` file to use OpenAI model instead of Hugging Face model.
</Note>

### Step 3: Run app locally

Follow the instructions given below to run app locally based on your development setup (with docker or without docker):

#### With docker

```bash  theme={null}
docker-compose build
ec start --docker
```

#### Without docker

```bash  theme={null}
ec install-reqs
ec start
```

Finally, you will have the Slack AI frontend running on [http://localhost:3000](http://localhost:3000). You can also access the REST APIs on [http://localhost:8000](http://localhost:8000).

## Credits

This demo was built using the Embedchain's [full stack demo template](https://docs.embedchain.ai/get-started/full-stack). Follow the instructions [given here](https://docs.embedchain.ai/get-started/full-stack) to create your own full stack RAG application.

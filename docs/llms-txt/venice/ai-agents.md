# Source: https://docs.venice.ai/overview/guides/ai-agents.md

# AI Agents

> Venice is supported with the following AI Agent communities.

* [Coinbase Agentkit](https://www.coinbase.com/developer-platform/discover/launches/introducing-agentkit)

* [Eliza](https://github.com/ai16z/eliza) - Venice support introduced via this [PR](https://github.com/ai16z/eliza/pull/1008).

## Eliza Instructions

To setup Eliza with Venice, follow these instructions. A full blog post with more detail can be found [here](https://venice.ai/blog/how-to-build-a-social-media-ai-agent-with-elizaos-venice-api).

* Clone the Eliza repository:

```bash  theme={null}
# Clone the repository
git clone https://github.com/ai16z/eliza.git
```

* Copy `.env.example` to `.env`

* Update `.env` specifying your `VENICE_API_KEY`, and model selections for  `SMALL_VENICE_MODEL`, `MEDIUM_VENICE_MODEL`, `LARGE_VENICE_MODEL`, `IMAGE_VENICE_MODEL`, instructions on generating your key can be found [here](/overview/guides/generating-api-key).

* Create a new character in the `/characters/` folder with a filename similar to  `your_character.character.json`to specify the character profile, tools/functions, and Venice.ai as the model provider:

```typescript  theme={null}
   modelProvider: "venice"
```

* Build the repo:

```bash  theme={null}
pnpm i
pnpm build
pnpm start
```

* Start your character

```bash  theme={null}
pnpm start --characters="characters/<your_character>.character.json"
```

* Start the local UI to chat with the agent

<img src="https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/eliza-config.png?fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=d6dff632864fd7a54e6ba3d2d558fd0a" alt="" data-og-width="1172" width="1172" data-og-height="1002" height="1002" data-path="images/eliza-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/eliza-config.png?w=280&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=cf44735fc0525bf0427569ec6831c8ac 280w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/eliza-config.png?w=560&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=f1a8a917ac07b317bd0dc6f8d58b9e23 560w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/eliza-config.png?w=840&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=6ef04f414b49054af6f71e08102ceb7f 840w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/eliza-config.png?w=1100&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=6a4ca049a1f1e9f1c409fa5d5bc98ed1 1100w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/eliza-config.png?w=1650&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=6026f1fdf6cca494e93a94c68b8f57f6 1650w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/eliza-config.png?w=2500&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=ec0b898e6060ab5b2a1f62751a2ce78e 2500w" />

# Source: https://upstash.com/docs/vector/integrations/flowise.md

# Flowise with Upstash Vector and Redis

Flowise is an open source low-code tool for developers to build customized LLM orchestration flows & AI agents. With Upstash Vector and Upstash Redis, you can extend your Flowise flows to include semantic search, caching, and conversation memory.

## Install

To get started, you can install Flowise locally using npm. Run:

```bash  theme={"system"}
npm install -g flowise
```

Start Flowise:

```bash  theme={"system"}
npx flowise start
```

Open: [http://localhost:3000](http://localhost:3000)

You also need to set up Upstash services:

1. Create a **Vector Index** in the [Upstash Console](https://console.upstash.com/vector). To learn more about index creation, you can check out [this page](https://docs.upstash.com/vector/overall/getstarted).
2. Create a **Redis Database** in the [Upstash Console](https://console.upstash.com/redis). To learn more about Redis database creation, you can check out [this page](/redis/overall/getstarted).

## Nodes Overview

Flowise supports multiple Upstash integrations. Below are the nodes and their functionalities:

### 1. Upstash Vector Node

Use the **Upstash Vector** node to perform semantic search and store document embeddings. Connect the node to document loaders and embedding components for indexing and querying.

<Frame>
  <img width="400" src="https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/flowise/vector-node.png?fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=2e16b449c650649ad9eb43dfbf73dd61" data-og-width="944" data-og-height="1520" data-path="img/vector/integrations/flowise/vector-node.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/flowise/vector-node.png?w=280&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=7c2671aafc53cab72b69bac48b1eeeb5 280w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/flowise/vector-node.png?w=560&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=0acc859973a46c88f510e4bdecb0c6e0 560w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/flowise/vector-node.png?w=840&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=ce251d9e914a6f5c9959a28a6c086367 840w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/flowise/vector-node.png?w=1100&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=bc953d3bb70dfcaf59814acdc7224933 1100w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/flowise/vector-node.png?w=1650&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=96370edc23725834cc9cf7cee4e17bbf 1650w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/flowise/vector-node.png?w=2500&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=75707988865124b42159f142d587e5d4 2500w" />
</Frame>

### 2. Upstash Redis Cache Node

The **Upstash Redis Cache** node caches LLM responses in a serverless Redis database.

<Frame>
  <img width="400" src="https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/flowise/cache-node.png?fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=29fe2a921e26ac2b2fe95870b7be167b" data-og-width="1300" data-og-height="1192" data-path="img/vector/integrations/flowise/cache-node.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/flowise/cache-node.png?w=280&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=5c43b8ebcabbf4c440006155212e6e58 280w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/flowise/cache-node.png?w=560&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=8baf075e02d0620895841829943b86ea 560w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/flowise/cache-node.png?w=840&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=bbf03f13809134617a60d5f6c943e9c6 840w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/flowise/cache-node.png?w=1100&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=a50f298127802a6e55ab092341d8ae35 1100w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/flowise/cache-node.png?w=1650&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=05b4f8c8be9f3c3ef64295ca0779d683 1650w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/flowise/cache-node.png?w=2500&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=b03856afca6a62de3ed0b0a3d85a9db3 2500w" />
</Frame>

### 3. Upstash Redis-Backed Chat Memory Node

The **Upstash Redis-Backed Chat Memory** node summarizes conversations and stores the memory in Redis. This enables persistent, context-aware interactions across multiple sessions.

<Frame>
  <img width="400" src="https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/flowise/chat-memory-node.png?fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=5df675581ac40ed4ea0a3bb4d37915a2" data-og-width="1146" data-og-height="1602" data-path="img/vector/integrations/flowise/chat-memory-node.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/flowise/chat-memory-node.png?w=280&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=d71367b889d24ae1253cea24bef7fd18 280w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/flowise/chat-memory-node.png?w=560&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=955fed5268e0900561e99fbb981e795f 560w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/flowise/chat-memory-node.png?w=840&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=3ac3bc7a5f37ec677d78f94c82ef3037 840w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/flowise/chat-memory-node.png?w=1100&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=3a4cacbe3799aacf776b5274a1b1e7e6 1100w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/flowise/chat-memory-node.png?w=1650&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=daecd49a5208fda423b4a3620a6a6e97 1650w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/flowise/chat-memory-node.png?w=2500&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=3346c12d18ec3d8a74d499b50d371d7c 2500w" />
</Frame>

## Example Flow

Below is an example flow using Upstash Vector:

<Frame caption="You can use a document loader to upload documents and connect it to the Upstash Vector node for indexing.">
  <img src="https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/flowise/flow.png?fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=97ad1ff7a88bf6dfd60f99dd54071637" data-og-width="2136" width="2136" data-og-height="1544" height="1544" data-path="img/vector/integrations/flowise/flow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/flowise/flow.png?w=280&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=c7c7d3097ae887609b8315e0b30ce971 280w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/flowise/flow.png?w=560&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=8cd669a856f13292499a86abbeedc7ac 560w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/flowise/flow.png?w=840&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=c7c828cabd82c11606d5d1153ed54579 840w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/flowise/flow.png?w=1100&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=58b5af8a786f3b82e1de8ec09629023a 1100w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/flowise/flow.png?w=1650&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=06bd5dcbb1aa3b4e7d5adaed5ef04a86 1650w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/flowise/flow.png?w=2500&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=34be8a588c5d5041ac542899fc3380f6 2500w" />
</Frame>

## Learn More

For more details, visit the [Flowise documentation](https://docs.flowiseai.com/).

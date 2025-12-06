# Nomic Documentation

Source: https://docs.nomic.ai/reference/typescript-api/overview

You can interact with the Nomic Atlas platform in Typescript with the official typescript bindings.

### Installation​

```
npm install nomic-ai/atlas
```

### Embeddings​

```
import { embed } from '@nomic-ai/atlas';embed(['so much depends upon', 'a red wheel barrow'], `nk-123456789`).then(  (embeddings) => console.log({ embeddings }));
```

- Installation
- Embeddings

# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/GgufMetadataTokenizer.md

---
url: /api/type-aliases/GgufMetadataTokenizer.md
---
# Type Alias: GgufMetadataTokenizer

```ts
type GgufMetadataTokenizer = {
  ggml: {
     model:   | "no_vocab"
        | "none"
        | "llama"
        | "gpt2"
        | "bert"
        | "rwkv"
        | "t5"
        | "plamo2"
        | string;
     pre?:   | "default"
        | "llama3"
        | "llama-v3"
        | "llama-bpe"
        | "deepseek-llm"
        | "deepseek-coder"
        | "falcon"
        | "falcon3"
        | "pixtral"
        | "mpt"
        | "starcoder"
        | "gpt-2"
        | "phi-2"
        | "jina-es"
        | "jina-de"
        | "jina-v1-en"
        | "jina-v2-es"
        | "jina-v2-de"
        | "jina-v2-code"
        | "refact"
        | "command-r"
        | "qwen2"
        | "stablelm2"
        | "olmo"
        | "dbrx"
        | "smaug-bpe"
        | "poro-chat"
        | "chatglm-bpe"
        | "viking"
        | "jais"
        | "tekken"
        | "smollm"
        | "codeshell"
        | "bloom"
        | "gpt3-finnish"
        | "exaone"
        | "exaone4"
        | "chameleon"
        | "minerva-7b"
        | "megrez"
        | "gpt-4o"
        | "superbpe"
        | "trillion"
        | "bailingmoe"
        | "a.x-4.0"
        | "mellum"
        | string;
     tokens: readonly string[];
     token_type: GgufMetadataTokenizerTokenType[];
     token_type_count?: number;
     scores?: readonly number[];
     merges?: readonly string[];
     bos_token_id?: number;
     eos_token_id?: number;
     eot_token_id?: number;
     eom_token_id?: number;
     unknown_token_id?: number;
     seperator_token_id?: number;
     padding_token_id?: number;
     cls_token_id?: number;
     mask_token_id?: number;
     add_bos_token?: boolean;
     add_eos_token?: boolean;
     add_space_prefix?: boolean;
     added_tokens?: readonly string[];
     fim_pre_token_id?: number;
     fim_suf_token_id?: number;
     fim_mid_token_id?: number;
     fim_pad_token_id?: number;
     fim_rep_token_id?: number;
     fim_sep_token_id?: number;
     prefix_token_id?: number;
     suffix_token_id?: number;
     middle_token_id?: number;
  };
  huggingface?: {
     json?: string;
  };
  chat_template?: string;
  chat_template.rerank?: string;
};
```

Defined in: [gguf/types/GgufMetadataTypes.ts:294](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L294)

## Properties

### ggml

```ts
readonly ggml: {
  model:   | "no_vocab"
     | "none"
     | "llama"
     | "gpt2"
     | "bert"
     | "rwkv"
     | "t5"
     | "plamo2"
     | string;
  pre?:   | "default"
     | "llama3"
     | "llama-v3"
     | "llama-bpe"
     | "deepseek-llm"
     | "deepseek-coder"
     | "falcon"
     | "falcon3"
     | "pixtral"
     | "mpt"
     | "starcoder"
     | "gpt-2"
     | "phi-2"
     | "jina-es"
     | "jina-de"
     | "jina-v1-en"
     | "jina-v2-es"
     | "jina-v2-de"
     | "jina-v2-code"
     | "refact"
     | "command-r"
     | "qwen2"
     | "stablelm2"
     | "olmo"
     | "dbrx"
     | "smaug-bpe"
     | "poro-chat"
     | "chatglm-bpe"
     | "viking"
     | "jais"
     | "tekken"
     | "smollm"
     | "codeshell"
     | "bloom"
     | "gpt3-finnish"
     | "exaone"
     | "exaone4"
     | "chameleon"
     | "minerva-7b"
     | "megrez"
     | "gpt-4o"
     | "superbpe"
     | "trillion"
     | "bailingmoe"
     | "a.x-4.0"
     | "mellum"
     | string;
  tokens: readonly string[];
  token_type: GgufMetadataTokenizerTokenType[];
  token_type_count?: number;
  scores?: readonly number[];
  merges?: readonly string[];
  bos_token_id?: number;
  eos_token_id?: number;
  eot_token_id?: number;
  eom_token_id?: number;
  unknown_token_id?: number;
  seperator_token_id?: number;
  padding_token_id?: number;
  cls_token_id?: number;
  mask_token_id?: number;
  add_bos_token?: boolean;
  add_eos_token?: boolean;
  add_space_prefix?: boolean;
  added_tokens?: readonly string[];
  fim_pre_token_id?: number;
  fim_suf_token_id?: number;
  fim_mid_token_id?: number;
  fim_pad_token_id?: number;
  fim_rep_token_id?: number;
  fim_sep_token_id?: number;
  prefix_token_id?: number;
  suffix_token_id?: number;
  middle_token_id?: number;
};
```

Defined in: [gguf/types/GgufMetadataTypes.ts:295](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L295)

#### model

```ts
readonly model: 
  | "no_vocab"
  | "none"
  | "llama"
  | "gpt2"
  | "bert"
  | "rwkv"
  | "t5"
  | "plamo2"
  | string;
```

#### pre?

```ts
readonly optional pre: 
  | "default"
  | "llama3"
  | "llama-v3"
  | "llama-bpe"
  | "deepseek-llm"
  | "deepseek-coder"
  | "falcon"
  | "falcon3"
  | "pixtral"
  | "mpt"
  | "starcoder"
  | "gpt-2"
  | "phi-2"
  | "jina-es"
  | "jina-de"
  | "jina-v1-en"
  | "jina-v2-es"
  | "jina-v2-de"
  | "jina-v2-code"
  | "refact"
  | "command-r"
  | "qwen2"
  | "stablelm2"
  | "olmo"
  | "dbrx"
  | "smaug-bpe"
  | "poro-chat"
  | "chatglm-bpe"
  | "viking"
  | "jais"
  | "tekken"
  | "smollm"
  | "codeshell"
  | "bloom"
  | "gpt3-finnish"
  | "exaone"
  | "exaone4"
  | "chameleon"
  | "minerva-7b"
  | "megrez"
  | "gpt-4o"
  | "superbpe"
  | "trillion"
  | "bailingmoe"
  | "a.x-4.0"
  | "mellum"
  | string;
```

#### tokens

```ts
readonly tokens: readonly string[];
```

#### token\_type

```ts
readonly token_type: GgufMetadataTokenizerTokenType[];
```

#### token\_type\_count?

```ts
readonly optional token_type_count: number;
```

#### scores?

```ts
readonly optional scores: readonly number[];
```

#### merges?

```ts
readonly optional merges: readonly string[];
```

#### bos\_token\_id?

```ts
readonly optional bos_token_id: number;
```

#### eos\_token\_id?

```ts
readonly optional eos_token_id: number;
```

#### eot\_token\_id?

```ts
readonly optional eot_token_id: number;
```

#### eom\_token\_id?

```ts
readonly optional eom_token_id: number;
```

#### unknown\_token\_id?

```ts
readonly optional unknown_token_id: number;
```

#### seperator\_token\_id?

```ts
readonly optional seperator_token_id: number;
```

#### padding\_token\_id?

```ts
readonly optional padding_token_id: number;
```

#### cls\_token\_id?

```ts
readonly optional cls_token_id: number;
```

#### mask\_token\_id?

```ts
readonly optional mask_token_id: number;
```

#### add\_bos\_token?

```ts
readonly optional add_bos_token: boolean;
```

#### add\_eos\_token?

```ts
readonly optional add_eos_token: boolean;
```

#### add\_space\_prefix?

```ts
readonly optional add_space_prefix: boolean;
```

#### added\_tokens?

```ts
readonly optional added_tokens: readonly string[];
```

#### fim\_pre\_token\_id?

```ts
readonly optional fim_pre_token_id: number;
```

#### fim\_suf\_token\_id?

```ts
readonly optional fim_suf_token_id: number;
```

#### fim\_mid\_token\_id?

```ts
readonly optional fim_mid_token_id: number;
```

#### fim\_pad\_token\_id?

```ts
readonly optional fim_pad_token_id: number;
```

#### fim\_rep\_token\_id?

```ts
readonly optional fim_rep_token_id: number;
```

#### fim\_sep\_token\_id?

```ts
readonly optional fim_sep_token_id: number;
```

#### ~~prefix\_token\_id?~~

```ts
readonly optional prefix_token_id: number;
```

##### Deprecated

#### ~~suffix\_token\_id?~~

```ts
readonly optional suffix_token_id: number;
```

##### Deprecated

#### ~~middle\_token\_id?~~

```ts
readonly optional middle_token_id: number;
```

##### Deprecated

***

### huggingface?

```ts
readonly optional huggingface: {
  json?: string;
};
```

Defined in: [gguf/types/GgufMetadataTypes.ts:334](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L334)

#### json?

```ts
readonly optional json: string;
```

***

### chat\_template?

```ts
readonly optional chat_template: string;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:337](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L337)

***

### chat\_template.rerank?

```ts
readonly optional chat_template.rerank: string;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:338](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L338)

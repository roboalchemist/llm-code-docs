# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/LlamaGrammarOptions.md

---
url: /api/type-aliases/LlamaGrammarOptions.md
---
# Type Alias: LlamaGrammarOptions

```ts
type LlamaGrammarOptions = {
  grammar: string;
  stopGenerationTriggers?: readonly (LlamaText | string | readonly (string | Token)[])[];
  trimWhitespaceSuffix?: boolean;
  rootRuleName?: string;
};
```

Defined in: [evaluator/LlamaGrammar.ts:10](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaGrammar.ts#L10)

## Properties

### grammar

```ts
grammar: string;
```

Defined in: [evaluator/LlamaGrammar.ts:12](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaGrammar.ts#L12)

GBNF grammar

***

### stopGenerationTriggers?

```ts
optional stopGenerationTriggers: readonly (LlamaText | string | readonly (string | Token)[])[];
```

Defined in: [evaluator/LlamaGrammar.ts:15](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaGrammar.ts#L15)

Consider any of these as EOS for the generated text. Only supported by `LlamaChat` and `LlamaChatSession`

***

### trimWhitespaceSuffix?

```ts
optional trimWhitespaceSuffix: boolean;
```

Defined in: [evaluator/LlamaGrammar.ts:18](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaGrammar.ts#L18)

Trim whitespace from the end of the generated text. Only supported by `LlamaChat` and `LlamaChatSession`

***

### rootRuleName?

```ts
optional rootRuleName: string;
```

Defined in: [evaluator/LlamaGrammar.ts:25](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaGrammar.ts#L25)

Root rule name.

Defaults to `"root"`.

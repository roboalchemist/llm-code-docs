# Managing Large Promptfoo Configurations

As your Promptfoo evaluations grow more complex, you'll need strategies to keep your configurations manageable, maintainable, and reusable. This guide covers best practices for organizing large configurations and making them modular.

## Separate Configuration Files

Split your configuration into multiple files based on functionality:

```yaml
promptfooconfig.yaml
```

```yaml
# yaml-language-server: $schema=https://promptfoo.dev/config-schema.json
description: Main evaluation configuration
prompts: file://configs/prompts.yaml
providers: file://configs/providers.yaml
tests: file://configs/tests/
defaultTest: file://configs/default-test.yaml
```

```yaml
configs/prompts.yaml
```

```yaml
# Prompts configuration
- file://prompts/system-message.txt
- file://prompts/user-prompt.txt
- id: custom-prompt
  label: Custom Prompt
  raw: |
    You are a helpful assistant. Please answer the following question:
    {{question}}
```

```yaml
configs/providers.yaml
```

```yaml
# Providers configuration
- id: gpt-5.2
  provider: openai:gpt-5.2
  config:
    temperature: 0.7
    max_tokens: 1000
- id: claude-sonnet-4-5-20250929
  provider: anthropic:claude-sonnet-4-5-20250929
  config:
    temperature: 0.7
    max_tokens: 1000
    requestsPerMinute: 100
```

```yaml
configs/env-prod.yaml
```

```yaml
# Production environment variables
OPENAI_API_KEY: {{ env.OPENAI_API_KEY_PROD }}
ANTHROPIC_API_KEY: {{ env.ANTHROPIC_API_KEY_PROD }}
LOG_LEVEL: info
```

## YAML References and Templates

Use YAML references to avoid repetition:

```yaml
promptfooconfig.yaml
```

```yaml
# yaml-language-server: $schema=https://promptfoo.dev/config-schema.json
description: Evaluation with reusable components
prompts: file://prompts/
providers: file://configs/providers-prod.yaml
tests: file://tests/
env: file://configs/env-prod.yaml
```

```javascript
promptfooconfig.js
```

```javascript
const baseConfig = {
  description: 'Dynamic configuration example',
  prompts: ['file://prompts/base-prompt.txt'],
  providers: ['openai:gpt-5.2', 'anthropic:claude-sonnet-4-5-20250929'],
}
```

```javascript
module.exports = baseConfig;
```

```typescript
promptfooconfig.ts
```

```typescript
import type { UnifiedConfig } from 'promptfoo';
const config: UnifiedConfig = {
  description: 'My evaluation suite',
  prompts: ['Tell me about {{topic}} in {{style}}'],
  providers: ['openai:gpt-5.2', 'anthropic:claude-sonnet-4-5-20250929'],
  tests: [
    {
      vars: {
        category: '{{topic}}',
        difficulty: '{{difficulty}}',
        question: `Generate a {{difficulty}} question about {{category}}`,
      },
      assert: [
        { type: 'contains', value: '{{category}}' },
        { type: 'javascript', value: `const wordCount = output.split(' ').length; const minWords = {{difficulty }}; const maxWords = {{difficulty }}; return wordCount >= minWords && wordCount <= maxWords;` },
      ],
    },
  ],
};
export default config;
```

## Dynamic Configuration with JavaScript

Use JavaScript configurations for complex logic:

```javascript
promptfooconfig.js
```

```javascript
import type { UnifiedConfig } from 'promptfoo';
const config: UnifiedConfig = {
  description: 'Dynamic configuration example',
  prompts: ['Tell me about {{topic}} in {{style}}'],
  providers: ['openai:gpt-5.2', 'anthropic:claude-sonnet-4-5-20250929'],
  tests: [
    {
      vars: {
        topic: 'quantum computing',
        style: 'simple terms',
      },
      assert: [
        { type: 'contains', value: 'quantum' },
      ],
    },
  ],
};
export default config;
```

## TypeScript Configuration

Promptfoo configs can be written in TypeScript:

```typescript
promptfooconfig.ts
```

```typescript
import type { UnifiedConfig } from 'promptfoo';
const config: UnifiedConfig = {
  description: 'My evaluation suite',
  prompts: ['Tell me about {{topic}} in {{style}}'],
  providers: ['openai:gpt-5.2', 'anthropic:claude-sonnet-4-5-20250929'],
  tests: [
    {
      vars: {
        topic: 'quantum computing',
        style: 'simple terms',
      },
      assert: [
        { type: 'contains', value: 'quantum' },
      ],
    },
  ],
};
export default config;
```

### Running TypeScript Configs

Install a TypeScript loader:

```bash
npm install tsx
```

Run with `NODE_OPTIONS`:

```bash
NODE_OPTIONS="--import tsx" promptfoo eval -c promptfooconfig.ts
```

### Dynamic Schema Generation

Share Zod schemas between your application and promptfoo:

```typescript
src/schemas/response.ts
```

```typescript
import { z } from 'zod';
export const ResponseSchema = z.object({
  answer: z.string(),
  confidence: z.number().min(0).max(1),
  sources: z.array(z.string()).nullable(),
});
```

```typescript
promptfooconfig.ts
```

```typescript
import { zodResponseFormat } from 'openai/helpers/zod.mjs';
import type { UnifiedConfig } from 'promptfoo';
import { ResponseSchema } from './src/schemas/response';
const responseFormat = zodResponseFormat(ResponseSchema, 'response');
const config: UnifiedConfig = {
  prompts: ['Answer this question: {{question}}'],
  providers: [
    {
      id: 'openai:gpt-5.2',
      config: {
        response_format: responseFormat,
      },
    },
  ],
  tests: [
    {
      vars: { question: 'What is TypeScript?' },
      assert: [{ type: 'is-json' }],
    },
  ],
};
export default config;
```

## Conditional Configuration Loading

Create configurations that adapt based on environment:

```javascript
promptfooconfig.js
```

```javascript
const isQuickTest = process.env.TEST_MODE === 'quick';
const isComprehensive = process.env.TEST_MODE === 'comprehensive';
const baseConfig = {
  description: 'Test mode adaptive configuration',
  prompts: ['file://prompts/'],
};
// Quick test configuration
if (isQuickTest) {
  module.exports = {
    ...baseConfig,
    providers: [
      'openai:gpt-5.1-mini', // Faster, cheaper for quick testing
    ],
    tests: 'file://tests/quick/', // Smaller test suite
    env: {
      LOG_LEVEL: 'debug',
    },
  };
}
// Comprehensive test configuration
if (isComprehensive) {
  module.exports = {
    ...baseConfig,
    providers: [
      'openai:gpt-5.2',
      'anthropic:claude-sonnet-4-5-20250929',
      'google:gemini-2.5-flash',
    ],
    tests: 'file://tests/comprehensive/', // Full test suite
    env: {
      LOG_LEVEL: 'info',
    },
    writeLatestResults: true,
  };
}
```

## Directory Structure

Organize your configuration files in a logical hierarchy:

```text
project/
├── promptfooconfig.yaml              # Main configuration
├── configs/
│   ├── providers/
│   │   ├── development.yaml
│   │   ├── staging.yaml
│   │   └── production.yaml
│   ├── prompts/
│   │   ├── system-prompts.yaml
│   │   ├── user-prompts.yaml
│   │   └── templates.yaml
│   └── defaults/
│       ├── assertions.yaml
│       └── test-config.yaml
├── tests/
│   ├── accuracy/
│   ├── safety/
│   ├── performance/
│   └── edge-cases/
├── prompts/
│   ├── system/
│   ├── user/
│   └── templates/
└── scripts/
    ├── config-generators/
    └── utilities/
```

## See Also

- [Configuration Guide](/docs/configuration/guide/) - Basic configuration concepts
- [Configuration Reference](/docs/configuration/reference/) - Complete configuration options
- [Test Cases](/docs/configuration/test-cases/) - Organizing test cases
- [Prompts](/docs/configuration/prompts/) - Managing prompts and templates
- [Providers](/docs/providers/) - Configuring LLM providers
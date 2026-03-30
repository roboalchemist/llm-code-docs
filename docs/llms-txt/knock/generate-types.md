# Source: https://docs.knock.app/cli/workflow/generate-types.md

# Generate types

Generate type definitions for workflow trigger data from your workflow schemas. This command fetches workflows with trigger data schemas and generates type-safe definitions for TypeScript, Python, Ruby, and Go.

The generated types enable compile-time safety when triggering workflows in your application code, helping catch integration errors before runtime. The target language is inferred from the output file extension.

Learn more about [type safety with workflows](/developer-tools/type-safety).

### Flags

- **--environment** (string): The environment to fetch workflows from. Defaults to development.
- **--output-file** (string): Specifies the file to generate types into. The language is inferred from the file suffix.

```bash title="Generate TypeScript types"
knock workflow generate-types \
  --output-file=./types/knock-workflows.ts
```

```bash title="Generate Python types"
knock workflow generate-types \
  --output-file=./types/knock_workflows.py
```

```bash title="Generate Ruby types"
knock workflow generate-types \
  --output-file=./types/knock_workflows.rb
```

```bash title="Generate Go types"
knock workflow generate-types \
  --output-file=./types/knock_workflows.go
```

```bash title="Generate from production environment"
knock workflow generate-types \
  --environment=production \
  --output-file=./types/knock-workflows.ts
```

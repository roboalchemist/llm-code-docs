# Source: https://docs.bito.ai/help/support-and-questions/troubleshooting.md

# Source: https://docs.bito.ai/ai-code-reviews-in-cli/troubleshooting.md

# Troubleshooting

#### Enable debug output

```shellscript
bitoreview review --debug
# or
bitoreview review -d
```

#### Enable verbose logging

```shellscript
bitoreview review --verbose
# or
bitoreview review -v
```

#### Common issues

**Issue: "API key not found"**

```shellscript
# Set your API key
bitoreview config set-api-key YOUR_KEY

# Verify it's set
bitoreview config show-api-key
```

**Issue: "Wingman binary not found"**

Re-run the CLI installer to reinstall wingman:

* **macOS/Linux (Terminal):**

```shellscript
curl -fsSL https://bitoreview.bito.ai/install.sh | bash
```

* **Windows (PowerShell):**

```shellscript
irm https://bitoreview.bito.ai/install.ps1 | iex
```

**Issue: Slow reviews on large codebases**

* Use `--mode essential` for faster feedback
* Focus on specific files: `bitoreview review src/changed-file.js`
* Use `--type uncommitted` to limit scope

**Issue: Too many low-priority issues**

```shellscript
# Filter to high severity only
bitoreview review --severity high

# Or use essential mode
bitoreview review --mode essential
```

#### Performance expectations

|    Codebase size    | Approximate time |
| :-----------------: | :--------------: |
|   Small (<5 files)  |   30-60 seconds  |
| Medium (5-20 files) |    1-3 minutes   |
|  Large (20+ files)  |    3-8 minutes   |

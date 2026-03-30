# Source: https://docs.tabnine.com/main/getting-started/tabnine-cli/examples/code-review.md

# Code Review

Learn how to use Tabnine CLI for effective code review.

### Basic Code Review

#### Review a Single File

```bash
tabnine
```

Then:

```
> Review @src/auth/login.ts and suggest improvements
```

{% stepper %}
{% step %}
**What Tabnine CLI does**

* Reads the file
* Analyzes code structure
* Checks for issues
* Suggests improvements
* Provides specific recommendations
  {% endstep %}

{% step %}
**Example Output**

```
AI: I've reviewed @src/auth/login.ts. Here are my findings:

✓ Good Practices:
- Proper async/await usage
- Input validation present

⚠️  Suggestions:

1. Security: Line 45
   Add password strength validation
   
2. Error Handling: Line 67
   Use custom error types
   
3. Code Quality: Line 89
   Extract magic number to constant

Would you like me to make these changes?
```

{% endstep %}
{% endstepper %}

#### Review Multiple Files

```
> Review all TypeScript files in @src/auth/ and check for:
> - Security vulnerabilities
> - Error handling
> - Missing documentation
```

#### Review Recent Changes

```
> Review the changes I made to @src/api/users.ts
```

### Using Remote Code Search

Find related code for better context:

```
> Using Remote Code Search, find similar authentication code and review @src/auth.ts for consistency
```

### Using Coaching Guidelines

Get best practices applied:

```
> Review @src/api/users.ts according to security best practices and coding guidelines
```

### Security Audit

```
> Perform security audit on @src/:
> - SQL injection
> - XSS vulnerabilities
> - Authentication issues
> - Hardcoded secrets
```

**Example Output**:

```
AI: 🔒 Security Audit Results:

⚠️  HIGH: SQL Injection (Line 78)
query = `SELECT * FROM users WHERE id = ${userId}`;

Risk: Direct user input in SQL
Fix: Use parameterized queries:
const query = 'SELECT * FROM users WHERE id = ?';
const results = await db.query(query, [userId]);

⚠️  MEDIUM: Missing Input Validation (Line 45)
Fix: Add validation before processing
```

### Performance Review

```
> Analyze @src/api/users.ts for performance issues:
> - N+1 queries
> - Inefficient loops
> - Missing caching
```

### Automation Examples

#### Pre-Commit Review

Create `review.sh`:

```bash
#!/bin/bash

# Get staged files
STAGED_FILES=$(git diff --cached --name-only --diff-filter=ACM | grep '\.ts$\|\.js$')

if [ -z "$STAGED_FILES" ]; then
  exit 0
fi

# Review
echo "Reviewing staged files..."
tabnine -p "Review these files for issues: $STAGED_FILES" --output-format json > review.json

# Check results
if grep -q "critical\|security" review.json; then
  echo "⚠️  Issues found. Review before committing."
  exit 1
fi

echo "✓ Review complete"
```

#### CI/CD Integration

**GitHub Actions**:

```yaml
- name: Code Review
  env:
    TABNINE_REFRESH_TOKEN: ${{ secrets.TABNINE_TOKEN }}
  run: |
    DIFF=$(git diff main...HEAD)
    tabnine -p "Review this PR: $DIFF" --output-format json > review.json
```

### Best Practices

{% stepper %}
{% step %}
**Be Specific**

❌ "Review my code"\
✅ "Review @src/auth.ts for security vulnerabilities and error handling"
{% endstep %}

{% step %}
**Provide Context**

```
> Review @src/payment/processor.ts

Context:
- Handles credit card payments
- Must be PCI compliant
- Processes ~1000 transactions/hour

Focus on security and reliability.
```

{% endstep %}

{% step %}
**Use Multiple Tools**

```
> Using Remote Code Search and Coaching Guidelines, review @src/api/ for best practices
```

{% endstep %}

{% step %}
**Ask Follow-ups**

```
> Review @src/auth.ts
> Can you explain the security issue in more detail?
> How would I fix it?
> Show me an example
```

{% endstep %}
{% endstepper %}

### Common Review Patterns

#### Before Merging

```
> Pre-merge checklist for @src/features/new-feature/:
> - All functions have tests
> - No debug code
> - Error handling complete
> - Documentation updated
> - Follows project conventions
```

#### After Refactoring

```
> Post-refactoring review of @src/services/user.ts:
> - Functionality preserved
> - No new bugs
> - More maintainable
> - Performance not degraded
```

#### For New Code

```
> Review @src/api/products.ts:
> - Code quality
> - Best practices
> - Security
> - Performance
> - Test coverage
```

### Next Steps

* [**Remote Code Search**](https://docs.tabnine.com/main/getting-started/context-engine) - Search large codebases
* [**Coaching Guidelines**](https://docs.tabnine.com/main/getting-started/context-engine/admin-console/coaching-guidelines-v) - Get best practices
* [**Quick Start**](https://docs.tabnine.com/main/getting-started/tabnine-cli/getting-started/quickstart) - Learn more

### Getting Help

* [**FAQ**](https://docs.tabnine.com/main/getting-started/tabnine-cli/troubleshooting/faq) - Common questions
* [**Troubleshooting**](https://docs.tabnine.com/main/getting-started/tabnine-cli/troubleshooting/common-issues) - Solve problems
* **In-App**: Type `/help` or `/bug`

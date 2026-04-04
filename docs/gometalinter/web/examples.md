# gometalinter Practical Examples and Use Cases

## Source: https://github.com/alecthomas/gometalinter

## Project Setup Examples

### New Project Setup

Initialize gometalinter for a new Go project:

```bash
# 1. Install gometalinter
brew install gometalinter

# 2. Download and install all linters
gometalinter --install

# 3. Create initial config
gometalinter --write-config=.gometalinter.json ./...

# 4. Run initial lint
gometalinter ./...

# 5. Address issues or suppress false positives
# Edit code to fix real issues
# Use // nolint for false positives
```

### Existing Project Integration

Add gometalinter to an established project:

```bash
# 1. Install with moderate settings
cat > .gometalinter.json << 'EOF'
{
  "enable": ["vet", "golint", "errcheck"],
  "skip-dirs": ["vendor", "build"],
  "deadline": "1m"
}
EOF

# 2. Run and capture baseline
gometalinter ./... 2>&1 | tee lint-baseline.txt

# 3. Gradually enable more linters as team addresses issues
# Uncomment additional linters weekly
```

## Development Workflow Examples

### Daily Development Check

Quick lint check during development:

```bash
# Fast check - only vet and golint
gometalinter --deadline=10s --enable=vet --enable=golint ./...
```

Save as a shell alias:

```bash
# Add to ~/.bashrc or ~/.zshrc
alias gmt-fast="gometalinter --deadline=10s --enable=vet --enable=golint"

# Usage
gmt-fast ./...
```

### Pre-commit Hook

Prevent commits with linting issues:

```bash
#!/bin/bash
# .git/hooks/pre-commit

# Get modified Go files
MODIFIED_GO_FILES=$(git diff --cached --name-only | grep '\.go$')

if [ -z "$MODIFIED_GO_FILES" ]; then
    exit 0
fi

# Run gometalinter on modified files
echo "Running gometalinter on modified files..."

for file in $MODIFIED_GO_FILES; do
    if ! gometalinter --deadline=5s "$file" 2>&1; then
        echo "Linting errors in $file. Commit aborted."
        exit 1
    fi
done

exit 0
```

### Feature Branch Validation

Lint changes in a feature branch:

```bash
#!/bin/bash
# Check only files changed in this branch

BASE_BRANCH="main"
CHANGED_FILES=$(git diff $BASE_BRANCH...HEAD --name-only | grep '\.go$')

echo "Linting changed files in branch..."
gometalinter --deadline=30s $(dirname $(echo $CHANGED_FILES | tr '\n' ' ' | awk '{print}'))
```

## CI/CD Integration Examples

### GitHub Actions Workflow

```yaml
# .github/workflows/lint.yml
name: Lint

on: [push, pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Go
        uses: actions/setup-go@v4
        with:
          go-version: '1.21'

      - name: Install gometalinter
        run: |
          go install gopkg.in/alecthomas/gometalinter.v1@latest
          gometalinter --install

      - name: Run gometalinter
        run: gometalinter --deadline=5m ./...

      - name: Checkstyle Report
        if: always()
        run: |
          gometalinter --checkstyle ./... > checkstyle-report.xml || true

      - name: Publish Checkstyle Report
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: checkstyle-report
          path: checkstyle-report.xml
```

### GitLab CI Configuration

```yaml
# .gitlab-ci.yml
stages:
  - lint

lint:
  stage: lint
  image: golang:1.21
  script:
    - go install gopkg.in/alecthomas/gometalinter.v1@latest
    - gometalinter --install
    - gometalinter --deadline=5m --checkstyle ./... > checkstyle.xml
  artifacts:
    reports:
      junit: checkstyle.xml
    paths:
      - checkstyle.xml
  allow_failure: false
```

### Jenkins Pipeline

```groovy
// Jenkinsfile
pipeline {
    agent any

    stages {
        stage('Lint') {
            steps {
                script {
                    sh '''
                        go install gopkg.in/alecthomas/gometalinter.v1@latest
                        gometalinter --install
                        gometalinter --deadline=5m --checkstyle ./... > checkstyle-report.xml || true
                    '''
                }
            }
        }

        stage('Report') {
            steps {
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '.',
                    reportFiles: 'checkstyle-report.xml',
                    reportName: 'Checkstyle Report'
                ])
            }
        }
    }

    post {
        always {
            step([$class: 'CheckStylePublisher',
                  pattern: 'checkstyle-report.xml'])
        }
    }
}
```

### Makefile Integration

```makefile
# Makefile
.PHONY: lint lint-install lint-check

# Install gometalinter
lint-install:
	go install gopkg.in/alecthomas/gometalinter.v1@latest
	gometalinter --install

# Quick lint check
lint-check:
	gometalinter --deadline=10s --enable=vet --enable=golint ./...

# Full lint with report
lint: lint-install
	gometalinter --deadline=5m --checkstyle ./... > lint-report.xml || true
	@echo "Lint report generated: lint-report.xml"

# Run all checks
check: lint lint-check test
	@echo "All checks passed!"
```

## Suppressing False Positives

### Using // nolint Comment Directive

Suppress all linters for a line:

```go
package main

import "fmt"

func main() {
    // nolint
    var unused string

    // nolint
    result := someExpensiveOperation()
    fmt.Println(result)
}
```

Suppress specific linter:

```go
// Only suppress misspell linter
// nolint: misspell
const commond = "misspell" // Intentional

// Suppress multiple specific linters
// nolint: errcheck,misspell
err = someFunction() // Suppress errcheck
```

Suppress warnings on function:

```go
// nolint
func DisabledLinterCheck() {
    var unusedVar string
    return
}
```

Suppress in struct tags:

```go
type Config struct {
    // nolint
    OldField string `deprecated:"Use NewField"`
}
```

### Suppress Entire Files

Create `.nolintignore` file:

```
# Ignore linting in generated files
**/*_pb.go
**/*_mock.go
**/*_gen.go
```

### Suppress Directory

Use configuration file:

```json
{
  "skip-dirs": ["vendor", "build"],
  "skip-files": [".*_test\\.go$", ".*_mock\\.go$"]
}
```

## Custom Linter Examples

### Adding a Custom Style Checker

```bash
# Create custom linter script
cat > /usr/local/bin/my-style-checker << 'EOF'
#!/bin/bash
grep -n "fmt.Print" "$1" | sed "s/:/ $(basename $1):/; s/$/: Use logging instead of fmt.Print/"
EOF

chmod +x /usr/local/bin/my-style-checker

# Configure in gometalinter
gometalinter \
  --linter="mystyle:my-style-checker {file}:^.*?:(?P<line>\\d+): (?P<message>.*)$" \
  ./...
```

### Integrating with Project-Specific Linters

```json
{
  "linters": {
    "custom-auth": {
      "command": "go run ./tools/lint-auth.go",
      "pattern": "^(?P<path>.*?\\.go):(?P<line>\\d+): (?P<message>.*)"
    },
    "custom-sql": {
      "command": "go run ./tools/lint-sql.go",
      "pattern": "^(?P<path>.*?\\.go):(?P<line>\\d+): (?P<message>.*)"
    }
  },
  "enable": [
    "vet",
    "golint",
    "custom-auth",
    "custom-sql"
  ]
}
```

## Gradual Adoption Strategy

### Phase 1: Start Minimal

Week 1 configuration:

```json
{
  "enable": ["vet"],
  "skip-dirs": ["vendor"],
  "deadline": "30s",
  "severity": "error"
}
```

### Phase 2: Add Common Linters

Week 2-3 configuration:

```json
{
  "enable": [
    "vet",
    "golint",
    "errcheck"
  ],
  "skip-dirs": ["vendor"],
  "deadline": "1m"
}
```

### Phase 3: Add Security and Performance

Week 4-6 configuration:

```json
{
  "enable": [
    "vet",
    "golint",
    "errcheck",
    "staticcheck",
    "gosec",
    "misspell"
  ],
  "skip-dirs": ["vendor", "build"],
  "deadline": "2m"
}
```

### Phase 4: Full Coverage

Final configuration:

```json
{
  "enable": [
    "vet",
    "golint",
    "errcheck",
    "staticcheck",
    "gosec",
    "misspell",
    "unconvert",
    "gocyclo",
    "deadcode"
  ],
  "disable": ["lll"],
  "skip-dirs": ["vendor", "build", "dist"],
  "deadline": "5m"
}
```

## Team Integration Examples

### Code Review Integration

In pull request comments, run gometalinter on changed code:

```bash
#!/bin/bash
# comment-pr-lint.sh

PR_FILES=$(gh pr diff $1 --name-only | grep '\.go$')

if [ -z "$PR_FILES" ]; then
    echo "No Go files changed"
    exit 0
fi

LINT_ISSUES=$(gometalinter --deadline=2m $PR_FILES 2>&1)

if [ -z "$LINT_ISSUES" ]; then
    gh pr comment $1 -b "✅ No linting issues found"
else
    gh pr comment $1 -b "⚠️ Linting issues found:\n\`\`\`\n$LINT_ISSUES\n\`\`\`"
fi
```

### Team Standards Documentation

Create `LINTING.md` for your team:

```markdown
# Linting Standards

## Running Linters

```bash
# Daily development
make lint-check

# Before committing
make lint

# In CI/CD
gometalinter --deadline=5m ./...
```

## Suppressing False Positives

Only use `// nolint` for legitimate false positives.
Always explain why in a comment:

```go
// nolint: errcheck
// We intentionally ignore Close() errors for stdout
fmt.Println(result)
```

## Enabled Linters

- **vet**: Official Go static analyzer
- **golint**: Style issues
- **errcheck**: Unchecked errors
- **staticcheck**: Advanced static analysis
- **gosec**: Security issues
- **misspell**: Spelling errors

Contact the team before suppressing warnings.
```

## Monitoring and Reporting

### Generate Weekly Report

```bash
#!/bin/bash
# weekly-lint-report.sh

TIMESTAMP=$(date +%Y-%m-%d)
REPORT_FILE="lint-reports/${TIMESTAMP}-lint-report.txt"

mkdir -p lint-reports

gometalinter \
  --deadline=10m \
  --json ./... > "lint-reports/${TIMESTAMP}-lint.json" || true

# Generate summary
echo "=== Lint Report for $TIMESTAMP ===" > "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "Total Issues: $(cat "lint-reports/${TIMESTAMP}-lint.json" | jq length)" >> "$REPORT_FILE"
echo "By Linter:" >> "$REPORT_FILE"
cat "lint-reports/${TIMESTAMP}-lint.json" | jq -r '.[].Linter' | sort | uniq -c >> "$REPORT_FILE"

echo "Report saved to $REPORT_FILE"
```

### Track Lint Quality Over Time

```bash
#!/bin/bash
# track-lint-history.sh

for week in {1..12}; do
    DATE=$(date -d "$week weeks ago" +%Y-%m-%d)
    COUNT=$(cat "lint-reports/${DATE}-lint.json" 2>/dev/null | jq length || echo 0)
    echo "$DATE: $COUNT issues"
done | sort | tee lint-history.txt
```

## Troubleshooting Examples

### Linter Not Found

Problem: `"go vet not found"`

Solution:

```bash
# Check if linter is installed
which go
which golint

# Install missing linter
go install honnef.co/go/tools/cmd/staticcheck@latest

# Update PATH if needed
export PATH="$PATH:$(go env GOPATH)/bin"
```

### Timeout Issues

Problem: `"deadline exceeded"`

Solution:

```bash
# Increase deadline
gometalinter --deadline=5m ./...

# Or disable slow linters
gometalinter --disable=gocyclo --deadline=2m ./...
```

### False Positives in Generated Code

Problem: Linting errors in `_pb.go` files

Solution:

```json
{
  "skip-files": [
    ".*_pb\\.go$",
    ".*_gen\\.go$"
  ]
}
```

# CodeClimate Integration Guide

## GitHub Integration

### Setup
1. Navigate to https://app.edp.codeclimate.com
2. Connect your GitHub account
3. Select repositories to analyze
4. Configure quality gates
5. Enable PR checks

### Features
- Automatic PR analysis
- Inline code comments
- Status checks for blocking
- Coverage reports
- Quality metrics

### Configuration
```yaml
# .codeclimate.yml (in repository root)
version: "2"
checks:
  similar-code:
    enabled: true
    threshold: 80
  duplication:
    enabled: true
    threshold: 3
exclude-patterns:
  - ^tests/
  - ^vendor/
engines:
  eslint:
    enabled: true
  fixme:
    enabled: true
ratings:
  paths:
    - js/**
    - src/**
    - tests/**
```

## GitLab Integration

### Setup
1. Connect GitLab account
2. Select projects for analysis
3. Configure MR checks
4. Set quality gates
5. Enable CI/CD pipeline integration

### Features
- Pipeline status integration
- MR comments and analysis
- Coverage reporting
- Quality gates enforcement

## Bitbucket Integration

### Setup
1. Connect Bitbucket account
2. Select repositories
3. Configure pull request checks
4. Set quality thresholds
5. Enable merge checks

## CI/CD Platform Integration

### GitHub Actions
```yaml
name: CodeClimate

on: [push, pull_request]

jobs:
  test-coverage:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run tests with coverage
        run: npm test -- --coverage
      - name: Upload coverage to CodeClimate
        uses: paambaati/codeclimate-action@v3
        env:
          CC_TEST_REPORTER_ID: ${{ secrets.CC_TEST_REPORTER_ID }}
```

### GitLab CI
```yaml
test:
  image: node:latest
  script:
    - npm install
    - npm test -- --coverage
  coverage: '/Coverage: \d+\.\d+%/'
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml
```

### Other CI/CD Systems
- CircleCI Orb available
- Jenkins integration via API
- Generic webhook support
- Custom script integration

## API Usage

### Authentication
```bash
# API token in requests
curl -H "Authorization: Token token=YOUR_TOKEN"   https://api.codeclimate.com/v1/...
```

### Common Endpoints
- `/repos` - Repository list
- `/repos/{id}/issues` - Code issues
- `/repos/{id}/test-reports` - Test coverage
- `/repos/{id}/snapshots` - Quality snapshots
- `/analysis/pull-requests` - PR analysis

### Example: Get Repository Metrics
```bash
curl -H "Authorization: Token token=YOUR_API_TOKEN"   https://api.codeclimate.com/v1/repos/your-repo-id/latest-snapshot
```

## Slack Integration

### Setup
1. Connect Slack workspace
2. Select channel for notifications
3. Configure notification types
4. Set alert thresholds

### Notifications
- New issues detected
- Coverage changes
- Quality gate failures
- Performance trends
- Team metrics updates

## Webhooks

### Custom Integrations
Define custom webhooks for:
- Issue detection
- Coverage changes
- Quality gate events
- Snapshot creation
- PR analysis completion

### Webhook Payload
```json
{
  "event": "snapshot.created",
  "data": {
    "repository_id": "123",
    "branch": "main",
    "coverage": 85.5,
    "gpa": 3.8,
    "issues": [
      {"type": "duplication", "count": 5}
    ]
  }
}
```

## Marketplace Integrations

CodeClimate integrates with:
- Jira
- Azure DevOps
- Asana
- Monday.com
- Slack
- Discord
- And many more via zapier

## Configuration Files

### .codeclimate.yml

Located in repository root, configures:
- Active engines
- Exclusion patterns
- Severity levels
- Custom rules
- Pylint/ESLint overrides

### Example Configuration
```yaml
version: "2"

checks:
  argument-count:
    config:
      threshold: 4
  complex-logic:
    enabled: false

exclude-patterns:
  - ^tests/
  - ^vendor/
  - ^node_modules/
  - ^\.

engines:
  eslint:
    enabled: true
    channel: "eslint-3"
  fixme:
    enabled: true
  duplication:
    enabled: true

ratings:
  paths:
    - "**.js"
    - "**.jsx"
    - "**.tsx"
    - "**.py"
```

## Troubleshooting

### Common Issues

**Coverage not reporting**
- Ensure coverage report is in supported format (Cobertura, LCOV, etc.)
- Check CI/CD integration configuration
- Verify API token has correct permissions

**PR checks not blocking**
- Verify quality gate settings
- Check branch protection rules
- Ensure status check is required

**Missing issues**
- Verify engines are enabled
- Check exclude patterns
- Review rule configuration

### Support
- Documentation: https://docs.edp.codeclimate.com/
- Support email: support@codeclimate.com
- Status page: https://status.codeclimate.com

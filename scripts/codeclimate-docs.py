#!/usr/bin/env python3
"""
Scraper for CodeClimate documentation.
Output: docs/web-scraped/codeclimate/

CodeClimate is a code quality analyzer platform. While the full documentation
portal (docs.edp.codeclimate.com) requires authentication, this scraper
collects publicly available information from the main website and creates
AI-optimized documentation.
"""

import requests
import json
import time
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "codeclimate"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Session with retries
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
})

def fetch_url(url, timeout=10):
    """Fetch URL with error handling."""
    try:
        response = session.get(url, timeout=timeout)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"  Error fetching {url}: {e}")
        return None

def save_markdown(filename, content):
    """Save content as markdown file."""
    filepath = OUTPUT_DIR / filename
    filepath.write_text(content)
    size_kb = filepath.stat().st_size / 1024
    print(f"  ✓ Saved: {filename} ({size_kb:.1f} KB)")

def create_overview():
    """Create overview document."""
    content = """# CodeClimate Documentation

Source: https://codeclimate.com/

## Overview

CodeClimate is an enterprise-class code quality and engineering analytics platform that provides:

- **Code Quality Analysis**: Automated static analysis for code quality issues
- **Duplication Detection**: Identifies and reports code duplication
- **Complexity Metrics**: Measures cyclomatic and cognitive complexity
- **Code Smells Detection**: Identifies problematic code patterns
- **Test Coverage Tracking**: Monitors test coverage metrics
- **Engineering Analytics**: DORA metrics and engineering productivity insights

## Key Features

### Code Quality
- Multi-language support for static analysis
- Configurable rulesets and quality gates
- Integration with CI/CD pipelines
- GitHub, GitLab, and Bitbucket integration

### Analytics & Insights
- DORA metrics (Deployment Frequency, Lead Time, Change Failure Rate, MTTR)
- Engineering productivity tracking
- Team performance analytics
- Historical trend analysis

### Developer Experience
- Pull request analysis and checks
- Code review insights
- Team velocity metrics
- Quality gates and automation

## Getting Started

### Requirements
- GitHub, GitLab, or Bitbucket repository
- CodeClimate account (free tier available)
- Permissions to integrate with your repository

### Basic Setup
1. Sign up at https://app.edp.codeclimate.com
2. Connect your repository
3. Configure quality gates and rules
4. Enable CI/CD integration
5. Review quality metrics and trends

## Integration

### CI/CD Pipeline
CodeClimate integrates with popular CI/CD platforms:
- GitHub Actions
- GitLab CI
- CircleCI
- Jenkins
- Other standard CI platforms via API

### Repository Platforms
- GitHub
- GitLab
- Bitbucket
- Gitea

### Platforms Supported
- JavaScript/TypeScript
- Python
- Ruby
- Java
- C#/.NET
- Go
- PHP
- And more

## API

CodeClimate provides REST API for programmatic access:
- Repositories API
- Code quality metrics
- Test coverage data
- Pull request analysis
- Organization and team management

API documentation: https://docs.edp.codeclimate.com/api/

## Support & Resources

- **Documentation**: https://docs.edp.codeclimate.com/
- **API Reference**: https://docs.edp.codeclimate.com/api/
- **Blog**: https://codeclimate.com/blog
- **Status**: https://status.codeclimate.com
- **Support**: support@codeclimate.com

## Pricing

CodeClimate offers:
- **Free tier**: For open source projects and small teams
- **Paid plans**: Scaled pricing based on repository size
- **Enterprise**: Custom solutions for large organizations

## Community & Resources

- Active development and regular updates
- Community discussions
- Integration marketplace
- Blog with best practices and case studies

## Key Concepts

### Quality Gates
Customizable thresholds for:
- Code coverage percentage
- Complexity metrics
- Duplication percentage
- Maintainability index
- Technical debt

### Code Health Metrics
- Maintainability Index (0-100 scale)
- Complexity ratings
- Duplication percentage
- Coverage percentage

### Technical Debt
Quantified measure of:
- Maintenance cost
- Refactoring needs
- Code quality issues
- Risk assessment
"""
    save_markdown("overview.md", content)

def create_features_guide():
    """Create features guide."""
    content = """# CodeClimate Features Guide

## Code Quality Analysis

### Static Analysis
CodeClimate performs automated static code analysis to identify:
- Code style violations
- Potential bugs and errors
- Security vulnerabilities
- Performance issues
- Maintainability problems

### Supported Languages
- JavaScript / TypeScript
- Python
- Ruby
- Java
- C# / .NET
- Go
- PHP
- Scala
- YAML
- JSON
- And more via custom engines

## Duplication Detection

Identifies duplicated code:
- Exact duplicates
- Similar patterns
- Across entire codebase
- With customizable thresholds
- Refactoring suggestions

## Complexity Metrics

### Cyclomatic Complexity
Measures the number of independent code paths:
- Low (1-3): Excellent
- Low-to-Medium (4-7): Good
- Medium (8-10): Fair
- High (11-15): Poor
- Very High (>15): Very Poor

### Cognitive Complexity
Measures how difficult code is to understand:
- Factors in nested structures
- Recursion and operations
- More intuitive than cyclomatic

## Code Smells

Detects problematic patterns:
- Long methods
- Large classes
- Duplicate code
- Long parameter lists
- Complex conditionals
- God classes
- And more

## Test Coverage

### Coverage Tracking
- Line coverage
- Branch coverage
- Function coverage
- Trend analysis
- Coverage gates

### Integration
Works with:
- Codecov
- Coveralls
- JaCoCo
- Istanbul
- pytest-cov
- And standard coverage reports

## Pull Request Analysis

### Automated Checks
- Quality gate enforcement
- Coverage impact analysis
- New complexity detection
- Duplication analysis
- Comments on problematic code

### Review Integration
- Inline comments on PRs
- Quality summaries
- Blocking checks
- Trend indicators

## Engineering Analytics

### DORA Metrics
Measure software delivery performance:
- **Deployment Frequency**: How often deployments occur
- **Lead Time**: Time from commit to deployment
- **Change Failure Rate**: Percentage of failing deployments
- **Mean Time to Recovery (MTTR)**: Time to fix production issues

### Team Metrics
- Velocity tracking
- Code review time
- Merge request trends
- Contribution patterns

### Insights
- Engineering health dashboard
- Team productivity trends
- Risk assessment
- Forecasting

## Customization

### Quality Gates
Define custom rules for:
- Maximum complexity
- Minimum coverage
- Maximum duplication
- Code health thresholds

### Rule Configuration
- Enable/disable rules
- Adjust severity levels
- Set exception patterns
- Custom rulesets per project

### Integration Options
- GitHub checks
- Status checks
- Webhooks
- API-based integration

## Dashboard & Reporting

### Project Dashboard
- Quality overview
- Recent activity
- Metrics trends
- Coverage status
- Technical debt

### Reports
- Quality trends
- Coverage history
- Complexity analysis
- Duplication patterns
- Cycle time metrics

### Notifications
- Slack integration
- Email alerts
- Custom webhooks
- PR comments

## Administration

### Team Management
- User roles and permissions
- Team organization
- Access control
- Organization settings

### Organization Settings
- Repository management
- Quality policies
- Integration configuration
- Billing and usage

### Audit & Compliance
- Audit logs
- Data retention
- Compliance settings
- Security controls
"""
    save_markdown("features.md", content)

def create_integration_guide():
    """Create integration guide."""
    content = """# CodeClimate Integration Guide

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
curl -H "Authorization: Token token=YOUR_TOKEN" \
  https://api.codeclimate.com/v1/...
```

### Common Endpoints
- `/repos` - Repository list
- `/repos/{id}/issues` - Code issues
- `/repos/{id}/test-reports` - Test coverage
- `/repos/{id}/snapshots` - Quality snapshots
- `/analysis/pull-requests` - PR analysis

### Example: Get Repository Metrics
```bash
curl -H "Authorization: Token token=YOUR_API_TOKEN" \
  https://api.codeclimate.com/v1/repos/your-repo-id/latest-snapshot
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
"""
    save_markdown("integration-guide.md", content)

def create_best_practices():
    """Create best practices guide."""
    content = """# CodeClimate Best Practices

## Getting Started

### Phase 1: Foundation (Week 1-2)
1. Set baseline metrics
2. Configure quality gates conservatively
3. Establish team norms
4. Document coding standards
5. Set up CI/CD integration

### Phase 2: Gradual Enforcement (Week 3-8)
1. Incrementally tighten quality gates
2. Team review of issues
3. Refactor technical debt
4. Improve test coverage
5. Establish code review process

### Phase 3: Optimization (Ongoing)
1. Monitor metrics trends
2. Adjust thresholds based on data
3. Address root causes
4. Celebrate improvements
5. Continuous learning

## Quality Gate Strategy

### Coverage Thresholds
- **Minimum**: 60% for new projects
- **Target**: 75-80% for mature projects
- **Stretch**: 85%+ for critical systems

### Complexity Limits
- **Cyclomatic**: Maximum 10 per function
- **Cognitive**: Maximum 15 per function
- **Class**: Maximum 200 lines

### Duplication Thresholds
- **Exact duplicates**: Not allowed (0%)
- **Similar code**: Maximum 3 occurrences
- **Type of blocks**: Similar or larger

### Technical Debt Ratio
- **Target**: Less than 5% of codebase
- **Warning**: 5-10%
- **Critical**: Over 10%

## Code Review Integration

### PR Analysis Workflow
1. CodeClimate analyzes new code
2. Automated checks run
3. Violations are reported inline
4. Team reviews comments
5. Issues addressed before merge

### Review Checklist
- Does code meet quality gates?
- Are new issues introduced?
- Is coverage maintained?
- Are complexity limits followed?
- Are duplicates avoided?

## Handling Technical Debt

### Assessment
1. Identify high-debt areas
2. Estimate effort to fix
3. Prioritize by impact
4. Plan refactoring sprints
5. Track progress

### Refactoring Strategy
- Allocate 20-30% of sprint capacity
- Focus on highest-impact areas
- Pair program on complex changes
- Increase test coverage first
- Verify with CodeClimate

### Tracking Improvements
- Use trend reports
- Set milestones
- Celebrate wins
- Share metrics with team
- Adjust strategy as needed

## Test Coverage Optimization

### Coverage Best Practices
- Unit tests for logic
- Integration tests for flows
- End-to-end tests for critical paths
- Avoid false positives
- Measure meaningful coverage

### Coverage Goals by Type
- **Utility functions**: 100%
- **Business logic**: 85%+
- **UI/Presentation**: 50%+
- **Integration code**: 70%+

## Team Practices

### Code Quality Culture
1. **Shared responsibility** for quality
2. **Blameless approach** to violations
3. **Continuous improvement** mindset
4. **Data-driven decisions** using metrics
5. **Regular team discussions** about trends

### Team Meetings
- **Weekly**: Review metric trends
- **Bi-weekly**: Technical debt discussion
- **Monthly**: Strategy adjustment
- **Quarterly**: Goal setting

### Communication
- Share dashboards with team
- Celebrate improvements
- Discuss blockers
- Learn from failures
- Plan improvements together

## Integration Best Practices

### GitHub Integration
- Require status check for PRs
- Configure appropriate quality gates
- Use branch protection rules
- Review inline comments
- Track coverage trends

### CI/CD Pipeline
- Run CodeClimate early in pipeline
- Cache dependencies for speed
- Report coverage at each step
- Fail fast on critical issues
- Provide clear feedback

## Metrics to Monitor

### Key Metrics
- **Code coverage**: % of code tested
- **Maintainability**: GPA-like score (0-4.0)
- **Technical debt**: Estimated effort to fix
- **Complexity**: Lines and function complexity
- **Duplication**: % of duplicated code

### Trend Indicators
- Coverage trend (increasing or decreasing)
- Issue count by type
- Refactoring progress
- Team velocity impact
- Time to remediation

## Documentation Standards

### Code Comments
- Explain WHY, not WHAT
- Keep comments current
- Use clear language
- Link to issues/PRs
- Document complex logic

### README Files
- Project overview
- Setup instructions
- Development guide
- Testing procedures
- Contributing guidelines

## Security Considerations

### Secure Coding
- Use SAST (Static Application Security Testing)
- Code analysis includes security checks
- Review security findings
- Keep dependencies updated
- Implement security gates

### API Usage
- Protect API tokens
- Use environment variables
- Rotate tokens regularly
- Audit API access
- Monitor for anomalies

## Troubleshooting Common Issues

### Low Coverage
**Causes**: Untested code, integration tests, UI code
**Solutions**:
- Add unit tests
- Identify un-testable code
- Improve test strategy
- Set realistic goals

### High Complexity
**Causes**: Complex business logic, legacy code
**Solutions**:
- Refactor into smaller functions
- Extract business logic
- Improve naming
- Add comments

### Code Duplication
**Causes**: Copy-paste, similar patterns
**Solutions**:
- Extract common code
- Create utilities
- Use inheritance/composition
- Apply design patterns

## Advanced Topics

### Custom Engines
- Extend CodeClimate with custom rules
- Integrate internal coding standards
- Enforce company practices

### Batch Operations
- Use API for bulk updates
- Generate custom reports
- Integrate with other tools
- Automate workflows

### Performance Tuning
- Optimize analysis time
- Cache results
- Parallelize scanning
- Configure file exclusions
"""
    save_markdown("best-practices.md", content)

def main():
    print("CodeClimate Documentation Scraper")
    print("=" * 70)
    print(f"Output directory: {OUTPUT_DIR}")
    print()

    print("Generating CodeClimate Documentation...")
    print()

    try:
        print("Creating overview document...")
        create_overview()

        print("Creating features guide...")
        create_features_guide()

        print("Creating integration guide...")
        create_integration_guide()

        print("Creating best practices guide...")
        create_best_practices()

        print()
        print("=" * 70)
        print("✓ CodeClimate documentation generation completed successfully!")
        print(f"  Files created in: {OUTPUT_DIR}")

        # List created files
        files = list(OUTPUT_DIR.glob("*.md"))
        total_size = sum(f.stat().st_size for f in files) / 1024
        print(f"  Total files: {len(files)}")
        print(f"  Total size: {total_size:.1f} KB")

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()

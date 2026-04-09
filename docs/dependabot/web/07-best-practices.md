# Dependabot Best Practices

Source: https://docs.github.com/en/code-security/dependabot

## Overview

This guide covers recommended practices for using Dependabot effectively to maintain secure and up-to-date Python projects and other codebases.

## Enable All Three Features

Dependabot works best when you enable all three components:

1. **Dependabot Alerts** - Immediate notification of vulnerabilities
2. **Dependabot Security Updates** - Automatic fixes for vulnerabilities
3. **Dependabot Version Updates** - Regular maintenance updates

Together, they provide comprehensive dependency management.

## Alerts

### Monitor Regularly

- Check your repository's Security tab at least weekly
- Set up notifications for Dependabot alerts
- Review severity levels (critical, high, moderate, low)
- Keep your team informed about active vulnerabilities

### Triage Alerts

Don't dismiss all alerts:

- **Not affected**: Only dismiss if the code path isn't used
- **Tolerable risk**: Document why you're accepting the risk
- **No bandwidth**: Set a reminder to address later
- **Inaccurate**: Report to GitHub if the alert is wrong

### Example Alert Review

1. Click the alert in the Security tab
2. Review affected package and vulnerability details
3. Check the proposed patch version
4. Review associated CVE/GHSA links
5. Decide: merge patch, dismiss, or defer

## Security Updates

### Prioritize Security Over Features

Security updates should be merged faster than other PRs:

- Review security PRs within 24 hours if possible
- Merge after CI passes (assuming no failures)
- Automate merging if your process allows
- Don't let security updates age unnecessarily

### Configuration Example

```yaml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "daily"
    labels:
      - "security"
    assign
ees:
      - "security-team"
```

### Group Security Updates

Reduce notification fatigue by grouping related vulnerabilities:

```yaml
updates:
  - package-ecosystem: "pip"
    directory: "/"
    groups:
      security:
        patterns:
          - "*"
        update-types:
          - "minor"  # Group minor security patches
```

## Version Updates

### Choose Appropriate Update Schedules

Different ecosystems and projects need different cadences:

- **High-security projects**: Weekly or bi-weekly
- **Libraries**: Weekly (stay current with dependencies)
- **Internal tools**: Monthly or quarterly
- **Legacy projects**: Monthly

```yaml
version: 2
updates:
  - package-ecosystem: "pip"
    schedule:
      interval: "weekly"
      day: "monday"
      time: "03:00"
```

### Separate Production and Development Dependencies

Reduce risk by updating development dependencies more frequently:

```yaml
updates:
  - package-ecosystem: "npm"
    groups:
      production:
        dependency-type: "production"
        schedule:
          interval: "monthly"
      development:
        dependency-type: "development"
        schedule:
          interval: "weekly"
```

### Limit Concurrent Pull Requests

Avoid overwhelming your team with updates:

```yaml
open-pull-requests-limit: 5
```

Start with 5, adjust based on your team's capacity.

### Use Dependency Groups

Consolidate updates to reduce noise:

```yaml
groups:
  major-updates:
    dependency-type: "direct"
    update-types:
      - "major"
  minor-patch-updates:
    dependency-type: "direct"
    update-types:
      - "minor"
      - "patch"
```

### Configure Intelligent Rebasing

Allow Dependabot to automatically resolve conflicts:

```yaml
rebase-strategy: "auto"  # Default, recommended
```

This keeps PRs mergeable without manual intervention.

## Python-Specific Practices

### Use dependabot.yml for pip

```yaml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
    dependency-type: "production"
    labels:
      - "dependencies"
```

### Support Multiple Python Versions

If your project supports multiple Python versions:

1. Test updates against all versions in CI
2. Verify compatibility before merging
3. Use GitHub Actions matrix builds

Example matrix CI config:

```yaml
strategy:
  matrix:
    python-version: ["3.9", "3.10", "3.11", "3.12"]
```

### Keep Requirements Files Organized

If using `requirements.txt`, `requirements-dev.txt`, etc.:

```yaml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    dependency-type: "production"

  - package-ecosystem: "pip"
    directory: "/"
    dependency-type: "development"
    schedule:
      interval: "weekly"
```

## Workflow Integration

### Use GitHub Actions for CI/CD

Ensure Dependabot PRs run through the same CI checks as regular PRs:

1. Run tests on all Dependabot PRs
2. Check for breaking changes
3. Verify compatibility
4. Enable auto-merge when tests pass

Example workflow:

```yaml
on: [pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: "3.11"
      - run: pip install -r requirements.txt
      - run: pytest
      - run: lint
```

### Customize Commit Messages

Make PR history clear:

```yaml
commit-message:
  prefix: "chore(deps):"
  include: "scope"
```

Results in commits like: `chore(deps): bump requests from 2.28 to 2.29`

### Automate with Labels

Use labels for automation:

```yaml
labels:
  - "dependencies"
  - "automated"
```

Then set up rules:

```yaml
auto-merge:
  filter:
    - label: "dependencies"
  merge-type: "squash"
```

## Organizational Practices

### Enable Across Organization

Use GitHub organization settings to enforce Dependabot:

1. Go to Organization Settings
2. Enable Dependabot in Security settings
3. Set organization-wide policies
4. Make dependabot.yml a template in new repos

### Document Your Policy

Create a `DEPENDABOT.md` guide for your team:

```markdown
# Dependabot Policy

## For Security Updates
- Review within 24 hours
- Merge after CI passes
- Prioritize over feature work

## For Version Updates
- Review within 1 week
- Check compatibility
- Run full test suite
```

### Assign to Teams

Route PRs to appropriate teams:

```yaml
assignees:
  - "backend-team"  # Group or username
```

### Monitor Inactive Repositories

Set up alerts for repos that go 90 days without Dependabot activity:

```bash
# Check which repos have paused Dependabot
gh repo list --limit 1000 --json name | jq -r '.[].name'
```

## Common Mistakes to Avoid

### 1. Dismissing Too Many Alerts

Don't just dismiss alerts without review. Only dismiss if:
- Truly not applicable to your code
- Risk has been assessed and accepted
- Documented in dismissal comment

### 2. Ignoring Inactivity Warnings

If Dependabot goes inactive:
- Merge some PRs to reactivate
- Don't let security updates pile up
- Re-enable in settings

### 3. Setting Conflicting Schedules

Be consistent:
- Don't have weekly schedules for major and minor updates together
- Separate by dependency type or ecosystem
- Use groups to organize

### 4. Neglecting Documentation

Keep team informed:
- Update CONTRIBUTING.md with Dependabot guidance
- Document dismissal policies
- Track security update SLAs

### 5. Ignoring Breaking Changes

Always review:
- Major version updates
- Dependency compatibility
- Migration requirements
- Test suite results

## Monitoring and Metrics

### Track Metrics

Monitor your Dependabot usage:

- Number of alerts per repository
- Average time to merge security updates
- Version update cadence compliance
- Automatic deactivation incidents

### Set Service Level Objectives (SLOs)

Example targets:

- Critical security updates: Merge within 24 hours
- High severity updates: Merge within 72 hours
- Regular updates: Merge within 2 weeks
- Inactivity: Never exceed 90 days

## Resources

- [GitHub Dependabot Documentation](https://docs.github.com/en/code-security/dependabot)
- [Dependabot Demo Repository](https://github.com/dependabot/demo)
- [Dependabot Blog](https://github.blog/tag/dependabot/)
- [GitHub Security Best Practices](https://docs.github.com/en/code-security)

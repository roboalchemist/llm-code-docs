# DeepScan Integration Guide

# Source: https://deepscan.io

## Overview

DeepScan integrates seamlessly with your development workflow through multiple integration points, from editor plugins to CI/CD pipelines.

## GitHub Integration

### How GitHub Integration Works
DeepScan provides native GitHub integration that:
- **Automatic Repository Synchronization**: Repositories are automatically synced when added to your team
- **Pull Request Code Review**: Inline comments on PRs show detected issues
- **Continuous Monitoring**: Analysis runs automatically as new commits are pushed
- **Private Repository Support**: Analyze private repositories (Starter plan and above)

### Setting Up GitHub Integration

1. **Connect GitHub Account**
   - Link your GitHub account to your DeepScan team
   - Grant DeepScan repository access permissions

2. **Add Repositories**
   - Navigate to team dashboard
   - Select repositories to analyze
   - DeepScan will begin analysis immediately

3. **View PR Feedback**
   - DeepScan comments on pull requests with detected issues
   - Issues appear inline with code
   - Navigate to dashboard for full analysis report

4. **Monitor Team Quality**
   - Dashboard shows overall quality status
   - Track code issues across all projects
   - Monitor lines of code statistics
   - Observe quality trends over time

## Editor Integration

### Visual Studio Code Extension

The official VS Code extension brings DeepScan analysis directly into your editor.

**Features**:
- Real-time issue detection as you code
- Inline error highlighting
- Hover tooltips with issue descriptions
- Quick fixes and suggestions
- Status bar showing project grade
- Integration with VS Code's problem panel

**Installation**:
1. Open VS Code Extensions marketplace
2. Search for "DeepScan"
3. Install official DeepScan extension
4. Sign in with your DeepScan account
5. Select project to analyze

**Available On**: Lite and Starter plans (and higher)

### IntelliJ Integration

DeepScan integrates with JetBrains IDEs including IntelliJ IDEA, WebStorm, and PhpStorm.

**Features**:
- IDE-native inspection integration
- Inline issue detection
- Problem highlighting in editor
- Integration with IDE's inspection framework
- Code analysis in run configurations

**Setup**: Contact support for IntelliJ integration details and configuration.

## CI/CD Pipeline Integration

### GitHub Actions

Integrate DeepScan analysis into your GitHub Actions workflows:

**Example Workflow**:
```yaml
name: DeepScan Analysis
on: [push, pull_request]

jobs:
  deepscan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run DeepScan
        # Detailed setup instructions available in dashboard
        run: |
          # Analysis runs with project configuration
```

**Available**: Included with GitHub integration

### SonarQube Server Integration

For organizations using SonarQube:
- Deploy DeepScan analysis rules in SonarQube
- Integrate with existing SonarQube dashboards
- Combine with SonarQube's analysis pipeline
- Custom rule integration

**Availability**: Enterprise plan

### Command-Line Interface

The CLI allows integration with any CI/CD system:

**Features**:
- Analyze code from command line
- Integrate with Jenkins, CircleCI, GitLab CI, etc.
- Custom pipeline integration
- Automated quality gates
- JSON output for parsing

**Usage**:
```bash
# Analyze project
deepscan analyze [options]

# Generate report
deepscan report --format json

# Integration with quality gates
deepscan analyze --fail-on-error
```

**Availability**: Enterprise plan

### Jenkins Integration

Integrate DeepScan into Jenkins pipelines:

**Pipeline Stage Example**:
```groovy
stage('DeepScan Analysis') {
  steps {
    // DeepScan analysis within Jenkins pipeline
    // Detailed integration guide available in enterprise docs
  }
}
```

### CircleCI Integration

Add DeepScan to CircleCI workflows:

**Configuration**: Available in enterprise documentation

### GitLab CI Integration

Integrate with GitLab CI/CD:

**Configuration**: Contact support for GitLab CI setup details

## Team Collaboration Dashboard

### Dashboard Features

The team collaboration dashboard provides:
- **Team Overview**: Overall quality status of team projects
- **Code Quality Metrics**: Issues found across projects
- **Code Statistics**: Lines of code per project
- **Historical Trends**: Quality tracking over time
- **Team Member Management**: Manage team access
- **Project Configuration**: Configure analysis settings

### Accessing the Dashboard

1. Sign in to your DeepScan account
2. Select your team
3. View dashboard with all projects and metrics
4. Click project to view detailed analysis

### Dashboard Capabilities

- **Real-Time Metrics**: Updates as code is analyzed
- **Drill-Down Analysis**: Click through to specific issues
- **Historical Comparison**: Compare metrics over time
- **Export Reports**: Download project reports
- **Team Sharing**: Share dashboards with team members

## GitHub Marketplace Integration

### Marketplace Installation

DeepScan is available on the GitHub Marketplace:

1. Navigate to GitHub Marketplace
2. Search for "DeepScan"
3. Select plan and billing option
4. GitHub Marketplace handles billing
5. Automatic integration with your GitHub account

### Benefits

- Single bill for GitHub services
- Automatic invoicing
- Simplified account management
- Direct GitHub authentication

**Availability**: Lite and Starter plans

## Project Configuration

### Configuration File

Customize DeepScan analysis through project configuration:

**File Location**: `.deepscan.json` or through dashboard settings

**Configuration Options**:
- Enable/disable specific rules
- Set severity thresholds
- Exclude files or directories
- Configure analysis scope
- Set custom quality gates

### Environment-Specific Configuration

- Different rules for different environments
- Development vs. production analysis
- Branch-specific configurations
- Scope analysis based on project type

## Enterprise Deployment Options

### Self-Hosted Deployment

For organizations requiring on-premises analysis:

**Options**:
- Docker-based deployment
- Kubernetes integration
- Private infrastructure setup
- Air-gapped environments

**Features**:
- Complete data privacy
- No code sent to cloud services
- Custom deployment architecture
- Internal CI/CD integration

### Infrastructure Integration

- Deploy alongside SonarQube
- Integrate with existing CI/CD infrastructure
- Custom networking setup
- Firewall and proxy compatibility

## Security and Privacy

### Data Handling
- Code analysis performed securely
- Historical data retention based on plan
- Integration with GitHub's security model
- Enterprise options for self-hosted analysis

### Permissions and Access Control
- Team member permission levels
- Repository-level access control
- Project-level restrictions
- Audit logging for enterprise

## Support and Resources

### Help and Documentation
- Online documentation portal
- FAQ and troubleshooting guides
- Integration tutorials
- Code examples

### Support Channels
- **Free Plan**: Community support
- **Lite/Starter**: Email support
- **Enterprise**: Dedicated account manager
- **Status Page**: System status monitoring

### Getting Help
1. Check online documentation
2. Search FAQ for your question
3. Contact support with details
4. Enterprise users have dedicated support

---

**Learn More**: Visit [deepscan.io](https://deepscan.io) for latest integration information and setup guides.

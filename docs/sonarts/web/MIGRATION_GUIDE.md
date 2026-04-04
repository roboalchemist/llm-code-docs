# Migrating from SonarTS to Modern Solutions

## Source
https://github.com/SonarSource/SonarTS

## Overview

SonarTS was archived in April 2021 and is no longer maintained. This guide helps you migrate from SonarTS to modern SonarQube/SonarCloud or alternative solutions.

## Why Migrate?

| Issue | Impact |
|-------|--------|
| No security updates | Vulnerability exposure |
| No new features | Missing modern TypeScript support |
| No bug fixes | Stability and reliability issues |
| Archived repository | Community support ends |
| Modern alternatives available | Better, more capable solutions |

## Migration Timeline

### Immediate (1-2 weeks)
- [ ] Assess current SonarTS usage
- [ ] Evaluate migration options
- [ ] Set up target platform (SonarCloud or SonarQube)
- [ ] Run parallel analysis

### Short-term (1 month)
- [ ] Test analysis on real projects
- [ ] Configure quality gates
- [ ] Train team on new platform
- [ ] Run baseline analysis

### Medium-term (2-3 months)
- [ ] Migrate CI/CD pipelines
- [ ] Update documentation
- [ ] Archive SonarTS infrastructure
- [ ] Decommission SonarTS

## Option 1: Migrate to SonarCloud (Easiest)

### Advantages
- Zero installation/maintenance
- Free tier available
- Cloud-based (no server)
- Integrated with GitHub, GitLab, Bitbucket, Azure DevOps
- Automatic analysis on every push
- AI CodeFix (premium)
- Better JavaScript/TypeScript support

### Migration Steps

#### 1. Create SonarCloud Account

```bash
# Visit https://sonarcloud.io
# Sign up with GitHub/GitLab/Bitbucket/Azure DevOps account
# Create organization
```

#### 2. Add Repository

```bash
# In SonarCloud:
# - Click "Add project"
# - Select your repository
# - Follow setup wizard
```

#### 3. Update Configuration

Create `sonar-project.properties`:

```properties
sonar.projectKey=your-org:project-name
sonar.projectName=My Project
sonar.projectVersion=1.0

# No sonar.language=ts needed - auto-detected
sonar.sources=src
sonar.tests=__tests__
sonar.exclusions=node_modules/**,coverage/**

# Coverage
sonar.typescript.lcov.reportPaths=coverage/lcov.info
```

#### 4. Generate Token

```bash
# In SonarCloud:
# - User menu > Security > Generate Tokens
# - Copy token
# - Add to CI/CD secrets as SONARCLOUD_TOKEN
```

#### 5. Update CI/CD Pipeline

**GitHub Actions**:
```yaml
name: SonarCloud Analysis
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  sonarcloud:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0  # Full history for better analysis

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Install dependencies
        run: npm install

      - name: Run tests with coverage
        run: npm run test:coverage

      - name: SonarCloud scan
        uses: SonarSource/sonarcloud-github-action@master
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          SONAR_TOKEN: ${{ secrets.SONARCLOUD_TOKEN }}
```

**GitLab CI**:
```yaml
sonarcloud:
  image: node:18
  stage: test
  script:
    - npm install
    - npm run test:coverage
    - npm install -D sonarcloud
    - npx sonar-scanner
      -Dsonar.projectKey=$CI_PROJECT_NAMESPACE:$CI_PROJECT_NAME
      -Dsonar.sources=src
      -Dsonar.typescript.lcov.reportPaths=coverage/lcov.info
      -Dsonar.host.url=https://sonarcloud.io
      -Dsonar.organization=$SONAR_ORGANIZATION
      -Dsonar.login=$SONAR_TOKEN
  only:
    - merge_requests
    - main
```

#### 6. Verify Results

```bash
# Wait for analysis to complete (1-5 minutes)
# Check SonarCloud dashboard:
# - Code quality metrics
# - Security hotspots
# - Coverage report
# - Pull request feedback
```

### Cost Comparison

| Feature | SonarCloud Free | SonarCloud Pro |
|---------|-----------------|----------------|
| Public repositories | Free | Free |
| Private repositories | Free (limited) | Paid |
| Pull request reviews | Yes | Yes |
| AI CodeFix | No | Yes |
| Advanced security | Basic | Full |
| Support | Community | Priority |

## Option 2: Migrate to SonarQube (Enterprise)

### Advantages
- Self-hosted (full control)
- No SaaS dependency
- Enterprise features
- Custom plugins
- Compliance-friendly

### Migration Steps

#### 1. Install SonarQube

**Docker Compose (Recommended)**:

```yaml
version: '3.8'

services:
  sonarqube:
    image: sonarqube:lts
    container_name: sonarqube
    environment:
      SONARQUBE_JDBC_URL: jdbc:postgresql://postgres:5432/sonarqube
      SONARQUBE_JDBC_USERNAME: sonarqube
      SONARQUBE_JDBC_PASSWORD: sonarqube
      SONAR_ADMIN_PASSWORD: admin
    ports:
      - "9000:9000"
    volumes:
      - sonarqube_data:/opt/sonarqube/data
      - sonarqube_extensions:/opt/sonarqube/extensions
      - sonarqube_logs:/opt/sonarqube/logs
    depends_on:
      - postgres
    networks:
      - sonarnet

  postgres:
    image: postgres:13
    container_name: postgres
    environment:
      POSTGRES_DB: sonarqube
      POSTGRES_USER: sonarqube
      POSTGRES_PASSWORD: sonarqube
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - sonarnet

volumes:
  sonarqube_data:
  sonarqube_extensions:
  sonarqube_logs:
  postgres_data:

networks:
  sonarnet:
```

**Start services**:
```bash
docker-compose up -d
# Access at http://localhost:9000
# Default credentials: admin/admin
```

#### 2. Create Project

```bash
# In SonarQube web interface:
# - Administration > Projects > Create Project
# - Enter project key and display name
```

#### 3. Generate Token

```bash
# User menu > My Account > Security
# Generate token
# Copy and store securely
```

#### 4. Configure Project

`sonar-project.properties`:
```properties
sonar.projectKey=my-typescript-project
sonar.projectName=My TypeScript Project
sonar.sources=src
sonar.tests=__tests__
sonar.typescript.lcov.reportPaths=coverage/lcov.info
sonar.exclusions=node_modules/**
```

#### 5. Run Analysis

```bash
npx sonar-scanner \
  -Dsonar.projectKey=my-typescript-project \
  -Dsonar.sources=src \
  -Dsonar.typescript.lcov.reportPaths=coverage/lcov.info \
  -Dsonar.host.url=http://sonarqube:9000 \
  -Dsonar.login=your-token
```

#### 6. Integrate with CI/CD

```bash
# Jenkins Declarative Pipeline
pipeline {
    agent any

    environment {
        SONAR_HOST = credentials('sonar-host-url')
        SONAR_TOKEN = credentials('sonar-token')
    }

    stages {
        stage('Build & Test') {
            steps {
                sh '''
                    npm install
                    npm run test:coverage
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                sh '''
                    npx sonar-scanner \
                        -Dsonar.projectKey=my-project \
                        -Dsonar.sources=src \
                        -Dsonar.host.url=${SONAR_HOST} \
                        -Dsonar.login=${SONAR_TOKEN}
                '''
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}
```

## Option 3: Lightweight Migration to ESLint

### For projects wanting simpler analysis

```bash
# Install ESLint and SonarJS plugin
npm install -D eslint eslint-plugin-sonarjs typescript @typescript-eslint/parser
```

`.eslintrc.json`:
```json
{
  "parser": "@typescript-eslint/parser",
  "parserOptions": {
    "ecmaVersion": 2021,
    "sourceType": "module"
  },
  "plugins": ["sonarjs", "@typescript-eslint"],
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:sonarjs/recommended"
  ],
  "rules": {
    "sonarjs/no-all-duplicated-branches": "warn",
    "sonarjs/no-identical-expressions": "error",
    "sonarjs/cognitive-complexity": ["warn", 15]
  }
}
```

**package.json**:
```json
{
  "scripts": {
    "lint": "eslint src",
    "lint:fix": "eslint src --fix"
  }
}
```

## Comparing Rule Coverage

### SonarTS Rules

Rules that must be replaced in migration:

| Rule | SonarTS | SonarCloud/Qube | ESLint |
|------|---------|-----------------|--------|
| no-all-duplicated-branches | ✓ | ✓ | sonarjs |
| no-identical-expressions | ✓ | ✓ | sonarjs |
| cognitive-complexity | ✓ | ✓ | sonarjs |
| dead code detection | ✓ | ✓ | no-unreachable |
| security hotspots | ✓ | ✓ (Enhanced) | - |
| coverage reporting | ✓ | ✓ | - |

## Data Migration

### Export SonarTS Results

```bash
# Get project analysis data via API
curl -u user:password \
  "http://sonarqube:9000/api/ce/activity?project=my-project" \
  > sonarts-analysis.json

# Export quality gate settings
curl -u user:password \
  "http://sonarqube:9000/api/qualitygates/show?name=MyQualityGate" \
  > quality-gate.json
```

### Import to New Platform

**SonarCloud**: No import needed - start fresh with better analysis

**SonarQube**: Configure same quality gates and rules:
```bash
# Via web interface:
# - Administration > Quality Gates > Copy existing gate
# - Adjust rules based on new JavaScript/TypeScript analyzer
```

## Rollout Plan

### Phase 1: Setup (Week 1)
```
[ ] Choose migration target (SonarCloud/SonarQube/ESLint)
[ ] Create account/infrastructure
[ ] Configure initial project
[ ] Run parallel analysis on sample project
[ ] Compare results
```

### Phase 2: Pilot (Week 2-3)
```
[ ] Migrate 2-3 sample projects
[ ] Test CI/CD integration
[ ] Train team
[ ] Document new workflow
[ ] Collect feedback
```

### Phase 3: Rollout (Week 4+)
```
[ ] Migrate all projects batch by batch
[ ] Update CI/CD for all repositories
[ ] Archive SonarTS configuration
[ ] Decommission SonarTS infrastructure
[ ] Monitor for issues
```

### Phase 4: Cleanup (Month 2)
```
[ ] Remove SonarTS plugin
[ ] Delete legacy SonarQube instance (if self-hosted)
[ ] Archive SonarTS documentation
[ ] Final verification
```

## Troubleshooting Migration

### Issue: Quality Gate Stricter in New Platform

**Cause**: Modern analyzers find more issues

**Solution**:
1. Run parallel analysis to measure impact
2. Adjust quality gate rules gradually
3. Focus on CRITICAL and BLOCKER issues first
4. Gradually increase strictness over sprints

### Issue: Coverage Not Showing

**Ensure**:
```bash
# Generate coverage in supported format
npm run test:coverage

# Verify LCOV file exists
ls coverage/lcov.info

# Specify in configuration
sonar.typescript.lcov.reportPaths=coverage/lcov.info
```

### Issue: Performance Degradation

**Check**:
- Analysis time longer than expected
- Increase memory allocation
- Optimize exclusions (exclude node_modules, coverage, etc.)

## Success Metrics

Track after migration:

| Metric | Target |
|--------|--------|
| Analysis time | <10 minutes per run |
| PR review time | <5 minutes feedback |
| Rule coverage | >90% parity with SonarTS |
| Team satisfaction | >4/5 rating |
| Issue detection rate | Same or better |

## Summary

**Recommended Migration Path**:

1. **For most projects**: SonarCloud (easiest, best support)
2. **For enterprises**: SonarQube LTS (self-hosted, full control)
3. **For lightweight needs**: ESLint + SonarJS plugin (simplest)

All modern solutions provide superior TypeScript analysis with ongoing updates, better security detection, and improved developer experience compared to legacy SonarTS.

**Start migration today** - SonarTS support has ended, and modern alternatives are production-ready.

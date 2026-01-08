# SonarTS Installation and Setup

## Source
https://github.com/SonarSource/SonarTS

## Status: DEPRECATED

This documentation is for reference only. SonarTS has been archived and is no longer maintained. For new projects, use **SonarCloud** or **SonarQube** instead.

## Legacy Installation Guide

### Prerequisites

- **Java**: JDK 8 or higher
- **SonarQube**: 7.9 LTS or compatible version
- **Node.js**: 8.x or higher (for development/testing)
- **npm**: 5.x or higher

### Installation Steps

#### 1. Download SonarTS Plugin

Download the latest SonarTS 2.1 JAR file from:
https://github.com/SonarSource/SonarTS/releases

```bash
# Example: SonarTS 2.1 (final release)
wget https://github.com/SonarSource/SonarTS/releases/download/2.1.0.4524/sonar-typescript-plugin-2.1.0.4524.jar
```

#### 2. Install Plugin

```bash
# Copy JAR to SonarQube extensions directory
cp sonar-typescript-plugin-2.1.0.4524.jar $SONARQUBE_HOME/extensions/plugins/

# Restart SonarQube
$SONARQUBE_HOME/bin/[linux|macosx|windows]/sonar.sh restart
```

#### 3. Verify Installation

```bash
# Access SonarQube web interface
# http://localhost:9000

# Navigate to Administration > Marketplace > Installed Plugins
# Should show: SonarTS 2.1
```

### Project Configuration

Create `sonar-project.properties` in project root:

```properties
# Project identification
sonar.projectKey=com.example:my-typescript-project
sonar.projectName=My TypeScript Project
sonar.projectVersion=1.0

# Source code
sonar.sources=src
sonar.exclusions=**/*.test.ts,**/*.spec.ts,node_modules/**

# Language
sonar.language=ts

# Optional: Test coverage
sonar.typescript.lcov.reportPaths=coverage/lcov.info

# Optional: Testing
sonar.tests=src
sonar.test.inclusions=**/*.test.ts,**/*.spec.ts
```

### SonarScanner Installation

#### Via npm (Recommended for TypeScript projects)

```bash
# Install SonarScanner for npm
npm install -D sonar-scanner

# Or globally
npm install -g sonar-scanner
```

#### Via Homebrew (macOS)

```bash
brew install sonar-scanner
```

#### Via Docker

```bash
docker run --rm \
  -e SONAR_HOST_URL=http://sonarqube:9000 \
  -e SONAR_LOGIN=your-token \
  -v "$(pwd):/usr/src" \
  sonarsource/sonar-scanner-cli
```

### Running Analysis

#### Local Analysis

```bash
# Install dependencies
npm install

# Run SonarTS analysis
npx sonar-scanner \
  -Dsonar.projectKey=my-project \
  -Dsonar.sources=src \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.login=your-sonarqube-token
```

#### With Coverage Report

```bash
# Generate coverage (example with Jest)
npm run test:coverage

# Run analysis with coverage
npx sonar-scanner \
  -Dsonar.projectKey=my-project \
  -Dsonar.sources=src \
  -Dsonar.typescript.lcov.reportPaths=coverage/lcov.info \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.login=your-sonarqube-token
```

#### Docker Analysis

```bash
docker run --rm \
  -e SONAR_HOST_URL=http://sonarqube:9000 \
  -e SONAR_LOGIN=your-token \
  -v "$(pwd):/usr/src" \
  sonarsource/sonar-scanner-cli \
  -Dsonar.projectKey=my-project \
  -Dsonar.sources=src
```

## Troubleshooting

### Issue: Plugin Not Loading

**Error**: TypeScript language not detected

**Solution**:
1. Verify JAR file is in `extensions/plugins/`
2. Check file permissions: `chmod 644 sonar-typescript-plugin-*.jar`
3. Restart SonarQube: `sonar.sh restart`
4. Check SonarQube logs: `tail -f logs/sonar.log`

### Issue: No TypeScript Files Detected

**Error**: 0 files analyzed

**Cause**: File extension or source path configuration

**Solution**:
```properties
# Ensure .ts and .tsx extensions are recognized
sonar.sources=src
sonar.inclusions=**/*.ts,**/*.tsx

# Exclude test files if needed
sonar.exclusions=**/*.test.ts,**/*.spec.ts
```

### Issue: Analysis Fails with Node Version Error

**Error**: Unsupported Node.js version

**Solution**: Upgrade Node.js to 8.x or higher
```bash
node --version  # Check current version
nvm install 16  # Upgrade with nvm
nvm use 16
```

### Issue: Token Authentication Fails

**Error**: Unauthorized (401)

**Solution**:
1. Generate new token in SonarQube: Administration > Security > Users
2. Verify token is passed correctly:
   ```bash
   -Dsonar.login=your-generated-token
   ```
3. Check token permissions include "Execute Analysis"

## Integration Examples

### GitHub Actions

```yaml
name: SonarTS Analysis

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  sonarts:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Install dependencies
        run: npm install

      - name: Generate coverage
        run: npm run test:coverage

      - name: SonarTS analysis
        env:
          SONAR_HOST_URL: https://your-sonarqube.com
          SONAR_LOGIN: ${{ secrets.SONAR_TOKEN }}
        run: |
          npx sonar-scanner \
            -Dsonar.projectKey=my-project \
            -Dsonar.sources=src \
            -Dsonar.typescript.lcov.reportPaths=coverage/lcov.info
```

### GitLab CI

```yaml
sonarts-analysis:
  stage: test
  image: node:16
  script:
    - npm install
    - npm run test:coverage
    - npm install -D sonar-scanner
    - npx sonar-scanner
      -Dsonar.projectKey=$CI_PROJECT_NAME
      -Dsonar.sources=src
      -Dsonar.host.url=$SONAR_HOST_URL
      -Dsonar.login=$SONAR_TOKEN
  only:
    - merge_requests
    - main
```

### Jenkins Pipeline

```groovy
pipeline {
    agent any

    stages {
        stage('Install') {
            steps {
                sh 'npm install'
            }
        }

        stage('Test & Coverage') {
            steps {
                sh 'npm run test:coverage'
            }
        }

        stage('SonarTS Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh '''
                        npx sonar-scanner \
                            -Dsonar.projectKey=my-project \
                            -Dsonar.sources=src \
                            -Dsonar.typescript.lcov.reportPaths=coverage/lcov.info
                    '''
                }
            }
        }

        stage('Quality Gate') {
            steps {
                waitForQualityGate abortPipeline: true
            }
        }
    }
}
```

## Example Project Structure

```
my-typescript-project/
├── src/
│   ├── app.ts
│   ├── services/
│   │   └── api.ts
│   └── utils/
│       └── helpers.ts
├── __tests__/
│   ├── app.test.ts
│   └── services/
│       └── api.test.ts
├── coverage/
│   ├── lcov.info
│   └── index.html
├── sonar-project.properties
├── package.json
└── tsconfig.json
```

## Modern Alternatives

Instead of SonarTS, use:

### Option 1: SonarCloud (Recommended for most projects)

```bash
# Simple setup - no installation needed
# Just connect your GitHub/GitLab/Bitbucket repo
# Analysis starts automatically

# For manual analysis:
npm install -D sonar-scanner
npx sonar-scanner \
  -Dsonar.projectKey=my-project \
  -Dsonar.sources=src \
  -Dsonar.host.url=https://sonarcloud.io \
  -Dsonar.organization=your-org \
  -Dsonar.login=$SONARCLOUD_TOKEN
```

### Option 2: SonarQube (Enterprise alternative)

```bash
# Docker Compose example
version: '3'
services:
  sonarqube:
    image: sonarqube:latest-lts
    ports:
      - "9000:9000"
    environment:
      SONARQUBE_JDBC_URL: jdbc:postgresql://postgres:5432/sonarqube
      SONARQUBE_JDBC_USERNAME: sonarqube
      SONARQUBE_JDBC_PASSWORD: sonarqube
    depends_on:
      - postgres

  postgres:
    image: postgres:13
    environment:
      POSTGRES_DB: sonarqube
      POSTGRES_USER: sonarqube
      POSTGRES_PASSWORD: sonarqube
```

### Option 3: ESLint with SonarJS Plugin

```bash
npm install -D eslint eslint-plugin-sonarjs
```

```javascript
// .eslintrc.json
{
  "plugins": ["sonarjs"],
  "extends": ["plugin:sonarjs/recommended"],
  "rules": {
    "sonarjs/no-all-duplicated-branches": "warn",
    "sonarjs/no-identical-expressions": "error"
  }
}
```

## Summary

SonarTS is no longer recommended for new installations. The installation guide above is provided for:
- Legacy system maintenance
- Understanding SonarTS architecture
- Migration planning to modern solutions

For new TypeScript projects, use:
1. **SonarCloud** - Easiest setup, cloud-based, free tier available
2. **SonarQube** - Enterprise solution, self-hosted, most control
3. **ESLint** - Lightweight, community-driven, best for continuous feedback

All modern solutions provide superior TypeScript analysis with ongoing updates and community support.

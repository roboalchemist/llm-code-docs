# Source: https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/snyk-cli-for-iac/test-your-iac-files/cloudformation-files.md

# CloudFormation files

With Snyk Infrastructure as Code, you can test your CloudFormation files using the CLI. You can test files in both YAML and JSON formats. You can also scan AWS CDK applications; see [AWS CDK files](https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/snyk-cli-for-iac/test-your-iac-files/aws-cdk-files).

Test for an issue in specified files using the following command:

```
snyk iac test
```

Example:

```
snyk iac test deploy.yaml
```

You can also specify multiple files by appending the file names after each other, for example:

```
snyk iac test file-1.yaml file-2.yaml
```

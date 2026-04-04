# Source: https://docs.aws.amazon.com/cfn-guard/latest/ug/llms.txt

# AWS CloudFormation Guard User Guide

> Provides a conceptual overview of the AWS CloudFormation Guard open-source policy-as-code evaluation tool. Includes walkthroughs for writing policy rules and validating data against rules using the Guard CLI.

- [What is AWS CloudFormation Guard?](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html)
- [Troubleshooting Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/troubleshooting.html)
- [Security](https://docs.aws.amazon.com/cfn-guard/latest/ug/security.html)
- [Document history](https://docs.aws.amazon.com/cfn-guard/latest/ug/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/cfn-guard/latest/ug/glossary.html)

## [Setting up Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/setting-up.html)

- [For Linux and macOS](https://docs.aws.amazon.com/cfn-guard/latest/ug/setting-up-linux.html): Describes how to install AWS CloudFormation Guard for Linux and macOS using the pre-built release binary, through Cargo, or Homebrew.
- [For Windows](https://docs.aws.amazon.com/cfn-guard/latest/ug/setting-up-windows.html): Describes the necessary prerequisites and how to install AWS CloudFormation Guard for Windows through Cargo or through Chocolatey.
- [As an AWS Lambda function](https://docs.aws.amazon.com/cfn-guard/latest/ug/setting-up-lambda.html): Describes how to install AWS CloudFormation Guard through Cargo, the Rust package manager.


## [Prerequisites and overview for using Guard rules](https://docs.aws.amazon.com/cfn-guard/latest/ug/getting-started.html)

### [Writing Guard rules](https://docs.aws.amazon.com/cfn-guard/latest/ug/writing-rules.html)

Learn how to write Guard rules so that you can validate your JSON- or YAML-formatted data against them.

- [Defining queries and filtering](https://docs.aws.amazon.com/cfn-guard/latest/ug/query-and-filtering.html): Learn how to write queries and use filtering when writing Guard rule clauses.
- [Assigning and referencing variables in Guard rules](https://docs.aws.amazon.com/cfn-guard/latest/ug/variables.html): Assign and reference variables in your Guard rules to promote reusability and remove verbosity and repetition when writing rules.
- [Composing named-rule blocks](https://docs.aws.amazon.com/cfn-guard/latest/ug/named-rule-block-composition.html): Describes how to write named-rule blocks for AWS CloudFormation Guard using conditional dependency or correlational dependency.
- [Writing clauses to perform context-aware evaluations](https://docs.aws.amazon.com/cfn-guard/latest/ug/context-aware-evaluations.html): Learn how to reference context values when writing Guard rules.
- [Testing Guard rules](https://docs.aws.amazon.com/cfn-guard/latest/ug/testing-rules.html): Test Guard rules against input data by using the Guard test command to ensure that rules work as intended.
- [Using input parameters with Guard rules](https://docs.aws.amazon.com/cfn-guard/latest/ug/using-input-parameters.html): Use the Guard input parameters for dynamic data lookups during validation.
- [Validating input data against Guard rules](https://docs.aws.amazon.com/cfn-guard/latest/ug/validating-rules.html): Use the Guard validate command to validate input data against Guard rules.


## [Guard CLI reference](https://docs.aws.amazon.com/cfn-guard/latest/ug/cfn-guard-command-reference.html)

- [Guard CLI global parameters](https://docs.aws.amazon.com/cfn-guard/latest/ug/cfn-guard-global-parameters.html): You can use the following parameters with any AWS CloudFormation Guard CLI command.
- [parse-tree](https://docs.aws.amazon.com/cfn-guard/latest/ug/cfn-guard-parse-tree.html): Generates a parse tree for the AWS CloudFormation Guard rules defined in a rules file.
- [rulegen](https://docs.aws.amazon.com/cfn-guard/latest/ug/cfn-guard-rulegen.html): Takes a JSON- or YAML-formatted AWS CloudFormation template file and autogenerates a set of AWS CloudFormation Guard rules that match the properties of the template resources.
- [test](https://docs.aws.amazon.com/cfn-guard/latest/ug/cfn-guard-test.html): Validates an AWS CloudFormation Guard rules file against a Guard unit testing file in JSON or YAML format to determine the success of individual rules.
- [validate](https://docs.aws.amazon.com/cfn-guard/latest/ug/cfn-guard-validate.html): Validates data against AWS CloudFormation Guard rules to determine success or failure.

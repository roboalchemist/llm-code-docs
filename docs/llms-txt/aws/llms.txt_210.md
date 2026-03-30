# Source: https://docs.aws.amazon.com/codeartifact/latest/ug/llms.txt

# CodeArtifact CodeArtifact User Guide

> AWS CodeArtifact User Guide

- [AWS CloudFormation resources](https://docs.aws.amazon.com/codeartifact/latest/ug/cloudformation-codeartifact.html)
- [Troubleshooting](https://docs.aws.amazon.com/codeartifact/latest/ug/troubleshooting.html)
- [Tagging resources](https://docs.aws.amazon.com/codeartifact/latest/ug/tag-resources.html)
- [Quotas in AWS CodeArtifact](https://docs.aws.amazon.com/codeartifact/latest/ug/service-limits.html)
- [Document history](https://docs.aws.amazon.com/codeartifact/latest/ug/history.html)

## [What is AWS CodeArtifact?](https://docs.aws.amazon.com/codeartifact/latest/ug/welcome.html)

- [Concepts](https://docs.aws.amazon.com/codeartifact/latest/ug/codeartifact-concepts.html): AWS CodeArtifact terminology and concepts, including an overview of domains, repositories, packages, assets, and more.


## [Setting up](https://docs.aws.amazon.com/codeartifact/latest/ug/get-set-up-for-codeartifact.html)

- [Sign up for AWS](https://docs.aws.amazon.com/codeartifact/latest/ug/get-set-up-sign-up-for-aws.html): Sign up for AWS to get ready to use CodeArtifact for the first time.
- [Install or upgrade and then configure the AWS CLI](https://docs.aws.amazon.com/codeartifact/latest/ug/get-set-up-install-cli.html): Install, upgrade, and configure the AWS CLI for use with CodeArtifact.
- [Provision an IAM user](https://docs.aws.amazon.com/codeartifact/latest/ug/get-set-up-provision-user.html): Prepare an IAM user to use CodeArtifact.
- [Install your package manager or build tool](https://docs.aws.amazon.com/codeartifact/latest/ug/getting-started-install-package-manager.html): Install the build tools that you want to use with CodeArtifact.


## [Getting started](https://docs.aws.amazon.com/codeartifact/latest/ug/getting-started.html)

- [Getting started using the console](https://docs.aws.amazon.com/codeartifact/latest/ug/getting-started-console.html): Create a domain and repositories in CodeArtifact using the AWS Management Console.
- [Getting started using the AWS CLI](https://docs.aws.amazon.com/codeartifact/latest/ug/getting-started-cli.html): Create a domain and repositories in CodeArtifact using the AWS CLI.


## [Working with repositories](https://docs.aws.amazon.com/codeartifact/latest/ug/repos.html)

- [Create a repository](https://docs.aws.amazon.com/codeartifact/latest/ug/create-repo.html): Create a repository for packages in CodeArtifact using the console or AWS CLI.
- [Connect to a repository](https://docs.aws.amazon.com/codeartifact/latest/ug/connect-repo.html): Connect to a repository in CodeArtifact using npm, Maven, or Python.
- [Delete a repository](https://docs.aws.amazon.com/codeartifact/latest/ug/delete-repo.html): Delete a repository in CodeArtifact using the console or AWS CLI.
- [List repositories](https://docs.aws.amazon.com/codeartifact/latest/ug/list-repos.html): List all the repositories in your AWS account or domain for CodeArtifact.
- [View or modify a repository configuration](https://docs.aws.amazon.com/codeartifact/latest/ug/config-repos.html): View and edit a repository configuration in CodeArtifact.
- [Repository policies](https://docs.aws.amazon.com/codeartifact/latest/ug/repo-policies.html): Control access to repositories in CodeArtifact by creating resource policies.
- [Tag a repository](https://docs.aws.amazon.com/codeartifact/latest/ug/tag-repositories.html): Describes how to tag repository resources in CodeArtifact.


## [Working with upstream repositories](https://docs.aws.amazon.com/codeartifact/latest/ug/repos-upstream.html)

- [Add or remove upstream repositories](https://docs.aws.amazon.com/codeartifact/latest/ug/repo-upstream-add.html): Follow the steps in the following sections to add or remove upstream repositories to or from an CodeArtifact repository.
- [Connect a CodeArtifact repository to a public repository](https://docs.aws.amazon.com/codeartifact/latest/ug/external-connection.html): Consume open-source dependencies used by your application by adding a connection between a CodeArtifact repository and an external public repository.
- [Requesting a package version with upstream repositories](https://docs.aws.amazon.com/codeartifact/latest/ug/repo-upstream-behavior.html): Learn what happens when a client requests a package version from a repository in CodeArtifact that contains upstream repositories.
- [Requesting packages from external connections](https://docs.aws.amazon.com/codeartifact/latest/ug/external-connection-requesting-packages.html): Learn about CodeArtifact behavior regarding external connection availability and package availability from external connections.
- [Upstream repository priority order](https://docs.aws.amazon.com/codeartifact/latest/ug/repo-upstream-search-order.html): Determine the priority order when you request a package version from a repository in CodeArtifact that contains upstream repositories.
- [API behavior with upstream repositories](https://docs.aws.amazon.com/codeartifact/latest/ug/upstream-repo-api-behavior.html): Learn about how many of the AWS CodeArtifact APIs interact with repositories that are connected to upstream repositories.


## [Working with packages](https://docs.aws.amazon.com/codeartifact/latest/ug/packages.html)

- [Packages overview](https://docs.aws.amazon.com/codeartifact/latest/ug/packages-overview.html): Overview of packages in CodeArtifact, including publishing and version status.
- [List package names](https://docs.aws.amazon.com/codeartifact/latest/ug/list-packages.html): List all the package names in a repository using CodeArtifact.
- [List package versions](https://docs.aws.amazon.com/codeartifact/latest/ug/list-packages-versions.html): List all the versions of a package name in a CodeArtifact repository using the AWS CLI.
- [List package version assets](https://docs.aws.amazon.com/codeartifact/latest/ug/list-assets.html): List the individual files in CodeArtifact that are associated with a specific package version using the AWS CLI.
- [Download package version assets](https://docs.aws.amazon.com/codeartifact/latest/ug/download-assets.html): Download the individual files in CodeArtifact that are associated with a specific package version using the AWS CLI.
- [Copy packages between repositories](https://docs.aws.amazon.com/codeartifact/latest/ug/copy-package.html): Copy one or more package versions from a source repository to a destination repository in the same domain in CodeArtifact.
- [Delete a package or package version](https://docs.aws.amazon.com/codeartifact/latest/ug/delete-package.html): Learn how to delete a package in AWS CodeArtifact.
- [View and update package version details and dependencies](https://docs.aws.amazon.com/codeartifact/latest/ug/describe-package-version.html): You can view information about a package version, including dependencies, in CodeArtifact.
- [Update package version status](https://docs.aws.amazon.com/codeartifact/latest/ug/update-package-version-status.html): Every package version in CodeArtifact has a status that describes the current state and availability of the package version.
- [Editing package origin controls](https://docs.aws.amazon.com/codeartifact/latest/ug/package-origin-controls.html): In AWS CodeArtifact, package versions can be added to a repository by directly publishing them, pulling them down from an upstream repository, or ingesting them from an external, public repository.


## [Working with package groups](https://docs.aws.amazon.com/codeartifact/latest/ug/package-groups.html)

- [Create a package group](https://docs.aws.amazon.com/codeartifact/latest/ug/create-package-group.html): You can create a package group using the CodeArtifact console, the AWS Command Line Interface (AWS CLI), or CloudFormation.
- [View or edit a package group](https://docs.aws.amazon.com/codeartifact/latest/ug/view-edit-package-group.html): You can view a list of all package groups, view details of a specific package group, or edit a package group's details or configuration using the CodeArtifact console or the AWS Command Line Interface (AWS CLI).
- [Delete a package group](https://docs.aws.amazon.com/codeartifact/latest/ug/delete-package-group.html): You can delete a package group using the CodeArtifact console or the AWS Command Line Interface (AWS CLI).
- [Package group origin controls](https://docs.aws.amazon.com/codeartifact/latest/ug/package-group-origin-controls.html): Package origin controls are used to configure how package versions can enter a domain.
- [Package group definition syntax and matching behavior](https://docs.aws.amazon.com/codeartifact/latest/ug/package-group-definition-syntax-matching-behavior.html): This topic contains information about defining package groups, pattern matching behavior, package association strength, and package group hierarchy.
- [Tag a package group](https://docs.aws.amazon.com/codeartifact/latest/ug/package-group-tags.html): Tags are key-value pairs associated with AWS resources.


## [Working with domains](https://docs.aws.amazon.com/codeartifact/latest/ug/domains.html)

- [Domain overview](https://docs.aws.amazon.com/codeartifact/latest/ug/domain-overview.html): When you're working with CodeArtifact, domains are useful for the following:
- [Create a domain](https://docs.aws.amazon.com/codeartifact/latest/ug/domain-create.html): Create a domain for repositories in CodeArtifact using the console or AWS CLI.
- [Delete a domain](https://docs.aws.amazon.com/codeartifact/latest/ug/delete-domain.html): Delete a domain in CodeArtifact using the console or AWS CLI.
- [Domain policies](https://docs.aws.amazon.com/codeartifact/latest/ug/domain-policies.html): Use policies to specify who has access to a CodeArtifact resource and which actions they can perform on it.
- [Tag a domain](https://docs.aws.amazon.com/codeartifact/latest/ug/tag-domains.html): Describes how to tag domain resources in CodeArtifact.


## [Using Cargo](https://docs.aws.amazon.com/codeartifact/latest/ug/using-cargo.html)

- [Configure and use Cargo](https://docs.aws.amazon.com/codeartifact/latest/ug/configure-use-cargo.html): You can use Cargo to publish and download crates from CodeArtifact repositories or to fetch crates from crates.io, the Rust community's crate registry.
- [Cargo command support](https://docs.aws.amazon.com/codeartifact/latest/ug/cargo-commands.html): The following sections summarize the Cargo commands that are supported by CodeArtifact repositories, in addition to specific commands that are not supported.


## [Using Maven](https://docs.aws.amazon.com/codeartifact/latest/ug/using-maven.html)

- [Use CodeArtifact with Gradle](https://docs.aws.amazon.com/codeartifact/latest/ug/maven-gradle.html): After you have the CodeArtifact auth token in an environment variable as described in Pass an auth token using an environment variable, follow these instructions to consume Maven packages from, and publish new packages to, a CodeArtifact repository.
- [Use CodeArtifact with mvn](https://docs.aws.amazon.com/codeartifact/latest/ug/maven-mvn.html): You use the mvn command to execute Maven builds.
- [Use CodeArtifact with deps.edn](https://docs.aws.amazon.com/codeartifact/latest/ug/maven-deps.html): You use deps.edn with clj to manage dependencies for Clojure projects.
- [Publishing with curl](https://docs.aws.amazon.com/codeartifact/latest/ug/maven-curl.html): This section shows how to use the HTTP client curl to publish Maven artifacts to a CodeArtifact repository.
- [Use Maven checksums](https://docs.aws.amazon.com/codeartifact/latest/ug/maven-checksums.html): When a Maven artifact is published to an AWS CodeArtifact repository, the checksum associated with each asset or file in the package is used to validate the upload.
- [Use Maven snapshots](https://docs.aws.amazon.com/codeartifact/latest/ug/maven-snapshots.html): A Maven snapshot is a special version of a Maven package that refers to the latest production branch code.
- [Requesting Maven packages from upstreams and external connections](https://docs.aws.amazon.com/codeartifact/latest/ug/maven-upstream-external-connections-request.html): Request Maven packages in AWS CodeArtifact from upstreams and external connections.
- [Maven troubleshooting](https://docs.aws.amazon.com/codeartifact/latest/ug/maven-troubleshooting.html): The following information might help you troubleshoot common issues with Maven and CodeArtifact.


## [Using npm](https://docs.aws.amazon.com/codeartifact/latest/ug/using-npm.html)

- [Configure and use npm](https://docs.aws.amazon.com/codeartifact/latest/ug/npm-auth.html): Use the npm client with CodeArtifact to install and publish packages.
- [Configure and use Yarn](https://docs.aws.amazon.com/codeartifact/latest/ug/npm-yarn.html): After you create a repository, you can use the Yarn client to manage npm packages.
- [npm command support](https://docs.aws.amazon.com/codeartifact/latest/ug/npm-commands.html): The following sections summarize the npm commands that are supported, by CodeArtifact repositories, in addition to specific commands that are not supported.
- [npm tag handling](https://docs.aws.amazon.com/codeartifact/latest/ug/npm-tags.html): npm registries support tags, which are string aliases for package versions.
- [Support for npm-compatible package managers](https://docs.aws.amazon.com/codeartifact/latest/ug/npm-other-clients.html): These other package managers are compatible with CodeArtifact and work with the npm package format and npm wire protocol:


## [Using NuGet](https://docs.aws.amazon.com/codeartifact/latest/ug/using-nuget.html)

- [Use CodeArtifact with Visual Studio](https://docs.aws.amazon.com/codeartifact/latest/ug/nuget-visual-studio.html): Configure the Visual Studio to consume packages with CodeArtifact.
- [Use CodeArtifact with nuget or dotnet](https://docs.aws.amazon.com/codeartifact/latest/ug/nuget-cli.html): Configure the NuGet package manager to consume and publish packages with CodeArtifact.
- [NuGet package name, version, and asset name normalization](https://docs.aws.amazon.com/codeartifact/latest/ug/nuget-name-normalization.html): CodeArtifact normalizes package and asset names and package versions before storing them, which means the names or versions in CodeArtifact may be different than the ones provided when the package or asset was published.
- [NuGet compatibility](https://docs.aws.amazon.com/codeartifact/latest/ug/nuget-compatibility.html): NuGet versions and compatibility in CodeArtifact.


## [Using Python](https://docs.aws.amazon.com/codeartifact/latest/ug/using-python.html)

- [Configure and use pip with CodeArtifact](https://docs.aws.amazon.com/codeartifact/latest/ug/python-configure-pip.html): Use the pip client and the twine client to install and publish packages with CodeArtifact.
- [Configure and use twine with CodeArtifact](https://docs.aws.amazon.com/codeartifact/latest/ug/python-configure-twine.html): twine is a package publishing utility for Python packages.
- [Python package name normalization](https://docs.aws.amazon.com/codeartifact/latest/ug/python-name-normalization.html): CodeArtifact normalizes package names before storing them, which means the package names in CodeArtifact may be different than the name provided when the package was published.
- [Python compatibility](https://docs.aws.amazon.com/codeartifact/latest/ug/python-compatibility.html): CodeArtifact does not support PyPI's XML-RPC or JSON APIs.
- [Requesting Python packages from upstreams and external connections](https://docs.aws.amazon.com/codeartifact/latest/ug/python-upstream-external-connections-request.html): When importing a Python package version from pypi.org, CodeArtifact will import all the assets in that package version.


## [Using Ruby](https://docs.aws.amazon.com/codeartifact/latest/ug/using-ruby.html)

- [Configure and use RubyGems and Bundler](https://docs.aws.amazon.com/codeartifact/latest/ug/configure-use-rubygems-bundler.html): After you create a repository in CodeArtifact, you can use RubyGems (gem) and Bundler (bundle) to install and publish gems.
- [RubyGems command support](https://docs.aws.amazon.com/codeartifact/latest/ug/ruby-command-support.html): CodeArtifact supports the gem install and gem push commands.
- [Bundler compatibility](https://docs.aws.amazon.com/codeartifact/latest/ug/bundler-compatibility.html): Bundler versions and compatibility in CodeArtifact.


## [Using Swift](https://docs.aws.amazon.com/codeartifact/latest/ug/using-swift.html)

- [Configure Swift with CodeArtifact](https://docs.aws.amazon.com/codeartifact/latest/ug/configure-swift.html): To use the Swift Package Manager to publish packages to or consume packages from AWS CodeArtifact, you'll first need to set up credentials to access your CodeArtifact repository.
- [Consuming and publishing Swift packages](https://docs.aws.amazon.com/codeartifact/latest/ug/swift-publish-consume.html)
- [Swift package name and namespace normalization](https://docs.aws.amazon.com/codeartifact/latest/ug/swift-name-normalization.html): CodeArtifact normalizes package names and namespaces before storing them, which means the names in CodeArtifact may be different than the ones provided when the package was published.
- [Swift troubleshooting](https://docs.aws.amazon.com/codeartifact/latest/ug/swift-troubleshooting.html): The following information might help you troubleshoot common issues with Swift and CodeArtifact.


## [Using generic packages](https://docs.aws.amazon.com/codeartifact/latest/ug/using-generic.html)

- [Generic packages overview](https://docs.aws.amazon.com/codeartifact/latest/ug/generic-packages-overview.html): Overview of packages in CodeArtifact, including publishing and version status.
- [Supported commands](https://docs.aws.amazon.com/codeartifact/latest/ug/generic-packages-supported-commands.html): Describes the CodeArtifact commands that work with generic packages.
- [Publishing and consuming generic packages](https://docs.aws.amazon.com/codeartifact/latest/ug/publishing-using-generic-packages.html)


## [Using CodeArtifact with CodeBuild](https://docs.aws.amazon.com/codeartifact/latest/ug/codebuild.html)

- [Using npm packages in CodeBuild](https://docs.aws.amazon.com/codeartifact/latest/ug/using-npm-packages-in-codebuild.html): Use npm packages from CodeBuild with CodeArtifact.
- [Using Python packages in CodeBuild](https://docs.aws.amazon.com/codeartifact/latest/ug/using-python-packages-in-codebuild.html): Use Python packages from CodeBuild with CodeArtifact.
- [Using Maven packages in CodeBuild](https://docs.aws.amazon.com/codeartifact/latest/ug/using-maven-packages-in-codebuild.html): Use Maven packages from CodeBuild with CodeArtifact.
- [Using NuGet packages in CodeBuild](https://docs.aws.amazon.com/codeartifact/latest/ug/using-nuget-packages-in-codebuild.html): Use NuGet packages from CodeBuild with CodeArtifact.
- [Dependency caching](https://docs.aws.amazon.com/codeartifact/latest/ug/dependency-caching.html): You can enable local caching in CodeBuild to reduce the number of dependencies that need to be fetched from CodeArtifact for each build.


## [Monitoring CodeArtifact](https://docs.aws.amazon.com/codeartifact/latest/ug/working-with-service-events.html)

- [Monitoring CodeArtifact events](https://docs.aws.amazon.com/codeartifact/latest/ug/monitoring-events.html): CodeArtifact is integrated with Amazon EventBridge, a service that automates and responds to events, including changes in a CodeArtifact repository.
- [Use an event to start a CodePipeline execution](https://docs.aws.amazon.com/codeartifact/latest/ug/configure-service-events-codepipeline.html): This example demonstrates how to configure an Amazon EventBridge rule so that an AWS CodePipeline execution starts when a package version in a CodeArtifact repository is published, modified, or deleted.
- [Use an event to run a Lambda function](https://docs.aws.amazon.com/codeartifact/latest/ug/configure-service-events-lambda-function.html): This example shows you how to configure an EventBridge rule that starts an AWS Lambda function when a package version in a CodeArtifact repository is published, modified, or deleted.


## [Security](https://docs.aws.amazon.com/codeartifact/latest/ug/security.html)

### [Data protection](https://docs.aws.amazon.com/codeartifact/latest/ug/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in AWS CodeArtifact.

- [Data encryption](https://docs.aws.amazon.com/codeartifact/latest/ug/security-encryption.html): Encryption is an important part of CodeArtifact security.
- [Traffic privacy](https://docs.aws.amazon.com/codeartifact/latest/ug/security-traffic-privacy.html): You can improve the security of your CodeArtifact domains and the assets that they contain by configuring CodeArtifact to use an interface virtual private cloud (VPC) endpoint.

### [Monitoring](https://docs.aws.amazon.com/codeartifact/latest/ug/security-logging-and-monitoring.html)

Lists the items to monitor to maintain the reliability, availability, and performance of your CodeArtifact.

- [Logging CodeArtifact API calls with AWS CloudTrail](https://docs.aws.amazon.com/codeartifact/latest/ug/codeartifact-information-in-cloudtrail.html): CodeArtifact is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in CodeArtifact.
- [Compliance validation](https://docs.aws.amazon.com/codeartifact/latest/ug/codeartifact-compliance-validation.html): Learn which AWS services are in scope of a specific compliance program.
- [Authentication and tokens](https://docs.aws.amazon.com/codeartifact/latest/ug/tokens-authentication.html): Learn how to authenticate with AWS CodeArtifact with tokens.
- [Resilience](https://docs.aws.amazon.com/codeartifact/latest/ug/codeartifact-disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific CodeArtifact features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/codeartifact/latest/ug/infrastructure-security.html): Learn how AWS CodeArtifact isolates service traffic.
- [Dependency substitution attacks](https://docs.aws.amazon.com/codeartifact/latest/ug/dependency-substitution-attacks.html): Learn more about package dependency substitution or confusion attacks and how to prevent them in AWS CodeArtifact.

### [Identity and Access Management](https://docs.aws.amazon.com/codeartifact/latest/ug/security-iam.html)

How to authenticate requests and manage access to your CodeArtifact resources.

- [How AWS CodeArtifact works with IAM](https://docs.aws.amazon.com/codeartifact/latest/ug/security_iam_service-with-iam.html): Before you use IAM to manage access to CodeArtifact, learn what IAM features are available to use with CodeArtifact.
- [Identity-based policy examples](https://docs.aws.amazon.com/codeartifact/latest/ug/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify CodeArtifact resources.
- [Using tags to control access to CodeArtifact resources](https://docs.aws.amazon.com/codeartifact/latest/ug/tag-based-access-control.html): Lists example tag-based access control policies for AWS CodeArtifact.
- [AWS CodeArtifact permissions reference](https://docs.aws.amazon.com/codeartifact/latest/ug/auth-and-access-control-permissions-reference.html): Describes the AWS CodeArtifact API operations and the corresponding actions that you grant permissions to perform.
- [Troubleshooting](https://docs.aws.amazon.com/codeartifact/latest/ug/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with CodeArtifact and IAM.


## [Working with VPC endpoints](https://docs.aws.amazon.com/codeartifact/latest/ug/vpc-endpoints.html)

- [Create VPC endpoints](https://docs.aws.amazon.com/codeartifact/latest/ug/create-vpc-endpoints.html): Create two VPC endpoints to access CodeArtifact repositories using package managers and build tools.
- [Create the Amazon S3 gateway endpoint](https://docs.aws.amazon.com/codeartifact/latest/ug/create-s3-gateway-endpoint.html): Create a gateway endpoint for Amazon S3 to pull packages from CodeArtifact.
- [Use CodeArtifact from a VPC](https://docs.aws.amazon.com/codeartifact/latest/ug/use-codeartifact-from-vpc.html): Override the hostname used by CodeArtifact when you use the AWS CLI or SDK.
- [Create a VPC endpoint policy](https://docs.aws.amazon.com/codeartifact/latest/ug/create-vpc-endoint-policy.html): Use an example VPC endpoint policy to authorize an account to fetch packages from a CodeArtifact repository.

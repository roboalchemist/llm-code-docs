# Source: https://docs.acceldata.io/documentation/user-defined-templates-cli.md

# User Defined Templates CLI



The Acceldata Observability Cloud offers a powerful solution in the form of the User Defined Template (UDT) feature. This feature empowers you to effortlessly create custom code templates and reuse them across multiple policies for different assets. The UDT lifecycle is managed through a user-friendly UI flow, allowing you to create UDTs for various programming languages and Spark SQL expressions with ease. The UI-driven design provides a smooth and convenient experience for verifying and utilizing UDT definitions.

But, for users with heavy UDT usage, concerns may arise with regards to:

- Tracking changes in accordance with their release cycle
- Reviewing code
- Testing scenarios in a fast and efficient manner
- Using external binaries to solve specific use cases

One of the features of the Acceldata ADOC CLI is the ability to create base projects for different programming languages. This means that users can easily set up a project in the language of their choice (such as Java, Scala) with the necessary files and configurations already in place. Additionally, the CLI provides sample and test suites that can be used to test the project and ensure it functions as intended.

**UDT Repo Support** has been created to address these concerns and is divided into two components:

1. UDT CLI Usage
2. End to End Flow



> - Only **GCS** and **S3** are supported for UDT Driven binary storage.> - Only the following Spark deployments support the data plane:>     - **Livy on Kubernetes**>     - **K8s**> > - **Scala** and **Java** are the only languages that are currently supported.






# Source: https://docs.socket.dev/docs/dependency-search.md

# Dependency Search

## Introduction

Socket's Dependency Search is a powerful tool designed to help developers and security teams quickly find and assess the security posture of dependencies used within their projects. This feature leverages advanced search capabilities to provide insights into vulnerabilities, licensing issues, and other critical information about the packages used in your codebase.

### How to Use Dependency Search

#### Step 1: Accessing Dependency Search

* **Navigate to the Dependency Search**: From the Socket dashboard, select the "Dependencies" option in the left-hand menu.

<Image align="center" src="https://files.readme.io/9d7f2974f37b4f36926bebeb82d29ba4043b49043a56466387c0e60dc0d98eee-Screenshot_2025-07-01_at_1.14.13_AM.png" />

#### Step 2: Performing a Search

* **Enter Your Query**: Use the search bar to enter the name of the dependency you want to investigate. You can search by package name of the dependency.
* <Image align="center" src="https://files.readme.io/0658298796b1ec45e7f9f59c387c561518547778f27a3a741c954047f6814dea-Screenshot_2025-07-01_at_1.15.52_AM.png" />

<Image align="center" src="https://files.readme.io/072412ee78aabdab9b3f92f54f0efb80b4567357bd47e4ed3c1b45ead92ae8e7-Screenshot_2025-07-01_at_1.15.36_AM.png" />

3. **View Search Results**: The search results will display a list of dependencies that match your query. Each result includes important information such as the package name, version, transitive or direct, and the repository where you can locate the dependency.

<Image align="center" src="https://files.readme.io/c5f1854e285494acc8c7a44d3f40465df6ad3f32fddcd64158ca44182257fdd1-Screenshot_2025-07-01_at_1.14.27_AM.png" />

#### Step 3: Taking Action

* **Update or Replace**: Based on the security and licensing information, decide whether to update the dependency to a more secure version or replace it with an alternative package.
* **Notify Your Team**: Use the information provided by Dependency Search to inform your team about potential risks and necessary actions. This ensures that everyone is aware of the dependencies' security status and any required updates.

### Best Practices

* **Regular Searches**: Perform regular searches for your dependencies to stay informed about new vulnerabilities and security issues.
* **Monitor Critical Dependencies**: Pay special attention to critical dependencies that are widely used across your projects.
* **Stay Updated**: Always keep your dependencies up to date to benefit from security patches and updates provided by the maintainers.
* **Automate Alerts**: Use Socket's automation features to set up alerts for new vulnerabilities or changes in the security status of your dependencies.

### Conclusion

Socket's Dependency Search is an essential tool for maintaining the security and compliance of your project's dependencies. By leveraging its powerful search and detailed insights, you can proactively manage and mitigate risks associated with third-party packages, ensuring a secure and compliant codebase.

For more detailed information and to start using Dependency Search, visit the [Socket Dependency Search Blog](https://socket.dev/blog/dependency-search).
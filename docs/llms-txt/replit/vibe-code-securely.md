# Source: https://docs.replit.com/tutorials/vibe-code-securely.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.replit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Replit's built-in security features

> Learn about the security features built into Replit.

When you're vibe coding—focusing on creativity and rapid iteration—it's easy to overlook security. Replit has designed the platform to push you towards security best practices by providing robust security features that work automatically.

<iframe src="https://www.youtube.com/embed/ItcUFQVkPFY" title="Security features in Replit" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

Replit provides several security features out of the box that make it easier to build secure applications.

<Steps>
  <Step title="Version control">
    Replit offers native version control with Git integration. Additionally, you can access file history directly in the Workspace:

    * Use the **History** panel to see every keystroke and revert changes
    * Access Git features through the **Git** pane
    * Roll back to checkpoints when using Agent
  </Step>

  <Step title="Google Cloud infrastructure">
    All Replit deployments are backed by Google Cloud Platform (GCP):

    * Deployments run on GCP
    * Object storage uses Google Cloud Storage (GCS)
    * Resource isolation between projects
    * DDoS protection through Google Cloud Armor
  </Step>

  <Step title="Encrypted secrets storage">
    Secrets are encrypted using Google Cloud's secure storage and are safely accessible from your application's code.

    To add a secret:

    1. Go to the **Secrets** pane in your Workspace
    2. Select **Add a new secret**
    3. Enter a key and value
    4. Select **Add secret**

    Keep sensitive information like API keys secure:

    ```javascript  theme={null}
    // Don't do this
    const apiKey = "sk_test_abcdef12345";

    // Do this instead
    const apiKey = process.env.API_KEY;
    ```
  </Step>

  <Step title="Object storage">
    When using Replit's object storage:

    * Files are backed by Google Cloud Storage
    * Only your app can access stored files by default
    * No need to worry about public access control
    * Agent can set up Object Storage with advanced authentication and access controls

    Ask Agent to add secure file storage:

    ```
    Add Object Storage with authentication for user file uploads
    ```
  </Step>

  <Step title="Replit Auth">
    Implement authentication without building it from scratch.

    Benefits of Replit Auth:

    * Handles login securely
    * Manages sessions
    * Reduces authentication implementation errors

    Ask Agent:

    ```
    Help me implement authentication for my application with Replit Auth
    ```
  </Step>

  <Step title="Secure architecture with Agent">
    Agent builds applications with:

    * Proper separation of front-end and back-end
    * Secure back-end communication with databases
    * Front-end that communicates only with your back-end API
  </Step>

  <Step title="Database security with ORMs">
    Agent uses Object-Relational Mapping (ORM) tools when building applications with databases:

    * Protection against SQL injection
    * Schema validation
    * Type safety
    * Managed database connections
  </Step>
</Steps>

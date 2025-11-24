# Source: https://docs.augmentcode.com/cli/custom-commands-examples.md

# Custom Slash Commands Examples

> Ready-to-use examples of custom slash commands for common development workflows.

## Example Commands

Here are some practical examples of custom slash commands you can use in your projects:

<AccordionGroup>
  <Accordion title="Code Review Command">
    ```markdown  theme={null}
    ---
    description: Perform a comprehensive code review
    argument-hint: [file-path]
    ---

    Please perform a comprehensive code review of the specified file or current changes, focusing on:

    1. **Code Quality**: Check for readability, maintainability, and adherence to best practices
    2. **Security**: Look for potential security vulnerabilities
    3. **Performance**: Identify potential performance issues
    4. **Testing**: Suggest areas that need test coverage
    5. **Documentation**: Check if code is properly documented

    $ARGUMENTS
    ```
  </Accordion>

  <Accordion title="Bug Fix Template">
    ```markdown  theme={null}
    ---
    description: Generate a structured bug fix approach
    argument-hint: [bug-description]
    ---

    Help me fix this bug: $ARGUMENTS

    Please provide:
    1. Root cause analysis
    2. Step-by-step fix approach
    3. Testing strategy
    4. Prevention measures for similar issues
    ```
  </Accordion>

  <Accordion title="Feature Implementation Guide">
    ```markdown  theme={null}
    ---
    description: Create implementation plan for new features
    argument-hint: [feature-description]
    ---

    Create a detailed implementation plan for: $ARGUMENTS

    Include:
    - Technical requirements
    - Architecture considerations
    - Implementation steps
    - Testing approach
    - Documentation needs
    ```
  </Accordion>

  <Accordion title="Security Review Command">
    ```markdown  theme={null}
    ---
    description: Perform security analysis on code
    argument-hint: [file-path]
    ---

    Perform a security review of: $ARGUMENTS

    Focus on:
    1. **Input validation** and sanitization
    2. **Authentication** and authorization checks
    3. **Data exposure** and privacy concerns
    4. **Injection vulnerabilities** (SQL, XSS, etc.)
    5. **Cryptographic** implementations
    6. **Dependencies** with known vulnerabilities

    Provide specific recommendations for any issues found.
    ```
  </Accordion>

  <Accordion title="Performance Optimization">
    ```markdown  theme={null}
    ---
    description: Analyze and optimize code performance
    argument-hint: [file-path]
    ---

    Analyze the performance of: $ARGUMENTS

    Please examine:
    1. **Algorithm complexity** and efficiency
    2. **Memory usage** patterns
    3. **Database queries** and optimization opportunities
    4. **Caching** strategies
    5. **Network requests** and bundling
    6. **Rendering performance** (for frontend code)

    Suggest specific optimizations with expected impact.
    ```
  </Accordion>

  <Accordion title="Documentation Generator">
    ```markdown  theme={null}
    ---
    description: Generate comprehensive documentation
    argument-hint: [file-path]
    ---

    Generate documentation for: $ARGUMENTS

    Include:
    1. **Overview** and purpose
    2. **API reference** with parameters and return values
    3. **Usage examples** with code snippets
    4. **Configuration options** if applicable
    5. **Error handling** and troubleshooting
    6. **Dependencies** and requirements

    Format as clear, structured markdown.
    ```
  </Accordion>

  <Accordion title="Test Generation Command">
    ```markdown  theme={null}
    ---
    description: Generate comprehensive test cases
    argument-hint: [file-path]
    ---

    Generate test cases for: $ARGUMENTS

    Create tests covering:
    1. **Happy path** scenarios
    2. **Edge cases** and boundary conditions
    3. **Error handling** and exceptions
    4. **Integration points** with other components
    5. **Performance** considerations
    6. **Security** edge cases

    Use appropriate testing framework conventions and include setup/teardown as needed.
    ```
  </Accordion>
</AccordionGroup>

## How to Add Commands to Your Project

To use these custom slash commands in your project, you need to save them in the `.augment/commands/` directory:

### Step 1: Create the Commands Directory

First, create the `.augment/commands/` directory in your project root if it doesn't exist:

```bash  theme={null}
mkdir -p .augment/commands
```

### Step 2: Save Command Files

Save each command as a separate `.md` file in the `.augment/commands/` directory. For example:

```bash  theme={null}
# Save the code review command
cat > .augment/commands/code-review.md << 'EOF'
---
description: Perform a comprehensive code review
argument-hint: [file-path]
---

Please perform a comprehensive code review of the specified file or current changes, focusing on:

1. **Code Quality**: Check for readability, maintainability, and adherence to best practices
2. **Security**: Look for potential security vulnerabilities
3. **Performance**: Identify potential performance issues
4. **Testing**: Suggest areas that need test coverage
5. **Documentation**: Check if code is properly documented

$ARGUMENTS
EOF
```

### Step 3: Use Your Commands

Once saved, your custom commands become available as slash commands in Augment:

```
/code-review src/components/Button.tsx
/bug-fix "Login form validation not working"
/security-review auth/middleware.js
```

### Directory Structure

Your project structure should look like this:

```
your-project/
├── .augment/
│   └── commands/
│       ├── code-review.md
│       ├── bug-fix.md
│       ├── security-review.md
│       └── performance-optimization.md
├── src/
└── package.json
```

## Usage Tips

* **Save these templates** in your `.augment/commands/` directory
* **Customize the prompts** to match your team's coding standards and practices
* **Add project-specific context** to make the commands more effective
* **Combine commands** by referencing outputs from one command in another
* **Use meaningful filenames** like `code-review.md`, `bug-fix.md`, etc.
* **Version control your commands** by committing the `.augment/commands/` directory to your repository

## Creating Your Own Examples

When creating custom commands, consider these patterns:

1. **Start with a clear description** in the frontmatter
2. **Use argument hints** to guide users on expected inputs
3. **Structure your prompts** with numbered lists or bullet points
4. **Include specific instructions** for the type of analysis or output you want
5. **Reference the `$ARGUMENTS` variable** where user input should be inserted

## See Also

* [Custom Slash Commands](/cli/custom-commands) - Learn how to create and manage custom commands
* [CLI Reference for Custom Commands](/cli/reference#custom-commands) - Complete command-line reference for custom commands

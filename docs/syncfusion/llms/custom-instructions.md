# Source: https://docs.syncfusion.com/code-studio/reference/configure-properties/custom-instructions.md

# Custom Instruction 
 
**Custom Instruction** in Code Studio allow you to provide specific instructions that guide how the AI assistant behaves when working with your code. Instead of the AI making assumptions about your coding standards, architecture patterns, or project-specific requirements, you can explicitly define guidelines that ensure consistent, contextually appropriate responses.
 
## What is Custom Instruction?

- **Define guidelines and rules** that automatically influence how AI generates code and handles development tasks.  
- **Reduce repeated context** by specifying instructions in a Markdown file instead of every chat prompt.  
- **Apply instructions automatically** to all chat requests or limit them to specific files.  
- **Attach instructions manually** to a specific chat prompt when needed.

## Types of Instruction Files

There are two types of instruction files:

### 1. Repository-wise Instructions
- Apply rules to the entire repository.  
- Once configured, the AI assistant automatically follows these guidelines for **all chats** and **code contexts** in the repo.
- use this when you want one consistent set of standards across the whole project.  
- **File Type:** `codestudio-instructions.md`  
- **Location:** `.codestudio/codestudio-instructions.md` (at the repository root)

### 2. Path-specific Instructions
- Apply rules only when certain files or folders are in context.  
- Useful when different parts of your project (e.g., frontend vs backend) need different coding standards.  
- **File Type:** `*.instructions.md`  
- **Location:** `.codestudio/instructions/`  
  - Example: `.codestudio/instructions/python.instructions.md`  
  - Example: `.codestudio/instructions/frontend.instructions.md`

## Purpose

- Provide **durable, repo-specific** guidance the assistant follows automatically.  
- Cut repeated **chat instructions** by setting defaults for behavior, style, tools, and project context.  
- Support **path-specific** rules so guidance matches the code youâre working on.

## Enabling Custom Instruction Files

**Step 1:** Open **settings** at the bottom left in Code Studio.  

<img src="../reference-images/instruction_option.png" alt="instruction_option" >

**Step 2:** Select **Code Studio Settings** in the pop-up options.

<img src="../reference-images/instruction_code_settings.png" alt="instruction_code_settings" >

**Step 3:** Click **Instruction** in the settings options.

<img src="../reference-images/instruction_repo.png" alt="instruction_repo" >

You will see three options:  
- **Option 1: Repository-wise instructions** 
    - Use this option when you want **one set of rules** for the entire repository.
    - Switch **ON** the repo path to enable the file.

    <img src="../reference-images/instruction_repo_path.png" alt="instruction_path" >

    - Once enabled, the AI assistant will automatically apply these instructions to **all chats and code contexts** in your project.

- **Option 2: Path-specific instructions**
    - Use this option when you want **different rules** for different file types or folders.
    - Switch **ON** the repo path to enable the file.

    <img src="../reference-images/instruction_specific_path.png" alt="instruction_specific_path" >

- **Option 3: Add New Path-specific Location**
    - Click the **Add New Location** in the instruction settings page.
    
    <img src="../reference-images/instruction_new_location.png" alt="instruction_new_location" >

    - You can add a new custom file path and switch **ON** the path specific settings.

    <img src="../reference-images/instruction_path_add.png" alt="instruction_path_add" >

    - Use this option when you want to create a **new instruction** file for a **custom path.**

## How to Configure Repository-wise Instruction File

**Step 1:** Open the `codestudio-instructions.md` file.
- There are **two** options to open the codestudio-instructions.md file. You can choose any one of them based on your preference.
    - **Option 1:**
        - Open the chat view.

        <img src="../reference-images/instruction_chat.png" alt="instruction_chat">

        -  Clcik the **Generate agent instructions** to open the file.
    - **Option 2:**
        - Open the chat view. Click the settings option at the top.

        <img src="../reference-images/instruction_chat_option.png" alt="instruction_chat_option" >

        - Select the âGenerate agent instructionsâ in the pop up.

**Step 2:** Now Code Studio will automatically create and open `codestudio-instructions.md`.  

<img src="../reference-images/instruction_repo_file.png" alt="instruction_repo_file">

**Step 3:** Customize the file to fit your project needs.  
**Step 4:** Open chat view and send a message. Now the instruction file will be **referenced** automatically.

<img src="../reference-images/instruction_repo_refer.png" alt="instruction_repo_refer">


## How to Configure Path-specific Instruction File

**Step 1:** Click *Settings* from the top right and clcik **chat instructions**

<img src="../reference-images/instruction_path_chat.png" alt="instruction_path_chat">

**Step 2:** Click **New Instruction File**.

<img src="../reference-images/instruction_path_new_chat.png" alt="instruction_path_new_chat">

**Step 3:** Choose where to save your file
- There are two options to save your instruction. You can choose any one of them based on your preference.

    - **Option 1: Workspace:** 
        - Save to `.codestudio/instructions/` folder in your project.
        - Use when: Sharing with your **team** while committing your source.
        - Location: `YOUR-PROJECT/.codestudio/instructions instruction-name.instructions.md`.
    - **Option 2: User Profile:**
        - Saves to: Your user profile folder.
        - Use when: Using across multiple projects.
        - Benefit: Available in all workspaces.

        <img src="../reference-images/instruction_path_workspace.png" alt="instruction_path_workspace">

    - Select your **preferred location** and click to Continue.               

**Step 4:** Name your instruction file
- For example, here the instruction file name entered is `test.instructions.md`.  

<img src="../reference-images/instruction_path_name.png" alt="instruction_path_name">

**Step 5:** The new file will be open automatically for editing.

<img src="../reference-images/instruction_path_test.png" alt="instruction_path_test">

**Step 6:** Target the path-specific instructions file
- For example, here target the `test.instructions.md` file.

- There are **two** options to target your path specific instruction. You can choose any one of them based on your preference.

### Option 1: Global Path Targeting
- **Definition:** `applyTo: '**'`  
- Applies rules **globally** to all files in the repository.  
- Best when you want rules to apply across every file types `(e.g.,.ts, .scss, .js, .html).`

- Steps to target the global path:
    - Step 1: Use path Like `'**'`

    <img src="../reference-images/instruction_global.png" alt="instruction_global" >

    - Step 2: Add instructions in the test-instructions.md.

    <img src="../reference-images/instruction_global_test.png" alt="instruction_global_test" >

    - Step 3: Open chat and send message your instruction will come in the **used reference.**

    <img src="../reference-images/instruction_global_result.png" alt="instruction_global_result" >

### Option 2: Pattern-specific Targeting
- **Definition:** `applyTo: **/*.scss` or other patterns. for example `(**/*.ts, **/*.css)` 
- Applies rules only to files matching the **given pattern.**  
- Best for adding rules to certain file types or directories.

- Steps to target the pattern specific path
    - Step 1: Use any specific path like `â**/*.scssâ.`

    <img src="../reference-images/instruction_path_apply.png" alt="instruction_path_apply" >

    - Step 2: Add instructions in the test-instructions.md.

    <img src="../reference-images/instruction_path_rules.png" alt="instruction_path_rules" >

    - Step 3: Give the file in the **chat context** which you want to edit.

    <img src="../reference-images/instruction_path_context.png" alt="instruction_path_context" >

    - Step 4: Open chat and send message your instruction file will come in the **used reference.**

    <img src="../reference-images/instruction_path_result.png" alt="instruction_path_result" >
    
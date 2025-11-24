# Source: https://docs.augmentcode.com/cli/interactive/prompt-enhancer.md

# Prompt Enhancer

> Use Ctrl+P to enhance your prompts with relevant context, structure, and conventions from your codebase.

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

## About the Prompt Enhancer

The Auggie CLI prompt enhancer is a powerful feature that helps you craft better prompts by automatically adding relevant context, structure, and conventions from your codebase. Instead of writing detailed prompts from scratch, you can start with a simple idea and let the prompt enhancer transform it into a comprehensive, well-structured prompt.

## Activating the Prompt Enhancer

To use the prompt enhancer in Auggie's interactive mode:

1. **Start typing your prompt** in the input box
2. **Press <Keyboard shortcut="Ctrl + P" />** to activate the prompt enhancer
3. **Wait for enhancement** - Auggie will process your prompt and replace it with an enhanced version
4. **Review and edit** the enhanced prompt if needed
5. **Submit your enhanced prompt** by pressing Enter

<Note>The prompt enhancer is only available when you have text entered at the command prompt. The <Keyboard shortcut="Ctrl + P" /> shortcut will only work in interactive mode.</Note>

## How It Works

When you press <Keyboard shortcut="Ctrl + P" />, the prompt enhancer:

1. **Captures your current input** and saves it to history
2. **Switches to Enhancement mode** - you'll see the mode indicator change and input will be temporarily disabled
3. **Sends your prompt** to the enhancement service using your current workspace context
4. **Processes the response** and extracts the enhanced prompt
5. **Replaces your input** with the enhanced version and returns to Normal mode

During enhancement, you'll see:

* The mode indicator shows "Enhancing your prompt, press Esc to cancel"
* Input is disabled to prevent conflicts
* A visual indication that processing is in progress

## Enhancement Process

The prompt enhancer uses your workspace context to improve your prompts by:

* **Adding relevant file references** from your current project
* **Including coding conventions** and patterns from your codebase
* **Structuring the prompt** for better clarity and specificity
* **Adding context** about your project's architecture and dependencies
* **Suggesting specific examples** based on existing code patterns

## Canceling Enhancement

You can cancel the prompt enhancement process at any time:

* **Press <Keyboard shortcut="Esc" />** to cancel enhancement and restore your original input
* **Press <Keyboard shortcut="Ctrl + C" />** to cancel enhancement and restore your original input

When canceled, you'll see a brief notification and your original prompt will be restored.

## Error Handling

If the prompt enhancement fails:

* Your original input will be restored
* An error notification will appear briefly (\~3 seconds)
* You can try enhancing again or proceed with your original prompt

Common reasons for enhancement failure:

* Network connectivity issues
* Service temporarily unavailable
* Input too short or unclear for enhancement

## Examples

### Before Enhancement

```
fix the login bug
```

### After Enhancement (Example)

```
Fix the authentication bug in the login flow. Please:

1. Review the current login implementation in `src/auth/login.ts`
2. Check for issues with token validation and session management
3. Examine error handling in the authentication middleware
4. Look at recent changes to the user authentication flow
5. Test the fix with both valid and invalid credentials
6. Ensure the fix follows our existing error handling patterns

Context: This appears to be related to the recent changes in the authentication system. Please maintain consistency with our existing auth patterns and ensure proper error messages are returned to the user.
```

## Integration with Other Features

The prompt enhancer works seamlessly with other Auggie CLI features:

* **History Navigation**: Enhanced prompts are added to your command history
* **Multi-line Input**: Works with both single-line and multi-line prompts
* **Conversation Context**: Uses your current conversation history for better enhancement
* **Workspace Awareness**: Leverages your current workspace and file context

## Tips for Best Results

1. **Start with clear intent** - Even simple prompts like "add tests" or "refactor this" work well
2. **Be specific about scope** - Mention specific files or components when relevant
3. **Use domain language** - Technical terms related to your project help the enhancer understand context
4. **Review enhanced prompts** - The enhancer provides a starting point; feel free to edit further
5. **Iterate if needed** - You can enhance the same prompt multiple times for different approaches

## Troubleshooting

**Ctrl+P doesn't work:**

* Ensure you have text in the input box
* Make sure you're in Normal mode (not in a menu or other mode)
* Check that you're using the correct key combination for your terminal

**Enhancement takes too long:**

* Press Esc to cancel and try again
* Check your network connection
* Try with a shorter or simpler prompt

**Enhanced prompt isn't helpful:**

* Edit the enhanced prompt manually
* Try starting with a more specific initial prompt
* Consider the context - the enhancer works best with workspace-relevant requests

## Related Features

* [Task Management](/cli/interactive/task-management) - Break down enhanced prompts into manageable tasks
* [Keyboard Shortcuts](/cli/interactive#shortcuts) - Learn other useful CLI shortcuts
* [Slash Commands](/cli/interactive#slash-commands) - Discover other interactive commands

# Source: https://docs.bito.ai/ai-code-reviews-in-ide/ai-chat-in-bito/keyboard-shortcuts.md

# Keyboard shortcuts

Bito UI in Visual Studio Code and JetBrains IDEs is entirely keyboard accessible. You can navigate Bito UI with standard keyboard actions such as TAB, SHIFT+TAB, ENTER, and ESC keys. Additionally, you can use the following shortcuts for quick operations.

The following video demonstrates important keyboard shortcuts.

{% embed url="<https://www.loom.com/share/a578f79e82414afb9c4fc7997cbc44f2>" %}

### General

| Command                                                                                                                                                     | Shortcuts                                                                                                                                                                                                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Open Bito Panel:** Toggle Bito Panel on and off in the JetBrains IDE. In the Visual Studio Code, the shortcut opens the Bito panel if not already opened. | SHIFT + CTRL + O                                                                                                                                                                                                                                                                                                                                      |
| Puts cursor in the chatbox when Bito panel is in focus.                                                                                                     | SPACEBAR (Or start typing your question directly)                                                                                                                                                                                                                                                                                                     |
| **Execute** the chat command                                                                                                                                | ENTER                                                                                                                                                                                                                                                                                                                                                 |
| Add a **new line** in the chatbox                                                                                                                           | CTRL + ENTER or SHIFT + ENTER                                                                                                                                                                                                                                                                                                                         |
| **Modify** the **most recently executed** prompt. This copies the last prompt in the chatbox for any edits.                                                 | CTRL + M                                                                                                                                                                                                                                                                                                                                              |
| Expands and Collapse the "Shortcut" panel                                                                                                                   | <p>WINDOWS: CTRL + <span data-gb-custom-inline data-tag="emoji" data-code="2b06">⬆️</span> / <span data-gb-custom-inline data-tag="emoji" data-code="2b07">⬇️</span>  <br>MAC: CTRL + SHIFT+  <span data-gb-custom-inline data-tag="emoji" data-code="2b06">⬆️</span> / <span data-gb-custom-inline data-tag="emoji" data-code="2b07">⬇️</span>  </p> |

### Question & Answers

The following keyboard shortcuts work after the Q/A block is selected.&#x20;

| Command                                                                                                                 | Keyboard Shortcut                                                                                                                                                                                                                                                                                                                                    |
| ----------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Navigate between the Questions/Answers block. </p><p>Note: You must select the Q/A container with TAB/SHIFT+TAB.</p> | :arrow\_up: / :arrow\_down:                                                                                                                                                                                                                                                                                                                          |
| Copy the answer to the clipboard.                                                                                       | CTRL + C                                                                                                                                                                                                                                                                                                                                             |
| Insert the answer in the code editor                                                                                    | CTRL + I                                                                                                                                                                                                                                                                                                                                             |
| Toggle the diff view (when Diff View is applicable)                                                                     | CTRL + D                                                                                                                                                                                                                                                                                                                                             |
| Expand/Collapse the code block in the question.                                                                         | <p>WINDOWS: CTRL + <span data-gb-custom-inline data-tag="emoji" data-code="2b06">⬆️</span> / <span data-gb-custom-inline data-tag="emoji" data-code="2b07">⬇️</span>  <br>MAC: CTRL + SHIFT+  <span data-gb-custom-inline data-tag="emoji" data-code="2b06">⬆️</span> / <span data-gb-custom-inline data-tag="emoji" data-code="2b07">⬇️</span> </p> |
| Regenerate the answer                                                                                                   | CTRL + L                                                                                                                                                                                                                                                                                                                                             |
| Modify the prompt for the selected Q\&A. Bito copies the prompt in the chatbox that you can modify as needed.           | CTRL + U                                                                                                                                                                                                                                                                                                                                             |

### Change Default Keyboard Shortcuts

Bito has carefully selected the keyboard shortcuts after thorough testing. However, it's possible that Bito selected key combination may conflict with IDE or other extensions shortcut. You can change the Bito default shortcut keys to avoid such conflicts.&#x20;

#### Visual Studio Code Editor

1. To Open the Keyboards Shortcuts editor in VS Code, navigate to the menu under **File** > **Preferences** > **Keyboard Shortcuts**. (**Code** > **Preferences** > **Keyboard Shortcuts** **on macOS**)

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FaMvFa1brpPpOtGrizNN9%2Fimage.png?alt=media&#x26;token=37f47323-0c58-4285-8930-ff74fcc259c1" alt=""><figcaption></figcaption></figure>

2. Search for default available commands, keybindings, or Bito extension-specific commands in VSCode keyboard shortcut editor.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FbEpQlRxPM7Zfe8undFaD%2Fimage.png?alt=media&#x26;token=cf8fd721-6da2-4075-b741-7044b01ec691" alt=""><figcaption></figcaption></figure>

3. Finding a conflict in Key binding → Search for the key and take necessary action, e.g., **Remove** or **Reset.**

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FssX3ehsh7Eyr7GDKhAMx%2Fimage.png?alt=media&#x26;token=d9267a20-0456-47af-800a-69fd3cb1b762" alt=""><figcaption></figcaption></figure>

4. **Add** a new key binding or map the existing Bito extension command.\
   Provide the necessary information (**Command ID**) to add the new key binding.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FeuPp23D6Qnwe36vXIXzg%2Fimage.png?alt=media&#x26;token=ee3a223e-8a71-4734-b935-1f6893655bd5" alt=""><figcaption></figcaption></figure>

#### JetBrains&#x20;

JetBrains Document: <https://www.jetbrains.com/help/idea/configuring-keyboard-and-mouse-shortcuts.html>

1. **File > settings > keymaps > configure keymaps**

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FSghgMvL6zl2sZThE825G%2Fimage.png?alt=media&#x26;token=9168b5ac-20be-49e0-8cdb-13e31db2232a" alt=""><figcaption></figcaption></figure>

2. Bito extension shortcuts can be **overwritten** by going into the\
   File > Settings > Keymaps > configure keymaps > to the action you want to assign.  It will also overwrite the Bito shortcut if there are conflicts.
3. Bito extension keyboard shortcuts can be **changed** from the IntelliJ settings.\
   File > Settings > Keymaps > configure keymaps > plugins > Bito > action you want to change by right click.
4. Bito extension Keyboard shortcuts can be **deleted** from the IntelliJ settings.\
   File > Settings > Keymaps > configure keymaps > plugins > Bito > action you want to delete by right click.

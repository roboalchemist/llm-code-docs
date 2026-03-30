# Source: https://docs.tabnine.com/main/getting-started/code-completion.md

# Code Completions

{% hint style="info" %}
**This feature is available in the following IDEs:**

VS Code, JetBrains IDEs, Visual Studio 2022 and Eclipse
{% endhint %}

As you code in your IDE, you’ll get AI code suggestions based on your current context. The code completions adapt to your code as you type, and can offer on-the-fly code completions, full-function completions, or even natural language comments to code.

Tabnine’s code completions can help save significant time and effort when you’re writing or revising code. For example, by writing lines of code for you or by providing exact syntax, Tabnine saves you the time and effort of looking it up when you can’t remember something.

### Getting started with code completions <a href="#getting-started-with-code-completions" id="getting-started-with-code-completions"></a>

#### **Get Tabnine’s code suggestions**

As you code, you’ll see Tabnine’s code suggestions inline in gray (in addition to the IDE’s pop-up suggestions):

![](https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-9846414a9ad438703906ab6f2025465f55f0d175%2FGetting%20started_gray.png?alt=media)

#### **Accept a code suggestion**

Hit Tab to accept a code suggestion:

![](https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-a4996b658b19c619c0b8866072c3ed0c881c652a%2FGetting%20the%20most%20of%20cc.gif?alt=media)

#### Accept part of a code completion

In some IDEs (VS Code and JetBrains), you can accept just part of a code completion:

* Line by line (VS Code and JetBrains)
* Word by word (VS Code)

{% hint style="info" %}
To set the key shortcut for accepting part of a code completion:

**JetBrains**\
Go to **Settings... > Keymap > Plugins > Tabnine > Accept Line**

**VS Code**\
Go to **Command Palette ... > Preferences: Open Keyboard Shortcuts > Accept Next Line (or Word) Of Inline Suggestion**
{% endhint %}

This is especially useful for code multiline code completions when you need only the first part of the completion.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-2f542896fde48e9e030e25f32ed669241ab82cd0%2FCompletions%20line%20by%20line%20-%20JB%20Edited.gif?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Tips**

1. Use descriptive functions and variable names for accurate predictions.
2. If the current suggestion isn’t what you need, try typing a few more characters to use slightly different functions or variable names.
   {% endhint %}

### Types of code completions provided by Tabnine <a href="#types-of-code-completions-provided-by-tabnine" id="types-of-code-completions-provided-by-tabnine"></a>

#### Whole-line suggestions

As you code, you’ll get code suggestions based on your current context, which adapts with every additional character you type. This is the most common type of code completion, suggesting code until the end of the current line.

**Tip:** Use descriptive functions and variable names for accurate predictions.

![Whole-line suggestion (1)](https://2500895905-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F03uIXF1SrI5fdiuQqdFr%2Fuploads%2FbqEcHiBFiuU7mUZyWVff%2F3.png?alt=media\&token=87e1657a-0221-4146-8513-3164986ef8c6)

![Whole-line suggestion (2)](https://2500895905-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F03uIXF1SrI5fdiuQqdFr%2Fuploads%2F4G0oNiiRVyhiXL9zdYyK%2F4.png?alt=media\&token=c7fd3eb6-a5d4-491e-a365-411b6ac706d0)

#### Full-function suggestions

When you get to a new line right after a function declaration, you’ll receive a suggestion for a full-function implementation. Again, we recommend using descriptive functions and variable names for accurate predictions.

If the full function isn’t what you expected, try using slightly different names:

![Full-function suggestion (1)](https://2500895905-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F03uIXF1SrI5fdiuQqdFr%2Fuploads%2FUyRlTF1YbM5DLUCYReGx%2F5.png?alt=media\&token=905ba41c-0f24-4acb-8a77-74b161a6990a)

![Full-function suggestion (2)](https://2500895905-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F03uIXF1SrI5fdiuQqdFr%2Fuploads%2FsFCVlem97vjU8Y0ZsFpO%2F6.png?alt=media\&token=eb7b636d-8cdb-4290-903b-9e33938147a9)

**Comment-to-code completions**

This type of completion allows you to explicitly declare what you want as a comment in natural language. On the line after the comment, Tabnine will suggest code that performs this task.

If the code isn’t what you were expecting, try using slightly different instructions:

![Natural language to code (1)](https://2500895905-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F03uIXF1SrI5fdiuQqdFr%2Fuploads%2FRy11PzaGTfbIun4WxHWd%2F7.png?alt=media\&token=0d3d1e19-bc9f-427b-af6c-9f9d2b59cbe2)

![Natural language to code (2)](https://2500895905-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F03uIXF1SrI5fdiuQqdFr%2Fuploads%2FUx1Ye647KNJH1KDnOMh7%2F8.png?alt=media\&token=7e893981-8437-4edc-acc0-dd16e8489567)

# Source: https://docs.tabnine.com/main/getting-started/tabnine-chat/tabnines-prompting-guide.md

# Tabnine's Prompting Guide

* [Be Specific and Clear](#be-specific-and-clear-1)
  * You must be very specific and clear when prompting an LLM
* [Define the Context](#define-the-context-1)
  * Defining context is critical when prompting Tabnine Chat.
* [Start a fresh conversation as appropriate](#start-a-fresh-convo-when-appropriate)
  * Starting a fresh conversation helps keep Tabnine Chat focused on the correct context when having a long or detailed conversation.
* [Include Necessary Details](#include-necessary-details-1)
  * It is often helpful to provide the LLM with the necessary details to get quality output.
* [Ask for examples](#ask-for-examples-1)
  * Tabnine Chat can be used to ask for examples of the desired output.
* [Be Concise, *But* Complete](#be-concise-but-complete-1)
  * LLMs perform best when prompts are concise but complete.
  * Use examples of expected output
  * Providing Tabnine Chat with examples of expected output will improve the generated response.

***

Working with LLM-based products requires expertise. Models are becoming increasingly better in understanding and following instructions, even when the instructions are ambiguous. However, models are often sensitive to exact phrasing, and minor changes to the prompt and context can yield significantly different results.

The goal of this guide is to provide high-level guidance for prompting Tabnine Chat. Different backend models will have slightly different sensitivities and would benefit from using specific phrases or forms. However, the guidance in this document should be practical and beneficial across all models.

## Be Specific and Clear

### Ask for a detailed explanation with examples

Here is the referenced function in the text editor:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-a2ca7d528f7804692c4f21bdc886d2092a5c3ca4%2F2.1celsiusFunction.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

Less effective prompt: *Explain this function:*

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-cc53f70159dbfb929a1aad2a4f77fad3a3181fed%2F1.1printCelsiusResponse1.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

More effective prompt: *Explain this function step by step, including an example:*

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea60291f9e7e9ab3643ec8ddaee6407c74989e3a%2F1.1printCelsiusResponse2.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

### Ask for alternative implementations as part of an explanation

Here, we ask Tabnine to *Explain this function in a detailed and precise manner, including alternative implementations*. Having the prompt contains the phrase "detailed and precise manner" often helps Tabnine produce a more focused response.

Here is the referenced function in the text editor:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-a7ec72df2098b8fb797d6a285aad1d127c49ed57%2F1.2findMaxFunction.png?alt=media" alt="" width="528"><figcaption></figcaption></figure>

Part one of the response, using the prompt *Explain this function in a detailed and precise manner, including alternative implementations:*

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-95ca5f909a79503c019fde883752c56e286be8de%2F1.2alternativeImplementationsResponse1.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

Part two of the response:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-7ec2e1c2ab41129674d6334bb4a2123e329c3db1%2F1.2alternativeImplementationsResponse2.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

## Define the Context

General rule: Provide context about the task, the project, or the specific issue you are dealing with.

### 1. Refer to the relevant entity or select it in the editor

Here is the referenced function in the text editor:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-a2ca7d528f7804692c4f21bdc886d2092a5c3ca4%2F2.1celsiusFunction.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

As an alternative to mentioning the function name in the prompt, you can also select the code in the editor or use the CodeLens `ask` option just above the code. Selecting the code in the current open file provides Tabnine Chat with explicit context. If you'd like to perform operations on specific code, be sure to select the code in the IDE before you ask Chat to operate it.

Less effective: prompt *Improve this code:*

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-29ebe0dd94fd0c56ab3cdf5a9c732fffb8ae40cf%2F2.1refactorResponse1.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

More effective: with the relevant code context made explicit as described above, prompt *Refactor the function printCelsius to have the formula just once:*

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-e87716538a606b0bd70279b36023b14e65adcca2%2F2.1refactorResponse2.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

### 2. Using (or not using) workspace context

Using workspace context is a form of [personalization](https://docs.tabnine.com/main/welcome/readme/personalization#what-is-personalization-and-why-does-it-matter) that Tabnine offers to improve the quality of responses from an LLM that was not trained on your existing code base. If workspace context is enabled by your team admin, it is on by default. The toggle to control whether it is on or off is in the lower right corner of the Tabnine Chat window.

Here is the workspace context selector with the toggle switched off:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-0036de794eee08769934cc9ae3907d796c0972b8%2F2.2workspaceIndicator.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

Using the same reference code in example 1 above, here is the response to the prompt *Modify this code to convert from Celsius to Fahrenheit* with workspace context on:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d1c44378c8f4f0fe065511265392db3db37eba07%2F2.2contextOnResponse.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-0ca1ea9ce38cd3cb375084b0c9efc3e88735f976%2F2.2localContextOn.png?alt=media" alt="" width="422"><figcaption></figcaption></figure>

Here is the response to the same prompt with the workspace context turned off:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-fba4de5f0432035b3d2c9774f5161459c308951c%2F2.2contextOffResponse.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-0789e02dc6de836cfed0fc4bdb7f219281ffddbb%2F2.2localContextOff.png?alt=media" alt="" width="419"><figcaption></figcaption></figure>

### 3. Using Mentions to refer to a specific code element outside of the currently opened files

It is not always best to add more context (such as by opening a large number of files in the workspace). Only the most recently touched 2 files in the text editor will be loaded into the context window. In cases where you do not want to open additional files, you can use [Mentions](https://docs.tabnine.com/main/welcome/readme/personalization#mentions) to reference specific files, methods or functions elsewhere in your local workspace as part of your prompt.

## Start a Fresh Convo When Appropriate

Tabnine uses previous chat messages as context. When you move between tasks, use the "New Conversation" button just above the chat text entry to clear the existing conversation's context:

![](https://docs.tabnine.com/~gitbook/image?url=https%3A%2F%2F3436682446-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FY2qxVf5VTm3fmwP4B4Gx%252Fuploads%252FQzQQMETqg49PkY7q3N04%252F3.1startNewConversationGreyedOut.png%3Falt%3Dmedia%26token%3D4dd9273c-1d00-4b2a-adcc-7dc65502be9b\&width=768\&dpr=4\&quality=100\&sign=6f77ae9d\&sv=2)

The "New Conversation" option is not available when there is no current chat context.

![](https://docs.tabnine.com/~gitbook/image?url=https%3A%2F%2F3436682446-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FY2qxVf5VTm3fmwP4B4Gx%252Fuploads%252FJByEyZBVYuzR9G4HOoiH%252F3.1newConversation.png%3Falt%3Dmedia%26token%3D43d2ef4b-75e6-47ea-b8d9-1d69bea01c2a\&width=768\&dpr=4\&quality=100\&sign=56b1441f\&sv=2)

The "New Conversation" option is available when there is current chat context.

You can also start a new chat from the chat menu at the top of the chat window:

![](https://docs.tabnine.com/~gitbook/image?url=https%3A%2F%2F3436682446-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FY2qxVf5VTm3fmwP4B4Gx%252Fuploads%252FHbnsEYHxOU3PcQX3j1pi%252F3.1newChatFromChatMenu.png%3Falt%3Dmedia%26token%3Dabaa202f-7362-4899-b532-76e5aa3773ca\&width=768\&dpr=4\&quality=100\&sign=24654dc8\&sv=2)

## Include Necessary Details

General Rule: Include any specific requirements, constraints, or desired outcomes.

### 1. Specifying input and output types <a href="#id-1.-specifying-input-and-output-types" id="id-1.-specifying-input-and-output-types"></a>

Here is the referenced code:

![](https://docs.tabnine.com/~gitbook/image?url=https%3A%2F%2F3436682446-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FY2qxVf5VTm3fmwP4B4Gx%252Fuploads%252FHMOvg15tLbkuqa9eFLd2%252F4.1referenceFunction.png%3Falt%3Dmedia%26token%3D1cda8ba3-451f-40f6-8134-ab3f4bda2cc0\&width=768\&dpr=4\&quality=100\&sign=6af6a85b\&sv=2)

Less effective prompt: *Write a function to convert from Celsius to Fahrenheit*

![](https://docs.tabnine.com/~gitbook/image?url=https%3A%2F%2F3436682446-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FY2qxVf5VTm3fmwP4B4Gx%252Fuploads%252FCQ3DbJjxxhr34inOsy5D%252F4.1response1.png%3Falt%3Dmedia%26token%3De5cb7eaf-3197-4385-9f40-a848f7d94ca2\&width=768\&dpr=4\&quality=100\&sign=2ed913ce\&sv=2)

More effective prompt: *Write a function to convert from Celsius to Fahrenheit, the function should take an integer and return an integer*

![](https://docs.tabnine.com/~gitbook/image?url=https%3A%2F%2F3436682446-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FY2qxVf5VTm3fmwP4B4Gx%252Fuploads%252F6ulxTZvM0Fc0Jd5Ft0qp%252F4.1response2.png%3Falt%3Dmedia%26token%3De0536457-d47a-4c79-b875-76038a0cec79\&width=768\&dpr=4\&quality=100\&sign=3b776ca7\&sv=2)

### 2. Specifying frameworks or libraries <a href="#id-2.-specifying-frameworks-or-libraries" id="id-2.-specifying-frameworks-or-libraries"></a>

If you want a specific testing framework to be used, include that detail in the prompt.

The prompt output below: *Write tests for this function using Mockito*

![](https://docs.tabnine.com/~gitbook/image?url=https%3A%2F%2F3436682446-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FY2qxVf5VTm3fmwP4B4Gx%252Fuploads%252FUYIzxBcOy3a0Hwihi8vv%252F4.2responseFramework.png%3Falt%3Dmedia%26token%3D877b1a00-a623-4d78-a32d-0675499b2895\&width=768\&dpr=4\&quality=100\&sign=2431693d\&sv=2)

## Ask for Examples

General Rule: Request examples to understand concepts better.

### 1. Asking for examples to improve results <a href="#id-1.-asking-for-examples-to-improve-results" id="id-1.-asking-for-examples-to-improve-results"></a>

Less effective prompt: *Explain SQL joins*

![](https://docs.tabnine.com/~gitbook/image?url=https%3A%2F%2F3436682446-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FY2qxVf5VTm3fmwP4B4Gx%252Fuploads%252Fvi9n7EXw2LNpoNrk2Ms0%252F5.1response1.png%3Falt%3Dmedia%26token%3D4be037ab-7279-4f29-9f17-899ecdaf2f9f\&width=768\&dpr=4\&quality=100\&sign=b030ebb8\&sv=2)

More effective prompt: *Explain SQL joins with examples for inner join, left join, right join, and full join*

![](https://docs.tabnine.com/~gitbook/image?url=https%3A%2F%2F3436682446-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FY2qxVf5VTm3fmwP4B4Gx%252Fuploads%252FY66vrUUkI4G8LcVtYD8q%252F5.1response2.png%3Falt%3Dmedia%26token%3D4261d9b1-fcb3-4eeb-85de-78ce9aa42fab\&width=768\&dpr=4\&quality=100\&sign=8c016f56\&sv=2)

Response image truncated for ease of presentation.

## Be Concise, *But* Complete

General Rule: Be concise to avoid overwhelming the model, but include all necessary information.

### 1. Non-specific prompts vs. specific prompts <a href="#id-1.-non-specific-prompts-vs.-specific-prompts" id="id-1.-non-specific-prompts-vs.-specific-prompts"></a>

Less effective prompt: *Can you help me with my project?*

![](https://docs.tabnine.com/~gitbook/image?url=https%3A%2F%2F3436682446-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FY2qxVf5VTm3fmwP4B4Gx%252Fuploads%252FhVbCKm843oCvPi7ovTC1%252F6.1helpWithProject.png%3Falt%3Dmedia%26token%3D0b4de914-282f-45de-93cd-9f07a48c41ae\&width=768\&dpr=4\&quality=100\&sign=694c4269\&sv=2)

More effective prompt: *I need help writing a Python function that reads a CSV file and prints the contents. The file has three columns: 'name', 'age', and 'email'.*

![](https://docs.tabnine.com/~gitbook/image?url=https%3A%2F%2F3436682446-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FY2qxVf5VTm3fmwP4B4Gx%252Fuploads%252F12xH7OzOQIdwb89GXcaC%252F6.1conciseButComplete.png%3Falt%3Dmedia%26token%3D7f7fd385-a9fc-4063-952b-2a7a2a7f8799\&width=768\&dpr=4\&quality=100\&sign=58e1b31\&sv=2)R

Response image truncated for ease of presentation.

## Use examples of expected output <a href="#use-examples-of-expected-output" id="use-examples-of-expected-output"></a>

Providing Tabnine Chat with examples of expected output will improve the generated response.

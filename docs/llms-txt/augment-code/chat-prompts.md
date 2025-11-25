# Source: https://docs.augmentcode.com/using-augment/chat-prompts.md

# Source: https://docs.augmentcode.com/jetbrains/using-augment/chat-prompts.md

# Source: https://docs.augmentcode.com/using-augment/chat-prompts.md

# Source: https://docs.augmentcode.com/jetbrains/using-augment/chat-prompts.md

# Example Prompts for Chat

> Using natural language to interact with your codebase unlocks a whole new way of working. Learn how to get the most out of Chat with the following example prompts.

export const type_0 = "chats"

## About chatting with your codebase

Augment's Chat has deep understanding about your codebase, dependencies, and best practices. You can use Chat to ask questions about your code, but it also can help you with general software engineering questions, think through technical decisions, explore new libraries, and more.

## Enhancing your prompt

You can improve the quality of your {type_0} by starting with a well crafted prompt. You can start with a quick or incomplete prompt and use the prompt enhancer to add relevant references, structure, and conventions from your codebase to improve the prompt before it is sent.

1. Write your prompt in the prompt input box
2. Click the Enhance Prompt ✨ button
3. Review and edit the enhanced prompt
4. Submit your prompt

## Example Prompts

### Explain code

* Explain this codebase to me
* How do I use the Twilio API to send a text message?
* Explain how generics work in TypeScript and give me a simple example

### Finding code

* Where are all the useEffect hooks that depend on the 'currentUser' variable?
* Find the decorators that implement retry logic across our microservices
* Find coroutines that handle database transactions without a timeout parameter

### Generate code

* Write a function to check if a string is a valid email address
* Generate a middleware function that rate-limits API requests using a sliding window algorithm
* Create a SQL query to find the top 5 customers who spent the most money last month

### Write tests

* Write integration tests for this API endpoint
* What edge cases have I not included in this test?
* Generate mock data for testing this customer order processing function

### Refactor and improve code

* This function is running slowly with large collections - how can I optimize it?
* Refactor this callback-based code to use async/await instead
* Rewrite this function in Rust

### Find and fix errors

* This endpoint sometimes returns a 500 error. Here's the error log - what's wrong?
* I'm getting 'TypeError: Cannot read property 'length' of undefined' in this component.
* Getting CORS errors when my frontend tries to fetch from the API

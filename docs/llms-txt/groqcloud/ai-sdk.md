# Source: https://console.groq.com/docs/ai-sdk

---
description: Learn how to use the Vercel AI SDK with Groq to build and deploy high-speed, scalable LLM applications with modern frontend frameworks.
title: Vercel AI SDK + Groq: Rapid LLM App Development - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

## [✨ Vercel AI SDK + Groq: Rapid App Development](#-vercel-ai-sdk--groq-rapid-app-development)

Vercel's AI SDK enables seamless integration with Groq, providing developers with powerful tools to leverage language models hosted on Groq for a variety of applications. By combining Vercel's cutting-edge platform with Groq's advanced inference capabilities, developers can create scalable, high-speed applications with ease.

### [Why Choose the Vercel AI SDK?](#why-choose-the-vercel-ai-sdk)

* A versatile toolkit for building applications powered by advanced language models like Llama 3.3 70B
* Ideal for creating chat interfaces, document summarization, and natural language generation
* Simple setup and flexible provider configurations for diverse use cases
* Fully supports standalone usage and seamless deployment with Vercel
* Scalable and efficient for handling complex tasks with minimal configuration

### [Quick Start Guide in JavaScript (5 minutes to deployment)](#quick-start-guide-in-javascript-5-minutes-to-deployment)

#### [1\. Create a new Next.js project with the AI SDK template:](#1-create-a-new-nextjs-project-with-the-ai-sdk-template)

curl

```
npx create-next-app@latest my-groq-app --typescript --tailwind --src-dir
cd my-groq-app
```

#### [2\. Install the required packages:](#2-install-the-required-packages)

curl

```
npm install @ai-sdk/groq ai
npm install react-markdown
```

#### [3\. Create a .env.local file in your project root and configure your Groq API Key:](#3-create-a-envlocal-file-in-your-project-root-and-configure-your-groq-api-key)

curl

```
GROQ_API_KEY="your-api-key"
```

#### [4\. Create a new directory structure for your Groq API endpoint:](#4-create-a-new-directory-structure-for-your-groq-api-endpoint)

curl

```
mkdir -p src/app/api/chat
```

#### [5\. Initialize the AI SDK by creating an API route file called route.ts in app/api/chat:](#5-initialize-the-ai-sdk-by-creating-an-api-route-file-called-routets-in-appapichat)

JavaScript

```
import { groq } from '@ai-sdk/groq';
import { streamText } from 'ai';

// Allow streaming responses up to 30 seconds
export const maxDuration = 30;

export async function POST(req: Request) {
  const { messages } = await req.json();

  const result = streamText({
    model: groq('llama-3.3-70b-versatile'),
    messages,
  });

  return result.toDataStreamResponse();
}
```

**Challenge**: Now that you have your basic chat interface working, try enhancing it to create a specialized code explanation assistant!

#### [6\. Create your front end interface by updating the app/page.tsx file:](#6-create-your-front-end-interface-by-updating-the-apppagetsx-file)

JavaScript

```
'use client';

import { useChat } from 'ai/react';

export default function Chat() {
  const { messages, input, handleInputChange, handleSubmit } = useChat();

  return (
    <div className="min-h-screen bg-white">
      <div className="mx-auto w-full max-w-2xl py-8 px-4">
        <div className="space-y-4 mb-4">
          {messages.map(m => (
            <div 
              key={m.id} 
              className={`flex ${m.role === 'user' ? 'justify-end' : 'justify-start'}`}
            >
              <div 
                className={`
                  max-w-[80%] rounded-lg px-4 py-2
                  ${m.role === 'user' 
                    ? 'bg-blue-100 text-black' 
                    : 'bg-gray-100 text-black'}
                `}
              >
                <div className="text-xs text-gray-500 mb-1">
                  {m.role === 'user' ? 'You' : 'Llama 3.3 70B powered by Groq'}
                </div>
                <div className="text-sm whitespace-pre-wrap">
                  {m.content}
                </div>
              </div>
            </div>
          ))}
        </div>

        <form onSubmit={handleSubmit} className="flex gap-4">
          <input
            value={input}
            onChange={handleInputChange}
            placeholder="Type your message..."
            className="flex-1 rounded-lg border border-gray-300 px-4 py-2 text-black focus:outline-none focus:ring-2 focus:ring-[#f55036]"
          />
          <button 
            type="submit"
            className="rounded-lg bg-[#f55036] px-4 py-2 text-white hover:bg-[#d94530] focus:outline-none focus:ring-2 focus:ring-[#f55036]"
          >
            Send
          </button>
        </form>
      </div>
    </div>
  );
}
```

#### [7\. Run your development enviornment to test our application locally:](#7-run-your-development-enviornment-to-test-our-application-locally)

curl

```
npm run dev
```

#### [8\. Easily deploy your application using Vercel CLI by installing vercel and then running the vercel command:](#8-easily-deploy-your-application-using-vercel-cli-by-installing-vercel-and-then-running-the-vercel-command)

The CLI will guide you through a few simple prompts:

* If this is your first time using Vercel CLI, you'll be asked to create an account or log in
* Choose to link to an existing Vercel project or create a new one
* Confirm your deployment settings

Once you've gone through the prompts, your app will be deployed instantly and you'll receive a production URL! 🚀

curl

```
npm install -g vercel
vercel
```

### [Additional Resources](#additional-resources)

For more details on integrating Groq with the Vercel AI SDK, see the following:

* [Official Documentation: Vercel](https://sdk.vercel.ai/providers/ai-sdk-providers/groq)
* [Vercel Templates for Groq](https://sdk.vercel.ai/providers/ai-sdk-providers/groq)
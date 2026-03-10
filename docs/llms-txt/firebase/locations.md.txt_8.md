# Source: https://firebase.google.com/docs/ai-logic/locations.md.txt

|---|
| *Click your Gemini API provider to view provider-specific content and code on this page.* <button value="dev" default="">Gemini Developer API</button> <button value="vertex">Vertex AI Gemini API</button> |

<br />

<br />

The Gemini Developer API provides global access to models, which means
your request will be handled by an available model anywhere in the global pool.

> [!NOTE]
> **Note:** This page is *not* about whether you as a developer or one of your end users in a region can access the Gemini Developer API. Learn more about the [supported regions](https://ai.google.dev/gemini-api/docs/available-regions) and any relevant [use restrictions](https://ai.google.dev/gemini-api/terms#use-restrictions) for the Gemini Developer API.   
>
> This page is about you *explicitly specifying the **location for the model**
> that you're accessing in your requests* (for example, to meet data residency requirements). If this feature is important to you, then consider using the Vertex AI Gemini API to access generative models instead.
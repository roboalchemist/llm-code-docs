# ✨ Build a Real-Time Stock Search App Using Dappier, Bolt.new, and Supabase
Source: https://docs.dappier.com/cookbook/recipes/bolt-stock-market-search



This cookbook demonstrates how to build a **real-time stock market search** application using [Dappier](https://dappier.com/), [Bolt.new](https://bolt.new/), and [Supabase](https://supabase.com/)—a powerful trio that lets you generate, run, and deploy fullstack applications directly from the browser without requiring local setup.

In this walkthrough, you'll explore:

* **Bolt.new**: An AI-assisted development platform by StackBlitz that enables instant scaffolding of fullstack web apps using natural language prompts. It supports both frontend and backend logic, with built-in support for React, Node.js, Express, Supabase Edge Functions, and more.
* **Supabase**: An open-source Firebase alternative offering a scalable backend, database, and serverless Edge Functions. It's ideal for deploying APIs securely and integrating them seamlessly with frontend apps.
* **Dappier**: A platform that connects LLMs and agentic AI applications to real-time, rights-cleared data from trusted sources. Dappier delivers enriched, prompt-ready data across domains like finance, news, and web search—making it ideal for real-time applications.
* **Real-Time Stock Market App**: A frontend + API application where users can enter a stock ticker or company name to retrieve the latest stock price and financial news using Dappier’s AI model, optionally routed through a Supabase Edge Function for deployment on Netlify or Vercel.

This setup demonstrates a practical example of how you can leverage Bolt.new, Supabase, and Dappier together to create useful, data-rich applications without complex infrastructure or boilerplate.

## Watch the Video Guide

If you prefer a visual walkthrough, check out the accompanying video guide below:

<iframe width="560" height="315" src="https://www.youtube.com/embed/wGpvljD3Ss4?si=_84C1CFl6d0t1gZT" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

## 🔍 Live Demo

Want to see the app in action or explore the code behind it?

* 👉 **Try the live real-time stock market explorer:**
  [https://teal-peony-ae1f3a.netlify.app/](https://teal-peony-ae1f3a.netlify.app/)

* 🛠 **View the source code directly on Bolt.new:**
  [https://bolt.new/\~/sb1-v4qi4fca](https://bolt.new/~/sb1-v4qi4fca)

This deployment is powered by **Bolt.new**, **Supabase Edge Functions**, and **Dappier** — delivering real-time stock insights with a premium, production-ready UI. Try queries like:

* `What's going on with AAPL today?`
* `Show me the latest on TSLA`
* `News and stock price of Google`

Experience your AI-powered financial assistant live in the browser.

## 🚀 Getting Started: From Prompt to Deployment

To build and deploy your real-time stock market app using **Bolt.new** and **Dappier**, follow these structured steps:

### 🧾 Step 1: Generate the Frontend App on Bolt.new

1. Open [https://bolt.new](https://bolt.new) in your browser.
2. Paste the following prompt exactly as it is into the Bolt.new interface:

```markdown  theme={null}
Create a beautiful frontend-only web app called "Stock Market Search using Dappier".

The app should have:
- A centered input field that accepts natural language stock queries (e.g., "What’s going on with AAPL today?")
- A bold, animated "Search" button below the input
- On click, show a styled Markdown-formatted AI response (use placeholder content for now)

UI design:
- Full-height responsive layout
- Clean, centered container with a blurred background
- Smooth animations for input focus, button press, and content transitions
- Rounded corners, soft shadows, and elegant hover effects
- Use a readable sans-serif font like Inter or SF Pro
- Dark mode by default with a light mode toggle
- Include a loading spinner while waiting for the Dappier AI

The interface should feel like a premium financial assistant — intuitive, modern, and production-ready.
```

3. Click **Submit** and wait for Bolt.new to scaffold your frontend application.

### 🔗 Step 2: Connect Bolt.new with Supabase

Once your frontend application is scaffolded, follow these steps to link it with your Supabase backend:

1. In the **Bolt.new** interface, click on the **Integrations** button located in the top-right corner of the screen.
2. From the available integrations, select **Supabase**.
3. Authenticate with your Supabase account if prompted.
4. Grant access to your **organization** and select the appropriate **Supabase project** from the list.

This connection will allow you to deploy serverless functions (Edge Functions) and access Supabase-managed environment variables directly from your Bolt.new workspace.

### ⚙️ Step 3: Create a Supabase Edge Function for Real-Time Search

Now that your frontend is ready and connected to Supabase, use the following prompt in **Bolt.new** to generate the backend logic:

````markdown  theme={null}
The interface should feel premium, intuitive, and visually polished — like a product-ready financial assistant.

Create a Supabase Edge Function called `stockSearch` that calls the Dappier Stock Market Search API.

## Behavior:
- Accepts a POST request with JSON payload: `{ "query": "<string>" }`
- Extracts the `query` from the request body
- Calls the Dappier API:

  POST https://api.dappier.com/app/aimodel/am_01j749h8pbf7ns8r1bq9s2evrh  
  Headers:
    - Authorization: Bearer (from environment variable `DAPIER_API_KEY`)
    - Content-Type: application/json  
  Body:
    ```json
    {
      "query": "<string>"
    }
    ```

- Returns the full JSON response from Dappier as-is: `{ "message": "<string>" }`
- Display the Dappier AI response on frontend instead of mocked response.
````

Once submitted, Bolt.new will scaffold the `stockSearch` Edge Function within your Supabase project.
You can now wire your frontend to call this function and render the live results from Dappier.

### 🔐 Step 4: Configure Your Dappier API Key

To authorize your Supabase Edge Function to access real-time financial data from Dappier, you need to generate and securely store your API key.

Follow these steps:

1. Go to the Dappier API Key Portal:
   👉 [https://platform.dappier.com/profile/api-keys](https://platform.dappier.com/profile/api-keys)

2. Sign in or create a free account.

3. Copy your personal **API Key** from the **Settings → Profile** page.

4. In your Supabase dashboard:

   * Navigate to your connected project.
   * Go to **Functions → Edge Functions**.
   * Open the **Secrets** tab.
   * Add a new secret with the key:

     ```
     DAPIER_API_KEY
     ```

     and paste your API key as the value.

5. Save the secret and redeploy your Edge Function if needed.

This ensures your function can securely authenticate requests to the Dappier API.

### 🚀 Step 5: Deploy with One Click

Once your frontend and Supabase Edge Function are set up:

1. In **Bolt.new**, click the **Deploy** button located at the top-right corner of the editor.

2. Bolt will automatically build and deploy your app to **Netlify**.

3. After deployment, you’ll see a link to **Claim your app on Netlify** — click it to connect the project to your Netlify account and manage it going forward.

That’s it! Your real-time stock search is now live and powered by Dappier + Supabase.

<img src="https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/bolt-stock-market-search.png?fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=940eb0488a0b5ed9592cb0e98df20f42" alt="Bolt Stock Market Search" data-og-width="3024" width="3024" data-og-height="1644" height="1644" data-path="images/bolt-stock-market-search.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/bolt-stock-market-search.png?w=280&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=07cc60339e9f85d75ab1c2fef5748132 280w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/bolt-stock-market-search.png?w=560&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=3ff846f1574177a5ee6519efff618171 560w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/bolt-stock-market-search.png?w=840&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=91a3e268f347be10dc7a35fc4f3530db 840w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/bolt-stock-market-search.png?w=1100&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=b8271df47a462fd7ff07b5adcbd8024c 1100w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/bolt-stock-market-search.png?w=1650&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=876f25478b78c62ec3126fd443790446 1650w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/bolt-stock-market-search.png?w=2500&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=2c8c71e0510ef56ee26a84c67eab2e96 2500w" />

## 🌟 Highlights

This cookbook demonstrated how to build a real-time stock market search by combining **Bolt.new**, **Supabase**, and **Dappier**. It provides a fast, browser-based setup that showcases a practical application of AI-generated fullstack apps powered by real-time financial data.

Key tools utilized in this cookbook include:

* **Bolt.new**: An AI-assisted development platform that allows developers to create, edit, and deploy fullstack applications directly from the browser with natural language prompts. It supports frameworks like React, Node.js, Express, and Supabase Edge Functions.
* **Supabase**: An open-source backend platform that enables secure, serverless function execution via Edge Functions. Used here to route real-time queries to Dappier's API with proper authentication and scalable deployment.
* **Dappier**: A platform connecting LLMs and agentic AI applications to real-time, rights-cleared data from trusted sources, including stock market data, financial news, and web search. It delivers enriched, prompt-ready data ideal for intelligent applications.
* **Real-Time Stock Market App**: A frontend + Edge Function application that takes user input (company name or ticker) and displays live stock price and news, rendered as Markdown from the Dappier API.

This complete example provides a flexible foundation that can be easily adapted for other use cases involving real-time data, serverless backends, and dynamic, AI-enhanced interfaces.
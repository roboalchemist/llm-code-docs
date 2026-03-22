# Source: https://docs.picaos.com/use-cases/chat-app.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.picaos.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Build an AI chat app

> Integrating Pica with a Chat App

<video muted controls className="w-full aspect-video" src="https://mintcdn.com/pica-236d4a1e/dw2klXE9UvFIza5R/videos/chat-app.mp4?fit=max&auto=format&n=dw2klXE9UvFIza5R&q=85&s=908d8755374f191349a0192ba81c90d0" data-path="videos/chat-app.mp4" />

<Card title="Chat App Example" icon="github" href="https://github.com/picahq/onetool-demo" horizontal>
  Clone the repository to get started with the Chat App.
</Card>

<Tip>
  The Chat App is now also available directly in the [Pica Dashboard](https://app.picaos.com/chat).
</Tip>

## Getting Started

This example demonstrates how to integrate [Pica OneTool](https://docs.picaos.com/core/one-tool) with a Chat App.

1. **Clone the repository:**

```bash  theme={null}
git clone https://github.com/picahq/onetool-demo.git
cd onetool-demo
```

2. **Install dependencies:**

```bash  theme={null}
npm install
```

3. **Create a `.env` file in the root directory from the `.env.example` file:**

```env  theme={null}
PICA_SECRET_KEY=your_secret_key
OPENAI_API_KEY=your_openai_api_key
```

| Variable          | Description                                                          | Required |
| ----------------- | -------------------------------------------------------------------- | -------- |
| `PICA_SECRET_KEY` | Your [Pica API secret key](https://app.picaos.com/settings/api-keys) | Yes      |
| `OPENAI_API_KEY`  | Your OpenAI API key                                                  | Yes      |

4. **Run the development server:**

```bash  theme={null}
npm run dev
```

5. **Open [http://localhost:3000](http://localhost:3000) in your browser 🚀**

## Usage

Here are some example commands you can use to get started:

* What connections are available?
* Send an email using gmail to [john@doe.com](mailto:john@doe.com)
* Create a new Shopify product
* Insert a new record into my Postgres database
* Create a record in Airtable
* What actions are supported for Attio?
* Search the web for the best restaurants in SF using Exa


Built with [Mintlify](https://mintlify.com).
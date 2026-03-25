# Source: https://docs.picaos.com/use-cases/gmail-contact-form.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.picaos.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Build a Contact Form Powered by Gmail

> Learn how to build a contact form in Next.js that sends emails directly to Gmail—no Formspree or third-party form backend required.

<Frame caption="Build your own contact form with Gmail integration">
  <iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/GpHftxh_fIE" title="Build a Contact Form Powered by Gmail" frameborder="0" allowFullScreen />
</Frame>

## Overview

Building contact forms typically requires paid services like Formspree or complex backend setups. With Pica's MCP Server and Gmail integration, you can build a fully functional contact form that delivers messages straight to your Gmail inbox—completely free.

This is perfect for:

* 📄 **Landing pages** that need simple contact forms
* 🚀 **SaaS products** requiring customer contact forms
* 💼 **Portfolio sites** with inquiry forms
* 🏢 **Small business websites** without expensive form tools

## Prerequisites

Before you start, make sure you have:

1. A [Pica account](https://app.picaos.com) (free)
2. [Pica MCP Server](/mcp-server/setup) installed and configured
3. Gmail connected in your Pica dashboard
4. Node.js and npm installed

## Getting Started

### Step 1: Clone the Repository

```bash  theme={null}
git clone https://github.com/picahq/awesome-pica.git
cd awesome-pica/gmail-contact-form-submission
```

### Step 2: Install Dependencies

```bash  theme={null}
npm install
```

### Step 3: Configure Environment Variables

Create a `.env.local` file with your configuration:

```bash  theme={null}
PICA_SECRET_KEY=your_pica_secret_key
PICA_GMAIL_CONNECTION_KEY=your_gmail_connection_key
YOUR_EMAIL=your-email@gmail.com
```

| Variable                    | Description                                                          | Required |
| --------------------------- | -------------------------------------------------------------------- | -------- |
| `PICA_SECRET_KEY`           | Your [Pica API secret key](https://app.picaos.com/settings/api-keys) | Yes      |
| `PICA_GMAIL_CONNECTION_KEY` | Your Gmail connection key from Pica                                  | Yes      |
| `YOUR_EMAIL`                | The Gmail address to receive form submissions                        | Yes      |

### Step 4: Run the Development Server

```bash  theme={null}
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser to see your contact form! 🚀

## Resources

<CardGroup cols={2}>
  <Card title="GitHub Repository" icon="github" href="https://github.com/picahq/awesome-pica/tree/main/gmail-contact-form-submission">
    View the full source code
  </Card>

  <Card title="Pica MCP Server" icon="server" href="/mcp-server">
    Learn more about the MCP Server
  </Card>

  <Card title="Gmail Integration" icon="envelope" href="https://app.picaos.com/connections#open=gmail">
    Connect your Gmail account
  </Card>

  <Card title="Get Started" icon="rocket" href="/get-started">
    New to Pica? Start here
  </Card>
</CardGroup>


Built with [Mintlify](https://mintlify.com).
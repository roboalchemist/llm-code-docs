# Agents

> BaseHub Agents are AI assistants that help with content management, automated workflows, and team collaboration.

## START

It comes preconfigured with:

*   An extensive system prompt optimized for BaseHub workflows and content operations
    
*   All available tools enabled, including content editing, users data, and web access
    
*   Deep integration with BaseHub's ecosystem, understanding your content structure and relationships
    

![](https://assets.basehub.com/7b31fb4b/59f1a39e9e9965cc156936cb77c6528f/image?width=3840&quality=90&format=auto)

## Comments

You will see START in the users list when typing `@` in your comments. You can use `@START` to include the agent in the conversation. Agents in comments have contextual awareness, they will know on which block the comment is and the previous conversation in the thread, just like another user!

![](https://assets.basehub.com/7b31fb4b/193a43804b2cee819f8bb002a41756fd/image?width=3840&quality=90&format=auto)

As you can see in the conversation, once mentioned, the agent knows it needs to give an answer and assumes the context based on where the comment is located

## Agents

BaseHub Agents (currently in free beta) are AI companions that can be customized through your dashboard to help with content management, automated workflows, and team collaboration. Whether you need contextual assistance in comments, automated content updates, or external integrations with platforms like Slack and Claude, agents can be tailored to your specific needs and workflows.

Step by step creating an Agent and customizing its properties

### External usage

#### Embed chat

You can embed your chat in any application with a simple snippet provided in the connect instructions above your agent tab.

app/layout.tsx

```
import Script from 'next/script'
import { basehub } from 'basehub'

import '../basehub.config'

export default async function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  const data = await basehub().query({
    _agents: {
      docsAi: {
        embedUrl: true,
      },
    },
  })

  return (
    <html lang="en" suppressHydrationWarning>
      <body className={`${GeistSans.variable} ${GeistMono.variable} font-sans`}>
        <ThemeProvider>
          <Header />
          {children}
          <Footer />
        </ThemeProvider>
        <Toolbar />

        <Script src={data._agents.docsAi.embedUrl} />
      </body>
    </html>
  )
}
```

Embed chat implemented in BaseHub Documentation

#### Slack bot

Chat with this Agent in your Slack workspace by following the instructions in the Connect section.

![](https://assets.basehub.com/7b31fb4b/4c5cb0fc58d7160e8755e3362adeea93/screenshot-2025-07-18-at-10.19.28-am.png?width=3840&quality=90&format=auto)

Agents → Your Agent → Connect

## Customize your agent

You can customize the visuals from your agent: name, description, avatar, colors.These will be consumed to create the embed chat bubble and messages style.

![](https://assets.basehub.com/7b31fb4b/94223e05ddc46363fab5e78082b5bda5/image.png?width=3840&quality=90&format=auto)

## Pricing and Limitations

BaseHub Agents are currently available in free beta with full access to all features. As the platform evolves, we may introduce pricing tiers for advanced AI models and implement rate limits for external API calls to agents. Workflow automations will remain unaffected by any future limitations, ensuring your internal processes continue running smoothly.
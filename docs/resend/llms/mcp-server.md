# Source: https://resend.com/docs/knowledge-base/mcp-server.md

> ## Documentation Index
> Fetch the complete documentation index at: https://resend.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MCP Server

> Learn how to use the MCP Server to send emails.

export const YouTube = ({id}) => {
  return <iframe className="w-full aspect-video rounded-xl" src={`https://www.youtube.com/embed/${id}`} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen></iframe>;
};

## What is an MCP Server?

MCP is an open protocol that standardizes how applications provide context to LLMs. Among other benefits, it provides LLMs tools to act on your behalf.

If you prefer to watch a video, check out our video walkthrough below.

<YouTube id="5QHOhvT-AFg" />

## What can Resend's MCP Server do?

Currently, Resend's MCP Server is a simple server you must build locally that can send emails using Resend's API on your behalf.

* Send plain text and HTML emails
* Schedule emails for future delivery
* Add CC and BCC recipients
* Configure reply-to addresses
* Customizable sender email (requires verification)

As an example, you could use this to run local scripts, chat with Claude, or process data and send the results to yourself or your team.

<video autoPlay muted loop playsInline className="w-full" src="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/mcp-server.mp4?fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=296653de6b6a5a471fb2357fcc766e58" data-path="images/mcp-server.mp4" />

## How to use Resend's MCP Server

Build the project locally to use this MCP server to use it in a [supported MCP client](#mcp-client-integrations).

<Steps>
  <Step title="Clone this project locally.">
    ```bash  theme={"theme":{"light":"github-light","dark":"vesper"}}
    git clone https://github.com/resend/mcp-send-email.git
    ```
  </Step>

  <Step title="Build the project">
    ```
    npm install
    npm run build
    ```
  </Step>

  <Step title="Setup Resend">
    1. [Create an API Key](https://resend.com/api-keys): copy this key to your clipboard
    2. [Verify your own domain](https://resend.com/domains): to send to email addresses other than your own
  </Step>
</Steps>

## MCP Client Integrations

With the MCP server built, you can now add it to a supported MCP client.

### Cursor

<Steps>
  <Step title="Open Cursor Settings">
    Open the command palette (`cmd`+`shift`+`p` on macOS or `ctrl`+`shift`+`p` on Windows) and choose **Cursor Settings**.
  </Step>

  <Step title="Add the MCP server">
    Select **MCP** from the left sidebar and click **Add new global MCP server** and add the following config:

    ```json  theme={"theme":{"light":"github-light","dark":"vesper"}}
    {
      "mcpServers": {
        "resend": {
          "type": "command",
          "command": "node ABSOLUTE_PATH_TO_MCP_SEND_EMAIL_PROJECT/build/index.js --key=YOUR_RESEND_API_KEY"
        }
      }
    }
    ```

    You can get the absolute path to your build script by right-clicking on the `/build/index.js` file in Cursor and selecting `Copy Path`.

    **Possible arguments**

    * `--key`: Your Resend API key (required)
    * `--sender`: Your sender email address from a verified domain (optional)
    * `--reply-to`: Your reply-to email address (optional)

    <Info>
      If you don't provide a sender email address, the MCP server will ask you to
      provide one each time you call the tool.
    </Info>

    Adding the MCP server to Cursor's global settings will let you send emails from any project on your machine using Cursor's Agent mode.
  </Step>

  <Step title="Test the sending">
    Test sending emails by going to `email.md` in the cloned project.

    * Replace the to: email address with your own
    * Select all text in `email.md`, and press `cmd+l`
    * Tell cursor to "send this as an email" in the chat (make sure cursor is in Agent mode by selecting "Agent" on lower left side dropdown).

    <img width="541" alt="Cursor chat with email.md file selected and Agent mode enabled" src="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/mcp-server-1.png?fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=fa2e1425ad8347080815dcd1dde4b7d8" data-og-width="882" data-og-height="376" data-path="images/mcp-server-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/mcp-server-1.png?w=280&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=dbdd880a1701b6a795635e33e129b62b 280w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/mcp-server-1.png?w=560&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=9e875f6e0a24e5574ac97f2b9d2d594a 560w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/mcp-server-1.png?w=840&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=d59c85a4ea1c3d375245f1e8a9015523 840w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/mcp-server-1.png?w=1100&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=4d56eb32baf2b586d5bb5f20ba426406 1100w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/mcp-server-1.png?w=1650&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=383fd69fc6081851ececb24f10d03e5a 1650w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/mcp-server-1.png?w=2500&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=380bba86ffb5c22b4828121b82f0da7c 2500w" />
  </Step>
</Steps>

### Claude Desktop

<Steps>
  <Step title="Open Claude Desktop settings">
    Open Claude Desktop settings and navigate to the "Developer" tab. Click `Edit Config`.
  </Step>

  <Step title="Add the MCP server">
    Add the following config:

    ```json  theme={"theme":{"light":"github-light","dark":"vesper"}}
    {
      "mcpServers": {
        "resend": {
          "command": "node",
          "args": ["ABSOLUTE_PATH_TO_MCP_SEND_EMAIL_PROJECT/build/index.js"],
          "env": {
            "RESEND_API_KEY": "YOUR_RESEND_API_KEY"
          }
        }
      }
    }
    ```

    You can get the absolute path to your build script by right-clicking on the `/build/index.js` file in your IDE and selecting `Copy Path`.

    **Possible environment variables**

    * `RESEND_API_KEY`: Your Resend API key (required)
    * `SENDER_EMAIL_ADDRESS`: Your sender email address from a verified domain (optional)
    * `REPLY_TO_EMAIL_ADDRESS`: Your reply-to email address (optional)

    <Info>
      If you don't provide a sender email address, the MCP server will ask you to
      provide one each time you call the tool.
    </Info>
  </Step>

  <Step title="Test the server">
    Close and reopen Claude Desktop. Verify that the `resend` tool is available in the Claude developer settings.

    <img alt="Claude Desktop developer settings with Resend MCP server showing" width="541" src="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/mcp-server-2.png?fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=4d5c737476c68debac2d0adef163fa6f" data-og-width="1584" data-og-height="1120" data-path="images/mcp-server-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/mcp-server-2.png?w=280&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=14cf03642a38d4ccb66885252da6ebd3 280w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/mcp-server-2.png?w=560&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=875b082f959d327eeef871892e7aed3f 560w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/mcp-server-2.png?w=840&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=6d34d65ae31bf92ccbe3d675c08f01f9 840w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/mcp-server-2.png?w=1100&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=15b671ad1c2b087f2d45d47eb6118783 1100w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/mcp-server-2.png?w=1650&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=6dd1751cbf3d65acb4cfad0e794cb44e 1650w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/mcp-server-2.png?w=2500&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=1d54794409ba8526e4cdfd233a8df479 2500w" />

    Chat with Claude and tell it to send you an email using the `resend` tool.
  </Step>
</Steps>

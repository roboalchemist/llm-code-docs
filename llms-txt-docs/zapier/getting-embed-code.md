# Source: https://docs.zapier.com/powered-by-zapier/embedding-zapier-mcp/guides/getting-embed-code.md

# Getting Embed Code

> Generate embed code snippets for integrating Zapier MCP into your application.

## Select your framework

<Tabs>
  <Tab title="HTML">
    The `<zapier-mcp>` element can be used directly in HTML. Add the script to the `<head>` and use the `<zapier-mcp>` element in your body.

    ### Head

    Add this script tag to your HTML `<head>`:

    ```html  theme={null}
    <script src="https://mcp.zapier.com/embed/v1/mcp.js"></script>
    ```

    ### Body

    Add the `<zapier-mcp>` element to your HTML body:

    ```html  theme={null}
    <zapier-mcp

    embed-id="FILL_IN_YOUR_EMBED_ID"
    width="100%"
    height="600px"
    sign-up-email="email_of_your_user@example.com"
    sign-up-first-name="first_name_of_your_user"
    sign-up-last-name="last_name_of_your_user"

    > </zapier-mcp>

    <script>
    document.querySelector('zapier-mcp').addEventListener('mcp-server-url', (event) => {
    // this is the URL of the MCP server for a specific user
    console.log('MCP Server URL:', event.detail.serverUrl);
    });

    document.querySelector('zapier-mcp').addEventListener('tools-changed', (event) => {
    // this is sent whenever a user adds/removes tools from their MCP server
    console.log('Tools changed');
    });

    document.querySelector('zapier-mcp').addEventListener('close-requested', (event) => {
    // this is sent when the user clicks the close button in the embed
    });
    </script>

    ```
  </Tab>

  <Tab title="Vanilla JS">
    The Zapier MCP custom element can be used with vanilla JS. Use the JavaScript snippet to load the script and add a `<zapier-mcp>` element.

    ### Javascript

    ```javascript  theme={null}
    // Load the MCP embed script

    const script = document.createElement("script");
    script.src = "https://mcp.zapier.com/embed/v1/mcp.js";
    document.head.appendChild(script);

    // Wait for script to load, then create and display zapier-mcp
    script.onload = () => {
    const element = document.createElement("zapier-mcp");
    element.setAttribute("embed-id", "FILL_IN_YOUR_EMBED_ID");
    element.setAttribute("width", "100%");
    element.setAttribute("height", "600px");
    element.setAttribute("sign-up-email", "email_of_your_user@example.com");
    element.setAttribute("sign-up-first-name", "first_name_of_your_user");
    element.setAttribute("sign-up-last-name", "last_name_of_your_user");

    element.addEventListener('mcp-server-url', (event) => {
    // this is the URL of the MCP server for a specific user
    console.log('MCP Server URL:', event.detail.serverUrl);
    });

    element.addEventListener('tools-changed', (event) => {
    // this is sent whenever a user adds/removes tools from their MCP server
    console.log('Tools changed');
    });

    element.addEventListener('close-requested', (event) => {
    // this is sent when the user clicks the close button in the embed
    console.log('Close requested');
    });

    const container = document.querySelector("#zapier-mcp-container") || document.body;
    container.appendChild(element);
    };
    ```
  </Tab>

  <Tab title="React">
    Custom elements (web components) can be used with React. The example shows a TypeScript wrapper component with typed props for handling callbacks. Add the `jsx-types.d.ts` snippet for proper TypeScript support.

    ### HTML

    Add the script to your HTML `<head>`:

    ```html  theme={null}
    <!-- See the "Vanilla JS" solution if you'd rather use JS to load these -->
    <script src="https://mcp.zapier.com/embed/v1/mcp.js"></script>
    ```

    Now create a React component to use the `<zapier-mcp>` element:

    ```ts twoslash ZapierMcp.tsx lines theme={null}

    import { useEffect, useRef } from "react";

    interface ZapierMcpProps {
    embedId: string;
    width?: string;
    height?: string;
    className?: string;
    origin?: string;
    signUpEmail?: string;
    signUpFirstName?: string;
    signUpLastName?: string;
    onMcpServerUrl?: (serverUrl: string) => void;
    onToolsChanged?: (tools: any[]) => void;
    onCloseRequested?: () => void;
    }

    export const ZapierMcp = ({
    embedId,
    width = "100%",
    height = "600px",
    className,
    origin,
    signUpEmail,
    signUpFirstName,
    signUpLastName,
    onMcpServerUrl,
    onToolsChanged,
    onCloseRequested,
    }: ZapierMcpProps) => {
    const mcpRef = useRef<HTMLElement>(null);

    useEffect(() => {
    const element = mcpRef.current;
    if (!element) return;

    const handleMcpServerUrl = (event: CustomEvent<{ serverUrl: string }>) => {
      onMcpServerUrl?.(event.detail.serverUrl);
    };

    const handleToolsChanged = (event: CustomEvent<{ tools: any[] }>) => {
      onToolsChanged?.();
    };

    const handleCloseRequested = () => {
      onCloseRequested?.();
    };

    element.addEventListener('mcp-server-url', handleMcpServerUrl as EventListener);
    element.addEventListener('tools-changed', handleToolsChanged as EventListener);
    element.addEventListener('close-requested', handleCloseRequested);

    return () => {
      element.removeEventListener('mcp-server-url', handleMcpServerUrl as EventListener);
      element.removeEventListener('tools-changed', handleToolsChanged as EventListener);
      element.removeEventListener('close-requested', handleCloseRequested);
    };

    }, [onMcpServerUrl, onToolsChanged, onCloseRequested]);

    return (
    <zapier-mcp
      ref={mcpRef}
      embed-id={embedId}
      width={width}
      height={height}
      class-name={className}
      origin={origin}
      sign-up-email={signUpEmail}
      sign-up-first-name={signUpFirstName}
      sign-up-last-name={signUpLastName}
    />
    );
    };

    // Example usage:
    export default function App() {
    const handleMcpServerUrl = (serverUrl: string) => {
    // this is the URL of the MCP server for a specific user
    console.log('MCP Server URL:', serverUrl);
    };

    const handleToolsChanged = () => {
    // this is sent whenever a user adds/removes tools from their MCP server
    console.log('Tools changed:', tools);
    };

    const handleCloseRequested = () => {
    // this is sent when the user clicks the close button in the embed
    console.log('Close requested');
    };

    return (
    <div>
    <h1>Zapier MCP React</h1>
    <ZapierMcp
        embedId="FILL_IN_YOUR_EMBED_ID"
        width="100%"
        height="600px"
        signUpEmail="email_of_your_user@example.com"
        signUpFirstName="first_name_of_your_user"
        signUpLastName="last_name_of_your_user"
        onMcpServerUrl={handleMcpServerUrl}
        onToolsChanged={handleToolsChanged}
        onCloseRequested={handleCloseRequested}
      />
    </div>
    );
    }

    ```

    <CodeGroup>
      ```ts jsx-types.d.ts (React 18) theme={null}
      declare namespace JSX {
        interface IntrinsicElements {
          "zapier-mcp": any;
        }
      }
      ```

      ```ts jsx-types.d.ts (React 19) theme={null}
      import "react";

      declare module "react" {
        namespace JSX {
          interface IntrinsicElements {
            "zapier-mcp": any;
          }
        }
      }
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Angular">
    Custom elements (web components) can be used with Angular. Use the following snippets as an example.

    ### Installation

    Add the script to your `<head>`:

    ```html  theme={null}
    <!-- See the "Vanilla JS" solution if you'd rather use JS to load these -->
    <script src="https://mcp.zapier.com/embed/v1/mcp.js"></script>
    ```

    And then use these components in your Angular application:

    <CodeGroup>
      ```html app.component.html theme={null}
      <div>
        <h1>Zapier MCP Angular</h1>
        <zapier-mcp
          #mcpEmbed
          [embed-id]="'FILL_IN_YOUR_EMBED_ID'"
          [width]="'100%'"
          [height]="'600px'"
          [sign-up-email]="'email_of_your_user@example.com'"
          [sign-up-first-name]="'first_name_of_your_user'"
          [sign-up-last-name]="'last_name_of_your_user'"
          (mcp-server-url)="onMcpServerUrl($event)"
          (tools-changed)="onToolsChanged($event)"
          (close-requested)="onCloseRequested($event)"
        ></zapier-mcp>
      </div>
      ```

      ```ts app.component.ts theme={null}
      import { Component } from "@angular/core";

      @Component({
        selector: "app-root",
        templateUrl: "./app.component.html",
        styleUrls: ["./app.component.css"],
      })
      export class AppComponent {
        onMcpServerUrl(event: CustomEvent) {
          // this is the URL of the MCP server for a specific user
          console.log("MCP Server URL:", event.detail.serverUrl);
        }

        onToolsChanged(event: CustomEvent) {
          // this is sent whenever a user adds/removes tools from their MCP server
          console.log("Tools changed");
        }

        onCloseRequested(event: CustomEvent) {
          // this is sent when the user clicks the close button in the embed
          console.log("Close requested");
        }
      }
      ```

      ```ts app.module.ts theme={null}
      import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from "@angular/core";
      import { BrowserModule } from "@angular/platform-browser";
      import { AppComponent } from "./app.component";

      @NgModule({
        imports: [BrowserModule],
        declarations: [AppComponent],
        bootstrap: [AppComponent],
        // -*-*-*- Add this line -*-*-*-
        schemas: [CUSTOM_ELEMENTS_SCHEMA],
        // -*-*-*-*-*-*-*-*-*-*-*-*-*-*-
      })
      export class AppModule {}
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Vue.js 2">
    Custom elements (web components) can be used with Vue.js. Use the main.js and App.vue snippets as examples.

    ### Installation

    Add the script to your `<head>`:

    ```html  theme={null}
    <!-- See the "Vanilla JS" solution if you'd rather use JS to load these -->
    <script src="https://mcp.zapier.com/embed/v1/mcp.js"></script>
    ```

    And then use these components in your Vue application:

    <CodeGroup>
      ```html App.vue theme={null}
      <template>
        <div>
          <h1>Zapier MCP Vue</h1>
          <zapier-mcp
            :embed-id.prop="'FILL_IN_YOUR_EMBED_ID'"
            :width.prop="'100%'"
            :height.prop="'600px'"
            :sign-up-email.prop="'email_of_your_user@example.com'"
            :sign-up-first-name.prop="'first_name_of_your_user'"
            :sign-up-last-name.prop="'last_name_of_your_user'"
            @mcp-server-url="onMcpServerUrl"
            @tools-changed="onToolsChanged"
            @close-requested="onCloseRequested"
          ></zapier-mcp>
        </div>
      </template>

      <script>
        export default {
          name: "App",
          methods: {
            onMcpServerUrl(event) {
              // this is the URL of the MCP server for a specific user
              console.log("MCP Server URL:", event.detail.serverUrl);
            },
            onToolsChanged(event) {
              // this is sent whenever a user adds/removes tools from their MCP server
              console.log("Tools changed");
            },
            onCloseRequested(event) {
              // this is sent when the user clicks the close button in the embed
              console.log("Close requested");
            },
          },
        };
      </script>
      ```

      ```javascript main.js theme={null}
      import Vue from "vue";
      import App from "./App.vue";

      Vue.config.productionTip = false;

      // -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
      // Allow `<zapier-mcp>` custom element
      // -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
      Vue.config.ignoredElements = ["zapier-mcp"];

      new Vue({ render: (h) => h(App) }).$mount("#app");
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Available Attributes

The `<zapier-mcp>` element supports the following attributes:

<ResponseField name="embed-id" type="string" required>
  The unique identifier for your embed.
</ResponseField>

<ResponseField name="width" type="string" default="100%">
  Width of the embed.
</ResponseField>

<ResponseField name="height" type="string" default="600px">
  Height of the embed.
</ResponseField>

<ResponseField name="class-name" type="string">
  CSS class to apply to the iframe.
</ResponseField>

## Event Reference

The `<zapier-mcp>` element dispatches the following events:

<ResponseField name="mcp-server-url" type="CustomEvent">
  Fired when an MCP server URL is received. `event.detail.serverUrl` contains
  the URL.
</ResponseField>

<ResponseField name="tools-changed" type="CustomEvent">
  Fired when available tools change. Use a `tools/list` request from your MCP
  client to get the updated list of tools.
</ResponseField>

<ResponseField name="close-requested" type="CustomEvent">
  Fired when the user requests to close the embed.
</ResponseField>

## Enable Quick Account Creation for your users (optional)

To enable Quick Account Creation, provide your user's email, first name, and last name to Zapier MCP. This will bypass Zapier sign-up for your users.

<Note>
  All three sign-up fields (`sign-up-email`, `sign-up-first-name`,
  `sign-up-last-name`) must be provided together to enable quick account
  creation.
</Note>

<ResponseField name="sign-up-email" type="string">
  User's email address for quick account creation.
</ResponseField>

<ResponseField name="sign-up-first-name" type="string">
  User's first name for quick account creation.
</ResponseField>

<ResponseField name="sign-up-last-name" type="string">
  User's last name for quick account creation.
</ResponseField>

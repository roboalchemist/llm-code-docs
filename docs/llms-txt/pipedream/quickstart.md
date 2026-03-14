# Source: https://pipedream.com/docs/workflows/quickstart.md

# Source: https://pipedream.com/docs/connect/quickstart.md

# Source: https://pipedream.com/docs/connect/managed-auth/quickstart.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Managed Auth Quickstart

export const ConnectLinkDemo = ({supabaseUrl, supabaseAnonKey}) => {
  const [appSlug, setAppSlug] = useState("google_sheets");
  const [tokenData, setTokenData] = useState(null);
  const [connectLinkUrl, setConnectLinkUrl] = useState("");
  const [error, setError] = useState(null);
  const [copied, setCopied] = useState(false);
  const [externalUserId, setExternalUserId] = useState("");
  useEffect(() => {
    setExternalUserId(crypto.randomUUID());
  }, []);
  const generateRequestToken = () => {
    if (typeof window === "undefined") return "";
    const baseString = `${navigator.userAgent}:${window.location.host}:connect-demo`;
    return btoa(baseString);
  };
  const getConnectToken = async () => {
    try {
      const requestToken = generateRequestToken();
      const response = await fetch(`${supabaseUrl}/functions/v1/demo-connect-token`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${supabaseAnonKey}`,
          "X-Request-Token": requestToken
        },
        body: JSON.stringify({
          external_user_id: externalUserId
        })
      });
      if (!response.ok) {
        throw new Error("Failed to get Connect token");
      }
      const data = await response.json();
      setTokenData(data);
    } catch (err) {
      setError(err.message || "Failed to get Connect token");
    }
  };
  useEffect(() => {
    if (externalUserId) {
      getConnectToken();
    }
  }, [externalUserId]);
  useEffect(() => {
    if (tokenData?.connect_link_url) {
      const url = new URL(tokenData.connect_link_url);
      url.searchParams.set("app", appSlug);
      setConnectLinkUrl(url.toString());
    } else {
      setConnectLinkUrl("");
    }
  }, [tokenData, appSlug]);
  const copyToClipboard = () => {
    navigator.clipboard.writeText(connectLinkUrl);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };
  if (!tokenData?.connect_link_url) {
    return <div className="border border-gray-200 dark:border-gray-700 rounded-md overflow-hidden mt-4">
        <div className="bg-gray-100 dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700 px-4 py-2 font-medium text-sm text-gray-800 dark:text-gray-200">
          Connect Link URL
        </div>
        <div className="p-4">
          <p className="text-sm text-gray-500 dark:text-gray-400">
            Generating Connect token...
          </p>
          {error && <div className="mt-4 p-3 bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-700 text-red-800 dark:text-red-400 rounded-md">
              <div className="font-medium text-sm">Error</div>
              <div className="mt-1 text-sm">{error}</div>
            </div>}
        </div>
      </div>;
  }
  return <div className="border border-gray-200 dark:border-gray-700 rounded-md overflow-hidden mt-4">
      <div className="bg-gray-100 dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700 px-4 py-2 font-medium text-sm text-gray-800 dark:text-gray-200">
        Connect Link URL
      </div>
      <div className="p-4">
        <div className="mb-4">
          <label className="flex items-center mb-4">
            <span className="text-sm font-medium text-gray-700 dark:text-gray-300 mr-3">App to connect:</span>
            <select value={appSlug} onChange={e => setAppSlug(e.target.value)} className="border border-gray-300 dark:border-gray-600 rounded py-1 px-2 bg-white dark:bg-gray-800 text-gray-800 dark:text-gray-200">
              <option value="google_sheets">Google Sheets</option>
              <option value="github">GitHub</option>
              <option value="notion">Notion</option>
              <option value="gmail">Gmail</option>
              <option value="openai">OpenAI</option>
            </select>
          </label>

          <div className="mb-4">
            <div className="border border-blue-100 dark:border-blue-800 rounded-lg overflow-hidden">
              <div className="bg-gray-50 dark:bg-gray-900 p-4 text-sm overflow-x-auto">
                <code className="text-gray-800 dark:text-gray-200 break-all">
                  {connectLinkUrl}
                </code>
              </div>
            </div>
          </div>
        </div>

        <div className="flex space-x-3 mb-4">
          <a href={connectLinkUrl} target="_blank" rel="noopener noreferrer" className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md font-medium text-sm transition-colors inline-flex items-center">
            Open
            <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
            </svg>
          </a>

          <button onClick={copyToClipboard} className="bg-gray-100 hover:bg-gray-200 dark:bg-gray-700 dark:hover:bg-gray-600 text-gray-800 dark:text-gray-200 px-4 py-2 rounded-md font-medium text-sm transition-colors inline-flex items-center">
            {copied ? "Copied!" : "Copy"}
            <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" />
            </svg>
          </button>
        </div>

        <div className="text-gray-600 dark:text-gray-400 text-sm">
          <p>
            This URL contains a Connect Token that expires in 4 hours
            <strong className="text-gray-800 dark:text-gray-200"> or after it's used once</strong>.
            You can send this link to your users via email, SMS, or chat.
          </p>
          <p className="mt-2 text-sm text-gray-500 dark:text-gray-500">
            <strong>Note:</strong>
            {" "}Connect tokens are single-use. After a successful connection, you'll need to generate a new token.
          </p>
        </div>

        {error && <div className="mt-4 p-3 bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-700 text-red-800 dark:text-red-400 rounded-md">
            <div className="font-medium text-sm">Error</div>
            <div className="mt-1 text-sm">{error}</div>
          </div>}
      </div>
    </div>;
};

export const TokenGenerationDemo = ({supabaseUrl, supabaseAnonKey}) => {
  const [externalUserId, setExternalUserId] = useState("");
  const [tokenData, setTokenData] = useState(null);
  const [tokenLoading, setTokenLoading] = useState(false);
  const [error, setError] = useState(null);
  const generateUUIDForComponent = () => {
    return crypto.randomUUID();
  };
  const generateRequestTokenForComponent = () => {
    if (typeof window === "undefined") return "";
    const baseString = `${navigator.userAgent}:${window.location.host}:connect-demo`;
    return btoa(baseString);
  };
  const generateConnectTokenForComponent = async (externalUserId, supabaseUrl) => {
    const requestToken = generateRequestTokenForComponent();
    const response = await fetch(`${supabaseUrl}/functions/v1/demo-connect-token`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${supabaseAnonKey}`,
        "X-Request-Token": requestToken
      },
      body: JSON.stringify({
        external_user_id: externalUserId
      })
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || "Failed to get token");
    }
    return await response.json();
  };
  useEffect(() => {
    setExternalUserId(generateUUIDForComponent());
  }, []);
  const handleGenerateToken = async () => {
    setTokenLoading(true);
    setError(null);
    try {
      const data = await generateConnectTokenForComponent(externalUserId, supabaseUrl);
      setTokenData(data);
    } catch (err) {
      setError(err.message || "An error occurred");
    } finally {
      setTokenLoading(false);
    }
  };
  return <div className="border border-gray-200 dark:border-gray-700 rounded-md overflow-hidden mt-4">
      <div className="bg-gray-100 dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700 px-4 py-2 font-medium text-sm text-gray-800 dark:text-gray-200">
        Generate a Connect Token from your server
      </div>
      <div className="p-4">
        <div className="mb-3">
          <div className="flex items-center mb-4">
            <span className="text-sm font-medium text-gray-700 dark:text-gray-300">External User ID:</span>
            <code className="ml-2 px-2 py-1 bg-gray-100 dark:bg-gray-800 rounded text-sm font-medium text-gray-800 dark:text-gray-200">
              {externalUserId}
            </code>
          </div>
        </div>

        <div className="mt-4 mb-2">
          <button onClick={handleGenerateToken} disabled={tokenLoading} className="bg-blue-600 hover:bg-blue-700 disabled:bg-blue-400 text-white px-4 py-2 rounded-md font-medium text-sm transition-colors">
            {tokenLoading ? "Generating..." : "Generate Token"}
          </button>
        </div>

        {error && <div className="mt-4 p-3 bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-700 text-red-800 dark:text-red-400 rounded-md">
            <p className="text-sm">{error}</p>
          </div>}

        {tokenData && <div className="mt-4">
            <div className="text-sm mb-2 font-medium text-gray-800 dark:text-gray-200">Response:</div>
            <div className="border border-green-200 dark:border-green-700 rounded-lg overflow-hidden">
              <pre className="bg-gray-50 dark:bg-gray-900 p-4 text-sm max-h-48 overflow-auto">
                <code className="text-gray-800 dark:text-gray-200">
                  {JSON.stringify(tokenData, null, 2)}
                </code>
              </pre>
            </div>
          </div>}
      </div>
    </div>;
};

export const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im92d3R0cXZyYm15aWNlcWtnYXZxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTEzODY4MTYsImV4cCI6MjA2Njk2MjgxNn0.7QHhvz7K9KPmCGI8vm36TM5hiIASuXAY54OXt3SqCVg';

export const SUPABASE_URL = 'https://ovwttqvrbmyiceqkgavq.supabase.co';

export const PUBLIC_APPS = '3,000';

Pipedream Connect is the easiest way for your users to connect to [over {PUBLIC_APPS}+ APIs](https://pipedream.com/apps), **right in your product**. You can build in-app messaging, CRM syncs, AI agents, [and much more](/connect/use-cases/), all in a few minutes.

{/* ## Visual overview

  Here’s a high-level overview of how Connect works with your app:

  <Frame>
  <img src="/images/2a039b17-image.png" />
  </Frame>

  Here’s how Connect sits in your frontend and backend, and communicates with Pipedream’s API:

  <Frame>
  <img src="/images/bd7c61dc-image.png" />
  </Frame> */}

## Getting started

We’ll walk through these steps below with an interactive demo that lets you see an execute the code directly in the docs.

<Steps>
  <Step title="Configure your environment">
    You’ll need to do two things to add Pipedream Connect to your app:

    1. [Connect to the Pipedream API from your server](/connect/managed-auth/quickstart/#generate-a-short-lived-token). This lets you make secure calls to the Pipedream API to initiate the account connection flow and retrieve account credentials.
    2. [Add the Pipedream SDK to your frontend](/connect/managed-auth/quickstart/#connect-your-users-account) or redirect your users to [a Pipedream-hosted URL](/connect/managed-auth/connect-link/) to start the account connection flow.

    If you’re building your own app, you’ll need to provide these credentials to the environment, or retrieve them from your secrets store:

    ```env  theme={null}
    # Used to authorize requests to the Pipedream API
    PIPEDREAM_CLIENT_ID=your_client_id
    PIPEDREAM_CLIENT_SECRET=your_client_secret
    PIPEDREAM_ENVIRONMENT=development
    PIPEDREAM_PROJECT_ID=your_project_id
    ```
  </Step>

  <Step title="Create a project in Pipedream">
    1. Open an existing Pipedream project or create a new one at [pipedream.com/projects](https://pipedream.com/projects)
    2. Click the **Settings** tab, then copy your **Project ID**
  </Step>

  <Step title="Create a Pipedream OAuth client">
    Pipedream uses OAuth to authorize requests to the REST API. To create an OAuth client:

    1. Visit the [API settings](https://pipedream.com/settings/api) for your workspace
    2. Create a new OAuth client and note the client ID and secret

    You’ll need these when configuring the SDK and making API requests.
  </Step>

  <Step title="Generate a short-lived token">
    To securely initiate account connections for your users, you’ll need to generate a short-lived token for your users and use that in the [account connection flow](/connect/managed-auth/quickstart/#connect-your-users-account). See [the docs on Connect tokens](/connect/managed-auth/tokens/) for a general overview of why we need to create tokens and scope them to end users.

    Check out the code below and **try it yourself**:

    <CodeGroup>
      ```typescript TypeScript theme={null}
      import { PipedreamClient } from "@pipedream/sdk";
       
      // This code runs on your server
      const client = new PipedreamClient({
        projectEnvironment: "production",
        clientId: process.env.PIPEDREAM_CLIENT_ID,
        clientSecret: process.env.PIPEDREAM_CLIENT_SECRET,
        projectId: process.env.PIPEDREAM_PROJECT_ID
      });
       
      // Create a token for a specific user
      const { token, expiresAt, connectLinkUrl } = await client.tokens.create({
        externalUserId: "YOUR_USER_ID", // Replace with your user's ID
      });
      ```
    </CodeGroup>

    <TokenGenerationDemo supabaseUrl={SUPABASE_URL} supabaseAnonKey={SUPABASE_ANON_KEY} />

    Once you have a token, expose an endpoint your frontend can call (the SDK's `tokenCallback` will use it) to start the account connection flow for the user, or redirect them to a Pipedream-hosted URL with [Connect Link](/connect/managed-auth/quickstart/#or-use-connect-link).

    <Note>
      Refer to the API docs for [full set of parameters you can pass](/connect/api-reference/create-connect-token) in the `ConnectTokenCreate` call.
    </Note>
  </Step>

  <Step title="Connect your user’s account">
    You have two options when connecting an account for your user:

    1. [Use the Pipedream SDK](/connect/managed-auth/quickstart/#use-the-pipedream-sdk-in-your-frontend) in your frontend
    2. [Use Connect Link](/connect/managed-auth/quickstart/#or-use-connect-link) to deliver a hosted URL to your user
  </Step>

  <Step title="Use the Pipedream SDK in your frontend">
    Use this method when you want to handle the account connection flow yourself, in your app. For example, you might want to show a **Connect Slack** button in your app that triggers the account connection flow.

    First, install the [Pipedream SDK](https://www.npmjs.com/package/@pipedream/sdk) in your frontend:

    ```java  theme={null}
    npm i --save @pipedream/sdk
    ```

    Configure the `PipedreamClient` with a `tokenCallback` that calls your backend endpoint to create tokens on demand. When the user connects an account, call `connectAccount`. The SDK opens a Pipedream iFrame and automatically refreshes tokens as they expire.

    <Note>
      If the Connect popup window doesn't open, try setting `Cross-Origin-Opener-Policy` (COOP) header to `same-origin-allow-popups` on the page that embeds the Connect iFrame.

      The default COOP is `unsafe-none`; only make this change if you explicitly enforce `same-origin`. This relaxes isolation just enough to allow trusted popups (e.g., OAuth) to open from iFrames.
    </Note>

    Try the interactive demo below to connect an account after generating a token in the previous step:

    <CodeGroup>
      ```typescript Google Sheets theme={null}
      import { PipedreamClient } from "@pipedream/sdk"

      const externalUserId = "{YOUR_USER_ID}" // Same user ID you used when generating tokens on the server

      const client = new PipedreamClient({
        projectEnvironment: "production",
        externalUserId,
        tokenCallback: async () => {
          const res = await fetch("/api/connect-token", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ external_user_id: externalUserId }),
          });

          if (!res.ok) throw new Error("Failed to fetch Connect token");
          const { token } = await res.json();
          if (!token) throw new Error("Failed to fetch Connect token");
          return token;
        },
      });

      // This code runs in the frontend; the SDK fetches tokens from your server
      export default function Home() {
        function connectAccount() {
          client.connectAccount({
            app: "google_sheets",
            // oauthAppId: "YOUR_CUSTOM_OAUTH_APP_ID",
            onSuccess: (account) => {
              // Handle successful connection
              console.log(`Account successfully connected: ${account.id}`)
            },
            onError: (err) => {
              // Handle connection error
              console.error(`Connection error: ${err.message}`)
            },
          });
        }

        return (
          <main>
            <button onClick={connectAccount}>Connect Account</button>
          </main>
        )
      }
      ```

      ```typescript GitHub theme={null}
      import { PipedreamClient } from "@pipedream/sdk"

      const externalUserId = "{YOUR_USER_ID}" // Same user ID you used when generating tokens on the server

      const client = new PipedreamClient({
        projectEnvironment: "production",
        externalUserId,
        tokenCallback: async () => {
          const res = await fetch("/api/connect-token", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ external_user_id: externalUserId }),
          });

          if (!res.ok) throw new Error("Failed to fetch Connect token");
          const { token } = await res.json();
          if (!token) throw new Error("Failed to fetch Connect token");
          return token;
        },
      });

      // This code runs in the frontend; the SDK fetches tokens from your server
      export default function Home() {
        function connectAccount() {
          client.connectAccount({
            app: "github",
            // oauthAppId: "YOUR_CUSTOM_OAUTH_APP_ID",
            onSuccess: (account) => {
              // Handle successful connection
              console.log(`Account successfully connected: ${account.id}`)
            },
            onError: (err) => {
              // Handle connection error
              console.error(`Connection error: ${err.message}`)
            },
          });
        }

        return (
          <main>
            <button onClick={connectAccount}>Connect Account</button>
          </main>
        )
      }

      ```

      ```typescript Notion theme={null}
      import { PipedreamClient } from "@pipedream/sdk"

      const externalUserId = "{YOUR_USER_ID}" // Same user ID you used when generating tokens on the server

      const client = new PipedreamClient({
        projectEnvironment: "production",
        externalUserId,
        tokenCallback: async () => {
          const res = await fetch("/api/connect-token", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ external_user_id: externalUserId }),
          });

          if (!res.ok) throw new Error("Failed to fetch Connect token");
          const { token } = await res.json();
          if (!token) throw new Error("Failed to fetch Connect token");
          return token;
        },
      });

      // This code runs in the frontend; the SDK fetches tokens from your server
      export default function Home() {
        function connectAccount() {
          client.connectAccount({
            app: "notion",
            // oauthAppId: "YOUR_CUSTOM_OAUTH_APP_ID",
            onSuccess: (account) => {
              // Handle successful connection
              console.log(`Account successfully connected: ${account.id}`)
            },
            onError: (err) => {
              // Handle connection error
              console.error(`Connection error: ${err.message}`)
            },
          });
        }

        return (
          <main>
            <button onClick={connectAccount}>Connect Account</button>
          </main>
        )
      }
      ```

      ```typescript Gmail theme={null}
      import { PipedreamClient } from "@pipedream/sdk"

      const externalUserId = "{YOUR_USER_ID}" // Same user ID you used when generating tokens on the server

      const client = new PipedreamClient({
        projectEnvironment: "production",
        externalUserId,
        tokenCallback: async () => {
          const res = await fetch("/api/connect-token", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ external_user_id: externalUserId }),
          });

          if (!res.ok) throw new Error("Failed to fetch Connect token");
          const { token } = await res.json();
          if (!token) throw new Error("Failed to fetch Connect token");
          return token;
        },
      });

      // This code runs in the frontend; the SDK fetches tokens from your server
      export default function Home() {
        function connectAccount() {
          client.connectAccount({
            app: "gmail",
            // oauthAppId: "YOUR_CUSTOM_OAUTH_APP_ID",
            onSuccess: (account) => {
              // Handle successful connection
              console.log(`Account successfully connected: ${account.id}`)
            },
            onError: (err) => {
              // Handle connection error
              console.error(`Connection error: ${err.message}`)
            },
          });
        }

        return (
          <main>
            <button onClick={connectAccount}>Connect Account</button>
          </main>
        )
      }
      ```

      ```typescript OpenAI theme={null}
      import { PipedreamClient } from "@pipedream/sdk"

      const externalUserId = "{YOUR_USER_ID}" // Same user ID you used when generating tokens on the server

      const client = new PipedreamClient({
        projectEnvironment: "production",
        externalUserId,
        tokenCallback: async () => {
          const res = await fetch("/api/connect-token", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ external_user_id: externalUserId }),
          });

          if (!res.ok) throw new Error("Failed to fetch Connect token");
          const { token } = await res.json();
          if (!token) throw new Error("Failed to fetch Connect token");
          return token;
        },
      });

      // This code runs in the frontend; the SDK fetches tokens from your server
      export default function Home() {
        function connectAccount() {
          client.connectAccount({
            app: "openai",
            // oauthAppId: "YOUR_CUSTOM_OAUTH_APP_ID",
            onSuccess: (account) => {
              // Handle successful connection
              console.log(`Account successfully connected: ${account.id}`)
            },
            onError: (err) => {
              // Handle connection error
              console.error(`Connection error: ${err.message}`)
            },
          });
        }

        return (
          <main>
            <button onClick={connectAccount}>Connect Account</button>
          </main>
        )
      }
      ```
    </CodeGroup>
  </Step>

  <Step title="Or use Connect Link">
    Use this option when you can’t execute JavaScript or open an iFrame in your environment (e.g. mobile apps) and instead want to share a URL with your end users.

    The Connect Link URL opens a Pipedream-hosted page, guiding users through the account connection process. The URL is specific to the user and expires after 4 hours.

    After generating a token in the [step above](/connect/managed-auth/quickstart/#generate-a-short-lived-token), you can use the resulting Connect Link URL. Try it below:

    <ConnectLinkDemo supabaseUrl={SUPABASE_URL} supabaseAnonKey={SUPABASE_ANON_KEY} />

    <Note>
      Make sure to add the `app` parameter to the end of the URL to specify the app.

      Check out the [full API docs](/connect/api-reference/create-connect-token) for all parameters you can pass when creating tokens, including setting redirect URLs for success or error cases.
    </Note>
  </Step>

  <Step title="Make authenticated requests">
    Now that your users have connected an account, you can use their auth in one of a few ways:

    1. [Expose 10k+ tools](/connect/components/) to your AI app or agent and call them on behalf of your customers
    2. [Send custom requests](/connect/api-proxy/) to any one of the 2500+ APIs using the Connect API proxy
    3. [Use Pipedream’s visual workflow builder](/connect/workflows/) to define complex logic to run on behalf of your users
    4. [Embed Pipedream components directly in your app](/connect/components/) to run actions and triggers on their behalf
  </Step>

  <Step title="Deploy your app to production">
    * Test end to end in [development](/connect/managed-auth/environments/)
    * Ship to production!
  </Step>
</Steps>

Built with [Mintlify](https://mintlify.com).

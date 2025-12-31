# Source: https://bun.com/docs/guides/deployment/vercel.md

# Deploy a Bun application on Vercel

export const ProductCard = ({img, href, title, description, model, type}) => {
  return <a href={href} target="_blank" rel="noopener noreferrer" className="group">
      <div className="flex flex-col gap-4 rounded-xl md:p-1">
        <div className="w-full h-32 overflow-hidden rounded-xl bg-gray-100 dark:bg-gray-800">
          <img src={img} className="w-full h-full object-cover transition-transform duration-300 group-hover:scale-105" alt={title} loading="lazy" />
        </div>
        <div className="flex flex-col gap-3 pb-2">
          <h2 className="text-md font-medium text-gray-900 dark:text-gray-200 group-hover:text-gray-600 dark:group-hover:text-gray-400 transition-colors mb-[-8px]">
            {title}
          </h2>
          <p className="text-gray-500 dark:text-gray-400 text-sm font-medium">{description}</p>
          <div className="flex gap-2 mt-2 mb-1">
            <span className="bg-gray-100 dark:bg-[#181817] text-gray-600 dark:text-white rounded-lg px-2 py-1 text-sm font-medium">
              {model}
            </span>
            <span className="bg-primary-light dark:bg-primary-dark text-white dark:text-white rounded-lg px-2 py-1 text-sm font-medium">
              {type}
            </span>
          </div>
        </div>
      </div>
    </a>;
};

[Vercel](https://vercel.com/) is a cloud platform that lets you build, deploy, and scale your apps.

<Warning>
  The Bun runtime is in Beta; certain features (e.g., automatic source maps, byte-code caching, metrics on
  `node:http/https`) are not yet supported.
</Warning>

<Note>
  `Bun.serve` is currently not supported on Vercel Functions. Use Bun with frameworks supported by Vercel, like Next.js,
  Express, Hono, or Nitro.
</Note>

***

<Steps>
  <Step title="Configure Bun in vercel.json">
    To enable the Bun runtime for your Functions, add a `bunVersion` field in your `vercel.json` file:

    ```json vercel.json icon="file-json" theme={"theme":{"light":"github-light","dark":"dracula"}}
    {
    	"bunVersion": "1.x" // [!code ++]
    }
    ```

    Vercel automatically detects this configuration and runs your application on Bun. The value has to be `"1.x"`, Vercel handles the minor version internally.

    For best results, match your local Bun version with the version used by Vercel.
  </Step>

  <Step title="Next.js configuration">
    If you’re deploying a **Next.js** project (including ISR), update your `package.json` scripts to use the Bun runtime:

    ```json package.json icon="file-json" theme={"theme":{"light":"github-light","dark":"dracula"}}
    {
    	"scripts": {
    		"dev": "bun --bun next dev", // [!code ++]
    		"build": "bun --bun next build" // [!code ++]
    	}
    }
    ```

    <Note>
      The `--bun` flag runs the Next.js CLI under Bun. Bundling (via Turbopack or Webpack) remains unchanged, but all commands execute within the Bun runtime.
    </Note>

    This ensures both local development and builds use Bun.
  </Step>

  <Step title="Deploy your app">
    Connect your repository to Vercel, or deploy from the CLI:

    ```bash terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
    # Using bunx (no global install)
    bunx vercel login
    bunx vercel deploy
    ```

    Or install the Vercel CLI globally:

    ```bash terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
    bun i -g vercel
    vercel login
    vercel deploy
    ```

    [Learn more in the Vercel Deploy CLI documentation →](https://vercel.com/docs/cli/deploy)
  </Step>

  <Step title="Verify the runtime">
    To confirm your deployment uses Bun, log the Bun version:

    ```ts index.ts icon="https://mintcdn.com/bun-1dd33a4e/Hq64iapoQXHbYMEN/icons/typescript.svg?fit=max&auto=format&n=Hq64iapoQXHbYMEN&q=85&s=c6cceedec8f82d2cc803d7c6ec82b240" theme={"theme":{"light":"github-light","dark":"dracula"}}
    console.log("runtime", process.versions.bun);
    ```

    ```txt  theme={"theme":{"light":"github-light","dark":"dracula"}}
    runtime 1.3.2
    ```

    [See the Vercel Bun Runtime documentation for feature support →](https://vercel.com/docs/functions/runtimes/bun#feature-support)
  </Step>
</Steps>

***

* [Fluid compute](https://vercel.com/docs/fluid-compute): Both Bun and Node.js runtimes run on Fluid compute and support the same core Vercel Functions features.
* [Middleware](https://vercel.com/docs/routing-middleware): To run Routing Middleware with Bun, set the runtime to `nodejs`:

```ts middleware.ts icon="https://mintcdn.com/bun-1dd33a4e/Hq64iapoQXHbYMEN/icons/typescript.svg?fit=max&auto=format&n=Hq64iapoQXHbYMEN&q=85&s=c6cceedec8f82d2cc803d7c6ec82b240" theme={"theme":{"light":"github-light","dark":"dracula"}}
export const config = { runtime: "nodejs" }; // [!code ++]
```

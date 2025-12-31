# Source: https://juno.build/docs/guides/manual-deployment.md

# Manual Deployment

We recommend using [GitHub Actions](/docs/guides/github-actions.md) for automated and efficient deployments. However, this guide walks you through manually deploying your app using the Juno CLI, covering the setup, build, and deployment process to your Juno Satellite.

---

## 1\. Install Juno CLI

Install the Juno command line interface by executing the following command in your terminal:

*   npm
*   yarn
*   pnpm

```
npm i -g @junobuild/cli
```

```
yarn global add @junobuild/cli
```

```
pnpm add -g @junobuild/cli
```

---

## 2\. Initialization

Once the CLI is set up, initialize your project by running:

```
juno config init
```

This command generates a configuration file and prompts you to log in to your Satellite from the terminal to authenticate your device.

Upon execution, Junoâs Console will open in your browser, where youâll be asked to grant permissions for your modules. These include Mission Control (your wallet), Satellite(s), and Analytics, allowing secure access from your machine.

**Info:**

If the login process opens in a different browser than the one where you're already signed into, simply copy the URL and paste it into your authenticated browser to continue.

This can occur if you've signed into the Juno Console in a browser other than your system's default.

---

## 3\. Deploy Your Project

You can use the CLI to manually deploy different parts of your app:

*   ðª Deploy frontend assets to your Satellite. Learn how.
*   ð ï¸ Build, publish and upgrade serverless functions (TypeScript or Rust). Learn how.

---

### a) ðª Deploy Frontend Assets

Get your app ready for deployment:

*   npm
*   yarn
*   pnpm

```
npm run build
```

```
yarn build
```

```
pnpm build
```

Deploy your application or website by running the following command from your projectâs root folder:

```
juno hosting deploy
```

**Tip:**

When prompted for the name or path of the folder containing your built dapp files, provide the appropriate folder name for your framework, such as `build` (SvelteKit), `out` (Next.js), or `dist` (React, Astro, or Vue).

Wait for the deploy to complete. Once uploaded, it will be live on your Juno Satellite and accessible on the web.

---

### b) ð ï¸ Build, Publish, and Upgrade Serverless Functions

To build and deploy your serverless functions written in TypeScript or Rust, you can use the CLI.

```
juno functions buildjuno functions publishjuno functions upgrade
```

*   Use publish `--no-apply` if your access key only has a **submit** role and cannot directly upgrade.
*   You can then approve and apply the change using the CLI (with another key) or Console UI.

For a full overview of the serverless lifecycleâincluding setup, development, local testing, publishing, approvals, and upgrades â see the Serverless Functions Lifecycle guide.
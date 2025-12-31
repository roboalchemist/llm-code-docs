# Source: https://docs.replit.com/getting-started/intro-replit.md

# Introduction

> Replit is the fastest way to go from idea to app. Create and publish full-stack apps from your browser with AI at your fingertips—no installation or setup required.

export const YouTubeEmbed = ({videoId, title = "YouTube video", startAt}) => {
  if (!videoId) {
    return null;
  }
  let url = "https://www.youtube.com/embed/" + videoId;
  if (startAt) {
    url = url + "?start=" + startAt;
  }
  return <Frame>
      <iframe src={url} title={title} allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowFullScreen></iframe>
    </Frame>;
};

Replit is an AI-powered platform that lets you create and publish apps from a single browser tab.
Instead of wrestling with complex development environments, you get coding, publishing, and collaboration tools in one integrated interface.

<Frame>
  <img src="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/getting-started/workspace.jpg?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=d254d021e7ba96a358f070a4700031bd" alt="Replit Workspace" data-og-width="1920" width="1920" data-og-height="1011" height="1011" data-path="images/getting-started/workspace.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/getting-started/workspace.jpg?w=280&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=50dca2489861404a46662d9c96e91010 280w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/getting-started/workspace.jpg?w=560&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=bfa0e5b1a9f711e17bf97b4f1f6c3734 560w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/getting-started/workspace.jpg?w=840&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=9370b9bc21ba9f4db2ee5ea86cbeef01 840w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/getting-started/workspace.jpg?w=1100&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=996477e5ff7c0496513e7f76913ff38a 1100w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/getting-started/workspace.jpg?w=1650&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=3934c3a7458f8b4c2af1d8a6e0cd6718 1650w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/getting-started/workspace.jpg?w=2500&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=ed11d6614e7a830524ed3a00a04267fe 2500w" />
</Frame>

Building apps traditionally requires installing programs, languages, and packages—a time-consuming setup process.
On Replit, the platform configures your environment instantly, so you can start building whether you're a beginner or experienced developer.

You have everything required to create apps from one browser tab—no installation required.
With AI coding tools, real-time collaboration, and instant sharing, Replit gets you from idea to app, fast.

## Quickstart guides

To create your app on Replit, choose the guide that matches your needs:

### Create new apps

<CardGroup cols={2}>
  <Card title="Remix an existing app" icon="shuffle" href="/getting-started/quickstarts/remix-an-app/">
    ⏱️ *1 minute*

    Jump-start your project by building on community-contributed apps.
  </Card>

  <Card title="Ask AI" icon="robot" href="/getting-started/quickstarts/ask-ai/">
    ⏱️ *7 minutes*

    Use the AI-powered Replit tools to create, explain, and debug your app.
  </Card>

  <Card title="Build from Scratch" icon="user-chef" href="/getting-started/quickstarts/from-scratch/">
    ⏱️ *15 minutes*

    Create a full-stack app with complete control.
  </Card>
</CardGroup>

### Import existing projects

<CardGroup cols={2}>
  <Card title="Import from GitHub" icon="github" href="/getting-started/quickstarts/import-from-github/">
    ⏱️ *2 minutes*

    Import an existing GitHub repository into Replit.
  </Card>

  <Card title="Import from Figma" icon="figma" href="/getting-started/quickstarts/import-from-figma/">
    ⏱️ *3 minutes*

    Convert your Figma designs into functional React applications.
  </Card>

  <Card title="Import from Bolt" icon="bolt" href="/getting-started/quickstarts/import-from-bolt/">
    ⏱️ *4 minutes*

    Migrate your Bolt projects to Replit with Agent assistance.
  </Card>

  <Card title="Import from Lovable" icon="heart" href="/getting-started/quickstarts/import-from-lovable/">
    ⏱️ *4 minutes*

    Transfer your Lovable projects to Replit and continue building.
  </Card>
</CardGroup>

### Workspace features

Replit provides the following essential app creation tools:

* [Real-time preview](/replit-workspace/workspace-features/preview) of your app
* [Publish in minutes](/category/replit-deployments)
* Browser native app that requires zero installation and configuration
* [Full-featured code editor](/category/workspace-features)
* [Mobile app](/platforms/mobile-app) for building apps from your phone or tablet
* [AI-assisted app creation](/replitai/agent)
* [Version control integration](/replit-workspace/workspace-features/version-control) for tracking changes
* [Team collaboration](/teams/public_profiles) for building together

### AI companion capabilities

<Frame>
  <img src="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/agent.jpg?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=408152e9cbfce44f10bda3881e4183cb" alt="Replit AI Agent" data-og-width="1920" width="1920" data-og-height="700" height="700" data-path="images/getting-started/agent.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/agent.jpg?w=280&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=d719a6d2c995683586cf797a21bdcdc4 280w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/agent.jpg?w=560&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=78a70340cead543bfda076142897adb8 560w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/agent.jpg?w=840&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=142d6f67d44c7913b07888edacc06495 840w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/agent.jpg?w=1100&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=5bb6ee43430ffab30266d7750d661902 1100w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/agent.jpg?w=1650&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=ccd99b75fe0b7f8a77b02554730127b1 1650w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/agent.jpg?w=2500&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=3e6267c7a46b0d72452f3992fe04db9c 2500w" />
</Frame>

Replit AI [Agent](/replitai/agent) and [Assistant](/replitai/assistant) accelerate app creation with the following capabilities:

* Complete app generation and setup from natural language descriptions
* Code suggestions and autocomplete
* Automated error detection and debugging assistance
* Documentation generation for your app

### Share in minutes

Publish your apps in minutes using the following tools:

* App publishing to the cloud in a few clicks
* Database integration and hosting
* Custom domain support and connection encryption for your applications

## Additional information

<Frame>
  <img src="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/mobile.jpg?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=33376aefc09f439b7d925f44ed670c19" alt="Replit Mobile" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="images/getting-started/mobile.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/mobile.jpg?w=280&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=2c4c045af7241193c1d19d1eba704f81 280w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/mobile.jpg?w=560&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=8b2f0d2cbe45b1ca6dbe759fa044689c 560w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/mobile.jpg?w=840&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=5c9f90c79cd2bbc3fc9f52be45d0c230 840w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/mobile.jpg?w=1100&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=f4e84ebf0d794fa37fb71f29bc84a574 1100w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/mobile.jpg?w=1650&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=504d9b63b67d4c1bb40dec89262b5c5e 1650w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/mobile.jpg?w=2500&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=edfa29f71ca9d2bff06804ed0440d1e3 2500w" />
</Frame>

To learn more about all of Replit's features, see the following resources:

* Learn about the Workspace features from [Workspace Features](/category/workspace-features).
* Learn about the capabilities of the Replit AI-powered features from [Replit Agent](/replitai/agent/) and [Replit Assistant](/replitai/assistant/).
* Learn how to share your creations from [Sharing Your Replit App](/replit-app/collaborate/).
* [Download the mobile app](https://replit.com/mobile/) for iOS or Android devices.

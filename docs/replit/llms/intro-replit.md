# Source: https://docs.replit.com/getting-started/intro-replit.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.replit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Introduction

> Replit is the fastest way to go from idea to app. Create and publish full-stack apps from your browser with AI at your fingertips—no installation or setup required.

export const AgentInput = ({defaultPrompt = ""}) => {
  if (typeof document !== 'undefined' && !window.LZString) {
    const script = document.createElement('script');
    script.src = 'https://cdnjs.cloudflare.com/ajax/libs/lz-string/1.5.0/lz-string.min.js';
    document.head.appendChild(script);
  }
  const inputId = 'agent-input-textarea';
  const appPlaceholder = "Make a software application that…";
  const designPlaceholder = "Design me a website, slide deck, interactive prototype...";
  if (typeof document !== 'undefined' && !document.getElementById('agent-input-styles')) {
    const style = document.createElement('style');
    style.id = 'agent-input-styles';
    style.textContent = `
      /* Theme variables - light mode */
      #agent-input-container {
        --ai-surface-bg: #FFFFFF;
        --ai-surface-higher: #F5F5F5;
        --ai-border-default: #E4E4E4;
        --ai-border-regular: #EBEBEB;
        --ai-text-secondary: #5C5C5C;
        --ai-text-tertiary: #858585;
        --ai-text-primary: #1D1D1D;
        --ai-button-bg-disabled: #F5F5F5;
        --ai-button-text-disabled: #858585;
        --ai-button-bg-active: #0079F2;
        --ai-button-text-active: #FFFFFF;
        --ai-inactive-hover-bg: #EBEBEB;
        --ai-shadow: 0 2px 6px #00000005;
      }
      
      /* Theme variables - dark mode */
      .dark #agent-input-container,
      html.dark #agent-input-container,
      [data-theme="dark"] #agent-input-container {
        --ai-surface-bg: #1A1C25;
        --ai-surface-higher: #24262F;
        --ai-border-default: #3A3D47;
        --ai-border-regular: #2E3039;
        --ai-text-secondary: #E0E0E0;
        --ai-text-tertiary: #9CA3AF;
        --ai-text-primary: #F5F5F5;
        --ai-button-bg-disabled: #24262F;
        --ai-button-text-disabled: #6B7280;
        --ai-inactive-hover-bg: #2E3039;
        --ai-shadow: 0 2px 6px #00000020;
      }
      
      /* Entry animation */
      @keyframes agent-input-fade-in-up {
        from { transform: translateY(10px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
      }
      
      /* Tab states - active */
      #agent-input-container a[data-active="true"] {
        color: var(--ai-text-secondary) !important;
        background: var(--ai-surface-bg) !important;
        border-color: var(--ai-border-default) !important;
        z-index: 2;
        transform: none;
      }
      #agent-input-container a[data-active="true"] .tab-curve-fill { fill: var(--ai-surface-bg); }
      #agent-input-container a[data-active="true"] .tab-curve-stroke { stroke: var(--ai-border-default); }
      #agent-input-container a[data-active="true"] .border-cover { display: block; background: var(--ai-surface-bg); }
      
      /* Tab states - inactive */
      #agent-input-container a[data-active="false"] {
        color: var(--ai-text-tertiary) !important;
        background: var(--ai-surface-higher) !important;
        border-color: var(--ai-border-regular) !important;
        z-index: 1;
        transform: translateY(2px);
        transition: 0.15s transform;
      }
      #agent-input-container a[data-active="false"] .tab-curve-fill { fill: var(--ai-surface-higher); }
      #agent-input-container a[data-active="false"] .tab-curve-stroke { stroke: var(--ai-border-regular); }
      #agent-input-container a[data-active="false"] .border-cover { display: none; }
      
      /* Hover state - triggered by hovering inner container OR active tab */
      #agent-input-container:has(#agent-input-inner:hover) #agent-input-inner,
      #agent-input-container:has(a[data-active="true"]:hover) #agent-input-inner {
        border-color: #85C7FF !important;
      }
      #agent-input-container:has(#agent-input-inner:hover) a[data-active="true"],
      #agent-input-container:has(a[data-active="true"]:hover) a[data-active="true"] {
        border-color: #85C7FF !important;
      }
      #agent-input-container:has(#agent-input-inner:hover) a[data-active="true"] .tab-curve-stroke,
      #agent-input-container:has(a[data-active="true"]:hover) a[data-active="true"] .tab-curve-stroke {
        stroke: #85C7FF !important;
      }
      
      /* Focus state */
      #agent-input-container:has(#agent-input-inner:focus-within) #agent-input-inner,
      #agent-input-container:has(#agent-input-inner:focus-within) a[data-active="true"] {
        border-color: #0079F2 !important;
      }
      #agent-input-container:has(#agent-input-inner:focus-within) a[data-active="true"] .tab-curve-stroke {
        stroke: #0079F2 !important;
      }
      
      /* Inactive tab hover */
      @media (hover: hover) {
        #agent-input-container a[data-active="false"]:hover {
          background: var(--ai-inactive-hover-bg) !important;
          color: var(--ai-text-secondary) !important;
          transform: translateY(0) !important;
          border-color: var(--ai-border-default) !important;
        }
        #agent-input-container a[data-active="false"]:hover .tab-curve-stroke {
          stroke: var(--ai-border-default) !important;
        }
      }
      
      /* Responsive - narrow screens */
      @media screen and (max-width: 420px) {
        #agent-input-container .tab-curve { display: none !important; }
        #agent-input-container #agent-input-tabs { padding-left: 0 !important; padding-right: 0 !important; }
        #agent-input-container #agent-input-tabs a { border-radius: 8px 8px 0 0 !important; }
        #agent-input-container #agent-input-tabs a:last-child { margin-right: 0 !important; }
        #agent-input-container #agent-input-inner { border-radius: 0 0 8px 8px !important; }
        #agent-input-container .border-cover { left: 0 !important; right: 0 !important; }
      }
    `;
    document.head.appendChild(style);
  }
  const getPromptValue = () => document.getElementById(inputId)?.value?.trim() || '';
  const getLink = () => {
    if (typeof document === 'undefined' || !window.LZString) return '';
    const prompt = getPromptValue();
    if (!prompt) return '';
    const stack = document.getElementById('agent-input-container')?.dataset?.stack || 'Build';
    const encoded = window.LZString.compressToEncodedURIComponent(prompt);
    const utm = 'utm_source=replit-docs&utm_medium=docs&utm_campaign=docs-intro-agent-input&utm_content=homepage-prompt-box';
    return `https://replit.com/?stack=${stack}&prompt=${encoded}&referrer=replit-docs&${utm}`;
  };
  const updateButtonState = () => {
    const btn = document.getElementById('agent-input-start-btn');
    if (!btn) return;
    const hasText = getPromptValue().length > 0;
    btn.style.background = `var(--ai-button-bg-${hasText ? 'active' : 'disabled'})`;
    btn.style.color = `var(--ai-button-text-${hasText ? 'active' : 'disabled'})`;
    btn.style.cursor = hasText ? 'pointer' : 'not-allowed';
  };
  const handleTabClick = (e, tabName) => {
    e.preventDefault();
    const container = document.getElementById('agent-input-container');
    const textarea = document.getElementById(inputId);
    if (!container) return;
    const isApp = tabName === 'App';
    container.dataset.stack = isApp ? 'Build' : 'Design';
    container.querySelector('#agent-input-tab-app').dataset.active = isApp ? 'true' : 'false';
    container.querySelector('#agent-input-tab-design').dataset.active = isApp ? 'false' : 'true';
    if (textarea) textarea.placeholder = isApp ? appPlaceholder : designPlaceholder;
  };
  const handleStartClick = e => {
    e.preventDefault();
    const link = getLink();
    if (link) window.open(link, '_blank');
  };
  const TabCurve = ({tabId, side}) => {
    const clipId = `clip-${tabId}-${side}`;
    return <svg className="tab-curve" width="9" height="9" viewBox="0 0 9 9" fill="none" style={{
      position: 'absolute',
      [side]: '-8px',
      bottom: '-1px',
      pointerEvents: 'none',
      transform: side === 'right' ? 'scaleX(-1)' : 'none',
      overflow: 'hidden'
    }}>
        <defs><clipPath id={clipId}><rect width="9" height="9" /></clipPath></defs>
        <g clipPath={`url(#${clipId})`}>
          <path className="tab-curve-fill" d="M9 9H-2V8H0C4.41828 8 8 4.41828 8 0V-2H9V9Z" />
          <rect className="tab-curve-stroke" x="-9.5" y="-9.5" width="17" height="17" rx="7.5" fill="none" strokeWidth="1" />
        </g>
      </svg>;
  };
  const Tab = ({id, name, icon, isActive}) => <a href="#" id={id} data-active={isActive ? "true" : "false"} onClick={e => handleTabClick(e, name)} style={{
    display: 'flex',
    flex: 1,
    position: 'relative',
    cursor: 'pointer',
    boxSizing: 'border-box',
    marginRight: '-1px',
    borderTop: '1px solid',
    borderLeft: '1px solid',
    borderRight: '1px solid',
    borderBottom: 'none',
    borderRadius: '8px 8px 0 0',
    height: '37px',
    textDecoration: 'none',
    userSelect: 'none',
    overflow: 'visible'
  }}>
      <TabCurve tabId={id} side="left" />
      <TabCurve tabId={id} side="right" />
      <span className="border-cover" style={{
    position: 'absolute',
    right: 0,
    bottom: '-1px',
    left: 0,
    height: '2px',
    zIndex: 3
  }} />
      <span style={{
    display: 'flex',
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    gap: '4px',
    zIndex: 1,
    padding: '8px 12px',
    fontSize: '14px'
  }}>
        {icon}
        <span>{name}</span>
      </span>
    </a>;
  const AppIcon = <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path fillRule="evenodd" d="M12 1.252c.483 0 .957.127 1.375.368l-.001.001 6.998 3.998.003.001.153.096a2.752 2.752 0 0 1 1.222 2.283v8.002a2.75 2.75 0 0 1-1.375 2.379h-.003l-6.998 3.999h.001a2.75 2.75 0 0 1-1.294.366.75.75 0 0 1-.163 0 2.748 2.748 0 0 1-1.293-.365l-6.997-4h-.003A2.751 2.751 0 0 1 2.25 16V7.999l.006-.18A2.75 2.75 0 0 1 3.625 5.62h.003l6.997-3.999c.418-.241.892-.37 1.375-.37ZM3.75 15.999l.01.163a1.25 1.25 0 0 0 .615.918l6.875 3.929v-8.575l-7.5-4.31v7.875Zm9-3.565v8.575l6.875-3.929A1.25 1.25 0 0 0 20.25 16V8.123l-7.5 4.31ZM12 2.752c-.22 0-.435.057-.625.167l-.003.002L4.52 6.836l7.479 4.299 7.48-4.3-6.851-3.914-.003-.002A1.25 1.25 0 0 0 12 2.752Z" clipRule="evenodd" /></svg>;
  const DesignIcon = <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M21.25 4.123a1.374 1.374 0 0 0-2.343-.97L12.06 9.999 14 11.94l6.848-6.845c.257-.257.402-.607.402-.97ZM8.37 13.688c.418.205.803.474 1.135.806.332.332.602.716.807 1.132L12.939 13l-1.94-1.94-2.629 2.629ZM3.75 17.5c0 .856-.326 1.68-.91 2.305l-.018.018a.252.252 0 0 0 .038.385.25.25 0 0 0 .138.042H6.5a2.75 2.75 0 1 0-2.75-2.75Zm19-13.377c0 .762-.303 1.493-.842 2.032l-11.163 11.16A4.248 4.248 0 0 1 6.5 21.75H3a1.75 1.75 0 0 1-1.256-2.97c.325-.347.506-.805.506-1.28a4.251 4.251 0 0 1 4.432-4.246L17.846 2.092a2.873 2.873 0 0 1 4.904 2.031Z" /></svg>;
  const ArrowIcon = <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path fillRule="evenodd" d="M19.53 11.47a.75.75 0 0 1 0 1.06l-7 7a.75.75 0 1 1-1.06-1.06l5.72-5.72H5a.75.75 0 0 1 0-1.5h12.19l-5.72-5.72a.75.75 0 0 1 1.06-1.06l7 7Z" clipRule="evenodd" /></svg>;
  if (typeof document !== 'undefined' && defaultPrompt) {
    setTimeout(() => {
      updateButtonState();
    }, 0);
  }
  return <div id="agent-input-container" data-stack="Build" style={{
    fontFamily: "'IBM Plex Sans', sans-serif",
    width: '100%',
    maxWidth: '650px',
    minWidth: '320px',
    alignSelf: 'center',
    opacity: 0,
    animation: 'agent-input-fade-in-up 300ms ease-out forwards'
  }}>
      <div style={{
    display: 'flex',
    flexDirection: 'column'
  }}>
        <div id="agent-input-tabs" style={{
    display: 'flex',
    position: 'relative',
    alignSelf: 'center',
    marginBottom: '-1px',
    padding: '0 37px',
    width: '100%',
    boxSizing: 'border-box',
    overflow: 'visible'
  }}>
          <Tab id="agent-input-tab-app" name="App" icon={AppIcon} isActive={true} />
          <Tab id="agent-input-tab-design" name="Design" icon={DesignIcon} isActive={false} />
        </div>
        <div id="agent-input-inner" style={{
    position: 'relative',
    zIndex: 1,
    borderRadius: '8px',
    border: '1px solid var(--ai-border-default)',
    background: 'var(--ai-surface-bg)',
    transition: 'border-color 120ms ease-out'
  }}>
          <div style={{
    display: 'grid',
    gridTemplate: '1fr / 1fr',
    position: 'relative',
    boxShadow: 'var(--ai-shadow)'
  }}>
            <div style={{
    gridArea: '1 / 1',
    display: 'flex',
    flexDirection: 'column',
    gap: '4px',
    padding: '12px'
  }}>
              <div style={{
    display: 'flex',
    flexGrow: 1,
    maxHeight: '300px',
    overflow: 'auto'
  }}>
                <textarea id={inputId} placeholder={appPlaceholder} defaultValue={defaultPrompt} onInput={updateButtonState} style={{
    width: '100%',
    minHeight: '80px',
    padding: '5px 6px',
    border: 'none',
    outline: 'none',
    resize: 'none',
    fontSize: '14px',
    lineHeight: '1.5',
    color: 'var(--ai-text-primary)',
    background: 'transparent',
    fontFamily: 'inherit',
    boxSizing: 'border-box',
    flexGrow: 1
  }} />
              </div>
              <div style={{
    display: 'flex',
    justifyContent: 'flex-end',
    alignItems: 'flex-end',
    height: '32px'
  }}>
                <a href="#" id="agent-input-start-btn" onClick={handleStartClick} style={{
    display: 'flex',
    alignItems: 'center',
    gap: '6px',
    padding: '0 14px',
    height: '32px',
    fontSize: '14px',
    border: 'none',
    borderRadius: '8px',
    transition: 'all 120ms ease-out',
    color: 'var(--ai-button-text-disabled)',
    background: 'var(--ai-button-bg-disabled)',
    cursor: 'not-allowed',
    textDecoration: 'none'
  }}>
                  <span>Start</span>
                  {ArrowIcon}
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>;
};

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

Building apps traditionally requires installing programs, languages, and packages—a time-consuming setup process.
On Replit, the platform configures your environment instantly, so you can start building whether you're a beginner or experienced developer.

<div align="center">
  <AgentInput />
</div>

You have everything required to create apps from one browser tab—no installation required.
With AI coding tools, real-time collaboration, and instant sharing, Replit gets you from idea to app, fast.

## Quickstart guides

To create your app on Replit, choose the guide that matches your needs:

### Create new apps

<CardGroup cols={2}>
  <Card title="Build your first app" icon="robot" href="/getting-started/quickstarts/ask-ai/">
    ⏱️ *5 minutes*

    Build your first app with AI-powered Replit tools.
  </Card>

  <Card title="Remix an existing app" icon="shuffle" href="/getting-started/quickstarts/remix-an-app/">
    ⏱️ *1 minute*

    Jump-start your project by building on community-contributed apps.
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

Replit [Agent](/replitai/agent) accelerates app creation with the following capabilities:

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

To learn more about all of Replit's features, see the following resources:

* [Starter Plan](/getting-started/starter-plan): Learn about Starter plan features and what you can build for free
* Learn about the Workspace features from [Workspace Features](/category/workspace-features).
* Learn about the capabilities of the Replit AI-powered features from [Replit Agent](/replitai/agent/).
* Learn how to share your creations from [Sharing Your Replit App](/replit-app/collaborate/).
* [Download the mobile app](https://replit.com/mobile/) for iOS or Android devices.

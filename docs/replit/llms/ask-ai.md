# Source: https://docs.replit.com/getting-started/quickstarts/ask-ai.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.replit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Build your first App

> Create an interactive piano app using Replit Agent in just a few minutes.

export const PromptAnatomy = () => {
  if (typeof document !== 'undefined' && !document.getElementById('prompt-anatomy-styles')) {
    const style = document.createElement('style');
    style.id = 'prompt-anatomy-styles';
    style.textContent = `
      /* Theme variables - light mode */
      .prompt-anatomy {
        --pa-bg: #FFFFFF;
        --pa-border: #E4E4E4;
        --pa-text: #1D1D1D;
        --pa-what-bg: #FFF4E6;
        --pa-what-border: #FFB951;
        --pa-what-text: #8B5A00;
        --pa-look-bg: #E8F4FF;
        --pa-look-border: #5BA8FF;
        --pa-look-text: #004B8D;
        --pa-work-bg: #F3E8FF;
        --pa-work-border: #A78BFA;
        --pa-work-text: #6B21A8;
        --pa-legend-bg: #F5F5F5;
      }

      /* Theme variables - dark mode */
      .dark .prompt-anatomy,
      html.dark .prompt-anatomy,
      [data-theme="dark"] .prompt-anatomy {
        --pa-bg: #1A1C25;
        --pa-border: #3A3D47;
        --pa-text: #F5F5F5;
        --pa-what-bg: #3D2E1F;
        --pa-what-border: #FFB951;
        --pa-what-text: #FFD494;
        --pa-look-bg: #1A2A3A;
        --pa-look-border: #5BA8FF;
        --pa-look-text: #9DCFFF;
        --pa-work-bg: #2D1B3D;
        --pa-work-border: #A78BFA;
        --pa-work-text: #D8B4FE;
        --pa-legend-bg: #24262F;
      }

      .prompt-anatomy {
        font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      }

      .prompt-anatomy-container {
        background: var(--pa-bg);
        border: 1px solid var(--pa-border);
        border-radius: 12px;
        padding: 20px;
        margin: 16px 0;
      }

      .prompt-anatomy-text {
        font-size: 15px;
        line-height: 2.3;
        color: var(--pa-text);
        margin-bottom: 20px;
      }

      .prompt-highlight {
        padding: 2px 4px;
        border-radius: 4px;
        border: 1px solid;
        font-weight: 500;
        transition: all 0.2s ease;
        box-decoration-break: clone;
        -webkit-box-decoration-break: clone;
      }

      .prompt-highlight-what {
        background: var(--pa-what-bg);
        border-color: var(--pa-what-border);
        color: var(--pa-what-text);
      }

      .prompt-highlight-look {
        background: var(--pa-look-bg);
        border-color: var(--pa-look-border);
        color: var(--pa-look-text);
      }

      .prompt-highlight-work {
        background: var(--pa-work-bg);
        border-color: var(--pa-work-border);
        color: var(--pa-work-text);
      }

      .prompt-anatomy-legend {
        display: flex;
        flex-wrap: wrap;
        gap: 16px;
        padding: 16px;
        background: var(--pa-legend-bg);
        border-radius: 8px;
      }

      .prompt-legend-item {
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 13px;
      }

      .prompt-legend-badge {
        padding: 4px 8px;
        border-radius: 4px;
        border: 1px solid;
        font-weight: 500;
        white-space: nowrap;
      }

      .prompt-legend-badge-what {
        background: var(--pa-what-bg);
        border-color: var(--pa-what-border);
        color: var(--pa-what-text);
      }

      .prompt-legend-badge-look {
        background: var(--pa-look-bg);
        border-color: var(--pa-look-border);
        color: var(--pa-look-text);
      }

      .prompt-legend-badge-work {
        background: var(--pa-work-bg);
        border-color: var(--pa-work-border);
        color: var(--pa-work-text);
      }

      .prompt-legend-text {
        color: var(--pa-text);
      }

      @media screen and (max-width: 640px) {
        .prompt-anatomy-container {
          padding: 16px;
        }

        .prompt-anatomy-text {
          font-size: 14px;
        }

        .prompt-anatomy-legend {
          flex-direction: column;
          gap: 12px;
        }
      }
    `;
    document.head.appendChild(style);
  }
  return <div className="prompt-anatomy">
      <div className="prompt-anatomy-container">
        <div className="prompt-anatomy-text">
          <span className="prompt-highlight prompt-highlight-what">Build a realistic 16-key piano</span>
          {' '}with{' '}
          <span className="prompt-highlight prompt-highlight-look">proper white and black key layout that looks exactly like a real piano</span>
          .{' '}
          <span className="prompt-highlight prompt-highlight-work">Each key should press down with realistic depth animation when clicked and play the correct note</span>.
        </div>

        <div className="prompt-anatomy-legend">
          <div className="prompt-legend-item">
            <span className="prompt-legend-badge prompt-legend-badge-what">What to build</span>
            <span className="prompt-legend-text">The main thing you want</span>
          </div>
          <div className="prompt-legend-item">
            <span className="prompt-legend-badge prompt-legend-badge-look">How it looks</span>
            <span className="prompt-legend-text">Visual details and design</span>
          </div>
          <div className="prompt-legend-item">
            <span className="prompt-legend-badge prompt-legend-badge-work">How it works</span>
            <span className="prompt-legend-text">Interactions and behavior</span>
          </div>
        </div>
      </div>
    </div>;
};

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

export const AiPrompt = ({children}) => {
  return <CodeBlock className="relative block font-sans whitespace-pre-wrap break-words">
      <div className="pr-7">
        {children}
      </div>
    </CodeBlock>;
};

⏰ *Estimated time: 5 minutes*

This guide will help you create your first app in just a few minutes, no coding experience required. You'll use Agent to build an interactive piano from a simple prompt.

<Frame>
  <img src="https://mintcdn.com/replit/CKgy3zbnPnUlDukQ/images/getting-started/quickstart_piano_complete.png?fit=max&auto=format&n=CKgy3zbnPnUlDukQ&q=85&s=76dbd6c44f768c4cb88bd7f1ee51699c" width="500" alt="Interactive piano app with white and black keys" data-og-width="1820" data-og-height="1024" data-path="images/getting-started/quickstart_piano_complete.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/CKgy3zbnPnUlDukQ/images/getting-started/quickstart_piano_complete.png?w=280&fit=max&auto=format&n=CKgy3zbnPnUlDukQ&q=85&s=c6fa3a98918b58530888496d523995a0 280w, https://mintcdn.com/replit/CKgy3zbnPnUlDukQ/images/getting-started/quickstart_piano_complete.png?w=560&fit=max&auto=format&n=CKgy3zbnPnUlDukQ&q=85&s=a63df97df109833b6a781e020e673666 560w, https://mintcdn.com/replit/CKgy3zbnPnUlDukQ/images/getting-started/quickstart_piano_complete.png?w=840&fit=max&auto=format&n=CKgy3zbnPnUlDukQ&q=85&s=8c22f8c1d9c852a10daaeca78b647741 840w, https://mintcdn.com/replit/CKgy3zbnPnUlDukQ/images/getting-started/quickstart_piano_complete.png?w=1100&fit=max&auto=format&n=CKgy3zbnPnUlDukQ&q=85&s=bac9b18817e82741c2c344a7cc6b9d73 1100w, https://mintcdn.com/replit/CKgy3zbnPnUlDukQ/images/getting-started/quickstart_piano_complete.png?w=1650&fit=max&auto=format&n=CKgy3zbnPnUlDukQ&q=85&s=85bf2db7ad259dcad4a892f5c26d4d51 1650w, https://mintcdn.com/replit/CKgy3zbnPnUlDukQ/images/getting-started/quickstart_piano_complete.png?w=2500&fit=max&auto=format&n=CKgy3zbnPnUlDukQ&q=85&s=de405cc4db69ccaca3d0e4c4fadf1b42 2500w" />
</Frame>

## Before you begin

You'll need:

* A free Replit account ([sign up at replit.com](https://replit.com))
* A modern web browser (Chrome, Firefox, Safari, or Edge)

<Note>This tutorial uses Agent, which is included in the free Starter plan with daily credits. No credit card required.</Note>

## Build your piano

<Steps>
  <Step title="Start with an idea">
    **Agent** is Replit's AI that builds apps from natural language. You describe what you want, and Agent writes the code, designs the interface, and creates a working app.

    To communicate with Agent, you write a **prompt** - a text instruction describing what you want to build. Be specific about what you want to build, how you want it to look, and how it will work.

    <PromptAnatomy />
  </Step>

  <Step title="Start building">
    Select **Start** below to open [Replit](https://replit.com) and start building.

    <AgentInput defaultPrompt="Build a realistic 16-key piano with proper white and black key layout that looks exactly like a real piano. Each key should press down with realistic depth animation when clicked and play the correct note." />
  </Step>

  <Step title="Agent builds your piano">
    Agent will set up your app and start building. You'll see real-time updates in the **Progress** tab as Agent creates your piano.

    <Frame>
      <img src="https://mintcdn.com/replit/CKgy3zbnPnUlDukQ/images/getting-started/quickstart_piano_building.png?fit=max&auto=format&n=CKgy3zbnPnUlDukQ&q=85&s=14cb55577a07158f149fe2c3cc8605ed" alt="Progress tab showing Agent building the piano in real-time" data-og-width="1230" width="1230" data-og-height="366" height="366" data-path="images/getting-started/quickstart_piano_building.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/CKgy3zbnPnUlDukQ/images/getting-started/quickstart_piano_building.png?w=280&fit=max&auto=format&n=CKgy3zbnPnUlDukQ&q=85&s=53a33bd2be76297319f28e11d84fa181 280w, https://mintcdn.com/replit/CKgy3zbnPnUlDukQ/images/getting-started/quickstart_piano_building.png?w=560&fit=max&auto=format&n=CKgy3zbnPnUlDukQ&q=85&s=f5048ddbcc69be51d0f48ca331156c6a 560w, https://mintcdn.com/replit/CKgy3zbnPnUlDukQ/images/getting-started/quickstart_piano_building.png?w=840&fit=max&auto=format&n=CKgy3zbnPnUlDukQ&q=85&s=25c2b1e5377bf0a9e4870485e715adf5 840w, https://mintcdn.com/replit/CKgy3zbnPnUlDukQ/images/getting-started/quickstart_piano_building.png?w=1100&fit=max&auto=format&n=CKgy3zbnPnUlDukQ&q=85&s=712d63b27a40dfc96a9abea7be191ee4 1100w, https://mintcdn.com/replit/CKgy3zbnPnUlDukQ/images/getting-started/quickstart_piano_building.png?w=1650&fit=max&auto=format&n=CKgy3zbnPnUlDukQ&q=85&s=8d304873c15c9576bd12bfc427c3a971 1650w, https://mintcdn.com/replit/CKgy3zbnPnUlDukQ/images/getting-started/quickstart_piano_building.png?w=2500&fit=max&auto=format&n=CKgy3zbnPnUlDukQ&q=85&s=5bca0efe01e0d163d4c42fa0d7f102be 2500w" />
    </Frame>

    When Agent finishes, it will show you what it built. The process takes about five minutes.
  </Step>

  <Step title="Play your piano">
    Once Agent completes, navigate to the **Preview** tab to see and interact with your piano.

    Click the keys to hear them play and see the realistic press-down animation.

    <Frame>
      <video autoPlay muted loop playsInline src="https://cdn.replit.com/sanity/quickstart-piano-demo.mp4" />
    </Frame>

    <Note>Your piano design might look slightly different since Agent can generate varied results from the same prompt.</Note>

    ### Try playing a tune

    Use the note names shown on your piano to play "Mary Had a Little Lamb":

    ```
    E D C D E E E
    D D D
    E G G
    E D C D E E E D D E D C
    ```

    Click the keys labeled with these note names to play the tune.

    ### Stretch goal: Add recording

    Want to take it further? Ask Agent to add a record button so you can capture your melody and play it back. Try prompting: "Add a record button that lets me record what I play and a play button to hear it back."
  </Step>
</Steps>

## Continue your journey

Now that you've built your first app, here's what to try next:

* **Build something new**: Try creating a game, drawing app, or anything you can imagine with [Agent](/replitai/agent)
* **Share with friends**: Publish your piano so others can play it. Learn how in [Replit Deployments](/category/replit-deployments)
* **Keep learning**: Learn about [App Mode vs Design Mode](/tutorials/design-vs-build-mode#design-vs-build-mode) to understand when to use each

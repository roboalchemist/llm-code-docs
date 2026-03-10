# Source: https://alexop.dev/prompts/claude/claude-create-slash-command

<!DOCTYPE html><html lang="en" class=" astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/prompts/claude/claude-create-slash-command/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>Create Command: Scaffold New Slash Commands | alexop.dev</title><meta name="title" content="Create Command: Scaffold New Slash Commands | alexop.dev"><meta name="description" content="Interactive agent that scaffolds new slash commands with best practices, proper frontmatter, and structured templates"><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
      document.addEventListener("DOMContentLoaded", function () {
        if (typeof renderMathInElement === "function") {
          renderMathInElement(document.body, {
            delimiters: [
              { left: "$$", right: "$$", display: true },
              { left: "$", right: "$", display: false },
              { left: "\\(", right: "\\)", display: false },
              { left: "\\[", right: "\\]", display: true },
            ],
            throwOnError: false,
            trust: true,
            strict: false,
            output: "html",
          });
        }
      });
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="Create Command: Scaffold New Slash Commands | alexop.dev"><meta property="og:description" content="Interactive agent that scaffolds new slash commands with best practices, proper frontmatter, and structured templates"><meta property="og:url" content="https://alexop.dev/prompts/claude/claude-create-slash-command/"><meta property="og:image" content="https://alexop.dev/prompts/claude/claude-create-slash-command/index.png"><meta property="og:type" content="website"><!-- Article Published/Modified time --><meta property="article:published_time" content="2025-05-22T00:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/prompts/claude/claude-create-slash-command/"><meta property="twitter:title" content="Create Command: Scaffold New Slash Commands | alexop.dev"><meta property="twitter:description" content="Interactive agent that scaffolds new slash commands with best practices, proper frontmatter, and structured templates"><meta property="twitter:image" content="https://alexop.dev/prompts/claude/claude-create-slash-command/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","headline":"Create Command: Scaffold New Slash Commands | alexop.dev","description":"Interactive agent that scaffolds new slash commands with best practices, proper frontmatter, and structured templates","datePublished":"2025-05-22T00:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic","url":"https://alexop.dev"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
<style>.breadcrumb:where(.astro-ilhxcym7){margin-left:auto;margin-right:auto;margin-bottom:.25rem;margin-top:2rem;width:100%;max-width:64rem;padding-left:1rem;padding-right:1rem}.breadcrumb:where(.astro-ilhxcym7) ul:where(.astro-ilhxcym7) li:where(.astro-ilhxcym7){display:inline}.breadcrumb:where(.astro-ilhxcym7) ul:where(.astro-ilhxcym7) li:where(.astro-ilhxcym7) a:where(.astro-ilhxcym7){text-transform:capitalize;opacity:.7}.breadcrumb:where(.astro-ilhxcym7) ul:where(.astro-ilhxcym7) li:where(.astro-ilhxcym7) span:where(.astro-ilhxcym7){opacity:.7}.breadcrumb:where(.astro-ilhxcym7) ul:where(.astro-ilhxcym7) li:where(.astro-ilhxcym7):not(:last-child) a:where(.astro-ilhxcym7):hover{opacity:1}
.prose h1,.prose h2,.prose h3,.prose h4,.prose h5,.prose h6{scroll-margin-top:2rem}.heading-link{margin-left:.5rem;text-decoration-line:none;opacity:0;transition-property:opacity;transition-timing-function:cubic-bezier(.4,0,.2,1);transition-duration:.2s}.heading-link:hover{--tw-text-opacity: 1;color:rgba(var(--color-accent),var(--tw-text-opacity, 1))}.heading-link:focus{opacity:1}.group:hover .heading-link{opacity:1}.heading-link-icon{--tw-text-opacity: 1;color:rgba(var(--color-accent),var(--tw-text-opacity, 1))}
.jazz-demo-root[data-v-1a336f1a]{background:#030712;border:1px solid #374151;border-radius:.75rem;padding:1rem;font-family:system-ui,-apple-system,sans-serif;color:#e5e7eb;font-size:14px}.jazz-demo-header[data-v-1a336f1a]{display:flex;align-items:center;justify-content:space-between;margin-bottom:1rem}.jazz-demo-title[data-v-1a336f1a]{color:#fff;font-size:1rem;font-weight:600}.jazz-demo-toggles[data-v-1a336f1a]{display:flex;align-items:center;gap:.75rem}.jazz-demo-toggle-wrap[data-v-1a336f1a]{display:flex;align-items:center;gap:.5rem}.jazz-demo-toggle-label[data-v-1a336f1a]{color:#d1d5db;font-size:.75rem}.jazz-demo-toggle[data-v-1a336f1a]{position:relative;display:inline-flex;height:1.25rem;width:2.25rem;align-items:center;border-radius:9999px;transition:background-color .2s;border:none;cursor:pointer;padding:0}.jazz-demo-toggle-on[data-v-1a336f1a]{background:#2563eb}.jazz-demo-toggle-off[data-v-1a336f1a]{background:#4b5563}.jazz-demo-toggle-dot[data-v-1a336f1a]{display:inline-block;height:.875rem;width:.875rem;border-radius:9999px;background:#fff;transition:transform .2s}.jazz-demo-toggle-dot-on[data-v-1a336f1a]{transform:translate(1.125rem)}.jazz-demo-toggle-dot-off[data-v-1a336f1a]{transform:translate(.125rem)}.jazz-demo-covalue-id[data-v-1a336f1a]{display:flex;align-items:center;gap:.375rem;margin-bottom:.5rem;padding:.25rem .5rem;background:#1e1b4b;border:1px solid #3730a3;border-radius:.375rem;overflow:hidden}.jazz-demo-covalue-label[data-v-1a336f1a]{color:#a78bfa;font-size:.625rem;font-weight:600;white-space:nowrap}.jazz-demo-covalue-code[data-v-1a336f1a]{color:#c4b5fd;font-size:.625rem;font-family:ui-monospace,monospace;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.jazz-demo-card[data-v-1a336f1a]{background:#111827;border:1px solid #374151;border-radius:.75rem;padding:1rem}.jazz-demo-loading[data-v-1a336f1a]{color:#9ca3af;text-align:center;padding:2rem 0}.jazz-demo-card[data-v-1a336f1a]{padding:1.5rem}.jazz-counter-display[data-v-1a336f1a]{font-size:3rem;font-weight:700;color:#fff;text-align:center;padding:1rem 0;font-variant-numeric:tabular-nums}.jazz-counter-controls[data-v-1a336f1a]{display:flex;gap:.5rem}.jazz-counter-btn[data-v-1a336f1a]{flex:1;padding:.5rem;font-size:1.25rem;font-weight:600;border:1px solid #374151;border-radius:.5rem;background:#1f2937;color:#e5e7eb;cursor:pointer;transition:background-color .2s}.jazz-counter-btn[data-v-1a336f1a]:hover{background:#374151}.jazz-counter-btn-primary[data-v-1a336f1a]{background:#2563eb;border-color:#2563eb;color:#fff}.jazz-counter-btn-primary[data-v-1a336f1a]:hover{background:#1d4ed8}
.jazz-demo-root[data-v-d8349330]{background:#030712;border:1px solid #374151;border-radius:.75rem;padding:1rem;font-family:system-ui,-apple-system,sans-serif;color:#e5e7eb;font-size:14px}.jazz-demo-header[data-v-d8349330]{display:flex;align-items:center;justify-content:space-between;margin-bottom:1rem}.jazz-demo-title[data-v-d8349330]{color:#fff;font-size:1rem;font-weight:600}.jazz-demo-toggles[data-v-d8349330]{display:flex;align-items:center;gap:.75rem}.jazz-demo-toggle-wrap[data-v-d8349330]{display:flex;align-items:center;gap:.5rem}.jazz-demo-toggle-label[data-v-d8349330]{color:#d1d5db;font-size:.75rem}.jazz-demo-toggle[data-v-d8349330]{position:relative;display:inline-flex;height:1.25rem;width:2.25rem;align-items:center;border-radius:9999px;transition:background-color .2s;border:none;cursor:pointer;padding:0}.jazz-demo-toggle-on[data-v-d8349330]{background:#2563eb}.jazz-demo-toggle-off[data-v-d8349330]{background:#4b5563}.jazz-demo-toggle-dot[data-v-d8349330]{display:inline-block;height:.875rem;width:.875rem;border-radius:9999px;background:#fff;transition:transform .2s}.jazz-demo-toggle-dot-on[data-v-d8349330]{transform:translate(1.125rem)}.jazz-demo-toggle-dot-off[data-v-d8349330]{transform:translate(.125rem)}.jazz-demo-covalue-id[data-v-d8349330]{display:flex;align-items:center;gap:.375rem;margin-bottom:.5rem;padding:.25rem .5rem;background:#1e1b4b;border:1px solid #3730a3;border-radius:.375rem;overflow:hidden}.jazz-demo-covalue-label[data-v-d8349330]{color:#a78bfa;font-size:.625rem;font-weight:600;white-space:nowrap}.jazz-demo-covalue-code[data-v-d8349330]{color:#c4b5fd;font-size:.625rem;font-family:ui-monospace,monospace;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.jazz-demo-card[data-v-d8349330]{background:#111827;border:1px solid #374151;border-radius:.75rem;padding:1rem}.jazz-demo-loading[data-v-d8349330]{color:#9ca3af;text-align:center;padding:2rem 0}.jazz-demo-card-title[data-v-d8349330]{font-size:1.25rem;font-weight:700;color:#fff;margin:0 0 .75rem}.jazz-demo-form[data-v-d8349330]{margin-bottom:.75rem;display:flex;flex-direction:column;gap:.5rem}.jazz-demo-input[data-v-d8349330]{width:100%;padding:.375rem .625rem;background:#1f2937;border:1px solid #4b5563;border-radius:.5rem;color:#fff;font-size:.8125rem;outline:none;box-sizing:border-box}.jazz-demo-input[data-v-d8349330]:focus{border-color:#3b82f6;box-shadow:0 0 0 2px #3b82f64d}.jazz-demo-input[data-v-d8349330]::-moz-placeholder{color:#6b7280}.jazz-demo-input[data-v-d8349330]::placeholder{color:#6b7280}.jazz-demo-add-btn[data-v-d8349330]{width:100%;padding:.375rem .75rem;background:#2563eb;color:#fff;border:none;border-radius:.5rem;font-weight:500;font-size:.8125rem;cursor:pointer;transition:background-color .2s}.jazz-demo-add-btn[data-v-d8349330]:hover{background:#1d4ed8}.jazz-demo-list[data-v-d8349330]{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:.25rem}.jazz-demo-item[data-v-d8349330]{display:flex;align-items:center;gap:.5rem;padding:.375rem;border-radius:.5rem}.jazz-demo-item[data-v-d8349330]:hover{background:#1f2937}.jazz-demo-item:hover .jazz-demo-delete[data-v-d8349330]{opacity:1}.jazz-demo-drag[data-v-d8349330]{cursor:grab;color:#4b5563;transition:color .2s;-webkit-user-select:none;-moz-user-select:none;user-select:none;display:flex;align-items:center}.jazz-demo-drag[data-v-d8349330]:active{cursor:grabbing}.jazz-demo-item:hover .jazz-demo-drag[data-v-d8349330]{color:#9ca3af}.jazz-demo-svg[data-v-d8349330]{width:1rem;height:1rem}.jazz-demo-checkbox[data-v-d8349330]{width:.875rem;height:.875rem;accent-color:#2563eb}.jazz-demo-text[data-v-d8349330]{flex:1;color:#e5e7eb;font-size:.8125rem}.jazz-demo-text-done[data-v-d8349330]{text-decoration:line-through;color:#6b7280}.jazz-demo-delete[data-v-d8349330]{opacity:0;transition:opacity .2s;color:#6b7280;background:none;border:none;padding:.125rem;cursor:pointer;display:flex;align-items:center}.jazz-demo-delete[data-v-d8349330]:hover{color:#f87171}.jazz-demo-empty[data-v-d8349330]{color:#6b7280;text-align:center;padding:1rem 0;margin:0;font-size:.8125rem}
</style></head> <body class="astro-sckkx6r4"> <div class="conference-wrapper border-b border-skin-line bg-skin-fill px-4 py-3 text-center text-skin-base astro-z2v4rtzb"><div class="mx-auto flex max-w-3xl flex-col items-center justify-center gap-3 sm:flex-row sm:gap-4 astro-z2v4rtzb"><div class="text-center sm:text-left astro-z2v4rtzb"><p class="text-lg font-semibold astro-z2v4rtzb"><span class="pulse-dot astro-z2v4rtzb"></span>
Next Talk: How to Build Local-First Apps with Vue</p><p class="text-sm opacity-80 astro-z2v4rtzb">March 12, 2026 — Vue.js Amsterdam</p></div><a href="https://vuejs.amsterdam/" class="conference-button inline-flex transform items-center justify-center gap-2 whitespace-nowrap rounded-md bg-skin-card px-4 py-2 font-medium text-skin-accent shadow transition-all duration-200 ease-in-out hover:scale-105 hover:bg-skin-card-muted hover:shadow-md astro-z2v4rtzb" target="_blank" rel="noopener noreferrer"><svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 astro-z2v4rtzb" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" class="astro-z2v4rtzb"></path><polyline points="15 3 21 3 21 9" class="astro-z2v4rtzb"></polyline><line x1="10" y1="14" x2="21" y2="3" class="astro-z2v4rtzb"></line></svg>
Conference
</a></div></div>  <header class="astro-3ef6ksr2"> <a id="skip-to-content" href="#main-content" class="astro-3ef6ksr2">Skip to content</a> <div class="nav-container astro-3ef6ksr2"> <div class="top-nav-wrap astro-3ef6ksr2"> <a href="/" class="logo whitespace-nowrap astro-3ef6ksr2"> alexop.dev </a> <nav id="nav-menu" aria-label="Main" class="astro-3ef6ksr2"> <button class="hamburger-menu focus-outline astro-3ef6ksr2" aria-label="Open Menu" aria-expanded="false" aria-controls="menu-items"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="menu-icon astro-3ef6ksr2"> <line x1="7" y1="12" x2="21" y2="12" class="line astro-3ef6ksr2"></line> <line x1="3" y1="6" x2="21" y2="6" class="line astro-3ef6ksr2"></line> <line x1="12" y1="18" x2="21" y2="18" class="line astro-3ef6ksr2"></line> <line x1="18" y1="6" x2="6" y2="18" class="close astro-3ef6ksr2"></line> <line x1="6" y1="6" x2="18" y2="18" class="close astro-3ef6ksr2"></line> </svg> </button> <ul id="menu-items" class="display-none sm:flex astro-3ef6ksr2"> <li class="astro-3ef6ksr2"> <a href="/posts/" class=" astro-3ef6ksr2">
📝 Posts
</a> </li> <li class="astro-3ef6ksr2"> <a href="/tils/" class=" astro-3ef6ksr2">
💡 TILs
</a> </li> <li class="astro-3ef6ksr2"> <a href="/notes/" class=" astro-3ef6ksr2">
📔 Notes
</a> </li> <li class="astro-3ef6ksr2"> <a href="/talks/" class=" astro-3ef6ksr2">
🎤 Talks
</a> </li> <li class="astro-3ef6ksr2"> <a href="/projects/" class=" astro-3ef6ksr2">
🚀 Projects
</a> </li> <li class="astro-3ef6ksr2"> <a href="/prompts/" class="active astro-3ef6ksr2">
🤖 Prompts
</a> </li> <li class="astro-3ef6ksr2"> <a href="/tags/" class=" astro-3ef6ksr2">
🏷️ Tags
</a> </li> <li class="astro-3ef6ksr2"> <a href="/about/" class=" astro-3ef6ksr2">
👤 About
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <nav class="breadcrumb astro-ilhxcym7" aria-label="breadcrumb"> <ul class="astro-ilhxcym7"> <li class="astro-ilhxcym7"> <a href="/" class="astro-ilhxcym7">Home</a> <span aria-hidden="true" class="astro-ilhxcym7">&raquo;</span> </li> <li class="astro-ilhxcym7"> <a href="/prompts/" class="astro-ilhxcym7">prompts</a> <span aria-hidden="true" class="astro-ilhxcym7">&raquo;</span> </li><li class="astro-ilhxcym7"> <a href="/claude/" class="astro-ilhxcym7">claude</a> <span aria-hidden="true" class="astro-ilhxcym7">&raquo;</span> </li><li class="astro-ilhxcym7"> <span class="lowercase astro-ilhxcym7" aria-current="page">  claude-create-slash-command </span> </li> </ul> </nav>  <main id="main-content" class="mx-auto max-w-4xl px-4 pb-12 pt-8"> <!-- Back Link --> <div class="mb-6"> <a href="/prompts/claude/" class="focus:ring-skin-accent inline-flex items-center gap-1 rounded-md px-3 py-1.5 text-sm text-skin-accent transition-colors hover:bg-skin-card focus:outline-none focus:ring-2 focus:ring-offset-2" onclick="event.preventDefault(); history.back();">
← Back to Claude Prompts
</a> </div> <!-- Header --> <header class="mb-8"> <h1 class="mb-4 text-3xl font-bold text-skin-base">Create Command: Scaffold New Slash Commands</h1> <div class="mb-4 flex flex-wrap items-center gap-2"> <span class="inline-block rounded-md bg-skin-card px-2 py-1 text-xs " role="img" aria-label="Category: Agent"><span aria-hidden="true">🤖</span> <!-- -->Agent</span> <span class="inline-block rounded-md bg-skin-card px-2 py-1 text-xs"> Claude </span> <span class="text-sm text-skin-base/70">Claude Sonnet</span> </div> <div class="flex flex-wrap gap-2"> <a href="/prompts/?q=claude-code" class="text-sm text-skin-base/70 transition-colors hover:text-skin-accent hover:underline">
#claude-code </a><a href="/prompts/?q=slash-commands" class="text-sm text-skin-base/70 transition-colors hover:text-skin-accent hover:underline">
#slash-commands </a><a href="/prompts/?q=automation" class="text-sm text-skin-base/70 transition-colors hover:text-skin-accent hover:underline">
#automation </a><a href="/prompts/?q=scaffolding" class="text-sm text-skin-base/70 transition-colors hover:text-skin-accent hover:underline">
#scaffolding </a> </div> </header> <!-- Description and Metadata --> <section class="mb-8"> <p class="mb-4 text-skin-base">Interactive agent that scaffolds new slash commands with best practices, proper frontmatter, and structured templates</p> <dl class="space-y-2 text-sm text-skin-base/70"> <div> <dt class="inline font-medium text-skin-base">
💡 Use Case:
</dt> <dd class="ml-2 inline">Creating new slash commands for Claude Code with consistent structure and patterns</dd> </div> <div> <dt class="inline font-medium text-skin-base">
📤 Expected Output:
</dt> <dd class="ml-2 inline">A complete slash command file with frontmatter, context blocks, and instructions</dd> </div>  </dl> </section> <!-- Prompt Content --> <section class="mb-8"> <div class="mb-4 flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between"> <h2 class="text-lg font-semibold text-skin-base">Prompt Content</h2> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="1Rh1h4" prefix="r3" component-url="/_astro/prompts.BTh7qZgL.js" component-export="PromptCopyButton" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;content&quot;:[0,&quot;## Create Command: Scaffold New Slash Commands\n\nAn interactive agent that guides you through creating well-structured slash commands for Claude Code. It asks the right questions and generates commands following proven patterns.\n\n## Purpose\n\nCreating effective slash commands requires understanding frontmatter options, context gathering patterns, and instruction structures. This agent encapsulates best practices so you can create powerful commands quickly without memorizing the format.\n\n## Instructions\n\n### Step 1: Gather Requirements\n\nAsk the user these questions:\n\n**Question 1: Command Category**\nWhat category best describes this command?\n\n| Category | Description | Defaults |\n|----------|-------------|----------|\n| `git-workflow` | Git operations (commit, branch, push, merge) | `model: haiku`, git tools |\n| `github` | GitHub operations (PR, issues, CI) | `model: haiku`, gh + git tools |\n| `quality` | Linting, testing, type checking | test/lint tools |\n| `debugging` | Fix errors, investigate issues | full tools, decision trees |\n| `code-transform` | Refactoring, code generation | full tools, file references |\n| `utility` | General purpose automation | varies |\n\n**Question 2: Arguments**\nDoes this command need arguments?\n\n| Option | Syntax | Example |\n|--------|--------|---------|\n| None | (no arguments) | `/lint` |\n| Single required | `$1` | `/review-pr 123` |\n| Multiple positional | `$1`, `$2`, `$3` | `/deploy staging v1.2.3` |\n| Free-form text | `$ARGUMENTS` | `/branch add dark mode toggle` |\n\n**Question 3: File References**\nDoes the command operate on specific files?\n\n- **Yes** - Use `@$1` syntax to reference file contents\n- **No** - Command works on general context\n\n**Question 4: Complexity**\nHow complex is the workflow?\n\n| Level | Characteristics | Structure |\n|-------|-----------------|-----------|\n| `simple` | Run command, report result | Linear steps |\n| `linear` | Sequential steps, no branching | Numbered instructions |\n| `branching` | Pre-checks, multiple paths | Decision tree |\n| `complex` | Multi-phase, verification, fallback | Full protocol with red flags |\n\n### Step 2: Generate Command File\n\nBased on the answers, generate the command file with:\n\n**Frontmatter:**\n```yaml\n---\ndescription: &lt;imperative verb phrase&gt;\nargument-hint: &lt;show expected args&gt;\nallowed-tools: &lt;category defaults&gt;\nmodel: &lt;haiku for routine, omit for complex&gt;\n---\n```\n\n**Context Blocks** using semantic XML tags:\n```markdown\n&lt;current_branch&gt;\n!`git branch --show-current`\n&lt;/current_branch&gt;\n```\n\n**Structure Templates** based on complexity level.\n\n### Step 3: Write the File\n\n1. Write the file to `.claude/commands/&lt;name&gt;.md`\n2. Show the user the generated command\n3. Explain how to use it\n\n## Expected Output\n\n- **Format:** Complete markdown file with YAML frontmatter\n- **Key sections:**\n  - Frontmatter with description, tools, model\n  - Context blocks with shell commands\n  - Decision tree (if branching/complex)\n  - Numbered instructions\n  - Red flags section (if complex)\n\n## Example\n\n**Input:**\n```\n/create-command deploy \&quot;Deploy to staging or production environment\&quot;\n```\n\n**Output:**\nA complete command file at `.claude/commands/deploy.md` with:\n- Proper frontmatter for deployment category\n- Context blocks for git status, current branch, latest tag\n- Decision tree handling uncommitted changes\n- Instructions for build and deploy steps\n\n## Done When\n\n- [ ] User requirements gathered via questions\n- [ ] Command file generated with correct frontmatter\n- [ ] Context blocks use appropriate shell commands\n- [ ] Instructions match complexity level\n- [ ] File written to `.claude/commands/`&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PromptCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus:ring-skin-accent/20 inline-flex items-center gap-2 whitespace-nowrap rounded-lg border-2 border-skin-line bg-skin-card px-4 py-2.5 text-sm font-medium text-skin-base shadow-sm transition-all hover:border-skin-accent/50 hover:text-skin-accent focus:border-skin-accent focus:outline-none focus:ring-2" aria-label="Copy prompt to clipboard"><svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg>Copy Prompt</button><!--astro:end--></astro-island> </div> <div class="overflow-x-auto rounded-md border border-skin-line bg-skin-card p-4"> <div class="prose prose-sm max-w-none text-skin-base prose-headings:text-skin-base prose-p:text-skin-base prose-a:text-skin-accent prose-strong:text-skin-base prose-code:text-skin-base prose-pre:bg-skin-fill"> <h2 id="create-command-scaffold-new-slash-commands">Create Command: Scaffold New Slash Commands<a class="heading-link" aria-label="Link to section" href="#create-command-scaffold-new-slash-commands"><span class="heading-link-icon">#</span></a></h2>
<p>An interactive agent that guides you through creating well-structured slash commands for Claude Code. It asks the right questions and generates commands following proven patterns.</p>
<h2 id="purpose">Purpose<a class="heading-link" aria-label="Link to section" href="#purpose"><span class="heading-link-icon">#</span></a></h2>
<p>Creating effective slash commands requires understanding frontmatter options, context gathering patterns, and instruction structures. This agent encapsulates best practices so you can create powerful commands quickly without memorizing the format.</p>
<h2 id="instructions">Instructions<a class="heading-link" aria-label="Link to section" href="#instructions"><span class="heading-link-icon">#</span></a></h2>
<h3 id="step-1-gather-requirements">Step 1: Gather Requirements<a class="heading-link" aria-label="Link to section" href="#step-1-gather-requirements"><span class="heading-link-icon">#</span></a></h3>
<p>Ask the user these questions:</p>
<p><strong>Question 1: Command Category</strong>
What category best describes this command?</p>








































<table><thead><tr><th>Category</th><th>Description</th><th>Defaults</th></tr></thead><tbody><tr><td data-label="Category"><code>git-workflow</code></td><td data-label="Description">Git operations (commit, branch, push, merge)</td><td data-label="Defaults"><code>model: haiku</code>, git tools</td></tr><tr><td data-label="Category"><code>github</code></td><td data-label="Description">GitHub operations (PR, issues, CI)</td><td data-label="Defaults"><code>model: haiku</code>, gh + git tools</td></tr><tr><td data-label="Category"><code>quality</code></td><td data-label="Description">Linting, testing, type checking</td><td data-label="Defaults">test/lint tools</td></tr><tr><td data-label="Category"><code>debugging</code></td><td data-label="Description">Fix errors, investigate issues</td><td data-label="Defaults">full tools, decision trees</td></tr><tr><td data-label="Category"><code>code-transform</code></td><td data-label="Description">Refactoring, code generation</td><td data-label="Defaults">full tools, file references</td></tr><tr><td data-label="Category"><code>utility</code></td><td data-label="Description">General purpose automation</td><td data-label="Defaults">varies</td></tr></tbody></table>
<p><strong>Question 2: Arguments</strong>
Does this command need arguments?</p>






























<table><thead><tr><th>Option</th><th>Syntax</th><th>Example</th></tr></thead><tbody><tr><td data-label="Option">None</td><td data-label="Syntax">(no arguments)</td><td data-label="Example"><code>/lint</code></td></tr><tr><td data-label="Option">Single required</td><td data-label="Syntax"><code>$1</code></td><td data-label="Example"><code>/review-pr 123</code></td></tr><tr><td data-label="Option">Multiple positional</td><td data-label="Syntax"><code>$1</code>, <code>$2</code>, <code>$3</code></td><td data-label="Example"><code>/deploy staging v1.2.3</code></td></tr><tr><td data-label="Option">Free-form text</td><td data-label="Syntax"><code>$ARGUMENTS</code></td><td data-label="Example"><code>/branch add dark mode toggle</code></td></tr></tbody></table>
<p><strong>Question 3: File References</strong>
Does the command operate on specific files?</p>
<ul>
<li><strong>Yes</strong> - Use <code>@$1</code> syntax to reference file contents</li>
<li><strong>No</strong> - Command works on general context</li>
</ul>
<p><strong>Question 4: Complexity</strong>
How complex is the workflow?</p>






























<table><thead><tr><th>Level</th><th>Characteristics</th><th>Structure</th></tr></thead><tbody><tr><td data-label="Level"><code>simple</code></td><td data-label="Characteristics">Run command, report result</td><td data-label="Structure">Linear steps</td></tr><tr><td data-label="Level"><code>linear</code></td><td data-label="Characteristics">Sequential steps, no branching</td><td data-label="Structure">Numbered instructions</td></tr><tr><td data-label="Level"><code>branching</code></td><td data-label="Characteristics">Pre-checks, multiple paths</td><td data-label="Structure">Decision tree</td></tr><tr><td data-label="Level"><code>complex</code></td><td data-label="Characteristics">Multi-phase, verification, fallback</td><td data-label="Structure">Full protocol with red flags</td></tr></tbody></table>
<h3 id="step-2-generate-command-file">Step 2: Generate Command File<a class="heading-link" aria-label="Link to section" href="#step-2-generate-command-file"><span class="heading-link-icon">#</span></a></h3>
<p>Based on the answers, generate the command file with:</p>
<p><strong>Frontmatter:</strong></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="yaml"><code><span class="line"><span style="color:#A9B1D6">---</span></span>
<span class="line"><span style="color:#F7768E">description</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> &#x3C;imperative verb phrase></span></span>
<span class="line"><span style="color:#F7768E">argument-hint</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> &#x3C;show expected args></span></span>
<span class="line"><span style="color:#F7768E">allowed-tools</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> &#x3C;category defaults></span></span>
<span class="line"><span style="color:#F7768E">model</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> &#x3C;haiku for routine, omit for complex></span></span>
<span class="line"><span style="color:#A9B1D6">---</span></span></code><button type="button" class="copy" data-code="---
description: <imperative verb phrase>
argument-hint: <show expected args>
allowed-tools: <category defaults>
model: <haiku for routine, omit for complex>
---" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><strong>Context Blocks</strong> using semantic XML tags:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#9AA5CE">&#x3C;current_branch></span></span>
<span class="line"><span style="color:#9AA5CE">!</span><span style="color:#89DDFF">`git branch --show-current`</span></span>
<span class="line"><span style="color:#9AA5CE">&#x3C;/current_branch></span></span></code><button type="button" class="copy" data-code="<current_branch>
!&#x60;git branch --show-current&#x60;
</current_branch>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><strong>Structure Templates</strong> based on complexity level.</p>
<h3 id="step-3-write-the-file">Step 3: Write the File<a class="heading-link" aria-label="Link to section" href="#step-3-write-the-file"><span class="heading-link-icon">#</span></a></h3>
<ol>
<li>Write the file to <code>.claude/commands/&#x3C;name>.md</code></li>
<li>Show the user the generated command</li>
<li>Explain how to use it</li>
</ol>
<h2 id="expected-output">Expected Output<a class="heading-link" aria-label="Link to section" href="#expected-output"><span class="heading-link-icon">#</span></a></h2>
<ul>
<li><strong>Format:</strong> Complete markdown file with YAML frontmatter</li>
<li><strong>Key sections:</strong>
<ul>
<li>Frontmatter with description, tools, model</li>
<li>Context blocks with shell commands</li>
<li>Decision tree (if branching/complex)</li>
<li>Numbered instructions</li>
<li>Red flags section (if complex)</li>
</ul>
</li>
</ul>
<h2 id="example">Example<a class="heading-link" aria-label="Link to section" href="#example"><span class="heading-link-icon">#</span></a></h2>
<p><strong>Input:</strong></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="plaintext"><code><span class="line"><span>/create-command deploy "Deploy to staging or production environment"</span></span></code><button type="button" class="copy" data-code="/create-command deploy &#x22;Deploy to staging or production environment&#x22;" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><strong>Output:</strong>
A complete command file at <code>.claude/commands/deploy.md</code> with:</p>
<ul>
<li>Proper frontmatter for deployment category</li>
<li>Context blocks for git status, current branch, latest tag</li>
<li>Decision tree handling uncommitted changes</li>
<li>Instructions for build and deploy steps</li>
</ul>
<h2 id="done-when">Done When<a class="heading-link" aria-label="Link to section" href="#done-when"><span class="heading-link-icon">#</span></a></h2>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> User requirements gathered via questions</li>
<li class="task-list-item"><input type="checkbox" disabled> Command file generated with correct frontmatter</li>
<li class="task-list-item"><input type="checkbox" disabled> Context blocks use appropriate shell commands</li>
<li class="task-list-item"><input type="checkbox" disabled> Instructions match complexity level</li>
<li class="task-list-item"><input type="checkbox" disabled> File written to <code>.claude/commands/</code></li>
</ul> </div> </div> </section> <!-- Usage Hint --> <aside class="text-sm text-skin-base/70"> <p>
💡 <strong class="text-skin-base">Tip:</strong> Click "Copy Prompt" to copy
        the entire content including any frontmatter.
 Save this to your `.claude/` directory to use it. </p> </aside> </main> <footer class="mt-auto astro-sz7xmlte"> <div class="max-w-5xl mx-auto px-4"> <hr class="border-skin-line" aria-hidden="true"> </div> <div class="footer-wrapper astro-sz7xmlte"> <div class="footer-content astro-sz7xmlte"> <div class="copyright-wrapper astro-sz7xmlte"> <span class="astro-sz7xmlte">Copyright &#169; 2026</span> <span class="separator astro-sz7xmlte">&nbsp;|&nbsp;</span> <span class="astro-sz7xmlte">All rights reserved.</span> </div> <div class="rss-prompt astro-sz7xmlte"> <a href="/rss.xml" class="rss-link group astro-sz7xmlte" title="Never miss a post - Subscribe via RSS" onclick="if (window.plausible) window.plausible('RSS Subscribe', { props: { location: 'footer' } })"> <div class="flex items-center gap-2 astro-sz7xmlte"> <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-skin-accent group-hover:animate-pulse astro-sz7xmlte"><path fill="currentColor" d="M19 20.001C19 11.729 12.271 5 4 5v2c7.168 0 13 5.832 13 13.001h2z" class="astro-sz7xmlte"></path><path fill="currentColor" d="M12 20.001h2C14 14.486 9.514 10 4 10v2c4.411 0 8 3.589 8 8.001z" class="astro-sz7xmlte"></path><circle cx="6" cy="18" r="2" fill="currentColor" class="astro-sz7xmlte"></circle> </svg> <span class="text-sm astro-sz7xmlte">Subscribe via RSS</span> </div> </a> </div> <div class="social-icons flex astro-upu6fzxr"> <a href="https://github.com/alexanderop" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title=" alexop.dev on Github" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M9 19c-4.3 1.4 -4.3 -2.5 -6 -3m12 5v-3.5c0 -1 .1 -1.4 -.5 -2c2.8 -.3 5.5 -1.4 5.5 -6a4.6 4.6 0 0 0 -1.3 -3.2a4.2 4.2 0 0 0 -.1 -3.2s-1.1 -.3 -3.5 1.3a12.3 12.3 0 0 0 -6.2 0c-2.4 -1.6 -3.5 -1.3 -3.5 -1.3a4.2 4.2 0 0 0 -.1 3.2a4.6 4.6 0 0 0 -1.3 3.2c0 4.6 2.7 5.7 5.5 6c-.6 .6 -.6 1.2 -.5 2v3.5"
    ></path>
  </svg> <span class="sr-only astro-upu6fzxr"> alexop.dev on Github</span> </a><a href="https://de.linkedin.com/in/alexander-opalic-55464a169" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title="alexop.dev on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <rect x="4" y="4" width="16" height="16" rx="2"></rect>
    <line x1="8" y1="11" x2="8" y2="16"></line>
    <line x1="8" y1="8" x2="8" y2="8.01"></line>
    <line x1="12" y1="16" x2="12" y2="11"></line>
    <path d="M16 16v-3a2 2 0 0 0 -4 0"></path>
  </svg> <span class="sr-only astro-upu6fzxr">alexop.dev on LinkedIn</span> </a><a href="mailto:alex.opalic.dev@gmail.com" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title="Send an email to alexop.dev" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-upu6fzxr">Send an email to alexop.dev</span> </a><a href="https://twitter.com/alexanderopalic" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title="alexop.dev on X" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-upu6fzxr">alexop.dev on X</span> </a><a href="https://bsky.app/profile/alexvue.bsky.social" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title="alexop.dev on BlueSky" target="_blank" rel="noopener noreferrer"> <svg 
      xmlns="http://www.w3.org/2000/svg" 
      class="icon-tabler" 
      viewBox="0 0 64 57"
    >
      <path fill="none" stroke="currentColor" stroke-width="2" d="M13.873 3.805C21.21 9.332 29.103 20.537 32 26.55v15.882c0-.338-.13.044-.41.867-1.512 4.456-7.418 21.847-20.923 7.944-7.111-7.32-3.819-14.64 9.125-16.85-7.405 1.264-15.73-.825-18.014-9.015C1.12 23.022 0 8.51 0 6.55 0-3.268 8.579-.182 13.873 3.805ZM50.127 3.805C42.79 9.332 34.897 20.537 32 26.55v15.882c0-.338.13.044.41.867 1.512 4.456 7.418 21.847 20.923 7.944 7.111-7.32 3.819-14.64-9.125-16.85 7.405 1.264 15.73-.825 18.014-9.015C62.88 23.022 64 8.51 64 6.55c0-9.818-8.578-6.732-13.873-2.745Z"></path>
    </svg> <span class="sr-only astro-upu6fzxr">alexop.dev on BlueSky</span> </a> </div>  </div> <div class="license-info astro-sz7xmlte"> <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener noreferrer" class="cc-license astro-sz7xmlte"> <img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" alt="CC" class="cc-icon astro-sz7xmlte"> <img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" alt="BY" class="cc-icon astro-sz7xmlte">
Content licensed under CC BY 4.0
</a> </div> <div class="legal-links astro-sz7xmlte"> <a href="/imprint/" class="legal-link astro-sz7xmlte"> Imprint </a> <span class="separator astro-sz7xmlte">|</span> <a href="/data-privacy/" class="legal-link astro-sz7xmlte"> Data Privacy </a> </div> </div> </footer>   <!-- Wiki link preview card hover script --> <script>
      function initInternalLinks() {
        const wrappers = document.querySelectorAll(".internal-link-wrapper");

        wrappers.forEach(wrapper => {
          const card = wrapper.querySelector(".preview-card");
          const link = wrapper.querySelector(".internal-link");
          if (!card || !link) return;

          // Skip if already initialized
          if (wrapper.dataset.initialized === "true") return;
          wrapper.dataset.initialized = "true";

          // Function to hide the card
          const hideCard = () => {
            card.classList.remove("is-fixed");
            card.style.removeProperty("--pc-top");
            card.style.removeProperty("--pc-left");
            card.style.opacity = "";
            card.style.visibility = "";
            // Remove scroll listener when hiding
            window.removeEventListener("scroll", hideCard);
          };

          wrapper.addEventListener("mouseenter", () => {
            // Make visible first so it has size
            card.style.opacity = "1";
            card.style.visibility = "visible";

            // Use fixed positioning to escape overflow clipping
            const linkRect = link.getBoundingClientRect();
            const cardRect = card.getBoundingClientRect();

            // Position above by default; flip below if too close to top
            const aboveTop = linkRect.top - 8 - cardRect.height;
            const belowTop = linkRect.bottom + 8;
            const top = aboveTop < 10 ? belowTop : aboveTop;

            // Center horizontally on the link
            const left = linkRect.left + linkRect.width / 2 - cardRect.width / 2;

            // Constrain to viewport
            const vw = document.documentElement.clientWidth;
            const safeLeft = Math.max(8, Math.min(left, vw - cardRect.width - 8));

            // Apply fixed position with coordinates
            card.classList.add("is-fixed");
            card.style.setProperty("--pc-top", `${Math.round(top)}px`);
            card.style.setProperty("--pc-left", `${Math.round(safeLeft)}px`);

            // Hide card on scroll
            window.addEventListener("scroll", hideCard, { passive: true });
          });

          wrapper.addEventListener("mouseleave", hideCard);
        });
      }

      // Initialize on both initial load and after client-side navigation
      document.addEventListener("astro:page-load", initInternalLinks);
    </script> </body> </html>  <script>
  /** Make headings groups for hover effect on anchor links */
  function makeHeadingsGroups() {
    const headings = Array.from(
      document.querySelectorAll(".prose h2, .prose h3, .prose h4, .prose h5, .prose h6")
    );
    for (const heading of headings) {
      heading.classList.add("group");
    }
  }

  // Run after DOM is loaded
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", makeHeadingsGroups);
  } else {
    makeHeadingsGroups();
  }
</script>
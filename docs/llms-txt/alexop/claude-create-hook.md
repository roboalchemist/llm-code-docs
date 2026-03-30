# Source: https://alexop.dev/prompts/claude/claude-create-hook

<!DOCTYPE html><html lang="en" class=" astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/prompts/claude/claude-create-hook/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>Create Hook | alexop.dev</title><meta name="title" content="Create Hook | alexop.dev"><meta name="description" content="Slash command to create and configure Claude Code hooks with reference documentation and interactive guidance"><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="Create Hook | alexop.dev"><meta property="og:description" content="Slash command to create and configure Claude Code hooks with reference documentation and interactive guidance"><meta property="og:url" content="https://alexop.dev/prompts/claude/claude-create-hook/"><meta property="og:image" content="https://alexop.dev/prompts/claude/claude-create-hook/index.png"><meta property="og:type" content="website"><!-- Article Published/Modified time --><meta property="article:published_time" content="2025-11-16T00:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/prompts/claude/claude-create-hook/"><meta property="twitter:title" content="Create Hook | alexop.dev"><meta property="twitter:description" content="Slash command to create and configure Claude Code hooks with reference documentation and interactive guidance"><meta property="twitter:image" content="https://alexop.dev/prompts/claude/claude-create-hook/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","headline":"Create Hook | alexop.dev","description":"Slash command to create and configure Claude Code hooks with reference documentation and interactive guidance","datePublished":"2025-11-16T00:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic","url":"https://alexop.dev"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
<style>.breadcrumb:where(.astro-ilhxcym7){margin-left:auto;margin-right:auto;margin-bottom:.25rem;margin-top:2rem;width:100%;max-width:64rem;padding-left:1rem;padding-right:1rem}.breadcrumb:where(.astro-ilhxcym7) ul:where(.astro-ilhxcym7) li:where(.astro-ilhxcym7){display:inline}.breadcrumb:where(.astro-ilhxcym7) ul:where(.astro-ilhxcym7) li:where(.astro-ilhxcym7) a:where(.astro-ilhxcym7){text-transform:capitalize;opacity:.7}.breadcrumb:where(.astro-ilhxcym7) ul:where(.astro-ilhxcym7) li:where(.astro-ilhxcym7) span:where(.astro-ilhxcym7){opacity:.7}.breadcrumb:where(.astro-ilhxcym7) ul:where(.astro-ilhxcym7) li:where(.astro-ilhxcym7):not(:last-child) a:where(.astro-ilhxcym7):hover{opacity:1}
.prose h1,.prose h2,.prose h3,.prose h4,.prose h5,.prose h6{scroll-margin-top:2rem}.heading-link{margin-left:.5rem;text-decoration-line:none;opacity:0;transition-property:opacity;transition-timing-function:cubic-bezier(.4,0,.2,1);transition-duration:.2s}.heading-link:hover{--tw-text-opacity: 1;color:rgba(var(--color-accent),var(--tw-text-opacity, 1))}.heading-link:focus{opacity:1}.group:hover .heading-link{opacity:1}.heading-link-icon{--tw-text-opacity: 1;color:rgba(var(--color-accent),var(--tw-text-opacity, 1))}
.jazz-demo-root[data-v-d8349330]{background:#030712;border:1px solid #374151;border-radius:.75rem;padding:1rem;font-family:system-ui,-apple-system,sans-serif;color:#e5e7eb;font-size:14px}.jazz-demo-header[data-v-d8349330]{display:flex;align-items:center;justify-content:space-between;margin-bottom:1rem}.jazz-demo-title[data-v-d8349330]{color:#fff;font-size:1rem;font-weight:600}.jazz-demo-toggles[data-v-d8349330]{display:flex;align-items:center;gap:.75rem}.jazz-demo-toggle-wrap[data-v-d8349330]{display:flex;align-items:center;gap:.5rem}.jazz-demo-toggle-label[data-v-d8349330]{color:#d1d5db;font-size:.75rem}.jazz-demo-toggle[data-v-d8349330]{position:relative;display:inline-flex;height:1.25rem;width:2.25rem;align-items:center;border-radius:9999px;transition:background-color .2s;border:none;cursor:pointer;padding:0}.jazz-demo-toggle-on[data-v-d8349330]{background:#2563eb}.jazz-demo-toggle-off[data-v-d8349330]{background:#4b5563}.jazz-demo-toggle-dot[data-v-d8349330]{display:inline-block;height:.875rem;width:.875rem;border-radius:9999px;background:#fff;transition:transform .2s}.jazz-demo-toggle-dot-on[data-v-d8349330]{transform:translate(1.125rem)}.jazz-demo-toggle-dot-off[data-v-d8349330]{transform:translate(.125rem)}.jazz-demo-covalue-id[data-v-d8349330]{display:flex;align-items:center;gap:.375rem;margin-bottom:.5rem;padding:.25rem .5rem;background:#1e1b4b;border:1px solid #3730a3;border-radius:.375rem;overflow:hidden}.jazz-demo-covalue-label[data-v-d8349330]{color:#a78bfa;font-size:.625rem;font-weight:600;white-space:nowrap}.jazz-demo-covalue-code[data-v-d8349330]{color:#c4b5fd;font-size:.625rem;font-family:ui-monospace,monospace;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.jazz-demo-card[data-v-d8349330]{background:#111827;border:1px solid #374151;border-radius:.75rem;padding:1rem}.jazz-demo-loading[data-v-d8349330]{color:#9ca3af;text-align:center;padding:2rem 0}.jazz-demo-card-title[data-v-d8349330]{font-size:1.25rem;font-weight:700;color:#fff;margin:0 0 .75rem}.jazz-demo-form[data-v-d8349330]{margin-bottom:.75rem;display:flex;flex-direction:column;gap:.5rem}.jazz-demo-input[data-v-d8349330]{width:100%;padding:.375rem .625rem;background:#1f2937;border:1px solid #4b5563;border-radius:.5rem;color:#fff;font-size:.8125rem;outline:none;box-sizing:border-box}.jazz-demo-input[data-v-d8349330]:focus{border-color:#3b82f6;box-shadow:0 0 0 2px #3b82f64d}.jazz-demo-input[data-v-d8349330]::-moz-placeholder{color:#6b7280}.jazz-demo-input[data-v-d8349330]::placeholder{color:#6b7280}.jazz-demo-add-btn[data-v-d8349330]{width:100%;padding:.375rem .75rem;background:#2563eb;color:#fff;border:none;border-radius:.5rem;font-weight:500;font-size:.8125rem;cursor:pointer;transition:background-color .2s}.jazz-demo-add-btn[data-v-d8349330]:hover{background:#1d4ed8}.jazz-demo-list[data-v-d8349330]{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:.25rem}.jazz-demo-item[data-v-d8349330]{display:flex;align-items:center;gap:.5rem;padding:.375rem;border-radius:.5rem}.jazz-demo-item[data-v-d8349330]:hover{background:#1f2937}.jazz-demo-item:hover .jazz-demo-delete[data-v-d8349330]{opacity:1}.jazz-demo-drag[data-v-d8349330]{cursor:grab;color:#4b5563;transition:color .2s;-webkit-user-select:none;-moz-user-select:none;user-select:none;display:flex;align-items:center}.jazz-demo-drag[data-v-d8349330]:active{cursor:grabbing}.jazz-demo-item:hover .jazz-demo-drag[data-v-d8349330]{color:#9ca3af}.jazz-demo-svg[data-v-d8349330]{width:1rem;height:1rem}.jazz-demo-checkbox[data-v-d8349330]{width:.875rem;height:.875rem;accent-color:#2563eb}.jazz-demo-text[data-v-d8349330]{flex:1;color:#e5e7eb;font-size:.8125rem}.jazz-demo-text-done[data-v-d8349330]{text-decoration:line-through;color:#6b7280}.jazz-demo-delete[data-v-d8349330]{opacity:0;transition:opacity .2s;color:#6b7280;background:none;border:none;padding:.125rem;cursor:pointer;display:flex;align-items:center}.jazz-demo-delete[data-v-d8349330]:hover{color:#f87171}.jazz-demo-empty[data-v-d8349330]{color:#6b7280;text-align:center;padding:1rem 0;margin:0;font-size:.8125rem}
.jazz-demo-root[data-v-1a336f1a]{background:#030712;border:1px solid #374151;border-radius:.75rem;padding:1rem;font-family:system-ui,-apple-system,sans-serif;color:#e5e7eb;font-size:14px}.jazz-demo-header[data-v-1a336f1a]{display:flex;align-items:center;justify-content:space-between;margin-bottom:1rem}.jazz-demo-title[data-v-1a336f1a]{color:#fff;font-size:1rem;font-weight:600}.jazz-demo-toggles[data-v-1a336f1a]{display:flex;align-items:center;gap:.75rem}.jazz-demo-toggle-wrap[data-v-1a336f1a]{display:flex;align-items:center;gap:.5rem}.jazz-demo-toggle-label[data-v-1a336f1a]{color:#d1d5db;font-size:.75rem}.jazz-demo-toggle[data-v-1a336f1a]{position:relative;display:inline-flex;height:1.25rem;width:2.25rem;align-items:center;border-radius:9999px;transition:background-color .2s;border:none;cursor:pointer;padding:0}.jazz-demo-toggle-on[data-v-1a336f1a]{background:#2563eb}.jazz-demo-toggle-off[data-v-1a336f1a]{background:#4b5563}.jazz-demo-toggle-dot[data-v-1a336f1a]{display:inline-block;height:.875rem;width:.875rem;border-radius:9999px;background:#fff;transition:transform .2s}.jazz-demo-toggle-dot-on[data-v-1a336f1a]{transform:translate(1.125rem)}.jazz-demo-toggle-dot-off[data-v-1a336f1a]{transform:translate(.125rem)}.jazz-demo-covalue-id[data-v-1a336f1a]{display:flex;align-items:center;gap:.375rem;margin-bottom:.5rem;padding:.25rem .5rem;background:#1e1b4b;border:1px solid #3730a3;border-radius:.375rem;overflow:hidden}.jazz-demo-covalue-label[data-v-1a336f1a]{color:#a78bfa;font-size:.625rem;font-weight:600;white-space:nowrap}.jazz-demo-covalue-code[data-v-1a336f1a]{color:#c4b5fd;font-size:.625rem;font-family:ui-monospace,monospace;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.jazz-demo-card[data-v-1a336f1a]{background:#111827;border:1px solid #374151;border-radius:.75rem;padding:1rem}.jazz-demo-loading[data-v-1a336f1a]{color:#9ca3af;text-align:center;padding:2rem 0}.jazz-demo-card[data-v-1a336f1a]{padding:1.5rem}.jazz-counter-display[data-v-1a336f1a]{font-size:3rem;font-weight:700;color:#fff;text-align:center;padding:1rem 0;font-variant-numeric:tabular-nums}.jazz-counter-controls[data-v-1a336f1a]{display:flex;gap:.5rem}.jazz-counter-btn[data-v-1a336f1a]{flex:1;padding:.5rem;font-size:1.25rem;font-weight:600;border:1px solid #374151;border-radius:.5rem;background:#1f2937;color:#e5e7eb;cursor:pointer;transition:background-color .2s}.jazz-counter-btn[data-v-1a336f1a]:hover{background:#374151}.jazz-counter-btn-primary[data-v-1a336f1a]{background:#2563eb;border-color:#2563eb;color:#fff}.jazz-counter-btn-primary[data-v-1a336f1a]:hover{background:#1d4ed8}
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <nav class="breadcrumb astro-ilhxcym7" aria-label="breadcrumb"> <ul class="astro-ilhxcym7"> <li class="astro-ilhxcym7"> <a href="/" class="astro-ilhxcym7">Home</a> <span aria-hidden="true" class="astro-ilhxcym7">&raquo;</span> </li> <li class="astro-ilhxcym7"> <a href="/prompts/" class="astro-ilhxcym7">prompts</a> <span aria-hidden="true" class="astro-ilhxcym7">&raquo;</span> </li><li class="astro-ilhxcym7"> <a href="/claude/" class="astro-ilhxcym7">claude</a> <span aria-hidden="true" class="astro-ilhxcym7">&raquo;</span> </li><li class="astro-ilhxcym7"> <span class="lowercase astro-ilhxcym7" aria-current="page">  claude-create-hook </span> </li> </ul> </nav>  <main id="main-content" class="mx-auto max-w-4xl px-4 pb-12 pt-8"> <!-- Back Link --> <div class="mb-6"> <a href="/prompts/claude/" class="focus:ring-skin-accent inline-flex items-center gap-1 rounded-md px-3 py-1.5 text-sm text-skin-accent transition-colors hover:bg-skin-card focus:outline-none focus:ring-2 focus:ring-offset-2" onclick="event.preventDefault(); history.back();">
← Back to Claude Prompts
</a> </div> <!-- Header --> <header class="mb-8"> <h1 class="mb-4 text-3xl font-bold text-skin-base">Create Hook</h1> <div class="mb-4 flex flex-wrap items-center gap-2"> <span class="inline-block rounded-md bg-skin-card px-2 py-1 text-xs " role="img" aria-label="Category: Instruction"><span aria-hidden="true">📋</span> <!-- -->Instruction</span> <span class="inline-block rounded-md bg-skin-card px-2 py-1 text-xs"> Claude </span>  </div> <div class="flex flex-wrap gap-2"> <a href="/prompts/?q=hooks" class="text-sm text-skin-base/70 transition-colors hover:text-skin-accent hover:underline">
#hooks </a><a href="/prompts/?q=automation" class="text-sm text-skin-base/70 transition-colors hover:text-skin-accent hover:underline">
#automation </a><a href="/prompts/?q=claude-code" class="text-sm text-skin-base/70 transition-colors hover:text-skin-accent hover:underline">
#claude-code </a><a href="/prompts/?q=workflow" class="text-sm text-skin-base/70 transition-colors hover:text-skin-accent hover:underline">
#workflow </a><a href="/prompts/?q=event-driven" class="text-sm text-skin-base/70 transition-colors hover:text-skin-accent hover:underline">
#event-driven </a> </div> </header> <!-- Description and Metadata --> <section class="mb-8"> <p class="mb-4 text-skin-base">Slash command to create and configure Claude Code hooks with reference documentation and interactive guidance</p> <dl class="space-y-2 text-sm text-skin-base/70"> <div> <dt class="inline font-medium text-skin-base">
💡 Use Case:
</dt> <dd class="ml-2 inline">Use when setting up automated workflows like ESLint auto-fixing, prettier formatting, test runners, or commit message validation</dd> </div>   </dl> </section> <!-- Prompt Content --> <section class="mb-8"> <div class="mb-4 flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between"> <h2 class="text-lg font-semibold text-skin-base">Prompt Content</h2> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="1Q3xL2" prefix="r3" component-url="/_astro/prompts.BTh7qZgL.js" component-export="PromptCopyButton" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;content&quot;:[0,&quot;---\n\ndescription: Create a new custom subagent for specialized tasks\nargument-hint: [name] [description]\n\n---\n\n## /create-agent\n\n## Purpose\n\nCreate a new custom subagent (skill) for specialized tasks with proper configuration and system prompts.\n\n## Contract\n\n**Inputs:**\n\n- `$1` — AGENT_NAME (lowercase, kebab-case, e.g., \&quot;code-reviewer\&quot;)\n- `$2` — DESCRIPTION (when this agent should be invoked, e.g., \&quot;Expert code reviewer. Use proactively after code changes.\&quot;)\n- `--user` — Create user-level agent in `~/.claude/agents/` (default: project-level in `.claude/agents/`)\n- `--tools` — Comma-separated list of tools (e.g., \&quot;Read,Grep,Glob,Bash\&quot;)\n- `--model` — Model to use: \&quot;sonnet\&quot;, \&quot;opus\&quot;, \&quot;haiku\&quot;, or \&quot;inherit\&quot; (default: sonnet)\n\n**Outputs:**\n\n- `STATUS=&lt;CREATED|EXISTS|FAIL&gt; PATH=&lt;path&gt; AGENT=&lt;name&gt;`\n\n## Instructions\n\n1. **Validate inputs:**\n   - Agent name must be lowercase, kebab-case only\n   - Description must be non-empty and descriptive\n   - If `--tools` specified, validate tool names against available tools\n   - If `--model` specified, validate it&#39;s one of: sonnet, opus, haiku, inherit\n\n2. **Determine file location:**\n   - Default: `.claude/agents/{AGENT_NAME}.md` (project-level)\n   - With `--user`: `~/.claude/agents/{AGENT_NAME}.md` (user-level)\n   - Create directory if it doesn&#39;t exist\n\n3. **Check for existing agent:**\n   - If file exists, output `STATUS=EXISTS` and exit\n   - Recommend using `/agents` command to edit existing agents\n\n4. **Generate agent file content:**\n\n   ```markdown\n   ---\n   name: { AGENT_NAME }\n   description: { DESCRIPTION }\n   tools: { TOOLS } # Optional - only include if specified\n   model: { MODEL } # Optional - only include if specified\n   ---\n\n   You are a specialized agent for {purpose based on description}.\n\n   When invoked:\n\n   1. Understand the specific task or problem\n   2. Analyze the relevant context\n   3. Execute your specialized function\n   4. Provide clear, actionable results\n\n   Key responsibilities:\n\n   - {Responsibility 1 based on description}\n   - {Responsibility 2 based on description}\n   - {Responsibility 3 based on description}\n\n   Best practices:\n\n   - Be focused and efficient\n   - Provide specific, actionable feedback\n   - Document your reasoning\n   - Follow established patterns and conventions\n\n   For each task:\n\n   - Explain your approach\n   - Show your work\n   - Highlight key findings or changes\n   - Suggest next steps if applicable\n   ```\n\n5. **Write the file:**\n   - Create the agent file with proper frontmatter\n   - Ensure proper formatting and indentation\n   - Set appropriate file permissions\n\n6. **Output result:**\n   - Print: `STATUS=CREATED PATH={path} AGENT={name}`\n   - Provide usage example: `Use the {name} agent to...`\n\n## Examples\n\n### Basic project-level agent\n\n```bash\n/create-skill code-reviewer \&quot;Expert code review specialist. Use proactively after code changes.\&quot;\n# Output: STATUS=CREATED PATH=.claude/agents/code-reviewer.md AGENT=code-reviewer\n```\n\n### User-level agent with specific tools\n\n```bash\n/create-skill debugger \&quot;Debugging specialist for errors and test failures\&quot; --user --tools \&quot;Read,Edit,Bash,Grep,Glob\&quot;\n# Output: STATUS=CREATED PATH=~/.claude/agents/debugger.md AGENT=debugger\n```\n\n### Agent with specific model\n\n```bash\n/create-skill data-scientist \&quot;Data analysis expert for SQL queries and insights\&quot; --tools \&quot;Bash,Read,Write\&quot; --model \&quot;sonnet\&quot;\n# Output: STATUS=CREATED PATH=.claude/agents/data-scientist.md AGENT=data-scientist\n```\n\n## Constraints\n\n- Idempotent: Won&#39;t overwrite existing agents\n- No network access required\n- Agent names must follow naming conventions\n- Tools list must match available Claude Code tools\n- Model must be valid alias or &#39;inherit&#39;\n\n## Best Practices\n\n- Use descriptive, action-oriented descriptions\n- Include \&quot;use PROACTIVELY\&quot; in description for automatic invocation\n- Start with Claude-generated agents via `/agents` for complex cases\n- Limit tools to only what the agent needs\n- Design focused agents with single, clear responsibilities\n- Add to version control for team collaboration\n\n## Related Commands\n\n- `/agents` - Interactive interface for managing agents (recommended for editing)\n- Use created agents: \&quot;Use the {name} agent to...\&quot;\n- Invoke explicitly: \&quot;Ask the {name} agent to investigate...\&quot;&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PromptCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus:ring-skin-accent/20 inline-flex items-center gap-2 whitespace-nowrap rounded-lg border-2 border-skin-line bg-skin-card px-4 py-2.5 text-sm font-medium text-skin-base shadow-sm transition-all hover:border-skin-accent/50 hover:text-skin-accent focus:border-skin-accent focus:outline-none focus:ring-2" aria-label="Copy prompt to clipboard"><svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg>Copy Prompt</button><!--astro:end--></astro-island> </div> <div class="overflow-x-auto rounded-md border border-skin-line bg-skin-card p-4"> <div class="prose prose-sm max-w-none text-skin-base prose-headings:text-skin-base prose-p:text-skin-base prose-a:text-skin-accent prose-strong:text-skin-base prose-code:text-skin-base prose-pre:bg-skin-fill"> <hr>
<p>description: Create a new custom subagent for specialized tasks
argument-hint: [name] [description]</p>
<hr>
<h2 id="create-agent">/create-agent<a class="heading-link" aria-label="Link to section" href="#create-agent"><span class="heading-link-icon">#</span></a></h2>
<h2 id="purpose">Purpose<a class="heading-link" aria-label="Link to section" href="#purpose"><span class="heading-link-icon">#</span></a></h2>
<p>Create a new custom subagent (skill) for specialized tasks with proper configuration and system prompts.</p>
<h2 id="contract">Contract<a class="heading-link" aria-label="Link to section" href="#contract"><span class="heading-link-icon">#</span></a></h2>
<p><strong>Inputs:</strong></p>
<ul>
<li><code>$1</code> — AGENT_NAME (lowercase, kebab-case, e.g., “code-reviewer”)</li>
<li><code>$2</code> — DESCRIPTION (when this agent should be invoked, e.g., “Expert code reviewer. Use proactively after code changes.”)</li>
<li><code>--user</code> — Create user-level agent in <code>~/.claude/agents/</code> (default: project-level in <code>.claude/agents/</code>)</li>
<li><code>--tools</code> — Comma-separated list of tools (e.g., “Read,Grep,Glob,Bash”)</li>
<li><code>--model</code> — Model to use: “sonnet”, “opus”, “haiku”, or “inherit” (default: sonnet)</li>
</ul>
<p><strong>Outputs:</strong></p>
<ul>
<li><code>STATUS=&#x3C;CREATED|EXISTS|FAIL> PATH=&#x3C;path> AGENT=&#x3C;name></code></li>
</ul>
<h2 id="instructions">Instructions<a class="heading-link" aria-label="Link to section" href="#instructions"><span class="heading-link-icon">#</span></a></h2>
<ol>
<li>
<p><strong>Validate inputs:</strong></p>
<ul>
<li>Agent name must be lowercase, kebab-case only</li>
<li>Description must be non-empty and descriptive</li>
<li>If <code>--tools</code> specified, validate tool names against available tools</li>
<li>If <code>--model</code> specified, validate it’s one of: sonnet, opus, haiku, inherit</li>
</ul>
</li>
<li>
<p><strong>Determine file location:</strong></p>
<ul>
<li>Default: <code>.claude/agents/{AGENT_NAME}.md</code> (project-level)</li>
<li>With <code>--user</code>: <code>~/.claude/agents/{AGENT_NAME}.md</code> (user-level)</li>
<li>Create directory if it doesn’t exist</li>
</ul>
</li>
<li>
<p><strong>Check for existing agent:</strong></p>
<ul>
<li>If file exists, output <code>STATUS=EXISTS</code> and exit</li>
<li>Recommend using <code>/agents</code> command to edit existing agents</li>
</ul>
</li>
<li>
<p><strong>Generate agent file content:</strong></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"><span style="color:#F7768E">name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> {</span><span style="color:#9ECE6A"> AGENT_NAME</span><span style="color:#89DDFF"> }</span></span>
<span class="line"><span style="color:#F7768E">description</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> {</span><span style="color:#9ECE6A"> DESCRIPTION</span><span style="color:#89DDFF"> }</span></span>
<span class="line"><span style="color:#F7768E">tools</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> {</span><span style="color:#9ECE6A"> TOOLS</span><span style="color:#89DDFF"> }</span><span style="color:#51597D;font-style:italic"> # Optional - only include if specified</span></span>
<span class="line"><span style="color:#F7768E">model</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> {</span><span style="color:#9ECE6A"> MODEL</span><span style="color:#89DDFF"> }</span><span style="color:#51597D;font-style:italic"> # Optional - only include if specified</span></span>
<span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">You are a specialized agent for {purpose based on description}.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">When invoked:</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">1.</span><span style="color:#9AA5CE"> Understand the specific task or problem</span></span>
<span class="line"><span style="color:#89DDFF">2.</span><span style="color:#9AA5CE"> Analyze the relevant context</span></span>
<span class="line"><span style="color:#89DDFF">3.</span><span style="color:#9AA5CE"> Execute your specialized function</span></span>
<span class="line"><span style="color:#89DDFF">4.</span><span style="color:#9AA5CE"> Provide clear, actionable results</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Key responsibilities:</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> {Responsibility 1 based on description}</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> {Responsibility 2 based on description}</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> {Responsibility 3 based on description}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Best practices:</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Be focused and efficient</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Provide specific, actionable feedback</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Document your reasoning</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Follow established patterns and conventions</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">For each task:</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Explain your approach</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Show your work</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Highlight key findings or changes</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Suggest next steps if applicable</span></span></code><button type="button" class="copy" data-code="---
name: { AGENT_NAME }
description: { DESCRIPTION }
tools: { TOOLS } # Optional - only include if specified
model: { MODEL } # Optional - only include if specified
---

You are a specialized agent for {purpose based on description}.

When invoked:

1. Understand the specific task or problem
2. Analyze the relevant context
3. Execute your specialized function
4. Provide clear, actionable results

Key responsibilities:

- {Responsibility 1 based on description}
- {Responsibility 2 based on description}
- {Responsibility 3 based on description}

Best practices:

- Be focused and efficient
- Provide specific, actionable feedback
- Document your reasoning
- Follow established patterns and conventions

For each task:

- Explain your approach
- Show your work
- Highlight key findings or changes
- Suggest next steps if applicable" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
</li>
<li>
<p><strong>Write the file:</strong></p>
<ul>
<li>Create the agent file with proper frontmatter</li>
<li>Ensure proper formatting and indentation</li>
<li>Set appropriate file permissions</li>
</ul>
</li>
<li>
<p><strong>Output result:</strong></p>
<ul>
<li>Print: <code>STATUS=CREATED PATH={path} AGENT={name}</code></li>
<li>Provide usage example: <code>Use the {name} agent to...</code></li>
</ul>
</li>
</ol>
<h2 id="examples">Examples<a class="heading-link" aria-label="Link to section" href="#examples"><span class="heading-link-icon">#</span></a></h2>
<h3 id="basic-project-level-agent">Basic project-level agent<a class="heading-link" aria-label="Link to section" href="#basic-project-level-agent"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#C0CAF5">/create-skill</span><span style="color:#9ECE6A"> code-reviewer</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">Expert code review specialist. Use proactively after code changes.</span><span style="color:#89DDFF">"</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"># Output: STATUS=CREATED PATH=.claude/agents/code-reviewer.md AGENT=code-reviewer</span></span></code><button type="button" class="copy" data-code="/create-skill code-reviewer &#x22;Expert code review specialist. Use proactively after code changes.&#x22;
# Output: STATUS=CREATED PATH=.claude/agents/code-reviewer.md AGENT=code-reviewer" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="user-level-agent-with-specific-tools">User-level agent with specific tools<a class="heading-link" aria-label="Link to section" href="#user-level-agent-with-specific-tools"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#C0CAF5">/create-skill</span><span style="color:#9ECE6A"> debugger</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">Debugging specialist for errors and test failures</span><span style="color:#89DDFF">"</span><span style="color:#E0AF68"> --user</span><span style="color:#E0AF68"> --tools</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">Read,Edit,Bash,Grep,Glob</span><span style="color:#89DDFF">"</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"># Output: STATUS=CREATED PATH=~/.claude/agents/debugger.md AGENT=debugger</span></span></code><button type="button" class="copy" data-code="/create-skill debugger &#x22;Debugging specialist for errors and test failures&#x22; --user --tools &#x22;Read,Edit,Bash,Grep,Glob&#x22;
# Output: STATUS=CREATED PATH=~/.claude/agents/debugger.md AGENT=debugger" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="agent-with-specific-model">Agent with specific model<a class="heading-link" aria-label="Link to section" href="#agent-with-specific-model"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#C0CAF5">/create-skill</span><span style="color:#9ECE6A"> data-scientist</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">Data analysis expert for SQL queries and insights</span><span style="color:#89DDFF">"</span><span style="color:#E0AF68"> --tools</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">Bash,Read,Write</span><span style="color:#89DDFF">"</span><span style="color:#E0AF68"> --model</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">sonnet</span><span style="color:#89DDFF">"</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"># Output: STATUS=CREATED PATH=.claude/agents/data-scientist.md AGENT=data-scientist</span></span></code><button type="button" class="copy" data-code="/create-skill data-scientist &#x22;Data analysis expert for SQL queries and insights&#x22; --tools &#x22;Bash,Read,Write&#x22; --model &#x22;sonnet&#x22;
# Output: STATUS=CREATED PATH=.claude/agents/data-scientist.md AGENT=data-scientist" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h2 id="constraints">Constraints<a class="heading-link" aria-label="Link to section" href="#constraints"><span class="heading-link-icon">#</span></a></h2>
<ul>
<li>Idempotent: Won’t overwrite existing agents</li>
<li>No network access required</li>
<li>Agent names must follow naming conventions</li>
<li>Tools list must match available Claude Code tools</li>
<li>Model must be valid alias or ‘inherit’</li>
</ul>
<h2 id="best-practices">Best Practices<a class="heading-link" aria-label="Link to section" href="#best-practices"><span class="heading-link-icon">#</span></a></h2>
<ul>
<li>Use descriptive, action-oriented descriptions</li>
<li>Include “use PROACTIVELY” in description for automatic invocation</li>
<li>Start with Claude-generated agents via <code>/agents</code> for complex cases</li>
<li>Limit tools to only what the agent needs</li>
<li>Design focused agents with single, clear responsibilities</li>
<li>Add to version control for team collaboration</li>
</ul>
<h2 id="related-commands">Related Commands<a class="heading-link" aria-label="Link to section" href="#related-commands"><span class="heading-link-icon">#</span></a></h2>
<ul>
<li><code>/agents</code> - Interactive interface for managing agents (recommended for editing)</li>
<li>Use created agents: “Use the {name} agent to…”</li>
<li>Invoke explicitly: “Ask the {name} agent to investigate…”</li>
</ul> </div> </div> </section> <!-- Usage Hint --> <aside class="text-sm text-skin-base/70"> <p>
💡 <strong class="text-skin-base">Tip:</strong> Click "Copy Prompt" to copy
        the entire content including any frontmatter.
 Paste directly into your AI assistant. </p> </aside> </main> <footer class="mt-auto astro-sz7xmlte"> <div class="max-w-5xl mx-auto px-4"> <hr class="border-skin-line" aria-hidden="true"> </div> <div class="footer-wrapper astro-sz7xmlte"> <div class="footer-content astro-sz7xmlte"> <div class="copyright-wrapper astro-sz7xmlte"> <span class="astro-sz7xmlte">Copyright &#169; 2026</span> <span class="separator astro-sz7xmlte">&nbsp;|&nbsp;</span> <span class="astro-sz7xmlte">All rights reserved.</span> </div> <div class="rss-prompt astro-sz7xmlte"> <a href="/rss.xml" class="rss-link group astro-sz7xmlte" title="Never miss a post - Subscribe via RSS" onclick="if (window.plausible) window.plausible('RSS Subscribe', { props: { location: 'footer' } })"> <div class="flex items-center gap-2 astro-sz7xmlte"> <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-skin-accent group-hover:animate-pulse astro-sz7xmlte"><path fill="currentColor" d="M19 20.001C19 11.729 12.271 5 4 5v2c7.168 0 13 5.832 13 13.001h2z" class="astro-sz7xmlte"></path><path fill="currentColor" d="M12 20.001h2C14 14.486 9.514 10 4 10v2c4.411 0 8 3.589 8 8.001z" class="astro-sz7xmlte"></path><circle cx="6" cy="18" r="2" fill="currentColor" class="astro-sz7xmlte"></circle> </svg> <span class="text-sm astro-sz7xmlte">Subscribe via RSS</span> </div> </a> </div> <div class="social-icons flex astro-upu6fzxr"> <a href="https://github.com/alexanderop" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title=" alexop.dev on Github" target="_blank" rel="noopener noreferrer"> <svg
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
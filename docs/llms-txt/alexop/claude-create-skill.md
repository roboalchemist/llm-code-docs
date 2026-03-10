# Source: https://alexop.dev/prompts/claude/claude-create-skill

<!DOCTYPE html><html lang="en" class=" astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/prompts/claude/claude-create-skill/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>Create Skill | alexop.dev</title><meta name="title" content="Create Skill | alexop.dev"><meta name="description" content="Slash command to generate new Claude Skills with proper structure, YAML frontmatter, and bundled resources"><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="Create Skill | alexop.dev"><meta property="og:description" content="Slash command to generate new Claude Skills with proper structure, YAML frontmatter, and bundled resources"><meta property="og:url" content="https://alexop.dev/prompts/claude/claude-create-skill/"><meta property="og:image" content="https://alexop.dev/prompts/claude/claude-create-skill/index.png"><meta property="og:type" content="website"><!-- Article Published/Modified time --><meta property="article:published_time" content="2025-11-16T00:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/prompts/claude/claude-create-skill/"><meta property="twitter:title" content="Create Skill | alexop.dev"><meta property="twitter:description" content="Slash command to generate new Claude Skills with proper structure, YAML frontmatter, and bundled resources"><meta property="twitter:image" content="https://alexop.dev/prompts/claude/claude-create-skill/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","headline":"Create Skill | alexop.dev","description":"Slash command to generate new Claude Skills with proper structure, YAML frontmatter, and bundled resources","datePublished":"2025-11-16T00:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic","url":"https://alexop.dev"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <nav class="breadcrumb astro-ilhxcym7" aria-label="breadcrumb"> <ul class="astro-ilhxcym7"> <li class="astro-ilhxcym7"> <a href="/" class="astro-ilhxcym7">Home</a> <span aria-hidden="true" class="astro-ilhxcym7">&raquo;</span> </li> <li class="astro-ilhxcym7"> <a href="/prompts/" class="astro-ilhxcym7">prompts</a> <span aria-hidden="true" class="astro-ilhxcym7">&raquo;</span> </li><li class="astro-ilhxcym7"> <a href="/claude/" class="astro-ilhxcym7">claude</a> <span aria-hidden="true" class="astro-ilhxcym7">&raquo;</span> </li><li class="astro-ilhxcym7"> <span class="lowercase astro-ilhxcym7" aria-current="page">  claude-create-skill </span> </li> </ul> </nav>  <main id="main-content" class="mx-auto max-w-4xl px-4 pb-12 pt-8"> <!-- Back Link --> <div class="mb-6"> <a href="/prompts/claude/" class="focus:ring-skin-accent inline-flex items-center gap-1 rounded-md px-3 py-1.5 text-sm text-skin-accent transition-colors hover:bg-skin-card focus:outline-none focus:ring-2 focus:ring-offset-2" onclick="event.preventDefault(); history.back();">
← Back to Claude Prompts
</a> </div> <!-- Header --> <header class="mb-8"> <h1 class="mb-4 text-3xl font-bold text-skin-base">Create Skill</h1> <div class="mb-4 flex flex-wrap items-center gap-2"> <span class="inline-block rounded-md bg-skin-card px-2 py-1 text-xs " role="img" aria-label="Category: Instruction"><span aria-hidden="true">📋</span> <!-- -->Instruction</span> <span class="inline-block rounded-md bg-skin-card px-2 py-1 text-xs"> Claude </span>  </div> <div class="flex flex-wrap gap-2"> <a href="/prompts/?q=skill" class="text-sm text-skin-base/70 transition-colors hover:text-skin-accent hover:underline">
#skill </a><a href="/prompts/?q=claude-code" class="text-sm text-skin-base/70 transition-colors hover:text-skin-accent hover:underline">
#claude-code </a><a href="/prompts/?q=automation" class="text-sm text-skin-base/70 transition-colors hover:text-skin-accent hover:underline">
#automation </a><a href="/prompts/?q=agent" class="text-sm text-skin-base/70 transition-colors hover:text-skin-accent hover:underline">
#agent </a> </div> </header> <!-- Description and Metadata --> <section class="mb-8"> <p class="mb-4 text-skin-base">Slash command to generate new Claude Skills with proper structure, YAML frontmatter, and bundled resources</p> <dl class="space-y-2 text-sm text-skin-base/70"> <div> <dt class="inline font-medium text-skin-base">
💡 Use Case:
</dt> <dd class="ml-2 inline">Use when creating reusable skills for workflows, file operations, or specialized tasks that Claude can invoke automatically</dd> </div>   </dl> </section> <!-- Prompt Content --> <section class="mb-8"> <div class="mb-4 flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between"> <h2 class="text-lg font-semibold text-skin-base">Prompt Content</h2> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="1dYwLu" prefix="r3" component-url="/_astro/prompts.BTh7qZgL.js" component-export="PromptCopyButton" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;content&quot;:[0,&quot;---\n\ndescription: Generate a new Claude Skill with proper structure and YAML frontmatter using official documentation as reference\nargument-hint: [skill-name] [description]\n\n---\n\n## /create-skill\n\n## Purpose\n\nGenerate a new Claude Skill with proper structure and YAML frontmatter using official documentation as reference\n\n## Contract\n\n**Inputs:**\n\n- `$1` — SKILL_NAME (lowercase, kebab-case, max 64 characters)\n- `$2` — DESCRIPTION (what the skill does and when to use it, max 1024 characters)\n- `--personal` — create in ~/.claude/skills/ (default)\n- `--project` — create in .claude/skills/\n\n**Outputs:** `STATUS=&lt;CREATED|EXISTS|FAIL&gt; PATH=&lt;path&gt;`\n\n## Instructions\n\n1. **Validate inputs:**\n   - Skill name: lowercase letters, numbers, hyphens only (max 64 chars)\n   - Description: non-empty, max 1024 characters, no angle brackets (&lt; or &gt;)\n   - Description should include both WHAT the skill does and WHEN to use it\n   - If user provides additional frontmatter properties, validate against allowed list:\n     - **Allowed:** name, description, license, allowed-tools, metadata\n     - **Warning** (not error) for unexpected properties like version, author, tags\n     - Inform user that unexpected properties may cause issues during packaging\n\n2. **Determine target directory:**\n   - Personal (default): `~/.claude/skills/{{SKILL_NAME}}/`\n   - Project: `.claude/skills/{{SKILL_NAME}}/`\n\n3. **Check if skill already exists:**\n   - If exists: output `STATUS=EXISTS PATH=&lt;path&gt;` and stop\n\n4. **Analyze what bundled resources this skill needs:**\n\n   Based on the skill name and description, intelligently determine which bundled resources would be valuable:\n\n   **Create scripts/ directory when:**\n   - Skill involves file manipulation (PDF, images, documents, etc.)\n   - Skill requires deterministic operations (data processing, conversions)\n   - Same code would be rewritten repeatedly\n   - Examples: pdf-editor, image-processor, data-analyzer, file-converter\n\n   **Create references/ directory when:**\n   - Skill needs reference documentation (API docs, schemas, specifications)\n   - Detailed information would make SKILL.md too long (&gt;5k words)\n   - Domain knowledge needs to be documented (company policies, standards)\n   - Examples: api-client, database-query, brand-guidelines, coding-standards\n\n   **Create assets/ directory when:**\n   - Skill uses templates or boilerplate code\n   - Skill needs brand assets (logos, fonts, images)\n   - Skill creates documents from templates (presentations, reports)\n   - Examples: frontend-builder, brand-guidelines, document-generator, presentation-maker\n\n   **Questions to ask user for clarification (only if unclear):**\n   - \&quot;Will this skill need to run any scripts repeatedly?\&quot; (→ scripts/)\n   - \&quot;Does this skill need reference documentation like API docs or schemas?\&quot; (→ references/)\n   - \&quot;Will this skill use templates or assets like logos/fonts/boilerplate?\&quot; (→ assets/)\n\n   **Communicate the decision:**\n   After analysis, inform the user which directories will be created and why:\n   - Example: \&quot;Based on the description, I&#39;ll create scripts/ for PDF manipulation utilities and references/ for schema documentation.\&quot;\n   - Be transparent about the reasoning\n   - It&#39;s better to include a directory with placeholders than to omit one that might be needed\n\n5. **Create skill directory structure based on analysis:**\n\n   Always create:\n\n   ```\n   {{SKILL_NAME}}/\n   └── SKILL.md (required)\n   ```\n\n   Conditionally create based on Step 4 analysis:\n\n   ```\n   ├── scripts/ (if determined needed)\n   │   └── example.py (executable placeholder with TODO)\n   ├── references/ (if determined needed)\n   │   └── README.md (documentation placeholder with guidance)\n   └── assets/ (if determined needed)\n       └── README.md (asset placeholder with examples)\n   ```\n\n6. **Generate SKILL.md using this template:**\n\n   ```markdown\n   ---\n   name: { { SKILL_NAME } }\n   description: { { DESCRIPTION } }\n   # Optional fields (uncomment if needed):\n   # allowed-tools: [\&quot;Read\&quot;, \&quot;Write\&quot;, \&quot;Bash\&quot;]  # Restrict to specific tools\n   # metadata:\n   #   category: \&quot;development\&quot;\n   #   version: \&quot;1.0.0\&quot;  # For tracking in your project\n   # license: \&quot;MIT\&quot;  # For shared skills\n   ---\n\n   # {{Title Case Skill Name}}\n\n   ## Overview\n\n   [TODO: 1-2 sentences explaining what this skill does and why it&#39;s valuable]\n\n   ## When to Use\n\n   [TODO: Specific triggers and scenarios where this skill should be invoked]\n\n   ## Structuring This Skill\n\n   Choose an organizational pattern:\n\n   **Workflow-Based** (sequential) - TDD workflows, git commits, deployments\n\n   - Structure: Overview → Step 1 → Step 2 → Step 3...\n\n   **Task-Based** (operations) - File tools, API operations, data transforms\n\n   - Structure: Overview → Quick Start → Operation A → Operation B...\n\n   **Reference-Based** (guidelines) - Brand standards, coding rules, checklists\n\n   - Structure: Overview → Guidelines → Specifications → Examples\n\n   **Capabilities-Based** (integrated) - Product management, debugging, systems\n\n   - Structure: Overview → Core Capabilities → Feature 1 → Feature 2...\n\n   Patterns can be mixed. Delete this section after choosing.\n\n   [TODO: Delete this \&quot;Structuring This Skill\&quot; section after choosing your approach]\n\n   ## Instructions\n\n   [TODO: Provide clear, step-by-step guidance using imperative/infinitive language]\n\n   [TODO: Reference any bundled resources (scripts, references, assets) so Claude knows how to use them]\n\n   Example structure:\n\n   1. First major step\n   2. Second major step\n   3. Third major step\n\n   ## Bundled Resources\n\n   [TODO: Document bundled resources. Delete unused subsections.]\n\n   **scripts/** - Executable code run directly (not loaded into context)\n\n   - Example: `scripts/process_data.py` - Processes CSV and generates reports\n\n   **references/** - Documentation loaded into context when needed\n\n   - Example: `references/api_docs.md` - API endpoint documentation\n\n   **assets/** - Files used in output (not loaded into context)\n\n   - Example: `assets/template.pptx` - Presentation template\n\n   ## Examples\n\n   [TODO: Show concrete examples with realistic user requests]\n   ```\n\n   User: \&quot;Help me [specific task]\&quot;\n   Claude: [How the skill responds]\n\n   ```\n\n   ## Progressive Disclosure\n\n   Keep SKILL.md &lt;5k words. Move detailed info to references/. Three-level loading:\n   1. Metadata (~100 words) - Always in context\n   2. SKILL.md - Loaded when triggered\n   3. Bundled resources - Loaded as needed\n   ```\n\n7. **Create bundled resource placeholders (based on Step 4 analysis):**\n\n   For each directory determined in Step 4, create appropriate placeholder files:\n\n   **scripts/** → Create `scripts/example.py` (executable Python template with TODO comment)\n   **references/** → Create `references/README.md` (documentation template explaining purpose)\n   **assets/** → Create `assets/README.md` (asset placeholder explaining common types)\n\n   Make scripts executable: `chmod +x scripts/*.py`\n\n8. **Follow official guidelines:**\n   - Name: lowercase, numbers, hyphens only (max 64 chars)\n   - Description: Include triggers and use cases (max 1024 chars)\n   - Instructions: Clear, step-by-step guidance\n   - Keep skills focused on single capabilities\n   - Make descriptions specific with trigger keywords\n\n9. **Output:**\n   - Print: `STATUS=CREATED PATH={{full_path}}`\n   - Summarize what was created and why (list directories + reasoning)\n   - Remind user to populate placeholders and complete [TODO] items\n\n## Constraints\n\n- Skills are model-invoked (Claude decides when to use them)\n- Description must be specific enough for Claude to discover when to use it\n- One skill = one capability (stay focused)\n- Use forward slashes in all file paths\n- Valid YAML syntax required in frontmatter\n\n## Frontmatter Properties\n\n**Required:**\n\n- `name` - Lowercase hyphen-case identifier (max 64 chars, matches directory name)\n- `description` - What it does + when to use it (max 1024 chars, no angle brackets)\n\n**Optional:**\n\n- `allowed-tools: [\&quot;Read\&quot;, \&quot;Write\&quot;, \&quot;Bash\&quot;]` - Restrict Claude to specific tools\n- `metadata: {category: \&quot;dev\&quot;, version: \&quot;1.0\&quot;}` - Custom tracking fields\n- `license: \&quot;MIT\&quot;` - License for shared skills\n\n**Prohibited** (causes warnings):\n\n- `version`, `author`, `tags` - Use metadata or description instead\n\n## Examples\n\n**Simple workflow skill:**\n\n```bash\n/create-skill commit-helper \&quot;Generate clear git commit messages from diffs. Use when writing commits or reviewing staged changes.\&quot;\n```\n\n_Claude will determine: No bundled resources needed - just workflow guidance_\n\n**File manipulation skill:**\n\n```bash\n/create-skill pdf-processor \&quot;Extract text and tables from PDF files. Use when working with PDFs, forms, or document extraction.\&quot;\n```\n\n_Claude will determine: Needs scripts/ directory for PDF manipulation utilities_\n\n**API integration skill:**\n\n```bash\n/create-skill api-client \&quot;Make REST API calls and handle responses. Use for API testing and integration work with the company API.\&quot;\n```\n\n_Claude will determine: Needs references/ directory for API documentation and schemas_\n\n**Image processing skill:**\n\n```bash\n/create-skill image-processor \&quot;Resize, rotate, and convert images. Use when editing images or batch processing files.\&quot;\n```\n\n_Claude will determine: Needs scripts/ directory for image manipulation operations_\n\n**Brand guidelines skill:**\n\n```bash\n/create-skill brand-guidelines \&quot;Apply company brand guidelines to designs. Use when creating presentations, documents, or marketing materials.\&quot;\n```\n\n_Claude will determine: Needs references/ for guidelines + assets/ for logos, fonts, templates_\n\n**Frontend builder skill:**\n\n```bash\n/create-skill frontend-builder \&quot;Build responsive web applications with React. Use when creating new frontend projects or components.\&quot; --project\n```\n\n_Claude will determine: Needs scripts/ for build tools + assets/ for boilerplate templates_\n\n**Database query skill:**\n\n```bash\n/create-skill database-query \&quot;Query and analyze database tables. Use when working with SQL, BigQuery, or data analysis tasks.\&quot; --project\n```\n\n_Claude will determine: Needs references/ for schema documentation_\n\n**How Claude determines what&#39;s needed:**\n\n- Mentions \&quot;PDF\&quot;, \&quot;images\&quot;, \&quot;documents\&quot;, \&quot;convert\&quot; → scripts/\n- Mentions \&quot;API\&quot;, \&quot;database\&quot;, \&quot;guidelines\&quot;, \&quot;standards\&quot; → references/\n- Mentions \&quot;templates\&quot;, \&quot;boilerplate\&quot;, \&quot;brand\&quot;, \&quot;presentations\&quot; → assets/\n- Simple workflow/process skills → SKILL.md only\n\n**Adding optional frontmatter properties:**\n\nAfter creating a skill, you can manually edit SKILL.md to add optional frontmatter properties:\n\n```markdown\n---\nname: database-query\ndescription: Query and analyze database tables. Use when working with SQL, BigQuery, or data analysis tasks.\nallowed-tools: [\&quot;Bash\&quot;, \&quot;Read\&quot;, \&quot;Grep\&quot;]\nmetadata:\n  category: \&quot;data\&quot;\n  version: \&quot;1.0.0\&quot;\n  team: \&quot;analytics\&quot;\nlicense: \&quot;MIT\&quot;\n---\n```\n\n## Post-Creation Workflow\n\n**1. Edit** - Complete [TODO] placeholders, populate bundled resources, add concrete examples\n\n**2. Test** - Restart Claude Code, test with trigger queries matching description\n\n**3. Validate** - Check frontmatter properties, description clarity, no sensitive data\n\n**4. Iterate** - Use on real tasks, update based on struggles/feedback\n\n**Optional:**\n\n- Package for distribution: Use packaging tools or `/create-plugin`\n- Share with team: Distribute .zip or via plugin marketplace\n\n## Example: Well-Structured Skill\n\nHere&#39;s an example of a production-quality skill to demonstrate best practices:\n\n**artifacts-builder** - A skill for creating complex React/TypeScript artifacts with shadcn/ui\n\n```\nartifacts-builder/\n├── SKILL.md (focused, ~75 lines)\n└── scripts/\n    ├── init-artifact.sh (323 lines - initializes React+Vite+shadcn project)\n    ├── bundle-artifact.sh (54 lines - bundles to single HTML)\n    └── shadcn-components.tar.gz (pre-packaged shadcn/ui components)\n```\n\n**SKILL.md structure:**\n\n````markdown\n---\nname: artifacts-builder\ndescription: Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts.\nlicense: Complete terms in LICENSE.txt\n---\n\n# Artifacts Builder\n\nTo build powerful frontend claude.ai artifacts, follow these steps:\n\n1. Initialize the frontend repo using `scripts/init-artifact.sh`\n2. Develop your artifact by editing the generated code\n3. Bundle all code into a single HTML file using `scripts/bundle-artifact.sh`\n4. Display artifact to user\n5. (Optional) Test the artifact\n\n**Stack**: React 18 + TypeScript + Vite + Parcel (bundling) + Tailwind CSS + shadcn/ui\n\n## Design &amp; Style Guidelines\n\nVERY IMPORTANT: To avoid what is often referred to as \&quot;AI slop\&quot;, avoid using excessive centered layouts, purple gradients, uniform rounded corners, and Inter font.\n\n## Quick Start\n\n### Step 1: Initialize Project\n\nRun the initialization script to create a new React project:\n\n```bash\nbash scripts/init-artifact.sh &lt;project-name&gt;\ncd &lt;project-name&gt;\n```\n````\n\nThis creates a fully configured project with:\n\n- ✅ React + TypeScript (via Vite)\n- ✅ Tailwind CSS 3.4.1 with shadcn/ui theming system\n- ✅ Path aliases (`@/`) configured\n- ✅ 40+ shadcn/ui components pre-installed\n- ✅ All Radix UI dependencies included\n- ✅ Parcel configured for bundling\n- ✅ Node 18+ compatibility\n\n### Step 2: Develop Your Artifact\n\nTo build the artifact, edit the generated files. See **Common Development Tasks** below for guidance.\n\n### Step 3: Bundle to Single HTML File\n\nTo bundle the React app into a single HTML artifact:\n\n```bash\nbash scripts/bundle-artifact.sh\n```\n\nThis creates `bundle.html` - a self-contained artifact with all JavaScript, CSS, and dependencies inlined.\n\n### Step 4: Share Artifact with User\n\nFinally, share the bundled HTML file in conversation with the user so they can view it as an artifact.\n\n### Step 5: Testing/Visualizing the Artifact (Optional)\n\nNote: This is a completely optional step. Only perform if necessary or requested.\n\n## Reference\n\n- **shadcn/ui components**: https://ui.shadcn.com/docs/components\n\n```\n\n**What makes this skill excellent:**\n\n1. **Clear, specific description** - States exactly what it does (React artifacts with shadcn/ui) and when NOT to use it (simple HTML)\n\n2. **Task-Based organizational pattern** - Uses numbered steps (Quick Start → Step 1, 2, 3...) for clear workflow\n\n3. **Practical scripts/** - Contains executable utilities that prevent rewriting the same setup code:\n   - `init-artifact.sh` - Automates 20+ setup steps (Vite, Tailwind, shadcn/ui, dependencies)\n   - `bundle-artifact.sh` - Bundles multi-file React app into single HTML\n   - `shadcn-components.tar.gz` - Pre-packaged components (saves installation time)\n\n4. **Focused SKILL.md** - Only ~75 lines, moves implementation details to scripts\n\n5. **Domain-specific guidance** - Includes \&quot;Design &amp; Style Guidelines\&quot; section with specific advice\n\n6. **Optional license field** - Uses `license: Complete terms in LICENSE.txt` since Apache 2.0 is verbose\n\n7. **Progressive disclosure** - Metadata (~50 words), SKILL.md core workflow (&lt;2k words), scripts executed without loading\n\n8. **Explicit references** - Points to external docs (shadcn/ui) rather than duplicating them\n\n**Claude Code would create scripts/ automatically for this skill because:**\n- Description mentions \&quot;tools\&quot;, \&quot;React\&quot;, \&quot;Tailwind CSS\&quot;, \&quot;shadcn/ui\&quot; (technical setup)\n- Name \&quot;builder\&quot; implies construction/automation\n- Description emphasizes \&quot;elaborate, multi-component\&quot; (complexity requiring tooling)\n\n## Reference\nBased on official Claude Code Agent Skills documentation:\n- Personal skills: `~/.claude/skills/`\n- Project skills: `.claude/skills/`\n- Changes take effect on next Claude Code restart\n- Test by asking questions matching the description triggers\n```&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PromptCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus:ring-skin-accent/20 inline-flex items-center gap-2 whitespace-nowrap rounded-lg border-2 border-skin-line bg-skin-card px-4 py-2.5 text-sm font-medium text-skin-base shadow-sm transition-all hover:border-skin-accent/50 hover:text-skin-accent focus:border-skin-accent focus:outline-none focus:ring-2" aria-label="Copy prompt to clipboard"><svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg>Copy Prompt</button><!--astro:end--></astro-island> </div> <div class="overflow-x-auto rounded-md border border-skin-line bg-skin-card p-4"> <div class="prose prose-sm max-w-none text-skin-base prose-headings:text-skin-base prose-p:text-skin-base prose-a:text-skin-accent prose-strong:text-skin-base prose-code:text-skin-base prose-pre:bg-skin-fill"> <hr>
<p>description: Generate a new Claude Skill with proper structure and YAML frontmatter using official documentation as reference
argument-hint: [skill-name] [description]</p>
<hr>
<h2 id="create-skill">/create-skill<a class="heading-link" aria-label="Link to section" href="#create-skill"><span class="heading-link-icon">#</span></a></h2>
<h2 id="purpose">Purpose<a class="heading-link" aria-label="Link to section" href="#purpose"><span class="heading-link-icon">#</span></a></h2>
<p>Generate a new Claude Skill with proper structure and YAML frontmatter using official documentation as reference</p>
<h2 id="contract">Contract<a class="heading-link" aria-label="Link to section" href="#contract"><span class="heading-link-icon">#</span></a></h2>
<p><strong>Inputs:</strong></p>
<ul>
<li><code>$1</code> — SKILL_NAME (lowercase, kebab-case, max 64 characters)</li>
<li><code>$2</code> — DESCRIPTION (what the skill does and when to use it, max 1024 characters)</li>
<li><code>--personal</code> — create in ~/.claude/skills/ (default)</li>
<li><code>--project</code> — create in .claude/skills/</li>
</ul>
<p><strong>Outputs:</strong> <code>STATUS=&#x3C;CREATED|EXISTS|FAIL> PATH=&#x3C;path></code></p>
<h2 id="instructions">Instructions<a class="heading-link" aria-label="Link to section" href="#instructions"><span class="heading-link-icon">#</span></a></h2>
<ol>
<li>
<p><strong>Validate inputs:</strong></p>
<ul>
<li>Skill name: lowercase letters, numbers, hyphens only (max 64 chars)</li>
<li>Description: non-empty, max 1024 characters, no angle brackets (&#x3C; or >)</li>
<li>Description should include both WHAT the skill does and WHEN to use it</li>
<li>If user provides additional frontmatter properties, validate against allowed list:
<ul>
<li><strong>Allowed:</strong> name, description, license, allowed-tools, metadata</li>
<li><strong>Warning</strong> (not error) for unexpected properties like version, author, tags</li>
<li>Inform user that unexpected properties may cause issues during packaging</li>
</ul>
</li>
</ul>
</li>
<li>
<p><strong>Determine target directory:</strong></p>
<ul>
<li>Personal (default): <code>~/.claude/skills/{{SKILL_NAME}}/</code></li>
<li>Project: <code>.claude/skills/{{SKILL_NAME}}/</code></li>
</ul>
</li>
<li>
<p><strong>Check if skill already exists:</strong></p>
<ul>
<li>If exists: output <code>STATUS=EXISTS PATH=&#x3C;path></code> and stop</li>
</ul>
</li>
<li>
<p><strong>Analyze what bundled resources this skill needs:</strong></p>
<p>Based on the skill name and description, intelligently determine which bundled resources would be valuable:</p>
<p><strong>Create scripts/ directory when:</strong></p>
<ul>
<li>Skill involves file manipulation (PDF, images, documents, etc.)</li>
<li>Skill requires deterministic operations (data processing, conversions)</li>
<li>Same code would be rewritten repeatedly</li>
<li>Examples: pdf-editor, image-processor, data-analyzer, file-converter</li>
</ul>
<p><strong>Create references/ directory when:</strong></p>
<ul>
<li>Skill needs reference documentation (API docs, schemas, specifications)</li>
<li>Detailed information would make SKILL.md too long (>5k words)</li>
<li>Domain knowledge needs to be documented (company policies, standards)</li>
<li>Examples: api-client, database-query, brand-guidelines, coding-standards</li>
</ul>
<p><strong>Create assets/ directory when:</strong></p>
<ul>
<li>Skill uses templates or boilerplate code</li>
<li>Skill needs brand assets (logos, fonts, images)</li>
<li>Skill creates documents from templates (presentations, reports)</li>
<li>Examples: frontend-builder, brand-guidelines, document-generator, presentation-maker</li>
</ul>
<p><strong>Questions to ask user for clarification (only if unclear):</strong></p>
<ul>
<li>“Will this skill need to run any scripts repeatedly?” (→ scripts/)</li>
<li>“Does this skill need reference documentation like API docs or schemas?” (→ references/)</li>
<li>“Will this skill use templates or assets like logos/fonts/boilerplate?” (→ assets/)</li>
</ul>
<p><strong>Communicate the decision:</strong>
After analysis, inform the user which directories will be created and why:</p>
<ul>
<li>Example: “Based on the description, I’ll create scripts/ for PDF manipulation utilities and references/ for schema documentation.”</li>
<li>Be transparent about the reasoning</li>
<li>It’s better to include a directory with placeholders than to omit one that might be needed</li>
</ul>
</li>
<li>
<p><strong>Create skill directory structure based on analysis:</strong></p>
<p>Always create:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="plaintext"><code><span class="line"><span>{{SKILL_NAME}}/</span></span>
<span class="line"><span>└── SKILL.md (required)</span></span></code><button type="button" class="copy" data-code="{{SKILL_NAME}}/
└── SKILL.md (required)" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>Conditionally create based on Step 4 analysis:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="plaintext"><code><span class="line"><span>├── scripts/ (if determined needed)</span></span>
<span class="line"><span>│   └── example.py (executable placeholder with TODO)</span></span>
<span class="line"><span>├── references/ (if determined needed)</span></span>
<span class="line"><span>│   └── README.md (documentation placeholder with guidance)</span></span>
<span class="line"><span>└── assets/ (if determined needed)</span></span>
<span class="line"><span>    └── README.md (asset placeholder with examples)</span></span></code><button type="button" class="copy" data-code="├── scripts/ (if determined needed)
│   └── example.py (executable placeholder with TODO)
├── references/ (if determined needed)
│   └── README.md (documentation placeholder with guidance)
└── assets/ (if determined needed)
    └── README.md (asset placeholder with examples)" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
</li>
<li>
<p><strong>Generate SKILL.md using this template:</strong></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"><span style="color:#F7768E">name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> {</span><span style="color:#89DDFF"> {</span><span style="color:#9ECE6A"> SKILL_NAME</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> }</span></span>
<span class="line"><span style="color:#F7768E">description</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> {</span><span style="color:#89DDFF"> {</span><span style="color:#9ECE6A"> DESCRIPTION</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> }</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"># Optional fields (uncomment if needed):</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"># allowed-tools: ["Read", "Write", "Bash"]  # Restrict to specific tools</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"># metadata:</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">#   category: "development"</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">#   version: "1.0.0"  # For tracking in your project</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"># license: "MIT"  # For shared skills</span></span>
<span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF;font-weight:bold">#</span><span style="color:#89DDFF;font-weight:bold"> {{Title Case Skill Name}}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Overview</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">[TODO: 1-2 sentences explaining what this skill does and why it's valuable]</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> When to Use</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">[TODO: Specific triggers and scenarios where this skill should be invoked]</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Structuring This Skill</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Choose an organizational pattern:</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**Workflow-Based**</span><span style="color:#9AA5CE"> (sequential) - TDD workflows, git commits, deployments</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Structure: Overview → Step 1 → Step 2 → Step 3...</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**Task-Based**</span><span style="color:#9AA5CE"> (operations) - File tools, API operations, data transforms</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Structure: Overview → Quick Start → Operation A → Operation B...</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**Reference-Based**</span><span style="color:#9AA5CE"> (guidelines) - Brand standards, coding rules, checklists</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Structure: Overview → Guidelines → Specifications → Examples</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**Capabilities-Based**</span><span style="color:#9AA5CE"> (integrated) - Product management, debugging, systems</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Structure: Overview → Core Capabilities → Feature 1 → Feature 2...</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Patterns can be mixed. Delete this section after choosing.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">[TODO: Delete this "Structuring This Skill" section after choosing your approach]</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Instructions</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">[TODO: Provide clear, step-by-step guidance using imperative/infinitive language]</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">[TODO: Reference any bundled resources (scripts, references, assets) so Claude knows how to use them]</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Example structure:</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">1.</span><span style="color:#9AA5CE"> First major step</span></span>
<span class="line"><span style="color:#89DDFF">2.</span><span style="color:#9AA5CE"> Second major step</span></span>
<span class="line"><span style="color:#89DDFF">3.</span><span style="color:#9AA5CE"> Third major step</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Bundled Resources</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">[TODO: Document bundled resources. Delete unused subsections.]</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**scripts/**</span><span style="color:#9AA5CE"> - Executable code run directly (not loaded into context)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Example: </span><span style="color:#89DDFF">`scripts/process_data.py`</span><span style="color:#9AA5CE"> - Processes CSV and generates reports</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**references/**</span><span style="color:#9AA5CE"> - Documentation loaded into context when needed</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Example: </span><span style="color:#89DDFF">`references/api_docs.md`</span><span style="color:#9AA5CE"> - API endpoint documentation</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**assets/**</span><span style="color:#9AA5CE"> - Files used in output (not loaded into context)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Example: </span><span style="color:#89DDFF">`assets/template.pptx`</span><span style="color:#9AA5CE"> - Presentation template</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Examples</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">[TODO: Show concrete examples with realistic user requests]</span></span></code><button type="button" class="copy" data-code="---
name: { { SKILL_NAME } }
description: { { DESCRIPTION } }
# Optional fields (uncomment if needed):
# allowed-tools: [&#x22;Read&#x22;, &#x22;Write&#x22;, &#x22;Bash&#x22;]  # Restrict to specific tools
# metadata:
#   category: &#x22;development&#x22;
#   version: &#x22;1.0.0&#x22;  # For tracking in your project
# license: &#x22;MIT&#x22;  # For shared skills
---

# {{Title Case Skill Name}}

## Overview

[TODO: 1-2 sentences explaining what this skill does and why it&#x27;s valuable]

## When to Use

[TODO: Specific triggers and scenarios where this skill should be invoked]

## Structuring This Skill

Choose an organizational pattern:

**Workflow-Based** (sequential) - TDD workflows, git commits, deployments

- Structure: Overview → Step 1 → Step 2 → Step 3...

**Task-Based** (operations) - File tools, API operations, data transforms

- Structure: Overview → Quick Start → Operation A → Operation B...

**Reference-Based** (guidelines) - Brand standards, coding rules, checklists

- Structure: Overview → Guidelines → Specifications → Examples

**Capabilities-Based** (integrated) - Product management, debugging, systems

- Structure: Overview → Core Capabilities → Feature 1 → Feature 2...

Patterns can be mixed. Delete this section after choosing.

[TODO: Delete this &#x22;Structuring This Skill&#x22; section after choosing your approach]

## Instructions

[TODO: Provide clear, step-by-step guidance using imperative/infinitive language]

[TODO: Reference any bundled resources (scripts, references, assets) so Claude knows how to use them]

Example structure:

1. First major step
2. Second major step
3. Third major step

## Bundled Resources

[TODO: Document bundled resources. Delete unused subsections.]

**scripts/** - Executable code run directly (not loaded into context)

- Example: &#x60;scripts/process_data.py&#x60; - Processes CSV and generates reports

**references/** - Documentation loaded into context when needed

- Example: &#x60;references/api_docs.md&#x60; - API endpoint documentation

**assets/** - Files used in output (not loaded into context)

- Example: &#x60;assets/template.pptx&#x60; - Presentation template

## Examples

[TODO: Show concrete examples with realistic user requests]" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>User: “Help me [specific task]”
Claude: [How the skill responds]</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="plaintext"><code><span class="line"><span></span></span>
<span class="line"><span>## Progressive Disclosure</span></span>
<span class="line"><span></span></span>
<span class="line"><span>Keep SKILL.md &#x3C;5k words. Move detailed info to references/. Three-level loading:</span></span>
<span class="line"><span>1. Metadata (~100 words) - Always in context</span></span>
<span class="line"><span>2. SKILL.md - Loaded when triggered</span></span>
<span class="line"><span>3. Bundled resources - Loaded as needed</span></span></code><button type="button" class="copy" data-code="
## Progressive Disclosure

Keep SKILL.md <5k words. Move detailed info to references/. Three-level loading:
1. Metadata (~100 words) - Always in context
2. SKILL.md - Loaded when triggered
3. Bundled resources - Loaded as needed" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
</li>
<li>
<p><strong>Create bundled resource placeholders (based on Step 4 analysis):</strong></p>
<p>For each directory determined in Step 4, create appropriate placeholder files:</p>
<p><strong>scripts/</strong> → Create <code>scripts/example.py</code> (executable Python template with TODO comment)
<strong>references/</strong> → Create <code>references/README.md</code> (documentation template explaining purpose)
<strong>assets/</strong> → Create <code>assets/README.md</code> (asset placeholder explaining common types)</p>
<p>Make scripts executable: <code>chmod +x scripts/*.py</code></p>
</li>
<li>
<p><strong>Follow official guidelines:</strong></p>
<ul>
<li>Name: lowercase, numbers, hyphens only (max 64 chars)</li>
<li>Description: Include triggers and use cases (max 1024 chars)</li>
<li>Instructions: Clear, step-by-step guidance</li>
<li>Keep skills focused on single capabilities</li>
<li>Make descriptions specific with trigger keywords</li>
</ul>
</li>
<li>
<p><strong>Output:</strong></p>
<ul>
<li>Print: <code>STATUS=CREATED PATH={{full_path}}</code></li>
<li>Summarize what was created and why (list directories + reasoning)</li>
<li>Remind user to populate placeholders and complete [TODO] items</li>
</ul>
</li>
</ol>
<h2 id="constraints">Constraints<a class="heading-link" aria-label="Link to section" href="#constraints"><span class="heading-link-icon">#</span></a></h2>
<ul>
<li>Skills are model-invoked (Claude decides when to use them)</li>
<li>Description must be specific enough for Claude to discover when to use it</li>
<li>One skill = one capability (stay focused)</li>
<li>Use forward slashes in all file paths</li>
<li>Valid YAML syntax required in frontmatter</li>
</ul>
<h2 id="frontmatter-properties">Frontmatter Properties<a class="heading-link" aria-label="Link to section" href="#frontmatter-properties"><span class="heading-link-icon">#</span></a></h2>
<p><strong>Required:</strong></p>
<ul>
<li><code>name</code> - Lowercase hyphen-case identifier (max 64 chars, matches directory name)</li>
<li><code>description</code> - What it does + when to use it (max 1024 chars, no angle brackets)</li>
</ul>
<p><strong>Optional:</strong></p>
<ul>
<li><code>allowed-tools: ["Read", "Write", "Bash"]</code> - Restrict Claude to specific tools</li>
<li><code>metadata: {category: "dev", version: "1.0"}</code> - Custom tracking fields</li>
<li><code>license: "MIT"</code> - License for shared skills</li>
</ul>
<p><strong>Prohibited</strong> (causes warnings):</p>
<ul>
<li><code>version</code>, <code>author</code>, <code>tags</code> - Use metadata or description instead</li>
</ul>
<h2 id="examples">Examples<a class="heading-link" aria-label="Link to section" href="#examples"><span class="heading-link-icon">#</span></a></h2>
<p><strong>Simple workflow skill:</strong></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#C0CAF5">/create-skill</span><span style="color:#9ECE6A"> commit-helper</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">Generate clear git commit messages from diffs. Use when writing commits or reviewing staged changes.</span><span style="color:#89DDFF">"</span></span></code><button type="button" class="copy" data-code="/create-skill commit-helper &#x22;Generate clear git commit messages from diffs. Use when writing commits or reviewing staged changes.&#x22;" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><em>Claude will determine: No bundled resources needed - just workflow guidance</em></p>
<p><strong>File manipulation skill:</strong></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#C0CAF5">/create-skill</span><span style="color:#9ECE6A"> pdf-processor</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">Extract text and tables from PDF files. Use when working with PDFs, forms, or document extraction.</span><span style="color:#89DDFF">"</span></span></code><button type="button" class="copy" data-code="/create-skill pdf-processor &#x22;Extract text and tables from PDF files. Use when working with PDFs, forms, or document extraction.&#x22;" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><em>Claude will determine: Needs scripts/ directory for PDF manipulation utilities</em></p>
<p><strong>API integration skill:</strong></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#C0CAF5">/create-skill</span><span style="color:#9ECE6A"> api-client</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">Make REST API calls and handle responses. Use for API testing and integration work with the company API.</span><span style="color:#89DDFF">"</span></span></code><button type="button" class="copy" data-code="/create-skill api-client &#x22;Make REST API calls and handle responses. Use for API testing and integration work with the company API.&#x22;" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><em>Claude will determine: Needs references/ directory for API documentation and schemas</em></p>
<p><strong>Image processing skill:</strong></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#C0CAF5">/create-skill</span><span style="color:#9ECE6A"> image-processor</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">Resize, rotate, and convert images. Use when editing images or batch processing files.</span><span style="color:#89DDFF">"</span></span></code><button type="button" class="copy" data-code="/create-skill image-processor &#x22;Resize, rotate, and convert images. Use when editing images or batch processing files.&#x22;" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><em>Claude will determine: Needs scripts/ directory for image manipulation operations</em></p>
<p><strong>Brand guidelines skill:</strong></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#C0CAF5">/create-skill</span><span style="color:#9ECE6A"> brand-guidelines</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">Apply company brand guidelines to designs. Use when creating presentations, documents, or marketing materials.</span><span style="color:#89DDFF">"</span></span></code><button type="button" class="copy" data-code="/create-skill brand-guidelines &#x22;Apply company brand guidelines to designs. Use when creating presentations, documents, or marketing materials.&#x22;" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><em>Claude will determine: Needs references/ for guidelines + assets/ for logos, fonts, templates</em></p>
<p><strong>Frontend builder skill:</strong></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#C0CAF5">/create-skill</span><span style="color:#9ECE6A"> frontend-builder</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">Build responsive web applications with React. Use when creating new frontend projects or components.</span><span style="color:#89DDFF">"</span><span style="color:#E0AF68"> --project</span></span></code><button type="button" class="copy" data-code="/create-skill frontend-builder &#x22;Build responsive web applications with React. Use when creating new frontend projects or components.&#x22; --project" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><em>Claude will determine: Needs scripts/ for build tools + assets/ for boilerplate templates</em></p>
<p><strong>Database query skill:</strong></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#C0CAF5">/create-skill</span><span style="color:#9ECE6A"> database-query</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">Query and analyze database tables. Use when working with SQL, BigQuery, or data analysis tasks.</span><span style="color:#89DDFF">"</span><span style="color:#E0AF68"> --project</span></span></code><button type="button" class="copy" data-code="/create-skill database-query &#x22;Query and analyze database tables. Use when working with SQL, BigQuery, or data analysis tasks.&#x22; --project" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><em>Claude will determine: Needs references/ for schema documentation</em></p>
<p><strong>How Claude determines what’s needed:</strong></p>
<ul>
<li>Mentions “PDF”, “images”, “documents”, “convert” → scripts/</li>
<li>Mentions “API”, “database”, “guidelines”, “standards” → references/</li>
<li>Mentions “templates”, “boilerplate”, “brand”, “presentations” → assets/</li>
<li>Simple workflow/process skills → SKILL.md only</li>
</ul>
<p><strong>Adding optional frontmatter properties:</strong></p>
<p>After creating a skill, you can manually edit SKILL.md to add optional frontmatter properties:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"><span style="color:#F7768E">name</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> database-query</span></span>
<span class="line"><span style="color:#F7768E">description</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Query and analyze database tables. Use when working with SQL, BigQuery, or data analysis tasks.</span></span>
<span class="line"><span style="color:#F7768E">allowed-tools</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> [</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">Bash</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">Read</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">Grep</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">]</span></span>
<span class="line"><span style="color:#F7768E">metadata</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#F7768E">  category</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">data</span><span style="color:#89DDFF">"</span></span>
<span class="line"><span style="color:#F7768E">  version</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">1.0.0</span><span style="color:#89DDFF">"</span></span>
<span class="line"><span style="color:#F7768E">  team</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">analytics</span><span style="color:#89DDFF">"</span></span>
<span class="line"><span style="color:#F7768E">license</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">MIT</span><span style="color:#89DDFF">"</span></span>
<span class="line"><span style="color:#89DDFF">---</span></span></code><button type="button" class="copy" data-code="---
name: database-query
description: Query and analyze database tables. Use when working with SQL, BigQuery, or data analysis tasks.
allowed-tools: [&#x22;Bash&#x22;, &#x22;Read&#x22;, &#x22;Grep&#x22;]
metadata:
  category: &#x22;data&#x22;
  version: &#x22;1.0.0&#x22;
  team: &#x22;analytics&#x22;
license: &#x22;MIT&#x22;
---" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h2 id="post-creation-workflow">Post-Creation Workflow<a class="heading-link" aria-label="Link to section" href="#post-creation-workflow"><span class="heading-link-icon">#</span></a></h2>
<p><strong>1. Edit</strong> - Complete [TODO] placeholders, populate bundled resources, add concrete examples</p>
<p><strong>2. Test</strong> - Restart Claude Code, test with trigger queries matching description</p>
<p><strong>3. Validate</strong> - Check frontmatter properties, description clarity, no sensitive data</p>
<p><strong>4. Iterate</strong> - Use on real tasks, update based on struggles/feedback</p>
<p><strong>Optional:</strong></p>
<ul>
<li>Package for distribution: Use packaging tools or <code>/create-plugin</code></li>
<li>Share with team: Distribute .zip or via plugin marketplace</li>
</ul>
<h2 id="example-well-structured-skill">Example: Well-Structured Skill<a class="heading-link" aria-label="Link to section" href="#example-well-structured-skill"><span class="heading-link-icon">#</span></a></h2>
<p>Here’s an example of a production-quality skill to demonstrate best practices:</p>
<p><strong>artifacts-builder</strong> - A skill for creating complex React/TypeScript artifacts with shadcn/ui</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="plaintext"><code><span class="line"><span>artifacts-builder/</span></span>
<span class="line"><span>├── SKILL.md (focused, ~75 lines)</span></span>
<span class="line"><span>└── scripts/</span></span>
<span class="line"><span>    ├── init-artifact.sh (323 lines - initializes React+Vite+shadcn project)</span></span>
<span class="line"><span>    ├── bundle-artifact.sh (54 lines - bundles to single HTML)</span></span>
<span class="line"><span>    └── shadcn-components.tar.gz (pre-packaged shadcn/ui components)</span></span></code><button type="button" class="copy" data-code="artifacts-builder/
├── SKILL.md (focused, ~75 lines)
└── scripts/
    ├── init-artifact.sh (323 lines - initializes React+Vite+shadcn project)
    ├── bundle-artifact.sh (54 lines - bundles to single HTML)
    └── shadcn-components.tar.gz (pre-packaged shadcn/ui components)" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><strong>SKILL.md structure:</strong></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"><span style="color:#F7768E">name</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> artifacts-builder</span></span>
<span class="line"><span style="color:#F7768E">description</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts.</span></span>
<span class="line"><span style="color:#F7768E">license</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Complete terms in LICENSE.txt</span></span>
<span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF;font-weight:bold">#</span><span style="color:#89DDFF;font-weight:bold"> Artifacts Builder</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">To build powerful frontend claude.ai artifacts, follow these steps:</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">1.</span><span style="color:#9AA5CE"> Initialize the frontend repo using </span><span style="color:#89DDFF">`scripts/init-artifact.sh`</span></span>
<span class="line"><span style="color:#89DDFF">2.</span><span style="color:#9AA5CE"> Develop your artifact by editing the generated code</span></span>
<span class="line"><span style="color:#89DDFF">3.</span><span style="color:#9AA5CE"> Bundle all code into a single HTML file using </span><span style="color:#89DDFF">`scripts/bundle-artifact.sh`</span></span>
<span class="line"><span style="color:#89DDFF">4.</span><span style="color:#9AA5CE"> Display artifact to user</span></span>
<span class="line"><span style="color:#89DDFF">5.</span><span style="color:#9AA5CE"> (Optional) Test the artifact</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**Stack**</span><span style="color:#9AA5CE">: React 18 + TypeScript + Vite + Parcel (bundling) + Tailwind CSS + shadcn/ui</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Design &#x26; Style Guidelines</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">VERY IMPORTANT: To avoid what is often referred to as "AI slop", avoid using excessive centered layouts, purple gradients, uniform rounded corners, and Inter font.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Quick Start</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Step 1: Initialize Project</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Run the initialization script to create a new React project:</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">```bash</span></span>
<span class="line"><span style="color:#C0CAF5">bash </span><span style="color:#9ECE6A">scripts/init-artifact.sh</span><span style="color:#89DDFF"> &#x3C;</span><span style="color:#9ECE6A">project-nam</span><span style="color:#C0CAF5">e</span><span style="color:#89DDFF">></span></span>
<span class="line"><span style="color:#0DB9D7">cd</span><span style="color:#89DDFF"> &#x3C;</span><span style="color:#9ECE6A">project-nam</span><span style="color:#C0CAF5">e</span><span style="color:#89DDFF">></span></span>
<span class="line"><span style="color:#89DDFF">```</span></span></code><button type="button" class="copy" data-code="---
name: artifacts-builder
description: Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts.
license: Complete terms in LICENSE.txt
---

# Artifacts Builder

To build powerful frontend claude.ai artifacts, follow these steps:

1. Initialize the frontend repo using &#x60;scripts/init-artifact.sh&#x60;
2. Develop your artifact by editing the generated code
3. Bundle all code into a single HTML file using &#x60;scripts/bundle-artifact.sh&#x60;
4. Display artifact to user
5. (Optional) Test the artifact

**Stack**: React 18 + TypeScript + Vite + Parcel (bundling) + Tailwind CSS + shadcn/ui

## Design &#x26; Style Guidelines

VERY IMPORTANT: To avoid what is often referred to as &#x22;AI slop&#x22;, avoid using excessive centered layouts, purple gradients, uniform rounded corners, and Inter font.

## Quick Start

### Step 1: Initialize Project

Run the initialization script to create a new React project:

&#x60;&#x60;&#x60;bash
bash scripts/init-artifact.sh <project-name>
cd <project-name>
&#x60;&#x60;&#x60;" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>This creates a fully configured project with:</p>
<ul>
<li>✅ React + TypeScript (via Vite)</li>
<li>✅ Tailwind CSS 3.4.1 with shadcn/ui theming system</li>
<li>✅ Path aliases (<code>@/</code>) configured</li>
<li>✅ 40+ shadcn/ui components pre-installed</li>
<li>✅ All Radix UI dependencies included</li>
<li>✅ Parcel configured for bundling</li>
<li>✅ Node 18+ compatibility</li>
</ul>
<h3 id="step-2-develop-your-artifact">Step 2: Develop Your Artifact<a class="heading-link" aria-label="Link to section" href="#step-2-develop-your-artifact"><span class="heading-link-icon">#</span></a></h3>
<p>To build the artifact, edit the generated files. See <strong>Common Development Tasks</strong> below for guidance.</p>
<h3 id="step-3-bundle-to-single-html-file">Step 3: Bundle to Single HTML File<a class="heading-link" aria-label="Link to section" href="#step-3-bundle-to-single-html-file"><span class="heading-link-icon">#</span></a></h3>
<p>To bundle the React app into a single HTML artifact:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#C0CAF5">bash</span><span style="color:#9ECE6A"> scripts/bundle-artifact.sh</span></span></code><button type="button" class="copy" data-code="bash scripts/bundle-artifact.sh" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>This creates <code>bundle.html</code> - a self-contained artifact with all JavaScript, CSS, and dependencies inlined.</p>
<h3 id="step-4-share-artifact-with-user">Step 4: Share Artifact with User<a class="heading-link" aria-label="Link to section" href="#step-4-share-artifact-with-user"><span class="heading-link-icon">#</span></a></h3>
<p>Finally, share the bundled HTML file in conversation with the user so they can view it as an artifact.</p>
<h3 id="step-5-testingvisualizing-the-artifact-optional">Step 5: Testing/Visualizing the Artifact (Optional)<a class="heading-link" aria-label="Link to section" href="#step-5-testingvisualizing-the-artifact-optional"><span class="heading-link-icon">#</span></a></h3>
<p>Note: This is a completely optional step. Only perform if necessary or requested.</p>
<h2 id="reference">Reference<a class="heading-link" aria-label="Link to section" href="#reference"><span class="heading-link-icon">#</span></a></h2>
<ul>
<li><strong>shadcn/ui components</strong>: <a href="https://ui.shadcn.com/docs/components" rel="noopener noreferrer" target="_blank">https://ui.shadcn.com/docs/components</a></li>
</ul>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="plaintext"><code><span class="line"><span></span></span>
<span class="line"><span>**What makes this skill excellent:**</span></span>
<span class="line"><span></span></span>
<span class="line"><span>1. **Clear, specific description** - States exactly what it does (React artifacts with shadcn/ui) and when NOT to use it (simple HTML)</span></span>
<span class="line"><span></span></span>
<span class="line"><span>2. **Task-Based organizational pattern** - Uses numbered steps (Quick Start → Step 1, 2, 3...) for clear workflow</span></span>
<span class="line"><span></span></span>
<span class="line"><span>3. **Practical scripts/** - Contains executable utilities that prevent rewriting the same setup code:</span></span>
<span class="line"><span>   - `init-artifact.sh` - Automates 20+ setup steps (Vite, Tailwind, shadcn/ui, dependencies)</span></span>
<span class="line"><span>   - `bundle-artifact.sh` - Bundles multi-file React app into single HTML</span></span>
<span class="line"><span>   - `shadcn-components.tar.gz` - Pre-packaged components (saves installation time)</span></span>
<span class="line"><span></span></span>
<span class="line"><span>4. **Focused SKILL.md** - Only ~75 lines, moves implementation details to scripts</span></span>
<span class="line"><span></span></span>
<span class="line"><span>5. **Domain-specific guidance** - Includes "Design &#x26; Style Guidelines" section with specific advice</span></span>
<span class="line"><span></span></span>
<span class="line"><span>6. **Optional license field** - Uses `license: Complete terms in LICENSE.txt` since Apache 2.0 is verbose</span></span>
<span class="line"><span></span></span>
<span class="line"><span>7. **Progressive disclosure** - Metadata (~50 words), SKILL.md core workflow (&#x3C;2k words), scripts executed without loading</span></span>
<span class="line"><span></span></span>
<span class="line"><span>8. **Explicit references** - Points to external docs (shadcn/ui) rather than duplicating them</span></span>
<span class="line"><span></span></span>
<span class="line"><span>**Claude Code would create scripts/ automatically for this skill because:**</span></span>
<span class="line"><span>- Description mentions "tools", "React", "Tailwind CSS", "shadcn/ui" (technical setup)</span></span>
<span class="line"><span>- Name "builder" implies construction/automation</span></span>
<span class="line"><span>- Description emphasizes "elaborate, multi-component" (complexity requiring tooling)</span></span>
<span class="line"><span></span></span>
<span class="line"><span>## Reference</span></span>
<span class="line"><span>Based on official Claude Code Agent Skills documentation:</span></span>
<span class="line"><span>- Personal skills: `~/.claude/skills/`</span></span>
<span class="line"><span>- Project skills: `.claude/skills/`</span></span>
<span class="line"><span>- Changes take effect on next Claude Code restart</span></span>
<span class="line"><span>- Test by asking questions matching the description triggers</span></span></code><button type="button" class="copy" data-code="
**What makes this skill excellent:**

1. **Clear, specific description** - States exactly what it does (React artifacts with shadcn/ui) and when NOT to use it (simple HTML)

2. **Task-Based organizational pattern** - Uses numbered steps (Quick Start → Step 1, 2, 3...) for clear workflow

3. **Practical scripts/** - Contains executable utilities that prevent rewriting the same setup code:
   - &#x60;init-artifact.sh&#x60; - Automates 20+ setup steps (Vite, Tailwind, shadcn/ui, dependencies)
   - &#x60;bundle-artifact.sh&#x60; - Bundles multi-file React app into single HTML
   - &#x60;shadcn-components.tar.gz&#x60; - Pre-packaged components (saves installation time)

4. **Focused SKILL.md** - Only ~75 lines, moves implementation details to scripts

5. **Domain-specific guidance** - Includes &#x22;Design &#x26; Style Guidelines&#x22; section with specific advice

6. **Optional license field** - Uses &#x60;license: Complete terms in LICENSE.txt&#x60; since Apache 2.0 is verbose

7. **Progressive disclosure** - Metadata (~50 words), SKILL.md core workflow (<2k words), scripts executed without loading

8. **Explicit references** - Points to external docs (shadcn/ui) rather than duplicating them

**Claude Code would create scripts/ automatically for this skill because:**
- Description mentions &#x22;tools&#x22;, &#x22;React&#x22;, &#x22;Tailwind CSS&#x22;, &#x22;shadcn/ui&#x22; (technical setup)
- Name &#x22;builder&#x22; implies construction/automation
- Description emphasizes &#x22;elaborate, multi-component&#x22; (complexity requiring tooling)

## Reference
Based on official Claude Code Agent Skills documentation:
- Personal skills: &#x60;~/.claude/skills/&#x60;
- Project skills: &#x60;.claude/skills/&#x60;
- Changes take effect on next Claude Code restart
- Test by asking questions matching the description triggers" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> </section> <!-- Usage Hint --> <aside class="text-sm text-skin-base/70"> <p>
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
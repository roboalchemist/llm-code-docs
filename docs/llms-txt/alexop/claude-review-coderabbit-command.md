# Source: https://alexop.dev/prompts/claude/claude-review-coderabbit-command

<!DOCTYPE html><html lang="en" class=" astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/prompts/claude/claude-review-coderabbit-command/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>Review CodeRabbit: Process AI Code Reviews | alexop.dev</title><meta name="title" content="Review CodeRabbit: Process AI Code Reviews | alexop.dev"><meta name="description" content="Agent that processes CodeRabbit review comments with technical rigor - verifies suggestions before implementing and pushes back when wrong"><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="Review CodeRabbit: Process AI Code Reviews | alexop.dev"><meta property="og:description" content="Agent that processes CodeRabbit review comments with technical rigor - verifies suggestions before implementing and pushes back when wrong"><meta property="og:url" content="https://alexop.dev/prompts/claude/claude-review-coderabbit-command/"><meta property="og:image" content="https://alexop.dev/prompts/claude/claude-review-coderabbit-command/index.png"><meta property="og:type" content="website"><!-- Article Published/Modified time --><meta property="article:published_time" content="2025-05-22T00:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/prompts/claude/claude-review-coderabbit-command/"><meta property="twitter:title" content="Review CodeRabbit: Process AI Code Reviews | alexop.dev"><meta property="twitter:description" content="Agent that processes CodeRabbit review comments with technical rigor - verifies suggestions before implementing and pushes back when wrong"><meta property="twitter:image" content="https://alexop.dev/prompts/claude/claude-review-coderabbit-command/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","headline":"Review CodeRabbit: Process AI Code Reviews | alexop.dev","description":"Agent that processes CodeRabbit review comments with technical rigor - verifies suggestions before implementing and pushes back when wrong","datePublished":"2025-05-22T00:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic","url":"https://alexop.dev"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <nav class="breadcrumb astro-ilhxcym7" aria-label="breadcrumb"> <ul class="astro-ilhxcym7"> <li class="astro-ilhxcym7"> <a href="/" class="astro-ilhxcym7">Home</a> <span aria-hidden="true" class="astro-ilhxcym7">&raquo;</span> </li> <li class="astro-ilhxcym7"> <a href="/prompts/" class="astro-ilhxcym7">prompts</a> <span aria-hidden="true" class="astro-ilhxcym7">&raquo;</span> </li><li class="astro-ilhxcym7"> <a href="/claude/" class="astro-ilhxcym7">claude</a> <span aria-hidden="true" class="astro-ilhxcym7">&raquo;</span> </li><li class="astro-ilhxcym7"> <span class="lowercase astro-ilhxcym7" aria-current="page">  claude-review-coderabbit-command </span> </li> </ul> </nav>  <main id="main-content" class="mx-auto max-w-4xl px-4 pb-12 pt-8"> <!-- Back Link --> <div class="mb-6"> <a href="/prompts/claude/" class="focus:ring-skin-accent inline-flex items-center gap-1 rounded-md px-3 py-1.5 text-sm text-skin-accent transition-colors hover:bg-skin-card focus:outline-none focus:ring-2 focus:ring-offset-2" onclick="event.preventDefault(); history.back();">
← Back to Claude Prompts
</a> </div> <!-- Header --> <header class="mb-8"> <h1 class="mb-4 text-3xl font-bold text-skin-base">Review CodeRabbit: Process AI Code Reviews</h1> <div class="mb-4 flex flex-wrap items-center gap-2"> <span class="inline-block rounded-md bg-skin-card px-2 py-1 text-xs " role="img" aria-label="Category: Agent"><span aria-hidden="true">🤖</span> <!-- -->Agent</span> <span class="inline-block rounded-md bg-skin-card px-2 py-1 text-xs"> Claude </span> <span class="text-sm text-skin-base/70">Claude Sonnet</span> </div> <div class="flex flex-wrap gap-2"> <a href="/prompts/?q=code-review" class="text-sm text-skin-base/70 transition-colors hover:text-skin-accent hover:underline">
#code-review </a><a href="/prompts/?q=coderabbit" class="text-sm text-skin-base/70 transition-colors hover:text-skin-accent hover:underline">
#coderabbit </a><a href="/prompts/?q=github" class="text-sm text-skin-base/70 transition-colors hover:text-skin-accent hover:underline">
#github </a><a href="/prompts/?q=pull-requests" class="text-sm text-skin-base/70 transition-colors hover:text-skin-accent hover:underline">
#pull-requests </a><a href="/prompts/?q=workflow" class="text-sm text-skin-base/70 transition-colors hover:text-skin-accent hover:underline">
#workflow </a> </div> </header> <!-- Description and Metadata --> <section class="mb-8"> <p class="mb-4 text-skin-base">Agent that processes CodeRabbit review comments with technical rigor - verifies suggestions before implementing and pushes back when wrong</p> <dl class="space-y-2 text-sm text-skin-base/70"> <div> <dt class="inline font-medium text-skin-base">
💡 Use Case:
</dt> <dd class="ml-2 inline">Processing automated code review feedback while maintaining code quality and avoiding unnecessary changes</dd> </div> <div> <dt class="inline font-medium text-skin-base">
📤 Expected Output:
</dt> <dd class="ml-2 inline">All CodeRabbit comments evaluated, valid issues fixed, invalid suggestions rejected with reasoning</dd> </div> <div> <dt class="inline font-medium text-skin-base">
✅ Success Rate:
</dt> <dd class="ml-2 inline capitalize">High - prevents blindly accepting AI suggestions</dd> </div> </dl> </section> <!-- Prompt Content --> <section class="mb-8"> <div class="mb-4 flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between"> <h2 class="text-lg font-semibold text-skin-base">Prompt Content</h2> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="Z1C5XQz" prefix="r3" component-url="/_astro/prompts.BTh7qZgL.js" component-export="PromptCopyButton" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;content&quot;:[0,&quot;---\ndescription: Fetch CodeRabbit review comments and process them with technical rigor - verify before implementing, push back when wrong\nallowed-tools: Bash(gh *), Bash(git *), Bash(pnpm typecheck*), Bash(pnpm lint*), Bash(pnpm test*), Bash(pnpm build*), Read, Glob, Grep, Edit, Write\n---\n\n# Review CodeRabbit Feedback\n\n## PR Context\n\n&lt;current_branch&gt;\n!`git branch --show-current`\n&lt;/current_branch&gt;\n\n&lt;pr_info&gt;\n!`gh pr view --json number,title,state,url 2&gt;&amp;1`\n&lt;/pr_info&gt;\n\n&lt;coderabbit_reviews&gt;\n!`gh pr view --json reviews --jq &#39;.reviews[] | select(.author.login == \&quot;coderabbitai\&quot;) | {state: .state, body: .body}&#39; 2&gt;&amp;1`\n&lt;/coderabbit_reviews&gt;\n\n&lt;coderabbit_comments&gt;\n!`gh pr view --json comments --jq &#39;.comments[] | select(.author.login == \&quot;coderabbitai\&quot;) | .body&#39; 2&gt;&amp;1`\n&lt;/coderabbit_comments&gt;\n\n&lt;review_threads&gt;\n!`gh api graphql -f query=&#39;query($owner: String!, $repo: String!, $pr: Int!) { repository(owner: $owner, name: $repo) { pullRequest(number: $pr) { reviewThreads(first: 100) { nodes { id isResolved path line comments(first: 10) { nodes { body author { login } } } } } } } }&#39; -F owner=\&quot;$(gh repo view --json owner -q .owner.login)\&quot; -F repo=\&quot;$(gh repo view --json name -q .name)\&quot; -F pr=\&quot;$(gh pr view --json number -q .number)\&quot; 2&gt;&amp;1 || echo \&quot;Could not fetch review threads\&quot;`\n&lt;/review_threads&gt;\n\n---\n\n## Decision Tree\n\n| Condition | Action |\n|-----------|--------|\n| No PR found | Branch has no PR. Create one first with `gh pr create` |\n| No CodeRabbit comments | No feedback to process. Done. |\n| Comments found | Continue to Review Reception Protocol below |\n\n---\n\n## Review Reception Protocol\n\n**CORE PRINCIPLE:** Verify before implementing. Ask before assuming. Technical correctness over social comfort.\n\n### The Response Pattern\n\n```\nFOR EACH CodeRabbit suggestion:\n\n1. READ: Complete feedback without reacting\n2. UNDERSTAND: Restate requirement in own words\n3. VERIFY: Check against codebase reality\n4. EVALUATE: Technically sound for THIS codebase?\n5. RESPOND: Technical acknowledgment or reasoned pushback\n6. IMPLEMENT: One item at a time, test each\n```\n\n### Forbidden Responses\n\n**NEVER say:**\n- \&quot;You&#39;re absolutely right!\&quot; (explicit CLAUDE.md violation)\n- \&quot;Great point!\&quot; / \&quot;Excellent feedback!\&quot; (performative)\n- \&quot;Let me implement that now\&quot; (before verification)\n- \&quot;Thanks for catching that!\&quot; (performative gratitude)\n\n**INSTEAD:**\n- Restate the technical requirement\n- Ask clarifying questions if needed\n- Push back with technical reasoning if wrong\n- Just fix it (actions &gt; words)\n\n---\n\n## Verification Checklist\n\nBEFORE implementing any CodeRabbit suggestion:\n\n- [ ] **Technically correct** for THIS codebase?\n- [ ] **Breaks existing functionality?** Check tests, grep for usage\n- [ ] **Reason for current implementation?** May be intentional\n- [ ] **Works on all platforms/versions?** Check compatibility\n- [ ] **Does reviewer understand full context?** AI may lack context\n\n### YAGNI Check\n\n```\nIF suggestion adds \&quot;proper\&quot; or \&quot;professional\&quot; features:\n  grep codebase for actual usage\n\n  IF unused: Consider removing (YAGNI) instead of improving\n  IF used: Then implement properly\n```\n\n---\n\n## When To Push Back\n\nPush back when:\n- Suggestion breaks existing functionality\n- Reviewer lacks full context (common with AI reviewers)\n- Violates YAGNI (unused feature)\n- Technically incorrect for this stack\n- Legacy/compatibility reasons exist\n- Conflicts with architectural decisions\n\n**How to push back:**\n```\n\&quot;Checked [X] - current implementation does [Y] because [reason].\nChanging to [suggestion] would [break/conflict with] [Z].\nKeep current approach? Or is there context I&#39;m missing?\&quot;\n```\n\n---\n\n## Processing CodeRabbit Feedback\n\n### Step 1: Categorize Each Item\n\n| Category | Priority | Action |\n|----------|----------|--------|\n| Security/Breaking | HIGH | Verify immediately, fix if confirmed |\n| Type errors/Bugs | HIGH | Verify locally, fix if real |\n| Style/Formatting | LOW | Check if matches project conventions |\n| \&quot;Best practices\&quot; | VERIFY | Check if actually applies here |\n| Refactoring suggestions | VERIFY | Check if code is actually used |\n\n### Step 2: Verify Before Acting\n\nFor each suggestion:\n1. **Read the referenced file** - understand current implementation\n2. **Check tests** - does current code pass? Would change break them?\n3. **Grep for usage** - is this code actually called?\n4. **Consider context** - why might it be written this way?\n\n### Step 3: Implementation Order\n\n```\nIF multiple items:\n  1. Clarify anything unclear FIRST\n  2. Then implement in order:\n     - Security/Breaking issues\n     - Confirmed bugs\n     - Simple fixes (imports, typos)\n     - Complex changes (refactoring)\n  3. Test each fix individually\n  4. Verify no regressions\n  5. RESOLVE each comment after addressing (see Resolution Protocol)\n```\n\n---\n\n## Acknowledging Correct Feedback\n\nWhen feedback IS correct:\n```\n- \&quot;Fixed. [Brief description of what changed]\&quot;\n- \&quot;Good catch - [specific issue]. Fixed in [location].\&quot;\n- [Just fix it and show in the code]\n```\n\nWhen you pushed back and were wrong:\n```\n\&quot;Verified this and you&#39;re correct. [Brief reason]. Fixing.\&quot;\n```\n\nNo long apologies. State correction factually and move on.\n\n---\n\n## Resolution Protocol\n\n**Every CodeRabbit comment MUST be resolved after processing.**\n\n&gt; **Note:** Resolving review threads requires the GraphQL API. The REST API does not support thread resolution.\n\n### Step 1: List Unresolved Review Threads\n\n```bash\n# Get all review threads with resolution status (GraphQL required)\ngh api graphql -f query=&#39;\nquery($owner: String!, $repo: String!, $pr: Int!) {\n  repository(owner: $owner, name: $repo) {\n    pullRequest(number: $pr) {\n      reviewThreads(first: 100) {\n        nodes {\n          id\n          isResolved\n          path\n          line\n          comments(first: 10) {\n            nodes {\n              body\n              author { login }\n            }\n          }\n        }\n      }\n    }\n  }\n}&#39; -F owner=\&quot;{owner}\&quot; -F repo=\&quot;{repo}\&quot; -F pr=\&quot;$(gh pr view --json number -q .number)\&quot;\n```\n\n### Step 2a: Resolve After Implementation\n\nWhen you implement a suggestion, resolve the thread directly (reply is optional - the commit speaks for itself):\n\n```bash\n# Resolve a review thread by its GraphQL node ID\ngh api graphql -f query=&#39;\nmutation($threadId: ID!) {\n  resolveReviewThread(input: {threadId: $threadId}) {\n    thread { isResolved }\n  }\n}&#39; -f threadId=\&quot;THREAD_NODE_ID\&quot;\n```\n\n### Step 2b: Reply and Resolve Without Implementation\n\nWhen you decide NOT to implement, reply with reasoning then resolve:\n\n```bash\n# Reply to a review thread (requires thread&#39;s GraphQL node ID)\ngh api graphql -f query=&#39;\nmutation($threadId: ID!, $body: String!) {\n  addPullRequestReviewThreadReply(input: {\n    pullRequestReviewThreadId: $threadId,\n    body: $body\n  }) {\n    comment { body }\n  }\n}&#39; -f threadId=\&quot;THREAD_NODE_ID\&quot; -f body=\&quot;Not implementing: [reason]\n\n- Current implementation does X because Y\n- Suggested change would [break/conflict with] Z\&quot;\n\n# Then resolve the thread\ngh api graphql -f query=&#39;\nmutation($threadId: ID!) {\n  resolveReviewThread(input: {threadId: $threadId}) {\n    thread { isResolved }\n  }\n}&#39; -f threadId=\&quot;THREAD_NODE_ID\&quot;\n```\n\n### Helper: Get Owner and Repo\n\n```bash\n# Extract owner/repo from current git remote\ngh repo view --json owner,name -q &#39;\&quot;\\(.owner.login)/\\(.name)\&quot;&#39;\n```\n\n### Resolution Checklist\n\nFor EACH CodeRabbit comment:\n- [ ] Evaluated (implemented or rejected with reason)\n- [ ] Response added (if rejecting - explain why)\n- [ ] Thread resolved via GraphQL mutation\n\n**Goal: Zero unresolved CodeRabbit comments when done.**\n\n---\n\n## Common CodeRabbit Patterns\n\n| Pattern | Verify |\n|---------|--------|\n| \&quot;Consider using X instead of Y\&quot; | Check if X works in this context |\n| \&quot;This could be simplified\&quot; | Check if simplification handles edge cases |\n| \&quot;Missing error handling\&quot; | Check if errors are handled elsewhere |\n| \&quot;Unused import/variable\&quot; | Verify with grep, may be used dynamically |\n| \&quot;Type could be more specific\&quot; | Check if generic type is intentional |\n| \&quot;Add documentation\&quot; | Check project conventions on docs |\n\n---\n\n## Red Flags - STOP and Verify\n\nIf you catch yourself:\n- Agreeing without checking the code\n- Implementing before understanding why current code exists\n- Not testing changes\n- Batch implementing without individual verification\n\n**STOP. You are being performative. Return to verification.**\n\n---\n\n## Summary\n\n**External AI feedback = suggestions to evaluate, not orders to follow.**\n\n1. Read all feedback first\n2. Verify each item against codebase\n3. Push back on incorrect suggestions\n4. Implement confirmed issues one at a time\n5. Test each change\n6. **Resolve every comment** (implemented or rejected with reason)\n\nNo performative agreement. Technical rigor always. Zero unresolved comments.&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PromptCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus:ring-skin-accent/20 inline-flex items-center gap-2 whitespace-nowrap rounded-lg border-2 border-skin-line bg-skin-card px-4 py-2.5 text-sm font-medium text-skin-base shadow-sm transition-all hover:border-skin-accent/50 hover:text-skin-accent focus:border-skin-accent focus:outline-none focus:ring-2" aria-label="Copy prompt to clipboard"><svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg>Copy Prompt</button><!--astro:end--></astro-island> </div> <div class="overflow-x-auto rounded-md border border-skin-line bg-skin-card p-4"> <div class="prose prose-sm max-w-none text-skin-base prose-headings:text-skin-base prose-p:text-skin-base prose-a:text-skin-accent prose-strong:text-skin-base prose-code:text-skin-base prose-pre:bg-skin-fill"> <hr>
<h2 id="description-fetch-coderabbit-review-comments-and-process-them-with-technical-rigor---verify-before-implementing-push-back-when-wrongallowed-tools-bashgh--bashgit--bashpnpm-typecheck-bashpnpm-lint-bashpnpm-test-bashpnpm-build-read-glob-grep-edit-write">description: Fetch CodeRabbit review comments and process them with technical rigor - verify before implementing, push back when wrong
allowed-tools: Bash(gh <em>), Bash(git <em>), Bash(pnpm typecheck</em>), Bash(pnpm lint</em>), Bash(pnpm test*), Bash(pnpm build*), Read, Glob, Grep, Edit, Write<a class="heading-link" aria-label="Link to section" href="#description-fetch-coderabbit-review-comments-and-process-them-with-technical-rigor---verify-before-implementing-push-back-when-wrongallowed-tools-bashgh--bashgit--bashpnpm-typecheck-bashpnpm-lint-bashpnpm-test-bashpnpm-build-read-glob-grep-edit-write"><span class="heading-link-icon">#</span></a></h2>
<h1 id="review-coderabbit-feedback">Review CodeRabbit Feedback</h1>
<h2 id="pr-context">PR Context<a class="heading-link" aria-label="Link to section" href="#pr-context"><span class="heading-link-icon">#</span></a></h2>
<p>&#x3C;current_branch>
!<code>git branch --show-current</code>
&#x3C;/current_branch></p>
<p>&#x3C;pr_info>
!<code>gh pr view --json number,title,state,url 2>&#x26;1</code>
&#x3C;/pr_info></p>
<p>&#x3C;coderabbit_reviews>
!<code>gh pr view --json reviews --jq '.reviews[] | select(.author.login == "coderabbitai") | {state: .state, body: .body}' 2>&#x26;1</code>
&#x3C;/coderabbit_reviews></p>
<p>&#x3C;coderabbit_comments>
!<code>gh pr view --json comments --jq '.comments[] | select(.author.login == "coderabbitai") | .body' 2>&#x26;1</code>
&#x3C;/coderabbit_comments></p>
<p>&#x3C;review_threads>
!<code>gh api graphql -f query='query($owner: String!, $repo: String!, $pr: Int!) { repository(owner: $owner, name: $repo) { pullRequest(number: $pr) { reviewThreads(first: 100) { nodes { id isResolved path line comments(first: 10) { nodes { body author { login } } } } } } } }' -F owner="$(gh repo view --json owner -q .owner.login)" -F repo="$(gh repo view --json name -q .name)" -F pr="$(gh pr view --json number -q .number)" 2>&#x26;1 || echo "Could not fetch review threads"</code>
&#x3C;/review_threads></p>
<hr>
<h2 id="decision-tree">Decision Tree<a class="heading-link" aria-label="Link to section" href="#decision-tree"><span class="heading-link-icon">#</span></a></h2>





















<table><thead><tr><th>Condition</th><th>Action</th></tr></thead><tbody><tr><td data-label="Condition">No PR found</td><td data-label="Action">Branch has no PR. Create one first with <code>gh pr create</code></td></tr><tr><td data-label="Condition">No CodeRabbit comments</td><td data-label="Action">No feedback to process. Done.</td></tr><tr><td data-label="Condition">Comments found</td><td data-label="Action">Continue to Review Reception Protocol below</td></tr></tbody></table>
<hr>
<h2 id="review-reception-protocol">Review Reception Protocol<a class="heading-link" aria-label="Link to section" href="#review-reception-protocol"><span class="heading-link-icon">#</span></a></h2>
<p><strong>CORE PRINCIPLE:</strong> Verify before implementing. Ask before assuming. Technical correctness over social comfort.</p>
<h3 id="the-response-pattern">The Response Pattern<a class="heading-link" aria-label="Link to section" href="#the-response-pattern"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="plaintext"><code><span class="line"><span>FOR EACH CodeRabbit suggestion:</span></span>
<span class="line"><span></span></span>
<span class="line"><span>1. READ: Complete feedback without reacting</span></span>
<span class="line"><span>2. UNDERSTAND: Restate requirement in own words</span></span>
<span class="line"><span>3. VERIFY: Check against codebase reality</span></span>
<span class="line"><span>4. EVALUATE: Technically sound for THIS codebase?</span></span>
<span class="line"><span>5. RESPOND: Technical acknowledgment or reasoned pushback</span></span>
<span class="line"><span>6. IMPLEMENT: One item at a time, test each</span></span></code><button type="button" class="copy" data-code="FOR EACH CodeRabbit suggestion:

1. READ: Complete feedback without reacting
2. UNDERSTAND: Restate requirement in own words
3. VERIFY: Check against codebase reality
4. EVALUATE: Technically sound for THIS codebase?
5. RESPOND: Technical acknowledgment or reasoned pushback
6. IMPLEMENT: One item at a time, test each" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="forbidden-responses">Forbidden Responses<a class="heading-link" aria-label="Link to section" href="#forbidden-responses"><span class="heading-link-icon">#</span></a></h3>
<p><strong>NEVER say:</strong></p>
<ul>
<li>“You’re absolutely right!” (explicit CLAUDE.md violation)</li>
<li>“Great point!” / “Excellent feedback!” (performative)</li>
<li>“Let me implement that now” (before verification)</li>
<li>“Thanks for catching that!” (performative gratitude)</li>
</ul>
<p><strong>INSTEAD:</strong></p>
<ul>
<li>Restate the technical requirement</li>
<li>Ask clarifying questions if needed</li>
<li>Push back with technical reasoning if wrong</li>
<li>Just fix it (actions > words)</li>
</ul>
<hr>
<h2 id="verification-checklist">Verification Checklist<a class="heading-link" aria-label="Link to section" href="#verification-checklist"><span class="heading-link-icon">#</span></a></h2>
<p>BEFORE implementing any CodeRabbit suggestion:</p>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> <strong>Technically correct</strong> for THIS codebase?</li>
<li class="task-list-item"><input type="checkbox" disabled> <strong>Breaks existing functionality?</strong> Check tests, grep for usage</li>
<li class="task-list-item"><input type="checkbox" disabled> <strong>Reason for current implementation?</strong> May be intentional</li>
<li class="task-list-item"><input type="checkbox" disabled> <strong>Works on all platforms/versions?</strong> Check compatibility</li>
<li class="task-list-item"><input type="checkbox" disabled> <strong>Does reviewer understand full context?</strong> AI may lack context</li>
</ul>
<h3 id="yagni-check">YAGNI Check<a class="heading-link" aria-label="Link to section" href="#yagni-check"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="plaintext"><code><span class="line"><span>IF suggestion adds "proper" or "professional" features:</span></span>
<span class="line"><span>  grep codebase for actual usage</span></span>
<span class="line"><span></span></span>
<span class="line"><span>  IF unused: Consider removing (YAGNI) instead of improving</span></span>
<span class="line"><span>  IF used: Then implement properly</span></span></code><button type="button" class="copy" data-code="IF suggestion adds &#x22;proper&#x22; or &#x22;professional&#x22; features:
  grep codebase for actual usage

  IF unused: Consider removing (YAGNI) instead of improving
  IF used: Then implement properly" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr>
<h2 id="when-to-push-back">When To Push Back<a class="heading-link" aria-label="Link to section" href="#when-to-push-back"><span class="heading-link-icon">#</span></a></h2>
<p>Push back when:</p>
<ul>
<li>Suggestion breaks existing functionality</li>
<li>Reviewer lacks full context (common with AI reviewers)</li>
<li>Violates YAGNI (unused feature)</li>
<li>Technically incorrect for this stack</li>
<li>Legacy/compatibility reasons exist</li>
<li>Conflicts with architectural decisions</li>
</ul>
<p><strong>How to push back:</strong></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="plaintext"><code><span class="line"><span>"Checked [X] - current implementation does [Y] because [reason].</span></span>
<span class="line"><span>Changing to [suggestion] would [break/conflict with] [Z].</span></span>
<span class="line"><span>Keep current approach? Or is there context I'm missing?"</span></span></code><button type="button" class="copy" data-code="&#x22;Checked [X] - current implementation does [Y] because [reason].
Changing to [suggestion] would [break/conflict with] [Z].
Keep current approach? Or is there context I&#x27;m missing?&#x22;" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr>
<h2 id="processing-coderabbit-feedback">Processing CodeRabbit Feedback<a class="heading-link" aria-label="Link to section" href="#processing-coderabbit-feedback"><span class="heading-link-icon">#</span></a></h2>
<h3 id="step-1-categorize-each-item">Step 1: Categorize Each Item<a class="heading-link" aria-label="Link to section" href="#step-1-categorize-each-item"><span class="heading-link-icon">#</span></a></h3>



































<table><thead><tr><th>Category</th><th>Priority</th><th>Action</th></tr></thead><tbody><tr><td data-label="Category">Security/Breaking</td><td data-label="Priority">HIGH</td><td data-label="Action">Verify immediately, fix if confirmed</td></tr><tr><td data-label="Category">Type errors/Bugs</td><td data-label="Priority">HIGH</td><td data-label="Action">Verify locally, fix if real</td></tr><tr><td data-label="Category">Style/Formatting</td><td data-label="Priority">LOW</td><td data-label="Action">Check if matches project conventions</td></tr><tr><td data-label="Category">”Best practices”</td><td data-label="Priority">VERIFY</td><td data-label="Action">Check if actually applies here</td></tr><tr><td data-label="Category">Refactoring suggestions</td><td data-label="Priority">VERIFY</td><td data-label="Action">Check if code is actually used</td></tr></tbody></table>
<h3 id="step-2-verify-before-acting">Step 2: Verify Before Acting<a class="heading-link" aria-label="Link to section" href="#step-2-verify-before-acting"><span class="heading-link-icon">#</span></a></h3>
<p>For each suggestion:</p>
<ol>
<li><strong>Read the referenced file</strong> - understand current implementation</li>
<li><strong>Check tests</strong> - does current code pass? Would change break them?</li>
<li><strong>Grep for usage</strong> - is this code actually called?</li>
<li><strong>Consider context</strong> - why might it be written this way?</li>
</ol>
<h3 id="step-3-implementation-order">Step 3: Implementation Order<a class="heading-link" aria-label="Link to section" href="#step-3-implementation-order"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="plaintext"><code><span class="line"><span>IF multiple items:</span></span>
<span class="line"><span>  1. Clarify anything unclear FIRST</span></span>
<span class="line"><span>  2. Then implement in order:</span></span>
<span class="line"><span>     - Security/Breaking issues</span></span>
<span class="line"><span>     - Confirmed bugs</span></span>
<span class="line"><span>     - Simple fixes (imports, typos)</span></span>
<span class="line"><span>     - Complex changes (refactoring)</span></span>
<span class="line"><span>  3. Test each fix individually</span></span>
<span class="line"><span>  4. Verify no regressions</span></span>
<span class="line"><span>  5. RESOLVE each comment after addressing (see Resolution Protocol)</span></span></code><button type="button" class="copy" data-code="IF multiple items:
  1. Clarify anything unclear FIRST
  2. Then implement in order:
     - Security/Breaking issues
     - Confirmed bugs
     - Simple fixes (imports, typos)
     - Complex changes (refactoring)
  3. Test each fix individually
  4. Verify no regressions
  5. RESOLVE each comment after addressing (see Resolution Protocol)" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr>
<h2 id="acknowledging-correct-feedback">Acknowledging Correct Feedback<a class="heading-link" aria-label="Link to section" href="#acknowledging-correct-feedback"><span class="heading-link-icon">#</span></a></h2>
<p>When feedback IS correct:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="plaintext"><code><span class="line"><span>- "Fixed. [Brief description of what changed]"</span></span>
<span class="line"><span>- "Good catch - [specific issue]. Fixed in [location]."</span></span>
<span class="line"><span>- [Just fix it and show in the code]</span></span></code><button type="button" class="copy" data-code="- &#x22;Fixed. [Brief description of what changed]&#x22;
- &#x22;Good catch - [specific issue]. Fixed in [location].&#x22;
- [Just fix it and show in the code]" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>When you pushed back and were wrong:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="plaintext"><code><span class="line"><span>"Verified this and you're correct. [Brief reason]. Fixing."</span></span></code><button type="button" class="copy" data-code="&#x22;Verified this and you&#x27;re correct. [Brief reason]. Fixing.&#x22;" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>No long apologies. State correction factually and move on.</p>
<hr>
<h2 id="resolution-protocol">Resolution Protocol<a class="heading-link" aria-label="Link to section" href="#resolution-protocol"><span class="heading-link-icon">#</span></a></h2>
<p><strong>Every CodeRabbit comment MUST be resolved after processing.</strong></p>
<blockquote>
<p><strong>Note:</strong> Resolving review threads requires the GraphQL API. The REST API does not support thread resolution.</p>
</blockquote>
<h3 id="step-1-list-unresolved-review-threads">Step 1: List Unresolved Review Threads<a class="heading-link" aria-label="Link to section" href="#step-1-list-unresolved-review-threads"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#51597D;font-style:italic"># Get all review threads with resolution status (GraphQL required)</span></span>
<span class="line"><span style="color:#C0CAF5">gh</span><span style="color:#9ECE6A"> api</span><span style="color:#9ECE6A"> graphql</span><span style="color:#E0AF68"> -f</span><span style="color:#9ECE6A"> query=</span><span style="color:#89DDFF">'</span></span>
<span class="line"><span style="color:#9ECE6A">query($owner: String!, $repo: String!, $pr: Int!) {</span></span>
<span class="line"><span style="color:#9ECE6A">  repository(owner: $owner, name: $repo) {</span></span>
<span class="line"><span style="color:#9ECE6A">    pullRequest(number: $pr) {</span></span>
<span class="line"><span style="color:#9ECE6A">      reviewThreads(first: 100) {</span></span>
<span class="line"><span style="color:#9ECE6A">        nodes {</span></span>
<span class="line"><span style="color:#9ECE6A">          id</span></span>
<span class="line"><span style="color:#9ECE6A">          isResolved</span></span>
<span class="line"><span style="color:#9ECE6A">          path</span></span>
<span class="line"><span style="color:#9ECE6A">          line</span></span>
<span class="line"><span style="color:#9ECE6A">          comments(first: 10) {</span></span>
<span class="line"><span style="color:#9ECE6A">            nodes {</span></span>
<span class="line"><span style="color:#9ECE6A">              body</span></span>
<span class="line"><span style="color:#9ECE6A">              author { login }</span></span>
<span class="line"><span style="color:#9ECE6A">            }</span></span>
<span class="line"><span style="color:#9ECE6A">          }</span></span>
<span class="line"><span style="color:#9ECE6A">        }</span></span>
<span class="line"><span style="color:#9ECE6A">      }</span></span>
<span class="line"><span style="color:#9ECE6A">    }</span></span>
<span class="line"><span style="color:#9ECE6A">  }</span></span>
<span class="line"><span style="color:#9ECE6A">}</span><span style="color:#89DDFF">'</span><span style="color:#E0AF68"> -F</span><span style="color:#9ECE6A"> owner=</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">{owner}</span><span style="color:#89DDFF">"</span><span style="color:#E0AF68"> -F</span><span style="color:#9ECE6A"> repo=</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">{repo}</span><span style="color:#89DDFF">"</span><span style="color:#E0AF68"> -F</span><span style="color:#9ECE6A"> pr=</span><span style="color:#89DDFF">"$(</span><span style="color:#C0CAF5">gh</span><span style="color:#9ECE6A"> pr view </span><span style="color:#E0AF68">--json</span><span style="color:#9ECE6A"> number </span><span style="color:#E0AF68">-q</span><span style="color:#9ECE6A"> .number</span><span style="color:#89DDFF">)"</span></span></code><button type="button" class="copy" data-code="# Get all review threads with resolution status (GraphQL required)
gh api graphql -f query=&#x27;
query($owner: String!, $repo: String!, $pr: Int!) {
  repository(owner: $owner, name: $repo) {
    pullRequest(number: $pr) {
      reviewThreads(first: 100) {
        nodes {
          id
          isResolved
          path
          line
          comments(first: 10) {
            nodes {
              body
              author { login }
            }
          }
        }
      }
    }
  }
}&#x27; -F owner=&#x22;{owner}&#x22; -F repo=&#x22;{repo}&#x22; -F pr=&#x22;$(gh pr view --json number -q .number)&#x22;" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="step-2a-resolve-after-implementation">Step 2a: Resolve After Implementation<a class="heading-link" aria-label="Link to section" href="#step-2a-resolve-after-implementation"><span class="heading-link-icon">#</span></a></h3>
<p>When you implement a suggestion, resolve the thread directly (reply is optional - the commit speaks for itself):</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#51597D;font-style:italic"># Resolve a review thread by its GraphQL node ID</span></span>
<span class="line"><span style="color:#C0CAF5">gh</span><span style="color:#9ECE6A"> api</span><span style="color:#9ECE6A"> graphql</span><span style="color:#E0AF68"> -f</span><span style="color:#9ECE6A"> query=</span><span style="color:#89DDFF">'</span></span>
<span class="line"><span style="color:#9ECE6A">mutation($threadId: ID!) {</span></span>
<span class="line"><span style="color:#9ECE6A">  resolveReviewThread(input: {threadId: $threadId}) {</span></span>
<span class="line"><span style="color:#9ECE6A">    thread { isResolved }</span></span>
<span class="line"><span style="color:#9ECE6A">  }</span></span>
<span class="line"><span style="color:#9ECE6A">}</span><span style="color:#89DDFF">'</span><span style="color:#E0AF68"> -f</span><span style="color:#9ECE6A"> threadId=</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">THREAD_NODE_ID</span><span style="color:#89DDFF">"</span></span></code><button type="button" class="copy" data-code="# Resolve a review thread by its GraphQL node ID
gh api graphql -f query=&#x27;
mutation($threadId: ID!) {
  resolveReviewThread(input: {threadId: $threadId}) {
    thread { isResolved }
  }
}&#x27; -f threadId=&#x22;THREAD_NODE_ID&#x22;" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="step-2b-reply-and-resolve-without-implementation">Step 2b: Reply and Resolve Without Implementation<a class="heading-link" aria-label="Link to section" href="#step-2b-reply-and-resolve-without-implementation"><span class="heading-link-icon">#</span></a></h3>
<p>When you decide NOT to implement, reply with reasoning then resolve:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#51597D;font-style:italic"># Reply to a review thread (requires thread's GraphQL node ID)</span></span>
<span class="line"><span style="color:#C0CAF5">gh</span><span style="color:#9ECE6A"> api</span><span style="color:#9ECE6A"> graphql</span><span style="color:#E0AF68"> -f</span><span style="color:#9ECE6A"> query=</span><span style="color:#89DDFF">'</span></span>
<span class="line"><span style="color:#9ECE6A">mutation($threadId: ID!, $body: String!) {</span></span>
<span class="line"><span style="color:#9ECE6A">  addPullRequestReviewThreadReply(input: {</span></span>
<span class="line"><span style="color:#9ECE6A">    pullRequestReviewThreadId: $threadId,</span></span>
<span class="line"><span style="color:#9ECE6A">    body: $body</span></span>
<span class="line"><span style="color:#9ECE6A">  }) {</span></span>
<span class="line"><span style="color:#9ECE6A">    comment { body }</span></span>
<span class="line"><span style="color:#9ECE6A">  }</span></span>
<span class="line"><span style="color:#9ECE6A">}</span><span style="color:#89DDFF">'</span><span style="color:#E0AF68"> -f</span><span style="color:#9ECE6A"> threadId=</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">THREAD_NODE_ID</span><span style="color:#89DDFF">"</span><span style="color:#E0AF68"> -f</span><span style="color:#9ECE6A"> body=</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">Not implementing: [reason]</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9ECE6A">- Current implementation does X because Y</span></span>
<span class="line"><span style="color:#9ECE6A">- Suggested change would [break/conflict with] Z</span><span style="color:#89DDFF">"</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic"># Then resolve the thread</span></span>
<span class="line"><span style="color:#C0CAF5">gh</span><span style="color:#9ECE6A"> api</span><span style="color:#9ECE6A"> graphql</span><span style="color:#E0AF68"> -f</span><span style="color:#9ECE6A"> query=</span><span style="color:#89DDFF">'</span></span>
<span class="line"><span style="color:#9ECE6A">mutation($threadId: ID!) {</span></span>
<span class="line"><span style="color:#9ECE6A">  resolveReviewThread(input: {threadId: $threadId}) {</span></span>
<span class="line"><span style="color:#9ECE6A">    thread { isResolved }</span></span>
<span class="line"><span style="color:#9ECE6A">  }</span></span>
<span class="line"><span style="color:#9ECE6A">}</span><span style="color:#89DDFF">'</span><span style="color:#E0AF68"> -f</span><span style="color:#9ECE6A"> threadId=</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">THREAD_NODE_ID</span><span style="color:#89DDFF">"</span></span></code><button type="button" class="copy" data-code="# Reply to a review thread (requires thread&#x27;s GraphQL node ID)
gh api graphql -f query=&#x27;
mutation($threadId: ID!, $body: String!) {
  addPullRequestReviewThreadReply(input: {
    pullRequestReviewThreadId: $threadId,
    body: $body
  }) {
    comment { body }
  }
}&#x27; -f threadId=&#x22;THREAD_NODE_ID&#x22; -f body=&#x22;Not implementing: [reason]

- Current implementation does X because Y
- Suggested change would [break/conflict with] Z&#x22;

# Then resolve the thread
gh api graphql -f query=&#x27;
mutation($threadId: ID!) {
  resolveReviewThread(input: {threadId: $threadId}) {
    thread { isResolved }
  }
}&#x27; -f threadId=&#x22;THREAD_NODE_ID&#x22;" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="helper-get-owner-and-repo">Helper: Get Owner and Repo<a class="heading-link" aria-label="Link to section" href="#helper-get-owner-and-repo"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#51597D;font-style:italic"># Extract owner/repo from current git remote</span></span>
<span class="line"><span style="color:#C0CAF5">gh</span><span style="color:#9ECE6A"> repo</span><span style="color:#9ECE6A"> view</span><span style="color:#E0AF68"> --json</span><span style="color:#9ECE6A"> owner,name</span><span style="color:#E0AF68"> -q</span><span style="color:#89DDFF"> '</span><span style="color:#9ECE6A">"\(.owner.login)/\(.name)"</span><span style="color:#89DDFF">'</span></span></code><button type="button" class="copy" data-code="# Extract owner/repo from current git remote
gh repo view --json owner,name -q &#x27;&#x22;\(.owner.login)/\(.name)&#x22;&#x27;" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="resolution-checklist">Resolution Checklist<a class="heading-link" aria-label="Link to section" href="#resolution-checklist"><span class="heading-link-icon">#</span></a></h3>
<p>For EACH CodeRabbit comment:</p>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> Evaluated (implemented or rejected with reason)</li>
<li class="task-list-item"><input type="checkbox" disabled> Response added (if rejecting - explain why)</li>
<li class="task-list-item"><input type="checkbox" disabled> Thread resolved via GraphQL mutation</li>
</ul>
<p><strong>Goal: Zero unresolved CodeRabbit comments when done.</strong></p>
<hr>
<h2 id="common-coderabbit-patterns">Common CodeRabbit Patterns<a class="heading-link" aria-label="Link to section" href="#common-coderabbit-patterns"><span class="heading-link-icon">#</span></a></h2>

































<table><thead><tr><th>Pattern</th><th>Verify</th></tr></thead><tbody><tr><td data-label="Pattern">”Consider using X instead of Y”</td><td data-label="Verify">Check if X works in this context</td></tr><tr><td data-label="Pattern">”This could be simplified”</td><td data-label="Verify">Check if simplification handles edge cases</td></tr><tr><td data-label="Pattern">”Missing error handling”</td><td data-label="Verify">Check if errors are handled elsewhere</td></tr><tr><td data-label="Pattern">”Unused import/variable”</td><td data-label="Verify">Verify with grep, may be used dynamically</td></tr><tr><td data-label="Pattern">”Type could be more specific”</td><td data-label="Verify">Check if generic type is intentional</td></tr><tr><td data-label="Pattern">”Add documentation”</td><td data-label="Verify">Check project conventions on docs</td></tr></tbody></table>
<hr>
<h2 id="red-flags---stop-and-verify">Red Flags - STOP and Verify<a class="heading-link" aria-label="Link to section" href="#red-flags---stop-and-verify"><span class="heading-link-icon">#</span></a></h2>
<p>If you catch yourself:</p>
<ul>
<li>Agreeing without checking the code</li>
<li>Implementing before understanding why current code exists</li>
<li>Not testing changes</li>
<li>Batch implementing without individual verification</li>
</ul>
<p><strong>STOP. You are being performative. Return to verification.</strong></p>
<hr>
<h2 id="summary">Summary<a class="heading-link" aria-label="Link to section" href="#summary"><span class="heading-link-icon">#</span></a></h2>
<p><strong>External AI feedback = suggestions to evaluate, not orders to follow.</strong></p>
<ol>
<li>Read all feedback first</li>
<li>Verify each item against codebase</li>
<li>Push back on incorrect suggestions</li>
<li>Implement confirmed issues one at a time</li>
<li>Test each change</li>
<li><strong>Resolve every comment</strong> (implemented or rejected with reason)</li>
</ol>
<p>No performative agreement. Technical rigor always. Zero unresolved comments.</p> </div> </div> </section> <!-- Usage Hint --> <aside class="text-sm text-skin-base/70"> <p>
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
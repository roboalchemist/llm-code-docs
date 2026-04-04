# Source: https://alexop.dev/posts/why-you-dont-need-nuxt-mcp-claude-code

<!DOCTYPE html><html lang="en" class="scroll-smooth astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/posts/why-you-dont-need-nuxt-mcp-claude-code/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>Why You Don&#39;t Need the Nuxt MCP When You Use Claude Code | alexop.dev</title><meta name="title" content="Why You Don't Need the Nuxt MCP When You Use Claude Code | alexop.dev"><meta name="description" content="Why I use custom research agents instead of MCP servers for AI-assisted development. Learn how llms.txt enables context-efficient documentation fetching with a practical Nuxt Content agent example."><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="Why You Don't Need the Nuxt MCP When You Use Claude Code | alexop.dev"><meta property="og:description" content="Why I use custom research agents instead of MCP servers for AI-assisted development. Learn how llms.txt enables context-efficient documentation fetching with a practical Nuxt Content agent example."><meta property="og:url" content="https://alexop.dev/posts/why-you-dont-need-nuxt-mcp-claude-code/"><meta property="og:image" content="https://alexop.dev/posts/why-you-dont-need-the-nuxt-mcp-when-you-use-claude-code/index.png"><meta property="og:type" content="article"><!-- Article Published/Modified time --><meta property="article:published_time" content="2025-12-31T00:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/posts/why-you-dont-need-nuxt-mcp-claude-code/"><meta property="twitter:title" content="Why You Don't Need the Nuxt MCP When You Use Claude Code | alexop.dev"><meta property="twitter:description" content="Why I use custom research agents instead of MCP servers for AI-assisted development. Learn how llms.txt enables context-efficient documentation fetching with a practical Nuxt Content agent example."><meta property="twitter:image" content="https://alexop.dev/posts/why-you-dont-need-the-nuxt-mcp-when-you-use-claude-code/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"Why You Don't Need the Nuxt MCP When You Use Claude Code | alexop.dev","description":"Why I use custom research agents instead of MCP servers for AI-assisted development. Learn how llms.txt enables context-efficient documentation fetching with a practical Nuxt Content agent example.","image":"https://alexop.dev/posts/why-you-dont-need-the-nuxt-mcp-when-you-use-claude-code/index.png","datePublished":"2025-12-31T00:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
<style>a:where(.astro-blwjyjpt){transition:all .3s ease}a:where(.astro-blwjyjpt):hover{transform:translateY(-2px);box-shadow:0 4px 6px -1px #0000001a,0 2px 4px -1px #0000000f}
.minimal-posts-list:where(.astro-eenky23y){width:100%;max-width:64rem;margin:0 auto;padding:2rem 1rem;background:rgb(var(--color-fill));color:rgb(var(--color-text-base))}.posts-title:where(.astro-eenky23y){font-size:2rem;margin-bottom:2rem;color:rgb(var(--color-accent));font-family:inherit;font-weight:600;letter-spacing:.02em}.year-group:where(.astro-eenky23y){margin-bottom:2.5rem}.year-heading:where(.astro-eenky23y){font-size:1.3rem;color:rgb(var(--color-text-base));margin:2.5rem 0 1.2rem;font-family:inherit;font-weight:500;letter-spacing:.04em}.year-group:where(.astro-eenky23y) ul:where(.astro-eenky23y){list-style:none;padding:0;margin:0}.post-item:where(.astro-eenky23y){display:flex;justify-content:space-between;align-items:center;padding:1rem 0;border-bottom:1px solid rgba(var(--color-border),.2)}.post-link:where(.astro-eenky23y){color:rgb(var(--color-text-base));text-decoration:none;font-size:1.1rem;transition:color .2s}.post-link:where(.astro-eenky23y):hover{color:rgb(var(--color-accent))}.post-date:where(.astro-eenky23y){color:rgb(var(--color-card-muted));font-size:.95rem;font-family:inherit;letter-spacing:.05em;min-width:70px;text-align:right}
@keyframes astroFadeInOut{0%{opacity:1}to{opacity:0}}@keyframes astroFadeIn{0%{opacity:0;mix-blend-mode:plus-lighter}to{opacity:1;mix-blend-mode:plus-lighter}}@keyframes astroFadeOut{0%{opacity:1;mix-blend-mode:plus-lighter}to{opacity:0;mix-blend-mode:plus-lighter}}@keyframes astroSlideFromRight{0%{transform:translate(100%)}}@keyframes astroSlideFromLeft{0%{transform:translate(-100%)}}@keyframes astroSlideToRight{to{transform:translate(100%)}}@keyframes astroSlideToLeft{to{transform:translate(-100%)}}@media(prefers-reduced-motion){::view-transition-group(*),::view-transition-old(*),::view-transition-new(*){animation:none!important}[data-astro-transition-scope]{animation:none!important}}
</style>
<link rel="stylesheet" href="/_astro/index.Ck-KI3hC.css">
<style>.subagent-diagram-container:where(.astro-tpygpejy){display:flex;flex-direction:column;align-items:center;margin:2rem 0;width:100%}.subagent-diagram-fallback:where(.astro-tpygpejy){width:100%;max-width:600px}.subagent-diagram-svg:where(.astro-tpygpejy){width:100%;height:auto}.agent-circle:where(.astro-tpygpejy){fill:rgb(var(--color-accent) / .1);stroke:rgb(var(--color-accent));stroke-width:2}.subagent-circle:where(.astro-tpygpejy){fill:rgb(var(--color-accent) / .05);stroke:rgb(var(--color-accent) / .7);stroke-width:2;stroke-dasharray:4 2}.agent-icon:where(.astro-tpygpejy){font-size:24px}.agent-label:where(.astro-tpygpejy){fill:rgb(var(--color-text-base));font-size:12px;font-weight:500}.arrow-path:where(.astro-tpygpejy){fill:none;stroke:rgb(var(--color-text-base) / .5);stroke-width:2}.arrow-path:where(.astro-tpygpejy).dashed{stroke-dasharray:5 3}.arrow-path:where(.astro-tpygpejy).search-arrow{stroke:rgb(var(--color-accent) / .6)}.arrowhead-fill:where(.astro-tpygpejy){fill:rgb(var(--color-text-base) / .5)}.arrow-label:where(.astro-tpygpejy){fill:rgb(var(--color-text-base) / .6);font-size:11px;font-style:italic}.file-tree:where(.astro-tpygpejy) .folder:where(.astro-tpygpejy){fill:rgb(var(--color-text-base));font-size:14px;font-family:ui-monospace,monospace}.file-tree:where(.astro-tpygpejy) .file:where(.astro-tpygpejy){fill:rgb(var(--color-text-base) / .7);font-size:14px;font-family:ui-monospace,monospace}.file-tree:where(.astro-tpygpejy) .file:where(.astro-tpygpejy).highlight{fill:rgb(var(--color-accent));font-weight:600}.subagent-diagram-caption:where(.astro-tpygpejy){margin-top:1rem;text-align:center;font-size:.875rem;color:rgb(var(--color-text-base) / .7)}.subagent-diagram-fallback:where(.astro-tpygpejy){display:none}
.parallel-subagent-diagram-container:where(.astro-u2chhpb2){display:flex;flex-direction:column;align-items:center;margin:2rem 0;width:100%}.parallel-subagent-diagram-fallback:where(.astro-u2chhpb2){width:100%;max-width:800px}.parallel-subagent-diagram-svg-static:where(.astro-u2chhpb2){width:100%;height:auto}.agent-circle:where(.astro-u2chhpb2){fill:rgb(var(--color-accent) / .1);stroke:rgb(var(--color-accent));stroke-width:2}.subagent-circle:where(.astro-u2chhpb2){stroke-width:2;stroke-dasharray:4 2}.agent-icon:where(.astro-u2chhpb2){font-size:24px}.agent-label:where(.astro-u2chhpb2){fill:rgb(var(--color-text-base));font-size:12px;font-weight:500}.task-label:where(.astro-u2chhpb2){fill:rgb(var(--color-text-base) / .8);font-size:13px;font-family:ui-monospace,monospace}.arrow-path:where(.astro-u2chhpb2){fill:none;stroke:rgb(var(--color-text-base) / .5);stroke-width:2}.arrow-path:where(.astro-u2chhpb2).dashed{stroke-dasharray:5 3}.arrow-path:where(.astro-u2chhpb2).report{stroke:#22c55e}.arrowhead-fill:where(.astro-u2chhpb2){fill:rgb(var(--color-text-base) / .5)}.domain-box-rect:where(.astro-u2chhpb2){fill:rgb(var(--color-fill) / .5);stroke-width:1.5}.domain-label:where(.astro-u2chhpb2){font-size:11px;font-weight:600}.finding-text:where(.astro-u2chhpb2){fill:rgb(var(--color-text-base) / .7);font-size:10px;font-family:ui-monospace,monospace}.synthesis-box:where(.astro-u2chhpb2){fill:#22c55e1a;stroke:#22c55e;stroke-width:2}.synthesis-text:where(.astro-u2chhpb2){fill:#22c55e;font-size:13px;font-weight:600}.parallel-subagent-diagram-caption:where(.astro-u2chhpb2){margin-top:1rem;text-align:center;font-size:.875rem;color:rgb(var(--color-text-base) / .7)}.parallel-subagent-diagram-fallback:where(.astro-u2chhpb2){display:none}
.shiki-magic-move-container{position:relative;white-space:pre}.shiki-magic-move-line-number{opacity:.3;-webkit-user-select:none;-moz-user-select:none;user-select:none}.shiki-magic-move-item{display:inline-block;transition:color var(--smm-duration,.5s) var(--smm-easing,"ease")}.shiki-magic-move-enter-active,.shiki-magic-move-leave-active,.shiki-magic-move-move{transition:all var(--smm-duration,.5s) var(--smm-easing,"ease")}.shiki-magic-move-container-resize,.shiki-magic-move-container-restyle{transition:all var(--smm-duration,.5s) var(--smm-easing,"ease");transition-delay:calc(var(--smm-duration, .5s)*var(--smm-delay-container, 1))}.shiki-magic-move-move{transition-delay:calc(var(--smm-duration, .5s)*var(--smm-delay-move, 1) + var(--smm-stagger, 0));z-index:1}.shiki-magic-move-enter-active{transition-delay:calc(var(--smm-duration, .5s)*var(--smm-delay-enter, 1) + var(--smm-stagger, 0));z-index:1}.shiki-magic-move-leave-active{transition-delay:calc(var(--smm-duration, .5s)*var(--smm-delay-leave, 1) + var(--smm-stagger, 0))}.shiki-magic-move-enter-from,.shiki-magic-move-leave-to{opacity:0}br.shiki-magic-move-leave-active{display:none}
.jazz-demo-root[data-v-d8349330]{background:#030712;border:1px solid #374151;border-radius:.75rem;padding:1rem;font-family:system-ui,-apple-system,sans-serif;color:#e5e7eb;font-size:14px}.jazz-demo-header[data-v-d8349330]{display:flex;align-items:center;justify-content:space-between;margin-bottom:1rem}.jazz-demo-title[data-v-d8349330]{color:#fff;font-size:1rem;font-weight:600}.jazz-demo-toggles[data-v-d8349330]{display:flex;align-items:center;gap:.75rem}.jazz-demo-toggle-wrap[data-v-d8349330]{display:flex;align-items:center;gap:.5rem}.jazz-demo-toggle-label[data-v-d8349330]{color:#d1d5db;font-size:.75rem}.jazz-demo-toggle[data-v-d8349330]{position:relative;display:inline-flex;height:1.25rem;width:2.25rem;align-items:center;border-radius:9999px;transition:background-color .2s;border:none;cursor:pointer;padding:0}.jazz-demo-toggle-on[data-v-d8349330]{background:#2563eb}.jazz-demo-toggle-off[data-v-d8349330]{background:#4b5563}.jazz-demo-toggle-dot[data-v-d8349330]{display:inline-block;height:.875rem;width:.875rem;border-radius:9999px;background:#fff;transition:transform .2s}.jazz-demo-toggle-dot-on[data-v-d8349330]{transform:translate(1.125rem)}.jazz-demo-toggle-dot-off[data-v-d8349330]{transform:translate(.125rem)}.jazz-demo-covalue-id[data-v-d8349330]{display:flex;align-items:center;gap:.375rem;margin-bottom:.5rem;padding:.25rem .5rem;background:#1e1b4b;border:1px solid #3730a3;border-radius:.375rem;overflow:hidden}.jazz-demo-covalue-label[data-v-d8349330]{color:#a78bfa;font-size:.625rem;font-weight:600;white-space:nowrap}.jazz-demo-covalue-code[data-v-d8349330]{color:#c4b5fd;font-size:.625rem;font-family:ui-monospace,monospace;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.jazz-demo-card[data-v-d8349330]{background:#111827;border:1px solid #374151;border-radius:.75rem;padding:1rem}.jazz-demo-loading[data-v-d8349330]{color:#9ca3af;text-align:center;padding:2rem 0}.jazz-demo-card-title[data-v-d8349330]{font-size:1.25rem;font-weight:700;color:#fff;margin:0 0 .75rem}.jazz-demo-form[data-v-d8349330]{margin-bottom:.75rem;display:flex;flex-direction:column;gap:.5rem}.jazz-demo-input[data-v-d8349330]{width:100%;padding:.375rem .625rem;background:#1f2937;border:1px solid #4b5563;border-radius:.5rem;color:#fff;font-size:.8125rem;outline:none;box-sizing:border-box}.jazz-demo-input[data-v-d8349330]:focus{border-color:#3b82f6;box-shadow:0 0 0 2px #3b82f64d}.jazz-demo-input[data-v-d8349330]::-moz-placeholder{color:#6b7280}.jazz-demo-input[data-v-d8349330]::placeholder{color:#6b7280}.jazz-demo-add-btn[data-v-d8349330]{width:100%;padding:.375rem .75rem;background:#2563eb;color:#fff;border:none;border-radius:.5rem;font-weight:500;font-size:.8125rem;cursor:pointer;transition:background-color .2s}.jazz-demo-add-btn[data-v-d8349330]:hover{background:#1d4ed8}.jazz-demo-list[data-v-d8349330]{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:.25rem}.jazz-demo-item[data-v-d8349330]{display:flex;align-items:center;gap:.5rem;padding:.375rem;border-radius:.5rem}.jazz-demo-item[data-v-d8349330]:hover{background:#1f2937}.jazz-demo-item:hover .jazz-demo-delete[data-v-d8349330]{opacity:1}.jazz-demo-drag[data-v-d8349330]{cursor:grab;color:#4b5563;transition:color .2s;-webkit-user-select:none;-moz-user-select:none;user-select:none;display:flex;align-items:center}.jazz-demo-drag[data-v-d8349330]:active{cursor:grabbing}.jazz-demo-item:hover .jazz-demo-drag[data-v-d8349330]{color:#9ca3af}.jazz-demo-svg[data-v-d8349330]{width:1rem;height:1rem}.jazz-demo-checkbox[data-v-d8349330]{width:.875rem;height:.875rem;accent-color:#2563eb}.jazz-demo-text[data-v-d8349330]{flex:1;color:#e5e7eb;font-size:.8125rem}.jazz-demo-text-done[data-v-d8349330]{text-decoration:line-through;color:#6b7280}.jazz-demo-delete[data-v-d8349330]{opacity:0;transition:opacity .2s;color:#6b7280;background:none;border:none;padding:.125rem;cursor:pointer;display:flex;align-items:center}.jazz-demo-delete[data-v-d8349330]:hover{color:#f87171}.jazz-demo-empty[data-v-d8349330]{color:#6b7280;text-align:center;padding:1rem 0;margin:0;font-size:.8125rem}
.jazz-demo-root[data-v-1a336f1a]{background:#030712;border:1px solid #374151;border-radius:.75rem;padding:1rem;font-family:system-ui,-apple-system,sans-serif;color:#e5e7eb;font-size:14px}.jazz-demo-header[data-v-1a336f1a]{display:flex;align-items:center;justify-content:space-between;margin-bottom:1rem}.jazz-demo-title[data-v-1a336f1a]{color:#fff;font-size:1rem;font-weight:600}.jazz-demo-toggles[data-v-1a336f1a]{display:flex;align-items:center;gap:.75rem}.jazz-demo-toggle-wrap[data-v-1a336f1a]{display:flex;align-items:center;gap:.5rem}.jazz-demo-toggle-label[data-v-1a336f1a]{color:#d1d5db;font-size:.75rem}.jazz-demo-toggle[data-v-1a336f1a]{position:relative;display:inline-flex;height:1.25rem;width:2.25rem;align-items:center;border-radius:9999px;transition:background-color .2s;border:none;cursor:pointer;padding:0}.jazz-demo-toggle-on[data-v-1a336f1a]{background:#2563eb}.jazz-demo-toggle-off[data-v-1a336f1a]{background:#4b5563}.jazz-demo-toggle-dot[data-v-1a336f1a]{display:inline-block;height:.875rem;width:.875rem;border-radius:9999px;background:#fff;transition:transform .2s}.jazz-demo-toggle-dot-on[data-v-1a336f1a]{transform:translate(1.125rem)}.jazz-demo-toggle-dot-off[data-v-1a336f1a]{transform:translate(.125rem)}.jazz-demo-covalue-id[data-v-1a336f1a]{display:flex;align-items:center;gap:.375rem;margin-bottom:.5rem;padding:.25rem .5rem;background:#1e1b4b;border:1px solid #3730a3;border-radius:.375rem;overflow:hidden}.jazz-demo-covalue-label[data-v-1a336f1a]{color:#a78bfa;font-size:.625rem;font-weight:600;white-space:nowrap}.jazz-demo-covalue-code[data-v-1a336f1a]{color:#c4b5fd;font-size:.625rem;font-family:ui-monospace,monospace;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.jazz-demo-card[data-v-1a336f1a]{background:#111827;border:1px solid #374151;border-radius:.75rem;padding:1rem}.jazz-demo-loading[data-v-1a336f1a]{color:#9ca3af;text-align:center;padding:2rem 0}.jazz-demo-card[data-v-1a336f1a]{padding:1.5rem}.jazz-counter-display[data-v-1a336f1a]{font-size:3rem;font-weight:700;color:#fff;text-align:center;padding:1rem 0;font-variant-numeric:tabular-nums}.jazz-counter-controls[data-v-1a336f1a]{display:flex;gap:.5rem}.jazz-counter-btn[data-v-1a336f1a]{flex:1;padding:.5rem;font-size:1.25rem;font-weight:600;border:1px solid #374151;border-radius:.5rem;background:#1f2937;color:#e5e7eb;cursor:pointer;transition:background-color .2s}.jazz-counter-btn[data-v-1a336f1a]:hover{background:#374151}.jazz-counter-btn-primary[data-v-1a336f1a]{background:#2563eb;border-color:#2563eb;color:#fff}.jazz-counter-btn-primary[data-v-1a336f1a]:hover{background:#1d4ed8}
.shiki-magic-move-container{position:relative;white-space:pre}.shiki-magic-move-line-number{opacity:.3;-webkit-user-select:none;-moz-user-select:none;user-select:none}.shiki-magic-move-item{display:inline-block;transition:color var(--smm-duration,.5s) var(--smm-easing,"ease")}.shiki-magic-move-enter-active,.shiki-magic-move-leave-active,.shiki-magic-move-move{transition:all var(--smm-duration,.5s) var(--smm-easing,"ease")}.shiki-magic-move-container-resize,.shiki-magic-move-container-restyle{transition:all var(--smm-duration,.5s) var(--smm-easing,"ease");transition-delay:calc(var(--smm-duration, .5s)*var(--smm-delay-container, 1))}.shiki-magic-move-move{transition-delay:calc(var(--smm-duration, .5s)*var(--smm-delay-move, 1) + var(--smm-stagger, 0));z-index:1}.shiki-magic-move-enter-active{transition-delay:calc(var(--smm-duration, .5s)*var(--smm-delay-enter, 1) + var(--smm-stagger, 0));z-index:1}.shiki-magic-move-leave-active{transition-delay:calc(var(--smm-duration, .5s)*var(--smm-delay-leave, 1) + var(--smm-stagger, 0))}.shiki-magic-move-enter-from,.shiki-magic-move-leave-to{opacity:0}br.shiki-magic-move-leave-active{display:none}
</style><style>[data-astro-transition-scope="astro-plk3gbjq-1"] { view-transition-name: why-you-dont-need-the-nuxt-mcp-when-you-use-claude-code; }@layer astro { ::view-transition-old(why-you-dont-need-the-nuxt-mcp-when-you-use-claude-code) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(why-you-dont-need-the-nuxt-mcp-when-you-use-claude-code) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(why-you-dont-need-the-nuxt-mcp-when-you-use-claude-code) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(why-you-dont-need-the-nuxt-mcp-when-you-use-claude-code) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; } }[data-astro-transition-fallback="old"] [data-astro-transition-scope="astro-plk3gbjq-1"],
			[data-astro-transition-fallback="old"][data-astro-transition-scope="astro-plk3gbjq-1"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition-fallback="new"] [data-astro-transition-scope="astro-plk3gbjq-1"],
			[data-astro-transition-fallback="new"][data-astro-transition-scope="astro-plk3gbjq-1"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back][data-astro-transition-fallback="old"] [data-astro-transition-scope="astro-plk3gbjq-1"],
			[data-astro-transition=back][data-astro-transition-fallback="old"][data-astro-transition-scope="astro-plk3gbjq-1"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back][data-astro-transition-fallback="new"] [data-astro-transition-scope="astro-plk3gbjq-1"],
			[data-astro-transition=back][data-astro-transition-fallback="new"][data-astro-transition-scope="astro-plk3gbjq-1"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }</style><style>.alert:where(.astro-7kdbuayl){margin-top:1.5rem;margin-bottom:1.5rem;border-radius:.5rem;border-left-width:4px;background-color:rgba(var(--color-card),var(--tw-bg-opacity, 1));--tw-bg-opacity: .5;padding:1rem}.alert-title:where(.astro-7kdbuayl){margin-bottom:.5rem;display:flex;align-items:center;gap:.5rem;font-weight:700;--tw-text-opacity: 1;color:rgba(var(--color-accent),var(--tw-text-opacity, 1))}.alert-icon:where(.astro-7kdbuayl){font-size:1.25rem;line-height:1.75rem}.alert-content:where(.astro-7kdbuayl){--tw-text-opacity: 1;color:rgba(var(--color-text-base),var(--tw-text-opacity, 1))}.alert-content:where(.astro-7kdbuayl) :where(.astro-7kdbuayl):is(:where(p):not(:where([class~=not-prose],[class~=not-prose] *))){margin-top:0}.alert-note:where(.astro-7kdbuayl){border-color:rgba(var(--color-accent),var(--tw-border-opacity, 1));--tw-border-opacity: .6 }.alert-tip:where(.astro-7kdbuayl){border-color:rgba(var(--color-accent),var(--tw-border-opacity, 1));--tw-border-opacity: .7 }.alert-important:where(.astro-7kdbuayl){border-color:rgba(var(--color-accent),var(--tw-border-opacity, 1));--tw-border-opacity: 1 }.alert-warning:where(.astro-7kdbuayl){border-color:rgba(var(--color-accent),var(--tw-border-opacity, 1));--tw-border-opacity: .8 }.alert-caution:where(.astro-7kdbuayl){border-color:rgba(var(--color-accent),var(--tw-border-opacity, 1));--tw-border-opacity: .9 }.alert-definition:where(.astro-7kdbuayl){border-color:rgba(var(--color-accent),var(--tw-border-opacity, 1));--tw-border-opacity: .5 }.alert-github:where(.astro-7kdbuayl){border-color:rgba(var(--color-accent),var(--tw-border-opacity, 1));--tw-border-opacity: .75 }
</style><style>.collapsible:where(.astro-kncz7yy6){display:block!important;width:100%!important;max-width:100%!important;margin:1.5rem 0;border:1px solid rgb(var(--color-border));border-radius:.5rem;overflow:hidden}.collapsible-summary:where(.astro-kncz7yy6){display:flex;align-items:center;gap:.5rem;padding:.75rem 1rem;font-weight:500;cursor:pointer;background:rgb(var(--color-card));-webkit-user-select:none;-moz-user-select:none;user-select:none;list-style:none}.collapsible-summary:where(.astro-kncz7yy6)::-webkit-details-marker{display:none}.collapsible-summary:where(.astro-kncz7yy6):hover{background:rgb(var(--color-card-muted))}.collapsible-icon:where(.astro-kncz7yy6){display:flex;align-items:center;transition:transform .2s ease}.collapsible:where(.astro-kncz7yy6)[open] .collapsible-icon:where(.astro-kncz7yy6){transform:rotate(90deg)}.collapsible-content:where(.astro-kncz7yy6){width:100%!important;max-width:100%!important}.collapsible-content:where(.astro-kncz7yy6) pre{margin:0!important;border-radius:0!important;width:100%!important;max-width:100%!important}.collapsible-content:where(.astro-kncz7yy6)>*:first-child{margin-top:0}.collapsible-content:where(.astro-kncz7yy6)>*:last-child{margin-bottom:0}
</style><style>.prose details.collapsible{display:block!important;width:100%!important;max-width:100%!important}
</style><style>.file-tree__item:where(.astro-o25vlg2d){margin:0;padding:0;position:relative}.file-tree__item:where(.astro-o25vlg2d):before{content:"";position:absolute;left:calc(.5rem + (var(--level) * 1.25rem));top:0;bottom:0;width:1px;background:rgba(var(--color-text-base),.15)}.file-tree__item:where(.astro-o25vlg2d):last-child:before{bottom:50%}.file-tree__item:where(.astro-o25vlg2d):after{content:"";position:absolute;left:calc(.5rem + (var(--level) * 1.25rem));top:50%;width:.75rem;height:1px;background:rgba(var(--color-text-base),.15)}.file-tree__folder:where(.astro-o25vlg2d){margin:0;padding:0}.file-tree__folder:where(.astro-o25vlg2d)>summary:where(.astro-o25vlg2d){list-style:none;cursor:pointer;display:flex;gap:.5rem;align-items:center;padding:.2rem .5rem .2rem calc(1.5rem + (var(--level) * 1.25rem));border-radius:.25rem;transition:background-color .15s ease;line-height:1.6;position:relative}.file-tree__folder:where(.astro-o25vlg2d)>summary:where(.astro-o25vlg2d):hover{background:rgba(var(--color-text-base),.05)}.file-tree__folder:where(.astro-o25vlg2d)[open]>summary:where(.astro-o25vlg2d) .file-tree__caret:where(.astro-o25vlg2d){transform:rotate(90deg)}.file-tree__folder:where(.astro-o25vlg2d):not([open])>summary:where(.astro-o25vlg2d) .file-tree__caret:where(.astro-o25vlg2d){transform:rotate(0)}.file-tree__folder:where(.astro-o25vlg2d)>summary:where(.astro-o25vlg2d)::-webkit-details-marker{display:none}.file-tree__list:where(.astro-o25vlg2d){list-style:none;margin:0;padding:0}.file-tree__file:where(.astro-o25vlg2d){display:flex;gap:.5rem;align-items:center;padding:.2rem .5rem .2rem calc(1.5rem + (var(--level) * 1.25rem));border-radius:.25rem;text-decoration:none;color:inherit;transition:background-color .15s ease;line-height:1.6;position:relative}.file-tree__file:where(.astro-o25vlg2d):hover{background:rgba(var(--color-text-base),.05)}a:where(.astro-o25vlg2d).file-tree__file:hover .file-tree__name:where(.astro-o25vlg2d){color:rgb(var(--color-accent))}.file-tree__icon:where(.astro-o25vlg2d){width:1rem;height:1rem;flex-shrink:0;color:rgba(var(--color-text-base),.4);display:inline-flex;align-items:center;justify-content:center}.file-tree__icon--file:where(.astro-o25vlg2d){color:rgba(var(--color-text-base),.4)}.file-tree__icon--colored:where(.astro-o25vlg2d){color:inherit}.file-tree__icon--text:where(.astro-o25vlg2d){font-weight:600;font-size:.875rem;display:inline-flex;align-items:center;justify-content:center;width:1rem;height:1rem}.file-tree__name:where(.astro-o25vlg2d){white-space:nowrap;transition:color .15s ease;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,Liberation Mono,Courier New,monospace}.file-tree__comment:where(.astro-o25vlg2d){color:rgba(var(--color-text-base),.5);font-style:italic;margin-left:.5rem;white-space:nowrap;font-size:.9em}.file-tree__caret:where(.astro-o25vlg2d){width:.75rem;height:.75rem;transition:transform .2s ease;flex-shrink:0;color:rgba(var(--color-text-base),.5);font-size:.625rem;display:inline-flex;align-items:center;justify-content:center;transform-origin:center}
</style><style>.file-tree:where(.astro-htwbjus4){font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,Liberation Mono,Courier New,monospace;font-size:.8125rem;background:rgb(var(--color-card));color:rgb(var(--color-text-base));border:1px solid rgba(var(--color-border),.5);border-radius:.5rem;padding:.75rem;margin:1.5rem 0;overflow-x:auto}.file-tree__list:where(.astro-htwbjus4){list-style:none;margin:0;padding:0}.file-tree__list:where(.astro-htwbjus4)>li:where(.astro-htwbjus4):first-child:before,.file-tree__list:where(.astro-htwbjus4)>li:where(.astro-htwbjus4):first-child:after{display:none}.file-tree:where(.astro-htwbjus4)::-webkit-scrollbar{height:.5rem}.file-tree:where(.astro-htwbjus4)::-webkit-scrollbar-track{background:rgb(var(--color-fill))}.file-tree:where(.astro-htwbjus4)::-webkit-scrollbar-thumb{background:rgb(var(--color-border));border-radius:.25rem}.file-tree:where(.astro-htwbjus4)::-webkit-scrollbar-thumb:hover{background:rgb(var(--color-card-muted))}
</style><style>.internal-link-wrapper:where(.astro-3tyn5ojg){position:relative;display:inline-block}.internal-link:where(.astro-3tyn5ojg){--tw-text-opacity: 1;color:rgba(var(--color-accent),var(--tw-text-opacity, 1));text-decoration-line:underline;text-decoration-style:dashed;text-decoration-thickness:1px;text-underline-offset:4px;transition-property:all;transition-timing-function:cubic-bezier(.4,0,.2,1);transition-duration:.15s}.internal-link:where(.astro-3tyn5ojg):hover{text-decoration-style:solid}.internal-link:where(.astro-3tyn5ojg){cursor:pointer;display:inline}.preview-card:where(.astro-3tyn5ojg){display:block;position:absolute;bottom:calc(100% + 8px);left:50%;transform:translate(-50%);z-index:9999;width:320px;max-width:90vw;border-radius:.5rem;border-width:1px;--tw-border-opacity: 1;border-color:rgba(var(--color-border),var(--tw-border-opacity, 1));--tw-bg-opacity: 1;background-color:rgba(var(--color-card),var(--tw-bg-opacity, 1));--tw-shadow: 0 10px 15px -3px rgb(0 0 0 / .1), 0 4px 6px -4px rgb(0 0 0 / .1);--tw-shadow-colored: 0 10px 15px -3px var(--tw-shadow-color), 0 4px 6px -4px var(--tw-shadow-color);box-shadow:var(--tw-ring-offset-shadow, 0 0 #0000),var(--tw-ring-shadow, 0 0 #0000),var(--tw-shadow);opacity:0;visibility:hidden;transition:opacity .2s ease-in-out,visibility .2s ease-in-out}.preview-card:where(.astro-3tyn5ojg).is-fixed{position:fixed!important;bottom:auto!important;top:var(--pc-top, 0px)!important;left:var(--pc-left, 0px)!important;transform:none!important}.preview-content:where(.astro-3tyn5ojg){display:block;padding:1rem}.preview-title:where(.astro-3tyn5ojg){display:block;margin-bottom:.5rem;font-size:1rem;line-height:1.5rem;font-weight:600;--tw-text-opacity: 1;color:rgba(var(--color-text-base),var(--tw-text-opacity, 1));line-height:1.3}.preview-title:where(.astro-3tyn5ojg) .heading-link:where(.astro-3tyn5ojg){display:none!important}.preview-description:where(.astro-3tyn5ojg){display:block;margin-bottom:.75rem;font-size:.875rem;line-height:1.25rem;color:rgba(var(--color-text-base),.8);line-height:1.4;overflow:hidden;text-overflow:ellipsis;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical}.preview-tags:where(.astro-3tyn5ojg){margin-bottom:.5rem;display:flex;flex-wrap:wrap;gap:.375rem}.preview-tag:where(.astro-3tyn5ojg){border-radius:.25rem;padding:.125rem .5rem;font-size:.75rem;line-height:1rem;background-color:rgba(var(--color-accent),.1);--tw-text-opacity: 1;color:rgba(var(--color-accent),var(--tw-text-opacity, 1));font-weight:500}.preview-tag-more:where(.astro-3tyn5ojg){border-radius:.25rem;padding:.125rem .5rem;font-size:.75rem;line-height:1rem;--tw-bg-opacity: 1;background-color:rgba(var(--color-fill),var(--tw-bg-opacity, 1));color:rgba(var(--color-text-base),.6);font-weight:500}.preview-date:where(.astro-3tyn5ojg){font-size:.75rem;line-height:1rem;color:rgba(var(--color-text-base),.6);display:block;margin-top:8px;font-style:italic}.preview-card:where(.astro-3tyn5ojg):after{content:"";position:absolute;top:100%;left:50%;transform:translate(-50%);border:6px solid transparent;border-top-color:var(--color-card)}.preview-card:where(.astro-3tyn5ojg).is-fixed:after{display:none}
</style><style>[data-astro-transition-scope="astro-36ssibgs-2"] { view-transition-name: ai; }@layer astro { ::view-transition-old(ai) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(ai) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(ai) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(ai) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; } }[data-astro-transition-fallback="old"] [data-astro-transition-scope="astro-36ssibgs-2"],
			[data-astro-transition-fallback="old"][data-astro-transition-scope="astro-36ssibgs-2"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition-fallback="new"] [data-astro-transition-scope="astro-36ssibgs-2"],
			[data-astro-transition-fallback="new"][data-astro-transition-scope="astro-36ssibgs-2"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back][data-astro-transition-fallback="old"] [data-astro-transition-scope="astro-36ssibgs-2"],
			[data-astro-transition=back][data-astro-transition-fallback="old"][data-astro-transition-scope="astro-36ssibgs-2"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back][data-astro-transition-fallback="new"] [data-astro-transition-scope="astro-36ssibgs-2"],
			[data-astro-transition=back][data-astro-transition-fallback="new"][data-astro-transition-scope="astro-36ssibgs-2"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-3"] { view-transition-name: claude-code; }@layer astro { ::view-transition-old(claude-code) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(claude-code) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(claude-code) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(claude-code) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; } }[data-astro-transition-fallback="old"] [data-astro-transition-scope="astro-36ssibgs-3"],
			[data-astro-transition-fallback="old"][data-astro-transition-scope="astro-36ssibgs-3"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition-fallback="new"] [data-astro-transition-scope="astro-36ssibgs-3"],
			[data-astro-transition-fallback="new"][data-astro-transition-scope="astro-36ssibgs-3"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back][data-astro-transition-fallback="old"] [data-astro-transition-scope="astro-36ssibgs-3"],
			[data-astro-transition=back][data-astro-transition-fallback="old"][data-astro-transition-scope="astro-36ssibgs-3"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back][data-astro-transition-fallback="new"] [data-astro-transition-scope="astro-36ssibgs-3"],
			[data-astro-transition=back][data-astro-transition-fallback="new"][data-astro-transition-scope="astro-36ssibgs-3"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-4"] { view-transition-name: nuxt; }@layer astro { ::view-transition-old(nuxt) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(nuxt) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(nuxt) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(nuxt) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; } }[data-astro-transition-fallback="old"] [data-astro-transition-scope="astro-36ssibgs-4"],
			[data-astro-transition-fallback="old"][data-astro-transition-scope="astro-36ssibgs-4"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition-fallback="new"] [data-astro-transition-scope="astro-36ssibgs-4"],
			[data-astro-transition-fallback="new"][data-astro-transition-scope="astro-36ssibgs-4"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back][data-astro-transition-fallback="old"] [data-astro-transition-scope="astro-36ssibgs-4"],
			[data-astro-transition=back][data-astro-transition-fallback="old"][data-astro-transition-scope="astro-36ssibgs-4"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back][data-astro-transition-fallback="new"] [data-astro-transition-scope="astro-36ssibgs-4"],
			[data-astro-transition=back][data-astro-transition-fallback="new"][data-astro-transition-scope="astro-36ssibgs-4"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-5"] { view-transition-name: tooling; }@layer astro { ::view-transition-old(tooling) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(tooling) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(tooling) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(tooling) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; } }[data-astro-transition-fallback="old"] [data-astro-transition-scope="astro-36ssibgs-5"],
			[data-astro-transition-fallback="old"][data-astro-transition-scope="astro-36ssibgs-5"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition-fallback="new"] [data-astro-transition-scope="astro-36ssibgs-5"],
			[data-astro-transition-fallback="new"][data-astro-transition-scope="astro-36ssibgs-5"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back][data-astro-transition-fallback="old"] [data-astro-transition-scope="astro-36ssibgs-5"],
			[data-astro-transition=back][data-astro-transition-fallback="old"][data-astro-transition-scope="astro-36ssibgs-5"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back][data-astro-transition-fallback="new"] [data-astro-transition-scope="astro-36ssibgs-5"],
			[data-astro-transition=back][data-astro-transition-fallback="new"][data-astro-transition-scope="astro-36ssibgs-5"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }</style></head> <body class="astro-sckkx6r4"> <div class="conference-wrapper border-b border-skin-line bg-skin-fill px-4 py-3 text-center text-skin-base astro-z2v4rtzb"><div class="mx-auto flex max-w-3xl flex-col items-center justify-center gap-3 sm:flex-row sm:gap-4 astro-z2v4rtzb"><div class="text-center sm:text-left astro-z2v4rtzb"><p class="text-lg font-semibold astro-z2v4rtzb"><span class="pulse-dot astro-z2v4rtzb"></span>
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/prompts/" class=" astro-3ef6ksr2">
🤖 Prompts
</a> </li> <li class="astro-3ef6ksr2"> <a href="/tags/" class=" astro-3ef6ksr2">
🏷️ Tags
</a> </li> <li class="astro-3ef6ksr2"> <a href="/about/" class=" astro-3ef6ksr2">
👤 About
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <div class="mx-auto flex w-full max-w-5xl justify-start px-2 astro-vj4tpspi"> <button class="focus-outline mb-2 mt-8 flex hover:opacity-75 astro-vj4tpspi" onclick="(() => (history.length === 1) ? window.location = '/' : history.back())()"> <svg xmlns="http://www.w3.org/2000/svg" class="astro-vj4tpspi"><path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg><span class="astro-vj4tpspi">Go back</span> </button> </div> <main data-pagefind-body id="main-content" class="relative astro-vj4tpspi"> <h1 class="post-title astro-vj4tpspi" data-astro-transition-scope="astro-plk3gbjq-1">Why You Don&#39;t Need the Nuxt MCP When You Use Claude Code</h1> <div class="my-2 flex items-center justify-between astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-100 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-base"><time dateTime="2025-12-31T00:00:00.000Z">Dec 31, 2025</time><span class="sr-only"> at </span></span></div> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="10OTDk" prefix="r3" component-url="/_astro/PostCopyButton.-PGtk4At.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;title&quot;:[0,&quot;Why You Don&#39;t Need the Nuxt MCP When You Use Claude Code&quot;],&quot;content&quot;:[0,&quot;import Alert from \&quot;@features/mdx-components/components/Alert.astro\&quot;;\nimport InternalLink from \&quot;@features/mdx-components/components/InternalLink.astro\&quot;;\nimport FileTree from \&quot;@features/filetree/components/FileTree.astro\&quot;;\nimport Figure from \&quot;@features/mdx-components/components/Figure.astro\&quot;;\nimport Collapsible from \&quot;@features/mdx-components/components/Collapsible.astro\&quot;;\nimport agentInAction from \&quot;@assets/images/claude/hooksexplained.png\&quot;;\n\nI think we all love Nuxt. One problem with using Nuxt for AI is that training data is not up to date. This is especially true for Nuxt Content where often times LLMs still think they&#39;re working with Nuxt 2. This is why the Nuxt team created their MCP server.\n\nI think the MCP is good and perfectly fine. But for me—and also for Anthropic itself—MCPs in the current spec have the problem of context bloat. Anthropic has [written down this problem perfectly](https://www.anthropic.com/engineering/code-execution-with-mcp) in their engineering blog.\n\n&lt;Alert type=\&quot;note\&quot; title=\&quot;The Context Bloat Problem\&quot;&gt;\nAnthropic identifies two main issues: **tool definition overload** (loading all tools upfront creates hundreds of thousands of tokens before the model even reads your request) and **intermediate result redundancy** (every result must pass through the model, sometimes processing 50,000+ tokens per operation).\n&lt;/Alert&gt;\n\nIf you want to dive deeper into what MCP is and how it works, check out my post on &lt;InternalLink slug=\&quot;what-is-model-context-protocol-mcp\&quot;&gt;What Is the Model Context Protocol (MCP)?&lt;/InternalLink&gt;.\n\n## Why I Use Custom Research Agents Instead\n\nThis is why for all my projects I don&#39;t use MCP but I use custom research agents.\n\nAll websites nowadays use `llms.txt`. Now if you let an LLM fetch `llms.txt` first, it can perfectly find every information needed from the docs itself.\n\nI&#39;ve written about &lt;InternalLink slug=\&quot;how-i-added-llms-txt-to-my-astro-blog\&quot;&gt;how I added llms.txt to my own blog&lt;/InternalLink&gt;—it&#39;s becoming a standard way for sites to expose their content to AI.\n\nThis approach has several advantages:\n\n1. **Only the description gets loaded as context** — The agent description is minimal, not the entire tool schema\n2. **You can customize it** — Full control over what the agent knows and how it behaves\n3. **It runs in its own context** — Your main agent could use the research agent only to gather information and then continue with its work without polluting its context window\n\nThis is essentially the same pattern I described in my post about &lt;InternalLink slug=\&quot;claude-code-customization-guide-claudemd-skills-subagents\&quot;&gt;Claude Code subagents&lt;/InternalLink&gt; — agents keep your main context clean by delegating specialized tasks.\n\n&lt;Alert type=\&quot;tip\&quot; title=\&quot;Claude Code Uses This Pattern Too\&quot;&gt;\nClaude Code itself uses this exact approach. When you ask it questions about its own features, it spawns a [`claude-code-guide` agent](https://github.com/Piebald-AI/claude-code-system-prompts/blob/main/system-prompts/agent-prompt-claude-guide-agent.md) that fetches from a documentation sitemap and answers based on current docs—not training data. We&#39;re just applying the same pattern to other libraries.\n&lt;/Alert&gt;\n\n## Example: Nuxt Content Specialist Agent\n\nHere&#39;s how my Nuxt Content agent looks. Just put it under `.claude/agents`:\n\n&lt;FileTree tree={[\n  { name: \&quot;.claude\&quot;, open: true, children: [\n    { name: \&quot;agents\&quot;, open: true, children: [\n      { name: \&quot;nuxt-content-specialist.md\&quot;, comment: \&quot;// Your custom agent\&quot; }\n    ]}\n  ]}\n]} /&gt;\n\n&lt;Collapsible title=\&quot;Full agent definition\&quot;&gt;\n````markdown\n---\nname: nuxt-content-specialist\ndescription: Use this agent when the task involves @nuxt/content v3 in any way - implementing, modifying, querying, reviewing, or improving content management code. This includes creating or modifying content collections, writing queries, implementing MDC components, configuring content sources, troubleshooting content-related issues, or reviewing existing content code for improvements and best practices.\\n\\nExamples:\\n\\n&lt;example&gt;\\nContext: User asks about improving their Nuxt Content implementation.\\nuser: \&quot;What can I improve on this codebase when it comes to Nuxt Content?\&quot;\\nassistant: \&quot;I&#39;ll use the nuxt-content-specialist agent to review your content implementation against current best practices.\&quot;\\n&lt;commentary&gt;\\nSince the user is asking about Nuxt Content improvements, use the nuxt-content-specialist agent to fetch the latest documentation and review the existing code for optimization opportunities, missing features, and best practice violations.\\n&lt;/commentary&gt;\\n&lt;/example&gt;\\n\\n&lt;example&gt;\\nContext: User needs to add a new content collection.\\nuser: \&quot;I need to add a &#39;blog&#39; collection separate from pages\&quot;\\nassistant: \&quot;I&#39;ll use the nuxt-content-specialist agent to implement this correctly.\&quot;\\n&lt;commentary&gt;\\nSince the user needs to modify the content collection schema, use the nuxt-content-specialist agent to first fetch the latest Nuxt Content documentation and then implement the collection following best practices.\\n&lt;/commentary&gt;\\n&lt;/example&gt;\\n\\n&lt;example&gt;\\nContext: User is asking about content query patterns.\\nuser: \&quot;How do I query content by multiple tags in Nuxt Content?\&quot;\\nassistant: \&quot;Let me use the nuxt-content-specialist agent to provide an accurate answer based on the current documentation.\&quot;\\n&lt;commentary&gt;\\nSince the user is asking about Nuxt Content query capabilities, use the nuxt-content-specialist agent to fetch documentation and provide an accurate, up-to-date response about queryCollection filtering.\\n&lt;/commentary&gt;\\n&lt;/example&gt;\\n\\n&lt;example&gt;\\nContext: User wants to embed Vue components in Markdown.\\nuser: \&quot;How do I use a custom component inside my markdown files?\&quot;\\nassistant: \&quot;I&#39;ll consult the nuxt-content-specialist agent to explain MDC syntax correctly.\&quot;\\n&lt;commentary&gt;\\nSince this involves MDC (Markdown Components) syntax, use the nuxt-content-specialist agent to fetch relevant documentation about component usage in Markdown files.\\n&lt;/commentary&gt;\\n&lt;/example&gt;\\n\\n&lt;example&gt;\\nContext: User needs to implement content search.\\nuser: \&quot;I want to add full-text search to my content site\&quot;\\nassistant: \&quot;I&#39;ll use the nuxt-content-specialist agent to implement search with queryCollectionSearchSections.\&quot;\\n&lt;commentary&gt;\\nSince search requires specific Nuxt Content APIs, use the nuxt-content-specialist agent to fetch the latest documentation on search implementation patterns.\\n&lt;/commentary&gt;\\n&lt;/example&gt;\nmodel: opus\ncolor: green\n---\n\n# Nuxt Content Specialist Agent\n\nThis document defines the Nuxt Content specialist agent&#39;s role and responsibilities for helping users with @nuxt/content v3 implementations.\n\n## Primary Domain\n\n**@nuxt/content v3**: Content management system for Nuxt applications providing file-based content with Markdown support, MDC syntax for embedding Vue components, SQLite-based querying, and full-text search capabilities.\n\n### Core Expertise Areas\n\n1. **Collections**: Defining collections in `content.config.ts`, schema validation with Zod, collection types (page, data), import sources\n2. **Content Files**: Markdown, YAML, JSON, CSV support and their appropriate use cases\n3. **MDC Syntax**: Embedding Vue components in Markdown, props, slots, block vs inline components\n4. **Querying**: `queryCollection()`, `queryCollectionNavigation()`, `queryCollectionItemSurroundings()`, `queryCollectionSearchSections()`\n5. **Rendering**: `&lt;ContentRenderer&gt;`, `&lt;Slot&gt;`, prose components, custom renderers\n6. **Search**: Full-text search implementation, search sections, indexing strategies\n7. **Sources**: Custom data sources, remote content, transformers\n8. **Deployment**: Static generation, server rendering, edge deployment considerations\n\n## Documentation Sources\n\nThe agent leverages one primary documentation resource:\n\n- **Nuxt Content docs** (`https://content.nuxt.com/llms.txt`): Covers collection definitions, querying APIs, MDC syntax, content rendering, search implementation, custom sources, and deployment patterns\n\n### Key Documentation Sections\n\n| Section | URL Path | Purpose |\n|---------|----------|---------|\n| Collections | `/docs/collections` | Collection definitions and configuration |\n| Querying | `/docs/querying` | Query composables and filtering |\n| ContentRenderer | `/docs/components/content-renderer` | Rendering content |\n| Markdown/MDC | `/docs/files/markdown` | Markdown and MDC syntax |\n| Search | `/docs/recipes/search` | Search implementation |\n| Sources | `/docs/advanced/sources` | Custom content sources |\n\n## Operational Approach\n\nThe agent follows a structured methodology:\n\n1. **Fetch documentation index** from `https://content.nuxt.com/llms.txt` to understand available documentation structure\n2. **Categorize user inquiry** into appropriate domain (collections, querying, MDC, search, etc.)\n3. **Identify specific documentation URLs** from the index relevant to the task\n4. **Fetch targeted documentation pages** for accurate, up-to-date information\n5. **Review project context** by reading relevant local files (`content.config.ts`, existing content files)\n6. **Provide actionable guidance** with TypeScript code examples following project conventions\n7. **Reference documentation sources** to support recommendations\n\n## Core Guidelines\n\n- Prioritize official documentation over training knowledge (v3 has significant v2 differences)\n- Maintain concise, actionable responses\n- Include TypeScript code examples following project conventions\n- Reference specific documentation URLs consulted\n- Avoid emojis\n- Always verify API specifics against fetched documentation before providing guidance\n- Note v2 to v3 migration considerations when relevant\n- Consider static vs server rendering implications\n- Handle content not found scenarios gracefully in implementations\n\n## Project Context\n\nThis agent operates within a Nuxt 4 application using:\n\n- **@nuxt/content v3** with SQLite-based querying\n- **@nuxt/ui v3** for UI components\n- **TypeScript** for type safety\n- **File-based routing** with catch-all content routes in `app/` directory\n\n### Established Patterns\n\n```typescript\n// content.config.ts - Collection definition pattern\nimport { defineCollection, z } from &#39;@nuxt/content&#39;\n\nexport const collections = {\n  content: defineCollection({\n    type: &#39;page&#39;,\n    source: &#39;**/*.md&#39;\n  })\n}\n```\n\n```vue\n&lt;!-- Catch-all route pattern: app/pages/[...slug].vue --&gt;\n&lt;script setup lang=\&quot;ts\&quot;&gt;\nconst route = useRoute()\nconst { data: page } = await useAsyncData(\n  route.path,\n  () =&gt; queryCollection(&#39;content&#39;).path(route.path).first()\n)\n&lt;/script&gt;\n\n&lt;template&gt;\n  &lt;ContentRenderer v-if=\&quot;page\&quot; :value=\&quot;page\&quot; /&gt;\n  &lt;div v-else&gt;Page not found&lt;/div&gt;\n&lt;/template&gt;\n```\n\n## Quality Assurance\n\n- Always verify suggestions against fetched documentation\n- If documentation is unclear or unavailable, explicitly state this with appropriate caveats\n- When multiple approaches exist, explain trade-offs\n- Be aware of build-time vs runtime content access differences\n- Ensure proper typing for collection queries and responses\n````\n&lt;/Collapsible&gt;\n\n## Key Design Principles\n\nThe agent follows these principles:\n\n1. **Documentation-first**: Always fetch `llms.txt` before answering anything\n2. **Specific expertise**: Focused on Nuxt Content v3, not general Nuxt knowledge\n3. **Verification**: Cross-reference documentation, don&#39;t rely on training data\n4. **Practical output**: TypeScript code following project conventions\n\n## How It Works in Practice\n\nWhen you ask Claude Code something like \&quot;How do hooks work in Nuxt Content?\&quot;, the main agent recognizes this matches the `nuxt-content-specialist` description and delegates to it.\n\n&lt;Figure\n  src={agentInAction}\n  alt=\&quot;Claude Code spawning the nuxt-content-specialist agent to research Nuxt Content hooks\&quot;\n  caption=\&quot;The agent researches in its own context while your main context stays clean\&quot;\n  width={800}\n/&gt;\n\nThe specialist agent then:\n1. Fetches `https://content.nuxt.com/llms.txt`\n2. Identifies the relevant documentation pages\n3. Fetches the actual docs\n4. Provides an accurate, up-to-date answer\n\nYour main context stays clean. The research happens in a separate context window.\n\n## Create Your Own\n\nYou can apply this pattern to any library or framework:\n\n1. Find if they have `llms.txt` (most modern docs sites do)\n2. Create an agent that fetches it first\n3. Define the expertise scope in the description\n4. Add examples so Claude Code knows when to delegate\n\nThis approach gives you 98%+ reduction in token usage compared to loading full MCP tool definitions, while maintaining access to current documentation.&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PostCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus-outline inline-flex items-center gap-1.5 rounded-md border border-skin-line bg-skin-card px-2.5 py-1.5 text-xs font-medium text-skin-base opacity-80 transition-all hover:border-skin-accent/50 hover:text-skin-accent hover:opacity-100" aria-label="Copy post as markdown" title="Copy post as markdown for AI/LLM"><svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg><span>Copy Post</span></button><!--astro:end--></astro-island> </div>  <article id="article" class="prose mx-auto mt-8 max-w-5xl astro-vj4tpspi"> <p>I think we all love Nuxt. One problem with using Nuxt for AI is that training data is not up to date. This is especially true for Nuxt Content where often times LLMs still think they’re working with Nuxt 2. This is why the Nuxt team created their MCP server.</p>
<p>I think the MCP is good and perfectly fine. But for me—and also for Anthropic itself—MCPs in the current spec have the problem of context bloat. Anthropic has <a href="https://www.anthropic.com/engineering/code-execution-with-mcp" rel="noopener noreferrer" target="_blank">written down this problem perfectly</a> in their engineering blog.</p>
<div class="alert alert-note astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">💡</span> The Context Bloat Problem </p> <div class="alert-content astro-7kdbuayl"> <p>Anthropic identifies two main issues: <strong>tool definition overload</strong> (loading all tools upfront creates hundreds of thousands of tokens before the model even reads your request) and <strong>intermediate result redundancy</strong> (every result must pass through the model, sometimes processing 50,000+ tokens per operation).</p> </div> </div> 
<p>If you want to dive deeper into what MCP is and how it works, check out my post on <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/what-is-model-context-protocol-mcp/" class="internal-link astro-3tyn5ojg"> What Is the Model Context Protocol (MCP)? </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">What Is the Model Context Protocol (MCP)? How It Works</span> <span class="preview-description astro-3tyn5ojg">Learn how MCP (Model Context Protocol) standardizes AI tool integration, enabling LLMs to interact with external services, databases, and APIs through a universal protocol similar to USB-C for AI applications.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">mcp</span><span class="preview-tag astro-3tyn5ojg">typescript</span><span class="preview-tag astro-3tyn5ojg">ai</span>  </span> <time class="preview-date astro-3tyn5ojg">Aug 10, 2025</time> </span> </span> </span>  <script>
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
</script>.</p>
<h2 id="why-i-use-custom-research-agents-instead">Why I Use Custom Research Agents Instead<a class="heading-link" aria-label="Link to section" href="#why-i-use-custom-research-agents-instead"><span class="heading-link-icon">#</span></a></h2>
<p>This is why for all my projects I don’t use MCP but I use custom research agents.</p>
<p>All websites nowadays use <code>llms.txt</code>. Now if you let an LLM fetch <code>llms.txt</code> first, it can perfectly find every information needed from the docs itself.</p>
<p>I’ve written about <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/how-i-added-llms-txt-to-my-astro-blog/" class="internal-link astro-3tyn5ojg"> how I added llms.txt to my own blog </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">How I Added llms.txt to My Astro Blog</span> <span class="preview-description astro-3tyn5ojg">I built a simple way to load my blog content into any LLM with one click. This post shows how you can do it too.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">astro</span><span class="preview-tag astro-3tyn5ojg">ai</span>  </span> <time class="preview-date astro-3tyn5ojg">Mar 3, 2025</time> </span> </span> </span>  <script>
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
</script>—it’s becoming a standard way for sites to expose their content to AI.</p>
<p>This approach has several advantages:</p>
<ol>
<li><strong>Only the description gets loaded as context</strong> — The agent description is minimal, not the entire tool schema</li>
<li><strong>You can customize it</strong> — Full control over what the agent knows and how it behaves</li>
<li><strong>It runs in its own context</strong> — Your main agent could use the research agent only to gather information and then continue with its work without polluting its context window</li>
</ol>
<p>This is essentially the same pattern I described in my post about <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/claude-code-customization-guide-claudemd-skills-subagents/" class="internal-link astro-3tyn5ojg"> Claude Code subagents </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Claude Code Customization: CLAUDE.md, Slash Commands, Skills, and Subagents</span> <span class="preview-description astro-3tyn5ojg">The complete guide to customizing Claude Code. Compare CLAUDE.md, slash commands, skills, and subagents with practical examples showing when to use each.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">claude-code</span><span class="preview-tag astro-3tyn5ojg">ai</span><span class="preview-tag astro-3tyn5ojg">tooling</span> <span class="preview-tag-more astro-3tyn5ojg">+1</span> </span> <time class="preview-date astro-3tyn5ojg">Dec 21, 2025</time> </span> </span> </span>  <script>
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
</script> — agents keep your main context clean by delegating specialized tasks.</p>
<div class="alert alert-tip astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">💪</span> Claude Code Uses This Pattern Too </p> <div class="alert-content astro-7kdbuayl"> <p>Claude Code itself uses this exact approach. When you ask it questions about its own features, it spawns a <a href="https://github.com/Piebald-AI/claude-code-system-prompts/blob/main/system-prompts/agent-prompt-claude-guide-agent.md" rel="noopener noreferrer" target="_blank"><code>claude-code-guide</code> agent</a> that fetches from a documentation sitemap and answers based on current docs—not training data. We’re just applying the same pattern to other libraries.</p> </div> </div> 
<h2 id="example-nuxt-content-specialist-agent">Example: Nuxt Content Specialist Agent<a class="heading-link" aria-label="Link to section" href="#example-nuxt-content-specialist-agent"><span class="heading-link-icon">#</span></a></h2>
<p>Here’s how my Nuxt Content agent looks. Just put it under <code>.claude/agents</code>:</p>
<nav class="file-tree astro-htwbjus4" aria-label="File tree"> <ul class="file-tree__list astro-htwbjus4"> <li class="file-tree__item astro-o25vlg2d" style="--level: 0;"> <details class="file-tree__folder astro-o25vlg2d" open> <summary class="astro-o25vlg2d"> <span class="file-tree__caret astro-o25vlg2d" aria-hidden="true">
▸
</span> <svg class="file-tree__icon astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">.claude</span>  </summary> <ul class="file-tree__list astro-o25vlg2d"> <li class="file-tree__item astro-o25vlg2d" style="--level: 1;"> <details class="file-tree__folder astro-o25vlg2d" open> <summary class="astro-o25vlg2d"> <span class="file-tree__caret astro-o25vlg2d" aria-hidden="true">
▸
</span> <svg class="file-tree__icon astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">agents</span>  </summary> <ul class="file-tree__list astro-o25vlg2d"> <li class="file-tree__item astro-o25vlg2d" style="--level: 2;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#519ABA" d="M22.27 19.385H1.73A1.73 1.73 0 010 17.655V6.345a1.73 1.73 0 011.73-1.73h20.54A1.73 1.73 0 0124 6.345v11.308a1.73 1.73 0 01-1.73 1.731zM5.769 15.923v-4.5l2.308 2.885 2.307-2.885v4.5h2.308V8.078h-2.308l-2.307 2.885-2.308-2.885H3.46v7.847zM21.232 12h-2.309V8.077h-2.307V12h-2.308l3.461 4.039z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">nuxt-content-specialist.md</span> <span class="file-tree__comment astro-o25vlg2d">// Your custom agent</span> </span> </li>  </ul> </details>   </li>  </ul> </details>   </li>  </ul> </nav> 
<details class="collapsible astro-kncz7yy6"> <summary class="collapsible-summary astro-kncz7yy6"> <span class="collapsible-icon astro-kncz7yy6"> <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="astro-kncz7yy6"> <polyline points="9 18 15 12 9 6" class="astro-kncz7yy6"></polyline> </svg> </span> Full agent definition </summary> <div class="collapsible-content astro-kncz7yy6"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"><span style="color:#F7768E">name</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> nuxt-content-specialist</span></span>
<span class="line"><span style="color:#F7768E">description</span><span style="color:#89DDFF">:</span><span style="color:#F7768E"> Use this agent when the task involves @nuxt/content v3 in any way - implementing, modifying, querying, reviewing, or improving content management code. This includes creating or modifying content collections, writing queries, implementing MDC components, configuring content sources, troubleshooting content-related issues, or reviewing existing content code for improvements and best practices.\n\nExamples:\n\n&lt;example&gt;\nContext</span><span style="color:#89DDFF">:</span><span style="color:#F7768E"> User asks about improving their Nuxt Content implementation.\nuser</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">What can I improve on this codebase when it comes to Nuxt Content?</span><span style="color:#89DDFF">&quot;</span><span style="color:#F7768E">\nassistant</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">I&#39;ll use the nuxt-content-specialist agent to review your content implementation against current best practices.</span><span style="color:#89DDFF">&quot;</span><span style="color:#F7768E">\n&lt;commentary&gt;\nSince the user is asking about Nuxt Content improvements, use the nuxt-content-specialist agent to fetch the latest documentation and review the existing code for optimization opportunities, missing features, and best practice violations.\n&lt;/commentary&gt;\n&lt;/example&gt;\n\n&lt;example&gt;\nContext</span><span style="color:#89DDFF">:</span><span style="color:#F7768E"> User needs to add a new content collection.\nuser</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">I need to add a &#39;blog&#39; collection separate from pages</span><span style="color:#89DDFF">&quot;</span><span style="color:#F7768E">\nassistant</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">I&#39;ll use the nuxt-content-specialist agent to implement this correctly.</span><span style="color:#89DDFF">&quot;</span><span style="color:#F7768E">\n&lt;commentary&gt;\nSince the user needs to modify the content collection schema, use the nuxt-content-specialist agent to first fetch the latest Nuxt Content documentation and then implement the collection following best practices.\n&lt;/commentary&gt;\n&lt;/example&gt;\n\n&lt;example&gt;\nContext</span><span style="color:#89DDFF">:</span><span style="color:#F7768E"> User is asking about content query patterns.\nuser</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">How do I query content by multiple tags in Nuxt Content?</span><span style="color:#89DDFF">&quot;</span><span style="color:#F7768E">\nassistant</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">Let me use the nuxt-content-specialist agent to provide an accurate answer based on the current documentation.</span><span style="color:#89DDFF">&quot;</span><span style="color:#F7768E">\n&lt;commentary&gt;\nSince the user is asking about Nuxt Content query capabilities, use the nuxt-content-specialist agent to fetch documentation and provide an accurate, up-to-date response about queryCollection filtering.\n&lt;/commentary&gt;\n&lt;/example&gt;\n\n&lt;example&gt;\nContext</span><span style="color:#89DDFF">:</span><span style="color:#F7768E"> User wants to embed Vue components in Markdown.\nuser</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">How do I use a custom component inside my markdown files?</span><span style="color:#89DDFF">&quot;</span><span style="color:#F7768E">\nassistant</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">I&#39;ll consult the nuxt-content-specialist agent to explain MDC syntax correctly.</span><span style="color:#89DDFF">&quot;</span><span style="color:#F7768E">\n&lt;commentary&gt;\nSince this involves MDC (Markdown Components) syntax, use the nuxt-content-specialist agent to fetch relevant documentation about component usage in Markdown files.\n&lt;/commentary&gt;\n&lt;/example&gt;\n\n&lt;example&gt;\nContext</span><span style="color:#89DDFF">:</span><span style="color:#F7768E"> User needs to implement content search.\nuser</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">I want to add full-text search to my content site</span><span style="color:#89DDFF">&quot;</span><span style="color:#F7768E">\nassistant</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">I&#39;ll use the nuxt-content-specialist agent to implement search with queryCollectionSearchSections.</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">\n&lt;commentary&gt;\nSince search requires specific Nuxt Content APIs, use the nuxt-content-specialist agent to fetch the latest documentation on search implementation patterns.\n&lt;/commentary&gt;\n&lt;/example&gt;</span></span>
<span class="line"><span style="color:#F7768E">model</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> opus</span></span>
<span class="line"><span style="color:#F7768E">color</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> green</span></span>
<span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF;font-weight:bold">#</span><span style="color:#89DDFF;font-weight:bold"> Nuxt Content Specialist Agent</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">This document defines the Nuxt Content specialist agent&#39;s role and responsibilities for helping users with @nuxt/content v3 implementations.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Primary Domain</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**@nuxt/content v3**</span><span style="color:#9AA5CE">: Content management system for Nuxt applications providing file-based content with Markdown support, MDC syntax for embedding Vue components, SQLite-based querying, and full-text search capabilities.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Core Expertise Areas</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">1.</span><span style="color:#C0CAF5;font-weight:bold"> **Collections**</span><span style="color:#9AA5CE">: Defining collections in </span><span style="color:#89DDFF">`content.config.ts`</span><span style="color:#9AA5CE">, schema validation with Zod, collection types (page, data), import sources</span></span>
<span class="line"><span style="color:#89DDFF">2.</span><span style="color:#C0CAF5;font-weight:bold"> **Content Files**</span><span style="color:#9AA5CE">: Markdown, YAML, JSON, CSV support and their appropriate use cases</span></span>
<span class="line"><span style="color:#89DDFF">3.</span><span style="color:#C0CAF5;font-weight:bold"> **MDC Syntax**</span><span style="color:#9AA5CE">: Embedding Vue components in Markdown, props, slots, block vs inline components</span></span>
<span class="line"><span style="color:#89DDFF">4.</span><span style="color:#C0CAF5;font-weight:bold"> **Querying**</span><span style="color:#9AA5CE">: </span><span style="color:#89DDFF">`queryCollection()`</span><span style="color:#9AA5CE">, </span><span style="color:#89DDFF">`queryCollectionNavigation()`</span><span style="color:#9AA5CE">, </span><span style="color:#89DDFF">`queryCollectionItemSurroundings()`</span><span style="color:#9AA5CE">, </span><span style="color:#89DDFF">`queryCollectionSearchSections()`</span></span>
<span class="line"><span style="color:#89DDFF">5.</span><span style="color:#C0CAF5;font-weight:bold"> **Rendering**</span><span style="color:#9AA5CE">: </span><span style="color:#89DDFF">`&lt;ContentRenderer&gt;`</span><span style="color:#9AA5CE">, </span><span style="color:#89DDFF">`&lt;Slot&gt;`</span><span style="color:#9AA5CE">, prose components, custom renderers</span></span>
<span class="line"><span style="color:#89DDFF">6.</span><span style="color:#C0CAF5;font-weight:bold"> **Search**</span><span style="color:#9AA5CE">: Full-text search implementation, search sections, indexing strategies</span></span>
<span class="line"><span style="color:#89DDFF">7.</span><span style="color:#C0CAF5;font-weight:bold"> **Sources**</span><span style="color:#9AA5CE">: Custom data sources, remote content, transformers</span></span>
<span class="line"><span style="color:#89DDFF">8.</span><span style="color:#C0CAF5;font-weight:bold"> **Deployment**</span><span style="color:#9AA5CE">: Static generation, server rendering, edge deployment considerations</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Documentation Sources</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">The agent leverages one primary documentation resource:</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#C0CAF5;font-weight:bold"> **Nuxt Content docs**</span><span style="color:#9AA5CE"> (</span><span style="color:#89DDFF">`https://content.nuxt.com/llms.txt`</span><span style="color:#9AA5CE">): Covers collection definitions, querying APIs, MDC syntax, content rendering, search implementation, custom sources, and deployment patterns</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Key Documentation Sections</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Section </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> URL Path </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Purpose </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|---------|----------|---------|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Collections </span><span style="color:#89DDFF">|</span><span style="color:#89DDFF"> `/docs/collections`</span><span style="color:#89DDFF"> |</span><span style="color:#C0CEFC"> Collection definitions and configuration </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Querying </span><span style="color:#89DDFF">|</span><span style="color:#89DDFF"> `/docs/querying`</span><span style="color:#89DDFF"> |</span><span style="color:#C0CEFC"> Query composables and filtering </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> ContentRenderer </span><span style="color:#89DDFF">|</span><span style="color:#89DDFF"> `/docs/components/content-renderer`</span><span style="color:#89DDFF"> |</span><span style="color:#C0CEFC"> Rendering content </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Markdown/MDC </span><span style="color:#89DDFF">|</span><span style="color:#89DDFF"> `/docs/files/markdown`</span><span style="color:#89DDFF"> |</span><span style="color:#C0CEFC"> Markdown and MDC syntax </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Search </span><span style="color:#89DDFF">|</span><span style="color:#89DDFF"> `/docs/recipes/search`</span><span style="color:#89DDFF"> |</span><span style="color:#C0CEFC"> Search implementation </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Sources </span><span style="color:#89DDFF">|</span><span style="color:#89DDFF"> `/docs/advanced/sources`</span><span style="color:#89DDFF"> |</span><span style="color:#C0CEFC"> Custom content sources </span><span style="color:#89DDFF">|</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Operational Approach</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">The agent follows a structured methodology:</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">1.</span><span style="color:#C0CAF5;font-weight:bold"> **Fetch documentation index**</span><span style="color:#9AA5CE"> from </span><span style="color:#89DDFF">`https://content.nuxt.com/llms.txt`</span><span style="color:#9AA5CE"> to understand available documentation structure</span></span>
<span class="line"><span style="color:#89DDFF">2.</span><span style="color:#C0CAF5;font-weight:bold"> **Categorize user inquiry**</span><span style="color:#9AA5CE"> into appropriate domain (collections, querying, MDC, search, etc.)</span></span>
<span class="line"><span style="color:#89DDFF">3.</span><span style="color:#C0CAF5;font-weight:bold"> **Identify specific documentation URLs**</span><span style="color:#9AA5CE"> from the index relevant to the task</span></span>
<span class="line"><span style="color:#89DDFF">4.</span><span style="color:#C0CAF5;font-weight:bold"> **Fetch targeted documentation pages**</span><span style="color:#9AA5CE"> for accurate, up-to-date information</span></span>
<span class="line"><span style="color:#89DDFF">5.</span><span style="color:#C0CAF5;font-weight:bold"> **Review project context**</span><span style="color:#9AA5CE"> by reading relevant local files (</span><span style="color:#89DDFF">`content.config.ts`</span><span style="color:#9AA5CE">, existing content files)</span></span>
<span class="line"><span style="color:#89DDFF">6.</span><span style="color:#C0CAF5;font-weight:bold"> **Provide actionable guidance**</span><span style="color:#9AA5CE"> with TypeScript code examples following project conventions</span></span>
<span class="line"><span style="color:#89DDFF">7.</span><span style="color:#C0CAF5;font-weight:bold"> **Reference documentation sources**</span><span style="color:#9AA5CE"> to support recommendations</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Core Guidelines</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Prioritize official documentation over training knowledge (v3 has significant v2 differences)</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Maintain concise, actionable responses</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Include TypeScript code examples following project conventions</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Reference specific documentation URLs consulted</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Avoid emojis</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Always verify API specifics against fetched documentation before providing guidance</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Note v2 to v3 migration considerations when relevant</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Consider static vs server rendering implications</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Handle content not found scenarios gracefully in implementations</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Project Context</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">This agent operates within a Nuxt 4 application using:</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#C0CAF5;font-weight:bold"> **@nuxt/content v3**</span><span style="color:#9AA5CE"> with SQLite-based querying</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#C0CAF5;font-weight:bold"> **@nuxt/ui v3**</span><span style="color:#9AA5CE"> for UI components</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#C0CAF5;font-weight:bold"> **TypeScript**</span><span style="color:#9AA5CE"> for type safety</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#C0CAF5;font-weight:bold"> **File-based routing**</span><span style="color:#9AA5CE"> with catch-all content routes in </span><span style="color:#89DDFF">`app/`</span><span style="color:#9AA5CE"> directory</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Established Patterns</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">```typescript</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">// content.config.ts - Collection definition pattern</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">defineCollection</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> z</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">@nuxt/content</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#9D7CD8;font-style:italic"> const</span><span style="color:#BB9AF7"> collections</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  content</span><span style="color:#89DDFF">:</span><span style="color:#7AA2F7"> defineCollection</span><span style="color:#9ABDF5">({</span></span>
<span class="line"><span style="color:#73DACA">    type</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">page</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    source</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">**/*.md</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"><span style="color:#89DDFF">```</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">```vue</span></span>
<span class="line"><span style="color:#89DDFF">&lt;!-- Catch-all route pattern: app/pages/[...slug].vue --&gt;</span></span>
<span class="line"><span style="color:#89DDFF">&lt;script setup lang=&quot;ts&quot;&gt;</span></span>
<span class="line"><span style="color:#89DDFF">const route = useRoute()</span></span>
<span class="line"><span style="color:#89DDFF">const { data: page } = await useAsyncData(</span></span>
<span class="line"><span style="color:#89DDFF">  route.path,</span></span>
<span class="line"><span style="color:#89DDFF">  () =&gt; queryCollection(&#39;content&#39;).path(route.path).first()</span></span>
<span class="line"><span style="color:#89DDFF">)</span></span>
<span class="line"><span style="color:#89DDFF">&lt;/script&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">&lt;template&gt;</span></span>
<span class="line"><span style="color:#89DDFF">  &lt;ContentRenderer v-if=&quot;page&quot; :value=&quot;page&quot; /&gt;</span></span>
<span class="line"><span style="color:#89DDFF">  &lt;div v-else&gt;Page not found&lt;/div&gt;</span></span>
<span class="line"><span style="color:#89DDFF">&lt;/template&gt;</span></span>
<span class="line"><span style="color:#89DDFF">```</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Quality Assurance</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Always verify suggestions against fetched documentation</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> If documentation is unclear or unavailable, explicitly state this with appropriate caveats</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> When multiple approaches exist, explain trade-offs</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Be aware of build-time vs runtime content access differences</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Ensure proper typing for collection queries and responses</span></span></code><button type="button" class="copy" data-code="---
name: nuxt-content-specialist
description: Use this agent when the task involves @nuxt/content v3 in any way - implementing, modifying, querying, reviewing, or improving content management code. This includes creating or modifying content collections, writing queries, implementing MDC components, configuring content sources, troubleshooting content-related issues, or reviewing existing content code for improvements and best practices.\n\nExamples:\n\n<example>\nContext: User asks about improving their Nuxt Content implementation.\nuser: &#34;What can I improve on this codebase when it comes to Nuxt Content?&#34;\nassistant: &#34;I'll use the nuxt-content-specialist agent to review your content implementation against current best practices.&#34;\n<commentary>\nSince the user is asking about Nuxt Content improvements, use the nuxt-content-specialist agent to fetch the latest documentation and review the existing code for optimization opportunities, missing features, and best practice violations.\n</commentary>\n</example>\n\n<example>\nContext: User needs to add a new content collection.\nuser: &#34;I need to add a 'blog' collection separate from pages&#34;\nassistant: &#34;I'll use the nuxt-content-specialist agent to implement this correctly.&#34;\n<commentary>\nSince the user needs to modify the content collection schema, use the nuxt-content-specialist agent to first fetch the latest Nuxt Content documentation and then implement the collection following best practices.\n</commentary>\n</example>\n\n<example>\nContext: User is asking about content query patterns.\nuser: &#34;How do I query content by multiple tags in Nuxt Content?&#34;\nassistant: &#34;Let me use the nuxt-content-specialist agent to provide an accurate answer based on the current documentation.&#34;\n<commentary>\nSince the user is asking about Nuxt Content query capabilities, use the nuxt-content-specialist agent to fetch documentation and provide an accurate, up-to-date response about queryCollection filtering.\n</commentary>\n</example>\n\n<example>\nContext: User wants to embed Vue components in Markdown.\nuser: &#34;How do I use a custom component inside my markdown files?&#34;\nassistant: &#34;I'll consult the nuxt-content-specialist agent to explain MDC syntax correctly.&#34;\n<commentary>\nSince this involves MDC (Markdown Components) syntax, use the nuxt-content-specialist agent to fetch relevant documentation about component usage in Markdown files.\n</commentary>\n</example>\n\n<example>\nContext: User needs to implement content search.\nuser: &#34;I want to add full-text search to my content site&#34;\nassistant: &#34;I'll use the nuxt-content-specialist agent to implement search with queryCollectionSearchSections.&#34;\n<commentary>\nSince search requires specific Nuxt Content APIs, use the nuxt-content-specialist agent to fetch the latest documentation on search implementation patterns.\n</commentary>\n</example>
model: opus
color: green
---

# Nuxt Content Specialist Agent

This document defines the Nuxt Content specialist agent's role and responsibilities for helping users with @nuxt/content v3 implementations.

## Primary Domain

**@nuxt/content v3**: Content management system for Nuxt applications providing file-based content with Markdown support, MDC syntax for embedding Vue components, SQLite-based querying, and full-text search capabilities.

### Core Expertise Areas

1. **Collections**: Defining collections in `content.config.ts`, schema validation with Zod, collection types (page, data), import sources
2. **Content Files**: Markdown, YAML, JSON, CSV support and their appropriate use cases
3. **MDC Syntax**: Embedding Vue components in Markdown, props, slots, block vs inline components
4. **Querying**: `queryCollection()`, `queryCollectionNavigation()`, `queryCollectionItemSurroundings()`, `queryCollectionSearchSections()`
5. **Rendering**: `<ContentRenderer>`, `<Slot>`, prose components, custom renderers
6. **Search**: Full-text search implementation, search sections, indexing strategies
7. **Sources**: Custom data sources, remote content, transformers
8. **Deployment**: Static generation, server rendering, edge deployment considerations

## Documentation Sources

The agent leverages one primary documentation resource:

- **Nuxt Content docs** (`https://content.nuxt.com/llms.txt`): Covers collection definitions, querying APIs, MDC syntax, content rendering, search implementation, custom sources, and deployment patterns

### Key Documentation Sections

| Section | URL Path | Purpose |
|---------|----------|---------|
| Collections | `/docs/collections` | Collection definitions and configuration |
| Querying | `/docs/querying` | Query composables and filtering |
| ContentRenderer | `/docs/components/content-renderer` | Rendering content |
| Markdown/MDC | `/docs/files/markdown` | Markdown and MDC syntax |
| Search | `/docs/recipes/search` | Search implementation |
| Sources | `/docs/advanced/sources` | Custom content sources |

## Operational Approach

The agent follows a structured methodology:

1. **Fetch documentation index** from `https://content.nuxt.com/llms.txt` to understand available documentation structure
2. **Categorize user inquiry** into appropriate domain (collections, querying, MDC, search, etc.)
3. **Identify specific documentation URLs** from the index relevant to the task
4. **Fetch targeted documentation pages** for accurate, up-to-date information
5. **Review project context** by reading relevant local files (`content.config.ts`, existing content files)
6. **Provide actionable guidance** with TypeScript code examples following project conventions
7. **Reference documentation sources** to support recommendations

## Core Guidelines

- Prioritize official documentation over training knowledge (v3 has significant v2 differences)
- Maintain concise, actionable responses
- Include TypeScript code examples following project conventions
- Reference specific documentation URLs consulted
- Avoid emojis
- Always verify API specifics against fetched documentation before providing guidance
- Note v2 to v3 migration considerations when relevant
- Consider static vs server rendering implications
- Handle content not found scenarios gracefully in implementations

## Project Context

This agent operates within a Nuxt 4 application using:

- **@nuxt/content v3** with SQLite-based querying
- **@nuxt/ui v3** for UI components
- **TypeScript** for type safety
- **File-based routing** with catch-all content routes in `app/` directory

### Established Patterns

```typescript
// content.config.ts - Collection definition pattern
import { defineCollection, z } from '@nuxt/content'

export const collections = {
  content: defineCollection({
    type: 'page',
    source: '**/*.md'
  })
}
```

```vue
<!-- Catch-all route pattern: app/pages/[...slug].vue -->
<script setup lang=&#34;ts&#34;>
const route = useRoute()
const { data: page } = await useAsyncData(
  route.path,
  () => queryCollection('content').path(route.path).first()
)
</script>

<template>
  <ContentRenderer v-if=&#34;page&#34; :value=&#34;page&#34; />
  <div v-else>Page not found</div>
</template>
```

## Quality Assurance

- Always verify suggestions against fetched documentation
- If documentation is unclear or unavailable, explicitly state this with appropriate caveats
- When multiple approaches exist, explain trade-offs
- Be aware of build-time vs runtime content access differences
- Ensure proper typing for collection queries and responses" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </details>  
<h2 id="key-design-principles">Key Design Principles<a class="heading-link" aria-label="Link to section" href="#key-design-principles"><span class="heading-link-icon">#</span></a></h2>
<p>The agent follows these principles:</p>
<ol>
<li><strong>Documentation-first</strong>: Always fetch <code>llms.txt</code> before answering anything</li>
<li><strong>Specific expertise</strong>: Focused on Nuxt Content v3, not general Nuxt knowledge</li>
<li><strong>Verification</strong>: Cross-reference documentation, don’t rely on training data</li>
<li><strong>Practical output</strong>: TypeScript code following project conventions</li>
</ol>
<h2 id="how-it-works-in-practice">How It Works in Practice<a class="heading-link" aria-label="Link to section" href="#how-it-works-in-practice"><span class="heading-link-icon">#</span></a></h2>
<p>When you ask Claude Code something like “How do hooks work in Nuxt Content?”, the main agent recognizes this matches the <code>nuxt-content-specialist</code> description and delegates to it.</p>
<figure class=" mx-auto "> <img src="/_astro/hooksexplained.DA3eqmQi_1vCxMK.webp" alt="Claude Code spawning the nuxt-content-specialist agent to research Nuxt Content hooks" loading="lazy" decoding="async" fetchpriority="auto" width="800" height="138" class="w-full"> <figcaption class="mt-2 text-center text-sm text-gray-500"> The agent researches in its own context while your main context stays clean </figcaption> </figure>
<p>The specialist agent then:</p>
<ol>
<li>Fetches <code>https://content.nuxt.com/llms.txt</code></li>
<li>Identifies the relevant documentation pages</li>
<li>Fetches the actual docs</li>
<li>Provides an accurate, up-to-date answer</li>
</ol>
<p>Your main context stays clean. The research happens in a separate context window.</p>
<h2 id="create-your-own">Create Your Own<a class="heading-link" aria-label="Link to section" href="#create-your-own"><span class="heading-link-icon">#</span></a></h2>
<p>You can apply this pattern to any library or framework:</p>
<ol>
<li>Find if they have <code>llms.txt</code> (most modern docs sites do)</li>
<li>Create an agent that fetches it first</li>
<li>Define the expertise scope in the description</li>
<li>Add examples so Claude Code knows when to delegate</li>
</ol>
<p>This approach gives you 98%+ reduction in token usage compared to loading full MCP tool definitions, while maintaining access to current documentation.</p> </article> <script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).only=e;window.dispatchEvent(new Event("astro:only"));})();</script><astro-island uid="Z1XneyL" component-url="/_astro/presentation.C3Wa0mjp.js" component-export="VMarkBlogRenderer" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;containerSelector&quot;:[0,&quot;#article&quot;],&quot;class&quot;:[0,&quot;astro-vj4tpspi&quot;]}" ssr client="only" opts="{&quot;name&quot;:&quot;VMarkBlogRenderer&quot;,&quot;value&quot;:&quot;react&quot;}"></astro-island> <!-- Fullscreen Modal Container using native dialog --><dialog id="mermaid-modal" class="mermaid-modal" aria-label="Fullscreen diagram view"> <div class="mermaid-modal-content"> <button class="mermaid-modal-close" aria-label="Close fullscreen view" type="button"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <line x1="18" y1="6" x2="6" y2="18"></line> <line x1="6" y1="6" x2="18" y2="18"></line> </svg> </button> <div class="mermaid-modal-diagram"></div> <div class="mermaid-modal-hint">Press <kbd>Esc</kbd> or click outside to close</div> </div> </dialog>  <script type="module">const p=new Set;function g(){const e=document.getElementById("mermaid-modal"),c=e?.querySelector(".mermaid-modal-diagram"),f=e?.querySelector(".mermaid-modal-close");if(!e||!c)return;document.querySelectorAll('svg[id^="mermaid-"]').forEach(t=>{if(!t.id.match(/^mermaid-\d+$/)||p.has(t.id)||t.parentElement?.classList.contains("mermaid-fullscreen-wrapper")||t.closest(".mermaid-modal"))return;p.add(t.id);const n=document.createElement("div");n.className="mermaid-fullscreen-wrapper mermaid-clickable",n.setAttribute("tabindex","0"),n.setAttribute("role","button"),n.setAttribute("aria-label","Click to view diagram fullscreen"),t.parentElement?.insertBefore(n,t),n.appendChild(t);const o=document.createElement("div");o.className="mermaid-expand-icon",o.innerHTML=`
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="15 3 21 3 21 9"></polyline>
          <polyline points="9 21 3 21 3 15"></polyline>
          <line x1="21" y1="3" x2="14" y2="10"></line>
          <line x1="3" y1="21" x2="10" y2="14"></line>
        </svg>
        <span>Fullscreen</span>
      `,n.appendChild(o);const d=m=>{m.stopPropagation(),c.innerHTML="";const i=t.cloneNode(!0),s=t.id,w=`-modal-${Date.now()}`,u=`${s}${w}`;i.setAttribute("id",u);const E=new Map;i.querySelectorAll("[id]").forEach(l=>{if(l===i)return;const a=l.getAttribute("id"),h=a+w;E.set(a,h),l.setAttribute("id",h)});let r=i.innerHTML;E.forEach((l,a)=>{r=r.replace(new RegExp(`url\\(#${a}\\)`,"g"),`url(#${l})`),r=r.replace(new RegExp(`href="#${a}"`,"g"),`href="#${l}"`)}),r=r.replace(new RegExp(`#${s}([^_\\w-])`,"g"),`#${u}$1`),r=r.replace(new RegExp(`#${s}\\{`,"g"),`#${u}{`),i.innerHTML=r,i.removeAttribute("style");const y=i.getAttribute("viewBox");if(y){const[,,l,a]=y.split(" ").map(Number);i.setAttribute("width",String(l)),i.setAttribute("height",String(a))}c.appendChild(i),e.showModal(),f.focus()};n.addEventListener("click",d),n.addEventListener("keydown",m=>{(m.key==="Enter"||m.key===" ")&&(m.preventDefault(),d(m))})}),f?.addEventListener("click",v),e?.addEventListener("click",t=>{const o=e?.querySelector(".mermaid-modal-content")?.getBoundingClientRect(),d=t;o&&(d.clientX<o.left||d.clientX>o.right||d.clientY<o.top||d.clientY>o.bottom)&&v()}),e.addEventListener("close",b)}function v(){const e=document.getElementById("mermaid-modal");e&&e.open&&e.close()}function b(){const c=document.getElementById("mermaid-modal")?.querySelector(".mermaid-modal-diagram");c&&(c.innerHTML="")}document.readyState==="loading"?document.addEventListener("DOMContentLoaded",g):g();document.addEventListener("astro:page-load",()=>{p.clear(),g()});</script>  <div id="cta-follow" class="notification-container fixed bottom-24 left-0 z-50 max-w-sm -translate-x-full opacity-0 transition-all duration-500 ease-out astro-vj4tpspi"> <div class="mx-4 transform rounded-lg border-l-4 border-skin-accent bg-skin-card p-6 shadow-xl transition-transform duration-200 hover:scale-[1.02] astro-vj4tpspi"> <div class="flex flex-col gap-4 astro-vj4tpspi"> <div class="flex items-center gap-3 astro-vj4tpspi"> <div class="rounded-full bg-skin-accent bg-opacity-10 p-2 astro-vj4tpspi"> <svg class="h-6 w-6 text-skin-accent astro-vj4tpspi" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg> </div> <h3 class="text-xl font-bold text-skin-accent astro-vj4tpspi">Stay Updated!</h3> </div> <div class="space-y-2 astro-vj4tpspi"> <p class="text-base leading-relaxed text-skin-base astro-vj4tpspi">
Subscribe to my newsletter for more TypeScript, Vue, and web dev
              insights directly in your inbox.
</p> <ul class="ml-1 list-inside list-disc space-y-1 text-sm text-skin-base astro-vj4tpspi"> <li class="astro-vj4tpspi">Background information about the articles</li> <li class="astro-vj4tpspi">
Weekly Summary of all the interesting blog posts that I read
</li> <li class="astro-vj4tpspi">Small tips and trick</li> </ul> </div> <a href="https://alex-op-newsletter.beehiiv.com/subscribe?utm_source=blog&utm_medium=post&utm_campaign=post_why-you-dont-need-nuxt-mcp-claude-code" target="_blank" rel="noopener noreferrer" id="newsletter-subscribe-button" class="inline-flex items-center justify-center gap-2 rounded-full bg-skin-accent px-6 py-3 text-base font-semibold text-skin-inverted shadow-md transition-all duration-200 hover:scale-[1.02] hover:transform hover:opacity-90 astro-vj4tpspi"> <svg class="h-5 w-5 fill-current astro-vj4tpspi" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg>
Subscribe Now
</a> <button id="newsletter-dismiss" data-post-slug="why-you-dont-need-nuxt-mcp-claude-code" class="absolute right-3 top-3 rounded-full p-1 text-skin-base transition-all duration-200 hover:bg-skin-accent hover:bg-opacity-10 hover:text-skin-accent astro-vj4tpspi" aria-label="Close notification"> <svg class="h-5 w-5 astro-vj4tpspi" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class="astro-vj4tpspi"></path> </svg> </button> </div> </div> </div> <ul class="my-8 flex flex-wrap gap-2 astro-vj4tpspi"> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/ai/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-2"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">ai</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/claude-code/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-3"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">claude-code</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/nuxt/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-4"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">nuxt</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/tooling/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-5"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">tooling</span>   </a> </li>  </ul> <div class="flex flex-col-reverse items-center justify-between gap-6 sm:flex-row-reverse sm:items-end sm:gap-4 astro-vj4tpspi"> <button id="back-to-top" class="focus-outline whitespace-nowrap py-1 hover:opacity-75 astro-vj4tpspi"> <svg xmlns="http://www.w3.org/2000/svg" class="rotate-90 astro-vj4tpspi"> <path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg> <span class="astro-vj4tpspi">Back to Top</span> </button> <div class="social-icons astro-wkojbtzc"> <span class="italic astro-wkojbtzc">Share this post on:</span> <div class="text-center astro-wkojbtzc"> <a href="https://wa.me/?text=https://alexop.dev/posts/why-you-dont-need-nuxt-mcp-claude-code/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via WhatsApp" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"></path>
      <path d="M9 10a0.5 .5 0 0 0 1 0v-1a0.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a0.5 .5 0 0 0 0 -1h-1a0.5 .5 0 0 0 0 1"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via WhatsApp</span> </a><a href="https://www.facebook.com/sharer.php?u=https://alexop.dev/posts/why-you-dont-need-nuxt-mcp-claude-code/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Facebook" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"
    ></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on Facebook</span> </a><a href="https://x.com/intent/tweet?url=https://alexop.dev/posts/why-you-dont-need-nuxt-mcp-claude-code/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Tweet this post" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Tweet this post</span> </a><a href="https://t.me/share/url?url=https://alexop.dev/posts/why-you-dont-need-nuxt-mcp-claude-code/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via Telegram" target="_blank" rel="noopener noreferrer"> <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon-tabler"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"></path>
      </svg> <span class="sr-only astro-wkojbtzc">Share this post via Telegram</span> </a><a href="https://pinterest.com/pin/create/button/?url=https://alexop.dev/posts/why-you-dont-need-nuxt-mcp-claude-code/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Pinterest" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <line x1="8" y1="20" x2="12" y2="11"></line>
      <path d="M10.7 14c.437 1.263 1.43 2 2.55 2c2.071 0 3.75 -1.554 3.75 -4a5 5 0 1 0 -9.7 1.7"></path>
      <circle cx="12" cy="12" r="9"></circle>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post on Pinterest</span> </a><a href="mailto:?subject=See%20this%20post&#38;body=https://alexop.dev/posts/why-you-dont-need-nuxt-mcp-claude-code/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via email" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via email</span> </a><a href="https://www.linkedin.com/shareArticle?mini=true&url=https://alexop.dev/posts/why-you-dont-need-nuxt-mcp-claude-code/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
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
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on LinkedIn</span> </a> </div> </div>  </div> <section id="comments-section" class="giscus-container"></section> <script type="module">function a(){const e=document.getElementById("comments-section");if(!e)return;e.querySelector(".giscus, iframe")&&(e.innerHTML="");const t=document.createElement("script");t.src="https://giscus.app/client.js",t.setAttribute("data-repo","alexanderop/blog-comments"),t.setAttribute("data-repo-id","R_kgDON-LviQ"),t.setAttribute("data-category","Q&A"),t.setAttribute("data-category-id","DIC_kwDON-Lvic4CnPll"),t.setAttribute("data-mapping","url"),t.setAttribute("data-strict","0"),t.setAttribute("data-reactions-enabled","1"),t.setAttribute("data-emit-metadata","0"),t.setAttribute("data-input-position","bottom"),t.setAttribute("data-theme","dark"),t.setAttribute("data-lang","en"),t.setAttribute("data-loading","lazy"),t.setAttribute("crossorigin","anonymous"),t.async=!0,e.appendChild(t)}a();document.addEventListener("astro:page-load",a);</script>  </main> <footer class="mt-auto astro-sz7xmlte"> <div class="max-w-5xl mx-auto px-4"> <hr class="border-skin-line" aria-hidden="true"> </div> <div class="footer-wrapper astro-sz7xmlte"> <div class="footer-content astro-sz7xmlte"> <div class="copyright-wrapper astro-sz7xmlte"> <span class="astro-sz7xmlte">Copyright &#169; 2026</span> <span class="separator astro-sz7xmlte">&nbsp;|&nbsp;</span> <span class="astro-sz7xmlte">All rights reserved.</span> </div> <div class="rss-prompt astro-sz7xmlte"> <a href="/rss.xml" class="rss-link group astro-sz7xmlte" title="Never miss a post - Subscribe via RSS" onclick="if (window.plausible) window.plausible('RSS Subscribe', { props: { location: 'footer' } })"> <div class="flex items-center gap-2 astro-sz7xmlte"> <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-skin-accent group-hover:animate-pulse astro-sz7xmlte"><path fill="currentColor" d="M19 20.001C19 11.729 12.271 5 4 5v2c7.168 0 13 5.832 13 13.001h2z" class="astro-sz7xmlte"></path><path fill="currentColor" d="M12 20.001h2C14 14.486 9.514 10 4 10v2c4.411 0 8 3.589 8 8.001z" class="astro-sz7xmlte"></path><circle cx="6" cy="18" r="2" fill="currentColor" class="astro-sz7xmlte"></circle> </svg> <span class="text-sm astro-sz7xmlte">Subscribe via RSS</span> </div> </a> </div> <div class="social-icons flex astro-upu6fzxr"> <a href="https://github.com/alexanderop" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title=" alexop.dev on Github" target="_blank" rel="noopener noreferrer"> <svg
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
    </script> </body> </html>  <script>(function(){const postSlug = "why-you-dont-need-nuxt-mcp-claude-code";

  function updateCTAFollowVisibility() {
    const cta = document.getElementById("cta-follow");
    const article = document.getElementById("article");
    if (!cta || !article) return;

    // If it has the force-hidden class, don't try to show it
    if (cta.classList.contains("force-hidden")) {
      return;
    }

    const viewportHeight = window.innerHeight;
    const articleBottom = article.getBoundingClientRect().bottom;

    // Only show if user has reached the end of the article (article bottom is visible)
    // and hasn't dismissed or subscribed
    if (
      articleBottom <= viewportHeight + 100 && // 100px buffer
      !localStorage.getItem("newsletter_dismissed") &&
      !localStorage.getItem("newsletter_subscribed")
    ) {
      cta.dataset.visible = "true";
      cta.style.transform = "translateX(0)";
      cta.style.opacity = "1";
    } else {
      cta.dataset.visible = "false";
      cta.style.transform = "translateX(-120%)";
      cta.style.opacity = "0";
    }
  }

  // Initialize visibility check
  window.addEventListener("scroll", updateCTAFollowVisibility);
  window.addEventListener("resize", updateCTAFollowVisibility);

  // Add a small delay to initial check to ensure proper positioning
  setTimeout(updateCTAFollowVisibility, 500);

  // Handle newsletter subscribe click with proper tracking
  document
    .getElementById("newsletter-subscribe-button")
    ?.addEventListener("click", () => {
      localStorage.setItem("newsletter_subscribed", "true");

      // Force the popup to stay hidden
      const cta = document.getElementById("cta-follow");
      if (cta) {
        cta.classList.add("force-hidden");
        cta.style.transform = "translateX(-120%)";
        cta.style.opacity = "0";
      }

      if (window.plausible) {
        window.plausible("Newsletter Subscribe Click", {
          props: {
            post: postSlug,
            location: "end_of_article",
            source: "notification",
          },
        });
      }
    });

  // Handle newsletter dismiss click
  document
    .getElementById("newsletter-dismiss")
    ?.addEventListener("click", function () {
      const slug = this.getAttribute("data-post-slug");
      localStorage.setItem("newsletter_dismissed", "true");

      const cta = document.getElementById("cta-follow");
      if (cta) {
        cta.classList.add("force-hidden");
        cta.style.transform = "translateX(-120%)";
        cta.style.opacity = "0";
      }

      if (window.plausible) {
        window.plausible("Newsletter Dismissed", {
          props: {
            post: slug,
            location: "end_of_article",
            source: "notification",
          },
        });
      }
    });
})();</script>  <script>
  /** Create a progress indicator
   *  at the top */
  function createProgressBar() {
    // Create the main container div
    const progressContainer = document.createElement("div");
    progressContainer.className =
      "progress-container fixed top-0 z-10 h-1 w-full bg-skin-fill";

    // Create the progress bar div
    const progressBar = document.createElement("div");
    progressBar.className = "progress-bar h-1 w-0 bg-skin-accent";
    progressBar.id = "myBar";

    // Append the progress bar to the progress container
    progressContainer.appendChild(progressBar);

    // Append the progress container to the document body or any other desired parent element
    document.body.appendChild(progressContainer);
  }
  createProgressBar();

  /** Update the progress bar
   *  when user scrolls */
  function updateScrollProgress() {
    const winScroll =
      document.body.scrollTop || document.documentElement.scrollTop;
    const height =
      document.documentElement.scrollHeight -
      document.documentElement.clientHeight;
    const scrolled = (winScroll / height) * 100;
    const myBar = document.getElementById("myBar");
    if (myBar) {
      myBar.style.width = scrolled + "%";
    }
  }
  document.addEventListener("scroll", updateScrollProgress);

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

  /** Scroll back to top functionality */
  function attachBackToTop() {
    const backToTopBtn = document.getElementById("back-to-top");
    if (backToTopBtn) {
      backToTopBtn.addEventListener("click", () => {
        window.scrollTo({ top: 0, behavior: "smooth" });
      });
    }
  }
  attachBackToTop();
</script>
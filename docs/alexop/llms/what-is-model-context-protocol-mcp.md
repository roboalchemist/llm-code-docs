# Source: https://alexop.dev/posts/what-is-model-context-protocol-mcp

<!DOCTYPE html><html lang="en" class="scroll-smooth astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/posts/what-is-model-context-protocol-mcp/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>What Is the Model Context Protocol (MCP)? How It Works | alexop.dev</title><meta name="title" content="What Is the Model Context Protocol (MCP)? How It Works | alexop.dev"><meta name="description" content="Learn how MCP (Model Context Protocol) standardizes AI tool integration, enabling LLMs to interact with external services, databases, and APIs through a universal protocol similar to USB-C for AI applications."><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="What Is the Model Context Protocol (MCP)? How It Works | alexop.dev"><meta property="og:description" content="Learn how MCP (Model Context Protocol) standardizes AI tool integration, enabling LLMs to interact with external services, databases, and APIs through a universal protocol similar to USB-C for AI applications."><meta property="og:url" content="https://alexop.dev/posts/what-is-model-context-protocol-mcp/"><meta property="og:image" content="https://alexop.dev/posts/what-is-the-model-context-protocol-mcp-how-it-works/index.png"><meta property="og:type" content="article"><!-- Article Published/Modified time --><meta property="article:published_time" content="2025-08-10T00:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/posts/what-is-model-context-protocol-mcp/"><meta property="twitter:title" content="What Is the Model Context Protocol (MCP)? How It Works | alexop.dev"><meta property="twitter:description" content="Learn how MCP (Model Context Protocol) standardizes AI tool integration, enabling LLMs to interact with external services, databases, and APIs through a universal protocol similar to USB-C for AI applications."><meta property="twitter:image" content="https://alexop.dev/posts/what-is-the-model-context-protocol-mcp-how-it-works/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"What Is the Model Context Protocol (MCP)? How It Works | alexop.dev","description":"Learn how MCP (Model Context Protocol) standardizes AI tool integration, enabling LLMs to interact with external services, databases, and APIs through a universal protocol similar to USB-C for AI applications.","image":"https://alexop.dev/posts/what-is-the-model-context-protocol-mcp-how-it-works/index.png","datePublished":"2025-08-10T00:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
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
</style><style>[data-astro-transition-scope="astro-plk3gbjq-1"] { view-transition-name: what-is-the-model-context-protocol-mcp-how-it-works; }@layer astro { ::view-transition-old(what-is-the-model-context-protocol-mcp-how-it-works) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(what-is-the-model-context-protocol-mcp-how-it-works) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(what-is-the-model-context-protocol-mcp-how-it-works) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(what-is-the-model-context-protocol-mcp-how-it-works) { 
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
</style><style>.captioned-image:where(.astro-t2d64o5a){margin:2rem auto;text-align:center;max-width:600px}.captioned-image:where(.astro-t2d64o5a) img:where(.astro-t2d64o5a){max-width:100%;height:auto}.captioned-image:where(.astro-t2d64o5a) figcaption:where(.astro-t2d64o5a){margin-top:.5rem;font-style:italic;color:var(--text-base)}
</style><style>.grid-cards-container:where(.astro-g5e4s2ea){display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1.5rem;margin:1.5rem 0}.grid-card:where(.astro-g5e4s2ea){padding:1rem;border-radius:.5rem;border:1px solid rgb(139,233,253,.2);background:#3038464d}.grid-card-title:where(.astro-g5e4s2ea){font-size:1.125rem;font-weight:700;margin-bottom:.75rem;color:#8be9fd;display:flex;align-items:center;gap:.5rem}.grid-card-icon:where(.astro-g5e4s2ea){font-size:1.25rem}.grid-card-list:where(.astro-g5e4s2ea){list-style:none;padding:0;margin:0}.grid-card-list:where(.astro-g5e4s2ea) li:where(.astro-g5e4s2ea){margin-bottom:.5rem;padding-left:1rem;position:relative}.grid-card-list:where(.astro-g5e4s2ea) li:where(.astro-g5e4s2ea):last-child{margin-bottom:0}.grid-card-list:where(.astro-g5e4s2ea) li:where(.astro-g5e4s2ea):before{content:"•";position:absolute;left:0}@media(prefers-color-scheme:light){.grid-card:where(.astro-g5e4s2ea){background:#8be9fd0d;border-color:#8be9fd4d}}
</style><style>.internal-link-wrapper:where(.astro-3tyn5ojg){position:relative;display:inline-block}.internal-link:where(.astro-3tyn5ojg){--tw-text-opacity: 1;color:rgba(var(--color-accent),var(--tw-text-opacity, 1));text-decoration-line:underline;text-decoration-style:dashed;text-decoration-thickness:1px;text-underline-offset:4px;transition-property:all;transition-timing-function:cubic-bezier(.4,0,.2,1);transition-duration:.15s}.internal-link:where(.astro-3tyn5ojg):hover{text-decoration-style:solid}.internal-link:where(.astro-3tyn5ojg){cursor:pointer;display:inline}.preview-card:where(.astro-3tyn5ojg){display:block;position:absolute;bottom:calc(100% + 8px);left:50%;transform:translate(-50%);z-index:9999;width:320px;max-width:90vw;border-radius:.5rem;border-width:1px;--tw-border-opacity: 1;border-color:rgba(var(--color-border),var(--tw-border-opacity, 1));--tw-bg-opacity: 1;background-color:rgba(var(--color-card),var(--tw-bg-opacity, 1));--tw-shadow: 0 10px 15px -3px rgb(0 0 0 / .1), 0 4px 6px -4px rgb(0 0 0 / .1);--tw-shadow-colored: 0 10px 15px -3px var(--tw-shadow-color), 0 4px 6px -4px var(--tw-shadow-color);box-shadow:var(--tw-ring-offset-shadow, 0 0 #0000),var(--tw-ring-shadow, 0 0 #0000),var(--tw-shadow);opacity:0;visibility:hidden;transition:opacity .2s ease-in-out,visibility .2s ease-in-out}.preview-card:where(.astro-3tyn5ojg).is-fixed{position:fixed!important;bottom:auto!important;top:var(--pc-top, 0px)!important;left:var(--pc-left, 0px)!important;transform:none!important}.preview-content:where(.astro-3tyn5ojg){display:block;padding:1rem}.preview-title:where(.astro-3tyn5ojg){display:block;margin-bottom:.5rem;font-size:1rem;line-height:1.5rem;font-weight:600;--tw-text-opacity: 1;color:rgba(var(--color-text-base),var(--tw-text-opacity, 1));line-height:1.3}.preview-title:where(.astro-3tyn5ojg) .heading-link:where(.astro-3tyn5ojg){display:none!important}.preview-description:where(.astro-3tyn5ojg){display:block;margin-bottom:.75rem;font-size:.875rem;line-height:1.25rem;color:rgba(var(--color-text-base),.8);line-height:1.4;overflow:hidden;text-overflow:ellipsis;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical}.preview-tags:where(.astro-3tyn5ojg){margin-bottom:.5rem;display:flex;flex-wrap:wrap;gap:.375rem}.preview-tag:where(.astro-3tyn5ojg){border-radius:.25rem;padding:.125rem .5rem;font-size:.75rem;line-height:1rem;background-color:rgba(var(--color-accent),.1);--tw-text-opacity: 1;color:rgba(var(--color-accent),var(--tw-text-opacity, 1));font-weight:500}.preview-tag-more:where(.astro-3tyn5ojg){border-radius:.25rem;padding:.125rem .5rem;font-size:.75rem;line-height:1rem;--tw-bg-opacity: 1;background-color:rgba(var(--color-fill),var(--tw-bg-opacity, 1));color:rgba(var(--color-text-base),.6);font-weight:500}.preview-date:where(.astro-3tyn5ojg){font-size:.75rem;line-height:1rem;color:rgba(var(--color-text-base),.6);display:block;margin-top:8px;font-style:italic}.preview-card:where(.astro-3tyn5ojg):after{content:"";position:absolute;top:100%;left:50%;transform:translate(-50%);border:6px solid transparent;border-top-color:var(--color-card)}.preview-card:where(.astro-3tyn5ojg).is-fixed:after{display:none}
</style><style>[data-astro-transition-scope="astro-36ssibgs-2"] { view-transition-name: mcp; }@layer astro { ::view-transition-old(mcp) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(mcp) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(mcp) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(mcp) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-3"] { view-transition-name: typescript; }@layer astro { ::view-transition-old(typescript) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(typescript) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(typescript) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(typescript) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-4"] { view-transition-name: ai; }@layer astro { ::view-transition-old(ai) { 
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <div class="mx-auto flex w-full max-w-5xl justify-start px-2 astro-vj4tpspi"> <button class="focus-outline mb-2 mt-8 flex hover:opacity-75 astro-vj4tpspi" onclick="(() => (history.length === 1) ? window.location = '/' : history.back())()"> <svg xmlns="http://www.w3.org/2000/svg" class="astro-vj4tpspi"><path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg><span class="astro-vj4tpspi">Go back</span> </button> </div> <main data-pagefind-body id="main-content" class="relative astro-vj4tpspi"> <h1 class="post-title astro-vj4tpspi" data-astro-transition-scope="astro-plk3gbjq-1">What Is the Model Context Protocol (MCP)? How It Works</h1> <div class="my-2 flex items-center justify-between astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-100 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-base"><time dateTime="2025-08-10T00:00:00.000Z">Aug 10, 2025</time><span class="sr-only"> at </span></span></div> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="Z1bemY7" prefix="r6" component-url="/_astro/PostCopyButton.-PGtk4At.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;title&quot;:[0,&quot;What Is the Model Context Protocol (MCP)? How It Works&quot;],&quot;content&quot;:[0,&quot;import Alert from \&quot;@features/mdx-components/components/Alert.astro\&quot;;\nimport GridCards from \&quot;../../components/GridCards.astro\&quot;;\nimport CaptionedImage from \&quot;@features/mdx-components/components/CaptionedImage.astro\&quot;;\nimport InternalLink from \&quot;@features/mdx-components/components/InternalLink.astro\&quot;;\nimport robotMcpComic from \&quot;../../assets/images/mcp/comic-mcp-robot.png\&quot;;\nimport scalingProblemComic from \&quot;../../assets/images/mcp/mcp-scaling-problem-comic.png\&quot;;\n\nI did not see how powerful MCP was until I used Claude Code with the Playwright MCP.\n**Playwright MCP lets an AI use a real browser.** It can open a page, click buttons, fill forms, and take screenshots.\nI asked Claude to audit my site for SEO. It ran checks in a real browser, gave me the results, and sent screenshots. You can read more about &lt;InternalLink slug=\&quot;how-i-use-claude-code-for-doing-seo-audits\&quot;&gt;how I use Claude Code for doing SEO audits&lt;/InternalLink&gt;.\n**That was when I saw it.** This was not just text prediction. This was an AI that can see and work with the web like a human tester.\n\n## What is MCP\n\nMCP means Model Context Protocol.\nBefore we define it, let us see how we got here.\n\n## How it started\n\n```mermaid\nflowchart TD\n    U[User] --&gt; A[LLM]\n    A --&gt; U\n```\n\nIn 2022 ChatGPT made AI open to everyone.\nYou typed a question. It predicted the next tokens and sent back text.\nYou could ask for your favorite author or create code.\n\n## The problem with plain LLMs\n\nA plain LLM is a text generator.\n\n- It has no live data\n- It cannot read your files\n- It struggles with math\n- It cannot tell you who won yesterday in football\n\nYou can read more in my post about &lt;InternalLink slug=\&quot;how-chatgpt-works-for-dummies\&quot;&gt;LLM limits&lt;/InternalLink&gt;.\n\n## The first fix: tools\n\n```mermaid {scale: &#39;0.5&#39;}\nflowchart TD\n    U[User] --&gt; A[LLM]\n    A --&gt; D{Needs Python?}\n    D --&gt;|Yes| P[Run code in Python sandbox]\n    P --&gt; O[Execution result]\n    O --&gt; A\n    D --&gt;|No| A\n    A --&gt; U\n```\n\nWhen OpenAI added a Python sandbox, LLMs could run code and give exact results.\n\n## More tools mean more power\n\n```mermaid {scale: &#39;0.5&#39;}\nflowchart TD\n    U[User] --&gt; A[LLM]\n    A --&gt; D{Needs external tool?}\n\n    D --&gt;|Python| P[Run code in Python sandbox]\n    P --&gt; O[Execution result]\n    O --&gt; A\n\n    D --&gt;|Web search| W[Search the web for information]\n    W --&gt; R[Search result]\n    R --&gt; A\n\n    D --&gt;|No| A\n    A --&gt; U\n```\n\nWeb search gave live knowledge. Now the model could answer fresh questions.\n\n## Even more tools\n\n```mermaid {scale: &#39;0.5&#39;}\nflowchart TD\n    U[User] --&gt; A[LLM]\n    A --&gt; D{Needs external tool?}\n\n    D --&gt;|Python| P[Run code in Python sandbox]\n    P --&gt; O[Execution result]\n    O --&gt; A\n\n    D --&gt;|Web search| W[Search the web for information]\n    W --&gt; R[Search result]\n    R --&gt; A\n\n    D --&gt;|Google Calendar| G[Check / update calendar events]\n    G --&gt; E[Calendar data]\n    E --&gt; A\n\n    D --&gt;|No| A\n    A --&gt; U\n```\n\nAnthropic added more tools to Claude like Google Calendar and email.\nYou can ask it what meetings you have next week and it tells you.\n\n&lt;CaptionedImage\n  src={scalingProblemComic}\n  alt=\&quot;Comic showing multiple teams reinventing the wheel by building the same API connectors\&quot;\n  caption=\&quot;If every team builds their own tool for connecting to email, calendar, and other APIs, everyone reinvents the wheel\&quot;\n/&gt;\n\n## The solution: a protocol\n\nWe need a standard.\nOne tool for Google Calendar that any agent can use.\nIn November the Model Context Protocol was released.\n\n## Definition\n\n**MCP** is an open protocol that lets apps give context to LLMs in a standard way.\n\nThink of **USB-C**. You plug in power, a display, or storage and it just works.\n\nMCP does the same for AI with data sources and tools.\n\nWith MCP you can build agents and workflows without custom glue code.\n\n&lt;CaptionedImage\n  src={robotMcpComic}\n  alt=\&quot;Robot MCP Comic showing how MCP connects different tools and services\&quot;\n  caption=\&quot;MCP acts as the universal connector for AI tools and services\&quot;\n/&gt;\n\n---\n\n## How MCP Works (mental model)\n\nAt its core, MCP has **three roles**:\n\n- **Host** → LLM applications that initiate connections\n- **Client** → Connectors within the host application\n- **Server** → Services that provide context and capabilities\n\n&lt;Alert type=\&quot;note\&quot;&gt;\n  MCP takes some inspiration from the Language Server Protocol, which\n  standardizes how to add support for programming languages across a whole\n  ecosystem of development tools. In a similar way, MCP standardizes how to\n  integrate additional context and tools into the ecosystem of AI applications.\n&lt;/Alert&gt;\n\nThe host embeds clients, and those clients connect to one or more servers.\nYour VS Code could have a Playwright MCP server for browser automation and another MCP server for your docs — all running at the same time.\n\n```mermaid\nflowchart LR\n  U((User))\n  U --&gt; H[Host UI&lt;br&gt;Claude Desktop, VS Code/Claude Code]\n  H --&gt; C1[MCP Client 1]\n  H --&gt; C2[MCP Client 2]\n  H --&gt; C3[MCP Client 3]\n  C1 --&gt; S1[MCP Server A]\n  C2 --&gt; S2[MCP Server B]\n  C3 --&gt; S3[MCP Server C]\n```\n\n---\n\n## How MCP Connects: Transports\n\nMCP uses **JSON-RPC 2.0** for all messages and supports two main transport mechanisms:\n\n&lt;GridCards\n  cards={[\n    {\n      title: \&quot;stdio (local)\&quot;,\n      icon: \&quot;📍\&quot;,\n      items: [\n        \&quot;Server runs as subprocess of the client\&quot;,\n        \&quot;Messages flow through stdin/stdout pipes\&quot;,\n        \&quot;No network latency - instant communication\&quot;,\n        \&quot;Perfect for local tools and dev environments\&quot;,\n      ],\n    },\n    {\n      title: \&quot;Streamable HTTP (remote)\&quot;,\n      icon: \&quot;🌐\&quot;,\n      items: [\n        \&quot;Single HTTP endpoint for all operations\&quot;,\n        \&quot;POST for sending messages, GET for listening\&quot;,\n        \&quot;Server-Sent Events (SSE) for streaming\&quot;,\n        \&quot;Ideal for cloud-hosted MCP servers\&quot;,\n      ],\n    },\n  ]}\n/&gt;\n\n**Key points:**\n\n- Messages are UTF-8 encoded JSON-RPC\n- stdio uses newline-delimited JSON (one message per line)\n- HTTP supports session management via `Mcp-Session-Id` headers\n- Both transports handle requests, responses, and notifications equally well\n\nThe transport choice depends on your use case: stdio for local tools with minimal latency, HTTP for remote services that multiple clients can connect to.\n\n## What servers can expose\n\nAn MCP server can offer any combination of three capabilities:\n\n### Tools: Functions the AI can call\n\n- Give AI ability to execute actions (check weather, query databases, solve math)\n- Each tool describes what it does and what info it needs\n- AI sends parameters → server runs function → returns results\n\n```typescript\n// Simple calculator tool example\nserver.registerTool(\n  \&quot;calculate\&quot;,\n  {\n    title: \&quot;Calculator\&quot;,\n    description: \&quot;Perform mathematical calculations\&quot;,\n    inputSchema: {\n      operation: z.enum([\&quot;add\&quot;, \&quot;subtract\&quot;, \&quot;multiply\&quot;, \&quot;divide\&quot;]),\n      a: z.number(),\n      b: z.number(),\n    },\n  },\n  async ({ operation, a, b }) =&gt; {\n    let result;\n    switch (operation) {\n      case \&quot;add\&quot;:\n        result = a + b;\n        break;\n      case \&quot;subtract\&quot;:\n        result = a - b;\n        break;\n      case \&quot;multiply\&quot;:\n        result = a * b;\n        break;\n      case \&quot;divide\&quot;:\n        result = b !== 0 ? a / b : \&quot;Error: Division by zero\&quot;;\n        break;\n    }\n\n    return {\n      content: [\n        {\n          type: \&quot;text\&quot;,\n          text: `${a} ${operation} ${b} = ${result}`,\n        },\n      ],\n    };\n  }\n);\n```\n\n### Resources: Context and data\n\n- AI can read files, docs, database schemas\n- Provides context before answering questions or using tools\n- Supports change notifications when files update\n\n```typescript\nserver.registerResource(\n  \&quot;app-config\&quot;,\n  \&quot;config://application\&quot;,\n  {\n    title: \&quot;Application Configuration\&quot;,\n    description: \&quot;Current app settings and environment\&quot;,\n    mimeType: \&quot;application/json\&quot;,\n  },\n  async uri =&gt; ({\n    contents: [\n      {\n        uri: uri.href,\n        text: JSON.stringify(\n          {\n            environment: process.env.NODE_ENV,\n            version: \&quot;1.0.0\&quot;,\n            features: {\n              darkMode: true,\n              analytics: false,\n              beta: process.env.BETA === \&quot;true\&quot;,\n            },\n          },\n          null,\n          2\n        ),\n      },\n    ],\n  })\n);\n```\n\n### Prompts: Templates for interaction\n\n- Pre-made templates for common tasks (code review, data analysis)\n- Exposed as slash commands or UI elements\n- Makes repetitive workflows quick and consistent\n\n````typescript\nserver.registerPrompt(\n  \&quot;code-review\&quot;,\n  {\n    title: \&quot;Code Review\&quot;,\n    description: \&quot;Review code for quality and best practices\&quot;,\n    argsSchema: {\n      language: z.enum([\&quot;javascript\&quot;, \&quot;typescript\&quot;, \&quot;python\&quot;, \&quot;go\&quot;]),\n      code: z.string(),\n      focus: z\n        .enum([\&quot;security\&quot;, \&quot;performance\&quot;, \&quot;readability\&quot;, \&quot;all\&quot;])\n        .default(\&quot;all\&quot;),\n    },\n  },\n  ({ language, code, focus }) =&gt; ({\n    messages: [\n      {\n        role: \&quot;user\&quot;,\n        content: {\n          type: \&quot;text\&quot;,\n          text: [\n            `Please review this ${language} code focusing on ${focus}:`,\n            \&quot;\&quot;,\n            \&quot;```\&quot; + language,\n            code,\n            \&quot;```\&quot;,\n            \&quot;\&quot;,\n            \&quot;Provide feedback on:\&quot;,\n            focus === \&quot;all\&quot;\n              ? \&quot;- Security issues\\n- Performance optimizations\\n- Code readability\\n- Best practices\&quot;\n              : focus === \&quot;security\&quot;\n                ? \&quot;- Potential security vulnerabilities\\n- Input validation\\n- Authentication/authorization issues\&quot;\n                : focus === \&quot;performance\&quot;\n                  ? \&quot;- Time complexity\\n- Memory usage\\n- Potential optimizations\&quot;\n                  : \&quot;- Variable naming\\n- Code structure\\n- Comments and documentation\&quot;,\n          ].join(\&quot;\\n\&quot;),\n        },\n      },\n    ],\n  })\n);\n````\n\n## What a Client can expose\n\nAn MCP client can provide capabilities that let servers interact with the world beyond their sandbox:\n\n### Roots: Filesystem boundaries\n\n- Client tells server which directories it can access\n- Creates secure sandbox (e.g., only your project folder)\n- Prevents access to system files or other projects\n\n### Sampling: Nested LLM calls\n\n- Servers can request AI completions through the client\n- No API keys needed on server side\n- Enables autonomous, agentic behaviors\n\n### Elicitation: Asking users for input\n\n- Servers request missing info from users via client UI\n- Client handles forms and validation\n- Users can accept, decline, or cancel requests\n\n## Example: How we can use MCPS in Vscode\n\nYour `mcp.json` could look like this:\n\n```json\n{\n  \&quot;servers\&quot;: {\n    \&quot;playwright\&quot;: {\n      \&quot;gallery\&quot;: true,\n      \&quot;command\&quot;: \&quot;npx\&quot;,\n      \&quot;args\&quot;: [\&quot;@playwright/mcp@latest\&quot;],\n      \&quot;type\&quot;: \&quot;stdio\&quot;\n    },\n    \&quot;deepwiki\&quot;: {\n      \&quot;type\&quot;: \&quot;http\&quot;,\n      \&quot;url\&quot;: \&quot;https://mcp.deepwiki.com/sse\&quot;,\n      \&quot;gallery\&quot;: true\n    }\n  }\n}\n```\n\n- **playwright** → Runs `npx @playwright/mcp@latest` locally over stdio for low-latency browser automation\n- **deepwiki** → Connects over HTTP/SSE to `https://mcp.deepwiki.com/sse` for live docs and codebase search\n- **gallery: true** → Makes them visible in tool pickers\n\n## What MCP is not\n\n- **Not a hosted service** — It is a protocol\n- **Not a replacement** for your app logic\n- **Not a magic fix** for every hallucination — It gives access to real tools and data\n- You still need good prompts and good UX\n\n---\n\n## Simple example of your first MCP Server\n\n```ts\n#!/usr/bin/env node\nimport { z } from \&quot;zod\&quot;;\nimport { McpServer } from \&quot;@modelcontextprotocol/sdk/server/mcp.js\&quot;;\nimport { StdioServerTransport } from \&quot;@modelcontextprotocol/sdk/server/stdio.js\&quot;;\n\nconst server = new McpServer({\n  name: \&quot;echo-onefile\&quot;,\n  version: \&quot;1.0.0\&quot;,\n});\n\nserver.tool(\n  \&quot;echo\&quot;,\n  \&quot;Echo back the provided text\&quot;,\n  {\n    text: z\n      .string()\n      .min(1, \&quot;Text cannot be empty\&quot;)\n      .describe(\&quot;Text to echo back\&quot;),\n  },\n  async ({ text }) =&gt; ({\n    content: [{ type: \&quot;text\&quot;, text }],\n  })\n);\n\nconst transport = new StdioServerTransport();\n\nserver\n  .connect(transport)\n  .then(() =&gt; console.error(\&quot;Echo MCP server listening on stdio\&quot;))\n  .catch(err =&gt; {\n    console.error(err);\n    process.exit(1);\n  });\n```\n\nThis example uses the official [MCP SDK for TypeScript](https://modelcontextprotocol.io/docs/sdk), which provides type-safe abstractions for building MCP servers.\n\nThe server exposes a single tool called \&quot;echo\&quot; that takes text input and returns it back. We&#39;re using [Zod](https://zod.dev/) for runtime schema validation, ensuring the input matches our expected structure with proper type safety and clear error messages.\n\n## Simple MCP Client Example\n\nHere&#39;s how to connect to an MCP server and use its capabilities:\n\n```typescript\nimport { Client } from \&quot;@modelcontextprotocol/sdk/client/index.js\&quot;;\nimport { StdioClientTransport } from \&quot;@modelcontextprotocol/sdk/client/stdio.js\&quot;;\n\n// Create a client that connects to your MCP server\nasync function connectToServer() {\n  // Create transport - this runs your server as a subprocess\n  const transport = new StdioClientTransport({\n    command: \&quot;node\&quot;,\n    args: [\&quot;./echo-server.js\&quot;],\n  });\n\n  // Create and connect the client\n  const client = new Client({\n    name: \&quot;my-mcp-client\&quot;,\n    version: \&quot;1.0.0\&quot;,\n  });\n\n  await client.connect(transport);\n\n  return client;\n}\n\n// Use the server&#39;s capabilities\nasync function useServer() {\n  const client = await connectToServer();\n\n  // List available tools\n  const tools = await client.listTools();\n  console.log(\&quot;Available tools:\&quot;, tools);\n\n  // Call a tool\n  const result = await client.callTool({\n    name: \&quot;echo\&quot;,\n    arguments: {\n      text: \&quot;Hello from MCP client!\&quot;,\n    },\n  });\n\n  console.log(\&quot;Tool result:\&quot;, result.content);\n\n  // List and read resources\n  const resources = await client.listResources();\n  for (const resource of resources) {\n    const content = await client.readResource({\n      uri: resource.uri,\n    });\n    console.log(`Resource ${resource.name}:`, content);\n  }\n\n  // Get and execute a prompt\n  const prompts = await client.listPrompts();\n  if (prompts.length &gt; 0) {\n    const prompt = await client.getPrompt({\n      name: prompts[0].name,\n      arguments: {\n        code: \&quot;console.log(&#39;test&#39;)\&quot;,\n        language: \&quot;javascript\&quot;,\n      },\n    });\n    console.log(\&quot;Prompt messages:\&quot;, prompt.messages);\n  }\n\n  // Clean up\n  await client.close();\n}\n\n// Run the client\nuseServer().catch(console.error);\n```\n\nThis client example shows how to:\n\n- Connect to an MCP server using stdio transport\n- List and call tools with arguments\n- Read resources from the server\n- Get and use prompt templates\n- Properly close the connection when done\n\n## Use it with Vscode\n\n```json\n{\n  \&quot;servers\&quot;: {\n    \&quot;echo\&quot;: {\n      \&quot;gallery\&quot;: true,\n      \&quot;type\&quot;: \&quot;stdio\&quot;,\n      \&quot;command\&quot;: \&quot;node\&quot;,\n      \&quot;args\&quot;: [\&quot;--import\&quot;, \&quot;tsx\&quot;, \&quot;/absolute/path/echo-server.ts\&quot;]\n    }\n  }\n}\n```\n\n## Summary\n\nThis was just my starter post for MCP to give an overview. I will write more blog posts that will go in depth about the different topics.\n\n&lt;Alert type=\&quot;note\&quot;&gt;\n  If you need a TypeScript starter template for your next MCP server, you can\n  use my\n  [mcp-server-starter-ts](https://github.com/alexanderop/mcp-server-starter-ts)\n  repository to get up and running quickly.\n&lt;/Alert&gt;&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PostCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus-outline inline-flex items-center gap-1.5 rounded-md border border-skin-line bg-skin-card px-2.5 py-1.5 text-xs font-medium text-skin-base opacity-80 transition-all hover:border-skin-accent/50 hover:text-skin-accent hover:opacity-100" aria-label="Copy post as markdown" title="Copy post as markdown for AI/LLM"><svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg><span>Copy Post</span></button><!--astro:end--></astro-island> </div>  <article id="article" class="prose mx-auto mt-8 max-w-5xl astro-vj4tpspi"> <p>I did not see how powerful MCP was until I used Claude Code with the Playwright MCP.
<strong>Playwright MCP lets an AI use a real browser.</strong> It can open a page, click buttons, fill forms, and take screenshots.
I asked Claude to audit my site for SEO. It ran checks in a real browser, gave me the results, and sent screenshots. You can read more about <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/how-i-use-claude-code-for-doing-seo-audits/" class="internal-link astro-3tyn5ojg"> how I use Claude Code for doing SEO audits </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">How I Use Claude Code for Doing SEO Audits</span> <span class="preview-description astro-3tyn5ojg">Learn how to leverage Claude Code with Puppeteer MCP to perform comprehensive SEO audits in minutes, complete with automated analysis and actionable reports.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">claude-code</span><span class="preview-tag astro-3tyn5ojg">ai</span><span class="preview-tag astro-3tyn5ojg">seo</span>  </span> <time class="preview-date astro-3tyn5ojg">Jun 26, 2025</time> </span> </span> </span>  <script>
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
</script>.
<strong>That was when I saw it.</strong> This was not just text prediction. This was an AI that can see and work with the web like a human tester.</p>
<h2 id="what-is-mcp">What is MCP<a class="heading-link" aria-label="Link to section" href="#what-is-mcp"><span class="heading-link-icon">#</span></a></h2>
<p>MCP means Model Context Protocol.
Before we define it, let us see how we got here.</p>
<h2 id="how-it-started">How it started<a class="heading-link" aria-label="Link to section" href="#how-it-started"><span class="heading-link-icon">#</span></a></h2>
<p><svg id="mermaid-0" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="flowchart" style="max-width:114.53125px" viewBox="0 0 114.53125 174" role="graphics-document document" aria-roledescription="flowchart-v2"><style>#mermaid-0{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-0 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-0 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-0 .error-icon{fill:#a44141;}#mermaid-0 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-0 .edge-thickness-normal{stroke-width:1px;}#mermaid-0 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-0 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-0 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-0 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-0 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-0 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-0 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-0 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-0 p{margin:0;}#mermaid-0 .label{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;color:#ccc;}#mermaid-0 .cluster-label text{fill:#F9FFFE;}#mermaid-0 .cluster-label span{color:#F9FFFE;}#mermaid-0 .cluster-label span p{background-color:transparent;}#mermaid-0 .label text,#mermaid-0 span{fill:#ccc;color:#ccc;}#mermaid-0 .node rect,#mermaid-0 .node circle,#mermaid-0 .node ellipse,#mermaid-0 .node polygon,#mermaid-0 .node path{fill:transparent;stroke:2px;stroke-width:1px;}#mermaid-0 .rough-node .label text,#mermaid-0 .node .label text,#mermaid-0 .image-shape .label,#mermaid-0 .icon-shape .label{text-anchor:middle;}#mermaid-0 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-0 .rough-node .label,#mermaid-0 .node .label,#mermaid-0 .image-shape .label,#mermaid-0 .icon-shape .label{text-align:center;}#mermaid-0 .node.clickable{cursor:pointer;}#mermaid-0 .root .anchor path{fill:rgb(171, 75, 153)!important;stroke-width:0;stroke:rgb(171, 75, 153);}#mermaid-0 .arrowheadPath{fill:lightgrey;}#mermaid-0 .edgePath .path{stroke:rgb(171, 75, 153);stroke-width:2.0px;}#mermaid-0 .flowchart-link{stroke:rgb(171, 75, 153);fill:none;}#mermaid-0 .edgeLabel{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-0 .edgeLabel p{background-color:hsla(0, 0%, 25%, 0);}#mermaid-0 .edgeLabel rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-0 .labelBkg{background-color:rgba(63.75, 63.75, 63.75, 0.5);}#mermaid-0 .cluster rect{fill:transparent;stroke:rgba(255, 255, 255, 0.25);stroke-width:1px;}#mermaid-0 .cluster text{fill:#F9FFFE;}#mermaid-0 .cluster span{color:#F9FFFE;}#mermaid-0 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:12px;background:rgb(138, 51, 123);border:1px solid rgba(255, 255, 255, 0.25);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-0 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-0 rect.text{fill:none;stroke-width:0;}#mermaid-0 .icon-shape,#mermaid-0 .image-shape{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-0 .icon-shape p,#mermaid-0 .image-shape p{background-color:hsla(0, 0%, 25%, 0);padding:2px;}#mermaid-0 .icon-shape rect,#mermaid-0 .image-shape rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-0 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-0 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-0 :root{--mermaid-font-family:arial,sans-serif;}</style><g><marker id="mermaid-0_flowchart-v2-pointEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-pointStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="4.5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 5 L 10 10 L 10 0 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-circleEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="11" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-0_flowchart-v2-circleStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="-1" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-0_flowchart-v2-crossEnd" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="12" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-crossStart" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="-1" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><g class="root"><g class="clusters"></g><g class="edgePaths"><path d="M52.073,62L51.272,66.167C50.471,70.333,48.868,78.667,48.742,86.345C48.616,94.024,49.967,101.048,50.643,104.56L51.318,108.072" id="L_U_A_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_U_A_0" data-points="W3sieCI6NTIuMDczMzE3MzA3NjkyMzEsInkiOjYyfSx7IngiOjQ3LjI2NTYyNSwieSI6ODd9LHsieCI6NTIuMDczMzE3MzA3NjkyMzEsInkiOjExMn1d" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M62.458,112L63.259,107.833C64.06,103.667,65.663,95.333,65.789,87.655C65.915,79.976,64.564,72.952,63.889,69.44L63.213,65.928" id="L_A_U_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_A_U_0" data-points="W3sieCI6NjIuNDU3OTMyNjkyMzA3NjksInkiOjExMn0seyJ4Ijo2Ny4yNjU2MjUsInkiOjg3fSx7IngiOjYyLjQ1NzkzMjY5MjMwNzY5LCJ5Ijo2Mn1d" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path></g><g class="edgeLabels"><g class="edgeLabel"><g class="label" data-id="L_U_A_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_A_U_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g></g><g class="nodes"><g class="node default" id="flowchart-U-0" transform="translate(57.265625, 35)"><rect class="basic label-container" style="" x="-49.265625" y="-27" width="98.53125" height="54"></rect><g class="label" style="" transform="translate(-19.265625, -12)"><rect></rect><foreignObject width="38.53125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>User</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-A-1" transform="translate(57.265625, 139)"><rect class="basic label-container" style="" x="-44.453125" y="-27" width="88.90625" height="54"></rect><g class="label" style="" transform="translate(-14.453125, -12)"><rect></rect><foreignObject width="28.90625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>LLM</p></span></div></foreignObject></g></g></g></g></g></svg></p>
<p>In 2022 ChatGPT made AI open to everyone.
You typed a question. It predicted the next tokens and sent back text.
You could ask for your favorite author or create code.</p>
<h2 id="the-problem-with-plain-llms">The problem with plain LLMs<a class="heading-link" aria-label="Link to section" href="#the-problem-with-plain-llms"><span class="heading-link-icon">#</span></a></h2>
<p>A plain LLM is a text generator.</p>
<ul>
<li>It has no live data</li>
<li>It cannot read your files</li>
<li>It struggles with math</li>
<li>It cannot tell you who won yesterday in football</li>
</ul>
<p>You can read more in my post about <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/how-chatgpt-works-for-dummies/" class="internal-link astro-3tyn5ojg"> LLM limits </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">How ChatGPT Works (for Dummies)</span> <span class="preview-description astro-3tyn5ojg">A plain English guide to how ChatGPT works—from token prediction to hallucinations. Perfect for developers who want to understand the AI they&#39;re building with.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">ai</span>  </span> <time class="preview-date astro-3tyn5ojg">Apr 21, 2025</time> </span> </span> </span>  <script>
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
<h2 id="the-first-fix-tools">The first fix: tools<a class="heading-link" aria-label="Link to section" href="#the-first-fix-tools"><span class="heading-link-icon">#</span></a></h2>
<p><svg id="mermaid-1" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="flowchart" style="max-width:335.5625px" viewBox="0 0 335.5625 683.234375" role="graphics-document document" aria-roledescription="flowchart-v2"><style>#mermaid-1{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-1 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-1 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-1 .error-icon{fill:#a44141;}#mermaid-1 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-1 .edge-thickness-normal{stroke-width:1px;}#mermaid-1 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-1 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-1 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-1 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-1 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-1 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-1 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-1 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-1 p{margin:0;}#mermaid-1 .label{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;color:#ccc;}#mermaid-1 .cluster-label text{fill:#F9FFFE;}#mermaid-1 .cluster-label span{color:#F9FFFE;}#mermaid-1 .cluster-label span p{background-color:transparent;}#mermaid-1 .label text,#mermaid-1 span{fill:#ccc;color:#ccc;}#mermaid-1 .node rect,#mermaid-1 .node circle,#mermaid-1 .node ellipse,#mermaid-1 .node polygon,#mermaid-1 .node path{fill:transparent;stroke:2px;stroke-width:1px;}#mermaid-1 .rough-node .label text,#mermaid-1 .node .label text,#mermaid-1 .image-shape .label,#mermaid-1 .icon-shape .label{text-anchor:middle;}#mermaid-1 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-1 .rough-node .label,#mermaid-1 .node .label,#mermaid-1 .image-shape .label,#mermaid-1 .icon-shape .label{text-align:center;}#mermaid-1 .node.clickable{cursor:pointer;}#mermaid-1 .root .anchor path{fill:rgb(171, 75, 153)!important;stroke-width:0;stroke:rgb(171, 75, 153);}#mermaid-1 .arrowheadPath{fill:lightgrey;}#mermaid-1 .edgePath .path{stroke:rgb(171, 75, 153);stroke-width:2.0px;}#mermaid-1 .flowchart-link{stroke:rgb(171, 75, 153);fill:none;}#mermaid-1 .edgeLabel{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-1 .edgeLabel p{background-color:hsla(0, 0%, 25%, 0);}#mermaid-1 .edgeLabel rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-1 .labelBkg{background-color:rgba(63.75, 63.75, 63.75, 0.5);}#mermaid-1 .cluster rect{fill:transparent;stroke:rgba(255, 255, 255, 0.25);stroke-width:1px;}#mermaid-1 .cluster text{fill:#F9FFFE;}#mermaid-1 .cluster span{color:#F9FFFE;}#mermaid-1 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:12px;background:rgb(138, 51, 123);border:1px solid rgba(255, 255, 255, 0.25);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-1 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-1 rect.text{fill:none;stroke-width:0;}#mermaid-1 .icon-shape,#mermaid-1 .image-shape{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-1 .icon-shape p,#mermaid-1 .image-shape p{background-color:hsla(0, 0%, 25%, 0);padding:2px;}#mermaid-1 .icon-shape rect,#mermaid-1 .image-shape rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-1 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-1 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-1 :root{--mermaid-font-family:arial,sans-serif;}</style><g><marker id="mermaid-1_flowchart-v2-pointEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-1_flowchart-v2-pointStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="4.5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 5 L 10 10 L 10 0 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-1_flowchart-v2-circleEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="11" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-1_flowchart-v2-circleStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="-1" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-1_flowchart-v2-crossEnd" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="12" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-1_flowchart-v2-crossStart" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="-1" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><g class="root"><g class="clusters"></g><g class="edgePaths"><path d="M152.816,62L152.816,66.167C152.816,70.333,152.816,78.667,152.816,86.333C152.816,94,152.816,101,152.816,104.5L152.816,108" id="L_U_A_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_U_A_0" data-points="W3sieCI6MTUyLjgxNjQwNjI1LCJ5Ijo2Mn0seyJ4IjoxNTIuODE2NDA2MjUsInkiOjg3fSx7IngiOjE1Mi44MTY0MDYyNSwieSI6MTEyfV0=" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path><path d="M140.315,166L137.46,172.167C134.605,178.333,128.894,190.667,126.866,203.903C124.838,217.138,126.492,231.277,127.32,238.346L128.147,245.415" id="L_A_D_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_A_D_0" data-points="W3sieCI6MTQwLjMxNTA2MzQ3NjU2MjUsInkiOjE2Nn0seyJ4IjoxMjMuMTgzNTkzNzUsInkiOjIwM30seyJ4IjoxMjguNjExODE1NjEwNTg2MzUsInkiOjI0OS4zODgxODQzODk0MTM2NX1d" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path><path d="M138,419.234L138,425.401C138,431.568,138,443.901,138,455.568C138,467.234,138,478.234,138,483.734L138,489.234" id="L_D_P_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_D_P_0" data-points="W3sieCI6MTM4LCJ5Ijo0MTkuMjM0Mzc1fSx7IngiOjEzOCwieSI6NDU2LjIzNDM3NX0seyJ4IjoxMzgsInkiOjQ5My4yMzQzNzV9XQ==" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path><path d="M138,571.234L138,575.401C138,579.568,138,587.901,144.047,595.879C150.093,603.857,162.186,611.479,168.233,615.29L174.28,619.101" id="L_P_O_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_P_O_0" data-points="W3sieCI6MTM4LCJ5Ijo1NzEuMjM0Mzc1fSx7IngiOjEzOCwieSI6NTk2LjIzNDM3NX0seyJ4IjoxNzcuNjYzNDYxNTM4NDYxNTUsInkiOjYyMS4yMzQzNzV9XQ==" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path><path d="M263.337,621.234L269.947,617.068C276.558,612.901,289.779,604.568,296.389,589.734C303,574.901,303,553.568,303,530.234C303,506.901,303,481.568,303,447.798C303,414.029,303,371.823,303,329.617C303,287.411,303,245.206,285.992,216.855C268.983,188.504,234.966,174.008,217.958,166.76L200.949,159.512" id="L_O_A_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_O_A_0" data-points="W3sieCI6MjYzLjMzNjUzODQ2MTUzODQ1LCJ5Ijo2MjEuMjM0Mzc1fSx7IngiOjMwMywieSI6NTk2LjIzNDM3NX0seyJ4IjozMDMsInkiOjUzMi4yMzQzNzV9LHsieCI6MzAzLCJ5Ijo0NTYuMjM0Mzc1fSx7IngiOjMwMywieSI6MzI5LjYxNzE4NzV9LHsieCI6MzAzLCJ5IjoyMDN9LHsieCI6MTk3LjI2OTUzMTI1LCJ5IjoxNTcuOTQzNDgwNjM1NjgwM31d" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path><path d="M147.388,249.388L148.293,241.657C149.198,233.925,151.007,218.463,151.912,205.231C152.816,192,152.816,181,152.816,175.5L152.816,170" id="L_D_A_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_D_A_0" data-points="W3sieCI6MTQ3LjM4ODE4NDM4OTQxMzY1LCJ5IjoyNDkuMzg4MTg0Mzg5NDEzNjV9LHsieCI6MTUyLjgxNjQwNjI1LCJ5IjoyMDN9LHsieCI6MTUyLjgxNjQwNjI1LCJ5IjoxNjZ9XQ==" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path><path d="M163.201,112L164.804,107.833C166.406,103.667,169.611,95.333,169.851,87.622C170.09,79.911,167.363,72.822,166,69.278L164.637,65.733" id="L_A_U_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_A_U_0" data-points="W3sieCI6MTYzLjIwMTAyMTYzNDYxNTQsInkiOjExMn0seyJ4IjoxNzIuODE2NDA2MjUsInkiOjg3fSx7IngiOjE2My4yMDEwMjE2MzQ2MTU0LCJ5Ijo2Mn1d" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path></g><g class="edgeLabels"><g class="edgeLabel"><g class="label" data-id="L_U_A_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_A_D_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(138, 456.234375)"><g class="label" data-id="L_D_P_0" transform="translate(-14.453125, -12)"><foreignObject width="28.90625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>Yes</p></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_P_O_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_O_A_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(152.81640625, 203)"><g class="label" data-id="L_D_A_0" transform="translate(-9.6328125, -12)"><foreignObject width="19.265625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>No</p></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_A_U_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g></g><g class="nodes"><g class="node default" id="flowchart-U-0" transform="translate(152.81640625, 35)"><rect class="basic label-container" style="" x="-49.265625" y="-27" width="98.53125" height="54"></rect><g class="label" style="" transform="translate(-19.265625, -12)"><rect></rect><foreignObject width="38.53125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>User</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-A-1" transform="translate(152.81640625, 139)"><rect class="basic label-container" style="" x="-44.453125" y="-27" width="88.90625" height="54"></rect><g class="label" style="" transform="translate(-14.453125, -12)"><rect></rect><foreignObject width="28.90625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>LLM</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-D-3" transform="translate(138, 329.6171875)"><polygon points="89.6171875,0 179.234375,-89.6171875 89.6171875,-179.234375 0,-89.6171875" class="label-container" transform="translate(-89.1171875, 89.6171875)"></polygon><g class="label" style="" transform="translate(-62.6171875, -12)"><rect></rect><foreignObject width="125.234375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Needs Python?</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-P-5" transform="translate(138, 532.234375)"><rect class="basic label-container" style="" x="-130" y="-39" width="260" height="78"></rect><g class="label" style="" transform="translate(-100, -24)"><rect></rect><foreignObject width="200" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table;white-space:break-spaces;line-height:1.5;max-width:200px;text-align:center;width:200px"><span class="nodeLabel"><p>Run code in Python sandbox</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-O-7" transform="translate(220.5, 648.234375)"><rect class="basic label-container" style="" x="-107.0625" y="-27" width="214.125" height="54"></rect><g class="label" style="" transform="translate(-77.0625, -12)"><rect></rect><foreignObject width="154.125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Execution result</p></span></div></foreignObject></g></g></g></g></g></svg></p>
<p>When OpenAI added a Python sandbox, LLMs could run code and give exact results.</p>
<h2 id="more-tools-mean-more-power">More tools mean more power<a class="heading-link" aria-label="Link to section" href="#more-tools-mean-more-power"><span class="heading-link-icon">#</span></a></h2>
<p><svg id="mermaid-2" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="flowchart" style="max-width:651.1171875px" viewBox="0 0 651.1171875 750.65625" role="graphics-document document" aria-roledescription="flowchart-v2"><style>#mermaid-2{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-2 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-2 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-2 .error-icon{fill:#a44141;}#mermaid-2 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-2 .edge-thickness-normal{stroke-width:1px;}#mermaid-2 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-2 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-2 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-2 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-2 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-2 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-2 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-2 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-2 p{margin:0;}#mermaid-2 .label{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;color:#ccc;}#mermaid-2 .cluster-label text{fill:#F9FFFE;}#mermaid-2 .cluster-label span{color:#F9FFFE;}#mermaid-2 .cluster-label span p{background-color:transparent;}#mermaid-2 .label text,#mermaid-2 span{fill:#ccc;color:#ccc;}#mermaid-2 .node rect,#mermaid-2 .node circle,#mermaid-2 .node ellipse,#mermaid-2 .node polygon,#mermaid-2 .node path{fill:transparent;stroke:2px;stroke-width:1px;}#mermaid-2 .rough-node .label text,#mermaid-2 .node .label text,#mermaid-2 .image-shape .label,#mermaid-2 .icon-shape .label{text-anchor:middle;}#mermaid-2 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-2 .rough-node .label,#mermaid-2 .node .label,#mermaid-2 .image-shape .label,#mermaid-2 .icon-shape .label{text-align:center;}#mermaid-2 .node.clickable{cursor:pointer;}#mermaid-2 .root .anchor path{fill:rgb(171, 75, 153)!important;stroke-width:0;stroke:rgb(171, 75, 153);}#mermaid-2 .arrowheadPath{fill:lightgrey;}#mermaid-2 .edgePath .path{stroke:rgb(171, 75, 153);stroke-width:2.0px;}#mermaid-2 .flowchart-link{stroke:rgb(171, 75, 153);fill:none;}#mermaid-2 .edgeLabel{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-2 .edgeLabel p{background-color:hsla(0, 0%, 25%, 0);}#mermaid-2 .edgeLabel rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-2 .labelBkg{background-color:rgba(63.75, 63.75, 63.75, 0.5);}#mermaid-2 .cluster rect{fill:transparent;stroke:rgba(255, 255, 255, 0.25);stroke-width:1px;}#mermaid-2 .cluster text{fill:#F9FFFE;}#mermaid-2 .cluster span{color:#F9FFFE;}#mermaid-2 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:12px;background:rgb(138, 51, 123);border:1px solid rgba(255, 255, 255, 0.25);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-2 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-2 rect.text{fill:none;stroke-width:0;}#mermaid-2 .icon-shape,#mermaid-2 .image-shape{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-2 .icon-shape p,#mermaid-2 .image-shape p{background-color:hsla(0, 0%, 25%, 0);padding:2px;}#mermaid-2 .icon-shape rect,#mermaid-2 .image-shape rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-2 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-2 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-2 :root{--mermaid-font-family:arial,sans-serif;}</style><g><marker id="mermaid-2_flowchart-v2-pointEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-2_flowchart-v2-pointStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="4.5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 5 L 10 10 L 10 0 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-2_flowchart-v2-circleEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="11" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-2_flowchart-v2-circleStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="-1" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-2_flowchart-v2-crossEnd" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="12" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-2_flowchart-v2-crossStart" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="-1" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><g class="root"><g class="clusters"></g><g class="edgePaths"><path d="M230.124,62L229.323,66.167C228.522,70.333,226.919,78.667,226.793,86.345C226.667,94.024,228.018,101.048,228.693,104.56L229.369,108.072" id="L_U_A_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_U_A_0" data-points="W3sieCI6MjMwLjEyNDA5ODU1NzY5MjMyLCJ5Ijo2Mn0seyJ4IjoyMjUuMzE2NDA2MjUsInkiOjg3fSx7IngiOjIzMC4xMjQwOTg1NTc2OTIzMiwieSI6MTEyfV0=" marker-end="url(#mermaid-2_flowchart-v2-pointEnd)"></path><path d="M190.863,164.372L179.583,170.81C168.303,177.248,145.743,190.124,135.133,203.804C124.522,217.483,125.86,231.967,126.53,239.208L127.199,246.45" id="L_A_D_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_A_D_0" data-points="W3sieCI6MTkwLjg2MzI4MTI1LCJ5IjoxNjQuMzcxNjk5Mjk2MzE0Mzh9LHsieCI6MTIzLjE4MzU5Mzc1LCJ5IjoyMDN9LHsieCI6MTI3LjU2NzAxODc5ODY0ODQzLCJ5IjoyNTAuNDMyOTgxMjAxMzUxNTd9XQ==" marker-end="url(#mermaid-2_flowchart-v2-pointEnd)"></path><path d="M138,486.656L138,492.823C138,498.99,138,511.323,138,522.99C138,534.656,138,545.656,138,551.156L138,556.656" id="L_D_P_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_D_P_0" data-points="W3sieCI6MTM4LCJ5Ijo0ODYuNjU2MjV9LHsieCI6MTM4LCJ5Ijo1MjMuNjU2MjV9LHsieCI6MTM4LCJ5Ijo1NjAuNjU2MjV9XQ==" marker-end="url(#mermaid-2_flowchart-v2-pointEnd)"></path><path d="M138,638.656L138,642.823C138,646.99,138,655.323,144.047,663.301C150.093,671.279,162.186,678.901,168.233,682.712L174.28,686.523" id="L_P_O_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_P_O_0" data-points="W3sieCI6MTM4LCJ5Ijo2MzguNjU2MjV9LHsieCI6MTM4LCJ5Ijo2NjMuNjU2MjV9LHsieCI6MTc3LjY2MzQ2MTUzODQ2MTU1LCJ5Ijo2ODguNjU2MjV9XQ==" marker-end="url(#mermaid-2_flowchart-v2-pointEnd)"></path><path d="M263.337,688.656L269.947,684.49C276.558,680.323,289.779,671.99,296.389,657.156C303,642.323,303,620.99,303,597.656C303,574.323,303,548.99,303,509.602C303,470.214,303,416.771,303,363.328C303,309.885,303,256.443,296.963,224.013C290.926,191.583,278.851,180.165,272.814,174.457L266.777,168.748" id="L_O_A_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_O_A_0" data-points="W3sieCI6MjYzLjMzNjUzODQ2MTUzODQ1LCJ5Ijo2ODguNjU2MjV9LHsieCI6MzAzLCJ5Ijo2NjMuNjU2MjV9LHsieCI6MzAzLCJ5Ijo1OTkuNjU2MjV9LHsieCI6MzAzLCJ5Ijo1MjMuNjU2MjV9LHsieCI6MzAzLCJ5IjozNjMuMzI4MTI1fSx7IngiOjMwMywieSI6MjAzfSx7IngiOjI2My44NzA0MjIzNjMyODEyNSwieSI6MTY2fV0=" marker-end="url(#mermaid-2_flowchart-v2-pointEnd)"></path><path d="M221.002,403.654L262.168,423.654C303.335,443.655,385.667,483.656,426.834,509.156C468,534.656,468,545.656,468,551.156L468,556.656" id="L_D_W_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_D_W_0" data-points="W3sieCI6MjIxLjAwMjEzNTA0OTg3MDkzLCJ5Ijo0MDMuNjU0MTE0OTUwMTI5MDR9LHsieCI6NDY4LCJ5Ijo1MjMuNjU2MjV9LHsieCI6NDY4LCJ5Ijo1NjAuNjU2MjV9XQ==" marker-end="url(#mermaid-2_flowchart-v2-pointEnd)"></path><path d="M468,638.656L468,642.823C468,646.99,468,655.323,474.047,663.301C480.093,671.279,492.186,678.901,498.233,682.712L504.28,686.523" id="L_W_R_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_W_R_0" data-points="W3sieCI6NDY4LCJ5Ijo2MzguNjU2MjV9LHsieCI6NDY4LCJ5Ijo2NjMuNjU2MjV9LHsieCI6NTA3LjY2MzQ2MTUzODQ2MTU1LCJ5Ijo2ODguNjU2MjV9XQ==" marker-end="url(#mermaid-2_flowchart-v2-pointEnd)"></path><path d="M593.337,688.656L599.947,684.49C606.558,680.323,619.779,671.99,626.389,657.156C633,642.323,633,620.99,633,597.656C633,574.323,633,548.99,633,509.602C633,470.214,633,416.771,633,363.328C633,309.885,633,256.443,574.786,220.353C516.573,184.263,400.146,165.526,341.932,156.158L283.719,146.789" id="L_R_A_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_R_A_0" data-points="W3sieCI6NTkzLjMzNjUzODQ2MTUzODUsInkiOjY4OC42NTYyNX0seyJ4Ijo2MzMsInkiOjY2My42NTYyNX0seyJ4Ijo2MzMsInkiOjU5OS42NTYyNX0seyJ4Ijo2MzMsInkiOjUyMy42NTYyNX0seyJ4Ijo2MzMsInkiOjM2My4zMjgxMjV9LHsieCI6NjMzLCJ5IjoyMDN9LHsieCI6Mjc5Ljc2OTUzMTI1LCJ5IjoxNDYuMTUzOTI4NTExNzkxOTJ9XQ==" marker-end="url(#mermaid-2_flowchart-v2-pointEnd)"></path><path d="M148.433,250.433L149.164,242.527C149.894,234.622,151.355,218.811,159.508,205.147C167.661,191.484,182.506,179.968,189.929,174.21L197.351,168.452" id="L_D_A_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_D_A_0" data-points="W3sieCI6MTQ4LjQzMjk4MTIwMTM1MTU3LCJ5IjoyNTAuNDMyOTgxMjAxMzUxNTd9LHsieCI6MTUyLjgxNjQwNjI1LCJ5IjoyMDN9LHsieCI6MjAwLjUxMTcxODc1LCJ5IjoxNjZ9XQ==" marker-end="url(#mermaid-2_flowchart-v2-pointEnd)"></path><path d="M240.509,112L241.31,107.833C242.111,103.667,243.714,95.333,243.84,87.655C243.966,79.976,242.615,72.952,241.939,69.44L241.264,65.928" id="L_A_U_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_A_U_0" data-points="W3sieCI6MjQwLjUwODcxMzk0MjMwNzY4LCJ5IjoxMTJ9LHsieCI6MjQ1LjMxNjQwNjI1LCJ5Ijo4N30seyJ4IjoyNDAuNTA4NzEzOTQyMzA3NjgsInkiOjYyfV0=" marker-end="url(#mermaid-2_flowchart-v2-pointEnd)"></path></g><g class="edgeLabels"><g class="edgeLabel"><g class="label" data-id="L_U_A_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_A_D_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(138, 523.65625)"><g class="label" data-id="L_D_P_0" transform="translate(-28.8984375, -12)"><foreignObject width="57.796875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>Python</p></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_P_O_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_O_A_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(468, 523.65625)"><g class="label" data-id="L_D_W_0" transform="translate(-48.1640625, -12)"><foreignObject width="96.328125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>Web search</p></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_W_R_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_R_A_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(157.84522, 199.09886)"><g class="label" data-id="L_D_A_0" transform="translate(-9.6328125, -12)"><foreignObject width="19.265625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>No</p></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_A_U_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g></g><g class="nodes"><g class="node default" id="flowchart-U-0" transform="translate(235.31640625, 35)"><rect class="basic label-container" style="" x="-49.265625" y="-27" width="98.53125" height="54"></rect><g class="label" style="" transform="translate(-19.265625, -12)"><rect></rect><foreignObject width="38.53125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>User</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-A-1" transform="translate(235.31640625, 139)"><rect class="basic label-container" style="" x="-44.453125" y="-27" width="88.90625" height="54"></rect><g class="label" style="" transform="translate(-14.453125, -12)"><rect></rect><foreignObject width="28.90625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>LLM</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-D-3" transform="translate(138, 363.328125)"><polygon points="123.328125,0 246.65625,-123.328125 123.328125,-246.65625 0,-123.328125" class="label-container" transform="translate(-122.828125, 123.328125)"></polygon><g class="label" style="" transform="translate(-96.328125, -12)"><rect></rect><foreignObject width="192.65625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Needs external tool?</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-P-5" transform="translate(138, 599.65625)"><rect class="basic label-container" style="" x="-130" y="-39" width="260" height="78"></rect><g class="label" style="" transform="translate(-100, -24)"><rect></rect><foreignObject width="200" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table;white-space:break-spaces;line-height:1.5;max-width:200px;text-align:center;width:200px"><span class="nodeLabel"><p>Run code in Python sandbox</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-O-7" transform="translate(220.5, 715.65625)"><rect class="basic label-container" style="" x="-107.0625" y="-27" width="214.125" height="54"></rect><g class="label" style="" transform="translate(-77.0625, -12)"><rect></rect><foreignObject width="154.125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Execution result</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-W-11" transform="translate(468, 599.65625)"><rect class="basic label-container" style="" x="-130" y="-39" width="260" height="78"></rect><g class="label" style="" transform="translate(-100, -24)"><rect></rect><foreignObject width="200" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table;white-space:break-spaces;line-height:1.5;max-width:200px;text-align:center;width:200px"><span class="nodeLabel"><p>Search the web for information</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-R-13" transform="translate(550.5, 715.65625)"><rect class="basic label-container" style="" x="-92.6171875" y="-27" width="185.234375" height="54"></rect><g class="label" style="" transform="translate(-62.6171875, -12)"><rect></rect><foreignObject width="125.234375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Search result</p></span></div></foreignObject></g></g></g></g></g></svg></p>
<p>Web search gave live knowledge. Now the model could answer fresh questions.</p>
<h2 id="even-more-tools">Even more tools<a class="heading-link" aria-label="Link to section" href="#even-more-tools"><span class="heading-link-icon">#</span></a></h2>
<p><svg id="mermaid-3" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="flowchart" style="max-width:981.1171875px" viewBox="0 0 981.1171875 750.65625" role="graphics-document document" aria-roledescription="flowchart-v2"><style>#mermaid-3{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-3 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-3 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-3 .error-icon{fill:#a44141;}#mermaid-3 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-3 .edge-thickness-normal{stroke-width:1px;}#mermaid-3 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-3 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-3 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-3 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-3 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-3 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-3 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-3 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-3 p{margin:0;}#mermaid-3 .label{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;color:#ccc;}#mermaid-3 .cluster-label text{fill:#F9FFFE;}#mermaid-3 .cluster-label span{color:#F9FFFE;}#mermaid-3 .cluster-label span p{background-color:transparent;}#mermaid-3 .label text,#mermaid-3 span{fill:#ccc;color:#ccc;}#mermaid-3 .node rect,#mermaid-3 .node circle,#mermaid-3 .node ellipse,#mermaid-3 .node polygon,#mermaid-3 .node path{fill:transparent;stroke:2px;stroke-width:1px;}#mermaid-3 .rough-node .label text,#mermaid-3 .node .label text,#mermaid-3 .image-shape .label,#mermaid-3 .icon-shape .label{text-anchor:middle;}#mermaid-3 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-3 .rough-node .label,#mermaid-3 .node .label,#mermaid-3 .image-shape .label,#mermaid-3 .icon-shape .label{text-align:center;}#mermaid-3 .node.clickable{cursor:pointer;}#mermaid-3 .root .anchor path{fill:rgb(171, 75, 153)!important;stroke-width:0;stroke:rgb(171, 75, 153);}#mermaid-3 .arrowheadPath{fill:lightgrey;}#mermaid-3 .edgePath .path{stroke:rgb(171, 75, 153);stroke-width:2.0px;}#mermaid-3 .flowchart-link{stroke:rgb(171, 75, 153);fill:none;}#mermaid-3 .edgeLabel{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-3 .edgeLabel p{background-color:hsla(0, 0%, 25%, 0);}#mermaid-3 .edgeLabel rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-3 .labelBkg{background-color:rgba(63.75, 63.75, 63.75, 0.5);}#mermaid-3 .cluster rect{fill:transparent;stroke:rgba(255, 255, 255, 0.25);stroke-width:1px;}#mermaid-3 .cluster text{fill:#F9FFFE;}#mermaid-3 .cluster span{color:#F9FFFE;}#mermaid-3 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:12px;background:rgb(138, 51, 123);border:1px solid rgba(255, 255, 255, 0.25);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-3 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-3 rect.text{fill:none;stroke-width:0;}#mermaid-3 .icon-shape,#mermaid-3 .image-shape{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-3 .icon-shape p,#mermaid-3 .image-shape p{background-color:hsla(0, 0%, 25%, 0);padding:2px;}#mermaid-3 .icon-shape rect,#mermaid-3 .image-shape rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-3 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-3 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-3 :root{--mermaid-font-family:arial,sans-serif;}</style><g><marker id="mermaid-3_flowchart-v2-pointEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-3_flowchart-v2-pointStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="4.5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 5 L 10 10 L 10 0 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-3_flowchart-v2-circleEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="11" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-3_flowchart-v2-circleStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="-1" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-3_flowchart-v2-crossEnd" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="12" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-3_flowchart-v2-crossStart" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="-1" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><g class="root"><g class="clusters"></g><g class="edgePaths"><path d="M477.624,62L476.823,66.167C476.022,70.333,474.419,78.667,474.293,86.345C474.167,94.024,475.518,101.048,476.193,104.56L476.869,108.072" id="L_U_A_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_U_A_0" data-points="W3sieCI6NDc3LjYyNDA5ODU1NzY5MjMsInkiOjYyfSx7IngiOjQ3Mi44MTY0MDYyNSwieSI6ODd9LHsieCI6NDc3LjYyNDA5ODU1NzY5MjMsInkiOjExMn1d" marker-end="url(#mermaid-3_flowchart-v2-pointEnd)"></path><path d="M445.98,166L437.566,172.167C429.153,178.333,412.327,190.667,409.321,208.793C406.316,226.919,417.133,250.839,422.541,262.799L427.949,274.758" id="L_A_D_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_A_D_0" data-points="W3sieCI6NDQ1Ljk3OTc5NzM2MzI4MTI1LCJ5IjoxNjZ9LHsieCI6Mzk1LjUsInkiOjIwM30seyJ4Ijo0MjkuNTk3MDQwNDY3MDgyNzYsInkiOjI3OC40MDI5NTk1MzI5MTcyNH1d" marker-end="url(#mermaid-3_flowchart-v2-pointEnd)"></path><path d="M384.998,403.654L343.832,423.654C302.665,443.655,220.333,483.656,179.166,509.156C138,534.656,138,545.656,138,551.156L138,556.656" id="L_D_P_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_D_P_0" data-points="W3sieCI6Mzg0Ljk5Nzg2NDk1MDEyOTA0LCJ5Ijo0MDMuNjU0MTE0OTUwMTI5MDR9LHsieCI6MTM4LCJ5Ijo1MjMuNjU2MjV9LHsieCI6MTM4LCJ5Ijo1NjAuNjU2MjV9XQ==" marker-end="url(#mermaid-3_flowchart-v2-pointEnd)"></path><path d="M138,638.656L138,642.823C138,646.99,138,655.323,144.047,663.301C150.093,671.279,162.186,678.901,168.233,682.712L174.28,686.523" id="L_P_O_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_P_O_0" data-points="W3sieCI6MTM4LCJ5Ijo2MzguNjU2MjV9LHsieCI6MTM4LCJ5Ijo2NjMuNjU2MjV9LHsieCI6MTc3LjY2MzQ2MTUzODQ2MTU1LCJ5Ijo2ODguNjU2MjV9XQ==" marker-end="url(#mermaid-3_flowchart-v2-pointEnd)"></path><path d="M263.337,688.656L269.947,684.49C276.558,680.323,289.779,671.99,296.389,657.156C303,642.323,303,620.99,303,597.656C303,574.323,303,548.99,303,509.602C303,470.214,303,416.771,303,363.328C303,309.885,303,256.443,324.932,221.915C346.865,187.388,390.73,171.775,412.662,163.969L434.595,156.163" id="L_O_A_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_O_A_0" data-points="W3sieCI6MjYzLjMzNjUzODQ2MTUzODQ1LCJ5Ijo2ODguNjU2MjV9LHsieCI6MzAzLCJ5Ijo2NjMuNjU2MjV9LHsieCI6MzAzLCJ5Ijo1OTkuNjU2MjV9LHsieCI6MzAzLCJ5Ijo1MjMuNjU2MjV9LHsieCI6MzAzLCJ5IjozNjMuMzI4MTI1fSx7IngiOjMwMywieSI6MjAzfSx7IngiOjQzOC4zNjMyODEyNSwieSI6MTU0LjgyMTY5MzEzMzE4NzA3fV0=" marker-end="url(#mermaid-3_flowchart-v2-pointEnd)"></path><path d="M468,486.656L468,492.823C468,498.99,468,511.323,468,522.99C468,534.656,468,545.656,468,551.156L468,556.656" id="L_D_W_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_D_W_0" data-points="W3sieCI6NDY4LCJ5Ijo0ODYuNjU2MjV9LHsieCI6NDY4LCJ5Ijo1MjMuNjU2MjV9LHsieCI6NDY4LCJ5Ijo1NjAuNjU2MjV9XQ==" marker-end="url(#mermaid-3_flowchart-v2-pointEnd)"></path><path d="M468,638.656L468,642.823C468,646.99,468,655.323,474.047,663.301C480.093,671.279,492.186,678.901,498.233,682.712L504.28,686.523" id="L_W_R_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_W_R_0" data-points="W3sieCI6NDY4LCJ5Ijo2MzguNjU2MjV9LHsieCI6NDY4LCJ5Ijo2NjMuNjU2MjV9LHsieCI6NTA3LjY2MzQ2MTUzODQ2MTU1LCJ5Ijo2ODguNjU2MjV9XQ==" marker-end="url(#mermaid-3_flowchart-v2-pointEnd)"></path><path d="M593.337,688.656L599.947,684.49C606.558,680.323,619.779,671.99,626.389,657.156C633,642.323,633,620.99,633,597.656C633,574.323,633,548.99,633,509.602C633,470.214,633,416.771,633,363.328C633,309.885,633,256.443,615.992,222.473C598.983,188.504,564.966,174.008,547.958,166.76L530.949,159.512" id="L_R_A_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_R_A_0" data-points="W3sieCI6NTkzLjMzNjUzODQ2MTUzODUsInkiOjY4OC42NTYyNX0seyJ4Ijo2MzMsInkiOjY2My42NTYyNX0seyJ4Ijo2MzMsInkiOjU5OS42NTYyNX0seyJ4Ijo2MzMsInkiOjUyMy42NTYyNX0seyJ4Ijo2MzMsInkiOjM2My4zMjgxMjV9LHsieCI6NjMzLCJ5IjoyMDN9LHsieCI6NTI3LjI2OTUzMTI1LCJ5IjoxNTcuOTQzNDgwNjM1NjgwM31d" marker-end="url(#mermaid-3_flowchart-v2-pointEnd)"></path><path d="M551.002,403.654L592.168,423.654C633.335,443.655,715.667,483.656,756.834,509.156C798,534.656,798,545.656,798,551.156L798,556.656" id="L_D_G_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_D_G_0" data-points="W3sieCI6NTUxLjAwMjEzNTA0OTg3MSwieSI6NDAzLjY1NDExNDk1MDEyOTA0fSx7IngiOjc5OCwieSI6NTIzLjY1NjI1fSx7IngiOjc5OCwieSI6NTYwLjY1NjI1fV0=" marker-end="url(#mermaid-3_flowchart-v2-pointEnd)"></path><path d="M798,638.656L798,642.823C798,646.99,798,655.323,804.047,663.301C810.093,671.279,822.186,678.901,828.233,682.712L834.28,686.523" id="L_G_E_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_G_E_0" data-points="W3sieCI6Nzk4LCJ5Ijo2MzguNjU2MjV9LHsieCI6Nzk4LCJ5Ijo2NjMuNjU2MjV9LHsieCI6ODM3LjY2MzQ2MTUzODQ2MTUsInkiOjY4OC42NTYyNX1d" marker-end="url(#mermaid-3_flowchart-v2-pointEnd)"></path><path d="M923.337,688.656L929.947,684.49C936.558,680.323,949.779,671.99,956.389,657.156C963,642.323,963,620.99,963,597.656C963,574.323,963,548.99,963,509.602C963,470.214,963,416.771,963,363.328C963,309.885,963,256.443,891.039,220.13C819.078,183.818,675.156,164.636,603.195,155.044L531.234,145.453" id="L_E_A_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_E_A_0" data-points="W3sieCI6OTIzLjMzNjUzODQ2MTUzODUsInkiOjY4OC42NTYyNX0seyJ4Ijo5NjMsInkiOjY2My42NTYyNX0seyJ4Ijo5NjMsInkiOjU5OS42NTYyNX0seyJ4Ijo5NjMsInkiOjUyMy42NTYyNX0seyJ4Ijo5NjMsInkiOjM2My4zMjgxMjV9LHsieCI6OTYzLCJ5IjoyMDN9LHsieCI6NTI3LjI2OTUzMTI1LCJ5IjoxNDQuOTI0ODE3MTY3OTEyNjZ9XQ==" marker-end="url(#mermaid-3_flowchart-v2-pointEnd)"></path><path d="M478.433,250.433L479.164,242.527C479.894,234.622,481.355,218.811,482.086,205.405C482.816,192,482.816,181,482.816,175.5L482.816,170" id="L_D_A_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_D_A_0" data-points="W3sieCI6NDc4LjQzMjk4MTIwMTM1MTU0LCJ5IjoyNTAuNDMyOTgxMjAxMzUxNTd9LHsieCI6NDgyLjgxNjQwNjI1LCJ5IjoyMDN9LHsieCI6NDgyLjgxNjQwNjI1LCJ5IjoxNjZ9XQ==" marker-end="url(#mermaid-3_flowchart-v2-pointEnd)"></path><path d="M488.009,112L488.81,107.833C489.611,103.667,491.214,95.333,491.34,87.655C491.466,79.976,490.115,72.952,489.439,69.44L488.764,65.928" id="L_A_U_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_A_U_0" data-points="W3sieCI6NDg4LjAwODcxMzk0MjMwNzcsInkiOjExMn0seyJ4Ijo0OTIuODE2NDA2MjUsInkiOjg3fSx7IngiOjQ4OC4wMDg3MTM5NDIzMDc3LCJ5Ijo2Mn1d" marker-end="url(#mermaid-3_flowchart-v2-pointEnd)"></path></g><g class="edgeLabels"><g class="edgeLabel"><g class="label" data-id="L_U_A_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_A_D_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(138, 523.65625)"><g class="label" data-id="L_D_P_0" transform="translate(-28.8984375, -12)"><foreignObject width="57.796875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>Python</p></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_P_O_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_O_A_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(468, 523.65625)"><g class="label" data-id="L_D_W_0" transform="translate(-48.1640625, -12)"><foreignObject width="96.328125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>Web search</p></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_W_R_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_R_A_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(798, 523.65625)"><g class="label" data-id="L_D_G_0" transform="translate(-72.25, -12)"><foreignObject width="144.5" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>Google Calendar</p></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_G_E_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_E_A_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(482.81640625, 203)"><g class="label" data-id="L_D_A_0" transform="translate(-9.6328125, -12)"><foreignObject width="19.265625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>No</p></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_A_U_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g></g><g class="nodes"><g class="node default" id="flowchart-U-0" transform="translate(482.81640625, 35)"><rect class="basic label-container" style="" x="-49.265625" y="-27" width="98.53125" height="54"></rect><g class="label" style="" transform="translate(-19.265625, -12)"><rect></rect><foreignObject width="38.53125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>User</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-A-1" transform="translate(482.81640625, 139)"><rect class="basic label-container" style="" x="-44.453125" y="-27" width="88.90625" height="54"></rect><g class="label" style="" transform="translate(-14.453125, -12)"><rect></rect><foreignObject width="28.90625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>LLM</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-D-3" transform="translate(468, 363.328125)"><polygon points="123.328125,0 246.65625,-123.328125 123.328125,-246.65625 0,-123.328125" class="label-container" transform="translate(-122.828125, 123.328125)"></polygon><g class="label" style="" transform="translate(-96.328125, -12)"><rect></rect><foreignObject width="192.65625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Needs external tool?</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-P-5" transform="translate(138, 599.65625)"><rect class="basic label-container" style="" x="-130" y="-39" width="260" height="78"></rect><g class="label" style="" transform="translate(-100, -24)"><rect></rect><foreignObject width="200" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table;white-space:break-spaces;line-height:1.5;max-width:200px;text-align:center;width:200px"><span class="nodeLabel"><p>Run code in Python sandbox</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-O-7" transform="translate(220.5, 715.65625)"><rect class="basic label-container" style="" x="-107.0625" y="-27" width="214.125" height="54"></rect><g class="label" style="" transform="translate(-77.0625, -12)"><rect></rect><foreignObject width="154.125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Execution result</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-W-11" transform="translate(468, 599.65625)"><rect class="basic label-container" style="" x="-130" y="-39" width="260" height="78"></rect><g class="label" style="" transform="translate(-100, -24)"><rect></rect><foreignObject width="200" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table;white-space:break-spaces;line-height:1.5;max-width:200px;text-align:center;width:200px"><span class="nodeLabel"><p>Search the web for information</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-R-13" transform="translate(550.5, 715.65625)"><rect class="basic label-container" style="" x="-92.6171875" y="-27" width="185.234375" height="54"></rect><g class="label" style="" transform="translate(-62.6171875, -12)"><rect></rect><foreignObject width="125.234375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Search result</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-G-17" transform="translate(798, 599.65625)"><rect class="basic label-container" style="" x="-130" y="-39" width="260" height="78"></rect><g class="label" style="" transform="translate(-100, -24)"><rect></rect><foreignObject width="200" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table;white-space:break-spaces;line-height:1.5;max-width:200px;text-align:center;width:200px"><span class="nodeLabel"><p>Check / update calendar events</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-E-19" transform="translate(880.5, 715.65625)"><rect class="basic label-container" style="" x="-92.6171875" y="-27" width="185.234375" height="54"></rect><g class="label" style="" transform="translate(-62.6171875, -12)"><rect></rect><foreignObject width="125.234375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Calendar data</p></span></div></foreignObject></g></g></g></g></g></svg></p>
<p>Anthropic added more tools to Claude like Google Calendar and email.
You can ask it what meetings you have next week and it tells you.</p>
<figure class="captioned-image astro-t2d64o5a"> <img src="/_astro/mcp-scaling-problem-comic.BGUyHRMd_Z17GJMd.webp" alt="Comic showing multiple teams reinventing the wheel by building the same API connectors" loading="lazy" decoding="async" fetchpriority="auto" width="1536" height="1024" class="astro-t2d64o5a"> <figcaption class="astro-t2d64o5a">If every team builds their own tool for connecting to email, calendar, and other APIs, everyone reinvents the wheel</figcaption> </figure> 
<h2 id="the-solution-a-protocol">The solution: a protocol<a class="heading-link" aria-label="Link to section" href="#the-solution-a-protocol"><span class="heading-link-icon">#</span></a></h2>
<p>We need a standard.
One tool for Google Calendar that any agent can use.
In November the Model Context Protocol was released.</p>
<h2 id="definition">Definition<a class="heading-link" aria-label="Link to section" href="#definition"><span class="heading-link-icon">#</span></a></h2>
<p><strong>MCP</strong> is an open protocol that lets apps give context to LLMs in a standard way.</p>
<p>Think of <strong>USB-C</strong>. You plug in power, a display, or storage and it just works.</p>
<p>MCP does the same for AI with data sources and tools.</p>
<p>With MCP you can build agents and workflows without custom glue code.</p>
<figure class="captioned-image astro-t2d64o5a"> <img src="/_astro/comic-mcp-robot.9WGWKium_Z1tTPA5.webp" alt="Robot MCP Comic showing how MCP connects different tools and services" loading="lazy" decoding="async" fetchpriority="auto" width="1536" height="1024" class="astro-t2d64o5a"> <figcaption class="astro-t2d64o5a">MCP acts as the universal connector for AI tools and services</figcaption> </figure> 
<hr/>
<h2 id="how-mcp-works-mental-model">How MCP Works (mental model)<a class="heading-link" aria-label="Link to section" href="#how-mcp-works-mental-model"><span class="heading-link-icon">#</span></a></h2>
<p>At its core, MCP has <strong>three roles</strong>:</p>
<ul>
<li><strong>Host</strong> → LLM applications that initiate connections</li>
<li><strong>Client</strong> → Connectors within the host application</li>
<li><strong>Server</strong> → Services that provide context and capabilities</li>
</ul>
<div class="alert alert-note astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">💡</span> Note </p> <div class="alert-content astro-7kdbuayl"> <p>MCP takes some inspiration from the Language Server Protocol, which
standardizes how to add support for programming languages across a whole
ecosystem of development tools. In a similar way, MCP standardizes how to
integrate additional context and tools into the ecosystem of AI applications.</p> </div> </div> 
<p>The host embeds clients, and those clients connect to one or more servers.
Your VS Code could have a Playwright MCP server for browser automation and another MCP server for your docs — all running at the same time.</p>
<p><svg id="mermaid-4" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="flowchart" style="max-width:830.71875px" viewBox="0 0 830.71875 278" role="graphics-document document" aria-roledescription="flowchart-v2"><style>#mermaid-4{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-4 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-4 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-4 .error-icon{fill:#a44141;}#mermaid-4 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-4 .edge-thickness-normal{stroke-width:1px;}#mermaid-4 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-4 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-4 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-4 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-4 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-4 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-4 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-4 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-4 p{margin:0;}#mermaid-4 .label{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;color:#ccc;}#mermaid-4 .cluster-label text{fill:#F9FFFE;}#mermaid-4 .cluster-label span{color:#F9FFFE;}#mermaid-4 .cluster-label span p{background-color:transparent;}#mermaid-4 .label text,#mermaid-4 span{fill:#ccc;color:#ccc;}#mermaid-4 .node rect,#mermaid-4 .node circle,#mermaid-4 .node ellipse,#mermaid-4 .node polygon,#mermaid-4 .node path{fill:transparent;stroke:2px;stroke-width:1px;}#mermaid-4 .rough-node .label text,#mermaid-4 .node .label text,#mermaid-4 .image-shape .label,#mermaid-4 .icon-shape .label{text-anchor:middle;}#mermaid-4 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-4 .rough-node .label,#mermaid-4 .node .label,#mermaid-4 .image-shape .label,#mermaid-4 .icon-shape .label{text-align:center;}#mermaid-4 .node.clickable{cursor:pointer;}#mermaid-4 .root .anchor path{fill:rgb(171, 75, 153)!important;stroke-width:0;stroke:rgb(171, 75, 153);}#mermaid-4 .arrowheadPath{fill:lightgrey;}#mermaid-4 .edgePath .path{stroke:rgb(171, 75, 153);stroke-width:2.0px;}#mermaid-4 .flowchart-link{stroke:rgb(171, 75, 153);fill:none;}#mermaid-4 .edgeLabel{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-4 .edgeLabel p{background-color:hsla(0, 0%, 25%, 0);}#mermaid-4 .edgeLabel rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-4 .labelBkg{background-color:rgba(63.75, 63.75, 63.75, 0.5);}#mermaid-4 .cluster rect{fill:transparent;stroke:rgba(255, 255, 255, 0.25);stroke-width:1px;}#mermaid-4 .cluster text{fill:#F9FFFE;}#mermaid-4 .cluster span{color:#F9FFFE;}#mermaid-4 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:12px;background:rgb(138, 51, 123);border:1px solid rgba(255, 255, 255, 0.25);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-4 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-4 rect.text{fill:none;stroke-width:0;}#mermaid-4 .icon-shape,#mermaid-4 .image-shape{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-4 .icon-shape p,#mermaid-4 .image-shape p{background-color:hsla(0, 0%, 25%, 0);padding:2px;}#mermaid-4 .icon-shape rect,#mermaid-4 .image-shape rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-4 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-4 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-4 :root{--mermaid-font-family:arial,sans-serif;}</style><g><marker id="mermaid-4_flowchart-v2-pointEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-4_flowchart-v2-pointStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="4.5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 5 L 10 10 L 10 0 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-4_flowchart-v2-circleEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="11" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-4_flowchart-v2-circleStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="-1" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-4_flowchart-v2-crossEnd" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="12" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-4_flowchart-v2-crossStart" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="-1" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><g class="root"><g class="clusters"></g><g class="edgePaths"><path d="M61.531,139L65.698,139C69.865,139,78.198,139,85.865,139C93.531,139,100.531,139,104.031,139L107.531,139" id="L_U_H_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_U_H_0" data-points="W3sieCI6NjEuNTMxMjUsInkiOjEzOX0seyJ4Ijo4Ni41MzEyNSwieSI6MTM5fSx7IngiOjExMS41MzEyNSwieSI6MTM5fV0=" marker-end="url(#mermaid-4_flowchart-v2-pointEnd)"></path><path d="M317.541,88L330.706,79.167C343.871,70.333,370.201,52.667,386.866,43.833C403.531,35,410.531,35,414.031,35L417.531,35" id="L_H_C1_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_H_C1_0" data-points="W3sieCI6MzE3LjU0MDg2NTM4NDYxNTM2LCJ5Ijo4OH0seyJ4IjozOTYuNTMxMjUsInkiOjM1fSx7IngiOjQyMS41MzEyNSwieSI6MzV9XQ==" marker-end="url(#mermaid-4_flowchart-v2-pointEnd)"></path><path d="M371.531,139L375.698,139C379.865,139,388.198,139,395.865,139C403.531,139,410.531,139,414.031,139L417.531,139" id="L_H_C2_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_H_C2_0" data-points="W3sieCI6MzcxLjUzMTI1LCJ5IjoxMzl9LHsieCI6Mzk2LjUzMTI1LCJ5IjoxMzl9LHsieCI6NDIxLjUzMTI1LCJ5IjoxMzl9XQ==" marker-end="url(#mermaid-4_flowchart-v2-pointEnd)"></path><path d="M317.541,190L330.706,198.833C343.871,207.667,370.201,225.333,386.866,234.167C403.531,243,410.531,243,414.031,243L417.531,243" id="L_H_C3_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_H_C3_0" data-points="W3sieCI6MzE3LjU0MDg2NTM4NDYxNTM2LCJ5IjoxOTB9LHsieCI6Mzk2LjUzMTI1LCJ5IjoyNDN9LHsieCI6NDIxLjUzMTI1LCJ5IjoyNDN9XQ==" marker-end="url(#mermaid-4_flowchart-v2-pointEnd)"></path><path d="M597.125,35L601.292,35C605.458,35,613.792,35,621.458,35C629.125,35,636.125,35,639.625,35L643.125,35" id="L_C1_S1_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_C1_S1_0" data-points="W3sieCI6NTk3LjEyNSwieSI6MzV9LHsieCI6NjIyLjEyNSwieSI6MzV9LHsieCI6NjQ3LjEyNSwieSI6MzV9XQ==" marker-end="url(#mermaid-4_flowchart-v2-pointEnd)"></path><path d="M597.125,139L601.292,139C605.458,139,613.792,139,621.458,139C629.125,139,636.125,139,639.625,139L643.125,139" id="L_C2_S2_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_C2_S2_0" data-points="W3sieCI6NTk3LjEyNSwieSI6MTM5fSx7IngiOjYyMi4xMjUsInkiOjEzOX0seyJ4Ijo2NDcuMTI1LCJ5IjoxMzl9XQ==" marker-end="url(#mermaid-4_flowchart-v2-pointEnd)"></path><path d="M597.125,243L601.292,243C605.458,243,613.792,243,621.458,243C629.125,243,636.125,243,639.625,243L643.125,243" id="L_C3_S3_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_C3_S3_0" data-points="W3sieCI6NTk3LjEyNSwieSI6MjQzfSx7IngiOjYyMi4xMjUsInkiOjI0M30seyJ4Ijo2NDcuMTI1LCJ5IjoyNDN9XQ==" marker-end="url(#mermaid-4_flowchart-v2-pointEnd)"></path></g><g class="edgeLabels"><g class="edgeLabel"><g class="label" data-id="L_U_H_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_H_C1_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_H_C2_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_H_C3_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_C1_S1_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_C2_S2_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_C3_S3_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g></g><g class="nodes"><g class="node default" id="flowchart-U-0" transform="translate(34.765625, 139)"><circle class="basic label-container" style="" r="26.765625" cx="0" cy="0"></circle><g class="label" style="" transform="translate(-19.265625, -12)"><rect></rect><foreignObject width="38.53125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>User</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-H-2" transform="translate(241.53125, 139)"><rect class="basic label-container" style="" x="-130" y="-51" width="260" height="102"></rect><g class="label" style="" transform="translate(-100, -36)"><rect></rect><foreignObject width="200" height="72"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table;white-space:break-spaces;line-height:1.5;max-width:200px;text-align:center;width:200px"><span class="nodeLabel"><p>Host UI<br/>Claude Desktop, VS Code/Claude Code</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-C1-4" transform="translate(509.328125, 35)"><rect class="basic label-container" style="" x="-87.796875" y="-27" width="175.59375" height="54"></rect><g class="label" style="" transform="translate(-57.796875, -12)"><rect></rect><foreignObject width="115.59375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>MCP Client 1</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-C2-6" transform="translate(509.328125, 139)"><rect class="basic label-container" style="" x="-87.796875" y="-27" width="175.59375" height="54"></rect><g class="label" style="" transform="translate(-57.796875, -12)"><rect></rect><foreignObject width="115.59375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>MCP Client 2</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-C3-8" transform="translate(509.328125, 243)"><rect class="basic label-container" style="" x="-87.796875" y="-27" width="175.59375" height="54"></rect><g class="label" style="" transform="translate(-57.796875, -12)"><rect></rect><foreignObject width="115.59375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>MCP Client 3</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-S1-10" transform="translate(734.921875, 35)"><rect class="basic label-container" style="" x="-87.796875" y="-27" width="175.59375" height="54"></rect><g class="label" style="" transform="translate(-57.796875, -12)"><rect></rect><foreignObject width="115.59375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>MCP Server A</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-S2-12" transform="translate(734.921875, 139)"><rect class="basic label-container" style="" x="-87.796875" y="-27" width="175.59375" height="54"></rect><g class="label" style="" transform="translate(-57.796875, -12)"><rect></rect><foreignObject width="115.59375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>MCP Server B</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-S3-14" transform="translate(734.921875, 243)"><rect class="basic label-container" style="" x="-87.796875" y="-27" width="175.59375" height="54"></rect><g class="label" style="" transform="translate(-57.796875, -12)"><rect></rect><foreignObject width="115.59375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>MCP Server C</p></span></div></foreignObject></g></g></g></g></g></svg></p>
<hr/>
<h2 id="how-mcp-connects-transports">How MCP Connects: Transports<a class="heading-link" aria-label="Link to section" href="#how-mcp-connects-transports"><span class="heading-link-icon">#</span></a></h2>
<p>MCP uses <strong>JSON-RPC 2.0</strong> for all messages and supports two main transport mechanisms:</p>
<div class="grid-cards-container astro-g5e4s2ea"> <div class="grid-card astro-g5e4s2ea"> <h3 class="grid-card-title astro-g5e4s2ea"> <span class="grid-card-icon astro-g5e4s2ea">📍</span> stdio (local) </h3> <ul class="grid-card-list astro-g5e4s2ea"> <li class="astro-g5e4s2ea">Server runs as subprocess of the client</li><li class="astro-g5e4s2ea">Messages flow through stdin/stdout pipes</li><li class="astro-g5e4s2ea">No network latency - instant communication</li><li class="astro-g5e4s2ea">Perfect for local tools and dev environments</li> </ul> </div><div class="grid-card astro-g5e4s2ea"> <h3 class="grid-card-title astro-g5e4s2ea"> <span class="grid-card-icon astro-g5e4s2ea">🌐</span> Streamable HTTP (remote) </h3> <ul class="grid-card-list astro-g5e4s2ea"> <li class="astro-g5e4s2ea">Single HTTP endpoint for all operations</li><li class="astro-g5e4s2ea">POST for sending messages, GET for listening</li><li class="astro-g5e4s2ea">Server-Sent Events (SSE) for streaming</li><li class="astro-g5e4s2ea">Ideal for cloud-hosted MCP servers</li> </ul> </div> </div> 
<p><strong>Key points:</strong></p>
<ul>
<li>Messages are UTF-8 encoded JSON-RPC</li>
<li>stdio uses newline-delimited JSON (one message per line)</li>
<li>HTTP supports session management via <code>Mcp-Session-Id</code> headers</li>
<li>Both transports handle requests, responses, and notifications equally well</li>
</ul>
<p>The transport choice depends on your use case: stdio for local tools with minimal latency, HTTP for remote services that multiple clients can connect to.</p>
<h2 id="what-servers-can-expose">What servers can expose<a class="heading-link" aria-label="Link to section" href="#what-servers-can-expose"><span class="heading-link-icon">#</span></a></h2>
<p>An MCP server can offer any combination of three capabilities:</p>
<h3 id="tools-functions-the-ai-can-call">Tools: Functions the AI can call<a class="heading-link" aria-label="Link to section" href="#tools-functions-the-ai-can-call"><span class="heading-link-icon">#</span></a></h3>
<ul>
<li>Give AI ability to execute actions (check weather, query databases, solve math)</li>
<li>Each tool describes what it does and what info it needs</li>
<li>AI sends parameters → server runs function → returns results</li>
</ul>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// Simple calculator tool example</span></span>
<span class="line"><span style="color:#C0CAF5">server</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">registerTool</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#9ECE6A">calculate</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  {</span></span>
<span class="line"><span style="color:#73DACA">    title</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">Calculator</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    description</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">Perform mathematical calculations</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    inputSchema</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">      operation</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> z</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">enum</span><span style="color:#9ABDF5">([</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">add</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">subtract</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">multiply</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">divide</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">])</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">      a</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> z</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">number</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">      b</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> z</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">number</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  async</span><span style="color:#9ABDF5"> (</span><span style="color:#89DDFF">{</span><span style="color:#E0AF68"> operation</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> a</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> b</span><span style="color:#89DDFF"> }</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    let</span><span style="color:#BB9AF7"> result</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">    switch</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">operation</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7">      case</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">add</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#C0CAF5">        result</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> a</span><span style="color:#89DDFF"> +</span><span style="color:#C0CAF5"> b</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">        break</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">      case</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">subtract</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#C0CAF5">        result</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> a</span><span style="color:#89DDFF"> -</span><span style="color:#C0CAF5"> b</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">        break</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">      case</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">multiply</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#C0CAF5">        result</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> a</span><span style="color:#89DDFF"> *</span><span style="color:#C0CAF5"> b</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">        break</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">      case</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">divide</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#C0CAF5">        result</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> b</span><span style="color:#BB9AF7"> !==</span><span style="color:#FF9E64"> 0</span><span style="color:#BB9AF7"> ?</span><span style="color:#C0CAF5"> a</span><span style="color:#89DDFF"> /</span><span style="color:#C0CAF5"> b</span><span style="color:#BB9AF7"> :</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">Error: Division by zero</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">        break</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">      content</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span></span>
<span class="line"><span style="color:#9ABDF5">        {</span></span>
<span class="line"><span style="color:#73DACA">          type</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">text</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">          text</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> `</span><span style="color:#7DCFFF">${</span><span style="color:#7DCFFF">a</span><span style="color:#7DCFFF">}</span><span style="color:#7DCFFF"> ${</span><span style="color:#7DCFFF">operation</span><span style="color:#7DCFFF">}</span><span style="color:#7DCFFF"> ${</span><span style="color:#7DCFFF">b</span><span style="color:#7DCFFF">}</span><span style="color:#9ECE6A"> = </span><span style="color:#7DCFFF">${</span><span style="color:#7DCFFF">result</span><span style="color:#7DCFFF">}</span><span style="color:#89DDFF">`</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">        }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">      ]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="// Simple calculator tool example
server.registerTool(
  &#34;calculate&#34;,
  {
    title: &#34;Calculator&#34;,
    description: &#34;Perform mathematical calculations&#34;,
    inputSchema: {
      operation: z.enum([&#34;add&#34;, &#34;subtract&#34;, &#34;multiply&#34;, &#34;divide&#34;]),
      a: z.number(),
      b: z.number(),
    },
  },
  async ({ operation, a, b }) => {
    let result;
    switch (operation) {
      case &#34;add&#34;:
        result = a + b;
        break;
      case &#34;subtract&#34;:
        result = a - b;
        break;
      case &#34;multiply&#34;:
        result = a * b;
        break;
      case &#34;divide&#34;:
        result = b !== 0 ? a / b : &#34;Error: Division by zero&#34;;
        break;
    }

    return {
      content: [
        {
          type: &#34;text&#34;,
          text: `${a} ${operation} ${b} = ${result}`,
        },
      ],
    };
  }
);" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="resources-context-and-data">Resources: Context and data<a class="heading-link" aria-label="Link to section" href="#resources-context-and-data"><span class="heading-link-icon">#</span></a></h3>
<ul>
<li>AI can read files, docs, database schemas</li>
<li>Provides context before answering questions or using tools</li>
<li>Supports change notifications when files update</li>
</ul>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#C0CAF5">server</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">registerResource</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#9ECE6A">app-config</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#9ECE6A">config://application</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  {</span></span>
<span class="line"><span style="color:#73DACA">    title</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">Application Configuration</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    description</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">Current app settings and environment</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    mimeType</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">application/json</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  async</span><span style="color:#E0AF68"> uri</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> ({</span></span>
<span class="line"><span style="color:#73DACA">    contents</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span></span>
<span class="line"><span style="color:#9ABDF5">      {</span></span>
<span class="line"><span style="color:#73DACA">        uri</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> uri</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">href</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">        text</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> JSON</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">stringify</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#9ABDF5">          {</span></span>
<span class="line"><span style="color:#41A6B5">            environment</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> process</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">env</span><span style="color:#89DDFF">.</span><span style="color:#FF9E64">NODE_ENV</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">            version</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">1.0.0</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">            features</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#41A6B5">              darkMode</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">              analytics</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> false</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">              beta</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> process</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">env</span><span style="color:#89DDFF">.</span><span style="color:#FF9E64">BETA</span><span style="color:#BB9AF7"> ===</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">true</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">            }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">          }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#FF9E64">          null</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#FF9E64">          2</span></span>
<span class="line"><span style="color:#9ABDF5">        )</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    ]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span></span>
<span class="line"><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="server.registerResource(
  &#34;app-config&#34;,
  &#34;config://application&#34;,
  {
    title: &#34;Application Configuration&#34;,
    description: &#34;Current app settings and environment&#34;,
    mimeType: &#34;application/json&#34;,
  },
  async uri => ({
    contents: [
      {
        uri: uri.href,
        text: JSON.stringify(
          {
            environment: process.env.NODE_ENV,
            version: &#34;1.0.0&#34;,
            features: {
              darkMode: true,
              analytics: false,
              beta: process.env.BETA === &#34;true&#34;,
            },
          },
          null,
          2
        ),
      },
    ],
  })
);" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="prompts-templates-for-interaction">Prompts: Templates for interaction<a class="heading-link" aria-label="Link to section" href="#prompts-templates-for-interaction"><span class="heading-link-icon">#</span></a></h3>
<ul>
<li>Pre-made templates for common tasks (code review, data analysis)</li>
<li>Exposed as slash commands or UI elements</li>
<li>Makes repetitive workflows quick and consistent</li>
</ul>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#C0CAF5">server</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">registerPrompt</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#9ECE6A">code-review</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  {</span></span>
<span class="line"><span style="color:#73DACA">    title</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">Code Review</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    description</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">Review code for quality and best practices</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    argsSchema</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">      language</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> z</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">enum</span><span style="color:#9ABDF5">([</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">javascript</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">typescript</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">python</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">go</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">])</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">      code</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> z</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">string</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">      focus</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> z</span></span>
<span class="line"><span style="color:#89DDFF">        .</span><span style="color:#7AA2F7">enum</span><span style="color:#9ABDF5">([</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">security</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">performance</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">readability</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">all</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">])</span></span>
<span class="line"><span style="color:#89DDFF">        .</span><span style="color:#7AA2F7">default</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">all</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  (</span><span style="color:#89DDFF">{</span><span style="color:#E0AF68"> language</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> code</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> focus</span><span style="color:#89DDFF"> }</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> ({</span></span>
<span class="line"><span style="color:#73DACA">    messages</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span></span>
<span class="line"><span style="color:#9ABDF5">      {</span></span>
<span class="line"><span style="color:#73DACA">        role</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">user</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">        content</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#41A6B5">          type</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">text</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">          text</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span></span>
<span class="line"><span style="color:#89DDFF">            `</span><span style="color:#9ECE6A">Please review this </span><span style="color:#7DCFFF">${</span><span style="color:#7DCFFF">language</span><span style="color:#7DCFFF">}</span><span style="color:#9ECE6A"> code focusing on </span><span style="color:#7DCFFF">${</span><span style="color:#7DCFFF">focus</span><span style="color:#7DCFFF">}</span><span style="color:#9ECE6A">:</span><span style="color:#89DDFF">`</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">            &quot;&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">            &quot;</span><span style="color:#9ECE6A">```</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF"> +</span><span style="color:#7DCFFF"> language</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#7DCFFF">            code</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">            &quot;</span><span style="color:#9ECE6A">```</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">            &quot;&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">            &quot;</span><span style="color:#9ECE6A">Provide feedback on:</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#7DCFFF">            focus</span><span style="color:#BB9AF7"> ===</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">all</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">              ?</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">- Security issues</span><span style="color:#89DDFF">\n</span><span style="color:#9ECE6A">- Performance optimizations</span><span style="color:#89DDFF">\n</span><span style="color:#9ECE6A">- Code readability</span><span style="color:#89DDFF">\n</span><span style="color:#9ECE6A">- Best practices</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">              :</span><span style="color:#7DCFFF"> focus</span><span style="color:#BB9AF7"> ===</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">security</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">                ?</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">- Potential security vulnerabilities</span><span style="color:#89DDFF">\n</span><span style="color:#9ECE6A">- Input validation</span><span style="color:#89DDFF">\n</span><span style="color:#9ECE6A">- Authentication/authorization issues</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">                :</span><span style="color:#7DCFFF"> focus</span><span style="color:#BB9AF7"> ===</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">performance</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">                  ?</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">- Time complexity</span><span style="color:#89DDFF">\n</span><span style="color:#9ECE6A">- Memory usage</span><span style="color:#89DDFF">\n</span><span style="color:#9ECE6A">- Potential optimizations</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">                  :</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">- Variable naming</span><span style="color:#89DDFF">\n</span><span style="color:#9ECE6A">- Code structure</span><span style="color:#89DDFF">\n</span><span style="color:#9ECE6A">- Comments and documentation</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">          ]</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">join</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;\n&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">        }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    ]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span></span>
<span class="line"><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="server.registerPrompt(
  &#34;code-review&#34;,
  {
    title: &#34;Code Review&#34;,
    description: &#34;Review code for quality and best practices&#34;,
    argsSchema: {
      language: z.enum([&#34;javascript&#34;, &#34;typescript&#34;, &#34;python&#34;, &#34;go&#34;]),
      code: z.string(),
      focus: z
        .enum([&#34;security&#34;, &#34;performance&#34;, &#34;readability&#34;, &#34;all&#34;])
        .default(&#34;all&#34;),
    },
  },
  ({ language, code, focus }) => ({
    messages: [
      {
        role: &#34;user&#34;,
        content: {
          type: &#34;text&#34;,
          text: [
            `Please review this ${language} code focusing on ${focus}:`,
            &#34;&#34;,
            &#34;```&#34; + language,
            code,
            &#34;```&#34;,
            &#34;&#34;,
            &#34;Provide feedback on:&#34;,
            focus === &#34;all&#34;
              ? &#34;- Security issues\n- Performance optimizations\n- Code readability\n- Best practices&#34;
              : focus === &#34;security&#34;
                ? &#34;- Potential security vulnerabilities\n- Input validation\n- Authentication/authorization issues&#34;
                : focus === &#34;performance&#34;
                  ? &#34;- Time complexity\n- Memory usage\n- Potential optimizations&#34;
                  : &#34;- Variable naming\n- Code structure\n- Comments and documentation&#34;,
          ].join(&#34;\n&#34;),
        },
      },
    ],
  })
);" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h2 id="what-a-client-can-expose">What a Client can expose<a class="heading-link" aria-label="Link to section" href="#what-a-client-can-expose"><span class="heading-link-icon">#</span></a></h2>
<p>An MCP client can provide capabilities that let servers interact with the world beyond their sandbox:</p>
<h3 id="roots-filesystem-boundaries">Roots: Filesystem boundaries<a class="heading-link" aria-label="Link to section" href="#roots-filesystem-boundaries"><span class="heading-link-icon">#</span></a></h3>
<ul>
<li>Client tells server which directories it can access</li>
<li>Creates secure sandbox (e.g., only your project folder)</li>
<li>Prevents access to system files or other projects</li>
</ul>
<h3 id="sampling-nested-llm-calls">Sampling: Nested LLM calls<a class="heading-link" aria-label="Link to section" href="#sampling-nested-llm-calls"><span class="heading-link-icon">#</span></a></h3>
<ul>
<li>Servers can request AI completions through the client</li>
<li>No API keys needed on server side</li>
<li>Enables autonomous, agentic behaviors</li>
</ul>
<h3 id="elicitation-asking-users-for-input">Elicitation: Asking users for input<a class="heading-link" aria-label="Link to section" href="#elicitation-asking-users-for-input"><span class="heading-link-icon">#</span></a></h3>
<ul>
<li>Servers request missing info from users via client UI</li>
<li>Client handles forms and validation</li>
<li>Users can accept, decline, or cancel requests</li>
</ul>
<h2 id="example-how-we-can-use-mcps-in-vscode">Example: How we can use MCPS in Vscode<a class="heading-link" aria-label="Link to section" href="#example-how-we-can-use-mcps-in-vscode"><span class="heading-link-icon">#</span></a></h2>
<p>Your <code>mcp.json</code> could look like this:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="json"><code><span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">servers</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">    &quot;</span><span style="color:#0DB9D7">playwright</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">      &quot;</span><span style="color:#7DCFFF">gallery</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &quot;</span><span style="color:#7DCFFF">command</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">npx</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &quot;</span><span style="color:#7DCFFF">args</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">@playwright/mcp@latest</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &quot;</span><span style="color:#7DCFFF">type</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">stdio</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">    &quot;</span><span style="color:#0DB9D7">deepwiki</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">      &quot;</span><span style="color:#7DCFFF">type</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">http</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &quot;</span><span style="color:#7DCFFF">url</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">https://mcp.deepwiki.com/sse</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &quot;</span><span style="color:#7DCFFF">gallery</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="{
  &#34;servers&#34;: {
    &#34;playwright&#34;: {
      &#34;gallery&#34;: true,
      &#34;command&#34;: &#34;npx&#34;,
      &#34;args&#34;: [&#34;@playwright/mcp@latest&#34;],
      &#34;type&#34;: &#34;stdio&#34;
    },
    &#34;deepwiki&#34;: {
      &#34;type&#34;: &#34;http&#34;,
      &#34;url&#34;: &#34;https://mcp.deepwiki.com/sse&#34;,
      &#34;gallery&#34;: true
    }
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<ul>
<li><strong>playwright</strong> → Runs <code>npx @playwright/mcp@latest</code> locally over stdio for low-latency browser automation</li>
<li><strong>deepwiki</strong> → Connects over HTTP/SSE to <code>https://mcp.deepwiki.com/sse</code> for live docs and codebase search</li>
<li><strong>gallery: true</strong> → Makes them visible in tool pickers</li>
</ul>
<h2 id="what-mcp-is-not">What MCP is not<a class="heading-link" aria-label="Link to section" href="#what-mcp-is-not"><span class="heading-link-icon">#</span></a></h2>
<ul>
<li><strong>Not a hosted service</strong> — It is a protocol</li>
<li><strong>Not a replacement</strong> for your app logic</li>
<li><strong>Not a magic fix</strong> for every hallucination — It gives access to real tools and data</li>
<li>You still need good prompts and good UX</li>
</ul>
<hr/>
<h2 id="simple-example-of-your-first-mcp-server">Simple example of your first MCP Server<a class="heading-link" aria-label="Link to section" href="#simple-example-of-your-first-mcp-server"><span class="heading-link-icon">#</span></a></h2>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="ts"><code><span class="line"><span style="color:#51597D;font-style:italic">#!/usr/bin/env node</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">z</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">zod</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">McpServer</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">@modelcontextprotocol/sdk/server/mcp.js</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">StdioServerTransport</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">@modelcontextprotocol/sdk/server/stdio.js</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> server</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> McpServer</span><span style="color:#9ABDF5">({</span></span>
<span class="line"><span style="color:#73DACA">  name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">echo-onefile</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  version</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">1.0.0</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">})</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">server</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">tool</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#9ECE6A">echo</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#9ECE6A">Echo back the provided text</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  {</span></span>
<span class="line"><span style="color:#73DACA">    text</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> z</span></span>
<span class="line"><span style="color:#89DDFF">      .</span><span style="color:#7AA2F7">string</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#89DDFF">      .</span><span style="color:#7AA2F7">min</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">1</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">Text cannot be empty</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#89DDFF">      .</span><span style="color:#7AA2F7">describe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">Text to echo back</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  async</span><span style="color:#9ABDF5"> (</span><span style="color:#89DDFF">{</span><span style="color:#E0AF68"> text</span><span style="color:#89DDFF"> }</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> ({</span></span>
<span class="line"><span style="color:#73DACA">    content</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [{</span><span style="color:#73DACA"> type</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">text</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#7DCFFF"> text</span><span style="color:#9ABDF5"> }]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span></span>
<span class="line"><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> transport</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> StdioServerTransport</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">server</span></span>
<span class="line"><span style="color:#89DDFF">  .</span><span style="color:#7AA2F7">connect</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">transport</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#89DDFF">  .</span><span style="color:#7AA2F7">then</span><span style="color:#9ABDF5">(()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#C0CAF5"> console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">error</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">Echo MCP server listening on stdio</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">))</span></span>
<span class="line"><span style="color:#89DDFF">  .</span><span style="color:#7AA2F7">catch</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">err</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">    console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">error</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">err</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">    process</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">exit</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">1</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="#!/usr/bin/env node
import { z } from &#34;zod&#34;;
import { McpServer } from &#34;@modelcontextprotocol/sdk/server/mcp.js&#34;;
import { StdioServerTransport } from &#34;@modelcontextprotocol/sdk/server/stdio.js&#34;;

const server = new McpServer({
  name: &#34;echo-onefile&#34;,
  version: &#34;1.0.0&#34;,
});

server.tool(
  &#34;echo&#34;,
  &#34;Echo back the provided text&#34;,
  {
    text: z
      .string()
      .min(1, &#34;Text cannot be empty&#34;)
      .describe(&#34;Text to echo back&#34;),
  },
  async ({ text }) => ({
    content: [{ type: &#34;text&#34;, text }],
  })
);

const transport = new StdioServerTransport();

server
  .connect(transport)
  .then(() => console.error(&#34;Echo MCP server listening on stdio&#34;))
  .catch(err => {
    console.error(err);
    process.exit(1);
  });" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>This example uses the official <a href="https://modelcontextprotocol.io/docs/sdk" rel="noopener noreferrer" target="_blank">MCP SDK for TypeScript</a>, which provides type-safe abstractions for building MCP servers.</p>
<p>The server exposes a single tool called “echo” that takes text input and returns it back. We’re using <a href="https://zod.dev/" rel="noopener noreferrer" target="_blank">Zod</a> for runtime schema validation, ensuring the input matches our expected structure with proper type safety and clear error messages.</p>
<h2 id="simple-mcp-client-example">Simple MCP Client Example<a class="heading-link" aria-label="Link to section" href="#simple-mcp-client-example"><span class="heading-link-icon">#</span></a></h2>
<p>Here’s how to connect to an MCP server and use its capabilities:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">Client</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">@modelcontextprotocol/sdk/client/index.js</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">StdioClientTransport</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">@modelcontextprotocol/sdk/client/stdio.js</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Create a client that connects to your MCP server</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">async</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> connectToServer</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Create transport - this runs your server as a subprocess</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> transport</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> StdioClientTransport</span><span style="color:#9ABDF5">({</span></span>
<span class="line"><span style="color:#73DACA">    command</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">node</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    args</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">./echo-server.js</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Create and connect the client</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> client</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> Client</span><span style="color:#9ABDF5">({</span></span>
<span class="line"><span style="color:#73DACA">    name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">my-mcp-client</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    version</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">1.0.0</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  await</span><span style="color:#C0CAF5"> client</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">connect</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">transport</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#C0CAF5"> client</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Use the server&#39;s capabilities</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">async</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useServer</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> client</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#7AA2F7"> connectToServer</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // List available tools</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> tools</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#C0CAF5"> client</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">listTools</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">  console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">log</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">Available tools:</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> tools</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Call a tool</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> result</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#C0CAF5"> client</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">callTool</span><span style="color:#9ABDF5">({</span></span>
<span class="line"><span style="color:#73DACA">    name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">echo</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    arguments</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">      text</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">Hello from MCP client!</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">  console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">log</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">Tool result:</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> result</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">content</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // List and read resources</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> resources</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#C0CAF5"> client</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">listResources</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">  for</span><span style="color:#9ABDF5"> (</span><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> resource</span><span style="color:#89DDFF"> of</span><span style="color:#C0CAF5"> resources</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> content</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#C0CAF5"> client</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">readResource</span><span style="color:#9ABDF5">({</span></span>
<span class="line"><span style="color:#73DACA">      uri</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> resource</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">uri</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">    console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">log</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">`</span><span style="color:#9ECE6A">Resource </span><span style="color:#7DCFFF">${</span><span style="color:#C0CAF5">resource</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">name</span><span style="color:#7DCFFF">}</span><span style="color:#9ECE6A">:</span><span style="color:#89DDFF">`</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> content</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Get and execute a prompt</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> prompts</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#C0CAF5"> client</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">listPrompts</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">prompts</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">length</span><span style="color:#BB9AF7"> &gt;</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> prompt</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#C0CAF5"> client</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">getPrompt</span><span style="color:#9ABDF5">({</span></span>
<span class="line"><span style="color:#73DACA">      name</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> prompts</span><span style="color:#9ABDF5">[</span><span style="color:#FF9E64">0</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">name</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">      arguments</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">        code</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">console.log(&#39;test&#39;)</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">        language</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">javascript</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">    console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">log</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">Prompt messages:</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> prompt</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">messages</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Clean up</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  await</span><span style="color:#C0CAF5"> client</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">close</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Run the client</span></span>
<span class="line"><span style="color:#7AA2F7">useServer</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">catch</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">console</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">error</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="import { Client } from &#34;@modelcontextprotocol/sdk/client/index.js&#34;;
import { StdioClientTransport } from &#34;@modelcontextprotocol/sdk/client/stdio.js&#34;;

// Create a client that connects to your MCP server
async function connectToServer() {
  // Create transport - this runs your server as a subprocess
  const transport = new StdioClientTransport({
    command: &#34;node&#34;,
    args: [&#34;./echo-server.js&#34;],
  });

  // Create and connect the client
  const client = new Client({
    name: &#34;my-mcp-client&#34;,
    version: &#34;1.0.0&#34;,
  });

  await client.connect(transport);

  return client;
}

// Use the server's capabilities
async function useServer() {
  const client = await connectToServer();

  // List available tools
  const tools = await client.listTools();
  console.log(&#34;Available tools:&#34;, tools);

  // Call a tool
  const result = await client.callTool({
    name: &#34;echo&#34;,
    arguments: {
      text: &#34;Hello from MCP client!&#34;,
    },
  });

  console.log(&#34;Tool result:&#34;, result.content);

  // List and read resources
  const resources = await client.listResources();
  for (const resource of resources) {
    const content = await client.readResource({
      uri: resource.uri,
    });
    console.log(`Resource ${resource.name}:`, content);
  }

  // Get and execute a prompt
  const prompts = await client.listPrompts();
  if (prompts.length > 0) {
    const prompt = await client.getPrompt({
      name: prompts[0].name,
      arguments: {
        code: &#34;console.log('test')&#34;,
        language: &#34;javascript&#34;,
      },
    });
    console.log(&#34;Prompt messages:&#34;, prompt.messages);
  }

  // Clean up
  await client.close();
}

// Run the client
useServer().catch(console.error);" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>This client example shows how to:</p>
<ul>
<li>Connect to an MCP server using stdio transport</li>
<li>List and call tools with arguments</li>
<li>Read resources from the server</li>
<li>Get and use prompt templates</li>
<li>Properly close the connection when done</li>
</ul>
<h2 id="use-it-with-vscode">Use it with Vscode<a class="heading-link" aria-label="Link to section" href="#use-it-with-vscode"><span class="heading-link-icon">#</span></a></h2>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="json"><code><span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">servers</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">    &quot;</span><span style="color:#0DB9D7">echo</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">      &quot;</span><span style="color:#7DCFFF">gallery</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &quot;</span><span style="color:#7DCFFF">type</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">stdio</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &quot;</span><span style="color:#7DCFFF">command</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">node</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &quot;</span><span style="color:#7DCFFF">args</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">--import</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">tsx</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">/absolute/path/echo-server.ts</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">]</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="{
  &#34;servers&#34;: {
    &#34;echo&#34;: {
      &#34;gallery&#34;: true,
      &#34;type&#34;: &#34;stdio&#34;,
      &#34;command&#34;: &#34;node&#34;,
      &#34;args&#34;: [&#34;--import&#34;, &#34;tsx&#34;, &#34;/absolute/path/echo-server.ts&#34;]
    }
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h2 id="summary">Summary<a class="heading-link" aria-label="Link to section" href="#summary"><span class="heading-link-icon">#</span></a></h2>
<p>This was just my starter post for MCP to give an overview. I will write more blog posts that will go in depth about the different topics.</p>
<div class="alert alert-note astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">💡</span> Note </p> <div class="alert-content astro-7kdbuayl"> <p>If you need a TypeScript starter template for your next MCP server, you can
use my
<a href="https://github.com/alexanderop/mcp-server-starter-ts" rel="noopener noreferrer" target="_blank">mcp-server-starter-ts</a>
repository to get up and running quickly.</p> </div> </div>  </article> <script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).only=e;window.dispatchEvent(new Event("astro:only"));})();</script><astro-island uid="Z1XneyL" component-url="/_astro/presentation.C3Wa0mjp.js" component-export="VMarkBlogRenderer" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;containerSelector&quot;:[0,&quot;#article&quot;],&quot;class&quot;:[0,&quot;astro-vj4tpspi&quot;]}" ssr client="only" opts="{&quot;name&quot;:&quot;VMarkBlogRenderer&quot;,&quot;value&quot;:&quot;react&quot;}"></astro-island> <!-- Fullscreen Modal Container using native dialog --><dialog id="mermaid-modal" class="mermaid-modal" aria-label="Fullscreen diagram view"> <div class="mermaid-modal-content"> <button class="mermaid-modal-close" aria-label="Close fullscreen view" type="button"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <line x1="18" y1="6" x2="6" y2="18"></line> <line x1="6" y1="6" x2="18" y2="18"></line> </svg> </button> <div class="mermaid-modal-diagram"></div> <div class="mermaid-modal-hint">Press <kbd>Esc</kbd> or click outside to close</div> </div> </dialog>  <script type="module">const p=new Set;function g(){const e=document.getElementById("mermaid-modal"),c=e?.querySelector(".mermaid-modal-diagram"),f=e?.querySelector(".mermaid-modal-close");if(!e||!c)return;document.querySelectorAll('svg[id^="mermaid-"]').forEach(t=>{if(!t.id.match(/^mermaid-\d+$/)||p.has(t.id)||t.parentElement?.classList.contains("mermaid-fullscreen-wrapper")||t.closest(".mermaid-modal"))return;p.add(t.id);const n=document.createElement("div");n.className="mermaid-fullscreen-wrapper mermaid-clickable",n.setAttribute("tabindex","0"),n.setAttribute("role","button"),n.setAttribute("aria-label","Click to view diagram fullscreen"),t.parentElement?.insertBefore(n,t),n.appendChild(t);const o=document.createElement("div");o.className="mermaid-expand-icon",o.innerHTML=`
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
</li> <li class="astro-vj4tpspi">Small tips and trick</li> </ul> </div> <a href="https://alex-op-newsletter.beehiiv.com/subscribe?utm_source=blog&utm_medium=post&utm_campaign=post_what-is-model-context-protocol-mcp" target="_blank" rel="noopener noreferrer" id="newsletter-subscribe-button" class="inline-flex items-center justify-center gap-2 rounded-full bg-skin-accent px-6 py-3 text-base font-semibold text-skin-inverted shadow-md transition-all duration-200 hover:scale-[1.02] hover:transform hover:opacity-90 astro-vj4tpspi"> <svg class="h-5 w-5 fill-current astro-vj4tpspi" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg>
Subscribe Now
</a> <button id="newsletter-dismiss" data-post-slug="what-is-model-context-protocol-mcp" class="absolute right-3 top-3 rounded-full p-1 text-skin-base transition-all duration-200 hover:bg-skin-accent hover:bg-opacity-10 hover:text-skin-accent astro-vj4tpspi" aria-label="Close notification"> <svg class="h-5 w-5 astro-vj4tpspi" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class="astro-vj4tpspi"></path> </svg> </button> </div> </div> </div> <ul class="my-8 flex flex-wrap gap-2 astro-vj4tpspi"> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/mcp/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-2"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">mcp</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/typescript/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-3"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">typescript</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/ai/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-4"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">ai</span>   </a> </li>  </ul> <div class="flex flex-col-reverse items-center justify-between gap-6 sm:flex-row-reverse sm:items-end sm:gap-4 astro-vj4tpspi"> <button id="back-to-top" class="focus-outline whitespace-nowrap py-1 hover:opacity-75 astro-vj4tpspi"> <svg xmlns="http://www.w3.org/2000/svg" class="rotate-90 astro-vj4tpspi"> <path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg> <span class="astro-vj4tpspi">Back to Top</span> </button> <div class="social-icons astro-wkojbtzc"> <span class="italic astro-wkojbtzc">Share this post on:</span> <div class="text-center astro-wkojbtzc"> <a href="https://wa.me/?text=https://alexop.dev/posts/what-is-model-context-protocol-mcp/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via WhatsApp" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"></path>
      <path d="M9 10a0.5 .5 0 0 0 1 0v-1a0.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a0.5 .5 0 0 0 0 -1h-1a0.5 .5 0 0 0 0 1"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via WhatsApp</span> </a><a href="https://www.facebook.com/sharer.php?u=https://alexop.dev/posts/what-is-model-context-protocol-mcp/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Facebook" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"
    ></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on Facebook</span> </a><a href="https://x.com/intent/tweet?url=https://alexop.dev/posts/what-is-model-context-protocol-mcp/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Tweet this post" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Tweet this post</span> </a><a href="https://t.me/share/url?url=https://alexop.dev/posts/what-is-model-context-protocol-mcp/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via Telegram" target="_blank" rel="noopener noreferrer"> <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon-tabler"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"></path>
      </svg> <span class="sr-only astro-wkojbtzc">Share this post via Telegram</span> </a><a href="https://pinterest.com/pin/create/button/?url=https://alexop.dev/posts/what-is-model-context-protocol-mcp/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Pinterest" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <line x1="8" y1="20" x2="12" y2="11"></line>
      <path d="M10.7 14c.437 1.263 1.43 2 2.55 2c2.071 0 3.75 -1.554 3.75 -4a5 5 0 1 0 -9.7 1.7"></path>
      <circle cx="12" cy="12" r="9"></circle>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post on Pinterest</span> </a><a href="mailto:?subject=See%20this%20post&#38;body=https://alexop.dev/posts/what-is-model-context-protocol-mcp/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via email" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via email</span> </a><a href="https://www.linkedin.com/shareArticle?mini=true&url=https://alexop.dev/posts/what-is-model-context-protocol-mcp/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
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
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on LinkedIn</span> </a> </div> </div>  </div> <section id="comments-section" class="giscus-container"></section> <script type="module">function a(){const e=document.getElementById("comments-section");if(!e)return;e.querySelector(".giscus, iframe")&&(e.innerHTML="");const t=document.createElement("script");t.src="https://giscus.app/client.js",t.setAttribute("data-repo","alexanderop/blog-comments"),t.setAttribute("data-repo-id","R_kgDON-LviQ"),t.setAttribute("data-category","Q&A"),t.setAttribute("data-category-id","DIC_kwDON-Lvic4CnPll"),t.setAttribute("data-mapping","url"),t.setAttribute("data-strict","0"),t.setAttribute("data-reactions-enabled","1"),t.setAttribute("data-emit-metadata","0"),t.setAttribute("data-input-position","bottom"),t.setAttribute("data-theme","dark"),t.setAttribute("data-lang","en"),t.setAttribute("data-loading","lazy"),t.setAttribute("crossorigin","anonymous"),t.async=!0,e.appendChild(t)}a();document.addEventListener("astro:page-load",a);</script> <div data-pagefind-ignore class="mb-8 mt-16 astro-vj4tpspi"> <h2 class="mb-6 text-3xl font-bold text-skin-accent astro-vj4tpspi">
Most Related Posts
</h2> <div class="md:grid-cols-3 grid grid-cols-1 gap-6 astro-vj4tpspi"> <a href="/posts/how-i-use-claude-code-for-doing-seo-audits/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">How I Use Claude Code for Doing SEO Audits</h3> <p class="related-post-description astro-vj4tpspi"> Learn how to leverage Claude Code with Puppeteer MCP to perform comprehensive SEO audits in minutes, complete with automated analysis and actionable reports. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-06-26T00:00:00.000Z">Jun 26, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> ai </span> </div> </div> </a><a href="/posts/understanding-claude-code-full-stack/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">Understanding Claude Code&#39;s Full Stack: MCP, Skills, Subagents, and Hooks Explained</h3> <p class="related-post-description astro-vj4tpspi"> A practical guide to Claude Code&#39;s features — explained in the order they were introduced: MCP (2024), Claude Code core (Feb 2025), Plugins (2025), and Agent Skills (Oct 2025). What each does, how they fit together, and when to use what. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-11-09T00:00:00.000Z">Nov 9, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> claude-code </span> </div> </div> </a><a href="/posts/how-i-added-llms-txt-to-my-astro-blog/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">How I Added llms.txt to My Astro Blog</h3> <p class="related-post-description astro-vj4tpspi"> I built a simple way to load my blog content into any LLM with one click. This post shows how you can do it too. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-03-03T00:00:00.000Z">Mar 3, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> astro </span> </div> </div> </a> </div> </div> </main> <footer class="mt-auto astro-sz7xmlte"> <div class="max-w-5xl mx-auto px-4"> <hr class="border-skin-line" aria-hidden="true"> </div> <div class="footer-wrapper astro-sz7xmlte"> <div class="footer-content astro-sz7xmlte"> <div class="copyright-wrapper astro-sz7xmlte"> <span class="astro-sz7xmlte">Copyright &#169; 2026</span> <span class="separator astro-sz7xmlte">&nbsp;|&nbsp;</span> <span class="astro-sz7xmlte">All rights reserved.</span> </div> <div class="rss-prompt astro-sz7xmlte"> <a href="/rss.xml" class="rss-link group astro-sz7xmlte" title="Never miss a post - Subscribe via RSS" onclick="if (window.plausible) window.plausible('RSS Subscribe', { props: { location: 'footer' } })"> <div class="flex items-center gap-2 astro-sz7xmlte"> <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-skin-accent group-hover:animate-pulse astro-sz7xmlte"><path fill="currentColor" d="M19 20.001C19 11.729 12.271 5 4 5v2c7.168 0 13 5.832 13 13.001h2z" class="astro-sz7xmlte"></path><path fill="currentColor" d="M12 20.001h2C14 14.486 9.514 10 4 10v2c4.411 0 8 3.589 8 8.001z" class="astro-sz7xmlte"></path><circle cx="6" cy="18" r="2" fill="currentColor" class="astro-sz7xmlte"></circle> </svg> <span class="text-sm astro-sz7xmlte">Subscribe via RSS</span> </div> </a> </div> <div class="social-icons flex astro-upu6fzxr"> <a href="https://github.com/alexanderop" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title=" alexop.dev on Github" target="_blank" rel="noopener noreferrer"> <svg
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
    </script> </body> </html>  <script>(function(){const postSlug = "what-is-model-context-protocol-mcp";

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
# Source: https://alexop.dev/posts/whats-new-vscode-copilot-january-2026

<!DOCTYPE html><html lang="en" class="scroll-smooth astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/posts/whats-new-vscode-copilot-january-2026/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>What&#39;s New in VS Code Copilot: January 2026 Update | alexop.dev</title><meta name="title" content="What's New in VS Code Copilot: January 2026 Update | alexop.dev"><meta name="description" content="Major updates to VS Code Copilot including parallel subagent execution, a new skills system, deeper Claude integration with extended thinking, terminal improvements with kitty keyboard protocol, and instruction files that now work everywhere."><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="What's New in VS Code Copilot: January 2026 Update | alexop.dev"><meta property="og:description" content="Major updates to VS Code Copilot including parallel subagent execution, a new skills system, deeper Claude integration with extended thinking, terminal improvements with kitty keyboard protocol, and instruction files that now work everywhere."><meta property="og:url" content="https://alexop.dev/posts/whats-new-vscode-copilot-january-2026/"><meta property="og:image" content="https://alexop.dev/posts/whats-new-in-vs-code-copilot-january-2026-update/index.png"><meta property="og:type" content="article"><!-- Article Published/Modified time --><meta property="article:published_time" content="2026-01-24T00:00:00.000Z"><meta property="article:modified_time" content="2026-01-24T12:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/posts/whats-new-vscode-copilot-january-2026/"><meta property="twitter:title" content="What's New in VS Code Copilot: January 2026 Update | alexop.dev"><meta property="twitter:description" content="Major updates to VS Code Copilot including parallel subagent execution, a new skills system, deeper Claude integration with extended thinking, terminal improvements with kitty keyboard protocol, and instruction files that now work everywhere."><meta property="twitter:image" content="https://alexop.dev/posts/whats-new-in-vs-code-copilot-january-2026-update/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"What's New in VS Code Copilot: January 2026 Update | alexop.dev","description":"Major updates to VS Code Copilot including parallel subagent execution, a new skills system, deeper Claude integration with extended thinking, terminal improvements with kitty keyboard protocol, and instruction files that now work everywhere.","image":"https://alexop.dev/posts/whats-new-in-vs-code-copilot-january-2026-update/index.png","datePublished":"2026-01-24T00:00:00.000Z","dateModified":"2026-01-24T12:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
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
</style><style>[data-astro-transition-scope="astro-plk3gbjq-1"] { view-transition-name: whats-new-in-vs-code-copilot-january-2026-update; }@layer astro { ::view-transition-old(whats-new-in-vs-code-copilot-january-2026-update) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(whats-new-in-vs-code-copilot-january-2026-update) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(whats-new-in-vs-code-copilot-january-2026-update) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(whats-new-in-vs-code-copilot-january-2026-update) { 
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
	animation-name: astroFadeIn; }</style><style>.file-tree__item:where(.astro-o25vlg2d){margin:0;padding:0;position:relative}.file-tree__item:where(.astro-o25vlg2d):before{content:"";position:absolute;left:calc(.5rem + (var(--level) * 1.25rem));top:0;bottom:0;width:1px;background:rgba(var(--color-text-base),.15)}.file-tree__item:where(.astro-o25vlg2d):last-child:before{bottom:50%}.file-tree__item:where(.astro-o25vlg2d):after{content:"";position:absolute;left:calc(.5rem + (var(--level) * 1.25rem));top:50%;width:.75rem;height:1px;background:rgba(var(--color-text-base),.15)}.file-tree__folder:where(.astro-o25vlg2d){margin:0;padding:0}.file-tree__folder:where(.astro-o25vlg2d)>summary:where(.astro-o25vlg2d){list-style:none;cursor:pointer;display:flex;gap:.5rem;align-items:center;padding:.2rem .5rem .2rem calc(1.5rem + (var(--level) * 1.25rem));border-radius:.25rem;transition:background-color .15s ease;line-height:1.6;position:relative}.file-tree__folder:where(.astro-o25vlg2d)>summary:where(.astro-o25vlg2d):hover{background:rgba(var(--color-text-base),.05)}.file-tree__folder:where(.astro-o25vlg2d)[open]>summary:where(.astro-o25vlg2d) .file-tree__caret:where(.astro-o25vlg2d){transform:rotate(90deg)}.file-tree__folder:where(.astro-o25vlg2d):not([open])>summary:where(.astro-o25vlg2d) .file-tree__caret:where(.astro-o25vlg2d){transform:rotate(0)}.file-tree__folder:where(.astro-o25vlg2d)>summary:where(.astro-o25vlg2d)::-webkit-details-marker{display:none}.file-tree__list:where(.astro-o25vlg2d){list-style:none;margin:0;padding:0}.file-tree__file:where(.astro-o25vlg2d){display:flex;gap:.5rem;align-items:center;padding:.2rem .5rem .2rem calc(1.5rem + (var(--level) * 1.25rem));border-radius:.25rem;text-decoration:none;color:inherit;transition:background-color .15s ease;line-height:1.6;position:relative}.file-tree__file:where(.astro-o25vlg2d):hover{background:rgba(var(--color-text-base),.05)}a:where(.astro-o25vlg2d).file-tree__file:hover .file-tree__name:where(.astro-o25vlg2d){color:rgb(var(--color-accent))}.file-tree__icon:where(.astro-o25vlg2d){width:1rem;height:1rem;flex-shrink:0;color:rgba(var(--color-text-base),.4);display:inline-flex;align-items:center;justify-content:center}.file-tree__icon--file:where(.astro-o25vlg2d){color:rgba(var(--color-text-base),.4)}.file-tree__icon--colored:where(.astro-o25vlg2d){color:inherit}.file-tree__icon--text:where(.astro-o25vlg2d){font-weight:600;font-size:.875rem;display:inline-flex;align-items:center;justify-content:center;width:1rem;height:1rem}.file-tree__name:where(.astro-o25vlg2d){white-space:nowrap;transition:color .15s ease;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,Liberation Mono,Courier New,monospace}.file-tree__comment:where(.astro-o25vlg2d){color:rgba(var(--color-text-base),.5);font-style:italic;margin-left:.5rem;white-space:nowrap;font-size:.9em}.file-tree__caret:where(.astro-o25vlg2d){width:.75rem;height:.75rem;transition:transform .2s ease;flex-shrink:0;color:rgba(var(--color-text-base),.5);font-size:.625rem;display:inline-flex;align-items:center;justify-content:center;transform-origin:center}
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-3"] { view-transition-name: tooling; }@layer astro { ::view-transition-old(tooling) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-4"] { view-transition-name: vscode; }@layer astro { ::view-transition-old(vscode) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(vscode) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(vscode) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(vscode) { 
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <div class="mx-auto flex w-full max-w-5xl justify-start px-2 astro-vj4tpspi"> <button class="focus-outline mb-2 mt-8 flex hover:opacity-75 astro-vj4tpspi" onclick="(() => (history.length === 1) ? window.location = '/' : history.back())()"> <svg xmlns="http://www.w3.org/2000/svg" class="astro-vj4tpspi"><path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg><span class="astro-vj4tpspi">Go back</span> </button> </div> <main data-pagefind-body id="main-content" class="relative astro-vj4tpspi"> <h1 class="post-title astro-vj4tpspi" data-astro-transition-scope="astro-plk3gbjq-1">What&#39;s New in VS Code Copilot: January 2026 Update</h1> <div class="my-2 flex items-center justify-between astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-100 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="italic text-base">Updated:</span><span class="italic text-base"><time dateTime="2026-01-24T12:00:00.000Z">Jan 24, 2026</time><span class="sr-only"> at </span></span></div> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="OTbuL" prefix="r3" component-url="/_astro/PostCopyButton.-PGtk4At.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;title&quot;:[0,&quot;What&#39;s New in VS Code Copilot: January 2026 Update&quot;],&quot;content&quot;:[0,&quot;import InternalLink from \&quot;@features/mdx-components/components/InternalLink.astro\&quot;;\nimport FileTree from \&quot;@features/filetree/components/FileTree.astro\&quot;;\nimport Figure from \&quot;@features/mdx-components/components/Figure.astro\&quot;;\nimport subAgentParallel from \&quot;@assets/images/vscodeUpdate/subAgentParallel.png\&quot;;\n\nThe past week has brought a wave of updates to VS Code&#39;s Copilot experience, with major improvements to how agents work together, a new skills system, deeper Claude integration, and significant terminal enhancements. Here&#39;s what you need to know—with concrete examples you can try today.\n\nFor those who want to dive deeper into the implementation details, I&#39;ve included links to the relevant GitHub pull requests and issues throughout this post.\n\n---\n\n## Subagents Get Smarter (and Faster)\n\nTwo significant changes make subagents far more practical for complex workflows.\n\n**Related:** [Issue #274630 - Parallel subagent execution](https://github.com/microsoft/vscode/issues/274630)\n\n### Parallel Execution\n\nPreviously, if you kicked off multiple `runSubagent` calls, they&#39;d run one after another. Now they can run simultaneously when tasks are independent, dramatically reducing wait times for research and code review operations.\n\n**Example prompt:**\n```\nResearch the best approaches for:\n1. Rate limiting in our REST API\n2. Caching strategies for our database queries\n3. Error handling patterns for our microservices\n\nUse a subagent for each topic and compile the findings.\n```\n\nWith parallel execution, all three research subagents run concurrently instead of sequentially—cutting total wait time significantly.\n\n&lt;Figure\n  src={subAgentParallel}\n  alt=\&quot;Parallel subagent execution visualization\&quot;\n  size=\&quot;large\&quot;\n/&gt;\n\n### Fine-Grained Tool Access\n\nYou can now constrain which tools a subagent can access. This is critical for safety-conscious workflows where you want AI help without the risk of unintended changes.\n\n**Creating a custom agent with restricted tools:**\n\nCreate a file at `.github/agents/github-researcher.md`:\n\n```markdown\n---\nname: github-researcher\ndescription: Research agent with access to GitHub. Use for searching issues,\n             reading documentation, and gathering information. Cannot edit files.\ntools: [&#39;read&#39;, &#39;search&#39;, &#39;web&#39;, &#39;github/*&#39;]\nargument-hint: The research task to complete\n---\n\nYou are a research assistant with read-only access to the codebase and GitHub.\n\nYour capabilities:\n- Search and read files in the repository\n- Search GitHub issues and pull requests\n- Fetch web documentation\n\nYou cannot:\n- Edit or create files\n- Run terminal commands\n- Make commits\n\nWhen researching, provide citations and links to sources.\n```\n\nNow you can ask: *\&quot;Use a subagent to find all issues assigned to me about authentication and summarize them\&quot;* — and the subagent will be limited to read-only operations.\n\nIf you&#39;ve used Claude Code&#39;s subagent system, you&#39;ll recognize this pattern—it&#39;s similar to how &lt;InternalLink slug=\&quot;claude-code-customization-guide-claudemd-skills-subagents\&quot;&gt;Claude Code handles skills and subagents&lt;/InternalLink&gt; with tool restrictions.\n\n### Control Subagent Availability\n\nUse the `infer` attribute to control whether an agent can be used as a subagent:\n\n```markdown\n---\nname: dangerous-deployer\ndescription: Handles production deployments\ntools: [&#39;execute&#39;, &#39;edit&#39;, &#39;read&#39;]\ninfer: false  # This agent cannot be auto-invoked as a subagent\n---\n```\n\n---\n\n## Skills Are Now a First-Class Feature\n\nSkills are now **enabled by default** for all users. They&#39;re folders containing instructions and resources that Copilot loads on-demand when relevant to your task.\n\n**Related PRs:**\n- [Issue #286237 - Custom agent improvements](https://github.com/microsoft/vscode/issues/286237)\n- [Issue #286238 - Skill lookup enhancements](https://github.com/microsoft/vscode/issues/286238)\n- [PR #3082 - Implement agent using CustomAgentProvider API](https://github.com/microsoft/vscode-copilot-chat/pull/3082)\n\n### Creating Your First Skill\n\nCreate a directory structure:\n\n&lt;FileTree tree={[\n  { name: \&quot;.github\&quot;, children: [\n    { name: \&quot;skills\&quot;, children: [\n      { name: \&quot;webapp-testing\&quot;, children: [\n        { name: \&quot;SKILL.md\&quot;, comment: \&quot;// Instructions\&quot; },\n        { name: \&quot;test-template.js\&quot;, comment: \&quot;// Example template\&quot; }\n      ]}\n    ]}\n  ]}\n]} /&gt;\n\n**`SKILL.md`:**\n```markdown\n---\nname: webapp-testing\ndescription: Guide for testing web applications using Playwright.\n             Use this when asked to create or run browser-based tests.\n---\n\n# Web Application Testing with Playwright\n\nWhen creating tests for this project, follow these patterns:\n\n## Test Structure\n- Use `describe` blocks for feature groupings\n- Use `test` for individual test cases\n- Always include setup and teardown\n\n## Assertions\n- Prefer `toBeVisible()` over `toHaveCount(1)`\n- Use `waitFor` for async operations\n- Include accessibility checks\n\n## Example Template\nReference the [test template](./test-template.js) for the standard structure.\n\n## Naming Convention\n- Test files: `*.spec.ts`\n- Test descriptions: \&quot;should [expected behavior] when [condition]\&quot;\n```\n\nNow when you ask *\&quot;Write Playwright tests for the login form\&quot;*, Copilot automatically loads this skill and follows your project&#39;s testing conventions.\n\n### Loading Skills from Custom Locations\n\nFor teams sharing skills across repos, use the new setting:\n\n```json\n{\n  \&quot;chat.agentSkillsLocations\&quot;: [\n    \&quot;.github/skills\&quot;,\n    \&quot;~/shared-skills\&quot;,\n    \&quot;/team/copilot-skills\&quot;\n  ]\n}\n```\n\n### Extension-Contributed Skills\n\nExtensions can now contribute skills via their `package.json`:\n\n```json\n{\n  \&quot;contributes\&quot;: {\n    \&quot;copilotSkills\&quot;: [\n      {\n        \&quot;name\&quot;: \&quot;docker-compose\&quot;,\n        \&quot;description\&quot;: \&quot;Helps create and debug Docker Compose configurations\&quot;,\n        \&quot;path\&quot;: \&quot;./skills/docker-compose\&quot;\n      }\n    ]\n  }\n}\n```\n\nOr dynamically via the new API:\n\n```typescript\nvscode.chat.registerSkill({\n  name: &#39;dynamic-skill&#39;,\n  description: &#39;A skill registered at runtime&#39;,\n  async getInstructions(context) {\n    // Return context-aware instructions\n    return generateInstructionsFor(context.workspace);\n  }\n});\n```\n\n---\n\n## Instruction Files Work Everywhere\n\nInstruction files now apply to **non-coding tasks** like code exploration, architecture explanation, and documentation. [#287152](https://github.com/microsoft/vscode/issues/287152)\n\n**Before:** Your `.github/copilot-instructions.md` was ignored when you asked *\&quot;Explain how authentication works in this codebase\&quot;*\n\n**After:** Those instructions are now read for all codebase-related work.\n\nThis aligns with the &lt;InternalLink slug=\&quot;stop-bloating-your-claude-md-progressive-disclosure-ai-coding-tools\&quot;&gt;progressive disclosure approach&lt;/InternalLink&gt; where context is loaded on-demand rather than crammed into a single file.\n\n**Example `copilot-instructions.md`:**\n```markdown\n# Project Context\n\nThis is a microservices architecture with:\n- API Gateway (Node.js/Express)\n- Auth Service (Go)\n- User Service (Python/FastAPI)\n- Shared message queue (RabbitMQ)\n\nWhen explaining code:\n- Always mention which service a file belongs to\n- Reference the architecture diagram at docs/architecture.md\n- Note any cross-service dependencies\n```\n\nNow *\&quot;How does user registration work?\&quot;* will include this context automatically.\n\n---\n\n## Claude Code Gets Extended Thinking\n\nThe Claude Code integration now supports **extended thinking**, showing Claude&#39;s chain-of-thought reasoning in a collapsible section. [#287658](https://github.com/microsoft/vscode/issues/287658)\n\n**Related:** [Issue #266962 - Claude agent support](https://github.com/microsoft/vscode/issues/266962), [#287933 - Model picker support](https://github.com/microsoft/vscode/issues/287933)\n\n### What It Looks Like\n\nWhen you ask Claude to solve a complex problem, you&#39;ll see:\n\n```\n▼ Thinking...\n  Let me analyze the codebase structure first. I see there are\n  three main modules: auth, api, and database. The user is asking\n  about the authentication flow, so I should trace the request\n  from the API gateway through to the auth service...\n\n  The JWT validation happens in middleware/auth.ts, but the token\n  generation is in services/auth/token.go. I need to explain how\n  these connect via the shared Redis cache...\n\nHere&#39;s how authentication works in your codebase:\n[Final response]\n```\n\n### Configuration\n\nEnable/disable thinking display in settings:\n```json\n{\n  \&quot;github.copilot.chat.claude.showThinking\&quot;: true\n}\n```\n\n### Model Picker\n\nYou can now select which Claude model to use:\n\n1. Open the Chat view\n2. Click the model selector dropdown\n3. Choose from available Claude models (Sonnet, Opus, etc.)\n\nDifferent models offer different speed/capability tradeoffs—use faster models for simple tasks, more capable models for complex reasoning.\n\n---\n\n## Terminal Gets Major Upgrades\n\nThe integrated terminal received significant keyboard handling improvements this release, with two new protocol implementations.\n\n**Related PRs:**\n- [PR #286897 - xterm.js 6.1.0 with kitty keyboard and win32-input-mode](https://github.com/microsoft/vscode/pull/286897)\n- [Issue #286809 - Kitty keyboard protocol support](https://github.com/microsoft/vscode/issues/286809)\n- [Issue #286896 - Win32 input mode support](https://github.com/microsoft/vscode/issues/286896)\n- [xterm.js PR #5600 - Implement kitty keyboard protocol](https://github.com/xtermjs/xterm.js/pull/5600) (upstream)\n\n### Kitty Keyboard Protocol (CSI u)\n\nVS Code&#39;s terminal now supports the [kitty keyboard protocol](https://sw.kovidgoyal.net/kitty/keyboard-protocol/), enabling more sophisticated keyboard input handling. This unlocks previously unavailable key combinations and provides better support for terminal applications that use this modern standard.\n\n**Important:** This feature is **disabled by default** as it&#39;s experimental. Enable it in settings:\n\n```json\n{\n  \&quot;terminal.integrated.enableKittyKeyboardProtocol\&quot;: true\n}\n```\n\nThe protocol improves handling of modifiers, key events, repeat detection, and escape sequences—particularly useful if you use tools like fish shell, neovim, or other terminal applications that support CSI u.\n\n### Win32 Input Mode\n\nFor Windows users, the terminal now supports win32-input-mode, improving keyboard handling compatibility with Windows console applications. VT sequences alone can&#39;t send everything that Windows console programs expect (encoded as win32 INPUT_RECORDs), so this mode bridges that gap.\n\n**Also disabled by default.** Enable with:\n\n```json\n{\n  \&quot;terminal.integrated.enableWin32InputMode\&quot;: true\n}\n```\n\n### Terminal Command Output Streams Inline\n\nWhen using Copilot in agent mode, terminal command output now streams inline inside the Chat view instead of requiring you to switch to the terminal panel. [#257468](https://github.com/microsoft/vscode/issues/257468) The output auto-expands on command execution and collapses on success [#287664](https://github.com/microsoft/vscode/issues/287664)—keeping you focused on the conversation flow.\n\n### Terminal Timeout Parameter\n\nThe terminal tool now supports a timeout parameter to control how long commands run before timing out. [#286598](https://github.com/microsoft/vscode/issues/286598) This prevents unnecessary polling and gives you more control over long-running operations.\n\n### Terminal Command Sandboxing\n\nTerminal command sandboxing is now available for **macOS and Linux** [#277286](https://github.com/microsoft/vscode/issues/277286), adding an extra layer of security when running commands through the terminal tool.\n\n### Syntax Highlighting in Confirmation Dialogs\n\nThe terminal tool now presents Python, Node.js, and Ruby commands with syntax highlighting in the confirmation dialog [#287772](https://github.com/microsoft/vscode/issues/287772), [#287773](https://github.com/microsoft/vscode/issues/287773), [#288360](https://github.com/microsoft/vscode/issues/288360)—making it easier to review commands before execution.\n\n### Expanded Auto-Approved Commands\n\nMore commands are now automatically approved for execution:\n- `dir` in PowerShell [#288431](https://github.com/microsoft/vscode/issues/288431)\n- `sed -i` when editing files within the workspace [#288318](https://github.com/microsoft/vscode/issues/288318)\n- `od`, `xxd`, and safe `docker` commands [#287652](https://github.com/microsoft/vscode/issues/287652)\n\n### SGR 221/222 Escape Sequences\n\nThe terminal now supports SGR 221 and 222 escape sequences [#286810](https://github.com/microsoft/vscode/issues/286810), allowing independent control of bold and faint text attributes for more granular formatting.\n\n---\n\n## MCP Gets More Powerful\n\nModel Context Protocol continues to evolve with significant new capabilities.\n\n### Dynamic Context Updates\n\nMCP apps now support model context update methods, enabling servers to update the context model dynamically. [#289473](https://github.com/microsoft/vscode/issues/289473) This means MCP servers can push new context to your chat sessions without requiring a refresh.\n\n### Custom Package Registries\n\nAdded support for `registryBaseUrl` in MCP packages [#287549](https://github.com/microsoft/vscode/issues/287549), allowing teams to use private package registries for their MCP servers.\n\n### Built-in MCP Apps Support\n\nBuilt-in support for MCP Apps enables servers to provide custom UI for tool invocation. [#260218](https://github.com/microsoft/vscode/issues/260218) This opens the door for richer, more interactive MCP experiences beyond simple text-based tools.\n\n---\n\n## Quality of Life Improvements\n\n### Codex Agent in Dropdown\n\nThe OpenAI Codex agent now appears directly in the agents dropdown [#289040](https://github.com/microsoft/vscode/issues/289040) for quick access:\n\n```\nAgents ▼\n├── Local Agent\n├── Background Agent\n├── Cloud Agent\n└── Codex Agent       ← New!\n```\n\n### New MCP Server Command\n\nA new `workbench.mcp.startServer` command [#283959](https://github.com/microsoft/vscode/issues/283959) lets you programmatically start specific or all MCP servers to discover their tools. This is useful for automation scenarios where you need to ensure servers are running before invoking their tools.\n\n### The `/clear` Command Archives Sessions\n\nThe `/clear` command now archives the current session and starts a new one automatically [#285854](https://github.com/microsoft/vscode/issues/285854)—no more losing your chat history when you want a fresh start.\n\n### New Local Chat Command\n\nA new \&quot;New Local Chat\&quot; command [#288467](https://github.com/microsoft/vscode/issues/288467) lets you start a local chat session quickly.\n\n### Chat Session Imports\n\nYou can now **import** a chat session directly into the Chat view [#283954](https://github.com/microsoft/vscode/issues/283954), instead of only being able to open it in a new editor tab. This makes it easier to continue conversations from exported sessions.\n\n### Chat Session Exports with MCP Info\n\nExported sessions now include &lt;InternalLink slug=\&quot;what-is-model-context-protocol-mcp\&quot;&gt;MCP server&lt;/InternalLink&gt; configuration [#283945](https://github.com/microsoft/vscode/issues/283945):\n\n```json\n{\n  \&quot;session\&quot;: {\n    \&quot;messages\&quot;: [...],\n    \&quot;mcpServers\&quot;: [\n      {\n        \&quot;name\&quot;: \&quot;github\&quot;,\n        \&quot;url\&quot;: \&quot;https://mcp.github.com\&quot;,\n        \&quot;tools\&quot;: [\&quot;search_issues\&quot;, \&quot;get_pr\&quot;, \&quot;list_repos\&quot;]\n      }\n    ]\n  }\n}\n```\n\nThis makes sessions reproducible—share them with teammates and they can recreate your exact setup.\n\n### Multi-Select in Sessions View\n\nSelect multiple chat sessions with `Cmd/Ctrl+Click` [#288448](https://github.com/microsoft/vscode/issues/288448):\n- Archive all selected\n- Mark all as read\n- Batch delete\n\nAdditional session management improvements include \&quot;Mark All Read\&quot;, \&quot;Archive All\&quot;, and \&quot;Unarchive All\&quot; actions in context menus [#288147](https://github.com/microsoft/vscode/issues/288147), and increased locally persisted chat sessions [#283123](https://github.com/microsoft/vscode/issues/283123).\n\n### Resizable Sessions Sidebar\n\nYou can now resize the sessions sidebar in the Chat view by dragging the separator [#281258](https://github.com/microsoft/vscode/issues/281258), similar to how terminal tabs work.\n\n### Extension Context Tooltips\n\nHover over extension-contributed context items to see additional information about what they provide. [#280658](https://github.com/microsoft/vscode/issues/280658)\n\n### Accessible View Streams Thinking Content\n\nThe Accessible View now dynamically streams thinking content [#289223](https://github.com/microsoft/vscode/issues/289223), making Claude&#39;s chain-of-thought reasoning accessible to screen reader users in real-time.\n\n### Multi-Model Selection in Language Models Editor\n\nSelect multiple models in the Language Models editor and toggle their visibility at once [#287511](https://github.com/microsoft/vscode/issues/287511). Enterprise and Business users also get access to the Manage Models action [#287814](https://github.com/microsoft/vscode/issues/287814).\n\n---\n\n## Editor &amp; Language Improvements\n\n### Improved Shebang Detection\n\nVS Code now recognizes Deno, Bun, and other modern JavaScript runtimes [#287819](https://github.com/microsoft/vscode/issues/287819) for better language detection when opening scripts.\n\n### Better Ghost Text Visibility\n\nImproved visibility of ghost text in next edit suggestions [#284517](https://github.com/microsoft/vscode/issues/284517), making it easier to distinguish AI suggestions from regular text.\n\n### Double-Click Selects Block Content\n\nDouble-clicking immediately after a curly brace or bracket now selects the content inside it [#9123](https://github.com/microsoft/vscode/issues/9123)—a small but impactful change for manipulating code blocks.\n\n### Match File Path Case Toggle\n\nA new \&quot;Match File Path Case\&quot; toggle in the Search view&#39;s \&quot;files to include\&quot; input [#10633](https://github.com/microsoft/vscode/issues/10633) lets you control whether file paths and glob patterns match case-sensitively.\n\n### Bracket Match Foreground Color\n\nNew `editorBracketMatch.foreground` theme color [#85775](https://github.com/microsoft/vscode/issues/85775) enables customization of matched bracket text color.\n\n### Parallel Build Tasks\n\nDependent build tasks can now run in parallel [#288439](https://github.com/microsoft/vscode/issues/288439), improving build performance for projects with multiple independent compilation steps.\n\n### Git Delete File Command\n\nA new \&quot;Git: Delete File\&quot; command [#111767](https://github.com/microsoft/vscode/issues/111767) performs `git rm` on the current file directly from the command palette.\n\n---\n\n## Try It Today\n\nHere&#39;s a quick workflow to test the new features:\n\n1. **Create a custom agent** at `.github/agents/researcher.md` with restricted tools\n2. **Create a skill** at `.github/skills/my-skill/SKILL.md`\n3. **Ask Copilot:** *\&quot;What skills and subagents do you have available?\&quot;*\n4. **Test parallel execution:** *\&quot;Use subagents to research three different topics simultaneously\&quot;*\n5. **Enable Claude thinking** and ask a complex architecture question\n\n---\n\n## Looking Ahead\n\nThese updates signal a clear direction: Copilot is evolving from a single-agent assistant into a **coordinated multi-agent system**. The combination of parallel subagents, constrained tool access, and shareable skills creates a foundation for sophisticated automated workflows.\n\nIf you&#39;re interested in building your own agent systems, check out &lt;InternalLink slug=\&quot;building-your-own-coding-agent-from-scratch\&quot;&gt;Building Your Own Coding Agent from Scratch&lt;/InternalLink&gt; for a hands-on guide to the underlying patterns.\n\nKey settings to know:\n```json\n{\n  \&quot;chat.useAgentSkills\&quot;: true,\n  \&quot;chat.agentSkillsLocations\&quot;: [\&quot;.github/skills\&quot;],\n  \&quot;chat.customAgentInSubagent.enabled\&quot;: true,\n  \&quot;github.copilot.chat.claude.showThinking\&quot;: true,\n  \&quot;terminal.integrated.enableKittyKeyboardProtocol\&quot;: true,\n  \&quot;terminal.integrated.enableWin32InputMode\&quot;: true\n}\n```\n\nThe ecosystem is about to get a lot more interesting.\n\n---\n\n## Related Pull Requests &amp; Issues\n\nFor those who want to dig into the implementation details:\n\n### Agent &amp; Skills\n- [#274630 - Parallel subagent execution](https://github.com/microsoft/vscode/issues/274630)\n- [#280704 - Agents define allowed subagents](https://github.com/microsoft/vscode/issues/280704)\n- [#288480 - Skills enabled by default](https://github.com/microsoft/vscode/issues/288480)\n- [#288483 - Extension-contributed skills via manifest](https://github.com/microsoft/vscode/issues/288483)\n- [#288486 - Dynamic skills API](https://github.com/microsoft/vscode/issues/288486)\n- [#282738 - Skills from custom locations](https://github.com/microsoft/vscode/issues/282738)\n\n### Claude Integration\n- [#287658 - Extended thinking support](https://github.com/microsoft/vscode/issues/287658)\n- [#287933 - Model picker for Claude](https://github.com/microsoft/vscode/issues/287933)\n- [#266962 - Claude agent support](https://github.com/microsoft/vscode/issues/266962)\n\n### Terminal\n- [#286809 - Kitty keyboard protocol](https://github.com/microsoft/vscode/issues/286809)\n- [#286896 - Win32 input mode](https://github.com/microsoft/vscode/issues/286896)\n- [#286810 - SGR 221/222 escape sequences](https://github.com/microsoft/vscode/issues/286810)\n- [#257468 - Terminal output streams inline](https://github.com/microsoft/vscode/issues/257468)\n- [#287664 - Auto-expand/collapse terminal output](https://github.com/microsoft/vscode/issues/287664)\n- [#277286 - Terminal sandboxing for macOS/Linux](https://github.com/microsoft/vscode/issues/277286)\n- [#286598 - Terminal timeout parameter](https://github.com/microsoft/vscode/issues/286598)\n- [#287772 - Python syntax highlighting in confirmations](https://github.com/microsoft/vscode/issues/287772)\n- [xterm.js #5600 - Kitty keyboard protocol](https://github.com/xtermjs/xterm.js/pull/5600)\n\n### MCP\n- [#289473 - Dynamic context updates](https://github.com/microsoft/vscode/issues/289473)\n- [#287549 - Custom package registries](https://github.com/microsoft/vscode/issues/287549)\n- [#260218 - Built-in MCP Apps](https://github.com/microsoft/vscode/issues/260218)\n- [#283959 - startServer command](https://github.com/microsoft/vscode/issues/283959)\n- [#283945 - MCP info in session exports](https://github.com/microsoft/vscode/issues/283945)\n\n### Chat &amp; Sessions\n- [#285854 - /clear archives sessions](https://github.com/microsoft/vscode/issues/285854)\n- [#288467 - New Local Chat command](https://github.com/microsoft/vscode/issues/288467)\n- [#283954 - Import chat sessions](https://github.com/microsoft/vscode/issues/283954)\n- [#288448 - Multi-select in sessions](https://github.com/microsoft/vscode/issues/288448)\n- [#281258 - Resizable sessions sidebar](https://github.com/microsoft/vscode/issues/281258)\n- [#283123 - Increased persisted sessions](https://github.com/microsoft/vscode/issues/283123)\n- [#289223 - Accessible View streams thinking](https://github.com/microsoft/vscode/issues/289223)\n\n### Editor &amp; Other\n- [#287819 - Improved shebang detection](https://github.com/microsoft/vscode/issues/287819)\n- [#284517 - Ghost text visibility](https://github.com/microsoft/vscode/issues/284517)\n- [#9123 - Double-click selects block content](https://github.com/microsoft/vscode/issues/9123)\n- [#10633 - Match file path case toggle](https://github.com/microsoft/vscode/issues/10633)\n- [#288439 - Parallel build tasks](https://github.com/microsoft/vscode/issues/288439)\n- [#111767 - Git Delete File command](https://github.com/microsoft/vscode/issues/111767)\n\n### Iteration Plan\n- [#286040 - January 2026 Iteration Plan](https://github.com/microsoft/vscode/issues/286040)\n\n---\n\n*These features are rolling out in VS Code Insiders (1.109) now, with stable release expected in early February. Note that some features like kitty keyboard protocol and win32-input-mode are disabled by default and require manual opt-in.*&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PostCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus-outline inline-flex items-center gap-1.5 rounded-md border border-skin-line bg-skin-card px-2.5 py-1.5 text-xs font-medium text-skin-base opacity-80 transition-all hover:border-skin-accent/50 hover:text-skin-accent hover:opacity-100" aria-label="Copy post as markdown" title="Copy post as markdown for AI/LLM"><svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg><span>Copy Post</span></button><!--astro:end--></astro-island> </div>  <article id="article" class="prose mx-auto mt-8 max-w-5xl astro-vj4tpspi"> <p>The past week has brought a wave of updates to VS Code’s Copilot experience, with major improvements to how agents work together, a new skills system, deeper Claude integration, and significant terminal enhancements. Here’s what you need to know—with concrete examples you can try today.</p>
<p>For those who want to dive deeper into the implementation details, I’ve included links to the relevant GitHub pull requests and issues throughout this post.</p>
<hr/>
<h2 id="subagents-get-smarter-and-faster">Subagents Get Smarter (and Faster)<a class="heading-link" aria-label="Link to section" href="#subagents-get-smarter-and-faster"><span class="heading-link-icon">#</span></a></h2>
<p>Two significant changes make subagents far more practical for complex workflows.</p>
<p><strong>Related:</strong> <a href="https://github.com/microsoft/vscode/issues/274630" rel="noopener noreferrer" target="_blank">Issue #274630 - Parallel subagent execution</a></p>
<h3 id="parallel-execution">Parallel Execution<a class="heading-link" aria-label="Link to section" href="#parallel-execution"><span class="heading-link-icon">#</span></a></h3>
<p>Previously, if you kicked off multiple <code>runSubagent</code> calls, they’d run one after another. Now they can run simultaneously when tasks are independent, dramatically reducing wait times for research and code review operations.</p>
<p><strong>Example prompt:</strong></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="plaintext"><code><span class="line"><span>Research the best approaches for:</span></span>
<span class="line"><span>1. Rate limiting in our REST API</span></span>
<span class="line"><span>2. Caching strategies for our database queries</span></span>
<span class="line"><span>3. Error handling patterns for our microservices</span></span>
<span class="line"><span></span></span>
<span class="line"><span>Use a subagent for each topic and compile the findings.</span></span></code><button type="button" class="copy" data-code="Research the best approaches for:
1. Rate limiting in our REST API
2. Caching strategies for our database queries
3. Error handling patterns for our microservices

Use a subagent for each topic and compile the findings." onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>With parallel execution, all three research subagents run concurrently instead of sequentially—cutting total wait time significantly.</p>
<figure class="max-w-4xl mx-auto "> <img src="/_astro/subAgentParallel.D9dF5SwX_Zjlk6o.webp" alt="Parallel subagent execution visualization" loading="lazy" decoding="async" fetchpriority="auto" width="608" height="386" class="w-full">  </figure>
<h3 id="fine-grained-tool-access">Fine-Grained Tool Access<a class="heading-link" aria-label="Link to section" href="#fine-grained-tool-access"><span class="heading-link-icon">#</span></a></h3>
<p>You can now constrain which tools a subagent can access. This is critical for safety-conscious workflows where you want AI help without the risk of unintended changes.</p>
<p><strong>Creating a custom agent with restricted tools:</strong></p>
<p>Create a file at <code>.github/agents/github-researcher.md</code>:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"><span style="color:#F7768E">name</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> github-researcher</span></span>
<span class="line"><span style="color:#F7768E">description</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Research agent with access to GitHub. Use for searching issues,</span></span>
<span class="line"><span style="color:#9ECE6A">             reading documentation, and gathering information. Cannot edit files.</span></span>
<span class="line"><span style="color:#F7768E">tools</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">read</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">search</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">web</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">github/*</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">]</span></span>
<span class="line"><span style="color:#F7768E">argument-hint</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> The research task to complete</span></span>
<span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">You are a research assistant with read-only access to the codebase and GitHub.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Your capabilities:</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Search and read files in the repository</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Search GitHub issues and pull requests</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Fetch web documentation</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">You cannot:</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Edit or create files</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Run terminal commands</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Make commits</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">When researching, provide citations and links to sources.</span></span></code><button type="button" class="copy" data-code="---
name: github-researcher
description: Research agent with access to GitHub. Use for searching issues,
             reading documentation, and gathering information. Cannot edit files.
tools: ['read', 'search', 'web', 'github/*']
argument-hint: The research task to complete
---

You are a research assistant with read-only access to the codebase and GitHub.

Your capabilities:
- Search and read files in the repository
- Search GitHub issues and pull requests
- Fetch web documentation

You cannot:
- Edit or create files
- Run terminal commands
- Make commits

When researching, provide citations and links to sources." onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>Now you can ask: <em>“Use a subagent to find all issues assigned to me about authentication and summarize them”</em> — and the subagent will be limited to read-only operations.</p>
<p>If you’ve used Claude Code’s subagent system, you’ll recognize this pattern—it’s similar to how <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/claude-code-customization-guide-claudemd-skills-subagents/" class="internal-link astro-3tyn5ojg"> Claude Code handles skills and subagents </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Claude Code Customization: CLAUDE.md, Slash Commands, Skills, and Subagents</span> <span class="preview-description astro-3tyn5ojg">The complete guide to customizing Claude Code. Compare CLAUDE.md, slash commands, skills, and subagents with practical examples showing when to use each.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">claude-code</span><span class="preview-tag astro-3tyn5ojg">ai</span><span class="preview-tag astro-3tyn5ojg">tooling</span> <span class="preview-tag-more astro-3tyn5ojg">+1</span> </span> <time class="preview-date astro-3tyn5ojg">Dec 21, 2025</time> </span> </span> </span>  <script>
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
</script> with tool restrictions.</p>
<h3 id="control-subagent-availability">Control Subagent Availability<a class="heading-link" aria-label="Link to section" href="#control-subagent-availability"><span class="heading-link-icon">#</span></a></h3>
<p>Use the <code>infer</code> attribute to control whether an agent can be used as a subagent:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"><span style="color:#F7768E">name</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> dangerous-deployer</span></span>
<span class="line"><span style="color:#F7768E">description</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Handles production deployments</span></span>
<span class="line"><span style="color:#F7768E">tools</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">execute</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">edit</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">read</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">]</span></span>
<span class="line"><span style="color:#F7768E">infer</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> false</span><span style="color:#51597D;font-style:italic">  # This agent cannot be auto-invoked as a subagent</span></span>
<span class="line"><span style="color:#89DDFF">---</span></span></code><button type="button" class="copy" data-code="---
name: dangerous-deployer
description: Handles production deployments
tools: ['execute', 'edit', 'read']
infer: false  # This agent cannot be auto-invoked as a subagent
---" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr/>
<h2 id="skills-are-now-a-first-class-feature">Skills Are Now a First-Class Feature<a class="heading-link" aria-label="Link to section" href="#skills-are-now-a-first-class-feature"><span class="heading-link-icon">#</span></a></h2>
<p>Skills are now <strong>enabled by default</strong> for all users. They’re folders containing instructions and resources that Copilot loads on-demand when relevant to your task.</p>
<p><strong>Related PRs:</strong></p>
<ul>
<li><a href="https://github.com/microsoft/vscode/issues/286237" rel="noopener noreferrer" target="_blank">Issue #286237 - Custom agent improvements</a></li>
<li><a href="https://github.com/microsoft/vscode/issues/286238" rel="noopener noreferrer" target="_blank">Issue #286238 - Skill lookup enhancements</a></li>
<li><a href="https://github.com/microsoft/vscode-copilot-chat/pull/3082" rel="noopener noreferrer" target="_blank">PR #3082 - Implement agent using CustomAgentProvider API</a></li>
</ul>
<h3 id="creating-your-first-skill">Creating Your First Skill<a class="heading-link" aria-label="Link to section" href="#creating-your-first-skill"><span class="heading-link-icon">#</span></a></h3>
<p>Create a directory structure:</p>
<nav class="file-tree astro-htwbjus4" aria-label="File tree"> <ul class="file-tree__list astro-htwbjus4"> <li class="file-tree__item astro-o25vlg2d" style="--level: 0;"> <details class="file-tree__folder astro-o25vlg2d"> <summary class="astro-o25vlg2d"> <span class="file-tree__caret astro-o25vlg2d" aria-hidden="true">
▸
</span> <svg class="file-tree__icon astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">.github</span>  </summary> <ul class="file-tree__list astro-o25vlg2d"> <li class="file-tree__item astro-o25vlg2d" style="--level: 1;"> <details class="file-tree__folder astro-o25vlg2d"> <summary class="astro-o25vlg2d"> <span class="file-tree__caret astro-o25vlg2d" aria-hidden="true">
▸
</span> <svg class="file-tree__icon astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">skills</span>  </summary> <ul class="file-tree__list astro-o25vlg2d"> <li class="file-tree__item astro-o25vlg2d" style="--level: 2;"> <details class="file-tree__folder astro-o25vlg2d"> <summary class="astro-o25vlg2d"> <span class="file-tree__caret astro-o25vlg2d" aria-hidden="true">
▸
</span> <svg class="file-tree__icon astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">webapp-testing</span>  </summary> <ul class="file-tree__list astro-o25vlg2d"> <li class="file-tree__item astro-o25vlg2d" style="--level: 3;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#519ABA" d="M22.27 19.385H1.73A1.73 1.73 0 010 17.655V6.345a1.73 1.73 0 011.73-1.73h20.54A1.73 1.73 0 0124 6.345v11.308a1.73 1.73 0 01-1.73 1.731zM5.769 15.923v-4.5l2.308 2.885 2.307-2.885v4.5h2.308V8.078h-2.308l-2.307 2.885-2.308-2.885H3.46v7.847zM21.232 12h-2.309V8.077h-2.307V12h-2.308l3.461 4.039z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">SKILL.md</span> <span class="file-tree__comment astro-o25vlg2d">// Instructions</span> </span> </li> <li class="file-tree__item astro-o25vlg2d" style="--level: 3;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#F7DF1E" d="M0 0h24v24H0V0zm22.034 18.276c-.175-1.095-.888-2.015-3.003-2.873-.736-.345-1.554-.585-1.797-1.14-.091-.33-.105-.51-.046-.705.15-.646.915-.84 1.515-.66.39.12.75.42.976.9 1.034-.676 1.034-.676 1.755-1.125-.27-.42-.404-.601-.586-.78-.63-.705-1.469-1.065-2.834-1.034l-.705.089c-.676.165-1.32.525-1.71 1.005-1.14 1.291-.811 3.541.569 4.471 1.365 1.02 3.361 1.244 3.616 2.205.24 1.17-.87 1.545-1.966 1.41-.811-.18-1.26-.586-1.755-1.336l-1.83 1.051c.21.48.45.689.81 1.109 1.74 1.756 6.09 1.666 6.871-1.004.029-.09.24-.705.074-1.65l.046.067zm-8.983-7.245h-2.248c0 1.938-.009 3.864-.009 5.805 0 1.232.063 2.363-.138 2.711-.33.689-1.18.601-1.566.48-.396-.196-.597-.466-.83-.855-.063-.105-.11-.196-.127-.196l-1.825 1.125c.305.63.75 1.172 1.324 1.517.855.51 2.004.675 3.207.405.783-.226 1.458-.691 1.811-1.411.51-.93.402-2.07.397-3.346.012-2.054 0-4.109 0-6.179l.004-.056z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">test-template.js</span> <span class="file-tree__comment astro-o25vlg2d">// Example template</span> </span> </li>  </ul> </details>   </li>  </ul> </details>   </li>  </ul> </details>   </li>  </ul> </nav> 
<p><strong><code>SKILL.md</code>:</strong></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"><span style="color:#F7768E">name</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> webapp-testing</span></span>
<span class="line"><span style="color:#F7768E">description</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Guide for testing web applications using Playwright.</span></span>
<span class="line"><span style="color:#9ECE6A">             Use this when asked to create or run browser-based tests.</span></span>
<span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF;font-weight:bold">#</span><span style="color:#89DDFF;font-weight:bold"> Web Application Testing with Playwright</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">When creating tests for this project, follow these patterns:</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Test Structure</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Use </span><span style="color:#89DDFF">`describe`</span><span style="color:#9AA5CE"> blocks for feature groupings</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Use </span><span style="color:#89DDFF">`test`</span><span style="color:#9AA5CE"> for individual test cases</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Always include setup and teardown</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Assertions</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Prefer </span><span style="color:#89DDFF">`toBeVisible()`</span><span style="color:#9AA5CE"> over </span><span style="color:#89DDFF">`toHaveCount(1)`</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Use </span><span style="color:#89DDFF">`waitFor`</span><span style="color:#9AA5CE"> for async operations</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Include accessibility checks</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Example Template</span></span>
<span class="line"><span style="color:#9AA5CE">Reference the </span><span style="color:#89DDFF">[</span><span style="color:#73DACA">test template</span><span style="color:#89DDFF">](</span><span style="color:#73DACA;text-decoration:underline">./test-template.js</span><span style="color:#89DDFF">)</span><span style="color:#9AA5CE"> for the standard structure.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Naming Convention</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Test files: </span><span style="color:#89DDFF">`*.spec.ts`</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Test descriptions: &quot;should [expected behavior] when </span><span style="color:#89DDFF">[</span><span style="color:#73DACA">condition</span><span style="color:#89DDFF">]</span><span style="color:#9AA5CE">&quot;</span></span></code><button type="button" class="copy" data-code="---
name: webapp-testing
description: Guide for testing web applications using Playwright.
             Use this when asked to create or run browser-based tests.
---

# Web Application Testing with Playwright

When creating tests for this project, follow these patterns:

## Test Structure
- Use `describe` blocks for feature groupings
- Use `test` for individual test cases
- Always include setup and teardown

## Assertions
- Prefer `toBeVisible()` over `toHaveCount(1)`
- Use `waitFor` for async operations
- Include accessibility checks

## Example Template
Reference the [test template](./test-template.js) for the standard structure.

## Naming Convention
- Test files: `*.spec.ts`
- Test descriptions: &#34;should [expected behavior] when [condition]&#34;" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>Now when you ask <em>“Write Playwright tests for the login form”</em>, Copilot automatically loads this skill and follows your project’s testing conventions.</p>
<h3 id="loading-skills-from-custom-locations">Loading Skills from Custom Locations<a class="heading-link" aria-label="Link to section" href="#loading-skills-from-custom-locations"><span class="heading-link-icon">#</span></a></h3>
<p>For teams sharing skills across repos, use the new setting:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="json"><code><span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">chat.agentSkillsLocations</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span></span>
<span class="line"><span style="color:#89DDFF">    &quot;</span><span style="color:#9ECE6A">.github/skills</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">    &quot;</span><span style="color:#9ECE6A">~/shared-skills</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">    &quot;</span><span style="color:#9ECE6A">/team/copilot-skills</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#9ABDF5">  ]</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="{
  &#34;chat.agentSkillsLocations&#34;: [
    &#34;.github/skills&#34;,
    &#34;~/shared-skills&#34;,
    &#34;/team/copilot-skills&#34;
  ]
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="extension-contributed-skills">Extension-Contributed Skills<a class="heading-link" aria-label="Link to section" href="#extension-contributed-skills"><span class="heading-link-icon">#</span></a></h3>
<p>Extensions can now contribute skills via their <code>package.json</code>:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="json"><code><span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">contributes</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">    &quot;</span><span style="color:#0DB9D7">copilotSkills</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span></span>
<span class="line"><span style="color:#9ABDF5">      {</span></span>
<span class="line"><span style="color:#89DDFF">        &quot;</span><span style="color:#7DCFFF">name</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">docker-compose</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">        &quot;</span><span style="color:#7DCFFF">description</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">Helps create and debug Docker Compose configurations</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">        &quot;</span><span style="color:#7DCFFF">path</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">./skills/docker-compose</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span></span>
<span class="line"><span style="color:#9ABDF5">    ]</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="{
  &#34;contributes&#34;: {
    &#34;copilotSkills&#34;: [
      {
        &#34;name&#34;: &#34;docker-compose&#34;,
        &#34;description&#34;: &#34;Helps create and debug Docker Compose configurations&#34;,
        &#34;path&#34;: &#34;./skills/docker-compose&#34;
      }
    ]
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>Or dynamically via the new API:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#C0CAF5">vscode</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">chat</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">registerSkill</span><span style="color:#9ABDF5">({</span></span>
<span class="line"><span style="color:#73DACA">  name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">dynamic-skill</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  description</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">A skill registered at runtime</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  async</span><span style="color:#7AA2F7"> getInstructions</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">context</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">    // Return context-aware instructions</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#7AA2F7"> generateInstructionsFor</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">context</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">workspace</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">})</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="vscode.chat.registerSkill({
  name: 'dynamic-skill',
  description: 'A skill registered at runtime',
  async getInstructions(context) {
    // Return context-aware instructions
    return generateInstructionsFor(context.workspace);
  }
});" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr/>
<h2 id="instruction-files-work-everywhere">Instruction Files Work Everywhere<a class="heading-link" aria-label="Link to section" href="#instruction-files-work-everywhere"><span class="heading-link-icon">#</span></a></h2>
<p>Instruction files now apply to <strong>non-coding tasks</strong> like code exploration, architecture explanation, and documentation. <a href="https://github.com/microsoft/vscode/issues/287152" rel="noopener noreferrer" target="_blank">#287152</a></p>
<p><strong>Before:</strong> Your <code>.github/copilot-instructions.md</code> was ignored when you asked <em>“Explain how authentication works in this codebase”</em></p>
<p><strong>After:</strong> Those instructions are now read for all codebase-related work.</p>
<p>This aligns with the <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/stop-bloating-your-claude-md-progressive-disclosure-ai-coding-tools/" class="internal-link astro-3tyn5ojg"> progressive disclosure approach </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Stop Bloating Your CLAUDE.md: Progressive Disclosure for AI Coding Tools</span> <span class="preview-description astro-3tyn5ojg">AI coding tools are stateless—every session starts fresh. The solution isn&#39;t cramming everything into CLAUDE.md, but building a layered context system where learnings accumulate in docs and specialized agents load on-demand.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">claude-code</span><span class="preview-tag astro-3tyn5ojg">ai-tools</span><span class="preview-tag astro-3tyn5ojg">developer-experience</span> <span class="preview-tag-more astro-3tyn5ojg">+1</span> </span> <time class="preview-date astro-3tyn5ojg">Jan 18, 2026</time> </span> </span> </span>  <script>
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
</script> where context is loaded on-demand rather than crammed into a single file.</p>
<p><strong>Example <code>copilot-instructions.md</code>:</strong></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF;font-weight:bold">#</span><span style="color:#89DDFF;font-weight:bold"> Project Context</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">This is a microservices architecture with:</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> API Gateway (Node.js/Express)</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Auth Service (Go)</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> User Service (Python/FastAPI)</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Shared message queue (RabbitMQ)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">When explaining code:</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Always mention which service a file belongs to</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Reference the architecture diagram at docs/architecture.md</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Note any cross-service dependencies</span></span></code><button type="button" class="copy" data-code="# Project Context

This is a microservices architecture with:
- API Gateway (Node.js/Express)
- Auth Service (Go)
- User Service (Python/FastAPI)
- Shared message queue (RabbitMQ)

When explaining code:
- Always mention which service a file belongs to
- Reference the architecture diagram at docs/architecture.md
- Note any cross-service dependencies" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>Now <em>“How does user registration work?”</em> will include this context automatically.</p>
<hr/>
<h2 id="claude-code-gets-extended-thinking">Claude Code Gets Extended Thinking<a class="heading-link" aria-label="Link to section" href="#claude-code-gets-extended-thinking"><span class="heading-link-icon">#</span></a></h2>
<p>The Claude Code integration now supports <strong>extended thinking</strong>, showing Claude’s chain-of-thought reasoning in a collapsible section. <a href="https://github.com/microsoft/vscode/issues/287658" rel="noopener noreferrer" target="_blank">#287658</a></p>
<p><strong>Related:</strong> <a href="https://github.com/microsoft/vscode/issues/266962" rel="noopener noreferrer" target="_blank">Issue #266962 - Claude agent support</a>, <a href="https://github.com/microsoft/vscode/issues/287933" rel="noopener noreferrer" target="_blank">#287933 - Model picker support</a></p>
<h3 id="what-it-looks-like">What It Looks Like<a class="heading-link" aria-label="Link to section" href="#what-it-looks-like"><span class="heading-link-icon">#</span></a></h3>
<p>When you ask Claude to solve a complex problem, you’ll see:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="plaintext"><code><span class="line"><span>▼ Thinking...</span></span>
<span class="line"><span>  Let me analyze the codebase structure first. I see there are</span></span>
<span class="line"><span>  three main modules: auth, api, and database. The user is asking</span></span>
<span class="line"><span>  about the authentication flow, so I should trace the request</span></span>
<span class="line"><span>  from the API gateway through to the auth service...</span></span>
<span class="line"><span></span></span>
<span class="line"><span>  The JWT validation happens in middleware/auth.ts, but the token</span></span>
<span class="line"><span>  generation is in services/auth/token.go. I need to explain how</span></span>
<span class="line"><span>  these connect via the shared Redis cache...</span></span>
<span class="line"><span></span></span>
<span class="line"><span>Here&#39;s how authentication works in your codebase:</span></span>
<span class="line"><span>[Final response]</span></span></code><button type="button" class="copy" data-code="▼ Thinking...
  Let me analyze the codebase structure first. I see there are
  three main modules: auth, api, and database. The user is asking
  about the authentication flow, so I should trace the request
  from the API gateway through to the auth service...

  The JWT validation happens in middleware/auth.ts, but the token
  generation is in services/auth/token.go. I need to explain how
  these connect via the shared Redis cache...

Here's how authentication works in your codebase:
[Final response]" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="configuration">Configuration<a class="heading-link" aria-label="Link to section" href="#configuration"><span class="heading-link-icon">#</span></a></h3>
<p>Enable/disable thinking display in settings:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="json"><code><span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">github.copilot.chat.claude.showThinking</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="{
  &#34;github.copilot.chat.claude.showThinking&#34;: true
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="model-picker">Model Picker<a class="heading-link" aria-label="Link to section" href="#model-picker"><span class="heading-link-icon">#</span></a></h3>
<p>You can now select which Claude model to use:</p>
<ol>
<li>Open the Chat view</li>
<li>Click the model selector dropdown</li>
<li>Choose from available Claude models (Sonnet, Opus, etc.)</li>
</ol>
<p>Different models offer different speed/capability tradeoffs—use faster models for simple tasks, more capable models for complex reasoning.</p>
<hr/>
<h2 id="terminal-gets-major-upgrades">Terminal Gets Major Upgrades<a class="heading-link" aria-label="Link to section" href="#terminal-gets-major-upgrades"><span class="heading-link-icon">#</span></a></h2>
<p>The integrated terminal received significant keyboard handling improvements this release, with two new protocol implementations.</p>
<p><strong>Related PRs:</strong></p>
<ul>
<li><a href="https://github.com/microsoft/vscode/pull/286897" rel="noopener noreferrer" target="_blank">PR #286897 - xterm.js 6.1.0 with kitty keyboard and win32-input-mode</a></li>
<li><a href="https://github.com/microsoft/vscode/issues/286809" rel="noopener noreferrer" target="_blank">Issue #286809 - Kitty keyboard protocol support</a></li>
<li><a href="https://github.com/microsoft/vscode/issues/286896" rel="noopener noreferrer" target="_blank">Issue #286896 - Win32 input mode support</a></li>
<li><a href="https://github.com/xtermjs/xterm.js/pull/5600" rel="noopener noreferrer" target="_blank">xterm.js PR #5600 - Implement kitty keyboard protocol</a> (upstream)</li>
</ul>
<h3 id="kitty-keyboard-protocol-csi-u">Kitty Keyboard Protocol (CSI u)<a class="heading-link" aria-label="Link to section" href="#kitty-keyboard-protocol-csi-u"><span class="heading-link-icon">#</span></a></h3>
<p>VS Code’s terminal now supports the <a href="https://sw.kovidgoyal.net/kitty/keyboard-protocol/" rel="noopener noreferrer" target="_blank">kitty keyboard protocol</a>, enabling more sophisticated keyboard input handling. This unlocks previously unavailable key combinations and provides better support for terminal applications that use this modern standard.</p>
<p><strong>Important:</strong> This feature is <strong>disabled by default</strong> as it’s experimental. Enable it in settings:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="json"><code><span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">terminal.integrated.enableKittyKeyboardProtocol</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="{
  &#34;terminal.integrated.enableKittyKeyboardProtocol&#34;: true
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>The protocol improves handling of modifiers, key events, repeat detection, and escape sequences—particularly useful if you use tools like fish shell, neovim, or other terminal applications that support CSI u.</p>
<h3 id="win32-input-mode">Win32 Input Mode<a class="heading-link" aria-label="Link to section" href="#win32-input-mode"><span class="heading-link-icon">#</span></a></h3>
<p>For Windows users, the terminal now supports win32-input-mode, improving keyboard handling compatibility with Windows console applications. VT sequences alone can’t send everything that Windows console programs expect (encoded as win32 INPUT_RECORDs), so this mode bridges that gap.</p>
<p><strong>Also disabled by default.</strong> Enable with:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="json"><code><span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">terminal.integrated.enableWin32InputMode</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="{
  &#34;terminal.integrated.enableWin32InputMode&#34;: true
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="terminal-command-output-streams-inline">Terminal Command Output Streams Inline<a class="heading-link" aria-label="Link to section" href="#terminal-command-output-streams-inline"><span class="heading-link-icon">#</span></a></h3>
<p>When using Copilot in agent mode, terminal command output now streams inline inside the Chat view instead of requiring you to switch to the terminal panel. <a href="https://github.com/microsoft/vscode/issues/257468" rel="noopener noreferrer" target="_blank">#257468</a> The output auto-expands on command execution and collapses on success <a href="https://github.com/microsoft/vscode/issues/287664" rel="noopener noreferrer" target="_blank">#287664</a>—keeping you focused on the conversation flow.</p>
<h3 id="terminal-timeout-parameter">Terminal Timeout Parameter<a class="heading-link" aria-label="Link to section" href="#terminal-timeout-parameter"><span class="heading-link-icon">#</span></a></h3>
<p>The terminal tool now supports a timeout parameter to control how long commands run before timing out. <a href="https://github.com/microsoft/vscode/issues/286598" rel="noopener noreferrer" target="_blank">#286598</a> This prevents unnecessary polling and gives you more control over long-running operations.</p>
<h3 id="terminal-command-sandboxing">Terminal Command Sandboxing<a class="heading-link" aria-label="Link to section" href="#terminal-command-sandboxing"><span class="heading-link-icon">#</span></a></h3>
<p>Terminal command sandboxing is now available for <strong>macOS and Linux</strong> <a href="https://github.com/microsoft/vscode/issues/277286" rel="noopener noreferrer" target="_blank">#277286</a>, adding an extra layer of security when running commands through the terminal tool.</p>
<h3 id="syntax-highlighting-in-confirmation-dialogs">Syntax Highlighting in Confirmation Dialogs<a class="heading-link" aria-label="Link to section" href="#syntax-highlighting-in-confirmation-dialogs"><span class="heading-link-icon">#</span></a></h3>
<p>The terminal tool now presents Python, Node.js, and Ruby commands with syntax highlighting in the confirmation dialog <a href="https://github.com/microsoft/vscode/issues/287772" rel="noopener noreferrer" target="_blank">#287772</a>, <a href="https://github.com/microsoft/vscode/issues/287773" rel="noopener noreferrer" target="_blank">#287773</a>, <a href="https://github.com/microsoft/vscode/issues/288360" rel="noopener noreferrer" target="_blank">#288360</a>—making it easier to review commands before execution.</p>
<h3 id="expanded-auto-approved-commands">Expanded Auto-Approved Commands<a class="heading-link" aria-label="Link to section" href="#expanded-auto-approved-commands"><span class="heading-link-icon">#</span></a></h3>
<p>More commands are now automatically approved for execution:</p>
<ul>
<li><code>dir</code> in PowerShell <a href="https://github.com/microsoft/vscode/issues/288431" rel="noopener noreferrer" target="_blank">#288431</a></li>
<li><code>sed -i</code> when editing files within the workspace <a href="https://github.com/microsoft/vscode/issues/288318" rel="noopener noreferrer" target="_blank">#288318</a></li>
<li><code>od</code>, <code>xxd</code>, and safe <code>docker</code> commands <a href="https://github.com/microsoft/vscode/issues/287652" rel="noopener noreferrer" target="_blank">#287652</a></li>
</ul>
<h3 id="sgr-221222-escape-sequences">SGR 221/222 Escape Sequences<a class="heading-link" aria-label="Link to section" href="#sgr-221222-escape-sequences"><span class="heading-link-icon">#</span></a></h3>
<p>The terminal now supports SGR 221 and 222 escape sequences <a href="https://github.com/microsoft/vscode/issues/286810" rel="noopener noreferrer" target="_blank">#286810</a>, allowing independent control of bold and faint text attributes for more granular formatting.</p>
<hr/>
<h2 id="mcp-gets-more-powerful">MCP Gets More Powerful<a class="heading-link" aria-label="Link to section" href="#mcp-gets-more-powerful"><span class="heading-link-icon">#</span></a></h2>
<p>Model Context Protocol continues to evolve with significant new capabilities.</p>
<h3 id="dynamic-context-updates">Dynamic Context Updates<a class="heading-link" aria-label="Link to section" href="#dynamic-context-updates"><span class="heading-link-icon">#</span></a></h3>
<p>MCP apps now support model context update methods, enabling servers to update the context model dynamically. <a href="https://github.com/microsoft/vscode/issues/289473" rel="noopener noreferrer" target="_blank">#289473</a> This means MCP servers can push new context to your chat sessions without requiring a refresh.</p>
<h3 id="custom-package-registries">Custom Package Registries<a class="heading-link" aria-label="Link to section" href="#custom-package-registries"><span class="heading-link-icon">#</span></a></h3>
<p>Added support for <code>registryBaseUrl</code> in MCP packages <a href="https://github.com/microsoft/vscode/issues/287549" rel="noopener noreferrer" target="_blank">#287549</a>, allowing teams to use private package registries for their MCP servers.</p>
<h3 id="built-in-mcp-apps-support">Built-in MCP Apps Support<a class="heading-link" aria-label="Link to section" href="#built-in-mcp-apps-support"><span class="heading-link-icon">#</span></a></h3>
<p>Built-in support for MCP Apps enables servers to provide custom UI for tool invocation. <a href="https://github.com/microsoft/vscode/issues/260218" rel="noopener noreferrer" target="_blank">#260218</a> This opens the door for richer, more interactive MCP experiences beyond simple text-based tools.</p>
<hr/>
<h2 id="quality-of-life-improvements">Quality of Life Improvements<a class="heading-link" aria-label="Link to section" href="#quality-of-life-improvements"><span class="heading-link-icon">#</span></a></h2>
<h3 id="codex-agent-in-dropdown">Codex Agent in Dropdown<a class="heading-link" aria-label="Link to section" href="#codex-agent-in-dropdown"><span class="heading-link-icon">#</span></a></h3>
<p>The OpenAI Codex agent now appears directly in the agents dropdown <a href="https://github.com/microsoft/vscode/issues/289040" rel="noopener noreferrer" target="_blank">#289040</a> for quick access:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="plaintext"><code><span class="line"><span>Agents ▼</span></span>
<span class="line"><span>├── Local Agent</span></span>
<span class="line"><span>├── Background Agent</span></span>
<span class="line"><span>├── Cloud Agent</span></span>
<span class="line"><span>└── Codex Agent       ← New!</span></span></code><button type="button" class="copy" data-code="Agents ▼
├── Local Agent
├── Background Agent
├── Cloud Agent
└── Codex Agent       ← New!" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="new-mcp-server-command">New MCP Server Command<a class="heading-link" aria-label="Link to section" href="#new-mcp-server-command"><span class="heading-link-icon">#</span></a></h3>
<p>A new <code>workbench.mcp.startServer</code> command <a href="https://github.com/microsoft/vscode/issues/283959" rel="noopener noreferrer" target="_blank">#283959</a> lets you programmatically start specific or all MCP servers to discover their tools. This is useful for automation scenarios where you need to ensure servers are running before invoking their tools.</p>
<h3 id="the-clear-command-archives-sessions">The <code>/clear</code> Command Archives Sessions<a class="heading-link" aria-label="Link to section" href="#the-clear-command-archives-sessions"><span class="heading-link-icon">#</span></a></h3>
<p>The <code>/clear</code> command now archives the current session and starts a new one automatically <a href="https://github.com/microsoft/vscode/issues/285854" rel="noopener noreferrer" target="_blank">#285854</a>—no more losing your chat history when you want a fresh start.</p>
<h3 id="new-local-chat-command">New Local Chat Command<a class="heading-link" aria-label="Link to section" href="#new-local-chat-command"><span class="heading-link-icon">#</span></a></h3>
<p>A new “New Local Chat” command <a href="https://github.com/microsoft/vscode/issues/288467" rel="noopener noreferrer" target="_blank">#288467</a> lets you start a local chat session quickly.</p>
<h3 id="chat-session-imports">Chat Session Imports<a class="heading-link" aria-label="Link to section" href="#chat-session-imports"><span class="heading-link-icon">#</span></a></h3>
<p>You can now <strong>import</strong> a chat session directly into the Chat view <a href="https://github.com/microsoft/vscode/issues/283954" rel="noopener noreferrer" target="_blank">#283954</a>, instead of only being able to open it in a new editor tab. This makes it easier to continue conversations from exported sessions.</p>
<h3 id="chat-session-exports-with-mcp-info">Chat Session Exports with MCP Info<a class="heading-link" aria-label="Link to section" href="#chat-session-exports-with-mcp-info"><span class="heading-link-icon">#</span></a></h3>
<p>Exported sessions now include <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/what-is-model-context-protocol-mcp/" class="internal-link astro-3tyn5ojg"> MCP server </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">What Is the Model Context Protocol (MCP)? How It Works</span> <span class="preview-description astro-3tyn5ojg">Learn how MCP (Model Context Protocol) standardizes AI tool integration, enabling LLMs to interact with external services, databases, and APIs through a universal protocol similar to USB-C for AI applications.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">mcp</span><span class="preview-tag astro-3tyn5ojg">typescript</span><span class="preview-tag astro-3tyn5ojg">ai</span>  </span> <time class="preview-date astro-3tyn5ojg">Aug 10, 2025</time> </span> </span> </span>  <script>
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
</script> configuration <a href="https://github.com/microsoft/vscode/issues/283945" rel="noopener noreferrer" target="_blank">#283945</a>:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="json"><code><span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">session</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">    &quot;</span><span style="color:#0DB9D7">messages</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#FF5370">...</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">    &quot;</span><span style="color:#0DB9D7">mcpServers</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span></span>
<span class="line"><span style="color:#9ABDF5">      {</span></span>
<span class="line"><span style="color:#89DDFF">        &quot;</span><span style="color:#7DCFFF">name</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">github</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">        &quot;</span><span style="color:#7DCFFF">url</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">https://mcp.github.com</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">        &quot;</span><span style="color:#7DCFFF">tools</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">search_issues</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">get_pr</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">list_repos</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">]</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span></span>
<span class="line"><span style="color:#9ABDF5">    ]</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="{
  &#34;session&#34;: {
    &#34;messages&#34;: [...],
    &#34;mcpServers&#34;: [
      {
        &#34;name&#34;: &#34;github&#34;,
        &#34;url&#34;: &#34;https://mcp.github.com&#34;,
        &#34;tools&#34;: [&#34;search_issues&#34;, &#34;get_pr&#34;, &#34;list_repos&#34;]
      }
    ]
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>This makes sessions reproducible—share them with teammates and they can recreate your exact setup.</p>
<h3 id="multi-select-in-sessions-view">Multi-Select in Sessions View<a class="heading-link" aria-label="Link to section" href="#multi-select-in-sessions-view"><span class="heading-link-icon">#</span></a></h3>
<p>Select multiple chat sessions with <code>Cmd/Ctrl+Click</code> <a href="https://github.com/microsoft/vscode/issues/288448" rel="noopener noreferrer" target="_blank">#288448</a>:</p>
<ul>
<li>Archive all selected</li>
<li>Mark all as read</li>
<li>Batch delete</li>
</ul>
<p>Additional session management improvements include “Mark All Read”, “Archive All”, and “Unarchive All” actions in context menus <a href="https://github.com/microsoft/vscode/issues/288147" rel="noopener noreferrer" target="_blank">#288147</a>, and increased locally persisted chat sessions <a href="https://github.com/microsoft/vscode/issues/283123" rel="noopener noreferrer" target="_blank">#283123</a>.</p>
<h3 id="resizable-sessions-sidebar">Resizable Sessions Sidebar<a class="heading-link" aria-label="Link to section" href="#resizable-sessions-sidebar"><span class="heading-link-icon">#</span></a></h3>
<p>You can now resize the sessions sidebar in the Chat view by dragging the separator <a href="https://github.com/microsoft/vscode/issues/281258" rel="noopener noreferrer" target="_blank">#281258</a>, similar to how terminal tabs work.</p>
<h3 id="extension-context-tooltips">Extension Context Tooltips<a class="heading-link" aria-label="Link to section" href="#extension-context-tooltips"><span class="heading-link-icon">#</span></a></h3>
<p>Hover over extension-contributed context items to see additional information about what they provide. <a href="https://github.com/microsoft/vscode/issues/280658" rel="noopener noreferrer" target="_blank">#280658</a></p>
<h3 id="accessible-view-streams-thinking-content">Accessible View Streams Thinking Content<a class="heading-link" aria-label="Link to section" href="#accessible-view-streams-thinking-content"><span class="heading-link-icon">#</span></a></h3>
<p>The Accessible View now dynamically streams thinking content <a href="https://github.com/microsoft/vscode/issues/289223" rel="noopener noreferrer" target="_blank">#289223</a>, making Claude’s chain-of-thought reasoning accessible to screen reader users in real-time.</p>
<h3 id="multi-model-selection-in-language-models-editor">Multi-Model Selection in Language Models Editor<a class="heading-link" aria-label="Link to section" href="#multi-model-selection-in-language-models-editor"><span class="heading-link-icon">#</span></a></h3>
<p>Select multiple models in the Language Models editor and toggle their visibility at once <a href="https://github.com/microsoft/vscode/issues/287511" rel="noopener noreferrer" target="_blank">#287511</a>. Enterprise and Business users also get access to the Manage Models action <a href="https://github.com/microsoft/vscode/issues/287814" rel="noopener noreferrer" target="_blank">#287814</a>.</p>
<hr/>
<h2 id="editor--language-improvements">Editor &amp; Language Improvements<a class="heading-link" aria-label="Link to section" href="#editor--language-improvements"><span class="heading-link-icon">#</span></a></h2>
<h3 id="improved-shebang-detection">Improved Shebang Detection<a class="heading-link" aria-label="Link to section" href="#improved-shebang-detection"><span class="heading-link-icon">#</span></a></h3>
<p>VS Code now recognizes Deno, Bun, and other modern JavaScript runtimes <a href="https://github.com/microsoft/vscode/issues/287819" rel="noopener noreferrer" target="_blank">#287819</a> for better language detection when opening scripts.</p>
<h3 id="better-ghost-text-visibility">Better Ghost Text Visibility<a class="heading-link" aria-label="Link to section" href="#better-ghost-text-visibility"><span class="heading-link-icon">#</span></a></h3>
<p>Improved visibility of ghost text in next edit suggestions <a href="https://github.com/microsoft/vscode/issues/284517" rel="noopener noreferrer" target="_blank">#284517</a>, making it easier to distinguish AI suggestions from regular text.</p>
<h3 id="double-click-selects-block-content">Double-Click Selects Block Content<a class="heading-link" aria-label="Link to section" href="#double-click-selects-block-content"><span class="heading-link-icon">#</span></a></h3>
<p>Double-clicking immediately after a curly brace or bracket now selects the content inside it <a href="https://github.com/microsoft/vscode/issues/9123" rel="noopener noreferrer" target="_blank">#9123</a>—a small but impactful change for manipulating code blocks.</p>
<h3 id="match-file-path-case-toggle">Match File Path Case Toggle<a class="heading-link" aria-label="Link to section" href="#match-file-path-case-toggle"><span class="heading-link-icon">#</span></a></h3>
<p>A new “Match File Path Case” toggle in the Search view’s “files to include” input <a href="https://github.com/microsoft/vscode/issues/10633" rel="noopener noreferrer" target="_blank">#10633</a> lets you control whether file paths and glob patterns match case-sensitively.</p>
<h3 id="bracket-match-foreground-color">Bracket Match Foreground Color<a class="heading-link" aria-label="Link to section" href="#bracket-match-foreground-color"><span class="heading-link-icon">#</span></a></h3>
<p>New <code>editorBracketMatch.foreground</code> theme color <a href="https://github.com/microsoft/vscode/issues/85775" rel="noopener noreferrer" target="_blank">#85775</a> enables customization of matched bracket text color.</p>
<h3 id="parallel-build-tasks">Parallel Build Tasks<a class="heading-link" aria-label="Link to section" href="#parallel-build-tasks"><span class="heading-link-icon">#</span></a></h3>
<p>Dependent build tasks can now run in parallel <a href="https://github.com/microsoft/vscode/issues/288439" rel="noopener noreferrer" target="_blank">#288439</a>, improving build performance for projects with multiple independent compilation steps.</p>
<h3 id="git-delete-file-command">Git Delete File Command<a class="heading-link" aria-label="Link to section" href="#git-delete-file-command"><span class="heading-link-icon">#</span></a></h3>
<p>A new “Git: Delete File” command <a href="https://github.com/microsoft/vscode/issues/111767" rel="noopener noreferrer" target="_blank">#111767</a> performs <code>git rm</code> on the current file directly from the command palette.</p>
<hr/>
<h2 id="try-it-today">Try It Today<a class="heading-link" aria-label="Link to section" href="#try-it-today"><span class="heading-link-icon">#</span></a></h2>
<p>Here’s a quick workflow to test the new features:</p>
<ol>
<li><strong>Create a custom agent</strong> at <code>.github/agents/researcher.md</code> with restricted tools</li>
<li><strong>Create a skill</strong> at <code>.github/skills/my-skill/SKILL.md</code></li>
<li><strong>Ask Copilot:</strong> <em>“What skills and subagents do you have available?”</em></li>
<li><strong>Test parallel execution:</strong> <em>“Use subagents to research three different topics simultaneously”</em></li>
<li><strong>Enable Claude thinking</strong> and ask a complex architecture question</li>
</ol>
<hr/>
<h2 id="looking-ahead">Looking Ahead<a class="heading-link" aria-label="Link to section" href="#looking-ahead"><span class="heading-link-icon">#</span></a></h2>
<p>These updates signal a clear direction: Copilot is evolving from a single-agent assistant into a <strong>coordinated multi-agent system</strong>. The combination of parallel subagents, constrained tool access, and shareable skills creates a foundation for sophisticated automated workflows.</p>
<p>If you’re interested in building your own agent systems, check out <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/building-your-own-coding-agent-from-scratch/" class="internal-link astro-3tyn5ojg"> Building Your Own Coding Agent from Scratch </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Building Your Own Coding Agent from Scratch</span> <span class="preview-description astro-3tyn5ojg">A practical guide to creating a minimal Claude-powered coding assistant in TypeScript. Start with a basic chat loop and progressively add tools until you have a fully functional coding agent in about 400 lines.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">ai</span><span class="preview-tag astro-3tyn5ojg">typescript</span><span class="preview-tag astro-3tyn5ojg">tooling</span>  </span> <time class="preview-date astro-3tyn5ojg">Jan 17, 2026</time> </span> </span> </span>  <script>
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
</script> for a hands-on guide to the underlying patterns.</p>
<p>Key settings to know:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="json"><code><span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">chat.useAgentSkills</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">chat.agentSkillsLocations</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">.github/skills</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">chat.customAgentInSubagent.enabled</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">github.copilot.chat.claude.showThinking</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">terminal.integrated.enableKittyKeyboardProtocol</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">terminal.integrated.enableWin32InputMode</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="{
  &#34;chat.useAgentSkills&#34;: true,
  &#34;chat.agentSkillsLocations&#34;: [&#34;.github/skills&#34;],
  &#34;chat.customAgentInSubagent.enabled&#34;: true,
  &#34;github.copilot.chat.claude.showThinking&#34;: true,
  &#34;terminal.integrated.enableKittyKeyboardProtocol&#34;: true,
  &#34;terminal.integrated.enableWin32InputMode&#34;: true
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>The ecosystem is about to get a lot more interesting.</p>
<hr/>
<h2 id="related-pull-requests--issues">Related Pull Requests &amp; Issues<a class="heading-link" aria-label="Link to section" href="#related-pull-requests--issues"><span class="heading-link-icon">#</span></a></h2>
<p>For those who want to dig into the implementation details:</p>
<h3 id="agent--skills">Agent &amp; Skills<a class="heading-link" aria-label="Link to section" href="#agent--skills"><span class="heading-link-icon">#</span></a></h3>
<ul>
<li><a href="https://github.com/microsoft/vscode/issues/274630" rel="noopener noreferrer" target="_blank">#274630 - Parallel subagent execution</a></li>
<li><a href="https://github.com/microsoft/vscode/issues/280704" rel="noopener noreferrer" target="_blank">#280704 - Agents define allowed subagents</a></li>
<li><a href="https://github.com/microsoft/vscode/issues/288480" rel="noopener noreferrer" target="_blank">#288480 - Skills enabled by default</a></li>
<li><a href="https://github.com/microsoft/vscode/issues/288483" rel="noopener noreferrer" target="_blank">#288483 - Extension-contributed skills via manifest</a></li>
<li><a href="https://github.com/microsoft/vscode/issues/288486" rel="noopener noreferrer" target="_blank">#288486 - Dynamic skills API</a></li>
<li><a href="https://github.com/microsoft/vscode/issues/282738" rel="noopener noreferrer" target="_blank">#282738 - Skills from custom locations</a></li>
</ul>
<h3 id="claude-integration">Claude Integration<a class="heading-link" aria-label="Link to section" href="#claude-integration"><span class="heading-link-icon">#</span></a></h3>
<ul>
<li><a href="https://github.com/microsoft/vscode/issues/287658" rel="noopener noreferrer" target="_blank">#287658 - Extended thinking support</a></li>
<li><a href="https://github.com/microsoft/vscode/issues/287933" rel="noopener noreferrer" target="_blank">#287933 - Model picker for Claude</a></li>
<li><a href="https://github.com/microsoft/vscode/issues/266962" rel="noopener noreferrer" target="_blank">#266962 - Claude agent support</a></li>
</ul>
<h3 id="terminal">Terminal<a class="heading-link" aria-label="Link to section" href="#terminal"><span class="heading-link-icon">#</span></a></h3>
<ul>
<li><a href="https://github.com/microsoft/vscode/issues/286809" rel="noopener noreferrer" target="_blank">#286809 - Kitty keyboard protocol</a></li>
<li><a href="https://github.com/microsoft/vscode/issues/286896" rel="noopener noreferrer" target="_blank">#286896 - Win32 input mode</a></li>
<li><a href="https://github.com/microsoft/vscode/issues/286810" rel="noopener noreferrer" target="_blank">#286810 - SGR 221/222 escape sequences</a></li>
<li><a href="https://github.com/microsoft/vscode/issues/257468" rel="noopener noreferrer" target="_blank">#257468 - Terminal output streams inline</a></li>
<li><a href="https://github.com/microsoft/vscode/issues/287664" rel="noopener noreferrer" target="_blank">#287664 - Auto-expand/collapse terminal output</a></li>
<li><a href="https://github.com/microsoft/vscode/issues/277286" rel="noopener noreferrer" target="_blank">#277286 - Terminal sandboxing for macOS/Linux</a></li>
<li><a href="https://github.com/microsoft/vscode/issues/286598" rel="noopener noreferrer" target="_blank">#286598 - Terminal timeout parameter</a></li>
<li><a href="https://github.com/microsoft/vscode/issues/287772" rel="noopener noreferrer" target="_blank">#287772 - Python syntax highlighting in confirmations</a></li>
<li><a href="https://github.com/xtermjs/xterm.js/pull/5600" rel="noopener noreferrer" target="_blank">xterm.js #5600 - Kitty keyboard protocol</a></li>
</ul>
<h3 id="mcp">MCP<a class="heading-link" aria-label="Link to section" href="#mcp"><span class="heading-link-icon">#</span></a></h3>
<ul>
<li><a href="https://github.com/microsoft/vscode/issues/289473" rel="noopener noreferrer" target="_blank">#289473 - Dynamic context updates</a></li>
<li><a href="https://github.com/microsoft/vscode/issues/287549" rel="noopener noreferrer" target="_blank">#287549 - Custom package registries</a></li>
<li><a href="https://github.com/microsoft/vscode/issues/260218" rel="noopener noreferrer" target="_blank">#260218 - Built-in MCP Apps</a></li>
<li><a href="https://github.com/microsoft/vscode/issues/283959" rel="noopener noreferrer" target="_blank">#283959 - startServer command</a></li>
<li><a href="https://github.com/microsoft/vscode/issues/283945" rel="noopener noreferrer" target="_blank">#283945 - MCP info in session exports</a></li>
</ul>
<h3 id="chat--sessions">Chat &amp; Sessions<a class="heading-link" aria-label="Link to section" href="#chat--sessions"><span class="heading-link-icon">#</span></a></h3>
<ul>
<li><a href="https://github.com/microsoft/vscode/issues/285854" rel="noopener noreferrer" target="_blank">#285854 - /clear archives sessions</a></li>
<li><a href="https://github.com/microsoft/vscode/issues/288467" rel="noopener noreferrer" target="_blank">#288467 - New Local Chat command</a></li>
<li><a href="https://github.com/microsoft/vscode/issues/283954" rel="noopener noreferrer" target="_blank">#283954 - Import chat sessions</a></li>
<li><a href="https://github.com/microsoft/vscode/issues/288448" rel="noopener noreferrer" target="_blank">#288448 - Multi-select in sessions</a></li>
<li><a href="https://github.com/microsoft/vscode/issues/281258" rel="noopener noreferrer" target="_blank">#281258 - Resizable sessions sidebar</a></li>
<li><a href="https://github.com/microsoft/vscode/issues/283123" rel="noopener noreferrer" target="_blank">#283123 - Increased persisted sessions</a></li>
<li><a href="https://github.com/microsoft/vscode/issues/289223" rel="noopener noreferrer" target="_blank">#289223 - Accessible View streams thinking</a></li>
</ul>
<h3 id="editor--other">Editor &amp; Other<a class="heading-link" aria-label="Link to section" href="#editor--other"><span class="heading-link-icon">#</span></a></h3>
<ul>
<li><a href="https://github.com/microsoft/vscode/issues/287819" rel="noopener noreferrer" target="_blank">#287819 - Improved shebang detection</a></li>
<li><a href="https://github.com/microsoft/vscode/issues/284517" rel="noopener noreferrer" target="_blank">#284517 - Ghost text visibility</a></li>
<li><a href="https://github.com/microsoft/vscode/issues/9123" rel="noopener noreferrer" target="_blank">#9123 - Double-click selects block content</a></li>
<li><a href="https://github.com/microsoft/vscode/issues/10633" rel="noopener noreferrer" target="_blank">#10633 - Match file path case toggle</a></li>
<li><a href="https://github.com/microsoft/vscode/issues/288439" rel="noopener noreferrer" target="_blank">#288439 - Parallel build tasks</a></li>
<li><a href="https://github.com/microsoft/vscode/issues/111767" rel="noopener noreferrer" target="_blank">#111767 - Git Delete File command</a></li>
</ul>
<h3 id="iteration-plan">Iteration Plan<a class="heading-link" aria-label="Link to section" href="#iteration-plan"><span class="heading-link-icon">#</span></a></h3>
<ul>
<li><a href="https://github.com/microsoft/vscode/issues/286040" rel="noopener noreferrer" target="_blank">#286040 - January 2026 Iteration Plan</a></li>
</ul>
<hr/>
<p><em>These features are rolling out in VS Code Insiders (1.109) now, with stable release expected in early February. Note that some features like kitty keyboard protocol and win32-input-mode are disabled by default and require manual opt-in.</em></p> </article> <script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).only=e;window.dispatchEvent(new Event("astro:only"));})();</script><astro-island uid="Z1XneyL" component-url="/_astro/presentation.C3Wa0mjp.js" component-export="VMarkBlogRenderer" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;containerSelector&quot;:[0,&quot;#article&quot;],&quot;class&quot;:[0,&quot;astro-vj4tpspi&quot;]}" ssr client="only" opts="{&quot;name&quot;:&quot;VMarkBlogRenderer&quot;,&quot;value&quot;:&quot;react&quot;}"></astro-island> <!-- Fullscreen Modal Container using native dialog --><dialog id="mermaid-modal" class="mermaid-modal" aria-label="Fullscreen diagram view"> <div class="mermaid-modal-content"> <button class="mermaid-modal-close" aria-label="Close fullscreen view" type="button"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <line x1="18" y1="6" x2="6" y2="18"></line> <line x1="6" y1="6" x2="18" y2="18"></line> </svg> </button> <div class="mermaid-modal-diagram"></div> <div class="mermaid-modal-hint">Press <kbd>Esc</kbd> or click outside to close</div> </div> </dialog>  <script type="module">const p=new Set;function g(){const e=document.getElementById("mermaid-modal"),c=e?.querySelector(".mermaid-modal-diagram"),f=e?.querySelector(".mermaid-modal-close");if(!e||!c)return;document.querySelectorAll('svg[id^="mermaid-"]').forEach(t=>{if(!t.id.match(/^mermaid-\d+$/)||p.has(t.id)||t.parentElement?.classList.contains("mermaid-fullscreen-wrapper")||t.closest(".mermaid-modal"))return;p.add(t.id);const n=document.createElement("div");n.className="mermaid-fullscreen-wrapper mermaid-clickable",n.setAttribute("tabindex","0"),n.setAttribute("role","button"),n.setAttribute("aria-label","Click to view diagram fullscreen"),t.parentElement?.insertBefore(n,t),n.appendChild(t);const o=document.createElement("div");o.className="mermaid-expand-icon",o.innerHTML=`
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
</li> <li class="astro-vj4tpspi">Small tips and trick</li> </ul> </div> <a href="https://alex-op-newsletter.beehiiv.com/subscribe?utm_source=blog&utm_medium=post&utm_campaign=post_whats-new-vscode-copilot-january-2026" target="_blank" rel="noopener noreferrer" id="newsletter-subscribe-button" class="inline-flex items-center justify-center gap-2 rounded-full bg-skin-accent px-6 py-3 text-base font-semibold text-skin-inverted shadow-md transition-all duration-200 hover:scale-[1.02] hover:transform hover:opacity-90 astro-vj4tpspi"> <svg class="h-5 w-5 fill-current astro-vj4tpspi" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg>
Subscribe Now
</a> <button id="newsletter-dismiss" data-post-slug="whats-new-vscode-copilot-january-2026" class="absolute right-3 top-3 rounded-full p-1 text-skin-base transition-all duration-200 hover:bg-skin-accent hover:bg-opacity-10 hover:text-skin-accent astro-vj4tpspi" aria-label="Close notification"> <svg class="h-5 w-5 astro-vj4tpspi" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class="astro-vj4tpspi"></path> </svg> </button> </div> </div> </div> <ul class="my-8 flex flex-wrap gap-2 astro-vj4tpspi"> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/ai/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-2"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">ai</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/tooling/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-3"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">tooling</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/vscode/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-4"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">vscode</span>   </a> </li>  </ul> <div class="flex flex-col-reverse items-center justify-between gap-6 sm:flex-row-reverse sm:items-end sm:gap-4 astro-vj4tpspi"> <button id="back-to-top" class="focus-outline whitespace-nowrap py-1 hover:opacity-75 astro-vj4tpspi"> <svg xmlns="http://www.w3.org/2000/svg" class="rotate-90 astro-vj4tpspi"> <path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg> <span class="astro-vj4tpspi">Back to Top</span> </button> <div class="social-icons astro-wkojbtzc"> <span class="italic astro-wkojbtzc">Share this post on:</span> <div class="text-center astro-wkojbtzc"> <a href="https://wa.me/?text=https://alexop.dev/posts/whats-new-vscode-copilot-january-2026/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via WhatsApp" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"></path>
      <path d="M9 10a0.5 .5 0 0 0 1 0v-1a0.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a0.5 .5 0 0 0 0 -1h-1a0.5 .5 0 0 0 0 1"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via WhatsApp</span> </a><a href="https://www.facebook.com/sharer.php?u=https://alexop.dev/posts/whats-new-vscode-copilot-january-2026/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Facebook" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"
    ></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on Facebook</span> </a><a href="https://x.com/intent/tweet?url=https://alexop.dev/posts/whats-new-vscode-copilot-january-2026/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Tweet this post" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Tweet this post</span> </a><a href="https://t.me/share/url?url=https://alexop.dev/posts/whats-new-vscode-copilot-january-2026/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via Telegram" target="_blank" rel="noopener noreferrer"> <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon-tabler"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"></path>
      </svg> <span class="sr-only astro-wkojbtzc">Share this post via Telegram</span> </a><a href="https://pinterest.com/pin/create/button/?url=https://alexop.dev/posts/whats-new-vscode-copilot-january-2026/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Pinterest" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <line x1="8" y1="20" x2="12" y2="11"></line>
      <path d="M10.7 14c.437 1.263 1.43 2 2.55 2c2.071 0 3.75 -1.554 3.75 -4a5 5 0 1 0 -9.7 1.7"></path>
      <circle cx="12" cy="12" r="9"></circle>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post on Pinterest</span> </a><a href="mailto:?subject=See%20this%20post&#38;body=https://alexop.dev/posts/whats-new-vscode-copilot-january-2026/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via email" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via email</span> </a><a href="https://www.linkedin.com/shareArticle?mini=true&url=https://alexop.dev/posts/whats-new-vscode-copilot-january-2026/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
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
    </script> </body> </html>  <script>(function(){const postSlug = "whats-new-vscode-copilot-january-2026";

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
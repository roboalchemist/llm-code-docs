# Source: https://alexop.dev/posts/vs-code-copilot-workshop

<!DOCTYPE html><html lang="en" class="scroll-smooth astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/posts/vs-code-copilot-workshop/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>Next Level GitHub Copilot: Agents, Instructions &amp; Automation in VS Code | alexop.dev</title><meta name="title" content="Next Level GitHub Copilot: Agents, Instructions &#38; Automation in VS Code | alexop.dev"><meta name="description" content="Workshop covering the transformation from LLM to Agent, context engineering, AGENTS.md, subagents, and skills in VS Code Copilot."><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="Next Level GitHub Copilot: Agents, Instructions &#38; Automation in VS Code | alexop.dev"><meta property="og:description" content="Workshop covering the transformation from LLM to Agent, context engineering, AGENTS.md, subagents, and skills in VS Code Copilot."><meta property="og:url" content="https://alexop.dev/posts/vs-code-copilot-workshop/"><meta property="og:image" content="https://alexop.dev/posts/next-level-git-hub-copilot-agents-instructions-automation-in-vs-code/index.png"><meta property="og:type" content="article"><!-- Article Published/Modified time --><meta property="article:published_time" content="2026-01-24T00:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/posts/vs-code-copilot-workshop/"><meta property="twitter:title" content="Next Level GitHub Copilot: Agents, Instructions &#38; Automation in VS Code | alexop.dev"><meta property="twitter:description" content="Workshop covering the transformation from LLM to Agent, context engineering, AGENTS.md, subagents, and skills in VS Code Copilot."><meta property="twitter:image" content="https://alexop.dev/posts/next-level-git-hub-copilot-agents-instructions-automation-in-vs-code/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"Next Level GitHub Copilot: Agents, Instructions & Automation in VS Code | alexop.dev","description":"Workshop covering the transformation from LLM to Agent, context engineering, AGENTS.md, subagents, and skills in VS Code Copilot.","image":"https://alexop.dev/posts/next-level-git-hub-copilot-agents-instructions-automation-in-vs-code/index.png","datePublished":"2026-01-24T00:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
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
</style><style>[data-astro-transition-scope="astro-plk3gbjq-1"] { view-transition-name: next-level-git-hub-copilot-agents-instructions-automation-in-vs-code; }@layer astro { ::view-transition-old(next-level-git-hub-copilot-agents-instructions-automation-in-vs-code) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(next-level-git-hub-copilot-agents-instructions-automation-in-vs-code) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(next-level-git-hub-copilot-agents-instructions-automation-in-vs-code) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(next-level-git-hub-copilot-agents-instructions-automation-in-vs-code) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-2"] { view-transition-name: vs-code; }@layer astro { ::view-transition-old(vs-code) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(vs-code) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(vs-code) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(vs-code) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-3"] { view-transition-name: github-copilot; }@layer astro { ::view-transition-old(github-copilot) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(github-copilot) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(github-copilot) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(github-copilot) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-4"] { view-transition-name: ai-agents; }@layer astro { ::view-transition-old(ai-agents) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(ai-agents) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(ai-agents) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(ai-agents) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-5"] { view-transition-name: context-engineering; }@layer astro { ::view-transition-old(context-engineering) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(context-engineering) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(context-engineering) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(context-engineering) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-6"] { view-transition-name: workshop; }@layer astro { ::view-transition-old(workshop) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(workshop) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(workshop) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(workshop) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; } }[data-astro-transition-fallback="old"] [data-astro-transition-scope="astro-36ssibgs-6"],
			[data-astro-transition-fallback="old"][data-astro-transition-scope="astro-36ssibgs-6"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition-fallback="new"] [data-astro-transition-scope="astro-36ssibgs-6"],
			[data-astro-transition-fallback="new"][data-astro-transition-scope="astro-36ssibgs-6"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back][data-astro-transition-fallback="old"] [data-astro-transition-scope="astro-36ssibgs-6"],
			[data-astro-transition=back][data-astro-transition-fallback="old"][data-astro-transition-scope="astro-36ssibgs-6"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back][data-astro-transition-fallback="new"] [data-astro-transition-scope="astro-36ssibgs-6"],
			[data-astro-transition=back][data-astro-transition-fallback="new"][data-astro-transition-scope="astro-36ssibgs-6"] { 
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <div class="mx-auto flex w-full max-w-5xl justify-start px-2 astro-vj4tpspi"> <button class="focus-outline mb-2 mt-8 flex hover:opacity-75 astro-vj4tpspi" onclick="(() => (history.length === 1) ? window.location = '/' : history.back())()"> <svg xmlns="http://www.w3.org/2000/svg" class="astro-vj4tpspi"><path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg><span class="astro-vj4tpspi">Go back</span> </button> </div> <main data-pagefind-body id="main-content" class="relative astro-vj4tpspi"> <h1 class="post-title astro-vj4tpspi" data-astro-transition-scope="astro-plk3gbjq-1">Next Level GitHub Copilot: Agents, Instructions &amp; Automation in VS Code</h1> <div class="my-2 flex items-center justify-between astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-100 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-base"><time dateTime="2026-01-24T00:00:00.000Z">Jan 24, 2026</time><span class="sr-only"> at </span></span></div> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="MtIV2" prefix="r22" component-url="/_astro/PostCopyButton.-PGtk4At.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;title&quot;:[0,&quot;Next Level GitHub Copilot: Agents, Instructions &amp; Automation in VS Code&quot;],&quot;content&quot;:[0,&quot;import { Slide, VClicks, SlotLeft, SlotRight, SubagentDiagram, ParallelSubagentDiagram, MagicMove } from \&quot;@features/presentation\&quot;;\nimport agentDiagram from \&quot;@assets/images/copilotWorkshop/agent.png\&quot;;\nimport Karpahty from \&quot;@assets/images/copilotWorkshop/karpathy.png\&quot;;\nimport agentTools from \&quot;@assets/images/copilotWorkshop/agentTools.png\&quot;;\nimport agentContext from \&quot;@assets/images/copilotWorkshop/agentContext.png\&quot;;\nimport ContextUtilizationVisualizer from \&quot;@features/llm-education/components/ContextUtilizationVisualizer\&quot;;\nimport ContextWindowVisualizer from \&quot;@features/llm-education/components/ContextWindowVisualizer\&quot;;\nimport AgentSum from \&quot;@assets/images/copilotWorkshop/agentSum.png\&quot;;\nimport progressiveDisc from \&quot;@assets/images/copilotWorkshop/progressiveDisc.png\&quot;;\nimport howAgentSkills from \&quot;@assets/images/copilotWorkshop/howAgentSkills.png\&quot;;\nimport BloatedAgent from \&quot;@assets/images/copilotWorkshop/bloatedAgent.png\&quot;;\nimport ContextFillupVisualizer from \&quot;@features/llm-education/components/ContextFillupVisualizer\&quot;;\nimport DocsStructureDiagram from \&quot;@features/agent-teams/components/DocsStructureDiagram\&quot;;\nimport BloatedAgentsDiagram from \&quot;@features/agent-teams/components/BloatedAgentsDiagram\&quot;;\nimport SettingsPng from \&quot;@assets/images/copilotWorkshop/settings.png\&quot;;\nimport skillExample from \&quot;@assets/images/copilotWorkshop/skillExample.png\&quot;;\nimport robot from \&quot;@assets/images/copilotWorkshop/robot.png\&quot;;\n\n&lt;Slide layout=\&quot;cover\&quot; /&gt;\n# Next Level GitHub Copilot\n\nAgents.md Subagents &amp; Skills\n\nby Alexander Opalic\n\n---\n\n&lt;Slide layout=\&quot;image\&quot; image={Karpahty} alt=\&quot;Agent architecture diagram\&quot; /&gt;\n---\n\n\n## Workshop Outline\n\n&lt;VClicks&gt;\n\n1. What is an Agent? (LLM → Agent transformation)\n2. Context Engineering (the real skill)\n3. Back Pressure (core validation concept)\n4. AGENTS.md (open standard)\n5. Subagents (specialized invocation)\n6. Skills (portable workflows)\n7. Live Demo\n\n&lt;/VClicks&gt;\n\n---\n\n&lt;Slide layout=\&quot;center\&quot; /&gt;\n## 🙋 Who has used GitHub Copilot in VS Code?\n\n---\n\n&lt;Slide layout=\&quot;two-cols-header\&quot; /&gt;\n\n## About me\n\n&lt;SlotLeft /&gt;\n\n&lt;div class=\&quot;flex flex-col items-center\&quot;&gt;\n  &lt;img class=\&quot;w-72 rounded-full\&quot; src=\&quot;https://avatars.githubusercontent.com/u/33398393?v=4\&quot; /&gt;\n  &lt;h2 class=\&quot;mt-4\&quot;&gt;Alex Opalic&lt;/h2&gt;\n&lt;/div&gt;\n\n&lt;SlotRight /&gt;\n\n&lt;VClicks&gt;\n\n* 🚀 7 years expierence as a full stack developer \n* 💼 Developer at Otto Payments\n* 🏡 Based in Geretsried (south of Munich, Bavaria)\n* ✍️ Blogger at alexop.dev\n* 🎤 Sharing &amp; speaking about Vue, testing &amp; GraphQL &amp; AI\n\n&lt;/VClicks&gt;\n\n---\n\n&lt;Slide layout=\&quot;section\&quot; /&gt;\n# What is an Agent?\n\n---\n\n## The Transformation: LLM → Agent\n\n- At the beginning, an LLM is just a text generator\n- One problem: the LLM didn&#39;t have access to current news\n- Solution: all providers gave the LLM access to tools\n- With tools, the LLM can now interact with the world\n- This is why an agent is an LLM + Tools + Agentic Loop\n\n---\n\n&lt;Slide layout=\&quot;image\&quot; image={agentDiagram} alt=\&quot;Agent architecture diagram\&quot; /&gt;\n\n---\n\n## The Agentic Loop (nanocode)\n\n```shell\nnanocode | claude-opus-4-5 | /Users/alexanderopalic/Projects/typescript/nanocode\n\n────────────────────────────────────────────────────────────────────────────────\n❯  create a simple typescript file as a sum function\n────────────────────────────────────────────────────────────────────────────────\n[agentLoop] Starting with 1 messages\n[agentLoop] Got response, stop_reason: tool_use\n\n⏺ Write(src/sum.ts)\n  ⎿  ok\n[agentLoop] Starting with 3 messages\n[agentLoop] Got response, stop_reason: end_turn\n\n⏺ Created `src/sum.ts` with a simple sum function that takes two numbers and returns their sum.\n```\n\n**~350 lines of TypeScript** to understand how Claude Code works.\n\n---\n\n## The Agentic Loop (Code)\n\n```typescript\nasync function agentLoop(messages: Message[], systemPrompt: string): Promise&lt;Message[]&gt; {\n  const response = await callApi(messages, systemPrompt)\n  printResponse(response)\n\n  const toolResults = await processToolCalls(response.content)\n  const newMessages = [...messages, { role: &#39;assistant&#39;, content: response.content }]\n\n  if (toolResults.length === 0) {\n    return newMessages  // No tools called, we&#39;re done\n  }\n\n  return agentLoop(  // Loop again with tool results\n    [...newMessages, { role: &#39;user&#39;, content: toolResults }],\n    systemPrompt\n  )\n}\n```\n\nThe entire request → response → execute → loop cycle in ~15 lines.\n\n---\n\n## Tool Registration\n\n```typescript\nconst TOOLS = new Map([\n  [&#39;read&#39;, {\n    description: &#39;Read file with line numbers&#39;,\n    schema: { path: &#39;string&#39;, offset: &#39;number?&#39;, limit: &#39;number?&#39; },\n    execute: read\n  }],\n  [&#39;write&#39;, {\n    description: &#39;Write content to file&#39;,\n    schema: { path: &#39;string&#39;, content: &#39;string&#39; },\n    execute: write\n  }],\n  [&#39;bash&#39;, {\n    description: &#39;Run shell command&#39;,\n    schema: { cmd: &#39;string&#39; },\n    execute: bash\n  }]\n])\n```\n\n---\n\n## A Complete Tool Implementation\n\n```typescript\nasync function read(args: Record&lt;string, unknown&gt;): Promise&lt;string&gt; {\n  const path = args.path as string\n  const text = await Bun.file(path).text()\n  const lines = text.split(&#39;\\n&#39;)\n  const offset = (args.offset as number) ?? 0\n  const limit = (args.limit as number) ?? lines.length\n  return lines\n    .slice(offset, offset + limit)\n    .map((line, i) =&gt; `${(offset + i + 1).toString().padStart(4)}| ${line}`)\n    .join(&#39;\\n&#39;)\n}\n```\n\n---\n\n&lt;Slide layout=\&quot;image\&quot; image={agentTools} alt=\&quot;Agent tools overview\&quot; /&gt;\n\n---\n\n## VS Code Copilot Built-in Tools\n\n- ⟨⟩ **agent** — Delegate tasks to other agents\n- ⓘ **askQuestions** — Ask questions to clarify requirements\n- ✎ **edit** — Edit files in your workspace\n- ▷ **execute** — Execute code and applications\n- ⧉ **read** — Read files in your workspace\n- 🔍 **search** — Search files in your workspace\n- ≡ **todo** — Manage and track todo items\n- ✕ **vscode** — Use VS Code features\n- 🌐 **web** — Fetch information from the web\n\n---\n\n&lt;Slide layout=\&quot;section\&quot; /&gt;\n# Context Engineering\n\n---\n\n&lt;Slide layout=\&quot;image\&quot; image={agentContext} alt=\&quot;Agent context engineering\&quot; /&gt;\n\n---\n\n&lt;ContextWindowVisualizer client:visible /&gt;\n\n---\n\n&lt;Slide layout=\&quot;quote\&quot; /&gt;\n&gt; \&quot;Context engineering is the art and science of filling the context window with just the right information at each step of an agent&#39;s trajectory.\&quot;\n&gt;\n&gt; — LangChain/Manus webinar\n\n---\n\n## Context Window Utilization\n\n&lt;ContextUtilizationVisualizer client:visible /&gt;\n\n---\n\n\n&lt;ContextFillupVisualizer client:visible /&gt;\n\n---\n\n## Three Long-Horizon Techniques\n\nFrom [Anthropic&#39;s guide](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents):\n\n&lt;VClicks&gt;\n1. **Compaction** — Summarize history, reset periodically\n2. **Structured note-taking** — External memory systems\n3. **Sub-agent architectures** — Distribute work across focused contexts\n&lt;/VClicks&gt;\n\n---\n\n&lt;Slide layout=\&quot;section\&quot; /&gt;\n# Back Pressure\n\n---\n\n## Why Back Pressure Matters\n\n**Back pressure** = automated feedback that validates agent work\n\n&lt;VClicks&gt;\n\n- Without back pressure, **you** become the validation layer\n- Agents cannot self-correct if nothing tells them something is wrong\n- With good back pressure, agents detect mistakes and iterate until correct\n\n&lt;/VClicks&gt;\n\n&gt; \&quot;If you&#39;re directly responsible for checking each line is valid, that&#39;s time taken away from higher-level goals.\&quot;\n\n---\n\n## Back Pressure Sources\n\n| Source | What It Validates |\n|--------|-------------------|\n| **Type system** | Types, interfaces, contracts |\n| **Build tools** | Syntax, imports, compilation |\n| **Tests** | Logic, behavior, regressions |\n| **Linters** | Style, patterns, best practices |\n\n**Key insight:** Expressive type systems + good error messages = agents can self-correct.\n\n---\n\n&lt;Slide layout=\&quot;section\&quot; /&gt;\n# AGENTS.md\n\n---\n\n## What is AGENTS.md?\n\n**What:** An open standard for agent-specific documentation\n\n**Where:** Repository root (works in monorepos too)\n\n**Who:** Works with Copilot, Claude, Cursor, Devin, 20+ agents\n\n&gt; \&quot;While README.md targets humans, AGENTS.md contains the extra context coding agents need.\&quot;\n\n---\n\n&lt;Slide layout=\&quot;iframe\&quot; src=\&quot;https://agents.md/\&quot; title=\&quot;AGENTS.md - Open Standard\&quot; /&gt;\n\n---\n\n## AGENTS.md Structure\n\n```markdown\n# AGENTS.md\n\n## Dev Environment\n- How to set up and navigate\n\n## Build &amp; Test Commands\n- `pnpm install &amp;&amp; pnpm dev`\n- `pnpm test:unit`\n\n## Code Style\n- TypeScript strict mode\n- Prefer composition over inheritance\n\n## PR Instructions\n- Keep PRs small and focused\n```\n\n**Key:** No required fields—use what helps your project.\n\n---\n\n&lt;Slide layout=\&quot;image\&quot; image={BloatedAgent} /&gt;\n\n---\n\n&lt;Slide layout=\&quot;two-cols-header\&quot; /&gt;\n\n## Before vs After: Progressive Disclosure\n\n&lt;SlotLeft /&gt;\n\n&lt;h3 class=\&quot;text-red-400 font-bold text-xl mb-4\&quot;&gt;❌ Bloated (847 lines)&lt;/h3&gt;\n\n```markdown\n# AGENTS.md\n\n## API Endpoints\n[200 lines of docs...]\n## Testing Strategy\n[150 lines of docs...]\n## Architecture\n[300 lines of docs...]\n## Code Style\n[100 lines of rules...]\n## Deployment\n[97 lines of docs...]\n```\n\n&lt;p class=\&quot;text-yellow-400 mt-4 text-sm\&quot;&gt;40% context consumed before work starts&lt;/p&gt;\n\n&lt;SlotRight /&gt;\n\n&lt;h3 class=\&quot;text-green-400 font-bold text-xl mb-4\&quot;&gt;✅ Lean (58 lines)&lt;/h3&gt;\n\n```markdown\n# AGENTS.md\n\n## Quick Start\npnpm install &amp;&amp; pnpm dev\n\n## Docs Reference\n| Doc | When to read |\n|-----|--------------|\n| docs/api.md | API work |\n| docs/testing.md | Tests |\n| docs/arch.md | Design |\n```\n\n&lt;p class=\&quot;text-cyan-400 mt-4 text-sm\&quot;&gt;Docs loaded on-demand when needed&lt;/p&gt;\n\n---\n\n&lt;Slide layout=\&quot;image\&quot; image={progressiveDisc} alt=\&quot;Progressive disclosure diagram\&quot; /&gt;\n\n---\n\n## The /learn Skill\n\n```markdown\n# Learn from Conversation\n\n## Phase 1: Deep Analysis\n- What patterns or approaches were discovered?\n- What gotchas or pitfalls were encountered?\n- What architecture decisions were made?\n\n## Phase 2: Categorize &amp; Locate\nRead existing docs to find the best home.\n\n## Phase 3: Draft the Learning\nFormat to match existing doc style.\n\n## Phase 4: User Approval (BLOCKING)\nPresent changes, wait for explicit approval.\n\n## Phase 5: Save\nAfter approval, save the learning.\n```\n\n---\n\n&lt;Slide layout=\&quot;section\&quot; /&gt;\n# Subagents\n\n---\n\n## Subagents in VS Code\n\n**How to invoke:**\n&lt;VClicks&gt;\n1. Enable tools in Copilot Chat (hammer icon)\n2. Call explicitly with `#runSubagent`\n3. Or accept when Copilot suggests one\n&lt;/VClicks&gt;\n\n---\n\n## Use Cases \n\n&lt;VClicks&gt;\n- Specialized searches (explore codebase, web, docs)\n- Long-running tasks (data analysis, refactoring)\n- TDD workflows (test generation, validation)\n- Multi-step processes (research, summarize, act)\n&lt;/VClicks&gt;\n---\n## Explore Subagent Flow\n\n&lt;SubagentDiagram\n  task=\&quot;Find auth files\&quot;\n  files={[\&quot;Auth.tsx\&quot;, \&quot;auth.ts\&quot;, \&quot;authService.ts\&quot;]}\n/&gt;\n\nClick **Start** to see how the main agent delegates file search to a specialized Explore subagent.\n\n---\n\n## Parallel Subagent Execution\n\n&lt;ParallelSubagentDiagram\n  task=\&quot;Research Vue 3 reactivity\&quot;\n  agents={[\n    { name: \&quot;Web Agent\&quot;, icon: \&quot;🌐\&quot;, color: \&quot;#3b82f6\&quot;, domain: \&quot;Docs, GitHub\&quot;, findings: [\&quot;Official guide\&quot;, \&quot;RFC #123\&quot;, \&quot;GitHub issue\&quot;] },\n    { name: \&quot;Community\&quot;, icon: \&quot;💬\&quot;, color: \&quot;#8b5cf6\&quot;, domain: \&quot;Reddit, SO\&quot;, findings: [\&quot;r/vuejs post\&quot;, \&quot;Top SO answer\&quot;, \&quot;Discord tip\&quot;] },\n    { name: \&quot;Codebase\&quot;, icon: \&quot;📂\&quot;, color: \&quot;#10b981\&quot;, domain: \&quot;Project files\&quot;, findings: [\&quot;useAuth.ts\&quot;, \&quot;store.ts\&quot;, \&quot;api/client.ts\&quot;] }\n  ]}\n/&gt;\n\nClick **Start** to see the fan-out/fan-in pattern where multiple subagents search in parallel.\n\n---\n\n## Subagent in nanocode: Fetch Tool\n\n```shell\nnanocode | claude-opus-4-5 | /Users/alexanderopalic/Projects/typescript/nanocode\n\n────────────────────────────────────────────────────────────────────────────────\n❯ how does fc bayern played yesterday\n────────────────────────────────────────────────────────────────────────────────\n[agentLoop] Starting with 1 messages\n[agentLoop] Got response, stop_reason: tool_use\n\n⏺ Fetch(https://www.google.com/search?q=fc+bayern+munich+m)\n  ⎿  I apologize, but I cannot access real-time sports results or ... +7 lines\n[agentLoop] Starting with 3 messages\n[agentLoop] Got response, stop_reason: tool_use\n\n⏺ Fetch(https://www.espn.com/soccer/team/_/id/132/bayern-m)\n  ⎿  Based on the information in the image, Bayern Munich&#39;s most  ... +7 lines\n[agentLoop] Starting with 5 messages\n[agentLoop] Got response, stop_reason: end_turn\n\n⏺ FC Bayern Munich lost 2-1 to FC Augsburg in the Bundesliga yesterday.\n```\n\nThe **Fetch tool** uses a subagent to summarize HTML responses before returning.\n\n---\n\n&lt;Slide layout=\&quot;section\&quot; /&gt;\n#  Skills\n\n---\n\n&lt;Slide layout=\&quot;image\&quot; image={howAgentSkills} alt=\&quot;How Agent Skills work diagram\&quot; /&gt;\n\n---\n\n## Real Skill: Plausible SEO Consultant\n\n```shell\n.claude/skills/plausible-insights/\n├── skill.md              # Skill definition + quick start\n├── scripts/              # Automation scripts \n│   └── fetch-data.ts    # Fetch Plausible data CLI\n└── references/           # On-demand docs (progressive disclosure)\n    ├── quick-ref.md      # Common query patterns\n    ├── api/\n    │   ├── filters.md    # Filter syntax\n    │   └── errors.md     # Error solutions\n    └── seo/\n        └── thresholds.md # Interpretation guidelines\n```\n\nThe agent reads `skill.md` first. Reference docs load only when needed.\n\n---\n\n## Skill in Action\n\n**User:** \&quot;Why is my bounce rate so high on the Vue posts?\&quot;\n\n&lt;VClicks&gt;\n\n1. Description matches → skill.md loads (~500 tokens)\n2. Agent runs: `bun cli top-pages --range 7d --pattern \&quot;/vue/\&quot;`\n3. Agent reads `references/seo/thresholds.md` for interpretation\n4. Agent fetches actual pages with WebFetch\n5. Returns specific fixes based on real content\n\n&lt;/VClicks&gt;\n\n**Key:** Data shows symptoms. Content shows causes.\n\n---\n\n&lt;Slide layout=\&quot;section\&quot; /&gt;\n# The Full Picture\n\n---\n\n&lt;Slide layout=\&quot;image\&quot; image={AgentSum} alt=\&quot;Agent summary diagram\&quot; /&gt;\n\n---\n\n&lt;Slide layout=\&quot;section\&quot; /&gt;\n# Live Demo\n\n---\n\n## Prerequisites\n\nThe demo uses `npx` (bundled with Node.js) and Python. Install for your platform:\n\n&lt;VClicks&gt;\n\n**Mac (Homebrew):**\n```bash\nbrew install node python\n```\n\n**Windows (winget):**\n```bash\nwinget install OpenJS.NodeJS Python.Python.3.12\n```\n\n**Or download from:** [nodejs.org](https://nodejs.org) | [python.org](https://python.org)\n\n&lt;/VClicks&gt;\n\n**Verify:**\n```bash\nnode --version &amp;&amp; npx --version &amp;&amp; python --version\n```\n\n---\n\n## Demo: Building a Skill\n\n&lt;VClicks&gt;\n\n1. **Enable Skills** in VS Code settings\n2. **Install skill-creator** via CLI\n3. **Prompt** to generate a new skill\n\n&lt;/VClicks&gt;\n\n---\n\n## Step 1: Enable Skills\n\n**VS Code Setting:**\n\n```json\n{\n  \&quot;chat.useAgentSkills\&quot;: true\n}\n```\n\nOr via UI: `Settings → Search \&quot;agent skills\&quot; → Enable`\n\n&gt; Note: Still in preview — enable in VS Code Insiders for latest features.\n\n---\n\n&lt;Slide layout=\&quot;image\&quot; image={SettingsPng} alt=\&quot;VS Code settings screenshot\&quot; /&gt;\n---\n\n## Step 3: Create a new Skill\n\n```md\n---\nname: hello\ndescription: &#39;use it everytime the user writes alex&#39;\n---\n\n# Hello SKill\n\nif the user writes \&quot;alex\&quot;, respond with \&quot;Hello, Alexander Opalic! How can I assist you today?\&quot;\n\n```\n\n---\n\n## Step 3: Install skill-creator\n\n```bash\nnpx skills add https://github.com/anthropics/skills --skill skill-creator\n```\n\nThis adds the **skill-creator** skill to your project — a skill that helps you create new skills.\n\n**Project structure after install:**\n\n```\nmy-project/\n└── .github/\n    └── skills/\n        └── skill-creator/\n            └── SKILL.md\n```\n\n---\n\n```shell\n◇  Source: https://github.com/anthropics/skills.git\n│\n◇  Repository cloned\n│\n◇  Found 17 skills (via Well-known Agent Skill Discovery)\n│\n●  Selected 1 skill: skill-creator\n│\n◇  Detected 3 agents\n│\n◇  Install to\n│  All agents (Recommended)\n│\n◇  Installation scope\n│  Project\n│\n◇  Installation method\n│  Symlink (Recommended)\n\n│\n◇  Installation Summary ──────────────────────────────╮\n│                                                     │\n│  ~/Projects/workshop/.agents/skills/skill-creator   │\n│    symlink → Claude Code, GitHub Copilot, OpenCode  │\n│                                                     │\n├─────────────────────────────────────────────────────╯\n│\n◆  Proceed with installation?\n│  ● Yes / ○ No\n└\n```\n---\n\n## Step 3: Generate a New Skill\n\nImportant Skill name and folder name must match!\n\n**Prompt:**\n\n```\nCreate a skill that will use https://alexop.dev/llms.txt\nand will answer any question regarding Vue or AI.\n\nThe skill should fetch the content and use the\n#runSubagent command. The subagent should do the\nheavy work and then report back to the main agent.\nname of the skill is vue-ai-assistant\n```\n\n→ **skill-creator generates the SKILL.md for us**\n\n---\n\n## What Gets Generated\n\n```markdown\n---\nname: vue-ai-assistant\ndescription: Answer questions about Vue.js, Nuxt, and AI topics using Alexander Opalic&#39;s knowledge base. Use this skill when the user asks about Vue, Vue 3, Nuxt, Nuxt 3, Composition API, Vue Router, Pinia, Vite, AI, machine learning, LLMs, or related frontend/AI topics. Triggers on questions like \&quot;how do I use Vue\&quot;, \&quot;explain Nuxt\&quot;, \&quot;what&#39;s new in Vue 3\&quot;, \&quot;AI agent patterns\&quot;, or any Vue/AI related query.\n---\n\n# Vue &amp; AI Assistant\n\nAnswer questions about Vue.js ecosystem and AI topics by fetching knowledge from https://alexop.dev/llms.txt and delegating research to a subagent.\n\n## MANDATORY Workflow\n\n**IMPORTANT: You MUST follow ALL steps below. Do NOT skip the subagent step. Do NOT answer directly after fetching - you MUST delegate to a subagent.**\n\n1. **Fetch the knowledge base**: Use `fetch_webpage` to retrieve content from `https://alexop.dev/llms.txt`\n2. **REQUIRED - Delegate to subagent**: Use `runSubagent` with the fetched content and user&#39;s question. **This step is NOT optional.**\n3. **Return the answer**: Present the subagent&#39;s findings to the user\n\n## Implementation\n\n**You MUST execute ALL steps below. Skipping the subagent is a violation of this skill&#39;s requirements.**\n\n### Step 1: Fetch Knowledge Base\n\nUse the fetch_webpage tool:\n- URL: `https://alexop.dev/llms.txt`\n- Query: The user&#39;s question about Vue or AI\n\n### Step 2: Run Subagent with Context (MANDATORY)\n\n**You MUST call `runSubagent` - do NOT answer the question yourself. The subagent handles the analysis and response.**\n\nUse `runSubagent` with a detailed prompt containing:\n\n1. The fetched content from llms.txt as the knowledge base\n2. The user&#39;s original question\n3. Instructions to:\n   - Analyze the knowledge base content thoroughly\n   - Find relevant information to answer the question\n   - Provide a clear, concise, and accurate answer\n   - Include code examples when relevant\n   - Cite specific sections from the knowledge base if applicable\n   - If the knowledge base doesn&#39;t contain the answer, use general knowledge but note this\n\nExample subagent prompt:\n\nYou are a Vue.js and AI expert. Answer the following question using the provided knowledge base content.\n\nKNOWLEDGE BASE CONTENT:\nfetched_content\n\nUSER QUESTION:\nuser_question\n\nAnalyze thoroughly, provide code examples when relevant, and cite sources from the knowledge base.\n### Step 3: Present Answer\n\nReturn the subagent&#39;s response to the user, formatted appropriately with code blocks and explanations.\n\n## Example\n\n**User asks**: \&quot;How do I use composables in Vue 3?\&quot;\n\n**Execution**:\n1. Fetch https://alexop.dev/llms.txt\n2. **MUST** call runSubagent with the content and question (do NOT skip this)\n3. Return the subagent&#39;s comprehensive answer about Vue 3 composables\n```\n\n---\n\n&lt;Slide layout=\&quot;image\&quot; image={skillExample} alt=\&quot;Generated skill example screenshot\&quot; /&gt;\n---\n\n## Bonus: The askQuestions Tool\n\nVS Code Copilot can **ask clarifying questions** mid-task.\n\n```md\nhelp me to create a workout tracking app use the #askQuestions tool to find out how the tech specs should be\n```\n\n---\n```shell\n┌─────────────────────────────────────────────────────────────┐\n│                     Platform (1/4)                          │\n├─────────────────────────────────────────────────────────────┤\n│ What platform should the workout tracking app target?       │\n├─────────────────────────────────────────────────────────────┤\n│ ★ Web App  Browser-based PWA, accessible anywhere      [✓]  │\n├─────────────────────────────────────────────────────────────┤\n│   iOS Native  Swift/SwiftUI for iPhone                      │\n├─────────────────────────────────────────────────────────────┤\n│   Android Native  Kotlin for Android devices                │\n├─────────────────────────────────────────────────────────────┤\n│   Cross-Platform  React Native or Flutter for iOS &amp; Android │\n├─────────────────────────────────────────────────────────────┤\n│   Desktop  Electron app for Mac/Windows                     │\n├─────────────────────────────────────────────────────────────┤\n│ ✎ Other...  Enter custom answer                             │\n└─────────────────────────────────────────────────────────────┘\n```\n\n---\n\n## Subagent Fan-Out Pattern\n\n**Prompt for VS Code Insiders:**\n\n```\n#runSubagent run 3 subagents that search the web\nand tell me something interesting about Geretsried\n```\n\nThis demonstrates the **fan-out/fan-in pattern** where multiple agents work in parallel.\n\n---\n\n## Live Action: Excalidraw Skill\n\n**Install the skill:**\n\n```bash\nnpx skills add https://github.com/softaworks/agent-toolkit --skill excalidraw\n```\n\nInstall the Excalidraw Extension in VS Code for best experience.\n\n**Prompt to customize with brand colors:**\n\n```\nUpdate the excalidraw skill to use these brand colors:\n\n- Fill: rgb(33, 39, 55)\n- Text: rgb(234, 237, 243)\n- Accent: rgb(255, 107, 237)\n- Card: rgb(52, 63, 96)\n- Card Muted: rgb(138, 51, 123)\n- Border: rgb(171, 75, 153)\n```\n\n→ Agent modifies the skill&#39;s SKILL.md to include color instructions\n\n---\n\n&lt;Slide layout=\&quot;image\&quot; image={robot} alt=\&quot;Robot working on laptop\&quot; /&gt;\n\n---\n\n## More Community Skills\n\n```bash\nnpx skills add https://github.com/anthropics/skills --skill frontend-design\nnpx skills add https://github.com/simonwong/agent-skills --skill code-simplifier\n```\n\n- **frontend-design** — creates polished, production-grade UI components\n- **code-simplifier** — simplifies and refines code for clarity\n\nBrowse and discover skills at [agentskills.io](https://agentskills.io/)\n\n---\n\n&lt;Slide layout=\&quot;section\&quot; /&gt;\n# Key Takeaways\n\n---\n\n&lt;Slide layout=\&quot;center\&quot; /&gt;\n## Key Takeaways\n\n1. **Agents = LLM + Tools + Loop** (nanocode shows this simply)\n2. **Context is finite** — treat tokens as budget\n3. **AGENTS.md** — standardized project context\n4. **Subagents** — specialized agents for complex tasks\n5. **Skills** — portable workflows that load on demand\n\n---\n\n&lt;Slide layout=\&quot;center\&quot; /&gt;\n# Thank You!\nQuestions?\n\n---\n\n&lt;Slide layout=\&quot;section\&quot; /&gt;\n# Resources\n\n---\n\n## Resources\n\n- [VS Code: Using Agents](https://code.visualstudio.com/docs/copilot/agents/overview) - Agent types and session management\n- [Anthropic: Effective Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) - Context engineering guide\n- [VS Code: Introducing Agent Skills](https://www.youtube.com/watch?v=JepVi1tBNEE) - Agent Skills deep dive\n- [VS Code: Context Engineering Guide](https://code.visualstudio.com/docs/copilot/guides/context-engineering-guide) - Microsoft&#39;s context engineering workflow\n- [AGENTS.md](https://agents.md/) - Open standard for agent documentation\n- [Agent Skills Spec](https://agentskills.io/) - Open standard for portable agent skills\n- [nanocode](https://github.com/alexanderop/nanocode) - Minimal agent implementation in TypeScript\n- [Writing a Good CLAUDE.md](https://www.humanlayer.dev/blog/writing-a-good-claude-md) - Best practices for agent documentation\n- [Plausible SEO Skill](https://github.com/alexanderop/claude-plausible-analytics) - Skills deep dive with Plausible example\n- [Don&#39;t Waste Your Back Pressure](https://banay.me/dont-waste-your-backpressure/) - Why automated feedback loops make agents more effective\n- [Workshop Solution](https://github.com/alexanderop/workshop) - Complete code examples from this workshop\n- [Learn Prompt](https://alexop.dev/prompts/claude/claude-learn-command/) - Skill that helps agents learn from conversations\n\n---&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PostCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus-outline inline-flex items-center gap-1.5 rounded-md border border-skin-line bg-skin-card px-2.5 py-1.5 text-xs font-medium text-skin-base opacity-80 transition-all hover:border-skin-accent/50 hover:text-skin-accent hover:opacity-100" aria-label="Copy post as markdown" title="Copy post as markdown for AI/LLM"><svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg><span>Copy Post</span></button><!--astro:end--></astro-island> </div>  <article id="article" class="prose mx-auto mt-8 max-w-5xl astro-vj4tpspi"> <script type="application/json" data-slide-config>{"layout":"cover"}</script> 
<h1 id="next-level-github-copilot">Next Level GitHub Copilot</h1>
<p>Agents.md Subagents &amp; Skills</p>
<p>by Alexander Opalic</p>
<hr/>
<script type="application/json" data-slide-config>{"layout":"image","image":"/_astro/karpathy.BdTcptZL_ZwArMQ.webp"}</script> <figure class="slide-image-fallback"><img src="/_astro/karpathy.BdTcptZL_ZwArMQ.webp" alt="Agent architecture diagram" loading="lazy" decoding="async" fetchpriority="auto" width="1182" height="1150" class="w-full rounded-lg"></figure>
<hr/>
<h2 id="workshop-outline">Workshop Outline<a class="heading-link" aria-label="Link to section" href="#workshop-outline"><span class="heading-link-icon">#</span></a></h2>
<script type="application/json" data-vclick-marker="v-clicks-start">{}</script><ol>
<li>What is an Agent? (LLM → Agent transformation)</li>
<li>Context Engineering (the real skill)</li>
<li>Back Pressure (core validation concept)</li>
<li>AGENTS.md (open standard)</li>
<li>Subagents (specialized invocation)</li>
<li>Skills (portable workflows)</li>
<li>Live Demo</li>
</ol><script type="application/json" data-vclick-marker="v-clicks-end">{}</script>
<hr/>
<script type="application/json" data-slide-config>{"layout":"center"}</script> 
<h2 id="-who-has-used-github-copilot-in-vs-code">🙋 Who has used GitHub Copilot in VS Code?<a class="heading-link" aria-label="Link to section" href="#-who-has-used-github-copilot-in-vs-code"><span class="heading-link-icon">#</span></a></h2>
<hr/>
<script type="application/json" data-slide-config>{"layout":"two-cols-header"}</script> 
<h2 id="about-me">About me<a class="heading-link" aria-label="Link to section" href="#about-me"><span class="heading-link-icon">#</span></a></h2>
<span data-slot-marker="left" style="display:none" aria-hidden="true"></span>
<div class="flex flex-col items-center"><img class="w-72 rounded-full" src="https://avatars.githubusercontent.com/u/33398393?v=4"/><h2 class="mt-4">Alex Opalic</h2></div>
<span data-slot-marker="right" style="display:none" aria-hidden="true"></span>
<script type="application/json" data-vclick-marker="v-clicks-start">{}</script><ul>
<li>🚀 7 years expierence as a full stack developer</li>
<li>💼 Developer at Otto Payments</li>
<li>🏡 Based in Geretsried (south of Munich, Bavaria)</li>
<li>✍️ Blogger at alexop.dev</li>
<li>🎤 Sharing &amp; speaking about Vue, testing &amp; GraphQL &amp; AI</li>
</ul><script type="application/json" data-vclick-marker="v-clicks-end">{}</script>
<hr/>
<script type="application/json" data-slide-config>{"layout":"section"}</script> 
<h1 id="what-is-an-agent">What is an Agent?</h1>
<hr/>
<h2 id="the-transformation-llm--agent">The Transformation: LLM → Agent<a class="heading-link" aria-label="Link to section" href="#the-transformation-llm--agent"><span class="heading-link-icon">#</span></a></h2>
<ul>
<li>At the beginning, an LLM is just a text generator</li>
<li>One problem: the LLM didn’t have access to current news</li>
<li>Solution: all providers gave the LLM access to tools</li>
<li>With tools, the LLM can now interact with the world</li>
<li>This is why an agent is an LLM + Tools + Agentic Loop</li>
</ul>
<hr/>
<script type="application/json" data-slide-config>{"layout":"image","image":"/_astro/agent.DSkKUjm-_ZrAEoi.webp"}</script> <figure class="slide-image-fallback"><img src="/_astro/agent.DSkKUjm-_ZrAEoi.webp" alt="Agent architecture diagram" loading="lazy" decoding="async" fetchpriority="auto" width="1716" height="1716" class="w-full rounded-lg"></figure>
<hr/>
<h2 id="the-agentic-loop-nanocode">The Agentic Loop (nanocode)<a class="heading-link" aria-label="Link to section" href="#the-agentic-loop-nanocode"><span class="heading-link-icon">#</span></a></h2>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="shell"><code><span class="line"><span style="color:#C0CAF5">nanocode</span><span style="color:#89DDFF"> |</span><span style="color:#C0CAF5"> claude-opus-4-5</span><span style="color:#89DDFF"> |</span><span style="color:#C0CAF5"> /Users/alexanderopalic/Projects/typescript/nanocode</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">────────────────────────────────────────────────────────────────────────────────</span></span>
<span class="line"><span style="color:#C0CAF5">❯</span><span style="color:#9ECE6A">  create</span><span style="color:#9ECE6A"> a</span><span style="color:#9ECE6A"> simple</span><span style="color:#9ECE6A"> typescript</span><span style="color:#9ECE6A"> file</span><span style="color:#9ECE6A"> as</span><span style="color:#9ECE6A"> a</span><span style="color:#9ECE6A"> sum</span><span style="color:#9ECE6A"> function</span></span>
<span class="line"><span style="color:#C0CAF5">────────────────────────────────────────────────────────────────────────────────</span></span>
<span class="line"><span style="color:#89DDFF">[</span><span style="color:#A9B1D6">agentLoop</span><span style="color:#89DDFF">]</span><span style="color:#A9B1D6"> Starting with 1 messages</span></span>
<span class="line"><span style="color:#89DDFF">[</span><span style="color:#A9B1D6">agentLoop</span><span style="color:#89DDFF">]</span><span style="color:#A9B1D6"> Got response, stop_reason: tool_use</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">⏺</span><span style="color:#9ECE6A"> Write</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">src/sum.ts</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#C0CAF5">  ⎿</span><span style="color:#9ECE6A">  ok</span></span>
<span class="line"><span style="color:#89DDFF">[</span><span style="color:#A9B1D6">agentLoop</span><span style="color:#89DDFF">]</span><span style="color:#A9B1D6"> Starting with 3 messages</span></span>
<span class="line"><span style="color:#89DDFF">[</span><span style="color:#A9B1D6">agentLoop</span><span style="color:#89DDFF">]</span><span style="color:#A9B1D6"> Got response, stop_reason: end_turn</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">⏺</span><span style="color:#9ECE6A"> Created</span><span style="color:#89DDFF"> `</span><span style="color:#C0CAF5">src/sum.ts</span><span style="color:#89DDFF">`</span><span style="color:#C0CAF5"> with</span><span style="color:#9ECE6A"> a</span><span style="color:#9ECE6A"> simple</span><span style="color:#9ECE6A"> sum</span><span style="color:#9ECE6A"> function</span><span style="color:#9ECE6A"> that</span><span style="color:#9ECE6A"> takes</span><span style="color:#9ECE6A"> two</span><span style="color:#9ECE6A"> numbers</span><span style="color:#9ECE6A"> and</span><span style="color:#9ECE6A"> returns</span><span style="color:#9ECE6A"> their</span><span style="color:#9ECE6A"> sum.</span></span></code><button type="button" class="copy" data-code="nanocode | claude-opus-4-5 | /Users/alexanderopalic/Projects/typescript/nanocode

────────────────────────────────────────────────────────────────────────────────
❯  create a simple typescript file as a sum function
────────────────────────────────────────────────────────────────────────────────
[agentLoop] Starting with 1 messages
[agentLoop] Got response, stop_reason: tool_use

⏺ Write(src/sum.ts)
  ⎿  ok
[agentLoop] Starting with 3 messages
[agentLoop] Got response, stop_reason: end_turn

⏺ Created `src/sum.ts` with a simple sum function that takes two numbers and returns their sum." onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><strong>~350 lines of TypeScript</strong> to understand how Claude Code works.</p>
<hr/>
<h2 id="the-agentic-loop-code">The Agentic Loop (Code)<a class="heading-link" aria-label="Link to section" href="#the-agentic-loop-code"><span class="heading-link-icon">#</span></a></h2>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#9D7CD8;font-style:italic">async</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> agentLoop</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">messages</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Message</span><span style="color:#9ABDF5">[]</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> systemPrompt</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Promise</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Message</span><span style="color:#9ABDF5">[]</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> response</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#7AA2F7"> callApi</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">messages</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> systemPrompt</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#7AA2F7">  printResponse</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">response</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> toolResults</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#7AA2F7"> processToolCalls</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">response</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">content</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> newMessages</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> [</span><span style="color:#F7768E;font-weight:bold">...</span><span style="color:#7DCFFF">messages</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">role</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">assistant</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> content</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> response</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">content</span><span style="color:#9ABDF5"> }]</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">toolResults</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">length</span><span style="color:#BB9AF7"> ===</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#C0CAF5"> newMessages</span><span style="color:#51597D;font-style:italic">  // No tools called, we&#39;re done</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#7AA2F7"> agentLoop</span><span style="color:#9ABDF5">(  </span><span style="color:#51597D;font-style:italic">// Loop again with tool results</span></span>
<span class="line"><span style="color:#9ABDF5">    [</span><span style="color:#F7768E;font-weight:bold">...</span><span style="color:#7DCFFF">newMessages</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">role</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">user</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> content</span><span style="color:#89DDFF">:</span><span style="color:#7DCFFF"> toolResults</span><span style="color:#9ABDF5"> }]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    systemPrompt</span></span>
<span class="line"><span style="color:#9ABDF5">  )</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="async function agentLoop(messages: Message[], systemPrompt: string): Promise<Message[]> {
  const response = await callApi(messages, systemPrompt)
  printResponse(response)

  const toolResults = await processToolCalls(response.content)
  const newMessages = [...messages, { role: 'assistant', content: response.content }]

  if (toolResults.length === 0) {
    return newMessages  // No tools called, we're done
  }

  return agentLoop(  // Loop again with tool results
    [...newMessages, { role: 'user', content: toolResults }],
    systemPrompt
  )
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>The entire request → response → execute → loop cycle in ~15 lines.</p>
<hr/>
<h2 id="tool-registration">Tool Registration<a class="heading-link" aria-label="Link to section" href="#tool-registration"><span class="heading-link-icon">#</span></a></h2>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> TOOLS</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> Map</span><span style="color:#9ABDF5">([</span></span>
<span class="line"><span style="color:#9ABDF5">  [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">read</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">    description</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Read file with line numbers</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    schema</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span><span style="color:#73DACA"> path</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">string</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> offset</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">number?</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> limit</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">number?</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    execute</span><span style="color:#89DDFF">:</span><span style="color:#7DCFFF"> read</span></span>
<span class="line"><span style="color:#9ABDF5">  }]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">write</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">    description</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Write content to file</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    schema</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span><span style="color:#73DACA"> path</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">string</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> content</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">string</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    execute</span><span style="color:#89DDFF">:</span><span style="color:#7DCFFF"> write</span></span>
<span class="line"><span style="color:#9ABDF5">  }]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">bash</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">    description</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Run shell command</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    schema</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span><span style="color:#73DACA"> cmd</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">string</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    execute</span><span style="color:#89DDFF">:</span><span style="color:#7DCFFF"> bash</span></span>
<span class="line"><span style="color:#9ABDF5">  }]</span></span>
<span class="line"><span style="color:#9ABDF5">])</span></span></code><button type="button" class="copy" data-code="const TOOLS = new Map([
  ['read', {
    description: 'Read file with line numbers',
    schema: { path: 'string', offset: 'number?', limit: 'number?' },
    execute: read
  }],
  ['write', {
    description: 'Write content to file',
    schema: { path: 'string', content: 'string' },
    execute: write
  }],
  ['bash', {
    description: 'Run shell command',
    schema: { cmd: 'string' },
    execute: bash
  }]
])" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr/>
<h2 id="a-complete-tool-implementation">A Complete Tool Implementation<a class="heading-link" aria-label="Link to section" href="#a-complete-tool-implementation"><span class="heading-link-icon">#</span></a></h2>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#9D7CD8;font-style:italic">async</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> read</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">args</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Record</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">string</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> unknown</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Promise</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">string</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> path</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> args</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">path</span><span style="color:#89DDFF"> as</span><span style="color:#0DB9D7"> string</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> text</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#C0CAF5"> Bun</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">file</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">path</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">text</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> lines</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> text</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">split</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;\n&#39;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> offset</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">args</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">offset</span><span style="color:#89DDFF"> as</span><span style="color:#0DB9D7"> number</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">??</span><span style="color:#FF9E64"> 0</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> limit</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">args</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">limit</span><span style="color:#89DDFF"> as</span><span style="color:#0DB9D7"> number</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">??</span><span style="color:#C0CAF5"> lines</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">length</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#C0CAF5"> lines</span></span>
<span class="line"><span style="color:#89DDFF">    .</span><span style="color:#7AA2F7">slice</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">offset</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> offset</span><span style="color:#89DDFF"> +</span><span style="color:#C0CAF5"> limit</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#89DDFF">    .</span><span style="color:#7AA2F7">map</span><span style="color:#9ABDF5">((</span><span style="color:#E0AF68">line</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> i</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#89DDFF"> `</span><span style="color:#7DCFFF">${</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">offset</span><span style="color:#89DDFF"> +</span><span style="color:#C0CAF5"> i</span><span style="color:#89DDFF"> +</span><span style="color:#FF9E64"> 1</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toString</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">padStart</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">4</span><span style="color:#9ABDF5">)</span><span style="color:#7DCFFF">}</span><span style="color:#9ECE6A">| </span><span style="color:#7DCFFF">${</span><span style="color:#C0CAF5">line</span><span style="color:#7DCFFF">}</span><span style="color:#89DDFF">`</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#89DDFF">    .</span><span style="color:#7AA2F7">join</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;\n&#39;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="async function read(args: Record<string, unknown>): Promise<string> {
  const path = args.path as string
  const text = await Bun.file(path).text()
  const lines = text.split('\n')
  const offset = (args.offset as number) ?? 0
  const limit = (args.limit as number) ?? lines.length
  return lines
    .slice(offset, offset + limit)
    .map((line, i) => `${(offset + i + 1).toString().padStart(4)}| ${line}`)
    .join('\n')
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr/>
<script type="application/json" data-slide-config>{"layout":"image","image":"/_astro/agentTools.BnhwP17B_Z2iINoQ.webp"}</script> <figure class="slide-image-fallback"><img src="/_astro/agentTools.BnhwP17B_Z2iINoQ.webp" alt="Agent tools overview" loading="lazy" decoding="async" fetchpriority="auto" width="1672" height="1116" class="w-full rounded-lg"></figure>
<hr/>
<h2 id="vs-code-copilot-built-in-tools">VS Code Copilot Built-in Tools<a class="heading-link" aria-label="Link to section" href="#vs-code-copilot-built-in-tools"><span class="heading-link-icon">#</span></a></h2>
<ul>
<li>⟨⟩ <strong>agent</strong> — Delegate tasks to other agents</li>
<li>ⓘ <strong>askQuestions</strong> — Ask questions to clarify requirements</li>
<li>✎ <strong>edit</strong> — Edit files in your workspace</li>
<li>▷ <strong>execute</strong> — Execute code and applications</li>
<li>⧉ <strong>read</strong> — Read files in your workspace</li>
<li>🔍 <strong>search</strong> — Search files in your workspace</li>
<li>≡ <strong>todo</strong> — Manage and track todo items</li>
<li>✕ <strong>vscode</strong> — Use VS Code features</li>
<li>🌐 <strong>web</strong> — Fetch information from the web</li>
</ul>
<hr/>
<script type="application/json" data-slide-config>{"layout":"section"}</script> 
<h1 id="context-engineering">Context Engineering</h1>
<hr/>
<script type="application/json" data-slide-config>{"layout":"image","image":"/_astro/agentContext.OCzhBjwD_26x2gM.webp"}</script> <figure class="slide-image-fallback"><img src="/_astro/agentContext.OCzhBjwD_26x2gM.webp" alt="Agent context engineering" loading="lazy" decoding="async" fetchpriority="auto" width="1716" height="1716" class="w-full rounded-lg"></figure>
<hr/>
<script>(()=>{var a=(s,i,o)=>{let r=async()=>{await(await s())()},t=typeof i.value=="object"?i.value:void 0,c={rootMargin:t==null?void 0:t.rootMargin},n=new IntersectionObserver(e=>{for(let l of e)if(l.isIntersecting){n.disconnect(),r();break}},c);for(let e of o.children)n.observe(e)};(self.Astro||(self.Astro={})).visible=a;window.dispatchEvent(new Event("astro:visible"));})();</script><astro-island uid="ZidCPP" prefix="r28" component-url="/_astro/ContextWindowVisualizer.YlsTKjWa.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{}" ssr client="visible" opts="{&quot;name&quot;:&quot;ContextWindowVisualizer&quot;,&quot;value&quot;:true}" await-children><div class="w-full max-w-3xl mx-auto my-8"><div class="rounded-lg overflow-hidden border border-[rgb(var(--color-border))] shadow-2xl"><div class="flex items-center gap-2 px-4 py-3 bg-[rgb(var(--color-card))] border-b border-[rgb(var(--color-border))]"><div class="flex gap-2"><div class="w-3 h-3 rounded-full bg-red-500/80"></div><div class="w-3 h-3 rounded-full bg-yellow-500/80"></div><div class="w-3 h-3 rounded-full bg-green-500/80"></div></div><div class="flex-1 text-center"><span class="text-sm text-[rgb(var(--color-text-base))] opacity-60 font-mono">context-window-demo</span></div><button class="text-xs px-2 py-1 rounded border border-[rgb(var(--color-border))]
                       text-[rgb(var(--color-text-base))] opacity-60 hover:opacity-100
                       hover:border-[rgb(var(--color-accent))] transition-all">Reset</button></div><div class="bg-[rgb(var(--color-fill))] font-mono text-sm"><div class="px-4 py-3 border-b border-[rgb(var(--color-border))]"><div class="flex items-center justify-between mb-2"><span class="text-[rgb(var(--color-accent))]">CONTEXT WINDOW</span><span class="text-[rgb(var(--color-text-base))] opacity-70">3.1k<!-- --> / <!-- -->200.0k<!-- --> tokens (<!-- -->1.6<!-- -->%)</span></div><div class="h-2 bg-[rgb(var(--color-card))] rounded-full overflow-hidden"><div class="h-full bg-[rgb(var(--color-accent))] transition-all duration-300" style="width:1.55%"></div></div><div class="flex justify-between mt-1 text-xs text-[rgb(var(--color-text-base))] opacity-50"><span>Used: <!-- -->1.6<!-- -->%</span><span>Remaining: <!-- -->98.5<!-- -->%</span></div></div><div class="p-4 max-h-80 overflow-y-auto"><div class="border border-[rgb(var(--color-border))] rounded"><div class="px-3 py-2 bg-[rgb(var(--color-card))] border-b border-[rgb(var(--color-border))] text-xs text-[rgb(var(--color-text-base))] opacity-70">messages: Message[] = [</div><div class="divide-y divide-[rgb(var(--color-border))]"><div class="px-3 py-2 flex items-start gap-3 hover:bg-[rgb(var(--color-card))] transition-colors"><span class="text-[rgb(var(--color-text-base))] opacity-50 w-16 flex-shrink-0">[<!-- -->0<!-- -->]</span><div class="flex-1 min-w-0"><span class="text-purple-400 font-medium">System<!-- -->:</span><span class="text-[rgb(var(--color-text-base))] ml-2 break-words">&quot;<!-- -->System prompt + CLAUDE.md<!-- -->&quot;</span></div><span class="text-[rgb(var(--color-text-base))] opacity-50 text-xs flex-shrink-0">3100<!-- --> tok</span></div><div class="px-3 py-2 flex items-center gap-3 text-[rgb(var(--color-accent))]"><span class="opacity-50 w-16 flex-shrink-0">[<!-- -->1<!-- -->]</span><span class="flex items-center"><span class="mr-2">← You are here</span><span class="inline-block w-2 h-4 bg-[rgb(var(--color-accent))] opacity-100 transition-opacity duration-100"></span></span></div></div><div class="px-3 py-2 bg-[rgb(var(--color-card))] border-t border-[rgb(var(--color-border))] text-xs text-[rgb(var(--color-text-base))] opacity-70">]</div></div><div class="mt-4 border border-dashed border-[rgb(var(--color-border))] rounded p-3 text-center"><div class="text-[rgb(var(--color-text-base))] opacity-50 text-xs mb-1">Yesterday&#x27;s session?</div><div class="text-[rgb(var(--color-text-base))] opacity-70">∅ Not in the array. Doesn&#x27;t exist.</div></div></div><form class="border-t border-[rgb(var(--color-border))]"><div class="flex items-center px-4 py-3"><span class="text-[rgb(var(--color-accent))] mr-2">❯</span><input type="text" placeholder="Type a message to see context fill up..." class="flex-1 bg-transparent text-[rgb(var(--color-text-base))] outline-none
                           placeholder:text-[rgb(var(--color-text-base))] placeholder:opacity-30" value=""/><button type="submit" class="ml-2 px-3 py-1 rounded border border-[rgb(var(--color-accent))]
                           text-[rgb(var(--color-accent))] text-sm hover:bg-[rgb(var(--color-accent))]
                           hover:text-[rgb(var(--color-fill))] transition-all">Send</button></div></form></div></div><p class="text-center mt-4 text-sm text-[rgb(var(--color-text-base))] opacity-50">Each message you send adds to the array. The context window is just a sliding array of messages.</p></div><!--astro:end--></astro-island>
<hr/>
<script type="application/json" data-slide-config>{"layout":"quote"}</script> 
<blockquote>
<p>“Context engineering is the art and science of filling the context window with just the right information at each step of an agent’s trajectory.”</p>
<p>— LangChain/Manus webinar</p>
</blockquote>
<hr/>
<h2 id="context-window-utilization">Context Window Utilization<a class="heading-link" aria-label="Link to section" href="#context-window-utilization"><span class="heading-link-icon">#</span></a></h2>
<astro-island uid="ZnlfoX" prefix="r29" component-url="/_astro/ContextUtilizationVisualizer.DYnJwqvK.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{}" ssr client="visible" opts="{&quot;name&quot;:&quot;ContextUtilizationVisualizer&quot;,&quot;value&quot;:true}" await-children><div class="w-full max-w-2xl mx-auto my-8"><div class="rounded-lg overflow-hidden border border-[rgb(var(--color-border))] shadow-2xl"><div class="bg-[rgb(var(--color-fill))] font-mono text-sm p-6"><div class="mb-8"><div class="relative"><div class="h-10 flex rounded-lg overflow-hidden border border-[rgb(var(--color-border))]"><div class="h-full flex items-center justify-center text-xs font-medium transition-opacity" style="width:40%;background-color:rgba(34, 197, 94, 0.2);color:rgb(34, 197, 94);opacity:1">Smart</div><div class="h-full flex items-center justify-center text-xs font-medium transition-opacity" style="width:20%;background-color:rgba(234, 179, 8, 0.2);color:rgb(234, 179, 8);opacity:0.4">Optimal</div><div class="h-full flex items-center justify-center text-xs font-medium transition-opacity" style="width:20%;background-color:rgba(249, 115, 22, 0.2);color:rgb(249, 115, 22);opacity:0.4">Degraded</div><div class="h-full flex items-center justify-center text-xs font-medium transition-opacity" style="width:20%;background-color:rgba(239, 68, 68, 0.2);color:rgb(239, 68, 68);opacity:0.4">Critical</div></div><div class="flex justify-between mt-1 text-xs text-[rgb(var(--color-text-base))] opacity-50"><span>0%</span><span style="margin-left:30%">40%</span><span style="margin-left:10%">60%</span><span style="margin-left:10%">80%</span><span>100%</span></div><div class="absolute top-0 w-1 h-10 bg-white rounded-full shadow-lg" style="box-shadow:0 0 8px rgb(34, 197, 94)"></div></div></div><div class="flex items-center justify-center gap-8 mb-8"><svg viewBox="0 0 100 100" class="w-24 h-24"><circle cx="50" cy="50" r="45" fill="rgba(34, 197, 94, 0.2)" stroke="rgb(34, 197, 94)" stroke-width="3"></circle><g><ellipse cx="33" cy="40" rx="5.375" ry="5.375" fill="rgb(34, 197, 94)"></ellipse><circle cx="33" r="2" fill="white"></circle></g><g><ellipse cx="67" cy="40" rx="5.375" ry="5.375" fill="rgb(34, 197, 94)"></ellipse><circle cx="67" r="2" fill="white"></circle></g><line x1="25" x2="40" stroke="rgb(34, 197, 94)" stroke-width="2" stroke-linecap="round"></line><line x1="60" x2="75" stroke="rgb(34, 197, 94)" stroke-width="2" stroke-linecap="round"></line><path d="M 30 65 Q 50 75.625 70 65" fill="none" stroke="rgb(34, 197, 94)" stroke-width="3" stroke-linecap="round"></path></svg><div class="text-center"><div class="text-4xl font-bold mb-1" style="color:rgb(34, 197, 94)">25<!-- -->%</div><div class="text-sm font-medium" style="color:rgb(34, 197, 94)">Smart Zone</div></div></div><div><input type="range" min="0" max="99" class="w-full h-3 rounded-lg appearance-none cursor-pointer" style="background:linear-gradient(to right,
                  rgb(34, 197, 94) 0%,
                  rgb(34, 197, 94) 40%,
                  rgb(234, 179, 8) 40%,
                  rgb(234, 179, 8) 60%,
                  rgb(249, 115, 22) 60%,
                  rgb(249, 115, 22) 80%,
                  rgb(239, 68, 68) 80%,
                  rgb(239, 68, 68) 100%)" value="25"/><style>
              input[type=&quot;range&quot;]::-webkit-slider-thumb {
                appearance: none;
                width: 20px;
                height: 20px;
                border-radius: 50%;
                background: white;
                cursor: pointer;
                box-shadow: 0 2px 6px rgba(0,0,0,0.3);
                border: 2px solid rgb(34, 197, 94);
                transition: border-color 0.3s;
              }
              input[type=&quot;range&quot;]::-moz-range-thumb {
                width: 20px;
                height: 20px;
                border-radius: 50%;
                background: white;
                cursor: pointer;
                box-shadow: 0 2px 6px rgba(0,0,0,0.3);
                border: 2px solid rgb(34, 197, 94);
              }
            </style></div></div></div></div><!--astro:end--></astro-island>
<hr/>
<astro-island uid="Z1EumNJ" prefix="r30" component-url="/_astro/ContextFillupVisualizer.CJ_jj5_T.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{}" ssr client="visible" opts="{&quot;name&quot;:&quot;ContextFillupVisualizer&quot;,&quot;value&quot;:true}" await-children><div class="my-8 rounded-lg bg-[rgb(var(--color-fill))] p-4"><style>
        @keyframes fadeIn {
          from { opacity: 0; transform: translateY(-10px); }
          to { opacity: 1; transform: translateY(0); }
        }
        @keyframes fadeOut {
          from { opacity: 1; transform: scale(1); }
          to { opacity: 0; transform: scale(0.8); }
        }
        @keyframes pulse {
          0%, 100% { transform: scale(1); }
          50% { transform: scale(1.05); }
        }
        .block-fade-in {
          animation: fadeIn 0.4s ease-out forwards;
        }
        .block-fade-out {
          animation: fadeOut 0.6s ease-in forwards;
        }
        .scissors-animate {
          animation: pulse 0.5s ease-in-out infinite;
        }
      </style><div class="mb-4 flex flex-wrap items-center justify-between gap-2"><h3 class="text-lg font-semibold text-[rgb(var(--color-text-base))]">Context Window Visualization</h3><div class="flex items-center gap-2"><select class="rounded border border-[rgb(var(--color-border))] bg-[rgb(var(--color-card))] px-2 py-1 text-sm text-[rgb(var(--color-text-base))]"><option value="0.5">0.5x</option><option value="1" selected="">1x</option><option value="2">2x</option><option value="3">3x</option></select><button class="rounded bg-[rgb(var(--color-accent))] px-3 py-1 text-sm text-[rgb(var(--color-fill))] transition hover:opacity-80">Play</button><button class="rounded border border-[rgb(var(--color-border))] px-3 py-1 text-sm text-[rgb(var(--color-text-base))] transition hover:opacity-80">Reset</button></div></div><div class="mb-4"><div class="mb-1 flex justify-between text-xs text-[rgb(var(--color-text-base))] opacity-60"><span>2,000<!-- --> / <!-- -->20,000<!-- --> tokens</span><span>10.0<!-- -->%</span></div><div class="h-3 overflow-hidden rounded-full bg-[rgb(var(--color-card))]"><div class="h-full transition-all duration-300" style="width:10%;background-color:#10B981"></div></div></div><div class="relative max-h-[400px] min-h-[300px] overflow-y-auto rounded-lg border-2 border-dashed border-[rgb(var(--color-border))] bg-[rgb(var(--color-card))] p-4"><div class="flex flex-col gap-2"><div class="flex items-center justify-between rounded-full px-4 py-2 text-sm font-medium text-white block-fade-in" style="background:#3B82F6;min-width:30%"><span>System Prompt</span><span class="ml-2 text-xs opacity-80">2,000</span></div></div></div><div class="mt-4 flex flex-wrap gap-3 text-xs"><div class="flex items-center gap-1"><div class="h-3 w-3 rounded-full" style="background:#3B82F6"></div><span class="text-[rgb(var(--color-text-base))] opacity-60">system</span></div><div class="flex items-center gap-1"><div class="h-3 w-3 rounded-full" style="background:#10B981"></div><span class="text-[rgb(var(--color-text-base))] opacity-60">doc</span></div><div class="flex items-center gap-1"><div class="h-3 w-3 rounded-full" style="background:#8B5CF6"></div><span class="text-[rgb(var(--color-text-base))] opacity-60">memory</span></div><div class="flex items-center gap-1"><div class="h-3 w-3 rounded-full" style="background:#F97316"></div><span class="text-[rgb(var(--color-text-base))] opacity-60">tool</span></div><div class="flex items-center gap-1"><div class="h-3 w-3 rounded-full" style="background:#EAB308"></div><span class="text-[rgb(var(--color-text-base))] opacity-60">user</span></div><div class="flex items-center gap-1"><div class="h-3 w-3 rounded-full" style="background:#6B7280"></div><span class="text-[rgb(var(--color-text-base))] opacity-60">history</span></div><div class="flex items-center gap-1"><div class="h-3 w-3 rounded-full" style="background:linear-gradient(135deg, #6366F1 0%, #8B5CF6 50%, #A855F7 100%)"></div><span class="text-[rgb(var(--color-text-base))] opacity-60">conversation summary</span></div></div></div><!--astro:end--></astro-island>
<hr/>
<h2 id="three-long-horizon-techniques">Three Long-Horizon Techniques<a class="heading-link" aria-label="Link to section" href="#three-long-horizon-techniques"><span class="heading-link-icon">#</span></a></h2>
<p>From <a href="https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents" rel="noopener noreferrer" target="_blank">Anthropic’s guide</a>:</p>
<script type="application/json" data-vclick-marker="v-clicks-start">{}</script><ol>
<li><strong>Compaction</strong> — Summarize history, reset periodically</li>
<li><strong>Structured note-taking</strong> — External memory systems</li>
<li><strong>Sub-agent architectures</strong> — Distribute work across focused contexts</li>
</ol><script type="application/json" data-vclick-marker="v-clicks-end">{}</script>
<hr/>
<script type="application/json" data-slide-config>{"layout":"section"}</script> 
<h1 id="back-pressure">Back Pressure</h1>
<hr/>
<h2 id="why-back-pressure-matters">Why Back Pressure Matters<a class="heading-link" aria-label="Link to section" href="#why-back-pressure-matters"><span class="heading-link-icon">#</span></a></h2>
<p><strong>Back pressure</strong> = automated feedback that validates agent work</p>
<script type="application/json" data-vclick-marker="v-clicks-start">{}</script><ul>
<li>Without back pressure, <strong>you</strong> become the validation layer</li>
<li>Agents cannot self-correct if nothing tells them something is wrong</li>
<li>With good back pressure, agents detect mistakes and iterate until correct</li>
</ul><script type="application/json" data-vclick-marker="v-clicks-end">{}</script>
<blockquote>
<p>“If you’re directly responsible for checking each line is valid, that’s time taken away from higher-level goals.”</p>
</blockquote>
<hr/>
<h2 id="back-pressure-sources">Back Pressure Sources<a class="heading-link" aria-label="Link to section" href="#back-pressure-sources"><span class="heading-link-icon">#</span></a></h2>

























<table><thead><tr><th>Source</th><th>What It Validates</th></tr></thead><tbody><tr><td data-label="Source"><strong>Type system</strong></td><td data-label="What It Validates">Types, interfaces, contracts</td></tr><tr><td data-label="Source"><strong>Build tools</strong></td><td data-label="What It Validates">Syntax, imports, compilation</td></tr><tr><td data-label="Source"><strong>Tests</strong></td><td data-label="What It Validates">Logic, behavior, regressions</td></tr><tr><td data-label="Source"><strong>Linters</strong></td><td data-label="What It Validates">Style, patterns, best practices</td></tr></tbody></table>
<p><strong>Key insight:</strong> Expressive type systems + good error messages = agents can self-correct.</p>
<hr/>
<script type="application/json" data-slide-config>{"layout":"section"}</script> 
<h1 id="agentsmd">AGENTS.md</h1>
<hr/>
<h2 id="what-is-agentsmd">What is AGENTS.md?<a class="heading-link" aria-label="Link to section" href="#what-is-agentsmd"><span class="heading-link-icon">#</span></a></h2>
<p><strong>What:</strong> An open standard for agent-specific documentation</p>
<p><strong>Where:</strong> Repository root (works in monorepos too)</p>
<p><strong>Who:</strong> Works with Copilot, Claude, Cursor, Devin, 20+ agents</p>
<blockquote>
<p>“While README.md targets humans, AGENTS.md contains the extra context coding agents need.”</p>
</blockquote>
<hr/>
<script type="application/json" data-slide-config>{"layout":"iframe","src":"https://agents.md/","title":"AGENTS.md - Open Standard"}</script> <div class="slide-iframe-fallback"><iframe src="https://agents.md/" title="AGENTS.md - Open Standard" class="slide-iframe-blog" loading="lazy" sandbox="allow-scripts allow-forms allow-same-origin allow-popups"></iframe></div>
<hr/>
<h2 id="agentsmd-structure">AGENTS.md Structure<a class="heading-link" aria-label="Link to section" href="#agentsmd-structure"><span class="heading-link-icon">#</span></a></h2>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF;font-weight:bold">#</span><span style="color:#89DDFF;font-weight:bold"> AGENTS.md</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Dev Environment</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> How to set up and navigate</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Build &amp; Test Commands</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#89DDFF"> `pnpm install &amp;&amp; pnpm dev`</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#89DDFF"> `pnpm test:unit`</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Code Style</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> TypeScript strict mode</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Prefer composition over inheritance</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> PR Instructions</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Keep PRs small and focused</span></span></code><button type="button" class="copy" data-code="# AGENTS.md

## Dev Environment
- How to set up and navigate

## Build &#38; Test Commands
- `pnpm install &#38;&#38; pnpm dev`
- `pnpm test:unit`

## Code Style
- TypeScript strict mode
- Prefer composition over inheritance

## PR Instructions
- Keep PRs small and focused" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><strong>Key:</strong> No required fields—use what helps your project.</p>
<hr/>
<script type="application/json" data-slide-config>{"layout":"image","image":"/_astro/bloatedAgent.GiKgOgA-_Z1dJ1EQ.webp"}</script> <figure class="slide-image-fallback"><img src="/_astro/bloatedAgent.GiKgOgA-_Z1dJ1EQ.webp" alt loading="lazy" decoding="async" fetchpriority="auto" width="1396" height="1014" class="w-full rounded-lg"></figure>
<hr/>
<script type="application/json" data-slide-config>{"layout":"two-cols-header"}</script> 
<h2 id="before-vs-after-progressive-disclosure">Before vs After: Progressive Disclosure<a class="heading-link" aria-label="Link to section" href="#before-vs-after-progressive-disclosure"><span class="heading-link-icon">#</span></a></h2>
<span data-slot-marker="left" style="display:none" aria-hidden="true"></span>
<h3 class="text-red-400 font-bold text-xl mb-4">❌ Bloated (847 lines)</h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF;font-weight:bold">#</span><span style="color:#89DDFF;font-weight:bold"> AGENTS.md</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> API Endpoints</span></span>
<span class="line"><span style="color:#9AA5CE">[200 lines of docs...]</span></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Testing Strategy</span></span>
<span class="line"><span style="color:#9AA5CE">[150 lines of docs...]</span></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Architecture</span></span>
<span class="line"><span style="color:#9AA5CE">[300 lines of docs...]</span></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Code Style</span></span>
<span class="line"><span style="color:#9AA5CE">[100 lines of rules...]</span></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Deployment</span></span>
<span class="line"><span style="color:#9AA5CE">[97 lines of docs...]</span></span></code><button type="button" class="copy" data-code="# AGENTS.md

## API Endpoints
[200 lines of docs...]
## Testing Strategy
[150 lines of docs...]
## Architecture
[300 lines of docs...]
## Code Style
[100 lines of rules...]
## Deployment
[97 lines of docs...]" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p class="text-yellow-400 mt-4 text-sm">40% context consumed before work starts</p>
<span data-slot-marker="right" style="display:none" aria-hidden="true"></span>
<h3 class="text-green-400 font-bold text-xl mb-4">✅ Lean (58 lines)</h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF;font-weight:bold">#</span><span style="color:#89DDFF;font-weight:bold"> AGENTS.md</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Quick Start</span></span>
<span class="line"><span style="color:#9AA5CE">pnpm install &amp;&amp; pnpm dev</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Docs Reference</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Doc </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> When to read </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|-----|--------------|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> docs/api.md </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> API work </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> docs/testing.md </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Tests </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> docs/arch.md </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Design </span><span style="color:#89DDFF">|</span></span></code><button type="button" class="copy" data-code="# AGENTS.md

## Quick Start
pnpm install &#38;&#38; pnpm dev

## Docs Reference
| Doc | When to read |
|-----|--------------|
| docs/api.md | API work |
| docs/testing.md | Tests |
| docs/arch.md | Design |" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p class="text-cyan-400 mt-4 text-sm">Docs loaded on-demand when needed</p>
<hr/>
<script type="application/json" data-slide-config>{"layout":"image","image":"/_astro/progressiveDisc.DJR1s0d9_ecuq5.webp"}</script> <figure class="slide-image-fallback"><img src="/_astro/progressiveDisc.DJR1s0d9_ecuq5.webp" alt="Progressive disclosure diagram" loading="lazy" decoding="async" fetchpriority="auto" width="1360" height="870" class="w-full rounded-lg"></figure>
<hr/>
<h2 id="the-learn-skill">The /learn Skill<a class="heading-link" aria-label="Link to section" href="#the-learn-skill"><span class="heading-link-icon">#</span></a></h2>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF;font-weight:bold">#</span><span style="color:#89DDFF;font-weight:bold"> Learn from Conversation</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Phase 1: Deep Analysis</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> What patterns or approaches were discovered?</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> What gotchas or pitfalls were encountered?</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> What architecture decisions were made?</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Phase 2: Categorize &amp; Locate</span></span>
<span class="line"><span style="color:#9AA5CE">Read existing docs to find the best home.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Phase 3: Draft the Learning</span></span>
<span class="line"><span style="color:#9AA5CE">Format to match existing doc style.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Phase 4: User Approval (BLOCKING)</span></span>
<span class="line"><span style="color:#9AA5CE">Present changes, wait for explicit approval.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Phase 5: Save</span></span>
<span class="line"><span style="color:#9AA5CE">After approval, save the learning.</span></span></code><button type="button" class="copy" data-code="# Learn from Conversation

## Phase 1: Deep Analysis
- What patterns or approaches were discovered?
- What gotchas or pitfalls were encountered?
- What architecture decisions were made?

## Phase 2: Categorize &#38; Locate
Read existing docs to find the best home.

## Phase 3: Draft the Learning
Format to match existing doc style.

## Phase 4: User Approval (BLOCKING)
Present changes, wait for explicit approval.

## Phase 5: Save
After approval, save the learning." onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr/>
<script type="application/json" data-slide-config>{"layout":"section"}</script> 
<h1 id="subagents">Subagents</h1>
<hr/>
<h2 id="subagents-in-vs-code">Subagents in VS Code<a class="heading-link" aria-label="Link to section" href="#subagents-in-vs-code"><span class="heading-link-icon">#</span></a></h2>
<p><strong>How to invoke:</strong></p>
<script type="application/json" data-vclick-marker="v-clicks-start">{}</script><ol>
<li>Enable tools in Copilot Chat (hammer icon)</li>
<li>Call explicitly with <code>#runSubagent</code></li>
<li>Or accept when Copilot suggests one</li>
</ol><script type="application/json" data-vclick-marker="v-clicks-end">{}</script>
<hr/>
<h2 id="use-cases">Use Cases<a class="heading-link" aria-label="Link to section" href="#use-cases"><span class="heading-link-icon">#</span></a></h2>
<script type="application/json" data-vclick-marker="v-clicks-start">{}</script><ul>
<li>Specialized searches (explore codebase, web, docs)</li>
<li>Long-running tasks (data analysis, refactoring)</li>
<li>TDD workflows (test generation, validation)</li>
<li>Multi-step processes (research, summarize, act)</li>
</ul><script type="application/json" data-vclick-marker="v-clicks-end">{}</script>
<hr/>
<h2 id="explore-subagent-flow">Explore Subagent Flow<a class="heading-link" aria-label="Link to section" href="#explore-subagent-flow"><span class="heading-link-icon">#</span></a></h2>
<div class="subagent-diagram-container astro-tpygpejy" data-subagent-diagram> <!-- Animated React component (shown in presentation mode via CSS) --> <!-- Using client:load instead of client:visible because CSS hides this with display:none --> <!-- until presentation mode activates, which prevents IntersectionObserver from firing --> <astro-island uid="1P9sOl" prefix="r24" component-url="/_astro/SubagentDiagramRenderer.DLSSo-ru.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;config&quot;:[0,{&quot;task&quot;:[0,&quot;Find auth files&quot;],&quot;files&quot;:[1,[[0,&quot;Auth.tsx&quot;],[0,&quot;auth.ts&quot;],[0,&quot;authService.ts&quot;]]],&quot;autoStart&quot;:[0,false],&quot;speed&quot;:[0,0.6]}]}" ssr client="load" opts="{&quot;name&quot;:&quot;SubagentDiagramRenderer&quot;,&quot;value&quot;:true}" await-children><div class="subagent-diagram-animated"><svg viewBox="0 0 620 420" class="subagent-diagram-svg-animated"><defs><marker id="arrowhead-animated" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0, 10 3.5, 0 7" class="arrowhead-fill"></polygon></marker></defs><g class="agent-node main-agent"><circle cx="100" cy="80" r="45" class="agent-circle main"></circle><text x="100" y="72" text-anchor="middle" class="agent-icon">🤖</text><text x="100" y="95" text-anchor="middle" class="agent-label">Main Agent</text></g><g class="file-tree" transform="translate(340, 50)"><text x="0" y="0" class="tree-header">File Tree</text><line x1="0" y1="10" x2="180" y2="10" class="tree-header-line"></line><g opacity="0.7"><text x="0" y="35" class="tree-node folder ">📁<!-- --> <!-- -->src/</text></g><g opacity="0.7"><text x="16" y="61" class="tree-node folder ">📁<!-- --> <!-- -->components/</text></g><g opacity="0.7"><text x="32" y="87" class="tree-node file ">📄<!-- --> <!-- -->Auth.tsx</text></g><g opacity="0.7"><text x="32" y="113" class="tree-node file ">📄<!-- --> <!-- -->Button.tsx</text></g><g opacity="0.7"><text x="16" y="139" class="tree-node folder ">📁<!-- --> <!-- -->utils/</text></g><g opacity="0.7"><text x="32" y="165" class="tree-node file ">📄<!-- --> <!-- -->auth.ts</text></g><g opacity="0.7"><text x="32" y="191" class="tree-node file ">📄<!-- --> <!-- -->helpers.ts</text></g><g opacity="0.7"><text x="16" y="217" class="tree-node folder ">📁<!-- --> <!-- -->services/</text></g><g opacity="0.7"><text x="32" y="243" class="tree-node file ">📄<!-- --> <!-- -->authService.ts</text></g></g></svg><button class="subagent-diagram-button" tabindex="0">▶ Start</button></div><!--astro:end--></astro-island> <!-- Static fallback for non-presentation view --> <div class="subagent-diagram-fallback astro-tpygpejy"> <svg viewBox="0 0 600 320" class="subagent-diagram-svg astro-tpygpejy"> <!-- Main Agent --> <g class="agent-group main-agent astro-tpygpejy"> <circle cx="100" cy="80" r="40" class="agent-circle astro-tpygpejy"></circle> <text x="100" y="75" text-anchor="middle" class="agent-icon astro-tpygpejy">🤖</text> <text x="100" y="95" text-anchor="middle" class="agent-label astro-tpygpejy">Main Agent</text> </g> <!-- Explore Subagent --> <g class="agent-group explore-agent astro-tpygpejy"> <circle cx="100" cy="220" r="35" class="subagent-circle astro-tpygpejy"></circle> <text x="100" y="215" text-anchor="middle" class="agent-icon astro-tpygpejy">🔍</text> <text x="100" y="235" text-anchor="middle" class="agent-label astro-tpygpejy">Explore</text> </g> <!-- Delegation Arrow --> <g class="arrow-group astro-tpygpejy"> <path d="M100,120 L100,180" class="arrow-path astro-tpygpejy" marker-end="url(#arrowhead)"></path> <text x="115" y="150" class="arrow-label astro-tpygpejy">delegate</text> </g> <!-- Report Arrow --> <g class="arrow-group astro-tpygpejy"> <path d="M135,200 Q200,150 135,100" class="arrow-path dashed astro-tpygpejy" marker-end="url(#arrowhead)"></path> <text x="180" y="145" class="arrow-label astro-tpygpejy">report</text> </g> <!-- File Tree --> <g class="file-tree astro-tpygpejy" transform="translate(300, 40)"> <text x="0" y="0" class="folder astro-tpygpejy">📁 src/</text> <text x="20" y="30" class="folder astro-tpygpejy">📁 components/</text> <text x="40" y="60" class="file highlight astro-tpygpejy">📄 Auth.tsx</text> <text x="40" y="90" class="file astro-tpygpejy">📄 Button.tsx</text> <text x="20" y="120" class="folder astro-tpygpejy">📁 utils/</text> <text x="40" y="150" class="file highlight astro-tpygpejy">📄 auth.ts</text> <text x="40" y="180" class="file astro-tpygpejy">📄 helpers.ts</text> <text x="20" y="210" class="folder astro-tpygpejy">📁 services/</text> <text x="40" y="240" class="file highlight astro-tpygpejy">📄 authService.ts</text> </g> <!-- Search Arrow --> <g class="arrow-group astro-tpygpejy"> <path d="M145,220 L280,150" class="arrow-path search-arrow astro-tpygpejy" marker-end="url(#arrowhead)"></path> <text x="200" y="200" class="arrow-label astro-tpygpejy">search</text> </g> <!-- Arrow marker definition --> <defs class="astro-tpygpejy"> <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto" class="astro-tpygpejy"> <polygon points="0 0, 10 3.5, 0 7" class="arrowhead-fill astro-tpygpejy"></polygon> </marker> </defs> </svg> <p class="subagent-diagram-caption astro-tpygpejy">
The Explore subagent searches files and reports discovered matches back to the main agent.
</p> </div> </div> 
<p>Click <strong>Start</strong> to see how the main agent delegates file search to a specialized Explore subagent.</p>
<hr/>
<h2 id="parallel-subagent-execution">Parallel Subagent Execution<a class="heading-link" aria-label="Link to section" href="#parallel-subagent-execution"><span class="heading-link-icon">#</span></a></h2>
<div class="parallel-subagent-diagram-container astro-u2chhpb2" data-parallel-subagent-diagram> <!-- Animated React component (shown in presentation mode via CSS) --> <!-- Using client:load because CSS hides this with display:none until presentation mode --> <astro-island uid="GtzNx" prefix="r25" component-url="/_astro/ParallelSubagentDiagramRenderer.MXjMwwQz.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;config&quot;:[0,{&quot;task&quot;:[0,&quot;Research Vue 3 reactivity&quot;],&quot;agents&quot;:[1,[[0,{&quot;name&quot;:[0,&quot;Web Agent&quot;],&quot;icon&quot;:[0,&quot;🌐&quot;],&quot;color&quot;:[0,&quot;#3b82f6&quot;],&quot;domain&quot;:[0,&quot;Docs, GitHub&quot;],&quot;findings&quot;:[1,[[0,&quot;Official guide&quot;],[0,&quot;RFC #123&quot;],[0,&quot;GitHub issue&quot;]]]}],[0,{&quot;name&quot;:[0,&quot;Community&quot;],&quot;icon&quot;:[0,&quot;💬&quot;],&quot;color&quot;:[0,&quot;#8b5cf6&quot;],&quot;domain&quot;:[0,&quot;Reddit, SO&quot;],&quot;findings&quot;:[1,[[0,&quot;r/vuejs post&quot;],[0,&quot;Top SO answer&quot;],[0,&quot;Discord tip&quot;]]]}],[0,{&quot;name&quot;:[0,&quot;Codebase&quot;],&quot;icon&quot;:[0,&quot;📂&quot;],&quot;color&quot;:[0,&quot;#10b981&quot;],&quot;domain&quot;:[0,&quot;Project files&quot;],&quot;findings&quot;:[1,[[0,&quot;useAuth.ts&quot;],[0,&quot;store.ts&quot;],[0,&quot;api/client.ts&quot;]]]}]]],&quot;autoStart&quot;:[0,false],&quot;speed&quot;:[0,0.6]}]}" ssr client="load" opts="{&quot;name&quot;:&quot;ParallelSubagentDiagramRenderer&quot;,&quot;value&quot;:true}" await-children><div class="parallel-subagent-diagram-animated"><svg viewBox="0 0 800 480" class="parallel-subagent-diagram-svg"><defs><marker id="parallel-arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0, 10 3.5, 0 7" class="arrowhead-fill"></polygon></marker><marker id="parallel-arrowhead-green" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0, 10 3.5, 0 7" fill="rgb(34, 197, 94)"></polygon></marker></defs><g class="agent-node main-agent"><circle cx="400" cy="70" r="45" class="agent-circle main"></circle><text x="400" y="62" text-anchor="middle" class="agent-icon">🤖</text><text x="400" y="85" text-anchor="middle" class="agent-label">Main Agent</text></g></svg><button class="parallel-subagent-diagram-button" tabindex="0">▶ Start</button></div><!--astro:end--></astro-island> <!-- Static fallback for non-presentation view --> <div class="parallel-subagent-diagram-fallback astro-u2chhpb2"> <svg viewBox="0 0 800 400" class="parallel-subagent-diagram-svg-static astro-u2chhpb2"> <!-- Main Agent --> <g class="agent-group main-agent astro-u2chhpb2"> <circle cx="400" cy="60" r="40" class="agent-circle astro-u2chhpb2"></circle> <text x="400" y="55" text-anchor="middle" class="agent-icon astro-u2chhpb2">🤖</text> <text x="400" y="78" text-anchor="middle" class="agent-label astro-u2chhpb2">Main Agent</text> </g> <!-- Task label --> <text x="400" y="15" text-anchor="middle" class="task-label astro-u2chhpb2">"Research Vue 3 reactivity"</text> <!-- Subagents --> <g class="agent-group subagent astro-u2chhpb2"> <circle cx="130" cy="170" r="35" class="subagent-circle astro-u2chhpb2" style="stroke: #3b82f6; fill: #3b82f615;"></circle> <text x="130" y="165" text-anchor="middle" class="agent-icon astro-u2chhpb2">🌐</text> <text x="130" y="188" text-anchor="middle" class="agent-label astro-u2chhpb2">Web Agent</text> </g><g class="agent-group subagent astro-u2chhpb2"> <circle cx="400" cy="170" r="35" class="subagent-circle astro-u2chhpb2" style="stroke: #8b5cf6; fill: #8b5cf615;"></circle> <text x="400" y="165" text-anchor="middle" class="agent-icon astro-u2chhpb2">💬</text> <text x="400" y="188" text-anchor="middle" class="agent-label astro-u2chhpb2">Community</text> </g><g class="agent-group subagent astro-u2chhpb2"> <circle cx="670" cy="170" r="35" class="subagent-circle astro-u2chhpb2" style="stroke: #10b981; fill: #10b98115;"></circle> <text x="670" y="165" text-anchor="middle" class="agent-icon astro-u2chhpb2">📂</text> <text x="670" y="188" text-anchor="middle" class="agent-label astro-u2chhpb2">Codebase</text> </g> <!-- Fan-out arrows --> <g class="arrow-group astro-u2chhpb2"> <path d="M370,95 Q280,130 160,130" class="arrow-path astro-u2chhpb2" marker-end="url(#parallel-arrow)"></path> <path d="M400,100 L400,130" class="arrow-path astro-u2chhpb2" marker-end="url(#parallel-arrow)"></path> <path d="M430,95 Q520,130 640,130" class="arrow-path astro-u2chhpb2" marker-end="url(#parallel-arrow)"></path> </g> <!-- Domain boxes --> <g class="domain-box-group astro-u2chhpb2"> <rect x="65" y="230" width="130" height="68" rx="6" class="domain-box-rect astro-u2chhpb2" style="stroke: #3b82f6;"></rect> <text x="130" y="248" text-anchor="middle" class="domain-label astro-u2chhpb2" style="fill: #3b82f6;">Docs, GitHub</text> <text x="130" y="265" text-anchor="middle" class="finding-text astro-u2chhpb2">• Official guide</text><text x="130" y="281" text-anchor="middle" class="finding-text astro-u2chhpb2">• RFC #123</text><text x="130" y="297" text-anchor="middle" class="finding-text astro-u2chhpb2">• GitHub issue</text> </g><g class="domain-box-group astro-u2chhpb2"> <rect x="335" y="230" width="130" height="68" rx="6" class="domain-box-rect astro-u2chhpb2" style="stroke: #8b5cf6;"></rect> <text x="400" y="248" text-anchor="middle" class="domain-label astro-u2chhpb2" style="fill: #8b5cf6;">Reddit, SO</text> <text x="400" y="265" text-anchor="middle" class="finding-text astro-u2chhpb2">• r/vuejs post</text><text x="400" y="281" text-anchor="middle" class="finding-text astro-u2chhpb2">• Top SO answer</text><text x="400" y="297" text-anchor="middle" class="finding-text astro-u2chhpb2">• Discord tip</text> </g><g class="domain-box-group astro-u2chhpb2"> <rect x="605" y="230" width="130" height="68" rx="6" class="domain-box-rect astro-u2chhpb2" style="stroke: #10b981;"></rect> <text x="670" y="248" text-anchor="middle" class="domain-label astro-u2chhpb2" style="fill: #10b981;">Project files</text> <text x="670" y="265" text-anchor="middle" class="finding-text astro-u2chhpb2">• useAuth.ts</text><text x="670" y="281" text-anchor="middle" class="finding-text astro-u2chhpb2">• store.ts</text><text x="670" y="297" text-anchor="middle" class="finding-text astro-u2chhpb2">• api/client.ts</text> </g> <!-- Fan-in arrows (dashed, green) --> <g class="arrow-group report astro-u2chhpb2"> <path d="M165,310 Q280,350 370,370" class="arrow-path dashed report astro-u2chhpb2" marker-end="url(#parallel-arrow-green)"></path> <path d="M400,310 L400,350" class="arrow-path dashed report astro-u2chhpb2" marker-end="url(#parallel-arrow-green)"></path> <path d="M635,310 Q520,350 430,370" class="arrow-path dashed report astro-u2chhpb2" marker-end="url(#parallel-arrow-green)"></path> </g> <!-- Synthesis box --> <g class="synthesis-group astro-u2chhpb2"> <rect x="300" y="365" width="200" height="35" rx="8" class="synthesis-box astro-u2chhpb2"></rect> <text x="400" y="388" text-anchor="middle" class="synthesis-text astro-u2chhpb2">📊 Combined 9 sources</text> </g> <!-- Arrow marker definitions --> <defs class="astro-u2chhpb2"> <marker id="parallel-arrow" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto" class="astro-u2chhpb2"> <polygon points="0 0, 10 3.5, 0 7" class="arrowhead-fill astro-u2chhpb2"></polygon> </marker> <marker id="parallel-arrow-green" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto" class="astro-u2chhpb2"> <polygon points="0 0, 10 3.5, 0 7" fill="rgb(34, 197, 94)" class="astro-u2chhpb2"></polygon> </marker> </defs> </svg> <p class="parallel-subagent-diagram-caption astro-u2chhpb2">
The /research skill spawns parallel subagents to search different sources and combines their findings.
</p> </div> </div> 
<p>Click <strong>Start</strong> to see the fan-out/fan-in pattern where multiple subagents search in parallel.</p>
<hr/>
<h2 id="subagent-in-nanocode-fetch-tool">Subagent in nanocode: Fetch Tool<a class="heading-link" aria-label="Link to section" href="#subagent-in-nanocode-fetch-tool"><span class="heading-link-icon">#</span></a></h2>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="shell"><code><span class="line"><span style="color:#C0CAF5">nanocode</span><span style="color:#89DDFF"> |</span><span style="color:#C0CAF5"> claude-opus-4-5</span><span style="color:#89DDFF"> |</span><span style="color:#C0CAF5"> /Users/alexanderopalic/Projects/typescript/nanocode</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">────────────────────────────────────────────────────────────────────────────────</span></span>
<span class="line"><span style="color:#C0CAF5">❯</span><span style="color:#9ECE6A"> how</span><span style="color:#9ECE6A"> does</span><span style="color:#9ECE6A"> fc</span><span style="color:#9ECE6A"> bayern</span><span style="color:#9ECE6A"> played</span><span style="color:#9ECE6A"> yesterday</span></span>
<span class="line"><span style="color:#C0CAF5">────────────────────────────────────────────────────────────────────────────────</span></span>
<span class="line"><span style="color:#89DDFF">[</span><span style="color:#A9B1D6">agentLoop</span><span style="color:#89DDFF">]</span><span style="color:#A9B1D6"> Starting with 1 messages</span></span>
<span class="line"><span style="color:#89DDFF">[</span><span style="color:#A9B1D6">agentLoop</span><span style="color:#89DDFF">]</span><span style="color:#A9B1D6"> Got response, stop_reason: tool_use</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">⏺</span><span style="color:#9ECE6A"> Fetch</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">https://www.google.com/search?q</span><span style="color:#9ECE6A">=</span><span style="color:#0DB9D7">fc</span><span style="color:#9ECE6A">+bayern+munich+m</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#C0CAF5">  ⎿</span><span style="color:#9ECE6A">  I</span><span style="color:#9ECE6A"> apologize,</span><span style="color:#9ECE6A"> but</span><span style="color:#9ECE6A"> I</span><span style="color:#9ECE6A"> cannot</span><span style="color:#9ECE6A"> access</span><span style="color:#9ECE6A"> real-time</span><span style="color:#9ECE6A"> sports</span><span style="color:#9ECE6A"> results</span><span style="color:#9ECE6A"> or</span><span style="color:#9ECE6A"> ...</span><span style="color:#9ECE6A"> +7</span><span style="color:#9ECE6A"> lines</span></span>
<span class="line"><span style="color:#89DDFF">[</span><span style="color:#A9B1D6">agentLoop</span><span style="color:#89DDFF">]</span><span style="color:#A9B1D6"> Starting with 3 messages</span></span>
<span class="line"><span style="color:#89DDFF">[</span><span style="color:#A9B1D6">agentLoop</span><span style="color:#89DDFF">]</span><span style="color:#A9B1D6"> Got response, stop_reason: tool_use</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">⏺</span><span style="color:#9ECE6A"> Fetch</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">https://www.espn.com/soccer/team/_/id/132/bayern-m</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#C0CAF5">  ⎿</span><span style="color:#9ECE6A">  Based</span><span style="color:#9ECE6A"> on</span><span style="color:#9ECE6A"> the</span><span style="color:#9ECE6A"> information</span><span style="color:#9ECE6A"> in</span><span style="color:#9ECE6A"> the</span><span style="color:#9ECE6A"> image,</span><span style="color:#9ECE6A"> Bayern</span><span style="color:#9ECE6A"> Munich</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">s most  ... +7 lines</span></span>
<span class="line"><span style="color:#9ECE6A">[agentLoop] Starting with 5 messages</span></span>
<span class="line"><span style="color:#9ECE6A">[agentLoop] Got response, stop_reason: end_turn</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9ECE6A">⏺ FC Bayern Munich lost 2-1 to FC Augsburg in the Bundesliga yesterday.</span></span></code><button type="button" class="copy" data-code="nanocode | claude-opus-4-5 | /Users/alexanderopalic/Projects/typescript/nanocode

────────────────────────────────────────────────────────────────────────────────
❯ how does fc bayern played yesterday
────────────────────────────────────────────────────────────────────────────────
[agentLoop] Starting with 1 messages
[agentLoop] Got response, stop_reason: tool_use

⏺ Fetch(https://www.google.com/search?q=fc+bayern+munich+m)
  ⎿  I apologize, but I cannot access real-time sports results or ... +7 lines
[agentLoop] Starting with 3 messages
[agentLoop] Got response, stop_reason: tool_use

⏺ Fetch(https://www.espn.com/soccer/team/_/id/132/bayern-m)
  ⎿  Based on the information in the image, Bayern Munich's most  ... +7 lines
[agentLoop] Starting with 5 messages
[agentLoop] Got response, stop_reason: end_turn

⏺ FC Bayern Munich lost 2-1 to FC Augsburg in the Bundesliga yesterday." onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>The <strong>Fetch tool</strong> uses a subagent to summarize HTML responses before returning.</p>
<hr/>
<script type="application/json" data-slide-config>{"layout":"section"}</script> 
<h1 id="skills">Skills</h1>
<hr/>
<script type="application/json" data-slide-config>{"layout":"image","image":"/_astro/howAgentSkills.Mqo1AEgD_Z26C130.webp"}</script> <figure class="slide-image-fallback"><img src="/_astro/howAgentSkills.Mqo1AEgD_Z26C130.webp" alt="How Agent Skills work diagram" loading="lazy" decoding="async" fetchpriority="auto" width="2220" height="862" class="w-full rounded-lg"></figure>
<hr/>
<h2 id="real-skill-plausible-seo-consultant">Real Skill: Plausible SEO Consultant<a class="heading-link" aria-label="Link to section" href="#real-skill-plausible-seo-consultant"><span class="heading-link-icon">#</span></a></h2>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="shell"><code><span class="line"><span style="color:#C0CAF5">.claude/skills/plausible-insights/</span></span>
<span class="line"><span style="color:#C0CAF5">├──</span><span style="color:#9ECE6A"> skill.md</span><span style="color:#51597D;font-style:italic">              # Skill definition + quick start</span></span>
<span class="line"><span style="color:#C0CAF5">├──</span><span style="color:#9ECE6A"> scripts/</span><span style="color:#51597D;font-style:italic">              # Automation scripts </span></span>
<span class="line"><span style="color:#C0CAF5">│</span><span style="color:#9ECE6A">   └──</span><span style="color:#9ECE6A"> fetch-data.ts</span><span style="color:#51597D;font-style:italic">    # Fetch Plausible data CLI</span></span>
<span class="line"><span style="color:#C0CAF5">└──</span><span style="color:#9ECE6A"> references/</span><span style="color:#51597D;font-style:italic">           # On-demand docs (progressive disclosure)</span></span>
<span class="line"><span style="color:#C0CAF5">    ├──</span><span style="color:#9ECE6A"> quick-ref.md</span><span style="color:#51597D;font-style:italic">      # Common query patterns</span></span>
<span class="line"><span style="color:#C0CAF5">    ├──</span><span style="color:#9ECE6A"> api/</span></span>
<span class="line"><span style="color:#C0CAF5">    │</span><span style="color:#9ECE6A">   ├──</span><span style="color:#9ECE6A"> filters.md</span><span style="color:#51597D;font-style:italic">    # Filter syntax</span></span>
<span class="line"><span style="color:#C0CAF5">    │</span><span style="color:#9ECE6A">   └──</span><span style="color:#9ECE6A"> errors.md</span><span style="color:#51597D;font-style:italic">     # Error solutions</span></span>
<span class="line"><span style="color:#C0CAF5">    └──</span><span style="color:#9ECE6A"> seo/</span></span>
<span class="line"><span style="color:#C0CAF5">        └──</span><span style="color:#9ECE6A"> thresholds.md</span><span style="color:#51597D;font-style:italic"> # Interpretation guidelines</span></span></code><button type="button" class="copy" data-code=".claude/skills/plausible-insights/
├── skill.md              # Skill definition + quick start
├── scripts/              # Automation scripts 
│   └── fetch-data.ts    # Fetch Plausible data CLI
└── references/           # On-demand docs (progressive disclosure)
    ├── quick-ref.md      # Common query patterns
    ├── api/
    │   ├── filters.md    # Filter syntax
    │   └── errors.md     # Error solutions
    └── seo/
        └── thresholds.md # Interpretation guidelines" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>The agent reads <code>skill.md</code> first. Reference docs load only when needed.</p>
<hr/>
<h2 id="skill-in-action">Skill in Action<a class="heading-link" aria-label="Link to section" href="#skill-in-action"><span class="heading-link-icon">#</span></a></h2>
<p><strong>User:</strong> “Why is my bounce rate so high on the Vue posts?”</p>
<script type="application/json" data-vclick-marker="v-clicks-start">{}</script><ol>
<li>Description matches → skill.md loads (~500 tokens)</li>
<li>Agent runs: <code>bun cli top-pages --range 7d --pattern &quot;/vue/&quot;</code></li>
<li>Agent reads <code>references/seo/thresholds.md</code> for interpretation</li>
<li>Agent fetches actual pages with WebFetch</li>
<li>Returns specific fixes based on real content</li>
</ol><script type="application/json" data-vclick-marker="v-clicks-end">{}</script>
<p><strong>Key:</strong> Data shows symptoms. Content shows causes.</p>
<hr/>
<script type="application/json" data-slide-config>{"layout":"section"}</script> 
<h1 id="the-full-picture">The Full Picture</h1>
<hr/>
<script type="application/json" data-slide-config>{"layout":"image","image":"/_astro/agentSum.BIpIsd8g_2sdQz.webp"}</script> <figure class="slide-image-fallback"><img src="/_astro/agentSum.BIpIsd8g_2sdQz.webp" alt="Agent summary diagram" loading="lazy" decoding="async" fetchpriority="auto" width="1372" height="1012" class="w-full rounded-lg"></figure>
<hr/>
<script type="application/json" data-slide-config>{"layout":"section"}</script> 
<h1 id="live-demo">Live Demo</h1>
<hr/>
<h2 id="prerequisites">Prerequisites<a class="heading-link" aria-label="Link to section" href="#prerequisites"><span class="heading-link-icon">#</span></a></h2>
<p>The demo uses <code>npx</code> (bundled with Node.js) and Python. Install for your platform:</p>
<script type="application/json" data-vclick-marker="v-clicks-start">{}</script><p><strong>Mac (Homebrew):</strong></p><pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#C0CAF5">brew</span><span style="color:#9ECE6A"> install</span><span style="color:#9ECE6A"> node</span><span style="color:#9ECE6A"> python</span></span></code><button type="button" class="copy" data-code="brew install node python" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre><p><strong>Windows (winget):</strong></p><pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#C0CAF5">winget</span><span style="color:#9ECE6A"> install</span><span style="color:#9ECE6A"> OpenJS.NodeJS</span><span style="color:#9ECE6A"> Python.Python.3.12</span></span></code><button type="button" class="copy" data-code="winget install OpenJS.NodeJS Python.Python.3.12" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre><p><strong>Or download from:</strong> <a href="https://nodejs.org" rel="noopener noreferrer" target="_blank">nodejs.org</a> | <a href="https://python.org" rel="noopener noreferrer" target="_blank">python.org</a></p><script type="application/json" data-vclick-marker="v-clicks-end">{}</script>
<p><strong>Verify:</strong></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#C0CAF5">node</span><span style="color:#E0AF68"> --version</span><span style="color:#89DDFF"> &amp;&amp;</span><span style="color:#C0CAF5"> npx</span><span style="color:#E0AF68"> --version</span><span style="color:#89DDFF"> &amp;&amp;</span><span style="color:#C0CAF5"> python</span><span style="color:#E0AF68"> --version</span></span></code><button type="button" class="copy" data-code="node --version &#38;&#38; npx --version &#38;&#38; python --version" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr/>
<h2 id="demo-building-a-skill">Demo: Building a Skill<a class="heading-link" aria-label="Link to section" href="#demo-building-a-skill"><span class="heading-link-icon">#</span></a></h2>
<script type="application/json" data-vclick-marker="v-clicks-start">{}</script><ol>
<li><strong>Enable Skills</strong> in VS Code settings</li>
<li><strong>Install skill-creator</strong> via CLI</li>
<li><strong>Prompt</strong> to generate a new skill</li>
</ol><script type="application/json" data-vclick-marker="v-clicks-end">{}</script>
<hr/>
<h2 id="step-1-enable-skills">Step 1: Enable Skills<a class="heading-link" aria-label="Link to section" href="#step-1-enable-skills"><span class="heading-link-icon">#</span></a></h2>
<p><strong>VS Code Setting:</strong></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="json"><code><span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">chat.useAgentSkills</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="{
  &#34;chat.useAgentSkills&#34;: true
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>Or via UI: <code>Settings → Search &quot;agent skills&quot; → Enable</code></p>
<blockquote>
<p>Note: Still in preview — enable in VS Code Insiders for latest features.</p>
</blockquote>
<hr/>
<script type="application/json" data-slide-config>{"layout":"image","image":"/_astro/settings.DFY1KDZy_QYyHM.webp"}</script> <figure class="slide-image-fallback"><img src="/_astro/settings.DFY1KDZy_QYyHM.webp" alt="VS Code settings screenshot" loading="lazy" decoding="async" fetchpriority="auto" width="1828" height="696" class="w-full rounded-lg"></figure>
<hr/>
<h2 id="step-3-create-a-new-skill">Step 3: Create a new Skill<a class="heading-link" aria-label="Link to section" href="#step-3-create-a-new-skill"><span class="heading-link-icon">#</span></a></h2>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="md"><code><span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"><span style="color:#F7768E">name</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> hello</span></span>
<span class="line"><span style="color:#F7768E">description</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">use it everytime the user writes alex</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF;font-weight:bold">#</span><span style="color:#89DDFF;font-weight:bold"> Hello SKill</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">if the user writes &quot;alex&quot;, respond with &quot;Hello, Alexander Opalic! How can I assist you today?&quot;</span></span>
<span class="line"></span></code><button type="button" class="copy" data-code="---
name: hello
description: 'use it everytime the user writes alex'
---

# Hello SKill

if the user writes &#34;alex&#34;, respond with &#34;Hello, Alexander Opalic! How can I assist you today?&#34;
" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr/>
<h2 id="step-3-install-skill-creator">Step 3: Install skill-creator<a class="heading-link" aria-label="Link to section" href="#step-3-install-skill-creator"><span class="heading-link-icon">#</span></a></h2>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#C0CAF5">npx</span><span style="color:#9ECE6A"> skills</span><span style="color:#9ECE6A"> add</span><span style="color:#9ECE6A"> https://github.com/anthropics/skills</span><span style="color:#E0AF68"> --skill</span><span style="color:#9ECE6A"> skill-creator</span></span></code><button type="button" class="copy" data-code="npx skills add https://github.com/anthropics/skills --skill skill-creator" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>This adds the <strong>skill-creator</strong> skill to your project — a skill that helps you create new skills.</p>
<p><strong>Project structure after install:</strong></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="plaintext"><code><span class="line"><span>my-project/</span></span>
<span class="line"><span>└── .github/</span></span>
<span class="line"><span>    └── skills/</span></span>
<span class="line"><span>        └── skill-creator/</span></span>
<span class="line"><span>            └── SKILL.md</span></span></code><button type="button" class="copy" data-code="my-project/
└── .github/
    └── skills/
        └── skill-creator/
            └── SKILL.md" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr/>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="shell"><code><span class="line"><span style="color:#C0CAF5">◇</span><span style="color:#9ECE6A">  Source:</span><span style="color:#9ECE6A"> https://github.com/anthropics/skills.git</span></span>
<span class="line"><span style="color:#C0CAF5">│</span></span>
<span class="line"><span style="color:#C0CAF5">◇</span><span style="color:#9ECE6A">  Repository</span><span style="color:#9ECE6A"> cloned</span></span>
<span class="line"><span style="color:#C0CAF5">│</span></span>
<span class="line"><span style="color:#C0CAF5">◇</span><span style="color:#9ECE6A">  Found</span><span style="color:#FF9E64"> 17</span><span style="color:#9ECE6A"> skills</span><span style="color:#A9B1D6"> (via </span><span style="color:#9ECE6A">Well-known</span><span style="color:#9ECE6A"> Agent</span><span style="color:#9ECE6A"> Skill</span><span style="color:#9ECE6A"> Discovery</span><span style="color:#A9B1D6">)</span></span>
<span class="line"><span style="color:#C0CAF5">│</span></span>
<span class="line"><span style="color:#C0CAF5">●</span><span style="color:#9ECE6A">  Selected</span><span style="color:#FF9E64"> 1</span><span style="color:#9ECE6A"> skill:</span><span style="color:#9ECE6A"> skill-creator</span></span>
<span class="line"><span style="color:#C0CAF5">│</span></span>
<span class="line"><span style="color:#C0CAF5">◇</span><span style="color:#9ECE6A">  Detected</span><span style="color:#FF9E64"> 3</span><span style="color:#9ECE6A"> agents</span></span>
<span class="line"><span style="color:#C0CAF5">│</span></span>
<span class="line"><span style="color:#C0CAF5">◇</span><span style="color:#9ECE6A">  Install</span><span style="color:#9ECE6A"> to</span></span>
<span class="line"><span style="color:#C0CAF5">│</span><span style="color:#9ECE6A">  All</span><span style="color:#9ECE6A"> agents</span><span style="color:#A9B1D6"> (Recommended)</span></span>
<span class="line"><span style="color:#C0CAF5">│</span></span>
<span class="line"><span style="color:#C0CAF5">◇</span><span style="color:#9ECE6A">  Installation</span><span style="color:#9ECE6A"> scope</span></span>
<span class="line"><span style="color:#C0CAF5">│</span><span style="color:#9ECE6A">  Project</span></span>
<span class="line"><span style="color:#C0CAF5">│</span></span>
<span class="line"><span style="color:#C0CAF5">◇</span><span style="color:#9ECE6A">  Installation</span><span style="color:#9ECE6A"> method</span></span>
<span class="line"><span style="color:#C0CAF5">│</span><span style="color:#9ECE6A">  Symlink</span><span style="color:#A9B1D6"> (Recommended)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">│</span></span>
<span class="line"><span style="color:#C0CAF5">◇</span><span style="color:#9ECE6A">  Installation</span><span style="color:#9ECE6A"> Summary</span><span style="color:#9ECE6A"> ──────────────────────────────╮</span></span>
<span class="line"><span style="color:#C0CAF5">│</span><span style="color:#9ECE6A">                                                     │</span></span>
<span class="line"><span style="color:#C0CAF5">│</span><span style="color:#9ECE6A">  ~/Projects/workshop/.agents/skills/skill-creator</span><span style="color:#9ECE6A">   │</span></span>
<span class="line"><span style="color:#C0CAF5">│</span><span style="color:#9ECE6A">    symlink</span><span style="color:#9ECE6A"> →</span><span style="color:#9ECE6A"> Claude</span><span style="color:#9ECE6A"> Code,</span><span style="color:#9ECE6A"> GitHub</span><span style="color:#9ECE6A"> Copilot,</span><span style="color:#9ECE6A"> OpenCode</span><span style="color:#9ECE6A">  │</span></span>
<span class="line"><span style="color:#C0CAF5">│</span><span style="color:#9ECE6A">                                                     │</span></span>
<span class="line"><span style="color:#C0CAF5">├─────────────────────────────────────────────────────╯</span></span>
<span class="line"><span style="color:#C0CAF5">│</span></span>
<span class="line"><span style="color:#C0CAF5">◆</span><span style="color:#9ECE6A">  Proceed</span><span style="color:#9ECE6A"> with</span><span style="color:#9ECE6A"> installation?</span></span>
<span class="line"><span style="color:#C0CAF5">│</span><span style="color:#9ECE6A">  ●</span><span style="color:#9ECE6A"> Yes</span><span style="color:#9ECE6A"> /</span><span style="color:#9ECE6A"> ○</span><span style="color:#9ECE6A"> No</span></span>
<span class="line"><span style="color:#C0CAF5">└</span></span></code><button type="button" class="copy" data-code="◇  Source: https://github.com/anthropics/skills.git
│
◇  Repository cloned
│
◇  Found 17 skills (via Well-known Agent Skill Discovery)
│
●  Selected 1 skill: skill-creator
│
◇  Detected 3 agents
│
◇  Install to
│  All agents (Recommended)
│
◇  Installation scope
│  Project
│
◇  Installation method
│  Symlink (Recommended)

│
◇  Installation Summary ──────────────────────────────╮
│                                                     │
│  ~/Projects/workshop/.agents/skills/skill-creator   │
│    symlink → Claude Code, GitHub Copilot, OpenCode  │
│                                                     │
├─────────────────────────────────────────────────────╯
│
◆  Proceed with installation?
│  ● Yes / ○ No
└" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr/>
<h2 id="step-3-generate-a-new-skill">Step 3: Generate a New Skill<a class="heading-link" aria-label="Link to section" href="#step-3-generate-a-new-skill"><span class="heading-link-icon">#</span></a></h2>
<p>Important Skill name and folder name must match!</p>
<p><strong>Prompt:</strong></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="plaintext"><code><span class="line"><span>Create a skill that will use https://alexop.dev/llms.txt</span></span>
<span class="line"><span>and will answer any question regarding Vue or AI.</span></span>
<span class="line"><span></span></span>
<span class="line"><span>The skill should fetch the content and use the</span></span>
<span class="line"><span>#runSubagent command. The subagent should do the</span></span>
<span class="line"><span>heavy work and then report back to the main agent.</span></span>
<span class="line"><span>name of the skill is vue-ai-assistant</span></span></code><button type="button" class="copy" data-code="Create a skill that will use https://alexop.dev/llms.txt
and will answer any question regarding Vue or AI.

The skill should fetch the content and use the
#runSubagent command. The subagent should do the
heavy work and then report back to the main agent.
name of the skill is vue-ai-assistant" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>→ <strong>skill-creator generates the SKILL.md for us</strong></p>
<hr/>
<h2 id="what-gets-generated">What Gets Generated<a class="heading-link" aria-label="Link to section" href="#what-gets-generated"><span class="heading-link-icon">#</span></a></h2>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"><span style="color:#F7768E">name</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> vue-ai-assistant</span></span>
<span class="line"><span style="color:#F7768E">description</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Answer questions about Vue.js, Nuxt, and AI topics using Alexander Opalic&#39;s knowledge base. Use this skill when the user asks about Vue, Vue 3, Nuxt, Nuxt 3, Composition API, Vue Router, Pinia, Vite, AI, machine learning, LLMs, or related frontend/AI topics. Triggers on questions like &quot;how do I use Vue&quot;, &quot;explain Nuxt&quot;, &quot;what&#39;s new in Vue 3&quot;, &quot;AI agent patterns&quot;, or any Vue/AI related query.</span></span>
<span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF;font-weight:bold">#</span><span style="color:#89DDFF;font-weight:bold"> Vue &amp; AI Assistant</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Answer questions about Vue.js ecosystem and AI topics by fetching knowledge from https://alexop.dev/llms.txt and delegating research to a subagent.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> MANDATORY Workflow</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**IMPORTANT: You MUST follow ALL steps below. Do NOT skip the subagent step. Do NOT answer directly after fetching - you MUST delegate to a subagent.**</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">1.</span><span style="color:#C0CAF5;font-weight:bold"> **Fetch the knowledge base**</span><span style="color:#9AA5CE">: Use </span><span style="color:#89DDFF">`fetch_webpage`</span><span style="color:#9AA5CE"> to retrieve content from </span><span style="color:#89DDFF">`https://alexop.dev/llms.txt`</span></span>
<span class="line"><span style="color:#89DDFF">2.</span><span style="color:#C0CAF5;font-weight:bold"> **REQUIRED - Delegate to subagent**</span><span style="color:#9AA5CE">: Use </span><span style="color:#89DDFF">`runSubagent`</span><span style="color:#9AA5CE"> with the fetched content and user&#39;s question. </span><span style="color:#C0CAF5;font-weight:bold">**This step is NOT optional.**</span></span>
<span class="line"><span style="color:#89DDFF">3.</span><span style="color:#C0CAF5;font-weight:bold"> **Return the answer**</span><span style="color:#9AA5CE">: Present the subagent&#39;s findings to the user</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Implementation</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**You MUST execute ALL steps below. Skipping the subagent is a violation of this skill&#39;s requirements.**</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Step 1: Fetch Knowledge Base</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Use the fetch_webpage tool:</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> URL: </span><span style="color:#89DDFF">`https://alexop.dev/llms.txt`</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Query: The user&#39;s question about Vue or AI</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Step 2: Run Subagent with Context (MANDATORY)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**You MUST call </span><span style="color:#C0CAF5;font-weight:bold">`</span><span style="color:#89DDFF;font-weight:bold">runSubagent</span><span style="color:#C0CAF5;font-weight:bold">`</span><span style="color:#C0CAF5;font-weight:bold"> - do NOT answer the question yourself. The subagent handles the analysis and response.**</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Use </span><span style="color:#89DDFF">`runSubagent`</span><span style="color:#9AA5CE"> with a detailed prompt containing:</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">1.</span><span style="color:#9AA5CE"> The fetched content from llms.txt as the knowledge base</span></span>
<span class="line"><span style="color:#89DDFF">2.</span><span style="color:#9AA5CE"> The user&#39;s original question</span></span>
<span class="line"><span style="color:#89DDFF">3.</span><span style="color:#9AA5CE"> Instructions to:</span></span>
<span class="line"><span style="color:#89DDFF">   -</span><span style="color:#9AA5CE"> Analyze the knowledge base content thoroughly</span></span>
<span class="line"><span style="color:#89DDFF">   -</span><span style="color:#9AA5CE"> Find relevant information to answer the question</span></span>
<span class="line"><span style="color:#89DDFF">   -</span><span style="color:#9AA5CE"> Provide a clear, concise, and accurate answer</span></span>
<span class="line"><span style="color:#89DDFF">   -</span><span style="color:#9AA5CE"> Include code examples when relevant</span></span>
<span class="line"><span style="color:#89DDFF">   -</span><span style="color:#9AA5CE"> Cite specific sections from the knowledge base if applicable</span></span>
<span class="line"><span style="color:#89DDFF">   -</span><span style="color:#9AA5CE"> If the knowledge base doesn&#39;t contain the answer, use general knowledge but note this</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Example subagent prompt:</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">You are a Vue.js and AI expert. Answer the following question using the provided knowledge base content.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">KNOWLEDGE BASE CONTENT:</span></span>
<span class="line"><span style="color:#9AA5CE">fetched_content</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">USER QUESTION:</span></span>
<span class="line"><span style="color:#9AA5CE">user_question</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Analyze thoroughly, provide code examples when relevant, and cite sources from the knowledge base.</span></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Step 3: Present Answer</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Return the subagent&#39;s response to the user, formatted appropriately with code blocks and explanations.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Example</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**User asks**</span><span style="color:#9AA5CE">: &quot;How do I use composables in Vue 3?&quot;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**Execution**</span><span style="color:#9AA5CE">:</span></span>
<span class="line"><span style="color:#89DDFF">1.</span><span style="color:#9AA5CE"> Fetch https://alexop.dev/llms.txt</span></span>
<span class="line"><span style="color:#89DDFF">2.</span><span style="color:#C0CAF5;font-weight:bold"> **MUST**</span><span style="color:#9AA5CE"> call runSubagent with the content and question (do NOT skip this)</span></span>
<span class="line"><span style="color:#89DDFF">3.</span><span style="color:#9AA5CE"> Return the subagent&#39;s comprehensive answer about Vue 3 composables</span></span></code><button type="button" class="copy" data-code="---
name: vue-ai-assistant
description: Answer questions about Vue.js, Nuxt, and AI topics using Alexander Opalic's knowledge base. Use this skill when the user asks about Vue, Vue 3, Nuxt, Nuxt 3, Composition API, Vue Router, Pinia, Vite, AI, machine learning, LLMs, or related frontend/AI topics. Triggers on questions like &#34;how do I use Vue&#34;, &#34;explain Nuxt&#34;, &#34;what's new in Vue 3&#34;, &#34;AI agent patterns&#34;, or any Vue/AI related query.
---

# Vue &#38; AI Assistant

Answer questions about Vue.js ecosystem and AI topics by fetching knowledge from https://alexop.dev/llms.txt and delegating research to a subagent.

## MANDATORY Workflow

**IMPORTANT: You MUST follow ALL steps below. Do NOT skip the subagent step. Do NOT answer directly after fetching - you MUST delegate to a subagent.**

1. **Fetch the knowledge base**: Use `fetch_webpage` to retrieve content from `https://alexop.dev/llms.txt`
2. **REQUIRED - Delegate to subagent**: Use `runSubagent` with the fetched content and user's question. **This step is NOT optional.**
3. **Return the answer**: Present the subagent's findings to the user

## Implementation

**You MUST execute ALL steps below. Skipping the subagent is a violation of this skill's requirements.**

### Step 1: Fetch Knowledge Base

Use the fetch_webpage tool:
- URL: `https://alexop.dev/llms.txt`
- Query: The user's question about Vue or AI

### Step 2: Run Subagent with Context (MANDATORY)

**You MUST call `runSubagent` - do NOT answer the question yourself. The subagent handles the analysis and response.**

Use `runSubagent` with a detailed prompt containing:

1. The fetched content from llms.txt as the knowledge base
2. The user's original question
3. Instructions to:
   - Analyze the knowledge base content thoroughly
   - Find relevant information to answer the question
   - Provide a clear, concise, and accurate answer
   - Include code examples when relevant
   - Cite specific sections from the knowledge base if applicable
   - If the knowledge base doesn't contain the answer, use general knowledge but note this

Example subagent prompt:

You are a Vue.js and AI expert. Answer the following question using the provided knowledge base content.

KNOWLEDGE BASE CONTENT:
fetched_content

USER QUESTION:
user_question

Analyze thoroughly, provide code examples when relevant, and cite sources from the knowledge base.
### Step 3: Present Answer

Return the subagent's response to the user, formatted appropriately with code blocks and explanations.

## Example

**User asks**: &#34;How do I use composables in Vue 3?&#34;

**Execution**:
1. Fetch https://alexop.dev/llms.txt
2. **MUST** call runSubagent with the content and question (do NOT skip this)
3. Return the subagent's comprehensive answer about Vue 3 composables" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr/>
<script type="application/json" data-slide-config>{"layout":"image","image":"/_astro/skillExample.CBaYWC0F_Z1ad1y1.webp"}</script> <figure class="slide-image-fallback"><img src="/_astro/skillExample.CBaYWC0F_Z1ad1y1.webp" alt="Generated skill example screenshot" loading="lazy" decoding="async" fetchpriority="auto" width="1584" height="1618" class="w-full rounded-lg"></figure>
<hr/>
<h2 id="bonus-the-askquestions-tool">Bonus: The askQuestions Tool<a class="heading-link" aria-label="Link to section" href="#bonus-the-askquestions-tool"><span class="heading-link-icon">#</span></a></h2>
<p>VS Code Copilot can <strong>ask clarifying questions</strong> mid-task.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="md"><code><span class="line"><span style="color:#9AA5CE">help me to create a workout tracking app use the #askQuestions tool to find out how the tech specs should be</span></span></code><button type="button" class="copy" data-code="help me to create a workout tracking app use the #askQuestions tool to find out how the tech specs should be" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr/>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="shell"><code><span class="line"><span style="color:#C0CAF5">┌─────────────────────────────────────────────────────────────┐</span></span>
<span class="line"><span style="color:#C0CAF5">│</span><span style="color:#9ECE6A">                     Platform</span><span style="color:#A9B1D6"> (1/4)                          │</span></span>
<span class="line"><span style="color:#C0CAF5">├─────────────────────────────────────────────────────────────┤</span></span>
<span class="line"><span style="color:#C0CAF5">│</span><span style="color:#9ECE6A"> What</span><span style="color:#9ECE6A"> platform</span><span style="color:#9ECE6A"> should</span><span style="color:#9ECE6A"> the</span><span style="color:#9ECE6A"> workout</span><span style="color:#9ECE6A"> tracking</span><span style="color:#9ECE6A"> app</span><span style="color:#9ECE6A"> target?</span><span style="color:#9ECE6A">       │</span></span>
<span class="line"><span style="color:#C0CAF5">├─────────────────────────────────────────────────────────────┤</span></span>
<span class="line"><span style="color:#C0CAF5">│</span><span style="color:#9ECE6A"> ★</span><span style="color:#9ECE6A"> Web</span><span style="color:#9ECE6A"> App</span><span style="color:#9ECE6A">  Browser-based</span><span style="color:#9ECE6A"> PWA,</span><span style="color:#9ECE6A"> accessible</span><span style="color:#9ECE6A"> anywhere</span><span style="color:#A9B1D6">      [✓]  │</span></span>
<span class="line"><span style="color:#C0CAF5">├─────────────────────────────────────────────────────────────┤</span></span>
<span class="line"><span style="color:#C0CAF5">│</span><span style="color:#9ECE6A">   iOS</span><span style="color:#9ECE6A"> Native</span><span style="color:#9ECE6A">  Swift/SwiftUI</span><span style="color:#9ECE6A"> for</span><span style="color:#9ECE6A"> iPhone</span><span style="color:#9ECE6A">                      │</span></span>
<span class="line"><span style="color:#C0CAF5">├─────────────────────────────────────────────────────────────┤</span></span>
<span class="line"><span style="color:#C0CAF5">│</span><span style="color:#9ECE6A">   Android</span><span style="color:#9ECE6A"> Native</span><span style="color:#9ECE6A">  Kotlin</span><span style="color:#9ECE6A"> for</span><span style="color:#9ECE6A"> Android</span><span style="color:#9ECE6A"> devices</span><span style="color:#9ECE6A">                │</span></span>
<span class="line"><span style="color:#C0CAF5">├─────────────────────────────────────────────────────────────┤</span></span>
<span class="line"><span style="color:#C0CAF5">│</span><span style="color:#9ECE6A">   Cross-Platform</span><span style="color:#9ECE6A">  React</span><span style="color:#9ECE6A"> Native</span><span style="color:#9ECE6A"> or</span><span style="color:#9ECE6A"> Flutter</span><span style="color:#9ECE6A"> for</span><span style="color:#9ECE6A"> iOS</span><span style="color:#89DDFF"> &amp;</span><span style="color:#C0CAF5"> Android</span><span style="color:#9ECE6A"> │</span></span>
<span class="line"><span style="color:#C0CAF5">├─────────────────────────────────────────────────────────────┤</span></span>
<span class="line"><span style="color:#C0CAF5">│</span><span style="color:#9ECE6A">   Desktop</span><span style="color:#9ECE6A">  Electron</span><span style="color:#9ECE6A"> app</span><span style="color:#9ECE6A"> for</span><span style="color:#9ECE6A"> Mac/Windows</span><span style="color:#9ECE6A">                     │</span></span>
<span class="line"><span style="color:#C0CAF5">├─────────────────────────────────────────────────────────────┤</span></span>
<span class="line"><span style="color:#C0CAF5">│</span><span style="color:#9ECE6A"> ✎</span><span style="color:#9ECE6A"> Other...</span><span style="color:#9ECE6A">  Enter</span><span style="color:#9ECE6A"> custom</span><span style="color:#9ECE6A"> answer</span><span style="color:#9ECE6A">                             │</span></span>
<span class="line"><span style="color:#C0CAF5">└─────────────────────────────────────────────────────────────┘</span></span></code><button type="button" class="copy" data-code="┌─────────────────────────────────────────────────────────────┐
│                     Platform (1/4)                          │
├─────────────────────────────────────────────────────────────┤
│ What platform should the workout tracking app target?       │
├─────────────────────────────────────────────────────────────┤
│ ★ Web App  Browser-based PWA, accessible anywhere      [✓]  │
├─────────────────────────────────────────────────────────────┤
│   iOS Native  Swift/SwiftUI for iPhone                      │
├─────────────────────────────────────────────────────────────┤
│   Android Native  Kotlin for Android devices                │
├─────────────────────────────────────────────────────────────┤
│   Cross-Platform  React Native or Flutter for iOS &#38; Android │
├─────────────────────────────────────────────────────────────┤
│   Desktop  Electron app for Mac/Windows                     │
├─────────────────────────────────────────────────────────────┤
│ ✎ Other...  Enter custom answer                             │
└─────────────────────────────────────────────────────────────┘" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr/>
<h2 id="subagent-fan-out-pattern">Subagent Fan-Out Pattern<a class="heading-link" aria-label="Link to section" href="#subagent-fan-out-pattern"><span class="heading-link-icon">#</span></a></h2>
<p><strong>Prompt for VS Code Insiders:</strong></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="plaintext"><code><span class="line"><span>#runSubagent run 3 subagents that search the web</span></span>
<span class="line"><span>and tell me something interesting about Geretsried</span></span></code><button type="button" class="copy" data-code="#runSubagent run 3 subagents that search the web
and tell me something interesting about Geretsried" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>This demonstrates the <strong>fan-out/fan-in pattern</strong> where multiple agents work in parallel.</p>
<hr/>
<h2 id="live-action-excalidraw-skill">Live Action: Excalidraw Skill<a class="heading-link" aria-label="Link to section" href="#live-action-excalidraw-skill"><span class="heading-link-icon">#</span></a></h2>
<p><strong>Install the skill:</strong></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#C0CAF5">npx</span><span style="color:#9ECE6A"> skills</span><span style="color:#9ECE6A"> add</span><span style="color:#9ECE6A"> https://github.com/softaworks/agent-toolkit</span><span style="color:#E0AF68"> --skill</span><span style="color:#9ECE6A"> excalidraw</span></span></code><button type="button" class="copy" data-code="npx skills add https://github.com/softaworks/agent-toolkit --skill excalidraw" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>Install the Excalidraw Extension in VS Code for best experience.</p>
<p><strong>Prompt to customize with brand colors:</strong></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="plaintext"><code><span class="line"><span>Update the excalidraw skill to use these brand colors:</span></span>
<span class="line"><span></span></span>
<span class="line"><span>- Fill: rgb(33, 39, 55)</span></span>
<span class="line"><span>- Text: rgb(234, 237, 243)</span></span>
<span class="line"><span>- Accent: rgb(255, 107, 237)</span></span>
<span class="line"><span>- Card: rgb(52, 63, 96)</span></span>
<span class="line"><span>- Card Muted: rgb(138, 51, 123)</span></span>
<span class="line"><span>- Border: rgb(171, 75, 153)</span></span></code><button type="button" class="copy" data-code="Update the excalidraw skill to use these brand colors:

- Fill: rgb(33, 39, 55)
- Text: rgb(234, 237, 243)
- Accent: rgb(255, 107, 237)
- Card: rgb(52, 63, 96)
- Card Muted: rgb(138, 51, 123)
- Border: rgb(171, 75, 153)" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>→ Agent modifies the skill’s SKILL.md to include color instructions</p>
<hr/>
<script type="application/json" data-slide-config>{"layout":"image","image":"/_astro/robot.CR82n8hL_kLQRJ.webp"}</script> <figure class="slide-image-fallback"><img src="/_astro/robot.CR82n8hL_kLQRJ.webp" alt="Robot working on laptop" loading="lazy" decoding="async" fetchpriority="auto" width="2610" height="1746" class="w-full rounded-lg"></figure>
<hr/>
<h2 id="more-community-skills">More Community Skills<a class="heading-link" aria-label="Link to section" href="#more-community-skills"><span class="heading-link-icon">#</span></a></h2>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#C0CAF5">npx</span><span style="color:#9ECE6A"> skills</span><span style="color:#9ECE6A"> add</span><span style="color:#9ECE6A"> https://github.com/anthropics/skills</span><span style="color:#E0AF68"> --skill</span><span style="color:#9ECE6A"> frontend-design</span></span>
<span class="line"><span style="color:#C0CAF5">npx</span><span style="color:#9ECE6A"> skills</span><span style="color:#9ECE6A"> add</span><span style="color:#9ECE6A"> https://github.com/simonwong/agent-skills</span><span style="color:#E0AF68"> --skill</span><span style="color:#9ECE6A"> code-simplifier</span></span></code><button type="button" class="copy" data-code="npx skills add https://github.com/anthropics/skills --skill frontend-design
npx skills add https://github.com/simonwong/agent-skills --skill code-simplifier" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<ul>
<li><strong>frontend-design</strong> — creates polished, production-grade UI components</li>
<li><strong>code-simplifier</strong> — simplifies and refines code for clarity</li>
</ul>
<p>Browse and discover skills at <a href="https://agentskills.io/" rel="noopener noreferrer" target="_blank">agentskills.io</a></p>
<hr/>
<script type="application/json" data-slide-config>{"layout":"section"}</script> 
<h1 id="key-takeaways">Key Takeaways</h1>
<hr/>
<script type="application/json" data-slide-config>{"layout":"center"}</script> 
<h2 id="key-takeaways-1">Key Takeaways<a class="heading-link" aria-label="Link to section" href="#key-takeaways-1"><span class="heading-link-icon">#</span></a></h2>
<ol>
<li><strong>Agents = LLM + Tools + Loop</strong> (nanocode shows this simply)</li>
<li><strong>Context is finite</strong> — treat tokens as budget</li>
<li><strong>AGENTS.md</strong> — standardized project context</li>
<li><strong>Subagents</strong> — specialized agents for complex tasks</li>
<li><strong>Skills</strong> — portable workflows that load on demand</li>
</ol>
<hr/>
<script type="application/json" data-slide-config>{"layout":"center"}</script> 
<h1 id="thank-you">Thank You!</h1>
<p>Questions?</p>
<hr/>
<script type="application/json" data-slide-config>{"layout":"section"}</script> 
<h1 id="resources">Resources</h1>
<hr/>
<h2 id="resources-1">Resources<a class="heading-link" aria-label="Link to section" href="#resources-1"><span class="heading-link-icon">#</span></a></h2>
<ul>
<li><a href="https://code.visualstudio.com/docs/copilot/agents/overview" rel="noopener noreferrer" target="_blank">VS Code: Using Agents</a> - Agent types and session management</li>
<li><a href="https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents" rel="noopener noreferrer" target="_blank">Anthropic: Effective Context Engineering</a> - Context engineering guide</li>
<li><a href="https://www.youtube.com/watch?v=JepVi1tBNEE" rel="noopener noreferrer" target="_blank">VS Code: Introducing Agent Skills</a> - Agent Skills deep dive</li>
<li><a href="https://code.visualstudio.com/docs/copilot/guides/context-engineering-guide" rel="noopener noreferrer" target="_blank">VS Code: Context Engineering Guide</a> - Microsoft’s context engineering workflow</li>
<li><a href="https://agents.md/" rel="noopener noreferrer" target="_blank">AGENTS.md</a> - Open standard for agent documentation</li>
<li><a href="https://agentskills.io/" rel="noopener noreferrer" target="_blank">Agent Skills Spec</a> - Open standard for portable agent skills</li>
<li><a href="https://github.com/alexanderop/nanocode" rel="noopener noreferrer" target="_blank">nanocode</a> - Minimal agent implementation in TypeScript</li>
<li><a href="https://www.humanlayer.dev/blog/writing-a-good-claude-md" rel="noopener noreferrer" target="_blank">Writing a Good CLAUDE.md</a> - Best practices for agent documentation</li>
<li><a href="https://github.com/alexanderop/claude-plausible-analytics" rel="noopener noreferrer" target="_blank">Plausible SEO Skill</a> - Skills deep dive with Plausible example</li>
<li><a href="https://banay.me/dont-waste-your-backpressure/" rel="noopener noreferrer" target="_blank">Don’t Waste Your Back Pressure</a> - Why automated feedback loops make agents more effective</li>
<li><a href="https://github.com/alexanderop/workshop" rel="noopener noreferrer" target="_blank">Workshop Solution</a> - Complete code examples from this workshop</li>
<li><a href="https://alexop.dev/prompts/claude/claude-learn-command/" rel="noopener noreferrer" target="_blank">Learn Prompt</a> - Skill that helps agents learn from conversations</li>
</ul>
<hr/> </article> <script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).only=e;window.dispatchEvent(new Event("astro:only"));})();</script><astro-island uid="Z1XneyL" component-url="/_astro/presentation.C3Wa0mjp.js" component-export="VMarkBlogRenderer" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;containerSelector&quot;:[0,&quot;#article&quot;],&quot;class&quot;:[0,&quot;astro-vj4tpspi&quot;]}" ssr client="only" opts="{&quot;name&quot;:&quot;VMarkBlogRenderer&quot;,&quot;value&quot;:&quot;react&quot;}"></astro-island> <!-- Fullscreen Modal Container using native dialog --><dialog id="mermaid-modal" class="mermaid-modal" aria-label="Fullscreen diagram view"> <div class="mermaid-modal-content"> <button class="mermaid-modal-close" aria-label="Close fullscreen view" type="button"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <line x1="18" y1="6" x2="6" y2="18"></line> <line x1="6" y1="6" x2="18" y2="18"></line> </svg> </button> <div class="mermaid-modal-diagram"></div> <div class="mermaid-modal-hint">Press <kbd>Esc</kbd> or click outside to close</div> </div> </dialog>  <script type="module">const p=new Set;function g(){const e=document.getElementById("mermaid-modal"),c=e?.querySelector(".mermaid-modal-diagram"),f=e?.querySelector(".mermaid-modal-close");if(!e||!c)return;document.querySelectorAll('svg[id^="mermaid-"]').forEach(t=>{if(!t.id.match(/^mermaid-\d+$/)||p.has(t.id)||t.parentElement?.classList.contains("mermaid-fullscreen-wrapper")||t.closest(".mermaid-modal"))return;p.add(t.id);const n=document.createElement("div");n.className="mermaid-fullscreen-wrapper mermaid-clickable",n.setAttribute("tabindex","0"),n.setAttribute("role","button"),n.setAttribute("aria-label","Click to view diagram fullscreen"),t.parentElement?.insertBefore(n,t),n.appendChild(t);const o=document.createElement("div");o.className="mermaid-expand-icon",o.innerHTML=`
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="15 3 21 3 21 9"></polyline>
          <polyline points="9 21 3 21 3 15"></polyline>
          <line x1="21" y1="3" x2="14" y2="10"></line>
          <line x1="3" y1="21" x2="10" y2="14"></line>
        </svg>
        <span>Fullscreen</span>
      `,n.appendChild(o);const d=m=>{m.stopPropagation(),c.innerHTML="";const i=t.cloneNode(!0),s=t.id,w=`-modal-${Date.now()}`,u=`${s}${w}`;i.setAttribute("id",u);const E=new Map;i.querySelectorAll("[id]").forEach(l=>{if(l===i)return;const a=l.getAttribute("id"),h=a+w;E.set(a,h),l.setAttribute("id",h)});let r=i.innerHTML;E.forEach((l,a)=>{r=r.replace(new RegExp(`url\\(#${a}\\)`,"g"),`url(#${l})`),r=r.replace(new RegExp(`href="#${a}"`,"g"),`href="#${l}"`)}),r=r.replace(new RegExp(`#${s}([^_\\w-])`,"g"),`#${u}$1`),r=r.replace(new RegExp(`#${s}\\{`,"g"),`#${u}{`),i.innerHTML=r,i.removeAttribute("style");const y=i.getAttribute("viewBox");if(y){const[,,l,a]=y.split(" ").map(Number);i.setAttribute("width",String(l)),i.setAttribute("height",String(a))}c.appendChild(i),e.showModal(),f.focus()};n.addEventListener("click",d),n.addEventListener("keydown",m=>{(m.key==="Enter"||m.key===" ")&&(m.preventDefault(),d(m))})}),f?.addEventListener("click",v),e?.addEventListener("click",t=>{const o=e?.querySelector(".mermaid-modal-content")?.getBoundingClientRect(),d=t;o&&(d.clientX<o.left||d.clientX>o.right||d.clientY<o.top||d.clientY>o.bottom)&&v()}),e.addEventListener("close",b)}function v(){const e=document.getElementById("mermaid-modal");e&&e.open&&e.close()}function b(){const c=document.getElementById("mermaid-modal")?.querySelector(".mermaid-modal-diagram");c&&(c.innerHTML="")}document.readyState==="loading"?document.addEventListener("DOMContentLoaded",g):g();document.addEventListener("astro:page-load",()=>{p.clear(),g()});</script> <astro-island uid="Z1ztiT3" prefix="r23" component-url="/_astro/presentation.C3Wa0mjp.js" component-export="PresentationMode" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;articleSelector&quot;:[0,&quot;#article&quot;],&quot;title&quot;:[0,&quot;Next Level GitHub Copilot: Agents, Instructions &amp; Automation in VS Code&quot;],&quot;slug&quot;:[0,&quot;vs-code-copilot-workshop&quot;],&quot;conference&quot;:[0,&quot;Technical SUMMIT 2026&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PresentationMode&quot;,&quot;value&quot;:true}" await-children><button type="button" aria-label="Enter presentation mode (P)" class="fixed bottom-20 right-4 flex items-center gap-2 rounded-full bg-skin-accent px-4 py-2 text-skin-inverted shadow-lg transition-all duration-300 hover:opacity-90 hover:scale-105 opacity-100"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-presentation h-5 w-5"><path d="M2 3h20"></path><path d="M21 3v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V3"></path><path d="m7 21 5-5 5 5"></path></svg><span class="text-sm font-medium">(P)</span></button><!--astro:end--></astro-island> <div id="cta-follow" class="notification-container fixed bottom-24 left-0 z-50 max-w-sm -translate-x-full opacity-0 transition-all duration-500 ease-out astro-vj4tpspi"> <div class="mx-4 transform rounded-lg border-l-4 border-skin-accent bg-skin-card p-6 shadow-xl transition-transform duration-200 hover:scale-[1.02] astro-vj4tpspi"> <div class="flex flex-col gap-4 astro-vj4tpspi"> <div class="flex items-center gap-3 astro-vj4tpspi"> <div class="rounded-full bg-skin-accent bg-opacity-10 p-2 astro-vj4tpspi"> <svg class="h-6 w-6 text-skin-accent astro-vj4tpspi" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg> </div> <h3 class="text-xl font-bold text-skin-accent astro-vj4tpspi">Stay Updated!</h3> </div> <div class="space-y-2 astro-vj4tpspi"> <p class="text-base leading-relaxed text-skin-base astro-vj4tpspi">
Subscribe to my newsletter for more TypeScript, Vue, and web dev
              insights directly in your inbox.
</p> <ul class="ml-1 list-inside list-disc space-y-1 text-sm text-skin-base astro-vj4tpspi"> <li class="astro-vj4tpspi">Background information about the articles</li> <li class="astro-vj4tpspi">
Weekly Summary of all the interesting blog posts that I read
</li> <li class="astro-vj4tpspi">Small tips and trick</li> </ul> </div> <a href="https://alex-op-newsletter.beehiiv.com/subscribe?utm_source=blog&utm_medium=post&utm_campaign=post_vs-code-copilot-workshop" target="_blank" rel="noopener noreferrer" id="newsletter-subscribe-button" class="inline-flex items-center justify-center gap-2 rounded-full bg-skin-accent px-6 py-3 text-base font-semibold text-skin-inverted shadow-md transition-all duration-200 hover:scale-[1.02] hover:transform hover:opacity-90 astro-vj4tpspi"> <svg class="h-5 w-5 fill-current astro-vj4tpspi" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg>
Subscribe Now
</a> <button id="newsletter-dismiss" data-post-slug="vs-code-copilot-workshop" class="absolute right-3 top-3 rounded-full p-1 text-skin-base transition-all duration-200 hover:bg-skin-accent hover:bg-opacity-10 hover:text-skin-accent astro-vj4tpspi" aria-label="Close notification"> <svg class="h-5 w-5 astro-vj4tpspi" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class="astro-vj4tpspi"></path> </svg> </button> </div> </div> </div> <ul class="my-8 flex flex-wrap gap-2 astro-vj4tpspi"> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/vs-code/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-2"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">vs-code</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/github-copilot/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-3"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">github-copilot</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/ai-agents/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-4"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">ai-agents</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/context-engineering/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-5"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">context-engineering</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/workshop/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-6"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">workshop</span>   </a> </li>  </ul> <div class="flex flex-col-reverse items-center justify-between gap-6 sm:flex-row-reverse sm:items-end sm:gap-4 astro-vj4tpspi"> <button id="back-to-top" class="focus-outline whitespace-nowrap py-1 hover:opacity-75 astro-vj4tpspi"> <svg xmlns="http://www.w3.org/2000/svg" class="rotate-90 astro-vj4tpspi"> <path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg> <span class="astro-vj4tpspi">Back to Top</span> </button> <div class="social-icons astro-wkojbtzc"> <span class="italic astro-wkojbtzc">Share this post on:</span> <div class="text-center astro-wkojbtzc"> <a href="https://wa.me/?text=https://alexop.dev/posts/vs-code-copilot-workshop/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via WhatsApp" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"></path>
      <path d="M9 10a0.5 .5 0 0 0 1 0v-1a0.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a0.5 .5 0 0 0 0 -1h-1a0.5 .5 0 0 0 0 1"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via WhatsApp</span> </a><a href="https://www.facebook.com/sharer.php?u=https://alexop.dev/posts/vs-code-copilot-workshop/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Facebook" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"
    ></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on Facebook</span> </a><a href="https://x.com/intent/tweet?url=https://alexop.dev/posts/vs-code-copilot-workshop/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Tweet this post" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Tweet this post</span> </a><a href="https://t.me/share/url?url=https://alexop.dev/posts/vs-code-copilot-workshop/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via Telegram" target="_blank" rel="noopener noreferrer"> <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon-tabler"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"></path>
      </svg> <span class="sr-only astro-wkojbtzc">Share this post via Telegram</span> </a><a href="https://pinterest.com/pin/create/button/?url=https://alexop.dev/posts/vs-code-copilot-workshop/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Pinterest" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <line x1="8" y1="20" x2="12" y2="11"></line>
      <path d="M10.7 14c.437 1.263 1.43 2 2.55 2c2.071 0 3.75 -1.554 3.75 -4a5 5 0 1 0 -9.7 1.7"></path>
      <circle cx="12" cy="12" r="9"></circle>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post on Pinterest</span> </a><a href="mailto:?subject=See%20this%20post&#38;body=https://alexop.dev/posts/vs-code-copilot-workshop/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via email" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via email</span> </a><a href="https://www.linkedin.com/shareArticle?mini=true&url=https://alexop.dev/posts/vs-code-copilot-workshop/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
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
    </script> </body> </html>  <script>(function(){const postSlug = "vs-code-copilot-workshop";

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
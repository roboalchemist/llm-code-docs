# Source: https://alexop.dev/posts/custom-tdd-workflow-claude-code-vue

<!DOCTYPE html><html lang="en" class="scroll-smooth astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/posts/custom-tdd-workflow-claude-code-vue/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>Forcing Claude Code to TDD: An Agentic Red-Green-Refactor Loop | alexop.dev</title><meta name="title" content="Forcing Claude Code to TDD: An Agentic Red-Green-Refactor Loop | alexop.dev"><meta name="description" content="Build a custom TDD workflow with Claude Code using skills and subagents that enforce Red-Green-Refactor discipline for your Vue projects."><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="Forcing Claude Code to TDD: An Agentic Red-Green-Refactor Loop | alexop.dev"><meta property="og:description" content="Build a custom TDD workflow with Claude Code using skills and subagents that enforce Red-Green-Refactor discipline for your Vue projects."><meta property="og:url" content="https://alexop.dev/posts/custom-tdd-workflow-claude-code-vue/"><meta property="og:image" content="https://alexop.dev/posts/forcing-claude-code-to-tdd-an-agentic-red-green-refactor-loop/index.png"><meta property="og:type" content="article"><!-- Article Published/Modified time --><meta property="article:published_time" content="2025-11-30T00:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/posts/custom-tdd-workflow-claude-code-vue/"><meta property="twitter:title" content="Forcing Claude Code to TDD: An Agentic Red-Green-Refactor Loop | alexop.dev"><meta property="twitter:description" content="Build a custom TDD workflow with Claude Code using skills and subagents that enforce Red-Green-Refactor discipline for your Vue projects."><meta property="twitter:image" content="https://alexop.dev/posts/forcing-claude-code-to-tdd-an-agentic-red-green-refactor-loop/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"Forcing Claude Code to TDD: An Agentic Red-Green-Refactor Loop | alexop.dev","description":"Build a custom TDD workflow with Claude Code using skills and subagents that enforce Red-Green-Refactor discipline for your Vue projects.","image":"https://alexop.dev/posts/forcing-claude-code-to-tdd-an-agentic-red-green-refactor-loop/index.png","datePublished":"2025-11-30T00:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
<style>a:where(.astro-blwjyjpt){transition:all .3s ease}a:where(.astro-blwjyjpt):hover{transform:translateY(-2px);box-shadow:0 4px 6px -1px #0000001a,0 2px 4px -1px #0000000f}
.minimal-posts-list:where(.astro-eenky23y){width:100%;max-width:64rem;margin:0 auto;padding:2rem 1rem;background:rgb(var(--color-fill));color:rgb(var(--color-text-base))}.posts-title:where(.astro-eenky23y){font-size:2rem;margin-bottom:2rem;color:rgb(var(--color-accent));font-family:inherit;font-weight:600;letter-spacing:.02em}.year-group:where(.astro-eenky23y){margin-bottom:2.5rem}.year-heading:where(.astro-eenky23y){font-size:1.3rem;color:rgb(var(--color-text-base));margin:2.5rem 0 1.2rem;font-family:inherit;font-weight:500;letter-spacing:.04em}.year-group:where(.astro-eenky23y) ul:where(.astro-eenky23y){list-style:none;padding:0;margin:0}.post-item:where(.astro-eenky23y){display:flex;justify-content:space-between;align-items:center;padding:1rem 0;border-bottom:1px solid rgba(var(--color-border),.2)}.post-link:where(.astro-eenky23y){color:rgb(var(--color-text-base));text-decoration:none;font-size:1.1rem;transition:color .2s}.post-link:where(.astro-eenky23y):hover{color:rgb(var(--color-accent))}.post-date:where(.astro-eenky23y){color:rgb(var(--color-card-muted));font-size:.95rem;font-family:inherit;letter-spacing:.05em;min-width:70px;text-align:right}
@keyframes astroFadeInOut{0%{opacity:1}to{opacity:0}}@keyframes astroFadeIn{0%{opacity:0;mix-blend-mode:plus-lighter}to{opacity:1;mix-blend-mode:plus-lighter}}@keyframes astroFadeOut{0%{opacity:1;mix-blend-mode:plus-lighter}to{opacity:0;mix-blend-mode:plus-lighter}}@keyframes astroSlideFromRight{0%{transform:translate(100%)}}@keyframes astroSlideFromLeft{0%{transform:translate(-100%)}}@keyframes astroSlideToRight{to{transform:translate(100%)}}@keyframes astroSlideToLeft{to{transform:translate(-100%)}}@media(prefers-reduced-motion){::view-transition-group(*),::view-transition-old(*),::view-transition-new(*){animation:none!important}[data-astro-transition-scope]{animation:none!important}}
</style>
<link rel="stylesheet" href="/_astro/index.Ck-KI3hC.css">
<style>.subagent-diagram-container:where(.astro-tpygpejy){display:flex;flex-direction:column;align-items:center;margin:2rem 0;width:100%}.subagent-diagram-fallback:where(.astro-tpygpejy){width:100%;max-width:600px}.subagent-diagram-svg:where(.astro-tpygpejy){width:100%;height:auto}.agent-circle:where(.astro-tpygpejy){fill:rgb(var(--color-accent) / .1);stroke:rgb(var(--color-accent));stroke-width:2}.subagent-circle:where(.astro-tpygpejy){fill:rgb(var(--color-accent) / .05);stroke:rgb(var(--color-accent) / .7);stroke-width:2;stroke-dasharray:4 2}.agent-icon:where(.astro-tpygpejy){font-size:24px}.agent-label:where(.astro-tpygpejy){fill:rgb(var(--color-text-base));font-size:12px;font-weight:500}.arrow-path:where(.astro-tpygpejy){fill:none;stroke:rgb(var(--color-text-base) / .5);stroke-width:2}.arrow-path:where(.astro-tpygpejy).dashed{stroke-dasharray:5 3}.arrow-path:where(.astro-tpygpejy).search-arrow{stroke:rgb(var(--color-accent) / .6)}.arrowhead-fill:where(.astro-tpygpejy){fill:rgb(var(--color-text-base) / .5)}.arrow-label:where(.astro-tpygpejy){fill:rgb(var(--color-text-base) / .6);font-size:11px;font-style:italic}.file-tree:where(.astro-tpygpejy) .folder:where(.astro-tpygpejy){fill:rgb(var(--color-text-base));font-size:14px;font-family:ui-monospace,monospace}.file-tree:where(.astro-tpygpejy) .file:where(.astro-tpygpejy){fill:rgb(var(--color-text-base) / .7);font-size:14px;font-family:ui-monospace,monospace}.file-tree:where(.astro-tpygpejy) .file:where(.astro-tpygpejy).highlight{fill:rgb(var(--color-accent));font-weight:600}.subagent-diagram-caption:where(.astro-tpygpejy){margin-top:1rem;text-align:center;font-size:.875rem;color:rgb(var(--color-text-base) / .7)}.subagent-diagram-fallback:where(.astro-tpygpejy){display:none}
.parallel-subagent-diagram-container:where(.astro-u2chhpb2){display:flex;flex-direction:column;align-items:center;margin:2rem 0;width:100%}.parallel-subagent-diagram-fallback:where(.astro-u2chhpb2){width:100%;max-width:800px}.parallel-subagent-diagram-svg-static:where(.astro-u2chhpb2){width:100%;height:auto}.agent-circle:where(.astro-u2chhpb2){fill:rgb(var(--color-accent) / .1);stroke:rgb(var(--color-accent));stroke-width:2}.subagent-circle:where(.astro-u2chhpb2){stroke-width:2;stroke-dasharray:4 2}.agent-icon:where(.astro-u2chhpb2){font-size:24px}.agent-label:where(.astro-u2chhpb2){fill:rgb(var(--color-text-base));font-size:12px;font-weight:500}.task-label:where(.astro-u2chhpb2){fill:rgb(var(--color-text-base) / .8);font-size:13px;font-family:ui-monospace,monospace}.arrow-path:where(.astro-u2chhpb2){fill:none;stroke:rgb(var(--color-text-base) / .5);stroke-width:2}.arrow-path:where(.astro-u2chhpb2).dashed{stroke-dasharray:5 3}.arrow-path:where(.astro-u2chhpb2).report{stroke:#22c55e}.arrowhead-fill:where(.astro-u2chhpb2){fill:rgb(var(--color-text-base) / .5)}.domain-box-rect:where(.astro-u2chhpb2){fill:rgb(var(--color-fill) / .5);stroke-width:1.5}.domain-label:where(.astro-u2chhpb2){font-size:11px;font-weight:600}.finding-text:where(.astro-u2chhpb2){fill:rgb(var(--color-text-base) / .7);font-size:10px;font-family:ui-monospace,monospace}.synthesis-box:where(.astro-u2chhpb2){fill:#22c55e1a;stroke:#22c55e;stroke-width:2}.synthesis-text:where(.astro-u2chhpb2){fill:#22c55e;font-size:13px;font-weight:600}.parallel-subagent-diagram-caption:where(.astro-u2chhpb2){margin-top:1rem;text-align:center;font-size:.875rem;color:rgb(var(--color-text-base) / .7)}.parallel-subagent-diagram-fallback:where(.astro-u2chhpb2){display:none}
.shiki-magic-move-container{position:relative;white-space:pre}.shiki-magic-move-line-number{opacity:.3;-webkit-user-select:none;-moz-user-select:none;user-select:none}.shiki-magic-move-item{display:inline-block;transition:color var(--smm-duration,.5s) var(--smm-easing,"ease")}.shiki-magic-move-enter-active,.shiki-magic-move-leave-active,.shiki-magic-move-move{transition:all var(--smm-duration,.5s) var(--smm-easing,"ease")}.shiki-magic-move-container-resize,.shiki-magic-move-container-restyle{transition:all var(--smm-duration,.5s) var(--smm-easing,"ease");transition-delay:calc(var(--smm-duration, .5s)*var(--smm-delay-container, 1))}.shiki-magic-move-move{transition-delay:calc(var(--smm-duration, .5s)*var(--smm-delay-move, 1) + var(--smm-stagger, 0));z-index:1}.shiki-magic-move-enter-active{transition-delay:calc(var(--smm-duration, .5s)*var(--smm-delay-enter, 1) + var(--smm-stagger, 0));z-index:1}.shiki-magic-move-leave-active{transition-delay:calc(var(--smm-duration, .5s)*var(--smm-delay-leave, 1) + var(--smm-stagger, 0))}.shiki-magic-move-enter-from,.shiki-magic-move-leave-to{opacity:0}br.shiki-magic-move-leave-active{display:none}
.shiki-magic-move-container{position:relative;white-space:pre}.shiki-magic-move-line-number{opacity:.3;-webkit-user-select:none;-moz-user-select:none;user-select:none}.shiki-magic-move-item{display:inline-block;transition:color var(--smm-duration,.5s) var(--smm-easing,"ease")}.shiki-magic-move-enter-active,.shiki-magic-move-leave-active,.shiki-magic-move-move{transition:all var(--smm-duration,.5s) var(--smm-easing,"ease")}.shiki-magic-move-container-resize,.shiki-magic-move-container-restyle{transition:all var(--smm-duration,.5s) var(--smm-easing,"ease");transition-delay:calc(var(--smm-duration, .5s)*var(--smm-delay-container, 1))}.shiki-magic-move-move{transition-delay:calc(var(--smm-duration, .5s)*var(--smm-delay-move, 1) + var(--smm-stagger, 0));z-index:1}.shiki-magic-move-enter-active{transition-delay:calc(var(--smm-duration, .5s)*var(--smm-delay-enter, 1) + var(--smm-stagger, 0));z-index:1}.shiki-magic-move-leave-active{transition-delay:calc(var(--smm-duration, .5s)*var(--smm-delay-leave, 1) + var(--smm-stagger, 0))}.shiki-magic-move-enter-from,.shiki-magic-move-leave-to{opacity:0}br.shiki-magic-move-leave-active{display:none}
.jazz-demo-root[data-v-1a336f1a]{background:#030712;border:1px solid #374151;border-radius:.75rem;padding:1rem;font-family:system-ui,-apple-system,sans-serif;color:#e5e7eb;font-size:14px}.jazz-demo-header[data-v-1a336f1a]{display:flex;align-items:center;justify-content:space-between;margin-bottom:1rem}.jazz-demo-title[data-v-1a336f1a]{color:#fff;font-size:1rem;font-weight:600}.jazz-demo-toggles[data-v-1a336f1a]{display:flex;align-items:center;gap:.75rem}.jazz-demo-toggle-wrap[data-v-1a336f1a]{display:flex;align-items:center;gap:.5rem}.jazz-demo-toggle-label[data-v-1a336f1a]{color:#d1d5db;font-size:.75rem}.jazz-demo-toggle[data-v-1a336f1a]{position:relative;display:inline-flex;height:1.25rem;width:2.25rem;align-items:center;border-radius:9999px;transition:background-color .2s;border:none;cursor:pointer;padding:0}.jazz-demo-toggle-on[data-v-1a336f1a]{background:#2563eb}.jazz-demo-toggle-off[data-v-1a336f1a]{background:#4b5563}.jazz-demo-toggle-dot[data-v-1a336f1a]{display:inline-block;height:.875rem;width:.875rem;border-radius:9999px;background:#fff;transition:transform .2s}.jazz-demo-toggle-dot-on[data-v-1a336f1a]{transform:translate(1.125rem)}.jazz-demo-toggle-dot-off[data-v-1a336f1a]{transform:translate(.125rem)}.jazz-demo-covalue-id[data-v-1a336f1a]{display:flex;align-items:center;gap:.375rem;margin-bottom:.5rem;padding:.25rem .5rem;background:#1e1b4b;border:1px solid #3730a3;border-radius:.375rem;overflow:hidden}.jazz-demo-covalue-label[data-v-1a336f1a]{color:#a78bfa;font-size:.625rem;font-weight:600;white-space:nowrap}.jazz-demo-covalue-code[data-v-1a336f1a]{color:#c4b5fd;font-size:.625rem;font-family:ui-monospace,monospace;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.jazz-demo-card[data-v-1a336f1a]{background:#111827;border:1px solid #374151;border-radius:.75rem;padding:1rem}.jazz-demo-loading[data-v-1a336f1a]{color:#9ca3af;text-align:center;padding:2rem 0}.jazz-demo-card[data-v-1a336f1a]{padding:1.5rem}.jazz-counter-display[data-v-1a336f1a]{font-size:3rem;font-weight:700;color:#fff;text-align:center;padding:1rem 0;font-variant-numeric:tabular-nums}.jazz-counter-controls[data-v-1a336f1a]{display:flex;gap:.5rem}.jazz-counter-btn[data-v-1a336f1a]{flex:1;padding:.5rem;font-size:1.25rem;font-weight:600;border:1px solid #374151;border-radius:.5rem;background:#1f2937;color:#e5e7eb;cursor:pointer;transition:background-color .2s}.jazz-counter-btn[data-v-1a336f1a]:hover{background:#374151}.jazz-counter-btn-primary[data-v-1a336f1a]{background:#2563eb;border-color:#2563eb;color:#fff}.jazz-counter-btn-primary[data-v-1a336f1a]:hover{background:#1d4ed8}
.jazz-demo-root[data-v-d8349330]{background:#030712;border:1px solid #374151;border-radius:.75rem;padding:1rem;font-family:system-ui,-apple-system,sans-serif;color:#e5e7eb;font-size:14px}.jazz-demo-header[data-v-d8349330]{display:flex;align-items:center;justify-content:space-between;margin-bottom:1rem}.jazz-demo-title[data-v-d8349330]{color:#fff;font-size:1rem;font-weight:600}.jazz-demo-toggles[data-v-d8349330]{display:flex;align-items:center;gap:.75rem}.jazz-demo-toggle-wrap[data-v-d8349330]{display:flex;align-items:center;gap:.5rem}.jazz-demo-toggle-label[data-v-d8349330]{color:#d1d5db;font-size:.75rem}.jazz-demo-toggle[data-v-d8349330]{position:relative;display:inline-flex;height:1.25rem;width:2.25rem;align-items:center;border-radius:9999px;transition:background-color .2s;border:none;cursor:pointer;padding:0}.jazz-demo-toggle-on[data-v-d8349330]{background:#2563eb}.jazz-demo-toggle-off[data-v-d8349330]{background:#4b5563}.jazz-demo-toggle-dot[data-v-d8349330]{display:inline-block;height:.875rem;width:.875rem;border-radius:9999px;background:#fff;transition:transform .2s}.jazz-demo-toggle-dot-on[data-v-d8349330]{transform:translate(1.125rem)}.jazz-demo-toggle-dot-off[data-v-d8349330]{transform:translate(.125rem)}.jazz-demo-covalue-id[data-v-d8349330]{display:flex;align-items:center;gap:.375rem;margin-bottom:.5rem;padding:.25rem .5rem;background:#1e1b4b;border:1px solid #3730a3;border-radius:.375rem;overflow:hidden}.jazz-demo-covalue-label[data-v-d8349330]{color:#a78bfa;font-size:.625rem;font-weight:600;white-space:nowrap}.jazz-demo-covalue-code[data-v-d8349330]{color:#c4b5fd;font-size:.625rem;font-family:ui-monospace,monospace;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.jazz-demo-card[data-v-d8349330]{background:#111827;border:1px solid #374151;border-radius:.75rem;padding:1rem}.jazz-demo-loading[data-v-d8349330]{color:#9ca3af;text-align:center;padding:2rem 0}.jazz-demo-card-title[data-v-d8349330]{font-size:1.25rem;font-weight:700;color:#fff;margin:0 0 .75rem}.jazz-demo-form[data-v-d8349330]{margin-bottom:.75rem;display:flex;flex-direction:column;gap:.5rem}.jazz-demo-input[data-v-d8349330]{width:100%;padding:.375rem .625rem;background:#1f2937;border:1px solid #4b5563;border-radius:.5rem;color:#fff;font-size:.8125rem;outline:none;box-sizing:border-box}.jazz-demo-input[data-v-d8349330]:focus{border-color:#3b82f6;box-shadow:0 0 0 2px #3b82f64d}.jazz-demo-input[data-v-d8349330]::-moz-placeholder{color:#6b7280}.jazz-demo-input[data-v-d8349330]::placeholder{color:#6b7280}.jazz-demo-add-btn[data-v-d8349330]{width:100%;padding:.375rem .75rem;background:#2563eb;color:#fff;border:none;border-radius:.5rem;font-weight:500;font-size:.8125rem;cursor:pointer;transition:background-color .2s}.jazz-demo-add-btn[data-v-d8349330]:hover{background:#1d4ed8}.jazz-demo-list[data-v-d8349330]{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:.25rem}.jazz-demo-item[data-v-d8349330]{display:flex;align-items:center;gap:.5rem;padding:.375rem;border-radius:.5rem}.jazz-demo-item[data-v-d8349330]:hover{background:#1f2937}.jazz-demo-item:hover .jazz-demo-delete[data-v-d8349330]{opacity:1}.jazz-demo-drag[data-v-d8349330]{cursor:grab;color:#4b5563;transition:color .2s;-webkit-user-select:none;-moz-user-select:none;user-select:none;display:flex;align-items:center}.jazz-demo-drag[data-v-d8349330]:active{cursor:grabbing}.jazz-demo-item:hover .jazz-demo-drag[data-v-d8349330]{color:#9ca3af}.jazz-demo-svg[data-v-d8349330]{width:1rem;height:1rem}.jazz-demo-checkbox[data-v-d8349330]{width:.875rem;height:.875rem;accent-color:#2563eb}.jazz-demo-text[data-v-d8349330]{flex:1;color:#e5e7eb;font-size:.8125rem}.jazz-demo-text-done[data-v-d8349330]{text-decoration:line-through;color:#6b7280}.jazz-demo-delete[data-v-d8349330]{opacity:0;transition:opacity .2s;color:#6b7280;background:none;border:none;padding:.125rem;cursor:pointer;display:flex;align-items:center}.jazz-demo-delete[data-v-d8349330]:hover{color:#f87171}.jazz-demo-empty[data-v-d8349330]{color:#6b7280;text-align:center;padding:1rem 0;margin:0;font-size:.8125rem}
</style><style>[data-astro-transition-scope="astro-plk3gbjq-1"] { view-transition-name: forcing-claude-code-to-tdd-an-agentic-red-green-refactor-loop; }@layer astro { ::view-transition-old(forcing-claude-code-to-tdd-an-agentic-red-green-refactor-loop) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(forcing-claude-code-to-tdd-an-agentic-red-green-refactor-loop) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(forcing-claude-code-to-tdd-an-agentic-red-green-refactor-loop) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(forcing-claude-code-to-tdd-an-agentic-red-green-refactor-loop) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-3"] { view-transition-name: vue; }@layer astro { ::view-transition-old(vue) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(vue) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(vue) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(vue) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-4"] { view-transition-name: testing; }@layer astro { ::view-transition-old(testing) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(testing) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(testing) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(testing) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-5"] { view-transition-name: claude-code; }@layer astro { ::view-transition-old(claude-code) { 
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <div class="mx-auto flex w-full max-w-5xl justify-start px-2 astro-vj4tpspi"> <button class="focus-outline mb-2 mt-8 flex hover:opacity-75 astro-vj4tpspi" onclick="(() => (history.length === 1) ? window.location = '/' : history.back())()"> <svg xmlns="http://www.w3.org/2000/svg" class="astro-vj4tpspi"><path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg><span class="astro-vj4tpspi">Go back</span> </button> </div> <main data-pagefind-body id="main-content" class="relative astro-vj4tpspi"> <h1 class="post-title astro-vj4tpspi" data-astro-transition-scope="astro-plk3gbjq-1">Forcing Claude Code to TDD: An Agentic Red-Green-Refactor Loop</h1> <div class="my-2 flex items-center justify-between astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-100 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-base"><time dateTime="2025-11-30T00:00:00.000Z">Nov 30, 2025</time><span class="sr-only"> at </span></span></div> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="fN8Jh" prefix="r6" component-url="/_astro/PostCopyButton.-PGtk4At.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;title&quot;:[0,&quot;Forcing Claude Code to TDD: An Agentic Red-Green-Refactor Loop&quot;],&quot;content&quot;:[0,&quot;import Alert from \&quot;@features/mdx-components/components/Alert.astro\&quot;;\nimport InternalLink from \&quot;@features/mdx-components/components/InternalLink.astro\&quot;;\nimport Figure from \&quot;@features/mdx-components/components/Figure.astro\&quot;;\nimport tddOverview from \&quot;@assets/images/claude/tddOverviewClaudeCode.png\&quot;;\nimport hooksOverview from \&quot;@assets/images/claude/HOOKSCLAUDE.png\&quot;;\nimport skillOverview from \&quot;@assets/images/claude/claudeCodeSKill.png\&quot;;\nimport contextProblem from \&quot;@assets/images/claude/contextProblem.png\&quot;;\n\n&lt;Figure src={tddOverview} alt=\&quot;TDD workflow overview with Claude Code showing Red-Green-Refactor cycle\&quot; caption=\&quot;Custom TDD workflow with Claude Code: Skills orchestrate subagents through the Red-Green-Refactor cycle\&quot; /&gt;\n\nI rely on Claude Code, but it has a structural limitation: it defaults to implementation-first. It writes the \&quot;Happy Path,\&quot; ignoring edge cases. When I try to force TDD in a single context window, the implementation \&quot;bleeds\&quot; into the test logic (context pollution). This article documents a multi-agent system using Claude&#39;s \&quot;Skills\&quot; and \&quot;Hooks\&quot; that enforces a strict Red-Green-Refactor cycle.\n\n&lt;Alert type=\&quot;note\&quot; title=\&quot;Framework Agnostic\&quot;&gt;\n  While this article uses Vue as an example, the TDD principles and Claude Code workflow apply to any technology. Whether you&#39;re working with React, Angular, Svelte, or even backend languages like Python, Go, or Rust—the Red-Green-Refactor cycle and subagent orchestration work the same way.\n&lt;/Alert&gt;\n\n## The Problem with AI-Assisted TDD\n\nWhen I ask Claude to \&quot;implement feature X,\&quot; it writes the implementation first. Every time. TDD flips this—you write the test first, watch it fail, then write minimal code to make it pass.\n\nI needed a way to:\n* **Force test-first** — No implementation before a failing test exists\n* **Keep phases focused** — The test writer shouldn&#39;t think about implementation details\n* **Ensure refactoring happens** — Easy to skip when the feature already works\n\n## Skills + Subagents\n\nClaude Code supports two features I hadn&#39;t explored until recently:\n\n* **&lt;InternalLink slug=\&quot;understanding-claude-code-full-stack\&quot;&gt;Skills&lt;/InternalLink&gt;** (`.claude/skills/`): High-level workflows that orchestrate complex tasks\n* **Agents** (`.claude/agents/`): Specialized workers that handle specific jobs\n\nYou might wonder: why use subagents at all? Skills alone could handle the TDD workflow. But there&#39;s a catch—context pollution.\n\n### The Context Pollution Problem\n\n&lt;Alert type=\&quot;warning\&quot; title=\&quot;Why Single-Context LLMs Cheat at TDD\&quot;&gt;\nWhen everything runs in one context window, **the LLM cannot truly follow TDD**. The test writer&#39;s detailed analysis bleeds into the implementer&#39;s thinking. The implementer&#39;s code exploration pollutes the refactorer&#39;s evaluation. Each phase drags along baggage from the others.\n\nThis isn&#39;t just messy—it fundamentally breaks TDD. The whole point of writing the test first is that **you don&#39;t know the implementation yet**. But if the same context sees both phases, the LLM subconsciously designs tests around the implementation it&#39;s already planning. It \&quot;cheats\&quot; without meaning to.\n&lt;/Alert&gt;\n\n&lt;Figure src={contextProblem} alt=\&quot;Context pollution problem when running all TDD phases in a single context\&quot; caption=\&quot;Without subagents, each phase pollutes the context with irrelevant details from previous phases\&quot; /&gt;\n\n**Subagents solve this architectural limitation.** Each phase runs in complete isolation:\n\n- The **test writer** focuses purely on test design—it has no idea how the feature will be implemented\n- The **implementer** sees only the failing test—it can&#39;t be influenced by test-writing decisions\n- The **refactorer** evaluates clean implementation code—it starts fresh without implementation baggage\n\nEach agent starts with exactly the context it needs and nothing more. This isn&#39;t just organization—it&#39;s the only way to get genuine test-first development from an LLM.\n\nCombining skills with subagents gave me exactly what I needed:\n\n&lt;Figure src={skillOverview} alt=\&quot;Claude Code skill structure showing how skills orchestrate subagents\&quot; caption=\&quot;Skills define high-level workflows that coordinate specialized subagents\&quot; /&gt;\n\n## The TDD Skill\n\nThe orchestrating skill lives at `.claude/skills/tdd-integration/skill.md`:\n\n```markdown\n---\nname: tdd-integration\ndescription: Enforce Test-Driven Development with strict Red-Green-Refactor cycle using integration tests. Auto-triggers when implementing new features or functionality. Trigger phrases include \&quot;implement\&quot;, \&quot;add feature\&quot;, \&quot;build\&quot;, \&quot;create functionality\&quot;, or any request to add new behavior. Does NOT trigger for bug fixes, documentation, or configuration changes.\n---\n\n# TDD Integration Testing\n\nEnforce strict Test-Driven Development using the Red-Green-Refactor cycle with dedicated subagents.\n\n## Mandatory Workflow\n\nEvery new feature MUST follow this strict 3-phase cycle. Do NOT skip phases.\n\n### Phase 1: RED - Write Failing Test\n\n🔴 RED PHASE: Delegating to tdd-test-writer...\n\nInvoke the `tdd-test-writer` subagent with:\n- Feature requirement from user request\n- Expected behavior to test\n\nThe subagent returns:\n- Test file path\n- Failure output confirming test fails\n- Summary of what the test verifies\n\n**Do NOT proceed to Green phase until test failure is confirmed.**\n\n### Phase 2: GREEN - Make It Pass\n\n🟢 GREEN PHASE: Delegating to tdd-implementer...\n\nInvoke the `tdd-implementer` subagent with:\n- Test file path from RED phase\n- Feature requirement context\n\nThe subagent returns:\n- Files modified\n- Success output confirming test passes\n- Implementation summary\n\n**Do NOT proceed to Refactor phase until test passes.**\n\n### Phase 3: REFACTOR - Improve\n\n🔵 REFACTOR PHASE: Delegating to tdd-refactorer...\n\nInvoke the `tdd-refactorer` subagent with:\n- Test file path\n- Implementation files from GREEN phase\n\nThe subagent returns either:\n- Changes made + test success output, OR\n- \&quot;No refactoring needed\&quot; with reasoning\n\n**Cycle complete when refactor phase returns.**\n\n## Multiple Features\n\nComplete the full cycle for EACH feature before starting the next:\n\nFeature 1: 🔴 → 🟢 → 🔵 ✓\nFeature 2: 🔴 → 🟢 → 🔵 ✓\nFeature 3: 🔴 → 🟢 → 🔵 ✓\n\n## Phase Violations\n\nNever:\n- Write implementation before the test\n- Proceed to Green without seeing Red fail\n- Skip Refactor evaluation\n- Start a new feature before completing the current cycle\n```\n\nThe `description` field contains trigger phrases so Claude activates this skill automatically when I ask to implement something. Each phase has explicit \&quot;Do NOT proceed until...\&quot; gates—Claude needs clear boundaries. The 🔴🟢🔵 emojis make tracking progress easy in the output.\n\n## The Test Writer Agent (RED Phase)\n\nAt `.claude/agents/tdd-test-writer.md`:\n\n```markdown\n---\nname: tdd-test-writer\ndescription: Write failing integration tests for TDD RED phase. Use when implementing new features with TDD. Returns only after verifying test FAILS.\ntools: Read, Glob, Grep, Write, Edit, Bash\nskills: vue-integration-testing\n---\n\n# TDD Test Writer (RED Phase)\n\nWrite a failing integration test that verifies the requested feature behavior.\n\n## Process\n\n1. Understand the feature requirement from the prompt\n2. Write an integration test in `src/__tests__/integration/`\n3. Run `pnpm test:unit &lt;test-file&gt;` to verify it fails\n4. Return the test file path and failure output\n\n## Test Structure\n\ntypescript\nimport { afterEach, describe, expect, it } from &#39;vitest&#39;\nimport { createTestApp } from &#39;../helpers/createTestApp&#39;\nimport { resetWorkout } from &#39;@/composables/useWorkout&#39;\nimport { resetDatabase } from &#39;../setup&#39;\n\ndescribe(&#39;Feature Name&#39;, () =&gt; {\n  afterEach(async () =&gt; {\n    resetWorkout()\n    await resetDatabase()\n    document.body.innerHTML = &#39;&#39;\n  })\n\n  it(&#39;describes the user journey&#39;, async () =&gt; {\n    const app = await createTestApp()\n\n    // Act: User interactions\n    await app.user.click(app.getByRole(&#39;button&#39;, { name: /action/i }))\n\n    // Assert: Verify outcomes\n    expect(app.router.currentRoute.value.path).toBe(&#39;/expected&#39;)\n\n    app.cleanup()\n  })\n})\n\n\n## Requirements\n\n- Test must describe user behavior, not implementation details\n- Use `createTestApp()` for full app integration\n- Use Testing Library queries (`getByRole`, `getByText`)\n- Test MUST fail when run - verify before returning\n\n## Return Format\n\nReturn:\n- Test file path\n- Failure output showing the test fails\n- Brief summary of what the test verifies\n```\n\nI limited the tools to only what&#39;s needed for writing and running tests. The `skills` field pulls in my `vue-integration-testing` skill for project-specific context. And the explicit return format ensures clean handoffs between phases.\n\n&lt;Alert type=\&quot;info\&quot; title=\&quot;About the vue-integration-testing skill\&quot;&gt;\n  This skill defines how I want tests written: using jsdom with Vue Test Utils, writing BDD-style tests that describe user behavior, and avoiding mocks wherever possible. I don&#39;t see much value in unit tests that mock everything—they often just verify implementation details rather than actual functionality. Integration tests that exercise real code paths catch more bugs.\n&lt;/Alert&gt;\n\n## The Implementer Agent (GREEN Phase)\n\nAt `.claude/agents/tdd-implementer.md`:\n\n```markdown\n---\nname: tdd-implementer\ndescription: Implement minimal code to pass failing tests for TDD GREEN phase. Write only what the test requires. Returns only after verifying test PASSES.\ntools: Read, Glob, Grep, Write, Edit, Bash\n---\n\n# TDD Implementer (GREEN Phase)\n\nImplement the minimal code needed to make the failing test pass.\n\n## Process\n\n1. Read the failing test to understand what behavior it expects\n2. Identify the files that need changes\n3. Write the minimal implementation to pass the test\n4. Run `pnpm test:unit &lt;test-file&gt;` to verify it passes\n5. Return implementation summary and success output\n\n## Principles\n\n- **Minimal**: Write only what the test requires\n- **No extras**: No additional features, no \&quot;nice to haves\&quot;\n- **Test-driven**: If the test passes, the implementation is complete\n- **Fix implementation, not tests**: If the test fails, fix your code\n\n## Return Format\n\nReturn:\n- Files modified with brief description of changes\n- Test success output\n- Summary of the implementation\n```\n\n## The Refactorer Agent (REFACTOR Phase)\n\nAt `.claude/agents/tdd-refactorer.md`:\n\n```markdown\n---\nname: tdd-refactorer\ndescription: Evaluate and refactor code after TDD GREEN phase. Improve code quality while keeping tests passing. Returns evaluation with changes made or \&quot;no refactoring needed\&quot; with reasoning.\ntools: Read, Glob, Grep, Write, Edit, Bash\nskills: vue-composables\n---\n\n# TDD Refactorer (REFACTOR Phase)\n\nEvaluate the implementation for refactoring opportunities and apply improvements while keeping tests green.\n\n## Process\n\n1. Read the implementation and test files\n2. Evaluate against refactoring checklist\n3. Apply improvements if beneficial\n4. Run `pnpm test:unit &lt;test-file&gt;` to verify tests still pass\n5. Return summary of changes or \&quot;no refactoring needed\&quot;\n\n## Refactoring Checklist\n\nEvaluate these opportunities:\n\n- **Extract composable**: Reusable logic that could benefit other components\n- **Simplify conditionals**: Complex if/else chains that could be clearer\n- **Improve naming**: Variables or functions with unclear names\n- **Remove duplication**: Repeated code patterns\n- **Thin components**: Business logic that should move to composables\n\n## Decision Criteria\n\nRefactor when:\n- Code has clear duplication\n- Logic is reusable elsewhere\n- Naming obscures intent\n- Component contains business logic\n\nSkip refactoring when:\n- Code is already clean and simple\n- Changes would be over-engineering\n- Implementation is minimal and focused\n\n## Return Format\n\nIf changes made:\n- Files modified with brief description\n- Test success output confirming tests pass\n- Summary of improvements\n\nIf no changes:\n- \&quot;No refactoring needed\&quot;\n- Brief reasoning (e.g., \&quot;Implementation is minimal and focused\&quot;)\n```\n\nThis agent has a **decision framework** for whether to refactor. Sometimes \&quot;no refactoring needed\&quot; is the right answer. The `skills` field references my `vue-composables` skill so it knows my project&#39;s patterns for extracting reusable logic.\n\n## Real Example: Adding Workout Detail View\n\nHere&#39;s what this looks like in practice. My request:\n\n&gt; \&quot;When a user is on the Workouts page, they should be able to click on a past workout and see a detail view of what exercises and sets they completed.\&quot;\n\nThe workflow executes like this:\n\n```mermaid\nsequenceDiagram\n    participant U as User\n    participant S as TDD Skill\n    participant TW as Test Writer\n    participant I as Implementer\n    participant R as Refactorer\n\n    U-&gt;&gt;S: \&quot;Add workout detail view\&quot;\n    S-&gt;&gt;TW: Feature requirement\n    TW-&gt;&gt;TW: Write test\n    TW-&gt;&gt;TW: Run test\n    TW--&gt;&gt;S: ❌ Test fails\n    S-&gt;&gt;I: Test file path\n    I-&gt;&gt;I: Write minimal code\n    I-&gt;&gt;I: Run test\n    I--&gt;&gt;S: ✅ Test passes\n    S-&gt;&gt;R: Implementation files\n    R-&gt;&gt;R: Evaluate code\n    R-&gt;&gt;R: Extract composable\n    R-&gt;&gt;R: Run test\n    R--&gt;&gt;S: ✅ Improvements applied\n    S--&gt;&gt;U: 🔴→🟢→🔵 Complete\n```\n\n### 🔴 RED Phase\n\nThe `tdd-test-writer` produced:\n\n```typescript\n// src/__tests__/integration/workout-detail.spec.ts\nimport { afterEach, describe, expect, it } from &#39;vitest&#39;\nimport { createTestApp } from &#39;../helpers/createTestApp&#39;\nimport { db, generateId } from &#39;@/db&#39;\n\ndescribe(&#39;Workout History Detail View&#39;, () =&gt; {\n  afterEach(async () =&gt; {\n    // cleanup\n  })\n\n  it(&#39;navigates to detail view when clicking a completed workout&#39;, async () =&gt; {\n    // Arrange: Create a completed workout\n    const completedWorkout = {\n      id: generateId(),\n      name: &#39;Push Day&#39;,\n      exercises: [{\n        name: &#39;Bench Press&#39;,\n        sets: [{ kg: &#39;100&#39;, reps: &#39;10&#39; }]\n      }],\n      completedAt: Date.now(),\n    }\n    await db.workouts.add(completedWorkout)\n\n    // Act: Navigate and click\n    const app = await createTestApp()\n    await app.user.click(app.getByRole(&#39;button&#39;, { name: /workouts/i }))\n    await app.user.click(await app.findByText(&#39;Push Day&#39;))\n\n    // Assert\n    expect(app.router.currentRoute.value.path)\n      .toBe(`/workouts/${completedWorkout.id}`)\n    expect(app.getByText(&#39;Bench Press&#39;)).toBeDefined()\n    expect(app.getByText(&#39;100&#39;)).toBeDefined()\n\n    app.cleanup()\n  })\n})\n```\n\nThe test failed:\n```\nAssertionError: expected &#39;/workouts&#39; to be &#39;/workouts/d747077d-...&#39;\n```\n\nExactly what I wanted—a clear failure pointing to missing functionality.\n\n### 🟢 GREEN Phase\n\nThe `tdd-implementer` created:\n* `WorkoutDetailView.vue` — New detail view component\n* Modified `TheWorkoutsView.vue` — Added click handlers\n* Modified `router/index.ts` — Added `/workouts/:id` route\n\nTest passed. Minimal implementation, just enough to satisfy the assertions.\n\n### 🔵 REFACTOR Phase\n\nThe `tdd-refactorer` evaluated the code and made improvements:\n* **Extracted &lt;InternalLink slug=\&quot;how-to-test-vue-composables\&quot;&gt;`useWorkoutDetail` composable&lt;/InternalLink&gt;** — Reusable data fetching with discriminated union states\n* **Created shared formatters** — Pulled `formatDuration` and `formatDate` into `lib/formatters.ts`\n* **Added accessibility** — Keyboard navigation for clickable cards\n\nAll tests still passed. The cycle completed.\n\n## The Test Helper\n\nA crucial piece making all this work is my `createTestApp()` helper:\n\n```typescript\n// src/__tests__/helpers/createTestApp.ts\nexport async function createTestApp(): Promise&lt;TestApp&gt; {\n  const pinia = createPinia()\n  const router = createRouter({\n    history: createMemoryHistory(),\n    routes,\n  })\n\n  render(App, {\n    global: { plugins: [router, pinia] },\n  })\n\n  await router.isReady()\n\n  return {\n    router,\n    user: userEvent.setup(),\n    getByRole: screen.getByRole,\n    getByText: screen.getByText,\n    findByText: screen.findByText,\n    waitForRoute: (pattern) =&gt; waitFor(() =&gt; {\n      if (!pattern.test(router.currentRoute.value.path)) {\n        throw new Error(&#39;Route mismatch&#39;)\n      }\n    }),\n    cleanup: () =&gt; { document.body.innerHTML = &#39;&#39; },\n  }\n}\n```\n\nThis gives agents a consistent API for rendering the full app and simulating user interactions. They don&#39;t need to figure out how to set up Vue, Pinia, and Vue Router each time—they just call `createTestApp()` and start writing assertions.\n\n## Hooks for Consistent Skill Activation\n\n&lt;Figure src={hooksOverview} alt=\&quot;Claude Code hooks lifecycle diagram showing UserPromptSubmit hook injection\&quot; caption=\&quot;Hooks inject instructions at specific lifecycle points in Claude Code\&quot; /&gt;\n\nEven with well-written skills, Claude sometimes skipped evaluation and jumped straight to implementation. I tracked this informally—skill activation happened maybe 20% of the time.\n\nI found a great solution in [Scott Spence&#39;s post on making skills activate reliably](https://scottspence.com/posts/how-to-make-claude-code-skills-activate-reliably). He tested 200+ prompts across different hook configurations and found that a \&quot;forced eval\&quot; approach—making Claude explicitly evaluate each skill before proceeding—jumped activation from ~20% to ~84%.\n\nThe fix: **&lt;InternalLink slug=\&quot;claude-code-notification-hooks\&quot;&gt;hooks&lt;/InternalLink&gt;**. Claude Code runs hooks at specific lifecycle points, and I used `UserPromptSubmit` to inject a reminder before every response.\n\nIn `.claude/settings.json`:\n\n```json\n{\n  \&quot;hooks\&quot;: {\n    \&quot;UserPromptSubmit\&quot;: [\n      {\n        \&quot;matcher\&quot;: \&quot;\&quot;,\n        \&quot;hooks\&quot;: [\n          {\n            \&quot;type\&quot;: \&quot;command\&quot;,\n            \&quot;command\&quot;: \&quot;npx tsx \\\&quot;$CLAUDE_PROJECT_DIR/.claude/hooks/user-prompt-skill-eval.ts\\\&quot;\&quot;,\n            \&quot;timeout\&quot;: 5\n          }\n        ]\n      }\n    ]\n  }\n}\n```\n\nThe hook script at `.claude/hooks/user-prompt-skill-eval.ts`:\n\n```typescript\n#!/usr/bin/env npx tsx\nimport { readFileSync } from &#39;node:fs&#39;\nimport { stdout } from &#39;node:process&#39;\n\nfunction main(): void {\n  readFileSync(0, &#39;utf-8&#39;) // consume stdin\n\n  const instruction = `\nINSTRUCTION: MANDATORY SKILL ACTIVATION SEQUENCE\n\nStep 1 - EVALUATE:\nFor each skill in &lt;available_skills&gt;, state: [skill-name] - YES/NO - [reason]\n\nStep 2 - ACTIVATE:\nIF any skills are YES → Use Skill(skill-name) tool for EACH relevant skill NOW\nIF no skills are YES → State \&quot;No skills needed\&quot; and proceed\n\nStep 3 - IMPLEMENT:\nOnly after Step 2 is complete, proceed with implementation.\n\nCRITICAL: You MUST call Skill() tool in Step 2. Do NOT skip to implementation.\n`\n\n  stdout.write(instruction.trim())\n}\n\nmain()\n```\n\n&lt;Alert type=\&quot;important\&quot; title=\&quot;Results\&quot;&gt;\n  With this hook, skill activation jumped from ~20% to ~84%. Now when I say \&quot;implement the workout detail view,\&quot; the TDD skill triggers automatically.\n&lt;/Alert&gt;\n\n## Conclusion\n\nClaude Code&#39;s default behavior produces implementation-first code with minimal test coverage. Without constraints, it optimizes for \&quot;working code\&quot; rather than \&quot;tested code.\&quot;\n\nThe system described here addresses this through architectural separation:\n\n* **Hooks** inject evaluation logic before every prompt, increasing skill activation from ~20% to ~84%\n* **Skills** define explicit phase gates that block progression until each TDD step completes\n* **Subagents** enforce context isolation—the test writer cannot see implementation plans, so tests reflect actual requirements rather than anticipated code structure\n\nThe setup cost is ~2 hours of configuration. After that, each feature request automatically follows the Red-Green-Refactor cycle without manual enforcement.&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PostCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus-outline inline-flex items-center gap-1.5 rounded-md border border-skin-line bg-skin-card px-2.5 py-1.5 text-xs font-medium text-skin-base opacity-80 transition-all hover:border-skin-accent/50 hover:text-skin-accent hover:opacity-100" aria-label="Copy post as markdown" title="Copy post as markdown for AI/LLM"><svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg><span>Copy Post</span></button><!--astro:end--></astro-island> </div>  <article id="article" class="prose mx-auto mt-8 max-w-5xl astro-vj4tpspi"> <figure class=" mx-auto "> <img src="/_astro/tddOverviewClaudeCode.CrmhZqEd_R4rn7.webp" alt="TDD workflow overview with Claude Code showing Red-Green-Refactor cycle" loading="lazy" decoding="async" fetchpriority="auto" width="1024" height="559" class="w-full"> <figcaption class="mt-2 text-center text-sm text-gray-500"> Custom TDD workflow with Claude Code: Skills orchestrate subagents through the Red-Green-Refactor cycle </figcaption> </figure>
<p>I rely on Claude Code, but it has a structural limitation: it defaults to implementation-first. It writes the “Happy Path,” ignoring edge cases. When I try to force TDD in a single context window, the implementation “bleeds” into the test logic (context pollution). This article documents a multi-agent system using Claude’s “Skills” and “Hooks” that enforces a strict Red-Green-Refactor cycle.</p>
<div class="alert alert-note astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">💡</span> Framework Agnostic </p> <div class="alert-content astro-7kdbuayl"> <p>While this article uses Vue as an example, the TDD principles and Claude Code workflow apply to any technology. Whether you’re working with React, Angular, Svelte, or even backend languages like Python, Go, or Rust—the Red-Green-Refactor cycle and subagent orchestration work the same way.</p> </div> </div> 
<h2 id="the-problem-with-ai-assisted-tdd">The Problem with AI-Assisted TDD<a class="heading-link" aria-label="Link to section" href="#the-problem-with-ai-assisted-tdd"><span class="heading-link-icon">#</span></a></h2>
<p>When I ask Claude to “implement feature X,” it writes the implementation first. Every time. TDD flips this—you write the test first, watch it fail, then write minimal code to make it pass.</p>
<p>I needed a way to:</p>
<ul>
<li><strong>Force test-first</strong> — No implementation before a failing test exists</li>
<li><strong>Keep phases focused</strong> — The test writer shouldn’t think about implementation details</li>
<li><strong>Ensure refactoring happens</strong> — Easy to skip when the feature already works</li>
</ul>
<h2 id="skills--subagents">Skills + Subagents<a class="heading-link" aria-label="Link to section" href="#skills--subagents"><span class="heading-link-icon">#</span></a></h2>
<p>Claude Code supports two features I hadn’t explored until recently:</p>
<ul>
<li><strong><span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/understanding-claude-code-full-stack/" class="internal-link astro-3tyn5ojg"> Skills </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Understanding Claude Code&#39;s Full Stack: MCP, Skills, Subagents, and Hooks Explained</span> <span class="preview-description astro-3tyn5ojg">A practical guide to Claude Code&#39;s features — explained in the order they were introduced: MCP (2024), Claude Code core (Feb 2025), Plugins (2025), and Agent Skills (Oct 2025). What each does, how they fit together, and when to use what.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">claude-code</span><span class="preview-tag astro-3tyn5ojg">ai</span><span class="preview-tag astro-3tyn5ojg">mcp</span> <span class="preview-tag-more astro-3tyn5ojg">+2</span> </span> <time class="preview-date astro-3tyn5ojg">Nov 9, 2025</time> </span> </span> </span>  <script>
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
</script></strong> (<code>.claude/skills/</code>): High-level workflows that orchestrate complex tasks</li>
<li><strong>Agents</strong> (<code>.claude/agents/</code>): Specialized workers that handle specific jobs</li>
</ul>
<p>You might wonder: why use subagents at all? Skills alone could handle the TDD workflow. But there’s a catch—context pollution.</p>
<h3 id="the-context-pollution-problem">The Context Pollution Problem<a class="heading-link" aria-label="Link to section" href="#the-context-pollution-problem"><span class="heading-link-icon">#</span></a></h3>
<div class="alert alert-warning astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">⚠️</span> Why Single-Context LLMs Cheat at TDD </p> <div class="alert-content astro-7kdbuayl"> <p>When everything runs in one context window, <strong>the LLM cannot truly follow TDD</strong>. The test writer’s detailed analysis bleeds into the implementer’s thinking. The implementer’s code exploration pollutes the refactorer’s evaluation. Each phase drags along baggage from the others.</p><p>This isn’t just messy—it fundamentally breaks TDD. The whole point of writing the test first is that <strong>you don’t know the implementation yet</strong>. But if the same context sees both phases, the LLM subconsciously designs tests around the implementation it’s already planning. It “cheats” without meaning to.</p> </div> </div> 
<figure class=" mx-auto "> <img src="/_astro/contextProblem.BUonOKg9_1VCPjA.webp" alt="Context pollution problem when running all TDD phases in a single context" loading="lazy" decoding="async" fetchpriority="auto" width="1024" height="547" class="w-full"> <figcaption class="mt-2 text-center text-sm text-gray-500"> Without subagents, each phase pollutes the context with irrelevant details from previous phases </figcaption> </figure>
<p><strong>Subagents solve this architectural limitation.</strong> Each phase runs in complete isolation:</p>
<ul>
<li>The <strong>test writer</strong> focuses purely on test design—it has no idea how the feature will be implemented</li>
<li>The <strong>implementer</strong> sees only the failing test—it can’t be influenced by test-writing decisions</li>
<li>The <strong>refactorer</strong> evaluates clean implementation code—it starts fresh without implementation baggage</li>
</ul>
<p>Each agent starts with exactly the context it needs and nothing more. This isn’t just organization—it’s the only way to get genuine test-first development from an LLM.</p>
<p>Combining skills with subagents gave me exactly what I needed:</p>
<figure class=" mx-auto "> <img src="/_astro/claudeCodeSKill.Daqc3k4g_Z1HxfzN.webp" alt="Claude Code skill structure showing how skills orchestrate subagents" loading="lazy" decoding="async" fetchpriority="auto" width="1024" height="547" class="w-full"> <figcaption class="mt-2 text-center text-sm text-gray-500"> Skills define high-level workflows that coordinate specialized subagents </figcaption> </figure>
<h2 id="the-tdd-skill">The TDD Skill<a class="heading-link" aria-label="Link to section" href="#the-tdd-skill"><span class="heading-link-icon">#</span></a></h2>
<p>The orchestrating skill lives at <code>.claude/skills/tdd-integration/skill.md</code>:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"><span style="color:#F7768E">name</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> tdd-integration</span></span>
<span class="line"><span style="color:#F7768E">description</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Enforce Test-Driven Development with strict Red-Green-Refactor cycle using integration tests. Auto-triggers when implementing new features or functionality. Trigger phrases include &quot;implement&quot;, &quot;add feature&quot;, &quot;build&quot;, &quot;create functionality&quot;, or any request to add new behavior. Does NOT trigger for bug fixes, documentation, or configuration changes.</span></span>
<span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF;font-weight:bold">#</span><span style="color:#89DDFF;font-weight:bold"> TDD Integration Testing</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Enforce strict Test-Driven Development using the Red-Green-Refactor cycle with dedicated subagents.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Mandatory Workflow</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Every new feature MUST follow this strict 3-phase cycle. Do NOT skip phases.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Phase 1: RED - Write Failing Test</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">🔴 RED PHASE: Delegating to tdd-test-writer...</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Invoke the </span><span style="color:#89DDFF">`tdd-test-writer`</span><span style="color:#9AA5CE"> subagent with:</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Feature requirement from user request</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Expected behavior to test</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">The subagent returns:</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Test file path</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Failure output confirming test fails</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Summary of what the test verifies</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**Do NOT proceed to Green phase until test failure is confirmed.**</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Phase 2: GREEN - Make It Pass</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">🟢 GREEN PHASE: Delegating to tdd-implementer...</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Invoke the </span><span style="color:#89DDFF">`tdd-implementer`</span><span style="color:#9AA5CE"> subagent with:</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Test file path from RED phase</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Feature requirement context</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">The subagent returns:</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Files modified</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Success output confirming test passes</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Implementation summary</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**Do NOT proceed to Refactor phase until test passes.**</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Phase 3: REFACTOR - Improve</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">🔵 REFACTOR PHASE: Delegating to tdd-refactorer...</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Invoke the </span><span style="color:#89DDFF">`tdd-refactorer`</span><span style="color:#9AA5CE"> subagent with:</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Test file path</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Implementation files from GREEN phase</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">The subagent returns either:</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Changes made + test success output, OR</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> &quot;No refactoring needed&quot; with reasoning</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**Cycle complete when refactor phase returns.**</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Multiple Features</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Complete the full cycle for EACH feature before starting the next:</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Feature 1: 🔴 → 🟢 → 🔵 ✓</span></span>
<span class="line"><span style="color:#9AA5CE">Feature 2: 🔴 → 🟢 → 🔵 ✓</span></span>
<span class="line"><span style="color:#9AA5CE">Feature 3: 🔴 → 🟢 → 🔵 ✓</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Phase Violations</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Never:</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Write implementation before the test</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Proceed to Green without seeing Red fail</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Skip Refactor evaluation</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Start a new feature before completing the current cycle</span></span></code><button type="button" class="copy" data-code="---
name: tdd-integration
description: Enforce Test-Driven Development with strict Red-Green-Refactor cycle using integration tests. Auto-triggers when implementing new features or functionality. Trigger phrases include &#34;implement&#34;, &#34;add feature&#34;, &#34;build&#34;, &#34;create functionality&#34;, or any request to add new behavior. Does NOT trigger for bug fixes, documentation, or configuration changes.
---

# TDD Integration Testing

Enforce strict Test-Driven Development using the Red-Green-Refactor cycle with dedicated subagents.

## Mandatory Workflow

Every new feature MUST follow this strict 3-phase cycle. Do NOT skip phases.

### Phase 1: RED - Write Failing Test

🔴 RED PHASE: Delegating to tdd-test-writer...

Invoke the `tdd-test-writer` subagent with:
- Feature requirement from user request
- Expected behavior to test

The subagent returns:
- Test file path
- Failure output confirming test fails
- Summary of what the test verifies

**Do NOT proceed to Green phase until test failure is confirmed.**

### Phase 2: GREEN - Make It Pass

🟢 GREEN PHASE: Delegating to tdd-implementer...

Invoke the `tdd-implementer` subagent with:
- Test file path from RED phase
- Feature requirement context

The subagent returns:
- Files modified
- Success output confirming test passes
- Implementation summary

**Do NOT proceed to Refactor phase until test passes.**

### Phase 3: REFACTOR - Improve

🔵 REFACTOR PHASE: Delegating to tdd-refactorer...

Invoke the `tdd-refactorer` subagent with:
- Test file path
- Implementation files from GREEN phase

The subagent returns either:
- Changes made + test success output, OR
- &#34;No refactoring needed&#34; with reasoning

**Cycle complete when refactor phase returns.**

## Multiple Features

Complete the full cycle for EACH feature before starting the next:

Feature 1: 🔴 → 🟢 → 🔵 ✓
Feature 2: 🔴 → 🟢 → 🔵 ✓
Feature 3: 🔴 → 🟢 → 🔵 ✓

## Phase Violations

Never:
- Write implementation before the test
- Proceed to Green without seeing Red fail
- Skip Refactor evaluation
- Start a new feature before completing the current cycle" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>The <code>description</code> field contains trigger phrases so Claude activates this skill automatically when I ask to implement something. Each phase has explicit “Do NOT proceed until…” gates—Claude needs clear boundaries. The 🔴🟢🔵 emojis make tracking progress easy in the output.</p>
<h2 id="the-test-writer-agent-red-phase">The Test Writer Agent (RED Phase)<a class="heading-link" aria-label="Link to section" href="#the-test-writer-agent-red-phase"><span class="heading-link-icon">#</span></a></h2>
<p>At <code>.claude/agents/tdd-test-writer.md</code>:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"><span style="color:#F7768E">name</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> tdd-test-writer</span></span>
<span class="line"><span style="color:#F7768E">description</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Write failing integration tests for TDD RED phase. Use when implementing new features with TDD. Returns only after verifying test FAILS.</span></span>
<span class="line"><span style="color:#F7768E">tools</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Read, Glob, Grep, Write, Edit, Bash</span></span>
<span class="line"><span style="color:#F7768E">skills</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> vue-integration-testing</span></span>
<span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF;font-weight:bold">#</span><span style="color:#89DDFF;font-weight:bold"> TDD Test Writer (RED Phase)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Write a failing integration test that verifies the requested feature behavior.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Process</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">1.</span><span style="color:#9AA5CE"> Understand the feature requirement from the prompt</span></span>
<span class="line"><span style="color:#89DDFF">2.</span><span style="color:#9AA5CE"> Write an integration test in </span><span style="color:#89DDFF">`src/__tests__/integration/`</span></span>
<span class="line"><span style="color:#89DDFF">3.</span><span style="color:#9AA5CE"> Run </span><span style="color:#89DDFF">`pnpm test:unit &lt;test-file&gt;`</span><span style="color:#9AA5CE"> to verify it fails</span></span>
<span class="line"><span style="color:#89DDFF">4.</span><span style="color:#9AA5CE"> Return the test file path and failure output</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Test Structure</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">typescript</span></span>
<span class="line"><span style="color:#9AA5CE">import { afterEach, describe, expect, it } from &#39;vitest&#39;</span></span>
<span class="line"><span style="color:#9AA5CE">import { createTestApp } from &#39;../helpers/createTestApp&#39;</span></span>
<span class="line"><span style="color:#9AA5CE">import { resetWorkout } from &#39;@/composables/useWorkout&#39;</span></span>
<span class="line"><span style="color:#9AA5CE">import { resetDatabase } from &#39;../setup&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">describe(&#39;Feature Name&#39;, () =&gt; {</span></span>
<span class="line"><span style="color:#9AA5CE">  afterEach(async () =&gt; {</span></span>
<span class="line"><span style="color:#9AA5CE">    resetWorkout()</span></span>
<span class="line"><span style="color:#9AA5CE">    await resetDatabase()</span></span>
<span class="line"><span style="color:#9AA5CE">    document.body.innerHTML = &#39;&#39;</span></span>
<span class="line"><span style="color:#9AA5CE">  })</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">  it(&#39;describes the user journey&#39;, async () =&gt; {</span></span>
<span class="line"><span style="color:#9AA5CE">    const app = await createTestApp()</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">    // Act: User interactions</span></span>
<span class="line"><span style="color:#9AA5CE">    await app.user.click(app.getByRole(&#39;button&#39;, { name: /action/i }))</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">    // Assert: Verify outcomes</span></span>
<span class="line"><span style="color:#9AA5CE">    expect(app.router.currentRoute.value.path).toBe(&#39;/expected&#39;)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">    app.cleanup()</span></span>
<span class="line"><span style="color:#9AA5CE">  })</span></span>
<span class="line"><span style="color:#9AA5CE">})</span></span>
<span class="line"></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Requirements</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Test must describe user behavior, not implementation details</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Use </span><span style="color:#89DDFF">`createTestApp()`</span><span style="color:#9AA5CE"> for full app integration</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Use Testing Library queries (</span><span style="color:#89DDFF">`getByRole`</span><span style="color:#9AA5CE">, </span><span style="color:#89DDFF">`getByText`</span><span style="color:#9AA5CE">)</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Test MUST fail when run - verify before returning</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Return Format</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Return:</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Test file path</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Failure output showing the test fails</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Brief summary of what the test verifies</span></span></code><button type="button" class="copy" data-code="---
name: tdd-test-writer
description: Write failing integration tests for TDD RED phase. Use when implementing new features with TDD. Returns only after verifying test FAILS.
tools: Read, Glob, Grep, Write, Edit, Bash
skills: vue-integration-testing
---

# TDD Test Writer (RED Phase)

Write a failing integration test that verifies the requested feature behavior.

## Process

1. Understand the feature requirement from the prompt
2. Write an integration test in `src/__tests__/integration/`
3. Run `pnpm test:unit <test-file>` to verify it fails
4. Return the test file path and failure output

## Test Structure

typescript
import { afterEach, describe, expect, it } from 'vitest'
import { createTestApp } from '../helpers/createTestApp'
import { resetWorkout } from '@/composables/useWorkout'
import { resetDatabase } from '../setup'

describe('Feature Name', () => {
  afterEach(async () => {
    resetWorkout()
    await resetDatabase()
    document.body.innerHTML = ''
  })

  it('describes the user journey', async () => {
    const app = await createTestApp()

    // Act: User interactions
    await app.user.click(app.getByRole('button', { name: /action/i }))

    // Assert: Verify outcomes
    expect(app.router.currentRoute.value.path).toBe('/expected')

    app.cleanup()
  })
})


## Requirements

- Test must describe user behavior, not implementation details
- Use `createTestApp()` for full app integration
- Use Testing Library queries (`getByRole`, `getByText`)
- Test MUST fail when run - verify before returning

## Return Format

Return:
- Test file path
- Failure output showing the test fails
- Brief summary of what the test verifies" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>I limited the tools to only what’s needed for writing and running tests. The <code>skills</code> field pulls in my <code>vue-integration-testing</code> skill for project-specific context. And the explicit return format ensures clean handoffs between phases.</p>
<div class="alert alert-info astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl"></span> About the vue-integration-testing skill </p> <div class="alert-content astro-7kdbuayl"> <p>This skill defines how I want tests written: using jsdom with Vue Test Utils, writing BDD-style tests that describe user behavior, and avoiding mocks wherever possible. I don’t see much value in unit tests that mock everything—they often just verify implementation details rather than actual functionality. Integration tests that exercise real code paths catch more bugs.</p> </div> </div> 
<h2 id="the-implementer-agent-green-phase">The Implementer Agent (GREEN Phase)<a class="heading-link" aria-label="Link to section" href="#the-implementer-agent-green-phase"><span class="heading-link-icon">#</span></a></h2>
<p>At <code>.claude/agents/tdd-implementer.md</code>:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"><span style="color:#F7768E">name</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> tdd-implementer</span></span>
<span class="line"><span style="color:#F7768E">description</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Implement minimal code to pass failing tests for TDD GREEN phase. Write only what the test requires. Returns only after verifying test PASSES.</span></span>
<span class="line"><span style="color:#F7768E">tools</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Read, Glob, Grep, Write, Edit, Bash</span></span>
<span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF;font-weight:bold">#</span><span style="color:#89DDFF;font-weight:bold"> TDD Implementer (GREEN Phase)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Implement the minimal code needed to make the failing test pass.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Process</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">1.</span><span style="color:#9AA5CE"> Read the failing test to understand what behavior it expects</span></span>
<span class="line"><span style="color:#89DDFF">2.</span><span style="color:#9AA5CE"> Identify the files that need changes</span></span>
<span class="line"><span style="color:#89DDFF">3.</span><span style="color:#9AA5CE"> Write the minimal implementation to pass the test</span></span>
<span class="line"><span style="color:#89DDFF">4.</span><span style="color:#9AA5CE"> Run </span><span style="color:#89DDFF">`pnpm test:unit &lt;test-file&gt;`</span><span style="color:#9AA5CE"> to verify it passes</span></span>
<span class="line"><span style="color:#89DDFF">5.</span><span style="color:#9AA5CE"> Return implementation summary and success output</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Principles</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#C0CAF5;font-weight:bold"> **Minimal**</span><span style="color:#9AA5CE">: Write only what the test requires</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#C0CAF5;font-weight:bold"> **No extras**</span><span style="color:#9AA5CE">: No additional features, no &quot;nice to haves&quot;</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#C0CAF5;font-weight:bold"> **Test-driven**</span><span style="color:#9AA5CE">: If the test passes, the implementation is complete</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#C0CAF5;font-weight:bold"> **Fix implementation, not tests**</span><span style="color:#9AA5CE">: If the test fails, fix your code</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Return Format</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Return:</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Files modified with brief description of changes</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Test success output</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Summary of the implementation</span></span></code><button type="button" class="copy" data-code="---
name: tdd-implementer
description: Implement minimal code to pass failing tests for TDD GREEN phase. Write only what the test requires. Returns only after verifying test PASSES.
tools: Read, Glob, Grep, Write, Edit, Bash
---

# TDD Implementer (GREEN Phase)

Implement the minimal code needed to make the failing test pass.

## Process

1. Read the failing test to understand what behavior it expects
2. Identify the files that need changes
3. Write the minimal implementation to pass the test
4. Run `pnpm test:unit <test-file>` to verify it passes
5. Return implementation summary and success output

## Principles

- **Minimal**: Write only what the test requires
- **No extras**: No additional features, no &#34;nice to haves&#34;
- **Test-driven**: If the test passes, the implementation is complete
- **Fix implementation, not tests**: If the test fails, fix your code

## Return Format

Return:
- Files modified with brief description of changes
- Test success output
- Summary of the implementation" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h2 id="the-refactorer-agent-refactor-phase">The Refactorer Agent (REFACTOR Phase)<a class="heading-link" aria-label="Link to section" href="#the-refactorer-agent-refactor-phase"><span class="heading-link-icon">#</span></a></h2>
<p>At <code>.claude/agents/tdd-refactorer.md</code>:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"><span style="color:#F7768E">name</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> tdd-refactorer</span></span>
<span class="line"><span style="color:#F7768E">description</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Evaluate and refactor code after TDD GREEN phase. Improve code quality while keeping tests passing. Returns evaluation with changes made or &quot;no refactoring needed&quot; with reasoning.</span></span>
<span class="line"><span style="color:#F7768E">tools</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Read, Glob, Grep, Write, Edit, Bash</span></span>
<span class="line"><span style="color:#F7768E">skills</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> vue-composables</span></span>
<span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF;font-weight:bold">#</span><span style="color:#89DDFF;font-weight:bold"> TDD Refactorer (REFACTOR Phase)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Evaluate the implementation for refactoring opportunities and apply improvements while keeping tests green.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Process</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">1.</span><span style="color:#9AA5CE"> Read the implementation and test files</span></span>
<span class="line"><span style="color:#89DDFF">2.</span><span style="color:#9AA5CE"> Evaluate against refactoring checklist</span></span>
<span class="line"><span style="color:#89DDFF">3.</span><span style="color:#9AA5CE"> Apply improvements if beneficial</span></span>
<span class="line"><span style="color:#89DDFF">4.</span><span style="color:#9AA5CE"> Run </span><span style="color:#89DDFF">`pnpm test:unit &lt;test-file&gt;`</span><span style="color:#9AA5CE"> to verify tests still pass</span></span>
<span class="line"><span style="color:#89DDFF">5.</span><span style="color:#9AA5CE"> Return summary of changes or &quot;no refactoring needed&quot;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Refactoring Checklist</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Evaluate these opportunities:</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#C0CAF5;font-weight:bold"> **Extract composable**</span><span style="color:#9AA5CE">: Reusable logic that could benefit other components</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#C0CAF5;font-weight:bold"> **Simplify conditionals**</span><span style="color:#9AA5CE">: Complex if/else chains that could be clearer</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#C0CAF5;font-weight:bold"> **Improve naming**</span><span style="color:#9AA5CE">: Variables or functions with unclear names</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#C0CAF5;font-weight:bold"> **Remove duplication**</span><span style="color:#9AA5CE">: Repeated code patterns</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#C0CAF5;font-weight:bold"> **Thin components**</span><span style="color:#9AA5CE">: Business logic that should move to composables</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Decision Criteria</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Refactor when:</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Code has clear duplication</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Logic is reusable elsewhere</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Naming obscures intent</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Component contains business logic</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Skip refactoring when:</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Code is already clean and simple</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Changes would be over-engineering</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Implementation is minimal and focused</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Return Format</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">If changes made:</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Files modified with brief description</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Test success output confirming tests pass</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Summary of improvements</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">If no changes:</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> &quot;No refactoring needed&quot;</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Brief reasoning (e.g., &quot;Implementation is minimal and focused&quot;)</span></span></code><button type="button" class="copy" data-code="---
name: tdd-refactorer
description: Evaluate and refactor code after TDD GREEN phase. Improve code quality while keeping tests passing. Returns evaluation with changes made or &#34;no refactoring needed&#34; with reasoning.
tools: Read, Glob, Grep, Write, Edit, Bash
skills: vue-composables
---

# TDD Refactorer (REFACTOR Phase)

Evaluate the implementation for refactoring opportunities and apply improvements while keeping tests green.

## Process

1. Read the implementation and test files
2. Evaluate against refactoring checklist
3. Apply improvements if beneficial
4. Run `pnpm test:unit <test-file>` to verify tests still pass
5. Return summary of changes or &#34;no refactoring needed&#34;

## Refactoring Checklist

Evaluate these opportunities:

- **Extract composable**: Reusable logic that could benefit other components
- **Simplify conditionals**: Complex if/else chains that could be clearer
- **Improve naming**: Variables or functions with unclear names
- **Remove duplication**: Repeated code patterns
- **Thin components**: Business logic that should move to composables

## Decision Criteria

Refactor when:
- Code has clear duplication
- Logic is reusable elsewhere
- Naming obscures intent
- Component contains business logic

Skip refactoring when:
- Code is already clean and simple
- Changes would be over-engineering
- Implementation is minimal and focused

## Return Format

If changes made:
- Files modified with brief description
- Test success output confirming tests pass
- Summary of improvements

If no changes:
- &#34;No refactoring needed&#34;
- Brief reasoning (e.g., &#34;Implementation is minimal and focused&#34;)" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>This agent has a <strong>decision framework</strong> for whether to refactor. Sometimes “no refactoring needed” is the right answer. The <code>skills</code> field references my <code>vue-composables</code> skill so it knows my project’s patterns for extracting reusable logic.</p>
<h2 id="real-example-adding-workout-detail-view">Real Example: Adding Workout Detail View<a class="heading-link" aria-label="Link to section" href="#real-example-adding-workout-detail-view"><span class="heading-link-icon">#</span></a></h2>
<p>Here’s what this looks like in practice. My request:</p>
<blockquote>
<p>“When a user is on the Workouts page, they should be able to click on a past workout and see a detail view of what exercises and sets they completed.”</p>
</blockquote>
<p>The workflow executes like this:</p>
<p><svg id="mermaid-0" width="1051" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" height="1139" viewBox="-50 -10 1051 1139" role="graphics-document document" aria-roledescription="sequence"><g><rect x="800" y="1053" fill="#eaeaea" stroke="#666" width="150" height="65" name="R" rx="3" ry="3" class="actor actor-bottom"></rect><text x="875" y="1085.5" dominant-baseline="central" alignment-baseline="central" class="actor actor-box" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="875" dy="0">Refactorer</tspan></text></g><g><rect x="600" y="1053" fill="#eaeaea" stroke="#666" width="150" height="65" name="I" rx="3" ry="3" class="actor actor-bottom"></rect><text x="675" y="1085.5" dominant-baseline="central" alignment-baseline="central" class="actor actor-box" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="675" dy="0">Implementer</tspan></text></g><g><rect x="400" y="1053" fill="#eaeaea" stroke="#666" width="150" height="65" name="TW" rx="3" ry="3" class="actor actor-bottom"></rect><text x="475" y="1085.5" dominant-baseline="central" alignment-baseline="central" class="actor actor-box" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="475" dy="0">Test Writer</tspan></text></g><g><rect x="200" y="1053" fill="#eaeaea" stroke="#666" width="150" height="65" name="S" rx="3" ry="3" class="actor actor-bottom"></rect><text x="275" y="1085.5" dominant-baseline="central" alignment-baseline="central" class="actor actor-box" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="275" dy="0">TDD Skill</tspan></text></g><g><rect x="0" y="1053" fill="#eaeaea" stroke="#666" width="150" height="65" name="U" rx="3" ry="3" class="actor actor-bottom"></rect><text x="75" y="1085.5" dominant-baseline="central" alignment-baseline="central" class="actor actor-box" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="75" dy="0">User</tspan></text></g><g><line id="actor4" x1="875" y1="65" x2="875" y2="1053" class="actor-line 200" stroke-width="0.5px" stroke="#999" name="R"></line><g id="root-4"><rect x="800" y="0" fill="#eaeaea" stroke="#666" width="150" height="65" name="R" rx="3" ry="3" class="actor actor-top"></rect><text x="875" y="32.5" dominant-baseline="central" alignment-baseline="central" class="actor actor-box" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="875" dy="0">Refactorer</tspan></text></g></g><g><line id="actor3" x1="675" y1="65" x2="675" y2="1053" class="actor-line 200" stroke-width="0.5px" stroke="#999" name="I"></line><g id="root-3"><rect x="600" y="0" fill="#eaeaea" stroke="#666" width="150" height="65" name="I" rx="3" ry="3" class="actor actor-top"></rect><text x="675" y="32.5" dominant-baseline="central" alignment-baseline="central" class="actor actor-box" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="675" dy="0">Implementer</tspan></text></g></g><g><line id="actor2" x1="475" y1="65" x2="475" y2="1053" class="actor-line 200" stroke-width="0.5px" stroke="#999" name="TW"></line><g id="root-2"><rect x="400" y="0" fill="#eaeaea" stroke="#666" width="150" height="65" name="TW" rx="3" ry="3" class="actor actor-top"></rect><text x="475" y="32.5" dominant-baseline="central" alignment-baseline="central" class="actor actor-box" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="475" dy="0">Test Writer</tspan></text></g></g><g><line id="actor1" x1="275" y1="65" x2="275" y2="1053" class="actor-line 200" stroke-width="0.5px" stroke="#999" name="S"></line><g id="root-1"><rect x="200" y="0" fill="#eaeaea" stroke="#666" width="150" height="65" name="S" rx="3" ry="3" class="actor actor-top"></rect><text x="275" y="32.5" dominant-baseline="central" alignment-baseline="central" class="actor actor-box" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="275" dy="0">TDD Skill</tspan></text></g></g><g><line id="actor0" x1="75" y1="65" x2="75" y2="1053" class="actor-line 200" stroke-width="0.5px" stroke="#999" name="U"></line><g id="root-0"><rect x="0" y="0" fill="#eaeaea" stroke="#666" width="150" height="65" name="U" rx="3" ry="3" class="actor actor-top"></rect><text x="75" y="32.5" dominant-baseline="central" alignment-baseline="central" class="actor actor-box" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="75" dy="0">User</tspan></text></g></g><style>#mermaid-0{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-0 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-0 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-0 .error-icon{fill:#a44141;}#mermaid-0 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-0 .edge-thickness-normal{stroke-width:1px;}#mermaid-0 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-0 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-0 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-0 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-0 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-0 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-0 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-0 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-0 p{margin:0;}#mermaid-0 .actor{stroke:#ccc;fill:transparent;}#mermaid-0 text.actor>tspan{fill:lightgrey;stroke:none;}#mermaid-0 .actor-line{stroke:#ccc;}#mermaid-0 .innerArc{stroke-width:1.5;stroke-dasharray:none;}#mermaid-0 .messageLine0{stroke-width:1.5;stroke-dasharray:none;stroke:lightgrey;}#mermaid-0 .messageLine1{stroke-width:1.5;stroke-dasharray:2,2;stroke:lightgrey;}#mermaid-0 #arrowhead path{fill:lightgrey;stroke:lightgrey;}#mermaid-0 .sequenceNumber{fill:black;}#mermaid-0 #sequencenumber{fill:lightgrey;}#mermaid-0 #crosshead path{fill:lightgrey;stroke:lightgrey;}#mermaid-0 .messageText{fill:lightgrey;stroke:none;}#mermaid-0 .labelBox{stroke:#ccc;fill:transparent;}#mermaid-0 .labelText,#mermaid-0 .labelText>tspan{fill:lightgrey;stroke:none;}#mermaid-0 .loopText,#mermaid-0 .loopText>tspan{fill:lightgrey;stroke:none;}#mermaid-0 .loopLine{stroke-width:2px;stroke-dasharray:2,2;stroke:#ccc;fill:#ccc;}#mermaid-0 .note{stroke:hsl(180, 0%, 18.3529411765%);fill:hsla(0, 0%, 16%, 0);}#mermaid-0 .noteText,#mermaid-0 .noteText>tspan{fill:rgb(183.8476190475, 181.5523809523, 181.5523809523);stroke:none;}#mermaid-0 .activation0{fill:hsla(0, 0%, 16%, 0);stroke:#ccc;}#mermaid-0 .activation1{fill:hsla(0, 0%, 16%, 0);stroke:#ccc;}#mermaid-0 .activation2{fill:hsla(0, 0%, 16%, 0);stroke:#ccc;}#mermaid-0 .actorPopupMenu{position:absolute;}#mermaid-0 .actorPopupMenuPanel{position:absolute;fill:transparent;box-shadow:0px 8px 16px 0px rgba(0,0,0,0.2);filter:drop-shadow(3px 5px 2px rgb(0 0 0 / 0.4));}#mermaid-0 .actor-man line{stroke:#ccc;fill:transparent;}#mermaid-0 .actor-man circle,#mermaid-0 line{stroke:#ccc;fill:transparent;stroke-width:2px;}#mermaid-0 :root{--mermaid-font-family:arial,sans-serif;}</style><g></g><defs><symbol id="computer" width="24" height="24"><path transform="scale(.5)" d="M2 2v13h20v-13h-20zm18 11h-16v-9h16v9zm-10.228 6l.466-1h3.524l.467 1h-4.457zm14.228 3h-24l2-6h2.104l-1.33 4h18.45l-1.297-4h2.073l2 6zm-5-10h-14v-7h14v7z"></path></symbol></defs><defs><symbol id="database" fill-rule="evenodd" clip-rule="evenodd"><path transform="scale(.5)" d="M12.258.001l.256.004.255.005.253.008.251.01.249.012.247.015.246.016.242.019.241.02.239.023.236.024.233.027.231.028.229.031.225.032.223.034.22.036.217.038.214.04.211.041.208.043.205.045.201.046.198.048.194.05.191.051.187.053.183.054.18.056.175.057.172.059.168.06.163.061.16.063.155.064.15.066.074.033.073.033.071.034.07.034.069.035.068.035.067.035.066.035.064.036.064.036.062.036.06.036.06.037.058.037.058.037.055.038.055.038.053.038.052.038.051.039.05.039.048.039.047.039.045.04.044.04.043.04.041.04.04.041.039.041.037.041.036.041.034.041.033.042.032.042.03.042.029.042.027.042.026.043.024.043.023.043.021.043.02.043.018.044.017.043.015.044.013.044.012.044.011.045.009.044.007.045.006.045.004.045.002.045.001.045v17l-.001.045-.002.045-.004.045-.006.045-.007.045-.009.044-.011.045-.012.044-.013.044-.015.044-.017.043-.018.044-.02.043-.021.043-.023.043-.024.043-.026.043-.027.042-.029.042-.03.042-.032.042-.033.042-.034.041-.036.041-.037.041-.039.041-.04.041-.041.04-.043.04-.044.04-.045.04-.047.039-.048.039-.05.039-.051.039-.052.038-.053.038-.055.038-.055.038-.058.037-.058.037-.06.037-.06.036-.062.036-.064.036-.064.036-.066.035-.067.035-.068.035-.069.035-.07.034-.071.034-.073.033-.074.033-.15.066-.155.064-.16.063-.163.061-.168.06-.172.059-.175.057-.18.056-.183.054-.187.053-.191.051-.194.05-.198.048-.201.046-.205.045-.208.043-.211.041-.214.04-.217.038-.22.036-.223.034-.225.032-.229.031-.231.028-.233.027-.236.024-.239.023-.241.02-.242.019-.246.016-.247.015-.249.012-.251.01-.253.008-.255.005-.256.004-.258.001-.258-.001-.256-.004-.255-.005-.253-.008-.251-.01-.249-.012-.247-.015-.245-.016-.243-.019-.241-.02-.238-.023-.236-.024-.234-.027-.231-.028-.228-.031-.226-.032-.223-.034-.22-.036-.217-.038-.214-.04-.211-.041-.208-.043-.204-.045-.201-.046-.198-.048-.195-.05-.19-.051-.187-.053-.184-.054-.179-.056-.176-.057-.172-.059-.167-.06-.164-.061-.159-.063-.155-.064-.151-.066-.074-.033-.072-.033-.072-.034-.07-.034-.069-.035-.068-.035-.067-.035-.066-.035-.064-.036-.063-.036-.062-.036-.061-.036-.06-.037-.058-.037-.057-.037-.056-.038-.055-.038-.053-.038-.052-.038-.051-.039-.049-.039-.049-.039-.046-.039-.046-.04-.044-.04-.043-.04-.041-.04-.04-.041-.039-.041-.037-.041-.036-.041-.034-.041-.033-.042-.032-.042-.03-.042-.029-.042-.027-.042-.026-.043-.024-.043-.023-.043-.021-.043-.02-.043-.018-.044-.017-.043-.015-.044-.013-.044-.012-.044-.011-.045-.009-.044-.007-.045-.006-.045-.004-.045-.002-.045-.001-.045v-17l.001-.045.002-.045.004-.045.006-.045.007-.045.009-.044.011-.045.012-.044.013-.044.015-.044.017-.043.018-.044.02-.043.021-.043.023-.043.024-.043.026-.043.027-.042.029-.042.03-.042.032-.042.033-.042.034-.041.036-.041.037-.041.039-.041.04-.041.041-.04.043-.04.044-.04.046-.04.046-.039.049-.039.049-.039.051-.039.052-.038.053-.038.055-.038.056-.038.057-.037.058-.037.06-.037.061-.036.062-.036.063-.036.064-.036.066-.035.067-.035.068-.035.069-.035.07-.034.072-.034.072-.033.074-.033.151-.066.155-.064.159-.063.164-.061.167-.06.172-.059.176-.057.179-.056.184-.054.187-.053.19-.051.195-.05.198-.048.201-.046.204-.045.208-.043.211-.041.214-.04.217-.038.22-.036.223-.034.226-.032.228-.031.231-.028.234-.027.236-.024.238-.023.241-.02.243-.019.245-.016.247-.015.249-.012.251-.01.253-.008.255-.005.256-.004.258-.001.258.001zm-9.258 20.499v.01l.001.021.003.021.004.022.005.021.006.022.007.022.009.023.01.022.011.023.012.023.013.023.015.023.016.024.017.023.018.024.019.024.021.024.022.025.023.024.024.025.052.049.056.05.061.051.066.051.07.051.075.051.079.052.084.052.088.052.092.052.097.052.102.051.105.052.11.052.114.051.119.051.123.051.127.05.131.05.135.05.139.048.144.049.147.047.152.047.155.047.16.045.163.045.167.043.171.043.176.041.178.041.183.039.187.039.19.037.194.035.197.035.202.033.204.031.209.03.212.029.216.027.219.025.222.024.226.021.23.02.233.018.236.016.24.015.243.012.246.01.249.008.253.005.256.004.259.001.26-.001.257-.004.254-.005.25-.008.247-.011.244-.012.241-.014.237-.016.233-.018.231-.021.226-.021.224-.024.22-.026.216-.027.212-.028.21-.031.205-.031.202-.034.198-.034.194-.036.191-.037.187-.039.183-.04.179-.04.175-.042.172-.043.168-.044.163-.045.16-.046.155-.046.152-.047.148-.048.143-.049.139-.049.136-.05.131-.05.126-.05.123-.051.118-.052.114-.051.11-.052.106-.052.101-.052.096-.052.092-.052.088-.053.083-.051.079-.052.074-.052.07-.051.065-.051.06-.051.056-.05.051-.05.023-.024.023-.025.021-.024.02-.024.019-.024.018-.024.017-.024.015-.023.014-.024.013-.023.012-.023.01-.023.01-.022.008-.022.006-.022.006-.022.004-.022.004-.021.001-.021.001-.021v-4.127l-.077.055-.08.053-.083.054-.085.053-.087.052-.09.052-.093.051-.095.05-.097.05-.1.049-.102.049-.105.048-.106.047-.109.047-.111.046-.114.045-.115.045-.118.044-.12.043-.122.042-.124.042-.126.041-.128.04-.13.04-.132.038-.134.038-.135.037-.138.037-.139.035-.142.035-.143.034-.144.033-.147.032-.148.031-.15.03-.151.03-.153.029-.154.027-.156.027-.158.026-.159.025-.161.024-.162.023-.163.022-.165.021-.166.02-.167.019-.169.018-.169.017-.171.016-.173.015-.173.014-.175.013-.175.012-.177.011-.178.01-.179.008-.179.008-.181.006-.182.005-.182.004-.184.003-.184.002h-.37l-.184-.002-.184-.003-.182-.004-.182-.005-.181-.006-.179-.008-.179-.008-.178-.01-.176-.011-.176-.012-.175-.013-.173-.014-.172-.015-.171-.016-.17-.017-.169-.018-.167-.019-.166-.02-.165-.021-.163-.022-.162-.023-.161-.024-.159-.025-.157-.026-.156-.027-.155-.027-.153-.029-.151-.03-.15-.03-.148-.031-.146-.032-.145-.033-.143-.034-.141-.035-.14-.035-.137-.037-.136-.037-.134-.038-.132-.038-.13-.04-.128-.04-.126-.041-.124-.042-.122-.042-.12-.044-.117-.043-.116-.045-.113-.045-.112-.046-.109-.047-.106-.047-.105-.048-.102-.049-.1-.049-.097-.05-.095-.05-.093-.052-.09-.051-.087-.052-.085-.053-.083-.054-.08-.054-.077-.054v4.127zm0-5.654v.011l.001.021.003.021.004.021.005.022.006.022.007.022.009.022.01.022.011.023.012.023.013.023.015.024.016.023.017.024.018.024.019.024.021.024.022.024.023.025.024.024.052.05.056.05.061.05.066.051.07.051.075.052.079.051.084.052.088.052.092.052.097.052.102.052.105.052.11.051.114.051.119.052.123.05.127.051.131.05.135.049.139.049.144.048.147.048.152.047.155.046.16.045.163.045.167.044.171.042.176.042.178.04.183.04.187.038.19.037.194.036.197.034.202.033.204.032.209.03.212.028.216.027.219.025.222.024.226.022.23.02.233.018.236.016.24.014.243.012.246.01.249.008.253.006.256.003.259.001.26-.001.257-.003.254-.006.25-.008.247-.01.244-.012.241-.015.237-.016.233-.018.231-.02.226-.022.224-.024.22-.025.216-.027.212-.029.21-.03.205-.032.202-.033.198-.035.194-.036.191-.037.187-.039.183-.039.179-.041.175-.042.172-.043.168-.044.163-.045.16-.045.155-.047.152-.047.148-.048.143-.048.139-.05.136-.049.131-.05.126-.051.123-.051.118-.051.114-.052.11-.052.106-.052.101-.052.096-.052.092-.052.088-.052.083-.052.079-.052.074-.051.07-.052.065-.051.06-.05.056-.051.051-.049.023-.025.023-.024.021-.025.02-.024.019-.024.018-.024.017-.024.015-.023.014-.023.013-.024.012-.022.01-.023.01-.023.008-.022.006-.022.006-.022.004-.021.004-.022.001-.021.001-.021v-4.139l-.077.054-.08.054-.083.054-.085.052-.087.053-.09.051-.093.051-.095.051-.097.05-.1.049-.102.049-.105.048-.106.047-.109.047-.111.046-.114.045-.115.044-.118.044-.12.044-.122.042-.124.042-.126.041-.128.04-.13.039-.132.039-.134.038-.135.037-.138.036-.139.036-.142.035-.143.033-.144.033-.147.033-.148.031-.15.03-.151.03-.153.028-.154.028-.156.027-.158.026-.159.025-.161.024-.162.023-.163.022-.165.021-.166.02-.167.019-.169.018-.169.017-.171.016-.173.015-.173.014-.175.013-.175.012-.177.011-.178.009-.179.009-.179.007-.181.007-.182.005-.182.004-.184.003-.184.002h-.37l-.184-.002-.184-.003-.182-.004-.182-.005-.181-.007-.179-.007-.179-.009-.178-.009-.176-.011-.176-.012-.175-.013-.173-.014-.172-.015-.171-.016-.17-.017-.169-.018-.167-.019-.166-.02-.165-.021-.163-.022-.162-.023-.161-.024-.159-.025-.157-.026-.156-.027-.155-.028-.153-.028-.151-.03-.15-.03-.148-.031-.146-.033-.145-.033-.143-.033-.141-.035-.14-.036-.137-.036-.136-.037-.134-.038-.132-.039-.13-.039-.128-.04-.126-.041-.124-.042-.122-.043-.12-.043-.117-.044-.116-.044-.113-.046-.112-.046-.109-.046-.106-.047-.105-.048-.102-.049-.1-.049-.097-.05-.095-.051-.093-.051-.09-.051-.087-.053-.085-.052-.083-.054-.08-.054-.077-.054v4.139zm0-5.666v.011l.001.02.003.022.004.021.005.022.006.021.007.022.009.023.01.022.011.023.012.023.013.023.015.023.016.024.017.024.018.023.019.024.021.025.022.024.023.024.024.025.052.05.056.05.061.05.066.051.07.051.075.052.079.051.084.052.088.052.092.052.097.052.102.052.105.051.11.052.114.051.119.051.123.051.127.05.131.05.135.05.139.049.144.048.147.048.152.047.155.046.16.045.163.045.167.043.171.043.176.042.178.04.183.04.187.038.19.037.194.036.197.034.202.033.204.032.209.03.212.028.216.027.219.025.222.024.226.021.23.02.233.018.236.017.24.014.243.012.246.01.249.008.253.006.256.003.259.001.26-.001.257-.003.254-.006.25-.008.247-.01.244-.013.241-.014.237-.016.233-.018.231-.02.226-.022.224-.024.22-.025.216-.027.212-.029.21-.03.205-.032.202-.033.198-.035.194-.036.191-.037.187-.039.183-.039.179-.041.175-.042.172-.043.168-.044.163-.045.16-.045.155-.047.152-.047.148-.048.143-.049.139-.049.136-.049.131-.051.126-.05.123-.051.118-.052.114-.051.11-.052.106-.052.101-.052.096-.052.092-.052.088-.052.083-.052.079-.052.074-.052.07-.051.065-.051.06-.051.056-.05.051-.049.023-.025.023-.025.021-.024.02-.024.019-.024.018-.024.017-.024.015-.023.014-.024.013-.023.012-.023.01-.022.01-.023.008-.022.006-.022.006-.022.004-.022.004-.021.001-.021.001-.021v-4.153l-.077.054-.08.054-.083.053-.085.053-.087.053-.09.051-.093.051-.095.051-.097.05-.1.049-.102.048-.105.048-.106.048-.109.046-.111.046-.114.046-.115.044-.118.044-.12.043-.122.043-.124.042-.126.041-.128.04-.13.039-.132.039-.134.038-.135.037-.138.036-.139.036-.142.034-.143.034-.144.033-.147.032-.148.032-.15.03-.151.03-.153.028-.154.028-.156.027-.158.026-.159.024-.161.024-.162.023-.163.023-.165.021-.166.02-.167.019-.169.018-.169.017-.171.016-.173.015-.173.014-.175.013-.175.012-.177.01-.178.01-.179.009-.179.007-.181.006-.182.006-.182.004-.184.003-.184.001-.185.001-.185-.001-.184-.001-.184-.003-.182-.004-.182-.006-.181-.006-.179-.007-.179-.009-.178-.01-.176-.01-.176-.012-.175-.013-.173-.014-.172-.015-.171-.016-.17-.017-.169-.018-.167-.019-.166-.02-.165-.021-.163-.023-.162-.023-.161-.024-.159-.024-.157-.026-.156-.027-.155-.028-.153-.028-.151-.03-.15-.03-.148-.032-.146-.032-.145-.033-.143-.034-.141-.034-.14-.036-.137-.036-.136-.037-.134-.038-.132-.039-.13-.039-.128-.041-.126-.041-.124-.041-.122-.043-.12-.043-.117-.044-.116-.044-.113-.046-.112-.046-.109-.046-.106-.048-.105-.048-.102-.048-.1-.05-.097-.049-.095-.051-.093-.051-.09-.052-.087-.052-.085-.053-.083-.053-.08-.054-.077-.054v4.153zm8.74-8.179l-.257.004-.254.005-.25.008-.247.011-.244.012-.241.014-.237.016-.233.018-.231.021-.226.022-.224.023-.22.026-.216.027-.212.028-.21.031-.205.032-.202.033-.198.034-.194.036-.191.038-.187.038-.183.04-.179.041-.175.042-.172.043-.168.043-.163.045-.16.046-.155.046-.152.048-.148.048-.143.048-.139.049-.136.05-.131.05-.126.051-.123.051-.118.051-.114.052-.11.052-.106.052-.101.052-.096.052-.092.052-.088.052-.083.052-.079.052-.074.051-.07.052-.065.051-.06.05-.056.05-.051.05-.023.025-.023.024-.021.024-.02.025-.019.024-.018.024-.017.023-.015.024-.014.023-.013.023-.012.023-.01.023-.01.022-.008.022-.006.023-.006.021-.004.022-.004.021-.001.021-.001.021.001.021.001.021.004.021.004.022.006.021.006.023.008.022.01.022.01.023.012.023.013.023.014.023.015.024.017.023.018.024.019.024.02.025.021.024.023.024.023.025.051.05.056.05.06.05.065.051.07.052.074.051.079.052.083.052.088.052.092.052.096.052.101.052.106.052.11.052.114.052.118.051.123.051.126.051.131.05.136.05.139.049.143.048.148.048.152.048.155.046.16.046.163.045.168.043.172.043.175.042.179.041.183.04.187.038.191.038.194.036.198.034.202.033.205.032.21.031.212.028.216.027.22.026.224.023.226.022.231.021.233.018.237.016.241.014.244.012.247.011.25.008.254.005.257.004.26.001.26-.001.257-.004.254-.005.25-.008.247-.011.244-.012.241-.014.237-.016.233-.018.231-.021.226-.022.224-.023.22-.026.216-.027.212-.028.21-.031.205-.032.202-.033.198-.034.194-.036.191-.038.187-.038.183-.04.179-.041.175-.042.172-.043.168-.043.163-.045.16-.046.155-.046.152-.048.148-.048.143-.048.139-.049.136-.05.131-.05.126-.051.123-.051.118-.051.114-.052.11-.052.106-.052.101-.052.096-.052.092-.052.088-.052.083-.052.079-.052.074-.051.07-.052.065-.051.06-.05.056-.05.051-.05.023-.025.023-.024.021-.024.02-.025.019-.024.018-.024.017-.023.015-.024.014-.023.013-.023.012-.023.01-.023.01-.022.008-.022.006-.023.006-.021.004-.022.004-.021.001-.021.001-.021-.001-.021-.001-.021-.004-.021-.004-.022-.006-.021-.006-.023-.008-.022-.01-.022-.01-.023-.012-.023-.013-.023-.014-.023-.015-.024-.017-.023-.018-.024-.019-.024-.02-.025-.021-.024-.023-.024-.023-.025-.051-.05-.056-.05-.06-.05-.065-.051-.07-.052-.074-.051-.079-.052-.083-.052-.088-.052-.092-.052-.096-.052-.101-.052-.106-.052-.11-.052-.114-.052-.118-.051-.123-.051-.126-.051-.131-.05-.136-.05-.139-.049-.143-.048-.148-.048-.152-.048-.155-.046-.16-.046-.163-.045-.168-.043-.172-.043-.175-.042-.179-.041-.183-.04-.187-.038-.191-.038-.194-.036-.198-.034-.202-.033-.205-.032-.21-.031-.212-.028-.216-.027-.22-.026-.224-.023-.226-.022-.231-.021-.233-.018-.237-.016-.241-.014-.244-.012-.247-.011-.25-.008-.254-.005-.257-.004-.26-.001-.26.001z"></path></symbol></defs><defs><symbol id="clock" width="24" height="24"><path transform="scale(.5)" d="M12 2c5.514 0 10 4.486 10 10s-4.486 10-10 10-10-4.486-10-10 4.486-10 10-10zm0-2c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm5.848 12.459c.202.038.202.333.001.372-1.907.361-6.045 1.111-6.547 1.111-.719 0-1.301-.582-1.301-1.301 0-.512.77-5.447 1.125-7.445.034-.192.312-.181.343.014l.985 6.238 5.394 1.011z"></path></symbol></defs><defs><marker id="arrowhead" refX="7.9" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" orient="auto-start-reverse"><path d="M -1 0 L 10 5 L 0 10 z"></path></marker></defs><defs><marker id="crosshead" markerWidth="15" markerHeight="8" orient="auto" refX="4" refY="4.5"><path fill="none" stroke="#000000" stroke-width="1pt" d="M 1,2 L 6,7 M 6,2 L 1,7" style="stroke-dasharray:0, 0"></path></marker></defs><defs><marker id="filled-head" refX="15.5" refY="7" markerWidth="20" markerHeight="28" orient="auto"><path d="M 18,7 L9,13 L14,7 L9,1 Z"></path></marker></defs><defs><marker id="sequencenumber" refX="15" refY="15" markerWidth="60" markerHeight="40" orient="auto"><circle cx="15" cy="15" r="6"></circle></marker></defs><text x="174" y="80" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">&quot;Add workout detail view&quot;</text><line x1="76" y1="113" x2="271" y2="113" class="messageLine0" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="fill:none"></line><text x="374" y="128" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">Feature requirement</text><line x1="276" y1="161" x2="471" y2="161" class="messageLine0" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="fill:none"></line><text x="476" y="176" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">Write test</text><path d="M 476,209 C 536,199 536,239 476,229" class="messageLine0" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="fill:none"></path><text x="476" y="254" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">Run test</text><path d="M 476,287 C 536,277 536,317 476,307" class="messageLine0" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="fill:none"></path><text x="377" y="332" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">❌ Test fails</text><line x1="474" y1="365" x2="279" y2="365" class="messageLine1" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="stroke-dasharray:3, 3;fill:none"></line><text x="474" y="380" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">Test file path</text><line x1="276" y1="413" x2="671" y2="413" class="messageLine0" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="fill:none"></line><text x="676" y="428" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">Write minimal</text><text x="676" y="447" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">code</text><path d="M 676,480 C 736,470 736,510 676,500" class="messageLine0" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="fill:none"></path><text x="676" y="525" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">Run test</text><path d="M 676,558 C 736,548 736,588 676,578" class="messageLine0" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="fill:none"></path><text x="477" y="603" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">✅ Test passes</text><line x1="674" y1="636" x2="279" y2="636" class="messageLine1" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="stroke-dasharray:3, 3;fill:none"></line><text x="574" y="651" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">Implementation files</text><line x1="276" y1="684" x2="871" y2="684" class="messageLine0" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="fill:none"></line><text x="876" y="699" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">Evaluate code</text><path d="M 876,732 C 936,722 936,762 876,752" class="messageLine0" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="fill:none"></path><text x="876" y="777" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">Extract</text><text x="876" y="796" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">composable</text><path d="M 876,829 C 936,819 936,859 876,849" class="messageLine0" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="fill:none"></path><text x="876" y="874" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">Run test</text><path d="M 876,907 C 936,897 936,937 876,927" class="messageLine0" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="fill:none"></path><text x="577" y="952" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">✅ Improvements applied</text><line x1="874" y1="985" x2="279" y2="985" class="messageLine1" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="stroke-dasharray:3, 3;fill:none"></line><text x="177" y="1000" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">🔴→🟢→🔵 Complete</text><line x1="274" y1="1033" x2="79" y2="1033" class="messageLine1" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="stroke-dasharray:3, 3;fill:none"></line></svg></p>
<h3 id="-red-phase">🔴 RED Phase<a class="heading-link" aria-label="Link to section" href="#-red-phase"><span class="heading-link-icon">#</span></a></h3>
<p>The <code>tdd-test-writer</code> produced:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// src/__tests__/integration/workout-detail.spec.ts</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">afterEach</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> describe</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> expect</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> it</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">vitest</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">createTestApp</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">../helpers/createTestApp</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">db</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> generateId</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">@/db</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">describe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">Workout History Detail View</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  afterEach</span><span style="color:#9ABDF5">(</span><span style="color:#9D7CD8;font-style:italic">async</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">    // cleanup</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">navigates to detail view when clicking a completed workout</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9D7CD8;font-style:italic"> async</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">    // Arrange: Create a completed workout</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> completedWorkout</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">      id</span><span style="color:#89DDFF">:</span><span style="color:#7AA2F7"> generateId</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">      name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Push Day</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">      exercises</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [{</span></span>
<span class="line"><span style="color:#73DACA">        name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Bench Press</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">        sets</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [{ </span><span style="color:#41A6B5">kg</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">100</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#41A6B5"> reps</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">10</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5"> }]</span></span>
<span class="line"><span style="color:#9ABDF5">      }]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">      completedAt</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Date</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">now</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    await</span><span style="color:#C0CAF5"> db</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">workouts</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">add</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">completedWorkout</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">    // Act: Navigate and click</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> app</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#7AA2F7"> createTestApp</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    await</span><span style="color:#C0CAF5"> app</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">user</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">click</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">app</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">getByRole</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">button</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> /</span><span style="color:#B4F9F8">workouts</span><span style="color:#89DDFF">/i</span><span style="color:#9ABDF5"> }))</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    await</span><span style="color:#C0CAF5"> app</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">user</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">click</span><span style="color:#9ABDF5">(</span><span style="color:#BB9AF7;font-style:italic">await</span><span style="color:#C0CAF5"> app</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">findByText</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">Push Day</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">))</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">    // Assert</span></span>
<span class="line"><span style="color:#7AA2F7">    expect</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">app</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">router</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">currentRoute</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">value</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">path</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#89DDFF">      .</span><span style="color:#7AA2F7">toBe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">`</span><span style="color:#9ECE6A">/workouts/</span><span style="color:#7DCFFF">${</span><span style="color:#C0CAF5">completedWorkout</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">id</span><span style="color:#7DCFFF">}</span><span style="color:#89DDFF">`</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#7AA2F7">    expect</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">app</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">getByText</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">Bench Press</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toBeDefined</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#7AA2F7">    expect</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">app</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">getByText</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">100</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toBeDefined</span><span style="color:#9ABDF5">()</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">    app</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">cleanup</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span></span>
<span class="line"><span style="color:#9ABDF5">})</span></span></code><button type="button" class="copy" data-code="// src/__tests__/integration/workout-detail.spec.ts
import { afterEach, describe, expect, it } from 'vitest'
import { createTestApp } from '../helpers/createTestApp'
import { db, generateId } from '@/db'

describe('Workout History Detail View', () => {
  afterEach(async () => {
    // cleanup
  })

  it('navigates to detail view when clicking a completed workout', async () => {
    // Arrange: Create a completed workout
    const completedWorkout = {
      id: generateId(),
      name: 'Push Day',
      exercises: [{
        name: 'Bench Press',
        sets: [{ kg: '100', reps: '10' }]
      }],
      completedAt: Date.now(),
    }
    await db.workouts.add(completedWorkout)

    // Act: Navigate and click
    const app = await createTestApp()
    await app.user.click(app.getByRole('button', { name: /workouts/i }))
    await app.user.click(await app.findByText('Push Day'))

    // Assert
    expect(app.router.currentRoute.value.path)
      .toBe(`/workouts/${completedWorkout.id}`)
    expect(app.getByText('Bench Press')).toBeDefined()
    expect(app.getByText('100')).toBeDefined()

    app.cleanup()
  })
})" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>The test failed:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="plaintext"><code><span class="line"><span>AssertionError: expected &#39;/workouts&#39; to be &#39;/workouts/d747077d-...&#39;</span></span></code><button type="button" class="copy" data-code="AssertionError: expected '/workouts' to be '/workouts/d747077d-...'" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>Exactly what I wanted—a clear failure pointing to missing functionality.</p>
<h3 id="-green-phase">🟢 GREEN Phase<a class="heading-link" aria-label="Link to section" href="#-green-phase"><span class="heading-link-icon">#</span></a></h3>
<p>The <code>tdd-implementer</code> created:</p>
<ul>
<li><code>WorkoutDetailView.vue</code> — New detail view component</li>
<li>Modified <code>TheWorkoutsView.vue</code> — Added click handlers</li>
<li>Modified <code>router/index.ts</code> — Added <code>/workouts/:id</code> route</li>
</ul>
<p>Test passed. Minimal implementation, just enough to satisfy the assertions.</p>
<h3 id="-refactor-phase">🔵 REFACTOR Phase<a class="heading-link" aria-label="Link to section" href="#-refactor-phase"><span class="heading-link-icon">#</span></a></h3>
<p>The <code>tdd-refactorer</code> evaluated the code and made improvements:</p>
<ul>
<li><strong>Extracted <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/how-to-test-vue-composables/" class="internal-link astro-3tyn5ojg"> <code>useWorkoutDetail</code> composable </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">How to Test Vue Composables: A Comprehensive Guide with Vitest</span> <span class="preview-description astro-3tyn5ojg">Learn how to effectively test Vue composables using Vitest. Covers independent and dependent composables, with practical examples and best practices.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">vue</span><span class="preview-tag astro-3tyn5ojg">testing</span>  </span> <time class="preview-date astro-3tyn5ojg">Nov 25, 2023</time> </span> </span> </span>  <script>
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
</script></strong> — Reusable data fetching with discriminated union states</li>
<li><strong>Created shared formatters</strong> — Pulled <code>formatDuration</code> and <code>formatDate</code> into <code>lib/formatters.ts</code></li>
<li><strong>Added accessibility</strong> — Keyboard navigation for clickable cards</li>
</ul>
<p>All tests still passed. The cycle completed.</p>
<h2 id="the-test-helper">The Test Helper<a class="heading-link" aria-label="Link to section" href="#the-test-helper"><span class="heading-link-icon">#</span></a></h2>
<p>A crucial piece making all this work is my <code>createTestApp()</code> helper:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// src/__tests__/helpers/createTestApp.ts</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#9D7CD8;font-style:italic"> async</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> createTestApp</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Promise</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">TestApp</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> pinia</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> createPinia</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> router</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> createRouter</span><span style="color:#9ABDF5">({</span></span>
<span class="line"><span style="color:#73DACA">    history</span><span style="color:#89DDFF">:</span><span style="color:#7AA2F7"> createMemoryHistory</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    routes</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  render</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">App</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">    global</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">plugins</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#7DCFFF">router</span><span style="color:#89DDFF">,</span><span style="color:#7DCFFF"> pinia</span><span style="color:#9ABDF5">] }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  await</span><span style="color:#C0CAF5"> router</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">isReady</span><span style="color:#9ABDF5">()</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">    router</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    user</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> userEvent</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">setup</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    getByRole</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> screen</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">getByRole</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    getByText</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> screen</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">getByText</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    findByText</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> screen</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">findByText</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#7AA2F7">    waitForRoute</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">pattern</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#7AA2F7"> waitFor</span><span style="color:#9ABDF5">(() </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">      if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#C0CAF5">pattern</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">test</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">router</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">currentRoute</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">value</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">path</span><span style="color:#9ABDF5">)) {</span></span>
<span class="line"><span style="color:#BB9AF7">        throw</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> Error</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">Route mismatch</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span></span>
<span class="line"><span style="color:#9ABDF5">    })</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#7AA2F7">    cleanup</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> { </span><span style="color:#C0CAF5">document</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">body</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">innerHTML</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> &#39;&#39;</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// src/__tests__/helpers/createTestApp.ts
export async function createTestApp(): Promise<TestApp> {
  const pinia = createPinia()
  const router = createRouter({
    history: createMemoryHistory(),
    routes,
  })

  render(App, {
    global: { plugins: [router, pinia] },
  })

  await router.isReady()

  return {
    router,
    user: userEvent.setup(),
    getByRole: screen.getByRole,
    getByText: screen.getByText,
    findByText: screen.findByText,
    waitForRoute: (pattern) => waitFor(() => {
      if (!pattern.test(router.currentRoute.value.path)) {
        throw new Error('Route mismatch')
      }
    }),
    cleanup: () => { document.body.innerHTML = '' },
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>This gives agents a consistent API for rendering the full app and simulating user interactions. They don’t need to figure out how to set up Vue, Pinia, and Vue Router each time—they just call <code>createTestApp()</code> and start writing assertions.</p>
<h2 id="hooks-for-consistent-skill-activation">Hooks for Consistent Skill Activation<a class="heading-link" aria-label="Link to section" href="#hooks-for-consistent-skill-activation"><span class="heading-link-icon">#</span></a></h2>
<figure class=" mx-auto "> <img src="/_astro/HOOKSCLAUDE.DZ2Sl5EC_Z1u6xaU.webp" alt="Claude Code hooks lifecycle diagram showing UserPromptSubmit hook injection" loading="lazy" decoding="async" fetchpriority="auto" width="1024" height="541" class="w-full"> <figcaption class="mt-2 text-center text-sm text-gray-500"> Hooks inject instructions at specific lifecycle points in Claude Code </figcaption> </figure>
<p>Even with well-written skills, Claude sometimes skipped evaluation and jumped straight to implementation. I tracked this informally—skill activation happened maybe 20% of the time.</p>
<p>I found a great solution in <a href="https://scottspence.com/posts/how-to-make-claude-code-skills-activate-reliably" rel="noopener noreferrer" target="_blank">Scott Spence’s post on making skills activate reliably</a>. He tested 200+ prompts across different hook configurations and found that a “forced eval” approach—making Claude explicitly evaluate each skill before proceeding—jumped activation from ~20% to ~84%.</p>
<p>The fix: <strong><span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/claude-code-notification-hooks/" class="internal-link astro-3tyn5ojg"> hooks </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Claude Code Notifications: Get Alerts When Tasks Finish (Hooks Setup)</span> <span class="preview-description astro-3tyn5ojg">How to set up Claude Code notifications using hooks. Get desktop alerts when Claude finishes a task, needs your input, or requests permission, instead of watching the terminal.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">claude-code</span><span class="preview-tag astro-3tyn5ojg">notifications</span><span class="preview-tag astro-3tyn5ojg">hooks</span> <span class="preview-tag-more astro-3tyn5ojg">+1</span> </span> <time class="preview-date astro-3tyn5ojg">Nov 23, 2025</time> </span> </span> </span>  <script>
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
</script></strong>. Claude Code runs hooks at specific lifecycle points, and I used <code>UserPromptSubmit</code> to inject a reminder before every response.</p>
<p>In <code>.claude/settings.json</code>:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="json"><code><span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">hooks</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">    &quot;</span><span style="color:#0DB9D7">UserPromptSubmit</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span></span>
<span class="line"><span style="color:#9ABDF5">      {</span></span>
<span class="line"><span style="color:#89DDFF">        &quot;</span><span style="color:#7DCFFF">matcher</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">        &quot;</span><span style="color:#7DCFFF">hooks</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span></span>
<span class="line"><span style="color:#9ABDF5">          {</span></span>
<span class="line"><span style="color:#89DDFF">            &quot;</span><span style="color:#BB9AF7">type</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">command</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">            &quot;</span><span style="color:#BB9AF7">command</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">npx tsx </span><span style="color:#89DDFF">\&quot;</span><span style="color:#9ECE6A">$CLAUDE_PROJECT_DIR/.claude/hooks/user-prompt-skill-eval.ts</span><span style="color:#89DDFF">\&quot;&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">            &quot;</span><span style="color:#BB9AF7">timeout</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 5</span></span>
<span class="line"><span style="color:#9ABDF5">          }</span></span>
<span class="line"><span style="color:#9ABDF5">        ]</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span></span>
<span class="line"><span style="color:#9ABDF5">    ]</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="{
  &#34;hooks&#34;: {
    &#34;UserPromptSubmit&#34;: [
      {
        &#34;matcher&#34;: &#34;&#34;,
        &#34;hooks&#34;: [
          {
            &#34;type&#34;: &#34;command&#34;,
            &#34;command&#34;: &#34;npx tsx \&#34;$CLAUDE_PROJECT_DIR/.claude/hooks/user-prompt-skill-eval.ts\&#34;&#34;,
            &#34;timeout&#34;: 5
          }
        ]
      }
    ]
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>The hook script at <code>.claude/hooks/user-prompt-skill-eval.ts</code>:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">#!/usr/bin/env npx tsx</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">readFileSync</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">node:fs</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">stdout</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">node:process</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> main</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> void</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  readFileSync</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">0</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">utf-8</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">) </span><span style="color:#51597D;font-style:italic">// consume stdin</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> instruction</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> `</span></span>
<span class="line"><span style="color:#9ECE6A">INSTRUCTION: MANDATORY SKILL ACTIVATION SEQUENCE</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9ECE6A">Step 1 - EVALUATE:</span></span>
<span class="line"><span style="color:#9ECE6A">For each skill in &lt;available_skills&gt;, state: [skill-name] - YES/NO - [reason]</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9ECE6A">Step 2 - ACTIVATE:</span></span>
<span class="line"><span style="color:#9ECE6A">IF any skills are YES → Use Skill(skill-name) tool for EACH relevant skill NOW</span></span>
<span class="line"><span style="color:#9ECE6A">IF no skills are YES → State &quot;No skills needed&quot; and proceed</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9ECE6A">Step 3 - IMPLEMENT:</span></span>
<span class="line"><span style="color:#9ECE6A">Only after Step 2 is complete, proceed with implementation.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9ECE6A">CRITICAL: You MUST call Skill() tool in Step 2. Do NOT skip to implementation.</span></span>
<span class="line"><span style="color:#89DDFF">`</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">  stdout</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">write</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">instruction</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">trim</span><span style="color:#9ABDF5">())</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">main</span><span style="color:#9ABDF5">()</span></span></code><button type="button" class="copy" data-code="#!/usr/bin/env npx tsx
import { readFileSync } from 'node:fs'
import { stdout } from 'node:process'

function main(): void {
  readFileSync(0, 'utf-8') // consume stdin

  const instruction = `
INSTRUCTION: MANDATORY SKILL ACTIVATION SEQUENCE

Step 1 - EVALUATE:
For each skill in <available_skills>, state: [skill-name] - YES/NO - [reason]

Step 2 - ACTIVATE:
IF any skills are YES → Use Skill(skill-name) tool for EACH relevant skill NOW
IF no skills are YES → State &#34;No skills needed&#34; and proceed

Step 3 - IMPLEMENT:
Only after Step 2 is complete, proceed with implementation.

CRITICAL: You MUST call Skill() tool in Step 2. Do NOT skip to implementation.
`

  stdout.write(instruction.trim())
}

main()" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<div class="alert alert-important astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">📢</span> Results </p> <div class="alert-content astro-7kdbuayl"> <p>With this hook, skill activation jumped from ~20% to ~84%. Now when I say “implement the workout detail view,” the TDD skill triggers automatically.</p> </div> </div> 
<h2 id="conclusion">Conclusion<a class="heading-link" aria-label="Link to section" href="#conclusion"><span class="heading-link-icon">#</span></a></h2>
<p>Claude Code’s default behavior produces implementation-first code with minimal test coverage. Without constraints, it optimizes for “working code” rather than “tested code.”</p>
<p>The system described here addresses this through architectural separation:</p>
<ul>
<li><strong>Hooks</strong> inject evaluation logic before every prompt, increasing skill activation from ~20% to ~84%</li>
<li><strong>Skills</strong> define explicit phase gates that block progression until each TDD step completes</li>
<li><strong>Subagents</strong> enforce context isolation—the test writer cannot see implementation plans, so tests reflect actual requirements rather than anticipated code structure</li>
</ul>
<p>The setup cost is ~2 hours of configuration. After that, each feature request automatically follows the Red-Green-Refactor cycle without manual enforcement.</p> </article> <script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).only=e;window.dispatchEvent(new Event("astro:only"));})();</script><astro-island uid="Z1XneyL" component-url="/_astro/presentation.C3Wa0mjp.js" component-export="VMarkBlogRenderer" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;containerSelector&quot;:[0,&quot;#article&quot;],&quot;class&quot;:[0,&quot;astro-vj4tpspi&quot;]}" ssr client="only" opts="{&quot;name&quot;:&quot;VMarkBlogRenderer&quot;,&quot;value&quot;:&quot;react&quot;}"></astro-island> <!-- Fullscreen Modal Container using native dialog --><dialog id="mermaid-modal" class="mermaid-modal" aria-label="Fullscreen diagram view"> <div class="mermaid-modal-content"> <button class="mermaid-modal-close" aria-label="Close fullscreen view" type="button"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <line x1="18" y1="6" x2="6" y2="18"></line> <line x1="6" y1="6" x2="18" y2="18"></line> </svg> </button> <div class="mermaid-modal-diagram"></div> <div class="mermaid-modal-hint">Press <kbd>Esc</kbd> or click outside to close</div> </div> </dialog>  <script type="module">const p=new Set;function g(){const e=document.getElementById("mermaid-modal"),c=e?.querySelector(".mermaid-modal-diagram"),f=e?.querySelector(".mermaid-modal-close");if(!e||!c)return;document.querySelectorAll('svg[id^="mermaid-"]').forEach(t=>{if(!t.id.match(/^mermaid-\d+$/)||p.has(t.id)||t.parentElement?.classList.contains("mermaid-fullscreen-wrapper")||t.closest(".mermaid-modal"))return;p.add(t.id);const n=document.createElement("div");n.className="mermaid-fullscreen-wrapper mermaid-clickable",n.setAttribute("tabindex","0"),n.setAttribute("role","button"),n.setAttribute("aria-label","Click to view diagram fullscreen"),t.parentElement?.insertBefore(n,t),n.appendChild(t);const o=document.createElement("div");o.className="mermaid-expand-icon",o.innerHTML=`
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
</li> <li class="astro-vj4tpspi">Small tips and trick</li> </ul> </div> <a href="https://alex-op-newsletter.beehiiv.com/subscribe?utm_source=blog&utm_medium=post&utm_campaign=post_custom-tdd-workflow-claude-code-vue" target="_blank" rel="noopener noreferrer" id="newsletter-subscribe-button" class="inline-flex items-center justify-center gap-2 rounded-full bg-skin-accent px-6 py-3 text-base font-semibold text-skin-inverted shadow-md transition-all duration-200 hover:scale-[1.02] hover:transform hover:opacity-90 astro-vj4tpspi"> <svg class="h-5 w-5 fill-current astro-vj4tpspi" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg>
Subscribe Now
</a> <button id="newsletter-dismiss" data-post-slug="custom-tdd-workflow-claude-code-vue" class="absolute right-3 top-3 rounded-full p-1 text-skin-base transition-all duration-200 hover:bg-skin-accent hover:bg-opacity-10 hover:text-skin-accent astro-vj4tpspi" aria-label="Close notification"> <svg class="h-5 w-5 astro-vj4tpspi" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class="astro-vj4tpspi"></path> </svg> </button> </div> </div> </div> <ul class="my-8 flex flex-wrap gap-2 astro-vj4tpspi"> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/ai/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-2"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">ai</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/vue/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-3"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">vue</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/testing/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-4"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">testing</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/claude-code/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-5"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">claude-code</span>   </a> </li>  </ul> <div class="flex flex-col-reverse items-center justify-between gap-6 sm:flex-row-reverse sm:items-end sm:gap-4 astro-vj4tpspi"> <button id="back-to-top" class="focus-outline whitespace-nowrap py-1 hover:opacity-75 astro-vj4tpspi"> <svg xmlns="http://www.w3.org/2000/svg" class="rotate-90 astro-vj4tpspi"> <path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg> <span class="astro-vj4tpspi">Back to Top</span> </button> <div class="social-icons astro-wkojbtzc"> <span class="italic astro-wkojbtzc">Share this post on:</span> <div class="text-center astro-wkojbtzc"> <a href="https://wa.me/?text=https://alexop.dev/posts/custom-tdd-workflow-claude-code-vue/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via WhatsApp" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"></path>
      <path d="M9 10a0.5 .5 0 0 0 1 0v-1a0.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a0.5 .5 0 0 0 0 -1h-1a0.5 .5 0 0 0 0 1"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via WhatsApp</span> </a><a href="https://www.facebook.com/sharer.php?u=https://alexop.dev/posts/custom-tdd-workflow-claude-code-vue/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Facebook" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"
    ></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on Facebook</span> </a><a href="https://x.com/intent/tweet?url=https://alexop.dev/posts/custom-tdd-workflow-claude-code-vue/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Tweet this post" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Tweet this post</span> </a><a href="https://t.me/share/url?url=https://alexop.dev/posts/custom-tdd-workflow-claude-code-vue/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via Telegram" target="_blank" rel="noopener noreferrer"> <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon-tabler"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"></path>
      </svg> <span class="sr-only astro-wkojbtzc">Share this post via Telegram</span> </a><a href="https://pinterest.com/pin/create/button/?url=https://alexop.dev/posts/custom-tdd-workflow-claude-code-vue/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Pinterest" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <line x1="8" y1="20" x2="12" y2="11"></line>
      <path d="M10.7 14c.437 1.263 1.43 2 2.55 2c2.071 0 3.75 -1.554 3.75 -4a5 5 0 1 0 -9.7 1.7"></path>
      <circle cx="12" cy="12" r="9"></circle>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post on Pinterest</span> </a><a href="mailto:?subject=See%20this%20post&#38;body=https://alexop.dev/posts/custom-tdd-workflow-claude-code-vue/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via email" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via email</span> </a><a href="https://www.linkedin.com/shareArticle?mini=true&url=https://alexop.dev/posts/custom-tdd-workflow-claude-code-vue/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
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
</h2> <div class="md:grid-cols-3 grid grid-cols-1 gap-6 astro-vj4tpspi"> <a href="/posts/understanding-claude-code-full-stack/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">Understanding Claude Code&#39;s Full Stack: MCP, Skills, Subagents, and Hooks Explained</h3> <p class="related-post-description astro-vj4tpspi"> A practical guide to Claude Code&#39;s features — explained in the order they were introduced: MCP (2024), Claude Code core (Feb 2025), Plugins (2025), and Agent Skills (Oct 2025). What each does, how they fit together, and when to use what. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-11-09T00:00:00.000Z">Nov 9, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> claude-code </span> </div> </div> </a><a href="/posts/building-my-first-claude-code-plugin/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">Building My First Claude Code Plugin</h3> <p class="related-post-description astro-vj4tpspi"> How I built a Claude Code plugin to generate skills, agents, commands, and more—and stopped copy-pasting boilerplate. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-11-08T00:00:00.000Z">Nov 8, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> claude-code </span> </div> </div> </a><a href="/posts/claude-code-notification-hooks/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">Get Notified When Claude Code Finishes With Hooks</h3> <p class="related-post-description astro-vj4tpspi"> Set up desktop notifications in Claude Code to know when Claude needs your input or permission. Learn how to use hooks for instant alerts instead of constantly checking. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-11-23T00:00:00.000Z">Nov 23, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> claude-code </span> </div> </div> </a> </div> </div> </main> <footer class="mt-auto astro-sz7xmlte"> <div class="max-w-5xl mx-auto px-4"> <hr class="border-skin-line" aria-hidden="true"> </div> <div class="footer-wrapper astro-sz7xmlte"> <div class="footer-content astro-sz7xmlte"> <div class="copyright-wrapper astro-sz7xmlte"> <span class="astro-sz7xmlte">Copyright &#169; 2026</span> <span class="separator astro-sz7xmlte">&nbsp;|&nbsp;</span> <span class="astro-sz7xmlte">All rights reserved.</span> </div> <div class="rss-prompt astro-sz7xmlte"> <a href="/rss.xml" class="rss-link group astro-sz7xmlte" title="Never miss a post - Subscribe via RSS" onclick="if (window.plausible) window.plausible('RSS Subscribe', { props: { location: 'footer' } })"> <div class="flex items-center gap-2 astro-sz7xmlte"> <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-skin-accent group-hover:animate-pulse astro-sz7xmlte"><path fill="currentColor" d="M19 20.001C19 11.729 12.271 5 4 5v2c7.168 0 13 5.832 13 13.001h2z" class="astro-sz7xmlte"></path><path fill="currentColor" d="M12 20.001h2C14 14.486 9.514 10 4 10v2c4.411 0 8 3.589 8 8.001z" class="astro-sz7xmlte"></path><circle cx="6" cy="18" r="2" fill="currentColor" class="astro-sz7xmlte"></circle> </svg> <span class="text-sm astro-sz7xmlte">Subscribe via RSS</span> </div> </a> </div> <div class="social-icons flex astro-upu6fzxr"> <a href="https://github.com/alexanderop" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title=" alexop.dev on Github" target="_blank" rel="noopener noreferrer"> <svg
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
    </script> </body> </html>  <script>(function(){const postSlug = "custom-tdd-workflow-claude-code-vue";

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
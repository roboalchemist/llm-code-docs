# Source: https://alexop.dev/posts/mutation-testing-ai-agents-vitest-browser-mode

<!DOCTYPE html><html lang="en" class="scroll-smooth astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/posts/mutation-testing-ai-agents-vitest-browser-mode/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>Mutation Testing with AI Agents When Stryker Doesn&#39;t Work | alexop.dev</title><meta name="title" content="Mutation Testing with AI Agents When Stryker Doesn't Work | alexop.dev"><meta name="description" content="When Stryker doesn't support your test stack, AI agents can execute mutation testing manually. A practical approach for Vitest browser mode and Playwright."><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="Mutation Testing with AI Agents When Stryker Doesn't Work | alexop.dev"><meta property="og:description" content="When Stryker doesn't support your test stack, AI agents can execute mutation testing manually. A practical approach for Vitest browser mode and Playwright."><meta property="og:url" content="https://alexop.dev/posts/mutation-testing-ai-agents-vitest-browser-mode/"><meta property="og:image" content="https://alexop.dev/posts/mutation-testing-with-ai-agents-when-stryker-doesnt-work/index.png"><meta property="og:type" content="article"><!-- Article Published/Modified time --><meta property="article:published_time" content="2026-01-13T00:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/posts/mutation-testing-ai-agents-vitest-browser-mode/"><meta property="twitter:title" content="Mutation Testing with AI Agents When Stryker Doesn't Work | alexop.dev"><meta property="twitter:description" content="When Stryker doesn't support your test stack, AI agents can execute mutation testing manually. A practical approach for Vitest browser mode and Playwright."><meta property="twitter:image" content="https://alexop.dev/posts/mutation-testing-with-ai-agents-when-stryker-doesnt-work/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"Mutation Testing with AI Agents When Stryker Doesn't Work | alexop.dev","description":"When Stryker doesn't support your test stack, AI agents can execute mutation testing manually. A practical approach for Vitest browser mode and Playwright.","image":"https://alexop.dev/posts/mutation-testing-with-ai-agents-when-stryker-doesnt-work/index.png","datePublished":"2026-01-13T00:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
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
</style><style>[data-astro-transition-scope="astro-plk3gbjq-1"] { view-transition-name: mutation-testing-with-ai-agents-when-stryker-doesnt-work; }@layer astro { ::view-transition-old(mutation-testing-with-ai-agents-when-stryker-doesnt-work) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(mutation-testing-with-ai-agents-when-stryker-doesnt-work) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(mutation-testing-with-ai-agents-when-stryker-doesnt-work) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(mutation-testing-with-ai-agents-when-stryker-doesnt-work) { 
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
</style><style>[data-astro-transition-scope="astro-36ssibgs-2"] { view-transition-name: testing; }@layer astro { ::view-transition-old(testing) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-3"] { view-transition-name: ai; }@layer astro { ::view-transition-old(ai) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-4"] { view-transition-name: claude-code; }@layer astro { ::view-transition-old(claude-code) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-5"] { view-transition-name: vitest; }@layer astro { ::view-transition-old(vitest) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(vitest) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(vitest) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(vitest) { 
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <div class="mx-auto flex w-full max-w-5xl justify-start px-2 astro-vj4tpspi"> <button class="focus-outline mb-2 mt-8 flex hover:opacity-75 astro-vj4tpspi" onclick="(() => (history.length === 1) ? window.location = '/' : history.back())()"> <svg xmlns="http://www.w3.org/2000/svg" class="astro-vj4tpspi"><path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg><span class="astro-vj4tpspi">Go back</span> </button> </div> <main data-pagefind-body id="main-content" class="relative astro-vj4tpspi"> <h1 class="post-title astro-vj4tpspi" data-astro-transition-scope="astro-plk3gbjq-1">Mutation Testing with AI Agents When Stryker Doesn&#39;t Work</h1> <div class="my-2 flex items-center justify-between astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-100 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-base"><time dateTime="2026-01-13T00:00:00.000Z">Jan 13, 2026</time><span class="sr-only"> at </span></span></div> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="de8De" prefix="r3" component-url="/_astro/PostCopyButton.-PGtk4At.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;title&quot;:[0,&quot;Mutation Testing with AI Agents When Stryker Doesn&#39;t Work&quot;],&quot;content&quot;:[0,&quot;import InternalLink from \&quot;@features/mdx-components/components/InternalLink.astro\&quot;;\nimport Alert from \&quot;@features/mdx-components/components/Alert.astro\&quot;;\n\n## The Coverage Lie\n\nCode coverage lies. A test that exercises a line doesn&#39;t mean it verifies that line does the right thing:\n\n```typescript\nfunction add(a: number, b: number): number {\n  return a + b\n}\n\n// 100% coverage - would still pass if add() returned 999\nit(&#39;adds numbers&#39;, () =&gt; {\n  add(2, 2)\n})\n```\n\nMutation testing flips the question. Instead of asking \&quot;did tests run this code?\&quot;, it asks **\&quot;if I break this code, do tests fail?\&quot;**\n\nUsing our `add` example, a mutation tester would:\n\n```typescript\n// Original\nfunction add(a: number, b: number): number {\n  return a + b\n}\n\n// Mutated: swap + for -\nfunction add(a: number, b: number): number {\n  return a - b  // &lt;-- bug introduced\n}\n```\n\nNow run the test. `add(2, 2)` returns `0` instead of `4`. Does the test fail? No—it never checked the result. **The mutant survives.** Your test has a gap.\n\nThe process:\n1. **Mutate**: Introduce a small bug (change `&gt;` to `&gt;=`, swap `&amp;&amp;` for `||`, delete a line)\n2. **Run tests**: Execute your test suite against the mutated code\n3. **Evaluate**: If tests pass with the bug, your tests are weak. If tests fail, they caught it.\n\nA mutation that tests fail to catch is a \&quot;surviving mutant\&quot;—proof of a test gap.\n\n---\n\n## When Stryker Works: The Gold Standard\n\nWhen your test stack supports it, automated mutation testing with Stryker is the way to go. It&#39;s fast, deterministic, generates HTML reports, and runs in CI pipelines. This is especially valuable when you have pure functions with high test coverage but want to verify test quality.\n\nHere&#39;s what it looks like in practice:\n\n```bash\npnpm test:mutation\n# or: stryker run\n```\n\n```\nINFO ProjectReader Found 7 of 2947 file(s) to be mutated.\nINFO Instrumenter Instrumented 7 source file(s) with 394 mutant(s)\nINFO DryRunExecutor Initial test run succeeded. Ran 184 tests in 0 seconds.\n\nMutation testing  [====================] 100% | 394/394 Mutants tested\n(35 survived, 0 timed out)\n\n--------------|---------|----------|----------|----------|\nFile          |  % score | # killed | # survived | # no cov |\n--------------|---------|----------|----------|----------|\nAll files     |   90.86 |      358 |         35 |        1 |\n backlinks.ts |   96.30 |       26 |          1 |        0 |\n callouts.ts  |   93.94 |       62 |          4 |        0 |\n graph.ts     |   91.55 |       65 |          6 |        0 |\n mentions.ts  |   91.30 |       63 |          5 |        1 |\n minimark.ts  |   82.61 |       76 |         16 |        0 |\n text.ts      |  100.00 |       34 |          0 |        0 |\n wikilinks.ts |   91.43 |       32 |          3 |        0 |\n--------------|---------|----------|----------|----------|\n\nINFO MutationTestExecutor Done in 36 seconds.\n```\n\n394 mutants tested across 7 files in 36 seconds. The report shows exactly which files have weak spots—`minimark.ts` at 82.61% needs attention, while `text.ts` is solid at 100%.\n\nStryker also generates an interactive HTML report where you can drill into each surviving mutant and see exactly what code change your tests failed to catch.\n\n&lt;Alert type=\&quot;tip\&quot; title=\&quot;Use Stryker When You Can\&quot;&gt;\n  If your stack supports Stryker (standard Vitest in Node mode, Jest, Mocha), use it. Deterministic tooling in your CI pipeline beats manual approaches every time. The AI agent technique in this post is for when Stryker isn&#39;t an option.\n&lt;/Alert&gt;\n\n---\n\n## The Vitest Browser Mode Problem\n\nBut what if Stryker doesn&#39;t support your stack? Stryker doesn&#39;t work with Vitest&#39;s browser mode. Their instrumentation assumes Node.js execution, but browser mode runs tests in actual Chromium via Playwright.\n\nMy setup:\n- **Framework**: Vitest 4 with `browser.enabled: true`\n- **Provider**: Playwright (Chromium)\n- **Test style**: Integration tests with real DOM\n\n&lt;InternalLink slug=\&quot;vue3_testing_pyramid_vitest_browser_mode\&quot;&gt;My testing strategy&lt;/InternalLink&gt; relies heavily on Vitest browser mode for realistic user flow testing. Stryker&#39;s mutation coverage reports? Not an option. And switching to Node-based testing would mean losing the browser-specific behavior I&#39;m actually testing.\n\n---\n\n## AI Agents as Manual Mutation Testers\n\nThe mutation testing algorithm is simple enough that an AI coding agent can execute it manually. Claude Code can:\n\n1. Read your source code\n2. Apply mutations systematically\n3. Run `pnpm test --run`\n4. Record whether tests passed or failed\n5. Restore the original code\n6. Report surviving mutants with suggested fixes\n\nI adapted a &lt;InternalLink slug=\&quot;claude-code-customization-guide-claudemd-skills-subagents\&quot;&gt;Claude Code skill&lt;/InternalLink&gt; originally created by [Paul Hammond](https://www.linkedin.com/posts/paul-hammond-bb5b78251_mutation-testing-is-typically-expensive-but-activity-7414719212071473152-_xTm) that codifies this workflow.\n\n```mermaid\nflowchart TD\n    subgraph Agent[\&quot;AI Agent Workflow\&quot;]\n        A[Read source file] --&gt; B[Identify mutation targets]\n        B --&gt; C[Apply single mutation]\n        C --&gt; D[Run test suite]\n        D --&gt; E{Tests fail?}\n        E --&gt;|Yes| F[Mutant KILLED]\n        E --&gt;|No| G[Mutant SURVIVED]\n        F --&gt; H[Restore original code]\n        G --&gt; H\n        H --&gt; I{More mutations?}\n        I --&gt;|Yes| C\n        I --&gt;|No| J[Generate report]\n    end\n\n    subgraph Results[\&quot;Report Output\&quot;]\n        J --&gt; K[Killed mutants: Tests caught the bug]\n        J --&gt; L[Survived mutants: Test gaps found]\n        L --&gt; M[Suggested fixes for each gap]\n    end\n\n    style G fill:#f96,stroke:#333\n    style F fill:#6f9,stroke:#333\n    style L fill:#f96,stroke:#333\n    style K fill:#6f9,stroke:#333\n```\n\n### The Mutation Testing Skill\n\nThe skill defines mutation operators in priority order:\n\n**Priority 1 - Boundaries** (most likely to survive):\n\n| Original | Mutate To |\n|----------|-----------|\n| `&lt;` | `&lt;=` |\n| `&gt;` | `&gt;=` |\n| `&lt;=` | `&lt;` |\n| `&gt;=` | `&gt;` |\n\n**Priority 2 - Boolean Logic**:\n\n| Original | Mutate To |\n|----------|-----------|\n| `&amp;&amp;` | `\\|\\|` |\n| `\\|\\|` | `&amp;&amp;` |\n| `!condition` | `condition` |\n\n**Priority 3 - Return Values**:\n\n| Original | Mutate To |\n|----------|-----------|\n| `return x` | `return null` |\n| `return true` | `return false` |\n| Early return | Remove it |\n\n**Priority 4 - Statement Removal**:\n\n| Original | Mutate To |\n|----------|-----------|\n| `array.push(x)` | Remove |\n| `await save(x)` | Remove |\n| `emit(&#39;event&#39;)` | Remove |\n\nThe agent applies each mutation one at a time, runs tests, records results, and restores the original code immediately.\n\n---\n\n## Real Example: Settings Feature\n\nI ran this against my settings feature. The integration tests looked comprehensive—theme toggling, language switching, unit preferences. Code coverage would show high percentages.\n\n**Results: 38% mutation score** (5 killed, 8 survived out of 13 mutations)\n\nHere&#39;s what the AI agent found:\n\n### Surviving Mutant #1: Volume Boundary Not Tested\n\n```typescript\n// Original (stores/settings.ts:65)\nMath.min(Math.max(volume, 0.5), 1)\n\n// Mutation: Change 0.5 to 0.4\nMath.min(Math.max(volume, 0.4), 1)\n\n// Result: Tests PASSED -&gt; Mutant SURVIVED\n```\n\nMy tests never verified the minimum volume constraint. A bug changing the minimum from 50% to 40% would ship undetected.\n\n### Surviving Mutant #2: Theme DOM Class Not Verified\n\n```typescript\n// Original (composables/useTheme.ts:26)\nnewMode === &#39;dark&#39;\n\n// Mutation: Negate the condition\nnewMode !== &#39;dark&#39;\n\n// Result: Tests PASSED -&gt; Mutant SURVIVED\n```\n\nMy test checked that clicking the toggle changed the stored preference. It never verified that `document.documentElement.classList` actually received the `dark` class. The UI could break while tests pass.\n\n### Surviving Mutant #3: Error Handling Path Untested\n\n```typescript\n// Original (stores/settings.ts:28)\nif (error) return\n\n// Mutation: Negate the condition\nif (!error) return\n\n// Result: Tests PASSED -&gt; Mutant SURVIVED\n```\n\nNo test exercised the error handling branch. A bug that inverted error handling would go unnoticed.\n\n### The Fixes\n\nThe agent suggested specific tests for each surviving mutant:\n\n```typescript\n// Fix for Mutant #1: Boundary test\nit(&#39;volume slider has minimum value constraint of 50%&#39;, async () =&gt; {\n  const volumeSlider = page.getByTestId(&#39;timer-sound-volume-slider&#39;)\n  await expect.poll(async () =&gt; {\n    const el = await volumeSlider.element()\n    return el.getAttribute(&#39;min&#39;)\n  }).toBe(&#39;0.5&#39;)\n})\n\n// Fix for Mutant #2: DOM verification\nit(&#39;adds dark class to html element when dark mode enabled&#39;, async () =&gt; {\n  const themeToggle = page.getByTestId(&#39;theme-toggle&#39;)\n  await userEvent.click(themeToggle)\n\n  await expect.poll(() =&gt;\n    document.documentElement.classList.contains(&#39;dark&#39;)\n  ).toBe(true)\n})\n```\n\n---\n\n## How to Set This Up\n\n### Step 1: Create the Skill\n\nSave this as `.claude/skills/mutation-testing/SKILL.md`:\n\n&lt;details&gt;\n&lt;summary&gt;Full Mutation Testing Skill (click to expand)&lt;/summary&gt;\n\n```markdown\n---\nname: mutation-testing\ndescription: |\n  Mutation testing patterns for verifying test effectiveness. Use when analyzing branch code\n  to find weak or missing tests. Triggers: \&quot;mutation testing\&quot;, \&quot;test effectiveness\&quot;,\n  \&quot;would tests catch this bug\&quot;, \&quot;weak tests\&quot;, \&quot;are my tests good enough\&quot;, \&quot;surviving mutants\&quot;.\n---\n\n# Mutation Testing\n\nMutation testing answers: **\&quot;Would my tests catch this bug?\&quot;** by actually introducing bugs and running tests.\n\n---\n\n## Execution Workflow\n\n**CRITICAL**: This skill actually mutates code and runs tests. Follow this exact process:\n\n### Step 1: Identify Target Code\n\ngit diff main...HEAD --name-only | grep -E &#39;\\.(ts|js|tsx|jsx|vue)&#39; | grep -v &#39;\\.test\\.&#39; | grep -v &#39;\\.spec\\.&#39;\n\n### Step 2: For Each Function to Test\n\nExecute this loop for each mutation:\n\n1. READ the original file and note exact content\n2. APPLY one mutation (edit the code)\n3. RUN tests: pnpm test --run (or specific test file)\n4. RECORD result: KILLED (test failed) or SURVIVED (test passed)\n5. RESTORE original code immediately\n6. Repeat for next mutation\n\n### Step 3: Report Results\n\nAfter all mutations, provide a summary table:\n\n| Mutation | Location | Result | Action Needed |\n|----------|----------|--------|---------------|\n| `&gt;` → `&gt;=` | file.ts:42 | SURVIVED | Add boundary test |\n| `&amp;&amp;` → `||` | file.ts:58 | KILLED | None |\n\n---\n\n## Mutation Operators to Apply\n\n### Priority 1: Boundary Mutations (Most Likely to Survive)\n\n| Original | Mutate To | Why It Matters |\n|----------|-----------|----------------|\n| `&lt;` | `&lt;=` | Boundary not tested |\n| `&gt;` | `&gt;=` | Boundary not tested |\n| `&lt;=` | `&lt;` | Equality case missed |\n| `&gt;=` | `&gt;` | Equality case missed |\n\n### Priority 2: Boolean Logic Mutations\n\n| Original | Mutate To | Why It Matters |\n|----------|-----------|----------------|\n| `&amp;&amp;` | `\\|\\|` | Only tested when both true |\n| `\\|\\|` | `&amp;&amp;` | Only tested when both false |\n| `!condition` | `condition` | Negation not verified |\n\n### Priority 3: Arithmetic Mutations\n\n| Original | Mutate To | Why It Matters |\n|----------|-----------|----------------|\n| `+` | `-` | Tested with 0 only |\n| `-` | `+` | Tested with 0 only |\n| `*` | `/` | Tested with 1 only |\n\n### Priority 4: Return/Early Exit Mutations\n\n| Original | Mutate To | Why It Matters |\n|----------|-----------|----------------|\n| `return x` | `return null` | Return value not asserted |\n| `return true` | `return false` | Boolean return not checked |\n| `if (cond) return` | `// removed` | Early exit not tested |\n\n### Priority 5: Statement Removal\n\n| Original | Mutate To | Why It Matters |\n|----------|-----------|----------------|\n| `array.push(x)` | `// removed` | Side effect not verified |\n| `await save(x)` | `// removed` | Async operation not verified |\n| `emit(&#39;event&#39;)` | `// removed` | Event emission not tested |\n\n---\n\n## Practical Execution Example\n\n### Example: Testing a Validation Function\n\n**Original code** (`src/utils/validation.ts:15`):\n\nexport function isValidAge(age: number): boolean {\n  return age &gt;= 18 &amp;&amp; age &lt;= 120;\n}\n\n**Mutation 1**: Change `&gt;=` to `&gt;`\n\nexport function isValidAge(age: number): boolean {\n  return age &gt; 18 &amp;&amp; age &lt;= 120;  // MUTATED\n}\n\n**Run tests**: `pnpm test --run src/__tests__/validation.test.ts`\n\n**Result**: Tests PASS → **SURVIVED** (Bad! Need test for `isValidAge(18)`)\n\n**Restore original code immediately**\n\n**Mutation 2**: Change `&amp;&amp;` to `||`\n\nexport function isValidAge(age: number): boolean {\n  return age &gt;= 18 || age &lt;= 120;  // MUTATED\n}\n\n**Run tests**: `pnpm test --run src/__tests__/validation.test.ts`\n\n**Result**: Tests FAIL → **KILLED** (Good! Tests catch this bug)\n\n**Restore original code immediately**\n\n---\n\n## Results Interpretation\n\n### Mutant States\n\n| State | Meaning | Action |\n|-------|---------|--------|\n| **KILLED** | Test failed with mutant | Tests are effective |\n| **SURVIVED** | Tests passed with mutant | **Add or strengthen test** |\n| **TIMEOUT** | Tests hung (infinite loop) | Counts as detected |\n\n### Mutation Score\n\nScore = (Killed + Timeout) / Total Mutations * 100\n\n| Score | Quality |\n|-------|---------|\n| &lt; 60% | Weak - significant test gaps |\n| 60-80% | Moderate - improvements needed |\n| 80-90% | Good - minor gaps |\n| &gt; 90% | Strong test suite |\n\n---\n\n## Fixing Surviving Mutants\n\nWhen a mutant survives, add a test that would catch it:\n\n### Surviving: Boundary mutation (`&gt;=` → `&gt;`)\n\n// Add boundary test\nit(&#39;accepts exactly 18 years old&#39;, () =&gt; {\n  expect(isValidAge(18)).toBe(true);  // Would fail if &gt;= became &gt;\n});\n\n### Surviving: Logic mutation (`&amp;&amp;` → `||`)\n\n// Add test with mixed conditions\nit(&#39;rejects when only one condition met&#39;, () =&gt; {\n  expect(isValidAge(15)).toBe(false);  // Would pass if &amp;&amp; became ||\n});\n\n### Surviving: Statement removal\n\n// Add side effect verification\nit(&#39;saves to database&#39;, async () =&gt; {\n  await processOrder(order);\n  expect(db.save).toHaveBeenCalledWith(order);  // Would fail if save removed\n});\n\n---\n\n## Quick Checklist During Mutation\n\nFor each mutation, ask:\n\n1. **Before mutating**: Does a test exist for this code path?\n2. **After running tests**: Did any test actually fail?\n3. **If survived**: What specific test would catch this?\n4. **After fixing**: Re-run mutation to confirm killed\n\n---\n\n## Common Surviving Mutation Patterns\n\n### Tests Only Check Happy Path\n\n// WEAK: Only tests success case\nit(&#39;validates&#39;, () =&gt; {\n  expect(validate(goodInput)).toBe(true);\n});\n\n// STRONG: Tests both cases\nit(&#39;validates good input&#39;, () =&gt; {\n  expect(validate(goodInput)).toBe(true);\n});\nit(&#39;rejects bad input&#39;, () =&gt; {\n  expect(validate(badInput)).toBe(false);\n});\n\n### Tests Use Identity Values\n\n// WEAK: Mutation survives\nexpect(multiply(5, 1)).toBe(5);  // 5*1 = 5/1 = 5\n\n// STRONG: Mutation detected\nexpect(multiply(5, 3)).toBe(15);  // 5*3 ≠ 5/3\n\n### Tests Don&#39;t Assert Return Values\n\n// WEAK: No return value check\nit(&#39;processes&#39;, () =&gt; {\n  process(data);  // No assertion!\n});\n\n// STRONG: Asserts outcome\nit(&#39;processes&#39;, () =&gt; {\n  const result = process(data);\n  expect(result).toEqual(expected);\n});\n\n---\n\n## Important Rules\n\n1. **ALWAYS restore original code** after each mutation\n2. **Run tests immediately** after applying mutation\n3. **One mutation at a time** - don&#39;t combine mutations\n4. **Focus on changed code** - prioritize branch diff\n5. **Track all results** - report full mutation summary\n\n---\n\n## Summary Report Template\n\nAfter completing mutation testing, provide:\n\n## Mutation Testing Results\n\n**Target**: `src/features/workout/utils.ts` (functions: X, Y, Z)\n**Total Mutations**: 12\n**Killed**: 9\n**Survived**: 3\n**Score**: 75%\n\n### Surviving Mutants (Action Required)\n\n| # | Location | Original | Mutated | Suggested Test |\n|---|----------|----------|---------|----------------|\n| 1 | line 42 | `&gt;=` | `&gt;` | Test boundary value |\n| 2 | line 58 | `&amp;&amp;` | `\\|\\|` | Test mixed conditions |\n| 3 | line 71 | `emit()` | removed | Verify event emission |\n\n### Killed Mutants (Tests Effective)\n\n- Line 35: `+` → `-` killed by `calculation.test.ts`\n- Line 48: `true` → `false` killed by `validate.test.ts`\n- ...\n```\n\n&lt;/details&gt;\n\n### Step 2: Invoke It\n\n```bash\nclaude \&quot;Run mutation testing on the settings feature\&quot;\n```\n\nThe agent will:\n- Find changed files on your branch\n- Identify testable functions\n- Apply mutations systematically\n- Report surviving mutants with suggested test fixes\n\n### Step 3: Review and Fix\n\nThe agent produces a markdown report. Review each surviving mutant and decide:\n- Add the suggested test\n- Accept the risk (document why)\n- Refactor the code to be more testable\n\n---\n\n## When to Use This Approach\n\n| Good Fit | Not Ideal |\n|----------|-----------|\n| Vitest browser mode (no Stryker support) | Large codebases needing full mutation coverage |\n| Playwright component testing | CI/CD automation (manual agent invocation) |\n| Small-to-medium codebases | Strict mutation score thresholds |\n| Pre-merge review of specific features | |\n| Learning what makes tests effective | |\n\n&lt;Alert type=\&quot;tip\&quot; title=\&quot;Complement, Don&#39;t Replace\&quot;&gt;\n  This approach works best alongside your existing testing strategy. Use it to spot-check critical features before merge, not as a replacement for automated mutation testing where available.\n&lt;/Alert&gt;\n\n&lt;Alert type=\&quot;info\&quot; title=\&quot;Feature Branches, Not Pipelines\&quot;&gt;\n  This skill shines on **feature branches** where you want to validate test quality before merging. Running AI agents in CI/CD pipelines is possible—you could build &lt;InternalLink slug=\&quot;building_ai_qa_engineer_claude_code_playwright\&quot;&gt;an automated QA agent&lt;/InternalLink&gt; with the Claude Agent SDK—but it adds complexity and cost. For pipeline automation, deterministic tools like Stryker remain the better choice when your stack supports them. Think of this as a developer tool for improving tests during development, not a CI gate.\n&lt;/Alert&gt;\n\n---\n\n## Key Takeaways\n\n1. **Coverage doesn&#39;t equal confidence.** High code coverage can coexist with ineffective tests.\n\n2. **Mutation testing reveals test gaps.** By breaking code and checking if tests notice, you find what&#39;s actually being verified.\n\n3. **AI agents can execute manual mutation testing.** When tooling doesn&#39;t support your stack, an agent can apply the algorithm systematically.\n\n4. **Focus on surviving mutants.** Each one is a potential bug your tests wouldn&#39;t catch.\n\n5. **This complements, not replaces.** Use this alongside coverage reports, not instead of automated mutation testing where available.\n\n---\n\n## Resources\n\n- [Paul Hammond&#39;s Mutation Testing Skill](https://github.com/citypaul/.dotfiles/blob/main/claude/.claude/skills/mutation-testing/SKILL.md) - The original skill this post is based on\n- [Mutation Testing on Wikipedia](https://en.wikipedia.org/wiki/Mutation_testing)\n- [Stryker Mutator](https://stryker-mutator.io/) - When your stack supports it\n- &lt;InternalLink slug=\&quot;custom-tdd-workflow-claude-code-vue\&quot;&gt;My TDD workflow with Claude Code&lt;/InternalLink&gt; - Related approach for test-first development&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PostCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus-outline inline-flex items-center gap-1.5 rounded-md border border-skin-line bg-skin-card px-2.5 py-1.5 text-xs font-medium text-skin-base opacity-80 transition-all hover:border-skin-accent/50 hover:text-skin-accent hover:opacity-100" aria-label="Copy post as markdown" title="Copy post as markdown for AI/LLM"><svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg><span>Copy Post</span></button><!--astro:end--></astro-island> </div>  <article id="article" class="prose mx-auto mt-8 max-w-5xl astro-vj4tpspi"> <h2 id="the-coverage-lie">The Coverage Lie<a class="heading-link" aria-label="Link to section" href="#the-coverage-lie"><span class="heading-link-icon">#</span></a></h2>
<p>Code coverage lies. A test that exercises a line doesn’t mean it verifies that line does the right thing:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> add</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">a</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> b</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#C0CAF5"> a</span><span style="color:#89DDFF"> +</span><span style="color:#C0CAF5"> b</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// 100% coverage - would still pass if add() returned 999</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">adds numbers</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  add</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">2</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 2</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">})</span></span></code><button type="button" class="copy" data-code="function add(a: number, b: number): number {
  return a + b
}

// 100% coverage - would still pass if add() returned 999
it('adds numbers', () => {
  add(2, 2)
})" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>Mutation testing flips the question. Instead of asking “did tests run this code?”, it asks <strong>“if I break this code, do tests fail?”</strong></p>
<p>Using our <code>add</code> example, a mutation tester would:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// Original</span></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> add</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">a</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> b</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#C0CAF5"> a</span><span style="color:#89DDFF"> +</span><span style="color:#C0CAF5"> b</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Mutated: swap + for -</span></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> add</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">a</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> b</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#C0CAF5"> a</span><span style="color:#89DDFF"> -</span><span style="color:#C0CAF5"> b</span><span style="color:#51597D;font-style:italic">  // &lt;-- bug introduced</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// Original
function add(a: number, b: number): number {
  return a + b
}

// Mutated: swap + for -
function add(a: number, b: number): number {
  return a - b  // <-- bug introduced
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>Now run the test. <code>add(2, 2)</code> returns <code>0</code> instead of <code>4</code>. Does the test fail? No—it never checked the result. <strong>The mutant survives.</strong> Your test has a gap.</p>
<p>The process:</p>
<ol>
<li><strong>Mutate</strong>: Introduce a small bug (change <code>&gt;</code> to <code>&gt;=</code>, swap <code>&amp;&amp;</code> for <code>||</code>, delete a line)</li>
<li><strong>Run tests</strong>: Execute your test suite against the mutated code</li>
<li><strong>Evaluate</strong>: If tests pass with the bug, your tests are weak. If tests fail, they caught it.</li>
</ol>
<p>A mutation that tests fail to catch is a “surviving mutant”—proof of a test gap.</p>
<hr/>
<h2 id="when-stryker-works-the-gold-standard">When Stryker Works: The Gold Standard<a class="heading-link" aria-label="Link to section" href="#when-stryker-works-the-gold-standard"><span class="heading-link-icon">#</span></a></h2>
<p>When your test stack supports it, automated mutation testing with Stryker is the way to go. It’s fast, deterministic, generates HTML reports, and runs in CI pipelines. This is especially valuable when you have pure functions with high test coverage but want to verify test quality.</p>
<p>Here’s what it looks like in practice:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#C0CAF5">pnpm</span><span style="color:#9ECE6A"> test:mutation</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"># or: stryker run</span></span></code><button type="button" class="copy" data-code="pnpm test:mutation
# or: stryker run" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="plaintext"><code><span class="line"><span>INFO ProjectReader Found 7 of 2947 file(s) to be mutated.</span></span>
<span class="line"><span>INFO Instrumenter Instrumented 7 source file(s) with 394 mutant(s)</span></span>
<span class="line"><span>INFO DryRunExecutor Initial test run succeeded. Ran 184 tests in 0 seconds.</span></span>
<span class="line"><span></span></span>
<span class="line"><span>Mutation testing  [====================] 100% | 394/394 Mutants tested</span></span>
<span class="line"><span>(35 survived, 0 timed out)</span></span>
<span class="line"><span></span></span>
<span class="line"><span>--------------|---------|----------|----------|----------|</span></span>
<span class="line"><span>File          |  % score | # killed | # survived | # no cov |</span></span>
<span class="line"><span>--------------|---------|----------|----------|----------|</span></span>
<span class="line"><span>All files     |   90.86 |      358 |         35 |        1 |</span></span>
<span class="line"><span> backlinks.ts |   96.30 |       26 |          1 |        0 |</span></span>
<span class="line"><span> callouts.ts  |   93.94 |       62 |          4 |        0 |</span></span>
<span class="line"><span> graph.ts     |   91.55 |       65 |          6 |        0 |</span></span>
<span class="line"><span> mentions.ts  |   91.30 |       63 |          5 |        1 |</span></span>
<span class="line"><span> minimark.ts  |   82.61 |       76 |         16 |        0 |</span></span>
<span class="line"><span> text.ts      |  100.00 |       34 |          0 |        0 |</span></span>
<span class="line"><span> wikilinks.ts |   91.43 |       32 |          3 |        0 |</span></span>
<span class="line"><span>--------------|---------|----------|----------|----------|</span></span>
<span class="line"><span></span></span>
<span class="line"><span>INFO MutationTestExecutor Done in 36 seconds.</span></span></code><button type="button" class="copy" data-code="INFO ProjectReader Found 7 of 2947 file(s) to be mutated.
INFO Instrumenter Instrumented 7 source file(s) with 394 mutant(s)
INFO DryRunExecutor Initial test run succeeded. Ran 184 tests in 0 seconds.

Mutation testing  [====================] 100% | 394/394 Mutants tested
(35 survived, 0 timed out)

--------------|---------|----------|----------|----------|
File          |  % score | # killed | # survived | # no cov |
--------------|---------|----------|----------|----------|
All files     |   90.86 |      358 |         35 |        1 |
 backlinks.ts |   96.30 |       26 |          1 |        0 |
 callouts.ts  |   93.94 |       62 |          4 |        0 |
 graph.ts     |   91.55 |       65 |          6 |        0 |
 mentions.ts  |   91.30 |       63 |          5 |        1 |
 minimark.ts  |   82.61 |       76 |         16 |        0 |
 text.ts      |  100.00 |       34 |          0 |        0 |
 wikilinks.ts |   91.43 |       32 |          3 |        0 |
--------------|---------|----------|----------|----------|

INFO MutationTestExecutor Done in 36 seconds." onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>394 mutants tested across 7 files in 36 seconds. The report shows exactly which files have weak spots—<code>minimark.ts</code> at 82.61% needs attention, while <code>text.ts</code> is solid at 100%.</p>
<p>Stryker also generates an interactive HTML report where you can drill into each surviving mutant and see exactly what code change your tests failed to catch.</p>
<div class="alert alert-tip astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">💪</span> Use Stryker When You Can </p> <div class="alert-content astro-7kdbuayl"> <p>If your stack supports Stryker (standard Vitest in Node mode, Jest, Mocha), use it. Deterministic tooling in your CI pipeline beats manual approaches every time. The AI agent technique in this post is for when Stryker isn’t an option.</p> </div> </div> 
<hr/>
<h2 id="the-vitest-browser-mode-problem">The Vitest Browser Mode Problem<a class="heading-link" aria-label="Link to section" href="#the-vitest-browser-mode-problem"><span class="heading-link-icon">#</span></a></h2>
<p>But what if Stryker doesn’t support your stack? Stryker doesn’t work with Vitest’s browser mode. Their instrumentation assumes Node.js execution, but browser mode runs tests in actual Chromium via Playwright.</p>
<p>My setup:</p>
<ul>
<li><strong>Framework</strong>: Vitest 4 with <code>browser.enabled: true</code></li>
<li><strong>Provider</strong>: Playwright (Chromium)</li>
<li><strong>Test style</strong>: Integration tests with real DOM</li>
</ul>
<p><span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/vue3_testing_pyramid_vitest_browser_mode/" class="internal-link astro-3tyn5ojg"> My testing strategy </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Vue 3 Testing Pyramid: A Practical Guide with Vitest Browser Mode</span> <span class="preview-description astro-3tyn5ojg">Learn a practical testing strategy for Vue 3 applications using composable unit tests, Vitest browser mode integration tests, and visual regression testing.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">vue</span><span class="preview-tag astro-3tyn5ojg">testing</span><span class="preview-tag astro-3tyn5ojg">vitest</span> <span class="preview-tag-more astro-3tyn5ojg">+2</span> </span> <time class="preview-date astro-3tyn5ojg">Dec 14, 2025</time> </span> </span> </span>  <script>
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
</script> relies heavily on Vitest browser mode for realistic user flow testing. Stryker’s mutation coverage reports? Not an option. And switching to Node-based testing would mean losing the browser-specific behavior I’m actually testing.</p>
<hr/>
<h2 id="ai-agents-as-manual-mutation-testers">AI Agents as Manual Mutation Testers<a class="heading-link" aria-label="Link to section" href="#ai-agents-as-manual-mutation-testers"><span class="heading-link-icon">#</span></a></h2>
<p>The mutation testing algorithm is simple enough that an AI coding agent can execute it manually. Claude Code can:</p>
<ol>
<li>Read your source code</li>
<li>Apply mutations systematically</li>
<li>Run <code>pnpm test --run</code></li>
<li>Record whether tests passed or failed</li>
<li>Restore the original code</li>
<li>Report surviving mutants with suggested fixes</li>
</ol>
<p>I adapted a <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/claude-code-customization-guide-claudemd-skills-subagents/" class="internal-link astro-3tyn5ojg"> Claude Code skill </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Claude Code Customization: CLAUDE.md, Slash Commands, Skills, and Subagents</span> <span class="preview-description astro-3tyn5ojg">The complete guide to customizing Claude Code. Compare CLAUDE.md, slash commands, skills, and subagents with practical examples showing when to use each.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">claude-code</span><span class="preview-tag astro-3tyn5ojg">ai</span><span class="preview-tag astro-3tyn5ojg">tooling</span> <span class="preview-tag-more astro-3tyn5ojg">+1</span> </span> <time class="preview-date astro-3tyn5ojg">Dec 21, 2025</time> </span> </span> </span>  <script>
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
</script> originally created by <a href="https://www.linkedin.com/posts/paul-hammond-bb5b78251_mutation-testing-is-typically-expensive-but-activity-7414719212071473152-_xTm" rel="noopener noreferrer" target="_blank">Paul Hammond</a> that codifies this workflow.</p>
<p><svg id="mermaid-0" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="flowchart" style="max-width:687.2421875px" viewBox="0 0 687.2421875 1628.46875" role="graphics-document document" aria-roledescription="flowchart-v2"><style>#mermaid-0{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-0 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-0 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-0 .error-icon{fill:#a44141;}#mermaid-0 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-0 .edge-thickness-normal{stroke-width:1px;}#mermaid-0 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-0 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-0 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-0 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-0 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-0 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-0 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-0 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-0 p{margin:0;}#mermaid-0 .label{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;color:#ccc;}#mermaid-0 .cluster-label text{fill:#F9FFFE;}#mermaid-0 .cluster-label span{color:#F9FFFE;}#mermaid-0 .cluster-label span p{background-color:transparent;}#mermaid-0 .label text,#mermaid-0 span{fill:#ccc;color:#ccc;}#mermaid-0 .node rect,#mermaid-0 .node circle,#mermaid-0 .node ellipse,#mermaid-0 .node polygon,#mermaid-0 .node path{fill:transparent;stroke:2px;stroke-width:1px;}#mermaid-0 .rough-node .label text,#mermaid-0 .node .label text,#mermaid-0 .image-shape .label,#mermaid-0 .icon-shape .label{text-anchor:middle;}#mermaid-0 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-0 .rough-node .label,#mermaid-0 .node .label,#mermaid-0 .image-shape .label,#mermaid-0 .icon-shape .label{text-align:center;}#mermaid-0 .node.clickable{cursor:pointer;}#mermaid-0 .root .anchor path{fill:rgb(171, 75, 153)!important;stroke-width:0;stroke:rgb(171, 75, 153);}#mermaid-0 .arrowheadPath{fill:lightgrey;}#mermaid-0 .edgePath .path{stroke:rgb(171, 75, 153);stroke-width:2.0px;}#mermaid-0 .flowchart-link{stroke:rgb(171, 75, 153);fill:none;}#mermaid-0 .edgeLabel{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-0 .edgeLabel p{background-color:hsla(0, 0%, 25%, 0);}#mermaid-0 .edgeLabel rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-0 .labelBkg{background-color:rgba(63.75, 63.75, 63.75, 0.5);}#mermaid-0 .cluster rect{fill:transparent;stroke:rgba(255, 255, 255, 0.25);stroke-width:1px;}#mermaid-0 .cluster text{fill:#F9FFFE;}#mermaid-0 .cluster span{color:#F9FFFE;}#mermaid-0 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:12px;background:rgb(138, 51, 123);border:1px solid rgba(255, 255, 255, 0.25);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-0 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-0 rect.text{fill:none;stroke-width:0;}#mermaid-0 .icon-shape,#mermaid-0 .image-shape{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-0 .icon-shape p,#mermaid-0 .image-shape p{background-color:hsla(0, 0%, 25%, 0);padding:2px;}#mermaid-0 .icon-shape rect,#mermaid-0 .image-shape rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-0 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-0 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-0 :root{--mermaid-font-family:arial,sans-serif;}</style><g><marker id="mermaid-0_flowchart-v2-pointEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-pointStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="4.5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 5 L 10 10 L 10 0 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-circleEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="11" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-0_flowchart-v2-circleStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="-1" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-0_flowchart-v2-crossEnd" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="12" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-crossStart" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="-1" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><g class="root"><g class="clusters"><g class="cluster" id="Results" data-look="classic"><rect style="" x="39.2421875" y="1364.46875" width="640" height="256"></rect><g class="cluster-label" transform="translate(296.625, 1364.46875)"><foreignObject width="125.234375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Report Output</p></span></div></foreignObject></g></g><g class="cluster" id="Agent" data-look="classic"><rect style="" x="8" y="8" width="642.02734375" height="1306.46875"></rect><g class="cluster-label" transform="translate(247.130859375, 8)"><foreignObject width="163.765625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>AI Agent Workflow</p></span></div></foreignObject></g></g></g><g class="edgePaths"><path d="M359.242,87L359.242,91.167C359.242,95.333,359.242,103.667,359.242,111.333C359.242,119,359.242,126,359.242,129.5L359.242,133" id="L_A_B_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_A_B_0" data-points="W3sieCI6MzU5LjI0MjE4NzUsInkiOjg3fSx7IngiOjM1OS4yNDIxODc1LCJ5IjoxMTJ9LHsieCI6MzU5LjI0MjE4NzUsInkiOjEzN31d" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M359.242,215L359.242,219.167C359.242,223.333,359.242,231.667,359.242,239.333C359.242,247,359.242,254,359.242,257.5L359.242,261" id="L_B_C_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_B_C_0" data-points="W3sieCI6MzU5LjI0MjE4NzUsInkiOjIxNX0seyJ4IjozNTkuMjQyMTg3NSwieSI6MjQwfSx7IngiOjM1OS4yNDIxODc1LCJ5IjoyNjV9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M308.969,343L303.598,347.167C298.227,351.333,287.484,359.667,282.113,367.333C276.742,375,276.742,382,276.742,385.5L276.742,389" id="L_C_D_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_C_D_0" data-points="W3sieCI6MzA4Ljk2ODc1LCJ5IjozNDN9LHsieCI6Mjc2Ljc0MjE4NzUsInkiOjM2OH0seyJ4IjoyNzYuNzQyMTg3NSwieSI6MzkzfV0=" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M276.742,447L276.742,451.167C276.742,455.333,276.742,463.667,276.742,471.333C276.742,479,276.742,486,276.742,489.5L276.742,493" id="L_D_E_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_D_E_0" data-points="W3sieCI6Mjc2Ljc0MjE4NzUsInkiOjQ0N30seyJ4IjoyNzYuNzQyMTg3NSwieSI6NDcyfSx7IngiOjI3Ni43NDIxODc1LCJ5Ijo0OTd9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M235.84,616.066L222.251,629.05C208.663,642.034,181.486,668.001,167.897,686.485C154.309,704.969,154.309,715.969,154.309,721.469L154.309,726.969" id="L_E_F_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_E_F_0" data-points="W3sieCI6MjM1LjgzOTc2NjgyNDQ1MjIsInkiOjYxNi4wNjYzMjkzMjQ0NTIyfSx7IngiOjE1NC4zMDg1OTM3NSwieSI6NjkzLjk2ODc1fSx7IngiOjE1NC4zMDg1OTM3NSwieSI6NzMwLjk2ODc1fV0=" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M317.645,616.066L331.233,629.05C344.822,642.034,371.999,668.001,385.587,686.485C399.176,704.969,399.176,715.969,399.176,721.469L399.176,726.969" id="L_E_G_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_E_G_0" data-points="W3sieCI6MzE3LjY0NDYwODE3NTU0NzgsInkiOjYxNi4wNjYzMjkzMjQ0NTIyfSx7IngiOjM5OS4xNzU3ODEyNSwieSI6NjkzLjk2ODc1fSx7IngiOjM5OS4xNzU3ODEyNSwieSI6NzMwLjk2ODc1fV0=" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M154.309,784.969L154.309,789.135C154.309,793.302,154.309,801.635,161.689,809.66C169.069,817.684,183.829,825.4,191.209,829.258L198.589,833.116" id="L_F_H_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_F_H_0" data-points="W3sieCI6MTU0LjMwODU5Mzc1LCJ5Ijo3ODQuOTY4NzV9LHsieCI6MTU0LjMwODU5Mzc1LCJ5Ijo4MDkuOTY4NzV9LHsieCI6MjAyLjEzNDIxNjMwODU5Mzc1LCJ5Ijo4MzQuOTY4NzV9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M399.176,784.969L399.176,789.135C399.176,793.302,399.176,801.635,391.796,809.66C384.416,817.684,369.655,825.4,362.275,829.258L354.895,833.116" id="L_G_H_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_G_H_0" data-points="W3sieCI6Mzk5LjE3NTc4MTI1LCJ5Ijo3ODQuOTY4NzV9LHsieCI6Mzk5LjE3NTc4MTI1LCJ5Ijo4MDkuOTY4NzV9LHsieCI6MzUxLjM1MDE1ODY5MTQwNjI1LCJ5Ijo4MzQuOTY4NzV9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M276.742,912.969L276.742,917.135C276.742,921.302,276.742,929.635,283.523,944.014C290.303,958.393,303.864,978.817,310.645,989.028L317.426,999.24" id="L_H_I_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_H_I_0" data-points="W3sieCI6Mjc2Ljc0MjE4NzUsInkiOjkxMi45Njg3NX0seyJ4IjoyNzYuNzQyMTg3NSwieSI6OTM3Ljk2ODc1fSx7IngiOjMxOS42MzgxOTcxNzM1MTg3MywieSI6MTAwMi41NzI3NDAzMjY0ODEzfV0=" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M419.382,1023.108L441.202,1008.919C463.022,994.729,506.661,966.349,528.481,941.492C550.301,916.635,550.301,895.302,550.301,873.969C550.301,852.635,550.301,831.302,550.301,811.969C550.301,792.635,550.301,775.302,550.301,755.969C550.301,736.635,550.301,715.302,550.301,685.138C550.301,654.974,550.301,615.979,550.301,578.984C550.301,541.99,550.301,506.995,550.301,480.831C550.301,454.667,550.301,437.333,550.301,420C550.301,402.667,550.301,385.333,538.494,372.712C526.688,360.09,503.075,352.18,491.268,348.225L479.461,344.271" id="L_I_C_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_I_C_0" data-points="W3sieCI6NDE5LjM4MTg5MTI4NzIxMjQ1LCJ5IjoxMDIzLjEwODQ1Mzc4NzIxMjR9LHsieCI6NTUwLjMwMDc4MTI1LCJ5Ijo5MzcuOTY4NzV9LHsieCI6NTUwLjMwMDc4MTI1LCJ5Ijo4NzMuOTY4NzV9LHsieCI6NTUwLjMwMDc4MTI1LCJ5Ijo4MDkuOTY4NzV9LHsieCI6NTUwLjMwMDc4MTI1LCJ5Ijo3NTcuOTY4NzV9LHsieCI6NTUwLjMwMDc4MTI1LCJ5Ijo2OTMuOTY4NzV9LHsieCI6NTUwLjMwMDc4MTI1LCJ5Ijo1NzYuOTg0Mzc1fSx7IngiOjU1MC4zMDA3ODEyNSwieSI6NDcyfSx7IngiOjU1MC4zMDA3ODEyNSwieSI6NDIwfSx7IngiOjU1MC4zMDA3ODEyNSwieSI6MzY4fSx7IngiOjQ3NS42Njg1MTgwNjY0MDYyNSwieSI6MzQzfV0=" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M359.242,1161.469L359.242,1167.635C359.242,1173.802,359.242,1186.135,359.242,1197.802C359.242,1209.469,359.242,1220.469,359.242,1225.969L359.242,1231.469" id="L_I_J_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_I_J_0" data-points="W3sieCI6MzU5LjI0MjE4NzUsInkiOjExNjEuNDY4NzV9LHsieCI6MzU5LjI0MjE4NzUsInkiOjExOTguNDY4NzV9LHsieCI6MzU5LjI0MjE4NzUsInkiOjEyMzUuNDY4NzV9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M278.761,1289.469L266.342,1293.635C253.922,1297.802,229.082,1306.135,216.662,1314.469C204.242,1322.802,204.242,1331.135,204.242,1339.469C204.242,1347.802,204.242,1356.135,204.242,1363.802C204.242,1371.469,204.242,1378.469,204.242,1381.969L204.242,1385.469" id="L_J_K_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_J_K_0" data-points="W3sieCI6Mjc4Ljc2MTQxODI2OTIzMDgsInkiOjEyODkuNDY4NzV9LHsieCI6MjA0LjI0MjE4NzUsInkiOjEzMTQuNDY4NzV9LHsieCI6MjA0LjI0MjE4NzUsInkiOjEzMzkuNDY4NzV9LHsieCI6MjA0LjI0MjE4NzUsInkiOjEzNjQuNDY4NzV9LHsieCI6MjA0LjI0MjE4NzUsInkiOjEzODkuNDY4NzV9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M439.723,1289.469L452.143,1293.635C464.563,1297.802,489.402,1306.135,501.822,1314.469C514.242,1322.802,514.242,1331.135,514.242,1339.469C514.242,1347.802,514.242,1356.135,514.242,1363.802C514.242,1371.469,514.242,1378.469,514.242,1381.969L514.242,1385.469" id="L_J_L_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_J_L_0" data-points="W3sieCI6NDM5LjcyMjk1NjczMDc2OTIsInkiOjEyODkuNDY4NzV9LHsieCI6NTE0LjI0MjE4NzUsInkiOjEzMTQuNDY4NzV9LHsieCI6NTE0LjI0MjE4NzUsInkiOjEzMzkuNDY4NzV9LHsieCI6NTE0LjI0MjE4NzUsInkiOjEzNjQuNDY4NzV9LHsieCI6NTE0LjI0MjE4NzUsInkiOjEzODkuNDY4NzV9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M514.242,1467.469L514.242,1471.635C514.242,1475.802,514.242,1484.135,514.242,1491.802C514.242,1499.469,514.242,1506.469,514.242,1509.969L514.242,1513.469" id="L_L_M_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_L_M_0" data-points="W3sieCI6NTE0LjI0MjE4NzUsInkiOjE0NjcuNDY4NzV9LHsieCI6NTE0LjI0MjE4NzUsInkiOjE0OTIuNDY4NzV9LHsieCI6NTE0LjI0MjE4NzUsInkiOjE1MTcuNDY4NzV9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path></g><g class="edgeLabels"><g class="edgeLabel"><g class="label" data-id="L_A_B_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_B_C_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_C_D_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_D_E_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(154.30859375, 693.96875)"><g class="label" data-id="L_E_F_0" transform="translate(-14.453125, -12)"><foreignObject width="28.90625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>Yes</p></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(399.17578125, 693.96875)"><g class="label" data-id="L_E_G_0" transform="translate(-9.6328125, -12)"><foreignObject width="19.265625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>No</p></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_F_H_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_G_H_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_H_I_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(550.30078125, 693.96875)"><g class="label" data-id="L_I_C_0" transform="translate(-14.453125, -12)"><foreignObject width="28.90625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>Yes</p></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(359.2421875, 1198.46875)"><g class="label" data-id="L_I_J_0" transform="translate(-9.6328125, -12)"><foreignObject width="19.265625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>No</p></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_J_K_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_J_L_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_L_M_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g></g><g class="nodes"><g class="node default" id="flowchart-A-0" transform="translate(359.2421875, 60)"><rect class="basic label-container" style="" x="-107.0625" y="-27" width="214.125" height="54"></rect><g class="label" style="" transform="translate(-77.0625, -12)"><rect></rect><foreignObject width="154.125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Read source file</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-B-1" transform="translate(359.2421875, 176)"><rect class="basic label-container" style="" x="-130" y="-39" width="260" height="78"></rect><g class="label" style="" transform="translate(-100, -24)"><rect></rect><foreignObject width="200" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table;white-space:break-spaces;line-height:1.5;max-width:200px;text-align:center;width:200px"><span class="nodeLabel"><p>Identify mutation targets</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-C-3" transform="translate(359.2421875, 304)"><rect class="basic label-container" style="" x="-130" y="-39" width="260" height="78"></rect><g class="label" style="" transform="translate(-100, -24)"><rect></rect><foreignObject width="200" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table;white-space:break-spaces;line-height:1.5;max-width:200px;text-align:center;width:200px"><span class="nodeLabel"><p>Apply single mutation</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-D-5" transform="translate(276.7421875, 420)"><rect class="basic label-container" style="" x="-97.4296875" y="-27" width="194.859375" height="54"></rect><g class="label" style="" transform="translate(-67.4296875, -12)"><rect></rect><foreignObject width="134.859375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Run test suite</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-E-7" transform="translate(276.7421875, 576.984375)"><polygon points="79.984375,0 159.96875,-79.984375 79.984375,-159.96875 0,-79.984375" class="label-container" transform="translate(-79.484375, 79.984375)"></polygon><g class="label" style="" transform="translate(-52.984375, -12)"><rect></rect><foreignObject width="105.96875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Tests fail?</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-F-9" transform="translate(154.30859375, 757.96875)"><rect class="basic label-container" style="fill:#6f9 !important;stroke:#333 !important" x="-92.6171875" y="-27" width="185.234375" height="54"></rect><g class="label" style="" transform="translate(-62.6171875, -12)"><rect></rect><foreignObject width="125.234375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Mutant KILLED</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-G-11" transform="translate(399.17578125, 757.96875)"><rect class="basic label-container" style="fill:#f96 !important;stroke:#333 !important" x="-102.25" y="-27" width="204.5" height="54"></rect><g class="label" style="" transform="translate(-72.25, -12)"><rect></rect><foreignObject width="144.5" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Mutant SURVIVED</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-H-13" transform="translate(276.7421875, 873.96875)"><rect class="basic label-container" style="" x="-130" y="-39" width="260" height="78"></rect><g class="label" style="" transform="translate(-100, -24)"><rect></rect><foreignObject width="200" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table;white-space:break-spaces;line-height:1.5;max-width:200px;text-align:center;width:200px"><span class="nodeLabel"><p>Restore original code</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-I-17" transform="translate(359.2421875, 1062.21875)"><polygon points="99.25,0 198.5,-99.25 99.25,-198.5 0,-99.25" class="label-container" transform="translate(-98.75, 99.25)"></polygon><g class="label" style="" transform="translate(-72.25, -12)"><rect></rect><foreignObject width="144.5" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>More mutations?</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-J-21" transform="translate(359.2421875, 1262.46875)"><rect class="basic label-container" style="" x="-102.25" y="-27" width="204.5" height="54"></rect><g class="label" style="" transform="translate(-72.25, -12)"><rect></rect><foreignObject width="144.5" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Generate report</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-K-23" transform="translate(204.2421875, 1428.46875)"><rect class="basic label-container" style="fill:#6f9 !important;stroke:#333 !important" x="-130" y="-39" width="260" height="78"></rect><g class="label" style="" transform="translate(-100, -24)"><rect></rect><foreignObject width="200" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table;white-space:break-spaces;line-height:1.5;max-width:200px;text-align:center;width:200px"><span class="nodeLabel"><p>Killed mutants: Tests caught the bug</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-L-25" transform="translate(514.2421875, 1428.46875)"><rect class="basic label-container" style="fill:#f96 !important;stroke:#333 !important" x="-130" y="-39" width="260" height="78"></rect><g class="label" style="" transform="translate(-100, -24)"><rect></rect><foreignObject width="200" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table;white-space:break-spaces;line-height:1.5;max-width:200px;text-align:center;width:200px"><span class="nodeLabel"><p>Survived mutants: Test gaps found</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-M-27" transform="translate(514.2421875, 1556.46875)"><rect class="basic label-container" style="" x="-130" y="-39" width="260" height="78"></rect><g class="label" style="" transform="translate(-100, -24)"><rect></rect><foreignObject width="200" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table;white-space:break-spaces;line-height:1.5;max-width:200px;text-align:center;width:200px"><span class="nodeLabel"><p>Suggested fixes for each gap</p></span></div></foreignObject></g></g></g></g></g></svg></p>
<h3 id="the-mutation-testing-skill">The Mutation Testing Skill<a class="heading-link" aria-label="Link to section" href="#the-mutation-testing-skill"><span class="heading-link-icon">#</span></a></h3>
<p>The skill defines mutation operators in priority order:</p>
<p><strong>Priority 1 - Boundaries</strong> (most likely to survive):</p>

























<table><thead><tr><th>Original</th><th>Mutate To</th></tr></thead><tbody><tr><td data-label="Original"><code>&lt;</code></td><td data-label="Mutate To"><code>&lt;=</code></td></tr><tr><td data-label="Original"><code>&gt;</code></td><td data-label="Mutate To"><code>&gt;=</code></td></tr><tr><td data-label="Original"><code>&lt;=</code></td><td data-label="Mutate To"><code>&lt;</code></td></tr><tr><td data-label="Original"><code>&gt;=</code></td><td data-label="Mutate To"><code>&gt;</code></td></tr></tbody></table>
<p><strong>Priority 2 - Boolean Logic</strong>:</p>





















<table><thead><tr><th>Original</th><th>Mutate To</th></tr></thead><tbody><tr><td data-label="Original"><code>&amp;&amp;</code></td><td data-label="Mutate To"><code>||</code></td></tr><tr><td data-label="Original"><code>||</code></td><td data-label="Mutate To"><code>&amp;&amp;</code></td></tr><tr><td data-label="Original"><code>!condition</code></td><td data-label="Mutate To"><code>condition</code></td></tr></tbody></table>
<p><strong>Priority 3 - Return Values</strong>:</p>





















<table><thead><tr><th>Original</th><th>Mutate To</th></tr></thead><tbody><tr><td data-label="Original"><code>return x</code></td><td data-label="Mutate To"><code>return null</code></td></tr><tr><td data-label="Original"><code>return true</code></td><td data-label="Mutate To"><code>return false</code></td></tr><tr><td data-label="Original">Early return</td><td data-label="Mutate To">Remove it</td></tr></tbody></table>
<p><strong>Priority 4 - Statement Removal</strong>:</p>





















<table><thead><tr><th>Original</th><th>Mutate To</th></tr></thead><tbody><tr><td data-label="Original"><code>array.push(x)</code></td><td data-label="Mutate To">Remove</td></tr><tr><td data-label="Original"><code>await save(x)</code></td><td data-label="Mutate To">Remove</td></tr><tr><td data-label="Original"><code>emit(&#39;event&#39;)</code></td><td data-label="Mutate To">Remove</td></tr></tbody></table>
<p>The agent applies each mutation one at a time, runs tests, records results, and restores the original code immediately.</p>
<hr/>
<h2 id="real-example-settings-feature">Real Example: Settings Feature<a class="heading-link" aria-label="Link to section" href="#real-example-settings-feature"><span class="heading-link-icon">#</span></a></h2>
<p>I ran this against my settings feature. The integration tests looked comprehensive—theme toggling, language switching, unit preferences. Code coverage would show high percentages.</p>
<p><strong>Results: 38% mutation score</strong> (5 killed, 8 survived out of 13 mutations)</p>
<p>Here’s what the AI agent found:</p>
<h3 id="surviving-mutant-1-volume-boundary-not-tested">Surviving Mutant #1: Volume Boundary Not Tested<a class="heading-link" aria-label="Link to section" href="#surviving-mutant-1-volume-boundary-not-tested"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// Original (stores/settings.ts:65)</span></span>
<span class="line"><span style="color:#C0CAF5">Math</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">min</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">Math</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">max</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">volume</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 0.5</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 1</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Mutation: Change 0.5 to 0.4</span></span>
<span class="line"><span style="color:#C0CAF5">Math</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">min</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">Math</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">max</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">volume</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 0.4</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 1</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Result: Tests PASSED -&gt; Mutant SURVIVED</span></span></code><button type="button" class="copy" data-code="// Original (stores/settings.ts:65)
Math.min(Math.max(volume, 0.5), 1)

// Mutation: Change 0.5 to 0.4
Math.min(Math.max(volume, 0.4), 1)

// Result: Tests PASSED -> Mutant SURVIVED" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>My tests never verified the minimum volume constraint. A bug changing the minimum from 50% to 40% would ship undetected.</p>
<h3 id="surviving-mutant-2-theme-dom-class-not-verified">Surviving Mutant #2: Theme DOM Class Not Verified<a class="heading-link" aria-label="Link to section" href="#surviving-mutant-2-theme-dom-class-not-verified"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// Original (composables/useTheme.ts:26)</span></span>
<span class="line"><span style="color:#C0CAF5">newMode</span><span style="color:#BB9AF7"> ===</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">dark</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Mutation: Negate the condition</span></span>
<span class="line"><span style="color:#C0CAF5">newMode</span><span style="color:#BB9AF7"> !==</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">dark</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Result: Tests PASSED -&gt; Mutant SURVIVED</span></span></code><button type="button" class="copy" data-code="// Original (composables/useTheme.ts:26)
newMode === 'dark'

// Mutation: Negate the condition
newMode !== 'dark'

// Result: Tests PASSED -> Mutant SURVIVED" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>My test checked that clicking the toggle changed the stored preference. It never verified that <code>document.documentElement.classList</code> actually received the <code>dark</code> class. The UI could break while tests pass.</p>
<h3 id="surviving-mutant-3-error-handling-path-untested">Surviving Mutant #3: Error Handling Path Untested<a class="heading-link" aria-label="Link to section" href="#surviving-mutant-3-error-handling-path-untested"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// Original (stores/settings.ts:28)</span></span>
<span class="line"><span style="color:#BB9AF7">if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">error</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7;font-style:italic"> return</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Mutation: Negate the condition</span></span>
<span class="line"><span style="color:#BB9AF7">if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#C0CAF5">error</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7;font-style:italic"> return</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Result: Tests PASSED -&gt; Mutant SURVIVED</span></span></code><button type="button" class="copy" data-code="// Original (stores/settings.ts:28)
if (error) return

// Mutation: Negate the condition
if (!error) return

// Result: Tests PASSED -> Mutant SURVIVED" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>No test exercised the error handling branch. A bug that inverted error handling would go unnoticed.</p>
<h3 id="the-fixes">The Fixes<a class="heading-link" aria-label="Link to section" href="#the-fixes"><span class="heading-link-icon">#</span></a></h3>
<p>The agent suggested specific tests for each surviving mutant:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// Fix for Mutant #1: Boundary test</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">volume slider has minimum value constraint of 50%</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9D7CD8;font-style:italic"> async</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> volumeSlider</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> page</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">getByTestId</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">timer-sound-volume-slider</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  await</span><span style="color:#C0CAF5"> expect</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">poll</span><span style="color:#9ABDF5">(</span><span style="color:#9D7CD8;font-style:italic">async</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> el</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#C0CAF5"> volumeSlider</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">element</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#C0CAF5"> el</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">getAttribute</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">min</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toBe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">0.5</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">})</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Fix for Mutant #2: DOM verification</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">adds dark class to html element when dark mode enabled</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9D7CD8;font-style:italic"> async</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> themeToggle</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> page</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">getByTestId</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">theme-toggle</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  await</span><span style="color:#C0CAF5"> userEvent</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">click</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">themeToggle</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  await</span><span style="color:#C0CAF5"> expect</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">poll</span><span style="color:#9ABDF5">(() </span><span style="color:#BB9AF7">=&gt;</span></span>
<span class="line"><span style="color:#C0CAF5">    document</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">documentElement</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">classList</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">contains</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">dark</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">  )</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toBe</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">true</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">})</span></span></code><button type="button" class="copy" data-code="// Fix for Mutant #1: Boundary test
it('volume slider has minimum value constraint of 50%', async () => {
  const volumeSlider = page.getByTestId('timer-sound-volume-slider')
  await expect.poll(async () => {
    const el = await volumeSlider.element()
    return el.getAttribute('min')
  }).toBe('0.5')
})

// Fix for Mutant #2: DOM verification
it('adds dark class to html element when dark mode enabled', async () => {
  const themeToggle = page.getByTestId('theme-toggle')
  await userEvent.click(themeToggle)

  await expect.poll(() =>
    document.documentElement.classList.contains('dark')
  ).toBe(true)
})" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr/>
<h2 id="how-to-set-this-up">How to Set This Up<a class="heading-link" aria-label="Link to section" href="#how-to-set-this-up"><span class="heading-link-icon">#</span></a></h2>
<h3 id="step-1-create-the-skill">Step 1: Create the Skill<a class="heading-link" aria-label="Link to section" href="#step-1-create-the-skill"><span class="heading-link-icon">#</span></a></h3>
<p>Save this as <code>.claude/skills/mutation-testing/SKILL.md</code>:</p>
<details><summary>Full Mutation Testing Skill (click to expand)</summary><pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"><span style="color:#F7768E">name</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> mutation-testing</span></span>
<span class="line"><span style="color:#F7768E">description</span><span style="color:#89DDFF">:</span><span style="color:#BB9AF7"> |</span></span>
<span class="line"><span style="color:#9ECE6A">  Mutation testing patterns for verifying test effectiveness. Use when analyzing branch code</span></span>
<span class="line"><span style="color:#9ECE6A">  to find weak or missing tests. Triggers: &quot;mutation testing&quot;, &quot;test effectiveness&quot;,</span></span>
<span class="line"><span style="color:#9ECE6A">  &quot;would tests catch this bug&quot;, &quot;weak tests&quot;, &quot;are my tests good enough&quot;, &quot;surviving mutants&quot;.</span></span>
<span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF;font-weight:bold">#</span><span style="color:#89DDFF;font-weight:bold"> Mutation Testing</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Mutation testing answers: </span><span style="color:#C0CAF5;font-weight:bold">**&quot;Would my tests catch this bug?&quot;**</span><span style="color:#9AA5CE"> by actually introducing bugs and running tests.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Execution Workflow</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**CRITICAL**</span><span style="color:#9AA5CE">: This skill actually mutates code and runs tests. Follow this exact process:</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Step 1: Identify Target Code</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">git diff main...HEAD --name-only | grep -E &#39;</span><span style="color:#89DDFF">\.</span><span style="color:#9AA5CE">(ts|js|tsx|jsx|vue)&#39; | grep -v &#39;</span><span style="color:#89DDFF">\.</span><span style="color:#9AA5CE">test</span><span style="color:#89DDFF">\.</span><span style="color:#9AA5CE">&#39; | grep -v &#39;</span><span style="color:#89DDFF">\.</span><span style="color:#9AA5CE">spec</span><span style="color:#89DDFF">\.</span><span style="color:#9AA5CE">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Step 2: For Each Function to Test</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Execute this loop for each mutation:</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">1.</span><span style="color:#9AA5CE"> READ the original file and note exact content</span></span>
<span class="line"><span style="color:#89DDFF">2.</span><span style="color:#9AA5CE"> APPLY one mutation (edit the code)</span></span>
<span class="line"><span style="color:#89DDFF">3.</span><span style="color:#9AA5CE"> RUN tests: pnpm test --run (or specific test file)</span></span>
<span class="line"><span style="color:#89DDFF">4.</span><span style="color:#9AA5CE"> RECORD result: KILLED (test failed) or SURVIVED (test passed)</span></span>
<span class="line"><span style="color:#89DDFF">5.</span><span style="color:#9AA5CE"> RESTORE original code immediately</span></span>
<span class="line"><span style="color:#89DDFF">6.</span><span style="color:#9AA5CE"> Repeat for next mutation</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Step 3: Report Results</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">After all mutations, provide a summary table:</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Mutation </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Location </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Result </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Action Needed </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|----------|----------|--------|---------------|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#89DDFF"> `&gt;`</span><span style="color:#C0CEFC"> → </span><span style="color:#89DDFF">`&gt;=`</span><span style="color:#89DDFF"> |</span><span style="color:#C0CEFC"> file.ts:42 </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> SURVIVED </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Add boundary test </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#89DDFF"> `&amp;&amp;`</span><span style="color:#C0CEFC"> → `</span><span style="color:#89DDFF">||</span><span style="color:#C0CEFC">` </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> file.ts:58 </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> KILLED </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> None </span><span style="color:#89DDFF">|</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-weight:bold">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Mutation Operators to Apply</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Priority 1: Boundary Mutations (Most Likely to Survive)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Original </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Mutate To </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Why It Matters </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|----------|-----------|----------------|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#89DDFF"> `&lt;`</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> `&lt;=`</span><span style="color:#89DDFF"> |</span><span style="color:#C0CEFC"> Boundary not tested </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#89DDFF"> `&gt;`</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> `&gt;=`</span><span style="color:#89DDFF"> |</span><span style="color:#C0CEFC"> Boundary not tested </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#89DDFF"> `&lt;=`</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> `&lt;`</span><span style="color:#89DDFF"> |</span><span style="color:#C0CEFC"> Equality case missed </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#89DDFF"> `&gt;=`</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> `&gt;`</span><span style="color:#89DDFF"> |</span><span style="color:#C0CEFC"> Equality case missed </span><span style="color:#89DDFF">|</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Priority 2: Boolean Logic Mutations</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Original </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Mutate To </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Why It Matters </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|----------|-----------|----------------|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#89DDFF"> `&amp;&amp;`</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> `\|\|`</span><span style="color:#89DDFF"> |</span><span style="color:#C0CEFC"> Only tested when both true </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#89DDFF"> `\|\|`</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> `&amp;&amp;`</span><span style="color:#89DDFF"> |</span><span style="color:#C0CEFC"> Only tested when both false </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#89DDFF"> `!condition`</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> `condition`</span><span style="color:#89DDFF"> |</span><span style="color:#C0CEFC"> Negation not verified </span><span style="color:#89DDFF">|</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Priority 3: Arithmetic Mutations</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Original </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Mutate To </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Why It Matters </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|----------|-----------|----------------|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#89DDFF"> `+`</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> `-`</span><span style="color:#89DDFF"> |</span><span style="color:#C0CEFC"> Tested with 0 only </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#89DDFF"> `-`</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> `+`</span><span style="color:#89DDFF"> |</span><span style="color:#C0CEFC"> Tested with 0 only </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#89DDFF"> `*`</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> `/`</span><span style="color:#89DDFF"> |</span><span style="color:#C0CEFC"> Tested with 1 only </span><span style="color:#89DDFF">|</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Priority 4: Return/Early Exit Mutations</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Original </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Mutate To </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Why It Matters </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|----------|-----------|----------------|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#89DDFF"> `return x`</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> `return null`</span><span style="color:#89DDFF"> |</span><span style="color:#C0CEFC"> Return value not asserted </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#89DDFF"> `return true`</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> `return false`</span><span style="color:#89DDFF"> |</span><span style="color:#C0CEFC"> Boolean return not checked </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#89DDFF"> `if (cond) return`</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> `// removed`</span><span style="color:#89DDFF"> |</span><span style="color:#C0CEFC"> Early exit not tested </span><span style="color:#89DDFF">|</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Priority 5: Statement Removal</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Original </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Mutate To </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Why It Matters </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|----------|-----------|----------------|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#89DDFF"> `array.push(x)`</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> `// removed`</span><span style="color:#89DDFF"> |</span><span style="color:#C0CEFC"> Side effect not verified </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#89DDFF"> `await save(x)`</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> `// removed`</span><span style="color:#89DDFF"> |</span><span style="color:#C0CEFC"> Async operation not verified </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#89DDFF"> `emit(&#39;event&#39;)`</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> `// removed`</span><span style="color:#89DDFF"> |</span><span style="color:#C0CEFC"> Event emission not tested </span><span style="color:#89DDFF">|</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-weight:bold">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Practical Execution Example</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Example: Testing a Validation Function</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**Original code**</span><span style="color:#9AA5CE"> (</span><span style="color:#89DDFF">`src/utils/validation.ts:15`</span><span style="color:#9AA5CE">):</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">export function isValidAge(age: number): boolean {</span></span>
<span class="line"><span style="color:#9AA5CE">  return age &gt;= 18 &amp;&amp; age &lt;= 120;</span></span>
<span class="line"><span style="color:#9AA5CE">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**Mutation 1**</span><span style="color:#9AA5CE">: Change </span><span style="color:#89DDFF">`&gt;=`</span><span style="color:#9AA5CE"> to </span><span style="color:#89DDFF">`&gt;`</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">export function isValidAge(age: number): boolean {</span></span>
<span class="line"><span style="color:#9AA5CE">  return age &gt; 18 &amp;&amp; age &lt;= 120;  // MUTATED</span></span>
<span class="line"><span style="color:#9AA5CE">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**Run tests**</span><span style="color:#9AA5CE">: </span><span style="color:#89DDFF">`pnpm test --run src/__tests__/validation.test.ts`</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**Result**</span><span style="color:#9AA5CE">: Tests PASS → </span><span style="color:#C0CAF5;font-weight:bold">**SURVIVED**</span><span style="color:#9AA5CE"> (Bad! Need test for </span><span style="color:#89DDFF">`isValidAge(18)`</span><span style="color:#9AA5CE">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**Restore original code immediately**</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**Mutation 2**</span><span style="color:#9AA5CE">: Change </span><span style="color:#89DDFF">`&amp;&amp;`</span><span style="color:#9AA5CE"> to </span><span style="color:#89DDFF">`||`</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">export function isValidAge(age: number): boolean {</span></span>
<span class="line"><span style="color:#9AA5CE">  return age &gt;= 18 || age &lt;= 120;  // MUTATED</span></span>
<span class="line"><span style="color:#9AA5CE">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**Run tests**</span><span style="color:#9AA5CE">: </span><span style="color:#89DDFF">`pnpm test --run src/__tests__/validation.test.ts`</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**Result**</span><span style="color:#9AA5CE">: Tests FAIL → </span><span style="color:#C0CAF5;font-weight:bold">**KILLED**</span><span style="color:#9AA5CE"> (Good! Tests catch this bug)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**Restore original code immediately**</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Results Interpretation</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Mutant States</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> State </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Meaning </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Action </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|-------|---------|--------|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CAF5;font-weight:bold"> **KILLED**</span><span style="color:#89DDFF"> |</span><span style="color:#C0CEFC"> Test failed with mutant </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Tests are effective </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CAF5;font-weight:bold"> **SURVIVED**</span><span style="color:#89DDFF"> |</span><span style="color:#C0CEFC"> Tests passed with mutant </span><span style="color:#89DDFF">|</span><span style="color:#C0CAF5;font-weight:bold"> **Add or strengthen test**</span><span style="color:#89DDFF"> |</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CAF5;font-weight:bold"> **TIMEOUT**</span><span style="color:#89DDFF"> |</span><span style="color:#C0CEFC"> Tests hung (infinite loop) </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Counts as detected </span><span style="color:#89DDFF">|</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Mutation Score</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Score = (Killed + Timeout) / Total Mutations * 100</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Score </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Quality </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|-------|---------|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> &lt; 60% </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Weak - significant test gaps </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> 60-80% </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Moderate - improvements needed </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> 80-90% </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Good - minor gaps </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> &gt; 90% </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Strong test suite </span><span style="color:#89DDFF">|</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-weight:bold">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Fixing Surviving Mutants</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">When a mutant survives, add a test that would catch it:</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Surviving: Boundary mutation (</span><span style="color:#89DDFF;font-weight:bold">`&gt;=`</span><span style="color:#7AA2F7;font-weight:bold"> → </span><span style="color:#89DDFF;font-weight:bold">`&gt;`</span><span style="color:#7AA2F7;font-weight:bold">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">// Add boundary test</span></span>
<span class="line"><span style="color:#9AA5CE">it(&#39;accepts exactly 18 years old&#39;, () =&gt; {</span></span>
<span class="line"><span style="color:#9AA5CE">  expect(isValidAge(18)).toBe(true);  // Would fail if &gt;= became &gt;</span></span>
<span class="line"><span style="color:#9AA5CE">});</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Surviving: Logic mutation (</span><span style="color:#89DDFF;font-weight:bold">`&amp;&amp;`</span><span style="color:#7AA2F7;font-weight:bold"> → </span><span style="color:#89DDFF;font-weight:bold">`||`</span><span style="color:#7AA2F7;font-weight:bold">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">// Add test with mixed conditions</span></span>
<span class="line"><span style="color:#9AA5CE">it(&#39;rejects when only one condition met&#39;, () =&gt; {</span></span>
<span class="line"><span style="color:#9AA5CE">  expect(isValidAge(15)).toBe(false);  // Would pass if &amp;&amp; became ||</span></span>
<span class="line"><span style="color:#9AA5CE">});</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Surviving: Statement removal</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">// Add side effect verification</span></span>
<span class="line"><span style="color:#9AA5CE">it(&#39;saves to database&#39;, async () =&gt; {</span></span>
<span class="line"><span style="color:#9AA5CE">  await processOrder(order);</span></span>
<span class="line"><span style="color:#9AA5CE">  expect(db.save).toHaveBeenCalledWith(order);  // Would fail if save removed</span></span>
<span class="line"><span style="color:#9AA5CE">});</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Quick Checklist During Mutation</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">For each mutation, ask:</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">1.</span><span style="color:#C0CAF5;font-weight:bold"> **Before mutating**</span><span style="color:#9AA5CE">: Does a test exist for this code path?</span></span>
<span class="line"><span style="color:#89DDFF">2.</span><span style="color:#C0CAF5;font-weight:bold"> **After running tests**</span><span style="color:#9AA5CE">: Did any test actually fail?</span></span>
<span class="line"><span style="color:#89DDFF">3.</span><span style="color:#C0CAF5;font-weight:bold"> **If survived**</span><span style="color:#9AA5CE">: What specific test would catch this?</span></span>
<span class="line"><span style="color:#89DDFF">4.</span><span style="color:#C0CAF5;font-weight:bold"> **After fixing**</span><span style="color:#9AA5CE">: Re-run mutation to confirm killed</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-weight:bold">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Common Surviving Mutation Patterns</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Tests Only Check Happy Path</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">// WEAK: Only tests success case</span></span>
<span class="line"><span style="color:#9AA5CE">it(&#39;validates&#39;, () =&gt; {</span></span>
<span class="line"><span style="color:#9AA5CE">  expect(validate(goodInput)).toBe(true);</span></span>
<span class="line"><span style="color:#9AA5CE">});</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">// STRONG: Tests both cases</span></span>
<span class="line"><span style="color:#9AA5CE">it(&#39;validates good input&#39;, () =&gt; {</span></span>
<span class="line"><span style="color:#9AA5CE">  expect(validate(goodInput)).toBe(true);</span></span>
<span class="line"><span style="color:#9AA5CE">});</span></span>
<span class="line"><span style="color:#9AA5CE">it(&#39;rejects bad input&#39;, () =&gt; {</span></span>
<span class="line"><span style="color:#9AA5CE">  expect(validate(badInput)).toBe(false);</span></span>
<span class="line"><span style="color:#9AA5CE">});</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Tests Use Identity Values</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">// WEAK: Mutation survives</span></span>
<span class="line"><span style="color:#9AA5CE">expect(multiply(5, 1)).toBe(5);  // 5*1 = 5/1 = 5</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">// STRONG: Mutation detected</span></span>
<span class="line"><span style="color:#9AA5CE">expect(multiply(5, 3)).toBe(15);  // 5*3 ≠ 5/3</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Tests Don&#39;t Assert Return Values</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">// WEAK: No return value check</span></span>
<span class="line"><span style="color:#9AA5CE">it(&#39;processes&#39;, () =&gt; {</span></span>
<span class="line"><span style="color:#9AA5CE">  process(data);  // No assertion!</span></span>
<span class="line"><span style="color:#9AA5CE">});</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">// STRONG: Asserts outcome</span></span>
<span class="line"><span style="color:#9AA5CE">it(&#39;processes&#39;, () =&gt; {</span></span>
<span class="line"><span style="color:#9AA5CE">  const result = process(data);</span></span>
<span class="line"><span style="color:#9AA5CE">  expect(result).toEqual(expected);</span></span>
<span class="line"><span style="color:#9AA5CE">});</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Important Rules</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">1.</span><span style="color:#C0CAF5;font-weight:bold"> **ALWAYS restore original code**</span><span style="color:#9AA5CE"> after each mutation</span></span>
<span class="line"><span style="color:#89DDFF">2.</span><span style="color:#C0CAF5;font-weight:bold"> **Run tests immediately**</span><span style="color:#9AA5CE"> after applying mutation</span></span>
<span class="line"><span style="color:#89DDFF">3.</span><span style="color:#C0CAF5;font-weight:bold"> **One mutation at a time**</span><span style="color:#9AA5CE"> - don&#39;t combine mutations</span></span>
<span class="line"><span style="color:#89DDFF">4.</span><span style="color:#C0CAF5;font-weight:bold"> **Focus on changed code**</span><span style="color:#9AA5CE"> - prioritize branch diff</span></span>
<span class="line"><span style="color:#89DDFF">5.</span><span style="color:#C0CAF5;font-weight:bold"> **Track all results**</span><span style="color:#9AA5CE"> - report full mutation summary</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-weight:bold">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Summary Report Template</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">After completing mutation testing, provide:</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Mutation Testing Results</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**Target**</span><span style="color:#9AA5CE">: </span><span style="color:#89DDFF">`src/features/workout/utils.ts`</span><span style="color:#9AA5CE"> (functions: X, Y, Z)</span></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**Total Mutations**</span><span style="color:#9AA5CE">: 12</span></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**Killed**</span><span style="color:#9AA5CE">: 9</span></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**Survived**</span><span style="color:#9AA5CE">: 3</span></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**Score**</span><span style="color:#9AA5CE">: 75%</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Surviving Mutants (Action Required)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> # </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Location </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Original </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Mutated </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Suggested Test </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|---|----------|----------|---------|----------------|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> 1 </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> line 42 </span><span style="color:#89DDFF">|</span><span style="color:#89DDFF"> `&gt;=`</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> `&gt;`</span><span style="color:#89DDFF"> |</span><span style="color:#C0CEFC"> Test boundary value </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> 2 </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> line 58 </span><span style="color:#89DDFF">|</span><span style="color:#89DDFF"> `&amp;&amp;`</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> `\|\|`</span><span style="color:#89DDFF"> |</span><span style="color:#C0CEFC"> Test mixed conditions </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> 3 </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> line 71 </span><span style="color:#89DDFF">|</span><span style="color:#89DDFF"> `emit()`</span><span style="color:#89DDFF"> |</span><span style="color:#C0CEFC"> removed </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Verify event emission </span><span style="color:#89DDFF">|</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Killed Mutants (Tests Effective)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Line 35: </span><span style="color:#89DDFF">`+`</span><span style="color:#9AA5CE"> → </span><span style="color:#89DDFF">`-`</span><span style="color:#9AA5CE"> killed by </span><span style="color:#89DDFF">`calculation.test.ts`</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Line 48: </span><span style="color:#89DDFF">`true`</span><span style="color:#9AA5CE"> → </span><span style="color:#89DDFF">`false`</span><span style="color:#9AA5CE"> killed by </span><span style="color:#89DDFF">`validate.test.ts`</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> ...</span></span></code><button type="button" class="copy" data-code="---
name: mutation-testing
description: |
  Mutation testing patterns for verifying test effectiveness. Use when analyzing branch code
  to find weak or missing tests. Triggers: &#34;mutation testing&#34;, &#34;test effectiveness&#34;,
  &#34;would tests catch this bug&#34;, &#34;weak tests&#34;, &#34;are my tests good enough&#34;, &#34;surviving mutants&#34;.
---

# Mutation Testing

Mutation testing answers: **&#34;Would my tests catch this bug?&#34;** by actually introducing bugs and running tests.

---

## Execution Workflow

**CRITICAL**: This skill actually mutates code and runs tests. Follow this exact process:

### Step 1: Identify Target Code

git diff main...HEAD --name-only | grep -E '\.(ts|js|tsx|jsx|vue)' | grep -v '\.test\.' | grep -v '\.spec\.'

### Step 2: For Each Function to Test

Execute this loop for each mutation:

1. READ the original file and note exact content
2. APPLY one mutation (edit the code)
3. RUN tests: pnpm test --run (or specific test file)
4. RECORD result: KILLED (test failed) or SURVIVED (test passed)
5. RESTORE original code immediately
6. Repeat for next mutation

### Step 3: Report Results

After all mutations, provide a summary table:

| Mutation | Location | Result | Action Needed |
|----------|----------|--------|---------------|
| `>` → `>=` | file.ts:42 | SURVIVED | Add boundary test |
| `&#38;&#38;` → `||` | file.ts:58 | KILLED | None |

---

## Mutation Operators to Apply

### Priority 1: Boundary Mutations (Most Likely to Survive)

| Original | Mutate To | Why It Matters |
|----------|-----------|----------------|
| `<` | `<=` | Boundary not tested |
| `>` | `>=` | Boundary not tested |
| `<=` | `<` | Equality case missed |
| `>=` | `>` | Equality case missed |

### Priority 2: Boolean Logic Mutations

| Original | Mutate To | Why It Matters |
|----------|-----------|----------------|
| `&#38;&#38;` | `\|\|` | Only tested when both true |
| `\|\|` | `&#38;&#38;` | Only tested when both false |
| `!condition` | `condition` | Negation not verified |

### Priority 3: Arithmetic Mutations

| Original | Mutate To | Why It Matters |
|----------|-----------|----------------|
| `+` | `-` | Tested with 0 only |
| `-` | `+` | Tested with 0 only |
| `*` | `/` | Tested with 1 only |

### Priority 4: Return/Early Exit Mutations

| Original | Mutate To | Why It Matters |
|----------|-----------|----------------|
| `return x` | `return null` | Return value not asserted |
| `return true` | `return false` | Boolean return not checked |
| `if (cond) return` | `// removed` | Early exit not tested |

### Priority 5: Statement Removal

| Original | Mutate To | Why It Matters |
|----------|-----------|----------------|
| `array.push(x)` | `// removed` | Side effect not verified |
| `await save(x)` | `// removed` | Async operation not verified |
| `emit('event')` | `// removed` | Event emission not tested |

---

## Practical Execution Example

### Example: Testing a Validation Function

**Original code** (`src/utils/validation.ts:15`):

export function isValidAge(age: number): boolean {
  return age >= 18 &#38;&#38; age <= 120;
}

**Mutation 1**: Change `>=` to `>`

export function isValidAge(age: number): boolean {
  return age > 18 &#38;&#38; age <= 120;  // MUTATED
}

**Run tests**: `pnpm test --run src/__tests__/validation.test.ts`

**Result**: Tests PASS → **SURVIVED** (Bad! Need test for `isValidAge(18)`)

**Restore original code immediately**

**Mutation 2**: Change `&#38;&#38;` to `||`

export function isValidAge(age: number): boolean {
  return age >= 18 || age <= 120;  // MUTATED
}

**Run tests**: `pnpm test --run src/__tests__/validation.test.ts`

**Result**: Tests FAIL → **KILLED** (Good! Tests catch this bug)

**Restore original code immediately**

---

## Results Interpretation

### Mutant States

| State | Meaning | Action |
|-------|---------|--------|
| **KILLED** | Test failed with mutant | Tests are effective |
| **SURVIVED** | Tests passed with mutant | **Add or strengthen test** |
| **TIMEOUT** | Tests hung (infinite loop) | Counts as detected |

### Mutation Score

Score = (Killed + Timeout) / Total Mutations * 100

| Score | Quality |
|-------|---------|
| < 60% | Weak - significant test gaps |
| 60-80% | Moderate - improvements needed |
| 80-90% | Good - minor gaps |
| > 90% | Strong test suite |

---

## Fixing Surviving Mutants

When a mutant survives, add a test that would catch it:

### Surviving: Boundary mutation (`>=` → `>`)

// Add boundary test
it('accepts exactly 18 years old', () => {
  expect(isValidAge(18)).toBe(true);  // Would fail if >= became >
});

### Surviving: Logic mutation (`&#38;&#38;` → `||`)

// Add test with mixed conditions
it('rejects when only one condition met', () => {
  expect(isValidAge(15)).toBe(false);  // Would pass if &#38;&#38; became ||
});

### Surviving: Statement removal

// Add side effect verification
it('saves to database', async () => {
  await processOrder(order);
  expect(db.save).toHaveBeenCalledWith(order);  // Would fail if save removed
});

---

## Quick Checklist During Mutation

For each mutation, ask:

1. **Before mutating**: Does a test exist for this code path?
2. **After running tests**: Did any test actually fail?
3. **If survived**: What specific test would catch this?
4. **After fixing**: Re-run mutation to confirm killed

---

## Common Surviving Mutation Patterns

### Tests Only Check Happy Path

// WEAK: Only tests success case
it('validates', () => {
  expect(validate(goodInput)).toBe(true);
});

// STRONG: Tests both cases
it('validates good input', () => {
  expect(validate(goodInput)).toBe(true);
});
it('rejects bad input', () => {
  expect(validate(badInput)).toBe(false);
});

### Tests Use Identity Values

// WEAK: Mutation survives
expect(multiply(5, 1)).toBe(5);  // 5*1 = 5/1 = 5

// STRONG: Mutation detected
expect(multiply(5, 3)).toBe(15);  // 5*3 ≠ 5/3

### Tests Don't Assert Return Values

// WEAK: No return value check
it('processes', () => {
  process(data);  // No assertion!
});

// STRONG: Asserts outcome
it('processes', () => {
  const result = process(data);
  expect(result).toEqual(expected);
});

---

## Important Rules

1. **ALWAYS restore original code** after each mutation
2. **Run tests immediately** after applying mutation
3. **One mutation at a time** - don't combine mutations
4. **Focus on changed code** - prioritize branch diff
5. **Track all results** - report full mutation summary

---

## Summary Report Template

After completing mutation testing, provide:

## Mutation Testing Results

**Target**: `src/features/workout/utils.ts` (functions: X, Y, Z)
**Total Mutations**: 12
**Killed**: 9
**Survived**: 3
**Score**: 75%

### Surviving Mutants (Action Required)

| # | Location | Original | Mutated | Suggested Test |
|---|----------|----------|---------|----------------|
| 1 | line 42 | `>=` | `>` | Test boundary value |
| 2 | line 58 | `&#38;&#38;` | `\|\|` | Test mixed conditions |
| 3 | line 71 | `emit()` | removed | Verify event emission |

### Killed Mutants (Tests Effective)

- Line 35: `+` → `-` killed by `calculation.test.ts`
- Line 48: `true` → `false` killed by `validate.test.ts`
- ..." onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre></details>
<h3 id="step-2-invoke-it">Step 2: Invoke It<a class="heading-link" aria-label="Link to section" href="#step-2-invoke-it"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#C0CAF5">claude</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">Run mutation testing on the settings feature</span><span style="color:#89DDFF">&quot;</span></span></code><button type="button" class="copy" data-code="claude &#34;Run mutation testing on the settings feature&#34;" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>The agent will:</p>
<ul>
<li>Find changed files on your branch</li>
<li>Identify testable functions</li>
<li>Apply mutations systematically</li>
<li>Report surviving mutants with suggested test fixes</li>
</ul>
<h3 id="step-3-review-and-fix">Step 3: Review and Fix<a class="heading-link" aria-label="Link to section" href="#step-3-review-and-fix"><span class="heading-link-icon">#</span></a></h3>
<p>The agent produces a markdown report. Review each surviving mutant and decide:</p>
<ul>
<li>Add the suggested test</li>
<li>Accept the risk (document why)</li>
<li>Refactor the code to be more testable</li>
</ul>
<hr/>
<h2 id="when-to-use-this-approach">When to Use This Approach<a class="heading-link" aria-label="Link to section" href="#when-to-use-this-approach"><span class="heading-link-icon">#</span></a></h2>





























<table><thead><tr><th>Good Fit</th><th>Not Ideal</th></tr></thead><tbody><tr><td data-label="Good Fit">Vitest browser mode (no Stryker support)</td><td data-label="Not Ideal">Large codebases needing full mutation coverage</td></tr><tr><td data-label="Good Fit">Playwright component testing</td><td data-label="Not Ideal">CI/CD automation (manual agent invocation)</td></tr><tr><td data-label="Good Fit">Small-to-medium codebases</td><td data-label="Not Ideal">Strict mutation score thresholds</td></tr><tr><td data-label="Good Fit">Pre-merge review of specific features</td><td data-label="Not Ideal"></td></tr><tr><td data-label="Good Fit">Learning what makes tests effective</td><td data-label="Not Ideal"></td></tr></tbody></table>
<div class="alert alert-tip astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">💪</span> Complement, Don&#39;t Replace </p> <div class="alert-content astro-7kdbuayl"> <p>This approach works best alongside your existing testing strategy. Use it to spot-check critical features before merge, not as a replacement for automated mutation testing where available.</p> </div> </div> 
<div class="alert alert-info astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl"></span> Feature Branches, Not Pipelines </p> <div class="alert-content astro-7kdbuayl"> <p>This skill shines on <strong>feature branches</strong> where you want to validate test quality before merging. Running AI agents in CI/CD pipelines is possible—you could build <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/building_ai_qa_engineer_claude_code_playwright/" class="internal-link astro-3tyn5ojg"> an automated QA agent </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Building an AI QA Engineer with Claude Code and Playwright MCP</span> <span class="preview-description astro-3tyn5ojg">Learn how to build an automated QA engineer using Claude Code and Playwright MCP that tests your web app like a real user, runs on every pull request, and writes detailed bug reports.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">ai</span><span class="preview-tag astro-3tyn5ojg">testing</span><span class="preview-tag astro-3tyn5ojg">claude-code</span> <span class="preview-tag-more astro-3tyn5ojg">+1</span> </span> <time class="preview-date astro-3tyn5ojg">Dec 13, 2025</time> </span> </span> </span>  <script>
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
</script> with the Claude Agent SDK—but it adds complexity and cost. For pipeline automation, deterministic tools like Stryker remain the better choice when your stack supports them. Think of this as a developer tool for improving tests during development, not a CI gate.</p> </div> </div> 
<hr/>
<h2 id="key-takeaways">Key Takeaways<a class="heading-link" aria-label="Link to section" href="#key-takeaways"><span class="heading-link-icon">#</span></a></h2>
<ol>
<li>
<p><strong>Coverage doesn’t equal confidence.</strong> High code coverage can coexist with ineffective tests.</p>
</li>
<li>
<p><strong>Mutation testing reveals test gaps.</strong> By breaking code and checking if tests notice, you find what’s actually being verified.</p>
</li>
<li>
<p><strong>AI agents can execute manual mutation testing.</strong> When tooling doesn’t support your stack, an agent can apply the algorithm systematically.</p>
</li>
<li>
<p><strong>Focus on surviving mutants.</strong> Each one is a potential bug your tests wouldn’t catch.</p>
</li>
<li>
<p><strong>This complements, not replaces.</strong> Use this alongside coverage reports, not instead of automated mutation testing where available.</p>
</li>
</ol>
<hr/>
<h2 id="resources">Resources<a class="heading-link" aria-label="Link to section" href="#resources"><span class="heading-link-icon">#</span></a></h2>
<ul>
<li><a href="https://github.com/citypaul/.dotfiles/blob/main/claude/.claude/skills/mutation-testing/SKILL.md" rel="noopener noreferrer" target="_blank">Paul Hammond’s Mutation Testing Skill</a> - The original skill this post is based on</li>
<li><a href="https://en.wikipedia.org/wiki/Mutation_testing" rel="noopener noreferrer" target="_blank">Mutation Testing on Wikipedia</a></li>
<li><a href="https://stryker-mutator.io/" rel="noopener noreferrer" target="_blank">Stryker Mutator</a> - When your stack supports it</li>
<li><span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/custom-tdd-workflow-claude-code-vue/" class="internal-link astro-3tyn5ojg"> My TDD workflow with Claude Code </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Forcing Claude Code to TDD: An Agentic Red-Green-Refactor Loop</span> <span class="preview-description astro-3tyn5ojg">Build a custom TDD workflow with Claude Code using skills and subagents that enforce Red-Green-Refactor discipline for your Vue projects.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">ai</span><span class="preview-tag astro-3tyn5ojg">vue</span><span class="preview-tag astro-3tyn5ojg">testing</span> <span class="preview-tag-more astro-3tyn5ojg">+1</span> </span> <time class="preview-date astro-3tyn5ojg">Nov 30, 2025</time> </span> </span> </span>  <script>
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
</script> - Related approach for test-first development</li>
</ul> </article> <script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).only=e;window.dispatchEvent(new Event("astro:only"));})();</script><astro-island uid="Z1XneyL" component-url="/_astro/presentation.C3Wa0mjp.js" component-export="VMarkBlogRenderer" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;containerSelector&quot;:[0,&quot;#article&quot;],&quot;class&quot;:[0,&quot;astro-vj4tpspi&quot;]}" ssr client="only" opts="{&quot;name&quot;:&quot;VMarkBlogRenderer&quot;,&quot;value&quot;:&quot;react&quot;}"></astro-island> <!-- Fullscreen Modal Container using native dialog --><dialog id="mermaid-modal" class="mermaid-modal" aria-label="Fullscreen diagram view"> <div class="mermaid-modal-content"> <button class="mermaid-modal-close" aria-label="Close fullscreen view" type="button"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <line x1="18" y1="6" x2="6" y2="18"></line> <line x1="6" y1="6" x2="18" y2="18"></line> </svg> </button> <div class="mermaid-modal-diagram"></div> <div class="mermaid-modal-hint">Press <kbd>Esc</kbd> or click outside to close</div> </div> </dialog>  <script type="module">const p=new Set;function g(){const e=document.getElementById("mermaid-modal"),c=e?.querySelector(".mermaid-modal-diagram"),f=e?.querySelector(".mermaid-modal-close");if(!e||!c)return;document.querySelectorAll('svg[id^="mermaid-"]').forEach(t=>{if(!t.id.match(/^mermaid-\d+$/)||p.has(t.id)||t.parentElement?.classList.contains("mermaid-fullscreen-wrapper")||t.closest(".mermaid-modal"))return;p.add(t.id);const n=document.createElement("div");n.className="mermaid-fullscreen-wrapper mermaid-clickable",n.setAttribute("tabindex","0"),n.setAttribute("role","button"),n.setAttribute("aria-label","Click to view diagram fullscreen"),t.parentElement?.insertBefore(n,t),n.appendChild(t);const o=document.createElement("div");o.className="mermaid-expand-icon",o.innerHTML=`
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
</li> <li class="astro-vj4tpspi">Small tips and trick</li> </ul> </div> <a href="https://alex-op-newsletter.beehiiv.com/subscribe?utm_source=blog&utm_medium=post&utm_campaign=post_mutation-testing-ai-agents-vitest-browser-mode" target="_blank" rel="noopener noreferrer" id="newsletter-subscribe-button" class="inline-flex items-center justify-center gap-2 rounded-full bg-skin-accent px-6 py-3 text-base font-semibold text-skin-inverted shadow-md transition-all duration-200 hover:scale-[1.02] hover:transform hover:opacity-90 astro-vj4tpspi"> <svg class="h-5 w-5 fill-current astro-vj4tpspi" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg>
Subscribe Now
</a> <button id="newsletter-dismiss" data-post-slug="mutation-testing-ai-agents-vitest-browser-mode" class="absolute right-3 top-3 rounded-full p-1 text-skin-base transition-all duration-200 hover:bg-skin-accent hover:bg-opacity-10 hover:text-skin-accent astro-vj4tpspi" aria-label="Close notification"> <svg class="h-5 w-5 astro-vj4tpspi" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class="astro-vj4tpspi"></path> </svg> </button> </div> </div> </div> <ul class="my-8 flex flex-wrap gap-2 astro-vj4tpspi"> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/testing/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-2"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">testing</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/ai/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-3"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">ai</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/claude-code/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-4"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">claude-code</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/vitest/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-5"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">vitest</span>   </a> </li>  </ul> <div class="flex flex-col-reverse items-center justify-between gap-6 sm:flex-row-reverse sm:items-end sm:gap-4 astro-vj4tpspi"> <button id="back-to-top" class="focus-outline whitespace-nowrap py-1 hover:opacity-75 astro-vj4tpspi"> <svg xmlns="http://www.w3.org/2000/svg" class="rotate-90 astro-vj4tpspi"> <path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg> <span class="astro-vj4tpspi">Back to Top</span> </button> <div class="social-icons astro-wkojbtzc"> <span class="italic astro-wkojbtzc">Share this post on:</span> <div class="text-center astro-wkojbtzc"> <a href="https://wa.me/?text=https://alexop.dev/posts/mutation-testing-ai-agents-vitest-browser-mode/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via WhatsApp" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"></path>
      <path d="M9 10a0.5 .5 0 0 0 1 0v-1a0.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a0.5 .5 0 0 0 0 -1h-1a0.5 .5 0 0 0 0 1"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via WhatsApp</span> </a><a href="https://www.facebook.com/sharer.php?u=https://alexop.dev/posts/mutation-testing-ai-agents-vitest-browser-mode/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Facebook" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"
    ></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on Facebook</span> </a><a href="https://x.com/intent/tweet?url=https://alexop.dev/posts/mutation-testing-ai-agents-vitest-browser-mode/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Tweet this post" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Tweet this post</span> </a><a href="https://t.me/share/url?url=https://alexop.dev/posts/mutation-testing-ai-agents-vitest-browser-mode/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via Telegram" target="_blank" rel="noopener noreferrer"> <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon-tabler"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"></path>
      </svg> <span class="sr-only astro-wkojbtzc">Share this post via Telegram</span> </a><a href="https://pinterest.com/pin/create/button/?url=https://alexop.dev/posts/mutation-testing-ai-agents-vitest-browser-mode/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Pinterest" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <line x1="8" y1="20" x2="12" y2="11"></line>
      <path d="M10.7 14c.437 1.263 1.43 2 2.55 2c2.071 0 3.75 -1.554 3.75 -4a5 5 0 1 0 -9.7 1.7"></path>
      <circle cx="12" cy="12" r="9"></circle>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post on Pinterest</span> </a><a href="mailto:?subject=See%20this%20post&#38;body=https://alexop.dev/posts/mutation-testing-ai-agents-vitest-browser-mode/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via email" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via email</span> </a><a href="https://www.linkedin.com/shareArticle?mini=true&url=https://alexop.dev/posts/mutation-testing-ai-agents-vitest-browser-mode/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
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
    </script> </body> </html>  <script>(function(){const postSlug = "mutation-testing-ai-agents-vitest-browser-mode";

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
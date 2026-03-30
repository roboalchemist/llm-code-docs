# Source: https://alexop.dev/posts/supercharging-reading-comprehension-claude-readwise

<!DOCTYPE html><html lang="en" class="scroll-smooth astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/posts/supercharging-reading-comprehension-claude-readwise/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>Unlocking Reading Insights: A Guide to Data Analysis with Claude and Readwise | alexop.dev</title><meta name="title" content="Unlocking Reading Insights: A Guide to Data Analysis with Claude and Readwise | alexop.dev"><meta name="description" content="Discover how to transform your reading data into actionable insights by combining Readwise exports with Claude AI's powerful analysis capabilities"><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="Unlocking Reading Insights: A Guide to Data Analysis with Claude and Readwise | alexop.dev"><meta property="og:description" content="Discover how to transform your reading data into actionable insights by combining Readwise exports with Claude AI's powerful analysis capabilities"><meta property="og:url" content="https://alexop.dev/posts/supercharging-reading-comprehension-claude-readwise/"><meta property="og:image" content="https://alexop.dev/posts/unlocking-reading-insights-a-guide-to-data-analysis-with-claude-and-readwise/index.png"><meta property="og:type" content="article"><!-- Article Published/Modified time --><meta property="article:published_time" content="2025-01-05T00:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/posts/supercharging-reading-comprehension-claude-readwise/"><meta property="twitter:title" content="Unlocking Reading Insights: A Guide to Data Analysis with Claude and Readwise | alexop.dev"><meta property="twitter:description" content="Discover how to transform your reading data into actionable insights by combining Readwise exports with Claude AI's powerful analysis capabilities"><meta property="twitter:image" content="https://alexop.dev/posts/unlocking-reading-insights-a-guide-to-data-analysis-with-claude-and-readwise/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"Unlocking Reading Insights: A Guide to Data Analysis with Claude and Readwise | alexop.dev","description":"Discover how to transform your reading data into actionable insights by combining Readwise exports with Claude AI's powerful analysis capabilities","image":"https://alexop.dev/posts/unlocking-reading-insights-a-guide-to-data-analysis-with-claude-and-readwise/index.png","datePublished":"2025-01-05T00:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
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
</style><style>[data-astro-transition-scope="astro-plk3gbjq-1"] { view-transition-name: unlocking-reading-insights-a-guide-to-data-analysis-with-claude-and-readwise; }@layer astro { ::view-transition-old(unlocking-reading-insights-a-guide-to-data-analysis-with-claude-and-readwise) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(unlocking-reading-insights-a-guide-to-data-analysis-with-claude-and-readwise) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(unlocking-reading-insights-a-guide-to-data-analysis-with-claude-and-readwise) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(unlocking-reading-insights-a-guide-to-data-analysis-with-claude-and-readwise) { 
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
	animation-name: astroFadeIn; }</style><style>.gif-container:where(.astro-t73tit66){margin:2rem auto;text-align:center;max-width:800px;width:100%}.gif-wrapper:where(.astro-t73tit66){position:relative;border-radius:.5rem;overflow:hidden;background:var(--card);box-shadow:0 4px 6px -1px #0000001a,0 2px 4px -2px #0000001a;aspect-ratio:16 / 10}.gif-wrapper:where(.astro-t73tit66) img:where(.astro-t73tit66){width:100%;height:100%;-o-object-fit:cover;object-fit:cover;display:block}figcaption:where(.astro-t73tit66){margin-top:.75rem;font-style:italic;color:var(--text-base);font-size:.95rem;line-height:1.4}.dark .gif-wrapper:where(.astro-t73tit66){background:var(--card)}@media(max-width:840px){.gif-container:where(.astro-t73tit66){max-width:100%;margin:2rem 0}}
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-3"] { view-transition-name: productivity; }@layer astro { ::view-transition-old(productivity) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(productivity) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(productivity) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(productivity) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-4"] { view-transition-name: reading; }@layer astro { ::view-transition-old(reading) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(reading) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(reading) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(reading) { 
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <div class="mx-auto flex w-full max-w-5xl justify-start px-2 astro-vj4tpspi"> <button class="focus-outline mb-2 mt-8 flex hover:opacity-75 astro-vj4tpspi" onclick="(() => (history.length === 1) ? window.location = '/' : history.back())()"> <svg xmlns="http://www.w3.org/2000/svg" class="astro-vj4tpspi"><path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg><span class="astro-vj4tpspi">Go back</span> </button> </div> <main data-pagefind-body id="main-content" class="relative astro-vj4tpspi"> <h1 class="post-title astro-vj4tpspi" data-astro-transition-scope="astro-plk3gbjq-1">Unlocking Reading Insights: A Guide to Data Analysis with Claude and Readwise</h1> <div class="my-2 flex items-center justify-between astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-100 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-base"><time dateTime="2025-01-05T00:00:00.000Z">Jan 5, 2025</time><span class="sr-only"> at </span></span></div> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="wyII4" prefix="r3" component-url="/_astro/PostCopyButton.-PGtk4At.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;title&quot;:[0,&quot;Unlocking Reading Insights: A Guide to Data Analysis with Claude and Readwise&quot;],&quot;content&quot;:[0,&quot;import AstroGif from \&quot;@features/mdx-components/components/AstroGif.astro\&quot;;\n\nRecently, I&#39;ve been exploring Claude.ai&#39;s new CSV analysis feature, which allows you to upload spreadsheet data for automated analysis and visualization. In this blog post, I&#39;ll demonstrate how to leverage Claude.ai&#39;s capabilities using Readwise data as an example. We&#39;ll explore how crafting better prompts can help you extract more meaningful insights from your data. Additionally, we&#39;ll peek under the hood to understand the technical aspects of how Claude processes and analyzes this information.\n\nReadwise is a powerful application that syncs and organizes highlights from your Kindle and other reading platforms. While this tutorial uses Readwise data as an example, the techniques demonstrated here can be applied to analyze any CSV dataset with Claude.\n\n## The Process: From Highlights to Insights\n\n### 1. Export and Initial Setup\n\nFirst things first: export your Readwise highlights as CSV.\nJust login into your Readwise account and go to -&gt; https://readwise.io/export\nScroll down to the bottom and click on \&quot;Export to CSV\&quot;\n![Readwise Export CSV](../../assets/images/readwise_claude_csv/readwise_export_csv.png)\n\n### 2. Upload the CSV into Claude\n\nDrop that CSV into Claude&#39;s interface. Yes, it&#39;s that simple. No need for complex APIs or coding knowledge.\n\n&gt; Note: The CSV file must fit within Claude&#39;s conversation context window. For very large export files, you may need to split them into smaller chunks.\n\n### 3. Use Prompts to analyze the data\n\n#### a) First Approach\n\nFirst we will use a generic Prompt to see what would happen if we don&#39;t even know what to analyze for:\n\n```plaintext\nPlease Claude, analyze this data for me.\n```\n\n&lt;AstroGif\n  src=\&quot;/images/readwise_claude_csv/claude_first_prompt.gif\&quot;\n  alt=\&quot;Claude first prompt response\&quot;\n  caption=\&quot;Claude analyzing the initial prompt and providing a structured response\&quot;\n/&gt;\n\nClaude analyzed my Readwise data and provided a high-level overview:\n\n- Collection stats: 1,322 highlights across 131 books by 126 authors from 2018-2024\n- Most highlighted books focused on writing and note-taking, with \&quot;How to Take Smart Notes\&quot; leading at 102 highlights\n- Tag analysis showed \&quot;discard\&quot; as most common (177), followed by color tags and topical tags like \&quot;mental\&quot; and \&quot;tech\&quot;\n\nClaude also offered to dive deeper into highlight lengths, reading patterns over time, tag relationships, and data visualization.\nEven with this basic prompt, Claude provides valuable insights and analysis. The initial overview can spark ideas for deeper investigation and more targeted analysis. However, we can craft more specific prompts to extract even more meaningful insights from our data.\n\n### 4. Visualization and Analysis\n\nWhile our last Prompt did give use some insights, it was not very useful for me.\nAlso I am a visual person, so I want to see some visualizations.\n\nThis is why I created this Prompt to get better Visualization I also added the Colors\nfrom this blog since I love them.\n\n```plaintext\nCreate a responsive data visualization dashboard for my Readwise highlights using React and Recharts.\n\nTheme Colors (Dark Mode):\n- Background: rgb(33, 39, 55)\n- Text: rgb(234, 237, 243)\n- Accent: rgb(255, 107, 237)\n- Card Background: rgb(52, 63, 96)\n- Muted Elements: rgb(138, 51, 123)\n- Borders: rgb(171, 75, 153)\n\nColor Application:\n- Use background color for main dashboard\n- Apply text color for all typography\n- Use accent color for interactive elements and highlights\n- Apply card background for visualization containers\n- Use muted colors for secondary information\n- Implement borders for section separation\n\nInput Data Structure:\n- CSV format with columns:\n  - Highlight text\n  - Book Title\n  - Book Author\n  - Color\n  - Tags\n  - Location\n  - Highlighted Date\n\nRequired Visualizations:\n1. Reading Analytics:\n   - Average reading time per book (calculated from highlight timestamps)\n   - Reading patterns by time of day (heatmap using card background and accent colors)\n   - Heat map showing active reading days\n     - Base: rgb(52, 63, 96)\n     - Intensity levels: rgb(138, 51, 123) → rgb(255, 107, 237)\n\n2. Content Analysis:\n   - Vertical bar chart: Top 10 most highlighted books\n   - Bars: gradient from rgb(138, 51, 123) to rgb(255, 107, 237)\n   - Labels: rgb(234, 237, 243)\n   - Grid lines: rgba(171, 75, 153, 0.2)\n\n3. Timeline View:\n   - Monthly highlighting activity\n   - Line color: rgb(255, 107, 237)\n   - Area fill: rgba(255, 107, 237, 0.1)\n   - Grid: rgba(171, 75, 153, 0.15)\n\n4. Knowledge Map:\n   - Interactive mind map using force-directed graph\n   - Node colors: rgb(52, 63, 96)\n   - Node borders: rgb(171, 75, 153)\n   - Connections: rgba(255, 107, 237, 0.6)\n   - Hover state: rgb(255, 107, 237)\n\n5. Summary Statistics Card:\n   - Background: rgb(52, 63, 96)\n   - Border: rgb(171, 75, 153)\n   - Headings: rgb(234, 237, 243)\n   - Values: rgb(255, 107, 237)\n\nDesign Requirements:\n- Typography:\n  - Primary font: Light text on dark background\n  - Base text: rgb(234, 237, 243)\n  - Minimum 16px for body text\n  - Headings: rgb(255, 107, 237)\n\n- Card Design:\n  - Background: rgb(52, 63, 96)\n  - Border: 1px solid rgb(171, 75, 153)\n  - Border radius: 8px\n  - Box shadow: 0 4px 6px rgba(0, 0, 0, 0.1)\n\n- Interaction States:\n  - Hover: Accent color rgb(255, 107, 237)\n  - Active: rgb(138, 51, 123)\n  - Focus: 2px solid rgb(255, 107, 237)\n\n- Responsive Design:\n  - Desktop: Grid layout with 2-3 columns\n  - Tablet: 2 columns\n  - Mobile: Single column, stacked\n  - Gap: 1.5rem\n  - Padding: 2rem\n\nAccessibility:\n- Ensure contrast ratio ≥ 4.5:1 with text color\n- Use rgba(234, 237, 243, 0.7) for secondary text\n- Provide focus indicators using accent color\n- Include aria-labels for interactive elements\n- Support keyboard navigation\n\nPerformance:\n- Implement CSS variables for theme colors\n- Use CSS transitions for hover states\n- Optimize SVG rendering for mind map\n- Implement virtualization for large datasets\n```\n\n&lt;AstroGif\n  src=\&quot;/images/readwise_claude_csv/readwise_analytics.gif\&quot;\n  alt=\&quot;Claude second prompt response\&quot;\n  caption=\&quot;Interactive dashboard visualization of Readwise highlights analysis\&quot;\n/&gt;\n\nThe interactive dashboard generated by Claude demonstrates the powerful synergy between generative AI and data analysis.\nBy combining Claude&#39;s natural language processing capabilities with programmatic visualization, we can transform raw reading data into actionable insights. This approach allows us to extract meaningful patterns and trends that would be difficult to identify through manual analysis alone.\n\nNow I want to give you some tips on how to get the best out of claude.\n\n## Writing Effective Analysis Prompts\n\nHere are key principles for crafting prompts that generate meaningful insights:\n\n### 1. Start with Clear Objectives\n\nInstead of vague requests, specify what you want to learn:\n\n```plaintext\nAnalyze my reading data to identify:\n1. Time-of-day reading patterns\n2. Most engaged topics\n3. Knowledge connection opportunities\n4. Potential learning gaps\n```\n\n### 2. Use Role-Based Prompting\n\nGive Claude a specific expert perspective:\n\n```plaintext\nAct as a learning science researcher analyzing my reading patterns.\nFocus on:\n- Comprehension patterns\n- Knowledge retention indicators\n- Learning efficiency metrics\n```\n\n### 3. Request Specific Visualizations\n\nBe explicit about the visual insights you need:\n\n```plaintext\nCreate visualizations showing:\n1. Daily reading heatmap\n2. Topic relationship network\n3. Highlight frequency trends\nUse theme-consistent colors for clarity\n```\n\n## Bonus: Behind the Scenes - How the Analysis Tool Works\n\nFor those curious about the technical implementation, let&#39;s peek under the hood at how Claude uses the analysis tool to process your Readwise data:\n\n### The JavaScript Runtime Environment\n\nWhen you upload your Readwise CSV, Claude has access to a JavaScript runtime environment similar to a browser&#39;s console. This environment comes pre-loaded with several powerful libraries:\n\n```javascript\n// Available libraries\nimport Papa from \&quot;papaparse\&quot;; // For CSV processing\nimport _ from \&quot;lodash\&quot;; // For data manipulation\nimport React from \&quot;react\&quot;; // For UI components\nimport { BarChart, LineChart, PieChart } from \&quot;recharts\&quot;; // For visualizations\n```\n\n### Data Processing Pipeline\n\nThe analysis happens in two main stages:\n\n1. **Initial Data Processing:**\n\n```javascript\nasync function analyzeReadingData() {\n  // Read the CSV file\n  const fileContent = await window.fs.readFile(\&quot;readwisedata.csv\&quot;, {\n    encoding: \&quot;utf8\&quot;,\n  });\n\n  // Parse CSV using Papaparse\n  const parsedData = Papa.parse(fileContent, {\n    header: true,\n    skipEmptyLines: true,\n    dynamicTyping: true,\n  });\n\n  // Analyze time patterns\n  const timeAnalysis = parsedData.data.map(row =&gt; {\n    const date = new Date(row[\&quot;Highlighted at\&quot;]);\n    return {\n      hour: date.getHours(),\n      title: row[\&quot;Book Title\&quot;],\n      tags: row[\&quot;Tags\&quot;],\n    };\n  });\n\n  // Group and count data using lodash\n  const hourlyDistribution = _.countBy(timeAnalysis, \&quot;hour\&quot;);\n  console.log(\&quot;Reading time distribution:\&quot;, hourlyDistribution);\n}\n```\n\n2. **Visualization Component:**\n\n```javascript\nconst ReadingPatterns = () =&gt; {\n  const [timeData, setTimeData] = useState([]);\n  const [topBooks, setTopBooks] = useState([]);\n\n  useEffect(() =&gt; {\n    const analyzeData = async () =&gt; {\n      const response = await window.fs.readFile(\&quot;readwisedata.csv\&quot;, {\n        encoding: \&quot;utf8\&quot;,\n      });\n\n      // Process time data for visualization\n      const timeAnalysis = parsedData.data.reduce((acc, row) =&gt; {\n        const hour = new Date(row[\&quot;Highlighted at\&quot;]).getHours();\n        acc[hour] = (acc[hour] || 0) + 1;\n        return acc;\n      }, {});\n\n      // Format data for charts\n      const timeDataForChart = Object.entries(timeAnalysis).map(\n        ([hour, count]) =&gt; ({\n          hour: `${hour}:00`,\n          count,\n        })\n      );\n\n      setTimeData(timeDataForChart);\n    };\n    analyzeData();\n  }, []);\n\n  return (\n    &lt;div className=\&quot;w-full space-y-8 p-4\&quot;&gt;\n      &lt;ResponsiveContainer width=\&quot;100%\&quot; height=\&quot;100%\&quot;&gt;\n        &lt;BarChart data={timeData}&gt;\n          &lt;CartesianGrid strokeDasharray=\&quot;3 3\&quot; /&gt;\n          &lt;XAxis dataKey=\&quot;hour\&quot; /&gt;\n          &lt;YAxis /&gt;\n          &lt;Bar dataKey=\&quot;count\&quot; fill=\&quot;#4F46E5\&quot; /&gt;\n        &lt;/BarChart&gt;\n      &lt;/ResponsiveContainer&gt;\n    &lt;/div&gt;\n  );\n};\n```\n\n### Key Technical Features\n\n1. **Asynchronous File Handling**: The `window.fs.readFile` API provides async file access, similar to Node.js&#39;s fs/promises.\n\n2. **Data Processing Libraries**:\n   - Papaparse handles CSV parsing with options for headers and type conversion\n   - Lodash provides efficient data manipulation functions\n   - React and Recharts enable interactive visualizations\n\n3. **React Integration**:\n   - Components use hooks for state management\n   - Tailwind classes for styling\n   - Responsive container adapts to screen size\n\n4. **Error Handling**: The code includes proper error boundaries and async/await patterns to handle potential issues gracefully.\n\nThis technical implementation allows Claude to process your reading data efficiently while providing interactive visualizations that help you understand your reading patterns better.\n\n## Conclusion\n\nI hope this blog post demonstrates how AI can accelerate data analysis workflows. What previously required significant time and technical expertise can now be accomplished in minutes. This democratization of data analysis empowers people without coding backgrounds to gain valuable insights from their own data.&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PostCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus-outline inline-flex items-center gap-1.5 rounded-md border border-skin-line bg-skin-card px-2.5 py-1.5 text-xs font-medium text-skin-base opacity-80 transition-all hover:border-skin-accent/50 hover:text-skin-accent hover:opacity-100" aria-label="Copy post as markdown" title="Copy post as markdown for AI/LLM"><svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg><span>Copy Post</span></button><!--astro:end--></astro-island> </div>  <article id="article" class="prose mx-auto mt-8 max-w-5xl astro-vj4tpspi"> <p>Recently, I’ve been exploring Claude.ai’s new CSV analysis feature, which allows you to upload spreadsheet data for automated analysis and visualization. In this blog post, I’ll demonstrate how to leverage Claude.ai’s capabilities using Readwise data as an example. We’ll explore how crafting better prompts can help you extract more meaningful insights from your data. Additionally, we’ll peek under the hood to understand the technical aspects of how Claude processes and analyzes this information.</p>
<p>Readwise is a powerful application that syncs and organizes highlights from your Kindle and other reading platforms. While this tutorial uses Readwise data as an example, the techniques demonstrated here can be applied to analyze any CSV dataset with Claude.</p>
<h2 id="the-process-from-highlights-to-insights">The Process: From Highlights to Insights<a class="heading-link" aria-label="Link to section" href="#the-process-from-highlights-to-insights"><span class="heading-link-icon">#</span></a></h2>
<h3 id="1-export-and-initial-setup">1. Export and Initial Setup<a class="heading-link" aria-label="Link to section" href="#1-export-and-initial-setup"><span class="heading-link-icon">#</span></a></h3>
<p>First things first: export your Readwise highlights as CSV.
Just login into your Readwise account and go to -&gt; <a href="https://readwise.io/export" rel="noopener noreferrer" target="_blank">https://readwise.io/export</a>
Scroll down to the bottom and click on “Export to CSV”
<img src="/_astro/readwise_export_csv.DwYry6bY_20bXGA.webp" alt="Readwise Export CSV" loading="lazy" decoding="async" fetchpriority="auto" width="1602" height="582"></p>
<h3 id="2-upload-the-csv-into-claude">2. Upload the CSV into Claude<a class="heading-link" aria-label="Link to section" href="#2-upload-the-csv-into-claude"><span class="heading-link-icon">#</span></a></h3>
<p>Drop that CSV into Claude’s interface. Yes, it’s that simple. No need for complex APIs or coding knowledge.</p>
<blockquote>
<p>Note: The CSV file must fit within Claude’s conversation context window. For very large export files, you may need to split them into smaller chunks.</p>
</blockquote>
<h3 id="3-use-prompts-to-analyze-the-data">3. Use Prompts to analyze the data<a class="heading-link" aria-label="Link to section" href="#3-use-prompts-to-analyze-the-data"><span class="heading-link-icon">#</span></a></h3>
<h4 id="a-first-approach">a) First Approach<a class="heading-link" aria-label="Link to section" href="#a-first-approach"><span class="heading-link-icon">#</span></a></h4>
<p>First we will use a generic Prompt to see what would happen if we don’t even know what to analyze for:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="plaintext"><code><span class="line"><span>Please Claude, analyze this data for me.</span></span></code><button type="button" class="copy" data-code="Please Claude, analyze this data for me." onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<figure class="gif-container astro-t73tit66"> <div class="gif-wrapper astro-t73tit66"> <img src="/images/readwise_claude_csv/claude_first_prompt.gif" alt="Claude first prompt response" width="800" height="500" loading="lazy" class="astro-t73tit66"> </div> <figcaption class="astro-t73tit66">Claude analyzing the initial prompt and providing a structured response</figcaption> </figure> 
<p>Claude analyzed my Readwise data and provided a high-level overview:</p>
<ul>
<li>Collection stats: 1,322 highlights across 131 books by 126 authors from 2018-2024</li>
<li>Most highlighted books focused on writing and note-taking, with “How to Take Smart Notes” leading at 102 highlights</li>
<li>Tag analysis showed “discard” as most common (177), followed by color tags and topical tags like “mental” and “tech”</li>
</ul>
<p>Claude also offered to dive deeper into highlight lengths, reading patterns over time, tag relationships, and data visualization.
Even with this basic prompt, Claude provides valuable insights and analysis. The initial overview can spark ideas for deeper investigation and more targeted analysis. However, we can craft more specific prompts to extract even more meaningful insights from our data.</p>
<h3 id="4-visualization-and-analysis">4. Visualization and Analysis<a class="heading-link" aria-label="Link to section" href="#4-visualization-and-analysis"><span class="heading-link-icon">#</span></a></h3>
<p>While our last Prompt did give use some insights, it was not very useful for me.
Also I am a visual person, so I want to see some visualizations.</p>
<p>This is why I created this Prompt to get better Visualization I also added the Colors
from this blog since I love them.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="plaintext"><code><span class="line"><span>Create a responsive data visualization dashboard for my Readwise highlights using React and Recharts.</span></span>
<span class="line"><span></span></span>
<span class="line"><span>Theme Colors (Dark Mode):</span></span>
<span class="line"><span>- Background: rgb(33, 39, 55)</span></span>
<span class="line"><span>- Text: rgb(234, 237, 243)</span></span>
<span class="line"><span>- Accent: rgb(255, 107, 237)</span></span>
<span class="line"><span>- Card Background: rgb(52, 63, 96)</span></span>
<span class="line"><span>- Muted Elements: rgb(138, 51, 123)</span></span>
<span class="line"><span>- Borders: rgb(171, 75, 153)</span></span>
<span class="line"><span></span></span>
<span class="line"><span>Color Application:</span></span>
<span class="line"><span>- Use background color for main dashboard</span></span>
<span class="line"><span>- Apply text color for all typography</span></span>
<span class="line"><span>- Use accent color for interactive elements and highlights</span></span>
<span class="line"><span>- Apply card background for visualization containers</span></span>
<span class="line"><span>- Use muted colors for secondary information</span></span>
<span class="line"><span>- Implement borders for section separation</span></span>
<span class="line"><span></span></span>
<span class="line"><span>Input Data Structure:</span></span>
<span class="line"><span>- CSV format with columns:</span></span>
<span class="line"><span>  - Highlight text</span></span>
<span class="line"><span>  - Book Title</span></span>
<span class="line"><span>  - Book Author</span></span>
<span class="line"><span>  - Color</span></span>
<span class="line"><span>  - Tags</span></span>
<span class="line"><span>  - Location</span></span>
<span class="line"><span>  - Highlighted Date</span></span>
<span class="line"><span></span></span>
<span class="line"><span>Required Visualizations:</span></span>
<span class="line"><span>1. Reading Analytics:</span></span>
<span class="line"><span>   - Average reading time per book (calculated from highlight timestamps)</span></span>
<span class="line"><span>   - Reading patterns by time of day (heatmap using card background and accent colors)</span></span>
<span class="line"><span>   - Heat map showing active reading days</span></span>
<span class="line"><span>     - Base: rgb(52, 63, 96)</span></span>
<span class="line"><span>     - Intensity levels: rgb(138, 51, 123) → rgb(255, 107, 237)</span></span>
<span class="line"><span></span></span>
<span class="line"><span>2. Content Analysis:</span></span>
<span class="line"><span>   - Vertical bar chart: Top 10 most highlighted books</span></span>
<span class="line"><span>   - Bars: gradient from rgb(138, 51, 123) to rgb(255, 107, 237)</span></span>
<span class="line"><span>   - Labels: rgb(234, 237, 243)</span></span>
<span class="line"><span>   - Grid lines: rgba(171, 75, 153, 0.2)</span></span>
<span class="line"><span></span></span>
<span class="line"><span>3. Timeline View:</span></span>
<span class="line"><span>   - Monthly highlighting activity</span></span>
<span class="line"><span>   - Line color: rgb(255, 107, 237)</span></span>
<span class="line"><span>   - Area fill: rgba(255, 107, 237, 0.1)</span></span>
<span class="line"><span>   - Grid: rgba(171, 75, 153, 0.15)</span></span>
<span class="line"><span></span></span>
<span class="line"><span>4. Knowledge Map:</span></span>
<span class="line"><span>   - Interactive mind map using force-directed graph</span></span>
<span class="line"><span>   - Node colors: rgb(52, 63, 96)</span></span>
<span class="line"><span>   - Node borders: rgb(171, 75, 153)</span></span>
<span class="line"><span>   - Connections: rgba(255, 107, 237, 0.6)</span></span>
<span class="line"><span>   - Hover state: rgb(255, 107, 237)</span></span>
<span class="line"><span></span></span>
<span class="line"><span>5. Summary Statistics Card:</span></span>
<span class="line"><span>   - Background: rgb(52, 63, 96)</span></span>
<span class="line"><span>   - Border: rgb(171, 75, 153)</span></span>
<span class="line"><span>   - Headings: rgb(234, 237, 243)</span></span>
<span class="line"><span>   - Values: rgb(255, 107, 237)</span></span>
<span class="line"><span></span></span>
<span class="line"><span>Design Requirements:</span></span>
<span class="line"><span>- Typography:</span></span>
<span class="line"><span>  - Primary font: Light text on dark background</span></span>
<span class="line"><span>  - Base text: rgb(234, 237, 243)</span></span>
<span class="line"><span>  - Minimum 16px for body text</span></span>
<span class="line"><span>  - Headings: rgb(255, 107, 237)</span></span>
<span class="line"><span></span></span>
<span class="line"><span>- Card Design:</span></span>
<span class="line"><span>  - Background: rgb(52, 63, 96)</span></span>
<span class="line"><span>  - Border: 1px solid rgb(171, 75, 153)</span></span>
<span class="line"><span>  - Border radius: 8px</span></span>
<span class="line"><span>  - Box shadow: 0 4px 6px rgba(0, 0, 0, 0.1)</span></span>
<span class="line"><span></span></span>
<span class="line"><span>- Interaction States:</span></span>
<span class="line"><span>  - Hover: Accent color rgb(255, 107, 237)</span></span>
<span class="line"><span>  - Active: rgb(138, 51, 123)</span></span>
<span class="line"><span>  - Focus: 2px solid rgb(255, 107, 237)</span></span>
<span class="line"><span></span></span>
<span class="line"><span>- Responsive Design:</span></span>
<span class="line"><span>  - Desktop: Grid layout with 2-3 columns</span></span>
<span class="line"><span>  - Tablet: 2 columns</span></span>
<span class="line"><span>  - Mobile: Single column, stacked</span></span>
<span class="line"><span>  - Gap: 1.5rem</span></span>
<span class="line"><span>  - Padding: 2rem</span></span>
<span class="line"><span></span></span>
<span class="line"><span>Accessibility:</span></span>
<span class="line"><span>- Ensure contrast ratio ≥ 4.5:1 with text color</span></span>
<span class="line"><span>- Use rgba(234, 237, 243, 0.7) for secondary text</span></span>
<span class="line"><span>- Provide focus indicators using accent color</span></span>
<span class="line"><span>- Include aria-labels for interactive elements</span></span>
<span class="line"><span>- Support keyboard navigation</span></span>
<span class="line"><span></span></span>
<span class="line"><span>Performance:</span></span>
<span class="line"><span>- Implement CSS variables for theme colors</span></span>
<span class="line"><span>- Use CSS transitions for hover states</span></span>
<span class="line"><span>- Optimize SVG rendering for mind map</span></span>
<span class="line"><span>- Implement virtualization for large datasets</span></span></code><button type="button" class="copy" data-code="Create a responsive data visualization dashboard for my Readwise highlights using React and Recharts.

Theme Colors (Dark Mode):
- Background: rgb(33, 39, 55)
- Text: rgb(234, 237, 243)
- Accent: rgb(255, 107, 237)
- Card Background: rgb(52, 63, 96)
- Muted Elements: rgb(138, 51, 123)
- Borders: rgb(171, 75, 153)

Color Application:
- Use background color for main dashboard
- Apply text color for all typography
- Use accent color for interactive elements and highlights
- Apply card background for visualization containers
- Use muted colors for secondary information
- Implement borders for section separation

Input Data Structure:
- CSV format with columns:
  - Highlight text
  - Book Title
  - Book Author
  - Color
  - Tags
  - Location
  - Highlighted Date

Required Visualizations:
1. Reading Analytics:
   - Average reading time per book (calculated from highlight timestamps)
   - Reading patterns by time of day (heatmap using card background and accent colors)
   - Heat map showing active reading days
     - Base: rgb(52, 63, 96)
     - Intensity levels: rgb(138, 51, 123) → rgb(255, 107, 237)

2. Content Analysis:
   - Vertical bar chart: Top 10 most highlighted books
   - Bars: gradient from rgb(138, 51, 123) to rgb(255, 107, 237)
   - Labels: rgb(234, 237, 243)
   - Grid lines: rgba(171, 75, 153, 0.2)

3. Timeline View:
   - Monthly highlighting activity
   - Line color: rgb(255, 107, 237)
   - Area fill: rgba(255, 107, 237, 0.1)
   - Grid: rgba(171, 75, 153, 0.15)

4. Knowledge Map:
   - Interactive mind map using force-directed graph
   - Node colors: rgb(52, 63, 96)
   - Node borders: rgb(171, 75, 153)
   - Connections: rgba(255, 107, 237, 0.6)
   - Hover state: rgb(255, 107, 237)

5. Summary Statistics Card:
   - Background: rgb(52, 63, 96)
   - Border: rgb(171, 75, 153)
   - Headings: rgb(234, 237, 243)
   - Values: rgb(255, 107, 237)

Design Requirements:
- Typography:
  - Primary font: Light text on dark background
  - Base text: rgb(234, 237, 243)
  - Minimum 16px for body text
  - Headings: rgb(255, 107, 237)

- Card Design:
  - Background: rgb(52, 63, 96)
  - Border: 1px solid rgb(171, 75, 153)
  - Border radius: 8px
  - Box shadow: 0 4px 6px rgba(0, 0, 0, 0.1)

- Interaction States:
  - Hover: Accent color rgb(255, 107, 237)
  - Active: rgb(138, 51, 123)
  - Focus: 2px solid rgb(255, 107, 237)

- Responsive Design:
  - Desktop: Grid layout with 2-3 columns
  - Tablet: 2 columns
  - Mobile: Single column, stacked
  - Gap: 1.5rem
  - Padding: 2rem

Accessibility:
- Ensure contrast ratio ≥ 4.5:1 with text color
- Use rgba(234, 237, 243, 0.7) for secondary text
- Provide focus indicators using accent color
- Include aria-labels for interactive elements
- Support keyboard navigation

Performance:
- Implement CSS variables for theme colors
- Use CSS transitions for hover states
- Optimize SVG rendering for mind map
- Implement virtualization for large datasets" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<figure class="gif-container astro-t73tit66"> <div class="gif-wrapper astro-t73tit66"> <img src="/images/readwise_claude_csv/readwise_analytics.gif" alt="Claude second prompt response" width="800" height="500" loading="lazy" class="astro-t73tit66"> </div> <figcaption class="astro-t73tit66">Interactive dashboard visualization of Readwise highlights analysis</figcaption> </figure> 
<p>The interactive dashboard generated by Claude demonstrates the powerful synergy between generative AI and data analysis.
By combining Claude’s natural language processing capabilities with programmatic visualization, we can transform raw reading data into actionable insights. This approach allows us to extract meaningful patterns and trends that would be difficult to identify through manual analysis alone.</p>
<p>Now I want to give you some tips on how to get the best out of claude.</p>
<h2 id="writing-effective-analysis-prompts">Writing Effective Analysis Prompts<a class="heading-link" aria-label="Link to section" href="#writing-effective-analysis-prompts"><span class="heading-link-icon">#</span></a></h2>
<p>Here are key principles for crafting prompts that generate meaningful insights:</p>
<h3 id="1-start-with-clear-objectives">1. Start with Clear Objectives<a class="heading-link" aria-label="Link to section" href="#1-start-with-clear-objectives"><span class="heading-link-icon">#</span></a></h3>
<p>Instead of vague requests, specify what you want to learn:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="plaintext"><code><span class="line"><span>Analyze my reading data to identify:</span></span>
<span class="line"><span>1. Time-of-day reading patterns</span></span>
<span class="line"><span>2. Most engaged topics</span></span>
<span class="line"><span>3. Knowledge connection opportunities</span></span>
<span class="line"><span>4. Potential learning gaps</span></span></code><button type="button" class="copy" data-code="Analyze my reading data to identify:
1. Time-of-day reading patterns
2. Most engaged topics
3. Knowledge connection opportunities
4. Potential learning gaps" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="2-use-role-based-prompting">2. Use Role-Based Prompting<a class="heading-link" aria-label="Link to section" href="#2-use-role-based-prompting"><span class="heading-link-icon">#</span></a></h3>
<p>Give Claude a specific expert perspective:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="plaintext"><code><span class="line"><span>Act as a learning science researcher analyzing my reading patterns.</span></span>
<span class="line"><span>Focus on:</span></span>
<span class="line"><span>- Comprehension patterns</span></span>
<span class="line"><span>- Knowledge retention indicators</span></span>
<span class="line"><span>- Learning efficiency metrics</span></span></code><button type="button" class="copy" data-code="Act as a learning science researcher analyzing my reading patterns.
Focus on:
- Comprehension patterns
- Knowledge retention indicators
- Learning efficiency metrics" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="3-request-specific-visualizations">3. Request Specific Visualizations<a class="heading-link" aria-label="Link to section" href="#3-request-specific-visualizations"><span class="heading-link-icon">#</span></a></h3>
<p>Be explicit about the visual insights you need:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="plaintext"><code><span class="line"><span>Create visualizations showing:</span></span>
<span class="line"><span>1. Daily reading heatmap</span></span>
<span class="line"><span>2. Topic relationship network</span></span>
<span class="line"><span>3. Highlight frequency trends</span></span>
<span class="line"><span>Use theme-consistent colors for clarity</span></span></code><button type="button" class="copy" data-code="Create visualizations showing:
1. Daily reading heatmap
2. Topic relationship network
3. Highlight frequency trends
Use theme-consistent colors for clarity" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h2 id="bonus-behind-the-scenes---how-the-analysis-tool-works">Bonus: Behind the Scenes - How the Analysis Tool Works<a class="heading-link" aria-label="Link to section" href="#bonus-behind-the-scenes---how-the-analysis-tool-works"><span class="heading-link-icon">#</span></a></h2>
<p>For those curious about the technical implementation, let’s peek under the hood at how Claude uses the analysis tool to process your Readwise data:</p>
<h3 id="the-javascript-runtime-environment">The JavaScript Runtime Environment<a class="heading-link" aria-label="Link to section" href="#the-javascript-runtime-environment"><span class="heading-link-icon">#</span></a></h3>
<p>When you upload your Readwise CSV, Claude has access to a JavaScript runtime environment similar to a browser’s console. This environment comes pre-loaded with several powerful libraries:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="javascript"><code><span class="line"><span style="color:#51597D;font-style:italic">// Available libraries</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#0DB9D7"> Papa</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">papaparse</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span><span style="color:#51597D;font-style:italic"> // For CSV processing</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#0DB9D7"> _</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">lodash</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span><span style="color:#51597D;font-style:italic"> // For data manipulation</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#0DB9D7"> React</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">react</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span><span style="color:#51597D;font-style:italic"> // For UI components</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">BarChart</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> LineChart</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> PieChart</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">recharts</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span><span style="color:#51597D;font-style:italic"> // For visualizations</span></span></code><button type="button" class="copy" data-code="// Available libraries
import Papa from &#34;papaparse&#34;; // For CSV processing
import _ from &#34;lodash&#34;; // For data manipulation
import React from &#34;react&#34;; // For UI components
import { BarChart, LineChart, PieChart } from &#34;recharts&#34;; // For visualizations" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="data-processing-pipeline">Data Processing Pipeline<a class="heading-link" aria-label="Link to section" href="#data-processing-pipeline"><span class="heading-link-icon">#</span></a></h3>
<p>The analysis happens in two main stages:</p>
<ol>
<li><strong>Initial Data Processing:</strong></li>
</ol>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="javascript"><code><span class="line"><span style="color:#9D7CD8;font-style:italic">async</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> analyzeReadingData</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Read the CSV file</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> fileContent</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#C0CAF5"> window</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">fs</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">readFile</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">readwisedata.csv</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">    encoding</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">utf8</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Parse CSV using Papaparse</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> parsedData</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> Papa</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">parse</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">fileContent</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">    header</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    skipEmptyLines</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    dynamicTyping</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Analyze time patterns</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> timeAnalysis</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> parsedData</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">data</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">map</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">row</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> date</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> Date</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">row</span><span style="color:#9ABDF5">[</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">Highlighted at</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">])</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">      hour</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> date</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">getHours</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">      title</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> row</span><span style="color:#9ABDF5">[</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">Book Title</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">      tags</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> row</span><span style="color:#9ABDF5">[</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">Tags</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Group and count data using lodash</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> hourlyDistribution</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> _</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">countBy</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">timeAnalysis</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">hour</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">  console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">log</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">Reading time distribution:</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> hourlyDistribution</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="async function analyzeReadingData() {
  // Read the CSV file
  const fileContent = await window.fs.readFile(&#34;readwisedata.csv&#34;, {
    encoding: &#34;utf8&#34;,
  });

  // Parse CSV using Papaparse
  const parsedData = Papa.parse(fileContent, {
    header: true,
    skipEmptyLines: true,
    dynamicTyping: true,
  });

  // Analyze time patterns
  const timeAnalysis = parsedData.data.map(row => {
    const date = new Date(row[&#34;Highlighted at&#34;]);
    return {
      hour: date.getHours(),
      title: row[&#34;Book Title&#34;],
      tags: row[&#34;Tags&#34;],
    };
  });

  // Group and count data using lodash
  const hourlyDistribution = _.countBy(timeAnalysis, &#34;hour&#34;);
  console.log(&#34;Reading time distribution:&#34;, hourlyDistribution);
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<ol start="2">
<li><strong>Visualization Component:</strong></li>
</ol>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="javascript"><code><span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#7AA2F7"> ReadingPatterns</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#89DDFF"> [</span><span style="color:#BB9AF7">timeData</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> setTimeData</span><span style="color:#89DDFF">]</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> useState</span><span style="color:#9ABDF5">([])</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#89DDFF"> [</span><span style="color:#BB9AF7">topBooks</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> setTopBooks</span><span style="color:#89DDFF">]</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> useState</span><span style="color:#9ABDF5">([])</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  useEffect</span><span style="color:#9ABDF5">(() </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#7AA2F7"> analyzeData</span><span style="color:#89DDFF"> =</span><span style="color:#9D7CD8;font-style:italic"> async</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">      const</span><span style="color:#BB9AF7"> response</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#C0CAF5"> window</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">fs</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">readFile</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">readwisedata.csv</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">        encoding</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">utf8</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">      })</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">      // Process time data for visualization</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">      const</span><span style="color:#BB9AF7"> timeAnalysis</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> parsedData</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">data</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">reduce</span><span style="color:#9ABDF5">((</span><span style="color:#E0AF68">acc</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> row</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">        const</span><span style="color:#BB9AF7"> hour</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> Date</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">row</span><span style="color:#9ABDF5">[</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">Highlighted at</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">])</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">getHours</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">        acc</span><span style="color:#9ABDF5">[</span><span style="color:#7DCFFF">hour</span><span style="color:#9ABDF5">] </span><span style="color:#89DDFF">=</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">acc</span><span style="color:#9ABDF5">[</span><span style="color:#7DCFFF">hour</span><span style="color:#9ABDF5">] </span><span style="color:#BB9AF7">||</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5">) </span><span style="color:#89DDFF">+</span><span style="color:#FF9E64"> 1</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">        return</span><span style="color:#C0CAF5"> acc</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">      // Format data for charts</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">      const</span><span style="color:#BB9AF7"> timeDataForChart</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> Object</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">entries</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">timeAnalysis</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">map</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#9ABDF5">        (</span><span style="color:#89DDFF">[</span><span style="color:#E0AF68">hour</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> count</span><span style="color:#89DDFF">]</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> ({</span></span>
<span class="line"><span style="color:#73DACA">          hour</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> `</span><span style="color:#7DCFFF">${</span><span style="color:#C0CAF5">hour</span><span style="color:#7DCFFF">}</span><span style="color:#9ECE6A">:00</span><span style="color:#89DDFF">`</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">          count</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">        })</span></span>
<span class="line"><span style="color:#9ABDF5">      )</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">      setTimeData</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">timeDataForChart</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">    analyzeData</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> [])</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> (</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">div</span><span style="color:#BB9AF7"> className</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">w-full space-y-8 p-4</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">      &lt;</span><span style="color:#DE5971">ResponsiveContainer </span><span style="color:#BB9AF7">width</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">100%</span><span style="color:#89DDFF">&quot;</span><span style="color:#BB9AF7"> height</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">100%</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">        &lt;</span><span style="color:#DE5971">BarChart </span><span style="color:#BB9AF7">data</span><span style="color:#89DDFF">=</span><span style="color:#7DCFFF">{</span><span style="color:#C0CAF5">timeData</span><span style="color:#7DCFFF">}</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">          &lt;</span><span style="color:#DE5971">CartesianGrid </span><span style="color:#BB9AF7">strokeDasharray</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">3 3</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97"> /&gt;</span></span>
<span class="line"><span style="color:#BA3C97">          &lt;</span><span style="color:#DE5971">XAxis </span><span style="color:#BB9AF7">dataKey</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">hour</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97"> /&gt;</span></span>
<span class="line"><span style="color:#BA3C97">          &lt;</span><span style="color:#DE5971">YAxis </span><span style="color:#BA3C97">/&gt;</span></span>
<span class="line"><span style="color:#BA3C97">          &lt;</span><span style="color:#DE5971">Bar </span><span style="color:#BB9AF7">dataKey</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">count</span><span style="color:#89DDFF">&quot;</span><span style="color:#BB9AF7"> fill</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">#4F46E5</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97"> /&gt;</span></span>
<span class="line"><span style="color:#BA3C97">        &lt;/</span><span style="color:#DE5971">BarChart</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">      &lt;/</span><span style="color:#DE5971">ResponsiveContainer</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#9ABDF5">  )</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="const ReadingPatterns = () => {
  const [timeData, setTimeData] = useState([]);
  const [topBooks, setTopBooks] = useState([]);

  useEffect(() => {
    const analyzeData = async () => {
      const response = await window.fs.readFile(&#34;readwisedata.csv&#34;, {
        encoding: &#34;utf8&#34;,
      });

      // Process time data for visualization
      const timeAnalysis = parsedData.data.reduce((acc, row) => {
        const hour = new Date(row[&#34;Highlighted at&#34;]).getHours();
        acc[hour] = (acc[hour] || 0) + 1;
        return acc;
      }, {});

      // Format data for charts
      const timeDataForChart = Object.entries(timeAnalysis).map(
        ([hour, count]) => ({
          hour: `${hour}:00`,
          count,
        })
      );

      setTimeData(timeDataForChart);
    };
    analyzeData();
  }, []);

  return (
    <div className=&#34;w-full space-y-8 p-4&#34;>
      <ResponsiveContainer width=&#34;100%&#34; height=&#34;100%&#34;>
        <BarChart data={timeData}>
          <CartesianGrid strokeDasharray=&#34;3 3&#34; />
          <XAxis dataKey=&#34;hour&#34; />
          <YAxis />
          <Bar dataKey=&#34;count&#34; fill=&#34;#4F46E5&#34; />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
};" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="key-technical-features">Key Technical Features<a class="heading-link" aria-label="Link to section" href="#key-technical-features"><span class="heading-link-icon">#</span></a></h3>
<ol>
<li>
<p><strong>Asynchronous File Handling</strong>: The <code>window.fs.readFile</code> API provides async file access, similar to Node.js’s fs/promises.</p>
</li>
<li>
<p><strong>Data Processing Libraries</strong>:</p>
<ul>
<li>Papaparse handles CSV parsing with options for headers and type conversion</li>
<li>Lodash provides efficient data manipulation functions</li>
<li>React and Recharts enable interactive visualizations</li>
</ul>
</li>
<li>
<p><strong>React Integration</strong>:</p>
<ul>
<li>Components use hooks for state management</li>
<li>Tailwind classes for styling</li>
<li>Responsive container adapts to screen size</li>
</ul>
</li>
<li>
<p><strong>Error Handling</strong>: The code includes proper error boundaries and async/await patterns to handle potential issues gracefully.</p>
</li>
</ol>
<p>This technical implementation allows Claude to process your reading data efficiently while providing interactive visualizations that help you understand your reading patterns better.</p>
<h2 id="conclusion">Conclusion<a class="heading-link" aria-label="Link to section" href="#conclusion"><span class="heading-link-icon">#</span></a></h2>
<p>I hope this blog post demonstrates how AI can accelerate data analysis workflows. What previously required significant time and technical expertise can now be accomplished in minutes. This democratization of data analysis empowers people without coding backgrounds to gain valuable insights from their own data.</p> </article> <script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).only=e;window.dispatchEvent(new Event("astro:only"));})();</script><astro-island uid="Z1XneyL" component-url="/_astro/presentation.C3Wa0mjp.js" component-export="VMarkBlogRenderer" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;containerSelector&quot;:[0,&quot;#article&quot;],&quot;class&quot;:[0,&quot;astro-vj4tpspi&quot;]}" ssr client="only" opts="{&quot;name&quot;:&quot;VMarkBlogRenderer&quot;,&quot;value&quot;:&quot;react&quot;}"></astro-island> <!-- Fullscreen Modal Container using native dialog --><dialog id="mermaid-modal" class="mermaid-modal" aria-label="Fullscreen diagram view"> <div class="mermaid-modal-content"> <button class="mermaid-modal-close" aria-label="Close fullscreen view" type="button"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <line x1="18" y1="6" x2="6" y2="18"></line> <line x1="6" y1="6" x2="18" y2="18"></line> </svg> </button> <div class="mermaid-modal-diagram"></div> <div class="mermaid-modal-hint">Press <kbd>Esc</kbd> or click outside to close</div> </div> </dialog>  <script type="module">const p=new Set;function g(){const e=document.getElementById("mermaid-modal"),c=e?.querySelector(".mermaid-modal-diagram"),f=e?.querySelector(".mermaid-modal-close");if(!e||!c)return;document.querySelectorAll('svg[id^="mermaid-"]').forEach(t=>{if(!t.id.match(/^mermaid-\d+$/)||p.has(t.id)||t.parentElement?.classList.contains("mermaid-fullscreen-wrapper")||t.closest(".mermaid-modal"))return;p.add(t.id);const n=document.createElement("div");n.className="mermaid-fullscreen-wrapper mermaid-clickable",n.setAttribute("tabindex","0"),n.setAttribute("role","button"),n.setAttribute("aria-label","Click to view diagram fullscreen"),t.parentElement?.insertBefore(n,t),n.appendChild(t);const o=document.createElement("div");o.className="mermaid-expand-icon",o.innerHTML=`
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
</li> <li class="astro-vj4tpspi">Small tips and trick</li> </ul> </div> <a href="https://alex-op-newsletter.beehiiv.com/subscribe?utm_source=blog&utm_medium=post&utm_campaign=post_supercharging-reading-comprehension-claude-readwise" target="_blank" rel="noopener noreferrer" id="newsletter-subscribe-button" class="inline-flex items-center justify-center gap-2 rounded-full bg-skin-accent px-6 py-3 text-base font-semibold text-skin-inverted shadow-md transition-all duration-200 hover:scale-[1.02] hover:transform hover:opacity-90 astro-vj4tpspi"> <svg class="h-5 w-5 fill-current astro-vj4tpspi" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg>
Subscribe Now
</a> <button id="newsletter-dismiss" data-post-slug="supercharging-reading-comprehension-claude-readwise" class="absolute right-3 top-3 rounded-full p-1 text-skin-base transition-all duration-200 hover:bg-skin-accent hover:bg-opacity-10 hover:text-skin-accent astro-vj4tpspi" aria-label="Close notification"> <svg class="h-5 w-5 astro-vj4tpspi" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class="astro-vj4tpspi"></path> </svg> </button> </div> </div> </div> <ul class="my-8 flex flex-wrap gap-2 astro-vj4tpspi"> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/ai/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-2"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">ai</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/productivity/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-3"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">productivity</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/reading/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-4"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">reading</span>   </a> </li>  </ul> <div class="flex flex-col-reverse items-center justify-between gap-6 sm:flex-row-reverse sm:items-end sm:gap-4 astro-vj4tpspi"> <button id="back-to-top" class="focus-outline whitespace-nowrap py-1 hover:opacity-75 astro-vj4tpspi"> <svg xmlns="http://www.w3.org/2000/svg" class="rotate-90 astro-vj4tpspi"> <path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg> <span class="astro-vj4tpspi">Back to Top</span> </button> <div class="social-icons astro-wkojbtzc"> <span class="italic astro-wkojbtzc">Share this post on:</span> <div class="text-center astro-wkojbtzc"> <a href="https://wa.me/?text=https://alexop.dev/posts/supercharging-reading-comprehension-claude-readwise/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via WhatsApp" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"></path>
      <path d="M9 10a0.5 .5 0 0 0 1 0v-1a0.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a0.5 .5 0 0 0 0 -1h-1a0.5 .5 0 0 0 0 1"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via WhatsApp</span> </a><a href="https://www.facebook.com/sharer.php?u=https://alexop.dev/posts/supercharging-reading-comprehension-claude-readwise/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Facebook" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"
    ></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on Facebook</span> </a><a href="https://x.com/intent/tweet?url=https://alexop.dev/posts/supercharging-reading-comprehension-claude-readwise/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Tweet this post" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Tweet this post</span> </a><a href="https://t.me/share/url?url=https://alexop.dev/posts/supercharging-reading-comprehension-claude-readwise/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via Telegram" target="_blank" rel="noopener noreferrer"> <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon-tabler"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"></path>
      </svg> <span class="sr-only astro-wkojbtzc">Share this post via Telegram</span> </a><a href="https://pinterest.com/pin/create/button/?url=https://alexop.dev/posts/supercharging-reading-comprehension-claude-readwise/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Pinterest" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <line x1="8" y1="20" x2="12" y2="11"></line>
      <path d="M10.7 14c.437 1.263 1.43 2 2.55 2c2.071 0 3.75 -1.554 3.75 -4a5 5 0 1 0 -9.7 1.7"></path>
      <circle cx="12" cy="12" r="9"></circle>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post on Pinterest</span> </a><a href="mailto:?subject=See%20this%20post&#38;body=https://alexop.dev/posts/supercharging-reading-comprehension-claude-readwise/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via email" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via email</span> </a><a href="https://www.linkedin.com/shareArticle?mini=true&url=https://alexop.dev/posts/supercharging-reading-comprehension-claude-readwise/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
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
    </script> </body> </html>  <script>(function(){const postSlug = "supercharging-reading-comprehension-claude-readwise";

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
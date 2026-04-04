# Source: https://alexop.dev/posts/frontend-testing-guide-10-essential-rules

<!DOCTYPE html><html lang="en" class="scroll-smooth astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/posts/frontend-testing-guide-10-essential-rules/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>Frontend Testing Guide: 10 Essential Rules for Naming Tests | alexop.dev</title><meta name="title" content="Frontend Testing Guide: 10 Essential Rules for Naming Tests | alexop.dev"><meta name="description" content="Learn how to write clear and maintainable frontend tests with 10 practical naming rules. Includes real-world examples showing good and bad practices for component testing across any framework."><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="Frontend Testing Guide: 10 Essential Rules for Naming Tests | alexop.dev"><meta property="og:description" content="Learn how to write clear and maintainable frontend tests with 10 practical naming rules. Includes real-world examples showing good and bad practices for component testing across any framework."><meta property="og:url" content="https://alexop.dev/posts/frontend-testing-guide-10-essential-rules/"><meta property="og:image" content="https://alexop.dev/posts/frontend-testing-guide-10-essential-rules-for-naming-tests/index.png"><meta property="og:type" content="article"><!-- Article Published/Modified time --><meta property="article:published_time" content="2024-10-26T08:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/posts/frontend-testing-guide-10-essential-rules/"><meta property="twitter:title" content="Frontend Testing Guide: 10 Essential Rules for Naming Tests | alexop.dev"><meta property="twitter:description" content="Learn how to write clear and maintainable frontend tests with 10 practical naming rules. Includes real-world examples showing good and bad practices for component testing across any framework."><meta property="twitter:image" content="https://alexop.dev/posts/frontend-testing-guide-10-essential-rules-for-naming-tests/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"Frontend Testing Guide: 10 Essential Rules for Naming Tests | alexop.dev","description":"Learn how to write clear and maintainable frontend tests with 10 practical naming rules. Includes real-world examples showing good and bad practices for component testing across any framework.","image":"https://alexop.dev/posts/frontend-testing-guide-10-essential-rules-for-naming-tests/index.png","datePublished":"2024-10-26T08:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
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
</style><style>[data-astro-transition-scope="astro-plk3gbjq-1"] { view-transition-name: frontend-testing-guide-10-essential-rules-for-naming-tests; }@layer astro { ::view-transition-old(frontend-testing-guide-10-essential-rules-for-naming-tests) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(frontend-testing-guide-10-essential-rules-for-naming-tests) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(frontend-testing-guide-10-essential-rules-for-naming-tests) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(frontend-testing-guide-10-essential-rules-for-naming-tests) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-2"] { view-transition-name: testing; }@layer astro { ::view-transition-old(testing) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-3"] { view-transition-name: vitest; }@layer astro { ::view-transition-old(vitest) { 
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <div class="mx-auto flex w-full max-w-5xl justify-start px-2 astro-vj4tpspi"> <button class="focus-outline mb-2 mt-8 flex hover:opacity-75 astro-vj4tpspi" onclick="(() => (history.length === 1) ? window.location = '/' : history.back())()"> <svg xmlns="http://www.w3.org/2000/svg" class="astro-vj4tpspi"><path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg><span class="astro-vj4tpspi">Go back</span> </button> </div> <main data-pagefind-body id="main-content" class="relative astro-vj4tpspi"> <h1 class="post-title astro-vj4tpspi" data-astro-transition-scope="astro-plk3gbjq-1">Frontend Testing Guide: 10 Essential Rules for Naming Tests</h1> <div class="my-2 flex items-center justify-between astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-100 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-base"><time dateTime="2024-10-26T08:00:00.000Z">Oct 26, 2024</time><span class="sr-only"> at </span></span></div> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="tEct1" prefix="r6" component-url="/_astro/PostCopyButton.-PGtk4At.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;title&quot;:[0,&quot;Frontend Testing Guide: 10 Essential Rules for Naming Tests&quot;],&quot;content&quot;:[0,&quot;## Introduction\n\nThe path to better testing starts with something surprisingly simple: how you name your tests. Good test names:\n\n- Make your test suite more maintainable\n- Guide you toward writing tests that focus on user behavior\n- Improve clarity and readability for your team\n\nIn this blog post, we&#39;ll explore 10 essential rules for writing better tests that will transform your approach to testing. These principles are:\n\n1. Framework-agnostic\n2. Applicable across the entire testing pyramid\n3. Useful for various testing tools:\n   - Unit tests (Jest, Vitest)\n   - Integration tests\n   - End-to-end tests (Cypress, Playwright)\n\nBy following these rules, you&#39;ll create a more robust and understandable test suite, regardless of your chosen testing framework or methodology.\n\n## Rule 1: Always Use \&quot;should\&quot; + Verb\n\nEvery test name should start with \&quot;should\&quot; followed by an action verb.\n\n```js\n// ❌ Bad\nit(\&quot;displays the error message\&quot;, () =&gt; {});\nit(\&quot;modal visibility\&quot;, () =&gt; {});\nit(\&quot;form validation working\&quot;, () =&gt; {});\n\n// ✅ Good\nit(\&quot;should display error message when validation fails\&quot;, () =&gt; {});\nit(\&quot;should show modal when trigger button is clicked\&quot;, () =&gt; {});\nit(\&quot;should validate form when user submits\&quot;, () =&gt; {});\n```\n\n**Generic Pattern:** `should [verb] [expected outcome]`\n\n## Rule 2: Include the Trigger Event\n\nSpecify what causes the behavior you&#39;re testing.\n\n```js\n// ❌ Bad\nit(\&quot;should update counter\&quot;, () =&gt; {});\nit(\&quot;should validate email\&quot;, () =&gt; {});\nit(\&quot;should show dropdown\&quot;, () =&gt; {});\n\n// ✅ Good\nit(\&quot;should increment counter when plus button is clicked\&quot;, () =&gt; {});\nit(\&quot;should show error when email format is invalid\&quot;, () =&gt; {});\nit(\&quot;should open dropdown when toggle is clicked\&quot;, () =&gt; {});\n```\n\n**Generic Pattern:** `should [verb] [expected outcome] when [trigger event]`\n\n## Rule 3: Group Related Tests with Descriptive Contexts\n\nUse describe blocks to create clear test hierarchies.\n\n```js\n// ❌ Bad\ndescribe(\&quot;AuthForm\&quot;, () =&gt; {\n  it(\&quot;should test empty state\&quot;, () =&gt; {});\n  it(\&quot;should test invalid state\&quot;, () =&gt; {});\n  it(\&quot;should test success state\&quot;, () =&gt; {});\n});\n\n// ✅ Good\ndescribe(\&quot;AuthForm\&quot;, () =&gt; {\n  describe(\&quot;when form is empty\&quot;, () =&gt; {\n    it(\&quot;should disable submit button\&quot;, () =&gt; {});\n    it(\&quot;should not show any validation errors\&quot;, () =&gt; {});\n  });\n\n  describe(\&quot;when submitting invalid data\&quot;, () =&gt; {\n    it(\&quot;should show validation errors\&quot;, () =&gt; {});\n    it(\&quot;should keep submit button disabled\&quot;, () =&gt; {});\n  });\n});\n```\n\n**Generic Pattern:**\n\n```js\ndescribe(\&quot;[Component/Feature]\&quot;, () =&gt; {\n  describe(\&quot;when [specific condition]\&quot;, () =&gt; {\n    it(\&quot;should [expected behavior]\&quot;, () =&gt; {});\n  });\n});\n```\n\n## Rule 4: Name State Changes Explicitly\n\nClearly describe the before and after states in your test names.\n\n```js\n// ❌ Bad\nit(\&quot;should change status\&quot;, () =&gt; {});\nit(\&quot;should update todo\&quot;, () =&gt; {});\nit(\&quot;should modify permissions\&quot;, () =&gt; {});\n\n// ✅ Good\nit(\&quot;should change status from pending to approved\&quot;, () =&gt; {});\nit(\&quot;should mark todo as completed when checkbox clicked\&quot;, () =&gt; {});\nit(\&quot;should upgrade user from basic to premium\&quot;, () =&gt; {});\n```\n\n**Generic Pattern:** `should change [attribute] from [initial state] to [final state]`\n\n## Rule 5: Describe Async Behavior Clearly\n\nInclude loading and result states for asynchronous operations.\n\n```js\n// ❌ Bad\nit(\&quot;should load data\&quot;, () =&gt; {});\nit(\&quot;should handle API call\&quot;, () =&gt; {});\nit(\&quot;should fetch user\&quot;, () =&gt; {});\n\n// ✅ Good\nit(\&quot;should show skeleton while loading data\&quot;, () =&gt; {});\nit(\&quot;should display error message when API call fails\&quot;, () =&gt; {});\nit(\&quot;should render profile after user data loads\&quot;, () =&gt; {});\n```\n\n**Generic Pattern:** `should [verb] [expected outcome] [during/after] [async operation]`\n\n## Rule 6: Name Error Cases Specifically\n\nBe explicit about the type of error and what causes it.\n\n```js\n// ❌ Bad\nit(\&quot;should show error\&quot;, () =&gt; {});\nit(\&quot;should handle invalid input\&quot;, () =&gt; {});\nit(\&quot;should validate form\&quot;, () =&gt; {});\n\n// ✅ Good\nit(&#39;should show \&quot;Invalid Card\&quot; when card number is wrong&#39;, () =&gt; {});\nit(&#39;should display \&quot;Required\&quot; when password is empty&#39;, () =&gt; {});\nit(\&quot;should show network error when API is unreachable\&quot;, () =&gt; {});\n```\n\n**Generic Pattern:** `should show [specific error message] when [error condition]`\n\n## Rule 7: Use Business Language, Not Technical Terms\n\nWrite tests using domain language rather than implementation details.\n\n```js\n// ❌ Bad\nit(\&quot;should update state\&quot;, () =&gt; {});\nit(\&quot;should dispatch action\&quot;, () =&gt; {});\nit(\&quot;should modify DOM\&quot;, () =&gt; {});\n\n// ✅ Good\nit(\&quot;should save customer order\&quot;, () =&gt; {});\nit(\&quot;should update cart total\&quot;, () =&gt; {});\nit(\&quot;should mark order as delivered\&quot;, () =&gt; {});\n```\n\n**Generic Pattern:** `should [business action] [business entity]`\n\n## Rule 8: Include Important Preconditions\n\nSpecify conditions that affect the behavior being tested.\n\n```js\n// ❌ Bad\nit(\&quot;should enable button\&quot;, () =&gt; {});\nit(\&quot;should show message\&quot;, () =&gt; {});\nit(\&quot;should apply discount\&quot;, () =&gt; {});\n\n// ✅ Good\nit(\&quot;should enable checkout when cart has items\&quot;, () =&gt; {});\nit(\&quot;should show free shipping when total exceeds $100\&quot;, () =&gt; {});\nit(\&quot;should apply discount when user is premium member\&quot;, () =&gt; {});\n```\n\n**Generic Pattern:** `should [expected behavior] when [precondition]`\n\n## Rule 9: Name UI Feedback Tests from User Perspective\n\nDescribe visual changes as users would perceive them.\n\n```js\n// ❌ Bad\nit(\&quot;should set error class\&quot;, () =&gt; {});\nit(\&quot;should toggle visibility\&quot;, () =&gt; {});\nit(\&quot;should update styles\&quot;, () =&gt; {});\n\n// ✅ Good\nit(\&quot;should highlight search box in red when empty\&quot;, () =&gt; {});\nit(\&quot;should show green checkmark when password is strong\&quot;, () =&gt; {});\nit(\&quot;should disable submit button while processing\&quot;, () =&gt; {});\n```\n\n**Generic Pattern:** `should [visual change] when [user action/condition]`\n\n## Rule 10: Structure Complex Workflows Step by Step\n\nBreak down complex processes into clear steps.\n\n```js\n// ❌ Bad\ndescribe(\&quot;Checkout\&quot;, () =&gt; {\n  it(\&quot;should process checkout\&quot;, () =&gt; {});\n  it(\&quot;should handle shipping\&quot;, () =&gt; {});\n  it(\&quot;should complete order\&quot;, () =&gt; {});\n});\n\n// ✅ Good\ndescribe(\&quot;Checkout Process\&quot;, () =&gt; {\n  it(\&quot;should first validate items are in stock\&quot;, () =&gt; {});\n  it(\&quot;should then collect shipping address\&quot;, () =&gt; {});\n  it(\&quot;should finally process payment\&quot;, () =&gt; {});\n\n  describe(\&quot;after successful payment\&quot;, () =&gt; {\n    it(\&quot;should display order confirmation\&quot;, () =&gt; {});\n    it(\&quot;should send confirmation email\&quot;, () =&gt; {});\n  });\n});\n```\n\n**Generic Pattern:**\n\n```js\ndescribe(\&quot;[Complex Process]\&quot;, () =&gt; {\n  it(\&quot;should first [initial step]\&quot;, () =&gt; {});\n  it(\&quot;should then [next step]\&quot;, () =&gt; {});\n  it(\&quot;should finally [final step]\&quot;, () =&gt; {});\n\n  describe(\&quot;after [key milestone]\&quot;, () =&gt; {\n    it(\&quot;should [follow-up action]\&quot;, () =&gt; {});\n  });\n});\n```\n\n## Complete Example\n\nHere&#39;s a comprehensive example showing how to combine all these rules:\n\n```js\n// ❌ Bad\ndescribe(\&quot;ShoppingCart\&quot;, () =&gt; {\n  it(\&quot;test adding item\&quot;, () =&gt; {});\n  it(\&quot;check total\&quot;, () =&gt; {});\n  it(\&quot;handle checkout\&quot;, () =&gt; {});\n});\n\n// ✅ Good\ndescribe(\&quot;ShoppingCart\&quot;, () =&gt; {\n  describe(\&quot;when adding items\&quot;, () =&gt; {\n    it(\&quot;should add item to cart when add button is clicked\&quot;, () =&gt; {});\n    it(\&quot;should update total price immediately\&quot;, () =&gt; {});\n    it(\&quot;should show item count badge\&quot;, () =&gt; {});\n  });\n\n  describe(\&quot;when cart is empty\&quot;, () =&gt; {\n    it(\&quot;should display empty cart message\&quot;, () =&gt; {});\n    it(\&quot;should disable checkout button\&quot;, () =&gt; {});\n  });\n\n  describe(\&quot;during checkout process\&quot;, () =&gt; {\n    it(\&quot;should validate stock before proceeding\&quot;, () =&gt; {});\n    it(\&quot;should show loading indicator while processing payment\&quot;, () =&gt; {});\n    it(\&quot;should display success message after completion\&quot;, () =&gt; {});\n  });\n});\n```\n\n## Test Name Checklist\n\nBefore committing your test, verify that its name:\n\n- [ ] Starts with \&quot;should\&quot;\n- [ ] Uses a clear action verb\n- [ ] Specifies the trigger condition\n- [ ] Uses business language\n- [ ] Describes visible behavior\n- [ ] Is specific enough for debugging\n- [ ] Groups logically with related tests\n\n## Conclusion\n\nThoughtful test naming is a fundamental building block in the broader landscape of writing better tests. To maintain consistency across your team:\n\n1. Document your naming conventions in detail\n2. Share these guidelines with all team members\n3. Integrate the guidelines into your development workflow\n\nFor teams using AI tools like GitHub Copilot:\n\n- Incorporate these guidelines into your project documentation\n- Link the markdown file containing these rules to Copilot\n- This integration allows Copilot to suggest test names aligned with your conventions\n\nFor more information on linking documentation to Copilot, see:\n[VS Code Experiments Boost AI Copilot Functionality](https://visualstudiomagazine.com/Articles/2024/09/09/VS-Code-Experiments-Boost-AI-Copilot-Functionality.aspx)\n\nBy following these steps, you can ensure consistent, high-quality test naming across your entire project.&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PostCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus-outline inline-flex items-center gap-1.5 rounded-md border border-skin-line bg-skin-card px-2.5 py-1.5 text-xs font-medium text-skin-base opacity-80 transition-all hover:border-skin-accent/50 hover:text-skin-accent hover:opacity-100" aria-label="Copy post as markdown" title="Copy post as markdown for AI/LLM"><svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg><span>Copy Post</span></button><!--astro:end--></astro-island> </div>  <article id="article" class="prose mx-auto mt-8 max-w-5xl astro-vj4tpspi"> <h2 id="introduction">Introduction<a class="heading-link" aria-label="Link to section" href="#introduction"><span class="heading-link-icon">#</span></a></h2>
<p>The path to better testing starts with something surprisingly simple: how you name your tests. Good test names:</p>
<ul>
<li>Make your test suite more maintainable</li>
<li>Guide you toward writing tests that focus on user behavior</li>
<li>Improve clarity and readability for your team</li>
</ul>
<p>In this blog post, we’ll explore 10 essential rules for writing better tests that will transform your approach to testing. These principles are:</p>
<ol>
<li>Framework-agnostic</li>
<li>Applicable across the entire testing pyramid</li>
<li>Useful for various testing tools:
<ul>
<li>Unit tests (Jest, Vitest)</li>
<li>Integration tests</li>
<li>End-to-end tests (Cypress, Playwright)</li>
</ul>
</li>
</ol>
<p>By following these rules, you’ll create a more robust and understandable test suite, regardless of your chosen testing framework or methodology.</p>
<h2 id="rule-1-always-use-should--verb">Rule 1: Always Use “should” + Verb<a class="heading-link" aria-label="Link to section" href="#rule-1-always-use-should--verb"><span class="heading-link-icon">#</span></a></h2>
<p>Every test name should start with “should” followed by an action verb.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="js"><code><span class="line"><span style="color:#51597D;font-style:italic">// ❌ Bad</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">displays the error message</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">modal visibility</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">form validation working</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// ✅ Good</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should display error message when validation fails</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should show modal when trigger button is clicked</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should validate form when user submits</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="// ❌ Bad
it(&#34;displays the error message&#34;, () => {});
it(&#34;modal visibility&#34;, () => {});
it(&#34;form validation working&#34;, () => {});

// ✅ Good
it(&#34;should display error message when validation fails&#34;, () => {});
it(&#34;should show modal when trigger button is clicked&#34;, () => {});
it(&#34;should validate form when user submits&#34;, () => {});" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><strong>Generic Pattern:</strong> <code>should [verb] [expected outcome]</code></p>
<h2 id="rule-2-include-the-trigger-event">Rule 2: Include the Trigger Event<a class="heading-link" aria-label="Link to section" href="#rule-2-include-the-trigger-event"><span class="heading-link-icon">#</span></a></h2>
<p>Specify what causes the behavior you’re testing.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="js"><code><span class="line"><span style="color:#51597D;font-style:italic">// ❌ Bad</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should update counter</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should validate email</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should show dropdown</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// ✅ Good</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should increment counter when plus button is clicked</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should show error when email format is invalid</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should open dropdown when toggle is clicked</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="// ❌ Bad
it(&#34;should update counter&#34;, () => {});
it(&#34;should validate email&#34;, () => {});
it(&#34;should show dropdown&#34;, () => {});

// ✅ Good
it(&#34;should increment counter when plus button is clicked&#34;, () => {});
it(&#34;should show error when email format is invalid&#34;, () => {});
it(&#34;should open dropdown when toggle is clicked&#34;, () => {});" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><strong>Generic Pattern:</strong> <code>should [verb] [expected outcome] when [trigger event]</code></p>
<h2 id="rule-3-group-related-tests-with-descriptive-contexts">Rule 3: Group Related Tests with Descriptive Contexts<a class="heading-link" aria-label="Link to section" href="#rule-3-group-related-tests-with-descriptive-contexts"><span class="heading-link-icon">#</span></a></h2>
<p>Use describe blocks to create clear test hierarchies.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="js"><code><span class="line"><span style="color:#51597D;font-style:italic">// ❌ Bad</span></span>
<span class="line"><span style="color:#7AA2F7">describe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">AuthForm</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should test empty state</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should test invalid state</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should test success state</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">})</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// ✅ Good</span></span>
<span class="line"><span style="color:#7AA2F7">describe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">AuthForm</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  describe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">when form is empty</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">    it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should disable submit button</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">    it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should not show any validation errors</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  describe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">when submitting invalid data</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">    it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should show validation errors</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">    it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should keep submit button disabled</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">})</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="// ❌ Bad
describe(&#34;AuthForm&#34;, () => {
  it(&#34;should test empty state&#34;, () => {});
  it(&#34;should test invalid state&#34;, () => {});
  it(&#34;should test success state&#34;, () => {});
});

// ✅ Good
describe(&#34;AuthForm&#34;, () => {
  describe(&#34;when form is empty&#34;, () => {
    it(&#34;should disable submit button&#34;, () => {});
    it(&#34;should not show any validation errors&#34;, () => {});
  });

  describe(&#34;when submitting invalid data&#34;, () => {
    it(&#34;should show validation errors&#34;, () => {});
    it(&#34;should keep submit button disabled&#34;, () => {});
  });
});" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><strong>Generic Pattern:</strong></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="js"><code><span class="line"><span style="color:#7AA2F7">describe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">[Component/Feature]</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  describe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">when [specific condition]</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">    it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should [expected behavior]</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">})</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="describe(&#34;[Component/Feature]&#34;, () => {
  describe(&#34;when [specific condition]&#34;, () => {
    it(&#34;should [expected behavior]&#34;, () => {});
  });
});" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h2 id="rule-4-name-state-changes-explicitly">Rule 4: Name State Changes Explicitly<a class="heading-link" aria-label="Link to section" href="#rule-4-name-state-changes-explicitly"><span class="heading-link-icon">#</span></a></h2>
<p>Clearly describe the before and after states in your test names.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="js"><code><span class="line"><span style="color:#51597D;font-style:italic">// ❌ Bad</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should change status</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should update todo</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should modify permissions</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// ✅ Good</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should change status from pending to approved</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should mark todo as completed when checkbox clicked</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should upgrade user from basic to premium</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="// ❌ Bad
it(&#34;should change status&#34;, () => {});
it(&#34;should update todo&#34;, () => {});
it(&#34;should modify permissions&#34;, () => {});

// ✅ Good
it(&#34;should change status from pending to approved&#34;, () => {});
it(&#34;should mark todo as completed when checkbox clicked&#34;, () => {});
it(&#34;should upgrade user from basic to premium&#34;, () => {});" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><strong>Generic Pattern:</strong> <code>should change [attribute] from [initial state] to [final state]</code></p>
<h2 id="rule-5-describe-async-behavior-clearly">Rule 5: Describe Async Behavior Clearly<a class="heading-link" aria-label="Link to section" href="#rule-5-describe-async-behavior-clearly"><span class="heading-link-icon">#</span></a></h2>
<p>Include loading and result states for asynchronous operations.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="js"><code><span class="line"><span style="color:#51597D;font-style:italic">// ❌ Bad</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should load data</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should handle API call</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should fetch user</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// ✅ Good</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should show skeleton while loading data</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should display error message when API call fails</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should render profile after user data loads</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="// ❌ Bad
it(&#34;should load data&#34;, () => {});
it(&#34;should handle API call&#34;, () => {});
it(&#34;should fetch user&#34;, () => {});

// ✅ Good
it(&#34;should show skeleton while loading data&#34;, () => {});
it(&#34;should display error message when API call fails&#34;, () => {});
it(&#34;should render profile after user data loads&#34;, () => {});" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><strong>Generic Pattern:</strong> <code>should [verb] [expected outcome] [during/after] [async operation]</code></p>
<h2 id="rule-6-name-error-cases-specifically">Rule 6: Name Error Cases Specifically<a class="heading-link" aria-label="Link to section" href="#rule-6-name-error-cases-specifically"><span class="heading-link-icon">#</span></a></h2>
<p>Be explicit about the type of error and what causes it.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="js"><code><span class="line"><span style="color:#51597D;font-style:italic">// ❌ Bad</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should show error</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should handle invalid input</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should validate form</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// ✅ Good</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">should show &quot;Invalid Card&quot; when card number is wrong</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">should display &quot;Required&quot; when password is empty</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should show network error when API is unreachable</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="// ❌ Bad
it(&#34;should show error&#34;, () => {});
it(&#34;should handle invalid input&#34;, () => {});
it(&#34;should validate form&#34;, () => {});

// ✅ Good
it('should show &#34;Invalid Card&#34; when card number is wrong', () => {});
it('should display &#34;Required&#34; when password is empty', () => {});
it(&#34;should show network error when API is unreachable&#34;, () => {});" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><strong>Generic Pattern:</strong> <code>should show [specific error message] when [error condition]</code></p>
<h2 id="rule-7-use-business-language-not-technical-terms">Rule 7: Use Business Language, Not Technical Terms<a class="heading-link" aria-label="Link to section" href="#rule-7-use-business-language-not-technical-terms"><span class="heading-link-icon">#</span></a></h2>
<p>Write tests using domain language rather than implementation details.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="js"><code><span class="line"><span style="color:#51597D;font-style:italic">// ❌ Bad</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should update state</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should dispatch action</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should modify DOM</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// ✅ Good</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should save customer order</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should update cart total</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should mark order as delivered</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="// ❌ Bad
it(&#34;should update state&#34;, () => {});
it(&#34;should dispatch action&#34;, () => {});
it(&#34;should modify DOM&#34;, () => {});

// ✅ Good
it(&#34;should save customer order&#34;, () => {});
it(&#34;should update cart total&#34;, () => {});
it(&#34;should mark order as delivered&#34;, () => {});" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><strong>Generic Pattern:</strong> <code>should [business action] [business entity]</code></p>
<h2 id="rule-8-include-important-preconditions">Rule 8: Include Important Preconditions<a class="heading-link" aria-label="Link to section" href="#rule-8-include-important-preconditions"><span class="heading-link-icon">#</span></a></h2>
<p>Specify conditions that affect the behavior being tested.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="js"><code><span class="line"><span style="color:#51597D;font-style:italic">// ❌ Bad</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should enable button</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should show message</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should apply discount</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// ✅ Good</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should enable checkout when cart has items</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should show free shipping when total exceeds $100</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should apply discount when user is premium member</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="// ❌ Bad
it(&#34;should enable button&#34;, () => {});
it(&#34;should show message&#34;, () => {});
it(&#34;should apply discount&#34;, () => {});

// ✅ Good
it(&#34;should enable checkout when cart has items&#34;, () => {});
it(&#34;should show free shipping when total exceeds $100&#34;, () => {});
it(&#34;should apply discount when user is premium member&#34;, () => {});" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><strong>Generic Pattern:</strong> <code>should [expected behavior] when [precondition]</code></p>
<h2 id="rule-9-name-ui-feedback-tests-from-user-perspective">Rule 9: Name UI Feedback Tests from User Perspective<a class="heading-link" aria-label="Link to section" href="#rule-9-name-ui-feedback-tests-from-user-perspective"><span class="heading-link-icon">#</span></a></h2>
<p>Describe visual changes as users would perceive them.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="js"><code><span class="line"><span style="color:#51597D;font-style:italic">// ❌ Bad</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should set error class</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should toggle visibility</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should update styles</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// ✅ Good</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should highlight search box in red when empty</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should show green checkmark when password is strong</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should disable submit button while processing</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="// ❌ Bad
it(&#34;should set error class&#34;, () => {});
it(&#34;should toggle visibility&#34;, () => {});
it(&#34;should update styles&#34;, () => {});

// ✅ Good
it(&#34;should highlight search box in red when empty&#34;, () => {});
it(&#34;should show green checkmark when password is strong&#34;, () => {});
it(&#34;should disable submit button while processing&#34;, () => {});" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><strong>Generic Pattern:</strong> <code>should [visual change] when [user action/condition]</code></p>
<h2 id="rule-10-structure-complex-workflows-step-by-step">Rule 10: Structure Complex Workflows Step by Step<a class="heading-link" aria-label="Link to section" href="#rule-10-structure-complex-workflows-step-by-step"><span class="heading-link-icon">#</span></a></h2>
<p>Break down complex processes into clear steps.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="js"><code><span class="line"><span style="color:#51597D;font-style:italic">// ❌ Bad</span></span>
<span class="line"><span style="color:#7AA2F7">describe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">Checkout</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should process checkout</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should handle shipping</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should complete order</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">})</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// ✅ Good</span></span>
<span class="line"><span style="color:#7AA2F7">describe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">Checkout Process</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should first validate items are in stock</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should then collect shipping address</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should finally process payment</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  describe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">after successful payment</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">    it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should display order confirmation</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">    it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should send confirmation email</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">})</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="// ❌ Bad
describe(&#34;Checkout&#34;, () => {
  it(&#34;should process checkout&#34;, () => {});
  it(&#34;should handle shipping&#34;, () => {});
  it(&#34;should complete order&#34;, () => {});
});

// ✅ Good
describe(&#34;Checkout Process&#34;, () => {
  it(&#34;should first validate items are in stock&#34;, () => {});
  it(&#34;should then collect shipping address&#34;, () => {});
  it(&#34;should finally process payment&#34;, () => {});

  describe(&#34;after successful payment&#34;, () => {
    it(&#34;should display order confirmation&#34;, () => {});
    it(&#34;should send confirmation email&#34;, () => {});
  });
});" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><strong>Generic Pattern:</strong></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="js"><code><span class="line"><span style="color:#7AA2F7">describe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">[Complex Process]</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should first [initial step]</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should then [next step]</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should finally [final step]</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  describe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">after [key milestone]</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">    it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should [follow-up action]</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">})</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="describe(&#34;[Complex Process]&#34;, () => {
  it(&#34;should first [initial step]&#34;, () => {});
  it(&#34;should then [next step]&#34;, () => {});
  it(&#34;should finally [final step]&#34;, () => {});

  describe(&#34;after [key milestone]&#34;, () => {
    it(&#34;should [follow-up action]&#34;, () => {});
  });
});" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h2 id="complete-example">Complete Example<a class="heading-link" aria-label="Link to section" href="#complete-example"><span class="heading-link-icon">#</span></a></h2>
<p>Here’s a comprehensive example showing how to combine all these rules:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="js"><code><span class="line"><span style="color:#51597D;font-style:italic">// ❌ Bad</span></span>
<span class="line"><span style="color:#7AA2F7">describe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">ShoppingCart</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">test adding item</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">check total</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">handle checkout</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">})</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// ✅ Good</span></span>
<span class="line"><span style="color:#7AA2F7">describe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">ShoppingCart</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  describe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">when adding items</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">    it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should add item to cart when add button is clicked</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">    it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should update total price immediately</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">    it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should show item count badge</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  describe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">when cart is empty</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">    it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should display empty cart message</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">    it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should disable checkout button</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  describe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">during checkout process</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">    it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should validate stock before proceeding</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">    it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should show loading indicator while processing payment</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">    it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should display success message after completion</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">})</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="// ❌ Bad
describe(&#34;ShoppingCart&#34;, () => {
  it(&#34;test adding item&#34;, () => {});
  it(&#34;check total&#34;, () => {});
  it(&#34;handle checkout&#34;, () => {});
});

// ✅ Good
describe(&#34;ShoppingCart&#34;, () => {
  describe(&#34;when adding items&#34;, () => {
    it(&#34;should add item to cart when add button is clicked&#34;, () => {});
    it(&#34;should update total price immediately&#34;, () => {});
    it(&#34;should show item count badge&#34;, () => {});
  });

  describe(&#34;when cart is empty&#34;, () => {
    it(&#34;should display empty cart message&#34;, () => {});
    it(&#34;should disable checkout button&#34;, () => {});
  });

  describe(&#34;during checkout process&#34;, () => {
    it(&#34;should validate stock before proceeding&#34;, () => {});
    it(&#34;should show loading indicator while processing payment&#34;, () => {});
    it(&#34;should display success message after completion&#34;, () => {});
  });
});" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h2 id="test-name-checklist">Test Name Checklist<a class="heading-link" aria-label="Link to section" href="#test-name-checklist"><span class="heading-link-icon">#</span></a></h2>
<p>Before committing your test, verify that its name:</p>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled/> Starts with “should”</li>
<li class="task-list-item"><input type="checkbox" disabled/> Uses a clear action verb</li>
<li class="task-list-item"><input type="checkbox" disabled/> Specifies the trigger condition</li>
<li class="task-list-item"><input type="checkbox" disabled/> Uses business language</li>
<li class="task-list-item"><input type="checkbox" disabled/> Describes visible behavior</li>
<li class="task-list-item"><input type="checkbox" disabled/> Is specific enough for debugging</li>
<li class="task-list-item"><input type="checkbox" disabled/> Groups logically with related tests</li>
</ul>
<h2 id="conclusion">Conclusion<a class="heading-link" aria-label="Link to section" href="#conclusion"><span class="heading-link-icon">#</span></a></h2>
<p>Thoughtful test naming is a fundamental building block in the broader landscape of writing better tests. To maintain consistency across your team:</p>
<ol>
<li>Document your naming conventions in detail</li>
<li>Share these guidelines with all team members</li>
<li>Integrate the guidelines into your development workflow</li>
</ol>
<p>For teams using AI tools like GitHub Copilot:</p>
<ul>
<li>Incorporate these guidelines into your project documentation</li>
<li>Link the markdown file containing these rules to Copilot</li>
<li>This integration allows Copilot to suggest test names aligned with your conventions</li>
</ul>
<p>For more information on linking documentation to Copilot, see:
<a href="https://visualstudiomagazine.com/Articles/2024/09/09/VS-Code-Experiments-Boost-AI-Copilot-Functionality.aspx" rel="noopener noreferrer" target="_blank">VS Code Experiments Boost AI Copilot Functionality</a></p>
<p>By following these steps, you can ensure consistent, high-quality test naming across your entire project.</p> </article> <script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).only=e;window.dispatchEvent(new Event("astro:only"));})();</script><astro-island uid="Z1XneyL" component-url="/_astro/presentation.C3Wa0mjp.js" component-export="VMarkBlogRenderer" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;containerSelector&quot;:[0,&quot;#article&quot;],&quot;class&quot;:[0,&quot;astro-vj4tpspi&quot;]}" ssr client="only" opts="{&quot;name&quot;:&quot;VMarkBlogRenderer&quot;,&quot;value&quot;:&quot;react&quot;}"></astro-island> <!-- Fullscreen Modal Container using native dialog --><dialog id="mermaid-modal" class="mermaid-modal" aria-label="Fullscreen diagram view"> <div class="mermaid-modal-content"> <button class="mermaid-modal-close" aria-label="Close fullscreen view" type="button"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <line x1="18" y1="6" x2="6" y2="18"></line> <line x1="6" y1="6" x2="18" y2="18"></line> </svg> </button> <div class="mermaid-modal-diagram"></div> <div class="mermaid-modal-hint">Press <kbd>Esc</kbd> or click outside to close</div> </div> </dialog>  <script type="module">const p=new Set;function g(){const e=document.getElementById("mermaid-modal"),c=e?.querySelector(".mermaid-modal-diagram"),f=e?.querySelector(".mermaid-modal-close");if(!e||!c)return;document.querySelectorAll('svg[id^="mermaid-"]').forEach(t=>{if(!t.id.match(/^mermaid-\d+$/)||p.has(t.id)||t.parentElement?.classList.contains("mermaid-fullscreen-wrapper")||t.closest(".mermaid-modal"))return;p.add(t.id);const n=document.createElement("div");n.className="mermaid-fullscreen-wrapper mermaid-clickable",n.setAttribute("tabindex","0"),n.setAttribute("role","button"),n.setAttribute("aria-label","Click to view diagram fullscreen"),t.parentElement?.insertBefore(n,t),n.appendChild(t);const o=document.createElement("div");o.className="mermaid-expand-icon",o.innerHTML=`
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
</li> <li class="astro-vj4tpspi">Small tips and trick</li> </ul> </div> <a href="https://alex-op-newsletter.beehiiv.com/subscribe?utm_source=blog&utm_medium=post&utm_campaign=post_frontend-testing-guide-10-essential-rules" target="_blank" rel="noopener noreferrer" id="newsletter-subscribe-button" class="inline-flex items-center justify-center gap-2 rounded-full bg-skin-accent px-6 py-3 text-base font-semibold text-skin-inverted shadow-md transition-all duration-200 hover:scale-[1.02] hover:transform hover:opacity-90 astro-vj4tpspi"> <svg class="h-5 w-5 fill-current astro-vj4tpspi" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg>
Subscribe Now
</a> <button id="newsletter-dismiss" data-post-slug="frontend-testing-guide-10-essential-rules" class="absolute right-3 top-3 rounded-full p-1 text-skin-base transition-all duration-200 hover:bg-skin-accent hover:bg-opacity-10 hover:text-skin-accent astro-vj4tpspi" aria-label="Close notification"> <svg class="h-5 w-5 astro-vj4tpspi" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class="astro-vj4tpspi"></path> </svg> </button> </div> </div> </div> <ul class="my-8 flex flex-wrap gap-2 astro-vj4tpspi"> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/testing/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-2"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">testing</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/vitest/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-3"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">vitest</span>   </a> </li>  </ul> <div class="flex flex-col-reverse items-center justify-between gap-6 sm:flex-row-reverse sm:items-end sm:gap-4 astro-vj4tpspi"> <button id="back-to-top" class="focus-outline whitespace-nowrap py-1 hover:opacity-75 astro-vj4tpspi"> <svg xmlns="http://www.w3.org/2000/svg" class="rotate-90 astro-vj4tpspi"> <path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg> <span class="astro-vj4tpspi">Back to Top</span> </button> <div class="social-icons astro-wkojbtzc"> <span class="italic astro-wkojbtzc">Share this post on:</span> <div class="text-center astro-wkojbtzc"> <a href="https://wa.me/?text=https://alexop.dev/posts/frontend-testing-guide-10-essential-rules/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via WhatsApp" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"></path>
      <path d="M9 10a0.5 .5 0 0 0 1 0v-1a0.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a0.5 .5 0 0 0 0 -1h-1a0.5 .5 0 0 0 0 1"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via WhatsApp</span> </a><a href="https://www.facebook.com/sharer.php?u=https://alexop.dev/posts/frontend-testing-guide-10-essential-rules/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Facebook" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"
    ></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on Facebook</span> </a><a href="https://x.com/intent/tweet?url=https://alexop.dev/posts/frontend-testing-guide-10-essential-rules/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Tweet this post" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Tweet this post</span> </a><a href="https://t.me/share/url?url=https://alexop.dev/posts/frontend-testing-guide-10-essential-rules/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via Telegram" target="_blank" rel="noopener noreferrer"> <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon-tabler"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"></path>
      </svg> <span class="sr-only astro-wkojbtzc">Share this post via Telegram</span> </a><a href="https://pinterest.com/pin/create/button/?url=https://alexop.dev/posts/frontend-testing-guide-10-essential-rules/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Pinterest" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <line x1="8" y1="20" x2="12" y2="11"></line>
      <path d="M10.7 14c.437 1.263 1.43 2 2.55 2c2.071 0 3.75 -1.554 3.75 -4a5 5 0 1 0 -9.7 1.7"></path>
      <circle cx="12" cy="12" r="9"></circle>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post on Pinterest</span> </a><a href="mailto:?subject=See%20this%20post&#38;body=https://alexop.dev/posts/frontend-testing-guide-10-essential-rules/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via email" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via email</span> </a><a href="https://www.linkedin.com/shareArticle?mini=true&url=https://alexop.dev/posts/frontend-testing-guide-10-essential-rules/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
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
</h2> <div class="md:grid-cols-3 grid grid-cols-1 gap-6 astro-vj4tpspi"> <a href="/posts/stop-white-box-testing-vue/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">Stop White Box Testing Vue Components Use Testing Library Instead</h3> <p class="related-post-description astro-vj4tpspi"> White Box testing makes your Vue tests fragile and misleading. In this post, I’ll show you how Testing Library helps you write Black Box tests that are resilient, realistic, and focused on actual user behavior </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-04-19T00:00:00.000Z">Apr 19, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> vue </span> </div> </div> </a><a href="/posts/visual-regression-testing-with-vue-and-vitest-browser/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">How to Do Visual Regression Testing in Vue with Vitest?</h3> <p class="related-post-description astro-vj4tpspi"> Learn how to implement visual regression testing in Vue.js using Vitest&#39;s browser mode. This comprehensive guide covers setting up screenshot-based testing, creating component stories, and integrating with CI/CD pipelines for automated visual testing. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-02-22T00:00:00.000Z">Feb 22, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> vue </span> </div> </div> </a><a href="/posts/how-to-test-vue-router-components-with-testing-library-and-vitest/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">How to Test Vue Router Components with Testing Library and Vitest</h3> <p class="related-post-description astro-vj4tpspi"> Learn how to test Vue Router components using Testing Library and Vitest. This guide covers real router integration, mocked router setups, and best practices for testing navigation, route guards, and dynamic components in Vue applications. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-02-16T00:00:00.000Z">Feb 16, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> vue </span> </div> </div> </a> </div> </div> </main> <footer class="mt-auto astro-sz7xmlte"> <div class="max-w-5xl mx-auto px-4"> <hr class="border-skin-line" aria-hidden="true"> </div> <div class="footer-wrapper astro-sz7xmlte"> <div class="footer-content astro-sz7xmlte"> <div class="copyright-wrapper astro-sz7xmlte"> <span class="astro-sz7xmlte">Copyright &#169; 2026</span> <span class="separator astro-sz7xmlte">&nbsp;|&nbsp;</span> <span class="astro-sz7xmlte">All rights reserved.</span> </div> <div class="rss-prompt astro-sz7xmlte"> <a href="/rss.xml" class="rss-link group astro-sz7xmlte" title="Never miss a post - Subscribe via RSS" onclick="if (window.plausible) window.plausible('RSS Subscribe', { props: { location: 'footer' } })"> <div class="flex items-center gap-2 astro-sz7xmlte"> <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-skin-accent group-hover:animate-pulse astro-sz7xmlte"><path fill="currentColor" d="M19 20.001C19 11.729 12.271 5 4 5v2c7.168 0 13 5.832 13 13.001h2z" class="astro-sz7xmlte"></path><path fill="currentColor" d="M12 20.001h2C14 14.486 9.514 10 4 10v2c4.411 0 8 3.589 8 8.001z" class="astro-sz7xmlte"></path><circle cx="6" cy="18" r="2" fill="currentColor" class="astro-sz7xmlte"></circle> </svg> <span class="text-sm astro-sz7xmlte">Subscribe via RSS</span> </div> </a> </div> <div class="social-icons flex astro-upu6fzxr"> <a href="https://github.com/alexanderop" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title=" alexop.dev on Github" target="_blank" rel="noopener noreferrer"> <svg
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
    </script> </body> </html>  <script>(function(){const postSlug = "frontend-testing-guide-10-essential-rules";

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
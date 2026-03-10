# Source: https://alexop.dev/posts/vue3_testing_pyramid_vitest_browser_mode

<!DOCTYPE html><html lang="en" class="scroll-smooth astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/posts/vue3_testing_pyramid_vitest_browser_mode/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>Vue 3 Testing Pyramid: A Practical Guide with Vitest Browser Mode | alexop.dev</title><meta name="title" content="Vue 3 Testing Pyramid: A Practical Guide with Vitest Browser Mode | alexop.dev"><meta name="description" content="Learn a practical testing strategy for Vue 3 applications using composable unit tests, Vitest browser mode integration tests, and visual regression testing."><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="Vue 3 Testing Pyramid: A Practical Guide with Vitest Browser Mode | alexop.dev"><meta property="og:description" content="Learn a practical testing strategy for Vue 3 applications using composable unit tests, Vitest browser mode integration tests, and visual regression testing."><meta property="og:url" content="https://alexop.dev/posts/vue3_testing_pyramid_vitest_browser_mode/"><meta property="og:image" content="https://alexop.dev/posts/vue-3-testing-pyramid-a-practical-guide-with-vitest-browser-mode/index.png"><meta property="og:type" content="article"><!-- Article Published/Modified time --><meta property="article:published_time" content="2025-12-14T00:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/posts/vue3_testing_pyramid_vitest_browser_mode/"><meta property="twitter:title" content="Vue 3 Testing Pyramid: A Practical Guide with Vitest Browser Mode | alexop.dev"><meta property="twitter:description" content="Learn a practical testing strategy for Vue 3 applications using composable unit tests, Vitest browser mode integration tests, and visual regression testing."><meta property="twitter:image" content="https://alexop.dev/posts/vue-3-testing-pyramid-a-practical-guide-with-vitest-browser-mode/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"Vue 3 Testing Pyramid: A Practical Guide with Vitest Browser Mode | alexop.dev","description":"Learn a practical testing strategy for Vue 3 applications using composable unit tests, Vitest browser mode integration tests, and visual regression testing.","image":"https://alexop.dev/posts/vue-3-testing-pyramid-a-practical-guide-with-vitest-browser-mode/index.png","datePublished":"2025-12-14T00:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
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
</style><style>[data-astro-transition-scope="astro-plk3gbjq-1"] { view-transition-name: vue-3-testing-pyramid-a-practical-guide-with-vitest-browser-mode; }@layer astro { ::view-transition-old(vue-3-testing-pyramid-a-practical-guide-with-vitest-browser-mode) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(vue-3-testing-pyramid-a-practical-guide-with-vitest-browser-mode) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(vue-3-testing-pyramid-a-practical-guide-with-vitest-browser-mode) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(vue-3-testing-pyramid-a-practical-guide-with-vitest-browser-mode) { 
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
</style><style>:root{--color-skin-card: rgb(var(--color-card));--color-skin-card-muted: rgb(var(--color-card-muted));--color-skin-border: rgb(var(--color-border));--color-skin-text-base: rgb(var(--color-text-base));--color-skin-accent: rgb(var(--color-accent));--color-skin-note: rgb(59, 130, 246);--color-skin-tip: rgb(16, 185, 129);--color-skin-caution: rgb(245, 158, 11);--color-skin-danger: rgb(239, 68, 68);--color-skin-info: rgb(99, 102, 241)}.aside:where(.astro-37uy2q7c){background-color:var(--color-skin-card);border-left:4px solid;border-radius:.5rem;box-shadow:0 4px 6px -1px #0000001a,0 2px 4px -1px #0000000f;margin:1.5rem 0;transition:all .3s ease}.aside:where(.astro-37uy2q7c):hover{box-shadow:0 10px 15px -3px #0000001a,0 4px 6px -2px #0000000d}.aside-content:where(.astro-37uy2q7c){padding:1rem 1.5rem}.aside-title:where(.astro-37uy2q7c){display:flex;align-items:center;font-weight:700;font-size:1.1rem;margin-bottom:.75rem}.aside-emoji:where(.astro-37uy2q7c){font-size:1.4rem;margin-right:.75rem}.aside-body:where(.astro-37uy2q7c){color:var(--color-skin-text-base);font-size:.95rem;line-height:1.6}.aside-note:where(.astro-37uy2q7c){background-color:rgba(var(--color-skin-note),.1);border-left-color:var(--color-skin-note)}.aside-note:where(.astro-37uy2q7c) .aside-title:where(.astro-37uy2q7c){color:var(--color-skin-note)}.aside-tip:where(.astro-37uy2q7c){background-color:rgba(var(--color-skin-tip),.1);border-left-color:var(--color-skin-tip)}.aside-tip:where(.astro-37uy2q7c) .aside-title:where(.astro-37uy2q7c){color:var(--color-skin-tip)}.aside-caution:where(.astro-37uy2q7c){background-color:rgba(var(--color-skin-caution),.1);border-left-color:var(--color-skin-caution)}.aside-caution:where(.astro-37uy2q7c) .aside-title:where(.astro-37uy2q7c){color:var(--color-skin-caution)}.aside-danger:where(.astro-37uy2q7c){background-color:rgba(var(--color-skin-danger),.1);border-left-color:var(--color-skin-danger)}.aside-danger:where(.astro-37uy2q7c) .aside-title:where(.astro-37uy2q7c){color:var(--color-skin-danger)}.aside-info:where(.astro-37uy2q7c){background-color:rgba(var(--color-skin-info),.1);border-left-color:var(--color-skin-info)}.aside-info:where(.astro-37uy2q7c) .aside-title:where(.astro-37uy2q7c){color:var(--color-skin-info)}
</style><style>.collapsible:where(.astro-kncz7yy6){display:block!important;width:100%!important;max-width:100%!important;margin:1.5rem 0;border:1px solid rgb(var(--color-border));border-radius:.5rem;overflow:hidden}.collapsible-summary:where(.astro-kncz7yy6){display:flex;align-items:center;gap:.5rem;padding:.75rem 1rem;font-weight:500;cursor:pointer;background:rgb(var(--color-card));-webkit-user-select:none;-moz-user-select:none;user-select:none;list-style:none}.collapsible-summary:where(.astro-kncz7yy6)::-webkit-details-marker{display:none}.collapsible-summary:where(.astro-kncz7yy6):hover{background:rgb(var(--color-card-muted))}.collapsible-icon:where(.astro-kncz7yy6){display:flex;align-items:center;transition:transform .2s ease}.collapsible:where(.astro-kncz7yy6)[open] .collapsible-icon:where(.astro-kncz7yy6){transform:rotate(90deg)}.collapsible-content:where(.astro-kncz7yy6){width:100%!important;max-width:100%!important}.collapsible-content:where(.astro-kncz7yy6) pre{margin:0!important;border-radius:0!important;width:100%!important;max-width:100%!important}.collapsible-content:where(.astro-kncz7yy6)>*:first-child{margin-top:0}.collapsible-content:where(.astro-kncz7yy6)>*:last-child{margin-bottom:0}
</style><style>.prose details.collapsible{display:block!important;width:100%!important;max-width:100%!important}
</style><style>.internal-link-wrapper:where(.astro-3tyn5ojg){position:relative;display:inline-block}.internal-link:where(.astro-3tyn5ojg){--tw-text-opacity: 1;color:rgba(var(--color-accent),var(--tw-text-opacity, 1));text-decoration-line:underline;text-decoration-style:dashed;text-decoration-thickness:1px;text-underline-offset:4px;transition-property:all;transition-timing-function:cubic-bezier(.4,0,.2,1);transition-duration:.15s}.internal-link:where(.astro-3tyn5ojg):hover{text-decoration-style:solid}.internal-link:where(.astro-3tyn5ojg){cursor:pointer;display:inline}.preview-card:where(.astro-3tyn5ojg){display:block;position:absolute;bottom:calc(100% + 8px);left:50%;transform:translate(-50%);z-index:9999;width:320px;max-width:90vw;border-radius:.5rem;border-width:1px;--tw-border-opacity: 1;border-color:rgba(var(--color-border),var(--tw-border-opacity, 1));--tw-bg-opacity: 1;background-color:rgba(var(--color-card),var(--tw-bg-opacity, 1));--tw-shadow: 0 10px 15px -3px rgb(0 0 0 / .1), 0 4px 6px -4px rgb(0 0 0 / .1);--tw-shadow-colored: 0 10px 15px -3px var(--tw-shadow-color), 0 4px 6px -4px var(--tw-shadow-color);box-shadow:var(--tw-ring-offset-shadow, 0 0 #0000),var(--tw-ring-shadow, 0 0 #0000),var(--tw-shadow);opacity:0;visibility:hidden;transition:opacity .2s ease-in-out,visibility .2s ease-in-out}.preview-card:where(.astro-3tyn5ojg).is-fixed{position:fixed!important;bottom:auto!important;top:var(--pc-top, 0px)!important;left:var(--pc-left, 0px)!important;transform:none!important}.preview-content:where(.astro-3tyn5ojg){display:block;padding:1rem}.preview-title:where(.astro-3tyn5ojg){display:block;margin-bottom:.5rem;font-size:1rem;line-height:1.5rem;font-weight:600;--tw-text-opacity: 1;color:rgba(var(--color-text-base),var(--tw-text-opacity, 1));line-height:1.3}.preview-title:where(.astro-3tyn5ojg) .heading-link:where(.astro-3tyn5ojg){display:none!important}.preview-description:where(.astro-3tyn5ojg){display:block;margin-bottom:.75rem;font-size:.875rem;line-height:1.25rem;color:rgba(var(--color-text-base),.8);line-height:1.4;overflow:hidden;text-overflow:ellipsis;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical}.preview-tags:where(.astro-3tyn5ojg){margin-bottom:.5rem;display:flex;flex-wrap:wrap;gap:.375rem}.preview-tag:where(.astro-3tyn5ojg){border-radius:.25rem;padding:.125rem .5rem;font-size:.75rem;line-height:1rem;background-color:rgba(var(--color-accent),.1);--tw-text-opacity: 1;color:rgba(var(--color-accent),var(--tw-text-opacity, 1));font-weight:500}.preview-tag-more:where(.astro-3tyn5ojg){border-radius:.25rem;padding:.125rem .5rem;font-size:.75rem;line-height:1rem;--tw-bg-opacity: 1;background-color:rgba(var(--color-fill),var(--tw-bg-opacity, 1));color:rgba(var(--color-text-base),.6);font-weight:500}.preview-date:where(.astro-3tyn5ojg){font-size:.75rem;line-height:1rem;color:rgba(var(--color-text-base),.6);display:block;margin-top:8px;font-style:italic}.preview-card:where(.astro-3tyn5ojg):after{content:"";position:absolute;top:100%;left:50%;transform:translate(-50%);border:6px solid transparent;border-top-color:var(--color-card)}.preview-card:where(.astro-3tyn5ojg).is-fixed:after{display:none}
</style><style>[data-astro-transition-scope="astro-36ssibgs-2"] { view-transition-name: vue; }@layer astro { ::view-transition-old(vue) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-3"] { view-transition-name: testing; }@layer astro { ::view-transition-old(testing) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-4"] { view-transition-name: vitest; }@layer astro { ::view-transition-old(vitest) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-5"] { view-transition-name: typescript; }@layer astro { ::view-transition-old(typescript) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-6"] { view-transition-name: accessibility; }@layer astro { ::view-transition-old(accessibility) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(accessibility) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(accessibility) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(accessibility) { 
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <div class="mx-auto flex w-full max-w-5xl justify-start px-2 astro-vj4tpspi"> <button class="focus-outline mb-2 mt-8 flex hover:opacity-75 astro-vj4tpspi" onclick="(() => (history.length === 1) ? window.location = '/' : history.back())()"> <svg xmlns="http://www.w3.org/2000/svg" class="astro-vj4tpspi"><path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg><span class="astro-vj4tpspi">Go back</span> </button> </div> <main data-pagefind-body id="main-content" class="relative astro-vj4tpspi"> <h1 class="post-title astro-vj4tpspi" data-astro-transition-scope="astro-plk3gbjq-1">Vue 3 Testing Pyramid: A Practical Guide with Vitest Browser Mode</h1> <div class="my-2 flex items-center justify-between astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-100 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-base"><time dateTime="2025-12-14T00:00:00.000Z">Dec 14, 2025</time><span class="sr-only"> at </span></span></div> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="ZsWCNV" prefix="r3" component-url="/_astro/PostCopyButton.-PGtk4At.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;title&quot;:[0,&quot;Vue 3 Testing Pyramid: A Practical Guide with Vitest Browser Mode&quot;],&quot;content&quot;:[0,&quot;import Alert from \&quot;@features/mdx-components/components/Alert.astro\&quot;;\nimport Aside from \&quot;@features/mdx-components/components/Aside.astro\&quot;;\nimport InternalLink from \&quot;@features/mdx-components/components/InternalLink.astro\&quot;;\nimport Collapsible from \&quot;@features/mdx-components/components/Collapsible.astro\&quot;;\nimport Figure from \&quot;@features/mdx-components/components/Figure.astro\&quot;;\nimport testingPyramid from \&quot;@assets/images/vueTestingStrategy/testingPyramid.png\&quot;;\nimport monolithVsComp from \&quot;@assets/images/vueTestingStrategy/monolithVsComponent.png\&quot;;\nimport factoryPattern from \&quot;@assets/images/vueTestingStrategy/factoryPattern.png\&quot;;\nimport aiDrivenTesting from \&quot;@assets/images/vueTestingStrategy/aiDrivenTesting.png\&quot;;\nimport cover from \&quot;@assets/images/vueTestingStrategy/vueTestingPyramidCover.png\&quot;;\nimport integrationVsComponent from \&quot;@assets/images/claude/integrationVsComponent.png\&quot;;\n\n&lt;Figure src={cover} alt=\&quot;Vue 3 Testing Pyramid with Vitest Browser Mode\&quot; size=\&quot;large\&quot; /&gt;\n\n## Quick Summary\n\nThis post covers a practical testing approach for Vue 3 applications:\n\n- Composable unit tests for fast logic verification\n- Integration tests with Vitest browser mode for realistic user flows\n- Accessibility and visual tests for critical screen checks\n- Simplified data factories to manage test data easily\n\n## Table of Contents\n\n## Introduction\n\nI&#39;m building a workout tracking PWA with Vue 3, and I needed confidence that my changes work. Not the \&quot;I clicked around and it seems fine\&quot; kind of confidence, but the \&quot;I can refactor this and know immediately if I broke something\&quot; kind.\n\nHere&#39;s the thing: I don&#39;t write much code myself anymore. AI tools handle most of the implementation. I describe what I want, review the changes, and guide the direction—but the actual keystrokes? That&#39;s the AI. This workflow is incredibly productive, but it comes with a catch: I need a robust safety net.\n\nWhen an AI writes code, tests become even more critical. They serve three purposes:\n\n1. **Catch bugs** before users do\n2. **Enable refactoring** — change code freely knowing tests will catch regressions\n3. **Document behavior** — tests act as a \&quot;user manual\&quot; for your code\n\n&lt;Alert type=\&quot;tip\&quot; title=\&quot;Don&#39;t Forget the Basics\&quot;&gt;\n  Tests are just one part of your safety net. **Linting** (ESLint) catches code style issues and potential bugs statically. **Type checking** (TypeScript) catches type errors at compile time. Run all three—lint, type check, and tests—before every commit.\n&lt;/Alert&gt;\n\n## Before We Start: A Mini Glossary\n\nTesting has a lot of jargon. Here&#39;s a cheat sheet to keep handy as you read:\n\n| Term | Meaning |\n|------|---------|\n| **Unit Test** | Testing a tiny, isolated piece of code (like a single function) to ensure it returns the right value |\n| **Integration Test** | Testing how multiple pieces work together (e.g., clicking a button and seeing a database update) |\n| **Regression** | A bug where a feature that used to work stops working after you change something else |\n| **Mock** | A fake version of a complex tool (like faking an API call) so you can test without relying on the internet |\n| **Assertion** | A line of code that checks if a result matches your expectation (e.g., `expect(2 + 2).toBe(4)`) |\n| **A11y** | Short for \&quot;Accessibility\&quot; (there are 11 letters between A and y) |\n\n---\n\n## Your Architecture Shapes Your Testing Strategy\n\nYour testing strategy reflects your frontend architecture. They&#39;re not independent choices.\n\nIf you write **monolithic components** (huge files with logic and UI mixed), testing is a nightmare. If you use **composables** (extracting logic into separate files), testing becomes straightforward.\n\n&lt;Figure src={monolithVsComp} alt=\&quot;Comparison of monolithic component with mixed logic vs composable pattern with extracted logic\&quot; caption=\&quot;Monolithic components trap logic inside; composables make it testable\&quot; size=\&quot;large\&quot; /&gt;\n\n### Bad vs. Good Architecture\n\n#### The Monolith (Hard to Test)\n\nTo test the timer logic here, you have to mount the whole component, find the button, click it, and wait for the UI to update. It&#39;s slow and fragile.\n\n```vue\n&lt;script setup&gt;\nimport { ref } from &#39;vue&#39;\n// Logic is trapped inside the component!\nconst time = ref(0)\nconst start = () =&gt; setInterval(() =&gt; time.value++, 1000)\n&lt;/script&gt;\n\n&lt;template&gt;\n  &lt;button @click=\&quot;start\&quot;&gt;{{ time }}&lt;/button&gt;\n&lt;/template&gt;\n```\n\n#### The Composable (Easy to Test)\n\nHere, the logic lives in a plain TypeScript file. We can test `useTimer` without ever looking at a Vue component or HTML.\n\n```typescript\n// useTimer.ts\nexport function useTimer() {\n  const time = ref(0)\n  const start = () =&gt; setInterval(() =&gt; time.value++, 1000)\n  return { time, start }\n}\n```\n\nMy strategy relies on this \&quot;composable-first\&quot; approach. However, for the UI itself, we use integration tests. These tests don&#39;t care about your code structure; they test behavior through the UI, just like a user would.\n\n&lt;Aside type=\&quot;tip\&quot; title=\&quot;Learn More About Composable Testing\&quot;&gt;\n  For a deep dive into testing composables specifically, check out &lt;InternalLink slug=\&quot;how-to-test-vue-composables\&quot;&gt;How to Test Vue Composables&lt;/InternalLink&gt;.\n&lt;/Aside&gt;\n\n---\n\n## The Testing Pyramid\n\nMy approach inverts the traditional pyramid. **Integration tests make up ~70%** of my test suite because Vitest browser mode makes them fast and reliable. Composable unit tests cover ~20% for pure logic, and the remaining ~10% goes to accessibility and visual regression tests.\n\n{/* TODO: Regenerate testingPyramid.png to show inverted distribution: Integration (70%), Unit (20%), A11y/Visual (10%) */}\n&lt;Figure src={testingPyramid} alt=\&quot;Testing strategy showing integration tests as the foundation (~70%), unit tests for composables (~20%), and visual/a11y tests at the top (~10%)\&quot; caption=\&quot;Integration tests form the foundation of this strategy\&quot; size=\&quot;large\&quot; /&gt;\n\n---\n\n## The Environment: Browser Mode vs JSDOM\n\nIn the past, most Vue tests ran in JSDOM. Now, I recommend **Vitest Browser Mode** with `vitest-browser-vue`. Here&#39;s why:\n\n| Feature | JSDOM (Old Standard) | Vitest Browser Mode (New Standard) |\n|---------|---------------------|-----------------------------------|\n| **What is it?** | A simulation of a browser running in Node.js (Fake) | A real instance of Chrome/Firefox running your tests (Real) |\n| **Accuracy** | Good for logic, bad for layout/CSS | 100% accurate — it&#39;s a real browser |\n| **Debugging** | Hard. You stare at console logs | Easy. You can watch the test click buttons on your screen |\n| **Speed** | Surprisingly slow (see benchmarks below) | Often faster due to native browser APIs |\n| **API** | Requires Testing Library for DOM queries | Built-in `page` object with Playwright-like locators |\n\n### Real-World Performance Comparison\n\nA common misconception is that browser mode is slower. In my testing with the same test suite, **browser mode was actually 4x faster**:\n\n| Metric | Vitest Browser Mode (Chromium) | Vitest Unit Mode (JSDOM) |\n|--------|-------------------------------|--------------------------|\n| **Total Duration** | 13.59s 🚀 | 53.72s |\n| **Test Files** | 15 | 15 |\n| **Total Tests** | 82 (78 passed) | 82 (78 passed) |\n| **Setup Time** | 4.48s | 53ms |\n| **Import Time** | 19.84s | 7.98s |\n| **Test Execution Time** | 29.48s | 40.53s |\n\nWhile browser mode has higher setup time (launching Chromium), the actual test execution is faster because it uses native browser APIs instead of JSDOM&#39;s JavaScript reimplementation. The total duration speaks for itself.\n\n&lt;Aside type=\&quot;tip\&quot; title=\&quot;Why Vitest Browser Mode for AI Workflows?\&quot;&gt;\n  Vitest browser mode handles everything in one command. The browser launches, components render, and tests run. It&#39;s much simpler for AI assistants (and humans) to manage than setting up complex End-to-End servers.\n&lt;/Aside&gt;\n\n### Setting Up Vitest Browser Mode\n\nVitest 4.0+ requires a browser provider package. Install the dependencies:\n\n```bash\nnpm install -D vitest @vitest/browser-playwright vitest-browser-vue playwright\n```\n\n&lt;Alert type=\&quot;note\&quot; title=\&quot;Provider Options\&quot;&gt;\n  You can use `@vitest/browser-playwright` (recommended) or `@vitest/browser-webdriverio`. Playwright offers the best developer experience with automatic browser downloads.\n&lt;/Alert&gt;\n\n### No More Testing Library\n\nWith Vitest browser mode, you don&#39;t need `@testing-library/vue` anymore. The `page` object from `vitest/browser` provides Playwright-like locators that are more powerful and consistent:\n\n```typescript\nimport { page, userEvent } from &#39;vitest/browser&#39;\n\n// Instead of screen.getByRole(), use page.getByRole()\nconst button = page.getByRole(&#39;button&#39;, { name: /submit/i })\nawait userEvent.click(button)\n```\n\n\n---\n\n## Layer 1: Composable Unit Tests\n\nComposables are just functions. You test them by calling them and checking the result.\n\n### A Simple Composable Test\n\n```typescript\nimport { describe, expect, it } from &#39;vitest&#39;\nimport { useDialogState } from &#39;@/composables/useDialogState&#39;\n\ndescribe(&#39;useDialogState&#39;, () =&gt; {\n  it(&#39;starts closed&#39;, () =&gt; {\n    // 1. Run the code\n    const { isOpen } = useDialogState()\n    // 2. Assert the result\n    expect(isOpen.value).toBe(false)\n  })\n\n  it(&#39;opens when requested&#39;, () =&gt; {\n    const { isOpen, open } = useDialogState()\n    open()\n    expect(isOpen.value).toBe(true)\n  })\n})\n```\n\nNo HTML, no mounting, no complexity. Just functions and values.\n\n&lt;Aside type=\&quot;tip\&quot; title=\&quot;Deep Dive: Composable Testing\&quot;&gt;\n  For comprehensive patterns including async composables, lifecycle hooks, and dependency injection, see &lt;InternalLink slug=\&quot;how-to-test-vue-composables\&quot;&gt;How to Test Vue Composables&lt;/InternalLink&gt;.\n&lt;/Aside&gt;\n\n---\n\n## Managing Test Data with Factories\n\nWhen writing tests, you constantly need data. For example, to test a \&quot;Profile Page,\&quot; you need a \&quot;User.\&quot;\n\nBeginners often copy-paste the same big object into every single test file. This is messy and hard to maintain. If you add a new required field (like `phoneNumber`) to your User, you have to go back and fix every single test.\n\nThe solution is the **Factory Pattern**. Think of it like ordering a pizza: there&#39;s a \&quot;standard\&quot; pizza (Cheese &amp; Tomato), and you only specify the changes you want (\&quot;...but add pepperoni\&quot;).\n\n&lt;Figure src={factoryPattern} alt=\&quot;Factory pattern showing default data merged with overrides to create test objects\&quot; caption=\&quot;Factories: define defaults once, override only what you need\&quot; size=\&quot;large\&quot; /&gt;\n\n### The Problem: Hard-coded Data\n\nWithout factories, your tests look like this. Notice how much noise there is just to test one specific thing:\n\n```typescript\n// ❌ BAD: Repeating data everywhere\nit(&#39;shows admin badge&#39;, () =&gt; {\n  const user = {\n    id: &#39;1&#39;,\n    name: &#39;John Doe&#39;,\n    email: &#39;john@example.com&#39;,\n    role: &#39;admin&#39;, // This is the only line we actually care about!\n    isActive: true,\n    createdAt: &#39;2023-01-01&#39;\n  }\n\n  // ... test logic ...\n})\n```\n\n### The Solution: A Simple Factory Function\n\nA factory is just a plain TypeScript function. It holds the \&quot;Standard Pizza\&quot; defaults and lets you overwrite specific slices using the spread operator (`...`).\n\n```typescript\n// factories/userFactory.ts\n\n// 1. Define the shape of your data\ninterface User {\n  id: string;\n  name: string;\n  role: &#39;user&#39; | &#39;admin&#39;;\n  isActive: boolean;\n}\n\n// 2. Define your \&quot;Standard Pizza\&quot; (Sensible Defaults)\nconst defaultUser: User = {\n  id: &#39;123&#39;,\n  name: &#39;Test User&#39;,\n  role: &#39;user&#39;,\n  isActive: true\n}\n\n// 3. The Factory Function\n// It takes \&quot;overrides\&quot; (partial data) and merges them on top of the defaults\nexport function createUser(overrides: Partial&lt;User&gt; = {}): User {\n  return {\n    ...defaultUser, // Start with defaults\n    ...overrides    // Apply your specific changes\n  };\n}\n```\n\n### Using It in Tests\n\nNow your tests focus purely on what matters for that specific scenario:\n\n```typescript\n// ✅ GOOD: Clean and focused\n\n// Scenario 1: I just need ANY user, I don&#39;t care about details\nconst basicUser = createUser();\n// Result: { id: &#39;123&#39;, name: &#39;Test User&#39;, role: &#39;user&#39;, ... }\n\n// Scenario 2: I specifically need an ADMIN\nconst admin = createUser({ role: &#39;admin&#39; });\n// Result: { id: &#39;123&#39;, name: &#39;Test User&#39;, role: &#39;admin&#39;, ... }\n\n// Scenario 3: I need an INACTIVE user\nconst bannedUser = createUser({ isActive: false });\n// Result: { id: &#39;123&#39;, name: &#39;Test User&#39;, isActive: false, ... }\n```\n\nThis pattern keeps your tests readable and makes refactoring easy. If you add a new field to `User` later, you only update the `defaultUser` object in one place.\n\n### Factories Work at Every Layer\n\nThe beauty of factories is that they work for **both** unit tests and integration tests:\n\n```typescript\n// ✅ Unit Test: Testing a composable\nit(&#39;formats user display name&#39;, () =&gt; {\n  const user = createUser({ name: &#39;Jane Doe&#39;, role: &#39;admin&#39; })\n  const { displayName } = useUserProfile(user)\n  expect(displayName.value).toBe(&#39;Jane Doe (Admin)&#39;)\n})\n\n// ✅ Integration Test: Testing a rendered component\nit(&#39;shows admin badge in profile&#39;, async () =&gt; {\n  const admin = createUser({ role: &#39;admin&#39; })\n  await renderProfilePage({ user: admin })\n  await expect.element(page.getByText(&#39;Admin&#39;)).toBeVisible()\n})\n```\n\n&gt; **Key Insight:** Factories handle **data**. They don&#39;t care whether you&#39;re testing a function or a full page—they just give you clean, predictable objects.\n\n&lt;Aside type=\&quot;note\&quot; title=\&quot;In My Workout Tracker\&quot;&gt;\n  For my workout tracking PWA, I use factories like `createWorkout()`, `createExercise()`, and `createSet()`. The pattern scales nicely—start simple and add complexity only when your data relationships demand it.\n&lt;/Aside&gt;\n\n---\n\n## Layer 2: Integration Tests\n\nIntegration tests verify complete user flows. They render the app, click buttons, and check if the right things appear on screen.\n\n&lt;Alert type=\&quot;note\&quot; title=\&quot;Integration Test vs E2E Test: What&#39;s the Difference?\&quot;&gt;\n  In this post, **integration test** means:\n  - Real browser (Vitest browser mode)\n  - Real Vue components, router, Pinia, and user interactions\n  - **Mocked**: external APIs (via [MSW](https://mswjs.io/)), browser storage (IndexedDB), third-party services\n\n  **E2E test** means:\n  - Real browser\n  - **Zero mocking**—full stack (frontend + backend + database)\n  - Tests exactly how a user interacts with the production system\n\n  **Examples**: In my workout tracker, I mock IndexedDB but test real Vue components and user flows—that&#39;s an integration test. For an e-commerce site, you&#39;d mock the product API and payment gateway via MSW, but test the real checkout flow. If you spin up your actual backend and database, that&#39;s E2E.\n&lt;/Alert&gt;\n\n### Component Tests vs. Integration Tests\n\nVitest browser mode supports two approaches:\n\n&lt;Figure src={integrationVsComponent} alt=\&quot;Component test renders single component vs Integration test renders full App.vue with router and store\&quot; caption=\&quot;Component tests isolate one piece; integration tests render the full app\&quot; size=\&quot;large\&quot; /&gt;\n\n| Approach | What you render | Use case |\n|----------|-----------------|----------|\n| **Component test** | Single component (`render(MyButton)`) | Testing component behavior in isolation |\n| **Integration test** | Full app (`render(App)` with router, store) | Testing complete user flows across multiple components |\n\n**Component tests** are faster and more focused—great for testing a single component&#39;s props, events, and states.\n\n**Integration tests** render your entire `App.vue` with router and Pinia. The user can navigate between pages, fill forms, and see how components work together. This is where you catch bugs that only appear when components interact.\n\nFor most Vue apps, I recommend focusing on **integration tests**. They give you more confidence because they test what users actually experience.\n\n### The \&quot;Test App\&quot; Helper\n\nTo make testing easier, I use a helper function called `createTestApp`. It sets up your Router, Pinia (state), and renders your app using `vitest-browser-vue` so you don&#39;t have to repeat it in every file.\n\n```typescript\n// helpers/createTestApp.ts\nexport async function createTestApp() {\n  // ... setup router, pinia, render app ...\n\n  return {\n    router,       // The navigation system\n    cleanup       // A function to tidy up after the test\n  }\n}\n```\n\n&lt;Collapsible title=\&quot;Full implementation example\&quot;&gt;\n```typescript\n// helpers/createTestApp.ts\nimport type { RouteLocationRaw, Router } from &#39;vue-router&#39;\nimport { render } from &#39;vitest-browser-vue&#39;\nimport { page } from &#39;vitest/browser&#39;\nimport { expect } from &#39;vitest&#39;\nimport { flushPromises } from &#39;@vue/test-utils&#39;\nimport { createPinia } from &#39;pinia&#39;\nimport { createMemoryHistory, createRouter } from &#39;vue-router&#39;\nimport App from &#39;@/App.vue&#39;\nimport { routes } from &#39;@/router&#39;\nimport { useExercisesStore } from &#39;@/stores/exercises&#39;\nimport { i18n } from &#39;@/i18n&#39;\nimport en from &#39;@/i18n/messages/en&#39;\nimport {\n  CommonPO,\n  BuilderPO,\n  ActiveWorkoutPO,\n  QueuePO,\n  BenchmarksPO,\n  BenchmarkFormPO,\n  BenchmarkDetailPO,\n} from &#39;./pages&#39;\n\ntype CreateTestAppOptions = {\n  initialRoute?: string\n}\n\ntype TestApp = {\n  router: Router\n  container: Element\n  // Page Objects\n  common: CommonPO\n  builder: BuilderPO\n  workout: ActiveWorkoutPO\n  queue: QueuePO\n  benchmarks: BenchmarksPO\n  benchmarkForm: BenchmarkFormPO\n  benchmarkDetail: BenchmarkDetailPO\n  // Raw query methods (use page.getBy* for new code)\n  getByRole: typeof page.getByRole\n  getByText: typeof page.getByText\n  getByTestId: typeof page.getByTestId\n  queryByRole: typeof page.getByRole\n  queryByText: typeof page.getByText\n  findByRole: typeof page.getByRole\n  findByText: typeof page.getByText\n  // Helpers\n  navigateTo: (to: RouteLocationRaw) =&gt; Promise&lt;void&gt;\n  cleanup: () =&gt; void\n}\n\nexport async function createTestApp(options: CreateTestAppOptions = {}): Promise&lt;TestApp&gt; {\n  const { initialRoute = &#39;/&#39; } = options\n\n  const pinia = createPinia()\n  const router = createRouter({\n    history: createMemoryHistory(),\n    routes,\n  })\n\n  if (initialRoute !== &#39;/&#39;) {\n    router.push(initialRoute)\n  }\n\n  // Preload English messages for tests\n  i18n.global.setLocaleMessage(&#39;en&#39;, en)\n  i18n.global.locale.value = &#39;en&#39;\n\n  const screen = render(App, {\n    global: {\n      plugins: [router, pinia, i18n],\n    },\n  })\n\n  await router.isReady()\n\n  // Flush Vue&#39;s async operations to ensure onMounted fires\n  await flushPromises()\n\n  // Wait for app initialization to complete (exercises seeding and loading)\n  const exercisesStore = useExercisesStore(pinia)\n  await expect\n    .poll(() =&gt; exercisesStore.customExercises.length, { timeout: 5000 })\n    .toBeGreaterThan(0)\n\n  // Create context for page objects\n  const context = { router }\n\n  // Instantiate page objects\n  const common = new CommonPO(context)\n  const builder = new BuilderPO(context, common)\n  const workout = new ActiveWorkoutPO(context, common)\n  const queue = new QueuePO(context, common)\n  const benchmarks = new BenchmarksPO(context, common)\n  const benchmarkForm = new BenchmarkFormPO(context, common)\n  const benchmarkDetail = new BenchmarkDetailPO(context, common)\n\n  // Simple navigation helper\n  async function navigateTo(to: RouteLocationRaw) {\n    await router.push(to)\n  }\n\n  // vitest-browser-vue cleans up before tests automatically\n  // This is kept for backward compatibility with test structure\n  function cleanup() {\n    screen.unmount()\n  }\n\n  return {\n    router,\n    container: screen.container,\n    // Page Objects\n    common,\n    builder,\n    workout,\n    queue,\n    benchmarks,\n    benchmarkForm,\n    benchmarkDetail,\n    // Raw query methods - use page locators (return Locators, not HTMLElements)\n    getByRole: page.getByRole.bind(page),\n    getByText: page.getByText.bind(page),\n    getByTestId: page.getByTestId.bind(page),\n    queryByRole: page.getByRole.bind(page),\n    queryByText: page.getByText.bind(page),\n    findByRole: page.getByRole.bind(page),\n    findByText: page.getByText.bind(page),\n    // Helpers\n    navigateTo,\n    cleanup,\n  }\n}\n```\n&lt;/Collapsible&gt;\n\n&lt;Alert type=\&quot;note\&quot; title=\&quot;Note\&quot;&gt;\n  This isn&#39;t a library you download. It&#39;s a helper file you write once for your project to handle the setup boilerplate.\n&lt;/Alert&gt;\n\n### A Real Integration Test\n\nNotice how we use `getByRole` to find elements—this ensures our app is accessible:\n\n```typescript\nimport { page, userEvent } from &#39;vitest/browser&#39;\n\nit(&#39;completes a set&#39;, async () =&gt; {\n  await createTestApp()\n\n  // 1. Find the \&quot;Start\&quot; button and click it\n  await userEvent.click(page.getByRole(&#39;button&#39;, { name: /start/i }))\n\n  // 2. Type \&quot;100\&quot; into the weight input\n  const weightInput = page.getByRole(&#39;spinbutton&#39;, { name: /weight/i })\n  await userEvent.type(weightInput, &#39;100&#39;)\n\n  // 3. Click \&quot;Complete\&quot;\n  await userEvent.click(page.getByRole(&#39;button&#39;, { name: /complete/i }))\n\n  // 4. Wait for the success message\n  await expect.element(page.getByText(&#39;Set Completed&#39;)).toBeVisible()\n})\n```\n\n&lt;Alert type=\&quot;tip\&quot; title=\&quot;getByRole = Built-in Accessibility Testing\&quot;&gt;\n  Always prefer `getByRole()` over `getByTestId()` or CSS selectors. When you use `getByRole(&#39;button&#39;, { name: /submit/i })`, you&#39;re asserting that:\n\n  1. The element has the correct ARIA role (it&#39;s actually a button)\n  2. The element has an accessible name (screen readers can announce it)\n  3. The element is visible and interactive\n\n  If your test can&#39;t find an element by role, that&#39;s a signal your UI has an accessibility problem—fix the component, not the test. Reserve `getByTestId` only for elements that truly have no semantic meaning.\n&lt;/Alert&gt;\n\n### Page Objects: Handling DOM Interaction\n\nAs your test suite grows, you&#39;ll notice repetitive DOM queries everywhere. **Page Objects** solve this by encapsulating all DOM interactions for a specific page or component.\n\n&gt; **Key Difference:** Factories handle **data** (creating test objects). Page Objects handle **DOM interaction** (clicking, typing, querying elements). They complement each other.\n\n```typescript\n// pages/WorkoutPage.ts\nimport { page, userEvent } from &#39;vitest/browser&#39;\n\nexport class WorkoutPage {\n  // Queries - finding elements\n  get startButton() {\n    return page.getByRole(&#39;button&#39;, { name: /start/i })\n  }\n\n  get weightInput() {\n    return page.getByRole(&#39;spinbutton&#39;, { name: /weight/i })\n  }\n\n  // Actions - user interactions\n  async start() {\n    await userEvent.click(this.startButton)\n  }\n\n  async setWeight(value: number) {\n    await userEvent.clear(this.weightInput)\n    await userEvent.type(this.weightInput, String(value))\n  }\n\n  async completeSet() {\n    await userEvent.click(page.getByRole(&#39;button&#39;, { name: /complete/i }))\n  }\n}\n```\n\nNow your tests read like plain English:\n\n```typescript\nimport { page } from &#39;vitest/browser&#39;\n\nit(&#39;completes a set with weight&#39;, async () =&gt; {\n  const workoutPage = new WorkoutPage()\n\n  await workoutPage.start()\n  await workoutPage.setWeight(100)\n  await workoutPage.completeSet()\n\n  await expect.element(page.getByText(&#39;Set Completed&#39;)).toBeVisible()\n})\n```\n\n| Helper | Handles | Used In |\n|--------|---------|---------|\n| **Factories** | Test data (objects, entities) | Unit tests, Integration tests |\n| **Page Objects** | DOM interaction (clicks, queries) | Integration tests only |\n\n&lt;Aside type=\&quot;tip\&quot; title=\&quot;When to Use Page Objects\&quot;&gt;\n  Don&#39;t create Page Objects upfront. Write your first few tests with inline queries. When you notice the same `getByRole` patterns repeating across 3+ tests, extract them into a Page Object.\n&lt;/Aside&gt;\n\n&lt;Aside type=\&quot;note\&quot; title=\&quot;Automate the Refactoring\&quot;&gt;\n  I use a [Claude Code command to refactor tests into Page Objects](/prompts/claude/claude-refactor-page-object-command) automatically. Point it at a test file and it extracts repeated queries into a clean page object factory.\n&lt;/Aside&gt;\n\nThis approach aligns with black box testing principles—testing behavior rather than implementation details.\n\n&lt;InternalLink slug=\&quot;stop-white-box-testing-vue\&quot;&gt;Stop White Box Testing Vue Components&lt;/InternalLink&gt;\n\n---\n\n## Layer 3: Accessibility and Visual Tests\n\nThese are the \&quot;cherries on top\&quot; of your pyramid.\n\n### Accessibility (A11y)\n\nWe use a tool called **axe-core**. It scans your rendered HTML for common violations (like low contrast text or missing labels).\n\n```typescript\nit(&#39;has no accessibility violations&#39;, async () =&gt; {\n  const { container } = await createTestApp()\n\n  // This one line checks for dozens of common a11y bugs!\n  await assertNoViolations(container)\n})\n```\n\n&lt;Aside type=\&quot;tip\&quot; title=\&quot;Learn More About Accessibility Testing\&quot;&gt;\n  For a complete setup guide with jest-axe, see &lt;InternalLink slug=\&quot;how-to-improve-accessibility-with-testing-library-and-jest-axe-for-your-vue-application\&quot;&gt;How to Improve Accessibility with Testing Library and jest-axe&lt;/InternalLink&gt;. For general Vue accessibility best practices, check out &lt;InternalLink slug=\&quot;vue-accessibility-blueprint-8-steps\&quot;&gt;Vue Accessibility Blueprint: 8 Steps&lt;/InternalLink&gt;.\n&lt;/Aside&gt;\n\n### Visual Regression\n\nThis takes a screenshot of your component and compares it to a \&quot;golden\&quot; version saved on your computer. If a pixel changes, the test fails.\n\n```typescript\nit(&#39;matches the design&#39;, async () =&gt; {\n  await expect(page.getByTestId(&#39;app&#39;)).toMatchScreenshot(&#39;settings-page.png&#39;)\n})\n```\n\nUse this sparingly. Visual tests are brittle (even a font rendering update can break them), so only use them for critical screens.\n\n&lt;Aside type=\&quot;info\&quot; title=\&quot;Deep Dive into Visual Testing\&quot;&gt;\n  For a complete setup guide on visual regression testing with Vitest browser mode, see &lt;InternalLink slug=\&quot;visual-regression-testing-with-vue-and-vitest-browser\&quot;&gt;How to Do Visual Regression Testing in Vue with Vitest&lt;/InternalLink&gt;.\n&lt;/Aside&gt;\n\n### Testing Your Core UI Library\n\nThere&#39;s one place where visual regression and accessibility tests shine: **your base component library**.\n\nIf you&#39;re building your own UI components (BaseButton, DatePicker, Modal, Input), these components should be:\n\n- **Dumb** — no business logic, just presentation\n- **Reusable** — used across your entire app\n- **Stable** — rarely change once built\n\nThis makes them perfect candidates for visual and accessibility testing:\n\n```typescript\n// BaseButton.visual.spec.ts\ndescribe(&#39;BaseButton&#39;, () =&gt; {\n  it(&#39;renders all variants correctly&#39;, async () =&gt; {\n    render(ButtonStory) // A component showing all button states\n    await expect(page).toMatchScreenshot(&#39;button-variants.png&#39;)\n  })\n\n  it(&#39;has no accessibility violations&#39;, async () =&gt; {\n    const { container } = render(BaseButton, {\n      props: { label: &#39;Click me&#39; }\n    })\n    await assertNoViolations(container)\n  })\n})\n```\n\nFor each base component, test:\n\n| Test Type | What to Check |\n|-----------|---------------|\n| **Visual** | All variants (primary, secondary, disabled, loading) |\n| **A11y** | Focus states, ARIA attributes, color contrast |\n| **Keyboard** | Tab navigation, Enter/Space activation |\n\n&lt;Aside type=\&quot;note\&quot; title=\&quot;Using a Component Library?\&quot;&gt;\n  If you use a pre-built library like **shadcn/ui**, **Vuetify**, or **PrimeVue**, skip this. Those libraries already handle visual consistency and accessibility. Focus your testing efforts on your business logic and user flows instead.\n&lt;/Aside&gt;\n\n---\n\n## Why Not End-to-End (E2E) Tests?\n\nYou might hear people say, \&quot;Just use Cypress or Playwright for everything!\&quot;\n\nE2E tests mean **zero mocking**—you run your real backend and database. They test your entire stack: Frontend + Backend + Database.\n\nFor a new developer or a solo project, this is painful because:\n\n- It&#39;s slow\n- It breaks easily (if the backend API is down, your frontend tests fail)\n\n### The Alternative: Mocking\n\nInstead, we use **MSW (Mock Service Worker)**. It intercepts network requests and returns fake data immediately. This makes your integration tests fast and stable. You don&#39;t need a running backend to test your frontend.\n\n&lt;Alert type=\&quot;tip\&quot; title=\&quot;The Golden Rule of Mocking\&quot;&gt;\n  **The less you mock, the better your tests.** Every mock is a lie you&#39;re telling your test suite. Mock only what you can&#39;t control:\n\n  - **External APIs** (network calls to third-party services)\n  - **System boundaries** (time, random numbers, file system)\n  - **Paid services** (payment gateways, SMS providers)\n\n  Never mock your own code just to make tests easier. If a component is hard to test without mocking internal modules, that&#39;s a sign your architecture needs refactoring—not more mocks.\n&lt;/Alert&gt;\n\n&lt;Alert type=\&quot;note\&quot; title=\&quot;What about Contract Testing?\&quot;&gt;\n  In large corporate teams, you might use \&quot;Contract Testing\&quot; to ensure your mocks match the real API. For now, don&#39;t worry about it. Focus on getting your integration and unit tests running smoothly.\n&lt;/Alert&gt;\n\n---\n\n## Comparison: Testing Approaches\n\n| Layer | Speed | Confidence | Flakiness | Distribution | When to Use |\n|-------|-------|------------|-----------|--------------|-------------|\n| **Unit Tests (Composables)** | ⚡ Very fast | Medium | None | ~20% | Logic validation, utility functions |\n| **Integration Tests (Browser)** | 🚀 Fast | High | Low | **~70%** | User flows, component interaction |\n| **A11y Tests** | 🚀 Fast | High | Medium | ~5% | Critical screens, forms |\n| **Visual Regression** | 🐢 Slow | Medium | High | ~5% | Design system components |\n\n---\n\n## Summary: Your Next Steps\n\nDon&#39;t try to implement the whole pyramid today. Start with what matters most.\n\n### Step 1: Identify What Can Never Fail\n\nAsk yourself: *\&quot;What flows in my app would be catastrophic if they broke?\&quot;* For an e-commerce site, that&#39;s checkout. For a banking app, that&#39;s transfers. For my workout tracker, it&#39;s completing a set.\n\nWrite integration tests for these critical paths first using Vitest browser mode. Even 3-5 tests covering your core flows provide massive confidence.\n\n### Step 2: Set Up the Infrastructure\n\nGet Vitest browser mode running with a simple `createTestApp` helper. Once you can render your app and click a button in a test, you have the foundation for everything else.\n\n### Step 3: Write Tickets with Testable Acceptance Criteria\n\nGood tickets have Gherkin-style acceptance criteria that read like tests:\n\n```gherkin\nGiven I am on the workout page\nWhen I tap \&quot;Complete Set\&quot;\nThen I should see \&quot;Set Completed\&quot; confirmation\nAnd the set should be saved to history\n```\n\nThese ACs translate directly into integration tests. Now you can practice TDD: write the test from the AC first, watch it fail, then implement the feature.\n\n### Step 4: Extract Patterns as You Go\n\nDon&#39;t create factories or page objects upfront. Write a few tests with inline data and queries. When you notice repetition, extract it. This way, your abstractions solve real problems instead of imagined ones.\n\nFor guidance on writing clear, maintainable test names, check out &lt;InternalLink slug=\&quot;frontend-testing-guide-10-essential-rules\&quot;&gt;Frontend Testing Guide: 10 Essential Rules for Naming Tests&lt;/InternalLink&gt;.\n\n&lt;Aside type=\&quot;note\&quot; title=\&quot;See It in Action\&quot;&gt;\n  Want to see this testing setup in a real project? Check out my [Workout Tracker PWA on GitHub](https://github.com/alexanderop/workoutTracker). It includes the `createTestApp` helper, page objects, factories, and integration tests using Vitest browser mode.\n&lt;/Aside&gt;\n\n---\n\n## Bonus: Performance Testing in CI\n\nWhile not part of the traditional testing pyramid, **performance budgets** catch regressions before they reach production. I run Lighthouse CI on every build to enforce thresholds for performance, accessibility, and best practices.\n\n```yaml\n# .github/workflows/ci.yml\nperformance-budget:\n  needs: build\n  runs-on: ubuntu-latest\n  timeout-minutes: 10\n  steps:\n    - name: Checkout code\n      uses: actions/checkout@v4.2.2\n\n    - name: Setup pnpm\n      uses: pnpm/action-setup@v4.1.0\n\n    - name: Setup Node.js\n      uses: actions/setup-node@v4.4.0\n      with:\n        node-version: ${{ env.NODE_VERSION }}\n\n    - name: Restore node_modules\n      uses: actions/cache/restore@v4.2.3\n      with:\n        path: node_modules\n        key: node-modules-${{ runner.os }}-${{ hashFiles(&#39;pnpm-lock.yaml&#39;) }}\n\n    - name: Download build artifacts\n      uses: actions/download-artifact@v6.0.0\n      with:\n        name: dist\n        path: dist\n\n    - name: Run Lighthouse CI\n      run: pnpm lhci autorun\n```\n\n&lt;Aside type=\&quot;tip\&quot; title=\&quot;What Lighthouse CI Catches\&quot;&gt;\n  - Performance regressions (bundle size bloat, slow renders)\n  - Accessibility violations (missing labels, low contrast)\n  - SEO issues (missing meta tags, non-crawlable links)\n  - Best practice violations (HTTP/2, image optimization)\n\n  Configure thresholds in `lighthouserc.js` to fail the build when scores drop below acceptable levels.\n&lt;/Aside&gt;\n\n---\n\n## Beyond the Pyramid: AI-Powered QA\n\nThere&#39;s a new layer emerging that doesn&#39;t fit neatly into the traditional pyramid: **AI-driven testing**.\n\n&lt;Figure src={aiDrivenTesting} alt=\&quot;AI-driven testing workflow showing Claude Code with Playwright testing an app and generating reports\&quot; caption=\&quot;AI QA: Claude Code + Playwright for intelligent exploratory testing\&quot; size=\&quot;large\&quot; /&gt;\n\nWhat if you could have an AI test your app the way a real QA engineer would? Not following scripts, but actually exploring your UI, trying edge cases, and writing bug reports?\n\nI&#39;ve been experimenting with exactly this approach. Using Claude Code combined with Playwright&#39;s browser automation, I built an AI QA engineer that:\n\n- Tests my app through the browser like a real user\n- Tries unexpected inputs and edge cases automatically\n- Runs on every pull request via GitHub Actions\n- Posts detailed bug reports with screenshots directly to my PRs\n\n```mermaid\ngraph LR\n    PR[Open PR] --&gt; GH[GitHub Actions]\n    GH --&gt; AI[Claude Code + Playwright]\n    AI --&gt; Test[Browser Testing]\n    Test --&gt; Report[QA Report on PR]\n```\n\nThis isn&#39;t a replacement for the testing pyramid—it&#39;s a complement. Your unit and integration tests catch regressions deterministically. AI QA excels at exploratory testing and finding bugs that scripted tests would never think to check.\n\n&lt;Aside type=\&quot;tip\&quot; title=\&quot;Want to Build Your Own AI QA Engineer?\&quot;&gt;\n  I wrote a complete guide on setting this up: &lt;InternalLink slug=\&quot;building_ai_qa_engineer_claude_code_playwright\&quot;&gt;Building an AI QA Engineer with Claude Code and Playwright MCP&lt;/InternalLink&gt;. It covers the GitHub Actions workflow, prompt engineering for effective testing, and how to get bug reports posted automatically to your PRs.\n&lt;/Aside&gt;\n\n---\n\n## Additional Resources\n\n- [Vitest Browser Mode Guide](https://vitest.dev/guide/browser/) - The official docs are excellent\n- [vitest-browser-vue](https://github.com/vitest-dev/vitest-browser-vue) - Vue rendering for Vitest browser mode\n- [vitest-examples on GitHub](https://github.com/vitest-dev/vitest/tree/main/examples) - \&quot;Hello World\&quot; setup examples&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PostCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus-outline inline-flex items-center gap-1.5 rounded-md border border-skin-line bg-skin-card px-2.5 py-1.5 text-xs font-medium text-skin-base opacity-80 transition-all hover:border-skin-accent/50 hover:text-skin-accent hover:opacity-100" aria-label="Copy post as markdown" title="Copy post as markdown for AI/LLM"><svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg><span>Copy Post</span></button><!--astro:end--></astro-island> </div>  <article id="article" class="prose mx-auto mt-8 max-w-5xl astro-vj4tpspi"> <figure class="max-w-4xl mx-auto "> <img src="/_astro/vueTestingPyramidCover.CPflLBsB_l1lGc.webp" alt="Vue 3 Testing Pyramid with Vitest Browser Mode" loading="lazy" decoding="async" fetchpriority="auto" width="1024" height="559" class="w-full">  </figure>
<h2 id="quick-summary">Quick Summary<a class="heading-link" aria-label="Link to section" href="#quick-summary"><span class="heading-link-icon">#</span></a></h2>
<p>This post covers a practical testing approach for Vue 3 applications:</p>
<ul>
<li>Composable unit tests for fast logic verification</li>
<li>Integration tests with Vitest browser mode for realistic user flows</li>
<li>Accessibility and visual tests for critical screen checks</li>
<li>Simplified data factories to manage test data easily</li>
</ul>
<h2 id="table-of-contents">Table of Contents<a class="heading-link" aria-label="Link to section" href="#table-of-contents"><span class="heading-link-icon">#</span></a></h2>
<p></p><details><summary>Open Table of Contents</summary><p></p>
<ul>
<li><a href="#introduction">Introduction</a></li>
<li><a href="#before-we-start-a-mini-glossary">Before We Start: A Mini Glossary</a></li>
<li><a href="#your-architecture-shapes-your-testing-strategy">Your Architecture Shapes Your Testing Strategy</a>
<ul>
<li><a href="#bad-vs-good-architecture">Bad vs. Good Architecture</a>
<ul>
<li><a href="#the-monolith-hard-to-test">The Monolith (Hard to Test)</a></li>
<li><a href="#the-composable-easy-to-test">The Composable (Easy to Test)</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="#the-testing-pyramid">The Testing Pyramid</a></li>
<li><a href="#the-environment-browser-mode-vs-jsdom">The Environment: Browser Mode vs JSDOM</a>
<ul>
<li><a href="#real-world-performance-comparison">Real-World Performance Comparison</a></li>
<li><a href="#setting-up-vitest-browser-mode">Setting Up Vitest Browser Mode</a></li>
<li><a href="#no-more-testing-library">No More Testing Library</a></li>
</ul>
</li>
<li><a href="#layer-1-composable-unit-tests">Layer 1: Composable Unit Tests</a>
<ul>
<li><a href="#a-simple-composable-test">A Simple Composable Test</a></li>
</ul>
</li>
<li><a href="#managing-test-data-with-factories">Managing Test Data with Factories</a>
<ul>
<li><a href="#the-problem-hard-coded-data">The Problem: Hard-coded Data</a></li>
<li><a href="#the-solution-a-simple-factory-function">The Solution: A Simple Factory Function</a></li>
<li><a href="#using-it-in-tests">Using It in Tests</a></li>
<li><a href="#factories-work-at-every-layer">Factories Work at Every Layer</a></li>
</ul>
</li>
<li><a href="#layer-2-integration-tests">Layer 2: Integration Tests</a>
<ul>
<li><a href="#component-tests-vs-integration-tests">Component Tests vs. Integration Tests</a></li>
<li><a href="#the-test-app-helper">The “Test App” Helper</a></li>
<li><a href="#a-real-integration-test">A Real Integration Test</a></li>
<li><a href="#page-objects-handling-dom-interaction">Page Objects: Handling DOM Interaction</a></li>
</ul>
</li>
<li><a href="#layer-3-accessibility-and-visual-tests">Layer 3: Accessibility and Visual Tests</a>
<ul>
<li><a href="#accessibility-a11y">Accessibility (A11y)</a></li>
<li><a href="#visual-regression">Visual Regression</a></li>
<li><a href="#testing-your-core-ui-library">Testing Your Core UI Library</a></li>
</ul>
</li>
<li><a href="#why-not-end-to-end-e2e-tests">Why Not End-to-End (E2E) Tests?</a>
<ul>
<li><a href="#the-alternative-mocking">The Alternative: Mocking</a></li>
</ul>
</li>
<li><a href="#comparison-testing-approaches">Comparison: Testing Approaches</a></li>
<li><a href="#summary-your-next-steps">Summary: Your Next Steps</a>
<ul>
<li><a href="#step-1-identify-what-can-never-fail">Step 1: Identify What Can Never Fail</a></li>
<li><a href="#step-2-set-up-the-infrastructure">Step 2: Set Up the Infrastructure</a></li>
<li><a href="#step-3-write-tickets-with-testable-acceptance-criteria">Step 3: Write Tickets with Testable Acceptance Criteria</a></li>
<li><a href="#step-4-extract-patterns-as-you-go">Step 4: Extract Patterns as You Go</a></li>
</ul>
</li>
<li><a href="#bonus-performance-testing-in-ci">Bonus: Performance Testing in CI</a></li>
<li><a href="#beyond-the-pyramid-ai-powered-qa">Beyond the Pyramid: AI-Powered QA</a></li>
<li><a href="#additional-resources">Additional Resources</a></li>
</ul>
<p></p></details><p></p>
<h2 id="introduction">Introduction<a class="heading-link" aria-label="Link to section" href="#introduction"><span class="heading-link-icon">#</span></a></h2>
<p>I’m building a workout tracking PWA with Vue 3, and I needed confidence that my changes work. Not the “I clicked around and it seems fine” kind of confidence, but the “I can refactor this and know immediately if I broke something” kind.</p>
<p>Here’s the thing: I don’t write much code myself anymore. AI tools handle most of the implementation. I describe what I want, review the changes, and guide the direction—but the actual keystrokes? That’s the AI. This workflow is incredibly productive, but it comes with a catch: I need a robust safety net.</p>
<p>When an AI writes code, tests become even more critical. They serve three purposes:</p>
<ol>
<li><strong>Catch bugs</strong> before users do</li>
<li><strong>Enable refactoring</strong> — change code freely knowing tests will catch regressions</li>
<li><strong>Document behavior</strong> — tests act as a “user manual” for your code</li>
</ol>
<div class="alert alert-tip astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">💪</span> Don&#39;t Forget the Basics </p> <div class="alert-content astro-7kdbuayl"> <p>Tests are just one part of your safety net. <strong>Linting</strong> (ESLint) catches code style issues and potential bugs statically. <strong>Type checking</strong> (TypeScript) catches type errors at compile time. Run all three—lint, type check, and tests—before every commit.</p> </div> </div> 
<h2 id="before-we-start-a-mini-glossary">Before We Start: A Mini Glossary<a class="heading-link" aria-label="Link to section" href="#before-we-start-a-mini-glossary"><span class="heading-link-icon">#</span></a></h2>
<p>Testing has a lot of jargon. Here’s a cheat sheet to keep handy as you read:</p>

































<table><thead><tr><th>Term</th><th>Meaning</th></tr></thead><tbody><tr><td data-label="Term"><strong>Unit Test</strong></td><td data-label="Meaning">Testing a tiny, isolated piece of code (like a single function) to ensure it returns the right value</td></tr><tr><td data-label="Term"><strong>Integration Test</strong></td><td data-label="Meaning">Testing how multiple pieces work together (e.g., clicking a button and seeing a database update)</td></tr><tr><td data-label="Term"><strong>Regression</strong></td><td data-label="Meaning">A bug where a feature that used to work stops working after you change something else</td></tr><tr><td data-label="Term"><strong>Mock</strong></td><td data-label="Meaning">A fake version of a complex tool (like faking an API call) so you can test without relying on the internet</td></tr><tr><td data-label="Term"><strong>Assertion</strong></td><td data-label="Meaning">A line of code that checks if a result matches your expectation (e.g., <code>expect(2 + 2).toBe(4)</code>)</td></tr><tr><td data-label="Term"><strong>A11y</strong></td><td data-label="Meaning">Short for “Accessibility” (there are 11 letters between A and y)</td></tr></tbody></table>
<hr/>
<h2 id="your-architecture-shapes-your-testing-strategy">Your Architecture Shapes Your Testing Strategy<a class="heading-link" aria-label="Link to section" href="#your-architecture-shapes-your-testing-strategy"><span class="heading-link-icon">#</span></a></h2>
<p>Your testing strategy reflects your frontend architecture. They’re not independent choices.</p>
<p>If you write <strong>monolithic components</strong> (huge files with logic and UI mixed), testing is a nightmare. If you use <strong>composables</strong> (extracting logic into separate files), testing becomes straightforward.</p>
<figure class="max-w-4xl mx-auto "> <img src="/_astro/monolithVsComponent.BUn3OTbj_152xD7.webp" alt="Comparison of monolithic component with mixed logic vs composable pattern with extracted logic" loading="lazy" decoding="async" fetchpriority="auto" width="1024" height="565" class="w-full"> <figcaption class="mt-2 text-center text-sm text-gray-500"> Monolithic components trap logic inside; composables make it testable </figcaption> </figure>
<h3 id="bad-vs-good-architecture">Bad vs. Good Architecture<a class="heading-link" aria-label="Link to section" href="#bad-vs-good-architecture"><span class="heading-link-icon">#</span></a></h3>
<h4 id="the-monolith-hard-to-test">The Monolith (Hard to Test)<a class="heading-link" aria-label="Link to section" href="#the-monolith-hard-to-test"><span class="heading-link-icon">#</span></a></h4>
<p>To test the timer logic here, you have to mount the whole component, find the button, click it, and wait for the UI to update. It’s slow and fragile.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">script</span><span style="color:#BB9AF7"> setup</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">ref</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Logic is trapped inside the component!</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> time</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">0</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#7AA2F7"> start</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#7AA2F7"> setInterval</span><span style="color:#9ABDF5">(()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#C0CAF5"> time</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">++,</span><span style="color:#FF9E64"> 1000</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">script</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">button</span><span style="color:#BB9AF7"> @click</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">start</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">{{ time }}</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">button</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<script setup>
import { ref } from 'vue'
// Logic is trapped inside the component!
const time = ref(0)
const start = () => setInterval(() => time.value++, 1000)
</script>

<template>
  <button @click=&#34;start&#34;>{{ time }}</button>
</template>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h4 id="the-composable-easy-to-test">The Composable (Easy to Test)<a class="heading-link" aria-label="Link to section" href="#the-composable-easy-to-test"><span class="heading-link-icon">#</span></a></h4>
<p>Here, the logic lives in a plain TypeScript file. We can test <code>useTimer</code> without ever looking at a Vue component or HTML.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// useTimer.ts</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useTimer</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> time</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">0</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#7AA2F7"> start</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#7AA2F7"> setInterval</span><span style="color:#9ABDF5">(() </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#C0CAF5"> time</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">++,</span><span style="color:#FF9E64"> 1000</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> { </span><span style="color:#C0CAF5">time</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> start</span><span style="color:#9ABDF5"> }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// useTimer.ts
export function useTimer() {
  const time = ref(0)
  const start = () => setInterval(() => time.value++, 1000)
  return { time, start }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>My strategy relies on this “composable-first” approach. However, for the UI itself, we use integration tests. These tests don’t care about your code structure; they test behavior through the UI, just like a user would.</p>
<aside aria-label="Learn More About Composable Testing" class="aside aside-tip astro-37uy2q7c"> <div class="aside-content astro-37uy2q7c"> <p class="aside-title astro-37uy2q7c"> <span class="aside-emoji astro-37uy2q7c" role="img" aria-hidden="true">💡</span> Learn More About Composable Testing </p> <section class="aside-body astro-37uy2q7c"> <p>For a deep dive into testing composables specifically, check out <span class="internal-link-wrapper astro-3tyn5ojg"> <a target="_blank" rel="noopener noreferrer" href="/posts/how-to-test-vue-composables/" class="internal-link astro-3tyn5ojg"> How to Test Vue Composables </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">How to Test Vue Composables: A Comprehensive Guide with Vitest</span> <span class="preview-description astro-3tyn5ojg">Learn how to effectively test Vue composables using Vitest. Covers independent and dependent composables, with practical examples and best practices.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">vue</span><span class="preview-tag astro-3tyn5ojg">testing</span>  </span> <time class="preview-date astro-3tyn5ojg">Nov 25, 2023</time> </span> </span> </span>  <script>
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
</script>.</p> </section> </div> </aside> 
<hr/>
<h2 id="the-testing-pyramid">The Testing Pyramid<a class="heading-link" aria-label="Link to section" href="#the-testing-pyramid"><span class="heading-link-icon">#</span></a></h2>
<p>My approach inverts the traditional pyramid. <strong>Integration tests make up ~70%</strong> of my test suite because Vitest browser mode makes them fast and reliable. Composable unit tests cover ~20% for pure logic, and the remaining ~10% goes to accessibility and visual regression tests.</p>

<figure class="max-w-4xl mx-auto "> <img src="/_astro/testingPyramid.CH1o4rxK_1XTN3R.webp" alt="Testing strategy showing integration tests as the foundation (~70%), unit tests for composables (~20%), and visual/a11y tests at the top (~10%)" loading="lazy" decoding="async" fetchpriority="auto" width="1956" height="1078" class="w-full"> <figcaption class="mt-2 text-center text-sm text-gray-500"> Integration tests form the foundation of this strategy </figcaption> </figure>
<hr/>
<h2 id="the-environment-browser-mode-vs-jsdom">The Environment: Browser Mode vs JSDOM<a class="heading-link" aria-label="Link to section" href="#the-environment-browser-mode-vs-jsdom"><span class="heading-link-icon">#</span></a></h2>
<p>In the past, most Vue tests ran in JSDOM. Now, I recommend <strong>Vitest Browser Mode</strong> with <code>vitest-browser-vue</code>. Here’s why:</p>



































<table><thead><tr><th>Feature</th><th>JSDOM (Old Standard)</th><th>Vitest Browser Mode (New Standard)</th></tr></thead><tbody><tr><td data-label="Feature"><strong>What is it?</strong></td><td data-label="JSDOM (Old Standard)">A simulation of a browser running in Node.js (Fake)</td><td data-label="Vitest Browser Mode (New Standard)">A real instance of Chrome/Firefox running your tests (Real)</td></tr><tr><td data-label="Feature"><strong>Accuracy</strong></td><td data-label="JSDOM (Old Standard)">Good for logic, bad for layout/CSS</td><td data-label="Vitest Browser Mode (New Standard)">100% accurate — it’s a real browser</td></tr><tr><td data-label="Feature"><strong>Debugging</strong></td><td data-label="JSDOM (Old Standard)">Hard. You stare at console logs</td><td data-label="Vitest Browser Mode (New Standard)">Easy. You can watch the test click buttons on your screen</td></tr><tr><td data-label="Feature"><strong>Speed</strong></td><td data-label="JSDOM (Old Standard)">Surprisingly slow (see benchmarks below)</td><td data-label="Vitest Browser Mode (New Standard)">Often faster due to native browser APIs</td></tr><tr><td data-label="Feature"><strong>API</strong></td><td data-label="JSDOM (Old Standard)">Requires Testing Library for DOM queries</td><td data-label="Vitest Browser Mode (New Standard)">Built-in <code>page</code> object with Playwright-like locators</td></tr></tbody></table>
<h3 id="real-world-performance-comparison">Real-World Performance Comparison<a class="heading-link" aria-label="Link to section" href="#real-world-performance-comparison"><span class="heading-link-icon">#</span></a></h3>
<p>A common misconception is that browser mode is slower. In my testing with the same test suite, <strong>browser mode was actually 4x faster</strong>:</p>








































<table><thead><tr><th>Metric</th><th>Vitest Browser Mode (Chromium)</th><th>Vitest Unit Mode (JSDOM)</th></tr></thead><tbody><tr><td data-label="Metric"><strong>Total Duration</strong></td><td data-label="Vitest Browser Mode (Chromium)">13.59s 🚀</td><td data-label="Vitest Unit Mode (JSDOM)">53.72s</td></tr><tr><td data-label="Metric"><strong>Test Files</strong></td><td data-label="Vitest Browser Mode (Chromium)">15</td><td data-label="Vitest Unit Mode (JSDOM)">15</td></tr><tr><td data-label="Metric"><strong>Total Tests</strong></td><td data-label="Vitest Browser Mode (Chromium)">82 (78 passed)</td><td data-label="Vitest Unit Mode (JSDOM)">82 (78 passed)</td></tr><tr><td data-label="Metric"><strong>Setup Time</strong></td><td data-label="Vitest Browser Mode (Chromium)">4.48s</td><td data-label="Vitest Unit Mode (JSDOM)">53ms</td></tr><tr><td data-label="Metric"><strong>Import Time</strong></td><td data-label="Vitest Browser Mode (Chromium)">19.84s</td><td data-label="Vitest Unit Mode (JSDOM)">7.98s</td></tr><tr><td data-label="Metric"><strong>Test Execution Time</strong></td><td data-label="Vitest Browser Mode (Chromium)">29.48s</td><td data-label="Vitest Unit Mode (JSDOM)">40.53s</td></tr></tbody></table>
<p>While browser mode has higher setup time (launching Chromium), the actual test execution is faster because it uses native browser APIs instead of JSDOM’s JavaScript reimplementation. The total duration speaks for itself.</p>
<aside aria-label="Why Vitest Browser Mode for AI Workflows?" class="aside aside-tip astro-37uy2q7c"> <div class="aside-content astro-37uy2q7c"> <p class="aside-title astro-37uy2q7c"> <span class="aside-emoji astro-37uy2q7c" role="img" aria-hidden="true">💡</span> Why Vitest Browser Mode for AI Workflows? </p> <section class="aside-body astro-37uy2q7c"> <p>Vitest browser mode handles everything in one command. The browser launches, components render, and tests run. It’s much simpler for AI assistants (and humans) to manage than setting up complex End-to-End servers.</p> </section> </div> </aside> 
<h3 id="setting-up-vitest-browser-mode">Setting Up Vitest Browser Mode<a class="heading-link" aria-label="Link to section" href="#setting-up-vitest-browser-mode"><span class="heading-link-icon">#</span></a></h3>
<p>Vitest 4.0+ requires a browser provider package. Install the dependencies:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#C0CAF5">npm</span><span style="color:#9ECE6A"> install</span><span style="color:#E0AF68"> -D</span><span style="color:#9ECE6A"> vitest</span><span style="color:#9ECE6A"> @vitest/browser-playwright</span><span style="color:#9ECE6A"> vitest-browser-vue</span><span style="color:#9ECE6A"> playwright</span></span></code><button type="button" class="copy" data-code="npm install -D vitest @vitest/browser-playwright vitest-browser-vue playwright" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<div class="alert alert-note astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">💡</span> Provider Options </p> <div class="alert-content astro-7kdbuayl"> <p>You can use <code>@vitest/browser-playwright</code> (recommended) or <code>@vitest/browser-webdriverio</code>. Playwright offers the best developer experience with automatic browser downloads.</p> </div> </div> 
<h3 id="no-more-testing-library">No More Testing Library<a class="heading-link" aria-label="Link to section" href="#no-more-testing-library"><span class="heading-link-icon">#</span></a></h3>
<p>With Vitest browser mode, you don’t need <code>@testing-library/vue</code> anymore. The <code>page</code> object from <code>vitest/browser</code> provides Playwright-like locators that are more powerful and consistent:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">page</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> userEvent</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">vitest/browser</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Instead of screen.getByRole(), use page.getByRole()</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> button</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> page</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">getByRole</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">button</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span><span style="color:#73DACA"> name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> /</span><span style="color:#B4F9F8">submit</span><span style="color:#89DDFF">/i</span><span style="color:#9ABDF5"> })</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">await</span><span style="color:#C0CAF5"> userEvent</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">click</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">button</span><span style="color:#9ABDF5">)</span></span></code><button type="button" class="copy" data-code="import { page, userEvent } from 'vitest/browser'

// Instead of screen.getByRole(), use page.getByRole()
const button = page.getByRole('button', { name: /submit/i })
await userEvent.click(button)" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr/>
<h2 id="layer-1-composable-unit-tests">Layer 1: Composable Unit Tests<a class="heading-link" aria-label="Link to section" href="#layer-1-composable-unit-tests"><span class="heading-link-icon">#</span></a></h2>
<p>Composables are just functions. You test them by calling them and checking the result.</p>
<h3 id="a-simple-composable-test">A Simple Composable Test<a class="heading-link" aria-label="Link to section" href="#a-simple-composable-test"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">describe</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> expect</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> it</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">vitest</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">useDialogState</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">@/composables/useDialogState</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">describe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">useDialogState</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">starts closed</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">    // 1. Run the code</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> isOpen</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> useDialogState</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">    // 2. Assert the result</span></span>
<span class="line"><span style="color:#7AA2F7">    expect</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">isOpen</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toBe</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">false</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">opens when requested</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> isOpen</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> open</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> useDialogState</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#7AA2F7">    open</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#7AA2F7">    expect</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">isOpen</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toBe</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">true</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span></span>
<span class="line"><span style="color:#9ABDF5">})</span></span></code><button type="button" class="copy" data-code="import { describe, expect, it } from 'vitest'
import { useDialogState } from '@/composables/useDialogState'

describe('useDialogState', () => {
  it('starts closed', () => {
    // 1. Run the code
    const { isOpen } = useDialogState()
    // 2. Assert the result
    expect(isOpen.value).toBe(false)
  })

  it('opens when requested', () => {
    const { isOpen, open } = useDialogState()
    open()
    expect(isOpen.value).toBe(true)
  })
})" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>No HTML, no mounting, no complexity. Just functions and values.</p>
<aside aria-label="Deep Dive: Composable Testing" class="aside aside-tip astro-37uy2q7c"> <div class="aside-content astro-37uy2q7c"> <p class="aside-title astro-37uy2q7c"> <span class="aside-emoji astro-37uy2q7c" role="img" aria-hidden="true">💡</span> Deep Dive: Composable Testing </p> <section class="aside-body astro-37uy2q7c"> <p>For comprehensive patterns including async composables, lifecycle hooks, and dependency injection, see <span class="internal-link-wrapper astro-3tyn5ojg"> <a target="_blank" rel="noopener noreferrer" href="/posts/how-to-test-vue-composables/" class="internal-link astro-3tyn5ojg"> How to Test Vue Composables </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">How to Test Vue Composables: A Comprehensive Guide with Vitest</span> <span class="preview-description astro-3tyn5ojg">Learn how to effectively test Vue composables using Vitest. Covers independent and dependent composables, with practical examples and best practices.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">vue</span><span class="preview-tag astro-3tyn5ojg">testing</span>  </span> <time class="preview-date astro-3tyn5ojg">Nov 25, 2023</time> </span> </span> </span>  <script>
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
</script>.</p> </section> </div> </aside> 
<hr/>
<h2 id="managing-test-data-with-factories">Managing Test Data with Factories<a class="heading-link" aria-label="Link to section" href="#managing-test-data-with-factories"><span class="heading-link-icon">#</span></a></h2>
<p>When writing tests, you constantly need data. For example, to test a “Profile Page,” you need a “User.”</p>
<p>Beginners often copy-paste the same big object into every single test file. This is messy and hard to maintain. If you add a new required field (like <code>phoneNumber</code>) to your User, you have to go back and fix every single test.</p>
<p>The solution is the <strong>Factory Pattern</strong>. Think of it like ordering a pizza: there’s a “standard” pizza (Cheese &amp; Tomato), and you only specify the changes you want (“…but add pepperoni”).</p>
<figure class="max-w-4xl mx-auto "> <img src="/_astro/factoryPattern.Dnh7cN_e_tmi6J.webp" alt="Factory pattern showing default data merged with overrides to create test objects" loading="lazy" decoding="async" fetchpriority="auto" width="1024" height="559" class="w-full"> <figcaption class="mt-2 text-center text-sm text-gray-500"> Factories: define defaults once, override only what you need </figcaption> </figure>
<h3 id="the-problem-hard-coded-data">The Problem: Hard-coded Data<a class="heading-link" aria-label="Link to section" href="#the-problem-hard-coded-data"><span class="heading-link-icon">#</span></a></h3>
<p>Without factories, your tests look like this. Notice how much noise there is just to test one specific thing:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// ❌ BAD: Repeating data everywhere</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">shows admin badge</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> user</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">    id</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">1</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">John Doe</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    email</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">john@example.com</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    role</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">admin</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#51597D;font-style:italic"> // This is the only line we actually care about!</span></span>
<span class="line"><span style="color:#73DACA">    isActive</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    createdAt</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">2023-01-01</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // ... test logic ...</span></span>
<span class="line"><span style="color:#9ABDF5">})</span></span></code><button type="button" class="copy" data-code="// ❌ BAD: Repeating data everywhere
it('shows admin badge', () => {
  const user = {
    id: '1',
    name: 'John Doe',
    email: 'john@example.com',
    role: 'admin', // This is the only line we actually care about!
    isActive: true,
    createdAt: '2023-01-01'
  }

  // ... test logic ...
})" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="the-solution-a-simple-factory-function">The Solution: A Simple Factory Function<a class="heading-link" aria-label="Link to section" href="#the-solution-a-simple-factory-function"><span class="heading-link-icon">#</span></a></h3>
<p>A factory is just a plain TypeScript function. It holds the “Standard Pizza” defaults and lets you overwrite specific slices using the spread operator (<code>...</code>).</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// factories/userFactory.ts</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// 1. Define the shape of your data</span></span>
<span class="line"><span style="color:#BB9AF7">interface</span><span style="color:#C0CAF5"> User</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  id</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  name</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  role</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">user</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">admin</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  isActive</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> boolean</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// 2. Define your &quot;Standard Pizza&quot; (Sensible Defaults)</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> defaultUser</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> User</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  id</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">123</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Test User</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  role</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">user</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  isActive</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// 3. The Factory Function</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">// It takes &quot;overrides&quot; (partial data) and merges them on top of the defaults</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> createUser</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">overrides</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Partial</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">User</span><span style="color:#89DDFF">&gt;</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> User</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#F7768E;font-weight:bold">    ...</span><span style="color:#C0CAF5">defaultUser</span><span style="color:#89DDFF">,</span><span style="color:#51597D;font-style:italic"> // Start with defaults</span></span>
<span class="line"><span style="color:#F7768E;font-weight:bold">    ...</span><span style="color:#C0CAF5">overrides</span><span style="color:#51597D;font-style:italic">    // Apply your specific changes</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// factories/userFactory.ts

// 1. Define the shape of your data
interface User {
  id: string;
  name: string;
  role: 'user' | 'admin';
  isActive: boolean;
}

// 2. Define your &#34;Standard Pizza&#34; (Sensible Defaults)
const defaultUser: User = {
  id: '123',
  name: 'Test User',
  role: 'user',
  isActive: true
}

// 3. The Factory Function
// It takes &#34;overrides&#34; (partial data) and merges them on top of the defaults
export function createUser(overrides: Partial<User> = {}): User {
  return {
    ...defaultUser, // Start with defaults
    ...overrides    // Apply your specific changes
  };
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="using-it-in-tests">Using It in Tests<a class="heading-link" aria-label="Link to section" href="#using-it-in-tests"><span class="heading-link-icon">#</span></a></h3>
<p>Now your tests focus purely on what matters for that specific scenario:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// ✅ GOOD: Clean and focused</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Scenario 1: I just need ANY user, I don&#39;t care about details</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> basicUser</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> createUser</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Result: { id: &#39;123&#39;, name: &#39;Test User&#39;, role: &#39;user&#39;, ... }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Scenario 2: I specifically need an ADMIN</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> admin</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> createUser</span><span style="color:#9ABDF5">({</span><span style="color:#73DACA"> role</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">admin</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5"> })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Result: { id: &#39;123&#39;, name: &#39;Test User&#39;, role: &#39;admin&#39;, ... }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Scenario 3: I need an INACTIVE user</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> bannedUser</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> createUser</span><span style="color:#9ABDF5">({</span><span style="color:#73DACA"> isActive</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> false</span><span style="color:#9ABDF5"> })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Result: { id: &#39;123&#39;, name: &#39;Test User&#39;, isActive: false, ... }</span></span></code><button type="button" class="copy" data-code="// ✅ GOOD: Clean and focused

// Scenario 1: I just need ANY user, I don't care about details
const basicUser = createUser();
// Result: { id: '123', name: 'Test User', role: 'user', ... }

// Scenario 2: I specifically need an ADMIN
const admin = createUser({ role: 'admin' });
// Result: { id: '123', name: 'Test User', role: 'admin', ... }

// Scenario 3: I need an INACTIVE user
const bannedUser = createUser({ isActive: false });
// Result: { id: '123', name: 'Test User', isActive: false, ... }" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>This pattern keeps your tests readable and makes refactoring easy. If you add a new field to <code>User</code> later, you only update the <code>defaultUser</code> object in one place.</p>
<h3 id="factories-work-at-every-layer">Factories Work at Every Layer<a class="heading-link" aria-label="Link to section" href="#factories-work-at-every-layer"><span class="heading-link-icon">#</span></a></h3>
<p>The beauty of factories is that they work for <strong>both</strong> unit tests and integration tests:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// ✅ Unit Test: Testing a composable</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">formats user display name</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> user</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> createUser</span><span style="color:#9ABDF5">({ </span><span style="color:#73DACA">name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Jane Doe</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> role</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">admin</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5"> })</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> displayName</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> useUserProfile</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">user</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#7AA2F7">  expect</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">displayName</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toBe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">Jane Doe (Admin)</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">})</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// ✅ Integration Test: Testing a rendered component</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">shows admin badge in profile</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9D7CD8;font-style:italic"> async</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> admin</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> createUser</span><span style="color:#9ABDF5">({ </span><span style="color:#73DACA">role</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">admin</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5"> })</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  await</span><span style="color:#7AA2F7"> renderProfilePage</span><span style="color:#9ABDF5">({ </span><span style="color:#73DACA">user</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> admin</span><span style="color:#9ABDF5"> })</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  await</span><span style="color:#C0CAF5"> expect</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">element</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">page</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">getByText</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">Admin</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toBeVisible</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#9ABDF5">})</span></span></code><button type="button" class="copy" data-code="// ✅ Unit Test: Testing a composable
it('formats user display name', () => {
  const user = createUser({ name: 'Jane Doe', role: 'admin' })
  const { displayName } = useUserProfile(user)
  expect(displayName.value).toBe('Jane Doe (Admin)')
})

// ✅ Integration Test: Testing a rendered component
it('shows admin badge in profile', async () => {
  const admin = createUser({ role: 'admin' })
  await renderProfilePage({ user: admin })
  await expect.element(page.getByText('Admin')).toBeVisible()
})" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<blockquote>
<p><strong>Key Insight:</strong> Factories handle <strong>data</strong>. They don’t care whether you’re testing a function or a full page—they just give you clean, predictable objects.</p>
</blockquote>
<aside aria-label="In My Workout Tracker" class="aside aside-note astro-37uy2q7c"> <div class="aside-content astro-37uy2q7c"> <p class="aside-title astro-37uy2q7c"> <span class="aside-emoji astro-37uy2q7c" role="img" aria-hidden="true">📝</span> In My Workout Tracker </p> <section class="aside-body astro-37uy2q7c"> <p>For my workout tracking PWA, I use factories like <code>createWorkout()</code>, <code>createExercise()</code>, and <code>createSet()</code>. The pattern scales nicely—start simple and add complexity only when your data relationships demand it.</p> </section> </div> </aside> 
<hr/>
<h2 id="layer-2-integration-tests">Layer 2: Integration Tests<a class="heading-link" aria-label="Link to section" href="#layer-2-integration-tests"><span class="heading-link-icon">#</span></a></h2>
<p>Integration tests verify complete user flows. They render the app, click buttons, and check if the right things appear on screen.</p>
<div class="alert alert-note astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">💡</span> Integration Test vs E2E Test: What&#39;s the Difference? </p> <div class="alert-content astro-7kdbuayl"> <p>In this post, <strong>integration test</strong> means:</p><ul>
<li>Real browser (Vitest browser mode)</li>
<li>Real Vue components, router, Pinia, and user interactions</li>
<li><strong>Mocked</strong>: external APIs (via <a href="https://mswjs.io/" rel="noopener noreferrer" target="_blank">MSW</a>), browser storage (IndexedDB), third-party services</li>
</ul><p><strong>E2E test</strong> means:</p><ul>
<li>Real browser</li>
<li><strong>Zero mocking</strong>—full stack (frontend + backend + database)</li>
<li>Tests exactly how a user interacts with the production system</li>
</ul><p><strong>Examples</strong>: In my workout tracker, I mock IndexedDB but test real Vue components and user flows—that’s an integration test. For an e-commerce site, you’d mock the product API and payment gateway via MSW, but test the real checkout flow. If you spin up your actual backend and database, that’s E2E.</p> </div> </div> 
<h3 id="component-tests-vs-integration-tests">Component Tests vs. Integration Tests<a class="heading-link" aria-label="Link to section" href="#component-tests-vs-integration-tests"><span class="heading-link-icon">#</span></a></h3>
<p>Vitest browser mode supports two approaches:</p>
<figure class="max-w-4xl mx-auto "> <img src="/_astro/integrationVsComponent.CJRsawdj_ZcDJB7.webp" alt="Component test renders single component vs Integration test renders full App.vue with router and store" loading="lazy" decoding="async" fetchpriority="auto" width="1024" height="559" class="w-full"> <figcaption class="mt-2 text-center text-sm text-gray-500"> Component tests isolate one piece; integration tests render the full app </figcaption> </figure>




















<table><thead><tr><th>Approach</th><th>What you render</th><th>Use case</th></tr></thead><tbody><tr><td data-label="Approach"><strong>Component test</strong></td><td data-label="What you render">Single component (<code>render(MyButton)</code>)</td><td data-label="Use case">Testing component behavior in isolation</td></tr><tr><td data-label="Approach"><strong>Integration test</strong></td><td data-label="What you render">Full app (<code>render(App)</code> with router, store)</td><td data-label="Use case">Testing complete user flows across multiple components</td></tr></tbody></table>
<p><strong>Component tests</strong> are faster and more focused—great for testing a single component’s props, events, and states.</p>
<p><strong>Integration tests</strong> render your entire <code>App.vue</code> with router and Pinia. The user can navigate between pages, fill forms, and see how components work together. This is where you catch bugs that only appear when components interact.</p>
<p>For most Vue apps, I recommend focusing on <strong>integration tests</strong>. They give you more confidence because they test what users actually experience.</p>
<h3 id="the-test-app-helper">The “Test App” Helper<a class="heading-link" aria-label="Link to section" href="#the-test-app-helper"><span class="heading-link-icon">#</span></a></h3>
<p>To make testing easier, I use a helper function called <code>createTestApp</code>. It sets up your Router, Pinia (state), and renders your app using <code>vitest-browser-vue</code> so you don’t have to repeat it in every file.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// helpers/createTestApp.ts</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#9D7CD8;font-style:italic"> async</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> createTestApp</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // ... setup router, pinia, render app ...</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">    router</span><span style="color:#89DDFF">,</span><span style="color:#51597D;font-style:italic">       // The navigation system</span></span>
<span class="line"><span style="color:#C0CAF5">    cleanup</span><span style="color:#51597D;font-style:italic">       // A function to tidy up after the test</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// helpers/createTestApp.ts
export async function createTestApp() {
  // ... setup router, pinia, render app ...

  return {
    router,       // The navigation system
    cleanup       // A function to tidy up after the test
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<details class="collapsible astro-kncz7yy6"> <summary class="collapsible-summary astro-kncz7yy6"> <span class="collapsible-icon astro-kncz7yy6"> <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="astro-kncz7yy6"> <polyline points="9 18 15 12 9 6" class="astro-kncz7yy6"></polyline> </svg> </span> Full implementation example </summary> <div class="collapsible-content astro-kncz7yy6"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// helpers/createTestApp.ts</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#BB9AF7"> type</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">RouteLocationRaw</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> Router</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">vue-router</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">render</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">vitest-browser-vue</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">page</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">vitest/browser</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">expect</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">vitest</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">flushPromises</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">@vue/test-utils</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">createPinia</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">pinia</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">createMemoryHistory</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> createRouter</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">vue-router</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#0DB9D7"> App</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">@/App.vue</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">routes</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">@/router</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">useExercisesStore</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">@/stores/exercises</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">i18n</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">@/i18n</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#0DB9D7"> en</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">@/i18n/messages/en</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#0DB9D7">  CommonPO</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#0DB9D7">  BuilderPO</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#0DB9D7">  ActiveWorkoutPO</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#0DB9D7">  QueuePO</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#0DB9D7">  BenchmarksPO</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#0DB9D7">  BenchmarkFormPO</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#0DB9D7">  BenchmarkDetailPO</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">./pages</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">type</span><span style="color:#C0CAF5"> CreateTestAppOptions</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  initialRoute</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> string</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">type</span><span style="color:#C0CAF5"> TestApp</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  router</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Router</span></span>
<span class="line"><span style="color:#73DACA">  container</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Element</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Page Objects</span></span>
<span class="line"><span style="color:#73DACA">  common</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> CommonPO</span></span>
<span class="line"><span style="color:#73DACA">  builder</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> BuilderPO</span></span>
<span class="line"><span style="color:#73DACA">  workout</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> ActiveWorkoutPO</span></span>
<span class="line"><span style="color:#73DACA">  queue</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> QueuePO</span></span>
<span class="line"><span style="color:#73DACA">  benchmarks</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> BenchmarksPO</span></span>
<span class="line"><span style="color:#73DACA">  benchmarkForm</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> BenchmarkFormPO</span></span>
<span class="line"><span style="color:#73DACA">  benchmarkDetail</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> BenchmarkDetailPO</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Raw query methods (use page.getBy* for new code)</span></span>
<span class="line"><span style="color:#73DACA">  getByRole</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> typeof</span><span style="color:#C0CAF5"> page</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">getByRole</span></span>
<span class="line"><span style="color:#73DACA">  getByText</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> typeof</span><span style="color:#C0CAF5"> page</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">getByText</span></span>
<span class="line"><span style="color:#73DACA">  getByTestId</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> typeof</span><span style="color:#C0CAF5"> page</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">getByTestId</span></span>
<span class="line"><span style="color:#73DACA">  queryByRole</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> typeof</span><span style="color:#C0CAF5"> page</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">getByRole</span></span>
<span class="line"><span style="color:#73DACA">  queryByText</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> typeof</span><span style="color:#C0CAF5"> page</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">getByText</span></span>
<span class="line"><span style="color:#73DACA">  findByRole</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> typeof</span><span style="color:#C0CAF5"> page</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">getByRole</span></span>
<span class="line"><span style="color:#73DACA">  findByText</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> typeof</span><span style="color:#C0CAF5"> page</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">getByText</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Helpers</span></span>
<span class="line"><span style="color:#7AA2F7">  navigateTo</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">to</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> RouteLocationRaw</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#C0CAF5"> Promise</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">void</span><span style="color:#89DDFF">&gt;</span></span>
<span class="line"><span style="color:#7AA2F7">  cleanup</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#9D7CD8;font-style:italic"> async</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> createTestApp</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">options</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> CreateTestAppOptions</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Promise</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">TestApp</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> initialRoute</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">/</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> options</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> pinia</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> createPinia</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> router</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> createRouter</span><span style="color:#9ABDF5">({</span></span>
<span class="line"><span style="color:#73DACA">    history</span><span style="color:#89DDFF">:</span><span style="color:#7AA2F7"> createMemoryHistory</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    routes</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">initialRoute</span><span style="color:#BB9AF7"> !==</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">/</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">    router</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">push</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">initialRoute</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Preload English messages for tests</span></span>
<span class="line"><span style="color:#C0CAF5">  i18n</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">global</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">setLocaleMessage</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">en</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> en</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#C0CAF5">  i18n</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">global</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">locale</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">en</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> screen</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> render</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">App</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">    global</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">      plugins</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#7DCFFF">router</span><span style="color:#89DDFF">,</span><span style="color:#7DCFFF"> pinia</span><span style="color:#89DDFF">,</span><span style="color:#7DCFFF"> i18n</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  await</span><span style="color:#C0CAF5"> router</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">isReady</span><span style="color:#9ABDF5">()</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Flush Vue&#39;s async operations to ensure onMounted fires</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  await</span><span style="color:#7AA2F7"> flushPromises</span><span style="color:#9ABDF5">()</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Wait for app initialization to complete (exercises seeding and loading)</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> exercisesStore</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> useExercisesStore</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">pinia</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  await</span><span style="color:#C0CAF5"> expect</span></span>
<span class="line"><span style="color:#89DDFF">    .</span><span style="color:#7AA2F7">poll</span><span style="color:#9ABDF5">(() </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#C0CAF5"> exercisesStore</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">customExercises</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">length</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">timeout</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 5000</span><span style="color:#9ABDF5"> })</span></span>
<span class="line"><span style="color:#89DDFF">    .</span><span style="color:#7AA2F7">toBeGreaterThan</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">0</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Create context for page objects</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> context</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> { </span><span style="color:#C0CAF5">router</span><span style="color:#9ABDF5"> }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Instantiate page objects</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> common</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> CommonPO</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">context</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> builder</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> BuilderPO</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">context</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> common</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> workout</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> ActiveWorkoutPO</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">context</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> common</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> queue</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> QueuePO</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">context</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> common</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> benchmarks</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> BenchmarksPO</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">context</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> common</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> benchmarkForm</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> BenchmarkFormPO</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">context</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> common</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> benchmarkDetail</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> BenchmarkDetailPO</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">context</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> common</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Simple navigation helper</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  async</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> navigateTo</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">to</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> RouteLocationRaw</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    await</span><span style="color:#C0CAF5"> router</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">push</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">to</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // vitest-browser-vue cleans up before tests automatically</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // This is kept for backward compatibility with test structure</span></span>
<span class="line"><span style="color:#BB9AF7">  function</span><span style="color:#7AA2F7"> cleanup</span><span style="color:#9ABDF5">() {</span></span>
<span class="line"><span style="color:#C0CAF5">    screen</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">unmount</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">    router</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    container</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> screen</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">container</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">    // Page Objects</span></span>
<span class="line"><span style="color:#C0CAF5">    common</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    builder</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    workout</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    queue</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    benchmarks</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    benchmarkForm</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    benchmarkDetail</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">    // Raw query methods - use page locators (return Locators, not HTMLElements)</span></span>
<span class="line"><span style="color:#73DACA">    getByRole</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> page</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">getByRole</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">bind</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">page</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    getByText</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> page</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">getByText</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">bind</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">page</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    getByTestId</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> page</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">getByTestId</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">bind</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">page</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    queryByRole</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> page</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">getByRole</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">bind</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">page</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    queryByText</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> page</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">getByText</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">bind</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">page</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    findByRole</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> page</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">getByRole</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">bind</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">page</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    findByText</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> page</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">getByText</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">bind</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">page</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">    // Helpers</span></span>
<span class="line"><span style="color:#C0CAF5">    navigateTo</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    cleanup</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// helpers/createTestApp.ts
import type { RouteLocationRaw, Router } from 'vue-router'
import { render } from 'vitest-browser-vue'
import { page } from 'vitest/browser'
import { expect } from 'vitest'
import { flushPromises } from '@vue/test-utils'
import { createPinia } from 'pinia'
import { createMemoryHistory, createRouter } from 'vue-router'
import App from '@/App.vue'
import { routes } from '@/router'
import { useExercisesStore } from '@/stores/exercises'
import { i18n } from '@/i18n'
import en from '@/i18n/messages/en'
import {
  CommonPO,
  BuilderPO,
  ActiveWorkoutPO,
  QueuePO,
  BenchmarksPO,
  BenchmarkFormPO,
  BenchmarkDetailPO,
} from './pages'

type CreateTestAppOptions = {
  initialRoute?: string
}

type TestApp = {
  router: Router
  container: Element
  // Page Objects
  common: CommonPO
  builder: BuilderPO
  workout: ActiveWorkoutPO
  queue: QueuePO
  benchmarks: BenchmarksPO
  benchmarkForm: BenchmarkFormPO
  benchmarkDetail: BenchmarkDetailPO
  // Raw query methods (use page.getBy* for new code)
  getByRole: typeof page.getByRole
  getByText: typeof page.getByText
  getByTestId: typeof page.getByTestId
  queryByRole: typeof page.getByRole
  queryByText: typeof page.getByText
  findByRole: typeof page.getByRole
  findByText: typeof page.getByText
  // Helpers
  navigateTo: (to: RouteLocationRaw) => Promise<void>
  cleanup: () => void
}

export async function createTestApp(options: CreateTestAppOptions = {}): Promise<TestApp> {
  const { initialRoute = '/' } = options

  const pinia = createPinia()
  const router = createRouter({
    history: createMemoryHistory(),
    routes,
  })

  if (initialRoute !== '/') {
    router.push(initialRoute)
  }

  // Preload English messages for tests
  i18n.global.setLocaleMessage('en', en)
  i18n.global.locale.value = 'en'

  const screen = render(App, {
    global: {
      plugins: [router, pinia, i18n],
    },
  })

  await router.isReady()

  // Flush Vue's async operations to ensure onMounted fires
  await flushPromises()

  // Wait for app initialization to complete (exercises seeding and loading)
  const exercisesStore = useExercisesStore(pinia)
  await expect
    .poll(() => exercisesStore.customExercises.length, { timeout: 5000 })
    .toBeGreaterThan(0)

  // Create context for page objects
  const context = { router }

  // Instantiate page objects
  const common = new CommonPO(context)
  const builder = new BuilderPO(context, common)
  const workout = new ActiveWorkoutPO(context, common)
  const queue = new QueuePO(context, common)
  const benchmarks = new BenchmarksPO(context, common)
  const benchmarkForm = new BenchmarkFormPO(context, common)
  const benchmarkDetail = new BenchmarkDetailPO(context, common)

  // Simple navigation helper
  async function navigateTo(to: RouteLocationRaw) {
    await router.push(to)
  }

  // vitest-browser-vue cleans up before tests automatically
  // This is kept for backward compatibility with test structure
  function cleanup() {
    screen.unmount()
  }

  return {
    router,
    container: screen.container,
    // Page Objects
    common,
    builder,
    workout,
    queue,
    benchmarks,
    benchmarkForm,
    benchmarkDetail,
    // Raw query methods - use page locators (return Locators, not HTMLElements)
    getByRole: page.getByRole.bind(page),
    getByText: page.getByText.bind(page),
    getByTestId: page.getByTestId.bind(page),
    queryByRole: page.getByRole.bind(page),
    queryByText: page.getByText.bind(page),
    findByRole: page.getByRole.bind(page),
    findByText: page.getByText.bind(page),
    // Helpers
    navigateTo,
    cleanup,
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </details>  
<div class="alert alert-note astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">💡</span> Note </p> <div class="alert-content astro-7kdbuayl"> <p>This isn’t a library you download. It’s a helper file you write once for your project to handle the setup boilerplate.</p> </div> </div> 
<h3 id="a-real-integration-test">A Real Integration Test<a class="heading-link" aria-label="Link to section" href="#a-real-integration-test"><span class="heading-link-icon">#</span></a></h3>
<p>Notice how we use <code>getByRole</code> to find elements—this ensures our app is accessible:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">page</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> userEvent</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">vitest/browser</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">completes a set</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9D7CD8;font-style:italic"> async</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  await</span><span style="color:#7AA2F7"> createTestApp</span><span style="color:#9ABDF5">()</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // 1. Find the &quot;Start&quot; button and click it</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  await</span><span style="color:#C0CAF5"> userEvent</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">click</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">page</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">getByRole</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">button</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> /</span><span style="color:#B4F9F8">start</span><span style="color:#89DDFF">/i</span><span style="color:#9ABDF5"> }))</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // 2. Type &quot;100&quot; into the weight input</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> weightInput</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> page</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">getByRole</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">spinbutton</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> /</span><span style="color:#B4F9F8">weight</span><span style="color:#89DDFF">/i</span><span style="color:#9ABDF5"> })</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  await</span><span style="color:#C0CAF5"> userEvent</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">type</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">weightInput</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">100</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // 3. Click &quot;Complete&quot;</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  await</span><span style="color:#C0CAF5"> userEvent</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">click</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">page</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">getByRole</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">button</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> /</span><span style="color:#B4F9F8">complete</span><span style="color:#89DDFF">/i</span><span style="color:#9ABDF5"> }))</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // 4. Wait for the success message</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  await</span><span style="color:#C0CAF5"> expect</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">element</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">page</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">getByText</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">Set Completed</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toBeVisible</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#9ABDF5">})</span></span></code><button type="button" class="copy" data-code="import { page, userEvent } from 'vitest/browser'

it('completes a set', async () => {
  await createTestApp()

  // 1. Find the &#34;Start&#34; button and click it
  await userEvent.click(page.getByRole('button', { name: /start/i }))

  // 2. Type &#34;100&#34; into the weight input
  const weightInput = page.getByRole('spinbutton', { name: /weight/i })
  await userEvent.type(weightInput, '100')

  // 3. Click &#34;Complete&#34;
  await userEvent.click(page.getByRole('button', { name: /complete/i }))

  // 4. Wait for the success message
  await expect.element(page.getByText('Set Completed')).toBeVisible()
})" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<div class="alert alert-tip astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">💪</span> getByRole = Built-in Accessibility Testing </p> <div class="alert-content astro-7kdbuayl"> <p>Always prefer <code>getByRole()</code> over <code>getByTestId()</code> or CSS selectors. When you use <code>getByRole(&#39;button&#39;, { name: /submit/i })</code>, you’re asserting that:</p><ol>
<li>The element has the correct ARIA role (it’s actually a button)</li>
<li>The element has an accessible name (screen readers can announce it)</li>
<li>The element is visible and interactive</li>
</ol><p>If your test can’t find an element by role, that’s a signal your UI has an accessibility problem—fix the component, not the test. Reserve <code>getByTestId</code> only for elements that truly have no semantic meaning.</p> </div> </div> 
<h3 id="page-objects-handling-dom-interaction">Page Objects: Handling DOM Interaction<a class="heading-link" aria-label="Link to section" href="#page-objects-handling-dom-interaction"><span class="heading-link-icon">#</span></a></h3>
<p>As your test suite grows, you’ll notice repetitive DOM queries everywhere. <strong>Page Objects</strong> solve this by encapsulating all DOM interactions for a specific page or component.</p>
<blockquote>
<p><strong>Key Difference:</strong> Factories handle <strong>data</strong> (creating test objects). Page Objects handle <strong>DOM interaction</strong> (clicking, typing, querying elements). They complement each other.</p>
</blockquote>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// pages/WorkoutPage.ts</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">page</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> userEvent</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">vitest/browser</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> class</span><span style="color:#C0CAF5"> WorkoutPage</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Queries - finding elements</span></span>
<span class="line"><span style="color:#BB9AF7">  get</span><span style="color:#7AA2F7"> startButton</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#C0CAF5"> page</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">getByRole</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">button</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> /</span><span style="color:#B4F9F8">start</span><span style="color:#89DDFF">/i</span><span style="color:#9ABDF5"> })</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  get</span><span style="color:#7AA2F7"> weightInput</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#C0CAF5"> page</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">getByRole</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">spinbutton</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> /</span><span style="color:#B4F9F8">weight</span><span style="color:#89DDFF">/i</span><span style="color:#9ABDF5"> })</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Actions - user interactions</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  async</span><span style="color:#7AA2F7"> start</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    await</span><span style="color:#C0CAF5"> userEvent</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">click</span><span style="color:#9ABDF5">(</span><span style="color:#F7768E">this</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">startButton</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  async</span><span style="color:#7AA2F7"> setWeight</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">value</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    await</span><span style="color:#C0CAF5"> userEvent</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">clear</span><span style="color:#9ABDF5">(</span><span style="color:#F7768E">this</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">weightInput</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    await</span><span style="color:#C0CAF5"> userEvent</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">type</span><span style="color:#9ABDF5">(</span><span style="color:#F7768E">this</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">weightInput</span><span style="color:#89DDFF">,</span><span style="color:#7AA2F7"> String</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">value</span><span style="color:#9ABDF5">))</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  async</span><span style="color:#7AA2F7"> completeSet</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    await</span><span style="color:#C0CAF5"> userEvent</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">click</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">page</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">getByRole</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">button</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> /</span><span style="color:#B4F9F8">complete</span><span style="color:#89DDFF">/i</span><span style="color:#9ABDF5"> }))</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// pages/WorkoutPage.ts
import { page, userEvent } from 'vitest/browser'

export class WorkoutPage {
  // Queries - finding elements
  get startButton() {
    return page.getByRole('button', { name: /start/i })
  }

  get weightInput() {
    return page.getByRole('spinbutton', { name: /weight/i })
  }

  // Actions - user interactions
  async start() {
    await userEvent.click(this.startButton)
  }

  async setWeight(value: number) {
    await userEvent.clear(this.weightInput)
    await userEvent.type(this.weightInput, String(value))
  }

  async completeSet() {
    await userEvent.click(page.getByRole('button', { name: /complete/i }))
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>Now your tests read like plain English:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">page</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">vitest/browser</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">completes a set with weight</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9D7CD8;font-style:italic"> async</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> workoutPage</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> WorkoutPage</span><span style="color:#9ABDF5">()</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  await</span><span style="color:#C0CAF5"> workoutPage</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">start</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  await</span><span style="color:#C0CAF5"> workoutPage</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">setWeight</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">100</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  await</span><span style="color:#C0CAF5"> workoutPage</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">completeSet</span><span style="color:#9ABDF5">()</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  await</span><span style="color:#C0CAF5"> expect</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">element</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">page</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">getByText</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">Set Completed</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toBeVisible</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#9ABDF5">})</span></span></code><button type="button" class="copy" data-code="import { page } from 'vitest/browser'

it('completes a set with weight', async () => {
  const workoutPage = new WorkoutPage()

  await workoutPage.start()
  await workoutPage.setWeight(100)
  await workoutPage.completeSet()

  await expect.element(page.getByText('Set Completed')).toBeVisible()
})" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>




















<table><thead><tr><th>Helper</th><th>Handles</th><th>Used In</th></tr></thead><tbody><tr><td data-label="Helper"><strong>Factories</strong></td><td data-label="Handles">Test data (objects, entities)</td><td data-label="Used In">Unit tests, Integration tests</td></tr><tr><td data-label="Helper"><strong>Page Objects</strong></td><td data-label="Handles">DOM interaction (clicks, queries)</td><td data-label="Used In">Integration tests only</td></tr></tbody></table>
<aside aria-label="When to Use Page Objects" class="aside aside-tip astro-37uy2q7c"> <div class="aside-content astro-37uy2q7c"> <p class="aside-title astro-37uy2q7c"> <span class="aside-emoji astro-37uy2q7c" role="img" aria-hidden="true">💡</span> When to Use Page Objects </p> <section class="aside-body astro-37uy2q7c"> <p>Don’t create Page Objects upfront. Write your first few tests with inline queries. When you notice the same <code>getByRole</code> patterns repeating across 3+ tests, extract them into a Page Object.</p> </section> </div> </aside> 
<aside aria-label="Automate the Refactoring" class="aside aside-note astro-37uy2q7c"> <div class="aside-content astro-37uy2q7c"> <p class="aside-title astro-37uy2q7c"> <span class="aside-emoji astro-37uy2q7c" role="img" aria-hidden="true">📝</span> Automate the Refactoring </p> <section class="aside-body astro-37uy2q7c"> <p>I use a <a target="_blank" rel="noopener noreferrer" href="/prompts/claude/claude-refactor-page-object-command">Claude Code command to refactor tests into Page Objects</a> automatically. Point it at a test file and it extracts repeated queries into a clean page object factory.</p> </section> </div> </aside> 
<p>This approach aligns with black box testing principles—testing behavior rather than implementation details.</p>
<span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/stop-white-box-testing-vue/" class="internal-link astro-3tyn5ojg"> Stop White Box Testing Vue Components </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Stop White Box Testing Vue Components Use Testing Library Instead</span> <span class="preview-description astro-3tyn5ojg">White Box testing makes your Vue tests fragile and misleading. In this post, I’ll show you how Testing Library helps you write Black Box tests that are resilient, realistic, and focused on actual user behavior</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">vue</span><span class="preview-tag astro-3tyn5ojg">testing</span>  </span> <time class="preview-date astro-3tyn5ojg">Apr 19, 2025</time> </span> </span> </span>  <script>
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
</script>
<hr/>
<h2 id="layer-3-accessibility-and-visual-tests">Layer 3: Accessibility and Visual Tests<a class="heading-link" aria-label="Link to section" href="#layer-3-accessibility-and-visual-tests"><span class="heading-link-icon">#</span></a></h2>
<p>These are the “cherries on top” of your pyramid.</p>
<h3 id="accessibility-a11y">Accessibility (A11y)<a class="heading-link" aria-label="Link to section" href="#accessibility-a11y"><span class="heading-link-icon">#</span></a></h3>
<p>We use a tool called <strong>axe-core</strong>. It scans your rendered HTML for common violations (like low contrast text or missing labels).</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">has no accessibility violations</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9D7CD8;font-style:italic"> async</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> container</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#7AA2F7"> createTestApp</span><span style="color:#9ABDF5">()</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // This one line checks for dozens of common a11y bugs!</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  await</span><span style="color:#7AA2F7"> assertNoViolations</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">container</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">})</span></span></code><button type="button" class="copy" data-code="it('has no accessibility violations', async () => {
  const { container } = await createTestApp()

  // This one line checks for dozens of common a11y bugs!
  await assertNoViolations(container)
})" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<aside aria-label="Learn More About Accessibility Testing" class="aside aside-tip astro-37uy2q7c"> <div class="aside-content astro-37uy2q7c"> <p class="aside-title astro-37uy2q7c"> <span class="aside-emoji astro-37uy2q7c" role="img" aria-hidden="true">💡</span> Learn More About Accessibility Testing </p> <section class="aside-body astro-37uy2q7c"> <p>For a complete setup guide with jest-axe, see <span class="internal-link-wrapper astro-3tyn5ojg"> <a target="_blank" rel="noopener noreferrer" href="/posts/how-to-improve-accessibility-with-testing-library-and-jest-axe-for-your-vue-application/" class="internal-link astro-3tyn5ojg"> How to Improve Accessibility with Testing Library and jest-axe </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">How to Improve Accessibility with Testing Library and jest-axe for Your Vue Application</span> <span class="preview-description astro-3tyn5ojg">Use Jest axe to have automatic tests for your vue application</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">vue</span><span class="preview-tag astro-3tyn5ojg">accessibility</span>  </span> <time class="preview-date astro-3tyn5ojg">Apr 12, 2023</time> </span> </span> </span>  <script>
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
</script>. For general Vue accessibility best practices, check out <span class="internal-link-wrapper astro-3tyn5ojg"> <a target="_blank" rel="noopener noreferrer" href="/posts/vue-accessibility-blueprint-8-steps/" class="internal-link astro-3tyn5ojg"> Vue Accessibility Blueprint: 8 Steps </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Vue Accessibility Blueprint: 8 Steps</span> <span class="preview-description astro-3tyn5ojg">Master Vue accessibility with our comprehensive guide. Learn 8 crucial steps to create inclusive, WCAG-compliant web applications that work for all users.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">vue</span><span class="preview-tag astro-3tyn5ojg">accessibility</span>  </span> <time class="preview-date astro-3tyn5ojg">May 18, 2024</time> </span> </span> </span>  <script>
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
</script>.</p> </section> </div> </aside> 
<h3 id="visual-regression">Visual Regression<a class="heading-link" aria-label="Link to section" href="#visual-regression"><span class="heading-link-icon">#</span></a></h3>
<p>This takes a screenshot of your component and compares it to a “golden” version saved on your computer. If a pixel changes, the test fails.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">matches the design</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9D7CD8;font-style:italic"> async</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  await</span><span style="color:#7AA2F7"> expect</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">page</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">getByTestId</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">app</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toMatchScreenshot</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">settings-page.png</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">})</span></span></code><button type="button" class="copy" data-code="it('matches the design', async () => {
  await expect(page.getByTestId('app')).toMatchScreenshot('settings-page.png')
})" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>Use this sparingly. Visual tests are brittle (even a font rendering update can break them), so only use them for critical screens.</p>
<aside aria-label="Deep Dive into Visual Testing" class="aside aside-info astro-37uy2q7c"> <div class="aside-content astro-37uy2q7c"> <p class="aside-title astro-37uy2q7c"> <span class="aside-emoji astro-37uy2q7c" role="img" aria-hidden="true">ℹ️</span> Deep Dive into Visual Testing </p> <section class="aside-body astro-37uy2q7c"> <p>For a complete setup guide on visual regression testing with Vitest browser mode, see <span class="internal-link-wrapper astro-3tyn5ojg"> <a target="_blank" rel="noopener noreferrer" href="/posts/visual-regression-testing-with-vue-and-vitest-browser/" class="internal-link astro-3tyn5ojg"> How to Do Visual Regression Testing in Vue with Vitest </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">How to Do Visual Regression Testing in Vue with Vitest?</span> <span class="preview-description astro-3tyn5ojg">Learn how to implement visual regression testing in Vue.js using Vitest&#39;s browser mode. This comprehensive guide covers setting up screenshot-based testing, creating component stories, and integrating with CI/CD pipelines for automated visual testing.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">vue</span><span class="preview-tag astro-3tyn5ojg">testing</span><span class="preview-tag astro-3tyn5ojg">vitest</span>  </span> <time class="preview-date astro-3tyn5ojg">Feb 22, 2025</time> </span> </span> </span>  <script>
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
</script>.</p> </section> </div> </aside> 
<h3 id="testing-your-core-ui-library">Testing Your Core UI Library<a class="heading-link" aria-label="Link to section" href="#testing-your-core-ui-library"><span class="heading-link-icon">#</span></a></h3>
<p>There’s one place where visual regression and accessibility tests shine: <strong>your base component library</strong>.</p>
<p>If you’re building your own UI components (BaseButton, DatePicker, Modal, Input), these components should be:</p>
<ul>
<li><strong>Dumb</strong> — no business logic, just presentation</li>
<li><strong>Reusable</strong> — used across your entire app</li>
<li><strong>Stable</strong> — rarely change once built</li>
</ul>
<p>This makes them perfect candidates for visual and accessibility testing:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// BaseButton.visual.spec.ts</span></span>
<span class="line"><span style="color:#7AA2F7">describe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">BaseButton</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">renders all variants correctly</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9D7CD8;font-style:italic"> async</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">    render</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">ButtonStory</span><span style="color:#9ABDF5">) </span><span style="color:#51597D;font-style:italic">// A component showing all button states</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    await</span><span style="color:#7AA2F7"> expect</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">page</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toMatchScreenshot</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">button-variants.png</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">has no accessibility violations</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9D7CD8;font-style:italic"> async</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> container</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> render</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">BaseButton</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">      props</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">label</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Click me</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5"> }</span></span>
<span class="line"><span style="color:#9ABDF5">    })</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    await</span><span style="color:#7AA2F7"> assertNoViolations</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">container</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span></span>
<span class="line"><span style="color:#9ABDF5">})</span></span></code><button type="button" class="copy" data-code="// BaseButton.visual.spec.ts
describe('BaseButton', () => {
  it('renders all variants correctly', async () => {
    render(ButtonStory) // A component showing all button states
    await expect(page).toMatchScreenshot('button-variants.png')
  })

  it('has no accessibility violations', async () => {
    const { container } = render(BaseButton, {
      props: { label: 'Click me' }
    })
    await assertNoViolations(container)
  })
})" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>For each base component, test:</p>





















<table><thead><tr><th>Test Type</th><th>What to Check</th></tr></thead><tbody><tr><td data-label="Test Type"><strong>Visual</strong></td><td data-label="What to Check">All variants (primary, secondary, disabled, loading)</td></tr><tr><td data-label="Test Type"><strong>A11y</strong></td><td data-label="What to Check">Focus states, ARIA attributes, color contrast</td></tr><tr><td data-label="Test Type"><strong>Keyboard</strong></td><td data-label="What to Check">Tab navigation, Enter/Space activation</td></tr></tbody></table>
<aside aria-label="Using a Component Library?" class="aside aside-note astro-37uy2q7c"> <div class="aside-content astro-37uy2q7c"> <p class="aside-title astro-37uy2q7c"> <span class="aside-emoji astro-37uy2q7c" role="img" aria-hidden="true">📝</span> Using a Component Library? </p> <section class="aside-body astro-37uy2q7c"> <p>If you use a pre-built library like <strong>shadcn/ui</strong>, <strong>Vuetify</strong>, or <strong>PrimeVue</strong>, skip this. Those libraries already handle visual consistency and accessibility. Focus your testing efforts on your business logic and user flows instead.</p> </section> </div> </aside> 
<hr/>
<h2 id="why-not-end-to-end-e2e-tests">Why Not End-to-End (E2E) Tests?<a class="heading-link" aria-label="Link to section" href="#why-not-end-to-end-e2e-tests"><span class="heading-link-icon">#</span></a></h2>
<p>You might hear people say, “Just use Cypress or Playwright for everything!”</p>
<p>E2E tests mean <strong>zero mocking</strong>—you run your real backend and database. They test your entire stack: Frontend + Backend + Database.</p>
<p>For a new developer or a solo project, this is painful because:</p>
<ul>
<li>It’s slow</li>
<li>It breaks easily (if the backend API is down, your frontend tests fail)</li>
</ul>
<h3 id="the-alternative-mocking">The Alternative: Mocking<a class="heading-link" aria-label="Link to section" href="#the-alternative-mocking"><span class="heading-link-icon">#</span></a></h3>
<p>Instead, we use <strong>MSW (Mock Service Worker)</strong>. It intercepts network requests and returns fake data immediately. This makes your integration tests fast and stable. You don’t need a running backend to test your frontend.</p>
<div class="alert alert-tip astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">💪</span> The Golden Rule of Mocking </p> <div class="alert-content astro-7kdbuayl"> <p><strong>The less you mock, the better your tests.</strong> Every mock is a lie you’re telling your test suite. Mock only what you can’t control:</p><ul>
<li><strong>External APIs</strong> (network calls to third-party services)</li>
<li><strong>System boundaries</strong> (time, random numbers, file system)</li>
<li><strong>Paid services</strong> (payment gateways, SMS providers)</li>
</ul><p>Never mock your own code just to make tests easier. If a component is hard to test without mocking internal modules, that’s a sign your architecture needs refactoring—not more mocks.</p> </div> </div> 
<div class="alert alert-note astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">💡</span> What about Contract Testing? </p> <div class="alert-content astro-7kdbuayl"> <p>In large corporate teams, you might use “Contract Testing” to ensure your mocks match the real API. For now, don’t worry about it. Focus on getting your integration and unit tests running smoothly.</p> </div> </div> 
<hr/>
<h2 id="comparison-testing-approaches">Comparison: Testing Approaches<a class="heading-link" aria-label="Link to section" href="#comparison-testing-approaches"><span class="heading-link-icon">#</span></a></h2>













































<table><thead><tr><th>Layer</th><th>Speed</th><th>Confidence</th><th>Flakiness</th><th>Distribution</th><th>When to Use</th></tr></thead><tbody><tr><td data-label="Layer"><strong>Unit Tests (Composables)</strong></td><td data-label="Speed">⚡ Very fast</td><td data-label="Confidence">Medium</td><td data-label="Flakiness">None</td><td data-label="Distribution">~20%</td><td data-label="When to Use">Logic validation, utility functions</td></tr><tr><td data-label="Layer"><strong>Integration Tests (Browser)</strong></td><td data-label="Speed">🚀 Fast</td><td data-label="Confidence">High</td><td data-label="Flakiness">Low</td><td data-label="Distribution"><strong>~70%</strong></td><td data-label="When to Use">User flows, component interaction</td></tr><tr><td data-label="Layer"><strong>A11y Tests</strong></td><td data-label="Speed">🚀 Fast</td><td data-label="Confidence">High</td><td data-label="Flakiness">Medium</td><td data-label="Distribution">~5%</td><td data-label="When to Use">Critical screens, forms</td></tr><tr><td data-label="Layer"><strong>Visual Regression</strong></td><td data-label="Speed">🐢 Slow</td><td data-label="Confidence">Medium</td><td data-label="Flakiness">High</td><td data-label="Distribution">~5%</td><td data-label="When to Use">Design system components</td></tr></tbody></table>
<hr/>
<h2 id="summary-your-next-steps">Summary: Your Next Steps<a class="heading-link" aria-label="Link to section" href="#summary-your-next-steps"><span class="heading-link-icon">#</span></a></h2>
<p>Don’t try to implement the whole pyramid today. Start with what matters most.</p>
<h3 id="step-1-identify-what-can-never-fail">Step 1: Identify What Can Never Fail<a class="heading-link" aria-label="Link to section" href="#step-1-identify-what-can-never-fail"><span class="heading-link-icon">#</span></a></h3>
<p>Ask yourself: <em>“What flows in my app would be catastrophic if they broke?”</em> For an e-commerce site, that’s checkout. For a banking app, that’s transfers. For my workout tracker, it’s completing a set.</p>
<p>Write integration tests for these critical paths first using Vitest browser mode. Even 3-5 tests covering your core flows provide massive confidence.</p>
<h3 id="step-2-set-up-the-infrastructure">Step 2: Set Up the Infrastructure<a class="heading-link" aria-label="Link to section" href="#step-2-set-up-the-infrastructure"><span class="heading-link-icon">#</span></a></h3>
<p>Get Vitest browser mode running with a simple <code>createTestApp</code> helper. Once you can render your app and click a button in a test, you have the foundation for everything else.</p>
<h3 id="step-3-write-tickets-with-testable-acceptance-criteria">Step 3: Write Tickets with Testable Acceptance Criteria<a class="heading-link" aria-label="Link to section" href="#step-3-write-tickets-with-testable-acceptance-criteria"><span class="heading-link-icon">#</span></a></h3>
<p>Good tickets have Gherkin-style acceptance criteria that read like tests:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="gherkin"><code><span class="line"><span style="color:#BB9AF7">Given </span><span style="color:#A9B1D6">I am on the workout page</span></span>
<span class="line"><span style="color:#BB9AF7">When </span><span style="color:#A9B1D6">I tap </span><span style="color:#9ECE6A">&quot;Complete Set&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">Then </span><span style="color:#A9B1D6">I should see </span><span style="color:#9ECE6A">&quot;Set Completed&quot;</span><span style="color:#A9B1D6"> confirmation</span></span>
<span class="line"><span style="color:#BB9AF7">And </span><span style="color:#A9B1D6">the set should be saved to history</span></span></code><button type="button" class="copy" data-code="Given I am on the workout page
When I tap &#34;Complete Set&#34;
Then I should see &#34;Set Completed&#34; confirmation
And the set should be saved to history" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>These ACs translate directly into integration tests. Now you can practice TDD: write the test from the AC first, watch it fail, then implement the feature.</p>
<h3 id="step-4-extract-patterns-as-you-go">Step 4: Extract Patterns as You Go<a class="heading-link" aria-label="Link to section" href="#step-4-extract-patterns-as-you-go"><span class="heading-link-icon">#</span></a></h3>
<p>Don’t create factories or page objects upfront. Write a few tests with inline data and queries. When you notice repetition, extract it. This way, your abstractions solve real problems instead of imagined ones.</p>
<p>For guidance on writing clear, maintainable test names, check out <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/frontend-testing-guide-10-essential-rules/" class="internal-link astro-3tyn5ojg"> Frontend Testing Guide: 10 Essential Rules for Naming Tests </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Frontend Testing Guide: 10 Essential Rules for Naming Tests</span> <span class="preview-description astro-3tyn5ojg">Learn how to write clear and maintainable frontend tests with 10 practical naming rules. Includes real-world examples showing good and bad practices for component testing across any framework.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">testing</span><span class="preview-tag astro-3tyn5ojg">vitest</span>  </span> <time class="preview-date astro-3tyn5ojg">Oct 26, 2024</time> </span> </span> </span>  <script>
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
<aside aria-label="See It in Action" class="aside aside-note astro-37uy2q7c"> <div class="aside-content astro-37uy2q7c"> <p class="aside-title astro-37uy2q7c"> <span class="aside-emoji astro-37uy2q7c" role="img" aria-hidden="true">📝</span> See It in Action </p> <section class="aside-body astro-37uy2q7c"> <p>Want to see this testing setup in a real project? Check out my <a target="_blank" rel="noopener noreferrer" href="https://github.com/alexanderop/workoutTracker" rel="noopener noreferrer" target="_blank">Workout Tracker PWA on GitHub</a>. It includes the <code>createTestApp</code> helper, page objects, factories, and integration tests using Vitest browser mode.</p> </section> </div> </aside> 
<hr/>
<h2 id="bonus-performance-testing-in-ci">Bonus: Performance Testing in CI<a class="heading-link" aria-label="Link to section" href="#bonus-performance-testing-in-ci"><span class="heading-link-icon">#</span></a></h2>
<p>While not part of the traditional testing pyramid, <strong>performance budgets</strong> catch regressions before they reach production. I run Lighthouse CI on every build to enforce thresholds for performance, accessibility, and best practices.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="yaml"><code><span class="line"><span style="color:#51597D;font-style:italic"># .github/workflows/ci.yml</span></span>
<span class="line"><span style="color:#F7768E">performance-budget</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#F7768E">  needs</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> build</span></span>
<span class="line"><span style="color:#F7768E">  runs-on</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> ubuntu-latest</span></span>
<span class="line"><span style="color:#F7768E">  timeout-minutes</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 10</span></span>
<span class="line"><span style="color:#F7768E">  steps</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#9ABDF5">    -</span><span style="color:#F7768E"> name</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Checkout code</span></span>
<span class="line"><span style="color:#F7768E">      uses</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> actions/checkout@v4.2.2</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9ABDF5">    -</span><span style="color:#F7768E"> name</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Setup pnpm</span></span>
<span class="line"><span style="color:#F7768E">      uses</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> pnpm/action-setup@v4.1.0</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9ABDF5">    -</span><span style="color:#F7768E"> name</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Setup Node.js</span></span>
<span class="line"><span style="color:#F7768E">      uses</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> actions/setup-node@v4.4.0</span></span>
<span class="line"><span style="color:#F7768E">      with</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#F7768E">        node-version</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> ${{ env.NODE_VERSION }}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9ABDF5">    -</span><span style="color:#F7768E"> name</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Restore node_modules</span></span>
<span class="line"><span style="color:#F7768E">      uses</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> actions/cache/restore@v4.2.3</span></span>
<span class="line"><span style="color:#F7768E">      with</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#F7768E">        path</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> node_modules</span></span>
<span class="line"><span style="color:#F7768E">        key</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> node-modules-${{ runner.os }}-${{ hashFiles(&#39;pnpm-lock.yaml&#39;) }}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9ABDF5">    -</span><span style="color:#F7768E"> name</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Download build artifacts</span></span>
<span class="line"><span style="color:#F7768E">      uses</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> actions/download-artifact@v6.0.0</span></span>
<span class="line"><span style="color:#F7768E">      with</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#F7768E">        name</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> dist</span></span>
<span class="line"><span style="color:#F7768E">        path</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> dist</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9ABDF5">    -</span><span style="color:#F7768E"> name</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Run Lighthouse CI</span></span>
<span class="line"><span style="color:#F7768E">      run</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> pnpm lhci autorun</span></span></code><button type="button" class="copy" data-code="# .github/workflows/ci.yml
performance-budget:
  needs: build
  runs-on: ubuntu-latest
  timeout-minutes: 10
  steps:
    - name: Checkout code
      uses: actions/checkout@v4.2.2

    - name: Setup pnpm
      uses: pnpm/action-setup@v4.1.0

    - name: Setup Node.js
      uses: actions/setup-node@v4.4.0
      with:
        node-version: ${{ env.NODE_VERSION }}

    - name: Restore node_modules
      uses: actions/cache/restore@v4.2.3
      with:
        path: node_modules
        key: node-modules-${{ runner.os }}-${{ hashFiles('pnpm-lock.yaml') }}

    - name: Download build artifacts
      uses: actions/download-artifact@v6.0.0
      with:
        name: dist
        path: dist

    - name: Run Lighthouse CI
      run: pnpm lhci autorun" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<aside aria-label="What Lighthouse CI Catches" class="aside aside-tip astro-37uy2q7c"> <div class="aside-content astro-37uy2q7c"> <p class="aside-title astro-37uy2q7c"> <span class="aside-emoji astro-37uy2q7c" role="img" aria-hidden="true">💡</span> What Lighthouse CI Catches </p> <section class="aside-body astro-37uy2q7c"> <ul>
<li>Performance regressions (bundle size bloat, slow renders)</li>
<li>Accessibility violations (missing labels, low contrast)</li>
<li>SEO issues (missing meta tags, non-crawlable links)</li>
<li>Best practice violations (HTTP/2, image optimization)</li>
</ul><p>Configure thresholds in <code>lighthouserc.js</code> to fail the build when scores drop below acceptable levels.</p> </section> </div> </aside> 
<hr/>
<h2 id="beyond-the-pyramid-ai-powered-qa">Beyond the Pyramid: AI-Powered QA<a class="heading-link" aria-label="Link to section" href="#beyond-the-pyramid-ai-powered-qa"><span class="heading-link-icon">#</span></a></h2>
<p>There’s a new layer emerging that doesn’t fit neatly into the traditional pyramid: <strong>AI-driven testing</strong>.</p>
<figure class="max-w-4xl mx-auto "> <img src="/_astro/aiDrivenTesting.DRn6L0Mo_gChNG.webp" alt="AI-driven testing workflow showing Claude Code with Playwright testing an app and generating reports" loading="lazy" decoding="async" fetchpriority="auto" width="1024" height="559" class="w-full"> <figcaption class="mt-2 text-center text-sm text-gray-500"> AI QA: Claude Code + Playwright for intelligent exploratory testing </figcaption> </figure>
<p>What if you could have an AI test your app the way a real QA engineer would? Not following scripts, but actually exploring your UI, trying edge cases, and writing bug reports?</p>
<p>I’ve been experimenting with exactly this approach. Using Claude Code combined with Playwright’s browser automation, I built an AI QA engineer that:</p>
<ul>
<li>Tests my app through the browser like a real user</li>
<li>Tries unexpected inputs and edge cases automatically</li>
<li>Runs on every pull request via GitHub Actions</li>
<li>Posts detailed bug reports with screenshots directly to my PRs</li>
</ul>
<p><svg id="mermaid-0" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="flowchart" style="max-width:1207.296875px" viewBox="0 0 1207.296875 94" role="graphics-document document" aria-roledescription="flowchart-v2"><style>#mermaid-0{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-0 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-0 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-0 .error-icon{fill:#a44141;}#mermaid-0 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-0 .edge-thickness-normal{stroke-width:1px;}#mermaid-0 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-0 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-0 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-0 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-0 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-0 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-0 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-0 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-0 p{margin:0;}#mermaid-0 .label{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;color:#ccc;}#mermaid-0 .cluster-label text{fill:#F9FFFE;}#mermaid-0 .cluster-label span{color:#F9FFFE;}#mermaid-0 .cluster-label span p{background-color:transparent;}#mermaid-0 .label text,#mermaid-0 span{fill:#ccc;color:#ccc;}#mermaid-0 .node rect,#mermaid-0 .node circle,#mermaid-0 .node ellipse,#mermaid-0 .node polygon,#mermaid-0 .node path{fill:transparent;stroke:2px;stroke-width:1px;}#mermaid-0 .rough-node .label text,#mermaid-0 .node .label text,#mermaid-0 .image-shape .label,#mermaid-0 .icon-shape .label{text-anchor:middle;}#mermaid-0 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-0 .rough-node .label,#mermaid-0 .node .label,#mermaid-0 .image-shape .label,#mermaid-0 .icon-shape .label{text-align:center;}#mermaid-0 .node.clickable{cursor:pointer;}#mermaid-0 .root .anchor path{fill:rgb(171, 75, 153)!important;stroke-width:0;stroke:rgb(171, 75, 153);}#mermaid-0 .arrowheadPath{fill:lightgrey;}#mermaid-0 .edgePath .path{stroke:rgb(171, 75, 153);stroke-width:2.0px;}#mermaid-0 .flowchart-link{stroke:rgb(171, 75, 153);fill:none;}#mermaid-0 .edgeLabel{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-0 .edgeLabel p{background-color:hsla(0, 0%, 25%, 0);}#mermaid-0 .edgeLabel rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-0 .labelBkg{background-color:rgba(63.75, 63.75, 63.75, 0.5);}#mermaid-0 .cluster rect{fill:transparent;stroke:rgba(255, 255, 255, 0.25);stroke-width:1px;}#mermaid-0 .cluster text{fill:#F9FFFE;}#mermaid-0 .cluster span{color:#F9FFFE;}#mermaid-0 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:12px;background:rgb(138, 51, 123);border:1px solid rgba(255, 255, 255, 0.25);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-0 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-0 rect.text{fill:none;stroke-width:0;}#mermaid-0 .icon-shape,#mermaid-0 .image-shape{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-0 .icon-shape p,#mermaid-0 .image-shape p{background-color:hsla(0, 0%, 25%, 0);padding:2px;}#mermaid-0 .icon-shape rect,#mermaid-0 .image-shape rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-0 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-0 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-0 :root{--mermaid-font-family:arial,sans-serif;}</style><g><marker id="mermaid-0_flowchart-v2-pointEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-pointStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="4.5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 5 L 10 10 L 10 0 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-circleEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="11" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-0_flowchart-v2-circleStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="-1" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-0_flowchart-v2-crossEnd" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="12" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-crossStart" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="-1" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><g class="root"><g class="clusters"></g><g class="edgePaths"><path d="M135.438,47L139.604,47C143.771,47,152.104,47,159.771,47C167.438,47,174.438,47,177.938,47L181.438,47" id="L_PR_GH_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_PR_GH_0" data-points="W3sieCI6MTM1LjQzNzUsInkiOjQ3fSx7IngiOjE2MC40Mzc1LCJ5Ijo0N30seyJ4IjoxODUuNDM3NSwieSI6NDd9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M380.297,47L384.464,47C388.63,47,396.964,47,404.63,47C412.297,47,419.297,47,422.797,47L426.297,47" id="L_GH_AI_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_GH_AI_0" data-points="W3sieCI6MzgwLjI5Njg3NSwieSI6NDd9LHsieCI6NDA1LjI5Njg3NSwieSI6NDd9LHsieCI6NDMwLjI5Njg3NSwieSI6NDd9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M690.297,47L694.464,47C698.63,47,706.964,47,714.63,47C722.297,47,729.297,47,732.797,47L736.297,47" id="L_AI_Test_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_AI_Test_0" data-points="W3sieCI6NjkwLjI5Njg3NSwieSI6NDd9LHsieCI6NzE1LjI5Njg3NSwieSI6NDd9LHsieCI6NzQwLjI5Njg3NSwieSI6NDd9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M944.797,47L948.964,47C953.13,47,961.464,47,969.13,47C976.797,47,983.797,47,987.297,47L990.797,47" id="L_Test_Report_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Test_Report_0" data-points="W3sieCI6OTQ0Ljc5Njg3NSwieSI6NDd9LHsieCI6OTY5Ljc5Njg3NSwieSI6NDd9LHsieCI6OTk0Ljc5Njg3NSwieSI6NDd9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path></g><g class="edgeLabels"><g class="edgeLabel"><g class="label" data-id="L_PR_GH_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_GH_AI_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_AI_Test_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_Test_Report_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g></g><g class="nodes"><g class="node default" id="flowchart-PR-0" transform="translate(71.71875, 47)"><rect class="basic label-container" style="" x="-63.71875" y="-27" width="127.4375" height="54"></rect><g class="label" style="" transform="translate(-33.71875, -12)"><rect></rect><foreignObject width="67.4375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Open PR</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-GH-1" transform="translate(282.8671875, 47)"><rect class="basic label-container" style="" x="-97.4296875" y="-27" width="194.859375" height="54"></rect><g class="label" style="" transform="translate(-67.4296875, -12)"><rect></rect><foreignObject width="134.859375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>GitHub Actions</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-AI-3" transform="translate(560.296875, 47)"><rect class="basic label-container" style="" x="-130" y="-39" width="260" height="78"></rect><g class="label" style="" transform="translate(-100, -24)"><rect></rect><foreignObject width="200" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table;white-space:break-spaces;line-height:1.5;max-width:200px;text-align:center;width:200px"><span class="nodeLabel"><p>Claude Code + Playwright</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-Test-5" transform="translate(842.546875, 47)"><rect class="basic label-container" style="" x="-102.25" y="-27" width="204.5" height="54"></rect><g class="label" style="" transform="translate(-72.25, -12)"><rect></rect><foreignObject width="144.5" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Browser Testing</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-Report-7" transform="translate(1097.046875, 47)"><rect class="basic label-container" style="" x="-102.25" y="-27" width="204.5" height="54"></rect><g class="label" style="" transform="translate(-72.25, -12)"><rect></rect><foreignObject width="144.5" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>QA Report on PR</p></span></div></foreignObject></g></g></g></g></g></svg></p>
<p>This isn’t a replacement for the testing pyramid—it’s a complement. Your unit and integration tests catch regressions deterministically. AI QA excels at exploratory testing and finding bugs that scripted tests would never think to check.</p>
<aside aria-label="Want to Build Your Own AI QA Engineer?" class="aside aside-tip astro-37uy2q7c"> <div class="aside-content astro-37uy2q7c"> <p class="aside-title astro-37uy2q7c"> <span class="aside-emoji astro-37uy2q7c" role="img" aria-hidden="true">💡</span> Want to Build Your Own AI QA Engineer? </p> <section class="aside-body astro-37uy2q7c"> <p>I wrote a complete guide on setting this up: <span class="internal-link-wrapper astro-3tyn5ojg"> <a target="_blank" rel="noopener noreferrer" href="/posts/building_ai_qa_engineer_claude_code_playwright/" class="internal-link astro-3tyn5ojg"> Building an AI QA Engineer with Claude Code and Playwright MCP </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Building an AI QA Engineer with Claude Code and Playwright MCP</span> <span class="preview-description astro-3tyn5ojg">Learn how to build an automated QA engineer using Claude Code and Playwright MCP that tests your web app like a real user, runs on every pull request, and writes detailed bug reports.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">ai</span><span class="preview-tag astro-3tyn5ojg">testing</span><span class="preview-tag astro-3tyn5ojg">claude-code</span> <span class="preview-tag-more astro-3tyn5ojg">+1</span> </span> <time class="preview-date astro-3tyn5ojg">Dec 13, 2025</time> </span> </span> </span>  <script>
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
</script>. It covers the GitHub Actions workflow, prompt engineering for effective testing, and how to get bug reports posted automatically to your PRs.</p> </section> </div> </aside> 
<hr/>
<h2 id="additional-resources">Additional Resources<a class="heading-link" aria-label="Link to section" href="#additional-resources"><span class="heading-link-icon">#</span></a></h2>
<ul>
<li><a href="https://vitest.dev/guide/browser/" rel="noopener noreferrer" target="_blank">Vitest Browser Mode Guide</a> - The official docs are excellent</li>
<li><a href="https://github.com/vitest-dev/vitest-browser-vue" rel="noopener noreferrer" target="_blank">vitest-browser-vue</a> - Vue rendering for Vitest browser mode</li>
<li><a href="https://github.com/vitest-dev/vitest/tree/main/examples" rel="noopener noreferrer" target="_blank">vitest-examples on GitHub</a> - “Hello World” setup examples</li>
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
</li> <li class="astro-vj4tpspi">Small tips and trick</li> </ul> </div> <a href="https://alex-op-newsletter.beehiiv.com/subscribe?utm_source=blog&utm_medium=post&utm_campaign=post_vue3_testing_pyramid_vitest_browser_mode" target="_blank" rel="noopener noreferrer" id="newsletter-subscribe-button" class="inline-flex items-center justify-center gap-2 rounded-full bg-skin-accent px-6 py-3 text-base font-semibold text-skin-inverted shadow-md transition-all duration-200 hover:scale-[1.02] hover:transform hover:opacity-90 astro-vj4tpspi"> <svg class="h-5 w-5 fill-current astro-vj4tpspi" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg>
Subscribe Now
</a> <button id="newsletter-dismiss" data-post-slug="vue3_testing_pyramid_vitest_browser_mode" class="absolute right-3 top-3 rounded-full p-1 text-skin-base transition-all duration-200 hover:bg-skin-accent hover:bg-opacity-10 hover:text-skin-accent astro-vj4tpspi" aria-label="Close notification"> <svg class="h-5 w-5 astro-vj4tpspi" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class="astro-vj4tpspi"></path> </svg> </button> </div> </div> </div> <ul class="my-8 flex flex-wrap gap-2 astro-vj4tpspi"> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/vue/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-2"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">vue</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/testing/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-3"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">testing</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/vitest/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-4"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">vitest</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/typescript/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-5"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">typescript</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/accessibility/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-6"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">accessibility</span>   </a> </li>  </ul> <div class="flex flex-col-reverse items-center justify-between gap-6 sm:flex-row-reverse sm:items-end sm:gap-4 astro-vj4tpspi"> <button id="back-to-top" class="focus-outline whitespace-nowrap py-1 hover:opacity-75 astro-vj4tpspi"> <svg xmlns="http://www.w3.org/2000/svg" class="rotate-90 astro-vj4tpspi"> <path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg> <span class="astro-vj4tpspi">Back to Top</span> </button> <div class="social-icons astro-wkojbtzc"> <span class="italic astro-wkojbtzc">Share this post on:</span> <div class="text-center astro-wkojbtzc"> <a href="https://wa.me/?text=https://alexop.dev/posts/vue3_testing_pyramid_vitest_browser_mode/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via WhatsApp" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"></path>
      <path d="M9 10a0.5 .5 0 0 0 1 0v-1a0.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a0.5 .5 0 0 0 0 -1h-1a0.5 .5 0 0 0 0 1"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via WhatsApp</span> </a><a href="https://www.facebook.com/sharer.php?u=https://alexop.dev/posts/vue3_testing_pyramid_vitest_browser_mode/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Facebook" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"
    ></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on Facebook</span> </a><a href="https://x.com/intent/tweet?url=https://alexop.dev/posts/vue3_testing_pyramid_vitest_browser_mode/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Tweet this post" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Tweet this post</span> </a><a href="https://t.me/share/url?url=https://alexop.dev/posts/vue3_testing_pyramid_vitest_browser_mode/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via Telegram" target="_blank" rel="noopener noreferrer"> <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon-tabler"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"></path>
      </svg> <span class="sr-only astro-wkojbtzc">Share this post via Telegram</span> </a><a href="https://pinterest.com/pin/create/button/?url=https://alexop.dev/posts/vue3_testing_pyramid_vitest_browser_mode/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Pinterest" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <line x1="8" y1="20" x2="12" y2="11"></line>
      <path d="M10.7 14c.437 1.263 1.43 2 2.55 2c2.071 0 3.75 -1.554 3.75 -4a5 5 0 1 0 -9.7 1.7"></path>
      <circle cx="12" cy="12" r="9"></circle>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post on Pinterest</span> </a><a href="mailto:?subject=See%20this%20post&#38;body=https://alexop.dev/posts/vue3_testing_pyramid_vitest_browser_mode/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via email" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via email</span> </a><a href="https://www.linkedin.com/shareArticle?mini=true&url=https://alexop.dev/posts/vue3_testing_pyramid_vitest_browser_mode/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
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
    </script> </body> </html>  <script>(function(){const postSlug = "vue3_testing_pyramid_vitest_browser_mode";

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
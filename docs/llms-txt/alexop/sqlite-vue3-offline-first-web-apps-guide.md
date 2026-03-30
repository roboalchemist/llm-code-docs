# Source: https://alexop.dev/posts/sqlite-vue3-offline-first-web-apps-guide

<!DOCTYPE html><html lang="en" class="scroll-smooth astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/posts/sqlite-vue3-offline-first-web-apps-guide/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>SQLite in Vue: Complete Guide to Building Offline-First Web Apps | alexop.dev</title><meta name="title" content="SQLite in Vue: Complete Guide to Building Offline-First Web Apps | alexop.dev"><meta name="description" content="Learn how to build offline-capable Vue 3 apps using SQLite and WebAssembly in 2024. Step-by-step tutorial includes code examples for database operations, query playground implementation, and best practices for offline-first applications."><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="SQLite in Vue: Complete Guide to Building Offline-First Web Apps | alexop.dev"><meta property="og:description" content="Learn how to build offline-capable Vue 3 apps using SQLite and WebAssembly in 2024. Step-by-step tutorial includes code examples for database operations, query playground implementation, and best practices for offline-first applications."><meta property="og:url" content="https://alexop.dev/posts/sqlite-vue3-offline-first-web-apps-guide/"><meta property="og:image" content="https://alexop.dev/posts/sq-lite-in-vue-complete-guide-to-building-offline-first-web-apps/index.png"><meta property="og:type" content="article"><!-- Article Published/Modified time --><meta property="article:published_time" content="2024-11-25T07:44:12.000Z"><meta property="article:modified_time" content="2024-11-25T07:44:12.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/posts/sqlite-vue3-offline-first-web-apps-guide/"><meta property="twitter:title" content="SQLite in Vue: Complete Guide to Building Offline-First Web Apps | alexop.dev"><meta property="twitter:description" content="Learn how to build offline-capable Vue 3 apps using SQLite and WebAssembly in 2024. Step-by-step tutorial includes code examples for database operations, query playground implementation, and best practices for offline-first applications."><meta property="twitter:image" content="https://alexop.dev/posts/sq-lite-in-vue-complete-guide-to-building-offline-first-web-apps/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"SQLite in Vue: Complete Guide to Building Offline-First Web Apps | alexop.dev","description":"Learn how to build offline-capable Vue 3 apps using SQLite and WebAssembly in 2024. Step-by-step tutorial includes code examples for database operations, query playground implementation, and best practices for offline-first applications.","image":"https://alexop.dev/posts/sq-lite-in-vue-complete-guide-to-building-offline-first-web-apps/index.png","datePublished":"2024-11-25T07:44:12.000Z","dateModified":"2024-11-25T07:44:12.000Z","author":{"@type":"Person","name":"Alexander Opalic"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
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
</style><style>[data-astro-transition-scope="astro-plk3gbjq-1"] { view-transition-name: sq-lite-in-vue-complete-guide-to-building-offline-first-web-apps; }@layer astro { ::view-transition-old(sq-lite-in-vue-complete-guide-to-building-offline-first-web-apps) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(sq-lite-in-vue-complete-guide-to-building-offline-first-web-apps) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(sq-lite-in-vue-complete-guide-to-building-offline-first-web-apps) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(sq-lite-in-vue-complete-guide-to-building-offline-first-web-apps) { 
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
	animation-name: astroFadeIn; }</style><style>.excalidraw-figure:where(.astro-hxyrieg5){margin-top:2rem;margin-bottom:2rem;width:100%;max-width:100%}.excalidraw-svg:where(.astro-hxyrieg5){width:100%;--excalidraw-text: rgb(var(--color-text-base));--excalidraw-fill: rgb(var(--color-card));--excalidraw-accent: rgb(var(--color-accent))}.excalidraw-svg svg.excalidraw-rendered{display:block;height:auto;width:100%}figcaption:where(.astro-hxyrieg5){margin-top:1rem;text-align:center;font-size:.875rem;line-height:1.25rem;font-style:italic;--tw-text-opacity: 1;color:rgba(var(--color-text-base),var(--tw-text-opacity, 1))}figcaption:where(.astro-hxyrieg5) a:where(.astro-hxyrieg5){--tw-text-opacity: 1;color:rgba(var(--color-accent),var(--tw-text-opacity, 1));transition-property:opacity;transition-timing-function:cubic-bezier(.4,0,.2,1);transition-duration:.2s}figcaption:where(.astro-hxyrieg5) a:where(.astro-hxyrieg5):hover{opacity:.8}figcaption:where(.astro-hxyrieg5) a:where(.astro-hxyrieg5){text-decoration:underline}
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-3"] { view-transition-name: local-first; }@layer astro { ::view-transition-old(local-first) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(local-first) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(local-first) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(local-first) { 
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <div class="mx-auto flex w-full max-w-5xl justify-start px-2 astro-vj4tpspi"> <button class="focus-outline mb-2 mt-8 flex hover:opacity-75 astro-vj4tpspi" onclick="(() => (history.length === 1) ? window.location = '/' : history.back())()"> <svg xmlns="http://www.w3.org/2000/svg" class="astro-vj4tpspi"><path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg><span class="astro-vj4tpspi">Go back</span> </button> </div> <main data-pagefind-body id="main-content" class="relative astro-vj4tpspi"> <h1 class="post-title astro-vj4tpspi" data-astro-transition-scope="astro-plk3gbjq-1">SQLite in Vue: Complete Guide to Building Offline-First Web Apps</h1> <div class="my-2 flex items-center justify-between astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-100 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-base"><time dateTime="2024-11-25T07:44:12.000Z">Nov 25, 2024</time><span class="sr-only"> at </span></span></div> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="2i0zUj" prefix="r6" component-url="/_astro/PostCopyButton.-PGtk4At.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;title&quot;:[0,&quot;SQLite in Vue: Complete Guide to Building Offline-First Web Apps&quot;],&quot;content&quot;:[0,&quot;import ExcalidrawSVG from \&quot;@features/mdx-components/components/ExcalidrawSVG.astro\&quot;;\nimport myDiagram from \&quot;../../assets/images/sqlite-vue/sqlite-vue2.svg?raw\&quot;;\n\n## TLDR\n\n- Set up SQLite WASM in a Vue 3 application for offline data storage\n- Learn how to use Origin Private File System (OPFS) for persistent storage\n- Build a SQLite query playground with Vue composables\n- Implement production-ready offline-first architecture\n- Compare SQLite vs IndexedDB for web applications\n\nLooking to add offline capabilities to your Vue application? While browsers offer IndexedDB, SQLite provides a more powerful solution for complex data operations. This comprehensive guide shows you how to integrate SQLite with Vue using WebAssembly for robust offline-first applications.\n\n## 📚 What We&#39;ll Build\n\n- A Vue 3 app with SQLite that works offline\n- A simple query playground to test SQLite\n- Everything runs in the browser - no server needed!\n\n![Screenshot Sqlite Playground](../../assets/images/sqlite-vue/sqlite-playground.png)\n_Try it out: Write and run SQL queries right in your browser_\n\n&gt; 🚀 **Want the code?** Get the complete example at [github.com/alexanderop/sqlite-vue-example](https://github.com/alexanderop/sqlite-vue-example)\n\n## 🗃️ Why SQLite?\n\nBrowser storage like IndexedDB is okay, but SQLite is better because:\n\n- It&#39;s a real SQL database in your browser\n- Your data stays safe even when offline\n- You can use normal SQL queries\n- It handles complex data relationships well\n\n## 🛠️ How It Works\n\nWe&#39;ll use three main technologies:\n\n1. **SQLite Wasm**: SQLite converted to run in browsers\n2. **Web Workers**: Runs database code without freezing your app\n3. **Origin Private File System**: A secure place to store your database\n\nHere&#39;s how they work together:\n\n&lt;ExcalidrawSVG\n  src={myDiagram}\n  alt=\&quot;How SQLite works in the browser\&quot;\n  caption=\&quot;How SQLite runs in your browser\&quot;\n/&gt;\n\n## 📝 Implementation Guide\n\nLet&#39;s build this step by step, starting with the core SQLite functionality and then creating a playground to test it.\n\n### Step 1: Install Dependencies\n\nFirst, install the required SQLite WASM package:\n\n```bash\nnpm install @sqlite.org/sqlite-wasm\n```\n\n### Step 2: Configure Vite\n\nCreate or update your `vite.config.ts` file to support WebAssembly and cross-origin isolation:\n\n```ts\nimport { defineConfig } from \&quot;vite\&quot;;\n\nexport default defineConfig(() =&gt; ({\n  server: {\n    headers: {\n      \&quot;Cross-Origin-Opener-Policy\&quot;: \&quot;same-origin\&quot;,\n      \&quot;Cross-Origin-Embedder-Policy\&quot;: \&quot;require-corp\&quot;,\n    },\n  },\n  optimizeDeps: {\n    exclude: [\&quot;@sqlite.org/sqlite-wasm\&quot;],\n  },\n}));\n```\n\nThis configuration is crucial for SQLite WASM to work properly:\n\n- **Cross-Origin Headers**:\n  - `Cross-Origin-Opener-Policy` and `Cross-Origin-Embedder-Policy` headers enable \&quot;cross-origin isolation\&quot;\n  - This is required for using SharedArrayBuffer, which SQLite WASM needs for optimal performance\n  - Without these headers, the WebAssembly implementation might fail or perform poorly\n\n- **Dependency Optimization**:\n  - `optimizeDeps.exclude` tells Vite not to pre-bundle the SQLite WASM package\n  - This is necessary because the WASM files need to be loaded dynamically at runtime\n  - Pre-bundling would break the WASM initialization process\n\n### Step 3: Add TypeScript Types\n\nSince `@sqlite.org/sqlite-wasm` doesn&#39;t include TypeScript types for Sqlite3Worker1PromiserConfig, we need to create our own. Create a new file `types/sqlite-wasm.d.ts`:\n\nDefine this as a d.ts file so that TypeScript knows about it.\n\n```ts\nimport type { Worker } from \&quot;node:worker_threads\&quot;;\n\ndeclare module \&quot;@sqlite.org/sqlite-wasm\&quot; {\n  type OnreadyFunction = () =&gt; void;\n\n  type Sqlite3Worker1PromiserConfig = {\n    onready?: OnreadyFunction;\n    worker?: Worker | (() =&gt; Worker);\n    generateMessageId?: (messageObject: unknown) =&gt; string;\n    debug?: (...args: any[]) =&gt; void;\n    onunhandled?: (event: MessageEvent) =&gt; void;\n  };\n\n  type DbId = string | undefined;\n\n  type PromiserMethods = {\n    \&quot;config-get\&quot;: {\n      args: Record&lt;string, never&gt;;\n      result: {\n        dbID: DbId;\n        version: {\n          libVersion: string;\n          sourceId: string;\n          libVersionNumber: number;\n          downloadVersion: number;\n        };\n        bigIntEnabled: boolean;\n        opfsEnabled: boolean;\n        vfsList: string[];\n      };\n    };\n    open: {\n      args: Partial&lt;{\n        filename?: string;\n        vfs?: string;\n      }&gt;;\n      result: {\n        dbId: DbId;\n        filename: string;\n        persistent: boolean;\n        vfs: string;\n      };\n    };\n    exec: {\n      args: {\n        sql: string;\n        dbId?: DbId;\n        bind?: unknown[];\n        returnValue?: string;\n      };\n      result: {\n        dbId: DbId;\n        sql: string;\n        bind: unknown[];\n        returnValue: string;\n        resultRows?: unknown[][];\n      };\n    };\n  };\n\n  type PromiserResponseSuccess&lt;T extends keyof PromiserMethods&gt; = {\n    type: T;\n    result: PromiserMethods[T][\&quot;result\&quot;];\n    messageId: string;\n    dbId: DbId;\n    workerReceivedTime: number;\n    workerRespondTime: number;\n    departureTime: number;\n  };\n\n  type PromiserResponseError = {\n    type: \&quot;error\&quot;;\n    result: {\n      operation: string;\n      message: string;\n      errorClass: string;\n      input: object;\n      stack: unknown[];\n    };\n    messageId: string;\n    dbId: DbId;\n  };\n\n  type PromiserResponse&lt;T extends keyof PromiserMethods&gt; =\n    | PromiserResponseSuccess&lt;T&gt;\n    | PromiserResponseError;\n\n  type Promiser = &lt;T extends keyof PromiserMethods&gt;(\n    messageType: T,\n    messageArguments: PromiserMethods[T][\&quot;args\&quot;]\n  ) =&gt; Promise&lt;PromiserResponse&lt;T&gt;&gt;;\n\n  export function sqlite3Worker1Promiser(\n    config?: Sqlite3Worker1PromiserConfig | OnreadyFunction\n  ): Promiser;\n}\n```\n\n### Step 4: Create the SQLite Composable\n\nThe core of our implementation is the `useSQLite` composable. This will handle all database operations:\n\n```ts\nimport type { DbId } from \&quot;@sqlite.org/sqlite-wasm\&quot;;\nimport { sqlite3Worker1Promiser } from \&quot;@sqlite.org/sqlite-wasm\&quot;;\nimport { ref } from \&quot;vue\&quot;;\n\nconst databaseConfig = {\n  filename: \&quot;file:mydb.sqlite3?vfs=opfs\&quot;,\n  tables: {\n    test: {\n      name: \&quot;test_table\&quot;,\n      schema: `\n        CREATE TABLE IF NOT EXISTS test_table (\n          id INTEGER PRIMARY KEY AUTOINCREMENT,\n          name TEXT NOT NULL,\n          created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP\n        );\n      `,\n    },\n  },\n} as const;\n\nexport function useSQLite() {\n  const isLoading = ref(false);\n  const error = ref&lt;Error | null&gt;(null);\n  const isInitialized = ref(false);\n\n  let promiser: ReturnType&lt;typeof sqlite3Worker1Promiser&gt; | null = null;\n  let dbId: string | null = null;\n\n  async function initialize() {\n    if (isInitialized.value) return true;\n\n    isLoading.value = true;\n    error.value = null;\n\n    try {\n      // Initialize the SQLite worker\n      promiser = await new Promise(resolve =&gt; {\n        const _promiser = sqlite3Worker1Promiser({\n          onready: () =&gt; resolve(_promiser),\n        });\n      });\n\n      if (!promiser) throw new Error(\&quot;Failed to initialize promiser\&quot;);\n\n      // Get configuration and open database\n      await promiser(\&quot;config-get\&quot;, {});\n      const openResponse = await promiser(\&quot;open\&quot;, {\n        filename: databaseConfig.filename,\n      });\n\n      if (openResponse.type === \&quot;error\&quot;) {\n        throw new Error(openResponse.result.message);\n      }\n\n      dbId = openResponse.result.dbId as string;\n\n      // Create initial tables\n      await promiser(\&quot;exec\&quot;, {\n        dbId,\n        sql: databaseConfig.tables.test.schema,\n      });\n\n      isInitialized.value = true;\n      return true;\n    } catch (err) {\n      error.value = err instanceof Error ? err : new Error(\&quot;Unknown error\&quot;);\n      throw error.value;\n    } finally {\n      isLoading.value = false;\n    }\n  }\n\n  async function executeQuery(sql: string, params: unknown[] = []) {\n    if (!dbId || !promiser) {\n      await initialize();\n    }\n\n    isLoading.value = true;\n    error.value = null;\n\n    try {\n      const result = await promiser!(\&quot;exec\&quot;, {\n        dbId: dbId as DbId,\n        sql,\n        bind: params,\n        returnValue: \&quot;resultRows\&quot;,\n      });\n\n      if (result.type === \&quot;error\&quot;) {\n        throw new Error(result.result.message);\n      }\n\n      return result;\n    } catch (err) {\n      error.value =\n        err instanceof Error ? err : new Error(\&quot;Query execution failed\&quot;);\n      throw error.value;\n    } finally {\n      isLoading.value = false;\n    }\n  }\n\n  return {\n    isLoading,\n    error,\n    isInitialized,\n    executeQuery,\n  };\n}\n```\n\n### Step 5: Create a SQLite Playground Component\n\nNow let&#39;s create a component to test our SQLite implementation:\n\n```vue\n&lt;script setup lang=\&quot;ts\&quot;&gt;\nimport { useSQLite } from \&quot;@/composables/useSQLite\&quot;;\nimport { ref } from \&quot;vue\&quot;;\n\nconst { isLoading, error, executeQuery } = useSQLite();\nconst sqlQuery = ref(\&quot;SELECT * FROM test_table\&quot;);\nconst queryResult = ref&lt;any[]&gt;([]);\nconst queryError = ref&lt;string | null&gt;(null);\n\n// Predefined example queries for testing\nconst exampleQueries = [\n  { title: \&quot;Select all\&quot;, query: \&quot;SELECT * FROM test_table\&quot; },\n  {\n    title: \&quot;Insert\&quot;,\n    query: \&quot;INSERT INTO test_table (name) VALUES (&#39;New Test Item&#39;)\&quot;,\n  },\n  {\n    title: \&quot;Update\&quot;,\n    query: \&quot;UPDATE test_table SET name = &#39;Updated Item&#39; WHERE name LIKE &#39;New%&#39;\&quot;,\n  },\n  {\n    title: \&quot;Delete\&quot;,\n    query: \&quot;DELETE FROM test_table WHERE name = &#39;Updated Item&#39;\&quot;,\n  },\n];\n\nasync function runQuery() {\n  queryError.value = null;\n  queryResult.value = [];\n\n  try {\n    const result = await executeQuery(sqlQuery.value);\n    const isSelect = sqlQuery.value.trim().toLowerCase().startsWith(\&quot;select\&quot;);\n\n    if (isSelect) {\n      queryResult.value = result?.result.resultRows || [];\n    } else {\n      // After mutation, fetch updated data\n      queryResult.value =\n        (await executeQuery(\&quot;SELECT * FROM test_table\&quot;))?.result.resultRows ||\n        [];\n    }\n  } catch (err) {\n    queryError.value = err instanceof Error ? err.message : \&quot;An error occurred\&quot;;\n  }\n}\n&lt;/script&gt;\n\n&lt;template&gt;\n  &lt;div class=\&quot;mx-auto max-w-7xl px-4 py-6\&quot;&gt;\n    &lt;h2 class=\&quot;text-2xl font-bold\&quot;&gt;SQLite Playground&lt;/h2&gt;\n\n    &lt;!-- Example queries --&gt;\n    &lt;div class=\&quot;mt-4\&quot;&gt;\n      &lt;h3 class=\&quot;text-sm font-medium\&quot;&gt;Example Queries:&lt;/h3&gt;\n      &lt;div class=\&quot;mt-2 flex gap-2\&quot;&gt;\n        &lt;button\n          v-for=\&quot;example in exampleQueries\&quot;\n          :key=\&quot;example.title\&quot;\n          class=\&quot;rounded-full bg-gray-100 px-3 py-1 text-sm hover:bg-gray-200\&quot;\n          @click=\&quot;sqlQuery = example.query\&quot;\n        &gt;\n          {{ example.title }}\n        &lt;/button&gt;\n      &lt;/div&gt;\n    &lt;/div&gt;\n\n    &lt;!-- Query input --&gt;\n    &lt;div class=\&quot;mt-6\&quot;&gt;\n      &lt;textarea\n        v-model=\&quot;sqlQuery\&quot;\n        rows=\&quot;4\&quot;\n        class=\&quot;w-full rounded-lg px-4 py-3 font-mono text-sm\&quot;\n        :disabled=\&quot;isLoading\&quot;\n      /&gt;\n      &lt;button\n        :disabled=\&quot;isLoading\&quot;\n        class=\&quot;mt-2 rounded-lg bg-blue-600 px-4 py-2 text-white\&quot;\n        @click=\&quot;runQuery\&quot;\n      &gt;\n        {{ isLoading ? \&quot;Running...\&quot; : \&quot;Run Query\&quot; }}\n      &lt;/button&gt;\n    &lt;/div&gt;\n\n    &lt;!-- Error display --&gt;\n    &lt;div\n      v-if=\&quot;error || queryError\&quot;\n      class=\&quot;mt-4 rounded-lg bg-red-50 p-4 text-red-600\&quot;\n    &gt;\n      {{ error?.message || queryError }}\n    &lt;/div&gt;\n\n    &lt;!-- Results table --&gt;\n    &lt;div v-if=\&quot;queryResult.length\&quot; class=\&quot;mt-4\&quot;&gt;\n      &lt;h3 class=\&quot;text-lg font-semibold\&quot;&gt;Results:&lt;/h3&gt;\n      &lt;div class=\&quot;mt-2 overflow-x-auto\&quot;&gt;\n        &lt;table class=\&quot;w-full\&quot;&gt;\n          &lt;thead&gt;\n            &lt;tr&gt;\n              &lt;th\n                v-for=\&quot;column in Object.keys(queryResult[0])\&quot;\n                :key=\&quot;column\&quot;\n                class=\&quot;px-4 py-2 text-left\&quot;\n              &gt;\n                {{ column }}\n              &lt;/th&gt;\n            &lt;/tr&gt;\n          &lt;/thead&gt;\n          &lt;tbody&gt;\n            &lt;tr v-for=\&quot;(row, index) in queryResult\&quot; :key=\&quot;index\&quot;&gt;\n              &lt;td\n                v-for=\&quot;column in Object.keys(row)\&quot;\n                :key=\&quot;column\&quot;\n                class=\&quot;px-4 py-2\&quot;\n              &gt;\n                {{ row[column] }}\n              &lt;/td&gt;\n            &lt;/tr&gt;\n          &lt;/tbody&gt;\n        &lt;/table&gt;\n      &lt;/div&gt;\n    &lt;/div&gt;\n  &lt;/div&gt;\n&lt;/template&gt;\n```\n\n## 🎯 Real-World Example: Notion&#39;s SQLite Implementation\n\n[Notion recently shared](https://www.notion.com/blog/how-we-sped-up-notion-in-the-browser-with-wasm-sqlite) how they implemented SQLite in their web application, providing some valuable insights:\n\n### Performance Improvements\n\n- 20% faster page navigation across all modern browsers\n- Even greater improvements for users with slower connections:\n\n### Multi-Tab Architecture\n\nNotion solved the challenge of handling multiple browser tabs with an innovative approach:\n\n1. Each tab has its own Web Worker for SQLite operations\n2. A SharedWorker manages which tab is \&quot;active\&quot;\n3. Only one tab can write to SQLite at a time\n4. Queries from all tabs are routed through the active tab&#39;s Worker\n\n### Key Learnings from Notion\n\n1. **Async Loading**: They load the WASM SQLite library asynchronously to avoid blocking initial page load\n2. **Race Conditions**: They implemented a \&quot;racing\&quot; system between SQLite and API requests to handle slower devices\n3. **OPFS Handling**: They discovered that Origin Private File System (OPFS) doesn&#39;t handle concurrency well out of the box\n4. **Cross-Origin Isolation**: They opted for OPFS SyncAccessHandle Pool VFS to avoid cross-origin isolation requirements\n\nThis real-world implementation demonstrates both the potential and challenges of using SQLite in production web applications. Notion&#39;s success shows that with careful architecture choices, SQLite can significantly improve web application performance.\n\n## 🎯 Conclusion\n\nYou now have a solid foundation for building offline-capable Vue applications using SQLite. This approach offers significant advantages over traditional browser storage solutions, especially for complex data requirements.&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PostCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus-outline inline-flex items-center gap-1.5 rounded-md border border-skin-line bg-skin-card px-2.5 py-1.5 text-xs font-medium text-skin-base opacity-80 transition-all hover:border-skin-accent/50 hover:text-skin-accent hover:opacity-100" aria-label="Copy post as markdown" title="Copy post as markdown for AI/LLM"><svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg><span>Copy Post</span></button><!--astro:end--></astro-island> </div> <nav class="mb-8 astro-sbmhws2g" aria-labelledby="series-heading"> <div class="mb-1 text-sm font-bold tracking-wide text-skin-accent astro-sbmhws2g"> Local-First Web Development Series </div> <h2 id="series-heading" class="mb-2 text-xs font-semibold uppercase tracking-widest text-skin-accent astro-sbmhws2g">
This post is part of a series
</h2> <ol class="space-y-2 astro-sbmhws2g"> <li class="ml-4 text-xs text-skin-base/50 astro-sbmhws2g" aria-hidden="true">
…
</li> <li class="relative flex flex-col rounded py-2 pl-4 transition-all   astro-sbmhws2g"> <div class="flex items-center gap-2 astro-sbmhws2g"> <span class="font-mono text-xs text-skin-base/60 astro-sbmhws2g"> 2.
</span> <a href="/posts/create-pwa-vue3-vite-4-steps/" class="font-medium underline-offset-4 text-skin-accent/80 hover:underline astro-sbmhws2g"> Create a Native-Like App in 4 Steps: PWA Magic with Vue 3 and Vite </a>  </div> <div class="ml-6 mt-1 text-xs text-skin-base/70 astro-sbmhws2g"> Transform your Vue 3 project into a powerful Progressive Web App in just 4 steps. Learn how to create offline-capable, installable web apps using Vite and modern PWA techniques. </div> </li><li class="relative flex flex-col rounded py-2 pl-4 transition-all border-l-4 border-skin-accent bg-skin-card/60  astro-sbmhws2g"> <div class="flex items-center gap-2 astro-sbmhws2g"> <span class="font-mono text-xs text-skin-accent astro-sbmhws2g"> 3.
</span> <a href="/posts/sqlite-vue3-offline-first-web-apps-guide/" class="font-medium underline-offset-4 pointer-events-none text-skin-accent astro-sbmhws2g" aria-current="page"> SQLite in Vue: Complete Guide to Building Offline-First Web Apps </a> <span class="ml-2 text-xs font-bold text-green-400 astro-sbmhws2g">
(current)
</span> </div> <div class="ml-6 mt-1 text-xs text-skin-base/70 astro-sbmhws2g"> Learn how to build offline-capable Vue 3 apps using SQLite and WebAssembly in 2024. Step-by-step tutorial includes code examples for database operations, query playground implementation, and best practices for offline-first applications. </div> </li><li class="relative flex flex-col rounded py-2 pl-4 transition-all   astro-sbmhws2g"> <div class="flex items-center gap-2 astro-sbmhws2g"> <span class="font-mono text-xs text-skin-base/60 astro-sbmhws2g"> 4.
</span> <a href="/posts/building-local-first-apps-vue-dexie/" class="font-medium underline-offset-4 text-skin-accent/80 hover:underline astro-sbmhws2g"> Building Local-First Apps with Vue and Dexie.js </a>  </div> <div class="ml-6 mt-1 text-xs text-skin-base/70 astro-sbmhws2g"> Learn how to create offline-capable, local-first applications using Vue 3 and Dexie.js. Discover patterns for data persistence, synchronization, and optimal user experience. </div> </li><li class="relative flex flex-col rounded py-2 pl-4 transition-all   astro-sbmhws2g"> <div class="flex items-center gap-2 astro-sbmhws2g"> <span class="font-mono text-xs text-skin-base/60 astro-sbmhws2g"> 5.
</span> <a href="/posts/building-real-time-todo-app-jazz-vue/" class="font-medium underline-offset-4 text-skin-accent/80 hover:underline astro-sbmhws2g"> Building a Real-Time Todo App with Jazz and Vue 3 </a>  </div> <div class="ml-6 mt-1 text-xs text-skin-base/70 astro-sbmhws2g"> Build a real-time, offline-capable todo app with Jazz and Vue 3. Learn CoValues, drag-and-drop with fractional indexing, and shareable URLs — no backend needed. </div> </li> <li class="ml-4 text-xs text-skin-base/50 astro-sbmhws2g" aria-hidden="true">
…
</li> </ol> <div class="mt-4 border-b border-skin-line opacity-40 astro-sbmhws2g"></div> </nav>  <article id="article" class="prose mx-auto mt-8 max-w-5xl astro-vj4tpspi"> <h2 id="tldr">TLDR<a class="heading-link" aria-label="Link to section" href="#tldr"><span class="heading-link-icon">#</span></a></h2>
<ul>
<li>Set up SQLite WASM in a Vue 3 application for offline data storage</li>
<li>Learn how to use Origin Private File System (OPFS) for persistent storage</li>
<li>Build a SQLite query playground with Vue composables</li>
<li>Implement production-ready offline-first architecture</li>
<li>Compare SQLite vs IndexedDB for web applications</li>
</ul>
<p>Looking to add offline capabilities to your Vue application? While browsers offer IndexedDB, SQLite provides a more powerful solution for complex data operations. This comprehensive guide shows you how to integrate SQLite with Vue using WebAssembly for robust offline-first applications.</p>
<h2 id="-what-well-build">📚 What We’ll Build<a class="heading-link" aria-label="Link to section" href="#-what-well-build"><span class="heading-link-icon">#</span></a></h2>
<ul>
<li>A Vue 3 app with SQLite that works offline</li>
<li>A simple query playground to test SQLite</li>
<li>Everything runs in the browser - no server needed!</li>
</ul>
<p><img src="/_astro/sqlite-playground.kM4zIFQD_ZiO2xP.webp" alt="Screenshot Sqlite Playground" loading="lazy" decoding="async" fetchpriority="auto" width="2582" height="1322">
<em>Try it out: Write and run SQL queries right in your browser</em></p>
<blockquote>
<p>🚀 <strong>Want the code?</strong> Get the complete example at <a href="https://github.com/alexanderop/sqlite-vue-example" rel="noopener noreferrer" target="_blank">github.com/alexanderop/sqlite-vue-example</a></p>
</blockquote>
<h2 id="️-why-sqlite">🗃️ Why SQLite?<a class="heading-link" aria-label="Link to section" href="#️-why-sqlite"><span class="heading-link-icon">#</span></a></h2>
<p>Browser storage like IndexedDB is okay, but SQLite is better because:</p>
<ul>
<li>It’s a real SQL database in your browser</li>
<li>Your data stays safe even when offline</li>
<li>You can use normal SQL queries</li>
<li>It handles complex data relationships well</li>
</ul>
<h2 id="️-how-it-works">🛠️ How It Works<a class="heading-link" aria-label="Link to section" href="#️-how-it-works"><span class="heading-link-icon">#</span></a></h2>
<p>We’ll use three main technologies:</p>
<ol>
<li><strong>SQLite Wasm</strong>: SQLite converted to run in browsers</li>
<li><strong>Web Workers</strong>: Runs database code without freezing your app</li>
<li><strong>Origin Private File System</strong>: A secure place to store your database</li>
</ol>
<p>Here’s how they work together:</p>
<figure class="excalidraw-figure astro-hxyrieg5"> <div class="excalidraw-svg astro-hxyrieg5" role="img" aria-label="How SQLite works in the browser"><svg version="1.1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 298.166015625 510.1531066894531" width="100%" class="excalidraw-rendered" preserveAspectRatio="xMidYMid meet">
  <!-- svg-source:excalidraw -->
  
  <defs>
    <style class="style-fonts">
      @font-face { font-family: Excalifont; src: url(data:font/woff2;base64,d09GMgABAAAAABXcAA4AAAAAJQQAABWGAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGhYbhzgcNAZgAIEsEQgKuASpUgtEAAE2AiQDgQQEIAWDGAcgG50co6KOsloqyP4iwXaG3gDE6nIHGg+gBfmISRGERZi+suP7DU/b/Hd3cJQgbRRtI2lPibYwMBorMWpR/8+5tXNRqatwGa4q+Ye62Nu/e6YHfBDYTZoEQQlHFGsCUZZMV81wRa2hxlyuyd09wRGPtyjVKel/AP/+UzqrpLtMussaZGtgwbjAs3tAYDiI5i7+7CuXsq9W2iCwNbACw8CCB5bhuaVOgq/3/9uv5Vmvu0BIMImkoeCVkCll35lBLg9v6xUxST8j1giRSjJrYnHFIrSlZUrfTq2URgmoVFsjmAQtdlq6ri/mAQgATgA8MEiDM48fBAAiiRiYiyE+DbjfOxprgPujsbQauL/szXXAHQYAoN+Y/yxtrAN4AHyhvwFrQCcv3F7RLGTvJTqGeGuvAwmqfm58l3+47qEwC7BW3A75dz1iaGpGh7Xk2Ynt+Tc/F5riRM+W16efRNj43/X01PHGVOnXF4O3YKWuCtA6khAWBAYWDgGREzIKZ1Q0dEwsLty48+DTYgATINMIoG4Y7AVdAMDbXgwEhbw0eH9pBucZiDMmtRr28gVAwIDTfvjwCOGDopnkvyAzJS4KKka6zebJyCryJjS1W/W8tzRoKix843sBAOLoKNANyPyE2pBrdacxEfTj6JitfwnsZRzUygFg0Vv89meYAw+kBEzLEDkxZoPHMaa3eZ+GjoFZglQZipWqVMOhRZuOOBJvVReOl8TGXlCtTuN3+N8DB/U74JYbrrvmkm0bpibGRvIg6If+AKzNXKEpGwQQTgCI3xAeKEtGekx9MMMG6Ku+rNZN9g/XlaVhM7TeCcVRJV7+EdwweX1yWnSDnClyUfoz3T3jhVo37wBn5ZETl2Su1e8E8ROIX0RulRsokbXEIMigN28C+hIQPT7ZfxCdFGr76lXbXUHTJvbGVoeu+mBtVWrM9FLGGGQU0DcooIXGhoEP6B/eXr6X5xgf1nsQlWBDAsqWSY+UKMsmaL2Zm96nX5pxzy1LtShwwyCEcM5RpuuuwMUiLR4VRbvAmuxQCguv6F+SHWl5/iS/sW2Xyh6XDXKOFtABxVsseWmKn0Rv3+htlecfq2A3OREeFfme2Uxhs5mbiCC+FZa6HqsFPsUIleFWNTI9CFNY/LtFp6hQf+SP6D7dBw99ee6TT/rKxB0s9Gpc3n6vlMFgUFgFi1xgOQB0J4jrXH/1RPz1nrrwwli+Z3rQu2UxH1CEOCpBZwYFQHPmPfgpM/fUBZX26ukQUAkSWSP7wGgAWdTWarQ7O3G4n+NI2arGDTIzqEFQtsDvNPO6mWMxxTk0RS4Eg2a6adEkoZQQg9QIqFGDUG0g5+iqX3EYVBMvZSmDzAdJh4Bz1Ji1jEbycJmUQF7LaXZ/cf2kshVluy5HK3jP9CqysCoB9YeALaWm11Q3JlKWQpYypml+7S80Q9nWOgrLKi+rLgoN/5IEo3PXe3zrCjojIUEppYRykJ0J7enHQm0rO1J2ZHowHVcYg7DrQKHw1T6PpthLIWRjyAoYOJWC7B5koz9J2StNRd+buaqzov4s6Dqb2pzTkX5HytvL9/D0xj8f2Kq2Vb61a5B36EhLkn3rJqA+9SE7GNwat8fd63qyZlzsZWhih3emMyGrMzM1C5pMZQHzwcYb+7I2O/+wQQH1A2v1OKPUBzd/z1VT5CLPsXARn2QZ2i0bJKOADgCVFdP7P0GPFf6nyg0jewlkijT49edoUi7G6uh/TSxe/XrP9OoFC/jScoJNWHhOQMEfHvayCwvQOvWIx3Z0NG+ze1CICF/tlc9dg7Ro4AMqQYfOyU3xJej6R5PyyD8U2mGExdKtJe/J3l5zeqXxXMJ0dNiQBZokK+Bwzr+JZtX1nlLYF9Mc4yt29KI+ho+aHlxiZkFWbGrMr9LJBMlMAm0M06IOIfS09rjiDH1A/5TK0HU9nOK9Nmtf+9QrVPNONSxRqd3JkfBw9LY3nymm+Y38BRYvTun8/E0W+NpGg2QGTxKQSCAbWnCtgAUvzw3kuacfcr7c3u7FynYVFlGERQ7ZpkUvDbLxdH+tsnmrnpoeFnt5raY5Iol7OTOqurEevr3XnrvN+DXHcuQxGulr7oIuJ7tVvhCWC3FJs8ItFNvbdYbuACbvs0BxFStTrRznOzCwqEZvgs5AWs5Ao4B2kyOI69iOe+5CrPMFPbpTF8dfYQeHlQBChrE4qfKRHeGe4MMzTRtoWmAKe/vk1cWL/bNnkWe7AtvC9Oqs4sDBsUvWRke6VG7ctfwWbXCUHUGTQ1WXg86oRWnSTcojnIc8dPGKuvO2wHdMr8tSBmAKWVRnb0JIKUjOc8FdCIU96fe85ovdg7K70vWm9+XGsdHx8fJDlSrL/UgdFkJgYXrzA2lJTi88SXtf7hRzwaVRS0rVo/uNzCDfUAopcxh+AfgoS2ZkF5XHrf7Kg/fvqKX82rgdBJYPSMJRjPgumP3rmDMIYPBlWjT7bKw5b8z66+pjZTiHj4KDa/KTxCBfNXxtrfh85+tm/nle0W6eq8mpVGmpyVjqeWZ+x46+apD9Ucv6nWbPURbb0Y06EwxvhexdNgC/JEcmiJclCu1oiVWcYbAGnYGvUcz5/YZqihsiz9iuTfAtrQl46TL68ouCrJnDcWd0vhSfINcwqLQGtVl1a1FEkS5i/dW4VFVRz087RVEJtC7rdu/vj8N1/aJaXFeHItNrOwx2mbYqpRYUw2GFAbr8Rg8qazymTJ4YBEhQafmN9/RIYbfKdXcKvUqgOQNNbG9jMZ3i6QWRbrJK4XSdoRYAmnQf/65vLfS5i2/0b5he8WHRl6Cz5HHfU2qRhyGfoDJFQALoCOxb1B9qbBOmv1LKOUel3NJV/ZPvv1/n3UWq/42B/GxWvmc4UpMMrNHv3kmlyeNP9jvBm9eW0t+vvn3n8yeLseaAkUEyZMxarQ1AN8BqhQXU1yMMcrvaiw/vtaOmSCFjmtPtiwg/2rCdnfSJ6TVFhLIS5eIFIYrf/l6Zl3rFE75hizyksyQB1IfXinbhOJ2H4Vu7y7tH+JXYLuvRQogSQGaooj6Yr+C39z7H+nRpXGEFrOdP8qWlnblRx+Il50BtmuYcZ2lTAFiehqguWKWyCjZGL7+gs2WSZYiHPObrukSWTfhtFK6HShe6zg+LKRY7ZkJvAxva6nGWMtM7qmxxpfZHxhQsheM5BwycYn7Yol2SEI4mZ8L19WrVDXU35K4orUiOoaYF88wU022Mo6s4+txjQRDAzQqrNKcPlC3OiveFSPF4buwK877xD8mEoC1d3+5HavGub5Aj13uhe1HZK6YHxxZtrXaDW3WRT6PtUfr/V0QkBM5Nrz3+oEN9jUowkKcopb7l1ypnX9/531+/fO3fBYN3dfrJ31AATNvH6REq211Ssoq6ms+wXsrP+Nqy5PPCYL32BzMXGg3VOzYz9wBcpTPfG4UguMh9DgWmdx8eK4RI0JqnEnkCzYzFpzHmnlyBfkEdHE3Tta0lEjHIEP/gam9LshwLgBZoVPE6FKfHqrgtjvhTB6LZhIkdyCFKPwmZBAyYuhIf1mUiQsff7z6iDcbK4bvqOMgqayR3ZDOMPl9q0lDdf+ZctTdVRNPQd4enzdvp0GmwVjI1f9Q0v7cCGYuqLWN2tBkRHmGeG3VuuCezBBli+TYK7kmRHElxix3LMrTkRP6MbSaQTPANYOZ+wO/qLLncC2+2NqT09aFYWsvP7HKiASa64A8ZCUcgwI93sfr2RtzxIC37ruV0iShdyTZDioGv2lVww3j/4o3Cow/VPiW0ic6CNsObIYuIZTEyusGGwyZLLRnFnTl1njhd6F5IHQNlYzQMc51FREjdC1qoS+OZaJ7TwV8W9MAKrqU1Bce52OfsusJlSEbU1SO9O1elWTvJ5wzFk+HRc87EJpQQChmFBLjWi6/DkdxC3aSvnxVSGm52coVIIQ33xIbmn8Z5bFgNstzChnaXu6UFr6bt0js3mJ5Q8DpiM4W2NUGBVwTaR8SzADXdsWVh0JI06YWp913Nd1OulAt736MMxF2GULVUBNJBozmvHHgVioFPWGvINGjaIeVanN94+81GJlaCSLCsIp+ZIAB8pxI6KVtK8d0mjPiNWSLIVrazLNLA/CA8WgC9mBVMYiwjW1a+zvzsn+fJIGTVvRRwoWw0Y3HKhJRhgOZRNpyAVIvBKdPAo9MW67fwtQz7nGBcejPA+SMjdS76grqmTJ46NCQSIjine1ijl/AMYDf3JHJVVsgaNbNjSWIcPxXP0uVqGT37H5FwV4xdx+ChAmHMY6RxrU9Gziw0k+1gA0xj9xLqcv0OggoCW0bjqsMWsTFYYxSIgvJ6CqgJvp2BaV6movbRAVAee2RPFtsT1erEKkiMn8F3i+OZyvISglN8LJkUkf6c/UG7i/Sch24gMCNxaoe7xCGqhlauSd+cEMRaEJsgClle3jGy/xMoY+QFQxpitsVjcvxTONVvV0d4uNKdvM0234bOR2sZRYIpgYZ8Vl8cyDB8f3TStaReI5gkd42PcgEcMhob1w2DLV30Jtoj1ZfDrS5jAAkYkqM30QTTQpZh1A+U/PvAyb0IJnqA1xM9V4pl2oMHHgMEw/k8YKP4C1dtPu6sfiOuCEa5ZRV4c1hlb4kwi+0WsT1N9r+fjW0aIq8sJK0sEqpTvyOMoOQjr+ifrAMfTWW0BrsAYc/03RRCN3ydVqSsOK1duI1/3C8/Kv/5SYo3QANknatVbmtslRmlQJeTGgaGQvgryttPK2zWpnjDTwb36N9Z3IvhLM6Fv+QlwrUhwwJuBynUdMaHyEwnQh1mBYyNU3I4DNYnZJ2d2ILfBBv3QDoe07nJpn6H8bfLt5XFYa18K3YUPzvYZlTe8HRe3/fjZZeMdFODHYVmdsZYjYN0c+gQxCkbiaX660uBG9wEJ/JWrc3hU8UPRLOk0NrPIhVkIbycOitVL7XV+g6Jdr62YHODVQINQXbenzDSCBqn/dQcnFHUqSJhp3bCuZCVUSHZOFSxLcGTiB6cF+fTNFUZmzgm/4s6urYUiFHPQ4mungcY2YXo+FpE6BAh/qHy8e/6v7ZKWZrvdwg4otXH0imse3Han/e8xym0rr2s7K7/lGX8YRYXOCmAQYP7kdn+mIZx/m4Um7gwyG9Ky6Qv5eMo2t5Wl23A071k7DZz+wRZR3evYGy7x6vkMMm3Ud8Lt+41HIV4a3mlVd7p505WtNv7vRPYFjP5MbxtxMePu2FbkDJu7Z7cnesRK+wn/wNmkoQxE8wMr7BKTCk7r9I78GuRTqf48ZVSo3SzKgycwrVm4f8SQ+qOjEmLul3pE07v59PK4yWtxPfPY43fnx0RJM0mw5AcQsHDPy4scrMS79dd1j/Z183kYQg38ePCCI8ufNVmFCXrhnSJ7ImYsZJwS/ykt6dPg0PoI7WraFLV9SQbKwAK0O8KKuF1m5yTcLTKueFncnMmuyS68HJcJ1GSML8ANrBoteGwQLGGrfbVNqRp8mjXoKGlJqQdp7Bg5D2ZfQ5MpTsgkkqM/hYxIRdKHYamebDekllVt2mziJ7vsc5jPZ0nItaRgufeprk+Yisv3DFuVrxCmpVOPT74xPE0mvHzy4VBgiTCAcNd22laNsgl97snfyym3vqJGuqmjGYX+D5XHeeWDcQKj/cjF79EXJzxovuDn2IPrIla/kn2KwHqrcY2KnCu7XnAN/2IoKwqJjne9WNxf0NyrAiTnIWwWfKauycpq4ri/2OMOn5L2yjkMR92WtnJSRiNv46f/bIN2/RFTfSCUx/LJzewmKdl5UvAlIMPf3hxiCtH2xk0a8oMVZdsML8DiqBl0Ma6nlkOyF4eOCsuE+fu9UJ09Dyrtv5SMJ4XAsEh/lVglceNYv1EteTpSicaWo6ghu+Hmq2H/wOvjw8qzDZ7HdowMFxP0dyEW33tJbyAnRCMR+E86dUg/fGxf5FqPzq+A+elRGogA3GyZLsACyehlcIcPrTUBEYxXI7fhYa5knFE0gl3mHQuqIPt6QOPwCJGIjmYvAs3wwwhes6mZeTBx0EfTHSjl5XT1bmijSYXHornqsOUKQxxYsMS3V4fM2mGFzYBIVC17zmHqwIpYZC29wo/vZ5/U8VdVjW1utfbaKMnIwch95ecCnAbE1C53/wLU1kVULlR7Tc71tIVe1xu2BBbO8zzS6lDwonzS2ebww0k9eJyiJcmDvI5upuW1q3D+waSIGLt+95qML/R4biZvo/maySuwoMydygll6Ab8f4kQ0/G9bR4S0x/nIa/rYvh3UxRLMAQ4E4uriqyZNqc0Jn7oz1YZpMhbaPwKynOedEwymAwhd9D0TGxW3hOLnIeGVq22GXFxJzRBUwswX2Siem02jhsHJEhHA8a2eSJEVErHgwMoiBmhA3rgFrPuCIMl73yWr5FRfI81aNsDV6YoLG5q5WGooseaO2zXEEqFuYiH6R9ulYTK2UMNvn91pZf1y6P+fauz/YhM0yT/xBHa+AOHw6Y4QM5wovbhaQhIqYpXXvoOsFrS9Gt+9oIRqZTf3j5zgr2crEv4igTSm9uUQ+sWAdG2b8ZqFtc8gzO4cSkTe5/SxWST9Y+9f/6tsqhRkwLc2P/wJ1kVeGQsARrA2c4uOmE4iLV456PKHVNgWOGdPhwlvd2KuWru10hPclGRsVfGTzpKCPCEcMCYWRIyvkiv8MEr72WMk+LX/jZDTgEU7iMwg0JFIVjBpGNH3/Ts8AxCsIhXdI8qJg1pl4eBc2HURGZFsijZYzEtdLS8ryGGbAzArQZcerGsocixKzlxqGBdK+j4tL50tTeiMfQItsHu2rqRmODwsLTxBjOPWC1eaREVoC7TZwZQq5TfsTk9YOmXbxuiOC6FV/xyKlR24kml5F+tG8jjWjge6SQEmS8MHjO/WsZvyOSyjG66EmpQ109eQmDYxoUb+FIocN1c8wGWVgkIYbvTgRohZYnr98pjC9wjv6CJyHPAXofdAToAJ7xcOmrITn8/yHr5VoAAA92oT/rdm50xrHfa39AfSt3FgH9mArAHwD+IU0nQG4G/7i883l+hb+Y/YvebuoJAL/7LNUBQjeJswL2pItOBUQFUo7vOLnx8Bk1lmAPKKKAiDKBJDdhYz5pPvzyByUgbZvg6GQ2n+saVMCADiEAVLooTjYEtAiBGhethDDtlzCKzRIRoFNiCBRJrBgCoLNIA6DXrphdjUpl6tVpFixFqXItatg1SleqUZNKbjyHlJjk4Ili5Hs6OFQY+lPIISP4zYXs4DD+vpfDWe3b8XVSGSWKcrV6tj4LLXkcOhhUirgiJPgJ4E8eGckJii2KWCPHLUrEvXZtxDOof6BGr3DPTV9QSqIUrbNxJcQQqO/fX1gAAA==); }
    </style>
    
  <style>
  .ed-text { fill: var(--excalidraw-text, #222e36); }
  .ed-fill { fill: var(--excalidraw-fill, #eaced7); }
  .ed-accent-fill { fill: var(--excalidraw-accent, #d3006a); }
  .ed-accent-stroke { stroke: var(--excalidraw-accent, #d3006a); }
</style></defs>
  <g stroke-linecap="round" transform="translate(10 10) rotate(0 139.0830078125 245.07655334472656)"><path d="M0 0 C68.5 -2.7, 137.17 -2.4, 278.17 0 M0 0 C80.67 -0.15, 160.53 -0.38, 278.17 0 M278.17 0 C278.5 189.55, 278.89 380.67, 278.17 490.15 M278.17 0 C276.58 116.1, 276.72 231.88, 278.17 490.15 M278.17 490.15 C189.65 490.1, 97.14 489.89, 0 490.15 M278.17 490.15 C177.1 489.42, 75.53 488.8, 0 490.15 M0 490.15 C-1.77 347.11, -0.64 203.27, 0 0 M0 490.15 C0.62 323.91, 0.89 158, 0 0" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(109.49303878843784 15) rotate(0 39.58996902406216 12.5)"><text x="39.58996902406216" y="17.619999999999997" font-family="Excalifont, Xiaolai, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">Browser</text></g><g stroke-linecap="round" transform="translate(101.19921875 35) rotate(0 43.03125 22)"><path d="M0 0 C34.3 -0.27, 65.93 -0.31, 86.06 0 M0 0 C26.13 -0.27, 54.95 0.11, 86.06 0 M86.06 0 C86.32 16.82, 84.67 30.06, 86.06 44 M86.06 0 C87.12 17.24, 86.51 34.7, 86.06 44 M86.06 44 C63.35 45.82, 45.16 45.96, 0 44 M86.06 44 C63.58 43.25, 40.41 44.53, 0 44 M0 44 C1.34 32.42, 1.17 21.41, 0 0 M0 44 C0.62 35.17, 0.93 23.47, 0 0" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(111.21048736572266 44.5) rotate(0 33.019981384277344 12.5)"><text x="33.019981384277344" y="17.619999999999997" font-family="Excalifont, Xiaolai, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">Vue UI</text></g><g stroke-linecap="round" transform="translate(69.48046875 158) rotate(0 74.75 22)"><path d="M0 0 C35.91 -0.23, 72.52 0.73, 149.5 0 M0 0 C48.63 0.43, 96.12 -0.12, 149.5 0 M149.5 0 C148.31 8.28, 151.34 21.08, 149.5 44 M149.5 0 C150.1 15.85, 149.32 31.41, 149.5 44 M149.5 44 C95.02 46.22, 37.25 45.85, 0 44 M149.5 44 C104.2 43.35, 58.54 41.96, 0 44 M0 44 C0.58 28.74, -1.77 14.65, 0 0 M0 44 C0.65 29.55, -0.02 17.82, 0 0" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(88.75051349401474 167.5) rotate(0 55.47995525598526 12.5)"><text x="55.47995525598526" y="17.619999999999997" font-family="Excalifont, Xiaolai, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">Web Worker</text></g><g stroke-linecap="round" transform="translate(65.03125 281) rotate(0 79.19921875 22)"><path d="M0 0 C41.65 0.78, 83.11 -1.17, 158.4 0 M0 0 C46.52 -0.71, 91.1 -0.25, 158.4 0 M158.4 0 C159.87 16.19, 159.05 32.06, 158.4 44 M158.4 0 C157.95 14.93, 159.23 27.27, 158.4 44 M158.4 44 C100.76 46.02, 44.58 45.66, 0 44 M158.4 44 C122.62 43.92, 88.17 45.28, 0 44 M0 44 C-1.73 32.04, -0.05 21.44, 0 0 M0 44 C-0.16 27.4, 0.39 9.39, 0 0" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(80.2605209350586 290.5) rotate(0 63.969947814941406 12.5)"><text x="63.969947814941406" y="17.619999999999997" font-family="Excalifont, Xiaolai, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">SQLite WASM</text></g><g stroke-linecap="round" transform="translate(108.76171875 403.99999832080266) rotate(0 35.46875 35.57655334472656)"><path d="M0 0 C18.8 -1.86, 36.62 1.71, 70.94 0 M0 0 C22.53 0.38, 46.96 -0.44, 70.94 0 M70.94 0 C72.5 16.76, 71.94 30.65, 70.94 71.15 M70.94 0 C71.28 24.74, 71.14 51.73, 70.94 71.15 M70.94 71.15 C44.98 72.1, 17.38 71.34, 0 71.15 M70.94 71.15 C46.39 71, 20.89 70.92, 0 71.15 M0 71.15 C0.67 53.23, 2.43 34.74, 0 0 M0 71.15 C0.62 56.89, 0.24 43.12, 0 0" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(116.75048828125 427.0765516655292) rotate(0 27.47998046875 12.5)"><text x="27.47998046875" y="17.619999999999997" font-family="Excalifont, Xiaolai, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">OPFS</text></g><g mask="url(#mask-uOL7BFIk6ERq77sfHYsMa)" stroke-linecap="round"><g transform="translate(126.3710000000001 79.5) rotate(0 -16.73149999999987 36.96549999999979)"><path d="M-1.09 -0.12 C-6.5 6.39, -31.98 27.05, -32.41 39.33 C-32.84 51.62, -8.18 67.8, -3.66 73.6 M0.54 -1.23 C-4.94 4.89, -32.04 24.72, -32.8 37.39 C-33.57 50.05, -8.59 68.41, -4.03 74.74" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(126.3710000000001 79.5) rotate(0 -16.73149999999987 36.96549999999979)"><path d="M-24.57 65.02 C-18.45 69.95, -11.38 72.41, -4.03 74.74 M-24.57 65.02 C-18.59 66.99, -14.33 71.16, -4.03 74.74" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(126.3710000000001 79.5) rotate(0 -16.73149999999987 36.96549999999979)"><path d="M-13.51 54.09 C-10.76 62.28, -7.09 68.1, -4.03 74.74 M-13.51 54.09 C-10.62 59.07, -9.37 66.21, -4.03 74.74" stroke-width="2" fill="none" class="ed-accent-stroke"/></g></g><mask id="mask-uOL7BFIk6ERq77sfHYsMa"><rect x="0" y="0" fill="#fff" width="259.83400000000006" height="253.431"/><rect x="65.11802960205114" y="106" fill="#000" width="55.57994079589844" height="25" opacity="1"/></mask><g transform="translate(65.11802960205114 106) rotate(0 45.11558623854944 10.256568482520379)"><text x="27.78997039794922" y="17.619999999999997" font-family="Excalifont, Xiaolai, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">Async</text></g><g mask="url(#mask-7eGUJoDsntVGCgRqNGppd)" stroke-linecap="round"><g transform="translate(126.64000000000033 202.5) rotate(0 -16.48999999999978 36.952999999999975)"><path d="M1.06 0.33 C-4.14 6.8, -31.19 26.37, -32.24 38.67 C-33.29 50.97, -9.96 68.39, -5.23 74.13 M0.15 -0.54 C-5.04 6.11, -32.31 27.35, -32.8 40.03 C-33.29 52.72, -7.7 69.93, -2.79 75.57" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(126.64000000000033 202.5) rotate(0 -16.48999999999978 36.952999999999975)"><path d="M-23.77 67.26 C-18.83 70.05, -15.54 69.12, -2.79 75.57 M-23.77 67.26 C-17.92 70.92, -9.85 73.16, -2.79 75.57" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(126.64000000000033 202.5) rotate(0 -16.48999999999978 36.952999999999975)"><path d="M-13.52 55.72 C-10.74 61.01, -9.59 62.5, -2.79 75.57 M-13.52 55.72 C-10.89 62.99, -6.09 68.92, -2.79 75.57" stroke-width="2" fill="none" class="ed-accent-stroke"/></g></g><mask id="mask-7eGUJoDsntVGCgRqNGppd"><rect x="0" y="0" fill="#fff" width="259.62000000000035" height="376.406"/><rect x="65.32002121567803" y="229" fill="#000" width="56.67995756864548" height="25" opacity="1"/></mask><g transform="translate(65.32002121567803 229) rotate(0 45.44353268878285 11.01618034005378)"><text x="28.33997878432274" y="17.619999999999997" font-family="Excalifont, Xiaolai, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">Query</text></g><g mask="url(#mask-5l73aELyb_6pOegm9eaZ8)" stroke-linecap="round"><g transform="translate(144.22999999999956 330.8000000000002) rotate(0 0 33.69999999999982)"><path d="M0.74 -0.33 C0.42 5.27, -0.83 22.77, -0.86 33.93 C-0.89 45.09, 0.58 60.88, 0.54 66.64 M-0.33 -1.55 C-0.37 3.63, 1.33 20.41, 1.4 31.92 C1.46 43.44, 0.52 61.8, 0.06 67.55" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(144.22999999999956 330.8000000000002) rotate(0 0 33.69999999999982)"><path d="M5.6 15.8 C3.2 8.36, 2.1 4.08, 0.74 -0.33 M5.6 15.8 C5.01 12.43, 4.15 8.38, 0.74 -0.33" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(144.22999999999956 330.8000000000002) rotate(0 0 33.69999999999982)"><path d="M-5.91 15.15 C-3.84 7.9, -0.48 3.86, 0.74 -0.33 M-5.91 15.15 C-3.78 11.83, -1.93 7.93, 0.74 -0.33" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(144.22999999999956 330.8000000000002) rotate(0 0 33.69999999999982)"><path d="M-4.7 51.39 C-3.27 56.42, -0.64 64.67, 0.06 67.55 M-4.7 51.39 C-3.3 55.57, -1.89 59.15, 0.06 67.55" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(144.22999999999956 330.8000000000002) rotate(0 0 33.69999999999982)"><path d="M6.8 52.11 C3.77 56.93, 1.94 64.9, 0.06 67.55 M6.8 52.11 C5.49 56.22, 4.18 59.63, 0.06 67.55" stroke-width="2" fill="none" class="ed-accent-stroke"/></g></g><mask id="mask-5l73aELyb_6pOegm9eaZ8"><rect x="0" y="0" fill="#fff" width="244.22999999999956" height="498.20000000000016"/><rect x="119.38001678466753" y="352" fill="#000" width="49.69996643066406" height="25" opacity="1"/></mask><g transform="translate(119.38001678466753 352) rotate(0 25.1191106091851 11.80277989518845)"><text x="24.84998321533203" y="17.619999999999997" font-family="Excalifont, Xiaolai, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">Data</text></g><g mask="url(#mask-TlJpXHfwhd1Koz5aM0z31)" stroke-linecap="round"><g transform="translate(164.20899999999983 280.5) rotate(0 18.634000000000015 -37.06050000000005)"><path d="M-0.86 0.23 C5.32 -6.34, 37.08 -27.55, 37.81 -39.76 C38.55 -51.98, 8.99 -67.44, 3.56 -73.07 M0.89 -0.7 C6.89 -7.1, 36.32 -26.27, 37.15 -38.63 C37.99 -50.99, 11.13 -68.66, 5.9 -74.86" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(164.20899999999983 280.5) rotate(0 18.634000000000015 -37.06050000000005)"><path d="M28.17 -65.98 C20.52 -68.44, 10.82 -74.32, 5.9 -74.86 M28.17 -65.98 C20.33 -69.12, 11.09 -72.17, 5.9 -74.86" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(164.20899999999983 280.5) rotate(0 18.634000000000015 -37.06050000000005)"><path d="M17.25 -53.74 C13.58 -60.55, 7.83 -70.85, 5.9 -74.86 M17.25 -53.74 C13.58 -61.68, 8.58 -69.47, 5.9 -74.86" stroke-width="2" fill="none" class="ed-accent-stroke"/></g></g><mask id="mask-TlJpXHfwhd1Koz5aM0z31"><rect x="0" y="0" fill="#fff" width="301.47699999999986" height="454.621"/><rect x="164.03702593040452" y="229" fill="#000" width="74.87994813919067" height="25" opacity="1"/></mask><g transform="translate(164.03702593040452 229) rotate(0 18.65407760619928 14.183279942230456)"><text x="37.43997406959534" y="17.619999999999997" font-family="Excalifont, Xiaolai, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">Results</text></g><g mask="url(#mask-88GA4eSOsliSe1_wvCEqC)" stroke-linecap="round"><g transform="translate(162.09000000000015 157.5) rotate(0 16.73149999999987 -36.96549999999979)"><path d="M0.54 -0.76 C6.09 -7.13, 31.67 -25.85, 32.41 -37.95 C33.15 -50.05, 9.49 -67.41, 4.99 -73.37 M-0.63 1.45 C5.35 -5.24, 33.71 -26.71, 34.57 -39.52 C35.43 -52.33, 9.27 -69.92, 4.54 -75.42" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(162.09000000000015 157.5) rotate(0 16.73149999999987 -36.96549999999979)"><path d="M25.67 -67.05 C19.56 -70.62, 17.76 -69.78, 4.54 -75.42 M25.67 -67.05 C18.5 -69.32, 10.4 -71.92, 4.54 -75.42" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(162.09000000000015 157.5) rotate(0 16.73149999999987 -36.96549999999979)"><path d="M15.35 -55.43 C11.57 -61.7, 12.13 -63.51, 4.54 -75.42 M15.35 -55.43 C11.67 -61.75, 7.14 -68.38, 4.54 -75.42" stroke-width="2" fill="none" class="ed-accent-stroke"/></g></g><mask id="mask-88GA4eSOsliSe1_wvCEqC"><rect x="0" y="0" fill="#fff" width="295.5530000000001" height="331.431"/><rect x="149.44303539085377" y="106" fill="#000" width="92.21992921829224" height="25" opacity="1"/></mask><g transform="translate(149.44303539085377 106) rotate(0 29.62673160933673 14.516825399043228)"><text x="46.10996460914612" y="17.619999999999997" font-family="Excalifont, Xiaolai, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">Response</text></g></svg></div> <figcaption class="astro-hxyrieg5">How SQLite runs in your browser</figcaption> </figure> <script type="module">function n(i){const t=new DOMParser().parseFromString(i,"image/svg+xml"),o=t.documentElement;o.removeAttribute("filter"),t.querySelectorAll("[filter]").forEach(e=>e.removeAttribute("filter")),o.classList.add("excalidraw-rendered"),o.setAttribute("width","100%"),o.removeAttribute("height"),o.setAttribute("preserveAspectRatio","xMidYMid meet"),o.getAttribute("viewBox")||o.setAttribute("viewBox","0 0 800 600"),t.querySelectorAll("text").forEach(e=>{const r=e.getAttribute("y");if(!r||r==="NaN"||isNaN(parseFloat(r))){const c=parseFloat(e.getAttribute("font-size")||"16");e.setAttribute("y",String(Math.round(c*.85)))}});const a={"#222e36":"var(--excalidraw-text)","#eaced7":"var(--excalidraw-fill)","#d3006a":"var(--excalidraw-accent)"};return t.querySelectorAll("[fill]").forEach(e=>{const r=e.getAttribute("fill")?.toLowerCase();r&&a[r]&&e.setAttribute("fill",a[r])}),t.querySelectorAll("[stroke]").forEach(e=>{const r=e.getAttribute("stroke")?.toLowerCase();r&&a[r]&&e.setAttribute("stroke",a[r])}),new XMLSerializer().serializeToString(t)}function l(){document.querySelectorAll(".excalidraw-svg[data-svg-url]").forEach(async i=>{const s=i.dataset.svgUrl;if(s)try{const t=await fetch(s);if(!t.ok)throw new Error(`Failed to fetch SVG: ${t.statusText}`);i.innerHTML=n(await t.text())}catch(t){console.error("Error in ExcalidrawSVG component:",t)}})}document.addEventListener("DOMContentLoaded",l);document.addEventListener("astro:page-load",l);</script> 
<h2 id="-implementation-guide">📝 Implementation Guide<a class="heading-link" aria-label="Link to section" href="#-implementation-guide"><span class="heading-link-icon">#</span></a></h2>
<p>Let’s build this step by step, starting with the core SQLite functionality and then creating a playground to test it.</p>
<h3 id="step-1-install-dependencies">Step 1: Install Dependencies<a class="heading-link" aria-label="Link to section" href="#step-1-install-dependencies"><span class="heading-link-icon">#</span></a></h3>
<p>First, install the required SQLite WASM package:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#C0CAF5">npm</span><span style="color:#9ECE6A"> install</span><span style="color:#9ECE6A"> @sqlite.org/sqlite-wasm</span></span></code><button type="button" class="copy" data-code="npm install @sqlite.org/sqlite-wasm" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="step-2-configure-vite">Step 2: Configure Vite<a class="heading-link" aria-label="Link to section" href="#step-2-configure-vite"><span class="heading-link-icon">#</span></a></h3>
<p>Create or update your <code>vite.config.ts</code> file to support WebAssembly and cross-origin isolation:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="ts"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">defineConfig</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">vite</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#7DCFFF"> default</span><span style="color:#7AA2F7"> defineConfig</span><span style="color:#9ABDF5">(()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> ({</span></span>
<span class="line"><span style="color:#73DACA">  server</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">    headers</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">      &quot;</span><span style="color:#9ECE6A">Cross-Origin-Opener-Policy</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">same-origin</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &quot;</span><span style="color:#9ECE6A">Cross-Origin-Embedder-Policy</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">require-corp</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  optimizeDeps</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">    exclude</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">@sqlite.org/sqlite-wasm</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">}))</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="import { defineConfig } from &#34;vite&#34;;

export default defineConfig(() => ({
  server: {
    headers: {
      &#34;Cross-Origin-Opener-Policy&#34;: &#34;same-origin&#34;,
      &#34;Cross-Origin-Embedder-Policy&#34;: &#34;require-corp&#34;,
    },
  },
  optimizeDeps: {
    exclude: [&#34;@sqlite.org/sqlite-wasm&#34;],
  },
}));" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>This configuration is crucial for SQLite WASM to work properly:</p>
<ul>
<li>
<p><strong>Cross-Origin Headers</strong>:</p>
<ul>
<li><code>Cross-Origin-Opener-Policy</code> and <code>Cross-Origin-Embedder-Policy</code> headers enable “cross-origin isolation”</li>
<li>This is required for using SharedArrayBuffer, which SQLite WASM needs for optimal performance</li>
<li>Without these headers, the WebAssembly implementation might fail or perform poorly</li>
</ul>
</li>
<li>
<p><strong>Dependency Optimization</strong>:</p>
<ul>
<li><code>optimizeDeps.exclude</code> tells Vite not to pre-bundle the SQLite WASM package</li>
<li>This is necessary because the WASM files need to be loaded dynamically at runtime</li>
<li>Pre-bundling would break the WASM initialization process</li>
</ul>
</li>
</ul>
<h3 id="step-3-add-typescript-types">Step 3: Add TypeScript Types<a class="heading-link" aria-label="Link to section" href="#step-3-add-typescript-types"><span class="heading-link-icon">#</span></a></h3>
<p>Since <code>@sqlite.org/sqlite-wasm</code> doesn’t include TypeScript types for Sqlite3Worker1PromiserConfig, we need to create our own. Create a new file <code>types/sqlite-wasm.d.ts</code>:</p>
<p>Define this as a d.ts file so that TypeScript knows about it.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="ts"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#BB9AF7"> type</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">Worker</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">node:worker_threads</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">declare</span><span style="color:#BB9AF7"> module</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">@sqlite.org/sqlite-wasm</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  type</span><span style="color:#C0CAF5"> OnreadyFunction</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#0DB9D7"> void</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  type</span><span style="color:#C0CAF5"> Sqlite3Worker1PromiserConfig</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">    onready</span><span style="color:#89DDFF">?:</span><span style="color:#C0CAF5"> OnreadyFunction</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">    worker</span><span style="color:#89DDFF">?:</span><span style="color:#C0CAF5"> Worker</span><span style="color:#89DDFF"> |</span><span style="color:#9ABDF5"> (() </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#C0CAF5"> Worker</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">    generateMessageId</span><span style="color:#89DDFF">?:</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">messageObject</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> unknown</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">    debug</span><span style="color:#89DDFF">?:</span><span style="color:#9ABDF5"> (</span><span style="color:#F7768E;font-weight:bold">...</span><span style="color:#E0AF68">args</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> any</span><span style="color:#9ABDF5">[]) </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#0DB9D7"> void</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">    onunhandled</span><span style="color:#89DDFF">?:</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">event</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> MessageEvent</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#0DB9D7"> void</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  type</span><span style="color:#C0CAF5"> DbId</span><span style="color:#89DDFF"> =</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> undefined</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  type</span><span style="color:#C0CAF5"> PromiserMethods</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">    &quot;</span><span style="color:#9ECE6A">config-get</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">      args</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Record</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">string</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> never</span><span style="color:#89DDFF">&gt;;</span></span>
<span class="line"><span style="color:#73DACA">      result</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">        dbID</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> DbId</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">        version</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">          libVersion</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">          sourceId</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">          libVersionNumber</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">          downloadVersion</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">        }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">        bigIntEnabled</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> boolean</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">        opfsEnabled</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> boolean</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">        vfsList</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#9ABDF5">[]</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">    open</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">      args</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Partial</span><span style="color:#89DDFF">&lt;</span><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#73DACA">        filename</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">        vfs</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span><span style="color:#89DDFF">&gt;;</span></span>
<span class="line"><span style="color:#73DACA">      result</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">        dbId</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> DbId</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">        filename</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">        persistent</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> boolean</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">        vfs</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">    exec</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">      args</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">        sql</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">        dbId</span><span style="color:#89DDFF">?:</span><span style="color:#C0CAF5"> DbId</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">        bind</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> unknown</span><span style="color:#9ABDF5">[]</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">        returnValue</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">      result</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">        dbId</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> DbId</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">        sql</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">        bind</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> unknown</span><span style="color:#9ABDF5">[]</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">        returnValue</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">        resultRows</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> unknown</span><span style="color:#9ABDF5">[][]</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  type</span><span style="color:#C0CAF5"> PromiserResponseSuccess</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#9D7CD8;font-style:italic"> extends</span><span style="color:#89DDFF"> keyof</span><span style="color:#C0CAF5"> PromiserMethods</span><span style="color:#89DDFF">&gt;</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">    type</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> T</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">    result</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> PromiserMethods</span><span style="color:#9ABDF5">[</span><span style="color:#C0CAF5">T</span><span style="color:#9ABDF5">][</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">result</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">    messageId</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">    dbId</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> DbId</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">    workerReceivedTime</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">    workerRespondTime</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">    departureTime</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  type</span><span style="color:#C0CAF5"> PromiserResponseError</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">    type</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">    result</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">      operation</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">      message</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">      errorClass</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">      input</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> object</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">      stack</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> unknown</span><span style="color:#9ABDF5">[]</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">    messageId</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">    dbId</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> DbId</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  type</span><span style="color:#C0CAF5"> PromiserResponse</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#9D7CD8;font-style:italic"> extends</span><span style="color:#89DDFF"> keyof</span><span style="color:#C0CAF5"> PromiserMethods</span><span style="color:#89DDFF">&gt;</span><span style="color:#89DDFF"> =</span></span>
<span class="line"><span style="color:#89DDFF">    |</span><span style="color:#C0CAF5"> PromiserResponseSuccess</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF">&gt;</span></span>
<span class="line"><span style="color:#89DDFF">    |</span><span style="color:#C0CAF5"> PromiserResponseError</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  type</span><span style="color:#C0CAF5"> Promiser</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> &lt;</span><span style="color:#C0CAF5">T</span><span style="color:#9D7CD8;font-style:italic"> extends</span><span style="color:#89DDFF"> keyof</span><span style="color:#C0CAF5"> PromiserMethods</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#E0AF68">    messageType</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> T</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#E0AF68">    messageArguments</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> PromiserMethods</span><span style="color:#9ABDF5">[</span><span style="color:#C0CAF5">T</span><span style="color:#9ABDF5">][</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">args</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">]</span></span>
<span class="line"><span style="color:#9ABDF5">  ) </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#C0CAF5"> Promise</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">PromiserResponse</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF">&gt;&gt;;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">  export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> sqlite3Worker1Promiser</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#E0AF68">    config</span><span style="color:#89DDFF">?:</span><span style="color:#C0CAF5"> Sqlite3Worker1PromiserConfig</span><span style="color:#89DDFF"> |</span><span style="color:#C0CAF5"> OnreadyFunction</span></span>
<span class="line"><span style="color:#9ABDF5">  )</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Promiser</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="import type { Worker } from &#34;node:worker_threads&#34;;

declare module &#34;@sqlite.org/sqlite-wasm&#34; {
  type OnreadyFunction = () => void;

  type Sqlite3Worker1PromiserConfig = {
    onready?: OnreadyFunction;
    worker?: Worker | (() => Worker);
    generateMessageId?: (messageObject: unknown) => string;
    debug?: (...args: any[]) => void;
    onunhandled?: (event: MessageEvent) => void;
  };

  type DbId = string | undefined;

  type PromiserMethods = {
    &#34;config-get&#34;: {
      args: Record<string, never>;
      result: {
        dbID: DbId;
        version: {
          libVersion: string;
          sourceId: string;
          libVersionNumber: number;
          downloadVersion: number;
        };
        bigIntEnabled: boolean;
        opfsEnabled: boolean;
        vfsList: string[];
      };
    };
    open: {
      args: Partial<{
        filename?: string;
        vfs?: string;
      }>;
      result: {
        dbId: DbId;
        filename: string;
        persistent: boolean;
        vfs: string;
      };
    };
    exec: {
      args: {
        sql: string;
        dbId?: DbId;
        bind?: unknown[];
        returnValue?: string;
      };
      result: {
        dbId: DbId;
        sql: string;
        bind: unknown[];
        returnValue: string;
        resultRows?: unknown[][];
      };
    };
  };

  type PromiserResponseSuccess<T extends keyof PromiserMethods> = {
    type: T;
    result: PromiserMethods[T][&#34;result&#34;];
    messageId: string;
    dbId: DbId;
    workerReceivedTime: number;
    workerRespondTime: number;
    departureTime: number;
  };

  type PromiserResponseError = {
    type: &#34;error&#34;;
    result: {
      operation: string;
      message: string;
      errorClass: string;
      input: object;
      stack: unknown[];
    };
    messageId: string;
    dbId: DbId;
  };

  type PromiserResponse<T extends keyof PromiserMethods> =
    | PromiserResponseSuccess<T>
    | PromiserResponseError;

  type Promiser = <T extends keyof PromiserMethods>(
    messageType: T,
    messageArguments: PromiserMethods[T][&#34;args&#34;]
  ) => Promise<PromiserResponse<T>>;

  export function sqlite3Worker1Promiser(
    config?: Sqlite3Worker1PromiserConfig | OnreadyFunction
  ): Promiser;
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="step-4-create-the-sqlite-composable">Step 4: Create the SQLite Composable<a class="heading-link" aria-label="Link to section" href="#step-4-create-the-sqlite-composable"><span class="heading-link-icon">#</span></a></h3>
<p>The core of our implementation is the <code>useSQLite</code> composable. This will handle all database operations:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="ts"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#BB9AF7"> type</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">DbId</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">@sqlite.org/sqlite-wasm</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">sqlite3Worker1Promiser</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">@sqlite.org/sqlite-wasm</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">ref</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> databaseConfig</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  filename</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">file:mydb.sqlite3?vfs=opfs</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  tables</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">    test</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#41A6B5">      name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">test_table</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">      schema</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> `</span></span>
<span class="line"><span style="color:#9ECE6A">        CREATE TABLE IF NOT EXISTS test_table (</span></span>
<span class="line"><span style="color:#9ECE6A">          id INTEGER PRIMARY KEY AUTOINCREMENT,</span></span>
<span class="line"><span style="color:#9ECE6A">          name TEXT NOT NULL,</span></span>
<span class="line"><span style="color:#9ECE6A">          created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP</span></span>
<span class="line"><span style="color:#9ECE6A">        );</span></span>
<span class="line"><span style="color:#89DDFF">      `</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#89DDFF"> as</span><span style="color:#9D7CD8;font-style:italic"> const</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useSQLite</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> isLoading</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">false</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> error</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Error</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">null</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> isInitialized</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">false</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  let</span><span style="color:#BB9AF7"> promiser</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> ReturnType</span><span style="color:#89DDFF">&lt;typeof</span><span style="color:#C0CAF5"> sqlite3Worker1Promiser</span><span style="color:#89DDFF">&gt;</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> null</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  let</span><span style="color:#BB9AF7"> dbId</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> null</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  async</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> initialize</span><span style="color:#9ABDF5">() {</span></span>
<span class="line"><span style="color:#BB9AF7">    if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">isInitialized</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7;font-style:italic">return</span><span style="color:#FF9E64"> true</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">    isLoading</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> true</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">    error</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> null</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">    try</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">      // Initialize the SQLite worker</span></span>
<span class="line"><span style="color:#C0CAF5">      promiser</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#89DDFF"> new</span><span style="color:#0DB9D7"> Promise</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">resolve</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">        const</span><span style="color:#BB9AF7"> _promiser</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> sqlite3Worker1Promiser</span><span style="color:#9ABDF5">({</span></span>
<span class="line"><span style="color:#7AA2F7">          onready</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#7AA2F7"> resolve</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">_promiser</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">        })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">      })</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">      if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#C0CAF5">promiser</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">throw</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> Error</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">Failed to initialize promiser</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">      // Get configuration and open database</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">      await</span><span style="color:#7AA2F7"> promiser</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">config-get</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">      const</span><span style="color:#BB9AF7"> openResponse</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#7AA2F7"> promiser</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">open</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">        filename</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> databaseConfig</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">filename</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">      })</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">      if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">openResponse</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">type</span><span style="color:#BB9AF7"> ===</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7">        throw</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> Error</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">openResponse</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">result</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">message</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">      dbId</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> openResponse</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">result</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">dbId</span><span style="color:#89DDFF"> as</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">      // Create initial tables</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">      await</span><span style="color:#7AA2F7"> promiser</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">exec</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">        dbId</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">        sql</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> databaseConfig</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">tables</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">test</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">schema</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">      })</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">      isInitialized</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> true</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">      return</span><span style="color:#FF9E64"> true</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    } </span><span style="color:#BB9AF7">catch</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">err</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">      error</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> err</span><span style="color:#89DDFF"> instanceof</span><span style="color:#C0CAF5"> Error</span><span style="color:#BB9AF7"> ?</span><span style="color:#C0CAF5"> err</span><span style="color:#BB9AF7"> :</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> Error</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">Unknown error</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">      throw</span><span style="color:#C0CAF5"> error</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    } </span><span style="color:#BB9AF7">finally</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">      isLoading</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> false</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  async</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> executeQuery</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">sql</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> params</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> unknown</span><span style="color:#9ABDF5">[] </span><span style="color:#89DDFF">=</span><span style="color:#9ABDF5"> []) {</span></span>
<span class="line"><span style="color:#BB9AF7">    if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#C0CAF5">dbId</span><span style="color:#BB9AF7"> ||</span><span style="color:#BB9AF7"> !</span><span style="color:#C0CAF5">promiser</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">      await</span><span style="color:#7AA2F7"> initialize</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">    isLoading</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> true</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">    error</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> null</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">    try</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">      const</span><span style="color:#BB9AF7"> result</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#7AA2F7"> promiser</span><span style="color:#89DDFF">!</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">exec</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">        dbId</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> dbId</span><span style="color:#89DDFF"> as</span><span style="color:#C0CAF5"> DbId</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">        sql</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">        bind</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> params</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">        returnValue</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">resultRows</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">      })</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">      if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">result</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">type</span><span style="color:#BB9AF7"> ===</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7">        throw</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> Error</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">result</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">result</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">message</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">      return</span><span style="color:#C0CAF5"> result</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    } </span><span style="color:#BB9AF7">catch</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">err</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">      error</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span></span>
<span class="line"><span style="color:#C0CAF5">        err</span><span style="color:#89DDFF"> instanceof</span><span style="color:#C0CAF5"> Error</span><span style="color:#BB9AF7"> ?</span><span style="color:#C0CAF5"> err</span><span style="color:#BB9AF7"> :</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> Error</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">Query execution failed</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">      throw</span><span style="color:#C0CAF5"> error</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    } </span><span style="color:#BB9AF7">finally</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">      isLoading</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> false</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">    isLoading</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    error</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    isInitialized</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    executeQuery</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="import type { DbId } from &#34;@sqlite.org/sqlite-wasm&#34;;
import { sqlite3Worker1Promiser } from &#34;@sqlite.org/sqlite-wasm&#34;;
import { ref } from &#34;vue&#34;;

const databaseConfig = {
  filename: &#34;file:mydb.sqlite3?vfs=opfs&#34;,
  tables: {
    test: {
      name: &#34;test_table&#34;,
      schema: `
        CREATE TABLE IF NOT EXISTS test_table (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
          created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
      `,
    },
  },
} as const;

export function useSQLite() {
  const isLoading = ref(false);
  const error = ref<Error | null>(null);
  const isInitialized = ref(false);

  let promiser: ReturnType<typeof sqlite3Worker1Promiser> | null = null;
  let dbId: string | null = null;

  async function initialize() {
    if (isInitialized.value) return true;

    isLoading.value = true;
    error.value = null;

    try {
      // Initialize the SQLite worker
      promiser = await new Promise(resolve => {
        const _promiser = sqlite3Worker1Promiser({
          onready: () => resolve(_promiser),
        });
      });

      if (!promiser) throw new Error(&#34;Failed to initialize promiser&#34;);

      // Get configuration and open database
      await promiser(&#34;config-get&#34;, {});
      const openResponse = await promiser(&#34;open&#34;, {
        filename: databaseConfig.filename,
      });

      if (openResponse.type === &#34;error&#34;) {
        throw new Error(openResponse.result.message);
      }

      dbId = openResponse.result.dbId as string;

      // Create initial tables
      await promiser(&#34;exec&#34;, {
        dbId,
        sql: databaseConfig.tables.test.schema,
      });

      isInitialized.value = true;
      return true;
    } catch (err) {
      error.value = err instanceof Error ? err : new Error(&#34;Unknown error&#34;);
      throw error.value;
    } finally {
      isLoading.value = false;
    }
  }

  async function executeQuery(sql: string, params: unknown[] = []) {
    if (!dbId || !promiser) {
      await initialize();
    }

    isLoading.value = true;
    error.value = null;

    try {
      const result = await promiser!(&#34;exec&#34;, {
        dbId: dbId as DbId,
        sql,
        bind: params,
        returnValue: &#34;resultRows&#34;,
      });

      if (result.type === &#34;error&#34;) {
        throw new Error(result.result.message);
      }

      return result;
    } catch (err) {
      error.value =
        err instanceof Error ? err : new Error(&#34;Query execution failed&#34;);
      throw error.value;
    } finally {
      isLoading.value = false;
    }
  }

  return {
    isLoading,
    error,
    isInitialized,
    executeQuery,
  };
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="step-5-create-a-sqlite-playground-component">Step 5: Create a SQLite Playground Component<a class="heading-link" aria-label="Link to section" href="#step-5-create-a-sqlite-playground-component"><span class="heading-link-icon">#</span></a></h3>
<p>Now let’s create a component to test our SQLite implementation:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">script</span><span style="color:#BB9AF7"> setup</span><span style="color:#BB9AF7"> lang</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">ts</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">useSQLite</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">@/composables/useSQLite</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">ref</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> isLoading</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> error</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> executeQuery</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> useSQLite</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> sqlQuery</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">SELECT * FROM test_table</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> queryResult</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">any</span><span style="color:#9ABDF5">[]</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">([])</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> queryError</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">string</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">null</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Predefined example queries for testing</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> exampleQueries</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> [</span></span>
<span class="line"><span style="color:#9ABDF5">  {</span><span style="color:#73DACA"> title</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">Select all</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> query</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">SELECT * FROM test_table</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  {</span></span>
<span class="line"><span style="color:#73DACA">    title</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">Insert</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    query</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">INSERT INTO test_table (name) VALUES (&#39;New Test Item&#39;)</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  {</span></span>
<span class="line"><span style="color:#73DACA">    title</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">Update</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    query</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">UPDATE test_table SET name = &#39;Updated Item&#39; WHERE name LIKE &#39;New%&#39;</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  {</span></span>
<span class="line"><span style="color:#73DACA">    title</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">Delete</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    query</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">DELETE FROM test_table WHERE name = &#39;Updated Item&#39;</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">async</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> runQuery</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">  queryError</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> null</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">  queryResult</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> []</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  try</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> result</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#7AA2F7"> executeQuery</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">sqlQuery</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> isSelect</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> sqlQuery</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">trim</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toLowerCase</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">startsWith</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">select</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">    if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">isSelect</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">      queryResult</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> result</span><span style="color:#89DDFF">?.</span><span style="color:#C0CAF5">result</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">resultRows</span><span style="color:#BB9AF7"> ||</span><span style="color:#9ABDF5"> []</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    } </span><span style="color:#BB9AF7">else</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">      // After mutation, fetch updated data</span></span>
<span class="line"><span style="color:#C0CAF5">      queryResult</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span></span>
<span class="line"><span style="color:#9ABDF5">        (</span><span style="color:#BB9AF7;font-style:italic">await</span><span style="color:#7AA2F7"> executeQuery</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">SELECT * FROM test_table</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">?.</span><span style="color:#C0CAF5">result</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">resultRows</span><span style="color:#BB9AF7"> ||</span></span>
<span class="line"><span style="color:#9ABDF5">        []</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#9ABDF5">  } </span><span style="color:#BB9AF7">catch</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">err</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">    queryError</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> err</span><span style="color:#89DDFF"> instanceof</span><span style="color:#C0CAF5"> Error</span><span style="color:#BB9AF7"> ?</span><span style="color:#C0CAF5"> err</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">message</span><span style="color:#BB9AF7"> :</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">An error occurred</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">script</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">div</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">mx-auto max-w-7xl px-4 py-6</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">h2</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">text-2xl font-bold</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">SQLite Playground</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">h2</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">    &lt;!-- Example queries --&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">div</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">mt-4</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">      &lt;</span><span style="color:#F7768E">h3</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">text-sm font-medium</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">Example Queries:</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">h3</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">      &lt;</span><span style="color:#F7768E">div</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">mt-2 flex gap-2</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">        &lt;</span><span style="color:#F7768E">button</span></span>
<span class="line"><span style="color:#BB9AF7">          v-for</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">example in exampleQueries</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">          :key</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">example.title</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">          class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">rounded-full bg-gray-100 px-3 py-1 text-sm hover:bg-gray-200</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">          @click</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">sqlQuery = example.query</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BA3C97">        &gt;</span></span>
<span class="line"><span style="color:#9AA5CE">          {{ example.title }}</span></span>
<span class="line"><span style="color:#BA3C97">        &lt;/</span><span style="color:#F7768E">button</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">      &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">    &lt;!-- Query input --&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">div</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">mt-6</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">      &lt;</span><span style="color:#F7768E">textarea</span></span>
<span class="line"><span style="color:#BB9AF7">        v-model</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">sqlQuery</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">        rows</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">4</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">        class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">w-full rounded-lg px-4 py-3 font-mono text-sm</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">        :disabled</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">isLoading</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#FF5370">      /</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">      &lt;</span><span style="color:#F7768E">button</span></span>
<span class="line"><span style="color:#BB9AF7">        :disabled</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">isLoading</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">        class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">mt-2 rounded-lg bg-blue-600 px-4 py-2 text-white</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">        @click</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">runQuery</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BA3C97">      &gt;</span></span>
<span class="line"><span style="color:#9AA5CE">        {{ isLoading ? &quot;Running...&quot; : &quot;Run Query&quot; }}</span></span>
<span class="line"><span style="color:#BA3C97">      &lt;/</span><span style="color:#F7768E">button</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">    &lt;!-- Error display --&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">div</span></span>
<span class="line"><span style="color:#BB9AF7">      v-if</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">error || queryError</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">      class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">mt-4 rounded-lg bg-red-50 p-4 text-red-600</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BA3C97">    &gt;</span></span>
<span class="line"><span style="color:#9AA5CE">      {{ error?.message || queryError }}</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">    &lt;!-- Results table --&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">div</span><span style="color:#BB9AF7"> v-if</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">queryResult.length</span><span style="color:#89DDFF">&quot;</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">mt-4</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">      &lt;</span><span style="color:#F7768E">h3</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">text-lg font-semibold</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">Results:</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">h3</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">      &lt;</span><span style="color:#F7768E">div</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">mt-2 overflow-x-auto</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">        &lt;</span><span style="color:#F7768E">table</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">w-full</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">          &lt;</span><span style="color:#F7768E">thead</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">            &lt;</span><span style="color:#F7768E">tr</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">              &lt;</span><span style="color:#F7768E">th</span></span>
<span class="line"><span style="color:#BB9AF7">                v-for</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">column in Object.keys(queryResult[0])</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">                :key</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">column</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">                class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">px-4 py-2 text-left</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BA3C97">              &gt;</span></span>
<span class="line"><span style="color:#9AA5CE">                {{ column }}</span></span>
<span class="line"><span style="color:#BA3C97">              &lt;/</span><span style="color:#F7768E">th</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">            &lt;/</span><span style="color:#F7768E">tr</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">          &lt;/</span><span style="color:#F7768E">thead</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">          &lt;</span><span style="color:#F7768E">tbody</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">            &lt;</span><span style="color:#F7768E">tr</span><span style="color:#BB9AF7"> v-for</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">(row, index) in queryResult</span><span style="color:#89DDFF">&quot;</span><span style="color:#BB9AF7"> :key</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">index</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">              &lt;</span><span style="color:#F7768E">td</span></span>
<span class="line"><span style="color:#BB9AF7">                v-for</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">column in Object.keys(row)</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">                :key</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">column</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">                class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">px-4 py-2</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BA3C97">              &gt;</span></span>
<span class="line"><span style="color:#9AA5CE">                {{ row[column] }}</span></span>
<span class="line"><span style="color:#BA3C97">              &lt;/</span><span style="color:#F7768E">td</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">            &lt;/</span><span style="color:#F7768E">tr</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">          &lt;/</span><span style="color:#F7768E">tbody</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">        &lt;/</span><span style="color:#F7768E">table</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">      &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<script setup lang=&#34;ts&#34;>
import { useSQLite } from &#34;@/composables/useSQLite&#34;;
import { ref } from &#34;vue&#34;;

const { isLoading, error, executeQuery } = useSQLite();
const sqlQuery = ref(&#34;SELECT * FROM test_table&#34;);
const queryResult = ref<any[]>([]);
const queryError = ref<string | null>(null);

// Predefined example queries for testing
const exampleQueries = [
  { title: &#34;Select all&#34;, query: &#34;SELECT * FROM test_table&#34; },
  {
    title: &#34;Insert&#34;,
    query: &#34;INSERT INTO test_table (name) VALUES ('New Test Item')&#34;,
  },
  {
    title: &#34;Update&#34;,
    query: &#34;UPDATE test_table SET name = 'Updated Item' WHERE name LIKE 'New%'&#34;,
  },
  {
    title: &#34;Delete&#34;,
    query: &#34;DELETE FROM test_table WHERE name = 'Updated Item'&#34;,
  },
];

async function runQuery() {
  queryError.value = null;
  queryResult.value = [];

  try {
    const result = await executeQuery(sqlQuery.value);
    const isSelect = sqlQuery.value.trim().toLowerCase().startsWith(&#34;select&#34;);

    if (isSelect) {
      queryResult.value = result?.result.resultRows || [];
    } else {
      // After mutation, fetch updated data
      queryResult.value =
        (await executeQuery(&#34;SELECT * FROM test_table&#34;))?.result.resultRows ||
        [];
    }
  } catch (err) {
    queryError.value = err instanceof Error ? err.message : &#34;An error occurred&#34;;
  }
}
</script>

<template>
  <div class=&#34;mx-auto max-w-7xl px-4 py-6&#34;>
    <h2 class=&#34;text-2xl font-bold&#34;>SQLite Playground</h2>

    <!-- Example queries -->
    <div class=&#34;mt-4&#34;>
      <h3 class=&#34;text-sm font-medium&#34;>Example Queries:</h3>
      <div class=&#34;mt-2 flex gap-2&#34;>
        <button
          v-for=&#34;example in exampleQueries&#34;
          :key=&#34;example.title&#34;
          class=&#34;rounded-full bg-gray-100 px-3 py-1 text-sm hover:bg-gray-200&#34;
          @click=&#34;sqlQuery = example.query&#34;
        >
          {{ example.title }}
        </button>
      </div>
    </div>

    <!-- Query input -->
    <div class=&#34;mt-6&#34;>
      <textarea
        v-model=&#34;sqlQuery&#34;
        rows=&#34;4&#34;
        class=&#34;w-full rounded-lg px-4 py-3 font-mono text-sm&#34;
        :disabled=&#34;isLoading&#34;
      />
      <button
        :disabled=&#34;isLoading&#34;
        class=&#34;mt-2 rounded-lg bg-blue-600 px-4 py-2 text-white&#34;
        @click=&#34;runQuery&#34;
      >
        {{ isLoading ? &#34;Running...&#34; : &#34;Run Query&#34; }}
      </button>
    </div>

    <!-- Error display -->
    <div
      v-if=&#34;error || queryError&#34;
      class=&#34;mt-4 rounded-lg bg-red-50 p-4 text-red-600&#34;
    >
      {{ error?.message || queryError }}
    </div>

    <!-- Results table -->
    <div v-if=&#34;queryResult.length&#34; class=&#34;mt-4&#34;>
      <h3 class=&#34;text-lg font-semibold&#34;>Results:</h3>
      <div class=&#34;mt-2 overflow-x-auto&#34;>
        <table class=&#34;w-full&#34;>
          <thead>
            <tr>
              <th
                v-for=&#34;column in Object.keys(queryResult[0])&#34;
                :key=&#34;column&#34;
                class=&#34;px-4 py-2 text-left&#34;
              >
                {{ column }}
              </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for=&#34;(row, index) in queryResult&#34; :key=&#34;index&#34;>
              <td
                v-for=&#34;column in Object.keys(row)&#34;
                :key=&#34;column&#34;
                class=&#34;px-4 py-2&#34;
              >
                {{ row[column] }}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h2 id="-real-world-example-notions-sqlite-implementation">🎯 Real-World Example: Notion’s SQLite Implementation<a class="heading-link" aria-label="Link to section" href="#-real-world-example-notions-sqlite-implementation"><span class="heading-link-icon">#</span></a></h2>
<p><a href="https://www.notion.com/blog/how-we-sped-up-notion-in-the-browser-with-wasm-sqlite" rel="noopener noreferrer" target="_blank">Notion recently shared</a> how they implemented SQLite in their web application, providing some valuable insights:</p>
<h3 id="performance-improvements">Performance Improvements<a class="heading-link" aria-label="Link to section" href="#performance-improvements"><span class="heading-link-icon">#</span></a></h3>
<ul>
<li>20% faster page navigation across all modern browsers</li>
<li>Even greater improvements for users with slower connections:</li>
</ul>
<h3 id="multi-tab-architecture">Multi-Tab Architecture<a class="heading-link" aria-label="Link to section" href="#multi-tab-architecture"><span class="heading-link-icon">#</span></a></h3>
<p>Notion solved the challenge of handling multiple browser tabs with an innovative approach:</p>
<ol>
<li>Each tab has its own Web Worker for SQLite operations</li>
<li>A SharedWorker manages which tab is “active”</li>
<li>Only one tab can write to SQLite at a time</li>
<li>Queries from all tabs are routed through the active tab’s Worker</li>
</ol>
<h3 id="key-learnings-from-notion">Key Learnings from Notion<a class="heading-link" aria-label="Link to section" href="#key-learnings-from-notion"><span class="heading-link-icon">#</span></a></h3>
<ol>
<li><strong>Async Loading</strong>: They load the WASM SQLite library asynchronously to avoid blocking initial page load</li>
<li><strong>Race Conditions</strong>: They implemented a “racing” system between SQLite and API requests to handle slower devices</li>
<li><strong>OPFS Handling</strong>: They discovered that Origin Private File System (OPFS) doesn’t handle concurrency well out of the box</li>
<li><strong>Cross-Origin Isolation</strong>: They opted for OPFS SyncAccessHandle Pool VFS to avoid cross-origin isolation requirements</li>
</ol>
<p>This real-world implementation demonstrates both the potential and challenges of using SQLite in production web applications. Notion’s success shows that with careful architecture choices, SQLite can significantly improve web application performance.</p>
<h2 id="-conclusion">🎯 Conclusion<a class="heading-link" aria-label="Link to section" href="#-conclusion"><span class="heading-link-icon">#</span></a></h2>
<p>You now have a solid foundation for building offline-capable Vue applications using SQLite. This approach offers significant advantages over traditional browser storage solutions, especially for complex data requirements.</p> </article> <script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).only=e;window.dispatchEvent(new Event("astro:only"));})();</script><astro-island uid="Z1XneyL" component-url="/_astro/presentation.C3Wa0mjp.js" component-export="VMarkBlogRenderer" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;containerSelector&quot;:[0,&quot;#article&quot;],&quot;class&quot;:[0,&quot;astro-vj4tpspi&quot;]}" ssr client="only" opts="{&quot;name&quot;:&quot;VMarkBlogRenderer&quot;,&quot;value&quot;:&quot;react&quot;}"></astro-island> <!-- Fullscreen Modal Container using native dialog --><dialog id="mermaid-modal" class="mermaid-modal" aria-label="Fullscreen diagram view"> <div class="mermaid-modal-content"> <button class="mermaid-modal-close" aria-label="Close fullscreen view" type="button"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <line x1="18" y1="6" x2="6" y2="18"></line> <line x1="6" y1="6" x2="18" y2="18"></line> </svg> </button> <div class="mermaid-modal-diagram"></div> <div class="mermaid-modal-hint">Press <kbd>Esc</kbd> or click outside to close</div> </div> </dialog>  <script type="module">const p=new Set;function g(){const e=document.getElementById("mermaid-modal"),c=e?.querySelector(".mermaid-modal-diagram"),f=e?.querySelector(".mermaid-modal-close");if(!e||!c)return;document.querySelectorAll('svg[id^="mermaid-"]').forEach(t=>{if(!t.id.match(/^mermaid-\d+$/)||p.has(t.id)||t.parentElement?.classList.contains("mermaid-fullscreen-wrapper")||t.closest(".mermaid-modal"))return;p.add(t.id);const n=document.createElement("div");n.className="mermaid-fullscreen-wrapper mermaid-clickable",n.setAttribute("tabindex","0"),n.setAttribute("role","button"),n.setAttribute("aria-label","Click to view diagram fullscreen"),t.parentElement?.insertBefore(n,t),n.appendChild(t);const o=document.createElement("div");o.className="mermaid-expand-icon",o.innerHTML=`
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
</li> <li class="astro-vj4tpspi">Small tips and trick</li> </ul> </div> <a href="https://alex-op-newsletter.beehiiv.com/subscribe?utm_source=blog&utm_medium=post&utm_campaign=post_sqlite-vue3-offline-first-web-apps-guide" target="_blank" rel="noopener noreferrer" id="newsletter-subscribe-button" class="inline-flex items-center justify-center gap-2 rounded-full bg-skin-accent px-6 py-3 text-base font-semibold text-skin-inverted shadow-md transition-all duration-200 hover:scale-[1.02] hover:transform hover:opacity-90 astro-vj4tpspi"> <svg class="h-5 w-5 fill-current astro-vj4tpspi" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg>
Subscribe Now
</a> <button id="newsletter-dismiss" data-post-slug="sqlite-vue3-offline-first-web-apps-guide" class="absolute right-3 top-3 rounded-full p-1 text-skin-base transition-all duration-200 hover:bg-skin-accent hover:bg-opacity-10 hover:text-skin-accent astro-vj4tpspi" aria-label="Close notification"> <svg class="h-5 w-5 astro-vj4tpspi" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class="astro-vj4tpspi"></path> </svg> </button> </div> </div> </div> <ul class="my-8 flex flex-wrap gap-2 astro-vj4tpspi"> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/vue/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-2"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">vue</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/local-first/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-3"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">local-first</span>   </a> </li>  </ul> <div class="flex flex-col-reverse items-center justify-between gap-6 sm:flex-row-reverse sm:items-end sm:gap-4 astro-vj4tpspi"> <button id="back-to-top" class="focus-outline whitespace-nowrap py-1 hover:opacity-75 astro-vj4tpspi"> <svg xmlns="http://www.w3.org/2000/svg" class="rotate-90 astro-vj4tpspi"> <path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg> <span class="astro-vj4tpspi">Back to Top</span> </button> <div class="social-icons astro-wkojbtzc"> <span class="italic astro-wkojbtzc">Share this post on:</span> <div class="text-center astro-wkojbtzc"> <a href="https://wa.me/?text=https://alexop.dev/posts/sqlite-vue3-offline-first-web-apps-guide/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via WhatsApp" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"></path>
      <path d="M9 10a0.5 .5 0 0 0 1 0v-1a0.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a0.5 .5 0 0 0 0 -1h-1a0.5 .5 0 0 0 0 1"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via WhatsApp</span> </a><a href="https://www.facebook.com/sharer.php?u=https://alexop.dev/posts/sqlite-vue3-offline-first-web-apps-guide/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Facebook" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"
    ></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on Facebook</span> </a><a href="https://x.com/intent/tweet?url=https://alexop.dev/posts/sqlite-vue3-offline-first-web-apps-guide/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Tweet this post" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Tweet this post</span> </a><a href="https://t.me/share/url?url=https://alexop.dev/posts/sqlite-vue3-offline-first-web-apps-guide/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via Telegram" target="_blank" rel="noopener noreferrer"> <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon-tabler"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"></path>
      </svg> <span class="sr-only astro-wkojbtzc">Share this post via Telegram</span> </a><a href="https://pinterest.com/pin/create/button/?url=https://alexop.dev/posts/sqlite-vue3-offline-first-web-apps-guide/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Pinterest" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <line x1="8" y1="20" x2="12" y2="11"></line>
      <path d="M10.7 14c.437 1.263 1.43 2 2.55 2c2.071 0 3.75 -1.554 3.75 -4a5 5 0 1 0 -9.7 1.7"></path>
      <circle cx="12" cy="12" r="9"></circle>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post on Pinterest</span> </a><a href="mailto:?subject=See%20this%20post&#38;body=https://alexop.dev/posts/sqlite-vue3-offline-first-web-apps-guide/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via email" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via email</span> </a><a href="https://www.linkedin.com/shareArticle?mini=true&url=https://alexop.dev/posts/sqlite-vue3-offline-first-web-apps-guide/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
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
</h2> <div class="md:grid-cols-3 grid grid-cols-1 gap-6 astro-vj4tpspi"> <a href="/posts/create-pwa-vue3-vite-4-steps/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">Create a Native-Like App in 4 Steps: PWA Magic with Vue 3 and Vite</h3> <p class="related-post-description astro-vj4tpspi"> Transform your Vue 3 project into a powerful Progressive Web App in just 4 steps. Learn how to create offline-capable, installable web apps using Vite and modern PWA techniques. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="italic text-sm">Updated:</span><span class="italic text-sm"><time dateTime="2024-12-30T22:00:00.000Z">Dec 30, 2024</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> vue </span> </div> </div> </a><a href="/posts/building-local-first-apps-vue-dexie/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">Building Local-First Apps with Vue and Dexie.js</h3> <p class="related-post-description astro-vj4tpspi"> Learn how to create offline-capable, local-first applications using Vue 3 and Dexie.js. Discover patterns for data persistence, synchronization, and optimal user experience. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-01-18T00:00:00.000Z">Jan 18, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> vue </span> </div> </div> </a><a href="/posts/what-is-local-first-web-development/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">What is Local-first Web Development?</h3> <p class="related-post-description astro-vj4tpspi"> Explore the power of local-first web development and its impact on modern web applications. Learn how to build offline-capable, user-centric apps that prioritize data ownership and seamless synchronization. Discover the key principles and implementation steps for creating robust local-first web apps using Vue. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="italic text-sm">Updated:</span><span class="italic text-sm"><time dateTime="2024-11-28T15:22:00.000Z">Nov 28, 2024</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> local-first </span> </div> </div> </a> </div> </div> </main> <footer class="mt-auto astro-sz7xmlte"> <div class="max-w-5xl mx-auto px-4"> <hr class="border-skin-line" aria-hidden="true"> </div> <div class="footer-wrapper astro-sz7xmlte"> <div class="footer-content astro-sz7xmlte"> <div class="copyright-wrapper astro-sz7xmlte"> <span class="astro-sz7xmlte">Copyright &#169; 2026</span> <span class="separator astro-sz7xmlte">&nbsp;|&nbsp;</span> <span class="astro-sz7xmlte">All rights reserved.</span> </div> <div class="rss-prompt astro-sz7xmlte"> <a href="/rss.xml" class="rss-link group astro-sz7xmlte" title="Never miss a post - Subscribe via RSS" onclick="if (window.plausible) window.plausible('RSS Subscribe', { props: { location: 'footer' } })"> <div class="flex items-center gap-2 astro-sz7xmlte"> <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-skin-accent group-hover:animate-pulse astro-sz7xmlte"><path fill="currentColor" d="M19 20.001C19 11.729 12.271 5 4 5v2c7.168 0 13 5.832 13 13.001h2z" class="astro-sz7xmlte"></path><path fill="currentColor" d="M12 20.001h2C14 14.486 9.514 10 4 10v2c4.411 0 8 3.589 8 8.001z" class="astro-sz7xmlte"></path><circle cx="6" cy="18" r="2" fill="currentColor" class="astro-sz7xmlte"></circle> </svg> <span class="text-sm astro-sz7xmlte">Subscribe via RSS</span> </div> </a> </div> <div class="social-icons flex astro-upu6fzxr"> <a href="https://github.com/alexanderop" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title=" alexop.dev on Github" target="_blank" rel="noopener noreferrer"> <svg
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
    </script> </body> </html>  <script>(function(){const postSlug = "sqlite-vue3-offline-first-web-apps-guide";

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
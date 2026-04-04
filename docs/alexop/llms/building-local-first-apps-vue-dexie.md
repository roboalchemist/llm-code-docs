# Source: https://alexop.dev/posts/building-local-first-apps-vue-dexie

<!DOCTYPE html><html lang="en" class="scroll-smooth astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/posts/building-local-first-apps-vue-dexie/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>Building Local-First Apps with Vue and Dexie.js | alexop.dev</title><meta name="title" content="Building Local-First Apps with Vue and Dexie.js | alexop.dev"><meta name="description" content="Learn how to create offline-capable, local-first applications using Vue 3 and Dexie.js. Discover patterns for data persistence, synchronization, and optimal user experience."><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="Building Local-First Apps with Vue and Dexie.js | alexop.dev"><meta property="og:description" content="Learn how to create offline-capable, local-first applications using Vue 3 and Dexie.js. Discover patterns for data persistence, synchronization, and optimal user experience."><meta property="og:url" content="https://alexop.dev/posts/building-local-first-apps-vue-dexie/"><meta property="og:image" content="https://alexop.dev/posts/building-local-first-apps-with-vue-and-dexie-js/index.png"><meta property="og:type" content="article"><!-- Article Published/Modified time --><meta property="article:published_time" content="2025-01-18T00:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/posts/building-local-first-apps-vue-dexie/"><meta property="twitter:title" content="Building Local-First Apps with Vue and Dexie.js | alexop.dev"><meta property="twitter:description" content="Learn how to create offline-capable, local-first applications using Vue 3 and Dexie.js. Discover patterns for data persistence, synchronization, and optimal user experience."><meta property="twitter:image" content="https://alexop.dev/posts/building-local-first-apps-with-vue-and-dexie-js/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"Building Local-First Apps with Vue and Dexie.js | alexop.dev","description":"Learn how to create offline-capable, local-first applications using Vue 3 and Dexie.js. Discover patterns for data persistence, synchronization, and optimal user experience.","image":"https://alexop.dev/posts/building-local-first-apps-with-vue-and-dexie-js/index.png","datePublished":"2025-01-18T00:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
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
</style><style>[data-astro-transition-scope="astro-plk3gbjq-1"] { view-transition-name: building-local-first-apps-with-vue-and-dexie-js; }@layer astro { ::view-transition-old(building-local-first-apps-with-vue-and-dexie-js) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(building-local-first-apps-with-vue-and-dexie-js) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(building-local-first-apps-with-vue-and-dexie-js) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(building-local-first-apps-with-vue-and-dexie-js) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-2"] { view-transition-name: vue; }@layer astro { ::view-transition-old(vue) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-3"] { view-transition-name: dexie; }@layer astro { ::view-transition-old(dexie) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(dexie) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(dexie) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(dexie) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-4"] { view-transition-name: indexeddb; }@layer astro { ::view-transition-old(indexeddb) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(indexeddb) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(indexeddb) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(indexeddb) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-5"] { view-transition-name: local-first; }@layer astro { ::view-transition-old(local-first) { 
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <div class="mx-auto flex w-full max-w-5xl justify-start px-2 astro-vj4tpspi"> <button class="focus-outline mb-2 mt-8 flex hover:opacity-75 astro-vj4tpspi" onclick="(() => (history.length === 1) ? window.location = '/' : history.back())()"> <svg xmlns="http://www.w3.org/2000/svg" class="astro-vj4tpspi"><path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg><span class="astro-vj4tpspi">Go back</span> </button> </div> <main data-pagefind-body id="main-content" class="relative astro-vj4tpspi"> <h1 class="post-title astro-vj4tpspi" data-astro-transition-scope="astro-plk3gbjq-1">Building Local-First Apps with Vue and Dexie.js</h1> <div class="my-2 flex items-center justify-between astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-100 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-base"><time dateTime="2025-01-18T00:00:00.000Z">Jan 18, 2025</time><span class="sr-only"> at </span></span></div> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="ZPewJE" prefix="r6" component-url="/_astro/PostCopyButton.-PGtk4At.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;title&quot;:[0,&quot;Building Local-First Apps with Vue and Dexie.js&quot;],&quot;content&quot;:[0,&quot;Ever been frustrated when your web app stops working because the internet connection dropped? That&#39;s where local-first applications come in! In this guide, we&#39;ll explore how to build robust, offline-capable apps using Vue 3 and Dexie.js. If you&#39;re new to local-first development, check out my [comprehensive introduction to local-first web development](https://alexop.dev/posts/what-is-local-first-web-development/) first.\n\n## What Makes an App \&quot;Local-First\&quot;?\n\nMartin Kleppmann defines local-first software as systems where \&quot;the availability of another computer should never prevent you from working.\&quot; Think Notion&#39;s desktop app or Figma&#39;s offline mode - they store data locally first and seamlessly sync when online.\n\nThree key principles:\n\n1. Works without internet connection\n2. Users stay productive when servers are down\n3. Data syncs smoothly when connectivity returns\n\n## The Architecture Behind Local-First Apps\n\n```mermaid\n---\ntitle: Local-First Architecture with Central Server\n---\nflowchart LR\n    subgraph Client1[\&quot;Client Device\&quot;]\n        UI1[\&quot;UI\&quot;] --&gt; DB1[\&quot;Local Data\&quot;]\n    end\n\n    subgraph Client2[\&quot;Client Device\&quot;]\n        UI2[\&quot;UI\&quot;] --&gt; DB2[\&quot;Local Data\&quot;]\n    end\n\n    subgraph Server[\&quot;Central Server\&quot;]\n        SDB[\&quot;Server Data\&quot;]\n        Sync[\&quot;Sync Service\&quot;]\n    end\n\n    DB1 &lt;--&gt; Sync\n    DB2 &lt;--&gt; Sync\n    Sync &lt;--&gt; SDB\n```\n\nKey decisions:\n\n- How much data to store locally (full vs. partial dataset)\n- How to handle multi-user conflict resolution\n\n## Enter Dexie.js: Your Local-First Swiss Army Knife\n\nDexie.js provides a robust offline-first architecture where database operations run against local IndexedDB first, ensuring responsiveness without internet connection.\n\n```mermaid\n---\ntitle: Dexie.js Local-First Implementation\n---\nflowchart LR\n    subgraph Client[\&quot;Client\&quot;]\n        App[\&quot;Application\&quot;]\n        Dexie[\&quot;Dexie.js\&quot;]\n        IDB[\&quot;IndexedDB\&quot;]\n\n        App --&gt; Dexie\n        Dexie --&gt; IDB\n\n        subgraph DexieSync[\&quot;Dexie Sync\&quot;]\n            Rev[\&quot;Revision Tracking\&quot;]\n            Queue[\&quot;Sync Queue\&quot;]\n            Rev --&gt; Queue\n        end\n    end\n\n    subgraph Cloud[\&quot;Dexie Cloud\&quot;]\n        Auth[\&quot;Auth Service\&quot;]\n        Store[\&quot;Data Store\&quot;]\n        Repl[\&quot;Replication Log\&quot;]\n\n        Auth --&gt; Store\n        Store --&gt; Repl\n    end\n\n    Dexie &lt;--&gt; Rev\n    Queue &lt;--&gt; Auth\n    IDB -.-&gt; Queue\n    Queue -.-&gt; Store\n```\n\n### Sync Strategies\n\n1. **WebSocket Sync**: Real-time updates for collaborative apps\n2. **HTTP Long-Polling**: Default sync mechanism, firewall-friendly\n3. **Service Worker Sync**: Optional background syncing when configured\n\n## Setting Up Dexie Cloud\n\nTo enable multi-device synchronization and real-time collaboration, we&#39;ll use Dexie Cloud. Here&#39;s how to set it up:\n\n1. **Create a Dexie Cloud Account**:\n   - Visit [https://dexie.org/cloud/](https://dexie.org/cloud/)\n   - Sign up for a free developer account\n   - Create a new database from the dashboard\n\n2. **Install Required Packages**:\n\n   ```bash\n   npm install dexie-cloud-addon\n   ```\n\n3. **Configure Environment Variables**:\n   Create a `.env` file in your project root:\n\n   ```bash\n   VITE_DEXIE_CLOUD_URL=https://db.dexie.cloud/db/&lt;your-db-id&gt;\n   ```\n\n   Replace `&lt;your-db-id&gt;` with the database ID from your Dexie Cloud dashboard.\n\n4. **Enable Authentication**:\n   Dexie Cloud provides built-in authentication. You can:\n   - Use email/password authentication\n   - Integrate with OAuth providers\n   - Create custom authentication flows\n\nThe free tier includes:\n\n- Up to 50MB of data per database\n- Up to 1,000 sync operations per day\n- Basic authentication and access control\n- Real-time sync between devices\n\n## Building a Todo App\n\nLet&#39;s implement a practical example with a todo app:\n\n```mermaid\nflowchart TD\n    subgraph VueApp[\&quot;Vue Application\&quot;]\n        App[\&quot;App.vue\&quot;]\n        TodoList[\&quot;TodoList.vue&lt;br&gt;Component\&quot;]\n        UseTodo[\&quot;useTodo.ts&lt;br&gt;Composable\&quot;]\n        Database[\&quot;database.ts&lt;br&gt;Dexie Configuration\&quot;]\n\n        App --&gt; TodoList\n        TodoList --&gt; UseTodo\n        UseTodo --&gt; Database\n    end\n\n    subgraph DexieLayer[\&quot;Dexie.js Layer\&quot;]\n        IndexedDB[\&quot;IndexedDB\&quot;]\n        SyncEngine[\&quot;Dexie Sync Engine\&quot;]\n\n        Database --&gt; IndexedDB\n        Database --&gt; SyncEngine\n    end\n\n    subgraph Backend[\&quot;Backend Services\&quot;]\n        Server[\&quot;Server\&quot;]\n        ServerDB[\&quot;Server Database\&quot;]\n\n        SyncEngine &lt;-.-&gt; Server\n        Server &lt;-.-&gt; ServerDB\n    end\n```\n\n## Setting Up the Database\n\n```typescript\nimport Dexie, { type Table } from \&quot;dexie\&quot;;\nimport dexieCloud from \&quot;dexie-cloud-addon\&quot;;\n\nexport interface Todo {\n  id?: string;\n  title: string;\n  completed: boolean;\n  createdAt: Date;\n}\n\nexport class TodoDB extends Dexie {\n  todos!: Table&lt;Todo&gt;;\n\n  constructor() {\n    super(\&quot;TodoDB\&quot;, { addons: [dexieCloud] });\n\n    this.version(1).stores({\n      todos: \&quot;@id, title, completed, createdAt\&quot;,\n    });\n  }\n\n  async configureSync(databaseUrl: string) {\n    await this.cloud.configure({\n      databaseUrl,\n      requireAuth: true,\n      tryUseServiceWorker: true,\n    });\n  }\n}\n\nexport const db = new TodoDB();\n\nif (!import.meta.env.VITE_DEXIE_CLOUD_URL) {\n  throw new Error(\&quot;VITE_DEXIE_CLOUD_URL environment variable is not defined\&quot;);\n}\n\ndb.configureSync(import.meta.env.VITE_DEXIE_CLOUD_URL).catch(console.error);\n\nexport const currentUser = db.cloud.currentUser;\nexport const login = () =&gt; db.cloud.login();\nexport const logout = () =&gt; db.cloud.logout();\n```\n\n## Creating the Todo Composable\n\n```typescript\nimport { db, type Todo } from \&quot;@/db/todo\&quot;;\nimport { useObservable } from \&quot;@vueuse/rxjs\&quot;;\nimport { liveQuery } from \&quot;dexie\&quot;;\nimport { from } from \&quot;rxjs\&quot;;\nimport { computed, ref } from \&quot;vue\&quot;;\n\nexport function useTodos() {\n  const newTodoTitle = ref(\&quot;\&quot;);\n  const error = ref&lt;string | null&gt;(null);\n\n  const todos = useObservable&lt;Todo[]&gt;(\n    from(liveQuery(() =&gt; db.todos.orderBy(\&quot;createdAt\&quot;).toArray()))\n  );\n\n  const completedTodos = computed(\n    () =&gt; todos.value?.filter(todo =&gt; todo.completed) ?? []\n  );\n\n  const pendingTodos = computed(\n    () =&gt; todos.value?.filter(todo =&gt; !todo.completed) ?? []\n  );\n\n  const addTodo = async () =&gt; {\n    try {\n      if (!newTodoTitle.value.trim()) return;\n\n      await db.todos.add({\n        title: newTodoTitle.value,\n        completed: false,\n        createdAt: new Date(),\n      });\n\n      newTodoTitle.value = \&quot;\&quot;;\n      error.value = null;\n    } catch (err) {\n      error.value = \&quot;Failed to add todo\&quot;;\n      console.error(err);\n    }\n  };\n\n  const toggleTodo = async (todo: Todo) =&gt; {\n    try {\n      await db.todos.update(todo.id!, {\n        completed: !todo.completed,\n      });\n      error.value = null;\n    } catch (err) {\n      error.value = \&quot;Failed to toggle todo\&quot;;\n      console.error(err);\n    }\n  };\n\n  const deleteTodo = async (id: string) =&gt; {\n    try {\n      await db.todos.delete(id);\n      error.value = null;\n    } catch (err) {\n      error.value = \&quot;Failed to delete todo\&quot;;\n      console.error(err);\n    }\n  };\n\n  return {\n    todos,\n    newTodoTitle,\n    error,\n    completedTodos,\n    pendingTodos,\n    addTodo,\n    toggleTodo,\n    deleteTodo,\n  };\n}\n```\n\n## Authentication Guard Component\n\n```vue\n&lt;script setup lang=\&quot;ts\&quot;&gt;\nimport { Button } from \&quot;@/components/ui/button\&quot;;\nimport {\n  Card,\n  CardContent,\n  CardDescription,\n  CardFooter,\n  CardHeader,\n  CardTitle,\n} from \&quot;@/components/ui/card\&quot;;\nimport { currentUser, login, logout } from \&quot;@/db/todo\&quot;;\nimport { Icon } from \&quot;@iconify/vue\&quot;;\nimport { useObservable } from \&quot;@vueuse/rxjs\&quot;;\nimport { computed, ref } from \&quot;vue\&quot;;\n\nconst user = useObservable(currentUser);\nconst isAuthenticated = computed(() =&gt; !!user.value);\nconst isLoading = ref(false);\n\nasync function handleLogin() {\n  isLoading.value = true;\n  try {\n    await login();\n  } finally {\n    isLoading.value = false;\n  }\n}\n&lt;/script&gt;\n\n&lt;template&gt;\n  &lt;div\n    v-if=\&quot;!isAuthenticated\&quot;\n    class=\&quot;bg-background flex min-h-screen flex-col items-center justify-center p-4\&quot;\n  &gt;\n    &lt;Card class=\&quot;w-full max-w-md\&quot;&gt;\n      &lt;!-- Login form content --&gt;\n    &lt;/Card&gt;\n  &lt;/div&gt;\n  &lt;template v-else&gt;\n    &lt;div class=\&quot;bg-card sticky top-0 z-20 border-b\&quot;&gt;\n      &lt;!-- User info and logout button --&gt;\n    &lt;/div&gt;\n    &lt;slot /&gt;\n  &lt;/template&gt;\n&lt;/template&gt;\n```\n\n## Better Architecture: Repository Pattern\n\n```typescript\nexport interface TodoRepository {\n  getAll(): Promise&lt;Todo[]&gt;;\n  add(todo: Omit&lt;Todo, \&quot;id\&quot;&gt;): Promise&lt;string&gt;;\n  update(id: string, todo: Partial&lt;Todo&gt;): Promise&lt;void&gt;;\n  delete(id: string): Promise&lt;void&gt;;\n  observe(): Observable&lt;Todo[]&gt;;\n}\n\nexport class DexieTodoRepository implements TodoRepository {\n  constructor(private db: TodoDB) {}\n\n  async getAll() {\n    return this.db.todos.toArray();\n  }\n\n  observe() {\n    return from(liveQuery(() =&gt; this.db.todos.orderBy(\&quot;createdAt\&quot;).toArray()));\n  }\n\n  async add(todo: Omit&lt;Todo, \&quot;id\&quot;&gt;) {\n    return this.db.todos.add(todo);\n  }\n\n  async update(id: string, todo: Partial&lt;Todo&gt;) {\n    await this.db.todos.update(id, todo);\n  }\n\n  async delete(id: string) {\n    await this.db.todos.delete(id);\n  }\n}\n\nexport function useTodos(repository: TodoRepository) {\n  const newTodoTitle = ref(\&quot;\&quot;);\n  const error = ref&lt;string | null&gt;(null);\n  const todos = useObservable&lt;Todo[]&gt;(repository.observe());\n\n  const addTodo = async () =&gt; {\n    try {\n      if (!newTodoTitle.value.trim()) return;\n      await repository.add({\n        title: newTodoTitle.value,\n        completed: false,\n        createdAt: new Date(),\n      });\n      newTodoTitle.value = \&quot;\&quot;;\n      error.value = null;\n    } catch (err) {\n      error.value = \&quot;Failed to add todo\&quot;;\n      console.error(err);\n    }\n  };\n\n  return {\n    todos,\n    newTodoTitle,\n    error,\n    addTodo,\n    // ... other methods\n  };\n}\n```\n\n## Understanding the IndexedDB Structure\n\nWhen you inspect your application in the browser&#39;s DevTools under the \&quot;Application\&quot; tab &gt; \&quot;IndexedDB\&quot;, you&#39;ll see a database named \&quot;TodoDB-zy02f1...\&quot; with several object stores:\n\n### Internal Dexie Stores (Prefixed with $)\n\n&gt; Note: These stores are only created when using Dexie Cloud for sync functionality.\n\n- **$baseRevs**: Keeps track of base revisions for synchronization\n- **$jobs**: Manages background synchronization tasks\n- **$logins**: Stores authentication data including your last login timestamp\n- **$members_mutations**: Tracks changes to member data for sync\n- **$realms_mutations**: Tracks changes to realm/workspace data\n- **$roles_mutations**: Tracks changes to role assignments\n- **$syncState**: Maintains the current synchronization state\n- **$todos_mutations**: Records all changes made to todos for sync and conflict resolution\n\n### Application Data Stores\n\n- **members**: Contains user membership data with compound indexes:\n  - `[userId+realmId]`: For quick user-realm lookups\n  - `[email+realmId]`: For email-based queries\n  - `realmId`: For realm-specific queries\n- **realms**: Stores available workspaces\n- **roles**: Manages user role assignments\n- **todos**: Your actual todo items containing:\n  - Title\n  - Completed status\n  - Creation timestamp\n\nHere&#39;s how a todo item actually looks in IndexedDB:\n\n```json\n{\n  \&quot;id\&quot;: \&quot;tds0PI7ogcJqpZ1JCly0qyAheHmcom\&quot;,\n  \&quot;title\&quot;: \&quot;test\&quot;,\n  \&quot;completed\&quot;: false,\n  \&quot;createdAt\&quot;: \&quot;Tue Jan 21 2025 08:40:59 GMT+0100 (Central Europe)\&quot;,\n  \&quot;owner\&quot;: \&quot;opalic.alexander@gmail.com\&quot;,\n  \&quot;realmId\&quot;: \&quot;opalic.alexander@gmail.com\&quot;\n}\n```\n\nEach todo gets a unique `id` generated by Dexie, and when using Dexie Cloud, additional fields like `owner` and `realmId` are automatically added for multi-user support.\n\nEach store in IndexedDB acts like a table in a traditional database, but is optimized for client-side storage and offline operations. The `$`-prefixed stores are managed automatically by Dexie.js to handle:\n\n1. **Offline Persistence**: Your todos are stored locally\n2. **Multi-User Support**: User data in `members` and `roles`\n3. **Sync Management**: All `*_mutations` stores track changes\n4. **Authentication**: Login state in `$logins`\n\n## Understanding Dexie&#39;s Merge Conflict Resolution\n\n```mermaid\n%%{init: {&#39;theme&#39;: &#39;base&#39;, &#39;themeVariables&#39;: { &#39;primaryColor&#39;: &#39;#344360&#39;, &#39;primaryBorderColor&#39;: &#39;#ab4b99&#39;, &#39;primaryTextColor&#39;: &#39;#eaedf3&#39;, &#39;lineColor&#39;: &#39;#ab4b99&#39;, &#39;textColor&#39;: &#39;#eaedf3&#39; }}}%%\nflowchart LR\n    A[Detect Change Conflict] --&gt; B{Different Fields?}\n    B --&gt;|Yes| C[Auto-Merge Changes]\n    B --&gt;|No| D{Same Field Conflict}\n    D --&gt; E[Apply Server Version&lt;br&gt;Last-Write-Wins]\n    F[Delete Operation] --&gt; G[Always Takes Priority&lt;br&gt;Over Updates]\n```\n\nDexie&#39;s conflict resolution system is sophisticated and field-aware, meaning:\n\n- Changes to different fields of the same record can be merged automatically\n- Conflicts in the same field use last-write-wins with server priority\n- Deletions always take precedence over updates to prevent \&quot;zombie\&quot; records\n\nThis approach ensures smooth collaboration while maintaining data consistency across devices and users.\n\n## Conclusion\n\nThis guide demonstrated building local-first applications with Dexie.js and Vue. For simpler applications like todo lists or note-taking apps, Dexie.js provides an excellent balance of features and simplicity. For more complex needs similar to Linear, consider building a custom sync engine.\n\nFind the complete example code on [GitHub](https://github.com/alexanderop/vue-dexie).&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PostCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus-outline inline-flex items-center gap-1.5 rounded-md border border-skin-line bg-skin-card px-2.5 py-1.5 text-xs font-medium text-skin-base opacity-80 transition-all hover:border-skin-accent/50 hover:text-skin-accent hover:opacity-100" aria-label="Copy post as markdown" title="Copy post as markdown for AI/LLM"><svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg><span>Copy Post</span></button><!--astro:end--></astro-island> </div> <nav class="mb-8 astro-sbmhws2g" aria-labelledby="series-heading"> <div class="mb-1 text-sm font-bold tracking-wide text-skin-accent astro-sbmhws2g"> Local-First Web Development Series </div> <h2 id="series-heading" class="mb-2 text-xs font-semibold uppercase tracking-widest text-skin-accent astro-sbmhws2g">
This post is part of a series
</h2> <ol class="space-y-2 astro-sbmhws2g"> <li class="ml-4 text-xs text-skin-base/50 astro-sbmhws2g" aria-hidden="true">
…
</li> <li class="relative flex flex-col rounded py-2 pl-4 transition-all   astro-sbmhws2g"> <div class="flex items-center gap-2 astro-sbmhws2g"> <span class="font-mono text-xs text-skin-base/60 astro-sbmhws2g"> 2.
</span> <a href="/posts/create-pwa-vue3-vite-4-steps/" class="font-medium underline-offset-4 text-skin-accent/80 hover:underline astro-sbmhws2g"> Create a Native-Like App in 4 Steps: PWA Magic with Vue 3 and Vite </a>  </div> <div class="ml-6 mt-1 text-xs text-skin-base/70 astro-sbmhws2g"> Transform your Vue 3 project into a powerful Progressive Web App in just 4 steps. Learn how to create offline-capable, installable web apps using Vite and modern PWA techniques. </div> </li><li class="relative flex flex-col rounded py-2 pl-4 transition-all   astro-sbmhws2g"> <div class="flex items-center gap-2 astro-sbmhws2g"> <span class="font-mono text-xs text-skin-base/60 astro-sbmhws2g"> 3.
</span> <a href="/posts/sqlite-vue3-offline-first-web-apps-guide/" class="font-medium underline-offset-4 text-skin-accent/80 hover:underline astro-sbmhws2g"> SQLite in Vue: Complete Guide to Building Offline-First Web Apps </a>  </div> <div class="ml-6 mt-1 text-xs text-skin-base/70 astro-sbmhws2g"> Learn how to build offline-capable Vue 3 apps using SQLite and WebAssembly in 2024. Step-by-step tutorial includes code examples for database operations, query playground implementation, and best practices for offline-first applications. </div> </li><li class="relative flex flex-col rounded py-2 pl-4 transition-all border-l-4 border-skin-accent bg-skin-card/60  astro-sbmhws2g"> <div class="flex items-center gap-2 astro-sbmhws2g"> <span class="font-mono text-xs text-skin-accent astro-sbmhws2g"> 4.
</span> <a href="/posts/building-local-first-apps-vue-dexie/" class="font-medium underline-offset-4 pointer-events-none text-skin-accent astro-sbmhws2g" aria-current="page"> Building Local-First Apps with Vue and Dexie.js </a> <span class="ml-2 text-xs font-bold text-green-400 astro-sbmhws2g">
(current)
</span> </div> <div class="ml-6 mt-1 text-xs text-skin-base/70 astro-sbmhws2g"> Learn how to create offline-capable, local-first applications using Vue 3 and Dexie.js. Discover patterns for data persistence, synchronization, and optimal user experience. </div> </li><li class="relative flex flex-col rounded py-2 pl-4 transition-all   astro-sbmhws2g"> <div class="flex items-center gap-2 astro-sbmhws2g"> <span class="font-mono text-xs text-skin-base/60 astro-sbmhws2g"> 5.
</span> <a href="/posts/building-real-time-todo-app-jazz-vue/" class="font-medium underline-offset-4 text-skin-accent/80 hover:underline astro-sbmhws2g"> Building a Real-Time Todo App with Jazz and Vue 3 </a>  </div> <div class="ml-6 mt-1 text-xs text-skin-base/70 astro-sbmhws2g"> Build a real-time, offline-capable todo app with Jazz and Vue 3. Learn CoValues, drag-and-drop with fractional indexing, and shareable URLs — no backend needed. </div> </li>  </ol> <div class="mt-4 border-b border-skin-line opacity-40 astro-sbmhws2g"></div> </nav>  <article id="article" class="prose mx-auto mt-8 max-w-5xl astro-vj4tpspi"> <p>Ever been frustrated when your web app stops working because the internet connection dropped? That’s where local-first applications come in! In this guide, we’ll explore how to build robust, offline-capable apps using Vue 3 and Dexie.js. If you’re new to local-first development, check out my <a href="https://alexop.dev/posts/what-is-local-first-web-development/" rel="noopener noreferrer" target="_blank">comprehensive introduction to local-first web development</a> first.</p>
<h2 id="what-makes-an-app-local-first">What Makes an App “Local-First”?<a class="heading-link" aria-label="Link to section" href="#what-makes-an-app-local-first"><span class="heading-link-icon">#</span></a></h2>
<p>Martin Kleppmann defines local-first software as systems where “the availability of another computer should never prevent you from working.” Think Notion’s desktop app or Figma’s offline mode - they store data locally first and seamlessly sync when online.</p>
<p>Three key principles:</p>
<ol>
<li>Works without internet connection</li>
<li>Users stay productive when servers are down</li>
<li>Data syncs smoothly when connectivity returns</li>
</ol>
<h2 id="the-architecture-behind-local-first-apps">The Architecture Behind Local-First Apps<a class="heading-link" aria-label="Link to section" href="#the-architecture-behind-local-first-apps"><span class="heading-link-icon">#</span></a></h2>
<p><svg id="mermaid-0" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="flowchart" style="max-width:843.15625px" viewBox="0 -50 843.15625 334" role="graphics-document document" aria-roledescription="flowchart-v2"><style>#mermaid-0{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-0 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-0 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-0 .error-icon{fill:#a44141;}#mermaid-0 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-0 .edge-thickness-normal{stroke-width:1px;}#mermaid-0 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-0 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-0 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-0 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-0 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-0 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-0 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-0 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-0 p{margin:0;}#mermaid-0 .label{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;color:#ccc;}#mermaid-0 .cluster-label text{fill:#F9FFFE;}#mermaid-0 .cluster-label span{color:#F9FFFE;}#mermaid-0 .cluster-label span p{background-color:transparent;}#mermaid-0 .label text,#mermaid-0 span{fill:#ccc;color:#ccc;}#mermaid-0 .node rect,#mermaid-0 .node circle,#mermaid-0 .node ellipse,#mermaid-0 .node polygon,#mermaid-0 .node path{fill:transparent;stroke:2px;stroke-width:1px;}#mermaid-0 .rough-node .label text,#mermaid-0 .node .label text,#mermaid-0 .image-shape .label,#mermaid-0 .icon-shape .label{text-anchor:middle;}#mermaid-0 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-0 .rough-node .label,#mermaid-0 .node .label,#mermaid-0 .image-shape .label,#mermaid-0 .icon-shape .label{text-align:center;}#mermaid-0 .node.clickable{cursor:pointer;}#mermaid-0 .root .anchor path{fill:rgb(171, 75, 153)!important;stroke-width:0;stroke:rgb(171, 75, 153);}#mermaid-0 .arrowheadPath{fill:lightgrey;}#mermaid-0 .edgePath .path{stroke:rgb(171, 75, 153);stroke-width:2.0px;}#mermaid-0 .flowchart-link{stroke:rgb(171, 75, 153);fill:none;}#mermaid-0 .edgeLabel{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-0 .edgeLabel p{background-color:hsla(0, 0%, 25%, 0);}#mermaid-0 .edgeLabel rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-0 .labelBkg{background-color:rgba(63.75, 63.75, 63.75, 0.5);}#mermaid-0 .cluster rect{fill:transparent;stroke:rgba(255, 255, 255, 0.25);stroke-width:1px;}#mermaid-0 .cluster text{fill:#F9FFFE;}#mermaid-0 .cluster span{color:#F9FFFE;}#mermaid-0 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:12px;background:rgb(138, 51, 123);border:1px solid rgba(255, 255, 255, 0.25);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-0 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-0 rect.text{fill:none;stroke-width:0;}#mermaid-0 .icon-shape,#mermaid-0 .image-shape{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-0 .icon-shape p,#mermaid-0 .image-shape p{background-color:hsla(0, 0%, 25%, 0);padding:2px;}#mermaid-0 .icon-shape rect,#mermaid-0 .image-shape rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-0 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-0 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-0 :root{--mermaid-font-family:arial,sans-serif;}</style><g><marker id="mermaid-0_flowchart-v2-pointEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-pointStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="4.5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 5 L 10 10 L 10 0 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-circleEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="11" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-0_flowchart-v2-circleStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="-1" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-0_flowchart-v2-crossEnd" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="12" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-crossStart" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="-1" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><g class="root"><g class="clusters"><g class="cluster" id="Server" data-look="classic"><rect style="" x="393.59375" y="19" width="441.5625" height="236"></rect><g class="cluster-label" transform="translate(546.9453125, 19)"><foreignObject width="134.859375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Central Server</p></span></div></foreignObject></g></g><g class="cluster" id="Client2" data-look="classic"><rect style="" x="8" y="152" width="335.59375" height="124"></rect><g class="cluster-label" transform="translate(113.1796875, 152)"><foreignObject width="125.234375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Client Device</p></span></div></foreignObject></g></g><g class="cluster" id="Client1" data-look="classic"><rect style="" x="8" y="8" width="335.59375" height="124"></rect><g class="cluster-label" transform="translate(113.1796875, 8)"><foreignObject width="125.234375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Client Device</p></span></div></foreignObject></g></g></g><g class="edgePaths"><path d="M112.266,70L116.432,70C120.599,70,128.932,70,136.599,70C144.266,70,151.266,70,154.766,70L158.266,70" id="L_UI1_DB1_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_UI1_DB1_0" data-points="W3sieCI6MTEyLjI2NTYyNSwieSI6NzB9LHsieCI6MTM3LjI2NTYyNSwieSI6NzB9LHsieCI6MTYyLjI2NTYyNSwieSI6NzB9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M112.266,214L116.432,214C120.599,214,128.932,214,136.599,214C144.266,214,151.266,214,154.766,214L158.266,214" id="L_UI2_DB2_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_UI2_DB2_0" data-points="W3sieCI6MTEyLjI2NTYyNSwieSI6MjE0fSx7IngiOjEzNy4yNjU2MjUsInkiOjIxNH0seyJ4IjoxNjIuMjY1NjI1LCJ5IjoyMTR9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M322.594,70L326.094,70C329.594,70,336.594,70,344.26,70C351.927,70,360.26,70,368.594,70C376.927,70,385.26,70,400.615,77.141C415.969,84.283,438.345,98.565,449.532,105.707L460.72,112.848" id="L_DB1_Sync_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_DB1_Sync_0" data-points="W3sieCI6MzE4LjU5Mzc1LCJ5Ijo3MH0seyJ4IjozNDMuNTkzNzUsInkiOjcwfSx7IngiOjM2OC41OTM3NSwieSI6NzB9LHsieCI6MzkzLjU5Mzc1LCJ5Ijo3MH0seyJ4Ijo0NjQuMDkxNzk2ODc1LCJ5IjoxMTV9XQ==" marker-start="url(#mermaid-0_flowchart-v2-pointStart)" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M322.594,214L326.094,214C329.594,214,336.594,214,344.26,214C351.927,214,360.26,214,368.594,214C376.927,214,385.26,214,400.615,206.859C415.969,199.717,438.345,185.435,449.532,178.293L460.72,171.152" id="L_DB2_Sync_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_DB2_Sync_0" data-points="W3sieCI6MzE4LjU5Mzc1LCJ5IjoyMTR9LHsieCI6MzQzLjU5Mzc1LCJ5IjoyMTR9LHsieCI6MzY4LjU5Mzc1LCJ5IjoyMTR9LHsieCI6MzkzLjU5Mzc1LCJ5IjoyMTR9LHsieCI6NDY0LjA5MTc5Njg3NSwieSI6MTY5fV0=" marker-start="url(#mermaid-0_flowchart-v2-pointStart)" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M598.188,142L601.688,142C605.188,142,612.188,142,619.188,142C626.188,142,633.188,142,636.688,142L640.188,142" id="L_Sync_SDB_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Sync_SDB_0" data-points="W3sieCI6NTk0LjE4NzUsInkiOjE0Mn0seyJ4Ijo2MTkuMTg3NSwieSI6MTQyfSx7IngiOjY0NC4xODc1LCJ5IjoxNDJ9XQ==" marker-start="url(#mermaid-0_flowchart-v2-pointStart)" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path></g><g class="edgeLabels"><g class="edgeLabel"><g class="label" data-id="L_UI1_DB1_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_UI2_DB2_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_DB1_Sync_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_DB2_Sync_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_Sync_SDB_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g></g><g class="nodes"><g class="node default" id="flowchart-UI1-0" transform="translate(72.6328125, 70)"><rect class="basic label-container" style="" x="-39.6328125" y="-27" width="79.265625" height="54"></rect><g class="label" style="" transform="translate(-9.6328125, -12)"><rect></rect><foreignObject width="19.265625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>UI</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-DB1-1" transform="translate(240.4296875, 70)"><rect class="basic label-container" style="" x="-78.1640625" y="-27" width="156.328125" height="54"></rect><g class="label" style="" transform="translate(-48.1640625, -12)"><rect></rect><foreignObject width="96.328125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Local Data</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-UI2-2" transform="translate(72.6328125, 214)"><rect class="basic label-container" style="" x="-39.6328125" y="-27" width="79.265625" height="54"></rect><g class="label" style="" transform="translate(-9.6328125, -12)"><rect></rect><foreignObject width="19.265625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>UI</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-DB2-3" transform="translate(240.4296875, 214)"><rect class="basic label-container" style="" x="-78.1640625" y="-27" width="156.328125" height="54"></rect><g class="label" style="" transform="translate(-48.1640625, -12)"><rect></rect><foreignObject width="96.328125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Local Data</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-SDB-4" transform="translate(727.171875, 142)"><rect class="basic label-container" style="" x="-82.984375" y="-27" width="165.96875" height="54"></rect><g class="label" style="" transform="translate(-52.984375, -12)"><rect></rect><foreignObject width="105.96875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Server Data</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-Sync-5" transform="translate(506.390625, 142)"><rect class="basic label-container" style="" x="-87.796875" y="-27" width="175.59375" height="54"></rect><g class="label" style="" transform="translate(-57.796875, -12)"><rect></rect><foreignObject width="115.59375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Sync Service</p></span></div></foreignObject></g></g></g></g></g><text text-anchor="middle" x="421.578125" y="-25" class="flowchartTitleText">Local-First Architecture with Central Server</text></svg></p>
<p>Key decisions:</p>
<ul>
<li>How much data to store locally (full vs. partial dataset)</li>
<li>How to handle multi-user conflict resolution</li>
</ul>
<h2 id="enter-dexiejs-your-local-first-swiss-army-knife">Enter Dexie.js: Your Local-First Swiss Army Knife<a class="heading-link" aria-label="Link to section" href="#enter-dexiejs-your-local-first-swiss-army-knife"><span class="heading-link-icon">#</span></a></h2>
<p>Dexie.js provides a robust offline-first architecture where database operations run against local IndexedDB first, ensuring responsiveness without internet connection.</p>
<p><svg id="mermaid-1" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="flowchart" style="max-width:1685.546875px" viewBox="0 -50 1685.546875 364" role="graphics-document document" aria-roledescription="flowchart-v2"><style>#mermaid-1{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-1 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-1 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-1 .error-icon{fill:#a44141;}#mermaid-1 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-1 .edge-thickness-normal{stroke-width:1px;}#mermaid-1 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-1 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-1 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-1 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-1 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-1 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-1 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-1 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-1 p{margin:0;}#mermaid-1 .label{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;color:#ccc;}#mermaid-1 .cluster-label text{fill:#F9FFFE;}#mermaid-1 .cluster-label span{color:#F9FFFE;}#mermaid-1 .cluster-label span p{background-color:transparent;}#mermaid-1 .label text,#mermaid-1 span{fill:#ccc;color:#ccc;}#mermaid-1 .node rect,#mermaid-1 .node circle,#mermaid-1 .node ellipse,#mermaid-1 .node polygon,#mermaid-1 .node path{fill:transparent;stroke:2px;stroke-width:1px;}#mermaid-1 .rough-node .label text,#mermaid-1 .node .label text,#mermaid-1 .image-shape .label,#mermaid-1 .icon-shape .label{text-anchor:middle;}#mermaid-1 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-1 .rough-node .label,#mermaid-1 .node .label,#mermaid-1 .image-shape .label,#mermaid-1 .icon-shape .label{text-align:center;}#mermaid-1 .node.clickable{cursor:pointer;}#mermaid-1 .root .anchor path{fill:rgb(171, 75, 153)!important;stroke-width:0;stroke:rgb(171, 75, 153);}#mermaid-1 .arrowheadPath{fill:lightgrey;}#mermaid-1 .edgePath .path{stroke:rgb(171, 75, 153);stroke-width:2.0px;}#mermaid-1 .flowchart-link{stroke:rgb(171, 75, 153);fill:none;}#mermaid-1 .edgeLabel{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-1 .edgeLabel p{background-color:hsla(0, 0%, 25%, 0);}#mermaid-1 .edgeLabel rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-1 .labelBkg{background-color:rgba(63.75, 63.75, 63.75, 0.5);}#mermaid-1 .cluster rect{fill:transparent;stroke:rgba(255, 255, 255, 0.25);stroke-width:1px;}#mermaid-1 .cluster text{fill:#F9FFFE;}#mermaid-1 .cluster span{color:#F9FFFE;}#mermaid-1 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:12px;background:rgb(138, 51, 123);border:1px solid rgba(255, 255, 255, 0.25);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-1 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-1 rect.text{fill:none;stroke-width:0;}#mermaid-1 .icon-shape,#mermaid-1 .image-shape{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-1 .icon-shape p,#mermaid-1 .image-shape p{background-color:hsla(0, 0%, 25%, 0);padding:2px;}#mermaid-1 .icon-shape rect,#mermaid-1 .image-shape rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-1 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-1 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-1 :root{--mermaid-font-family:arial,sans-serif;}</style><g><marker id="mermaid-1_flowchart-v2-pointEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-1_flowchart-v2-pointStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="4.5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 5 L 10 10 L 10 0 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-1_flowchart-v2-circleEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="11" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-1_flowchart-v2-circleStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="-1" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-1_flowchart-v2-crossEnd" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="12" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-1_flowchart-v2-crossStart" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="-1" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><g class="root"><g class="clusters"><g class="cluster" id="Cloud" data-look="classic"><rect style="" x="991.125" y="17" width="686.421875" height="165"></rect><g class="cluster-label" transform="translate(1281.3515625, 17)"><foreignObject width="105.96875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Dexie Cloud</p></span></div></foreignObject></g></g><g class="cluster" id="Client" data-look="classic"><rect style="" x="8" y="8" width="933.125" height="298"></rect><g class="cluster-label" transform="translate(445.6640625, 8)"><foreignObject width="57.796875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Client</p></span></div></foreignObject></g></g><g class="cluster" id="DexieSync" data-look="classic"><rect style="" x="436.03125" y="28" width="480.09375" height="154"></rect><g class="cluster-label" transform="translate(627.9140625, 28)"><foreignObject width="96.328125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Dexie Sync</p></span></div></foreignObject></g></g></g><g class="edgePaths"><path d="M198.969,172L203.135,172C207.302,172,215.635,172,223.302,172C230.969,172,237.969,172,241.469,172L244.969,172" id="L_App_Dexie_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_App_Dexie_0" data-points="W3sieCI6MTk4Ljk2ODc1LCJ5IjoxNzJ9LHsieCI6MjIzLjk2ODc1LCJ5IjoxNzJ9LHsieCI6MjQ4Ljk2ODc1LCJ5IjoxNzJ9XQ==" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path><path d="M352.574,199L362.317,206.5C372.06,214,391.546,229,405.455,236.5C419.365,244,427.698,244,441.786,244C455.875,244,475.719,244,485.641,244L495.563,244" id="L_Dexie_IDB_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Dexie_IDB_0" data-points="W3sieCI6MzUyLjU3NDIxODc1LCJ5IjoxOTl9LHsieCI6NDExLjAzMTI1LCJ5IjoyNDR9LHsieCI6NDM2LjAzMTI1LCJ5IjoyNDR9LHsieCI6NDk5LjU2MjUsInkiOjI0NH1d" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path><path d="M684.797,90L688.964,90C693.13,90,701.464,90,709.142,90.681C716.821,91.362,723.846,92.724,727.358,93.404L730.87,94.085" id="L_Rev_Queue_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Rev_Queue_0" data-points="W3sieCI6Njg0Ljc5Njg3NSwieSI6OTB9LHsieCI6NzA5Ljc5Njg3NSwieSI6OTB9LHsieCI6NzM0Ljc5Njg3NSwieSI6OTQuODQ2NjQ4OTk2NTkyMn1d" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path><path d="M1191.719,79L1195.885,79C1200.052,79,1208.385,79,1216.08,80.06C1223.775,81.12,1230.832,83.241,1234.36,84.301L1237.888,85.361" id="L_Auth_Store_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Auth_Store_0" data-points="W3sieCI6MTE5MS43MTg3NSwieSI6Nzl9LHsieCI6MTIxNi43MTg3NSwieSI6Nzl9LHsieCI6MTI0MS43MTg3NSwieSI6ODYuNTEyMzA1OTQ0NzE3OTF9XQ==" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path><path d="M1398.047,110L1402.214,110C1406.38,110,1414.714,110,1422.38,110C1430.047,110,1437.047,110,1440.547,110L1444.047,110" id="L_Store_Repl_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Store_Repl_0" data-points="W3sieCI6MTM5OC4wNDY4NzUsInkiOjExMH0seyJ4IjoxNDIzLjA0Njg3NSwieSI6MTEwfSx7IngiOjE0NDguMDQ2ODc1LCJ5IjoxMTB9XQ==" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path><path d="M351.305,142.363L361.259,133.636C371.214,124.909,391.122,107.454,405.243,98.727C419.365,90,427.698,90,435.365,90C443.031,90,450.031,90,453.531,90L457.031,90" id="L_Dexie_Rev_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Dexie_Rev_0" data-points="W3sieCI6MzQ4LjI5Njg3NSwieSI6MTQ1fSx7IngiOjQxMS4wMzEyNSwieSI6OTB9LHsieCI6NDM2LjAzMTI1LCJ5Ijo5MH0seyJ4Ijo0NjEuMDMxMjUsInkiOjkwfV0=" marker-start="url(#mermaid-1_flowchart-v2-pointStart)" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path><path d="M894.956,85.361L898.484,84.301C902.012,83.241,909.069,81.12,916.763,80.06C924.458,79,932.792,79,941.125,79C949.458,79,957.792,79,966.125,79C974.458,79,982.792,79,990.458,79C998.125,79,1005.125,79,1008.625,79L1012.125,79" id="L_Queue_Auth_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Queue_Auth_0" data-points="W3sieCI6ODkxLjEyNSwieSI6ODYuNTEyMzA1OTQ0NzE3OTF9LHsieCI6OTE2LjEyNSwieSI6Nzl9LHsieCI6OTQxLjEyNSwieSI6Nzl9LHsieCI6OTY2LjEyNSwieSI6Nzl9LHsieCI6OTkxLjEyNSwieSI6Nzl9LHsieCI6MTAxNi4xMjUsInkiOjc5fV0=" marker-start="url(#mermaid-1_flowchart-v2-pointStart)" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path><path d="M608.796,217L625.629,204.333C642.463,191.667,676.13,166.333,696.492,152.606C716.853,138.88,723.91,136.759,727.438,135.699L730.966,134.639" id="L_IDB_Queue_0" class="edge-thickness-normal edge-pattern-dotted edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_IDB_Queue_0" data-points="W3sieCI6NjA4Ljc5NTk2NDgwNTgyNTMsInkiOjIxN30seyJ4Ijo3MDkuNzk2ODc1LCJ5IjoxNDF9LHsieCI6NzM0Ljc5Njg3NSwieSI6MTMzLjQ4NzY5NDA1NTI4MjA4fV0=" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path><path d="M891.125,133.488L895.292,134.74C899.458,135.992,907.792,138.496,916.125,139.748C924.458,141,932.792,141,941.125,141C949.458,141,957.792,141,966.125,141C974.458,141,982.792,141,1005.758,141C1028.724,141,1066.323,141,1103.922,141C1141.521,141,1179.12,141,1201.447,139.94C1223.775,138.88,1230.832,136.759,1234.36,135.699L1237.888,134.639" id="L_Queue_Store_0" class="edge-thickness-normal edge-pattern-dotted edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Queue_Store_0" data-points="W3sieCI6ODkxLjEyNSwieSI6MTMzLjQ4NzY5NDA1NTI4MjA4fSx7IngiOjkxNi4xMjUsInkiOjE0MX0seyJ4Ijo5NDEuMTI1LCJ5IjoxNDF9LHsieCI6OTY2LjEyNSwieSI6MTQxfSx7IngiOjk5MS4xMjUsInkiOjE0MX0seyJ4IjoxMTAzLjkyMTg3NSwieSI6MTQxfSx7IngiOjEyMTYuNzE4NzUsInkiOjE0MX0seyJ4IjoxMjQxLjcxODc1LCJ5IjoxMzMuNDg3Njk0MDU1MjgyMDh9XQ==" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path></g><g class="edgeLabels"><g class="edgeLabel"><g class="label" data-id="L_App_Dexie_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_Dexie_IDB_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_Rev_Queue_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_Auth_Store_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_Store_Repl_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_Dexie_Rev_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_Queue_Auth_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_IDB_Queue_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_Queue_Store_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g></g><g class="nodes"><g class="node default" id="flowchart-App-0" transform="translate(115.984375, 172)"><rect class="basic label-container" style="" x="-82.984375" y="-27" width="165.96875" height="54"></rect><g class="label" style="" transform="translate(-52.984375, -12)"><rect></rect><foreignObject width="105.96875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Application</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-Dexie-1" transform="translate(317.5, 172)"><rect class="basic label-container" style="" x="-68.53125" y="-27" width="137.0625" height="54"></rect><g class="label" style="" transform="translate(-38.53125, -12)"><rect></rect><foreignObject width="77.0625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Dexie.js</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-IDB-2" transform="translate(572.9140625, 244)"><rect class="basic label-container" style="" x="-73.3515625" y="-27" width="146.703125" height="54"></rect><g class="label" style="" transform="translate(-43.3515625, -12)"><rect></rect><foreignObject width="86.703125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>IndexedDB</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-Rev-7" transform="translate(572.9140625, 90)"><rect class="basic label-container" style="" x="-111.8828125" y="-27" width="223.765625" height="54"></rect><g class="label" style="" transform="translate(-81.8828125, -12)"><rect></rect><foreignObject width="163.765625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Revision Tracking</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-Queue-8" transform="translate(812.9609375, 110)"><rect class="basic label-container" style="" x="-78.1640625" y="-27" width="156.328125" height="54"></rect><g class="label" style="" transform="translate(-48.1640625, -12)"><rect></rect><foreignObject width="96.328125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Sync Queue</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-Auth-11" transform="translate(1103.921875, 79)"><rect class="basic label-container" style="" x="-87.796875" y="-27" width="175.59375" height="54"></rect><g class="label" style="" transform="translate(-57.796875, -12)"><rect></rect><foreignObject width="115.59375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Auth Service</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-Store-12" transform="translate(1319.8828125, 110)"><rect class="basic label-container" style="" x="-78.1640625" y="-27" width="156.328125" height="54"></rect><g class="label" style="" transform="translate(-48.1640625, -12)"><rect></rect><foreignObject width="96.328125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Data Store</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-Repl-13" transform="translate(1550.296875, 110)"><rect class="basic label-container" style="" x="-102.25" y="-27" width="204.5" height="54"></rect><g class="label" style="" transform="translate(-72.25, -12)"><rect></rect><foreignObject width="144.5" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Replication Log</p></span></div></foreignObject></g></g></g></g></g><text text-anchor="middle" x="842.7734375" y="-25" class="flowchartTitleText">Dexie.js Local-First Implementation</text></svg></p>
<h3 id="sync-strategies">Sync Strategies<a class="heading-link" aria-label="Link to section" href="#sync-strategies"><span class="heading-link-icon">#</span></a></h3>
<ol>
<li><strong>WebSocket Sync</strong>: Real-time updates for collaborative apps</li>
<li><strong>HTTP Long-Polling</strong>: Default sync mechanism, firewall-friendly</li>
<li><strong>Service Worker Sync</strong>: Optional background syncing when configured</li>
</ol>
<h2 id="setting-up-dexie-cloud">Setting Up Dexie Cloud<a class="heading-link" aria-label="Link to section" href="#setting-up-dexie-cloud"><span class="heading-link-icon">#</span></a></h2>
<p>To enable multi-device synchronization and real-time collaboration, we’ll use Dexie Cloud. Here’s how to set it up:</p>
<ol>
<li>
<p><strong>Create a Dexie Cloud Account</strong>:</p>
<ul>
<li>Visit <a href="https://dexie.org/cloud/" rel="noopener noreferrer" target="_blank">https://dexie.org/cloud/</a></li>
<li>Sign up for a free developer account</li>
<li>Create a new database from the dashboard</li>
</ul>
</li>
<li>
<p><strong>Install Required Packages</strong>:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#C0CAF5">npm</span><span style="color:#9ECE6A"> install</span><span style="color:#9ECE6A"> dexie-cloud-addon</span></span></code><button type="button" class="copy" data-code="npm install dexie-cloud-addon" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
</li>
<li>
<p><strong>Configure Environment Variables</strong>:
Create a <code>.env</code> file in your project root:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#C0CAF5">VITE_DEXIE_CLOUD_URL</span><span style="color:#89DDFF">=</span><span style="color:#9ECE6A">https://db.dexie.cloud/db/</span><span style="color:#89DDFF">&lt;</span><span style="color:#9ECE6A">your-db-id</span><span style="color:#89DDFF">&gt;</span></span></code><button type="button" class="copy" data-code="VITE_DEXIE_CLOUD_URL=https://db.dexie.cloud/db/<your-db-id>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>Replace <code>&lt;your-db-id&gt;</code> with the database ID from your Dexie Cloud dashboard.</p>
</li>
<li>
<p><strong>Enable Authentication</strong>:
Dexie Cloud provides built-in authentication. You can:</p>
<ul>
<li>Use email/password authentication</li>
<li>Integrate with OAuth providers</li>
<li>Create custom authentication flows</li>
</ul>
</li>
</ol>
<p>The free tier includes:</p>
<ul>
<li>Up to 50MB of data per database</li>
<li>Up to 1,000 sync operations per day</li>
<li>Basic authentication and access control</li>
<li>Real-time sync between devices</li>
</ul>
<h2 id="building-a-todo-app">Building a Todo App<a class="heading-link" aria-label="Link to section" href="#building-a-todo-app"><span class="heading-link-icon">#</span></a></h2>
<p>Let’s implement a practical example with a todo app:</p>
<p><svg id="mermaid-2" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="flowchart" style="max-width:506.46875px" viewBox="0 0 506.46875 916" role="graphics-document document" aria-roledescription="flowchart-v2"><style>#mermaid-2{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-2 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-2 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-2 .error-icon{fill:#a44141;}#mermaid-2 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-2 .edge-thickness-normal{stroke-width:1px;}#mermaid-2 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-2 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-2 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-2 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-2 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-2 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-2 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-2 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-2 p{margin:0;}#mermaid-2 .label{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;color:#ccc;}#mermaid-2 .cluster-label text{fill:#F9FFFE;}#mermaid-2 .cluster-label span{color:#F9FFFE;}#mermaid-2 .cluster-label span p{background-color:transparent;}#mermaid-2 .label text,#mermaid-2 span{fill:#ccc;color:#ccc;}#mermaid-2 .node rect,#mermaid-2 .node circle,#mermaid-2 .node ellipse,#mermaid-2 .node polygon,#mermaid-2 .node path{fill:transparent;stroke:2px;stroke-width:1px;}#mermaid-2 .rough-node .label text,#mermaid-2 .node .label text,#mermaid-2 .image-shape .label,#mermaid-2 .icon-shape .label{text-anchor:middle;}#mermaid-2 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-2 .rough-node .label,#mermaid-2 .node .label,#mermaid-2 .image-shape .label,#mermaid-2 .icon-shape .label{text-align:center;}#mermaid-2 .node.clickable{cursor:pointer;}#mermaid-2 .root .anchor path{fill:rgb(171, 75, 153)!important;stroke-width:0;stroke:rgb(171, 75, 153);}#mermaid-2 .arrowheadPath{fill:lightgrey;}#mermaid-2 .edgePath .path{stroke:rgb(171, 75, 153);stroke-width:2.0px;}#mermaid-2 .flowchart-link{stroke:rgb(171, 75, 153);fill:none;}#mermaid-2 .edgeLabel{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-2 .edgeLabel p{background-color:hsla(0, 0%, 25%, 0);}#mermaid-2 .edgeLabel rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-2 .labelBkg{background-color:rgba(63.75, 63.75, 63.75, 0.5);}#mermaid-2 .cluster rect{fill:transparent;stroke:rgba(255, 255, 255, 0.25);stroke-width:1px;}#mermaid-2 .cluster text{fill:#F9FFFE;}#mermaid-2 .cluster span{color:#F9FFFE;}#mermaid-2 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:12px;background:rgb(138, 51, 123);border:1px solid rgba(255, 255, 255, 0.25);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-2 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-2 rect.text{fill:none;stroke-width:0;}#mermaid-2 .icon-shape,#mermaid-2 .image-shape{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-2 .icon-shape p,#mermaid-2 .image-shape p{background-color:hsla(0, 0%, 25%, 0);padding:2px;}#mermaid-2 .icon-shape rect,#mermaid-2 .image-shape rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-2 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-2 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-2 :root{--mermaid-font-family:arial,sans-serif;}</style><g><marker id="mermaid-2_flowchart-v2-pointEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-2_flowchart-v2-pointStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="4.5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 5 L 10 10 L 10 0 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-2_flowchart-v2-circleEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="11" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-2_flowchart-v2-circleStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="-1" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-2_flowchart-v2-crossEnd" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="12" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-2_flowchart-v2-crossStart" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="-1" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><g class="root"><g class="clusters"><g class="cluster" id="Backend" data-look="classic"><rect style="" x="214.3359375" y="700" width="274.5" height="208"></rect><g class="cluster-label" transform="translate(274.5234375, 700)"><foreignObject width="154.125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Backend Services</p></span></div></foreignObject></g></g><g class="cluster" id="DexieLayer" data-look="classic"><rect style="" x="8" y="546" width="490.46875" height="104"></rect><g class="cluster-label" transform="translate(185.8046875, 546)"><foreignObject width="134.859375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Dexie.js Layer</p></span></div></foreignObject></g></g><g class="cluster" id="VueApp" data-look="classic"><rect style="" x="18.09375" y="8" width="421.75" height="488"></rect><g class="cluster-label" transform="translate(156.71875, 8)"><foreignObject width="144.5" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Vue Application</p></span></div></foreignObject></g></g></g><g class="edgePaths"><path d="M233.969,87L233.969,91.167C233.969,95.333,233.969,103.667,233.969,111.333C233.969,119,233.969,126,233.969,129.5L233.969,133" id="L_App_TodoList_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_App_TodoList_0" data-points="W3sieCI6MjMzLjk2ODc1LCJ5Ijo4N30seyJ4IjoyMzMuOTY4NzUsInkiOjExMn0seyJ4IjoyMzMuOTY4NzUsInkiOjEzN31d" marker-end="url(#mermaid-2_flowchart-v2-pointEnd)"></path><path d="M233.969,215L233.969,219.167C233.969,223.333,233.969,231.667,233.969,239.333C233.969,247,233.969,254,233.969,257.5L233.969,261" id="L_TodoList_UseTodo_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_TodoList_UseTodo_0" data-points="W3sieCI6MjMzLjk2ODc1LCJ5IjoyMTV9LHsieCI6MjMzLjk2ODc1LCJ5IjoyNDB9LHsieCI6MjMzLjk2ODc1LCJ5IjoyNjV9XQ==" marker-end="url(#mermaid-2_flowchart-v2-pointEnd)"></path><path d="M233.969,343L233.969,347.167C233.969,351.333,233.969,359.667,233.969,367.333C233.969,375,233.969,382,233.969,385.5L233.969,389" id="L_UseTodo_Database_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_UseTodo_Database_0" data-points="W3sieCI6MjMzLjk2ODc1LCJ5IjozNDN9LHsieCI6MjMzLjk2ODc1LCJ5IjozNjh9LHsieCI6MjMzLjk2ODc1LCJ5IjozOTN9XQ==" marker-end="url(#mermaid-2_flowchart-v2-pointEnd)"></path><path d="M162.296,471L154.638,475.167C146.981,479.333,131.666,487.667,124.009,496C116.352,504.333,116.352,512.667,116.352,521C116.352,529.333,116.352,537.667,116.352,545.333C116.352,553,116.352,560,116.352,563.5L116.352,567" id="L_Database_IndexedDB_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Database_IndexedDB_0" data-points="W3sieCI6MTYyLjI5NTc3NjM2NzE4NzUsInkiOjQ3MX0seyJ4IjoxMTYuMzUxNTYyNSwieSI6NDk2fSx7IngiOjExNi4zNTE1NjI1LCJ5Ijo1MjF9LHsieCI6MTE2LjM1MTU2MjUsInkiOjU0Nn0seyJ4IjoxMTYuMzUxNTYyNSwieSI6NTcxfV0=" marker-end="url(#mermaid-2_flowchart-v2-pointEnd)"></path><path d="M305.642,471L313.299,475.167C320.956,479.333,336.271,487.667,343.929,496C351.586,504.333,351.586,512.667,351.586,521C351.586,529.333,351.586,537.667,351.586,545.333C351.586,553,351.586,560,351.586,563.5L351.586,567" id="L_Database_SyncEngine_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Database_SyncEngine_0" data-points="W3sieCI6MzA1LjY0MTcyMzYzMjgxMjUsInkiOjQ3MX0seyJ4IjozNTEuNTg1OTM3NSwieSI6NDk2fSx7IngiOjM1MS41ODU5Mzc1LCJ5Ijo1MjF9LHsieCI6MzUxLjU4NTkzNzUsInkiOjU0Nn0seyJ4IjozNTEuNTg1OTM3NSwieSI6NTcxfV0=" marker-end="url(#mermaid-2_flowchart-v2-pointEnd)"></path><path d="M351.586,629L351.586,632.5C351.586,636,351.586,643,351.586,650.667C351.586,658.333,351.586,666.667,351.586,675C351.586,683.333,351.586,691.667,351.586,699.333C351.586,707,351.586,714,351.586,717.5L351.586,721" id="L_SyncEngine_Server_0" class="edge-thickness-normal edge-pattern-dotted edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_SyncEngine_Server_0" data-points="W3sieCI6MzUxLjU4NTkzNzUsInkiOjYyNX0seyJ4IjozNTEuNTg1OTM3NSwieSI6NjUwfSx7IngiOjM1MS41ODU5Mzc1LCJ5Ijo2NzV9LHsieCI6MzUxLjU4NTkzNzUsInkiOjcwMH0seyJ4IjozNTEuNTg1OTM3NSwieSI6NzI1fV0=" marker-start="url(#mermaid-2_flowchart-v2-pointStart)" marker-end="url(#mermaid-2_flowchart-v2-pointEnd)"></path><path d="M351.586,783L351.586,786.5C351.586,790,351.586,797,351.586,804C351.586,811,351.586,818,351.586,821.5L351.586,825" id="L_Server_ServerDB_0" class="edge-thickness-normal edge-pattern-dotted edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Server_ServerDB_0" data-points="W3sieCI6MzUxLjU4NTkzNzUsInkiOjc3OX0seyJ4IjozNTEuNTg1OTM3NSwieSI6ODA0fSx7IngiOjM1MS41ODU5Mzc1LCJ5Ijo4Mjl9XQ==" marker-start="url(#mermaid-2_flowchart-v2-pointStart)" marker-end="url(#mermaid-2_flowchart-v2-pointEnd)"></path></g><g class="edgeLabels"><g class="edgeLabel"><g class="label" data-id="L_App_TodoList_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_TodoList_UseTodo_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_UseTodo_Database_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_Database_IndexedDB_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_Database_SyncEngine_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_SyncEngine_Server_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_Server_ServerDB_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g></g><g class="nodes"><g class="node default" id="flowchart-App-0" transform="translate(233.96875, 60)"><rect class="basic label-container" style="" x="-63.71875" y="-27" width="127.4375" height="54"></rect><g class="label" style="" transform="translate(-33.71875, -12)"><rect></rect><foreignObject width="67.4375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>App.vue</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-TodoList-1" transform="translate(233.96875, 176)"><rect class="basic label-container" style="" x="-87.796875" y="-39" width="175.59375" height="78"></rect><g class="label" style="" transform="translate(-57.796875, -24)"><rect></rect><foreignObject width="115.59375" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>TodoList.vue<br/>Component</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-UseTodo-2" transform="translate(233.96875, 304)"><rect class="basic label-container" style="" x="-78.1640625" y="-39" width="156.328125" height="78"></rect><g class="label" style="" transform="translate(-48.1640625, -24)"><rect></rect><foreignObject width="96.328125" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>useTodo.ts<br/>Composable</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-Database-3" transform="translate(233.96875, 432)"><rect class="basic label-container" style="" x="-121.515625" y="-39" width="243.03125" height="78"></rect><g class="label" style="" transform="translate(-91.515625, -24)"><rect></rect><foreignObject width="183.03125" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>database.ts<br/>Dexie Configuration</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-IndexedDB-10" transform="translate(116.3515625, 598)"><rect class="basic label-container" style="" x="-73.3515625" y="-27" width="146.703125" height="54"></rect><g class="label" style="" transform="translate(-43.3515625, -12)"><rect></rect><foreignObject width="86.703125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>IndexedDB</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-SyncEngine-11" transform="translate(351.5859375, 598)"><rect class="basic label-container" style="" x="-111.8828125" y="-27" width="223.765625" height="54"></rect><g class="label" style="" transform="translate(-81.8828125, -12)"><rect></rect><foreignObject width="163.765625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Dexie Sync Engine</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-Server-16" transform="translate(351.5859375, 752)"><rect class="basic label-container" style="" x="-58.8984375" y="-27" width="117.796875" height="54"></rect><g class="label" style="" transform="translate(-28.8984375, -12)"><rect></rect><foreignObject width="57.796875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Server</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-ServerDB-17" transform="translate(351.5859375, 856)"><rect class="basic label-container" style="" x="-102.25" y="-27" width="204.5" height="54"></rect><g class="label" style="" transform="translate(-72.25, -12)"><rect></rect><foreignObject width="144.5" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Server Database</p></span></div></foreignObject></g></g></g></g></g></svg></p>
<h2 id="setting-up-the-database">Setting Up the Database<a class="heading-link" aria-label="Link to section" href="#setting-up-the-database"><span class="heading-link-icon">#</span></a></h2>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#0DB9D7"> Dexie</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> { </span><span style="color:#BB9AF7">type</span><span style="color:#0DB9D7"> Table</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">dexie</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#0DB9D7"> dexieCloud</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">dexie-cloud-addon</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> interface</span><span style="color:#C0CAF5"> Todo</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  id</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  title</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  completed</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> boolean</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  createdAt</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Date</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> class</span><span style="color:#C0CAF5"> TodoDB</span><span style="color:#9D7CD8;font-style:italic"> extends</span><span style="color:#BB9AF7"> Dexie</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  todos</span><span style="color:#89DDFF">!:</span><span style="color:#C0CAF5"> Table</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Todo</span><span style="color:#89DDFF">&gt;;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  constructor</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#F7768E">    super</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">TodoDB</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">addons</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#7DCFFF">dexieCloud</span><span style="color:#9ABDF5">] })</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#F7768E">    this</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">version</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">1</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">stores</span><span style="color:#9ABDF5">({</span></span>
<span class="line"><span style="color:#73DACA">      todos</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">@id, title, completed, createdAt</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  async</span><span style="color:#7AA2F7"> configureSync</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">databaseUrl</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    await</span><span style="color:#F7768E"> this</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">cloud</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">configure</span><span style="color:#9ABDF5">({</span></span>
<span class="line"><span style="color:#C0CAF5">      databaseUrl</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">      requireAuth</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">      tryUseServiceWorker</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#9D7CD8;font-style:italic"> const</span><span style="color:#BB9AF7"> db</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> TodoDB</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#7DCFFF">import</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">meta</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">env</span><span style="color:#89DDFF">.</span><span style="color:#FF9E64">VITE_DEXIE_CLOUD_URL</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  throw</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> Error</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">VITE_DEXIE_CLOUD_URL environment variable is not defined</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">db</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">configureSync</span><span style="color:#9ABDF5">(</span><span style="color:#7DCFFF">import</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">meta</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">env</span><span style="color:#89DDFF">.</span><span style="color:#FF9E64">VITE_DEXIE_CLOUD_URL</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">catch</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">console</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">error</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#9D7CD8;font-style:italic"> const</span><span style="color:#BB9AF7"> currentUser</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> db</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">cloud</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">currentUser</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#9D7CD8;font-style:italic"> const</span><span style="color:#7AA2F7"> login</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#C0CAF5"> db</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">cloud</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">login</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#9D7CD8;font-style:italic"> const</span><span style="color:#7AA2F7"> logout</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#C0CAF5"> db</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">cloud</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">logout</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="import Dexie, { type Table } from &#34;dexie&#34;;
import dexieCloud from &#34;dexie-cloud-addon&#34;;

export interface Todo {
  id?: string;
  title: string;
  completed: boolean;
  createdAt: Date;
}

export class TodoDB extends Dexie {
  todos!: Table<Todo>;

  constructor() {
    super(&#34;TodoDB&#34;, { addons: [dexieCloud] });

    this.version(1).stores({
      todos: &#34;@id, title, completed, createdAt&#34;,
    });
  }

  async configureSync(databaseUrl: string) {
    await this.cloud.configure({
      databaseUrl,
      requireAuth: true,
      tryUseServiceWorker: true,
    });
  }
}

export const db = new TodoDB();

if (!import.meta.env.VITE_DEXIE_CLOUD_URL) {
  throw new Error(&#34;VITE_DEXIE_CLOUD_URL environment variable is not defined&#34;);
}

db.configureSync(import.meta.env.VITE_DEXIE_CLOUD_URL).catch(console.error);

export const currentUser = db.cloud.currentUser;
export const login = () => db.cloud.login();
export const logout = () => db.cloud.logout();" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h2 id="creating-the-todo-composable">Creating the Todo Composable<a class="heading-link" aria-label="Link to section" href="#creating-the-todo-composable"><span class="heading-link-icon">#</span></a></h2>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">db</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> type</span><span style="color:#0DB9D7"> Todo</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">@/db/todo</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">useObservable</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">@vueuse/rxjs</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">liveQuery</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">dexie</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">from</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">rxjs</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">computed</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> ref</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useTodos</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> newTodoTitle</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> error</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">string</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">null</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> todos</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> useObservable</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Todo</span><span style="color:#9ABDF5">[]</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#7AA2F7">    from</span><span style="color:#9ABDF5">(</span><span style="color:#7AA2F7">liveQuery</span><span style="color:#9ABDF5">(() </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#C0CAF5"> db</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">todos</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">orderBy</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">createdAt</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toArray</span><span style="color:#9ABDF5">()))</span></span>
<span class="line"><span style="color:#9ABDF5">  )</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> completedTodos</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> computed</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#9ABDF5">    () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#C0CAF5"> todos</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">?.</span><span style="color:#7AA2F7">filter</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">todo</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#C0CAF5"> todo</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">completed</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">??</span><span style="color:#9ABDF5"> []</span></span>
<span class="line"><span style="color:#9ABDF5">  )</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> pendingTodos</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> computed</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#9ABDF5">    () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#C0CAF5"> todos</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">?.</span><span style="color:#7AA2F7">filter</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">todo</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#BB9AF7"> !</span><span style="color:#C0CAF5">todo</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">completed</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">??</span><span style="color:#9ABDF5"> []</span></span>
<span class="line"><span style="color:#9ABDF5">  )</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#7AA2F7"> addTodo</span><span style="color:#89DDFF"> =</span><span style="color:#9D7CD8;font-style:italic"> async</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">    try</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">      if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#C0CAF5">newTodoTitle</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">trim</span><span style="color:#9ABDF5">()) </span><span style="color:#BB9AF7;font-style:italic">return</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">      await</span><span style="color:#C0CAF5"> db</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">todos</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">add</span><span style="color:#9ABDF5">({</span></span>
<span class="line"><span style="color:#73DACA">        title</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> newTodoTitle</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">        completed</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> false</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">        createdAt</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> Date</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">      })</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">      newTodoTitle</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> &quot;&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">      error</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> null</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    } </span><span style="color:#BB9AF7">catch</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">err</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">      error</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">Failed to add todo</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">      console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">error</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">err</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#7AA2F7"> toggleTodo</span><span style="color:#89DDFF"> =</span><span style="color:#9D7CD8;font-style:italic"> async</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">todo</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Todo</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">    try</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">      await</span><span style="color:#C0CAF5"> db</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">todos</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">update</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">todo</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">id</span><span style="color:#BB9AF7">!</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">        completed</span><span style="color:#89DDFF">:</span><span style="color:#BB9AF7"> !</span><span style="color:#C0CAF5">todo</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">completed</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">      })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">      error</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> null</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    } </span><span style="color:#BB9AF7">catch</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">err</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">      error</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">Failed to toggle todo</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">      console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">error</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">err</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#7AA2F7"> deleteTodo</span><span style="color:#89DDFF"> =</span><span style="color:#9D7CD8;font-style:italic"> async</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">id</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">    try</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">      await</span><span style="color:#C0CAF5"> db</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">todos</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">delete</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">id</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">      error</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> null</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    } </span><span style="color:#BB9AF7">catch</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">err</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">      error</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">Failed to delete todo</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">      console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">error</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">err</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">    todos</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    newTodoTitle</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    error</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    completedTodos</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    pendingTodos</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    addTodo</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    toggleTodo</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    deleteTodo</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="import { db, type Todo } from &#34;@/db/todo&#34;;
import { useObservable } from &#34;@vueuse/rxjs&#34;;
import { liveQuery } from &#34;dexie&#34;;
import { from } from &#34;rxjs&#34;;
import { computed, ref } from &#34;vue&#34;;

export function useTodos() {
  const newTodoTitle = ref(&#34;&#34;);
  const error = ref<string | null>(null);

  const todos = useObservable<Todo[]>(
    from(liveQuery(() => db.todos.orderBy(&#34;createdAt&#34;).toArray()))
  );

  const completedTodos = computed(
    () => todos.value?.filter(todo => todo.completed) ?? []
  );

  const pendingTodos = computed(
    () => todos.value?.filter(todo => !todo.completed) ?? []
  );

  const addTodo = async () => {
    try {
      if (!newTodoTitle.value.trim()) return;

      await db.todos.add({
        title: newTodoTitle.value,
        completed: false,
        createdAt: new Date(),
      });

      newTodoTitle.value = &#34;&#34;;
      error.value = null;
    } catch (err) {
      error.value = &#34;Failed to add todo&#34;;
      console.error(err);
    }
  };

  const toggleTodo = async (todo: Todo) => {
    try {
      await db.todos.update(todo.id!, {
        completed: !todo.completed,
      });
      error.value = null;
    } catch (err) {
      error.value = &#34;Failed to toggle todo&#34;;
      console.error(err);
    }
  };

  const deleteTodo = async (id: string) => {
    try {
      await db.todos.delete(id);
      error.value = null;
    } catch (err) {
      error.value = &#34;Failed to delete todo&#34;;
      console.error(err);
    }
  };

  return {
    todos,
    newTodoTitle,
    error,
    completedTodos,
    pendingTodos,
    addTodo,
    toggleTodo,
    deleteTodo,
  };
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h2 id="authentication-guard-component">Authentication Guard Component<a class="heading-link" aria-label="Link to section" href="#authentication-guard-component"><span class="heading-link-icon">#</span></a></h2>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">script</span><span style="color:#BB9AF7"> setup</span><span style="color:#BB9AF7"> lang</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">ts</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">Button</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">@/components/ui/button</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#0DB9D7">  Card</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#0DB9D7">  CardContent</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#0DB9D7">  CardDescription</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#0DB9D7">  CardFooter</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#0DB9D7">  CardHeader</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#0DB9D7">  CardTitle</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">@/components/ui/card</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">currentUser</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> login</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> logout</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">@/db/todo</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">Icon</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">@iconify/vue</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">useObservable</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">@vueuse/rxjs</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">computed</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> ref</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> user</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> useObservable</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">currentUser</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> isAuthenticated</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> computed</span><span style="color:#9ABDF5">(()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#BB9AF7"> !!</span><span style="color:#C0CAF5">user</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> isLoading</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">false</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">async</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> handleLogin</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">  isLoading</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> true</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">  try</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    await</span><span style="color:#7AA2F7"> login</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  } </span><span style="color:#BB9AF7">finally</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">    isLoading</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> false</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">script</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">div</span></span>
<span class="line"><span style="color:#BB9AF7">    v-if</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">!isAuthenticated</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">    class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">bg-background flex min-h-screen flex-col items-center justify-center p-4</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BA3C97">  &gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#DE5971">Card </span><span style="color:#BB9AF7">class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">w-full max-w-md</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">      &lt;!-- Login form content --&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;/</span><span style="color:#DE5971">Card</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">template</span><span style="color:#BB9AF7"> v-else</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">div</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">bg-card sticky top-0 z-20 border-b</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">      &lt;!-- User info and logout button --&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">slot</span><span style="color:#FF5370"> /</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;/</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<script setup lang=&#34;ts&#34;>
import { Button } from &#34;@/components/ui/button&#34;;
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from &#34;@/components/ui/card&#34;;
import { currentUser, login, logout } from &#34;@/db/todo&#34;;
import { Icon } from &#34;@iconify/vue&#34;;
import { useObservable } from &#34;@vueuse/rxjs&#34;;
import { computed, ref } from &#34;vue&#34;;

const user = useObservable(currentUser);
const isAuthenticated = computed(() => !!user.value);
const isLoading = ref(false);

async function handleLogin() {
  isLoading.value = true;
  try {
    await login();
  } finally {
    isLoading.value = false;
  }
}
</script>

<template>
  <div
    v-if=&#34;!isAuthenticated&#34;
    class=&#34;bg-background flex min-h-screen flex-col items-center justify-center p-4&#34;
  >
    <Card class=&#34;w-full max-w-md&#34;>
      <!-- Login form content -->
    </Card>
  </div>
  <template v-else>
    <div class=&#34;bg-card sticky top-0 z-20 border-b&#34;>
      <!-- User info and logout button -->
    </div>
    <slot />
  </template>
</template>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h2 id="better-architecture-repository-pattern">Better Architecture: Repository Pattern<a class="heading-link" aria-label="Link to section" href="#better-architecture-repository-pattern"><span class="heading-link-icon">#</span></a></h2>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> interface</span><span style="color:#C0CAF5"> TodoRepository</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  getAll</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Promise</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Todo</span><span style="color:#9ABDF5">[]</span><span style="color:#89DDFF">&gt;;</span></span>
<span class="line"><span style="color:#7AA2F7">  add</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">todo</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Omit</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Todo</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">id</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Promise</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">string</span><span style="color:#89DDFF">&gt;;</span></span>
<span class="line"><span style="color:#7AA2F7">  update</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">id</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> todo</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Partial</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Todo</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Promise</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">void</span><span style="color:#89DDFF">&gt;;</span></span>
<span class="line"><span style="color:#7AA2F7">  delete</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">id</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Promise</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">void</span><span style="color:#89DDFF">&gt;;</span></span>
<span class="line"><span style="color:#7AA2F7">  observe</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Observable</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Todo</span><span style="color:#9ABDF5">[]</span><span style="color:#89DDFF">&gt;;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> class</span><span style="color:#C0CAF5"> DexieTodoRepository</span><span style="color:#9D7CD8;font-style:italic"> implements</span><span style="color:#BB9AF7"> TodoRepository</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  constructor</span><span style="color:#9ABDF5">(</span><span style="color:#9D7CD8;font-style:italic">private</span><span style="color:#E0AF68"> db</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> TodoDB</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  async</span><span style="color:#7AA2F7"> getAll</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#F7768E"> this</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">db</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">todos</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toArray</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  observe</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#7AA2F7"> from</span><span style="color:#9ABDF5">(</span><span style="color:#7AA2F7">liveQuery</span><span style="color:#9ABDF5">(() </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#F7768E"> this</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">db</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">todos</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">orderBy</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">createdAt</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toArray</span><span style="color:#9ABDF5">()))</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  async</span><span style="color:#7AA2F7"> add</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">todo</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Omit</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Todo</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">id</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#F7768E"> this</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">db</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">todos</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">add</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">todo</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  async</span><span style="color:#7AA2F7"> update</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">id</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> todo</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Partial</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Todo</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    await</span><span style="color:#F7768E"> this</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">db</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">todos</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">update</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">id</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> todo</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  async</span><span style="color:#7AA2F7"> delete</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">id</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    await</span><span style="color:#F7768E"> this</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">db</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">todos</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">delete</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">id</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useTodos</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">repository</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> TodoRepository</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> newTodoTitle</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> error</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">string</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">null</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> todos</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> useObservable</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Todo</span><span style="color:#9ABDF5">[]</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">repository</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">observe</span><span style="color:#9ABDF5">())</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#7AA2F7"> addTodo</span><span style="color:#89DDFF"> =</span><span style="color:#9D7CD8;font-style:italic"> async</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">    try</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">      if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#C0CAF5">newTodoTitle</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">trim</span><span style="color:#9ABDF5">()) </span><span style="color:#BB9AF7;font-style:italic">return</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">      await</span><span style="color:#C0CAF5"> repository</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">add</span><span style="color:#9ABDF5">({</span></span>
<span class="line"><span style="color:#73DACA">        title</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> newTodoTitle</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">        completed</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> false</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">        createdAt</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> Date</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">      })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">      newTodoTitle</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> &quot;&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">      error</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> null</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    } </span><span style="color:#BB9AF7">catch</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">err</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">      error</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">Failed to add todo</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">      console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">error</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">err</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">    todos</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    newTodoTitle</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    error</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    addTodo</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">    // ... other methods</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="export interface TodoRepository {
  getAll(): Promise<Todo[]>;
  add(todo: Omit<Todo, &#34;id&#34;>): Promise<string>;
  update(id: string, todo: Partial<Todo>): Promise<void>;
  delete(id: string): Promise<void>;
  observe(): Observable<Todo[]>;
}

export class DexieTodoRepository implements TodoRepository {
  constructor(private db: TodoDB) {}

  async getAll() {
    return this.db.todos.toArray();
  }

  observe() {
    return from(liveQuery(() => this.db.todos.orderBy(&#34;createdAt&#34;).toArray()));
  }

  async add(todo: Omit<Todo, &#34;id&#34;>) {
    return this.db.todos.add(todo);
  }

  async update(id: string, todo: Partial<Todo>) {
    await this.db.todos.update(id, todo);
  }

  async delete(id: string) {
    await this.db.todos.delete(id);
  }
}

export function useTodos(repository: TodoRepository) {
  const newTodoTitle = ref(&#34;&#34;);
  const error = ref<string | null>(null);
  const todos = useObservable<Todo[]>(repository.observe());

  const addTodo = async () => {
    try {
      if (!newTodoTitle.value.trim()) return;
      await repository.add({
        title: newTodoTitle.value,
        completed: false,
        createdAt: new Date(),
      });
      newTodoTitle.value = &#34;&#34;;
      error.value = null;
    } catch (err) {
      error.value = &#34;Failed to add todo&#34;;
      console.error(err);
    }
  };

  return {
    todos,
    newTodoTitle,
    error,
    addTodo,
    // ... other methods
  };
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h2 id="understanding-the-indexeddb-structure">Understanding the IndexedDB Structure<a class="heading-link" aria-label="Link to section" href="#understanding-the-indexeddb-structure"><span class="heading-link-icon">#</span></a></h2>
<p>When you inspect your application in the browser’s DevTools under the “Application” tab &gt; “IndexedDB”, you’ll see a database named “TodoDB-zy02f1…” with several object stores:</p>
<h3 id="internal-dexie-stores-prefixed-with">Internal Dexie Stores (Prefixed with $)<a class="heading-link" aria-label="Link to section" href="#internal-dexie-stores-prefixed-with"><span class="heading-link-icon">#</span></a></h3>
<blockquote>
<p>Note: These stores are only created when using Dexie Cloud for sync functionality.</p>
</blockquote>
<ul>
<li><strong>$baseRevs</strong>: Keeps track of base revisions for synchronization</li>
<li><strong>$jobs</strong>: Manages background synchronization tasks</li>
<li><strong>$logins</strong>: Stores authentication data including your last login timestamp</li>
<li><strong>$members_mutations</strong>: Tracks changes to member data for sync</li>
<li><strong>$realms_mutations</strong>: Tracks changes to realm/workspace data</li>
<li><strong>$roles_mutations</strong>: Tracks changes to role assignments</li>
<li><strong>$syncState</strong>: Maintains the current synchronization state</li>
<li><strong>$todos_mutations</strong>: Records all changes made to todos for sync and conflict resolution</li>
</ul>
<h3 id="application-data-stores">Application Data Stores<a class="heading-link" aria-label="Link to section" href="#application-data-stores"><span class="heading-link-icon">#</span></a></h3>
<ul>
<li><strong>members</strong>: Contains user membership data with compound indexes:
<ul>
<li><code>[userId+realmId]</code>: For quick user-realm lookups</li>
<li><code>[email+realmId]</code>: For email-based queries</li>
<li><code>realmId</code>: For realm-specific queries</li>
</ul>
</li>
<li><strong>realms</strong>: Stores available workspaces</li>
<li><strong>roles</strong>: Manages user role assignments</li>
<li><strong>todos</strong>: Your actual todo items containing:
<ul>
<li>Title</li>
<li>Completed status</li>
<li>Creation timestamp</li>
</ul>
</li>
</ul>
<p>Here’s how a todo item actually looks in IndexedDB:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="json"><code><span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">id</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">tds0PI7ogcJqpZ1JCly0qyAheHmcom</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">title</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">test</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">completed</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> false</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">createdAt</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">Tue Jan 21 2025 08:40:59 GMT+0100 (Central Europe)</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">owner</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">opalic.alexander@gmail.com</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">realmId</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">opalic.alexander@gmail.com</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="{
  &#34;id&#34;: &#34;tds0PI7ogcJqpZ1JCly0qyAheHmcom&#34;,
  &#34;title&#34;: &#34;test&#34;,
  &#34;completed&#34;: false,
  &#34;createdAt&#34;: &#34;Tue Jan 21 2025 08:40:59 GMT+0100 (Central Europe)&#34;,
  &#34;owner&#34;: &#34;opalic.alexander@gmail.com&#34;,
  &#34;realmId&#34;: &#34;opalic.alexander@gmail.com&#34;
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>Each todo gets a unique <code>id</code> generated by Dexie, and when using Dexie Cloud, additional fields like <code>owner</code> and <code>realmId</code> are automatically added for multi-user support.</p>
<p>Each store in IndexedDB acts like a table in a traditional database, but is optimized for client-side storage and offline operations. The <code>$</code>-prefixed stores are managed automatically by Dexie.js to handle:</p>
<ol>
<li><strong>Offline Persistence</strong>: Your todos are stored locally</li>
<li><strong>Multi-User Support</strong>: User data in <code>members</code> and <code>roles</code></li>
<li><strong>Sync Management</strong>: All <code>*_mutations</code> stores track changes</li>
<li><strong>Authentication</strong>: Login state in <code>$logins</code></li>
</ol>
<h2 id="understanding-dexies-merge-conflict-resolution">Understanding Dexie’s Merge Conflict Resolution<a class="heading-link" aria-label="Link to section" href="#understanding-dexies-merge-conflict-resolution"><span class="heading-link-icon">#</span></a></h2>
<p><svg id="mermaid-3" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="flowchart" style="max-width:1204.59375px" viewBox="0 0 1204.59375 401.640625" role="graphics-document document" aria-roledescription="flowchart-v2"><style>#mermaid-3{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#eaedf3;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-3 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-3 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-3 .error-icon{fill:rgb(138, 51, 123);}#mermaid-3 .error-text{fill:#75cc84;stroke:#75cc84;}#mermaid-3 .edge-thickness-normal{stroke-width:1px;}#mermaid-3 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-3 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-3 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-3 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-3 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-3 .marker{fill:#ab4b99;stroke:#ab4b99;}#mermaid-3 .marker.cross{stroke:#ab4b99;}#mermaid-3 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-3 p{margin:0;}#mermaid-3 .label{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;color:#eaedf3;}#mermaid-3 .cluster-label text{fill:#75cc84;}#mermaid-3 .cluster-label span{color:#75cc84;}#mermaid-3 .cluster-label span p{background-color:transparent;}#mermaid-3 .label text,#mermaid-3 span{fill:#eaedf3;color:#eaedf3;}#mermaid-3 .node rect,#mermaid-3 .node circle,#mermaid-3 .node ellipse,#mermaid-3 .node polygon,#mermaid-3 .node path{fill:transparent;stroke:2px;stroke-width:1px;}#mermaid-3 .rough-node .label text,#mermaid-3 .node .label text,#mermaid-3 .image-shape .label,#mermaid-3 .icon-shape .label{text-anchor:middle;}#mermaid-3 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-3 .rough-node .label,#mermaid-3 .node .label,#mermaid-3 .image-shape .label,#mermaid-3 .icon-shape .label{text-align:center;}#mermaid-3 .node.clickable{cursor:pointer;}#mermaid-3 .root .anchor path{fill:#ab4b99!important;stroke-width:0;stroke:#ab4b99;}#mermaid-3 .arrowheadPath{fill:#0b0b0b;}#mermaid-3 .edgePath .path{stroke:#ab4b99;stroke-width:2.0px;}#mermaid-3 .flowchart-link{stroke:#ab4b99;fill:none;}#mermaid-3 .edgeLabel{background-color:rgb(52, 63, 96);text-align:center;}#mermaid-3 .edgeLabel p{background-color:rgb(52, 63, 96);}#mermaid-3 .edgeLabel rect{opacity:0.5;background-color:rgb(52, 63, 96);fill:rgb(52, 63, 96);}#mermaid-3 .labelBkg{background-color:rgba(52, 63, 96, 0.5);}#mermaid-3 .cluster rect{fill:transparent;stroke:hsl(310.3448275862, 6.0317460317%, 27.0588235294%);stroke-width:1px;}#mermaid-3 .cluster text{fill:#75cc84;}#mermaid-3 .cluster span{color:#75cc84;}#mermaid-3 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:12px;background:rgb(138, 51, 123);border:1px solid hsl(310.3448275862, 6.0317460317%, 27.0588235294%);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-3 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#eaedf3;}#mermaid-3 rect.text{fill:none;stroke-width:0;}#mermaid-3 .icon-shape,#mermaid-3 .image-shape{background-color:rgb(52, 63, 96);text-align:center;}#mermaid-3 .icon-shape p,#mermaid-3 .image-shape p{background-color:rgb(52, 63, 96);padding:2px;}#mermaid-3 .icon-shape rect,#mermaid-3 .image-shape rect{opacity:0.5;background-color:rgb(52, 63, 96);fill:rgb(52, 63, 96);}#mermaid-3 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-3 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-3 :root{--mermaid-font-family:arial,sans-serif;}</style><g><marker id="mermaid-3_flowchart-v2-pointEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-3_flowchart-v2-pointStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="4.5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 5 L 10 10 L 10 0 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-3_flowchart-v2-circleEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="11" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-3_flowchart-v2-circleStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="-1" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-3_flowchart-v2-crossEnd" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="12" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-3_flowchart-v2-crossStart" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="-1" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><g class="root"><g class="clusters"></g><g class="edgePaths"><path d="M268,132.758L272.167,132.758C276.333,132.758,284.667,132.758,295.853,132.758C307.039,132.758,321.078,132.758,328.098,132.758L335.117,132.758" id="L_A_B_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_A_B_0" data-points="W3sieCI6MjY4LCJ5IjoxMzIuNzU3ODEyNX0seyJ4IjoyOTMsInkiOjEzMi43NTc4MTI1fSx7IngiOjMzOS4xMTcxODc1LCJ5IjoxMzIuNzU3ODEyNX1d" marker-end="url(#mermaid-3_flowchart-v2-pointEnd)"></path><path d="M517.049,92.924L533.783,83.27C550.517,73.616,583.985,54.308,606.931,44.654C629.878,35,642.302,35,648.514,35L654.727,35" id="L_B_C_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_B_C_0" data-points="W3sieCI6NTE3LjA0ODU2ODkzMDM1NywieSI6OTIuOTIzNTY4OTMwMzU2OTl9LHsieCI6NjE3LjQ1MzEyNSwieSI6MzV9LHsieCI6NjU4LjcyNjU2MjUsInkiOjM1fV0=" marker-end="url(#mermaid-3_flowchart-v2-pointEnd)"></path><path d="M517.049,172.592L533.783,182.246C550.517,191.9,583.985,211.208,606.628,220.862C629.271,230.516,641.089,230.516,646.997,230.516L652.906,230.516" id="L_B_D_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_B_D_0" data-points="W3sieCI6NTE3LjA0ODU2ODkzMDM1NywieSI6MTcyLjU5MjA1NjA2OTY0M30seyJ4Ijo2MTcuNDUzMTI1LCJ5IjoyMzAuNTE1NjI1fSx7IngiOjY1Ni45MDYyNSwieSI6MjMwLjUxNTYyNX1d" marker-end="url(#mermaid-3_flowchart-v2-pointEnd)"></path><path d="M893.938,230.516L898.104,230.516C902.271,230.516,910.604,230.516,918.271,230.516C925.938,230.516,932.938,230.516,936.438,230.516L939.938,230.516" id="L_D_E_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_D_E_0" data-points="W3sieCI6ODkzLjkzNzUsInkiOjIzMC41MTU2MjV9LHsieCI6OTE4LjkzNzUsInkiOjIzMC41MTU2MjV9LHsieCI6OTQzLjkzNzUsInkiOjIzMC41MTU2MjV9XQ==" marker-end="url(#mermaid-3_flowchart-v2-pointEnd)"></path><path d="M245.063,342.641L253.052,342.641C261.042,342.641,277.021,342.641,288.51,342.641C300,342.641,307,342.641,310.5,342.641L314,342.641" id="L_F_G_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_F_G_0" data-points="W3sieCI6MjQ1LjA2MjUsInkiOjM0Mi42NDA2MjV9LHsieCI6MjkzLCJ5IjozNDIuNjQwNjI1fSx7IngiOjMxOCwieSI6MzQyLjY0MDYyNX1d" marker-end="url(#mermaid-3_flowchart-v2-pointEnd)"></path></g><g class="edgeLabels"><g class="edgeLabel"><g class="label" data-id="L_A_B_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(617.453125, 35)"><g class="label" data-id="L_B_C_0" transform="translate(-14.453125, -12)"><foreignObject width="28.90625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>Yes</p></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(617.453125, 230.515625)"><g class="label" data-id="L_B_D_0" transform="translate(-9.6328125, -12)"><foreignObject width="19.265625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>No</p></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_D_E_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_F_G_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g></g><g class="nodes"><g class="node default" id="flowchart-A-0" transform="translate(138, 132.7578125)"><rect class="basic label-container" style="" x="-130" y="-39" width="260" height="78"></rect><g class="label" style="" transform="translate(-100, -24)"><rect></rect><foreignObject width="200" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table;white-space:break-spaces;line-height:1.5;max-width:200px;text-align:center;width:200px"><span class="nodeLabel"><p>Detect Change Conflict</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-B-1" transform="translate(448, 132.7578125)"><polygon points="108.8828125,0 217.765625,-108.8828125 108.8828125,-217.765625 0,-108.8828125" class="label-container" transform="translate(-108.3828125, 108.8828125)"></polygon><g class="label" style="" transform="translate(-81.8828125, -12)"><rect></rect><foreignObject width="163.765625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Different Fields?</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-C-3" transform="translate(775.421875, 35)"><rect class="basic label-container" style="" x="-116.6953125" y="-27" width="233.390625" height="54"></rect><g class="label" style="" transform="translate(-86.6953125, -12)"><rect></rect><foreignObject width="173.390625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Auto-Merge Changes</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-D-5" transform="translate(775.421875, 230.515625)"><polygon points="118.515625,0 237.03125,-118.515625 118.515625,-237.03125 0,-118.515625" class="label-container" transform="translate(-118.015625, 118.515625)"></polygon><g class="label" style="" transform="translate(-91.515625, -12)"><rect></rect><foreignObject width="183.03125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Same Field Conflict</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-E-7" transform="translate(1070.265625, 230.515625)"><rect class="basic label-container" style="" x="-126.328125" y="-39" width="252.65625" height="78"></rect><g class="label" style="" transform="translate(-96.328125, -24)"><rect></rect><foreignObject width="192.65625" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Apply Server Version<br/>Last-Write-Wins</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-F-8" transform="translate(138, 342.640625)"><rect class="basic label-container" style="" x="-107.0625" y="-27" width="214.125" height="54"></rect><g class="label" style="" transform="translate(-77.0625, -12)"><rect></rect><foreignObject width="154.125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Delete Operation</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-G-9" transform="translate(448, 342.640625)"><rect class="basic label-container" style="" x="-130" y="-51" width="260" height="102"></rect><g class="label" style="" transform="translate(-100, -36)"><rect></rect><foreignObject width="200" height="72"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table;white-space:break-spaces;line-height:1.5;max-width:200px;text-align:center;width:200px"><span class="nodeLabel"><p>Always Takes Priority<br/>Over Updates</p></span></div></foreignObject></g></g></g></g></g></svg></p>
<p>Dexie’s conflict resolution system is sophisticated and field-aware, meaning:</p>
<ul>
<li>Changes to different fields of the same record can be merged automatically</li>
<li>Conflicts in the same field use last-write-wins with server priority</li>
<li>Deletions always take precedence over updates to prevent “zombie” records</li>
</ul>
<p>This approach ensures smooth collaboration while maintaining data consistency across devices and users.</p>
<h2 id="conclusion">Conclusion<a class="heading-link" aria-label="Link to section" href="#conclusion"><span class="heading-link-icon">#</span></a></h2>
<p>This guide demonstrated building local-first applications with Dexie.js and Vue. For simpler applications like todo lists or note-taking apps, Dexie.js provides an excellent balance of features and simplicity. For more complex needs similar to Linear, consider building a custom sync engine.</p>
<p>Find the complete example code on <a href="https://github.com/alexanderop/vue-dexie" rel="noopener noreferrer" target="_blank">GitHub</a>.</p> </article> <script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).only=e;window.dispatchEvent(new Event("astro:only"));})();</script><astro-island uid="Z1XneyL" component-url="/_astro/presentation.C3Wa0mjp.js" component-export="VMarkBlogRenderer" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;containerSelector&quot;:[0,&quot;#article&quot;],&quot;class&quot;:[0,&quot;astro-vj4tpspi&quot;]}" ssr client="only" opts="{&quot;name&quot;:&quot;VMarkBlogRenderer&quot;,&quot;value&quot;:&quot;react&quot;}"></astro-island> <!-- Fullscreen Modal Container using native dialog --><dialog id="mermaid-modal" class="mermaid-modal" aria-label="Fullscreen diagram view"> <div class="mermaid-modal-content"> <button class="mermaid-modal-close" aria-label="Close fullscreen view" type="button"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <line x1="18" y1="6" x2="6" y2="18"></line> <line x1="6" y1="6" x2="18" y2="18"></line> </svg> </button> <div class="mermaid-modal-diagram"></div> <div class="mermaid-modal-hint">Press <kbd>Esc</kbd> or click outside to close</div> </div> </dialog>  <script type="module">const p=new Set;function g(){const e=document.getElementById("mermaid-modal"),c=e?.querySelector(".mermaid-modal-diagram"),f=e?.querySelector(".mermaid-modal-close");if(!e||!c)return;document.querySelectorAll('svg[id^="mermaid-"]').forEach(t=>{if(!t.id.match(/^mermaid-\d+$/)||p.has(t.id)||t.parentElement?.classList.contains("mermaid-fullscreen-wrapper")||t.closest(".mermaid-modal"))return;p.add(t.id);const n=document.createElement("div");n.className="mermaid-fullscreen-wrapper mermaid-clickable",n.setAttribute("tabindex","0"),n.setAttribute("role","button"),n.setAttribute("aria-label","Click to view diagram fullscreen"),t.parentElement?.insertBefore(n,t),n.appendChild(t);const o=document.createElement("div");o.className="mermaid-expand-icon",o.innerHTML=`
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
</li> <li class="astro-vj4tpspi">Small tips and trick</li> </ul> </div> <a href="https://alex-op-newsletter.beehiiv.com/subscribe?utm_source=blog&utm_medium=post&utm_campaign=post_building-local-first-apps-vue-dexie" target="_blank" rel="noopener noreferrer" id="newsletter-subscribe-button" class="inline-flex items-center justify-center gap-2 rounded-full bg-skin-accent px-6 py-3 text-base font-semibold text-skin-inverted shadow-md transition-all duration-200 hover:scale-[1.02] hover:transform hover:opacity-90 astro-vj4tpspi"> <svg class="h-5 w-5 fill-current astro-vj4tpspi" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg>
Subscribe Now
</a> <button id="newsletter-dismiss" data-post-slug="building-local-first-apps-vue-dexie" class="absolute right-3 top-3 rounded-full p-1 text-skin-base transition-all duration-200 hover:bg-skin-accent hover:bg-opacity-10 hover:text-skin-accent astro-vj4tpspi" aria-label="Close notification"> <svg class="h-5 w-5 astro-vj4tpspi" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class="astro-vj4tpspi"></path> </svg> </button> </div> </div> </div> <ul class="my-8 flex flex-wrap gap-2 astro-vj4tpspi"> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/vue/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-2"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">vue</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/dexie/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-3"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">dexie</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/indexeddb/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-4"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">indexeddb</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/local-first/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-5"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">local-first</span>   </a> </li>  </ul> <div class="flex flex-col-reverse items-center justify-between gap-6 sm:flex-row-reverse sm:items-end sm:gap-4 astro-vj4tpspi"> <button id="back-to-top" class="focus-outline whitespace-nowrap py-1 hover:opacity-75 astro-vj4tpspi"> <svg xmlns="http://www.w3.org/2000/svg" class="rotate-90 astro-vj4tpspi"> <path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg> <span class="astro-vj4tpspi">Back to Top</span> </button> <div class="social-icons astro-wkojbtzc"> <span class="italic astro-wkojbtzc">Share this post on:</span> <div class="text-center astro-wkojbtzc"> <a href="https://wa.me/?text=https://alexop.dev/posts/building-local-first-apps-vue-dexie/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via WhatsApp" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"></path>
      <path d="M9 10a0.5 .5 0 0 0 1 0v-1a0.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a0.5 .5 0 0 0 0 -1h-1a0.5 .5 0 0 0 0 1"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via WhatsApp</span> </a><a href="https://www.facebook.com/sharer.php?u=https://alexop.dev/posts/building-local-first-apps-vue-dexie/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Facebook" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"
    ></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on Facebook</span> </a><a href="https://x.com/intent/tweet?url=https://alexop.dev/posts/building-local-first-apps-vue-dexie/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Tweet this post" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Tweet this post</span> </a><a href="https://t.me/share/url?url=https://alexop.dev/posts/building-local-first-apps-vue-dexie/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via Telegram" target="_blank" rel="noopener noreferrer"> <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon-tabler"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"></path>
      </svg> <span class="sr-only astro-wkojbtzc">Share this post via Telegram</span> </a><a href="https://pinterest.com/pin/create/button/?url=https://alexop.dev/posts/building-local-first-apps-vue-dexie/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Pinterest" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <line x1="8" y1="20" x2="12" y2="11"></line>
      <path d="M10.7 14c.437 1.263 1.43 2 2.55 2c2.071 0 3.75 -1.554 3.75 -4a5 5 0 1 0 -9.7 1.7"></path>
      <circle cx="12" cy="12" r="9"></circle>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post on Pinterest</span> </a><a href="mailto:?subject=See%20this%20post&#38;body=https://alexop.dev/posts/building-local-first-apps-vue-dexie/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via email" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via email</span> </a><a href="https://www.linkedin.com/shareArticle?mini=true&url=https://alexop.dev/posts/building-local-first-apps-vue-dexie/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
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
</h2> <div class="md:grid-cols-3 grid grid-cols-1 gap-6 astro-vj4tpspi"> <a href="/posts/what-is-local-first-web-development/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">What is Local-first Web Development?</h3> <p class="related-post-description astro-vj4tpspi"> Explore the power of local-first web development and its impact on modern web applications. Learn how to build offline-capable, user-centric apps that prioritize data ownership and seamless synchronization. Discover the key principles and implementation steps for creating robust local-first web apps using Vue. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="italic text-sm">Updated:</span><span class="italic text-sm"><time dateTime="2024-11-28T15:22:00.000Z">Nov 28, 2024</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> local-first </span> </div> </div> </a><a href="/posts/how-to-persist-user-data-with-localstorage-in-vue/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">How to Persist User Data with LocalStorage in Vue</h3> <p class="related-post-description astro-vj4tpspi"> Learn how to efficiently store and manage user preferences like dark mode in Vue applications using LocalStorage. This guide covers basic operations, addresses common challenges, and provides type-safe solutions for robust development. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2024-04-21T15:22:00.000Z">Apr 21, 2024</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> vue </span> </div> </div> </a><a href="/posts/sqlite-vue3-offline-first-web-apps-guide/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">SQLite in Vue: Complete Guide to Building Offline-First Web Apps</h3> <p class="related-post-description astro-vj4tpspi"> Learn how to build offline-capable Vue 3 apps using SQLite and WebAssembly in 2024. Step-by-step tutorial includes code examples for database operations, query playground implementation, and best practices for offline-first applications. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2024-11-25T07:44:12.000Z">Nov 25, 2024</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> vue </span> </div> </div> </a> </div> </div> </main> <footer class="mt-auto astro-sz7xmlte"> <div class="max-w-5xl mx-auto px-4"> <hr class="border-skin-line" aria-hidden="true"> </div> <div class="footer-wrapper astro-sz7xmlte"> <div class="footer-content astro-sz7xmlte"> <div class="copyright-wrapper astro-sz7xmlte"> <span class="astro-sz7xmlte">Copyright &#169; 2026</span> <span class="separator astro-sz7xmlte">&nbsp;|&nbsp;</span> <span class="astro-sz7xmlte">All rights reserved.</span> </div> <div class="rss-prompt astro-sz7xmlte"> <a href="/rss.xml" class="rss-link group astro-sz7xmlte" title="Never miss a post - Subscribe via RSS" onclick="if (window.plausible) window.plausible('RSS Subscribe', { props: { location: 'footer' } })"> <div class="flex items-center gap-2 astro-sz7xmlte"> <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-skin-accent group-hover:animate-pulse astro-sz7xmlte"><path fill="currentColor" d="M19 20.001C19 11.729 12.271 5 4 5v2c7.168 0 13 5.832 13 13.001h2z" class="astro-sz7xmlte"></path><path fill="currentColor" d="M12 20.001h2C14 14.486 9.514 10 4 10v2c4.411 0 8 3.589 8 8.001z" class="astro-sz7xmlte"></path><circle cx="6" cy="18" r="2" fill="currentColor" class="astro-sz7xmlte"></circle> </svg> <span class="text-sm astro-sz7xmlte">Subscribe via RSS</span> </div> </a> </div> <div class="social-icons flex astro-upu6fzxr"> <a href="https://github.com/alexanderop" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title=" alexop.dev on Github" target="_blank" rel="noopener noreferrer"> <svg
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
    </script> </body> </html>  <script>(function(){const postSlug = "building-local-first-apps-vue-dexie";

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
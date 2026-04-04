# Source: https://alexop.dev/posts/vueuse_composables_style_guide

<!DOCTYPE html><html lang="en" class="scroll-smooth astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/posts/vueuse_composables_style_guide/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>Vue Composables Style Guide: Lessons from VueUse&#39;s Codebase | alexop.dev</title><meta name="title" content="Vue Composables Style Guide: Lessons from VueUse's Codebase | alexop.dev"><meta name="description" content="A practical guide for writing production-quality Vue 3 composables, distilled from studying VueUse's patterns for SSR safety, cleanup, and TypeScript."><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="Vue Composables Style Guide: Lessons from VueUse's Codebase | alexop.dev"><meta property="og:description" content="A practical guide for writing production-quality Vue 3 composables, distilled from studying VueUse's patterns for SSR safety, cleanup, and TypeScript."><meta property="og:url" content="https://alexop.dev/posts/vueuse_composables_style_guide/"><meta property="og:image" content="https://alexop.dev/posts/vue-composables-style-guide-lessons-from-vue-uses-codebase/index.png"><meta property="og:type" content="article"><!-- Article Published/Modified time --><meta property="article:published_time" content="2025-12-13T00:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/posts/vueuse_composables_style_guide/"><meta property="twitter:title" content="Vue Composables Style Guide: Lessons from VueUse's Codebase | alexop.dev"><meta property="twitter:description" content="A practical guide for writing production-quality Vue 3 composables, distilled from studying VueUse's patterns for SSR safety, cleanup, and TypeScript."><meta property="twitter:image" content="https://alexop.dev/posts/vue-composables-style-guide-lessons-from-vue-uses-codebase/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"Vue Composables Style Guide: Lessons from VueUse's Codebase | alexop.dev","description":"A practical guide for writing production-quality Vue 3 composables, distilled from studying VueUse's patterns for SSR safety, cleanup, and TypeScript.","image":"https://alexop.dev/posts/vue-composables-style-guide-lessons-from-vue-uses-codebase/index.png","datePublished":"2025-12-13T00:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
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
</style><style>[data-astro-transition-scope="astro-plk3gbjq-1"] { view-transition-name: vue-composables-style-guide-lessons-from-vue-uses-codebase; }@layer astro { ::view-transition-old(vue-composables-style-guide-lessons-from-vue-uses-codebase) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(vue-composables-style-guide-lessons-from-vue-uses-codebase) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(vue-composables-style-guide-lessons-from-vue-uses-codebase) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(vue-composables-style-guide-lessons-from-vue-uses-codebase) { 
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
	animation-name: astroFadeIn; }</style><style>:root{--color-skin-card: rgb(var(--color-card));--color-skin-card-muted: rgb(var(--color-card-muted));--color-skin-border: rgb(var(--color-border));--color-skin-text-base: rgb(var(--color-text-base));--color-skin-accent: rgb(var(--color-accent));--color-skin-note: rgb(59, 130, 246);--color-skin-tip: rgb(16, 185, 129);--color-skin-caution: rgb(245, 158, 11);--color-skin-danger: rgb(239, 68, 68);--color-skin-info: rgb(99, 102, 241)}.aside:where(.astro-37uy2q7c){background-color:var(--color-skin-card);border-left:4px solid;border-radius:.5rem;box-shadow:0 4px 6px -1px #0000001a,0 2px 4px -1px #0000000f;margin:1.5rem 0;transition:all .3s ease}.aside:where(.astro-37uy2q7c):hover{box-shadow:0 10px 15px -3px #0000001a,0 4px 6px -2px #0000000d}.aside-content:where(.astro-37uy2q7c){padding:1rem 1.5rem}.aside-title:where(.astro-37uy2q7c){display:flex;align-items:center;font-weight:700;font-size:1.1rem;margin-bottom:.75rem}.aside-emoji:where(.astro-37uy2q7c){font-size:1.4rem;margin-right:.75rem}.aside-body:where(.astro-37uy2q7c){color:var(--color-skin-text-base);font-size:.95rem;line-height:1.6}.aside-note:where(.astro-37uy2q7c){background-color:rgba(var(--color-skin-note),.1);border-left-color:var(--color-skin-note)}.aside-note:where(.astro-37uy2q7c) .aside-title:where(.astro-37uy2q7c){color:var(--color-skin-note)}.aside-tip:where(.astro-37uy2q7c){background-color:rgba(var(--color-skin-tip),.1);border-left-color:var(--color-skin-tip)}.aside-tip:where(.astro-37uy2q7c) .aside-title:where(.astro-37uy2q7c){color:var(--color-skin-tip)}.aside-caution:where(.astro-37uy2q7c){background-color:rgba(var(--color-skin-caution),.1);border-left-color:var(--color-skin-caution)}.aside-caution:where(.astro-37uy2q7c) .aside-title:where(.astro-37uy2q7c){color:var(--color-skin-caution)}.aside-danger:where(.astro-37uy2q7c){background-color:rgba(var(--color-skin-danger),.1);border-left-color:var(--color-skin-danger)}.aside-danger:where(.astro-37uy2q7c) .aside-title:where(.astro-37uy2q7c){color:var(--color-skin-danger)}.aside-info:where(.astro-37uy2q7c){background-color:rgba(var(--color-skin-info),.1);border-left-color:var(--color-skin-info)}.aside-info:where(.astro-37uy2q7c) .aside-title:where(.astro-37uy2q7c){color:var(--color-skin-info)}
</style><style>.file-tree__item:where(.astro-o25vlg2d){margin:0;padding:0;position:relative}.file-tree__item:where(.astro-o25vlg2d):before{content:"";position:absolute;left:calc(.5rem + (var(--level) * 1.25rem));top:0;bottom:0;width:1px;background:rgba(var(--color-text-base),.15)}.file-tree__item:where(.astro-o25vlg2d):last-child:before{bottom:50%}.file-tree__item:where(.astro-o25vlg2d):after{content:"";position:absolute;left:calc(.5rem + (var(--level) * 1.25rem));top:50%;width:.75rem;height:1px;background:rgba(var(--color-text-base),.15)}.file-tree__folder:where(.astro-o25vlg2d){margin:0;padding:0}.file-tree__folder:where(.astro-o25vlg2d)>summary:where(.astro-o25vlg2d){list-style:none;cursor:pointer;display:flex;gap:.5rem;align-items:center;padding:.2rem .5rem .2rem calc(1.5rem + (var(--level) * 1.25rem));border-radius:.25rem;transition:background-color .15s ease;line-height:1.6;position:relative}.file-tree__folder:where(.astro-o25vlg2d)>summary:where(.astro-o25vlg2d):hover{background:rgba(var(--color-text-base),.05)}.file-tree__folder:where(.astro-o25vlg2d)[open]>summary:where(.astro-o25vlg2d) .file-tree__caret:where(.astro-o25vlg2d){transform:rotate(90deg)}.file-tree__folder:where(.astro-o25vlg2d):not([open])>summary:where(.astro-o25vlg2d) .file-tree__caret:where(.astro-o25vlg2d){transform:rotate(0)}.file-tree__folder:where(.astro-o25vlg2d)>summary:where(.astro-o25vlg2d)::-webkit-details-marker{display:none}.file-tree__list:where(.astro-o25vlg2d){list-style:none;margin:0;padding:0}.file-tree__file:where(.astro-o25vlg2d){display:flex;gap:.5rem;align-items:center;padding:.2rem .5rem .2rem calc(1.5rem + (var(--level) * 1.25rem));border-radius:.25rem;text-decoration:none;color:inherit;transition:background-color .15s ease;line-height:1.6;position:relative}.file-tree__file:where(.astro-o25vlg2d):hover{background:rgba(var(--color-text-base),.05)}a:where(.astro-o25vlg2d).file-tree__file:hover .file-tree__name:where(.astro-o25vlg2d){color:rgb(var(--color-accent))}.file-tree__icon:where(.astro-o25vlg2d){width:1rem;height:1rem;flex-shrink:0;color:rgba(var(--color-text-base),.4);display:inline-flex;align-items:center;justify-content:center}.file-tree__icon--file:where(.astro-o25vlg2d){color:rgba(var(--color-text-base),.4)}.file-tree__icon--colored:where(.astro-o25vlg2d){color:inherit}.file-tree__icon--text:where(.astro-o25vlg2d){font-weight:600;font-size:.875rem;display:inline-flex;align-items:center;justify-content:center;width:1rem;height:1rem}.file-tree__name:where(.astro-o25vlg2d){white-space:nowrap;transition:color .15s ease;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,Liberation Mono,Courier New,monospace}.file-tree__comment:where(.astro-o25vlg2d){color:rgba(var(--color-text-base),.5);font-style:italic;margin-left:.5rem;white-space:nowrap;font-size:.9em}.file-tree__caret:where(.astro-o25vlg2d){width:.75rem;height:.75rem;transition:transform .2s ease;flex-shrink:0;color:rgba(var(--color-text-base),.5);font-size:.625rem;display:inline-flex;align-items:center;justify-content:center;transform-origin:center}
</style><style>.file-tree:where(.astro-htwbjus4){font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,Liberation Mono,Courier New,monospace;font-size:.8125rem;background:rgb(var(--color-card));color:rgb(var(--color-text-base));border:1px solid rgba(var(--color-border),.5);border-radius:.5rem;padding:.75rem;margin:1.5rem 0;overflow-x:auto}.file-tree__list:where(.astro-htwbjus4){list-style:none;margin:0;padding:0}.file-tree__list:where(.astro-htwbjus4)>li:where(.astro-htwbjus4):first-child:before,.file-tree__list:where(.astro-htwbjus4)>li:where(.astro-htwbjus4):first-child:after{display:none}.file-tree:where(.astro-htwbjus4)::-webkit-scrollbar{height:.5rem}.file-tree:where(.astro-htwbjus4)::-webkit-scrollbar-track{background:rgb(var(--color-fill))}.file-tree:where(.astro-htwbjus4)::-webkit-scrollbar-thumb{background:rgb(var(--color-border));border-radius:.25rem}.file-tree:where(.astro-htwbjus4)::-webkit-scrollbar-thumb:hover{background:rgb(var(--color-card-muted))}
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <div class="mx-auto flex w-full max-w-5xl justify-start px-2 astro-vj4tpspi"> <button class="focus-outline mb-2 mt-8 flex hover:opacity-75 astro-vj4tpspi" onclick="(() => (history.length === 1) ? window.location = '/' : history.back())()"> <svg xmlns="http://www.w3.org/2000/svg" class="astro-vj4tpspi"><path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg><span class="astro-vj4tpspi">Go back</span> </button> </div> <main data-pagefind-body id="main-content" class="relative astro-vj4tpspi"> <h1 class="post-title astro-vj4tpspi" data-astro-transition-scope="astro-plk3gbjq-1">Vue Composables Style Guide: Lessons from VueUse&#39;s Codebase</h1> <div class="my-2 flex items-center justify-between astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-100 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-base"><time dateTime="2025-12-13T00:00:00.000Z">Dec 13, 2025</time><span class="sr-only"> at </span></span></div> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="Z2tWkbe" prefix="r3" component-url="/_astro/PostCopyButton.-PGtk4At.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;title&quot;:[0,&quot;Vue Composables Style Guide: Lessons from VueUse&#39;s Codebase&quot;],&quot;content&quot;:[0,&quot;import Aside from \&quot;@features/mdx-components/components/Aside.astro\&quot;;\nimport FileTree from \&quot;@features/filetree/components/FileTree.astro\&quot;;\nimport InternalLink from \&quot;@features/mdx-components/components/InternalLink.astro\&quot;;\n\nI was studying VueUse&#39;s codebase to understand how they structure their composables. VueUse has become the de facto standard library for Vue utilities, and I wanted to understand the patterns that make their composables so reliable. After diving deep into their source code, I distilled the key patterns into this style guide.\n\nWhether you&#39;re building your own composable library or just want to write better code, these patterns will help you create maintainable, type-safe, and SSR-compatible composition utilities.\n\nIf you&#39;re new to Vue composables, I recommend starting with my earlier post &lt;InternalLink slug=\&quot;mastering-vue-3-composables-a-comprehensive-style-guide\&quot;&gt;Mastering Vue 3 Composables: A Comprehensive Style Guide&lt;/InternalLink&gt;, which covers many of the same patterns from a beginner-friendly perspective.\n\n## Quick Summary\n\nThis guide covers patterns for writing production-quality Vue 3 composables:\n\n- **Project structure** and naming conventions\n- **Ref type selection** (shallowRef vs ref)\n- **Flexible inputs** with `MaybeRefOrGetter`\n- **SSR safety** patterns for server-side rendering\n- **Cleanup and memory management** with auto-cleanup utilities\n- **Controllable composables** (pausable, stoppable patterns)\n- **TypeScript best practices** for full type inference\n- **Testing strategies** - see &lt;InternalLink slug=\&quot;how-to-test-vue-composables\&quot;&gt;How to Test Vue Composables&lt;/InternalLink&gt;\n\n## Table of Contents\n\n---\n\n## 1. Getting Started\n\n### What Makes a Good Composable?\n\nA well-designed composable should be:\n\n- **Focused**: Does one thing well\n- **Flexible**: Accepts refs, getters, or plain values\n- **Safe**: Works in SSR, handles cleanup automatically\n- **Typed**: Full TypeScript support with inference\n- **Testable**: Easy to unit test in isolation\n\n### Minimal Example\n\n```typescript\nimport { shallowRef, toValue, type MaybeRefOrGetter } from &#39;vue&#39;\n\nexport function useCounter(initialValue: MaybeRefOrGetter&lt;number&gt; = 0) {\n  const count = shallowRef(toValue(initialValue))\n\n  const increment = () =&gt; count.value++\n  const decrement = () =&gt; count.value--\n  const reset = () =&gt; count.value = toValue(initialValue)\n\n  return { count, increment, decrement, reset }\n}\n```\n\nThis simple example already demonstrates several VueUse patterns: using `shallowRef` for primitives, accepting `MaybeRefOrGetter` for flexible inputs, and returning an object with reactive state and methods.\n\n---\n\n## 2. Project Structure\n\n### Recommended Layout\n\n&lt;FileTree\n  tree={[\n    {\n      name: \&quot;src/composables\&quot;,\n      open: true,\n      children: [\n        {\n          name: \&quot;useCounter\&quot;,\n          open: true,\n          children: [\n            { name: \&quot;index.ts\&quot;, comment: \&quot;Implementation\&quot; },\n            { name: \&quot;index.test.ts\&quot;, comment: \&quot;Tests\&quot; },\n            { name: \&quot;types.ts\&quot;, comment: \&quot;Types (optional)\&quot; },\n          ],\n        },\n        {\n          name: \&quot;useFetch\&quot;,\n          children: [\n            { name: \&quot;index.ts\&quot; },\n            { name: \&quot;index.test.ts\&quot; },\n          ],\n        },\n        {\n          name: \&quot;utils\&quot;,\n          children: [\n            { name: \&quot;ssr.ts\&quot;, comment: \&quot;SSR utilities\&quot; },\n            { name: \&quot;types.ts\&quot;, comment: \&quot;Shared types\&quot; },\n            { name: \&quot;cleanup.ts\&quot;, comment: \&quot;Cleanup utilities\&quot; },\n          ],\n        },\n        { name: \&quot;index.ts\&quot;, comment: \&quot;Public exports\&quot; },\n      ],\n    },\n  ]}\n/&gt;\n\n### Export Pattern\n\n```typescript\n// src/composables/index.ts\nexport { useCounter } from &#39;./useCounter&#39;\nexport { useFetch } from &#39;./useFetch&#39;\nexport type { UseCounterReturn, UseCounterOptions } from &#39;./useCounter&#39;\nexport type { UseFetchReturn, UseFetchOptions } from &#39;./useFetch&#39;\n```\n\n&lt;Aside type=\&quot;caution\&quot; title=\&quot;Important\&quot;&gt;\nUse named exports only. Never use default exports for composables. This ensures better tree-shaking and clearer imports.\n&lt;/Aside&gt;\n\nFor more on project organization, check out &lt;InternalLink slug=\&quot;how-to-structure-vue-projects\&quot;&gt;How to Structure Vue Projects&lt;/InternalLink&gt;.\n\n---\n\n## 3. Naming Conventions\n\n### Function Names\n\n| Prefix | Use Case | Example |\n|--------|----------|---------|\n| `use` | Standard composables | `useMouse`, `useStorage`, `useFetch` |\n| `create` | Factory functions that return composables | `createSharedState`, `createEventHook` |\n| `on` | Event listener composables | `onClickOutside`, `onKeyPress` |\n| `try` | Safe operations that may fail silently | `tryOnMounted`, `tryOnCleanup` |\n\n### Type Names\n\n```typescript\n// Options: Use{Name}Options\nexport interface UseStorageOptions {\n  deep?: boolean\n  listenToChanges?: boolean\n}\n\n// Return type: Use{Name}Return\nexport interface UseStorageReturn&lt;T&gt; {\n  data: Ref&lt;T&gt;\n  set: (value: T) =&gt; void\n  remove: () =&gt; void\n}\n\n// Inferred type shorthand\nexport type UseStorageReturnType&lt;T&gt; = ReturnType&lt;typeof useStorage&lt;T&gt;&gt;\n```\n\n---\n\n## 4. Choosing the Right Ref Type\n\nThis is one of the most important decisions when writing composables. VueUse consistently follows this pattern:\n\n```mermaid\nflowchart TD\n    A[What type of data?] --&gt; B{Primitive?}\n    B --&gt;|Yes| C[shallowRef]\n    B --&gt;|No| D{Will you mutate nested properties?}\n    D --&gt;|Yes| E[ref - deep reactivity]\n    D --&gt;|No - replace whole object| F[shallowRef]\n\n    style C fill:#22c55e,color:#fff\n    style E fill:#3b82f6,color:#fff\n    style F fill:#22c55e,color:#fff\n```\n\n### shallowRef - For Primitives and Replaced Objects\n\n```typescript\n// Primitives\nconst count = shallowRef(0)\nconst isActive = shallowRef(false)\nconst name = shallowRef(&#39;&#39;)\n\n// Objects that get replaced, not mutated\nconst user = shallowRef&lt;User | null&gt;(null)\nconst response = shallowRef&lt;Response | null&gt;(null)\n\n// Usage: Replace the whole object\nuser.value = { name: &#39;John&#39;, age: 30 }  // Triggers reactivity\n```\n\n### ref - For Deep Mutations\n\n```typescript\n// Objects with nested mutations\nconst form = ref({\n  user: { name: &#39;&#39;, email: &#39;&#39; },\n  settings: { theme: &#39;light&#39; }\n})\n\n// Usage: Mutate nested properties\nform.value.user.name = &#39;John&#39;  // Triggers reactivity\nform.value.settings.theme = &#39;dark&#39;  // Triggers reactivity\n```\n\n### Let Users Choose\n\nFor composables storing user data, let them decide:\n\n```typescript\nexport interface UseStateOptions {\n  /**\n   * Use shallow reactivity for better performance with large objects\n   * @default false\n   */\n  shallow?: boolean\n}\n\nexport function useState&lt;T&gt;(initialValue: T, options: UseStateOptions = {}) {\n  const { shallow = false } = options\n\n  const state = shallow\n    ? shallowRef(initialValue)\n    : ref(initialValue)\n\n  return { state }\n}\n```\n\n---\n\n## 5. Flexible Inputs\n\n### Accept Refs, Getters, or Plain Values\n\nUse `MaybeRefOrGetter&lt;T&gt;` to make your composables flexible:\n\n```typescript\nimport { toValue, type MaybeRefOrGetter } from &#39;vue&#39;\n\nexport function useTitle(title: MaybeRefOrGetter&lt;string&gt;) {\n  // toValue() handles all input types:\n  // - Plain value: &#39;Hello&#39; → &#39;Hello&#39;\n  // - Ref: ref(&#39;Hello&#39;) → &#39;Hello&#39;\n  // - Getter: () =&gt; &#39;Hello&#39; → &#39;Hello&#39;\n\n  watchEffect(() =&gt; {\n    document.title = toValue(title)\n  })\n}\n\n// All of these work:\nuseTitle(&#39;Static Title&#39;)\nuseTitle(ref(&#39;Reactive Title&#39;))\nuseTitle(() =&gt; `Page ${currentPage.value}`)\nuseTitle(computed(() =&gt; `${userName.value}&#39;s Profile`))\n```\n\n### Reactive Configuration\n\nFor options that should be reactive:\n\n```typescript\nexport interface UseIntervalOptions {\n  interval?: MaybeRefOrGetter&lt;number&gt;\n  immediate?: boolean\n}\n\nexport function useInterval(\n  callback: () =&gt; void,\n  options: UseIntervalOptions = {}\n) {\n  const { interval = 1000, immediate = true } = options\n\n  // Watch the interval for changes\n  watch(\n    () =&gt; toValue(interval),\n    (ms) =&gt; {\n      clearInterval(timer)\n      if (ms &gt; 0) {\n        timer = setInterval(callback, ms)\n      }\n    },\n    { immediate }\n  )\n}\n\n// Interval can change reactively\nconst delay = ref(1000)\nuseInterval(() =&gt; console.log(&#39;tick&#39;), { interval: delay })\ndelay.value = 500  // Interval updates automatically\n```\n\n---\n\n## 6. Designing Options\n\n### Structure\n\n```typescript\nexport interface UseStorageOptions&lt;T&gt; {\n  /**\n   * Storage type to use\n   * @default &#39;local&#39;\n   */\n  storage?: &#39;local&#39; | &#39;session&#39;\n\n  /**\n   * Custom serializer for complex data\n   * @default JSON.stringify/parse\n   */\n  serializer?: {\n    read: (raw: string) =&gt; T\n    write: (value: T) =&gt; string\n  }\n\n  /**\n   * Sync across browser tabs\n   * @default true\n   */\n  listenToStorageChanges?: boolean\n\n  /**\n   * Called when an error occurs\n   */\n  onError?: (error: Error) =&gt; void\n}\n```\n\n### Rules for Options\n\n1. **Document every option** with JSDoc\n2. **Provide sensible defaults** using `@default`\n3. **Use callbacks** for events (`onError`, `onSuccess`, `onChange`)\n4. **Group related options** in nested objects if complex\n\n### Extending Base Interfaces\n\nCreate reusable option interfaces:\n\n```typescript\n// src/composables/utils/types.ts\n\n/** Options for composables that use window */\nexport interface ConfigurableWindow {\n  /**\n   * Custom window instance (useful for iframes or testing)\n   * @default window\n   */\n  window?: Window\n}\n\n/** Options for composables that use document */\nexport interface ConfigurableDocument {\n  /**\n   * Custom document instance\n   * @default document\n   */\n  document?: Document\n}\n\n// Usage in composables\nexport interface UseEventListenerOptions extends ConfigurableWindow {\n  capture?: boolean\n  passive?: boolean\n}\n```\n\n---\n\n## 7. Return Values\n\n### Object Return (Recommended for Multiple Values)\n\n```typescript\nexport interface UseMouseReturn {\n  /** Current X position */\n  x: Readonly&lt;Ref&lt;number&gt;&gt;\n  /** Current Y position */\n  y: Readonly&lt;Ref&lt;number&gt;&gt;\n  /** Source of the last event */\n  sourceType: Readonly&lt;Ref&lt;&#39;mouse&#39; | &#39;touch&#39; | null&gt;&gt;\n}\n\nexport function useMouse(): UseMouseReturn {\n  const x = shallowRef(0)\n  const y = shallowRef(0)\n  const sourceType = shallowRef&lt;&#39;mouse&#39; | &#39;touch&#39; | null&gt;(null)\n\n  // ... implementation\n\n  return {\n    x: readonly(x),\n    y: readonly(y),\n    sourceType: readonly(sourceType),\n  }\n}\n```\n\n### Single Ref Return (For Simple Composables)\n\n```typescript\nexport function useOnline(): Readonly&lt;Ref&lt;boolean&gt;&gt; {\n  const isOnline = shallowRef(navigator.onLine)\n\n  // ... implementation\n\n  return readonly(isOnline)\n}\n```\n\n### Tuple Return (When Destructuring Order Matters)\n\n```typescript\nexport function useToggle(\n  initialValue = false\n): [Ref&lt;boolean&gt;, (value?: boolean) =&gt; void] {\n  const state = shallowRef(initialValue)\n\n  const toggle = (value?: boolean) =&gt; {\n    state.value = value ?? !state.value\n  }\n\n  return [state, toggle]\n}\n\n// Usage\nconst [isOpen, toggleOpen] = useToggle()\n```\n\n### Making Composables Awaitable\n\nFor async composables, implement `PromiseLike`:\n\n```typescript\nexport function useFetch&lt;T&gt;(url: MaybeRefOrGetter&lt;string&gt;) {\n  const data = shallowRef&lt;T | null&gt;(null)\n  const isLoading = shallowRef(true)\n  const error = shallowRef&lt;Error | null&gt;(null)\n\n  const execute = async () =&gt; {\n    isLoading.value = true\n    try {\n      const response = await fetch(toValue(url))\n      data.value = await response.json()\n    } catch (e) {\n      error.value = e as Error\n    } finally {\n      isLoading.value = false\n    }\n  }\n\n  execute()\n\n  const shell = { data, isLoading, error, execute }\n\n  return {\n    ...shell,\n    // Make it awaitable\n    then&lt;TResult&gt;(\n      onFulfilled?: (value: typeof shell) =&gt; TResult\n    ): Promise&lt;TResult&gt; {\n      return new Promise((resolve) =&gt; {\n        watch(isLoading, (loading) =&gt; {\n          if (!loading) resolve(onFulfilled?.(shell) as TResult)\n        }, { immediate: true })\n      })\n    }\n  }\n}\n\n// Can be used both ways:\nconst { data, isLoading } = useFetch(&#39;/api/users&#39;)\n\n// Or awaited:\nconst { data } = await useFetch(&#39;/api/users&#39;)\nconsole.log(data.value)  // Data is ready\n```\n\n---\n\n## 8. SSR Safety\n\n### The Problem\n\nBrowser APIs (`window`, `document`, `localStorage`) don&#39;t exist on the server. Accessing them during SSR causes errors.\n\nFor a deep dive into this topic, see &lt;InternalLink slug=\&quot;how-vueuse-solves-ssr-window-errors-vue-applications\&quot;&gt;How VueUse Solves SSR Window Errors&lt;/InternalLink&gt;.\n\n```mermaid\nsequenceDiagram\n    participant B as Browser\n    participant S as Server (Node.js)\n    B-&gt;&gt;S: Request page\n    S--&gt;&gt;S: Run Vue code (no window!)\n    Note over S: window, document undefined\n    S--&gt;&gt;B: Send HTML\n    B--&gt;&gt;B: Hydrate app (has window)\n    Note over B: Browser APIs available\n```\n\n### Solution: Create SSR Utilities\n\n```typescript\n// src/composables/utils/ssr.ts\n\n/**\n * Check if code is running in browser\n */\nexport const isClient = typeof window !== &#39;undefined&#39;\n\n/**\n * Check if code is running on server\n */\nexport const isServer = !isClient\n\n/**\n * Safe window reference (undefined on server)\n */\nexport const defaultWindow = isClient ? window : undefined\n\n/**\n * Safe document reference (undefined on server)\n */\nexport const defaultDocument = isClient ? document : undefined\n\n/**\n * Safe localStorage reference (undefined on server)\n */\nexport const defaultStorage = isClient ? localStorage : undefined\n```\n\n### Using SSR Utilities\n\n```typescript\nimport { defaultWindow, type ConfigurableWindow } from &#39;../utils/ssr&#39;\n\nexport interface UseWindowSizeOptions extends ConfigurableWindow {\n  initialWidth?: number\n  initialHeight?: number\n}\n\nexport function useWindowSize(options: UseWindowSizeOptions = {}) {\n  const {\n    window = defaultWindow,\n    initialWidth = Infinity,\n    initialHeight = Infinity,\n  } = options\n\n  const width = shallowRef(initialWidth)\n  const height = shallowRef(initialHeight)\n\n  const update = () =&gt; {\n    // Guard: Only run if window exists\n    if (window) {\n      width.value = window.innerWidth\n      height.value = window.innerHeight\n    }\n  }\n\n  // Only set up listeners on client\n  if (window) {\n    update()\n    window.addEventListener(&#39;resize&#39;, update)\n\n    onUnmounted(() =&gt; {\n      window.removeEventListener(&#39;resize&#39;, update)\n    })\n  }\n\n  return { width, height }\n}\n```\n\n### Feature Detection\n\nCreate a utility to safely check for browser features:\n\n```typescript\nexport function useSupported(check: () =&gt; boolean): Readonly&lt;Ref&lt;boolean&gt;&gt; {\n  const isSupported = shallowRef(false)\n\n  onMounted(() =&gt; {\n    isSupported.value = check()\n  })\n\n  return readonly(isSupported)\n}\n\n// Usage\nexport function useClipboard() {\n  const isSupported = useSupported(\n    () =&gt; navigator &amp;&amp; &#39;clipboard&#39; in navigator\n  )\n\n  const copy = async (text: string) =&gt; {\n    if (!isSupported.value) {\n      console.warn(&#39;Clipboard API not supported&#39;)\n      return false\n    }\n    // ... implementation\n  }\n\n  return { isSupported, copy }\n}\n```\n\n---\n\n## 9. Cleanup and Memory Management\n\n### The Problem\n\nEvent listeners, timers, and observers must be cleaned up to prevent memory leaks.\n\n```mermaid\nflowchart LR\n    A[Composable Created] --&gt; B[Register Resources]\n    B --&gt; C[Listeners, Timers, etc.]\n    C --&gt; D{Component Unmounted?}\n    D --&gt;|Yes| E[Cleanup Required]\n    D --&gt;|No| C\n    E --&gt; F[Remove Listeners]\n    E --&gt; G[Clear Timers]\n    E --&gt; H[Disconnect Observers]\n\n    style E fill:#ef4444,color:#fff\n    style F fill:#22c55e,color:#fff\n    style G fill:#22c55e,color:#fff\n    style H fill:#22c55e,color:#fff\n```\n\n### Solution: Auto-Cleanup Utility\n\n```typescript\n// src/composables/utils/cleanup.ts\nimport { getCurrentScope, onScopeDispose } from &#39;vue&#39;\n\n/**\n * Register a cleanup function that runs when the scope is disposed.\n * Safe to call outside of component context.\n *\n * @returns true if cleanup was registered, false otherwise\n */\nexport function tryOnCleanup(fn: () =&gt; void): boolean {\n  if (getCurrentScope()) {\n    onScopeDispose(fn)\n    return true\n  }\n  return false\n}\n\n/**\n * Safe onMounted that doesn&#39;t error outside component context\n */\nexport function tryOnMounted(fn: () =&gt; void): void {\n  if (getCurrentScope()) {\n    onMounted(fn)\n  }\n}\n```\n\n### Using Auto-Cleanup\n\n```typescript\nimport { tryOnCleanup } from &#39;../utils/cleanup&#39;\n\nexport function useInterval(callback: () =&gt; void, ms: number) {\n  let timer: ReturnType&lt;typeof setInterval&gt; | null = null\n\n  const start = () =&gt; {\n    stop()\n    timer = setInterval(callback, ms)\n  }\n\n  const stop = () =&gt; {\n    if (timer) {\n      clearInterval(timer)\n      timer = null\n    }\n  }\n\n  start()\n\n  // Automatically stops when component unmounts\n  tryOnCleanup(stop)\n\n  return { start, stop }\n}\n```\n\n### Event Listener Composable with Auto-Cleanup\n\n```typescript\nexport function useEventListener&lt;K extends keyof WindowEventMap&gt;(\n  event: K,\n  handler: (event: WindowEventMap[K]) =&gt; void,\n  options?: AddEventListenerOptions &amp; ConfigurableWindow\n): () =&gt; void {\n  const { window = defaultWindow, ...listenerOptions } = options ?? {}\n\n  let cleanup = () =&gt; {}\n\n  if (window) {\n    window.addEventListener(event, handler, listenerOptions)\n    cleanup = () =&gt; window.removeEventListener(event, handler, listenerOptions)\n  }\n\n  tryOnCleanup(cleanup)\n\n  return cleanup\n}\n```\n\n---\n\n## 10. Controllable Composables\n\n### Pausable Pattern\n\n```mermaid\nstateDiagram-v2\n    [*] --&gt; Active: immediate=true\n    [*] --&gt; Paused: immediate=false\n    Active --&gt; Paused: pause()\n    Paused --&gt; Active: resume()\n    Active --&gt; [*]: cleanup\n    Paused --&gt; [*]: cleanup\n```\n\nFor composables that can be paused and resumed:\n\n```typescript\nexport interface Pausable {\n  /** Whether the composable is currently active */\n  isActive: Readonly&lt;Ref&lt;boolean&gt;&gt;\n  /** Pause the composable */\n  pause: () =&gt; void\n  /** Resume the composable */\n  resume: () =&gt; void\n}\n\nexport interface UseIntervalOptions {\n  /** Start immediately */\n  immediate?: boolean\n  /** Call callback immediately when starting */\n  immediateCallback?: boolean\n}\n\nexport function useIntervalFn(\n  callback: () =&gt; void,\n  interval: MaybeRefOrGetter&lt;number&gt; = 1000,\n  options: UseIntervalOptions = {}\n): Pausable {\n  const { immediate = true, immediateCallback = false } = options\n\n  const isActive = shallowRef(false)\n  let timer: ReturnType&lt;typeof setInterval&gt; | null = null\n\n  function clean() {\n    if (timer) {\n      clearInterval(timer)\n      timer = null\n    }\n  }\n\n  function pause() {\n    isActive.value = false\n    clean()\n  }\n\n  function resume() {\n    const ms = toValue(interval)\n    if (ms &lt;= 0) return\n\n    isActive.value = true\n    if (immediateCallback) callback()\n\n    clean()\n    timer = setInterval(callback, ms)\n  }\n\n  if (immediate) resume()\n\n  tryOnCleanup(pause)\n\n  return {\n    isActive: readonly(isActive),\n    pause,\n    resume,\n  }\n}\n\n// Usage\nconst { isActive, pause, resume } = useIntervalFn(() =&gt; {\n  console.log(&#39;tick&#39;)\n}, 1000)\n\npause()   // Stop ticking\nresume()  // Start again\n```\n\n### Stoppable Pattern\n\nFor one-way stopping (e.g., timeouts, one-time operations):\n\n```typescript\nexport interface Stoppable {\n  /** Whether the operation is pending */\n  isPending: Readonly&lt;Ref&lt;boolean&gt;&gt;\n  /** Stop the operation */\n  stop: () =&gt; void\n}\n\nexport function useTimeoutFn(\n  callback: () =&gt; void,\n  interval: MaybeRefOrGetter&lt;number&gt;,\n  options: { immediate?: boolean } = {}\n): Stoppable &amp; { start: () =&gt; void } {\n  const { immediate = true } = options\n\n  const isPending = shallowRef(false)\n  let timer: ReturnType&lt;typeof setTimeout&gt; | null = null\n\n  function stop() {\n    isPending.value = false\n    if (timer) {\n      clearTimeout(timer)\n      timer = null\n    }\n  }\n\n  function start() {\n    stop()\n    isPending.value = true\n    timer = setTimeout(() =&gt; {\n      isPending.value = false\n      timer = null\n      callback()\n    }, toValue(interval))\n  }\n\n  if (immediate) start()\n\n  tryOnCleanup(stop)\n\n  return {\n    isPending: readonly(isPending),\n    stop,\n    start,\n  }\n}\n```\n\n---\n\n## 11. Error Handling\n\n### Graceful Degradation\n\n```typescript\nexport function useGeolocation() {\n  const isSupported = useSupported(\n    () =&gt; navigator &amp;&amp; &#39;geolocation&#39; in navigator\n  )\n\n  const coords = shallowRef&lt;GeolocationCoordinates | null&gt;(null)\n  const error = shallowRef&lt;GeolocationPositionError | null&gt;(null)\n\n  function update() {\n    if (!isSupported.value) return\n\n    navigator.geolocation.getCurrentPosition(\n      (position) =&gt; {\n        coords.value = position.coords\n        error.value = null\n      },\n      (err) =&gt; {\n        error.value = err\n      }\n    )\n  }\n\n  if (isSupported.value) {\n    update()\n  }\n\n  return {\n    isSupported,\n    coords,\n    error,\n    update,\n  }\n}\n```\n\n### Error Callbacks\n\n```typescript\nexport interface UseAsyncStateOptions&lt;T&gt; {\n  /** Called on success */\n  onSuccess?: (data: T) =&gt; void\n  /** Called on error */\n  onError?: (error: unknown) =&gt; void\n  /**\n   * Whether to throw errors\n   * @default false\n   */\n  throwError?: boolean\n}\n\nexport function useAsyncState&lt;T&gt;(\n  promise: () =&gt; Promise&lt;T&gt;,\n  initialState: T,\n  options: UseAsyncStateOptions&lt;T&gt; = {}\n) {\n  const { onSuccess, onError, throwError = false } = options\n\n  const state = shallowRef&lt;T&gt;(initialState)\n  const error = shallowRef&lt;unknown&gt;(null)\n  const isLoading = shallowRef(false)\n\n  async function execute() {\n    isLoading.value = true\n    error.value = null\n\n    try {\n      const data = await promise()\n      state.value = data\n      onSuccess?.(data)\n    } catch (e) {\n      error.value = e\n      onError?.(e)\n      if (throwError) throw e\n    } finally {\n      isLoading.value = false\n    }\n  }\n\n  execute()\n\n  return { state, error, isLoading, execute }\n}\n```\n\n---\n\n## 13. TypeScript Best Practices\n\n### Generic Type Inference\n\nLet TypeScript infer types when possible:\n\n```typescript\n// Type T is inferred from defaultValue\nexport function useStorage&lt;T&gt;(key: string, defaultValue: T): Ref&lt;T&gt; {\n  // ...\n}\n\n// Usage - types are inferred\nconst name = useStorage(&#39;name&#39;, &#39;John&#39;)     // Ref&lt;string&gt;\nconst count = useStorage(&#39;count&#39;, 0)        // Ref&lt;number&gt;\nconst user = useStorage(&#39;user&#39;, { id: 1 })  // Ref&lt;{ id: number }&gt;\n```\n\n### Function Overloads\n\nUse overloads for different call signatures:\n\n```typescript\n// Overload 1: Window events\nexport function useEventListener&lt;K extends keyof WindowEventMap&gt;(\n  event: K,\n  handler: (e: WindowEventMap[K]) =&gt; void\n): () =&gt; void\n\n// Overload 2: Element events\nexport function useEventListener&lt;K extends keyof HTMLElementEventMap&gt;(\n  target: MaybeRefOrGetter&lt;HTMLElement | null&gt;,\n  event: K,\n  handler: (e: HTMLElementEventMap[K]) =&gt; void\n): () =&gt; void\n\n// Implementation\nexport function useEventListener(...args: any[]): () =&gt; void {\n  // ... implementation handles all cases\n}\n```\n\n### Conditional Return Types\n\n```typescript\n// If passed a ref, return just the toggle function\nexport function useToggle(\n  value: Ref&lt;boolean&gt;\n): (value?: boolean) =&gt; boolean\n\n// If passed a plain value, return tuple\nexport function useToggle(\n  initialValue?: boolean\n): [Ref&lt;boolean&gt;, (value?: boolean) =&gt; boolean]\n\n// Implementation\nexport function useToggle(\n  initialValue: MaybeRef&lt;boolean&gt; = false\n) {\n  const valueIsRef = isRef(initialValue)\n  const state = shallowRef(toValue(initialValue))\n\n  const toggle = (value?: boolean) =&gt; {\n    state.value = value ?? !state.value\n    return state.value\n  }\n\n  if (valueIsRef) {\n    return toggle\n  }\n  return [state, toggle] as const\n}\n```\n\n---\n\n## 14. Testing\n\nFor comprehensive testing strategies including basic test structure, testing with timers, and testing async composables, see &lt;InternalLink slug=\&quot;how-to-test-vue-composables\&quot;&gt;How to Test Vue Composables&lt;/InternalLink&gt;.\n\n---\n\n## 15. Documentation\n\n### JSDoc Comments\n\n```typescript\n/**\n * Reactive mouse position\n *\n * @param options - Configuration options\n * @returns Reactive mouse coordinates and source type\n *\n * @example\n * ```ts\n * const { x, y } = useMouse()\n *\n * watchEffect(() =&gt; {\n *   console.log(`Mouse at ${x.value}, ${y.value}`)\n * })\n * ```\n *\n * @see https://your-docs.com/composables/use-mouse\n */\nexport function useMouse(options?: UseMouseOptions): UseMouseReturn {\n  // ...\n}\n```\n\n### Document Every Option\n\nEvery option should have a JSDoc comment with a `@default` tag:\n\n```typescript\nexport interface UseStorageOptions {\n  /**\n   * Storage type to use\n   * @default &#39;local&#39;\n   */\n  storage?: &#39;local&#39; | &#39;session&#39;\n\n  /**\n   * Whether to sync across browser tabs\n   * @default true\n   */\n  listenToStorageChanges?: boolean\n}\n```\n\n---\n\n## 16. Templates\n\n### Basic Composable Template\n\n```typescript\nimport { shallowRef, readonly, toValue, type MaybeRefOrGetter, type Ref } from &#39;vue&#39;\nimport { tryOnCleanup } from &#39;../utils/cleanup&#39;\n\nexport interface UseXxxOptions {\n  /**\n   * Option description\n   * @default &#39;defaultValue&#39;\n   */\n  someOption?: string\n}\n\nexport interface UseXxxReturn {\n  /** Description of value */\n  value: Readonly&lt;Ref&lt;number&gt;&gt;\n  /** Description of action */\n  doSomething: () =&gt; void\n}\n\n/**\n * Short description of what this composable does\n *\n * @param param - Description of parameter\n * @param options - Configuration options\n */\nexport function useXxx(\n  param: MaybeRefOrGetter&lt;string&gt;,\n  options: UseXxxOptions = {}\n): UseXxxReturn {\n  const { someOption = &#39;defaultValue&#39; } = options\n\n  const value = shallowRef(0)\n\n  function doSomething() {\n    const paramValue = toValue(param)\n    value.value++\n  }\n\n  // Cleanup if needed\n  tryOnCleanup(() =&gt; {\n    // cleanup logic\n  })\n\n  return {\n    value: readonly(value),\n    doSomething,\n  }\n}\n```\n\n### Async Composable Template\n\n```typescript\nimport { shallowRef, readonly, toValue, type MaybeRefOrGetter, type Ref } from &#39;vue&#39;\nimport { createEventHook, type EventHook } from &#39;../utils/eventHook&#39;\nimport { tryOnCleanup } from &#39;../utils/cleanup&#39;\n\nexport interface UseAsyncXxxOptions&lt;T&gt; {\n  /**\n   * Execute immediately\n   * @default true\n   */\n  immediate?: boolean\n  /**\n   * Called on success\n   */\n  onSuccess?: (data: T) =&gt; void\n  /**\n   * Called on error\n   */\n  onError?: (error: Error) =&gt; void\n}\n\nexport interface UseAsyncXxxReturn&lt;T&gt; {\n  data: Readonly&lt;Ref&lt;T | null&gt;&gt;\n  error: Readonly&lt;Ref&lt;Error | null&gt;&gt;\n  isLoading: Readonly&lt;Ref&lt;boolean&gt;&gt;\n  execute: () =&gt; Promise&lt;void&gt;\n  onSuccess: EventHook&lt;T&gt;[&#39;on&#39;]\n  onError: EventHook&lt;Error&gt;[&#39;on&#39;]\n}\n\nexport function useAsyncXxx&lt;T&gt;(\n  fetcher: () =&gt; Promise&lt;T&gt;,\n  options: UseAsyncXxxOptions&lt;T&gt; = {}\n): UseAsyncXxxReturn&lt;T&gt; {\n  const { immediate = true, onSuccess, onError } = options\n\n  const data = shallowRef&lt;T | null&gt;(null)\n  const error = shallowRef&lt;Error | null&gt;(null)\n  const isLoading = shallowRef(false)\n\n  const successHook = createEventHook&lt;T&gt;()\n  const errorHook = createEventHook&lt;Error&gt;()\n\n  async function execute() {\n    isLoading.value = true\n    error.value = null\n\n    try {\n      const result = await fetcher()\n      data.value = result\n      onSuccess?.(result)\n      successHook.trigger(result)\n    } catch (e) {\n      const err = e as Error\n      error.value = err\n      onError?.(err)\n      errorHook.trigger(err)\n    } finally {\n      isLoading.value = false\n    }\n  }\n\n  if (immediate) {\n    execute()\n  }\n\n  return {\n    data: readonly(data),\n    error: readonly(error),\n    isLoading: readonly(isLoading),\n    execute,\n    onSuccess: successHook.on,\n    onError: errorHook.on,\n  }\n}\n```\n\n### Pausable Composable Template\n\n```typescript\nimport { shallowRef, readonly, toValue, type MaybeRefOrGetter, type Ref } from &#39;vue&#39;\nimport { tryOnCleanup } from &#39;../utils/cleanup&#39;\n\nexport interface Pausable {\n  isActive: Readonly&lt;Ref&lt;boolean&gt;&gt;\n  pause: () =&gt; void\n  resume: () =&gt; void\n}\n\nexport interface UsePausableXxxOptions {\n  /**\n   * Start immediately\n   * @default true\n   */\n  immediate?: boolean\n}\n\nexport function usePausableXxx(\n  callback: () =&gt; void,\n  interval: MaybeRefOrGetter&lt;number&gt; = 1000,\n  options: UsePausableXxxOptions = {}\n): Pausable {\n  const { immediate = true } = options\n\n  const isActive = shallowRef(false)\n  let timer: ReturnType&lt;typeof setInterval&gt; | null = null\n\n  function clean() {\n    if (timer) {\n      clearInterval(timer)\n      timer = null\n    }\n  }\n\n  function pause() {\n    isActive.value = false\n    clean()\n  }\n\n  function resume() {\n    const ms = toValue(interval)\n    if (ms &lt;= 0) return\n\n    isActive.value = true\n    clean()\n    timer = setInterval(callback, ms)\n  }\n\n  if (immediate) {\n    resume()\n  }\n\n  tryOnCleanup(pause)\n\n  return {\n    isActive: readonly(isActive),\n    pause,\n    resume,\n  }\n}\n```\n\n---\n\n## Quick Reference Checklist\n\nUse this checklist when creating new composables:\n\n**Structure**\n- [ ] Named export (no default)\n- [ ] Explicit return type interface\n- [ ] JSDoc with `@param`, `@returns`, `@example`\n\n**Reactivity**\n- [ ] `shallowRef` for primitives\n- [ ] `ref` only when deep mutations needed\n- [ ] `MaybeRefOrGetter` for flexible inputs\n- [ ] `toValue()` to unwrap inputs\n- [ ] `readonly()` for exposed refs\n\n**Safety**\n- [ ] Guard browser APIs (`if (window)`)\n- [ ] Auto-cleanup with `tryOnCleanup`\n- [ ] Feature detection for optional APIs\n\n**TypeScript**\n- [ ] Generic type inference where possible\n- [ ] Overloads for multiple signatures\n- [ ] Strict types, no `any`\n\n**Testing**\n- [ ] Unit tests for all functionality\n- [ ] Edge cases (null, undefined, empty)\n- [ ] Cleanup verification\n\n---\n\n## Additional Resources\n\n- [Vue Composition API Docs](https://vuejs.org/guide/extras/composition-api-faq.html)\n- [Vue Reactivity in Depth](https://vuejs.org/guide/extras/reactivity-in-depth.html)\n- [VueUse](https://vueuse.org) - Collection of Vue composables (the source of these patterns)\n- [Vitest](https://vitest.dev) - Testing framework for Vue\n\n---\n\nThese patterns represent the accumulated wisdom from VueUse&#39;s codebase. Apply them consistently to build maintainable, type-safe, and production-ready Vue composables.&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PostCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus-outline inline-flex items-center gap-1.5 rounded-md border border-skin-line bg-skin-card px-2.5 py-1.5 text-xs font-medium text-skin-base opacity-80 transition-all hover:border-skin-accent/50 hover:text-skin-accent hover:opacity-100" aria-label="Copy post as markdown" title="Copy post as markdown for AI/LLM"><svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg><span>Copy Post</span></button><!--astro:end--></astro-island> </div>  <article id="article" class="prose mx-auto mt-8 max-w-5xl astro-vj4tpspi"> <p>I was studying VueUse’s codebase to understand how they structure their composables. VueUse has become the de facto standard library for Vue utilities, and I wanted to understand the patterns that make their composables so reliable. After diving deep into their source code, I distilled the key patterns into this style guide.</p>
<p>Whether you’re building your own composable library or just want to write better code, these patterns will help you create maintainable, type-safe, and SSR-compatible composition utilities.</p>
<p>If you’re new to Vue composables, I recommend starting with my earlier post <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/mastering-vue-3-composables-a-comprehensive-style-guide/" class="internal-link astro-3tyn5ojg"> Mastering Vue 3 Composables: A Comprehensive Style Guide </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Mastering Vue 3 Composables: A Comprehensive Style Guide</span> <span class="preview-description astro-3tyn5ojg">Did you ever struggle how to write better composables in Vue? In this Blog post I try to give some tips how to do that</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">vue</span>  </span> <time class="preview-date astro-3tyn5ojg">Sep 16, 2023</time> </span> </span> </span>  <script>
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
</script>, which covers many of the same patterns from a beginner-friendly perspective.</p>
<h2 id="quick-summary">Quick Summary<a class="heading-link" aria-label="Link to section" href="#quick-summary"><span class="heading-link-icon">#</span></a></h2>
<p>This guide covers patterns for writing production-quality Vue 3 composables:</p>
<ul>
<li><strong>Project structure</strong> and naming conventions</li>
<li><strong>Ref type selection</strong> (shallowRef vs ref)</li>
<li><strong>Flexible inputs</strong> with <code>MaybeRefOrGetter</code></li>
<li><strong>SSR safety</strong> patterns for server-side rendering</li>
<li><strong>Cleanup and memory management</strong> with auto-cleanup utilities</li>
<li><strong>Controllable composables</strong> (pausable, stoppable patterns)</li>
<li><strong>TypeScript best practices</strong> for full type inference</li>
<li><strong>Testing strategies</strong> - see <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/how-to-test-vue-composables/" class="internal-link astro-3tyn5ojg"> How to Test Vue Composables </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">How to Test Vue Composables: A Comprehensive Guide with Vitest</span> <span class="preview-description astro-3tyn5ojg">Learn how to effectively test Vue composables using Vitest. Covers independent and dependent composables, with practical examples and best practices.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">vue</span><span class="preview-tag astro-3tyn5ojg">testing</span>  </span> <time class="preview-date astro-3tyn5ojg">Nov 25, 2023</time> </span> </span> </span>  <script>
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
</script></li>
</ul>
<h2 id="table-of-contents">Table of Contents<a class="heading-link" aria-label="Link to section" href="#table-of-contents"><span class="heading-link-icon">#</span></a></h2>
<p></p><details><summary>Open Table of Contents</summary><p></p>
<ul>
<li><a href="#1-getting-started">1. Getting Started</a>
<ul>
<li><a href="#what-makes-a-good-composable">What Makes a Good Composable?</a></li>
<li><a href="#minimal-example">Minimal Example</a></li>
</ul>
</li>
<li><a href="#2-project-structure">2. Project Structure</a>
<ul>
<li><a href="#recommended-layout">Recommended Layout</a></li>
<li><a href="#export-pattern">Export Pattern</a></li>
</ul>
</li>
<li><a href="#3-naming-conventions">3. Naming Conventions</a>
<ul>
<li><a href="#function-names">Function Names</a></li>
<li><a href="#type-names">Type Names</a></li>
</ul>
</li>
<li><a href="#4-choosing-the-right-ref-type">4. Choosing the Right Ref Type</a>
<ul>
<li><a href="#shallowref---for-primitives-and-replaced-objects">shallowRef - For Primitives and Replaced Objects</a></li>
<li><a href="#ref---for-deep-mutations">ref - For Deep Mutations</a></li>
<li><a href="#let-users-choose">Let Users Choose</a></li>
</ul>
</li>
<li><a href="#5-flexible-inputs">5. Flexible Inputs</a>
<ul>
<li><a href="#accept-refs-getters-or-plain-values">Accept Refs, Getters, or Plain Values</a></li>
<li><a href="#reactive-configuration">Reactive Configuration</a></li>
</ul>
</li>
<li><a href="#6-designing-options">6. Designing Options</a>
<ul>
<li><a href="#structure">Structure</a></li>
<li><a href="#rules-for-options">Rules for Options</a></li>
<li><a href="#extending-base-interfaces">Extending Base Interfaces</a></li>
</ul>
</li>
<li><a href="#7-return-values">7. Return Values</a>
<ul>
<li><a href="#object-return-recommended-for-multiple-values">Object Return (Recommended for Multiple Values)</a></li>
<li><a href="#single-ref-return-for-simple-composables">Single Ref Return (For Simple Composables)</a></li>
<li><a href="#tuple-return-when-destructuring-order-matters">Tuple Return (When Destructuring Order Matters)</a></li>
<li><a href="#making-composables-awaitable">Making Composables Awaitable</a></li>
</ul>
</li>
<li><a href="#8-ssr-safety">8. SSR Safety</a>
<ul>
<li><a href="#the-problem">The Problem</a></li>
<li><a href="#solution-create-ssr-utilities">Solution: Create SSR Utilities</a></li>
<li><a href="#using-ssr-utilities">Using SSR Utilities</a></li>
<li><a href="#feature-detection">Feature Detection</a></li>
</ul>
</li>
<li><a href="#9-cleanup-and-memory-management">9. Cleanup and Memory Management</a>
<ul>
<li><a href="#the-problem-1">The Problem</a></li>
<li><a href="#solution-auto-cleanup-utility">Solution: Auto-Cleanup Utility</a></li>
<li><a href="#using-auto-cleanup">Using Auto-Cleanup</a></li>
<li><a href="#event-listener-composable-with-auto-cleanup">Event Listener Composable with Auto-Cleanup</a></li>
</ul>
</li>
<li><a href="#10-controllable-composables">10. Controllable Composables</a>
<ul>
<li><a href="#pausable-pattern">Pausable Pattern</a></li>
<li><a href="#stoppable-pattern">Stoppable Pattern</a></li>
</ul>
</li>
<li><a href="#11-error-handling">11. Error Handling</a>
<ul>
<li><a href="#graceful-degradation">Graceful Degradation</a></li>
<li><a href="#error-callbacks">Error Callbacks</a></li>
</ul>
</li>
<li><a href="#13-typescript-best-practices">13. TypeScript Best Practices</a>
<ul>
<li><a href="#generic-type-inference">Generic Type Inference</a></li>
<li><a href="#function-overloads">Function Overloads</a></li>
<li><a href="#conditional-return-types">Conditional Return Types</a></li>
</ul>
</li>
<li><a href="#14-testing">14. Testing</a></li>
<li><a href="#15-documentation">15. Documentation</a>
<ul>
<li><a href="#jsdoc-comments">JSDoc Comments</a></li>
<li><a href="#document-every-option">Document Every Option</a></li>
</ul>
</li>
<li><a href="#16-templates">16. Templates</a>
<ul>
<li><a href="#basic-composable-template">Basic Composable Template</a></li>
<li><a href="#async-composable-template">Async Composable Template</a></li>
<li><a href="#pausable-composable-template">Pausable Composable Template</a></li>
</ul>
</li>
<li><a href="#quick-reference-checklist">Quick Reference Checklist</a></li>
<li><a href="#additional-resources">Additional Resources</a></li>
</ul>
<p></p></details><p></p>
<h2 id="1-getting-started">1. Getting Started<a class="heading-link" aria-label="Link to section" href="#1-getting-started"><span class="heading-link-icon">#</span></a></h2>
<h3 id="what-makes-a-good-composable">What Makes a Good Composable?<a class="heading-link" aria-label="Link to section" href="#what-makes-a-good-composable"><span class="heading-link-icon">#</span></a></h3>
<p>A well-designed composable should be:</p>
<ul>
<li><strong>Focused</strong>: Does one thing well</li>
<li><strong>Flexible</strong>: Accepts refs, getters, or plain values</li>
<li><strong>Safe</strong>: Works in SSR, handles cleanup automatically</li>
<li><strong>Typed</strong>: Full TypeScript support with inference</li>
<li><strong>Testable</strong>: Easy to unit test in isolation</li>
</ul>
<h3 id="minimal-example">Minimal Example<a class="heading-link" aria-label="Link to section" href="#minimal-example"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">shallowRef</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> toValue</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> type</span><span style="color:#0DB9D7"> MaybeRefOrGetter</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useCounter</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">initialValue</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> MaybeRefOrGetter</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">number</span><span style="color:#89DDFF">&gt;</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> count</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> shallowRef</span><span style="color:#9ABDF5">(</span><span style="color:#7AA2F7">toValue</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">initialValue</span><span style="color:#9ABDF5">))</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#7AA2F7"> increment</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#C0CAF5"> count</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">++</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#7AA2F7"> decrement</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#C0CAF5"> count</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">--</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#7AA2F7"> reset</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#C0CAF5"> count</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> toValue</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">initialValue</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> { </span><span style="color:#C0CAF5">count</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> increment</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> decrement</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> reset</span><span style="color:#9ABDF5"> }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="import { shallowRef, toValue, type MaybeRefOrGetter } from 'vue'

export function useCounter(initialValue: MaybeRefOrGetter<number> = 0) {
  const count = shallowRef(toValue(initialValue))

  const increment = () => count.value++
  const decrement = () => count.value--
  const reset = () => count.value = toValue(initialValue)

  return { count, increment, decrement, reset }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>This simple example already demonstrates several VueUse patterns: using <code>shallowRef</code> for primitives, accepting <code>MaybeRefOrGetter</code> for flexible inputs, and returning an object with reactive state and methods.</p>
<hr/>
<h2 id="2-project-structure">2. Project Structure<a class="heading-link" aria-label="Link to section" href="#2-project-structure"><span class="heading-link-icon">#</span></a></h2>
<h3 id="recommended-layout">Recommended Layout<a class="heading-link" aria-label="Link to section" href="#recommended-layout"><span class="heading-link-icon">#</span></a></h3>
<nav class="file-tree astro-htwbjus4" aria-label="File tree"> <ul class="file-tree__list astro-htwbjus4"> <li class="file-tree__item astro-o25vlg2d" style="--level: 0;"> <details class="file-tree__folder astro-o25vlg2d" open> <summary class="astro-o25vlg2d"> <span class="file-tree__caret astro-o25vlg2d" aria-hidden="true">
▸
</span> <svg class="file-tree__icon astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">src/composables</span>  </summary> <ul class="file-tree__list astro-o25vlg2d"> <li class="file-tree__item astro-o25vlg2d" style="--level: 1;"> <details class="file-tree__folder astro-o25vlg2d" open> <summary class="astro-o25vlg2d"> <span class="file-tree__caret astro-o25vlg2d" aria-hidden="true">
▸
</span> <svg class="file-tree__icon astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">useCounter</span>  </summary> <ul class="file-tree__list astro-o25vlg2d"> <li class="file-tree__item astro-o25vlg2d" style="--level: 2;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#3178C6" d="M1.125 0C.502 0 0 .502 0 1.125v21.75C0 23.498.502 24 1.125 24h21.75c.623 0 1.125-.502 1.125-1.125V1.125C24 .502 23.498 0 22.875 0zm17.363 9.75c.612 0 1.154.037 1.627.111a6.38 6.38 0 0 1 1.306.34v2.458a3.95 3.95 0 0 0-.643-.361 5.093 5.093 0 0 0-.717-.26 5.453 5.453 0 0 0-1.426-.2c-.3 0-.573.028-.819.086a2.1 2.1 0 0 0-.623.242c-.17.104-.3.229-.393.374a.888.888 0 0 0-.14.49c0 .196.053.373.156.529.104.156.252.304.443.444s.423.276.696.41c.273.135.582.274.926.416.47.197.892.407 1.266.628.374.222.695.473.963.753.268.279.472.598.614.957.142.359.214.776.214 1.253 0 .657-.125 1.21-.373 1.656a3.033 3.033 0 0 1-1.012 1.085 4.38 4.38 0 0 1-1.487.596c-.566.12-1.163.18-1.79.18a9.916 9.916 0 0 1-1.84-.164 5.544 5.544 0 0 1-1.512-.493v-2.63a5.033 5.033 0 0 0 3.237 1.2c.333 0 .624-.03.872-.09.249-.06.456-.144.623-.25.166-.108.29-.234.373-.38a1.023 1.023 0 0 0-.074-1.089 2.12 2.12 0 0 0-.537-.5 5.597 5.597 0 0 0-.807-.444 27.72 27.72 0 0 0-1.007-.436c-.918-.383-1.602-.852-2.053-1.405-.45-.553-.676-1.222-.676-2.005 0-.614.123-1.141.369-1.582.246-.441.58-.804 1.004-1.089a4.494 4.494 0 0 1 1.47-.629 7.536 7.536 0 0 1 1.77-.201zm-15.113.188h9.563v2.166H9.506v9.646H6.789v-9.646H3.375z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">index.ts</span> <span class="file-tree__comment astro-o25vlg2d">Implementation</span> </span> </li> <li class="file-tree__item astro-o25vlg2d" style="--level: 2;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#3178C6" d="M1.125 0C.502 0 0 .502 0 1.125v21.75C0 23.498.502 24 1.125 24h21.75c.623 0 1.125-.502 1.125-1.125V1.125C24 .502 23.498 0 22.875 0zm17.363 9.75c.612 0 1.154.037 1.627.111a6.38 6.38 0 0 1 1.306.34v2.458a3.95 3.95 0 0 0-.643-.361 5.093 5.093 0 0 0-.717-.26 5.453 5.453 0 0 0-1.426-.2c-.3 0-.573.028-.819.086a2.1 2.1 0 0 0-.623.242c-.17.104-.3.229-.393.374a.888.888 0 0 0-.14.49c0 .196.053.373.156.529.104.156.252.304.443.444s.423.276.696.41c.273.135.582.274.926.416.47.197.892.407 1.266.628.374.222.695.473.963.753.268.279.472.598.614.957.142.359.214.776.214 1.253 0 .657-.125 1.21-.373 1.656a3.033 3.033 0 0 1-1.012 1.085 4.38 4.38 0 0 1-1.487.596c-.566.12-1.163.18-1.79.18a9.916 9.916 0 0 1-1.84-.164 5.544 5.544 0 0 1-1.512-.493v-2.63a5.033 5.033 0 0 0 3.237 1.2c.333 0 .624-.03.872-.09.249-.06.456-.144.623-.25.166-.108.29-.234.373-.38a1.023 1.023 0 0 0-.074-1.089 2.12 2.12 0 0 0-.537-.5 5.597 5.597 0 0 0-.807-.444 27.72 27.72 0 0 0-1.007-.436c-.918-.383-1.602-.852-2.053-1.405-.45-.553-.676-1.222-.676-2.005 0-.614.123-1.141.369-1.582.246-.441.58-.804 1.004-1.089a4.494 4.494 0 0 1 1.47-.629 7.536 7.536 0 0 1 1.77-.201zm-15.113.188h9.563v2.166H9.506v9.646H6.789v-9.646H3.375z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">index.test.ts</span> <span class="file-tree__comment astro-o25vlg2d">Tests</span> </span> </li> <li class="file-tree__item astro-o25vlg2d" style="--level: 2;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#3178C6" d="M1.125 0C.502 0 0 .502 0 1.125v21.75C0 23.498.502 24 1.125 24h21.75c.623 0 1.125-.502 1.125-1.125V1.125C24 .502 23.498 0 22.875 0zm17.363 9.75c.612 0 1.154.037 1.627.111a6.38 6.38 0 0 1 1.306.34v2.458a3.95 3.95 0 0 0-.643-.361 5.093 5.093 0 0 0-.717-.26 5.453 5.453 0 0 0-1.426-.2c-.3 0-.573.028-.819.086a2.1 2.1 0 0 0-.623.242c-.17.104-.3.229-.393.374a.888.888 0 0 0-.14.49c0 .196.053.373.156.529.104.156.252.304.443.444s.423.276.696.41c.273.135.582.274.926.416.47.197.892.407 1.266.628.374.222.695.473.963.753.268.279.472.598.614.957.142.359.214.776.214 1.253 0 .657-.125 1.21-.373 1.656a3.033 3.033 0 0 1-1.012 1.085 4.38 4.38 0 0 1-1.487.596c-.566.12-1.163.18-1.79.18a9.916 9.916 0 0 1-1.84-.164 5.544 5.544 0 0 1-1.512-.493v-2.63a5.033 5.033 0 0 0 3.237 1.2c.333 0 .624-.03.872-.09.249-.06.456-.144.623-.25.166-.108.29-.234.373-.38a1.023 1.023 0 0 0-.074-1.089 2.12 2.12 0 0 0-.537-.5 5.597 5.597 0 0 0-.807-.444 27.72 27.72 0 0 0-1.007-.436c-.918-.383-1.602-.852-2.053-1.405-.45-.553-.676-1.222-.676-2.005 0-.614.123-1.141.369-1.582.246-.441.58-.804 1.004-1.089a4.494 4.494 0 0 1 1.47-.629 7.536 7.536 0 0 1 1.77-.201zm-15.113.188h9.563v2.166H9.506v9.646H6.789v-9.646H3.375z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">types.ts</span> <span class="file-tree__comment astro-o25vlg2d">Types (optional)</span> </span> </li>  </ul> </details>   </li> <li class="file-tree__item astro-o25vlg2d" style="--level: 1;"> <details class="file-tree__folder astro-o25vlg2d"> <summary class="astro-o25vlg2d"> <span class="file-tree__caret astro-o25vlg2d" aria-hidden="true">
▸
</span> <svg class="file-tree__icon astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">useFetch</span>  </summary> <ul class="file-tree__list astro-o25vlg2d"> <li class="file-tree__item astro-o25vlg2d" style="--level: 2;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#3178C6" d="M1.125 0C.502 0 0 .502 0 1.125v21.75C0 23.498.502 24 1.125 24h21.75c.623 0 1.125-.502 1.125-1.125V1.125C24 .502 23.498 0 22.875 0zm17.363 9.75c.612 0 1.154.037 1.627.111a6.38 6.38 0 0 1 1.306.34v2.458a3.95 3.95 0 0 0-.643-.361 5.093 5.093 0 0 0-.717-.26 5.453 5.453 0 0 0-1.426-.2c-.3 0-.573.028-.819.086a2.1 2.1 0 0 0-.623.242c-.17.104-.3.229-.393.374a.888.888 0 0 0-.14.49c0 .196.053.373.156.529.104.156.252.304.443.444s.423.276.696.41c.273.135.582.274.926.416.47.197.892.407 1.266.628.374.222.695.473.963.753.268.279.472.598.614.957.142.359.214.776.214 1.253 0 .657-.125 1.21-.373 1.656a3.033 3.033 0 0 1-1.012 1.085 4.38 4.38 0 0 1-1.487.596c-.566.12-1.163.18-1.79.18a9.916 9.916 0 0 1-1.84-.164 5.544 5.544 0 0 1-1.512-.493v-2.63a5.033 5.033 0 0 0 3.237 1.2c.333 0 .624-.03.872-.09.249-.06.456-.144.623-.25.166-.108.29-.234.373-.38a1.023 1.023 0 0 0-.074-1.089 2.12 2.12 0 0 0-.537-.5 5.597 5.597 0 0 0-.807-.444 27.72 27.72 0 0 0-1.007-.436c-.918-.383-1.602-.852-2.053-1.405-.45-.553-.676-1.222-.676-2.005 0-.614.123-1.141.369-1.582.246-.441.58-.804 1.004-1.089a4.494 4.494 0 0 1 1.47-.629 7.536 7.536 0 0 1 1.77-.201zm-15.113.188h9.563v2.166H9.506v9.646H6.789v-9.646H3.375z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">index.ts</span>  </span> </li> <li class="file-tree__item astro-o25vlg2d" style="--level: 2;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#3178C6" d="M1.125 0C.502 0 0 .502 0 1.125v21.75C0 23.498.502 24 1.125 24h21.75c.623 0 1.125-.502 1.125-1.125V1.125C24 .502 23.498 0 22.875 0zm17.363 9.75c.612 0 1.154.037 1.627.111a6.38 6.38 0 0 1 1.306.34v2.458a3.95 3.95 0 0 0-.643-.361 5.093 5.093 0 0 0-.717-.26 5.453 5.453 0 0 0-1.426-.2c-.3 0-.573.028-.819.086a2.1 2.1 0 0 0-.623.242c-.17.104-.3.229-.393.374a.888.888 0 0 0-.14.49c0 .196.053.373.156.529.104.156.252.304.443.444s.423.276.696.41c.273.135.582.274.926.416.47.197.892.407 1.266.628.374.222.695.473.963.753.268.279.472.598.614.957.142.359.214.776.214 1.253 0 .657-.125 1.21-.373 1.656a3.033 3.033 0 0 1-1.012 1.085 4.38 4.38 0 0 1-1.487.596c-.566.12-1.163.18-1.79.18a9.916 9.916 0 0 1-1.84-.164 5.544 5.544 0 0 1-1.512-.493v-2.63a5.033 5.033 0 0 0 3.237 1.2c.333 0 .624-.03.872-.09.249-.06.456-.144.623-.25.166-.108.29-.234.373-.38a1.023 1.023 0 0 0-.074-1.089 2.12 2.12 0 0 0-.537-.5 5.597 5.597 0 0 0-.807-.444 27.72 27.72 0 0 0-1.007-.436c-.918-.383-1.602-.852-2.053-1.405-.45-.553-.676-1.222-.676-2.005 0-.614.123-1.141.369-1.582.246-.441.58-.804 1.004-1.089a4.494 4.494 0 0 1 1.47-.629 7.536 7.536 0 0 1 1.77-.201zm-15.113.188h9.563v2.166H9.506v9.646H6.789v-9.646H3.375z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">index.test.ts</span>  </span> </li>  </ul> </details>   </li> <li class="file-tree__item astro-o25vlg2d" style="--level: 1;"> <details class="file-tree__folder astro-o25vlg2d"> <summary class="astro-o25vlg2d"> <span class="file-tree__caret astro-o25vlg2d" aria-hidden="true">
▸
</span> <svg class="file-tree__icon astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">utils</span>  </summary> <ul class="file-tree__list astro-o25vlg2d"> <li class="file-tree__item astro-o25vlg2d" style="--level: 2;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#3178C6" d="M1.125 0C.502 0 0 .502 0 1.125v21.75C0 23.498.502 24 1.125 24h21.75c.623 0 1.125-.502 1.125-1.125V1.125C24 .502 23.498 0 22.875 0zm17.363 9.75c.612 0 1.154.037 1.627.111a6.38 6.38 0 0 1 1.306.34v2.458a3.95 3.95 0 0 0-.643-.361 5.093 5.093 0 0 0-.717-.26 5.453 5.453 0 0 0-1.426-.2c-.3 0-.573.028-.819.086a2.1 2.1 0 0 0-.623.242c-.17.104-.3.229-.393.374a.888.888 0 0 0-.14.49c0 .196.053.373.156.529.104.156.252.304.443.444s.423.276.696.41c.273.135.582.274.926.416.47.197.892.407 1.266.628.374.222.695.473.963.753.268.279.472.598.614.957.142.359.214.776.214 1.253 0 .657-.125 1.21-.373 1.656a3.033 3.033 0 0 1-1.012 1.085 4.38 4.38 0 0 1-1.487.596c-.566.12-1.163.18-1.79.18a9.916 9.916 0 0 1-1.84-.164 5.544 5.544 0 0 1-1.512-.493v-2.63a5.033 5.033 0 0 0 3.237 1.2c.333 0 .624-.03.872-.09.249-.06.456-.144.623-.25.166-.108.29-.234.373-.38a1.023 1.023 0 0 0-.074-1.089 2.12 2.12 0 0 0-.537-.5 5.597 5.597 0 0 0-.807-.444 27.72 27.72 0 0 0-1.007-.436c-.918-.383-1.602-.852-2.053-1.405-.45-.553-.676-1.222-.676-2.005 0-.614.123-1.141.369-1.582.246-.441.58-.804 1.004-1.089a4.494 4.494 0 0 1 1.47-.629 7.536 7.536 0 0 1 1.77-.201zm-15.113.188h9.563v2.166H9.506v9.646H6.789v-9.646H3.375z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">ssr.ts</span> <span class="file-tree__comment astro-o25vlg2d">SSR utilities</span> </span> </li> <li class="file-tree__item astro-o25vlg2d" style="--level: 2;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#3178C6" d="M1.125 0C.502 0 0 .502 0 1.125v21.75C0 23.498.502 24 1.125 24h21.75c.623 0 1.125-.502 1.125-1.125V1.125C24 .502 23.498 0 22.875 0zm17.363 9.75c.612 0 1.154.037 1.627.111a6.38 6.38 0 0 1 1.306.34v2.458a3.95 3.95 0 0 0-.643-.361 5.093 5.093 0 0 0-.717-.26 5.453 5.453 0 0 0-1.426-.2c-.3 0-.573.028-.819.086a2.1 2.1 0 0 0-.623.242c-.17.104-.3.229-.393.374a.888.888 0 0 0-.14.49c0 .196.053.373.156.529.104.156.252.304.443.444s.423.276.696.41c.273.135.582.274.926.416.47.197.892.407 1.266.628.374.222.695.473.963.753.268.279.472.598.614.957.142.359.214.776.214 1.253 0 .657-.125 1.21-.373 1.656a3.033 3.033 0 0 1-1.012 1.085 4.38 4.38 0 0 1-1.487.596c-.566.12-1.163.18-1.79.18a9.916 9.916 0 0 1-1.84-.164 5.544 5.544 0 0 1-1.512-.493v-2.63a5.033 5.033 0 0 0 3.237 1.2c.333 0 .624-.03.872-.09.249-.06.456-.144.623-.25.166-.108.29-.234.373-.38a1.023 1.023 0 0 0-.074-1.089 2.12 2.12 0 0 0-.537-.5 5.597 5.597 0 0 0-.807-.444 27.72 27.72 0 0 0-1.007-.436c-.918-.383-1.602-.852-2.053-1.405-.45-.553-.676-1.222-.676-2.005 0-.614.123-1.141.369-1.582.246-.441.58-.804 1.004-1.089a4.494 4.494 0 0 1 1.47-.629 7.536 7.536 0 0 1 1.77-.201zm-15.113.188h9.563v2.166H9.506v9.646H6.789v-9.646H3.375z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">types.ts</span> <span class="file-tree__comment astro-o25vlg2d">Shared types</span> </span> </li> <li class="file-tree__item astro-o25vlg2d" style="--level: 2;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#3178C6" d="M1.125 0C.502 0 0 .502 0 1.125v21.75C0 23.498.502 24 1.125 24h21.75c.623 0 1.125-.502 1.125-1.125V1.125C24 .502 23.498 0 22.875 0zm17.363 9.75c.612 0 1.154.037 1.627.111a6.38 6.38 0 0 1 1.306.34v2.458a3.95 3.95 0 0 0-.643-.361 5.093 5.093 0 0 0-.717-.26 5.453 5.453 0 0 0-1.426-.2c-.3 0-.573.028-.819.086a2.1 2.1 0 0 0-.623.242c-.17.104-.3.229-.393.374a.888.888 0 0 0-.14.49c0 .196.053.373.156.529.104.156.252.304.443.444s.423.276.696.41c.273.135.582.274.926.416.47.197.892.407 1.266.628.374.222.695.473.963.753.268.279.472.598.614.957.142.359.214.776.214 1.253 0 .657-.125 1.21-.373 1.656a3.033 3.033 0 0 1-1.012 1.085 4.38 4.38 0 0 1-1.487.596c-.566.12-1.163.18-1.79.18a9.916 9.916 0 0 1-1.84-.164 5.544 5.544 0 0 1-1.512-.493v-2.63a5.033 5.033 0 0 0 3.237 1.2c.333 0 .624-.03.872-.09.249-.06.456-.144.623-.25.166-.108.29-.234.373-.38a1.023 1.023 0 0 0-.074-1.089 2.12 2.12 0 0 0-.537-.5 5.597 5.597 0 0 0-.807-.444 27.72 27.72 0 0 0-1.007-.436c-.918-.383-1.602-.852-2.053-1.405-.45-.553-.676-1.222-.676-2.005 0-.614.123-1.141.369-1.582.246-.441.58-.804 1.004-1.089a4.494 4.494 0 0 1 1.47-.629 7.536 7.536 0 0 1 1.77-.201zm-15.113.188h9.563v2.166H9.506v9.646H6.789v-9.646H3.375z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">cleanup.ts</span> <span class="file-tree__comment astro-o25vlg2d">Cleanup utilities</span> </span> </li>  </ul> </details>   </li> <li class="file-tree__item astro-o25vlg2d" style="--level: 1;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#3178C6" d="M1.125 0C.502 0 0 .502 0 1.125v21.75C0 23.498.502 24 1.125 24h21.75c.623 0 1.125-.502 1.125-1.125V1.125C24 .502 23.498 0 22.875 0zm17.363 9.75c.612 0 1.154.037 1.627.111a6.38 6.38 0 0 1 1.306.34v2.458a3.95 3.95 0 0 0-.643-.361 5.093 5.093 0 0 0-.717-.26 5.453 5.453 0 0 0-1.426-.2c-.3 0-.573.028-.819.086a2.1 2.1 0 0 0-.623.242c-.17.104-.3.229-.393.374a.888.888 0 0 0-.14.49c0 .196.053.373.156.529.104.156.252.304.443.444s.423.276.696.41c.273.135.582.274.926.416.47.197.892.407 1.266.628.374.222.695.473.963.753.268.279.472.598.614.957.142.359.214.776.214 1.253 0 .657-.125 1.21-.373 1.656a3.033 3.033 0 0 1-1.012 1.085 4.38 4.38 0 0 1-1.487.596c-.566.12-1.163.18-1.79.18a9.916 9.916 0 0 1-1.84-.164 5.544 5.544 0 0 1-1.512-.493v-2.63a5.033 5.033 0 0 0 3.237 1.2c.333 0 .624-.03.872-.09.249-.06.456-.144.623-.25.166-.108.29-.234.373-.38a1.023 1.023 0 0 0-.074-1.089 2.12 2.12 0 0 0-.537-.5 5.597 5.597 0 0 0-.807-.444 27.72 27.72 0 0 0-1.007-.436c-.918-.383-1.602-.852-2.053-1.405-.45-.553-.676-1.222-.676-2.005 0-.614.123-1.141.369-1.582.246-.441.58-.804 1.004-1.089a4.494 4.494 0 0 1 1.47-.629 7.536 7.536 0 0 1 1.77-.201zm-15.113.188h9.563v2.166H9.506v9.646H6.789v-9.646H3.375z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">index.ts</span> <span class="file-tree__comment astro-o25vlg2d">Public exports</span> </span> </li>  </ul> </details>   </li>  </ul> </nav> 
<h3 id="export-pattern">Export Pattern<a class="heading-link" aria-label="Link to section" href="#export-pattern"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// src/composables/index.ts</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">useCounter</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">./useCounter</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">useFetch</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">./useFetch</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> type</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">UseCounterReturn</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> UseCounterOptions</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">./useCounter</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> type</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">UseFetchReturn</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> UseFetchOptions</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">./useFetch</span><span style="color:#89DDFF">&#39;</span></span></code><button type="button" class="copy" data-code="// src/composables/index.ts
export { useCounter } from './useCounter'
export { useFetch } from './useFetch'
export type { UseCounterReturn, UseCounterOptions } from './useCounter'
export type { UseFetchReturn, UseFetchOptions } from './useFetch'" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<aside aria-label="Important" class="aside aside-caution astro-37uy2q7c"> <div class="aside-content astro-37uy2q7c"> <p class="aside-title astro-37uy2q7c"> <span class="aside-emoji astro-37uy2q7c" role="img" aria-hidden="true">⚠️</span> Important </p> <section class="aside-body astro-37uy2q7c"> <p>Use named exports only. Never use default exports for composables. This ensures better tree-shaking and clearer imports.</p> </section> </div> </aside> 
<p>For more on project organization, check out <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/how-to-structure-vue-projects/" class="internal-link astro-3tyn5ojg"> How to Structure Vue Projects </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">How to Structure Vue Projects</span> <span class="preview-description astro-3tyn5ojg">Discover best practices for structuring Vue projects of any size, from simple apps to complex enterprise solutions.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">vue</span><span class="preview-tag astro-3tyn5ojg">architecture</span>  </span> <time class="preview-date astro-3tyn5ojg">May 12, 2024</time> </span> </span> </span>  <script>
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
<hr/>
<h2 id="3-naming-conventions">3. Naming Conventions<a class="heading-link" aria-label="Link to section" href="#3-naming-conventions"><span class="heading-link-icon">#</span></a></h2>
<h3 id="function-names">Function Names<a class="heading-link" aria-label="Link to section" href="#function-names"><span class="heading-link-icon">#</span></a></h3>






























<table><thead><tr><th>Prefix</th><th>Use Case</th><th>Example</th></tr></thead><tbody><tr><td data-label="Prefix"><code>use</code></td><td data-label="Use Case">Standard composables</td><td data-label="Example"><code>useMouse</code>, <code>useStorage</code>, <code>useFetch</code></td></tr><tr><td data-label="Prefix"><code>create</code></td><td data-label="Use Case">Factory functions that return composables</td><td data-label="Example"><code>createSharedState</code>, <code>createEventHook</code></td></tr><tr><td data-label="Prefix"><code>on</code></td><td data-label="Use Case">Event listener composables</td><td data-label="Example"><code>onClickOutside</code>, <code>onKeyPress</code></td></tr><tr><td data-label="Prefix"><code>try</code></td><td data-label="Use Case">Safe operations that may fail silently</td><td data-label="Example"><code>tryOnMounted</code>, <code>tryOnCleanup</code></td></tr></tbody></table>
<h3 id="type-names">Type Names<a class="heading-link" aria-label="Link to section" href="#type-names"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// Options: Use{Name}Options</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> interface</span><span style="color:#C0CAF5"> UseStorageOptions</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  deep</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> boolean</span></span>
<span class="line"><span style="color:#73DACA">  listenToChanges</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> boolean</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Return type: Use{Name}Return</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> interface</span><span style="color:#C0CAF5"> UseStorageReturn</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  data</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Ref</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF">&gt;</span></span>
<span class="line"><span style="color:#7AA2F7">  set</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">value</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> T</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span></span>
<span class="line"><span style="color:#7AA2F7">  remove</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Inferred type shorthand</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> type</span><span style="color:#C0CAF5"> UseStorageReturnType</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF">&gt;</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> ReturnType</span><span style="color:#89DDFF">&lt;typeof</span><span style="color:#C0CAF5"> useStorage</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF">&gt;&gt;</span></span></code><button type="button" class="copy" data-code="// Options: Use{Name}Options
export interface UseStorageOptions {
  deep?: boolean
  listenToChanges?: boolean
}

// Return type: Use{Name}Return
export interface UseStorageReturn<T> {
  data: Ref<T>
  set: (value: T) => void
  remove: () => void
}

// Inferred type shorthand
export type UseStorageReturnType<T> = ReturnType<typeof useStorage<T>>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr/>
<h2 id="4-choosing-the-right-ref-type">4. Choosing the Right Ref Type<a class="heading-link" aria-label="Link to section" href="#4-choosing-the-right-ref-type"><span class="heading-link-icon">#</span></a></h2>
<p>This is one of the most important decisions when writing composables. VueUse consistently follows this pattern:</p>
<p><svg id="mermaid-0" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="flowchart" style="max-width:590.41015625px" viewBox="0 0 590.41015625 798.328125" role="graphics-document document" aria-roledescription="flowchart-v2"><style>#mermaid-0{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-0 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-0 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-0 .error-icon{fill:#a44141;}#mermaid-0 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-0 .edge-thickness-normal{stroke-width:1px;}#mermaid-0 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-0 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-0 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-0 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-0 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-0 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-0 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-0 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-0 p{margin:0;}#mermaid-0 .label{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;color:#ccc;}#mermaid-0 .cluster-label text{fill:#F9FFFE;}#mermaid-0 .cluster-label span{color:#F9FFFE;}#mermaid-0 .cluster-label span p{background-color:transparent;}#mermaid-0 .label text,#mermaid-0 span{fill:#ccc;color:#ccc;}#mermaid-0 .node rect,#mermaid-0 .node circle,#mermaid-0 .node ellipse,#mermaid-0 .node polygon,#mermaid-0 .node path{fill:transparent;stroke:2px;stroke-width:1px;}#mermaid-0 .rough-node .label text,#mermaid-0 .node .label text,#mermaid-0 .image-shape .label,#mermaid-0 .icon-shape .label{text-anchor:middle;}#mermaid-0 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-0 .rough-node .label,#mermaid-0 .node .label,#mermaid-0 .image-shape .label,#mermaid-0 .icon-shape .label{text-align:center;}#mermaid-0 .node.clickable{cursor:pointer;}#mermaid-0 .root .anchor path{fill:rgb(171, 75, 153)!important;stroke-width:0;stroke:rgb(171, 75, 153);}#mermaid-0 .arrowheadPath{fill:lightgrey;}#mermaid-0 .edgePath .path{stroke:rgb(171, 75, 153);stroke-width:2.0px;}#mermaid-0 .flowchart-link{stroke:rgb(171, 75, 153);fill:none;}#mermaid-0 .edgeLabel{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-0 .edgeLabel p{background-color:hsla(0, 0%, 25%, 0);}#mermaid-0 .edgeLabel rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-0 .labelBkg{background-color:rgba(63.75, 63.75, 63.75, 0.5);}#mermaid-0 .cluster rect{fill:transparent;stroke:rgba(255, 255, 255, 0.25);stroke-width:1px;}#mermaid-0 .cluster text{fill:#F9FFFE;}#mermaid-0 .cluster span{color:#F9FFFE;}#mermaid-0 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:12px;background:rgb(138, 51, 123);border:1px solid rgba(255, 255, 255, 0.25);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-0 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-0 rect.text{fill:none;stroke-width:0;}#mermaid-0 .icon-shape,#mermaid-0 .image-shape{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-0 .icon-shape p,#mermaid-0 .image-shape p{background-color:hsla(0, 0%, 25%, 0);padding:2px;}#mermaid-0 .icon-shape rect,#mermaid-0 .image-shape rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-0 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-0 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-0 :root{--mermaid-font-family:arial,sans-serif;}</style><g><marker id="mermaid-0_flowchart-v2-pointEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-pointStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="4.5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 5 L 10 10 L 10 0 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-circleEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="11" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-0_flowchart-v2-circleStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="-1" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-0_flowchart-v2-crossEnd" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="12" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-crossStart" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="-1" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><g class="root"><g class="clusters"></g><g class="edgePaths"><path d="M219.746,62L219.746,66.167C219.746,70.333,219.746,78.667,219.746,86.333C219.746,94,219.746,101,219.746,104.5L219.746,108" id="L_A_B_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_A_B_0" data-points="W3sieCI6MjE5Ljc0NjA5Mzc1LCJ5Ijo2Mn0seyJ4IjoyMTkuNzQ2MDkzNzUsInkiOjg3fSx7IngiOjIxOS43NDYwOTM3NSwieSI6MTEyfV0=" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M178.889,221.471L163.435,234.447C147.98,247.423,117.072,273.376,101.618,310.519C86.164,347.661,86.164,395.995,86.164,420.161L86.164,444.328" id="L_B_C_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_B_C_0" data-points="W3sieCI6MTc4Ljg4ODYwNTQ2Nzk0MjgsInkiOjIyMS40NzA2MzY3MTc5NDI4fSx7IngiOjg2LjE2NDA2MjUsInkiOjI5OS4zMjgxMjV9LHsieCI6ODYuMTY0MDYyNSwieSI6NDQ4LjMyODEyNX1d" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M260.604,221.471L276.058,234.447C291.512,247.423,322.42,273.376,337.874,291.852C353.328,310.328,353.328,321.328,353.328,326.828L353.328,332.328" id="L_B_D_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_B_D_0" data-points="W3sieCI6MjYwLjYwMzU4MjAzMjA1NzIsInkiOjIyMS40NzA2MzY3MTc5NDI4fSx7IngiOjM1My4zMjgxMjUsInkiOjI5OS4zMjgxMjV9LHsieCI6MzUzLjMyODEyNSwieSI6MzM2LjMyODEyNX1d" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M296.742,557.742L284.659,575.34C272.577,592.937,248.411,628.133,236.329,653.23C224.246,678.328,224.246,693.328,224.246,700.828L224.246,708.328" id="L_D_E_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_D_E_0" data-points="W3sieCI6Mjk2Ljc0MjEyOTY1NjcyMDgsInkiOjU1Ny43NDIxMjk2NTY3MjA5fSx7IngiOjIyNC4yNDYwOTM3NSwieSI6NjYzLjMyODEyNX0seyJ4IjoyMjQuMjQ2MDkzNzUsInkiOjcxMi4zMjgxMjV9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M409.914,557.742L421.997,575.34C434.079,592.937,458.245,628.133,470.327,655.23C482.41,682.328,482.41,701.328,482.41,710.828L482.41,720.328" id="L_D_F_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_D_F_0" data-points="W3sieCI6NDA5LjkxNDEyMDM0MzI3OTIsInkiOjU1Ny43NDIxMjk2NTY3MjA5fSx7IngiOjQ4Mi40MTAxNTYyNSwieSI6NjYzLjMyODEyNX0seyJ4Ijo0ODIuNDEwMTU2MjUsInkiOjcyNC4zMjgxMjV9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path></g><g class="edgeLabels"><g class="edgeLabel"><g class="label" data-id="L_A_B_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(86.1640625, 299.328125)"><g class="label" data-id="L_B_C_0" transform="translate(-14.453125, -12)"><foreignObject width="28.90625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>Yes</p></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(353.328125, 299.328125)"><g class="label" data-id="L_B_D_0" transform="translate(-9.6328125, -12)"><foreignObject width="19.265625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>No</p></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(224.24609375, 663.328125)"><g class="label" data-id="L_D_E_0" transform="translate(-14.453125, -12)"><foreignObject width="28.90625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>Yes</p></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(482.41015625, 663.328125)"><g class="label" data-id="L_D_F_0" transform="translate(-100, -24)"><foreignObject width="200" height="48"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table;white-space:break-spaces;line-height:1.5;max-width:200px;text-align:center;width:200px"><span class="edgeLabel"><p>No - replace whole object</p></span></div></foreignObject></g></g></g><g class="nodes"><g class="node default" id="flowchart-A-0" transform="translate(219.74609375, 35)"><rect class="basic label-container" style="" x="-116.6953125" y="-27" width="233.390625" height="54"></rect><g class="label" style="" transform="translate(-86.6953125, -12)"><rect></rect><foreignObject width="173.390625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>What type of data?</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-B-1" transform="translate(219.74609375, 187.1640625)"><polygon points="75.1640625,0 150.328125,-75.1640625 75.1640625,-150.328125 0,-75.1640625" class="label-container" transform="translate(-74.6640625, 75.1640625)"></polygon><g class="label" style="" transform="translate(-48.1640625, -12)"><rect></rect><foreignObject width="96.328125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Primitive?</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-C-3" transform="translate(86.1640625, 475.328125)"><rect class="basic label-container" style="fill:#22c55e !important" x="-78.1640625" y="-27" width="156.328125" height="54"></rect><g class="label" style="color:#fff !important" transform="translate(-48.1640625, -12)"><rect></rect><foreignObject width="96.328125" height="24"><div style="color:rgb(255, 255, 255) !important;display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center" xmlns="http://www.w3.org/1999/xhtml"><span style="color:#fff !important" class="nodeLabel"><p>shallowRef</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-D-5" transform="translate(353.328125, 475.328125)"><polygon points="139,0 278,-139 139,-278 0,-139" class="label-container" transform="translate(-138.5, 139)"></polygon><g class="label" style="" transform="translate(-100, -24)"><rect></rect><foreignObject width="200" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table;white-space:break-spaces;line-height:1.5;max-width:200px;text-align:center;width:200px"><span class="nodeLabel"><p>Will you mutate nested properties?</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-E-7" transform="translate(224.24609375, 751.328125)"><rect class="basic label-container" style="fill:#3b82f6 !important" x="-130" y="-39" width="260" height="78"></rect><g class="label" style="color:#fff !important" transform="translate(-100, -24)"><rect></rect><foreignObject width="200" height="48"><div style="color:rgb(255, 255, 255) !important;display:table;white-space:break-spaces;line-height:1.5;max-width:200px;text-align:center;width:200px" xmlns="http://www.w3.org/1999/xhtml"><span style="color:#fff !important" class="nodeLabel"><p>ref - deep reactivity</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-F-9" transform="translate(482.41015625, 751.328125)"><rect class="basic label-container" style="fill:#22c55e !important" x="-78.1640625" y="-27" width="156.328125" height="54"></rect><g class="label" style="color:#fff !important" transform="translate(-48.1640625, -12)"><rect></rect><foreignObject width="96.328125" height="24"><div style="color:rgb(255, 255, 255) !important;display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center" xmlns="http://www.w3.org/1999/xhtml"><span style="color:#fff !important" class="nodeLabel"><p>shallowRef</p></span></div></foreignObject></g></g></g></g></g></svg></p>
<h3 id="shallowref---for-primitives-and-replaced-objects">shallowRef - For Primitives and Replaced Objects<a class="heading-link" aria-label="Link to section" href="#shallowref---for-primitives-and-replaced-objects"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// Primitives</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> count</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> shallowRef</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">0</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> isActive</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> shallowRef</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">false</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> name</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> shallowRef</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;&#39;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Objects that get replaced, not mutated</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> user</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> shallowRef</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">User</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">null</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> response</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> shallowRef</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Response</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">null</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Usage: Replace the whole object</span></span>
<span class="line"><span style="color:#C0CAF5">user</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span><span style="color:#73DACA"> name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">John</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> age</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 30</span><span style="color:#9ABDF5"> }</span><span style="color:#51597D;font-style:italic">  // Triggers reactivity</span></span></code><button type="button" class="copy" data-code="// Primitives
const count = shallowRef(0)
const isActive = shallowRef(false)
const name = shallowRef('')

// Objects that get replaced, not mutated
const user = shallowRef<User | null>(null)
const response = shallowRef<Response | null>(null)

// Usage: Replace the whole object
user.value = { name: 'John', age: 30 }  // Triggers reactivity" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="ref---for-deep-mutations">ref - For Deep Mutations<a class="heading-link" aria-label="Link to section" href="#ref---for-deep-mutations"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// Objects with nested mutations</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> form</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#9ABDF5">({</span></span>
<span class="line"><span style="color:#73DACA">  user</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span><span style="color:#73DACA"> name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;&#39;</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> email</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;&#39;</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  settings</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span><span style="color:#73DACA"> theme</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">light</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5"> }</span></span>
<span class="line"><span style="color:#9ABDF5">})</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Usage: Mutate nested properties</span></span>
<span class="line"><span style="color:#C0CAF5">form</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">value</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">user</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">name</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">John</span><span style="color:#89DDFF">&#39;</span><span style="color:#51597D;font-style:italic">  // Triggers reactivity</span></span>
<span class="line"><span style="color:#C0CAF5">form</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">value</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">settings</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">theme</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">dark</span><span style="color:#89DDFF">&#39;</span><span style="color:#51597D;font-style:italic">  // Triggers reactivity</span></span></code><button type="button" class="copy" data-code="// Objects with nested mutations
const form = ref({
  user: { name: '', email: '' },
  settings: { theme: 'light' }
})

// Usage: Mutate nested properties
form.value.user.name = 'John'  // Triggers reactivity
form.value.settings.theme = 'dark'  // Triggers reactivity" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="let-users-choose">Let Users Choose<a class="heading-link" aria-label="Link to section" href="#let-users-choose"><span class="heading-link-icon">#</span></a></h3>
<p>For composables storing user data, let them decide:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> interface</span><span style="color:#C0CAF5"> UseStateOptions</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   * Use shallow reactivity for better performance with large objects</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   * </span><span style="color:#646E9C;font-style:italic">@default</span><span style="color:#5A638C;font-style:italic"> false</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   */</span></span>
<span class="line"><span style="color:#73DACA">  shallow</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> boolean</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useState</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">initialValue</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> T</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> options</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> UseStateOptions</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {})</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> shallow</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> false</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> options</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> state</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> shallow</span></span>
<span class="line"><span style="color:#BB9AF7">    ?</span><span style="color:#7AA2F7"> shallowRef</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">initialValue</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#BB9AF7">    :</span><span style="color:#7AA2F7"> ref</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">initialValue</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> { </span><span style="color:#C0CAF5">state</span><span style="color:#9ABDF5"> }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="export interface UseStateOptions {
  /**
   * Use shallow reactivity for better performance with large objects
   * @default false
   */
  shallow?: boolean
}

export function useState<T>(initialValue: T, options: UseStateOptions = {}) {
  const { shallow = false } = options

  const state = shallow
    ? shallowRef(initialValue)
    : ref(initialValue)

  return { state }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr/>
<h2 id="5-flexible-inputs">5. Flexible Inputs<a class="heading-link" aria-label="Link to section" href="#5-flexible-inputs"><span class="heading-link-icon">#</span></a></h2>
<h3 id="accept-refs-getters-or-plain-values">Accept Refs, Getters, or Plain Values<a class="heading-link" aria-label="Link to section" href="#accept-refs-getters-or-plain-values"><span class="heading-link-icon">#</span></a></h3>
<p>Use <code>MaybeRefOrGetter&lt;T&gt;</code> to make your composables flexible:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">toValue</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> type</span><span style="color:#0DB9D7"> MaybeRefOrGetter</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useTitle</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">title</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> MaybeRefOrGetter</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">string</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // toValue() handles all input types:</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // - Plain value: &#39;Hello&#39; → &#39;Hello&#39;</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // - Ref: ref(&#39;Hello&#39;) → &#39;Hello&#39;</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // - Getter: () =&gt; &#39;Hello&#39; → &#39;Hello&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  watchEffect</span><span style="color:#9ABDF5">(() </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">    document</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">title</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> toValue</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">title</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// All of these work:</span></span>
<span class="line"><span style="color:#7AA2F7">useTitle</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">Static Title</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#7AA2F7">useTitle</span><span style="color:#9ABDF5">(</span><span style="color:#7AA2F7">ref</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">Reactive Title</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">))</span></span>
<span class="line"><span style="color:#7AA2F7">useTitle</span><span style="color:#9ABDF5">(()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#89DDFF"> `</span><span style="color:#9ECE6A">Page </span><span style="color:#7DCFFF">${</span><span style="color:#C0CAF5">currentPage</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#7DCFFF">}</span><span style="color:#89DDFF">`</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#7AA2F7">useTitle</span><span style="color:#9ABDF5">(</span><span style="color:#7AA2F7">computed</span><span style="color:#9ABDF5">(()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#89DDFF"> `</span><span style="color:#7DCFFF">${</span><span style="color:#C0CAF5">userName</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#7DCFFF">}</span><span style="color:#9ECE6A">&#39;s Profile</span><span style="color:#89DDFF">`</span><span style="color:#9ABDF5">))</span></span></code><button type="button" class="copy" data-code="import { toValue, type MaybeRefOrGetter } from 'vue'

export function useTitle(title: MaybeRefOrGetter<string>) {
  // toValue() handles all input types:
  // - Plain value: 'Hello' → 'Hello'
  // - Ref: ref('Hello') → 'Hello'
  // - Getter: () => 'Hello' → 'Hello'

  watchEffect(() => {
    document.title = toValue(title)
  })
}

// All of these work:
useTitle('Static Title')
useTitle(ref('Reactive Title'))
useTitle(() => `Page ${currentPage.value}`)
useTitle(computed(() => `${userName.value}'s Profile`))" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="reactive-configuration">Reactive Configuration<a class="heading-link" aria-label="Link to section" href="#reactive-configuration"><span class="heading-link-icon">#</span></a></h3>
<p>For options that should be reactive:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> interface</span><span style="color:#C0CAF5"> UseIntervalOptions</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  interval</span><span style="color:#89DDFF">?:</span><span style="color:#C0CAF5"> MaybeRefOrGetter</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">number</span><span style="color:#89DDFF">&gt;</span></span>
<span class="line"><span style="color:#73DACA">  immediate</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> boolean</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useInterval</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#7AA2F7">  callback</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#E0AF68">  options</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> UseIntervalOptions</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {}</span></span>
<span class="line"><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> interval</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> 1000</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> immediate</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> true</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> options</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Watch the interval for changes</span></span>
<span class="line"><span style="color:#7AA2F7">  watch</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#9ABDF5">    () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#7AA2F7"> toValue</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">interval</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    (</span><span style="color:#E0AF68">ms</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">      clearInterval</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">timer</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#BB9AF7">      if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">ms</span><span style="color:#BB9AF7"> &gt;</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">        timer</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> setInterval</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">callback</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> ms</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    { </span><span style="color:#C0CAF5">immediate</span><span style="color:#9ABDF5"> }</span></span>
<span class="line"><span style="color:#9ABDF5">  )</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Interval can change reactively</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> delay</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">1000</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#7AA2F7">useInterval</span><span style="color:#9ABDF5">(()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#C0CAF5"> console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">log</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">tick</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span><span style="color:#73DACA"> interval</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> delay</span><span style="color:#9ABDF5"> })</span></span>
<span class="line"><span style="color:#C0CAF5">delay</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> 500</span><span style="color:#51597D;font-style:italic">  // Interval updates automatically</span></span></code><button type="button" class="copy" data-code="export interface UseIntervalOptions {
  interval?: MaybeRefOrGetter<number>
  immediate?: boolean
}

export function useInterval(
  callback: () => void,
  options: UseIntervalOptions = {}
) {
  const { interval = 1000, immediate = true } = options

  // Watch the interval for changes
  watch(
    () => toValue(interval),
    (ms) => {
      clearInterval(timer)
      if (ms > 0) {
        timer = setInterval(callback, ms)
      }
    },
    { immediate }
  )
}

// Interval can change reactively
const delay = ref(1000)
useInterval(() => console.log('tick'), { interval: delay })
delay.value = 500  // Interval updates automatically" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr/>
<h2 id="6-designing-options">6. Designing Options<a class="heading-link" aria-label="Link to section" href="#6-designing-options"><span class="heading-link-icon">#</span></a></h2>
<h3 id="structure">Structure<a class="heading-link" aria-label="Link to section" href="#structure"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> interface</span><span style="color:#C0CAF5"> UseStorageOptions</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   * Storage type to use</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   * </span><span style="color:#646E9C;font-style:italic">@default</span><span style="color:#89DDFF;font-style:italic"> &#39;</span><span style="color:#5A638C;font-style:italic">local</span><span style="color:#89DDFF;font-style:italic">&#39;</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   */</span></span>
<span class="line"><span style="color:#73DACA">  storage</span><span style="color:#89DDFF">?:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">local</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">session</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   * Custom serializer for complex data</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   * </span><span style="color:#646E9C;font-style:italic">@default</span><span style="color:#5A638C;font-style:italic"> JSON.stringify/parse</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   */</span></span>
<span class="line"><span style="color:#73DACA">  serializer</span><span style="color:#89DDFF">?:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">    read</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">raw</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#C0CAF5"> T</span></span>
<span class="line"><span style="color:#7AA2F7">    write</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">value</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> T</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> string</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   * Sync across browser tabs</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   * </span><span style="color:#646E9C;font-style:italic">@default</span><span style="color:#5A638C;font-style:italic"> true</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   */</span></span>
<span class="line"><span style="color:#73DACA">  listenToStorageChanges</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> boolean</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   * Called when an error occurs</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   */</span></span>
<span class="line"><span style="color:#7AA2F7">  onError</span><span style="color:#89DDFF">?:</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">error</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Error</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="export interface UseStorageOptions<T> {
  /**
   * Storage type to use
   * @default 'local'
   */
  storage?: 'local' | 'session'

  /**
   * Custom serializer for complex data
   * @default JSON.stringify/parse
   */
  serializer?: {
    read: (raw: string) => T
    write: (value: T) => string
  }

  /**
   * Sync across browser tabs
   * @default true
   */
  listenToStorageChanges?: boolean

  /**
   * Called when an error occurs
   */
  onError?: (error: Error) => void
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="rules-for-options">Rules for Options<a class="heading-link" aria-label="Link to section" href="#rules-for-options"><span class="heading-link-icon">#</span></a></h3>
<ol>
<li><strong>Document every option</strong> with JSDoc</li>
<li><strong>Provide sensible defaults</strong> using <code>@default</code></li>
<li><strong>Use callbacks</strong> for events (<code>onError</code>, <code>onSuccess</code>, <code>onChange</code>)</li>
<li><strong>Group related options</strong> in nested objects if complex</li>
</ol>
<h3 id="extending-base-interfaces">Extending Base Interfaces<a class="heading-link" aria-label="Link to section" href="#extending-base-interfaces"><span class="heading-link-icon">#</span></a></h3>
<p>Create reusable option interfaces:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// src/composables/utils/types.ts</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">/** Options for composables that use window */</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> interface</span><span style="color:#C0CAF5"> ConfigurableWindow</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   * Custom window instance (useful for iframes or testing)</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   * </span><span style="color:#646E9C;font-style:italic">@default</span><span style="color:#5A638C;font-style:italic"> window</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   */</span></span>
<span class="line"><span style="color:#73DACA">  window</span><span style="color:#89DDFF">?:</span><span style="color:#C0CAF5"> Window</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">/** Options for composables that use document */</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> interface</span><span style="color:#C0CAF5"> ConfigurableDocument</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   * Custom document instance</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   * </span><span style="color:#646E9C;font-style:italic">@default</span><span style="color:#5A638C;font-style:italic"> document</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   */</span></span>
<span class="line"><span style="color:#73DACA">  document</span><span style="color:#89DDFF">?:</span><span style="color:#C0CAF5"> Document</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Usage in composables</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> interface</span><span style="color:#C0CAF5"> UseEventListenerOptions</span><span style="color:#9D7CD8;font-style:italic"> extends</span><span style="color:#BB9AF7"> ConfigurableWindow</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  capture</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> boolean</span></span>
<span class="line"><span style="color:#73DACA">  passive</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> boolean</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// src/composables/utils/types.ts

/** Options for composables that use window */
export interface ConfigurableWindow {
  /**
   * Custom window instance (useful for iframes or testing)
   * @default window
   */
  window?: Window
}

/** Options for composables that use document */
export interface ConfigurableDocument {
  /**
   * Custom document instance
   * @default document
   */
  document?: Document
}

// Usage in composables
export interface UseEventListenerOptions extends ConfigurableWindow {
  capture?: boolean
  passive?: boolean
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr/>
<h2 id="7-return-values">7. Return Values<a class="heading-link" aria-label="Link to section" href="#7-return-values"><span class="heading-link-icon">#</span></a></h2>
<h3 id="object-return-recommended-for-multiple-values">Object Return (Recommended for Multiple Values)<a class="heading-link" aria-label="Link to section" href="#object-return-recommended-for-multiple-values"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> interface</span><span style="color:#C0CAF5"> UseMouseReturn</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /** Current X position */</span></span>
<span class="line"><span style="color:#73DACA">  x</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Readonly</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Ref</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">number</span><span style="color:#89DDFF">&gt;&gt;</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /** Current Y position */</span></span>
<span class="line"><span style="color:#73DACA">  y</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Readonly</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Ref</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">number</span><span style="color:#89DDFF">&gt;&gt;</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /** Source of the last event */</span></span>
<span class="line"><span style="color:#73DACA">  sourceType</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Readonly</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Ref</span><span style="color:#89DDFF">&lt;</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">mouse</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">touch</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF">&gt;&gt;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useMouse</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> UseMouseReturn</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> x</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> shallowRef</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">0</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> y</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> shallowRef</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">0</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> sourceType</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> shallowRef</span><span style="color:#89DDFF">&lt;</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">mouse</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">touch</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">null</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // ... implementation</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">    x</span><span style="color:#89DDFF">:</span><span style="color:#7AA2F7"> readonly</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">x</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    y</span><span style="color:#89DDFF">:</span><span style="color:#7AA2F7"> readonly</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">y</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    sourceType</span><span style="color:#89DDFF">:</span><span style="color:#7AA2F7"> readonly</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">sourceType</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="export interface UseMouseReturn {
  /** Current X position */
  x: Readonly<Ref<number>>
  /** Current Y position */
  y: Readonly<Ref<number>>
  /** Source of the last event */
  sourceType: Readonly<Ref<'mouse' | 'touch' | null>>
}

export function useMouse(): UseMouseReturn {
  const x = shallowRef(0)
  const y = shallowRef(0)
  const sourceType = shallowRef<'mouse' | 'touch' | null>(null)

  // ... implementation

  return {
    x: readonly(x),
    y: readonly(y),
    sourceType: readonly(sourceType),
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="single-ref-return-for-simple-composables">Single Ref Return (For Simple Composables)<a class="heading-link" aria-label="Link to section" href="#single-ref-return-for-simple-composables"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useOnline</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Readonly</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Ref</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">boolean</span><span style="color:#89DDFF">&gt;&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> isOnline</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> shallowRef</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">navigator</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">onLine</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // ... implementation</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#7AA2F7"> readonly</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">isOnline</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="export function useOnline(): Readonly<Ref<boolean>> {
  const isOnline = shallowRef(navigator.onLine)

  // ... implementation

  return readonly(isOnline)
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="tuple-return-when-destructuring-order-matters">Tuple Return (When Destructuring Order Matters)<a class="heading-link" aria-label="Link to section" href="#tuple-return-when-destructuring-order-matters"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useToggle</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#E0AF68">  initialValue</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> false</span></span>
<span class="line"><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#C0CAF5">Ref</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">boolean</span><span style="color:#89DDFF">&gt;,</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">value</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> boolean</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span><span style="color:#9ABDF5">]</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> state</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> shallowRef</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">initialValue</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#7AA2F7"> toggle</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">value</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> boolean</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">    state</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> value</span><span style="color:#BB9AF7"> ??</span><span style="color:#BB9AF7"> !</span><span style="color:#C0CAF5">state</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> [</span><span style="color:#7DCFFF">state</span><span style="color:#89DDFF">,</span><span style="color:#7DCFFF"> toggle</span><span style="color:#9ABDF5">]</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Usage</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#89DDFF"> [</span><span style="color:#BB9AF7">isOpen</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> toggleOpen</span><span style="color:#89DDFF">]</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> useToggle</span><span style="color:#9ABDF5">()</span></span></code><button type="button" class="copy" data-code="export function useToggle(
  initialValue = false
): [Ref<boolean>, (value?: boolean) => void] {
  const state = shallowRef(initialValue)

  const toggle = (value?: boolean) => {
    state.value = value ?? !state.value
  }

  return [state, toggle]
}

// Usage
const [isOpen, toggleOpen] = useToggle()" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="making-composables-awaitable">Making Composables Awaitable<a class="heading-link" aria-label="Link to section" href="#making-composables-awaitable"><span class="heading-link-icon">#</span></a></h3>
<p>For async composables, implement <code>PromiseLike</code>:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useFetch</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">url</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> MaybeRefOrGetter</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">string</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> data</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> shallowRef</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">null</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> isLoading</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> shallowRef</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">true</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> error</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> shallowRef</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Error</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">null</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#7AA2F7"> execute</span><span style="color:#89DDFF"> =</span><span style="color:#9D7CD8;font-style:italic"> async</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">    isLoading</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> true</span></span>
<span class="line"><span style="color:#BB9AF7">    try</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">      const</span><span style="color:#BB9AF7"> response</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#7AA2F7"> fetch</span><span style="color:#9ABDF5">(</span><span style="color:#7AA2F7">toValue</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">url</span><span style="color:#9ABDF5">))</span></span>
<span class="line"><span style="color:#C0CAF5">      data</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#C0CAF5"> response</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">json</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#9ABDF5">    } </span><span style="color:#BB9AF7">catch</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">e</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">      error</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> e</span><span style="color:#89DDFF"> as</span><span style="color:#C0CAF5"> Error</span></span>
<span class="line"><span style="color:#9ABDF5">    } </span><span style="color:#BB9AF7">finally</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">      isLoading</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> false</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  execute</span><span style="color:#9ABDF5">()</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> shell</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> { </span><span style="color:#C0CAF5">data</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> isLoading</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> error</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> execute</span><span style="color:#9ABDF5"> }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#F7768E;font-weight:bold">    ...</span><span style="color:#C0CAF5">shell</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">    // Make it awaitable</span></span>
<span class="line"><span style="color:#7AA2F7">    then</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">TResult</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#7AA2F7">      onFulfilled</span><span style="color:#89DDFF">?:</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">value</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> typeof</span><span style="color:#C0CAF5"> shell</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#C0CAF5"> TResult</span></span>
<span class="line"><span style="color:#9ABDF5">    )</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Promise</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">TResult</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">      return</span><span style="color:#89DDFF"> new</span><span style="color:#0DB9D7"> Promise</span><span style="color:#9ABDF5">((</span><span style="color:#E0AF68">resolve</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">        watch</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">isLoading</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">loading</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">          if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#C0CAF5">loading</span><span style="color:#9ABDF5">) </span><span style="color:#7AA2F7">resolve</span><span style="color:#9ABDF5">(</span><span style="color:#7AA2F7">onFulfilled</span><span style="color:#89DDFF">?.</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">shell</span><span style="color:#9ABDF5">) </span><span style="color:#89DDFF">as</span><span style="color:#C0CAF5"> TResult</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">        }</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">immediate</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span><span style="color:#9ABDF5"> })</span></span>
<span class="line"><span style="color:#9ABDF5">      })</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Can be used both ways:</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> data</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> isLoading</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> useFetch</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">/api/users</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Or awaited:</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> data</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#7AA2F7"> useFetch</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">/api/users</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#C0CAF5">console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">log</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">data</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">)</span><span style="color:#51597D;font-style:italic">  // Data is ready</span></span></code><button type="button" class="copy" data-code="export function useFetch<T>(url: MaybeRefOrGetter<string>) {
  const data = shallowRef<T | null>(null)
  const isLoading = shallowRef(true)
  const error = shallowRef<Error | null>(null)

  const execute = async () => {
    isLoading.value = true
    try {
      const response = await fetch(toValue(url))
      data.value = await response.json()
    } catch (e) {
      error.value = e as Error
    } finally {
      isLoading.value = false
    }
  }

  execute()

  const shell = { data, isLoading, error, execute }

  return {
    ...shell,
    // Make it awaitable
    then<TResult>(
      onFulfilled?: (value: typeof shell) => TResult
    ): Promise<TResult> {
      return new Promise((resolve) => {
        watch(isLoading, (loading) => {
          if (!loading) resolve(onFulfilled?.(shell) as TResult)
        }, { immediate: true })
      })
    }
  }
}

// Can be used both ways:
const { data, isLoading } = useFetch('/api/users')

// Or awaited:
const { data } = await useFetch('/api/users')
console.log(data.value)  // Data is ready" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr/>
<h2 id="8-ssr-safety">8. SSR Safety<a class="heading-link" aria-label="Link to section" href="#8-ssr-safety"><span class="heading-link-icon">#</span></a></h2>
<h3 id="the-problem">The Problem<a class="heading-link" aria-label="Link to section" href="#the-problem"><span class="heading-link-icon">#</span></a></h3>
<p>Browser APIs (<code>window</code>, <code>document</code>, <code>localStorage</code>) don’t exist on the server. Accessing them during SSR causes errors.</p>
<p>For a deep dive into this topic, see <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/how-vueuse-solves-ssr-window-errors-vue-applications/" class="internal-link astro-3tyn5ojg"> How VueUse Solves SSR Window Errors </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">How VueUse Solves SSR Window Errors in Vue Applications</span> <span class="preview-description astro-3tyn5ojg">Discover how VueUse solves SSR issues with browser APIs and keeps your Vue composables safe from &#39;window is not defined&#39; errors.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">vue</span>  </span> <time class="preview-date astro-3tyn5ojg">Jul 14, 2025</time> </span> </span> </span>  <script>
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
<p><svg id="mermaid-1" width="451" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" height="616" viewBox="-50 -10 451 616" role="graphics-document document" aria-roledescription="sequence"><g><rect x="200" y="530" fill="#eaeaea" stroke="#666" width="150" height="65" name="S" rx="3" ry="3" class="actor actor-bottom"></rect><text x="275" y="562.5" dominant-baseline="central" alignment-baseline="central" class="actor actor-box" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="275" dy="0">Server (Node.js)</tspan></text></g><g><rect x="0" y="530" fill="#eaeaea" stroke="#666" width="150" height="65" name="B" rx="3" ry="3" class="actor actor-bottom"></rect><text x="75" y="562.5" dominant-baseline="central" alignment-baseline="central" class="actor actor-box" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="75" dy="0">Browser</tspan></text></g><g><line id="actor1" x1="275" y1="65" x2="275" y2="530" class="actor-line 200" stroke-width="0.5px" stroke="#999" name="S"></line><g id="root-1"><rect x="200" y="0" fill="#eaeaea" stroke="#666" width="150" height="65" name="S" rx="3" ry="3" class="actor actor-top"></rect><text x="275" y="32.5" dominant-baseline="central" alignment-baseline="central" class="actor actor-box" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="275" dy="0">Server (Node.js)</tspan></text></g></g><g><line id="actor0" x1="75" y1="65" x2="75" y2="530" class="actor-line 200" stroke-width="0.5px" stroke="#999" name="B"></line><g id="root-0"><rect x="0" y="0" fill="#eaeaea" stroke="#666" width="150" height="65" name="B" rx="3" ry="3" class="actor actor-top"></rect><text x="75" y="32.5" dominant-baseline="central" alignment-baseline="central" class="actor actor-box" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="75" dy="0">Browser</tspan></text></g></g><style>#mermaid-1{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-1 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-1 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-1 .error-icon{fill:#a44141;}#mermaid-1 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-1 .edge-thickness-normal{stroke-width:1px;}#mermaid-1 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-1 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-1 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-1 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-1 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-1 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-1 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-1 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-1 p{margin:0;}#mermaid-1 .actor{stroke:#ccc;fill:transparent;}#mermaid-1 text.actor>tspan{fill:lightgrey;stroke:none;}#mermaid-1 .actor-line{stroke:#ccc;}#mermaid-1 .innerArc{stroke-width:1.5;stroke-dasharray:none;}#mermaid-1 .messageLine0{stroke-width:1.5;stroke-dasharray:none;stroke:lightgrey;}#mermaid-1 .messageLine1{stroke-width:1.5;stroke-dasharray:2,2;stroke:lightgrey;}#mermaid-1 #arrowhead path{fill:lightgrey;stroke:lightgrey;}#mermaid-1 .sequenceNumber{fill:black;}#mermaid-1 #sequencenumber{fill:lightgrey;}#mermaid-1 #crosshead path{fill:lightgrey;stroke:lightgrey;}#mermaid-1 .messageText{fill:lightgrey;stroke:none;}#mermaid-1 .labelBox{stroke:#ccc;fill:transparent;}#mermaid-1 .labelText,#mermaid-1 .labelText>tspan{fill:lightgrey;stroke:none;}#mermaid-1 .loopText,#mermaid-1 .loopText>tspan{fill:lightgrey;stroke:none;}#mermaid-1 .loopLine{stroke-width:2px;stroke-dasharray:2,2;stroke:#ccc;fill:#ccc;}#mermaid-1 .note{stroke:hsl(180, 0%, 18.3529411765%);fill:hsla(0, 0%, 16%, 0);}#mermaid-1 .noteText,#mermaid-1 .noteText>tspan{fill:rgb(183.8476190475, 181.5523809523, 181.5523809523);stroke:none;}#mermaid-1 .activation0{fill:hsla(0, 0%, 16%, 0);stroke:#ccc;}#mermaid-1 .activation1{fill:hsla(0, 0%, 16%, 0);stroke:#ccc;}#mermaid-1 .activation2{fill:hsla(0, 0%, 16%, 0);stroke:#ccc;}#mermaid-1 .actorPopupMenu{position:absolute;}#mermaid-1 .actorPopupMenuPanel{position:absolute;fill:transparent;box-shadow:0px 8px 16px 0px rgba(0,0,0,0.2);filter:drop-shadow(3px 5px 2px rgb(0 0 0 / 0.4));}#mermaid-1 .actor-man line{stroke:#ccc;fill:transparent;}#mermaid-1 .actor-man circle,#mermaid-1 line{stroke:#ccc;fill:transparent;stroke-width:2px;}#mermaid-1 :root{--mermaid-font-family:arial,sans-serif;}</style><g></g><defs><symbol id="computer" width="24" height="24"><path transform="scale(.5)" d="M2 2v13h20v-13h-20zm18 11h-16v-9h16v9zm-10.228 6l.466-1h3.524l.467 1h-4.457zm14.228 3h-24l2-6h2.104l-1.33 4h18.45l-1.297-4h2.073l2 6zm-5-10h-14v-7h14v7z"></path></symbol></defs><defs><symbol id="database" fill-rule="evenodd" clip-rule="evenodd"><path transform="scale(.5)" d="M12.258.001l.256.004.255.005.253.008.251.01.249.012.247.015.246.016.242.019.241.02.239.023.236.024.233.027.231.028.229.031.225.032.223.034.22.036.217.038.214.04.211.041.208.043.205.045.201.046.198.048.194.05.191.051.187.053.183.054.18.056.175.057.172.059.168.06.163.061.16.063.155.064.15.066.074.033.073.033.071.034.07.034.069.035.068.035.067.035.066.035.064.036.064.036.062.036.06.036.06.037.058.037.058.037.055.038.055.038.053.038.052.038.051.039.05.039.048.039.047.039.045.04.044.04.043.04.041.04.04.041.039.041.037.041.036.041.034.041.033.042.032.042.03.042.029.042.027.042.026.043.024.043.023.043.021.043.02.043.018.044.017.043.015.044.013.044.012.044.011.045.009.044.007.045.006.045.004.045.002.045.001.045v17l-.001.045-.002.045-.004.045-.006.045-.007.045-.009.044-.011.045-.012.044-.013.044-.015.044-.017.043-.018.044-.02.043-.021.043-.023.043-.024.043-.026.043-.027.042-.029.042-.03.042-.032.042-.033.042-.034.041-.036.041-.037.041-.039.041-.04.041-.041.04-.043.04-.044.04-.045.04-.047.039-.048.039-.05.039-.051.039-.052.038-.053.038-.055.038-.055.038-.058.037-.058.037-.06.037-.06.036-.062.036-.064.036-.064.036-.066.035-.067.035-.068.035-.069.035-.07.034-.071.034-.073.033-.074.033-.15.066-.155.064-.16.063-.163.061-.168.06-.172.059-.175.057-.18.056-.183.054-.187.053-.191.051-.194.05-.198.048-.201.046-.205.045-.208.043-.211.041-.214.04-.217.038-.22.036-.223.034-.225.032-.229.031-.231.028-.233.027-.236.024-.239.023-.241.02-.242.019-.246.016-.247.015-.249.012-.251.01-.253.008-.255.005-.256.004-.258.001-.258-.001-.256-.004-.255-.005-.253-.008-.251-.01-.249-.012-.247-.015-.245-.016-.243-.019-.241-.02-.238-.023-.236-.024-.234-.027-.231-.028-.228-.031-.226-.032-.223-.034-.22-.036-.217-.038-.214-.04-.211-.041-.208-.043-.204-.045-.201-.046-.198-.048-.195-.05-.19-.051-.187-.053-.184-.054-.179-.056-.176-.057-.172-.059-.167-.06-.164-.061-.159-.063-.155-.064-.151-.066-.074-.033-.072-.033-.072-.034-.07-.034-.069-.035-.068-.035-.067-.035-.066-.035-.064-.036-.063-.036-.062-.036-.061-.036-.06-.037-.058-.037-.057-.037-.056-.038-.055-.038-.053-.038-.052-.038-.051-.039-.049-.039-.049-.039-.046-.039-.046-.04-.044-.04-.043-.04-.041-.04-.04-.041-.039-.041-.037-.041-.036-.041-.034-.041-.033-.042-.032-.042-.03-.042-.029-.042-.027-.042-.026-.043-.024-.043-.023-.043-.021-.043-.02-.043-.018-.044-.017-.043-.015-.044-.013-.044-.012-.044-.011-.045-.009-.044-.007-.045-.006-.045-.004-.045-.002-.045-.001-.045v-17l.001-.045.002-.045.004-.045.006-.045.007-.045.009-.044.011-.045.012-.044.013-.044.015-.044.017-.043.018-.044.02-.043.021-.043.023-.043.024-.043.026-.043.027-.042.029-.042.03-.042.032-.042.033-.042.034-.041.036-.041.037-.041.039-.041.04-.041.041-.04.043-.04.044-.04.046-.04.046-.039.049-.039.049-.039.051-.039.052-.038.053-.038.055-.038.056-.038.057-.037.058-.037.06-.037.061-.036.062-.036.063-.036.064-.036.066-.035.067-.035.068-.035.069-.035.07-.034.072-.034.072-.033.074-.033.151-.066.155-.064.159-.063.164-.061.167-.06.172-.059.176-.057.179-.056.184-.054.187-.053.19-.051.195-.05.198-.048.201-.046.204-.045.208-.043.211-.041.214-.04.217-.038.22-.036.223-.034.226-.032.228-.031.231-.028.234-.027.236-.024.238-.023.241-.02.243-.019.245-.016.247-.015.249-.012.251-.01.253-.008.255-.005.256-.004.258-.001.258.001zm-9.258 20.499v.01l.001.021.003.021.004.022.005.021.006.022.007.022.009.023.01.022.011.023.012.023.013.023.015.023.016.024.017.023.018.024.019.024.021.024.022.025.023.024.024.025.052.049.056.05.061.051.066.051.07.051.075.051.079.052.084.052.088.052.092.052.097.052.102.051.105.052.11.052.114.051.119.051.123.051.127.05.131.05.135.05.139.048.144.049.147.047.152.047.155.047.16.045.163.045.167.043.171.043.176.041.178.041.183.039.187.039.19.037.194.035.197.035.202.033.204.031.209.03.212.029.216.027.219.025.222.024.226.021.23.02.233.018.236.016.24.015.243.012.246.01.249.008.253.005.256.004.259.001.26-.001.257-.004.254-.005.25-.008.247-.011.244-.012.241-.014.237-.016.233-.018.231-.021.226-.021.224-.024.22-.026.216-.027.212-.028.21-.031.205-.031.202-.034.198-.034.194-.036.191-.037.187-.039.183-.04.179-.04.175-.042.172-.043.168-.044.163-.045.16-.046.155-.046.152-.047.148-.048.143-.049.139-.049.136-.05.131-.05.126-.05.123-.051.118-.052.114-.051.11-.052.106-.052.101-.052.096-.052.092-.052.088-.053.083-.051.079-.052.074-.052.07-.051.065-.051.06-.051.056-.05.051-.05.023-.024.023-.025.021-.024.02-.024.019-.024.018-.024.017-.024.015-.023.014-.024.013-.023.012-.023.01-.023.01-.022.008-.022.006-.022.006-.022.004-.022.004-.021.001-.021.001-.021v-4.127l-.077.055-.08.053-.083.054-.085.053-.087.052-.09.052-.093.051-.095.05-.097.05-.1.049-.102.049-.105.048-.106.047-.109.047-.111.046-.114.045-.115.045-.118.044-.12.043-.122.042-.124.042-.126.041-.128.04-.13.04-.132.038-.134.038-.135.037-.138.037-.139.035-.142.035-.143.034-.144.033-.147.032-.148.031-.15.03-.151.03-.153.029-.154.027-.156.027-.158.026-.159.025-.161.024-.162.023-.163.022-.165.021-.166.02-.167.019-.169.018-.169.017-.171.016-.173.015-.173.014-.175.013-.175.012-.177.011-.178.01-.179.008-.179.008-.181.006-.182.005-.182.004-.184.003-.184.002h-.37l-.184-.002-.184-.003-.182-.004-.182-.005-.181-.006-.179-.008-.179-.008-.178-.01-.176-.011-.176-.012-.175-.013-.173-.014-.172-.015-.171-.016-.17-.017-.169-.018-.167-.019-.166-.02-.165-.021-.163-.022-.162-.023-.161-.024-.159-.025-.157-.026-.156-.027-.155-.027-.153-.029-.151-.03-.15-.03-.148-.031-.146-.032-.145-.033-.143-.034-.141-.035-.14-.035-.137-.037-.136-.037-.134-.038-.132-.038-.13-.04-.128-.04-.126-.041-.124-.042-.122-.042-.12-.044-.117-.043-.116-.045-.113-.045-.112-.046-.109-.047-.106-.047-.105-.048-.102-.049-.1-.049-.097-.05-.095-.05-.093-.052-.09-.051-.087-.052-.085-.053-.083-.054-.08-.054-.077-.054v4.127zm0-5.654v.011l.001.021.003.021.004.021.005.022.006.022.007.022.009.022.01.022.011.023.012.023.013.023.015.024.016.023.017.024.018.024.019.024.021.024.022.024.023.025.024.024.052.05.056.05.061.05.066.051.07.051.075.052.079.051.084.052.088.052.092.052.097.052.102.052.105.052.11.051.114.051.119.052.123.05.127.051.131.05.135.049.139.049.144.048.147.048.152.047.155.046.16.045.163.045.167.044.171.042.176.042.178.04.183.04.187.038.19.037.194.036.197.034.202.033.204.032.209.03.212.028.216.027.219.025.222.024.226.022.23.02.233.018.236.016.24.014.243.012.246.01.249.008.253.006.256.003.259.001.26-.001.257-.003.254-.006.25-.008.247-.01.244-.012.241-.015.237-.016.233-.018.231-.02.226-.022.224-.024.22-.025.216-.027.212-.029.21-.03.205-.032.202-.033.198-.035.194-.036.191-.037.187-.039.183-.039.179-.041.175-.042.172-.043.168-.044.163-.045.16-.045.155-.047.152-.047.148-.048.143-.048.139-.05.136-.049.131-.05.126-.051.123-.051.118-.051.114-.052.11-.052.106-.052.101-.052.096-.052.092-.052.088-.052.083-.052.079-.052.074-.051.07-.052.065-.051.06-.05.056-.051.051-.049.023-.025.023-.024.021-.025.02-.024.019-.024.018-.024.017-.024.015-.023.014-.023.013-.024.012-.022.01-.023.01-.023.008-.022.006-.022.006-.022.004-.021.004-.022.001-.021.001-.021v-4.139l-.077.054-.08.054-.083.054-.085.052-.087.053-.09.051-.093.051-.095.051-.097.05-.1.049-.102.049-.105.048-.106.047-.109.047-.111.046-.114.045-.115.044-.118.044-.12.044-.122.042-.124.042-.126.041-.128.04-.13.039-.132.039-.134.038-.135.037-.138.036-.139.036-.142.035-.143.033-.144.033-.147.033-.148.031-.15.03-.151.03-.153.028-.154.028-.156.027-.158.026-.159.025-.161.024-.162.023-.163.022-.165.021-.166.02-.167.019-.169.018-.169.017-.171.016-.173.015-.173.014-.175.013-.175.012-.177.011-.178.009-.179.009-.179.007-.181.007-.182.005-.182.004-.184.003-.184.002h-.37l-.184-.002-.184-.003-.182-.004-.182-.005-.181-.007-.179-.007-.179-.009-.178-.009-.176-.011-.176-.012-.175-.013-.173-.014-.172-.015-.171-.016-.17-.017-.169-.018-.167-.019-.166-.02-.165-.021-.163-.022-.162-.023-.161-.024-.159-.025-.157-.026-.156-.027-.155-.028-.153-.028-.151-.03-.15-.03-.148-.031-.146-.033-.145-.033-.143-.033-.141-.035-.14-.036-.137-.036-.136-.037-.134-.038-.132-.039-.13-.039-.128-.04-.126-.041-.124-.042-.122-.043-.12-.043-.117-.044-.116-.044-.113-.046-.112-.046-.109-.046-.106-.047-.105-.048-.102-.049-.1-.049-.097-.05-.095-.051-.093-.051-.09-.051-.087-.053-.085-.052-.083-.054-.08-.054-.077-.054v4.139zm0-5.666v.011l.001.02.003.022.004.021.005.022.006.021.007.022.009.023.01.022.011.023.012.023.013.023.015.023.016.024.017.024.018.023.019.024.021.025.022.024.023.024.024.025.052.05.056.05.061.05.066.051.07.051.075.052.079.051.084.052.088.052.092.052.097.052.102.052.105.051.11.052.114.051.119.051.123.051.127.05.131.05.135.05.139.049.144.048.147.048.152.047.155.046.16.045.163.045.167.043.171.043.176.042.178.04.183.04.187.038.19.037.194.036.197.034.202.033.204.032.209.03.212.028.216.027.219.025.222.024.226.021.23.02.233.018.236.017.24.014.243.012.246.01.249.008.253.006.256.003.259.001.26-.001.257-.003.254-.006.25-.008.247-.01.244-.013.241-.014.237-.016.233-.018.231-.02.226-.022.224-.024.22-.025.216-.027.212-.029.21-.03.205-.032.202-.033.198-.035.194-.036.191-.037.187-.039.183-.039.179-.041.175-.042.172-.043.168-.044.163-.045.16-.045.155-.047.152-.047.148-.048.143-.049.139-.049.136-.049.131-.051.126-.05.123-.051.118-.052.114-.051.11-.052.106-.052.101-.052.096-.052.092-.052.088-.052.083-.052.079-.052.074-.052.07-.051.065-.051.06-.051.056-.05.051-.049.023-.025.023-.025.021-.024.02-.024.019-.024.018-.024.017-.024.015-.023.014-.024.013-.023.012-.023.01-.022.01-.023.008-.022.006-.022.006-.022.004-.022.004-.021.001-.021.001-.021v-4.153l-.077.054-.08.054-.083.053-.085.053-.087.053-.09.051-.093.051-.095.051-.097.05-.1.049-.102.048-.105.048-.106.048-.109.046-.111.046-.114.046-.115.044-.118.044-.12.043-.122.043-.124.042-.126.041-.128.04-.13.039-.132.039-.134.038-.135.037-.138.036-.139.036-.142.034-.143.034-.144.033-.147.032-.148.032-.15.03-.151.03-.153.028-.154.028-.156.027-.158.026-.159.024-.161.024-.162.023-.163.023-.165.021-.166.02-.167.019-.169.018-.169.017-.171.016-.173.015-.173.014-.175.013-.175.012-.177.01-.178.01-.179.009-.179.007-.181.006-.182.006-.182.004-.184.003-.184.001-.185.001-.185-.001-.184-.001-.184-.003-.182-.004-.182-.006-.181-.006-.179-.007-.179-.009-.178-.01-.176-.01-.176-.012-.175-.013-.173-.014-.172-.015-.171-.016-.17-.017-.169-.018-.167-.019-.166-.02-.165-.021-.163-.023-.162-.023-.161-.024-.159-.024-.157-.026-.156-.027-.155-.028-.153-.028-.151-.03-.15-.03-.148-.032-.146-.032-.145-.033-.143-.034-.141-.034-.14-.036-.137-.036-.136-.037-.134-.038-.132-.039-.13-.039-.128-.041-.126-.041-.124-.041-.122-.043-.12-.043-.117-.044-.116-.044-.113-.046-.112-.046-.109-.046-.106-.048-.105-.048-.102-.048-.1-.05-.097-.049-.095-.051-.093-.051-.09-.052-.087-.052-.085-.053-.083-.053-.08-.054-.077-.054v4.153zm8.74-8.179l-.257.004-.254.005-.25.008-.247.011-.244.012-.241.014-.237.016-.233.018-.231.021-.226.022-.224.023-.22.026-.216.027-.212.028-.21.031-.205.032-.202.033-.198.034-.194.036-.191.038-.187.038-.183.04-.179.041-.175.042-.172.043-.168.043-.163.045-.16.046-.155.046-.152.048-.148.048-.143.048-.139.049-.136.05-.131.05-.126.051-.123.051-.118.051-.114.052-.11.052-.106.052-.101.052-.096.052-.092.052-.088.052-.083.052-.079.052-.074.051-.07.052-.065.051-.06.05-.056.05-.051.05-.023.025-.023.024-.021.024-.02.025-.019.024-.018.024-.017.023-.015.024-.014.023-.013.023-.012.023-.01.023-.01.022-.008.022-.006.023-.006.021-.004.022-.004.021-.001.021-.001.021.001.021.001.021.004.021.004.022.006.021.006.023.008.022.01.022.01.023.012.023.013.023.014.023.015.024.017.023.018.024.019.024.02.025.021.024.023.024.023.025.051.05.056.05.06.05.065.051.07.052.074.051.079.052.083.052.088.052.092.052.096.052.101.052.106.052.11.052.114.052.118.051.123.051.126.051.131.05.136.05.139.049.143.048.148.048.152.048.155.046.16.046.163.045.168.043.172.043.175.042.179.041.183.04.187.038.191.038.194.036.198.034.202.033.205.032.21.031.212.028.216.027.22.026.224.023.226.022.231.021.233.018.237.016.241.014.244.012.247.011.25.008.254.005.257.004.26.001.26-.001.257-.004.254-.005.25-.008.247-.011.244-.012.241-.014.237-.016.233-.018.231-.021.226-.022.224-.023.22-.026.216-.027.212-.028.21-.031.205-.032.202-.033.198-.034.194-.036.191-.038.187-.038.183-.04.179-.041.175-.042.172-.043.168-.043.163-.045.16-.046.155-.046.152-.048.148-.048.143-.048.139-.049.136-.05.131-.05.126-.051.123-.051.118-.051.114-.052.11-.052.106-.052.101-.052.096-.052.092-.052.088-.052.083-.052.079-.052.074-.051.07-.052.065-.051.06-.05.056-.05.051-.05.023-.025.023-.024.021-.024.02-.025.019-.024.018-.024.017-.023.015-.024.014-.023.013-.023.012-.023.01-.023.01-.022.008-.022.006-.023.006-.021.004-.022.004-.021.001-.021.001-.021-.001-.021-.001-.021-.004-.021-.004-.022-.006-.021-.006-.023-.008-.022-.01-.022-.01-.023-.012-.023-.013-.023-.014-.023-.015-.024-.017-.023-.018-.024-.019-.024-.02-.025-.021-.024-.023-.024-.023-.025-.051-.05-.056-.05-.06-.05-.065-.051-.07-.052-.074-.051-.079-.052-.083-.052-.088-.052-.092-.052-.096-.052-.101-.052-.106-.052-.11-.052-.114-.052-.118-.051-.123-.051-.126-.051-.131-.05-.136-.05-.139-.049-.143-.048-.148-.048-.152-.048-.155-.046-.16-.046-.163-.045-.168-.043-.172-.043-.175-.042-.179-.041-.183-.04-.187-.038-.191-.038-.194-.036-.198-.034-.202-.033-.205-.032-.21-.031-.212-.028-.216-.027-.22-.026-.224-.023-.226-.022-.231-.021-.233-.018-.237-.016-.241-.014-.244-.012-.247-.011-.25-.008-.254-.005-.257-.004-.26-.001-.26.001z"></path></symbol></defs><defs><symbol id="clock" width="24" height="24"><path transform="scale(.5)" d="M12 2c5.514 0 10 4.486 10 10s-4.486 10-10 10-10-4.486-10-10 4.486-10 10-10zm0-2c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm5.848 12.459c.202.038.202.333.001.372-1.907.361-6.045 1.111-6.547 1.111-.719 0-1.301-.582-1.301-1.301 0-.512.77-5.447 1.125-7.445.034-.192.312-.181.343.014l.985 6.238 5.394 1.011z"></path></symbol></defs><defs><marker id="arrowhead" refX="7.9" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" orient="auto-start-reverse"><path d="M -1 0 L 10 5 L 0 10 z"></path></marker></defs><defs><marker id="crosshead" markerWidth="15" markerHeight="8" orient="auto" refX="4" refY="4.5"><path fill="none" stroke="#000000" stroke-width="1pt" d="M 1,2 L 6,7 M 6,2 L 1,7" style="stroke-dasharray:0, 0"></path></marker></defs><defs><marker id="filled-head" refX="15.5" refY="7" markerWidth="20" markerHeight="28" orient="auto"><path d="M 18,7 L9,13 L14,7 L9,1 Z"></path></marker></defs><defs><marker id="sequencenumber" refX="15" refY="15" markerWidth="60" markerHeight="40" orient="auto"><circle cx="15" cy="15" r="6"></circle></marker></defs><g><rect x="200" y="220" fill="#EDF2AE" stroke="#666" width="150" height="77" class="note"></rect><text x="275" y="225" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="noteText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400"><tspan x="275">window,</tspan></text><text x="275" y="244" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="noteText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400"><tspan x="275">document</tspan></text><text x="275" y="263" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="noteText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400"><tspan x="275">undefined</tspan></text></g><g><rect x="0" y="452" fill="#EDF2AE" stroke="#666" width="150" height="58" class="note"></rect><text x="75" y="457" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="noteText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400"><tspan x="75">Browser APIs</tspan></text><text x="75" y="476" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="noteText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400"><tspan x="75">available</tspan></text></g><text x="174" y="80" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">Request page</text><line x1="76" y1="113" x2="271" y2="113" class="messageLine0" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="fill:none"></line><text x="276" y="128" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">Run Vue code (no</text><text x="276" y="147" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">window!)</text><path d="M 276,180 C 336,170 336,210 276,200" class="messageLine1" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="stroke-dasharray:3, 3;fill:none"></path><text x="177" y="312" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">Send HTML</text><line x1="274" y1="345" x2="79" y2="345" class="messageLine1" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="stroke-dasharray:3, 3;fill:none"></line><text x="76" y="360" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">Hydrate app (has</text><text x="76" y="379" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">window)</text><path d="M 76,412 C 136,402 136,442 76,432" class="messageLine1" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="stroke-dasharray:3, 3;fill:none"></path></svg></p>
<h3 id="solution-create-ssr-utilities">Solution: Create SSR Utilities<a class="heading-link" aria-label="Link to section" href="#solution-create-ssr-utilities"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// src/composables/utils/ssr.ts</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">/**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * Check if code is running in browser</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> */</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#9D7CD8;font-style:italic"> const</span><span style="color:#BB9AF7"> isClient</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> typeof</span><span style="color:#C0CAF5"> window</span><span style="color:#BB9AF7"> !==</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">undefined</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">/**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * Check if code is running on server</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> */</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#9D7CD8;font-style:italic"> const</span><span style="color:#BB9AF7"> isServer</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7"> !</span><span style="color:#C0CAF5">isClient</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">/**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * Safe window reference (undefined on server)</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> */</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#9D7CD8;font-style:italic"> const</span><span style="color:#BB9AF7"> defaultWindow</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> isClient</span><span style="color:#BB9AF7"> ?</span><span style="color:#C0CAF5"> window</span><span style="color:#BB9AF7"> :</span><span style="color:#FF9E64"> undefined</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">/**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * Safe document reference (undefined on server)</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> */</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#9D7CD8;font-style:italic"> const</span><span style="color:#BB9AF7"> defaultDocument</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> isClient</span><span style="color:#BB9AF7"> ?</span><span style="color:#C0CAF5"> document</span><span style="color:#BB9AF7"> :</span><span style="color:#FF9E64"> undefined</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">/**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * Safe localStorage reference (undefined on server)</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> */</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#9D7CD8;font-style:italic"> const</span><span style="color:#BB9AF7"> defaultStorage</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> isClient</span><span style="color:#BB9AF7"> ?</span><span style="color:#C0CAF5"> localStorage</span><span style="color:#BB9AF7"> :</span><span style="color:#FF9E64"> undefined</span></span></code><button type="button" class="copy" data-code="// src/composables/utils/ssr.ts

/**
 * Check if code is running in browser
 */
export const isClient = typeof window !== 'undefined'

/**
 * Check if code is running on server
 */
export const isServer = !isClient

/**
 * Safe window reference (undefined on server)
 */
export const defaultWindow = isClient ? window : undefined

/**
 * Safe document reference (undefined on server)
 */
export const defaultDocument = isClient ? document : undefined

/**
 * Safe localStorage reference (undefined on server)
 */
export const defaultStorage = isClient ? localStorage : undefined" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="using-ssr-utilities">Using SSR Utilities<a class="heading-link" aria-label="Link to section" href="#using-ssr-utilities"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">defaultWindow</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> type</span><span style="color:#0DB9D7"> ConfigurableWindow</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">../utils/ssr</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> interface</span><span style="color:#C0CAF5"> UseWindowSizeOptions</span><span style="color:#9D7CD8;font-style:italic"> extends</span><span style="color:#BB9AF7"> ConfigurableWindow</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  initialWidth</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> number</span></span>
<span class="line"><span style="color:#73DACA">  initialHeight</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> number</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useWindowSize</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">options</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> UseWindowSizeOptions</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {})</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#89DDFF"> {</span></span>
<span class="line"><span style="color:#BB9AF7">    window</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> defaultWindow</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#BB9AF7">    initialWidth</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> Infinity</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#BB9AF7">    initialHeight</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> Infinity</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">  }</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> options</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> width</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> shallowRef</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">initialWidth</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> height</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> shallowRef</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">initialHeight</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#7AA2F7"> update</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">    // Guard: Only run if window exists</span></span>
<span class="line"><span style="color:#BB9AF7">    if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">window</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">      width</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> window</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">innerWidth</span></span>
<span class="line"><span style="color:#C0CAF5">      height</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> window</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">innerHeight</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Only set up listeners on client</span></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">window</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#7AA2F7">    update</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#C0CAF5">    window</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">addEventListener</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">resize</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> update</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">    onUnmounted</span><span style="color:#9ABDF5">(() </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">      window</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">removeEventListener</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">resize</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> update</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">    })</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> { </span><span style="color:#C0CAF5">width</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> height</span><span style="color:#9ABDF5"> }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="import { defaultWindow, type ConfigurableWindow } from '../utils/ssr'

export interface UseWindowSizeOptions extends ConfigurableWindow {
  initialWidth?: number
  initialHeight?: number
}

export function useWindowSize(options: UseWindowSizeOptions = {}) {
  const {
    window = defaultWindow,
    initialWidth = Infinity,
    initialHeight = Infinity,
  } = options

  const width = shallowRef(initialWidth)
  const height = shallowRef(initialHeight)

  const update = () => {
    // Guard: Only run if window exists
    if (window) {
      width.value = window.innerWidth
      height.value = window.innerHeight
    }
  }

  // Only set up listeners on client
  if (window) {
    update()
    window.addEventListener('resize', update)

    onUnmounted(() => {
      window.removeEventListener('resize', update)
    })
  }

  return { width, height }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="feature-detection">Feature Detection<a class="heading-link" aria-label="Link to section" href="#feature-detection"><span class="heading-link-icon">#</span></a></h3>
<p>Create a utility to safely check for browser features:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useSupported</span><span style="color:#9ABDF5">(</span><span style="color:#7AA2F7">check</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> boolean</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Readonly</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Ref</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">boolean</span><span style="color:#89DDFF">&gt;&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> isSupported</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> shallowRef</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">false</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  onMounted</span><span style="color:#9ABDF5">(() </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">    isSupported</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> check</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#7AA2F7"> readonly</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">isSupported</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Usage</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useClipboard</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> isSupported</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> useSupported</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#9ABDF5">    () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#C0CAF5"> navigator</span><span style="color:#BB9AF7"> &amp;&amp;</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">clipboard</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF"> in</span><span style="color:#C0CAF5"> navigator</span></span>
<span class="line"><span style="color:#9ABDF5">  )</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#7AA2F7"> copy</span><span style="color:#89DDFF"> =</span><span style="color:#9D7CD8;font-style:italic"> async</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">text</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">    if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#C0CAF5">isSupported</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">      console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">warn</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">Clipboard API not supported</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">      return</span><span style="color:#FF9E64"> false</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">    // ... implementation</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> { </span><span style="color:#C0CAF5">isSupported</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> copy</span><span style="color:#9ABDF5"> }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="export function useSupported(check: () => boolean): Readonly<Ref<boolean>> {
  const isSupported = shallowRef(false)

  onMounted(() => {
    isSupported.value = check()
  })

  return readonly(isSupported)
}

// Usage
export function useClipboard() {
  const isSupported = useSupported(
    () => navigator &#38;&#38; 'clipboard' in navigator
  )

  const copy = async (text: string) => {
    if (!isSupported.value) {
      console.warn('Clipboard API not supported')
      return false
    }
    // ... implementation
  }

  return { isSupported, copy }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr/>
<h2 id="9-cleanup-and-memory-management">9. Cleanup and Memory Management<a class="heading-link" aria-label="Link to section" href="#9-cleanup-and-memory-management"><span class="heading-link-icon">#</span></a></h2>
<h3 id="the-problem-1">The Problem<a class="heading-link" aria-label="Link to section" href="#the-problem-1"><span class="heading-link-icon">#</span></a></h3>
<p>Event listeners, timers, and observers must be cleaned up to prevent memory leaks.</p>
<p><svg id="mermaid-2" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="flowchart" style="max-width:1754.390625px" viewBox="0 0 1754.390625 278" role="graphics-document document" aria-roledescription="flowchart-v2"><style>#mermaid-2{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-2 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-2 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-2 .error-icon{fill:#a44141;}#mermaid-2 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-2 .edge-thickness-normal{stroke-width:1px;}#mermaid-2 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-2 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-2 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-2 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-2 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-2 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-2 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-2 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-2 p{margin:0;}#mermaid-2 .label{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;color:#ccc;}#mermaid-2 .cluster-label text{fill:#F9FFFE;}#mermaid-2 .cluster-label span{color:#F9FFFE;}#mermaid-2 .cluster-label span p{background-color:transparent;}#mermaid-2 .label text,#mermaid-2 span{fill:#ccc;color:#ccc;}#mermaid-2 .node rect,#mermaid-2 .node circle,#mermaid-2 .node ellipse,#mermaid-2 .node polygon,#mermaid-2 .node path{fill:transparent;stroke:2px;stroke-width:1px;}#mermaid-2 .rough-node .label text,#mermaid-2 .node .label text,#mermaid-2 .image-shape .label,#mermaid-2 .icon-shape .label{text-anchor:middle;}#mermaid-2 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-2 .rough-node .label,#mermaid-2 .node .label,#mermaid-2 .image-shape .label,#mermaid-2 .icon-shape .label{text-align:center;}#mermaid-2 .node.clickable{cursor:pointer;}#mermaid-2 .root .anchor path{fill:rgb(171, 75, 153)!important;stroke-width:0;stroke:rgb(171, 75, 153);}#mermaid-2 .arrowheadPath{fill:lightgrey;}#mermaid-2 .edgePath .path{stroke:rgb(171, 75, 153);stroke-width:2.0px;}#mermaid-2 .flowchart-link{stroke:rgb(171, 75, 153);fill:none;}#mermaid-2 .edgeLabel{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-2 .edgeLabel p{background-color:hsla(0, 0%, 25%, 0);}#mermaid-2 .edgeLabel rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-2 .labelBkg{background-color:rgba(63.75, 63.75, 63.75, 0.5);}#mermaid-2 .cluster rect{fill:transparent;stroke:rgba(255, 255, 255, 0.25);stroke-width:1px;}#mermaid-2 .cluster text{fill:#F9FFFE;}#mermaid-2 .cluster span{color:#F9FFFE;}#mermaid-2 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:12px;background:rgb(138, 51, 123);border:1px solid rgba(255, 255, 255, 0.25);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-2 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-2 rect.text{fill:none;stroke-width:0;}#mermaid-2 .icon-shape,#mermaid-2 .image-shape{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-2 .icon-shape p,#mermaid-2 .image-shape p{background-color:hsla(0, 0%, 25%, 0);padding:2px;}#mermaid-2 .icon-shape rect,#mermaid-2 .image-shape rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-2 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-2 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-2 :root{--mermaid-font-family:arial,sans-serif;}</style><g><marker id="mermaid-2_flowchart-v2-pointEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-2_flowchart-v2-pointStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="4.5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 5 L 10 10 L 10 0 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-2_flowchart-v2-circleEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="11" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-2_flowchart-v2-circleStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="-1" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-2_flowchart-v2-crossEnd" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="12" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-2_flowchart-v2-crossStart" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="-1" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><g class="root"><g class="clusters"></g><g class="edgePaths"><path d="M241.391,139L245.557,139C249.724,139,258.057,139,265.724,139C273.391,139,280.391,139,283.891,139L287.391,139" id="L_A_B_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_A_B_0" data-points="W3sieCI6MjQxLjM5MDYyNSwieSI6MTM5fSx7IngiOjI2Ni4zOTA2MjUsInkiOjEzOX0seyJ4IjoyOTEuMzkwNjI1LCJ5IjoxMzl9XQ==" marker-end="url(#mermaid-2_flowchart-v2-pointEnd)"></path><path d="M524.781,139L528.948,139C533.115,139,541.448,139,549.115,139C556.781,139,563.781,139,567.281,139L570.781,139" id="L_B_C_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_B_C_0" data-points="W3sieCI6NTI0Ljc4MTI1LCJ5IjoxMzl9LHsieCI6NTQ5Ljc4MTI1LCJ5IjoxMzl9LHsieCI6NTc0Ljc4MTI1LCJ5IjoxMzl9XQ==" marker-end="url(#mermaid-2_flowchart-v2-pointEnd)"></path><path d="M834.781,126.366L840.553,125.805C846.326,125.244,857.87,124.122,870.641,124.27C883.413,124.418,897.412,125.836,904.411,126.545L911.41,127.254" id="L_C_D_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_C_D_0" data-points="W3sieCI6ODM0Ljc4MTI1LCJ5IjoxMjYuMzY1ODIzNTY1NzAwMTh9LHsieCI6ODY5LjQxNDA2MjUsInkiOjEyM30seyJ4Ijo5MTUuMzg5OTM4NzI2NTkwOSwieSI6MTI3LjY1NjkzNjI3MzQwOTA5fV0=" marker-end="url(#mermaid-2_flowchart-v2-pointEnd)"></path><path d="M1150.703,139L1157.279,139C1163.854,139,1177.005,139,1189.49,139C1201.974,139,1213.792,139,1219.701,139L1225.609,139" id="L_D_E_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_D_E_0" data-points="W3sieCI6MTE1MC43MDMxMjUsInkiOjEzOX0seyJ4IjoxMTkwLjE1NjI1LCJ5IjoxMzl9LHsieCI6MTIyOS42MDkzNzUsInkiOjEzOX1d" marker-end="url(#mermaid-2_flowchart-v2-pointEnd)"></path><path d="M915.39,150.343L907.727,151.119C900.065,151.895,884.739,153.448,871.968,153.727C859.197,154.007,848.98,153.014,843.871,152.518L838.762,152.021" id="L_D_C_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_D_C_0" data-points="W3sieCI6OTE1LjM4OTkzODcyNjU5MDksInkiOjE1MC4zNDMwNjM3MjY1OTA5fSx7IngiOjg2OS40MTQwNjI1LCJ5IjoxNTV9LHsieCI6ODM0Ljc4MTI1LCJ5IjoxNTEuNjM0MTc2NDM0Mjk5OH1d" marker-end="url(#mermaid-2_flowchart-v2-pointEnd)"></path><path d="M1370.957,112L1387.254,99.167C1403.55,86.333,1436.142,60.667,1459.149,47.833C1482.156,35,1495.578,35,1502.289,35L1509,35" id="L_E_F_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_E_F_0" data-points="W3sieCI6MTM3MC45NTczMzE3MzA3NjkzLCJ5IjoxMTJ9LHsieCI6MTQ2OC43MzQzNzUsInkiOjM1fSx7IngiOjE1MTMsInkiOjM1fV0=" marker-end="url(#mermaid-2_flowchart-v2-pointEnd)"></path><path d="M1443.734,139L1447.901,139C1452.068,139,1460.401,139,1474.49,139C1488.578,139,1508.422,139,1518.344,139L1528.266,139" id="L_E_G_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_E_G_0" data-points="W3sieCI6MTQ0My43MzQzNzUsInkiOjEzOX0seyJ4IjoxNDY4LjczNDM3NSwieSI6MTM5fSx7IngiOjE1MzIuMjY1NjI1LCJ5IjoxMzl9XQ==" marker-end="url(#mermaid-2_flowchart-v2-pointEnd)"></path><path d="M1370.957,166L1387.254,178.833C1403.55,191.667,1436.142,217.333,1455.938,230.167C1475.734,243,1482.734,243,1486.234,243L1489.734,243" id="L_E_H_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_E_H_0" data-points="W3sieCI6MTM3MC45NTczMzE3MzA3NjkzLCJ5IjoxNjZ9LHsieCI6MTQ2OC43MzQzNzUsInkiOjI0M30seyJ4IjoxNDkzLjczNDM3NSwieSI6MjQzfV0=" marker-end="url(#mermaid-2_flowchart-v2-pointEnd)"></path></g><g class="edgeLabels"><g class="edgeLabel"><g class="label" data-id="L_A_B_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_B_C_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_C_D_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(1190.15625, 139)"><g class="label" data-id="L_D_E_0" transform="translate(-14.453125, -12)"><foreignObject width="28.90625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>Yes</p></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(875.09258, 154.42482)"><g class="label" data-id="L_D_C_0" transform="translate(-9.6328125, -12)"><foreignObject width="19.265625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>No</p></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_E_F_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_E_G_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_E_H_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g></g><g class="nodes"><g class="node default" id="flowchart-A-0" transform="translate(124.6953125, 139)"><rect class="basic label-container" style="" x="-116.6953125" y="-27" width="233.390625" height="54"></rect><g class="label" style="" transform="translate(-86.6953125, -12)"><rect></rect><foreignObject width="173.390625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Composable Created</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-B-1" transform="translate(408.0859375, 139)"><rect class="basic label-container" style="" x="-116.6953125" y="-27" width="233.390625" height="54"></rect><g class="label" style="" transform="translate(-86.6953125, -12)"><rect></rect><foreignObject width="173.390625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Register Resources</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-C-3" transform="translate(704.78125, 139)"><rect class="basic label-container" style="" x="-130" y="-39" width="260" height="78"></rect><g class="label" style="" transform="translate(-100, -24)"><rect></rect><foreignObject width="200" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table;white-space:break-spaces;line-height:1.5;max-width:200px;text-align:center;width:200px"><span class="nodeLabel"><p>Listeners, Timers, etc.</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-D-5" transform="translate(1027.375, 139)"><polygon points="123.328125,0 246.65625,-123.328125 123.328125,-246.65625 0,-123.328125" class="label-container" transform="translate(-122.828125, 123.328125)"></polygon><g class="label" style="" transform="translate(-96.328125, -12)"><rect></rect><foreignObject width="192.65625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Component Unmounted?</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-E-7" transform="translate(1336.671875, 139)"><rect class="basic label-container" style="fill:#ef4444 !important" x="-107.0625" y="-27" width="214.125" height="54"></rect><g class="label" style="color:#fff !important" transform="translate(-77.0625, -12)"><rect></rect><foreignObject width="154.125" height="24"><div style="color:rgb(255, 255, 255) !important;display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center" xmlns="http://www.w3.org/1999/xhtml"><span style="color:#fff !important" class="nodeLabel"><p>Cleanup Required</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-F-11" transform="translate(1620.0625, 35)"><rect class="basic label-container" style="fill:#22c55e !important" x="-107.0625" y="-27" width="214.125" height="54"></rect><g class="label" style="color:#fff !important" transform="translate(-77.0625, -12)"><rect></rect><foreignObject width="154.125" height="24"><div style="color:rgb(255, 255, 255) !important;display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center" xmlns="http://www.w3.org/1999/xhtml"><span style="color:#fff !important" class="nodeLabel"><p>Remove Listeners</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-G-13" transform="translate(1620.0625, 139)"><rect class="basic label-container" style="fill:#22c55e !important" x="-87.796875" y="-27" width="175.59375" height="54"></rect><g class="label" style="color:#fff !important" transform="translate(-57.796875, -12)"><rect></rect><foreignObject width="115.59375" height="24"><div style="color:rgb(255, 255, 255) !important;display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center" xmlns="http://www.w3.org/1999/xhtml"><span style="color:#fff !important" class="nodeLabel"><p>Clear Timers</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-H-15" transform="translate(1620.0625, 243)"><rect class="basic label-container" style="fill:#22c55e !important" x="-126.328125" y="-27" width="252.65625" height="54"></rect><g class="label" style="color:#fff !important" transform="translate(-96.328125, -12)"><rect></rect><foreignObject width="192.65625" height="24"><div style="color:rgb(255, 255, 255) !important;display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center" xmlns="http://www.w3.org/1999/xhtml"><span style="color:#fff !important" class="nodeLabel"><p>Disconnect Observers</p></span></div></foreignObject></g></g></g></g></g></svg></p>
<h3 id="solution-auto-cleanup-utility">Solution: Auto-Cleanup Utility<a class="heading-link" aria-label="Link to section" href="#solution-auto-cleanup-utility"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// src/composables/utils/cleanup.ts</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">getCurrentScope</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> onScopeDispose</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">/**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * Register a cleanup function that runs when the scope is disposed.</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * Safe to call outside of component context.</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> *</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * </span><span style="color:#646E9C;font-style:italic">@returns</span><span style="color:#51597D;font-style:italic"> true if cleanup was registered, false otherwise</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> */</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> tryOnCleanup</span><span style="color:#9ABDF5">(</span><span style="color:#7AA2F7">fn</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> boolean</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#7AA2F7">getCurrentScope</span><span style="color:#9ABDF5">()) {</span></span>
<span class="line"><span style="color:#7AA2F7">    onScopeDispose</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">fn</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#FF9E64"> true</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#FF9E64"> false</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">/**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * Safe onMounted that doesn&#39;t error outside component context</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> */</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> tryOnMounted</span><span style="color:#9ABDF5">(</span><span style="color:#7AA2F7">fn</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> void</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#7AA2F7">getCurrentScope</span><span style="color:#9ABDF5">()) {</span></span>
<span class="line"><span style="color:#7AA2F7">    onMounted</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">fn</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// src/composables/utils/cleanup.ts
import { getCurrentScope, onScopeDispose } from 'vue'

/**
 * Register a cleanup function that runs when the scope is disposed.
 * Safe to call outside of component context.
 *
 * @returns true if cleanup was registered, false otherwise
 */
export function tryOnCleanup(fn: () => void): boolean {
  if (getCurrentScope()) {
    onScopeDispose(fn)
    return true
  }
  return false
}

/**
 * Safe onMounted that doesn't error outside component context
 */
export function tryOnMounted(fn: () => void): void {
  if (getCurrentScope()) {
    onMounted(fn)
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="using-auto-cleanup">Using Auto-Cleanup<a class="heading-link" aria-label="Link to section" href="#using-auto-cleanup"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">tryOnCleanup</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">../utils/cleanup</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useInterval</span><span style="color:#9ABDF5">(</span><span style="color:#7AA2F7">callback</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> ms</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  let</span><span style="color:#BB9AF7"> timer</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> ReturnType</span><span style="color:#89DDFF">&lt;typeof</span><span style="color:#C0CAF5"> setInterval</span><span style="color:#89DDFF">&gt;</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> null</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#7AA2F7"> start</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">    stop</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#C0CAF5">    timer</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> setInterval</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">callback</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> ms</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#7AA2F7"> stop</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">    if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">timer</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#7AA2F7">      clearInterval</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">timer</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#C0CAF5">      timer</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> null</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  start</span><span style="color:#9ABDF5">()</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Automatically stops when component unmounts</span></span>
<span class="line"><span style="color:#7AA2F7">  tryOnCleanup</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">stop</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> { </span><span style="color:#C0CAF5">start</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> stop</span><span style="color:#9ABDF5"> }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="import { tryOnCleanup } from '../utils/cleanup'

export function useInterval(callback: () => void, ms: number) {
  let timer: ReturnType<typeof setInterval> | null = null

  const start = () => {
    stop()
    timer = setInterval(callback, ms)
  }

  const stop = () => {
    if (timer) {
      clearInterval(timer)
      timer = null
    }
  }

  start()

  // Automatically stops when component unmounts
  tryOnCleanup(stop)

  return { start, stop }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="event-listener-composable-with-auto-cleanup">Event Listener Composable with Auto-Cleanup<a class="heading-link" aria-label="Link to section" href="#event-listener-composable-with-auto-cleanup"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useEventListener</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">K</span><span style="color:#9D7CD8;font-style:italic"> extends</span><span style="color:#89DDFF"> keyof</span><span style="color:#C0CAF5"> WindowEventMap</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#E0AF68">  event</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> K</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#7AA2F7">  handler</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">event</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> WindowEventMap</span><span style="color:#9ABDF5">[</span><span style="color:#C0CAF5">K</span><span style="color:#9ABDF5">])</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#E0AF68">  options</span><span style="color:#89DDFF">?:</span><span style="color:#C0CAF5"> AddEventListenerOptions</span><span style="color:#89DDFF"> &amp;</span><span style="color:#C0CAF5"> ConfigurableWindow</span></span>
<span class="line"><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> window</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> defaultWindow</span><span style="color:#89DDFF">,</span><span style="color:#F7768E;font-weight:bold"> ...</span><span style="color:#BB9AF7">listenerOptions</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> options</span><span style="color:#BB9AF7"> ??</span><span style="color:#9ABDF5"> {}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  let</span><span style="color:#7AA2F7"> cleanup</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">window</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">    window</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">addEventListener</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">event</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> handler</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> listenerOptions</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#7AA2F7">    cleanup</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#C0CAF5"> window</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">removeEventListener</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">event</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> handler</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> listenerOptions</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  tryOnCleanup</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">cleanup</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#C0CAF5"> cleanup</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="export function useEventListener<K extends keyof WindowEventMap>(
  event: K,
  handler: (event: WindowEventMap[K]) => void,
  options?: AddEventListenerOptions &#38; ConfigurableWindow
): () => void {
  const { window = defaultWindow, ...listenerOptions } = options ?? {}

  let cleanup = () => {}

  if (window) {
    window.addEventListener(event, handler, listenerOptions)
    cleanup = () => window.removeEventListener(event, handler, listenerOptions)
  }

  tryOnCleanup(cleanup)

  return cleanup
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr/>
<h2 id="10-controllable-composables">10. Controllable Composables<a class="heading-link" aria-label="Link to section" href="#10-controllable-composables"><span class="heading-link-icon">#</span></a></h2>
<h3 id="pausable-pattern">Pausable Pattern<a class="heading-link" aria-label="Link to section" href="#pausable-pattern"><span class="heading-link-icon">#</span></a></h3>
<p><svg id="mermaid-3" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="statediagram" style="max-width:333.9140625px" viewBox="0 0 333.9140625 346" role="graphics-document document" aria-roledescription="stateDiagram"><style>#mermaid-3{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-3 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-3 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-3 .error-icon{fill:#a44141;}#mermaid-3 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-3 .edge-thickness-normal{stroke-width:1px;}#mermaid-3 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-3 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-3 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-3 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-3 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-3 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-3 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-3 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-3 p{margin:0;}#mermaid-3 defs #statediagram-barbEnd{fill:lightgrey;stroke:lightgrey;}#mermaid-3 g.stateGroup text{fill:2px;stroke:none;font-size:10px;}#mermaid-3 g.stateGroup text{fill:#ccc;stroke:none;font-size:10px;}#mermaid-3 g.stateGroup .state-title{font-weight:bolder;fill:rgb(234, 237, 243);}#mermaid-3 g.stateGroup rect{fill:transparent;stroke:2px;}#mermaid-3 g.stateGroup line{stroke:rgb(171, 75, 153);stroke-width:1;}#mermaid-3 .transition{stroke:lightgrey;stroke-width:1;fill:none;}#mermaid-3 .stateGroup .composit{fill:#333;border-bottom:1px;}#mermaid-3 .stateGroup .alt-composit{fill:#e0e0e0;border-bottom:1px;}#mermaid-3 .state-note{stroke:hsl(180, 0%, 18.3529411765%);fill:hsla(0, 0%, 16%, 0);}#mermaid-3 .state-note text{fill:rgb(183.8476190475, 181.5523809523, 181.5523809523);stroke:none;font-size:10px;}#mermaid-3 .stateLabel .box{stroke:none;stroke-width:0;fill:transparent;opacity:0.5;}#mermaid-3 .edgeLabel .label rect{fill:transparent;opacity:0.5;}#mermaid-3 .edgeLabel{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-3 .edgeLabel p{background-color:hsla(0, 0%, 25%, 0);}#mermaid-3 .edgeLabel rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-3 .edgeLabel .label text{fill:#ccc;}#mermaid-3 .label div .edgeLabel{color:#ccc;}#mermaid-3 .stateLabel text{fill:rgb(234, 237, 243);font-size:10px;font-weight:bold;}#mermaid-3 .node circle.state-start{fill:#f4f4f4;stroke:#f4f4f4;}#mermaid-3 .node .fork-join{fill:#f4f4f4;stroke:#f4f4f4;}#mermaid-3 .node circle.state-end{fill:rgb(171, 75, 153);stroke:#333;stroke-width:1.5;}#mermaid-3 .end-state-inner{fill:#333;stroke-width:1.5;}#mermaid-3 .node rect{fill:transparent;stroke:2px;stroke-width:1px;}#mermaid-3 .node polygon{fill:transparent;stroke:2px;stroke-width:1px;}#mermaid-3 #statediagram-barbEnd{fill:rgb(171, 75, 153);}#mermaid-3 .statediagram-cluster rect{fill:transparent;stroke:2px;stroke-width:1px;}#mermaid-3 .cluster-label,#mermaid-3 .nodeLabel{color:rgb(234, 237, 243);}#mermaid-3 .statediagram-cluster rect.outer{rx:5px;ry:5px;}#mermaid-3 .statediagram-state .divider{stroke:2px;}#mermaid-3 .statediagram-state .title-state{rx:5px;ry:5px;}#mermaid-3 .statediagram-cluster.statediagram-cluster .inner{fill:#333;}#mermaid-3 .statediagram-cluster.statediagram-cluster-alt .inner{fill:#555;}#mermaid-3 .statediagram-cluster .inner{rx:0;ry:0;}#mermaid-3 .statediagram-state rect.basic{rx:5px;ry:5px;}#mermaid-3 .statediagram-state rect.divider{stroke-dasharray:10,10;fill:#555;}#mermaid-3 .note-edge{stroke-dasharray:5;}#mermaid-3 .statediagram-note rect{fill:hsla(0, 0%, 16%, 0);stroke:hsl(180, 0%, 18.3529411765%);stroke-width:1px;rx:0;ry:0;}#mermaid-3 .statediagram-note rect{fill:hsla(0, 0%, 16%, 0);stroke:hsl(180, 0%, 18.3529411765%);stroke-width:1px;rx:0;ry:0;}#mermaid-3 .statediagram-note text{fill:rgb(183.8476190475, 181.5523809523, 181.5523809523);}#mermaid-3 .statediagram-note .nodeLabel{color:rgb(183.8476190475, 181.5523809523, 181.5523809523);}#mermaid-3 .statediagram .edgeLabel{color:red;}#mermaid-3 #dependencyStart,#mermaid-3 #dependencyEnd{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);stroke-width:1;}#mermaid-3 .statediagramTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-3 :root{--mermaid-font-family:arial,sans-serif;}</style><g><defs><marker id="mermaid-3_stateDiagram-barbEnd" refX="19" refY="7" markerWidth="20" markerHeight="14" markerUnits="userSpaceOnUse" orient="auto"><path d="M 19,7 L9,13 L14,7 L9,1 Z"></path></marker></defs><g class="root"><g class="clusters"></g><g class="edgePaths"><path d="M171.913,18.528L183.47,25.274C195.028,32.019,218.143,45.509,229.784,58.505C241.424,71.5,241.591,84,241.674,90.25L241.758,96.5" id="edge0" class="edge-thickness-normal edge-pattern-solid transition" style="fill:none" data-edge="true" data-et="edge" data-id="edge0" data-points="W3sieCI6MTcxLjkxMjg2NzA5MTkxNDQ4LCJ5IjoxOC41Mjg0MjE0OTg2MTc4NjN9LHsieCI6MjQxLjI1NzgxMjUsInkiOjU5fSx7IngiOjI0MS43NTc4MTI1LCJ5Ijo5Ni41fV0=" marker-end="url(#mermaid-3_stateDiagram-barbEnd)"></path><path d="M159.641,18.2L146.409,25C133.177,31.8,106.714,45.4,93.482,61.7C80.25,78,80.25,97,80.25,116C80.25,135,80.25,154,93.481,170.107C106.713,186.214,133.175,199.427,146.406,206.034L159.638,212.641" id="edge1" class="edge-thickness-normal edge-pattern-solid transition" style="fill:none" data-edge="true" data-et="edge" data-id="edge1" data-points="W3sieCI6MTU5LjY0MTIzNTcwODk3MDIsInkiOjE4LjE5OTYxMzE0NzgzMDk4OH0seyJ4Ijo4MC4yNSwieSI6NTl9LHsieCI6ODAuMjUsInkiOjExNn0seyJ4Ijo4MC4yNSwieSI6MTczfSx7IngiOjE1OS42Mzc1MTA4NTY0ODkxLCJ5IjoyMTIuNjQwNjUxNDI1MjkzNzV9XQ==" marker-end="url(#mermaid-3_stateDiagram-barbEnd)"></path><path d="M225.574,136.5L220.5,142.583C215.427,148.667,205.28,160.833,200.29,173.167C195.299,185.5,195.466,198,195.549,204.25L195.633,210.5" id="edge2" class="edge-thickness-normal edge-pattern-solid transition" style="fill:none" data-edge="true" data-et="edge" data-id="edge2" data-points="W3sieCI6MjI1LjU3MzYwMTk3MzY4NDIyLCJ5IjoxMzYuNX0seyJ4IjoxOTUuMTMyODEyNSwieSI6MTczfSx7IngiOjE5NS42MzI4MTI1LCJ5IjoyMTAuNX1d" marker-end="url(#mermaid-3_stateDiagram-barbEnd)"></path><path d="M227.969,210.52L237.871,204.267C247.773,198.013,267.578,185.507,272.574,173.17C277.569,160.833,267.756,148.667,262.849,142.583L257.942,136.5" id="edge3" class="edge-thickness-normal edge-pattern-solid transition" style="fill:none" data-edge="true" data-et="edge" data-id="edge3" data-points="W3sieCI6MjI3Ljk2ODY1MTQzMDQwNTM3LCJ5IjoyMTAuNTIwMTMyMDQzMDAxNTh9LHsieCI6Mjg3LjM4MjgxMjUsInkiOjE3M30seyJ4IjoyNTcuOTQyMDIzMDI2MzE1OCwieSI6MTM2LjV9XQ==" marker-end="url(#mermaid-3_stateDiagram-barbEnd)"></path><path d="M204.859,128.119L180.758,135.6C156.656,143.08,108.453,158.04,84.352,175.02C60.25,192,60.25,211,60.25,230C60.25,249,60.25,268,68.155,284.087C76.06,300.173,91.87,313.346,99.776,319.933L107.681,326.519" id="edge4" class="edge-thickness-normal edge-pattern-solid transition" style="fill:none" data-edge="true" data-et="edge" data-id="edge4" data-points="W3sieCI6MjA0Ljg1OTM3NSwieSI6MTI4LjExOTQ0ODQwMDg4MDV9LHsieCI6NjAuMjUsInkiOjE3M30seyJ4Ijo2MC4yNSwieSI6MjMwfSx7IngiOjYwLjI1LCJ5IjoyODd9LHsieCI6MTA3LjY4MDY4NjEzNDYxNjIsInkiOjMyNi41MTkxMzk2MjcyMTQ3N31d" marker-end="url(#mermaid-3_stateDiagram-barbEnd)"></path><path d="M195.633,250.5L195.549,256.583C195.466,262.667,195.299,274.833,182.565,287.699C169.831,300.564,144.53,314.128,131.879,320.911L119.228,327.693" id="edge5" class="edge-thickness-normal edge-pattern-solid transition" style="fill:none" data-edge="true" data-et="edge" data-id="edge5" data-points="W3sieCI6MTk1LjYzMjgxMjUsInkiOjI1MC41fSx7IngiOjE5NS4xMzI4MTI1LCJ5IjoyODd9LHsieCI6MTE5LjIyNzk2MjM4NTUxODIzLCJ5IjozMjcuNjkyNjAwNjIyOTg0M31d" marker-end="url(#mermaid-3_stateDiagram-barbEnd)"></path></g><g class="edgeLabels"><g class="edgeLabel" transform="translate(241.2578125, 59)"><g class="label" data-id="edge0" transform="translate(-67.4296875, -12)"><foreignObject width="134.859375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>immediate=true</p></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(80.25, 116)"><g class="label" data-id="edge1" transform="translate(-72.25, -12)"><foreignObject width="144.5" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>immediate=false</p></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(195.1328125, 173)"><g class="label" data-id="edge2" transform="translate(-33.71875, -12)"><foreignObject width="67.4375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>pause()</p></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(287.3828125, 173)"><g class="label" data-id="edge3" transform="translate(-38.53125, -12)"><foreignObject width="77.0625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>resume()</p></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(60.25, 230)"><g class="label" data-id="edge4" transform="translate(-33.71875, -12)"><foreignObject width="67.4375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>cleanup</p></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(195.1328125, 287)"><g class="label" data-id="edge5" transform="translate(-33.71875, -12)"><foreignObject width="67.4375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>cleanup</p></span></div></foreignObject></g></g></g><g class="nodes"><g class="node default" id="state-root_start-1" transform="translate(165.8671875, 15)"><circle class="state-start" r="7" width="14" height="14"></circle></g><g class="node statediagram-state" id="state-Active-4" transform="translate(241.2578125, 116)"><g class="basic label-container outer-path"><path d="M-31.8984375 -20 C-9.34893519686685 -20, 13.200567106266298 -20, 31.8984375 -20 M-31.8984375 -20 C-6.726671543657407 -20, 18.445094412685187 -20, 31.8984375 -20 M31.8984375 -20 C31.8984375 -20, 31.8984375 -20, 31.8984375 -20 M31.8984375 -20 C31.8984375 -20, 31.8984375 -20, 31.8984375 -20 M31.8984375 -20 C32.00817581439392 -19.99546118974297, 32.11791412878785 -19.990922379485937, 32.31133422736166 -19.982922465033347 M31.8984375 -20 C32.009590862764064 -19.995402662909456, 32.12074422552812 -19.99080532581891, 32.31133422736166 -19.982922465033347 M32.31133422736166 -19.982922465033347 C32.45674896731894 -19.964796536600595, 32.60216370727621 -19.94667060816784, 32.72141045140367 -19.931806517013612 M32.31133422736166 -19.982922465033347 C32.468081977004594 -19.96338387841649, 32.624829726647526 -19.943845291799633, 32.72141045140367 -19.931806517013612 M32.72141045140367 -19.931806517013612 C32.81795500672326 -19.91156325252744, 32.91449956204285 -19.891319988041264, 33.125864935703994 -19.847001329696653 M32.72141045140367 -19.931806517013612 C32.86140458497776 -19.902452834011275, 33.00139871855185 -19.873099151008933, 33.125864935703994 -19.847001329696653 M33.125864935703994 -19.847001329696653 C33.23467872359064 -19.8146060614577, 33.343492511477294 -19.782210793218745, 33.52193484602342 -19.729086208503173 M33.125864935703994 -19.847001329696653 C33.25641749789407 -19.80813414793991, 33.386970060084145 -19.769266966183167, 33.52193484602342 -19.729086208503173 M33.52193484602342 -19.729086208503173 C33.66957748299839 -19.67147587278417, 33.81722011997336 -19.613865537065166, 33.906914623264846 -19.578866633275286 M33.52193484602342 -19.729086208503173 C33.675870273461705 -19.669020418325832, 33.829805700899996 -19.608954628148492, 33.906914623264846 -19.578866633275286 M33.906914623264846 -19.578866633275286 C33.99853742816571 -19.534074973314112, 34.090160233066584 -19.489283313352942, 34.278174465185366 -19.397368756032446 M33.906914623264846 -19.578866633275286 C34.04609235047394 -19.510826788412825, 34.18527007768304 -19.442786943550363, 34.278174465185366 -19.397368756032446 M34.278174465185366 -19.397368756032446 C34.416883823238436 -19.314715918926, 34.555593181291506 -19.232063081819554, 34.633178290612136 -19.185832391312644 M34.278174465185366 -19.397368756032446 C34.39593291829909 -19.327199948536478, 34.513691371412804 -19.257031141040507, 34.633178290612136 -19.185832391312644 M34.633178290612136 -19.185832391312644 C34.73056831729942 -19.11629724877513, 34.82795834398671 -19.046762106237612, 34.96950106344834 -18.94570254698197 M34.633178290612136 -19.185832391312644 C34.76143610055337 -19.094258075141134, 34.88969391049461 -19.00268375896962, 34.96950106344834 -18.94570254698197 M34.96950106344834 -18.94570254698197 C35.03847123557862 -18.887287790940615, 35.10744140770889 -18.828873034899264, 35.284845358128706 -18.678619553365657 M34.96950106344834 -18.94570254698197 C35.07736981775448 -18.854342372392647, 35.18523857206061 -18.76298219780332, 35.284845358128706 -18.678619553365657 M35.284845358128706 -18.678619553365657 C35.37976890499565 -18.583696006498712, 35.474692451862595 -18.488772459631768, 35.57705705336566 -18.386407858128706 M35.284845358128706 -18.678619553365657 C35.3739284646279 -18.589536446866457, 35.463011571127105 -18.50045334036726, 35.57705705336566 -18.386407858128706 M35.57705705336566 -18.386407858128706 C35.67636591905864 -18.26915410197061, 35.77567478475163 -18.151900345812514, 35.84414004698197 -18.07106356344834 M35.57705705336566 -18.386407858128706 C35.67666949554804 -18.268795669886877, 35.776281937730424 -18.15118348164505, 35.84414004698197 -18.07106356344834 M35.84414004698197 -18.07106356344834 C35.934724407157965 -17.94419227314745, 36.02530876733397 -17.817320982846557, 36.084269891312644 -17.734740790612136 M35.84414004698197 -18.07106356344834 C35.940165029065994 -17.93657220804825, 36.03619001115001 -17.80208085264816, 36.084269891312644 -17.734740790612136 M36.084269891312644 -17.734740790612136 C36.12834833337115 -17.66076762022912, 36.17242677542966 -17.5867944498461, 36.29580625603245 -17.37973696518537 M36.084269891312644 -17.734740790612136 C36.16549263146528 -17.598431444916315, 36.24671537161791 -17.462122099220498, 36.29580625603245 -17.37973696518537 M36.29580625603245 -17.37973696518537 C36.3455246506612 -17.278036363443825, 36.39524304528994 -17.17633576170228, 36.47730413327529 -17.008477123264846 M36.29580625603245 -17.37973696518537 C36.366600284364424 -17.234925465642156, 36.4373943126964 -17.090113966098944, 36.47730413327529 -17.008477123264846 M36.47730413327529 -17.008477123264846 C36.516456289571934 -16.908138746014487, 36.55560844586858 -16.807800368764127, 36.627523708503176 -16.623497346023417 M36.47730413327529 -17.008477123264846 C36.53265130395982 -16.866634481194076, 36.587998474644344 -16.724791839123306, 36.627523708503176 -16.623497346023417 M36.627523708503176 -16.623497346023417 C36.664509137519076 -16.499265479871013, 36.701494566534976 -16.375033613718607, 36.74543882969665 -16.227427435703994 M36.627523708503176 -16.623497346023417 C36.66076404217817 -16.51184503337353, 36.69400437585317 -16.40019272072364, 36.74543882969665 -16.227427435703994 M36.74543882969665 -16.227427435703994 C36.76811893406796 -16.119261058061443, 36.79079903843926 -16.011094680418893, 36.83024401701361 -15.82297295140367 M36.74543882969665 -16.227427435703994 C36.77749804529577 -16.07453002550486, 36.8095572608949 -15.921632615305725, 36.83024401701361 -15.82297295140367 M36.83024401701361 -15.82297295140367 C36.84120785299319 -15.735015892331107, 36.852171688972774 -15.647058833258544, 36.88135996503335 -15.412896727361662 M36.83024401701361 -15.82297295140367 C36.84237694494418 -15.725636885751149, 36.85450987287474 -15.628300820098625, 36.88135996503335 -15.412896727361662 M36.88135996503335 -15.412896727361662 C36.88684548326262 -15.280269124538881, 36.89233100149189 -15.1476415217161, 36.8984375 -15 M36.88135996503335 -15.412896727361662 C36.88744362474034 -15.26580739694576, 36.89352728444733 -15.118718066529858, 36.8984375 -15 M36.8984375 -15 C36.8984375 -15, 36.8984375 -15, 36.8984375 -15 M36.8984375 -15 C36.8984375 -15, 36.8984375 -15, 36.8984375 -15 M36.8984375 -15 C36.8984375 -5.758602810852841, 36.8984375 3.4827943782943187, 36.8984375 15 M36.8984375 -15 C36.8984375 -4.968466673429976, 36.8984375 5.063066653140048, 36.8984375 15 M36.8984375 15 C36.8984375 15, 36.8984375 15, 36.8984375 15 M36.8984375 15 C36.8984375 15, 36.8984375 15, 36.8984375 15 M36.8984375 15 C36.89270966846371 15.138486198437384, 36.88698183692742 15.276972396874768, 36.88135996503335 15.412896727361662 M36.8984375 15 C36.892090488623474 15.153456586738756, 36.88574347724695 15.30691317347751, 36.88135996503335 15.412896727361662 M36.88135996503335 15.412896727361662 C36.86530616036969 15.541687913929094, 36.84925235570603 15.670479100496525, 36.83024401701361 15.822972951403669 M36.88135996503335 15.412896727361662 C36.8640940717876 15.551411859746475, 36.84682817854185 15.689926992131285, 36.83024401701361 15.822972951403669 M36.83024401701361 15.822972951403669 C36.81241370238135 15.90800962118367, 36.79458338774909 15.99304629096367, 36.74543882969665 16.227427435703994 M36.83024401701361 15.822972951403669 C36.81013521558459 15.91887622299808, 36.79002641415556 16.014779494592492, 36.74543882969665 16.227427435703994 M36.74543882969665 16.227427435703994 C36.71222619215296 16.33898671868873, 36.67901355460926 16.450546001673462, 36.627523708503176 16.623497346023417 M36.74543882969665 16.227427435703994 C36.71146116081008 16.341556413671853, 36.67748349192351 16.45568539163971, 36.627523708503176 16.623497346023417 M36.627523708503176 16.623497346023417 C36.56770092107758 16.776810010781855, 36.50787813365198 16.930122675540293, 36.47730413327529 17.008477123264846 M36.627523708503176 16.623497346023417 C36.58538047524999 16.731501196556433, 36.5432372419968 16.83950504708945, 36.47730413327529 17.008477123264846 M36.47730413327529 17.008477123264846 C36.42138632255591 17.122858833307895, 36.365468511836525 17.23724054335094, 36.29580625603245 17.379736965185366 M36.47730413327529 17.008477123264846 C36.41979702608864 17.12610979119328, 36.362289918901986 17.243742459121712, 36.29580625603245 17.379736965185366 M36.29580625603245 17.379736965185366 C36.23734363468919 17.47784990311367, 36.178881013345936 17.57596284104197, 36.084269891312644 17.734740790612133 M36.29580625603245 17.379736965185366 C36.244537524349376 17.46577699852137, 36.1932687926663 17.55181703185738, 36.084269891312644 17.734740790612133 M36.084269891312644 17.734740790612133 C36.01091251377939 17.837484190495417, 35.93755513624613 17.940227590378704, 35.84414004698197 18.07106356344834 M36.084269891312644 17.734740790612133 C36.009807380039334 17.839032026604023, 35.93534486876603 17.943323262595914, 35.84414004698197 18.07106356344834 M35.84414004698197 18.07106356344834 C35.78158853615557 18.144917992723908, 35.719037025329165 18.218772421999475, 35.57705705336566 18.386407858128706 M35.84414004698197 18.07106356344834 C35.73958721069696 18.194508863984744, 35.63503437441195 18.31795416452115, 35.57705705336566 18.386407858128706 M35.57705705336566 18.386407858128706 C35.46099930160973 18.502465609884627, 35.344941549853814 18.618523361640552, 35.284845358128706 18.678619553365657 M35.57705705336566 18.386407858128706 C35.51260104632935 18.45086386516501, 35.448145039293045 18.51531987220132, 35.284845358128706 18.678619553365657 M35.284845358128706 18.678619553365657 C35.194386737024416 18.755234097311746, 35.10392811592013 18.831848641257835, 34.96950106344834 18.94570254698197 M35.284845358128706 18.678619553365657 C35.20480635077279 18.746409134630678, 35.12476734341688 18.8141987158957, 34.96950106344834 18.94570254698197 M34.96950106344834 18.94570254698197 C34.896029287016695 18.998160387075426, 34.82255751058505 19.050618227168883, 34.633178290612136 19.185832391312644 M34.96950106344834 18.94570254698197 C34.84031465514303 19.037939869641953, 34.711128246837724 19.130177192301932, 34.633178290612136 19.185832391312644 M34.633178290612136 19.185832391312644 C34.504627977907255 19.26243175133502, 34.37607766520237 19.33903111135739, 34.278174465185366 19.397368756032446 M34.633178290612136 19.185832391312644 C34.53106317017857 19.246679795797576, 34.42894804974501 19.307527200282507, 34.278174465185366 19.397368756032446 M34.278174465185366 19.397368756032446 C34.14132581251587 19.464269985733374, 34.00447715984639 19.531171215434302, 33.906914623264846 19.578866633275286 M34.278174465185366 19.397368756032446 C34.1894945299681 19.44072173467055, 34.10081459475083 19.484074713308654, 33.906914623264846 19.578866633275286 M33.906914623264846 19.578866633275286 C33.790436039266744 19.624316717788084, 33.67395745526864 19.66976680230088, 33.52193484602342 19.729086208503173 M33.906914623264846 19.578866633275286 C33.81609619784183 19.61430409284178, 33.72527777241881 19.649741552408276, 33.52193484602342 19.729086208503173 M33.52193484602342 19.729086208503173 C33.38238750203212 19.770631252825506, 33.24284015804081 19.812176297147836, 33.125864935703994 19.847001329696653 M33.52193484602342 19.729086208503173 C33.39847366588599 19.765842194351364, 33.275012485748555 19.802598180199556, 33.125864935703994 19.847001329696653 M33.125864935703994 19.847001329696653 C32.98911278440148 19.875675240500904, 32.85236063309897 19.904349151305155, 32.72141045140367 19.931806517013612 M33.125864935703994 19.847001329696653 C33.03038196202353 19.8670220039205, 32.93489898834308 19.88704267814435, 32.72141045140367 19.931806517013612 M32.72141045140367 19.931806517013612 C32.61675728590565 19.944851520488744, 32.512104120407635 19.95789652396388, 32.31133422736166 19.982922465033347 M32.72141045140367 19.931806517013612 C32.56545702987798 19.951246090733914, 32.40950360835229 19.970685664454212, 32.31133422736166 19.982922465033347 M32.31133422736166 19.982922465033347 C32.22152118599183 19.9866371599021, 32.131708144621996 19.99035185477085, 31.8984375 20 M32.31133422736166 19.982922465033347 C32.165625111622056 19.98894903863906, 32.01991599588245 19.994975612244772, 31.8984375 20 M31.8984375 20 C31.8984375 20, 31.8984375 20, 31.8984375 20 M31.8984375 20 C31.8984375 20, 31.8984375 20, 31.8984375 20 M31.8984375 20 C8.974728495205959 20, -13.948980509588083 20, -31.8984375 20 M31.8984375 20 C12.172393746309318 20, -7.553650007381364 20, -31.8984375 20 M-31.8984375 20 C-31.8984375 20, -31.8984375 20, -31.8984375 20 M-31.8984375 20 C-31.8984375 20, -31.8984375 20, -31.8984375 20 M-31.8984375 20 C-31.989279852905888 19.996242732491208, -32.080122205811776 19.992485464982412, -32.31133422736166 19.982922465033347 M-31.8984375 20 C-32.023009851291555 19.99484764943851, -32.147582202583116 19.989695298877017, -32.31133422736166 19.982922465033347 M-32.31133422736166 19.982922465033347 C-32.44164299916856 19.966679493566865, -32.571951770975446 19.950436522100386, -32.72141045140367 19.931806517013612 M-32.31133422736166 19.982922465033347 C-32.41695437496688 19.96975692736425, -32.52257452257209 19.95659138969516, -32.72141045140367 19.931806517013612 M-32.72141045140367 19.931806517013612 C-32.81466398657825 19.91225330688632, -32.90791752175284 19.89270009675903, -33.125864935703994 19.847001329696653 M-32.72141045140367 19.931806517013612 C-32.80478582956804 19.91432453860241, -32.888161207732416 19.89684256019121, -33.125864935703994 19.847001329696653 M-33.125864935703994 19.847001329696653 C-33.23576232881926 19.814283458203757, -33.34565972193453 19.781565586710858, -33.52193484602342 19.729086208503173 M-33.125864935703994 19.847001329696653 C-33.23285490852373 19.815149034728446, -33.33984488134345 19.78329673976024, -33.52193484602342 19.729086208503173 M-33.52193484602342 19.729086208503173 C-33.66115146848535 19.6747637138497, -33.80036809094728 19.62044121919623, -33.906914623264846 19.578866633275286 M-33.52193484602342 19.729086208503173 C-33.61410760000299 19.69312028829404, -33.70628035398255 19.657154368084907, -33.906914623264846 19.578866633275286 M-33.906914623264846 19.578866633275286 C-34.01294842320971 19.527029867126732, -34.11898222315456 19.475193100978174, -34.278174465185366 19.397368756032446 M-33.906914623264846 19.578866633275286 C-34.05037659441345 19.508732349174288, -34.193838565562054 19.43859806507329, -34.278174465185366 19.397368756032446 M-34.278174465185366 19.397368756032446 C-34.35094204029529 19.354008692828273, -34.4237096154052 19.310648629624104, -34.633178290612136 19.185832391312644 M-34.278174465185366 19.397368756032446 C-34.378034975359576 19.337864807656896, -34.477895485533786 19.278360859281346, -34.633178290612136 19.185832391312644 M-34.633178290612136 19.185832391312644 C-34.72571605202271 19.119761699593376, -34.81825381343329 19.053691007874107, -34.96950106344834 18.94570254698197 M-34.633178290612136 19.185832391312644 C-34.72140804617667 19.122837556647188, -34.8096378017412 19.059842721981735, -34.96950106344834 18.94570254698197 M-34.96950106344834 18.94570254698197 C-35.06183121068727 18.86750290125633, -35.154161357926185 18.789303255530694, -35.284845358128706 18.67861955336566 M-34.96950106344834 18.94570254698197 C-35.04367672812849 18.882878963646384, -35.117852392808636 18.8200553803108, -35.284845358128706 18.67861955336566 M-35.284845358128706 18.67861955336566 C-35.35776674146765 18.605698170026713, -35.4306881248066 18.532776786687766, -35.57705705336566 18.386407858128706 M-35.284845358128706 18.67861955336566 C-35.378417881374126 18.58504703012024, -35.47199040461955 18.49147450687482, -35.57705705336566 18.386407858128706 M-35.57705705336566 18.386407858128706 C-35.642924927470474 18.308637806129372, -35.70879280157529 18.23086775413004, -35.84414004698197 18.07106356344834 M-35.57705705336566 18.386407858128706 C-35.6572529712518 18.291720716803713, -35.73744888913794 18.197033575478724, -35.84414004698197 18.07106356344834 M-35.84414004698197 18.07106356344834 C-35.9204635433911 17.964165855600232, -35.996787039800225 17.857268147752123, -36.084269891312644 17.734740790612133 M-35.84414004698197 18.07106356344834 C-35.925111905518506 17.957655419364393, -36.00608376405504 17.844247275280445, -36.084269891312644 17.734740790612133 M-36.084269891312644 17.734740790612133 C-36.139226920249214 17.642510995832332, -36.194183949185785 17.55028120105253, -36.29580625603244 17.37973696518537 M-36.084269891312644 17.734740790612133 C-36.13103031030663 17.656266682184434, -36.17779072930061 17.57779257375673, -36.29580625603244 17.37973696518537 M-36.29580625603244 17.37973696518537 C-36.359414572623876 17.249624073942186, -36.42302288921531 17.119511182699004, -36.47730413327528 17.00847712326485 M-36.29580625603244 17.37973696518537 C-36.344284952743536 17.280572206065948, -36.39276364945462 17.181407446946526, -36.47730413327528 17.00847712326485 M-36.47730413327528 17.00847712326485 C-36.53066875848453 16.87171530980304, -36.58403338369378 16.73495349634123, -36.627523708503176 16.623497346023417 M-36.47730413327528 17.00847712326485 C-36.5145908196707 16.912919535641525, -36.55187750606611 16.8173619480182, -36.627523708503176 16.623497346023417 M-36.627523708503176 16.623497346023417 C-36.65491318935247 16.53149770158531, -36.68230267020177 16.4394980571472, -36.74543882969665 16.227427435703994 M-36.627523708503176 16.623497346023417 C-36.66270930268353 16.505311018515158, -36.697894896863886 16.387124691006903, -36.74543882969665 16.227427435703994 M-36.74543882969665 16.227427435703994 C-36.764581437017576 16.136132155107397, -36.783724044338506 16.044836874510796, -36.83024401701361 15.82297295140367 M-36.74543882969665 16.227427435703994 C-36.76311037369667 16.143147977790612, -36.78078191769668 16.05886851987723, -36.83024401701361 15.82297295140367 M-36.83024401701361 15.82297295140367 C-36.84135160417557 15.733862652601537, -36.85245919133753 15.644752353799403, -36.88135996503335 15.412896727361664 M-36.83024401701361 15.82297295140367 C-36.847443272693084 15.684992416979327, -36.86464252837255 15.547011882554985, -36.88135996503335 15.412896727361664 M-36.88135996503335 15.412896727361664 C-36.88690911721692 15.278730597372432, -36.89245826940051 15.1445644673832, -36.8984375 15 M-36.88135996503335 15.412896727361664 C-36.885494159804374 15.31294111347671, -36.88962835457541 15.212985499591754, -36.8984375 15 M-36.8984375 15 C-36.8984375 15, -36.8984375 15, -36.8984375 15 M-36.8984375 15 C-36.8984375 15, -36.8984375 15, -36.8984375 15 M-36.8984375 15 C-36.8984375 3.4035714746243073, -36.8984375 -8.192857050751385, -36.8984375 -15 M-36.8984375 15 C-36.8984375 7.337462903406513, -36.8984375 -0.3250741931869747, -36.8984375 -15 M-36.8984375 -15 C-36.8984375 -15, -36.8984375 -15, -36.8984375 -15 M-36.8984375 -15 C-36.8984375 -15, -36.8984375 -15, -36.8984375 -15 M-36.8984375 -15 C-36.89448809714464 -15.095487757290206, -36.89053869428928 -15.190975514580412, -36.88135996503335 -15.41289672736166 M-36.8984375 -15 C-36.89364294822254 -15.115921574275495, -36.88884839644508 -15.23184314855099, -36.88135996503335 -15.41289672736166 M-36.88135996503335 -15.41289672736166 C-36.868763015584975 -15.513955392305954, -36.8561660661366 -15.61501405725025, -36.83024401701361 -15.822972951403669 M-36.88135996503335 -15.41289672736166 C-36.86998145308865 -15.50418051244765, -36.85860294114394 -15.59546429753364, -36.83024401701361 -15.822972951403669 M-36.83024401701361 -15.822972951403669 C-36.81185801268294 -15.910659826878796, -36.79347200835226 -15.998346702353922, -36.74543882969665 -16.227427435703994 M-36.83024401701361 -15.822972951403669 C-36.80786247092765 -15.92971543929192, -36.78548092484169 -16.036457927180173, -36.74543882969665 -16.227427435703994 M-36.74543882969665 -16.227427435703994 C-36.70110391116517 -16.376345801975038, -36.65676899263368 -16.52526416824608, -36.627523708503176 -16.623497346023417 M-36.74543882969665 -16.227427435703994 C-36.7087084319454 -16.35080266693889, -36.67197803419415 -16.47417789817379, -36.627523708503176 -16.623497346023417 M-36.627523708503176 -16.623497346023417 C-36.5875449340891 -16.725954163951226, -36.54756615967502 -16.82841098187903, -36.47730413327529 -17.008477123264846 M-36.627523708503176 -16.623497346023417 C-36.585345419132565 -16.731591037685693, -36.54316712976196 -16.83968472934797, -36.47730413327529 -17.008477123264846 M-36.47730413327529 -17.008477123264846 C-36.42799093764137 -17.10934887721462, -36.37867774200744 -17.210220631164397, -36.29580625603245 -17.379736965185366 M-36.47730413327529 -17.008477123264846 C-36.41024045052753 -17.145658078952987, -36.34317676777977 -17.28283903464113, -36.29580625603245 -17.379736965185366 M-36.29580625603245 -17.379736965185366 C-36.251337157749184 -17.454365741305015, -36.20686805946592 -17.52899451742466, -36.084269891312644 -17.734740790612133 M-36.29580625603245 -17.379736965185366 C-36.24544059976959 -17.46426144241712, -36.19507494350672 -17.54878591964887, -36.084269891312644 -17.734740790612133 M-36.084269891312644 -17.734740790612133 C-36.03290965169988 -17.806675281921375, -35.981549412087126 -17.87860977323062, -35.84414004698197 -18.07106356344834 M-36.084269891312644 -17.734740790612133 C-35.99626818726515 -17.857994845942322, -35.908266483217666 -17.981248901272515, -35.84414004698197 -18.07106356344834 M-35.84414004698197 -18.07106356344834 C-35.77813341308667 -18.148997448822715, -35.71212677919137 -18.22693133419709, -35.57705705336566 -18.386407858128706 M-35.84414004698197 -18.07106356344834 C-35.7651179261354 -18.164364805227535, -35.686095805288836 -18.25766604700673, -35.57705705336566 -18.386407858128706 M-35.57705705336566 -18.386407858128706 C-35.504138772479 -18.459326139015364, -35.43122049159234 -18.532244419902018, -35.284845358128706 -18.678619553365657 M-35.57705705336566 -18.386407858128706 C-35.479653486448214 -18.483811425046152, -35.382249919530764 -18.581214991963595, -35.284845358128706 -18.678619553365657 M-35.284845358128706 -18.678619553365657 C-35.17788950710873 -18.769206538312222, -35.070933656088755 -18.859793523258787, -34.96950106344834 -18.945702546981966 M-35.284845358128706 -18.678619553365657 C-35.21878358429656 -18.734571021701488, -35.15272181046441 -18.79052249003732, -34.96950106344834 -18.945702546981966 M-34.96950106344834 -18.945702546981966 C-34.900237190184846 -18.99515600195988, -34.83097331692135 -19.044609456937795, -34.633178290612136 -19.185832391312644 M-34.96950106344834 -18.945702546981966 C-34.87592767712836 -19.01251266067431, -34.78235429080838 -19.079322774366656, -34.633178290612136 -19.185832391312644 M-34.633178290612136 -19.185832391312644 C-34.513641029090785 -19.257061138553293, -34.39410376756943 -19.328289885793943, -34.278174465185366 -19.397368756032446 M-34.633178290612136 -19.185832391312644 C-34.52442484342106 -19.250635379961825, -34.41567139622998 -19.31543836861101, -34.278174465185366 -19.397368756032446 M-34.278174465185366 -19.397368756032446 C-34.13620341140406 -19.466774175045558, -33.99423235762276 -19.536179594058673, -33.906914623264846 -19.578866633275286 M-34.278174465185366 -19.397368756032446 C-34.1892012091021 -19.440865130504193, -34.10022795301883 -19.48436150497594, -33.906914623264846 -19.578866633275286 M-33.906914623264846 -19.578866633275286 C-33.81265859409884 -19.615645449984676, -33.71840256493284 -19.652424266694066, -33.52193484602342 -19.729086208503173 M-33.906914623264846 -19.578866633275286 C-33.77192310369925 -19.631540487662694, -33.63693158413365 -19.6842143420501, -33.52193484602342 -19.729086208503173 M-33.52193484602342 -19.729086208503173 C-33.42034154258052 -19.759331845386455, -33.31874823913762 -19.78957748226974, -33.125864935703994 -19.847001329696653 M-33.52193484602342 -19.729086208503173 C-33.40309945284058 -19.764465037907126, -33.284264059657744 -19.799843867311075, -33.125864935703994 -19.847001329696653 M-33.125864935703994 -19.847001329696653 C-32.98104727282005 -19.8773664004386, -32.836229609936105 -19.907731471180547, -32.72141045140367 -19.931806517013612 M-33.125864935703994 -19.847001329696653 C-32.96584110467085 -19.88055479861027, -32.80581727363771 -19.914108267523883, -32.72141045140367 -19.931806517013612 M-32.72141045140367 -19.931806517013612 C-32.62028902803029 -19.944411289292013, -32.51916760465691 -19.95701606157041, -32.31133422736166 -19.982922465033347 M-32.72141045140367 -19.931806517013612 C-32.57381397567108 -19.95020439852715, -32.42621749993849 -19.968602280040685, -32.31133422736166 -19.982922465033347 M-32.31133422736166 -19.982922465033347 C-32.16945971035009 -19.988790438462498, -32.02758519333852 -19.994658411891653, -31.8984375 -20 M-32.31133422736166 -19.982922465033347 C-32.188068535429345 -19.988020771763978, -32.06480284349703 -19.993119078494605, -31.8984375 -20 M-31.8984375 -20 C-31.8984375 -20, -31.8984375 -20, -31.8984375 -20 M-31.8984375 -20 C-31.8984375 -20, -31.8984375 -20, -31.8984375 -20" stroke="2px" stroke-width="1.3" fill="none" stroke-dasharray="0 0" style=""></path></g><g class="label" style="" transform="translate(-28.8984375, -12)"><rect></rect><foreignObject width="57.796875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Active</p></span></div></foreignObject></g></g><g class="node statediagram-state" id="state-Paused-5" transform="translate(195.1328125, 230)"><g class="basic label-container outer-path"><path d="M-31.8984375 -20 C-13.042628417040266 -20, 5.813180665919468 -20, 31.8984375 -20 M-31.8984375 -20 C-9.469232024946884 -20, 12.959973450106233 -20, 31.8984375 -20 M31.8984375 -20 C31.8984375 -20, 31.8984375 -20, 31.8984375 -20 M31.8984375 -20 C31.8984375 -20, 31.8984375 -20, 31.8984375 -20 M31.8984375 -20 C31.99103046510672 -19.996170326634992, 32.08362343021344 -19.992340653269984, 32.31133422736166 -19.982922465033347 M31.8984375 -20 C31.987894214326257 -19.996300042926787, 32.077350928652514 -19.992600085853574, 32.31133422736166 -19.982922465033347 M32.31133422736166 -19.982922465033347 C32.46672987115987 -19.963552418234272, 32.62212551495807 -19.944182371435193, 32.72141045140367 -19.931806517013612 M32.31133422736166 -19.982922465033347 C32.3980202173536 -19.97211706764944, 32.48470620734553 -19.961311670265527, 32.72141045140367 -19.931806517013612 M32.72141045140367 -19.931806517013612 C32.802848630579476 -19.91473072651594, 32.88428680975529 -19.897654936018267, 33.125864935703994 -19.847001329696653 M32.72141045140367 -19.931806517013612 C32.82072192957464 -19.91098308981492, 32.9200334077456 -19.890159662616224, 33.125864935703994 -19.847001329696653 M33.125864935703994 -19.847001329696653 C33.22069294772594 -19.818769807334636, 33.31552095974788 -19.790538284972623, 33.52193484602342 -19.729086208503173 M33.125864935703994 -19.847001329696653 C33.278430176460425 -19.801580689589965, 33.430995417216856 -19.756160049483277, 33.52193484602342 -19.729086208503173 M33.52193484602342 -19.729086208503173 C33.60444954936283 -19.696888871348165, 33.68696425270225 -19.664691534193157, 33.906914623264846 -19.578866633275286 M33.52193484602342 -19.729086208503173 C33.640728578888684 -19.682732750099138, 33.75952231175395 -19.636379291695103, 33.906914623264846 -19.578866633275286 M33.906914623264846 -19.578866633275286 C33.99518191126682 -19.535715385568373, 34.0834491992688 -19.492564137861464, 34.278174465185366 -19.397368756032446 M33.906914623264846 -19.578866633275286 C34.01787683944572 -19.524620511241704, 34.128839055626585 -19.47037438920812, 34.278174465185366 -19.397368756032446 M34.278174465185366 -19.397368756032446 C34.36882132647688 -19.343354950722556, 34.4594681877684 -19.289341145412664, 34.633178290612136 -19.185832391312644 M34.278174465185366 -19.397368756032446 C34.38015089977142 -19.336603990375377, 34.48212733435747 -19.275839224718307, 34.633178290612136 -19.185832391312644 M34.633178290612136 -19.185832391312644 C34.706465783325925 -19.13350612726475, 34.77975327603971 -19.081179863216853, 34.96950106344834 -18.94570254698197 M34.633178290612136 -19.185832391312644 C34.715200874130026 -19.127269392305312, 34.79722345764792 -19.068706393297976, 34.96950106344834 -18.94570254698197 M34.96950106344834 -18.94570254698197 C35.05584341880288 -18.87257430228882, 35.14218577415742 -18.799446057595674, 35.284845358128706 -18.678619553365657 M34.96950106344834 -18.94570254698197 C35.05890611204767 -18.86998033342956, 35.148311160647005 -18.794258119877146, 35.284845358128706 -18.678619553365657 M35.284845358128706 -18.678619553365657 C35.38533633575571 -18.578128575738653, 35.485827313382714 -18.477637598111652, 35.57705705336566 -18.386407858128706 M35.284845358128706 -18.678619553365657 C35.36985762196522 -18.59360728952915, 35.45486988580172 -18.508595025692642, 35.57705705336566 -18.386407858128706 M35.57705705336566 -18.386407858128706 C35.6366063742518 -18.31609810781749, 35.69615569513794 -18.24578835750627, 35.84414004698197 -18.07106356344834 M35.57705705336566 -18.386407858128706 C35.66238859889485 -18.285657092703534, 35.74772014442405 -18.184906327278362, 35.84414004698197 -18.07106356344834 M35.84414004698197 -18.07106356344834 C35.90438932588133 -17.98667919799266, 35.96463860478069 -17.90229483253698, 36.084269891312644 -17.734740790612136 M35.84414004698197 -18.07106356344834 C35.93469343516357 -17.944235652124625, 36.025246823345164 -17.817407740800913, 36.084269891312644 -17.734740790612136 M36.084269891312644 -17.734740790612136 C36.13771786438231 -17.645043518343268, 36.191165837451976 -17.5553462460744, 36.29580625603245 -17.37973696518537 M36.084269891312644 -17.734740790612136 C36.154517927958615 -17.616849373828682, 36.224765964604586 -17.49895795704523, 36.29580625603245 -17.37973696518537 M36.29580625603245 -17.37973696518537 C36.357248871923304 -17.254054085532175, 36.41869148781416 -17.128371205878985, 36.47730413327529 -17.008477123264846 M36.29580625603245 -17.37973696518537 C36.33325079086169 -17.30314294495398, 36.37069532569093 -17.226548924722593, 36.47730413327529 -17.008477123264846 M36.47730413327529 -17.008477123264846 C36.513767026099885 -16.915030737626388, 36.55022991892448 -16.821584351987926, 36.627523708503176 -16.623497346023417 M36.47730413327529 -17.008477123264846 C36.53526777428584 -16.859929042427236, 36.59323141529639 -16.711380961589622, 36.627523708503176 -16.623497346023417 M36.627523708503176 -16.623497346023417 C36.665968193009945 -16.49436459886805, 36.70441267751671 -16.365231851712682, 36.74543882969665 -16.227427435703994 M36.627523708503176 -16.623497346023417 C36.66011708880059 -16.51401811146263, 36.69271046909801 -16.404538876901842, 36.74543882969665 -16.227427435703994 M36.74543882969665 -16.227427435703994 C36.778673467541374 -16.06892417976335, 36.811908105386095 -15.91042092382271, 36.83024401701361 -15.82297295140367 M36.74543882969665 -16.227427435703994 C36.773262303625984 -16.09473120383939, 36.80108577755532 -15.962034971974791, 36.83024401701361 -15.82297295140367 M36.83024401701361 -15.82297295140367 C36.8474638459408 -15.68482736869071, 36.86468367486799 -15.54668178597775, 36.88135996503335 -15.412896727361662 M36.83024401701361 -15.82297295140367 C36.84433822913978 -15.709902539654376, 36.858432441265954 -15.596832127905081, 36.88135996503335 -15.412896727361662 M36.88135996503335 -15.412896727361662 C36.887003202214956 -15.276455831848304, 36.89264643939656 -15.140014936334945, 36.8984375 -15 M36.88135996503335 -15.412896727361662 C36.88701499990291 -15.276170590052145, 36.89267003477247 -15.139444452742627, 36.8984375 -15 M36.8984375 -15 C36.8984375 -15, 36.8984375 -15, 36.8984375 -15 M36.8984375 -15 C36.8984375 -15, 36.8984375 -15, 36.8984375 -15 M36.8984375 -15 C36.8984375 -3.2886885433969617, 36.8984375 8.422622913206077, 36.8984375 15 M36.8984375 -15 C36.8984375 -3.0891748677459407, 36.8984375 8.821650264508119, 36.8984375 15 M36.8984375 15 C36.8984375 15, 36.8984375 15, 36.8984375 15 M36.8984375 15 C36.8984375 15, 36.8984375 15, 36.8984375 15 M36.8984375 15 C36.8934320328093 15.121021038808664, 36.8884265656186 15.242042077617327, 36.88135996503335 15.412896727361662 M36.8984375 15 C36.89447784497698 15.095735631850644, 36.89051818995397 15.19147126370129, 36.88135996503335 15.412896727361662 M36.88135996503335 15.412896727361662 C36.865530421063525 15.539888788957475, 36.84970087709371 15.666880850553285, 36.83024401701361 15.822972951403669 M36.88135996503335 15.412896727361662 C36.86940050277773 15.508841169621899, 36.85744104052211 15.604785611882136, 36.83024401701361 15.822972951403669 M36.83024401701361 15.822972951403669 C36.81134556730979 15.913103790929627, 36.792447117605974 16.003234630455587, 36.74543882969665 16.227427435703994 M36.83024401701361 15.822972951403669 C36.809847494309736 15.920248428679406, 36.78945097160586 16.017523905955144, 36.74543882969665 16.227427435703994 M36.74543882969665 16.227427435703994 C36.70956537497192 16.347924246052496, 36.673691920247194 16.468421056401, 36.627523708503176 16.623497346023417 M36.74543882969665 16.227427435703994 C36.70029258166935 16.37907100971256, 36.65514633364205 16.530714583721128, 36.627523708503176 16.623497346023417 M36.627523708503176 16.623497346023417 C36.56848193913467 16.774808433043496, 36.50944016976617 16.926119520063573, 36.47730413327529 17.008477123264846 M36.627523708503176 16.623497346023417 C36.59307690881557 16.711776927764337, 36.558630109127954 16.800056509505257, 36.47730413327529 17.008477123264846 M36.47730413327529 17.008477123264846 C36.431564278728615 17.102039491191313, 36.38582442418193 17.195601859117776, 36.29580625603245 17.379736965185366 M36.47730413327529 17.008477123264846 C36.42414918871194 17.117207300254634, 36.370994244148584 17.225937477244422, 36.29580625603245 17.379736965185366 M36.29580625603245 17.379736965185366 C36.214643800183794 17.515945140765336, 36.13348134433514 17.65215331634531, 36.084269891312644 17.734740790612133 M36.29580625603245 17.379736965185366 C36.21223152575521 17.519993459602908, 36.12865679547797 17.660249954020447, 36.084269891312644 17.734740790612133 M36.084269891312644 17.734740790612133 C36.02199956668078 17.821955806737986, 35.95972924204892 17.90917082286384, 35.84414004698197 18.07106356344834 M36.084269891312644 17.734740790612133 C36.03441398272302 17.804568335230208, 35.98455807413339 17.874395879848283, 35.84414004698197 18.07106356344834 M35.84414004698197 18.07106356344834 C35.74873967910428 18.18370256495607, 35.653339311226595 18.296341566463802, 35.57705705336566 18.386407858128706 M35.84414004698197 18.07106356344834 C35.769821745837206 18.1588110158002, 35.69550344469244 18.246558468152056, 35.57705705336566 18.386407858128706 M35.57705705336566 18.386407858128706 C35.47726338963448 18.486201521859883, 35.3774697259033 18.58599518559106, 35.284845358128706 18.678619553365657 M35.57705705336566 18.386407858128706 C35.517628312663 18.445836598831363, 35.45819957196034 18.505265339534017, 35.284845358128706 18.678619553365657 M35.284845358128706 18.678619553365657 C35.180017102277276 18.767404557124028, 35.075188846425846 18.8561895608824, 34.96950106344834 18.94570254698197 M35.284845358128706 18.678619553365657 C35.1777899148536 18.769290888649586, 35.07073447157849 18.85996222393351, 34.96950106344834 18.94570254698197 M34.96950106344834 18.94570254698197 C34.88297769877506 19.00747904196847, 34.79645433410178 19.069255536954966, 34.633178290612136 19.185832391312644 M34.96950106344834 18.94570254698197 C34.84595118090798 19.03391546759778, 34.72240129836762 19.122128388213593, 34.633178290612136 19.185832391312644 M34.633178290612136 19.185832391312644 C34.49807911223509 19.266334028263056, 34.362979933858036 19.346835665213465, 34.278174465185366 19.397368756032446 M34.633178290612136 19.185832391312644 C34.55838366848353 19.230400312367173, 34.48358904635493 19.274968233421703, 34.278174465185366 19.397368756032446 M34.278174465185366 19.397368756032446 C34.13357002235623 19.46806156050493, 33.98896557952709 19.53875436497741, 33.906914623264846 19.578866633275286 M34.278174465185366 19.397368756032446 C34.133926560252135 19.467887259748537, 33.98967865531891 19.53840576346463, 33.906914623264846 19.578866633275286 M33.906914623264846 19.578866633275286 C33.803420945633846 19.61924999160102, 33.69992726800284 19.65963334992675, 33.52193484602342 19.729086208503173 M33.906914623264846 19.578866633275286 C33.787793078190774 19.625348004400127, 33.6686715331167 19.671829375524965, 33.52193484602342 19.729086208503173 M33.52193484602342 19.729086208503173 C33.43867004932515 19.753875212509836, 33.35540525262687 19.7786642165165, 33.125864935703994 19.847001329696653 M33.52193484602342 19.729086208503173 C33.39262479953376 19.767583477308737, 33.263314753044114 19.806080746114297, 33.125864935703994 19.847001329696653 M33.125864935703994 19.847001329696653 C33.01233210803179 19.87080666031135, 32.89879928035958 19.894611990926045, 32.72141045140367 19.931806517013612 M33.125864935703994 19.847001329696653 C32.994360173566626 19.87457497869556, 32.862855411429265 19.90214862769447, 32.72141045140367 19.931806517013612 M32.72141045140367 19.931806517013612 C32.56049637226198 19.951864436060895, 32.3995822931203 19.971922355108177, 32.31133422736166 19.982922465033347 M32.72141045140367 19.931806517013612 C32.59780932774304 19.94721338101061, 32.47420820408242 19.962620245007606, 32.31133422736166 19.982922465033347 M32.31133422736166 19.982922465033347 C32.1933261691475 19.987803314424855, 32.07531811093334 19.992684163816364, 31.8984375 20 M32.31133422736166 19.982922465033347 C32.21173134142177 19.987042070868654, 32.11212845548188 19.99116167670396, 31.8984375 20 M31.8984375 20 C31.8984375 20, 31.8984375 20, 31.8984375 20 M31.8984375 20 C31.8984375 20, 31.8984375 20, 31.8984375 20 M31.8984375 20 C8.031015944522721 20, -15.836405610954557 20, -31.8984375 20 M31.8984375 20 C8.14284723212323 20, -15.612743035753539 20, -31.8984375 20 M-31.8984375 20 C-31.8984375 20, -31.8984375 20, -31.8984375 20 M-31.8984375 20 C-31.8984375 20, -31.8984375 20, -31.8984375 20 M-31.8984375 20 C-31.982928137188388 19.996505441396547, -32.067418774376776 19.993010882793094, -32.31133422736166 19.982922465033347 M-31.8984375 20 C-32.00394732095809 19.995636081525152, -32.10945714191618 19.991272163050308, -32.31133422736166 19.982922465033347 M-32.31133422736166 19.982922465033347 C-32.43744825710544 19.967202367619745, -32.56356228684921 19.951482270206146, -32.72141045140367 19.931806517013612 M-32.31133422736166 19.982922465033347 C-32.428994660915976 19.968256107285853, -32.54665509447028 19.95358974953836, -32.72141045140367 19.931806517013612 M-32.72141045140367 19.931806517013612 C-32.8102014050055 19.913189011844196, -32.89899235860732 19.894571506674783, -33.125864935703994 19.847001329696653 M-32.72141045140367 19.931806517013612 C-32.86031470147326 19.902681358550723, -32.99921895154285 19.873556200087833, -33.125864935703994 19.847001329696653 M-33.125864935703994 19.847001329696653 C-33.23904260491573 19.813306877697674, -33.35222027412747 19.779612425698698, -33.52193484602342 19.729086208503173 M-33.125864935703994 19.847001329696653 C-33.26506109254017 19.80556083832035, -33.40425724937635 19.76412034694405, -33.52193484602342 19.729086208503173 M-33.52193484602342 19.729086208503173 C-33.60122281154003 19.698147948353682, -33.68051077705665 19.66720968820419, -33.906914623264846 19.578866633275286 M-33.52193484602342 19.729086208503173 C-33.652558737834475 19.678116607754077, -33.78318262964554 19.627147007004986, -33.906914623264846 19.578866633275286 M-33.906914623264846 19.578866633275286 C-33.99686049550748 19.53489477573652, -34.0868063677501 19.49092291819776, -34.278174465185366 19.397368756032446 M-33.906914623264846 19.578866633275286 C-33.983380885370245 19.54148455558805, -34.05984714747564 19.504102477900812, -34.278174465185366 19.397368756032446 M-34.278174465185366 19.397368756032446 C-34.39893644512726 19.32541023501492, -34.51969842506916 19.253451713997393, -34.633178290612136 19.185832391312644 M-34.278174465185366 19.397368756032446 C-34.368894660633174 19.34331125305025, -34.45961485608098 19.289253750068053, -34.633178290612136 19.185832391312644 M-34.633178290612136 19.185832391312644 C-34.71959700379702 19.124130616052692, -34.806015716981896 19.062428840792744, -34.96950106344834 18.94570254698197 M-34.633178290612136 19.185832391312644 C-34.766816573727 19.09041649113327, -34.900454856841854 18.995000590953893, -34.96950106344834 18.94570254698197 M-34.96950106344834 18.94570254698197 C-35.083843879622 18.848859121693, -35.19818669579566 18.75201569640403, -35.284845358128706 18.67861955336566 M-34.96950106344834 18.94570254698197 C-35.074460783001825 18.856806199147652, -35.17942050255532 18.76790985131333, -35.284845358128706 18.67861955336566 M-35.284845358128706 18.67861955336566 C-35.397776767408786 18.565688144085577, -35.51070817668887 18.45275673480549, -35.57705705336566 18.386407858128706 M-35.284845358128706 18.67861955336566 C-35.372303729509035 18.591161181985328, -35.459762100889364 18.503702810605, -35.57705705336566 18.386407858128706 M-35.57705705336566 18.386407858128706 C-35.681245827436484 18.263392405036335, -35.78543460150732 18.14037695194396, -35.84414004698197 18.07106356344834 M-35.57705705336566 18.386407858128706 C-35.63945541357962 18.31273425343955, -35.70185377379359 18.239060648750396, -35.84414004698197 18.07106356344834 M-35.84414004698197 18.07106356344834 C-35.91262637549072 17.975142492206093, -35.98111270399946 17.879221420963848, -36.084269891312644 17.734740790612133 M-35.84414004698197 18.07106356344834 C-35.90148552701929 17.9907462213473, -35.95883100705662 17.910428879246265, -36.084269891312644 17.734740790612133 M-36.084269891312644 17.734740790612133 C-36.132273476323256 17.65418038041723, -36.18027706133386 17.57361997022233, -36.29580625603244 17.37973696518537 M-36.084269891312644 17.734740790612133 C-36.12819887459771 17.66101844441429, -36.17212785788277 17.58729609821645, -36.29580625603244 17.37973696518537 M-36.29580625603244 17.37973696518537 C-36.34152176960855 17.286224387510035, -36.387237283184646 17.1927118098347, -36.47730413327528 17.00847712326485 M-36.29580625603244 17.37973696518537 C-36.339990731238856 17.289356176552094, -36.38417520644526 17.198975387918818, -36.47730413327528 17.00847712326485 M-36.47730413327528 17.00847712326485 C-36.533545739137075 16.864342240287545, -36.58978734499886 16.720207357310244, -36.627523708503176 16.623497346023417 M-36.47730413327528 17.00847712326485 C-36.510530018432675 16.923326477304524, -36.54375590359006 16.838175831344195, -36.627523708503176 16.623497346023417 M-36.627523708503176 16.623497346023417 C-36.66986067683294 16.48128997618107, -36.7121976451627 16.339082606338724, -36.74543882969665 16.227427435703994 M-36.627523708503176 16.623497346023417 C-36.672140720095825 16.473631445862683, -36.71675773168848 16.323765545701946, -36.74543882969665 16.227427435703994 M-36.74543882969665 16.227427435703994 C-36.763637452616 16.140634223157775, -36.78183607553536 16.053841010611556, -36.83024401701361 15.82297295140367 M-36.74543882969665 16.227427435703994 C-36.76943682095071 16.11297576730987, -36.793434812204765 15.998524098915743, -36.83024401701361 15.82297295140367 M-36.83024401701361 15.82297295140367 C-36.848425396503316 15.677113356935543, -36.86660677599302 15.531253762467415, -36.88135996503335 15.412896727361664 M-36.83024401701361 15.82297295140367 C-36.84396326800296 15.712910654599082, -36.857682518992306 15.602848357794493, -36.88135996503335 15.412896727361664 M-36.88135996503335 15.412896727361664 C-36.88699352698616 15.276689757313209, -36.892627088938966 15.140482787264753, -36.8984375 15 M-36.88135996503335 15.412896727361664 C-36.88584213003154 15.304527969056489, -36.890324295029735 15.196159210751311, -36.8984375 15 M-36.8984375 15 C-36.8984375 15, -36.8984375 15, -36.8984375 15 M-36.8984375 15 C-36.8984375 15, -36.8984375 15, -36.8984375 15 M-36.8984375 15 C-36.8984375 6.025632536286132, -36.8984375 -2.9487349274277364, -36.8984375 -15 M-36.8984375 15 C-36.8984375 3.831963109642974, -36.8984375 -7.336073780714052, -36.8984375 -15 M-36.8984375 -15 C-36.8984375 -15, -36.8984375 -15, -36.8984375 -15 M-36.8984375 -15 C-36.8984375 -15, -36.8984375 -15, -36.8984375 -15 M-36.8984375 -15 C-36.894054470301946 -15.105971887733734, -36.88967144060389 -15.211943775467468, -36.88135996503335 -15.41289672736166 M-36.8984375 -15 C-36.89283159295039 -15.135538336135715, -36.88722568590077 -15.27107667227143, -36.88135996503335 -15.41289672736166 M-36.88135996503335 -15.41289672736166 C-36.86991302940231 -15.504729439504928, -36.85846609377128 -15.596562151648195, -36.83024401701361 -15.822972951403669 M-36.88135996503335 -15.41289672736166 C-36.864985658656835 -15.544259129710024, -36.84861135228032 -15.67562153205839, -36.83024401701361 -15.822972951403669 M-36.83024401701361 -15.822972951403669 C-36.80390252355884 -15.948601294291839, -36.77756103010407 -16.07422963718001, -36.74543882969665 -16.227427435703994 M-36.83024401701361 -15.822972951403669 C-36.81121941641568 -15.913705432131497, -36.79219481581775 -16.004437912859323, -36.74543882969665 -16.227427435703994 M-36.74543882969665 -16.227427435703994 C-36.713999732085576 -16.333029503066598, -36.6825606344745 -16.438631570429198, -36.627523708503176 -16.623497346023417 M-36.74543882969665 -16.227427435703994 C-36.70361534903182 -16.36791003088349, -36.661791868367 -16.50839262606299, -36.627523708503176 -16.623497346023417 M-36.627523708503176 -16.623497346023417 C-36.57361639269745 -16.761649956288018, -36.51970907689172 -16.89980256655262, -36.47730413327529 -17.008477123264846 M-36.627523708503176 -16.623497346023417 C-36.58342458169017 -16.736513722159874, -36.53932545487716 -16.849530098296327, -36.47730413327529 -17.008477123264846 M-36.47730413327529 -17.008477123264846 C-36.42094384349809 -17.123763938687393, -36.364583553720884 -17.239050754109936, -36.29580625603245 -17.379736965185366 M-36.47730413327529 -17.008477123264846 C-36.440096523734844 -17.0845865050718, -36.40288891419439 -17.160695886878756, -36.29580625603245 -17.379736965185366 M-36.29580625603245 -17.379736965185366 C-36.22164830402293 -17.50419006658978, -36.147490352013406 -17.62864316799419, -36.084269891312644 -17.734740790612133 M-36.29580625603245 -17.379736965185366 C-36.22088443461408 -17.505472004863734, -36.14596261319571 -17.631207044542105, -36.084269891312644 -17.734740790612133 M-36.084269891312644 -17.734740790612133 C-36.02127121386007 -17.822975928334905, -35.958272536407485 -17.911211066057678, -35.84414004698197 -18.07106356344834 M-36.084269891312644 -17.734740790612133 C-36.03389980429705 -17.80528848692329, -35.983529717281456 -17.875836183234444, -35.84414004698197 -18.07106356344834 M-35.84414004698197 -18.07106356344834 C-35.76865936564496 -18.160183435499828, -35.69317868430794 -18.249303307551315, -35.57705705336566 -18.386407858128706 M-35.84414004698197 -18.07106356344834 C-35.76832547148888 -18.16057766358497, -35.69251089599578 -18.250091763721596, -35.57705705336566 -18.386407858128706 M-35.57705705336566 -18.386407858128706 C-35.505936799124605 -18.45752811236976, -35.434816544883546 -18.528648366610813, -35.284845358128706 -18.678619553365657 M-35.57705705336566 -18.386407858128706 C-35.47636274013832 -18.487102171356042, -35.375668426910984 -18.587796484583375, -35.284845358128706 -18.678619553365657 M-35.284845358128706 -18.678619553365657 C-35.18475283460569 -18.763393596442082, -35.08466031108267 -18.848167639518504, -34.96950106344834 -18.945702546981966 M-35.284845358128706 -18.678619553365657 C-35.17192238152915 -18.774260435877398, -35.0589994049296 -18.869901318389143, -34.96950106344834 -18.945702546981966 M-34.96950106344834 -18.945702546981966 C-34.86407086536602 -19.02097826155747, -34.7586406672837 -19.096253976132974, -34.633178290612136 -19.185832391312644 M-34.96950106344834 -18.945702546981966 C-34.88349235451088 -19.00711158483589, -34.79748364557342 -19.068520622689814, -34.633178290612136 -19.185832391312644 M-34.633178290612136 -19.185832391312644 C-34.50318855541885 -19.26328946096709, -34.373198820225575 -19.340746530621537, -34.278174465185366 -19.397368756032446 M-34.633178290612136 -19.185832391312644 C-34.54560884308992 -19.2380124560404, -34.45803939556771 -19.29019252076816, -34.278174465185366 -19.397368756032446 M-34.278174465185366 -19.397368756032446 C-34.15650773147549 -19.45684799780872, -34.03484099776562 -19.516327239584996, -33.906914623264846 -19.578866633275286 M-34.278174465185366 -19.397368756032446 C-34.18011230450997 -19.445308425209596, -34.08205014383457 -19.493248094386747, -33.906914623264846 -19.578866633275286 M-33.906914623264846 -19.578866633275286 C-33.766561214923236 -19.633632703155474, -33.626207806581625 -19.68839877303566, -33.52193484602342 -19.729086208503173 M-33.906914623264846 -19.578866633275286 C-33.82699872777546 -19.610049912460475, -33.74708283228608 -19.641233191645664, -33.52193484602342 -19.729086208503173 M-33.52193484602342 -19.729086208503173 C-33.427195789571 -19.757291247644705, -33.33245673311858 -19.78549628678624, -33.125864935703994 -19.847001329696653 M-33.52193484602342 -19.729086208503173 C-33.41576176926524 -19.760695302976742, -33.309588692507056 -19.792304397450316, -33.125864935703994 -19.847001329696653 M-33.125864935703994 -19.847001329696653 C-32.98868503753706 -19.875764929586747, -32.851505139370126 -19.90452852947684, -32.72141045140367 -19.931806517013612 M-33.125864935703994 -19.847001329696653 C-32.98873617381941 -19.875754207435868, -32.851607411934836 -19.904507085175084, -32.72141045140367 -19.931806517013612 M-32.72141045140367 -19.931806517013612 C-32.56286213678377 -19.95156954382079, -32.40431382216388 -19.97133257062796, -32.31133422736166 -19.982922465033347 M-32.72141045140367 -19.931806517013612 C-32.62162861096226 -19.944244310453676, -32.52184677052085 -19.956682103893744, -32.31133422736166 -19.982922465033347 M-32.31133422736166 -19.982922465033347 C-32.21768690221563 -19.986795747052156, -32.12403957706961 -19.990669029070965, -31.8984375 -20 M-32.31133422736166 -19.982922465033347 C-32.2274910379973 -19.986390244996716, -32.143647848632924 -19.989858024960085, -31.8984375 -20 M-31.8984375 -20 C-31.8984375 -20, -31.8984375 -20, -31.8984375 -20 M-31.8984375 -20 C-31.8984375 -20, -31.8984375 -20, -31.8984375 -20" stroke="2px" stroke-width="1.3" fill="none" stroke-dasharray="0 0" style=""></path></g><g class="label" style="" transform="translate(-28.8984375, -12)"><rect></rect><foreignObject width="57.796875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Paused</p></span></div></foreignObject></g></g><g class="node default" id="state-root_end-5" transform="translate(113.05859375, 331)"><g><path d="M7 0 C7 0.40517908122283747, 6.964012880168563 0.816513743121899, 6.893654271085456 1.2155372436685123 C6.823295662002349 1.6145607442151257, 6.716427752933756 2.013397210557766, 6.5778483455013586 2.394141003279681 C6.439268938068961 2.7748847960015954, 6.26476736710249 3.149104622578984, 6.062177826491071 3.4999999999999996 C5.859588285879653 3.8508953774210153, 5.622755194947063 4.189128084166967, 5.362311101832846 4.499513267805774 C5.10186700871863 4.809898451444582, 4.809898451444583 5.10186700871863, 4.499513267805775 5.362311101832846 C4.189128084166968 5.622755194947063, 3.8508953774210166 5.859588285879652, 3.500000000000001 6.06217782649107 C3.149104622578985 6.264767367102489, 2.7748847960015963 6.439268938068961, 2.3941410032796817 6.5778483455013586 C2.013397210557767 6.716427752933756, 1.6145607442151264 6.823295662002349, 1.2155372436685128 6.893654271085456 C0.8165137431218992 6.964012880168563, 0.4051790812228379 7, 4.286263797015736e-16 7 C-0.405179081222837 7, -0.8165137431218985 6.964012880168563, -1.2155372436685121 6.893654271085456 C-1.6145607442151257 6.823295662002349, -2.0133972105577667 6.716427752933756, -2.394141003279681 6.5778483455013586 C-2.774884796001595 6.439268938068961, -3.149104622578983 6.26476736710249, -3.4999999999999982 6.062177826491071 C-3.8508953774210135 5.859588285879653, -4.189128084166966 5.6227551949470636, -4.499513267805773 5.362311101832848 C-4.809898451444581 5.101867008718632, -5.101867008718628 4.809898451444586, -5.3623111018328435 4.499513267805779 C-5.622755194947059 4.189128084166971, -5.859588285879649 3.8508953774210206, -6.062177826491068 3.5000000000000053 C-6.264767367102486 3.14910462257899, -6.439268938068958 2.774884796001602, -6.577848345501356 2.394141003279688 C-6.716427752933754 2.0133972105577738, -6.823295662002347 1.614560744215134, -6.893654271085454 1.215537243668521 C-6.9640128801685615 0.816513743121908, -6.999999999999999 0.4051790812228472, -7 1.0183126166254463e-14 C-7.000000000000001 -0.40517908122282686, -6.964012880168565 -0.8165137431218878, -6.893654271085459 -1.215537243668501 C-6.823295662002352 -1.6145607442151142, -6.716427752933759 -2.0133972105577542, -6.577848345501363 -2.394141003279669 C-6.439268938068967 -2.7748847960015834, -6.264767367102496 -3.149104622578972, -6.062177826491078 -3.4999999999999876 C-5.859588285879661 -3.8508953774210033, -5.6227551949470715 -4.1891280841669545, -5.362311101832856 -4.499513267805763 C-5.10186700871864 -4.809898451444571, -4.809898451444594 -5.10186700871862, -4.499513267805787 -5.362311101832836 C-4.189128084166979 -5.622755194947053, -3.850895377421028 -5.859588285879643, -3.5000000000000133 -6.062177826491062 C-3.1491046225789985 -6.264767367102482, -2.774884796001611 -6.439268938068954, -2.3941410032796973 -6.577848345501353 C-2.0133972105577835 -6.716427752933752, -1.6145607442151435 -6.823295662002345, -1.2155372436685306 -6.893654271085453 C-0.8165137431219176 -6.9640128801685615, -0.40517908122285695 -6.999999999999999, -1.9937625952807352e-14 -7 C0.4051790812228171 -7.000000000000001, 0.8165137431218781 -6.964012880168565, 1.2155372436684913 -6.89365427108546 C1.6145607442151044 -6.823295662002354, 2.013397210557745 -6.716427752933763, 2.3941410032796595 -6.5778483455013665 C2.774884796001574 -6.43926893806897, 3.149104622578963 -6.2647673671025, 3.499999999999979 -6.062177826491083 C3.8508953774209953 -5.859588285879665, 4.189128084166947 -5.622755194947077, 4.499513267805756 -5.362311101832862 C4.809898451444564 -5.1018670087186475, 5.101867008718613 -4.809898451444602, 5.362311101832829 -4.499513267805796 C5.622755194947046 -4.189128084166989, 5.859588285879637 -3.8508953774210393, 6.062177826491056 -3.500000000000025 C6.2647673671024755 -3.1491046225790105, 6.439268938068949 -2.774884796001623, 6.577848345501348 -2.3941410032797092 C6.716427752933747 -2.0133972105577955, 6.823295662002342 -1.6145607442151562, 6.893654271085451 -1.2155372436685434 C6.96401288016856 -0.8165137431219307, 6.982275711847575 -0.2025895406114567, 7 -3.2800750208310675e-14 C7.017724288152425 0.2025895406113911, 7.017724288152424 -0.2025895406114242, 7 0" stroke="none" stroke-width="0" fill="transparent" style=""></path><path d="M7 0 C7 0.40517908122283747, 6.964012880168563 0.816513743121899, 6.893654271085456 1.2155372436685123 C6.823295662002349 1.6145607442151257, 6.716427752933756 2.013397210557766, 6.5778483455013586 2.394141003279681 C6.439268938068961 2.7748847960015954, 6.26476736710249 3.149104622578984, 6.062177826491071 3.4999999999999996 C5.859588285879653 3.8508953774210153, 5.622755194947063 4.189128084166967, 5.362311101832846 4.499513267805774 C5.10186700871863 4.809898451444582, 4.809898451444583 5.10186700871863, 4.499513267805775 5.362311101832846 C4.189128084166968 5.622755194947063, 3.8508953774210166 5.859588285879652, 3.500000000000001 6.06217782649107 C3.149104622578985 6.264767367102489, 2.7748847960015963 6.439268938068961, 2.3941410032796817 6.5778483455013586 C2.013397210557767 6.716427752933756, 1.6145607442151264 6.823295662002349, 1.2155372436685128 6.893654271085456 C0.8165137431218992 6.964012880168563, 0.4051790812228379 7, 4.286263797015736e-16 7 C-0.405179081222837 7, -0.8165137431218985 6.964012880168563, -1.2155372436685121 6.893654271085456 C-1.6145607442151257 6.823295662002349, -2.0133972105577667 6.716427752933756, -2.394141003279681 6.5778483455013586 C-2.774884796001595 6.439268938068961, -3.149104622578983 6.26476736710249, -3.4999999999999982 6.062177826491071 C-3.8508953774210135 5.859588285879653, -4.189128084166966 5.6227551949470636, -4.499513267805773 5.362311101832848 C-4.809898451444581 5.101867008718632, -5.101867008718628 4.809898451444586, -5.3623111018328435 4.499513267805779 C-5.622755194947059 4.189128084166971, -5.859588285879649 3.8508953774210206, -6.062177826491068 3.5000000000000053 C-6.264767367102486 3.14910462257899, -6.439268938068958 2.774884796001602, -6.577848345501356 2.394141003279688 C-6.716427752933754 2.0133972105577738, -6.823295662002347 1.614560744215134, -6.893654271085454 1.215537243668521 C-6.9640128801685615 0.816513743121908, -6.999999999999999 0.4051790812228472, -7 1.0183126166254463e-14 C-7.000000000000001 -0.40517908122282686, -6.964012880168565 -0.8165137431218878, -6.893654271085459 -1.215537243668501 C-6.823295662002352 -1.6145607442151142, -6.716427752933759 -2.0133972105577542, -6.577848345501363 -2.394141003279669 C-6.439268938068967 -2.7748847960015834, -6.264767367102496 -3.149104622578972, -6.062177826491078 -3.4999999999999876 C-5.859588285879661 -3.8508953774210033, -5.6227551949470715 -4.1891280841669545, -5.362311101832856 -4.499513267805763 C-5.10186700871864 -4.809898451444571, -4.809898451444594 -5.10186700871862, -4.499513267805787 -5.362311101832836 C-4.189128084166979 -5.622755194947053, -3.850895377421028 -5.859588285879643, -3.5000000000000133 -6.062177826491062 C-3.1491046225789985 -6.264767367102482, -2.774884796001611 -6.439268938068954, -2.3941410032796973 -6.577848345501353 C-2.0133972105577835 -6.716427752933752, -1.6145607442151435 -6.823295662002345, -1.2155372436685306 -6.893654271085453 C-0.8165137431219176 -6.9640128801685615, -0.40517908122285695 -6.999999999999999, -1.9937625952807352e-14 -7 C0.4051790812228171 -7.000000000000001, 0.8165137431218781 -6.964012880168565, 1.2155372436684913 -6.89365427108546 C1.6145607442151044 -6.823295662002354, 2.013397210557745 -6.716427752933763, 2.3941410032796595 -6.5778483455013665 C2.774884796001574 -6.43926893806897, 3.149104622578963 -6.2647673671025, 3.499999999999979 -6.062177826491083 C3.8508953774209953 -5.859588285879665, 4.189128084166947 -5.622755194947077, 4.499513267805756 -5.362311101832862 C4.809898451444564 -5.1018670087186475, 5.101867008718613 -4.809898451444602, 5.362311101832829 -4.499513267805796 C5.622755194947046 -4.189128084166989, 5.859588285879637 -3.8508953774210393, 6.062177826491056 -3.500000000000025 C6.2647673671024755 -3.1491046225790105, 6.439268938068949 -2.774884796001623, 6.577848345501348 -2.3941410032797092 C6.716427752933747 -2.0133972105577955, 6.823295662002342 -1.6145607442151562, 6.893654271085451 -1.2155372436685434 C6.96401288016856 -0.8165137431219307, 6.982275711847575 -0.2025895406114567, 7 -3.2800750208310675e-14 C7.017724288152425 0.2025895406113911, 7.017724288152424 -0.2025895406114242, 7 0" stroke="rgb(171, 75, 153)" stroke-width="2" fill="none" stroke-dasharray="0 0" style=""></path><g><path d="M2.5 0 C2.5 0.14470681472244193, 2.487147457203058 0.29161205111496386, 2.46201938253052 0.4341204441673258 C2.436891307857982 0.5766288372196877, 2.3987241974763416 0.7190704323420595, 2.3492315519647713 0.8550503583141718 C2.299738906453201 0.991030284286284, 2.2374169168223177 1.124680222349637, 2.165063509461097 1.2499999999999998 C2.092710102099876 1.3753197776503625, 2.0081268553382365 1.496117172916774, 1.915111107797445 1.6069690242163481 C1.8220953602566536 1.7178208755159223, 1.7178208755159226 1.8220953602566536, 1.6069690242163484 1.915111107797445 C1.4961171729167742 2.0081268553382365, 1.375319777650363 2.0927101020998755, 1.2500000000000002 2.1650635094610964 C1.1246802223496375 2.2374169168223172, 0.9910302842862845 2.2997389064532, 0.8550503583141721 2.349231551964771 C0.7190704323420597 2.3987241974763416, 0.576628837219688 2.436891307857982, 0.43412044416732604 2.46201938253052 C0.291612051114964 2.487147457203058, 0.14470681472244212 2.5, 1.5308084989341916e-16 2.5 C-0.1447068147224418 2.5, -0.2916120511149638 2.487147457203058, -0.43412044416732576 2.46201938253052 C-0.5766288372196877 2.436891307857982, -0.7190704323420595 2.3987241974763416, -0.8550503583141718 2.3492315519647713 C-0.991030284286284 2.299738906453201, -1.124680222349637 2.2374169168223177, -1.2499999999999996 2.165063509461097 C-1.375319777650362 2.092710102099876, -1.4961171729167733 2.008126855338237, -1.6069690242163475 1.9151111077974459 C-1.7178208755159217 1.8220953602566548, -1.822095360256653 1.7178208755159234, -1.9151111077974443 1.6069690242163495 C-2.0081268553382357 1.4961171729167755, -2.0927101020998746 1.3753197776503645, -2.1650635094610955 1.250000000000002 C-2.2374169168223164 1.1246802223496395, -2.2997389064531992 0.9910302842862865, -2.34923155196477 0.8550503583141743 C-2.3987241974763407 0.7190704323420621, -2.436891307857981 0.5766288372196907, -2.4620193825305194 0.434120444167329 C-2.487147457203058 0.29161205111496724, -2.5 0.14470681472244545, -2.5 3.636830773662308e-15 C-2.5 -0.14470681472243818, -2.4871474572030587 -0.2916120511149599, -2.4620193825305208 -0.4341204441673218 C-2.436891307857983 -0.5766288372196837, -2.398724197476343 -0.7190704323420553, -2.3492315519647726 -0.8550503583141675 C-2.2997389064532023 -0.9910302842862798, -2.23741691682232 -1.1246802223496328, -2.165063509461099 -1.2499999999999956 C-2.092710102099878 -1.3753197776503583, -2.00812685533824 -1.4961171729167695, -1.9151111077974488 -1.606969024216344 C-1.8220953602566576 -1.7178208755159183, -1.7178208755159263 -1.82209536025665, -1.6069690242163523 -1.9151111077974416 C-1.4961171729167784 -2.0081268553382334, -1.3753197776503672 -2.0927101020998724, -1.2500000000000047 -2.1650635094610937 C-1.1246802223496422 -2.237416916822315, -0.9910302842862897 -2.299738906453198, -0.8550503583141776 -2.3492315519647686 C-0.7190704323420656 -2.3987241974763394, -0.5766288372196942 -2.4368913078579806, -0.43412044416733236 -2.462019382530519 C-0.29161205111497057 -2.4871474572030574, -0.1447068147224489 -2.4999999999999996, -7.120580697431198e-15 -2.5 C0.14470681472243463 -2.5000000000000004, 0.29161205111495647 -2.487147457203059, 0.4341204441673183 -2.4620193825305217 C0.5766288372196802 -2.436891307857984, 0.7190704323420518 -2.3987241974763442, 0.8550503583141642 -2.349231551964774 C0.9910302842862766 -2.2997389064532037, 1.1246802223496295 -2.2374169168223212, 1.2499999999999925 -2.165063509461101 C1.3753197776503554 -2.0927101020998804, 1.4961171729167668 -2.008126855338242, 1.6069690242163412 -1.915111107797451 C1.7178208755159157 -1.82209536025666, 1.8220953602566472 -1.7178208755159294, 1.915111107797439 -1.6069690242163557 C2.0081268553382308 -1.496117172916782, 2.09271010209987 -1.3753197776503712, 2.1650635094610915 -1.2500000000000089 C2.237416916822313 -1.1246802223496466, 2.299738906453196 -0.9910302842862939, 2.3492315519647673 -0.855050358314182 C2.3987241974763385 -0.71907043234207, 2.4368913078579792 -0.5766288372196986, 2.462019382530518 -0.4341204441673369 C2.487147457203057 -0.29161205111497523, 2.4936698970884197 -0.07235340736123454, 2.5 -1.1714553645825241e-14 C2.5063301029115803 0.07235340736121111, 2.50633010291158 -0.07235340736122292, 2.5 0" stroke="none" stroke-width="0" fill="2px" style=""></path><path d="M2.5 0 C2.5 0.14470681472244193, 2.487147457203058 0.29161205111496386, 2.46201938253052 0.4341204441673258 C2.436891307857982 0.5766288372196877, 2.3987241974763416 0.7190704323420595, 2.3492315519647713 0.8550503583141718 C2.299738906453201 0.991030284286284, 2.2374169168223177 1.124680222349637, 2.165063509461097 1.2499999999999998 C2.092710102099876 1.3753197776503625, 2.0081268553382365 1.496117172916774, 1.915111107797445 1.6069690242163481 C1.8220953602566536 1.7178208755159223, 1.7178208755159226 1.8220953602566536, 1.6069690242163484 1.915111107797445 C1.4961171729167742 2.0081268553382365, 1.375319777650363 2.0927101020998755, 1.2500000000000002 2.1650635094610964 C1.1246802223496375 2.2374169168223172, 0.9910302842862845 2.2997389064532, 0.8550503583141721 2.349231551964771 C0.7190704323420597 2.3987241974763416, 0.576628837219688 2.436891307857982, 0.43412044416732604 2.46201938253052 C0.291612051114964 2.487147457203058, 0.14470681472244212 2.5, 1.5308084989341916e-16 2.5 C-0.1447068147224418 2.5, -0.2916120511149638 2.487147457203058, -0.43412044416732576 2.46201938253052 C-0.5766288372196877 2.436891307857982, -0.7190704323420595 2.3987241974763416, -0.8550503583141718 2.3492315519647713 C-0.991030284286284 2.299738906453201, -1.124680222349637 2.2374169168223177, -1.2499999999999996 2.165063509461097 C-1.375319777650362 2.092710102099876, -1.4961171729167733 2.008126855338237, -1.6069690242163475 1.9151111077974459 C-1.7178208755159217 1.8220953602566548, -1.822095360256653 1.7178208755159234, -1.9151111077974443 1.6069690242163495 C-2.0081268553382357 1.4961171729167755, -2.0927101020998746 1.3753197776503645, -2.1650635094610955 1.250000000000002 C-2.2374169168223164 1.1246802223496395, -2.2997389064531992 0.9910302842862865, -2.34923155196477 0.8550503583141743 C-2.3987241974763407 0.7190704323420621, -2.436891307857981 0.5766288372196907, -2.4620193825305194 0.434120444167329 C-2.487147457203058 0.29161205111496724, -2.5 0.14470681472244545, -2.5 3.636830773662308e-15 C-2.5 -0.14470681472243818, -2.4871474572030587 -0.2916120511149599, -2.4620193825305208 -0.4341204441673218 C-2.436891307857983 -0.5766288372196837, -2.398724197476343 -0.7190704323420553, -2.3492315519647726 -0.8550503583141675 C-2.2997389064532023 -0.9910302842862798, -2.23741691682232 -1.1246802223496328, -2.165063509461099 -1.2499999999999956 C-2.092710102099878 -1.3753197776503583, -2.00812685533824 -1.4961171729167695, -1.9151111077974488 -1.606969024216344 C-1.8220953602566576 -1.7178208755159183, -1.7178208755159263 -1.82209536025665, -1.6069690242163523 -1.9151111077974416 C-1.4961171729167784 -2.0081268553382334, -1.3753197776503672 -2.0927101020998724, -1.2500000000000047 -2.1650635094610937 C-1.1246802223496422 -2.237416916822315, -0.9910302842862897 -2.299738906453198, -0.8550503583141776 -2.3492315519647686 C-0.7190704323420656 -2.3987241974763394, -0.5766288372196942 -2.4368913078579806, -0.43412044416733236 -2.462019382530519 C-0.29161205111497057 -2.4871474572030574, -0.1447068147224489 -2.4999999999999996, -7.120580697431198e-15 -2.5 C0.14470681472243463 -2.5000000000000004, 0.29161205111495647 -2.487147457203059, 0.4341204441673183 -2.4620193825305217 C0.5766288372196802 -2.436891307857984, 0.7190704323420518 -2.3987241974763442, 0.8550503583141642 -2.349231551964774 C0.9910302842862766 -2.2997389064532037, 1.1246802223496295 -2.2374169168223212, 1.2499999999999925 -2.165063509461101 C1.3753197776503554 -2.0927101020998804, 1.4961171729167668 -2.008126855338242, 1.6069690242163412 -1.915111107797451 C1.7178208755159157 -1.82209536025666, 1.8220953602566472 -1.7178208755159294, 1.915111107797439 -1.6069690242163557 C2.0081268553382308 -1.496117172916782, 2.09271010209987 -1.3753197776503712, 2.1650635094610915 -1.2500000000000089 C2.237416916822313 -1.1246802223496466, 2.299738906453196 -0.9910302842862939, 2.3492315519647673 -0.855050358314182 C2.3987241974763385 -0.71907043234207, 2.4368913078579792 -0.5766288372196986, 2.462019382530518 -0.4341204441673369 C2.487147457203057 -0.29161205111497523, 2.4936698970884197 -0.07235340736123454, 2.5 -1.1714553645825241e-14 C2.5063301029115803 0.07235340736121111, 2.50633010291158 -0.07235340736122292, 2.5 0" stroke="2px" stroke-width="2" fill="none" stroke-dasharray="0 0" style=""></path></g></g></g></g></g></g></svg></p>
<p>For composables that can be paused and resumed:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> interface</span><span style="color:#C0CAF5"> Pausable</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /** Whether the composable is currently active */</span></span>
<span class="line"><span style="color:#73DACA">  isActive</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Readonly</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Ref</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">boolean</span><span style="color:#89DDFF">&gt;&gt;</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /** Pause the composable */</span></span>
<span class="line"><span style="color:#7AA2F7">  pause</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /** Resume the composable */</span></span>
<span class="line"><span style="color:#7AA2F7">  resume</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> interface</span><span style="color:#C0CAF5"> UseIntervalOptions</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /** Start immediately */</span></span>
<span class="line"><span style="color:#73DACA">  immediate</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> boolean</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /** Call callback immediately when starting */</span></span>
<span class="line"><span style="color:#73DACA">  immediateCallback</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> boolean</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useIntervalFn</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#7AA2F7">  callback</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#E0AF68">  interval</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> MaybeRefOrGetter</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">number</span><span style="color:#89DDFF">&gt;</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> 1000</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#E0AF68">  options</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> UseIntervalOptions</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {}</span></span>
<span class="line"><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Pausable</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> immediate</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> true</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> immediateCallback</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> false</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> options</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> isActive</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> shallowRef</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">false</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  let</span><span style="color:#BB9AF7"> timer</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> ReturnType</span><span style="color:#89DDFF">&lt;typeof</span><span style="color:#C0CAF5"> setInterval</span><span style="color:#89DDFF">&gt;</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> null</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  function</span><span style="color:#7AA2F7"> clean</span><span style="color:#9ABDF5">() {</span></span>
<span class="line"><span style="color:#BB9AF7">    if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">timer</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#7AA2F7">      clearInterval</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">timer</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#C0CAF5">      timer</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> null</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  function</span><span style="color:#7AA2F7"> pause</span><span style="color:#9ABDF5">() {</span></span>
<span class="line"><span style="color:#C0CAF5">    isActive</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> false</span></span>
<span class="line"><span style="color:#7AA2F7">    clean</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  function</span><span style="color:#7AA2F7"> resume</span><span style="color:#9ABDF5">() {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> ms</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> toValue</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">interval</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#BB9AF7">    if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">ms</span><span style="color:#BB9AF7"> &lt;=</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7;font-style:italic">return</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">    isActive</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> true</span></span>
<span class="line"><span style="color:#BB9AF7">    if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">immediateCallback</span><span style="color:#9ABDF5">) </span><span style="color:#7AA2F7">callback</span><span style="color:#9ABDF5">()</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">    clean</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#C0CAF5">    timer</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> setInterval</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">callback</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> ms</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">immediate</span><span style="color:#9ABDF5">) </span><span style="color:#7AA2F7">resume</span><span style="color:#9ABDF5">()</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  tryOnCleanup</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">pause</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">    isActive</span><span style="color:#89DDFF">:</span><span style="color:#7AA2F7"> readonly</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">isActive</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    pause</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    resume</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Usage</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> isActive</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> pause</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> resume</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> useIntervalFn</span><span style="color:#9ABDF5">(()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">  console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">log</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">tick</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 1000</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">pause</span><span style="color:#9ABDF5">()</span><span style="color:#51597D;font-style:italic">   // Stop ticking</span></span>
<span class="line"><span style="color:#7AA2F7">resume</span><span style="color:#9ABDF5">()</span><span style="color:#51597D;font-style:italic">  // Start again</span></span></code><button type="button" class="copy" data-code="export interface Pausable {
  /** Whether the composable is currently active */
  isActive: Readonly<Ref<boolean>>
  /** Pause the composable */
  pause: () => void
  /** Resume the composable */
  resume: () => void
}

export interface UseIntervalOptions {
  /** Start immediately */
  immediate?: boolean
  /** Call callback immediately when starting */
  immediateCallback?: boolean
}

export function useIntervalFn(
  callback: () => void,
  interval: MaybeRefOrGetter<number> = 1000,
  options: UseIntervalOptions = {}
): Pausable {
  const { immediate = true, immediateCallback = false } = options

  const isActive = shallowRef(false)
  let timer: ReturnType<typeof setInterval> | null = null

  function clean() {
    if (timer) {
      clearInterval(timer)
      timer = null
    }
  }

  function pause() {
    isActive.value = false
    clean()
  }

  function resume() {
    const ms = toValue(interval)
    if (ms <= 0) return

    isActive.value = true
    if (immediateCallback) callback()

    clean()
    timer = setInterval(callback, ms)
  }

  if (immediate) resume()

  tryOnCleanup(pause)

  return {
    isActive: readonly(isActive),
    pause,
    resume,
  }
}

// Usage
const { isActive, pause, resume } = useIntervalFn(() => {
  console.log('tick')
}, 1000)

pause()   // Stop ticking
resume()  // Start again" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="stoppable-pattern">Stoppable Pattern<a class="heading-link" aria-label="Link to section" href="#stoppable-pattern"><span class="heading-link-icon">#</span></a></h3>
<p>For one-way stopping (e.g., timeouts, one-time operations):</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> interface</span><span style="color:#C0CAF5"> Stoppable</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /** Whether the operation is pending */</span></span>
<span class="line"><span style="color:#73DACA">  isPending</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Readonly</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Ref</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">boolean</span><span style="color:#89DDFF">&gt;&gt;</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /** Stop the operation */</span></span>
<span class="line"><span style="color:#7AA2F7">  stop</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useTimeoutFn</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#7AA2F7">  callback</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#E0AF68">  interval</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> MaybeRefOrGetter</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">number</span><span style="color:#89DDFF">&gt;,</span></span>
<span class="line"><span style="color:#E0AF68">  options</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span><span style="color:#73DACA"> immediate</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> boolean</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {}</span></span>
<span class="line"><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Stoppable</span><span style="color:#89DDFF"> &amp;</span><span style="color:#9ABDF5"> {</span><span style="color:#7AA2F7"> start</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span><span style="color:#9ABDF5"> }</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> immediate</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> true</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> options</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> isPending</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> shallowRef</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">false</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  let</span><span style="color:#BB9AF7"> timer</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> ReturnType</span><span style="color:#89DDFF">&lt;typeof</span><span style="color:#C0CAF5"> setTimeout</span><span style="color:#89DDFF">&gt;</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> null</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  function</span><span style="color:#7AA2F7"> stop</span><span style="color:#9ABDF5">() {</span></span>
<span class="line"><span style="color:#C0CAF5">    isPending</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> false</span></span>
<span class="line"><span style="color:#BB9AF7">    if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">timer</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#7AA2F7">      clearTimeout</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">timer</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#C0CAF5">      timer</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> null</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  function</span><span style="color:#7AA2F7"> start</span><span style="color:#9ABDF5">() {</span></span>
<span class="line"><span style="color:#7AA2F7">    stop</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#C0CAF5">    isPending</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> true</span></span>
<span class="line"><span style="color:#C0CAF5">    timer</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> setTimeout</span><span style="color:#9ABDF5">(() </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">      isPending</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> false</span></span>
<span class="line"><span style="color:#C0CAF5">      timer</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> null</span></span>
<span class="line"><span style="color:#7AA2F7">      callback</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#89DDFF">,</span><span style="color:#7AA2F7"> toValue</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">interval</span><span style="color:#9ABDF5">))</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">immediate</span><span style="color:#9ABDF5">) </span><span style="color:#7AA2F7">start</span><span style="color:#9ABDF5">()</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  tryOnCleanup</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">stop</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">    isPending</span><span style="color:#89DDFF">:</span><span style="color:#7AA2F7"> readonly</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">isPending</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    stop</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    start</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="export interface Stoppable {
  /** Whether the operation is pending */
  isPending: Readonly<Ref<boolean>>
  /** Stop the operation */
  stop: () => void
}

export function useTimeoutFn(
  callback: () => void,
  interval: MaybeRefOrGetter<number>,
  options: { immediate?: boolean } = {}
): Stoppable &#38; { start: () => void } {
  const { immediate = true } = options

  const isPending = shallowRef(false)
  let timer: ReturnType<typeof setTimeout> | null = null

  function stop() {
    isPending.value = false
    if (timer) {
      clearTimeout(timer)
      timer = null
    }
  }

  function start() {
    stop()
    isPending.value = true
    timer = setTimeout(() => {
      isPending.value = false
      timer = null
      callback()
    }, toValue(interval))
  }

  if (immediate) start()

  tryOnCleanup(stop)

  return {
    isPending: readonly(isPending),
    stop,
    start,
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr/>
<h2 id="11-error-handling">11. Error Handling<a class="heading-link" aria-label="Link to section" href="#11-error-handling"><span class="heading-link-icon">#</span></a></h2>
<h3 id="graceful-degradation">Graceful Degradation<a class="heading-link" aria-label="Link to section" href="#graceful-degradation"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useGeolocation</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> isSupported</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> useSupported</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#9ABDF5">    () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#C0CAF5"> navigator</span><span style="color:#BB9AF7"> &amp;&amp;</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">geolocation</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF"> in</span><span style="color:#C0CAF5"> navigator</span></span>
<span class="line"><span style="color:#9ABDF5">  )</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> coords</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> shallowRef</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">GeolocationCoordinates</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">null</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> error</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> shallowRef</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">GeolocationPositionError</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">null</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  function</span><span style="color:#7AA2F7"> update</span><span style="color:#9ABDF5">() {</span></span>
<span class="line"><span style="color:#BB9AF7">    if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#C0CAF5">isSupported</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7;font-style:italic">return</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">    navigator</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">geolocation</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">getCurrentPosition</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#9ABDF5">      (</span><span style="color:#E0AF68">position</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">        coords</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> position</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">coords</span></span>
<span class="line"><span style="color:#C0CAF5">        error</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> null</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">      (</span><span style="color:#E0AF68">err</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">        error</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> err</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span></span>
<span class="line"><span style="color:#9ABDF5">    )</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">isSupported</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#7AA2F7">    update</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">    isSupported</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    coords</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    error</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    update</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="export function useGeolocation() {
  const isSupported = useSupported(
    () => navigator &#38;&#38; 'geolocation' in navigator
  )

  const coords = shallowRef<GeolocationCoordinates | null>(null)
  const error = shallowRef<GeolocationPositionError | null>(null)

  function update() {
    if (!isSupported.value) return

    navigator.geolocation.getCurrentPosition(
      (position) => {
        coords.value = position.coords
        error.value = null
      },
      (err) => {
        error.value = err
      }
    )
  }

  if (isSupported.value) {
    update()
  }

  return {
    isSupported,
    coords,
    error,
    update,
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="error-callbacks">Error Callbacks<a class="heading-link" aria-label="Link to section" href="#error-callbacks"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> interface</span><span style="color:#C0CAF5"> UseAsyncStateOptions</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /** Called on success */</span></span>
<span class="line"><span style="color:#7AA2F7">  onSuccess</span><span style="color:#89DDFF">?:</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">data</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> T</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /** Called on error */</span></span>
<span class="line"><span style="color:#7AA2F7">  onError</span><span style="color:#89DDFF">?:</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">error</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> unknown</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   * Whether to throw errors</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   * </span><span style="color:#646E9C;font-style:italic">@default</span><span style="color:#5A638C;font-style:italic"> false</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   */</span></span>
<span class="line"><span style="color:#73DACA">  throwError</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> boolean</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useAsyncState</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#7AA2F7">  promise</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#C0CAF5"> Promise</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF">&gt;,</span></span>
<span class="line"><span style="color:#E0AF68">  initialState</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> T</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#E0AF68">  options</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> UseAsyncStateOptions</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF">&gt;</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {}</span></span>
<span class="line"><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> onSuccess</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> onError</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> throwError</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> false</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> options</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> state</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> shallowRef</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">initialState</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> error</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> shallowRef</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">unknown</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">null</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> isLoading</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> shallowRef</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">false</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  async</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> execute</span><span style="color:#9ABDF5">() {</span></span>
<span class="line"><span style="color:#C0CAF5">    isLoading</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> true</span></span>
<span class="line"><span style="color:#C0CAF5">    error</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> null</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">    try</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">      const</span><span style="color:#BB9AF7"> data</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#7AA2F7"> promise</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#C0CAF5">      state</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> data</span></span>
<span class="line"><span style="color:#7AA2F7">      onSuccess</span><span style="color:#89DDFF">?.</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">data</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">    } </span><span style="color:#BB9AF7">catch</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">e</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">      error</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> e</span></span>
<span class="line"><span style="color:#7AA2F7">      onError</span><span style="color:#89DDFF">?.</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">e</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#BB9AF7">      if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">throwError</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">throw</span><span style="color:#C0CAF5"> e</span></span>
<span class="line"><span style="color:#9ABDF5">    } </span><span style="color:#BB9AF7">finally</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">      isLoading</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> false</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  execute</span><span style="color:#9ABDF5">()</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> { </span><span style="color:#C0CAF5">state</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> error</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> isLoading</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> execute</span><span style="color:#9ABDF5"> }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="export interface UseAsyncStateOptions<T> {
  /** Called on success */
  onSuccess?: (data: T) => void
  /** Called on error */
  onError?: (error: unknown) => void
  /**
   * Whether to throw errors
   * @default false
   */
  throwError?: boolean
}

export function useAsyncState<T>(
  promise: () => Promise<T>,
  initialState: T,
  options: UseAsyncStateOptions<T> = {}
) {
  const { onSuccess, onError, throwError = false } = options

  const state = shallowRef<T>(initialState)
  const error = shallowRef<unknown>(null)
  const isLoading = shallowRef(false)

  async function execute() {
    isLoading.value = true
    error.value = null

    try {
      const data = await promise()
      state.value = data
      onSuccess?.(data)
    } catch (e) {
      error.value = e
      onError?.(e)
      if (throwError) throw e
    } finally {
      isLoading.value = false
    }
  }

  execute()

  return { state, error, isLoading, execute }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr/>
<h2 id="13-typescript-best-practices">13. TypeScript Best Practices<a class="heading-link" aria-label="Link to section" href="#13-typescript-best-practices"><span class="heading-link-icon">#</span></a></h2>
<h3 id="generic-type-inference">Generic Type Inference<a class="heading-link" aria-label="Link to section" href="#generic-type-inference"><span class="heading-link-icon">#</span></a></h3>
<p>Let TypeScript infer types when possible:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// Type T is inferred from defaultValue</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useStorage</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">key</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> defaultValue</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> T</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Ref</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // ...</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Usage - types are inferred</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> name</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> useStorage</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">name</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">John</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span><span style="color:#51597D;font-style:italic">     // Ref&lt;string&gt;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> count</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> useStorage</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">count</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5">)</span><span style="color:#51597D;font-style:italic">        // Ref&lt;number&gt;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> user</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> useStorage</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">user</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span><span style="color:#73DACA"> id</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 1</span><span style="color:#9ABDF5"> })</span><span style="color:#51597D;font-style:italic">  // Ref&lt;{ id: number }&gt;</span></span></code><button type="button" class="copy" data-code="// Type T is inferred from defaultValue
export function useStorage<T>(key: string, defaultValue: T): Ref<T> {
  // ...
}

// Usage - types are inferred
const name = useStorage('name', 'John')     // Ref<string>
const count = useStorage('count', 0)        // Ref<number>
const user = useStorage('user', { id: 1 })  // Ref<{ id: number }>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="function-overloads">Function Overloads<a class="heading-link" aria-label="Link to section" href="#function-overloads"><span class="heading-link-icon">#</span></a></h3>
<p>Use overloads for different call signatures:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// Overload 1: Window events</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useEventListener</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">K</span><span style="color:#9D7CD8;font-style:italic"> extends</span><span style="color:#89DDFF"> keyof</span><span style="color:#C0CAF5"> WindowEventMap</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#E0AF68">  event</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> K</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#7AA2F7">  handler</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">e</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> WindowEventMap</span><span style="color:#9ABDF5">[</span><span style="color:#C0CAF5">K</span><span style="color:#9ABDF5">])</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span></span>
<span class="line"><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Overload 2: Element events</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useEventListener</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">K</span><span style="color:#9D7CD8;font-style:italic"> extends</span><span style="color:#89DDFF"> keyof</span><span style="color:#C0CAF5"> HTMLElementEventMap</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#E0AF68">  target</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> MaybeRefOrGetter</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">HTMLElement</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF">&gt;,</span></span>
<span class="line"><span style="color:#E0AF68">  event</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> K</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#7AA2F7">  handler</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">e</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> HTMLElementEventMap</span><span style="color:#9ABDF5">[</span><span style="color:#C0CAF5">K</span><span style="color:#9ABDF5">])</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span></span>
<span class="line"><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Implementation</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useEventListener</span><span style="color:#9ABDF5">(</span><span style="color:#F7768E;font-weight:bold">...</span><span style="color:#E0AF68">args</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> any</span><span style="color:#9ABDF5">[])</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // ... implementation handles all cases</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// Overload 1: Window events
export function useEventListener<K extends keyof WindowEventMap>(
  event: K,
  handler: (e: WindowEventMap[K]) => void
): () => void

// Overload 2: Element events
export function useEventListener<K extends keyof HTMLElementEventMap>(
  target: MaybeRefOrGetter<HTMLElement | null>,
  event: K,
  handler: (e: HTMLElementEventMap[K]) => void
): () => void

// Implementation
export function useEventListener(...args: any[]): () => void {
  // ... implementation handles all cases
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="conditional-return-types">Conditional Return Types<a class="heading-link" aria-label="Link to section" href="#conditional-return-types"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// If passed a ref, return just the toggle function</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useToggle</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#E0AF68">  value</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Ref</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">boolean</span><span style="color:#89DDFF">&gt;</span></span>
<span class="line"><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">value</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> boolean</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> boolean</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// If passed a plain value, return tuple</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useToggle</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#E0AF68">  initialValue</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> boolean</span></span>
<span class="line"><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#C0CAF5">Ref</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">boolean</span><span style="color:#89DDFF">&gt;,</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">value</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> boolean</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> boolean</span><span style="color:#9ABDF5">]</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Implementation</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useToggle</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#E0AF68">  initialValue</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> MaybeRef</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">boolean</span><span style="color:#89DDFF">&gt;</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> false</span></span>
<span class="line"><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> valueIsRef</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> isRef</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">initialValue</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> state</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> shallowRef</span><span style="color:#9ABDF5">(</span><span style="color:#7AA2F7">toValue</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">initialValue</span><span style="color:#9ABDF5">))</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#7AA2F7"> toggle</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">value</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> boolean</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">    state</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> value</span><span style="color:#BB9AF7"> ??</span><span style="color:#BB9AF7"> !</span><span style="color:#C0CAF5">state</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#C0CAF5"> state</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">valueIsRef</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#C0CAF5"> toggle</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> [</span><span style="color:#7DCFFF">state</span><span style="color:#89DDFF">,</span><span style="color:#7DCFFF"> toggle</span><span style="color:#9ABDF5">] </span><span style="color:#89DDFF">as</span><span style="color:#9D7CD8;font-style:italic"> const</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// If passed a ref, return just the toggle function
export function useToggle(
  value: Ref<boolean>
): (value?: boolean) => boolean

// If passed a plain value, return tuple
export function useToggle(
  initialValue?: boolean
): [Ref<boolean>, (value?: boolean) => boolean]

// Implementation
export function useToggle(
  initialValue: MaybeRef<boolean> = false
) {
  const valueIsRef = isRef(initialValue)
  const state = shallowRef(toValue(initialValue))

  const toggle = (value?: boolean) => {
    state.value = value ?? !state.value
    return state.value
  }

  if (valueIsRef) {
    return toggle
  }
  return [state, toggle] as const
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr/>
<h2 id="14-testing">14. Testing<a class="heading-link" aria-label="Link to section" href="#14-testing"><span class="heading-link-icon">#</span></a></h2>
<p>For comprehensive testing strategies including basic test structure, testing with timers, and testing async composables, see <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/how-to-test-vue-composables/" class="internal-link astro-3tyn5ojg"> How to Test Vue Composables </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">How to Test Vue Composables: A Comprehensive Guide with Vitest</span> <span class="preview-description astro-3tyn5ojg">Learn how to effectively test Vue composables using Vitest. Covers independent and dependent composables, with practical examples and best practices.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">vue</span><span class="preview-tag astro-3tyn5ojg">testing</span>  </span> <time class="preview-date astro-3tyn5ojg">Nov 25, 2023</time> </span> </span> </span>  <script>
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
<hr/>
<h2 id="15-documentation">15. Documentation<a class="heading-link" aria-label="Link to section" href="#15-documentation"><span class="heading-link-icon">#</span></a></h2>
<h3 id="jsdoc-comments">JSDoc Comments<a class="heading-link" aria-label="Link to section" href="#jsdoc-comments"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">/**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * Reactive mouse position</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> *</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * </span><span style="color:#646E9C;font-style:italic">@param</span><span style="color:#5A638C;font-style:italic"> options</span><span style="color:#51597D;font-style:italic"> - Configuration options</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * </span><span style="color:#646E9C;font-style:italic">@returns</span><span style="color:#51597D;font-style:italic"> Reactive mouse coordinates and source type</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> *</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * </span><span style="color:#646E9C;font-style:italic">@example</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * ```ts</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * const { x, y } = useMouse()</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> *</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * watchEffect(() =&gt; {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> *   console.log(`Mouse at ${x.value}, ${y.value}`)</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * })</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * ```</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> *</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * </span><span style="color:#646E9C;font-style:italic">@see</span><span style="color:#5A638C;font-style:italic"> https://your-docs.com/composables/use-mouse</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> */</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useMouse</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">options</span><span style="color:#89DDFF">?:</span><span style="color:#C0CAF5"> UseMouseOptions</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> UseMouseReturn</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // ...</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="/**
 * Reactive mouse position
 *
 * @param options - Configuration options
 * @returns Reactive mouse coordinates and source type
 *
 * @example
 * ```ts
 * const { x, y } = useMouse()
 *
 * watchEffect(() => {
 *   console.log(`Mouse at ${x.value}, ${y.value}`)
 * })
 * ```
 *
 * @see https://your-docs.com/composables/use-mouse
 */
export function useMouse(options?: UseMouseOptions): UseMouseReturn {
  // ...
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="document-every-option">Document Every Option<a class="heading-link" aria-label="Link to section" href="#document-every-option"><span class="heading-link-icon">#</span></a></h3>
<p>Every option should have a JSDoc comment with a <code>@default</code> tag:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> interface</span><span style="color:#C0CAF5"> UseStorageOptions</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   * Storage type to use</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   * </span><span style="color:#646E9C;font-style:italic">@default</span><span style="color:#89DDFF;font-style:italic"> &#39;</span><span style="color:#5A638C;font-style:italic">local</span><span style="color:#89DDFF;font-style:italic">&#39;</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   */</span></span>
<span class="line"><span style="color:#73DACA">  storage</span><span style="color:#89DDFF">?:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">local</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">session</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   * Whether to sync across browser tabs</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   * </span><span style="color:#646E9C;font-style:italic">@default</span><span style="color:#5A638C;font-style:italic"> true</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   */</span></span>
<span class="line"><span style="color:#73DACA">  listenToStorageChanges</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> boolean</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="export interface UseStorageOptions {
  /**
   * Storage type to use
   * @default 'local'
   */
  storage?: 'local' | 'session'

  /**
   * Whether to sync across browser tabs
   * @default true
   */
  listenToStorageChanges?: boolean
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr/>
<h2 id="16-templates">16. Templates<a class="heading-link" aria-label="Link to section" href="#16-templates"><span class="heading-link-icon">#</span></a></h2>
<h3 id="basic-composable-template">Basic Composable Template<a class="heading-link" aria-label="Link to section" href="#basic-composable-template"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">shallowRef</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> readonly</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> toValue</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> type</span><span style="color:#0DB9D7"> MaybeRefOrGetter</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> type</span><span style="color:#0DB9D7"> Ref</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">tryOnCleanup</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">../utils/cleanup</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> interface</span><span style="color:#C0CAF5"> UseXxxOptions</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   * Option description</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   * </span><span style="color:#646E9C;font-style:italic">@default</span><span style="color:#89DDFF;font-style:italic"> &#39;</span><span style="color:#5A638C;font-style:italic">defaultValue</span><span style="color:#89DDFF;font-style:italic">&#39;</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   */</span></span>
<span class="line"><span style="color:#73DACA">  someOption</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> string</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> interface</span><span style="color:#C0CAF5"> UseXxxReturn</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /** Description of value */</span></span>
<span class="line"><span style="color:#73DACA">  value</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Readonly</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Ref</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">number</span><span style="color:#89DDFF">&gt;&gt;</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /** Description of action */</span></span>
<span class="line"><span style="color:#7AA2F7">  doSomething</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">/**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * Short description of what this composable does</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> *</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * </span><span style="color:#646E9C;font-style:italic">@param</span><span style="color:#5A638C;font-style:italic"> param</span><span style="color:#51597D;font-style:italic"> - Description of parameter</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * </span><span style="color:#646E9C;font-style:italic">@param</span><span style="color:#5A638C;font-style:italic"> options</span><span style="color:#51597D;font-style:italic"> - Configuration options</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> */</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useXxx</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#E0AF68">  param</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> MaybeRefOrGetter</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">string</span><span style="color:#89DDFF">&gt;,</span></span>
<span class="line"><span style="color:#E0AF68">  options</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> UseXxxOptions</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {}</span></span>
<span class="line"><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> UseXxxReturn</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> someOption</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">defaultValue</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> options</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> value</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> shallowRef</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">0</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  function</span><span style="color:#7AA2F7"> doSomething</span><span style="color:#9ABDF5">() {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> paramValue</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> toValue</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">param</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#C0CAF5">    value</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">++</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Cleanup if needed</span></span>
<span class="line"><span style="color:#7AA2F7">  tryOnCleanup</span><span style="color:#9ABDF5">(() </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">    // cleanup logic</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">    value</span><span style="color:#89DDFF">:</span><span style="color:#7AA2F7"> readonly</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">value</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    doSomething</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="import { shallowRef, readonly, toValue, type MaybeRefOrGetter, type Ref } from 'vue'
import { tryOnCleanup } from '../utils/cleanup'

export interface UseXxxOptions {
  /**
   * Option description
   * @default 'defaultValue'
   */
  someOption?: string
}

export interface UseXxxReturn {
  /** Description of value */
  value: Readonly<Ref<number>>
  /** Description of action */
  doSomething: () => void
}

/**
 * Short description of what this composable does
 *
 * @param param - Description of parameter
 * @param options - Configuration options
 */
export function useXxx(
  param: MaybeRefOrGetter<string>,
  options: UseXxxOptions = {}
): UseXxxReturn {
  const { someOption = 'defaultValue' } = options

  const value = shallowRef(0)

  function doSomething() {
    const paramValue = toValue(param)
    value.value++
  }

  // Cleanup if needed
  tryOnCleanup(() => {
    // cleanup logic
  })

  return {
    value: readonly(value),
    doSomething,
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="async-composable-template">Async Composable Template<a class="heading-link" aria-label="Link to section" href="#async-composable-template"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">shallowRef</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> readonly</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> toValue</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> type</span><span style="color:#0DB9D7"> MaybeRefOrGetter</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> type</span><span style="color:#0DB9D7"> Ref</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">createEventHook</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> type</span><span style="color:#0DB9D7"> EventHook</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">../utils/eventHook</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">tryOnCleanup</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">../utils/cleanup</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> interface</span><span style="color:#C0CAF5"> UseAsyncXxxOptions</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   * Execute immediately</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   * </span><span style="color:#646E9C;font-style:italic">@default</span><span style="color:#5A638C;font-style:italic"> true</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   */</span></span>
<span class="line"><span style="color:#73DACA">  immediate</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> boolean</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   * Called on success</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   */</span></span>
<span class="line"><span style="color:#7AA2F7">  onSuccess</span><span style="color:#89DDFF">?:</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">data</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> T</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   * Called on error</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   */</span></span>
<span class="line"><span style="color:#7AA2F7">  onError</span><span style="color:#89DDFF">?:</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">error</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Error</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> interface</span><span style="color:#C0CAF5"> UseAsyncXxxReturn</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  data</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Readonly</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Ref</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF">&gt;&gt;</span></span>
<span class="line"><span style="color:#73DACA">  error</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Readonly</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Ref</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Error</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF">&gt;&gt;</span></span>
<span class="line"><span style="color:#73DACA">  isLoading</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Readonly</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Ref</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">boolean</span><span style="color:#89DDFF">&gt;&gt;</span></span>
<span class="line"><span style="color:#7AA2F7">  execute</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#C0CAF5"> Promise</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">void</span><span style="color:#89DDFF">&gt;</span></span>
<span class="line"><span style="color:#73DACA">  onSuccess</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> EventHook</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">[</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">on</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span></span>
<span class="line"><span style="color:#73DACA">  onError</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> EventHook</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Error</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">[</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">on</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useAsyncXxx</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#7AA2F7">  fetcher</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#C0CAF5"> Promise</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF">&gt;,</span></span>
<span class="line"><span style="color:#E0AF68">  options</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> UseAsyncXxxOptions</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF">&gt;</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {}</span></span>
<span class="line"><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> UseAsyncXxxReturn</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> immediate</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> true</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> onSuccess</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> onError</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> options</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> data</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> shallowRef</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">null</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> error</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> shallowRef</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Error</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">null</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> isLoading</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> shallowRef</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">false</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> successHook</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> createEventHook</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> errorHook</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> createEventHook</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Error</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">()</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  async</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> execute</span><span style="color:#9ABDF5">() {</span></span>
<span class="line"><span style="color:#C0CAF5">    isLoading</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> true</span></span>
<span class="line"><span style="color:#C0CAF5">    error</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> null</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">    try</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">      const</span><span style="color:#BB9AF7"> result</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#7AA2F7"> fetcher</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#C0CAF5">      data</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> result</span></span>
<span class="line"><span style="color:#7AA2F7">      onSuccess</span><span style="color:#89DDFF">?.</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">result</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#C0CAF5">      successHook</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">trigger</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">result</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">    } </span><span style="color:#BB9AF7">catch</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">e</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">      const</span><span style="color:#BB9AF7"> err</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> e</span><span style="color:#89DDFF"> as</span><span style="color:#C0CAF5"> Error</span></span>
<span class="line"><span style="color:#C0CAF5">      error</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> err</span></span>
<span class="line"><span style="color:#7AA2F7">      onError</span><span style="color:#89DDFF">?.</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">err</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#C0CAF5">      errorHook</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">trigger</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">err</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">    } </span><span style="color:#BB9AF7">finally</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">      isLoading</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> false</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">immediate</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#7AA2F7">    execute</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">    data</span><span style="color:#89DDFF">:</span><span style="color:#7AA2F7"> readonly</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">data</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    error</span><span style="color:#89DDFF">:</span><span style="color:#7AA2F7"> readonly</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">error</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    isLoading</span><span style="color:#89DDFF">:</span><span style="color:#7AA2F7"> readonly</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">isLoading</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    execute</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    onSuccess</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> successHook</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">on</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    onError</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> errorHook</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">on</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="import { shallowRef, readonly, toValue, type MaybeRefOrGetter, type Ref } from 'vue'
import { createEventHook, type EventHook } from '../utils/eventHook'
import { tryOnCleanup } from '../utils/cleanup'

export interface UseAsyncXxxOptions<T> {
  /**
   * Execute immediately
   * @default true
   */
  immediate?: boolean
  /**
   * Called on success
   */
  onSuccess?: (data: T) => void
  /**
   * Called on error
   */
  onError?: (error: Error) => void
}

export interface UseAsyncXxxReturn<T> {
  data: Readonly<Ref<T | null>>
  error: Readonly<Ref<Error | null>>
  isLoading: Readonly<Ref<boolean>>
  execute: () => Promise<void>
  onSuccess: EventHook<T>['on']
  onError: EventHook<Error>['on']
}

export function useAsyncXxx<T>(
  fetcher: () => Promise<T>,
  options: UseAsyncXxxOptions<T> = {}
): UseAsyncXxxReturn<T> {
  const { immediate = true, onSuccess, onError } = options

  const data = shallowRef<T | null>(null)
  const error = shallowRef<Error | null>(null)
  const isLoading = shallowRef(false)

  const successHook = createEventHook<T>()
  const errorHook = createEventHook<Error>()

  async function execute() {
    isLoading.value = true
    error.value = null

    try {
      const result = await fetcher()
      data.value = result
      onSuccess?.(result)
      successHook.trigger(result)
    } catch (e) {
      const err = e as Error
      error.value = err
      onError?.(err)
      errorHook.trigger(err)
    } finally {
      isLoading.value = false
    }
  }

  if (immediate) {
    execute()
  }

  return {
    data: readonly(data),
    error: readonly(error),
    isLoading: readonly(isLoading),
    execute,
    onSuccess: successHook.on,
    onError: errorHook.on,
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="pausable-composable-template">Pausable Composable Template<a class="heading-link" aria-label="Link to section" href="#pausable-composable-template"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">shallowRef</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> readonly</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> toValue</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> type</span><span style="color:#0DB9D7"> MaybeRefOrGetter</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> type</span><span style="color:#0DB9D7"> Ref</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">tryOnCleanup</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">../utils/cleanup</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> interface</span><span style="color:#C0CAF5"> Pausable</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  isActive</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Readonly</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Ref</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">boolean</span><span style="color:#89DDFF">&gt;&gt;</span></span>
<span class="line"><span style="color:#7AA2F7">  pause</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span></span>
<span class="line"><span style="color:#7AA2F7">  resume</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> interface</span><span style="color:#C0CAF5"> UsePausableXxxOptions</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   * Start immediately</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   * </span><span style="color:#646E9C;font-style:italic">@default</span><span style="color:#5A638C;font-style:italic"> true</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   */</span></span>
<span class="line"><span style="color:#73DACA">  immediate</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> boolean</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> usePausableXxx</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#7AA2F7">  callback</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#E0AF68">  interval</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> MaybeRefOrGetter</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">number</span><span style="color:#89DDFF">&gt;</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> 1000</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#E0AF68">  options</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> UsePausableXxxOptions</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {}</span></span>
<span class="line"><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Pausable</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> immediate</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> true</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> options</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> isActive</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> shallowRef</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">false</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  let</span><span style="color:#BB9AF7"> timer</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> ReturnType</span><span style="color:#89DDFF">&lt;typeof</span><span style="color:#C0CAF5"> setInterval</span><span style="color:#89DDFF">&gt;</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> null</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  function</span><span style="color:#7AA2F7"> clean</span><span style="color:#9ABDF5">() {</span></span>
<span class="line"><span style="color:#BB9AF7">    if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">timer</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#7AA2F7">      clearInterval</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">timer</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#C0CAF5">      timer</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> null</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  function</span><span style="color:#7AA2F7"> pause</span><span style="color:#9ABDF5">() {</span></span>
<span class="line"><span style="color:#C0CAF5">    isActive</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> false</span></span>
<span class="line"><span style="color:#7AA2F7">    clean</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  function</span><span style="color:#7AA2F7"> resume</span><span style="color:#9ABDF5">() {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> ms</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> toValue</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">interval</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#BB9AF7">    if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">ms</span><span style="color:#BB9AF7"> &lt;=</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7;font-style:italic">return</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">    isActive</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> true</span></span>
<span class="line"><span style="color:#7AA2F7">    clean</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#C0CAF5">    timer</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> setInterval</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">callback</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> ms</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">immediate</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#7AA2F7">    resume</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  tryOnCleanup</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">pause</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">    isActive</span><span style="color:#89DDFF">:</span><span style="color:#7AA2F7"> readonly</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">isActive</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    pause</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    resume</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="import { shallowRef, readonly, toValue, type MaybeRefOrGetter, type Ref } from 'vue'
import { tryOnCleanup } from '../utils/cleanup'

export interface Pausable {
  isActive: Readonly<Ref<boolean>>
  pause: () => void
  resume: () => void
}

export interface UsePausableXxxOptions {
  /**
   * Start immediately
   * @default true
   */
  immediate?: boolean
}

export function usePausableXxx(
  callback: () => void,
  interval: MaybeRefOrGetter<number> = 1000,
  options: UsePausableXxxOptions = {}
): Pausable {
  const { immediate = true } = options

  const isActive = shallowRef(false)
  let timer: ReturnType<typeof setInterval> | null = null

  function clean() {
    if (timer) {
      clearInterval(timer)
      timer = null
    }
  }

  function pause() {
    isActive.value = false
    clean()
  }

  function resume() {
    const ms = toValue(interval)
    if (ms <= 0) return

    isActive.value = true
    clean()
    timer = setInterval(callback, ms)
  }

  if (immediate) {
    resume()
  }

  tryOnCleanup(pause)

  return {
    isActive: readonly(isActive),
    pause,
    resume,
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr/>
<h2 id="quick-reference-checklist">Quick Reference Checklist<a class="heading-link" aria-label="Link to section" href="#quick-reference-checklist"><span class="heading-link-icon">#</span></a></h2>
<p>Use this checklist when creating new composables:</p>
<p><strong>Structure</strong></p>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled/> Named export (no default)</li>
<li class="task-list-item"><input type="checkbox" disabled/> Explicit return type interface</li>
<li class="task-list-item"><input type="checkbox" disabled/> JSDoc with <code>@param</code>, <code>@returns</code>, <code>@example</code></li>
</ul>
<p><strong>Reactivity</strong></p>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled/> <code>shallowRef</code> for primitives</li>
<li class="task-list-item"><input type="checkbox" disabled/> <code>ref</code> only when deep mutations needed</li>
<li class="task-list-item"><input type="checkbox" disabled/> <code>MaybeRefOrGetter</code> for flexible inputs</li>
<li class="task-list-item"><input type="checkbox" disabled/> <code>toValue()</code> to unwrap inputs</li>
<li class="task-list-item"><input type="checkbox" disabled/> <code>readonly()</code> for exposed refs</li>
</ul>
<p><strong>Safety</strong></p>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled/> Guard browser APIs (<code>if (window)</code>)</li>
<li class="task-list-item"><input type="checkbox" disabled/> Auto-cleanup with <code>tryOnCleanup</code></li>
<li class="task-list-item"><input type="checkbox" disabled/> Feature detection for optional APIs</li>
</ul>
<p><strong>TypeScript</strong></p>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled/> Generic type inference where possible</li>
<li class="task-list-item"><input type="checkbox" disabled/> Overloads for multiple signatures</li>
<li class="task-list-item"><input type="checkbox" disabled/> Strict types, no <code>any</code></li>
</ul>
<p><strong>Testing</strong></p>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled/> Unit tests for all functionality</li>
<li class="task-list-item"><input type="checkbox" disabled/> Edge cases (null, undefined, empty)</li>
<li class="task-list-item"><input type="checkbox" disabled/> Cleanup verification</li>
</ul>
<hr/>
<h2 id="additional-resources">Additional Resources<a class="heading-link" aria-label="Link to section" href="#additional-resources"><span class="heading-link-icon">#</span></a></h2>
<ul>
<li><a href="https://vuejs.org/guide/extras/composition-api-faq.html" rel="noopener noreferrer" target="_blank">Vue Composition API Docs</a></li>
<li><a href="https://vuejs.org/guide/extras/reactivity-in-depth.html" rel="noopener noreferrer" target="_blank">Vue Reactivity in Depth</a></li>
<li><a href="https://vueuse.org" rel="noopener noreferrer" target="_blank">VueUse</a> - Collection of Vue composables (the source of these patterns)</li>
<li><a href="https://vitest.dev" rel="noopener noreferrer" target="_blank">Vitest</a> - Testing framework for Vue</li>
</ul>
<hr/>
<p>These patterns represent the accumulated wisdom from VueUse’s codebase. Apply them consistently to build maintainable, type-safe, and production-ready Vue composables.</p> </article> <script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).only=e;window.dispatchEvent(new Event("astro:only"));})();</script><astro-island uid="Z1XneyL" component-url="/_astro/presentation.C3Wa0mjp.js" component-export="VMarkBlogRenderer" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;containerSelector&quot;:[0,&quot;#article&quot;],&quot;class&quot;:[0,&quot;astro-vj4tpspi&quot;]}" ssr client="only" opts="{&quot;name&quot;:&quot;VMarkBlogRenderer&quot;,&quot;value&quot;:&quot;react&quot;}"></astro-island> <!-- Fullscreen Modal Container using native dialog --><dialog id="mermaid-modal" class="mermaid-modal" aria-label="Fullscreen diagram view"> <div class="mermaid-modal-content"> <button class="mermaid-modal-close" aria-label="Close fullscreen view" type="button"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <line x1="18" y1="6" x2="6" y2="18"></line> <line x1="6" y1="6" x2="18" y2="18"></line> </svg> </button> <div class="mermaid-modal-diagram"></div> <div class="mermaid-modal-hint">Press <kbd>Esc</kbd> or click outside to close</div> </div> </dialog>  <script type="module">const p=new Set;function g(){const e=document.getElementById("mermaid-modal"),c=e?.querySelector(".mermaid-modal-diagram"),f=e?.querySelector(".mermaid-modal-close");if(!e||!c)return;document.querySelectorAll('svg[id^="mermaid-"]').forEach(t=>{if(!t.id.match(/^mermaid-\d+$/)||p.has(t.id)||t.parentElement?.classList.contains("mermaid-fullscreen-wrapper")||t.closest(".mermaid-modal"))return;p.add(t.id);const n=document.createElement("div");n.className="mermaid-fullscreen-wrapper mermaid-clickable",n.setAttribute("tabindex","0"),n.setAttribute("role","button"),n.setAttribute("aria-label","Click to view diagram fullscreen"),t.parentElement?.insertBefore(n,t),n.appendChild(t);const o=document.createElement("div");o.className="mermaid-expand-icon",o.innerHTML=`
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
</li> <li class="astro-vj4tpspi">Small tips and trick</li> </ul> </div> <a href="https://alex-op-newsletter.beehiiv.com/subscribe?utm_source=blog&utm_medium=post&utm_campaign=post_vueuse_composables_style_guide" target="_blank" rel="noopener noreferrer" id="newsletter-subscribe-button" class="inline-flex items-center justify-center gap-2 rounded-full bg-skin-accent px-6 py-3 text-base font-semibold text-skin-inverted shadow-md transition-all duration-200 hover:scale-[1.02] hover:transform hover:opacity-90 astro-vj4tpspi"> <svg class="h-5 w-5 fill-current astro-vj4tpspi" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg>
Subscribe Now
</a> <button id="newsletter-dismiss" data-post-slug="vueuse_composables_style_guide" class="absolute right-3 top-3 rounded-full p-1 text-skin-base transition-all duration-200 hover:bg-skin-accent hover:bg-opacity-10 hover:text-skin-accent astro-vj4tpspi" aria-label="Close notification"> <svg class="h-5 w-5 astro-vj4tpspi" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class="astro-vj4tpspi"></path> </svg> </button> </div> </div> </div> <ul class="my-8 flex flex-wrap gap-2 astro-vj4tpspi"> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/vue/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-2"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">vue</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/typescript/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-3"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">typescript</span>   </a> </li>  </ul> <div class="flex flex-col-reverse items-center justify-between gap-6 sm:flex-row-reverse sm:items-end sm:gap-4 astro-vj4tpspi"> <button id="back-to-top" class="focus-outline whitespace-nowrap py-1 hover:opacity-75 astro-vj4tpspi"> <svg xmlns="http://www.w3.org/2000/svg" class="rotate-90 astro-vj4tpspi"> <path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg> <span class="astro-vj4tpspi">Back to Top</span> </button> <div class="social-icons astro-wkojbtzc"> <span class="italic astro-wkojbtzc">Share this post on:</span> <div class="text-center astro-wkojbtzc"> <a href="https://wa.me/?text=https://alexop.dev/posts/vueuse_composables_style_guide/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via WhatsApp" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"></path>
      <path d="M9 10a0.5 .5 0 0 0 1 0v-1a0.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a0.5 .5 0 0 0 0 -1h-1a0.5 .5 0 0 0 0 1"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via WhatsApp</span> </a><a href="https://www.facebook.com/sharer.php?u=https://alexop.dev/posts/vueuse_composables_style_guide/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Facebook" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"
    ></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on Facebook</span> </a><a href="https://x.com/intent/tweet?url=https://alexop.dev/posts/vueuse_composables_style_guide/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Tweet this post" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Tweet this post</span> </a><a href="https://t.me/share/url?url=https://alexop.dev/posts/vueuse_composables_style_guide/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via Telegram" target="_blank" rel="noopener noreferrer"> <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon-tabler"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"></path>
      </svg> <span class="sr-only astro-wkojbtzc">Share this post via Telegram</span> </a><a href="https://pinterest.com/pin/create/button/?url=https://alexop.dev/posts/vueuse_composables_style_guide/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Pinterest" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <line x1="8" y1="20" x2="12" y2="11"></line>
      <path d="M10.7 14c.437 1.263 1.43 2 2.55 2c2.071 0 3.75 -1.554 3.75 -4a5 5 0 1 0 -9.7 1.7"></path>
      <circle cx="12" cy="12" r="9"></circle>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post on Pinterest</span> </a><a href="mailto:?subject=See%20this%20post&#38;body=https://alexop.dev/posts/vueuse_composables_style_guide/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via email" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via email</span> </a><a href="https://www.linkedin.com/shareArticle?mini=true&url=https://alexop.dev/posts/vueuse_composables_style_guide/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
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
    </script> </body> </html>  <script>(function(){const postSlug = "vueuse_composables_style_guide";

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
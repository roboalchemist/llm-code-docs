# Source: https://alexop.dev/posts/mastering-graphql-fragments-vue3-component-driven-data-fetching

<!DOCTYPE html><html lang="en" class="scroll-smooth astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/posts/mastering-graphql-fragments-vue3-component-driven-data-fetching/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>Mastering GraphQL Fragments in Vue 3: Component-Driven Data Fetching | alexop.dev</title><meta name="title" content="Mastering GraphQL Fragments in Vue 3: Component-Driven Data Fetching | alexop.dev"><meta name="description" content="Part 3 of the Vue 3 + GraphQL series: Learn how to use GraphQL fragments with fragment masking to create truly component-driven data fetching in Vue 3."><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="Mastering GraphQL Fragments in Vue 3: Component-Driven Data Fetching | alexop.dev"><meta property="og:description" content="Part 3 of the Vue 3 + GraphQL series: Learn how to use GraphQL fragments with fragment masking to create truly component-driven data fetching in Vue 3."><meta property="og:url" content="https://alexop.dev/posts/mastering-graphql-fragments-vue3-component-driven-data-fetching/"><meta property="og:image" content="https://alexop.dev/posts/mastering-graph-ql-fragments-in-vue-3-component-driven-data-fetching/index.png"><meta property="og:type" content="article"><!-- Article Published/Modified time --><meta property="article:published_time" content="2025-07-06T00:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/posts/mastering-graphql-fragments-vue3-component-driven-data-fetching/"><meta property="twitter:title" content="Mastering GraphQL Fragments in Vue 3: Component-Driven Data Fetching | alexop.dev"><meta property="twitter:description" content="Part 3 of the Vue 3 + GraphQL series: Learn how to use GraphQL fragments with fragment masking to create truly component-driven data fetching in Vue 3."><meta property="twitter:image" content="https://alexop.dev/posts/mastering-graph-ql-fragments-in-vue-3-component-driven-data-fetching/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"Mastering GraphQL Fragments in Vue 3: Component-Driven Data Fetching | alexop.dev","description":"Part 3 of the Vue 3 + GraphQL series: Learn how to use GraphQL fragments with fragment masking to create truly component-driven data fetching in Vue 3.","image":"https://alexop.dev/posts/mastering-graph-ql-fragments-in-vue-3-component-driven-data-fetching/index.png","datePublished":"2025-07-06T00:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
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
</style><style>[data-astro-transition-scope="astro-plk3gbjq-1"] { view-transition-name: mastering-graph-ql-fragments-in-vue-3-component-driven-data-fetching; }@layer astro { ::view-transition-old(mastering-graph-ql-fragments-in-vue-3-component-driven-data-fetching) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(mastering-graph-ql-fragments-in-vue-3-component-driven-data-fetching) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(mastering-graph-ql-fragments-in-vue-3-component-driven-data-fetching) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(mastering-graph-ql-fragments-in-vue-3-component-driven-data-fetching) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-2"] { view-transition-name: graphql; }@layer astro { ::view-transition-old(graphql) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(graphql) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(graphql) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(graphql) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-4"] { view-transition-name: typescript; }@layer astro { ::view-transition-old(typescript) { 
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <div class="mx-auto flex w-full max-w-5xl justify-start px-2 astro-vj4tpspi"> <button class="focus-outline mb-2 mt-8 flex hover:opacity-75 astro-vj4tpspi" onclick="(() => (history.length === 1) ? window.location = '/' : history.back())()"> <svg xmlns="http://www.w3.org/2000/svg" class="astro-vj4tpspi"><path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg><span class="astro-vj4tpspi">Go back</span> </button> </div> <main data-pagefind-body id="main-content" class="relative astro-vj4tpspi"> <h1 class="post-title astro-vj4tpspi" data-astro-transition-scope="astro-plk3gbjq-1">Mastering GraphQL Fragments in Vue 3: Component-Driven Data Fetching</h1> <div class="my-2 flex items-center justify-between astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-100 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-base"><time dateTime="2025-07-06T00:00:00.000Z">Jul 6, 2025</time><span class="sr-only"> at </span></span></div> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="ui10s" prefix="r6" component-url="/_astro/PostCopyButton.-PGtk4At.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;title&quot;:[0,&quot;Mastering GraphQL Fragments in Vue 3: Component-Driven Data Fetching&quot;],&quot;content&quot;:[0,&quot;```mermaid\ngraph TD\n    A[\&quot;❌ Traditional Approach\&quot;] --&gt; A1[\&quot;Monolithic Queries\&quot;]\n    A1 --&gt; A2[\&quot;Over-fetching\&quot;]\n    A1 --&gt; A3[\&quot;Tight Coupling\&quot;]\n    A1 --&gt; A4[\&quot;Implicit Dependencies\&quot;]\n\n    B[\&quot;✅ Fragment Masking\&quot;] --&gt; B1[\&quot;Component-Owned Data\&quot;]\n    B1 --&gt; B2[\&quot;Type Safety\&quot;]\n    B1 --&gt; B3[\&quot;Data Encapsulation\&quot;]\n    B1 --&gt; B4[\&quot;Safe Refactoring\&quot;]\n```\n\n## Why Fragments Are a Game-Changer\n\nIn Part 2, we achieved type safety with GraphQL Code Generator. But our queries are still monolithic—each component doesn&#39;t declare its own data needs. This creates several problems:\n\n- **Over-fetching**: Parent components request data their children might not need\n- **Under-fetching**: Adding a field means hunting down every query using that type\n- **Tight coupling**: Components depend on their parents to provide the right data\n- **Implicit dependencies**: Parent components can accidentally rely on data from child fragments\n- **Brittle refactoring**: Changing a component&#39;s data needs can break unrelated components\n\nEnter GraphQL fragments with **fragment masking**—the pattern that Relay popularized and that Apollo Client 3.12 has made even more powerful. This transforms how we think about data fetching by providing **true data encapsulation** at the component level.\n\n## What Are GraphQL Fragments?\n\nGraphQL fragments are **reusable units of fields** that components can declare for themselves. But they&#39;re more than just field groupings—when combined with fragment masking, they provide **data access control**.\n\n```graphql\nfragment CountryBasicInfo on Country {\n  code\n  name\n  emoji\n  capital\n}\n```\n\n**Fragment masking** is the key innovation that makes fragments truly powerful. It ensures that:\n\n1. **Data is encapsulated**: Only the component that defines a fragment can access its fields\n2. **Dependencies are explicit**: Components can&#39;t accidentally rely on data from other fragments\n3. **Refactoring is safe**: Changing a fragment won&#39;t break unrelated components\n4. **Type safety is enforced**: TypeScript prevents accessing fields you didn&#39;t request\n\n## Understanding Fragments Through the Spread Operator\n\nIf you&#39;re familiar with JavaScript&#39;s spread operator, fragments work exactly the same way:\n\n```javascript\n// JavaScript objects\nconst basicInfo = { code: \&quot;US\&quot;, name: \&quot;United States\&quot; };\nconst fullCountry = { ...basicInfo, capital: \&quot;Washington D.C.\&quot; };\n```\n\n```graphql\n# GraphQL fragments\nfragment CountryBasicInfo on Country {\n  code\n  name\n}\n\nquery GetCountryDetails {\n  country(code: \&quot;US\&quot;) {\n    ...CountryBasicInfo # Spread fragment fields\n    capital # Add extra fields\n  }\n}\n```\n\n**Fragment masking** takes this further by ensuring components can only access the data they explicitly request—pioneered by **Relay** and now enhanced in **Apollo Client 3.12**.\n\n## Step 1: Enable Fragment Masking\n\nEnsure your `codegen.ts` uses the client preset (from Part 2):\n\n```typescript\nconst config: CodegenConfig = {\n  overwrite: true,\n  schema: \&quot;https://countries.trevorblades.com/graphql\&quot;,\n  documents: [\&quot;src/**/*.vue\&quot;, \&quot;src/**/*.graphql\&quot;],\n  generates: {\n    \&quot;src/gql/\&quot;: {\n      preset: \&quot;client\&quot;,\n      plugins: [],\n      config: { useTypeImports: true },\n    },\n  },\n};\n```\n\nThis generates:\n\n- `FragmentType&lt;T&gt;`: Masked fragment types for props\n- `useFragment()`: Function to unmask fragment data\n- Type safety to prevent accessing non-fragment fields\n\n## Step 2: Your First Fragment with Masking\n\nLet&#39;s create a `CountryCard` component that declares its own data requirements:\n\n```vue\n&lt;script setup lang=\&quot;ts\&quot;&gt;\nimport { computed } from \&quot;vue\&quot;;\nimport { graphql } from \&quot;../gql\&quot;;\nimport { FragmentType, useFragment } from \&quot;../gql/fragment-masking\&quot;;\n\n// Define what data this component needs\nconst CountryCard_CountryFragment = graphql(`\n  fragment CountryCard_CountryFragment on Country {\n    code\n    name\n    emoji\n    capital\n    phone\n    currency\n  }\n`);\n\n// Props accept a masked fragment type\ninterface Props {\n  country: FragmentType&lt;typeof CountryCard_CountryFragment&gt;;\n}\n\nconst props = defineProps&lt;Props&gt;();\n\n// Unmask to access the actual data (reactive for Vue)\nconst country = computed(() =&gt;\n  useFragment(CountryCard_CountryFragment, props.country)\n);\n&lt;/script&gt;\n\n&lt;template&gt;\n  &lt;div class=\&quot;country-card\&quot;&gt;\n    &lt;h3&gt;{{ country.emoji }} {{ country.name }}&lt;/h3&gt;\n    &lt;p&gt;Capital: {{ country.capital }}&lt;/p&gt;\n    &lt;p&gt;Phone: +{{ country.phone }}&lt;/p&gt;\n    &lt;p&gt;Currency: {{ country.currency }}&lt;/p&gt;\n  &lt;/div&gt;\n&lt;/template&gt;\n```\n\n## Understanding Fragment Masking: The Key to Data Isolation\n\n**Fragment masking** is the core concept that makes this pattern so powerful. It&#39;s not just about code organization—it&#39;s about **data access control and encapsulation**.\n\n### What Fragment Masking Actually Does\n\nThink of fragment masking like **access control in programming languages**. Just as a module can have private and public methods, fragment masking controls which components can access which pieces of data.\n\n```typescript\n// Without fragment masking (traditional approach)\nconst result = useQuery(GET_COUNTRIES);\nconst countries = result.value?.countries || [];\n\n// ❌ Parent can access ANY field from the query\nconsole.log(countries[0].name); // Works\nconsole.log(countries[0].capital); // Works\nconsole.log(countries[0].currency); // Works\n```\n\nWith fragment masking enabled:\n\n```typescript\n// ✅ Parent component CANNOT access fragment fields\nconst name = result.value?.countries[0].name; // TypeScript error!\n\n// ✅ Only CountryCard can access its fragment data\nconst country = useFragment(CountryCard_CountryFragment, props.country);\nconsole.log(country.name); // Works!\n```\n\n### The Power of Data Encapsulation\n\nFragment masking provides **true data encapsulation**:\n\n1. **Prevents Implicit Dependencies**: Parent components can&#39;t accidentally rely on data their children need\n2. **Catches Breaking Changes Early**: If a child component removes a field, the parent can&#39;t access it anymore\n3. **Enforces Component Boundaries**: Each component owns its data requirements\n4. **Enables Safe Refactoring**: Change a fragment without breaking unrelated components\n\n### Why This Matters\n\nWithout fragment masking, parent components can accidentally depend on child fragment data. When the child removes a field, the parent breaks at runtime. With fragment masking, TypeScript catches this at compile time.\n\n```typescript\n// Parent can only access explicitly requested fields\ncountries[0].id; // ✅ Works (parent requested this)\ncountries[0].name; // ❌ TypeScript error (only in fragment)\n\n// Child components unmask their fragment data\nconst country = useFragment(CountryCard_CountryFragment, props.country);\ncountry.name; // ✅ Works (component owns this fragment)\n```\n\n&gt; **📝 Vue Reactivity Note**: Always wrap `useFragment` in a `computed()` for Vue reactivity. This ensures the component updates when fragment data changes.\n\n## Step 3: Parent Component Uses the Fragment\n\nNow the parent component includes the child&#39;s fragment in its query:\n\n```vue\n&lt;script setup lang=\&quot;ts\&quot;&gt;\nimport { computed } from \&quot;vue\&quot;;\nimport { useQuery } from \&quot;@vue/apollo-composable\&quot;;\nimport { graphql } from \&quot;../gql\&quot;;\nimport CountryCard from \&quot;./CountryCard.vue\&quot;;\n\nconst COUNTRIES_WITH_DETAILS_QUERY = graphql(`\n  query CountriesWithDetails {\n    countries {\n      code\n      # Parent can add its own fields\n      region\n      # Child component&#39;s fragment\n      ...CountryCard_CountryFragment\n    }\n  }\n`);\n\nconst { result, loading, error } = useQuery(COUNTRIES_WITH_DETAILS_QUERY);\n\n// Parent can access its own fields\nconst countriesByRegion = computed(() =&gt; {\n  if (!result.value?.countries) return {};\n\n  return result.value.countries.reduce(\n    (acc, country) =&gt; {\n      const region = country.region;\n      if (!acc[region]) acc[region] = [];\n      acc[region].push(country);\n      return acc;\n    },\n    {} as Record&lt;string, typeof result.value.countries&gt;\n  );\n});\n\n// But parent CANNOT access fragment fields:\n// const name = result.value?.countries[0].name ❌ TypeScript error!\n&lt;/script&gt;\n\n&lt;template&gt;\n  &lt;div class=\&quot;countries-container\&quot;&gt;\n    &lt;div v-if=\&quot;loading\&quot;&gt;Loading countries...&lt;/div&gt;\n    &lt;div v-else-if=\&quot;error\&quot;&gt;Error: {{ error.message }}&lt;/div&gt;\n    &lt;div v-else class=\&quot;countries-by-region\&quot;&gt;\n      &lt;div\n        v-for=\&quot;(countries, region) in countriesByRegion\&quot;\n        :key=\&quot;region\&quot;\n        class=\&quot;region-section\&quot;\n      &gt;\n        &lt;h2&gt;{{ region }}&lt;/h2&gt;\n        &lt;div class=\&quot;country-grid\&quot;&gt;\n          &lt;CountryCard\n            v-for=\&quot;country in countries\&quot;\n            :key=\&quot;country.code\&quot;\n            :country=\&quot;country\&quot;\n          /&gt;\n        &lt;/div&gt;\n      &lt;/div&gt;\n    &lt;/div&gt;\n  &lt;/div&gt;\n&lt;/template&gt;\n```\n\n## The Magic of Fragment Masking\n\nHere&#39;s what just happened:\n\n```mermaid\ngraph TB\n    subgraph \&quot;GraphQL Query Result\&quot;\n        QR[\&quot;countries: Country[]\&quot;]\n    end\n\n    subgraph \&quot;Parent Component\&quot;\n        PC[\&quot;Parent can access:&lt;br/&gt;• countries[].code&lt;br/&gt;• countries[].region&lt;br/&gt;❌ countries[].name\&quot;]\n    end\n\n    subgraph \&quot;Child Component\&quot;\n        CC[\&quot;CountryCard receives:&lt;br/&gt;Masked Fragment Data\&quot;]\n        UF[\&quot;useFragment() unmasks:&lt;br/&gt;• code&lt;br/&gt;• name&lt;br/&gt;• emoji&lt;br/&gt;• capital\&quot;]\n    end\n\n    QR --&gt; PC\n    QR --&gt; CC\n    CC --&gt; UF\n```\n\nThe parent component **cannot access** fields from `CountryCard_Fragment`—they&#39;re masked! Only `CountryCard` can unmask and use that data.\n\n## Step 4: Nested Fragments\n\nFragments can include other fragments, creating a hierarchy:\n\n```graphql\n# Basic fragment\nfragment LanguageItem_LanguageFragment on Language {\n  code\n  name\n  native\n}\n\n# Fragment that uses other fragments\nfragment CountryWithLanguages_CountryFragment on Country {\n  code\n  name\n  emoji\n  languages {\n    ...LanguageItem_LanguageFragment\n  }\n}\n```\n\nChild components use their own fragments:\n\n```vue\n&lt;!-- LanguageItem.vue --&gt;\n&lt;script setup lang=\&quot;ts\&quot;&gt;\nimport { computed } from \&quot;vue\&quot;;\nimport { graphql, FragmentType, useFragment } from \&quot;../gql\&quot;;\n\nconst LanguageItem_LanguageFragment = graphql(`\n  fragment LanguageItem_LanguageFragment on Language {\n    code\n    name\n    native\n  }\n`);\n\ninterface Props {\n  language: FragmentType&lt;typeof LanguageItem_LanguageFragment&gt;;\n}\n\nconst props = defineProps&lt;Props&gt;();\nconst language = computed(() =&gt;\n  useFragment(LanguageItem_LanguageFragment, props.language)\n);\n&lt;/script&gt;\n\n&lt;template&gt;\n  &lt;div class=\&quot;language-item\&quot;&gt;\n    &lt;span&gt;{{ language.name }} ({{ language.code }})&lt;/span&gt;\n  &lt;/div&gt;\n&lt;/template&gt;\n```\n\n## Fragment Dependency Management\n\nNotice how the query automatically includes all nested fragments:\n\n```mermaid\ngraph LR\n    subgraph \&quot;Components\&quot;\n        A[CountryDetailPage]\n        B[CountryWithLanguages.vue]\n        C[LanguageItem.vue]\n    end\n\n    subgraph \&quot;Their Fragments\&quot;\n        A1[Page Fields:&lt;br/&gt;code]\n        B1[Country Fragment:&lt;br/&gt;code, name, emoji&lt;br/&gt;languages]\n        C1[Language Fragment:&lt;br/&gt;code, name, native]\n    end\n\n    A -.-&gt; A1\n    B -.-&gt; B1\n    C -.-&gt; C1\n```\n\n## Step 5: Conditional Fragments\n\nUse GraphQL directives to conditionally include fragments:\n\n```graphql\nquery CountriesConditional($includeLanguages: Boolean!) {\n  countries {\n    code\n    name\n    ...CountryDetails_CountryFragment @include(if: $includeLanguages)\n  }\n}\n```\n\nThis enables dynamic data loading based on user interactions or application state.\n\n## Best Practices\n\n### Key Guidelines\n\n1. **Naming**: Use `ComponentName_TypeNameFragment` convention\n2. **Vue Reactivity**: Always wrap `useFragment` in `computed()`\n3. **TypeScript**: Use `FragmentType&lt;typeof MyFragment&gt;` for props\n4. **Organization**: Colocate fragments with components\n\n```typescript\n// ✅ Good naming and Vue reactivity\nconst CountryCard_CountryFragment = graphql(`...`);\n\ninterface Props {\n  country: FragmentType&lt;typeof CountryCard_CountryFragment&gt;;\n}\n\nconst country = computed(() =&gt;\n  useFragment(CountryCard_CountryFragment, props.country)\n);\n```\n\n## Performance Benefits\n\nFragments aren&#39;t just about developer experience - they provide concrete performance and maintainability benefits:\n\n```mermaid\ngraph TD\n    A[\&quot;❌ Multiple Queries\&quot;] --&gt; A1[\&quot;3 Network Requests\&quot;]\n    A1 --&gt; A2[\&quot;Duplicate Data Fetching\&quot;]\n    A2 --&gt; A3[\&quot;Larger Bundle Size\&quot;]\n\n    B[\&quot;✅ Fragment Composition\&quot;] --&gt; B1[\&quot;Single Network Request\&quot;]\n    B1 --&gt; B2[\&quot;Optimized Payload\&quot;]\n    B2 --&gt; B3[\&quot;Better Performance\&quot;]\n```\n\n## Summary\n\nGraphQL fragments with fragment masking enable **component-driven data fetching** in Vue 3:\n\n✅ **Type Safety**: Components can only access their declared fields\n✅ **True Modularity**: Each component declares its exact data needs  \n✅ **Better Performance**: Load only the data you need\n✅ **Maintainable Code**: Changes to fragments don&#39;t break unrelated components\n\n## Migration Checklist\n\n1. Start with leaf components (no children)\n2. Always use `computed()` with `useFragment` for Vue reactivity\n3. Update TypeScript interfaces to use `FragmentType`\n4. Run `npm run codegen` after fragment changes\n\n## What&#39;s Next?\n\nThis is Part 3 of our Vue 3 + GraphQL series:\n\n1. **Part 1**: Setting up Apollo Client with Vue 3\n2. **Part 2**: Type-safe queries with GraphQL Code Generator\n3. **Part 3**: Advanced fragments and component-driven data fetching (current)\n4. **Part 4**: GraphQL Caching Strategies in Vue 3 (coming next!)\n\n## Other Fragment Use Cases\n\nBeyond component-driven data fetching, fragments offer additional powerful patterns:\n\n- **Fragments on Unions and Interfaces**: Handle polymorphic types with inline fragments (`... on Type`)\n- **Batch Operations**: Share field selections between queries, mutations, and subscriptions\n- **Schema Documentation**: Use fragments as living documentation of data shapes\n- **Testing**: Create fragment mocks for isolated component testing\n- **Fragment Composition**: Build complex queries from simple, reusable pieces\n\nFor more advanced fragment patterns, see the [Vue Apollo Fragments documentation](https://apollo.vuejs.org/guide-composable/fragments).\n\n## Source Code\n\nFind the full demo for this series here: [example](https://github.com/alexanderop/vue-graphql-simple-example)\n\n**Note:** The code for this tutorial is on the `part3` branch.\n\n```bash\ngit clone https://github.com/alexanderop/vue-graphql-simple-example.git\ncd vue-graphql-simple-example\ngit checkout part3\n```&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PostCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus-outline inline-flex items-center gap-1.5 rounded-md border border-skin-line bg-skin-card px-2.5 py-1.5 text-xs font-medium text-skin-base opacity-80 transition-all hover:border-skin-accent/50 hover:text-skin-accent hover:opacity-100" aria-label="Copy post as markdown" title="Copy post as markdown for AI/LLM"><svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg><span>Copy Post</span></button><!--astro:end--></astro-island> </div> <nav class="mb-8 astro-sbmhws2g" aria-labelledby="series-heading"> <div class="mb-1 text-sm font-bold tracking-wide text-skin-accent astro-sbmhws2g"> Vue 3 + GraphQL Series </div> <h2 id="series-heading" class="mb-2 text-xs font-semibold uppercase tracking-widest text-skin-accent astro-sbmhws2g">
This post is part of a series
</h2> <ol class="space-y-2 astro-sbmhws2g">  <li class="relative flex flex-col rounded py-2 pl-4 transition-all   astro-sbmhws2g"> <div class="flex items-center gap-2 astro-sbmhws2g"> <span class="font-mono text-xs text-skin-base/60 astro-sbmhws2g"> 1.
</span> <a href="/posts/getting-started-graphql-vue3-apollo-typescript/" class="font-medium underline-offset-4 text-skin-accent/80 hover:underline astro-sbmhws2g"> Getting Started with GraphQL in Vue 3 — Complete Setup with Apollo </a>  </div> <div class="ml-6 mt-1 text-xs text-skin-base/70 astro-sbmhws2g"> Part 1 of the Vue 3 + GraphQL series: a zero-to-hero guide for wiring up a Vue 3 app to a GraphQL API using the Composition API, Apollo Client, and Vite. </div> </li><li class="relative flex flex-col rounded py-2 pl-4 transition-all   astro-sbmhws2g"> <div class="flex items-center gap-2 astro-sbmhws2g"> <span class="font-mono text-xs text-skin-base/60 astro-sbmhws2g"> 2.
</span> <a href="/posts/type-safe-graphql-queries-vue3-codegen/" class="font-medium underline-offset-4 text-skin-accent/80 hover:underline astro-sbmhws2g"> Type-Safe GraphQL Queries in Vue 3 with GraphQL Code Generator </a>  </div> <div class="ml-6 mt-1 text-xs text-skin-base/70 astro-sbmhws2g"> Part 2 of the Vue 3 + GraphQL series: generate fully-typed `useQuery` composables in Vue 3 with GraphQL Code Generator </div> </li><li class="relative flex flex-col rounded py-2 pl-4 transition-all border-l-4 border-skin-accent bg-skin-card/60  astro-sbmhws2g"> <div class="flex items-center gap-2 astro-sbmhws2g"> <span class="font-mono text-xs text-skin-accent astro-sbmhws2g"> 3.
</span> <a href="/posts/mastering-graphql-fragments-vue3-component-driven-data-fetching/" class="font-medium underline-offset-4 pointer-events-none text-skin-accent astro-sbmhws2g" aria-current="page"> Mastering GraphQL Fragments in Vue 3: Component-Driven Data Fetching </a> <span class="ml-2 text-xs font-bold text-green-400 astro-sbmhws2g">
(current)
</span> </div> <div class="ml-6 mt-1 text-xs text-skin-base/70 astro-sbmhws2g"> Part 3 of the Vue 3 + GraphQL series: Learn how to use GraphQL fragments with fragment masking to create truly component-driven data fetching in Vue 3. </div> </li>  </ol> <div class="mt-4 border-b border-skin-line opacity-40 astro-sbmhws2g"></div> </nav>  <article id="article" class="prose mx-auto mt-8 max-w-5xl astro-vj4tpspi"> <p><svg id="mermaid-0" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="flowchart" style="max-width:1519.578125px" viewBox="0 0 1519.578125 326" role="graphics-document document" aria-roledescription="flowchart-v2"><style>#mermaid-0{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-0 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-0 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-0 .error-icon{fill:#a44141;}#mermaid-0 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-0 .edge-thickness-normal{stroke-width:1px;}#mermaid-0 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-0 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-0 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-0 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-0 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-0 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-0 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-0 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-0 p{margin:0;}#mermaid-0 .label{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;color:#ccc;}#mermaid-0 .cluster-label text{fill:#F9FFFE;}#mermaid-0 .cluster-label span{color:#F9FFFE;}#mermaid-0 .cluster-label span p{background-color:transparent;}#mermaid-0 .label text,#mermaid-0 span{fill:#ccc;color:#ccc;}#mermaid-0 .node rect,#mermaid-0 .node circle,#mermaid-0 .node ellipse,#mermaid-0 .node polygon,#mermaid-0 .node path{fill:transparent;stroke:2px;stroke-width:1px;}#mermaid-0 .rough-node .label text,#mermaid-0 .node .label text,#mermaid-0 .image-shape .label,#mermaid-0 .icon-shape .label{text-anchor:middle;}#mermaid-0 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-0 .rough-node .label,#mermaid-0 .node .label,#mermaid-0 .image-shape .label,#mermaid-0 .icon-shape .label{text-align:center;}#mermaid-0 .node.clickable{cursor:pointer;}#mermaid-0 .root .anchor path{fill:rgb(171, 75, 153)!important;stroke-width:0;stroke:rgb(171, 75, 153);}#mermaid-0 .arrowheadPath{fill:lightgrey;}#mermaid-0 .edgePath .path{stroke:rgb(171, 75, 153);stroke-width:2.0px;}#mermaid-0 .flowchart-link{stroke:rgb(171, 75, 153);fill:none;}#mermaid-0 .edgeLabel{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-0 .edgeLabel p{background-color:hsla(0, 0%, 25%, 0);}#mermaid-0 .edgeLabel rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-0 .labelBkg{background-color:rgba(63.75, 63.75, 63.75, 0.5);}#mermaid-0 .cluster rect{fill:transparent;stroke:rgba(255, 255, 255, 0.25);stroke-width:1px;}#mermaid-0 .cluster text{fill:#F9FFFE;}#mermaid-0 .cluster span{color:#F9FFFE;}#mermaid-0 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:12px;background:rgb(138, 51, 123);border:1px solid rgba(255, 255, 255, 0.25);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-0 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-0 rect.text{fill:none;stroke-width:0;}#mermaid-0 .icon-shape,#mermaid-0 .image-shape{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-0 .icon-shape p,#mermaid-0 .image-shape p{background-color:hsla(0, 0%, 25%, 0);padding:2px;}#mermaid-0 .icon-shape rect,#mermaid-0 .image-shape rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-0 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-0 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-0 :root{--mermaid-font-family:arial,sans-serif;}</style><g><marker id="mermaid-0_flowchart-v2-pointEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-pointStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="4.5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 5 L 10 10 L 10 0 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-circleEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="11" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-0_flowchart-v2-circleStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="-1" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-0_flowchart-v2-crossEnd" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="12" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-crossStart" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="-1" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><g class="root"><g class="clusters"></g><g class="edgePaths"><path d="M340.664,86L340.664,90.167C340.664,94.333,340.664,102.667,340.664,110.333C340.664,118,340.664,125,340.664,128.5L340.664,132" id="L_A_A1_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_A_A1_0" data-points="W3sieCI6MzQwLjY2NDA2MjUsInkiOjg2fSx7IngiOjM0MC42NjQwNjI1LCJ5IjoxMTF9LHsieCI6MzQwLjY2NDA2MjUsInkiOjEzNn1d" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M223.969,188.279L203.41,192.733C182.852,197.186,141.734,206.093,121.176,216.047C100.617,226,100.617,237,100.617,242.5L100.617,248" id="L_A1_A2_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_A1_A2_0" data-points="W3sieCI6MjIzLjk2ODc1LCJ5IjoxODguMjc5MDQ3MDYxMTIwODh9LHsieCI6MTAwLjYxNzE4NzUsInkiOjIxNX0seyJ4IjoxMDAuNjE3MTg3NSwieSI6MjUyfV0=" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M340.664,190L340.664,194.167C340.664,198.333,340.664,206.667,340.664,216.333C340.664,226,340.664,237,340.664,242.5L340.664,248" id="L_A1_A3_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_A1_A3_0" data-points="W3sieCI6MzQwLjY2NDA2MjUsInkiOjE5MH0seyJ4IjozNDAuNjY0MDYyNSwieSI6MjE1fSx7IngiOjM0MC42NjQwNjI1LCJ5IjoyNTJ9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M457.359,184.873L484.148,189.894C510.938,194.915,564.516,204.958,591.305,213.479C618.094,222,618.094,229,618.094,232.5L618.094,236" id="L_A1_A4_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_A1_A4_0" data-points="W3sieCI6NDU3LjM1OTM3NSwieSI6MTg0Ljg3Mjc3MTgxNzE4MzR9LHsieCI6NjE4LjA5Mzc1LCJ5IjoyMTV9LHsieCI6NjE4LjA5Mzc1LCJ5IjoyNDB9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M1130.758,74L1130.758,80.167C1130.758,86.333,1130.758,98.667,1130.758,108.333C1130.758,118,1130.758,125,1130.758,128.5L1130.758,132" id="L_B_B1_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_B_B1_0" data-points="W3sieCI6MTEzMC43NTc4MTI1LCJ5Ijo3NH0seyJ4IjoxMTMwLjc1NzgxMjUsInkiOjExMX0seyJ4IjoxMTMwLjc1NzgxMjUsInkiOjEzNn1d" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M1004.43,189.31L983.871,193.592C963.313,197.873,922.195,206.437,901.637,216.218C881.078,226,881.078,237,881.078,242.5L881.078,248" id="L_B1_B2_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_B1_B2_0" data-points="W3sieCI6MTAwNC40Mjk2ODc1LCJ5IjoxODkuMzA5OTU5NjM1NzgzMzR9LHsieCI6ODgxLjA3ODEyNSwieSI6MjE1fSx7IngiOjg4MS4wNzgxMjUsInkiOjI1Mn1d" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M1130.758,190L1130.758,194.167C1130.758,198.333,1130.758,206.667,1130.758,216.333C1130.758,226,1130.758,237,1130.758,242.5L1130.758,248" id="L_B1_B3_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_B1_B3_0" data-points="W3sieCI6MTEzMC43NTc4MTI1LCJ5IjoxOTB9LHsieCI6MTEzMC43NTc4MTI1LCJ5IjoyMTV9LHsieCI6MTEzMC43NTc4MTI1LCJ5IjoyNTJ9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M1257.086,186.996L1281.658,191.663C1306.229,196.331,1355.372,205.665,1379.944,215.833C1404.516,226,1404.516,237,1404.516,242.5L1404.516,248" id="L_B1_B4_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_B1_B4_0" data-points="W3sieCI6MTI1Ny4wODU5Mzc1LCJ5IjoxODYuOTk1ODkwNTI4MjM4MzZ9LHsieCI6MTQwNC41MTU2MjUsInkiOjIxNX0seyJ4IjoxNDA0LjUxNTYyNSwieSI6MjUyfV0=" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path></g><g class="edgeLabels"><g class="edgeLabel"><g class="label" data-id="L_A_A1_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_A1_A2_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_A1_A3_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_A1_A4_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_B_B1_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_B1_B2_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_B1_B3_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_B1_B4_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g></g><g class="nodes"><g class="node default" id="flowchart-A-0" transform="translate(340.6640625, 47)"><rect class="basic label-container" style="" x="-130" y="-39" width="260" height="78"></rect><g class="label" style="" transform="translate(-100, -24)"><rect></rect><foreignObject width="200" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table;white-space:break-spaces;line-height:1.5;max-width:200px;text-align:center;width:200px"><span class="nodeLabel"><p>❌ Traditional Approach</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-A1-1" transform="translate(340.6640625, 163)"><rect class="basic label-container" style="" x="-116.6953125" y="-27" width="233.390625" height="54"></rect><g class="label" style="" transform="translate(-86.6953125, -12)"><rect></rect><foreignObject width="173.390625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Monolithic Queries</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-A2-3" transform="translate(100.6171875, 279)"><rect class="basic label-container" style="" x="-92.6171875" y="-27" width="185.234375" height="54"></rect><g class="label" style="" transform="translate(-62.6171875, -12)"><rect></rect><foreignObject width="125.234375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Over-fetching</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-A3-5" transform="translate(340.6640625, 279)"><rect class="basic label-container" style="" x="-97.4296875" y="-27" width="194.859375" height="54"></rect><g class="label" style="" transform="translate(-67.4296875, -12)"><rect></rect><foreignObject width="134.859375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Tight Coupling</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-A4-7" transform="translate(618.09375, 279)"><rect class="basic label-container" style="" x="-130" y="-39" width="260" height="78"></rect><g class="label" style="" transform="translate(-100, -24)"><rect></rect><foreignObject width="200" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table;white-space:break-spaces;line-height:1.5;max-width:200px;text-align:center;width:200px"><span class="nodeLabel"><p>Implicit Dependencies</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-B-8" transform="translate(1130.7578125, 47)"><rect class="basic label-container" style="" x="-116.6953125" y="-27" width="233.390625" height="54"></rect><g class="label" style="" transform="translate(-86.6953125, -12)"><rect></rect><foreignObject width="173.390625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>✅ Fragment Masking</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-B1-9" transform="translate(1130.7578125, 163)"><rect class="basic label-container" style="" x="-126.328125" y="-27" width="252.65625" height="54"></rect><g class="label" style="" transform="translate(-96.328125, -12)"><rect></rect><foreignObject width="192.65625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Component-Owned Data</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-B2-11" transform="translate(881.078125, 279)"><rect class="basic label-container" style="" x="-82.984375" y="-27" width="165.96875" height="54"></rect><g class="label" style="" transform="translate(-52.984375, -12)"><rect></rect><foreignObject width="105.96875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Type Safety</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-B3-13" transform="translate(1130.7578125, 279)"><rect class="basic label-container" style="" x="-116.6953125" y="-27" width="233.390625" height="54"></rect><g class="label" style="" transform="translate(-86.6953125, -12)"><rect></rect><foreignObject width="173.390625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Data Encapsulation</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-B4-15" transform="translate(1404.515625, 279)"><rect class="basic label-container" style="" x="-107.0625" y="-27" width="214.125" height="54"></rect><g class="label" style="" transform="translate(-77.0625, -12)"><rect></rect><foreignObject width="154.125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Safe Refactoring</p></span></div></foreignObject></g></g></g></g></g></svg></p>
<h2 id="why-fragments-are-a-game-changer">Why Fragments Are a Game-Changer<a class="heading-link" aria-label="Link to section" href="#why-fragments-are-a-game-changer"><span class="heading-link-icon">#</span></a></h2>
<p>In Part 2, we achieved type safety with GraphQL Code Generator. But our queries are still monolithic—each component doesn’t declare its own data needs. This creates several problems:</p>
<ul>
<li><strong>Over-fetching</strong>: Parent components request data their children might not need</li>
<li><strong>Under-fetching</strong>: Adding a field means hunting down every query using that type</li>
<li><strong>Tight coupling</strong>: Components depend on their parents to provide the right data</li>
<li><strong>Implicit dependencies</strong>: Parent components can accidentally rely on data from child fragments</li>
<li><strong>Brittle refactoring</strong>: Changing a component’s data needs can break unrelated components</li>
</ul>
<p>Enter GraphQL fragments with <strong>fragment masking</strong>—the pattern that Relay popularized and that Apollo Client 3.12 has made even more powerful. This transforms how we think about data fetching by providing <strong>true data encapsulation</strong> at the component level.</p>
<h2 id="what-are-graphql-fragments">What Are GraphQL Fragments?<a class="heading-link" aria-label="Link to section" href="#what-are-graphql-fragments"><span class="heading-link-icon">#</span></a></h2>
<p>GraphQL fragments are <strong>reusable units of fields</strong> that components can declare for themselves. But they’re more than just field groupings—when combined with fragment masking, they provide <strong>data access control</strong>.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="graphql"><code><span class="line"><span style="color:#BB9AF7">fragment</span><span style="color:#C0CAF5"> CountryBasicInfo</span><span style="color:#BB9AF7"> on</span><span style="color:#0DB9D7"> Country</span><span style="color:#89DDFF"> {</span></span>
<span class="line"><span style="color:#C0CAF5">  code</span></span>
<span class="line"><span style="color:#C0CAF5">  name</span></span>
<span class="line"><span style="color:#C0CAF5">  emoji</span></span>
<span class="line"><span style="color:#C0CAF5">  capital</span></span>
<span class="line"><span style="color:#89DDFF">}</span></span></code><button type="button" class="copy" data-code="fragment CountryBasicInfo on Country {
  code
  name
  emoji
  capital
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><strong>Fragment masking</strong> is the key innovation that makes fragments truly powerful. It ensures that:</p>
<ol>
<li><strong>Data is encapsulated</strong>: Only the component that defines a fragment can access its fields</li>
<li><strong>Dependencies are explicit</strong>: Components can’t accidentally rely on data from other fragments</li>
<li><strong>Refactoring is safe</strong>: Changing a fragment won’t break unrelated components</li>
<li><strong>Type safety is enforced</strong>: TypeScript prevents accessing fields you didn’t request</li>
</ol>
<h2 id="understanding-fragments-through-the-spread-operator">Understanding Fragments Through the Spread Operator<a class="heading-link" aria-label="Link to section" href="#understanding-fragments-through-the-spread-operator"><span class="heading-link-icon">#</span></a></h2>
<p>If you’re familiar with JavaScript’s spread operator, fragments work exactly the same way:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="javascript"><code><span class="line"><span style="color:#51597D;font-style:italic">// JavaScript objects</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> basicInfo</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span><span style="color:#73DACA"> code</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">US</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">United States</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> fullCountry</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span><span style="color:#F7768E;font-weight:bold"> ...</span><span style="color:#C0CAF5">basicInfo</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> capital</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">Washington D.C.</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="// JavaScript objects
const basicInfo = { code: &#34;US&#34;, name: &#34;United States&#34; };
const fullCountry = { ...basicInfo, capital: &#34;Washington D.C.&#34; };" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="graphql"><code><span class="line"><span style="color:#51597D;font-style:italic"># GraphQL fragments</span></span>
<span class="line"><span style="color:#BB9AF7">fragment</span><span style="color:#C0CAF5"> CountryBasicInfo</span><span style="color:#BB9AF7"> on</span><span style="color:#0DB9D7"> Country</span><span style="color:#89DDFF"> {</span></span>
<span class="line"><span style="color:#C0CAF5">  code</span></span>
<span class="line"><span style="color:#C0CAF5">  name</span></span>
<span class="line"><span style="color:#89DDFF">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">query</span><span style="color:#7AA2F7"> GetCountryDetails</span><span style="color:#89DDFF"> {</span></span>
<span class="line"><span style="color:#C0CAF5">  country</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">code</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">US</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF"> {</span></span>
<span class="line"><span style="color:#F7768E;font-weight:bold">    ...</span><span style="color:#C0CAF5">CountryBasicInfo</span><span style="color:#51597D;font-style:italic"> # Spread fragment fields</span></span>
<span class="line"><span style="color:#C0CAF5">    capital</span><span style="color:#51597D;font-style:italic"> # Add extra fields</span></span>
<span class="line"><span style="color:#89DDFF">  }</span></span>
<span class="line"><span style="color:#89DDFF">}</span></span></code><button type="button" class="copy" data-code="# GraphQL fragments
fragment CountryBasicInfo on Country {
  code
  name
}

query GetCountryDetails {
  country(code: &#34;US&#34;) {
    ...CountryBasicInfo # Spread fragment fields
    capital # Add extra fields
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><strong>Fragment masking</strong> takes this further by ensuring components can only access the data they explicitly request—pioneered by <strong>Relay</strong> and now enhanced in <strong>Apollo Client 3.12</strong>.</p>
<h2 id="step-1-enable-fragment-masking">Step 1: Enable Fragment Masking<a class="heading-link" aria-label="Link to section" href="#step-1-enable-fragment-masking"><span class="heading-link-icon">#</span></a></h2>
<p>Ensure your <code>codegen.ts</code> uses the client preset (from Part 2):</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> config</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> CodegenConfig</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  overwrite</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  schema</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">https://countries.trevorblades.com/graphql</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  documents</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">src/**/*.vue</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">src/**/*.graphql</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  generates</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">    &quot;</span><span style="color:#9ECE6A">src/gql/</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#41A6B5">      preset</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">client</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">      plugins</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> []</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">      config</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span><span style="color:#41A6B5"> useTypeImports</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="const config: CodegenConfig = {
  overwrite: true,
  schema: &#34;https://countries.trevorblades.com/graphql&#34;,
  documents: [&#34;src/**/*.vue&#34;, &#34;src/**/*.graphql&#34;],
  generates: {
    &#34;src/gql/&#34;: {
      preset: &#34;client&#34;,
      plugins: [],
      config: { useTypeImports: true },
    },
  },
};" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>This generates:</p>
<ul>
<li><code>FragmentType&lt;T&gt;</code>: Masked fragment types for props</li>
<li><code>useFragment()</code>: Function to unmask fragment data</li>
<li>Type safety to prevent accessing non-fragment fields</li>
</ul>
<h2 id="step-2-your-first-fragment-with-masking">Step 2: Your First Fragment with Masking<a class="heading-link" aria-label="Link to section" href="#step-2-your-first-fragment-with-masking"><span class="heading-link-icon">#</span></a></h2>
<p>Let’s create a <code>CountryCard</code> component that declares its own data requirements:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">script</span><span style="color:#BB9AF7"> setup</span><span style="color:#BB9AF7"> lang</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">ts</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">computed</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">graphql</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">../gql</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">FragmentType</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> useFragment</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">../gql/fragment-masking</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Define what data this component needs</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> CountryCard_CountryFragment</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> graphql</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">`</span></span>
<span class="line"><span style="color:#9ECE6A">  fragment CountryCard_CountryFragment on Country {</span></span>
<span class="line"><span style="color:#9ECE6A">    code</span></span>
<span class="line"><span style="color:#9ECE6A">    name</span></span>
<span class="line"><span style="color:#9ECE6A">    emoji</span></span>
<span class="line"><span style="color:#9ECE6A">    capital</span></span>
<span class="line"><span style="color:#9ECE6A">    phone</span></span>
<span class="line"><span style="color:#9ECE6A">    currency</span></span>
<span class="line"><span style="color:#9ECE6A">  }</span></span>
<span class="line"><span style="color:#89DDFF">`</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Props accept a masked fragment type</span></span>
<span class="line"><span style="color:#BB9AF7">interface</span><span style="color:#C0CAF5"> Props</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  country</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> FragmentType</span><span style="color:#89DDFF">&lt;typeof</span><span style="color:#C0CAF5"> CountryCard_CountryFragment</span><span style="color:#89DDFF">&gt;;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> props</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> defineProps</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Props</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Unmask to access the actual data (reactive for Vue)</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> country</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> computed</span><span style="color:#9ABDF5">(()</span><span style="color:#BB9AF7"> =&gt;</span></span>
<span class="line"><span style="color:#7AA2F7">  useFragment</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">CountryCard_CountryFragment</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> props</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">country</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">script</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">div</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">country-card</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">h3</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">{{ country.emoji }} {{ country.name }}</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">h3</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">p</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">Capital: {{ country.capital }}</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">p</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">p</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">Phone: +{{ country.phone }}</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">p</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">p</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">Currency: {{ country.currency }}</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">p</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<script setup lang=&#34;ts&#34;>
import { computed } from &#34;vue&#34;;
import { graphql } from &#34;../gql&#34;;
import { FragmentType, useFragment } from &#34;../gql/fragment-masking&#34;;

// Define what data this component needs
const CountryCard_CountryFragment = graphql(`
  fragment CountryCard_CountryFragment on Country {
    code
    name
    emoji
    capital
    phone
    currency
  }
`);

// Props accept a masked fragment type
interface Props {
  country: FragmentType<typeof CountryCard_CountryFragment>;
}

const props = defineProps<Props>();

// Unmask to access the actual data (reactive for Vue)
const country = computed(() =>
  useFragment(CountryCard_CountryFragment, props.country)
);
</script>

<template>
  <div class=&#34;country-card&#34;>
    <h3>{{ country.emoji }} {{ country.name }}</h3>
    <p>Capital: {{ country.capital }}</p>
    <p>Phone: +{{ country.phone }}</p>
    <p>Currency: {{ country.currency }}</p>
  </div>
</template>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h2 id="understanding-fragment-masking-the-key-to-data-isolation">Understanding Fragment Masking: The Key to Data Isolation<a class="heading-link" aria-label="Link to section" href="#understanding-fragment-masking-the-key-to-data-isolation"><span class="heading-link-icon">#</span></a></h2>
<p><strong>Fragment masking</strong> is the core concept that makes this pattern so powerful. It’s not just about code organization—it’s about <strong>data access control and encapsulation</strong>.</p>
<h3 id="what-fragment-masking-actually-does">What Fragment Masking Actually Does<a class="heading-link" aria-label="Link to section" href="#what-fragment-masking-actually-does"><span class="heading-link-icon">#</span></a></h3>
<p>Think of fragment masking like <strong>access control in programming languages</strong>. Just as a module can have private and public methods, fragment masking controls which components can access which pieces of data.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// Without fragment masking (traditional approach)</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> result</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> useQuery</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">GET_COUNTRIES</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> countries</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> result</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">value</span><span style="color:#89DDFF">?.</span><span style="color:#7DCFFF">countries</span><span style="color:#BB9AF7"> ||</span><span style="color:#9ABDF5"> []</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// ❌ Parent can access ANY field from the query</span></span>
<span class="line"><span style="color:#C0CAF5">console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">log</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">countries</span><span style="color:#9ABDF5">[</span><span style="color:#FF9E64">0</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">name</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span><span style="color:#51597D;font-style:italic"> // Works</span></span>
<span class="line"><span style="color:#C0CAF5">console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">log</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">countries</span><span style="color:#9ABDF5">[</span><span style="color:#FF9E64">0</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">capital</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span><span style="color:#51597D;font-style:italic"> // Works</span></span>
<span class="line"><span style="color:#C0CAF5">console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">log</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">countries</span><span style="color:#9ABDF5">[</span><span style="color:#FF9E64">0</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">currency</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span><span style="color:#51597D;font-style:italic"> // Works</span></span></code><button type="button" class="copy" data-code="// Without fragment masking (traditional approach)
const result = useQuery(GET_COUNTRIES);
const countries = result.value?.countries || [];

// ❌ Parent can access ANY field from the query
console.log(countries[0].name); // Works
console.log(countries[0].capital); // Works
console.log(countries[0].currency); // Works" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>With fragment masking enabled:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// ✅ Parent component CANNOT access fragment fields</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> name</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> result</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">value</span><span style="color:#89DDFF">?.</span><span style="color:#7DCFFF">countries</span><span style="color:#9ABDF5">[</span><span style="color:#FF9E64">0</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">name</span><span style="color:#89DDFF">;</span><span style="color:#51597D;font-style:italic"> // TypeScript error!</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// ✅ Only CountryCard can access its fragment data</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> country</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> useFragment</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">CountryCard_CountryFragment</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> props</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">country</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">log</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">country</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">name</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span><span style="color:#51597D;font-style:italic"> // Works!</span></span></code><button type="button" class="copy" data-code="// ✅ Parent component CANNOT access fragment fields
const name = result.value?.countries[0].name; // TypeScript error!

// ✅ Only CountryCard can access its fragment data
const country = useFragment(CountryCard_CountryFragment, props.country);
console.log(country.name); // Works!" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="the-power-of-data-encapsulation">The Power of Data Encapsulation<a class="heading-link" aria-label="Link to section" href="#the-power-of-data-encapsulation"><span class="heading-link-icon">#</span></a></h3>
<p>Fragment masking provides <strong>true data encapsulation</strong>:</p>
<ol>
<li><strong>Prevents Implicit Dependencies</strong>: Parent components can’t accidentally rely on data their children need</li>
<li><strong>Catches Breaking Changes Early</strong>: If a child component removes a field, the parent can’t access it anymore</li>
<li><strong>Enforces Component Boundaries</strong>: Each component owns its data requirements</li>
<li><strong>Enables Safe Refactoring</strong>: Change a fragment without breaking unrelated components</li>
</ol>
<h3 id="why-this-matters">Why This Matters<a class="heading-link" aria-label="Link to section" href="#why-this-matters"><span class="heading-link-icon">#</span></a></h3>
<p>Without fragment masking, parent components can accidentally depend on child fragment data. When the child removes a field, the parent breaks at runtime. With fragment masking, TypeScript catches this at compile time.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// Parent can only access explicitly requested fields</span></span>
<span class="line"><span style="color:#C0CAF5">countries</span><span style="color:#9ABDF5">[</span><span style="color:#FF9E64">0</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">id</span><span style="color:#89DDFF">;</span><span style="color:#51597D;font-style:italic"> // ✅ Works (parent requested this)</span></span>
<span class="line"><span style="color:#C0CAF5">countries</span><span style="color:#9ABDF5">[</span><span style="color:#FF9E64">0</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">name</span><span style="color:#89DDFF">;</span><span style="color:#51597D;font-style:italic"> // ❌ TypeScript error (only in fragment)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Child components unmask their fragment data</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> country</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> useFragment</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">CountryCard_CountryFragment</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> props</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">country</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">country</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">name</span><span style="color:#89DDFF">;</span><span style="color:#51597D;font-style:italic"> // ✅ Works (component owns this fragment)</span></span></code><button type="button" class="copy" data-code="// Parent can only access explicitly requested fields
countries[0].id; // ✅ Works (parent requested this)
countries[0].name; // ❌ TypeScript error (only in fragment)

// Child components unmask their fragment data
const country = useFragment(CountryCard_CountryFragment, props.country);
country.name; // ✅ Works (component owns this fragment)" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<blockquote>
<p><strong>📝 Vue Reactivity Note</strong>: Always wrap <code>useFragment</code> in a <code>computed()</code> for Vue reactivity. This ensures the component updates when fragment data changes.</p>
</blockquote>
<h2 id="step-3-parent-component-uses-the-fragment">Step 3: Parent Component Uses the Fragment<a class="heading-link" aria-label="Link to section" href="#step-3-parent-component-uses-the-fragment"><span class="heading-link-icon">#</span></a></h2>
<p>Now the parent component includes the child’s fragment in its query:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">script</span><span style="color:#BB9AF7"> setup</span><span style="color:#BB9AF7"> lang</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">ts</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">computed</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">useQuery</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">@vue/apollo-composable</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">graphql</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">../gql</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#0DB9D7"> CountryCard</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">./CountryCard.vue</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> COUNTRIES_WITH_DETAILS_QUERY</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> graphql</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">`</span></span>
<span class="line"><span style="color:#9ECE6A">  query CountriesWithDetails {</span></span>
<span class="line"><span style="color:#9ECE6A">    countries {</span></span>
<span class="line"><span style="color:#9ECE6A">      code</span></span>
<span class="line"><span style="color:#9ECE6A">      # Parent can add its own fields</span></span>
<span class="line"><span style="color:#9ECE6A">      region</span></span>
<span class="line"><span style="color:#9ECE6A">      # Child component&#39;s fragment</span></span>
<span class="line"><span style="color:#9ECE6A">      ...CountryCard_CountryFragment</span></span>
<span class="line"><span style="color:#9ECE6A">    }</span></span>
<span class="line"><span style="color:#9ECE6A">  }</span></span>
<span class="line"><span style="color:#89DDFF">`</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> result</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> loading</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> error</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> useQuery</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">COUNTRIES_WITH_DETAILS_QUERY</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Parent can access its own fields</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> countriesByRegion</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> computed</span><span style="color:#9ABDF5">(()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#C0CAF5">result</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">value</span><span style="color:#89DDFF">?.</span><span style="color:#7DCFFF">countries</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7;font-style:italic">return</span><span style="color:#9ABDF5"> {}</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#C0CAF5"> result</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">countries</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">reduce</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#9ABDF5">    (</span><span style="color:#E0AF68">acc</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> country</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">      const</span><span style="color:#BB9AF7"> region</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> country</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">region</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">      if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#C0CAF5">acc</span><span style="color:#9ABDF5">[</span><span style="color:#7DCFFF">region</span><span style="color:#9ABDF5">]) </span><span style="color:#C0CAF5">acc</span><span style="color:#9ABDF5">[</span><span style="color:#7DCFFF">region</span><span style="color:#9ABDF5">] </span><span style="color:#89DDFF">=</span><span style="color:#9ABDF5"> []</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">      acc</span><span style="color:#9ABDF5">[</span><span style="color:#7DCFFF">region</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">push</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">country</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">      return</span><span style="color:#C0CAF5"> acc</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    {} </span><span style="color:#89DDFF">as</span><span style="color:#C0CAF5"> Record</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">string</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> typeof</span><span style="color:#C0CAF5"> result</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">value</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">countries</span><span style="color:#89DDFF">&gt;</span></span>
<span class="line"><span style="color:#9ABDF5">  )</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">})</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// But parent CANNOT access fragment fields:</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">// const name = result.value?.countries[0].name ❌ TypeScript error!</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">script</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">div</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">countries-container</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">div</span><span style="color:#BB9AF7"> v-if</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">loading</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">Loading countries...</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">div</span><span style="color:#BB9AF7"> v-else-if</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">Error: {{ error.message }}</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">div</span><span style="color:#BB9AF7"> v-else</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">countries-by-region</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">      &lt;</span><span style="color:#F7768E">div</span></span>
<span class="line"><span style="color:#BB9AF7">        v-for</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">(countries, region) in countriesByRegion</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">        :key</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">region</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">        class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">region-section</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BA3C97">      &gt;</span></span>
<span class="line"><span style="color:#BA3C97">        &lt;</span><span style="color:#F7768E">h2</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">{{ region }}</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">h2</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">        &lt;</span><span style="color:#F7768E">div</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">country-grid</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">          &lt;</span><span style="color:#DE5971">CountryCard</span></span>
<span class="line"><span style="color:#BB9AF7">            v-for</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">country in countries</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">            :key</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">country.code</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">            :country</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">country</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BA3C97">          /&gt;</span></span>
<span class="line"><span style="color:#BA3C97">        &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">      &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<script setup lang=&#34;ts&#34;>
import { computed } from &#34;vue&#34;;
import { useQuery } from &#34;@vue/apollo-composable&#34;;
import { graphql } from &#34;../gql&#34;;
import CountryCard from &#34;./CountryCard.vue&#34;;

const COUNTRIES_WITH_DETAILS_QUERY = graphql(`
  query CountriesWithDetails {
    countries {
      code
      # Parent can add its own fields
      region
      # Child component's fragment
      ...CountryCard_CountryFragment
    }
  }
`);

const { result, loading, error } = useQuery(COUNTRIES_WITH_DETAILS_QUERY);

// Parent can access its own fields
const countriesByRegion = computed(() => {
  if (!result.value?.countries) return {};

  return result.value.countries.reduce(
    (acc, country) => {
      const region = country.region;
      if (!acc[region]) acc[region] = [];
      acc[region].push(country);
      return acc;
    },
    {} as Record<string, typeof result.value.countries>
  );
});

// But parent CANNOT access fragment fields:
// const name = result.value?.countries[0].name ❌ TypeScript error!
</script>

<template>
  <div class=&#34;countries-container&#34;>
    <div v-if=&#34;loading&#34;>Loading countries...</div>
    <div v-else-if=&#34;error&#34;>Error: {{ error.message }}</div>
    <div v-else class=&#34;countries-by-region&#34;>
      <div
        v-for=&#34;(countries, region) in countriesByRegion&#34;
        :key=&#34;region&#34;
        class=&#34;region-section&#34;
      >
        <h2>{{ region }}</h2>
        <div class=&#34;country-grid&#34;>
          <CountryCard
            v-for=&#34;country in countries&#34;
            :key=&#34;country.code&#34;
            :country=&#34;country&#34;
          />
        </div>
      </div>
    </div>
  </div>
</template>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h2 id="the-magic-of-fragment-masking">The Magic of Fragment Masking<a class="heading-link" aria-label="Link to section" href="#the-magic-of-fragment-masking"><span class="heading-link-icon">#</span></a></h2>
<p>Here’s what just happened:</p>
<p><svg id="mermaid-1" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="flowchart" style="max-width:688.65625px" viewBox="0 0 688.65625 595" role="graphics-document document" aria-roledescription="flowchart-v2"><style>#mermaid-1{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-1 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-1 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-1 .error-icon{fill:#a44141;}#mermaid-1 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-1 .edge-thickness-normal{stroke-width:1px;}#mermaid-1 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-1 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-1 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-1 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-1 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-1 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-1 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-1 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-1 p{margin:0;}#mermaid-1 .label{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;color:#ccc;}#mermaid-1 .cluster-label text{fill:#F9FFFE;}#mermaid-1 .cluster-label span{color:#F9FFFE;}#mermaid-1 .cluster-label span p{background-color:transparent;}#mermaid-1 .label text,#mermaid-1 span{fill:#ccc;color:#ccc;}#mermaid-1 .node rect,#mermaid-1 .node circle,#mermaid-1 .node ellipse,#mermaid-1 .node polygon,#mermaid-1 .node path{fill:transparent;stroke:2px;stroke-width:1px;}#mermaid-1 .rough-node .label text,#mermaid-1 .node .label text,#mermaid-1 .image-shape .label,#mermaid-1 .icon-shape .label{text-anchor:middle;}#mermaid-1 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-1 .rough-node .label,#mermaid-1 .node .label,#mermaid-1 .image-shape .label,#mermaid-1 .icon-shape .label{text-align:center;}#mermaid-1 .node.clickable{cursor:pointer;}#mermaid-1 .root .anchor path{fill:rgb(171, 75, 153)!important;stroke-width:0;stroke:rgb(171, 75, 153);}#mermaid-1 .arrowheadPath{fill:lightgrey;}#mermaid-1 .edgePath .path{stroke:rgb(171, 75, 153);stroke-width:2.0px;}#mermaid-1 .flowchart-link{stroke:rgb(171, 75, 153);fill:none;}#mermaid-1 .edgeLabel{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-1 .edgeLabel p{background-color:hsla(0, 0%, 25%, 0);}#mermaid-1 .edgeLabel rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-1 .labelBkg{background-color:rgba(63.75, 63.75, 63.75, 0.5);}#mermaid-1 .cluster rect{fill:transparent;stroke:rgba(255, 255, 255, 0.25);stroke-width:1px;}#mermaid-1 .cluster text{fill:#F9FFFE;}#mermaid-1 .cluster span{color:#F9FFFE;}#mermaid-1 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:12px;background:rgb(138, 51, 123);border:1px solid rgba(255, 255, 255, 0.25);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-1 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-1 rect.text{fill:none;stroke-width:0;}#mermaid-1 .icon-shape,#mermaid-1 .image-shape{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-1 .icon-shape p,#mermaid-1 .image-shape p{background-color:hsla(0, 0%, 25%, 0);padding:2px;}#mermaid-1 .icon-shape rect,#mermaid-1 .image-shape rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-1 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-1 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-1 :root{--mermaid-font-family:arial,sans-serif;}</style><g><marker id="mermaid-1_flowchart-v2-pointEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-1_flowchart-v2-pointStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="4.5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 5 L 10 10 L 10 0 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-1_flowchart-v2-circleEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="11" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-1_flowchart-v2-circleStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="-1" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-1_flowchart-v2-crossEnd" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="12" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-1_flowchart-v2-crossStart" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="-1" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><g class="root"><g class="clusters"><g class="cluster" id="subGraph2" data-look="classic"><rect style="" x="8" y="162" width="330" height="425"></rect><g class="cluster-label" transform="translate(100.75, 162)"><foreignObject width="144.5" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Child Component</p></span></div></foreignObject></g></g><g class="cluster" id="subGraph1" data-look="classic"><rect style="" x="358" y="162" width="322.65625" height="176"></rect><g class="cluster-label" transform="translate(442.265625, 162)"><foreignObject width="154.125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Parent Component</p></span></div></foreignObject></g></g><g class="cluster" id="subGraph0" data-look="classic"><rect style="" x="72.3359375" y="8" width="537.65625" height="104"></rect><g class="cluster-label" transform="translate(244.8359375, 8)"><foreignObject width="192.65625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>GraphQL Query Result</p></span></div></foreignObject></g></g></g><g class="edgePaths"><path d="M436.076,87L449.951,91.167C463.827,95.333,491.577,103.667,505.453,112C519.328,120.333,519.328,128.667,519.328,137C519.328,145.333,519.328,153.667,519.328,161.333C519.328,169,519.328,176,519.328,179.5L519.328,183" id="L_QR_PC_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_QR_PC_0" data-points="W3sieCI6NDM2LjA3NjE3MTg3NSwieSI6ODd9LHsieCI6NTE5LjMyODEyNSwieSI6MTEyfSx7IngiOjUxOS4zMjgxMjUsInkiOjEzN30seyJ4Ijo1MTkuMzI4MTI1LCJ5IjoxNjJ9LHsieCI6NTE5LjMyODEyNSwieSI6MTg3fV0=" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path><path d="M256.252,87L242.377,91.167C228.501,95.333,200.751,103.667,186.875,112C173,120.333,173,128.667,173,137C173,145.333,173,153.667,173,163.333C173,173,173,184,173,189.5L173,195" id="L_QR_CC_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_QR_CC_0" data-points="W3sieCI6MjU2LjI1MTk1MzEyNSwieSI6ODd9LHsieCI6MTczLCJ5IjoxMTJ9LHsieCI6MTczLCJ5IjoxMzd9LHsieCI6MTczLCJ5IjoxNjJ9LHsieCI6MTczLCJ5IjoxOTl9XQ==" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path><path d="M173,301L173,307.167C173,313.333,173,325.667,173,336C173,346.333,173,354.667,173,362.333C173,370,173,377,173,380.5L173,384" id="L_CC_UF_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_CC_UF_0" data-points="W3sieCI6MTczLCJ5IjozMDF9LHsieCI6MTczLCJ5IjozMzh9LHsieCI6MTczLCJ5IjozNjN9LHsieCI6MTczLCJ5IjozODh9XQ==" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path></g><g class="edgeLabels"><g class="edgeLabel"><g class="label" data-id="L_QR_PC_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_QR_CC_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_CC_UF_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g></g><g class="nodes"><g class="node default" id="flowchart-QR-0" transform="translate(346.1640625, 60)"><rect class="basic label-container" style="" x="-126.328125" y="-27" width="252.65625" height="54"></rect><g class="label" style="" transform="translate(-96.328125, -12)"><rect></rect><foreignObject width="192.65625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>countries: Country[]</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-PC-1" transform="translate(519.328125, 250)"><rect class="basic label-container" style="" x="-126.328125" y="-63" width="252.65625" height="126"></rect><g class="label" style="" transform="translate(-96.328125, -48)"><rect></rect><foreignObject width="192.65625" height="96"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Parent can access:<br/>• countries[].code<br/>• countries[].region<br/>❌ countries[].name</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-CC-2" transform="translate(173, 250)"><rect class="basic label-container" style="" x="-130" y="-51" width="260" height="102"></rect><g class="label" style="" transform="translate(-100, -36)"><rect></rect><foreignObject width="200" height="72"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table;white-space:break-spaces;line-height:1.5;max-width:200px;text-align:center;width:200px"><span class="nodeLabel"><p>CountryCard receives:<br/>Masked Fragment Data</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-UF-3" transform="translate(173, 475)"><rect class="basic label-container" style="" x="-130" y="-87" width="260" height="174"></rect><g class="label" style="" transform="translate(-100, -72)"><rect></rect><foreignObject width="200" height="144"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table;white-space:break-spaces;line-height:1.5;max-width:200px;text-align:center;width:200px"><span class="nodeLabel"><p>useFragment() unmasks:<br/>• code<br/>• name<br/>• emoji<br/>• capital</p></span></div></foreignObject></g></g></g></g></g></svg></p>
<p>The parent component <strong>cannot access</strong> fields from <code>CountryCard_Fragment</code>—they’re masked! Only <code>CountryCard</code> can unmask and use that data.</p>
<h2 id="step-4-nested-fragments">Step 4: Nested Fragments<a class="heading-link" aria-label="Link to section" href="#step-4-nested-fragments"><span class="heading-link-icon">#</span></a></h2>
<p>Fragments can include other fragments, creating a hierarchy:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="graphql"><code><span class="line"><span style="color:#51597D;font-style:italic"># Basic fragment</span></span>
<span class="line"><span style="color:#BB9AF7">fragment</span><span style="color:#C0CAF5"> LanguageItem_LanguageFragment</span><span style="color:#BB9AF7"> on</span><span style="color:#0DB9D7"> Language</span><span style="color:#89DDFF"> {</span></span>
<span class="line"><span style="color:#C0CAF5">  code</span></span>
<span class="line"><span style="color:#C0CAF5">  name</span></span>
<span class="line"><span style="color:#C0CAF5">  native</span></span>
<span class="line"><span style="color:#89DDFF">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic"># Fragment that uses other fragments</span></span>
<span class="line"><span style="color:#BB9AF7">fragment</span><span style="color:#C0CAF5"> CountryWithLanguages_CountryFragment</span><span style="color:#BB9AF7"> on</span><span style="color:#0DB9D7"> Country</span><span style="color:#89DDFF"> {</span></span>
<span class="line"><span style="color:#C0CAF5">  code</span></span>
<span class="line"><span style="color:#C0CAF5">  name</span></span>
<span class="line"><span style="color:#C0CAF5">  emoji</span></span>
<span class="line"><span style="color:#C0CAF5">  languages</span><span style="color:#89DDFF"> {</span></span>
<span class="line"><span style="color:#F7768E;font-weight:bold">    ...</span><span style="color:#C0CAF5">LanguageItem_LanguageFragment</span></span>
<span class="line"><span style="color:#89DDFF">  }</span></span>
<span class="line"><span style="color:#89DDFF">}</span></span></code><button type="button" class="copy" data-code="# Basic fragment
fragment LanguageItem_LanguageFragment on Language {
  code
  name
  native
}

# Fragment that uses other fragments
fragment CountryWithLanguages_CountryFragment on Country {
  code
  name
  emoji
  languages {
    ...LanguageItem_LanguageFragment
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>Child components use their own fragments:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#51597D;font-style:italic">&lt;!-- LanguageItem.vue --&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">script</span><span style="color:#BB9AF7"> setup</span><span style="color:#BB9AF7"> lang</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">ts</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">computed</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">graphql</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> FragmentType</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> useFragment</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">../gql</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> LanguageItem_LanguageFragment</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> graphql</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">`</span></span>
<span class="line"><span style="color:#9ECE6A">  fragment LanguageItem_LanguageFragment on Language {</span></span>
<span class="line"><span style="color:#9ECE6A">    code</span></span>
<span class="line"><span style="color:#9ECE6A">    name</span></span>
<span class="line"><span style="color:#9ECE6A">    native</span></span>
<span class="line"><span style="color:#9ECE6A">  }</span></span>
<span class="line"><span style="color:#89DDFF">`</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">interface</span><span style="color:#C0CAF5"> Props</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  language</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> FragmentType</span><span style="color:#89DDFF">&lt;typeof</span><span style="color:#C0CAF5"> LanguageItem_LanguageFragment</span><span style="color:#89DDFF">&gt;;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> props</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> defineProps</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Props</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> language</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> computed</span><span style="color:#9ABDF5">(()</span><span style="color:#BB9AF7"> =&gt;</span></span>
<span class="line"><span style="color:#7AA2F7">  useFragment</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">LanguageItem_LanguageFragment</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> props</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">language</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">script</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">div</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">language-item</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">span</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">{{ language.name }} ({{ language.code }})</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">span</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<!-- LanguageItem.vue -->
<script setup lang=&#34;ts&#34;>
import { computed } from &#34;vue&#34;;
import { graphql, FragmentType, useFragment } from &#34;../gql&#34;;

const LanguageItem_LanguageFragment = graphql(`
  fragment LanguageItem_LanguageFragment on Language {
    code
    name
    native
  }
`);

interface Props {
  language: FragmentType<typeof LanguageItem_LanguageFragment>;
}

const props = defineProps<Props>();
const language = computed(() =>
  useFragment(LanguageItem_LanguageFragment, props.language)
);
</script>

<template>
  <div class=&#34;language-item&#34;>
    <span>{{ language.name }} ({{ language.code }})</span>
  </div>
</template>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h2 id="fragment-dependency-management">Fragment Dependency Management<a class="heading-link" aria-label="Link to section" href="#fragment-dependency-management"><span class="heading-link-icon">#</span></a></h2>
<p>Notice how the query automatically includes all nested fragments:</p>
<p><svg id="mermaid-2" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="flowchart" style="max-width:690.578125px" viewBox="0 0 690.578125 444" role="graphics-document document" aria-roledescription="flowchart-v2"><style>#mermaid-2{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-2 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-2 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-2 .error-icon{fill:#a44141;}#mermaid-2 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-2 .edge-thickness-normal{stroke-width:1px;}#mermaid-2 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-2 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-2 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-2 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-2 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-2 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-2 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-2 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-2 p{margin:0;}#mermaid-2 .label{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;color:#ccc;}#mermaid-2 .cluster-label text{fill:#F9FFFE;}#mermaid-2 .cluster-label span{color:#F9FFFE;}#mermaid-2 .cluster-label span p{background-color:transparent;}#mermaid-2 .label text,#mermaid-2 span{fill:#ccc;color:#ccc;}#mermaid-2 .node rect,#mermaid-2 .node circle,#mermaid-2 .node ellipse,#mermaid-2 .node polygon,#mermaid-2 .node path{fill:transparent;stroke:2px;stroke-width:1px;}#mermaid-2 .rough-node .label text,#mermaid-2 .node .label text,#mermaid-2 .image-shape .label,#mermaid-2 .icon-shape .label{text-anchor:middle;}#mermaid-2 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-2 .rough-node .label,#mermaid-2 .node .label,#mermaid-2 .image-shape .label,#mermaid-2 .icon-shape .label{text-align:center;}#mermaid-2 .node.clickable{cursor:pointer;}#mermaid-2 .root .anchor path{fill:rgb(171, 75, 153)!important;stroke-width:0;stroke:rgb(171, 75, 153);}#mermaid-2 .arrowheadPath{fill:lightgrey;}#mermaid-2 .edgePath .path{stroke:rgb(171, 75, 153);stroke-width:2.0px;}#mermaid-2 .flowchart-link{stroke:rgb(171, 75, 153);fill:none;}#mermaid-2 .edgeLabel{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-2 .edgeLabel p{background-color:hsla(0, 0%, 25%, 0);}#mermaid-2 .edgeLabel rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-2 .labelBkg{background-color:rgba(63.75, 63.75, 63.75, 0.5);}#mermaid-2 .cluster rect{fill:transparent;stroke:rgba(255, 255, 255, 0.25);stroke-width:1px;}#mermaid-2 .cluster text{fill:#F9FFFE;}#mermaid-2 .cluster span{color:#F9FFFE;}#mermaid-2 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:12px;background:rgb(138, 51, 123);border:1px solid rgba(255, 255, 255, 0.25);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-2 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-2 rect.text{fill:none;stroke-width:0;}#mermaid-2 .icon-shape,#mermaid-2 .image-shape{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-2 .icon-shape p,#mermaid-2 .image-shape p{background-color:hsla(0, 0%, 25%, 0);padding:2px;}#mermaid-2 .icon-shape rect,#mermaid-2 .image-shape rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-2 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-2 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-2 :root{--mermaid-font-family:arial,sans-serif;}</style><g><marker id="mermaid-2_flowchart-v2-pointEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-2_flowchart-v2-pointStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="4.5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 5 L 10 10 L 10 0 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-2_flowchart-v2-circleEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="11" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-2_flowchart-v2-circleStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="-1" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-2_flowchart-v2-crossEnd" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="12" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-2_flowchart-v2-crossStart" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="-1" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><g class="root"><g class="clusters"><g class="cluster" id="subGraph1" data-look="classic"><rect style="" x="399.1875" y="8" width="283.390625" height="428"></rect><g class="cluster-label" transform="translate(468.6328125, 8)"><foreignObject width="144.5" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Their Fragments</p></span></div></foreignObject></g></g><g class="cluster" id="Components" data-look="classic"><rect style="" x="8" y="20" width="341.1875" height="404"></rect><g class="cluster-label" transform="translate(130.4296875, 20)"><foreignObject width="96.328125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Components</p></span></div></foreignObject></g></g></g><g class="edgePaths"><path d="M290.477,82L300.262,82C310.047,82,329.617,82,343.569,82C357.521,82,365.854,82,374.188,82C382.521,82,390.854,82,403.337,82C415.82,82,432.453,82,440.77,82L449.086,82" id="L_A_A1_0" class="edge-thickness-normal edge-pattern-dotted edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_A_A1_0" data-points="W3sieCI6MjkwLjQ3NjU2MjUsInkiOjgyfSx7IngiOjM0OS4xODc1LCJ5Ijo4Mn0seyJ4IjozNzQuMTg3NSwieSI6ODJ9LHsieCI6Mzk5LjE4NzUsInkiOjgyfSx7IngiOjQ1My4wODU5Mzc1LCJ5Ijo4Mn1d" marker-end="url(#mermaid-2_flowchart-v2-pointEnd)"></path><path d="M324.188,222L328.354,222C332.521,222,340.854,222,349.188,222C357.521,222,365.854,222,374.188,222C382.521,222,390.854,222,399.323,222C407.792,222,416.396,222,420.698,222L425,222" id="L_B_B1_0" class="edge-thickness-normal edge-pattern-dotted edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_B_B1_0" data-points="W3sieCI6MzI0LjE4NzUsInkiOjIyMn0seyJ4IjozNDkuMTg3NSwieSI6MjIyfSx7IngiOjM3NC4xODc1LCJ5IjoyMjJ9LHsieCI6Mzk5LjE4NzUsInkiOjIyMn0seyJ4Ijo0MjksInkiOjIyMn1d" marker-end="url(#mermaid-2_flowchart-v2-pointEnd)"></path><path d="M285.656,362L296.245,362C306.833,362,328.01,362,342.766,362C357.521,362,365.854,362,374.188,362C382.521,362,390.854,362,398.521,362C406.188,362,413.188,362,416.688,362L420.188,362" id="L_C_C1_0" class="edge-thickness-normal edge-pattern-dotted edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_C_C1_0" data-points="W3sieCI6Mjg1LjY1NjI1LCJ5IjozNjJ9LHsieCI6MzQ5LjE4NzUsInkiOjM2Mn0seyJ4IjozNzQuMTg3NSwieSI6MzYyfSx7IngiOjM5OS4xODc1LCJ5IjozNjJ9LHsieCI6NDI0LjE4NzUsInkiOjM2Mn1d" marker-end="url(#mermaid-2_flowchart-v2-pointEnd)"></path></g><g class="edgeLabels"><g class="edgeLabel"><g class="label" data-id="L_A_A1_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_B_B1_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_C_C1_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g></g><g class="nodes"><g class="node default" id="flowchart-A-0" transform="translate(178.59375, 82)"><rect class="basic label-container" style="" x="-111.8828125" y="-27" width="223.765625" height="54"></rect><g class="label" style="" transform="translate(-81.8828125, -12)"><rect></rect><foreignObject width="163.765625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>CountryDetailPage</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-B-1" transform="translate(178.59375, 222)"><rect class="basic label-container" style="" x="-145.59375" y="-27" width="291.1875" height="54"></rect><g class="label" style="" transform="translate(-115.59375, -12)"><rect></rect><foreignObject width="231.1875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table;white-space:break-spaces;line-height:1.5;max-width:200px;text-align:center;width:200px"><span class="nodeLabel"><p>CountryWithLanguages.vue</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-C-2" transform="translate(178.59375, 362)"><rect class="basic label-container" style="" x="-107.0625" y="-27" width="214.125" height="54"></rect><g class="label" style="" transform="translate(-77.0625, -12)"><rect></rect><foreignObject width="154.125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>LanguageItem.vue</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-A1-3" transform="translate(540.8828125, 82)"><rect class="basic label-container" style="" x="-87.796875" y="-39" width="175.59375" height="78"></rect><g class="label" style="" transform="translate(-57.796875, -24)"><rect></rect><foreignObject width="115.59375" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Page Fields:<br/>code</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-B1-4" transform="translate(540.8828125, 222)"><rect class="basic label-container" style="" x="-111.8828125" y="-51" width="223.765625" height="102"></rect><g class="label" style="" transform="translate(-81.8828125, -36)"><rect></rect><foreignObject width="163.765625" height="72"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Country Fragment:<br/>code, name, emoji<br/>languages</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-C1-5" transform="translate(540.8828125, 362)"><rect class="basic label-container" style="" x="-116.6953125" y="-39" width="233.390625" height="78"></rect><g class="label" style="" transform="translate(-86.6953125, -24)"><rect></rect><foreignObject width="173.390625" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Language Fragment:<br/>code, name, native</p></span></div></foreignObject></g></g></g></g></g></svg></p>
<h2 id="step-5-conditional-fragments">Step 5: Conditional Fragments<a class="heading-link" aria-label="Link to section" href="#step-5-conditional-fragments"><span class="heading-link-icon">#</span></a></h2>
<p>Use GraphQL directives to conditionally include fragments:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="graphql"><code><span class="line"><span style="color:#BB9AF7">query</span><span style="color:#7AA2F7"> CountriesConditional</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">$includeLanguages</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> Boolean</span><span style="color:#89DDFF">!</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF"> {</span></span>
<span class="line"><span style="color:#C0CAF5">  countries</span><span style="color:#89DDFF"> {</span></span>
<span class="line"><span style="color:#C0CAF5">    code</span></span>
<span class="line"><span style="color:#C0CAF5">    name</span></span>
<span class="line"><span style="color:#F7768E;font-weight:bold">    ...</span><span style="color:#C0CAF5">CountryDetails_CountryFragment</span><span style="color:#7AA2F7"> @include</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">if</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> $includeLanguages</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#89DDFF">  }</span></span>
<span class="line"><span style="color:#89DDFF">}</span></span></code><button type="button" class="copy" data-code="query CountriesConditional($includeLanguages: Boolean!) {
  countries {
    code
    name
    ...CountryDetails_CountryFragment @include(if: $includeLanguages)
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>This enables dynamic data loading based on user interactions or application state.</p>
<h2 id="best-practices">Best Practices<a class="heading-link" aria-label="Link to section" href="#best-practices"><span class="heading-link-icon">#</span></a></h2>
<h3 id="key-guidelines">Key Guidelines<a class="heading-link" aria-label="Link to section" href="#key-guidelines"><span class="heading-link-icon">#</span></a></h3>
<ol>
<li><strong>Naming</strong>: Use <code>ComponentName_TypeNameFragment</code> convention</li>
<li><strong>Vue Reactivity</strong>: Always wrap <code>useFragment</code> in <code>computed()</code></li>
<li><strong>TypeScript</strong>: Use <code>FragmentType&lt;typeof MyFragment&gt;</code> for props</li>
<li><strong>Organization</strong>: Colocate fragments with components</li>
</ol>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// ✅ Good naming and Vue reactivity</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> CountryCard_CountryFragment</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> graphql</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">`</span><span style="color:#9ECE6A">...</span><span style="color:#89DDFF">`</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">interface</span><span style="color:#C0CAF5"> Props</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  country</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> FragmentType</span><span style="color:#89DDFF">&lt;typeof</span><span style="color:#C0CAF5"> CountryCard_CountryFragment</span><span style="color:#89DDFF">&gt;;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> country</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> computed</span><span style="color:#9ABDF5">(()</span><span style="color:#BB9AF7"> =&gt;</span></span>
<span class="line"><span style="color:#7AA2F7">  useFragment</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">CountryCard_CountryFragment</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> props</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">country</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="// ✅ Good naming and Vue reactivity
const CountryCard_CountryFragment = graphql(`...`);

interface Props {
  country: FragmentType<typeof CountryCard_CountryFragment>;
}

const country = computed(() =>
  useFragment(CountryCard_CountryFragment, props.country)
);" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h2 id="performance-benefits">Performance Benefits<a class="heading-link" aria-label="Link to section" href="#performance-benefits"><span class="heading-link-icon">#</span></a></h2>
<p>Fragments aren’t just about developer experience - they provide concrete performance and maintainability benefits:</p>
<p><svg id="mermaid-3" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="flowchart" style="max-width:572.6953125px" viewBox="0 0 572.6953125 454" role="graphics-document document" aria-roledescription="flowchart-v2"><style>#mermaid-3{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-3 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-3 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-3 .error-icon{fill:#a44141;}#mermaid-3 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-3 .edge-thickness-normal{stroke-width:1px;}#mermaid-3 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-3 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-3 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-3 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-3 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-3 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-3 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-3 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-3 p{margin:0;}#mermaid-3 .label{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;color:#ccc;}#mermaid-3 .cluster-label text{fill:#F9FFFE;}#mermaid-3 .cluster-label span{color:#F9FFFE;}#mermaid-3 .cluster-label span p{background-color:transparent;}#mermaid-3 .label text,#mermaid-3 span{fill:#ccc;color:#ccc;}#mermaid-3 .node rect,#mermaid-3 .node circle,#mermaid-3 .node ellipse,#mermaid-3 .node polygon,#mermaid-3 .node path{fill:transparent;stroke:2px;stroke-width:1px;}#mermaid-3 .rough-node .label text,#mermaid-3 .node .label text,#mermaid-3 .image-shape .label,#mermaid-3 .icon-shape .label{text-anchor:middle;}#mermaid-3 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-3 .rough-node .label,#mermaid-3 .node .label,#mermaid-3 .image-shape .label,#mermaid-3 .icon-shape .label{text-align:center;}#mermaid-3 .node.clickable{cursor:pointer;}#mermaid-3 .root .anchor path{fill:rgb(171, 75, 153)!important;stroke-width:0;stroke:rgb(171, 75, 153);}#mermaid-3 .arrowheadPath{fill:lightgrey;}#mermaid-3 .edgePath .path{stroke:rgb(171, 75, 153);stroke-width:2.0px;}#mermaid-3 .flowchart-link{stroke:rgb(171, 75, 153);fill:none;}#mermaid-3 .edgeLabel{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-3 .edgeLabel p{background-color:hsla(0, 0%, 25%, 0);}#mermaid-3 .edgeLabel rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-3 .labelBkg{background-color:rgba(63.75, 63.75, 63.75, 0.5);}#mermaid-3 .cluster rect{fill:transparent;stroke:rgba(255, 255, 255, 0.25);stroke-width:1px;}#mermaid-3 .cluster text{fill:#F9FFFE;}#mermaid-3 .cluster span{color:#F9FFFE;}#mermaid-3 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:12px;background:rgb(138, 51, 123);border:1px solid rgba(255, 255, 255, 0.25);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-3 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-3 rect.text{fill:none;stroke-width:0;}#mermaid-3 .icon-shape,#mermaid-3 .image-shape{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-3 .icon-shape p,#mermaid-3 .image-shape p{background-color:hsla(0, 0%, 25%, 0);padding:2px;}#mermaid-3 .icon-shape rect,#mermaid-3 .image-shape rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-3 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-3 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-3 :root{--mermaid-font-family:arial,sans-serif;}</style><g><marker id="mermaid-3_flowchart-v2-pointEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-3_flowchart-v2-pointStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="4.5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 5 L 10 10 L 10 0 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-3_flowchart-v2-circleEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="11" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-3_flowchart-v2-circleStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="-1" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-3_flowchart-v2-crossEnd" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="12" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-3_flowchart-v2-crossStart" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="-1" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><g class="root"><g class="clusters"></g><g class="edgePaths"><path d="M138,74L138,80.167C138,86.333,138,98.667,138,110.333C138,122,138,133,138,138.5L138,144" id="L_A_A1_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_A_A1_0" data-points="W3sieCI6MTM4LCJ5Ijo3NH0seyJ4IjoxMzgsInkiOjExMX0seyJ4IjoxMzgsInkiOjE0OH1d" marker-end="url(#mermaid-3_flowchart-v2-pointEnd)"></path><path d="M138,202L138,208.167C138,214.333,138,226.667,138,236.333C138,246,138,253,138,256.5L138,260" id="L_A1_A2_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_A1_A2_0" data-points="W3sieCI6MTM4LCJ5IjoyMDJ9LHsieCI6MTM4LCJ5IjoyMzl9LHsieCI6MTM4LCJ5IjoyNjR9XQ==" marker-end="url(#mermaid-3_flowchart-v2-pointEnd)"></path><path d="M138,342L138,346.167C138,350.333,138,358.667,138,366.333C138,374,138,381,138,384.5L138,388" id="L_A2_A3_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_A2_A3_0" data-points="W3sieCI6MTM4LCJ5IjozNDJ9LHsieCI6MTM4LCJ5IjozNjd9LHsieCI6MTM4LCJ5IjozOTJ9XQ==" marker-end="url(#mermaid-3_flowchart-v2-pointEnd)"></path><path d="M434.695,86L434.695,90.167C434.695,94.333,434.695,102.667,434.695,110.333C434.695,118,434.695,125,434.695,128.5L434.695,132" id="L_B_B1_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_B_B1_0" data-points="W3sieCI6NDM0LjY5NTMxMjUsInkiOjg2fSx7IngiOjQzNC42OTUzMTI1LCJ5IjoxMTF9LHsieCI6NDM0LjY5NTMxMjUsInkiOjEzNn1d" marker-end="url(#mermaid-3_flowchart-v2-pointEnd)"></path><path d="M434.695,214L434.695,218.167C434.695,222.333,434.695,230.667,434.695,240.333C434.695,250,434.695,261,434.695,266.5L434.695,272" id="L_B1_B2_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_B1_B2_0" data-points="W3sieCI6NDM0LjY5NTMxMjUsInkiOjIxNH0seyJ4Ijo0MzQuNjk1MzEyNSwieSI6MjM5fSx7IngiOjQzNC42OTUzMTI1LCJ5IjoyNzZ9XQ==" marker-end="url(#mermaid-3_flowchart-v2-pointEnd)"></path><path d="M434.695,330L434.695,336.167C434.695,342.333,434.695,354.667,434.695,364.333C434.695,374,434.695,381,434.695,384.5L434.695,388" id="L_B2_B3_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_B2_B3_0" data-points="W3sieCI6NDM0LjY5NTMxMjUsInkiOjMzMH0seyJ4Ijo0MzQuNjk1MzEyNSwieSI6MzY3fSx7IngiOjQzNC42OTUzMTI1LCJ5IjozOTJ9XQ==" marker-end="url(#mermaid-3_flowchart-v2-pointEnd)"></path></g><g class="edgeLabels"><g class="edgeLabel"><g class="label" data-id="L_A_A1_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_A1_A2_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_A2_A3_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_B_B1_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_B1_B2_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_B2_B3_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g></g><g class="nodes"><g class="node default" id="flowchart-A-0" transform="translate(138, 47)"><rect class="basic label-container" style="" x="-116.6953125" y="-27" width="233.390625" height="54"></rect><g class="label" style="" transform="translate(-86.6953125, -12)"><rect></rect><foreignObject width="173.390625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>❌ Multiple Queries</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-A1-1" transform="translate(138, 175)"><rect class="basic label-container" style="" x="-116.6953125" y="-27" width="233.390625" height="54"></rect><g class="label" style="" transform="translate(-86.6953125, -12)"><rect></rect><foreignObject width="173.390625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>3 Network Requests</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-A2-3" transform="translate(138, 303)"><rect class="basic label-container" style="" x="-130" y="-39" width="260" height="78"></rect><g class="label" style="" transform="translate(-100, -24)"><rect></rect><foreignObject width="200" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table;white-space:break-spaces;line-height:1.5;max-width:200px;text-align:center;width:200px"><span class="nodeLabel"><p>Duplicate Data Fetching</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-A3-5" transform="translate(138, 419)"><rect class="basic label-container" style="" x="-116.6953125" y="-27" width="233.390625" height="54"></rect><g class="label" style="" transform="translate(-86.6953125, -12)"><rect></rect><foreignObject width="173.390625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Larger Bundle Size</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-B-6" transform="translate(434.6953125, 47)"><rect class="basic label-container" style="" x="-130" y="-39" width="260" height="78"></rect><g class="label" style="" transform="translate(-100, -24)"><rect></rect><foreignObject width="200" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table;white-space:break-spaces;line-height:1.5;max-width:200px;text-align:center;width:200px"><span class="nodeLabel"><p>✅ Fragment Composition</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-B1-7" transform="translate(434.6953125, 175)"><rect class="basic label-container" style="" x="-130" y="-39" width="260" height="78"></rect><g class="label" style="" transform="translate(-100, -24)"><rect></rect><foreignObject width="200" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table;white-space:break-spaces;line-height:1.5;max-width:200px;text-align:center;width:200px"><span class="nodeLabel"><p>Single Network Request</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-B2-9" transform="translate(434.6953125, 303)"><rect class="basic label-container" style="" x="-111.8828125" y="-27" width="223.765625" height="54"></rect><g class="label" style="" transform="translate(-81.8828125, -12)"><rect></rect><foreignObject width="163.765625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Optimized Payload</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-B3-11" transform="translate(434.6953125, 419)"><rect class="basic label-container" style="" x="-116.6953125" y="-27" width="233.390625" height="54"></rect><g class="label" style="" transform="translate(-86.6953125, -12)"><rect></rect><foreignObject width="173.390625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Better Performance</p></span></div></foreignObject></g></g></g></g></g></svg></p>
<h2 id="summary">Summary<a class="heading-link" aria-label="Link to section" href="#summary"><span class="heading-link-icon">#</span></a></h2>
<p>GraphQL fragments with fragment masking enable <strong>component-driven data fetching</strong> in Vue 3:</p>
<p>✅ <strong>Type Safety</strong>: Components can only access their declared fields
✅ <strong>True Modularity</strong>: Each component declares its exact data needs<br/>
✅ <strong>Better Performance</strong>: Load only the data you need
✅ <strong>Maintainable Code</strong>: Changes to fragments don’t break unrelated components</p>
<h2 id="migration-checklist">Migration Checklist<a class="heading-link" aria-label="Link to section" href="#migration-checklist"><span class="heading-link-icon">#</span></a></h2>
<ol>
<li>Start with leaf components (no children)</li>
<li>Always use <code>computed()</code> with <code>useFragment</code> for Vue reactivity</li>
<li>Update TypeScript interfaces to use <code>FragmentType</code></li>
<li>Run <code>npm run codegen</code> after fragment changes</li>
</ol>
<h2 id="whats-next">What’s Next?<a class="heading-link" aria-label="Link to section" href="#whats-next"><span class="heading-link-icon">#</span></a></h2>
<p>This is Part 3 of our Vue 3 + GraphQL series:</p>
<ol>
<li><strong>Part 1</strong>: Setting up Apollo Client with Vue 3</li>
<li><strong>Part 2</strong>: Type-safe queries with GraphQL Code Generator</li>
<li><strong>Part 3</strong>: Advanced fragments and component-driven data fetching (current)</li>
<li><strong>Part 4</strong>: GraphQL Caching Strategies in Vue 3 (coming next!)</li>
</ol>
<h2 id="other-fragment-use-cases">Other Fragment Use Cases<a class="heading-link" aria-label="Link to section" href="#other-fragment-use-cases"><span class="heading-link-icon">#</span></a></h2>
<p>Beyond component-driven data fetching, fragments offer additional powerful patterns:</p>
<ul>
<li><strong>Fragments on Unions and Interfaces</strong>: Handle polymorphic types with inline fragments (<code>... on Type</code>)</li>
<li><strong>Batch Operations</strong>: Share field selections between queries, mutations, and subscriptions</li>
<li><strong>Schema Documentation</strong>: Use fragments as living documentation of data shapes</li>
<li><strong>Testing</strong>: Create fragment mocks for isolated component testing</li>
<li><strong>Fragment Composition</strong>: Build complex queries from simple, reusable pieces</li>
</ul>
<p>For more advanced fragment patterns, see the <a href="https://apollo.vuejs.org/guide-composable/fragments" rel="noopener noreferrer" target="_blank">Vue Apollo Fragments documentation</a>.</p>
<h2 id="source-code">Source Code<a class="heading-link" aria-label="Link to section" href="#source-code"><span class="heading-link-icon">#</span></a></h2>
<p>Find the full demo for this series here: <a href="https://github.com/alexanderop/vue-graphql-simple-example" rel="noopener noreferrer" target="_blank">example</a></p>
<p><strong>Note:</strong> The code for this tutorial is on the <code>part3</code> branch.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#C0CAF5">git</span><span style="color:#9ECE6A"> clone</span><span style="color:#9ECE6A"> https://github.com/alexanderop/vue-graphql-simple-example.git</span></span>
<span class="line"><span style="color:#0DB9D7">cd</span><span style="color:#9ECE6A"> vue-graphql-simple-example</span></span>
<span class="line"><span style="color:#C0CAF5">git</span><span style="color:#9ECE6A"> checkout</span><span style="color:#9ECE6A"> part3</span></span></code><button type="button" class="copy" data-code="git clone https://github.com/alexanderop/vue-graphql-simple-example.git
cd vue-graphql-simple-example
git checkout part3" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </article> <script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).only=e;window.dispatchEvent(new Event("astro:only"));})();</script><astro-island uid="Z1XneyL" component-url="/_astro/presentation.C3Wa0mjp.js" component-export="VMarkBlogRenderer" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;containerSelector&quot;:[0,&quot;#article&quot;],&quot;class&quot;:[0,&quot;astro-vj4tpspi&quot;]}" ssr client="only" opts="{&quot;name&quot;:&quot;VMarkBlogRenderer&quot;,&quot;value&quot;:&quot;react&quot;}"></astro-island> <!-- Fullscreen Modal Container using native dialog --><dialog id="mermaid-modal" class="mermaid-modal" aria-label="Fullscreen diagram view"> <div class="mermaid-modal-content"> <button class="mermaid-modal-close" aria-label="Close fullscreen view" type="button"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <line x1="18" y1="6" x2="6" y2="18"></line> <line x1="6" y1="6" x2="18" y2="18"></line> </svg> </button> <div class="mermaid-modal-diagram"></div> <div class="mermaid-modal-hint">Press <kbd>Esc</kbd> or click outside to close</div> </div> </dialog>  <script type="module">const p=new Set;function g(){const e=document.getElementById("mermaid-modal"),c=e?.querySelector(".mermaid-modal-diagram"),f=e?.querySelector(".mermaid-modal-close");if(!e||!c)return;document.querySelectorAll('svg[id^="mermaid-"]').forEach(t=>{if(!t.id.match(/^mermaid-\d+$/)||p.has(t.id)||t.parentElement?.classList.contains("mermaid-fullscreen-wrapper")||t.closest(".mermaid-modal"))return;p.add(t.id);const n=document.createElement("div");n.className="mermaid-fullscreen-wrapper mermaid-clickable",n.setAttribute("tabindex","0"),n.setAttribute("role","button"),n.setAttribute("aria-label","Click to view diagram fullscreen"),t.parentElement?.insertBefore(n,t),n.appendChild(t);const o=document.createElement("div");o.className="mermaid-expand-icon",o.innerHTML=`
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
</li> <li class="astro-vj4tpspi">Small tips and trick</li> </ul> </div> <a href="https://alex-op-newsletter.beehiiv.com/subscribe?utm_source=blog&utm_medium=post&utm_campaign=post_mastering-graphql-fragments-vue3-component-driven-data-fetching" target="_blank" rel="noopener noreferrer" id="newsletter-subscribe-button" class="inline-flex items-center justify-center gap-2 rounded-full bg-skin-accent px-6 py-3 text-base font-semibold text-skin-inverted shadow-md transition-all duration-200 hover:scale-[1.02] hover:transform hover:opacity-90 astro-vj4tpspi"> <svg class="h-5 w-5 fill-current astro-vj4tpspi" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg>
Subscribe Now
</a> <button id="newsletter-dismiss" data-post-slug="mastering-graphql-fragments-vue3-component-driven-data-fetching" class="absolute right-3 top-3 rounded-full p-1 text-skin-base transition-all duration-200 hover:bg-skin-accent hover:bg-opacity-10 hover:text-skin-accent astro-vj4tpspi" aria-label="Close notification"> <svg class="h-5 w-5 astro-vj4tpspi" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class="astro-vj4tpspi"></path> </svg> </button> </div> </div> </div> <ul class="my-8 flex flex-wrap gap-2 astro-vj4tpspi"> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/graphql/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-2"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">graphql</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/vue/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-3"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">vue</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/typescript/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-4"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">typescript</span>   </a> </li>  </ul> <div class="flex flex-col-reverse items-center justify-between gap-6 sm:flex-row-reverse sm:items-end sm:gap-4 astro-vj4tpspi"> <button id="back-to-top" class="focus-outline whitespace-nowrap py-1 hover:opacity-75 astro-vj4tpspi"> <svg xmlns="http://www.w3.org/2000/svg" class="rotate-90 astro-vj4tpspi"> <path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg> <span class="astro-vj4tpspi">Back to Top</span> </button> <div class="social-icons astro-wkojbtzc"> <span class="italic astro-wkojbtzc">Share this post on:</span> <div class="text-center astro-wkojbtzc"> <a href="https://wa.me/?text=https://alexop.dev/posts/mastering-graphql-fragments-vue3-component-driven-data-fetching/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via WhatsApp" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"></path>
      <path d="M9 10a0.5 .5 0 0 0 1 0v-1a0.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a0.5 .5 0 0 0 0 -1h-1a0.5 .5 0 0 0 0 1"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via WhatsApp</span> </a><a href="https://www.facebook.com/sharer.php?u=https://alexop.dev/posts/mastering-graphql-fragments-vue3-component-driven-data-fetching/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Facebook" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"
    ></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on Facebook</span> </a><a href="https://x.com/intent/tweet?url=https://alexop.dev/posts/mastering-graphql-fragments-vue3-component-driven-data-fetching/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Tweet this post" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Tweet this post</span> </a><a href="https://t.me/share/url?url=https://alexop.dev/posts/mastering-graphql-fragments-vue3-component-driven-data-fetching/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via Telegram" target="_blank" rel="noopener noreferrer"> <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon-tabler"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"></path>
      </svg> <span class="sr-only astro-wkojbtzc">Share this post via Telegram</span> </a><a href="https://pinterest.com/pin/create/button/?url=https://alexop.dev/posts/mastering-graphql-fragments-vue3-component-driven-data-fetching/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Pinterest" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <line x1="8" y1="20" x2="12" y2="11"></line>
      <path d="M10.7 14c.437 1.263 1.43 2 2.55 2c2.071 0 3.75 -1.554 3.75 -4a5 5 0 1 0 -9.7 1.7"></path>
      <circle cx="12" cy="12" r="9"></circle>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post on Pinterest</span> </a><a href="mailto:?subject=See%20this%20post&#38;body=https://alexop.dev/posts/mastering-graphql-fragments-vue3-component-driven-data-fetching/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via email" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via email</span> </a><a href="https://www.linkedin.com/shareArticle?mini=true&url=https://alexop.dev/posts/mastering-graphql-fragments-vue3-component-driven-data-fetching/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
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
</h2> <div class="md:grid-cols-3 grid grid-cols-1 gap-6 astro-vj4tpspi"> <a href="/posts/getting-started-graphql-vue3-apollo-typescript/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">Getting Started with GraphQL in Vue 3 — Complete Setup with Apollo</h3> <p class="related-post-description astro-vj4tpspi"> Part 1 of the Vue 3 + GraphQL series: a zero-to-hero guide for wiring up a Vue 3 app to a GraphQL API using the Composition API, Apollo Client, and Vite. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-04-26T00:00:00.000Z">Apr 26, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> graphql </span> </div> </div> </a><a href="/posts/type-safe-graphql-queries-vue3-codegen/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">Type-Safe GraphQL Queries in Vue 3 with GraphQL Code Generator</h3> <p class="related-post-description astro-vj4tpspi"> Part 2 of the Vue 3 + GraphQL series: generate fully-typed `useQuery` composables in Vue 3 with GraphQL Code Generator </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-05-04T00:00:00.000Z">May 4, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> graphql </span> </div> </div> </a><a href="/posts/the-problem-with-as-in-typescript-why-its-a-shortcut-we-should-avoid/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">The Problem with as in TypeScript: Why It&#39;s a Shortcut We Should Avoid</h3> <p class="related-post-description astro-vj4tpspi"> Learn why as can be a Problem in Typescript </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="italic text-sm">Updated:</span><span class="italic text-sm"><time dateTime="2024-09-29T15:22:00.000Z">Sep 29, 2024</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> typescript </span> </div> </div> </a> </div> </div> </main> <footer class="mt-auto astro-sz7xmlte"> <div class="max-w-5xl mx-auto px-4"> <hr class="border-skin-line" aria-hidden="true"> </div> <div class="footer-wrapper astro-sz7xmlte"> <div class="footer-content astro-sz7xmlte"> <div class="copyright-wrapper astro-sz7xmlte"> <span class="astro-sz7xmlte">Copyright &#169; 2026</span> <span class="separator astro-sz7xmlte">&nbsp;|&nbsp;</span> <span class="astro-sz7xmlte">All rights reserved.</span> </div> <div class="rss-prompt astro-sz7xmlte"> <a href="/rss.xml" class="rss-link group astro-sz7xmlte" title="Never miss a post - Subscribe via RSS" onclick="if (window.plausible) window.plausible('RSS Subscribe', { props: { location: 'footer' } })"> <div class="flex items-center gap-2 astro-sz7xmlte"> <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-skin-accent group-hover:animate-pulse astro-sz7xmlte"><path fill="currentColor" d="M19 20.001C19 11.729 12.271 5 4 5v2c7.168 0 13 5.832 13 13.001h2z" class="astro-sz7xmlte"></path><path fill="currentColor" d="M12 20.001h2C14 14.486 9.514 10 4 10v2c4.411 0 8 3.589 8 8.001z" class="astro-sz7xmlte"></path><circle cx="6" cy="18" r="2" fill="currentColor" class="astro-sz7xmlte"></circle> </svg> <span class="text-sm astro-sz7xmlte">Subscribe via RSS</span> </div> </a> </div> <div class="social-icons flex astro-upu6fzxr"> <a href="https://github.com/alexanderop" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title=" alexop.dev on Github" target="_blank" rel="noopener noreferrer"> <svg
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
    </script> </body> </html>  <script>(function(){const postSlug = "mastering-graphql-fragments-vue3-component-driven-data-fetching";

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